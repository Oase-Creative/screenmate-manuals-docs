# FR remediation log — Task 10 findings

**Branch:** `lang-expansion-de-fr-it` · **Date:** 2026-08-11 · **Sources:**
`adversarial-fr-F1.md`, `-F2.md`, `-F3.md`, `-F4.md`, `backtranslation-review-fr.md`.
**Binding:** `translations/glossary-fr.md` (§0 precedence rule 3 — shipped QC'd pages outrank the
glossary; §4.1 spacing).

**Totals: 28 distinct findings applied across 34 `fr/` pages + 2 governance files; 11 skipped with reason.**

Line numbers are stable before and after: every edit is a one-line, in-place replacement — no
file changed its line count.

**Invariants after the pass**

| Gate | Result |
|---|---|
| `python scripts/verify_translation.py --base en --targets fr` | `0 FAIL, 0 WARN`, exit `0` |
| Group-A `safety.mdx` body md5 (onecable, lite, lite-144hz, flip, expand, one-4k, one-4k-oled) | `252d38c7ba75e62be909e889175ed7a2` — byte-identical ×7 |
| `dual-flip/safety.mdx` body md5 (its own EN group — bullets, not numbered) | `cffcd1c8123d867a6f0da091847cf8a1` |
| Frozen `display-settings` body md5 (onecable / flip / dual-flip / expand) | unchanged, still byte-identical ×4 |
| Glossary §11 greps 1, 1b, 2, 3, 4, 5, 7, 9, 10, 11, 14, 15, 16, 17, 18 | 0 hits |
| Glossary §11 greps 6, 8 | only the two pre-existing, previously-recorded false positives (`USB-A 2.0` in an `alt=`, `câble transporte à la fois`) |
| FR `lite` ↔ `lite-144hz` `installation.mdx` prose divergence | **0 lines** (was 11) — now matches the EN baseline exactly (description + image paths only) |

---

## 1 · SAFETY (highest priority) — misplaced `uniquement`

**Finding:** F2-6 / F4-1 (Major ×2, same defect). EN `Only use the device **with** a 5V power
source` restricts the *power source*; the FR word order attached `uniquement` to `l'appareil`
("use only the device"), detaching the restriction from the thing it must restrict. NL, DE and IT
all place the restrictive adverb after the object; FR was the sole outlier, and it contradicted
items 2 and 8 of its own list.

**Change** (F4-1's proposal, chosen over F2-6's `N'utilisez … qu'avec` because it mirrors item 8's
existing `Nettoyez l'écran uniquement avec…` pattern character-for-character and is the smaller edit):

```
- Utilisez uniquement l'appareil avec une source d'alimentation de 5&nbsp;V via le câble approprié.
+ Utilisez l'appareil uniquement avec une source d'alimentation de 5&nbsp;V via le câble approprié.
```

Re-propagated byte-identically to the whole frozen group in this commit:

| File:line | Group |
|---|---|
| `fr/manuals/onecable/safety.mdx:16` | A (canonical) |
| `fr/manuals/lite/safety.mdx:16` | A |
| `fr/manuals/lite-144hz/safety.mdx:16` | A |
| `fr/manuals/flip/safety.mdx:16` | A |
| `fr/manuals/expand/safety.mdx:16` | A |
| `fr/manuals/one-4k/safety.mdx:16` | A |
| `fr/manuals/one-4k-oled/safety.mdx:16` | A |
| `fr/manuals/dual-flip/safety.mdx:16` | separate EN group (bulleted); same sentence, same fix |

`panorama`, `infinity` and `infinity-lite` safety chapters do **not** carry this EN item — verified,
not assumed (`grep "Only use the device" en/manuals/*/safety.mdx` → 8 files).

Group-A checksum verified identical on all seven **after** the edit, and the verifier's `dedupe`
FAIL check (which enforces exactly this) passes.

---

## 2 · Negation-scope inversions

