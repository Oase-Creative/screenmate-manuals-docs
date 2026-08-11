# DE — `lite-144hz` (index, installation, controls, osd)

Task 7-de / lite-144hz. Format: `- [file] EN says X / NL says Y — blocked|proceeded-with-Z`

Raised: 5. Blocked: 0.

## EN↔NL divergences

- [osd.mdx] EN says the Color Temperature presets are **`User, Warm, or Cool`** (English on-device
  values) / NL says **`Gebruikersinstelling, Warm of Koel`** — NL translated two of the three preset
  values — proceeded-with `Wähle User, Warm oder Cool`. Glossary §6.3 lists `Warm`, `Cool`, `User`
  as on-device menu values that stay verbatim English, and §6.2 confirms the presets beside a
  translated gloss are never translated. The NL page is the outlier, not the EN one; German follows
  EN + the glossary. Worth reporting upstream: the NL page contradicts its own OSD-verbatim rule.

- [osd.mdx] EN frontmatter `title: "On-Screen Menu (OSD)"` and `## On-Screen Menu Settings` /
  NL frontmatter `title: "Beeldscherminstellingen (OSD)"` and `## Beeldscherminstellingen`
  (= *display settings*, i.e. NL names the chapter after the settings, EN after the menu) —
  proceeded-with `Bildschirmmenü (OSD)` / `## Einstellungen im Bildschirmmenü` per glossary §7.1
  and §7.3, which lock both strings against the EN headings. EN is the structural template.

- [osd.mdx] EN says `### 2. Image Modes` / NL says `### 2. Modusopties` (= *mode options*) —
  proceeded-with `2. Bildmodi`, the locked §6.4 target for the EN heading.

- [installation.mdx] EN `<Note>` lead-in is `**Important:**` / NL is `**Let op:**` (= *note / mind
  this*) — proceeded-with `**Wichtig:**`, the §10.1 target for the EN string. EN is the structural
  template; the NL page softened the callout.

- [installation.mdx] EN §5 opens "To connect **the Screenmate** to an HDMI device…" / NL opens
  "Om **de draagbare monitor** aan te sluiten…" (= *the portable monitor*) — same referent,
  different noun — proceeded-with `den Screenmate`, following the EN template. Recorded only so a
  later pass does not re-open it.

## Glossary-vs-source notes (no EN/NL conflict — recorded for the reviewer)

- [controls.mdx, osd.mdx] Both EN and NL keep the on-device button name in English
  (`Power & Return Button` / `Power & Return-knop`). Glossary §7.4 nevertheless locks
  `Power & Return Button` → `Power- und Zurück-Taste`, and the string is **not** in `dnt.json`
  nor in the §6.1 ALL-CAPS token list. Translated per the binding glossary, in the
  `### Power- und Zurück-Taste` heading and in the `osd.mdx` intro sentence alike. If the physical
  button is silk-screened "Power & Return", the client may want the EN token restored — an asset
  question, not a translation one. (Same observation as `it-lite-144hz.md`.)

- [index.mdx] EN and NL both write the resolution closed (`1920×1080`) while the dimensions row is
  spaced (`35.4 × 22.1 × 1.1 cm`). Glossary §4 locks resolutions to `×` **with** spaces, so DE ships
  `1920 × 1080`. Likewise `99% sRGB` → `99 % sRGB` per the §4 percent rule (DIN 5008), a deliberate
  DE-only divergence from the NL lock — see §11. Not a defect; do not "fix" back to the EN spacing.

- [index.mdx] `15.6" Full HD portable monitor` became `15,6"-Full-HD-Monitor` (§3.2 Durchkopplung
  with the inch mark retained per §4, which forbids expanding to `Zoll`). Flagged only because the
  glossary's compound example uses the spelled-out `15,6-Zoll-Bildschirm` while its number table
  forbids `Zoll`; the inch-mark form honours both the "keep the inch mark" and the "hyphenate every
  junction" rules.

## Proposed glossary additions (§12) — used on this page, not yet in `glossary-de.md`

| English | German (used) | Reason |
|---|---|---|
| `picture mode` | `Bildmodus` | `osd.mdx` ECO-modes bullet; aligns with the §6.4 heading target `2. Bildmodi`. |
| `widescreen` *(lowercase prose, not the `WIDE` token)* | `Breitbild` | `osd.mdx` Aspect Ratio bullet. Distinct from the §6.1/§6.3 device token `WIDE`, which is untouched. |
| `RGB value` | `RGB-Wert` | `osd.mdx` Red/Green/Blue bullets. Plain §3.1 acronym+noun Durchkopplung. |
| `connection scenario` | `Anschlussszenario` | `installation.mdx` intro. Triple-s spelling is correct post-1996; `Anschluss-Szenario` is the Duden-permitted legibility variant if the client prefers it. |
| `power user` | `Power-User` | `index.mdx` body. Established German loan; §3.1 hyphenates the English compound. |
| `Real-Time Strategy (RTS) games` / `First-Person Shooter (FPS) games` | `Real-Time-Strategy-Spiele (RTS)` / `First-Person-Shooter-Spiele (FPS)` | `osd.mdx` ECO-mode bullets. Genre names stay English and take full §3.1 Durchkopplung; the acronym moves after the noun so the CAPS token is not split. |
| `video support` | `Videounterstützung` | `installation.mdx` §3. All-German compound, closed per §3.1. |
