# Network Performance Analysis

Archive of the University of Sheffield course *Network Performance Analysis*, taught by Neil Lawrence from October 2001 to December 2006.

Module codes over that period were COM 6131 (MSc) with COM 3270 and later COM 4290 (undergraduate). The material covers probability review, Poisson processes, birth–death chains, Markov queues, Little's formula, Erlang delay and loss, and discrete-event simulation (including ns-2 labs).

This repository preserves the lecturer sources, MATLAB and ns-2 labs, past papers, and the student-facing website as last used in 2005–2006.

Lecture notes and slides are being converted to [LaMD](https://github.com/lawrennd/lamd). Converted sources live in `_lamd/`; NPA-specific snippets stay in `snippets/_npa/` in this repository until they are promoted to the central snippets repo. See `_lamd/README.md` for the conversion map. MATLAB helpers are rewritten in `python/npa_plots.py`.

## Notebook smoke tests

Execute numbered lecture and lab notebooks under `_notebooks/` with CI-safe patches (Agg backend, mocked stdin, no widget hangs). The runner is the shared mlatcl harness (`scripts/smoke_notebooks.py`); course defaults live in `scripts/smoke.yml`.

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements-smoke.txt
python scripts/smoke_notebooks.py
# subset: python scripts/smoke_notebooks.py --only 01 03
```

GitHub Actions runs the same harness on pull requests that touch notebooks, `python/`, or the smoke files, weekly on a schedule, and via **workflow_dispatch** (optional `--only` input). Results land in `_notebooks/test-results/` (gitignored) and as a workflow artifact.

## Layout

| Path | What it is |
| --- | --- |
| `*.lyx`, `*.tex` | Lecture notes, slides, tutorials, lab sheets, and exams (LyX / LaTeX) |
| `matlab/` | MATLAB demos: Erlang B/C, exponential sampling, probability diagrams |
| `labs/` | Lab sheets, MATLAB used in labs, and ns-2 scripts (`mm1.tcl`, `multipath.tcl`) |
| `diagrams/` | Figures (xfig, EPS, PDF) |
| `html/` | Lecturer module page for 2005–2006 (COM 6131/3270) |
| `published/` | Student website snapshot from `public_html/campus_only` (COM 6131/4290, 2006). Identical copy existed as `com3270`. Includes notes, slides, labs, tutorials, and ns-2 `source.zip`. |
| `published/source-2005.zip` | Earlier ns-2 scripts from `public_html/NPA/` (November 2005) |
| `published/errata/` | One recorded rate error on the packet-arrival example |

Student mark sheets (`marks.xml`, `marks.xls`, `2002courseworkMarks.xml`) are not included.

## History

Git history starts from the personal CVS repository `~/.lecturescvs` (module `npa`):

1. 4 Sep 2005 — initial NPA files
2. 17 Oct 2005 — further commits, including the 2004 exam source

Most files in that CVS tree were only ever revision 1.1. Later lecture notes, 2005–2006 exams, MATLAB, and compiled handouts lived in the lecturer working copy and were never committed. Those files, and the published website, are added in subsequent commits on top of the CVS conversion.

## Provenance

- CVS: `/Users/neil/dcs/.lecturescvs` (converted with `cvs-fast-export`)
- Working copy: `svnmlprojects/lectures/npa`
- Published site: `old_Dropbox/public_html/campus_only/com6131` (byte-identical to `com3270`), plus `public_html/NPA/source.zip` and `public_html/errata/COM6131`
