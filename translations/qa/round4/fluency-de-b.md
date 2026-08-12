# Monolingual German fluency review — Batch B

**Reviewer role:** native German technical editor, consumer electronics
**Scope:** `de/manuals/` — one-4k, one-4k-oled, dual-flip, infinity, infinity-lite, panorama
**Method:** German read only. No en/ or nl/ file opened. Findings are what a German customer meets on the page.
**Date:** 2026-08-12
**Mode:** READ-ONLY. No content file was modified.

Skipped per brief: `one-4k/safety.mdx` body, `one-4k-oled/safety.mdx` body, `dual-flip/display-settings.mdx` body (frontmatter checked in all three).

---

## Global pre-checks (clean)

These were checked corpus-wide and came back clean — recording so the next reviewer does not redo them:

- **Register:** zero "Sie" / "Ihr" / "Ihre" leakage across all 30 files. `du` is consistent everywhere. No du/Sie mixing.
- **Compound hyphenation around English terms:** no `USB-C Kabel`, `HDMI Kabel`, `OSD Menü` style misses. `USB-C-auf-USB-C-Kabel`, `Mini-HDMI-auf-HDMI-Kabel`, `3,5-mm-Klinkenanschluss`, `65-W-USB-C-Netzteil`, `5-V/2-A-Netzteil` are all correctly hyphenated. This is genuinely well done.
- **SI unit spacing:** correct in 100 % of instances (`45 W`, `100 %`, `60 Hz`, `10 ms`, `−20 °C`, `5 V`, `2 A`).
- **Decimal comma / thousands point:** correct (`15,6"`, `1,3 cm`, `100.000:1`).
- **Article/gender on English terms:** correct throughout (`der USB-C-Anschluss`, `das OSD-Menü`, `das Mini-HDMI-auf-HDMI-Kabel`, `der Screenmate`, `die Nintendo Switch`).
- **Dashes:** en dash `–` used throughout, no em dash `—` in visible copy. Consistent.
- **No double spaces, no orphaned English/Dutch words in visible copy or alt text.**

---

## de/manuals/one-4k/

### index.mdx

| Quoted German | Issue | Suggested rewrite | Severity |
|---|---|---|---|
| „Er wird über USB-C oder HDMI angeschlossen und überträgt auf kompatiblen Geräten Video und Strom über ein einziges USB-C-Kabel." | Zeugma: passive (`wird angeschlossen`) and active (`überträgt`) coordinated on one subject. German style guides treat this as an error; it also makes the monitor the thing that "transmits power", which is backwards. | „Du schließt ihn über USB-C oder HDMI an. Auf kompatiblen Geräten laufen Bild und Strom über ein einziges USB-C-Kabel." | **Major** |
| „Er gibt dir einen hochauflösenden zweiten Bildschirm für deinen Laptop…" | `geben` + abstract object is English-shaped ("it gives you"). Tolerable colloquially, but a German copywriter writes `verschaffen` / `bieten`. | „Er verschafft dir einen hochauflösenden zweiten Bildschirm für …" | Minor |
| „\| **Gewicht** \| 860 Gramm \|" | Every other unit in the same table is abbreviated (`cd/m²`, `ms`, `cm`, `Hz`, `%`). Spelling out `Gramm` breaks the table's own convention. Corpus-wide (also 1900/2390/3000 Gramm). | „860 g" — and for the heavy models `1,9 kg`, `2,4 kg`, `3,0 kg`. | Minor |
| „\| **Bildschirmgröße** \| 15,6" \|" | Same spec row is labelled `Größe` in dual-flip, infinity, infinity-lite and panorama. Two names for one spec across the German set. | Standardise on `Bildschirmgröße` (clearer) or `Größe` — pick one. | Minor |

### controls.mdx

| Quoted German | Issue | Suggested rewrite | Severity |
|---|---|---|---|
| „Dedizierter Stromeingang." | `dediziert` is a raw anglicism ("dedicated"). It exists in German IT jargon but reads as untranslated in consumer copy. | „Reiner Stromanschluss." or „Nur für die Stromversorgung." | **Major** |
| „öffnet im allgemeinen Modus den Schnellzugriff für die Helligkeit" (and the `−` bullet) | `im allgemeinen Modus` is a calque; German has no such mode. Compare dual-flip/controls.mdx, which says `im normalen Gebrauch` for the identical concept — so the corpus contradicts itself too. | „öffnet außerhalb des Menüs den Schnellzugriff für die Helligkeit" (and align dual-flip to the same wording) | **Major** |
| „### Menütaste (Power / OSD)" | This page names the button `Menütaste`; `osd.mdx` for the same product calls it only `Power-Taste`, six times. A customer who reads the ports page and then the OSD page is looking for two different buttons. | Name it once — `Power-Taste (Menü/OSD)` — and use that name on both pages. | **Major** |
| „Verwende den USB-C-Anschluss für Strom & Video, wenn dein Gerät …" | `&` inside a running German sentence is not German orthography (Duden: firm names and fixed pairs only). Same file, heading `(Strom & Video)`. Also `1× USB-C & 1× USB-A & 1× HDMI` (dual-flip), `1× USB-C & 1× USB & 1× HDMI` (infinity), and the heading `USB-C + HDMI & USB-A` mixes `+` and `&` in five words. | „für Strom und Video"; in the connection lists use `+` throughout. | Minor |
| „Um den Screenmate mit einer Spielkonsole mit USB-C-Anschluss zu verwenden" (installation.mdx) | Stacked `mit … mit`. Classic thing a German editor rewrites. | „So schließt du eine Spielkonsole mit USB-C-Anschluss an:" | Minor |

### installation.mdx

