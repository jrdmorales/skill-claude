---
name: frontend-design
description: Create distinctive, production-grade frontend interfaces with exceptional design quality. Use this skill whenever the user asks to build, style, animate, or improve ANY web UI — websites, landing pages, dashboards, React/Vue components, HTML/CSS layouts, widgets, posters, artifacts — or mentions things like "make it look better", "add animations", "polish the UI", "design a component", typography, color palettes, dark mode, micro-interactions, charts, or visual effects, even if they don't say "design" explicitly. Produces creative, polished code that avoids generic AI aesthetics.
license: Complete terms in LICENSE.txt
---

# Frontend Design

This skill guides creation of distinctive, production-grade frontend interfaces that avoid generic "AI slop" aesthetics. The techniques are distilled from studying design-engineering component libraries (KokonutUI, Cult UI, and the shadcn ecosystem): real spring physics values, layered-surface recipes, complete aesthetic playbooks, and interaction patterns that ship in production.

The deliverable is always **real working code** — never a mockup description.

## Reference files — read what the task needs

| File | Read it when |
|------|--------------|
| `references/directions.md` | ALWAYS at the start — 10 complete aesthetic playbooks (palette + type + surfaces + motion + signature + kill-list). Pick one, execute its whole row. |
| `references/typography.md` | Choosing fonts, building a type scale, anything text-heavy. Pairings by direction, micro-rules (tracking, measure, tabular-nums). |
| `references/color.md` | Defining tokens/palette, dark mode, gradients. Semantic token architecture in OKLCH, ramp construction, contrast rules. |
| `references/layout.md` | Page structure, spacing, responsive work. Compositional moves, grid recipes, container queries, z-axis discipline. |
| `references/surfaces.md` | Styling cards, buttons, panels, backgrounds — depth/texture/glass recipes (layered hairlines, tactile shadows, liquid glass, generative backgrounds). |
| `references/motion.md` | ANY animation: entrances, hovers, loaders, text effects, mouse-tracking. Spring presets, choreography rules, CSS-only equivalents. |
| `references/components.md` | Interactive components, forms, icons, or a component library. Pattern catalog + engineering standards (CVA, compound components, full ARIA). |
| `references/data-viz.md` | Dashboards, charts, tables, monitoring/telemetry UIs, KPI cards, live data, empty/loading/error states. |

Minimum read for any visual task: `directions.md` + the 2–3 files matching the work. They are short and dense; skipping them produces flat, generic output.

`scripts/check_contrast.py` — run it on the final token set (both modes): `python scripts/check_contrast.py fg=#222 bg=#fafaf5 accent=#c2410c` → ratio + WCAG grade per pair.

## Design thinking — before any code

Commit to a BOLD, specific aesthetic direction:

- **Purpose**: What problem does this interface solve? Who uses it, and in what state of mind?
- **Tone**: Pick ONE playbook from `references/directions.md`. Don't average between flavors; execute one with precision.
- **Constraints**: Framework, performance budget, accessibility, existing brand.
- **Differentiation**: Name the ONE thing someone will remember — a signature interaction, a striking background, an unexpected layout. Build the design around it.

Intentionality beats intensity: refined minimalism executed precisely outranks busy maximalism executed sloppily — and vice versa. Match implementation complexity to the vision.

## The workflow

Work in this order — it prevents the most common failure mode (decorating a weak structure):

1. **Direction** — pick the playbook and the memorable element.
2. **Tokens** — CSS variables first: semantic colors with light AND dark values (`color.md`), type pairing + scale (`typography.md`), radius and spacing rhythm (`layout.md`). Every later choice references tokens; never hardcode one-off values mid-component.
3. **Structure** — layout and hierarchy with real content; one deliberate compositional move (`layout.md`).
4. **Surfaces** — depth/texture per `surfaces.md`. This is where "flat AI demo" becomes "crafted product".
5. **Motion** — choreograph last, per `motion.md`. One orchestrated entrance plus purposeful micro-interactions beats scattered effects.
6. **Verify** — quality bar below + contrast script. If a browser/screenshot tool is available, render and LOOK at the result in both modes and at 360px width before delivering; fix what looks wrong, don't rationalize it.

## Self-review rubric

Before delivering, score the work honestly (1–5) on: distinctiveness (would you recognize it among five AI outputs?), cohesion (does every element obey the chosen playbook?), craft (tokens, spacing rhythm, dark mode, states), and restraint (is anything there that doesn't earn its place?). Anything under 4 → revise that axis before shipping. The kill-list of the chosen playbook is part of the review.

## Quality bar (verify before delivering)

- [ ] Both color modes work; every surface, border, and shadow has a dark-mode pair.
- [ ] Contrast verified with `scripts/check_contrast.py` — body ≥ 4.5:1, large/UI ≥ 3:1, both modes.
- [ ] Interactive elements have hover, active, focus-visible, and disabled states.
- [ ] Hover effects gated for hover-capable devices; touch targets ≥ 44px.
- [ ] `prefers-reduced-motion` respected (`motion-reduce:` classes or `useReducedMotion`).
- [ ] Animations touch only `transform`, `opacity`, `filter` — never layout properties.
- [ ] Custom interactive widgets have ARIA roles, labels, and keyboard handlers.
- [ ] Text over imagery/gradients keeps contrast; decorative layers are `pointer-events-none aria-hidden`.
- [ ] No hardcoded one-off values where a token exists; spacing follows the established rhythm.
- [ ] Empty, loading, and error states designed (not defaulted) for anything data-driven.

## NEVER ship generic AI aesthetics

- Purple-gradient-on-white hero with Inter and three identical feature cards.
- Evenly-distributed timid palettes; gray-on-white "clean" defaults with no point of view; pure-gray neutrals next to a colored accent.
- Uniform `rounded-lg` cards with a single `box-shadow` floating on flat backgrounds.
- Emoji as icons; placeholder-feeling copy ("Lorem", "Feature 1"); library-default chart colors and tooltips.
- The same fonts, layout skeletons, and component shapes across different projects — every design should feel made for its context. Vary playbooks, type pairings, and light/dark themes between generations.

Interpret creatively and make unexpected choices that feel genuinely designed for the context. Claude is capable of extraordinary creative work — commit fully to a distinctive vision and execute it with engineering precision.
