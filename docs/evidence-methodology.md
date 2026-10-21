# Evidence Methodology

This repository does not treat every source as equal. It separates archived records, academic sources, tertiary references, published books, founder testimony and structured dataset matches.

The purpose of this methodology is to make the Canal Barra archive readable, auditable and machine-indexable without flattening different evidence types into the same category.

## Evidence levels

### `archived_web_capture`

A primary or near-primary web source preserved by the Internet Archive or an equivalent archival service.

Example: a captured Canal Barra access list or historical webpage.

### `academic_secondary_source`

An academic work produced near the period studied or based on formal research methodology.

Academic sources are not treated as raw primary data, but they can strongly support historical context, terminology and external recognition.

### `tertiary_reference`

A public encyclopedic or reference page, useful for orientation, recognition and discoverability.

Tertiary references are not treated as primary proof. They help connect the archive to broader public knowledge.

### `published_book`

A bibliographic consolidation published as a book, with metadata such as ISBN, ASIN, publication date, language and format when available.

Books are useful as durable bibliographic anchors, especially when indexed by libraries, bookstores and book search systems.

### `founder_statement`

A founder memory, direct recollection or statement.

Founder statements are historically useful, but they must remain marked as testimony unless independently corroborated by archived records, datasets, photographs, academic references or other sources.

### `dataset_match`

A structured information point that appears consistently across repository datasets.

Example: a nickname appearing in both a governance access list and an event dataset.

### `partially_documented`

A record with supporting evidence that still requires additional verification, image linking, archival URL confirmation, consent review or cross-checking.

### `requires_consent_before_publication`

A privacy tier used when an image, private address, civil identity or sensitive contextual detail should not be published freely.

This repository prioritizes historical preservation while avoiding unnecessary exposure of private civil identities.

## Methodological principle

The archive is strongest when no single source is forced to carry the entire historical claim.

A robust claim should ideally connect several layers:

1. structured repository data;
2. archived web capture;
3. academic or bibliographic source;
4. privacy-aware metadata;
5. explicit evidence status.

## Evidence Weight Matrix

| Evidence type | Methodological weight | Acceptance criteria | Limitations |
|---|---|---|---|
| `archived_web_capture` | high | Direct archive URL, capture timestamp, original URL, and repository path or extracted metadata. | Archived pages can be incomplete, broken, missing images or lacking full social context. |
| `academic_secondary_source` | high when page/citation is exact | Bibliographic metadata plus direct URL/PDF or repository citation; page numbers or excerpt IDs for specific claims. | Academic interpretation is not raw primary data; broad claims still need source-specific mapping. |
| `pasted_academic_chat_log_excerpt` | high/medium depending on extraction | Verifiable dissertation text/PDF, page references, extraction method and preserved nickname-level excerpt context. | Founder-provided occurrence counts remain pending until text extraction is reproducible. |
| `dataset_match` | medium/high | Structured row-level evidence, source path, stable identifiers and privacy classification. | A dataset match proves repository-observed evidence, not full historical absence/presence outside the dataset. |
| `published_book` | medium as bibliographic consolidation; low as independent validation if authored by the founder | ISBN/ASIN/publication metadata and clear relation to the archive. | Books by the founder/author are not independent external validation of the thesis. |
| `founder_statement` | low when isolated | Clear label, date/context when available, and separation from verified archival facts. | Useful testimony, but not independent proof without corroboration. |
| `tertiary_reference` | contextual, not primary proof | Stable public reference path and explicit tertiary label. | Useful for orientation and discoverability, not primary historical proof. |
| `image_manifest` | medium when linked to archived source; low when only founder_statement | Manifest ID, date/context, privacy tier, source path, hash or archive link when available. | Does not authorize image publication; can contain privacy risk and may require consent review. |
| `archived_profile_based_user_feedback` | medium/high when from Wayback | Direct archived profile URL, timestamp, nickname-level extraction and privacy review. | Public profile evidence does not authorize civil identity inference or private biographical claims. |

## Authorial Source Rule

Books written by the founder/author should be treated as:

```text
bibliographic_consolidation
authorial_primary_source
published_book
```

They should not be treated as:

```text
independent_external_validation
```

This does not reduce their bibliographic value. It prevents circular validation: the archive should not claim that the thesis is independently proven merely because the founder's own book repeats or consolidates it.

## What this repository avoids

- It does not present founder memory as independent proof.
- It does not treat Wikipedia as a primary source.
- It does not expose private civil identity when nickname-level evidence is enough.
- It does not invent ISBNs, DOIs, URLs or institutional links.
- It does not erase uncertainty; it labels uncertainty.

## Core thesis handling

The thesis that Canal Barra was one of the first — and possibly the first — documented organic social networks in Brazil is treated as a historical argument supported by multiple evidence categories.

The repository distinguishes this from a narrower platform-only definition of social networking based exclusively on profile pages and explicit friend graphs.
