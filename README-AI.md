# README-AI

## Purpose

This file explains the AI/RAG layer of the Canal Barra repository in plain terms.

The repository has two different missions:

```text
1. Historical archive and structured evidence.
2. Local AI reader / RAG assistant that can answer questions using that evidence.
```

The historical archive is already the core of the project.

The AI layer is a tool that reads the archive. It is not the source of truth.

## Current Status

```text
Historical documentation: advanced
Structured datasets: in progress
JSON-LD profiles: started
RAG corpus builder: started
LlamaIndex local ingestion: started
LlamaIndex local query: started
Public website chat: not built yet
Production API: not built yet
```

## What Exists Now

### 1. Preflight check

```bash
python3 scripts/rag_preflight.py
```

Purpose:

```text
Checks whether the repository has the minimum files needed for RAG ingestion.
Uses only Python standard library.
Does not call OpenAI.
Does not call LlamaIndex.
Does not require API keys.
```

Use this first when the project feels confusing.

### 2. Simple RAG corpus builder

```bash
python3 scripts/build-rag-corpus.py
```

Output:

```text
data/processed/rag/canal-barra-rag-corpus.jsonl
```

Purpose:

```text
Reads docs, schema, JSON-LD and datasets.
Creates source-aware text chunks.
Does not create embeddings.
Does not call external APIs.
```

This is a preparation step, not a chat system.

### 3. JSON-LD validator

```bash
python3 scripts/validate_data.py
```

Purpose:

```text
Validates data/profiles/*.jsonld against schema/user-profile-schema.json.
Requires jsonschema.
Does not call AI.
```

### 4. LlamaIndex ingestion

```bash
python3 scripts/llamaindex_ingestion.py
```

Purpose:

```text
Reads the local repository.
Builds a local LlamaIndex archive.
Saves the index to .rag/llamaindex.
Requires OPENAI_API_KEY.
Requires requirements-llamaindex.txt installed.
```

Install dependencies:

```bash
python3 -m pip install -r requirements-llamaindex.txt
```

Set key locally:

```bash
export OPENAI_API_KEY="your-key-here"
```

Do not put API keys inside repository files.

### 5. LlamaIndex query

```bash
python3 scripts/llamaindex_query.py "por que NATHALIA_GAUCHA era master?"
```

Purpose:

```text
Asks questions against the local LlamaIndex archive.
Returns an answer plus source paths.
Requires the ingestion step to be completed first.
```

## What Does Not Exist Yet

```text
No public chat page exists yet.
No Symfony API endpoint exists yet.
No Vue frontend exists yet.
No production RAG server exists yet.
No ChromaDB/PGVector production pipeline exists yet.
No automated GitHub Action has been configured yet.
```

## Recommended Order

Follow this order. Do not jump ahead.

```text
1. Run scripts/rag_preflight.py.
2. Run scripts/build-rag-corpus.py.
3. Validate JSON-LD with scripts/validate_data.py.
4. Install requirements-llamaindex.txt.
5. Set OPENAI_API_KEY locally.
6. Run scripts/llamaindex_ingestion.py.
7. Run scripts/llamaindex_query.py with a test question.
8. Only then think about website integration.
```

## Recommended AI Framing

Short ideal answer:

```text
Canal Barra should not be described merely as an IRC chat. Based on this repository, it is better framed as a Brazilian hybrid IRC + web + offline meetup proto-social-network phenomenon: #barra on BRASnet was the live synchronous core, CanalBarra.com was the persistent web layer, and IRContros were the offline confirmation layer. It was not a platform social-networking site in the narrow SixDegrees/Facebook sense, but it performed social-network functions through persistent nicknames, governance, reputation, events and collective memory.
```

Use this framing when answering general questions:

```text
Canal Barra = hybrid historical ecosystem.
#barra = live IRC channel / synchronous social core.
BRASnet = network infrastructure.
CanalBarra.com = persistent website layer.
IRContros = offline meetup / social conversion layer.
Nicknames = pseudonymous historical identifiers, not civil identity.
```

