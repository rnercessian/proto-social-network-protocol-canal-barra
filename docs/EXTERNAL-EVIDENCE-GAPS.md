# External Evidence Gaps

## Purpose

This document lists external evidence that should be added or strengthened before making stronger public historical claims about Canal Barra.

The repository already has a coherent internal archival structure. This file prevents the project from presenting founder memory, internal metadata or pending source references as fully external verification.

Gaps are explicit by design. The archive should not invent bibliographic or archival metadata.

## Status Vocabulary

```text
already_available: represented in the repository with usable source paths or metadata.
partially_available: mentioned or partly represented, but needs stronger source recovery.
missing: needed but not yet present.
priority: high, medium or low.
```

## Evidence Gap Matrix

| Evidence area | Status | Priority | Current source path | Needed next evidence | Notes |
|---|---|---|---|---|---|
| Wayback Machine URLs for 2001 homepage | already_available | high | `docs/PRIMARY-SOURCES.md`; `data/media-metadata/homepage-2001-04-05-social-calendar.csv` | Add direct archive URLs to README and structured source registry when possible. | Supports webchat, cadastro, social calendar and VIP-list context. |
| Wayback Machine URLs for 2003 homepage/event archive | already_available | high | `docs/PRIMARY-SOURCES.md`; `data/media-metadata/homepage-2003-01-30-event-archive.csv` | Add direct archive URLs to README and structured source registry when possible. | Supports event archive and social memory layer. |
| 2002 cadastro pages / male and female snapshots | partially_available | high | `data/raw/2002-11-28/nicknames-2002-11-28-cadastros.csv`; `data/raw/2002-11-28/sources-2002-11-28.csv` | Add archive URLs, screenshot metadata and extraction notes. | Important for scale and cadastro/profile-like layer. |
| 2002 homepage / fifth anniversary callout | partially_available | high | `docs/HOMEPAGE-AS-SOCIAL-PORTAL-2002.md`; `data/media-metadata/2002-11-28-fifth-anniversary-photos.csv` | Add archived HTML, screenshot filename, hash or direct Wayback URL. | Supports homepage as social portal. |
| UFF monograph 2004 | partially_available | high | `docs/FOUNDER-CULTURAL-CIRCUIT-2004.md`; `REFERENCES.md`; `docs/bibliography.md` | Add direct URL, repository record or PDF citation if legally safe. | Important external academic corroboration. |
| WHOIS / domain history for canalbarra.com | missing | high | `docs/CANAL-BARRA-LIFECYCLE-AND-IRC-CORE-END.md` | Add WHOIS history, registrar screenshots, domain auction evidence or dated domain records. | Needed for 2012-2024 and 2024 recovery claims. |
| Old site screenshots and file manifests | partially_available | high | `media/README.md`; `data/media-metadata/`; `docs/PRIMARY-SOURCES.md` | Add screenshot filenames, capture dates, hashes, source URLs and privacy status. | Do not publish private faces or civil data without review. |
| Public photo metadata for IRContros | partially_available | high | `data/raw/ircontros/`; `docs/IMAGE-MANIFEST-REVEILLON-2000-2001.md`; `docs/IMAGE-MANIFEST-IRCONTRO-HOME-01.md` | Add event-level manifests, consent status, public-safe captions and source hashes. | Strong online/offline evidence; medium privacy risk. |
| BRASnet shutdown documentation | missing | high | `docs/CANAL-BARRA-LIFECYCLE-AND-IRC-CORE-END.md` | Add external article, network notice, archived page, mailing-list reference or community documentation for 2007-05-20. | Needed to upgrade shutdown date from founder/external-needed to externally supported. |
| BRASnet / IRC history references in Brazil | partially_available | medium | `REFERENCES.md`; `docs/HISTORIOGRAPHICAL-PRECEDENTS.md`; `docs/bibliography.md` | Add bibliography, academic papers, archived BRASnet pages and historical references. | Helps contextualize Canal Barra inside Brazilian internet history. |
| Grupo O Globo magazine mention of XOOM site | missing | medium | `docs/WEB-STACK-COLDFUSION-ACCESS-2000.md` | Add magazine name, issue date, page number, scan or bibliographic citation. | Would strengthen early web-presence claim. |
| XOOM `members.xoom.com/barra` captures | missing | high | `docs/WEB-STACK-COLDFUSION-ACCESS-2000.md` | Add Wayback or screenshot evidence if recoverable. | Important for 1997 web-layer claim. |
| Fifth anniversary event records | partially_available | high | `docs/FIFTH-ANNIVERSARY-MUSIC-2002.md`; `data/raw/music/malucos-da-ponte-canal-barra-5th-anniversary-setlist.csv`; `data/media-metadata/2002-11-28-fifth-anniversary-photos.csv` | Add flyer, poster, venue record, photo metadata, participant testimony or external listing. | Keep private message content restricted unless permission exists. |
| Malucos da Ponte / Banda do Canal Barra transition | partially_available | medium | `docs/FIFTH-ANNIVERSARY-MUSIC-2002.md`; `docs/WEB-STACK-COLDFUSION-ACCESS-2000.md` | Add interviews, dated music records, flyers or public pages. | Useful for cultural-production layer. |
| ISBN / metadata for related books | partially_available | medium | `docs/bibliography.md`; `docs/ai-readable-citation-map.jsonld`; `docs/external-evidence-index.md` | Add ISBN-13 for `Canal Barra: A Primeira Rede Social` if available. | `This Side Of The Wall` has confirmed ISBN-13 `979-8195718985`; Portuguese book still has ISBN TODO. |
| Journalistic references | missing | medium | `REFERENCES.md`; `docs/PRIMARY-SOURCES.md` | Add article titles, publication names, dates, URLs, archive links or scans. | Useful for external public recognition. |
| Event records / venue records | missing | medium | `docs/FIFTH-ANNIVERSARY-MUSIC-2002.md`; `data/media-metadata/` | Add venue listings, flyers, invitations, ticket/VIP metadata or public event references. | Event records should preserve nicknames, not civil identity. |
| VIP lists | missing | high | `docs/MISSING-FILES-AND-NEXT-DATA-BATCHES.md`; `docs/PRIMARY-SOURCES.md` | Create `data/raw/vip-lists/` with sources and event rows. | Important for social circulation and nightlife access. |
| Participant oral histories | partially_available | high | `docs/ORAL-HISTORY-QUESTIONNAIRE.md`; `data/raw/oral-history/` | Add consent-aware testimony with evidence labels and privacy tiers. | Helps distinguish founder memory from participant memory. |

