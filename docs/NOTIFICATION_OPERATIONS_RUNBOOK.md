# Notification Operations Runbook

## Signals
Monitor enqueue rate, accepted rate, provider success, bounce and complaint rates, retry depth, dead-letter depth, callback failures, latency percentiles and tenant throttling.

## Incident playbooks
1. Provider outage: pause non-critical traffic, fail over approved provider, preserve ordering and idempotency.
2. Notification storm: activate tenant kill switch, inspect source event and revoke compromised credentials.
3. PII exposure: stop affected channel, preserve evidence, rotate secrets, notify privacy and security owners.
4. Callback forgery: reject unsigned callbacks, rotate webhook secret and reconcile delivery status.
5. Consent breach: suppress campaign, identify recipients, preserve audit data and start corrective review.

## Recovery
Replay only from the durable queue using the original idempotency key. Never replay dead-letter items without cause classification and approval.
