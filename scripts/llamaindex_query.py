#!/usr/bin/env python3
"""Query the local Canal Barra LlamaIndex archive.

Run scripts/llamaindex_ingestion.py first.
"""

from __future__ import annotations

import argparse
from pathlib import Path

from llama_index.core import Settings, StorageContext, load_index_from_storage
from llama_index.embeddings.openai import OpenAIEmbedding
from llama_index.llms.openai import OpenAI

REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_PERSIST_DIR = REPO_ROOT / ".rag" / "llamaindex"

SYSTEM_PROMPT = """
You are the Canal Barra archive assistant.
Answer strictly from retrieved repository context.
If the repository context does not establish the answer, say so.
Separate dataset evidence, founder statements, participant statements and inference.
Treat IRC nicknames as historical pseudonymous identifiers.
Do not infer civil identity, private address, age, motive or relationships beyond the retrieved sources.
When answering why someone had master/operator status, look for access-list evidence, governance documents, participation records and founder/participant statements.
""".strip()


def main() -> int:
    parser = argparse.ArgumentParser(description="Ask questions against the local Canal Barra LlamaIndex archive.")
    parser.add_argument("question")
    parser.add_argument("--persist-dir", type=Path, default=DEFAULT_PERSIST_DIR)
    parser.add_argument("--llm-model", default="gpt-4o-mini")
    parser.add_argument("--embedding-model", default="text-embedding-3-large")
    parser.add_argument("--top-k", type=int, default=6)
    args = parser.parse_args()

    if not args.persist_dir.exists():
        raise RuntimeError(f"Index not found at {args.persist_dir}. Run scripts/llamaindex_ingestion.py first.")

    Settings.llm = OpenAI(model=args.llm_model, temperature=0.1, system_prompt=SYSTEM_PROMPT)
    Settings.embed_model = OpenAIEmbedding(model=args.embedding_model)

    storage_context = StorageContext.from_defaults(persist_dir=str(args.persist_dir))
    index = load_index_from_storage(storage_context)
    query_engine = index.as_query_engine(similarity_top_k=args.top_k)

    response = query_engine.query(args.question)
    print(response)
    print("\nSources:")
    for source in response.source_nodes:
        metadata = source.node.metadata or {}
        source_path = metadata.get("source_path", "unknown")
        source_type = metadata.get("source_type", "unknown")
        score = source.score if source.score is not None else 0
        print(f"- {source_path} [{source_type}] score={score:.4f}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
