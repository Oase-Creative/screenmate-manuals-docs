# Round 4 — Italian: source-inherited findings (EN/NL side, not translation defects)

**Date:** 2026-08-12 · **Branch:** `round4-fixes` · **Scope:** `it/**`

Every item below was raised against the Italian pages by
`fluency-it-a.md`, `fluency-it-b.md` or `safety-align-it.md`, and every one of them turned out to
be **faithful to the English structural base** (and, where checked, to the Dutch source). The
Italian was therefore left untouched: fixing it on the Italian side alone would break EN↔IT
parity and would silently diverge from `de`, `fr` and `nl`.

These are **client / EN-source decisions**. Where the fix belongs on the English page, that is
noted. Where it is a product-fact question, no wording is proposed — the facts are not the
translator's to invent.

Legend: **[SAFETY]** = the Italian body is additionally frozen (four rounds of meaning
verification passed), so even a purely stylistic change is out of scope for this pass.

---

## 1. Reader-blocking contradictions carried by the source

### 1.1 5–20 V input vs. "esclusivamente 5 V" — **[SAFETY]**

| | |
|---|---|
| **Files** | `it/manuals/{onecable,lite,lite-144hz,flip,expand,one-4k,one-4k-oled}/safety.mdx` items 5–6 · `it/manuals/dual-flip/safety.mdx` bullets 5–6 |
| **IT** | `Il monitor funziona con un ingresso DC compreso tra 5 V e 20 V (con una tolleranza di ±2 V).` / `Usa il dispositivo esclusivamente con una fonte di alimentazione da 5 V tramite il cavo appropriato.` |
| **EN** | `The monitor operates with a DC input between 5V and 20V (with a tolerance of ±2V).` / `Only use the device with a 5V power source via the appropriate cable.` |

Two consecutive safety points accept 5–20 V and then restrict the user *exclusively* to 5 V. The
contradiction is present verbatim in English. Rated Critical by both fluency reviewers; the
line-alignment audit (`safety-align-it.md` §R2) independently confirmed the Italian scoping is
correct and in fact **less** ambiguous than the English. Needs an engineering ruling on the EN
page, then propagation to all five languages.

### 1.2 Infinity Lite port map: "leftmost" port vs. "third" port

| | |
|---|---|
| **Files** | `it/manuals/infinity-lite/controls.mdx` · `it/manuals/infinity-lite/installation.mdx` |
| **IT** | `La porta più a sinistra in basso.` (reserved for the HDMI→USB-C cable) / `Collega il cavo da HDMI a USB-C alla **terza** porta dello Screenmate per il segnale video.` |
| **EN** | `The leftmost bottom port.` / `Connect the HDMI to USB-C cable to the **third** port of the Screenmate for the video signal.` |

The product documents two USB-C ports plus a 3.5 mm jack, so "the third port" has no referent.
Both statements are word-for-word EN. Product-fact question for the client: what is the real port
map, and which numbering scheme should the manuals use?

### 1.3 Infinity brightness/volume control map

| | |
|---|---|
| **File** | `it/manuals/infinity/controls.mdx` |
| **IT** | `**Premi a destra ("Plus"):** aumenta la retroilluminazione (luminosità).` / `**Premi a sinistra ("Min"):** riduci il volume.` |
| **EN** | `**Press right ("Plus"):** increase the backlight (brightness).` / `**Press left ("Min"):** decrease the volume.` |

Under a heading promising *brightness and volume*, only "raise brightness" and "lower volume" are
documented — there is no documented way to lower brightness or raise volume, and
`infinity-lite/controls.mdx` maps the same two labels the other way round (left = brightness,
right = volume). Identical in English. Needs the real gesture map from the client.

> The `("Plus")` / `("Min")` labels themselves are **EN source strings** and are glossary-locked
> (§9.9). `Min` is Dutch in origin, but it reaches Italian through the English page, so changing
> it is an EN-side decision.

### 1.4 Infinity Lite orientation value: `'Duplicato'` vs `'Capovolto'`

