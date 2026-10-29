---
name: cwru-look-and-feel
description: Use when building or restyling a website, web app, or internal tool that must look like it belongs to Case Western Reserve University (CWRU) - colors, typeface, logo, header and footer, accessible color pairs, and CWRU voice in copy. Covers choosing and enforcing the CWRU palette, Open Sans as the stand-in for Arizona Sans, logo placement and clear space, program or unit accent colors, and a test that fails the build on off-brand colors. Use alongside a general design skill, not instead of one. Not for print, slides, or for deciding whether a unit may use the brand at all.
version: 0.1.0
user-invocable: true
argument-hint: "[setup | review | color | type | logo | copy] [target]"
---

Make a web interface read as a Case Western Reserve University product, and keep it that way as people change it. This skill is the **brand layer**. It says what CWRU permits. It does not say how to design well. For layout, hierarchy, critique, motion and accessibility craft, use a general design skill (for example `impeccable`) with this one: the general skill proposes, this one vetoes.

## Read this first: what is verified and what is not

- The rules below were checked against the CWRU Brand Guidelines PDF (140 pages; pages cited in the references) and <https://case.edu/brand/visual-identity/color>, and were worked through while building an internal CWRU web application. Guides get revised: before a launch, confirm against the current version. Questions and approvals go to University Marketing and Communications: **brand@case.edu**.
- The guide is written mostly for print and marketing. It names websites only briefly (Open Sans for "external affiliated websites", the digital logo minimum, the accessible color pairs). Anything it does not cover is marked **decision** below.
- Contrast ratios in this skill were computed (WCAG 2.x relative luminance), not copied.
- Where the guide says nothing (tints, a unit accent color), this skill says **"decision"** and names who should confirm. Do not present a decision as policy.
- Not bundled, on purpose: the logo artwork, the brand PDF and Arizona Sans. Each belongs to the university. Get them from University Marketing.

## Setup (once per project)

1. Ask which of these apply, in one message, before writing anything: Is there a unit or program that needs its own accent? Is Arizona Sans licensed for this project (almost always no)? Where will the logo come from? Is there an existing stylesheet or Tailwind config to adopt?
2. Copy the starters from `assets/` into the project and adjust paths:
   - `assets/cwru-tokens.css`: the palette as CSS variables, type roles, focus and selection. Plain CSS; works with any stack.
   - `assets/theme.js`: the same palette as Tailwind CDN colors, if the project uses Tailwind. Load it straight after the Tailwind script.
   - `assets/test_brand_colors.py`: a pytest check that fails on any color outside the palette. Adapt `ROOT` and `_ui_files()`. Port the idea to the project's test runner if it is not Python; keep the intent.
3. Self-host Open Sans (SIL Open Font License; ship `OFL.txt` with the files). Do not load it from a font CDN. See `reference/type-and-logo.md`.
4. Put the color tokens in **one** place and the test over it. Everything below depends on there being a single source of truth.

## The rules that matter most

**Palette: only the university palette, and tints of it.** "Do not use unapproved colors or alter the color palette." No Tailwind default scales (`bg-blue-600`), no "close enough" blues, no gradients other than the guide's.

| Role | Color | Hex |
|---|---|---|
| Primary | CWRU Blue | `#003071` |
| Secondary | CWRU Dark Blue | `#09143A` |
| Secondary | Force Blue | `#2359EF` |
| Secondary | CWRU True Blue | `#007AB8` |
| Secondary | CWRU Light Blue | `#A6D2E6` |
| Secondary | Black / Dark Gray / Light Gray | `#000000` / `#999999` / `#D3D3D3` |
| Tertiary | Copper Red / Orange / Blue Green / Violet Purple / Vivid Green | `#D63D1F` / `#FF9239` / `#377E72` / `#692C95` / `#61A530` |

**CWRU Blue leads.** Target mix: 45% CWRU Blue, 20% True Blue and Force Blue, 10% Light Blue, 10% Dark Blue, 10% neutrals, 5% tertiary. Secondary and tertiary colors never appear without CWRU Blue, and nothing overpowers it. Tertiary colors are for meaning (error, success, distinction), not decoration.

**Gradient:** the primary gradient runs Force Blue to CWRU Dark Blue (CWRU Blue falls in the middle), white text on it. The guide also defines warmer secondary gradients built on Force Blue; use them only with CWRU Blue clearly present. Gradients are expressive, not UI chrome: keep them to hero areas.

**Text on color: use approved pairs only.** The full table, with computed ratios, is in `reference/color-and-contrast.md`. The short version:
- Safe text on **white**: CWRU Blue, Dark Blue, Force Blue, True Blue, Blue Green, Copper Red, Violet Purple, black.
- **Never as text on white:** Light Gray, Dark Gray, Light Blue, Orange. Vivid Green only at 18pt and larger.
- White text works on CWRU Blue, Dark Blue, Force Blue, True Blue, Blue Green, Copper Red, Violet Purple.
- Light Blue and Light Gray text work **only** on CWRU Blue or Dark Blue.
- **No blue on black, no black on blue.**
- **Gotcha (computed, not in the guide):** True Blue (4.29:1), Copper Red (4.22:1) and Blue Green (4.37:1) pass on pure white but fall under 4.5:1 on a pale gray-blue page background such as `#F2F5F8`. If the page background is not white, keep those colors for fills with white text, or put the text on a white card.

