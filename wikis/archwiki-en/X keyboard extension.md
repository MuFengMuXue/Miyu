# X keyboard extension

The X keyboard extension, or XKB, defines the way keyboards codes are handled in X, and provides access to internal translation tables. It is the basic mechanism that allows using multiple keyboard layouts in X.

This article describes how to modify and create keyboard layouts. If you are looking for how to configure your keyboard, see Xorg/Keyboard configuration.

## Precautions and preparations
To prepare for the possibility of your X server crashing or your keyboard being put into an unusable state:

# Make sure you have some way to terminate the session without using your keyboard. (Aside from a power button, having some way to  or reboot the host remotely may be a good idea.)
# Make sure you have saved all your work to prevent data loss.
# If you use GNOME, you can install  to recover settings with the mouse. For example, when the keyboard becomes unusable, navigate to Keyboard & Mouse > Additional Layout Options with the mouse, and then check and uncheck all settings, which will reset the keyboard to the system behaviour.

## Getting and setting XKB layout
## Using rules
Look inside  for  files or the XKB Homepage to get ideas on how to configure rules. Your own configurations can go in .

For example one may want to remap their  key to :

## Using keymap
Use  (package ) to manipulate XKB data. To get current configuration, run

 $ xkbcomp $DISPLAY output.xkb

To upload the data back to the server, run

 $ xkbcomp input.xkb $DISPLAY

Note that without  argument  will try to compile .xkb file into (mostly useless) .xkm file, without uploading anything to the server. It will, however, check the syntax and report errors.

Once the layout is ready, save it as  and make  load it on startup:

The actual file name is irrelevant. Note that unlike standard system-wide configuration via , this is a per-user keymap. Also, there is no problem changing XKB configuration while X is running.

## Basic information on XKB
The core XKB functionality is quite simple, and it is necessary to have an idea on how it works before working on the keymaps.

## Tools and values
Use xev (package ) to get keycodes and to check how your keymap works.

Note keycode , state  and keysym  aka . Keycode  is what input device supplied to X, typically a physical key index of some sort. The state represents modifier keys,  is . Keycode together with the state value is what X sends to the application in  structure. Keysym and corresponding string is what the client obtained using  and friends.

The bits in the state field have pre-defined names: , , , , , ,  and , lowest to highest. Thus,  is 0x05, and so on. Client applications typically only check the bits they need, so an application with normal keyboard input and  shortcuts usually makes no distinction between  and  states.

Keysyms are numeric, too. A lot of them have names, declared in  with  prefix. However, the number is what clients actually receive. Keysyms are only important when an application expects some particular values; typically that is keys like arrows, Enter, Backspace, F-keys, and various shortcuts. For the rest, the string is used.

## Keycode translation
XKB works mostly at the XLookupString stage, transforming incoming keycode into keysym according to its own internal state, which is  group and state values:

    (keycode, group, state) → keysym

Group typically represents a "layout", as in US-English, French-AZERTY, Russian, Greek etc. There can be at most 4 groups.