`tous les X ne … pas` is the ambiguous French partial-negation frame and is routinely read as total
negation — the opposite operational advice. Rewritten with `ne … pas tous`, which is unambiguous
and keeps the full `ne … pas` per §5.5. On the three `phone/tablet` sites the partitive `de` under
negation (a second cue for *complete* negation, per F4-2) was also lifted to `un signal vidéo`.

| Finding | File:line | Change |
|---|---|---|
| F1-01 (Medium, `<Note>` callout) | `fr/manuals/infinity/installation.mdx:63` | `tous les ports USB-C ne prennent pas en charge la sortie vidéo` → `les ports USB-C ne prennent pas tous en charge la sortie vidéo` |
| F4-2 (Major) | `fr/manuals/one-4k/installation.mdx:45` | `tous les ports USB-C ne peuvent pas transmettre de signal vidéo` → `les ports USB-C ne peuvent pas tous transmettre un signal vidéo` |
| F4-2, same pattern | `fr/manuals/lite/installation.mdx:35` | same rewrite (also carried the §5.2 and twin-parity fixes, §4 below) |
| F4-2, same pattern | `fr/manuals/lite-144hz/installation.mdx:35` | `… ne peuvent pas transmettre d'image` → `les ports USB-C ne peuvent pas tous transmettre un signal vidéo` |

A corpus-wide sweep for `tous les … ne …` / `toutes les … ne …` returned exactly these four sites;
all four are fixed. Post-fix sweep: 0 hits.

---

## 3 · Gender / grammar

| Finding | File:line | Change |
|---|---|---|
| F2-1 (Major) | `fr/manuals/lite-144hz/installation.mdx:57` | `ou **une** Nintendo Charging Dock` → `ou **un** Nintendo Charging Dock` — `dock` is masculine; §2.2 gives no feminine override for third-party names; the sibling `lite` page already had the correct form for a byte-identical EN sentence |

---

## 4 · Twin / family harmonisation

### 4a · `lite` ↔ `lite-144hz` `installation.mdx` — 11 line pairs (F2-2, Major)

EN body diff between the two products: **0 lines**. FR body diff was **11**. Winners picked per
F2's divergence inventory; result is 0 prose divergence.

| Pair | Surviving form | File(s) edited |
|---|---|---|
| 13 | `…à votre ordinateur portable **à l'aide du** câble USB-C vers USB-C.` | `lite-144hz/installation.mdx:13` |
| 19 (alt) | `alt="Connexion USB-C à **l'**ordinateur portable"` | `lite-144hz/installation.mdx:19` |
| 23 (alt) | `alt="Connexion USB-C à **l'**ordinateur portable avec alimentation supplémentaire"` | `lite-144hz/installation.mdx:23` |
| 27 | `Connectez le Screenmate **à l'aide d'un** câble HDMI…` | `lite-144hz/installation.mdx:27` |
| 31 (alt) | `alt="Connexion HDMI à **l'**ordinateur portable"` | `lite-144hz/installation.mdx:31` |
| 35a (= F2-4, Moderate) | `vous pouvez **brancher** … directement **sur le** port USB-C` — §5.2 splits the verb by object; the object is a *port* | `lite/installation.mdx:35` |
| 35b | `un port USB-C **compatible vidéo**` | `lite/installation.mdx:35` |
| 35c | `**un signal vidéo**` (§5.4 term; also the F4-2 negation fix) | both |
| 37 (alt) | `alt="Connexion USB-C **au téléphone ou à la tablette**"` | `lite-144hz/installation.mdx:37` |
| 41 (alt) | `alt="Connexion USB-C **au téléphone ou à la tablette** avec alimentation supplémentaire"` | `lite-144hz/installation.mdx:41` |
| 47 / 59 | `raccordez-le au moniteur **à l'aide du** câble USB-C vers USB-A.` (×2) | `lite-144hz/installation.mdx:47,59` |
| 57 | `**un** Nintendo Charging Dock` (= F2-1) | `lite-144hz/installation.mdx:57` |

### 4b · Other `lite` twin divergences

