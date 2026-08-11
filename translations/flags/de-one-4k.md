# DE one-4k flags

Task 7-de, slug `one-4k` (index, installation, controls, osd). Format:
`- [file] EN says X / NL says Y — blocked|proceeded-with-Z`

Raised: 3. Blocked: 0.

- [installation.mdx] EN says `## Getting Started` (a 7-bullet lead-in block that exists **only** in one-4k and one-4k-oled) / NL says `## Aansluiten` (= "Connecting", which collides semantically with the `## Aansluitmogelijkheden` heading right below it) — proceeded-with `## Erste Schritte`. Rationale: EN is the structural template and glossary §7.3 locks `Getting Started` → `Erste Schritte`. NL's heading is a paraphrase, not a different meaning; taking it would have produced two near-identical German headings in sequence.

- [index.mdx] EN says "a high-resolution second screen" / NL says "een hoogwaardig tweede scherm" (= *high-quality*, not *high-resolution*) — proceeded-with `einen hochauflösenden zweiten Bildschirm`. Rationale: EN is more specific and factually correct for a 3840 × 2160 panel; the NL wording looks like a softening, not a corrected fact.

- [index.mdx] NL is internally inconsistent on the inch decimal in this product: frontmatter `One 4K 15.6\"` and the `<Note>`/`Produktnaam` cells keep the period `15.6"`, while the `Schermgrootte` row switches to `15,6 inch` — the same defect class glossary §4.1 already documents for `nl/manuals/panorama/index.mdx` — proceeded-with the comma in **all four** positions (`15,6\"` in frontmatter, `15,6"` in the Note, the Produktname row and the Bildschirmgröße row), and with `"` rather than `Zoll` per §4. Not a meaning conflict; logged so the client is not surprised that DE and NL differ here on purpose.

## Notes (not flags)

- The MDX comment at `osd.mdx:27` (`{/* The PDF only documents controls … */}`) is not user-visible. NL translates it, but glossary §7.7's rationale ("not user-visible — leave in English") is applied corpus-wide: **kept byte-identical to the EN source**, matching the de/one-4k-oled slug, which keeps its two `{/* TODO … */}` comments in English. Its em dash is EN-source text, not German body copy, so §3.6 does not apply to it.
- `100 % sRGB`, `3840 × 2160` and `15,6"` diverge from the EN/NL source formatting by design (glossary §4, DIN 5008 unit spacing) — per glossary §11 this is **not** an nl↔de parity defect.
