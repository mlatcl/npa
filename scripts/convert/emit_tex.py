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
    # Keep ~ as a non-breaking space (LyX InsetSpace). Replacing it with a
    # normal space turned "Lab~Classes" into a description label "Lab" and a
    # body starting with "Classes", and a following ] became the TeX closer \].
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
        raw = run.raw.strip()
        if raw in {"~", "\\~"}:
            return "~"
        if not raw.startswith("\\"):
            raw = "\\" + raw
        return raw
    if isinstance(run, Graphics):
        return include_graphics(run.filename, run.width)
    if isinstance(run, Unhandled):
        return f"% unhandled {run.kind}\n{run.text}\n"
    return ""


# 2006 FoilTeX logos lived on the lecturer machine; map to copies in this repo.
LOGO_MAP = {
    "sheffieldlogo.eps": "sheffield-lockup-2005.png",
    "sheffieldlogo": "sheffield-lockup-2005.png",
}


GRAPHIC_DIRS = [
    Path("slides") / "diagrams" / "npa",
    Path("slides") / "diagrams" / "logos",
    Path("diagrams"),
    Path("."),
]


def _prefer_printable(name: str) -> str:
    """pdflatex+epstopdf fails when .eps is not on the TeX search path."""
    root = Path(__file__).resolve().parents[2]
    mapped = LOGO_MAP.get(name, name)
    base = Path(mapped).stem
    for directory in [root / rel for rel in GRAPHIC_DIRS]:
        for ext in (".png", ".pdf", ".jpg"):
            candidate = directory / f"{base}{ext}"
            if candidate.is_file():
                return candidate.name
        for ext in (".eps", ".EPS"):
            candidate = directory / f"{base}{ext}"
            if candidate.is_file():
                return candidate.name
    return mapped


def include_graphics(filename: str, width: str | None) -> str:
    if not (filename or "").strip():
        return ""
    stem = _prefer_printable(Path(filename).name)
    frac = width_to_frac(width) if width else None
    w = f"{frac}\\linewidth" if frac else "\\linewidth"
    # EPS distilled without -dEPSCrop becomes a full Letter page; cap height.
    return (
        f"\\includegraphics[width={w},height=0.45\\textheight,"
        f"keepaspectratio]{{{stem}}}"
    )


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


def description_item(body: str) -> tuple[str, str]:
    """LyX description labels use InsetSpace (~) to include extra words."""
    body = body.replace("\\~", "~").replace("\n", " ")
    parts = body.split()
    if not parts:
        return "", ""
    if parts[0].endswith("~") and len(parts) > 1:
        label = parts[0][:-1] + "~" + parts[1]
        return label, " ".join(parts[2:])
    return parts[0], " ".join(parts[1:])


def emit_list(items: list[Paragraph], indent: str) -> str:
    env = {"Enumerate": "enumerate", "Itemize": "itemize", "Description": "description"}[
        items[0].layout
    ]
    lines = [f"{indent}\\begin{{{env}}}"]
    for item in items:
        body = emit_runs(item.runs).strip()
        if items[0].layout == "Description" and " " in body:
            label, rest = description_item(body)
            lines.append(f"{indent}  \\item[{{{label}}}] {rest}")
        else:
            lines.append(f"{indent}  \\item {body}")
        if item.nested:
            nested = emit_blocks(item.nested, indent + "  ")
            if nested:
                lines.append(nested)
    lines.append(f"{indent}\\end{{{env}}}")
    return "\n".join(lines)


_SIZE_CMD = re.compile(
    r"\\(?:tiny|scriptsize|footnotesize|small|normalsize|large|Large|LARGE|huge|Huge)\b"
)


def _is_size_only(body: str) -> bool:
    stripped = _SIZE_CMD.sub("", body)
    return bool(body) and not stripped.strip()


def _split_size_wrap(body: str) -> tuple[str, str]:
    """LyX ERT \\tiny / \\normalsize arrive as runs; the table is nested."""
    cmds = _SIZE_CMD.findall(body)
    opens = [c for c in cmds if c != r"\normalsize"]
    closes = [c for c in cmds if c == r"\normalsize"]
    before = "".join(opens) or body
    after = "".join(closes) or (r"\normalsize" if opens else "")
    return before, after


FOIL_CHROME = {
    "Left Header": "leftheader",
    "Right Header": "rightheader",
    "Right Footer": "rightfooter",
    "My Logo": "MyLogo",
}


