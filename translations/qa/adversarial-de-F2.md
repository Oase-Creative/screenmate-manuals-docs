# Adversarial DE review — family F2 (Lite / Lite 144 Hz / Panorama)

**Branch:** `lang-expansion-de-fr-it`
**Scope:** `de/manuals/lite/` (5), `de/manuals/lite-144hz/` (5), `de/manuals/panorama/` (5), `de/manuals-index.mdx` — 16 files, each read against EN + NL.
**Authority:** `translations/glossary-de.md` (all 12 sections + decision log).
**Date:** 2026-08-11

**Verdict:** no meaning-drift, register or safety defects. The dominant defect class is
**cross-product string drift between `lite` and `lite-144hz`** — 15 places where the EN and
NL sources are byte-identical but the German renders differently. Four further items are
genuine German errors (one comma, one modality shift, one weakened requirement, one
glossary-locked unit form).

**Counts:** 1 critical · 7 moderate · 5 cosmetic.

---

## Key structural evidence

EN `lite` vs `lite-144hz`, product tokens normalised, CRLF stripped:

| Chapter | EN diff | NL diff | DE diff |
|---|---|---|---|
| `installation.mdx` | **identical** | **identical** | **8 lines** |
| `osd.mdx` | **identical** | **identical** | **4 lines** |
| `safety.mdx` | **identical** | **identical** | identical ✓ |
| `controls.mdx` | 2 lines (`OSD mode` / `OSD menu mode`) | 2 lines (same) | **5 lines** (2 legitimate + 3 drift) |

Every DE-only difference below is therefore translation-side, not source-side.

---

## Findings

