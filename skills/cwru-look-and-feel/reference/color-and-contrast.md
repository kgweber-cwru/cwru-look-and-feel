# Color and contrast

Ratios below are WCAG 2.x contrast, computed from the hex values. The guide's own approved pairs come first; ratios are there to show the margin.

## Contrast against white and against CWRU Blue

| Color | Hex | On white | White on it |
|---|---|---|---|
| Black | `#000000` | 21.0 | 21.0 |
| CWRU Dark Blue | `#09143A` | 17.91 | 17.91 |
| CWRU Blue | `#003071` | 12.64 | 12.64 |
| Violet Purple | `#692C95` | 8.77 | 8.77 |
| Force Blue | `#2359EF` | 5.60 | 5.60 |
| Blue Green | `#377E72` | 4.78 | 4.78 |
| True Blue | `#007AB8` | 4.69 | 4.69 |
| Copper Red | `#D63D1F` | 4.62 | 4.62 |
| Vivid Green | `#61A530` | 3.03 | 3.03 (large text only, 18pt+) |
| Dark Gray | `#999999` | 2.85 | not allowed |
| Orange | `#FF9239` | 2.23 | not allowed |
| Light Blue | `#A6D2E6` | 1.62 | not allowed |
| Light Gray | `#D3D3D3` | 1.50 | not allowed |

On a dark brand background: Light Blue on CWRU Blue 7.82, Light Blue on Dark Blue 11.07, Light Gray on CWRU Blue 8.44. CWRU Blue on Light Blue 7.82. Dark Blue on Light Gray 11.96.

## Approved pairs (screen), from the guide (pp.78-83)

Allowed: black, CWRU Blue, Dark Blue, True Blue or Force Blue on white; white on black, CWRU Blue, Dark Blue, True Blue or Force Blue; CWRU Blue, Dark Blue or black on Light Gray; Light Gray on CWRU Blue, Dark Blue or black; Light Blue on CWRU Blue or Dark Blue; CWRU Blue or Dark Blue on Light Blue; Blue Green, Copper Red or Violet Purple on white, and white on them; Vivid Green on white and white on Vivid Green at 18pt and larger only.

Other pairs in the guide (black on Orange, Copper Red, the grays or Light Blue) are **for print only**.

**Not allowed on screen:** Light Gray, Dark Gray, Light Blue, Orange or (below 18pt) Vivid Green on white, and white on those; any blue on black, or black on any blue; Copper Red on black, or black on Copper Red.

## Tints

The guide allows tints "where appropriate" and gives no values. These were derived by mixing a palette color with white and are a **decision**; confirm with University Marketing if the project is high-profile.

| Role | Hex | Made from | Use | Text on it |
|---|---|---|---|---|
| canvas | `#F2F5F8` | CWRU Blue 5% | page background | Blue, Dark Blue, ink-muted, ink-subtle only (see gotcha) |
| notice | `#EDF6FA` | Light Blue 20% | quiet surfaces, hover | same |
| notice-hover | `#DBEDF5` | Light Blue 40% | hover on notice | same |
| ink-muted | `#4E5671` | Dark Blue 72% | secondary text (7.3:1 on white) | |
| ink-subtle | `#666D85` | Dark Blue 62% | meta text, placeholders (5.1:1) | |
| line | `#D3D3D3` | Light Gray | dividers | |
| line-strong | `#848A9C` | Dark Blue 50% | input borders (3.4:1, meets the 3:1 for UI components) | |
| success-tint | `#EBF2F1` | Blue Green 10% | success surface | |
| danger-tint | `#FBECE9` | Copper Red 10% | error surface | |
| caution-tint | `#FFF2E7` | Orange 12% | caution surface | |

**Gotcha: pale backgrounds.** On `#F2F5F8`, True Blue is 4.29:1, Copper Red 4.22:1 and Blue Green 4.37:1, all under 4.5. Either use a white page, or put those colors' text on white cards, or use them only as fills behind white text.

If you add a tint, add it to the test's allow-list **with its source color and percentage in a comment**, and check body-text pairs yourself.

## Mapping common off-brand colors

| Seen in the wild | Use |
|---|---|
| any primary blue (`#1565c0`, `blue-600`) | CWRU Blue `#003071` |
| bright link or focus blue (`#2563eb`) | Force Blue `#2359EF` |
| teal/sky/cyan accents | True Blue `#007AB8` |
| near-black body text, `gray-900` | CWRU Dark Blue `#09143A` |
| `gray-500` secondary text | ink-muted `#4E5671` |
| `gray-200` borders | Light Gray `#D3D3D3` |
| `green-600` success | Blue Green `#377E72` |
| `red-600` error | Copper Red `#D63D1F` |
| `yellow/amber` warning | Orange `#FF9239`, as border or fill, never text |
| purple highlights | Violet Purple `#692C95` (tertiary; keep under ~5%) |

## Checks the color test cannot do

The starter test scans hex values and Tailwind default classes. It does not see `rgb()`/`hsl()`/named colors, colors built in JavaScript, SVG `fill` set by class, images, or third-party widgets. Grep for those in a review. It also cannot judge proportion: look at the page and ask whether CWRU Blue is plainly the dominant color.

## Proportions (p.76)

45% CWRU Blue, 20% True Blue and Force Blue combined, 10% Light Blue, 10% Dark Blue, 10% neutrals, 5% tertiary. "The overall impression of the brand should be unambiguously CWRU Blue, with the other colors serving as accents." Integrity rules (p.83): no secondary or tertiary color without CWRU Blue; use the approved ratios; no unapproved colors or altered palette; nothing overpowers CWRU Blue.
