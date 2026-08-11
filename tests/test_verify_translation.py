import json
import textwrap
from pathlib import Path

import pytest

from scripts.verify_translation import (
    parse_page, verify_tree, _dnt_pattern, body_hash, _normalize_spaced_thousands,
)

def write(root: Path, rel: str, text: str) -> None:
    p = root / rel
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(textwrap.dedent(text), encoding="utf-8")

EN_PAGE = """\
    ---
    title: "Controls"
    description: "Buttons"
    icon: "gamepad"
    ---
    ## Ports
    The screen is 15.6" wide. Do not cover the vents.
    <Note>
    Use **Power Delivery** chargers only.
    </Note>
    <img src="/images/x.png" alt="Ports overview" />
    1. Press the button.
    2. Wait 5 seconds.
    """

DE_PAGE_OK = """\
    ---
    title: "Bedienung"
    description: "Tasten"
    icon: "gamepad"
    ---
    ## Anschlüsse
    Der Bildschirm ist 15,6" breit. Decke die Lüftungsschlitze nicht ab.
    <Note>
    Verwende nur **Power Delivery**-Ladegeräte.
    </Note>
    <img src="/images/x.png" alt="Übersicht der Anschlüsse" />
    1. Drücke die Taste.
    2. Warte 5 Sekunden.
    """

@pytest.fixture
def tree(tmp_path: Path) -> Path:
    (tmp_path / "translations").mkdir()
    (tmp_path / "translations" / "dnt.json").write_text(json.dumps(["Power Delivery"]))
    write(tmp_path, "en/manuals/lite/controls.mdx", EN_PAGE)
    write(tmp_path, "de/manuals/lite/controls.mdx", DE_PAGE_OK)
    return tmp_path

def test_clean_tree_passes(tree: Path) -> None:
    issues = verify_tree(tree, base="en", targets=["de"])
    assert [i for i in issues if i.severity == "FAIL"] == []

def test_parse_extracts_structure(tree: Path) -> None:
    page = parse_page(tree / "en/manuals/lite/controls.mdx")
    assert page["icon"] == "gamepad"
    assert [lvl for lvl, _ in page["headings"]] == [2]
    assert page["components"] == ["Note", "/Note"]
    assert page["srcs"] == ["/images/x.png"]
    assert page["steps"] == 2

def test_missing_heading_fails(tree: Path) -> None:
    bad = (tree / "de/manuals/lite/controls.mdx").read_text(encoding="utf-8").replace("## Anschlüsse\n", "")
    (tree / "de/manuals/lite/controls.mdx").write_text(bad, encoding="utf-8")
    issues = verify_tree(tree, base="en", targets=["de"])
    assert any(i.check == "structure" and i.severity == "FAIL" for i in issues)

def test_decimal_transform_accepted_and_missing_number_fails(tree: Path) -> None:
    # 15.6 -> 15,6 must be accepted (fixture already passes); dropping a number must fail
    bad = (tree / "de/manuals/lite/controls.mdx").read_text(encoding="utf-8").replace("Warte 5 Sekunden", "Warte kurz")
    (tree / "de/manuals/lite/controls.mdx").write_text(bad, encoding="utf-8")
    issues = verify_tree(tree, base="en", targets=["de"])
    assert any(i.check == "numbers" and i.severity == "FAIL" for i in issues)

def test_wrong_register_warns(tree: Path) -> None:
    bad = (tree / "de/manuals/lite/controls.mdx").read_text(encoding="utf-8").replace("Drücke die Taste", "Drücken Sie die Taste")
    (tree / "de/manuals/lite/controls.mdx").write_text(bad, encoding="utf-8")
    issues = verify_tree(tree, base="en", targets=["de"])
    assert any(i.check == "register" and i.severity == "WARN" for i in issues)

def test_missing_dnt_term_fails(tree: Path) -> None:
    bad = (tree / "de/manuals/lite/controls.mdx").read_text(encoding="utf-8").replace("Power Delivery", "Stromlieferung")
    (tree / "de/manuals/lite/controls.mdx").write_text(bad, encoding="utf-8")
    issues = verify_tree(tree, base="en", targets=["de"])
    assert any(i.check == "dnt" and i.severity == "FAIL" for i in issues)