def emit_block(block: Block, indent: str = "") -> str:
    if isinstance(block, Heading):
        title = emit_runs(block.runs).strip()
        if block.layout == "My Logo":
            return (
                f"{indent}\\MyLogo{{\\includegraphics[height=1.2cm]"
                f"{{sheffield-lockup-2005.png}}}}"
            )
        if block.layout == "Right Footer":
            return (
                f"{indent}\\rightfooter{{\\includegraphics[height=1cm]"
                f"{{dcslogo.pdf}}\\quad\\thepage}}"
            )
        if block.layout in FOIL_CHROME:
            return f"{indent}\\{FOIL_CHROME[block.layout]}{{{title}}}"
        macro, starred = heading_macro(block.layout)
        star = "*" if starred else ""
        if macro in {"title", "author", "date"}:
            return f"{indent}\\{macro}{{{title}}}"
        if macro == "foilhead":
            # Match the 2006 LyX export: tighten the gap above the foil title.
            return f"{indent}\\foilhead[-0.5in]{{{title}}}"
        return f"{indent}\\{macro}{star}{{{title}}}"
    if isinstance(block, Paragraph):
        body = emit_runs(block.runs).strip()
        nested = emit_blocks(block.nested, indent) if block.nested else ""
        if block.layout == "Caption":
            return f"{indent}\\caption{{{body}}}\n{nested}".rstrip()
        if nested and _is_size_only(body):
            before, after = _split_size_wrap(body)
            return "\n".join(p for p in (f"{indent}{before}", nested, f"{indent}{after}") if p)
        parts = [f"{indent}{body}"] if body else []
        if nested:
            parts.append(nested)
        return "\n".join(parts)
    if isinstance(block, Figure):
        cap = emit_runs(block.caption).strip()
        inc = include_graphics(block.filename, block.width)
        if not inc:
            # LyX caption-only floats (no Graphics inset) must not emit
            # \\includegraphics{}. Keep the caption as ordinary text.
            return f"{indent}{cap}" if cap else ""
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
        if not inner.strip():
            return ""
        return f"{indent}\\begin{{lyxnote}}\n{inner}\n{indent}\\end{{lyxnote}}"
    if isinstance(block, Footnote):
        inner = emit_blocks(block.blocks, "").replace("\n", " ")
        return f"{indent}\\footnote{{{inner.strip()}}}"
    if isinstance(block, Formula):
        return f"{indent}{block.tex}"
    return ""


def _escape_cell_amps(text: str) -> str:
    """LyX cells contain literal '&' ('Lectures 1 & 2'); those are not columns."""
    return text.replace("\\&", "&").replace("&", r"\&")


def emit_table(table: Table, indent: str) -> str:
    if not table.rows:
        return f"{indent}% empty table"
    cols = max((len(r) for r in table.rows), default=1)
    spec = "l" * cols
    lines = [f"{indent}\\begin{{tabular}}{{{spec}}}"]
    for row in table.rows:
        cells = [_escape_cell_amps(emit_runs(cell).strip()) for cell in row]
        while len(cells) < cols:
            cells.append("")
        lines.append(indent + "  " + " & ".join(cells) + " \\\\")
    lines.append(f"{indent}\\end{{tabular}}")
    return "\n".join(lines)


# LyX Note insets are speaker cribs (not exported by LyX). Keep the
# environment in the .tex so LaMD can map it to \\speakernotes, but do not
# typeset it. \\answer matches notes.cls: lecturer prints the body, student
# option (\\answerfalse) leaves \\vspace*{#1cm}.
_NOTE_ANSWER_ENVS = """\
\\newif\\ifanswer\\answertrue
\\newenvironment{lyxnote}{\\setbox0\\vbox\\bgroup}{\\egroup}
\\newenvironment{answer}[1][0]{%
  \\def\\npaanswervspace{#1}%
  \\ifanswer\\par\\else\\setbox0\\vbox\\bgroup\\fi
}{%
  \\ifanswer\\par\\else\\egroup\\vspace*{\\npaanswervspace cm}\\fi
}
"""

ARTICLE_PREAMBLE = (
    """\
\\documentclass{article}
\\usepackage[utf8]{inputenc}
\\usepackage{amsmath,amssymb,graphicx}
\\usepackage[authoryear]{natbib}
"""
    + _NOTE_ANSWER_ENVS
    + """\
\\providecommand{\\foilhead}[1]{\\section{#1}}
"""
)

