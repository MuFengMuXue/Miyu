**Resources**

[[]][Home](https://xmonad.org/)

[[]][Wikipedia](https://en.wikipedia.org/wiki/Xmonad "wikipedia:Xmonad")

**xmonad** is a fast and lightweight tiling [window manager](https://wiki.gentoo.org/wiki/Window_manager "Window manager") for [X11](https://wiki.gentoo.org/wiki/X11 "X11"), written, configured, and extended in the purely-functional programming language [Haskell](https://wiki.gentoo.org/wiki/Haskell "Haskell").

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
    -   [[1.3] [Cabal (unsupported)]](#Cabal_.28unsupported.29)
-   [[2] [Configuration]](#Configuration)
    -   [[2.1] [Starting]](#Starting)
    -   [[2.2] [\~/.xmonad/xmonad.hs]](#.7E.2F.xmonad.2Fxmonad.hs)
    -   [[2.3] [Adding status bars]](#Adding_status_bars)
        -   [[2.3.1] [xmobar]](#xmobar)
        -   [[2.3.2] [dzen]](#dzen)
-   [[3] [External resources]](#External_resources)

## [Installation]

### [USE flags]

### [USE flags for] [x11-wm/xmonad](https://packages.gentoo.org/packages/x11-wm/xmonad) [[]] [A tiling window manager]

  --------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------
  [`doc`](https://packages.gentoo.org/useflags/doc)                                 Add extra documentation (API, Javadoc, etc). It is recommended to enable per package instead of globally
  [`hscolour`](https://packages.gentoo.org/useflags/hscolour)                       Include coloured haskell sources to generated documentation (dev-haskell/hscolour)
  [`no-autorepeat-keys`](https://packages.gentoo.org/useflags/no-autorepeat-keys)   Allow ignoring of keyboard autorepeat.
  [`profile`](https://packages.gentoo.org/useflags/profile)                         Add support for software performance analysis (will likely vary from ebuild to ebuild)
  [`test`](https://packages.gentoo.org/useflags/test)                               Enable dependencies and/or preparations necessary to run tests (usually controlled by FEATURES=test but can be toggled independently)
  --------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2025-05-21 12:51] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

There are two ways to install XMonad. The Gentoo recommended method is to use Portage so that the package will be integrated into the system\'s package database.

### [Emerge]

Merge the [[[x11-wm/xmonad]](https://packages.gentoo.org/packages/x11-wm/xmonad)[]] package:

`root `[`#`]`emerge --ask x11-wm/xmonad`

### [][Cabal (unsupported)]

It is possible to install using [cabal](https://wiki.gentoo.org/wiki/Haskell#Cabal "Haskell"), although it is not the Gentoo recommended method for installation system-wide packages. When choosing this route proceed with caution (Portage will not track xmonad)!

`user `[`$`]`cabal install xmonad`

## [Configuration]

### [Starting]

Start xmonad using a [display manager](https://wiki.gentoo.org/wiki/Display_manager "Display manager") or the [startx] command.

If want to use startx and want [elogind](https://wiki.gentoo.org/wiki/Elogind "Elogind") support, create the following file:

[FILE] **`~/.xinitrc`**

    exec dbus-launch --sh-syntax --exit-with-session xmonad

### [][\~/.xmonad/xmonad.hs]

XMonad itself can be configured through [\~/.xmonad/xmonad.hs] which is written in Haskell.

Minimal configuration file with default configuration:

[CODE] **Primitive xmonad.hs**

    import XMonad

    main = xmonad $ def

Once you changed your config file you should compile it and restart XMonad.

`user `[`$`]`xmonad --recompile `

`user `[`$`]`xmonad --restart `

In most cases to write a config file you need additional features provided by the xmonad-contrib library. You can install it from [[[x11-wm/xmonad-contrib]](https://packages.gentoo.org/packages/x11-wm/xmonad-contrib)[]]

`root `[`#`]`emerge --ask xmonad-contrib`

OR using [cabal](https://wiki.gentoo.org/wiki/Haskell#Cabal "Haskell"):

`user `[`$`]`cabal install xmonad-contrib`

### [Adding status bars]

Unlike many other window managers, XMonad does not have any built-in status bars. Instead of this it can pipe required information to an external program. Usually, xmobar, or dzen is a good choice for a status bar.

#### [xmobar]

Install [[[x11-misc/xmobar]](https://packages.gentoo.org/packages/x11-misc/xmobar)[]]:

`root `[`#`]`emerge --ask x11-misc/xmobar`

#### [dzen]

Install [[[x11-misc/dzen]](https://packages.gentoo.org/packages/x11-misc/dzen)[]]:

`root `[`#`]`emerge --ask x11-misc/dzen`

## [External resources]

-   [man xmonad]
-   [Official tutorial for configuring Xmonad](https://xmonad.org/TUTORIAL.html)
-   [XMonad on HaskellWiki](http://www.haskell.org/haskellwiki/Xmonad)
-   [XMonad on ArchWiki](https://wiki.archlinux.org/index.php/Xmonad)