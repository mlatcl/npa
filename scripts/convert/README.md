# NPA LyX → LaTeX → LaMD conversion

Canonical sources are `lectureNotes.lyx` and `lectureSlides.lyx`. Notes and
slides are converted independently so the FoilTeX A4 deck is not reconstructed
by summarising the notes.

## Pipeline

1. Parse LyX 1.4 (`lyx14.py`) into a document tree.
2. Emit inspectable LaTeX to `build/conversion/notes.tex` and `slides.tex`.
3. Convert that LaTeX to LaMD snippets under `snippets/_npa/generated/`.
4. Rewrite `_lamd/{lecture}.md` to include the generated notes and slides.
5. Write `build/conversion/fidelity.md` (word, figure, and foil counts).

Each original portrait Letter `\foilhead` becomes two Reveal `\newslide`s
unless the foil is already short or is one frame of a same-title overlay
sequence. The 2006 FoilTeX deck is US Letter portrait (612x792), 20pt; Beamer
PDFs from LaMD are a separate landscape reconstruction.

```bash
python3 scripts/convert/run.py
python3 scripts/convert/test_convert.py
```

To rebuild the **portrait FoilTeX** PDF (not Beamer), after `run.py` or on its
own:

```bash
python3 scripts/convert/compile_foils.py
```

That fetches CTAN FoilTeX into gitignored `build/texmf/` (the class is not in
TeX Live) and writes `build/conversion/slides.pdf`. MediaBox should be
612x792, matching `lectureSlides.pdf`.

PDF reconstruction via LaMD (notes article + Beamer slides) is a separate check.
After `maketalk --format notes --to pdf` and `maketalk --format slides --to pdf`:

```bash
python3 scripts/compare_pdfs.py
```

That compares `_notes/*.notes.pdf` and `slides/*.slides.pdf` (copied to
`build/pdf/`) against `lectureNotesLecturer.pdf` and `lectureSlides.pdf`.
Page counts are diagnostics; the pass is heading recall and token overlap.

Handwritten material in `snippets/_npa/includes/` is not used by the generated
lecture files. Keep it until the conversion is trusted; do not promote generated
snippets into `lawrennd/snippets` yet.

MATLAB examples in the archive are rewritten as Python only where they already
were; this converter preserves mathematics and figures, not the ns-2 labs.
