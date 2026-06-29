Other languages:

-   [English]
-   [magyar](https://wiki.gentoo.org/wiki/Bspwm/hu "Bspwm (9% translated)")

**Resources**

[[]][Package information](https://packages.gentoo.org/packages/x11-wm/bspwm)

[[]][GitHub](https://github.com/baskerville/bspwm)

[[]][[#bspwm](ircs://irc.libera.chat/#bspwm)] ([[webchat](https://web.libera.chat/#bspwm)])

[![Ohloh Logo](/images/thumb/c/c1/Ohloh-logo.png/30px-Ohloh-logo.png)][Open Hub](https://www.openhub.net/p/bspwm)

**bspwm** is a lightweight, tiling, minimalist [window manager](https://wiki.gentoo.org/wiki/Window_manager "Window manager") written in C, which organizes its windows as nodes of a binary tree. Its installed size is less than 600 KB (even with the [[[examples]](https://packages.gentoo.org/useflags/examples)[[]](https://wiki.gentoo.org/wiki/USE_flag "USE flag")] [USE flag](https://wiki.gentoo.org/wiki/USE_flag "USE flag") set). It only responds to X events and messages it receives on a dedicated socket from a program included in its package, [bspc].

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
-   [[2] [Configuration]](#Configuration)
    -   [[2.1] [Autostart programs]](#Autostart_programs)
        -   [[2.1.1] [Alternative Way]](#Alternative_Way)
    -   [[2.2] [Hide/Show windows]](#Hide.2FShow_windows)
-   [[3] [Additional software]](#Additional_software)
    -   [[3.1] [dmenu]](#dmenu)
    -   [[3.2] [Terminal emulators]](#Terminal_emulators)
        -   [[3.2.1] [st aka suckless/simple terminal]](#st_aka_suckless.2Fsimple_terminal)
        -   [[3.2.2] [rxvt-unicode aka urxvt]](#rxvt-unicode_aka_urxvt)
    -   [[3.3] [i3lock]](#i3lock)
    -   [[3.4] [File managers]](#File_managers)
        -   [[3.4.1] [ranger]](#ranger)
-   [[4] [See also]](#See_also)
-   [[5] [External resources]](#External_resources)

## [[] Installation]

### [[] USE flags]

### [USE flags for] [x11-wm/bspwm](https://packages.gentoo.org/packages/x11-wm/bspwm) [[]] [Tiling window manager based on binary space partitioning]

  ------------------------------------------------------------- ---------------------------------------
  [`examples`](https://packages.gentoo.org/useflags/examples)   Install examples, usually source code
  ------------------------------------------------------------- ---------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2025-11-08 08:09] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [[] Emerge]

To install [bspwm] using Portage merely issue the command:

`root `[`#`]`emerge --ask x11-wm/bspwm`

[sxhkd] is used for keybindings and pointer bindings so one may wish to install it too:

`root `[`#`]`emerge --ask x11-misc/sxhkd`

## [[] Configuration]

If [bspwm] was installed with the `examples` USE flag enabled, proper configuration is necessary.

First create the necessary directories that will hold the configuration files. Since [bspwm] does not manage keyboard or pointer inputs, it utilizes [[[x11-misc/sxhkd]](https://packages.gentoo.org/packages/x11-misc/sxhkd)[]] (Simple X hotkey daemon) for this purpose. Consequently, we will need a configuration file for [[[x11-misc/sxhkd]](https://packages.gentoo.org/packages/x11-misc/sxhkd)[]], as it will house all of your key bindings.

`user `[`$`]`mkdir -vp ~/.config/bspwm ~/.config/sxhkd`

Now copy the sample configuration files from [/usr/share/doc/bspwm-0.9.10/examples/] and, if required, extract them:

`user `[`$`]`cp -v /usr/share/doc/bspwm-0.9.10/examples/bspwmrc.* ~/.config/bspwm/ `

`user `[`$`]`cp -v /usr/share/doc/bspwm-0.9.10/examples/sxhkdrc.* ~/.config/sxhkd/ `

If the configuration files are compressed, extract them using the applicable command for the compression format. For instance, if the files are compressed using [zstd] ([.zst] files), use the command:

`user `[`$`]`zstd -vd ~/.config/bspwm/bspwmrc.zst `

`user `[`$`]`zstd -vd ~/.config/sxhkd/sxhkdrc.zst `

The compressed files can then be removed:

`user `[`$`]`rm -v ~/.config/bspwm/bspwm/bspwm.zst `

`user `[`$`]`rm -v ~/.config/sxhkd/sxhkdrc.zst `

Adapt the above commands for the particular compression format used by Portage.

** Note**\
Ensure that the [bspwm] configuration file is executable. If it is not, one must make it executable by running the command [chmod +x \~/.config/bspwm/bspwmrc].

### [[] Autostart programs]

If there are specific programs that need to be started after logging in on the workstation, such as [[[net-misc/dropbox]](https://packages.gentoo.org/packages/net-misc/dropbox)[]] and [[[media-gfx/feh]](https://packages.gentoo.org/packages/media-gfx/feh)[]], one can achieve this by starting them in the bspwm configuration file:

[FILE] **`~/.config/bspwm/bspwmrc`bspwm configuration file**

    # autostart programs
    dropbox
    feh --bg-scale ~/.config/my_wallpaper.png
    $/.config/polybar/launch.sh

#### [[] Alternative Way]

Another way to autostart programs once [bspwm] has started is to make a specialized file containing every program that should autostart and then including that file into [bspwmrc]. In some specific cases, this way of autostarting programs may fix issues that may have probably arosen from the method mentioned above.

[FILE] **`~/.config/bspwm/autostart`Custom autostart file**

    #!/bin/bash
    dropbox &
    feh --bg-scale ~/.config/my_wallpaper.png &
    $/.config/polybar/launch.sh &

** Note**\
The autostart file must also be executable. This can be achieved by running: [chmod +x \~/.config/bspwm/autostart]

Then, the file should be included in [bspwmrc].

[FILE] **`~/.config/bspwm/bspwmrc`Including the custom autostart file**

    # Other stuff....

    ~/.config/bspwm/autostart &

### [][[] Hide/Show windows]

Some programs may have tray icons, and users may wish to replicate the *minimize* behavior (referred to as *hide* in the bspwm environment). This can be achieved by configuring a keyboard shortcut. It is important to note that when restoring these hidden windows, they will reappear on the same monitor where they were initially hidden.

[FILE] **`~/.config/sxhkd/sxhkdrc`sxhkd configuration file**

    # hide window
    super + v
      bspc node -g hidden

    # unhide window
    super + shift + v
      bspc node  -g hidden=off

## [Additional software]

### [[] dmenu]

A dynamic menu designed for X initially developed for [dwm](https://wiki.gentoo.org/wiki/Dwm "Dwm"). Primarily focused on launching programs, but it can also be configured to perform other tasks.

### [USE flags for] [x11-misc/dmenu](https://packages.gentoo.org/packages/x11-misc/dmenu) [[]] [a generic, highly customizable, and efficient menu for the X Window System]

  ------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------
  [`savedconfig`](https://packages.gentoo.org/useflags/savedconfig)   Use this to restore your config from /etc/portage/savedconfig \$/\$. Make sure your USE flags allow for appropriate dependencies
  [`xinerama`](https://packages.gentoo.org/useflags/xinerama)         Add support for querying multi-monitor screen geometry through the Xinerama API
  ------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2025-09-13 21:16] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

To assign a keyboard shortcut for launching [dmenu]:

[FILE] **`~/.config/sxhkd/sxhkdrc`sxhkd configuration file**

    # program launcher
    super + space
      dmenu_run

### [[] Terminal emulators]

#### [][[] st aka suckless/simple terminal]

**[st](https://wiki.gentoo.org/wiki/St "St")** is an extremely minimal terminal emulator developed by the developers of dmenu.

### [USE flags for] [x11-terms/st](https://packages.gentoo.org/packages/x11-terms/st) [[]] [Simple terminal implementation for X]

  ------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------
  [`savedconfig`](https://packages.gentoo.org/useflags/savedconfig)   Use this to restore your config from /etc/portage/savedconfig \$/\$. Make sure your USE flags allow for appropriate dependencies
  ------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2025-12-01 09:47] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

To install it, just issue the command:

`root `[`#`]`emerge --ask x11-terms/st`

To enable a keyboard shortcut for launching the terminal

[FILE] **`~/.config/sxhkd/sxhkdrc`sxhkd configuration file**

    # terminal emulator
    super + Return
      st

#### [[] rxvt-unicode aka urxvt]

**[urxvt](https://wiki.gentoo.org/wiki/Rxvt-unicode "Rxvt-unicode")** is another alternative, although it lacks full Unicode support and you *might* have some issues with Powerline Fonts.

### [USE flags for] [x11-terms/rxvt-unicode](https://packages.gentoo.org/packages/x11-terms/rxvt-unicode) [[]] [rxvt clone with xft and unicode support]

  ------------------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [`+font-styles`](https://packages.gentoo.org/useflags/+font-styles)                   Enable support for bold and italic fonts
  [`+mousewheel`](https://packages.gentoo.org/useflags/+mousewheel)                     Enable scrolling via mouse wheel or buttons 4 and 5
  [`24-bit-color`](https://packages.gentoo.org/useflags/24-bit-color)                   Enable 24-bit color support. Note that this feature is unofficial, may cause visual glitches due to the fact there is no termcap/terminfo definition for rxvt-unicode-24bit yet so it is necessary to use the one for 256 colours, visibly increases memory usage, and might slow urxvt down dramatically when more than six fonts are in use in a terminal instance.
  [`256-color`](https://packages.gentoo.org/useflags/256-color)                         Enable 256 color support
  [`blink`](https://packages.gentoo.org/useflags/blink)                                 Enable blinking text
  [`fading-colors`](https://packages.gentoo.org/useflags/fading-colors)                 Enable colors fading when off focus
  [`gdk-pixbuf`](https://packages.gentoo.org/useflags/gdk-pixbuf)                       Enable transparency support using x11-libs/gdk-pixbuf
  [`iso14755`](https://packages.gentoo.org/useflags/iso14755)                           Enable ISO-14755 support
  [`perl`](https://packages.gentoo.org/useflags/perl)                                   Enable perl script support. You can still disable this at runtime with -pe \"\"
  [`startup-notification`](https://packages.gentoo.org/useflags/startup-notification)   Enable application startup event feedback mechanism
  [`unicode3`](https://packages.gentoo.org/useflags/unicode3)                           Use 21 instead of 16 bits to represent unicode characters
  [`wide-glyphs`](https://packages.gentoo.org/useflags/wide-glyphs)                     Enable support for wide glyphs, required for certain symbol/icon fonts to display correctly. Note that this feature is \*unofficial\* and has been observed to cause stability issues for some users.
  [`xft`](https://packages.gentoo.org/useflags/xft)                                     Build with support for XFT font renderer (x11-libs/libXft)
  ------------------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-01-20 01:35] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

You can install it issuing the command:

`root `[`#`]`emerge --ask x11-terms/rxvt-unicode`

### [[] i3lock]

Locking your screen is always recommended in order to avoid unauthorized access to your Workstation

### [USE flags for] [x11-misc/i3lock](https://packages.gentoo.org/packages/x11-misc/i3lock) [[]] [Simple screen locker]

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-05-26 00:28] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

You can install it by issuing the command:

`root `[`#`]`emerge --ask x11-misc/i3lock`

In order to assign a keyboard shortcut for locking your screen, you should update your configuration file

[FILE] **`~/.config/sxhkd/sxhkdrc`sxhkd configuration file**

    # lock the screen with a dark background
    super + q
      i3lock -c 000000

### [[] File managers]

#### [ranger]

[ranger](https://wiki.gentoo.org/wiki/Ranger "Ranger") is a console file manager with VI key bindings. It provides a minimalistic and nice curses interface with a view on the directory hierarchy. It ships with [rifle], a file launcher that is good at automatically finding out which program to use for what file type.

You can install [ranger] via

`root `[`#`]`emerge --ask app-misc/ranger`

If you want to tune [ranger] with your own settings:

Start [ranger] and exit so that it creates the directory structure for its configuration files.

`user `[`$`]`ranger `

`user `[`$`]`Q `

Now copy the configuration files:

`user `[`$`]`ranger --copy-config=all`

    creating: /home/user/.config/ranger/apps.py
    creating: /home/user/.config/ranger/commands.py
    creating: /home/user/.config/ranger/rc.conf
    creating: /home/user/.config/ranger/options.py
    creating: /home/user/.config/ranger/scope.sh

## [[] See also]

-   [JWM](https://wiki.gentoo.org/wiki/JWM "JWM") --- an extremely lightweight [window manager](https://wiki.gentoo.org/wiki/Window_manager "Window manager") for the [X](https://wiki.gentoo.org/wiki/X "X") window system.
-   [XFCE](https://wiki.gentoo.org/wiki/XFCE "XFCE") --- a lightweight [desktop environment](https://wiki.gentoo.org/wiki/Desktop_environment "Desktop environment") built to be fast, good looking, and user friendly.

## [[] External resources]

-   [ranger](https://github.com/ranger/ranger/wiki) file manager official wiki
-   [Installing and Using Ranger, a Terminal File Manager](https://www.digitalocean.com/community/tutorials/installing-and-using-ranger-a-terminal-file-manager-on-a-ubuntu-vps) by Justin Ellingwood on DigitalOcean tutorials
-   [hide/show bspwm windows](https://www.reddit.com/r/bspwm/comments/99xzae/is_there_any_way_to_minimizemaximize_windows/e4rsh2l/) on Reddit