---
name: egyptian-web-audit
description: Audit a website or app for Egyptian and Arabic localization quality. Use when asked to review, audit, or QA an Arabic or Egyptian site for RTL bugs, broken bidi text, stiff or machine-translated Arabic copy, checkout, phone, address, and payment flows, mobile performance, accessibility, or trust signals, and to produce severity-ranked findings with evidence and fixes instead of a score.
metadata:
  version: 1.0.0
  category: egypt-localization
  locale: ar-EG
  tags: [egypt, audit, localization, rtl]
---

# Egyptian Web Audit

## Purpose

Produce evidence-backed findings about whether a product works and feels intentional for Egyptian users. Do not equate the presence of Arabic with localization quality. Do not assign a numerical score unless the user explicitly requests one and defines how it will be used.

## Use this skill when

Use it to audit an existing site, app, page set, design, or implementation for Egypt. Load specialist skills when deeper analysis is needed: `arabic-ui`, `arabic-rtl`, `egyptian-copy`, `egyptian-product-ux`, and `egyptian-backend` for observable integration/data issues.

## Workflow

1. Agree or infer the mode, scope, environment, target audience, supported locales, and critical journeys. State access limits.
2. Collect evidence at representative phone and desktop widths. Exercise interaction rather than judging screenshots alone.
3. Trace at least one critical journey end to end, including error and recovery paths when safe.
4. Record findings with reproducible evidence and separate observed behavior from inference.
5. Deduplicate root causes. One broken direction provider may explain many component symptoms.
6. Prioritize by user harm and journey impact, then propose a concrete fix and example.
7. Finish with systemic patterns, quick wins, and unknowns requiring product, legal, operational, or technical confirmation.

## Audit modes

- **Quick audit:** Sample the home/entry page, one conversion journey, navigation, and mobile RTL. Report the highest-impact issues and scope limitations.
- **Full audit:** Cover representative templates, acquisition-to-completion journeys, states, responsiveness, accessibility, performance, trust, localization, and technical RTL.
- **Content audit:** Focus on register, terminology, literal translation, CTAs, forms, states, transactions, and mixed language.
- **RTL audit:** Focus on direction roots, logical CSS, component order, bidi tokens, icons, tables, charts, portals, responsive behavior, and browser variance.
- **UX audit:** Focus on Egyptian product fit, mobile task completion, onboarding, phone/address/payment flows, support, trust, resilience, and recovery.

If scope is not stated, choose the smallest mode that answers the request and name the excluded areas.

## Evidence collection

For each issue capture:

- route/page and component;
- viewport/device and locale;
- steps to reproduce;
- observed text or behavior;
- screenshot, DOM/CSS detail, or network/performance evidence when available;
- whether the issue is consistent or intermittent;
- expected behavior and basis for that expectation.

Do not claim user behavior, business impact, legal noncompliance, or provider support without evidence. Use “may” and identify the validation needed when impact is inferred.

## Audit dimensions

### UI and typography

- Arabic-capable fonts, real weights, legibility, line height, hierarchy, density, truncation, and content expansion.
- Clear actions, touch targets, form labels, state coverage, dialog behavior, and bilingual visual balance.
- Layout behavior at narrow widths, zoom, large text, long Arabic strings, and short/empty data.

### RTL and bidi

- Correct `lang`/`dir` scope, logical properties, DOM/focus order, flex/grid reversal, offsets, radii, and portal inheritance.
- Directional versus non-directional icons, breadcrumbs, steppers, carousels, charts, tables, and horizontal scrolling.
- Phone, email, URL, code, order IDs, dates, and currency embedded in Arabic sentences.

### Copy and localization

- Declared/implicit register, consistency, literal syntax, forced transliteration, exaggerated slang, punctuation, and terminology.
- Specific CTAs, helpful validation, truthful state language, actionable errors, and distinct pending/success states.
- Missing strings, fallback leakage, concatenated fragments, untranslated metadata, and plural/date/number formatting.

### Egyptian product fit

- Phone input and OTP recovery, optional language switching, flexible address capture, EGP clarity, payment availability/status, and support channels.
- Registration friction, document upload, interruption/resume, slow-network behavior, and mobile-first prioritization.
- Trust signals must be verifiable. Do not assume WhatsApp, cash, a provider, or a document is required merely because the market is Egypt.

