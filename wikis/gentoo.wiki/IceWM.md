**Resources**

[[]][GitHub](https://github.com/bbidulock/icewm)

[[]][Home](https://ice-wm.org/)

[![Ohloh Logo](/images/thumb/c/c1/Ohloh-logo.png/30px-Ohloh-logo.png)][Open Hub](https://www.openhub.net/p/icewm)

[[]][SourceForge](https://sourceforge.net/projects/icewm/)

[[]][Wikipedia](https://en.wikipedia.org/wiki/IceWM "wikipedia:IceWM")

**IceWM** is a free and open-source, lightweight, stacking [window manager](https://wiki.gentoo.org/wiki/Window_manager "Window manager") for [X11](https://wiki.gentoo.org/wiki/X11 "X11"). It is written in C++ and is designed to be easily customizable. It is also used by lightweight, beginner-friendly distributions like Puppy Linux.

## [Installation]

### [USE flags]

### [USE flags for] [x11-wm/icewm](https://packages.gentoo.org/packages/x11-wm/icewm) [[]] [Ice Window Manager with Themes]

  ------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [`+alsa`](https://packages.gentoo.org/useflags/+alsa)               Add support for media-libs/alsa-lib (Advanced Linux Sound Architecture)
  [`+gdk-pixbuf`](https://packages.gentoo.org/useflags/+gdk-pixbuf)   Enable gdk-pixbuf rendering
  [`ao`](https://packages.gentoo.org/useflags/ao)                     Use libao audio output library for sound playback
  [`bidi`](https://packages.gentoo.org/useflags/bidi)                 Enable bidirectional language support
  [`debug`](https://packages.gentoo.org/useflags/debug)               Enable extra debug codepaths, like asserts and extra output. If you want to get meaningful backtraces see https://wiki.gentoo.org/wiki/Project:Quality_Assurance/Backtraces
  [`imlib`](https://packages.gentoo.org/useflags/imlib)               Add support for imlib, an image loading and rendering library
  [`nls`](https://packages.gentoo.org/useflags/nls)                   Add Native Language Support (using gettext - GNU locale utilities)
  [`truetype`](https://packages.gentoo.org/useflags/truetype)         Add support for FreeType and/or FreeType2 fonts
  [`xinerama`](https://packages.gentoo.org/useflags/xinerama)         Add support for querying multi-monitor screen geometry through the Xinerama API
  ------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2025-09-02 17:00] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

Install [[[x11-wm/icewm]](https://packages.gentoo.org/packages/x11-wm/icewm)[]] with:

`root `[`#`]`emerge --ask x11-wm/icewm`