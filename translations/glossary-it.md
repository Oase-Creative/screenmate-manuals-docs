# Screenmate EN→IT Glossary

Locked terminology for all Screenmate Italian copy. Use these exact Italian renderings unless the
English term is intentionally retained (**Keep EN? = ✓**).

This file is **binding** for every Italian translation pass. If a term is not listed here, do not
invent a rendering silently — propose an addition (see the last section).

**Source of truth for "Keep EN?":** `translations/dnt.json` (42 entries: 11 product names, 6 connector
/ standard names, `DRIVERS`, `FAQ`, `OSD`, and 22 OSD caps labels). Every entry in it is
marked ✓ below. Additional ✓ entries are third-party product names, on-device strings and file/
folder names that `dnt.json` does not enumerate but which are equally untranslatable.

**Format:**

| English | Italian (locked) | Notes / variants | Keep EN? |
|---|---|---|---|

---

## 1. Register: informal `tu` — never `Lei` / `Suo`

**Rule:** always address the reader with the informal second person singular: `tu`, `ti`, `te`,
`tuo` / `tua` / `tuoi` / `tue`. Never the courtesy form `Lei` / `La` / `Le` / `Suo` / `Sua` /
`Suoi` / `Sue`, never the plural-courtesy `Voi` / `Vostro`, and never the impersonal-infinitive
instruction style (`Assicurarsi che…`, `Collegare il cavo…`) that Italian appliance manuals default
to. Screenmate copy is friendly and direct, matching the Dutch `je` register.

### 1.1 Wrong register → right register (worked examples)

| ✗ Wrong (courtesy / impersonal) | ✓ Right (informal `tu`) |
|---|---|
| `Colleghi il Suo laptop allo Screenmate.` | `Collega il tuo laptop allo Screenmate.` |
| `La preghiamo di leggere attentamente le seguenti istruzioni prima dell'uso.` | `Leggi attentamente le istruzioni seguenti prima dell'uso.` |
| `Se il Suo laptop non dispone di una porta USB-C, può utilizzare il cavo USB-A.` | `Se il tuo laptop non ha una porta USB-C, puoi usare il cavo USB-A.` |
| `Vada su Impostazioni schermo e selezioni "Estendi il desktop a questo schermo".` | `Vai su Impostazioni schermo e scegli "Estendi il desktop a questo schermo".` |
| `Assicurarsi che entrambe le estremità del cavo siano collegate correttamente.` | `Assicurati che entrambe le estremità del cavo siano collegate correttamente.` |
| `Vi consigliamo di riavviare il computer dopo l'installazione.` | `Ti consigliamo di riavviare il computer dopo l'installazione.` |
| `Prema e tenga premuto il pulsante di accensione.` | `Tieni premuto il pulsante di accensione.` |
| `Non toccare il dispositivo con le mani bagnate.` *(impersonal — acceptable only in the numbered safety list, see 1.4)* | `Non toccare il dispositivo con le mani bagnate.` *(identical form; the `tu` negative imperative **is** `non` + infinitive)* |

### 1.2 Imperatives in numbered steps

Italian numbered steps use the **`tu` imperative**, no subject pronoun. This mirrors the English
imperative one-for-one.

| ✗ Wrong | ✓ Right |
|---|---|
| `Tu colleghi il cavo al laptop` | `Collega il cavo al laptop` |
| `Collegare il cavo al laptop` (infinitive) | `Collega il cavo al laptop` |
| `Colleghi il cavo al laptop` (courtesy) | `Collega il cavo al laptop` |
| `Vada su Impostazioni di Sistema` | `Vai su Impostazioni di Sistema` |
| `Faccia clic su "Apri"` | `Fai clic su "Apri"` |

**Irregular `tu` imperatives that must be used:**
`andare → vai` · `fare → fai` · `dare → dai` · `stare → stai` · `dire → di'` · `avere → abbi`
· `essere → sii` · `tenere → tieni` · `scegliere → scegli` · `rimuovere → rimuovi` ·
`spegnere → spegni` · `accendere → accendi` · `estrarre → estrai` · `apporre/appoggiare → appoggia`.

**Negative imperative:** `non` + **infinitive** (never `non` + imperative).

| ✗ Wrong | ✓ Right |
|---|---|
| `Non premi sullo schermo` | `Non premere sullo schermo` |
| `Non usa liquidi` | `Non usare liquidi` |
| `Non lascia cadere il monitor` | `Non far cadere il monitor` |
| `Non ruoti gli schermi oltre l'angolo massimo` | `Non ruotare gli schermi oltre l'angolo massimo` |

### 1.3 Possessives

Italian drops the possessive far more often than English. Do **not** mechanically render every
English "your".

