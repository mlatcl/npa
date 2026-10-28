"""Emit inspectable LaTeX from a LyX 1.4 document tree."""

from __future__ import annotations

import re
from pathlib import Path

from lyx14 import (
    LIST_LAYOUTS,
    Answer,
    Block,
    Command,
    Document,
    Figure,
    Footnote,
    Formula,
    Graphics,
    Heading,
    Note,
    Paragraph,
    Run,
    Table,
    TextRun,
    Unhandled,
    group_answers,
    plain_text,
)


def escape_text(text: str) -> str:
    text = text.replace("~", " ")
    # LyX already stored most special chars; keep TeX specials that arrived as text.
    return text


def run_to_tex(run: Run) -> str:
    if isinstance(run, TextRun):
        text = escape_text(run.text)
        if run.bold:
            text = f"\\textbf{{{text}}}"
        if run.emph:
            text = f"\\emph{{{text}}}"
        return text
    if isinstance(run, Formula):
        return run.tex
    if isinstance(run, Command):
        raw = run.raw
        if not raw.startswith("\\"):
            raw = "\\" + raw
        return raw
    if isinstance(run, Graphics):
        return include_graphics(run.filename, run.width)
    if isinstance(run, Unhandled):
        return f"% unhandled {run.kind}\n{run.text}\n"
    return ""


def include_graphics(filename: str, width: str | None) -> str:
    stem = Path(filename).name
    option = ""
    if width:
        frac = width_to_frac(width)
        if frac:
            option = f"[width={frac}\\textwidth]"
    return f"\\includegraphics{option}{{{stem}}}"


def width_to_frac(width: str) -> str | None:
    # "100text%" / "80text%" / "4cm"
    m = re.search(r"(\d+)\s*text%", width)
    if m:
        return f"{int(m.group(1)) / 100:.2f}".rstrip("0").rstrip(".")
    return None


def heading_macro(layout: str) -> tuple[str, bool]:
    starred = layout.endswith("*")
    name = layout.rstrip("*").lower().replace(" ", "")
    mapping = {
        "title": "title",
        "author": "author",
        "date": "date",
        "chapter": "chapter",
        "section": "section",
        "subsection": "subsection",
        "subsubsection": "subsubsection",
        "paragraph": "paragraph",
        "foilhead": "foilhead",
        "shortfoilhead": "foilhead",
    }
    return mapping.get(name, "section"), starred


def emit_runs(runs: list[Run]) -> str:
    return "".join(run_to_tex(r) for r in runs)


def emit_blocks(blocks: list[Block], indent: str = "") -> str:
    parts: list[str] = []
    i = 0
    while i < len(blocks):
        block = blocks[i]
        if isinstance(block, Paragraph) and block.layout in LIST_LAYOUTS:
            group, i = collect_list(blocks, i)
            parts.append(emit_list(group, indent))
            continue
        parts.append(emit_block(block, indent))
        i += 1
    return "\n".join(p for p in parts if p)


def collect_list(blocks: list[Block], i: int) -> tuple[list[Paragraph], int]:
    layout = blocks[i].layout  # type: ignore[union-attr]
    group: list[Paragraph] = []
    while i < len(blocks) and isinstance(blocks[i], Paragraph) and blocks[i].layout == layout:
        group.append(blocks[i])  # type: ignore[arg-type]
        i += 1
    return group, i


def emit_list(items: list[Paragraph], indent: str) -> str:
    env = {"Enumerate": "enumerate", "Itemize": "itemize", "Description": "description"}[
        items[0].layout
    ]
    lines = [f"{indent}\\begin{{{env}}}"]
    for item in items:
        body = emit_runs(item.runs).strip()
        if items[0].layout == "Description" and " " in body:
            label, rest = body.split(" ", 1)
            lines.append(f"{indent}  \\item[{label}] {rest}")
        else:
            lines.append(f"{indent}  \\item {body}")
        if item.nested:
            nested = emit_blocks(item.nested, indent + "  ")
            if nested:
                lines.append(nested)
    lines.append(f"{indent}\\end{{{env}}}")
    return "\n".join(lines)