| Finding | File:line | Change |
|---|---|---|
| F2-3 (Moderate) | `fr/manuals/lite-144hz/controls.mdx:38` | `menu **de** réglages` → `menu **des** réglages` (§5.4 lock; `lite` already correct) |
| F2-7 (Moderate) | `fr/manuals/lite/osd.mdx:28` | `lisibilité optimale **pour le** texte.` → `lisibilité optimale **du** texte.` (adopt 144hz form) |
| F2-7 (Moderate) | `fr/manuals/lite/osd.mdx:30` | `optimisé pour **les jeux**.` → `optimisé pour **le jeu**.` — restores the generic/specific contrast against lines 26–27 (`les jeux RTS` / `les jeux FPS`) |
| F2-8 (Minor) | `fr/manuals/lite-144hz/controls.mdx:32` | `revenir d'une étape en arrière` → `revenir en arrière d'une étape` |

The remaining `lite` ↔ `lite-144hz` differences are the genuine 144 Hz differentiators
(`144&nbsp;Hz` spec row + marketing sentence, `Mode menu OSD` vs `Mode OSD`, product-name
expansion) and were deliberately left in place.

### 4c · `de l'une des manières suivantes` (F1-02, Low)

`fr/manuals/dual-flip/installation.mdx:9` and `fr/manuals/flip/installation.mdx:9` — both shipped
and QC'd — already render EN `in the following ways` as `de l'une des manières suivantes`. §0
precedence rule 3 makes the shipped form win and the glossary is amended to match.

| File:line | Change |
|---|---|
| `fr/manuals/infinity/installation.mdx:29` | `connecté des manières suivantes` → `connecté de l'une des manières suivantes` |
| `fr/manuals/expand/installation.mdx:14` | same |
| `translations/glossary-fr.md:693` (§6 row) | locked target changed to `de l'une des manières suivantes`, annotated as the shipped form |

### 4d · `prédéfini` vs `préréglé` — unified corpus-wide (F3-03, Minor)

§5.4 locks `preset` → `préréglage`; `préréglé` is the stem-aligned adjective and is what
`dual-flip` and `expand` already use. `flip` was the sole outlier, in two places.

| File:line | Change |
|---|---|
| `fr/manuals/flip/osd.mdx:20` | `modes d'image **prédéfinis**` → `modes d'image **préréglés**` (the noun `modes d'image` is **kept** — EN genuinely says `picture modes` here vs `display modes` on the siblings) |
| `fr/manuals/flip/osd.mdx:34` | `un mode **prédéfini**` → `un mode **préréglé**` (EN `a preset mode`, unique to flip — the EN difference is preserved) |

Post-fix sweep: `grep -rn "prédéfini" fr/` → 0 hits.

### 4e · Family paraphrase drift, `flip` / `dual-flip` / `expand` (F3-02, Minor)

Byte-identical EN sentences were getting different French across the family. One rendering per EN
sentence, propagated:

| EN sentence | Surviving French | File:line edited |
|---|---|---|
| `Connect the other side using/with the HDMI cable …` | `**Branchez** l'autre côté…` (a cable is being plugged in → §5.2 `brancher`) | `dual-flip/installation.mdx:41`, `expand/installation.mdx:54` (`avec` vs `à l'aide de` kept — mirrors a real EN `with`/`using` split) |
| `Use the included USB-C cable to connect one side …` | `…pour **relier** un côté…` | `dual-flip/installation.mdx:41` |
| `use the two included USB-C cables to connect your laptop to the Screenmate` | `…pour connecter **votre ordinateur portable** au Screenmate.` | `flip/installation.mdx:59` |
| `first check which ports your laptop has` | `vérifiez d'abord **de quels ports dispose** votre ordinateur portable.` | `dual-flip/installation.mdx:9` |
| `Use the icons below as a reference.` | `**Utilisez les icônes** ci-dessous comme référence.` | `flip/installation.mdx:22` |
| `… and store it in a safe place.` | `…et rangez-le **en lieu sûr**.` | `dual-flip/installation.mdx:56` |

