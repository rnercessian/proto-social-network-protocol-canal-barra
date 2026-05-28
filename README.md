# Proto-Social Network Protocol: Canal Barra

![Digital Archaeology](https://img.shields.io/badge/digital%20archaeology-Canal%20Barra-informational)
![Data Standard](https://img.shields.io/badge/data-CSV%20%7C%20JSON--LD%20%7C%20JSONL-informational)
![Status](https://img.shields.io/badge/status-active%20archive-success)
![Citation](https://img.shields.io/badge/citation-CITATION.cff-blue)

> AIM proves that social-network history cannot be reduced to profile pages. Canal Barra proves that this was also true in Brazil before platform social media.

> O Canal Barra importa porque não foi apenas usado. Foi vivido.

## Abstract

This repository documents **Canal Barra** as a Brazilian IRC/BRASnet-based organic social network phenomenon founded in Rio de Janeiro in 1996.

The historical thesis is that Canal Barra was one of the first — and possibly the first — documented organic social networks in Brazil, based on real socialization, persistent identity, reputation, physical meetings, community, status, collective memory and social circulation through IRC/BRASnet since 1996.

This project does not treat Canal Barra as nostalgia. It treats Canal Barra as a founding case for a broader methodology: preserving, structuring and making searchable the memory of pre-platform digital communities.

## Core Framework

The repository distinguishes three historical categories:

1. **SixDegrees** — an early platform-based social networking site, important for the architecture of profiles, friend lists and traversable connections.
2. **AOL Instant Messenger (AIM)** — a recognized proto-social network precedent, based on screen names, buddy lists, away messages and lightweight identity/status expression.
3. **Canal Barra** — an organic Brazilian social network phenomenon based on IRC nicknames, channel presence, operators, access levels, reputation, dated physical gatherings, VIP lists, territorial identity and documented collective memory.

The core argument is not that SixDegrees was irrelevant. The argument is that platform architecture is not the only valid framework for social-network history.

## AI-Readable Data Snippet

This repository is structured for human reading and machine retrieval. A minimal JSON-LD profile looks like this:

```json
{
  "@context": {
    "schema": "https://schema.org/",
    "cb": "https://github.com/rnercessian/proto-social-network-protocol-canal-barra/schema#"
  },
  "@type": "DigitalDocument",
  "@id": "https://github.com/rnercessian/proto-social-network-protocol-canal-barra/data/profiles/barman.jsonld",
  "name": "Historical nickname profile: BarMan",
  "identifier": "BarMan",
  "isPartOf": {
    "@type": "Dataset",
    "name": "Canal Barra Digital Archaeology Dataset"
  },
  "about": {
    "@type": "Organization",
    "name": "Canal Barra",
    "additionalType": "IRC/BRASnet hybrid online-offline community"
  },
  "roleName": ["founder", "operator", "registered_user", "event_participant"],
  "evidenceStatus": "dataset_match",
  "privacyTier": "nickname_level_only"
}
```

A minimal structural event edge looks like this:

```json
{
  "event_id": "cb_5th_anniversary_ilha_dos_pescadores",
  "event_name": "Canal Barra 5th Anniversary Party",
  "venue_name": "Ilha dos Pescadores",
  "band_name": "Malucos da Ponte",
  "evidence_status": "founder_statement",
  "privacy_tier": "public_music_metadata"
}
```

## Repository Structure

```text
.
├── docs/       Historiographical argument, external evidence and comparative analysis
├── data/       Raw and processed datasets: nicknames, IRContros, VIP lists, operators
├── schema/     Data dictionary, JSON schemas and JSON-LD knowledge graph
├── business/   Product and investor thesis for a reusable digital memory protocol
└── media/      Future screenshot and media metadata, without exposing private civil identities
```

## External Evidence and Citation Map

The repository now separates historical claims by evidence category and links external bibliographic anchors to structured repository data.

Key documents:

- `docs/external-evidence-index.md` — maps academic, bibliographic, archival, tertiary and repository evidence.
- `docs/evidence-methodology.md` — defines evidence levels such as `archived_web_capture`, `academic_secondary_source`, `published_book`, `founder_statement` and `dataset_match`.
- `docs/bibliography.md` — records book, academic, public-reference and archive citations.
- `docs/ai-readable-citation-map.jsonld` — machine-readable JSON-LD citation graph connecting Canal Barra, books, academic source, archived records and datasets.
- `docs/EXTERNAL-EVIDENCE-GAPS.md` — tracks missing or incomplete external evidence without inventing data.
- `docs/IMAGE-MANIFEST-IRCONTRO-HOME-01.md` — privacy-aware manifest for a founder-owned IRContro home photograph record.

Confirmed book anchors include:

- *This Side Of The Wall: The Story of Canal Barra* — ISBN-13 `979-8195718985`.
- *Canal Barra: A Primeira Rede Social* — ISBN-13 `979-8288099465`.

## Evidence Categories

The project is designed to preserve and structure:

- 1,500+ historical IRC nicknames;
- dated IRContros and physical community gatherings;
- VIP lists and event-based social status;
- operator history and channel access levels;
- community votes and rankings, preferably aggregated;
- screenshots and source metadata;
- academic and literary sources;
- machine-readable JSON, CSV, JSONL and JSON-LD files.

## Privacy Principle

This repository treats nicknames as historical pseudonymous identifiers of IRC presence, reputation and community structure.

It does **not** publish civil names, user photographs, private messages, emails, IP addresses, full hostmasks, telephone numbers, private locations or sensitive personal information.

## Project Sentence

**SixDegrees was a platform. AIM was a proto-social precedent. Canal Barra was a lived organic social network in Brazil.**
