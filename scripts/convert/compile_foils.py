#!/usr/bin/env python3
"""Compile the conversion slides.tex with FoilTeX as portrait Letter foils.

FoilTeX is not in TeX Live (IBM licence). This script fetches the unmodified
CTAN package into gitignored build/texmf/ and runs pdflatex with that on
TEXINPUTS. The 2006 deck is US Letter portrait (612x792), 20pt, not Beamer.
"""

from __future__ import annotations

import argparse
import os
import re
import subprocess
import sys
import zipfile
from pathlib import Path
from urllib.request import urlopen

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
sys.path.insert(0, str(HERE))

from emit_tex import document_to_tex  # noqa: E402
from lyx14 import parse_file  # noqa: E402

BUILD = ROOT / "build" / "conversion"
TEXMF = ROOT / "build" / "texmf"
FOILTEX_ZIP = "https://mirrors.ctan.org/macros/latex/contrib/foiltex.zip"


def ensure_foiltex() -> Path:
    """Return the directory that contains foils.cls, downloading CTAN FoilTeX if needed."""
    cls = TEXMF / "foils.cls"
    if cls.is_file():
        return TEXMF
    TEXMF.mkdir(parents=True, exist_ok=True)
    zip_path = TEXMF / "foiltex.zip"
    print(f"fetching FoilTeX from CTAN into {zip_path}")
    with urlopen(FOILTEX_ZIP, timeout=60) as resp:
        zip_path.write_bytes(resp.read())
    src = TEXMF / "src"
    if src.exists():
        pass
    with zipfile.ZipFile(zip_path) as zf:
        zf.extractall(src)
    ins_dir = next(src.rglob("foiltex.ins")).parent
    subprocess.run(
        ["latex", "-interaction=nonstopmode", "foiltex.ins"],
        cwd=ins_dir,
        check=True,
        capture_output=True,
        text=True,
    )
    for pattern in ("*.cls", "*.clo", "*.sty", "*.tex"):
        for path in ins_dir.glob(pattern):
            if path.name.startswith("foiltex"):
                continue
            dest = TEXMF / path.name
            dest.write_bytes(path.read_bytes())
    if not cls.is_file():
        raise SystemExit(f"unpacking FoilTeX did not produce {cls}")
    return TEXMF


def _find_graphic(name: str) -> Path | None:
    base = Path(name).name
    stem = Path(base).stem
    for directory in (
        ROOT / "slides" / "diagrams" / "npa",
        ROOT / "slides" / "diagrams" / "logos",
        ROOT / "diagrams",
        ROOT,
    ):
        for candidate in (
            directory / base,
            directory / f"{stem}.png",
            directory / f"{stem}.pdf",
            directory / f"{stem}.eps",
        ):
            if candidate.is_file():
                return candidate
    return None


def stage_graphics(tex_path: Path) -> None:
    """Copy/rasterize figures into the compile directory so epstopdf can see them."""
    tex = tex_path.read_text(encoding="utf-8")
    names = re.findall(r"\\includegraphics(?:\[[^\]]*\])?\{([^}]+)\}", tex)
    dest = tex_path.parent
    replacements: dict[str, str] = {}
    for name in names:
        src = _find_graphic(name)
        if src is None:
            print(f"missing graphic {name}")
            continue
        if src.suffix.lower() == ".eps":
            pdf = dest / f"{src.stem}.pdf"
            subprocess.run(
                [
                    "gs",
                    "-dSAFER",
                    "-dBATCH",
                    "-dNOPAUSE",
                    "-dQUIET",
                    "-dEPSCrop",
                    "-sDEVICE=pdfwrite",
                    f"-sOutputFile={pdf}",
                    str(src),
                ],
                check=False,
            )
            if pdf.is_file():
                replacements[name] = pdf.name
                continue
        target = dest / src.name
        if src.resolve() != target.resolve():
            target.write_bytes(src.read_bytes())
        if name != src.name:
            replacements[name] = src.name
    for old, new in replacements.items():
        tex = tex.replace("{" + old + "}", "{" + new + "}")
    tex_path.write_text(tex, encoding="utf-8")


