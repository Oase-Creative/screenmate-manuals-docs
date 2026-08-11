import json
import textwrap
from pathlib import Path

import pytest

from scripts.verify_translation import parse_page, verify_tree

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
