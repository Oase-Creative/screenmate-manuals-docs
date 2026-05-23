"""
Scan MDX files per product and emit a manifest of image paths the MDX expects.

Usage:
    python scripts/build_image_manifest.py <slug>     # one product
    python scripts/build_image_manifest.py            # all products

Output: sources/<slug>/expected-images.json

Each entry: {
    "path": "/images/.../some-image.png",   # what the MDX references
    "alt": "...",                            # alt text if found
    "ref_files": ["manuals/en/<slug>/index.mdx", ...],
}
"""

import json
import re
import sys
import urllib.parse
from pathlib import Path

SLUGS = [
    "onecable", "lite", "lite-144hz", "dual-flip", "flip-14",
    "flip-15-6", "expand-14", "expand-15-6", "infinity", "infinity-lite",
]

# <img src="/images/..."> with optional alt
IMG_TAG_RE = re.compile(
    r'<img\s+[^>]*src="(/images/[^"]+)"[^>]*?(?:alt="([^"]*)")?[^>]*/?>',
    re.IGNORECASE,
)
# Also Markdown ![alt](/images/...)
MD_IMG_RE = re.compile(r'!\[([^\]]*)\]\((/images/[^)]+)\)')


def scan_product(slug: str) -> dict:
    entries: dict[str, dict] = {}

    for lang in ("en", "nl"):
        mdx_dir = Path("manuals") / lang / slug
        if not mdx_dir.exists():
            continue
        for mdx in sorted(mdx_dir.glob("*.mdx")):
            text = mdx.read_text(encoding="utf-8")
            rel_mdx = str(mdx).replace("\\", "/")

            for m in IMG_TAG_RE.finditer(text):
                raw_path = urllib.parse.unquote(m.group(1))
                alt = m.group(2) or ""
                entry = entries.setdefault(raw_path, {"path": raw_path, "alt": alt, "ref_files": []})
                if alt and not entry["alt"]:
                    entry["alt"] = alt
                if rel_mdx not in entry["ref_files"]:
                    entry["ref_files"].append(rel_mdx)

            for m in MD_IMG_RE.finditer(text):
                alt = m.group(1)
                raw_path = urllib.parse.unquote(m.group(2))
                entry = entries.setdefault(raw_path, {"path": raw_path, "alt": alt, "ref_files": []})
                if alt and not entry["alt"]:
                    entry["alt"] = alt
                if rel_mdx not in entry["ref_files"]:
                    entry["ref_files"].append(rel_mdx)

    # Only keep images that belong to THIS product's image folder.
    folder_hint = f"Screenmate - "  # all our product image folders start this way
    out_list = [
        e for e in entries.values()
        if folder_hint in e["path"]
    ]
    out_list.sort(key=lambda e: e["path"])
    return {"slug": slug, "count": len(out_list), "expected": out_list}


def main():
    # OneCable has curated images; skip by default to avoid overwriting them via
    # the apply step. Pass `onecable` explicitly to include.
    DEFAULT_SKIP = {"onecable"}
    targets = sys.argv[1:] or [s for s in SLUGS if s not in DEFAULT_SKIP]
    for slug in targets:
        manifest = scan_product(slug)
        out_path = Path("sources") / slug / "expected-images.json"
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(json.dumps(manifest, indent=2, ensure_ascii=False), encoding="utf-8")
        print(f"{slug}: {manifest['count']} expected images -> {out_path}")


if __name__ == "__main__":
    main()
