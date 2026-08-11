# DE onecable flags

Task 7-de / onecable (index, installation, installation-windows, installation-mac, controls, troubleshooting).
Format: `- [file] EN says X / NL says Y — blocked|proceeded-with-Z`

Raised: 4. Blocked: 0.

- [installation-windows.mdx] EN says `Open **This PC** ('Deze pc') and open the included **DRIVERS (D:)** drive` — English label plus a **Dutch** parenthetical gloss / NL says `Open **Deze pc** en open de meegeleverde **DRIVERS (D:)**-schijf` — Dutch label only — proceeded-with `Öffne **Dieser PC** und dort das mitgelieferte Laufwerk **DRIVERS (D:)**`, i.e. the German OS label alone, no Dutch gloss (glossary §9 `This PC` → `Dieser PC`; task brief). `DRIVERS (D:)`, `Win10&11`, `Win 7&8`, `mac OS` kept verbatim per §5. **Asset caveat (same one already logged in `de-shared.md` for display-settings):** the referenced screenshots `installation-images/screenmate-onecable-installation-windows-step-1/2/3.png` are **Dutch-language Windows**, so neither the English nor the German label matches what the reader sees. Not blocking — needs an asset decision (re-shoot in German), not a translation change.

- [installation-mac.mdx] EN says `**'System Settings'** > **'Privacy & Security'** > **'Screen & System Audio Recording'**` — English labels, no gloss / NL says the same English labels **plus** a Dutch parenthetical gloss at every occurrence — proceeded-with the glossary §9 pattern: English label + German gloss on **first mention** (`**„System Settings“** („Systemeinstellungen“) …`), German label alone thereafter (`**„Systemeinstellungen“** > **„Datenschutz & Sicherheit“** …`). Same rule applied per label, so `Applications`/`Open` take their gloss at their own first mention in step 3. Justified here because these screenshots really are English (`new installation media/mac-english-*.png`), unlike the Windows ones above. Matches the pattern Task 6-de already shipped in `de/manuals/onecable/display-settings.mdx`.

- [troubleshooting.mdx] EN says `Connection method: Connect your laptop's USB-C port …` as one continuous paragraph / NL says `Aansluitmethode:` on its own line, followed by a separate paragraph — proceeded-with the EN structure (single paragraph, `Anschlussmethode: Verbinde …`), since EN is the structural template. Meaning identical; formatting only.

- [troubleshooting.mdx] EN says `Go to your Mac's launchpad` / NL says `Ga dan naar het opstartplatform van je Mac` — NL translates the feature name into a common noun — proceeded-with `Öffne das Launchpad deines Mac`: `Launchpad` is a keep-EN macOS feature name in `dnt.json`/glossary §5, so the NL common-noun rendering is not followed.
