"""Checks on the skill itself, so edits cannot quietly break it."""

import importlib.util
import json
import os
import re
import subprocess
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent
SKILL = ROOT / "skills" / "cwru-look-and-feel"
ASSETS = SKILL / "assets"
HEX = re.compile(r"#[0-9A-Fa-f]{6}\b")


def load(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


contrast = load(ASSETS / "contrast.py", "contrast")


def text_files():
    return [p for p in ROOT.rglob("*") if p.is_file() and p.suffix in {".md", ".css", ".js", ".py", ".json"}
            and not {".git", ".venv", "__pycache__", ".pytest_cache"} & set(p.parts)
            and p != Path(__file__).resolve()]


def test_front_matter_is_valid():
    text = (SKILL / "SKILL.md").read_text()
    match = re.match(r"---\n(.*?)\n---\n", text, re.S)
    assert match, "SKILL.md needs YAML front matter"
    fields = dict(re.findall(r"^(\w[\w-]*):\s*(.+)$", match.group(1), re.M))
    assert fields["name"] == SKILL.name
    assert len(fields["description"]) > 80


def test_files_named_in_the_skill_exist():
    text = (SKILL / "SKILL.md").read_text()
    for ref in set(re.findall(r"`((?:reference|assets)/[\w./-]+)`", text)):
        assert (SKILL / ref).exists(), f"SKILL.md names {ref}, which does not exist"


def test_american_spelling():
    british = re.compile(r"\b(colou?r(?:s|ed|ing|ways?)?)\b", re.I)
    for path in text_files():
        for number, line in enumerate(path.read_text().splitlines(), 1):
            for word in british.findall(line):
                assert word.lower().startswith("color"), f"{path.relative_to(ROOT)}:{number}: {word}"
            assert not re.search(r"\b(grey|licence|favour\w*|behaviour)\b", line, re.I), \
                f"{path.relative_to(ROOT)}:{number}: British spelling"


def test_starters_use_only_documented_colors():
    checks = load(ASSETS / "test_brand_colors.py", "brand_checks")
    for name in ("cwru-tokens.css", "theme.js"):
        found = {h.upper() for h in HEX.findall((ASSETS / name).read_text())}
        assert found <= checks.ALLOWED, f"{name}: {sorted(found - checks.ALLOWED)}"


def test_css_and_tailwind_theme_agree():
    css = (ASSETS / "cwru-tokens.css").read_text()
    root_block = css[css.index(":root {"):css.index("}", css.index(":root {"))]
    in_css = {h.upper() for h in HEX.findall(root_block)}
    in_theme = {h.upper() for h in HEX.findall((ASSETS / "theme.js").read_text())}
    assert in_css == in_theme, sorted(in_css ^ in_theme)


def test_documented_contrast_matches_the_calculation():
    """Rows like | CWRU Blue | `#003071` | 12.64 | ... | in color-and-contrast.md"""
    rows = re.findall(r"^\|[^|]+\|\s*`(#[0-9A-Fa-f]{6})`\s*\|\s*([\d.]+)\s*\|",
                      (SKILL / "reference" / "color-and-contrast.md").read_text(), re.M)
    assert len(rows) >= 10
    for hex_value, documented in rows:
        if hex_value.upper() == "#000000":
            continue
        assert contrast.ratio(hex_value, "#FFFFFF") == pytest.approx(float(documented), abs=0.011), hex_value


def test_the_known_pale_background_problem_is_still_true():
    for text in ("true", "copper", "bluegreen"):
        assert contrast.ratio(text, "white") >= 4.5
        assert contrast.ratio(text, "canvas") < 4.5


def test_manifests_and_changelog_agree():
    plugin = json.loads((ROOT / ".claude-plugin" / "plugin.json").read_text())
    market = json.loads((ROOT / ".claude-plugin" / "marketplace.json").read_text())
    assert market["plugins"][0]["name"] == plugin["name"]
    first = re.search(r"^## (\S+)", (ROOT / "CHANGELOG.md").read_text(), re.M).group(1)
    assert first == plugin["version"]


@pytest.mark.parametrize("fixture, should_pass", [("good", True), ("bad", False)])
def test_the_palette_check_catches_off_brand_colors(fixture, should_pass):
    env = {**os.environ, "BRAND_ROOT": str(ROOT / "tests" / "fixtures" / fixture)}
    result = subprocess.run(
        [sys.executable, "-m", "pytest", "-q", "-p", "no:cacheprovider", "-c", os.devnull,
         "--rootdir", str(ROOT), str(ASSETS / "test_brand_colors.py")],
        env=env, capture_output=True, text=True,
    )
    assert (result.returncode == 0) == should_pass, result.stdout[-800:]
