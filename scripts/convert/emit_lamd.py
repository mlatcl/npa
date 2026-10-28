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


def _strip_macro(text: str, cmd: str) -> str:
    token = "\\" + cmd
    while True:
        i = text.find(token)
        if i < 0:
            return text
        j = i + len(token)
        while j < len(text) and text[j].isspace():
            j += 1
        if j < len(text) and text[j] == "{":
            text = text[:i] + text[_consume_braced(text, j) :]
        else:
            text = text[:i] + text[j:]


def strip_figure_chrome(text: str) -> str:
    """Drop leftover LyX figure wrappers once the image is a \\figure{...}."""
    text = re.sub(r"\\begin\{figure\}\s*\[[^\]]*\]", "", text)
    text = re.sub(r"\\begin\{figure\}", "", text)
    text = re.sub(r"\\end\{figure\}", "", text)
    text = re.sub(r"\\centering\b", "", text)
    text = _strip_macro(text, "caption")
    text = re.sub(r"^\s*\[ht(?:b)?\]\s*$", "", text, flags=re.M)
    text = re.sub(r"\[ht(?:b)?\]", "", text)
    return text


def strip_answer_macros(text: str) -> str:
    text = re.sub(r"\\answer\{", "", text)
    text = re.sub(r"\\\}[ \t]*\{\d+\}", "", text)
    text = re.sub(r"\}\{\d+\}", "", text)
    return text


def fix_cases_arrays(text: str) -> str:
    """LyX cases often survive as \\left\\{ {cc} rather than array."""
    text = re.sub(r"\\left\s*\\\{\s*\{([clr|]+)\}", r"\\begin{array}{\1}", text)
    text = re.sub(r"\\left\s*\(\s*\{([clr|]+)\}", r"\\begin{array}{\1}", text)
    while text.count(r"\begin{array}") > text.count(r"\end{array}"):
        m = re.search(r"\\right\s*\.", text)
        if not m:
            text += r"\end{array}"
            break
        text = text[: m.start()] + r"\end{array}" + text[m.end() :]
    text = re.sub(r"\{l{3,}\}", "", text)
    text = re.sub(r"\\tiny\b", "", text)
    text = re.sub(r"\\normalsize\b", "", text)
    return text


def _try_consume_braced(text: str, i: int) -> int | None:
    depth = 0
    for j in range(i, len(text)):
        if text[j] == "{":
            depth += 1
        elif text[j] == "}":
            depth -= 1
            if depth == 0:
                return j + 1
    return None


def tidy_dollar_math(text: str) -> str:
    """Keep `$...$` (pandoc's tex_math_dollars); trim spaces and un-escape braces."""
    out: list[str] = []
    i = 0
    n = len(text)
    while i < n:
        if text.startswith(r"\(", i):
            j = text.find(r"\)", i + 2)
            if j < 0:
                out.append(text[i:])
                break
            out.append("$" + text[i + 2 : j].strip() + "$")
            i = j + 2
            continue
        out.append(text[i])
        i += 1
    text = "".join(out)

    def repl(m: re.Match[str]) -> str:
        inner = m.group(1).strip()
        inner = inner.replace(r"\left\{", r"\left\lbrace")
        inner = inner.replace(r"\right\}", r"\right\rbrace")
        return "$" + inner + "$"

    parts = text.split("$$")
    for i in range(0, len(parts), 2):
        parts[i] = re.sub(r"\$([^$]+)\$", repl, parts[i])
    return "$$".join(parts)


MATH_CMD_RE = re.compile(
    r"\\(?:infty|rightarrow|leftarrow|Delta|lambda|mu|rho|alpha|beta|gamma|theta|"
    r"sigma|omega|bar|hat|tilde|frac|times|exp|sum|prod|int|"
    r"partial|cdot|leq|geq|neq|approx|dots|ldots|cdots|prime|quad|qquad|"
    r"lim|ln|log|sin|cos|tan|mathrm|mathbf)\b"
)


def _consume_mathish(text: str, i: int) -> int:
    n = len(text)
    while i < n:
        if text[i] == "\\":
            j = i + 1
            if j < n and text[j] in "{}%$&_#":
                i = j + 1
                continue
            while j < n and text[j].isalpha():
                j += 1
            cmd = text[i + 1 : j]
            i = j
            if cmd in {"left", "right"} and i < n:
                if text.startswith(r"\langle", i) or text.startswith(r"\rangle", i):
                    i += 7
                elif text[i] in ".()[]|/<>":
                    i += 1
            continue
        if text[i] == "{":
            end = _try_consume_braced(text, i)
            if end is None:
                break
            i = end
            continue
        if text[i] in "([":
            opener = text[i]
            closer = ")" if opener == "(" else "]"
            depth = 1
            i += 1
            while i < n and depth:
                if text[i] == opener:
                    depth += 1
                elif text[i] == closer:
                    depth -= 1
                i += 1
            continue
        if text[i] in "^_":
            i += 1
            if i < n and text[i] == "{":
                end = _try_consume_braced(text, i)
                if end is None:
                    break
                i = end
            elif i < n and not text[i].isspace():
                i += 1
            continue
        if text[i] in " \t" and i + 1 < n and text[i + 1] == "\\":
            i += 1
            continue
        break
    return i