Internally, the translation involves additional steps:

    (keycode group) → type
    (state, type) → level
    (keycode, group, level) → Swith  being the translation table (actually called , see #xkb_symbols).

Types are used to tell which modifiers affect which keys; essentially it is a way to reduce the third dimension of . For example, a typical alphanumeric key is only affected by , so its type is set to , and

    (state, TWO_LEVEL) → level = ((state >> 0) & 0x01) = state & 0x01

is either 0 or 1. Thus it is  instead of .

## Keysyms and states
In X terms,  and  means same keysym and different states, but  and  are different keysyms.

Generally it is XKB task to provide different keysyms, but states are handled later by individual applications.

Also, states in XKB have somewhat delayed effect, that is, you must have the state set prior to pressing a key.

Example:  can be configured to act as backspace in rxvt (application setting). This way rxvt will receive  keysym with  bit set in the state value, and it will be clearly different from  keysym. Alternatively, XKB can be used to make  combination generate  keysym with  bit set; in this case, rxvt will not see any difference between physical  key and  key as long as  key is pressed. Making  combination generate  keysym with no  bit set is an XKB task, too, but it is much more difficult to implement than .

## Actions
Keysym obtained from the table above can also trigger some action:

    (keysym, state) → action

For XKB, setting or locking a modifier bit is an action, and so is any X server interaction like switching consoles, terminating the server, moving pointer etc. Actions do not generally affect keysyms, and generating a keysym is not an action.

There is only one possible action for each (keysym, state) pair.

## Editing the layout
Start with whatever default configuration your server has. Whenever possible, make the changes gradually and test them.

The .xkb file produced by  is a simple text file. C++ style comments, // till the end of line, are allowed.  Section names, as in xkb_keycodes "name-here", are irrelevant at this point and can be omitted.

## xkb_keycodes
Keycode definition. The rest of the file does not use numeric keycodes, only symbolic keylabels defined in this section.

It is a good idea to leave only those keys the keyboard in question actually has here.

The labels themselves are arbitrary. They are only used in xkb_symbols section later.

## xkb_types
This section comes before xkb_symbols, so take a look, but try not to make changes yet. Standard types depend a lot on virtual modifiers, which will be explained later. For now, just find the types you need. Start with the following: ONE_LEVEL, TWO_LEVEL, ALPHABETIC.

ONE_LEVEL keys are not affected by modifiers; typically it is Enter, Space, Escape, F keys, Shift/Alt/Ctrl keys and so on. TWO_LEVEL and ALPHABETIC keys produce different keysyms depending on Shift state. All alphanumeric keys are of these types. ALPHABETIC additionally respects CapsLock.

Type description themselves are quite simple. The line

    modifiers= Shift+NumLock+LevelThree;

means keys of this type are affected by Shift, NumLock and LevelThree bits only. Map lines like

    map[Shift+LevelThree= Level4;

define which combination corresponds to which level value.  uses "LevelN" when dumping the data, but short and much more convenient "N" can be used as well.

level_name lines are irrelevant and can be ignored.

## xkb_compatibility
Action definitions () and keyboard LEDs () among other things. You can remove stuff you do not have or do not use, like keypad actions, mouse control or extra modifiers.

Note that  is equivalent to just , but  is much easier to read.

Check groups switching if you need it.  can be useful if you have four groups, otherwise / are enough.  can be useful for unusual setups.

## xkb_symbols
The main section that defines what each key does. Syntax:

    key  { [ G1L1, G1L2, G1L3, ... ], [ G2L1, G2L2, G2L3, ... ], ... }

 is keylabel from xkb_keycodes section,  is keysym for group i level j. The number of keysyms in each group must match the number of levels defined for this type ( will warn you if it does not).

Check  for the list of possible keysyms. Aside from those listed, you can also use  for Unicode symbol with hex code nnnn, e.g.  for combining acute accent. Note that  and  are treated differently (for instance, most applications expect , not  because their numeric values are different.

Key types are also specified here, either as

    key.type = "T1";
    key  { ... };
    key  { ... };
    key  { ... };
    key.type = "T2";
    key  { ... };
    key  { ... };

or individually for each key:

    key  { type = "T", [ .... ], [ .... ] };

Key type may be different in different groups. This is somewhat counter-intuitive, but actually has some useful applications. To set types for each group, use this:

    key  { type= "T1", type[2 = "T2", [ ... ], [ ... ] };

You can set labels for the groups using

    name= "EN";     // group 1
    name[2 = "RU";     // group 2
    name= "UA";     // group 3

This is what  will show if labels are enabled there.

The section also contains  lines. Leave them alone for now, or check Virtual Modifiers below.

## xkb_geometry
A completely irrelevant section describing physical keyboard layout. Can be deleted without any consequences.

## Basic examples
Check your existing layout first, as it likely contains standard definition for many common keys.

Throughout the text, "xkb_keycodes { text }" means "text" should be added to xkb_keycodes section. Whenever it is clear from context, section names are omitted.

## Simple key assignment
Enabling additional (aka multimedia) keys:

    xkb_keycodes {
         = 122;       // check with xev
         = 123;
    }

    xkb_symbols {
        key.type = "ONE_LEVEL";
        key  { [ XF86AudioLowerVolume  };
        key  { [ XF86AudioRaiseVolume ] };
    }

Escape on CapsLock, for Vim users mostly:

    key.type = "ONE_LEVEL";
    key  { [ Escape ] };

Exchanging Ins and PrintScreen (in case they are reversed — happens on Dell laptop keyboards):

    key.type = "ONE_LEVEL";
    key   { [    Print ] };
    key  { [   Insert ] };

On some HP laptop keyboards, the above does not work. Instead, the keycodes themselves must be redefined:

    partial xkb_keycodes "insert" {
        alias  = ;
        &lt;INS&gt;  = 218;
         = 118;
    };

Changing shift to a sticky key version:

replace

    key  {         [         Shift_L ] };

with

    key  {         [         ISO_Level2_Latch ] };

You might also need to add the following to

    interpret ISO_Level2_Latch+AnyOf(all) {
        useModMapMods=level1;
        action= LatchMods(modifiers=Shift,clearLocks,latchToLock);
    };
    interpret ISO_Level2_Latch+AnyOfOrNone(all) {
        action= LatchMods(modifiers=Shift,clearLocks,latchToLock);
    };

## Multiple layouts
For regular alphanumeric keys, just add a second/third/fourth [ ] section to the key definition:

    key.type = "ALPHABETIC";
    key  { [ q, Q ], [ a, A ] };      // QWERTY-AZERTY

    key  { [        s,        S ],        // two cyrillic layouts
                 [    U044B,    U042B ],
                 [    U0456,    U0406 ] };

Layout switching is done by triggering action LockGroup:

    interpret ISO_Next_Group { action = LockGroup(group=+1); };
    interpret ISO_Prev_Group { action = LockGroup(group=-1); };

Typically this means placing ISO_Next_Group and ISO_Prev_Group keysyms in correct group/level positions. Note that groups wrap, so if you have two groups and hit ISO_Next_Group twice, you will return to the group you started with.

Cyclic switching between two or more layouts with a dedicated key:

    key.type = "ONE_LEVEL";
    key  { [ ISO_Next_Group ] }

If you have more than two layouts and some keys to spare, it may be a better idea to have a dedicated key for each layout. Example for three layouts:

    key.type = "ONE_LEVEL";
    key  { [ ISO_Next_Group ],    // g1: switch to g2
                 [ ISO_Prev_Group ],    // g2: switch back to g1
                 [ ISO_Prev_Group ] };  // g3: switch to g2

    key  { [ ISO_Prev_Group ],    // g1: switch to g3
                 [ ISO_Next_Group ],    // g2: switch to g3
                 [ ISO_Next_Group ] };  // g3: switch back to g1

With four layouts, you will likely have to use ISO_First_Group and ISO_Last_Group.

The same idea can be implemented with only one key by utilizing TWO_LEVEL type:

    key.type = "TWO_LEVEL";
    key  { [ ISO_Next_Group, ISO_Prev_Group ],
                 [ ISO_Prev_Group, ISO_Next_Group ],
                 [ ISO_Prev_Group, ISO_Next_Group ] };

This way it is Menu for group 2 and Shift-Menu for group 3. To use Ctrl or Alt instead of Shift, replace TWO_LEVEL with PC_CONTROL_LEVEL2 or PC_ALT_LEVEL2 types respectively.

Switching using two modifier keys (Shift+Shift, Ctrl+Shift etc) can be done by using something other than ONE_LEVEL for these keys. Shift+Shift example:

    key.type = "TWO_LEVEL";
    key  { [ Shift_L, ISO_Prev_Group ] };
    key  { [ Shift_R, ISO_Next_Group ] };

To latch a group (aka toggle; set for the time you hold the key only), use LatchGroup action typically bound to ISO_Group_Latch keysym:

    key  { [ ISO_Group_Latch ] }

Adjust ISO_Group_Latch definition in xkb_compatibility section to use the right group:

    interpret ISO_Group_Latch { action = LatchGroup(group=3); };

Check  for more standard examples.

## Caps hjkl as vimlike arrow keys
Creating keymappings that clear modifiers from the keypress is necessary if the target key is to be used in keyboard shortcuts. For instance, highlighting text from the main keyboard (), or changing chats in most messengers () will not work if there is an additional  modifier sent. However, an additional modifier must be sent if a user rebinds a letter key by simply putting the keysym in the symbols section. Rebinding as follows permits functionality like AHK's blind command.

The  section (which defines layer mapping) must contain an entry such that:
*When no modifiers are pressed, the first level of keysyms is used (lowercase letters).
*When Shift only is pressed, the second level of keysyms is used (capital letters).
*When Lock only is pressed, the third level of keysyms is used (the arrow keys)
*When Shift and Lock are pressed, the third level of keysyms is also used (shift+arrow keys).

Add this to the bottom of your types section:

  xkb_types "complete" {
    ...
    type "CUST_CAPSLOCK" {
        modifiers= Shift+Lock;
        map= Level2;            //maps shift and no Lock. Shift+Alt goes here, too, because Alt isn't in modifiers.
        map[Lock = Level3;
        map= Level3;       //maps shift and Lock. Shift+Lock+Alt goes here, too.
        level_name[Level1= "Base";
        level_name"Shift";
        level_name[Level3= "Lock";
    };
  };

Now change caps from a lock (toggle) to a set (press) by modifying the already existing definition in compatability from LockMods to SetMods:

(Note that this means you cannot use capslock like normal)

  xkb_compatibility "complete" {
    ...
    interpret Caps_Lock+AnyOfOrNone(all) {
        action= SetMods(modifiers=Lock);
    };
    ...
  };

Finally, modify your symbols file as follows.

  xkb_symbols "pc_us_inet(evdev)" {
    ...
    key  {
        type= "CUST_CAPSLOCK",
        symbols[               h,               H,               Left,
        actions[      NoAction(),      NoAction(),   RedirectKey(keycode=, clearmods=Lock)
   };

## Additional symbols
Typing more with the same keys.

## Compose key
Easy to set up and extremely useful for entering common Unicode characters.

    key  { [ Multi_key ] };

## Level3
The idea is similar to Alt or AltGr in their original meaning: alphanumeric keys get additional characters, activated by holding down some modifier key.

First of all, setting up the modifier.

    xkb_symbols {
        key  {  };
        modifier_map Mod5 { ISO_Level3_Shift };
    }

Also, the following should already be defined in the relevant sections, but in case it is not:

    xkb_compatibility {
        interpret ISO_Level3_Shift { action= SetMods(modifiers=Mod5); };
    }

    xkb_types {
        type "THREE_LEVEL" {
            modifiers= Shift+Mod5;
            mapLevel2;
            map[Mod5= Level3;
            mapLevel3;
            level_name[Level1= "Base";
            level_name"Shift";
            level_name[Level3= "Level3";
        };
        type "FOUR_LEVEL" {
            modifiers= Shift+LevelThree;
            mapLevel2;
            map[LevelThree= Level3;
            mapLevel4;
            level_name[Level1= "Base";
            level_name"Shift";
            level_name[Level3= "Alt Base";
            level_name"Shift Alt";
        };
    }

Note standard definitions have LevelThree instead of Mod5 in xkb_compatibility and xkb_types. As long as modifier_map above uses Mod5, there is no practical difference, you will end up using Mod5 bit anyway.

Now, the keys themselves, vi-style cursors in this case:

    key.type = "THREE_LEVEL";
    key  { [ h, H,  Left  };
    key  { [ j, J,  Down ] };
    key  { [ k, K,    Up ] };
    key  { [ l, L, Right ] };

As you may find out using , this produces Mod5+Left instead of just Left. But that is ok as most applications ignore state bits they do not use. For an alternative solution, check Overlays below.

## Meta, Super and Hyper
## Real modifiers
Some applications (notably Emacs) allow meaningful use of higher state bits. It is usually assumed there are modifier keys called Meta, Super and Hyper on the keyboard beside standard Shift, Ctrl and Alt, which control these bits.

From XKB point of view this means setting Mod2, Mod3, Mod4 and Mod5 modifier bits. Because all you need is the bits themselves, there is no need to edit types like in the Level3 example above.

    xkb_compatibility {
        interpret Super_L { action = SetMods(modifiers=Mod3); };
    }

    xkb_symbols {
        key  { [ Super_L ] };
        modifier_map Mod3 { Super_L };
    }

Standard definitions use Super modifier instead of Mod3 in . You can keep that, just make sure  line is in place.

Keep in mind there is no strict correspondence between ModN and named modifiers like Super, Hyper or even Alt. Mod1 is the only one that is widely used; some applications call it Meta, some Alt. For the others, check how particular application treats state bits, and/or check Virtual modifiers below.

## Keysym tracking
At least one application (openbox) is known to track KeyPress/KeyRelease events for Meta_Super_[LR and Hyper_keysyms instead of relying on the state bits. In such case

    xkb_symbols {
        key  { [ Super_L  };
    }

is enough and you can omit  and  lines.

Speaking of Openbox, note it actually allows both methods: "S-h" tracks Super_events while "Mod3-h" checks relevant state bit.

## Preset configuration
XKB is often configured by specifying XkbTypes/XkbCompat/XkbSymbols, or XkbModel/XkbLayout (+XkbVariant/XkbOptions), or XkbKeymap, typically in /etc/X11/xorg.conf or /etc/X11/xorg.conf.d/*.conf, like this:

    Option  "XkbModel"    "thinkpad60"
    Option  "XkbLayout"   "us,sk,de"
    Option  "XkbVariant"  "altgr-intl,qwerty,"
    Option  "XkbOptions"  "grp:menu_toggle,grp_led:caps"

These values define full XKB map (the one that can be dumped by ) by combining several files from . In fact, equivalent .xkb file for  can be obtained using :

 $ setxkbmap -model thinkpad60 -layout us,sk,de -variant altgr-intl,qwerty \
        -option -option grp:menu_toggle -option grp_led:caps -print

Note include statements in the output. The files for each section are fetched from relevant subdirectories under , i.e.

    xkb_types { include "complete" };

means  will look for . Plus signs mean concatenation, so

    xkb_keycodes { include "evdev+aliases(qwerty)" };

means

    xkb_keycodes {
        include "evdev";
        include "aliases(qwerty)";
    };

Parenthesis select named section from the file. Check  and note

    xkb_keycodes "qwerty" { ... };

this is the part  refers to. Finally, colons allow shifting parts of layout to another group.

Unlike XkbTypes/XkbCompat/XkbSymbols/XkbGeometry values, which define relevant .xkb file sections directly, XkbModel, XkbLayout and XkbRules refer to additional non-xkb files found under  that match model and layout values to specific symbols and geometry. XkbKeymap refers to complete keymaps. Check Ivan Pascal page for detailed description.

Just like with  approach, this kind of configuration can be done on the fly: use  without -print option.

The files from  are a good source of examples, especially when it comes to standard keyboard features with nontrivial XKB implementation (e.g. keypad/NumLock handling). Also, these are the files you have to edit to push your changes upstream. Check [https://www.freedesktop.org/wiki/Software/XKeyboardConfig/Rules X Keyboard Config Rules before doing it though.

## xmodmap
xmodmap is not directly related to XKB; it uses different (pre-XKB) ideas on how keycodes are processed within X. In particular, it lacks the notion of groups and types, so trying to set more than one keysym per key is not likely to work. In general, except for the simplest modifications of keymaps or pointer button mappings,  should be used instead.

## Indicators
As in "keyboard LEDs". Indicator names are used to match the to the physical LEDs in xkb_keycodes section. Otherwise, they are irrelevant. Indicators not matched to any LED are called "virtual";  (package ) can be used to check their state. Example:

    xkb_keycodes {
        indicator 1 = "LED1";       // first physical LED
    }

Indicators always reflect specified part of XKB internal state. Two common modes is showing modifier state:

    xkb_compatibility {
        indicator "LED1" { modifiers = Lock; }; // CapsLock indicator
    }

or current group:

    xkb_compatibility {
        indicator "LED1" { groups = 0x06; };    // "group 2 or group 3 is active"
    }

The values are bitmasks. For groups, bit 1 is group 1, bit 2 is group 2 and so on.

## Modifiers and types
At some point it may become necessary to clean up types section, and/or to introduce unusual types.

Types and modifiers are tightly connected, so it makes a lot of sense to start with the modifier bits first, before doing anything with the type descriptions.

Decide which bits you will use. There are only eight of them, and of those, Shift, Control and Mod1 are widely used in applications, and Lock (aka CapsLock) has pre-defined meaning which also may be hard to override. The remaining four, however, are fair play.

Warning: four standard types, ONE_LEVEL, TWO_LEVEL, ALPHABETIC and KEYPAD, receive special treatment in . They may work differently just because they are named this way. Avoid deleting them. If some changes do not work as expected, try adding a new type instead.

## Using real modifiers in standard types
Depending of your base configuration, there may be a lot of unused standard types like EIGHT_LEVEL or PC_RCONTROL_LEVEL2. Remove them to avoid doing unnecessary work.

Now, some standard types use virtual modifiers. If you decide to use them, check Virtual modifiers below and skip this section. Otherwise, it is a good idea to get rid of them completely. Check the types you need, and either replace them with corresponding real ones, or remove relevant definitions. Example:

    type "KEYPAD" {
        modifiers= Shift+NumLock;
        mapLevel2;
        map[NumLock= Level2;
        level_name"Base";
        level_name[Level2= "Number";
    };

if you use Mod2 for NumLock, change the type to

    type "KEYPAD" {
        modifiers= Shift+Mod2;
        mapLevel2;
        map[Mod2= Level2;
        level_name"Base";
        level_name[Level2= "Number";
    };

if you are not going to have NumLock modifier, change it to

    type "KEYPAD" {
        modifiers= Shift;
        mapLevel2;
        level_name[Level1= "Base";
        level_name"Number";
    };

Do the same in xkb_compatibility section too. Once it is done, you should be able to remove all "virtual_modifiers" lines in the file.

## Switching a single modifier bit
Basically all you need is a keysym with a relevant interpretation entry. Example for Mod5 switching with  key, with  for keysym:

    xkb_compatibility {
        interpret ISO_Level3_Shift { action = SetMods(modifiers=Mod5); };
    }

    xkb_symbols {
        key  { [ISO_Level3_Shift  };
    }

Aside from , you can also use  or .  makes a regular "on while pressed" modifier key.  makes an "on/off" switch like CapsLock or NumLock.  means "on until next keypress" aka sticky modifier

## modifier_map
Modifier map is a table that maps each of eight modifier bits to at most 4 keys:

    modifier_map Mod1 { Alt_L, Alt_R };

In the core protocol, without XKB, it means more or less the same thing as

    interpret Alt_L { action = SetMods(modifiers=Mod1); };
    interpret Alt_R { action = SetMods(modifiers=Mod1); };

XKB does not use modifier map in its original meaning. Within XKB, its only function is to map virtual modifiers (see below).

However, the table is easily accessible by clients, and there is one counter-intuitive (but well-known) trick involving it: modifier map is used to tell which of ModX bits is Alt. Because of this, it is a good idea to have one modifier mapped to Alt_L or Alt_R as shown above. Unless you have very good reasons to do otherwise, it should be Mod1.

## Multiple keyboards
XKB allows setting keymap for a single connected physical keyboard only. This feature can be extremely useful for multi-keyboard setups when keyboards in question are different; consider a laptop with a full-size USB keyboard attached.

First of all, use xinput (package ) to get device IDs:

    AT Translated Set 2 keyboard                id=11   keyboard (3)

Now,

 $ xkbcomp -i 11 file.xkb $DISPLAY

or

 $ setxkbmap -device 11 ...

will set keymap for specified keyboard only. Dumping XKB configuration works too:

 $ xkbcomp -i 11 $DISPLAY file.xkb

Note  will not work and will not give a clear error message either. Make sure you have space after .

## Debugging XKB
When keys do not work as expected, the first thing to check is XKB internal state: modifiers, effective group and control bits. All three can be used to drive LEDs; use  to check them

    indicator "LED1" { modifiers = Lock; };
    indicator "LED2" { groups = 2; };
    indicator "LED3" { controls = audiblebell; };

Additionally,  shows all (real) modifiers together with their lock/latch status. Modifiers are also reported by .  can be used to monitor effective group, but make sure two_state mode is off.

In case interpretations section does not work well, make sure to check for duplicated "interpret" blocks. Better yet, try commenting out anything related to specific keysym. See section 9.2 for explanation.

It also makes sense to check what exactly the server got by downloading the keymap back with

 $ xkbcomp $DISPLAY out.xkb

The results tend to be different from the input file. There is no known work-around for this.

## Virtual modifiers
One of the most troublesome parts of XKB, virtual modifiers appear prominently in all standard keymaps, despite being a relatively minor and mostly useless feature. The term itself is grossly misleading, and most of the docs do not help much either.

So, first of all: virtual modifiers are not modifiers in the same way real modifiers are. If anything, it is a way to name some of the real modifiers. They are not 16 more bits that can be used in level definitions. They are 16 possible names, each referring to one (or some, or none) of the 8 modifier bits.

Real modifier bits are called Shift, Lock, Control and Mod1-Mod5. There are no Alt among them. Virtual modifiers were introduced to allow saying something like

    #define Alt Mod1

to applications willing to use this information.

It is possible to make a usable layout without defining virtual modifiers at all. Among standard modifiers, only Alt/Meta actually need such treatment, because Shift and Control are real modifiers anyway and NumLock is not normally used as a modifier.

Also, unlike most of the keymap-related things that affect any application using basic Xlib functions, virtual modifiers must be queried explicitly using XKBlib calls. Not all applications actually do that.

## Defining virtual modifiers
The mapping between virtual and real modifiers is defined in a rather weird way using keysyms as a medium. Refer to XKBproto for some reasons behind this. Real modifiers M are assigned to a key using

    modifier_map M {  };

Virtual modifiers V can be assigned to a key using

    interpret  { virtualMod = V; };

If a virtual modifier V shares at least one keysym with a real modifier M, it is bound to M.

Note that virtual modifier names are not pre-defined and must be declared in  xkb_compatibility and xkb_types sections before using them:

    xkb_compatibility "complete" {
        virtual_modifiers LevelThree,NumLock,Alt;
    }

## Keysym interpretation
Virtual modifiers can be used in interpret  blocks as if they were defined to the respective real modifiers. For a virtual modifier V not bound to any real modifier, this means

    #define V

type declaration, and

    interpret  { }
    interpret +V { }

blocks will be treated as duplicates. Only one of them, the last one in the file, will work.  usually gives a warning in cases like this.

## Client side notes
Handling XKB virtual modifiers on the client side requires some non-trivial server interaction. Most applications just do not bother, sticking with 8 real modifiers supplied in XKeyEvent.state.

However, it is possible for an application to obtain virtual modifiers associated with a key press. Gtk, for instance, has which may or may not be used in particular application.

Some others may implement something that looks like virtual modifier support, but actually is not, see the Openbox example in #Keysym tracking. Regarding Alt handling, see #modifier_map.

## XKB control bits
A bunch of bit flags affecting various aspects of XKB functionality. To control them, use {Set,Latch,Lock}Controls actions.

## Mouse control
XKB allows controlling mouse pointer from keyboard. When set up properly, it can be extremely useful. However, its usability depends a lot on particular physical keyboard layout and on user's individual preferences.

From XKB point of view it is relatively simple to implement, one should just trigger relevant actions. Fairly complete implementation can be found in .

Note that the actions will not work unless  control bit is set:

    interpret Pointer_EnableKeys { action= LockControls(controls=MouseKeys); };

Because most keyboards do not have dedicated mouse control keys,  combining  and one of the  flags may be a good idea:

    interpret Pointer_EnableKeys { action= LockControls(controls=MouseKeys+Overlay1); };

This allows moving pointer control keys to appropriate overlay block:

    xkb_keycodes {
         = 218;
         = 212;
         = 214;
         = 216;
    }

    xkb_symbols {
        key    { [    Up , overlay1 =  };
        key  { [  Left ], overlay1 =  };
        key  { [ Right ], overlay1 =  };
        key  { [  Down ], overlay1 =  };

        key   { [ Pointer_Up ] };
        key  { [ Pointer_Down ] };
        key  { [ Pointer_Left ] };
        key  { [ Pointer_Right ] };
    }

This way it is possible to assign non-mouse actions to the keys used to control mouse, and thus, for example, use modifier keys to generate mouse buttons events.

## Local XKB folder
You can set an X keymap from a local file using the following command:

 $ xkbcomp keymap.xkb $DISPLAY

where  must have a structure like

{{hc|keymap.xkb|
xkb_keymap {
    xkb_keycodes  { ... };
    xkb_types     { ... };
    xkb_compat    { ... };
    xkb_symbols   { ... };

    // Geometry is completely optional.
    // xkb_geometry  { include "pc(pc104)" };
};
}}

You can use includes from this file, where the inclusion refer to a local folder instead of . You need to use the  parameter of  for that. Full example:

 $ xkbcomp -I$HOME/.xkb $HOME/.keymap.xkb $DISPLAY

{{hc|$HOME/.keymap.xkb|
xkb_keymap {
    xkb_keycodes  { include "evdev+aliases(qwerty)" };
    xkb_types     { include "complete" };
    xkb_compat    { include "complete" };
    xkb_symbols   { include "pc+custom+inet(evdev)" };
};
}}

The symbol file must have the same name as specified in the  right above.
{{hc|$HOME/.xkb/symbols/custom|
partial alphanumeric_keys xkb_symbols "custom" { ... };
}}

## Configuration tools
Most desktop environments allow for changing XKB options via their settings managers. Other relevant tools include:
*  - a GUI tool for key remapping.
*  - Keyboard Layout Files Creator is a CLI utility for generating layouts from a JSON specifiation into various formats.

## Troubleshooting
## Setting layout via xorg.conf or .xinitrc doesn't work
If you are able to sucessfully set an XKB layout after starting Xorg, via , but not at startup using an Xorg configuration file or  (either with  using a precompiled XKB map or ), then you might have an input method enabled which is overriding XKB. This behavior exists and can be disabled for Fcitx and Fcitx5.

## I have an USB keyboard and the settings get lost upon unplugging it
Using rules instead of static keymap configuration will give you a more flexible and permanent key mapping that does not need to be reloaded manually (or by a script).
