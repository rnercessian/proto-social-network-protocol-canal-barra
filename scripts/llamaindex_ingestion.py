#!/usr/bin/env python3
"""Build a local LlamaIndex archive for the Canal Barra repository.

This script reads local repository files only. It does not use GitHub tokens.
It creates a persistent index under .rag/llamaindex.
"""

from __future__ import annotations

import argparse
import csv
import json
import re
from pathlib import Path
from typing import Any, Dict, Iterable, List, Tuple

from llama_index.core import Document, Settings, StorageContext, VectorStoreIndex
from llama_index.core.node_parser import SentenceSplitter
from llama_index.embeddings.openai import OpenAIEmbedding
from llama_index.llms.openai import OpenAI

REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_PERSIST_DIR = REPO_ROOT / ".rag" / "llamaindex"
DEFAULT_INPUTS = [
    "README.md",
    "CITATION.cff",
    "docs",
    "schema",
    "data/profiles",
    "data/raw/ircontros",
    "data/raw/governance",
    "data/raw/2002-11-28",
    "data/processed",
]
TEXT_EXTENSIONS = {".md", ".txt", ".json", ".jsonld", ".jsonl", ".csv", ".cff", ".yaml", ".yml"}


def relative(path: Path) -> str:
    return path.resolve().relative_to(REPO_ROOT).as_posix()


def iter_files(inputs: Iterable[str]) -> Iterable[Path]:
    for item in inputs:
        path = REPO_ROOT / item
        if not path.exists():
            continue
        if path.is_file() and path.suffix.lower() in TEXT_EXTENSIONS:
            yield path
        if path.is_dir():
            for child in sorted(path.rglob("*")):
                if child.is_file() and child.suffix.lower() in TEXT_EXTENSIONS:
                    yield child


def source_type(path: Path) -> str:
    rel = relative(path)
    if rel.startswith("docs/"):
        return "historiographical_markdown"
    if rel.startswith("schema/"):
        return "schema"
    if rel.startswith("data/profiles/"):
        return "profile_jsonld"
    if rel.startswith("data/raw/ircontros/"):
        return "raw_ircontro_dataset"
    if rel.startswith("data/raw/governance/"):
        return "raw_governance_dataset"
    if rel.startswith("data/raw/"):
        return "raw_dataset"
    if rel.startswith("data/processed/"):
        return "processed_dataset"
    if rel == "README.md":
        return "readme"
    if rel == "CITATION.cff":
        return "citation"
    return "repository_text"


def json_metadata(data: Any) -> Dict[str, str]:
    if not isinstance(data, dict):
        return {}
    metadata: Dict[str, str] = {}
    for key in ["@id", "@type", "name", "identifier", "evidenceStatus", "privacyTier"]:
        if key in data:
            metadata[key.replace("@", "jsonld_")] = str(data[key])
    if isinstance(data.get("roleName"), list):
        metadata["roleName"] = " | ".join(str(v) for v in data["roleName"])
    if isinstance(data.get("about"), dict):
        metadata["about_name"] = str(data["about"].get("name", ""))
        metadata["about_type"] = str(data["about"].get("@type", ""))
    if isinstance(data.get("sameAsNicknameInSources"), list):
        metadata["sameAsNicknameInSources"] = " | ".join(str(v) for v in data["sameAsNicknameInSources"])
    return metadata


def flatten_json(data: Any, prefix: str = "") -> List[str]:
    rows: List[str] = []
    if isinstance(data, dict):
        for key, value in data.items():
            next_prefix = f"{prefix}.{key}" if prefix else str(key)
            rows.extend(flatten_json(value, next_prefix))
    elif isinstance(data, list):
        for index, value in enumerate(data):
            rows.extend(flatten_json(value, f"{prefix}[{index}]"))
    else:
        rows.append(f"{prefix}: {data}")
    return rows


