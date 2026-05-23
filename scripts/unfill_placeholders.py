"""
Reverse the fallback image fill — delete just the files that were jammed in
as placeholder duplicates of composite raws.

Reads each product's image-mapping.json -> unmatched_expected paths and
deletes those files. Leaves the real per-component PDF extractions intact.
"""

import json
import sys
import urllib.parse
from pathlib import Path

SLUGS = ["dual-flip", "flip-14", "flip-15-6", "expand-14", "expand-15-6", "infinity"]


def normalize(entry) -> str | None:
    if isinstance(entry, str):
        return entry
    if isinstance(entry, dict):
        return entry.get("path")
    return None


def unfill(slug: str) -> None:
    mp = Path("sources") / slug / "image-mapping.json"
    if not mp.exists():
        return
    data = json.loads(mp.read_text(encoding="utf-8"))
    paths = [normalize(e) for e in data.get("unmatched_expected", [])]
    paths = [p for p in paths if p]

    deleted = 0
    for p in paths:
        cleaned = p.replace('"', "")
        rel = urllib.parse.unquote(cleaned.lstrip("/"))
        fp = Path(rel)
        if fp.exists():
            fp.unlink()
            deleted += 1
    print(f"{slug}: deleted {deleted}")


if __name__ == "__main__":
    for slug in sys.argv[1:] or SLUGS:
        unfill(slug)
    # Also the lone cable-types.png I manually placed for expand-14
    extra = Path("images/Screenmate - Expand 14 - Handleiding images/cable-types.png")
    if extra.exists():
        extra.unlink()
        print("deleted expand-14 cable-types.png (manual placeholder)")
