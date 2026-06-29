# Xorg/Keyboard configuration

This article describes the basics of Xorg keyboard configuration. For advanced topics such as keyboard layout modification or additional key mappings, see X keyboard extension or Extra keyboard keys respectively.

The Xorg server uses the X keyboard extension (XKB) to define keyboard layouts. Optionally, xmodmap can be used to access the internal keymap table directly, although this is not recommended for complex tasks. Also systemd's localectl can be used to define the keyboard layout for both the Xorg server and the virtual console.

## Viewing keyboard settings
You can use the following command to see the actual XKB settings:

{{hc|$ setxkbmap -print -verbose 10|
Setting verbose level to 10
locale is C
Applied rules from evdev:
model:      evdev
layout:     us
options:    terminate:ctrl_alt_bksp
Trying to build keymap using the following components:
keycodes:   evdev+aliases(qwerty)
types:      complete
compat:     complete
symbols:    pc+us+inet(evdev)+terminate(ctrl_alt_bksp)
geometry:   pc(pc104)
xkb_keymap {
        xkb_keycodes  { include "evdev+aliases(qwerty)" };
        xkb_types     { include "complete"      };
        xkb_compat    { include "complete"      };
        xkb_symbols   { include "pc+us+inet(evdev)+terminate(ctrl_alt_bksp)"    };
        xkb_geometry  { include "pc(pc104)"     };
};
}}

## Third party utilities
There are some "unofficial" utilities which allow to print specific information about the currently used keyboard layout.

* :

* :

## Setting keyboard layout
Keyboard layout in Xorg can be set in multiple ways. Here is an explanation of used options:

*  selects the keyboard model. This has an influence only for some extra keys your keyboard might have. The safe fallback are  (ANSI) or  (ISO). But for instance laptops usually have some extra keys, and sometimes you can make them work by simply setting a proper model.
*  selects the keyboard layout. Multiple layouts may be specified in a comma-separated list, e.g. if you want to quickly switch between layouts.
*  selects a specific layout variant available for the . For instance, the default  (Slovak) variant is , but you can manually specify , etc.
*  contains some extra options (comma-separated). Used for specifying layout switching, notification LED, compose mode etc. See the #Frequently used XKB options section for examples.

The layout name is usually a 2-letter country code. To see a full list of keyboard models, layouts, variants and options, along with a short description, open . Alternatively, you may use one of the following commands to see a list without a description:

*
*
*
*

Examples in the following subsections will have the same effect, they will set  model,  as primary layout,  as secondary layout,  variant for  layout and the  combination for switching between layouts. See  for more detailed information.

## Using X configuration files
The syntax of X configuration files is explained in Xorg#Configuration. This method creates system-wide configuration which is persistent across reboots.

Here is an example:

## Using localectl
For convenience, the tool localectl may be used instead of manually editing X configuration files. It will save the configuration in , this file should not be manually edited, because localectl will overwrite the changes on next start.

The usage is as follows:

 # localectl set-x11-keymap layout [model [variant options]

To set a model, variant or options, all preceding fields need to be specified, but the preceding fields can be skipped by passing an empty string with . Unless the  option is passed, the specified keymap is also converted to the closest matching console keymap and applied to the console configuration in . See  for more information.

To create a  like the above:

 # localectl --no-convert set-x11-keymap cz,us pc104 ,dvorak grp:win_space_toggle

## Using setxkbmap
setxkbmap sets the keyboard layout for the current X session only, but can be made persistent in xinitrc or xprofile. This overrides system-wide configuration specified following #Using X configuration files.

The usage is as follows (see ):

 $ setxkbmap xkb_model xkb_layout xkb_variant xkb_options

To change just the layout ( is the default flag):

 $ setxkbmap xkb_layout

For multiple customizations:

 $ setxkbmap -model pc104 -layout cz,us -variant ,dvorak -option grp:win_space_toggle

## Frequently used XKB options
## Switching between keyboard layouts
To be able to easily switch keyboard layouts, first specify multiple layouts between which you want to switch (the first one is the default). Then specify a key (or key combination), which will be used for switching. For example, to switch between a US and a Swedish layout using the  key, use  as an argument of  and  as an argument of . The number of s should match that of the s — if you want to switch solely between different variants, then duplicate the layout accordingly (e.g. ).

The list of available layouts (and variants) can be found in . The key combinations available for layout switching are listed in .

Note that the  option is unreliable and unlikely to be fixed; prefer other combinations.

