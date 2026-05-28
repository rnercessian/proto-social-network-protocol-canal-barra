#!/usr/bin/env python3
"""Count configured nickname occurrences across UFF 2004 PDF extracts.

This script reads:

- data/uff-2004/pdf-sources.csv
- data/uff-2004/nickname-search-targets.csv

It writes:

- data/uff-2004/nickname-occurrence-audit.csv
- data/uff-2004/nickname-occurrence-summary.csv

The search targets are editable in nickname-search-targets.csv.
The PDFs are expected to exist locally in data/uff-2004/sources/.

No civil identities are inferred. The script only counts literal nickname targets.
"""

from __future__ import annotations

import csv
import hashlib
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "data" / "uff-2004"
SOURCES_CSV = DATA_DIR / "pdf-sources.csv"
TARGETS_CSV = DATA_DIR / "nickname-search-targets.csv"
AUDIT_CSV = DATA_DIR / "nickname-occurrence-audit.csv"
SUMMARY_CSV = DATA_DIR / "nickname-occurrence-summary.csv"


@dataclass(frozen=True)
class PdfSource:
    source_id: str
    source_file: Path
    source_url: str
    expected_sha256: str
    status: str
    notes: str


@dataclass(frozen=True)
class NickTarget:
    nickname: str
    enabled: bool
    match_mode: str
    case_sensitive: bool
    reported_total: str
    notes: str


