#!/usr/bin/env python3
"""Build a local JSONL corpus for Retrieval-Augmented Generation.

This script does not create embeddings and does not call any AI API.
It prepares clean, source-aware chunks that can later be loaded into ChromaDB,
PGVector, Pinecone, LlamaIndex, LangChain or another RAG pipeline.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
from pathlib import Path
from typing import Dict, Iterable, List

DEFAULT_OUTPUT = Path("data/processed/rag/canal-barra-rag-corpus.jsonl")
DEFAULT_PATHS = [
    Path("README.md"),
    Path("CITATION.cff"),
    Path("docs"),
    Path("schema"),
    Path("data/profiles"),
    Path("data/raw/ircontros"),
    Path("data/raw/governance"),
    Path("data/raw/2002-11-28"),
    Path("data/processed/geography"),
    Path("data/processed/participation"),
    Path("data/processed/timeline"),
    Path("data/processed/evaluation"),
    Path("data/processed/impact"),
    Path("data/processed/graph"),
]

TEXT_SUFFIXES = {".md", ".txt", ".json", ".jsonld", ".jsonl", ".csv", ".cff", ".yaml", ".yml"}
MAX_CHARS = 2400
OVERLAP_CHARS = 250


def sha256_text(value: str) -> str:
    return hashlib.sha256(value.encode("utf-8")).hexdigest()


def normalize_text(value: str) -> str:
    value = value.replace("\r\n", "\n").replace("\r", "\n")
    value = re.sub(r"\n{4,}", "\n\n\n", value)
    return value.strip()


def iter_files(paths: Iterable[Path]) -> Iterable[Path]:
    for path in paths:
        if not path.exists():
            continue
        if path.is_file() and path.suffix.lower() in TEXT_SUFFIXES:
            yield path
        elif path.is_dir():
            for item in sorted(path.rglob("*")):
                if item.is_file() and item.suffix.lower() in TEXT_SUFFIXES:
                    yield item


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def chunk_text(text: str, max_chars: int = MAX_CHARS, overlap_chars: int = OVERLAP_CHARS) -> List[str]:
    text = normalize_text(text)
    if not text:
        return []
    if len(text) <= max_chars:
        return [text]

    chunks: List[str] = []
    start = 0
    while start < len(text):
        end = min(start + max_chars, len(text))
        if end < len(text):
            paragraph_break = text.rfind("\n\n", start, end)
            if paragraph_break > start + max_chars // 2:
                end = paragraph_break
        chunks.append(text[start:end].strip())
        if end >= len(text):
            break
        start = max(0, end - overlap_chars)
    return [chunk for chunk in chunks if chunk]


def infer_source_type(path: Path) -> str:
    path_text = str(path)
    if path_text.startswith("docs/"):
        return "documentation"
    if path_text.startswith("schema/"):
        return "schema"
    if path_text.startswith("data/profiles/"):
        return "jsonld_profile"
    if path_text.startswith("data/raw/ircontros/"):
        return "raw_ircontro_dataset"
    if path_text.startswith("data/raw/governance/"):
        return "raw_governance_dataset"
    if path_text.startswith("data/raw/"):
        return "raw_dataset"
    if path_text.startswith("data/processed/"):
        return "processed_dataset"
    if path.name == "README.md":
        return "readme"
    return "repository_text"


def csv_summary(path: Path, text: str) -> Dict[str, object]:
    if path.suffix.lower() != ".csv":
        return {}
    lines = text.splitlines()
    if not lines:
        return {}
    try:
        reader = csv.reader(lines)
        headers = next(reader, [])
        row_count = sum(1 for _ in reader)
        return {"csv_headers": headers, "csv_row_count": row_count}
    except csv.Error:
        return {}


def build_records(paths: Iterable[Path]) -> Iterable[Dict[str, object]]:
    for path in iter_files(paths):
        text = read_text(path)
        extra_metadata = csv_summary(path, text)
        chunks = chunk_text(text)
        for index, chunk in enumerate(chunks, start=1):
            record = {
                "id": f"{path.as_posix()}::chunk-{index}",
                "source_path": path.as_posix(),
                "source_type": infer_source_type(path),
                "chunk_index": index,
                "chunk_count": len(chunks),
                "content_sha256": sha256_text(chunk),
                "text": chunk,
                "metadata": {
                    "project": "Canal Barra Digital Archaeology",
                    "privacy_scope": "repository_public_or_publication_ready_text",
                    "rag_use": "retrieval_context",
                    **extra_metadata,
                },
            }
            yield record


def main() -> int:
    parser = argparse.ArgumentParser(description="Build Canal Barra RAG-ready JSONL corpus.")
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("paths", nargs="*", type=Path, default=DEFAULT_PATHS)
    args = parser.parse_args()

    args.output.parent.mkdir(parents=True, exist_ok=True)
    count = 0
    with args.output.open("w", encoding="utf-8") as handle:
        for record in build_records(args.paths):
            handle.write(json.dumps(record, ensure_ascii=False, sort_keys=True) + "\n")
            count += 1

    print(f"Wrote {count} RAG corpus records to {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
