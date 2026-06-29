**[] Deprecated article**\
\

This article is **deprecated (obsolete)**. Contents are [no longer relevant], and are intended for historical reference only!

\
TLDR: **Do not use this article!**

**Resources**

[[]][Home](http://www.compiz.org)

[[]][Wikipedia](https://en.wikipedia.org/wiki/Compiz "wikipedia:Compiz")

** Note**\
Compiz is outdated and is not available in Gentoo. A replacement is available for wayland with [Wayfire](https://wiki.gentoo.org/wiki/Wayfire "Wayfire")

Information on this page is outdated and at least needs to be updated with information for release 2.4.1 and newer.

**Compiz** is an open-source compositing [window manager](https://wiki.gentoo.org/wiki/Window_manager "Window manager") for [X11](https://wiki.gentoo.org/wiki/X11 "X11").

## Contents

-   [[1] [Install]](#Install)
    -   [[1.1] [Preinstall]](#Preinstall)
    -   [[1.2] [Backend]](#Backend)
    -   [[1.3] [Emerge]](#Emerge)
-   [[2] [Setup]](#Setup)

## [Install]

### [Preinstall]

First compiz must be keyworded in, and USE flags set to pull in emerald:

[FILE] **`/etc/portage/package.accept_keywords`Emerald package.accept_keywords example**

    x11-plugins/compiz-plugins-main
    x11-libs/compiz-bcop
    x11-wm/compiz-fusion
    x11-plugins/compiz-plugins-extra
    x11-libs/libcompizconfig
    x11-wm/compiz
    dev-python/compizconfig-python
    x11-libs/compizconfig-backend-gconf
    x11-wm/emerald
    x11-themes/emerald-themes
    x11-apps/fusion-icon
    x11-misc/ccsm

[FILE] **`/etc/portage/package.use`Emerald package.use example**

    x11-wm/compiz-fusion emerald

### [Backend]

Install a backend that is appropriate for the system. Failure to do so might result in unstable compiz behavior. Possible backends include:

`root `[`#`]`emerge --ask x11-libs/compizconfig-backend-gconf`

or

`root `[`#`]`emerge --ask x11-libs/compizconfig-backend-kconfig4`

### [Emerge]

`root `[`#`]`emerge --ask compiz-fusion fusion-icon ccsm`

## [Setup]

Press [Alt] + [F2]. Enter \"fusion-icon\". Then run.

Right click the fusion-icon and select [settings manager].

Some options must be selected since ccsm\'s default configuration is empty. These should help set the system to be configured correctly.

Turn on

\"Effects\"

    Window Decoration

\"window management\"

    Move Window, Resize Window, & Application Switcher