def read_csv(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        raise FileNotFoundError(f"Missing CSV: {path}")
    with path.open("r", encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def load_sources() -> list[PdfSource]:
    sources: list[PdfSource] = []
    for row in read_csv(SOURCES_CSV):
        sources.append(
            PdfSource(
                source_id=row["source_id"].strip(),
                source_file=(ROOT / row["source_file"].strip()).resolve(),
                source_url=row["source_url"].strip(),
                expected_sha256=row.get("sha256", "").strip(),
                status=row.get("status", "").strip(),
                notes=row.get("notes", "").strip(),
            )
        )
    return sources


def load_targets() -> list[NickTarget]:
    targets: list[NickTarget] = []
    for row in read_csv(TARGETS_CSV):
        enabled = row.get("enabled", "").strip().lower() in {"true", "1", "yes", "y"}
        targets.append(
            NickTarget(
                nickname=row["nickname"].strip(),
                enabled=enabled,
                match_mode=row.get("match_mode", "literal").strip() or "literal",
                case_sensitive=row.get("case_sensitive", "true").strip().lower() in {"true", "1", "yes", "y"},
                reported_total=row.get("reported_total", "").strip(),
                notes=row.get("notes", "").strip(),
            )
        )
    return [target for target in targets if target.enabled]


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def extract_pages(path: Path) -> list[str]:
    try:
        import pypdf  # type: ignore
    except ImportError as exc:
        raise SystemExit(
            "Missing dependency: pypdf. Install with: python3 -m pip install pypdf"
        ) from exc

    reader = pypdf.PdfReader(str(path))
    pages: list[str] = []
    for page in reader.pages:
        pages.append(page.extract_text() or "")
    return pages


def build_pattern(target: NickTarget) -> re.Pattern[str]:
    flags = 0 if target.case_sensitive else re.IGNORECASE
    literal = re.escape(target.nickname)

    if target.match_mode == "irc_nick":
        # IRC nick-ish boundary: avoid matching inside longer nick tokens.
        # Keeps punctuation such as trailing hyphen or underscore as part of the literal target.
        pattern = rf"(?<![A-Za-z0-9_\-\[\]\\`^{{}}|]){literal}(?![A-Za-z0-9_\-\[\]\\`^{{}}|])"
    elif target.match_mode == "word":
        pattern = rf"\b{literal}\b"
    else:
        pattern = literal

    return re.compile(pattern, flags)


def line_matches(text: str, pattern: re.Pattern[str]) -> Iterable[tuple[int, str, int]]:
    for line_number, line in enumerate(text.splitlines(), start=1):
        for match in pattern.finditer(line):
            yield line_number, line.strip(), match.start()


def detect_operator_action(line: str) -> bool:
    lowered = line.lower()
    markers = [
        "mode",
        "+o",
        "-o",
        "+b",
        "-b",
        "ban",
        "unban",
        "desban",
        "kick",
        "op",
        "deop",
    ]
    return any(marker in lowered for marker in markers)


def write_outputs() -> None:
    sources = load_sources()
    targets = load_targets()

    audit_rows: list[dict[str, object]] = []
    summary: dict[tuple[str, str], int] = {}
    missing_sources: list[str] = []
    sha_warnings: list[str] = []

    for source in sources:
        if not source.source_file.exists():
            missing_sources.append(str(source.source_file.relative_to(ROOT)))
            continue

        actual_sha = sha256_file(source.source_file)
        if source.expected_sha256 and actual_sha != source.expected_sha256:
            sha_warnings.append(
                f"SHA mismatch for {source.source_id}: expected {source.expected_sha256}, got {actual_sha}"
            )

        pages = extract_pages(source.source_file)
        for pdf_page, page_text in enumerate(pages, start=1):
            for target in targets:
                pattern = build_pattern(target)
                for line_number, line_text, _ in line_matches(page_text, pattern):
                    occurrence_id = f"{source.source_id}-p{pdf_page:03d}-l{line_number:04d}-{target.nickname}"
                    operator_action = detect_operator_action(line_text)
                    audit_rows.append(
                        {
                            "occurrence_id": occurrence_id,
                            "nickname": target.nickname,
                            "normalized_nickname": target.nickname,
                            "source_id": source.source_id,
                            "source_file": str(source.source_file.relative_to(ROOT)),
                            "source_url": source.source_url,
                            "source_sha256": actual_sha,
                            "pdf_page": pdf_page,
                            "printed_page": "",
                            "section": "",
                            "excerpt_id": f"{source.source_id}:p{pdf_page}:l{line_number}",
                            "line_text": line_text,
                            "match_type": target.match_mode,
                            "operator_action_detected": str(operator_action).lower(),
                            "duplicate_group_id": "",
                            "is_duplicate": "false",
                            "verification_status": "machine_extracted_pending_human_review",
                            "notes": "Generated by scripts/count_uff_pdf_nicknames.py; page numbers are PDF pages, not printed dissertation pages.",
                        }
                    )
                    summary[(target.nickname, source.source_id)] = summary.get((target.nickname, source.source_id), 0) + 1

    fieldnames = [
        "occurrence_id",
        "nickname",
        "normalized_nickname",
        "source_id",
        "source_file",
        "source_url",
        "source_sha256",
        "pdf_page",
        "printed_page",
        "section",
        "excerpt_id",
        "line_text",
        "match_type",
        "operator_action_detected",
        "duplicate_group_id",
        "is_duplicate",
        "verification_status",
        "notes",
    ]

    DATA_DIR.mkdir(parents=True, exist_ok=True)
    with AUDIT_CSV.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(audit_rows)

    summary_fieldnames = [
        "nickname",
        "source_id",
        "machine_count",
        "reported_total",
        "verification_status",
        "notes",
    ]
    reported_by_nick = {target.nickname: target.reported_total for target in targets}
    with SUMMARY_CSV.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=summary_fieldnames)
        writer.writeheader()
        for target in targets:
            total = 0
            for source in sources:
                count = summary.get((target.nickname, source.source_id), 0)
                total += count
                writer.writerow(
                    {
                        "nickname": target.nickname,
                        "source_id": source.source_id,
                        "machine_count": count,
                        "reported_total": reported_by_nick.get(target.nickname, ""),
                        "verification_status": "machine_count_pending_human_review",
                        "notes": "Source file missing" if not source.source_file.exists() else "",
                    }
                )
            writer.writerow(
                {
                    "nickname": target.nickname,
                    "source_id": "combined_public_extract_set",
                    "machine_count": total,
                    "reported_total": reported_by_nick.get(target.nickname, ""),
                    "verification_status": "machine_count_pending_human_review_and_deduplication",
                    "notes": "Combined machine count across configured PDF sources; deduplication and OCR/PDF extraction quality review still required.",
                }
            )

    print(f"Wrote {AUDIT_CSV.relative_to(ROOT)} ({len(audit_rows)} rows)")
    print(f"Wrote {SUMMARY_CSV.relative_to(ROOT)}")

    if missing_sources:
        print("Missing source PDFs:", file=sys.stderr)
        for source in missing_sources:
            print(f"- {source}", file=sys.stderr)

    if sha_warnings:
        print("SHA warnings:", file=sys.stderr)
        for warning in sha_warnings:
            print(f"- {warning}", file=sys.stderr)


if __name__ == "__main__":
    write_outputs()
