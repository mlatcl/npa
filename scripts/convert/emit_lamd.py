"""Convert the generated conversion LaTeX into LaMD notes and slides.

Notes and slides are emitted as separate snippet files. Each original A4 foil
becomes two Reveal slides unless it is already short or is one frame of a
same-title overlay sequence.
"""

from __future__ import annotations

import re
import textwrap
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
        rest = rest.lstrip()
        if rest.startswith("["):
            depth = 0
            end = None
            for i, ch in enumerate(rest):
                if ch == "[":
                    depth += 1
                elif ch == "]":
                    depth -= 1
                    if depth == 0:
                        end = i
                        break
            if end is None:
                return None
            rest = rest[end + 1 :].lstrip()
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
    r"\\includegraphics(?:\[([^\]]*)\])?\{([^}]+)\}"
)


def _width_frac_from_opts(opts: str | None) -> str | None:
    if not opts:
        return None
    m = re.search(r"width=([0-9.]+)\\(?:text|line)width", opts)
    if m:
        return m.group(1)
    if r"\linewidth" in opts or r"\textwidth" in opts:
        return "1"
    return None


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
    text = re.sub(
        r"\\includegraphics(?:\[[^\]]*\])?\{\s*\}",
        "",
        text,
    )
    return text


def strip_answer_macros(text: str, *, keep_lyx_close: bool = False) -> str:
    """Drop leftover LyX \\}{n} closers.

    Notes still need those closers so expand_answers can finish a leftover
    \\answer{ ... } pair; FoilTeX sanitising should strip them.
    """
    if keep_lyx_close:
        return text
    return re.sub(r"\\\}[ \t]*\{\d+\}", "", text)


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
            rows = [ln for ln in math_lines if ln.strip()]
            math_lines.clear()
            if rows:
                chunks.append(
                    "$$\n\\begin{aligned}\n" + "\n".join(rows) + "\n\\end{aligned}\n$$"
                )

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


_ALIGN_REL = {
    "=",
    r"\equiv",
    r"\leq",
    r"\geq",
    r"\neq",
    r"\approx",
    r"\rightarrow",
    r"\leftarrow",
    r"\propto",
    r"\sim",
    r"\subset",
    r"\in",
}


def _align_row_cells(ln: str) -> list[str]:
    return [c.strip() for c in ln.replace(r"\\", "").split("&")]


def _is_eqnarray_row(ln: str) -> bool:
    """LyX eqnarray is `lhs & = & rhs`, not a table row."""
    cells = _align_row_cells(ln)
    if len(cells) != 3:
        return False
    mid = cells[1].split()[0] if cells[1] else ""
    return mid in _ALIGN_REL or mid.startswith("\\") and mid[1:].isalpha()


def wrap_alignments(body: str) -> str:
    """Orphan `&` rows from LyX tabular/eqnarray become a table or aligned math."""
    if "&" not in body:
        return body
    if r"\begin{aligned}" in body or r"\begin{array}" in body or r"\begin{tabular}" in body:
        return body
    lines = body.splitlines()
    aligned = [ln for ln in lines if "&" in ln]
    if not aligned:
        return body
    if aligned and all(_is_eqnarray_row(ln) for ln in aligned):
        wrapped = "$$\n\\begin{aligned}\n" + "\n".join(aligned) + "\n\\end{aligned}\n$$"
        other = [ln for ln in lines if "&" not in ln]
        return "\n\n".join(["\n".join(other), wrapped] if other else [wrapped])
    if any(ln.count("&") >= 2 for ln in aligned) and not any(_is_eqnarray_row(ln) for ln in aligned):
        cells = [_align_row_cells(ln) for ln in aligned]
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
    text = strip_answer_macros(strip_figure_chrome(text), keep_lyx_close=True)
    text = re.sub(r"\\tiny\b", "", text)
    text = re.sub(r"\\normalsize\b", "", text)
    text = latex_envs_for_markdown(text)
    text = wrap_alignments(text)
    text = tidy_dollar_math(text)
    text = wrap_bare_tex(text)
    text = repair_fracs(text)
    text = inject_ensuremath(text)
    text = isolate_display_math(text)
    text = text.replace(r"\ensuremath{\lambda\}", r"\ensuremath{\lambda}")
    text = re.sub(
        r"\\ensuremath\{\\frac\{([^{}]+)\}\{([^{}]+)\}\\\}",
        r"\\ensuremath{\\frac{\1}{\2}}",
        text,
    )
    return text


