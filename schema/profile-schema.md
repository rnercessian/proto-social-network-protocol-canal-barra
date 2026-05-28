# Profile Schema

## Purpose

This document defines the minimum archival-integrity fields for nickname-level JSON-LD profiles in `data/profiles/`.

The schema is not a civil-identity disclosure model. It exists to keep profiles consistent, machine-readable and privacy-aware.

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
| `roleName` | optional array | Historical role labels such as `registered_user`, `operator`, `event_participant` or `founder`. If present, it must be an array. |
| `sameAsNicknameInSources` | recommended | Source paths, archive URLs or source identifiers where the nickname appears. |
| `evidenceStatus` | required, non-empty | Evidence label such as `dataset_match`, `archived_web_capture`, `founder_statement` or `pending_verification`. |
| `privacyTier` | required, non-empty | Privacy classification such as `nickname_level_only`. |
| `civilIdentityLinked` | required, must be `false` | Public profiles must not link nicknames to civil identity. |
| `sensitiveDataIncluded` | required, must be `false` | Public profiles must not include sensitive personal data. |

## Validation

Run:

```bash
python3 scripts/validate_profiles.py
```

The validator checks JSON validity, required fields, non-empty evidence/privacy labels, privacy booleans and `roleName` array shape.

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
