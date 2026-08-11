# Adversarial FR review — family F1 (OneCable / Infinity / Infinity Lite)

**Branch:** `lang-expansion-de-fr-it` · **Date:** 2026-08-11 · **Reviewer:** adversarial pass, EN + NL + FR side by side
**Scope:** 18 pages — `fr/manuals/onecable/` (8), `fr/manuals/infinity/` (5), `fr/manuals/infinity-lite/` (5)
**Authority:** `translations/glossary-fr.md`, `translations/dnt.json`

**Verdict:** the mechanical layer is clean (every §11 grep passes; `scripts/verify_translation.py --base en --targets fr` → `0 FAIL, 0 WARN`). All findings below are semantic, grammatical or consistency defects that no grep reaches. **8 defects + 2 informational.** No High-severity defect found; one Medium (safety-callout negation scope).

---

## Findings

| # | File : line | Quoted text | Problem | Sev | Proposed fix |
|---|---|---|---|---|---|
| F1-01 | `fr/manuals/infinity/installation.mdx:63` | `**Important&nbsp;:** tous les ports USB-C ne prennent pas en charge la sortie vidéo.` | **Negation-scope ambiguity in an `Important` callout.** EN `Not every USB-C port supports video output.` / NL `niet alle USB-C-poorten ondersteunen beeld` are both unambiguously partitive. The FR `tous les X ne … pas` construction is formally ambiguous and is routinely read as the *total* negation "no USB-C port supports video output" — the opposite operational advice. This is the callout that stops a user plugging video into a power-only port. Drift vs **both** sources. | **Medium** | `**Important&nbsp;:** les ports USB-C ne prennent pas tous en charge la sortie vidéo.` (alt: `Certains ports USB-C ne prennent pas en charge la sortie vidéo.`) Keeps `ne … pas` full per §5.5. |
| F1-02 | `fr/manuals/infinity/installation.mdx:29` | `Le Screenmate peut être connecté des manières suivantes&nbsp;:` | **Inconsistent with shipped FR siblings, and the less idiomatic of the two forms.** `fr/manuals/dual-flip/installation.mdx:9` and `fr/manuals/flip/installation.mdx:9` — both already shipped and QC'd — render the identical EN string `in the following ways` as **`de l'une des manières suivantes`**. Glossary §6 locks the bare `des manières suivantes`, but §0 precedence rule 3 says a shipped QC'd page wins over the glossary and the glossary is amended to match. Bare `peut être connecté des manières suivantes` reads as a calque. Same defect at `fr/manuals/expand/installation.mdx:14` (outside F1). | Low | `Le Screenmate peut être connecté de l'une des manières suivantes&nbsp;:` — then amend glossary §6 row `in the following ways` to the shipped form, and fix `expand` in the same commit. |
| F1-03 | `fr/manuals/onecable/controls.mdx:49`<br>`fr/manuals/onecable/installation.mdx:54`<br>`fr/manuals/onecable/troubleshooting.mdx:37` | `… le port Power sert uniquement à l'alimentation.`<br>`… sur le port Power du Screenmate`<br>`… sur le port USB-C Power du Screenmate` | **Untranslated `Power` breaks the on-page cross-reference.** `Power` is *not* in `translations/dnt.json` (only `Power Delivery` is), and glossary §9.4 locks `USB-C Port (Power)` → `Port USB-C (alimentation)` and `(Power Only / …)` → `(alimentation uniquement / …)`. `controls.mdx:49` is the disambiguation note sitting directly under the heading `### Port USB-C (alimentation uniquement / Power Delivery)` — it names a port that appears nowhere on the page under the name it uses. | Low | Either render `le port d'alimentation` in all three places (consistent with §9.4), **or** add `Power` to `dnt.json` as an on-device label and record the split. Glossary decision — do not fix unilaterally (§12). |
| F1-04 | `fr/manuals/onecable/index.mdx:101`, `:121`<br>`fr/manuals/infinity-lite/index.mdx:45`<br>vs `fr/manuals/infinity/index.mdx:47` | `39 × 24 × 2,5 cm` / `34,5 × 22 × 2,5 cm` / `36,2 × 20,9 × 1,6 cm`<br>vs `36,1 × 21,6 × 4,5&nbsp;cm` | **FR-internal unit-spacing inconsistency.** The same field (`Dimensions (plié)`), same unit symbol, rendered two ways across four sibling spec tables. §4/§4.1 mandate `&nbsp;` between a number and a unit symbol, and the corpus already does this consistently for `mm` (`3,5&nbsp;mm`, `fr/manuals/infinity-lite/controls.mdx:21`). Glossary is self-contradictory here: §4's decimal row shows `40,6 × 23,7 × 2,5 cm` and §5.7 shows `(60 cm)` / `(1,2 m)` with plain spaces. **Not** covered by the "unit spacing divergences" carve-out, which is about FR-vs-EN/NL, not FR-vs-FR. | Low | Normalise to `&nbsp;cm` (per §4.1, the mechanical rule) across all four cells, and correct the §4/§5.7 illustrative examples in the same commit so the glossary stops contradicting itself. |
| F1-05 | `fr/manuals/infinity-lite/display-settings.mdx:23` | `Organisez les trois écrans dans la vue **Identifier** en faisant glisser chacun d'eux pour correspondre à sa position physique.` | **Dangling infinitive.** `pour correspondre` inherits the subject of `en faisant glisser`, i.e. `vous` — so the sentence literally says the *reader* matches "its" physical position, while the possessive `sa` points at the screen. EN `by dragging each one to match its physical position` has no such clash (English `to match` binds to `each one`). | Low | `… en faisant glisser chacun d'eux **pour qu'il corresponde à** sa position physique.` |
| F1-06 | `fr/manuals/infinity-lite/installation.mdx:46` | `Dépliez le support, réglez-le sur le bon angle d'appui, …` | **Same EN verb rendered two ways across F1.** EN here is `Open the stand, …` (`en/manuals/infinity-lite/installation.mdx:47`); the identical EN instruction at `en/manuals/infinity/installation.mdx:77` is rendered `Ouvrez le support` at `fr/manuals/infinity/installation.mdx:76`. Glossary §5.5 maps `Open` → `Ouvrez` and `Unfold` → `Dépliez`, so `Dépliez` is the non-conformant one. | Low | `Ouvrez le support, réglez-le sur le bon angle d'appui, …` |
| F1-07 | `fr/manuals/infinity-lite/installation.mdx:69` | `L'Infinity Lite prend en charge deux principales méthodes de connexion, selon les ports de votre ordinateur portable.` | **Wrong noun+modifier order.** Antéposed `principal` after a bare numeral (no article) is marked in French; the classifying adjective belongs after the noun phrase. The current order also mirrors the EN adjective stack `two main connection methods` — a calque of English modifier order, which §2 rejects as the general pattern. | Low | `L'Infinity Lite prend en charge deux méthodes de connexion principales, selon les ports de votre ordinateur portable.` |
| F1-08 | `fr/manuals/onecable/troubleshooting.mdx:33` | `C'est possible, à condition que les conditions suivantes soient réunies&nbsp;:` | **Root repetition inside one clause** (`condition` / `conditions`). Glossary §6 locks `provided that` → `à condition que` + subjunctive, which is correct in general, but the lock does not require pairing it with `conditions` as its complement — EN `provided the following conditions are met` invites exactly this collision and it should be broken. | Low | `C'est possible si les conditions suivantes sont réunies&nbsp;:` (or `… à condition que les critères suivants soient réunis&nbsp;:`). §6 lock is unaffected — it still governs the other `provided that` sites. |

