---
name: egyptian-backend
description: Design backends for Egyptian-facing products. Use when modeling EGP money, +20 phone numbers, Africa/Cairo time and daylight saving, Arabic text storage and search normalization, locale negotiation, SMS, WhatsApp, and email notifications, OTP login, document uploads, or adapters for Egyptian payment, wallet, and messaging providers in FastAPI, Node.js, or Next.js. Not for UI flows (use egyptian-product-ux).
metadata:
  version: 1.0.0
  category: egypt-localization
  locale: ar-EG
  tags: [egypt, backend, internationalization, security]
---

# Egyptian Backend

## Purpose

Build backend contracts and data systems that preserve Arabic correctly, represent Egyptian product data explicitly, and keep changing local integrations behind adapters. This skill is not about writing code identifiers in Arabic or assuming a single Egyptian architecture.

## Use this skill when

Use it for APIs, schemas, authentication, search, notification delivery, money, dates, phone/address data, uploads, and local integrations for Egyptian-facing products. It applies to FastAPI, Node.js, Next.js server environments, and other stacks without prescribing a framework.

## Workflow

1. Identify locale-sensitive domain values and separate canonical storage, normalized lookup, and localized display. Use [references/egypt-data.md](references/egypt-data.md) for Egyptian phone, digit, ID, EGP, time-zone, search, and payment-state defaults.
2. Model money, time, phone, address, and message state explicitly.
3. Define locale negotiation and fallback at system boundaries.
4. Put email, SMS, WhatsApp, payment, and other changing providers behind capability-based adapters.
5. Threat-model authentication, OTP, uploads, privacy, logs, and webhook/callback flows.
6. Define idempotency, retry, timeout, pending, and reconciliation behavior.
7. Test Arabic round trips, normalization/search behavior, templates, concurrency, failures, and fallbacks.
8. Verify current official provider and regulatory documentation before implementing changing requirements.

## Text and internationalization data

- Use UTF-8 end to end: source, database, connection, API, queues, logs, files, and tests. Verify actual database collation/encoding rather than relying on defaults.
- Store user-authored Arabic exactly as entered unless a domain rule requires transformation. Normalization for search must not overwrite display text.
- Keep stable localization keys in code/data and localized templates in versioned resources. Do not use an English sentence as the database key.
- Define fallback deliberately, for example requested `ar-EG` → supported `ar` → product default. Log missing keys without exposing sensitive interpolation data.
- Keep locale separate from direction. A locale selects language/formatting; direction is derived from supported locale metadata.
- Avoid constructing sentences by concatenating translated fragments. Templates need complete messages and named variables.

## Arabic search

Arabic search can require a separate indexed representation. Decide based on product requirements and measured queries:

- Unicode normalization form;
- optional diacritic removal;
- handling tatweel;
- controlled equivalence for selected letter forms;
- tokenization, stemming, typo tolerance, and Arabic/Latin transliteration policy;
- exact versus broad search by field.

Never destroy the original value. Version normalization logic so indexes can be rebuilt. Test Egyptian names and mixed Arabic/Latin product terms, not only dictionary words. Avoid aggressive equivalence for identifiers, passwords, legal names, or exact-match security fields.

## Phone numbers

- Accept human input at the API boundary, validate with maintained numbering metadata, and store a normalized international representation when valid.
- Retain a safe display/original value when it supports user confirmation or customer service; do not use it as the unique identity key without normalization.
- Keep verification state and timestamps separate from the phone value. A changed number is not verified because the previous number was.
- Normalize Arabic-Indic digits and every common Egyptian input format to E.164. Do not validate by operator prefix; number portability breaks that mapping.
- Mask numbers in responses and logs according to context. Protect account lookup endpoints from enumeration.

## Money and EGP

Never store or calculate money using binary floating point.

```text
Money {
  amount_minor: integer
  currency: ISO-style currency code, e.g. "EGP"
}
```

An exact decimal representation is also valid when scale rules are explicit. Define rounding per business operation, preserve line-item calculations needed for audit, and require currency on every monetary boundary. Formatting (`ج.م` versus `EGP`, separators, digits) belongs at presentation/template time.

- Make totals reproducible from immutable/recorded inputs where the domain requires it.
- Do not infer paid state from redirect success; reconcile with a verified provider result.
- Model initiated, action-required, pending, succeeded, failed, cancelled, refunded, and disputed states only as supported by the actual integration. Confirmation timing differs sharply by Egyptian payment method (reference codes and cash on delivery stay pending for hours or days); see the table in [references/egypt-data.md](references/egypt-data.md).

## Time and dates

- Store event instants as UTC with an unambiguous type.
- Store the relevant IANA time-zone identifier for future local schedules and recurring events.
- Render in the user's/product locale and zone at the edge. Do not hardcode Egypt as a fixed UTC offset; time-zone rules can change.
- Distinguish a calendar date (birthday/deadline date) from an instant (submission timestamp).
- Record source/provider timestamps and receipt timestamps for asynchronous events when reconciliation needs both.

## Locale negotiation

Choose locale from explicit account/profile preference, request override, and validated language headers in a documented precedence order. Return the effective locale when clients need to stay consistent. Reject unsupported arbitrary template locales safely and use a deterministic fallback.

