# DE Panorama flags

Task 7-de / slug `panorama`. Pages: index, installation, controls, osd
(safety.mdx belongs to Task 6; this product has no display-settings.mdx).

Format: `- [file] EN says X / NL says Y — blocked|proceeded-with-Z`

Raised: 7. Blocked: 0.

## VERBATIM-SENSITIVE ZONE — client-dictated copy

- [installation.mdx] The `<Info>` block under "Option 1 – USB-C (nur ein Kabel)" is
  **client-dictated copy**, authored in Dutch and mirrored into EN. EN says "Use the long
  white cable for power, and the short black cable to connect the Panorama to your
  laptop." / NL says "Gebruik de lange witte kabel voor stroom, en de korte zwarte kabel
  om de Panorama met je laptop te verbinden." — **EN and NL agree exactly**; no
  divergence to resolve. Translated with extra literalness, preserving all four
  load-bearing attributes and their pairings:
  `lang + weiß → Strom`, `kurz + schwarz → Verbindung zum Laptop`.
  German: `Verwende das lange weiße Kabel für den Strom und das kurze schwarze Kabel, um
  den Panorama mit deinem Laptop zu verbinden.`
  **Do not paraphrase, reorder, or "improve" this sentence in any later pass.** The two
  cables are physically distinguishable only by length and colour, and the Option 2 step
  3 instruction ("HDMI-Anschluss neben dem weißen Netzkabel") depends on the white cable
  still being identified as the power cable here. Any client revision to the Dutch must
  be re-mirrored into DE verbatim rather than re-translated from EN.

## EN/NL divergences

