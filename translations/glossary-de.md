# Screenmate EN→DE Glossary (locked)

Locked terminology and formatting for all Screenmate German copy. These renderings are
binding: use them exactly, unless the English term is intentionally retained
(column "Keep EN?" = ✓).

Source of truth for the term inventory: the full EN corpus (`en/manuals/**/*.mdx`,
`en/manuals-index.mdx`), read in full for this glossary. "Keep EN?" is seeded from
`translations/dnt.json` — all 42 DNT entries are marked ✓ below (aligned to the
post-`Drivers`→`DRIVERS` / `+DisplayPort` revision of that file).

Structure mirrors `.claude/skills/screenmate-dutch-fidelity/references/glossary.md`;
the rules are German, not translated Dutch.

**Format:**
| English | German (locked) | Notes / variants | Keep EN? |
|---|---|---|---|

---

## 0. The five rules that break most often

Read these first. Everything else in this file is detail.

1. **Informal `du` / `dein`, always lowercase.** Never `Sie`, `Ihnen`, `Ihr`, `Ihre`.
   See §2.
2. **Durchkopplung.** Acronym or English term + German noun = hyphenate *every*
   junction: `USB-C-Kabel`, `USB-C-Anschluss`, `3,5-mm-Klinkenanschluss`. Never a bare
   space (`USB C Kabel`, `USB-C Kabel` are both defects). See §3.
3. **The three-part cable chain is `X-auf-Y-Kabel`.** `USB-C to USB-C cable` →
   **`USB-C-auf-USB-C-Kabel`**. Never `zu`, never `–`, never a space. See §3.3.
4. **`der Screenmate`** — masculine, in every product variant. `den Screenmate`,
   `dem Screenmate`. See §1.0.
5. **The device is in English.** Every ALL-CAPS OSD label, every on-device menu *value*,
   stays verbatim English. OSD *headings*, by contrast, are translated. See §6.

---

## 1. Product & hardware

### 1.0 Gender — locked

German needs a decision the English source never had to make. It is made here; do not
re-litigate it per page.

| Noun | Article | Locked forms |
|---|---|---|
| Screenmate (all products) | **der** | `der Screenmate`, `den Screenmate`, `dem Screenmate`, `des Screenmate` |
| Screenmate OneCable / Flip / Dual Flip / Expand / Infinity / Infinity Lite / Lite / Lite 144 Hz / One 4K / One 4K OLED / Panorama | **der** | `der Screenmate Infinity Lite` (even though it is a "display extension", not a monitor) |
| Bildschirm | der | `den Bildschirm`, `dem Bildschirm` |
| Display | das | `das Display`, plural `die Displays` |
| Monitor | der | `den Monitor` |
| Laptop | der | `der Laptop` (never `das Laptop` — pick one, this is it) |
| Kabel | das | `das Kabel`, plural `die Kabel` |
| Anschluss | der | plural `die Anschlüsse` |
| Taste | die | plural `die Tasten` |
| Netzteil | das | — |
| Ständer | der | — |
| Halterung | die | — |
| Treiber | der | plural `die Treiber` |
| Menü | das | `das OSD-Menü` |
| OSD | das | `das OSD` |
| Stick | der | `der USB-Stick` |
| Helligkeit / Lautstärke / Auflösung / Schutzhülle | die | — |

### 1.1 Core hardware

| English | German | Notes | Keep EN? |
|---|---|---|---|
| Screenmate | Screenmate | brand, never inflected internally | ✓ |
| screen | Bildschirm | `der Bildschirm`, pl. `die Bildschirme` | — |
| display (the panel as a device) | Display | `das Display`; use when the EN means the physical panel/unit | — |
| displays (multiple monitors, OS context) | Bildschirme | in OS instructions ("arrange the displays") use `Bildschirme` | — |
| monitor | Monitor | — | — |
| portable monitor | tragbarer Monitor | — | — |
| display extension | Bildschirmerweiterung | Infinity Lite product description | — |
| triple-screen portable monitor | tragbarer Monitor mit drei Bildschirmen | not `Dreifach-Bildschirm-Monitor` | — |
| foldable dual-screen extension | faltbare Doppelbildschirm-Erweiterung | Dual Flip | — |
| multi-screen monitor | Multiscreen-Monitor | Flip | — |
| laptop | Laptop | — | — |
| MacBook | MacBook | — | ✓ |
| PC | PC | — | ✓ |
| phone / smartphone | Smartphone | never `Telefon`, never `Handy` in body copy | — |
| tablet | Tablet | — | — |
| game console | Spielkonsole | pl. `Spielkonsolen` | — |
| Nintendo Switch / PlayStation / Xbox | Nintendo Switch / PlayStation / Xbox | device names | ✓ |
| Nintendo Charging Dock | Nintendo Charging Dock | product name | ✓ |
| switch dock | Switch-Dock | — | — |
| cable | Kabel | see §3 for every compound | — |
| port | **Anschluss** | locked over `Port`. `USB-C-Anschluss`, not `USB-C-Port` | — |
| connector | Anschluss | "a USB-C connector with video output" → `ein USB-C-Anschluss mit Videoausgang` | — |
| plug (noun, on a cable end) | Stecker | "the black USB-A plug" → `der schwarze USB-A-Stecker` | — |
| button | **Taste** | locked over `Knopf`/`Button`. pl. `Tasten` | — |
| control buttons | Bedientasten | heading "Control Buttons" | — |
| multifunctional button | Multifunktionstaste | Infinity's rotatable button | — |
| menu button | Menütaste | `M – OSD-Menütaste` | — |
| power button | Power-Taste | locked; not `Ein-/Ausschalter` (device is labelled "Power") | — |
| scroll wheel | Scrollrad | — | — |
| brightness | Helligkeit | — | — |
| contrast | Kontrast | — | — |
| volume | Lautstärke | — | — |
| sharpness | Schärfe | body prose only; the OSD label stays `SHARPNESS` | — |
| speaker (device part) | Lautsprecher | "built-in speaker" → `integrierter Lautsprecher` | — |
| headphones | Kopfhörer | — | — |
| external speakers | externe Lautsprecher | — | — |
| headphone jack (3.5 mm) | 3,5-mm-Klinkenanschluss | note comma decimal + full Durchkopplung | — |
| indicator light | Statusanzeige | heading "Indicator Light" | — |
| LED indicator | LED-Anzeige | heading "LED Indicator" | — |
| motherboard indicator light | Kontrollleuchte der Hauptplatine | FAQ only | — |
| protective case | Schutzhülle | — | — |
| protective sleeve | Schutzhülle | **same word** — EN uses both, DE uses one | — |
| protective cap | Schutzkappe | Expand | — |
| protective clips | Schutzclips | Expand, `6× Schutzclips` | — |
| protective film | Schutzfolie | safety step 1 | — |
| leather carry pouch | Leder-Tragetasche | hyphen for legibility (Duden-permitted Gliederungsbindestrich) | — |
| cable organizer | Kabelhalter | Expand package contents | — |
| USB stick | USB-Stick | — | — |
| power adapter | **Netzteil** | locked over `Netzadapter`/`Stromadapter`. `65-W-Netzteil` | — |
| AC/DC adapter | AC/DC-Netzteil | safety text | — |
| charger | Ladegerät | `PD-Ladegerät`, `USB-C-Ladegerät` | — |
| laptop charger | Laptop-Ladegerät | — | — |
| video adapter | Videoadapter | Infinity package contents | — |
| hub | Hub | `USB-C-Hub`, `HDMI-Hub` | ✓ |
| adapter | Adapter | — | — |
| stand | Ständer | `der Ständer` | — |
| adjustable stand | verstellbarer Ständer | — | — |
| screen stand | Bildschirmständer | Infinity Lite package contents | — |
| single screen stand | Ständer für einen Bildschirm | do not build `Einzelbildschirmständer` | — |
| display stand | Bildschirmständer | — | — |
| built-in stand | integrierter Ständer | spec field "Special Features" | — |
| bracket | Halterung | Expand clips onto the laptop lid | — |
| rotatable mount | drehbare Halterung | — | — |
| screen support | Bildschirmhalterung | Infinity Lite step 3 | — |
| main stand | Hauptständer | Infinity Lite step 2 | — |
| movable arm | beweglicher Arm | Infinity dual-screen setup | — |
| frame | Rahmen | Infinity Lite step 4 | — |
| locking legs | Verriegelungsfüße | Panorama step 2 | — |
| front lock | vordere Verriegelung | Panorama step 3 | — |
| stability rubbers | Stabilisierungsgummis | Infinity, `8× Stabilisierungsgummis` | — |
| magnet | Magnet | Infinity Lite package contents | — |
| silicone strip | Silikonstreifen | Infinity storage | — |
| groove | Aussparung | Infinity storage | — |
| centre piece | Mittelstück | Infinity setup | — |
| mouse | Maus | — | — |
| keyboard | Tastatur | — | — |
| accessories | Zubehör | `USB-2.0-Zubehör` | — |
| packaging | Verpackung | — | — |
| desk | Schreibtisch | — | — |
| flat surface | ebene Fläche | — | — |

### 1.2 Product names — never translated, never re-spaced

All product names come from `dnt.json` and are used verbatim. Size suffixes take the
German decimal comma (§4).

The inch mark below is shown in its **markdown** form. In a `<Tab title="…">` it must be
written `&quot;` and in frontmatter `\"` — **see §4.1 before pasting these anywhere.**

| English | German | Keep EN? |
|---|---|---|
| Screenmate | Screenmate | ✓ |
| OneCable | OneCable | ✓ |
| Lite 144 (Hz) | Lite 144 Hz | ✓ |
| Dual Flip | Dual Flip | ✓ |
| Flip | Flip | ✓ |
| Expand | Expand | ✓ |
| Infinity | Infinity | ✓ |
| Infinity Lite | Infinity Lite | ✓ |
| One 4K | One 4K | ✓ |
| One 4K OLED | One 4K OLED | ✓ |
| Panorama | Panorama | ✓ |
| Flip 15.6" | Flip 15,6" | ✓ (comma is the only change) |
| Expand 14" | Expand 14" | ✓ |
| Dual Flip 16" | Dual Flip 16" | ✓ |

---

## 2. Register — informal `du`, lowercase

**Rule:** always the informal second person singular: `du`, `dich`, `dir`, `dein`,
`deine`, `deinem`, `deinen`. **Never** `Sie`, `Ihnen`, `Ihr`, `Ihre`, `Ihrem`, `Ihren`,
`Ihres`.

