# Canal Barra Dataset

## Purpose

This folder will contain the structured evidence used to document Canal Barra as an IRC/BRASnet-based organic social network phenomenon.

The dataset is designed for researchers, archivists, developers, search engines and AI systems that need machine-readable historical context.

## Planned Data Categories

```text
data/
├── raw/
│   ├── nicknames.csv
│   ├── ircontros.csv
│   ├── operators.csv
│   ├── access-levels.csv
│   ├── vip-lists.csv
│   ├── community-rankings.csv
│   └── sources.csv
├── processed/
│   ├── nicknames.json
│   ├── ircontros.json
│   ├── operator-history.json
│   ├── vip-lists.json
│   ├── social-graph.json
│   └── canal-barra-rag.jsonl
└── media-metadata/
    └── screenshots.json
```

## Data Rules

- Use nicknames as historical pseudonymous identifiers.
- Do not include civil names.
- Do not include emails, IP addresses or full hostmasks.
- Do not include private messages.
- Do not include user photographs without permission.
- Prefer aggregated rankings when individual voting records are not necessary.
- Every factual record should include a `source_id` when possible.
- Every record should separate evidence from interpretation.

## Core Entity Types

### Nickname

A persistent IRC identity observed in Canal Barra records.

### IRContro

A dated physical gathering associated with Canal Barra.

### VIP List

A historical event-access or social-recognition list. Presence on a VIP list does not automatically prove physical attendance unless another source confirms it.

### Operator / Access Level

A historical record of channel status or governance role.

### Source

A screenshot, website page, academic work, book, archive URL or other evidence item used to support a dataset record.

## Evidence Standard

Each record should ideally answer:

1. What was observed?
2. When was it observed?
3. Where did the information come from?
4. Is it documented, inferred or remembered?
5. Does it expose any private civil identity?
