from __future__ import annotations

CASES = {
    "cross_tenant_recipient": "reject",
    "client_supplied_tenant_override": "reject",
    "missing_idempotency_key": "reject",
    "marketing_without_consent": "reject",
    "marketing_without_unsubscribe": "reject",
    "minor_without_guardian_controls": "reject",
    "unsigned_provider_callback": "reject",
    "duplicate_provider_callback": "ignore",
    "template_with_secret": "reject",
    "template_with_unapproved_link": "reject",
    "retry_after_max_attempts": "dead-letter",
    "quiet_hours_non_critical": "defer",
}


def main() -> None:
    assert len(CASES) >= 12
    assert all(outcome in {"reject", "ignore", "dead-letter", "defer"} for outcome in CASES.values())
    print("Notification negative safety cases defined")


if __name__ == "__main__":
    main()
