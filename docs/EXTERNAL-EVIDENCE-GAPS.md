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
| Wayback Machine URLs for 2001 homepage | already_available | high | `data/processed/indexes/primary-sources.md`; `data/media-metadata/homepage-2001-04-05-social-calendar.csv` | Add direct archive URLs to README and structured source registry when possible. | Supports webchat, cadastro, social calendar and VIP-list context. |
| Wayback Machine URLs for 2003 homepage/event archive | already_available | high | `data/processed/indexes/primary-sources.md`; `data/media-metadata/homepage-2003-01-30-event-archive.csv` | Add direct archive URLs to README and structured source registry when possible. | Supports event archive and social memory layer. |
| 2002 cadastro pages / male and female snapshots | partially_available | high | `data/raw/2002-11-28/nicknames-2002-11-28-cadastros.csv`; `data/raw/2002-11-28/sources-2002-11-28.csv` | Add archive URLs, screenshot metadata and extraction notes. | Important for scale and cadastro/profile-like layer. |
| 2002 homepage / fifth anniversary callout | partially_available | high | `evidence/website/wayback-2002/HOMEPAGE-AS-SOCIAL-PORTAL-2002.md`; `data/media-metadata/2002-11-28-fifth-anniversary-photos.csv` | Add archived HTML, screenshot filename, hash or direct Wayback URL. | Supports homepage as social portal. |
| UFF dissertation 2004 direct URL/PDF | partially_available | high | `evidence/academic-sources/uff-2004-index.md`; `data/uff-2004/reported-nickname-occurrence-index.md`; `docs/bibliography.md` | Add direct URL, repository record or PDF citation if legally safe. | Important external academic corroboration. Do not treat reported nickname counts as verified until source text is available. |
| UFF dissertation exact pages/excerpts | missing | high | `evidence/academic-sources/uff-2004-index.md` | Add page numbers, excerpt IDs or safe quoted/extracted references for Canal Barra chat excerpts. | Needed before using specific nickname occurrence claims as strong academic evidence. |
| Verifiable UFF nickname occurrence extraction | missing | high | `data/uff-2004/reported-nickname-occurrence-index.md` | Add extracted text, script or reproducible occurrence table for nicknames such as VaNZaN and Biano. | Current counts are founder_provided_count_pending_repository_verification. |
| WHOIS / domain history for canalbarra.com | missing | high | `docs/CANAL-BARRA-LIFECYCLE-AND-IRC-CORE-END.md` | Add WHOIS history, registrar screenshots, domain auction evidence or dated domain records. | Needed for 2012-2024 and 2024 recovery claims. |
| Old site screenshots and file manifests | partially_available | high | `media/README.md`; `data/media-metadata/`; `data/processed/indexes/primary-sources.md` | Add screenshot filenames, capture dates, hashes, source URLs and privacy status. | Do not publish private faces or civil data without review. |
| SHA-256 hashes for Wayback HTML/source captures | missing | medium | `data/processed/indexes/primary-sources.md`; `data/media-metadata/` | Add SHA-256 hashes for downloaded HTML or screenshot metadata artifacts when legally safe to store. | Strengthens reproducibility and tamper-evidence for source extraction. |
| Public photo metadata for IRContros | partially_available | high | `data/raw/ircontros/`; `evidence/photos/ircontros/IMAGE-MANIFEST-REVEILLON-2000-2001.md`; `evidence/photos/ircontros/IMAGE-MANIFEST-IRCONTRO-PRIVATE-INDOOR-01.md` | Add event-level manifests, consent status, public-safe captions and source hashes. | Strong online/offline evidence; medium privacy risk. |
| BRASnet shutdown documentation | missing | high | `docs/CANAL-BARRA-LIFECYCLE-AND-IRC-CORE-END.md` | Add external article, network notice, archived page, mailing-list reference or community documentation for 2007-05-20. | Needed to upgrade shutdown date from founder/external-needed to externally supported. |
| BRASnet / IRC history references in Brazil | partially_available | medium | `REFERENCES.md`; `docs/HISTORIOGRAPHICAL-PRECEDENTS.md`; `docs/bibliography.md` | Add bibliography, academic papers, archived BRASnet pages and historical references. | Helps contextualize Canal Barra inside Brazilian internet history. |
| Grupo O Globo magazine mention of XOOM site | missing | medium | `evidence/website/WEB-STACK-COLDFUSION-ACCESS-2000.md` | Add magazine name, issue date, page number, scan or bibliographic citation. | Would strengthen early web-presence claim. |
| XOOM `members.xoom.com/barra` captures | missing | high | `evidence/website/WEB-STACK-COLDFUSION-ACCESS-2000.md` | Add Wayback or screenshot evidence if recoverable. | Important for 1997 web-layer claim. |
| Fifth anniversary event records | partially_available | high | `evidence/events/FIFTH-ANNIVERSARY-MUSIC-2002.md`; `data/raw/music/malucos-da-ponte-canal-barra-5th-anniversary-setlist.csv`; `data/media-metadata/2002-11-28-fifth-anniversary-photos.csv` | Add flyer, poster, venue record, photo metadata, participant testimony or external listing. | Keep private message content restricted unless permission exists. |
| Malucos da Ponte / Banda do Canal Barra transition | partially_available | medium | `evidence/events/FIFTH-ANNIVERSARY-MUSIC-2002.md`; `evidence/website/WEB-STACK-COLDFUSION-ACCESS-2000.md` | Add interviews, dated music records, flyers or public pages. | Useful for cultural-production layer. |
| ISBN / metadata for related books | already_available | medium | `docs/bibliography.md`; `data/processed/graph/ai-readable-citation-map.jsonld`; `data/processed/indexes/external-evidence-index.md` | Add future editions if published. | `This Side Of The Wall` has ISBN-13 `979-8195718985`; `Canal Barra: A Primeira Rede Social` has ISBN-13 `979-8288099465`. |
| Journalistic references | missing | medium | `REFERENCES.md`; `data/processed/indexes/primary-sources.md` | Add article titles, publication names, dates, URLs, archive links or scans. | Useful for external public recognition. |
| Event records / venue records | missing | medium | `evidence/events/FIFTH-ANNIVERSARY-MUSIC-2002.md`; `data/media-metadata/` | Add venue listings, flyers, invitations, ticket/VIP metadata or public event references. | Event records should preserve nicknames, not civil identity. |
| VIP lists | missing | high | `docs/MISSING-FILES-AND-NEXT-DATA-BATCHES.md`; `data/processed/indexes/primary-sources.md` | Create `data/raw/vip-lists/` with sources and event rows. | Important for social circulation and nightlife access. |
| Participant oral histories | partially_available | high | `docs/ORAL-HISTORY-QUESTIONNAIRE.md`; `data/raw/oral-history/` | Add consent-aware testimony with evidence labels and privacy tiers. | Helps distinguish founder memory from participant memory. |
| Automated JSON-LD profile validation | partially_available | high | `scripts/validate_profiles.py`; `schema/profile-schema.md`; `data/profiles/` | Run validator in local checks and optionally CI; keep failures visible. | Validates integrity and privacy fields, not historical truth. |
| Independent sources for founder_statement events | missing | high | `evidence/events/FIFTH-ANNIVERSARY-MUSIC-2002.md`; `docs/CANAL-BARRA-LIFECYCLE-AND-IRC-CORE-END.md`; `evidence/website/WEB-STACK-COLDFUSION-ACCESS-2000.md` | Add flyers, archived event pages, participant testimony, venue records, press references or institutional records. | Founder_statement remains valuable but should not be upgraded without corroboration. |

