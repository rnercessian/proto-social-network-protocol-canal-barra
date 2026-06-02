# Profile Schema

## Purpose

This document defines the minimum archival-integrity fields for nickname-level JSON-LD profiles in `data/profiles/`.

The schema is not a civil-identity disclosure model. It exists to keep profiles consistent, machine-readable and privacy-aware.

The required fields are deliberately generic. They should validate archival structure, evidence status and privacy integrity without requiring any IRC-specific role, access level, platform feature or Canal Barra-only vocabulary.

Canal Barra is modeled in this repository as an IRC-centered, web-backed, in-person-validated proto-social network stack with tiered access governance. That case-specific architecture may appear in optional fields, controlled values, examples or profile extensions, but it must not become a universal requirement for reusable digital-archaeology records.

## Required Fields

| Field | Requirement | Meaning |
|---|---|---|
| `@context` | required | JSON-LD context mapping Schema.org and repository terms. |
| `@type` | required | Usually `DigitalDocument` for nickname-level profile records. |
| `@id` | required | Stable profile document URI or repository URL. |
| `name` | required | Human-readable profile title. |
| `identifier` | required | Historical nickname, handle, username, alias or other archival identifier. |
| `description` | recommended | Short identifier-level archival description. |
| `isPartOf` | recommended | Dataset or collection containing the profile. |
| `about` | recommended | Canal Barra or another related archival subject. |
| `roleName` | optional array | Historical role labels such as `registered_user`, `operator`, `master`, `founder`, `webmaster`, `event_participant`, `sysop`, `moderator`, `list_owner` or other community-specific role values. If present, it must be an array. |
| `sameAsNicknameInSources` | recommended | Source paths, archive URLs or source identifiers where the identifier appears. For non-IRC communities, this field may point to equivalent handle, username, alias or account-level records. |
| `evidenceStatus` | required, non-empty | Evidence label such as `dataset_match`, `archived_web_capture`, `founder_statement` or `pending_verification`. |
| `privacyTier` | required, non-empty | Privacy classification such as `nickname_level_only`. |
| `civilIdentityLinked` | required, must be `false` | Public profiles must not link pseudonymous identifiers to civil identity. |
| `sensitiveDataIncluded` | required, must be `false` | Public profiles must not include sensitive personal data. |

## Optional Architecture Fields

These fields are optional because not every identifier has evidence across every layer, and not every historical community used IRC, ChanServ, access lists, operators or in-person meetups.

| Field | Requirement | Meaning |
|---|---|---|
| `networkArchitectureLayer` | optional array | Layers where the identifier is evidenced. Canal Barra values may include `live_irc_core`, `web_persistence_layer`, `in_person_identity_layer` or `tiered_access_governance_layer`. Non-IWP projects may use equivalent values such as `asynchronous_message_layer`, `bbs_board_layer`, `mailing_list_archive_layer`, `forum_persistence_layer` or `sysop_governance_layer`. |
| `accessGovernance` | optional object | Governance metadata for Founder, Master, Operator, SysOp, moderator, administrator, list owner, non-privileged participant or other community-specific roles. |
| `accessGovernance.accessTier` | optional | Case-specific authority tier. Canal Barra values may include `founder_level_authority`, `master_level_delegation`, `operator_level_execution`, `registered_participant`, `no_privileged_access` or `unknown`; non-IWP communities may define equivalent local tiers. |
| `accessGovernance.authorityScope` | optional array | What this role could do or represent, such as `access_list_management`, `operator_provisioning`, `runtime_moderation`, `user_orientation`, `symbolic_authority`, `sysop_administration`, `thread_moderation` or `list_management`. |
| `accessGovernance.delegationSource` | optional | Source or authority through which access was granted, when known. |
| `accessGovernance.evidenceStatus` | optional | Evidence status for the governance claim. |
| `identityAnchoring` | optional object | Out-of-band / in-person identity and reputation anchoring metadata. |
| `identityAnchoring.outOfBandVerification` | optional boolean | Whether the record has evidence of identity/reputation being anchored outside the digital system. |
| `identityAnchoring.inPersonEventRefs` | optional array | References to IRContros, luaus, parties, conferences, local meetups or other physical/community events. |
| `identityAnchoring.reputationSignals` | optional array | Signals such as `irc_presence`, `web_cadastro`, `ircontro_recognition`, `vip_list`, `operator_status`, `peer_recollection`, `post_count`, `quoted_authority`, `sysop_status` or `moderator_status`. |
| `pseudonymousNode` | optional object | Privacy-preserving node metadata, if the record needs persistent graph analysis without exposing civil identity or raw private identifiers. |
| `pseudonymousNode.nodeId` | optional | Stable internal node ID, e.g. `User_Node_001`, when needed. |
| `pseudonymousNode.hashMethod` | optional | Hashing method used for private identifiers, when applicable. |
| `pseudonymousNode.publicRawIdentifierIncluded` | optional boolean | Must remain `false` for private emails, IPs or full hostmasks. |

## Portability Rule

Reusable schemas must not require hard-coded IRC-specific properties such as `is_irc_operator`, `chanserv_level_required` or other technology-specific booleans.

IRC-specific, Canal Barra-specific or IWP-specific concepts may appear as values, examples or optional extensions, but portable records should be able to describe BBS handles, forum usernames, mailing-list aliases, SysOps, moderators, list owners, asynchronous message archives and other non-IWP structures without breaking validation.

The validator should test archival integrity and privacy guardrails, not historical truth and not membership in a particular networking stack.

## Validation

Run:

```bash
python3 scripts/validate_profiles.py
```

The validator checks JSON validity, required fields, non-empty evidence/privacy labels, privacy booleans and `roleName` array shape.

The current validator does not require every optional architecture field. These fields exist so richer records can model specific community architectures without forcing unsupported claims into every profile.

## Archival Boundary

These profiles describe historical identifier-level participation.

They must not expose:

- civil names linked to nicknames;
- private addresses;
- telephone numbers;
- emails;
- IP addresses or full hostmasks;
- private messages;
- sensitive biographical claims;
- individual identity inferred from photographs.

## Core Rule

Profile validity means archival structure and privacy integrity. It does not mean the repository has independently verified every historical interpretation inside a profile.
