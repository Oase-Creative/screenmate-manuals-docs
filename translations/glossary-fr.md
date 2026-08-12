# Screenmate EN→FR Glossary (locked)

Locked terminology for all Screenmate French copy. Use these exact French renderings unless
the English term is intentionally retained (column "Keep EN?" = ✓). The "Keep EN?" column is
seeded from `translations/dnt.json` — anything in that file is do-not-translate by default.

This file is **binding** for every Phase 2 French translation task. If a term is missing, do not
improvise silently: propose an addition using the template in §12.

**Corpus this glossary was built from** (2026-08-11, branch `lang-expansion-de-fr-it`):
`en/manuals/**/*.mdx` (61 files) + `en/manuals-index.mdx` — 22 unique frontmatter titles,
36 unique frontmatter descriptions, 1 H1, 55 unique H2, 107 unique H3.

---

## 0. Precedence order

When two rules appear to conflict, apply them in this order:

1. `translations/dnt.json` — do-not-translate tokens win over everything.
2. On-device / OS-UI strings (§7, §8) — must match what the user physically sees.
3. **Already-shipped, QC'd FR pages.** Where a string is already live in `fr/` and this glossary
   says something different, **the shipped page wins** and the glossary is amended to match — not
   the reverse. Sections written after a chapter shipped can and did diverge from it (§10.1.F is
   the worked example). Never edit a shipped page to satisfy a later glossary lock.
4. This glossary's term tables (§5) and section-name tables (§9).
5. The typography and number rules (§3, §4).
6. General French usage.

The canonical shipped references are `fr/manuals/onecable/display-settings.mdx` and
`fr/manuals/onecable/safety.mdx`. The display-settings body is byte-identical across onecable,
dual-flip, flip and expand (verified — only the `description:` frontmatter differs on `flip`, which
faithfully mirrors an EN frontmatter difference), so any change there must land on all four at once.

Structural parity with `en/` is non-negotiable: same files, same heading levels, same heading
count, same order, same components. Translate the text, never the structure.

---

## 1. Register: formal **vous** — never tu / toi / ton

**Rule:** Always address the reader with the formal second person plural: `vous`, `votre`, `vos`.
Never `tu`, `te`, `toi`, `ton`, `ta`, `tes`, and never the second-person-singular imperative
(`Branche`, `Appuie`, `Vérifie`, `Assure-toi`).

### Why this differs from the Dutch pages (deliberate brand-voice decision)

The Dutch manuals use the informal `je` / `jouw`. **That decision does not transfer to French.**
French consumer hardware manuals conventionally use `vous` even for young, casual, direct-to-consumer
brands — tutoiement in a printed or published product manual reads either as childish or as an
untouched machine translation, and it is one of the first things a French reviewer flags. Three
concrete reasons this is locked:

- **Address is marked in French in a way it is not in Dutch.** `je` in Dutch is register-neutral in
  consumer copy; `tu` in French is a social claim about the relationship with the reader.
- **The corpus itself addresses professional buyers.** The safety chapter states the product is
  "suitable for both home and business use" (`en/manuals/*/safety.mdx`). Safety and warranty text
  addressed with `tu` is a liability-adjacent register error.
- **`vous` is universal, `tu` is not.** `vous` is correct for every French-speaking market
  (FR, BE, CH, CA); `tu` is not.

If the client later asks for tutoiement, that is a glossary change (§12), not a per-page judgement call.

### 5 example pairs (wrong register → right register)

| ✗ Wrong (tutoiement) | ✓ Right (vouvoiement) |
|---|---|
| `Branche le câble sur ton ordinateur portable.` | `Branchez le câble sur votre ordinateur portable.` |
| `Tu peux régler la luminosité de chaque écran séparément.` | `Vous pouvez régler la luminosité de chaque écran séparément.` |
| `Assure-toi d'utiliser le bon port USB-C.` | `Assurez-vous d'utiliser le bon port USB-C.` |
| `Ton Screenmate est prêt à l'emploi. Si ça ne marche pas, redémarre ton PC.` | `Votre Screenmate est prêt à l'emploi. Si cela ne fonctionne pas, redémarrez votre ordinateur.` |
| `Ouvre les Réglages Système, puis va dans Moniteurs et choisis Disposition.` | `Ouvrez les Réglages Système, allez dans Moniteurs, puis cliquez sur Disposition.` |

### Instructions use the plain `vous` imperative

Numbered steps take the bare `vous`-imperative — no subject pronoun, no `veuillez`, no `s'il vous plaît`.

| ✗ Wrong | ✓ Right |
|---|---|
| `Vous connectez le câble au port USB-C.` | `Branchez le câble sur le port USB-C.` |
| `Veuillez retirer le film de protection.` | `Retirez le film de protection.` |
| `Il faut redémarrer votre ordinateur portable.` | `Redémarrez votre ordinateur portable.` |
| `S'il vous plaît, lisez attentivement les consignes.` | `Lisez attentivement les consignes suivantes.` |

**Locked exception:** none. English "Please …" is always dropped, including in the safety chapter
opener ("Please read the following guidelines carefully" → `Lisez attentivement les consignes suivantes`).

### Defect greps (any hit is a register defect until proven otherwise)

```
grep -nEi '\b(tu|toi|ton|ta|tes|t)\b' fr/manuals/**/*.mdx
grep -nE '\b(Branche|Connecte|Appuie|Vérifie|Ouvre|Choisis|Utilise|Règle|Retire|Clique|Télécharge|Installe|Redémarre|Débranche|Range|Plie|Déplie|Place|Sélectionne|Maintiens|Fais) ' fr/manuals/**/*.mdx
grep -nE 'Assure-toi|-toi\b|\bton\b|\bta\b|\btes\b' fr/manuals/**/*.mdx
```

False positives to expect and ignore: `ta` inside `étape`/`tablette` (the `\b` guards handle it),
and `Place` as a noun. Every other hit must be fixed.

---

## 2. Compound formation: head noun first, modifier after — never a hyphen chain

French does **not** build closed or hyphen-chained compounds the way German and Dutch do. The head
noun comes first; the qualifier follows it, either bare (apposition) or introduced by `de` / `à` / `pour`.
The internal hyphens of a trademark token (`USB-C`, `USB-A`, `Mini-HDMI`, `Type-C1`) belong to the
token itself and never change.

| English | ✗ Wrong (DE/NL pattern) | ✓ Locked French |
|---|---|---|
| USB-C cable | `USB-C-câble`, `câble-USB-C` | **`câble USB-C`** |
| USB-C port | `USB-C-port`, `USB C port` | **`port USB-C`** |
| USB-A port | `USB-A-port` | **`port USB-A`** |
| HDMI cable | `HDMI-câble` | **`câble HDMI`** |
| Mini HDMI port | `port Mini HDMI` | **`port Mini-HDMI`** |
| USB stick | `USB-clé`, `stick USB` | **`clé USB`** |
| PD charger | `PD-chargeur` | **`chargeur PD`** |
| Power Delivery port | `Power-Delivery-port` | **`port Power Delivery`** |
| USB-C charging port | `USB-C-port de charge` | **`port de charge USB-C`** |
| 45 W adapter | `45W-adaptateur` | **`adaptateur 45&nbsp;W`** |
| power adapter | `adaptateur de puissance` | **`adaptateur secteur`** |
| display driver | `affichage-pilote` | **`pilote d'affichage`** |
| headphone jack | `casque-prise` | **`prise casque`** |
| brightness button | `luminosité-bouton` | **`bouton de luminosité`** |
| power button | `alimentation-bouton` | **`bouton d'alimentation`** |
| menu button | `bouton-menu` | **`bouton Menu`** |
| scroll wheel | `roue de défilement` | **`molette`** |
| Windows version | `Windows-version` | **`version de Windows`** |
| OSD menu | `OSD-menu` | **`menu OSD`** |
| video signal | `vidéo-signal` | **`signal vidéo`** |

**Never write:** `USB C`, `USBC`, `usb-c`, `mini HDMI`, `Mini HDMI` (unhyphenated),
`Type C1`. `Mini-HDMI` is always hyphenated in French even where the EN source writes
`Mini HDMI` — `translations/dnt.json` lists the hyphenated form, and it wins. This deliberately
normalises an inconsistency that exists on the EN side.

### 2.1 The three-part chain — **LOCKED**, no exceptions

The English pattern `{A} to {B} cable` becomes:

> ### **`câble {A} vers {B}`**

The Dutch glossary was inconsistent here. **Do not repeat that.** Every occurrence in the corpus:

| English source | ✓ Locked French |
|---|---|
| USB-C to USB-C cable | **`câble USB-C vers USB-C`** |
| USB-C to USB-A cable | **`câble USB-C vers USB-A`** |
| USB-A to USB-C cable | **`câble USB-A vers USB-C`** |
| HDMI to USB-C cable | **`câble HDMI vers USB-C`** |
| Mini HDMI to HDMI cable | **`câble Mini-HDMI vers HDMI`** |
| dual USB-A to USB-C cable | **`câble double USB-A vers USB-C`** |
| USB-C > USB-C Cable *(package-contents `>` form)* | **`câble USB-C vers USB-C`** |
| USB-A > USB-C Cable *(package-contents `>` form)* | **`câble USB-A vers USB-C`** |
| USB-C (for HDMI > USB-C) *(heading)* | **`USB-C (pour HDMI vers USB-C)`** |

**Rules that make this deterministic:**

1. **`vers`, always.** Not `à`, not `-`, not `/`, not `>`.
2. **Order mirrors the EN source, A→B.** The two ends of these cables plug into different things;
   reversing the order is a factual error, not a stylistic one. `câble HDMI vers USB-C` and
   `câble USB-C vers HDMI` describe different setups.
3. **Only `câble` inflects.** Plural: `câbles USB-C vers USB-C`. The connector tokens never take `-s`
   (`câbles USB-C`, never `câbles USB-Cs`).
4. **Article:** `un câble` / `le câble` (masculine). `un câble USB-C vers USB-C`.
5. **Counts drop the `x`.** EN `2x USB-C to USB-C cables` → `2 câbles USB-C vers USB-C`, not
   `2x câbles`. The `×` multiplier sign is reserved for dimensions and resolutions
   (`1920 × 1080`, `40,6 × 23,7 × 2,5 cm`) and for the `3 × ports Mini-HDMI` heading, where it
   counts ports in a heading and the EN source already uses `×`.

**Explicitly rejected alternatives** (recorded so no later pass re-litigates them):

- ✗ `câble USB-C à USB-C` — `à` reads as purpose or attribute (`verre à vin`), not direction.
- ✗ `câble USB-C/USB-C` and `câble USB-C – USB-C` — ambiguous and unspeakable in a support call.
- ✗ `câble USB-C-USB-C` — hyphen chain; German/Dutch pattern, wrong for French.
- ✗ `câble USB-C > USB-C` — a bare `>` at the start of an MDX line becomes a blockquote, and mid-line
  it is noise. Always expand `>` to `vers`.

### 2.2 Gender and elision (locked)

All Screenmate product names are **masculine**: `le Screenmate`, `le Screenmate OneCable`,
`votre Screenmate Expand`, `le Panorama`, `l'Infinity Lite`.

| Term | Gender | Written form |
|---|---|---|
| câble | m. | `le câble`, `un câble` |
| port | m. | `le port` |
| écran | m. | `l'écran`, `les écrans` |
| moniteur | m. | `le moniteur` |
| adaptateur | m. | `l'adaptateur` |
| alimentation | f. | `l'alimentation` |
| prise | f. | `la prise` |
| clé USB | f. | `la clé USB` |
| housse / housse de protection | f. | `la housse` |
| étui de protection | m. | `l'étui` |
| support | m. | `le support` |
| bouton | m. | `le bouton` |
| molette | f. | `la molette` |
| voyant | m. | `le voyant` |
| haut-parleur | m. | `le haut-parleur`, pl. `les haut-parleurs` |
| dalle | f. | `la dalle` |
| pilote | m. | `le pilote` |
| hub | m. | `le hub` (no elision) |
| appareil | m. | `l'appareil` |
| ordinateur portable | m. | `l'ordinateur portable`, `votre ordinateur portable` |

---

## 3. French typography — the locked spacing convention

### 3.1 THE DECISION

> **Locked: the HTML entity `&nbsp;` before `:` `;` `!` `?` `%`, and inside guillemets
> `«&nbsp;…&nbsp;»`. A literal U+00A0 is used *only* in YAML frontmatter. A plain ASCII space
> before these marks is a defect. U+202F (narrow no-break space) is banned.**

Wherever French requires a space before a punctuation mark, that space is a **non-breaking**
space written as the entity `&nbsp;` — never a plain space, never a literal invisible character
in body copy.

| Context | Write | Renders as |
|---|---|---|
| Before `:` | `**Remarque&nbsp;:** utilisez le bon port.` | Remarque : utilisez le bon port. |
| Before `?` | `## Besoin d'aide&nbsp;?` | Besoin d'aide ? |
| Before `!` | `Un seul port USB&nbsp;!` | Un seul port USB ! |
| Before `;` | `Appuyez sur **M**&nbsp;; le menu s'ouvre.` | Appuyez sur M ; le menu s'ouvre. |
| Before `%` | `Réglez l'échelle sur 150&nbsp;%.` | Réglez l'échelle sur 150 %. |
| Quoted UI string | `Choisissez «&nbsp;Étendre le Bureau à cet écran&nbsp;».` | Choisissez « Étendre le Bureau à cet écran ». |
| Between number and unit | `un adaptateur de 45&nbsp;W` | un adaptateur de 45 W |
| **Frontmatter only** | literal U+00A0 (see 3.3) | — |

### 3.2 Why the entity and not the invisible character — verified, not assumed

Tested on 2026-08-11 against `@mdx-js/mdx@3.1.1`, the exact compiler bundled with the
globally installed `mint@4.2.776` this repo builds with. Both forms compile; the entity is
strictly safer:

