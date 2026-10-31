"""Compare LyX, conversion LaTeX, and LaMD so the second stage cannot silently drop material."""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from pathlib import Path

from lyx14 import Document, Figure, Formula, Graphics, iter_runs, plain_text


WORD_RE = re.compile(r"[A-Za-z0-9]+")


def words(text: str) -> list[str]:
    return WORD_RE.findall(text.lower())


def word_count(text: str) -> int:
    return len(words(text))


def lyx_stats(doc: Document) -> dict:
    from lyx14 import TextRun

    text_parts: list[str] = []
    figures = 0
    equations = 0
    seen_files: set[str] = set()
    for run in iter_runs(doc.blocks):
        if isinstance(run, Graphics) and run.filename not in seen_files:
            figures += 1
            seen_files.add(run.filename)
        elif isinstance(run, Formula):
            if run.tex.startswith(("\\[", "\\begin")):
                equations += 1
        if isinstance(run, TextRun):
            text_parts.append(run.text)
    body = " ".join(text_parts)
    return {
        "words": word_count(body),
        "figures": figures,
        "display_equations": equations,
        "warnings": list(doc.warnings),
    }


def tex_stats(tex: str) -> dict:
    figures = len(re.findall(r"\\includegraphics", tex))
    display = len(re.findall(r"\\\[|\\begin\{equation\}|\\begin\{eqnarray", tex))
    foilheads = len(re.findall(r"^\s*\\foilhead(?:\[[^\]]*\])?\{", tex, re.M))
    chapters = len(re.findall(r"\\chapter", tex))
    # Strip macros for a rough word count of remaining text.
    stripped = re.sub(r"\\[A-Za-z]+\*?(\[[^\]]*\])?\{[^{}]*\}", " ", tex)
    stripped = re.sub(r"\\[\[\]]", " ", stripped)
    return {
        "words": word_count(stripped),
        "figures": figures,
        "display_equations": display,
        "foilheads": foilheads,
        "chapters": chapters,
    }


def lamd_stats(markdown: str) -> dict:
    notes = re.findall(r"\\notes\{", markdown)
    slides = re.findall(r"\\newslide\{", markdown)
    figures = len(re.findall(r"\\includepng", markdown))
    display = len(re.findall(r"\$\$|\\\[|\\begin\{equation\}|\\begin\{eqnarray", markdown))
    stripped = re.sub(r"\\[A-Za-z]+", " ", markdown)
    return {
        "words": word_count(stripped),
        "figures": figures,
        "display_equations": display,
        "notes_blocks": len(notes),
        "newslides": len(slides),
    }


@dataclass
class Check:
    name: str
    ok: bool
    detail: str


@dataclass
class Report:
    checks: list[Check] = field(default_factory=list)

    def add(self, name: str, ok: bool, detail: str) -> None:
        self.checks.append(Check(name, ok, detail))

    @property
    def ok(self) -> bool:
        return all(c.ok for c in self.checks)

    def markdown(self) -> str:
        lines = ["# Conversion fidelity", ""]
        for c in self.checks:
            mark = "ok" if c.ok else "FAIL"
            lines.append(f"- **{mark}** `{c.name}` — {c.detail}")
        return "\n".join(lines) + "\n"


def compare(
    lyx: dict,
    tex: dict,
    lamd_notes: dict,
    lamd_slides: dict,
    word_floor: float = 0.90,
) -> Report:
    report = Report()
    if lyx["words"]:
        ratio = tex["words"] / lyx["words"]
        report.add(
            "lyx-to-tex-words",
            ratio >= word_floor,
            f"LyX {lyx['words']} words → TeX {tex['words']} ({ratio:.0%})",
        )
        nratio = lamd_notes["words"] / lyx["words"]
        report.add(
            "lyx-to-notes-words",
            nratio >= word_floor,
            f"LyX {lyx['words']} words → notes {lamd_notes['words']} ({nratio:.0%})",
        )
    if lyx["figures"]:
        report.add(
            "figures-tex",
            tex["figures"] >= lyx["figures"] * 0.9,
            f"LyX figures {lyx['figures']} → TeX {tex['figures']}",
        )
        report.add(
            "figures-notes",
            lamd_notes["figures"] >= lyx["figures"] * 0.70,
            f"LyX figures {lyx['figures']} → converted {lamd_notes['figures']}",
        )
    if tex.get("foilheads", 0) >= 10:
        report.add(
            "foil-split",
            lamd_slides["newslides"] >= tex["foilheads"],
            f"{tex['foilheads']} A4 foils → {lamd_slides['newslides']} Reveal slides",
        )
    if lyx.get("warnings"):
        report.add(
            "unhandled-insets",
            False,
            f"{len(lyx['warnings'])} parser warnings: " + "; ".join(lyx["warnings"][:8]),
        )
    else:
        report.add("unhandled-insets", True, "no unhandled insets")
    return report


def write_report(report: Report, dest: Path) -> None:
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(report.markdown(), encoding="utf-8")
