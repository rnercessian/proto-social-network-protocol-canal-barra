# Participation Coverage Analysis

## Purpose

This document defines how to compare nickname-level evidence across Canal Barra datasets.

## Data Layers

The repository can compare three layers:

```text
2002 cadastro records
access-list records
IRContro caption records
```

## IRC Nickname Syntax

Participation analysis should preserve the observed nickname text while also marking whether the value is syntactically compatible with an IRC nickname.

An IRC-compatible nickname may use letters, numbers after the first character, hyphen after the first character, and IRC special characters such as `[`, `]`, `\`, `` ` ``, `_`, `^`, `{`, `|` and `}`.

Values containing spaces, `@`, `#`, `/`, `.`, accented letters or decorative symbols should not be treated as literal IRC nicknames without additional source context.

This distinction matters because some website cadastro entries or captions may represent display labels, ornamental aliases, copied page text or extraction artifacts rather than nicknames that could have been used directly in IRC.

## Useful Filters

```text
registered nickname with IRContro caption presence
access-list nickname with IRContro caption presence
access-list nickname without current IRContro caption match
registered nickname with access-list match
registered nickname with access-list match and IRContro caption match
```

## Evidence Boundary

A missing match means only:

```text
no match in the current repository datasets
```

It does not mean:

```text
no historical attendance
```

## Why It Matters

The comparison helps measure the relationship between formal channel roles and visible social participation in archived event evidence.

## Core Sentence

**Participation coverage analysis should compare formal access records with documented event-caption presence while keeping all conclusions at nickname and dataset level.**