| Test | Literal U+00A0 | `&nbsp;` entity |
|---|---|---|
| Body prose, headings, tables, `<Note>` children, link text, JSX `alt=` attributes | ✅ renders as NBSP | ✅ renders as NBSP (decoded to U+00A0 in output — identical DOM) |
| Immediately after an opening `**` | ❌ **silently breaks the emphasis** — U+00A0 is Unicode whitespace, so `**` is no longer left-flanking and the literal asterisks leak into the page | ✅ emphasis still parses (`&` is punctuation to the tokenizer) |
| Visible in `git diff` / review / `grep` | ❌ invisible | ✅ visible and countable |
| YAML frontmatter | ✅ survives the YAML parser | ❌ **leaks literally** — the sidebar would show `Réglages&nbsp;: Flip` |
| Inside a code span or fenced block | renders as NBSP | ❌ leaks literally as `&nbsp;` |

Two of those rows are the reason for the decision. The `**` row is a real, silent, page-breaking
failure mode that a translator agent hits the moment it writes `**&nbsp;Remarque&nbsp;:**`.
The review row matters for this project specifically: every French page goes through a diff
review, and a convention that is invisible in a diff cannot be reviewed.

**U+202F (narrow no-break space) is banned.** It compiles, but it survives into the rendered page
as U+202F, whose coverage in the Mintlify default font stack is not guaranteed — a missing glyph
renders as a tofu box on the live site. It is also visually indistinguishable from U+00A0 in
review, so it silently creates two conventions where the glossary locks one.

### 3.3 Frontmatter is the one exception

Frontmatter is parsed as YAML before MDX ever sees it, and **YAML does not decode HTML entities**
(verified against `js-yaml` as bundled with `mint`). Therefore:

1. **Preferred:** phrase every `title:` and `description:` so it contains no `:` `;` `!` `?` `%`.
   Every locked French title and description in §9 already satisfies this — none needs a
   non-breaking space. Keep it that way.
2. **Fallback only if unavoidable:** a literal U+00A0 character in the double-quoted YAML string.
   Flag it in the PR description, because it is invisible.
3. Never write `&nbsp;` inside frontmatter.

### 3.4 The mandatory `16:9` carve-out

A colon that is **not punctuation** takes no space on either side. This is the single most likely
place for a translator or a "fix the French spacing" pass to introduce a defect:

| Never touch | Reason |
|---|---|
| `16:9`, `4:3`, `16:10` | aspect ratios |
| `1000:1`, `100 000:1` | contrast ratios — the colon stays tight even though the number itself carries a space (§4.1) |
| `https://`, `http://` | URLs |
| `10:30` | clock times |
| `Type-C1`, `S6-L`, `S6-R`, `RGB` | device/hardware identifiers |
| anything inside a code span or fenced block | source, not prose |
| `--- title: ... ---` frontmatter keys | YAML syntax |

A colon introducing prose gets `&nbsp;`. A colon inside a ratio, URL, time or identifier gets nothing.

### 3.5 Other typography rules (locked)

| Item | Locked form | Notes |
|---|---|---|
| Apostrophe | ASCII `'` (U+0027) | **Never** U+2019 `’`. The EN and NL corpora contain zero U+2019; mixing creates grep and diff noise and complicates YAML. `l'écran`, `d'alimentation`, `qu'est-ce que`. |
| Quotation marks | `«&nbsp;…&nbsp;»` | For quoted UI strings. Straight `'…'` and `"…"` in French prose are defects. Where the EN source uses `**bold**` for a UI label, keep bold — do not convert bold to guillemets. |
| Parenthetical dash | `—` (U+2014) with a plain space each side | Matches the EN corpus exactly (19 files use `—`). Do **not** put `&nbsp;` around dashes. |
| Numeric range dash | `–` (U+2013) | Matches the EN corpus: `0–100`, `0–4`, `10–60 secondes`, `0° – 235°`. In flowing prose prefer `de 0 à 100`. |
| Heading case | **sentence case** | French headings are sentence case, not title case. `Ports and Buttons` → `Ports et boutons`. Proper nouns, DNT tokens and OSD caps keep their casing: `Configuration de l'affichage Windows`, `Réglages OSD`. |
| Inch mark | `15,6"` | Straight `"`, no space before it. In frontmatter it must be escaped: `\"`. |
| Sentence spacing | one space | Never two. |
| Ellipsis | `…` or `...` — match the EN source | Do not introduce ellipses that are not in the source. |

---

## 4. Numbers, units and measurements

