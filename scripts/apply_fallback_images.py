"""
Fill image gaps by copying composite raws into multiple expected slots.

When the PDF has one composite (e.g. package-contents showing all cables together)
but the MDX expects per-component renders, the mapping agents leave those slots
unmatched. This script fills them with the composite as a placeholder until
proper assets land from the agency.

Usage:
    python scripts/apply_fallback_images.py            # all products
    python scripts/apply_fallback_images.py expand-15-6

For each unmatched_expected path, copy the configured fallback raw image
(resized) into the target path. Same image will appear N times in the MDX —
acceptable placeholder until real assets arrive.
"""

import json
import sys
import urllib.parse
from pathlib import Path

from PIL import Image

MAX_WIDTH = 1400

# Per-product hint: which raw image to use as the fallback for each
# unmatched semantic bucket. Buckets are matched by substring against the
# missing target path.
FALLBACKS: dict[str, list[tuple[str, str]]] = {
    "dual-flip": [
        # buckets ordered most specific first
        ("install-steps",     "page-09-img-01.png"),
        ("storage-steps",     "page-10-img-01.png"),
        ("port-icons",        "page-07-img-01.png"),
        ("protective-case",   "page-06-img-01.png"),
        ("cable-",            "page-06-img-01.png"),
    ],
    "flip-14": [
        ("icon-",             "page-07-img-01.png"),
        ("port-",             "page-07-img-01.png"),
        ("cable-",            "page-06-img-01.png"),
    ],
    "flip-15-6": [
        ("icon-",             "page-07-img-01.png"),
        ("port-",             "page-07-img-01.png"),
        ("cable-",            "page-06-img-01.png"),
    ],
    "expand-14": [
        ("cable-types",       "page-06-img-01.png"),
        ("cable-",            "page-06-img-01.png"),
        ("port-icons",        "page-07-img-01.png"),
    ],
    "expand-15-6": [
        # package-contents components: 6 items x 2 modes = 12 slots, all the composite
        ("Day Mode",          "page-06-img-01.png"),
        ("Night Mode",        "page-06-img-01.png"),
        ("port-icons",        "page-07-img-01.png"),
        ("cable-",            "page-06-img-01.png"),
    ],
    "infinity": [
        ("port-hdmi",         "page-07-img-01.png"),
        ("port-usb-",         "page-07-img-01.png"),
        ("port-",             "page-07-img-01.png"),
    ],
}


def normalize_unmatched(entry) -> str | None:
    if isinstance(entry, str):
        return entry
    if isinstance(entry, dict):
        return entry.get("path")
    return None


def pick_fallback(slug: str, target_path: str) -> str | None:
    rules = FALLBACKS.get(slug, [])
    for substr, raw in rules:
        if substr in target_path:
            return raw
    return None


def fill(slug: str) -> None:
    mapping_path = Path("sources") / slug / "image-mapping.json"
    if not mapping_path.exists():
        print(f"{slug}: no mapping file, skipping")
        return

    data = json.loads(mapping_path.read_text(encoding="utf-8"))
    unmatched = [normalize_unmatched(e) for e in data.get("unmatched_expected", [])]
    unmatched = [u for u in unmatched if u]

    if not unmatched:
        print(f"{slug}: nothing to fill")
        return

    raw_dir = Path("sources") / slug / "raw"
    filled = 0
    unfilled = []

    for target in unmatched:
        raw_name = pick_fallback(slug, target)
        if raw_name is None:
            unfilled.append((target, "no fallback rule"))
            continue

        raw_path = raw_dir / raw_name
        if not raw_path.exists():
            unfilled.append((target, f"raw missing: {raw_name}"))
            continue

        # Strip filesystem-illegal chars (Windows can't have " in dir names).
        target_clean = target.replace('"', "")
        target_rel = urllib.parse.unquote(target_clean.lstrip("/"))
        target_p = Path(target_rel)
        target_p.parent.mkdir(parents=True, exist_ok=True)

        try:
            with Image.open(raw_path) as im:
                if im.mode in ("CMYK", "P"):
                    im = im.convert("RGB")
                if im.width > MAX_WIDTH:
                    ratio = MAX_WIDTH / im.width
                    im = im.resize((MAX_WIDTH, int(im.height * ratio)), Image.LANCZOS)
                im.save(target_p, "PNG", optimize=True)
            filled += 1
        except Exception as e:
            unfilled.append((target, str(e)))

    print(f"{slug}: filled {filled} of {len(unmatched)} gaps")
    for target, reason in unfilled:
        print(f"  unfilled: {target} ({reason})")


if __name__ == "__main__":
    targets = sys.argv[1:] or list(FALLBACKS.keys())
    for slug in targets:
        fill(slug)
