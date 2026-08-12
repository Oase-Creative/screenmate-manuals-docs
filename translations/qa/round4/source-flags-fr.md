# Round 4 — EN/NL source defects surfaced by the French fluency review

**Date:** 2026-08-12 · **Branch:** `round4-fixes` · **Author:** FR translator-editor pass

Every item below was raised as a French defect by `fluency-fr-a.md`, `fluency-fr-b.md` or
`safety-align-fr.md`. In each case the French was checked line-by-line against its `en/`
counterpart and found **faithful**: the same wrong, vague or self-contradictory statement is present
in the English source (and, where noted, in the Dutch origin). **The French was not changed.**
Fixing these means fixing `en/` — and, for the product-fact items, getting a ruling from the client.

Severity is the reviewer's rating of how the defect lands on a French reader, not a judgement of the
translation.

---

## A · Safety-relevant — highest priority for a client ruling

| # | Where (FR = EN) | The problem | Severity |
|---|---|---|---|
| **S1** | `*/safety.mdx` items 5 & 6 — Group A ×7 (`onecable`, `lite`, `lite-144hz`, `flip`, `expand`, `one-4k`, `one-4k-oled`) + `dual-flip` | EN item 5: *"The monitor operates on a DC input **between 5V and 20V** (with a tolerance of ±2V)."* EN item 6: *"**Only** use the device with a **5V** power source via the appropriate cable."* Item 6 forbids most of the range item 5 permits. FR mirrors both exactly (`entre 5&nbsp;V et 20&nbsp;V` / `uniquement avec une source d'alimentation de 5&nbsp;V`), so a French customer holding a 20 V USB-C PD charger cannot tell which instruction binds. **Already logged as E1 in `safety-align-fr.md`; re-raised independently by both fluency reviewers as the corpus's only Critical.** | **Critical** |
| **S2** | `onecable/troubleshooting.mdx`, first FAQ answer | EN: *"Check if the **motherboard indicator light** is on."* There is no user-visible motherboard LED on a sealed portable monitor, so the very first troubleshooting step is unactionable in every language. FR is faithful (`le voyant de la carte mère`) and the rendering is glossary-locked (§5.1). Needs a client answer: **which LED is meant?** | Major |

---

## B · Product-fact contradictions — need hardware confirmation, not a translation fix

