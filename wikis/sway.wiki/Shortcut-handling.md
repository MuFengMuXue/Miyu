### Format

    bindsym [--release] [--locked] [--no-repeat] [<Modifiers>+]<Keysyms> <command>
    bindcode [--release] [--locked] [--no-repeat] [<Modifiers>+]<Keycodes> <command>

`<Modifiers>` is a (possibly empty) `+` separated list of modifier bit flag names.
(`Shift`=`0x01`, `Lock`=`0x02`, `Ctrl`=`0x04`,  `Mod1`=`Alt`=`0x08`, `Mod2`=`0x10`, `Mod3`=`0x20`, `Mod4`=`0x40`, `Mod5`=`0x80`). These names should not be confused with the keys whose
pressing might produce the modifier; on US keyboards, keysym `Alt_L` (keycode 64) and keysym `Alt_R` (keycode 108) both produce the `Alt` modifier.

`<Keysyms>` is a nonempty `+` separated list of keysym names, case insensitive (so that `A` and `a` are both assumed to be lowercase `a`.)

`<Keycodes>` is a nonempty `+` separated list of xkbcommon keycode ids, typically an integer between 9 and 255, although possibly much larger.

The binding specifications here mostly overlap with those from i3 (see https://i3wm.org/docs/userguide.html#keybindings). Currently XKB layout specifiers are not supported.

### How to identify keys

If you have `xev` available, run `xev -event keyboard` to find the translated keysyms and keycodes
corresponding to a given key press or release.

A list of keysym names can be found in the `xkbcommon-keysyms.h` header file, usually
located in `/usr/include/xkbcommon/`. 

On Linux, scancode ids are often available in the `linux/input-event-codes.h` header; the
xkb keycodes are typically `scancode + 8`.

Under wayland, [wshowkeys](https://git.sr.ht/~sircmpwn/wshowkeys) can help identify key strokes.

### Examples
    
    # These two shortcuts are equivalent for US keyboards
    bindsym Ctrl+Shift+1 kill
    bindsym Ctrl+exclam kill

    # These shortcuts are equivalent and will both exit when, for
    # instance, Control_L, P and Q are pressed simultaneously
    bindsym Ctrl+q+p exit
    bindsym Ctrl+p+q exit

    # These two shortcuts are identical thanks to case insensitivity
    bindsym Mod5+R reload
    bindsym Mod5+r reload
    # This shortcut requires Shift to be held
    bindsym Mod5+Shift+R reload
    
    # When the <ESC> key is pressed, switch to workspace "F"
    bindcode 9 workspace F

    # When the right shift key is released, run the program `false`
    bindcode --release Shift_R exec false

    # When all modifiers but Caps Lock are active, and keys A
    # through G, 1 through 5 are pressed simultaneously, exit
    bindsym Mod5+Mod4+Mod3+Mod2+Mod1+Shift+Ctrl+a+b+c+d+e+f+g+1+2+3+4+5 exit

    # Dead key and compose key transformations are ignored
    bindsym Ctrl+dead_acute+e exec false
    bindsym Alt+Multi_key+1+2 exec false

### Limitations

Pressing multiple keys which would result in the same modifier change if pressed alone 
(such as `Shift_L` and `Shift_R` on US keyboards) may trigger bindings like `bindsym Shift+Shift_R`,
possibly contrary to expectation.

When multiple keys generate the same keysym or when a single key generates multiple keysyms, shortcuts
like `Ctrl+a+a+b` are possible. Similarly, `Ctrl+a+b` might not work if multiple distinct keys generating
`a` are pressed at the same time.
 
When running sway under X11, holding a modifier (say, `Control_R`) long enough to activate key repeat and then pressing another key (say, `A`), may trigger the shortcut `Ctrl+Control_R+a` rather than `Ctrl+a` as likely expected.