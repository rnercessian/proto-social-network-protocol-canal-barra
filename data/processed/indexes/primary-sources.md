# Primary Sources Registry

## Purpose

This document lists the primary source groups currently used by the repository.

The goal is to make the historical argument auditable: a researcher should be able to move from a claim to a dated source, dataset, screenshot, archive capture or metadata file.

## Source Policy

Primary sources are separated from interpretation.

A source may prove that a page, event, rule, list or credit existed. It does not automatically prove every broader interpretation attached to it.

## Wayback / Archived Website Captures

### 2001-03-03 — `canalbarra.com/banda/` (festival announcement preserved after the event)

- **Archive:** https://web.archive.org/web/20010303094733/http://www.canalbarra.com/banda/
- **Capture timestamp:** 20010303094733 (3 March 2001, not the event date).
- **Historical dates discussed:** 15 and 29 October (year 2000 explicitly supplied by founder; both Sundays).
- **Source status:** screenshot-inspected Wayback replay; screenshot SHA-256 `e4b49c3f4201f114db2fcfa94ee3fdc79dfca0b159c91205fed26853482eae50`. HTML not separately extracted.
- **Page observations:** Festival de Bandas do Clube Carioca, Rua Jardim Botânico 650, invitation to support the band; 8 original songs listed; captioned photos name BarMan, Mad and Arrudabatera; financial/email/phone details excluded from public transcription.
- **Limits:** promotion/thanks are page evidence; ~200 crowd and elimination from CD competition are founder recollections; playing the announced 8 songs and the full audience composition are not independently verified.
- **Records:** [two separate musical IRContros](../../evidence/events/CLUBE-CARIOCA-MUSICAL-IRCONTROS-2000.md), [chronological index](../../docs/DOCUMENTED-IRCONTROS-CHRONOLOGY.md), [event CSV](../../data/raw/ircontros/clube-carioca-banda-canal-barra-festival-2000.csv).

### 2001-04-05 — Canal Barra homepage / social calendar

Source context:

```text
Original URL: http://canalbarra.com/
Capture date: 2001-04-05
Wayback timestamp from screenshot metadata: 20010405063516
Repository metadata: data/media-metadata/homepage-2001-04-05-social-calendar.csv
```

Evidence value:

```text
homepage_visual_evidence
webchat entry
cadastro link
passeio information
#Barra topic area
NIGHT weekly programming
VIP list via PVT to DrNando
sponsor/ad area
access counter
```

Interpretation boundary:

```text
This supports the claim that Canal Barra had website-mediated social programming and online-to-offline nightlife circulation by 2001.
```

### 2003-01-30 — Canal Barra homepage / event archive

Source context:

```text
Original URL: http://www.canalbarra.com/
Capture date: 2003-01-30
Wayback timestamp from screenshot metadata: 20030130024059
Repository metadata: data/media-metadata/homepage-2003-01-30-event-archive.csv
```

Evidence value:

```text
homepage_visual_evidence
event-photo links from 2002
29/11 Rosas Niver Negaum
15/9 Reunião dos Op
3/10 Casanova Quinta
best-cadastro voting
recent cadastros
total cadastro count
```

Interpretation boundary:

```text
This supports the claim that the homepage worked as an event archive and not only as a temporary chat-entry page.
```

## Internal / Founder-Held Primary Materials

Some primary materials are founder-held and not yet public in raw form because they may contain personal data, identifiable faces, private fields, signatures, payment details or copyrighted material.

These materials should be represented by redacted metadata whenever possible.

Current examples:

```text
1999-06-23 ChanServ access list / operator meeting photo
2001 Rosa dos Ventos event captions
2002 Canal Barra rules page
2002 operator page / disabled profile evidence
2002 fifth-anniversary party evidence
2002/2003 homepage screenshots
ABRAMUS / ECAD music-work metadata
ECAD cinema-rights documentation
```

## Missing or Unstable Archive Captures

If a previously visible Wayback capture becomes unavailable, the repository should not pretend the capture is still directly accessible.

The correct status is:

```text
previously_observed_capture
current_availability_unverified_or_unavailable
local_screenshot_or_metadata_exists
requires_recovery_or_alternate_source
```

This is especially important for early 2000 captures that may have disappeared from visible Wayback navigation or may no longer render correctly.

## Preservation Rule

For every important external source, preserve at least one of the following:

```text
archive URL
screenshot filename
capture date
original URL
local metadata file
SHA-256 hash when available
redacted PDF or screenshot when legally safe
notes explaining what the source proves and does not prove
```

## What Primary Sources Should Not Contain Publicly

Do not publish:

```text
civil identities unnecessarily
private addresses
telephone numbers
CPF or tax identifiers
full payment documents
private email threads
full hostmasks or IP addresses
identifiable user photos without permission or clear archival/legal basis
copyrighted video or music excerpts beyond legally safe metadata
```

## Core Sentence

**The Canal Barra argument should be auditable through dated primary sources: archived pages, screenshots, captions, rules, access lists, event metadata, registrations and redacted institutional records.**
