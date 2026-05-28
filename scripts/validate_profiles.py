#!/usr/bin/env python3
"""Validate JSON-LD profile integrity and privacy fields.

This validator intentionally uses only the Python standard library. It checks
archival integrity and privacy guardrails; it does not verify historical truth
or civil identity.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any, Dict, List

REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_PROFILE_DIR = REPO_ROOT / "data" / "profiles"

REQUIRED_FIELDS = [
    "@context",
    "@type",
    "@id",
    "name",
    "identifier",
    "evidenceStatus",
    "privacyTier",
    "civilIdentityLinked",
    "sensitiveDataIncluded",
]


def is_empty(value: Any) -> bool:
    return value is None or value == "" or value == [] or value == {}


def validate_profile(path: Path) -> List[str]:
    errors: List[str] = []

    try:
        with path.open("r", encoding="utf-8") as handle:
            data: Dict[str, Any] = json.load(handle)
    except json.JSONDecodeError as error:
        return [f"invalid JSON: {error}"]

    if not isinstance(data, dict):
        return ["root JSON value must be an object"]

    for field in REQUIRED_FIELDS:
        if field not in data:
            errors.append(f"missing required field: {field}")

    for field in ["evidenceStatus", "privacyTier"]:
        if field in data and is_empty(data[field]):
            errors.append(f"field must not be empty: {field}")

    if data.get("civilIdentityLinked") is not False:
        errors.append("civilIdentityLinked must be false")

    if data.get("sensitiveDataIncluded") is not False:
        errors.append("sensitiveDataIncluded must be false")

    if "roleName" in data and not isinstance(data["roleName"], list):
        errors.append("roleName must be an array when present")

    return errors


def iter_profiles(profile_dir: Path) -> List[Path]:
    if not profile_dir.exists():
        return []
    return sorted(profile_dir.glob("*.jsonld"))


def main() -> int:
    profile_dir = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_PROFILE_DIR
    profiles = iter_profiles(profile_dir)

    if not profiles:
        print(f"FAIL no JSON-LD profile files found in {profile_dir}", file=sys.stderr)
        return 1

    failed = 0
    for path in profiles:
        errors = validate_profile(path)
        try:
            rel_path = path.relative_to(REPO_ROOT)
        except ValueError:
            rel_path = path
        if errors:
            failed += 1
            print(f"FAIL {rel_path}")
            for error in errors:
                print(f"  - {error}")
        else:
            print(f"OK   {rel_path}")

    if failed:
        print(f"\nValidation failed for {failed} profile file(s).", file=sys.stderr)
        return 1

    print(f"\nAll {len(profiles)} profile file(s) passed archival integrity checks.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
