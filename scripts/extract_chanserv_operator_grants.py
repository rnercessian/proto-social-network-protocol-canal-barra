#!/usr/bin/env python3
"""
Extract ChanServ +o operator grants from Portuguese mIRC/BRASnet logs.

Target evidence pattern:

    *** ChanServ escolheu os modos: +o Nick

The script outputs nickname-level CSV evidence only. It does not parse ordinary
conversation and does not infer civil identity.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import re
from pathlib import Path
from typing import Dict, Iterator, List, Optional

NICK_RE = r"[A-Za-z0-9_\-\[\]\\`^{}|][A-Za-z0-9_\-\[\]\\`^{}|]{0,31}"
TIME_RE = re.compile(r"^\[(?P<time>\d{1,2}:\d{2}(?::\d{2})?)\]\s*(?P<body>.*)$")
CHANSERV_OP_RE = re.compile(
    rf"ChanServ\s+escolheu\s+os\s+modos\s*:\s*\+[^\s]*o[^\s]*(?:\s+(?P<nick>{NICK_RE}))",
    re.IGNORECASE,
)


def iter_files(paths: List[Path]) -> Iterator[Path]:
    for path in paths:
        if path.is_file():
            yield path
        elif path.is_dir():
            for candidate in sorted(path.rglob("*")):
                if candidate.is_file() and candidate.suffix.lower() in {".log", ".txt", ".irc", ".mirc"}:
                    yield candidate


def split_time(line: str) -> tuple[Optional[str], str]:
    clean = line.strip()
    match = TIME_RE.match(clean)
    if not match:
        return None, clean
    return match.group("time"), match.group("body").strip()


def evidence_id(source_label: str, file_path: Path, line_number: int, raw_line: str) -> str:
    digest = hashlib.sha1(
        f"{source_label}:{file_path}:{line_number}:{raw_line}".encode("utf-8", "replace")
    ).hexdigest()[:12]
    return f"cb_chanserv_op_{digest}"


def observed_at(date_value: Optional[str], time_value: Optional[str]) -> str:
    if date_value and time_value:
        if time_value.count(":") == 1:
            time_value = f"{time_value}:00"
        return f"{date_value}T{time_value}"
    return date_value or time_value or ""


def extract_file(file_path: Path, source_label: str, date_value: Optional[str], channel: str) -> List[Dict[str, str]]:
    rows: List[Dict[str, str]] = []

    with file_path.open("r", encoding="utf-8", errors="replace") as handle:
        for line_number, raw_line in enumerate(handle, start=1):
            time_value, body = split_time(raw_line)
            match = CHANSERV_OP_RE.search(body)
            if not match:
                continue

            nick = match.group("nick")
            rows.append(
                {
                    "evidence_id": evidence_id(source_label, file_path, line_number, raw_line),
                    "source_label": source_label,
                    "source_path": str(file_path),
                    "source_line": str(line_number),
                    "observed_at": observed_at(date_value, time_value),
                    "service": "ChanServ",
                    "channel": channel,
                    "mode": "+o",
                    "nickname": nick,
                    "event_type": "chanserv_operator_grant",
                    "evidence_status": "raw_log_match_needs_review",
                    "privacy_tier": "nickname_level_only",
                    "raw_match_redacted": f"ChanServ escolheu os modos: +o {nick}",
                }
            )

    return rows


def write_csv(rows: List[Dict[str, str]], output_path: Path) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    fields = [
        "evidence_id",
        "source_label",
        "source_path",
        "source_line",
        "observed_at",
        "service",
        "channel",
        "mode",
        "nickname",
        "event_type",
        "evidence_status",
        "privacy_tier",
        "raw_match_redacted",
    ]
    with output_path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def main() -> int:
    parser = argparse.ArgumentParser(description="Extract ChanServ +o operator grants from Portuguese mIRC/BRASnet logs.")
    parser.add_argument("paths", nargs="+", help="Log files or directories to scan.")
    parser.add_argument("--source-label", default="unlabeled-source")
    parser.add_argument("--date", default=None, help="Optional source date: YYYY-MM-DD.")
    parser.add_argument("--channel", default="#barra")
    parser.add_argument("--out", required=True, help="Output CSV path.")
    args = parser.parse_args()

    rows: List[Dict[str, str]] = []
    files_scanned = 0

    for file_path in iter_files([Path(item) for item in args.paths]):
        files_scanned += 1
        rows.extend(extract_file(file_path, args.source_label, args.date, args.channel))

    write_csv(rows, Path(args.out))
    unique_nicks = sorted({row["nickname"] for row in rows})

    print(f"Scanned files: {files_scanned}")
    print(f"ChanServ +o events found: {len(rows)}")
    print(f"Unique operator nicknames observed: {len(unique_nicks)}")
    if unique_nicks:
        print("Nicknames: " + ", ".join(unique_nicks))
    print(f"Wrote: {args.out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