| # | Where (FR = EN) | The problem | Severity |
|---|---|---|---|
| **P1** | `infinity/controls.mdx` | EN documents only two of four actions: *"Press right ("Plus"): increase the backlight (brightness)"* / *"Press left ("Min"): decrease the volume."* As written there is no way to lower brightness or raise volume. `infinity-lite/controls.mdx` documents the **opposite** mapping for the same control family (left = backlight, right = volume) — also faithfully. Inventing a French mapping would fabricate product behaviour, so nothing was changed. | **Critical** |
| **P2** | `infinity/controls.mdx`, `infinity-lite/controls.mdx` | The button labels **"Min"** and **"Plus"** come from the EN source (`### Left "Min" Button`, `**Press left ("Min"):**`) and are Dutch (`min` = *moins*). A French reader parses `Min` as *minimum*, not as the minus direction. FR renders them verbatim per glossary §9.4 / §10.2 locks. If the physical buttons are engraved `−` / `+`, **EN should say so** and all four languages follow. | Major |
| **P3** | `lite/controls.mdx`, `lite-144hz/controls.mdx`, and the matching `osd.mdx` pages | EN gives the power-on/off gesture to the **Scroll Wheel** (*"Short press: turn the device on"*) while the control named **Power & Return Button** only opens the OSD. Read in any language, the button called "power" never powers anything. FR is faithful and both names are glossary-locked. | Major |
| **P4** | `infinity-lite/installation.mdx` | EN: *"Follow these steps in order to safely deploy **both extension screens** behind your laptop"*, with headings *"Unfolding the Screens" / "Open the screens" / "Close the screens"* — on a product `index.mdx` and `controls.mdx` both describe as a **single** screen (*"one extra portable display"*, one panel, one speaker). FR mirrors the plural exactly. Singularising the French alone would silently diverge from `en/`, `de/`, `it/` and `nl/`. | **Critical** |
| **P5** | `infinity-lite/installation.mdx` vs `infinity-lite/controls.mdx` | EN numbers the same port two ways: installation says *"the **third** port of the Screenmate"* (and *"the first or second port"* for power), controls says *"The **leftmost** bottom port"*. The customer cannot map either instruction onto the hardware. FR faithful. | Major |
| **P6** | `infinity-lite/installation.mdx`, last section | EN: *"**Switch to the correct connection mode** (external power required) … Phone mode also requires external power."* No page on this product documents a mode switch, and the second sentence repeats the parenthesis of the first. FR faithful. | Major |
| **P7** | `panorama/index.mdx` spec table | EN states **Viewing Angle | 360°**, which is physically meaningless for an LCD; sibling products state 172°/178°. FR faithful (`Angle de vision | 360°`). | Minor |
| **P8** | `dual-flip/index.mdx`, `flip/index.mdx` rotation callout | EN: *"**Left** screen: 0° – 245° (**180° tiltable** up and down)"* / *"**Right** screen: 0° – 205° (tilts up and down, **just like the left screen**)"*. Neither parenthetical parses against its own range, and the right-hand note claims parity right after quoting a different maximum. FR faithful. | Major |
| **P9** | `one-4k/installation.mdx`, `one-4k-oled/installation.mdx` | EN: *"If your device supports charging over USB-C, **the screen** automatically charges…"* — tells the customer the monitor has a battery, which nothing else in the manual supports. The referent is probably *the device*. FR keeps EN's referent (`l'écran se recharge`); changing it would be a unilateral product-fact decision. *(The separate cacophony `prend en charge la charge` **was** fixed — see the fixlog.)* | Major |

---

## C · Headings and labels that document the wrong thing

| # | Where (FR = EN) | The problem | Severity |
|---|---|---|---|
| **H1** | `onecable/installation.mdx` | EN heading *"## Charging the Screenmate OneCable"* sits over a section that ends *"Your **laptop** is now being charged via the Screenmate"* — the section documents reverse charging, i.e. charging the laptop, not the monitor. A reader scanning the TOC for "how do I charge my monitor" is sent to the wrong place. FR is faithful and the heading is glossary-locked (§9.3). | Major |
| **H2** | `onecable/index.mdx`, `lite/index.mdx`, `lite-144hz/index.mdx`, `dual-flip/index.mdx` | EN labels a **% sRGB / % NTSC** figure as **Color Accuracy**. That figure is gamut coverage, not accuracy (ΔE). The correct EN field name is *Color Gamut*, which the same corpus uses elsewhere. FR renders both per the §5.6 lock (`Précision des couleurs` / `Gamme de couleurs`). | Major |
| **H3** | `flip/index.mdx`, `expand/index.mdx` | The **same spec row** carries a different EN label in each tab of one page — flip: 14" = *Color Gamut*, 15.6" = *Color Accuracy*; expand: the split runs the **opposite** way. The reader watches the label change as they toggle tabs. FR mirrors the split faithfully in both directions; harmonising the French alone would hide an EN defect. | Major |
| **H4** | `flip/installation.mdx` | Two parallel size headings give contradictory instructions: EN *"### Flip 14" — First check which ports **the Screenmate** has."* vs *"### Flip 15.6" — First check which ports **your laptop** has."* Nothing explains why the two sizes would differ. FR faithful. | Major |
| **H5** | `flip/installation.mdx`, first line | EN *"first check which **ports are involved**"* — involved in what? The reader cannot tell whether to look at the monitor or the laptop, which is exactly what the sentence exists to say. FR faithful (`quels ports sont concernés`). | Major |
| **H6** | `expand/index.mdx` vs `expand/installation.mdx` | The box list says **"6x protective clips"**; the installation page tells you to fit the **"Protective Cap"**. Two names, and a customer with the open box cannot tell whether they are the same part. Both FR renderings are §5.7/§9.3-locked. | Major |
| **H7** | `infinity/index.mdx` vs `infinity/installation.mdx` | Box list says **"Protective case"**; the storage step says *"Place the fully folded unit in the supplied **leather carry pouch**"* — a different name **and** a different material for an item that must be found in the box. Both FR renderings are §5.1/§5.7-locked. | Major |
| **H8** | `expand/installation.mdx` step 3 | EN: *"make sure it grips firmly **so your screen is clamped tightly**"* — instructs the customer to clamp their laptop lid tight. Alarming in any language and a genuine over-tightening risk. FR faithful (`de sorte que votre écran soit bien serré`). | Major |
| **H9** | `dual-flip/controls.mdx` | Two consecutive `### USB-C Port` headings with a byte-identical one-line description, so the reader has no way to tell the two ports apart — the entire purpose of a ports page. FR faithful; disambiguating in French only would break heading parity with `en/`. | Major |
| **H10** | `dual-flip/osd.mdx` | **HDR** is documented under the heading *"### 5. Reset"*. FR faithful (`### 5. Réinitialisation`); moving it is a structural change. | Minor |
| **H11** | `infinity/index.mdx` vs `infinity/controls.mdx` | EN says **"built-in speakers"** (plural) on one page and **"a built-in speaker"** (singular) on the next, for the same hardware. FR mirrors both. | Major |
| **H12** | `panorama/controls.mdx` | The page documents how to switch the monitor **off** (*"Long press (1 second): Switch the monitor off"*) but never how to switch it **on**. FR faithful. | Minor |

