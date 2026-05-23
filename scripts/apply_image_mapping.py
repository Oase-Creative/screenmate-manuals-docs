"""
Apply a raw->target image mapping for a product. Resize for web and place under /images/.

Usage:
    python scripts/apply_image_mapping.py <slug>

Reads sources/<slug>/image-mapping.json with shape:
{
  "mappings": [
    {"raw": "page-04-img-01.png", "target": "/images/Screenmate - Lite - Handleiding images/install-step-1.png"},
    ...
  ],
  "skipped_raw": ["page-01-img-01.png", ...],
  "unmatched_expected": ["/images/.../missing.png", ...],
  "notes": "..."
}

For each mapping:
- Read raw from sources/<slug>/raw/<raw>
- Resize to max width MAX_WIDTH (preserving aspect)
- Save to <target> (relative to repo root; leading / stripped)
"""

import json
import sys
import urllib.parse
from pathlib import Path

from PIL import Image

MAX_WIDTH = 1400  # plenty for retina, still keeps file sizes reasonable
JPEG_QUALITY = 88


def apply(slug: str) -> None:
    mapping_path = Path("sources") / slug / "image-mapping.json"
    if not mapping_path.exists():
        sys.exit(f"missing mapping: {mapping_path}")

    raw_dir = Path("sources") / slug / "raw"
    data = json.loads(mapping_path.read_text(encoding="utf-8"))

    ok = 0
    failed = []

    def normalize_targets(m: dict) -> list[str]:
        # Agents used different field names. Accept all common variants.
        for key in ("target", "expected", "expected_path"):
            v = m.get(key)
            if isinstance(v, str) and v:
                return [v]
        v = m.get("targets")
        if isinstance(v, list):
            return [t for t in v if isinstance(t, str) and t]
        return []

    for m in data.get("mappings", []):
        raw_name = m.get("raw")
        if not raw_name:
            continue
        targets = normalize_targets(m)
        if not targets:
            continue  # null/missing target — agent flagged the raw as unmapped

        raw_path = raw_dir / raw_name
        if not raw_path.exists():
            for target in targets:
                failed.append((raw_name, target, "raw not found"))
            continue



        for target in targets:
            # Strip leading slash; normalize URL-encoded path segments.
            target_rel = urllib.parse.unquote(target.lstrip("/"))
            target_path = Path(target_rel)
            target_path.parent.mkdir(parents=True, exist_ok=True)

            try:
                with Image.open(raw_path) as im:
                    if im.mode in ("CMYK", "P"):
                        im = im.convert("RGB")
                    if im.mode == "RGBA" and target_path.suffix.lower() in (".jpg", ".jpeg"):
                        bg = Image.new("RGB", im.size, "white")
                        bg.paste(im, mask=im.split()[3])
                        im = bg

                    if im.width > MAX_WIDTH:
                        ratio = MAX_WIDTH / im.width
                        new_h = int(im.height * ratio)
                        im = im.resize((MAX_WIDTH, new_h), Image.LANCZOS)

                    if target_path.suffix.lower() in (".jpg", ".jpeg"):
                        im.save(target_path, "JPEG", quality=JPEG_QUALITY, optimize=True)
                    else:
                        im.save(target_path, "PNG", optimize=True)
            except Exception as e:
                failed.append((raw_name, target, str(e)))
                continue

            ok += 1

    print(f"{slug}: applied {ok} mappings")
    if failed:
        print(f"  failed ({len(failed)}):")
        for raw, target, err in failed:
            print(f"    {raw} -> {target}: {err}")
    if data.get("unmatched_expected"):
        print(f"  unmatched expected ({len(data['unmatched_expected'])}):")
        for p in data["unmatched_expected"]:
            print(f"    {p}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit("usage: apply_image_mapping.py <slug>")
    for slug in sys.argv[1:]:
        apply(slug)