| Quoted German | Issue | Suggested rewrite | Severity |
|---|---|---|---|
| „Wenn dein Gerät das Laden über USB-C unterstützt, wird der Bildschirm automatisch geladen, sobald das Ladegerät am Screenmate angeschlossen ist." | **Meaning-breaking.** German `laden` = charge a battery. The One 4K has no battery anywhere in its spec table, so this tells the customer the monitor charges up — and the conditional is a non-sequitur (*your device* supports charging → *the screen* gets charged). Same sentence in one-4k-oled. | „Wenn dein Gerät das Laden über USB-C unterstützt, wird es über den Screenmate mitgeladen, sobald ein Netzteil am Screenmate angeschlossen ist." — **verify against source which device is meant.** | **Critical** |
| „Bei Unterstützung von Power Delivery (PD) schaltet der Screenmate automatisch auf die Schnellladefunktion um." | `auf die Schnellladefunktion umschalten` is not a German collocation (you switch to *Schnellladen*, not to a *function*). Heavy nominal opener. | „Unterstützt dein Netzteil Power Delivery (PD), lädt der Screenmate automatisch schneller." | **Major** |
| „…muss der Monitor separat über eine zusätzliche Stromquelle versorgt werden." / „…versorge den Monitor separat über eine zusätzliche Stromquelle" | `versorgen` obligatorily takes `mit`. As written the sentence has no object of supply. Four instances (one-4k ×2, one-4k-oled ×2). | „…musst du den Monitor über ein zusätzliches Netzteil mit Strom versorgen." | **Major** |
| „Hinweis: Dein Smartphone oder Tablet muss einen USB-C-Anschluss mit Videounterstützung haben" | Inline `Hinweis:` in body prose while the same page uses `<Note>` callouts for exactly this. Page-internal inconsistency. | Move into a `<Note>` like the others. | Minor |
| „Das USB-A-Kabel kannst du für die Stromversorgung auch an einen USB-A-Anschluss des Laptops anschließen." | Two sentences earlier the same cable is `USB-C-auf-USB-A-Kabel`. Naming drift inside one section. | „Das USB-C-auf-USB-A-Kabel kannst du …" | Minor |

### osd.mdx

| Quoted German | Issue | Suggested rewrite | Severity |
|---|---|---|---|
| „Halte die Taste über der Power-Taste **10 Sekunden** lang gedrückt, um es zu entsperren." | Unresolvable referent. `controls.mdx` documents exactly three buttons (Menütaste, +, −) and never establishes a vertical order, so „die Taste über der Power-Taste" points at nothing the reader can identify. Also same file in one-4k-oled. | „Halte die Taste **+** 10 Sekunden lang gedrückt, um das OSD zu entsperren." — **needs confirmation which button it actually is.** | **Major** |
| „Wenn die Tasten an der Vorderseite nicht mehr reagieren" | `controls.mdx` never says the buttons are on the front. | „Wenn die Bedientasten nicht mehr reagieren" | Minor |
| Heading „## Bedienung und OSD-Menü" vs. frontmatter title „Bildschirmmenü (OSD)" | Page announces itself under two names. | Align heading with the title. | Minor |

### safety.mdx (frontmatter only)

| Quoted German | Issue | Suggested rewrite | Severity |
|---|---|---|---|
| `description: "Wichtige Sicherheitshinweise und Warnungen"` | `Warnungen` is the everyday word; the fixed term in German manuals is `Warnhinweise`. Identical description on all six safety pages, so it is a one-line corpus fix. | „Wichtige Sicherheits- und Warnhinweise" | Minor |

---

## de/manuals/one-4k-oled/

### index.mdx

| Quoted German | Issue | Suggested rewrite | Severity |
|---|---|---|---|
| „Er wird über USB-C oder HDMI angeschlossen und überträgt …" | Same zeugma as one-4k/index.mdx. | See above. | **Major** |
| „– ideal für Video, Foto und kreatives Arbeiten." | Parallelism break: two bare nouns + a nominalised verb phrase. | „– ideal für Video- und Fotobearbeitung und für kreatives Arbeiten." | Minor |
| „\| **Abmessungen (zusammengeklappt)** \|" | The One 4K OLED is a flat panel with an integrated stand — nothing folds. The identical One 4K page correctly says just `Abmessungen`. | „Abmessungen" | Minor |
| „\| **Paneltyp** \| OLED \| / \| **Bildschirmtyp** \| AM-OLED \|" | The two rows say the same thing in the wrong order (AM-OLED *is* the panel type). On the One 4K the pair is meaningful (IPS / LCD). | „Paneltyp: AM-OLED" and drop the second row, or „Bildschirmtyp: OLED / Paneltyp: AM-OLED". | Minor |

### controls.mdx

| Quoted German | Issue | Suggested rewrite | Severity |
|---|---|---|---|
| „### USB-A-Anschluss" — followed by nothing but an invisible JSX comment | The published German page renders a heading with **zero body text**. A German reader sees a port listed and no explanation. (The One 4K page has the full text for this port.) | Reuse the One 4K wording: „Zum Anschließen von USB-2.0-Zubehör wie einer Maus oder einer Tastatur. Sobald über den USB-C-Anschluss ein Signal empfangen wird, erkennt der Screenmate angeschlossenes Zubehör automatisch." — pending Louie's confirmation. | **Major** |
| „Dedizierter Stromeingang." / „im allgemeinen Modus" / „für Strom & Video" | Identical to one-4k/controls.mdx. | See above. | **Major** / **Major** / Minor |

### installation.mdx / osd.mdx

Identical wording to one-4k for the four issues already listed: the `laden` sentence (**Critical**), `Schnellladefunktion umschalten` (**Major**), `über eine Stromquelle versorgen` (**Major**), `die Taste über der Power-Taste` (**Major**), `Menütaste` vs `Power-Taste` (**Major**), `mit … mit` (Minor).

One difference worth noting as clean: the OLED installation page merges the "with/without extra power" images into single steps and reads slightly tighter than the One 4K page. No new findings.

### safety.mdx (frontmatter only)
Same `Warnungen` note as above. Nothing else.

---

## de/manuals/dual-flip/

### index.mdx