- [installation.mdx] EN says the laptop USB-C port "does not supply enough power on its
  own to run the Panorama **at full brightness**" and closes with "Always connect the
  65 W adapter for stable operation." / NL splits it differently: "levert niet genoeg
  stroom om de Screenmate Panorama **optimaal te laten functioneren**" and appends the
  brightness claim to the second sentence ("voor een stabiele werking **en maximale
  helderheid**"); NL also adds "meegeleverde" (supplied) — proceeded-with the EN
  distribution: `… nicht genug Strom, um den Panorama mit voller Helligkeit zu betreiben.
  Schließe für einen stabilen Betrieb immer das 65-W-Netzteil an.` Same claim, EN is the
  structural template.

- [installation.mdx] EN says "Connecting a separate charger to your laptop **while the
  Panorama is also providing power** may cause interference." / NL drops the concessive
  clause: "Als je daarnaast nog een extra oplader aansluit, kan dit storingen
  veroorzaken." — proceeded-with the fuller EN version (`… während der Panorama ihn
  ebenfalls mit Strom versorgt …`). The clause names the actual failure condition, so
  dropping it loses information.

- [installation.mdx] EN says "your laptop" throughout the connection steps (Option 1
  step 2; Option 2 steps 2 and 3) / NL says "je pc of laptop" (PC *or* laptop) —
  proceeded-with EN (`deines Laptops`). The driver section above it already says "PC oder
  Laptop" in both trees, so the narrower wording in the steps is EN's deliberate scope,
  not an omission.

- [controls.mdx] EN says "Connect the supplied 65 W power adapter here using the USB-C to
  USB-C cable" (adapter is the object) / NL inverts the sentence: "Sluit hier de USB-C-
  kabel aan op de meegeleverde 65 W-voedingsadapter" (cable is the object) —
  proceeded-with the EN direction: `Schließe hier das mitgelieferte 65-W-Netzteil über
  das USB-C-auf-USB-C-Kabel an.` Identical physical action; EN's phrasing keeps the
  section heading (`USB-C-Ladeanschluss`) as the thing being described.

- [osd.mdx] EN says "**Follow the steps below to configure each display.**" / NL says
  "Volg de stappen hieronder om **alles eenvoudig** in te stellen" (= to set *everything*
  up easily — drops "each display", adds "easily") — proceeded-with EN: `Folge den
  Schritten unten, um jeden Bildschirm einzurichten.` "Each screen" is the point of the
  whole chapter (per-screen OSD), so EN carries the meaning.

- [osd.mdx] EN says Windows orientation option `**"Flipped"**` / NL says
  `**"Gespiegeld"**` (= mirrored) — proceeded-with `**„Querformat (gedreht)“**` per
  glossary §9. German Windows has no standalone "Gedreht" entry and `Gespiegelt` does not
  exist in the German dropdown. Same ruling as `de-shared.md` made for
  `infinity-lite/display-settings.mdx`; glossary §11 already lists the German string as
  pending verification against a real German Windows install.

- [osd.mdx] EN heading says `## Display Configuration (OS-Level)` / NL says
  `## Beeldschermconfiguratie (op je computer)` (= "on your computer" — paraphrases the
  OS-level qualifier) — proceeded-with the glossary §7.3 lock
  `## Bildschirmkonfiguration (Betriebssystem)`, which follows EN.

## Non-flag decisions worth recording

- **Windows/macOS UI labels are German-only in this file, no English parenthetical.**
  Glossary §9's "„Display settings“ („Anzeigeeinstellungen“) on first mention" instruction
  is scoped to the *display-settings chapter* (Task 6). `panorama/osd.mdx` is a different
  chapter and NL ships Dutch-only labels here (`Beeldscherminstellingen`,
  `Identificeren`, `Beeldschermstand`, `Schaal`), so DE ships German-only
  (`Anzeigeeinstellungen`, `Identifizieren`, `Anzeigeausrichtung`, `Skalierung`).
  **Same asset caveat as `de-shared.md`:** the referenced screenshots are not German, so
  the labels will not match the images. Asset decision, not a translation change.
- **`button` splits two ways** per glossary §10.4: device buttons are `Taste`
  (`Power-Taste`, `Taste Auf (+)`, `Taste Ab (−)`), OS UI buttons are `Schaltfläche`
  (`Schaltfläche Identifizieren`, `Schaltfläche „Anordnen“`).
- **`Confirm / Exit Button` bold boundary moved.** EN writes `the **Confirm / Exit**
  button` with "button" outside the bold; German folds the noun into the locked compound
  `**Bestätigen-/Beenden-Taste**` (§7.4), matching what NL did
  (`**Bevestig- / Exit-knop**`). Splitting the German compound across the bold marker is
  not writable.
- **`Reverse Charging` glossed once on first use** — `(Reverse Charging, also umgekehrtes
  Laden)` in `installation.mdx`, per its §5 keep-EN lock. It appears exactly once in this
  slug, so there is no second occurrence to strip the gloss from.
- **DIN 5008 unit spacing** applied (§4, §11): `100 % sRGB` (EN `100% sRGB`), `150 %`
  (EN `150%`). Deliberately unlike the NL lock — **not** an nl↔de parity defect.
- **`1920×1080` normalised to `1920 × 1080`** (§4, resolution takes spaced `×`); EN and NL
  both ship it unspaced in this file. Same precedent as `de-expand.md`. Purely
  typographic.
- **Spec field `Backlight` → `Hintergrundbeleuchtung`** (§8) although NL keeps the English
  `Backlight`; glossary §11 settles this (NL's keep-EN spec rows are booklet inheritance).
- **Frontmatter inch mark: `15,6\"` with a comma.** Glossary §4.1 flags
  `nl/manuals/panorama/index.mdx` by name for leaving its frontmatter at `15.6\"` with a
  period while `flip` used the comma; DE applies the comma in all three contexts —
  frontmatter `15,6\"`, markdown body `15,6"`. No `&quot;` context exists in this slug
  (no `<Tab>` elements).
- **Cable lengths abbreviated, not spelled out.** EN `(1.2 m)` / NL `(1,2 meter)` — DE
  keeps EN's abbreviation with a German decimal comma and DIN spacing: `(1,2 m)`,
  `(0,5 m)`. Formatting only.
- **`65 Watt USB-C power adapter` → `65-Watt-USB-C-Netzteil`.** EN spells out "Watt" here
  (elsewhere in the slug it is `65 W` → `65-W-Netzteil`); the spelled-out form is carried
  over and fully Durchkopplung-hyphenated per §3.2. The two forms coexist in the EN source
  and the divergence is preserved.
- **Em dashes → en dashes** (§3.6) in both `### Option 1 – …` / `### Option 2 – …`
  headings and in the frontmatter title `Screenmate Panorama – Handbuch`.
- **EN's mixed bullet voice in `controls.mdx` is mirrored**, not normalised: the first two
  bullets under each of `Taste Ab (−)` / `Taste Auf (+)` are infinitive phrases
  (`Im Menü navigieren.`) and the third is third-person (`Öffnet das
  Schnellzugriffsmenü …`), exactly as EN and NL both do.