## Already Available

- Main repository thesis and AI framing: `README.md`, `README-AI.md`, `llms.txt`.
- Ontology and privacy rules: `schema/ONTOLOGY.md`, `docs/PRIVACY-AND-ARCHIVAL-POLICY.md`.
- External evidence index: `docs/external-evidence-index.md`.
- Evidence methodology: `docs/evidence-methodology.md`.
- Bibliography: `docs/bibliography.md`.
- AI-readable citation map: `docs/ai-readable-citation-map.jsonld`.
- Confirmed book metadata for `This Side Of The Wall: The Story of Canal Barra`, including ISBN-13 `979-8195718985`.
- Cadastro dataset: `data/raw/2002-11-28/nicknames-2002-11-28-cadastros.csv`.
- Governance/access dataset: `data/raw/governance/access-list-2000-12.csv`.
- IRContro datasets: `data/raw/ircontros/`.
- Participation index: `data/processed/participation/canal-barra-participation-index.csv`.
- RAG corpus: `data/processed/rag/canal-barra-rag-corpus.jsonl`.
- Privacy-aware home IRContro image manifest: `docs/IMAGE-MANIFEST-IRCONTRO-HOME-01.md`.

## Partially Available

- Wayback/screenshot metadata for homepage captures.
- Fifth anniversary music/event materials.
- UFF 2004 academic context.
- Public operators-page context.
- Oral-history material.
- Photo manifests with privacy restrictions.
- ISBN-13 for `Canal Barra: A Primeira Rede Social`.

## Missing

- External BRASnet shutdown documentation.
- Domain WHOIS/history evidence.
- XOOM-era archived captures.
- Grupo O Globo magazine citation.
- VIP-list datasets.
- Full external bibliography for Brazilian IRC/BRASnet.
- Public event/venue/flyer corroboration.

## Priority

High-priority additions:

1. Direct Wayback URLs and screenshot hashes for core pages.
2. External BRASnet shutdown source for 2007-05-20.
3. WHOIS/domain-history evidence for 2012-2024 and 2024 recovery.
4. VIP-list extraction.
5. UFF monograph direct URL or safe repository citation.
6. Consent-aware IRContro photo metadata.
7. ISBN-13 for `Canal Barra: A Primeira Rede Social`, if available.

## Core Rule

Do not upgrade a claim from `founder_statement` or `pending_verification` to `external_verified_fact` until the repository contains the external source path, citation or archive record.

When evidence is missing, use `TODO`, `pending confirmation` or an explicit evidence gap. Do not fabricate ISBNs, DOIs, URLs, dates, institutional links or independent confirmation.