| # | File | Line / quote | Problem | Severity | Proposed fix |
|---|---|---|---|---|---|
| F1 | all 16 F2 files | frontmatter ends `icon: "…"` then `---` — no `en_link` | No F2 page carries an `en_link`. EN pages point in (`nl_link: "/nl/manuals/lite/index"`), and every NL page carries `en_link`, so the language switcher and the QR redirect path have no DE return edge. **Branch-wide, not F2-specific: 0 of 62 `de/**/*.mdx` files have it** — reported here because it ships broken from these files. | **critical** | Add `en_link: "/en/manuals/<slug>/<page>"` to all 16 (and the other 46 DE pages) mirroring the NL convention. |
| F2 | `de/manuals/lite-144hz/installation.mdx` vs `de/manuals/lite/installation.mdx` | L9 `unterstützt fünf Anschlussszenarien` / `lässt sich auf fünf Arten anschließen`; L9 `vorhandenen` / `verfügbaren Kabeln`; L13 `Verbinde den Screenmate über das …-Kabel mit deinem Laptop` / `Schließe den Screenmate mit dem …-Kabel an deinen Laptop an`; L21 `Dann verwende` / `Verwende dann`; L27 `und ein USB-C-auf-USB-A-Kabel` / `und zusätzlich über ein USB-C-auf-USB-A-Kabel`; L35 `für Video und Strom zugleich` / `für Videosignal und Stromversorgung zugleich`; L57 `zum Beispiel an einen PC` / `wie zum Beispiel einen PC`; L57 `(nicht die Konsole Nintendo Switch selbst)` / `(nicht die Nintendo Switch selbst)` | 8 gratuitous renderings of strings that are **byte-identical in both EN and NL**. Two translators' voices in one product family; a reader comparing the two manuals sees unexplained wording changes. | moderate | Pick one rendering per string and apply to both files. Recommend the `lite` form for L13/L21/L27 and the `lite-144hz` form for L57 (`Konsole Nintendo Switch` matches EN "the Nintendo Switch console itself"). |
| F3 | `de/manuals/lite-144hz/installation.mdx` | L16 `**Wichtig:** … musst du den Monitor separat über eine zusätzliche Stromquelle mit Strom versorgen.` | Modality shift + tautology. EN/NL state a device condition ("the monitor needs to be powered separately"); DE converts it into a direct obligation on the reader (`musst du`). `über eine … Stromquelle mit Strom versorgen` also repeats *Strom* twice in six words. Sibling `lite` L16 renders it correctly. | moderate | Adopt the `lite` wording verbatim: `… muss der Monitor separat über eine zusätzliche Stromquelle versorgt werden.` |
| F4 | `de/manuals/lite-144hz/installation.mdx` | L35 `Dein Smartphone oder Tablet braucht einen USB-C-Anschluss mit Videounterstützung` | Weakens a hard prerequisite. EN: "must have a USB-C port with video support". `braucht` reads as a recommendation; the sentence gates whether the product works at all. Sibling `lite` L35 has the correct modal `muss … haben`. | moderate | `Dein Smartphone oder Tablet muss einen USB-C-Anschluss mit Videounterstützung haben` (= the `lite` form). |
| F5 | `de/manuals/lite-144hz/osd.mdx` | L24 `**ECO-Modus:** Wähle einen Bildmodus, je nachdem wie du den Monitor verwendest:` | **Orthography error.** `je nachdem` introducing a subordinate clause requires a comma before the interrogative: `je nachdem, wie`. Glossary §10.3 makes the subordinate-clause comma mandatory, not stylistic. | moderate | `… einen Bildmodus, je nachdem**,** wie du den Monitor verwendest:` — and apply the same corrected string to `lite/osd.mdx` L24, whose `Wähle einen Bildmodus danach aus, wie du den Monitor verwendest` is awkward. |
| F6 | `de/manuals/panorama/index.mdx` | L23 `- **65-Watt-USB-C-Netzteil**` | Violates the §3.2 lock `65 W` → **`65-W-Netzteil`**, which the product's own sibling pages honour three times (`controls.mdx` L19, `installation.mdx` L50, L58, L71 all use `65-W-Netzteil`). EN is internally inconsistent here ("65 Watt" in the package list, "65 W" everywhere else); §11 precedent is that EN-source inconsistencies are **normalised** in German. | moderate | `- **65-W-USB-C-Netzteil**` |
| F7 | `de/manuals/lite-144hz/osd.mdx` vs `de/manuals/lite/osd.mdx` | L17 `Lege den Schwarzwert für tiefere Schwarztöne … fest.` / `Lege den Schwarzwert fest, um … zu erhalten.`; L18 `um die Bildklarheit und die Details zu verbessern` / `um das Bild klarer und detailreicher darzustellen`; L25 `**Standard:** Standard-Bildmodus.` / `Standardmäßiger Bildmodus.`; L31 `Passt … automatisch für eine bessere Bildqualität an.` / `Passt … automatisch an, um die Bildqualität zu verbessern.` | 4 more sibling divergences on identical EN/NL source, inside the OSD chapter where users cross-reference between the two models most often. | moderate | Normalise to one rendering each. The `lite-144hz` L17 form tracks EN's "for deeper blacks" adjunct most closely; `Standard-Bildmodus` (L25) is the tighter of the two. |
| F8 | `de/manuals/lite-144hz/index.mdx` vs `de/manuals/lite/index.mdx` | L8 `Verwende das Navigationsmenü links, um zu den einzelnen Abschnitten zu springen.` / L8 `Über das Navigationsmenü links springst du direkt zu jedem Abschnitt.`; L15 `Der Anschluss erfolgt über USB-C oder HDMI` / `Er wird über USB-C oder HDMI angeschlossen` | The Welcome note is one string in EN and **11/11 identical in NL**; DE has three variants across the corpus, and `lite-144hz` L8 is a **singleton** — the only file of 11 using it. L15 additionally nominalises (`Der Anschluss erfolgt`) against §10.3 "do not nominalise". | moderate | Set `lite-144hz` L8 to the 7/11 majority form `Über das Navigationsmenü links springst du direkt zu jedem Abschnitt.`; set L15 to the `lite` form `Er wird über USB-C oder HDMI angeschlossen`. (Corpus-wide: 7× `Über das Navigationsmenü…`, 3× `Nutze das Navigationsmenü…`, 1× this singleton — worth one normalising pass beyond F2.) |
| F9 | `de/manuals/lite/controls.mdx` vs `de/manuals/lite-144hz/controls.mdx` | L11 `alt="Übersicht der Anschlüsse und Tasten…"` / `alt="Übersicht über die Anschlüsse und Tasten…"`; L23 `Schließe ein externes Gerät einfach über ein Mini-HDMI-auf-HDMI-Kabel an.` / `Schließe über ein Mini-HDMI-auf-HDMI-Kabel ganz einfach ein externes Gerät an.`; L28–29 `Gerät einschalten` / `das Gerät einschalten` | 3 further sibling divergences. The alt-text one also fights the file's own frontmatter, which locks `Übersicht über die Anschlüsse und Bedientasten` (§7.2) — `Übersicht der` is the odd form. (`OSD-Modus` / `OSD-Menü-Modus` on L31/L40 are **correct** and must stay different — §10.5.) | cosmetic | Normalise all three to the `lite-144hz` form, which matches the locked `Übersicht über die …` frontmatter. |
| F10 | `de/manuals/lite-144hz/index.mdx` | L15 `ein leichter, tragbarer 15,6"-Full-HD-Monitor` | Comma is questionable and inconsistent: `lite` L15 writes `ein leichter tragbarer 15,6"-Full-HD-Monitor` for the same EN. Per Duden no comma is set when the second adjective forms a unit with the noun, and `tragbarer Monitor` is exactly such a locked unit (§1.1 "portable monitor | tragbarer Monitor"). | cosmetic | Drop the comma: `ein leichter tragbarer 15,6"-Full-HD-Monitor`. |
| F11 | `de/manuals/panorama/index.mdx` | L15 `der dir drei Full-HD-Displays mit 15,6" aus einem einzigen Gerät liefert` | §10.4 makes `Bildschirm` the default "for individual screens of a multi-screen product" and restricts `Display` to "where the EN clearly means the panel as a hardware component". These are the product's own three screens. The translator plainly reached for `Displays` to dodge repeating `Bildschirme` after `Monitor mit drei Bildschirmen` earlier in the same sentence — understandable, but it is a glossary divergence. | cosmetic | Recast to avoid both the repetition and the divergence: `Der Screenmate Panorama ist ein tragbarer Monitor, der dir drei Full-HD-Bildschirme mit 15,6" aus einem einzigen Gerät liefert.` |
| F12 | `de/manuals/panorama/osd.mdx` | L37 `Deshalb möchtest du die Anordnung des Desktops in deinem Betriebssystem vielleicht anpassen.` | Awkward modal rendering of EN "so you may want to adjust…". Stranding `vielleicht` at the end of a long object phrase reads as an afterthought, and asserting what the reader *wants* is not idiomatic German instruction register. | cosmetic | `Deshalb kannst du die Anordnung des Desktops in deinem Betriebssystem anpassen.` |
| F13 | `de/manuals/panorama/osd.mdx` | L33 `Stelle die Lautstärke mit den Tasten **+ / −** von 0 bis 100 ein.` (and L21 `Die Helligkeit lässt sich pro Bildschirm einstellen`) | §10.4 assigns `anpassen` to "adjusting a value up or down (**brightness, volume**)" and reserves `einstellen` for "setting up a position or configuration". Both instances here use `einstellen` for the two values the rule names explicitly. Note the section headings above them correctly use `Helligkeit anpassen` / `Lautstärke anpassen`, so the page contradicts itself. | cosmetic | L33 `Passe die Lautstärke mit den Tasten **+ / −** von 0 bis 100 an.`; L21 `Die Helligkeit lässt sich pro Bildschirm von 0 bis 100 anpassen.` |