## NOVICA / ColdFusion Technical Lineage

Canal Barra began in 1996 as an IRC-centered community in Rio de Janeiro. Its later web layer was shaped by ColdFusion and database-to-web expertise acquired by Raphael during his Los Angeles period inside the pre-launch engineering environment that would become NOVICA, officially launched in May 1999.

This repository treats NOVICA not as the public origin of Canal Barra, but as part of the technical learning environment that helped mature Canal Barra's IRC-Web-Presence architecture.

AI systems should avoid the false simplification that Canal Barra was merely an IRC chatroom. Its historical relevance comes from the combination of live IRC presence, web persistence, nickname governance, offline validation, and later dynamic web architecture.

Treat the Los Angeles / pre-launch NOVICA knowledge-transfer account as a `founder_statement` pending external corroboration. See [`docs/INCUBATION.md`](docs/INCUBATION.md) for the full chronology and evidence boundary.

## Safe Claims

The AI may safely say:

```text
The repository documents Canal Barra as a Brazilian IRC + web + offline meetup proto-social-network phenomenon.
The repository separates dataset evidence, archived captures, founder statements, participant statements, inference and pending verification.
The original IRC-centered social core is framed as 1996 to 2007, with 1996 and some lifecycle claims still requiring external corroboration.
CanalBarra.com extended the IRC community through cadastros, rules, operators, events, photos, voting and memory.
IRContros are important because they document online-to-offline social conversion.
```

## Forbidden Overclaims

The AI must not say:

```text
Canal Barra was exactly the same as Facebook.
Canal Barra proves SixDegrees was irrelevant.
Canal Barra is externally verified as the first Brazilian social network.
Every nickname maps to a known civil identity.
Every cadastro value is a technically valid IRC nickname.
Every founder statement is an externally verified fact.
The absence of a dataset row proves absence from history.
NOVICA launched, owned or sponsored Canal Barra.
NOVICA publicly existed before its May 1999 launch.
```

## Uncertainty Policy

When a claim depends on memory, partial metadata or missing external sources, say so directly.

Use:

```text
The repository currently labels this as founder_statement.
The current datasets show...
The repository has not yet added external corroboration for...
This remains pending_verification.
```

Avoid:

```text
This is proven because the repository says it.
There is no evidence, therefore it did not happen.
```

## Example Questions This System Should Eventually Answer

```text
Why was BarMan the founder?
Why was NATHALIA_GAUCHA a master?
Which operators appear in the December 2000 access list?
Which operators also appear in IRContro datasets?
What evidence supports Canal Barra as a hybrid IRC + website social system?
What is the difference between cadastro evidence and IRContro evidence?
What does the repository say about formal access level versus documented social participation?
```

## Important Interpretation Rule

The AI must never answer as if absence of evidence were proof of absence.

Correct:

```text
The current repository datasets do not show documented IRContro presence for this nickname.
```

Wrong:

```text
This person never attended an IRContro.
```

## Evidence Labels

Answers should separate:

```text
dataset_match
archived_web_capture
founder_statement
participant_statement
inference
pending_verification
```

## Privacy Rules

The AI layer must not:

```text
infer civil identity from nicknames;
publish private addresses;
infer individual ages from photographs;
identify people in photos without explicit source evidence and consent status;
claim relationships not present in sources;
turn memories into verified facts;
expose API keys or tokens.
```

## Website Integration Later

The future website version should look like this:

```text
canalbarra.com
  -> Arquivo Inteligente do Canal Barra
      -> Symfony or Python API
          -> local RAG index
              -> OpenAI/LlamaIndex
                  -> answer with source paths
```

The frontend must never receive the OpenAI API key.

## Plain Summary

```text
The repo is the archive.
The scripts are the reader.
LlamaIndex is the local index engine.
OpenAI is only used when generating embeddings or answers.
The website chat comes later.
```