def _bib_search_path() -> str:
    """LyX \\bibtex{lawrence,other,zbooks} resolves via the publications tree."""
    home = Path.home()
    dirs = [
        home / "lawrennd" / "publications" / "papers",
        home / "lawrennd" / "publications" / "tex",
        home / "lawrennd" / "bibliography",
        home / "SheffieldML" / "publications" / "bib",
    ]
    parts = [str(path) + "//" for path in dirs if path.is_dir()]
    existing = os.environ.get("BIBINPUTS", "")
    if existing:
        parts.append(existing)
    return os.pathsep.join(parts)


def compile_tex(tex_path: Path, texmf: Path) -> Path:
    """pdflatex, bibtex, pdflatex x2. Output PDF next to the .tex file."""
    env = os.environ.copy()
    texinputs = os.pathsep.join(
        [
            str(texmf) + "//",
            str(ROOT),
            str(ROOT / "diagrams"),
            str(ROOT / "slides" / "diagrams" / "logos"),
            env.get("TEXINPUTS", ""),
        ]
    )
    env["TEXINPUTS"] = texinputs
    env["BIBINPUTS"] = _bib_search_path()
    latex = [
        "pdflatex",
        "-interaction=nonstopmode",
        "-shell-escape",
        tex_path.name,
    ]

    def run(cmd: list[str]) -> tuple[int, str]:
        proc = subprocess.run(cmd, cwd=tex_path.parent, env=env, capture_output=True)
        log_text = (proc.stdout + b"\n" + proc.stderr).decode("latin-1", errors="replace")
        return proc.returncode, log_text

    code, log_text = run(latex)
    aux = tex_path.with_suffix(".aux")
    if aux.is_file() and r"\bibdata" in aux.read_text(encoding="latin-1", errors="replace"):
        bcode, blog = run(["bibtex", tex_path.stem])
        (tex_path.parent / (tex_path.stem + ".bibtex.out")).write_text(blog, encoding="utf-8")
        if bcode != 0:
            print(f"bibtex reported errors (exit {bcode})")
        code, log_text = run(latex)
        code, log_text = run(latex)
    else:
        code, log_text = run(latex)
    (tex_path.parent / (tex_path.stem + ".pdflatex.out")).write_text(
        log_text, encoding="utf-8"
    )
    pdf = tex_path.with_suffix(".pdf")
    if not pdf.is_file():
        tail = log_text[-3000:]
        raise SystemExit(f"pdflatex produced no PDF for {tex_path}.\n{tail}")
    if code != 0:
        print(f"pdflatex reported errors (exit {code}); PDF still written to {pdf}")
    return pdf


def media_box(pdf: Path) -> tuple[float, float, int]:
    from pypdf import PdfReader

    reader = PdfReader(str(pdf))
    box = reader.pages[0].mediabox
    return float(box.width), float(box.height), len(reader.pages)


def _foil_titles(tex: str) -> list[str]:
    titles: list[str] = []
    i = 0
    while True:
        j = tex.find(r"\foilhead", i)
        if j < 0:
            break
        k = j + len(r"\foilhead")
        if k < len(tex) and tex[k] == "[":
            depth = 1
            k += 1
            while k < len(tex) and depth:
                if tex[k] == "[":
                    depth += 1
                elif tex[k] == "]":
                    depth -= 1
                k += 1
        if k >= len(tex) or tex[k] != "{":
            i = max(k, j + 1)
            continue
        k += 1
        depth = 1
        start = k
        while k < len(tex) and depth:
            if tex[k] == "{":
                depth += 1
            elif tex[k] == "}":
                depth -= 1
            k += 1
        titles.append(tex[start : k - 1])
        i = k
    return titles