### Accessibility

- Semantic structure, labels, keyboard/focus, contrast, status announcements, target sizes, reflow, error association, media alternatives, and language changes.
- Test reading/focus order in RTL. Visual correctness can conceal an inaccessible DOM order.

### Performance and resilience

- Initial payload, font loading, image sizing, render blocking, layout shifts, interaction readiness, caching, retry, duplicate submission, and preservation of work.
- Use measurements from the audited environment. Do not present lab estimates as field user data.

### Trust, onboarding, and checkout

- Business identity, contact/recovery path, pricing/fees, data requests, permission explanations, service coverage, policies, order/payment state, confirmation, and references.
- Identify dark patterns, hidden commitment, ambiguous opt-in, surprise fees, and premature success language.

## Severity model

Use severity based on consequence, reach, and recoverability:

- **Critical:** blocks or corrupts a critical journey; creates serious security/privacy risk; or can cause irreversible financial/data harm.
- **High:** prevents many target users from completing an important task, produces materially misleading status, or has no reasonable recovery.
- **Medium:** causes recurring confusion, friction, accessibility loss, or localization failure but has a discoverable workaround.
- **Low:** polish or consistency issue with limited task impact.

Do not inflate severity because an issue is visually obvious. State confidence (`high`, `medium`, `low`) when evidence is incomplete.

## Finding format

```markdown
### [High] Phone number becomes visually reordered in the OTP confirmation

- **Affected:** `/sign-in`, confirmation sentence, 390 px, Arabic
- **Evidence:** After entering `+20 10 1234 5678`, punctuation and digits appear in separate visual runs.
- **Why it matters:** Users cannot confidently verify the destination before requesting a code.
- **Cause or inference:** Dynamic LTR data is interpolated directly into an RTL paragraph without isolation.
- **Recommended fix:** Render the number as an isolated LTR token and retain the surrounding sentence as RTL.
- **Example fix:** `<bdi dir="ltr">+20 10 1234 5678</bdi>`
- **Verify:** Selection/copy, screen-reader output, and Chromium/Firefox/WebKit at phone widths.
- **Confidence:** High
```

Include: issue, severity, affected location, evidence, why it matters, recommended fix, example fix, verification, and confidence. Add owner/category only if it helps triage.

## Reporting structure

1. **Scope and constraints**: mode, pages, locales, viewports, test environment, unavailable areas.
2. **Executive summary**: three to five systemic observations, not a marketing grade.
3. **Findings**: sorted by severity and then journey; use the standard format.
4. **Cross-cutting patterns**: shared typography, direction, copy, data, or component causes.
5. **Prioritized next actions**: immediate containment, near-term system fix, and research/verification.
6. **Unknowns**: facts needing analytics, user research, operations, security, legal, or provider confirmation.

Read [references/checklists.md](references/checklists.md) for mode-specific coverage.

## Avoid these audit failures

- Reporting preferences as defects without a user/task rationale.
- Calling dialect automatically better than MSA.
- Treating every physical CSS property as a bug without understanding intent.
- Recommending icon or chart mirroring globally.
- Claiming legal noncompliance without current authoritative review.
- Assigning an arbitrary localization percentage or score.
- Listing the same root cause on every page instead of showing affected examples and a systemic fix.
- Auditing only the home page or only the happy path.
- Suggesting WhatsApp, cash, or a named provider without operational evidence.

## Quality checklist

- [ ] Mode, scope, audience, environment, and access limits are explicit.
- [ ] Critical journeys include mobile, errors, and recovery where safely testable.
- [ ] Every finding contains reproducible evidence and a concrete fix.
- [ ] Severity reflects harm, reach, and recoverability; confidence reflects evidence.
- [ ] Observations, inferences, and external facts are clearly separated.
- [ ] UI, RTL, copy, local data, accessibility, performance, trust, and state handling are covered as scope requires.
- [ ] Root causes are consolidated and next actions are prioritized.
- [ ] No arbitrary score, fabricated regulation, or unsupported provider claim is included.
