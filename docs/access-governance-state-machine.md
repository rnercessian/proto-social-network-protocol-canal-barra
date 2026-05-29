# Access Governance State Machine

This document models Canal Barra access provisioning as a historical state machine.

It does not claim that every transition was automated or formally documented from the beginning. It provides a technical model for how a participant could move from ordinary presence to trusted operational authority across the Canal Barra stack.

## State machine

```mermaid
stateDiagram-v2
    [*] --> UnknownVisitor

    UnknownVisitor: Visitor / guest / unknown nick
    UnknownVisitor --> LiveIrcParticipant: joins #barra on BRASnet

    LiveIrcParticipant: Live IRC presence
    LiveIrcParticipant --> WebRegisteredParticipant: creates or appears in CanalBarra.com cadastro
    LiveIrcParticipant --> RecognizedRegular: repeated IRC presence

    WebRegisteredParticipant: Web persistence / cadastro layer
    WebRegisteredParticipant --> RecognizedRegular: nickname recognized across IRC and website

    RecognizedRegular: Recognized nickname-level identity
    RecognizedRegular --> InPersonRecognized: appears in IRContro / luau / party
    RecognizedRegular --> TrustedParticipant: trusted by existing Masters / Founder

    InPersonRecognized: In-person identity anchoring
    InPersonRecognized --> TrustedParticipant: offline reputation reinforces trust

    TrustedParticipant: Trusted participant / candidate signal
    TrustedParticipant --> OperatorCandidate: considered for OP status

    OperatorCandidate: Candidate for operator-level execution
    OperatorCandidate --> OperatorProvisioned: Master or Founder grants access-list privilege
    OperatorCandidate --> NoAccessChange: insufficient trust / no vacancy / no consensus

    OperatorProvisioned: Operator-level execution
    OperatorProvisioned --> ActiveOperator: receives runtime moderation authority
    ActiveOperator --> AccessListReview: turnover / performance / continuity review

    AccessListReview: Access-list realignment or OP meeting
    AccessListReview --> ActiveOperator: retained
    AccessListReview --> DeProvisioned: access removed or reduced
    AccessListReview --> MasterDelegationCandidate: exceptional trust / higher delegation considered

    MasterDelegationCandidate: Candidate for master-level delegation
    MasterDelegationCandidate --> MasterProvisioned: Founder-level authority grants Master access
    MasterProvisioned --> MasterLevelDelegation: can provision/evaluate Operators

    DeProvisioned: Access revoked or reduced
    NoAccessChange: No privileged access change

    MasterLevelDelegation --> AccessListReview
```

## Interpretation

The model separates four layers:

1. Live IRC presence.
2. Web-backed persistence through CanalBarra.com.
3. In-person identity and reputation anchoring through IRContros and gatherings.
4. Tiered access governance through Founder, Masters, Operators and access-list realignment.

## Default synchronization assumption

Unless evidence documents a specific bot or automated bridge, the connection between these layers should be treated as human-mediated state synchronization.

That means reputation and eligibility signals were recognized by people across IRC presence, web cadastro records and in-person gatherings, while technical access-list changes were executed through the available IRC service mechanisms.

## Key transitions

| Transition | Meaning |
| --- | --- |
| `UnknownVisitor -> LiveIrcParticipant` | A user appears in the live IRC channel. |
| `LiveIrcParticipant -> WebRegisteredParticipant` | The nickname becomes associated with web persistence / cadastro evidence. |
| `RecognizedRegular -> InPersonRecognized` | Nickname identity is anchored through an in-person event. |
| `TrustedParticipant -> OperatorCandidate` | Social trust becomes a candidate signal for privileged access. |
| `OperatorCandidate -> OperatorProvisioned` | Master or Founder grants operator-level access. |
| `ActiveOperator -> AccessListReview` | Operational status becomes subject to turnover or realignment. |
| `MasterDelegationCandidate -> MasterProvisioned` | Founder-level authority grants Master access. |

## Evidence boundary

This diagram is a technical abstraction. Individual historical records must still carry their own evidence status, date, source and privacy tier.
