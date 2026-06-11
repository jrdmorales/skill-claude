#!/usr/bin/env python3
"""WCAG 2.x contrast checker for color token pairs.

Usage:
    python check_contrast.py "#1a1a2e" "#e0e0f0"            # one pair
    python check_contrast.py fg=#222 bg=#fafaf5 accent=#c2410c bg2=#16161d
        (named values: every value whose name starts with 'fg'/'accent'/'text'
         is checked against every value whose name starts with 'bg'/'surface')

Exit code 0 if all checked pairs pass AA (4.5:1), 1 otherwise.
No dependencies. Accepts #rgb, #rrggbb, rgb(r,g,b).
"""

import re
import sys


def parse_color(value: str) -> tuple[float, float, float]:
    value = value.strip().lower()
    m = re.fullmatch(r"#?([0-9a-f]{3})", value)
    if m:
        return tuple(int(c * 2, 16) / 255 for c in m.group(1))  # type: ignore[return-value]
    m = re.fullmatch(r"#?([0-9a-f]{6})", value)
    if m:
        h = m.group(1)
        return tuple(int(h[i : i + 2], 16) / 255 for i in (0, 2, 4))  # type: ignore[return-value]
    m = re.fullmatch(r"rgba?\(\s*(\d+)\s*,\s*(\d+)\s*,\s*(\d+)", value)
    if m:
        return tuple(min(int(g), 255) / 255 for g in m.groups())  # type: ignore[return-value]
    raise ValueError(f"Unsupported color format: {value!r} (use hex or rgb())")


def relative_luminance(rgb: tuple[float, float, float]) -> float:
    def channel(c: float) -> float:
        return c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4

    r, g, b = (channel(c) for c in rgb)
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def contrast_ratio(c1: str, c2: str) -> float:
    l1 = relative_luminance(parse_color(c1))
    l2 = relative_luminance(parse_color(c2))
    lighter, darker = max(l1, l2), min(l1, l2)
    return (lighter + 0.05) / (darker + 0.05)


def grade(ratio: float) -> str:
    if ratio >= 7.0:
        return "AAA"
    if ratio >= 4.5:
        return "AA"
    if ratio >= 3.0:
        return "AA-large/UI only"
    return "FAIL"


def main(argv: list[str]) -> int:
    args = argv[1:]
    if len(args) < 2:
        print(__doc__)
        return 2

    pairs: list[tuple[str, str, str]] = []  # (label, fg, bg)

    if all("=" in a for a in args):
        named = dict(a.split("=", 1) for a in args)
        fgs = {k: v for k, v in named.items() if k.startswith(("fg", "accent", "text"))}
        bgs = {k: v for k, v in named.items() if k.startswith(("bg", "surface"))}
        if not fgs or not bgs:
            print("Named mode needs at least one fg*/accent*/text* and one bg*/surface* value.")
            return 2
        for fk, fv in fgs.items():
            for bk, bv in bgs.items():
                pairs.append((f"{fk} on {bk}", fv, bv))
    else:
        if len(args) % 2 != 0:
            print("Positional mode needs pairs of colors: fg bg [fg bg ...]")
            return 2
        for i in range(0, len(args), 2):
            pairs.append((f"{args[i]} on {args[i + 1]}", args[i], args[i + 1]))

    all_aa = True
    width = max(len(p[0]) for p in pairs)
    for label, fg, bg in pairs:
        try:
            ratio = contrast_ratio(fg, bg)
        except ValueError as exc:
            print(f"{label:<{width}}  ERROR: {exc}")
            all_aa = False
            continue
        g = grade(ratio)
        if g not in ("AA", "AAA"):
            all_aa = False
        print(f"{label:<{width}}  {ratio:5.2f}:1  {g}")

    return 0 if all_aa else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))
