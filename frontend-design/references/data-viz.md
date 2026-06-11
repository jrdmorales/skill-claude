# Data visualization & dashboards

Dashboards are where craft is most measurable: the same data can read as noise or as instant comprehension. The governing rule is **maximize data-ink**: every pixel either encodes data or earns its place.

## Dashboard anatomy

- **Hierarchy in 3 tiers**: (1) KPI row — the numbers that answer "is everything OK?"; (2) primary chart — the trend behind the headline number; (3) detail grids/tables. A user should get tier-1 comprehension in under 3 seconds.
- **KPI card**: label (eyebrow style, `text-xs uppercase tracking-wider text-fg-muted`) → value (display font, `tabular-nums`, animated count-up on load) → delta chip (`▲ 12.4%` in `--ok`/`--crit` with `aria-label` spelling it out) → optional sparkline. Never center-align KPI stacks; left-align for scanability.
- **Card chrome stays quiet**: surfaces.md §4 shadow stack or §1 hairlines; the DATA is the hero, not the card.
- Density per directions.md → industrial playbook: 4px grid, compact paddings, mono for values.

## Charts

**Reduce before styling** — remove default chartjunk: outer borders, axis lines (keep ticks/labels), legends when ≤2 series (label lines directly), and most gridlines (horizontal only, `--border` at 50% opacity, dashed).

- **Series color**: one hue ramp for related series + the accent for the highlighted series; status semantics where applicable. NEVER default library rainbows. Muted context series (`--fg-subtle`) + one saturated focus series is the strongest pattern.
- **Line charts**: 2–2.5px stroke, `strokeLinecap="round"`; area fill = vertical gradient accent 15% → 0%; dots only on hover/last point. Last-value label at line end beats a legend.
- **Bar charts**: radius only on the data end (`[4,4,0,0]`), category gap ≥ 30%, hover = lighten + tooltip, baseline always zero (lines may zoom, bars may not).
- **Axes**: `tabular-nums`, `--fg-subtle`, compact formats (`12.4k`, `Jan 5`, `99.95%`), max ~6 y-ticks, no axis titles when the card title says it.
- **Tooltips**: custom-styled (surface token, hairline border, shadow stack §4) — library-default tooltips break the aesthetic instantly. Shared cursor line across stacked charts for time correlation.
- **Animate once**: draw-in/grow ≤ 800ms on mount, none on data refresh (jarring on live data); respect `prefers-reduced-motion`.
- Recharts: style via tokens (`stroke="var(--accent)"`), kill defaults (`tickLine={false} axisLine={false}`), `<defs><linearGradient>` for area fills. Chart.js: set global font/color defaults from tokens before render, `maintainAspectRatio: false` inside sized containers.

## Tables

- Hairline row separators only (no vertical lines, no heavy zebra; zebra at 2–3% tint acceptable for >10 dense columns).
- Header: `text-xs uppercase tracking-wider text-fg-muted`, sticky (`sticky top-0 bg-surface/95 backdrop-blur`), sort indicators on hover.
- Numbers right-aligned + `tabular-nums`; text left; never center data columns. Units in the header, not repeated per cell.
- Row hover tint; row height 40–48px comfortable / 32px dense (offer the toggle on pro tools).
- Status as dot + label chip, not background-painted rows (paint = colorblind + contrast hazard).
- Long tables: virtualize past ~100 rows; skeleton rows during load matching final row height (no layout jump).

## Live / monitoring patterns (telemetry, uptime, fleets)

- **Status semantics**: dot + label, `--ok`/`--warn`/`--crit`; live = subtle pulse (scaled-down `animate-ping`, `motion-reduce:animate-none`); stale data = explicitly marked ("last seen 4m ago"), never silently frozen.
- **Timestamps**: relative by default ("2m ago"), absolute on hover/title attr; `<time datetime>`; mono font.
- **Thresholds on charts**: reference lines (dashed, `--warn`/`--crit` at 60%) with right-edge labels; band fills for acceptable ranges.
- **Uptime/heatmap strips**: 90-day bar strip (GitHub-contribution style) — instant pattern recognition; tooltip per cell.
- **Auto-refresh**: indicate it (spinning-free — a quiet "updated 10s ago" beats a spinner); animate value CHANGES (count-up, flash-fade of row) so updates are perceivable without being noisy.
- **Alert states**: critical banners use `role="alert"`, icon + plain-language summary + action; chart regions in alarm get tinted background bands, not flashing.

## Empty, loading, error — design them, don't default them

- **Empty**: small illustration or icon composition (not a giant sad-face emoji), one sentence of guidance, primary CTA. An empty dashboard is the FIRST thing new users see — it's onboarding.
- **Loading**: skeletons mirror final layout (KPI blocks, chart rectangle, table rows) with shimmer (motion.md); never a lone centered spinner for a full page.
- **Error**: state what failed in plain language, keep the layout (don't collapse to a void), offer retry; partial failures degrade per-card, not whole-page.

## Accessibility for data

- Charts get a text alternative: `aria-label` summarizing the takeaway ("CPU stable around 40%, spike to 92% at 14:00") or a visually-hidden table.
- Interactive chart points/series keyboard-reachable, or provide the data-table fallback toggle.
- Color-blind safety: status always color + shape/label; test the ramp in grayscale — if series are indistinguishable, vary line style (solid/dashed) too.
