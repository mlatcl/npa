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

Each original A4 `\foilhead` becomes two Reveal `\newslide`s unless the foil
is already short or is one frame of a same-title overlay sequence.

```bash
python3 scripts/convert/run.py
python3 scripts/convert/test_convert.py
```

Handwritten material in `snippets/_npa/includes/` is not used by the generated
lecture files. Keep it until the conversion is trusted; do not promote generated
snippets into `lawrennd/snippets` yet.

MATLAB examples in the archive are rewritten as Python only where they already
were; this converter preserves mathematics and figures, not the ns-2 labs.
