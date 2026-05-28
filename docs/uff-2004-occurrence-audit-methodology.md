# UFF 2004 Occurrence Audit Methodology

## Purpose

This document defines how the repository counts nickname occurrences in the public dissertation-derived extract set for the 2004 UFF dissertation:

```text
IRC e ICQ: uma análise sócio-comunicativa das plataformas de comunicação on-line
Flaviana Rangel Pesset Gonzaga
Universidade Federal Fluminense
2004
```

## Public Extract Set

The current public extract set contains two files:

```text
short_dossier
https://canalbarra.com/documents/dossie-canal-barra-monografia-uff-2004-curto.pdf

anexo_2_logs
https://canalbarra.com/documents/dossie-canal-barra-monografia-uff-2004-anexo-2-logs.pdf
```

The short dossier contains contextual dissertation material and the Canal Barra-related section.

The Anexo 2 dossier contains the public chat-log extract beginning at complete dissertation PDF page 217.

## Editable Search Targets

The list of nicknames to search is intentionally editable here:

```text
data/uff-2004/nickname-search-targets.csv
```

Initial enabled targets:

```text
VaNZaN
BM_
Biano-
```

`Biano-` includes the trailing hyphen because that is the exact target currently being searched.

## Source Inventory

The configured PDF sources are listed here:

```text
data/uff-2004/pdf-sources.csv
```

The PDFs should be stored locally under:

```text
data/uff-2004/sources/
```

Expected file names:

```text
data/uff-2004/sources/dossie-canal-barra-monografia-uff-2004-curto.pdf
data/uff-2004/sources/dossie-canal-barra-monografia-uff-2004-anexo-2-logs.pdf
```

## Counter Script

The counter script is:

```text
scripts/count_uff_pdf_nicknames.py
```

Run:

```bash
python3 -m pip install pypdf
python3 scripts/count_uff_pdf_nicknames.py
```

It writes:

```text
data/uff-2004/nickname-occurrence-audit.csv
data/uff-2004/nickname-occurrence-summary.csv
```

## Status of Counts

The current reported totals:

```text
VaNZaN = 119
BM_ = 108
Biano- = 80
```

remain provisional until the script output is reviewed by a human.

Correct status:

```text
reported_total_pending_line_by_line_audit
```

After the script runs, machine counts must still be treated as:

```text
machine_count_pending_human_review_and_deduplication
```

## Why Machine Counts Are Not Final

PDF extraction can miss or distort text.

Nicknames may appear:

- in contextual prose;
- in pasted IRC logs;
- inside repeated excerpts;
- inside formatting artifacts;
- as part of commands or scripts;
- with OCR or extraction noise.

Therefore, the final audited count must separate:

- source file;
- PDF page;
- printed page when visible;
- excerpt ID;
- exact line text;
- duplicate group;
- whether the line is duplicate;
- whether an operator action is visible.

## Operator Action Detection

The script marks possible operator-action lines when a matched line contains technical markers such as:

```text
mode
+o
-o
+b
-b
ban
unban
desban
kick
op
deop
```

This is only a machine hint.

Human review is required before treating any nickname as an operator based on a specific excerpt.

## Core Rule

Do not treat reported totals or machine counts as final evidence until the repository contains a reviewed occurrence table with page and line references.
