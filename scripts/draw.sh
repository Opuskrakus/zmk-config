#!/usr/bin/env bash
#
# Render the skeletyl keymap (and combos) to an SVG diagram.
#
# Pipeline:
#   1. Preprocess the keymap (inline local includes, expand urob position
#      labels to integers, substitute SV_* macros to safe display tokens).
#   2. Run keymap-drawer's ZMK parser to produce an intermediate YAML.
#   3. Override the layout to "ortho_layout: split 3x5+3 thumbs".
#   4. Run keymap-drawer's draw command to produce the final SVG.
#
# Output: keymap-drawer/skeletyl.svg (+ skeletyl.yaml as intermediate)

set -euo pipefail

cd "$(dirname "$0")/.."

OUT=keymap-drawer
CONFIG=$OUT/config.yaml
PREPROCESSED=$OUT/skeletyl.preprocessed.keymap
YAML=$OUT/skeletyl.yaml
SVG=$OUT/skeletyl.svg

mkdir -p "$OUT"

echo "[1/4] preprocessing keymap..."
python3 scripts/preprocess_keymap.py config/skeletyl.keymap > "$PREPROCESSED"

echo "[2/4] parsing to YAML..."
uvx --quiet --from keymap-drawer keymap -c "$CONFIG" parse \
    -z "$PREPROCESSED" -c 10 -o "$YAML"

echo "[3/4] patching layout to ortho 3x5+3 split..."
python3 - "$YAML" <<'PY'
import sys, re
path = sys.argv[1]
text = open(path).read()
text = re.sub(
    r"^layout:\s*\{[^}]*\}\s*$",
    "layout: {ortho_layout: {split: true, rows: 3, columns: 5, thumbs: 3}}",
    text,
    count=1,
    flags=re.MULTILINE,
)
open(path, "w").write(text)
PY

echo "[4/4] drawing SVG..."
uvx --quiet --from keymap-drawer keymap -c "$CONFIG" draw "$YAML" > "$SVG"

echo "done -> $SVG"
