#!/usr/bin/env python3
"""
Audit web-registered Canal Barra nicknames against conservative IRC nickname rules.

Purpose:
- Detect nicknames that are valid as web/social identities but incompatible with
  strict IRC nickname syntax.
- Support the methodological claim that CanalBarra.com had an autonomous
  web identity namespace, not merely a mirror of #barra IRC nicknames.

Important:
- This does NOT prove that the person never used IRC.
- It only shows that the exact web nickname could not be used as a strict IRC nick.
"""

from __future__ import annotations

import json
import re
from dataclasses import asdict, dataclass
from typing import Iterable, List


# Conservative RFC-style IRC nickname rule:
# first char: letter or allowed special
# next chars: letters, digits, allowed specials, hyphen
#
# RFC-style allowed specials include:
# [ ] \\ ` _ ^ { | }
#
# This intentionally rejects spaces, @, #, *, >, <, =, dots,
# accented/non-ASCII chars and decorative symbols.
IRC_NICK_RE = re.compile(r"^[A-Za-z\[\]\\`_^{|}][A-Za-z0-9\[\]\\`_^{|}-]*$")


@dataclass(frozen=True)
class NickAudit:
    nickname: str
    strict_irc_valid: bool
    invalid_reasons: List[str]
    interpretation: str


def audit_nickname(nick: str) -> NickAudit:
    reasons: List[str] = []

    if not nick:
        reasons.append("empty_nickname")

    if " " in nick:
        reasons.append("contains_space")

    if any(ord(ch) > 127 for ch in nick):
        reasons.append("contains_non_ascii_or_extended_character")

    forbidden_chars = sorted({ch for ch in nick if ch in "@#*<>=."})
    if forbidden_chars:
        reasons.append(f"contains_forbidden_or_nonstandard_chars:{''.join(forbidden_chars)}")

    if nick and not re.match(r"^[A-Za-z\[\]\\`_^{|}]", nick[0]):
        reasons.append("invalid_first_character_for_strict_irc")

    if not IRC_NICK_RE.match(nick):
        reasons.append("does_not_match_strict_irc_nickname_pattern")

    valid = len(reasons) == 0

    interpretation = (
        "exact_nickname_is_compatible_with_strict_irc"
        if valid
        else "exact_web_nickname_is_incompatible_with_strict_irc_and_supports_web_identity_namespace_claim"
    )

    return NickAudit(
        nickname=nick,
        strict_irc_valid=valid,
        invalid_reasons=reasons,
        interpretation=interpretation,
    )


def audit_many(nicknames: Iterable[str]) -> dict:
    results = [asdict(audit_nickname(nick)) for nick in nicknames]
    return {
        "id": "web-only-nickname-irc-compatibility-audit-v1",
        "type": "technical_audit_result",
        "method": "strict_irc_nickname_syntax_check",
        "methodological_note": (
            "Invalidity under strict IRC nickname rules does not prove the person never used IRC. "
            "It proves only that the exact web-registered nickname belongs to a web/social identity "
            "namespace not reducible to IRC nickname syntax."
        ),
        "founder_context": (
            "The founder states that some users with web-registered nicknames incompatible with IRC/NickServ "
            "rules still communicated through the CanalBarra.com internal messaging service. This is treated as "
            "curator/founder context pending independent source indexing."
        ),
        "results": results,
    }


def main() -> None:
    nicknames = [
        "#*GOHN.BARRA#*",
        "*>ALOHA<*",
        "=====->ŠÑÎÞË® - KßÇÅ",
        ">>>>--> HULK <--<<<<",
        "s@r@do",
        "***B!@***",
    ]

    print(json.dumps(audit_many(nicknames), ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
