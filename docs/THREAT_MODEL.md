# Notification Threat Model

## Protected assets
Recipient identity, tenant boundaries, consent state, templates, provider credentials, message payloads, delivery metadata and audit evidence.

## Principal threats
- Cross-tenant recipient or template access
- Unauthorised bulk messaging
- Consent or quiet-hour bypass
- Template injection and malicious links
- PII leakage through payloads, logs or provider callbacks
- Replay and duplicate delivery
- Provider credential compromise
- Child-account messaging without guardian controls
- Notification flooding and denial of service
- Forged delivery callbacks

## Required controls
Authenticated APIs, tenant-derived authorisation, role checks, idempotency keys, signed provider callbacks, destination validation, template allowlists, consent enforcement, rate limiting, bounded retries, dead-letter queues, encryption, redacted logs and immutable audit records.

## Trust boundaries
Client to API gateway; service to message queue; worker to delivery provider; provider callback to webhook; tenant administrator to template governance.
