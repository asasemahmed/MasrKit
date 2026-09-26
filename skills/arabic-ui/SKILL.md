---
name: arabic-ui
description: Design and review Arabic-first interfaces for any Arabic market. Use when choosing Arabic fonts, type scale, and line height, laying out Arabic or bilingual pages, forms, navigation, cards, dashboards, and dialogs, or specifying loading, empty, error, and success states with accessibility. Not for RTL implementation bugs (use arabic-rtl) or Egypt-specific flows (use egyptian-product-ux).
metadata:
  version: 1.0.0
  category: arabic-foundation
  locale: ar
  tags: [arabic, ui, typography, accessibility]
---

# Arabic UI

## Purpose

Create interfaces whose hierarchy, rhythm, components, and content behavior work naturally in Arabic. Treat language direction as one input to design, not as an instruction to mirror every visual decision. Coordinate with `arabic-rtl` when implementation details or bidirectional text are in scope.

## Use this skill when

Use it for Arabic-first or bilingual pages, components, design systems, responsive layouts, and visual reviews. For Egyptian tone and terminology, also use `egyptian-copy`. For market-specific product flows, also use `egyptian-product-ux`.

## Workflow

1. Identify the primary locale, secondary language, audience, device context, and task. Label missing facts as assumptions.
2. Inventory every content type: headings, body copy, labels, numbers, identifiers, statuses, actions, and mixed-language strings.
3. Establish Arabic typography and spacing tokens before tuning individual components.
4. Design the narrow/mobile state first when the audience is phone-heavy. Expand layouts without changing reading or keyboard order.
5. Specify default, hover/focus, disabled, loading, empty, validation, error, and success behavior.
6. Review hierarchy and scan paths with realistic Arabic content, including long and short variants.
7. Test accessibility, zoom, text enlargement, and mixed Arabic/Latin data.

## Typography and hierarchy

- Choose a font family with a complete, well-drawn Arabic character set and the weights actually shipped. Do not assume a Latin family's Arabic fallback will share its proportions.
- Evaluate Arabic at the intended size on target devices. Thin weights and tight counters lose clarity quickly; regular or medium often works better than light for UI text.
- Pair Arabic and Latin fonts by perceived size, x-height/counter scale, weight, and tone rather than identical numeric size. Prefer a family designed for both scripts when it fits the brand.
- Use real font weight files or verified variable-font axes. Synthetic bold can damage joins and legibility.
- Start body copy around the platform's normal readable size, then test. Arabic often benefits from more line height than comparable Latin copy because of marks and vertical forms.
- Keep heading levels semantic. Create hierarchy through size, weight, spacing, and contrast; do not rely on bold everywhere.
- Avoid letter spacing on Arabic. It can break joining behavior or produce unnatural texture. Adjust font, size, width, or word spacing instead.
- Keep prose lines moderate. As a working test, compare lines around 45–75 Arabic characters, then adjust for font, device, and content. Forms and dashboards need shorter scan lengths.
- Never clip diacritics or dots with fixed line boxes. Test strings containing marks even if everyday copy usually omits full vocalization.

Read [references/typography.md](references/typography.md) when selecting fonts or defining type tokens.

## Layout and visual rhythm

- Align primary Arabic reading content to the start edge. Center only short, intentionally prominent copy such as a compact hero or empty state.
- Derive spacing from content density and touch needs, not by copying an English screen pixel for pixel. Arabic labels may be taller or longer.
- Let containers grow. Avoid fixed heights around text, fixed-width CTA labels, and truncation of critical actions.
- In bilingual screens, make the primary language visually dominant and give the secondary language a repeatable treatment. Do not alternate alignment randomly.
- Keep reading order, DOM order, focus order, and visual order consistent. Visual mirroring must not create a different keyboard sequence.
- Use whitespace to separate semantic groups. Dense enterprise screens may be compact, but must retain clear row boundaries and hit targets.

## Component rules

### Navigation

- Put primary destinations in a predictable start-to-end sequence. Mirror directional navigation where it represents movement through an interface; preserve brand marks and non-directional symbols.
- On mobile, prioritize the current task and a small set of destinations. Translate labels for meaning, not word length; allow the layout to accommodate longer labels.
- Expose the current location visually and programmatically. Do not depend only on color.

### Buttons and actions