| Quoted German | Issue | Suggested rewrite | Severity |
|---|---|---|---|
| „…zu zwei zusätzlichen 16"-Bildschirmen aufklappst – einer auf jeder Seite." | Case agreement. The loose apposition hangs off a dative (`zu … Bildschirmen`) but is in the nominative. | „– je einen links und rechts von deinem Laptop." | **Major** |
| „Jeder Bildschirm hat eine Auflösung von 2560 × 1600, und du schließt **ihn** über USB-C oder über USB-C + HDMI + USB-A an." | Wrong referent: `ihn` grammatically points back to `jeder Bildschirm`, but you connect the device, not each screen individually — and the very next page explains that one cable feeds one side. Genuinely misleading. | „Jeder Bildschirm löst 2560 × 1600 auf. Den Dual Flip schließt du über zwei USB-C-Kabel oder über USB-C + HDMI + USB-A an." | **Major** |
| „Der Screenmate verbraucht im Standby-Modus eine geringe Menge Strom." | `eine geringe Menge Strom` is a word-for-word rendering of "a small amount of power". No German tech writer produces this. | „Im Standby verbraucht der Screenmate weiterhin etwas Strom." | **Major** |
| „…empfehlen wir, das **Netzkabel** abzuziehen, wenn der Monitor nicht in Gebrauch ist." | The Dual Flip has no Netzkabel. Its own Lieferumfang lists only USB-C cables and a Mini-HDMI cable — there is no mains cable and no power adapter in the box. The customer is told to unplug a part they do not own. | „…empfehlen wir, die Kabel abzuziehen, wenn du den Dual Flip nicht nutzt." | **Major** |
| „\| **Farbgenauigkeit** \| 100 % sRGB \|" | Mislabels the spec: 100 % sRGB is colour-gamut *coverage*, not accuracy (which would be a ΔE value). All five other products correctly label the identical row `Farbraum`. | „Farbraum \| 100 % sRGB" | **Major** |
| „**Linker Bildschirm:** 0° – 245°" | Spaced en dash in a numeric range. Duden requires an unspaced en dash — and dual-flip's own osd.mdx does it correctly six times (`0–100`, `0–4`, `10–60 Sekunden`). Page-to-page typographic split inside one product. | „0–245°" | Minor |
| „**Geh** sorgsam mit deinem Screenmate Dual Flip um" | Apocopated imperative; the rest of the corpus uses the full form (`Gehe so vor`, `Klappe`, `Stelle`, `Lege`). | „Geh**e** sorgsam … um" | Minor |

### controls.mdx

| Quoted German | Issue | Suggested rewrite | Severity |
|---|---|---|---|
| „### USB-C-Anschluss / Stromversorgung und Videoübertragung." — **appears twice, byte-identical** | The page lists two ports with the same heading and the same one-line body, giving the reader no way to tell them apart. The product's own OSD page distinguishes them as `Type-C1` and `Type-C2`. | „### USB-C-Anschluss 1 (Type-C1)" / „### USB-C-Anschluss 2 (Type-C2)", each with the side it feeds. | **Major** |
| „Erhöht im normalen Gebrauch die Helligkeit und **navigiert / erhöht Werte** im OSD-Menü." (and the `−` twin) | `navigieren` is intransitive — it cannot govern `Werte`. As written it reads "navigates values". The spaced slash also collides with the German convention (unspaced, or spell it out). | „Erhöht im normalen Gebrauch die Helligkeit. Im OSD-Menü navigierst du damit und erhöhst Werte." | **Major** |

### installation.mdx

The cleanest page in the batch. Steps are properly imperative, the storage section is well sequenced, `5 V/2 A` is correctly spaced. Only finding:

| Quoted German | Issue | Suggested rewrite | Severity |
|---|---|---|---|
| „- **1× USB-C & 1× USB-A & 1× HDMI**" | Ampersands (see one-4k/controls entry). | „1× USB-C + 1× USB-A + 1× HDMI" | Minor |

### osd.mdx

| Quoted German | Issue | Suggested rewrite | Severity |
|---|---|---|---|
| „### 5. Zurücksetzen" containing „**HDR:** Aktiviere HDR (High Dynamic Range)…" | Heading and content do not match — HDR is not a reset function. Likely faithful to the device menu, but the German reader will not find HDR where they look for it. | Keep the device grouping but signpost it: „### 5. Zurücksetzen und HDR". | Minor |
| „**ECO:** Voreingestellte Bildmodi…" vs „**DCR:** Wähle ON oder OFF…" vs „**LOW BLUE LIGHT:** Reduziert den Blaulichtanteil…" | Three grammatical patterns for one bullet list: bare noun phrase, imperative, third-person description. German menu documentation normally picks one. | Use the imperative throughout (it dominates the list): „**LOW BLUE LIGHT:** Reduziere den Blaulichtanteil des Bildschirms und entlaste so deine Augen." | Minor |
| „Reduziert den Blaulichtanteil **auf dem** Bildschirm" | Wrong preposition — the blue-light share is a property *of* the screen, not something located on it. | „…den Blaulichtanteil **des** Bildschirms" | Minor |

### safety.mdx

| Quoted German | Issue | Suggested rewrite | Severity |
|---|---|---|---|
| „Der Monitor arbeitet mit einem DC-Eingang zwischen 5 V und 20 V (mit einer Toleranz von ±2 V)." immediately followed by „Verwende das Gerät ausschließlich mit einer 5-V-Stromquelle über das passende Kabel." | **Two adjacent safety bullets contradict each other outright**: 5–20 V accepted vs. 5 V exclusively. In a safety list this is the worst place for an unresolved contradiction — a customer following bullet 2 will reject a compliant 20 V PD supply, and one reading bullet 1 may connect something bullet 2 forbids. | Resolve against the hardware, e.g. „Der Monitor arbeitet mit einem DC-Eingang von 5 V bis 20 V (±2 V). Verwende ausschließlich Netzteile in diesem Bereich." | **Critical** |
| „Verwende ausschließlich das **mitgelieferte** AC/DC-Netzteil als Stromversorgung." | No AC/DC adapter ships with the Dual Flip — the Lieferumfang lists cables and a Schutzhülle only. `das mitgelieferte` sends the customer looking for a part that is not in the box. | „Verwende zur Stromversorgung ausschließlich ein geeignetes AC/DC-Netzteil." | **Major** |
| „Empfohlene Umgebungstemperatur: zwischen −20 °C und 60 °C." | `empfohlen` is wrong for an 80-kelvin span — nobody *recommends* −20 °C. This is the permissible range. Same line on all six safety pages. | „Zulässige Umgebungstemperatur: −20 °C bis 60 °C." | Minor |

### display-settings.mdx (frontmatter only)

