# Type and logo

## Typefaces

| Face | Use on the web |
|---|---|
| **Arizona Sans** (Light, Regular, Medium, Bold, italics) | "The primary font for digital communications" (guide p.87). Licensed; use it only if the project holds a license or University Marketing supplies it. |
| **Arizona Text** | Print. Digital only at University Marketing's discretion. |
| **Arizona Flare Bold** | Logos and exceptional cases approved in advance by University Marketing. Never UI type. |
| **Open Sans** | "The default font" where Arizona is not available (the guide's examples: emails, Google Slides, external affiliated websites; p.98). Listed weights: Light, Regular, Medium, Bold, Extra Bold. |
| **Arial** | "Where Google fonts are not possible, the default font is Arial." |

Default for most projects: **Open Sans, then Arial.** Say in the hand-off that this is a substitution so it can be swapped when Arizona Sans is obtained. Swapping should be a one-line change to the font stack and the `@font-face` block, which is why the stack lives in one place.

### Self-hosting Open Sans

- Download the variable `latin` and `latin-ext` WOFF2 files (normal and italic) from Google Fonts' open-source repository or `@fontsource-variable/open-sans`. License: SIL Open Font License 1.1. **Ship `OFL.txt` next to the files.**
- Do not link `fonts.googleapis.com`. It sends visitors' addresses to a third party and adds a failure point; the test in `assets/test_brand_colors.py` can check for it.
- `font-display: swap`, plus a size-matched Arial fallback so text does not jump when the font arrives. `assets/cwru-tokens.css` includes the `@font-face` blocks and the fallback metrics (`size-adjust: 105.64%`, `ascent-override: 101.18%`, `descent-override: 27.73%`).

### Hierarchy

Contrast weight and size; do not add colors or faces to make hierarchy.

- Weights: 400 text, 500 labels and sections, 700 titles. These are weights the guide lists. (Open Sans has a 600 weight, but the guide does not list it. Prefer 500.)
- Scale about 1.25: 0.75 / 0.8125 / 0.875 / 1 / 1.125 / 1.25 / 1.5 / 1.875 / 2.5 rem.
- Body 16px everywhere including phones; form inputs 16px minimum so iOS does not zoom.
- Line height about 1.6 for body; reading width capped near 68 characters.
- Titles in CWRU Blue, body in Dark Blue, one title per page. Use named roles (`type-title`, `type-section`, `type-label`, `type-meta`) rather than ad hoc sizes, so the scale cannot drift.
- Tabular figures (`font-variant-numeric: tabular-nums`) for times, counts and versions.

## Logo

- **Artwork:** the official two-line horizontal logo, as supplied (p.52: "should not be recreated by retyping. Use the official vector artwork"). There are five configurations (two-line horizontal, four-line, four-line stacked, four-line centered, acronym); the two-line is primary and fits a header. Never retype, redraw, recolor, stretch or add effects. If the project only has a blue-on-white logo and needs a reversed one, ask University Marketing for a white-on-transparent file. Cropping the supplied "white on CWRU Blue" artwork works but fixes its background to CWRU Blue, so it can only sit on that exact color; say so in the hand-off.
- **Colorways (pp.68-69):** CWRU Blue on white (preferred when legible), white on CWRU Blue, white on Force Blue, white on black, black on white, CWRU Blue on Light Gray. Forbidden: True Blue on white or on Light Blue, CWRU Blue on True Blue, CWRU Blue on Dark Gray or Copper Red, Light Blue on white or Dark Blue, black on True Blue or Dark Gray, outlined logos, any tertiary on another tertiary. The sunburst inside the logo is always white. Do not change the color of official logo vectors.
- **Never (pp.70-71):** alter or crop, put inside body text, add a drop shadow, rearrange, rotate, distort, redraw, fill with an image, or make unapproved lockups.
- **Background:** not over a pattern or photograph (the guide asks that the logo stay fully legible). On the gradient, over its darker part (decision: the guide shows the logo on solid colors).
- **Size:** at least **255 x 25 px** on screen. Check the rendered size, not the file size.
- **Clear space:** half the height of the logo's square, on every side. Nothing (text, rules, buttons) enters it. Crop the clear space into the image file or reproduce it with padding; do not eyeball it.
- **Alt text:** "Case Western Reserve University". Link it to the product's home.
- **Lockups:** school lockups (such as "School of Medicine" set under the logo) are "not for website usage" (p.115); all new logos are requested through University Marketing and Communications. Until then, put the unit's name next to the logo as plain text in the product's type.
- **Sunburst:** a secondary device "in applications that require further expression of the brand", from provided artwork only, "when the primary logo is already present" (p.116). The sunburst with a border is always white. Use sparingly.
- **Acronym logo:** a less formal secondary mark; on a web page it may appear in the footer if a primary logo is at or near the top.
- **Favicon:** the guide is silent. An emoji favicon is a stopgap; ask University Marketing for an approved mark.
- **Name:** keep the product name distinct from the university's. Do not imply the product is the university's own website unless it is.
