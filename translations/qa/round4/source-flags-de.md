# Round 4 — source-inherited findings surfaced by the German review

**What this file is.** Every round-4 finding where the German is a *faithful* rendering of the
English (and, where checked, the Dutch), and the defect the reviewer saw is therefore in the
source. **No German file was changed for any item on this list.** Fixing the German here would
have broken meaning parity with EN/NL; these need a decision from the client or the EN/NL owner,
after which the change propagates to all five languages at once.

Verified by opening the aligned `en/` line for every row. Where the EN wording was itself
ambiguous, the `nl/` line was checked too.

---

## 1. Safety — the 5 V vs 5–20 V contradiction (highest value on this list)

**Files:** canonical safety body — `de/manuals/{onecable,lite,lite-144hz,flip,expand,one-4k,one-4k-oled}/safety.mdx` and `de/manuals/dual-flip/safety.mdx` (**8 shipped files**).

> EN 5: `The monitor operates on a DC input between 5V and 20V (with a tolerance of ±2V).`
> EN 6: `Only use the device with a 5V power source via the appropriate cable.`
> DE 5: `Der Monitor arbeitet mit einem DC-Eingang zwischen 5 V und 20 V (mit einer Toleranz von ±2 V).`
> DE 6: `Verwende das Gerät ausschließlich mit einer 5-V-Stromquelle über das passende Kabel.`

Item 6 forbids most of the range item 5 permits, and the same manuals elsewhere tell the customer
to use a 45 W PD charger, i.e. not 5 V. The German reproduces both lines exactly — restriction
scope, numbers and units all verified correct in round-4's safety alignment audit. **This is an
EN/NL source defect now shipped in five languages, in safety copy.** Resolve at source, then
propagate.

## 2. Colour spec labelled two ways inside one table

**Files:** `flip/index.mdx`, `expand/index.mdx` (two tabs of one table), plus `onecable/index.mdx`,
`lite/index.mdx`, `dual-flip/index.mdx`.

*(Corrected after review — the original wording of this section overstated the scope.)*

There are **two distinct EN defects** here, not one:

1. **A true same-value split inside one table — `flip/index.mdx` only.** `:47` labels `45% NTSC`
   as `Color Gamut`, `:66` labels the *identical* value `45% NTSC` as `Color Accuracy`, in two
   tabs of one table. `expand/index.mdx` has the same two labels but on **different** values
   (`72%` vs `45%`), so it is a labelling inconsistency, not a self-contradiction.
2. **`Color Accuracy` is the wrong term for gamut coverage** wherever it is used — accuracy is a
   ΔE quantity, coverage is not. This affects `onecable`, `lite` and `dual-flip` too, which use
   `Color Accuracy` alone with no in-file split.

German follows the glossary (§8) in every case: `Color Gamut` → `Farbraum`,
`Color Accuracy` → `Farbgenauigkeit`. Do **not** harmonise in German only; that would hide the
EN defect from the other four languages.

## 3. Box contents that do not match the box

| File | EN line | Problem |
|---|---|---|
| `onecable`, `flip`, `expand`, `dual-flip` `/index.mdx` | `we recommend disconnecting the power cable when the monitor is not in use` | Several of these products ship no mains cable and no adapter; the Dual Flip's own package list is cables + case only. |
| `dual-flip/safety.mdx` | `Only use the included AC/DC adapter as power supply.` | No AC/DC adapter in the Dual Flip box. (The indefinite `an AC/DC adapter` variant used by infinity / infinity-lite / panorama does not have this problem.) |
| `infinity/installation.mdx` step 4 | `Place the fully folded set into the included leather carry pouch.` | The Infinity package list calls it a `Protective case`. Two names, one part. |
| `expand/index.mdx` vs `expand/installation.mdx` | `6x protective clips` vs `## Protective Cap` | Different word *and* different number for the part the customer is told to fit. |

## 4. Instructions that cannot be followed as written