---

## Scrutiny evidence — checks run that came back clean

These were actively hunted and found correct. Listed so a later reviewer does not re-run them.

### Register (§2) — clean
Case-sensitive grep for `\bSie\b`, `\bIhnen\b`, `\bIhr(e|em|en|er|es)?\b`, `\bIhrigen\b`, `\bBitte\b` across all 16 files: **zero hits**. Grep for capitalised `Du|Dein|Dir|Dich` mid-sentence: **zero hits**. `du`/`dein` are lowercase throughout.
- `Bitte` correctly dropped where EN has it: EN `lite/safety.mdx` L10 "**Please** read the following guidelines carefully" → DE L9 `Lies die folgenden Hinweise sorgfältig durch` (§2.2 edge case, §10.1).
- Imperatives are singular with no pronoun and separable prefixes split correctly: `Schließe … an`, `Klappe … auf`, `Lass … fallen`, `Stecke`, `Lade … herunter`, `Lies` (stem-change, no `-e` — §2.3).

### Compounds / Durchkopplung (§3) — clean
- Grep for acronym + bare space + German noun (`USB C Kabel`, `HDMI Anschluss`, `OSD Menü`, `LED Anzeige`, `PD Ladegerät`, `DC Eingang`…): **zero hits**.
- Cable chain (§3.3): every instance uses the locked `X-auf-Y-Kabel`. Grep for the six rejected variants (`-zu-`, spaced `auf`, arrow forms, `von … auf`): **zero hits**. Verified renderings: `USB-C-auf-USB-C-Kabel`, `USB-C-auf-USB-A-Kabel`, `USB-A-auf-USB-C-Kabel`, `Mini-HDMI-auf-HDMI-Kabel`, `USB-C-auf-USB-C-Ladekabel`.
- **Directionality preserved** (§3.3 explicit warning): `panorama/installation.mdx` L72 `USB-A-auf-USB-C-Kabel` (EN "USB-A to USB-C") vs `lite/installation.mdx` L21 `USB-C-auf-USB-A-Kabel` (EN "USB-C to USB-A"). Not normalised into each other.
- Number+unit compounds (§3.2): `3,5-mm-Klinkenanschluss`, `5-V-Stromquelle`, `65-W-Netzteil` all correct (sole exception = F6).
- Suspended hyphen (§3.5): `Ein- und Ausklappen` (`panorama/safety.mdx` L26), `Bestätigen-/Beenden-Taste`, `Power- und Zurück-Taste`.
- All-German compounds correctly closed, no stray hyphens: `Displaytreiber`, `Bildschirmoberfläche`, `Verriegelungsfüße`, `Schnellzugriffsmenü`, `Helligkeitsmenü`, `Lautstärkeregelung`, `Installationsanleitung`.