def test_stub_marker_fails(tree: Path) -> None:
    write(tree, "de/manuals/lite/osd.mdx", '---\ntitle: "STUB"\n---\n{/* STUB-TRANSLATION-PENDING */}\n')
    write(tree, "en/manuals/lite/osd.mdx", '---\ntitle: "OSD"\nicon: "sliders"\n---\n## Menu\n')
    issues = verify_tree(tree, base="en", targets=["de"])
    assert any(i.check == "stub" and i.severity == "FAIL" for i in issues)

def test_dedupe_divergence_fails(tree: Path) -> None:
    write(tree, "en/manuals/onecable/safety.mdx", '---\ntitle: "Safety"\nicon: "shield"\n---\nNever cover it.\n')
    write(tree, "en/manuals/flip/safety.mdx",     '---\ntitle: "Safety"\nicon: "shield"\n---\nNever cover it.\n')
    write(tree, "de/manuals/onecable/safety.mdx", '---\ntitle: "Sicherheit"\nicon: "shield"\n---\nDecke es niemals ab.\n')
    write(tree, "de/manuals/flip/safety.mdx",     '---\ntitle: "Sicherheit"\nicon: "shield"\n---\nDecke es nie ab.\n')
    issues = verify_tree(tree, base="en", targets=["de"])
    assert any(i.check == "dedupe" and i.severity == "FAIL" for i in issues)

# --- Regression tests for the tunings applied during nl calibration ---

NUMWORD_HEADING_EN = """\
    ---
    title: "Counts"
    icon: "hash"
    ---
    ## Connection Options
    ### 1. Three USB-C cables
    Use the included cables.
    Connect it once.
    """

def test_numword_credit_leak_is_not_forgiven_outside_target_heading(tree: Path) -> None:
    # Base spells the heading count as a word ("Three" -> credit for digit '3').
    write(tree, "en/manuals/lite/counts.mdx", NUMWORD_HEADING_EN)
    # Target ALSO keeps the heading as a spelled word (no digit '3' anywhere in
    # its own heading -- the credit is never actually "spent" there) but has an
    # unrelated, genuine duplicated "3" in body prose. A same-valued credit
    # generated elsewhere in the document must not silently forgive a real
    # defect just because the numbers match -- forgiveness must be scoped to
    # digits that actually appear within the target's own heading line.
    write(tree, "de/manuals/lite/counts.mdx", """\
        ---
        title: "Zählungen"
        icon: "hash"
        ---
        ## Verbindungsoptionen
        ### 1. Drei USB-C-Kabel
        Verwende die mitgelieferten Kabel.
        Schließe es 3 Mal an.
        """)
    issues = verify_tree(tree, base="en", targets=["de"])
    assert any(i.check == "numbers" and i.severity == "FAIL" for i in issues)

def test_numword_credit_legitimate_heading_conversion_passes(tree: Path) -> None:
    # Base spells the heading count as a word; target legitimately renders the
    # same count as a digit in ITS OWN heading (matching the digit+"x" style
    # convention used elsewhere) -- this must be accepted, not flagged.
    write(tree, "en/manuals/lite/counts.mdx", NUMWORD_HEADING_EN)
    write(tree, "de/manuals/lite/counts.mdx", """\
        ---
        title: "Zählungen"
        icon: "hash"
        ---
        ## Verbindungsoptionen
        ### 1. 3 USB-C-Kabel
        Verwende die mitgelieferten Kabel.
        Schließe es an.
        """)
    issues = verify_tree(tree, base="en", targets=["de"])
    assert [i for i in issues if i.check == "numbers" and i.severity == "FAIL"] == []

def test_dnt_pattern_matches_whole_word_not_inside_unrelated_word() -> None:
    pat = _dnt_pattern("Flip")
    assert pat.search("Screenmate Flip 15.6\" manual") is not None
    assert pat.search("choose 'Flipped' to correct this") is None

def test_body_hash_ignores_trailing_whitespace_but_catches_mid_body_diff(tmp_path: Path) -> None:
    a = tmp_path / "a.mdx"
    b = tmp_path / "b.mdx"
    c = tmp_path / "c.mdx"
    a.write_text('---\ntitle: "X"\n---\nSame content here.\n', encoding="utf-8")
    b.write_text('---\ntitle: "X"\n---\nSame content here.\n\n\n', encoding="utf-8")
    c.write_text('---\ntitle: "X"\n---\nDifferent content here.\n', encoding="utf-8")
    assert body_hash(a) == body_hash(b)
    assert body_hash(a) != body_hash(c)