**Rule (German-specific):** write `du` and `dein` **lowercase** in running text
(post-1996 Duden). `Du`/`Dein` capitalised is a defect except at the start of a sentence.

### 2.1 Five example pairs

| Wrong (formal) | Right (informal) |
|---|---|
| Verbinden **Sie Ihren** Laptop über ein USB-C-Kabel mit dem Screenmate. | Verbinde **deinen** Laptop über ein USB-C-Kabel mit dem Screenmate. |
| Bitte lesen **Sie** die folgenden Hinweise, bevor **Sie** den Monitor verwenden. | Lies die folgenden Hinweise, bevor **du** den Monitor verwendest. |
| Stellen **Sie** sicher, dass **Ihr** Laptop genug Strom liefert. | Achte darauf, dass **dein** Laptop genug Strom liefert. |
| Möchten **Sie Ihre** Arbeitsfläche erweitern? | Möchtest **du deine** Arbeitsfläche erweitern? |
| **Ihr** Laptop wird jetzt über den Screenmate geladen. | **Dein** Laptop wird jetzt über den Screenmate geladen. |

### 2.2 Defect search patterns

Any hit is a defect (check case-sensitively):

```
\bSie\b        \bIhnen\b       \bIhr\b        \bIhre\b       \bIhrem\b
\bIhren\b      \bIhrer\b       \bIhres\b      \bIhrigen\b    \bBitte\b
```

**Edge case — sentence-initial `Sie`.** A sentence beginning with `Sie` is ambiguous
(formal "you" vs. "they/she"). Do not try to disambiguate: rewrite the sentence so it
does not start with a pronoun. Same for a sentence-initial `Ihr`.

**Edge case — lowercase `sie`/`ihr` are fine.** `sie` = they/she, `ihr` = her/their.
Only the capitalised forms mid-sentence are defects. Do not blind-replace.

**Edge case — regulatory / safety text.** If a source line is verbatim regulatory
wording that uses `Sie`, do **not** silently convert it. Flag it for the user to decide.
(The Screenmate safety pages are house-written, not regulatory boilerplate, so they
take `du` like everything else.)

**Edge case — `Bitte`.** German instructions in this house style drop it, exactly as
Dutch drops "alstublieft". `Please read the following guidelines` →
`Lies die folgenden Hinweise` — not `Bitte lies …`.

### 2.3 Imperatives

Numbered steps use the **imperative singular** (`du`-form, no pronoun):
`Verbinde`, `Öffne`, `Drücke`, `Klicke`, `Wähle`, `Entferne`, `Lege`, `Starte`, `Halte`.

| Wrong | Right |
|---|---|
| Du verbindest den Screenmate mit deinem Laptop. | Verbinde den Screenmate mit deinem Laptop. |
| Bitte entfernen Sie die Schutzfolie. | Entferne die Schutzfolie. |
| Anschließe das Kabel an den Laptop. | **Schließe** das Kabel an den Laptop **an**. |
| Neustarte deinen Laptop. | **Starte** deinen Laptop **neu**. |
| Aufklappe die beiden Bildschirme. | **Klappe** die beiden Bildschirme **auf**. |

**Separable verbs split in the imperative.** The prefix goes to the end of the clause:
`anschließen` → `Schließe … an`; `aufklappen` → `Klappe … auf`;
`einstecken` → `Stecke … ein`; `neu starten` → `Starte … neu`;
`herunterladen` → `Lade … herunter`; `ausklappen` → `Klappe … aus`.

**Imperative -e ending.** Prefer the full form (`Verbinde`, `Klicke`, `Drücke`,
`Öffne`, `Wähle`) over the clipped form (`Verbind`, `Klick`). Verbs with a stem change
keep the changed stem and take no -e: `Lies` (not `Lese`), `Nimm` (not `Nehme`),
`Sieh` (not `Sehe`).

---

## 3. Compounds & hyphenation (Durchkopplung)

German writes compounds closed. When a compound contains an acronym, a product name, a
number+unit, or an English loan element, **every junction gets a hyphen** — this is
*Durchkopplung* and it is the single highest-frequency error site in German technical
copy.

### 3.1 Acronym / loanword + German noun

| Wrong | Right |
|---|---|
| USB C Kabel, USB-C Kabel, USBC-Kabel | **USB-C-Kabel** |
| USB C Anschluss, USB-C Anschluss | **USB-C-Anschluss** |
| USB A Anschluss | **USB-A-Anschluss** |
| USB Stick, USB Speicherstick | **USB-Stick** |
| HDMI Kabel, HDMI-kabel | **HDMI-Kabel** |
| HDMI Anschluss | **HDMI-Anschluss** |
| Mini HDMI Anschluss, Mini-HDMI Anschluss | **Mini-HDMI-Anschluss** |
| OSD Menü, OSD Menu | **OSD-Menü** |
| OSD Timer (in prose) | **OSD-Timer** (the device label stays `OSD TIMER`) |
| LED Anzeige | **LED-Anzeige** |
| PD Ladegerät | **PD-Ladegerät** |
| Power Delivery Anschluss | **Power-Delivery-Anschluss** |
| Windows Version | **Windows-Version** |
| Mac OS Version, macOS Version | **macOS-Version** |
| Switch Dock | **Switch-Dock** |
| Standby Modus | **Standby-Modus** |
| Display Treiber, Displaytreiber | **Displaytreiber** (all-German compound — closed, no hyphen) |

**Rule of thumb:** if any element of the compound is an acronym, a Latin-letter brand,
or an English word, hyphenate every junction. If every element is an ordinary German
noun, close the compound with no hyphen (`Bildschirmständer`, `Helligkeitstasten`,
`Stromversorgung`, `Installationsschritte`, `Multifunktionstaste`).

### 3.2 Number + unit + noun

The number, the unit and the noun are all coupled. The space that separates a number
from its unit *in isolation* (§4) disappears inside a compound, replaced by hyphens.

| Standalone (spaced) | Inside a compound (coupled) |
|---|---|
| `65 W` | **`65-W-Netzteil`** |
| `45 W` | **`45-W-Ladegerät`** |
| `3,5 mm` | **`3,5-mm-Klinkenanschluss`** |
| `5 V` | **`5-V-Stromquelle`** |
| `5 V/2 A` | **`5-V/2-A-Netzteil`** |
| `144 Hz` | **`144-Hz-Bildschirm`** (but the product name stays `Lite 144 Hz`) |
| `15,6 Zoll` | **`15,6-Zoll-Bildschirm`** |
| `2,0` | **`USB-2.0-Zubehör`** |

Wrong: `65W Netzteil`, `65 W Netzteil`, `65W-Netzteil`, `3,5mm Klinkenanschluss`.

### 3.3 The three-part cable chain — LOCKED

This is the construction the Dutch pass got inconsistent on. There is exactly one
correct German form and no permitted variants.

**`<A> to <B> cable` → `<A>-auf-<B>-Kabel`**

| English | German (locked) |
|---|---|
| USB-C to USB-C cable | **USB-C-auf-USB-C-Kabel** |
| USB-C to USB-A cable | **USB-C-auf-USB-A-Kabel** |
| USB-A to USB-C cable | **USB-A-auf-USB-C-Kabel** |
| HDMI to USB-C cable | **HDMI-auf-USB-C-Kabel** |
| Mini HDMI to HDMI cable | **Mini-HDMI-auf-HDMI-Kabel** |
| USB-A > USB-C Cable *(arrow form in package lists)* | **USB-A-auf-USB-C-Kabel** |
| USB-C > USB-C Cable | **USB-C-auf-USB-C-Kabel** |
| USB-C to USB-C charging cable | **USB-C-auf-USB-C-Ladekabel** |
| USB-C with USB-A adapter (cable) | **USB-C-Kabel mit USB-A-Adapter** *(not a chain — the adapter is a separate part)* |

Rejected variants — **do not use any of these**:

- `USB-C zu USB-C Kabel` (missing hyphens, and `zu` is not the locked connector)
- `USB-C-zu-USB-C-Kabel` (`auf` is locked, not `zu`)
- `USB-C auf USB-C Kabel` (spaces instead of hyphens)
- `USB-C-USB-C-Kabel` (drops the connector word — ambiguous)
- `USB-C → USB-C-Kabel` / `USB-C > USB-C-Kabel` (arrows are EN source formatting only)
- `Kabel von USB-C auf USB-C` (paraphrase; breaks the locked noun phrase)

**Directionality is preserved.** `USB-A to USB-C` and `USB-C to USB-A` are different
cables in this corpus (Infinity ships `USB-A-auf-USB-C-Kabel`; Lite uses a
`USB-C-auf-USB-A-Kabel` for power). Never normalise one into the other.

**Plural.** `Kabel` is invariant: `zwei USB-C-auf-USB-C-Kabel`,
`2× Mini-HDMI-auf-HDMI-Kabel`.

**Inside a longer phrase**, the chain stays intact:
`Schließe das 65-W-Netzteil mit dem mitgelieferten USB-C-auf-USB-C-Kabel an den
USB-C-Ladeanschluss des Monitors an.`

### 3.4 Brand / product name + German noun

| Case | Rule | Example |
|---|---|---|
| Single-token brand + German noun | couple with a hyphen | `Screenmate-Handbuch`, `Screenmate-Produkte`, `Screenmate-Handbücher` |
| Multi-token product designation + German noun | **do not** couple — use an appositive with an en dash | `Screenmate OneCable – Handbuch`, `Screenmate One 4K OLED – Handbuch` |

Rationale: `Screenmate-One-4K-OLED-Handbuch` is technically correct Durchkopplung and
completely unreadable; the appositive keeps the trademark intact. Rejected:
`Screenmate OneCable Handbuch` (Deppenleerzeichen — a real error, not a style choice).

### 3.5 Suspended hyphens (Ergänzungsstrich)

When two compounds share a tail, suspend the first: `Anzeige- und Toneinstellungen`,
`Bildschirm- & Systemaudioaufnahme`, `Menü-/Auswahl-/Bestätigungstaste`,
`Ein- und Ausklappen`. The suspension hyphen is mandatory — `Anzeige und
Toneinstellungen` is a defect.

### 3.6 Punctuation & quotes

- **Quotation marks:** German typographic quotes `„…“` for quoted UI strings and
  labels. `Klicke auf „Öffnen“.` Not `'Öffnen'`, not `"Öffnen"`, not `»Öffnen«`.
  (This is a deliberate divergence from the Dutch pages, which lock ASCII `'…'`.)
