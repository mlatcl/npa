#!/usr/bin/env python3
"""LyX → LaTeX → LaMD conversion for the NPA archive.

Notes and slides are converted independently from lectureNotes.lyx and
lectureSlides.lyx. Each A4 foil is split into two Reveal slides unless it is
already short. Fidelity checks fail the run if the notes lose more than 10% of
the LyX word count.
"""

from __future__ import annotations

import argparse
import re
import shutil
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
sys.path.insert(0, str(HERE))

from emit_lamd import (  # noqa: E402
    collect_foils,
    foil_to_slides,
    normalise_overlay,
    split_foil_units,
    split_tex_units,
    units_to_notes,
    write_snippet,
)
from emit_tex import document_to_tex  # noqa: E402
from fidelity import compare, lamd_stats, lyx_stats, tex_stats, write_report  # noqa: E402
from lyx14 import parse_file  # noqa: E402
from mapping import (  # noqa: E402
    EXERCISES,
    LECTURES,
    PYTHON_INCLUDES,
    READINGS,
    lecture_for_chapter,
    lecture_for_foil,
)

BUILD = ROOT / "build" / "conversion"
GEN_NOTES = ROOT / "snippets" / "_npa" / "generated" / "notes"
GEN_SLIDES = ROOT / "snippets" / "_npa" / "generated" / "slides"
LAMD = ROOT / "_lamd"


def split_by_macro(tex: str, macro: str) -> list[tuple[str, str]]:
    """Return (title, body) chunks starting at each \\macro{title}."""
    pattern = rf"^\\{macro}\*?\{{(.*)\}}\s*$"
    import re

    lines = tex.splitlines()
    chunks: list[tuple[str, list[str]]] = []
    current_title = ""
    current: list[str] = []
    for line in lines:
        m = re.match(pattern, line.strip())
        if m:
            if current_title or current:
                chunks.append((current_title, current))
            current_title = m.group(1)
            current = [line]
            continue
        current.append(line)
    if current_title or current:
        chunks.append((current_title, current))
    return [(t, "\n".join(b) + "\n") for t, b in chunks]


def split_mg1(body: str) -> tuple[str, str]:
    """ARQ is a section of the M/G/1 chapter; it is its own lecture."""
    import re

    m = re.search(r"^\\section\{Automatic Repeat Request.*$", body, re.M)
    if not m:
        return body, ""
    return body[: m.start()], body[m.start() :]


def guard_name(prefix: str, lecture_id: str) -> str:
    parts = "".join(p.title() for p in lecture_id.replace("-", " ").split())
    return f"npaGen{prefix}{parts}"


def write_lecture_files(notes_by: dict[str, str], slides_by: dict[str, str]) -> None:
    for lecture_id, meta in LECTURES.items():
        if meta["kind"] != "lecture":
            continue
        notes_path = GEN_NOTES / f"{lecture_id}.md"
        slides_path = GEN_SLIDES / f"{lecture_id}.md"
        if lecture_id in notes_by:
            write_snippet(notes_path, guard_name("Notes", lecture_id), notes_by[lecture_id])
        if lecture_id in slides_by:
            write_snippet(slides_path, guard_name("Slides", lecture_id), slides_by[lecture_id])
        dest = LAMD / f"{lecture_id}.md"
        dest.write_text(lecture_markdown(lecture_id, meta), encoding="utf-8")


def lecture_markdown(lecture_id: str, meta: dict) -> str:
    fm = [
        "---",
        f"week: {meta['week']}",
        f"session: {meta['session']}",
        f"title: {meta['title']!r}".replace("'", '"')
        if False
        else f'title: "{meta["title"]}"',
        "abstract: >",
    ]
    abstract = meta["abstract"].rstrip()
    for line in abstract.split("\n"):
        fm.append(f"  {line}")
    fm.append(f"date: {meta['date']}")
    if meta.get("featured_image"):
        fm.append(f"featured_image: {meta['featured_image']}")
    fm.append("---")
    body = [
        "",
        f"\\include{{snippets/_npa/generated/notes/{lecture_id}.md}}",
    ]
    for path in PYTHON_INCLUDES.get(lecture_id, []):
        body.append(f"\\include{{{path}}}")
    body.append(f"\\include{{snippets/_npa/generated/slides/{lecture_id}.md}}")
    body.append("")
    for key, note in READINGS.get(lecture_id, []):
        body.append(f"\\addreading{{{key}}}{{{note}}}")
    if READINGS.get(lecture_id):
        body.append("")
    for key, note in EXERCISES.get(lecture_id, []):
        body.append(f"\\addexercise{{{key}}}{{{note}}}")
    if EXERCISES.get(lecture_id):
        body.append("")
    body.extend(
        [
            "\\thanks",
            "",
            "\\reading",
            "",
        ]
    )
    if EXERCISES.get(lecture_id):
        body.extend(["\\exercises", ""])
    body.extend(["\\references", ""])
    return "\n".join(fm + body)


