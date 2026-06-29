**Resources**

[[]][Package information](https://packages.gentoo.org/packages/media-gfx/imv)

[[]][Sourcehut](https://sr.ht/~exec64/imv)

[![Ohloh Logo](/images/thumb/c/c1/Ohloh-logo.png/30px-Ohloh-logo.png)][Open Hub](https://www.openhub.net/p/imv)

**imv** is a free and open-source simple image viewer for [X11](https://wiki.gentoo.org/wiki/X11 "X11") and [Wayland](https://wiki.gentoo.org/wiki/Wayland "Wayland"). It can also be used for providing a desktop background for tiling [window managers](https://wiki.gentoo.org/wiki/Window_managers "Window managers") like [i3](https://wiki.gentoo.org/wiki/I3 "I3").

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
    -   [[1.3] [Usage]](#Usage)
-   [[2] [See also]](#See_also)

## [Installation]

### [USE flags]

### [USE flags for] [media-gfx/imv](https://packages.gentoo.org/packages/media-gfx/imv) [[]] [Minimal image viewer designed for tiling window manager users]

  ----------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------
  [`+X`](https://packages.gentoo.org/useflags/+X)             Add support for X11
  [`+jpeg`](https://packages.gentoo.org/useflags/+jpeg)       Add JPEG image support
  [`+png`](https://packages.gentoo.org/useflags/+png)         Add support for libpng (PNG images)
  [`bmp`](https://packages.gentoo.org/useflags/bmp)           Add bitmap (.bmp) image support using media-libs/libnsbmp
  [`gif`](https://packages.gentoo.org/useflags/gif)           Add GIF image support
  [`heif`](https://packages.gentoo.org/useflags/heif)         Enable support for ISO/IEC 23008-12:2017 HEIF/HEIC image format
  [`icu`](https://packages.gentoo.org/useflags/icu)           Enable ICU (Internationalization Components for Unicode) support, using dev-libs/icu
  [`jpegxl`](https://packages.gentoo.org/useflags/jpegxl)     Add JPEG XL image support
  [`svg`](https://packages.gentoo.org/useflags/svg)           Add support for SVG (Scalable Vector Graphics)
  [`test`](https://packages.gentoo.org/useflags/test)         Enable dependencies and/or preparations necessary to run tests (usually controlled by FEATURES=test but can be toggled independently)
  [`tiff`](https://packages.gentoo.org/useflags/tiff)         Add support for the TIFF image format
  [`wayland`](https://packages.gentoo.org/useflags/wayland)   Enable dev-libs/wayland backend
  [`webp`](https://packages.gentoo.org/useflags/webp)         Add support for the WebP image format
  ----------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-03-20 22:27] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

Install [[[media-gfx/imv]](https://packages.gentoo.org/packages/media-gfx/imv)[]]:

`root `[`#`]`emerge --ask media-gfx/imv`

### [Usage]

Refer to the [[[imv(1)]](https://man.archlinux.org/man/imv.1.en)[[]](https://wiki.gentoo.org/wiki/Special:MyLanguage/man_page "Special:MyLanguage/man page")] man page for information such as command-line options and default bindings. Refer to the [[[imv-msg(1)]](https://man.archlinux.org/man/imv-msg.1.en)[[]](https://wiki.gentoo.org/wiki/Special:MyLanguage/man_page "Special:MyLanguage/man page")] man page for information about sending commands to [imv] via a socket.

## [See also]

-   [Feh](https://wiki.gentoo.org/wiki/Feh "Feh") --- an open-source image viewer that is mainly aimed at command-line users.