def test_numword_credit_leak_via_heading_ordinal_digit_is_not_forgiven(tree: Path) -> None:
    # A second variant of the credit-leak bug: the heading ordinal prefix
    # itself ("### 2." -> digit '2') must not count as "digit content present
    # in the target's heading" -- only digits in the translated text AFTER
    # the ordinal may fund forgiveness. Reproduction (reviewer-supplied):
    # base credits '2' via a spelled "Two" in heading 1; target's heading 2
    # happens to be numbered "2." (pure ordinal, no translated digit) plus a
    # genuine unrelated extra "2" in body prose. The ordinal digit must not
    # be mistaken for a legitimate word->digit conversion of that credit.
    write(tree, "en/manuals/lite/counts.mdx", """\
        ---
        title: "Counts"
        icon: "hash"
        ---
        ## Connection Options
        ### 1. Two USB-C cables
        ### 2. One extra accessory
        """)
    write(tree, "de/manuals/lite/counts.mdx", """\
        ---
        title: "Zählungen"
        icon: "hash"
        ---
        ## Verbindungsoptionen
        ### 1. Zwei USB-C-Kabel
        ### 2. Ein Zubehoerteil
        Schliesse es 2 Mal an.
        """)
    issues = verify_tree(tree, base="en", targets=["de"])
    assert any(i.check == "numbers" and i.severity == "FAIL" for i in issues)

def test_numword_credit_leak_via_decimal_heading_false_ordinal(tree: Path) -> None:
    # Root-cause variant (reviewer-supplied, real corpus pattern present in
    # lite/one-4k/one-4k-oled/lite-144hz controls.mdx): "### 3.5mm Headphone
    # Jack" is NOT a numbered step -- it's a measurement that happens to look
    # like an ordinal prefix. A heading-content extraction built on
    # `^#{1,6}\s+\d+\.\s*(.*)$` tears it apart: "3." is consumed as a fake
    # ordinal and "5mm Headphone Jack" becomes "content", minting a phantom
    # digit '5' that can then forgive a completely unrelated credit generated
    # at a different heading ("### 1. Five HDMI ports" -> credit '5'). The
    # genuine extra "5" in body prose must still be caught.
    write(tree, "en/manuals/lite/counts.mdx", """\
        ---
        title: "Counts"
        icon: "hash"
        ---
        ## Ports
        ### 1. Five HDMI ports
        ### 3.5mm Headphone Jack
        """)
    write(tree, "de/manuals/lite/counts.mdx", """\
        ---
        title: "Zählungen"
        icon: "hash"
        ---
        ## Ports
        ### 1. Five HDMI ports
        ### 3.5mm Headphone Jack
        Schliesse es 5 Mal an.
        """)
    issues = verify_tree(tree, base="en", targets=["de"])
    assert any(i.check == "numbers" and i.severity == "FAIL" for i in issues)

def test_decimal_heading_translated_still_passes(tree: Path) -> None:
    # Positive companion: a legitimately translated decimal-looking heading
    # (comma decimal separator, as German/Dutch convention requires) must not
    # be misread as a broken ordinal and must not trigger a false "numbers"
    # FAIL -- the decimal token ("3.5" / "3,5") has to survive as a single
    # unit through the heading comparison, not get torn into "3." + "5".
    write(tree, "en/manuals/lite/counts.mdx", """\
        ---
        title: "Counts"
        icon: "hash"
        ---
        ## Ports
        ### 3.5mm Headphone Jack
        Located on the side.
        """)
    write(tree, "de/manuals/lite/counts.mdx", """\
        ---
        title: "Zählungen"
        icon: "hash"
        ---
        ## Ports
        ### 3,5-mm-Kopfhöreranschluss
        Befindet sich seitlich.
        """)
    issues = verify_tree(tree, base="en", targets=["de"])
    assert [i for i in issues if i.check == "numbers" and i.severity == "FAIL"] == []

# --- Spaced-thousands normalization (fr glossary: "100 000:1" contrast ratio) ---

