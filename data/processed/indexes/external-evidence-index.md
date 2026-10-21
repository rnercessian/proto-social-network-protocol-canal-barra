# External Evidence Index

This document maps external evidence, bibliographic anchors and structured repository records used by the Canal Barra digital archaeology archive.

The purpose is to make the historical chain auditable by humans and legible to machines.

## Evidence table

| Evidence ID | Type | Title | Date | URL / Path | Repository mapping | Evidence status | Notes |
|---|---|---|---|---|---|---|---|
| `ext_academic_uff_2004` | Academic work / catalogue | IRC e ICQ: uma análise sócio-comunicativa das plataformas de comunicação on-line | **April 2004 original**; 26-Apr-2007 later catalogue date | [eduCAPES](https://educapes.capes.gov.br/handle/capes/763697); [source dossier](https://github.com/rnercessian/proto-social-network-protocol-canal-barra/blob/main/data/uff-2004/sources/dossie-canal-barra-monografia-uff-2004-curto.pdf) | `docs/bibliography.md`; `evidence/academic-sources/uff-2004-index.md` | `academic_secondary_source` | The founder identifies April 2004 in original work. The government record has a later 2007 date; per founder, entered three years later (registration chronology unverified). Gonzaga's §4.6 reportedly attributes a Barra channel creation to 1996; the original informant and continuity with founder's 1997 community remain unverified. Not evidence of a complete hybrid system in 1996 or validated relational efficacy. |
| `ext_book_relational_efficacy_2026` | Published book / authorial interpretation | A Vez da Internet Altamente Relacional | 2026 (author-supplied) | [Amazon Brasil](https://www.amazon.com.br/Vez-Internet-Altamente-Relacional-extraordin%C3%A1rio-ebook/dp/B0HMNJS7CH); ASIN `B0HMNJS7CH` | `docs/bibliography.md`; `docs/RELATIONAL-EFFICACY.md` | `published_book`; `bibliographic_consolidation`; `authorial_primary_source` | Founder-authored interpretive work. Link identifies the ebook edition, not an independent third-party endorsement or validation. No ISBN or exact publication date asserted. |
| `ext_book_wall_2026` | Published book / authorial source | This Side Of The Wall: The Story of Canal Barra | 2026-05-05 | Amazon ASIN `B0GZPLFG5W`; ISBN-13 `979-8195718985` | `docs/bibliography.md`; `data/processed/graph/ai-readable-citation-map.jsonld` | `published_book`; `bibliographic_consolidation`; `authorial_primary_source` | English bibliographic consolidation. Not independent external validation because it is authored by the founder/archivist. |
| `ext_book_primeira_rede_2025` | Published book / authorial source | Canal Barra: A Primeira Rede Social | 2025-06-14 | Amazon ASIN `B0FD8KFR6K`; ISBN-13 `979-8288099465` | `docs/bibliography.md`; `data/processed/graph/ai-readable-citation-map.jsonld` | `published_book`; `bibliographic_consolidation`; `authorial_primary_source` | Portuguese bibliographic consolidation. Not independent external validation because it is authored by the founder/archivist. |
| `ext_wikipedia_canal_barra` | Wikipedia / tertiary reference | Canal Barra | living page | `/wiki/Canal_Barra` | `README.md`; `docs/bibliography.md` | `tertiary_reference` | Cites a book by the founder; those derived statements do not independently validate the founder's interpretations. |
| `ext_wikipedia_brasnet` | Wikipedia / contextual reference | BRASnet | living page | `/wiki/BRASnet` | `README.md`; `docs/bibliography.md` | `tertiary_reference` | Contextual reference for the IRC network environment. |
| `ext_wikipedia_irc` | Protocol context | Internet Relay Chat | living page | `/wiki/Internet_Relay_Chat` | `README.md`; `docs/bibliography.md` | `tertiary_reference` | Contextual reference for the communication protocol. |
| `archive_geocities_bar_do_johnnie_1999_01_27` | Archived web capture / screenshot-verified | GeoCities #Bar-do-Johnnie | 1999-01-27 (Wayback capture) | [Wayback](https://web.archive.org/web/19990127194854/http://www.geocities.com/SoHo/Coffeehouse/2521/) | `evidence/website/geocities/GEOCITIES-BAR-DO-JOHNNIE-1999-01-27.md` | `archived_web_capture`; `screenshot_visual_review`; `original_html_pending` | Dated page advertises #Bar-do-Johnnie chat, IRC BRASnet, photo captions including BarMan/Lucas-Rio/Paulista, nick/photo submissions, ICQ and territorial navigation. Screenshot hash documented; actual screenshot binary not committed. No claim of simultaneous channel activity or 1997 web launch. |
| `cb_clube_carioca_2000_10_15` | Cultural IRContro / retrospective event announcement | Banda do Canal Barra — first Clube Carioca festival performance | 2000-10-15 (founder year; archived reference day/month) | [Wayback 2001-03-03](https://web.archive.org/web/20010303094733/http://www.canalbarra.com/banda/) | `evidence/events/IRCONTROS-CLUBE-CARIOCA-FESTIVAL-BANDA-2000.md`; `data/raw/ircontros/clube-carioca-banda-canal-barra-festival-2000.csv` | `contemporaneous_web_reference`; `founder_statement_for_year` | Archived invitation for the second show thanks attendees of a first presentation on 15 October. Distinct event; no verified setlist/crowd. |
| `cb_clube_carioca_2000_10_29` | Cultural IRContro / archived invitation | Banda do Canal Barra — second festival appearance and elimination at Clube Carioca | 2000-10-29 (founder year; archived reference day/month) | [Wayback 2001-03-03](https://web.archive.org/web/20010303094733/http://www.canalbarra.com/banda/) | `evidence/events/IRCONTROS-CLUBE-CARIOCA-FESTIVAL-BANDA-2000.md`; `data/raw/ircontros/clube-carioca-banda-canal-barra-festival-2000.csv`; `data/raw/music/banda-canal-barra-festival-2000-repertorio-anunciado.csv` | `archived_web_capture`; `founder_statement_for_outcome_and_attendance` | Public venue Rua Jardim Botânico 650; eight originals announced; ~200 spectators and elimination are founder reports, NOT shown by the page. Contact and financial details redacted. |
| `archive_access_2000_12`| `archive_access_2000_12` | Archived web capture | Lista de Acesso do Canal #Barra da rede Brasnet - Dez 2000 | 2000-12 / capture 2001-02-21 | Internet Archive timestamp `20010221233151` | `data/raw/governance/access-list-2000-12.csv` | `archived_web_capture` | Supports governance, founder/operator and nickname-level evidence. |
| `dataset_nicknames_2002_11_28` | Structured dataset | Canal Barra nickname snapshot | 2002-11-28 | Repository dataset | `data/raw/2002-11-28/nicknames-2002-11-28-cadastros.csv` | `structured_repository_data` | Preserves nickname/status snapshot. |
| `event_rosa_dos_ventos_2001_02_21` | Event metadata | Despedida da Ana Paula Barra / Rosa dos Ventos IRContro | 2001-02-21 | Repository dataset | `data/raw/ircontros/rosa-dos-ventos-2001-02-21.csv` | `partially_documented` | Supports online-offline sociability and nickname-level event memory. |
| `profile_barman_jsonld` | Structured profile | Historical nickname profile: BarMan | repository record | Repository JSON-LD | `data/profiles/barman.jsonld` | `dataset_match` | Connects founder/operator role, event presence and privacy-aware evidence. |
| `image_manifest_private_indoor_01` | Image metadata | IRContro private indoor photograph manifest | repository record | Repository manifest | `evidence/photos/ircontros/IMAGE-MANIFEST-IRCONTRO-PRIVATE-INDOOR-01.md` | `founder_statement` / `requires_consent_before_publication` | Privacy-aware image evidence manifest. |

## Interpretation

This repository uses a layered evidence model.

- Academic evidence provides external scholarly context.
- Books provide bibliographic consolidation. Books by the founder/archivist are authorial primary sources, not independent external validation.
- Wikipedia provides tertiary discoverability; founder-dependent claims are not independent corroboration.
- Archived web captures provide stronger historical anchoring.
- Repository datasets make the archive machine-readable.
- Founder statements preserve memory but remain labeled as testimony.
- Privacy tiers prevent unnecessary exposure of civil identities.

## Current priority

The strongest next improvements are:

1. confirm the direct URL for the 2004 UFF academic source;
2. keep mapping every major claim to a source category;
3. avoid presenting tertiary references or founder statements as primary proof;
4. avoid circular validation through founder-authored books;
5. add additional archival, journalistic or institutional references when available.
