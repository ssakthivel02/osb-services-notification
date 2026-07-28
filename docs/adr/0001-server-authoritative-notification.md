# ADR 0001: Server-authoritative notification delivery

## Decision
The notification service, not the client, owns recipient resolution, tenant scope, consent evaluation, quiet-hour enforcement, template version selection, rate limiting, idempotency and provider dispatch.

## Rationale
Client-authoritative delivery permits tenant spoofing, consent bypass, duplicate messages, template tampering and uncontrolled provider use.

## Consequences
Clients submit intent and business references only. The service derives protected attributes from trusted data, records every state transition and exposes bounded status information. Provider callbacks are authenticated and reconciled against existing delivery records.
