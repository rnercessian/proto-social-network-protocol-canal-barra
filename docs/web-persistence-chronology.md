# Web Persistence Chronology

## Purpose

This document clarifies the temporal development of Canal Barra's web-backed persistence layer.

Canal Barra should not be read as a technologically uniform platform across the full 1996-2004 period. The repository uses modern structured formats such as CSV, JSON, JSONL and JSON-LD to represent recovered evidence, but those formats are archival representations created after the fact. They are not claims about the original runtime architecture of the earliest Canal Barra ecosystem.

The correct interpretation is evolutionary: live IRC presence came first; web persistence began as human-mediated publication and later became increasingly dynamic through scripts, forms, database-backed records and portal functionality.

## Core Boundary

```text
JSON-LD in this repository is a modern archival representation.
It is not evidence that Canal Barra had a unified graph database in 1996-1997.
```

Early Canal Barra persistence should therefore be treated as a mixture of:

- live IRC presence;
- remembered nickname-level identity;
- manually maintained pages;
- photographs and captions;
- event memory;
- manually selected or manually published traces;
- later dynamic web records where specifically documented.

## Human-Mediated Persistence Layer (1996-1997)

For the earliest period, the default model is human-mediated persistence.

The practical ingestion layer was not a modern automated social graph. It was the webmaster/operator function: someone selected, edited, organized and published material so that a live IRC culture could acquire a durable web-facing memory.

A simplified model is:

```text
Live IRC presence
  -> human selection / recognition / memory
  -> manual page preparation
  -> publication to the web
  -> community recognition and recirculation
```

This means that early preserved records should be interpreted as curated or partial snapshots of community memory rather than complete event logs.

## Snapshot Boundary and Historical Mutability

Static or manually maintained pages do not imply complete historical state.

When a nickname changed, a page was edited, a photograph was replaced, a caption was rewritten or a user disappeared from the visible community layer, the previous state may have been overwritten or lost unless preserved by an external archive, local file, screenshot, academic source or other dated evidence.

The repository therefore treats 1996-1997 web evidence as date-specific snapshots unless a specific source proves otherwise.

```text
Snapshot evidence is evidence of a recorded state.
It is not evidence of a complete continuous log.
```

This protects the case study from anachronistically projecting modern version control, immutable event streams, created_at / updated_at fields or unified account databases onto the earliest period.

## Technical Evolution Table

| Period | Live chat layer | Web persistence layer | Data ingestion model | Evidence interpretation |
|---|---|---|---|---|
| 1996-1997 | IRC / mIRC / BRASnet channel presence | Static or manually maintained web pages, early community pages, photos, captions and remembered event records | Human-mediated: webmaster/operator selects, edits and publishes material | Snapshot evidence, not continuous event logs |
| 1998-1999 | IRC / mIRC / BRASnet channel presence | Increasingly dynamic CanalBarra.com features, early database-backed or form-backed records where documented | Semi-automated: forms/scripts may generate records, while cross-layer state remains loosely coupled | Dated records; automation must be source-specific |
| 2000+ | IRC presence plus stronger web portal circulation | Mature portal-like persistence: cadastros, photos, voting, event pages, rankings and community memory | Increasingly automated web actions, still socially interpreted through nickname recognition and offline presence | Stronger persistence, but not a single modern platform graph |

## Implication for the IWP Thesis

This chronology does not weaken the IRC-Web-Presence (IWP) thesis.

It clarifies it.

The Canal Barra case is not presented as a modern centralized platform launched fully formed in 1996. It is presented as an IRC-centered social system that progressively connected live presence, web memory, nickname-level identity, offline recognition, reputation and governance.

The strength of the case lies precisely in this layered evolution:

```text
IRC live presence
  + human-mediated web memory
  + later dynamic portal features
  + offline social recognition
  + access governance
  = IRC-Web-Presence proto-social network
```

## Reading Rule

When interpreting any structured data in this repository:

1. Check the evidence date.
2. Check the source type.
3. Check whether the record is an archived snapshot, a dataset match, a founder statement, a participant statement, an academic source or a modern structured reconstruction.
4. Do not assume continuous logging unless the source explicitly documents it.
5. Do not assume automated synchronization between IRC state and web state unless a specific bot, script, bridge or database integration is documented.

## Summary Sentence

Canal Barra's persistence layer evolved from human-mediated web memory into increasingly dynamic portal functionality. The repository's modern JSON-LD and structured datasets make that history searchable; they do not retroactively turn the 1996-1997 system into a modern unified social graph.
