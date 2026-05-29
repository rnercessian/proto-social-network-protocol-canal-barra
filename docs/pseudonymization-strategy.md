# Pseudonymization Strategy

This document defines how the repository preserves graph-level historical analysis without exposing civil identity or sensitive personal data.

## Problem

Digital archaeology needs persistent identifiers to study participation, roles, reputation and governance.

However, public release of civil names, emails, IP addresses, full hostmasks, telephone numbers or private messages would violate the repository privacy model.

The repository must therefore preserve graph structure without exposing raw private identifiers.

## Principle

Public records should prefer nickname-level historical identifiers when the nickname itself is the historical public identity.

Private or sensitive identifiers must not be published raw.

When graph continuity is needed, use pseudonymous node IDs or salted hashes.

## Allowed public identifiers

Allowed when they are historically public or already part of archival source context:

- IRC nickname
- public historical role label
- public event participation label
- public website nickname / cadastro identifier
- public operator or master status when supported by evidence

## Prohibited public identifiers

Do not publish:

- civil names linked to nicknames without explicit consent and purpose;
- private emails;
- IP addresses;
- full hostmasks;
- telephone numbers;
- private addresses;
- private messages;
- unconsented contemporary photographs;
- sensitive personal data.

## Pseudonymous node IDs

When a stable non-public identity is needed for graph analysis, use a generated identifier:

```text
User_Node_001
User_Node_002
User_Node_003
```

The mapping between node IDs and any private source identifiers must be held outside the public repository.

## Hashing policy

If historical private identifiers must be matched across sources, prefer salted SHA-256 hashes kept stable within a closed research context.

Example conceptual fields:

```json
{
  "pseudonymousNode": {
    "nodeId": "User_Node_001",
    "hashMethod": "sha256_salted",
    "publicRawIdentifierIncluded": false
  }
}
```

The salt must not be committed to the public repository.

Unsalted hashes are discouraged because emails, IPs and hostmasks may be vulnerable to dictionary attacks.

## Graph preservation

The goal is to preserve relationships such as:

- same pseudonymous participant appears in multiple sources;
- same nickname appears in access-list and IRContro evidence;
- same participant moves between role states;
- same participant has reputation signals across web, IRC and offline layers.

The goal is not to expose civil identity.

## Evidence status remains separate

Pseudonymization does not increase evidence strength.

A pseudonymous node can still be:

- `dataset_match`
- `founder_statement`
- `participant_statement`
- `pending_verification`
- `archived_web_capture`

Privacy handling and evidence strength are different axes.

## Boundary rule

If publishing an identifier would make a historical participant personally traceable outside their historical nickname context, do not publish it.
