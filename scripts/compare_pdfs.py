#!/usr/bin/env python3
"""Compare reconstructed LaMD PDFs against the 2006 lecturer notes and FoilTeX slides.

Notes text comes from pypdf on lectureNotesLecturer.pdf. FoilTeX slides use
custom fonts that pypdf cannot decode, so slide text is OCR of lectureSlides.pdf
(cached at build/conversion/old-slides-ocr.txt). Page counts are diagnostics.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts" / "convert"))

from mapping import (  # noqa: E402
    CHAPTER_TO_LECTURE,
    LECTURES,
    lecture_for_foil,
    normalise_title,
)

WORD_RE = re.compile(r"[A-Za-z0-9]+")
WORD_FLOOR = 0.50  # PDF/OCR extraction is lossy versus markdown.
OCR_CACHE = ROOT / "build" / "conversion" / "old-slides-ocr.txt"
SLIDES_TEX = ROOT / "build" / "conversion" / "slides.tex"


def words(text: str) -> list[str]:
    return WORD_RE.findall(text.lower())


def word_set(text: str) -> set[str]:
    return {w for w in words(text) if len(w) > 2}


def extract_pdf_text(path: Path) -> str:
    try:
        from pypdf import PdfReader
    except ImportError as exc:  # pragma: no cover
        raise SystemExit(f"pypdf is required to read {path}: {exc}") from exc
    reader = PdfReader(str(path))
    parts: list[str] = []
    for page in reader.pages:
        parts.append(page.extract_text() or "")
    return "\n".join(parts)


def page_count(path: Path) -> int:
    from pypdf import PdfReader

    return len(PdfReader(str(path)).pages)


def media_box(path: Path) -> str:
    from pypdf import PdfReader

    page = PdfReader(str(path)).pages[0]
    box = page.mediabox
    return f"{float(box.width):.0f}x{float(box.height):.0f}"


def find_pdf(kind: str, lecture_id: str, extra_dirs: list[Path]) -> Path | None:
    """kind is 'notes' or 'slides'."""
    patterns = [f"*{lecture_id}.{kind}.pdf", f"*{lecture_id}*.{kind}.pdf"]
    search = extra_dirs + [
        ROOT / "build" / "pdf",
        ROOT / "_notes",
        ROOT / "slides",
        ROOT / "_lamd",
    ]
    for directory in search:
        if not directory.is_dir():
            continue
        for pattern in patterns:
            hits = sorted(directory.glob(pattern))
            if hits:
                return hits[-1]
    return None


def split_old_notes(text: str) -> dict[str, str]:
    """Split lecturer notes PDF text into lecture buckets via chapter titles."""
    buckets: dict[str, list[str]] = {
        lid: [] for lid, meta in LECTURES.items() if meta["kind"] == "lecture"
    }
    current: str | None = None
    for raw_line in text.splitlines():
        line = raw_line.strip()
        if not line:
            continue
        lid = None
        norm = normalise_title(line)
        if norm:
            for prefix, lecture_id in CHAPTER_TO_LECTURE:
                if prefix in norm and lecture_id in buckets:
                    lid = lecture_id
                    break
        if lid:
            current = lid
            continue
        if current:
            buckets[current].append(line)
    return {k: "\n".join(v) for k, v in buckets.items()}


def parse_foil_titles(tex: str) -> list[tuple[int, str, str]]:
    """Return (1-based index, lecture_id, title) for each \\foilhead."""
    titles: list[tuple[int, str, str]] = []
    needle = "\\foilhead{"
    i = 0
    index = 0
    while True:
        j = tex.find(needle, i)
        if j < 0:
            break
        start = j + len(needle)
        depth = 1
        k = start
        while k < len(tex) and depth:
            if tex[k] == "{":
                depth += 1
            elif tex[k] == "}":
                depth -= 1
            k += 1
        index += 1
        title = tex[start : k - 1]
        lid = lecture_for_foil(index) or ""
        titles.append((index, lid, title))
        i = k
    return titles


_STOP = {"the", "and", "for", "with", "from", "into", "that", "this", "a"}


def _title_tokens(title: str) -> list[str]:
    return [
        t
        for t in normalise_title(title).split()
        if len(t) > 2 and t not in _STOP
    ]


def heading_present(title: str, text: str) -> bool:
    norm_text = normalise_title(text)
    tokens = _title_tokens(title)
    if not tokens:
        return False
    return all(tok in norm_text for tok in tokens)


def _line_is_foil_title(line: str, title: str) -> bool:
    """True when an OCR line looks like this foilhead, not a mention in body text."""
    tokens = _title_tokens(title)
    if not tokens:
        return False
    norm_line = normalise_title(line)
    norm_title = normalise_title(title)
    if not all(tok in norm_line for tok in tokens):
        return False
    if len(norm_line) > max(72, len(norm_title) + 24):
        return False
    # One-token titles ("Examples", "Monopoly") must be an exact heading.
    if len(tokens) < 2:
        return norm_line == norm_title or norm_line.endswith(norm_title)
    return True


def _lecture_for_slide_page(page: int, n_pages: int = 236, n_foils: int = 243) -> str | None:
    """Map a FoilTeX PDF page to a lecture via the 1-based foil index ranges."""
    foil = int(round(page * n_foils / n_pages))
    foil = max(1, min(n_foils, foil))
    return lecture_for_foil(foil)


def split_old_slides(ocr_text: str, foils: list[tuple[int, str, str]]) -> dict[str, str]:
    """Split OCR of lectureSlides.pdf by page using FOIL_RANGES, not running headers."""
    del foils  # titles are used for recall, not for this split
    buckets: dict[str, list[str]] = defaultdict(list)
    parts = re.split(r"----- PAGE page-(\d+) -----", ocr_text)
    for k in range(1, len(parts), 2):
        page = int(parts[k])
        text = parts[k + 1] if k + 1 < len(parts) else ""
        lines = [ln.strip() for ln in text.splitlines() if ln.strip()]
        lid = _lecture_for_slide_page(page)
        if lid and lines:
            buckets[lid].extend(lines)
    return {k: "\n".join(v) for k, v in buckets.items()}


def overlap_ratio(new_text: str, old_text: str) -> float:
    """Precision: fraction of reconstructed tokens that appear in the original."""
    new_w = word_set(new_text)
    old_w = word_set(old_text)
    if not new_w or not old_w:
        return 0.0
    return len(new_w & old_w) / len(new_w)


def recall_ratio(new_text: str, old_text: str) -> float:
    """Recall: fraction of original tokens that appear in the reconstruction."""
    new_w = word_set(new_text)
    old_w = word_set(old_text)
    if not new_w or not old_w:
        return 0.0
    return len(new_w & old_w) / len(old_w)


def foil_recall(foils: list[tuple[int, str, str]], lecture_id: str, slides_text: str) -> tuple[int, int]:
    titles = [title for _, lid, title in foils if lid == lecture_id]
    hits = sum(1 for title in titles if heading_present(title, slides_text))
    return hits, len(titles)


def load_old_slides_text(path: Path, cache: Path) -> tuple[str, str]:
    """Return (text, source_label). Prefer OCR cache; pypdf is usually empty for FoilTeX."""
    if cache.is_file() and cache.stat().st_size > 1000:
        return cache.read_text(encoding="utf-8", errors="replace"), "ocr"
    raw = extract_pdf_text(path)
    letters = sum(c.isalpha() for c in raw)
    if letters > 500:
        return raw, "pypdf"
    raise SystemExit(
        f"Cannot extract text from {path.name} (FoilTeX fonts). "
        f"OCR cache missing at {cache}. Render pages and run tesseract first."
    )


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--old-notes", type=Path, default=ROOT / "lectureNotesLecturer.pdf")
    parser.add_argument("--old-slides", type=Path, default=ROOT / "lectureSlides.pdf")
    parser.add_argument("--ocr-cache", type=Path, default=OCR_CACHE)
    parser.add_argument(
        "--out",
        type=Path,
        default=ROOT / "build" / "conversion" / "pdf-compare.md",
    )
    parser.add_argument(
        "--json",
        type=Path,
        default=ROOT / "build" / "conversion" / "pdf-compare.json",
    )
    args = parser.parse_args()

    lectures = [lid for lid, meta in LECTURES.items() if meta["kind"] == "lecture"]
    old_notes_text = extract_pdf_text(args.old_notes)
    old_slides_text, slides_source = load_old_slides_text(args.old_slides, args.ocr_cache)
    old_notes_pages = page_count(args.old_notes)
    old_slides_pages = page_count(args.old_slides)
    old_notes_box = media_box(args.old_notes)
    old_slides_box = media_box(args.old_slides)
    old_notes_by = split_old_notes(old_notes_text)
    foils = parse_foil_titles(SLIDES_TEX.read_text(encoding="utf-8")) if SLIDES_TEX.is_file() else []
    old_slides_by = split_old_slides(old_slides_text, foils)

    lines: list[str] = [
        "# NPA PDF reconstruction comparison",
        "",
        f"Old notes: `{args.old_notes.name}` ({old_notes_pages} pages, MediaBox {old_notes_box}), text via pypdf.",
        f"Old slides: `{args.old_slides.name}` ({old_slides_pages} pages, MediaBox {old_slides_box}), text via {slides_source}.",
        "",
        "Page counts are diagnostics. Notes pass at "
        f"{WORD_FLOOR:.0%} token precision versus `lectureNotesLecturer.pdf`.",
        "Slides pass at that floor versus OCR of `lectureSlides.pdf`, or when at least",
        "75% of original foil titles appear in the reconstructed Beamer PDF (FoilTeX math OCR is lossy).",
        "",
        "| Lecture | Notes pp | Slides pp | Notes | Slides | Slide recall | Foil titles | Result |",
        "|---|---:|---:|---:|---:|---:|---|---|",
    ]

    rows: list[dict] = []
    failures = 0
    for lecture_id in lectures:
        meta = LECTURES[lecture_id]
        notes_pdf = find_pdf("notes", lecture_id, [ROOT / "build" / "pdf"])
        slides_pdf = find_pdf("slides", lecture_id, [ROOT / "build" / "pdf"])
        notes_ok = notes_pdf is not None
        slides_ok = slides_pdf is not None
        notes_pages = page_count(notes_pdf) if notes_pdf else 0
        slides_pages = page_count(slides_pdf) if slides_pdf else 0
        notes_text = extract_pdf_text(notes_pdf) if notes_pdf else ""
        slides_text = extract_pdf_text(slides_pdf) if slides_pdf else ""

        old_notes_target = old_notes_by.get(lecture_id) or old_notes_text
        # 2006 notes keep ARQ inside the M/G/1 chapter; score both against the union.
        if lecture_id in {"mg1", "mg1-arq"}:
            old_notes_target = "\n".join(
                t for t in (old_notes_by.get("mg1"), old_notes_by.get("mg1-arq")) if t
            ) or old_notes_target
        old_slides_target = old_slides_by.get(lecture_id) or old_slides_text
        notes_overlap = overlap_ratio(notes_text, old_notes_target)
        slides_overlap = overlap_ratio(slides_text, old_slides_target)
        slides_recall = recall_ratio(slides_text, old_slides_target)
        foil_hits, foil_total = foil_recall(foils, lecture_id, slides_text)
        foil_ratio = (foil_hits / foil_total) if foil_total else 0.0
        title_ok = heading_present(meta["title"], notes_text + "\n" + slides_text)
        slides_content_ok = slides_overlap >= WORD_FLOOR or foil_ratio >= 0.75

        passed = (
            notes_ok
            and slides_ok
            and title_ok
            and notes_overlap >= WORD_FLOOR
            and slides_content_ok
        )
        if not passed:
            failures += 1
        rows.append(
            {
                "id": lecture_id,
                "title": meta["title"],
                "notes_pdf": notes_pdf.name if notes_pdf else None,
                "slides_pdf": slides_pdf.name if slides_pdf else None,
                "notes_pages": notes_pages,
                "slides_pages": slides_pages,
                "notes_overlap": round(notes_overlap, 4),
                "slides_overlap": round(slides_overlap, 4),
                "slides_recall": round(slides_recall, 4),
                "foil_hits": foil_hits,
                "foil_total": foil_total,
                "title_ok": title_ok,
                "passed": passed,
            }
        )
        lines.append(
            "| {id} | {np} | {sp} | {no:.0%} | {so:.0%} | {sr:.0%} | {fh}/{ft} | {res} |".format(
                id=lecture_id,
                np=notes_pages,
                sp=slides_pages,
                no=notes_overlap,
                so=slides_overlap,
                sr=slides_recall,
                fh=foil_hits,
                ft=foil_total,
                res="pass" if passed else "fail",
            )
        )

    n_pass = len(lectures) - failures
    lines.extend(
        [
            "",
            f"**Result:** {n_pass}/{len(lectures)} lectures passed "
            f"(notes vs `{args.old_notes.name}`, slides vs `{args.old_slides.name}`).",
            "",
        ]
    )
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text("\n".join(lines) + "\n", encoding="utf-8")
    payload = {
        "old_notes": args.old_notes.name,
        "old_slides": args.old_slides.name,
        "old_notes_pages": old_notes_pages,
        "old_slides_pages": old_slides_pages,
        "slides_text_source": slides_source,
        "word_floor": WORD_FLOOR,
        "passed": n_pass,
        "total": len(lectures),
        "lectures": rows,
    }
    args.json.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(args.out.read_text(encoding="utf-8"))
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
