# Operator Turnover: 1999 to 2002

## Purpose

This document analyzes the historical rotation of Canal Barra operator and access-level identities between:

- the ChanServ access list used in the operators meeting of 1999-06-23;
- the CanalBarra.com cadastro snapshot from 2002-11-28.

The goal is to show that Canal Barra had a living and changing governance structure, not a static list of names.

## Source 1: Operators Meeting — 1999-06-23

The 1999 source is a photographed meeting record from a Wednesday, 1999-06-23, described by the founder as an operators meeting held at the founder BarMan's house.

The photographed record contains ChanServ access-level information.

According to the founder's note:

- access level `5` = operator;
- access level `10` = master operator.

The public dataset preserves only:

- `display_nickname`;
- `access_level`;
- meeting date;
- source identifier;
- transcription status;
- comparison with the 2002 snapshot.

Private fields visible or implied in the original record are not preserved in the public dataset.

Dataset path:

```text
data/raw/1999-06-23/access-list-1999-06-23.csv
```

## Source 2: Cadastro Snapshot — 2002-11-28

The 2002 source is the CanalBarra.com cadastro/user-list snapshot from 2002-11-28, the day of the Canal Barra 5th anniversary party at Ilha dos Pescadores.

The uploaded Wayback text shows the headline `1336 Cadastros!!!`.

The extracted batch summary is:

| Segment | Rows extracted |
|---|---:|
| Men | 950 |
| Women | 386 |
| Total | 1336 |

Summary path:

```text
data/raw/2002-11-28/NICKNAMES-2002-11-28-SUMMARY.md
```

## Important Methodological Point

The 2002 cadastro list is a snapshot.

It is not a complete census of every participant, operator or access-level identity across the entire history of Canal Barra.

Therefore, the absence of a 1999 operator nickname in the 2002 snapshot should not be treated as an error. It may indicate turnover, migration, inactivity, nickname change, community split or reduced participation.

## Observed Continuity

Some 1999 access-list identities appear again in the 2002 snapshot, either as exact matches or possible variants.

Examples:

| 1999 display_nickname | 1999 access level | 2002 status | 2002 possible display_nickname |
|---|---:|---|---|
| barMan | 10 | found | BarMan |
| negaum | 10 | found | NEGAUM |
| Lucas-Rio | 10 | found | Lucas_Rio |
| AphroditeRJ | 5 | found | AphroditeRJ |
| Natasha | 5 | found | Natasha |
| KUAT_RJ | 1 | found | KUAT_RJ |
| Lena-Barra | 5 | found | Lena-Barra |
| Lisa-Barra | 5 | found | Lisa-Barra |

This continuity supports the argument that Canal Barra had persistent identity across years.

## Observed Turnover

Some 1999 access-list identities were not observed in the 2002 cadastro snapshot.

Examples:

| 1999 display_nickname | 1999 access level | 2002 status | Historical interpretation |
|---|---:|---|---|
| Daiane-de-Ipanema | 3 | not found | Older access-list identity absent from 2002 snapshot |
| JU-RJ | 5 | not found | Older operator absent from 2002 snapshot |
| ClarinhaM / ClaraM | 5 | not found | Older operator/access-list identity absent from 2002 snapshot |
| WaterHand | 10 | not found | Master operator absent from 2002 snapshot |
| pilar | 10 | not found | Master operator absent from 2002 snapshot |
| CELY | 5 | not found | Operator/access-list identity absent from 2002 snapshot |
| Indomada | 5 | not found | Operator/access-list identity absent from 2002 snapshot |
| _ANGRA | 5 | not found | Operator/access-list identity absent from 2002 snapshot |

These absences are historically meaningful. They document social and administrative rotation.

## Why This Matters

A static directory does not show social life.

Turnover shows social life.

The comparison between 1999 and 2002 demonstrates that Canal Barra had:

- operator cycles;
- access-level changes;
- persistent identities;
- disappearing identities;
- replacement and rotation;
- active governance over time.

This is direct evidence of a living community structure.

## Link to the Main Thesis

The main thesis of this repository is that Canal Barra was one of the first — and possibly the first — documented organic social networks in Brazil, based on real socialization, persistent identity, reputation, physical meetings, community, status, collective memory and social circulation through IRC/BRASnet since 1996.

The 1999-to-2002 turnover analysis supports that thesis by showing that the channel had durable yet changing governance.

## Core Sentence

**The absence of older operator nicknames in the 2002 snapshot is not a weakness. It is evidence that Canal Barra was a living network with historical rotation.**