def test_normalize_spaced_thousands_merges_recognized_separators() -> None:
    # en's own native "100,000" already tokenizes as one NUM_RE match; fr's
    # convention groups the same value with a space (or non-breaking-space
    # variant) instead of a comma. Canonicalize to the comma form en already
    # produces natively, so both sides land on the identical token instead of
    # requiring a second, divergent "bare digits" representation.
    assert _normalize_spaced_thousands("100 000:1") == "100,000:1"
    assert _normalize_spaced_thousands("100&nbsp;000:1") == "100,000:1"
    assert _normalize_spaced_thousands("100 000:1") == "100,000:1"  # U+00A0 NBSP
    assert _normalize_spaced_thousands("100 000:1") == "100,000:1"  # U+202F NNBSP
    # en's own comma form must pass through unchanged (no space/nbsp present).
    assert _normalize_spaced_thousands("100,000:1") == "100,000:1"

def test_normalize_spaced_thousands_does_not_merge_non_three_digit_group(tree: Path) -> None:
    # Guard: only a RIGHT-hand group of EXACTLY 3 digits is a valid thousands
    # grouping. A 2-digit or 4-digit right-hand group must be left untouched
    # -- merging would treat two independent numbers as if they were one and
    # could mask a genuine defect in either of them.
    assert _normalize_spaced_thousands("10 0000 units") == "10 0000 units"
    assert _normalize_spaced_thousands("10 00 units") == "10 00 units"

def test_spaced_thousands_plain_space_passes_numbers_check(tree: Path) -> None:
    # Reproduces the real one-4k-oled corpus pattern: contrast ratio appears
    # both in prose and in a spec table row.
    write(tree, "en/manuals/one-4k-oled/index.mdx", """\
        ---
        title: "Overview"
        icon: "book-open"
        ---
        ## Specs
        The OLED panel delivers a 100,000:1 contrast ratio for deep blacks.
        | Spec | Value |
        | :--- | :--- |
        | **Contrast Ratio** | 100,000:1 |
        """)
    write(tree, "fr/manuals/one-4k-oled/index.mdx", """\
        ---
        title: "Aperçu"
        icon: "book-open"
        ---
        ## Caractéristiques
        Le panneau OLED offre un rapport de contraste de 100 000:1 pour des noirs profonds.
        | Caractéristique | Valeur |
        | :--- | :--- |
        | **Rapport de contraste** | 100 000:1 |
        """)
    issues = verify_tree(tree, base="en", targets=["fr"])
    assert [i for i in issues if i.check == "numbers" and i.severity == "FAIL"] == []

def test_spaced_thousands_nbsp_entity_passes_numbers_check(tree: Path) -> None:
    write(tree, "en/manuals/one-4k-oled/index.mdx", """\
        ---
        title: "Overview"
        icon: "book-open"
        ---
        ## Specs
        The OLED panel delivers a 100,000:1 contrast ratio for deep blacks.
        | Spec | Value |
        | :--- | :--- |
        | **Contrast Ratio** | 100,000:1 |
        """)
    write(tree, "fr/manuals/one-4k-oled/index.mdx", """\
        ---
        title: "Aperçu"
        icon: "book-open"
        ---
        ## Caractéristiques
        Le panneau OLED offre un rapport de contraste de 100&nbsp;000:1 pour des noirs profonds.
        | Caractéristique | Valeur |
        | :--- | :--- |
        | **Rapport de contraste** | 100&nbsp;000:1 |
        """)
    issues = verify_tree(tree, base="en", targets=["fr"])
    assert [i for i in issues if i.check == "numbers" and i.severity == "FAIL"] == []

def test_spaced_thousands_genuinely_missing_number_still_fails(tree: Path) -> None:
    # A real defect (the number dropped entirely, not just reformatted) must
    # still be caught -- the normalization must not make the checker blind to
    # a genuinely missing figure.
    write(tree, "en/manuals/one-4k-oled/index.mdx", """\
        ---
        title: "Overview"
        icon: "book-open"
        ---
        ## Specs
        The OLED panel delivers a 100,000:1 contrast ratio for deep blacks.
        | Spec | Value |
        | :--- | :--- |
        | **Contrast Ratio** | 100,000:1 |
        """)
    write(tree, "fr/manuals/one-4k-oled/index.mdx", """\
        ---
        title: "Aperçu"
        icon: "book-open"
        ---
        ## Caractéristiques
        Le panneau OLED offre des noirs profonds superbes.
        | Caractéristique | Valeur |
        | :--- | :--- |
        | **Rapport de contraste** | excellent |
        """)
    issues = verify_tree(tree, base="en", targets=["fr"])
    assert any(i.check == "numbers" and i.severity == "FAIL" for i in issues)
