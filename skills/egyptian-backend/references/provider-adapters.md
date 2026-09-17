# Provider adapter review

Before integrating any Egypt-relevant payment, SMS, WhatsApp, identity, address, delivery, or notification provider:

1. Link the current official API documentation and record the checked date/version.
2. Confirm account, country, currency, environment, and approval constraints with the actual product account.
3. Define only required capabilities: send, authorize, capture, refund, status, webhook, or equivalent.
4. Map provider states into a conservative domain state machine. Preserve unknown states for investigation; do not label them successful.
5. Set connect/read/overall timeouts, retry categories, idempotency behavior, and circuit/queue strategy.
6. Verify webhook signatures exactly as documented, protect replay, and handle duplicates/out-of-order events.
7. Redact credentials, message content, documents, tokens, and unnecessary personal data from logs.
8. Provide a fake adapter for deterministic tests and a sandbox adapter only when the provider officially supports it.
9. Define migration/disable behavior so the domain is not locked to provider payloads or IDs.
10. Document operational ownership, reconciliation, alerts, and user-facing fallback.

Treat provider marketing pages and third-party examples as discovery material, not authoritative integration contracts.
