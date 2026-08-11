# DE Lite flags

Task 7-de / slug `lite`. Pages: index, installation, controls, osd (safety.mdx owned by Task 6).
Format: `- [file] EN says X / NL says Y — blocked|proceeded-with-Z`

Raised: 5. Blocked: 0.

## EN ↔ NL divergences

- [installation.mdx] EN says `**Important:**` / NL says `**Let op:**` (= "Note:") — proceeded-with `**Wichtig:**`. Rationale: EN is the structural template, and glossary §10.1 keeps `Important:` → `Wichtig:` distinct from `Note:` → `Hinweis:`; §10.5 counts `Important:` as its own lead-in with 10 corpus occurrences. NL collapsed the two lead-ins; German keeps them apart.

- [osd.mdx] EN says `Choose User, Warm, or Cool` — on-device values in English / NL says `Kies uit Gebruikersinstelling, Warm of Koel` — two of the three values translated — proceeded-with `Wähle User, Warm oder Cool`. Rationale: glossary §6.3 lists `Warm`, `Cool`, `User`, `Standard` explicitly as firmware-rendered menu values that stay verbatim English. The NL page translates what the reader physically sees on the panel; German does not follow it there.

- [osd.mdx] EN says `**Aspect Ratio (16:9 / 4:3):**` — English gloss, no CAPS token / NL says `**Aspect Ratio (16:9 / 4:3):**` — left English while every sibling gloss on the same page is translated (`Helderheid`, `Contrast`, `Zwartniveau`, `Scherpte`, `Kleurtemperatuur`) — proceeded-with `**Seitenverhältnis (16:9 / 4:3):**`. Rationale: glossary §6.2 third style (gloss without a CAPS token still translates) plus §6.2.1, which locks `Aspect / Aspect Ratio` → `Seitenverhältnis`. NL's keep-EN here is an isolated per-file inconsistency, not a device-label rule.

- [osd.mdx] EN says `### 2. Image Modes` / NL says `### 2. Modusopties` (= "mode options") — proceeded-with `### 2. Bildmodi`, per the §6.4 lock `2. Image Modes` → `2. Bildmodi`. Non-blocking; noted only because the NL heading names the menu differently from EN.

- [controls.mdx] EN says `### Power & Return Button` / NL says `### Power & Return-knop` — NL keeps the English button name, EN uses it as a heading — proceeded-with `### Power- und Zurück-Taste` per glossary §7.4. **Client eye, not blocking:** if "Power & Return" is silkscreened on the physical unit, the German heading will no longer match the hardware. §6.1 covers only ALL-CAPS OSD labels, and this string is not one, so the glossary lock stands — but a photo of the button would settle it.

## Proposed glossary additions (§12)

Neither term is in the glossary; both are the spelled-out expansions of DNT acronyms (`RTS`, `FPS`) and were handled by analogy with §6.1's treatment of `DCR (Dynamic Contrast Ratio)` and `HDR (High Dynamic Range)` — acronym expansions stay English — combined with §3.1 Durchkopplung.

```
Proposed glossary addition:
| Real-Time Strategy (RTS) games | Real-Time-Strategy-Spiele (RTS) | expansion of the DNT label RTS; kept EN like Dynamic Contrast Ratio, hyphenated per §3.1 | ✓ (expansion) |
| First-Person Shooter (FPS) games | First-Person-Shooter-Spiele (FPS) | expansion of the DNT label FPS; idem | ✓ (expansion) |
Reason: lite/osd.mdx and lite-144hz/osd.mdx, "### 2. Image Modes" ECO-mode list. The
alternative German renderings (`Echtzeit-Strategiespiele`, `Ego-Shooter`) would break the
visual link to the RTS / FPS values the reader selects on the device.
```