| File | EN line | Problem |
|---|---|---|
| `infinity-lite/installation.mdx` L13 | `Follow these steps in order to safely deploy both extension screens behind your laptop.` | Two-screen wording on a one-screen product (`index.mdx`: "one extra portable display"). Verified: EN says "both extension screens". |
| `infinity-lite/installation.mdx` L91 | `Connect the HDMI to USB-C cable to the **third** port of the Screenmate` | `controls.mdx` documents **two** USB-C ports and identifies the HDMI port as the leftmost. A third port is never defined. |
| `infinity-lite/installation.mdx` L102 | `Switch to the correct connection mode (external power required) … Phone mode also requires external power.` | No "connection mode" is defined anywhere in the manual, and the power requirement is stated twice in consecutive sentences. |
| `infinity-lite/installation.mdx` L32 | `Hold both red arrow positions … and pull the screen outward to release the single screen.` | The object pulled and the object released are the same screen, phrased as if they were different. |
| `infinity-lite/installation.mdx` L41 vs heading | `### 4. Pull out the frame` / `Click open the frame to extend it.` | Heading says pull out, body says click open in order to extend. |
| `one-4k` + `one-4k-oled` `/installation.mdx` L17 | `If your device supports charging over USB-C, the screen automatically charges as soon as the charger is connected to the Screenmate.` | **Checked against EN as instructed:** EN literally says the *screen* charges. Neither product has a battery, and the conditional is a non-sequitur (*your device* supports charging → *the screen* gets charged). German is faithful; do not "fix" it to power wording until the source is settled. |
| `one-4k` + `one-4k-oled` `/osd.mdx` L34 | `Press and hold the button above the power button for 10 seconds` | `controls.mdx` documents three buttons and never establishes a vertical order, so "the button above the power button" points at nothing identifiable. |
| `panorama/installation.mdx` L77 | `On the monitor, connect the HDMI cable to the HDMI port next to the white power cable.` | `controls.mdx` documents `3 × Mini HDMI Ports`. There is no HDMI port, and there are three Mini-HDMI ports, so the definite singular resolves to nothing. |
| `panorama/installation.mdx` L50 | `### Option 1 — USB-C (single cable)` followed by two steps using two USB-C cables | Self-contradiction at the point where the customer picks a setup. Also glossary-locked (§7.4). |
| `panorama/controls.mdx` L31 | `**Long press (1 second):** Switch the monitor off.` | Only switching off is documented; the reader is never told how to switch the Panorama on. |
| `panorama/osd.mdx` L28 | `Press the **Exit** button to close the menu.` | `controls.mdx` names it `Confirm / Exit Button` and specifies that a **long** press exits. EN shortens the name and drops the long press. |
| `onecable/installation.mdx` L36 | `connect both cables to the laptop first, before connecting the other end to the Screenmate` | Two cables, singular "the other end" — the number mismatch is in EN. |
| `onecable/installation.mdx` L57 | `Connect your laptop to Screenmate via a USB-C cable (with full functionality)` | Dangling parenthetical: it is impossible to tell what needs full functionality. |
| `onecable/installation.mdx` L62 | `Note: Use a power adapter of at least 45W. No USB-C charger? Use a suitable power adapter.` | Tautology in EN ("no charger? use a charger"). `troubleshooting.mdx` states the same case correctly, so EN already contains its own fix. |
| `onecable/installation.mdx` L44 | `Then connect the other USB cable to a power outlet.` | A USB-A connector does not go into a wall socket; EN means a power adapter. |
| `onecable/troubleshooting.mdx` L15 | `Check if the motherboard indicator light is on.` | A consumer cannot see a motherboard LED. This is the *first* step of the first troubleshooting answer, so it blocks the whole answer. Glossary §1.1 locks the German rendering. |

## 5. Button / port mappings that contradict each other

| Files | EN | Problem |
|---|---|---|
| `infinity/controls.mdx` L45–46 | `Press right ("Plus"): increase the backlight (brightness).` / `Press left ("Min"): decrease the volume.` | The pair is logically incomplete — no documented way to *lower* brightness or *raise* volume. |
| `infinity/controls.mdx` vs `infinity-lite/controls.mdx` | right = brightness, left = volume (Infinity) vs left = brightness, right = volume (Infinity Lite) | The same two directions carry opposite functions on two sibling products. One of the two is factually wrong; needs hardware confirmation. |
| `lite/controls.mdx` + `lite-144hz/controls.mdx` | `Scroll Wheel — Short press: turn the device on` vs `Power & Return Button — Press to open the on-screen settings menu` | As documented, the scroll wheel powers the device and the button named "Power" does not. (The *German* naming defect — "Power- und Zurück-Taste" reading as two buttons — **was** fixed, see fixlog. The function mapping was not touched.) |
| `expand/controls.mdx` vs `expand/osd.mdx` | `**≡ Menu button:**` vs `Press the **M (Menu)** button` | **Checked as instructed:** EN itself uses two different names for the same button on consecutive pages, so the German divergence is inherited, not translator drift. |
| `one-4k` + `one-4k-oled` `controls.mdx` vs `osd.mdx` | `### Menu Button (Power / OSD)` vs `power button` (×5 on the OSD page) | Same pattern: the EN pages disagree with each other. |
| `one-4k-oled/controls.mdx` L37–39 | `### USB-A Port` followed only by a `{/* TODO: confirm with Louie … */}` comment | The EN page ships a heading with no body. The German reproduces it exactly. Blocked on Louie. |
| `onecable` `controls` / `installation` / `troubleshooting` | `USB-C Port (Power Only / Power Delivery)` / `the Power port` / `Power USB-C port` | Three EN names for one socket inside one manual. |
| `onecable/installation-mac.mdx` | `your MacBook` / `restart your Mac` / `restart your laptop` / `to your laptop` | Three EN names for the customer's machine on one page, including inside two parallel step lists. |

