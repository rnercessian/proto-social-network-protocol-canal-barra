# Nickname Geographic Signals

## Purpose

This folder is reserved for datasets that extract geographic signals from historical Canal Barra nicknames.

The goal is to measure how often the 2002 cadastro list encoded Rio de Janeiro geography inside nicknames, such as Barra, Recreio, Jacarepaguá, Copacabana, Ipanema, Leblon, Tijuca, Méier and other areas.

## Important Boundary

A geographic token inside a nickname is not proof of residence.

Correct interpretation:

```text
nickname_geographic_signal_only
```

Incorrect interpretation:

```text
confirmed_home_address
confirmed_residence
civil_identity_location
```

## Why This Matters

Geographic nicknames help document that Canal Barra was not an abstract chat room. It carried territorial identity.

Examples of useful signals:

```text
Daniel_Recreio -> Recreio dos Bandeirantes signal
[Aviator-RJ-Barra] -> Barra da Tijuca + Rio de Janeiro signal
*_SaRaDo_Do_MeIeR_* -> Méier signal
```

These are cultural and territorial signals, not private-address data.

## Recommended Dataset

Expected file:

```text
data/processed/geography/nickname-geographic-signals-2002.csv
```

Recommended columns:

```text
record_id
snapshot_date
source_capture_date
segment
display_nickname
raw_line
matched_signal
normalized_place
place_type
confidence
inference_scope
residence_claim
notes
```

## Preliminary Extraction Summary

A preliminary extraction from the 1336-row 2002 cadastro dataset produced approximately:

```text
353 geographic signal rows
162 Rio/RJ-level signals
97 Barra da Tijuca signals
33 Recreio dos Bandeirantes signals
13 Jacarepaguá signals
10 Copacabana signals
8 Méier signals
6 Tijuca signals
5 Leblon signals
5 Ilha-area signals
4 Ipanema signals
```

This summary should be regenerated from the final script before being treated as stable.

## Privacy Rule

Do not infer or publish civil location data from nicknames.

The safe claim is:

```text
The nickname list contains explicit geographic self-presentation signals.
```

The unsafe claim is:

```text
These users lived in those neighborhoods.
```

## Core Sentence

**Geographic nicknames are evidence of territorial identity and social self-presentation inside the Canal Barra ecosystem, not evidence of private residence.**