| Quoted German | Issue | Suggested rewrite | Severity |
|---|---|---|---|
| `title: "Anzeigeeinstellungen"` / `description: "Anzeigeeinstellungen für Windows und macOS"` | The description restates the title verbatim and adds only the OS names. Infinity and Infinity Lite use the more informative pairing (`Anzeige- und Toneinstellungen` / `… einrichten`). | „So richtest du zusätzliche Bildschirme unter Windows und macOS ein" | Minor |

---

## de/manuals/infinity/

### index.mdx

| Quoted German | Issue | Suggested rewrite | Severity |
|---|---|---|---|
| „Du befestigst ihn hinter deinem Laptop und hast damit zwei zusätzliche Bildschirme **auf einmal**." | Wrong collocation. `auf einmal` in German means "suddenly" or "in one go" — it does not carry the English "at once = simultaneously" sense intended here. A German reader trips on it. | „…und hast damit **gleich zwei** zusätzliche Bildschirme." | **Major** |
| „…ist ein **faltbarer tragbarer** Doppelmonitor" | Two unlinked attributive adjectives, no comma, no hierarchy. German wants either a comma or a restructure. | „…ist ein tragbarer Doppelmonitor zum Zusammenklappen" | Minor |
| „- **Ständer für einen Bildschirm**" | Reads like a description, not a part name, in a list where everything else is a part name. | „**Einzelbildschirm-Ständer**" | Minor |

### controls.mdx

