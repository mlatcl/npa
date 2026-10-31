"""Parse LyX 1.4 (format 245) into a block tree.

The tree is the source of truth for the later LaTeX and LaMD emitters.
Unknown insets are kept as raw text so conversion cannot silently drop them.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Iterator


HEADING_LAYOUTS = {
    "Title",
    "Author",
    "Date",
    "Chapter",
    "Chapter*",
    "Section",
    "Section*",
    "Subsection",
    "Subsection*",
    "Subsubsection",
    "Subsubsection*",
    "Paragraph",
    "Paragraph*",
    "Foilhead",
    "ShortFoilhead",
    "Left Header",
    "Right Header",
    "Right Footer",
    "My Logo",
}

LIST_LAYOUTS = {"Enumerate", "Itemize", "Description"}


@dataclass
class TextRun:
    text: str
    emph: bool = False
    bold: bool = False


@dataclass
class Formula:
    tex: str


@dataclass
class Command:
    raw: str


@dataclass
class Graphics:
    filename: str
    width: str | None = None


@dataclass
class Unhandled:
    kind: str
    text: str


Run = TextRun | Formula | Command | Graphics | Unhandled


@dataclass
class Paragraph:
    layout: str
    runs: list[Run] = field(default_factory=list)
    nested: list["Block"] = field(default_factory=list)


@dataclass
class Heading:
    layout: str
    runs: list[Run] = field(default_factory=list)


@dataclass
class Figure:
    filename: str
    width: str | None
    caption: list[Run]
    label: str | None = None


@dataclass
class Table:
    rows: list[list[list[Run]]]


@dataclass
class Answer:
    blocks: list["Block"]
    vspace: str = "0"


@dataclass
class Note:
    blocks: list["Block"]


@dataclass
class Footnote:
    blocks: list["Block"]


Block = Paragraph | Heading | Figure | Table | Answer | Note | Footnote | Formula


@dataclass
class Document:
    path: str
    textclass: str
    blocks: list[Block]
    warnings: list[str] = field(default_factory=list)


class Cursor:
    def __init__(self, lines: list[str]):
        self.lines = lines
        self.i = 0

    def peek(self) -> str | None:
        if self.i >= len(self.lines):
            return None
        return self.lines[self.i]

    def next(self) -> str | None:
        line = self.peek()
        if line is not None:
            self.i += 1
        return line

    def skip_blank(self) -> None:
        while self.peek() == "":
            self.next()


def _join_lyx_text(parts: list[str]) -> str:
    """Reassemble LyX's 80-column wraps without inserting mid-word spaces."""
    out = ""
    for part in parts:
        if not out:
            out = part
            continue
        if part.startswith((" ", "\t")):
            out += part
        elif out.endswith("-") and part[:1].islower():
            out = out[:-1] + part
        elif out.endswith((" ", "\t")):
            out += part
        elif part[:1].isalnum() and out[-1:].isalnum():
            out += part
        else:
            out += " " + part
    return out


def _apply_inset_space(text: str) -> str:
    return text.replace("InsetSpace ~", "~").replace("InsetSpace~", "~")


def parse_file(path: str | Path) -> Document:
    raw = Path(path).read_bytes()
    try:
        text = raw.decode("utf-8")
    except UnicodeDecodeError:
        text = raw.decode("latin-1")
    lines = text.splitlines()
    cur = Cursor(lines)
    textclass = "unknown"
    while cur.peek() is not None:
        line = cur.next()
        if line.startswith("\\textclass "):
            textclass = line.split(" ", 1)[1].strip()
        if line == "\\begin_body":
            break
    warnings: list[str] = []
    blocks = parse_blocks(cur, warnings, stop=lambda s: s == "\\end_body")
    blocks = promote_structural_headings(blocks)
    return Document(path=str(path), textclass=textclass, blocks=blocks, warnings=warnings)


STRUCTURAL_HEADINGS = {
    "Chapter",
    "Chapter*",
    "Section",
    "Section*",
    "Subsection",
    "Subsection*",
    "Subsubsection",
    "Subsubsection*",
    "Paragraph",
    "Paragraph*",
    "Foilhead",
    "ShortFoilhead",
}

FOIL_HEADINGS = {"Foilhead", "ShortFoilhead"}


def _is_foil_heading(block: Block) -> bool:
    return isinstance(block, Heading) and block.layout in FOIL_HEADINGS


def _split_at_foilheads(blocks: list[Block]) -> tuple[list[Block], list[Block]]:
    """Keep the preamble; lift overlay foilheads together with their bodies."""
    for i, block in enumerate(blocks):
        if _is_foil_heading(block):
            return blocks[:i], blocks[i:]
    return blocks, []


