"""Smoke tests for the LyX conversion pipeline."""

from __future__ import annotations

import re
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


def test_expand_answers_and_slides_stay_off_notes():
    from emit_lamd import polish_notes, units_to_slides, split_tex_units

    raw = r"""
\notes{1. Nightclub. \answer{
  Waiting time $\bar{T}=1/2$. \}{0}}
"""
    out = polish_notes(raw)
    assert r"\answer{" not in out, out
    assert r"\subsection{Answer}" in out
    assert "Waiting time" in out
    bracketed = r"""
\notes{Question text.
  [0]
    Because $\rho=0.9$.
\}{0}
"""
    out2 = polish_notes(bracketed)
    assert r"\}{0}" not in out2, out2
    assert "Because" in out2

    from emit_tex import document_to_tex

    doc = parse_file(ROOT / "lectureSlides.lyx")
    md = units_to_slides(split_tex_units(document_to_tex(doc)))
    assert "<!-- original A4 foil" not in md
    if r"\figure{" in md:
        assert r"\slides{\figure{" in md.replace("\n", "")


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


def test_foils_preamble_is_portrait_letter():
    from emit_tex import document_to_tex

    doc = parse_file(ROOT / "lectureSlides.lyx")
    tex = document_to_tex(doc)
    assert r"\documentclass[20pt,letterpaper]{foils}" in tex
    assert r"\providecommand{\foilhead}[1]{\section{#1}}" not in tex
    assert r"\foilhead[-0.5in]{" in tex
    assert r"\leftheader{Neil Lawrence}" in tex
    assert r"\maketitle" in tex
    assert r"\item[Lab\]" not in tex
    assert "Lab~Classes" in tex
    body = tex.split(r"\begin{document}", 1)[-1]
    assert body.count(r"\foilhead[-0.5in]{") == 243
    assert r"\begin{tabular}{lll}" in tex
    assert not re.search(r"\\begin\{tabular\}\s*\n", tex)
    assert r"\foilhead[-0.5in]{Reading List \& Evaluation}" in tex
    assert r"Lectures 1 \& 2" in tex
    assert r"\tiny" in tex
    assert r"\tiny\normalsize" not in tex
    tiny_at = tex.find(r"\tiny")
    tab_at = tex.find(r"\begin{tabular}{lll}")
    norm_at = tex.find(r"\normalsize")
    assert 0 <= tiny_at < tab_at < norm_at
    assert r"\bibtex" not in tex
    assert r"\bibliographystyle{abbrvnat}" in tex
    assert r"\bibliography{lawrence,other,zbooks}" in tex
    assert r"\renewcommand{\bibsection}" in tex


def test_pdf_sanitize_strips_figure_chrome_and_math():
    from emit_lamd import notes_wrap, prepare_tex_body, strip_figure_chrome

    leftover = r"""
ARPANET was predecessor of the internet.
  [ht]
    \caption{The ARPANET in 1975.}
"""
    cleaned = strip_figure_chrome(leftover)
    assert r"\caption" not in cleaned
    assert "[ht]" not in cleaned
    assert "ARPANET was predecessor" in cleaned

    math = r"also see expectations written in the form $E\left\{ f\left(x\right)\right\} $."
    wrapped = notes_wrap(math)
    assert r"\left\lbrace" in wrapped
    assert r"\$E\left" not in wrapped

    cases = r"\mu_{k}=\left\{ {cc} k\mu & k=0 \\ m\mu & k>m\right."
    out = prepare_tex_body(cases)
    assert r"\begin{array}{cc}" in out
    assert r"\end{array}" in out
    # Do not rewrite \right) belonging to \left(k-1\right).
    balanced = r"\lambda P\left(k-1\right)=\mu P\left(k\right)"
    assert r"\end{array}" not in prepare_tex_body(balanced)

    from emit_lamd import fix_cases_arrays

    table = r"\begin{tabular}{lll}" + "\n  a & b & c \\\\\n\\end{tabular}"
    assert r"\begin{tabular}{lll}" in fix_cases_arrays(table)


def test_overlay_foilheads_keep_their_bodies():
    from emit_tex import document_to_tex
    from lyx14 import Heading, parse_file

    doc = parse_file(ROOT / "lectureSlides.lyx")
    blocks = doc.blocks
    titles = []
    for i, block in enumerate(blocks):
        if isinstance(block, Heading) and block.layout in {"ShortFoilhead", "Foilhead"}:
            titles.append((i, "".join(getattr(r, "text", "") for r in block.runs)))
    seq = [i for i, title in titles if title == "Average Number in System II"]
    assert len(seq) == 8, len(seq)
    for pos, block_i in enumerate(seq):
        nxt = titles[titles.index((block_i, "Average Number in System II")) + 1][0] if pos + 1 < len(seq) else None
        # Use the next heading of any kind as the end of this foil.
        end = len(blocks)
        for j, other in enumerate(blocks[block_i + 1 :], block_i + 1):
            if isinstance(other, Heading) and other.layout in {"ShortFoilhead", "Foilhead"}:
                end = j
                break
        body = blocks[block_i + 1 : end]
        assert body, f"overlay frame {pos} has no body"

    tex = document_to_tex(doc)
    chunks = tex.split(r"\foilhead[-0.5in]{Average Number in System II}")
    assert len(chunks) == 9, len(chunks)  # split yields preamble + 8 frames
    for i, chunk in enumerate(chunks[1:], 1):
        next_head = chunk.find(r"\foilhead[-0.5in]{")
        body = chunk if next_head < 0 else chunk[:next_head]
        assert r"\begin{eqnarray" in body or r"\left\langle k" in body, f"frame {i} empty: {body[:80]!r}"


def test_escape_bare_ampersands():
    from emit_tex import escape_bare_ampersands

    body = "Reading List & Evaluation\n\\begin{tabular}{ll}\n  a & b \\\\\n\\end{tabular}\nnode 1 & 5"
    out = escape_bare_ampersands(body)
    assert r"Reading List \& Evaluation" in out
    assert r"  a & b \\" in out
    assert r"node 1 \& 5" in out


if __name__ == "__main__":
    test_expand_answers_and_slides_stay_off_notes()
    print("notes polish ok")
    test_mapping()
    print("mapping ok")
    test_parse_notes_chapters()
    print("notes chapters ok")
    test_parse_slides_foils()
    print("slides foils ok")
    test_collect_foils_from_tex()
    print("collect foils ok")
    test_foils_preamble_is_portrait_letter()
    print("foils preamble ok")
    test_pdf_sanitize_strips_figure_chrome_and_math()
    print("pdf sanitize ok")
    test_overlay_foilheads_keep_their_bodies()
    print("overlay bodies ok")
    test_escape_bare_ampersands()
    print("ampersands ok")
