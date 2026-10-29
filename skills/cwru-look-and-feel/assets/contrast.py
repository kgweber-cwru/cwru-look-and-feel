#!/usr/bin/env python3
"""WCAG 2.x contrast ratio of two colors.

    python contrast.py '#D63D1F' '#F2F5F8'
    python contrast.py copper canvas            # palette names work too
    python contrast.py --table '#F2F5F8'        # every palette color as text on a background

Exits 1 when the ratio is under 4.5:1 (the bar for body text), so it can gate a script.
Ratios for UI components and large text (18pt, or 14pt bold) need only 3:1.
"""

import sys

NAMES = {
    "blue": "#003071", "dark": "#09143A", "force": "#2359EF", "true": "#007AB8",
    "light": "#A6D2E6", "lightgray": "#D3D3D3", "darkgray": "#999999",
    "bluegreen": "#377E72", "copper": "#D63D1F", "orange": "#FF9239",
    "violet": "#692C95", "vivid": "#61A530", "white": "#FFFFFF", "black": "#000000",
    "canvas": "#F2F5F8", "notice": "#EDF6FA", "danger-tint": "#FBECE9",
    "success-tint": "#EBF2F1", "caution-tint": "#FFF2E7",
}


def parse(value):
    value = NAMES.get(value.lower(), value).lstrip("#")
    if len(value) == 3:
        value = "".join(ch * 2 for ch in value)
    if len(value) != 6:
        raise SystemExit(f"not a color: {value!r}")
    return tuple(int(value[i:i + 2], 16) / 255 for i in (0, 2, 4))


def luminance(rgb):
    r, g, b = (c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4 for c in rgb)
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def ratio(a, b):
    hi, lo = sorted((luminance(parse(a)), luminance(parse(b))), reverse=True)
    return (hi + 0.05) / (lo + 0.05)


def main(argv):
    if len(argv) == 3 and argv[1] == "--table":
        for name in NAMES:
            r = ratio(name, argv[2])
            print(f"{name:13} {r:6.2f}  {'ok' if r >= 4.5 else 'under 4.5' if r >= 3 else 'under 3'}")
        return 0
    if len(argv) != 3:
        print(__doc__)
        return 2
    r = ratio(argv[1], argv[2])
    verdict = "passes body text (4.5:1)" if r >= 4.5 else (
        "large text and UI components only (3:1)" if r >= 3 else "fails")
    print(f"{r:.2f}:1  {verdict}")
    return 0 if r >= 4.5 else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))
