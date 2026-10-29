# cwru-look-and-feel

A [Claude Code](https://claude.com/claude-code) skill for building websites and web apps that look like they belong to Case Western Reserve University (CWRU).

It gives Claude the brand rules and the tools to keep to them: the color palette and which text and background pairs are accessible, Open Sans as the stand-in for Arizona Sans, logo placement and clear space, a header and footer pattern, CWRU voice for interface copy, and a test that fails your build when someone adds an off-brand color.

> **Unofficial.** This project is not made, reviewed or endorsed by Case Western Reserve University or its Marketing and Communications office. The university's name, logos and brand guidelines belong to the university. This repository contains none of its artwork, fonts or documents. When the rules here and the university's current guidelines differ, the guidelines win. Questions about brand use go to University Marketing and Communications (brand@case.edu).

## What it does

Ask Claude to build or restyle a page and mention CWRU, or invoke the skill directly. It will:

- **Set up** a project with color tokens (plain CSS and a Tailwind theme), type roles, focus styles and a page frame.
- **Review** existing work against the palette, approved text pairs, type, logo rules and copy, and list what to fix.
- **Enforce** the palette in your test suite, so it stays enforced after the first pass.
- **Check contrast** for any two colors from the command line.

It is the brand layer only. For layout, hierarchy and craft, use it with a general design skill (it has notes on working with [impeccable](https://impeccable.style)).

## Install

**As a plugin** (recommended; gets updates):

```
/plugin marketplace add kgweber-cwru/cwru-look-and-feel
/plugin install cwru-look-and-feel@cwru-look-and-feel
```

**As a plain skill** (no plugin system): copy `skills/cwru-look-and-feel/` into your project's `.claude/skills/` (shared with your team through git) or into `~/.claude/skills/` (just you).

Then ask for it by name, for example "use the cwru-look-and-feel skill to review `templates/`", or give a task that mentions CWRU branding and Claude will pick it up. A plugin's skills are namespaced by the plugin name.

## What is in the skill

| Path (under `skills/cwru-look-and-feel/`) | What |
|---|---|
| `SKILL.md` | The rules, the commands (`setup`, `review`, `color`, `type`, `logo`, `copy`), and how it works with a design skill |
| `reference/color-and-contrast.md` | Palette, approved text pairs with computed ratios, tints, proportions |
| `reference/type-and-logo.md` | Typefaces, self-hosting Open Sans, logo colorways and clear space |
| `reference/patterns.md` | Header, footer, buttons, status messages, error wording |
| `assets/cwru-tokens.css` | Palette, type roles, focus, page frame, buttons: plain CSS |
| `assets/theme.js` | The same palette for the Tailwind CDN |
| `assets/test_brand_colors.py` | pytest check for off-palette colors, emoji icons and font CDNs |
| `assets/contrast.py` | WCAG contrast of any two colors: `python contrast.py copper canvas` |

## How far to trust it

- The rules were checked against the CWRU Brand Guidelines PDF (a 140-page edition; page numbers are cited in the references) and <https://case.edu/brand/visual-identity/color>. Guidelines get revised, so confirm against the current edition before a launch.
- Contrast ratios are computed, not copied.
- The guide is written mostly for print and marketing. Where it is silent about the web (tints, unit accent colors, dark mode, the favicon), the skill says **decision** and does not present a guess as policy. Take those to University Marketing.
- One finding is the skill's own, not the guide's: True Blue, Copper Red and Blue Green text pass on white but fall under 4.5:1 on a pale gray-blue page background (`#F2F5F8`). The skill warns about it and `contrast.py` checks it.

## Not included, on purpose

The logo artwork, the brand guidelines PDF and Arizona Sans. Get them from University Marketing and Communications. Open Sans is under the SIL Open Font License; ship its `OFL.txt` with the font files.

## Contributing

Issues and pull requests are welcome, especially corrections against the current brand guidelines (cite the page) and fixes for stacks the starters do not cover.

```
python -m venv .venv && . .venv/bin/activate
pip install pytest
pytest
claude plugin validate .
```

`pytest` checks the skill itself: valid front matter, no broken file references, American spelling, and that the starter files agree with the documented palette and contrast numbers. Keep it passing, and raise the version in `.claude-plugin/plugin.json` and `CHANGELOG.md` for any change to the rules.

## License

[MIT](LICENSE) for this repository's text and code. It does not license any CWRU marks or materials.