| | |
|---|---|
| **File** | `it/manuals/infinity-lite/display-settings.mdx` (top section vs. the Tabs/video section) |
| **IT** | `…scegli **Capovolto** per correggerlo.` / `…scegli 'Duplicato' per correggerlo.` |
| **EN** | `…choose **Flipped** to correct it.` / `…choose 'Mirrored' to correct this.` |

The Italian faithfully renders two *different* English strings: `Flipped` → `Capovolto` and
`Mirrored` → `Duplicato`, both glossary-locked (§8). The English page is the stale one — glossary
§8 already records `Mirrored` as *"superseded — EN pages now say 'Flipped'"*, but this EN page was
not updated. Fix on the EN side (`Mirrored` → `Flipped`), then re-translate the line in all five
languages.

### 1.5 Flip: "check the Screenmate's ports" vs. "check your laptop's ports"

| | |
|---|---|
| **File** | `it/manuals/flip/installation.mdx` |
| **IT** | `### Flip 14"` → `Controlla prima quali porte ha lo Screenmate.` / `### Flip 15,6"` → `Controlla prima quali porte ha il tuo laptop.` |
| **EN** | `First check which ports the Screenmate has.` / `First check which ports your laptop has.` |

Two parallel sections give the reader opposite instructions for two models of the same product.
Identical divergence in English.

### 1.6 "scegli tra due sorgenti" followed by three values

| | |
|---|---|
| **Files** | `it/manuals/flip/osd.mdx` · `it/manuals/expand/osd.mdx` |
| **IT** | `**Sorgente (SOURCE):** scegli tra due sorgenti del segnale: Type-C1 / Type-C2 e HDMI.` |
| **EN** | `**Source (SOURCE):** Pick from two signal sources: Type-C1 / Type-C2 and HDMI.` (flip) · `Choose between two signal sources: …` (expand) |

Announces two, lists three. Present in English; the Italian target is additionally locked in
glossary §7.3.

### 1.7 Dual Flip rotation limits: 245° range annotated "180°"

| | |
|---|---|
| **Files** | `it/manuals/dual-flip/index.mdx` · `it/manuals/flip/index.mdx` |
| **IT** | `Non ruotare gli schermi oltre l'angolo massimo indicato qui sotto.` + `**Schermo sinistro:** 0° – 245° (si inclina di 180° verso l'alto e verso il basso)` |
| **EN** | `Do not rotate the screens beyond the maximum angle shown below.` + `**Left screen:** 0° – 245° (tilts 180° up and down)` |

The parenthesis contradicts the range it annotates, and the instruction verb (`rotate` / `ruotare`)
differs from the spec verb (`tilts` / `si inclina`) three lines apart. Both are exactly as in
English. The 180° figure needs verification.

### 1.8 Panorama: "HDMI port" on a Mini-HDMI-only monitor

| | |
|---|---|
| **File** | `it/manuals/panorama/installation.mdx` |
| **IT** | `Sul monitor, collega il cavo HDMI alla porta HDMI accanto al cavo di alimentazione bianco.` |
| **EN** | `On the monitor, connect the HDMI cable to the HDMI port next to the white power cable.` |

`panorama/controls.mdx` documents `3 × Mini-HDMI` ports and the same paragraph calls the cable
`da Mini-HDMI a HDMI`, so the instruction sends the reader to the wrong end of the cable. Verbatim
from English.

### 1.9 Panorama viewing angle 360°

`it/manuals/panorama/index.mdx` — `| **Angolo di visione** | 360° |`, from EN `| **Viewing Angle** |
360° |`. Every sibling IPS panel in the range lists 178°. Spec-sheet question for the client.

---

## 2. Terminology and labelling drift that originates in English

### 2.1 `Gamma cromatica` vs `Precisione cromatica` in adjacent tabs