### Informational (no page edit proposed)

| # | Scope | Observation | Sev |
|---|---|---|---|
| F1-09 | `fr/manuals/onecable/display-settings.mdx` (4 sites), `fr/manuals/onecable/installation-windows.mdx` (2 sites) | **The Dutch UI glosses are dropped throughout.** EN carries a Dutch parenthetical beside each Windows label precisely *because* the screenshots stay Dutch — `**Display settings** ('Beeldscherminstellingen')` (`en/…/display-settings.mdx:10,20,29,33`), `Open **This PC** ('Deze pc')` (`en/…/installation-windows.mdx:47,48`). FR drops all six. Consequence: an FR reader sees `Paramètres d'affichage` in prose and `Beeldscherminstellingen` in the screenshot with no bridge; the EN reader has one. Applied uniformly and clearly deliberate, and adjacent to the recorded "Dutch Windows screenshots" non-defect — so recorded, not flagged. Worth putting to the client alongside the screenshot-language question. | Info |
| F1-10 | all 18 F1 pages (and all 61 `fr/`, `de/`, `it/` pages) | **No cross-language link frontmatter.** No `en_link:` / `nl_link:` / `de_link:` / `it_link:` on any FR page; `en/` and `nl/` still carry only the old single key. `docs.json` marks every product tab `hidden: true`, so Mintlify cannot infer counterparts and the switcher will not reach the FR pages. `python scripts/generate_language_links.py --check` confirms every page in every language needs regeneration — i.e. this is a tooled, repo-wide, pending build step, **not** a translation defect. Remediation: run `python scripts/generate_language_links.py`. | Info |

