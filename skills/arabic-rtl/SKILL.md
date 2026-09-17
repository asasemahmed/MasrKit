---
name: arabic-rtl
description: Implement and test robust right-to-left web layouts, bidirectional content, direction-aware components, and mixed Arabic/Latin data.
metadata:
  version: 1.0.0
  category: arabic-foundation
  locale: ar
  tags: [rtl, bidi, css, web]
---

# Arabic RTL Engineering

## Purpose

Make direction a supported system property across markup, CSS, components, data display, and tests. `dir="rtl"` establishes the base direction; it does not solve component geometry, mixed-direction text, icons, charts, or interaction order.

## Use this skill when

Use it to implement or review RTL web applications, bilingual components, CSS systems, React/Next.js pages, Tailwind utilities, and bidirectional data. Pair with `arabic-ui` for visual decisions and `egyptian-copy` for language.

## Workflow

1. Determine direction at the document or locale-root level; use local overrides only for genuinely different content.
2. Audit physical CSS (`left`, `right`, `margin-left`, absolute offsets, directional radii/borders) and classify each as flow-relative or physically anchored.
3. Map DOM, reading, keyboard, and visual order. Fix source order before using CSS reversal.
4. Identify LTR islands: phone numbers, emails, URLs, code, IDs, and sometimes dates/numeric expressions.
5. Classify icons and data visualizations by meaning before flipping.
6. Test both RTL and LTR at narrow and wide widths with realistic mixed content.
7. Add direction-specific regression tests for the risky components.

## Direction foundations

- Set `<html lang="ar" dir="rtl">` for an Arabic document. For locale-scoped applications, set `lang` and `dir` on the locale root and update both on language change.
- Prefer the HTML `dir` attribute over CSS `direction` for content direction because user agents and assistive technology understand it.
- Use `dir="auto"` for isolated user-generated text only when first-strong-character behavior is actually desired and tested.
- Use `dir="ltr"` on a wrapper or input for values whose internal order is LTR. Direction and text alignment are separate decisions.
- Do not store presentational direction marks in domain data unless the data standard requires them. Apply isolation at rendering boundaries.

## Logical CSS

Use logical properties when a value depends on writing direction:

```css
.panel {
  margin-inline-start: 1rem;
  padding-inline: 1.25rem;
  border-inline-start: 0.25rem solid var(--accent);
  inset-inline-start: 0;
  text-align: start;
}
```

Prefer `inline-size`, `block-size`, `min-inline-size`, `border-start-start-radius`, and `inset-inline-end` where they express intent. Physical properties remain correct for physical concepts such as a map coordinate, a drag axis tied to the screen, or an art-directed background. Document that choice.

Do not mechanically replace every `left` with `right`; determine whether the relationship is logical, physical, temporal, or semantic.

## Flexbox and grid

- Let base direction influence inline flow. Avoid combining RTL with `row-reverse` merely to obtain expected visual order; this commonly reverses twice and harms focus order.
- Keep DOM order semantic. Use grid areas or responsive layout changes without changing the logical reading sequence.
- Check `justify-content`, auto margins, absolute badges, overflow shadows, and scroll-start behavior in both directions.
- For horizontally scrollable lists, test initial scroll position and keyboard navigation in each target browser; scroll-coordinate behavior has historical differences.
- In tables, choose column order based on the audience's scan task. Do not reverse time-series or identifier characters.

## Icons and imagery

Flip icons whose meaning is relative to reading/navigation direction: back/forward arrows, undo/redo when drawn directionally, reply/indent, and directional chevrons.

Do not flip:

- logos and trademarks;
- phone, camera, microphone, search, check, close, download, or play icons;
- clocks, maps with real geography, product images, or physical-world objects where orientation is meaningful;
- payment/network/provider marks;
- charts merely because the UI is RTL.

When meaning is ambiguous, use separate RTL/LTR assets or a component prop. Prefer icon metadata (`directional: true`) over scattered CSS selectors.

## Bidirectional content

Wrap self-contained dynamic values with `<bdi>` so surrounding punctuation does not jump:

```html
<p>تم إرسال الرسالة إلى <bdi dir="ltr">name@example.com</bdi></p>
<p>رقم الطلب: <bdi dir="ltr">EG-2048-A</bdi></p>
```

For known-direction editable values:

```html
<label for="phone">رقم الموبايل</label>
<input id="phone" type="tel" dir="ltr" inputmode="tel" autocomplete="tel">
```

