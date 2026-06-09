# ChanServ Operator Grants in the UFF Log Extract

This document records nicknames that are visibly granted operator status by `ChanServ` in the UFF 2004 Canal Barra log extract.

The scope is intentionally narrow.

Included:

```text
*** ChanServ escolheu os modos: +o <nickname>
```

Excluded from the grant list, but methodologically relevant:

```text
*** <nickname> escolheu os modos: +o <nickname>
*** ChanServ escolheu os modos: -o <nickname>
```

This distinction matters because a `ChanServ +o` line is direct IRC-layer evidence that the BRASnet service recognized and applied operator status to a nickname at that moment. It is not inferred from CanalBarra.com cadastro records.

A `ChanServ -o` line after a user attempts to give operator status should be interpreted separately. In the Canal Barra context, it is evidence of channel-protection enforcement: ChanServ removed operator status from a nickname that was not authorized to keep it according to the registered channel's access configuration.

The exact BRASnet option name should not be asserted here unless a BRASnet help record or services configuration record is found. In IRC services documentation, this behavior corresponds to the general ChanServ model for registered/protected channels: channel ownership and operator rights are maintained through founder designation, access lists or xOP lists, and ChanServ can automatically remove operator status from users who are not authorized to hold it.

Founder interpretation: this enforcement behavior reflects security settings left in place by BarMan to protect #barra from unauthorized operator elevation, takeover or misuse. The log lines therefore matter not only as revocations, but as evidence that the channel's access-list protection was still active in the live IRC layer.

## Observed ChanServ +o grants

| Nickname receiving +o | Time shown in extract | Raw evidence line | Evidence type | Notes |
|---|---:|---|---|---|
| `Nerd24Hs` | `02:37` | `*** ChanServ escolheu os modos: +o Nerd24Hs` | `chanserv_operator_grant` | `_vivian_` had just changed nick to `Nerd24Hs` shortly before the grant. |
| `VaNZaN` | `02:38` | `*** ChanServ escolheu os modos: +o VaNZaN` | `chanserv_operator_grant` | `VaNZaN` later appears as `GV` in the same extract. |
| `Biano-` | `18:42` | `*** ChanServ escolheu os modos: +o Biano-` | `chanserv_operator_grant` | This appears in a later session block of the same UFF log extract. |

## Access-list enforcement events

The extract also contains temporary or attempted operator grants made by channel users, followed by ChanServ removals.

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

These lines should not be counted as `ChanServ +o` grants to `Pedrinho{RJ}`. They show a different mechanism: an attempted operator elevation followed by automatic ChanServ enforcement. In practical terms, the service allowed the channel to reject operator status for someone not authorized in the access configuration.

## Methodological interpretation

This evidence supports a layered reading of Canal Barra identity and authority:

- CanalBarra.com cadastro records document the web layer.
- IRContros and photo/event records document the physical-social layer.
- `ChanServ +o` lines document the live IRC governance layer.
- `ChanServ -o` lines after unauthorized `+o` attempts document live channel-protection enforcement.

Therefore, an operator may be technically visible in the IRC layer even if that nickname is absent from a CanalBarra.com cadastro dataset. Conversely, a nickname may appear in a user-issued `+o` attempt without being recognized by ChanServ as authorized to keep operator status.

The correct claims are limited:

```text
The UFF log extract contains nickname-level IRC evidence of operator grants applied by ChanServ to specific users in #barra.
```

and:

```text
The UFF log extract also contains nickname-level IRC evidence of ChanServ removing operator status from a nickname after an attempted operator elevation, consistent with registered-channel access-list enforcement.
```

These claims should not be expanded into civil identity claims or into claims that every operator appears in website registration data.

## Suggested derived CSV

The `+o` entries above can be represented in a processed index such as:

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

The `-o` enforcement entries should be indexed separately, for example:

```text
data/processed/indexes/chanserv-access-enforcement-uff-extract.csv
```

with an event type such as:

```text
chanserv_operator_removal_after_unauthorized_grant
```