- **Dashes:** use the en dash `–` with spaces for parenthetical interruptions and in
  ranges. **Never** the em dash `—` in German body copy. EN headings such as
  `Option 2 — USB-A + HDMI` become `Option 2 – USB-A + HDMI`.
- **Ranges:** `0 – 100`, `10 – 60 Sekunden`, `−20 °C bis 60 °C`. In OSD value ranges
  copied verbatim from the device, keep the source form `(0–100)`, `(0–4)`.
- **Minus sign:** the button is `−` (U+2212, as in the EN source), not the hyphen `-`.
  Keep the source character.
- **`×` for multiplication and counts:** `2× USB-C`, `1920 × 1080`, `39 × 24 × 2,5 cm`.
  Not `2x`, not `2 x`.
- **No double space** after a full stop.
- **ß vs ss:** standard German orthography (`Anschluss`, `groß`, `schließen`,
  `Straße`). Do not use Swiss `ss` spellings.
- **Umlauts are never transliterated:** `Menü`, not `Menue`; `Größe`, not `Groesse`.

### 3.7 Headings — sentence case

EN uses title case; German uses sentence case (only the first word and nouns are
capitalised, and German capitalises all nouns anyway).

EN: `Driver Installation for Windows` → DE: `Treiberinstallation für Windows`
EN: `Choose Your Cables` → DE: `Die richtigen Kabel wählen`

---

## 4. Number formatting

| Type | Format | Example |
|---|---|---|
| Decimal separator | **comma** | `2,5 cm`, `15,6"`, `3,5 mm`, `34,5 × 22,1 × 1,1 cm` |
| Thousands (4 digits) | **no separator** | `1820 Gramm`, `1920 × 1080`, `2560 × 1600`, `3840 × 2160` |
| Thousands (5+ digits) | period | `100.000:1` (One 4K OLED contrast ratio) — see flag in §9 |
| Number + unit | **space** (DIN 5008) | `60 Hz`, `144 Hz`, `25 ms`, `350 cd/m²`, `1820 Gramm`, `65 W`, `45 W`, `5 V`, `2 A` |
| Number + unit inside a compound | hyphens, no space | `65-W-Netzteil` (§3.2) |
| Percent | **space** | `100 % sRGB`, `72 % NTSC`, `150 %` |
| Degrees (angle) | **no space** | `178°`, `360°`, `0° – 245°`, `180°` |
| Degrees (temperature) | **space before °C** | `−20 °C`, `60 °C` |
| Inches | comma + inch mark | `15,6"`, `14"`, `16"` — do **not** expand to `Zoll`. **The quote character is context-dependent — see §4.1** |
| Resolution | `×` with spaces | `1920 × 1080`, `2560 × 1600` |
| Dimensions | `×` with spaces, comma decimals | `39 × 24 × 2,5 cm`, `40,6 × 23,7 × 2,5 cm` |
| Ratios | colon, no spaces | `1000:1`, `16:9`, `16:10`, `4:3` |
| Voltage / amperage pair | `5 V/2 A`, `5 V/3 A` | space before each unit, slash unspaced |
| Range with units | unit once, at the end | `zwischen 5 V und 20 V`, `10 – 60 Sekunden` |
| Tolerance | `±2 V` | no space after `±` |
| Weight | `Gramm` spelled out | `1820 Gramm`, `609 Gramm` — matches EN "grams" |
| Counts / quantities | `2×`, `3×`, `6×`, `8×` | `2× USB-C-auf-USB-C-Kabel`, `6× Schutzclips` |
| Ordinals | period after digit | `der 3. Anschluss`, `zum 1. Mal` |

### 4.1 The inch mark — PARSE HAZARD, three contexts

Changing `15.6` to `15,6` is safe everywhere. **Changing the quote character is not.**
The inch mark takes a different form in each of the three places it appears, and getting
it wrong breaks the MDX build rather than just looking wrong.

| Context | Form | Example (source, as it must be written) |
|---|---|---|
| **JSX attribute** — `<Tab title="…">` | **`&quot;`** | `<Tab title="Flip 15,6&quot;" icon="display">` |
| **Frontmatter** — YAML double-quoted `description:` | **`\"`** | `description: "… erhältlich in 14\" und 15,6\""` |
| **Markdown** — headings, prose, spec-table cells | **literal `"`** | `### Flip 15,6"` |

**Why this matters:** a translator who copies the markdown form `Flip 15,6"` into a
`<Tab title="…">` closes the JSX attribute early and the page fails to build. The same
paste into frontmatter terminates the YAML string early.

**Rule:** carry over whatever escape the EN source already uses at that spot and change
only the decimal separator. The EN corpus is already correct in all three contexts —
`<Tab title="Flip 15.6&quot;">`, `description: "… 15.6\" …"`, `### Flip 15.6"` — so the
edit is always `15.6` → `15,6` and nothing else.

NL ships exactly this three-way split, which confirms it:
`<Tab title="Flip 15,6&quot;">` / `description: "… 14\" en 15,6\""` / `### Flip 15,6"`.

**One NL defect not to copy:** `nl/manuals/panorama/index.mdx` left its frontmatter at
`Panorama 15.6\"` (period) while `flip` correctly uses `15,6\"`. German applies the comma
in **all** products, frontmatter included.

**Note on the unit space.** German (DIN 5008 / SI) requires a space between numeral and
unit symbol — including for `W`, `V`, `A`, `%` and `°C`, where the EN source writes them
closed (`45W`, `5V/2A`, `100%`, `-20°C`). This is a deliberate divergence from the Dutch
glossary, which locked the closed forms. Angles (`178°`) keep no space in both.

**Note on the minus sign in temperatures.** Use the typographic minus `−20 °C`
(U+2212), matching the `−` button glyph used throughout the corpus.

---

## 5. Connections, power & software

| English | German | Notes | Keep EN? |
|---|---|---|---|
| USB-C | USB-C | never `USB C`, never `USBC` | ✓ |
| USB-A | USB-A | — | ✓ |
| USB 2.0 | USB 2.0 | `USB-2.0-Zubehör` when compounded | ✓ |
| HDMI | HDMI | — | ✓ |
| Mini-HDMI / Mini HDMI | **Mini-HDMI** | EN is inconsistent (`Mini HDMI` / `Mini-HDMI`); DE always hyphenates, per `dnt.json` | ✓ |
| Power Delivery (PD) | Power Delivery (PD) | brand term; compounds as `Power-Delivery-Anschluss` | ✓ |
| DisplayPort Alt Mode | DisplayPort Alt Mode | spec term | ✓ |
| DP (monitor label) | DP | Panorama "left screen (DP monitor)" → `linker Bildschirm (DP-Monitor)` | ✓ |
| reverse charging | Reverse Charging | keep EN, capitalised as a German noun; gloss once on first use as `umgekehrtes Laden` if the sentence needs it | ✓ |
| Type-C1 / Type-C2 | Type-C1 / Type-C2 | on-device SOURCE values | ✓ |
| power (electricity) | Strom | `genug Strom liefern` | — |
| power supply (the function) | Stromversorgung | `zusätzliche Stromversorgung` | — |
| power source | Stromquelle | `externe Stromquelle` | — |
| external power supply | externe Stromversorgung | — | — |
| output power | Ausgangsleistung | `eine Ausgangsleistung von mehr als 10 W` | — |
| power input / DC input | DC-Eingang | safety text: `Der DC-Eingang liegt zwischen 5 V und 20 V` | — |
| dedicated power input | dedizierter Stromeingang | One 4K controls | — |
| power outlet / wall outlet | Steckdose | — | — |
| power cable | Netzkabel | "disconnect the power cable" → `das Netzkabel abziehen` | — |
| charging port | Ladeanschluss | `USB-C-Ladeanschluss` | — |
| to charge | laden | `Dein Laptop wird geladen` | — |
| fast-charge mode | Schnellladefunktion | One 4K "switches to fast-charge mode" | — |
| grounded | geerdet | safety | — |
| amperage | Stromstärke | safety | — |
| connection | Anschluss / Verbindung | `Anschluss` for the physical link, `Verbindung` for the established link | — |
| connection cable | Verbindungskabel | FAQ | — |
| to connect | anschließen | `Schließe … an`; use `verbinden` for "connect A with B" | — |
| to disconnect | trennen | `Trenne den Screenmate von deinem Laptop` | — |
| to plug in | einstecken | `Stecke das Kabel in den Anschluss` | — |
| signal | Signal | `das Signal` | — |
| video signal | Videosignal | — | — |
| signal source | Signalquelle | `drei Signalquellen` | — |
| input source | Eingangsquelle | "select the correct input source" | — |
| video output | Videoausgang | `Videoausgang über USB-C` | — |
| video transfer / transmission | Videoübertragung | Flip/Expand/Dual Flip port lists | — |
| data | Daten | `Daten/Video/Strom` | — |
| output device | Ausgabegerät | Windows/macOS sound settings | — |
| pass-through | Durchschleifen | rare; check context | — |
| driver | **Treiber** | default in body copy; `der Treiber` | — |
| DRIVERS (volume name) | DRIVERS | the literal USB-stick volume label, `DRIVERS (D:)`. This — not the English word "drivers" — is the invariant | ✓ |
| DisplayPort | DisplayPort | interface name; `DisplayPort Alt Mode`, `S6-R (DisplayPort)` | ✓ |
| display driver | Displaytreiber | Panorama | — |
| to download | herunterladen | `Lade den Treiber herunter` | — |
| download (noun) | Download | `die Download-Seite` | — |
| to install / installation | installieren / Installation | — | — |
| manual installation | manuelle Installation | — | — |
| installer | Installationsprogramm | `Doppelklicke auf das Installationsprogramm` | — |
| to restart | neu starten | `Starte deinen Laptop neu` — never `restarten`/`neustarten` as one word in the imperative | — |
| operating system | Betriebssystem | — | — |
| software | Software | — | — |
| archive / to unzip | Archiv / entpacken | Panorama driver step | — |
| update | Update / aktualisieren | — | — |
| toggle (noun, macOS switch) | Schalter | `Aktiviere den Schalter neben „UsbDisplay“` | — |
| password | Passwort | — | — |
| menu bar | Menüleiste | macOS FAQ | — |
| taskbar | Taskleiste | Windows sound settings | — |
| Launchpad | Launchpad | macOS feature name | ✓ |
| UsbDisplay / RacerUSB / RacerDisplayDriver-2024.9.13-en | verbatim | app and file names | ✓ |
| Win10&11 / Win 7&8 / mac OS *(folder names on the stick)* | verbatim | folder names as they appear on the USB stick | ✓ |
| Silicon Motion | Silicon Motion | vendor name | ✓ |
| S6-L / S6-R / HD Audio Driver for Display Audio / Speaker (Realtek(R) Audio) | verbatim | audio device names as they appear in the OS | ✓ |