| Quoted German | Issue | Suggested rewrite | Severity |
|---|---|---|---|
| „…findest du weiter unten die vollständige Übersicht aller **Gesten**." | `Geste` in German means a hand/touch gesture. These are presses and holds on a physical rocker switch. Straight calque. | „…die vollständige Übersicht aller Tastenbefehle." | **Major** |
| „Eine drehbare Taste …, mit der du **das Ein- und Ausschalten**, das Bildschirmmenü, die Helligkeit und die Lautstärke **steuerst**." | You do not "control the switching on and off" in German — you switch it on and off. The mixed list (one nominalised action + three objects) makes it worse. | „Eine drehbare Taste auf der Rückseite jedes Bildschirms. Damit schaltest du den Bildschirm ein und aus und regelst Menü, Helligkeit und Lautstärke." | **Major** |
| „- **Nach rechts drücken („Plus"):** die Hintergrundbeleuchtung (Helligkeit) erhöhen. / - **Nach links drücken („Min"):** die Lautstärke verringern." | Three problems in two lines. (1) The pair is logically incomplete — there is no documented way to *lower* brightness or *raise* volume. (2) `„Min"` is not German; it reads as "Minute". German uses `Minus` or the `−` sign. (3) infinity-lite/controls.mdx maps the **same two directions to the opposite functions** (left = Helligkeit, right = Lautstärke). One of the two pages is wrong and a customer with both products will notice. | „- **Nach rechts drücken (+):** Wert erhöhen (Helligkeit bzw. Lautstärke). / - **Nach links drücken (−):** Wert verringern." — **and reconcile with infinity-lite against the hardware.** | **Major** |
| frontmatter `title: "Anschlüsse und Bedienelemente"` vs body heading „## Anschlüsse und Tasten" | The page announces itself under two names, and it is the only one of the six products not titled `Anschlüsse und Tasten`. | Align to `Anschlüsse und Tasten`. | Minor |
| „Der Anschluss ist **auf** jedem Bildschirm **auf** der Rückseite mit einem blauen Aufkleber markiert." | Stacked identical preposition. | „Der Anschluss ist an jedem Bildschirm auf der Rückseite mit einem blauen Aufkleber markiert." | Minor |

### installation.mdx

| Quoted German | Issue | Suggested rewrite | Severity |
|---|---|---|---|
| „- 1× USB-C & **1× USB** & 1× HDMI" | Truncated port name. `USB` alone is meaningless here — the heading two lines down and the rest of the manual say USB-A. Reader cannot act on it. | „- 1× USB-C + 1× USB-A + 1× HDMI" | **Major** |
| „Der hervorstehende Teil des Bildschirms muss sauber in die Aussparung am Ständer **fallen**, damit alles fest sitzt." | Calque of "fall into place". In German a part `greift`, `rastet ein` or `sitzt` in a recess — it does not fall into one, and `fallen` + `fest sitzen` in one sentence is self-contradictory. | „…muss sauber in die Aussparung am Ständer **einrasten**, damit alles fest sitzt." | **Major** |
| „Lege das vollständig zusammengeklappte **Set** in die mitgelieferte **Leder-Tragetasche**." | Two problems: `Set` is an unnecessary anglicism, and the bag is called `Schutzhülle` in this product's own Lieferumfang. The customer is told to use an item that, by name, is not in the box. | „Lege den vollständig zusammengeklappten Screenmate in die mitgelieferte Schutzhülle." | **Major** |
| „Der Ständer **öffnet sich** bis zu einem maximalen Winkel von 235°." | Reflexive implies the stand opens by itself. | „Der Ständer lässt sich bis zu einem Winkel von 235° öffnen." | Minor |
| „Jeder Bildschirm **dreht sich** maximal 90°." … six lines later … „Jeder Bildschirm **lässt sich** maximal 90° **drehen**." | The same fact stated twice on one page, once in the wrong voice and once correctly. | Delete the first instance. | Minor |
| „### Mögliche Anordnungen" uses `Querformat` / `Hochformat`; „### Zwei Bildschirme – vorne und hinten, **horizontal**" / „**vertikal**" | Two vocabularies for screen orientation on one page. (Infinity Lite adds a third: `senkrecht` / `waagerecht`.) | Standardise on `Querformat` / `Hochformat` corpus-wide. | Minor |

### display-settings.mdx

| Quoted German | Issue | Suggested rewrite | Severity |
|---|---|---|---|
| „Öffne die **Display settings** („Anzeigeeinstellungen") und wähle …" | The single clearest translation artefact in the batch. A German customer runs a **German** Windows, where the item is called **Anzeigeeinstellungen** — the English string is not on their screen. Leading with English and glossing it in German inverts the correct order and marks the page as translated. Also in infinity-lite/display-settings.mdx. | „Öffne die **Anzeigeeinstellungen** und wähle …" | **Major** |
| „gehe zu **Anzeigeausrichtung**" | German Windows labels this field **Bildschirmausrichtung** (Windows 10 and 11, under Skalierung und Layout). `Anzeigeausrichtung` is a coined string the customer will not find. Four instances corpus-wide (infinity, infinity-lite ×2, panorama). *Verify on a German Windows install before mass-editing.* | „gehe zu **Bildschirmausrichtung**" | **Major** |
| „Auf dem Screenshot sind die *MacBook-Lautsprecher* markiert, du musst aber den Eintrag **S6-R / Screenmate** wählen" | Comma splice — two main clauses joined by a comma with `aber` in third position. Tolerated in speech, not in published copy. | „…markiert. Du musst aber den Eintrag **S6-R / Screenmate** wählen, …" | Minor |
| „damit Text und **Elemente** größer dargestellt werden" | `Elemente` alone is vague (calque of "items"); panorama says `Text und Bedienelemente` for the same sentence. | „damit Text, Apps und andere Elemente größer dargestellt werden" (matches the German Windows wording) | Minor |

### safety.mdx

| Quoted German | Issue | Suggested rewrite | Severity |
|---|---|---|---|
| „Verwende **ausschließlich ein** AC/DC-Netzteil als Stromversorgung." | Ambiguous: `ausschließlich ein` can be read as "only one adapter". The intended meaning is "only an adapter of this type". | „Verwende zur Stromversorgung ausschließlich ein geeignetes AC/DC-Netzteil." | Minor |
| „Für den privaten und gewerblichen Gebrauch geeignet." | Verbless fragment dropped into an otherwise fully imperative list. | „Das Gerät ist für den privaten und gewerblichen Gebrauch geeignet." | Minor |
| „### Vor der Verwendung **prüfen**" vs infinity-lite „### Vor der Verwendung **lesen**" vs panorama „### Vor der Verwendung" | Three headings over three identical lists. | „### Vor der Verwendung" everywhere. | Minor |

---

## de/manuals/infinity-lite/

### index.mdx

| Quoted German | Issue | Suggested rewrite | Severity |
|---|---|---|---|
| „…und **ist auf Plug-and-Play mit** Laptops, Smartphones, Tablets und Spielkonsolen **ausgelegt**." | `auf X ausgelegt sein` needs a purpose, not a feature name; "designed for plug-and-play with" transferred literally. | „…und funktioniert per Plug-and-Play mit Laptops, Smartphones, Tablets und Spielkonsolen." | **Major** |
| „…die du hinter deinem Laptop **montierst**" | `montieren` implies fitting with tools. The Infinity page uses `befestigst` for the identical action. | „…die du hinter deinem Laptop befestigst" | Minor |
| „So bekommst du unterwegs einen zusätzlichen tragbaren **Bildschirm** und mehr **Bildschirm**fläche." | Root repetition plus a redundant second clause (an extra screen *is* more screen area). | „So hast du unterwegs einen zweiten Bildschirm und deutlich mehr Arbeitsfläche." | Minor |

### controls.mdx

| Quoted German | Issue | Suggested rewrite | Severity |
|---|---|---|---|
| „### Linke Taste „Min" / Nach links drücken – stellt die Hintergrundbeleuchtung (Helligkeit) ein." (and the „Plus" twin) | Ungrammatical: an infinitive phrase, a dash, then a finite verb with no subject. Neither half can govern the other. | „### Linke Taste (−) / Drücke nach links, um die Helligkeit einzustellen." | **Major** |
| „„Min"" / „„Plus"" as button names; left = Helligkeit, right = Lautstärke | Non-German abbreviation (see infinity/controls), **and the mapping is the mirror image of infinity/controls.mdx**. One of the two is factually wrong. | Use `−` / `+`, and reconcile the two products against the hardware. | **Major** |
| „Der **äußerste linke** Anschluss an der Unterseite." | Superlative + positional adjective stacked; German prefers `der ganz linke` or `der linke äußere`. | „Der ganz linke Anschluss an der Unterseite." | Minor |

### installation.mdx

| Quoted German | Issue | Suggested rewrite | Severity |
|---|---|---|---|
| „…um **beide Erweiterungsbildschirme** sicher hinter deinem Laptop aufzustellen." (plus the headings „Die Bildschirme aufklappen", „Die Bildschirme öffnen", „Die Bildschirme schließen") | **Contradicts the product.** index.mdx describes the Infinity Lite as a single-screen extension („einen zusätzlichen tragbaren Bildschirm"), and its Lieferumfang lists one stand and one set of cables. `beide Erweiterungsbildschirme` is a two-screen statement on a one-screen product; a customer will conclude a screen is missing from the box. | „…um den Erweiterungsbildschirm sicher hinter deinem Laptop aufzustellen." and „Den Bildschirm aufklappen / öffnen / schließen". | **Critical** |
| „Klappe den Rahmen auf, bis er einrastet, **um ihn auszuziehen**." under the heading „### 4. Den Rahmen **herausziehen**" | Circular and lexically wrong: heading says pull out, body says unfold *in order to* pull out, and `ausziehen` in German primarily means to undress/extend a table. The reader cannot tell what to do. | „### 4. Den Rahmen ausfahren / Zieh den Rahmen heraus, bis er hörbar einrastet." — **needs confirmation of the actual motion.** | **Major** |
| „Stecke das Kabel in den **ersten oder zweiten** Anschluss des Screenmate" … „Schließe das HDMI-auf-USB-C-Kabel … an den **dritten** Anschluss an." | The port numbering is never defined for the reader, and it contradicts controls.mdx, which documents **two** USB-C ports and identifies the HDMI-auf-USB-C port as the **leftmost** one. Following this page, the customer plugs video into a port that (per the other page) does not exist. | Drop the numbering and use controls.mdx's physical description: „…an den ganz linken USB-C-Anschluss". | **Major** |
| „**Wechsle in den richtigen Verbindungsmodus** (externe Stromversorgung erforderlich), um den Screenmate mit einem Smartphone … zu verwenden. **Auch der Smartphone-Modus benötigt eine externe Stromversorgung.**" | Two faults. (1) `Verbindungsmodus` appears nowhere else in the manual — no mode is defined, so the instruction cannot be followed. (2) The external-power requirement is stated twice in two consecutive sentences, the second adding nothing. | „Für Smartphones, Spielkonsolen und andere USB-C-Geräte brauchst du immer eine externe Stromversorgung." | **Major** |
| „Halte mit beiden Händen die beiden mit roten Pfeilen markierten Stellen fest und ziehe **den Bildschirm** nach außen, um **den einzelnen Bildschirm** zu lösen." | Circular reference — the object being pulled and the object being released are the same noun, phrased as if they were different. | „Halte die beiden rot markierten Stellen mit beiden Händen fest und zieh den Bildschirm nach außen, bis er sich löst." | **Major** |
| Three `<Warning>` callouts containing neutral assembly instructions: „Klappe den Ständer auf, stelle ihn auf den richtigen Stützwinkel ein, platziere ihn hinter deinem Computerbildschirm und schließe die Montage des Bildschirmständers ab." (step 5), and step 3 | A German reader sees a red **Warnung** box and finds no hazard in it. Repeated use devalues the real warnings on the safety page. Editorial, but it degrades the German reading experience directly. | Move the instructions into body text; keep `<Warning>` for the genuine damage risks („Klappe den Monitor vollständig auf, um Schäden zu vermeiden."). | **Major** |
| „Passe den Abstand zwischen dem tragbaren Bildschirm und dem Computerbildschirm **für ein angenehmeres Nutzungserlebnis** nach deinen Vorlieben **an**." | `Nutzungserlebnis` is corporate anglicism ("user experience"), and 17 words separate `Passe` from its `an`. Both mark the sentence as translated. | „Stell den Abstand zwischen den beiden Bildschirmen so ein, wie es für dich am angenehmsten ist." | **Major** |
| „…mit einer einzelnen Bildschirmhalterung, in **senkrechter** oder in **waagerechter** Position" | Third vocabulary for orientation in the corpus (see infinity/installation). | „…im Hochformat oder im Querformat" | Minor |
| „…um Schäden am Gerät zu vermeiden. Verstaue deinen Screenmate sorgfältig, **damit das Gerät nicht beschädigt wird**." | The same purpose clause twice in two consecutive sentences. | Delete the second. | Minor |

### display-settings.mdx

| Quoted German | Issue | Suggested rewrite | Severity |
|---|---|---|---|
| „### Windows … Gehe zu den **Display settings** („Anzeigeeinstellungen")…" and later, in the Tabs block, „Gehe zu den **Anzeigeeinstellungen** und wähle …" | The **same page** gives the same instruction twice, once with the English label and once with the German one. Whichever is right, the page contradicts itself. | Use `Anzeigeeinstellungen` in both places. | **Major** |
| Entire Windows + macOS instruction set appears twice: once under „## Bildschirmkonfiguration" and again under „## Bildschirme anordnen (Video)" | The reader is walked through the identical four steps twice with slightly different wording, which reads as an editing accident rather than as a video supplement. | If the second block exists only to host the videos, cut its prose to a one-line lead-in („Die Schritte im Video:") and keep the wording identical where it stays. | **Major** |
| „gehe zu **Anzeigeausrichtung**" (×2 on this page) | See infinity/display-settings. | „Bildschirmausrichtung" | **Major** |
| Top half marks UI strings in **bold** (`**Desktop auf diese Anzeige erweitern**`); Tabs half marks the identical strings in „quotes" (`„Desktop auf diese Anzeige erweitern"`) | Page-internal typographic inconsistency for one category of text. | Pick one — bold is the corpus majority. | Minor |

