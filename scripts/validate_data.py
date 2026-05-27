#!/usr/bin/env python3
"""Validate Canal Barra JSON-LD profile data against repository schemas.

This script intentionally validates structure only.
It does not verify historical truth, civil identity, residence, relationships or private attributes.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any, Dict, Iterable

try:
    import jsonschema
    from jsonschema import Draft202012Validator
except ImportError:  # pragma: no cover
    print("Missing dependency: jsonschema. Install with: python3 -m pip install jsonschema", file=sys.stderr)
    raise SystemExit(2)

DEFAULT_SCHEMA = Path("schema/user-profile-schema.json")
DEFAULT_DATA_DIR = Path("data/profiles")


def load_json(path: Path) -> Dict[str, Any]:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def iter_jsonld_files(path: Path) -> Iterable[Path]:
    if not path.exists():
        return []
    return sorted(
        item for item in path.rglob("*")
        if item.is_file() and item.suffix.lower() in {".json", ".jsonld"}
    )


def validate_repository(schema_path: Path, data_dir: Path) -> int:
    print("Starting Canal Barra JSON-LD validation...\n")

    if not schema_path.exists():
        print(f"Schema not found: {schema_path}", file=sys.stderr)
        return 2

    schema = load_json(schema_path)
    validator = Draft202012Validator(schema)
    files = list(iter_jsonld_files(data_dir))

    if not files:
        print(f"No JSON/JSON-LD profile files found in: {data_dir}", file=sys.stderr)
        return 1

    failed = 0
    for file_path in files:
        try:
            instance = load_json(file_path)
        except json.JSONDecodeError as error:
            print(f"FAIL {file_path}: invalid JSON -> {error}")
            failed += 1
            continue

        errors = sorted(validator.iter_errors(instance), key=lambda item: list(item.path))
        if errors:
            print(f"FAIL {file_path}")
            for error in errors:
                path = ".".join(str(part) for part in error.path) or "<root>"
                print(f"  - {path}: {error.message}")
            failed += 1
        else:
            print(f"OK   {file_path}")

    print()
    if failed:
        print(f"Validation finished with {failed} failing file(s).")
        return 1

    print("All JSON-LD profile files match the repository schema.")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate Canal Barra JSON-LD profile data.")
    parser.add_argument("--schema", type=Path, default=DEFAULT_SCHEMA)
    parser.add_argument("--data-dir", type=Path, default=DEFAULT_DATA_DIR)
    args = parser.parse_args()

    return validate_repository(args.schema, args.data_dir)


if __name__ == "__main__":
    raise SystemExit(main())