Not touched: `flip/installation.mdx:9` (`vérifiez d'abord quels ports sont concernés`) — its EN
genuinely differs (`check which ports are involved`), and the EN inconsistency it reflects is
back-translation EN-source issue #12, i.e. an `en/` problem.

### 4f · `one-4k` ↔ `one-4k-oled` (F4-5 Minor, F4-6 Low)

| Finding | File:line | Change |
|---|---|---|
| F4-5 | `fr/manuals/one-4k-oled/index.mdx:15` | `un écran portable **15,6" 4K UHD**` → `un écran portable **4K UHD de 15,6"**` — EN is character-identical across the pair; adopt the more idiomatic `one-4k` form |
| F4-6 | `fr/manuals/one-4k/index.mdx:15`, `fr/manuals/one-4k-oled/index.mdx:15` | `et **transporte à la fois** la vidéo et l'alimentation` → `et **prend en charge** la vidéo et l'alimentation` — EN `supports` is a capability statement; `transporte` is reserved for EN `carries` (`controls.mdx:13,19`), restoring the EN supports/carries distinction |
| F4-5 (bookkeeping) | `translations/flags/fr-one-4k-oled.md:113–114` | the "every remaining difference corresponds to a real EN difference" claim was **false** for `index.mdx:15`; note corrected and both fixes recorded |

### 4g · RESET — dropped goal complement (F4-4, Minor)

EN has a patient (*all settings*) **and** a goal (*to factory defaults*); FR collapsed both into one
noun phrase, so `tous` re-attached to `réglages d'usine` ("restore all the factory settings").

`pour rétablir tous les réglages d'usine.` → `pour rétablir tous les réglages **à leurs valeurs**
d'usine.` at `fr/manuals/dual-flip/osd.mdx:51`, `fr/manuals/expand/osd.mdx:53`,
`fr/manuals/flip/osd.mdx:51`.

---

## 5 · Remaining minors and lows

