"""Smoke tests for the LyX conversion pipeline."""

from __future__ import annotations

from pathlib import Path

from lyx14 import Heading, parse_file
from mapping import lecture_for_chapter, lecture_for_foil

ROOT = Path(__file__).resolve().parents[2]


def test_parse_notes_chapters():
    doc = parse_file(ROOT / "lectureNotes.lyx")
    chapters = [
        b for b in doc.blocks if isinstance(b, Heading) and b.layout.startswith("Chapter")
    ]
    assert len(chapters) >= 13, len(chapters)


def test_parse_slides_foils():
    doc = parse_file(ROOT / "lectureSlides.lyx")
    foils = [
        b
        for b in doc.blocks
        if isinstance(b, Heading) and b.layout in {"ShortFoilhead", "Foilhead"}
    ]
    assert len(foils) == 243, len(foils)


def test_mapping():
    assert lecture_for_chapter("Little's Formula") == "littles-formula"
    assert lecture_for_chapter(r"$M$/$G$/$1$ Queue") == "mg1"
    assert lecture_for_chapter("Automatic Repeat Request (ARQ) System.") == "mg1-arq"
    assert lecture_for_foil(1) == "course-info-practical"
    assert lecture_for_foil(94) == "littles-formula"
    assert lecture_for_foil(243) == "aloha"


def test_collect_foils_from_tex():
    from emit_tex import document_to_tex
    from emit_lamd import collect_foils, split_tex_units, units_to_slides

    doc = parse_file(ROOT / "lectureSlides.lyx")
    tex = document_to_tex(doc)
    foils = collect_foils(split_tex_units(tex))
    assert len(foils) == 243, len(foils)
    md = units_to_slides(split_tex_units(tex))
    n_new = md.count("\\newslide{")
    assert n_new >= 243, n_new


if __name__ == "__main__":
    test_mapping()
    print("mapping ok")
    test_parse_notes_chapters()
    print("notes chapters ok")
    test_parse_slides_foils()
    print("slides foils ok")
    test_collect_foils_from_tex()
    print("collect foils ok")
