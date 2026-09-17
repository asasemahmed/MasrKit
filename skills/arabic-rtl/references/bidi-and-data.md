# Bidirectional data reference

| Data | Typical internal direction | Rendering guidance |
|---|---|---|
| Arabic prose | RTL | Inherit from Arabic locale root |
| Phone number | LTR | `dir="ltr"`; keep country code and digits together |
| Email / URL | LTR | `<bdi dir="ltr">` in prose; LTR editable input |
| Order ID / code | Usually LTR | Isolate; do not translate or reverse |
| Currency amount | Locale-formatted | Format value and currency together; test sign and punctuation |
| Date/time | Locale-formatted | Use locale formatter; isolate if embedded punctuation is unstable |
| Source code | LTR | LTR code block; surrounding explanation can remain RTL |
| User-generated text | Unknown | Consider `dir="auto"` per item; sanitize independently |

For plain-text channels without markup, use Unicode FSI (U+2068) and PDI (U+2069) around unknown or opposite-direction tokens when the delivery channel preserves them. Treat LRM/RLM and embedding/override controls as specialized tools, not a routine fix. Log/debug escaped code points when diagnosing invisible-control problems.
