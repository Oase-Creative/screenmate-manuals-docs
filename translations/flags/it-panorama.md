# IT — Panorama: EN↔NL meaning discrepancies

Format: `- [file] EN says X / NL says Y — blocked|proceeded-with-Z`

Raised by Task 7-it (`it/manuals/panorama/{index,installation,controls,osd}.mdx`).
Phrasing-only differences are deliberately **not** listed here.
`safety.mdx` is out of scope for this task (Task 6 owns it; its one flag is in `it-shared.md`).

## Windows "Flipped" vs "Gespiegeld" (Mirrored) — different Windows options

- [it/manuals/panorama/osd.mdx, §Configurazione dello schermo ▸ Windows] EN says `choose **"Flipped"**` / NL says `kies **"Gespiegeld"**` (= Mirrored/Duplicato) — proceeded-with-`**"Capovolto"**`
  (Glossary §8 rules `Flipped → Capovolto` and marks `Mirrored → Duplicato` as *superseded — EN pages now say "Flipped"*. EN is the structural template and the glossary ruling is binding, so no block. Identical to the discrepancy already logged in `it-shared.md` for the six `display-settings.mdx` pages — panorama carries the same passage inline in `osd.mdx` instead, so it is recorded here too. Client should still confirm which Windows control the screenshot actually shows.)

## Verbatim-sensitive zone — client-dictated `<Info>` copy (cable colours)

**No EN↔NL discrepancy — EN and NL agree exactly.** Recorded because the passage is client-dictated
copy originating in NL and any future edit must preserve its literal meaning, not paraphrase it.

- [it/manuals/panorama/installation.mdx, §Opzioni di collegamento ▸ Opzione 1, `<Info>`]
  - EN: `Use the long white cable for power, and the short black cable to connect the Panorama to your laptop.`
  - NL: `Gebruik de lange witte kabel voor stroom, en de korte zwarte kabel om de Panorama met je laptop te verbinden.`
  - IT: `Usa il cavo bianco lungo per l'alimentazione e il cavo nero corto per collegare il Panorama al tuo laptop.`
  - Translated with extra literalness: both distinguishing attributes (length **and** colour) are carried on both cables, in the same order, with the same cable→role assignment (white = power, black = laptop). Adjective order is `colore + lunghezza` (`cavo bianco lungo`), the natural Italian sequence with the classifying adjective adjacent to the noun; no adjective was dropped or merged. `il Panorama` mirrors EN/NL's bare product reference without `Screenmate`.
  - **Do not paraphrase on review.** Reversing the cable→role mapping, dropping either adjective, or generalising to "il cavo di alimentazione" would break a client-dictated instruction that is the page's only disambiguation between two supplied USB-C cables (1,2 m and 0,5 m, `index.mdx`).
  - Related, same page: step 3 of Opzione 2 refers back to this cable as `il cavo di alimentazione bianco` (EN `the white power cable`) — the colour must stay attached there too.

## Non-flags — checked and dismissed (recorded for the reviewer)

