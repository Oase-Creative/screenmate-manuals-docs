"""
Extract embedded images from a Screenmate PDF booklet into a flat raw/ folder.

Usage:
    python scripts/extract_pdf_images.py <slug>

Reads the PDF for <slug> (per SLUG_TO_PDF map below), writes images to
sources/<slug>/raw/page-NN-img-MM.<ext> and a meta.json index.
"""

import json
import sys
from pathlib import Path

import fitz  # PyMuPDF

INBOX = Path("sources/_inbox/Handleiding Screenmate v2")

SLUG_TO_PDF = {
    "onecable":      "Screenmate - OneCable - Handleiding (v2).pdf",
    "lite":          "Screenmate - Lite - Handleiding (v2).pdf",
    "lite-144hz":    "Screenmate - Lite 144Hz - Handleiding (v2).pdf",
    "dual-flip":     "Screenmate - Dual Flip 16 - Handleiding (v2).pdf",
    "flip-14":       "Screenmate - Flip 14 - Handleiding (v2).pdf",
    "flip-15-6":     "Screenmate - Flip 15.6 - Handleiding (v2).pdf",
    "expand-14":     "Screenmate - Expand 14 - Handleiding.pdf",
    "expand-15-6":   "Screenmate - Expand 15.6 - Handleiding (v2).pdf",
    "infinity":      "Screenmate - Infinity - Handleiding (v2).pdf",
    "infinity-lite": "Screenmate - Infinity Lite - Handleiding (v2) .pdf",
}

MIN_DIM = 60  # drop tiny icons / page-decoration slivers below this


def extract(slug: str) -> None:
    pdf_name = SLUG_TO_PDF.get(slug)
    if pdf_name is None:
        sys.exit(f"unknown slug: {slug}")

    pdf_path = INBOX / pdf_name
    if not pdf_path.exists():
        sys.exit(f"pdf missing: {pdf_path}")

    out_dir = Path("sources") / slug / "raw"
    out_dir.mkdir(parents=True, exist_ok=True)

    # Clear any prior extraction so re-runs are clean.
    for f in out_dir.iterdir():
        if f.is_file():
            f.unlink()

    doc = fitz.open(pdf_path)
    meta = []
    seen_xrefs = set()

    for page_index, page in enumerate(doc, start=1):
        img_list = page.get_images(full=True)
        for img_idx, img_info in enumerate(img_list, start=1):
            xref = img_info[0]
            if xref in seen_xrefs:
                continue  # dedupe — same image re-used across pages
            seen_xrefs.add(xref)

            try:
                pix = fitz.Pixmap(doc, xref)
            except Exception as e:
                print(f"  ! page {page_index} img {img_idx}: extract failed ({e})")
                continue

            if pix.width < MIN_DIM or pix.height < MIN_DIM:
                pix = None
                continue

            # Convert CMYK / alpha to plain RGB PNG for predictability.
            if pix.n - pix.alpha >= 4:
                pix = fitz.Pixmap(fitz.csRGB, pix)

            out_name = f"page-{page_index:02d}-img-{img_idx:02d}.png"
            out_path = out_dir / out_name
            pix.save(out_path)

            meta.append({
                "file": out_name,
                "page": page_index,
                "width": pix.width,
                "height": pix.height,
                "xref": xref,
            })
            pix = None

    (out_dir / "meta.json").write_text(
        json.dumps({"pdf": str(pdf_path), "count": len(meta), "images": meta}, indent=2),
        encoding="utf-8",
    )

    print(f"{slug}: {len(meta)} images -> {out_dir}")


if __name__ == "__main__":
    # OneCable has curated, pre-existing image assets — don't extract by default.
    # Pass `onecable` explicitly if you really want to overwrite.
    DEFAULT_SKIP = {"onecable"}
    targets = sys.argv[1:] or [s for s in SLUG_TO_PDF if s not in DEFAULT_SKIP]
    for slug in targets:
        extract(slug)
