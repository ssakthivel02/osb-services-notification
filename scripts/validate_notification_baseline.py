from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def load(path: str) -> dict:
    return json.loads((ROOT / path).read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    policy = load("config/notification-policy.json")
    templates = load("config/template-policy.json")

    require(policy["apiVersion"] == "v1", "Versioned API policy is required")
    require(policy["authenticationRequired"], "Authentication must be required")
    require(policy["tenantIsolation"], "Tenant isolation must be enabled")
    require(policy["idempotencyRequired"], "Idempotency must be required")
    require(policy["consentRequiredForMarketing"], "Marketing consent must be enforced")
    require(policy["minorAccountsRequireGuardianControls"], "Guardian controls are required")
    require({"en-GB", "ta"}.issubset(policy["supportedLocales"]), "English and Tamil are required")
    require(policy["retry"]["deadLetterQueue"], "Dead-letter handling is required")
    require(templates["immutablePublishedVersions"], "Published templates must be immutable")
    require(templates["requiredApprovals"] >= 2, "Dual approval is required")
    require(templates["linkAllowlistRequired"], "Template links require an allowlist")
    require(templates["accessibilityReviewRequired"], "Accessibility review is required")

    print("Notification baseline validation passed")


if __name__ == "__main__":
    main()