def isolate_display_math(text: str) -> str:
    """Put $$...$$ blocks on their own paragraphs so pandoc sees display math.

    Walk character-by-character so ``$X$$`` (inline close then display open)
    is not split through the middle of the inline math.
    """
    if "$$" not in text:
        return text
    out: list[str] = []
    i = 0
    n = len(text)
    in_inline = False
    while i < n:
        if not in_inline and text.startswith("$$", i):
            j = text.find("$$", i + 2)
            if j < 0:
                out.append(text[i:])
                break
            math = text[i + 2 : j].strip()
            if math:
                out.append("\n\n$$\n" + math + "\n$$\n\n")
            i = j + 2
            continue
        ch = text[i]
        if ch == "$" and (i == 0 or text[i - 1] != "\\"):
            in_inline = not in_inline
        out.append(ch)
        i += 1
    text = "".join(out)
    return re.sub(r"\n{3,}", "\n\n", text)


def inject_ensuremath(text: str) -> str:
    """Wrap leftover math commands so they are legal in text mode.

    Skip material already in `$...$`, `$$...$$`, or a math environment — wrapping
    ``\\exp\\left(-`` there splits the atom at the minus and breaks pdflatex.
    """
    cmd_re = re.compile(
        r"\\(?:infty|rightarrow|leftarrow|Delta|lambda|mu|rho|alpha|beta|gamma|"
        r"theta|sigma|omega|bar|hat|tilde|frac|times|exp|sum|prod|int|partial|"
        r"cdot|leq|geq|neq|approx|dots|ldots|cdots|lim|ln|log)\b"
    )
    math_begin = re.compile(r"\\begin\{(aligned|align\*?|equation\*?|eqnarray\*?|array|cases)\}")
    math_end = re.compile(r"\\end\{(aligned|align\*?|equation\*?|eqnarray\*?|array|cases)\}")
    out: list[str] = []
    i = 0
    n = len(text)
    in_display = False
    in_inline = False
    env_depth = 0
    while i < n:
        if not in_inline and env_depth == 0 and text.startswith("$$", i):
            in_display = not in_display
            out.append("$$")
            i += 2
            continue
        if not in_display and env_depth == 0 and text[i] == "$" and (i == 0 or text[i - 1] != "\\"):
            in_inline = not in_inline
            out.append("$")
            i += 1
            continue
        mb = math_begin.match(text, i)
        if mb:
            env_depth += 1
            out.append(mb.group(0))
            i = mb.end()
            continue
        me = math_end.match(text, i)
        if me and env_depth:
            env_depth -= 1
            out.append(me.group(0))
            i = me.end()
            continue
        m = cmd_re.match(text, i)
        if m and not in_display and not in_inline and env_depth == 0:
            if text.rfind(r"\ensuremath{", 0, i) > text.rfind("}", 0, i):
                out.append(m.group(0))
                i = m.end()
                continue
            end = _consume_mathish(text, i)
            chunk = text[i:end]
            if chunk.startswith(r"\ensuremath{"):
                out.append(chunk)
            else:
                out.append(r"\ensuremath{" + chunk + "}")
            i = end
            continue
        out.append(text[i])
        i += 1
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
    if not stem:
        return latex_inline_to_md(caption) if caption else ""
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


def _brace_wrap(macro: str, text: str) -> str:
    text = text.strip()
    if not text:
        return ""
    text = prepare_tex_body(text)
    extra = text.count("{") - text.count("}")
    if extra > 0:
        text += "}" * extra
    elif extra < 0:
        text = ("{" * (-extra)) + text
    return f"\\{macro}{{{text}}}"


def notes_wrap(text: str) -> str:
    return _brace_wrap("notes", text)


def speakernotes_wrap(text: str) -> str:
    return _brace_wrap("speakernotes", text)


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
        if line.startswith(
            (
                "\\leftheader",
                "\\rightheader",
                "\\rightfooter",
                "\\MyLogo",
                "\\maketitle",
                "\\graphicspath",
                "\\AtBeginDocument",
            )
        ):
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


