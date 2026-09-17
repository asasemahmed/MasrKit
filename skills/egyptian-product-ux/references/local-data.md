# Egypt-oriented local data boundaries

This reference defines product questions, not a permanent country database. Verify changing facts with current authoritative sources.

## Phone

Keep at least: raw/display input when useful for support, normalized international representation when validation succeeds, verification timestamp/status, and channel consent separately. Do not encode the full numbering plan in UI regexes. Libraries and metadata must be kept current.

## Address

Use stable internal identifiers for maintained governorate/locality datasets plus localized labels. Permit operational detail and landmarks without pretending they are formal administrative units. Version imported datasets and define fallback when a locality is missing.

## Money

Carry `{amount_minor, currency}` or an exact decimal plus explicit currency across boundaries. Display with the selected locale and product convention. Never derive payment status from UI navigation alone.

## Date and time

Store instants in UTC, retain the relevant IANA time zone for scheduled local events, and render for the user. Verify the current Egypt time-zone rules from maintained platform data; do not hardcode a fixed UTC offset.

## Evidence record

For any local constraint, record: claim, source owner, source URL/document, checked date, affected feature, fallback, and review trigger. A competitor screen is inspiration, not authoritative evidence.
