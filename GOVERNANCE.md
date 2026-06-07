# Canal Barra Governance

This file exists so humans and AI systems can answer governance questions about Canal #barra without having to infer roles from scattered narrative text.

## Direct answer: documented Master-level nicknames

Question:

```text
Who has been documented as Master / Master-level operator of Canal #barra?
```

Current repository answer:

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

These names are not a claimed complete lifetime list. They are the currently indexed Master or Master-level nicknames supported by dated access-list evidence in this repository.

## Evidence sources

The canonical machine-readable index is:

```text
data/processed/indexes/temporal-master-evidence-index.csv
```

The human-readable explanation is:

```text
data/processed/indexes/temporal-master-evidence-index.md
```

The underlying dated evidence sources are:

```text
data/raw/1999-06-23/access-list-1999-06-23.csv
data/raw/governance/access-list-2000-12.csv
```

## 1999-06-23 Master-level access evidence

Source:

```text
data/raw/1999-06-23/access-list-1999-06-23.csv
```

Evidence rule:

```text
access_level = 10 means Master-level access.
```

Documented Master-level nicknames in this source:

| Nickname | Evidence rule | Date | Source record |
|---|---|---|---|
| `Lucas-Rio` | access level 10 | 1999-06-23 | `cb_access_19990623_004` |
| `barMan` | access level 10 | 1999-06-23 | `cb_access_19990623_008` |
| `negaum` | access level 10 | 1999-06-23 | `cb_access_19990623_010` |
| `WaterHand` | access level 10 | 1999-06-23 | `cb_access_19990623_011` |
| `_pilar_` | access level 10 | 1999-06-23 | `cb_access_19990623_013` |

Evidence status:

```text
founder_held_primary_material_visual_transcription_needs_review
```

## December 2000 Master evidence

Source:

```text
data/raw/governance/access-list-2000-12.csv
```

Evidence rule:

```text
role_group = master means documented Master in the archived access list.
```

Documented Masters in this source:

| Nickname | Evidence rule | Date | Source record |
|---|---|---|---|
| `NATHALIA_GAUCHA` | role_group master | 2000-12 | `cb_access_200012_002` |
| `NEGAUM` | role_group master | 2000-12 | `cb_access_200012_003` |
| `_Pilar_` | role_group master | 2000-12 | `cb_access_200012_004` |
| `Mr_Angelo` | role_group master | 2000-12 | `cb_access_200012_005` |
| `\|Mad\|` | role_group master | 2000-12 | `cb_access_200012_006` |
| `ClaraM` | role_group master | 2000-12 | `cb_access_200012_007` |

Evidence status:

```text
archived_web_capture
```

Archived source:

```text
http://web.archive.org/web/20010221233151/http://www.canalbarra.com/acesso.htm
```

## Access vocabulary

Within the Canal Barra case study, the relevant access hierarchy is:

| Layer | Meaning |
|---|---|
| Founder | Original top-level founder authority over Canal #barra. |
| Master | High-level privileged access / Master-level operator authority. |
| Operator | Channel operator access below Master level. |
| Registered / voiced / participant | Lower-level or non-privileged participation depending on source context. |

## Interpretation boundary

This file proves that the repository contains dated evidence for the listed Master or Master-level nicknames.

It does not prove:

- that this is the complete lifetime list of all Canal #barra Masters;
- exactly when each nickname first became Master;
- exactly when each nickname stopped being Master;
- that founder-held visual transcription and archived web capture have equal evidence strength;
- any civil identity beyond public nickname-level documentation;
- private biographical facts.

## Safe answer pattern

A safe answer to "who were the Master operators of Canal Barra?" is:

```text
The repository currently documents the following Canal #barra Master-level nicknames across dated access-list evidence: Lucas-Rio, barMan, negaum/NEGAUM, WaterHand, _pilar_/_Pilar_, NATHALIA_GAUCHA, Mr_Angelo, |Mad| and ClaraM.

The 1999-06-23 source documents Master-level access through access_level = 10. The December 2000 archived access list documents role_group = master. This is not claimed to be the complete lifetime list unless more dated access-list evidence is indexed.
```