def extract_env_blocks(text: str, env: str) -> tuple[list[str], str]:
    """Pull \\begin{env}...\\end{env} bodies out of text; return (bodies, remainder)."""
    begin = f"\\begin{{{env}}}"
    end = f"\\end{{{env}}}"
    found: list[str] = []
    rest: list[str] = []
    i = 0
    while True:
        j = text.find(begin, i)
        if j < 0:
            rest.append(text[i:])
            break
        rest.append(text[i:j])
        k = j + len(begin)
        if k < len(text) and text.startswith("[", k):
            close = text.find("]", k)
            k = close + 1 if close >= 0 else k
        depth = 1
        pos = k
        inner_end = None
        while pos < len(text):
            b = text.find(begin, pos)
            e = text.find(end, pos)
            if e < 0:
                break
            if b >= 0 and b < e:
                depth += 1
                pos = b + len(begin)
                continue
            depth -= 1
            if depth == 0:
                inner_end = e
                break
            pos = e + len(end)
        if inner_end is None:
            rest.append(text[j:])
            break
        found.append(text[k:inner_end].strip())
        i = inner_end + len(end)
    return found, "".join(rest)


def extract_answer_blocks(text: str) -> tuple[list[tuple[str, str]], str]:
    """Pull \\begin{answer}[vspace]...\\end{answer} bodies; return ([(body, vspace)], remainder)."""
    begin = "\\begin{answer}"
    end = "\\end{answer}"
    found: list[tuple[str, str]] = []
    rest: list[str] = []
    i = 0
    while True:
        j = text.find(begin, i)
        if j < 0:
            rest.append(text[i:])
            break
        rest.append(text[i:j])
        k = j + len(begin)
        vspace = "0"
        if k < len(text) and text.startswith("[", k):
            close = text.find("]", k)
            if close >= 0:
                vspace = text[k + 1 : close].strip() or "0"
                k = close + 1
        depth = 1
        pos = k
        inner_end = None
        while pos < len(text):
            b = text.find(begin, pos)
            e = text.find(end, pos)
            if e < 0:
                break
            if b >= 0 and b < e:
                depth += 1
                pos = b + len(begin)
                continue
            depth -= 1
            if depth == 0:
                inner_end = e
                break
            pos = e + len(end)
        if inner_end is None:
            rest.append(text[j:])
            break
        found.append((text[k:inner_end].strip(), vspace))
        i = inner_end + len(end)
    return found, "".join(rest)


def _vspace_from_answer_begin(line: str) -> str:
    m = re.search(r"\\begin\{answer\}(?:\[([^\]]*)\])?", line)
    if m and m.group(1):
        return m.group(1).strip() or "0"
    return "0"


def _answer_slot(body: str, vspace: str = "0") -> str:
    body = textwrap.dedent(body).strip()
    if not body:
        return ""
    vspace = vspace.strip() or "0"
    # Pandoc treats a 4-space indent as a code block; keep the slot flush left.
    body = "\n".join(ln.lstrip() if ln.startswith("    ") else ln for ln in body.splitlines())
    return f"\\answer{{\n{body}\n}}{{{vspace}}}"


def _answer_to_notes(inner: str, vspace: str = "0") -> str:
    inner = strip_figure_chrome(strip_answer_macros(inner)).strip()
    if not inner:
        return ""
    if r"\item" in inner:
        md = itemize_to_md(inner, "itemize")
    else:
        md = latex_inline_to_md(inner)
    slot = _answer_slot(md, vspace)
    return notes_wrap(slot) if slot else ""


