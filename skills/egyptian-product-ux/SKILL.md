---
name: egyptian-product-ux
description: Design product flows for Egyptian users. Use when designing signup and login with Egyptian phone numbers and OTP, Egyptian address forms (governorate, district, landmark), EGP pricing and checkout with cash on delivery, cards, Meeza, mobile wallets, InstaPay, or Fawry-style reference payments, WhatsApp handoff, document uploads, language switching, or flows that must survive weak mobile connections. Includes dated Egypt reference facts.
metadata:
  version: 1.0.0
  category: egypt-localization
  locale: ar-EG
  tags: [egypt, product-ux, mobile, localization]
---

# Egyptian Product UX

## Purpose

Turn local context into testable product decisions without treating Egyptians as one homogeneous persona. Separate three layers in every recommendation:

1. **Universal UX:** accessibility, feedback, error recovery, clear hierarchy.
2. **Arabic-wide:** RTL, mixed scripts, Arabic typography.
3. **Egypt-specific:** phone/address patterns, EGP display, locally validated channels and expectations.

Start from the dated defaults in [references/egypt-facts.md](references/egypt-facts.md): phone formats, address structure, EGP display, digits, time zone and weekend, common payment methods, and messaging channels. Design with those directly. Only facts marked *(changes)* there, plus anything legal or provider-specific, need confirmation from a current official source before they become hard rules.

## Use this skill when

Use it to design or review acquisition, onboarding, registration, checkout, booking, marketplace, education, SaaS, support, and identity/document flows for Egypt.

This skill owns the user-facing flow. Neighboring skills own the rest, so load them when the task reaches their layer:

| Topic | This skill decides | Owned elsewhere |
|---|---|---|
| Phone and OTP | Flow, correction, resend UX | Storage, limits, enumeration: `egyptian-backend` |
| Payments | Which methods to show, pending and recovery screens | State machine, reconciliation: `egyptian-backend`; wording: `egyptian-copy` |
| Uploads and documents | What to ask for, guidance, retry | Validation, storage, access: `egyptian-backend` |
| Mixed Arabic/Latin values | Where they appear | Isolation and direction: `arabic-rtl` |

## Workflow

1. Define audience segments by task, context, device, language comfort, and constraints, not stereotypes.
2. Create an evidence table: known product facts, research findings, assumptions to test, and external facts requiring current verification.
3. Map the critical path on a narrow screen and intermittent connection. Identify interruption/resume points.
4. Decide language, phone, address, currency, payment, support, and identity behavior explicitly.
5. Reduce initial commitment and ask for information at the moment it becomes necessary.
6. Design pending, offline, duplicate, timeout, rejection, and recovery paths alongside the happy path.
7. Validate with representative Egyptian users and operational teams; record segment differences rather than averaging them away.

## Mobile and connection resilience

- Treat mobile-first as prioritization, not simply a single-column desktop page. Keep the current task, progress, and primary action visible without crowding.
- Minimize payload and blocking assets. Use responsive images, cache stable content, defer noncritical code, and show meaningful progress.
- Preserve draft form state across navigation and transient failures. Tell users whether a draft is local, synced, or submitted.
- Make submission idempotent where feasible. Disable duplicate actions only while communicating status and allowing recovery.
- For uploads, validate before transfer, show progress, allow retry per file, and avoid making the user restart the form.
- Do not claim “offline support” unless the product genuinely queues and reconciles actions.

## Language choice

- Make Arabic and English switching discoverable when both are supported. Use language names (`العربية`, `English`), not flags.
- Preserve task state during a language switch. Do not return the user to a home page or erase input.
- Store language preference at an appropriate account/device/session level and allow override.
- Do not assume English proficiency from age, education, job, or device. Test terminology with the intended audience.
- Keep official names and common technical identifiers intact when translation creates ambiguity.

## Phone-number-first flows

Phone-first may be appropriate when the product's authentication, delivery, or support model genuinely depends on it. It is not a universal Egyptian requirement.

- Accept common human-entered separators and normalize at the backend boundary.
- Show a clear country calling code when international form is expected; do not silently prepend/strip without feedback.
- Keep the field visually LTR and the label/instructions RTL.
- Accept every input format listed in [references/egypt-facts.md](references/egypt-facts.md), including Arabic-Indic digits. Never validate or label by operator prefix.
- Offer correction before sending OTP. Mask the destination in confirmation screens without hiding which number was used.

## OTP UX

- Explain where the code was sent and how long the current code remains usable only if the backend enforces that rule.
- Support paste and platform autofill where available. A single logical input is often more accessible than six unrelated boxes.
- Show when resend becomes available without trapping the user.
- Handle delayed messages, expired/replaced codes, too many attempts, number correction, and alternate verified channels.
- Keep screens neutral about whether an account exists; the backend enforces this.

## Egyptian addresses

Ask only for the precision the fulfillment or service needs. Egyptian addresses may require a flexible combination of governorate, city/area/district, street, building, floor, apartment, landmark, recipient, and phone. Do not force every address into a foreign state/ZIP template.

