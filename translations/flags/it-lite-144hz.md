# IT — `lite-144hz` (index, installation, controls, osd)

Task 7-it / lite-144hz. Format: `- [file] EN says X / NL says Y — blocked|proceeded-with-Z`

Raised: 4. Blocked: 0.

## EN↔NL meaning divergences

- [osd.mdx] EN says the Color Temperature presets are **`User, Warm, or Cool`** (English on-device
  values) / NL says **`Gebruikersinstelling, Warm of Koel`** — NL translated two of the three preset
  values — proceeded-with `scegli User, Warm o Cool`. Glossary §7.2 lists `Warm`, `Cool`, `User` as
  on-device preset values that stay English, and §7.3.1 confirms the presets beside a translated
  gloss are never translated. The NL page is the outlier here, not the EN one; Italian follows EN +
  the glossary. Worth reporting upstream: the NL page contradicts its own OSD-verbatim rule.

- [osd.mdx] EN frontmatter `title: "On-Screen Menu (OSD)"` and `## On-Screen Menu Settings` /
  NL frontmatter `title: "Beeldscherminstellingen (OSD)"` and `## Beeldscherminstellingen`
  (= *Display settings*, i.e. NL names the chapter after the settings, EN after the menu) —
  proceeded-with `Menu a schermo (OSD)` / `## Impostazioni del menu a schermo` per glossary
  §9.1 and §9.3, which lock both strings against the EN headings. EN is the structural template.

- [osd.mdx] EN says `### 2. Image Modes` / NL says `### 2. Modusopties` (= *mode options*) —
  proceeded-with `2. Modalità immagine`, the locked §9.6 target for the EN heading.

- [installation.mdx] EN §5 opens "To connect **the Screenmate** to an HDMI device…" / NL opens
  "Om **de draagbare monitor** aan te sluiten…" (= *the portable monitor*) — same referent, different
  noun — proceeded-with `lo Screenmate`, following the EN template. Recorded only so a later pass
  does not re-open it.

## Glossary-vs-source notes (no EN/NL conflict — recorded for the reviewer)

- [controls.mdx, osd.mdx] Both EN and NL keep the on-device button name in English
  (`Power & Return Button` / `Power & Return-knop`). Glossary §9.4 nevertheless locks
  `Power & Return Button` → `Pulsante di accensione e ritorno`, and the string is **not** in
  `dnt.json` nor in the §7.1 ALL-CAPS token list. Translated per the binding glossary, in the
  `### Pulsante di accensione e ritorno` heading and in the `osd.mdx` intro sentence alike.
  If the physical button is silk-screened "Power & Return", the client may want the EN token
  restored — that is an asset question, not a translation one.

## Proposed glossary additions (§12) — used on this page, not yet in `glossary-it.md`

| English | Italian (used) | Reason |
|---|---|---|
| `General mode` *(controls bold run-in)* | `Modalità generale` | `controls.mdx` — bold run-in above the scroll-wheel / power-button bullet lists; no §9.9 row covers it. Mirrors NL `Algemene modus`. |
| `OSD menu mode` *(controls bold run-in)* | `Modalità menu OSD` | `controls.mdx` — sibling of the above. `menu OSD` per §2.1. |
| `picture mode` | `modalità immagine` | `osd.mdx` ECO-modes bullet; aligns with the §9.6 heading target `2. Modalità immagine`. |
| `widescreen` *(lowercase prose, not the `WIDE` token)* | `formato panoramico` | `osd.mdx` Aspect Ratio bullet. Distinct from the §7.2 device token `WIDE`, which is untouched. |
| `RGB value` | `valore RGB` | `osd.mdx` Red/Green/Blue bullets. Follows the §2.1 `NOUN + ACRONYM` rule. |
| `connection scenario` | `scenario di collegamento` | `installation.mdx` intro. `collegamento`, never `connessione` (§6). |