def env_to_notes(block: TexBlock) -> str:
    kind = block.kind.split(":", 1)[-1]
    body = "\n".join(block.lines)
    if kind == "figure":
        return figure_from_tex(body)
    if kind in {"itemize", "enumerate", "description"}:
        speakers, body = extract_env_blocks(body, "lyxnote")
        answers, body = extract_answer_blocks(body)
        figures, body = extract_env_blocks(body, "figure")
        items = itemize_to_md(
            strip_figure_chrome(strip_answer_macros(body, keep_lyx_close=True)), kind
        )
        parts = [notes_wrap(items)] if items.strip() else []
        for fig in figures:
            parts.append(figure_from_tex(fig))
        for sp in speakers:
            parts.append(speakernotes_wrap(latex_inline_to_md(_strip_answer_env(sp))))
        for ans, vspace in answers:
            parts.append(_answer_to_notes(ans, vspace))
        return "\n\n".join(p for p in parts if p)
    if kind == "answer":
        vspace = _vspace_from_answer_begin(block.lines[0] if block.lines else "")
        inner = "\n".join(block.lines[1:-1]).strip()
        return _answer_to_notes(inner, vspace)
    if kind == "lyxnote":
        inner = "\n".join(block.lines[1:-1]).strip()
        answers, inner = extract_answer_blocks(inner)
        parts = [speakernotes_wrap(latex_inline_to_md(_strip_answer_env(inner)))]
        for ans, _vspace in answers:
            parts.append(speakernotes_wrap(latex_inline_to_md(_strip_answer_env(ans))))
        return "\n\n".join(p for p in parts if p)
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
    width = _width_frac_from_opts(gm.group(1) if gm else None)
    caption = _cmd_arg(body, "caption")
    caption = re.sub(r"\\answer\{.*?\}(?:\{\d+\})?", "", caption)
    caption = caption.replace(r"\}", "").strip()
    label = _cmd_arg(body, "label")
    return figure_lamd(filename, width, caption, label)


def _replace_tabulars(text: str) -> str:
    """Turn nested \\begin{tabular}...\\end{tabular} into markdown tables."""
    out: list[str] = []
    i = 0
    begin = r"\begin{tabular}"
    end = r"\end{tabular}"
    while True:
        j = text.find(begin, i)
        if j < 0:
            out.append(text[i:])
            break
        out.append(text[i:j])
        k = text.find(end, j)
        if k < 0:
            out.append(text[j:])
            break
        out.append("\n" + tabular_to_md(text[j : k + len(end)]) + "\n")
        i = k + len(end)
    return "".join(out)


def itemize_to_md(body: str, kind: str) -> str:
    items = re.split(r"\\item\s*", body)
    out: list[str] = []
    n = 0
    for item in items[1:]:
        item = re.sub(
            r"\\begin\{(?:enumerate|itemize|description)\}|\\end\{(?:enumerate|itemize|description)\}",
            "",
            item,
        )
        item = _replace_tabulars(item).strip()
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
                parts.append(
                    figure_from_tex(raw)
                    if r"\caption" in raw
                    else figure_lamd(gm.group(2), _width_frac_from_opts(gm.group(1)), "", "")
                )
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
        lambda m: figure_lamd(m.group(2), _width_frac_from_opts(m.group(1)), "", ""),
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


def _parse_answer_macro(text: str, start: int) -> tuple[str, str, int, bool]:
    """Return (body, vspace, index after slot, lyx_escaped_close) at \\answer{."""
    i = start + len("\\answer{")
    depth = 1
    body: list[str] = []
    while i < len(text):
        if depth == 1 and text.startswith("\\}{", i):
            body_text = "".join(body)
            rest = text[i + 3 :]
            m = re.match(r"(\d+)\}", rest)
            vspace = m.group(1) if m else "0"
            end = i + 3 + (m.end() if m else 0)
            return body_text, vspace, end, True
        ch = text[i]
        if ch == "{":
            depth += 1
        elif ch == "}":
            depth -= 1
            if depth == 0:
                rest = text[i + 1 :]
                m = re.match(r"\{(\d+)\}", rest)
                vspace = m.group(1) if m else "0"
                end = i + 1 + (m.end() if m else 0)
                return "".join(body), vspace, end, False
        body.append(ch)
        i += 1
    return "".join(body), "0", len(text), True


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
    if (
        "&" in body
        and r"\begin{eqnarray" not in body
        and r"\begin{aligned}" not in body
        and r"\begin{tabular}" not in body
    ):
        lines = [ln for ln in body.splitlines() if ln.strip()]
        aligned = [ln for ln in lines if "&" in ln]
        if aligned and all(_is_eqnarray_row(ln) for ln in aligned):
            wrapped = "\\begin{eqnarray*}\n" + "\n".join(aligned) + "\n\\end{eqnarray*}"
            other = [ln for ln in lines if "&" not in ln]
            body = "\n\n".join(["\n".join(other), wrapped] if other else [wrapped])
    return body.strip()


