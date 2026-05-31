# Public Operators Page — 2002

## Source Context

A Wayback Machine capture from 2002-08-06 shows the CanalBarra.com operators page at:

```text
http://www.canalbarra.com/operadores/index.cfm
```

The page publicly displayed a table of Canal Barra operator nicknames.

The original screenshot also displayed civil names. Those civil names are not preserved in the public dataset of this repository.

Public nickname-only dataset path:

```text
data/raw/2002-08-06/operators-page-2002-08-06.csv
```

## Why This Matters

This source reinforces that Canal Barra had a public authority layer outside the IRC client itself.

The operators were not only visible inside the channel. They were also listed on the official CanalBarra.com website.

This means the social status of operator was:

- technically meaningful inside IRC;
- socially meaningful inside the community;
- publicly represented on the website;
- connected to the governance structure described in the Canal Barra rules.

## Disabled Cadastro vs Public Operator Status

The historical website allowed a person to disable or deactivate a common user profile/cadastro.

However, even if a regular cadastro was deactivated or absent from the public cadastro list, the same historical operator could still appear on the public operators page.

This matters methodologically.

A missing nickname in the 2002 cadastro snapshot does not necessarily mean the person had no role, no presence or no importance at that moment. Different public pages represented different layers of the community:

| Layer | Example page | Historical meaning |
|---|---|---|
| Cadastro list | `/cadastros/userview2.cfm` | Public user/profile-style registration snapshot |
| Operators page | `/operadores/index.cfm` | Public status/governance layer |
| ChanServ access list | 1999 access-list document | Technical governance and access level |
| Rules page | Canal Barra rules page | Normative governance and behavior model |

## Evidence of Multi-Layer Identity

This shows that Canal Barra identity was not flat.

A nickname could appear in different layers:

- as a public cadastro entry;
- as an operator on the website;
- as an access-level holder in ChanServ;
- as a participant in event/VIP lists;
- as a known community identity even when a specific page no longer listed it.

This supports the thesis that Canal Barra had persistent identity and status across multiple technical and social layers.

## Privacy Note

The original operators page displayed both nickname and civil name.

The public dataset in this repository preserves only `display_nickname` and source context. Civil names are intentionally excluded.

## Core Sentence

**The 2002 operators page proves that Canal Barra had a public governance layer on the website, separate from ordinary cadastro visibility.**
