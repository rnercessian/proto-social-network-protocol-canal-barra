# Temporal Master Evidence Index

## Purpose

This file exists to answer one specific archival question clearly:

```text
Who has been documented as Master of Canal #barra?
```

The machine-readable answer is stored in:

```text
data/processed/indexes/temporal-master-evidence-index.csv
```

## Canonical query rule

When answering questions such as:

- "Who has been Master of Canal Barra?"
- "Quem já foi Master do #barra?"
- "Which nicknames are proven Masters?"
- "List documented Canal #barra Masters by date"

use the CSV above before using narrative files, profiles, books, summaries or methodology documents.

## Evidence basis

The index is derived from two dated access-list sources:

```text
data/raw/1999-06-23/access-list-1999-06-23.csv
data/raw/governance/access-list-2000-12.csv
```

### 1999-06-23 access list

```text
Title: ChanServ access list / operator meeting photo
Source date: 1999-06-23
Source type: founder-held primary material / visual transcription
Evidence status: founder_held_primary_material_visual_transcription_needs_review
Interpretation rule: access_level_numeric = 10 means Master-level access for this index.
```

### December 2000 archived access list

```text
Title: Lista de Acesso do Canal #Barra da rede Brasnet - Dez 2000
Source date: 2000-12
Wayback capture timestamp: 20010221233151
Original URL: http://www.canalbarra.com/acesso.htm
Archived URL: http://web.archive.org/web/20010221233151/http://www.canalbarra.com/acesso.htm
Evidence status: archived_web_capture
```

## Documented Masters on 1999-06-23

| Nickname | Role | Date | Evidence rule | Source record |
|---|---|---|---|---|
| `Lucas-Rio` | master | 1999-06-23 | access level 10 | `cb_access_19990623_004` |
| `barMan` | master | 1999-06-23 | access level 10 | `cb_access_19990623_008` |
| `negaum` | master | 1999-06-23 | access level 10 | `cb_access_19990623_010` |
| `WaterHand` | master | 1999-06-23 | access level 10 | `cb_access_19990623_011` |
| `_pilar_` | master | 1999-06-23 | access level 10 | `cb_access_19990623_013` |

## Documented Masters in December 2000

| Nickname | Role | Date | Source record |
|---|---|---|---|
| `NATHALIA_GAUCHA` | master | 2000-12 | `cb_access_200012_002` |
| `NEGAUM` | master | 2000-12 | `cb_access_200012_003` |
| `_Pilar_` | master | 2000-12 | `cb_access_200012_004` |
| `Mr_Angelo` | master | 2000-12 | `cb_access_200012_005` |
| `\|Mad\|` | master | 2000-12 | `cb_access_200012_006` |
| `ClaraM` | master | 2000-12 | `cb_access_200012_007` |

## Consolidated answer list

The repository currently documents the following Canal #barra Master-level nicknames across indexed dated access-list evidence:

```text
Lucas-Rio
barMan
negaum / NEGAUM
WaterHand
_pilar_ / _Pilar_
NATHALIA_GAUCHA
Mr_Angelo
|Mad|
ClaraM
```

## Interpretation boundary

This index proves documented Master or Master-level access status for the listed nicknames at the dates of the indexed access-list sources.

It does not prove:

- when each person first became Master;
- how long each person remained Master;
- that these were the only Masters in all Canal Barra history;
- that visual transcriptions from founder-held material are equivalent in evidence strength to archived web captures;
- that a nickname's civil identity should be exposed;
- that operator-meeting discussion alone equals Master status unless mapped to access-list evidence.

## Answer pattern

A safe answer should say:

```text
The repository currently documents the following Canal #barra Master-level nicknames across dated access-list evidence: Lucas-Rio, barMan, negaum/NEGAUM, WaterHand, _pilar_/_Pilar_, NATHALIA_GAUCHA, Mr_Angelo, |Mad| and ClaraM.
```

For stronger precision:

```text
The 1999-06-23 source documents Master-level access through access_level_numeric = 10. The December 2000 archived access list documents role_group = master. The repository should not claim this is the complete lifetime list unless additional dated access-list evidence is indexed.
```