def expand_answers(text: str) -> str:
    """Turn leftover LyX \\answer{...}{n} into \\answer slots inside \\notes."""
    out: list[str] = []
    i = 0
    while True:
        j = text.find("\\answer{", i)
        if j < 0:
            out.append(text[i:])
            break
        body, vspace, end, escaped = _parse_answer_macro(text, j)
        if not escaped:
            # Already a first-class LaMD slot; do not re-prepare (that empties
            # aligned environments and can swallow the next table).
            out.append(text[i:end])
            i = end
            continue
        prefix, closed = _close_open_notes(text[i:j])
        out.append(prefix)
        cleaned = tidy_answer_body(body)
        chunks: list[str] = []
        if r"\figure{" in cleaned:
            before, fig_block, after = _split_figure(cleaned)
            if before.strip():
                chunks.append(notes_wrap(_answer_slot(latex_inline_to_md(before), vspace)))
            if fig_block:
                chunks.append(fig_block.strip())
            if after.strip():
                chunks.append(notes_wrap(_answer_slot(latex_inline_to_md(after), vspace)))
        elif cleaned:
            chunks.append(notes_wrap(_answer_slot(latex_inline_to_md(cleaned), vspace)))
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
            + notes_wrap(_answer_slot(latex_inline_to_md(body), "0"))
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


def _strip_answer_env(text: str) -> str:
    text = re.sub(r"\\begin\{answer\}(?:\[[^\]]*\])?", "", text)
    text = re.sub(r"\\end\{answer\}", "", text)
    return text.strip()


def _unwrap_container(unit: TexBlock) -> list[TexBlock]:
    """Lift leftover LyX notes to speaker-note units; flatten answers that wrap figures."""
    if unit.kind.startswith("env:lyxnote"):
        return [unit]
    raw = "\n".join(unit.lines)
    if r"\begin{lyxnote}" in raw or (
        not unit.kind.startswith("env:answer") and r"\begin{answer}" in raw
    ):
        notes, rest = extract_env_blocks(raw, "lyxnote")
        answers, rest = extract_answer_blocks(rest)
        out: list[TexBlock] = []
        rest = rest.strip()
        if rest:
            rebuilt = TexBlock(
                kind=unit.kind,
                title=unit.title,
                lines=rest.split("\n"),
                starred=unit.starred,
            )
            if rebuilt.kind.startswith("env:answer"):
                out.extend(_flatten_answer(rebuilt))
            else:
                out.append(rebuilt)
        for n in notes:
            out.append(
                TexBlock(kind="env:lyxnote", lines=["\\begin{lyxnote}", n, "\\end{lyxnote}"])
            )
        for a, vspace in answers:
            out.extend(
                _flatten_answer(
                    TexBlock(
                        kind="env:answer",
                        lines=[f"\\begin{{answer}}[{vspace}]", a, "\\end{answer}"],
                    )
                )
            )
        return out or [unit]
    if unit.kind.startswith("env:answer"):
        return _flatten_answer(unit)
    return [unit]


def _flatten_answer(unit: TexBlock) -> list[TexBlock]:
    inner = "\n".join(unit.lines[1:-1] if len(unit.lines) >= 2 else unit.lines)
    nested = split_tex_units(inner)
    if not nested:
        text = latex_inline_to_md(inner)
        return [TexBlock(kind="para", lines=[text])] if text else []
    out: list[TexBlock] = []
    for child in nested:
        out.extend(_unwrap_container(child))
    return out or [unit]


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
        if unit.kind.startswith("env:lyxnote"):
            inner = _strip_answer_env("\n".join(unit.lines[1:-1] if len(unit.lines) >= 2 else unit.lines))
            text = pythonise_matlab(latex_inline_to_md(inner))
            if text.strip():
                extras.append(speakernotes_wrap(text))
            continue
        if unit.kind.startswith("env:answer"):
            vspace = _vspace_from_answer_begin(unit.lines[0] if unit.lines else "")
            inner = latex_inline_to_md("\n".join(unit.lines[1:-1]))
            slot = _answer_slot(inner, vspace)
            if slot:
                extras.append(slides_wrap([slot]))
            continue
        if unit.kind.startswith("env:figure"):
            extras.append(slides_wrap([figure_from_tex(raw)]))
            continue
        for gm in GRAPHICS_RE.finditer(raw):
            extras.append(
                slides_wrap(
                    [
                        figure_from_tex(raw)
                        if r"\caption" in raw
                        else figure_lamd(
                            gm.group(2),
                            _width_frac_from_opts(gm.group(1)),
                            "",
                            stem_of(gm.group(2)),
                        )
                    ]
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
