#!/usr/bin/env python3
"""Build a Canal Barra participation index.

This script joins three evidence layers when available:

1. registered nicknames from the 2002 cadastro dataset;
2. IRContro attendance/caption datasets;
3. operator / master / ChanServ access datasets.

The goal is to identify historically visible participation patterns, not civil identities.

Safe filters produced by the output:

- registered + present in at least one IRContro;
- operator/master + present in at least one IRContro;
- registered + operator/master + present in at least one IRContro.
"""

from __future__ import annotations

import argparse
import csv
import re
import unicodedata
from collections import defaultdict
from pathlib import Path
from typing import Dict, Iterable, List, Set

DEFAULT_CADASTROS = Path("data/raw/2002-11-28/nicknames-2002-11-28-cadastros.csv")
DEFAULT_IRCONTROS_DIR = Path("data/raw/ircontros")
DEFAULT_GOVERNANCE_DIR = Path("data/raw/governance")
DEFAULT_OUTPUT = Path("data/processed/participation/canal-barra-participation-index.csv")

OUTPUT_FIELDS = [
    "normalized_nickname_key",
    "display_nickname_examples",
    "irc_syntax_status",
    "irc_syntax_invalid_examples",
    "registered_in_2002_cadastros",
    "cadastro_segments",
    "cadastro_record_ids",
    "operator_or_master",
    "operator_access_levels",
    "operator_source_records",
    "present_in_ircontro",
    "ircontro_event_ids",
    "ircontro_event_names",
    "ircontro_source_records",
    "participation_profile",
    "evidence_scope",
    "privacy_scope",
    "notes",
]

NICKNAME_COLUMNS = [
    "display_nickname",
    "nickname",
    "historical_nickname",
    "participant_nickname",
    "operator_nickname",
    "raw_nickname",
]

EVENT_ID_COLUMNS = ["event_id", "ircontro_id", "source_event_id"]
EVENT_NAME_COLUMNS = ["event_name", "ircontro_name", "event_title"]
ACCESS_LEVEL_COLUMNS = ["access_level", "chanserv_level", "level", "operator_level"]
RECORD_ID_COLUMNS = ["record_id", "source_record_id", "row_id"]

IRC_NICKNAME_PATTERN = re.compile(r"^[A-Za-z\[\]\\`_^{|}][A-Za-z0-9\-\[\]\\`_^{|}]{0,29}$")


def strip_accents(value: str) -> str:
    normalized = unicodedata.normalize("NFKD", value)
    return "".join(ch for ch in normalized if not unicodedata.combining(ch))


def normalize_nickname(value: str) -> str:
    value = value.strip()
    value = re.sub(r"^[+@%&~\s]+", "", value)
    value = strip_accents(value).lower()
    value = re.sub(r"\s+", "_", value)
    value = re.sub(r"[^a-z0-9_\-\[\]\|{}^`]+", "", value)
    return value.strip("_")


def is_valid_irc_nickname(value: str) -> bool:
    """Return whether a value is syntactically compatible with an IRC nickname.

    This is an archival syntax check only. Invalid display values may still be
    historically meaningful website labels, captions, ornamental aliases or OCR
    artifacts.
    """
    return bool(IRC_NICKNAME_PATTERN.fullmatch(value.strip()))


def irc_syntax_status(examples: Set[str]) -> str:
    if not examples:
        return "no_examples"
    valid_count = sum(1 for example in examples if is_valid_irc_nickname(example))
    if valid_count == len(examples):
        return "all_examples_valid"
    if valid_count > 0:
        return "mixed_examples"
    return "no_examples_valid"


