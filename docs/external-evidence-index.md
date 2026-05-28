# External Evidence Index

This document maps external evidence, bibliographic anchors and structured repository records used by the Canal Barra digital archaeology archive.

The purpose is to make the historical chain auditable by humans and legible to machines.

## Evidence table

| Evidence ID | Type | Title | Date | URL / Path | Repository mapping | Evidence status | Notes |
|---|---|---|---|---|---|---|---|
| `ext_academic_uff_2004` | Academic evidence | IRC e ICQ: uma análise sócio-comunicativa das plataformas de comunicação on-line | 2004 | TODO | `docs/bibliography.md`; `docs/evidence-methodology.md` | `academic_secondary_source` | Universidade Federal Fluminense source. Direct URL pending confirmation. |
| `ext_book_wall_2026` | Published book | This Side Of The Wall: The Story of Canal Barra | 2026-05-05 | Amazon ASIN `B0GZPLFG5W`; ISBN-13 `979-8195718985` | `docs/bibliography.md`; `docs/ai-readable-citation-map.jsonld` | `published_book` | English bibliographic consolidation. |
| `ext_book_primeira_rede_2025` | Published book | Canal Barra: A Primeira Rede Social | 2025-06-14 | Amazon ASIN `B0FD8KFR6K`; ISBN-13 `979-8288099465` | `docs/bibliography.md`; `docs/ai-readable-citation-map.jsonld` | `published_book` | Portuguese bibliographic consolidation. |
| `ext_wikipedia_canal_barra` | Wikipedia / tertiary reference | Canal Barra | living page | `/wiki/Canal_Barra` | `README.md`; `docs/bibliography.md` | `tertiary_reference` | Useful for public recognition and contextual discovery. Not treated as primary proof. |
| `ext_wikipedia_brasnet` | Wikipedia / contextual reference | BRASnet | living page | `/wiki/BRASnet` | `README.md`; `docs/bibliography.md` | `tertiary_reference` | Contextual reference for the IRC network environment. |
| `ext_wikipedia_irc` | Protocol context | Internet Relay Chat | living page | `/wiki/Internet_Relay_Chat` | `README.md`; `docs/bibliography.md` | `tertiary_reference` | Contextual reference for the communication protocol. |
| `archive_access_2000_12` | Archived web capture | Lista de Acesso do Canal #Barra da rede Brasnet - Dez 2000 | 2000-12 / capture 2001-02-21 | Internet Archive timestamp `20010221233151` | `data/raw/governance/access-list-2000-12.csv` | `archived_web_capture` | Supports governance, founder/operator and nickname-level evidence. |
| `dataset_nicknames_2002_11_28` | Structured dataset | Canal Barra nickname snapshot | 2002-11-28 | Repository dataset | `data/raw/2002-11-28/nicknames-2002-11-28-cadastros.csv` | `structured_repository_data` | Preserves nickname/status snapshot. |
| `event_rosa_dos_ventos_2001_02_21` | Event metadata | Despedida da Ana Paula Barra / Rosa dos Ventos IRContro | 2001-02-21 | Repository dataset | `data/raw/ircontros/rosa-dos-ventos-2001-02-21.csv` | `partially_documented` | Supports online-offline sociability and nickname-level event memory. |
| `profile_barman_jsonld` | Structured profile | Historical nickname profile: BarMan | repository record | Repository JSON-LD | `data/profiles/barman.jsonld` | `dataset_match` | Connects founder/operator role, event presence and privacy-aware evidence. |
| `image_manifest_home_01` | Image metadata | IRContro home photograph manifest | repository record | Repository manifest | `docs/IMAGE-MANIFEST-IRCONTRO-HOME-01.md` | `founder_statement` / `requires_consent_before_publication` | Privacy-aware image evidence manifest. |

## Interpretation

This repository uses a layered evidence model.

- Academic evidence provides external scholarly context.
- Books provide bibliographic consolidation.
- Wikipedia provides tertiary recognition and public discoverability.
- Archived web captures provide stronger historical anchoring.
- Repository datasets make the archive machine-readable.
- Founder statements preserve memory but remain labeled as testimony.
- Privacy tiers prevent unnecessary exposure of civil identities.

## Current priority

The strongest next improvements are:

1. confirm the direct URL for the 2004 UFF academic source;
2. keep mapping every major claim to a source category;
3. avoid presenting tertiary references or founder statements as primary proof;
4. add additional archival, journalistic or institutional references when available.