`it/manuals/flip/index.mdx` (14" tab vs 15,6" tab), `it/manuals/expand/index.mdx`,
`it/manuals/dual-flip/index.mdx`. The English tabs literally read `**Color Gamut** | 45% NTSC` and
`**Color Accuracy** | 45% NTSC` for the same row and the same value. Both Italian targets are
glossary-locked (§5.4). *Color accuracy* is the wrong term for NTSC coverage in English too — an
EN-side correction, after which the Italian follows automatically.

### 2.2 `≡` vs `M` for one physical button

`it/manuals/expand/controls.mdx` (`**≡ Pulsante Menu:**`) vs `it/manuals/expand/osd.mdx`
(`**M (Menu)**`). English has exactly the same split (`**≡ Menu button:**` / `**M (Menu)**`).

### 2.3 Byte-identical duplicated `Porta USB-C` bullets/headings

`it/manuals/flip/controls.mdx`, `it/manuals/expand/controls.mdx` (bullets) and
`it/manuals/dual-flip/controls.mdx` (two identical `### USB-C Port` headings, which also produce
colliding anchors). All duplicated the same way in English. Numbering or side-labelling them is an
EN-side edit.

### 2.4 Mount-hardware vocabulary (`staffa` / `supporto` / `sostegno` / `clip` / `cappuccio`)

Raised as Italian drift by both reviewers; on inspection the Italian maps EN 1:1 through the locked
glossary (§5.1): `bracket` → `staffa`, `stand` → `supporto`, `screen support` → `sostegno dello
schermo`, `protective cap` → `cappuccio protettivo`, `protective clips` → `clip protettive`. The
drift is English's:

- `en/manuals/expand/index.mdx` package contents says **`6x protective clips`** while
  `en/manuals/expand/installation.mdx` calls the same fitting the **`protective cap`** — and the
  Dutch original says `6x beschermkap` (*cap*) in both places, so English is the outlier.
- `en/manuals/infinity-lite/installation.mdx` uses `main stand`, `small support`, `screen support`,
  `the stand` and `display stand` across seven numbered steps.

Recommendation: settle the English part names first; the Italian glossary rows are already correct
and will follow.

### 2.5 Menu / button naming splits inside one product

| Files | EN split |
|---|---|
| `one-4k`, `one-4k-oled` `controls.mdx` vs `osd.mdx` | `Menu Button (Power / OSD)` vs `the power button` |
| `lite/controls.mdx` vs `lite-144hz/controls.mdx` | `OSD mode` vs `OSD menu mode` |
| `lite/controls.mdx` vs `lite/osd.mdx` | `on-screen settings menu (OSD)` vs `on-screen menu` |
| `onecable/controls.mdx` vs `onecable/troubleshooting.mdx` | `USB-C Port (Power only / Power Delivery)` vs `the Power USB-C port` |
| `infinity/controls.mdx` frontmatter vs its own H2 | `Ports and controls` vs `## Ports and Buttons` |

Each Italian page is faithful to its English page.

### 2.6 Speaker count: plural on the index, singular on controls

`it/manuals/infinity/index.mdx` `Ogni schermo ha altoparlanti integrati` vs
`it/manuals/infinity/controls.mdx` `Ogni schermo ha un altoparlante integrato sul bordo esterno`.
English: `Each screen has built-in speakers` / `Each screen has a built-in speaker`. Product fact.

### 2.7 Panorama `professionale` vs Infinity/Infinity Lite `aziendale` — **[SAFETY]**

Already recorded as observation **E1** in `safety-align-it.md` §8: `en/manuals/panorama/safety.mdx`
reads `home and **professional** use` where the other two read `home and **business** use`, and the
Dutch original is `zakelijk` (*business*) for all three. The Italian mirrors whichever EN variant it
was given. EN-side normalisation.

---

## 3. Prompts and sentences whose oddness is in the source

### 3.1 `Vuoi più spazio a schermo?` — retained on two pages

The meaning-inverting rendering was **fixed** where English reads `Need more overview?` (6
occurrences; see `fixlog-it.md`). It is **retained** on:

- `it/manuals/infinity/display-settings.mdx` — EN `**Want more on-screen space?**`
- `it/manuals/panorama/osd.mdx` — EN `**Need more room?**`

On those two pages the Italian is a faithful rendering of the English. That the English prompts
themselves sit badly with the answer they introduce (raising scaling to 150% yields *larger
elements and less usable space*) is an EN-source matter. Suggested EN fix: make all three prompts
one string, on the model of `Need more overview?`.

### 3.2 `## Ricarica dello Screenmate OneCable` heading over a reverse-charging section

`it/manuals/onecable/installation.mdx` — EN `## Charging the Screenmate OneCable`, NL
`## Opladen van de Screenmate OneCable`. The heading promises "charging the Screenmate"; the
section is about the Screenmate charging *the laptop*. Present in both source languages.

### 3.3 `l'altra estremità` (singular) for two cables

`it/manuals/onecable/installation.mdx` — EN `before connecting the other end to the Screenmate`,
NL `voordat je het andere uiteinde op de Screenmate aansluit`. Both sources are singular.

### 3.4 `alimentatore` vs `caricabatterie` for the 45 W adapter

`it/manuals/onecable/installation.mdx` — `Nota: usa un alimentatore da almeno 45 W. Non hai un
caricabatterie USB-C? Usa un alimentatore adatto.` EN: `Note: Use a power adapter of at least 45W.
No USB-C charger? Use a suitable power adapter.` NL: `netstroom-adapter` / `USB-C-lader` /
`netstroom-oplader`. The apparent circularity is the source's; the two Italian words are the
glossary-locked targets of two distinct English words (`power adapter` → `alimentatore`,
`charger` → `caricabatterie`, §5.1). Collapsing them in Italian only would misrepresent the source
and break the glossary.

### 3.5 `Per un funzionamento a basso consumo, ti consigliamo di scollegare…`

`it/manuals/{onecable,flip,expand,dual-flip}/index.mdx` — EN `For energy-efficient operation, we
recommend disconnecting the power cable when the monitor is not in use.` Unplugging is not an
*operation* in either language; the Italian phrase is itself idiomatic.

### 3.6 `regola la luminosità del valore RGB rosso`

`it/manuals/lite/osd.mdx`, `it/manuals/lite-144hz/osd.mdx` — EN `Adjust the brightness of the red
RGB value.` A *value* has no brightness in English either. `en/manuals/expand/osd.mdx` words the
same control correctly as `Adjust the red channel` (and the Italian there correctly reads `regola
il canale rosso`), so the EN Lite pages should adopt the Expand wording.

### 3.7 `Temperatura colore: … per regolare l'intensità cromatica complessiva`

`it/manuals/lite/osd.mdx`, `it/manuals/lite-144hz/osd.mdx` — EN `Choose User, Warm, or Cool to
adjust the overall color intensity.` Colour temperature changes tint, not intensity, in the English
too.

### 3.8 Lite: the wheel powers on, the "power button" opens the OSD

`it/manuals/lite/controls.mdx`, `it/manuals/lite-144hz/controls.mdx` — EN `### Scroll Wheel` →
`Short press: turn the device on`; `### Power & Return Button` → `Press to open the on-screen
settings menu (OSD)`. Source labelling; renaming the button in Italian only would make the Italian
manual disagree with the English one and possibly with the hardware.

### 3.9 One 4K: "your device supports charging" → "lo schermo si ricarica"

`it/manuals/one-4k/installation.mdx`, `it/manuals/one-4k-oled/installation.mdx` — EN `If your
device supports charging over USB-C, the screen automatically charges as soon as the charger is
connected to the Screenmate.` The subject switch mid-sentence, and the implication that the
(battery-less) monitor charges, are both in the English.

### 3.10 `Passa alla modalità di collegamento corretta` / `modalità telefono`

`it/manuals/infinity-lite/installation.mdx` — EN `Switch to the correct connection mode (external
power required) to use the Screenmate with a phone, game console or other USB-C device. Phone mode
also requires external power.` The external-power requirement is stated twice, "phone mode" is
never defined, and no switching instructions are given — all as in English.