# Portrait Letter, 20pt sans, matching lectureSlides.lyx (\\options 20pt and
# \\paperorientation portrait). Do not pass dvips: we compile with pdflatex.
# foils.cls is not in TeX Live; compile_foils.py puts CTAN FoilTeX on TEXINPUTS.
FOILS_PREAMBLE = (
    """\
\\documentclass[20pt,letterpaper]{foils}
\\usepackage[T1]{fontenc}
\\usepackage[utf8]{inputenc}
\\usepackage{amsmath,amssymb,graphicx,pifont,url,color}
\\usepackage[authoryear]{natbib}
\\graphicspath{{../../diagrams/}{diagrams/}{../../}{../../slides/diagrams/npa/}{slides/diagrams/npa/}{../../slides/diagrams/logos/}{slides/diagrams/logos/}}
\\providecommand{\\tabularnewline}{\\\\}
\\newcommand{\\lyxdot}{.}
"""
    + _NOTE_ANSWER_ENVS
    + """\
\\AtBeginDocument{%
  \\def\\labelitemi{\\ding{122}}%
  \\def\\labelitemii{\\ding{229}}%
  \\renewcommand{\\bibsection}{\\foilhead[-0.5in]{\\refname}}%
}
\\newcounter{npafoil}
\\makeatletter
\\let\\npa@oldfoilhead\\foilhead
\\renewcommand{\\foilhead}[2][-0.5in]{%
  \\npa@oldfoilhead[#1]{#2}%
  \\stepcounter{npafoil}%
  \\typeout{NPAFOIL \\thenpafoil\\space PAGE \\thepage}%
}
\\makeatother
"""
)


_ALIGN_ENVS = {
    "tabular",
    "array",
    "align",
    "align*",
    "aligned",
    "eqnarray",
    "eqnarray*",
    "cases",
    "matrix",
    "pmatrix",
    "bmatrix",
    "vmatrix",
    "split",
}


def escape_bare_ampersands(text: str) -> str:
    """Turn literal '&' into '\\&' outside alignment environments."""
    out: list[str] = []
    i = 0
    n = len(text)
    depth = 0
    begin_re = re.compile(r"\\begin\{([^}]+)\}")
    end_re = re.compile(r"\\end\{([^}]+)\}")
    while i < n:
        if text.startswith(r"\&", i):
            out.append(r"\&")
            i += 2
            continue
        m = begin_re.match(text, i)
        if m:
            out.append(m.group(0))
            if m.group(1) in _ALIGN_ENVS:
                depth += 1
            i = m.end()
            continue
        m = end_re.match(text, i)
        if m:
            out.append(m.group(0))
            if m.group(1) in _ALIGN_ENVS and depth:
                depth -= 1
            i = m.end()
            continue
        if text[i] == "&" and depth == 0:
            out.append(r"\&")
            i += 1
            continue
        out.append(text[i])
        i += 1
    return "".join(out)


def _expand_bibtex(text: str) -> str:
    """LyX \\bibtex[style]{files} is \\bibliographystyle + \\bibliography.

    The .bib files live in the publications tree (BIBINPUTS / ~lawrennd/publications).
    """

    def repl(match: re.Match[str]) -> str:
        style = match.group(1) or "abbrvnat"
        files = match.group(2)
        return f"\\bibliographystyle{{{style}}}\n\\bibliography{{{files}}}"

    return re.sub(r"\\bibtex(?:\[([^\]]*)\])?\{([^}]+)\}", repl, text)


def _sanitize_foils_body(body: str) -> str:
    """Keep FoilTeX compiling: LyX leftovers that are fatal in \\foilhead."""
    from emit_lamd import (
        fix_cases_arrays,
        repair_fracs,
        strip_answer_macros,
        strip_figure_chrome,
    )

    body = body.replace("\\~", "~")
    body = strip_answer_macros(strip_figure_chrome(body))
    body = fix_cases_arrays(body)
    body = repair_fracs(body)
    body = _expand_bibtex(body)
    return escape_bare_ampersands(body)


def _insert_maketitle(body: str) -> str:
    """FoilTeX needs \\maketitle after \\title/\\author/\\date for the title foil."""
    if r"\maketitle" in body:
        return body
    for macro in (r"\date{", r"\author{", r"\title{"):
        i = body.find(macro)
        if i < 0:
            continue
        nl = body.find("\n", i)
        if nl < 0:
            return body + "\n\\maketitle\n"
        return body[: nl + 1] + "\\maketitle\n" + body[nl + 1 :]
    return "\\maketitle\n" + body


def document_to_tex(doc: Document) -> str:
    blocks = group_answers(doc.blocks)
    body = emit_blocks(blocks)
    foils = doc.textclass == "foils"
    if foils:
        body = _sanitize_foils_body(body)
        body = _insert_maketitle(body)
        preamble = FOILS_PREAMBLE
    else:
        preamble = ARTICLE_PREAMBLE
    return (
        f"% Generated from {doc.path}. Do not edit; regenerate with scripts/convert/run.py.\n"
        f"{preamble}"
        "\\begin{document}\n\n"
        f"{body}\n"
        "\\end{document}\n"
    )


def write_tex(doc: Document, dest: str | Path) -> Path:
    dest = Path(dest)
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(document_to_tex(doc), encoding="utf-8")
    return dest