---

## D · Style and register defects inherited from EN

| # | Where (FR = EN) | The problem | Severity |
|---|---|---|---|
| **D1** | `onecable/troubleshooting.mdx`, last FAQ | EN announces a list with a colon (*"This is possible, provided the following conditions are met:"*) and then runs three flat sentences together in one paragraph instead of bulleting them. FR faithful; adding bullets in French only would break list parity. | Major |
| **D2** | `onecable/installation.mdx` | A standalone one-word paragraph **"Or"** (FR `Ou`). Layout artefact, present in EN. | Minor |
| **D3** | `onecable/installation-windows.mdx` | `alt="Driver Installation Windows - **Day Mode**"` / `"- **Night Mode**"` — internal day/night asset vocabulary leaked into user-visible alt text, in EN. A French screen-reader user hears `mode jour`, which describes nothing. FR faithful. | Minor |
| **D4** | `onecable/installation-mac.mdx` | Three names for one machine on one page, in EN: *"your **MacBook**"*, *"restart your **Mac**"*, *"restart your **laptop**"* — and the Mac-only fallback list is the one that says "laptop". FR faithful. | Minor |
| **D5** | `onecable/controls.mdx` | Three names for one port in EN: *"the Power port"*, *"the Power USB-C port"*, *"USB-C Port (Power Only / Power Delivery)"*. FR faithful. | Minor |
| **D6** | `lite/osd.mdx`, `lite-144hz/osd.mdx` | EN: *"**Color Temperature:** Choose User, Warm, or Cool to adjust the overall **color intensity**."* Colour temperature adjusts warmth/tone, not intensity — a reader who follows it looks for the wrong effect. FR faithful (`l'intensité globale des couleurs`). | Major |
| **D7** | `lite/osd.mdx`, `lite-144hz/osd.mdx` | EN: *"**Transparency (0–100):** Adjust the transparency of the OSD menu **for a better view**."* "A better view" of what? Raising transparency makes the *menu* less visible. FR inherits the ambiguity as `pour une meilleure visibilité`, which a French reader will read as "so the menu is more visible" — the opposite. Cannot be fixed in FR without inventing the referent EN withholds. | Minor |
| **D8** | `lite/osd.mdx`, `lite-144hz/osd.mdx` | EN: *"Adjust the brightness of the **red RGB value**."* A three-noun stack; `expand/osd.mdx` says *"Adjust the red channel"* for the identical setting. FR mirrors both EN forms. | Minor |
| **D9** | `flip/osd.mdx`, `expand/osd.mdx` | EN: *"**Source (SOURCE):** Pick from two signal sources: Type-C1 / Type-C2 and HDMI."* — announces two, then prints three tokens. (Defensible if `Type-C1 / Type-C2` counts as one slash-grouped source, which is how FR reads it.) `dual-flip/osd.mdx` says **three** for the same menu. FR mirrors each. | Minor |
| **D10** | `flip/osd.mdx`, `expand/osd.mdx`, `dual-flip/osd.mdx` | The `LOW BLUE LIGHT` bullet alone slides into third-person description (*"Reduces the amount of blue light…"*) while every neighbouring bullet is an imperative to the reader. The register break is EN's. | Major |
| **D11** | `panorama/controls.mdx` | Four button entries, two grammatical modes, in EN: infinitive-style bullets (*"Navigate within the menu." / "Decrease values such as…"*) against third person (*"**Short press:** Confirms a selection"*, *"Opens the brightness shortcut menu."*). The page reads as assembled from two sources. FR mirrors the mixture. | Major |
| **D12** | `panorama/osd.mdx` | **"DP"** (*"the left screen (DP monitor)"*) is never introduced anywhere in the manual. FR renders `moniteur DP` per §5.2; `DP` is glossary open item #1. | Minor |
| **D13** | `panorama/installation.mdx` vs `controls.mdx` | EN calls the same socket **"the HDMI port"** on the installation page and **"3 × Mini HDMI Ports"** on the controls page. The customer is looking at a Mini-HDMI socket. FR faithful. | Minor |
| **D14** | `infinity-lite/display-settings.mdx` | The whole `## Arrange Your Displays (Video)` `<Tabs>` block repeats, almost word for word, the Windows and macOS instructions given ~30 lines above — **in EN**, and with the UI-string convention switching between the two passes (bold, then quoted). FR reproduces both passes; deleting one in French only would break structural parity. *(Note: the duplicated EN block still says `'Mirrored'` where the first pass says `Flipped` — a third variant of the E4 defect below.)* | Major |
| **D15** | `infinity/controls.mdx` | EN calls button presses on a rotary control **"gestures"** (*"the full gesture reference"*, *"The same gestures work"*). In French `geste` means a touch/trackpad gesture, so the word sends the reader looking for a touchscreen. FR faithful. | Major |
| **D16** | `infinity/installation.mdx` | EN package line **"1× USB-C & 1× USB & 1× HDMI"** — *"1× USB"* is not a port type, on a page whose whole point is distinguishing USB-A from USB-C. FR faithful (`1 USB-C, 1 USB et 1 HDMI`). | Major |
| **D17** | `onecable/installation.mdx` steps 3–4 | EN: *"Place the **bracket** firmly on a flat surface."* then *"The **adjustable stand** is located at the back."* Two part names in consecutive steps with nothing saying whether it is one part or two — and a *bracket* (the clip that grips the laptop lid) that you lay on a table is odd in any language. Both FR renderings are §5.1-locked. | Major |
| **D18** | `infinity/display-settings.mdx`, `infinity-lite/display-settings.mdx` | EN heads a scaling instruction *"Want more on-screen space?" / "Need more overview?"* and then tells the reader to scale **up** to 150 %, which reduces both. Question and answer pull in opposite directions. FR faithful; the question leads are §10.1.F-locked. | Minor |
| **D19** | `en/manuals/expand/installation.mdx:63` vs `flip:76` / `dual-flip:50` | **EN-expand has drifted from the Dutch.** The Dutch says *"Dit kan **gemakkelijk** via de USB-A-poort van je laptop"* in **all three** products (`nl/…/flip:76`, `nl/…/dual-flip:50`, `nl/…/expand:63`). EN keeps it in two — *"This can easily be done via your laptop's USB-A port"* — but expand reads *"The USB-A port on your laptop works well for this"*, silently dropping *easily*. So the EN variance here is **not** null: expand is the drifted side. FR now mirrors EN per file (flip/dual-flip carry `permet de le faire facilement`, expand keeps `convient parfaitement pour cela`, faithful to its own EN). **If EN-expand is repaired to say "easily", the three French sentences should collapse onto `Le port USB-A de votre ordinateur portable permet de le faire facilement.`** Raised by `review-fr.md` M-3. | Minor |

