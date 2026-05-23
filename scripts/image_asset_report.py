"""
Generate a designer-facing inventory of every image asset the manuals need.

For each product, list every image path the MDX references and mark its status:
  [scraped]  — we have a placeholder pulled from the PDF; replace if a higher-
                fidelity asset exists.
  [missing]  — no placeholder on disk; the MDX renders a broken image.
  [curated]  — OneCable assets pre-existed; no action needed unless replacing.

Output: tasks/image-assets-needed.md
"""

import json
import urllib.parse
from pathlib import Path

SLUGS = [
    "onecable", "lite", "lite-144hz", "dual-flip", "flip-14",
    "flip-15-6", "expand-14", "expand-15-6", "infinity", "infinity-lite",
]


def status_for(slug: str, fs_path: Path) -> str:
    if not fs_path.exists():
        return "missing"
    if slug == "onecable":
        return "curated"
    return "scraped"


def short_ref(refs: list[str]) -> str:
    # show just the basename of referencing MDX files, deduped & sorted
    bases = sorted({Path(r).stem for r in refs})
    return ", ".join(bases)


def build():
    lines = [
        "# Screenmate manuals — image asset inventory",
        "",
        "Every image referenced by the Mintlify MDX files, per product.",
        "",
        "**Status legend**",
        "- `[curated]` — OneCable asset already in place (pre-existing). Replace only if a newer/better version exists.",
        "- `[scraped]` — placeholder extracted from the PDF booklet. Functional but typically lower fidelity than the designer's original. Replace if possible.",
        "- `[missing]` — no image on disk; the MDX shows a broken-image icon. **These are the ones we most need from you.**",
        "",
        "Paths shown are relative to the docs site root (`/images/...`). Drop replacement files at the same paths and the docs will pick them up automatically.",
        "",
    ]

    grand = {"curated": 0, "scraped": 0, "missing": 0}

    for slug in SLUGS:
        manifest_path = Path("sources") / slug / "expected-images.json"
        if not manifest_path.exists():
            continue
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        entries = manifest["expected"]

        counts = {"curated": 0, "scraped": 0, "missing": 0}
        rows = []
        for e in entries:
            url_path = e["path"]
            fs_rel = urllib.parse.unquote(url_path.replace('"', "").lstrip("/"))
            status = status_for(slug, Path(fs_rel))
            counts[status] += 1
            grand[status] += 1
            rows.append((status, url_path, e.get("alt", ""), e.get("ref_files", [])))

        # Sort so missing surfaces first, then scraped, then curated
        order = {"missing": 0, "scraped": 1, "curated": 2}
        rows.sort(key=lambda r: (order[r[0]], r[1]))

        lines.append(f"## {slug}")
        lines.append("")
        summary_parts = []
        if counts["missing"]:
            summary_parts.append(f"**{counts['missing']} missing**")
        if counts["scraped"]:
            summary_parts.append(f"{counts['scraped']} scraped")
        if counts["curated"]:
            summary_parts.append(f"{counts['curated']} curated")
        lines.append(" · ".join(summary_parts) + f" · {len(entries)} total")
        lines.append("")

        for status, url_path, alt, refs in rows:
            tag = f"`[{status}]`"
            alt_part = f" — *{alt}*" if alt else ""
            ref_part = f"  \n  Used in: {short_ref(refs)}" if refs else ""
            lines.append(f"- {tag} `{url_path}`{alt_part}{ref_part}")
        lines.append("")

    lines.append("---")
    lines.append("")
    lines.append("## Totals")
    lines.append("")
    lines.append(f"- **missing**: {grand['missing']}")
    lines.append(f"- scraped (PDF placeholder, replace if possible): {grand['scraped']}")
    lines.append(f"- curated (OneCable pre-existing): {grand['curated']}")

    out = Path("tasks") / "image-assets-needed.md"
    out.parent.mkdir(exist_ok=True)
    out.write_text("\n".join(lines), encoding="utf-8")
    print(f"wrote {out}")
    print(f"missing: {grand['missing']}, scraped: {grand['scraped']}, curated: {grand['curated']}")


if __name__ == "__main__":
    build()