---

## 6. OSD — the device speaks English

The on-screen display is rendered by the monitor firmware in English. Nothing that the
user reads *on the device* may be translated, or the manual stops matching the hardware.

### 6.1 ALL-CAPS OSD labels — verbatim, untranslatable

These 22 labels come from `translations/dnt.json` and appear on the physical device.
Reproduce them character-for-character, including the caps.

```
ASPECT        BLUE          BRIGHTNESS    COLOR TEMP    CONTRAST
DCR           ECO           FPS           GREEN         HDR
HDR MODE      LANGUAGE      LOW BLUE LIGHT              ON/OFF
OSD TIMER     RED           RESET         RTS           SHARPNESS
SOURCE        TRANSPARENCY  WIDE
```

Also verbatim: `OSD`, `DCR` and its expansion `Dynamic Contrast Ratio`, `HDR` and its
expansion `High Dynamic Range`.

**`Backlight` is context-dependent** (`dnt.json`, commit `12b31e3`) — it is *not* a flat
DNT term. In this corpus it never appears in ALL CAPS, so it is **always translated**:

| Context | German |
|---|---|
| OSD chapter heading `### 1. Backlight` / `## Backlight` | **`Hintergrundbeleuchtung`** (§6.4) |
| Spec-table field name (the `Backlight` row, value `LED`) | **`Hintergrundbeleuchtung`** |
| Body prose ("the backlight brightness") | **`Hintergrundbeleuchtung`** |
| Button description "adjusts the backlight (brightness)" | `stellt die Hintergrundbeleuchtung (Helligkeit) ein` |

Where the EN writes `**Color Temp. (COLOR TEMP.):**` the trailing period inside the
parentheses is part of the on-device label — keep it.

### 6.2 Gloss pattern

The EN corpus uses two styles. Mirror each one:

| EN pattern | German pattern |
|---|---|
| `**Brightness (BRIGHTNESS):**` — gloss + label | `**Helligkeit (BRIGHTNESS):**` — translate the gloss, keep the label |
| `**BRIGHTNESS (0–100):**` — bare label + range | `**BRIGHTNESS (0–100):**` — unchanged |
| `**ECO mode (ECO):**` | `**ECO-Modus (ECO):**` |
| `**Low Blue Light (LOW BLUE LIGHT):**` | `**Low Blue Light (LOW BLUE LIGHT):**` — the gloss is already the label; leave it |

A third style appears on Lite / Lite 144 Hz, where the EN gives the gloss **without** a
CAPS token (`**Color Temperature:**`, `**Language:**`, `**Black Level (0–100):**`). Use
the same German word as in §6.2.1 — the gloss word never changes just because the CAPS
token is absent.

### 6.2.1 Gloss vocabulary — the German words used *as* the gloss

The CAPS token beside them never changes; only these words do. Locking them here is what
keeps eleven per-product translators from drifting (`Signalquelle` vs `Quelle`,
`Schärfe` vs `Bildschärfe`).

| EN gloss | German (locked) |
|---|---|
| Brightness | Helligkeit |
| Contrast | Kontrast |
| Sharpness | Schärfe |
| Black Level | Schwarzwert |
| Aspect / Aspect Ratio | Seitenverhältnis |
| Color Temperature / Color Temp. | Farbtemperatur |
| Red | Rot |
| Green | Grün |
| Blue | Blau |
| Language | Sprache |
| OSD Timer | OSD-Timer |
| Transparency | Transparenz |
| Source | Signalquelle |
| Reset | Zurücksetzen |
| HDR Mode | HDR-Modus |
| ECO mode / ECO Mode / ECO modes | ECO-Modus *(EN casing varies by product — one German target)* |
| Low Blue Light | Low Blue Light *(the gloss **is** the device label — leave it)* |
| DCR (Dynamic Contrast Ratio) | DCR (Dynamic Contrast Ratio) *(acronym + its expansion, both EN)* |

**The ~37 range-suffixed run-in variants are generated, not listed.** The corpus contains
`**Brightness (0–100):**`, `**Sharpness (0–4):**`, `**OSD Timer (10–60 seconds):**`,
`**Aspect Ratio (16:9 / 4:3):**`, `**DCR (Dynamic Contrast Ratio) (ON/OFF):**` and so on.
Do not look for each one here: apply the §6.2 pattern with the vocabulary above and the
number rules in §4. Worked examples:

| EN | German |
|---|---|
| `**Brightness (0–100):**` | `**Helligkeit (0–100):**` |
| `**Sharpness (0–4):**` | `**Schärfe (0–4):**` |
| `**OSD Timer (10–60 seconds):**` | `**OSD-Timer (10–60 Sekunden):**` |
| `**Aspect Ratio (16:9 / 4:3):**` | `**Seitenverhältnis (16:9 / 4:3):**` |
| `**DCR (Dynamic Contrast Ratio) (ON/OFF):**` | `**DCR (Dynamic Contrast Ratio) (ON/OFF):**` |
| `**Transparency (TRANSPARENCY):**` | `**Transparenz (TRANSPARENCY):**` |

Only `seconds` → `Sekunden` is translated inside a range; digits, `:`-ratios, `ON/OFF`
and CAPS tokens are untouched.

### 6.3 On-device menu *values* — verbatim

Every selectable value shown by the firmware stays English:

```
Standard   Game   Movie   Text   FPS   RTS   Energy Saving
Warm       Cool   User    Standard
Off        Auto   2084
ON         OFF    ON/OFF
Type-C1    Type-C2   HDMI
4:3        16:9   WIDE
```

`Wähle **RESET**, um alle Einstellungen auf die Werkseinstellungen zurückzusetzen.` —
the label and the value stay English, the sentence around them is German.

### 6.4 OSD chapter headings — translated

**Every OSD chapter heading is translated into natural German.** Headings are the
document's own prose, not device text; only the parenthesised ALL-CAPS labels inside the
body (`(LANGUAGE)`, `(OSD TIMER)`, `(BRIGHTNESS)` …) render on the physical device and
stay English.

This follows the locked NL precedent, which translates every `osd.mdx` heading:
`## Backlight` → `## Achtergrondverlichting`, `## Image` → `## Beeldinstellingen`,
`## Reset` → `## Resetten`, `### 1. Achtergrondverlichting`, `### 5. Resetten`.

| EN heading | German |
|---|---|
| `1. Backlight` | `1. Hintergrundbeleuchtung` |
| `1. Brightness` | `1. Helligkeit` |
| `2. Image` | `2. Bildeinstellungen` |
| `2. Image Modes` | `2. Bildmodi` |
| `3. Color` | `3. Farbeinstellungen` |
| `3. Color Settings` | `3. Farbeinstellungen` |
| `4. Settings` | `4. Einstellungen` |
| `4. OSD Settings` | `4. OSD-Einstellungen` |
| `5. Reset` | `5. Zurücksetzen` |
| `6. Other` | `6. Sonstiges` |
| `## Backlight` *(Flip, `##`-level)* | `## Hintergrundbeleuchtung` |
| `## Image` *(Flip)* | `## Bildeinstellungen` |
| `## Color` *(Flip)* | `## Farbeinstellungen` |
| `## Settings` *(Flip)* | `## Einstellungen` |
| `## Reset` *(Flip)* | `## Zurücksetzen` |
| `## Other` *(Flip)* | `## Sonstiges` |

**No parenthetical device name in the heading.** NL's `expand/osd.mdx` alone appends the
English menu name — `### 1. Achtergrondverlichting (Backlight)` — while its five sibling
products do not. That is exactly the per-file inconsistency this glossary exists to
prevent, so German uses the bare translated heading in **all** products.

**`Reset` heading vs `RESET` label.** The heading is `5. Zurücksetzen`; the value the
user selects on the device inside that menu stays `RESET`:
`Wähle **RESET**, um alle Einstellungen auf die Werkseinstellungen zurückzusetzen.`
Same split for `Zurücksetzen (RESET)` in the §6.2 gloss pattern.

The wrapper headings around these sections are likewise translated — see §7
(`Using the OSD` → `Das OSD verwenden`, `OSD Settings` (wrapper) → `OSD-Einstellungen`,
`Introduction to the OSD` → `Einführung in das OSD`). Note that the wrapper
`## OSD Settings` and the numbered `### 4. OSD Settings` both render as
`OSD-Einstellungen`; that collision exists in the EN source too and is not a defect.

---

## 7. Document & section names

Every `##` / `###` heading and every frontmatter `title` in the EN corpus.

### 7.1 Frontmatter `title`

| English | German |
|---|---|
| Screenmate Product Manuals | Screenmate-Produkthandbücher |
| Screenmate OneCable Manual | Screenmate OneCable – Handbuch |
| Screenmate Lite Manual | Screenmate Lite – Handbuch |
| Screenmate Lite 144 Hz Manual | Screenmate Lite 144 Hz – Handbuch |
| Screenmate Dual Flip Manual | Screenmate Dual Flip – Handbuch |
| Screenmate Flip Manual | Screenmate Flip – Handbuch |
| Screenmate Expand Manual | Screenmate Expand – Handbuch |
| Screenmate Infinity Manual | Screenmate Infinity – Handbuch |
| Screenmate Infinity Lite Manual | Screenmate Infinity Lite – Handbuch |
| Screenmate One 4K Manual | Screenmate One 4K – Handbuch |
| Screenmate One 4K OLED Manual | Screenmate One 4K OLED – Handbuch |
| Screenmate Panorama Manual | Screenmate Panorama – Handbuch |
| Installation | Installation |
| Installation Windows | Installation Windows |
| Installation macOS | Installation macOS |
| Ports and Buttons | Anschlüsse und Tasten |
| Ports and Controls | Anschlüsse und Bedienelemente |
| On-Screen Menu (OSD) | Bildschirmmenü (OSD) |
| Display Settings | Anzeigeeinstellungen |
| Display & Sound Settings | Anzeige- und Toneinstellungen |
| FAQ | FAQ |
| Safety Instructions | Sicherheitshinweise |

### 7.2 Frontmatter `description`

