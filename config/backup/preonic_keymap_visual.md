# Preonic Rev 3 Keymap Visualization (Swedish Developer Layout)

This document provides a visual representation of each layer in the optimized Swedish developer keymap for the Preonic Rev 3.

## Layout Overview

The Preonic has 60 keys in a 5x12 ortholinear grid:

```
 0  1  2  3  4  5  6  7  8  9 10 11
12 13 14 15 16 17 18 19 20 21 22 23
24 25 26 27 28 29 30 31 32 33 34 35
36 37 38 39 40 41 42 43 44 45 46 47
48 49 50 51 52 53 54 55 56 57 58 59
```

## Layers Visual Representation

### BASE Layer (0)

```
┌─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┐
│  `  │  1  │  2  │  3  │  4  │  5  │  6  │  7  │  8  │  9  │  0  │ BSPC│
├─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┤
│ ESC │  Q  │  W  │  E  │  R  │  T  │  Y  │  U  │  I  │  O  │  P  │ DEL │
├─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┤
│CTLTB│  GA │  AS │  CD │  SF │  G  │  H  │  SJ │  CK │  AL │  GO │  AÄ │
├─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┤
│SHIFT│  Z  │  X  │  C  │  V  │  B  │  N  │  M  │  ,  │  .  │  -  │ RET │
├─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┤
│LCTRL│ LALT│ LGUI│ NAV │ NUM │ SPC │ SPC │ SYM │ FUN │ DOWN│  UP │RIGHT│
└─────┴─────┴─────┴─────┴─────┴─────┴─────┴─────┴─────┴─────┴─────┴─────┘
```

- GA = GUI+A (hold for GUI, tap for A)
- AS = ALT+S (hold for ALT, tap for S)
- CD = CTRL+D (hold for CTRL, tap for D)
- SF = SHIFT+F (hold for SHIFT, tap for F)
- SJ = SHIFT+J (hold for SHIFT, tap for J)
- CK = CTRL+K (hold for CTRL, tap for K)
- AL = ALT+L (hold for ALT, tap for L)
- GO = GUI+Ö (hold for GUI, tap for Ö)
- AÄ = ALT+Ä (hold for ALT, tap for Ä)
- NAV = Hold for NAV layer, tap for TAB
- NUM = Hold for NUM layer, tap for SPACE
- SYM = Hold for SYM layer, tap for RETURN
- FUN = Hold for FUN layer, tap for LEFT arrow
- CTLTB = Hold for CTRL, tap for TAB

### NAV Layer (1) - Navigation and Editing

```
┌─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┐
│ --- │ --- │ --- │ --- │ --- │ --- │ --- │ --- │ --- │ --- │ --- │ --- │
├─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┤
│ --- │PGUP │C-S-C│  UP │C-S-TB│C-TAB│HOME │PGDN │PGUP │ END │ A-D │ DEL │
├─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┤
│ --- │PGDN │LEFT │DOWN │RIGHT│A-TAB│LEFT │DOWN │ UP  │RIGHT│ RET │ --- │
├─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┤
│ --- │ C-Z │ C-X │ C-C │ C-V │ C-Y │C-S-C│C-S-V│C-S-T│A-S-T│C-TAB│ --- │
├─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┤
│ --- │ --- │ --- │ --- │ --- │ SPC │ SPC │ RET │ BSP │ --- │ --- │ --- │
└─────┴─────┴─────┴─────┴─────┴─────┴─────┴─────┴─────┴─────┴─────┴─────┘
```

- C-Z = Control+Z (Undo)
- C-X = Control+X (Cut)
- C-C = Control+C (Copy in GUI apps)
- C-V = Control+V (Paste in GUI apps)
- C-Y = Control+Y (Redo)
- C-S-C = Control+Shift+C (Copy in terminal)
- C-S-V = Control+Shift+V (Paste in terminal)
- C-S-T = Control+Shift+T (New terminal tab)
- C-TAB = Control+Tab (Switch tabs right)
- C-S-TB = Control+Shift+Tab (Switch tabs left)
- A-TAB = Alt+Tab (Switch applications forward)
- A-S-T = Alt+Shift+Tab (Switch applications backward)
- A-D = Alt+D (Address bar in browsers)
- PGUP = Page Up
- PGDN = Page Down
- --- = Transparent (passes through to base layer)

### SYM Layer (2) - Symbols for Programming

```
┌─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┐
│ --- │ --- │ --- │ --- │ --- │ --- │ --- │ --- │ --- │ --- │ --- │ --- │
├─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┤
│ --- │  !  │  @  │  #  │  $  │  %  │  ^  │  &  │  *  │  (  │  )  │ --- │
├─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┤
│ --- │  \  │  |  │  =  │  +  │  -  │  _  │  {  │  }  │  [  │  ]  │ --- │
├─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┤
│ --- │ <-  │ ->  │ =>  │  :  │  ;  │  "  │  '  │  <  │  >  │  ?  │ --- │
├─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┤
│ --- │ --- │ --- │ --- │ --- │ --- │ --- │ --- │ --- │ --- │ --- │ --- │
└─────┴─────┴─────┴─────┴─────┴─────┴─────┴─────┴─────┴─────┴─────┴─────┘
```

- <- = Left arrow macro (types "<-")
- -> = Right arrow macro (types "->") 
- => = Fat arrow macro (types "=>")
- --- = Transparent (passes through to base layer)

### NUM Layer (3) - Numbers and Math Operators

```
┌─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┐
│ --- │ --- │ --- │ --- │ --- │ --- │ --- │ --- │ --- │ --- │ --- │ --- │
├─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┤
│ --- │  1  │  2  │  3  │  4  │  5  │  6  │  7  │  8  │  9  │  0  │ --- │
├─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┤
│ --- │ GUI │ ALT │CTRL │SHIFT│ TAB │  +  │  4  │  5  │  6  │  *  │ --- │
├─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┤
│ --- │ --- │ --- │ --- │ --- │ --- │  -  │  1  │  2  │  3  │  /  │ --- │
├─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┤
│ --- │ --- │ --- │ --- │ --- │ SPC │ SPC │  0  │  .  │ --- │ --- │ --- │
└─────┴─────┴─────┴─────┴─────┴─────┴─────┴─────┴─────┴─────┴─────┴─────┘
```

### FUN Layer (4) - Function Keys and System Controls

```
┌─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┐
│ --- │ --- │ --- │ --- │ --- │ --- │ --- │ --- │ --- │ --- │ --- │ --- │
├─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┤
│ F1  │ F2  │ F3  │ F4  │ F5  │ F6  │ F7  │ F8  │ F9  │ F10 │ F11 │ F12 │
├─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┤
│ --- │ BT1 │ BT2 │ BT3 │ BT4 │ BT5 │MUTE │VOL- │VOL+ │PLAY │NEXT │ --- │
├─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┤
│ --- │BTCLR│OUTG │ --- │ --- │ PWR │CAPS │SLCK │PSCR │PREV │PAUS │ --- │
├─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┤
│ --- │ --- │ --- │ --- │ --- │ --- │ --- │ --- │ --- │ --- │ --- │ --- │
└─────┴─────┴─────┴─────┴─────┴─────┴─────┴─────┴─────┴─────┴─────┴─────┘
```

- BT1-BT5 = Bluetooth profile select
- BTCLR = Bluetooth clear
- OUTG = Output toggle (USB/BT)
- PWR = External power toggle
- MUTE = Volume mute
- VOL- = Volume down
- VOL+ = Volume up
- PLAY = Play/pause
- NEXT = Next track
- PREV = Previous track
- CAPS = Caps lock
- SLCK = Scroll lock
- PSCR = Print screen
- PAUS = Pause break

### ADJUST Layer (5) - System Functions (NAV+SYM)

```
┌─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┐
│ --- │ --- │ --- │ --- │ --- │ --- │ --- │ --- │ --- │ --- │ --- │ --- │
├─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┤
│RESET│BOOT │ --- │ --- │ --- │ --- │ --- │ --- │ --- │ --- │BOOT │RESET│
├─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┤
│ --- │BTCLR│BTPRV│BTNXT│OUTG │ --- │ --- │ --- │ --- │ --- │ --- │ --- │
├─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┤
│ --- │ --- │ --- │ --- │ --- │ PWR │ --- │ --- │ --- │ --- │ --- │ --- │
├─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┤
│ --- │ --- │ --- │ --- │ --- │ --- │ --- │ --- │ --- │ --- │ --- │ --- │
└─────┴─────┴─────┴─────┴─────┴─────┴─────┴─────┴─────┴─────┴─────┴─────┘
```

- RESET = System reset
- BOOT = Bootloader (for flashing)
- BTCLR = Bluetooth clear
- BTPRV = Bluetooth previous
- BTNXT = Bluetooth next
- OUTG = Output toggle
- PWR = Power toggle

## Combo Key Mappings

### Brackets (Adjacent Split Combos)
- T+Y keys (SL5+SR0) → [] with cursor in between
- G+H keys (ML5+MR0) → () with cursor in between
- B+N keys (FL5+FR0) → {} with cursor in between

### Programming Symbols
- E+R keys (SL3+SL4) → = (same-hand adjacent combo)
- D+L keys (ML3+MR3) → : (cross-hand combo)
- S+K keys (ML2+MR2) → ; (cross-hand combo)
- I+O keys (SR2+SR3) → \ (same-hand adjacent combo)
- K+L keys (MR2+MR3) → / (same-hand adjacent combo)
- .-  keys (FR3+FR4) → | (same-hand adjacent combo)

### Swedish Characters (Cross-hand Combos)
- A+J keys (ML1+MR1) → ä
- Q+U keys (SL1+SR1) → ö
- A+Y keys (ML1+SR0) → å

### Shortcuts
- P+Del keys (SR4+SR5) → DEL
- W+I keys (SL2+SR2) → Ctrl+Shift+7 (Comment in VSCode) 