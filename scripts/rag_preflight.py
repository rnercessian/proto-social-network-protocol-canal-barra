#!/usr/bin/env python3
"""Preflight check for the Canal Barra RAG pipeline.

This script uses only the Python standard library.
It does not call OpenAI, LlamaIndex or any external service.
Its job is to confirm that the repository contains enough local evidence files
for the RAG ingestion scripts to work later.
"""

from __future__ import annotations

import csv
import json
from pathlib import Path
from typing import Dict, List

REPO_ROOT = Path(__file__).resolve().parents[1]

REQUIRED_PATHS = [
    "README.md",
    "CITATION.cff",
    "requirements-llamaindex.txt",
    "scripts/llamaindex_ingestion.py",
    "scripts/llamaindex_query.py",
    "schema/user-profile-schema.json",
    "data/profiles/barman.jsonld",
    "data/raw/governance/access-list-2000-12.csv",
    "data/raw/ircontros/rosa-dos-ventos-2001-02-21.csv",
    "data/raw/2002-11-28/nicknames-2002-11-28-cadastros.csv",
]


def check_paths() -> bool:
    ok = True
    print("Checking required files...")
    for rel in REQUIRED_PATHS:
        path = REPO_ROOT / rel
        if path.exists():
            print(f"OK   {rel}")
        else:
            print(f"MISS {rel}")
            ok = False
    return ok


def read_csv(path: Path) -> List[Dict[str, str]]:
    with path.open("r", encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def check_access_list() -> bool:
    path = REPO_ROOT / "data/raw/governance/access-list-2000-12.csv"
    if not path.exists():
        return False
    rows = read_csv(path)
    masters = [row for row in rows if row.get("role_group") == "master"]
    operators = [row for row in rows if row.get("role_group") == "operator"]
    founder = [row for row in rows if row.get("role_group") == "founder"]
    print("\nGovernance access-list summary:")
    print(f"founder rows:   {len(founder)}")
    print(f"master rows:    {len(masters)}")
    print(f"operator rows:  {len(operators)}")
    print("masters:", ", ".join(row.get("display_nickname", "") for row in masters))
    return bool(founder and masters and operators)


def check_ircontro_rows() -> bool:
    base = REPO_ROOT / "data/raw/ircontros"
    if not base.exists():
        return False
    total_rows = 0
    files = sorted(base.glob("*.csv"))
    print("\nIRContro dataset summary:")
    for path in files:
        rows = read_csv(path)
        total_rows += len(rows)
        print(f"{path.name}: {len(rows)} rows")
    print(f"total IRContro caption rows: {total_rows}")
    return total_rows > 0


def check_profile_jsonld() -> bool:
    path = REPO_ROOT / "data/profiles/barman.jsonld"
    if not path.exists():
        return False
    data = json.loads(path.read_text(encoding="utf-8"))
    print("\nProfile JSON-LD summary:")
    print("identifier:", data.get("identifier"))
    print("roles:", ", ".join(data.get("roleName", [])))
    print("evidenceStatus:", data.get("evidenceStatus"))
    print("privacyTier:", data.get("privacyTier"))
    return data.get("identifier") == "BarMan"


def main() -> int:
    checks = [
        check_paths(),
        check_access_list(),
        check_ircontro_rows(),
        check_profile_jsonld(),
    ]
    print("\nPreflight result:")
    if all(checks):
        print("OK - Repository is ready for local RAG ingestion.")
        return 0
    print("FAIL - Repository is missing required files or minimum data.")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