| English | German |
|---|---|
| Digital manuals for all Screenmate products | Digitale Handbücher für alle Screenmate-Produkte |
| Setting up and connecting your Screenmate {X} | Aufbau und Anschluss deines Screenmate {X} |
| Connecting your Screenmate {X} | So schließt du deinen Screenmate {X} an |
| Unfolding, connecting and storing your Screenmate Flip | Aufklappen, Anschließen und Verstauen deines Screenmate Flip |
| Unfolding, setting up and storing your Screenmate Infinity Lite | Aufklappen, Aufbauen und Verstauen deines Screenmate Infinity Lite |
| Installation and connecting your Screenmate OneCable | Installation und Anschluss deines Screenmate OneCable |
| Overview of ports and control buttons | Übersicht über die Anschlüsse und Bedientasten |
| Overview of ports and the multifunctional button | Übersicht über die Anschlüsse und die Multifunktionstaste |
| Display settings via the on-screen menu | Bildschirmeinstellungen über das Bildschirmmenü |
| Adjusting display settings via the on-screen menu | Bildschirmeinstellungen über das Bildschirmmenü anpassen |
| Per-screen display settings via the on-screen menu | Bildschirmeinstellungen pro Bildschirm über das Bildschirmmenü |
| Display settings for Windows and macOS | Anzeigeeinstellungen für Windows und macOS |
| Configuring your displays on Windows and macOS | Bildschirme unter Windows und macOS einrichten |
| Configuring extra screens and audio output on Windows and macOS | Zusätzliche Bildschirme und Audioausgabe unter Windows und macOS einrichten |
| Configure display and sound output on Windows and macOS | Bildschirm- und Tonausgabe unter Windows und macOS einrichten |
| Driver installation for Windows | Treiberinstallation für Windows |
| Driver installation for macOS | Treiberinstallation für macOS |
| Frequently asked questions and troubleshooting | Häufige Fragen und Fehlerbehebung |
| Important safety information and warnings | Wichtige Sicherheitshinweise und Warnungen |

The eleven product-index descriptions, in full (the `\"` escapes in the EN frontmatter
are preserved as-is in the DE frontmatter):

| English | German |
|---|---|
| Complete user manual for your Screenmate OneCable portable monitor | Vollständiges Handbuch für deinen tragbaren Monitor Screenmate OneCable |
| Complete user manual for your Screenmate Lite portable monitor | Vollständiges Handbuch für deinen tragbaren Monitor Screenmate Lite |
| Complete user manual for your Screenmate Lite 144 Hz portable monitor | Vollständiges Handbuch für deinen tragbaren Monitor Screenmate Lite 144 Hz |
| Complete user manual for your Screenmate Dual Flip 16" foldable dual-screen extension | Vollständiges Handbuch für deine faltbare Doppelbildschirm-Erweiterung Screenmate Dual Flip 16" |
| Complete user manual for your Screenmate Flip — available in 14" and 15.6" | Vollständiges Handbuch für deinen Screenmate Flip – erhältlich in 14" und 15,6" |
| Complete user manual for your Screenmate Expand triple-screen portable monitor, available in 14" and 15.6" | Vollständiges Handbuch für deinen tragbaren Monitor Screenmate Expand mit drei Bildschirmen, erhältlich in 14" und 15,6" |
| Complete user manual for your Screenmate Infinity dual portable monitor | Vollständiges Handbuch für deinen tragbaren Doppelmonitor Screenmate Infinity |
| Complete user manual for your Screenmate Infinity Lite portable display extension | Vollständiges Handbuch für deine tragbare Bildschirmerweiterung Screenmate Infinity Lite |
| Complete user manual for your Screenmate One 4K 15.6" portable monitor | Vollständiges Handbuch für deinen tragbaren Monitor Screenmate One 4K 15,6" |
| Complete user manual for your Screenmate One 4K OLED 15.6" portable monitor | Vollständiges Handbuch für deinen tragbaren Monitor Screenmate One 4K OLED 15,6" |
| Complete user manual for your Screenmate Panorama 15.6" triple-screen portable monitor | Vollständiges Handbuch für deinen tragbaren Monitor Screenmate Panorama 15,6" mit drei Bildschirmen |

Note the article agreement: the product noun governs it, so `deinen … Monitor
Screenmate OneCable` (masc.) but `deine … Bildschirmerweiterung Screenmate Infinity
Lite` (fem.). In every other context the product itself is masculine — `der Screenmate
Infinity Lite` (§1.0).

### 7.3 `#` and `##` headings

| English | German |
|---|---|
| Welcome to Screenmate Manuals | Willkommen bei den Screenmate-Handbüchern |
| Available Manuals | Verfügbare Handbücher |
| Need Help? | Brauchst du Hilfe? |
| What is the Screenmate {X}? | Was ist der Screenmate {X}? |
| Package Contents | Lieferumfang |
| Technical Specifications | Technische Daten |
| Choose Your Cables | Die richtigen Kabel wählen |
| Installation Instructions | Installationsanleitung |
| Installation Steps | Installationsschritte |
| Physical Setup | Aufbau und Aufstellung |
| Setup | Aufbau |
| Protective Cap | Schutzkappe |
| Unfolding the Screens | Die Bildschirme aufklappen |
| Connection Options | Anschlussmöglichkeiten |
| Using with 2 USB Cables | Verwendung mit 2 USB-Kabeln |
| Charging the Screenmate OneCable | Den Screenmate OneCable laden |
| Storage | Aufbewahrung |
| Storing the Screenmate | Den Screenmate verstauen |
| Getting Started | Erste Schritte |
| Install the Display Driver | Displaytreiber installieren |
| Driver Installation for Windows | Treiberinstallation für Windows |
| Driver Installation for macOS | Treiberinstallation für macOS |
| If the Driver Doesn't Work | Wenn der Treiber nicht funktioniert |
| Ports and Buttons | Anschlüsse und Tasten |
| Buttons and Functions | Tasten und Funktionen |
| Controls and OSD Menu | Bedienung und OSD-Menü |
| On-Screen Menu (OSD) | Bildschirmmenü (OSD) |
| On-Screen Menu Settings | Einstellungen im Bildschirmmenü |
| Introduction to the OSD | Einführung in das OSD |
| Using the OSD | Das OSD verwenden |
| Using the OSD Menu | Das OSD-Menü verwenden |
| OSD Settings *(wrapper heading over the numbered sections)* | OSD-Einstellungen |
| Per-Screen Settings | Einstellungen pro Bildschirm |
| Display Configuration | Bildschirmkonfiguration |
| Display Configuration Windows | Bildschirmkonfiguration Windows |
| Display Configuration macOS | Bildschirmkonfiguration macOS |
| Display Configuration (OS-Level) | Bildschirmkonfiguration (Betriebssystem) |
| Arrange Your Displays (Video) | Bildschirme anordnen (Video) |
| Sound Settings | Toneinstellungen |
| Backlight / Image / Color / Settings / Reset / Other *(Flip OSD chapters)* | Hintergrundbeleuchtung / Bildeinstellungen / Farbeinstellungen / Einstellungen / Zurücksetzen / Sonstiges — see §6.4 |
| FAQ | FAQ |
| Safety Instructions | Sicherheitshinweise |

**Locked exception (mirrors the NL lock).** The display-settings chapter headings are
`Bildschirmkonfiguration Windows` / `Bildschirmkonfiguration macOS`, with the
frontmatter `title` `Anzeigeeinstellungen`. That word split and that casing are fixed.
This chapter is checksum-identical across OneCable, Dual Flip, Flip and Expand in the EN
and NL trees — it must stay checksum-identical in DE. Never edit one product's copy of
it without editing all four.

### 7.4 `###` headings

**Ports & buttons**

| English | German |
|---|---|
| Ports | Anschlüsse |
| Side Ports | Seitliche Anschlüsse |
| USB-C | USB-C |
| USB-C Port | USB-C-Anschluss |
| USB-C Port (Power & Video) | USB-C-Anschluss (Strom & Video) |
| USB-C Port (Power) | USB-C-Anschluss (Strom) |
| USB-C Port (Power Only / Power Delivery) | USB-C-Anschluss (nur Strom / Power Delivery) |
| USB-C Port (Data/Video/Power) | USB-C-Anschluss (Daten/Video/Strom) |
| USB-C Charging Port | USB-C-Ladeanschluss |
| USB-C (for HDMI > USB-C) | USB-C (für HDMI-auf-USB-C) |
| USB-A Port | USB-A-Anschluss |
| HDMI Port | HDMI-Anschluss |
| Mini HDMI | Mini-HDMI |
| Mini HDMI Port | Mini-HDMI-Anschluss |
| 3 × Mini HDMI Ports | 3 × Mini-HDMI-Anschlüsse |
| 3.5mm Headphone Jack / 3.5 mm Headphone Jack | 3,5-mm-Klinkenanschluss |
| Speaker | Lautsprecher |
| Indicator Light | Statusanzeige |
| LED Indicator | LED-Anzeige |
| Buttons | Tasten |
| Control Buttons | Bedientasten |
| Brightness Buttons | Helligkeitstasten |
| Multifunctional Button | Multifunktionstaste |
| Menu Button (Power / OSD) | Menütaste (Power / OSD) |
| M — OSD Menu Button | M – OSD-Menütaste |
| Menu / Selection / Confirm Button | Menü-/Auswahl-/Bestätigungstaste |
| Menu / Select / Confirm | Menü / Auswahl / Bestätigen |
| Confirm / Exit Button | Bestätigen-/Beenden-Taste |
| Power Button | Power-Taste |
| Power & Return Button | Power- und Zurück-Taste |
| Scroll Wheel | Scrollrad |
| + and − Buttons | Tasten + und − |
| + Button (Increase Brightness) | Taste + (Helligkeit erhöhen) |
| − Button (Decrease Brightness) | Taste − (Helligkeit verringern) |
| Up Button (+) | Taste Auf (+) |
| Down Button (−) | Taste Ab (−) |
| Left "Min" Button | Linke Taste „Min“ |
| Right "Plus" Button | Rechte Taste „Plus“ |
| Brightness and volume | Helligkeit und Lautstärke |
| Volume and Brightness Shortcuts | Schnellzugriff für Lautstärke und Helligkeit |
| Adjusting Brightness | Helligkeit anpassen |
| Adjusting Volume | Lautstärke anpassen |
| Opening the OSD Menu | Das OSD-Menü öffnen |
| OSD Lock | OSD-Sperre |

**Connection scenarios**

