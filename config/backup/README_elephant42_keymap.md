# Optimized ZMK Keymap for Elephant42 (Swedish Developer Layout)

This keymap is designed for the Elephant42 keyboard specifically optimized for developers who use a Swedish system layout. It incorporates ergonomic features, frequently used programming symbols, and Swedish-specific characters.

## Key Features

### 1. Home Row Mods (GACS Order)
- Uses the "home row" for modifiers allowing you to access Shift, Ctrl, Alt, and GUI without moving your fingers from the home position
- Left side: GACS (GUI/Alt/Ctrl/Shift)
- Right side: SCAG (Shift/Ctrl/Alt/GUI)

### 2. Layer Structure
- **BASE (0)**: Main typing layer with Swedish letters ö, ä on right pinky positions
- **NAV (1)**: Navigation and editing controls (cursor movement, copy/paste, etc)
- **SYM (2)**: Programming symbols (braces, operators, etc)
- **NUM (3)**: Numbers and mathematical operations
- **FUN (4)**: Function keys and system controls
- **ADJUST (5)**: Reset, bootloader, and advanced Bluetooth controls (accessed by holding NAV+SYM)

### 3. Smart Combos
- **Brackets**: Easy access to paired brackets that automatically place cursor between them
  - AS → () with cursor in between
  - AW → [] with cursor in between
  - WS → {} with cursor in between
- **Programming Symbols**: Quick access to commonly used symbols
  - ER → =
  - FK → :
  - CV → ;
  - OP → /
  - JK → \
  - ./ → |
- **Special Characters**: Swedish-specific characters as combos (in addition to dedicated keys)
  - A+J → ä
  - R+U → ö
  - A+Y → å

### 4. Programming Macros
- Code-friendly arrow operators:
  - `->` (arrow right)
  - `<-` (arrow left)
  - `=>` (fat arrow)

### 5. Thumb Key Optimization
- Space/Shift on strongest thumb positions
- Layer access on other thumb keys
- Return and backspace easily accessible

## Key Positions Reference

This keymap uses key position definitions to enable combos. The positions are defined as:

```
LT0 LT1 LT2 LT3 LT4 LT5 | RT0 RT1 RT2 RT3 RT4 RT5
LM0 LM1 LM2 LM3 LM4 LM5 | RM0 RM1 RM2 RM3 RM4 RM5
    LB0 LB1 LB2 LB3 LB4 | RB0 RB1 RB2 RB3 RB4
        LH0 LH1 LH2 LH3 | RH0 RH1 RH2 RH3
```

## Installation

1. Copy `elephant42_optimized.keymap` to your ZMK config directory
2. Ensure you have the `keys_sv.h` file in the same directory
3. Build and flash your firmware

## Customization Tips

- Adjust tapping-term timing if the home row mods trigger too easily or not easily enough
- Modify combos to fit your specific programming needs
- Add language-specific snippets as macros for your primary programming languages 