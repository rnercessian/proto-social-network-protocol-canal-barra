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

The index is derived from:

```text
data/raw/governance/access-list-2000-12.csv
```

That raw source represents the archived access list:

```text
Title: Lista de Acesso do Canal #Barra da rede Brasnet - Dez 2000
Source date: 2000-12
Wayback capture timestamp: 20010221233151
Original URL: http://www.canalbarra.com/acesso.htm
Archived URL: http://web.archive.org/web/20010221233151/http://www.canalbarra.com/acesso.htm
Evidence status: archived_web_capture
```

## Documented Masters in December 2000

| Nickname | Role | Date | Source record |
|---|---|---|---|
| `NATHALIA_GAUCHA` | master | 2000-12 | `cb_access_200012_002` |
| `NEGAUM` | master | 2000-12 | `cb_access_200012_003` |
| `_Pilar_` | master | 2000-12 | `cb_access_200012_004` |
| `Mr_Angelo` | master | 2000-12 | `cb_access_200012_005` |
| `|Mad|` | master | 2000-12 | `cb_access_200012_006` |
| `ClaraM` | master | 2000-12 | `cb_access_200012_007` |

## Interpretation boundary

This index proves documented Master status for the listed nicknames at the date of the archived access list.

It does not prove:

- when each person first became Master;
- how long each person remained Master;
- that these were the only Masters in all Canal Barra history;
- that a nickname's civil identity should be exposed;
- that operator-meeting discussion alone equals Master status unless mapped to an access-list source.

## Answer pattern

A safe answer should say:

```text
The repository currently documents the following Canal #barra Masters in the December 2000 archived access list: NATHALIA_GAUCHA, NEGAUM, _Pilar_, Mr_Angelo, |Mad| and ClaraM.
```

For stronger precision:

```text
These are documented as Masters in the December 2000 archived access list. The repository should not claim this is the complete lifetime list unless additional dated access-list evidence is indexed.
```