APIs should return stable error codes plus safe structured parameters; clients choose localized UI text. Server-generated emails/SMS/WhatsApp messages use the recipient's stored/effective locale and a versioned template.

## Notification architecture

Model message intent separately from delivery channel:

```text
NotificationIntent -> TemplateRenderer(locale, version) -> ChannelAdapter -> Provider
                                    |                         |
                                  audit                    receipt/status
```

- Keep templates for Arabic and English structurally equivalent but naturally written.
- Validate required variables before enqueueing. Escape for the output channel.
- Use stable idempotency keys for events that must not notify twice.
- Queue delivery where appropriate, retry only retryable failures with backoff, and dead-letter/escalate terminal failures.
- Track provider message IDs and status transitions without exposing them as business truth beyond documented semantics.
- Do not log message bodies containing secrets, OTPs, or unnecessary personal data.

Read [references/provider-adapters.md](references/provider-adapters.md) before implementing a local integration.

## OTP and authentication

- Generate codes with a cryptographically secure generator. Store a keyed hash or equivalent verifier, not plaintext OTPs.
- Scope a challenge to purpose, destination, session/user context, expiry, and attempt counters.
- Enforce server-side expiry, one-time use, resend/cooldown, verification attempts, and rate limits across relevant IP/device/account/destination dimensions.
- A resend may invalidate older codes; make the rule explicit and test delayed delivery.
- Use generic responses where necessary to prevent account enumeration.
- Do not place OTPs in URLs, analytics, exception messages, or logs.
- Secure sessions with appropriate cookie/token controls, rotation/revocation, CSRF defense where applicable, and step-up authentication for sensitive actions.

## Uploads and documents

Egyptian products often collect national ID scans, certificates, and utility bills over slow mobile connections. Apply standard upload security (content-signature allowlists, server-generated names, private storage, authorization on every download) and add:

- resumable or chunked uploads with per-file retry, since users should not restart a form after a dropped connection;
- server-side image downscaling so phone photos of documents stay small;
- encryption, restricted access, and masking for identity documents and national ID numbers;
- explicit retention and deletion for every document purpose.

## Privacy, security, and audit logs

- Apply standard API security: object-level authorization, input limits, rate limits, secrets in managed configuration, and audit logs without OTPs, credentials, or full documents.
- Egypt's Personal Data Protection Law (Law No. 151 of 2020) applies to personal data of people in Egypt. Define purpose, retention, and deletion for phone numbers, addresses, national IDs, and documents, and confirm current obligations with counsel; see [references/egypt-data.md](references/egypt-data.md).

## Provider adapters

Define the capability the product needs, then adapt providers:

```text
interface MessageProvider {
  send(request, idempotencyKey) -> providerReference
  getStatus(providerReference) -> normalizedStatus
}
```

The adapter owns credentials, payload mapping, timeout, signature verification, error classification, and provider-specific identifiers. Domain services own business state and policy. Webhooks must verify authenticity using the provider's current official method, handle replay/idempotency, acknowledge promptly, and process durable work asynchronously when needed.

Never state that an SMS, WhatsApp, payment, identity, or address provider supports a feature until current official documentation and the account/environment confirm it.

## Framework application

- **FastAPI:** Use typed request/response models, dependency-based authentication, explicit background/queue boundaries, and database types that preserve exact money and timezone semantics. Framework background tasks are not automatically a durable queue.
- **Node.js:** Configure UTF-8 boundaries, use schema validation, exact money types/libraries, centralized error codes, and abort/timeouts for provider calls. Avoid floating-point coercion through JSON/business logic.
- **Next.js server environments:** Keep secrets and provider SDKs server-only, distinguish Node/edge runtime capabilities, validate server actions/route handlers, and do not trust locale or identity from client state alone.

Verify framework/version documentation before choosing middleware, runtime APIs, or deployment behavior.

## Testing

- Round-trip Arabic, mixed Arabic/Latin, emoji where allowed, combining marks, and long strings through database/API/queue/template paths.
- Property/test vectors for phone normalization, money arithmetic, date boundaries, locale fallback, and search normalization.
- OTP concurrency, expiry, resend, reuse, rate limit, enumeration resistance, and log redaction.
- Provider adapter contract tests plus recorded/sandbox fixtures where terms permit; never hit production in routine tests.
- Upload signature mismatch, oversized files, active content, unauthorized access, interrupted transfer, cleanup, and retention.
- Webhook invalid signature, replay, out-of-order delivery, duplicate events, and unknown statuses.

## Quality checklist

- [ ] UTF-8 and original Arabic values survive every storage and transport boundary.
- [ ] Search normalization is separate, versioned, and field-appropriate.
- [ ] Phones have normalized/display concerns separated; verification state is explicit.
- [ ] Money uses integer minor units or exact decimal with explicit currency, never float.
- [ ] Instants are UTC; calendar dates and future local schedules are modeled distinctly.
- [ ] Locale negotiation, fallback, error codes, and template versions are deterministic.
- [ ] Notifications and local integrations use capability-based adapters and idempotent delivery.
- [ ] OTP, authentication, uploads, logs, and webhooks pass security abuse cases.
- [ ] Current provider and regulatory claims are verified from official sources.
