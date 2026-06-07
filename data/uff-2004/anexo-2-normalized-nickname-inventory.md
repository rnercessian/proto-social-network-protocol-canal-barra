# Anexo 2 Normalized Nickname Inventory

Source: UFF 2004 Anexo 2 public Canal Barra log dossier.

Related source records:

- `evidence/academic-sources/uff-2004-index.md`
- `data/uff-2004/reported-nickname-occurrence-index.md`
- public log dossier: `dossie-canal-barra-monografia-uff-2004-anexo-2-logs.pdf`

## Scope

This file lists nicknames observed in the Anexo 2 Canal Barra public log corpus and collapses obvious same-session nickname variations.

The purpose is not to count occurrences. The purpose is to preserve a normalized nickname inventory for future audit.

## Normalization rule

Nick changes caused by status, joke suffixes, temporary event tags, away markers, or the "chiclete" joke are grouped under a canonical nickname when the log explicitly shows the change or when the variation is visibly mechanical.

Examples:

- `VaNZaN`, `VaNZaN[CHICLETAO]` and the same-session change to `GV` are grouped under `VaNZaN`.
- `fui-embora`, `Biano-` and `Biano[CHICLETEEEEEEEEEEE]` are grouped under `Biano` because the log shows `fui-embora agora é Biano-` and later `Biano- agora é Biano[CHICLETEEEEEEEEEEE]`.
- `cArGa[vB]`, `[vB]cArGa`, `cArGa[y2k]` and `cArGa[BiChO\`RuIm]` are grouped under `cArGa`.
- `Lelo_Jpa`, `Lelo_Jpa_tel` and `Lelo_Jpa_odeia_X9` are grouped under `Lelo_Jpa`.
- `Rindo\`Horrores` is grouped under `ManuzinhaXuperLove` where the log shows `Rindo\`Horrores agora é ManuzinhaXuperLove`.

## Important caveat

This is a normalized inventory, not a validated occurrence count.

The Anexo 2 logs contain IRC control lines, joins, quits, parts, away messages, mode changes, kicks, topic text, color-code noise and music/status-script output. Therefore, final quantitative use still requires a line-by-line machine extraction and human review.

## Normalized nickname list

