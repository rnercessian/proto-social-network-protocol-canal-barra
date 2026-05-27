# Missing Files and Next Data Batches

## Purpose

This document tracks promised or expected repository files that are not yet complete.

It exists to prevent the repository from looking finished when key evidence batches are still pending.

## Critical Missing / Incomplete Items

### 1. VIP Lists

Status:

```text
missing_dataset
primary_source_context_exists
needs_extraction
```

Expected path:

```text
data/raw/vip-lists/
```

Why it matters:

VIP lists are important because they show that Canal Barra did not only host conversation. It mediated access to real-world nightlife, entrance lists, promoters and social status.

Evidence already mentioned in repository context:

```text
2001 homepage screenshot showing VIP list instruction via PVT to DrNando
```

Needed files:

```text
data/raw/vip-lists/README.md
data/raw/vip-lists/vip-list-sources.csv
data/raw/vip-lists/vip-list-events.csv
```

### 2. Wayback Primary Source Links in README

Status:

```text
partially_documented
needs_readme_section
```

Needed action:

Add a **Primary Sources** section to `README.md`, linking the main Wayback captures and repository metadata files.

Relevant captures already tracked:

```text
2001-04-05 homepage social calendar / VIP list context
2003-01-30 homepage event archive context
2002-12-17 male cadastro page
2002-12-17 female cadastro page
```

### 3. Full Primary Source Registry Expansion

Status:

```text
started
needs_expansion
```

Existing file:

```text
docs/PRIMARY-SOURCES.md
```

Needs:

```text
operator meeting / ChanServ source block
2002 rules page source block
2002 operator page source block
2002 fifth anniversary evidence block
2004 UFF monograph source block
```

### 4. IRContro Dataset Files

Status:

```text
schema_exists
dataset_pending
```

Existing schema:

```text
schema/ircontro-event.schema.json
```

Needed files:

```text
data/raw/ircontros/ircontros-index.csv
data/raw/ircontros/rosa-dos-ventos-2001-02-21.csv
data/raw/ircontros/homepage-event-archive-2002.csv
```

### 5. Governance / Operator Dataset Files

Status:

```text
partially_documented
dataset_pending
```

Needed files:

```text
data/raw/governance/operator-meeting-1999-06-23.csv
data/raw/governance/chanserv-access-levels-1999-06-23.csv
data/raw/governance/operator-meeting-2002-09.csv
```

Notes:

The 2002 September operator meeting is known from screenshot evidence, but the meeting minutes are not preserved yet.

### 6. Canal Barra Rules Dataset

Status:

```text
source_text_provided
dataset_pending
```

Needed files:

```text
data/raw/rules/canal-barra-rules-2002-11.csv
docs/CANAL-BARRA-RULES-2002.md
```

### 7. 2002 Cadastro Dataset

Status:

```text
completed
```

Completed file:

```text
data/raw/2002-11-28/nicknames-2002-11-28-cadastros.csv
```

Current recovered count:

```text
1336 records
950 male records
386 female records
```

## Core Rule

Do not present missing datasets as completed evidence.

Use these labels:

```text
completed
partially_documented
dataset_pending
source_known_extraction_pending
missing_dataset
```

## Core Sentence

**The repository is strongest when it clearly separates completed datasets from promised evidence batches still awaiting extraction, especially VIP lists, IRContros, governance records and primary-source links.**