| Finding | File:line | Change |
|---|---|---|
| F1-04 (Low) | 10 `Dimensions` spec cells (`dual-flip/index:44`, `flip/index:46,65`, `infinity-lite/index:45`, `lite/index:34`, `lite-144hz/index:34`, `one-4k/index:36`, `one-4k-oled/index:34`, `onecable/index:101,121`) | plain space → `&nbsp;cm`, per the §4.1 mechanical rule (number + unit symbol). This removes the FR-vs-FR split against `expand/index:49,68`, `infinity/index:47` and `panorama/index:44`, which already used `&nbsp;cm`. **Scope note:** the §5.7 package-contents parentheticals `(60 cm)`, `(90 cm)`, `(1,2 m)` were deliberately **not** touched — §5 term tables outrank §4/§4.1 typography under the §0 precedence order, so the locked strings stand. `translations/glossary-fr.md` §4 decimal-separator example corrected to `2,5&nbsp;cm` / `3,5&nbsp;mm` / `40,6 × 23,7 × 2,5&nbsp;cm` so the glossary stops contradicting itself; the `cm`-spacing note in `translations/flags/fr-one-4k-oled.md` marked resolved. |
| F1-05 (Low) | `fr/manuals/infinity-lite/display-settings.mdx:23` | `en faisant glisser chacun d'eux **pour correspondre à** sa position physique` → `**pour qu'il corresponde à**` — removes the dangling infinitive whose implied subject was `vous`, not the screen |
| F1-06 (Low) | `fr/manuals/infinity-lite/installation.mdx:46` | `**Dépliez** le support` → `**Ouvrez** le support` — EN is `Open the stand`; §5.5 maps `Open` → `Ouvrez`, `Unfold` → `Dépliez`; matches `fr/manuals/infinity/installation.mdx:76` for the identical EN instruction |
| F1-07 (Low) | `fr/manuals/infinity-lite/installation.mdx:69` | `deux **principales méthodes** de connexion` → `deux **méthodes de connexion principales**` — antéposed `principal` after a bare numeral is marked in French and calques the EN modifier stack |
| F1-08 (Low) | `fr/manuals/onecable/troubleshooting.mdx:33` | `C'est possible, à condition que les **conditions** suivantes soient réunies` → `C'est possible **si** les conditions suivantes sont réunies` — breaks the `condition`/`conditions` root repetition. §6's `provided that` → `à condition que` lock still governs its other sites (unchanged). |
| F2-5 (Moderate) | `fr/manuals/panorama/installation.mdx:28` | `**Attention&nbsp;:** **faites attention à** vos doigts` → `**Attention&nbsp;:** **prenez garde à** vos doigts` — kills the `Attention : faites attention…` stutter. §6 locks `Watch your fingers` → `Attention à vos doigts`, which cannot be pasted verbatim after an `**Attention&nbsp;:**` lead; the locked form remains in place at `fr/manuals/panorama/safety.mdx:26`. |
| F2-9 (Minor) | `fr/manuals/lite/index.mdx:15` | `un écran portable Full HD **15,6" léger**` → `un écran portable Full HD **léger de 15,6"**` — un-strands the adjective; matches the sibling `lite-144hz/index.mdx:15` |
| F2-10 (Minor) / BT row 7 | `fr/manuals/panorama/index.mdx:15` | `(ou USB-A + HDMI **en alternative**)` → `(ou USB-A + HDMI **en solution de repli**)` — EN says `as a fallback`; the page's own `### Option 2` frames it as the path for laptops whose USB-C port carries no video, not a co-equal choice |
| F2-11 (Minor) | `fr/manuals/panorama/installation.mdx:54` | `le **court câble noir**` → `le **câble noir court**` — a prenominal `court` in front of a noun already carrying a postnominal colour adjective is unidiomatic |
| F3-04 (Low) | `fr/manuals/flip/controls.mdx:24–25` | `— **A**ugmenter` / `— **D**iminuer` → lowercase, matching `- **M** — bouton du menu OSD.` on line 23 and the §9.4 lock `### M — bouton du menu OSD` |
| F3-05 (Low) | `fr/manuals/flip/installation.mdx:80` | `de 180° **en sens inverse, dans le sens indiqué**` → `de 180° **pour le ramener dans le sens indiqué**` — the EN `back` is an adverb of return, not a second direction; the old text read as self-contradictory |
| F3-06 (Low) | `fr/manuals/flip/index.mdx:15` | `…**pour vous offrir** deux écrans supplémentaires, **gage d'**une meilleure vue d'ensemble et d'une plus grande concentration.` → `…**et vous offre** deux écrans supplémentaires **pour** une meilleure vue d'ensemble et plus de concentration.` — `gage de` ("guarantee of") inflated a benefit statement into a guarantee. F3's proposed tail is used verbatim; the preceding verb was switched from `pour vous offrir` to `et vous offre` so the sentence does not stutter `pour … pour`. |
| F3-07 (Low) | `fr/manuals/flip/index.mdx:8` | `**valable pour** les modèles 14" et 15,6"` → `**qui couvre** les modèles 14" et 15,6"` — `valable pour` is a validity/legal register; the clause is about coverage. The rest of the Welcome block still byte-matches the §10 lock (which ends at "…accéder à chaque section."). |

---

## 6 · Skipped, with reason

