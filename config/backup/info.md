What I changed (urob-style port, Swedish keycodes, QWERTY base)
Pinned your build to urob’s stack
Updated config/west.yml to match urob’s v0.3 pin + added his module remotes/projects (zmk-helpers, zmk-tri-state, zmk-auto-layer, zmk-leader-key, zmk-unicode, zmk-adaptive-key).
Updated .github/workflows/build.yml to use build-user-config.yml@v0.3.
Adopted urob’s project/keymap structure
Added split-out config files:
config/combos.dtsi (urob-style combos, adapted to SV_* from keys_sv.h)
config/leader.dtsi (leader sequences using zmk-leader-key + zmk-unicode)
config/mouse.dtsi (mouse emulation tuning + aliases)
config/skeletyl.conf (enables combos/leader/adaptive/unicode/pointing)
Refactored your actual keymap
Replaced your monolithic config/skeletyl.keymap with a urob-inspired layout:
Timeless HRMs (balanced + hold-trigger-on-release + cross-hand triggers)
Combos instead of a symbol layer
Tri-state swapper (Alt+Tab)
Smart num (num-word + sticky num via tap-dance)
Magic shift (tap = shift-repeat/sticky-shift, shifted tap = caps-word, hold = shift)
Files to look at
Main entry: config/skeletyl.keymap
Combos: config/combos.dtsi
Leader: config/leader.dtsi
Mouse: config/mouse.dtsi
Kconfig: config/skeletyl.conf
Manifest: config/west.yml
Important notes / next steps
Pointing enabled (CONFIG_ZMK_POINTING=y): after flashing, you may need to remove + re-pair BLE so hosts notice the HID descriptor change.
Unicode on macOS: the keymap defaults to UC_MODE_MACOS. Make sure macOS has Unicode Hex Input enabled (as described in urob’s zmk-unicode docs).
You still have untracked config/test.keymap / config/test2.keymap in the repo; I left them untouched.
If you tell me your preferred thumb key ordering (which of the 6 thumb positions you want as Space/Enter/Backspace), I can quickly remap the urob features to match your muscle memory without changing the rest.