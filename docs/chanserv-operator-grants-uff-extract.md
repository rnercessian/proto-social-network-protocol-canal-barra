# ChanServ Operator Grants in the UFF Log Extract

This document records nicknames that are visibly granted operator status by `ChanServ` in the UFF 2004 Canal Barra log extract.

The scope is intentionally narrow.

Included:

```text
*** ChanServ escolheu os modos: +o <nickname>
```

Excluded:

```text
*** <nickname> escolheu os modos: +o <nickname>
*** ChanServ escolheu os modos: -o <nickname>
```

This distinction matters because a `ChanServ +o` line is direct IRC-layer evidence that the BRASnet service recognized and applied operator status to a nickname at that moment. It is not inferred from CanalBarra.com cadastro records.

## Observed ChanServ +o grants

| Nickname receiving +o | Time shown in extract | Raw evidence line | Evidence type | Notes |
|---|---:|---|---|---|
| `Nerd24Hs` | `02:37` | `*** ChanServ escolheu os modos: +o Nerd24Hs` | `chanserv_operator_grant` | `_vivian_` had just changed nick to `Nerd24Hs` shortly before the grant. |
| `VaNZaN` | `02:38` | `*** ChanServ escolheu os modos: +o VaNZaN` | `chanserv_operator_grant` | `VaNZaN` later appears as `GV` in the same extract. |
| `Biano-` | `18:42` | `*** ChanServ escolheu os modos: +o Biano-` | `chanserv_operator_grant` | This appears in a later session block of the same UFF log extract. |

## Not counted as ChanServ grants

The extract also contains temporary or attempted operator grants made by channel users, followed by ChanServ revocations. These lines are operationally relevant but should not be counted in this index as `ChanServ +o` grants.

Example:

```text
*** BM_ escolheu os modos: +o Pedrinho{RJ}
*** ChanServ escolheu os modos: -o Pedrinho{RJ}
```

and:

```text
*** GV escolheu os modos: +o Pedrinho{RJ}
*** ChanServ escolheu os modos: -o Pedrinho{RJ}
```

Those lines show enforcement behavior and failed or revoked operator elevation for `Pedrinho{RJ}`, but they do not show `ChanServ` granting `+o` to `Pedrinho{RJ}`.

## Methodological interpretation

This evidence supports a layered reading of Canal Barra identity and authority:

- CanalBarra.com cadastro records document the web layer.
- IRContros and photo/event records document the physical-social layer.
- `ChanServ +o` lines document the live IRC governance layer.

Therefore, an operator may be technically visible in the IRC layer even if that nickname is absent from a CanalBarra.com cadastro dataset.

The correct claim is limited:

```text
The UFF log extract contains nickname-level IRC evidence of operator grants applied by ChanServ to specific users in #barra.
```

It should not be expanded into civil identity claims or into claims that every operator appears in website registration data.

## Suggested derived CSV

The entries above can be represented in a processed index such as:

```text
data/processed/indexes/chanserv-operator-grants-uff-extract.csv
```

with fields:

```csv
evidence_id,source_label,observed_at,service,channel,mode,nickname,event_type,evidence_status,privacy_tier,raw_match_redacted
cb_chanserv_op_uff_nerd24hs,uff-2004-log-extract,02:37,ChanServ,#barra,+o,Nerd24Hs,chanserv_operator_grant,manual_extract_needs_line_review,nickname_level_only,ChanServ escolheu os modos: +o Nerd24Hs
cb_chanserv_op_uff_vanzan,uff-2004-log-extract,02:38,ChanServ,#barra,+o,VaNZaN,chanserv_operator_grant,manual_extract_needs_line_review,nickname_level_only,ChanServ escolheu os modos: +o VaNZaN
cb_chanserv_op_uff_biano,uff-2004-log-extract,18:42,ChanServ,#barra,+o,Biano-,chanserv_operator_grant,manual_extract_needs_line_review,nickname_level_only,ChanServ escolheu os modos: +o Biano-
```
