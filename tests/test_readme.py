from pathlib import Path


def test_readme_removes_template_comment():
    readme = Path("README.md").read_text(encoding="utf-8")
    assert "special" not in readme
    assert "Here are some ideas to get you started" not in readme


def test_readme_has_required_sections():
    readme = Path("README.md").read_text(encoding="utf-8")
    for heading in ("### About me", "### Contact", "### Fun fact"):
        assert heading in readme


def test_readme_contact_line_is_actionable():
    readme = Path("README.md").read_text(encoding="utf-8")
    assert "Reach me via GitHub Issues" in readme