def read_csv(path: Path) -> Iterable[Dict[str, str]]:
    with path.open("r", encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        for row in reader:
            yield {key: (value or "") for key, value in row.items()}


def first_existing(row: Dict[str, str], candidates: List[str]) -> str:
    for candidate in candidates:
        if candidate in row and row[candidate].strip():
            return row[candidate].strip()
    return ""


def iter_csv_files(path: Path) -> Iterable[Path]:
    if not path.exists():
        return []
    if path.is_file() and path.suffix.lower() == ".csv":
        return [path]
    return sorted(p for p in path.rglob("*.csv") if p.is_file())


def add_example(store: Dict[str, Set[str]], key: str, value: str) -> None:
    if value:
        store[key].add(value)


def main() -> int:
    parser = argparse.ArgumentParser(description="Build Canal Barra participation index from cadastro, IRContro and governance CSVs.")
    parser.add_argument("--cadastros", type=Path, default=DEFAULT_CADASTROS)
    parser.add_argument("--ircontros-dir", type=Path, default=DEFAULT_IRCONTROS_DIR)
    parser.add_argument("--governance-dir", type=Path, default=DEFAULT_GOVERNANCE_DIR)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()

    index: Dict[str, Dict[str, Set[str]]] = defaultdict(lambda: defaultdict(set))

    if args.cadastros.exists():
        for row in read_csv(args.cadastros):
            nickname = first_existing(row, NICKNAME_COLUMNS)
            key = normalize_nickname(nickname)
            if not key:
                continue
            index[key]["display_examples"].add(nickname)
            index[key]["registered"].add("true")
            add_example(index[key], "cadastro_segments", row.get("segment", ""))
            add_example(index[key], "cadastro_record_ids", row.get("record_id", ""))

    for path in iter_csv_files(args.ircontros_dir):
        for row in read_csv(path):
            nickname = first_existing(row, NICKNAME_COLUMNS)
            key = normalize_nickname(nickname)
            if not key:
                continue
            index[key]["display_examples"].add(nickname)
            index[key]["present_in_ircontro"].add("true")
            index[key]["ircontro_event_ids"].add(first_existing(row, EVENT_ID_COLUMNS) or path.stem)
            index[key]["ircontro_event_names"].add(first_existing(row, EVENT_NAME_COLUMNS) or path.stem)
            index[key]["ircontro_source_records"].add(first_existing(row, RECORD_ID_COLUMNS) or str(path))

    for path in iter_csv_files(args.governance_dir):
        for row in read_csv(path):
            nickname = first_existing(row, NICKNAME_COLUMNS)
            key = normalize_nickname(nickname)
            if not key:
                continue
            index[key]["display_examples"].add(nickname)
            index[key]["operator_or_master"].add("true")
            add_example(index[key], "operator_access_levels", first_existing(row, ACCESS_LEVEL_COLUMNS))
            index[key]["operator_source_records"].add(first_existing(row, RECORD_ID_COLUMNS) or str(path))

    args.output.parent.mkdir(parents=True, exist_ok=True)

    with args.output.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=OUTPUT_FIELDS)
        writer.writeheader()

        for key in sorted(index.keys()):
            item = index[key]
            registered = "true" if item.get("registered") else "false"
            operator = "true" if item.get("operator_or_master") else "false"
            ircontro = "true" if item.get("present_in_ircontro") else "false"

            if registered == "true" and operator == "true" and ircontro == "true":
                profile = "registered_operator_present_in_ircontro"
            elif operator == "true" and ircontro == "true":
                profile = "operator_present_in_ircontro"
            elif registered == "true" and ircontro == "true":
                profile = "registered_present_in_ircontro"
            elif registered == "true" and operator == "true":
                profile = "registered_operator"
            elif ircontro == "true":
                profile = "ircontro_presence_only"
            elif operator == "true":
                profile = "operator_only"
            else:
                profile = "registered_only"

            writer.writerow(
                {
                    "normalized_nickname_key": key,
                    "display_nickname_examples": " | ".join(sorted(item.get("display_examples", []))),
                    "irc_syntax_status": irc_syntax_status(item.get("display_examples", set())),
                    "irc_syntax_invalid_examples": " | ".join(
                        sorted(example for example in item.get("display_examples", set()) if not is_valid_irc_nickname(example))
                    ),
                    "registered_in_2002_cadastros": registered,
                    "cadastro_segments": " | ".join(sorted(item.get("cadastro_segments", []))),
                    "cadastro_record_ids": " | ".join(sorted(item.get("cadastro_record_ids", []))),
                    "operator_or_master": operator,
                    "operator_access_levels": " | ".join(sorted(item.get("operator_access_levels", []))),
                    "operator_source_records": " | ".join(sorted(item.get("operator_source_records", []))),
                    "present_in_ircontro": ircontro,
                    "ircontro_event_ids": " | ".join(sorted(item.get("ircontro_event_ids", []))),
                    "ircontro_event_names": " | ".join(sorted(item.get("ircontro_event_names", []))),
                    "ircontro_source_records": " | ".join(sorted(item.get("ircontro_source_records", []))),
                    "participation_profile": profile,
                    "evidence_scope": "historical_nickname_level_only",
                    "privacy_scope": "no_civil_identity_inference",
                    "notes": "This index joins nickname-level evidence only. It does not infer civil identity, residence or private relationships.",
                }
            )

    print(f"Wrote {len(index)} nickname participation rows to {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