## Switch languages using Alt Shift
To set  as a layout shortcut, use  in .

However, there is a known issue with XKB that causes other shortcuts of the type  to break. Moreover, XKB may set the right  to be  by default in some keyboard layouts, making  not working for layout switching.

As a workaround, sxhkd may be used to switch layouts by adding the following to :

 Shift_L + Alt_L
     setxkbmap -query | grep -q 'fr' && setxkbmap us || setxkbmap fr,us
 Shift_R + Alt_R
     setxkbmap -query | grep -q 'fr' && setxkbmap us || setxkbmap fr,us

Note that for some reason,  must be pressed before  to be detected by sxhkd.

## Terminating Xorg with Ctrl+Alt+Backspace
By default, the key combination  is disabled. You can enable it by passing  to . This can also be done by binding a key to  in  (which undoes any existing  setting).
In order for either method to work, one also needs to have  set to "off" in : since 2004 this is the default.

## Swapping Caps Lock with Left Control
To swap Caps Lock with Left Control key, add  to . Run the following command to see similar options along with their descriptions:

 $ grep -E "(ctrl|caps):" /usr/share/X11/xkb/rules/evdev.lst

## Enabling mouse keys
Mouse keys, not to be confused with the keys of the mouse, is disabled by default and has to be manually enabled by passing  to . This will make the  shortcut toggle mouse keys.

See also X keyboard extension#Mouse control for advanced configuration.

## Configuring AltGr
The AltGr (Alternate Graphic) key can be used to access additional characters and symbols on a keyboard. It functions as a modifier key similar to Shift but provides access to a third level of key mappings. Note that mapping levels work as follows:

* 1st Level: Default layer of keys (no modifier).
* 2nd Level: Accessed by pressing the Shift key, providing secondary characters (e.g. capitalization) or symbols (e.g. @ symbol).
* 3rd Level: Accessed by pressing the AltGr key, allowing access to additional characters or symbols not available on the 1st and 2nd levels.

2nd level characters are usually printed on keyboard keys and are easy to find. On the other hand, to check the characters on additional levels, you can use  or look up your keyboard mapping on .

## Configuring compose key
Though typically not on traditional keyboards, a Compose key can be configured to an existent key.

The  key begins a keypress sequence that involves (usually two) additional keypresses. Usage is typically either for entering characters in a language that the keyboard was not designed for, or for other less-used characters that are not covered with the  modifier. For example, pressing    produces , or     will produce an "em dash": .

Though a few more eccentric keyboards feature a  key, its availability is usually through substituting an already existing key to it. For example, to make the  key a  key use the Desktop environment configuration, or pass  to  (or setxkbmap: ). Allowed key substitutions are defined in :

 $ grep "compose:" /usr/share/X11/xkb/rules/evdev.lst

If the desired mapping is not found in that file, an alternative is to use xmodmap to map the desired key to the  keysym, which acts as a compose key by default (note that xmodmap settings are reset by setxkbmap).

## Key combinations
The default combinations for the compose keys depend on the locale configured for the session and are stored in , where  is for example .

You can define your own compose key combinations by copying the default file to  and editing it. Alternatively, create an empty  and include the default one using , for example:

The compose key (denoted as  in the  file) works with any of the thousands of valid Unicode characters, including those outside the Basic Multilingual Plane. Take a look at the  man page, it explains the format of the XCompose files.

However, GTK does not use XIM by default and therefore does not follow  keys. This can be fixed by forcing GTK to use XIM by configure the graphical environment variables  and/or .

## Currency sign on other key
Most European keyboards have a Euro sign (€) printed on on the  key. For example, to access it with , use the  and  options.

The Rupee sign (₹) can be used the same way with .

## Switching state immediately when Caps Lock is pressed
Those who prefer typing capital letters with the Caps Lock key may experience a short delay when Caps Lock state is switched, resulting in two or more capital letters (e.g. THe, ARch LInux). This occurs because Caps Lock is enabled immediately once the Caps Lock key is pressed, but is only disabled upon release of the second key-press. This behaviour stems from typewriters where a Caps Lock function was achieved by physically locking the shifted typebars in place, and the release of a shift key-press was the action that caused the release of the lock.