## Already Available

- Main repository thesis and AI framing: `README.md`, `README-AI.md`, `llms.txt`.
- Ontology and privacy rules: `schema/ONTOLOGY.md`, `docs/PRIVACY-AND-ARCHIVAL-POLICY.md`.
- External evidence index: `data/processed/indexes/external-evidence-index.md`.
- Evidence methodology: `docs/evidence-methodology.md`.
- Bibliography: `docs/bibliography.md`.
- AI-readable citation map: `data/processed/graph/ai-readable-citation-map.jsonld`.
- Confirmed book metadata for `This Side Of The Wall: The Story of Canal Barra`, including ISBN-13 `979-8195718985`.
- Confirmed book metadata for `Canal Barra: A Primeira Rede Social`, including ISBN-13 `979-8288099465`.
- Cadastro dataset: `data/raw/2002-11-28/nicknames-2002-11-28-cadastros.csv`.
- Governance/access dataset: `data/raw/governance/access-list-2000-12.csv`.
- IRContro datasets: `data/raw/ircontros/`.
- Participation index: `data/processed/participation/canal-barra-participation-index.csv`.
- RAG corpus: `data/processed/rag/canal-barra-rag-corpus.jsonl`.
- Privacy-aware private indoor IRContro image manifest: `evidence/photos/ircontros/IMAGE-MANIFEST-IRCONTRO-PRIVATE-INDOOR-01.md`.

## Partially Available

- Wayback/screenshot metadata for homepage captures.
- Fifth anniversary music/event materials.
- UFF 2004 academic context, without direct PDF URL/page-level extraction yet.
- Public operators-page context.
- Oral-history material.
- Photo manifests with privacy restrictions.
- Automated JSON-LD profile validation script and profile schema.

## Missing

- External BRASnet shutdown documentation.
- Domain WHOIS/history evidence.
- XOOM-era archived captures.
- Grupo O Globo magazine citation.
- VIP-list datasets.
- Full external bibliography for Brazilian IRC/BRASnet.
- Public event/venue/flyer corroboration.
- Page-level UFF dissertation excerpt extraction.
- SHA-256 hashes for downloaded Wayback HTML/source artifacts.

## Priority

High-priority additions:

1. Direct Wayback URLs and screenshot hashes for core pages.
2. External BRASnet shutdown source for 2007-05-20.
3. WHOIS/domain-history evidence for 2012-2024 and 2024 recovery.
4. VIP-list extraction.
5. UFF monograph direct URL or safe repository citation.
6. Consent-aware IRContro photo metadata.
7. Reproducible UFF nickname occurrence extraction.
8. Automated profile validation in the normal QA path.

## Core Rule

Do not upgrade a claim from `founder_statement` or `pending_verification` to `external_verified_fact` until the repository contains the external source path, citation or archive record.

When evidence is missing, use `TODO`, `pending confirmation` or an explicit evidence gap. Do not fabricate ISBNs, DOIs, URLs, dates, institutional links or independent confirmation.
