# Egypt-oriented local data boundaries

This reference defines product questions, canonical datasets, and domain structures for Egyptian applications. Verify changing facts with current authoritative sources. For concrete Egyptian values (formats, zones, payment methods), see [egypt-facts.md](egypt-facts.md).

## 1. Phone

Keep at least: raw/display input when useful for support, normalized international representation when validation succeeds, verification timestamp/status, and channel consent separately. Do not encode the full numbering plan in UI regexes. Libraries and metadata must be kept current.

- Local prefix: `010`, `011`, `012`, `015`. (Operator prefixes are historical and do not reliably identify operators after number portability).
- International E.164 form: `+20 10...` / `+20 11...` / `+20 12...` / `+20 15...` (total 10 digits after `+20`).
- Input rendering: Visually `dir="ltr"` with `inputmode="tel"` and `autocomplete="tel"`.

---

## 2. Money and EGP

Carry `{amount_minor, currency}` or an exact decimal plus explicit currency across boundaries. Display with the selected locale and product convention. Never derive payment status from UI navigation alone.

---

## 3. Date and time

Store instants in UTC, retain the relevant IANA time zone for scheduled local events, and render for the user. Verify the current Egypt time-zone rules from maintained platform data; do not hardcode a fixed UTC offset.

---

## 4. Evidence record

For any local constraint, record: claim, source owner, source URL/document, checked date, affected feature, fallback, and review trigger. A competitor screen is inspiration, not authoritative evidence.