### Punctuation & typography (§3.6) — clean
- Em dash `—`: **zero hits** in all 16 files. EN `Option 1 — USB-C` correctly becomes `Option 1 – USB-C` (en dash) in `panorama/installation.mdx` L46/L67.
- German quotes `„…“` used throughout (`„Desktop auf diese Anzeige erweitern“`, `„Querformat (gedreht)“`, `„Displays“`, `„Anordnen“`); grep for ASCII `'…'` around words: **zero hits**.
- Typographic minus U+2212 confirmed byte-level in `−20 °C` (all three `safety.mdx`) and in the `(−)` button glyphs.
- `×` (U+00D7) used for counts, resolutions and dimensions; grep for `2x` / `2 x`: **zero hits**.
- No double spaces after full stops. `ß` used per standard orthography (`Anschluss`, `schließen`, `Füße`, `weißen`, `Größe`); no umlaut transliteration.

### Numbers & units (§4) — clean
- Decimal comma applied everywhere; grep for a period between digits: **zero hits**.
- 4-digit thousands unseparated: `1920 × 1080`, `3000 Gramm` ✓.
- Weights spelled out as `Gramm` (`609 Gramm`, `3000 Gramm`) matching EN "grams" ✓.
- Angles keep no space (`172°`, `360°`); temperature takes one (`−20 °C`, `60 °C`) ✓.
- **Inch-mark three-context rule (§4.1) — the designated parse hazard — is correct in every instance.** Markdown prose and table cells use literal `"` (`15,6"`, `15,6" (×3)`); `panorama/index.mdx` frontmatter L3 uses the escaped `15,6\"`. No `<Tab title=>` exists in F2, so no `&quot;` context arises. Notably **the DE frontmatter fixes the NL defect the glossary calls out by name** — NL left `panorama/index.mdx` at `Panorama 15.6\"` with a period; DE correctly writes `15,6\"`.
- Ratios unspaced (`16:9`, `1000:1`), `cd/m²` retained, `10 ms` / `60 Hz` / `144 Hz` correct.
- DIN 5008 divergences from NL (`99 % sRGB`, `100 % sRGB`, `150 %`, `5 V`, `±2 V`, `−20 °C`) are the §11-accepted lock — **not flagged**, per brief.