def split_markdown_by_heading(text: str) -> List[Tuple[str, str]]:
    chunks: List[Tuple[str, str]] = []
    heading = ""
    lines: List[str] = []
    for line in text.splitlines():
        match = re.match(r"^(#{1,6})\s+(.+)$", line)
        if match and lines:
            chunks.append((heading, "\n".join(lines).strip()))
            lines = []
        if match:
            heading = match.group(2).strip()
        lines.append(line)
    if lines:
        chunks.append((heading, "\n".join(lines).strip()))
    return [(h, c) for h, c in chunks if c]


def csv_to_documents(path: Path, base_metadata: Dict[str, str]) -> List[Document]:
    text = path.read_text(encoding="utf-8", errors="replace")
    rows = list(csv.DictReader(text.splitlines()))
    documents: List[Document] = []
    batch: List[str] = []
    batch_start = 1
    for index, row in enumerate(rows, start=1):
        row_text = " | ".join(f"{k}={v}" for k, v in row.items() if v)
        if sum(len(item) for item in batch) + len(row_text) > 1800 and batch:
            metadata = {**base_metadata, "csv_row_start": str(batch_start), "csv_row_end": str(index - 1)}
            documents.append(Document(text="\n".join(batch), metadata=metadata))
            batch = []
            batch_start = index
        batch.append(row_text)
    if batch:
        metadata = {**base_metadata, "csv_row_start": str(batch_start), "csv_row_end": str(len(rows))}
        documents.append(Document(text="\n".join(batch), metadata=metadata))
    return documents


def parse_file(path: Path) -> List[Document]:
    rel = relative(path)
    base_metadata = {
        "source_path": rel,
        "source_type": source_type(path),
        "context": "canal_barra_brasnet_irc_digital_archaeology",
    }
    suffix = path.suffix.lower()
    text = path.read_text(encoding="utf-8", errors="replace").strip()

    if suffix == ".csv":
        return csv_to_documents(path, base_metadata)

    if suffix in {".json", ".jsonld"}:
        try:
            data = json.loads(text)
            metadata = {**base_metadata, **json_metadata(data)}
            body = "\n".join(flatten_json(data))
            return [Document(text=body, metadata=metadata)]
        except json.JSONDecodeError:
            return [Document(text=text, metadata=base_metadata)]

    if suffix == ".md":
        return [
            Document(text=chunk, metadata={**base_metadata, "section_heading": heading})
            for heading, chunk in split_markdown_by_heading(text)
        ]

    return [Document(text=text, metadata=base_metadata)]


def build_index(args: argparse.Namespace) -> None:
    Settings.llm = OpenAI(model=args.llm_model, temperature=0.1)
    Settings.embed_model = OpenAIEmbedding(model=args.embedding_model)
    Settings.node_parser = SentenceSplitter(chunk_size=args.chunk_size, chunk_overlap=args.chunk_overlap)

    documents: List[Document] = []
    for path in iter_files(args.inputs):
        documents.extend(parse_file(path))

    if not documents:
        raise RuntimeError("No documents found for ingestion.")

    print(f"Loaded {len(documents)} source documents/sections.")
    index = VectorStoreIndex.from_documents(documents, show_progress=True)
    index.storage_context.persist(persist_dir=str(args.persist_dir))
    print(f"LlamaIndex archive saved to {args.persist_dir}")


def main() -> int:
    parser = argparse.ArgumentParser(description="Build local LlamaIndex archive for Canal Barra.")
    parser.add_argument("--persist-dir", type=Path, default=DEFAULT_PERSIST_DIR)
    parser.add_argument("--llm-model", default="gpt-4o-mini")
    parser.add_argument("--embedding-model", default="text-embedding-3-large")
    parser.add_argument("--chunk-size", type=int, default=900)
    parser.add_argument("--chunk-overlap", type=int, default=120)
    parser.add_argument("inputs", nargs="*", default=DEFAULT_INPUTS)
    args = parser.parse_args()
    build_index(args)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