def promote_structural_headings(blocks: list[Block]) -> list[Block]:
    """Pull chapter/section/foil heads out of notes and unclosed \\begin_deeper nests.

    Overlay sequences live inside LyX Note insets as repeated ShortFoilhead
    layouts. Lift each foilhead *and* the blocks that follow it, otherwise the
    titles become empty pages and every overlay step piles onto the first foil.
    """
    out: list[Block] = []
    for block in blocks:
        if isinstance(block, Paragraph):
            nested = promote_structural_headings(block.nested)
            preamble, lifted = _split_at_foilheads(nested)
            kept: list[Block] = []
            promoted: list[Block] = []
            for child in preamble:
                if isinstance(child, Heading) and child.layout in STRUCTURAL_HEADINGS:
                    promoted.append(child)
                else:
                    kept.append(child)
            block.nested = kept
            out.append(block)
            out.extend(promoted)
            out.extend(lifted)
        elif isinstance(block, (Answer, Note, Footnote)):
            inner = promote_structural_headings(block.blocks)
            kept, lifted = _split_at_foilheads(inner)
            block.blocks = kept
            out.append(block)
            out.extend(lifted)
        else:
            out.append(block)
    return out


def parse_blocks(cur: Cursor, warnings: list[str], stop) -> list[Block]:
    blocks: list[Block] = []
    ancestor_ends = {"\\end_inset", "\\end_body", "\\end_deeper"}
    while cur.peek() is not None:
        line = cur.peek()
        if line is None or stop(line):
            if line is not None and stop(line) and line.startswith("\\end_"):
                cur.next()
            break
        if line in ancestor_ends and not stop(line):
            # Unclosed deeper/layout inside an inset: leave the end token
            # for the ancestor so later chapters are not swallowed.
            break
        if line.startswith("\\begin_layout "):
            layout = line[len("\\begin_layout ") :]
            cur.next()
            runs, nested = parse_layout_body(cur, warnings)
            if layout in HEADING_LAYOUTS:
                blocks.append(Heading(layout=layout, runs=runs))
                if nested:
                    blocks.extend(nested)
            else:
                blocks.append(Paragraph(layout=layout, runs=runs, nested=nested))
        elif line == "\\begin_deeper":
            cur.next()
            nested = parse_blocks(cur, warnings, stop=lambda s: s == "\\end_deeper")
            if blocks and isinstance(blocks[-1], Paragraph):
                blocks[-1].nested.extend(nested)
            else:
                blocks.extend(nested)
        elif line.startswith("\\begin_inset "):
            inset = parse_inset(cur, warnings)
            blocks.extend(_blocks_from_inset(inset, warnings))
        else:
            cur.next()
    return blocks


def parse_layout_body(cur: Cursor, warnings: list[str]) -> tuple[list[Run], list[Block]]:
    text_parts: list[str] = []
    runs: list[Run] = []
    nested: list[Block] = []
    emph = False
    bold = False

    def flush_text() -> None:
        nonlocal text_parts
        if not text_parts:
            return
        text = _apply_inset_space(_join_lyx_text(text_parts))
        text_parts = []
        if text:
            runs.append(TextRun(text=text, emph=emph, bold=bold))

    while cur.peek() is not None:
        line = cur.peek()
        if line == "\\end_layout":
            cur.next()
            break
        if line in {"\\end_deeper", "\\end_inset", "\\end_body", "\\end_document"}:
            break
        if line is not None and line.startswith("\\begin_layout "):
            break
        if line == "\\begin_deeper":
            flush_text()
            cur.next()
            nested.extend(parse_blocks(cur, warnings, stop=lambda s: s == "\\end_deeper"))
            continue
        if line is not None and line.startswith("\\begin_inset "):
            flush_text()
            inset = parse_inset(cur, warnings)
            extra = _runs_from_inset(inset, warnings)
            if extra:
                runs.extend(extra)
            else:
                nested.extend(_blocks_from_inset(inset, warnings))
            continue
        cur.next()
        if line is None:
            break
        stripped = line.strip()
        if stripped == "\\emph on":
            flush_text()
            emph = True
            continue
        if stripped == "\\emph default":
            flush_text()
            emph = False
            continue
        if stripped == "\\series bold":
            flush_text()
            bold = True
            continue
        if stripped == "\\series default":
            flush_text()
            bold = False
            continue
        if stripped.startswith("\\family ") or stripped.startswith("\\shape "):
            continue
        if stripped.startswith("\\size ") or stripped.startswith("\\align "):
            continue
        if stripped.startswith("\\bar ") or stripped.startswith("\\noun "):
            continue
        if stripped.startswith("\\color "):
            continue
        if stripped == "\\noindent":
            continue
        if stripped.startswith("\\start_of_appendix"):
            continue
        if stripped.startswith("\\"):
            if stripped.startswith("\\backslash"):
                text_parts.append("\\")
            elif stripped.startswith("\\InsetSpace"):
                text_parts.append("~")
            elif stripped in {"\\hfill", "\\hfill{}"}:
                text_parts.append(" ")
            elif stripped.startswith("\\newline"):
                text_parts.append("\n")
            else:
                warnings.append(f"layout command kept as text: {stripped}")
                text_parts.append(stripped)
            continue
        text_parts.append(line)
    flush_text()
    return runs, nested


