# DE One 4K OLED flags

Task 7-de / slug `one-4k-oled`. Pages: index, installation, controls, osd (safety.mdx owned by Task 6).
Format: `- [file] EN says X / NL says Y — blocked|proceeded-with-Z`

Raised: 5. Blocked: 0.

## EN ↔ NL divergences

- [installation.mdx] EN says `## Getting Started` / NL says `## Aansluiten` (= "Connecting") — proceeded-with `## Erste Schritte`. Rationale: EN is the structural template and glossary §7.3 locks `Getting Started` → `Erste Schritte`. NL renamed the section after its content rather than translating the heading; German keeps the EN heading. Note this is the first corpus use of `Erste Schritte` — only `one-4k` and `one-4k-oled` carry a `## Getting Started`, so the two slugs must agree.

- [installation.mdx] EN says `**Important:**` / NL says `**Let op:**` (= "Note:") — proceeded-with `**Wichtig:**`. Rationale: glossary §10.1 keeps `Important:` → `Wichtig:` distinct from `Note:` → `Hinweis:`; §10.5 counts `Important:` as its own lead-in. Same call as the `lite` slug — NL collapses the two lead-ins, German keeps them apart.

- [controls.mdx, osd.mdx] EN says `{/* TODO: confirm with Louie — … */}` in English / NL says the same comment with its body translated into Dutch (`gebruik van USB-A-poort …`, `volledige OSD-menustructuur …`) — proceeded-with the **EN comment verbatim** in both files. Rationale: these are internal notes addressed to the client, not user-visible copy. Glossary §7.7 rules the analogous `{/* … */}` template block in `manuals-index.mdx` stays English ("Not user-visible — leave the whole comment block in English"). Translating a question addressed to Louie into German would also make the two open items harder to reconcile across the three new languages. Non-blocking; if the client would rather have every comment localised, this is a one-line revert per file.

- [installation.mdx] EN says "To connect **the Screenmate** to an HDMI device …" / NL says "Om **de draagbare monitor** aan te sluiten …" (= "the portable monitor") — proceeded-with `Um **den Screenmate** an ein HDMI-Gerät anzuschließen …`. Rationale: EN is the template, and the four sibling installation pages that share this paragraph (lite, lite-144hz, one-4k, one-4k-oled) already read `den Screenmate` in the shipped DE `lite` page. NL's generic noun is an isolated per-file drift.

- [index.mdx] EN says `| **Screen Size** | 15.6" |` / NL says `| **Schermgrootte** | 15,6 inch |` — the unit spelled out — proceeded-with `| **Bildschirmgröße** | 15,6" |`. Rationale: glossary §4 locks inches as comma + inch mark and says explicitly "do **not** expand to `Zoll`". Markdown table cell, so the literal `"` is correct here (§4.1); the frontmatter `description` on the same page keeps the EN `\"` escape.

## Locked figures verified on this slug

- **Contrast ratio `100.000:1`** (§4 thousands rule, 5+ digits; §11 decision log). Applied in **both** places it occurs: the `## Was ist der Screenmate One 4K OLED?` prose sentence and the `**Kontrastverhältnis**` spec row. EN writes `100,000:1`, NL writes `100.000:1` — they agree in value, and German takes the NL separator by rule, not by inheritance.
- **DIN 5008 unit spacing** applied against NL's closed forms: `100 % sRGB` (EN/NL `100% sRGB`). Not an nl↔de parity defect — §11 rules this a deliberate divergence. Angle `178°` keeps no space in all three.
- **Four-digit figures keep no separator:** `3840 × 2160`. Only the contrast figure crosses five digits.

## Coordinator ruling R9 — alt text (applied)

R9: image `alt` text translates FULLY into German. All **7** alts on this slug (1 index, 5 installation, 1 controls; osd has no images) are fully German. No OSD menu name appears in any alt on this slug, so the failure mode R9 targets did not arise. Non-German tokens remaining are DNT only: `Screenmate`, `One 4K OLED`, `USB-C`, `USB-A`, `HDMI` (§7.7).

## Coordinator ruling R8 — descriptive control names (applied)

- `### Indicator Light` → `### Statusanzeige` (§7.4), not a transliteration of NL `Indicatielampje`.
- `### Menu Button (Power / OSD)` → `### Menütaste (Power / OSD)` (§7.4): the descriptive word translates, the on-device literal `Power` and the acronym `OSD` do not. Same split in `osd.mdx`, where NL's `aan/uit-knop` becomes `Power-Taste` per §1.1 ("device is labelled 'Power'").
- `### 3.5mm Headphone Jack` → `### 3,5-mm-Klinkenanschluss` (§7.4 + §3.2 Durchkopplung). NL's `3,5 mm koptelefoonaansluiting` keeps the standalone spaced unit; German couples it inside the compound.
- `### + and − Buttons` → `### Tasten + und −`, run-ins `**Taste +:**` / `**Taste −:**` (§10.5). The `−` is U+2212 throughout, carried over from the EN source (§3.6).
