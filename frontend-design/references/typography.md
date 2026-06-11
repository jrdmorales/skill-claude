# Typography — type systems with character

Typography is the highest-leverage design decision: swap the fonts and the same layout reads as a different product. Generic AI output uses one neutral sans for everything; crafted products use a deliberate **pairing** plus a **scale**.

## Pairing logic

Pick ONE display voice + ONE quiet body workhorse. Contrast in personality, harmony in proportions (similar x-height):

- **Display** carries the aesthetic: expressive serif, condensed grotesque, mono, or geometric — used ONLY for headings/hero/numbers.
- **Body** disappears: high legibility at 14–16px, good weights (400/500/600).
- Optional **mono** for data, code, labels, timestamps — instant technical credibility.

Never more than 3 families. Often 2 weights of one family + a mono is enough.

## Pairings by direction (Google Fonts, all free)

Use as starting points — vary between projects, never default to the same pairing twice in a row:

| Direction | Display | Body | Mono/accent |
|-----------|---------|------|-------------|
| Luxury / refined | Cormorant Garamond, Fraunces (soft optical) | Outfit, Jost | — |
| Editorial / magazine | Newsreader, Playfair Display | Source Serif 4, PT Serif | Spline Sans Mono |
| Brutalist / raw | Archivo Black, Anton | Archivo, Space Grotesk* | Space Mono |
| Retro-futuristic / terminal | Major Mono Display, Unica One | IBM Plex Sans | IBM Plex Mono, VT323 (sparingly) |
| Industrial / dashboard | Barlow Condensed (display) | Barlow, Inter Tight* | JetBrains Mono, Geist Mono |
| Playful / toy-like | Bricolage Grotesque, Gabarito | Nunito Sans, Figtree | — |
| Organic / natural | Fraunces, Gelasio | Karla, Albert Sans | — |
| Art deco / geometric | Marcellus, Poiret One | Josefin Sans, Manrope | — |
| Soft / pastel | Sora, Quicksand (light) | DM Sans | — |
| Tech / spatial glass | Geist, Instrument Sans | same family lighter | Geist Mono |

*Asterisked picks are overused — only acceptable in a supporting role, never as the personality.

Loading: `<link rel="preconnect" href="https://fonts.googleapis.com">` + `display=swap`; request only the weights used. Prefer variable fonts when available.

## Scale — pick a ratio, stick to it

Choose by tone: **1.2** (minor third — dense pro tools), **1.25** (major third — balanced default), **1.333–1.5** (dramatic editorial/landing).

```css
:root {
  --text-xs: 0.75rem; --text-sm: 0.875rem; --text-base: 1rem;
  --text-lg: 1.25rem; --text-xl: 1.563rem; --text-2xl: 1.953rem;
  --text-3xl: 2.441rem; --text-4xl: 3.052rem;            /* ratio 1.25 */
  --text-hero: clamp(2.5rem, 1.2rem + 5vw, 5rem);        /* fluid hero */
}
```

Fluid `clamp()` for hero/display sizes only; body text stays fixed.

## Micro-rules that separate crafted from generic

- **Tracking**: large display → `letter-spacing: -0.02em` to `-0.04em` (`tracking-tight/tighter`). Uppercase labels/eyebrows → `+0.08em` to `+0.12em` + `text-xs` + `font-medium`. Never letter-space lowercase body.
- **Line height inversely proportional to size**: hero 0.95–1.1, headings 1.1–1.2, body 1.5–1.7, captions 1.4.
- **Measure**: body text 45–75ch (`max-w-prose` or `max-w-[65ch]`). Centered text blocks max ~3 lines.
- **Numbers that change** (timers, prices, metrics, tables): `font-variant-numeric: tabular-nums` — prevents jitter and misalignment.
- **Wrapping**: `text-wrap: balance` on headings, `text-wrap: pretty` on paragraphs; prevent orphans in heroes.
- **Hierarchy through contrast, not size alone**: combine weight (400 vs 650), color (`--fg` vs `--fg-muted`), and size. Two levels of muted is usually enough: `--fg`, `--fg-muted`, `--fg-subtle`.
- **OpenType**: enable `ss01`/`case`/`liga` when the font offers them (`font-feature-settings`); Fraunces' `SOFT`/`WONK` axes, optical sizing (`font-optical-sizing: auto`) for variable serifs.
- **Eyebrow pattern** (above hero H1): small caps/uppercase label + accent color or a 1px rule — instantly editorial.

## Anti-patterns

- Inter/Roboto/system-ui as the personality of the page.
- One font, one weight everywhere; size-only hierarchy.
- Letter-spaced lowercase; centered long paragraphs; 100ch lines.
- Hero set in `font-bold` default when the direction calls for 800/900 display weight or an expressive family.
