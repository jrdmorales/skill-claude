# Layout — composition, rhythm, responsiveness

Generic AI layouts are symmetric, centered, evenly padded, and identical across projects. Crafted layouts make ONE deliberate compositional move and keep everything else disciplined.

## Spacing rhythm

- Base unit 4px; component spacing from a fixed scale (4/8/12/16/24/32/48/64/96/128). Define `--space-*` tokens or use Tailwind's scale consistently — mixed arbitrary values (`p-[13px]`, `mt-[22px]`) are a generic tell.
- **Proximity = relationship**: space within a group < space between groups (e.g. 8px label-to-input, 24px field-to-field, 64px section-to-section). Most "messy" layouts are proximity failures, not alignment failures.
- Section padding (landing pages): 96–160px vertical on desktop, 48–80px mobile. Cramped sections read as dashboards; airy sections read as marketing. Choose per context.
- Density is a decision: pro tools pack 4px-grid-tight; editorial breathes. Never split the difference accidentally.

## Compositional moves (pick ONE signature per page)

- **Asymmetric hero**: 7/5 or 8/4 column split instead of centered; headline overlapping the visual by a column.
- **Overlap**: pull elements across boundaries — card overlapping the hero's bottom edge (`-mt-16`), image breaking out of its container, badge straddling a border. Overlap = depth without shadows.
- **Grid-breaking full-bleed**: contained text column + edge-to-edge media:
  ```css
  .content-grid { display: grid; grid-template-columns: 1fr min(72rem, 100% - 3rem) 1fr; }
  .content-grid > * { grid-column: 2; } .full-bleed { grid-column: 1 / -1; }
  ```
- **Bento**: mixed-span grid (`grid-cols-4` with `col-span-2 row-span-2` features). Vary cell content type (metric / visual / text), share radius + gap (the discipline that makes bento work).
- **Editorial columns**: generous outer margins, a visible baseline of hairline rules, numbered sections (`01`, `02`), text in 2 columns past `lg`.
- **Diagonal flow**: alternate left/right placement of section content; or one rotated/offset element (`rotate-2`) in an otherwise strict grid — tension, not chaos.
- **Sticky split**: left column sticky (`sticky top-24 self-start`) with chapter nav/summary, right column scrolls.

Whitespace is content: if everything is emphasized, nothing is. Generous negative space OR controlled density — deliberately.

## Grid mechanics

- CSS Grid for 2D page structure, flex for 1D rows. `gap` over margins between siblings.
- Auto-fit card grids: `grid-template-columns: repeat(auto-fit, minmax(min(18rem, 100%), 1fr))` — responsive without breakpoints.
- `aspect-ratio` for media slots; `object-cover` images; never let images dictate row heights.
- Max content width 65–80rem; reading column 45–75ch (typography.md).
- Align to the grid's edges, not to optical centers of unequal boxes; use `place-items`/`align-content` intentionally — default `stretch` causes mysterious tall cards.

## Responsive strategy

- **Mobile-first**; enhance upward. Test the 360px and the 1440px story — both must look designed, not merely "not broken".
- What changes at small sizes: bento → single column (keep ONE featured 2-span), sticky split → stacked, dock/toolbar → bottom bar, hover reveals → always-visible or tap, multi-col footers → accordion.
- **Container queries** for reusable components: `@container (min-width: 28rem)` lets a card adapt to its slot, not the viewport — correct tool for component libraries.
- Touch: targets ≥ 44×44px (`min-h-11`), `touch-action: manipulation`, hover-only affordances gated (`@media (hover: hover)`), bottom-sheet over centered modal on mobile.
- Safe areas for fixed bars: `padding-bottom: env(safe-area-inset-bottom)`.
- Fixed headers: `scroll-margin-top` on anchor targets; `scrollbar-gutter: stable` to stop layout shift.

## Z-axis discipline

Define a scale once and stick to it: content 0, raised cards 10, sticky chrome 20, dropdowns 30, overlays/modals 40, toasts 50. Ad-hoc `z-[9999]` means the scale failed. Portaled elements (tooltips, menus) render above everything by DOM position, not z-index wars.
