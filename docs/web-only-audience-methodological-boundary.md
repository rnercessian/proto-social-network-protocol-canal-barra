# Web-Only Audience: Methodological Boundary

This note defines how the repository treats web-only or web-first Canal Barra participation evidence.

The strongest evidence currently available is not a complete census of users who never entered IRC. The strongest evidence is technical and architectural: CanalBarra.com preserved web-registered nicknames that are incompatible with conservative IRC nickname syntax, such as nicknames containing `@`, `#`, `*`, spaces, decorative arrows or extended characters. These records indicate that the website operated a social identity namespace that was not reducible to the strict IRC/NickServ nickname namespace.

This distinction supports the IRC-Web-Presence model. The #barra channel provided synchronous presence, while CanalBarra.com provided a persistent web layer where identity, visibility, voting, profile display, neighborhood metadata and internal messaging could operate independently of live IRC participation.

The category should be used cautiously:

- It is valid to claim that CanalBarra.com had an autonomous web identity layer.
- It is valid to claim that some web-visible identities could not exist as exact IRC nicknames.
- It is valid to claim that the site supported web-first or web-mediated participation modes.
- It is not valid to claim, from nickname incompatibility alone, that a civil person never used IRC under another nickname.
- It is not valid to estimate the number of web-only users without aggregate data.
- It is not valid to use access counters or hosting pressure as precise membership counts.

Access counters, high-access messages and hosting-limit exhaustion may support the existence of substantial web attention. They should be treated as traffic and visibility indicators, not as direct user-count metrics.

## Evidence Gap

The repository still lacks a complete aggregate dataset linking all CanalBarra.com profile records to IRC-validity checks, vote counts, messaging metadata and confirmed IRC participation status. Until such a dataset exists, the web-only category should be treated as an evidence-backed architectural category, not as a quantified demographic class.

## Current Supporting Files

- `scripts/audit_web_only_nicknames.py`
- `data/processed/web-only-nickname-audit.json`
- `schema/web-only-audience.schema.jsonld`

## Recommended Wording

Use:

> CanalBarra.com supported a web identity namespace that was not technically reducible to IRC nickname syntax, indicating a web-first or web-mediated participation layer within the Canal Barra ecosystem.

Avoid:

> These users never used IRC.

Avoid:

> The number of web-only users was X.

unless independently verified by aggregate evidence.
