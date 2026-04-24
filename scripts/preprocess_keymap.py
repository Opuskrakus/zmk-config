#!/usr/bin/env python3
"""
Pre-process a ZMK keymap for keymap-drawer.

keymap-drawer's ZMK parser does not run the C preprocessor; it only follows
local `#include "file.dtsi"` directives textually. This script:

  1. Inlines local `#include "..."` directives (angle-bracket system
     includes are left as-is -- keymap-drawer ignores them), but skips
     `keys_sv.h` because its macros expand to raw HID_USAGE_* expressions
     that keymap-drawer cannot render.
  2. Substitutes urob-style position labels (LT0..RH2 from
     <zmk-helpers/key-labels/36.h>) with their integer values inside
     `key-positions = <...>` and `hold-trigger-key-positions = <...>`.
  3. Rewrites `SV_*` Swedish keycode macros to a form keymap-drawer
     can display (either the literal symbol or an underscore-prefixed
     keycode).
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

# From urob/zmk-helpers/include/zmk-helpers/key-labels/36.h
POS: dict[str, int] = {
    "LT0": 4,  "LT1": 3,  "LT2": 2,  "LT3": 1,  "LT4": 0,
    "RT0": 5,  "RT1": 6,  "RT2": 7,  "RT3": 8,  "RT4": 9,
    "LM0": 14, "LM1": 13, "LM2": 12, "LM3": 11, "LM4": 10,
    "RM0": 15, "RM1": 16, "RM2": 17, "RM3": 18, "RM4": 19,
    "LB0": 24, "LB1": 23, "LB2": 22, "LB3": 21, "LB4": 20,
    "RB0": 25, "RB1": 26, "RB2": 27, "RB3": 28, "RB4": 29,
    "LH0": 32, "LH1": 31, "LH2": 30,
    "RH0": 33, "RH1": 34, "RH2": 35,
}

# Friendly display names for Swedish (SV_*) macros. Only the *target* symbol
# matters for visualization -- the actual HID usage comes from the firmware.
SV_MAP: dict[str, str] = {
    "SV_EXCL": "!", "SV_EXCLAMATION": "!",
    "SV_DQT": "DT_DQT", "SV_DOUBLE_QUOTES": "DT_DQT",
    "SV_HASH": "#", "SV_POUND": "#",
    "SV_DLLR": "$", "SV_DOLLAR": "$",
    "SV_PRCNT": "%", "SV_PERCENT": "%",
    "SV_AMPS": "DT_AMPS", "SV_AMPERSAND": "DT_AMPS",
    "SV_SQT": "'", "SV_SINGLE_QUOTE": "'", "SV_APOSTROPHE": "'", "SV_APOS": "'",
    "SV_LPAR": "(", "SV_LEFT_PARENTHESIS": "(",
    "SV_RPAR": ")", "SV_RIGHT_PARENTHESIS": ")",
    "SV_STAR": "*", "SV_ASTERISK": "*", "SV_ASTRK": "*",
    "SV_PLUS": "+",
    "SV_COMMA": ",",
    "SV_MINUS": "-",
    "SV_DOT": ".", "SV_PERIOD": ".",
    "SV_FSLH": "/", "SV_SLASH": "/",
    "SV_COLON": ":",
    "SV_SEMI": "DT_SEMI", "SV_SEMICOLON": "DT_SEMI",
    # '<' and '>' break devicetree cell parsing; use safe tokens and let
    # raw_binding_map in keymap-drawer config map these to their symbols.
    "SV_LT": "DT_LT", "SV_LESS_THAN": "DT_LT",
    "SV_EQUAL": "=",
    "SV_GT": "DT_GT", "SV_GREATER_THAN": "DT_GT",
    "SV_QMARK": "?", "SV_QUESTION": "?",
    "SV_AT": "@", "SV_AT_SIGN": "@",
    "SV_LBKT": "[", "SV_LEFT_BRACKET": "[",
    "SV_BSLH": "DT_BSLH", "SV_BACKSLASH": "DT_BSLH",
    "SV_RBKT": "]", "SV_RIGHT_BRACKET": "]",
    "SV_CARET": "^",
    "SV_UNDER": "DT_UNDER", "SV_UNDERSCORE": "DT_UNDER",
    "SV_GRAVE": "`",
    "SV_LBRC": "DT_LBRC", "SV_LEFT_BRACE": "DT_LBRC",
    "SV_PIPE": "|",
    "SV_RBRC": "DT_RBRC", "SV_RIGHT_BRACE": "DT_RBRC",
    "SV_TILDE": "~",
    "SV_A_RING": "å",
    "SV_A_UMLAUT": "ä",
    "SV_O_UMLAUT": "ö",
    "SV_EURO": "€",
    "SV_POUND_SIGN": "£",
    "SV_CURRENCY_SIGN": "¤", "SV_CURREN": "¤",
    "SV_SECTION": "§", "SV_SECT": "§",
    "SV_UMLAUT": "¨",
    "SV_ACUTE": "´",
    "SV_MU": "µ", "SV_MICRO": "µ",
    "SV_ONE_HALF": "½", "SV_FRAC_1_2": "½",
    "SV_SPACE": "SPACE",
    "SV_N0": "0", "SV_N1": "1", "SV_N2": "2", "SV_N3": "3", "SV_N4": "4",
    "SV_N5": "5", "SV_N6": "6", "SV_N7": "7", "SV_N8": "8", "SV_N9": "9",
}

# Single-letter SV_A..SV_Z
for _c in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
    SV_MAP[f"SV_{_c}"] = _c

LOCAL_INCLUDE_RE = re.compile(r'^\s*#include\s+"([^"]+)"\s*$', re.MULTILINE)
FIELD_RE = re.compile(
    r"((?:key-positions|hold-trigger-key-positions)\s*=\s*<)([^>]+)(>)"
)
SV_TOKEN_RE = re.compile(r"\bSV_[A-Z0-9_]+\b")

# Skip includes whose macros expand to raw HID expressions keymap-drawer
# cannot render; we handle them via SV_MAP instead.
SKIP_INCLUDES = {"keys_sv.h"}


def inline_includes(path: Path, seen: set[Path] | None = None) -> str:
    seen = seen or set()
    if path in seen:
        return ""
    seen.add(path)
    text = path.read_text()

    def replace(match: re.Match) -> str:
        name = match.group(1)
        if name in SKIP_INCLUDES:
            return f"/* --- skipped: {name} (handled by SV_MAP) --- */"
        target = (path.parent / name).resolve()
        if not target.exists():
            return match.group(0)
        return f"/* --- inlined: {name} --- */\n{inline_includes(target, seen)}"

    return LOCAL_INCLUDE_RE.sub(replace, text)


def substitute_positions(text: str) -> str:
    def expand(m: re.Match) -> str:
        inner = m.group(2)
        for label, num in POS.items():
            inner = re.sub(rf"\b{label}\b", str(num), inner)
        return f"{m.group(1)}{inner}{m.group(3)}"

    return FIELD_RE.sub(expand, text)


def substitute_sv_tokens(text: str) -> str:
    def replace(m: re.Match) -> str:
        token = m.group(0)
        return SV_MAP.get(token, token)

    return SV_TOKEN_RE.sub(replace, text)


def main() -> int:
    if len(sys.argv) != 2:
        print("usage: preprocess_keymap.py <keymap_path>", file=sys.stderr)
        return 2
    src = Path(sys.argv[1]).resolve()
    merged = inline_includes(src)
    merged = substitute_positions(merged)
    merged = substitute_sv_tokens(merged)
    sys.stdout.write(merged)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