**Type: Arizona Sans is the digital face; where the Arizona family is not available, Open Sans is the default, and where Google fonts are not possible, Arial.** Arizona Text is print-first (digital only at University Marketing's discretion); Arizona Flare Bold is for logos and pre-approved exceptions. The guide lists Open Sans in Light, Regular, Medium, Bold and Extra Bold, so build the type scale from those weights (300/400/500/700/800), not semibold 600. Hierarchy comes from contrasting weight and size, not from more colors or more fonts. Details and a size-matched Arial fallback are in `reference/type-and-logo.md`.

**Logo: official vector artwork only, never retyped or rebuilt.** The two-line horizontal logo is the primary one. Clear space is 50% of the height of the logo's square on every side; the digital minimum is 255 x 25 px. Use only the approved colorways: CWRU Blue on white (preferred), white on CWRU Blue, white on Force Blue, white on black, black on white, CWRU Blue on Light Gray. Never recolor it (True Blue on white, Light Blue on Dark Blue and Blue on True Blue are all on the guide's forbidden list); the sunburst inside it is always white. No drop shadows, rotation, distortion, cropping, image fills, or placing it inside body text. School lockups are **not for website use**, and all new logos or lockups are requested from University Marketing. A program's name is ordinary text beside the logo, not a lockup. The acronym logo may appear as a secondary mark in a footer only if the primary logo is at or near the top.

**Voice in copy:** the guide's voice is "charged, clear and catalytic", with five principles: driving, empowering, precise-not-puffed, radically optimistic, uniting. For a tool's interface, take the clear half and keep the energy light: active verbs, speak to "you", say more with less. The guide's don'ts are the useful test: no academic or institutional jargon, no soft generalities, nothing passive or bureaucratic ("remains committed to fostering ... where applicable"), no flat repeated sentence structure. "Force" is a campaign word: the guide says to avoid it as a generic descriptor and in everyday communications, so keep it out of buttons, labels and error messages. Say what happened and what to do next.

## Page frame that works

A pattern proven in production (see `reference/patterns.md` for markup):
- **Header:** a CWRU Blue band with the reversed (white) logo at left, the product and unit name as plain text beside it, navigation in white. A 4px rule along the bottom carries a unit or program accent if there is one.
- **Body:** white or a very light CWRU Blue tint; text in Dark Blue (not black); headings in CWRU Blue; primary buttons CWRU Blue with white text, hover to Dark Blue; focus ring Force Blue (Light Blue inside the blue band).
- **Footer:** CWRU Dark Blue with Light Gray text.
- **Sign-in or landing:** a CWRU Blue field, the reversed logo above a white card.
- **Status colors:** success Blue Green, error Copper Red, caution Orange (borders and fills only, never text), info Light Blue tint. Always pair color with an icon or words; never color alone.
- **Icons are drawn (SVG), never emoji.** Emoji are off-brand and read aloud by screen readers.

## Unit or program accent colors (a decision, not policy)

The guide does not define unit accents. One team's approach, allowed by a reading of "tertiary colors for distinction in a small share of a design": each unit gets one color from CWRU Blue, True Blue, Force Blue, Dark Blue or Violet Purple (all legible as text on white), shown only as a thin rule and a name, never as the main color. Validate it at startup so a typo cannot ship an off-brand color. **Whether units should differ by color at all is a question for University Marketing**; say so in the project's brief.

## Commands

- **setup**: run Setup above.
- **review [target]**: audit the target against this skill. Check, in order: colors outside the palette (run the test, then look for inline styles and SVG fills it cannot see); text/background pairs against the table; font stack and self-hosting; logo size, clear space and background; lockups or retyped marks; emoji used as icons; copy that is passive or puffed. Check any suspect text/background pair with `python assets/contrast.py <text-hex> <background-hex>`. Report findings as a short list ordered by how visible they are to the university, each with the file and the fix. Do not fix unless asked.
- **color [target]**: replace off-palette colors with palette roles (see the mapping hints in `reference/color-and-contrast.md`) and re-run the test.
- **type [target]**: apply the type roles and fallback stack.
- **logo [target]**: place the logo correctly; ask for the artwork if it is not in the project.
- **copy [target]**: rewrite user-facing text in the CWRU voice without changing meaning or adding claims.

## Working with a general design skill

When `impeccable` or a similar skill is installed, run it for the design work and apply this skill's constraints on top. Expect these conflicts and resolve them in the brand's favor:
- **Overused-font warnings on Open Sans.** Accepted: the guide names it as the required substitute. Record the exception with the reason in the design skill's ignore list so it is not re-litigated.
- **"Bolder" or "more distinctive" palette suggestions.** Out of bounds. Distinctiveness comes from layout, scale, weight, spacing and copy inside the palette.
- **Dark mode, extra accent colors and decorative illustration.** The guide covers none of these for interfaces: ask before adding. The guide's gradients and the sunburst (supplied artwork only, "when the primary logo is already present") are the sanctioned flourishes.
- **Fonts from a CDN.** Self-host instead.

## Finish

1. Run the color test. Fix every failure by changing the color, not by widening the allow-list. Widen the list only for a documented third-party mark (for example Google's multicolor "G" on a sign-in button, which Google's branding rules forbid recoloring), by adding its hex values for that one file to `THIRD_PARTY` in the test, with a comment saying why.
2. Check the page at phone width and desktop width. Text 16px or larger in inputs.
3. State plainly in the hand-off what is a substitution (Open Sans for Arizona Sans), what is a decision awaiting University Marketing (unit accents, tints), and what artwork is still needed (a white-on-transparent logo, if you cropped one).