def convert_notes(lyx_path: Path) -> tuple[str, dict[str, str], dict]:
    doc = parse_file(lyx_path)
    tex = document_to_tex(doc)
    (BUILD / "notes.tex").write_text(tex, encoding="utf-8")
    notes_by: dict[str, list[str]] = {}
    for title, chunk in split_by_macro(tex, "chapter"):
        lecture_id = lecture_for_chapter(title) if title else "course-info-practical"
        if lecture_id is None:
            lecture_id = "course-info-practical"
        if lecture_id == "mg1":
            main, arq = split_mg1(chunk)
            notes_by.setdefault("mg1", []).append(units_to_notes(split_tex_units(main)))
            if arq.strip():
                notes_by.setdefault("mg1-arq", []).append(
                    units_to_notes(split_tex_units(arq))
                )
            continue
        notes_by.setdefault(lecture_id, []).append(units_to_notes(split_tex_units(chunk)))
    joined = {k: "\n\n".join(v) for k, v in notes_by.items()}
    return tex, joined, lyx_stats(doc)


def rasterize_missing_diagrams(markdown: str) -> None:
    """Ghostscript-rasterize EPS diagrams that generated snippets include."""
    dest = ROOT / "slides" / "diagrams" / "npa"
    dest.mkdir(parents=True, exist_ok=True)
    stems = set(re.findall(r"\\includepng\{\\diagramsDir/npa/([^}]+)\}", markdown))
    gs = shutil.which("gs")
    if not gs:
        print("ghostscript not found; skip rasterizing diagrams")
        return
    for stem in sorted(stems):
        png = dest / f"{stem}.png"
        if png.exists():
            continue
        eps = ROOT / "diagrams" / f"{stem}.eps"
        if not eps.exists():
            print(f"missing diagram source for {stem}")
            continue
        subprocess.run(
            [
                gs,
                "-dSAFER",
                "-dBATCH",
                "-dNOPAUSE",
                "-dQUIET",
                "-sDEVICE=png16m",
                "-r150",
                f"-sOutputFile={png}",
                str(eps),
            ],
            check=False,
        )


def convert_slides(lyx_path: Path) -> tuple[str, dict[str, str], dict]:
    doc = parse_file(lyx_path)
    tex = document_to_tex(doc)
    (BUILD / "slides.tex").write_text(tex, encoding="utf-8")
    foils = collect_foils(split_tex_units(tex))
    slides_by: dict[str, list[str]] = {}
    for i, foil in enumerate(foils):
        overlay = False
        if i > 0 and normalise_overlay(foils[i - 1].title) == normalise_overlay(foil.title):
            overlay = True
        if i + 1 < len(foils) and normalise_overlay(foils[i + 1].title) == normalise_overlay(
            foil.title
        ):
            overlay = True
        rendered = [
            foil_to_slides(foil.title, chunk, continued=j > 0, orig_index=foil.index)
            for j, chunk in enumerate(split_foil_units(foil, overlay=overlay))
        ]
        lecture_id = lecture_for_foil(foil.index) or "course-info-practical"
        slides_by.setdefault(lecture_id, []).append("\n\n".join(p for p in rendered if p))
    joined = {k: "\n\n".join(v) for k, v in slides_by.items()}
    return tex, joined, lyx_stats(doc)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--notes",
        type=Path,
        default=ROOT / "lectureNotes.lyx",
        help="LyX notes source",
    )
    parser.add_argument(
        "--slides",
        type=Path,
        default=ROOT / "lectureSlides.lyx",
        help="LyX FoilTeX source",
    )
    parser.add_argument(
        "--skip-slides",
        action="store_true",
        help="Convert notes only",
    )
    args = parser.parse_args(argv)
    BUILD.mkdir(parents=True, exist_ok=True)

    notes_tex, notes_by, notes_lyx = convert_notes(args.notes)
    slides_tex, slides_by, slides_lyx = ("", {}, {"words": 0, "figures": 0, "warnings": []})
    if not args.skip_slides:
        slides_tex, slides_by, slides_lyx = convert_slides(args.slides)

    write_lecture_files(notes_by, slides_by)

    all_notes = "\n\n".join(notes_by.values())
    all_slides = "\n\n".join(slides_by.values())
    rasterize_missing_diagrams(all_notes + "\n" + all_slides)
    (BUILD / "notes.md").write_text(all_notes, encoding="utf-8")
    (BUILD / "slides.md").write_text(all_slides, encoding="utf-8")

    report = compare(
        notes_lyx,
        tex_stats(notes_tex),
        lamd_stats(all_notes),
        {"newslides": 0, "words": 0, "figures": 0, "display_equations": 0},
    )
    if slides_tex:
        slide_md = lamd_stats(all_slides)
        sreport = compare(
            slides_lyx,
            tex_stats(slides_tex),
            slide_md,
            slide_md,
            word_floor=0.85,
        )
        for check in sreport.checks:
            if check.name == "lyx-to-notes-words":
                check.name = "lyx-to-slides-words"
            else:
                check.name = "slides-" + check.name
            report.checks.append(check)
    write_report(report, BUILD / "fidelity.md")
    print(report.markdown())
    print(f"wrote {BUILD}")
    print(f"notes lectures: {sorted(notes_by)}")
    print(f"slides lectures: {sorted(slides_by)}")
    return 0 if report.ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
