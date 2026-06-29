This page contains [[changes](https://wiki.gentoo.org/index.php?title=Keyd&oldid=1432208&diff=1432414)] which are not marked for translation.

Other languages:

-   [English]
-   [español](https://wiki.gentoo.org/wiki/Keyd/es "keyd (7% translated)")
-   [magyar](https://wiki.gentoo.org/wiki/Keyd/hu "keyd (66% translated)")

[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=Keyd&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

**Resources**

[[]][GitHub](https://github.com/rvaiya/keyd)

**keyd** is a key remapping daemon that allows the user to map keys per application and globally with support for both [Xorg](https://wiki.gentoo.org/wiki/Xorg "Xorg") and [Wayland](https://wiki.gentoo.org/wiki/Wayland "Wayland").

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [Kernel]](#Kernel)
    -   [[1.2] [Emerge]](#Emerge)
-   [[2] [Usage]](#Usage)
-   [[3] [Configuration cases for per application usage]](#Configuration_cases_for_per_application_usage)
    -   [[3.1] [Three keys like Alt+Shift+v]](#Three_keys_like_Alt.2BShift.2Bv)
    -   [[3.2] [Two action at one key]](#Two_action_at_one_key)
    -   [[3.3] [Chords]](#Chords)
    -   [[3.4] [Clear other layer]](#Clear_other_layer)
    -   [[3.5] [Switching between virtual consoles]](#Switching_between_virtual_consoles)
-   [[4] [Security concerns]](#Security_concerns)
    -   [[4.1] [Wayland security]](#Wayland_security)
-   [[5] [Example of running keyd-application-mapper with DEBUG in Wayland Sway with doas]](#Example_of_running_keyd-application-mapper_with_DEBUG_in_Wayland_Sway_with_doas)
-   [[6] [Example of configuration of Emacs keys for Firefox]](#Example_of_configuration_of_Emacs_keys_for_Firefox)
-   [[7] [See also]](#See_also)

## [Installation]

### [Kernel]

[keyd] relies on the uinput kernel module to create virtual input devices in userspace.

[KERNEL] **Enable support for keyd**

    Device Drivers --->
      Input device support --->
        -*- Generic input layer (needed for keyboard, mouse, ...) Search for <code>CONFIG_CONFIG_INPUT</code> to find this item. --->
          [*] Miscellaneous devices Search for <code>CONFIG_INPUT_MISC</code> to find this item.
            <M/*> User level driver support Search for <code>CONFIG_INPUT_UINPUT</code> to find this item.

### [Emerge]

[keyd] is currently only available on the [GURU](https://wiki.gentoo.org/wiki/GURU "GURU") [ebuild repository](https://wiki.gentoo.org/wiki/Ebuild_repository "Ebuild repository").

If the overlay is not enabled, run:

`root `[`#`]`eselect repository enable guru `

`root `[`#`]`emaint sync -r guru `

After activating the overlay, [keyd] can be installed:

`root `[`#`]`emerge --ask app-misc/keyd`

## [Usage]

There is global config file at [/etc/keyd/default.conf] that define \"layers\", are packs of keys, that may be activated sequentially or at the same time with keys that activate layer.

For per application usage there is separate config at [\~/.config/keyd/app.conf] that define layers per applications. In this layers you define additional keys to global. Key here may be double in form of \<layer\>.\<key\>.

Global configuration activated with \"keyd service\".

When using OpenRC add the service to the default runlevel.

`root `[`#`]`rc-update add keyd default `

`root `[`#`]`rc-service keyd start `

[keyd] distributed with \"keyd-application-mapper\" script for usage in window environment. Permission to group \"keyd\" should be granted with following command for user \"larry\":

`root `[`#`]`usermod -aG keyd larry `

## [Configuration cases for per application usage]

### [][Three keys like Alt+Shift+v]

There are two predefined layers here *alt* and *shift*. You should define global combined layer \"\[alt+shift\]\", after that you may use this as the name of the layer.

[FILE] **`.config/keyd/app.conf`**

    alt+shift.v = C-end

### [Two action at one key]

If you need several keys to be pressed you may use \"macro\" action with several expressions separated by space.

If you need some internal action like \"clear()\" you should look for \"clearm()\" action that execute expression before \"clear()\" call.

### [Chords]

Implemented with \"oneshot()\" action for example \"Ctrl+x key\":

[FILE] **`/etc/keyd/default.conf`**

    control.x = oneshot(<global layer with some key>)

### [Clear other layer]

Only \"clearm()\" working for current stable version, that breaks all layers.

### [Switching between virtual consoles]

We need to reset key\'s bindings of [keyd-application-mapper] script and made action of [Ctrl]+[Alt]+[Fn] keys. To switch between terminals we use [chvt] command from [[[sys-apps/busybox]](https://packages.gentoo.org/packages/sys-apps/busybox)[]].

`root `[`#`]`emerge --ask busybox`

[FILE] **`/etc/keyd/default.conf`Global**

    [control+alt]
    f6 = command(keyd bind reset && chvt 6)

## [Security concerns]

When a user is granted access to the keyd group, and thereby to /run/keyd.socket, which allows them to send keys system-wide, it creates a breach that may be exploited by any malicious program within that user\'s environment. This could potentially lead to elevated root access. This vulnerability affects all uinput-based applications that allow arbitrary keys to be sent from user space.

### [Wayland security]

This vulnerability may be closed if we run script as root with Wayland environment variables:

`user `[`$`]`sudo --preserve-env=WAYLAND_DISPLAY,XDG_RUNTIME_DIR /usr/bin/keyd-application-mapper `

For this command add sudo permission for current user:

[CODE] **Basic /etc/sudoers syntax**

    larry ALL=(root) SETENV:NOPASSWD:/usr/bin/keyd-application-mapper

Copy user configuration to root folder:

`root `[`#`]`mkdir -p /root/.config/keyd `

`root `[`#`]`cp /home/larry/.config/keyd/app.conf /root/.config/keyd/app.conf `

Withdraw permits by removing user from \"keyd\" group:

`root `[`#`]`gpasswd -d larry keyd `

## [Example of running [keyd-application-mapper] with DEBUG in Wayland Sway with doas]

[FILE] **`/etc/doas.conf`**

    permit setenv  nopass larry cmd /usr/bin/keyd-application-mapper

[FILE] **`/home/larry/.config/sway/config`**

    exec /bin/bash -c 'KEYD_DEBUG=True doas /usr/bin/keyd-application-mapper' >> /home/larry/.config/keyd/app.log &

## [Example of configuration of Emacs keys for Firefox]

[FILE] **`.config/keyd/app.conf`For Firefox**

    [firefox-esr|*]
    # Firefox
    alt.x = C-l
    alt.a = C-pageup
    alt.e = C-pagedown
    control.s = C-f
    # - Firefox built-in:
    # control.[ - back
    # control.] - forward
    # F3 - search forward
    # shift.F3 - search backward

    # - enter, escape
    control.g = clearm(escape)
    control.m = enter
    # - begin, end of string
    control.a = home
    control.e = end
    # - edit
    control.h = backspace
    control.d = delete
    control.l = left
    control.f = right
    control.n = down
    control.k = up
    alt.l = C-left
    alt.f = C-right
    control.slash = C-z
    # - scroll
    alt.v = pageup
    control.v = pagedown
    alt.z = up
    control.z = down
    # - copy, paste
    control.w = clearm(C-x)
    alt.w = clearm(C-c)
    control.y = clearm(C-v)
    alt.c = C-v
    # - selection mode - remember: C+h and C+d don't work with
    control.space = toggle(shift)
    control.c = clearm(C-c)

    # - select all
    control.x = oneshot(control_x)

[FILE] **`/etc/keyd/default.conf`Global**

    [ids]
    *

    # - Firefox copy text
    [control+alt]
    w = C-w

    [alt+shift]
    dot = C-end
    comma = C-home

    [control_x]
    h = C-a

## [See also]

-   [https://github.com/kawao/x-set-keys](https://github.com/kawao/x-set-keys)
-   [https://github.com/pyinput/python-uinput](https://github.com/pyinput/python-uinput)
-   [https://github.com/acro5piano/sway-remap](https://github.com/acro5piano/sway-remap)