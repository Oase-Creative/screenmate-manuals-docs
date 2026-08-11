# IT — Infinity: EN↔NL meaning discrepancies

Format: `- [file] EN says X / NL says Y — blocked|proceeded-with-Z`

Scope: `it/manuals/infinity/{index,installation,controls}.mdx` (Task 7-it).
`safety.mdx` and `display-settings.mdx` are Task 6's — see `it-shared.md`.
Phrasing-only differences are deliberately **not** listed here.

## Left/right screen layout: mirrored vs identical

- [it/manuals/infinity/controls.mdx, §Porte e pulsanti intro] EN says `The layout is mirrored on both the left and right screen.` / NL says `De indeling is identiek op het linker- en rechterscherm.` (= *identical*, not mirror-imaged) — proceeded-with-`La disposizione è speculare sullo schermo sinistro e su quello destro.`
  EN followed as the structural and semantic template, and the physical claim is corroborated by the next section on the same page — `Each screen has a built-in speaker on its outer edge` / `Ogni schermo ha un altoparlante integrato sul bordo esterno` — which only makes sense if the two screens are mirror images of each other. Low severity, but `speculare` and `identica` are genuinely different claims about the hardware; the client should confirm against the ports/buttons diagram, and normalise NL if EN is correct.

## Non-flags — checked and dismissed (recorded for the reviewer)

- Multifunction control direction: EN `Press right ("Plus"): increase the backlight (brightness)` / `Press left ("Min"): decrease the volume` — NL agrees exactly (`Druk naar rechts … verhoog de achtergrondverlichting (helderheid)` / `Druk naar links … verlaag het volume`). Translated faithfully. The known cross-product disagreement with `infinity-lite` on which direction does brightness vs volume is an upstream client question, deliberately mirrored rather than fixed.
- `## Setup` (EN) vs `## Installatie` (NL) and `### Setup instructions` vs `### Set-up instructies` — heading phrasing only; glossary §9.3/§9.5 lock `Montaggio` / `Istruzioni di montaggio`.
- `## Package Contents` (EN) vs `## Onderdelen overzicht` (NL); `## On-Screen Menu (OSD)` vs `## OSD-instellingen`; `### Menu / Select / Confirm` vs `### Menu / Selectie / Bevestigingsknop` — phrasing only, glossary-locked targets used.
- `Use the icons below as a reference` vs `Gebruik daarbij de onderstaande afbeeldingen ter hulp`; `Plug it into the port marked with the red sticker` vs NL repeating the full cable name — phrasing only.
- In-page anchor `[On-Screen Menu](#on-screen-menu-osd)` retargeted to `#menu-a-schermo-osd` to match the translated `##` heading, following the NL precedent (`[OSD-instellingen](#osd-instellingen)`). Not a meaning difference; `src`, `icon` and `className` are byte-identical to EN throughout.
