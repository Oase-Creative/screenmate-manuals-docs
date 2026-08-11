# FR shared-chapter flags (Task 6-fr: safety + display-settings)

EN↔NL divergences found while translating `fr/manuals/*/safety.mdx` and
`fr/manuals/*/display-settings.mdx`. Format:
`- [file] EN says X / NL says Y — blocked|proceeded-with-Z`

Phrasing differences are not listed. Only meaning-level divergences are.

## Display-settings

- [fr/manuals/{onecable,dual-flip,flip,expand}/display-settings.mdx] EN says the Windows display-orientation option is **'Flipped'** / NL says **'Gespiegeld'** (= *Mirrored*) — these are two different Windows options, not two phrasings — proceeded-with-`Paysage (inversé)` per glossary §8, which maps **both** `Flipped` and `Mirrored` to `Paysage (inversé)` and marks `Mirrored` as "superseded on EN pages by Flipped".

- [fr/manuals/infinity/display-settings.mdx] EN says **"Flipped"** / NL says **'Gespiegeld'** (= *Mirrored*) — same divergence as above — proceeded-with-`Paysage (inversé)` per glossary §8.

- [fr/manuals/infinity-lite/display-settings.mdx] EN is internally inconsistent: **"Flipped"** in `## Display Configuration` (line 18) but **'Mirrored'** in `## Arrange Your Displays (Video)` (line 54); NL says **'Gespiegeld'** in both places — proceeded-with-`Paysage (inversé)` in both positions per glossary §8. Note this makes the FR page self-consistent where the EN page is not. **Worth reporting upstream: the EN source should pick one.**

- [fr/manuals/{onecable,dual-flip,flip,expand}/display-settings.mdx] EN names the English OS label and appends a Dutch gloss — `**Display settings** ('Beeldscherminstellingen')`, `'Extend desktop to this display' ('Bureaublad uitbreiden naar dit beeldscherm')`, `'Identify' ('Identificeren')`, `'Display orientation' ('Beeldschermstand')`, `'Scale' ('Schaal')` / NL names only the Dutch label — proceeded-with-French-OS-labels-and-no-gloss (`Paramètres d'affichage`, `Étendre le Bureau à cet écran`, `Identifier`, `Orientation de l'affichage`, `Échelle`) per glossary §8, whose `This PC ('Deze pc')` → `Ce PC` row locks exactly this drop-the-gloss pattern.
  **Caveat for the client:** the three Windows screenshots on this page are **Dutch-language Windows**, not English (verified by opening `images/Screenmate - OneCable - Handleiding images/installation-images/screenmate-onecable-installation-windows-step-5.png`). The EN page's parenthetical glosses exist to bridge that gap. A French reader now sees French label names in prose next to Dutch labels in the screenshot. The glossary ruling was followed as binding, but re-shooting these screenshots (or restoring a gloss) is a real content decision the client may want to make. Same caveat applies to the DE and IT pages.

## Safety

- [fr/manuals/panorama/safety.mdx] EN says "Suitable for both home and **professional** use." / NL says "Geschikt voor zowel thuis als **zakelijk** gebruik." (= *business*) — the other safety pages (infinity, infinity-lite) say "business" on the EN side too — proceeded-with-`Convient à un usage domestique comme professionnel.` (the locked glossary §10 boilerplate, which renders both EN variants identically in French, so the FR corpus stays internally consistent).

## Not flagged (recorded so a later pass does not re-open them)

- NL `nl/manuals/onecable/safety.mdx` hashes differently from the other six NL group-A files. Cause is **line endings + a trailing blank line only** (LF vs CRLF); the prose is character-identical. No semantic divergence.
- Safety section headings differ in wording between EN and NL (`Check before use` / `Read this before use` / `Before use` vs a single NL `Let hierop vóór gebruik`). Glossary §9.4 locks a distinct French heading for each EN variant (`À vérifier avant utilisation` / `À lire avant utilisation` / `Avant utilisation`), so EN structure was followed. Phrasing, not meaning.