---

## F · French is more specific than both sources — for the native reviewer to confirm

| # | Where | The gap | Severity |
|---|---|---|---|
| **F1** | `panorama/installation.mdx:66` | Both sources are **vague about the failure mode**: EN *"may cause **interference**"*, NL *"kan dit **storingen** veroorzaken"* (= *disturbances / malfunctions*, generic). The shipped French now reads `peut provoquer **un conflit d'alimentation**`. That change was necessary — French `interférences` reads as *electromagnetic* interference and pointed the customer at the wrong phenomenon entirely — but `conflit d'alimentation` names a **power-negotiation conflict**, which is an editorial inference from the surrounding sentence (a second charger and the Panorama both feeding the laptop), not something either source states. Glossary §5.2 now locks that inference as a term. **Two ways to close the gap, client's choice:** (a) confirm the mechanism and fix EN/NL to say what they mean, or (b) soften the French to a source-vague rendering such as `des perturbations` or `des dysfonctionnements`. Kept as-is pending that call — it is a net improvement over the EMI misreading either way. Raised by `review-fr.md` M-4. | Minor |

## E · Already on the client list (restated for completeness)

| # | Where | Observation |
|---|---|---|
| **E4** | all `display-settings` pages | **`'Flipped'` is not a Windows option label**; the real French label is `Paysage (inversé)` and the real English one is *"Landscape (flipped)"*. FR (and DE) silently supply the correct label; IT keeps the literal; the NL origin says `Gespiegeld` (= *mirrored*, a different feature). Adjudicated in `backtranslation-review-fr.md` row 3 and `safety-align-fr.md` finding 6.1 — **fix `en/`**, FR is the correct side. |
| **E7** | `infinity` / `infinity-lite` / `panorama` `safety.mdx` | Three different EN headings for the same ten-item list (*"Check before use" / "Read this before use" / "Before use"*), with two list styles. FR mirrors all three distinctly, which is correct behaviour, but the EN inconsistency is worth a client note. |
| **E2/E3/E5** | `safety.mdx` set | Null EN variance (*way/manner*, *business/professional*, *impact/impacts*) collapsed to one French form each. No action. |
