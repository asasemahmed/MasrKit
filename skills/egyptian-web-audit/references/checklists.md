# Audit coverage checklists

## Quick

- Locale entry and switch; header/navigation; primary CTA.
- One critical flow on a phone width.
- Root direction, mixed phone/email, one form error, and one async state.
- Arabic font/readability, register consistency, EGP/date formatting.
- Keyboard path, zoom/reflow, obvious performance blockers.

## Content

- Voice/register by journey and risk.
- Navigation labels, CTAs, helper text, validation, pending/success/error.
- Repeated terminology and English/transliteration decisions.
- Transactional notification consistency with in-product state.
- Literal phrasing, missing/fallback strings, fragment concatenation.

## RTL

- `lang`/`dir`, portals, logical CSS, source/focus order.
- Directional icon inventory and non-flippable assets.
- Tables, charts, breadcrumbs, steppers, overflow, sticky edges.
- LTR islands, punctuation, caret, selection/copy/paste.
- Narrow/wide layouts in supported browser engines.

## UX/full

- Acquisition, registration, onboarding, core task, support/recovery.
- Phone/OTP, language state, address, currency/payment, uploads/documents.
- Slow/intermittent network, interrupted flow, duplicates, uncertain outcomes.
- Trust and privacy explanations, accessibility, measurable performance.
- Operations/legal/provider unknowns explicitly routed for verification.