def parse_inset(cur: Cursor, warnings: list[str]):
    header = cur.next() or ""
    kind = header[len("\\begin_inset ") :]
    if kind.startswith("Formula"):
        rest = kind[len("Formula") :].lstrip()
        body_lines: list[str] = []
        if rest:
            body_lines.append(rest)
        while cur.peek() is not None and cur.peek() != "\\end_inset":
            body_lines.append(cur.next() or "")
        if cur.peek() == "\\end_inset":
            cur.next()
        tex = "\n".join(body_lines).strip()
        return Formula(tex=tex)
    if kind.startswith("LatexCommand "):
        raw = kind[len("LatexCommand ") :].strip()
        while cur.peek() is not None and cur.peek() != "\\end_inset":
            extra = cur.next() or ""
            if extra.strip():
                raw += extra.strip()
        if cur.peek() == "\\end_inset":
            cur.next()
        return Command(raw=raw)
    if kind.startswith("Graphics"):
        filename = ""
        width = None
        while cur.peek() is not None and cur.peek() != "\\end_inset":
            line = cur.next() or ""
            s = line.strip()
            if s.startswith("filename "):
                filename = s.split(" ", 1)[1].strip()
            elif s.startswith("width "):
                width = s.split(" ", 1)[1].strip()
        if cur.peek() == "\\end_inset":
            cur.next()
        return Graphics(filename=filename, width=width)
    if kind.startswith("ERT"):
        return _parse_ert(cur, warnings)
    if kind.startswith("Float "):
        return _parse_float(cur, kind, warnings)
    if kind.startswith("Tabular"):
        return _parse_tabular(cur, warnings)
    if kind.startswith("Note "):
        inner = _parse_inset_blocks(cur, warnings)
        return Note(blocks=inner)
    if kind.startswith("Foot"):
        inner = _parse_inset_blocks(cur, warnings)
        return Footnote(blocks=inner)
    if kind.startswith("Box "):
        return _parse_inset_blocks(cur, warnings)
    if kind.startswith("Text"):
        return _parse_inset_blocks(cur, warnings)
    if kind.startswith("Caption"):
        return _parse_inset_blocks(cur, warnings)
    # Skip the rest of an unknown inset but keep its text.
    raw_lines: list[str] = []
    depth = 1
    while cur.peek() is not None and depth:
        line = cur.next() or ""
        if line.startswith("\\begin_inset "):
            depth += 1
        if line == "\\end_inset":
            depth -= 1
            if depth == 0:
                break
        raw_lines.append(line)
    warnings.append(f"unhandled inset: {kind.split()[0]}")
    return Unhandled(kind=kind, text="\n".join(raw_lines))


def _parse_inset_blocks(cur: Cursor, warnings: list[str]) -> list[Block]:
    # Consume status / collapsed lines then nested layouts.
    while cur.peek() is not None and not cur.peek().startswith("\\begin_") and cur.peek() != "\\end_inset":
        cur.next()
    blocks = parse_blocks(cur, warnings, stop=lambda s: s == "\\end_inset")
    return blocks


def _parse_ert(cur: Cursor, warnings: list[str]) -> Command:
    while cur.peek() is not None and not cur.peek().startswith("\\begin_layout") and cur.peek() != "\\end_inset":
        cur.next()
    chunks: list[str] = []
    while cur.peek() is not None and cur.peek() != "\\end_inset":
        line = cur.next() or ""
        if line.startswith("\\begin_layout "):
            continue
        if line == "\\end_layout":
            continue
        if line.strip() == "\\backslash":
            nxt = cur.peek()
            if nxt is None:
                chunks.append("\\")
            else:
                cur.next()
                chunks.append("\\" + (nxt or "").lstrip())
            continue
        chunks.append(line)
    if cur.peek() == "\\end_inset":
        cur.next()
    return Command(raw="".join(chunks).strip())


def _parse_float(cur: Cursor, kind: str, warnings: list[str]) -> Figure | Table | Unhandled:
    inner = _parse_inset_blocks(cur, warnings)
    filename = ""
    width = None
    caption: list[Run] = []
    label = None
    for block in inner:
        if isinstance(block, Paragraph):
            for run in block.runs:
                if isinstance(run, Graphics):
                    filename = run.filename
                    width = run.width
                elif isinstance(run, Command) and run.raw.startswith("\\label"):
                    label = run.raw[len("\\label") :].strip().strip("{}")
                else:
                    caption.append(run)
            for nested in block.nested:
                if isinstance(nested, Paragraph):
                    caption.extend(nested.runs)
        elif isinstance(block, Figure):
            return block
        elif isinstance(block, Table):
            return block
    if "table" in kind.lower() and not filename:
        return Table(rows=[])
    return Figure(filename=filename, width=width, caption=caption, label=label)


