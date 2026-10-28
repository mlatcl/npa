"""Convert the generated conversion LaTeX into LaMD notes and slides.

Notes and slides are emitted as separate snippet files. Each original A4 foil
becomes two Reveal slides unless it is already short or is one frame of a
same-title overlay sequence.
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from pathlib import Path


def _macro_arg(line: str, names: tuple[str, ...]) -> tuple[str, str, bool] | None:
    """Return (name, argument, starred) for a one-argument TeX macro at line start."""
    s = line.strip()
    for name in names:
        prefix = "\\" + name
        if not s.startswith(prefix):
            continue
        rest = s[len(prefix) :]
        starred = rest.startswith("*")
        if starred:
            rest = rest[1:]
        if not rest.startswith("{"):
            return None
        depth = 0
        for i, ch in enumerate(rest):
            if ch == "{":
                depth += 1
            elif ch == "}":
                depth -= 1
                if depth == 0:
                    return name, rest[1:i], starred
        return name, rest[1:], starred
    return None
BEGIN_ENV_RE = re.compile(r"^\\begin\{([a-zA-Z*]+)\}(?:\[(.*)\])?")
END_ENV_RE = re.compile(r"^\\end\{([a-zA-Z*]+)\}")
GRAPHICS_RE = re.compile(
    r"\\includegraphics(?:\[width=([0-9.]+)\\textwidth\])?\{([^}]+)\}"
)


def strip_tex(text: str) -> str:
    text = re.sub(r"%.*", "", text)
    return text.strip()


def latex_inline_to_md(text: str) -> str:
    """Keep math; turn a few text macros into markdown."""
    text = re.sub(r"\\emph\{([^{}]*)\}", lambda m: f"*{m.group(1).strip()}*", text)
    text = re.sub(r"\\textbf\{([^{}]*)\}", lambda m: f"**{m.group(1).strip()}**", text)
    text = re.sub(r"\\textit\{([^{}]*)\}", lambda m: f"*{m.group(1).strip()}*", text)
    text = re.sub(r"\\citeauthor\{([^}]+)\}", r"[@\1]", text)
    text = re.sub(r"\\citet\{([^}]+)\}", r"[@\1]", text)
    text = re.sub(r"\\citep(?:\[[^\]]*\])?\{([^}]+)\}", r"[@\1]", text)
    text = re.sub(r"\\cite\{([^}]+)\}", r"[@\1]", text)
    text = re.sub(r"\\url\{([^}]+)\}", r"[\1](\1)", text)
    text = re.sub(r"\\ref\{([^}]+)\}", r"\\ref{\1}", text)
    text = re.sub(r"~", " ", text)
    return text.strip()


def stem_of(path: str) -> str:
    name = Path(path).name
    for ext in (".eps", ".pdf", ".png", ".jpg", ".gif", ".ps"):
        if name.lower().endswith(ext):
            return name[: -len(ext)]
    return Path(name).stem


def figure_lamd(filename: str, width_frac: str | None, caption: str, label: str) -> str:
    stem = stem_of(filename)
    pct = "80%"
    if width_frac:
        try:
            pct = f"{int(float(width_frac) * 100)}%"
        except ValueError:
            pass
    cap = latex_inline_to_md(caption) or stem
    key = label or stem.replace("_", "-")
    return (
        f"\\figure{{\\includepng{{\\diagramsDir/npa/{stem}}}{{{pct}}}}}{{{cap}}}{{{key}}}"
    )


def notes_wrap(text: str) -> str:
    text = text.strip()
    if not text:
        return ""
    text = text.replace(r"\[", "$$").replace(r"\]", "$$")
    # GPP is brace-aware; keep the block balanced.
    extra = text.count("{") - text.count("}")
    if extra > 0:
        text += "}" * extra
    elif extra < 0:
        text = ("{" * (-extra)) + text
    return f"\\notes{{{text}}}"


def slides_wrap(lines: list[str]) -> str:
    body = "\n".join(lines).strip()
    if not body:
        return ""
    body = body.replace(r"\[", "$$").replace(r"\]", "$$")
    extra = body.count("{") - body.count("}")
    if extra > 0:
        body += "}" * extra
    elif extra < 0:
        body = ("{" * (-extra)) + body
    return f"\\slides{{{body}}}"


@dataclass
class TexBlock:
    kind: str
    title: str = ""
    lines: list[str] = field(default_factory=list)
    starred: bool = False


def split_tex_units(tex: str) -> list[TexBlock]:
    """Linear scan of the conversion LaTeX into chapters, sections, foils, envs."""
    units: list[TexBlock] = []
    current = TexBlock(kind="preamble")
    env_stack: list[str] = []

    def push():
        nonlocal current
        if current.kind != "preamble" or current.lines:
            units.append(current)
        current = TexBlock(kind="para", lines=[])

    for raw in tex.splitlines():
        line = raw.rstrip()
        if line.strip() in {"\\begin{document}", "\\end{document}"}:
            continue
        if line.startswith("%") or line.startswith("\\documentclass") or line.startswith("\\usepackage") or line.startswith("\\new") or line.startswith("\\providecommand") or line.startswith("\\newenvironment"):
            continue
        heading = _macro_arg(
            line,
            ("foilhead", "chapter", "section", "subsection", "subsubsection", "paragraph"),
        )
        if heading and (not env_stack or heading[0] in {"foilhead", "chapter", "section"}):
            name, title, starred = heading
            push()
            env_stack.clear()
            kind = "foil" if name == "foilhead" else name
            current = TexBlock(kind=kind, title=title, starred=starred, lines=[])
            continue
        b = BEGIN_ENV_RE.match(line.strip())
        if b:
            env = b.group(1)
            if env in {"figure", "answer", "lyxnote", "itemize", "enumerate", "description", "tabular", "equation", "eqnarray", "eqnarray*"}:
                if not env_stack:
                    if current.kind != "para" or current.lines or current.title:
                        push()
                        current = TexBlock(kind="env:" + env, lines=[line])
                    else:
                        current.kind = "env:" + env
                        current.lines.append(line)
                else:
                    current.lines.append(line)
                env_stack.append(env)
                continue
        e = END_ENV_RE.match(line.strip())
        if e and env_stack and e.group(1) == env_stack[-1]:
            current.lines.append(line)
            env_stack.pop()
            if not env_stack and current.kind.startswith("env:"):
                push()
                current = TexBlock(kind="para", lines=[])
            continue
        if line.strip() == "" and not env_stack:
            if current.kind == "para" and current.lines:
                push()
                current = TexBlock(kind="para", lines=[])
            continue
        current.lines.append(line)
    if current.kind != "preamble" or current.lines:
        units.append(current)
    return [u for u in units if u.kind != "preamble"]


def env_to_notes(block: TexBlock) -> str:
    kind = block.kind.split(":", 1)[-1]
    body = "\n".join(block.lines)
    if kind == "figure":
        return figure_from_tex(body)
    if kind in {"itemize", "enumerate", "description"}:
        items = itemize_to_md(body, kind)
        return notes_wrap(items)
    if kind == "answer":
        inner = "\n".join(block.lines[1:-1]).strip()
        return "\\notes{\\subsection{Answer}}\n\n" + notes_wrap(latex_inline_to_md(inner))
    if kind == "lyxnote":
        inner = "\n".join(block.lines[1:-1]).strip()
        return notes_wrap("*Note.* " + latex_inline_to_md(inner))
    if kind == "tabular":
        return notes_wrap(tabular_to_md(body))
    if kind in {"equation", "eqnarray", "eqnarray*"}:
        return notes_wrap(body)
    return notes_wrap(latex_inline_to_md(body))


def _cmd_arg(text: str, cmd: str) -> str:
    token = "\\" + cmd + "{"
    i = text.find(token)
    if i < 0:
        return ""
    rest = text[i + len(token) - 1 :]
    depth = 0
    for j, ch in enumerate(rest):
        if ch == "{":
            depth += 1
        elif ch == "}":
            depth -= 1
            if depth == 0:
                return rest[1:j]
    return rest[1:]


def figure_from_tex(body: str) -> str:
    gm = GRAPHICS_RE.search(body)
    filename = gm.group(2) if gm else "unknown"
    width = gm.group(1) if gm else None
    caption = _cmd_arg(body, "caption")
    caption = re.sub(r"\\answer\{.*?\}(?:\{\d+\})?", "", caption)
    caption = caption.replace(r"\}", "").strip()
    label = _cmd_arg(body, "label")
    return figure_lamd(filename, width, caption, label)


def itemize_to_md(body: str, kind: str) -> str:
    items = re.split(r"\\item\s*", body)
    out: list[str] = []
    n = 0
    for item in items[1:]:
        item = re.sub(r"\\begin\{[^}]+\}|\\end\{[^}]+\}", "", item).strip()
        if not item:
            continue
        n += 1
        desc = re.match(r"\[([^\]]+)\]\s*(.*)", item, re.S)
        if desc:
            out.append(f"* **{desc.group(1)}** {latex_inline_to_md(desc.group(2))}")
        elif kind == "enumerate":
            out.append(f"{n}. {latex_inline_to_md(item)}")
        else:
            out.append(f"* {latex_inline_to_md(item)}")
    return "\n".join(out)


def tabular_to_md(body: str) -> str:
    rows = []
    for line in body.splitlines():
        if "&" not in line:
            continue
        line = line.replace("\\\\", "").strip()
        cells = [latex_inline_to_md(c) for c in line.split("&")]
        rows.append(cells)
    if not rows:
        return ""
    width = max(len(r) for r in rows)
    rows = [r + [""] * (width - len(r)) for r in rows]
    header = rows[0]
    sep = ["---"] * width
    lines = ["| " + " | ".join(header) + " |", "| " + " | ".join(sep) + " |"]
    for row in rows[1:]:
        lines.append("| " + " | ".join(row) + " |")
    return "\n".join(lines)


def units_to_notes(units: list[TexBlock]) -> str:
    parts: list[str] = []
    for unit in units:
        if unit.kind == "chapter":
            continue
        if unit.kind in {"section", "subsection", "subsubsection", "paragraph"}:
            title = latex_inline_to_md(unit.title)
            if unit.starred:
                hashes = {
                    "section": "##",
                    "subsection": "###",
                    "subsubsection": "####",
                    "paragraph": "**",
                }[unit.kind]
                heading = f"**{title}**" if unit.kind == "paragraph" else f"{hashes} {title}"
                parts.append(notes_wrap(heading))
            else:
                parts.append(notes_wrap(f"\\{unit.kind}{{{title}}}"))
            if unit.lines:
                parts.append(notes_wrap(latex_inline_to_md("\n".join(unit.lines))))
            continue
        if unit.kind.startswith("env:"):
            parts.append(env_to_notes(unit))
            continue
        if unit.kind == "para":
            raw = "\n".join(unit.lines)
            gm = GRAPHICS_RE.search(raw)
            if gm:
                parts.append(figure_lamd(gm.group(2), gm.group(1), "", ""))
                raw = GRAPHICS_RE.sub("", raw)
            text = latex_inline_to_md(raw)
            if text:
                parts.append(notes_wrap(text))
            continue
        if unit.kind == "foil":
            continue
    text = "\n\n".join(p for p in parts if p)
    text = GRAPHICS_RE.sub(
        lambda m: figure_lamd(m.group(2), m.group(1), "", ""),
        text,
    )
    return polish_notes(text)


def pythonise_matlab(text: str) -> str:
    text = re.sub(
        r"\(in MATLAB use rand\s*\)",
        "(in Python, `numpy.random.random()`)",
        text,
    )
    text = text.replace(
        "functions in MATLAB",
        "functions in Python (`scipy.special.gammaln`)",
    )
    return text


def _parse_answer_macro(text: str, start: int) -> tuple[str, int]:
    """Return (body, index after \\answer{body}{vspace}) starting at \\answer{."""
    i = start + len("\\answer{")
    depth = 1
    body: list[str] = []
    while i < len(text):
        if depth == 1 and text.startswith("\\}{", i):
            body_text = "".join(body)
            rest = text[i + 3 :]
            m = re.match(r"(\d+)\}", rest)
            end = i + 3 + (m.end() if m else 0)
            return body_text, end
        ch = text[i]
        if ch == "{":
            depth += 1
        elif ch == "}":
            depth -= 1
            if depth == 0:
                rest = text[i + 1 :]
                m = re.match(r"\{(\d+)\}", rest)
                end = i + 1 + (m.end() if m else 0)
                return "".join(body), end
        body.append(ch)
        i += 1
    return "".join(body), len(text)


def _close_open_notes(prefix: str) -> tuple[str, bool]:
    token = "\\notes{"
    last = prefix.rfind(token)
    if last < 0:
        return prefix, False
    rest = prefix[last + len(token) - 1 :]
    depth = 0
    for ch in rest:
        if ch == "{":
            depth += 1
        elif ch == "}":
            depth -= 1
    if depth > 0:
        return prefix + ("}" * depth), True
    return prefix, False


def _consume_braced(text: str, i: int) -> int:
    depth = 0
    for j in range(i, len(text)):
        if text[j] == "{":
            depth += 1
        elif text[j] == "}":
            depth -= 1
            if depth == 0:
                return j + 1
    return len(text)


def _split_figure(text: str) -> tuple[str, str, str]:
    k = text.find("\\figure{")
    if k < 0:
        return text, "", ""
    i = k + len("\\figure")
    for _ in range(3):
        while i < len(text) and text[i].isspace():
            i += 1
        if i < len(text) and text[i] == "{":
            i = _consume_braced(text, i)
    return text[:k], text[k:i], text[i:]


def tidy_answer_body(body: str) -> str:
    body = body.replace(r"\}", "}")
    body = re.sub(r"^\s*\[ht\]\s*$", "", body, flags=re.M)
    body = re.sub(r"\\centering", "", body)
    body = re.sub(r"\\caption\{[^{}]*\}", "", body)
    body = re.sub(r"\\label\{[^{}]*\}", "", body)
    body = re.sub(r"^\s*\[0\]\s*$", "", body, flags=re.M)
    if "&" in body and r"\begin{eqnarray" not in body:
        lines = [ln for ln in body.splitlines() if ln.strip()]
        aligned = [ln for ln in lines if "&" in ln]
        if aligned:
            wrapped = "\\begin{eqnarray*}\n" + "\n".join(aligned) + "\n\\end{eqnarray*}"
            other = [ln for ln in lines if "&" not in ln]
            body = "\n\n".join(["\n".join(other), wrapped] if other else [wrapped])
    return body.strip()


def expand_answers(text: str) -> str:
    """Turn leftover LyX \\answer{...}{n} into Answer subsections."""
    out: list[str] = []
    i = 0
    while True:
        j = text.find("\\answer{", i)
        if j < 0:
            out.append(text[i:])
            break
        prefix, closed = _close_open_notes(text[i:j])
        out.append(prefix)
        body, end = _parse_answer_macro(text, j)
        cleaned = tidy_answer_body(body)
        chunks = [notes_wrap("\\subsection{Answer}")]
        if r"\figure{" in cleaned:
            before, fig_block, after = _split_figure(cleaned)
            if before.strip():
                chunks.append(notes_wrap(latex_inline_to_md(before)))
            if fig_block:
                chunks.append(fig_block.strip())
            if after.strip():
                chunks.append(notes_wrap(latex_inline_to_md(after)))
        elif cleaned:
            chunks.append(notes_wrap(latex_inline_to_md(cleaned)))
        out.append("\n\n" + "\n\n".join(c for c in chunks if c) + "\n\n")
        i = end
        if closed:
            while i < len(text) and text[i] in "}\n":
                if text[i] == "}":
                    i += 1
                    break
                i += 1
    return "".join(out)


def expand_bracket_answers(text: str) -> str:
    """LyX \\answer{...}{0} that survived as a '[0]' vspace marker plus \\}{0}."""

    def repl(m):
        body = tidy_answer_body(m.group(1))
        return (
            "}\n\n"
            + notes_wrap("\\subsection{Answer}")
            + "\n\n"
            + notes_wrap(latex_inline_to_md(body))
            + "\n\n\\notes{"
        )

    return re.sub(
        r"\n[ \t]*\[0\][ \t]*\n(.*?)\\\}[ \t]*\{0\}",
        repl,
        text,
        flags=re.S,
    )


def polish_notes(text: str) -> str:
    text = expand_answers(text)
    text = expand_bracket_answers(text)
    text = pythonise_matlab(text)
    text = re.sub(r"\\notes\{#{2,4} Answer\}\n?", "", text)
    text = re.sub(r"\\subsubsection\*?\{Answer\}\n?", "", text)
    text = re.sub(r"\\notes\{\\subsubsection\{Answer\}\}\n?", "", text)
    text = re.sub(r"^\s*\d+\}\}\s*$", "", text, flags=re.M)
    text = re.sub(
        r"\n\\notes\{\\subsection\{Answer\}\}\s*\n+\\notes\{\\subsection\{Answer\}\}",
        lambda _m: "\n\\notes{\\subsection{Answer}}",
        text,
    )
    text = re.sub(r"\\notes\{\{+", r"\\notes{", text)
    text = re.sub(r"\\notes\{\s*\}", "", text)
    return text


@dataclass
class Foil:
    title: str
    units: list[TexBlock]
    index: int


def collect_foils(units: list[TexBlock]) -> list[Foil]:
    foils: list[Foil] = []
    current: Foil | None = None
    n = 0
    for unit in units:
        if unit.kind == "foil":
            n += 1
            attached: list[TexBlock] = []
            if unit.lines:
                attached.append(TexBlock(kind="para", lines=list(unit.lines)))
            current = Foil(title=unit.title, units=attached, index=n)
            foils.append(current)
            continue
        if current is None:
            continue
        current.units.extend(_unwrap_container(unit))
    return foils


def _unwrap_container(unit: TexBlock) -> list[TexBlock]:
    """LyX notes and answers wrap figures and lists; flatten them into foil body."""
    if not unit.kind.startswith("env:lyxnote") and not unit.kind.startswith("env:answer"):
        return [unit]
    inner = "\n".join(unit.lines[1:-1] if len(unit.lines) >= 2 else unit.lines)
    nested = split_tex_units(inner)
    if not nested:
        text = latex_inline_to_md(inner)
        return [TexBlock(kind="para", lines=[text])] if text else []
    out: list[TexBlock] = []
    for child in nested:
        out.extend(_unwrap_container(child))
    return out


def content_units(foil: Foil) -> int:
    n = 0
    for unit in foil.units:
        if unit.kind.startswith("env:itemize") or unit.kind.startswith("env:enumerate"):
            n += max(1, len(re.findall(r"\\item", "\n".join(unit.lines))))
        elif unit.kind.startswith("env:figure"):
            n += 2
        elif unit.kind == "para":
            text = " ".join(unit.lines).strip()
            if text:
                n += 1 if len(text) < 280 else 2
        else:
            n += 1
    return n


def char_count(foil: Foil) -> int:
    return sum(len("\n".join(u.lines)) for u in foil.units)


def _nonempty_units(units: list[TexBlock]) -> list[TexBlock]:
    return [u for u in units if any(line.strip() for line in u.lines)]


def split_foil_units(foil: Foil, overlay: bool) -> list[list[TexBlock]]:
    """One A4 foil -> two Reveal slides, unless it is already small or an overlay frame."""
    units = _nonempty_units(foil.units)
    if overlay or not units:
        return [units]
    n = content_units(Foil(title=foil.title, units=units, index=foil.index))
    chars = sum(len("\n".join(u.lines)) for u in units)
    if n <= 2 and chars < 280:
        return [units]
    fig_idx = next(
        (i for i, u in enumerate(units) if u.kind.startswith("env:figure") or GRAPHICS_RE.search("\n".join(u.lines))),
        None,
    )
    if fig_idx is not None and n >= 3:
        first = [units[fig_idx]]
        rest = [u for i, u in enumerate(units) if i != fig_idx]
        if rest:
            return [first, rest]
    if len(units) == 1:
        return _split_single_unit(units[0])
    mid = max(1, len(units) // 2)
    return [units[:mid], units[mid:]]


def _split_single_unit(unit: TexBlock) -> list[list[TexBlock]]:
    if unit.kind.startswith("env:itemize") or unit.kind.startswith("env:enumerate"):
        items = re.split(r"(?=\\item\s*)", "\n".join(unit.lines))
        head = items[:1]
        body = [i for i in items[1:] if i.strip()]
        if len(body) < 4:
            return [[unit]]
        mid = max(1, len(body) // 2)
        a = TexBlock(kind=unit.kind, lines=_rewrap_list(head, body[:mid], unit.kind))
        b = TexBlock(kind=unit.kind, lines=_rewrap_list(head, body[mid:], unit.kind))
        return [[a], [b]]
    return [[unit]]


def _rewrap_list(head: list[str], items: list[str], kind: str) -> list[str]:
    env = kind.split(":", 1)[-1]
    begin = next((h for h in head if h.strip().startswith("\\begin")), f"\\begin{{{env}}}")
    return [begin, *items, f"\\end{{{env}}}"]


def foil_to_slides(title: str, units: list[TexBlock], continued: bool, orig_index: int) -> str:
    shown = latex_inline_to_md(title)
    if continued:
        shown = f"{shown} (continued)"
    bullets: list[str] = []
    extras: list[str] = []
    for unit in units:
        raw = "\n".join(unit.lines)
        if unit.kind.startswith("env:figure"):
            extras.append(slides_wrap([figure_from_tex(raw)]))
            continue
        for gm in GRAPHICS_RE.finditer(raw):
            extras.append(slides_wrap([figure_lamd(gm.group(2), gm.group(1), "", stem_of(gm.group(2)))]))
        raw = GRAPHICS_RE.sub("", raw)
        if unit.kind.startswith("env:itemize") or unit.kind.startswith("env:enumerate") or unit.kind.startswith("env:description"):
            md = pythonise_matlab(itemize_to_md(raw, unit.kind.split(":")[-1]))
            bullets.extend(line for line in md.splitlines() if line.strip())
            continue
        if unit.kind.startswith("env:equation") or unit.kind.startswith("env:eqnarray"):
            extras.append("\\slides{" + "\n".join(unit.lines) + "}")
            continue
        if unit.kind == "para":
            text = pythonise_matlab(latex_inline_to_md(raw))
            if text:
                bullets.append(f"* {text}")
            continue
        if unit.kind.startswith("env:tabular"):
            table = tabular_to_md("\n".join(unit.lines))
            if table:
                extras.append(slides_wrap([table]))
            continue
        if unit.kind.startswith("env:answer"):
            bullets.append("* **Answer.**")
            inner = latex_inline_to_md("\n".join(unit.lines[1:-1]))
            if inner:
                bullets.append(f"* {inner}")
    if not bullets and not extras:
        if continued:
            return ""
    parts = [f"\\newslide{{{shown}}}"]
    if bullets:
        parts.append(slides_wrap(bullets))
    parts.extend(extras)
    return "\n\n".join(p for p in parts if p)


def units_to_slides(units: list[TexBlock]) -> str:
    foils = collect_foils(units)
    parts: list[str] = []
    for i, foil in enumerate(foils):
        overlay = False
        if i > 0 and normalise_overlay(foils[i - 1].title) == normalise_overlay(foil.title):
            overlay = True
        if i + 1 < len(foils) and normalise_overlay(foils[i + 1].title) == normalise_overlay(foil.title):
            overlay = True
        chunks = split_foil_units(foil, overlay=overlay)
        for j, chunk in enumerate(chunks):
            parts.append(
                foil_to_slides(foil.title, chunk, continued=j > 0, orig_index=foil.index)
            )
    return "\n\n".join(p for p in parts if p)


def normalise_overlay(title: str) -> str:
    t = re.sub(r"\s+", " ", title).strip().lower()
    t = re.sub(r"\s+(contd\.?|continued|ii+)$", "", t)
    return t


def write_snippet(path: Path, guard: str, body: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        f"\\ifndef{{{guard}}}\n\\define{{{guard}}}\n\n"
        f"{body.rstrip()}\n\n\\endif\n",
        encoding="utf-8",
    )