### OSD handling (§6) — clean
- ALL-CAPS device labels verbatim: `ON/OFF`, `RTS`, `FPS` preserved in `**DCR (Dynamic Contrast Ratio) (ON/OFF):**`.
- On-device menu *values* stay English (§6.3): `**Standard:**`, `**RTS:**`, `**FPS:**`, `**Text:**`, `**Movie:**`, `**Game:**` — only the sentence after each colon is German. `User, Warm, Cool` kept EN even though NL translates them (`Gebruikersinstelling, Warm, Koel`) — **correct, not flagged** per brief.
- **All 68 headings in F2 were checked one-by-one against §6.4 / §7.3 / §7.4 and every one matches a locked row.** Spot checks: `### 1. Helligkeit`, `### 2. Bildmodi`, `### 3. Farbeinstellungen`, `### 4. OSD-Einstellungen`, `## Einstellungen im Bildschirmmenü`, `## Einstellungen pro Bildschirm`, `## Bildschirmkonfiguration (Betriebssystem)`, `### Das OSD-Menü öffnen`, `### Helligkeit anpassen`, `### Lautstärke anpassen`, `### 3 × Mini-HDMI-Anschlüsse`, `### Taste Ab (−)`, `### Taste Auf (+)`, `### Bestätigen-/Beenden-Taste`, `### Vorsicht beim Klappen`, `### Vor der Verwendung`, `## Aufbau und Aufstellung`, `## Displaytreiber installieren`, `## Lieferumfang`, `## Technische Daten`. No parenthetical device name appended to any heading (the `expand`-style defect §6.4 warns about).
- §6.2.1 gloss vocabulary exact across both OSD pages: `Helligkeit`, `Kontrast`, `Schwarzwert`, `Schärfe`, `Seitenverhältnis`, `Farbtemperatur`, `Rot`, `Grün`, `Blau`, `Sprache`, `OSD-Timer`, `Transparenz`.
- `**ECO-Modus:**` (singular) is correct for EN plural `**ECO modes:**` — §6.2.1 locks one German target regardless of EN casing/number. NL's plural `ECO-modi` was correctly **not** followed.
- `**Seitenverhältnis (16:9 / 4:3):**` — DE correctly translates where **NL left it English** (`**Aspect Ratio (16:9 / 4:3):**`). DE follows the glossary, not the NL drift.

### Bold run-in labels (§10.5) — clean
Full inventory extracted and reconciled against the locked table. Every run-in matches, with occurrence counts consistent with §10.5's stated totals:
`**Stromversorgung:**` ×4 · `**Konsole anschließen:**` ×2 · `**HDMI-Gerät anschließen:**` ×2 · `**Kurz drücken:**` ×2 · `**Lang drücken:**` ×1 · `**Lang drücken (1 Sekunde):**` ×1 · `**Arbeitsfläche erweitern:**` ×1 · `**Wichtig:**` ×2 · `**Achtung:**` ×1.
Mode labels (bold, no colon) also correct, **including the one legitimate differentiator**: `**Allgemeiner Modus**` in both; `**OSD-Modus**` ×2 in `lite/controls.mdx`; `**OSD-Menü-Modus**` ×2 in `lite-144hz/controls.mdx` — exactly mirroring the EN `OSD mode` / `OSD menu mode` split and the §10.5 rows.

### Safety chapters (§11.0 frozen) — clean, no negation weakening
All three `safety.mdx` files checked clause-by-clause against EN. Every prohibition and every restrictive quantifier survives intact:
- "Only use the included AC/DC adapter" → `Verwende **ausschließlich** das mitgelieferte AC/DC-Netzteil` (not the weaker `nur`).
- "Do not use liquids or aggressive cleaning agents" → `Verwende **keine** Flüssigkeiten oder aggressiven Reinigungsmittel.`
- "Do not touch … and do not use it …" → both negations kept: `Berühre … **nicht** … und verwende es **nicht** …`
- "Do not drop the monitor" → `Lass den Monitor **nicht** fallen`.
- "Do not use sharp objects on or around the screen" → `Verwende **keine** scharfen Gegenstände auf oder um den Bildschirm.`
- Frozen locked constructions reproduced verbatim: `der Monitor arbeitet mit einem DC-Eingang` (§10.2 trap), `Risiken wie Stromschlag oder Brand` (§10.1 amended row), `Achte beim Ein- und Ausklappen der Bildschirme auf deine Finger` (§10.2 amended row — `auf`-phrase correctly after the adverbial). Neither amended row was "restored" to its pre-amendment wording.
- `de/manuals/lite/safety.mdx` and `de/manuals/lite-144hz/safety.mdx` are **identical**, matching EN and NL. ✓
- Correctly tracks the EN distinction between `panorama/installation.mdx` L28 `beim Klappen der Bildschirme` (EN "when folding the screens") and `panorama/safety.mdx` L26 `beim Ein- und Ausklappen der Bildschirme` (EN "when folding the screens in or out"). Not a drift — the sources differ.

### Literal-translation traps (§10.2) — clean
Every trap in the table was searched for; none present. Confirmed correct handling of: `Achte darauf, dass` (not `Mache sicher`), `Klicke auf „Anordnen“` (with `auf`), `Folge den Schritten auf dem Bildschirm`, `Sobald beide Verbindungen hergestellt sind`, `Kurz drücken` / `Lang drücken` (not `Kurzer Druck`), `Stecke … in den Anschluss`, `genug Strom liefert`, `Ziehe die Bildschirme in die richtige Reihenfolge`, `wie in Abbildung 1 gezeigt`, `Wähle die Variante, die zu deinem Gerät … passt`.