def emit_block(block: Block, indent: str = "") -> str:
    if isinstance(block, Heading):
        if block.layout in {"Left Header", "Right Header", "Right Footer", "My Logo"}:
            return ""
        macro, starred = heading_macro(block.layout)
        star = "*" if starred else ""
        title = emit_runs(block.runs).strip()
        if macro in {"title", "author", "date"}:
            return f"{indent}\\{macro}{{{title}}}"
        return f"{indent}\\{macro}{star}{{{title}}}"
    if isinstance(block, Paragraph):
        body = emit_runs(block.runs).strip()
        nested = emit_blocks(block.nested, indent) if block.nested else ""
        if block.layout == "Caption":
            return f"{indent}\\caption{{{body}}}\n{nested}".rstrip()
        parts = [f"{indent}{body}"] if body else []
        if nested:
            parts.append(nested)
        return "\n".join(parts)
    if isinstance(block, Figure):
        cap = emit_runs(block.caption).strip()
        inc = include_graphics(block.filename, block.width)
        lines = [f"{indent}\\begin{{figure}}[ht]", f"{indent}  \\centering", f"{indent}  {inc}"]
        if cap:
            lines.append(f"{indent}  \\caption{{{cap}}}")
        if block.label:
            lines.append(f"{indent}  \\label{{{block.label}}}")
        lines.append(f"{indent}\\end{{figure}}")
        return "\n".join(lines)
    if isinstance(block, Table):
        return emit_table(block, indent)
    if isinstance(block, Answer):
        inner = emit_blocks(block.blocks, indent + "  ")
        return f"{indent}\\begin{{answer}}[{block.vspace}]\n{inner}\n{indent}\\end{{answer}}"
    if isinstance(block, Note):
        inner = emit_blocks(block.blocks, indent + "  ")
        return f"{indent}\\begin{{lyxnote}}\n{inner}\n{indent}\\end{{lyxnote}}"
    if isinstance(block, Footnote):
        inner = emit_blocks(block.blocks, "").replace("\n", " ")
        return f"{indent}\\footnote{{{inner.strip()}}}"
    if isinstance(block, Formula):
        return f"{indent}{block.tex}"
    return ""


def emit_table(table: Table, indent: str) -> str:
    if not table.rows:
        return f"{indent}% empty table"
    cols = max((len(r) for r in table.rows), default=1)
    spec = "l" * cols
    lines = [f"{indent}\\begin{{tabular}}{{{spec}}}"]
    for row in table.rows:
        cells = [emit_runs(cell).strip() for cell in row]
        while len(cells) < cols:
            cells.append("")
        lines.append(indent + "  " + " & ".join(cells) + " \\\\")
    lines.append(f"{indent}\\end{{tabular}}")
    return "\n".join(lines)


def document_to_tex(doc: Document) -> str:
    blocks = group_answers(doc.blocks)
    body = emit_blocks(blocks)
    cls = "foils" if doc.textclass == "foils" else "article"
    return (
        f"% Generated from {doc.path}. Do not edit; regenerate with scripts/convert/run.py.\n"
        f"\\documentclass{{{cls}}}\n"
        "\\usepackage[utf8]{inputenc}\n"
        "\\usepackage{amsmath,amssymb,graphicx}\n"
        "\\usepackage[authoryear]{natbib}\n"
        "\\newif\\ifanswer\\answertrue\n"
        "\\newenvironment{answer}[1][0]{\\par\\textbf{Answer.}\\par}{\\par}\n"
        "\\newenvironment{lyxnote}{\\par\\textit{Note.}\\par}{\\par}\n"
        "\\providecommand{\\foilhead}[1]{\\section{#1}}\n"
        "\\begin{document}\n\n"
        f"{body}\n"
        "\\end{document}\n"
    )


def write_tex(doc: Document, dest: str | Path) -> Path:
    dest = Path(dest)
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(document_to_tex(doc), encoding="utf-8")
    return dest