def report_overflow_pages(pdf: Path, tex_path: Path, n_pages: int) -> None:
    """Foils that spill past one page are the extra pages versus a 1-foil-per-page deck."""
    from mapping import lecture_for_foil

    log = (tex_path.parent / (tex_path.stem + ".log")).read_text(
        encoding="latin-1", errors="replace"
    )
    hits = [(int(a), int(b)) for a, b in re.findall(r"NPAFOIL\s+(\d+)\s+PAGE\s+(\d+)", log)]
    # Last pdflatex pass may duplicate; keep the last page number for each foil index.
    start_page: dict[int, int] = {}
    for index, page in hits:
        start_page[index] = page
    if not start_page:
        print("page map: no NPAFOIL markers in the log")
        return
    titles = _foil_titles(tex_path.read_text(encoding="utf-8"))
    # Skip the renewcommand's \foilhead in the preamble.
    titles = [t for t in titles if t not in {r"#2", r"\refname"}]
    overflow: list[tuple[int, int, str, str, int]] = []
    by_lecture: dict[str, int] = {}
    indices = sorted(start_page)
    for pos, index in enumerate(indices):
        start = start_page[index]
        end = start_page[indices[pos + 1]] if pos + 1 < len(indices) else n_pages + 1
        n = max(1, end - start)
        extra = n - 1
        lid = lecture_for_foil(index) or ""
        title = titles[index - 1] if 0 < index <= len(titles) else "?"
        if extra:
            overflow.append((index, extra, lid, title, n))
            by_lecture[lid or "unknown"] = by_lecture.get(lid or "unknown", 0) + extra
    extra_total = sum(item[1] for item in overflow)
    title_pages = start_page[indices[0]] - 1
    print(
        f"page map: {n_pages} pages = title {title_pages}p + {len(indices)} foils "
        f"+ {extra_total} overflow ({len(overflow)} foils longer than one page)"
    )
    print("overflow by lecture:")
    for lid, extra in sorted(by_lecture.items(), key=lambda kv: -kv[1]):
        print(f"  +{extra:3d}p  {lid or '-'}")
    overflow.sort(key=lambda row: -row[1])
    print("longest foils:")
    for index, extra, lid, title, n in overflow[:15]:
        plain = re.sub(r"\\(?:emph|textbf|label)\{([^}]*)\}", r"\1", title)
        plain = re.sub(r"\\[A-Za-z]+", "", plain)
        plain = re.sub(r"[{}$]", "", plain)
        print(f"  +{extra}p  foil {index:3d}  {lid or '-':24s}  {plain[:58]}  ({n} pages)")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--lyx",
        type=Path,
        default=ROOT / "lectureSlides.lyx",
        help="LyX FoilTeX source",
    )
    parser.add_argument(
        "--tex",
        type=Path,
        default=BUILD / "slides.tex",
        help="Where to write/read the FoilTeX .tex",
    )
    args = parser.parse_args(argv)

    texmf = ensure_foiltex()
    args.tex.parent.mkdir(parents=True, exist_ok=True)
    doc = parse_file(args.lyx)
    args.tex.write_text(document_to_tex(doc), encoding="utf-8")
    print(f"wrote {args.tex}")
    stage_graphics(args.tex)

    try:
        pdf = compile_tex(args.tex, texmf)
    except SystemExit as exc:
        # Keep a PDF if pdflatex wrote one before the error.
        maybe = args.tex.with_suffix(".pdf")
        if maybe.is_file():
            w, h, n = media_box(maybe)
            print(f"partial PDF {maybe.name}: {n} pages, MediaBox {w:.0f}x{h:.0f}")
        raise SystemExit(exc) from None

    w, h, n = media_box(pdf)
    portrait = h > w
    print(f"{pdf}: {n} pages, MediaBox {w:.0f}x{h:.0f} ({'portrait' if portrait else 'landscape'})")
    report_overflow_pages(pdf, args.tex, n)
    if not portrait:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
