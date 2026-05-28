# UFF 2004 PDF Sources

This directory stores local PDF source files used by the UFF 2004 nickname occurrence counter.

The files in this directory are not treated as new interpretive evidence by themselves. They are local copies of public dissertation-derived extracts used for reproducible counting, page review and audit.

## Expected Files

Place the following PDF files here:

```text
data/uff-2004/sources/dossie-canal-barra-monografia-uff-2004-curto.pdf
data/uff-2004/sources/dossie-canal-barra-monografia-uff-2004-anexo-2-logs.pdf
```

## Public Source URLs

```text
short_dossier:
https://canalbarra.com/documents/dossie-canal-barra-monografia-uff-2004-curto.pdf

anexo_2_logs:
https://canalbarra.com/documents/dossie-canal-barra-monografia-uff-2004-anexo-2-logs.pdf
```

## Source Inventory

The machine-readable inventory is:

```text
data/uff-2004/pdf-sources.csv
```

Each PDF source should have:

```text
source_id
source_file
source_url
sha256
status
notes
```

The Anexo 2 public extract currently has this recorded SHA-256:

```text
69065faabc1a07d7ae003e31efd01b79ae183ba5b627f1d856c7f363754b038b
```

If a local file produces a different SHA-256, do not silently overwrite the value. Investigate whether the PDF was regenerated, renamed, recompressed or replaced.

## What These Files Are For

These PDFs are used by:

```text
scripts/count_uff_pdf_nicknames.py
```

The script searches the editable nickname list in:

```text
data/uff-2004/nickname-search-targets.csv
```

and produces:

```text
data/uff-2004/nickname-occurrence-audit.csv
data/uff-2004/nickname-occurrence-summary.csv
```

## Current Search Targets

The initial nickname targets are:

```text
VaNZaN
BM_
Biano-
```

`Biano-` includes the trailing hyphen because that is the exact target currently being audited.

## Important Methodological Limits

The short dossier does not include the full chat logs.

The Anexo 2 file contains the public chat-log extraction beginning at complete dissertation PDF page 217.

The reported totals are currently treated as:

```text
reported_total_pending_line_by_line_audit
```

The machine output must be treated as:

```text
machine_count_pending_human_review_and_deduplication
```

PDF text extraction can miss, duplicate or distort text. The final audited count must be reviewed manually before being treated as validated.

## Do Not Add Here

Do not add:

- unrelated Canal Barra PDFs;
- private logs;
- private messages;
- civil identity documents;
- unconsented personal data;
- raw files containing private hostmasks or private contact data.

This directory is only for public UFF 2004 dissertation-derived PDF extracts used in the occurrence audit.