| English | ✗ Over-literal | ✓ Natural |
|---|---|---|
| `Remove the Screenmate from the packaging` | `Rimuovi il tuo Screenmate dalla tua confezione` | `Rimuovi lo Screenmate dalla confezione` |
| `Connect your laptop` | `Collega il tuo laptop` | `Collega il tuo laptop` *(keep — the laptop is genuinely the reader's)* |
| `your laptop's USB-C port` | `la porta USB-C del tuo laptop` | `la porta USB-C del tuo laptop` *(keep)* |
| `Take good care of your Screenmate` | `Prendi buona cura del tuo Screenmate` | `Abbi cura del tuo Screenmate` |
| `Check your device's specifications` | `Controlla le specifiche del tuo dispositivo` | `Controlla le specifiche del dispositivo` |

**Rule of thumb:** keep `tuo` when the object belongs to the reader and the contrast matters
(`il tuo laptop` vs. lo Screenmate). Drop it for parts of the Screenmate itself
(`lo schermo`, not `il tuo schermo`) and for generic references.

### 1.4 Edge cases

- **Safety / regulatory text.** The 10–14 numbered safety items are already `tu`-compatible because
  they are negative imperatives (`Non toccare…`, `Non usare…`) plus affirmative imperatives
  (`Rimuovi la pellicola protettiva…`, `Pulisci lo schermo…`). Render them as `tu` imperatives.
  If a future source safety text arrives written in the courtesy form or the impersonal infinitive,
  **do not silently convert it** — flag it for the client. Legal/regulatory copy is verbatim.
- **First word of a sentence.** No exception: `Il tuo laptop è ora in carica.` never
  `Il Suo laptop…`.
- **"Please".** English "Please read…" / "Please note" have **no** Italian equivalent here. Drop it
  and use the bare imperative. Never `La preghiamo di`, never `Per favore`, never `Si prega di`.

### 1.5 Courtesy-form defect grep

Any hit in an Italian page is a defect until proven otherwise:

```
\bLei\b|\bSuo\b|\bSua\b|\bSuoi\b|\bSue\b|\bVostr[oaie]\b|\bVi (preghiamo|consigliamo|invitiamo)\b|La preghiamo|Le consigliamo|Si prega di|Per favore|\bpuò\b|\bdeve\b|\bvoglia\b
```

Formal (courtesy) imperatives to grep for as whole words — each one is the courtesy form of a verb
this corpus uses constantly:

```
\b(prema|colleghi|selezioni|scelga|vada|faccia|usi|utilizzi|apra|inserisca|rimuova|verifichi|controlli|scarichi|installi|riavvii|tenga|prenda|segua|posizioni|sollevi|ruoti|pieghi|spenga|accenda)\b
```

**Known false positives** (check context before "fixing"): `selezioni` = plural noun "selections";
`usi` = plural noun "uses"; `posizioni` = plural noun "positions"; `può` / `deve` are legitimate
when the subject is a **thing**, not the reader — `la porta non può fornire alimentazione`,
`il monitor deve essere collegato` are correct. Only `può`/`deve` with the reader as subject
are defects.

---

## 2. Compound formation & hyphenation

Italian is **head-initial**: the head noun comes first, the modifier follows. Every English
"MODIFIER + NOUN" compound inverts.

### 2.1 The core rule

> **`NOUN + ACRONYM`, no hyphen between them, hyphens preserved *inside* the acronym.**

| ✗ Wrong | ✓ Right |
|---|---|
| `USB-C cavo` | `cavo USB-C` |
| `cavo-USB-C` | `cavo USB-C` |
| `USB C cavo` | `cavo USB-C` |
| `USB-C-cavo` | `cavo USB-C` |
| `USB-C porta` | `porta USB-C` |
| `porta-USB-C` | `porta USB-C` |
| `HDMI porta` | `porta HDMI` |
| `Mini HDMI porta` | `porta Mini-HDMI` |
| `USB-A porta` | `porta USB-A` |
| `USB stick` / `USB-stick` | `chiavetta USB` |
| `OSD menu` | `menu OSD` |
| `LED indicatore` | `indicatore LED` |
| `PD caricatore` | `caricabatterie PD` |
| `Power Delivery porta` | `porta Power Delivery` |

**Never** import the Dutch/German hyphen habit (`USB-C-kabel`, `USB-C-Kabel`). Italian uses a
plain space: `cavo USB-C`.

### 2.2 Tokens whose internal hyphens are locked

Write these exactly, always: `USB-C` · `USB-A` · `Mini-HDMI` · `Type-C1` · `Type-C2` ·
`AM-OLED` · `S6-L` · `S6-R` · `HDR 10` (space, no hyphen) · `4:3` · `16:9` · `16:10`.

> **Note — `Mini HDMI` vs `Mini-HDMI`:** the EN corpus is inconsistent (`Mini HDMI Port`,
> `Mini-HDMI to HDMI cables`, `3 × Mini HDMI Ports`). Italian is **locked on the hyphenated
> `Mini-HDMI` in all positions**, matching `dnt.json`. Do not mirror the EN inconsistency.

### 2.3 Noun + noun compounds: use `di` / `per` / `da`

English stacks bare nouns; Italian links them with a preposition.

| English | ✓ Italian |
|---|---|
| driver installation | `installazione del driver` |
| display driver | `driver dello schermo` |
| charging port | `porta di ricarica` |
| power button | `pulsante di accensione` |
| menu button | `pulsante del menu` |
| brightness buttons | `pulsanti della luminosità` |
| display settings | `impostazioni schermo` *(locked short form — see §5)* |
| sound settings | `impostazioni audio` |
| headphone jack | `jack per cuffie` |
| power adapter | `alimentatore` |
| power source / power supply | `fonte di alimentazione` / `alimentazione` |
| output device | `dispositivo di output` |
| screen support | `sostegno dello schermo` |
| package contents | `contenuto della confezione` |
| refresh rate | `frequenza di aggiornamento` |
| response time | `tempo di risposta` |
| viewing angle | `angolo di visione` |
| aspect ratio | `rapporto d'aspetto` |
| contrast ratio | `rapporto di contrasto` |

**Exception — `video` as a postposed modifier** is well established and takes no preposition:
`segnale video` · `uscita video` · `trasmissione video` · `supporto video`.

### 2.4 Specs, ratings and lengths attach with `da`

| English | ✓ Italian |
|---|---|
| 65 W power adapter | `alimentatore da 65 W` |
| a power adapter of at least 45 W | `un alimentatore da almeno 45 W` |
| PD charger of at least 45 W | `un caricabatterie PD da almeno 45 W` |
| 5 V/2 A power source | `una fonte di alimentazione da 5 V/2 A` |
| 3.5 mm headphone jack | `jack per cuffie da 3,5 mm` |
| USB-C to USB-C cable (1.2 m) | `cavo da USB-C a USB-C (1,2 m)` |
| 15.6" portable monitor | `monitor portatile da 15,6"` |
| DC 5V/3A adapter | `alimentatore DC da 5 V/3 A` |

Never `45 W adattatore`, never `adattatore 45 W`, never `adattatore-45W`.

### 2.5 THE THREE-PART CABLE CHAIN — locked

> The Dutch glossary left this under-specified and the NL pages drifted between three renderings.
> **There is exactly one correct Italian form: `cavo da X a Y`.** No exceptions, no synonyms.

**Pattern:** `cavo` + `da` + *source connector* + `a` + *destination connector*.

| English (all source spellings) | ✓ Italian (locked) |
|---|---|
| USB-C to USB-C cable | `cavo da USB-C a USB-C` |
| USB-C > USB-C Cable | `cavo da USB-C a USB-C` |
| 2x USB-C to USB-C cables | `2 cavi da USB-C a USB-C` |
| USB-C to USB-A cable | `cavo da USB-C a USB-A` |
| USB-A to USB-C cable | `cavo da USB-A a USB-C` |
| 2x USB-A > USB-C Cable | `2 cavi da USB-A a USB-C` |
| dual USB-A to USB-C cable | `cavo doppio da USB-A a USB-C` |
| Mini HDMI to HDMI cable | `cavo da Mini-HDMI a HDMI` |
| Mini-HDMI to HDMI cables | `cavi da Mini-HDMI a HDMI` |
| HDMI to USB-C cable | `cavo da HDMI a USB-C` |
| USB-C with USB-A adapter cable | `cavo USB-C con adattatore USB-A` |
| USB-C to USB-C charging cable | `cavo di ricarica da USB-C a USB-C` |

**Rejected variants — never write any of these:**

| ✗ Never | Why |
|---|---|
| `cavo USB-C a USB-C` | missing `da`; reads as "the USB-C cable, to USB-C" |
| `cavo USB-C-USB-C` | hyphen chain is German/Dutch, not Italian |
| `cavo USB-C/USB-C` | slash is ambiguous with the `5 V/2 A` pattern |
| `cavo USB-C verso USB-C` | `verso` = "towards"; wrong register, not used for connectors |
| `cavo da USB-C su USB-C` | wrong preposition |
| `cavo USB-C to USB-C` | untranslated English preposition |
| `cavo dall'USB-C all'USB-C` | never contract `da`/`a` with an article before a bare acronym |
| `cavo da USB-C ad USB-C` | see the `ad` rule below |

**`a`, never `ad`.** The euphonic *d* is locked **off** before every connector acronym:
write `a USB-C`, `a USB-A`, `a HDMI`, `a Mini-HDMI`. This is deliberate — the euphonic *d* is
optional even where the letter-name vowel would license it (`ad HDMI`), and locking one form
removes a whole class of drift. Never `ad USB-C`, never `ad HDMI`.

**Pluralisation:** only the head noun inflects. `cavo` → `cavi`; the `da … a …` chain is frozen.
`2 cavi da USB-C a USB-C` ✓ · `2 cavi da USB-C a USB-C cavi` ✗.

**Directionality is preserved from the EN source, not "corrected".** The EN corpus itself lists
`USB-C to USB-A cable` (Expand) and `USB-A > USB-C Cable` (OneCable) for physically similar cables.
Mirror whichever direction the source page uses. Do not normalise the direction — that is an EN-side
editorial decision, not a translation decision.

### 2.6 Bare acronyms never take an article

Always attach a connector acronym to a head noun. `la porta USB-C` ✓ · `il cavo HDMI` ✓ ·
`l'USB-C` ✗ · `la USB-C` ✗ · `il HDMI` ✗. This single rule removes every gender/article
ambiguity around connector names.

---

## 3. Gender, articles and elision

Italian gender is a high-frequency error site in this corpus because so many head nouns are
loanwords, and because `Screenmate` and `schermo` both trigger the `lo` allomorph.

### 3.1 The `lo` / `gli` trap — `lo Screenmate`, `lo schermo`

`Screenmate` and `schermo` both begin with **s + consonant**, so they take `lo` / `gli`, not
`il` / `i`.

| ✗ Wrong | ✓ Right |
|---|---|
| `il Screenmate` | `lo Screenmate` |
| `i Screenmate` | `gli Screenmate` |
| `del Screenmate` | `dello Screenmate` |
| `al Screenmate` / `sul Screenmate` / `nel Screenmate` | `allo Screenmate` / `sullo Screenmate` / `nello Screenmate` |
| `il schermo` | `lo schermo` |
| `i schermi` | `gli schermi` |
| `sul schermo` | `sullo schermo` |
| `il smartphone` | `lo smartphone` |

**Critical sub-rule — the article agrees with the *next word*, not with the noun.** When a
possessive or adjective intervenes, the allomorph changes:

- `lo Screenmate` **but** `il tuo Screenmate` (because `tuo` begins with `t`)
- `lo schermo` **but** `il tuo schermo`, `il primo schermo`, `il secondo schermo`
- `gli schermi` **but** `i tuoi schermi`, `i due schermi`, `i tre schermi`
- `dello schermo` **but** `del tuo schermo`

### 3.2 Gender of the corpus head nouns

| Noun | Gender | Singular / plural | Notes |
|---|---|---|---|
| Screenmate | m. | `lo Screenmate` / `gli Screenmate` | invariable; never inflect the brand |
| schermo | m. | `lo schermo` / `gli schermi` | |
| display | m. | `il display` / `i display` | invariable loanword |
| monitor | m. | `il monitor` / `i monitor` | invariable |
| laptop | m. | `il laptop` / `i laptop` | invariable |
| smartphone | m. | `lo smartphone` / `gli smartphone` | invariable, `lo` allomorph |
| tablet | m. | `il tablet` / `i tablet` | invariable |
| cavo | m. | `il cavo` / `i cavi` | |
| porta | **f.** | `la porta` / `le porte` | frequent error: never `il porta` |
| presa | f. | `la presa` / `le prese` | |
| spina | f. | `la spina` / `le spine` | plug |
| pulsante | m. | `il pulsante` / `i pulsanti` | |
| rotella | f. | `la rotella` / `le rotelle` | scroll wheel |
| driver | m. | `il driver` / `i driver` | **invariable — never `i drivers`** |
| menu | m. | `il menu` / `i menu` | invariable, **no accent**: `menu`, never `menù` |
| OSD | m. | `l'OSD` | prefer `il menu OSD` |
| alimentatore | m. | `l'alimentatore` / `gli alimentatori` | |
| alimentazione | f. | `l'alimentazione` | |
| luminosità | f. | invariable | `la luminosità` |
| custodia | f. | `la custodia` | |
| chiavetta | f. | `la chiavetta USB` | |
| supporto | m. | `il supporto` / `i supporti` | stand |
| staffa | f. | `la staffa` / `le staffe` | bracket |
| altoparlante | m. | `l'altoparlante` / `gli altoparlanti` | |
| cuffie | f. pl. | `le cuffie` | headphones, always plural |
| pellicola | f. | `la pellicola protettiva` | protective film |
| confezione | f. | `la confezione` | packaging |
| telaio | m. | `il telaio` | frame |
| impostazioni | f. pl. | `le impostazioni` | |

### 3.3 Elision and apostrophes

- Elide before a vowel, with **no space** after the apostrophe:
  `dell'OSD` · `l'alimentazione` · `all'immagine` · `dall'alto` · `un'immagine` (f.) ·
  `d'aspetto`. Never `dell' OSD`.
- `un` before a masculine vowel takes **no** apostrophe: `un alimentatore` ✓, `un'alimentatore` ✗.
  `un'` is feminine only: `un'immagine` ✓.
- Use the **straight ASCII apostrophe `'`** (U+0027), matching the rest of the repo. Never the
  typographic `’`.
- **Accented vowels are real characters, never apostrophe hacks.** `è` not `e'`; `perché` not
  `perche'`; `più`, `può`, `luminosità`, `nitidezza`, `qualità`, `già`.
- `qual è` — **no apostrophe** (`qual'è` is always wrong).
- Verb-final accents: `è` (is) vs `e` (and) — a single missing accent inverts the sentence. Grep
  for ` e ` immediately preceding an adjective when reviewing.

---

## 4. Number, unit and measurement formatting

### 4.1 The table

| Type | Format | Example |
|---|---|---|
| **Decimal separator** | **comma** | `15,6"` · `2,5 cm` · `1,2 m` · `0,5 m` · `3,5 mm` · `2,8 cm` |
| **Thousands separator** | **none — never a comma** | `1820 grammi` · `1000:1` · `1920 × 1080` · `3840 × 2160` |
| Six-digit exception | period | `100.000:1` (One 4K OLED contrast ratio — the corpus's only case) |
| Unit spacing | **space** between value and unit symbol | `60 Hz` · `300 cd/m²` · `25 ms` · `65 W` · `5 V` · `2 A` · `90 cm` · `609 grammi` |
| Compound electrical spec | space on both sides of the value | `5 V/2 A` · `DC 5 V/3 A` · `±2 V` |
| Percent | **no** space | `100% sRGB` · `45% NTSC` · `99% sRGB` · `150%` |
| Angle (degrees of rotation) | **no** space | `180°` · `235°` · `360°` · `90°` |
| Temperature | space before `°C` | `-20 °C` · `60 °C` |
| Inches | straight double prime, no space | `15,6"` · `14"` · `16"` |
| Numeric range (OSD values) | mirror the EN en-dash form | `0–100` · `0–4` · `10–60 secondi` |
| Angle range | en-dash **with** spaces (mirrors EN) | `0° – 235°` · `0° – 360°` |
| Dimensions | `×` with spaces, comma decimals | `40,6 × 23,7 × 2,5 cm` |
| Resolution | mirror the EN form | `1920 × 1080` or `1920×1080` — match the source row |
| Quantity prefix | **number + plural noun**, drop `x` / `×` | `2 cavi da USB-C a USB-C` · `6 clip protettive` · `8 gommini antiscivolo` |
| Time | `secondi` spelled out | `10 secondi` · `2 secondi` · `1 secondo` |

### 4.2 The one rule that matters most

English `1,820 grams` read as Italian is **1,82 grams** — a 1000× error. **Never let an
English comma-thousands separator survive a translation.** Grep every Italian page for
`\d,\d\d\d` before sign-off; every hit is a defect.

Conversely, English `2.5 cm` read as Italian is `25 cm` if the period is dropped. Grep for
`\d\.\d` in Italian body copy; every hit outside the whitelist in §4.3 is a defect.

### 4.3 Never localise these — periods and commas inside them are structural

`M107` · `M109` · `RacerDisplayDriver-2024.9.13-en` · `Win10&11` · `Windows 10` · `Windows 11` ·
`Win 7&8` · `DRIVERS (D:)` · `USB 2.0` · `PlayStation 4/5` · `HDR 10` · `2084` · `S6-L` · `S6-R` ·
`4:3` · `16:9` · `16:10` · `1000:1` · `100.000:1` · `Type-C1` · `Type-C2` · `144 Hz` (in the
product name `Screenmate Lite 144 Hz`).

### 4.4 Units spelled out vs. symbol

- `grams` → `grammi` (spelled out, as in the EN spec tables): `1820 grammi`, `609 grammi`.
- `Watt` in prose → `W` with `da`: EN `65 Watt USB-C power adapter` → `alimentatore USB-C da 65 W`.
- `seconds` → `secondi` (never `sec.`).
- `inch` → keep the `"` prime in spec tables and product-size headings; in flowing prose
  `da 15,6 pollici` is acceptable but `da 15,6"` is preferred for consistency.

### 4.5 Product-size strings carry the decimal comma

The size is a **measurement**, not part of a protected product name, so it converts:

| EN | ✓ IT |
|---|---|
| `Flip 15.6"` | `Flip 15,6"` |
| `Expand 15.6"` | `Expand 15,6"` |
| `OneCable 16"` | `OneCable 16"` |
| `Screenmate Panorama 15.6"` | `Screenmate Panorama 15,6"` |
| `Screenmate Lite 144 Hz` | `Screenmate Lite 144 Hz` *(no decimal — unchanged)* |

The table above is the **literal-`"`** form, used in markdown headings, body prose and spec
tables. Inside a JSX attribute the same string takes `&quot;` instead — `<Tab title="Flip
15,6&quot;">`. See §9.9; a literal `"` there breaks the MDX build.

---

## 5. Term table

### 5.1 Product & hardware

| English | Italian | Notes | Keep EN? |
|---|---|---|---|
| Screenmate | Screenmate | `lo Screenmate` / `gli Screenmate`; never inflect | ✓ |
| OneCable · Lite 144 · Dual Flip · Flip · Expand · Infinity Lite · Infinity · One 4K OLED · One 4K · Panorama | *(unchanged)* | product names; always preceded by `Screenmate` on first mention | ✓ |
| screen | schermo | `lo schermo` / `gli schermi` | — |
| display *(the panel as a device)* | display | m. invariable; use when EN contrasts "display" with "screen" | ✓ |
| monitor | monitor | m. invariable | ✓ |
| portable monitor | monitor portatile | | — |
| triple-screen portable monitor | monitor portatile a tre schermi | | — |
| foldable dual-screen extension | estensione pieghevole a doppio schermo | | — |
| multi-screen monitor | monitor multi-schermo | | — |
| extension screen | schermo aggiuntivo | not `schermo di estensione` | — |
| laptop | laptop | m. invariable; never `portatile` as a noun (ambiguous with `monitor portatile`) | ✓ |
| PC | PC | | ✓ |
| computer | computer | m. invariable | ✓ |
| phone | telefono | | — |
| smartphone | smartphone | `lo smartphone` | ✓ |
| tablet | tablet | | ✓ |
| game console | console di gioco | `la console`, f. invariable | — |
| device | dispositivo | | — |
| cable | cavo | see §2.5 for the `da … a …` chain | — |
| connection cable | cavo di collegamento | | — |
| port | porta | **f.** — `la porta USB-C` | — |
| connector | connettore | | — |
| plug *(noun)* | spina | `la spina USB-A nera` | — |
| button | pulsante | never `bottone` (that is a garment button) | — |
| scroll wheel | rotella di scorrimento | | — |
| multifunctional button | pulsante multifunzione | invariable adjective | — |
| brightness | luminosità | f. invariable | — |
| volume | volume | | — |
| contrast | contrasto | | — |
| sharpness | nitidezza | | — |
| black level | livello del nero | | — |
| speaker *(hardware)* | altoparlante | `l'altoparlante`; EN spec value `Speaker (Realtek(R) Audio)` stays verbatim | — |
| headphones | cuffie | always f. plural | — |
| headphone jack | jack per cuffie | `jack per cuffie da 3,5 mm` | — |
| protective case | custodia protettiva | | — |
| protective sleeve | custodia protettiva | same target — collapses the EN case/sleeve split | — |
| protective cap | cappuccio protettivo | | — |
| protective clips | clip protettive | `clip` invariable f. | — |
| protective film | pellicola protettiva | | — |
| cable organizer | organizzatore per cavi | | — |
| leather carry pouch | custodia in pelle | | — |
| USB stick | chiavetta USB | never `USB-stick` | — |
| power adapter | alimentatore | `l'alimentatore da 65 W` | — |
| AC/DC adapter | alimentatore AC/DC | `AC/DC` verbatim | ✓ *(acronym)* |
| charger | caricabatterie | m. invariable; `caricabatterie PD` | — |
| stand / adjustable stand | supporto / supporto regolabile | | — |
| single screen stand | supporto per schermo singolo | | — |
| screen stand | supporto per schermo | | — |
| screen support | sostegno dello schermo | distinct from `supporto` (the stand) | — |
| bracket | staffa | | — |
| frame | telaio | | — |
| movable arm | braccio mobile | | — |
| locking leg | piedino di bloccaggio | | — |
| front lock | blocco anteriore | | — |
| magnet | magnete | | — |
| stability rubbers | gommini antiscivolo | | — |
| video adapter | adattatore video | | — |
| hub / HDMI hub | hub / hub HDMI | m. invariable | ✓ |
| switch dock | dock | m. invariable; `Nintendo Switch` verbatim | ✓ |
| indicator light | spia luminosa | | — |
| LED indicator | indicatore LED | | — |
| motherboard indicator light | spia della scheda madre | | — |
| ventilation openings | aperture di ventilazione | | — |
| desk | scrivania | | — |
| flat surface | superficie piana | | — |
| workstation | postazione di lavoro | | — |
| workspace | spazio di lavoro | `estendere lo spazio di lavoro` | — |

### 5.2 Connections & power

| English | Italian | Notes | Keep EN? |
|---|---|---|---|
| USB-C | USB-C | | ✓ |
| USB-A | USB-A | | ✓ |
| HDMI | HDMI | | ✓ |
| Mini-HDMI | Mini-HDMI | locked hyphenated in IT even where EN writes `Mini HDMI` | ✓ |
| Power Delivery (PD) | Power Delivery (PD) | brand/standard term | ✓ |
| DisplayPort / DisplayPort Alt Mode | DisplayPort / DisplayPort Alt Mode | standard names | ✓ |
| reverse charging | ricarica inversa | gloss on first use per page: `ricarica inversa (reverse charging)`; **not** in `dnt.json` — see §9 flag | — |
| reverse charging mode | modalità di ricarica inversa | | — |
| fast-charge mode | modalità di ricarica rapida | | — |
| to charge | ricaricare | `il laptop è in carica` = "is charging" | — |
| power *(noun, electricity)* | alimentazione | `alimentazione aggiuntiva` | — |
| power *(output capability)* | potenza | `una potenza in uscita superiore a 10 W` | — |
| output power | potenza in uscita | | — |
| power supply | alimentazione | `alimentazione esterna` = external power supply | — |
| power source | fonte di alimentazione | | — |
| external power source | fonte di alimentazione esterna | | — |
| additional power supply | alimentazione aggiuntiva | | — |
| power outlet / wall outlet | presa di corrente | | — |
| mains | rete elettrica | | — |
| grounded | messa a terra | `assicurati che la presa sia dotata di messa a terra` | — |
| amperage | amperaggio | | — |
| DC input | ingresso DC | `DC` verbatim | ✓ *(acronym)* |
| tolerance | tolleranza | `con una tolleranza di ±2 V` | — |
| standby mode | modalità standby | `standby` invariable | ✓ *(term)* |
| power cable | cavo di alimentazione | | — |
| to connect | collegare | prefer over `connettere` for hardware | — |
| to plug in | inserire / collegare | `inserisci il cavo nella porta` | — |
| to disconnect | scollegare | | — |
| connection | collegamento | `opzioni di collegamento`; **not** `connessione` (that is network) | — |
| video signal | segnale video | | — |
| video output | uscita video | | — |
| video transfer / transmission | trasmissione video | one target for both EN variants | — |
| input source | sorgente di ingresso | | — |
| signal source | sorgente del segnale | | — |
| accessory | accessorio | `accessori USB 2.0` | — |
| mouse | mouse | m. invariable | ✓ |
| keyboard | tastiera | | — |

### 5.3 Software, drivers & OS

| English | Italian | Notes | Keep EN? |
|---|---|---|---|
| driver | driver | m. **invariable** — `il driver`, `i driver`; never `i drivers`, never `pilota` | ✓ |
| `DRIVERS (D:)` *(volume name of the bundled USB stick)* | DRIVERS (D:) | verbatim — `DRIVERS` is the DNT token; it covers the literal drive/volume label only, never the word "driver" in prose or headings | ✓ |
| display driver | driver dello schermo | | — |
| driver installation | installazione del driver | | — |
| to download | scaricare | `Scarica il driver` | — |
| download *(noun / page)* | download | m. invariable | ✓ |
| to install / installation | installare / installazione | | — |
| manual installation | installazione manuale | | — |
| installer | programma di installazione | | — |
| to unzip / extract | estrarre | `estrai l'archivio` | — |
| archive | archivio | | — |
| to restart | riavviare | `Riavvia il laptop`; never `ricominciare` | — |
| operating system | sistema operativo | | — |
| Windows version | versione di Windows | never `Windows versione` | — |
| Windows 10 or higher | Windows 10 o versioni successive | | — |
| to update | aggiornare | | — |
| update *(noun)* | aggiornamento | | — |
| software | software | m. invariable | ✓ |
| application | applicazione | | — |
| to enable / disable | attivare / disattivare | | — |
| toggle | interruttore | `attiva l'interruttore accanto a 'UsbDisplay'` | — |
| to click | fare clic su | `Fai clic su 'Apri'` — Microsoft/Apple IT house style; never `clicca` | — |
| to double-click | fare doppio clic su | | — |
| to right-click | fare clic con il pulsante destro del mouse su | | — |
| to drag | trascinare | | — |
| password | password | f. invariable | ✓ |
| menu bar | barra dei menu | | — |
| taskbar | barra delle applicazioni | Windows IT label | — |
| desktop | desktop | m. invariable | ✓ |
| icon | icona | | — |
| screenshot | screenshot | m. invariable | ✓ |
| on-screen instructions | istruzioni visualizzate sullo schermo | | — |
| UsbDisplay · RacerUSB · RacerDisplayDriver | *(unchanged)* | literal app/file names | ✓ |
| Silicon Motion | Silicon Motion | vendor name | ✓ |
| Windows · macOS · Linux · Mac · MacBook · Apple | *(unchanged)* | | ✓ |
| Nintendo Switch · Nintendo Charging Dock · PlayStation · Xbox · Realtek | *(unchanged)* | | ✓ |

### 5.4 Panel & spec vocabulary

| English | Italian | Notes | Keep EN? |
|---|---|---|---|
| Feature *(spec table column)* | Caratteristica | | — |
| Specification *(spec table column)* | Specifica | | — |
| Model Number | Numero di modello | | — |
| Product Name | Nome del prodotto | | — |
| Resolution | Risoluzione | | — |
| Brightness *(spec field)* | Luminosità | | — |
| Aspect Ratio | Rapporto d'aspetto | | — |
| Response Time | Tempo di risposta | | — |
| Size / Screen Size | Dimensioni schermo | one target for both EN variants | — |
| Dimensions (folded) | Dimensioni (da chiuso) | | — |
| Contrast Ratio | Rapporto di contrasto | | — |
| Panel Type | Tipo di pannello | | — |
| Screen Type | Tipo di schermo | | — |
| Viewing Angle | Angolo di visione | | — |
| Refresh Rate | Frequenza di aggiornamento | | — |
| Color Accuracy | Precisione cromatica | | — |
| Color Gamut | Gamma cromatica | | — |
| Backlight | Retroilluminazione | one target in **every** position — spec-table field (value `LED`) and OSD chapter heading (`### 1. Backlight`) alike. Removed from `dnt.json` in `12b31e3` as context-dependent; gate ruling R1 resolved it to "always translate". Only the ALL-CAPS on-device token inside a parenthetical gloss stays EN | — |
| Weight | Peso | | — |
| Color *(spec field)* | Colore | values: `Grey` → `Grigio`, `Black` → `Nero` | — |
| Special Features | Caratteristiche speciali | | — |
| Supported OS | Sistemi operativi supportati | | — |
| HDR *(spec field)* | HDR | | ✓ |
| IPS · LCD · OLED · AM-OLED · LED · sRGB · NTSC · cd/m² · ms · Hz | *(unchanged)* | standards and unit symbols | ✓ |
| Full HD · 4K UHD | Full HD · 4K UHD | | ✓ |
| built-in stand | supporto integrato | | — |
| deep blacks | neri profondi | | — |
| vivid colours | colori vividi | | — |

### 5.5 Actions, states & connectives

| English | Italian | Notes | Keep EN? |
|---|---|---|---|
| to unfold / fold out | aprire | `Apri i due schermi` | — |
| to fold in / fold back | richiudere / ripiegare | | — |
| to unpack / remove from packaging | estrarre dalla confezione | | — |
| to place | posizionare / appoggiare | | — |
| to lift | sollevare | | — |
| to pull out / extend | estrarre | `Estrai il telaio` | — |
| to retract / slide back in | far rientrare | | — |
| to attach / mount | fissare / montare | | — |
| to release / detach | sganciare / staccare | | — |
| to rotate | ruotare | | — |
| to tilt | inclinare | | — |
| to store | riporre | `Riponi lo Screenmate in un luogo sicuro` | — |
| to press | premere | `Premi il pulsante M` | — |
| press and hold | tieni premuto | never `premi e tieni` | — |
| short press | pressione breve | | — |
| long press | pressione prolungata | | — |
| to turn on / off | accendere / spegnere | | — |
| to navigate | navigare | `naviga nel menu` | — |
| to confirm | confermare | | — |
| to select | selezionare / scegliere | | — |
| to adjust / set | regolare / impostare | | — |
| to increase / decrease | aumentare / ridurre | | — |
| to extend the desktop | estendere il desktop | | — |
| to arrange (displays) | disporre | | — |
| to flicker | sfarfallare | `lo schermo sfarfalla` | — |
| to cut out | interrompersi | | — |
| unstable | instabile | | — |
| upside down | capovolto | `Schermo capovolto?` | — |
| included / supplied | in dotazione | `i cavi in dotazione`; `incluso` also acceptable | — |
| required | necessario | | — |
| optional | opzionale | | — |
| suitable | adatto | | — |
| compatible | compatibile | | — |
| at least | almeno | | — |
| provided that | a condizione che | + subjunctive | — |
| as soon as | non appena | | — |
| if necessary | se necessario | | — |
| for example / e.g. | ad esempio | | — |
| such as | come | | — |
| as shown in image 2 | come mostrato nell'immagine 2 | | — |
| in the direction shown | nella direzione indicata | | — |
| Note: | Nota: | `<Note>` lead-in | — |
| Please note: | Nota: | **same target as `Note:`** — "please" is dropped (§1.4). Deliberate collapse: the EN corpus uses both interchangeably for the identical callout | — |
| Important: | Importante: | `<Note>` lead-in | — |
| Important Information: | Informazioni importanti: | `<Note>` lead-in on the index pages; matches the `## Important Information` heading in §9.3 | — |
| Caution: | Attenzione: | | — |
| Warning | Avvertenza | `<Warning>` callout | — |
| Tip: | Suggerimento: | | — |
| Welcome! | Benvenuto! | | — |

---

## 6. Literal-translation traps

Word-by-word renderings that are wrong or unidiomatic in Italian.

| English | ✗ Wrong (literal) | ✓ Right (natural) |
|---|---|---|
| Make sure that X | `Fai sicuro che X` | `Assicurati che X` *(+ subjunctive: `che il cavo **sia** collegato`)* |
| Please read the following guidelines | `Per favore leggi le seguenti linee guida` | `Leggi attentamente le indicazioni seguenti` |
| Press and hold the button | `Premi e tieni il pulsante` | `Tieni premuto il pulsante` |
| Follow the on-screen instructions | `Segui le istruzioni sullo-schermo` | `Segui le istruzioni visualizzate sullo schermo` |
| Restart your laptop | `Ricomincia il tuo laptop` | `Riavvia il laptop` |
| Click 'Open' | `Clicca 'Apri'` | `Fai clic su 'Apri'` |
| Once both connections are made | `Una volta che entrambe le connessioni sono fatte` | `Quando entrambi i collegamenti sono stati effettuati` |
| Then proceed to step 5 | `Poi procedi allo step 5` | `Vai direttamente al passaggio 5` |
| Take good care of your Screenmate | `Prendi buona cura del tuo Screenmate` | `Abbi cura del tuo Screenmate` |
| Do not drop the monitor | `Non lasciare cadere giù il monitor` | `Non far cadere il monitor` |
| You'll need your password | `Avrai bisogno della tua password` | `Ti servirà la password` |
| Pick the one that matches your laptop | `Prendi quello che combacia con il tuo laptop` | `Scegli quella adatta al tuo laptop` |
| boost your productivity | `spingere la tua produttività` | `aumentare la tua produttività` |
| on the go | `sull'andare` | `ovunque ti trovi` / `in mobilità` |
| Need more overview? | `Hai bisogno di più panoramica?` | `Vuoi più spazio a schermo?` |
| Want to extend your workspace? | `Vuoi estendere il tuo spazio di lavoro?` | `Vuoi estendere lo spazio di lavoro?` |
| The screen stays black | `Lo schermo rimane nero` | `Lo schermo resta nero` |
| What could be the cause? | `Cosa potrebbe essere la causa?` | `Quale può essere la causa?` |
| What should I do? | `Cosa dovrei fare?` | `Cosa posso fare?` |
| to ease eye strain | `per alleviare lo sforzo dell'occhio` | `per ridurre l'affaticamento degli occhi` |
| for a snug fit | `per un adattamento accogliente` | `perché resti ben saldo` |
| Keep ventilation openings clear | `Tieni le aperture di ventilazione chiare` | `Non ostruire le aperture di ventilazione` |
| suited for watching films | `adatto per guardare film` | `ideale per guardare film` |
| the highlighted option | `l'opzione evidenziata in giallo` | `l'opzione evidenziata in giallo` *(correct — keep)* |
| lifespan | `durata della vita` | `durata` / `vita utile` |
| Scanning a QR code? | `Scansionando un codice QR?` | `Hai scansionato un codice QR?` |

**Connection vs. connessione.** `connessione` in Italian means a *network* connection. This corpus
is about physical cabling: use `collegamento` for the act/arrangement and `porta`/`cavo` for the
hardware. `Opzioni di collegamento`, never `Opzioni di connessione`.

---

## 7. OSD labels — verbatim, never translated

These strings are **engraved in the device firmware and render in English on the physical panel**.
Translating them in the manual would make the manual disagree with the hardware. Reproduce them
character-for-character, including capitalisation.

> **Scope of this section (gate ruling R1).** "Verbatim" applies to the **ALL-CAPS device tokens
> and preset values**, not to the chapter headings that name them. Every `##` / `###` heading in
> `osd.mdx` **is translated** — see §9.3 and §9.6. The NL precedent is the model:
> `### 1. Backlight` → NL `### 1. Achtergrondverlichting` → IT `### 1. Retroilluminazione`.
> Only the parenthesised caps label survives in English.

### 7.1 Locked ALL-CAPS labels (all 22 are in `dnt.json`)

```
ASPECT      BLUE        BRIGHTNESS      COLOR TEMP      CONTRAST
DCR         ECO         FPS             GREEN           HDR
HDR MODE    LANGUAGE    LOW BLUE LIGHT  ON/OFF          OSD TIMER
RED         RESET       RTS             SHARPNESS       SOURCE
TRANSPARENCY            WIDE
```

Also reproduce `COLOR TEMP.` with its trailing period where the source page has it
(`expand/osd.mdx`, `flip/osd.mdx`) — the period is part of the on-device string.

### 7.2 Additional on-device strings — also verbatim

Preset **values** that render on the panel (these are menu *options*, not chapter names):

```
Standard    Game    Movie   Text       Energy Saving
Warm        Cool    User
Off         Auto    2084
Type-C1     Type-C2     HDMI
4:3         16:9        WIDE
```

**Not in this list:** `Backlight`, `Image`, `Color`, `Settings`, `Reset`, `Other`. These are OSD
**chapter names**, and per R1 they are translated wherever they appear as a heading —
`Retroilluminazione`, `Immagine`, `Colore`, `Impostazioni`, `Ripristino`, `Altro`. `Backlight` was
removed from `dnt.json` in commit `12b31e3` precisely because it is context-dependent; do not
treat it as a protected token. Its spec-table homograph (`Backlight | LED`) takes the same
Italian target, `Retroilluminazione`.

### 7.2.1 Optional parenthetical device gloss

The NL pages sometimes append the EN device token to a translated OSD heading
(`### 1. Achtergrondverlichting (Backlight)`, `### 5. Resetten (Reset)`) and sometimes do not
(`### 1. Achtergrondverlichting`). Italian may do the same **where the EN or NL sibling page
carries the gloss**, giving `### 1. Retroilluminazione (Backlight)`. The translated word is
mandatory; the parenthetical is optional and must never appear alone.

### 7.3 Glossing pattern in body copy

The EN corpus writes OSD entries as `**Gloss (CAPS):** description` or `**CAPS:** description`.
Italian keeps the CAPS token untouched and translates only the gloss and the description:

| EN | ✓ IT |
|---|---|
| `**Brightness (BRIGHTNESS):** Adjust the screen brightness (0–100).` | `**Luminosità (BRIGHTNESS):** regola la luminosità dello schermo (0–100).` |
| `**Sharpness (SHARPNESS):** Adjust image sharpness (0–4).` | `**Nitidezza (SHARPNESS):** regola la nitidezza dell'immagine (0–4).` |
| `**DCR (Dynamic Contrast Ratio):** Turn dynamic contrast ON or OFF.` | `**DCR (Dynamic Contrast Ratio):** attiva o disattiva il contrasto dinamico (ON / OFF).` |
| `**Aspect (ASPECT):** Switch between **4:3** and **WIDE**.` | `**Formato (ASPECT):** alterna tra **4:3** e **WIDE**.` |
| `**Low Blue Light (LOW BLUE LIGHT):** Reduces the amount of blue light…` | `**Luce blu ridotta (LOW BLUE LIGHT):** riduce la quantità di luce blu…` |
| `**Language (LANGUAGE):** Choose the OSD language.` | `**Lingua (LANGUAGE):** scegli la lingua dell'OSD.` |
| `**OSD Timer (OSD TIMER):** …(10–60 seconds).` | `**Timer OSD (OSD TIMER):** …(10–60 secondi).` |
| `**Source (SOURCE):** Choose between two signal sources: Type-C1 / Type-C2 and HDMI.` | `**Sorgente (SOURCE):** scegli tra due sorgenti del segnale: Type-C1 / Type-C2 e HDMI.` |
| `**HDR Mode (HDR MODE):** Enable HDR (High Dynamic Range)… Available modes: Off, Auto, 2084.` | `**Modalità HDR (HDR MODE):** attiva l'HDR (High Dynamic Range)… Modalità disponibili: Off, Auto, 2084.` |
| `**ECO mode (ECO):** Preset display modes (Standard, Game, Movie, Text, FPS, RTS, Energy Saving).` | `**Modalità ECO (ECO):** modalità immagine predefinite (Standard, Game, Movie, Text, FPS, RTS, Energy Saving).` |
| `**Reset (RESET):** Choose RESET to restore all settings to factory defaults.` | `**Ripristino (RESET):** scegli RESET per riportare tutte le impostazioni ai valori di fabbrica.` |

Where the EN uses only the CAPS token with no gloss (`**BRIGHTNESS (0–100):**`, dual-flip),
keep the CAPS token alone — do not add an Italian gloss the EN page does not have. Structural
parity with EN takes precedence.

#### 7.3.1 Gloss vocabulary

The Italian words used *as* the gloss. The CAPS token beside them never changes.

| EN gloss | Italian |
|---|---|
| Brightness | Luminosità |
| Contrast | Contrasto |
| Sharpness | Nitidezza |
| Black Level | Livello del nero |
| Aspect / Aspect Ratio | Formato / Rapporto d'aspetto |
| Color Temperature / Color Temp. | Temperatura colore |
| Red | Rosso |
| Green | Verde |
| Blue | Blu |
| Language | Lingua |
| OSD Timer | Timer OSD |
| Transparency | Trasparenza |
| Source | Sorgente |
| Reset | Ripristino |
| HDR Mode | Modalità HDR |
| Low Blue Light | Luce blu ridotta |
| ECO mode / ECO Mode / ECO modes | Modalità ECO *(EN casing varies by product — one Italian target)* |

The **preset values** beside these glosses (`Standard`, `Game`, `Movie`, `Text`, `Energy Saving`,
`Warm`, `Cool`, `User`, `Off`, `Auto`, `2084`) stay English — see §7.2.

### 7.4 The OSD language list is lowercase in Italian

Language names are **not** capitalised in Italian.

| EN | ✓ IT |
|---|---|
| `Available languages: English, French, German, Simplified Chinese, Italian, Spanish, Portuguese, Turkish, Polish, Dutch, Japanese, Korean.` | `Lingue disponibili: inglese, francese, tedesco, cinese semplificato, italiano, spagnolo, portoghese, turco, polacco, olandese, giapponese, coreano.` |

---

## 8. OS-specific UI labels

These must match what the reader actually sees in an **Italian-language** OS. Screenshots stay
English on all language pages (client decision, inherited from the NL rules) — this table governs
**label text in prose only**.

| Context | EN | IT (matches OS UI) |
|---|---|---|
| Windows | Display settings | `Impostazioni schermo` |
| Windows | Extend desktop to this display | `Estendi il desktop a questo schermo` |
| Windows | Identify | `Identifica` |
| Windows | Display orientation | `Orientamento dello schermo` |
| Windows | Flipped | `Capovolto` |
| Windows | Mirrored *(superseded — EN pages now say "Flipped")* | `Duplicato` |
| Windows | Scale | `Ridimensionamento` |
| Windows | Scale and layout | `Ridimensionamento e layout` |
| Windows | This PC | `Questo PC` |
| Windows | taskbar | `barra delle applicazioni` |
| Windows | Sound settings | `Impostazioni audio` |
| Windows | output device | `dispositivo di output` |
| macOS | System Settings / System Preferences | `Impostazioni di Sistema` / `Preferenze di Sistema` |
| macOS | Displays | `Schermi` |
| macOS | Arrange / Arrangement | `Disponi` / `Disposizione` |
| macOS | Privacy & Security / Security & Privacy | `Privacy e sicurezza` |
| macOS | Screen & System Audio Recording | `Registrazione schermo e audio di sistema` |
| macOS | Screen Recording | `Registrazione schermo` |
| macOS | Applications | `Applicazioni` |
| macOS | Open | `Apri` |
| macOS | Rotation | `Rotazione` |
| macOS | Standard | `Standard` |
| macOS | Sound | `Suono` |
| macOS | Output | `Uscita` |
| macOS | Apple menu | `menu Apple` |
| macOS | menu bar | `barra dei menu` |
| macOS | Launchpad | `Launchpad` |

**Note on the NL parenthetical pattern.** Several EN pages carry a Dutch gloss inline —
`**Display settings** ('Beeldscherminstellingen')`, `**This PC** ('Deze pc')`. On Italian pages
these become the Italian OS label in the same slot:
`**Display settings** ('Impostazioni schermo')`, `**This PC** ('Questo PC')`. Never leave a Dutch
string on an Italian page.

**Verification status:** these renderings follow current Microsoft and Apple Italian localisation.
Flagged in §9 for a native-speaker / live-OS confirmation pass before publication.

---

## 9. Document & section names

Locked renderings for every frontmatter `title` and every `##` / `###` heading in the EN corpus
(`en/manuals-index.mdx` + `en/manuals/*/*.mdx`, 62 files).

**Casing:** Italian headings use **sentence case** — capitalise only the first word plus proper
nouns, product names, OS names and protected tokens. EN uses title case; do not carry it over.
`Porte e pulsanti` ✓ · `Porte E Pulsanti` ✗.

**Structural punctuation is preserved.** Where an EN heading carries an em dash (`M — OSD Menu
Button`, `Option 1 — USB-C`, `Dual screen — front and back horizontal`) or a leading number, keep
the punctuation and the numbering exactly while translating the words:
`### 1. Backlight` → `### 1. Retroilluminazione`.

### 9.1 Frontmatter titles

| English | Italian |
|---|---|
| Screenmate Product Manuals | Manuali dei prodotti Screenmate |
| Screenmate OneCable Manual | Manuale Screenmate OneCable |
| Screenmate Lite Manual | Manuale Screenmate Lite |
| Screenmate Lite 144 Hz Manual | Manuale Screenmate Lite 144 Hz |
| Screenmate Dual Flip Manual | Manuale Screenmate Dual Flip |
| Screenmate Flip Manual | Manuale Screenmate Flip |
| Screenmate Expand Manual | Manuale Screenmate Expand |
| Screenmate Infinity Manual | Manuale Screenmate Infinity |
| Screenmate Infinity Lite Manual | Manuale Screenmate Infinity Lite |
| Screenmate One 4K Manual | Manuale Screenmate One 4K |
| Screenmate One 4K OLED Manual | Manuale Screenmate One 4K OLED |
| Screenmate Panorama Manual | Manuale Screenmate Panorama |
| Installation | Installazione |
| Installation Windows | Installazione Windows |
| Installation macOS | Installazione macOS |
| Ports and Buttons | Porte e pulsanti |
| Ports and Controls | Porte e comandi |
| On-Screen Menu (OSD) | Menu a schermo (OSD) |
| Display Settings | Impostazioni schermo |
| Display & Sound Settings | Impostazioni schermo e audio |
| Safety Instructions | Istruzioni di sicurezza |
| FAQ | FAQ |

### 9.2 Frontmatter descriptions

| English | Italian |
|---|---|
| Digital manuals for all Screenmate products | Manuali digitali di tutti i prodotti Screenmate |
| Complete user manual for your Screenmate OneCable portable monitor | Manuale d'uso completo del tuo monitor portatile Screenmate OneCable |
| Complete user manual for your Screenmate Lite portable monitor | Manuale d'uso completo del tuo monitor portatile Screenmate Lite |
| Complete user manual for your Screenmate Lite 144 Hz portable monitor | Manuale d'uso completo del tuo monitor portatile Screenmate Lite 144 Hz |
| Complete user manual for your Screenmate One 4K 15.6" portable monitor | Manuale d'uso completo del tuo monitor portatile Screenmate One 4K 15,6" |
| Complete user manual for your Screenmate One 4K OLED 15.6" portable monitor | Manuale d'uso completo del tuo monitor portatile Screenmate One 4K OLED 15,6" |
| Complete user manual for your Screenmate Dual Flip 16" foldable dual-screen extension | Manuale d'uso completo della tua estensione pieghevole a doppio schermo Screenmate Dual Flip 16" |
| Complete user manual for your Screenmate Flip — available in 14" and 15.6" | Manuale d'uso completo del tuo Screenmate Flip — disponibile da 14" e 15,6" |
| Complete user manual for your Screenmate Expand triple-screen portable monitor, available in 14" and 15.6" | Manuale d'uso completo del tuo monitor portatile a tre schermi Screenmate Expand, disponibile da 14" e 15,6" |
| Complete user manual for your Screenmate Infinity dual portable monitor | Manuale d'uso completo del tuo doppio monitor portatile Screenmate Infinity |
| Complete user manual for your Screenmate Infinity Lite portable display extension | Manuale d'uso completo della tua estensione schermo portatile Screenmate Infinity Lite |
| Complete user manual for your Screenmate Panorama 15.6" triple-screen portable monitor | Manuale d'uso completo del tuo monitor portatile a tre schermi Screenmate Panorama 15,6" |
| Setting up and connecting your Screenmate Dual Flip / Expand / Infinity / Panorama | Montaggio e collegamento del tuo Screenmate {Prodotto} |
| Connecting your Screenmate Lite / Lite 144 Hz / One 4K / One 4K OLED | Collegamento del tuo Screenmate {Prodotto} |
| Installation and connecting your Screenmate OneCable | Installazione e collegamento del tuo Screenmate OneCable |
| Unfolding, connecting and storing your Screenmate Flip | Apertura, collegamento e come riporre il tuo Screenmate Flip |
| Unfolding, setting up and storing your Screenmate Infinity Lite | Apertura, montaggio e come riporre il tuo Screenmate Infinity Lite |
| Overview of ports and control buttons | Panoramica delle porte e dei pulsanti di comando |
| Overview of ports and the multifunctional button | Panoramica delle porte e del pulsante multifunzione |
| Driver installation for Windows | Installazione del driver per Windows |
| Driver installation for macOS | Installazione del driver per macOS |
| Display settings for Windows and macOS | Impostazioni schermo per Windows e macOS |
| Configuring your displays on Windows and macOS | Configurazione degli schermi su Windows e macOS |
| Configure display and sound output on Windows and macOS | Configurazione dello schermo e dell'audio su Windows e macOS |
| Configuring extra screens and audio output on Windows and macOS | Configurazione degli schermi aggiuntivi e dell'audio su Windows e macOS |
| Display settings via the on-screen menu | Impostazioni schermo dal menu a schermo |
| Adjusting display settings via the on-screen menu | Regolazione delle impostazioni schermo dal menu a schermo |
| Per-screen display settings via the on-screen menu | Impostazioni schermo per singolo schermo dal menu a schermo |
| Frequently asked questions and troubleshooting | Domande frequenti e risoluzione dei problemi |
| Important safety information and warnings | Informazioni di sicurezza e avvertenze importanti |

### 9.3 `##` headings

| English | Italian |
|---|---|
| *(H1)* Welcome to Screenmate Manuals | Benvenuto nei manuali Screenmate |
| Available Manuals | Manuali disponibili |
| Need Help? | Serve aiuto? |
| What is the Screenmate OneCable? | Che cos'è lo Screenmate OneCable? |
| What is the Screenmate Lite? | Che cos'è lo Screenmate Lite? |
| What is the Screenmate Lite 144 Hz? | Che cos'è lo Screenmate Lite 144 Hz? |
| What is the Screenmate Dual Flip? | Che cos'è lo Screenmate Dual Flip? |
| What is the Screenmate Flip? | Che cos'è lo Screenmate Flip? |
| What is the Screenmate Expand? | Che cos'è lo Screenmate Expand? |
| What is the Screenmate Infinity? | Che cos'è lo Screenmate Infinity? |
| What is the Screenmate Infinity Lite? | Che cos'è lo Screenmate Infinity Lite? |
| What is the Screenmate One 4K? | Che cos'è lo Screenmate One 4K? |
| What is the Screenmate One 4K OLED? | Che cos'è lo Screenmate One 4K OLED? |
| What is the Screenmate Panorama? | Che cos'è lo Screenmate Panorama? |
| Package Contents | Contenuto della confezione |
| Technical Specifications | Specifiche tecniche |
| Important Information | Informazioni importanti |
| Getting Started | Per iniziare |
| Choose Your Cables | Scegli i cavi |
| Protective Cap | Cappuccio protettivo |
| Installation Instructions | Istruzioni di installazione |
| Installation Steps | Fasi di installazione |
| Physical Setup | Montaggio |
| Setup | Montaggio |
| Unfolding the Screens | Apertura degli schermi |
| Install the Display Driver | Installa il driver dello schermo |
| Connection Options | Opzioni di collegamento |
| Using with 2 USB Cables | Uso con 2 cavi USB |
| Charging the Screenmate OneCable | Ricarica dello Screenmate OneCable |
| Storage | Come riporre il prodotto |
| Storing the Screenmate | Come riporre lo Screenmate |
| Driver Installation for Windows | Installazione del driver per Windows |
| Driver Installation for macOS | Installazione del driver per macOS |
| If the Driver Doesn't Work | Se il driver non funziona |
| Ports and Buttons | Porte e pulsanti |
| Buttons and Functions | Pulsanti e funzioni |
| Controls and OSD Menu | Comandi e menu OSD |
| On-Screen Menu (OSD) | Menu a schermo (OSD) |
| On-Screen Menu Settings | Impostazioni del menu a schermo |
| Introduction to the OSD | Introduzione all'OSD |
| Using the OSD | Uso dell'OSD |
| Using the OSD Menu | Uso del menu OSD |
| OSD Settings | Impostazioni OSD |
| Per-Screen Settings | Impostazioni per singolo schermo |
| Backlight *(OSD page)* | Retroilluminazione |
| Image *(OSD page)* | Immagine |
| Color *(OSD page)* | Colore |
| Settings *(OSD page)* | Impostazioni |
| Reset *(OSD page)* | Ripristino |
| Other *(OSD page)* | Altro |
| Display Configuration | Configurazione dello schermo |
| Display Configuration Windows | Configurazione dello schermo Windows |
| Display Configuration macOS | Configurazione dello schermo macOS |
| Display Configuration (OS-Level) | Configurazione dello schermo (a livello di sistema operativo) |
| Display Settings | Impostazioni schermo |
| Arrange Your Displays (Video) | Disponi gli schermi (video) |
| Sound Settings | Impostazioni audio |
| FAQ | FAQ |
| Safety Instructions | Istruzioni di sicurezza |

### 9.4 `###` headings — ports, buttons & controls

| English | Italian |
|---|---|
| Ports | Porte |
| Side Ports | Porte laterali |
| USB-C | USB-C |
| USB-C Port | Porta USB-C |
| USB-C Port (Power) | Porta USB-C (alimentazione) |
| USB-C Port (Power & Video) | Porta USB-C (alimentazione e video) |
| USB-C Port (Data/Video/Power) | Porta USB-C (dati/video/alimentazione) |
| USB-C Port (Power Only / Power Delivery) | Porta USB-C (solo alimentazione / Power Delivery) |
| USB-C Charging Port | Porta USB-C di ricarica |
| USB-C (for HDMI > USB-C) | USB-C (per il cavo da HDMI a USB-C) |
| USB-A Port | Porta USB-A |
| HDMI Port | Porta HDMI |
| Mini HDMI | Mini-HDMI |
| Mini HDMI Port | Porta Mini-HDMI |
| 3 × Mini HDMI Ports | 3 × porte Mini-HDMI |
| 3.5mm Headphone Jack / 3.5 mm Headphone Jack | Jack per cuffie da 3,5 mm |
| Speaker | Altoparlante |
| Indicator Light | Spia luminosa |
| LED Indicator | Indicatore LED |
| Buttons | Pulsanti |
| Control Buttons | Pulsanti di comando |
| Brightness Buttons | Pulsanti della luminosità |
| Power Button | Pulsante di accensione |
| Power & Return Button | Pulsante di accensione e ritorno |
| Menu Button (Power / OSD) | Pulsante Menu (accensione / OSD) |
| Menu / Selection / Confirm Button | Pulsante Menu / Selezione / Conferma |
| Menu / Select / Confirm | Menu / Selezione / Conferma |
| Confirm / Exit Button | Pulsante Conferma / Esci |
| Multifunctional Button | Pulsante multifunzione |
| Scroll Wheel | Rotella di scorrimento |
| M — OSD Menu Button | M — pulsante del menu OSD |
| + and − Buttons | Pulsanti + e − |
| + Button (Increase Brightness) | Pulsante + (aumenta la luminosità) |
| − Button (Decrease Brightness) | Pulsante − (riduce la luminosità) |
| Up Button (+) | Pulsante Su (+) |
| Down Button (−) | Pulsante Giù (−) |
| Left "Min" Button | Pulsante sinistro "Min" |
| Right "Plus" Button | Pulsante destro "Plus" |
| OSD Lock | Blocco dell'OSD |
| Opening the OSD Menu | Apertura del menu OSD |
| Volume and Brightness Shortcuts | Scorciatoie per volume e luminosità |
| Brightness and volume | Luminosità e volume |
| Adjusting Brightness | Regolazione della luminosità |
| Adjusting Volume | Regolazione del volume |

### 9.5 `###` headings — installation, connection & storage

| English | Italian |
|---|---|
| Flip 14" | Flip 14" |
| Flip 15.6" | Flip 15,6" |
| Windows | Windows |
| macOS | macOS |
| Windows 10 or higher | Windows 10 o versioni successive |
| Download Drivers | Scarica i driver |
| Download Driver for macOS | Scarica il driver per macOS |
| Manual Installation (if needed) | Installazione manuale (se necessaria) |
| Installation Steps | Fasi di installazione |
| Setup instructions | Istruzioni di montaggio |
| Unfolding the screen | Apertura dello schermo |
| Folding the screen back up | Come richiudere lo schermo |
| Folding caution | Attenzione durante la chiusura |
| Possible layouts | Configurazioni possibili |
| Single screen | Schermo singolo |
| Dual screen — front and back horizontal | Doppio schermo — davanti e dietro in orizzontale |
| Dual screen — front and back vertical | Doppio schermo — davanti e dietro in verticale |
| Smartphones and game consoles | Smartphone e console di gioco |
| Connect the Screenmate Infinity Lite to your laptop | Collega lo Screenmate Infinity Lite al laptop |
| Connect the Screenmate to your phone or other devices | Collega lo Screenmate al telefono o ad altri dispositivi |
| Option 1 — USB-C (single cable) | Opzione 1 — USB-C (cavo singolo) |
| Option 2 — USB-A + HDMI | Opzione 2 — USB-A + HDMI |
| 1. Two USB-C Cables / 1. Two USB-C cables | 1. Due cavi USB-C |
| 1. Dual USB-C connection | 1. Collegamento doppio USB-C |
| 2. One USB-C Cable, One HDMI Cable and One USB-A Cable | 2. Un cavo USB-C, un cavo HDMI e un cavo USB-A |
| 2. One USB-C cable, one HDMI cable, and one USB-A cable | 2. Un cavo USB-C, un cavo HDMI e un cavo USB-A |
| 2. 1x USB-C, 1x HDMI and 1x USB-A | 2. 1 USB-C, 1 HDMI e 1 USB-A |
| 2. USB-C + HDMI & USB-A connection | 2. Collegamento USB-C + HDMI e USB-A |
| 3. 2x USB-A and 2x HDMI | 3. 2 USB-A e 2 HDMI |
| 1. Laptop via USB-C cable | 1. Laptop tramite cavo USB-C |
| 2. Laptop via HDMI cable | 2. Laptop tramite cavo HDMI |
| 3. Phone or tablet via USB-C cable | 3. Telefono o tablet tramite cavo USB-C |
| 4. USB-C game console | 4. Console di gioco USB-C |
| 5. Devices with an HDMI port | 5. Dispositivi con porta HDMI |
| 1. Release the screen from the stand | 1. Sgancia lo schermo dal supporto |
| 2. Attach the main stand | 2. Fissa il supporto principale |
| 3. Mount the screen support | 3. Monta il sostegno dello schermo |
| 4. Pull out the frame | 4. Estrai il telaio |
| 5. Adjust the stand | 5. Regola il supporto |
| 6. Open the screens | 6. Apri gli schermi |
| 7. Close the screens | 7. Chiudi gli schermi |
| Read this before use | Leggi prima dell'uso |
| Check before use | Controlla prima dell'uso |
| Before use | Prima dell'uso |

### 9.6 `###` headings — OSD sections

Per gate ruling R1, **every** OSD chapter heading is translated. The ALL-CAPS device token stays
English only inside the body-copy gloss (§7.3) or an optional parenthetical (§7.2.1).

| English | Italian |
|---|---|
| 1. Backlight | 1. Retroilluminazione |
| 1. Brightness | 1. Luminosità |
| 2. Image | 2. Immagine |
| 2. Image Modes | 2. Modalità immagine |
| 3. Color | 3. Colore |
| 3. Color Settings | 3. Impostazioni colore |
| 4. OSD Settings | 4. Impostazioni OSD |
| 4. Settings | 4. Impostazioni |
| 5. Reset | 5. Ripristino |
| 6. Other | 6. Altro |

### 9.7 `###` headings — FAQ questions

| English | Italian |
|---|---|
| My screen stays black and there's no image after connecting. What should I do? | Lo schermo resta nero e non compare nessuna immagine dopo il collegamento. Cosa posso fare? |
| The screen is unstable, flickers or occasionally cuts out. What could be the cause? | Lo schermo è instabile, sfarfalla o si interrompe di tanto in tanto. Quale può essere la causa? |
| My laptop doesn't have a USB-C port. How can I still use the Screenmate? | Il mio laptop non ha una porta USB-C. Posso comunque usare lo Screenmate? |
| A startup logo appears, but there's no image on my MacBook. What should I do? | Compare il logo di avvio, ma sul MacBook non c'è nessuna immagine. Cosa posso fare? |
| Can the Screenmate charge my laptop when connected to a power source? | Lo Screenmate può ricaricare il mio laptop quando è collegato a una fonte di alimentazione? |

### 9.8 Card titles (`manuals-index.mdx`)

| English | Italian |
|---|---|
| OneCable Manual … Panorama Manual | Manuale OneCable … Manuale Panorama *(pattern: `Manuale {Product}`)* |
| Contact Support | Contatta l'assistenza |
| Get help from our support team | Ricevi aiuto dal nostro team di assistenza |
| Shop Products | Acquista i prodotti |
| Browse all Screenmate products | Sfoglia tutti i prodotti Screenmate |
| Warranty Info | Informazioni sulla garanzia |
| Learn about product warranties | Scopri le garanzie sui prodotti |
| Scanning a QR code? | Hai scansionato un codice QR? |

### 9.9 JSX-embedded user-visible strings

**Why this table exists:** these strings render to the reader but live inside JSX elements, so
they are invisible to a `^#` heading grep and to a frontmatter grep. They are the single easiest
class of string to leave untranslated. Sweep them explicitly on every page.

**Translate** these JSX slots: `<a>` link text · `<Tab title="…">` · `<Card title="…">` ·
`<Card>` body text · `<p>` / `<div>` text children (image captions, package-contents labels) ·
`<video>` fallback text · button labels.

**Never translate:** `className` · `href` · `src` · `icon` · `alt` *(user-visible, but translated
per page by the translator against the page's own context — not glossary-locked)* ·
anything inside an MDX comment `{/* … */}` *(never rendered)*.

#### Link and button text

| English | Italian | Source |
|---|---|---|
| Download Windows Drivers | Scarica i driver per Windows | `onecable/installation-windows.mdx` `<a>` |
| Download for macOS | Scarica per macOS | `onecable/installation-mac.mdx` `<a>` |

#### Tab titles — inch marks must stay `&quot;`-escaped

> **Parse hazard.** In a JSX attribute the inch mark is written `&quot;`, never a literal `"` —
> a literal double quote closes the attribute and **breaks the MDX build**. Copy the escaped form
> exactly. The decimal comma still applies *inside* the escaped string: the NL pages literally
> ship `<Tab title="Expand 15,6&quot;">`, verified against `nl/manuals/expand/index.mdx`.

| English (source form) | Italian (locked, escaped) |
|---|---|
| `Expand 14&quot;` | `Expand 14&quot;` |
| `Expand 15.6&quot;` | `Expand 15,6&quot;` |
| `Flip 14&quot;` | `Flip 14&quot;` |
| `Flip 15.6&quot;` | `Flip 15,6&quot;` |
| `OneCable 14&quot;` | `OneCable 14&quot;` |
| `OneCable 16&quot;` | `OneCable 16&quot;` |
| `Windows` | `Windows` *(DNT)* |
| `macOS` | `macOS` *(DNT)* |

**Context rule — the same product size is written two different ways:**

| Context | Form | Example |
|---|---|---|
| JSX attribute (`<Tab title="…">`, `<Card title="…">`) | `&quot;` | `<Tab title="Flip 15,6&quot;">` |
| Markdown heading, body prose, spec table | literal `"` | `### Flip 15,6"` · `monitor portatile da 15,6"` |

§9.5 and §4.5 give the literal-`"` heading and prose forms; this table gives the JSX-attribute
forms. Both carry the decimal comma — only the quote character differs.

#### Image captions and figure labels (`<p className="…">` children)

| English | Italian | Source |
|---|---|---|
| Landscape view | Vista orizzontale | `infinity/installation.mdx` |
| Portrait view | Vista verticale | `infinity/installation.mdx` |
| Portrait & landscape combination | Combinazione verticale e orizzontale | `infinity/installation.mdx` |
| Detached view | Vista separata | `infinity/installation.mdx` |
| Place the screen on the single stand | Appoggia lo schermo sul supporto singolo | `infinity/installation.mdx` |
| The stand supports 360° rotation | Il supporto ruota di 360° | `infinity/installation.mdx` |
| USB-C · HDMI · USB-A · USB-A 2.0 | *(unchanged — **DNT**, connector names)* | `flip/`, `infinity/installation.mdx` port-icon captions |

#### Package-contents captions (`onecable/index.mdx`)

These are JSX `<p>` children, **not** the markdown bullet lists the other products use.

| English | Italian |
|---|---|
| Protective Case | Custodia protettiva |
| 2x USB-A > USB-C Cable | 2 cavi da USB-A a USB-C |
| USB-C > USB-C Cable | Cavo da USB-C a USB-C |
| USB Stick (Incl. Driver) | Chiavetta USB (con driver) |

The two cable captions follow the §2.5 chain rule — the `>` renders as `da … a …`, exactly like
`to`. Sentence case applies: `Cavo da USB-C a USB-C`, not `Cavo Da USB-C A USB-C`.

#### Boilerplate

| English | Italian | Occurrences |
|---|---|---|
| Your browser does not support the video tag. | Il tuo browser non supporta il tag video. | 14 — 2× in each of the six `display-settings.mdx`, 1× each in `onecable/installation-windows.mdx` and `-mac.mdx` |

#### Callout lead-ins (bare text children of `<Note>` / `<Warning>`)

These are bold bare-text children, not attributes, so they escape an attribute-oriented sweep.
They recur across products and must read identically everywhere — full renderings in §5.5.

| English | Italian | Where |
|---|---|---|
| `**Important Information:**` | `**Informazioni importanti:**` | index pages of dual-flip, expand, flip, infinity-lite, onecable (5×) |
| `**Please note:**` | `**Nota:**` | `flip/installation.mdx` (1×) — collapses onto the same target as `**Note:**` |
| `**Note:**` · `**Important:**` · `**Caution:**` · `**Tip:**` · `**Welcome!**` | `**Nota:**` · `**Importante:**` · `**Attenzione:**` · `**Suggerimento:**` · `**Benvenuto!**` | throughout |

The bold markers are structural — carry them over exactly, colon included.

#### Bold run-in labels (body copy)

Same escape route as the callout lead-ins: bold bare text, not attributes. These are the non-OSD
ones (OSD run-ins are governed by the §7.3 glossing pattern and §7.3.1 vocabulary).

| English | Italian | Where |
|---|---|---|
| `**Turn on:**` | `**Accensione:**` | `one-4k`, `one-4k-oled` osd |
| `**Open the OSD menu:**` | `**Apertura del menu OSD:**` | idem |
| `**Navigate:**` | `**Navigazione:**` | idem |
| `**Select:**` | `**Selezione:**` | idem |
| `**Adjust settings:**` | `**Regolazione delle impostazioni:**` | idem |
| `**Go back:**` | `**Indietro:**` | idem |
| `**Short press:**` | `**Pressione breve:**` | controls pages |
| `**Long press:**` | `**Pressione prolungata:**` | controls pages |
| `**Long press (1 second):**` | `**Pressione prolungata (1 secondo):**` | `panorama/controls` |
| `**Press and hold (2 seconds):**` | `**Tieni premuto (2 secondi):**` | `infinity/controls` |
| `**Press and hold (3 seconds):**` | `**Tieni premuto (3 secondi):**` | idem |
| `**Press right ("Plus"):**` | `**Premi a destra ("Plus"):**` | idem |
| `**Press left ("Min"):**` | `**Premi a sinistra ("Min"):**` | idem |
| `**Power supply:**` | `**Alimentazione:**` | lite / lite-144hz / one-4k installation |
| `**Connecting the console:**` | `**Collegamento della console:**` | idem |
| `**Connecting the HDMI device:**` | `**Collegamento del dispositivo HDMI:**` | idem |
| `**Steps:**` | `**Procedura:**` | `expand/installation` |
| `**Extend your workspace:**` | `**Estendi lo spazio di lavoro:**` | `panorama/osd` |
| `**Left screen:**` / `**Right screen:**` | `**Schermo sinistro:**` / `**Schermo destro:**` | `expand/index`, `flip/index` |
| `**USB-C Port:**` · `**Mini HDMI:**` | `**Porta USB-C:**` · `**Mini-HDMI:**` | `flip/controls` |

#### Ruled DNT — not user-visible

| String | Ruling |
|---|---|
| `[Product Name] Manual` | inside `{/* … */}` in `manuals-index.mdx` — an authoring template for future products, never rendered. Leave verbatim. |
| `Brief product description` | same commented-out `<Card>` template. Leave verbatim. |
| `https://www.siliconmotion.com/downloads/index.html` | URL used as both link text and target in `panorama/installation.mdx`. Leave verbatim. |
| `Win10&11` · `DRIVERS (D:)` · `UsbDisplay` · `RacerUSB` · `S6-L` · `S6-R` | literal UI/file strings appearing in prose and `alt` text — see §4.3 and §5.3. |

---

## 10. Punctuation, quotes & typography

- **Quotes around UI strings:** straight ASCII single quotes `'…'`, matching the EN and NL pages —
  `scegli 'Estendi il desktop a questo schermo'`. Do **not** use Italian caporali `«…»` and do not
  use curly quotes; structural parity with the EN pages wins.
- **Apostrophe:** straight ASCII `'`, no space after it (`dell'OSD`, `l'alimentazione`).
- **Em dash `—`:** preserve it where an EN **heading** already has one (§9). Avoid introducing it
  into body copy; use `–` (en dash) with spaces, or a comma.
- **En dash `–`:** ranges and parenthetical interruptions.
- **Colon before a list:** lowercase after the colon (`Lingue disponibili: inglese, francese, …`).
- **Sentence-final double space:** never. Single space only.
- **`&`:** translate to `e` in prose and headings (`Privacy & Security` is an OS label and keeps its
  own Italian form, see §8). Exception: literal file/folder names (`Win10&11`) stay verbatim.
- **`/` in labels:** keep, with spaces where EN has them (`Menu / Selezione / Conferma`,
  `dati/video/alimentazione` closed up as EN does).
- **Bold and italics** carry over position-for-position from the EN source. Do not add or remove
  emphasis.
- **MDX components** (`<Note>`, `<Warning>`, `<Info>`, `<Tip>`, `<Tabs>`, `<Tab title="…">`,
  `<Card title="…">`, `className`, `href`, `src`, `icon`) are code: translate only the visible
  string attributes (`title`) and the visible text children (callout body, `<Card>` body, `<p>`
  captions, `<a>` link text, `<video>` fallback). Never translate `icon`, `href`, `src`,
  `className` or image filenames. **Full inventory of the JSX-embedded strings in this corpus,
  with locked renderings: §9.9.**
- **`alt` text** is user-visible and **is** translated — per page, against that page's context.
  It is deliberately not glossary-locked, because the same image carries different `alt` copy
  across products.
- **MDX comments `{/* … */}` are never rendered** — leave their contents verbatim, including the
  commented-out `<Card>` template in `manuals-index.mdx` and the `TODO: confirm with Louie` notes
  in `one-4k-oled/`.
- **Frontmatter keys** (`title`, `description`, `icon`, `nl_link` / `it_link`) are never translated;
  only their string values, and only `title` and `description`.

---

## 11. Decision log

### 11.1 Resolved at the glossary gate — binding

1. **All OSD chapter headings translate (ruling R1).** `Backlight` was removed from `dnt.json` in
   commit `12b31e3` as context-dependent. There is no split treatment: `Backlight` →
   `Retroilluminazione` in **every** position — OSD chapter heading and spec-table field alike.
   `Reset` → `Ripristino` as a heading, matching the NL precedent `Resetten`. Only the ALL-CAPS
   device token stays English, and only inside a body-copy gloss (§7.3) or the optional
   parenthetical (§7.2.1). The OSD chapter therefore reads fully Italian:
   `Retroilluminazione / Immagine / Colore / Impostazioni / Ripristino / Altro`.
2. **`Download Drivers` → `Scarica i driver` (ruling R3).** Confirmed. The NL keep-EN heading is an
   anomaly being raised with the client, not a precedent. The DNT token is now `DRIVERS`
   (uppercase), which covers only the literal `DRIVERS (D:)` volume label of the bundled USB stick
   — it never applies to the word "driver" in prose or headings, where Italian uses the invariable
   `il driver` / `i driver`.
3. **`reverse charging` → `ricarica inversa` with an EN gloss on first use.** Confirmed, client
   sign-off noted.
4. **`100.000:1`.** Confirmed. Italian point separator for the corpus's single six-digit figure;
   every other figure is ≤ 4 digits and takes no separator.
5. **SI unit spacing** (`45 W`, `5 V`, `2 A`, `-20 °C`, with `180°` and `150%` closed up).
   Accepted as a deliberate per-language divergence from the NL glossary's closed-up forms.
6. **`DisplayPort`** is now a DNT token; already marked Keep EN ✓ in §5.2 alongside
   `DisplayPort Alt Mode`.

### 11.2 Carried to the delivery doc — client ask

7. **OS UI labels need a live-OS confirmation pass** (§8). They follow current Microsoft/Apple
   Italian localisation as documented, but Windows 11 in particular has renamed
   `Impostazioni schermo` / `Ridimensionamento` across builds. Routed to the delivery doc as a
   client verification item.

### 11.3 Translator-facing notes — no action required

8. **`Storage` → two targets.** `## Storage` (dual-flip, infinity) is locked as
   `Come riporre il prodotto` and `## Storing the Screenmate` (flip) as
   `Come riporre lo Screenmate`. Italian has no natural one-word noun for this sense
   (`Conservazione` reads industrial, `Immagazzinamento` is warehousing), so both are verb phrases.
   Deliberate.

---

## 12. Adding to the glossary

If you encounter a term not listed here, propose an addition — do not improvise silently.

```
Proposed glossary addition:
| {English} | {Italian} | {notes} | {keep EN?} |
Reason: {file:line where it appears + why this Italian rendering}
```