### 3.11 `entrambi gli schermi` on a single-screen product

`it/manuals/infinity-lite/installation.mdx` — EN `…to safely deploy both extension screens behind
your laptop`, `### 6. Open the screens`, `### 7. Close the screens`. The English page carries the
plural, apparently left over from the two-screen Infinity.

### 3.12 `(l'altro schermo compare come **S6-R**)` on a single-screen product

`it/manuals/infinity-lite/display-settings.mdx` — EN `(the other screen appears as **S6-R**)`.

### 3.13 `### Porta USB-A` with an empty body

`it/manuals/one-4k-oled/controls.mdx` line 37 — the heading is followed only by
`{/* TODO: confirm with Louie — USB-A port use … */}`. The English page is byte-identical, comment
included. Structural parity forbids dropping the heading on the Italian side only; the fix is to
resolve the TODO on the English page.

### 3.14 Duplicated purpose clause with two nouns for one object

`it/manuals/infinity-lite/installation.mdx` — EN `Follow the correct sequence when opening and
closing to avoid damage to the device. Store your Screenmate carefully to prevent damage to the
equipment.`

### 3.15 Resolution spacing `1920 × 1080` vs `1920×1080` in adjacent tabs

`it/manuals/expand/index.mdx`, `it/manuals/one-4k/index.mdx`, `it/manuals/infinity/index.mdx`,
`it/manuals/panorama/index.mdx`. The English tables have exactly the same spaced/unspaced split;
the Italian mirrors it row for row. A typography sweep on the EN spec tables would propagate.

### 3.16 Callout formatting: bare `Nota:` paragraphs vs `<Note>` callouts

`it/manuals/onecable/installation.mdx` (lines 24, 34, 62) and `it/manuals/one-4k/installation.mdx`.
The English pages put the same asides in bare paragraphs on those pages and in `<Note>` blocks
elsewhere. Structural parity: the Italian cannot wrap them without diverging from EN.

### 3.17 EN `'Flipped'` glossed asymmetrically inside one sentence

Recorded as observation **E2** in `safety-align-it.md` §8:
`en/manuals/onecable/display-settings.mdx` glosses `Display orientation` with its Dutch original but
gives `'Flipped'` with no gloss, which is what leaves the translated pages without a pattern to
follow. EN-side normalisation.

---

## 4. Not defects — recorded so a future reviewer does not "correct" them

- **Ventilation-opening polarity.** `Keep ventilation openings clear` → `Non ostruire le aperture di
  ventilazione`. Truth-conditionally equivalent, glossary-locked (§6), and the literal rendering
  (`Tieni le aperture … chiare`) is explicitly rejected there. **[SAFETY]**
- **`### Attenzione durante la chiusura`.** Glossary-locked (§9) and closer to the Dutch source
  heading `Let op bij inklappen` than the broadened English `### Folding caution` is; the body line
  beneath restores full scope. **[SAFETY]**
- **`Only use the device with a 5V power source…` scope.** Observation **E3** in
  `safety-align-it.md`: sentence-initial English `only` is scopally ambiguous; the Italian
  `esclusivamente` placement is unambiguous and correct. Do not loosen it toward the English.
  **[SAFETY]**
- **macOS steps given as bare Italian labels** (`Apri Impostazioni di Sistema`, `Vai su Schermi`,
  `Fai clic su Disposizione`) while the Windows half uses `English UI string ('Italian gloss')`.
  The English page uses exactly the same two conventions in the same two halves, and every label is
  glossary-locked (§8).
- **Italian number and unit formatting** (`1000:1`, `1820 grammi`, `100% sRGB`, `45 W`, `-20 °C`,
  `15,6"`). Locked in glossary §4; reviewer B independently verified the corpus as correct and
  consistent. The `1.000:1` / `1.820 g` / `100 %` suggestions in `fluency-it-a.md` would break §4.3
  and §4.1.
