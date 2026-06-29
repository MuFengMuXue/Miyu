[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=Conky&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

**Resources**

[[]][Home](https://github.com/brndnmtthws/conky)

[[]][Package information](https://packages.gentoo.org/packages/app-admin/conky)

[[]][Wikipedia](https://en.wikipedia.org/wiki/Conky_(software) "wikipedia:Conky (software)")

[[]][[#conky](ircs://irc.libera.chat/#conky)] ([[webchat](https://web.libera.chat/#conky)])

[[]][Guide](https://wiki.gentoo.org/wiki/Conky/Guide "Conky/Guide")

**Conky** is an advanced and highly configurable system monitor for the [Xorg window system](https://wiki.gentoo.org/wiki/Xorg "Xorg"), which \"can display arbitrary information (such as the date, CPU temperature from [I2C](https://wiki.gentoo.org/wiki/I2C "I2C"), [MPD](https://wiki.gentoo.org/wiki/MPD "MPD") info, and anything else you desire) to the root window in X. Conky normally does this by drawing to the root window, however Conky can also be run in windowed mode (though this is not how Conky was meant to be used).\"^[\[1\]](#cite_note-1)^

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
-   [[2] [Configuration]](#Configuration)
-   [[3] [See also]](#See_also)
-   [[4] [External resources]](#External_resources)
-   [[5] [References]](#References)

## [Installation]

### [USE flags]

### [USE flags for] [app-admin/conky](https://packages.gentoo.org/packages/app-admin/conky) [[]] [An advanced, highly configurable system monitor for X]

  --------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------
  [`+portmon`](https://packages.gentoo.org/useflags/+portmon)                 Enable support for tcp (ip4) port monitoring
  [`X`](https://packages.gentoo.org/useflags/X)                               Add support for X11
  [`apcupsd`](https://packages.gentoo.org/useflags/apcupsd)                   Enable support for sys-power/apcupsd
  [`bundled-toluapp`](https://packages.gentoo.org/useflags/bundled-toluapp)   Enable support for bundled toluapp. This only makes sense in combination with the lua-\* flags
  [`cmus`](https://packages.gentoo.org/useflags/cmus)                         Enable monitoring of music played by media-sound/cmus
  [`colour-name-map`](https://packages.gentoo.org/useflags/colour-name-map)   Include mappings of colour name
  [`curl`](https://packages.gentoo.org/useflags/curl)                         Add support for client-side URL transfer library
  [`doc`](https://packages.gentoo.org/useflags/doc)                           Add extra documentation (API, Javadoc, etc). It is recommended to enable per package instead of globally
  [`extras`](https://packages.gentoo.org/useflags/extras)                     Enable syntax highlighting for app-editors/nanoand app-editors/vim
  [`hddtemp`](https://packages.gentoo.org/useflags/hddtemp)                   Enable monitoring of hdd temperature (app-admin/hddtemp)
  [`ical`](https://packages.gentoo.org/useflags/ical)                         Enable support for events from iCalendar (RFC 5545) files using dev-libs/libical
  [`iconv`](https://packages.gentoo.org/useflags/iconv)                       Enable support for the iconv character set conversion library
  [`imlib`](https://packages.gentoo.org/useflags/imlib)                       Add support for imlib, an image loading and rendering library
  [`intel-backlight`](https://packages.gentoo.org/useflags/intel-backlight)   Enable support for Intel backlight
  [`iostats`](https://packages.gentoo.org/useflags/iostats)                   Enable support for per-task I/O statistics
  [`irc`](https://packages.gentoo.org/useflags/irc)                           Enable support for displaying everything from an irc channel using net-libs/libircclient
  [`lua-cairo`](https://packages.gentoo.org/useflags/lua-cairo)               Enable if you want Lua Cairo bindings
  [`lua-cairo-xlib`](https://packages.gentoo.org/useflags/lua-cairo-xlib)     Enable support for Cairo and Xlib interoperability for Lua
  [`lua-imlib`](https://packages.gentoo.org/useflags/lua-imlib)               Enable if you want Lua Imlib2 bindings
  [`lua-rsvg`](https://packages.gentoo.org/useflags/lua-rsvg)                 Enable if you want Lua RSVG bindings
  [`math`](https://packages.gentoo.org/useflags/math)                         Enable support for glibc\'s libm math library
  [`moc`](https://packages.gentoo.org/useflags/moc)                           Enable monitoring of music played by media-sound/moc
  [`mouse-events`](https://packages.gentoo.org/useflags/mouse-events)         Enable support for mouse events\"
  [`mpd`](https://packages.gentoo.org/useflags/mpd)                           Enable monitoring of music controlled by media-sound/mpd
  [`mysql`](https://packages.gentoo.org/useflags/mysql)                       Add mySQL Database support
  [`ncurses`](https://packages.gentoo.org/useflags/ncurses)                   Add ncurses support (console display library)
  [`nvidia`](https://packages.gentoo.org/useflags/nvidia)                     Enable reading of nvidia card temperature sensors via x11-drivers/nvidia-drivers
  [`pulseaudio`](https://packages.gentoo.org/useflags/pulseaudio)             Add sound server support via media-libs/libpulse (may be PulseAudio or PipeWire)
  [`rss`](https://packages.gentoo.org/useflags/rss)                           Enable support for RSS feeds
  [`systemd`](https://packages.gentoo.org/useflags/systemd)                   Enable use of systemd-specific libraries and features like socket activation or session tracking
  [`test`](https://packages.gentoo.org/useflags/test)                         Enable dependencies and/or preparations necessary to run tests (usually controlled by FEATURES=test but can be toggled independently)
  [`thinkpad`](https://packages.gentoo.org/useflags/thinkpad)                 Enable support for IBM/Lenovo notebooks
  [`truetype`](https://packages.gentoo.org/useflags/truetype)                 Add support for FreeType and/or FreeType2 fonts
  [`wayland`](https://packages.gentoo.org/useflags/wayland)                   Enable dev-libs/wayland backend
  [`webserver`](https://packages.gentoo.org/useflags/webserver)               Enable support to act as a webserver serving conkys output using net-libs/libmicrohttpd
  [`wifi`](https://packages.gentoo.org/useflags/wifi)                         Enable wireless network functions
  [`xinerama`](https://packages.gentoo.org/useflags/xinerama)                 Add support for querying multi-monitor screen geometry through the Xinerama API
  [`xinput`](https://packages.gentoo.org/useflags/xinput)                     Enable support for Xinput 2 (slow)
  [`xmms2`](https://packages.gentoo.org/useflags/xmms2)                       Enable monitoring of music played by media-sound/xmms2
  --------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-05-19 18:30] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

Install [[[app-admin/conky]](https://packages.gentoo.org/packages/app-admin/conky)[]]:

`root `[`#`]`emerge --ask app-admin/conky`

## [Configuration]

After installing Conky, create a default configuration as a starting point:

`user `[`$`]`mkdir -p ~/.config/conky && conky -C > ~/.config/conky/conky.conf `

Open the configuration file with a text editor of choice and edit away. Enabling lua syntax highlighting may help.

Users of modern composited desktop environments will probably want to use conky in own window mode with true transparency:

[FILE] **`~/.config/conky/conky.conf`**

    own_window = true,
    own_window_class = 'conky',
    own_window_argb_visual = true,
    own_window_argb_value = 80,
    own_window_hints = 'undecorated,below,sticky,skip_taskbar,skip_pager',
    own_window_colour = '101010',
    own_window_type = 'desktop'

## [See also]

-   [Conky/Guide](https://wiki.gentoo.org/wiki/Conky/Guide "Conky/Guide") --- describes how to install and configure the system monitor known as Conky.

## [External resources]

-   [Conky FAQ](https://github.com/brndnmtthws/conky/wiki/FAQ)
-   [Example configurations](https://github.com/brndnmtthws/conky/wiki/Configs)
-   [Conky page on ArchWiki](https://wiki.archlinux.org/index.php/Conky)

## [References]

1.  [[[↑](#cite_ref-1)] [[http://conky.sourceforge.net/faq.html](http://conky.sourceforge.net/faq.html)]]