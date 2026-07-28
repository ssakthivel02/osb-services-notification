# Production Readiness Gate

Status: **NO-GO** until evidence exists for all items below.

- Running `/health`, `/ready` and versioned `/api/v1/notifications` endpoints
- Auth, role and tenant-isolation integration tests
- Consent, unsubscribe, quiet-hour and guardian-control tests
- Email, push, SMS and in-app provider integration tests
- Signed callback verification and replay protection
- Idempotency, retry, failover and dead-letter recovery tests
- Template approval, localisation and accessibility review
- PII redaction and retention enforcement
- Rate-limit, burst and notification-storm tests
- Monitoring dashboards, alerts and on-call ownership
- Backup, restore, reconciliation and incident-response exercises

Policy files and CI checks establish governance only; they do not certify a production service.
