**Resources**

[[]][Home](http://www.fvwm.org/)

[[]][Package information](https://packages.gentoo.org/packages/x11-wm/fvwm3)

[[]][Wikipedia](https://en.wikipedia.org/wiki/FVWM "wikipedia:FVWM")

[[]][GitHub](https://github.com/fvwmorg/fvwm)

[[]][[#fvwm](ircs://irc.libera.chat/#fvwm)] ([[webchat](https://web.libera.chat/#fvwm)])

[![Ohloh Logo](/images/thumb/c/c1/Ohloh-logo.png/30px-Ohloh-logo.png)][Open Hub](https://www.openhub.net/p/fvwm)

**FVWM** (**F V**irtual **W**indow **M**anager) is a stacking [window manager](https://wiki.gentoo.org/wiki/Window_manager "Window manager") for [Xorg](https://wiki.gentoo.org/wiki/Xorg "Xorg"). It is designed to minimize memory consumption, provide a 3D look to window frames, and to provide a virtual desktop. It is also possible to extend FVWM using C, M4 and Perl preprocessing or scripts, in the case of Perl.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
-   [[2] [Configuration]](#Configuration)
    -   [[2.1] [Starting]](#Starting)
-   [[3] [See also]](#See_also)
-   [[4] [External resources]](#External_resources)

## [Installation]

### [USE flags]

### [USE flags for] [x11-wm/fvwm3](https://packages.gentoo.org/packages/x11-wm/fvwm3) [[]] [A multiple large virtual desktop window manager derived from fvwm]

  ------------------------------------------------------------- ---------------------------------------------------------------------------------------
  [`+go`](https://packages.gentoo.org/useflags/+go)             Enable building dev-lang/go code (FvwmPrompt)
  [`bidi`](https://packages.gentoo.org/useflags/bidi)           Enable bidirectional language support
  [`nls`](https://packages.gentoo.org/useflags/nls)             Add Native Language Support (using gettext - GNU locale utilities)
  [`readline`](https://packages.gentoo.org/useflags/readline)   Enable support for libreadline, a GNU line-editing library that almost everyone wants
  [`svg`](https://packages.gentoo.org/useflags/svg)             Add support for SVG (Scalable Vector Graphics)
  ------------------------------------------------------------- ---------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-03-09 02:24] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

After flags have been set issue an emerge command to install FVWM:

`root `[`#`]`emerge --ask x11-wm/fvwm3`

## [Configuration]

FVWM\'s main configuration file is [\~/.fvwm/config].

### [Starting]

To start FVWM use a [display manager](https://wiki.gentoo.org/wiki/Display_manager "Display manager") or the [startx] command.

When using [startx] with [elogind](https://wiki.gentoo.org/wiki/Elogind "Elogind") support, setup elogind and create the following file:

[FILE] **`~/.xinitrc`**

    exec dbus-launch --sh-syntax --exit-with-session fvwm

## [See also]

-   [FVWM-Crystal](https://wiki.gentoo.org/wiki/FVWM-Crystal "FVWM-Crystal") --- an easy to use, powerful and pretty desktop environment.

## [External resources]

-   [FVWM wiki](https://www.fvwm.org/Wiki/)
-   [#fvwmFAQ](https://www.fvwm.org/Wiki/Irc/HashFvwmFAQ/)
-   [http://zensites.net/fvwm/guide/](http://zensites.net/fvwm/guide/)
-   [X Window Managers and Perl, with a section on using perl with FVWM](http://migo.sixbit.org/papers/X_WM_and_Perl/slide-index.html)