## 6. Specs and alt texts that do not match the product

| File | EN | Problem |
|---|---|---|
| `panorama/index.mdx` | `**Viewing Angle** \| 360°` | Physically impossible and out of line with every sibling (172°/178°). Reads as a typo and costs the whole table its credibility. |
| `panorama/index.mdx` + `panorama/installation.mdx` | `Viewing Angle` (panel spec) and `your desired viewing angle` (the tilt the user sets) | One EN term, two unrelated meanings, inside one product. German is faithful to both. |
| `one-4k-oled/index.mdx` | `**Dimensions (folded)**` | Flat panel with an integrated stand — nothing folds. The One 4K page correctly says just `Dimensions`. |
| `one-4k-oled/index.mdx` | `Panel Type \| OLED` + `Screen Type \| AM-OLED` | The two rows say the same thing in the wrong order (AM-OLED *is* the panel type). On the One 4K the pair is meaningful (IPS / LCD). |
| `lite`, `lite-144hz`, `one-4k`, `one-4k-oled` `/installation.mdx` | alt: `HDMI connection to a PC, console, or camera` | No camera appears anywhere in the manual. |
| `expand/installation.mdx` | alt: `Installation steps 1 through 6` | The procedure has five steps. |
| `flip/index.mdx` | `- **Left** screen: 0° – 245° (180° tiltable up and down)` | A 180° tilt stated behind a 245° rotation range; the two cannot be reconciled from the page. |
| `dual-flip/index.mdx` | `Each screen runs at 2560 × 1600 resolution and connects via USB-C or via USB-C + HDMI + USB-A.` | "Each screen … connects" points the reader at connecting screens individually; the next page explains that one cable feeds one side. |

## 7. Editorial defects the German inherits verbatim