- Keep phone digits in entered/logical order. Never reverse strings in application code.
- Render URLs, emails, code, serials, and file paths as LTR islands while keeping surrounding sentences RTL.
- Localize display dates with `Intl.DateTimeFormat` or an equivalent, then isolate the rendered token if punctuation becomes ambiguous.
- Use Unicode isolation controls only when markup is unavailable (for example, a plain-text notification). Prefer isolate controls over embedding/override controls, generate them at presentation time, and test copy/paste behavior.
- Never use bidi override to make malformed data appear correct.

Read [references/bidi-and-data.md](references/bidi-and-data.md) for data-type handling.

## Components with special direction behavior

### Breadcrumbs and steppers

Order items by conceptual progression, render separators directionally, and preserve meaningful DOM order. Announce the current step/location. A visual arrow may flip; step numbers do not.

### Tables

Keep row actions predictably at the logical end or start according to the product convention. Align prose to start and numeric comparison columns consistently. On mobile, convert to labeled records rather than relying on horizontal reversal.

### Charts

Decide each axis from the data model. Chronological axes often remain earliest-to-latest according to visualization convention even in RTL products; category lists may follow reading order. Label units, expose a data table/summary, and test tooltips containing mixed text. Never transform the dataset to achieve visual mirroring.

### Inputs

Arabic free text is RTL. Phone, email, URL, password, code, OTP, and many identifiers should be explicit LTR islands. Numeric input direction does not determine locale formatting. Prefixes/suffixes must remain attached to the value under bidi reordering.

## React and Next.js

- Derive `lang` and `dir` from validated locale metadata at the highest stable layout boundary. With server rendering, ensure server and client choose the same values to avoid hydration changes.
- Keep direction in shared locale context only when components genuinely need behavior beyond CSS flow.
- Avoid conditional duplication of complete component trees for RTL. Share semantics; parameterize direction-specific assets and positioning.
- If the component library has an RTL cache/plugin, verify its documented setup and version. Do not assume all third-party components inherit direction correctly.
- Test portals (dialogs, menus, tooltips) because they may render outside the locale root and lose inherited `dir`.

## Tailwind

- Prefer direction-neutral utilities and logical-property utilities supported by the project's actual Tailwind version.
- When using `rtl:`/`ltr:` variants or plugins, verify official documentation and generated CSS. Keep physical utility exceptions explicit.
- Avoid class strings that apply both a physical offset and an RTL counter-offset unless the component truly needs two variants.
- A small semantic component class can be clearer than a long set of duplicated direction variants.

## Testing strategy

- Unit/component tests: assert root `dir`, local LTR islands, icon variant/transform, and semantic order.
- Visual tests: capture LTR and RTL at small/large widths with long Arabic, mixed tokens, and empty/error states.
- Interaction tests: tab through controls, operate arrow keys, open portals, scroll horizontal content, and use zoom.
- Browser tests: current supported Chromium, Firefox, and WebKit/Safari where applicable. Check selection, copy/paste, autofill, native date/number controls, and horizontal scrolling.
- Assistive technology: verify language announcement, label association, reading order, live status, and that visual reversal does not alter meaning.

Read [references/test-matrix.md](references/test-matrix.md) for a reusable browser checklist.

## Common bugs

- Double reversal from `dir="rtl"` plus `flex-row-reverse`.
- Correct-looking CSS with incorrect DOM/tab order.
- Phone or order numbers visually scrambled by surrounding punctuation.
- Menus/tooltips rendered in a portal with LTR direction.
- Absolute badges pinned to `right` in both locales.
- Both previous and next icons flipped by a global SVG transform.
- Timeline/chart data reversed rather than intentionally laid out.
- Arabic placeholder aligned correctly while the typed email becomes hard to edit.
- Ellipsis appearing on the misleading side of a mixed string.

## Quality checklist

- [ ] Locale root has correct `lang` and `dir`; portals inherit or receive direction.
- [ ] Flow-relative spacing, borders, radii, and offsets use logical properties.
- [ ] DOM, focus, reading, and visual order are coherent.
- [ ] Every directional icon is classified; non-directional assets are unchanged.
- [ ] Phone, email, URL, code, and identifiers are tested as LTR islands.
- [ ] Tables, breadcrumbs, steppers, and charts follow their data semantics.
- [ ] RTL and LTR pass narrow/wide visual and keyboard tests.
- [ ] No string reversal or bidi override hides a data/modeling bug.
