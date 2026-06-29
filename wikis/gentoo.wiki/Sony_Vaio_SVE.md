[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=Sony_Vaio_SVE&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

[] This article has been flagged for not conforming to the [wiki guidelines](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Guidelines "Gentoo Wiki:Guidelines"). Please [help Gentoo out](https://wiki.gentoo.org/wiki/Help_improve_Gentoo_by_getting_involved_with_documentation!#Make_articles_conform_to_the_guidelines "Help improve Gentoo by getting involved with documentation!") by starting fixing things.

\"Chroot: illegal instruction\" for amd64. Architecture x86 is working excellent.

## Contents

-   [[1] [BIOS]](#BIOS)
-   [[2] [Backlight - screen brightness]](#Backlight_-_screen_brightness)
-   [[3] [Shift keys now working problem]](#Shift_keys_now_working_problem)
    -   [[3.1] [Console]](#Console)
    -   [[3.2] [Xorg]](#Xorg)
-   [[4] [Tested and works]](#Tested_and_works)
-   [[5] [Problems]](#Problems)

## [BIOS]

Winbond 25Q32CVSIG

Programming is not working.

## [Backlight - screen brightness]

    echo 255 > /sys/class/backlight/radeon_bl0/brightness

To set brightness at startup create udev rule to load brightness level:

[FILE] **`/etc/udev/rules.d/91-backlight.rules`udev event to load brightness at boot**

    # loading brightness
    ACTION=="add", SUBSYSTEM=="backlight", RUN+="/bin/sh -c 'echo 150 > /sys/class/backlight/radeon_bl0/brightness'"

## [Shift keys now working problem]

Solution is to bind any other key to Shift.

### [Console]

-   get key number:

<!-- -->

    # showkey

-   create file personal.map

<!-- -->

    keycode 86 = Shift Shift Shift Shift

-   load key assigment:

<!-- -->

    # loadkeys personal.map

can be placed in ̃/.bashrc file

### [Xorg]

    setxkbmap -option caps:shiftlock

or

    $ xmodmap .xmodmap

where .xmodmap:

    keycode 66 = Shift_L

you can get 66 with

    ̩$ xev

## [Tested and works]

-   Ethernet
-   Wifi
-   Touchpad
-   Audio
-   HDMI and HDMI Audio

## [Problems]

\- Function keys is not working