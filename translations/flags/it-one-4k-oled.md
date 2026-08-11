# IT — One 4K OLED: EN↔NL discrepancies

Format: `- [file] EN says X / NL says Y — blocked|proceeded-with-Z`

Raised by Task 7-it/one-4k-oled. Phrasing-only differences are deliberately **not** listed here.
No blockers — all three entries below are resolved by a binding glossary ruling.

## `## Getting Started` vs NL `## Aansluiten` — different section labels

- [it/manuals/one-4k-oled/installation.mdx, first `##`] EN says `## Getting Started` / NL says `## Aansluiten` (= *Connecting*) — proceeded-with-`## Per iniziare`
  (glossary §9.3 locks `Getting Started` → `Per iniziare`. EN is the structural template and the section's body is a generic seven-bullet orientation list, not connection steps, so the EN label is the accurate one. The NL page mislabels it; only `one-4k` and `one-4k-oled` carry this section in EN, so the divergence is contained to two products. Client may wish to normalise the NL heading.)

## `Menu Button (Power / OSD)`: NL keeps `Power` in English, IT translates it

- [it/manuals/one-4k-oled/controls.mdx, §Pulsante Menu (accensione / OSD)] EN says `### Menu Button (Power / OSD)` / NL says `### Menu-knop (Power / OSD)` (EN word `Power` retained inside the parenthetical) — proceeded-with-`### Pulsante Menu (accensione / OSD)`
  (glossary §9.4 locks this exact heading → `Pulsante Menu (accensione / OSD)`. `Power` is not an OSD caps token and is not in `dnt.json`, so it is not DNT; §5.5 gives `to turn on → accendere` and §2.3 `power button → pulsante di accensione`. `OSD` stays verbatim as a DNT term. Deliberate IT divergence from NL — worth a client eyeball if the physical unit is silk-screened "Power".)

## MDX `TODO` comment: NL translated it, IT keeps the EN text verbatim

- [it/manuals/one-4k-oled/controls.mdx §Porta USB-A; it/manuals/one-4k-oled/osd.mdx after §Scorciatoie] EN says `{/* TODO: confirm with Louie — USB-A port use … */}` / NL says the same comment translated into Dutch (`gebruik van USB-A-poort …`) — proceeded-with-**EN verbatim**
  (glossary §10 rules MDX comments never rendered and explicitly names "the `TODO: confirm with Louie` notes in `one-4k-oled/`" as leave-verbatim. Both comments are byte-identical to the EN source. Note the content itself is an **open client question**: the USB-A port's function and the full OSD menu tree are still unconfirmed, so the IT page — like EN and NL — ships §Porta USB-A with no body copy.)

## Non-flags — checked and dismissed (recorded for the reviewer)

- `index.mdx §Specifiche tecniche`: EN `100,000:1` / NL `100.000:1` — number format only. IT renders `100.000:1` in **both** the spec row and the intro prose, per glossary §4.1 six-digit exception and decision-log ruling 4. This is the corpus's only six-digit figure.
- `index.mdx §Specifiche tecniche`: EN `Screen Size | 15.6"` / NL `Schermgrootte | 15,6 inch` (unit spelled out) — format only; IT uses the preferred prime form `15,6"` per §4.4.
- `index.mdx §Specifiche tecniche`: EN `Special Features | Built-in stand` / NL `Met ingebouwde standaard` ("With a built-in stand") — phrasing only → `Supporto integrato` per §5.4.
- `controls.mdx §Pulsante Menu`: EN link text `[On-Screen Menu]` / NL `[Beeldscherminstellingen (OSD)]` (NL used the target page's own frontmatter title) — phrasing only; EN template followed → `[Menu a schermo]`, href retargeted to `/it/manuals/one-4k-oled/osd`.
- `osd.mdx`: EN `### OSD Lock` / NL `### OSD vergrendeld` ("OSD locked", stative) — heading form only; §9.4 locks `OSD Lock` → `Blocco dell'OSD`.
- `installation.mdx §5`: EN `To connect the Screenmate to an HDMI device` / NL `Om de draagbare monitor aan te sluiten` — coreferential, phrasing only (identical to the dismissed `lite` case).
- `installation.mdx §1` callout: EN `**Important:**` / NL `**Let op:**` (= *Note:*) — callout lead-in label; §5.5 maps `Important:` → `Importante:` and EN is the template.
- `installation.mdx`: NL turns several EN statements into rhetorical questions (`Werkt het niet direct?`, `Levert het apparaat onvoldoende stroom?`) — register device, no meaning change; IT follows the EN declarative form, matching the already-approved `it/manuals/lite/installation.mdx`.