def _parse_tabular(cur: Cursor, warnings: list[str]) -> Table:
    rows: list[list[list[Run]]] = []
    current_row: list[list[Run]] = []
    while cur.peek() is not None and cur.peek() != "\\end_inset":
        line = cur.peek() or ""
        if line.startswith("\\begin_inset Text"):
            inner = parse_inset(cur, warnings)
            cell_runs: list[Run] = []
            if isinstance(inner, list):
                for block in inner:
                    if isinstance(block, Paragraph):
                        cell_runs.extend(block.runs)
                    elif isinstance(block, Heading):
                        cell_runs.extend(block.runs)
            elif isinstance(inner, Paragraph):
                cell_runs.extend(inner.runs)
            else:
                extra = _runs_from_inset(inner, warnings)
                cell_runs.extend(extra)
            current_row.append(cell_runs)
            continue
        cur.next()
        if "<row" in line and current_row:
            rows.append(current_row)
            current_row = []
        if line.strip() == "</row>" and current_row:
            rows.append(current_row)
            current_row = []
    if current_row:
        rows.append(current_row)
    if cur.peek() == "\\end_inset":
        cur.next()
    return Table(rows=rows)


def _runs_from_inset(inset, warnings: list[str]) -> list[Run]:
    if isinstance(inset, (Formula, Command, Graphics, Unhandled, TextRun)):
        return [inset]
    return []


def _blocks_from_inset(inset, warnings: list[str]) -> list[Block]:
    if isinstance(inset, list):
        return list(inset)
    if isinstance(inset, (Figure, Table, Note, Footnote, Answer, Formula)):
        return [inset]
    if isinstance(inset, Paragraph):
        return [inset]
    if isinstance(inset, Heading):
        return [inset]
    if isinstance(inset, Unhandled):
        return [Paragraph(layout="Standard", runs=[inset])]
    if isinstance(inset, (Command, Graphics, TextRun)):
        return [Paragraph(layout="Standard", runs=[inset])]
    return []


def iter_runs(blocks: list[Block]) -> Iterator[Run]:
    for block in blocks:
        if isinstance(block, (Paragraph, Heading)):
            yield from block.runs
            if isinstance(block, Paragraph):
                yield from iter_runs(block.nested)
        elif isinstance(block, Figure):
            yield Graphics(filename=block.filename, width=block.width)
            yield from block.caption
        elif isinstance(block, Table):
            for row in block.rows:
                for cell in row:
                    yield from cell
        elif isinstance(block, (Answer, Note, Footnote)):
            yield from iter_runs(block.blocks)
        elif isinstance(block, Formula):
            yield block


def plain_text(runs: list[Run]) -> str:
    parts: list[str] = []
    for run in runs:
        if isinstance(run, TextRun):
            parts.append(run.text)
        elif isinstance(run, Formula):
            parts.append(run.tex)
        elif isinstance(run, Command):
            parts.append(run.raw)
        elif isinstance(run, Graphics):
            parts.append(run.filename)
        elif isinstance(run, Unhandled):
            parts.append(run.text)
    return " ".join(p for p in parts if p)


def group_answers(blocks: list[Block]) -> list[Block]:
    """Turn split ERT \\answer{ ... }{n} pairs into Answer blocks."""
    out: list[Block] = []
    i = 0
    while i < len(blocks):
        block = blocks[i]
        if _is_answer_open(block):
            inner: list[Block] = []
            i += 1
            vspace = "0"
            while i < len(blocks):
                if _is_answer_close(blocks[i]):
                    vspace = _answer_vspace(blocks[i])
                    i += 1
                    break
                if _is_foil_heading(blocks[i]):
                    break
                inner.append(blocks[i])
                i += 1
            out.append(Answer(blocks=group_answers(inner), vspace=vspace))
            continue
        if isinstance(block, Paragraph) and block.nested:
            block.nested = group_answers(block.nested)
        out.append(block)
        i += 1
    return out


def _is_answer_open(block: Block) -> bool:
    if not isinstance(block, Paragraph):
        return False
    text = plain_text(block.runs).strip()
    return text.startswith("\\answer{") and not text.endswith("}")


def _is_answer_close(block: Block) -> bool:
    if not isinstance(block, Paragraph):
        return False
    text = plain_text(block.runs).strip()
    return text.startswith("}{") or text == "}"


def _answer_vspace(block: Block) -> str:
    text = plain_text(block.runs).strip()
    if text.startswith("}{") and text.endswith("}"):
        return text[2:-1]
    return "0"