| English | German |
|---|---|
| 1. Laptop via USB-C cable | 1. Laptop über USB-C-Kabel |
| 2. Laptop via HDMI cable | 2. Laptop über HDMI-Kabel |
| 3. Phone or tablet via USB-C cable | 3. Smartphone oder Tablet über USB-C-Kabel |
| 4. USB-C game console | 4. Spielkonsole über USB-C |
| 5. Devices with an HDMI port | 5. Geräte mit HDMI-Anschluss |
| 1. Two USB-C Cables / 1. Two USB-C cables | 1. Zwei USB-C-Kabel |
| 1. Dual USB-C connection | 1. Anschluss über zwei USB-C-Kabel |
| 2. USB-C + HDMI & USB-A connection | 2. Anschluss über USB-C + HDMI & USB-A |
| 2. One USB-C Cable, One HDMI Cable and One USB-A Cable | 2. Ein USB-C-Kabel, ein HDMI-Kabel und ein USB-A-Kabel |
| 2. One USB-C cable, one HDMI cable, and one USB-A cable | 2. Ein USB-C-Kabel, ein HDMI-Kabel und ein USB-A-Kabel |
| 2. 1x USB-C, 1x HDMI and 1x USB-A | 2. 1× USB-C, 1× HDMI und 1× USB-A |
| 3. 2x USB-A and 2x HDMI | 3. 2× USB-A und 2× HDMI |
| Option 1 — USB-C (single cable) | Option 1 – USB-C (nur ein Kabel) |
| Option 2 — USB-A + HDMI | Option 2 – USB-A + HDMI |
| Smartphones and game consoles | Smartphones und Spielkonsolen |
| Connect the Screenmate Infinity Lite to your laptop | Den Screenmate Infinity Lite mit deinem Laptop verbinden |
| Connect the Screenmate to your phone or other devices | Den Screenmate mit deinem Smartphone oder anderen Geräten verbinden |

**Setup, folding & storage**

| English | German |
|---|---|
| 1. Release the screen from the stand | 1. Den Bildschirm vom Ständer lösen |
| 2. Attach the main stand | 2. Den Hauptständer anbringen |
| 3. Mount the screen support | 3. Die Bildschirmhalterung montieren |
| 4. Pull out the frame | 4. Den Rahmen herausziehen |
| 5. Adjust the stand | 5. Den Ständer einstellen |
| 6. Open the screens | 6. Die Bildschirme öffnen |
| 7. Close the screens | 7. Die Bildschirme schließen |
| Unfolding the screen | Den Bildschirm aufklappen |
| Folding the screen back up | Den Bildschirm wieder zusammenklappen |
| Folding caution | Vorsicht beim Klappen |
| Setup instructions | Hinweise zum Aufbau |
| Possible layouts | Mögliche Anordnungen |
| Single screen | Einzelner Bildschirm |
| Dual screen — front and back horizontal | Zwei Bildschirme – vorne und hinten, horizontal |
| Dual screen — front and back vertical | Zwei Bildschirme – vorne und hinten, vertikal |
| Flip 14" | Flip 14" |
| Flip 15.6" | Flip 15,6" |

These two are markdown `###` headings (`### Flip 15.6"` in `flip/installation.mdx`), so
the **literal** `"` shown here is correct — NL ships `### Flip 15,6"` the same way. Do
not "fix" these rows to `&quot;`; that escape belongs only in JSX attributes (§4.1,
§7.7).

**Drivers, OS & safety**

| English | German |
|---|---|
| Windows | Windows |
| macOS | macOS |
| Windows 10 or higher | Windows 10 oder höher |
| Download Drivers | Treiber herunterladen |
| Download Driver for macOS | Treiber für macOS herunterladen |
| Installation Steps | Installationsschritte |
| Manual Installation (if needed) | Manuelle Installation (falls nötig) |
| Read this before use | Vor der Verwendung lesen |
| Before use | Vor der Verwendung |
| Check before use | Vor der Verwendung prüfen |

Note: the `Download Drivers` **heading** is translated (`Treiber herunterladen`) because
it names the action, not the volume. The literal volume and folder names —
`DRIVERS (D:)`, `Win10&11`, `Win 7&8`, `mac OS` — stay verbatim (§5). The button label
`Download Windows Drivers` → `Windows-Treiber herunterladen`; `Download for macOS` →
`Für macOS herunterladen`.

**FAQ questions**

| English | German |
|---|---|
| My screen stays black and there's no image after connecting. What should I do? | Mein Bildschirm bleibt schwarz und zeigt nach dem Anschließen kein Bild. Was soll ich tun? |
| The screen is unstable, flickers or occasionally cuts out. What could be the cause? | Das Bild ist instabil, flackert oder fällt gelegentlich aus. Woran kann das liegen? |
| My laptop doesn't have a USB-C port. How can I still use the Screenmate? | Mein Laptop hat keinen USB-C-Anschluss. Wie kann ich den Screenmate trotzdem verwenden? |
| A startup logo appears, but there's no image on my MacBook. What should I do? | Ein Startlogo erscheint, aber auf meinem MacBook wird kein Bild angezeigt. Was soll ich tun? |
| Can the Screenmate charge my laptop when connected to a power source? | Kann der Screenmate meinen Laptop laden, wenn er an eine Stromquelle angeschlossen ist? |

FAQ questions stay in the first person (`Mein …`, `ich`) — they are the reader's voice,
not an instruction, so they take `ich`/`mein`, never `du`/`dein`.

### 7.5 Card titles (`en/manuals-index.mdx`)

| English | German |
|---|---|
| {Product} Manual *(card title)* | {Product} – Handbuch |
| Contact Support | Support kontaktieren |
| Shop Products | Produkte ansehen |
| Warranty Info | Garantieinformationen |
| Get help from our support team | Hilfe von unserem Support-Team erhalten |
| Browse all Screenmate products | Alle Screenmate-Produkte durchsuchen |
| Learn about product warranties | Mehr über die Produktgarantie erfahren |
| Scanning a QR code? | Du hast einen QR-Code gescannt? |

### 7.6 Navigation labels (already locked in `docs.json`)

Do not diverge from these; they were locked in Task 2.

| English | German |
|---|---|
| Manuals *(top-level tab)* | Handbücher |
| Installation Instructions *(OneCable sub-group)* | Installationsanleitungen |

Product tab labels (`OneCable`, `Lite`, `Lite 144 Hz`, `Dual Flip`, `Flip`, `Expand`,
`Infinity`, `Infinity Lite`, `One 4K`, `One 4K OLED`, `Panorama`) are unchanged.

### 7.7 JSX-embedded strings

**These render to the user but are invisible to a heading/frontmatter grep.** Anyone
translating a page by walking `##` headings and frontmatter will leave them in English.
Sweep every page for `<Tab title=`, `<Card title=`, `<a>…</a>` link text, and `<p>`
caption text before declaring a page done.

**In scope:** JSX attribute and child text that renders — `title=` on `<Tab>`/`<Card>`,
link/button text, `<p>` captions under images, and **bare text children** such as the
`<video>` fallback (easy to miss: it is not wrapped in any tag at all).
**Out of scope:** `className`, `src`, `href`, `icon` (never translated) and `alt` (image
alt text is translated per page by the translator, not locked here).

**`<Tab title=…>` — spec tabs and OS tabs**

> **PARSE HAZARD.** The inch mark inside a double-quoted JSX attribute is HTML-escaped as
> `&quot;`. **Keep the entity.** Writing the literal `"` here — e.g. copying
> `Flip 15,6"` out of §1.2 or §7.4 — closes the attribute early and breaks the MDX
> build. Both columns below are shown in the escaped form deliberately, so the row can
> be pasted as-is. Full three-context rule: §4.1.

| English | German |
|---|---|
| `title="OneCable 16&quot;"` | `title="OneCable 16&quot;"` |
| `title="OneCable 14&quot;"` | `title="OneCable 14&quot;"` |
| `title="Expand 15.6&quot;"` | `title="Expand 15,6&quot;"` |
| `title="Expand 14&quot;"` | `title="Expand 14&quot;"` |
| `title="Flip 14&quot;"` | `title="Flip 14&quot;"` |
| `title="Flip 15.6&quot;"` | `title="Flip 15,6&quot;"` |
| `title="Windows"` | `title="Windows"` |
| `title="macOS"` | `title="macOS"` |

Only the decimal separator changes (§4). The product token is DNT.

**`<a>` link / button text** *(OneCable driver pages)*

| English | German |
|---|---|
| Download Windows Drivers | Windows-Treiber herunterladen |
| Download for macOS | Für macOS herunterladen |

Both are translated: they name the action, not the `DRIVERS (D:)` volume (§5, §7.4).

**`<video>` fallback text** *(bare text child, no wrapping tag)*

| English | German |
|---|---|
| Your browser does not support the video tag. | Dein Browser unterstützt das Video-Tag nicht. |

Appears **14 times across 8 files** — twice in each of the six `display-settings.mdx`
pages (12), once each in `onecable/installation-windows.mdx` and
`onecable/installation-mac.mdx` (2). It sits between `<source …/>` and `</video>` with
no tag of its own, so it is invisible to any sweep that only looks inside `<p>`, `<a>`
or `title=`. Translate every occurrence; the string is identical in all 14.

**`<p>` image captions**

| English | German | File |
|---|---|---|
| Protective Case | Schutzhülle | onecable/index |
| 2x USB-A > USB-C Cable | 2× USB-A-auf-USB-C-Kabel | onecable/index |
| USB-C > USB-C Cable | USB-C-auf-USB-C-Kabel | onecable/index |
| USB Stick (Incl. Driver) | USB-Stick (inkl. Treiber) | onecable/index |
| USB-C | USB-C | flip, infinity/installation |
| HDMI | HDMI | flip, infinity/installation |
| USB-A | USB-A | infinity/installation |
| USB-A 2.0 | USB-A 2.0 | flip/installation |
| Landscape view | Querformat | infinity/installation |
| Portrait view | Hochformat | infinity/installation |
| Portrait & landscape combination | Hoch- und Querformat kombiniert | infinity/installation |
| Detached view | Getrennt aufgestellt | infinity/installation |
| Place the screen on the single stand | Den Bildschirm auf den Ständer setzen | infinity/installation |
| The stand supports 360° rotation | Der Ständer lässt sich um 360° drehen | infinity/installation |

Notes:

- The two cable captions use the `>` arrow form in the EN source. German applies the
  locked chain rule (§3.3) and drops the arrow: `2× USB-A-auf-USB-C-Kabel`. The `2x`
  count also becomes `2×` (§4).
- `Place the screen on the single stand` shortens to `auf den Ständer` — the section
  heading above it is already `Einzelner Bildschirm`, so repeating "für einen
  Bildschirm" reads redundant in German. Do not invent `Einzelständer`.
- The port-icon captions (`USB-C`, `HDMI`, `USB-A`, `USB-A 2.0`) are DNT interface names
  and stay exactly as-is.
