# Notification Quality Evaluation

A release candidate must demonstrate:

- Cross-tenant requests are rejected.
- Duplicate requests produce one logical delivery.
- Marketing respects consent and unsubscribe state.
- Quiet hours and guardian controls are enforced.
- Tamil and English templates render correctly.
- Provider callbacks require valid signatures.
- Secrets and message content are redacted from logs.
- Retry exhaustion moves records to a dead-letter queue.
- Accessibility checks cover subject, body, links and status views.
- Load tests confirm channel and tenant rate limits.
- Backup, restore and delivery reconciliation are evidenced.

Passing policy validation is necessary but does not prove production readiness.
