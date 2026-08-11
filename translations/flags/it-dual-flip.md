# IT — dual-flip: EN↔NL meaning discrepancies

Format: `- [file] EN says X / NL says Y — blocked|proceeded-with-Z`

Raised by Task 7-it (dual-flip: index, installation, controls, osd).
Phrasing-only differences are deliberately **not** listed here.

## Spec-table field: colour accuracy vs colour coverage

- [it/manuals/dual-flip/index.mdx, §Specifiche tecniche] EN says `Color Accuracy | 100% sRGB` / NL says `Kleurdekking | 100% sRGB` (= colour *coverage* / gamut) — proceeded-with-`Precisione cromatica`
  (Glossary §5.4 locks `Color Accuracy → Precisione cromatica` and `Color Gamut → Gamma cromatica` as two distinct targets, so the EN/NL split cannot be collapsed silently. EN is the structural template and the glossary term is locked, hence no block. **Client note:** the value `100% sRGB` is a gamut-coverage figure, so the NL field name is arguably the technically correct one and the EN field name the defect. If the client confirms, the EN page should change to `Color Gamut` and the IT page follows in one edit to `Gamma cromatica`. Same field appears across the other product index pages — worth normalising corpus-wide, not per product.)

## Non-flags — checked and dismissed (recorded for the reviewer)

- [osd.mdx, §3 Impostazioni colore] NL translates the OSD **preset values** (`Warm, Koel, Gebruiker, Standaard`); EN keeps `Warm, Cool, User, Standard`. Glossary §7.2 lists these as on-device strings that stay English → IT keeps the EN forms. NL-side deviation from the DNT policy, not an EN↔NL meaning difference.
- [osd.mdx, §1 Retroilluminazione, `DCR`] NL translates the device tokens (`Kies AAN of UIT`); `ON/OFF` is a `dnt.json` token → IT keeps `scegli ON o OFF`. Same class as above.
- [osd.mdx, §2] EN heading `2. Image` / NL `2. Beeldinstellingen` (= Image settings). Glossary §9.6 locks `2. Image → 2. Immagine` and `2. Image Modes → 2. Modalità immagine` separately; EN followed. Heading-scope drift, not meaning.
- [osd.mdx, §5 Ripristino, `HDR`] EN `if the connected device supports it` / NL `als het apparaat compatibel is` — same condition, phrasing only.
- [osd.mdx, `ASPECT`] EN `Switch the aspect ratio between 4:3 and WIDE` / NL `Pas de beeldverhouding aan naar 4:3 of WIDE` — both describe a two-value toggle. Phrasing only.
- [osd.mdx, all `<img alt>`] NL keeps the English OSD chapter word in alt text (`OSD-menu Backlight`); IT translates it (`Menu OSD Retroilluminazione`) per glossary ruling R1 / §11.1.1, which makes `Backlight → Retroilluminazione` binding "in every position" and explicitly de-lists it from `dnt.json`. Deliberate IT/NL divergence, not an EN↔NL conflict.
- [index.mdx, §Contenuto della confezione] EN `1x / 2x` and installation's `2× / 1×` quantity prefixes are dropped per glossary §4.1 and §9.5 (`2x USB-A and 2x HDMI → 2 USB-A e 2 HDMI`). This removes the `×` (U+00D7) from `it/manuals/dual-flip/installation.mdx` — an intentional character-inventory divergence from EN, not an omission.
- [installation.mdx, `<Note>`] EN lead-in `**Important:**` / NL `**Let op:**` (= Caution). Glossary §5.5 gives distinct targets (`Importante:` / `Attenzione:`); EN followed as template. Callout-register drift, not meaning.
- [index.mdx, table] EN `Backlight | LED` left untranslated on the NL page; IT renders `Retroilluminazione` per §5.4 and R1. Not a meaning difference.
