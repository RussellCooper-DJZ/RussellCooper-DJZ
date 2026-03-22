from pathlib import Path

import pytest

README_TEXT = Path("README.md").read_text(encoding="utf-8")


def test_readme_removes_template_comment():
    template_markers = (
        "**RussellCooper-DJZ/RussellCooper-DJZ** is a",
        "Here are some ideas to get you started:",
        "Pronouns:",
    )
    for marker in template_markers:
        assert marker not in README_TEXT


@pytest.mark.parametrize("heading", ["### About me", "### Contact", "### Fun fact"])
def test_readme_has_required_sections(heading: str):
    assert heading in README_TEXT


def test_readme_contact_line_is_actionable():
    # Keep docs and tests aligned: README currently directs contact via Issues.
    assert "Reach me through GitHub Issues" in README_TEXT
