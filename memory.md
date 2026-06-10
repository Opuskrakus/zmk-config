Återställ kanske nav layer combos
kolla på stickys på nav 
Överävger att separera num och sym layer
Kanske ta bort hrm på default och bara ha ett eget lager för det? 
Kolla på navigering för i3 , känns som att vi behöver ctrl tab/shifttab, ctrl w, osv  


Checka snabbare mus om det är blev bättre
Leader och repeat har vi kollat på och swappat nav & shift 

***

The "repeat key" on your LH1 thumb is actually a 3-in-1 magic shift (skeletyl.keymap:105-136). Tap behavior depends on context:

Context	Action	What fires
Hold	Regular shift	&kp LSHFT
Plain tap (no recent typing)	Sticky shift (next key shifted)	&sk LSHFT
Tap within 1200ms after A-Z	Repeats the last key	&key_repeat
Shift + tap (double-tap shift)	Caps-word (auto-caps for one word)	&caps_word
The adaptive-key magic is in the shift_repeat behavior:


trigger-keys = <A B C ... Z>;   // only after alpha
bindings = <&key_repeat>;        // fires repeat instead of sticky shift
max-prior-idle-ms = <1200>;      // only within 1200ms of the alpha
strict-modifiers;                // mods must match exactly
So if you just typed hell and you want another l, tapping the magic_shift thumb gives you l again instead of sticky shift. If you wait longer than 1200ms, it reverts to sticky-shift behavior.

Caps-word (the shifted tap → &caps_word) is a one-shot auto-caps that capitalizes the next word until it sees a space/punctuation — handy for typing CONSTANT_NAMES without holding shift.


preonic: 
Kolla på piltangenter, nedhållen tangent funkar inte, måste spamma tangenten