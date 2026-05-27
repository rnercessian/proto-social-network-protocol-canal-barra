# Canal Barra Cadastros — 2002 Source Summary

## Purpose

This file records the source URLs and consolidation status for the Canal Barra cadastro nickname lists recovered from Wayback captures.

## Source URLs

Male cadastro list:

```text
https://web.archive.org/web/20021217125338/http://www.canalbarra.com/cadastros/userview2.cfm?sexo=m
```

Female cadastro list:

```text
https://web.archive.org/web/20021217125338/http://www.canalbarra.com/cadastros/userview2.cfm?sexo=f
```

## Current Consolidation Count

Founder-provided extracted lists currently contain:

```text
male records: 950
female records: 386
total records: 1336
```

## Date Handling

The repository currently keeps the dataset under:

```text
data/raw/2002-11-28/
```

because the list was historically associated by the founder with the Canal Barra 5th anniversary period.

The Wayback capture URL itself is from:

```text
2002-12-17
```

So downstream datasets should preserve both ideas when possible:

```text
snapshot_context_date: 2002-11-28
source_capture_date: 2002-12-17
```

## Parsing Rules

Leading IRC prefixes are not part of the nickname.

Examples:

```text
@ BarMan  -> prefix @, display_nickname BarMan
+ |Ryan|  -> prefix +, display_nickname |Ryan|
+ @ Advogata_rj -> prefixes + @, display_nickname Advogata_rj
```

## Privacy Classification

All rows should be classified as:

```text
historical_public_nickname
civil_identity_linked=false
sensitive_data_included=false
```

## Status

The previous CSV in this folder had only a few placeholder rows.

It must be replaced by the consolidated 1336-row dataset generated from the male and female source lists.

## Core Sentence

**The 2002 cadastro lists are primary evidence of large-scale persistent nickname registration on the Canal Barra website, with 1336 recovered records across male and female cadastro pages.**
