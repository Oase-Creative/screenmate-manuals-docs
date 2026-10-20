from scripts.generate_language_links import link_target


def test_regular_page_keeps_full_path():
    assert link_target("fr", "manuals/flip/installation") == "/fr/manuals/flip/installation"


def test_index_page_links_to_folder_route():
    # Mintlify serves index.mdx at the folder route. A client-side switch to
    # ".../index" renders the page but leaves the language selector on the old
    # language and the sidebar empty (live-reproduced 2026-10-20).
    assert link_target("fr", "manuals/flip/index") == "/fr/manuals/flip"


def test_manuals_index_page_is_not_a_folder_index():
    assert link_target("de", "manuals-index") == "/de/manuals-index"
