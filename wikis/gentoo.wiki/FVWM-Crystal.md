**Resources**

[[]][Home](http://fvwm-crystal.sourceforge.net/)

[[]][Package information](https://packages.gentoo.org/packages/x11-themes/fvwm-crystal)

[[]][Wikipedia](https://en.wikipedia.org/wiki/FVWM-Crystal "wikipedia:FVWM-Crystal")

[[]][SourceForge](http://sourceforge.net/projects/fvwm-crystal/)

**FVWM-Crystal** is an easy to use, powerful and pretty desktop environment. It builds upon [FVWM](https://wiki.gentoo.org/wiki/FVWM "FVWM") and has some interesting features unique to Linux/UNIX desktops and also works on other Unix-like operating systems.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [Emerge]](#Emerge)
-   [[2] [Configuration]](#Configuration)
    -   [[2.1] [Additional software]](#Additional_software)
-   [[3] [Usage]](#Usage)
    -   [[3.1] [Preferences]](#Preferences)
    -   [[3.2] [Start-up]](#Start-up)
    -   [[3.3] [Applications menu]](#Applications_menu)
    -   [[3.4] [Full screen mode]](#Full_screen_mode)
-   [[4] [See also]](#See_also)
-   [[5] [External resources]](#External_resources)

## [Installation]

### [Emerge]

To install FVWM-Crystal:

`root `[`#`]`emerge --ask x11-themes/fvwm-crystal`

FVWM-Crystal depends on either [[[x11-misc/stalonetray]](https://packages.gentoo.org/packages/x11-misc/stalonetray)[]] or [[[x11-misc/trayer]](https://packages.gentoo.org/packages/x11-misc/trayer)[]] as a notification area manager; It\'s possible to install both and choose which one to use in the preferences. For *full support* with all recipes (FVWM-Crystal\'s themes) use stalonetray.

To set the wallpaper either [[[x11-misc/hsetroot]](https://packages.gentoo.org/packages/x11-misc/hsetroot)[]] or [[[media-gfx/feh]](https://packages.gentoo.org/packages/media-gfx/feh)[]] is needed. Hsetroot is a small tool to compose wallpapers for X, feh is a fast and powerful picture viewer.

## [Configuration]

### [Additional software]

There are a lot of optional programs you can install to improve your FVWM-Crystal experience:

-   A file manager: FVWM-Crystal can use any file manager as its desktop icon manager (with support for more than 10 different file managers built in and others can be selected via custom commands). 2 file managers can be used simultaneously.
-   A terminal emulator: at least one of gnome-terminal, konsole, xfce4-terminal, xterm, aterm, Eterm, mrxvt, urxvt (rxvt-unicode) or terminator.
-   Quake console: at least one of mrxvt, urxwt, aterm or xterm.
-   ROX-Filer (rox) or nautilus: for alternative ways to get icons on the desktop and wallpaper.
-   xscreensaver - a modular screen saver and locker.
-   sudo and optionally gksudo for running applications as root and reboot/shutdown.
-   A media player: at least one of Music Player Daemon (mpc), X MultiMedia System 2 (xmms2), alsaplayer, cmus, mocp, mplayer, mplayer2, quodlibet or cdcd.
-   A mixer application: at least one of aumix or alsamixer. With alsamixer, you will get true dB control.
-   transset and xcompmgr for full transparency support and the Bling bling clone.
-   xrandr for video mode switching.
-   pmount or pmount-gui for auto-mounting of removable USB and Firewire media. You may want to install uam too. autofs is a good alternative for auto-mounting of CDROM/DVD drives.
-   Xephyr (xorg-server with USE=\"kdrive xephyr\") for nested sessions.

It is possible to have a full featured FVWM-Crystal with auto-mounting support without udisks and its dependencies.

As a minimum, I will recommend you to install the following:

`root `[`#`]`emerge --ask mc pcmanfm rxvt-unicode xscreensaver alsaplayer mplayer alsamixer`

If you are having trouble with desktop icons, try installing xdg-user-dirs:

`root `[`#`]`emerge --ask xdg-user-dirs`

## [Usage]

FVWM-Crystal is very easy to use. There are a few man pages that can be accessed from the main menu or on the website. It is recommended that the Keyboard bindings be investigated; there are a large number.

### [Preferences]

All the preferences are available from the main [Crystal menu -\> Preferences]. They will be applied on the fly, with the exception of the Desktop manager which needs to restart X or when shifting between (or back and from) Nautilus and the Rox-Filer.

A few things are not in the preferences but in X resources files. You will find them in [/usr/share/fvwm-crystal/addons]. From that directory copy the following files:

`user `[`$`]`cp /usr/share/fvwm-crystal/addons/Xdefaults ~/.Xdefaults`

`user `[`$`]`cp /usr/share/fvwm-crystal/addons/Xresources ~/.Xresources`

You may edit them to suit your needs. They are used to determine the fonts, colors and geometry of the terminals. You may also define here you cursor theme. An X restart is necessary for changes in these files to apply.

FVWM-Crystal comes with several themes, called recipes. The exact memory usage of FVWM will depend mostly on the recipe in use, as well as its start time and a new recipe load. After the start there must be no speed difference between a thin recipe like Thin or Silent hacker, and an overloaded recipe like Amiga.

All the other preferences like the desktop geometry, the focus model, the windows decorations, the color theme, and so on, are fully independent of the recipe in use and applies to all of them.

The focus models are as follow:

-   Amiga: click to focus without raise
-   FVWM-Crystal: focus follow mouse without raise
-   FVWM-Crystal with raise: focus follow mouse with raise
-   MS Windows: click to focus with raise

Be also aware that when Privileged terminal is On, a terminal will never lose its focus. You can select which terminal emulator to use from the preferences, and launch it with a right-click on the desktop.

When On, Silent operation will add **2\>/dev/null** to most command launched by FVWM-Crystal. It is very useful if you want to debug Crystal and not be polluted by external applications in its log file.

### [Start-up]

To launch FVWM-Crystal, you can use a graphical login manager like gdm, but the preferred way is to use startx:

[FILE] **`~/.xinitrc`**

    #!/bin/sh
    xrdb ~/.Xdefaults
    exec /usr/bin/fvwm-crystal

When using elogind, you may need to have something like:

[FILE] **`~/.xinitrc`**

    #!/bin/sh
    xrdb ~/.Xdefaults
    exec dbus-launch --sh-syntax --exit-with-session fvwm-crystal

If you want to debug FVWM-Crystal or log its messages:

[FILE] **`~/.xinitrc`**

    #!/bin/sh
    xrdb ~/.Xdefaults
    exec /usr/bin/fvwm-crystal 2>.errors.fvwm-crystal

Note that all messages here will not necessarily come from FVWM-Crystal. You may find things like libpng warnings and messages from other programs.

You may want to use sudo to stop the computer or use the mount command from FVWM-Crystal. For a user called dom:

[FILE] **`/etc/sudoers.d/dom`**

    dom ALL=(ALL) NOPASSWD: /sbin/shutdown
    dom ALL=(ALL) NOPASSWD: /sbin/reboot
    dom ALL=(ALL) NOPASSWD: /sbin/halt
    dom ALL=(ALL) NOPASSWD: /bin/mount
    dom ALL=(ALL) NOPASSWD: /bin/umount

### [Applications menu]

FVWM-Crystal has its own applications menu with full support for the xdg additional categories. It work in 2 steps.

First, it comes with a extensive database of menu entries and icons. The Application database helps explain in detail how it works and how you can customize it. Take also a look at the existing entries, they will show you the way.

Second, you can generate the missing entries by running from the main menu FVWM-Crystal -\> Preferences -\> Generate application menu. For that, a script will scan the desktop files provided by the applications and generate the missing entries. It will use the categories found in these desktop files. New entries will be in [\~/.fvwm-crystal/Applications] and the new icons in [\~/.fvwm-crystal/icons].

### [Full screen mode]

You can put almost any application into full screen mode. For that use [Alt] + [Numpad_Multiply] ([Alt] + [\*] on the Numpad). This will toggle the focused window.

[Alt] + [Shift] + [F] will toggle all the windows on the current desktop page. With [Alt] + [Shift] + [Numpad_Multiply], you can scroll between the full screened windows and the current desktop page. Numpad\_. and Numpad_0 is another way to scroll between windows, try it. There are also [Alt] + [Tab] which emulate the windows task list, and [Alt] + [Shift] + [Tab] which do the same for the iconic windows.

There are also other key bindings relative to window placement, e.g., [Alt] + [Shift] + \[1 to 0\]. For instance, if you have a few firefox windows on the same screen, you can do the following sequence and see what happens:

[Ctrl] + [Shift] + [2]; [Ctrl] + [Shift] + [F]; [Ctrl] + [Shift] + [Numpad_Multiply] a few times; [Ctrl] + [Shift] + [F]

Do read the Keyboard bindings documentation because some functions are only available via key bindings, for example the Expose clone via [Alt] + [E].

## [See also]

-   [Desktop environment](https://wiki.gentoo.org/wiki/Desktop_environment "Desktop environment") --- provides a list of desktop environments available in Gentoo.
-   [FVWM](https://wiki.gentoo.org/wiki/FVWM "FVWM") --- a stacking [window manager](https://wiki.gentoo.org/wiki/Window_manager "Window manager") for [Xorg](https://wiki.gentoo.org/wiki/Xorg "Xorg").

## [External resources]

-   [FVWM-Crystal live ebuild](http://svnweb.tuxfamily.org/listing.php?repname=proaudio%2Fproaudio&path=%2Ftrunk%2Foverlays%2Fproaudio%2Fx11-themes%2Ffvwm-crystal%2F&language=en)
-   [Gentoo forum thread](https://forums.gentoo.org/viewtopic-p-7490076.html)
-   [Forum thread in French](https://forums.gentoo.org/viewtopic-t-959584-highlight-.html)