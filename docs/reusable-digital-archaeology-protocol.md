# Reusable Digital Archaeology Data Protocol

This document separates the reusable data protocol from the Canal Barra historical case study.

## Purpose

The reusable protocol is a general data model for documenting historical digital communities without assuming that every community operated like Canal Barra.

Canal Barra is the founding case study. The protocol is the abstraction extracted from that case.

## General layers

The reusable model should describe historical digital communities through abstract layers that can apply across different systems.

### Identity layer

Records pseudonymous, public or semi-public identifiers without forcing civil identity exposure.

Examples:

- IRC nickname
- forum username
- BBS handle
- mailing-list address alias
- screen name
- profile slug

### Presence / interaction layer

Records how participants appeared, communicated or interacted inside the system.

Examples:

- IRC channel presence
- forum posts
- mailing-list messages
- BBS sessions
- comments
- status updates

### Persistence layer

Records what the system preserved beyond live interaction.

Examples:

- profiles
- cadastros
- forum threads
- archives
- photo galleries
- user pages
- rules pages
- event pages

### Governance layer

Records how authority, moderation, access, roles and continuity were managed.

Examples:

- IRC access levels
- moderators
- admins
- forum staff
- list owners
- BBS sysops
- governance logs
- moderation records

### Reputation / status layer

Records visible or socially meaningful signals of reputation, rank, trust or status.

Examples:

- VIP lists
- operator status
- post counts
- badges
- rankings
- curated lists
- event participation

### Offline / out-of-band layer

Records interactions or validation outside the digital system when relevant.

Examples:

- meetups
- parties
- conferences
- phone calls
- printed newsletters
- photographs
- in-person identity recognition

### Evidence layer

Records source type, provenance, reliability and uncertainty.

Examples:

- archived snapshot
- academic source
- primary recollection
- peer recollection
- photograph metadata
- book citation
- dataset match
- unresolved gap

### Privacy layer

Records what must not be exposed publicly.

Examples:

- civil names
- private emails
- IP addresses
- full hostmasks
- telephone numbers
- private photos
- private messages
- sensitive personal data

## Canal Barra mapping

The Canal Barra case maps into the reusable model like this:

| Generic protocol layer | Canal Barra case-specific example |
| --- | --- |
| Identity layer | IRC nicknames, CanalBarra.com cadastros |
| Presence / interaction layer | #barra live IRC presence on BRASnet |
| Persistence layer | CanalBarra.com profiles, rules, photos, voting |
| Governance layer | Founder, Masters, Operators, access lists |
| Reputation / status layer | VIP lists, OP status, votes, IRContro recognition |
| Offline / out-of-band layer | IRContros, luaus, pizzarias, parties |
| Evidence layer | UFF 2004, Wayback captures, books, datasets |
| Privacy layer | nickname-level records, no civil identity exposure |

## Design rule

Schemas intended for reuse should avoid hard-coding Canal Barra-only terms as required fields.

Prefer generic fields such as:

- `identifier`
- `identityType`
- `roleType`
- `governanceRole`
- `persistenceSource`
- `interactionLayer`
- `reputationSignal`
- `offlineEventType`
- `evidenceStatus`
- `privacyTier`

Canal Barra-specific vocabulary may appear as values, extensions or case-study mappings, but not as universal requirements.

## Boundary statement

The protocol does not claim that every historical digital community had IRC channels, operators, VIP lists or IRContros.

It claims that historical digital communities can be documented through repeatable layers of identity, presence, persistence, governance, reputation, offline interaction, evidence and privacy.
