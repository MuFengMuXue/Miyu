This article is written for the Logitech G15 but it should work with other keyboards in the G-series produced by Logitech.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [Kernel]](#Kernel)
    -   [[1.2] [Portage]](#Portage)
    -   [[1.3] [Emerge]](#Emerge)
-   [[2] [Configuration]](#Configuration)
    -   [[2.1] [Xorg]](#Xorg)
    -   [[2.2] [Service]](#Service)
        -   [[2.2.1] [OpenRC]](#OpenRC)
-   [[3] [Usage]](#Usage)
    -   [[3.1] [Multimedia keys]](#Multimedia_keys)
    -   [[3.2] [G & M keys]](#G_.26_M_keys)
-   [[4] [See also]](#See_also)
-   [[5] [External resources]](#External_resources)

## [Installation]

### [Kernel]

g15daemon requires user level driver support.

[KERNEL]

    Device Drivers --->
      Input Device support --->
        [*]   Miscellaneous devices --->
                <*>   User level driver support

### [Portage]

To get other applications to know about the G15 keyboard, add the following to [/etc/portage/make.conf].

[FILE] **`/etc/portage/make.conf`**

    LCD_DEVICES="g15"
    USE="g15 lcd"

### [Emerge]

Install [[[app-misc/g15daemon]](https://packages.gentoo.org/packages/app-misc/g15daemon)[]] for the multimedia keys and LCD display, and [[[app-misc/g15macro]](https://packages.gentoo.org/packages/app-misc/g15macro)[]] for the [M\^] and [G\^] keys.

`root `[`#`]`emerge --ask app-misc/g15daemon app-misc/g15macro`

## [Configuration]

After installing g15daemon and g15macro, check the g15daemon configuration file before starting the service. Normally the default values should work.

** Note**\
Note the 24-hour clock format in [/etc/g15daemon.conf]

[FILE] **`/etc/g15daemon.conf`**

    # G15Daemon Configuration File
    # any items entered before a [section] header
    # will be in the Global config space
    # comments you wish to keep should start with a semicolon';'

    [Global]
    Use MR as Cycle Key: Off

    [PLUGIN_LOAD_ORDER]
    0: g15plugin_uinput.so
    1: g15plugin_clock.so
    2: g15plugin_tcpserver.so
    TotalPlugins: 3

    [PLUGINS]
    Linux UINPUT Keyboard Output: Load
    Clock: Load
    LCDServer: Load

    [Keyboard OS Mapping (uinput)]
    device: /dev/input/uinput
    Lkeys.mapped: 0

    [Clock]
    24hrFormat: On
    ShowDate: On
    Digital: On

### [Xorg]

Optionally add the following to [/etc/X11/[xorg.conf](https://wiki.gentoo.org/wiki/Xorg.conf "Xorg.conf")]:

[FILE] **`/etc/X11/xorg.conf`**

    Option         "XkbModel" "logitech_g15"

### [Service]

#### [OpenRC]

Configure the g15daemon service configuration file:

[FILE] **`/etc/conf.d/g15daemon`**

    # Key to switch the client-screens. Default is the MR key,
    # Set to "yes" to use L1 key instead (black round key below the LCD, above the multimedia keys).
    CLIENT_SWITCH_L1="no"

    # Set to "yes" to switch off the lcd backlight when stopping g15daemon.
    BACKLIGHT_OFF="no"

To start g15daemon:

`root `[`#`]`rc-service g15daemon start`

To start g15daemon at boot:

`root `[`#`]`rc-update add g15daemon default`

If everything worked correctly a clock should be visible on the G15 LCD display.

## [Usage]

### [Multimedia keys]

To have the new keys working in X11, create a specific xmodmap in your home directory or edit an existing one.

Create the xmodmap:

`user `[`$`]`cp /usr/share/g15daemon/contrib/xmodmaprc ~/.Xmodmap`

Adding keycodes to an existing xmodmap:

`user `[`$`]`cat /usr/share/g15daemon/contrib/xmodmaprc >> ~/.Xmodmap`

To get the new keys you might need to restart your session or run:

`user `[`$`]`xmodmap ~/.Xmodmap`

To check if your keys have been mapped correctly you can test them with [[[x11-apps/xev]](https://packages.gentoo.org/packages/x11-apps/xev)[]].

### [][G & M keys]

To get your [G\^] and [M\^] keys to work you need to start up g15macro, preferably you should make it start automatically with the rest of your desktop.

`user `[`$`]`/usr/bin/g15macro &`

Your extra keys should now be working and you should be able to record macro keys by pushing the [MR] key.

## [See also]

[Sidewinderd](https://wiki.gentoo.org/wiki/Sidewinderd "Sidewinderd") --- a user space daemon that enables special keys and macro recording for various Logitech and Microsoft gaming peripherals.

## [External resources]

-   [LogitechG15 - Ubuntu Community Wiki](https://help.ubuntu.com/community/LogitechG15)