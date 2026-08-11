# DE infinity-lite flags

Task 7-de / slug `infinity-lite`. Pages in scope: `index.mdx`, `installation.mdx`,
`controls.mdx` (`safety.mdx` and `display-settings.mdx` belong to Task 6).
Format: `- [file] EN says X / NL says Y — blocked|proceeded-with-Z`

Raised: 4. Blocked: 0.

## EN ↔ NL differences

- [infinity-lite/controls.mdx] EN says `### Left "Min" Button` / `### Right "Plus" Button` (the button, named) / NL says `### Naar links schakelen – "Min"` / `### Naar rechts schakelen – "Plus"` (the gesture, named) — proceeded-with the locked glossary §7.4 renderings `### Linke Taste „Min“` and `### Rechte Taste „Plus“`, i.e. the EN structure. NL renames the heading after the gesture in the body line below it; that is a wording choice, not a meaning conflict. The body lines keep the gesture: `Nach links drücken – …` / `Nach rechts drücken – …`, which also matches the §10.5 lock `**Nach links drücken („Min“):**` used on the sibling `infinity/controls.mdx`.

- [infinity-lite/controls.mdx] EN says `### LED Indicator` (glossary §7.4 → `LED-Anzeige`) / NL says `### LED-Indicator` — proceeded-with `### LED-Anzeige` per the locked glossary. Cosmetic only.

- [infinity-lite/controls.mdx] EN says `Toggle left – adjusts the backlight (brightness)` and `Toggle right – adjusts the volume` — one verb ("adjusts") for both / DE uses two verbs: `stellt die Hintergrundbeleuchtung (Helligkeit) ein` (the verbatim §6.1 lock for this exact sentence) and `passt die Lautstärke an` (§10.4 assigns `anpassen` to raising/lowering brightness and volume). Not an EN↔NL conflict; logged so a reviewer does not "harmonise" the two verbs and break one of the two locks.

- [infinity-lite/index.mdx vs installation.mdx] EN is internally inconsistent about screen count: `index.mdx` says "giving you **one** extra portable display", `installation.mdx` says "safely deploy **both** extension screens". NL mirrors the same split ("een extra beeldscherm" / "beide uitbreidingsschermen"), so EN and NL agree — proceeded-with a faithful mirror in DE (`einen zusätzlichen tragbaren Bildschirm` / `beide Erweiterungsbildschirme`). **Client decision needed:** the Infinity Lite is a single-panel product; "both extension screens" is likely inherited from the Infinity booklet and should probably be corrected upstream in EN + NL first.

## Cross-product contradiction (upstream, mirrored not fixed)

- [infinity-lite/controls.mdx vs infinity/controls.mdx] The two products give **opposite** directions for the same control: `infinity-lite` says left "Min" = backlight/brightness, right "Plus" = volume; `infinity` says `**Press right ("Plus"):** increase the backlight (brightness)` and `**Press left ("Min"):** decrease the volume`. Within `infinity-lite`, EN and NL agree with each other, so the German page translates its own source faithfully and does **not** import the Infinity direction. Per the task brief this upstream contradiction is mirrored, not fixed. (Note also that Infinity's own EN pairs "increase" with brightness but "decrease" with volume — a second oddity in that file, out of scope here.)

## "Flipped" / "Mirrored" — out of scope for this task, recorded for Task 6

- `en/manuals/infinity-lite/display-settings.mdx` uses **`Flipped`** (line 18, Windows tab) and **`Mirrored`** (line 54, macOS-side block) for the same orientation setting; NL renders both as `'Gespiegeld'`. Both occurrences live in `display-settings.mdx`, which Task 6 owns — no occurrence of either word exists in `index.mdx`, `installation.mdx` or `controls.mdx`, so nothing was rendered here. Glossary §9 maps **both** EN spellings to the single German target `Querformat (gedreht)` (German Windows has no standalone "Gedreht" entry, and `Gespiegelt` is the Dutch solution with no German counterpart). Task 6 should use `Querformat (gedreht)` in both places.

## Formatting divergences applied per glossary (not defects, logged so a reviewer does not "fix" them)

- Resolution spaced in DE — `1920 × 1080` — where EN and NL both write `1920×1080` (§4). Matches the sibling DE `lite` and `flip` pages.
- DIN 5008 unit spacing: `120 % sRGB` (EN/NL `120% sRGB`), `5 V`, `20 V`, `±2 V` (EN/NL `5V`, `20V`, `±2V`) — §4 and §11, explicitly *not* an nl↔de parity defect.
- `5V/2A power adapter` → `5-V/2-A-Netzteil` (§3.2 number+unit inside a compound).
- `3.5 mm Headphone Jack` → `3,5-mm-Klinkenanschluss` (§3.2 + §7.4); `USB-C (for HDMI > USB-C)` → `USB-C (für HDMI-auf-USB-C)`, arrow dropped per the locked cable chain (§3.3, §7.4).
- The three package-contents cables take the locked chain form (§3.3), preserving direction: `USB-A-auf-USB-C-Kabel`, `USB-C-auf-USB-C-Kabel`, `HDMI-auf-USB-C-Kabel`. NL's looser `HDMI naar USB-C-kabel` (spaced) is not copied.
- `One USB-A or USB-C to USB-C cable` → `Ein USB-A- oder USB-C-auf-USB-C-Kabel`, using the suspended hyphen (§3.5) over the chain rule (§3.3) rather than spelling both chains out in full.
- Inch mark: `15,6"` appears only in markdown contexts here (prose + spec-table cell), so the literal `"` is correct; this product has no `<Tab title=…>` and no inch mark in frontmatter (§4.1).
- German typographic quotes `„…“` in `Linke Taste „Min“` / `Rechte Taste „Plus“` (§3.6), where EN uses `"…"` and NL uses ASCII `'…'`.
