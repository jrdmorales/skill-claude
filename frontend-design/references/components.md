# Components — pattern catalog & engineering standards

A vocabulary of high-impact interaction patterns (from KokonutUI and Cult UI) plus the engineering conventions that make components production-grade. Use the catalog for inspiration when a brief is vague ("make it interesting") — pick the pattern that fits the product's job, then build it with the standards below.

## Pattern catalog — pick by job

**Inputs & commands**
- *Action search bar*: input that expands a results dropdown with keyboard shortcuts shown as `<kbd>`; debounce queries (`useDebounce`); animate dropdown height smoothly.
- *AI prompt input*: auto-resizing textarea (hook measuring scrollHeight, min/max rows) + model-selector dropdown + send button that morphs to a loading state.
- *Popover form*: a button that morphs in place into a small form (shared `layoutId`), then into a success state. Far more elegant than opening a modal for one field.
- *Hold-to-confirm button*: destructive actions confirmed by press-and-hold with a radial/linear progress fill — better UX than a confirm dialog.

**Navigation & containers**
- *Dynamic island*: a compact pill that expands into rich content with spring morphs (see motion.md → morphing layouts).
- *Dock*: icon bar with mouse-proximity magnification (see motion.md → mouse-proximity).
- *Direction-aware tabs*: content slides left/right matching tab order direction; measure container for height transitions.
- *Expandable card / toolbar*: collapsed summary that springs open on click; animate measured height, never `height: auto`.
- *Floating panel / smooth drawer*: backdrop blur + spring slide-in; respect focus trap and Escape.

**Display & feedback**
- *Bento grid*: featured cells span 2×, mixed content density, each cell with its own micro-interaction.
- *Card stack*: stacked offset cards (`translateY` + `scale` per index) that fan out on click.
- *Animated number*: spring-animated counter for metrics; always `tabular-nums`.
- *Status/transfer flows*: multi-step progress with staggered check reveals — show process, not just result.
- *Loading states*: shimmer text or skeleton with moving gradient — never a bare spinner.
- *File upload*: drag-and-drop zone with distinct dragover state and animated upload progress.
- *Logo carousel*: infinite marquee, `mask-image` linear-gradient fade at edges, pause on hover.

**Text & heroes** (one per page, maximum)
- Shimmer / gradient heading / typewriter / glitch / word-swap — recipes in motion.md.
- Generative animated background behind the hero — recipes in surfaces.md §6.

## Forms & validation

Forms are where users judge whether software respects them.

- **Labels always visible** — placeholder-as-label disappears on focus and fails recall. Placeholder shows format examples only (`"name@company.com"`).
- **Validate on blur, re-validate on change** after first error — not on every keystroke of a pristine field, never only on submit.
- **Error anatomy**: border → `--crit`, message below the field (`text-sm`, icon + plain language, "what to do" not "invalid input"), `aria-invalid="true"` + `aria-describedby` pointing at the message, `role="alert"`/`aria-live="polite"` so screen readers announce it. Focus jumps to the first invalid field on submit.
- **Shake is acceptable feedback** for a rejected submit (x: [0,-6,6,-3,3,0], ~350ms) — once, with `motion-reduce` fallback to a color flash.
- **Submit button states**: idle → loading (spinner replaces label, button keeps width — measure or `min-w`) → success (check morph) → idle. Disable during flight; never let layout jump.
- Right input types/attrs: `inputmode`, `autocomplete`, `enterkeyhint` — mobile keyboards are UX.
- Multi-step forms: progress indicator + values preserved on back-navigation; one topic per step.

## Iconography

- One library, one style: outline at one stroke width (Lucide at `stroke-width={1.5/2}`) or one filled set. NEVER emoji as UI icons; never mixed styles.
- Sizes on the type grid: 16px inline with text, 20px buttons/inputs, 24px nav. `currentColor` so tokens drive color.
- Icon-only buttons: `aria-label` mandatory + tooltip on hover/focus.
- Decorative icons: `aria-hidden="true"`.

## Engineering standards

### Variants with CVA + cn()

Define visual variants declaratively, not with prop-conditional class soup:

```tsx
import { cva, type VariantProps } from "class-variance-authority"
const buttonVariants = cva("inline-flex items-center justify-center transition", {
  variants: {
    variant: { primary: "...", ghost: "..." },
    size: { sm: "h-8 rounded-md px-3 text-xs", default: "h-10 rounded-lg px-4 text-sm" },
  },
  defaultVariants: { variant: "primary", size: "default" },
})
// className always merges last: cn(buttonVariants({ variant, size }), className)
```

For two-layer surfaces (gradient ring, surfaces.md §2), define a CVA pair — `outerVariants` + `innerVariants` — keyed by the same variant names.

### Composition

- **Compound components** for anything with regions: `Card` / `CardHeader` / `CardTitle` / `CardContent` / `CardFooter`, each forwarding `ref` and accepting `className`. Consumers compose; they don't configure via 15 props.
- **`asChild` + Radix `Slot`** so a button can render as `<a>` or `<Link>` without duplicating styles.
- **Context for coordinated children** (dock items, tab groups, sortable lists): provider holds shared motion values and state; children consume via a `useX()` hook. Never prop-drill motion values.
- Demos/examples live OUTSIDE the component file's exports — ship the primitive, show usage separately.

### State & correctness

- `useId()` for SVG filter/gradient ids and `aria-labelledby` pairs — hardcoded ids collide.
- Cleanup every `setInterval`/`setTimeout`/listener in effect teardown; stable callbacks via a `useCallbackRef` pattern for resize/mouse handlers.
- Extract magic numbers to named constants (`const HOLD_DURATION_MS = 800`).
- Hooks that components share (`useDebounce`, `useAutoResizeTextarea`, `useMousePosition`) go in separate files, reusable.

### Accessibility (non-negotiable for custom widgets)

Custom interactive elements implement the full ARIA pattern. Example — a seek/progress slider:

```tsx
<div role="slider" tabIndex={0}
     aria-label="Seek" aria-valuemin={0} aria-valuemax={duration} aria-valuenow={current}
     aria-valuetext={`${fmt(current)} of ${fmt(duration)}`}
     onClick={seekToPointer}
     onKeyDown={(e) => {
       if (e.key === "ArrowRight") { e.preventDefault(); seek(current + 5) }
       if (e.key === "ArrowLeft")  { e.preventDefault(); seek(current - 5) }
       if (e.key === "Home") { e.preventDefault(); seek(0) }
       if (e.key === "End")  { e.preventDefault(); seek(duration) }
     }} />
```

The same rigor applies to tabs (`role="tablist"`, arrow-key navigation), toggles (`aria-pressed`), expandables (`aria-expanded`/`aria-controls`), and drag-to-sort (keyboard alternative). Icon-only buttons always get `aria-label`. Loading states get `aria-busy` / `aria-live="polite"`.

### Performance

- `React.memo` heavy decorative subtrees (generated SVG, particle fields); `useMemo` generated data keyed by real inputs.
- Canvas or SVG for >50 animated elements — not 50 DOM nodes with springs.
- Images: explicit dimensions + `sizes`; videos in hover-players lazy-load and pause off-screen.
- Debounce search input (~200ms); throttle scroll/resize handlers via rAF.