| Type | Locked format | Example |
|---|---|---|
| Decimal separator | **comma** | `15,6"`, `2,5&nbsp;cm`, `3,5&nbsp;mm`, `40,6 × 23,7 × 2,5&nbsp;cm` |
| Thousands, 4 digits | **no separator** | `1820 grammes`, `1750 grammes`, `1552 grammes`, `3000 grammes`, `1920 × 1080` — never `1.820`, never `1 820` |
| Thousands, 5+ digits | **plain space** | `100 000:1` — French groups by three above four digits. Never `100,000` (English) and never `100.000` (German/Dutch). |
| Number + unit symbol | non-breaking space | `45&nbsp;W`, `65&nbsp;W`, `10&nbsp;W`, `5&nbsp;V`, `2&nbsp;A`, `60&nbsp;Hz`, `144&nbsp;Hz`, `25&nbsp;ms`, `300&nbsp;cd/m²` |
| Percent | space before `%` | `100&nbsp;%&nbsp;sRGB`, `72&nbsp;%&nbsp;NTSC`, `150&nbsp;%` — French takes a space before `%`, unlike EN/NL |
| Degrees Celsius | space before `°C` | `-20&nbsp;°C`, `60&nbsp;°C` (`°C` is a unit symbol) |
| Angle degrees | **no** space | `178°`, `360°`, `235°`, `180°`, `90°` (`°` alone is not a unit symbol) |
| Voltage / current pairs | expand both | EN `5V/2A` → `5&nbsp;V/2&nbsp;A`; EN `DC 5V/3A` → `CC 5&nbsp;V/3&nbsp;A` |
| Ranges | en dash, or `de … à …` | `0–100`, `10–60 secondes`, `5&nbsp;V – 20&nbsp;V`, `de 0 à 100` |
| Ratios | colon untouched | `16:9`, `4:3`, `16:10`, `1000:1`, `100 000:1` — see §3.4 |
| Contrast ratio 100,000:1 | **`100 000:1`** | **locked (gate ruling R5).** The only 5-digit figure in the corpus: `one-4k-oled/index.mdx` line 16 (prose) and line 28 (spec row). Both occurrences take the identical form. |
| Resolutions | `×` with spaces | `1920 × 1080`, `1920 × 1200` (normalise the EN corpus's `1920×1080` variant) |
| Counts | drop `x` | EN `2x USB-C cables` → `2 câbles USB-C`; EN `6x protective clips` → `6 clips de protection` |
| Ordinals | `1er`, `2e`, `3e` | not `1ère`/`2ème` |
| Sizes as product variants | comma decimal | `Flip 14"` stays; `Flip 15.6"` → `Flip 15,6"`; `Lite 144 Hz` stays (`144 Hz` is part of the DNT product name **Lite 144**) |

**Note on the unit space.** This is a deliberate divergence from the EN source's `45W` / `100%` /
`-20°C` and from the Dutch glossary, which locks the closed forms. French typographic and SI
convention requires the space, and a French reviewer reads `45W` and `100%` as untranslated
English. It is locked; do not "restore" the EN spacing.

### 4.1 Which space goes where — plain vs `&nbsp;` (gate ruling R5)

Two different spaces are in play and they are **not** interchangeable. The rule is mechanical:

| Position of the space | Form | Why |
|---|---|---|
| **Between digits** of a 5+ digit number | **plain space** — `100 000:1` | Verified MDX-safe in every context (see below). Nothing here sits next to a `**` delimiter, so the §3.2 emphasis hazard cannot fire. |
| **Between a number and a unit symbol** | `&nbsp;` — `45&nbsp;W`, `-20&nbsp;°C`, `100&nbsp;%` | Same reason as §3: the unit must not wrap away from its number, and these frequently sit inside `**bold**` spec labels. |
| **Before `:` `;` `!` `?`** as punctuation | `&nbsp;` | §3.1. |

**Verification (2026-08-11, `@mdx-js/mdx@3.1.1` as bundled with `mint@4.2.776`).** `100 000:1`
compiles cleanly and renders identically in all five probed positions: a spec-table cell, plain
prose, immediately after a bold label (`**Taux de contraste&nbsp;:** 100 000:1`), immediately after
a closing `**`, and adjacent to other ratios (`100 000:1 et 1000:1 et 16:9` — all three colons
correctly left tight). `strong` parsed in every bold case; no literal `**` leaked in any case.
This confirms the §3.2 finding was specific to whitespace *touching* a `**` delimiter, which
digit-internal spacing never does.

**Accepted tradeoff:** a plain space can line-wrap, so `100 000:1` may in principle break across
two lines in a narrow column. This is accepted per the gate ruling (it keeps the figure greppable
and lets the shared verification script normalise spaced thousands across all languages). If the
client ever reports a visible wrap, the fix is a one-cell change to `100&nbsp;000:1`, which is
also verified working — do not make that change unilaterally.

---

## 5. Term tables

### 5.1 Product & hardware

| English | French | Notes | Keep EN? |
|---|---|---|---|
| Screenmate | Screenmate | masculine: `le Screenmate`, `votre Screenmate` | ✓ |
| OneCable / Lite / Lite 144 / Dual Flip / Flip / Expand / Infinity / Infinity Lite / One 4K / One 4K OLED / Panorama | *(unchanged)* | product names; always preceded by `le`/`votre` + `Screenmate` where the EN does | ✓ |
| screen | écran (m.) | `l'écran`, pl. `les écrans` | — |
| display *(the panel as a device)* | écran (m.) | never `display`; `affichage` is the output, not the object | — |
| display *(verb)* | afficher | — | — |
| monitor | moniteur (m.) | the device as a whole, esp. in OSD/safety context | — |
| portable monitor | écran portable (m.) | locked market term — overrides monitor→moniteur here | — |
| triple-screen portable monitor | écran portable triple | — | — |
| dual portable monitor | double écran portable | — | — |
| portable display extension | extension d'écran portable (f.) | — | — |
| foldable dual-screen extension | extension double écran pliable (f.) | — | — |
| laptop | ordinateur portable (m.) | never bare `portable` (ambiguous with *mobile phone*), never `laptop` | — |
| computer | ordinateur (m.) | — | — |
| PC | PC (m.) | — | ✓ |
| MacBook / Mac | MacBook / Mac | — | ✓ |
| phone / smartphone | téléphone (m.) / smartphone (m.) | — | — |
| tablet | tablette (f.) | — | — |
| game console | console de jeu (f.) | pl. `consoles de jeu` | — |
| Nintendo Switch / PlayStation / Xbox / Nintendo Charging Dock | *(unchanged)* | third-party product names | ✓ |
| device | appareil (m.) | never `dispositif` in consumer copy | — |
| accessories | accessoires (m.pl.) | `une souris ou un clavier` | — |
| mouse / keyboard | souris (f.) / clavier (m.) | — | — |
| cable | câble (m.) | see §2.1 for the `vers` chain | — |
| port | port (m.) | — | — |
| connector | connecteur (m.) | — | — |
| plug *(noun)* | fiche (f.) | `la fiche USB-A noire` | — |
| button | bouton (m.) | — | — |
| menu button | bouton Menu | capital M — it names the on-device `M` key | — |
| power button | bouton d'alimentation | — | — |
| Power & Return button | bouton d'alimentation et de retour | — | — |
| multifunctional button | bouton multifonction | invariable in the singular | — |
| scroll wheel | molette (f.) | — | — |
| speaker *(built-in)* | haut-parleur (m.) | — | — |
| external speakers | enceintes externes (f.pl.) | — | — |
| headphones | casque (m.) | `prise casque` | — |
| 3.5 mm headphone jack | prise casque 3,5&nbsp;mm (f.) | normalises the EN `3.5mm` / `3.5 mm` variants | — |
| indicator light / status LED | voyant lumineux (m.) / voyant d'état | — | — |
| LED indicator | voyant LED (m.) | `LED` stays EN | — |
| motherboard indicator light | voyant de la carte mère | — | — |
| stand | support (m.) | — | — |
| adjustable stand | support réglable | — | — |
| screen stand / single screen stand | support d'écran / support pour écran unique | — | — |
| bracket | support de fixation (m.) | the clip that grips the laptop lid | — |
| movable arm | bras mobile (m.) | — | — |
| frame | cadre (m.) | — | — |
| locking legs | pieds de verrouillage (m.pl.) | — | — |
| front lock | verrou avant (m.) | — | — |
| groove | rainure (f.) | — | — |
| silicone strip | bande en silicone (f.) | — | — |
| centre piece | pièce centrale (f.) | — | — |
| protective case | étui de protection (m.) | keeps the EN case/sleeve distinction | — |
| protective sleeve | housse de protection (f.) | keeps the EN case/sleeve distinction | — |
| protective cap | capuchon de protection (m.) | — | — |
| protective clips | clips de protection (m.pl.) | — | — |
| protective film | film de protection (m.) | — | — |
| cable organizer | range-câbles (m., invariable) | — | — |
| stability rubbers | patins antidérapants (m.pl.) | — | — |
| leather carry pouch | pochette de transport en cuir (f.) | — | — |
| magnet | aimant (m.) | — | — |
| USB stick | clé USB (f.) | never `stick USB` | — |
| packaging | emballage (m.) | — | — |
| flat surface | surface plane (f.) | — | — |
| desk | bureau (m.) | lowercase — distinct from Windows `Bureau` (desktop) | — |
| workspace | espace de travail (m.) | — | — |
| workstation | poste de travail (m.) | — | — |

### 5.2 Connections & power

| English | French | Notes | Keep EN? |
|---|---|---|---|
| USB-C | USB-C | never `USB C` / `USBC` | ✓ |
| USB-A | USB-A | — | ✓ |
| USB 2.0 | USB 2.0 | — | ✓ |
| HDMI | HDMI | — | ✓ |
| Mini-HDMI | Mini-HDMI | always hyphenated, even where EN writes `Mini HDMI` | ✓ |
| DisplayPort | DisplayPort | in `dnt.json` since the gate R3 realign | ✓ |
| DisplayPort Alt Mode | DisplayPort Alt Mode | covered by the `DisplayPort` DNT token; never translate the `Alt Mode` tail either | ✓ |
| DP monitor | moniteur DP | `DP` stays | — |
| Type-C1 / Type-C2 | Type-C1 / Type-C2 | on-device SOURCE values | ✓ |
| Power Delivery (PD) | Power Delivery (PD) | brand term | ✓ |
| PD-compatible | compatible PD | — | — |
| reverse charging | charge inversée (f.) | gloss the EN once per page on first use: `charge inversée (reverse charging)` | — |
| reverse charging mode | mode de charge inversée | — | — |
| fast-charge mode | mode de charge rapide | — | — |
| charge *(verb)* | recharger | `recharger votre ordinateur portable` | — |
| charger | chargeur (m.) | `chargeur PD`, `chargeur USB-C` | — |
| power adapter | adaptateur secteur (m.) | — | — |
| AC/DC adapter | adaptateur CA/CC (m.) | `CA/CC` is the correct French abbreviation | — |
| DC input | entrée CC (f.) | `une entrée CC comprise entre 5&nbsp;V et 20&nbsp;V` | — |
| power *(electrical supply)* | alimentation (f.) | — | — |
| power *(output capability)* | puissance (f.) | `puissance suffisante` | — |
| output power | puissance de sortie (f.) | — | — |
| power supply | alimentation (f.) | — | — |
| additional / external power supply | alimentation supplémentaire / externe | — | — |
| power source | source d'alimentation (f.) | — | — |
| power outlet / wall outlet | prise de courant (f.) | — | — |
| grounded | mis à la terre | `une prise de courant correctement mise à la terre` | — |
| amperage | ampérage (m.) | — | — |
| power cable | câble d'alimentation (m.) | — | — |
| connection cable | câble de connexion (m.) | — | — |
| supplied / included cable | câble fourni / inclus | — | — |
| hub | hub (m.) | `hub USB-C`, `hub HDMI` | ✓ |
| adapter | adaptateur (m.) | — | — |
| video adapter | adaptateur vidéo (m.) | — | — |
| switch dock / charging dock | station d'accueil (f.) | — | — |
| connect *(plug a cable in)* | brancher | `Branchez le câble sur le port USB-C.` | — |
| connect *(establish the link)* | connecter | `Connectez le Screenmate à votre ordinateur portable.` | — |
| disconnect | débrancher | — | — |
| connection | connexion (f.) | — | — |
| single cable / one cable | câble unique / un seul câble | — | — |
| standby mode | mode veille (m.) | — | — |
| interference *(electromagnetic)* | interférences (f.pl.) | usually plural in French. **Only for the EM sense** — the safety chapter's "strong magnetic fields or transmitting equipment" line. | — |
| interference *(two power sources fighting)* | conflit d'alimentation (m.) | **round-4 correction.** `panorama/installation.mdx` used `interférences` for EN "may cause interference" about a charger plugged in while the Panorama also supplies power. French `interférences` reads as EMI and points the customer at the wrong phenomenon; the intended sense is a power-negotiation conflict. | — |
| receive power *(a port)* | recevoir du courant | **round-4 addition** (`onecable/controls.mdx`). `recevoir de l'alimentation` is not a French collocation — `alimentation` is the supply, `courant` is what flows through the port. `sert à l'alimentation` is also correct where the port is described by purpose rather than by what it receives. | — |

### 5.3 Software, drivers & OS

| English | French | Notes | Keep EN? |
|---|---|---|---|
| driver | pilote (m.) | **default in body copy** | — |
| display driver | pilote d'affichage (m.) | — | — |
| `DRIVERS` *(drive/folder name)* | `DRIVERS` | keep verbatim when naming the actual drive or folder on the supplied USB stick. The DNT token is the **caps** form (realigned from `Drivers` at the gate) — which matches the only way the EN corpus writes it as an on-disk artifact: `**DRIVERS (D:)**` in `onecable/installation-windows.mdx:47`. | ✓ |
| `DRIVERS (D:)` *(drive label)* | `DRIVERS (D:)` | keep verbatim — it is what Windows shows | ✓ |
| `Win10&11`, `Win 7&8`, `mac OS` *(folder names)* | *(unchanged)* | folder names on the supplied stick | ✓ |
| `RacerDisplayDriver-2024.9.13-en`, `RacerUSB`, `UsbDisplay` | *(unchanged)* | file / app / permission entry names | ✓ |
| "Download Drivers" *(heading)* | `Télécharger les pilotes` | **confirmed at the gate.** Only the literal drive/folder name `DRIVERS` stays EN; the lowercase common noun is always `pilote(s)`. The DNT token being caps-only makes this unambiguous. | — |
| "Download Windows Drivers" *(button label)* | `Télécharger les pilotes Windows` | — | — |
| "Download for macOS" *(button label)* | `Télécharger pour macOS` | — | — |
| download *(verb / noun)* | télécharger / téléchargement (m.) | — | — |
| install / installation | installer / installation (f.) | — | — |
| manual installation | installation manuelle | — | — |
| installer | programme d'installation (m.) | — | — |
| unzip / extract the archive | décompresser l'archive | — | — |
| restart | redémarrer | `Redémarrez votre ordinateur portable.` | — |
| operating system | système d'exploitation (m.) | — | — |
| Windows / macOS / Linux | *(unchanged)* | never `Mac OS`, never `MacOS` | ✓ |
| Windows version | version de Windows (f.) | — | — |
| Windows 10 or higher | Windows 10 ou version ultérieure | — | — |
| update | mettre à jour / mise à jour (f.) | — | — |
| software | logiciel (m.) | — | — |
| application / app | application (f.) | — | — |
| file | fichier (m.) | — | — |
| folder | dossier (m.) | — | — |
| drive | lecteur (m.) | — | — |
| password | mot de passe (m.) | — | — |
| toggle *(macOS switch)* | option (f.) | `activez l'option en regard de UsbDisplay` | — |
| internet | Internet | `connecté à Internet` (no article) | — |
| on-screen instructions | les instructions à l'écran | never `instructions sur écran` | — |
| menu bar *(macOS)* | barre des menus (f.) | — | — |
| taskbar *(Windows)* | barre des tâches (f.) | — | — |
| Launchpad | Launchpad | Apple keeps it in French | ✓ |
| output device | périphérique de sortie (m.) | — | — |
| desktop *(Windows)* | Bureau (m.) | capital B — the Windows FR label | — |

### 5.4 Display, image & OSD concepts *(prose, not device labels — see §7 for those)*

| English | French | Notes | Keep EN? |
|---|---|---|---|
| on-screen menu (OSD) | menu à l'écran (OSD) | — | partly ✓ |
| OSD | OSD | acronym stays | ✓ |
| OSD menu | menu OSD (m.) | — | — |
| settings menu | menu des réglages (m.) | — | — |
| settings | réglages (m.pl.) | `paramètres` only for OS settings screens | — |
| brightness | luminosité (f.) | — | — |
| contrast | contraste (m.) | — | — |
| dynamic contrast | contraste dynamique | — | — |
| sharpness | netteté (f.) | — | — |
| volume | volume (m.) | — | — |
| backlight | rétroéclairage (m.) | translated everywhere, including the OSD chapter heading `## Backlight` → `## Rétroéclairage`. `Backlight` was removed from `dnt.json` in `12b31e3` as context-dependent; the EN corpus never writes it in caps, so never invent a `(BACKLIGHT)` gloss. As a spec-table field value it stays `LED`. | — |
| black level | niveau de noir (m.) | — | — |
| colour / color | couleur (f.) | — | — |
| colour temperature | température de couleur (f.) | — | — |
| red / green / blue channel | canal rouge / vert / bleu | — | — |
| RGB values | valeurs RVB | French uses RVB; keep `RGB` only when quoting the on-device menu | — |
| preset | préréglage (m.) | — | — |
| picture mode / display mode | mode d'image / mode d'affichage (m.) | — | — |
| factory defaults | réglages d'usine (m.pl.) | `rétablir les réglages d'usine` | — |
| aspect ratio | format d'image (m.) | — | — |
| widescreen | format large (m.) | — | — |
| resolution | résolution (f.) | — | — |
| refresh rate | taux de rafraîchissement (m.) | — | — |
| response time | temps de réponse (m.) | — | — |
| contrast ratio | taux de contraste (m.) | — | — |
| viewing angle | angle de vision (m.) | — | — |
| panel type | type de dalle (m.) | `dalle` is the French term for the panel | — |
| screen type | type d'écran (m.) | — | — |
| colour accuracy | précision des couleurs (f.) | — | — |
| colour gamut | gamme de couleurs (f.) | — | — |
| HDR / HDR 10 / IPS / LCD / LED / OLED / NTSC / sRGB / Full HD / 4K | *(unchanged)* | — | ✓ |
| video signal | signal vidéo (m.) | — | — |
| input source | source d'entrée (f.) | — | — |
| signal source | source de signal (f.) | — | — |
| video output | sortie vidéo (f.) | — | — |
| audio output / sound output | sortie audio (f.) | — | — |
| no signal | aucun signal | — | — |
| flicker *(verb)* | scintiller | `l'écran scintille` | — |
| cut out *(verb)* | se couper | `se coupe par moments` | — |
| unstable | instable | — | — |
| extend the desktop | étendre le Bureau | — | — |
| mirror / duplicate displays | dupliquer les écrans | — | — |
| scale *(noun)* | échelle (f.) | — | — |
| landscape view | mode paysage (m.) | — | — |
| portrait view | mode portrait (m.) | — | — |
| upside down | à l'envers | `Un écran est à l'envers&nbsp;?` | — |
| dual screen | double écran (m.) | — | — |
| eye strain | fatigue oculaire (f.) | — | — |
| blue light | lumière bleue (f.) | — | — |
| startup logo | logo de démarrage (m.) | — | — |
| screen surface | surface de l'écran (f.) | — | — |
| ventilation openings | ouvertures de ventilation (f.pl.) | — | — |
| ambient temperature | température ambiante (f.) | — | — |

### 5.5 Actions & instruction verbs

| English | French imperative (vous) | Notes |
|---|---|---|
| Press | Appuyez sur | never `Pressez` |
| Press and hold | Maintenez … enfoncé | `Maintenez le bouton M enfoncé.` |
| Press briefly / short press | Appuyez brièvement / appui court | — |
| Long press | Appui long | — |
| Click | Cliquez sur | never `Cliquez X` without `sur` |
| Right-click | Faites un clic droit sur | — |
| Double-click | Double-cliquez sur | — |
| Select | Sélectionnez | — |
| Choose | Choisissez | — |
| Confirm | Confirmez / validez | — |
| Navigate | Naviguez dans | — |
| Adjust / set | Réglez | `Réglez la luminosité.` |
| Increase / decrease | Augmentez / diminuez | — |
| Turn on / off | Allumez / éteignez | for the device |
| Enable / disable | Activez / désactivez | for a setting |
| Switch to | Basculez sur / passez à | — |
| Connect | Branchez *(cable)* / connectez *(device)* | see §5.2 |
| Disconnect | Débranchez | — |
| Unpack / remove from the packaging | Déballez / retirez de l'emballage | — |
| Remove *(the film)* | Retirez | — |
| Place | Placez / posez | — |
| Attach / mount | Fixez / montez | — |
| Detach / release | Détachez | — |
| Unfold / fold out | Dépliez | — |
| Fold in / fold back up | Repliez | — |
| Rotate | Faites pivoter | `Faites pivoter l'écran de 180°.` |
| Pull out | Déployez / tirez | — |
| Slide | Faites glisser | — |
| Drag | Faites glisser | for on-screen elements |
| Open / close | Ouvrez / fermez | — |
| Go to | Allez dans | `Allez dans Réglages Système.` |
| Follow | Suivez | — |
| Check / make sure | Vérifiez / assurez-vous que | — |
| Store | Rangez | — |
| Clean | Nettoyez | — |
| Avoid / prevent | Évitez | — |
| Do not … | Ne … pas + infinitive | `Ne posez pas d'objets sur l'écran.` |

### 5.6 Spec-table field names (`## Caractéristiques techniques`)

| English field | French field |
|---|---|
| Feature | Caractéristique |
| Specification | Spécification |
| Product Name | Nom du produit |
| Model Number | Numéro de modèle |
| Resolution | Résolution |
| Brightness | Luminosité |
| Aspect Ratio | Format d'image |
| Response Time | Temps de réponse |
| Size | Taille |
| Screen Size | Taille de l'écran |
| Contrast Ratio | Taux de contraste |
| Panel Type | Type de dalle |
| Screen Type | Type d'écran |
| Viewing Angle | Angle de vision |
| Refresh Rate | Taux de rafraîchissement |
| Color Accuracy | Précision des couleurs |
| Color Gamut | Gamme de couleurs |
| Color | Couleur |
| Backlight | Rétroéclairage |
| HDR | HDR |
| Weight | Poids |
| Dimensions | Dimensions |
| Dimensions (folded) | Dimensions (plié) |
| Supported OS | Systèmes d'exploitation pris en charge |
| Special Features | Caractéristiques particulières |

Field **values** that are identifiers or units stay unchanged (`IPS`, `LCD`, `LED`, `HDR 10`,
`M107`, `M109`, `1000:1`, `16:9`, `100 % sRGB`, `72 % NTSC`, `178°`, `Windows, macOS, Linux`).
Three values do change: `Grey` → `Gris`, `1820 grams` → `1820 grammes`, and
`100,000:1` → **`100 000:1`** (§4.1 — One 4K OLED only).

### 5.7 Package-contents items (`## Contenu de l'emballage`)

| English | French |
|---|---|
| `Screenmate {Product}` | `Screenmate {Product}` *(unchanged)* |
| 2x USB-C to USB-C cables | 2 câbles USB-C vers USB-C |
| 2x USB-C to USB-C Cables (60 cm) | 2 câbles USB-C vers USB-C (60 cm) |
| USB-C > USB-C Cable | Câble USB-C vers USB-C |
| 2x USB-A > USB-C Cable | 2 câbles USB-A vers USB-C |
| 2x USB-C to USB-A cables | 2 câbles USB-C vers USB-A |
| 1x USB-C to USB-A adapter cable (90 cm) | 1 câble adaptateur USB-C vers USB-A (90 cm) |
| 2x Mini-HDMI to HDMI cables | 2 câbles Mini-HDMI vers HDMI |
| 1x Mini HDMI to HDMI cable (90 cm) | 1 câble Mini-HDMI vers HDMI (90 cm) |
| 1x USB-C to USB-C cable (1.2 m) | 1 câble USB-C vers USB-C (1,2 m) |
| 1x USB-C to USB-C cable (0.5 m) | 1 câble USB-C vers USB-C (0,5 m) |
| 65 Watt USB-C power adapter | Adaptateur secteur USB-C 65&nbsp;W |
| USB Stick (Incl. Driver) | Clé USB (pilote inclus) |
| 1x video adapter | 1 adaptateur vidéo |
| Protective case | Étui de protection |
| Protective Sleeve | Housse de protection |
| Cable organizer | Range-câbles |
| 6x protective clips | 6 clips de protection |
| 8x stability rubbers | 8 patins antidérapants |
| Screen stand | Support d'écran |
| Single screen stand | Support pour écran unique |
| Magnet | Aimant |

---

## 6. Tone & phrasing — literal-translation traps

| English construction | ✗ Wrong (literal) | ✓ Locked French |
|---|---|---|
| Make sure that … | `Faites sûr que…` | `Assurez-vous que…` / `Veillez à ce que…` |
| Please … | `S'il vous plaît, …` | *(drop it — bare imperative)* |
| **Note:** | `**Note&nbsp;:**` | `**Remarque&nbsp;:**` |
| **Important:** | `**Importante&nbsp;:**` | `**Important&nbsp;:**` |
| **Caution:** | `**Attention&nbsp;!**` | `**Attention&nbsp;:**` |
| **Tip:** | `**Pointe&nbsp;:**` | `**Conseil&nbsp;:**` |
| **Please note:** | `**Veuillez noter&nbsp;:**` | `**Remarque&nbsp;:**` |
| Follow the on-screen instructions | `Suivez les instructions sur-écran` | `Suivez les instructions à l'écran` |
| Click 'Open' | `Cliquez 'Ouvrir'` | `Cliquez sur «&nbsp;Ouvrir&nbsp;»` |
| Restart your laptop | `Restartez votre laptop` | `Redémarrez votre ordinateur portable` |
| After successful installation, … | `Après installation réussie…` | `Une fois l'installation terminée, …` |
| Then proceed to step 5 | `Passez alors directement à l'étape&nbsp;5` *(the pre-round-4 lock, superseded — **not** a wrong-from-the-start example)* | `Passez directement à l'étape&nbsp;5` *(round-4: `alors` dropped — see §6.1; the original ✗ example `Alors procédez à l'étape 5` remains wrong too)* |
| It's now ready for use | `Il est maintenant prêt pour l'usage` | `Il est maintenant prêt à l'emploi` |
| If it doesn't work right away | `Si ça ne marche pas tout de suite` | `Si cela ne fonctionne pas immédiatement` |
| provided that … | `fourni que…` | `à condition que…` (+ subjunctive) |
| such as | `comme par exemple` | `tel qu'un…` / `par exemple` |
| as shown in image 2 | `comme montré dans image 2` | `comme illustré sur l'image&nbsp;2` |
| in the following ways | `dans les manières suivantes` | `de l'une des manières suivantes` *(shipped form — harmonised across onecable/infinity/flip/dual-flip/expand)* |
| supports five connection scenarios | `supporte cinq scénarios` | `prend en charge cinq scénarios de connexion` |
| does not deliver enough power | `ne délivre pas assez de puissance` | `ne fournit pas une puissance suffisante` |
| the port does not deliver power | `le port ne délivre pas d'énergie` | `le port ne fournit pas d'alimentation` |
| Take good care of your Screenmate | `Prenez bon soin de votre Screenmate` | `Prenez soin de votre Screenmate` |
| to prevent damage | `pour prévenir dommage` | `afin d'éviter tout dommage` |
| Watch your fingers | `Regardez vos doigts` | `Attention à vos doigts` |
| Need more overview? | `Besoin de plus de chambre&nbsp;?` | `Besoin d'une meilleure vue d'ensemble&nbsp;?` *(shipped form — §10.1.F)* |
| Pick the one that matches … | `Prenez celui qui matche…` | `Choisissez celui qui correspond à…` |
| your device's specifications | `les spécifications de votre appareil` | `la fiche technique de votre appareil` |
| boost your productivity | `booster votre productivité` | `améliorer votre productivité` |
| on the go | `sur le go` | `en déplacement` |

**Question headings:** the FAQ headings are full questions. Use inversion or `est-ce que`-free
phrasing with `&nbsp;?` — see §9.4. Never leave an English-style bare `?` with no space.

### 6.1 The `…&nbsp;? … alors …` question rhythm — **banned** (round-4 ruling)

The EN corpus (via the Dutch source) repeatedly answers a rhetorical question with `Then …`:
*"Is the output power lower than 10W? **Then** additional power supply is needed."* Two independent
native French reviewers named the resulting `…&nbsp;? … **alors** …` the single loudest translationese
tell in the FR corpus (9 occurrences, corrected 2026-08-12).

> **Rule: keep the question, drop `alors`.** The bare question followed by a plain imperative or
> declarative is idiomatic French consumer copy; the `alors` is what marks it as translated.

| ✗ Wrong | ✓ Locked French |
|---|---|
| `Besoin d'une alimentation supplémentaire&nbsp;? Utilisez **alors** le câble…` | `Besoin d'une alimentation supplémentaire&nbsp;? Utilisez le câble…` |
| `…figure déjà dans la liste&nbsp;? Passez **alors** directement à l'étape&nbsp;5.` | `…figure déjà dans la liste&nbsp;? Passez directement à l'étape&nbsp;5.` |
| `…&nbsp;? Une alimentation supplémentaire est **alors** nécessaire…` | `…&nbsp;? Une alimentation supplémentaire est nécessaire…` |
| `…&nbsp;? Suivez **alors** ces étapes&nbsp;:` | `…&nbsp;? Suivez ces étapes&nbsp;:` |

The pre-existing `Pas de chargeur USB-C&nbsp;? Utilisez un adaptateur secteur approprié.`
(`onecable/installation.mdx`) is the model. Do **not** restructure the question itself into
`Si …, …` — that changes the sentence type the EN source uses. Only `alors` goes.

#### The carve-out: **the rule applies inside a sentence only**

> **Across a paragraph break, replace `alors` with `Dans ce cas` — do not delete it.**

When the question and its answer are **separate paragraphs**, adjacency no longer carries the
condition and deleting the connector turns a conditional instruction into an unconditional one.
That is a change in instruction semantics, not in style. Both source languages keep an explicit
connector across the break, so the French must too:

| | |
|---|---|
| EN `onecable/installation.mdx:44` | *"**Then** connect the other USB cable to a power outlet."* |
| NL `onecable/installation.mdx:44` | *"Sluit **dan** de andere USB-kabel aan op het netstroom."* |
| ✗ Wrong (deletes the condition) | `Vous n'avez qu'un seul port USB&nbsp;?` ¶ `Branchez l'autre câble USB sur une prise de courant.` |
| ✓ Locked French | `Vous n'avez qu'un seul port USB&nbsp;?` ¶ `**Dans ce cas**, branchez l'autre câble USB sur une prise de courant.` |

`Dans ce cas, …` is idiomatic French, is not the `alors` calque, and is the standard French device
for exactly this cross-paragraph question-answer pattern. Merging the two paragraphs into one would
also restore the condition, but it changes the block structure and breaks parity with `en/`.

Of the nine sites corrected on 2026-08-12, **eight are intra-sentence** (`alors` deleted) and
**one is cross-paragraph** (`onecable/installation.mdx:44`, `Dans ce cas` added).

#### Defect greps — two passes, both must return nothing

`alors que` as a conjunction is fine and neither pattern reaches it.

```
# 1. same-sentence form
grep -rnE '&nbsp;\?[^|]*\balors\b' fr/

# 2. cross-paragraph form (the carve-out shape) — needs PCRE: POSIX ERE reads \n literally
LC_ALL=C.UTF-8 grep -rlzP '&nbsp;\?\s*\n\s*\n[^\n]*\balors\b' fr/
```

**Both passes were validated against `ebbda95` (the pre-fix tree):** pass 1 finds the 8
intra-sentence sites, pass 2 finds `fr/manuals/onecable/installation.mdx`. A single-line `-E`
expression **cannot** guard the carve-out — GNU grep's ERE treats `\n` as a literal `n`, so a
`\n\n` alternative silently matches nothing. Do not "simplify" these two passes back into one.

### 6.2 Three more banned constructions (round-4 ruling)

| ✗ Wrong | ✓ Locked French | Why |
|---|---|---|
| `Vérifiez si le voyant est allumé.` | `Vérifiez que le voyant est allumé.` / `Assurez-vous que…` | `vérifier si` = *find out whether* (open question). An instruction takes `que`. Calque of NL `controleer of`. |
| `rétablir tous les réglages **à** leurs valeurs d'usine` | `réinitialiser tous les réglages **aux** valeurs d'usine` | `rétablir X à Y` is the EN *restore X to Y* pattern; French has no such preposition. `rétablir les réglages d'usine` (§5.4) is also correct. |
| `basculez **le format d'image** entre 4:3 et WIDE` | `basculez **entre les formats** 4:3 et WIDE` | `basculer` in the *switch between modes* sense is intransitive; transitive `basculer qqch` means to tip it over. |

---

## 7. OSD caps labels — **untranslatable, verbatim**

These strings are engraved in the monitor's firmware menu and render **in English on the physical
device** regardless of the manual's language. They are listed in `translations/dnt.json` and must
appear character-for-character as below. Never translate them, never lowercase them, never add
accents, never put a `&nbsp;` inside them.

```
ASPECT        BLUE          BRIGHTNESS    COLOR TEMP    CONTRAST
DCR           ECO           FPS           GREEN         HDR
HDR MODE      LANGUAGE      LOW BLUE LIGHT              ON/OFF
OSD TIMER     RED           RESET         RTS           SHARPNESS
SOURCE        TRANSPARENCY  WIDE
```

`COLOR TEMP` also occurs in the corpus as `COLOR TEMP.` (with a trailing period, in
`expand/osd.mdx` and `flip/osd.mdx`) — reproduce whichever form the EN source uses on that line.

**Pattern to follow.** The EN corpus writes `French gloss (CAPS LABEL)`. Keep that structure and
translate only the gloss:

| English source line | Locked French |
|---|---|
| `**Brightness (BRIGHTNESS):**` | `**Luminosité (BRIGHTNESS)&nbsp;:**` |
| `**Contrast (CONTRAST):**` | `**Contraste (CONTRAST)&nbsp;:**` |
| `**Sharpness (SHARPNESS):**` | `**Netteté (SHARPNESS)&nbsp;:**` |
| `**ECO mode (ECO):**` | `**Mode ECO (ECO)&nbsp;:**` |
| `**Aspect (ASPECT):**` | `**Format d'image (ASPECT)&nbsp;:**` |
| `**Color Temp. (COLOR TEMP.):**` | `**Température de couleur (COLOR TEMP.)&nbsp;:**` |
| `**Red (RED):**` / `**Green (GREEN):**` / `**Blue (BLUE):**` | `**Rouge (RED)&nbsp;:**` / `**Vert (GREEN)&nbsp;:**` / `**Bleu (BLUE)&nbsp;:**` |
| `**Language (LANGUAGE):**` | `**Langue (LANGUAGE)&nbsp;:**` |
| `**OSD Timer (OSD TIMER):**` | `**Minuterie OSD (OSD TIMER)&nbsp;:**` |
| `**Transparency (TRANSPARENCY):**` | `**Transparence (TRANSPARENCY)&nbsp;:**` |
| `**Reset (RESET):**` | `**Réinitialisation (RESET)&nbsp;:**` |
| `**HDR Mode (HDR MODE):**` | `**Mode HDR (HDR MODE)&nbsp;:**` |
| `**Source (SOURCE):**` | `**Source (SOURCE)&nbsp;:**` |
| `**Low Blue Light (LOW BLUE LIGHT):**` | `**Lumière bleue faible (LOW BLUE LIGHT)&nbsp;:**` |
| `**DCR (Dynamic Contrast Ratio):**` | `**DCR (taux de contraste dynamique)&nbsp;:**` — note the reversed order: `DCR` is the label, the parenthetical is the expansion and *is* translated |
| `**DCR (Dynamic Contrast Ratio) (ON/OFF):**` | `**DCR (taux de contraste dynamique) (ON/OFF)&nbsp;:**` |

Where the EN source uses the **bare caps label with no gloss** (`dual-flip/osd.mdx`:
`**BRIGHTNESS (0–100):**`, `**ASPECT:**`, `**COLOR TEMP:**`, `**LANGUAGE:**`, `**SOURCE:**`,
`**LOW BLUE LIGHT:**`, `**RESET:**`, `**HDR:**`), keep it bare — do **not** add a French gloss
that is not in the source. Structural parity beats helpfulness.

**Headings are not caps labels.** The OSD chapter *headings* (`## Backlight`, `## Reset`,
`### 1. Backlight`, `### 5. Reset`, `## Image`, `## Color`, `## Settings`, `## Other`) are Title
case in the EN source, not caps. Translate them plainly — `## Rétroéclairage`,
`## Réinitialisation`, `## Image`, `## Couleur`, `## Réglages`, `## Autres`. Do **not** append a
`(BACKLIGHT)` / `(RESET)` gloss to a heading: that would invent a device string the EN page never
shows. The caps label belongs only on the bullet line where the EN source already prints it.

### 7.1 Device-rendered menu **values** — also verbatim

These are options the user reads on the monitor's own screen. Keep them in English; add a French
gloss in parentheses only where the EN source already glosses them.

```
Standard   Game   Movie   Text   Energy Saving   FPS   RTS
Warm   Cool   User
Off   Auto   2084
ON   OFF
Type-C1   Type-C2   HDMI
4:3   16:9   WIDE
```

`Real-Time Strategy (RTS)` → `Real-Time Strategy (RTS)` — the genre name stays English;
`First-Person Shooter (FPS)` likewise. The surrounding prose is French:
`**RTS&nbsp;:** optimisé pour les jeux Real-Time Strategy (RTS).`

Physical button engravings are also verbatim: `M`, `+`, `−`, `≡`, `L`, `R`, `S6-L`, `S6-R`.
Note `−` is U+2212 (minus sign) in the corpus, not a hyphen — copy it exactly.

### 7.2 Gloss vocabulary — the French words used *beside* a CAPS token

The CAPS token never changes (§7). Only the gloss beside it is translated, and it must be
translated the same way every time. These 17 entries are the complete gloss vocabulary of the
corpus.

| EN gloss | French gloss |
|---|---|
| Brightness | Luminosité |
| Contrast | Contraste |
| Sharpness | Netteté |
| Black Level | Niveau de noir |
| Aspect / Aspect Ratio | Format / Format d'image |
| Color Temperature / Color Temp. | Température de couleur |
| Red | Rouge |
| Green | Vert |
| Blue | Bleu |
| Language | Langue |
| OSD Timer | Minuterie OSD |
| Transparency | Transparence |
| Source | Source |
| Reset | Réinitialisation |
| HDR Mode | Mode HDR |
| Low Blue Light | Lumière bleue faible |
| ECO mode / ECO Mode / ECO modes | Mode ECO / **Modes ECO** when the EN is plural |

EN casing varies by product (`ECO mode`, `ECO Mode`) — that variation collapses to one French form.
EN **number** does not: `ECO modes` (lite, lite-144hz) is plural and stays plural in French.

### 7.3 The suffix pattern — do not enumerate the ~38 variants

**16 run-in labels in the corpus rely on this pattern alone** (the other suffixed forms are already
spelled out in the §7 CAPS table). They are not listed individually, because the pattern plus §7.2
generates every one of them deterministically:

> `**{Gloss} ({SUFFIX}):**` → `**{French gloss} ({SUFFIX})&nbsp;:**`

The suffix is copied **verbatim** when it is a CAPS token (`BRIGHTNESS`, `ASPECT`, `ON/OFF`,
`COLOR TEMP.`), a numeric range (`0–100`, `0–4`), or a ratio (`16:9 / 4:3`).

**The one trap:** a suffix that contains a real word is not verbatim — the word is prose and must
be translated.

| EN | ✗ Wrong | ✓ Right |
|---|---|---|
| `**OSD Timer (10–60 seconds):**` | `**Minuterie OSD (10–60 seconds)&nbsp;:**` | `**Minuterie OSD (10–60 secondes)&nbsp;:**` |
| `**OSD TIMER (10–60 seconds):**` | — | `**OSD TIMER (10–60 secondes)&nbsp;:**` *(bare-caps form: label stays, unit word translates)* |
| `**Brightness (0–100):**` | — | `**Luminosité (0–100)&nbsp;:**` *(pure range — verbatim)* |
| `**DCR (Dynamic Contrast Ratio) (ON/OFF):**` | — | `**DCR (taux de contraste dynamique) (ON/OFF)&nbsp;:**` |

Note the `&nbsp;` before every colon (§3.1) — the colon sits inside the `**…**` run, which §3.2
verified is safe with the entity form and **unsafe** with a literal U+00A0.

---

## 8. OS-specific UI labels — must match the localized OS

These must match what a French-language Windows or macOS actually shows. Do not invent
translations, and do not leave them in English.

**Note:** this applies to *label text in prose*. The screenshots themselves stay English on all
language pages (client decision, carried over from the Dutch pages).

| Context | EN in corpus | French (matches OS UI) |
|---|---|---|
| Windows | Display Settings / Display settings | `Paramètres d'affichage` |
| Windows | Extend desktop to this display | `Étendre le Bureau à cet écran` |
| Windows | Identify | `Identifier` |
| Windows | Display orientation | `Orientation de l'affichage` |
| Windows | Flipped | `Paysage (inversé)` — the portrait equivalent is `Portrait (inversé)` |
| Windows | Mirrored *(superseded on EN pages by "Flipped")* | `Paysage (inversé)` |
| Windows | Scale | `Échelle` |
| Windows | This PC ('Deze pc') | `Ce PC` |
| Windows | DRIVERS (D:) | `DRIVERS (D:)` *(unchanged)* |
| Windows | taskbar | `barre des tâches` |
| Windows | sound settings | `Paramètres de son` |
| Windows | Speaker (Realtek(R) Audio) | *(unchanged — a device name)* |
| macOS | System Settings | `Réglages Système` |
| macOS | System Preferences *(older builds)* | `Préférences Système` |
| macOS | Displays | `Moniteurs` |
| macOS | Arrange / Arrangement | `Disposition` |
| macOS | Privacy & Security | `Confidentialité et sécurité` |
| macOS | Security & Privacy *(older builds)* | `Sécurité et confidentialité` |
| macOS | Screen Recording | `Enregistrement de l'écran` |
| macOS | Screen & System Audio Recording | `Enregistrement de l'écran et de l'audio système` |
| macOS | Applications | `Applications` |
| macOS | Open | `Ouvrir` |
| macOS | Rotation | `Rotation` |
| macOS | Standard | `Standard` |
| macOS | Sound | `Son` |
| macOS | Output *(tab)* | `Sortie` |
| macOS | Apple menu | `menu Pomme` |
| macOS | sidebar | `barre latérale` |
| macOS | MacBook speakers | `Haut-parleurs du MacBook` |
| macOS | UsbDisplay / RacerUSB | *(unchanged — app and permission entry names)* |

---

## 9. Document & section names — locked

Complete coverage of the EN corpus. French renderings are shown in backticks so the exact source
string (including `&nbsp;`) is unambiguous. **Headings are sentence case.**

### 9.1 Frontmatter `title:` (22 unique)

| English | French |
|---|---|
| Screenmate Product Manuals | `Manuels des produits Screenmate` |
| Screenmate OneCable Manual | `Manuel Screenmate OneCable` |
| Screenmate Lite Manual | `Manuel Screenmate Lite` |
| Screenmate Lite 144 Hz Manual | `Manuel Screenmate Lite 144 Hz` |
| Screenmate Dual Flip Manual | `Manuel Screenmate Dual Flip` |
| Screenmate Flip Manual | `Manuel Screenmate Flip` |
| Screenmate Expand Manual | `Manuel Screenmate Expand` |
| Screenmate Infinity Manual | `Manuel Screenmate Infinity` |
| Screenmate Infinity Lite Manual | `Manuel Screenmate Infinity Lite` |
| Screenmate One 4K Manual | `Manuel Screenmate One 4K` |
| Screenmate One 4K OLED Manual | `Manuel Screenmate One 4K OLED` |
| Screenmate Panorama Manual | `Manuel Screenmate Panorama` |
| Installation | `Installation` |
| Installation Windows | `Installation Windows` |
| Installation macOS | `Installation macOS` |
| Ports and Buttons | `Ports et boutons` |
| Ports and Controls | `Ports et commandes` |
| On-Screen Menu (OSD) | `Menu à l'écran (OSD)` |
| Display Settings | `Réglages d'affichage` |
| Display & Sound Settings | `Réglages d'affichage et de son` |
| Safety Instructions | `Consignes de sécurité` |
| FAQ | `FAQ` |

### 9.2 Frontmatter `description:` (36 unique)

Inch marks inside these strings stay escaped as `\"` — they are inside a double-quoted YAML scalar.

| English | French |
|---|---|
| Digital manuals for all Screenmate products | `Manuels numériques pour tous les produits Screenmate` |
| Complete user manual for your Screenmate OneCable portable monitor | `Manuel d'utilisation complet de votre écran portable Screenmate OneCable` |
| Complete user manual for your Screenmate Lite portable monitor | `Manuel d'utilisation complet de votre écran portable Screenmate Lite` |
| Complete user manual for your Screenmate Lite 144 Hz portable monitor | `Manuel d'utilisation complet de votre écran portable Screenmate Lite 144 Hz` |
| Complete user manual for your Screenmate Dual Flip 16\" foldable dual-screen extension | `Manuel d'utilisation complet de votre extension double écran pliable Screenmate Dual Flip 16\"` |
| Complete user manual for your Screenmate Flip — available in 14\" and 15.6\" | `Manuel d'utilisation complet de votre Screenmate Flip — disponible en 14\" et 15,6\"` |
| Complete user manual for your Screenmate Expand triple-screen portable monitor, available in 14\" and 15.6\" | `Manuel d'utilisation complet de votre écran portable triple Screenmate Expand, disponible en 14\" et 15,6\"` |
| Complete user manual for your Screenmate Infinity dual portable monitor | `Manuel d'utilisation complet de votre double écran portable Screenmate Infinity` |
| Complete user manual for your Screenmate Infinity Lite portable display extension | `Manuel d'utilisation complet de votre extension d'écran portable Screenmate Infinity Lite` |
| Complete user manual for your Screenmate One 4K 15.6\" portable monitor | `Manuel d'utilisation complet de votre écran portable Screenmate One 4K 15,6\"` |
| Complete user manual for your Screenmate One 4K OLED 15.6\" portable monitor | `Manuel d'utilisation complet de votre écran portable Screenmate One 4K OLED 15,6\"` |
| Complete user manual for your Screenmate Panorama 15.6\" triple-screen portable monitor | `Manuel d'utilisation complet de votre écran portable triple Screenmate Panorama 15,6\"` |
| Installation and connecting your Screenmate OneCable | `Installer et connecter votre Screenmate OneCable` |
| Setting up and connecting your Screenmate Dual Flip | `Installer et connecter votre Screenmate Dual Flip` |
| Setting up and connecting your Screenmate Expand | `Installer et connecter votre Screenmate Expand` |
| Setting up and connecting your Screenmate Infinity | `Installer et connecter votre Screenmate Infinity` |
| Setting up and connecting your Screenmate Panorama | `Installer et connecter votre Screenmate Panorama` |
| Connecting your Screenmate Lite | `Connecter votre Screenmate Lite` |
| Connecting your Screenmate Lite 144 Hz | `Connecter votre Screenmate Lite 144 Hz` |
| Connecting your Screenmate One 4K | `Connecter votre Screenmate One 4K` |
| Connecting your Screenmate One 4K OLED | `Connecter votre Screenmate One 4K OLED` |
| Unfolding, connecting and storing your Screenmate Flip | `Déplier, connecter et ranger votre Screenmate Flip` |
| Unfolding, setting up and storing your Screenmate Infinity Lite | `Déplier, installer et ranger votre Screenmate Infinity Lite` |
| Overview of ports and control buttons | `Aperçu des ports et des boutons de commande` |
| Overview of ports and the multifunctional button | `Aperçu des ports et du bouton multifonction` |
| Display settings via the on-screen menu | `Réglages d'affichage via le menu à l'écran` |
| Adjusting display settings via the on-screen menu | `Régler les paramètres d'affichage via le menu à l'écran` |
| Per-screen display settings via the on-screen menu | `Réglages d'affichage par écran via le menu à l'écran` |
| Display settings for Windows and macOS | `Réglages d'affichage pour Windows et macOS` |
| Configuring your displays on Windows and macOS | `Configurer vos écrans sous Windows et macOS` |
| Configuring extra screens and audio output on Windows and macOS | `Configurer les écrans supplémentaires et la sortie audio sous Windows et macOS` |
| Configure display and sound output on Windows and macOS | `Configurer l'affichage et la sortie audio sous Windows et macOS` |
| Driver installation for Windows | `Installation du pilote pour Windows` |
| Driver installation for macOS | `Installation du pilote pour macOS` |
| Frequently asked questions and troubleshooting | `Questions fréquentes et dépannage` |
| Important safety information and warnings | `Informations de sécurité et avertissements importants` |

### 9.3 H1 and H2 headings (1 + 55 unique)

| English | French |
|---|---|
| `# Welcome to Screenmate Manuals` | `# Bienvenue dans les manuels Screenmate` |
| `## Available Manuals` | `## Manuels disponibles` |
| `## Need Help?` | `## Besoin d'aide&nbsp;?` |
| `## What is the Screenmate OneCable?` | `## Qu'est-ce que le Screenmate OneCable&nbsp;?` |
| `## What is the Screenmate Lite?` | `## Qu'est-ce que le Screenmate Lite&nbsp;?` |
| `## What is the Screenmate Lite 144 Hz?` | `## Qu'est-ce que le Screenmate Lite 144 Hz&nbsp;?` |
| `## What is the Screenmate Dual Flip?` | `## Qu'est-ce que le Screenmate Dual Flip&nbsp;?` |
| `## What is the Screenmate Flip?` | `## Qu'est-ce que le Screenmate Flip&nbsp;?` |
| `## What is the Screenmate Expand?` | `## Qu'est-ce que le Screenmate Expand&nbsp;?` |
| `## What is the Screenmate Infinity?` | `## Qu'est-ce que le Screenmate Infinity&nbsp;?` |
| `## What is the Screenmate Infinity Lite?` | `## Qu'est-ce que le Screenmate Infinity Lite&nbsp;?` |
| `## What is the Screenmate One 4K?` | `## Qu'est-ce que le Screenmate One 4K&nbsp;?` |
| `## What is the Screenmate One 4K OLED?` | `## Qu'est-ce que le Screenmate One 4K OLED&nbsp;?` |
| `## What is the Screenmate Panorama?` | `## Qu'est-ce que le Screenmate Panorama&nbsp;?` |
| `## Package Contents` | `## Contenu de l'emballage` |
| `## Technical Specifications` | `## Caractéristiques techniques` |
| `## Getting Started` | `## Pour commencer` |
| `## Choose Your Cables` | `## Choisir vos câbles` |
| `## Protective Cap` | `## Capuchon de protection` |
| `## Installation Instructions` | `## Instructions d'installation` |
| `## Installation Steps` | `## Étapes d'installation` |
| `## Physical Setup` | `## Installation physique` |
| `## Setup` | `## Installation` |
| `## Unfolding the Screens` | `## Déplier les écrans` |
| `## Connection Options` | `## Options de connexion` |
| `## Using with 2 USB Cables` | `## Utilisation avec 2 câbles USB` |
| `## Charging the Screenmate OneCable` | `## Recharger le Screenmate OneCable` |
| `## Install the Display Driver` | `## Installer le pilote d'affichage` |
| `## Driver Installation for Windows` | `## Installation du pilote pour Windows` |
| `## Driver Installation for macOS` | `## Installation du pilote pour macOS` |
| `## If the Driver Doesn't Work` | `## Si le pilote ne fonctionne pas` |
| `## Storage` | `## Rangement` |
| `## Storing the Screenmate` | `## Ranger le Screenmate` |
| `## Ports and Buttons` | `## Ports et boutons` |
| `## Buttons and Functions` | `## Boutons et fonctions` |
| `## Controls and OSD Menu` | `## Commandes et menu OSD` |
| `## On-Screen Menu (OSD)` | `## Menu à l'écran (OSD)` |
| `## On-Screen Menu Settings` | `## Réglages du menu à l'écran` |
| `## Introduction to the OSD` | `## Introduction au menu OSD` |
| `## Using the OSD` | `## Utiliser l'OSD` |
| `## Using the OSD Menu` | `## Utiliser le menu OSD` |
| `## OSD Settings` | `## Réglages OSD` |
| `## Per-Screen Settings` | `## Réglages par écran` |
| `## Backlight` | `## Rétroéclairage` |
| `## Image` | `## Image` |
| `## Color` | `## Couleur` |
| `## Settings` | `## Réglages` |
| `## Reset` | `## Réinitialisation` |
| `## Other` | `## Autres` |
| `## Display Configuration` | `## Configuration de l'affichage` |
| `## Display Configuration (OS-Level)` | `## Configuration de l'affichage (système d'exploitation)` |
| `## Display Configuration Windows` | `## Configuration de l'affichage Windows` |
| `## Display Configuration macOS` | `## Configuration de l'affichage macOS` |
| `## Arrange Your Displays (Video)` | `## Organiser vos écrans (vidéo)` |
| `## Sound Settings` | `## Réglages du son` |
| `## Safety Instructions` | `## Consignes de sécurité` |
| `## FAQ` | `## FAQ` |

**Locked pairing:** `Display Configuration Windows` / `Display Configuration macOS` →
`Configuration de l'affichage Windows` / `Configuration de l'affichage macOS`, with the frontmatter
title `Réglages d'affichage`. This chapter is byte-identical across OneCable, Flip, Dual Flip and
Expand on the EN and NL sides and must stay byte-identical across all four on the FR side. Change
one, change all four, in the same commit.

**Collision note:** `## Using the OSD` and `## Using the OSD Menu` are distinct EN headings and must
stay distinct in French (`Utiliser l'OSD` vs `Utiliser le menu OSD`). Do not collapse them.

### 9.4 H3 headings (107 unique, incl. two `<svg>`-suffixed variants)

For `### Windows <svg …>` and `### macOS <svg …>`, translate nothing — the heading text is already
a proper noun and the inline SVG is copied through untouched.

| English | French |
|---|---|
| `### Windows` | `### Windows` |
| `### Windows 10 or higher` | `### Windows 10 ou version ultérieure` |
| `### macOS` | `### macOS` |
| `### Ports` | `### Ports` |
| `### Side Ports` | `### Ports latéraux` |
| `### USB-C` | `### USB-C` |
| `### USB-C (for HDMI > USB-C)` | `### USB-C (pour HDMI vers USB-C)` |
| `### USB-C Port` | `### Port USB-C` |
| `### USB-C Port (Power)` | `### Port USB-C (alimentation)` |
| `### USB-C Port (Power & Video)` | `### Port USB-C (alimentation et vidéo)` |
| `### USB-C Port (Data/Video/Power)` | `### Port USB-C (données/vidéo/alimentation)` |
| `### USB-C Port (Power Only / Power Delivery)` | `### Port USB-C (alimentation uniquement / Power Delivery)` |
| `### USB-C Charging Port` | `### Port de charge USB-C` |
| `### USB-A Port` | `### Port USB-A` |
| `### HDMI Port` | `### Port HDMI` |
| `### Mini HDMI` | `### Mini-HDMI` |
| `### Mini HDMI Port` | `### Port Mini-HDMI` |
| `### 3 × Mini HDMI Ports` | `### 3 × ports Mini-HDMI` |
| `### 3.5 mm Headphone Jack` | `### Prise casque 3,5&nbsp;mm` |
| `### 3.5mm Headphone Jack` | `### Prise casque 3,5&nbsp;mm` *(EN spacing variant, same French)* |
| `### Speaker` | `### Haut-parleur` |
| `### Indicator Light` | `### Voyant lumineux` |
| `### LED Indicator` | `### Voyant LED` |
| `### Buttons` | `### Boutons` |
| `### Control Buttons` | `### Boutons de commande` |
| `### Brightness Buttons` | `### Boutons de luminosité` |
| `### + and − Buttons` | `### Boutons + et −` |
| `### + Button (Increase Brightness)` | `### Bouton + (augmenter la luminosité)` |
| `### − Button (Decrease Brightness)` | `### Bouton − (diminuer la luminosité)` |
| `### Up Button (+)` | `### Bouton Haut (+)` |
| `### Down Button (−)` | `### Bouton Bas (−)` |
| `### Power Button` | `### Bouton d'alimentation` |
| `### Power & Return Button` | `### Bouton d'alimentation et de retour` |
| `### Menu Button (Power / OSD)` | `### Bouton Menu (alimentation / OSD)` |
| `### Menu / Select / Confirm` | `### Menu / Sélectionner / Confirmer` |
| `### Menu / Selection / Confirm Button` | `### Bouton Menu / Sélection / Confirmation` |
| `### Confirm / Exit Button` | `### Bouton Confirmer / Quitter` |
| `### M — OSD Menu Button` | `### M — bouton du menu OSD` |
| `### Multifunctional Button` | `### Bouton multifonction` |
| `### Left "Min" Button` | `### Bouton «&nbsp;Min&nbsp;» gauche` |
| `### Right "Plus" Button` | `### Bouton «&nbsp;Plus&nbsp;» droit` |
| `### Scroll Wheel` | `### Molette` |
| `### Brightness and volume` | `### Luminosité et volume` |
| `### Adjusting Brightness` | `### Régler la luminosité` |
| `### Adjusting Volume` | `### Régler le volume` |
| `### Volume and Brightness Shortcuts` | `### Raccourcis volume et luminosité` |
| `### Opening the OSD Menu` | `### Ouvrir le menu OSD` |
| `### OSD Lock` | `### Verrouillage de l'OSD` |
| `### 1. Backlight` | `### 1. Rétroéclairage` |
| `### 1. Brightness` | `### 1. Luminosité` |
| `### 2. Image` | `### 2. Image` |
| `### 2. Image Modes` | `### 2. Modes d'image` |
| `### 3. Color` | `### 3. Couleur` |
| `### 3. Color Settings` | `### 3. Réglages de couleur` |
| `### 4. Settings` | `### 4. Réglages` |
| `### 4. OSD Settings` | `### 4. Réglages OSD` |
| `### 5. Reset` | `### 5. Réinitialisation` |
| `### 6. Other` | `### 6. Autres` |
| `### Choose Your Cables` *(see H2)* | — |
| `### 1. Dual USB-C connection` | `### 1. Double connexion USB-C` |
| `### 1. Two USB-C Cables` | `### 1. Deux câbles USB-C` |
| `### 1. Two USB-C cables` | `### 1. Deux câbles USB-C` *(EN casing variant, same French)* |
| `### 2. USB-C + HDMI & USB-A connection` | `### 2. Connexion USB-C + HDMI et USB-A` |
| `### 2. 1x USB-C, 1x HDMI and 1x USB-A` | `### 2. 1 USB-C, 1 HDMI et 1 USB-A` |
| `### 2. One USB-C Cable, One HDMI Cable and One USB-A Cable` | `### 2. Un câble USB-C, un câble HDMI et un câble USB-A` |
| `### 2. One USB-C cable, one HDMI cable, and one USB-A cable` | `### 2. Un câble USB-C, un câble HDMI et un câble USB-A` *(EN casing variant, same French)* |
| `### 3. 2x USB-A and 2x HDMI` | `### 3. 2 USB-A et 2 HDMI` |
| `### 1. Laptop via USB-C cable` | `### 1. Ordinateur portable via câble USB-C` |
| `### 2. Laptop via HDMI cable` | `### 2. Ordinateur portable via câble HDMI` |
| `### 3. Phone or tablet via USB-C cable` | `### 3. Téléphone ou tablette via câble USB-C` |
| `### 4. USB-C game console` | `### 4. Console de jeu USB-C` |
| `### 5. Devices with an HDMI port` | `### 5. Appareils dotés d'un port HDMI` |
| `### Option 1 — USB-C (single cable)` | `### Option 1 — USB-C (câble unique)` |
| `### Option 2 — USB-A + HDMI` | `### Option 2 — USB-A + HDMI` |
| `### Smartphones and game consoles` | `### Smartphones et consoles de jeu` |
| `### Connect the Screenmate Infinity Lite to your laptop` | `### Connecter le Screenmate Infinity Lite à votre ordinateur portable` |
| `### Connect the Screenmate to your phone or other devices` | `### Connecter le Screenmate à votre téléphone ou à d'autres appareils` |
| `### Installation Steps` | `### Étapes d'installation` |
| `### Setup instructions` | `### Instructions de montage` |
| `### Unfolding the screen` | `### Déplier l'écran` |
| `### 1. Release the screen from the stand` | `### 1. Détacher l'écran du support` |
| `### 2. Attach the main stand` | `### 2. Fixer le support principal` |
| `### 3. Mount the screen support` | `### 3. Monter le support d'écran` |
| `### 4. Pull out the frame` | `### 4. Déployer le cadre` |
| `### 5. Adjust the stand` | `### 5. Régler le support` |
| `### 6. Open the screens` | `### 6. Ouvrir les écrans` |
| `### 7. Close the screens` | `### 7. Fermer les écrans` |
| `### Possible layouts` | `### Dispositions possibles` |
| `### Single screen` | `### Écran unique` |
| `### Dual screen — front and back horizontal` | `### Double écran — avant et arrière à l'horizontale` |
| `### Dual screen — front and back vertical` | `### Double écran — avant et arrière à la verticale` |
| `### Folding the screen back up` | `### Replier l'écran` |
| `### Folding caution` | `### Précaution lors du pliage` |
| `### Flip 14"` | `### Flip 14"` |
| `### Flip 15.6"` | `### Flip 15,6"` |
| `### Download Drivers` | `### Télécharger les pilotes` |
| `### Download Driver for macOS` | `### Télécharger le pilote pour macOS` |
| `### Manual Installation (if needed)` | `### Installation manuelle (si nécessaire)` |
| `### Before use` | `### Avant utilisation` |
| `### Check before use` | `### À vérifier avant utilisation` |
| `### Read this before use` | `### À lire avant utilisation` |
| `### My screen stays black and there's no image after connecting. What should I do?` | `### Mon écran reste noir et aucune image ne s'affiche après le branchement. Que faire&nbsp;?` |
| `### The screen is unstable, flickers or occasionally cuts out. What could be the cause?` | `### L'écran est instable, scintille ou se coupe par moments. Quelle peut en être la cause&nbsp;?` |
| `### My laptop doesn't have a USB-C port. How can I still use the Screenmate?` | `### Mon ordinateur portable n'a pas de port USB-C. Puis-je quand même utiliser le Screenmate&nbsp;?` |
| `### A startup logo appears, but there's no image on my MacBook. What should I do?` | `### Un logo de démarrage apparaît, mais aucune image ne s'affiche sur mon MacBook. Que faire&nbsp;?` |
| `### Can the Screenmate charge my laptop when connected to a power source?` | `### Le Screenmate peut-il recharger mon ordinateur portable lorsqu'il est branché sur une source d'alimentation&nbsp;?` |

---

## 10. Recurring boilerplate — locked once, reused everywhere

These blocks are repeated verbatim across many products in the EN corpus. Translate them **once**
and paste the identical French into every product so `fr/` keeps the same cross-product identity
`en/` has.

| English (recurring) | Locked French |
|---|---|
| `**Welcome!** This is your complete digital manual for the Screenmate X. Use the navigation menu on the left to jump to each section.` | `**Bienvenue&nbsp;!** Voici le manuel numérique complet de votre Screenmate X. Utilisez le menu de navigation à gauche pour accéder à chaque section.` |
| `This section provides an overview of all physical ports and control buttons on the Screenmate X.` | `Cette section présente l'ensemble des ports physiques et des boutons de commande du Screenmate X.` |
| `This section gives an overview of all physical ports and control buttons on the Screenmate X.` | `Cette section présente l'ensemble des ports physiques et des boutons de commande du Screenmate X.` |
| `**Important Information:**` | `**Informations importantes&nbsp;:**` |
| `Take good care of your Screenmate X and do not press on the screens to prevent damage.` | `Prenez soin de votre Screenmate X et n'appuyez pas sur les écrans afin d'éviter tout dommage.` |
| `The Screenmate consumes a small amount of power in standby mode. For energy-efficient operation, we recommend disconnecting the power cable when the monitor is not in use.` | `Le Screenmate consomme une faible quantité d'énergie en mode veille. Pour une utilisation économe en énergie, nous vous recommandons de débrancher le câble d'alimentation lorsque le moniteur n'est pas utilisé.` |
| `Please read the following guidelines carefully before using the monitor. They ensure safe operation and extend the lifespan of your Screenmate.` | `Lisez attentivement les consignes suivantes avant d'utiliser le moniteur. Elles garantissent une utilisation sûre et prolongent la durée de vie de votre Screenmate.` |
| `Always use this product in a safe and responsible manner. Read the following guidelines carefully to avoid risks such as electric shock or fire.` | `Utilisez toujours ce produit de manière sûre et responsable. Lisez attentivement les consignes suivantes afin d'éviter tout risque d'électrocution ou d'incendie.` |
| `Recommended ambient temperature: between -20°C and 60°C.` | `Température ambiante recommandée&nbsp;: entre -20&nbsp;°C et 60&nbsp;°C.` |
| `The monitor operates on a DC input between 5V and 20V (with a tolerance of ±2V).` | `Le moniteur fonctionne avec une entrée CC comprise entre 5&nbsp;V et 20&nbsp;V (avec une tolérance de ±2&nbsp;V).` |
| `Suitable for both home and business use.` | `Convient à un usage domestique comme professionnel.` |
| `The Screenmate X supports five connection scenarios. Pick the one that matches your device and available cables.` | `Le Screenmate X prend en charge cinq scénarios de connexion. Choisissez celui qui correspond à votre appareil et aux câbles dont vous disposez.` |
| `**Important:** If the connected device doesn't supply enough power, the monitor needs to be powered separately via an additional power source.` | `**Important&nbsp;:** si l'appareil connecté ne fournit pas une puissance suffisante, le moniteur doit être alimenté séparément par une source d'alimentation supplémentaire.` |
| `**Note:** The HDMI port does not deliver power, so the Screenmate must be connected to a power source of 5V/2A or higher.` | `**Remarque&nbsp;:** le port HDMI ne fournit pas d'alimentation&nbsp;; le Screenmate doit donc être raccordé à une source d'alimentation de 5&nbsp;V/2&nbsp;A ou plus.` |
| `Your browser does not support the video tag.` | `Votre navigateur ne prend pas en charge la balise vidéo.` |
| `Once both connections are made, the video signal appears automatically on the monitor.` | `Une fois les deux connexions établies, le signal vidéo s'affiche automatiquement sur le moniteur.` |
| `**Scanning a QR code?** Your QR code should have taken you directly to your product manual. If you need a different manual, select it from the list above.` | `**Vous scannez un QR code&nbsp;?** Votre QR code devrait vous avoir mené directement au manuel de votre produit. Si vous cherchez un autre manuel, sélectionnez-le dans la liste ci-dessus.` |
| `Contact Support` / `Get help from our support team` | `Contacter le support` / `Obtenez de l'aide auprès de notre équipe d'assistance` |
| `Shop Products` / `Browse all Screenmate products` | `Voir les produits` / `Parcourez tous les produits Screenmate` |
| `Warranty Info` / `Learn about product warranties` | `Informations de garantie` / `En savoir plus sur les garanties produit` |
| `{Product} Manual` *(card titles on the index page)* | `Manuel {Product}` |
| `Find the complete digital manual for your Screenmate product. Each manual includes setup instructions, troubleshooting guides, and technical specifications.` | `Retrouvez le manuel numérique complet de votre produit Screenmate. Chaque manuel contient les instructions d'installation, les guides de dépannage et les caractéristiques techniques.` |

### 10.1 JSX-embedded strings — attributes, captions, link text

**These are invisible to a heading/frontmatter sweep.** They live inside JSX attributes and inside
`<div>` / `<p>` / `<a>` elements, so `grep "^#"` and `grep "^title:"` never see them. This section
is the complete inventory.

**Extraction method — AST, not regex.** The list below was produced by parsing every EN `.mdx` to
an mdast tree (`mdast-util-from-markdown` + `mdast-util-mdx` + `micromark-extension-mdxjs`, the
same stack `mint` uses) and walking `mdxJsxFlowElement` / `mdxJsxTextElement` nodes for
user-visible attributes and text children. **Do not re-derive this list with a regex** — three
documented regex traps defeat the obvious patterns:

1. `<a[^>]*>[^<]+</a>` finds nothing here: the `<a>` wraps a multi-line `<svg>` before its text, so
   the label is not in the same match group.
2. A `<p>` pattern that excludes `>` silently drops the two OneCable cable captions, because the
   caption text itself contains a literal `>` (`2x USB-A > USB-C Cable`).
3. Tab-title inch marks are `&quot;`-escaped in the source; a regex reading the decoded value will
   round-trip a literal `"` back into the attribute and break the MDX parse.

#### A. `<Tab title=…>` — `&quot;` is mandatory, and the decimal comma applies

The inch mark inside a JSX attribute **must** stay as the entity `&quot;`. A literal `"` terminates
the attribute string and is a hard MDX parse error. The decimal comma applies inside the attribute
exactly as it does in body copy — verified against the NL precedent, which already ships
`Expand 15,6&quot;` (`nl/manuals/expand/index.mdx:33`).

| EN source (verbatim) | FR source (verbatim) |
|---|---|
| `<Tab title="OneCable 16&quot;" icon="display">` | `<Tab title="OneCable 16&quot;" icon="display">` |
| `<Tab title="OneCable 14&quot;" icon="display">` | `<Tab title="OneCable 14&quot;" icon="display">` |
| `<Tab title="Expand 15.6&quot;" icon="display">` | `<Tab title="Expand 15,6&quot;" icon="display">` |
| `<Tab title="Expand 14&quot;" icon="display">` | `<Tab title="Expand 14&quot;" icon="display">` |
| `<Tab title="Flip 15.6&quot;" icon="display">` | `<Tab title="Flip 15,6&quot;" icon="display">` |
| `<Tab title="Flip 14&quot;" icon="display">` | `<Tab title="Flip 14&quot;" icon="display">` |
| `<Tab title="Windows">` | `<Tab title="Windows">` |
| `<Tab title="macOS">` | `<Tab title="macOS">` |

Only the two `15.6` titles change. `14` and `16` are whole numbers and carry no separator.
The `icon="display"` attribute is machine-facing — never translate it.

#### B. Port-icon captions and OS tab labels — DNT, unchanged

These `<p>` captions sit under the connector icons in the "Choose Your Cables" figures and are
connector names, not prose.

| EN caption | FR caption |
|---|---|
| `USB-C` | `USB-C` |
| `USB-A` | `USB-A` |
| `USB-A 2.0` | `USB-A 2.0` |
| `HDMI` | `HDMI` |
| `Windows` | `Windows` |
| `macOS` | `macOS` |

#### C. Package / figure captions — including the two with a literal `>`

| EN caption | FR caption |
|---|---|
| `USB-C > USB-C Cable` | `Câble USB-C vers USB-C` |
| `2x USB-A > USB-C Cable` | `2 câbles USB-A vers USB-C` |
| `USB Stick (Incl. Driver)` | `Clé USB (pilote inclus)` |
| `Protective Case` | `Étui de protection` |

The `>` is expanded to `vers` per §2.1 — the caption form is not an exception to the cable chain.

#### D. Layout and stand captions (Infinity / Infinity Lite)

| EN caption | FR caption |
|---|---|
| `Landscape view` | `Disposition paysage` |
| `Portrait view` | `Disposition portrait` |
| `Portrait & landscape combination` | `Disposition mixte portrait et paysage` |
| `Detached view` | `Écrans détachés` |
| `The stand supports 360° rotation` | `Le support pivote à 360°` |
| `Place the screen on the single stand` | `Placez l'écran sur le support simple` |

**Disambiguation with §5.4.** §5.4 locks `landscape view` → `mode paysage` for the *OS display
orientation* sense (the Windows/macOS rotation setting). These captions describe the *physical
arrangement of the stands*, so they take `Disposition …`, matching their own section heading
`### Possible layouts` → `### Dispositions possibles`. Both renderings are correct in their own
context; pick by which one the surrounding page is about.

#### E. `<a>` link text (wrapped around an inline `<svg>` — regex trap 1)

| EN link text | FR link text |
|---|---|
| `Download Windows Drivers` | `Télécharger les pilotes Windows` |
| `Download for macOS` | `Télécharger pour macOS` |

#### F. Bold prose leads in the display-settings chapter

This chapter is checksum-identical across products (§9.3), so these six strings must be translated
once and reused byte-for-byte everywhere they appear.

| EN | FR |
|---|---|
> **Source of truth: the shipped files, not this glossary.** These six renderings were
> reverse-derived from `fr/manuals/onecable/display-settings.mdx` and its siblings (shipped and
> QC'd in `7a96840`), which predate this section. My original independent derivation diverged on
> five of the six; the shipped forms below **win** and are now the locked forms. Never "correct" a
> shipped file to match an earlier glossary lock — the direction of travel is the other way.

| English | French (locked = shipped) | Occurrences |
|---|---|---|
| `**Want to extend your workspace?**` | `**Vous souhaitez étendre votre espace de travail&nbsp;?**` | 7 — all six display-settings pages |
| `**Screen upside down?**` | `**Écran à l'envers&nbsp;?**` | 10 — dual-flip, expand, flip, infinity-lite, onecable |
| `**Is a screen upside down?**` | `**Un écran est à l'envers&nbsp;?**` | 3 — infinity, infinity-lite |
| `**Need more overview?**` | `**Besoin d'une meilleure vue d'ensemble&nbsp;?**` | 6 — dual-flip, expand, flip, infinity-lite, onecable |
| `**Want more on-screen space?**` | `**Vous souhaitez plus d'espace à l'écran&nbsp;?**` | 1 — infinity |
| `**Working with three screens?**` | `**Vous travaillez avec trois écrans&nbsp;?**` | 1 — infinity-lite |

**The house pattern these establish** — apply it when a new question lead appears:

- `Want to …?` / `Want more …?` → **`Vous souhaitez …&nbsp;?`** (not `Envie de …`, not `Besoin de …`).
- A question stated as a fact keeps declarative word order plus `?` — **`Un écran est à l'envers&nbsp;?`**,
  not the inverted `Un écran est-il à l'envers&nbsp;?`. This matches the conversational register of
  the surrounding chapter.
- `Working with …?` → **`Vous travaillez avec …&nbsp;?`**, keeping the `Vous` + present-tense frame.
- `overview` in this chapter is **`vue d'ensemble`**, not `lisibilité` or `aperçu`.

#### G. `alt=` attributes — a rule, not a list

The corpus carries **144 unique `alt=` strings**. They are user-visible (screen readers, and
whenever an image fails to load), so they are translated — but they are ordinary descriptive prose
and are fully governed by the §5 term tables, so enumerating them here would add bulk without
adding determinism. The rule:

- Translate the descriptive part using §5 vocabulary.
- Keep verbatim: DNT tokens, OS UI labels (§8), file/folder/app names (`DRIVERS (D:)`, `UsbDisplay`,
  `RacerUSB`, `Win10&11`), and device identifiers (`S6-L`, `Type-C1`).
- `Step 1: open This PC …` → `Étape 1&nbsp;: ouvrir Ce PC …` — the `&nbsp;` rule applies inside
  attributes too (verified: entities decode correctly in JSX attribute values).
- **Never translate** `src`, `href`, `className`, `icon`, `viewBox`, `type` — machine-facing.
- Image paths are URL-encoded and language-independent: never touch a `src` even when it contains
  Dutch words (`Handleiding%20images`, `Aansluitmogelijkheden.png`).

#### H. Not user-visible — leave in English

`title="[Product Name] Manual"` at `en/manuals-index.mdx:73` sits inside a `{/* … */}` scaffold
comment for adding future products. It never renders. Leave it, and its sibling
`href="/en/manuals/[product-slug]/index"`, exactly as-is — including the `/en/` path.

#### I. Callout lead-ins and bare text children

Two more classes that no attribute- or tag-based pattern can reach. Both are already locked in §10;
they are restated here so this inventory is self-contained.

**Callout lead-ins** — bold text opening a `<Note>` block:

| EN | FR | Occurrences (verified) |
|---|---|---|
| `**Important Information:**` | `**Informations importantes&nbsp;:**` | 5 products — `dual-flip`, `expand`, `flip`, `infinity-lite`, `onecable`, all in `index.mdx` |
| `**Please note:**` | `**Remarque&nbsp;:**` | **1 occurrence only** — `flip/installation.mdx:73` |
| `**Note:**` | `**Remarque&nbsp;:**` | many |
| `**Important:**` | `**Important&nbsp;:**` | many |
| `**Caution:**` | `**Attention&nbsp;:**` | `panorama/installation.mdx` |
| `**Tip:**` | `**Conseil&nbsp;:**` | `infinity/installation.mdx` |

Note the `&nbsp;` before the colon per §3.1 — these lead-ins are the single most frequent site for
the French spacing rule in the whole corpus, and the colon sits inside the `**…**` run, which
§3.2 verified is safe with the entity form.

**Deliberate many-to-one merge:** EN `**Note:**` and `**Please note:**` both render as
`**Remarque&nbsp;:**`. French has no idiomatic distinction between them and `Veuillez noter` is the
literal-translation trap flagged in §6. This is intended — do not invent a second French form to
preserve an EN distinction that carries no meaning.

**Correction to the brief:** `Please note:` was described as recurring across 5 products. It does
not — it appears exactly once (`flip/installation.mdx:73`). Only `Important Information:` has the
5-product spread. This matters because it changes whether the string is frozen-chapter boilerplate
(it is not) or a one-off (it is).

**Bare text children of `<video>`** — wrapped in **no tag at all**, so `<p>`, `<a>` and attribute
patterns are all blind to it. My AST walk catches it because it visits text/paragraph nodes whose
*parent* is a JSX element, regardless of whether an inner tag exists:

| EN | FR | Occurrences (verified) |
|---|---|---|
| `Your browser does not support the video tag.` | `Votre navigateur ne prend pas en charge la balise vidéo.` | **14** — 2× in each of the six `display-settings.mdx`, plus 1× each in `onecable/installation-windows.mdx` and `onecable/installation-mac.mdx` |

Since 12 of the 14 sit in the checksum-identical display-settings chapter, this string must be
byte-identical everywhere. The `<source src=… type="video/mp4" />` sibling is machine-facing —
never translate `src` or `type`.

---

### 10.2 Bold run-in labels (body copy)

**A separate class from §10.1.** These are markdown `strong` nodes inside ordinary paragraphs and
list items — *not* JSX children — so the §10.1 AST sweep did not reach them, and a heading grep
never will either. The corpus has **89 unique `**…:**` run-ins** in total, distributed as:

| Group | Count | Handling |
|---|---|---|
| **Non-OSD run-ins** | **27** | **enumerated below** |
| Callout lead-ins (`Note:`, `Important:`, `Important Information:`, `Please note:`, `Caution:`, `Tip:`) | 6 | §10.1.I |
| ECO preset values (`Standard:`, `Game:`, `Movie:`, `Text:`, `RTS:`, `FPS:`) | 6 | device values — stay English (§7.1) |
| OSD glosses and CAPS-glossed forms (`Brightness (BRIGHTNESS):`, `Language:`, `Color Temperature:`, `ECO modes:`, …) | 34 | §7 CAPS table + §7.2 vocabulary |
| Range-suffixed variants (`Brightness (0–100):`, `OSD Timer (10–60 seconds):`, …) | 16 | **not enumerated** — generated by §7.3 pattern + §7.2 vocabulary |
| **Total unique** | **89** | 0 unresolved (verified) |

**The `&nbsp;` rule applies to every one of these** (§3.1). The colon sits inside the `**…**` run,
which §3.2 verified is safe with the entity and breaks with a literal U+00A0.

| English | French | Occurrences / where |
|---|---|---|
| `**Turn on:**` | `**Allumer&nbsp;:**` | 2 — `one-4k/osd`, `one-4k-oled/osd` |
| `**Open the OSD menu:**` | `**Ouvrir le menu OSD&nbsp;:**` | 2 — idem |
| `**Navigate:**` | `**Naviguer&nbsp;:**` | 2 — idem |
| `**Select:**` | `**Sélectionner&nbsp;:**` | 2 — idem |
| `**Adjust settings:**` | `**Régler les paramètres&nbsp;:**` | 2 — idem |
| `**Go back:**` | `**Revenir en arrière&nbsp;:**` | 2 — idem |
| `**Short press:**` | `**Appui court&nbsp;:**` | 3 — `infinity/controls`, `panorama/controls` |
| `**Long press:**` | `**Appui long&nbsp;:**` | 2 — `panorama/controls` |
| `**Long press (1 second):**` | `**Appui long (1 seconde)&nbsp;:**` | 1 — `panorama/controls` |
| `**Press and hold (2 seconds):**` | `**Appui prolongé (2 secondes)&nbsp;:**` | 1 — `infinity/controls` |
| `**Press and hold (3 seconds):**` | `**Appui prolongé (3 secondes)&nbsp;:**` | 1 — `infinity/controls` |
| `**Press right ("Plus"):**` | `**Appui vers la droite («&nbsp;Plus&nbsp;»)&nbsp;:**` | 1 — `infinity/controls` |
| `**Press left ("Min"):**` | `**Appui vers la gauche («&nbsp;Min&nbsp;»)&nbsp;:**` | 1 — `infinity/controls` |
| `**Power supply:**` | `**Alimentation&nbsp;:**` | 8 — `lite`, `lite-144hz`, `one-4k`, `one-4k-oled` installation |
| `**Connecting the console:**` | `**Connexion de la console&nbsp;:**` | 4 — idem |
| `**Connecting the HDMI device:**` | `**Connexion de l'appareil HDMI&nbsp;:**` | 4 — idem |
| `**Steps:**` | `**Étapes&nbsp;:**` | 1 — `expand/installation` |
| `**Extend your workspace:**` | `**Étendre votre espace de travail&nbsp;:**` | 1 — `panorama/osd` |
| `**Left screen:**` | `**Écran gauche&nbsp;:**` | 2 — `dual-flip/index`, `expand/index` |
| `**Right screen:**` | `**Écran droit&nbsp;:**` | 2 — idem |
| `**USB-C Port:**` | `**Port USB-C&nbsp;:**` | 4 — `expand/controls`, `flip/controls` |
| `**Mini HDMI:**` | `**Mini-HDMI&nbsp;:**` | 2 — idem (hyphenated per §2) |
| `**+ button:**` | `**Bouton +&nbsp;:**` | 2 — `one-4k/controls`, `one-4k-oled/controls` |
| `**− button:**` | `**Bouton −&nbsp;:**` | 2 — idem |
| `**≡ Menu button:**` | `**≡ Bouton Menu&nbsp;:**` | 1 — `expand/controls` |
| `**− Decrease brightness:**` | `**− Diminuer la luminosité&nbsp;:**` | 1 — `expand/controls` |
| `**+ Increase brightness:**` | `**+ Augmenter la luminosité&nbsp;:**` | 1 — `expand/controls` |

**Notes.**

- The glyphs `+`, `−` (U+2212), `≡` are button engravings — copy verbatim, keep them in their EN
  position (leading), and do not swap `−` for a hyphen.
- `Short press` / `Long press` become nouns in French (`Appui court` / `Appui long`), not verbs.
  This matches the corpus, where they label a gesture rather than instruct.
- `Press and hold (n seconds)` → `Appui prolongé (n secondes)` — note `seconds` → `secondes`,
  the same unit-word trap as §7.3.
- `Press right ("Plus")` uses guillemets per §3.5, matching the `### Bouton «&nbsp;Plus&nbsp;» droit`
  heading in §9.4.
- `**Power supply:**` is the run-in label (8×) and is distinct from the prose noun
  `alimentation` in §5.2 — same French word, but here it must keep the bold-and-colon structure.

---

## 11. Verification greps (run before declaring a French page done)

```
# 1. Register — any hit is a defect (see §1 for expected false positives)
grep -nEi '\b(tu|toi|ton|ta|tes)\b' fr/manuals/**/*.mdx

# 2. Plain space before French punctuation — must be &nbsp;
#    (excludes ratios/URLs/times, which have no space before the colon anyway)
grep -nE '[^ |] [:;!?]( |$)' fr/manuals/**/*.mdx

# 3. Banned narrow no-break space U+202F
LC_ALL=C.UTF-8 grep -rnP '\x{202F}' fr/

# 4. Literal U+00A0 outside frontmatter (should be zero — use &nbsp; in body copy)
LC_ALL=C.UTF-8 grep -rnP '\x{00A0}' fr/

# 5. Typographic apostrophe U+2019 — must be zero, corpus uses ASCII '
LC_ALL=C.UTF-8 grep -rnP '\x{2019}' fr/

# 6. Period decimals that should be commas
grep -nE '[0-9]\.[0-9] ?(cm|mm|m|"|pouces)' fr/manuals/**/*.mdx

# 7. Closed unit forms that should carry a non-breaking space
grep -nE '[0-9](W|V|A|Hz|ms|%)\b' fr/manuals/**/*.mdx

# 8. Broken cable chain — must be "câble A vers B"
grep -nE 'câble [A-Za-z0-9-]+ (à|>|/|-) [A-Za-z0-9-]+' fr/manuals/**/*.mdx

# 9. Hyphen-chain compounds (German/Dutch pattern leaking into French)
grep -nEi '(USB-[CA]|HDMI)-(câble|port|adaptateur|chargeur)' fr/manuals/**/*.mdx

# 10. Unhyphenated connector tokens
grep -nE 'USB C|USBC|Mini HDMI' fr/manuals/**/*.mdx

# 11. Untranslated "driver" in body prose (only the caps DRIVERS drive/folder keeps EN)
grep -nE '\bdriver(s)?\b' fr/manuals/**/*.mdx

# 14. English/German thousands separator on the contrast figure (want zero hits)
grep -nE '100[,.]000' fr/manuals/**/*.mdx

# 15. JSX-embedded strings left untranslated (want zero hits) — see §10.1
grep -nE 'Tab title="(Expand|Flip|OneCable) [0-9.]+&quot;' fr/manuals/*/index.mdx | grep -E '15\.6'
grep -rnE 'Landscape view|Portrait view|Detached view|Protective Case|USB Stick \(Incl' fr/
grep -rn 'does not support the video tag' fr/            # EN string must be gone
grep -rn 'Important Information:|Please note:|Download Windows Drivers' fr/

# 16. Literal " inside a JSX attribute (hard MDX parse error) — want zero hits
grep -rnE '<Tab title="[^"]*[0-9]"' fr/manuals/*/index.mdx

# 17. Glossary-vs-shipped drift on the frozen question leads (§10.1.F) — want zero hits.
#     Any hit means someone applied a pre-7a96840 glossary lock to a shipped page.
grep -rnE "Envie d'étendre|Besoin de plus de lisibilité|est-il à l'envers|Vous utilisez trois écrans|Besoin de plus d'espace à l'écran" fr/

# 18. Frozen display-settings body parity across the four products (must print nothing)
for p in dual-flip flip expand; do
  a=$(awk 'f>1{print} /^---$/{f++}' fr/manuals/onecable/display-settings.mdx | md5sum)
  b=$(awk 'f>1{print} /^---$/{f++}' fr/manuals/$p/display-settings.mdx | md5sum)
  [ "$a" = "$b" ] || echo "FROZEN CHAPTER DRIFT: $p"
done

# 12. Structural parity with en/ (must print nothing)
for f in $(cd en && find . -name '*.mdx'); do
  a=$(grep -c '^#\{1,4\} ' "en/$f"); b=$(grep -c '^#\{1,4\} ' "fr/$f")
  [ "$a" = "$b" ] || echo "HEADING COUNT MISMATCH $f: en=$a fr=$b"
done

# 13. Required link frontmatter on every page
grep -L 'en_link:' fr/manuals/**/*.mdx fr/manuals-index.mdx
```

Grep 2 is the workhorse for §3. It flags `Remarque :` (plain space) and passes
`Remarque&nbsp;:`. Ratios like `16:9` have no space before the colon and are correctly ignored.

---

## 12. Adding to the glossary

If you meet a term that is not listed here, do **not** invent a rendering and move on. Propose it:

```
Proposed glossary addition:
| {English} | {French} | {notes} | {keep EN?} |
Reason: {file:line where it appears} + {why this French rendering}
```

### Open items for the orchestrator / client

**Resolved at the glossary gate (2026-08-11) — no further action:**

- ✅ **`DisplayPort`** added to `translations/dnt.json` (gate R3). `DisplayPort Alt Mode` is covered
  by that token; §5.2 updated.
- ✅ **`Drivers` → `DRIVERS`** in `dnt.json` (gate R3). Confirms the §5.3 split: the caps drive/folder
  name stays EN, the lowercase common noun is always `pilote(s)`.
- ✅ **`100,000:1` → `100 000:1`** locked (gate R5), with the plain-vs-`&nbsp;` space rule in §4.1.
- ✅ **`reverse charging` → `charge inversée`** confirmed, with the EN gloss on first use. Client
  sign-off recorded in the delivery doc.
- ✅ **OSD chapter headings translate** (`## Backlight` → `## Rétroéclairage`) — gate R1, §7.

**Still open:**

1. **`DP`** (as in `DP monitor`, `panorama/osd.mdx:31`) — considered during the Task 2 DNT
   reconciliation and deliberately left out; still absent after the R3 realign. FR renders it
   `moniteur DP`. Adding it would make DE/FR/IT handling of it explicit rather than incidental.
2. **Unit spacing (`45 W`, `100 %`, `-20 °C`)** deliberately diverges from the EN source and from
   the Dutch glossary. This is correct French typography, but it is a visible difference from the
   NL pages if anyone diffs them side by side. Confirm with the client if they compare languages.
3. **`100 000:1` uses a wrappable plain space** per the R5 ruling. Accepted tradeoff, documented in
   §4.1; the `100&nbsp;000:1` fallback is verified working if a wrap is ever reported.

**Round-4 proposals — §10-locked strings, NOT applied, awaiting client sign-off (2026-08-12).**
Both round-4 fluency reviewers independently flagged these as calques. Each sits on a §10 locked
boilerplate string reused across 3–5 products (and, for the `Évitez … afin d'éviter` items, inside a
**frozen** `safety.mdx` body), so per the §10 lock and the `safety-align-fr.md` precedent none was
changed unilaterally. Applying any of them means editing the glossary row **and** re-propagating to
every affected file in one commit.

| # | Locked FR string | Proposed | Where | Flagged by |
|---|---|---|---|---|
| R4-P1 | `Pour une utilisation économe en énergie, nous vous recommandons de débrancher le câble d'alimentation lorsque le moniteur n'est pas utilisé.` | `Pour limiter la consommation, débranchez le câble d'alimentation lorsque vous n'utilisez pas le moniteur.` | `index.mdx` ×4 (onecable, flip, dual-flip, expand) | fluency-fr-a **Major**, fluency-fr-b **Major** — nominal calque + `utilisation … utilisé` |
| R4-P2 | `Votre QR code devrait vous avoir mené directement au manuel de votre produit.` | `En principe, votre QR code vous a conduit directement au manuel de votre produit.` | `fr/manuals-index.mdx` ×1 | fluency-fr-a **Major** — conditional-past calque |
| R4-P3 | `écran portable triple` | `triple écran portable` | §5.1 term + §9.2 descriptions; `expand/index.mdx`, `panorama/index.mdx` | fluency-fr-a **Major**, fluency-fr-b **Major** — adjective order; the range already ships `double écran portable` for the dual product |
| R4-P4 | `Lumière bleue faible (LOW BLUE LIGHT)` | `Réduction de la lumière bleue (LOW BLUE LIGHT)` | §7 CAPS table, §7.2; `flip/osd.mdx`, `expand/osd.mdx` | fluency-fr-a **Major** — no French product labels the feature this way |
| R4-P5 | `Évitez toute exposition à l'humidité … afin d'éviter tout dommage…` / `Évitez les espaces humides … afin d'éviter…` | `… afin de ne pas endommager les composants électroniques` / `Évitez les environnements humides …` | **frozen** `safety.mdx` bodies (Group A ×7, infinity group ×3) | fluency-fr-a **Major**, fluency-fr-b **Major** — same verb twice; `espaces humides` |
| R4-P6 | `Utilisez uniquement l'adaptateur CA/CC fourni comme alimentation.` | `Utilisez uniquement l'adaptateur secteur (CA/CC) fourni.` | **frozen** `safety.mdx` bodies | fluency-fr-a **Major**, fluency-fr-b **Major** — `comme alimentation` calque of *as power supply* |
| R4-P7 | `Elles garantissent une utilisation sûre…` / `…adaptée à l'ampérage requis` | `Elles assurent un fonctionnement sûr…` / `…adaptée à l'intensité requise` | **frozen** `safety.mdx` bodies | `safety-align-fr.md` findings 1.1 / 1.2 (Minor) — carried forward unchanged |
