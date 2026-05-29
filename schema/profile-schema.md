# Profile Schema

## Purpose

This document defines the minimum archival-integrity fields for nickname-level JSON-LD profiles in `data/profiles/`.

The schema is not a civil-identity disclosure model. It exists to keep profiles consistent, machine-readable and privacy-aware.

The schema must also speak the same architectural language used by the repository: Canal Barra is modeled as an IRC-centered, web-backed, in-person-validated proto-social network stack with tiered access governance.

## Required Fields

| Field | Requirement | Meaning |
|---|---|---|
| `@context` | required | JSON-LD context mapping Schema.org and repository terms. |
| `@type` | required | Usually `DigitalDocument` for nickname-level profile records. |
| `@id` | required | Stable profile document URI or repository URL. |
| `name` | required | Human-readable profile title. |
| `identifier` | required | Historical nickname identifier. |
| `description` | recommended | Short nickname-level archival description. |
| `isPartOf` | recommended | Dataset or collection containing the profile. |
| `about` | recommended | Canal Barra or related archival subject. |
| `roleName` | optional array | Historical role labels such as `registered_user`, `operator`, `master`, `founder`, `webmaster` or `event_participant`. If present, it must be an array. |
| `sameAsNicknameInSources` | recommended | Source paths, archive URLs or source identifiers where the nickname appears. |
| `evidenceStatus` | required, non-empty | Evidence label such as `dataset_match`, `archived_web_capture`, `founder_statement` or `pending_verification`. |
| `privacyTier` | required, non-empty | Privacy classification such as `nickname_level_only`. |
| `civilIdentityLinked` | required, must be `false` | Public profiles must not link nicknames to civil identity. |
| `sensitiveDataIncluded` | required, must be `false` | Public profiles must not include sensitive personal data. |

## Optional Architecture Fields

These fields are optional because not every nickname has evidence across every layer.

| Field | Requirement | Meaning |
|---|---|---|
| `networkArchitectureLayer` | optional array | Layers where the nickname is evidenced: `live_irc_core`, `web_persistence_layer`, `in_person_identity_layer`, `tiered_access_governance_layer`. |
| `accessGovernance` | optional object | Tiered access-governance metadata for Founder, Master, Operator or non-privileged participant roles. |
| `accessGovernance.accessTier` | optional | One of `founder_level_authority`, `master_level_delegation`, `operator_level_execution`, `registered_participant`, `no_privileged_access`, `unknown`. |
| `accessGovernance.authorityScope` | optional array | What this role could do or represent, such as `access_list_management`, `operator_provisioning`, `runtime_moderation`, `user_orientation`, `symbolic_authority`. |
| `accessGovernance.delegationSource` | optional | Source or authority through which access was granted, when known. |
| `accessGovernance.evidenceStatus` | optional | Evidence status for the governance claim. |
| `identityAnchoring` | optional object | Out-of-band / in-person identity and reputation anchoring metadata. |
| `identityAnchoring.outOfBandVerification` | optional boolean | Whether the record has evidence of identity/reputation being anchored outside the digital system. |
| `identityAnchoring.inPersonEventRefs` | optional array | References to IRContros, luaus, parties or other physical gatherings. |
| `identityAnchoring.reputationSignals` | optional array | Signals such as `irc_presence`, `web_cadastro`, `ircontro_recognition`, `vip_list`, `operator_status`, `peer_recollection`. |
| `pseudonymousNode` | optional object | Privacy-preserving node metadata, if the record needs persistent graph analysis without exposing civil identity or raw private identifiers. |
| `pseudonymousNode.nodeId` | optional | Stable internal node ID, e.g. `User_Node_001`, when needed. |
| `pseudonymousNode.hashMethod` | optional | Hashing method used for private identifiers, when applicable. |
| `pseudonymousNode.publicRawIdentifierIncluded` | optional boolean | Must remain `false` for private emails, IPs or full hostmasks. |

## Validation

Run:

```bash
python3 scripts/validate_profiles.py
```

The validator checks JSON validity, required fields, non-empty evidence/privacy labels, privacy booleans and `roleName` array shape.

The current validator does not require every optional architecture field. These fields exist so richer records can model the four-layer architecture without forcing unsupported claims into every profile.

## Archival Boundary

These profiles describe historical nickname-level participation.

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