def wrap_bare_tex(text: str) -> str:
    """Wrap leftover TeX commands that sit outside `$...$` / `$$...$$`."""
    out: list[str] = []
    i = 0
    n = len(text)
    in_display = False
    in_inline = False
    while i < n:
        if not in_inline and text.startswith("$$", i):
            in_display = not in_display
            out.append("$$")
            i += 2
            continue
        if not in_display and text[i] == "$" and (i == 0 or text[i - 1] != "\\"):
            in_inline = not in_inline
            out.append("$")
            i += 1
            continue
        if not in_display and not in_inline:
            if text.startswith(r"\left", i):
                j = text.find(r"\right", i + 5)
                k = i
                while k > 0 and text[k - 1].isalpha():
                    k -= 1
                if j < 0:
                    end = _consume_mathish(text, i)
                    chunk = text[k:end] + r"\right."
                else:
                    end = _consume_mathish(text, j)
                    chunk = text[k:end]
                out.append("$" + chunk + "$")
                i = end
                continue
            m = MATH_CMD_RE.match(text, i)
            if m:
                end = _consume_mathish(text, i)
                chunk = text[i:end]
                if chunk:
                    out.append("$" + chunk + "$")
                    i = end
                    continue
        out.append(text[i])
        i += 1
    return "".join(out)


def latex_envs_for_markdown(text: str) -> str:
    text = text.replace(r"\[", "$$").replace(r"\]", "$$")
    text = re.sub(r"\\begin\{equation\*?\}", "$$", text)
    text = re.sub(r"\\end\{equation\*?\}", "$$", text)

    def eqna(m: re.Match[str]) -> str:
        inner = m.group(1).replace(r"\&", "&")
        math_lines: list[str] = []
        chunks: list[str] = []

        def flush() -> None:
            if math_lines:
                chunks.append(
                    "$$\n\\begin{aligned}\n" + "\n".join(math_lines) + "\n\\end{aligned}\n$$"
                )
                math_lines.clear()

        for ln in inner.splitlines():
            s = ln.strip()
            if not s:
                continue
            if "&" in s or s.endswith(r"\\") or s.startswith("\\"):
                math_lines.append(ln)
            else:
                flush()
                chunks.append(s)
        flush()
        return "\n\n".join(chunks) if chunks else ""

    text = re.sub(
        r"\\begin\{eqnarray\*?\}(.*?)\\end\{eqnarray\*?\}",
        eqna,
        text,
        flags=re.S,
    )
    return fix_cases_arrays(text)


def wrap_alignments(body: str) -> str:
    """Orphan `&` rows from LyX tabular/eqnarray become aligned math."""
    if "&" not in body:
        return body
    if r"\begin{aligned}" in body or r"\begin{array}" in body:
        return body
    lines = body.splitlines()
    aligned = [ln for ln in lines if "&" in ln]
    if not aligned:
        return body
    if any(ln.count("&") >= 2 for ln in aligned):
        cells = []
        for ln in aligned:
            row = [c.strip() for c in ln.replace(r"\\", "").split("&")]
            cells.append(row)
        width = max(len(r) for r in cells)
        cells = [r + [""] * (width - len(r)) for r in cells]
        header, rest = cells[0], cells[1:]
        table = [
            "| " + " | ".join(header) + " |",
            "| " + " | ".join(["---"] * width) + " |",
        ]
        for row in rest:
            table.append("| " + " | ".join(row) + " |")
        other = [ln for ln in lines if "&" not in ln]
        return "\n\n".join(["\n".join(other), "\n".join(table)] if other else ["\n".join(table)])
    wrapped = "$$\n\\begin{aligned}\n" + "\n".join(aligned) + "\n\\end{aligned}\n$$"
    other = [ln for ln in lines if "&" not in ln]
    return "\n\n".join(["\n".join(other), wrapped] if other else [wrapped])


def prepare_tex_body(text: str) -> str:
    text = strip_answer_macros(strip_figure_chrome(text))
    text = latex_envs_for_markdown(text)
    text = wrap_alignments(text)
    text = tidy_dollar_math(text)
    text = repair_fracs(text)
    text = inject_ensuremath(text)
    text = text.replace(r"\ensuremath{\lambda\}", r"\ensuremath{\lambda}")
    text = re.sub(
        r"\\ensuremath\{\\frac\{([^{}]+)\}\{([^{}]+)\}\\\}",
        r"\\ensuremath{\\frac{\1}{\2}}",
        text,
    )
    return text


