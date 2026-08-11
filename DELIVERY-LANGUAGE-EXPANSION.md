# Delivery Report — German, French & Italian Manuals

**Date:** 2026-08-11 · **Branch:** `lang-expansion-de-fr-it` · **Scope:** full expansion of the Screenmate manuals site from 2 languages (NL, EN) to 5 (NL, EN, DE, FR, IT)

---

## 1. What shipped

- **186 new pages** — the complete manual set (11 products + site index, 62 pages) in German, French and Italian, at `/de/…`, `/fr/…`, `/it/…` mirroring the existing URL scheme.
- **Language switcher** now offers all 5 languages, each with its country flag, and **preserves the current page** when switching (e.g. the Italian Flip OSD page switches directly to the German Flip OSD page). 1,116 cross-language links generated and machine-verified.
- **Locked terminology glossaries** per language (`translations/glossary-de.md`, `-fr.md`, `-it.md`) — the same role the Dutch glossary plays today: registers, technical terms, device labels, number formats, section names. All future copy in these languages should be written against them.
- The QR-code redirects and all existing NL/EN content are untouched (one whitespace-only fix aside).

## 2. Language register choices (need your sign-off)

| Language | Register | Rationale |
|---|---|---|
| German | informal **du** | Mirrors the Dutch "je" brand voice; common for consumer-tech brands in DACH. |
| French | formal **vous** | Deliberate exception: French consumer manuals overwhelmingly use vous even for casual brands; tu would read as an error, not warmth. |
| Italian | informal **tu** | Mirrors the Dutch voice; standard for consumer tech in Italy. |

Related conventions applied deliberately (details in the glossaries): SI unit spacing in all three languages (`45 W`, `100 %`) where NL/EN close them up; German title style `Screenmate OneCable – Handbuch`; `reverse charging` stays English in German, is translated with a first-use English gloss in French (`charge inversée`) and Italian (`ricarica inversa`).

## 3. Verification performed

**Mechanical (machine-checked, all passing):**
1. Structural parity vs. English on every page: headings, steps, tables, components, images — 0 failures.
2. Numeric fidelity: every number in the English corpus verified present with correct locale formatting — 0 failures.
3. Safety-negation counts, register scans (no Sie/tu/Lei leakage), do-not-translate term survival (42 locked terms) — clean.
4. Shared-chapter byte-identity: safety and display-settings chapters are literally identical across the products that share them, per language — enforced by checksum.
5. Build check and link check pass at the pre-existing baseline (the checker's known false positives on URL-encoded image paths; all images verified rendering in the browser).
6. An automated checker (`scripts/verify_translation.py`) with a 20-test suite (`tests/test_verify_translation.py`) now guards all of the above for future edits.

**Semantic (independent AI review):**
7. **Blind back-translation:** 12 independent agents translated every one of the 186 pages back to English *without access to the originals*; 3 comparers then diffed against the source. Result: **zero critical and zero moderate meaning drift in all three languages** (12 cosmetic notes, fixed or logged).
8. **Adversarial review:** 12 further agents read English + Dutch + target side by side with instructions to find errors. ~130 findings were raised; 102 accepted findings were fixed in three review-verified fix waves — including three safety-relevant catches (a French modifier that weakened the 5 V power restriction, a dropped "properly" in the Italian grounding clause, French partial-negation phrasing). **Zero critical findings survived.**

**Visual:** all three languages rendered and navigated in a live build; switcher, flags, page-preservation, and images verified by screenshot.

## 4. What machine verification cannot prove

Stated plainly: the checks above prove the translations are **structurally complete and semantically faithful**. They cannot prove that the copy **reads natively** to a German, French or Italian customer, nor that the safety wording satisfies each market's **regulatory expectations**. That residual risk is what §5 and §6 are for.

## 5. The bounded ask for your review partner

A native-speaker review does not need to cover 60,000 words. Because the safety chapters are shared across products, the entire high-stakes surface is:

- **5 distinct safety texts ≈ 1,000 words per language ≈ 3,000 words total**, plus the spec tables.
- Canonical files (fixing the first file of a group fixes all its copies — they are byte-identical):
  - `de|fr|it/manuals/onecable/safety.mdx` (shared by 7 products)
  - `de|fr|it/manuals/dual-flip/safety.mdx`, `…/infinity/safety.mdx`, `…/infinity-lite/safety.mdx`, `…/panorama/safety.mdx`
- Optional second tier: the OS-settings chapter (`onecable/display-settings.mdx`, shared by 4 products) and the per-product spec tables.

## 6. Compliance note (please confirm with your advisor)

Our reading of **EU Regulation 2023/988 (GPSR, in force since December 2024)** is that safety information must be provided in the language of each member state where the product is sold. If that reading is correct, the safety translations above carry legal weight in Germany, France, Italy (and other markets where these languages apply). This is our reading, not legal advice — please confirm with your compliance contact.

## 7. Findings for you — `translations/flags-consolidated.md`

The review process also audited your existing content. The consolidated report contains:
- **41 English-source issues** (e.g. the same spec value labelled "Color Gamut" on one tab and "Color Accuracy" on another; "two signal sources" followed by a list of three; a port-check instruction that differs between the 14″ and 15.6″ tabs) — confirmed independently by multiple languages; we recommend an EN/NL cleanup pass.
- **21 Dutch-side observations** (e.g. `nl` says the Infinity layout is "identiek" where EN and all three new languages say mirrored) — NL was frozen during this project; your call.
- **11 product-fact questions** only you can answer (e.g. the Infinity vs Infinity Lite control-direction contradiction; whether the Lite's button is silk-screened in English).
- 11 minor internal items we deferred deliberately.

## 8. Numbers

110 commits · 387 files changed · ~32,000 lines added · 3 locked glossaries · 30 QA artifacts under `translations/qa/` (back-translations, reviews, fix logs — full audit trail).