Some more popular operating systems have removed this behaviour, either voluntarily (as it can be confusing to some) or by mistake, however this is a question of preference. Bug reports have been filed on the Xserver bug tracker, as there is currently no easy way to switch to the behaviour reflected by those other operating systems. For anyone who would like to follow up the issue, bug reports and latest working progress can be found at [https://bugs.freedesktop.org/show_bug.cgi?id=27903 and ==== Workaround ====

First, export your keyboard configurations to a file:

 $ xkbcomp -xkb $DISPLAY xkbmap

In the file xkbmap, locate the Caps Lock section which begins with key :

  key  {         [       Caps_Lock  };

and replace whole section with the following code:

 key  {
     repeat=no,
     typesymbols[group1=[ Caps_Lock, Caps_Lock],
     actionsLockMods(modifiers=Lock), Private(type=3,data[0=1,data};

Save and reload keyboard configurations:

 $ xkbcomp -w 0 xkbmap $DISPLAY

Consider making it a service launching after X starts, since reloaded configurations do not survive a system reboot.

## One-click key functions
To assign an additional one-click function to a modifier key, you can use . For example it is possible to have  work as  when pressed alone, and as  when used with another key. First set the  swapping using setxkbmap as mentioned earlier, and xcape to set the  association:

 $ xcape -e 'Caps_Lock=Escape'

You can set multiple associations separated with a semicolon, e.g.: .

If you hold a key for longer than the timeout value (default 500 ms), xcape will not generate a key event.

## Adjusting typematic delay and rate
The typematic delay indicates the amount of time (typically in milliseconds) a key needs to be pressed and held in order for the repeating process to begin. After the repeating process has been triggered, the character will be repeated with a certain frequency (usually given in Hz) specified by the typematic rate. Note that these settings are configured separately for Xorg and for the virtual console.

## Using xset
The tool xset, provided by , can be used to set the typematic delay and rate for an active X server, though certain actions during runtime may cause the X server to reset these changes and revert instead to its seat defaults.

Usage:

 $ xset r rate delay [rate

For example to set a typematic delay to 200ms and a typematic rate to 30Hz, use the following command:

 $ xset r rate 200 30

Issuing the command without specifying the delay and rate will reset the typematic values to their respective defaults; a delay of 660ms and a rate of 25Hz:

 $ xset r rate

## Using xautocfg
 can apply repeat rate settings for newly connected devices automatically. It watches for X11 events and applies repeat rate configuration to newly connected keyboards.

Adjust the configuration:

If  is started by your window manager or desktop environment, enable the systemd/User . Alternatively, launch  manually.

## Using AutoRepeat configuration option
To persist the configuration system-wide, change the seat defaults with an Xorg configuration file as described in #Using X configuration files, and add a  section entry: The parameters for  are  and  in milliseconds. If you like 25 Hz  of xset, the corresponding  1000 / 25 = 40 milliseconds.

## Using XServer startup options
Another method of persisting the configuration is to pass the desired settings to the X server on its startup using the following options:

*  - sets the autorepeat delay (length of time in milliseconds that a key must be depressed before autorepeat starts).
*  - sets the autorepeat interval (length of time in milliseconds that should elapse between autorepeat-generated keystrokes).

See  for a full list of X server options and refer to your display manager for information about how to pass these options.

## Manually crafting a new layout
To manually modify or create a layout, some low-level knowledge is needed.

To physical keys, numbers assigned by kernel. They are listed in , provided —a dependency of —is installed, like this:

 #define KEY_Q			16
 #define KEY_W			17
 ...
 #define KEY_LEFTBRACE		26
 #define KEY_RIGHTBRACE		27

These values are used by libevdev. For input remap utilities that rely on libevdev, key names are often these entries in lowercase, without the prefix . Xorg's "keycode" value is the one in the file  + 8. (For example  is 16. The X's keycode of the key  printed "Q" 24.)

In XKB however, i.e. for X and Wayland, the key names look like  or . Most of them are easy to guess; for example if you have an Italian keyboard, just look at . It has the lines:

 key   {[ backslash,        bar,        notsign,       brokenbar };
 key   {[    egrave,     eacute,    bracketleft,       braceleft ]};

When it is not sufficient, look at files in , in particular the file . These lines define the keycode for the key name.

  = 49;
  = 34;

Finally, what are possible symbols that can be assigned to keys, like  or  in the above example? They are defined in

 #define XK_brokenbar                     0x00a6  /* U+00A6 BROKEN BAR */
 #define XK_notsign                       0x00ac  /* U+00AC NOT SIGN */

Some symbols with the prefix XF86 is listed in the separate file .

 #define XF86XK_MonBrightnessUp       0x1008ff02  /* Monitor/panel brightness */

This key is called  in X. (Again rip off XK_, but in such cases the middle of the name.)
