# Direction playbooks — complete aesthetic recipes

Each playbook is a coherent bundle: palette character, type, surface language, motion character, one signature element, and a kill-list. Pick ONE, execute everything from its row. Mixing playbooks is how designs become mud; varying playbooks BETWEEN projects is how you avoid converging on a house style.

Fonts reference typography.md's pairing table; surface numbers reference surfaces.md.

## Refined minimal / luxury
- **Palette**: warm tinted off-whites, ink text, ONE metallic-feeling accent (deep green, oxblood, gold-ochre) used scarcely. Dark variant: espresso/charcoal, not slate.
- **Surfaces**: layered hairlines (§1) + gradient rings (§2) + 3% grain. Radius small (6–10px) or none.
- **Type**: expressive serif display, geometric sans body, weight contrast extreme (300 vs 600).
- **Motion**: slow (600–1000ms), custom bezier, blur-in entrances. No bounce, ever.
- **Signature**: one oversized serif headline with tight tracking; hairline-ruled sections.
- **Kill-list**: drop shadows, bright saturated accents, bouncy springs, rounded-2xl.

## Brutalist / raw
- **Palette**: white/black + one shock accent (electric blue, signal red, acid yellow). No grays between — contrast is the system.
- **Surfaces**: flat planes, 2px solid black borders, hard offset shadows (`shadow-[6px_6px_0_#000]`), zero blur, radius 0.
- **Type**: Archivo Black/Anton display at huge sizes, mono labels, visible underlines.
- **Motion**: instant (≤150ms) or stepped (`steps()`); hover = invert colors or shift the offset shadow. No easing curves that feel "smooth".
- **Signature**: oversized type crashing into the grid; visible structure (borders on everything).
- **Kill-list**: gradients, soft shadows, glassmorphism, pastel anything, subtle animation.

## Editorial / magazine
- **Palette**: paper tones, ink, one print accent (vermilion, cobalt). Restrained.
- **Surfaces**: nearly flat; hairline rules, numbered sections, footnote styling. Generous margins.
- **Type**: THE hero — serif display + serif/sans body mix, drop caps, pull quotes, eyebrow labels, baseline discipline.
- **Motion**: scroll-driven reveals only; text appears like pages settling. ~400ms easeOut.
- **Signature**: asymmetric column grid with one full-bleed image; running section numbers (01/02/03).
- **Kill-list**: cards everywhere, heavy shadows, icon noise, bouncy interactions.

## Retro-futuristic / terminal
- **Palette**: near-black tinted background (phosphor green/amber or cyan/magenta on #0a0e12), scanline-dim neutrals.
- **Surfaces**: 1px glowing borders (`box-shadow: 0 0 12px var(--accent-tint)`), dot grids, CRT vignette, occasional dashed borders.
- **Type**: mono-forward (IBM Plex Mono, VT323 accents), uppercase labels with wide tracking, blinking caret.
- **Motion**: typewriter text, glitch on hover (sparingly), shimmer scanline sweep, stepped loaders (`▓▓▓░░`).
- **Signature**: live-feeling data readouts — timestamps, coordinates, status lines that tick.
- **Kill-list**: soft pastels, serif fonts, rounded-friendly shapes, slow gentle fades.

## Neumorphic / tactile toy
- **Palette**: one mid-lightness base hue family; accents as saturated "candy" fills.
- **Surfaces**: tactile shadows (§3) everywhere — every control visibly pressable; pill and squircle radii (12–24px).
- **Type**: rounded grotesque (Bricolage, Gabarito), chunky weights.
- **Motion**: springy (stiffness 400/damping 10), whileTap scale 0.95, hold-to-confirm, drag with rubber-banding.
- **Signature**: the press — active states that physically depress (inset shrink + instant transition).
- **Kill-list**: hairline elegance, flat ghost buttons, low-contrast text on busy fills.

## Glass / spatial
- **Palette**: deep atmospheric background (gradient mesh, aurora) with white/alpha foregrounds; one luminous accent.
- **Surfaces**: liquid glass (§5) panels over atmospheric backgrounds (§6); inset edge highlights; backdrop blur tiers (2px cards / 12px overlays).
- **Type**: clean geometric sans (Geist, Instrument Sans), light weights at large sizes.
- **Motion**: floating ambient loops, parallax layers, sheen sweeps on hover; medium-slow springs.
- **Signature**: depth — content visibly floating in layers above a living background.
- **Kill-list**: flat opaque cards, pure-white backgrounds, hard borders, brutalist type.

## Organic / natural
- **Palette**: earth ramp (moss, clay, sand, bark) + cream background; low chroma, warm.
- **Surfaces**: soft large radii, blob shapes (`border-radius: 40% 60% 55% 45%/55% 45% 60% 40%`), paper grain, hand-drawn underline SVGs.
- **Type**: humanist serif display (Fraunces soft), rounded sans body.
- **Motion**: slow drift, breathing scale loops (1.0→1.02), nothing mechanical.
- **Signature**: irregularity — one asymmetric blob mask or curved section divider.
- **Kill-list**: neon, hard grids visible, mono fonts, sharp corners, glitch effects.

## Industrial / utilitarian (pro dashboards)
- **Palette**: cool tinted neutrals, high-clarity status colors (ok/warn/crit), one brand accent. Dark-mode-first is legitimate here.
- **Surfaces**: shadow stacks (§4) + hairlines (§1), 4–8px radius, dense 4px-grid spacing.
- **Type**: condensed display for headers/KPIs, compact sans body, mono for all values/timestamps. `tabular-nums` everywhere.
- **Motion**: fast (150–250ms), functional only — state changes, count-ups, pulse on live data. Nothing decorative.
- **Signature**: information density done calmly — clear hierarchy at a glance. See data-viz.md.
- **Kill-list**: marketing-style heroes, slow entrances, decorative illustrations, oversized padding.

## Soft / pastel playful
- **Palette**: 2–3 pastels at equal lightness + dark text for contrast discipline; white space dominant.
- **Surfaces**: flat fills with subtle borders, sticker-like cards (white border + soft shadow), large radii.
- **Type**: friendly geometric (Sora, DM Sans), medium weights.
- **Motion**: gentle springs, staggered pop-ins (scale 0.9→1), wiggle on hover for fun elements only.
- **Signature**: charm in the details — custom empty states, playful microcopy, one mascot-ish shape.
- **Kill-list**: dark heavy shadows, aggressive contrast, corporate blue, dense layouts.

## Art deco / geometric
- **Palette**: black/cream + gold or jewel tone; metallic gradient used as hairline accents, not fills.
- **Surfaces**: symmetric frames, double-line borders, chevron/sunburst SVG patterns at low opacity, sharp + arch shapes.
- **Type**: high-contrast display (Marcellus, Poiret One), generous uppercase tracking, centered compositions allowed (the one direction where symmetry IS the move).
- **Motion**: reveal like curtains — clip-path wipes, line-draw SVG animations; stately timing.
- **Signature**: ornamental geometry framing content; numbered fine rules.
- **Kill-list**: casual rounded shapes, bouncy motion, lowercase headlines, gradient meshes.
