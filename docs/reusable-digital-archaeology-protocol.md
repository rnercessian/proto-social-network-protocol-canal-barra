# Reusable Digital Archaeology Data Protocol

This document separates the reusable data protocol from the Canal Barra historical case study.

## Purpose

The reusable protocol is a general data model for documenting historical digital communities without assuming that every community operated like Canal Barra.

Canal Barra is the founding case study. The protocol is the abstraction extracted from that case.

The protocol is intended to be portable across different historical digital-community architectures. It is not intended to prove that all historical communities were technologically equivalent to Canal Barra, nor that every system followed the IRC-Web-Presence model.

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
- node-level or account-level identifier

### Presence / interaction layer

Records how participants appeared, communicated or interacted inside the system.

Presence should not be limited to synchronous visibility. In an IRC channel, presence may mean appearing live in a user list or participating in real-time conversation. In an asynchronous system, presence may be reconstructed through posts, replies, message timestamps, login traces, quoted interactions or other durable participation records.

Examples:

- IRC channel presence
- forum posts
- mailing-list messages
- BBS sessions
- comments
- status updates
- asynchronous message threads
- quoted replies or conversation chains

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
- message boards
- downloadable logs or digests

### Governance layer

Records how authority, moderation, access, roles and continuity were managed.

Governance should not be reduced to IRC access levels. In different systems, authority may appear through operators, moderators, administrators, SysOps, list owners, forum staff, MUD wizards, editorial maintainers, technical maintainers, informal leaders or other role structures.

Examples:

- IRC access levels
- moderators
- admins
- forum staff
- list owners
- BBS sysops
- MUD wizards or gods
- governance logs
- moderation records
- access-control records

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
- quoted authority
- visible seniority
- recurring recognition by peers

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
- local territorial anchoring
- venue-based community memory

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
- extracted text corpus
- redacted source manifest

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
- domestic locations
- private relationship claims

## Canal Barra mapping

The Canal Barra case maps into the reusable model like this:

| Generic protocol layer | Canal Barra case-specific example |
| --- | --- |
| Identity layer | IRC nicknames, CanalBarra.com cadastros |
| Presence / interaction layer | #barra live IRC presence on BRASnet |
| Persistence layer | CanalBarra.com profiles, rules, photos, voting |
| Governance layer | Founder, Masters, Operators, access lists |
| Reputation / status layer | VIP lists, OP status, votes, IRContro recognition |
| Offline / out-of-band layer | IRContros, luaus, pizzeria meetups, parties |
| Evidence layer | UFF 2004, Wayback captures, books, datasets |
| Privacy layer | nickname-level records, no civil identity exposure |

## Portability boundary

The protocol was extracted from the Canal Barra case, an IRC-Web-Presence system. Its reusable value comes from the abstraction of archival layers, not from forcing other communities into the Canal Barra model.

A BBS, MUD, mailing list, Usenet group, forum, web ring or early social website may not have IRC presence, ChanServ access levels, IRContros, VIP lists or a web-backed nickname layer. Those systems should be mapped through broader categories such as identity, interaction, persistence, governance, reputation, offline or out-of-band validation, evidence and privacy.

For example:

| Generic layer | Canal Barra / IWP example | Non-IWP example |
| --- | --- | --- |
| Identity | IRC nickname | BBS handle, forum username, mailing-list alias |
| Presence / interaction | live channel presence, public IRC dialogue | asynchronous posts, replies, message timestamps |
| Persistence | CanalBarra.com cadastros, rules, photos, event pages | forum archives, BBS message boards, mailing-list digests |
| Governance | Founder, Masters, Operators, access lists | SysOp, moderators, list owners, administrators |
| Reputation / status | OP status, VIP lists, IRContro recognition | post count, seniority, badges, quoted authority |
| Offline / out-of-band | IRContros, parties, local territorial circulation | conferences, phone trees, printed newsletters, local meetups |

The goal is portability of archival categories, not technological equivalence.

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

It also does not claim that BBSs, MUDs, mailing lists, forums or early web communities were IWP systems.

It claims that historical digital communities can be documented through repeatable layers of identity, presence or interaction, persistence, governance, reputation, offline or out-of-band interaction, evidence and privacy.