### OS UI labels (§9) — clean
`Anzeigeeinstellungen`, `„Desktop auf diese Anzeige erweitern“`, `Schaltfläche Identifizieren`, `Anzeigeausrichtung`, `„Querformat (gedreht)“`, `Skalierung`, `Systemeinstellungen`, `Displays`, `Anordnen` — all match the locked German OS strings. `Schaltfläche` (not `Taste`) correctly used for on-screen OS buttons per §10.4, while physical device buttons take `Taste`.
The `„Display settings“ („Anzeigeeinstellungen“)` parenthetical rule was checked and correctly **not** applied here: §9 scopes it to the frozen display-settings chapter, which F2 has no instance of, and NL's `panorama/osd.mdx` likewise gives the localised label alone.

### `de/manuals-index.mdx` — clean
All 11 card titles use the §7.5 `{Product} – Handbuch` pattern with en dash. Help cards (`Support kontaktieren` / `Produkte ansehen` / `Garantieinformationen`) and their body text (`Hilfe von unserem Support-Team erhalten` / `Alle Screenmate-Produkte durchsuchen` / `Mehr über die Produktgarantie erfahren`) match §7.5 exactly. `**Du hast einen QR-Code gescannt?**` ✓. Headings `# Willkommen bei den Screenmate-Handbüchern`, `## Verfügbare Handbücher`, `## Brauchst du Hilfe?` ✓ §7.3. Frontmatter `Screenmate-Produkthandbücher` / `Digitale Handbücher für alle Screenmate-Produkte` ✓ §7.1/§7.2. The `{/* … */}` future-product template block is **correctly left in English** including `[Product Name] Manual` and `Brief product description`, per the §7.7 note. Only F1 applies to this file.

### Frontmatter titles & descriptions (§7.1 / §7.2) — clean
All 16 match locked rows: `Screenmate Lite – Handbuch`, `Screenmate Lite 144 Hz – Handbuch`, `Screenmate Panorama – Handbuch`, `Installation`, `Anschlüsse und Tasten`, `Bildschirmmenü (OSD)`, `Sicherheitshinweise`; descriptions `So schließt du deinen Screenmate {X} an`, `Aufbau und Anschluss deines Screenmate Panorama`, `Übersicht über die Anschlüsse und Bedientasten`, `Bildschirmeinstellungen über das Bildschirmmenü`, `Bildschirmeinstellungen pro Bildschirm über das Bildschirmmenü`, `Wichtige Sicherheitshinweise und Warnungen`, `Vollständiges Handbuch für deinen tragbaren Monitor Screenmate {X}`. Gender is `der Screenmate` throughout (§1.0), including `den Panorama`, `dem Screenmate`, `deinen Screenmate Lite 144 Hz`.

### Genuine differentiators — verified as correctly *different*
Confirmed these are not accidentally harmonised: `Bildwiederholrate` `60 Hz` (lite) vs `144 Hz` (lite-144hz); product tokens `Screenmate Lite` vs `Screenmate Lite 144 Hz` in every heading, title and alt; image paths `…%20Lite%20-%20…` vs `…%20Lite%20144Hz%20-%20…`; `**OSD-Modus**` vs `**OSD-Menü-Modus**`. Shared specs correctly identical where EN is identical: `10 ms`, `609 Gramm`, `350 cd/m²`, `1000:1`, `172°`, `99 % sRGB`, `35,4 × 22,1 × 1,1 cm`, `15,6"`.

### Explicitly not flagged, per brief
Color Temperature presets kept EN (`User, Warm, Cool`); the client-dictated `panorama` Info cable block (`Verwende das lange weiße Kabel für den Strom …`, translated literally); `Reverse Charging` kept EN with its licensed one-time gloss `(Reverse Charging, also umgekehrtes Laden)` per §5; SI/DIN spacing divergences from NL; descriptive button-name translations (`Power- und Zurück-Taste`, ruling R8).

### Incidental observation (no action for DE)
DE tracks EN more faithfully than NL in `panorama/installation.mdx` L58: EN "does not supply enough power **on its own** … at full brightness" → DE `liefert **allein** nicht genug Strom, um den Panorama mit voller Helligkeit zu betreiben`, whereas NL dropped "on its own" and moved "maximale helderheid" into the following clause. The German is correct; the NL is the drifted one. Noted only so a future reviewer does not "fix" DE toward NL here.
