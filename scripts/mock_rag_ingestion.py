#!/usr/bin/env python3
"""
Canal Barra - Digital Archaeology RAG Ingestion Pipeline
========================================================

This script demonstrates how to ingest, parse and index the Canal Barra
Digital Archaeology repository using LlamaIndex.

It is intentionally a mock / reference pipeline:

- It reads local repository folders only.
- It does not require a GitHub token.
- It can run in mock mode without an OpenAI API key.
- It preserves source paths as metadata for RAG and academic traceability.
- It teaches AI agents and engineers how the repository should be read.

Author: rnercessian & The Canal Barra Digital Archaeology Project (2026)
"""

from __future__ import annotations

import os
from pathlib import Path
from typing import Iterable, List

try:
    from llama_index.core import Document, Settings, SimpleDirectoryReader, VectorStoreIndex
    from llama_index.core.node_parser import SentenceSplitter
    from llama_index.core.embeddings import MockEmbedding
    from llama_index.core.llms import MockLLM
except ImportError as exc:  # pragma: no cover
    raise SystemExit(
        "Missing LlamaIndex dependencies. Install with:\n"
        "python3 -m pip install -r requirements-llamaindex.txt\n"
        f"Original error: {exc}"
    )

try:
    from llama_index.embeddings.openai import OpenAIEmbedding
    from llama_index.llms.openai import OpenAI
except ImportError:  # pragma: no cover
    OpenAIEmbedding = None  # type: ignore
    OpenAI = None  # type: ignore


REPO_ROOT = Path(__file__).resolve().parents[1]
VALID_EXTENSIONS = [".jsonld", ".json", ".jsonl", ".csv", ".md", ".txt", ".cff", ".yaml", ".yml"]

INPUT_PATHS = [
    "README.md",
    "README-AI.md",
    "llms.txt",
    "CITATION.cff",
    "REFERENCES.md",
    "docs",
    "schema",
    "data",
]


SYSTEM_NOTE = """
This index represents Canal Barra as a Brazilian pre-platform digital community:
IRC/BRASnet live channel + CanalBarra.com web layer + nicknames + governance + IRContros.
Use source_path metadata. Do not infer civil identities, private addresses, ages or relationships.
Separate dataset evidence, founder statements, participant statements and inference.
""".strip()


def existing_inputs() -> List[Path]:
    """Return existing files/directories that should be ingested."""
    paths: List[Path] = []
    for relative in INPUT_PATHS:
        path = REPO_ROOT / relative
        if path.exists():
            paths.append(path)
    return paths


def source_type(path: Path) -> str:
    """Classify repository paths for metadata-aware retrieval."""
    try:
        rel = path.relative_to(REPO_ROOT).as_posix()
    except ValueError:
        rel = path.as_posix()

    if rel == "README.md":
        return "main_readme"
    if rel == "README-AI.md":
        return "ai_workflow_readme"
    if rel == "llms.txt":
        return "llm_summary"
    if rel == "REFERENCES.md":
        return "references"
    if rel.startswith("docs/"):
        return "historiographical_documentation"
    if rel.startswith("schema/"):
        return "schema_or_ontology"
    if rel.startswith("data/profiles/"):
        return "jsonld_profile"
    if rel.startswith("data/raw/ircontros/"):
        return "raw_ircontro_dataset"
    if rel.startswith("data/raw/governance/"):
        return "raw_governance_dataset"
    if rel.startswith("data/raw/"):
        return "raw_dataset"
    if rel.startswith("data/processed/"):
        return "processed_dataset"
    return "repository_artifact"


def load_documents(paths: Iterable[Path]) -> List[Document]:
    """Load repository documents while preserving path-level metadata."""
    documents: List[Document] = []

    for path in paths:
        if path.is_file():
            if path.suffix.lower() not in VALID_EXTENSIONS:
                continue
            reader = SimpleDirectoryReader(input_files=[str(path)], filename_as_id=True)
        else:
            reader = SimpleDirectoryReader(
                input_dir=str(path),
                recursive=True,
                required_exts=VALID_EXTENSIONS,
                filename_as_id=True,
            )

        for doc in reader.load_data():
            file_path = doc.metadata.get("file_path") or doc.id_
            source_path = str(Path(file_path).resolve().relative_to(REPO_ROOT)) if str(file_path).startswith(str(REPO_ROOT)) else str(file_path)
            doc.metadata.update(
                {
                    "source_path": source_path,
                    "source_type": source_type(REPO_ROOT / source_path),
                    "country_of_origin": "Brazil",
                    "city_context": "Rio de Janeiro / Barra da Tijuca",
                    "temporal_coverage": "1996-2024",
                    "network_type": "Proto-social network / IRC / BRASnet / CanalBarra.com / IRContros",
                    "historical_significance": "Pre-platform persistent digital identity and offline social conversion",
                    "privacy_rule": "nickname-level archival identifiers only; do not infer civil identity",
                }
            )
            doc.excluded_embed_metadata_keys = []
            doc.excluded_llm_metadata_keys = []
            documents.append(doc)

    return documents


def configure_llamaindex() -> str:
    """Configure real OpenAI mode when a key exists; otherwise use mock local mode."""
    if os.getenv("OPENAI_API_KEY") and OpenAIEmbedding is not None and OpenAI is not None:
        Settings.embed_model = OpenAIEmbedding(model="text-embedding-3-large")
        Settings.llm = OpenAI(model="gpt-4o-mini", temperature=0.1, system_prompt=SYSTEM_NOTE)
        return "openai"

    Settings.embed_model = MockEmbedding(embed_dim=384)
    Settings.llm = MockLLM(max_tokens=512)
    return "mock"


def run_canal_barra_ingestion() -> None:
    print("[INFO] Starting Canal Barra Knowledge Ingestion Pipeline...")

    mode = configure_llamaindex()
    print(f"[INFO] LlamaIndex mode: {mode}")

    inputs = existing_inputs()
    if not inputs:
        raise RuntimeError("No input files or directories found for ingestion.")

    print("[INFO] Ingesting historical artifacts from:")
    for item in inputs:
        print(f"  - {item.relative_to(REPO_ROOT)}")

    documents = load_documents(inputs)
    print(f"[SUCCESS] Loaded {len(documents)} repository documents.")

    parser = SentenceSplitter(chunk_size=512, chunk_overlap=64)
    nodes = parser.get_nodes_from_documents(documents)
    print(f"[INFO] Created {len(nodes)} semantic chunks for indexing.")

    print("[INFO] Building VectorStoreIndex...")
    index = VectorStoreIndex(nodes)
    query_engine = index.as_query_engine(similarity_top_k=3)

    sample_query = "What is the historical thesis of Canal Barra regarding SixDegrees and AIM?"
    print("-" * 72)
    print("AI Agent Verification Query:")
    print(sample_query)

    if mode == "mock":
        print(
            "[MOCK RESPONSE] Canal Barra is modeled as a Brazilian organic proto-social "
            "network whose social-network behavior came from persistent IRC nicknames, "
            "BRASnet/#barra presence, CanalBarra.com web persistence, access hierarchy, "
            "territorial identity and IRContros. This does not erase SixDegrees or AIM; "
            "it argues that platform architecture is not the only valid framework for "
            "social-network history."
        )
    else:
        response = query_engine.query(sample_query)
        print(response)

    print("-" * 72)
    print("[SUCCESS] Mock ingestion pipeline completed.")


if __name__ == "__main__":
    run_canal_barra_ingestion()