| Canonical nickname | Observed variants / aliases collapsed | Notes |
|---|---|---|
| `_C_a_R_o_L__CaRpEtA` | `_C_a_R_o_L__CaRpEtA` | Mentioned in live conversation. |
| `_joao_henriques_` | `_joao_henriques_` | Join line. |
| `_Layne_` | `_Layne_` | Join line. |
| `_Rambo_19` | `_Rambo_19`, `Rambo_19` | Visible in dialogue/script formatting. |
| `Agent-86` | `Agent-86` | Join line. |
| `anabiaaaa` | `anabiaaaa` | Message line. |
| `Biano` | `fui-embora`, `Biano-`, `Biano[CHICLETEEEEEEEEEEE]` | Explicit nick-change chain in Anexo 2. |
| `Binha-_-` | `Binha-_-` | Message lines. |
| `BM_` | `BM_` | Topic setter, operator/mode lines, message lines. |
| `Bodyboard_21` | `Bodyboard_21` | Message/status-script line. |
| `BPM_OFF` | `BPM_OFF` | Music/status-script line. |
| `br0d` | `br0d` | Message line. |
| `Bruce_RJ` | `Bruce_RJ` | Quit/join lines. |
| `CaFaJeStE_24_Rj` | `CaFaJeStE_24_Rj` | Music/status-script line. |
| `CaroliNa-27` | `CaroliNa-27` | Lag-test/action line. |
| `cArGa` | `cArGa[BiChO\`RuIm]`, `cArGa[vB]`, `cArGa[y2k]`, `[vB]cArGa` | Mechanical suffix/status variations. |
| `DaNieL_BaRra` | `DaNieL_BaRra` | Message and voice-mode lines. |
| `Dani18-rindoMUITO-sozinha` | `Dani18-rindoMUITO-sozinha` | Message and mode lines. |
| `DDeXTerr` | `DDeXTerr` | Music/status-script line. |
| `DrNando` | `DrNando`, `-DrNando-` | Away/script and mention. |
| `ErV|nHA` | `ErV|nHA` | Mentioned in addressed message. |
| `esprock` | `esprock` | Part line. |
| `Fabio__` | `Fabio__` | Away line. |
| `Garoto_de_programa_-rj-_` | `Garoto_de_programa_-rj-_` | Voice-mode line. |
| `Gatinhu_` | `Gatinhu_` | Join line. |
| `GiZeLLe` | `GiZeLLe`, `GiZeLLe_Ic` | Quit line includes nick and user ident. Canonical kept as visible nick. |
| `guigo_diretoria` | `guigo_diretoria`, `guigOFF_diretoria` | Explicit away/off-style nick change. |
| `guto_barra` | `guto_barra` | Quit line. |
| `LadY_of_hipHop` | `LadY_of_hipHop` | Message/status-script line. |
| `Lelo_Jpa` | `Lelo_Jpa`, `Lelo_Jpa_tel`, `Lelo_Jpa_odeia_X9` | Tel/away/X9 suffix variants grouped. |
| `Lindinha_barra` | `Lindinha_barra` | Quit line. |
| `loirinha____` | `loirinha____` | Join line. |
| `LUA` | `LUA||Xou\`Muito\`Maix\`Eu||`, `Lua||XuPer\`In\`Up||` | Similar LUA-style status nick family; needs later human confirmation. |
| `Mak__Copa` | `Mak__Copa` | Join/message line. |
| `malha` | `malha[out]` | Mode line. |
| `malhado-Rj` | `malhado-Rj` | Join line. |
| `ManuzinhaXuperLove` | `ManuzinhaXuperLove`, `Rindo\`Horrores` | Explicit nick change to ManuzinhaXuperLove. |
| `Mateus_Barra_22` | `Mateus_Barra_22` | Join/message line. |
| `medico-jpa` | `medico-jpa` | Join line. |
| `MErendA-[RJ]` | `MErendA-[RJ]` | Join/part line. |
| `Miagui_RJ` | `Miagui_RJ` | Quit line. |
| `Nerd24Hs` | `_vivian_`, `Nerd24Hs` | Explicit nick change `_vivian_ agora é Nerd24Hs`. |
| `ninabarra-25` | `ninabarra-25` | Join/part line. |
| `Nudistasss` | `Nudistasss` | Join/kick line. |
| `o_mais_feio` | `o_mais_feio` | Part line. |
| `os-olhos` | `os-olhos` | Message line. |
| `P01` | `P01` | Message/part/quit lines. |
| `Pedrinho{RJ}` | `Pedrinho{RJ}` | Message, mode and kick lines. |
| `Pepeia` | `Pepeia` | Message line. |
| `Pit-bull` | `Pit-bull` | Join/message line. |
| `Playboy_barra` | `nukando_a_galera_barra`, `Playboy_barra` | Explicit nick change. |
| `Playmobil_RJ` | `Playmobil_RJ`, `Toulouse_RJ` | Explicit nick change from Playmobil_RJ to Toulouse_RJ; see Toulouse note. |
| `Qu3lzinh4__JPA` | `Qu3lzinh4__JPA`, `Quelzinh4__JPA` | Script/color formatting visually splits the nick; canonical kept as logged. |
| `QuIkSiLvEr_zsul__` | `QuIkSiLvEr_zsul__` | Join line. |
| `RaFa_RoiF` | `RaFa_RoiF` | Quit line. |
| `RaPhAElluS` | `RaPhAElluS` | Message/action lines. |
| `R-eNaTo_O` | `R-eNaTo_O[cHeGaNdO-dO-MaRaCa]` | Status suffix collapsed. |
| `Roooo` | `Roooo` | Message lines. |
| `R-Caruso` | `R-Caruso` | Message line. |
| `R3pTiL3` | `R3pTiL3}}` | Braces treated as decoration/noise unless later confirmed. |
| `Sarada_42-RJ` | `Sarada_42-RJ-Away` | Away suffix collapsed. |
| `SHARK_RIO` | `SHARK_RIO[26_HJ][OFFz]` | Age/date/off suffix collapsed. |
| `SUFOCADOR` | `SUFOCADOR` | Voice-mode line. |
| `SUPERHOMEM-RJ` | `SUPERHOMEM-RJ` | Message and mode lines. |
| `tchetchelo` | `tchetchelo_MuiToCurioSo`, `tchetchelo_Anestesiado` | Explicit nick change. |
| `Thati_-RJ` | `Thati_-RJ`, `thåtï_-®j` | Same stylized nick family; needs later human confirmation. |
| `Thiffany` | `Thiffany` | Message lines. |
| `TO_NERDANDO_AKI` | `TO_NERDANDO_AKI[FLUmeio\`off]` | Status suffix collapsed. |
| `TO-NEM_AI` | `To_Nem_Aii`, `TO-NEM_AI` | Explicit nick change. |
| `Tom_del0nge_182` | `Tom_del0nge_182` | Message/mention lines. |
| `Toulouse_RJ` | `Toulouse_RJ`, `Toulouse_RJ|OFF|` | Off suffix collapsed; also appears after `Playmobil_RJ agora é Toulouse_RJ`. |
| `Tuna_` | `Tuna_` | Join/message/kick lines. |
| `tunazuda` | `tunazuda` | Message line. |
| `VaNZaN` | `VaNZaN`, `VaNZaN[CHICLETAO]`, `GV` | Explicit nick-change chain; `GV` grouped because Anexo 2 shows `VaNZaN agora é GV`. |
| `valente` | `valente` | Message line. |
| `VouSozinhaMesmoPraAxeJurney` | `VouSozinhaMesmoPraAxeJurney` | Quit line. |
| `XEIHZ` | `XEIHZ` | Message/status-script line. |
| `ZoIo_AzUl_SuRf_RoCk` | `ZoIo_AzUl_SuRf_RoCk` | Quit line. |

## System/service names observed but not counted as community nicknames

| Service/system name | Reason excluded |
|---|---|
| `ChanServ` | IRC service, not a participant nickname. |

## Follow-up audit tasks

1. Generate a clean text extraction from the Anexo 2 PDF.
2. Parse all IRC patterns: `<nick>`, `*** Joins: nick`, `*** Quits: nick`, `*** Parts: nick`, `*** nick agora é newnick`, `*** nick escolheu os modos`, `*** nick foi kickado por op`.
3. Remove hostmasks, idents, IP fragments, song titles, URLs and script artifacts.
4. Produce two outputs:
   - raw nickname strings exactly as seen;
   - normalized canonical nickname list with alias mapping.
5. Mark uncertain merges as `needs_human_confirmation` instead of forcing identity collapse.