| File | EN | Note |
|---|---|---|
| all six `safety.mdx` | `Recommended ambient temperature: between -20°C and 60°C.` | `Recommended` is wrong for an 80-kelvin span — this is the *permissible* range. Safety body: frozen, not touched. |
| `flip/installation.mdx` | `first check which ports are involved` → `First check which ports the Screenmate has` → `First check which ports your laptop has` | Three "first check" in twelve lines, the last two contradicting each other about what to check first. |
| `infinity/installation.mdx` | `Each screen rotates a maximum of 90°.` … six lines later … `Each screen has a maximum rotation of 90°.` | Same fact, twice, on one page. |
| `infinity-lite/installation.mdx` | `Follow the correct sequence … to avoid damage to the device. Store your Screenmate carefully to prevent damage to the equipment.` | Same purpose clause twice in consecutive sentences. |
| `infinity-lite/display-settings.mdx` | Windows + macOS instruction set appears twice (`## Display Configuration`, then `## Arrange Your Displays (Video)`), with slightly different wording and a bold-vs-quotes split for the same UI strings | Reads as an editing accident. The duplicated *blocks* must stay — removing one would break structural parity. *(Corrected after review: an earlier version of this row said parity "forbids collapsing it in German only", which misdescribed the file. The one substantive EN divergence inside the duplicate — `:57` `'Mirrored'`, the only such occurrence in the whole EN corpus against eight `Flipped` — **is** collapsed onto the `Querformat (gedreht)` target in German, and that is correct and locked: `glossary-de.md` §9 carries the row `Mirrored (superseded — EN now says "Flipped") → Querformat (gedreht)`. No page change needed; only this description was wrong.)* |
| `infinity-lite/installation.mdx` | three `<Warning>` callouts containing neutral assembly instructions | Component choice is structural; changing it in German only would break parity. Worth raising with the EN owner — repeated non-warnings devalue the real ones. |
| `lite` + `lite-144hz` `/osd.mdx` | `Adjust the brightness of the red RGB value.` (and green, blue) | A *value* has no brightness. `expand/osd.mdx` gets it right in EN (`Adjust the red channel`), so EN already contains its own fix. |
| `lite` + `lite-144hz` `/osd.mdx` | `Color Temperature: Choose User, Warm, or Cool to adjust the overall color intensity.` | Colour temperature shifts the white point, not intensity. |
| `infinity/controls.mdx` | `the full gesture reference` / `The same gestures work for both screens.` | "Gesture" is used for presses and holds on a physical rocker switch. German `Geste` carries the same touch-input implication, so the German is faithful — but a reader of either language is misdirected. |
| `panorama/controls.mdx` | `Use a Mini HDMI to HDMI cable to connect your laptop to an individual screen.` | The intended meaning (each of the three Mini-HDMI ports drives one panel) is not recoverable from the EN sentence. |
| `panorama/osd.mdx` | `The Panorama drives three independent screens, so you may want to adjust the desktop layout…` | The causal link does not hold — arranging displays in the OS is true of any external display. (The German *modality* was repaired, see fixlog; the causal claim is the source's.) |
| `en/manuals/**/display-settings.mdx` | Dutch parenthetical glosses (`'Beeldscherminstellingen'`, `'Identificeren'`, `'Beeldschermstand'`) in EN body copy and alt text | Intentional (the screenshots are Dutch), but it is why the German page previously led with an English label that appears neither on the screenshot nor in the reader's OS. See the §9 amendment in `glossary-de.md`. |

---

## 8. The scaling prompt — one Dutch string, three English strings *(added in review follow-up)*

**Files:** `de/manuals/{onecable,dual-flip,flip,expand}/display-settings.mdx:34` (shared body),
`infinity-lite/display-settings.mdx:23` and `:59`, `infinity/display-settings.mdx:30`,
`panorama/osd.mdx:49` — **8 shipped sites**.

All eight introduce the identical instruction: *set scaling to 150 % so text and elements are
displayed larger*. The Dutch source says **`overzicht`** at every one of them. The English has
drifted into three different strings:

| Site | **NL — the source** | EN | DE (after this round) |
|---|---|---|---|
| `{onecable,dual-flip,flip,expand}/display-settings:34` | `Behoefte aan meer overzicht?` | `Need more overview?` | `Brauchst du mehr Übersicht?` |
| `infinity-lite/display-settings:23` | `Heb je behoefte aan meer overzicht?` | `Need more overview?` | idem |
| `infinity-lite/display-settings:59` | `Behoefte aan meer overzicht?` | `Need more overview?` | idem |
| `infinity/display-settings:30` | `Heb je behoefte aan meer **overzicht**?` | `Want more on-screen space?` | idem |
| `panorama/osd:49` | `Meer **overzicht** nodig?` | `Need more room?` | idem |

**Two separate findings for the EN owner:**

**8a — EN-side drift (3 strings for 1 source string).** `Want more on-screen space?` and
`Need more room?` are not translations of `meer overzicht`; they are English rewrites that changed
the meaning. Recommend harmonising the EN corpus to a single string so the other four languages
stop having to adjudicate which witness to follow.

**8b — the prompt does not match the instruction it introduces, in *any* language.** Raising
scaling to 150 % enlarges text and UI elements and therefore shows **less** on screen at once —
so neither "more overview" (NL, and now DE/IT) nor "more space" (the old DE/IT target) follows
from it. `mehr Übersicht` restores **fidelity to the Dutch**; it does not make the passage
logical. The underlying defect is in the source and is inherited by all five languages at all
eight sites. Recommend rewording at source — something like *"Is everything too small?"* /
*"Alles zu klein?"* — and propagating once.

**Cross-language state.** Italian resolved this against the Dutch in `f66e287`; German now matches
on all eight sites (this round). The rule is recorded as a standing ruling in `glossary-de.md`
§10.1: *this family resolves against the Dutch; do not re-split the row per EN variant.* FR should
be checked against the same principle before the branch ships.
