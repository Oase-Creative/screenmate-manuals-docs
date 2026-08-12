# Round 4 — German fix log

**Branch:** `round4-fixes`
**Commits:** `fd77217` (glossary + display-settings OS-label pass), `1cf7bbf` (fluency wave),
`bd2b490` (docs), plus the review follow-up commit — see **§F**.
**Inputs triaged:** `fluency-de-a.md`, `fluency-de-b.md`, `safety-align-de.md`, then
`review-de.md` (independent review of this round — §F).
**Files touched:** 41 under `de/**` + `translations/glossary-de.md`. **No `safety.mdx` body was
edited** (`git diff --stat a0525eb..HEAD -- 'de/manuals/*/safety.mdx'` is empty).

**Triage totals** *(including the §F follow-up)*

| Outcome | Count |
|---|---|
| Fixed (real German defects) | **69** distinct edits across 42 files |
| Rejected (locked convention / faithful to source / taste) | **42** |
| Source-flagged (EN/NL defect, German faithful) | **46** rows, logged in `source-flags-de.md` |
| Deferred (worth a native reviewer's eye, not fixed here) | **7** |

Every finding was checked against the aligned `en/` line before a verdict.

> **Correction (§F1).** An earlier version of this paragraph claimed `nl/` was consulted "wherever
> the EN wording was itself ambiguous (the `Need more overview?` … rows in particular)". That claim
> was **overstated**: the NL grep behind it was case-sensitive and silently missed
> `nl/manuals/panorama/osd.mdx:49` `**Meer overzicht nodig?**`, which is why two sites were wrongly
> classified as source-inherited. NL has now been checked case-insensitively at all eight sites and
> the classification corrected — see §F1.

---

## A. Glossary amendments — locked strings that carried meaning errors

Five locked strings were fixed **together with every affected page in the same commit**, as the
brief requires. These are the highest-consequence changes in this round. Three of the five were
corrected again in the review follow-up (§F) — the **Now** column shows the final state.

| § | Was | Now | Why it is a meaning error, not a preference |
|---|---|---|---|
| §9 | `Display orientation → Anzeigeausrichtung` | **`Bildschirmausrichtung`** | `Anzeigeausrichtung` is a coined string. German Windows labels the field **`Bildschirmausrichtung`** under *Skalierung und Layout*. The reader is sent looking for something that is not on their screen. 8 body occurrences + 1 `alt` text updated. |
| §10.1 | `Need more room? / Need more overview? → Brauchst du mehr Platz?` | **`Brauchst du mehr Übersicht?`** at **all 8 sites** *(first split three ways keyed to EN — corrected in §F)* | The single target inverted the meaning: the instruction under it sets scaling to 150 %, which *reduces* usable desktop area. See the superseded-note below and §F1. |
| §9 note | English OS label first, German gloss in parentheses | **German label only, no gloss** *(first "German leads + English gloss" — corrected in §F3)* | The analogy to the NL pages does not hold: the screenshots in this chapter are **Dutch**, so on a German page the English string is on neither the screenshot nor the reader's OS. NL itself carries no gloss. |
| §7.5 | `Browse all Screenmate products → Alle Screenmate-Produkte durchsuchen` | **`… durchstöbern`** *(first `entdecken` — corrected in §F4/M7)* | `durchsuchen` = to search through / rummage (the police *durchsuchen* a flat). It also contradicted its own card title `Produkte ansehen` directly above it. |
| §7.4 | `Power & Return Button → Power- und Zurück-Taste` | **`Power-/Zurück-Taste`** | EN says "Button" (singular) and "Press the … button" — it is **one** button. The suspended-hyphen + `und` form reads as two, so `Drücke die Power- und Zurück-Taste` instructed the reader to press both. §3.5 already establishes slash-suspension (`Menü-/Auswahl-/Bestätigungstaste`) as the house form for a multi-function single button. 4 occurrences (lite, lite-144hz × controls, osd). |

> ### ⚠ Superseded — the three-way split below was wrong. See §F1.
>
> This round first split §10.1 into one row per EN prompt and fixed only the 6 `overview` sites,
> leaving `Brauchst du mehr Platz?` at `infinity/display-settings:30` and `panorama/osd:49`:
>
> | EN prompt | German (as first shipped) | Occurrences | Action then |
> |---|---|---|---|
> | `Need more overview?` | `Brauchst du mehr Übersicht?` | 6 | fixed |
> | `Want more on-screen space?` | `Brauchst du mehr Platz?` | 1 — `infinity/display-settings` | left alone |
> | `Need more room?` | `Brauchst du mehr Platz?` | 1 — `panorama/osd` | left alone |
>
> **That reasoning was keyed to the English and it was wrong.** NL — the ultimate source — says
> `overzicht` at **all eight** sites, so the three EN strings are EN-side drift, not a meaning
> distinction. All eight German sites now read `Brauchst du mehr Übersicht?`, the glossary row is
> folded back into one NL-anchored row with a standing "resolve against the Dutch" ruling, and the
> EN drift is filed in `source-flags-de.md` §8. Full account in **§F1**.

Not part of this family and already correct: `Need extra power?` → `Brauchst du mehr Strom?` —
**3** installation pages (`lite`, `lite-144hz`, `one-4k`; `one-4k-oled` carries no such prompt).

§11.0 was rewritten (see §F2) to state the two chapters' different regimes: **safety** is frozen;
**display-settings** is editable but must stay checksum-identical across its four products.

---

## B. Accepted fixes (before → after)

### B1 — display-settings chapter (shared body, 4 products + 2 own-body products)

| File(s) | Before | After |
|---|---|---|
| `{onecable,dual-flip,flip,expand}/display-settings.mdx` | `wähle **Display settings** („Anzeigeeinstellungen“)` | `wähle **Anzeigeeinstellungen**` *(final state after §F3; this round first shipped it with an English gloss)* |
| idem | `gehe zu „Anzeigeausrichtung“` | `gehe zu „Bildschirmausrichtung“` |
| idem | `**Brauchst du mehr Platz?**` | `**Brauchst du mehr Übersicht?**` |
| `infinity/display-settings.mdx` | `Öffne die **Display settings** („Anzeigeeinstellungen“) und wähle …` | `Öffne die **Anzeigeeinstellungen** und wähle …` *(EN carries no gloss here)* |
| idem | `gehe zu **Anzeigeausrichtung**` | `gehe zu **Bildschirmausrichtung**` |
| `infinity-lite/display-settings.mdx` | `Gehe zu den **Display settings** („Anzeigeeinstellungen“)` | `Gehe zu den **Anzeigeeinstellungen**` — this also removes the page's self-contradiction with line 48, which already said `Anzeigeeinstellungen` |
| idem | `Anzeigeausrichtung` ×2 body + ×1 `alt` | `Bildschirmausrichtung` |
| idem | `**Brauchst du mehr Platz?**` ×2 | `**Brauchst du mehr Übersicht?**` ×2 |
| `panorama/osd.mdx` | `gehe zu **Anzeigeausrichtung**` | `gehe zu **Bildschirmausrichtung**` |

### B2 — English sentence architecture (the Majors both reviewers converged on)

| File | Before | After |
|---|---|---|
| `onecable/index.mdx` | `… ein tragbarer Monitor, der darauf ausgelegt ist, deine Produktivität zu steigern, indem er deinen Laptop mit nur einer Kabelverbindung um zwei zusätzliche Bildschirme erweitert.` | `… ein tragbarer Monitor, der deine Produktivität steigert: Er erweitert deinen Laptop mit nur einer Kabelverbindung um zwei zusätzliche Bildschirme.` |
| `lite/index.mdx` | `… der darauf ausgelegt ist, … zu steigern, indem er deinem Laptop … einen zusätzlichen Bildschirm **hinzufügt**.` | `… der deine Produktivität steigert: Er **erweitert** deinen Laptop, dein Smartphone, dein Tablet oder deine Spielkonsole **um** einen zusätzlichen Bildschirm.` (German extends a device *um* a screen; it does not *add* one *to* it) |
| `lite-144hz/index.mdx` | `Er ist dafür gemacht, Gamern … einen **flüssigen** zweiten Bildschirm … zu bieten.` | `Damit bietet er Gamern und Power-Usern einen zweiten Bildschirm **mit flüssiger Darstellung** …` (a screen is not *flüssig*; its rendering is) |
| `one-4k/index.mdx`, `one-4k-oled/index.mdx` *(twins, edited identically)* | `Er wird über USB-C oder HDMI angeschlossen **und überträgt** auf kompatiblen Geräten Video und Strom …` | `Du schließt ihn über USB-C oder HDMI an. Auf kompatiblen Geräten laufen Video und Strom über ein einziges USB-C-Kabel.` (zeugma: passive + active on one subject, and it made the monitor transmit power) |
| `one-4k/index.mdx` | `Er **gibt** dir einen hochauflösenden zweiten Bildschirm` | `Er **bietet** dir …` |
| `onecable/controls.mdx` | `Dieser Anschluss empfängt Daten und Video von deinem Laptop und kann auch Strom aufnehmen.` | ~~`Über diesen Anschluss empfängt der Monitor …`~~ → **reverted in §F4/M4**; the original was idiomatic (`Strom aufnehmen` is standard German) and port-as-subject matches `:34` and the EN |
| `onecable/controls.mdx` | `Das ist der Hauptanschluss, **um** deinen Laptop über USB-C **anzuschließen**.` | `Das ist der Hauptanschluss **für die Verbindung zu** deinem Laptop über USB-C.` *(final state after §F4/M4 — drops the purpose-infinitive hanging off a copula **and** keeps the "this is the main port" assertion that `en/…:53` later depends on)* |
| `onecable/controls.mdx` | `… und **wird verwendet für:**` | `… und wird **für Folgendes** verwendet:` (stranded preposition before a bullet list is English) |
| `expand/index.mdx` | `… den du an deinen Laptop klemmst und **zu zwei Full-HD-Bildschirmen aufklappst – einer auf jeder Seite**.` | `… den du an deinen Laptop klemmst und aufklappst: Du bekommst zwei Full-HD-Bildschirme, **je einen** auf jeder Seite.` |
| `dual-flip/index.mdx` | `… aufklappst – **einer** auf jeder Seite.` | `… aufklappst – **je einer** auf jeder Seite.` |
| `panorama/index.mdx` | `… der dir drei Full-HD-Bildschirme mit 15,6" **aus einem einzigen Gerät liefert**. … **Er ist dafür gemacht**, deine Arbeitsfläche unterwegs enorm zu erweitern. **Ein erforderlicher Displaytreiber macht es möglich**, drei unabhängige Bildschirme … anzusteuern.` | `… der dir **in einem einzigen Gerät** drei Full-HD-Bildschirme mit 15,6" **bietet**. … **Damit erweiterst du** deine Arbeitsfläche auch unterwegs enorm. **Dafür ist ein Displaytreiber erforderlich: Er steuert** drei unabhängige Bildschirme über ein einziges Kabel **an**.` |
| `infinity/index.mdx` | `… und hast damit zwei zusätzliche Bildschirme **auf einmal**.` | `… und hast damit **gleich zwei** zusätzliche Bildschirme.` (`auf einmal` = suddenly / in one go, not "simultaneously") |
| `infinity-lite/index.mdx` | `… und **ist auf Plug-and-Play mit** Laptops … **ausgelegt**.` | `… und **funktioniert per Plug-and-Play mit** Laptops …` (`auf X ausgelegt sein` needs a purpose, not a feature name) |
| `infinity-lite/index.mdx` | `einen zusätzlichen tragbaren Bildschirm **und** mehr Bildschirmfläche` | `… **und damit** mehr Bildschirmfläche` (EN has a purpose relation, not two separate things) |
| `infinity/controls.mdx` | `… mit der du **das Ein- und Ausschalten**, das Bildschirmmenü, die Helligkeit und die Lautstärke **steuerst**.` | `… mit der du **den Bildschirm ein- und ausschaltest sowie** Bildschirmmenü, Helligkeit und Lautstärke steuerst.` |
| `infinity/installation.mdx` | `Der Ständer **öffnet sich** bis zu einem maximalen Winkel von 235°.` | `Der Ständer **lässt sich** bis zu einem maximalen Winkel von 235° **öffnen**.` |
| `infinity/installation.mdx` | `… muss sauber in die Aussparung am Ständer **fallen**, damit alles fest sitzt.` | `… muss sauber in die Aussparung am Ständer **greifen**, …` (calque of "fall into place"; `fallen` + `fest sitzen` in one sentence is self-contradictory. `greifen` chosen over `einrasten` so as not to claim a click-lock the EN does not) |
| `infinity-lite/controls.mdx` | `Nach links drücken – **stellt** die Hintergrundbeleuchtung (Helligkeit) **ein**.` (+ the „Plus" twin) | `Drücke die Taste nach links, um die Hintergrundbeleuchtung (Helligkeit) einzustellen.` (infinitive phrase + dash + subjectless finite verb: neither half can govern the other) |
| `infinity-lite/installation.mdx` | `Passe den Abstand zwischen dem tragbaren Bildschirm und dem Computerbildschirm **für ein angenehmeres Nutzungserlebnis** nach deinen Vorlieben **an**.` | `Stelle den Abstand zwischen dem tragbaren Bildschirm und dem Computerbildschirm so ein, wie es für dich am angenehmsten ist.` (corporate anglicism + 17 words inside the Satzklammer) |
| `flip/index.mdx` | `Beide seitlichen Bildschirme **klappen** flach an das mittlere Gehäuse` | `Beide seitlichen Bildschirme **lassen sich** flach an das mittlere Gehäuse **klappen**` |
| `flip/installation.mdx` ×2, `expand/installation.mdx` ×1 | `Klappe den rechten Bildschirm **in die in Abbildung 2 gezeigte** Richtung auf.` | `Klappe den rechten Bildschirm **in die Richtung auf, die in Abbildung 2 gezeigt wird**.` (stacked extended attribute; the very next step already used the natural form) |
| `panorama/installation.mdx` | `**Fasse** die Bildschirme **an** und ziehe sie nach oben` | `**Greife** die Bildschirme und ziehe sie nach oben` (`anfassen` = to touch) |
| `panorama/installation.mdx` | `führe **die Schritte oben** in umgekehrter Reihenfolge aus` | `führe **die oben beschriebenen Schritte** in umgekehrter Reihenfolge aus` |
| `panorama/installation.mdx` | `Lade den Treiber **von** der Download-Seite **von** Silicon Motion herunter` | `Lade den Treiber **auf** der Download-Seite von Silicon Motion herunter` |
| `panorama/osd.mdx` | `Der Panorama steuert drei unabhängige Bildschirme an. **Deshalb kannst du** die Anordnung des Desktops … anpassen.` | `… **Vielleicht möchtest du** die Anordnung des Desktops **daher** … anpassen.` (restores EN's `you may want to`; the bare `Deshalb kannst du` read as a non-sequitur) |
| `dual-flip/controls.mdx` ×2 | `Erhöht im normalen Gebrauch die Helligkeit und **navigiert / erhöht Werte** im OSD-Menü.` | `Erhöht im normalen Gebrauch die Helligkeit. Im OSD-Menü navigierst du damit und erhöhst Werte.` (`navigieren` is intransitive and cannot govern `Werte`) |
| `onecable/installation.mdx` | `Hebe den Ständer an und **ziehe ihn mit der Taste aus oder schiebe ihn ein**, um mehr Stabilität zu erhalten.` | `Hebe den Ständer an und **fahre ihn mit der Taste aus oder ein**, um mehr Stabilität zu erhalten.` (a button does not *ausziehen*) |
| `lite/osd.mdx`, `lite-144hz/osd.mdx` | `**Sprache:** Wähle aus 12 verfügbaren Sprachen **für die Anzeige des OSD-Menüs**.` | `**Sprache:** Wähle **die Sprache des OSD-Menüs** aus 12 verfügbaren Sprachen.` (dangling English word order) |
| `manuals-index.mdx` | `Alle Screenmate-Produkte **durchsuchen**` | `Alle Screenmate-Produkte **entdecken**` |

### B3 — Grammar, orthography and punctuation

| File | Before | After |
|---|---|---|
| `onecable/troubleshooting.mdx` ×2 | `in der Menüleiste deines **Mac**` / `das Launchpad deines **Mac**` | `deines **Macs**` (Duden: *der Mac, des Macs*) |
| `onecable/troubleshooting.mdx` | `Schließe falls nötig eine externe Stromversorgung an` | `Schließe**,** falls nötig**,** eine externe Stromversorgung an` |
| `onecable/troubleshooting.mdx` | `Verwende das **doppelte** USB-A-auf-USB-C-Kabel:` | `Verwende das USB-A-auf-USB-C-Kabel **mit zwei USB-A-Steckern**:` (`das doppelte Kabel` is not a German noun phrase; the locked chain `USB-A-auf-USB-C-Kabel` per §3.3 is preserved, and the two plugs are named in the next sentence anyway) |
| `flip/osd.mdx`, `dual-flip/osd.mdx` | `**Vereinfachtes** Chinesisch` | `Chinesisch (vereinfacht)` (English title-case bleed; also harmonises with `expand/osd.mdx`, which already had the correct German form) |
| `lite/index.mdx`, `lite-144hz/index.mdx`, `infinity/index.mdx` | `ein leichter tragbarer …` / `ein faltbarer tragbarer Doppelmonitor` | comma between the coordinate adjectives |
| `infinity/controls.mdx` | `Der Anschluss ist **auf** jedem Bildschirm **auf** der Rückseite … markiert.` | `… ist **an** jedem Bildschirm auf der Rückseite … markiert.` |
| `infinity-lite/controls.mdx` | `Der **äußerste linke** Anschluss an der Unterseite.` | `Der **ganz linke** Anschluss an der Unterseite.` |

### B4 — Terminology drift where EN uses one term and German used several

These are German-internal defects: the EN source is consistent, the German was not.

| EN term | Was (German) | Now |
|---|---|---|
| `connection scenarios` | `Anschlussszenarien` (lite, lite-144hz) / `Anschlussvarianten` (flip) / `lässt sich auf N Arten anschließen` (expand, one-4k, one-4k-oled) | **`Anschlussvarianten`** in all six. Chosen over `Anschlussszenarien` for register (a consumer manual does not have *Szenarien*) and legibility (triple `s`), and it chains cleanly into the following `Wähle die Variante, die …`. |
| `a small amount of power` | `eine geringe Menge Strom` (flip, dual-flip) / `etwas Strom` (onecable, expand) | **`etwas Strom`** in all four. |
| `Power & Return Button` | `Power- und Zurück-Taste` | **`Power-/Zurück-Taste`** — see §A. |
| macOS path glossing on one page | step 4 English-first with gloss, the same path German-only 14 lines later | **German-only in both places**, matching EN which carries no gloss at all on that page (`onecable/installation-mac.mdx`) |
| `Simplified Chinese` | `Vereinfachtes Chinesisch` / `Chinesisch (vereinfacht)` | **`Chinesisch (vereinfacht)`** in all three OSD pages |

### B5 — Modality / collocation fixes

| File | Before | After |
|---|---|---|
| `one-4k/installation.mdx`, `one-4k-oled/installation.mdx` *(twins, edited identically)* | `Bei Unterstützung von Power Delivery (PD) schaltet der Screenmate automatisch **auf die Schnellladefunktion um**.` | `Wenn Power Delivery (PD) unterstützt wird, schaltet der Screenmate automatisch **die Schnellladefunktion ein**.` (you switch *to fast charging*, not *to a function*; the glossary-locked noun `Schnellladefunktion` is kept) |
| `lite`, `lite-144hz`, `one-4k`, `one-4k-oled` `/installation.mdx` | `Um den Screenmate **mit** einer Spielkonsole **mit** USB-C-Anschluss zu verwenden` | `Um den Screenmate mit einer Spielkonsole zu verwenden, **die einen USB-C-Anschluss hat**` (matches EN's relative clause) |

---

## C. Rejected — one line each

**Glossary-locked, and the lock is correct:**

1. `## Bildschirmkonfiguration Windows` → "unter Windows" — locked §7.3 / §11.0, EN heading is `Display Configuration Windows`.
2. `Gewicht | 1820 Gramm` → `1820 g` — §4 locks `Gramm` spelled out, matching EN "grams". (Same for 609/860/1450/1552/1565/1750/1900/2390/3000.)
3. `Blickwinkel` / `Größe` vs `Bildschirmgröße` — §8; EN itself uses `Viewing Angle`, `Size` and `Screen Size` in different products.
4. `Farbgenauigkeit` for sRGB/NTSC coverage — §8; the term error is EN's (`Color Accuracy`). Source-flagged.
5. `das Netzkabel abziehen` — §5 locks it for EN `disconnect the power cable`.
6. `Dedizierter Stromeingang` — §5 locks it for EN `dedicated power input`.
7. `im allgemeinen Modus` — §10.5 locks `General mode → Allgemeiner Modus`. dual-flip's `im normalen Gebrauch` renders a *different* EN string (`in general use`).
8. `Kontrollleuchte der Hauptplatine` — §1.1 locks it; the customer-visibility problem is EN's. Source-flagged.
9. `6× Schutzclips` → `6× Schutzclip` — §1.1 locks the plural form.
10. `Verriegelungsfüße` — §1.1 locks it for `locking legs`.
11. `Ständer für einen Bildschirm` — §1.1 explicitly forbids `Einzelbildschirmständer`.
12. `Taste Ab (−)` / `Taste Auf (+)` — §7.4 locks both.
13. `3 × Mini-HDMI-Anschlüsse` (spaced) → `3×` — §7.4 locks the spaced form, matching EN `3 × Mini HDMI Ports`.
14. `Geh sorgsam mit deinem Screenmate um` → `Gehe` — §10.1 locks the apocopated form.
15. `Option 1 – USB-C (nur ein Kabel)` — §7.4 locked; the one-cable/two-cable contradiction is EN's. Source-flagged.
16. `Achtung:` + `Achte … auf deine Finger` root echo — both halves locked (§10.1, §10.2).
17. `(DP-Monitor)` → spelled-out `DisplayPort` — §5 locks `DP`.
18. `Bildschirmkonfiguration (Betriebssystem)` — §7.3 locks it for `Display Configuration (OS-Level)`.
19. `Warnungen` → `Warnhinweise` in the safety `description` — §7.2 locks it, and `Warnungen` renders EN `warnings` faithfully.
20. `„15,6"-Full-HD-Monitor` → `15,6-Zoll-` — §4: do not expand the inch mark to `Zoll`.
21. Number ranges `0° – 245°` (spaced) → unspaced — §3.6 locks spaced ranges, and EN is spaced too.
22. `- **Helligkeit - (linker Bildschirm)**` ASCII hyphen → `−` (U+2212) — §3.6 says keep the source character, and the EN source uses the ASCII hyphen here.
23. `**OSD-Modus**` (lite) vs `**OSD-Menü-Modus**` (lite-144hz) — §10.5 locks both separately; EN differs the same way.

**Faithful to the source — changing the German would break parity:**

24. macOS block missing quotation marks around UI labels — EN has none either.
25. `display-settings` frontmatter `description` differs on flip — because the **EN** description differs on flip.
26. `am Monitor Screenmate OneCable` → drop `Monitor` — EN says "the Screenmate OneCable monitor", and §7.2 uses exactly this apposition pattern.
27. `die Bildschirmhelligkeit … zu verbessern` vs `Optimierung` elsewhere — EN says `improve` in one place and `optimization` in the other.
28. `HDMI-Verbindung mit … einer Kamera` (alt text) — the camera is in the EN alt text. Source-flagged.
29. `nicht in Gebrauch ist` → `wenn du den Monitor nicht benutzt` — faithful to `when the monitor is not in use`; no meaning gap.
30. `den du **um** deinen Laptop klemmst` (flip) — EN says "clips **around** your laptop", and the Flip does wrap around. Expand's `an` renders EN's "clips **onto**".
31. `montierst` (infinity-lite) vs `befestigst` (infinity) — EN says `mounts` and `clips` respectively.
32. `senkrecht`/`waagerecht` → `Hochformat`/`Querformat` — EN says `vertical`/`horizontal` there and `Landscape/Portrait view` in the captions; two EN vocabularies, faithfully rendered.
33. `<Warning>` callouts containing neutral instructions — component choice is structural parity; changing it in German only is forbidden. Source-flagged.
34. `wähle es oben aus der Liste aus` → "aus" — EN says "from the list above"; the grid-vs-list mismatch is the source's.

---

## D. Deferred — for the native reviewer / client, not fixed here

1. **`safety.mdx` style suggestions (frozen bodies, logged as instructed).**
   (a) Item 12 `Begrenze die Einwirkung von starken Magnetfeldern oder Sendeanlagen` — `Begrenze die
   Einwirkung von` is *limit exposure to* word-for-word, and `Sendeanlagen` is not something a
   consumer meets; a native would write `Halte das Gerät von starken Magnetfeldern und Funksendern
   fern`. (b) The device is called `Monitor` / `Bildschirm` / `Gerät` / `Screenmate` inside one
   14-item list, twice within item 10 — worth fixing `Monitor` for the device and reserving
   `Bildschirm` for the panel, but only in a round that is allowed to reopen the frozen chapter,
   and only alongside EN. Both were verified as *faithful* renderings in `safety-align-de.md`;
   neither changes what the reader must do.
2. **`Anschlussszenarien` register was fixed, but `Szenarien` also appears nowhere else** — if the
   client prefers `Anschlussmöglichkeiten` in the body as well as the heading, that is a one-line
   sweep across six files.
3. **Alt texts on the display-settings chapter carry German OS labels while the screenshots are
   Dutch.** A German screen-reader user is given a label that is not in the image. Consistent with
   §9 and with all four products, so left as-is; worth an accessibility decision.
4. **`die gesamte Farbintensität`** (lite, lite-144hz osd) — literal rendering of EN's "the overall
   color intensity"; the concept error under *Farbtemperatur* is EN's, so the German was left
   faithful. If EN is corrected, correct German with it.
5. **`Verwende das lange weiße Kabel für den Strom und das kurze schwarze Kabel, um … zu verbinden`**
   (panorama/installation) — non-parallel coordination mirroring EN's own non-parallel sentence.
6. **`versorgt werden` without `mit Strom`** (lite, lite-144hz, one-4k, one-4k-oled installation) —
   flagged by reviewer B as ungrammatical. Rejected as a defect: `Das Gerät wird über USB versorgt`
   is standard German engineering usage. Recorded here in case a native reviewer disagrees.

---

## E. Verification (run after the final edit)

```
$ python scripts/verify_translation.py --base en --targets de --include-nl
0 FAIL, 0 WARN

$ python -m pytest tests/test_verify_translation.py -q
....................                                                     [100%]
20 passed in 0.19s

$ git diff --stat HEAD -- 'de/**/safety.mdx'
(no output — safety bodies unchanged)

$ for f in onecable dual-flip flip expand; do
    awk 'BEGIN{c=0} /^---$/{c++; next} c>=2{print}' de/manuals/$f/display-settings.mdx | md5sum
  done
onecable     23c155f4861fc970c03a1d1f0838886a
dual-flip    23c155f4861fc970c03a1d1f0838886a
flip         23c155f4861fc970c03a1d1f0838886a
expand       23c155f4861fc970c03a1d1f0838886a
```

0 FAIL, 0 WARN — and **no new warn classes**: the run was clean before this round and is clean
after it. The four display-settings bodies remain byte-identical after propagation. The twin
products (`lite` / `lite-144hz` and `one-4k` / `one-4k-oled`) received identical edits wherever
their EN pages are identical apart from product name and specs.

---

# F. Review follow-up — `review-de.md` (0 Critical, 3 Important, 16 Minor)

Second pass on `round4-fixes` addressing the independent review. All three Importants fixed, plus
9 of the 16 Minors; the remaining 8 are logged below with reasons. **The review's §0 finding is
recorded: zero target defects were wrongly classified as source-inherited (13 confirmed, 2 partial,
0 wrong).** The two partials were wording errors in the claim documents, both corrected here.

## F1 — Important 3: the scaling prompt, resolved against the Dutch *(the significant one)*

**I was wrong, and the review caught a verification error, not just a judgement call.** §E of this
log claimed `nl/` had been consulted on these rows. It had not been, effectively: the NL grep I ran
was **case-sensitive** and `nl/manuals/panorama/osd.mdx:49` reads `**Meer overzicht nodig?**` with a
capital *M*, so it never appeared in my results. I then reasoned from EN alone and concluded the two
remaining sites were source-inherited.

Re-run case-insensitively, the picture inverts: **NL says `overzicht` at all eight sites.** The
three EN strings are EN-side drift from one Dutch string, and a drifted witness does not outvote the
source.

| Site | NL | EN | Was | Now |
|---|---|---|---|---|
| `infinity/display-settings.mdx:30` | `Heb je behoefte aan meer **overzicht**?` | `Want more on-screen space?` | `Brauchst du mehr Platz?` | **`Brauchst du mehr Übersicht?`** |
| `panorama/osd.mdx:49` | `Meer **overzicht** nodig?` | `Need more room?` | `Brauchst du mehr Platz?` | **`Brauchst du mehr Übersicht?`** |

`grep -rn "mehr Platz" de/` → **0 hits**. All 8 sites now carry `mehr Übersicht`, matching the
Italian resolution in `f66e287` — DE and IT now resolve the same source line on the same principle.

Glossary: the three per-EN-variant rows are **folded back into one NL-anchored row** with a standing
ruling — *this family resolves against the Dutch; do not re-split per EN variant* — plus the full
site table and the NL evidence. Filed as an EN defect in `source-flags-de.md` §8, split into **8a**
(EN drift: 3 strings for 1) and **8b** (the prompt does not match its instruction in *any* language
— 150 % scaling shows *less* at once, so "more overview" is a source-side non-sequitur too).

**The review is also right that §A of this log overstated the win.** `mehr Übersicht` restores
fidelity to the Dutch. It does **not** make the passage logical. That claim has been corrected here
and in the glossary note.

## F2 — Important 1: the glossary contradicted itself about the display-settings freeze

`§11.0` said the chapter was "no longer byte-frozen" and, three lines later, still listed it under
`Frozen chapters (shipped 4792819): safety and display-settings`. Replaced both with one
**freeze-status table** that states the true, different regimes:

- **safety** — FROZEN, 17 files, body not editable; verify `git diff a0525eb..HEAD -- 'de/manuals/*/safety.mdx'` is empty.
- **display-settings** — **not frozen**, editable under the propagation rule; the invariant is
  **byte-identity across the four shared products, enforced by checksum**, not by a freeze. The
  `awk … | md5sum` command is written out in the table so the next round can run it.

## F3 — Important 2: one OS-label gloss pattern, swept

The round-4 note argued the English gloss "helps nobody" on a German page and then kept exactly that
gloss on the one line it rewrote — while making every other page German-only. Resolved to the NL
precedent the note itself cites: **German label only, no gloss, any language, any mention.**

| Site | Was | Now |
|---|---|---|
| `{onecable,dual-flip,flip,expand}/display-settings.mdx:13` | `wähle **Anzeigeeinstellungen** („Display settings“)` | `wähle **Anzeigeeinstellungen**` |
| same file `:31` | already gloss-free (EN has two Dutch glosses) | unchanged — now consistent with `:13` |

Evidence for the ruling: `nl/manuals/onecable/display-settings.mdx:13` is `kies
**Beeldscherminstellingen**` — no gloss, because for a Dutch reader the leading label is already
their own. A German reader is in the same position. Glossary §9 now states the single rule with a
grep check; `grep -rn "Display settings|System Settings|Privacy & Security" de/` → **0 hits**.

## F4 — Minors fixed

| # | File | Was | Now |
|---|---|---|---|
| M4 | `onecable/controls.mdx:17,19` | `Über diesen Anschluss empfängt der Monitor … und kann **darüber** auch mit Strom versorgt werden.` / `An diesem Hauptanschluss schließt du deinen Laptop über USB-C an.` | `Dieser Anschluss empfängt Daten und Video von deinem Laptop und kann auch Strom aufnehmen.` / `Das ist der Hauptanschluss für die Verbindung zu deinem Laptop über USB-C.` — the assertion `en/…:53` depends on is restored, the duplicated connection statement is gone, `darüber` is gone, and port-as-subject is consistent with `:34` again |
| M2 | `infinity-lite/index.mdx:19` | `und **funktioniert** per Plug-and-Play mit …` | `und **ist für den Plug-and-Play-Betrieb** mit … **ausgelegt**` — EN says "is designed for"; the German was promising it works |
| M3 | `panorama/index.mdx:19` | `… erforderlich: **Er steuert** drei unabhängige Bildschirme … **an**.` | `… erforderlich: **Erst er macht es möglich**, drei unabhängige Bildschirme … **anzusteuern**.` — restores EN's `allows … to be driven` |
| M7 | `manuals-index.mdx:101` | `Alle Screenmate-Produkte **entdecken**` | `… **durchstöbern**` — `entdecken` (discover) is a marketing register EN `Browse` / NL `Bekijk` do not have; `durchstöbern` is the exact German for "browse" |
| M8a | `dual-flip/controls.mdx:35,39` | `Im OSD-Menü **navigierst du** damit und **erhöhst** Werte.` | `Im OSD-Menü **dient die Taste zum Navigieren und zum Erhöhen** von Werten.` — keeps one voice inside the entry |
| M8b | `panorama/osd.mdx:41` | `**Vielleicht** möchtest du … **daher** …` | `**Daher** möchtest du … **vielleicht** …` |
| M10 | `lite/index.mdx:19`, `lite-144hz/index.mdx:19` | `ein leichter**,** tragbarer …-Monitor` | comma **reverted** — the pair is hierarchical, not coordinate (`tragbarer …-Monitor` is the Gesamtbegriff, amtl. Regelwerk §71 E1). The sibling `ein faltbarer, tragbarer Doppelmonitor` passes the und-Probe and stays. |
| M13a | `infinity/installation.mdx:174` | `muss sauber in die Aussparung … **greifen**` | `muss genau in die Aussparung … **passen**` — EN `drop neatly into … for a snug fit` is passive seating; `greifen` claimed active engagement |
| M13b | `panorama/installation.mdx:23` | `**Greife** die Bildschirme` | `**Fasse** die Bildschirme **an**` — **reverted**. My stated reason (`anfassen` = "to touch") was wrong: Duden gives *mit der Hand berühren, **ergreifen***, so the original was already correct for EN `Grip`. Reverting also removes the third sense `greifen` had acquired across `de/`. |
| M14 | `lite/osd.mdx:51`, `lite-144hz/osd.mdx:51` | `Wähle die **Sprache** des OSD-Menüs aus 12 verfügbaren **Sprachen**.` | `Wähle eine von 12 verfügbaren Sprachen für das OSD-Menü.` |
| M6 | `glossary-de.md` §10.1 | three round-4 harmonisations applied but unrecorded | rows added for `connection scenarios → Anschlussvarianten` (6 sites, with the scoping note), `a small amount of power → etwas Strom` (4 sites), `Simplified Chinese → Chinesisch (vereinfacht)` (3 sites), **plus** an explicit do-not-normalise row for the EN strings that only *look* similar (`connection methods`, `can be connected in the following ways`) |
| M9 | claim documents | three inaccuracies | (a) `Need extra power?` corrected 4 → **3** sites; (b) `source-flags` §2 rewritten — only `flip/index` is a true same-value split, `expand` differs in value and `onecable`/`lite`/`dual-flip` have no in-file split at all; (c) `source-flags` §7 reworded — the infinity-lite `'Mirrored'` line **is** collapsed onto the `Flipped` target and that is correct and glossary-locked; the old flag text misdescribed the file |

## F5 — Minors rejected, one line each

1. **M1** (`designed to / built to` asserted as fact on 5 product intros) — kept. German product copy
   asserts; confined to non-procedural marketing prose; the review calls it defensible. The one
   member that crossed into a capability promise (M2) *was* fixed. Flagged for client sign-off.
2. **M5a** (`for a better user experience` dropped at `infinity-lite/installation:58`) — kept.
   `so ein, wie es für dich am angenehmsten ist` carries the adjunct; restoring it literally
   reinstates the `Nutzungserlebnis` anglicism the fix removed.
3. **M5b** (`mit zwei USB-A-Steckern` explicitates EN `dual`) — kept. `das doppelte Kabel` was not a
   German noun phrase and the detail is stated two lines later in EN; the reader must be able to
   identify the accessory in a troubleshooting answer.
4. **M5c** (`umschalten` → `einschalten` for EN `switches to fast-charge mode`) — kept, **but the
   stated reason in §B5 was wrong**: EN does say *mode*. The rendering stands only because
   `Schnellladefunktion` is glossary-locked, which rules out `in den Schnelllademodus um`. Reason
   corrected here.
5. **M11** (`von`-stacking at `panorama/installation:43`) — rejected. The stacking *was* removed:
   `von der Download-Seite **von** Silicon Motion` (two adjacent `von`-phrases) is now
   `auf der Download-Seite **von** Silicon Motion` (one). The suggested
   `Silicon-Motion-Downloadseite` would collide with §3.4, which forbids coupling a multi-token
   brand into a German compound.
6. **M12** (passive/active split across four sibling index pages) — rejected. The One 4K rewrite was
   driven by a *meaning* defect (the coordination made the monitor the thing that transmits power),
   not by the diathesis alone. `Er wird über USB-C oder HDMI angeschlossen und wiegt nur 609 Gramm`
   coordinates a passive with a harmless stative and reads fine; changing it would be churn.
7. **M15** (commas around `falls nötig`) — kept. The review itself notes both forms are correct
   (amtl. Regelwerk §77 E1) and that there is "no defect either way". Logged so it is not re-flagged.
8. **M16** (`Bildschirmausrichtung` is the Windows 11 label while `Desktop auf diese Anzeige
   erweitern` is Windows 10-era) — no change; the fix is an improvement regardless. Added to the
   deferred list for verification against a live German Windows 11 install before ship.

## F6 — Verification (re-run after the follow-up)

```
$ python scripts/verify_translation.py --base en --targets de --include-nl
0 FAIL, 0 WARN

$ python -m pytest tests/test_verify_translation.py -q
....................                                                     [100%]
20 passed in 0.18s

$ git diff --stat a0525eb..HEAD -- 'de/manuals/*/safety.mdx'
(no output — safety bodies untouched since a0525eb)

$ for f in onecable dual-flip flip expand; do
    awk 'BEGIN{c=0} /^---$/{c++; next} c>=2{print}' de/manuals/$f/display-settings.mdx | md5sum
  done
onecable     77cfed71bc3e4b0b63e9ea963e4c44aa
dual-flip    77cfed71bc3e4b0b63e9ea963e4c44aa
flip         77cfed71bc3e4b0b63e9ea963e4c44aa
expand       77cfed71bc3e4b0b63e9ea963e4c44aa

$ grep -rn "mehr Platz" de/                                              -> 0 hits
$ grep -rn "Display settings|System Settings|Privacy & Security" de/     -> 0 hits
```

The shared body checksum changed from `23c155f4…` to `77cfed71…` because the I2 gloss sweep edits
that body; all four products moved together and remain byte-identical, which is the invariant that
matters. 0 FAIL, 0 WARN with no new warn classes.