- `title="[Product Name] Manual"` in `manuals-index.mdx` sits inside a `{/* … */}`
  comment block as a template for future products. **Not user-visible — leave the whole
  comment block in English**, including its `[Product Name]` placeholder and
  `Brief product description` body.

---

## 8. Spec table fields

The `| Feature | Specification |` header row and every field name:

| English | German |
|---|---|
| Feature | Merkmal |
| Specification | Spezifikation |
| Product Name | Produktname |
| Model Number | Modellnummer |
| Resolution | Auflösung |
| Brightness | Helligkeit |
| Aspect Ratio | Seitenverhältnis |
| Response Time | Reaktionszeit |
| Size | Größe |
| Screen Size | Bildschirmgröße |
| Contrast Ratio | Kontrastverhältnis |
| Panel Type | Paneltyp |
| Screen Type | Bildschirmtyp |
| Viewing Angle | Blickwinkel |
| Refresh Rate | Bildwiederholrate |
| Color Accuracy | Farbgenauigkeit |
| Color Gamut | Farbraum |
| Backlight | Hintergrundbeleuchtung |
| Weight | Gewicht |
| Dimensions | Abmessungen |
| Dimensions (folded) | Abmessungen (zusammengeklappt) |
| Color | Farbe |
| Special Features | Besonderheiten |
| HDR | HDR |
| Supported OS | Unterstützte Betriebssysteme |

Values that stay verbatim: `IPS`, `LCD`, `OLED`, `AM-OLED`, `LED`, `HDR 10`, `sRGB`,
`NTSC`, `4K UHD`, `Full HD`, `cd/m²`, `ms`, `Hz`, model numbers (`M107`, `M109`, `M205`),
`Windows`, `macOS`, `Linux`. Translated values: `Grey` → `Grau`, `Black` → `Schwarz`,
`Built-in stand` → `Integrierter Ständer`, `grams` → `Gramm`, `(per screen)` →
`(pro Bildschirm)`.

---

## 9. OS-specific UI labels (must match the German OS)

These must match what the user actually sees in a German-language OS. They apply to
**label text in prose**; the screenshots stay English on all language pages (client
decision, same as NL).

Quote them with German quotes: `Wähle „Desktop auf diese Anzeige erweitern“.`

| Context | EN | DE (matches OS UI) |
|---|---|---|
| Windows | Display settings / Display Settings | Anzeigeeinstellungen |
| Windows | Extend desktop to this display | Desktop auf diese Anzeige erweitern |
| Windows | Identify | Identifizieren |
| Windows | Display orientation | Anzeigeausrichtung |
| Windows | Flipped | Querformat (gedreht) — see note |
| Windows | Mirrored *(superseded — EN now says "Flipped")* | Querformat (gedreht) |
| Windows | Scale | Skalierung |
| Windows | Scale and layout | Skalierung und Anordnung |
| Windows | This PC | Dieser PC |
| Windows | Sound settings | Soundeinstellungen |
| Windows | Output device | Ausgabegerät |
| Windows | taskbar | Taskleiste |
| macOS | System Preferences / System Settings | Systemeinstellungen |
| macOS | Displays | Displays |
| macOS | Arrange / Arrangement | Anordnen |
| macOS | Privacy & Security / Security & Privacy | Datenschutz & Sicherheit |
| macOS | Screen & System Audio Recording | Bildschirm- & Systemaudioaufnahme |
| macOS | Screen Recording | Bildschirmaufnahme |
| macOS | Applications | Programme |
| macOS | Open | Öffnen |
| macOS | Rotation | Drehung |
| macOS | Standard | Standard |
| macOS | Unlock | Entsperren |
| macOS | Sound | Ton |
| macOS | Output *(Sound tab)* | Ausgabe |
| macOS | Apple menu | Apple-Menü |
| macOS | sidebar | Seitenleiste |

**Note on "Flipped".** German Windows has no standalone "Gedreht" entry in the
orientation dropdown; the options are `Querformat`, `Hochformat`,
`Querformat (gedreht)`, `Hochformat (gedreht)`. `Querformat (gedreht)` is the item that
corresponds to the EN "Flipped" in this instruction. Do not invent `Gespiegelt` — that
is the Dutch solution and it does not appear in German Windows.

The NL pages carry parenthetical Dutch OS labels alongside the English
(`'Display settings' ('Beeldscherminstellingen')`) because the screenshots are English.
Do the same in German: `„Display settings“ („Anzeigeeinstellungen“)` on first mention in
the display-settings chapter, then the German label alone.

---

## 10. Tone, phrasing & literal-translation traps

### 10.1 Locked constructions

| English | German (locked) |
|---|---|
| Note: | Hinweis: |
| Please note: | Hinweis: *(drop "please", same as `Note:`)* |
| Important: | Wichtig: |
| Important Information: | Wichtige Informationen: |
| Caution: | Achtung: |
| Warning | Warnung |
| Tip: | Tipp: |
| Welcome! | Willkommen! |
| Please … | *(drop it — bare imperative)* |
| Make sure that … | Achte darauf, dass … |
| Make sure you use the correct USB-C port. | Achte darauf, dass du den richtigen USB-C-Anschluss verwendest. |
| You can / You may | Du kannst |
| Your laptop | Dein Laptop |
| Your Screenmate | Dein Screenmate — never `Ihr Screenmate` |
| After successful installation, … | Nach erfolgreicher Installation … |
| Follow these steps: | Gehe so vor: |
| Follow the on-screen instructions | Folge den Anweisungen auf dem Bildschirm |
| Then proceed to step 5 | Fahre dann mit Schritt 5 fort |
| See [X] for … | Unter [X] findest du … |
| as shown in image 2 | wie in Abbildung 2 gezeigt |
| for example / e.g. | zum Beispiel / z. B. *(note the space in `z. B.`)* |
| such as | wie zum Beispiel |
| if needed / if necessary | falls nötig |
| provided that | sofern |
| it's now ready for use | er ist jetzt einsatzbereit *(`er` = der Screenmate)* |
| Pick the one that matches your device. | Wähle die Variante, die zu deinem Gerät passt. |
| We recommend … | Wir empfehlen, … |
| Take good care of your Screenmate | Geh sorgsam mit deinem Screenmate um |
| Do not press on the screens | Drücke nicht auf die Bildschirme |
| Turn off the screen when not in use | Schalte den Bildschirm aus, wenn du ihn nicht verwendest |
| Only use the included AC/DC adapter | Verwende ausschließlich das mitgelieferte AC/DC-Netzteil |
| the included / the supplied | das mitgelieferte |
| Need extra power? | Brauchst du mehr Strom? |
| No USB-C port on your laptop? | Dein Laptop hat keinen USB-C-Anschluss? |
| Screen upside down? | Bildschirm steht auf dem Kopf? |
| Need more room? / Need more overview? | Brauchst du mehr Platz? |
| Want to extend your workspace? | Möchtest du deine Arbeitsfläche erweitern? |

### 10.2 Literal-translation traps

Word-for-word renderings that are wrong or unidiomatic in German.

| English | Wrong (literal DE) | Right (natural DE) |
|---|---|---|
| Make sure that X | Mache sicher, dass X | Achte darauf, dass X |
| As soon as you connect it | Sobald du es verbindest | Sobald du ihn anschließt |
| Click 'Open' | Klicke „Öffnen“ | Klicke **auf** „Öffnen“ |
| Follow the on-screen instructions | Folge den Auf-dem-Bildschirm-Anweisungen | Folge den Anweisungen auf dem Bildschirm |
| Restart your laptop | Restarte deinen Laptop / Neustarte deinen Laptop | Starte deinen Laptop neu |
| If the driver doesn't work | Wenn der Treiber nicht arbeitet | Wenn der Treiber nicht funktioniert |
| Then proceed to step 5 | Dann fortfahre zu Schritt 5 | Fahre dann mit Schritt 5 fort |
| Take good care of your X | Nimm gute Sorge von deinem X | Geh sorgsam mit deinem X um |
| The screen turns on | Der Bildschirm dreht an | Der Bildschirm schaltet sich ein |
| Turn the device on / off | Drehe das Gerät an / aus | Schalte das Gerät ein / aus |
| Press and hold | Drücke und halte | Halte … gedrückt |
| Short press / long press | Kurzer Druck / langer Druck | Kurz drücken / lang drücken |
| Plug the cable into the port | Plugge das Kabel in den Port | Stecke das Kabel in den Anschluss |
| Your laptop delivers enough power | Dein Laptop liefert genug Macht | Dein Laptop liefert genug Strom |
| Drag the displays into order | Ziehe die Displays in Ordnung | Ziehe die Bildschirme in die richtige Reihenfolge |
| Check whether … | Checke ob … | Prüfe, ob … |
| Screen real estate | Bildschirm-Immobilien | Bildschirmfläche |
| Watch your fingers | Beobachte deine Finger | Achte auf deine Finger |
| the monitor operates on a DC input | der Monitor operiert auf einem DC-Eingang | der Monitor arbeitet mit einem DC-Eingang |
| It is recommended to restart | Es ist empfohlen zu neustarten | Wir empfehlen, den Laptop neu zu starten |
| supports video output | supportet Videoausgang | unterstützt die Videoausgabe |
| ready for use | fertig für Gebrauch | einsatzbereit |
| Once both connections are made | Einmal beide Verbindungen gemacht sind | Sobald beide Verbindungen hergestellt sind |

### 10.3 Sentence structure

- **Comma before subordinate clauses is mandatory** in German: `Achte darauf**,** dass
  du den richtigen Anschluss verwendest.` / `Prüfe**,** ob der Treiber installiert ist.`
  / `Schalte den Bildschirm aus**,** wenn du ihn nicht verwendest.` A missing comma here
  is a grammar error, not a style choice.
- **Comma before an extended infinitive with `um … zu`:**
  `Drücke die M-Taste**,** um das OSD-Menü zu öffnen.`
- **Verb-second in main clauses, verb-final in subordinate clauses.** English
  "If your laptop has two USB-C ports, use the two included cables" →
  `Wenn dein Laptop zwei USB-C-Anschlüsse **hat**, verwende die beiden mitgelieferten
  Kabel.` (verb at the end of the `wenn` clause).
- **Keep sentences short.** Where the EN chains three clauses, split into two German
  sentences rather than building a 40-word Schachtelsatz.
- **Prefer the active voice.** `Der Screenmate erkennt angeschlossenes Zubehör
  automatisch.` over `Angeschlossenes Zubehör wird automatisch erkannt.`
