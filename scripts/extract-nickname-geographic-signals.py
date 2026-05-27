#!/usr/bin/env python3
"""Extract geographic self-presentation signals from Canal Barra nickname datasets.

This script does not infer residence, civil identity, address or private location.
It only extracts explicit geographic tokens that appear inside historical nicknames.
"""

from __future__ import annotations

import argparse
import csv
import re
import unicodedata
from pathlib import Path
from typing import Dict, Iterable, List

DEFAULT_INPUT = Path("data/raw/2002-11-28/nicknames-2002-11-28-cadastros.csv")
DEFAULT_OUTPUT = Path("data/processed/geography/nickname-geographic-signals-2002.csv")
DEFAULT_SOURCE_CAPTURE_DATE = "2002-12-17"

OUTPUT_FIELDS = [
    "source_record_id",
    "snapshot_date",
    "source_capture_date",
    "segment",
    "list_position",
    "display_nickname",
    "raw_line",
    "matched_signal",
    "normalized_place",
    "place_type",
    "confidence",
    "inference_scope",
    "residence_claim",
    "notes",
]

# Keep this list conservative. The goal is a defensible signal extraction,
# not aggressive geolocation.
GEOGRAPHIC_PATTERNS: List[Dict[str, str]] = [
    {"signal": "barra", "place": "Barra da Tijuca", "type": "neighborhood", "confidence": "high", "pattern": r"barra"},
    {"signal": "recreio", "place": "Recreio dos Bandeirantes", "type": "neighborhood", "confidence": "high", "pattern": r"recreio"},
    {"signal": "jpa", "place": "Jacarepaguá", "type": "neighborhood_area", "confidence": "medium", "pattern": r"(^|[^a-z0-9])jpa([^a-z0-9]|$)"},
    {"signal": "jacarepagua", "place": "Jacarepaguá", "type": "neighborhood_area", "confidence": "high", "pattern": r"jacarepagua"},
    {"signal": "copa", "place": "Copacabana", "type": "neighborhood", "confidence": "medium", "pattern": r"(^|[^a-z0-9])copa([^a-z0-9]|$)"},
    {"signal": "copacabana", "place": "Copacabana", "type": "neighborhood", "confidence": "high", "pattern": r"copacabana"},
    {"signal": "ipanema", "place": "Ipanema", "type": "neighborhood", "confidence": "high", "pattern": r"ipanema"},
    {"signal": "leblon", "place": "Leblon", "type": "neighborhood", "confidence": "high", "pattern": r"leblon"},
    {"signal": "leme", "place": "Leme", "type": "neighborhood", "confidence": "high", "pattern": r"(^|[^a-z0-9])leme([^a-z0-9]|$)"},
    {"signal": "tijuca", "place": "Tijuca", "type": "neighborhood", "confidence": "high", "pattern": r"tijuca"},
    {"signal": "meier", "place": "Méier", "type": "neighborhood", "confidence": "high", "pattern": r"meier"},
    {"signal": "urca", "place": "Urca", "type": "neighborhood", "confidence": "high", "pattern": r"urca"},
    {"signal": "botafogo", "place": "Botafogo", "type": "neighborhood", "confidence": "high", "pattern": r"botafogo"},
    {"signal": "humaita", "place": "Humaitá", "type": "neighborhood", "confidence": "high", "pattern": r"humaita"},
    {"signal": "vila_isabel", "place": "Vila Isabel", "type": "neighborhood", "confidence": "high", "pattern": r"vila[^a-z0-9]*isabel"},
    {"signal": "freguesia", "place": "Freguesia", "type": "neighborhood_area", "confidence": "high", "pattern": r"freguesia"},
    {"signal": "penha", "place": "Penha", "type": "neighborhood", "confidence": "high", "pattern": r"penha"},
    {"signal": "gloria", "place": "Glória", "type": "neighborhood", "confidence": "high", "pattern": r"gloria"},
    {"signal": "ilha", "place": "Ilha do Governador / Ilha-area signal", "type": "area_signal", "confidence": "medium", "pattern": r"(^|[^a-z0-9])ilha([^a-z0-9]|$)"},
    {"signal": "novo_leblon", "place": "Novo Leblon / Barra da Tijuca locality", "type": "locality", "confidence": "medium", "pattern": r"novo[^a-z0-9]*leblon"},
    {"signal": "zs", "place": "Zona Sul", "type": "city_zone", "confidence": "medium", "pattern": r"(^|[^a-z0-9])zs([^a-z0-9]|$)"},
    {"signal": "rio_rj", "place": "Rio de Janeiro", "type": "city_or_state_signal", "confidence": "medium", "pattern": r"(^|[^a-z0-9])(rio|rj)([^a-z0-9]|$)"},
]


def normalize_text(value: str) -> str:
    normalized = unicodedata.normalize("NFKD", value)
    ascii_text = "".join(ch for ch in normalized if not unicodedata.combining(ch))
    return ascii_text.lower()


def find_geo_signals(nickname: str) -> Iterable[Dict[str, str]]:
    normalized = normalize_text(nickname)
    for item in GEOGRAPHIC_PATTERNS:
        if re.search(item["pattern"], normalized, flags=re.IGNORECASE):
            yield item


def build_output_row(input_row: Dict[str, str], match: Dict[str, str], source_capture_date: str) -> Dict[str, str]:
    return {
        "source_record_id": input_row.get("record_id", ""),
        "snapshot_date": input_row.get("snapshot_date", ""),
        "source_capture_date": source_capture_date,
        "segment": input_row.get("segment", ""),
        "list_position": input_row.get("list_position", ""),
        "display_nickname": input_row.get("display_nickname", ""),
        "raw_line": input_row.get("raw_line", ""),
        "matched_signal": match["signal"],
        "normalized_place": match["place"],
        "place_type": match["type"],
        "confidence": match["confidence"],
        "inference_scope": "nickname_geographic_signal_only",
        "residence_claim": "false",
        "notes": "Geographic token appears in historical nickname; this is not proof of residence.",
    }


def extract(input_path: Path, output_path: Path, source_capture_date: str) -> int:
    if not input_path.exists():
        raise FileNotFoundError(f"Input file not found: {input_path}")

    output_path.parent.mkdir(parents=True, exist_ok=True)

    count = 0
    with input_path.open("r", encoding="utf-8", newline="") as source_file, output_path.open(
        "w", encoding="utf-8", newline=""
    ) as output_file:
        reader = csv.DictReader(source_file)
        writer = csv.DictWriter(output_file, fieldnames=OUTPUT_FIELDS)
        writer.writeheader()

        for row in reader:
            nickname = row.get("display_nickname", "")
            for match in find_geo_signals(nickname):
                writer.writerow(build_output_row(row, match, source_capture_date))
                count += 1

    return count


def main() -> int:
    parser = argparse.ArgumentParser(description="Extract geographic nickname signals from Canal Barra cadastro CSV.")
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--source-capture-date", default=DEFAULT_SOURCE_CAPTURE_DATE)
    args = parser.parse_args()

    count = extract(args.input, args.output, args.source_capture_date)
    print(f"Wrote {count} geographic signal rows to {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
