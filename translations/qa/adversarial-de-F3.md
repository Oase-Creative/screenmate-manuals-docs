# Adversarial review — DE, family F3 (`flip` + `dual-flip`)

Branch `lang-expansion-de-fr-it`. 12 files reviewed against **both** sources (EN structural
template + NL prior art) and `translations/glossary-de.md`.

**Verdict:** no critical defects. The frozen shared chapters are intact, register is clean,
and every mechanical sweep passes. One release-gate structural gap (F1) and eleven
copy-level findings, none blocking.

Severity key: **Critical** (breaks build / frozen-chapter divergence / safety meaning
inverted) · **Major** (ships wrong or incomplete) · **Minor** (meaning or glossary drift a
German reader would notice) · **Nit** (style, consistency, polish).

Known non-defects were checked and are **excluded** by instruction: dual-flip OSD bare CAPS
tokens (glossary carve-out), Dutch screenshots, the EN `Color Gamut` / `Color Accuracy`
split (client flag), DIN 5008 unit spacing.

---

## Findings

| # | File | Line — quote | Problem | Sev | Proposed fix |
|---|---|---|---|---|---|
| F1 | all 12 F3 files | frontmatter: `title:` / `description:` / `icon:` — **no `*_link:` key** | Every EN page carries `nl_link:` and every NL page carries `en_link:` (61/61 each). The DE tree has **0/61** — as do FR and IT. Per the locked language-switcher architecture (`ab10152`), cross-language link frontmatter is required on every page; without it the switcher cannot preserve the current page and lands the reader on an index. `scripts/generate_language_links.py` exists but has not been run against the expansion trees. Branch-wide, not F3-specific, but it makes all 12 F3 pages incomplete. | **Major** | Run `scripts/generate_language_links.py` for `de/`, `fr/`, `it/` and re-emit `en_link`/`nl_link`/`de_link` across all trees before release. |
| F2 | `de/manuals/dual-flip/installation.mdx` | 51 — `Wenn du den Dual Flip nicht mehr brauchst, verstaue ihn so:` | Meaning drift vs **both** sources. EN `When you're done using the Dual Flip`, NL `Als je klaar bent met het gebruiken van de Dual Flip` — both mean "finished with it for now". `nicht mehr brauchst` = "no longer need it", which reads as permanent disposal, not end-of-session storage. | Minor | `Wenn du mit dem Dual Flip fertig bist, verstaue ihn so:` |
| F3 | `de/manuals/flip/osd.mdx` · `de/manuals/dual-flip/osd.mdx` | 43 — `Vereinfachtes Chinesisch` **vs** 43 — `Chinesisch (vereinfacht)` | Same EN string (`Simplified Chinese`), same product family, two different German renderings. Same line also splits on `Wähle die OSD-Sprache` (flip) vs `Wähle die Sprache des OSD` (dual-flip). NL is uniform (`Vereenvoudigd Chinees`) in both. This is exactly the per-file drift the glossary exists to prevent. | Minor | Normalise both files to `Vereinfachtes Chinesisch` and `Wähle die OSD-Sprache`. |
| F4 | `de/manuals/flip/installation.mdx` | 67 — `Verbinde die eine Seite des Screenmate mit dem mitgelieferten USB-C-Kabel mit deinem Laptop.` | Double `mit … mit` in one clause — clumsy German, and the instrumental vs directional roles collide. The sibling page renders the identical EN sentence correctly: `dual-flip/installation.mdx:41` uses `über das mitgelieferte USB-C-Kabel mit deinem Laptop`. | Minor | `Verbinde eine Seite des Screenmate über das mitgelieferte USB-C-Kabel mit deinem Laptop.` |
| F5 | `de/manuals/flip/installation.mdx` | 18 — `alt="Anschlüsse an der Seite des Screenmate Flip 14 Zoll: …"` | Expands the inch mark to `Zoll` **inside a product designation**. Glossary §4 states inches "do **not** expand to `Zoll`", and §1.2 makes `Flip 14"` a DNT product token. The same file writes `### Flip 14"` four lines below, so the page contradicts itself. (EN spells "14 inch" here, which likely prompted it.) | Minor | `alt="Anschlüsse an der Seite des Screenmate Flip 14&quot;: …"` — **note the parse hazard (§4.1): this is a JSX attribute, so the escape must be `&quot;`, never a literal `"`.** If the client prefers spelled-out units in assistive text, keep `Zoll` and record it as a deliberate alt-text exception. |
| F6 | `de/manuals/flip/index.mdx` | 15 — `ein faltbarer Multiscreen-Monitor, der um deinen Laptop herum geklappt wird` | Two problems. (a) Passive voice against §10.3 ("prefer the active voice"). (b) EN says the Flip **clips** around the laptop (`clips around your laptop`) — a mechanical attachment; `geklappt wird` says only that it folds. NL inherits the same softening (`klapt`), so DE compounds an existing drift rather than correcting it. The sibling dual-flip page renders the parallel EN correctly and actively (`die du an deinem Laptop befestigst`). | Minor | `… ein faltbarer Multiscreen-Monitor, den du um deinen Laptop klemmst und der dir zwei zusätzliche Bildschirme … gibt.` |
| F7 | `de/manuals/flip/index.mdx` | 8 — `für das 14"- und das 15,6"-Modell` | Drops the EN `covering **both** the 14" and 15.6" models` / NL `voor **zowel** het 14"- **als** het 15,6"-model`. The same file-set's `installation.mdx:9` renders the parallel EN construction with the full `Sowohl der Flip 14" als auch der Flip 15,6"`, so F3 handles "both" two ways. | Nit | `sowohl für das 14"- als auch für das 15,6"-Modell` |
| F8 | `de/manuals/flip/index.mdx` · `de/manuals/dual-flip/index.mdx` | 80 / 55 — `verbraucht im Standby-Modus etwas Strom` | Softens EN `a small amount of power` / NL `een kleine hoeveelheid stroom` to a vague "some power". The sentence exists to justify unplugging the cable, so the quantity matters. Consistent across both files, so it is one decision, not a slip. | Nit | `verbraucht im Standby-Modus eine geringe Menge Strom` |
| F9 | `de/manuals/flip/osd.mdx` · `de/manuals/dual-flip/osd.mdx` | 14/26/32/41/49/56 (×6 each) — `alt="OSD-Menü Hintergrundbeleuchtung"` | Bare space between two nouns forming a designation — the Deppenleerzeichen pattern §3.4 explicitly rejects (`Screenmate OneCable Handbuch`), whose prescribed fix is an appositive with an en dash. Gate ruling **R9** (logged in `translations/flags/de-dual-flip.md`) settles that alt text is *translated*; it says nothing about the *spacing* of the resulting apposition, so this is not a re-litigation of R9. 12 occurrences. | Nit | `alt="OSD-Menü – Hintergrundbeleuchtung"` (en dash per §3.6), applied to all 12. German quotes `„…"` would also be safe inside the attribute since they are not ASCII `"`. |
| F10 | `de/manuals/dual-flip/index.mdx` | 15 — `und wird über USB-C oder über USB-C + HDMI + USB-A angeschlossen` | Passive against §10.3, and drops the reader-agency the rest of the sentence already has (`die du an deinem Laptop befestigst … aufklappst`). NL keeps it active (`je sluit hem aan via`). Mid-sentence voice switch. | Nit | `… aufklappst. Jeder Bildschirm hat eine Auflösung von 2560 × 1600, und du schließt ihn über USB-C oder über USB-C + HDMI + USB-A an.` |
| F11 | `de/manuals/flip/controls.mdx` · `de/manuals/dual-flip/controls.mdx` | 9 — `Dieser Abschnitt gibt dir einen Überblick` **vs** 9 — `Dieser Abschnitt gibt einen Überblick` | Same-family split on the identical opening sentence. EN varies trivially (`gives` / `provides`) and does not motivate dropping the dative `dir`; the `du` register argues for keeping it in both. | Nit | Use `gibt dir einen Überblick` in both. |
| F12 | `de/manuals/flip/osd.mdx` | 59 — `Reduziert die Menge an blauem Licht vom Bildschirm` | `Menge an blauem Licht **vom** Bildschirm` is not idiomatic — `von` cannot govern a source-of-emission genitive here. (Faithful to EN `from the screen`, and the dual-flip sibling's `den Blaulichtanteil auf dem Bildschirm` is fine because its EN says `on the screen`, so this is flip-only.) | Nit | `Reduziert den Anteil des blauen Lichts, das der Bildschirm abgibt, und entlastet so die Augen.` |

**Count:** Critical 0 · Major 1 · Minor 5 · Nit 6 · **total 12**

---

## Scrutiny evidence

Everything below was executed, not assumed. Passing checks are listed because an
adversarial review has to show where it looked and found nothing.

### 1. Frozen shared chapters — PASS (the critical check)

Body checksums taken after stripping frontmatter (`awk` on the second `---`), so a
legitimate per-product `description` cannot mask a body divergence.

**`display-settings.mdx` — must be byte-identical across onecable / flip / dual-flip / expand:**

| Tree | onecable | flip | dual-flip | expand |
|---|---|---|---|---|
| DE | `e6f54bf0…` | `e6f54bf0…` | `e6f54bf0…` | `e6f54bf0…` |
| EN | `467551f5…` | `467551f5…` | `467551f5…` | `467551f5…` |
| NL | `88f65c86…` | `88f65c86…` | `88f65c86…` | `88f65c86…` |

All four DE copies identical; the DE partition matches EN's and NL's exactly. **No divergence.**

**`safety.mdx` — DE grouping vs EN grouping, all 11 products:**

| Group | EN hash | DE hash | Members |
|---|---|---|---|
| A | `b709f7d9…` | `cf3a7469…` | expand, **flip**, lite-144hz, lite, one-4k-oled, one-4k, onecable |
| B | `7b08b090…` | `7dea0485…` | **dual-flip** |
| C | `d0739e92…` | `33e8d276…` | infinity-lite |
| D | `5d0cd41d…` | `f1094236…` | infinity |
| E | `535f650e…` | `82792478…` | panorama |

The DE partition is **isomorphic to EN's** — same five groups, same membership. `flip` sits
in the shared 7-product group; `dual-flip` is legitimately its own because its EN source is
its own (bullets rather than a numbered list, otherwise identical wording). Both DE files
carry identical sentence text across the list-marker difference, which is correct.

**Frozen-chapter frontmatter:** `flip/display-settings.mdx` carries
`description: "Bildschirme unter Windows und macOS einrichten"` while the other three carry
`"Anzeigeeinstellungen für Windows und macOS"`. This **looks** like divergence and is not:
EN's flip page independently says `Configuring your displays on Windows and macOS` where
the other three say `Display settings for Windows and macOS`, and glossary §7.2 locks those
two EN strings to exactly these two different German targets. Faithful, inherited, correct.
All four share `title: "Anzeigeeinstellungen"` per the §7.3 locked exception.

### 2. Mechanical sweeps over all 12 DE F3 files — all PASS

| Sweep | Pattern | Result |
|---|---|---|
| Formal register | `\b(Sie\|Ihnen\|Ihr\|Ihre\|Ihrem\|Ihren\|Ihrer\|Ihres\|Bitte)\b` | **0 hits** — `du` register clean, no `Bitte` |
| Capitalised `Du`/`Dein` mid-sentence | `\b(Du\|Dein\|Deine\|Deinem\|Deinen\|Dir\|Dich)\b` | 4 hits, all sentence-initial `Dein Browser unterstützt das Video-Tag nicht.` — the §11.0 locked string. Clean |
| Em dash in body | `—` | **0 hits** — §3.6 satisfied (en dash `–` used throughout, incl. `M – OSD-Menütaste`) |
| Wrong quote marks | `»`, `«`, ASCII `'…'` | **0 hits** — German `„…"` only |
| Cable-chain violations | `zu`-connector, spaced chains, `→` | **0 hits** — `USB-C-auf-USB-C-Kabel`, `Mini-HDMI-auf-HDMI-Kabel`, `USB-C-auf-USB-A-Kabel` all correct, and the `USB-C to USB-A` **direction is preserved**, not normalised (§3.3) |
| Deppenleerzeichen | acronym + space + German noun | **0 hits** in body copy (the alt-text case F9 is a noun+noun apposition, caught separately) |
| Missing DIN unit space | `[0-9](W\|V\|A\|%\|Hz\|ms\|cm\|mm)` | 21 hits, **all inside `src=` image URLs** (`…Flip%2015.6%20-%20Handleiding…`). Zero in prose |
| Period decimals | `[0-9]\.[0-9]` | 20 hits, **all inside `src=` image URLs**. Zero in prose |
| `2x` instead of `2×` | `[0-9] ?x ?[0-9A-Z]` | **0 hits** — EN's `1x`/`2x` correctly became `1×`/`2×` |
| Hyphen-minus temperature | `-[0-9]+ ?°C` | **0 hits** — typographic `−20 °C` (U+2212) used |
| Untranslated English | `the\|your\|screen\|settings\|press\|button\|cable\|port` outside DNT | **0 hits** |

### 3. Inch mark — three contexts verified individually (§4.1 parse hazard)

| Context | Occurrences | Form found | Verdict |
|---|---|---|---|
| JSX `<Tab title=…>` | `flip/index.mdx:30,49` | `title="Flip 14&quot;"`, `title="Flip 15,6&quot;"` | **Correct** — entity kept, only the decimal separator changed |
| Frontmatter `description:` | `flip/index.mdx:3`, `dual-flip/index.mdx:3` | `… 14\" und 15,6\""`, `… Dual Flip 16\""` | **Correct** — `\"` escape kept, comma applied |
| Markdown heading | `flip/installation.mdx:14,20` | `### Flip 14"`, `### Flip 15,6"` | **Correct** — literal `"`, per §7.4's explicit "do not fix these to `&quot;`" |
| Any literal `"` inside a JSX attribute | regex `(title\|alt)="[^"]*[0-9]"` | **0 hits** | No build hazard anywhere in F3 |

`dual-flip/index.mdx:11` correctly uses `alt="Der Screenmate Dual Flip 16&quot;"`.
The DE tree also avoids the NL `panorama` frontmatter defect the glossary warns about
(period instead of comma) — both DE `description` lines use the comma.

### 4. Numeric parity EN↔DE — 12/12 PASS

Every numeral extracted from each EN file and its DE counterpart, normalised
(`,`→`.`) and sorted. All twelve pairs match exactly. No spec-table transcription drift,
no dropped angle, no altered range: `1920 × 1200`, `1920 × 1080`, `2560 × 1600`,
`250 cd/m²`, `450 cd/m²`, `1000:1`, `178°`, `60 Hz`, `1565`/`1875`/`1900 Gramm`,
`34,5 × 22 × 3,5 cm`, `39 × 23 × 3,5 cm`, `39 × 24 × 3,5 cm`, `0° – 245°`, `0° – 205°`,
`5 V/2 A`, `5 V`–`20 V`, `±2 V`, `−20 °C`–`60 °C`, `0–100`, `0–4`, `10–60 Sekunden`.

### 5. Structural parity EN↔DE — 12/12 PASS

Counted per file pair: `##` headings, `###` headings, `<img>`, list items, `**…:**` bold
run-ins, `<p>` captions. Every one of the six counts matches in all twelve pairs. Nothing
dropped, nothing invented — including the 17 OSD run-ins per `osd.mdx` and the 3 port-icon
`<p>` captions in `flip/installation.mdx` (`USB-C` / `HDMI` / `USB-A 2.0`, correctly left
as DNT interface names per §7.7 while their sibling `alt` attributes take full
Durchkopplung: `USB-A-2.0-Anschluss`).

### 6. OSD chapter policy (R1 / R9 / §6) — PASS

- **Headings translated** (§6.4): flip `## Hintergrundbeleuchtung / Bildeinstellungen /
  Farbeinstellungen / Einstellungen / Zurücksetzen / Sonstiges`; dual-flip
  `### 1.–6.` with the same six renderings. Matches the §6.4 table row-for-row. No
  parenthetical English menu name appended (the NL `expand` defect is not copied).
- **Parenthesised CAPS labels English** (§6.1): DNT-token multiset compared EN↔DE across
  `osd.mdx`, `controls.mdx`, `index.mdx` for both products — **exact match, 6/6 files**.
  `(COLOR TEMP.)` keeps its trailing period in flip; dual-flip's `COLOR TEMP` correctly has
  none, matching its own EN source.
- **On-device values English** (§6.3): `Standard, Game, Movie, Text, FPS, RTS, Energy
  Saving`, `Warm, Cool, User, Standard`, `ON`/`OFF`, `Off, Auto, 2084`, `Type-C1 / Type-C2`,
  `4:3` / `WIDE` — all verbatim, deliberately diverging from NL, which translates them.
- **Gloss vocabulary** (§6.2.1): `Helligkeit, Kontrast, Schärfe, Seitenverhältnis,
  Farbtemperatur, Rot, Grün, Blau, Sprache, OSD-Timer, Transparenz, Signalquelle,
  Zurücksetzen, HDR-Modus, ECO-Modus` — all match the locked column. `Low Blue Light`
  correctly left as-is (the gloss *is* the device label).
- **`Wähle RESET, um alle Einstellungen auf die Werkseinstellungen zurückzusetzen.`** —
  byte-matches the §6.3 worked example in both products.
- **Alt text fully German** (R9): all 30 unique `alt` strings in F3 enumerated; **zero**
  English residue. DE is stricter than NL here, which leaves `OSD-menu Backlight` /
  `OSD-menu Set` in `dual-flip`.

### 7. Glossary spot-checks that passed

§7.1 titles (`Screenmate Flip – Handbuch` appositive with en dash, not Durchkopplung) ·
§7.2 descriptions (all six DE descriptions byte-match their locked targets) ·
§7.3/§7.4 headings (`Die richtigen Kabel wählen`, `Installationsanleitung`,
`Anschlussmöglichkeiten`, `Den Screenmate verstauen`, `Aufbewahrung`, `Bedientasten`,
`Seitliche Anschlüsse`, `Taste + (Helligkeit erhöhen)`, `Taste − (Helligkeit verringern)`,
`M – OSD-Menütaste`, `Einführung in das OSD`, `Das OSD-Menü verwenden`) ·
§8 spec fields (all 15 rows per table) · §10.1 constructions (`Willkommen!`, `Hinweis:` —
including the corpus' single `Please note:` in `flip/installation.mdx:72` collapsing onto
it — `Wichtig:`, `Wichtige Informationen:`, `Geh sorgsam mit deinem Screenmate … um`,
`Möchtest du deine Arbeitsfläche erweitern?`, `Bildschirm steht auf dem Kopf?`,
`Brauchst du mehr Platz?`, `Wähle die Variante, die zu … passt`) ·
§10.5 run-ins (`**USB-C-Anschluss:**`, `**Mini-HDMI:**`, `**Linker Bildschirm:**`,
`**Rechter Bildschirm:**`) · §9 OS labels (`„Anzeigeausrichtung"`,
`„Querformat (gedreht)"`, `die Schaltfläche „Identifizieren"`, `Systemeinstellungen`,
`Displays`, `Anordnen`, `Drehung`, `Standard`, first-mention
`**Display settings** („Anzeigeeinstellungen")`) · §2.3 imperatives (every numbered step
across all 12 files uses imperative singular with correct separable-prefix placement:
`Klappe … auf`, `Klappe … aus`, `Klappe … ein`, `Schließe … an`, `Stelle … ein`,
`Lege … fest`, `Passe … an`, `Halte … gedrückt`; stem-changing `Lies`, `Nimm` correct) ·
§10.3 subordinate-clause commas (checked every `dass` / `ob` / `wenn` / `um … zu`
boundary — none missing).

### 8. Safety-negation integrity — PASS

All 14 safety items compared clause-by-clause against EN in both products. No negation
weakened, none dropped, no restriction loosened:

- `Only use the included AC/DC adapter` → `Verwende **ausschließlich** das mitgelieferte
  AC/DC-Netzteil` (`ausschließlich`, not the weaker `nur`)
- `Only use the device with a 5V power source` → `Verwende das Gerät **ausschließlich** mit
  einer 5-V-Stromquelle`
- `Do not use liquids or aggressive cleaning agents` → `Verwende **keine** Flüssigkeiten
  oder aggressiven Reinigungsmittel` (`keine` correctly distributes across both nouns,
  giving the weak `-en` ending on `aggressiven`)
- `Do not touch … and do not use it …` → **both** negations preserved: `Berühre … **nicht**
  … und verwende es **nicht** …`
- `Do not drop the monitor` → `Lass den Monitor **nicht** fallen`
- `Do not rotate the screens beyond the maximum angle` → `Drehe die Bildschirme **nicht**
  über den … maximalen Winkel **hinaus**`
- `do not press on the screens` → `drücke **nicht** auf die Bildschirme`
- `the HDMI port does **not** supply power` → `Der HDMI-Anschluss liefert **keinen** Strom`
- `Keep ventilation openings clear` → `Halte die Lüftungsöffnungen frei`
- `Limit exposure to strong magnetic fields` → `Begrenze die Einwirkung von starken
  Magnetfeldern`

§10.2 traps avoided throughout: `arbeitet mit einem DC-Eingang` (not `operiert auf`),
`Achte darauf, dass` (not `Mache sicher`), `Prüfe zuerst` (not `Checke`),
`Starte … neu` pattern respected, `Schalte den Bildschirm aus` (not `Drehe … aus`).

### 9. Registration

All 12 F3 pages are present in `docs.json` under the `"language": "de"` block
(lines 353–358 dual-flip, 365–370 flip), in the same page order as EN. No orphans, no
missing entries.