- [installation.mdx, `<Note>` after step 4] EN `Watch your fingers when folding the screens` (direction unspecified) / NL `tijdens het inklappen van de schermen` (= while folding the screens **in**/closed). NL narrows, it does not contradict; the hazard exists in both directions and the note sits between the unfolding steps and the "fold back up" sentence. Rendered with EN's unspecified `quando pieghi gli schermi`.
- [installation.mdx, `<Note>` on adapter] EN attaches "at full brightness" to sentence 1 and says only `stable operation` in sentence 2; NL says `optimaal te laten functioneren` in sentence 1 and adds `en maximale helderheid` plus `meegeleverde` (supplied) to sentence 2. Same two facts, redistributed across the two sentences. EN followed.
- [installation.mdx, reverse-charging `<Note>`] EN `Connecting a separate charger to your laptop while the Panorama is also providing power may cause interference` / NL `Als je daarnaast nog een extra oplader aansluit, kan dit storingen veroorzaken` (omits both "to your laptop" and the "while the Panorama is also providing power" clause). EN is strictly more specific; EN followed. `reverse charging` glossed per glossary §5.2 / decision 11.1.3 as `ricarica inversa (reverse charging)`, matching the three existing occurrences in `it/manuals/onecable/`.
- [installation.mdx, Opzione 1 step 2 and Opzione 2 step 2] EN `your laptop's USB-C port` / `a USB-A port on your laptop`; NL `je pc of laptop` in both. EN followed.
- [installation.mdx, §Installa il driver dello schermo] EN `you must install the correct display driver` / NL `is het belangrijk om eerst het juiste stuurprogramma te installeren` (= it is important to). Modal strength differs slightly; EN followed (`devi installare`). Note NL uses `stuurprogramma` throughout where EN uses `display driver` — glossary §5.3 locks the invariable `il driver` / `driver dello schermo`.
- [osd.mdx, §Windows] EN `Need more room?` / NL `Meer overzicht nodig?`, and EN `larger text and UI elements` / NL `een grotere weergave van tekst en elementen` (no "UI"). Glossary §9.10 explicitly collapses the `Need more overview? / Want more on-screen space? / Need more room?` group onto the single target `Vuoi più spazio a schermo?` and locks the body as `per testo ed elementi più grandi`, byte-identical across every Italian page. Locked targets used; EN's "UI" is part of the drift the collapse resolves.
- [osd.mdx, `## Display Configuration (OS-Level)`] EN `(OS-Level)` / NL `(op je computer)` (= on your computer). Glossary §9.3 locks the EN form as `Configurazione dello schermo (a livello di sistema operativo)`. Heading-name drift, not a meaning conflict.
- [osd.mdx, §Regolazione della luminosità, bullet 3] EN `Press the Down (−) button again to open the brightness menu for the next screen` / NL `Druk je nogmaals op de Omlaag-knop, dan wordt het helderheidsmenu van het volgende scherm geopend` (conditional phrasing). Same instruction; EN's imperative followed.
- [osd.mdx, §Impostazioni per singolo schermo] EN `Follow the steps below to configure each display` / NL `Volg de stappen hieronder om alles eenvoudig in te stellen` (= to set everything up easily). EN is more specific; EN followed.
- [controls.mdx, §Pulsante di accensione] EN `Opens the OSD menu … for the currently selected screen` / NL `voor de gekozen monitor` (= for the chosen monitor). Same referent; EN followed.
- [controls.mdx, §Pulsante Giù/Su] EN `Opens the brightness/volume shortcut menu` / NL `Activeert het helderheids-/volumemenu` (= activates the …menu, no "shortcut"). EN followed (`Apre il menu rapido della luminosità` / `del volume`).
- [controls.mdx, §Porta USB-C di ricarica] EN `Connect the supplied 65 W power adapter here using the USB-C to USB-C cable` / NL `Sluit hier de USB-C-kabel aan op de meegeleverde 65 W-voedingsadapter` (cable and adapter swap roles as object/complement). Same physical action; EN followed.
- [index.mdx] EN `A required display driver allows three independent screens to be driven through one cable` / NL `Een vereiste display-driver maakt het mogelijk om…` — identical. Rendered as `Per gestire tre schermi indipendenti tramite un solo cavo è necessario installare il driver dello schermo.`: a clause-order change only, chosen because a postposed `necessario` on `driver` reads ambiguously in Italian. No content added or dropped.
- [index.mdx, §Specifiche tecniche] EN `Size | 15.6" (×3)` / NL `Grootte | 15,6" (×3)`, EN `Contrast Ratio` / NL `Contrast ratio`, EN `Color Gamut` / NL `Kleurdekking`, EN `Supported OS` / NL `Ondersteunde systemen`. NL-internal field-naming drift; glossary §5.4 targets used against the EN field names. Unlike `expand/index.mdx`, panorama's single spec table already labels the `100% sRGB` row `Color Gamut`, so no accuracy/gamut conflict arises here.
- [index.mdx, §Contenuto della confezione] EN `1x … cable (1.2 m)` / NL `1x …-kabel (1,2 meter)` (unit spelled out). Glossary §4.1 locks the symbol form with a comma decimal: `(1,2 m)`, `(0,5 m)`.
- [all four files] NL writes `15.6` in frontmatter but `15,6` in body; EN writes `15.6` throughout. IT uses `15,6` everywhere per glossary §4.5 — including the frontmatter `description`, where the inch mark stays backslash-escaped (`15,6\"`) exactly as EN escapes it.
