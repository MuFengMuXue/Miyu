This page contains [[changes](https://wiki.gentoo.org/index.php?title=Keyboard_layout_switching&oldid=1266127&diff=1429094)] which are not marked for translation.

Other languages:

-   [English]
-   [magyar](https://wiki.gentoo.org/wiki/Keyboard_layout_switching/hu "A billentyűzetkiosztás módosítása (100% translated)")
-   [русский](https://wiki.gentoo.org/wiki/Keyboard_layout_switching/ru "Переключение раскладки клавиатуры (62% translated)")
-   [தமிழ்](https://wiki.gentoo.org/wiki/Keyboard_layout_switching/ta "விசைபலகை இடுவெளியை மாற்றுதல் (39% translated)")
-   [中文（中国大陆）‎](https://wiki.gentoo.org/wiki/Keyboard_layout_switching/zh-cn "切换键盘布局 (29% translated)")
-   [日本語](https://wiki.gentoo.org/wiki/Keyboard_layout_switching/ja "キーボードレイアウトの切替え (100% translated)")
-   [한국어](https://wiki.gentoo.org/wiki/Keyboard_layout_switching/ko "키보드 배치 바꾸기 (67% translated)")

A **keyboard layout** maps scancodes from a keyboard into characters sent to an application.

An appropriate keyboard layout is required to support both QWERTY and non-QWERTY keyboards, to enter characters outside of ASCII set.

Keyboard layouts can also do more complex transformations, e.g. via so called dead keys which do not output characters on their own, but modify output of subsequent keys.

## Contents

-   [[1] [Text-mode]](#Text-mode)
    -   [[1.1] [OpenRC]](#OpenRC)
        -   [[1.1.1] [Custom keymap]](#Custom_keymap)
    -   [[1.2] [systemd]](#systemd)
-   [[2] [X11]](#X11)
    -   [[2.1] [KDE Plasma]](#KDE_Plasma)
        -   [[2.1.1] [EurKEY (US) Layout]](#EurKEY_.28US.29_Layout)
    -   [[2.2] [Generic desktop environment]](#Generic_desktop_environment)
    -   [[2.3] [Generic X11]](#Generic_X11)
        -   [[2.3.1] [Using setxkbmap]](#Using_setxkbmap)
        -   [[2.3.2] [Using system-wide configured layouts and shortcut]](#Using_system-wide_configured_layouts_and_shortcut)
            -   [[2.3.2.1] [Additional configuration possibilities]](#Additional_configuration_possibilities)
    -   [[2.4] [Enhancing an X keyboard layout]](#Enhancing_an_X_keyboard_layout)
        -   [[2.4.1] [The fundamentals]](#The_fundamentals)
        -   [[2.4.2] [Adding key assignments]](#Adding_key_assignments)
        -   [[2.4.3] [Adding actions to function keys]](#Adding_actions_to_function_keys)
            -   [[2.4.3.1] [Creating the new type CTRL+ALT+SHIFT]](#Creating_the_new_type_CTRL.2BALT.2BSHIFT)
            -   [[2.4.3.2] [Activating the symbols F13, \..., F24]](#Activating_the_symbols_F13.2C_....2C_F24)
            -   [[2.4.3.3] [Amending the entries in symbols for keys F1, \..., F12]](#Amending_the_entries_in_symbols_for_keys_F1.2C_....2C_F12)
-   [[3] [See also]](#See_also)

## [Text-mode]

### [OpenRC]

The default console keymap is set in [/etc/conf.d/keymaps] by assigning the appropriate keymap as the value for `keymap`. The keymap values are defined in [/usr/share/keymaps], and most users will use a value from [/usr/share/keymaps/i386/qwerty/]. Optionally, set the value for the `extended_keymaps` variable from the appropriate include directory, like [/usr/share/keymaps/i386/include]. For example, set extended_keymaps=\"euro2\" to get Euro and cent with Alt-Gr on the positions where many keyboards have E and C.

[FILE] **`/etc/conf.d/keymaps`Example configuration**

    keymap="us"
    extended_keymaps=""

Lastly restart `keymaps` for apply changes and add `keymaps` to the boot runlevel:

`root `[`#`]`rc-service keymaps restart `

`root `[`#`]`rc-update add keymaps boot`

If you need the terminal show non-ASCII characters you must edit [/etc/conf.d/consolefont] and change font:

[FILE] **`/etc/conf.d/consolefont`Example configuration for cyrillic font**

    consolefont="cyr-sun16"

Restart the consolefont service and add it to boot runlevel:

`root `[`#`]`rc-service consolefont restart `

`root `[`#`]`rc-update add consolefont boot `

#### [Custom keymap]

To make a custom keymap look at the provided keymaps in [/usr/share/keymaps]:

`user `[`$`]`vi <keymap file>.map `

`user `[`$`]`gzip <keymap file>.map `

`root `[`#`]`mv <keymap file>.map /usr/share/keymaps/<some directory>`

Here is an example custom keymap which is the same as the U.S. QWERTY keymap, except the forward slash and apostrophe keys are swapped:

[FILE] **`/usr/share/keymaps/i386/qwerty/swap_slash_apostrophe.map.gz`Example Keymap**

    include "us.map"

    keycode  40 = slash            question
    keycode  53 = apostrophe       quotedbl

** Warning**\
Keycodes are likely to differ from system to system.

To find the keycodes mapped to keys view the output of [dumpkeys]:

`user `[`$`]`dumpkeys -l`

If the key cannot be found using the above command, run:

`user `[`$`]`showkey`

Just press the key and its keycode will be shown. When finished wait a few seconds and [showkey] will close.

### [systemd]

[systemd](https://wiki.gentoo.org/wiki/Systemd "Systemd") uses [/etc/vconsole.conf] and includes both terminal font and keyboard layout settings but lacks advanced settings found in OpenRC. Valid values should match what OpenRC supports for the corresponding variable.

[FILE] **`/etc/vconsole.conf`Example settings**

    KEYMAP=pl2
    FONT=LatArCyrHeb-16

## [X11]

Modern X11 applications usually use [[[x11-libs/libxklavier]](https://packages.gentoo.org/packages/x11-libs/libxklavier)[]] (\"*klavier*\" being German for "*piano*\") and can be configured by using [setxkbmap]. Furthermore X11 supports much broader sets of keyboard layouts than is supported for virtual terminals.

It should be kept in mind that a proper desktop environment will do its own keyboard layout management. There is no need to directly use the aforementioned application but it can come in handy when dealing with broken or lacking keyboard layout management.

### [KDE Plasma]

Open [System Settings] and navigate to the [Input Devices] module.

To make additional languages available in the [SDDM](https://wiki.gentoo.org/wiki/SDDM "SDDM") login manager, follow instructions on [adding custom keymap](https://wiki.gentoo.org/wiki/SDDM#Keymap "SDDM").

#### [][EurKEY (US) Layout]

The **EurKEY (US)** layout provides an augmented US keyboard layout with additional characters available using [Right Alt]. For example [Right Alt]+[5] for the euro currency symbol (`€`) and [Right Alt]+[u] for `ü`.

From [System Settings] navigate to *Keyboard* under [Input & Output]. Enable the toggle for *Layouts* and click *+ Add\...*. From the dialog that appears search for and select **EurKEY (US)**, press *OK* and apply changes.

### [Generic desktop environment]

Edit [\~/.xprofile] and call [setxkbmap] from there or setup the keyboard in Xorg configuration file ([see below](https://wiki.gentoo.org/wiki/Keyboard_layout_switching#Generic_X11 "Keyboard layout switching") for examples).

** Note**\
Recent versions of [GNOME](https://wiki.gentoo.org/wiki/GNOME "GNOME") 3 do not use [[[x11-libs/libxklavier]](https://packages.gentoo.org/packages/x11-libs/libxklavier)[]] any more therefore this might not work at all or likely get overridden by GNOME. Similarly any other desktop environment might also override the [[[x11-libs/libxklavier]](https://packages.gentoo.org/packages/x11-libs/libxklavier)[]] configuration as part of the initialization or layout change.

** Warning**\
[\~/.xprofile] is a non-standard file that is sourced only when logging in via a display manager that supports it (tested only on [GDM](https://wiki.gentoo.org/wiki/GNOME/GDM "GNOME/GDM"), [LightDM](https://wiki.gentoo.org/wiki/LightDM "LightDM"), [LXDM](https://wiki.gentoo.org/wiki/LXDE "LXDE") and [SDDM](https://wiki.gentoo.org/wiki/SDDM "SDDM")) and it might be distribution specific although all common distributions seem to support this file.

### [[] Generic X11]

#### [Using setxkbmap]

These changes are non-permanent and will persist only as long as the user does not restart X11. Naturally the command can be called from a startup script to set the appropriate parameters on every start of the X server.

To query the existing configuration:

`user `[`$`]`setxkbmap -query`

Setting a keyboard layout:

`user `[`$`]`setxkbmap lv`

Setting a keyboard layout, its variant and model:

`user `[`$`]`setxkbmap lv apostrophe -model logiultrax`

Setting up two keyboard layouts with LED indication:

`user `[`$`]`setxkbmap -layout us,ru -option grp:shifts_toggle -option grp_led:caps`

It is advised to read `xkeyboard-config` manual for a full list of keyboard configuration options:

`user `[`$`]`LESS=--chop-long-lines man xkeyboard-config`

Finding the supported layouts and variants or values of other xkb properties does not appear to be possible with this application, although most of them are listed in the [/usr/share/X11/xkb/rules/base.lst] file. To get the most complete list seems to be possible only by examining other files in [/usr/share/X11/xkb/]. For sake of sanity, it is advised to use of a proper desktop environment with its own keyboard layout management.

#### [Using system-wide configured layouts and shortcut]

This method is recommended for configurations without desktop environments, in other words just X11 with a window manager. Since Gnome removed the ability to change the Keyboard layouts in GDM using the gnome-control-center, GDM also relies on this method on systems without systemd. Create the [[10-keyboard.conf](https://wiki.gentoo.org/wiki/Xorg/Guide#Configuring_the_keyboard "Xorg/Guide")] file and configure it with the appropriate keyboard settings. Create the directory /etc/X11/xorg.conf.d if it does not exist.

[FILE] **`/etc/X11/xorg.conf.d/10-keyboard.conf`Example for US and brazilian layouts**

    Section "InputClass"
        Identifier "keyboard-all"
        Driver "evdev"
        Option "XkbLayout" "us,br"
        Option "XkbVariant" ",abnt2"
        Option "XkbOptions" "grp:shifts_toggle,grp_led:scroll"
        MatchIsKeyboard "on"
    EndSection

The example above configures US and Brazilian keyboard layouts with [Left Shift]+[Right Shift] as shortcut to alternate between them. Brazilian layout is signalled by Scroll Lock LED on the keyboard.

** Note**\
When using a Cyrillic language layout and the keyboard has "Windows®" keys, it may be necessary to add responsive `",winkeys"` to `XkbVariant` option.

##### [Additional configuration possibilities]

There are a number of variants and options available which can be used while configuring the keyboard mappings. Most of those can be found in the [/usr/share/X11/xkb/rules/base.lst] file.

For example, the US layout with possibility to write some international characters can be configured by using the variant `altgr-intl`:

[FILE] **`/etc/X11/xorg.conf.d/10-keyboard.conf`AltGr-international variant for US layout**

    ...
        Option "XkbLayout" "us,br"
        Option "XkbVariant" "altgr-intl,abnt2"
    ...

[Right Alt] is then used as a modifier for typing international characters.

Xorg provides the option to type international and various symbol characters by composition - which means by pressing *compose key* followed by a sequence of characters. To enable composition add the `compose:<compose_key>` option:

[FILE] **`/etc/X11/xorg.conf.d/10-keyboard.conf`Enabling key composition**

    ...
    Option "XkbOptions" "grp:shifts_toggle,grp_led:scroll,compose:sclk"
    ...

The `compose:sclk` option above configures [Scroll Lock] as compose key. With this setting:

-   Press [Scroll Lock] then type \'oo\' to get degree sign \'°\'
-   Press [Scroll Lock] then type \'oc\' to get copyright sign \'©\'
-   Press [Scroll Lock] then type \':)\' to get smiling face \'☺\'
-   Press [Scroll Lock] then type \'\^2\' to get superscript 2 (\'²\')
-   Press [Scroll Lock] then type \'\_2\' to get subscript 2 (\'₂\')
-   Press [Scroll Lock] then type \'di\' to get diameter sign \'⌀\'

\... and many more. The [/usr/share/X11/locale/compose.dir] file lists all possible composition sources.

### [Enhancing an X keyboard layout]

This is necessary when more far-reaching changes have to be made to the keyboard layout, such as adding key assignments, or adding actions to function keys. Since such changes are actually enhancements to the source files of a package, it is recommended to use the [User patching mechanism](https://wiki.gentoo.org/wiki//etc/portage/patches "/etc/portage/patches") so that these amendments are preserved when the package is next updated.

#### [The fundamentals]

The relevant Gentoo package is [[[x11-misc/xkeyboard-config]](https://packages.gentoo.org/packages/x11-misc/xkeyboard-config)[]]. Configuring a keyboard under X is more complicated than doing the same for a virtual console. The pertinent configuration files can be found in [/usr/share/X11/xkb] in these subdirectories:

[keycodes]

[geometry]

[types]

[symbols]

[compat]

[rules]

A fuller description of the files in these directories can be found at [An Unreliable Guide to XKB Configuration by Doug Palmer](https://www.charvolant.org/doug/xkb/html/index.html). It is a lot better than its name suggests. Further documentation can be found at xkeyboard-config\'s home page at [freedesktop.org](http://www.freedesktop.org/wiki/Software/XKeyboardConfig/).

Xkb gives keys names like \"\<AC01\>\" which means \"key in the **A**lphanumeric area, in row **C** (i.e. third row from the bottom, the row CapsLock is on), and key number **01**, the first key at the left of the row\". This key is [A] in an English layout. Keys in other areas have other names, such as \"\<FK05\>\" for [F5], or \"\<LCTL\>\" for the left control key.

#### [Adding key assignments]

As an example, this section will enhance the British English keyboard layout such that typing [a], [o], or [u] with [AltGr] will generate the German umlaut letters ä, ö, and ü. It should also do the Right Thing for the upper case versions. The keys to enhance are [A] (\<AC01\>), [O] (\<AD09\>) and [U] (\<AD07\>). (The character ß is already assigned to [AltGr]+[S].)

The names of the umlauted letters in xkb are \"adiaeresis\" and so on. These names can be found in the file [/usr/include/X11/keysymdef.h], though the leading \"XK\_\"s have to be removed to get the names.

Identify the right file in the [symbols] directory. Most of these files are named as two letter country codes (such as [gb] for Great Britain) so guess the one which matches the keyboard layout currently selected in X. In this example, [symbols/gb] is enhanced.

With the information above, create new entries by copying the existing scheme in [symbols/gb]. In this example, these entries should be added into the section called \"basic\". From its content, it is easy to guess that the four items in the braces and brackets within the entry for each key are for regular (without other key combinations), [Shift], [AltGr], and [Shift]+[AltGr] respectively:

[FILE] **`/usr/share/X11/xkb/symbols/gb`Typical key entry**

    key <AE02> ;

After making the additions, the section looks like this:

[FILE] **`/usr/share/X11/xkb/symbols/gb`Example for enhancing the British English keyboard**

    default  partial alphanumeric_keys
    xkb_symbols "basic" ;
        key <AE03>    ;
        key <AE04>    ;

        key <AC11>    ;
        key <TLDE>    ;

        key <BKSL>    ;
        key <LSGT>    ;

    // Keys inserted by ACM, 2015-10-23.
        key <AD07>  ;
        key <AD09>  ;
        key <AC01>  ;
    // End of insertion 2015-10-23
        include "level3(ralt_switch_multikey)"
    };

Having saved this file, restart X Windows. A typical desktop environment, XFCE, re-reads the above configuration files each time it starts. Should there be errors, error messages will be written to the normal [stderr] - if X Windows is started from the command line, [stderr] will be the virtual terminal it was started from.

#### [Adding actions to function keys]

As an example, add the actions \"switch to virtual terminal n\" (where n \> 12) to the function keys [F1] - [F12] when [Ctrl], [Alt], and [Shift] are all selected. The same effect should also occur when [AltGr] and [Fn] are selected.

First, search for the file in the [symbols] directory which handles the existing assignments for the Function keys. This file is [symbols/srvr_ctrl]. The entry in this file for [F1], which is intended to be modified, is:

[FILE] **`/usr/share/X11/xkb/symbols/srvr_ctrl`Existing entry for [F1]**

    key <FK01> ;

There are two things to note with this entry:

-   It is of type \"CTRL+ALT\"; it thus takes the standard four shift key settings with [Shift] and [AltGr], plus a fifth setting of [Ctrl]+[Alt]. Since the goal is to use [Ctrl]+[Alt]+[Shift], and there is no suitable existing type, a new one needs to be created.
-   The \"action\" `XF86_Switch_VT_1` is just a defined symbol in the xkb system. Its semantics are given to it by an entry in a file in the [compat] directory, namely [compat/xfree86]. There is no symbol `XF86_Switch_VT_13` (or higher) - instead, steal the otherwise unused existing symbols F13, F14, \..., F24.

##### [][Creating the new type CTRL+ALT+SHIFT]

Having located \"CTRL+ALT\" in [types/pc], it is easy enough to copy it, rename the copy to \"CTRL+ALT+SHIFT\" and extend this to allow the modifier key combination [Ctrl]+[Alt]+[Shift]. The result looks like this:

[FILE] **`/usr/share/X11/xkb/types/pc`Creating a new type**

    type "CTRL+ALT+SHIFT" ;

##### [][Activating the symbols F13, \..., F24]

The symbol `XF86_Switch_VT_1` is swiftly located in [compat/xfree86]. It is a simple matter to copy its form, creating assignments for the symbols F13, \..., F24. The definition for the first of these symbols, F13, in [compat/xfree86] then looks like:

[FILE] **`/usr/share/X11/xkb/compat/xfree86`Assigning an action to a symbol**

    interpret  F13 ;

Analogous definitions for F14, \..., F24 should also be put into the file.

##### [][Amending the entries in symbols for keys [F1], \..., [F12]]

Now that the new type CTRL+ALT+SHIFT and definitions for the symbols F13, \..., F24 are defined, amend the key definitions for the function keys in [symbols/srvr_ctrl]. The one for [F1] is mentioned below, analogous definitions also need to be inserted for the other function keys:

[FILE] **`/usr/share/X11/xkb/symbols/srvr_ctrl`Redefinition of function key**

    key <FK01> ;

After making these changes to [types/pc], [compat/xfree86], and [symbols/srvr_ctrl], and restarting the X server, switching from X directly to virtual terminals 13 and above is now possible - provided that these have been configured in the [/etc/inittab](https://wiki.gentoo.org/wiki/Handbook:AMD64/Working/Initscripts#How_init_works "Handbook:AMD64/Working/Initscripts") (or systemd equivalent) of course.

## [See also]

-   [Key repeat rate](https://wiki.gentoo.org/wiki/Key_repeat_rate "Key repeat rate") --- controls how quickly a key press on the keyboard will repeat if the key is pressed and held for a period of time.