def inject_ensuremath(text: str) -> str:
    """Wrap leftover math commands so they are legal in text mode."""
    cmd_re = re.compile(
        r"\\(?:infty|rightarrow|leftarrow|Delta|lambda|mu|rho|alpha|beta|gamma|"
        r"theta|sigma|omega|bar|hat|tilde|frac|times|exp|sum|prod|int|partial|"
        r"cdot|leq|geq|neq|approx|dots|ldots|cdots|lim|ln|log)\b"
    )
    out: list[str] = []
    i = 0
    n = len(text)
    while i < n:
        m = cmd_re.search(text, i)
        if not m:
            out.append(text[i:])
            break
        start = m.start()
        if text.rfind(r"\ensuremath{", i, start) > text.rfind("}", i, start):
            out.append(text[i : m.end()])
            i = m.end()
            continue
        out.append(text[i:start])
        end = _consume_mathish(text, start)
        chunk = text[start:end]
        if chunk.startswith(r"\ensuremath{"):
            out.append(chunk)
        else:
            out.append(r"\ensuremath{" + chunk + "}")
        i = end
    return "".join(out)


def repair_fracs(text: str) -> str:
    """Give \\frac two brace arguments, or flatten it if LyX left it unclosed."""

    def once(src: str) -> str:
        out: list[str] = []
        i = 0
        n = len(src)
        while i < n:
            if src.startswith(r"\frac", i) and (i == 0 or not src[i - 1].isalpha()):
                i += 5
                args: list[str] = []
                broken = False
                while len(args) < 2 and not broken:
                    while i < n and src[i].isspace():
                        i += 1
                    if i < n and src[i] == "{":
                        end = _try_consume_braced(src, i)
                        if end is None:
                            cut = n
                            for sep in ("$", "\n"):
                                p = src.find(sep, i + 1)
                                if p >= 0:
                                    cut = min(cut, p)
                            args.append(src[i + 1 : cut])
                            i = cut
                            broken = True
                        else:
                            args.append(src[i + 1 : end - 1])
                            i = end
                    else:
                        args.append("1")
                if broken:
                    out.append(" ".join(args))
                else:
                    out.append(r"\frac{" + args[0] + "}{" + args[1] + "}")
                continue
            out.append(src[i])
            i += 1
        return "".join(out)

    prev = None
    for _ in range(6):
        if src := once(text):
            if src == prev:
                return src
            prev, text = src, src
    return text


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
    text = prepare_tex_body(text)
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
    body = prepare_tex_body(body)
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
        items = itemize_to_md(strip_figure_chrome(strip_answer_macros(body)), kind)
        return notes_wrap(items)
    if kind == "answer":
        inner = "\n".join(block.lines[1:-1]).strip()
        return "\\notes{\\subsection{Answer}}\n\n" + notes_wrap(
            latex_inline_to_md(strip_figure_chrome(strip_answer_macros(inner)))
        )
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
                parts.append(figure_from_tex(raw) if r"\caption" in raw else figure_lamd(gm.group(2), gm.group(1), "", ""))
                raw = GRAPHICS_RE.sub("", raw)
            raw = strip_figure_chrome(raw)
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
    text = lift_figures_from_notes(text)
    return text


def lift_figures_from_notes(text: str) -> str:
    """\\figure must sit outside \\notes so GPP expands it as a float."""
    prev = None
    while prev != text:
        prev = text
        text = _lift_figures_once(text)
    return text


def _figure_end(text: str, k: int) -> int:
    i = k + len("\\figure")
    for _ in range(3):
        while i < len(text) and text[i].isspace():
            i += 1
        if i < len(text) and text[i] == "{":
            i = _consume_braced(text, i)
    return i


def _lift_figures_once(text: str) -> str:
    token = "\\notes{"
    out: list[str] = []
    i = 0
    while True:
        k = text.find(r"\figure{", i)
        if k < 0:
            out.append(text[i:])
            break
        prefix = text[i:k]
        last_notes = prefix.rfind(token)
        unclosed = False
        if last_notes >= 0:
            rest = prefix[last_notes + len(token) - 1 :]
            depth = 0
            for ch in rest:
                if ch == "{":
                    depth += 1
                elif ch == "}":
                    depth -= 1
            unclosed = depth > 0
        if unclosed:
            out.append(prefix)
            out.append("}\n\n")
            end = _figure_end(text, k)
            out.append(text[k:end].strip())
            out.append("\n\n\\notes{")
            i = end
            continue
        out.append(prefix)
        end = _figure_end(text, k)
        out.append(text[k:end])
        i = end
    return "".join(out)


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
            extras.append(
                slides_wrap(
                    [figure_from_tex(raw) if r"\caption" in raw else figure_lamd(gm.group(2), gm.group(1), "", stem_of(gm.group(2)))]
                )
            )
        raw = GRAPHICS_RE.sub("", raw)
        raw = strip_figure_chrome(strip_answer_macros(raw))
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
