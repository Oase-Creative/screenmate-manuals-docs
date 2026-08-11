# Task 10 — German fix log

Branch `lang-expansion-de-fr-it`. Source findings: `adversarial-de-F1.md`, `-F2.md`, `-F3.md`,
`-F4.md`, `backtranslation-review-de.md`. Authority: `translations/glossary-de.md`.

**Result: 47 findings applied · 5 skipped with reason · 4 + 29 skipped by disposition class.**
`python scripts/verify_translation.py --base en --targets de` → **0 FAIL, 0 WARN, exit 0**
(before and after). Register (§2.2), em-dash, DIN-spacing, `2x`, period-decimal and
Durchkopplung sweeps re-run over `de/` → clean.

Line numbers are the **pre-fix** DE line numbers quoted by the reports.

---

## 1. Grammar / meaning errors

| # | Finding | File : line | Change |
|---|---|---|---|
| F1-1 | case-government `auf oder um den Bildschirm` (`auf` static = dative, `um` = accusative, coordinated over one NP) | `de/manuals/infinity/safety.mdx:19`, `de/manuals/infinity-lite/safety.mdx:19`, `de/manuals/panorama/safety.mdx:19` | → `Verwende keine scharfen Gegenstände auf dem Bildschirm oder in seiner Umgebung.` Verified first that the string exists in **exactly** these 3 files and that each is its own dedupe/checksum group (`33e8d276`, `f1094236`, `82792478`); the 7-product group `cf3a7469` (onecable/lite/lite-144hz/flip/expand/one-4k/one-4k-oled) and `dual-flip` carry a different sentence and were **not** touched, so no group re-propagation was needed. `panorama` included per F1-1's own "(also at …, same fix)". |
| F1-2 | bare `Dieser PC` in object position reads as a nominative; §9 requires German quotes, and the same file quotes it at :53 | `de/manuals/onecable/installation-windows.mdx:46` | → `Öffne **„Dieser PC“** und dort …` |
| F1-3 | EN word-order calque + comma German does not license before a plain PP (§10.2/§10.3) | `de/manuals/infinity-lite/installation.mdx:54` | → `… und dem Computerbildschirm für ein angenehmeres Nutzungserlebnis nach deinen Vorlieben an.` |
| F2-F5 | `je nachdem` + interrogative needs a comma (orthography, not style) | `de/manuals/lite-144hz/osd.mdx:24` **+** `de/manuals/lite/osd.mdx:24` | both → `- **ECO-Modus:** Wähle einen Bildmodus, je nachdem, wie du den Monitor verwendest:` (also removes lite's awkward `danach aus, wie`) |
| F2-F3 | modality shift: EN states a device condition, DE imposed an obligation (`musst du`) + `Strom … Strom` tautology | `de/manuals/lite-144hz/installation.mdx:16` | → the `lite` wording `… muss der Monitor separat über eine zusätzliche Stromquelle versorgt werden.` |
| F2-F4 | `braucht` weakens a hard prerequisite (EN "must have") | `de/manuals/lite-144hz/installation.mdx:35` | → `… muss einen USB-C-Anschluss mit Videounterstützung haben` (= the `lite` form) |
| F4-03 | `aktiviert` loses the *switching* sense the glossary §5 row cites verbatim | `de/manuals/one-4k/installation.mdx:14` | → the oled form `… schaltet der Screenmate automatisch auf die Schnellladefunktion um.` |
| F2-F6 | §3.2 lock `65 W` → `65-W-Netzteil`; EN is internally inconsistent, §11 normalises in German | `de/manuals/panorama/index.mdx:23` | → `- **65-W-USB-C-Netzteil**` |

## 2. Twin harmonisation — `lite` ↔ `lite-144hz` (EN + NL byte-identical)

Result: `installation.mdx`, `osd.mdx`, `safety.mdx` are now byte-identical across the pair
modulo the product token; `controls.mdx` differs only in the §10.5-locked
`**OSD-Modus**` / `**OSD-Menü-Modus**` pair; `index.mdx` only where EN itself differs
(144 Hz description + `Bildwiederholrate` row).

| # | Span | Chosen rendering | Why |
|---|---|---|---|
| F2-F2 | `installation:9` | `unterstützt fünf Anschlussszenarien` + `den verfügbaren Kabeln` | merge: 144hz clause tracks EN "supports five connection scenarios", lite's `verfügbaren` tracks EN "available" |
| F2-F2 | `installation:13` | lite: `Schließe den Screenmate mit dem … an deinen Laptop an.` | glossary §5 `to connect → anschließen` |
| F2-F3 | `installation:16` | lite | see §1 |
| F2-F2 | `installation:21` | lite: `Verwende dann das …` | per report |
| F2-F2 | `installation:27` | lite: `… und zusätzlich über ein USB-C-auf-USB-A-Kabel …` | renders EN "together with" |
| F2-F2/F4 | `installation:35` | lite: `für Videosignal und Stromversorgung zugleich` + `muss … haben` | matches the identical sentence already shipped in `one-4k/installation` |
| F2-F2 | `installation:57` | lite's `wie zum Beispiel einen PC, …` **+** 144hz's `(nicht die Konsole Nintendo Switch selbst)` | §10.1: a 5-item list *is* a genuine enumeration, so `wie zum Beispiel` stays; `Konsole` tracks EN "the Nintendo Switch console itself" |
| F2-F7 | `osd:17`, `osd:18`, `osd:25`, `osd:31` | the `lite-144hz` rendering in all four | those four track EN structure most closely (`for deeper blacks`, `to improve image clarity and detail`, `Default picture mode`, `for better picture quality`); F2-F7 recommends 144hz for 17 and 25 explicitly |
| F2-F5 | `osd:24` | corrected shared string | see §1 |
| F2-F9 | `controls:11` (alt) | `Übersicht über die Anschlüsse und Tasten des Screenmate Lite` | matches the §7.2-locked `Übersicht über die …` |
| F2-F9 | `controls:23` | lite: `Schließe ein externes Gerät einfach über ein Mini-HDMI-auf-HDMI-Kabel an.` | **deviation from F2-F9's recommendation**: its "use 144hz" rationale was the alt-text lock only; EN is `Easily connect an external device via a …`, whose object-early order the lite form reproduces |
| F2-F9 | `controls:28–29` | 144hz: `das Gerät ein-/ausschalten` | EN says "the device" |
| F2-F8 | `index:8` | see §3 | |
| F2-F8 | `index:15` | `Er wird über USB-C oder HDMI angeschlossen und wiegt nur 609 Gramm.` | de-nominalises `Der Anschluss erfolgt` (§10.3) and matches lite for the clause EN shares |
| F2-F10 | `index:15` | drop the comma in `ein leichter tragbarer 15,6"-Full-HD-Monitor` | `tragbarer Monitor` is a §1.1-locked unit |

## 3. Twin harmonisation — `one-4k` ↔ `one-4k-oled` (EN byte-identical)

Remaining differences after the pass are exactly those EN carries itself (image
`src`/`alt`, the `{/* … */}` comments locked to EN by §7.7, the missing USB-A body,
OLED specs, link targets).

| # | Span | Chosen rendering | Why |
|---|---|---|---|
| F4-01 | `installation:10` (cables) | oled: `Verwende immer die mitgelieferten Kabel für optimale Leistung.` | EN order |
| **F4-02** | `installation:11`, `:12` | one-4k: `Anzeigeeinstellungen` (both oled occurrences changed) | §9 locks OS-level display settings → `Anzeigeeinstellungen`; §7.2 reserves `Bildschirmeinstellungen` for the OSD context |
| F4-01 | `installation:13` (charging) | oled: `sobald das Ladegerät am Screenmate angeschlossen ist` | EN is passive there |
| F4-03 | `installation:14` | oled `schaltet … um` | see §1 |
| F4-01/F4-05 | `installation:15` | one-4k clause order + `wie eine Maus oder eine Tastatur` | **deviation from F4-01's "use oled"**: oled stranded `automatisch` at clause end; one-4k's `erkennt … außerdem automatisch angeschlossenes …` tracks EN's adverb position. `wie zum Beispiel` → bare `wie` per F4-05 (short apposition, §10.1) |
| F4-04/F4-08 | `controls:13` | one-4k: `für Strom & Video …` + `Diese eine Verbindung überträgt Strom und Video über ein einziges Kabel.` | restores agreement with the §7.4-locked heading `USB-C-Anschluss (Strom & Video)`; drops the `laufen … zusammen` (= converge) paraphrase |
| — | `controls:19` | oled: `… wenn er an ein USB-C-Gerät angeschlossen ist, das DisplayPort Alt Mode unterstützt.` | keeps EN's subject (the port is what is connected) |
| F4-05 | `controls:35` | `Zum Anschließen von USB-2.0-Zubehör wie einer Maus oder einer Tastatur.` | §10.1 short apposition |
| — | `controls:39` | oled: `Status-LED, die den Strom- und Signalstatus anzeigt.` | EN participle; one-4k repeated `Status … Status` |
| F4-09 | `controls:43` | oled: `Wenn der Monitor eingeschaltet ist` | §10.2 rejects the colloquial `an sein` |
| F4-12/F3-F11 | `controls:9` | see §5 | |
| F4-11 | `osd:9`, `:13`, `:17` | oled renderings | EN-clause order; keeps the three run-ins internally parallel |
| F4-10 | `osd:13` | `Die ausgewählte Option **ist** gelb hervorgehoben.` | EN "is highlighted" = state, not process passive |
| F4-11 | `osd:30` | one-4k: `**10 Sekunden** lang gedrückt` | `X Sekunden lang gedrückt halten` is the correct German for a duration |
| F2-F9 (ext.) | `one-4k/controls:11` (alt) | `Übersicht über die Anschlüsse und Tasten …` | same EN alt shape as the lite pair; aligns with the §7.2 lock |

## 4. Welcome-note harmonisation (11 files)

One EN string (`**Welcome!** This is your complete digital manual for the Screenmate {X}.
Use the navigation menu on the left to jump to each section.`) had **3** DE renderings:
7× `Das ist … Über das Navigationsmenü links springst du direkt zu jedem Abschnitt.`,
3× `Dies ist … Nutze das Navigationsmenü links, um direkt zu einem Abschnitt zu springen.`,
1× singleton `Verwende das Navigationsmenü links, um zu den einzelnen Abschnitten zu springen.`

**Locked target, applied to all 11 `de/manuals/*/index.mdx:8`:**

> `**Willkommen!** Das ist dein vollständiges digitales Handbuch für den Screenmate {X}. Nutze das Navigationsmenü links, um direkt zu einem Abschnitt zu springen.`

Chosen per F1-4 over F2-F8's majority form: EN is an **imperative**, and the majority
variant demotes it to an indicative (§2.3 imperative singular; §10.3 active voice).
`Das ist` is the 8/11 majority for the first sentence. F2-F8's own singleton is retired.

F3-F7 folded into the same Note: `de/manuals/flip/index.mdx:8` →
`… für den Screenmate Flip, sowohl für das 14"- als auch für das 15,6"-Modell.`
(EN "covering **both** … models"; matches `flip/installation.mdx:9`'s `Sowohl … als auch`).

## 5. §9 first-mention English OS label — Infinity display-settings

Both files are their own checksum group (`c5483629`, `05dc2010`); the shared-4 body
(`e6f54bf0`: onecable/dual-flip/flip/expand) was **not** touched, and the dedupe check
still passes.

| File : line | Change |
|---|---|
| `de/manuals/infinity/display-settings.mdx:12` | → `Öffne die **Display settings** („Anzeigeeinstellungen“) und wähle **„Desktop auf diese Anzeige erweitern“**.` |
| `de/manuals/infinity-lite/display-settings.mdx:12` | → `Gehe zu den **Display settings** („Anzeigeeinstellungen“) und wähle **Desktop auf diese Anzeige erweitern**.` |

Rationale: §9 mandates `„Display settings“ („Anzeigeeinstellungen“)` on first mention
*because the screenshots stay English*; the frozen canonical page
`de/manuals/onecable/display-settings.mdx:9` already does exactly this. Later mentions
(`Identifizieren`, `Anzeigeausrichtung`, `Skalierung`) were already German-only and were
left alone.

## 6. F3 minors / nits, plus the remaining F1 / F2 / F4 items

| # | File : line | Change |
|---|---|---|
| F3-F2 | `dual-flip/installation.mdx:51` | `nicht mehr brauchst` (= permanent disposal) → `Wenn du mit dem Dual Flip fertig bist, verstaue ihn so:` |
| F3-F3 | `dual-flip/osd.mdx:43` | → `Wähle die OSD-Sprache.` + `Vereinfachtes Chinesisch` (normalised onto `flip/osd.mdx:43`, which was left unchanged) |
| F3-F4 | `flip/installation.mdx:67` | double `mit … mit` → `Verbinde eine Seite des Screenmate über das mitgelieferte USB-C-Kabel mit deinem Laptop.` |
| F3-F5 | `flip/installation.mdx:18` | `Screenmate Flip 14 Zoll` → `Screenmate Flip 14&quot;` — §4 "do not expand to `Zoll`"; `&quot;` because it is a **JSX attribute** (§4.1 parse hazard). Only `Zoll` occurrence in the DE tree; now zero. |
| F3-F6 | `flip/index.mdx:15` | passive + lost "clips" → `… ein faltbarer Multiscreen-Monitor, den du um deinen Laptop klemmst und der dir zwei zusätzliche Bildschirme … gibt.` (also closes the backtranslation "clips around" row) |
| F3-F8 | `flip/index.mdx:80`, `dual-flip/index.mdx:55` | `etwas Strom` → `eine geringe Menge Strom` (EN "a small amount of power" — the quantity justifies unplugging) |
| F3-F9 | `flip/osd.mdx` + `dual-flip/osd.mdx`, 6 alt each (**12**) | `alt="OSD-Menü Hintergrundbeleuchtung"` → `alt="OSD-Menü – Hintergrundbeleuchtung"` (en dash, §3.6; removes the §3.4 Deppenleerzeichen) — likewise Bildeinstellungen / Farbeinstellungen / Einstellungen / Zurücksetzen / Sonstiges |
| F3-F10 | `dual-flip/index.mdx:15` | mid-sentence voice switch → `… Auflösung von 2560 × 1600, und du schließt ihn über USB-C oder über USB-C + HDMI + USB-A an.` |
| F3-F11 + F4-12 | all 11 `de/manuals/*/controls.mdx:9` | one house opener, tracking EN "…control buttons **on** the Screenmate X": `Dieser Abschnitt gibt **dir** einen Überblick über … Bedientasten **am** Screenmate {X}.` Resolves the corpus split (was 6× `am` / 5× `des`, 3× with `dir` / 8× without). `am` per F4-12; `dir` per F3-F11 (`du` register) — the two reports conflicted only on `dir`, and `dir` wins because F3-F11 is explicit and the one-4k twin already carried it. Per-file legitimate variants preserved: `die physischen` (infinity-lite, EN "the"), `am Monitor Screenmate OneCable` (EN "the Screenmate OneCable monitor"), infinity's trailing mirror-layout sentence. |
| F3-F12 | `flip/osd.mdx:59` | `die Menge an blauem Licht vom Bildschirm` → `den Blaulichtanteil des Bildschirms` (EN "from the screen"; `von` cannot govern a source-of-emission here) — harmonised with the F4-14 target |
| F4-14 | `expand/osd.mdx:61` | `Blaulichtanteil auf dem Bildschirm` → `des Bildschirms` (EN "from the screen") |
| F4-06 | `expand/osd.mdx:24` | `Bildschärfe` → `Passe die Schärfe des Bildes an (0–4).` (§6.2.1 names this drift by name; only DE file using `Bildschärfe`) |
| F4-13 | `expand/index.mdx:15` | `zwei Full-HD-Displays … eines auf jeder Seite` → `zwei Full-HD-Bildschirmen … einer auf jeder Seite` (§10.4; note the agreement change) |
| F4-15 | `expand/installation.mdx:29` | → `2. Klappe die beiden Bildschirme in die in Abbildung 2 gezeigte Richtung auf.` (§10.1 participial family, matches `flip/installation.mdx:47`) |
| F2-F11 | `panorama/index.mdx:15` | `drei Full-HD-Displays` → `drei Full-HD-Bildschirme`, recast per F2-F11 to avoid `drei Bildschirmen … drei Bildschirme` (§10.4) |
| F2-F12 | `panorama/osd.mdx:37` | → `Deshalb kannst du die Anordnung des Desktops in deinem Betriebssystem anpassen.` |
| F2-F13 | `panorama/osd.mdx:21`, `:33` | `einstellen` → `anpassen` for brightness/volume (§10.4; the section headings above already say `Helligkeit anpassen` / `Lautstärke anpassen`). Digit tokens `0`/`100` preserved on both lines. |
| F1-7 | `infinity/display-settings.mdx:68`, `infinity-lite/display-settings.mdx:93` | `eingebaute Lautsprecher` → `integrierte Lautsprecher` (§1.1 lock) |
| F1-8 | `infinity/installation.mdx:59` | `wie zum Beispiel das der Nintendo Switch` → `wie das der Nintendo Switch` (§10.1 short apposition) |
| F1-11 | `onecable/installation.mdx:11` | garden path `fest … stellen` → `Stelle die Halterung stabil auf eine ebene Fläche.` |
| F1-12 | `onecable/installation-windows.mdx:47` | see §1 (imperative restored) |
| F1-14 | `onecable/index.mdx:15` **+** `lite/index.mdx:15` | hedge restored: `… der darauf ausgelegt ist, deine Produktivität zu steigern, indem er …`. **Extended to `lite`** because it carries the byte-identical EN hedge ("designed to boost your productivity") — those are the only two occurrences in `en/`. |

---

## 7. Skipped, with reason

| # | Finding | Reason |
|---|---|---|
| F1-9 | inch-mark compound `15,6"-Bildschirmen`: §3.2's `15,6-Zoll-Bildschirm` example vs §4's "do not expand to `Zoll`" | **No de/ edit.** The glossary contradicts itself; §4 is the explicit, unambiguous row and the DE tree is already self-consistent across all 6 files. Resolving it means amending `glossary-de.md` §3.2/§4, which is outside a de/-only fix pass. Left for the glossary gate. (The related **F3-F5** `14 Zoll` alt **was** fixed, in the §4 direction.) |
| F1-10 | non-ASCII in-page anchor `](#bildschirmmenü-osd)` in `infinity/controls.mdx:19` | **No edit.** Verified the target heading `## Bildschirmmenü (OSD)` exists in the same file and that the anchor is the exact github-slugger output (lowercase, unicode letters preserved, parentheses dropped, space → `-`). Dropping the anchor, as the report's zero-risk alternative proposes, would lose a working cross-reference. Flagged for a built-preview check, not a text defect. |
| F1-13 | `infinity-lite/installation.mdx:37` `bis er einrastet` = invented completion criterion | **No edit — report conflict resolved against F1.** `backtranslation-review-de.md` §1 row 6 adjudicates the same span as "DE disambiguates an ambiguous EN phrase. The German is clearer … **No action**." Both sources *do* assert the click (EN "**Click** open the frame", NL "**Klik** het frame open"), so `bis er einrastet` renders the source rather than inventing. |
| BT row 4 | `infinity/index.mdx` "clips behind" → `Du befestigst ihn` | Adjudicated "cosmetic · optional polish" by the backtranslation review. Unlike `flip` (F3-F6), the DE is already active and reader-agentive; no grammar or glossary defect. |
| BT row 5 | `Schutzhülle` / `Kabelhalter` one notch more generic than EN | Both are **glossary-locked** (§1.1 `protective case`/`protective sleeve` → `Schutzhülle`; `cable organizer` → `Kabelhalter`). Changing them would break the lock. Noted in the report itself as a glossary candidate, not a translation defect. |

## 8. Skipped by disposition class (per the task brief)

- **`*_link` frontmatter absent on all 62 DE pages** — F2-F1 (critical), F3-F1 (major),
  F4-07 (medium), backtranslation §2 item 27. False positive here: owned by the
  `scripts/generate_language_links.py` generator task. **4 findings.**
- **EN-source / source-inherited** — F1-6 (`beide Erweiterungsbildschirme` on the
  single-screen Infinity Lite), backtranslation §1 row 1 (`'Mirrored'` — DE already
  normalises EN's defect) and the full backtranslation §2 list of **27** EN-source issues
  (5 V/20 V safety tension, `Color Gamut`/`Color Accuracy` split, Flipped/Mirrored,
  OneCable screenshots on other products, the Louie TODOs, …). Client list; `de/` must not
  diverge from `en/` unilaterally. **29 items.**
- **Loop artifacts** — backtranslation §1 row 2 (`'Flipped'` → `„Querformat (gedreht)“`
  on 6 pages) is correct localisation per §9, no action. **1 item.**

## 9. Invariants re-checked after the edits

| Check | Result |
|---|---|
| `python scripts/verify_translation.py --base en --targets de` | **0 FAIL, 0 WARN — exit 0** (structure, numbers, DNT, stub, dedupe, register, negation) |
| dedupe byte-identity, `safety.mdx` group (7 slugs) | untouched — no member edited |
| dedupe byte-identity, `display-settings.mdx` group (onecable/dual-flip/flip/expand) | untouched — only the two singleton Infinity bodies were edited |
| §2.2 register grep `\b(Sie\|Ihnen\|Ihr\|Ihre\|Ihrem\|Ihren\|Ihrer\|Ihres\|Ihrigen\|Bitte)\b` over `de/` | 0 hits |
| §3.6 em dash `—` in body copy | 0 hits |
| §4 DIN unit spacing `[0-9](W\|V\|A\|%\|Hz\|ms\|cm\|mm)` | 0 hits in prose |
| §3.6 `2x` instead of `2×` | 0 hits |
| §4 period decimals | 0 defects (remaining hits are `USB-A 2.0`, `USB-2.0-Zubehör`, the `100.000:1` thousands separator, and SVG path data) |
| §3.1 Durchkopplung (acronym + space + German noun) | 0 hits |
| `lite` ↔ `lite-144hz` diff (product token normalised) | only the §10.5-locked `OSD-Modus`/`OSD-Menü-Modus` pair and the EN-side 144 Hz differences remain |
| `one-4k` ↔ `one-4k-oled` diff (product token normalised) | only differences EN itself carries remain |
