[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=Compose_key&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

**Resources**

[[]][Wikipedia](https://en.wikipedia.org/wiki/Compose_key "wikipedia:Compose key")

The **Compose key**, also known as *Multi_key* on the X Window System, allows one to combine several keys into one character (e.g. [compose] [o] [/] to form ø, or [compose] [=] [e] to form €).

## Contents

-   [[1] [Configuration]](#Configuration)
    -   [[1.1] [Xorg]](#Xorg)
    -   [[1.2] [Wayland]](#Wayland)
        -   [[1.2.1] [Sway]](#Sway)
    -   [[1.3] [Key combinations]](#Key_combinations)
-   [[2] [See also]](#See_also)
-   [[3] [External resources]](#External_resources)

## [Configuration]

Note: there is no compose key defined by default.

### [Xorg]

The user can specify it in `XkbOptions`:

[FILE] **`/etc/X11/xorg.conf.d/keyboard.conf`**

    Section "InputClass"
            Identifier          "Keyboard0"
            MatchIsKeyboard     "on"
            Option "XkbLayout"  "us,ru"
            Option "XkbOptions" "grp:alt_shift_toggle,compose:rctrl"
    EndSection

...or through graphical front-ends such as [[[x11-misc/qxkb]](https://packages.gentoo.org/packages/x11-misc/qxkb)[]]

Note that not every key can be assigned as the Compose key. To see a list of keys that **can** be used:

`user `[`$`]`grep "compose:" /usr/share/X11/xkb/rules/base.lst`

[FILE] **`/usr/share/X11/xkb/rules/base.lst`**

      compose:ralt         Right Alt
      compose:lwin         Left Win
      compose:lwin-altgr   3rd level of Left Win
      compose:rwin         Right Win
      compose:rwin-altgr   3rd level of Right Win
      compose:menu         Menu
      compose:menu-altgr   3rd level of Menu
      compose:lctrl        Left Ctrl
      compose:lctrl-altgr  3rd level of Left Ctrl
      compose:rctrl        Right Ctrl
      compose:rctrl-altgr  3rd level of Right Ctrl
      compose:caps         Caps Lock
      compose:caps-altgr   3rd level of Caps Lock
      compose:102          The "&lt; &gt;" key
      compose:102-altgr    3rd level of the "&lt; &gt;" key
      compose:paus         Pause
      compose:ins          Insert
      compose:prsc         PrtSc
      compose:sclk         Scroll Lock

### [Wayland]

#### [Sway]

To set the compose key to **Right Control**, update your Sway config with:

[FILE] **`~/.config/sway/config`**

    ...
    input * xkb_options compose:rctrl
    ...

### [Key combinations]

See the [Arch wiki](https://wiki.archlinux.org/title/Xorg/Keyboard_configuration#Key_combinations) for how to list and modify key combinations.

## [See also]

-   [Input_methods/key_sequence](https://wiki.gentoo.org/wiki/Input_methods/key_sequence "Input methods/key sequence")
-   [Keyboard_layout_switching#X11](https://wiki.gentoo.org/wiki/Keyboard_layout_switching#X11 "Keyboard layout switching")
-   [Xorg/Guide#Configuring_the_keyboard](https://wiki.gentoo.org/wiki/Xorg/Guide#Configuring_the_keyboard "Xorg/Guide")

## [External resources]

-   [ArchWiki XKB article](https://wiki.archlinux.org/index.php/XKB)
-   [ArchWiki Keyboard configuration](https://wiki.archlinux.org/index.php/Xorg/Keyboard_configuration#Configuring_compose_key)