---

## Scrutiny evidence

Everything below was actively checked and **cleared**. Recorded so the absence of a finding is demonstrably a result, not an omission.

### Automated sweeps (all 18 pages)

| Check (glossary §11) | Result |
|---|---|
| 1 · register `\b(tu\|toi\|ton\|ta\|tes)\b` | 0 hits |
| 1b · 2sg imperatives (`Branche`, `Appuie`, `Vérifie`, `Ouvre`, `Choisis`, `Assure-toi`, …) | 0 hits |
| 2 · plain space before `: ; ! ?` | 0 hits |
| 3 · banned U+202F | 0 hits |
| 4 · literal U+00A0 outside frontmatter | 0 hits |
| 5 · typographic apostrophe U+2019 | 0 hits |
| 6 · period decimals (`2.5 cm`) | 0 hits |
| 7 · closed unit forms (`45W`) | 0 real hits (2 matches are `src=` image paths) |
| 8 · broken cable chain (`câble A à/>/-/ B`) | 0 hits — every chain is `câble A vers B` |
| 9 · hyphen-chain compounds (`USB-C-câble`) | 0 hits |
| 10 · `USB C` / `USBC` / unhyphenated `Mini HDMI` | 0 hits |
| 11 · untranslated `driver` in prose | 0 real hits (3 matches are `src=`/URL) |
| 14 · `100,000` / `100.000` | 0 hits |
| 15 · untranslated JSX strings (`Landscape view`, `Protective Case`, `does not support the video tag`, `Important Information:`, `Download Windows Drivers`, …) | 0 hits |
| 16 · literal `"` inside a `<Tab title=…>` attribute | 0 hits |
| 17 · pre-`7a96840` glossary drift on the frozen question leads | 0 hits |
| Repo verifier · `verify_translation.py --base en --targets fr` | **0 FAIL, 0 WARN** |

### Structural parity

- **Heading count** EN vs FR: identical on all 18 pages.
- **Heading levels** (`#`/`##`/`###` sequence) EN vs FR: identical on all 18 pages.
- **Frozen display-settings chapter**: FR body md5 identical across `onecable` / `dual-flip` / `flip` / `expand` (§9.3 requirement) — no drift.
- **Line-count deltas of −1** on 14 files were investigated and **dismissed**: `en/` and `nl/` are checked out CRLF while `de/fr/it` are LF, and `.gitattributes` (`* text=auto`, `*.mdx text`) normalises to LF in the repo. Not a defect.
- **Guillemets**: `«`/`»` counts balanced in every file; every one carries `&nbsp;` on the inside (`«&nbsp;…&nbsp;»`) — 0 bare guillemets.
- **`&nbsp;` next to `**`**: the only matches are `**…**&nbsp;:` (closing delimiter), which §3.2 verified as the *safe* pattern. No `**&nbsp;` opening-delimiter hazard anywhere.
- **Bold run-ins**: 0 instances of `**…:**` missing the `&nbsp;` before the colon.

### Items specifically hunted and found correct

