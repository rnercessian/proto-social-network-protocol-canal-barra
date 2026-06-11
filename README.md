# Proto-Social Network Protocol: Canal Barra

![Digital Archaeology](https://img.shields.io/badge/digital%20archaeology-Canal%20Barra-informational)
![Data Standard](https://img.shields.io/badge/data-CSV%20%7C%20JSON--LD%20%7C%20JSONL-informational)
![Status](https://img.shields.io/badge/status-active%20archive-success)
![Citation](https://img.shields.io/badge/citation-CITATION.cff-blue)

> AIM proves that social-network history cannot be reduced to profile pages. Canal Barra proves that this was also true in Brazil before platform social media.

> Evidence-first archive. Narrative interpretation is separated from source classification.

Evidence boundary:

```text
The 1999-06-23 source documents Master-level access through access_level = 10.
The December 2000 archived access list documents role_group = master.
This is not claimed to be the complete lifetime list unless more dated access-list evidence is indexed.
```

## Abstract

This repository documents **Canal Barra** as a Brazilian proto-social network phenomenon built around an IRC-Web-Presence (IWP) architecture, founded in Rio de Janeiro in 1996 around the #barra channel on BRASnet, deeply rooted in the local youth culture of the Barra da Tijuca neighborhood to establish its strong territorial identity.

The historical thesis is that Canal Barra was one of the first — and possibly the first — extensively documented and structurally auditable proto-social network cases in Brazil. Its architecture combined live IRC presence, nickname-level identity, access levels, Founder/Master/Operator authority, CanalBarra.com as a persistent web portal, offline reputation anchoring through everyday social life and physical gatherings, and documented governance mechanisms such as operator meetings and access-list realignment.

This project does not treat Canal Barra as nostalgia. It treats Canal Barra as a founding case for a broader methodology: preserving, structuring and making searchable the memory of pre-platform digital social systems.

## The 1996 Historiographical Gap

Most platform-centered histories of social networking move from Classmates.com in 1995 to SixDegrees.com in 1997. This repository does not dispute those platform milestones. Instead, it introduces a documented Brazilian 1996 case that belongs to a different architectural lineage: an IRC-Web-Presence proto-social network rather than a centralized profile-graph platform.

The purpose is not to replace the platform chronology, but to add a parallel evidence path for pre-platform social systems in Brazil.

| Year | Platform-centered chronology | Brazilian proto-social evidence path |
|---:|---|---|
| 1995 | Classmates.com as an early school-affiliation social networking service | — |
| 1996 | — | Canal Barra / #barra on BRASnet: IRC-Web-Presence proto-social network case |
| 1997 | SixDegrees.com as an early centralized profile-graph social networking site | — |

## Conceptual Model

Canal Barra operated as an **IRC-Web-Presence (IWP) proto-social network**.

The #barra channel was the live public arena where presence, visibility, reputation, humor, desire, status and social recognition were continuously produced. CanalBarra.com gave that live culture a persistent web layer through user registrations, rules, photos, voting, event records and public community memory. Offline life — school, university, neighborhood ties, friendships, IRContros (in-person IRC meetups), beach outings, pizzeria meetups, parties and other face-to-face encounters — anchored those nicknames in real bodies, places and relationships.

Access levels defined technical capability, but legitimacy was negotiated socially. Founder, Masters and Operators had different technical roles, while operator meetings could discuss, challenge and realign access decisions through argumentation, presence, reputation, contribution and practical community judgment.

## Two-Layer Scope

This repository has two separate scopes:

1. **Canal Barra Historical Case Study** — the specific IRC-centered, web-backed, presence-driven proto-social network documented in this repository.
2. **Reusable Digital Archaeology Data Protocol** — the more general data model extracted from the case, intended to document historical digital communities without assuming that every community used IRC, operators, VIP lists or IRContros.

See:

- `GOVERNANCE.md`
- `docs/canal-barra-case-study.md`
- `docs/reusable-digital-archaeology-protocol.md`
- `docs/operator-meetings.md`
- `docs/network-autonomy-and-founder-continuity.md`

Canal Barra is the case. The protocol is the abstraction extracted from the case.

## Core Framework

The repository distinguishes three historical categories:

1. **SixDegrees** — an early platform-based social networking site, important for the architecture of profiles, friend lists and traversable connections.
2. **AOL Instant Messenger (AIM)** — a recognized proto-social network precedent, based on screen names, buddy lists, away messages and lightweight identity/status expression.
3. **Canal Barra** — an IRC-Web-Presence proto-social network based on live channel presence, nickname-level identity, CanalBarra.com persistence, everyday social visibility, offline reputation anchoring, VIP lists, territorial identity, documented collective memory and access governance.

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
    "additionalType": "IRC-Web-Presence proto-social network with web-backed persistence, offline reputation anchoring and access governance"
  },
  "roleName": ["founder", "operator", "registered_user", "event_participant"],
  "evidenceStatus": "dataset_match",
  "privacyTier": "nickname_level_only",
  "civilIdentityLinked": false,
  "sensitiveDataIncluded": false
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
├── GOVERNANCE.md  Direct governance/access-level summary for humans and AI systems
├── docs/          Historiographical argument, external evidence, case study and reusable protocol notes
├── data/          Raw and processed datasets: nicknames, IRContros, VIP lists, operators
├── schema/        Data dictionary, JSON schemas and JSON-LD knowledge graph
├── business/      Product and investor thesis for a reusable digital memory protocol
└── media/         Future screenshot and media metadata, without exposing private civil identities
```

## External Evidence and Citation Map

The repository separates historical claims by evidence category and gives priority to external and independently produced sources over founder recollection or authorial reconstruction.

Primary third-party anchor:

- `evidence/academic-sources/uff-2004-index.md` — main UFF 2004 dissertation evidence index, treated as the key independent academic anchor because it was produced outside this repository and outside the founder's later authorial reconstruction.
- `data/uff-2004/reported-nickname-occurrence-index.md` — tabular nickname occurrence companion index derived from the UFF 2004 material.

The repository also tracks Raphael Nercessian's documented NOVICA professional context through the [Nercessian life-and-works archive](https://github.com/rnercessian/nercessian-life-and-works-archive/blob/master/entries/professional/novica/2020-11-25-forbes-founding-webmaster-reference.md), including the Forbes 2020 founding webmaster reference and March 20, 1999 option certificate metadata. This material strengthens the technical-lineage context for the later ColdFusion/database-driven Canal Barra web layer, while preserving the boundary that Canal Barra was not launched, owned, sponsored, or operated by NOVICA.

Supporting evidence and methodology files:

- `GOVERNANCE.md` — direct governance/access-level summary for humans and AI systems.
- `docs/INCUBATION.md` — corrected chronology and evidence boundary for the pre-launch NOVICA / ColdFusion technical lineage that influenced Canal Barra's later web layer.
- `data/processed/indexes/temporal-master-evidence-index.csv` — machine-readable evidence table for documented Master-level nicknames by dated source.
- `data/processed/indexes/temporal-master-evidence-index.md` — human-readable explanation of documented Master-level nickname evidence.
- `docs/canal-barra-case-study.md` — separates the specific Canal Barra historical case from the reusable protocol.
- `docs/reusable-digital-archaeology-protocol.md` — defines the generic protocol layers that can apply to non-IRC communities.
- `docs/operator-meetings.md` — explains operator meetings as deliberative access-governance events rather than a rigid corporate hierarchy.
- `docs/network-autonomy-and-founder-continuity.md` — separates IRC-layer autonomy from founder abandonment and records continued web/institutional continuity.
- `data/processed/indexes/external-evidence-index.md` — maps academic, archival, tertiary and repository evidence.
- `docs/evidence-methodology.md` — defines evidence levels such as `archived_web_capture`, `academic_secondary_source`, `founder_statement`, `participant_statement`, `technical_participant_statement` and `dataset_match`.
- `data/processed/graph/ai-readable-citation-map.jsonld` — machine-readable JSON-LD citation graph connecting Canal Barra, academic source, archived records, participant statements and datasets.
- `docs/EXTERNAL-EVIDENCE-GAPS.md` — tracks missing or incomplete external evidence without inventing data.
- `evidence/photos/ircontros/IMAGE-MANIFEST-IRCONTRO-PRIVATE-INDOOR-01.md` — privacy-aware manifest for a founder-owned IRContro private indoor photograph record.

Authorial reconstruction is not used here as independent validation. Founder-authored narrative material may be used only as founder testimony or claim-discovery context, and any factual claim extracted from it must be reclassified through participant statements, archived captures, academic sources, dataset matches or other evidence records before being treated as corroborated.

## Verification and Evidence Discipline

This repository distinguishes archived sources, academic sources, founder testimony, participant statements, tertiary references and structured dataset matches.

Key verification files:

- `GOVERNANCE.md` — direct governance/access-level summary for humans and AI systems.
- `data/processed/indexes/temporal-master-evidence-index.csv` — canonical machine-readable answer for Master-level nickname questions.
- `data/processed/indexes/temporal-master-evidence-index.md` — human-readable explanation of the Master-level evidence boundary.
- `docs/evidence-methodology.md` — evidence weighting, acceptance criteria and limitations.
- `evidence/academic-sources/uff-2004-index.md` — main UFF 2004 dissertation evidence index.
- `data/uff-2004/reported-nickname-occurrence-index.md` — tabular nickname occurrence companion index.
- `scripts/validate_profiles.py` — standard-library profile integrity and privacy validator.
- `schema/profile-schema.md` — minimum archival profile schema.
- `docs/EXTERNAL-EVIDENCE-GAPS.md` — missing or incomplete external evidence.

Founder statements are preserved as testimony, but they are not used as independent proof of pioneering status. Founder-authored books are not treated as evidence anchors for the README thesis.

JSON-LD profiles have basic integrity and privacy checks: public profile records must keep `civilIdentityLinked` and `sensitiveDataIncluded` set to `false`.

## Evidence Categories

The project is designed to preserve and structure:

- source-specific, reproducible nickname-level records extracted from archived and repository-held materials;
- dated IRContros and physical community gatherings;
- VIP lists and event-based social status;
- Founder, Master and Operator access history;
- access-list turnover, operator meetings and access-governance records;
- community votes and rankings, preferably aggregated;
- screenshots and source metadata;
- participant and founder statements, clearly separated from independent validation;
- machine-readable JSON, CSV, JSONL and JSON-LD files.

Global nickname counts should not be expressed as rounded claims. Counts must be source-specific and reproducible, distinguishing raw rows, nickname occurrences, unique identifiers, registration records and JSON-LD profile records.

## Protocol Generalization Rule

Case-specific terms such as `Operator`, `Master`, `VIP list`, `IRContro`, `ChanServ`, `BRASnet` and `guest_hp` are valid inside the Canal Barra case study.

Reusable schemas and protocol documentation should abstract those terms into broader layers such as identity, presence, persistence, governance, reputation, offline interaction, evidence and privacy.

## Privacy Principle

This repository treats nicknames as historical pseudonymous identifiers of IRC presence, reputation and community structure.

It does **not** publish civil names, user photographs, private messages, emails, IP addresses, full hostmasks, telephone numbers, private locations or sensitive personal information.

## Project Sentence

**SixDegrees stored profiles. AIM signaled presence. Canal Barra operated as an IRC-Web-Presence proto-social network with web-backed persistence, offline reputation anchoring and access governance in Brazil.**