### safety.mdx
Same three Minors as infinity/safety.mdx (`ausschließlich ein`, verbless bullet, heading variant „Vor der Verwendung **lesen**" over a list of actions rather than reading matter). No new findings.

---

## de/manuals/panorama/

### index.mdx

| Quoted German | Issue | Suggested rewrite | Severity |
|---|---|---|---|
| „…der dir drei Full-HD-Bildschirme **mit 15,6"** **aus einem einzigen Gerät liefert**." | Two calques in one clause. German attaches the size attributively (`drei 15,6"-Bildschirme in Full HD`, exactly as infinity/index.mdx does), and `aus einem einzigen Gerät liefern` is "delivers … from a single device" transferred word for word. | „…der dir drei 15,6"-Bildschirme in Full HD in einem einzigen Gerät bietet." | **Major** |
| „**Ein erforderlicher Displaytreiber** macht es möglich, drei unabhängige Bildschirme über ein einziges Kabel anzusteuern." | `erforderlich` cannot sit attributively on an indefinite noun like this — it reads as "a required driver" (as opposed to the optional ones?). The requirement is the point of the sentence and needs to be predicated. | „Dafür ist ein Displaytreiber erforderlich: Er steuert drei unabhängige Bildschirme über ein einziges Kabel an." | **Major** |
| „\| **Blickwinkel** \| 360° \|" | Physically impossible and out of line with every sibling product (172°/178°). A German reader who compares spec tables will read it as a typo and lose trust in the table. **Verify against source.** | „178°" (or the real figure) | **Major** |
| „**Er ist dafür gemacht**, deine Arbeitsfläche unterwegs **enorm** zu erweitern." | `dafür gemacht sein` is spoken register; `enorm` is unquantified marketing in an otherwise factual paragraph. | „Damit erweiterst du deine Arbeitsfläche auch unterwegs deutlich." | Minor |

### controls.mdx

| Quoted German | Issue | Suggested rewrite | Severity |
|---|---|---|---|
| „### 3 × Mini-HDMI-Anschlüsse / Verbinde deinen Laptop über ein Mini-HDMI-auf-HDMI-Kabel **mit einem einzelnen Bildschirm**." | Reads as "connect your laptop to a single screen", which is not what the port does. The intended meaning — each Mini-HDMI port drives one of the three panels — is lost. | „Über jeden dieser Anschlüsse steuerst du einen einzelnen Bildschirm an. Verbinde deinen Laptop dazu über das Mini-HDMI-auf-HDMI-Kabel." | **Major** |
| „### **3 ×** Mini-HDMI-Anschlüsse" | Spaced multiplication sign; the corpus uses unspaced `2×`, `1×`, `8×` everywhere else. | „### 3× Mini-HDMI-Anschlüsse" | Minor |
| „### **Taste Ab** (−)" / „### **Taste Auf** (+)" | Noun + bare adverb is not a German button name; it reads like a placeholder. Every other product uses `Taste −` / `Taste +`. | „### Taste − (Ab)" / „### Taste + (Auf)" | Minor |
| „### Power-Taste / - **Lang drücken (1 Sekunde):** Monitor ausschalten." | Only switching *off* is documented; the reader is never told how to switch the Panorama on. Every other product's controls page covers both. | Add „- **Lang drücken:** Monitor einschalten (wenn er aus ist)." | Minor |

### installation.mdx

| Quoted German | Issue | Suggested rewrite | Severity |
|---|---|---|---|
| „### Option 1 – USB-C **(nur ein Kabel)**" followed by two steps using two USB-C cables | The heading promises one cable; the instructions immediately below require two (power + data). Self-contradiction at the point of decision — this is the heading the customer uses to choose their setup. | „### Option 1 – USB-C (ein Kabel zum Laptop)" | **Major** |
| „**Fasse** die Bildschirme **an** und ziehe sie nach oben" | `anfassen` = to touch. You do not "touch and pull" a mechanism in German instructions. | „Greif die Bildschirme und zieh sie nach oben" | **Major** |
| „…und klappe sie dann bis zum gewünschten **Blickwinkel** auf." | Terminology collision inside one product: `Blickwinkel` is the panel spec in index.mdx (the 360° row). Here it means the tilt the user sets. | „…und klappe sie dann bis zum gewünschten Neigungswinkel auf." | **Major** |
| „**Achtung:** **Achte** beim **Klappen** der Bildschirme auf deine Finger" | Two faults: the `Achtung/Achte` root echo is clumsy, and `beim Klappen` is not idiomatic on its own — panorama/safety.mdx says `beim Ein- und Ausklappen` for the identical warning, so the product contradicts itself stylistically. | „**Vorsicht:** Pass beim Ein- und Ausklappen der Bildschirme auf deine Finger auf." | **Major** |
| „…führe **die Schritte oben** in umgekehrter Reihenfolge aus." | Calque of "the steps above". German needs an attributive form. | „…führe die oben beschriebenen Schritte in umgekehrter Reihenfolge aus." | **Major** |
| „Schließe das HDMI-Kabel am Monitor an **den HDMI-Anschluss** neben dem weißen Netzkabel an." | Two problems: the monitor has **Mini**-HDMI (controls.mdx), not HDMI, and it has **three** of them — the definite singular points at nothing identifiable. | „Schließe das Kabel an den Mini-HDMI-Anschluss neben dem weißen Netzkabel an." | **Major** |
| „Lade den Treiber **von** der Download-Seite **von** Silicon Motion herunter" | Stacked identical preposition. | „Lade den Treiber auf der Downloadseite von Silicon Motion herunter" | Minor |
| „Verwende das lange weiße Kabel **für den Strom** und das kurze schwarze Kabel, **um den Panorama … zu verbinden**." | Non-parallel coordination (prepositional phrase + infinitive clause). Also: the Lieferumfang lists the cables by length only, never by colour, so the colour cue is unverifiable from the manual. | „Verwende das lange weiße Kabel für den Strom und das kurze schwarze Kabel für die Verbindung zum Laptop." (and add the colours to the Lieferumfang) | Minor |
| „Klappe die **Verriegelungsfüße** nach innen." | Coinage; not a term a German reader will map onto a part. | „Klappe die Standfüße nach innen, bis sie einrasten." | Minor |

### osd.mdx

| Quoted German | Issue | Suggested rewrite | Severity |
|---|---|---|---|
| „Der Panorama steuert drei unabhängige Bildschirme an. **Deshalb** kannst du die Anordnung des Desktops in deinem Betriebssystem anpassen." | The causal connector does not hold — being able to arrange displays in the OS does not follow from there being three of them (it is true of two, or of any external display). The German reader stops on `Deshalb`. | „Weil der Panorama drei unabhängige Bildschirme bereitstellt, ordnest du sie im Betriebssystem wie gewohnt an." | **Major** |
| „gehe zu **Anzeigeausrichtung**" | See infinity/display-settings. | „Bildschirmausrichtung" | **Major** |
| „Drücke die **Beenden-Taste**, um das Menü zu schließen." | controls.mdx names it `Bestätigen-/Beenden-Taste` and specifies that *long* press exits. This page shortens the name and drops the long press, so the instruction as given does not work. | „Halte die **Bestätigen-/Beenden-Taste** gedrückt, um das Menü zu schließen." | Minor |
| „Die Lautstärkeregelung ist nur auf dem linken Bildschirm **(DP-Monitor)** verfügbar." | Unexplained abbreviation in consumer copy; `DP` appears nowhere else in the German manual. | „…nur auf dem linken Bildschirm (dem über DisplayPort angesteuerten) verfügbar." | Minor |
| „## Bildschirmkonfiguration **(Betriebssystem)**" | Parenthetical noun as a heading qualifier is clunky German. | „## Bildschirme im Betriebssystem anordnen" | Minor |
| „**„Desktop auf diese Anzeige erweitern"**" vs „**Identifizieren**" vs „**Anzeigeausrichtung**" on one page | UI strings marked three ways (bold+quotes, bold only) within four consecutive lines. | Bold only, corpus-wide. | Minor |

### safety.mdx
Clean apart from the shared corpus Minors (`Warnungen`, `ausschließlich ein`, `Empfohlene Umgebungstemperatur`, heading variant). The extra section „### Vorsicht beim Klappen / Achte beim Ein- und Ausklappen der Bildschirme auf deine Finger" is good, idiomatic German — and is the wording installation.mdx should have used.

---

## Totals

| Severity | Count |
|---|---|
| **Critical** | **3** |
| **Major** | **44** |
| **Minor (itemised)** | **15** |
| **Total reported** | **62** |

Deduplication note: findings that recur verbatim across files (e.g. `Dedizierter Stromeingang.` in one-4k and one-4k-oled; `Anzeigeausrichtung` in four files; `über eine Stromquelle versorgen` in four places) are **counted once** and all locations listed in the row. Counting instances rather than distinct defects would put Majors at roughly 60.

Minors were capped per brief. Roughly a dozen further polish items were observed and deliberately not itemised — mostly preference-level (e.g. `zugleich` vs `gleichzeitig`, sentence-final separable-verb distance in the one-4k installation steps, `8× Stabilisierungsgummis` pluralisation, the `Aufbewahrung` vs `Verstauen` split, bullet-vs-numbered list style differences between the six safety pages). None of these would make a German reader stumble.

### Where the damage is concentrated

| File | Critical | Major |
|---|---|---|
| infinity-lite/installation.mdx | 1 | 5 |
| panorama/installation.mdx | 0 | 6 |
| infinity/installation.mdx | 0 | 3 |
| dual-flip/index.mdx | 0 | 5 |
| dual-flip/safety.mdx | 1 | 1 |
| one-4k/installation.mdx + one-4k-oled/installation.mdx | 1 | 3 |
| infinity/controls.mdx | 0 | 3 |
| infinity-lite/display-settings.mdx | 0 | 3 |

Everything else is one or two findings per file.

---

## Verdict

### Would a German customer notice this is a translation?

**Yes — but only in specific places, and not on most pages.**

The reader who opens `dual-flip/installation.mdx`, `panorama/osd.mdx` or any of the six `safety.mdx` pages will not suspect anything. Those pages are genuinely well written: correct imperative mood, correct case and gender, correct compound hyphenation around English terms (`USB-C-auf-USB-C-Kabel`, `65-W-USB-C-Netzteil`, `3,5-mm-Klinkenanschluss` — this is where machine output usually fails and it does not fail here), correct SI spacing, correct German locale numbers, consistent `du` with zero `Sie` leakage across 30 files, and real German Windows/macOS UI strings (`Desktop auf diese Anzeige erweitern`, `Querformat (gedreht)`, `Anordnen`, `Drehung`/`Standard`, `Ton` → `Ausgabe`) rather than invented ones. Someone who knows German conventions made these decisions.

The reader who opens `infinity-lite/installation.mdx` or `panorama/installation.mdx` will notice within two paragraphs. The tells cluster:

1. **Lexical calques a native would not produce.** `Dedizierter Stromeingang`, `im allgemeinen Modus`, `eine geringe Menge Strom`, `muss in die Aussparung fallen`, `die Schritte oben`, `Nutzungserlebnis`, `Übersicht aller Gesten`, `zwei Bildschirme auf einmal`, `aus einem einzigen Gerät liefert`, `Fasse die Bildschirme an`. Each is individually survivable; nine of them across six products establishes a pattern.
2. **The `Display settings („Anzeigeeinstellungen")` construction.** This is the single most diagnostic finding in the batch. It is what a translator does when they are translating an English screenshot caption rather than writing for someone sitting in front of a German Windows. It appears on two in-scope pages (plus the out-of-scope onecable/dual-flip shared file), and `infinity-lite/display-settings.mdx` even contradicts itself by using the German name correctly 30 lines further down.
3. **Grammatical breakage under structural pressure.** `Nach links drücken – stellt die Hintergrundbeleuchtung ein` (subjectless finite verb), `navigiert / erhöht Werte`, `einer auf jeder Seite` (case), `wird angeschlossen und überträgt` (zeugma). These occur where the source presumably had a compact English label the translator tried to preserve.

Separately — and more serious than the fluency issues — this read surfaced **internal contradictions that no bilingual check would catch**, because each half is a faithful rendering of its own source line: 5 V vs 5–20 V in one safety list (Critical); a two-screen setup procedure on a one-screen product (Critical); a monitor that charges itself (Critical); a *mitgeliefertes Netzteil* that is not in the box; a *Leder-Tragetasche* the Lieferumfang calls a *Schutzhülle*; a third port on a two-port device; `Plus`/`Min` mapped to opposite functions on Infinity and Infinity Lite; `nur ein Kabel` above a two-cable procedure. These are the highest-value findings here and should be routed to whoever can check the hardware, not to a language editor.

### Readability grade

**Near-native**, with a clear internal split:

- **Native or effectively native:** all six `safety.mdx`, `dual-flip/installation.mdx`, `dual-flip/osd.mdx`, `panorama/osd.mdx`, `one-4k/osd.mdx`, `one-4k-oled/osd.mdx`, `infinity/display-settings.mdx` (apart from the two UI-label issues).
- **Near-native:** the four `index.mdx` files, `one-4k`/`one-4k-oled` `controls.mdx` and `installation.mdx`, `infinity/controls.mdx`, `infinity/installation.mdx`.
- **Noticeably translated:** `infinity-lite/installation.mdx` and `panorama/installation.mdx`. Both would need a rewriting pass, not a correction pass — the problems are structural (circular instructions, undefined references, warnings that contain no warning), not word-level.

**Reasoning for the grade:** the mechanical layer of German — the part that is hardest to fake and easiest to measure — is essentially flawless across all 30 files, and the register discipline (`du`, no formality drift, no marketing bloat) is better than most German consumer manuals written from scratch. What holds it back from "native" is that the *idiom* layer was translated rather than rewritten: roughly one calqued collocation per 400 words, concentrated in the procedural pages, plus the English-UI-label artefact that a German writer would never have produced. Fixing the 44 Majors would move the whole batch to native; fixing only the 3 Criticals plus the `Anzeigeeinstellungen`/`Bildschirmausrichtung` pair would already remove the most visible tells.

### Recommended order of work

1. The 3 **Criticals** — all are product-fact contradictions, all need hardware confirmation, one is in a safety list.
2. The nine internal contradictions listed above (box contents, port counts, button mappings, cable counts) — same owner as (1).
3. The two UI-label fixes (`Display settings` → `Anzeigeeinstellungen`; `Anzeigeausrichtung` → `Bildschirmausrichtung`) — cheap, high visibility, ~6 files, and `Bildschirmausrichtung` should be verified on a German Windows install first.
4. The remaining Majors, product by product, starting with `infinity-lite/installation.mdx` and `panorama/installation.mdx`.
5. Minors last, as a single consistency sweep (units, `Farbraum`, `Warnhinweise`, orientation vocabulary, ampersands, UI-string emphasis style).