- **Do not nominalise.** `Nach der Durchführung der Installation` → `Nach der
  Installation`.
- **Do not translate `you` in generic statements.** `Your computer recognises the video
  signal automatically` → `Dein Computer erkennt das Videosignal automatisch` (keep the
  possessive), but `not every USB-C port can output video` →
  `Nicht jeder USB-C-Anschluss kann Video ausgeben` (no `du` needed — don't insert one).

### 10.4 Specific terms to watch

- **`Anschluss` vs `Verbindung`:** `Anschluss` = the physical socket, and the act of
  plugging in. `Verbindung` = the established link. `Anschlussmöglichkeiten` (heading),
  but `wenn die Verbindung instabil ist`.
- **`Taste` vs `Knopf` vs `Schalter`:** always `Taste` for the device's buttons.
  `Schalter` only for a macOS toggle switch in Systemeinstellungen.
- **`Bildschirm` vs `Display` vs `Monitor`:** `Bildschirm` is the default for the screen
  surface and for individual screens of a multi-screen product. `Monitor` for the product
  as a whole ("the monitor turns on"). `Display` only where the EN clearly means the
  panel as a hardware component, and in the macOS UI label `Displays`.
- **`Treiber` vs `DRIVERS`:** `Treiber` in body copy and headings — always. `DRIVERS`
  only when quoting the literal USB-stick volume label `DRIVERS (D:)`.
- **`falls` vs `wenn` vs `ob`:** `falls` = "in case / if it should happen"; `wenn` =
  plain conditional or temporal "when"; `ob` = "whether" after `prüfen`/`sehen`. Never
  use `wenn` where the EN means "whether".
- **`einstellen` vs `anpassen` vs `festlegen`:** `anpassen` for adjusting a value up or
  down (brightness, volume); `einstellen` for setting up a position or configuration
  (the stand, the angle); `festlegen` for defining a fixed value (`Lege den Schwarzwert
  fest`).
- **`mitgeliefert` vs `enthalten`:** `mitgeliefert` for "included/supplied" with the
  product; `enthalten` for "contained in the package" (`Prüfe, ob alle unten
  aufgeführten Teile in der Verpackung enthalten sind`).
- **English gerund headings.** EN `-ing` headings (`Adjusting Brightness`, `Storing the
  Screenmate`, `Using the OSD`) become German infinitive phrases with the object first:
  `Helligkeit anpassen`, `Den Screenmate verstauen`, `Das OSD verwenden`. Never a
  German present participle (`Anpassend der Helligkeit`).

### 10.5 Bold run-in labels (non-OSD)

`**Label:**` run-ins open a line of body copy. They are bold **bare text**, not
attributes and not headings, so no heading grep, frontmatter grep or JSX sweep sees
them — and they recur across products, where eleven per-product translators drift
(`Einschalten:` vs `Anschalten:` vs `Einschalten des Monitors:`). Lock them.

Carry the bold markers and the colon over exactly. German sentence-style capitalisation
applies: only the first word (and nouns) are capitalised.

| English | German | Occurrences |
|---|---|---|
| `**Power supply:**` | `**Stromversorgung:**` | 8 — lite, lite-144hz, one-4k, one-4k-oled installation |
| `**Connecting the console:**` | `**Konsole anschließen:**` | 4 — same four installation pages |
| `**Connecting the HDMI device:**` | `**HDMI-Gerät anschließen:**` | 4 — same four |
| `**USB-C Port:**` | `**USB-C-Anschluss:**` | 4 — expand, flip controls |
| `**Short press:**` | `**Kurz drücken:**` | 3 — infinity, panorama controls |
| `**Long press:**` | `**Lang drücken:**` | 1 — panorama/controls |
| `**Long press (1 second):**` | `**Lang drücken (1 Sekunde):**` | 1 — panorama/controls |
| `**Press and hold (2 seconds):**` | `**2 Sekunden gedrückt halten:**` | 1 — infinity/controls |
| `**Press and hold (3 seconds):**` | `**3 Sekunden gedrückt halten:**` | 1 — infinity/controls |
| `**Press right ("Plus"):**` | `**Nach rechts drücken („Plus“):**` | 1 — infinity/controls |
| `**Press left ("Min"):**` | `**Nach links drücken („Min“):**` | 1 — infinity/controls |
| `**Turn on:**` | `**Einschalten:**` | 2 — one-4k, one-4k-oled osd |
| `**Open the OSD menu:**` | `**OSD-Menü öffnen:**` | 2 — idem |
| `**Navigate:**` | `**Navigieren:**` | 2 — idem |
| `**Select:**` | `**Auswählen:**` | 2 — idem |
| `**Adjust settings:**` | `**Einstellungen anpassen:**` | 2 — idem |
| `**Go back:**` | `**Zurück:**` | 2 — idem |
| `**+ button:**` | `**Taste +:**` | 2 — one-4k, one-4k-oled controls |
| `**− button:**` | `**Taste −:**` | 2 — idem |
| `**+ Increase brightness:**` | `**+ Helligkeit erhöhen:**` | 1 — expand/controls |
| `**− Decrease brightness:**` | `**− Helligkeit verringern:**` | 1 — expand/controls |
| `**≡ Menu button:**` | `**≡ Menütaste:**` | 1 — expand/controls |
| `**Mini HDMI:**` | `**Mini-HDMI:**` | 2 — expand, flip controls |
| `**Steps:**` | `**Schritte:**` | 1 — expand/installation |
| `**Extend your workspace:**` | `**Arbeitsfläche erweitern:**` | 1 — panorama/osd |
| `**Left screen:**` | `**Linker Bildschirm:**` | 2 — dual-flip, expand index |
| `**Right screen:**` | `**Rechter Bildschirm:**` | 2 — dual-flip, expand index |

**Mode labels** — bold, but no colon. Same treatment:

| English | German | Occurrences |
|---|---|---|
| `**General mode**` | `**Allgemeiner Modus**` | 4 — lite, lite-144hz controls |
| `**OSD mode**` | `**OSD-Modus**` | 2 — lite/controls |
| `**OSD menu mode**` | `**OSD-Menü-Modus**` | 2 — lite-144hz/controls |

Consistency anchors — these must agree with renderings already locked elsewhere:
`**Taste +:**` with the §7.4 heading `Taste + (Helligkeit erhöhen)`;
`**Kurz drücken:**` / `**Lang drücken:**` with the §10.2 trap row rejecting
`Kurzer Druck` / `Langer Druck`; `**Nach rechts drücken („Plus“):**` with the §7.4
heading `Rechte Taste „Plus“` and the §3.6 German quote rule.

**Not in this table, by design:**

- **Callout lead-ins** (`**Note:**`, `**Important:**`, `**Important Information:**`,
  `**Please note:**`, `**Caution:**`, `**Tip:**`, `**Welcome!**`) — §10.1. Occurrence
  counts: `Important:` 10, `Important Information:` 5, `Note:` 3, and
  **`Please note:` exactly 1** (`flip/installation.mdx`), which collapses onto the same
  `Hinweis:` target as `**Note:**`.
- **OSD glossed run-ins** (`**Brightness (BRIGHTNESS):**` and the ~37 range-suffixed
  variants) — generated from §6.2 + §6.2.1, deliberately not enumerated.
- **On-device preset values used as run-ins** (`**Standard:**`, `**Game:**`,
  `**Movie:**`, `**Text:**` in the Lite ECO-mode lists) — stay English per §6.3. Only the
  sentence after the colon is translated.
- **Spec-table field names** (`**Resolution**`, `**Weight**`, …) — §8.
- **OS UI labels in bold** (`**Display settings**`, `**System Settings**`, `**Identify**`,
  `**Arrange**`, `**Scale**`, `**Displays**`, `**Display orientation**`) — §9.
- **Device/product literals in bold** (`**M**`, `**+**`, `**−**`, `**+ / −**`,
  `**M (Menu)**`, `**S6-L**`, `**S6-R**`, `**'UsbDisplay'**`, `**Screenmate**`) —
  unchanged; see §5 and §6.1.

---

## 11. Decision log (glossary gate)

All items below have been through the orchestrator's glossary gate. Nothing here is
still open; the log exists so a later reviewer does not re-open a settled question.

**Ruled by the gate**

- **R1 — OSD chapter headings translate.** Corrected: every `osd.mdx` heading is rendered
  in natural German (§6.4), matching the locked NL precedent
  (`## Backlight` → `## Achtergrondverlichting`, `## Reset` → `## Resetten`). Only
  parenthesised ALL-CAPS device labels stay English. My earlier keep-EN rule for
  `## Backlight` was overturned.
- **Spec-table field names translate** — `Backlight` → `Hintergrundbeleuchtung` (§8)
  **confirmed**. NL's keep-EN spec rows are verbatim inheritance from the Dutch booklet;
  no German booklet exists, so DE/FR/IT translate them.
- **`Download Drivers` → `Treiber herunterladen`** — stands (§7.4).
- **`Reverse Charging` keep-EN** — stands (§5), client sign-off noted.
- **`100.000:1`** — stands (§4). German period as thousands separator; the only figure in
  the corpus above four digits. Four-digit figures keep no separator (`1820 Gramm`).
- **DIN 5008 unit spacing** — accepted (§4): `45 W`, `5 V/2 A`, `100 %`, `−20 °C`. This
  is deliberately **not** identical to the NL lock (`45W`, `5V`, `100%`, `-20°C`); do not
  flag it as an nl↔de parity defect. Angles (`178°`) keep no space in both.
- **Title style `Screenmate OneCable – Handbuch`** — accepted pending client sign-off
  (§3.4, §7.1).

**Still worth the client's eye (not blocking)**

- **Windows "Flipped" → `Querformat (gedreht)`** (§9). German Windows has no standalone
  "Gedreht" entry, and the NL solution (`Gespiegeld`) has no German counterpart. Verify
  against a real German Windows install before the pages ship.
- **Three EN-source inconsistencies normalised in German.** `Mini HDMI` / `Mini-HDMI` →
  always `Mini-HDMI` (per `dnt.json`); `protective case` / `protective sleeve` → always
  `Schutzhülle`; `3.5mm` / `3.5 mm` → always `3,5-mm-`.

---

## 12. Adding to the glossary

If you hit a term that is not listed here, do not improvise silently. Propose it:

```
Proposed glossary addition:
| {English} | {German} | {notes} | {keep EN?} |
Reason: {file + heading where this term appears, and why this German rendering}
```

Check first that the term is not already covered by a rule rather than a table row —
most missing compounds are answered by §3, most missing numbers by §4, and anything
in ALL CAPS by §6.1.