- A practical delivery form: governorate (select), city or district (select with a free-text fallback), street, building number, floor, apartment, landmark (`علامة مميزة`), and a recipient phone the courier can call.
- Use structured fields for routing/filtering and a flexible address/detail field for local delivery nuance. Do not require a postal code.
- Make field labels concrete and mark required versus optional.
- Provide searchable choices only when the maintained dataset is authoritative and current; otherwise allow safe fallback entry.
- Keep address book entries editable and show a human-readable summary before confirmation.
- Do not infer administrative legality or serviceability from a typed locality; validate against actual operational coverage.

Read [references/local-data.md](references/local-data.md) for phone, address, currency, date, and timezone boundaries.

## Currency and payment UX

- Represent currency explicitly as EGP in product requirements and backend data. Display may use `ج.م`, `EGP`, or a verified localized formatter according to audience and context.
- Show total, fees, discounts, delivery, and tax treatment clearly. Do not reveal a new mandatory charge at the final action.
- Display a payment method only when it is supported for this order, user, amount, and environment.
- Egyptian users expect some mix of cash on delivery, cards (including Meeza), mobile wallets, InstaPay, reference-code payments such as Fawry, and installments. Show only the ones this account actually has enabled.
- For reference-code payments and cash on delivery, the order is pending by design: show the code or instructions, the expiry, and how the user will know it went through.
- Distinguish initiated, awaiting user action, pending provider confirmation, paid, failed, refunded, and partially refunded.
- On uncertain outcomes, prevent blind repeat payment, show how status will update, and provide a reference/support path.

## Trust and registration friction

- Explain why sensitive or unusual information is needed at the point of collection.
- Let users explore value before registration when the business and risk model permit it.
- Use specific, verifiable trust signals: clear business identity, contact path, policies, secure interaction, real service coverage, and transparent pricing. Avoid generic shield icons as proof.
- Minimize permissions and documents. A request from operations is not automatically a requirement for every user.
- Show how to correct account details and recover access. Do not make WhatsApp the only support/recovery channel unless that limitation is explicit.

## WhatsApp-centric flows

Use WhatsApp as an optional channel when research and operations support it: sales handoff, booking follow-up, support, or order communication. Keep the core state in the product/backend where continuity, audit, or privacy requires it.

- State what will be shared before opening a conversation.
- Pre-fill only necessary, non-sensitive context and let the user edit it.
- Provide a fallback when WhatsApp is unavailable or inappropriate.
- Do not imply end-to-end product completion if the user is merely leaving the app to message a business.
- Do not promise WhatsApp automation (templates, bots, delivery receipts) that the business has not actually set up.

## Domain patterns

### Education and applications

Support discovery before account creation, draft/resume, eligibility explanations, document previews, clear deadlines from verified sources, and a distinct final-submission confirmation. Preserve official program/institution names.

### Ecommerce

Prioritize product truth, variants, stock, total cost, delivery coverage, editable address/contact, payment status, and order recovery. Guest checkout can reduce friction where the risk model permits.

### Service booking

Clarify service scope, location/remote mode, provider/time availability, price basis, confirmation semantics, rescheduling/cancellation, reminders, and late/failed confirmation paths.

### Marketplaces

Separate platform, buyer, and seller responsibility. Show identity/reputation evidence proportionally, protect contact details, handle unavailable inventory, and design dispute/support escalation without inventing guarantees.

### SaaS

Handle role/permission clarity, organization setup, bilingual data, imports, invitations, billing state, and administrator recovery. Do not localize domain terms inconsistently across UI and exports.

## Documents and identity-related forms

- Request only necessary documents and explain purpose, accepted types, size, image quality, retention, and who can access them.
- Provide camera guidance and preview/replace controls. Support low-bandwidth retry.
- Ask for the national ID or identity documents only when a confirmed requirement exists. A requirement seen in another Egyptian service is not evidence for yours.

## Accessibility and recovery

- Provide labels, focus order, contrast, touch targets, status announcements, and non-color cues.
- Write recovery paths for invalid data, expired sessions, network loss, duplicate submission, unavailable options, and partial completion.
- Preserve user work by default. If it cannot be preserved, warn before the loss.
- Give support a reference ID and enough context without exposing secrets or personal data.

## Quality checklist

- [ ] Recommendations are labeled universal, Arabic-wide, or Egypt-specific where ambiguity matters.
- [ ] User segments and assumptions are explicit and non-stereotyped.
- [ ] The critical flow works on a phone and recovers from interruption.
- [ ] Language switching preserves state; mixed terms remain understandable.
- [ ] Phone, address, currency, date, and payment behavior is specified without brittle assumptions.
- [ ] OTP, uploads, documents, and sensitive data have secure recovery paths.
- [ ] WhatsApp or other local channels are optional/verified and operationally supported.
- [ ] Pending and uncertain transaction states cannot trigger accidental duplicates.
- [ ] Legal, regulatory, provider, and numbering facts are verified from current official sources.
