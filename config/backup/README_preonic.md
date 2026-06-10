# Preonic Rev 3 Swedish Developer Layout

This is a ZMK keymap for the Preonic Rev 3 keyboard with Swedish layout optimized for developers. It includes advanced features like home row mods, layer-tap keys, and programming symbol shortcuts optimized for the Swedish keyboard layout.

## Features

- Optimized for Swedish developers
- Comprehensive programming symbols with Swedish layout compatibility
- Home row mods for ergonomic modifier access
- Smart combos for brackets, arrows, and special characters
- Terminal-specific shortcuts (like Ctrl+Shift+C/V)
- Navigation and editing layer with cursor controls
- Number pad and function key layers
- Bluetooth, media, and system control features

## Layer Access

The keyboard uses 6 layers that are accessed as follows:

1. **BASE Layer (0)**: Default layer when you turn on the keyboard
2. **NAV Layer (1)**: Hold the 4th key on bottom row (tap for TAB)
3. **SYM Layer (2)**: Hold the 8th key on bottom row (tap for RETURN)
4. **NUM Layer (3)**: Hold the 5th key on bottom row (tap for SPACE)
5. **FUN Layer (4)**: Hold the 9th key on bottom row (tap for LEFT arrow)
6. **ADJUST Layer (5)**: Hold both NAV and SYM layer keys simultaneously

## Files

- `config/preonic_rev3.keymap` - The main keymap file
- `config/keys_sv.h` - Swedish key definitions
- `config/preonic_keymap_visual.md` - Visual representation of all layers
- `build.yaml` - Build configuration

## Building and Flashing

### Option 1: GitHub Actions (Recommended)

1. Fork this repository to your GitHub account
2. Push any changes to your fork
3. GitHub Actions will automatically build the firmware
4. Download the `preonic_rev3-zmk.uf2` file from the Actions artifacts
5. Connect your Preonic Rev 3 in bootloader mode (press RESET twice)
6. Copy the .uf2 file to the USB drive that appears

### Option 2: Building Locally

If you prefer to build locally:

1. Install ZMK build dependencies:
   ```
   sudo apt install git cmake ninja-build gperf ccache dfu-util wget python3-pip python3-setuptools python3-tk python3-wheel xz-utils file make gcc gcc-multilib g++-multilib libsdl2-dev libmagic1
   ```

2. Install the Zephyr SDK:
   ```
   pip3 install --user -U west
   west init -l ~/zmk
   cd ~/zmk
   west update
   west zephyr-export
   pip3 install --user -r zephyr/scripts/requirements.txt
   ```

3. Build the firmware:
   ```
   cd ~/zmk
   west build -p -b preonic_rev3 -d build/preonic_rev3
   ```

4. Flash the firmware:
   - Put your keyboard into bootloader mode
   - Copy `build/preonic_rev3/zephyr/zmk.uf2` to the USB drive that appears

## Customization

To customize this keymap:

1. Edit `config/preonic_rev3.keymap` to modify layers, combos, or key bindings
2. Consult `config/preonic_keymap_visual.md` to understand the current layout
3. Refer to the ZMK documentation at [zmk.dev/docs](https://zmk.dev/docs/) for more details

## Swedish Layout Considerations

This keymap adapts to the Swedish keyboard layout by using the keys_sv.h definitions. This ensures that symbols typed on your keyboard will correctly match what's shown on your Swedish-configured computer.

For example:
- Your OS receives the correct scancodes for Swedish characters (å, ä, ö)
- Programming symbols are mapped to match their positions on a Swedish layout
- Arrow syntax (`->`, `<-`, `=>`) generates correctly regardless of your OS language settings 