- **R10 — `mirrored`.** `en/manuals/infinity/controls.mdx:10` "The layout is mirrored…" → `fr/…:9` `La disposition est en miroir sur l'écran gauche et sur l'écran droit.` FR follows EN; NL `identiek` is the outlier, and FR correctly did **not** follow NL. ✅
- **Anchor `#menu-à-lécran-osd`.** The only internal anchor in all of `fr/`. `fr/manuals/infinity/controls.mdx:19` targets `## Menu à l'écran (OSD)` at line 29 of the same file. GitHub-style slugging (lowercase, strip `'` and `()`, spaces→`-`, preserve Unicode letters) yields exactly `menu-à-lécran-osd`. Resolves. EN counterpart `#on-screen-menu-osd` → `## On-Screen Menu (OSD)` likewise. ✅
- **`Flipped` vs `Mirrored`.** `en/manuals/infinity-lite/display-settings.mdx` uses **both** EN labels (`**Flipped**` line 18, `'Mirrored'` line 54). FR renders both as `Paysage (inversé)` per §8, and correctly preserves the markup difference — bold at `fr/…:17` (EN bold), guillemets at `fr/…:53` (EN single quotes), per §3.5's "keep bold, don't convert to guillemets". ✅
- **The four `§10.1.F` question leads.** All present in their shipped-locked forms and correctly discriminated: `**Un écran est à l'envers&nbsp;?**` (infinity, infinity-lite — EN `Is a screen upside down?`) vs `**Écran à l'envers&nbsp;?**` (onecable, infinity-lite video tab — EN `Screen upside down?`); plus `**Vous souhaitez plus d'espace à l'écran&nbsp;?**` (infinity only), `**Vous travaillez avec trois écrans&nbsp;?**` (infinity-lite only), `**Besoin d'une meilleure vue d'ensemble&nbsp;?**`, `**Vous souhaitez étendre votre espace de travail&nbsp;?**`. Two EN variants that collapse in careless translation stayed distinct. ✅
- **Safety negation integrity.** All 14 OneCable + 10 Infinity + 10 Infinity Lite safety items read against EN: every prohibition keeps the full `ne … pas` (`N'utilisez pas d'objets tranchants`, `Ne touchez pas`, `Ne faites pas tomber`, `n'appuyez pas sur les écrans`, `Ne faites pas pivoter les écrans au-delà de…`). No weakening to `évitez de`, no dropped `ne`, no softened modality. ✅
- **Safety EN-variant fidelity.** OneCable EN `the included AC/DC adapter` → `l'adaptateur CA/CC fourni`; Infinity/Infinity Lite EN `an AC/DC adapter` → `un adaptateur CA/CC`. OneCable/Infinity EN `when not in use` → `lorsqu'il n'est pas utilisé`; Infinity Lite EN `when you are not using it` → `lorsque vous ne l'utilisez pas`. Infinity uses `-` bullets, Infinity Lite uses `1.`-numbered — FR mirrors each. Real EN differences preserved rather than smoothed. ✅
- **`charge inversée` gloss discipline.** Glossed once per page on first use, exactly as §5.2 requires: `onecable/installation.mdx:49`, `onecable/controls.mdx:30` (bare at `:45`, correct — second use), `onecable/troubleshooting.mdx:37`. No page glosses twice, none omits it. ✅ (Locked form — not flagged.)
- **`100 000:1` / spaced thousands** — not present in F1 (OneCable/Infinity/Infinity Lite are all `1000:1`). Ratios `16:9`, `16:10`, `1000:1` all keep the colon tight per §3.4. ✅
- **Voltage/current pairs.** `5V/2A` → `5&nbsp;V/2&nbsp;A`, `DC 5V/3A` → `CC 5&nbsp;V/3&nbsp;A`, `5V…20V (±2V)` → `5&nbsp;V…20&nbsp;V (±2&nbsp;V)`. §4 conformant everywhere. ✅
- **Percent & cd/m².** `100&nbsp;%&nbsp;sRGB`, `72&nbsp;%&nbsp;NTSC`, `120&nbsp;%&nbsp;sRGB`, `150&nbsp;%`, `300/350&nbsp;cd/m²` — all §4 conformant. ✅
- **Resolutions.** EN `1920×1200` / `1920×1080` normalised to `1920 × 1200` / `1920 × 1080` per §4. ✅
- **Angles vs temperatures.** `178°`, `172°`, `360°`, `330°`, `235°`, `90°` take **no** space; `-20&nbsp;°C`, `60&nbsp;°C` take `&nbsp;`. The §4 split is respected — this is the exact place a blanket "add a space before units" pass would have broken. ✅
- **Range dashes.** `0° – 360°` / `0° – 330°` (`onecable/index.mdx:129`) use U+2013 with spaces, matching the §3.5 corpus form `0° – 235°`, normalising EN's ASCII hyphen. ✅
- **Package-contents renderings.** `2 câbles USB-A vers USB-C`, `Câble USB-C vers USB-C`, `Clé USB (pilote inclus)`, `Étui de protection`, `Support pour écran unique`, `Support d'écran`, `8 patins antidérapants`, `1 adaptateur vidéo`, `Aimant` — all match §5.7/§10.1.C; the two captions containing a literal `>` correctly expanded to `vers`. ✅
- **`Télécharger les pilotes`.** `installation-windows.mdx:9` heading and `:24` button label both use the lowercase common noun; the caps drive/folder name `DRIVERS (D:)` at `:46` and `:53` stays verbatim. The §5.3 split is applied correctly in both directions. ✅
- **macOS/Windows UI labels (§8).** `Réglages Système`, `Moniteurs`, `Disposition`, `Confidentialité et sécurité`, `Enregistrement de l'écran et de l'audio système`, `Rotation`, `Standard`, `Son`, `Sortie`, `menu Pomme`, `barre latérale`, `Haut-parleurs du MacBook`, `Paramètres d'affichage`, `Étendre le Bureau à cet écran`, `Identifier`, `Orientation de l'affichage`, `Échelle`, `Ce PC`, `barre des tâches`. All match §8. Device names `Speaker (Realtek(R) Audio)`, `S6-L`, `S6-R`, `UsbDisplay`, `RacerUSB`, `RacerDisplayDriver-2024.9.13-en`, `Win10&11`, `Win 7&8`, `DRIVERS (D:)` all verbatim. ✅
- **§10.2 run-in labels on `infinity/controls.mdx`.** `**Appui court&nbsp;:**`, `**Appui prolongé (2 secondes)&nbsp;:**`, `**Appui prolongé (3 secondes)&nbsp;:**`, `**Appui vers la droite («&nbsp;Plus&nbsp;»)&nbsp;:**`, `**Appui vers la gauche («&nbsp;Min&nbsp;»)&nbsp;:**` — byte-match the §10.2 table, including `seconds`→`secondes` (the §7.3 unit-word trap) and the guillemets on `Plus`/`Min`. ✅
- **Button engravings.** `L`, `R`, `+`, `-` kept verbatim and in EN position; `onecable/controls.mdx:56-57` correctly copies EN's **ASCII hyphen** rather than substituting U+2212, because the EN source uses a hyphen there. ✅
- **Callout lead-ins.** `**Informations importantes&nbsp;:**`, `**Remarque&nbsp;:**`, `**Important&nbsp;:**`, `**Conseil&nbsp;:**` — all §10.1.I conformant; no `**Note&nbsp;:**`, no `**Veuillez noter&nbsp;:**`, no `**Attention&nbsp;!**`. ✅
- **`Please` deletion.** `en/manuals/onecable/safety.mdx:10` "Please read the following guidelines carefully" → `Lisez attentivement les consignes suivantes` — dropped, not rendered as `Veuillez` or `S'il vous plaît` (§1 locked exception: none). ✅
- **§6 literal-translation traps.** Spot-checked every site: `Une fois l'installation terminée`, `prêt à l'emploi`, `Passez alors directement à l'étape&nbsp;5`, `comme illustré sur l'image&nbsp;2`, `à condition que` + subjunctive (`fournisse`, `soient`), `ne fournit pas une puissance suffisante`, `la fiche technique de votre appareil`, `en déplacement`, `améliorer votre productivité`, `Assurez-vous que`, `Veillez à`, `les instructions à l'écran`, `activez l'option en regard de`, `Prenez soin de votre Screenmate`, `afin d'éviter tout dommage`. All locked forms present. ✅
- **`l'ensemble des` drop, `infinity-lite/controls.mdx:9`** — verified genuine: `en/manuals/infinity-lite/controls.mdx:10` says "an overview of **the** physical ports" (no "all"), unlike the OneCable/Infinity variants which do say "all". FR correctly tracks the EN difference. Recorded non-defect, confirmed **not** a defect. ✅
- **`infinity-lite` "both extension screens"** (`fr/…/installation.mdx:9` `les deux écrans d'extension`) — EN+NL mirrored, client flag. Not flagged, per brief. ✅
- **Gender & elision (§2.2).** `le Screenmate`, `l'Infinity Lite` + masculine agreement (`est doté`), `une extension d'écran` (f.), `la fiche USB-A noire` (f.), `le hub` (no elision), `la pochette de transport en cuir fournie` (f. agreement), `la bande en silicone`, `la rainure`, `la pièce centrale`, `les bras mobiles` (m.). All correct. ✅
- **`×` multiplier on count bullets.** `en/manuals/infinity/installation.mdx:32-33` `2× USB-C` / `1× USB-C & …` → FR `2 USB-C` / `1 USB-C, 1 USB et 1 HDMI`. §4 "Counts — drop `x`" vs §2.1 rule 5's `×` carve-out is genuinely ambiguous here; FR is consistent with its own sibling `fr/manuals/expand/installation.mdx:16-18`, so treated as a settled house choice rather than a defect. Noted, not flagged. ✅
- **Raw `&` in `Win10&11` / `Win 7&8`** (`fr/…/installation-windows.mdx:47,54`) — present identically in the EN source; not FR-introduced. Not flagged. ✅

### Method

Every one of the 18 FR pages was read in full against its EN and NL counterparts (54 files), not sampled. Frontmatter (`title`, `description`) was checked against §9.1/§9.2; every H2/H3 against §9.3/§9.4; every `alt=`, `<p>` caption, `<a>` link text and `<Tab title=>` against §10.1.A–I; every `**…:**` run-in against §7/§10.2. Mechanical greps were run first so that reading time went to what greps cannot see.
