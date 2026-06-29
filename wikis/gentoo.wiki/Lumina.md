This page contains [[changes](https://wiki.gentoo.org/index.php?title=Lumina&oldid=1233600&diff=1429038)] which are not marked for translation.

Other languages:

-   [English]
-   [magyar](https://wiki.gentoo.org/wiki/Lumina/hu "Lumina (100% translated)")
-   [日本語](https://wiki.gentoo.org/wiki/Lumina/ja "Lumina (100% translated)")

**[] Archived article**\
\
This article is **archived (obsolete)**. Contents are surely incorrect for current usage, and are intended for historical reference only.

Lumina [removed Dec 21, 2025](https://gitweb.gentoo.org/repo/gentoo.git/commit/?id=b151bb07f558599bd05fbdf0eb3084325d207134) - dead upstream.

\
TLDR: **Do not use this article!**

**Resources**

[[]][Home](https://lumina-desktop.org/)

[[]][Package information](https://packages.gentoo.org/packages/x11-wm/lumina)

[[]][Wikipedia](https://en.wikipedia.org/wiki/Lumina_(desktop_environment) "wikipedia:Lumina (desktop environment)")

[[]][Official documentation](http://www.lumina-desktop.org/handbook/)

[[]][Bugs (upstream)](https://github.com/trueos/lumina/issues)

[[]][GitHub](https://github.com/trueos/lumina)

**Lumina** is a lightweight [desktop environment](https://wiki.gentoo.org/wiki/Desktop_environment "Desktop environment"), free of [D-Bus](https://wiki.gentoo.org/wiki/D-Bus "D-Bus") and \*kit, designed to have as few system dependencies and requirements as possible.

## Contents

-   [[1] [Installation]](#Installation)
-   [[2] [Configuration]](#Configuration)
-   [[3] [Invocation]](#Invocation)
-   [[4] [External resources]](#External_resources)

## [Installation]

The [[[x11-wm/lumina]](https://packages.gentoo.org/packages/x11-wm/lumina)[]] package is configurable by one [USE flag](https://wiki.gentoo.org/wiki/USE_flag "USE flag"):

\
To install Lumina desktop, run:

`root `[`#`]`emerge --ask x11-wm/lumina`

## [Configuration]

A configuration file is installed in [/etc/luminaDesktop.conf]. Lumina also has a bunch of own configuration tools.

## [Invocation]

Lumina provides its own replacement for [startx](https://wiki.gentoo.org/wiki/Xorg/Guide#Using_startx "Xorg/Guide") to be started from console.

`user `[`$`]`start-lumina-desktop`

Alternatively it can be added to the [\~./xinitrc] file for being started via [startx](https://wiki.gentoo.org/wiki/Xorg/Guide#Using_startx "Xorg/Guide") or a [display manager](https://wiki.gentoo.org/wiki/Display_manager "Display manager")

[FILE] **`~/.xinitrc`**

    [[ -f ~/.Xresources ]] && xrdb -merge -I$HOME ~/.Xresources
    exec start-lumina-desktop

## [External resources]

-   [Official webpage](https://lumina-desktop.org/)