| # | Finding | Reason |
|---|---|---|
| S-01 | F1-10 / F2-12 / F3-01 / F4-3 / BT "non-semantic note" — no `en_link:` / `nl_link:` on any FR page | **FALSE POSITIVE for this task.** Cross-language link frontmatter is generated by `scripts/generate_language_links.py` in a later, dedicated task; it is repo-wide (0/61 FR, 0/61 DE, 0/61 IT) and is not a translation defect. Explicitly out of scope per the brief. |
| S-02 | BT §2, all 22 EN-source issues (10 W boundary, `Flipped`/`Mirrored`, two-vs-three signal sources, `Installation steps 1 through 6`, empty `USB-A Port` heading, OSD TODOs, `Color Gamut`/`Color Accuracy`, `Dimensions (folded)` on a non-folding monitor, Dutch UI glosses in `en/`, …) | EN-side defects. `fr/` mirrors them faithfully, which is correct. Editing `fr/` to paper over an `en/` fault would break EN↔FR parity. Client list — fix `en/` first, then re-propagate. |
| S-03 | BT rows 1, 3, 4 — `>10 W`/`<10 W` gap; `Flipped`; `Mirrored` | EN-source quirks, already adjudicated in the back-translation review. Row 4 is the one place FR silently *corrected* EN; that correction is kept. |
| S-04 | BT rows 2, 9 — macOS `Moniteurs` vs `Displays`; `bracket`/`stand` rendering | Loop artifacts. The FR source is consistent and correct (`Moniteurs` is the genuine French macOS pane; `support de fixation` / `support réglable` distinguish the two parts). Excluded per the brief. |
| S-05 | F1-03 — `Power` left untranslated at `onecable/controls.mdx:49`, `onecable/installation.mdx:54`, `onecable/troubleshooting.mdx:37` | The report itself says **"Glossary decision — do not fix unilaterally (§12)."** `Power` is not in `dnt.json` (only `Power Delivery` is), so the choice is between rendering `le port d'alimentation` everywhere (§9.4) or adding `Power` to `dnt.json` as an on-device label. Needs a §12 proposal + sign-off, not a unilateral edit. **Open for the orchestrator.** |
| S-06 | F1-09 (Info) — the six Dutch UI glosses in `en/` are dropped in FR | No page edit proposed by the report; applied uniformly and deliberately, and adjacent to the recorded "Dutch Windows screenshots" client question. BT row 10 independently adjudicates the drop as **correct localisation**. Client question, not a defect. |
| S-07 | BT row 5 — card title `Voir les produits` for EN `Shop Products` | `translations/glossary-fr.md` §10 (line 1170) **locks** `Shop Products` → `Voir les produits`, and the shipped page matches the lock. BT scores it cosmetic with intent intact (`href`, body copy and `shopping-cart` icon unchanged) and recommends no FR remediation. Changing it would break a §10 lock for a cosmetic gain. |
| S-08 | BT row 8 — `stability rubbers` → `patins antidérapants` | §5.7 **locked** package-contents rendering. Same component, same quantity (8), same use case. Cosmetic per BT. |
| S-09 | BT row 6 — pinch-hazard scope narrowed to `repliez` (closing) only | The **verb** half was fixed (F2-5 above). The **scope** half was deliberately not widened: `en/manuals/panorama/installation.mdx:29` says only "when folding the screens" — it is `en/manuals/panorama/safety.mdx:27` that says "in or out", and the FR safety page already carries `repliez ou dépliez`. Adding "ou dépliez" to the installation callout would add meaning the EN installation line does not have. EN-side ambiguity; recorded for the client list. |
| S-10 | F3 recorded non-defects N-01 … N-05; F4 §8 "deliberately not flagged" items | Verified correct by their reviewers and explicitly marked do-not-fix. Left untouched: the `1 câble adaptateur USB-C vers USB-A (90 cm)` §5.7 string, the two bold shapes for left/right screen labels, the plural verb after `A comme B`, the translated `LANGUAGE` value list, `alt="Étapes d'installation 1 à 6"`, the `{/* TODO */}` comments kept EN-verbatim, and the `Menu OSD {Section}` alt shape (ruling R9). |
| S-11 | F4 §8 — FR-vs-EN/NL unit-spacing divergence (`45&nbsp;W` vs `45W`, `100&nbsp;%` vs `100%`, `-20&nbsp;°C` vs `-20°C`) | Deliberate, locked §4 divergence ("do not 'restore' the EN spacing"); glossary §12 open item 2, pending a client cross-language comparison. Only the **FR-internal** `cm` split was in scope, and it is fixed (F1-04 above). |
