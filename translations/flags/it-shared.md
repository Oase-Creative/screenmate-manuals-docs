# IT — shared chapters (safety, display-settings): EN↔NL meaning discrepancies

Format: `- [file] EN says X / NL says Y — blocked|proceeded-with-Z`

Raised by Task 6-it. Phrasing-only differences are deliberately **not** listed here.

## Windows "Flipped" vs "Gespiegeld" (Mirrored) — different Windows options

- [it/manuals/{onecable,dual-flip,flip,expand}/display-settings.mdx, "Schermo capovolto?" §Windows] EN says `choose 'Flipped'` / NL says `kies 'Gespiegeld'` (= Mirrored/Duplicato) — proceeded-with-`'Capovolto'`
  (glossary §8 rules `Flipped → Capovolto` and marks `Mirrored → Duplicato` as *superseded — EN pages now say "Flipped"*. EN is the structural template; the glossary ruling is binding, so no block. Client should still confirm which Windows control the screenshot actually shows.)
- [it/manuals/infinity/display-settings.mdx, §Display Configuration ▸ Windows tab] EN says `choose **"Flipped"**` / NL says `kies **'Gespiegeld'**` — proceeded-with-`**"Capovolto"**` (same ruling)
- [it/manuals/infinity-lite/display-settings.mdx, §Configurazione dello schermo ▸ Windows] EN says `choose **Flipped**` / NL says `kies **'Gespiegeld'**` — proceeded-with-`**Capovolto**` (same ruling)

### Related — EN-internal inconsistency, no EN↔NL conflict

- [it/manuals/infinity-lite/display-settings.mdx, §Disponi gli schermi (video) ▸ Windows] EN says `choose 'Mirrored'` / NL says `kies 'Gespiegeld'` — **EN and NL agree here** → rendered `'Duplicato'` per glossary §8.
  Consequence: the infinity-lite page now says `Capovolto` in its first Windows section and `Duplicato` in the video section, exactly mirroring the EN page's own `Flipped` / `Mirrored` split. This is faithful to the EN template but is an **EN-side editorial defect** — recommend the client normalise the EN page, after which the IT page should follow in one edit.

## Safety — scope of non-domestic use

- [it/manuals/panorama/safety.mdx, §Prima dell'uso] EN says `Suitable for both home and professional use.` / NL says `Geschikt voor zowel thuis als zakelijk gebruik.` (= *business* use) — proceeded-with-`Adatto sia all'uso domestico sia a quello professionale.`
  (EN followed as structural/semantic template. Note the sibling pages `infinity` and `infinity-lite` say `business use` in EN **and** `zakelijk` in NL, and are rendered `aziendale`; only panorama's EN diverges to `professional`. Low severity — both readings contrast with domestic use — but the IT corpus now carries two different adjectives for what is plausibly one sentence. Client may wish to normalise EN.)

## Non-flags — checked and dismissed (recorded for the reviewer)

- Safety intro heading, infinity / infinity-lite / panorama: EN `Check before use` / `Read this before use` / `Before use` vs NL's single `Let hierop vóór gebruik` for all three. Glossary §9.5 already locks all three EN variants separately (`Controlla prima dell'uso` / `Leggi prima dell'uso` / `Prima dell'uso`) — EN followed, no flag.
- NL `nl/manuals/onecable/safety.mdx` body differs from its six group-A siblings by exactly one trailing blank line; text is identical. Not a meaning difference.
- `Open Display Settings` (EN infinity) vs `Ga naar de Beeldscherminstellingen` (NL), `Want more on-screen space?` vs `Heb je behoefte aan meer overzicht?`, `Turn off the screen when not in use` vs `als je het niet gebruikt` — phrasing only.