- Use verbs that describe the result: `كمّل الطلب`, `احفظ التغييرات`, or an audience-appropriate neutral equivalent.
- Keep one clear primary action per decision area. Place action groups according to reading flow, platform convention, and risk, not a blanket mirroring rule.
- Preserve label width under loading. Pair a spinner with an accessible status, prevent duplicate submission, and state what is happening.
- For destructive actions, name the object and offer a safe confirmation or undo proportional to the harm.

### Forms

- Place persistent labels above or beside fields; placeholders are examples, not labels.
- Associate instructions and errors with inputs programmatically. Explain how to recover, not merely that a value is invalid.
- Group related fields and reveal optional detail progressively. Match field direction to the value: Arabic prose RTL; phone, email, URL, code, and many identifiers as explicit LTR islands.
- Preserve user input after a validation or network error. Move focus to an error summary only when it improves recovery, then link each error to its field.
- Use localized examples without using an example as a hidden validation rule.

### Cards, lists, and dashboards

- Use cards for meaningful groups, not every sentence. Preserve a clear start edge for titles, metadata, status, and actions.
- For repeated records, optimize comparison: stable columns, consistent number alignment, and visible labels at narrow widths.
- Give charts titles, units, accessible summaries, and table alternatives where needed. Do not reverse time or magnitude simply because surrounding UI is RTL.
- Keep status color plus text/icon. Ensure filters, result count, empty results, stale data, and partial failures are represented.

### Dialogs and transient UI

- Give dialogs a descriptive title, initial focus, contained focus, Escape/close behavior where safe, and returned focus after dismissal.
- Keep primary and secondary actions clearly differentiated. Confirmation copy must state consequence and object.
- Toasts are for supplemental confirmation, not the sole carrier of errors or required next steps. Allow enough reading time and expose updates to assistive technology.

## States

- **Loading:** Use a skeleton only when it approximates the final layout; otherwise use a status indicator and meaningful label. Avoid fake precision.
- **Empty:** Distinguish first-use, no-results, permission-limited, and error emptiness. Explain the state and offer one useful next action.
- **Error:** Say what failed, what remains safe, and how to retry or choose another path. Preserve entered data.
- **Success:** Confirm the completed object and next step. Avoid generic `تم بنجاح` when the result can be named.
- **Offline/slow:** Show pending state, prevent duplicate actions, and explain whether work was saved locally or submitted.

## Mixed language and numbers

- Keep product names, model numbers, codes, email addresses, and URLs intact when translation harms recognition.
- Isolate mixed-direction tokens with semantic markup such as `bdi` or a deliberate direction wrapper. Do not insert invisible Unicode controls into stored copy as a default workaround.
- Choose Arabic-Indic or Western digits from product convention and user research; stay consistent within a task. Never reorder the digits themselves.
- Localize date and currency display with locale-aware formatters, then verify the exact product requirement. Avoid hand-concatenating symbols and values.

## Accessibility

- Meet applicable contrast and target-size guidance; verify rather than assuming a palette is accessible.
- Support keyboard navigation, visible focus, meaningful landmark/headings, accessible names, and status announcements.
- Test at 200% zoom and with enlarged text. Content and actions must reflow without two-dimensional scrolling except for inherently wide data.
- Use semantic HTML before ARIA. Match accessible names to visible Arabic labels; set the document or section language correctly.
- Do not encode meaning only through direction, position, icon, or color.

## Common anti-patterns

- Mirroring every image, logo, chart, media control, or icon.
- Applying `text-align: right` globally, including to emails and phone numbers.
- Using a decorative Arabic display font for long body copy.
- Shrinking Arabic text to force parity with an English card.
- Fixed-height buttons or cards that clip translated copy.
- Mixing formal Arabic, Egyptian Arabic, and untranslated English without a voice decision.
- Center-aligning long forms or paragraphs.
- Omitting error, empty, loading, and offline behavior from the design.

## Quality checklist

- [ ] The chosen font supports Arabic and required weights without synthetic styling.
- [ ] Heading, body, label, and helper-text hierarchy remains clear with real Arabic copy.
- [ ] Components tolerate longer text, zoom, and small screens without clipping.
- [ ] Mixed-language tokens and numbers remain readable and selectable.
- [ ] Reading, DOM, focus, and visual order agree.
- [ ] Every async and data component has meaningful loading, empty, error, and success behavior.
- [ ] Directional icons are evaluated individually; brand and semantic icons are preserved.
- [ ] Keyboard, screen-reader labels, contrast, and touch targets are tested.
