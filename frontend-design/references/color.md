# Color — token architecture & palette craft

Color failures in generated UIs are structural, not aesthetic: hardcoded hex values scattered through markup, gray defaults with no point of view, and dark mode as an afterthought. Fix the structure first.

## Semantic token architecture

Define ALL color as semantic CSS variables at `:root` / `.dark`. Components reference roles, never raw values:

```css
:root {
  --background: oklch(0.98 0.005 95);      /* tinted, never pure white */
  --surface: oklch(1 0 0);
  --surface-raised: oklch(1 0 0);          /* + shadow does the lifting */
  --border: oklch(0.91 0.01 95);
  --border-strong: oklch(0.85 0.012 95);
  --fg: oklch(0.22 0.015 95);
  --fg-muted: oklch(0.45 0.012 95);
  --fg-subtle: oklch(0.60 0.01 95);
  --accent: oklch(0.62 0.19 35);           /* the personality */
  --accent-fg: oklch(0.99 0.01 35);        /* text ON accent */
  --accent-muted: oklch(0.94 0.05 35);     /* tints, hovers, selected bg */
  --ok: oklch(0.65 0.15 150); --warn: oklch(0.75 0.15 85); --crit: oklch(0.60 0.20 25);
  --radius: 12px;
}
.dark {
  --background: oklch(0.16 0.012 95);      /* tinted, never #000 or pure gray */
  --surface: oklch(0.20 0.014 95);
  --surface-raised: oklch(0.24 0.016 95);  /* elevation = lighter, not shadow */
  --border: oklch(0.28 0.015 95);
  --fg: oklch(0.93 0.008 95);
  --fg-muted: oklch(0.70 0.012 95);
  --accent: oklch(0.70 0.17 35);           /* lighter & slightly desaturated */
}
```

Rules encoded above, applied always:

- **Neutrals are tinted** toward the accent hue (the constant hue channel, e.g. `95` here). Pure grays look dead next to any accent.
- **Dark mode is not inversion**: backgrounds get the same hue at low lightness; accents go LIGHTER and slightly less chromatic (saturated colors vibrate on dark); elevation switches from shadows to lighter surfaces + inset top highlights (see surfaces.md).
- Tailwind: map tokens in config/`@theme` so utilities stay semantic (`bg-surface`, `text-fg-muted`).

## Building the palette

1. **One dominant** (often the tinted neutral family) + **one sharp accent** + semantic status colors. 60-30-10 distribution: timid evenly-spread palettes are the #1 generic tell.
2. Work in **OKLCH** (perceptually uniform): ramps = vary L (0.97 → 0.20) holding C and H roughly constant; drop C slightly at the extremes. This gives even steps that HSL cannot.
3. **Hue-shift the depths**: shadows and dark ramp steps rotate hue slightly toward blue/violet; highlights toward yellow — this is what makes palettes feel "expensive".
4. Statement options per direction: monochrome + single accent (brutalist), analogous warm (organic), high-chroma duotone (playful), desaturated + metallic neutrals (luxury). Commit; don't sprinkle five hues.

## Gradients

- Same-hue lightness gradients for surfaces (`from-neutral-100 to-white`), analogous hues for atmosphere; avoid complementary-hue gradients on UI chrome (muddy midpoint).
- Long gradients need easing: add intermediate stops or a noise overlay (surfaces.md §6) to prevent banding.
- Text gradients: keep both stops within contrast range of the background.

## Contrast (verify, don't eyeball)

- Body text ≥ 4.5:1; large text (≥24px / 19px bold) ≥ 3:1; UI components & borders of inputs ≥ 3:1 against adjacent colors.
- `--fg-muted` must still clear 4.5:1; "subtle" is for captions/disabled only.
- Run the bundled checker: `python scripts/check_contrast.py "#1a1a2e" "#e0e0f0"` — accepts pairs, prints ratio + pass/fail for each WCAG level. Check every fg/bg pair in the token set, both modes.
- Never rely on color alone for status — pair with icon/shape/label (color-blind users).

## Application details

- Focus rings: `outline: 2px solid var(--accent); outline-offset: 2px` — visible in BOTH modes (a dark-on-dark focus ring is a real bug, not polish).
- Selection color: `::selection { background: var(--accent-muted) }` — tiny, memorable.
- `color-scheme: light dark` on `:root` so native controls/scrollbars match.
- Overlays: `backdrop-brightness`/scrims sized to keep overlaid text ≥ 4.5:1.
- `accent-color: var(--accent)` for native checkboxes/radios/progress.
