"""The interface uses CWRU colors only.

Case Western's brand guidelines allow only the university palette (and tints of it).
These tests fail the build on a hex color or Tailwind default color class outside it,
on emoji used as icons, and on a font loaded from a CDN.

To adopt: set UI_GLOBS to where your templates, scripts and styles live (relative to
the project root), and ROOT if this file is not in <root>/tests/. They cannot see
rgb()/hsl()/named colors, colors built in JavaScript, images or third-party widgets;
review those by hand.
"""

import os
import re
from pathlib import Path

import pytest

ROOT = Path(os.environ.get("BRAND_ROOT", Path(__file__).resolve().parent.parent))

# Where interface code lives. Edit for your project.
UI_GLOBS = [
    "templates/**/*.html",
    "static/**/*.css",
    "static/**/*.js",
    "src/**/*.{css,js,jsx,ts,tsx,html,vue,svelte}",
]

# The university palette (https://case.edu/brand/visual-identity/color)
PALETTE = {
    "#003071",  # CWRU Blue
    "#09143A",  # CWRU Dark Blue
    "#2359EF",  # Force Blue
    "#007AB8",  # CWRU True Blue
    "#A6D2E6",  # CWRU Light Blue
    "#D3D3D3",  # Light Gray
    "#999999",  # Dark Gray
    "#377E72",  # Blue Green
    "#D63D1F",  # Copper Red
    "#FF9239",  # Orange
    "#692C95",  # Violet Purple
    "#61A530",  # Vivid Green
}
# Tints: each a palette color mixed with white. Add one only with its source color
# and percentage, and check body-text contrast (reference/color-and-contrast.md).
TINTS = {
    "#F2F5F8",  # canvas: CWRU Blue 5%
    "#4E5671",  # ink-muted: Dark Blue 72%
    "#666D85",  # ink-subtle: Dark Blue 62%
    "#848A9C",  # line-strong: Dark Blue 50%
    "#EDF6FA",  # notice: Light Blue 20%
    "#DBEDF5",  # notice-hover: Light Blue 40%
    "#EBF2F1",  # success-tint: Blue Green 10%
    "#FBECE9",  # danger-tint: Copper Red 10%
    "#FFF2E7",  # caution-tint: Orange 12%
}
# Third-party marks that must not be recolored, keyed by file name. The usual case is
# Google's multicolor "G" on a "Sign in with Google" button: Google's branding rules
# forbid recoloring it, so its four hex values are exempt in that one file. Without an
# entry like the example below, this test fails on that file. Say why in a comment, and
# never widen ALLOWED instead.
THIRD_PARTY = {
    # "login.html": {"#4285F4", "#34A853", "#FBBC05", "#EA4335"},  # Google "G" mark
}
ALLOWED = PALETTE | TINTS

BLACK_WHITE = {"#FFF", "#FFFFFF", "#000", "#000000"}
HEX = re.compile(r"#[0-9A-Fa-f]{6}\b|#[0-9A-Fa-f]{3}\b(?![0-9A-Fa-f])")
TAILWIND_SCALE = re.compile(
    r"\b(?:bg|text|border|ring|ring-offset|from|via|to|divide|outline|placeholder|"
    r"accent|fill|stroke|shadow|decoration|caret)-"
    r"(?:slate|gray|zinc|neutral|stone|red|orange|amber|yellow|lime|green|emerald|"
    r"teal|cyan|sky|blue|indigo|violet|purple|fuchsia|pink|rose)-\d{2,3}\b"
)
EMOJI = re.compile("[\U0001F300-\U0001FAFF☀-➿⭐]")
FONT_CDN = re.compile(r"fonts\.googleapis\.com|fonts\.gstatic\.com|use\.typekit\.net")


def _expand(pattern):
    # Path.glob has no brace expansion
    m = re.search(r"\{([^}]+)\}", pattern)
    if not m:
        return [pattern]
    return [pattern[: m.start()] + alt + pattern[m.end():] for alt in m.group(1).split(",")]


def _ui_files():
    found = set()
    for glob in UI_GLOBS:
        for pattern in _expand(glob):
            found.update(p for p in ROOT.glob(pattern) if p.is_file())
    return sorted(found)


def _rel(path):
    # pytest passes a placeholder when FILES is empty; the "found some files" test
    # below then reports the real problem
    return path.relative_to(ROOT).as_posix() if isinstance(path, Path) else str(path)


FILES = _ui_files()


def test_some_interface_files_were_found():
    """A wrong UI_GLOBS would otherwise make every check below pass by checking nothing."""
    assert FILES, f"UI_GLOBS matched no files under {ROOT}; edit it for this project"


@pytest.mark.parametrize("path", FILES, ids=_rel)
def test_no_tailwind_default_colors(path):
    found = TAILWIND_SCALE.findall(path.read_text())
    assert not found, f"{_rel(path)} uses Tailwind colors outside the CWRU palette: {found}"


@pytest.mark.parametrize("path", FILES, ids=_rel)
def test_hex_colors_are_cwru(path):
    allowed = ALLOWED | THIRD_PARTY.get(path.name, set())
    found = {h.upper() for h in HEX.findall(path.read_text())} - BLACK_WHITE
    stray = sorted(found - allowed)
    assert not stray, f"{_rel(path)} uses colors outside the CWRU palette: {stray}"


@pytest.mark.parametrize("path", FILES, ids=_rel)
def test_no_emoji_as_icons(path):
    """Emoji are off-brand and read aloud by screen readers; draw icons as SVG. A
    favicon line is the one exception."""
    lines = [l for l in path.read_text().splitlines() if 'rel="icon"' not in l]
    found = sorted({ch for l in lines for ch in EMOJI.findall(l)})
    assert not found, f"{_rel(path)} uses emoji: {found}"


@pytest.mark.parametrize("path", FILES, ids=_rel)
def test_fonts_are_self_hosted(path):
    assert not FONT_CDN.search(path.read_text()), f"{_rel(path)} loads a font from a CDN"
