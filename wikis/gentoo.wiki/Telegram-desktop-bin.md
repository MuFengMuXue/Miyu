[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=Telegram&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

**Resources**

[[]][Home](https://telegram.org)

[[]][Package information](https://packages.gentoo.org/packages/net-im/telegram-desktop)

[[]][Package information](https://packages.gentoo.org/packages/net-im/telegram-desktop-bin)

[[]][Wikipedia](https://en.wikipedia.org/wiki/Telegram_(software) "wikipedia:Telegram (software)")

[[]][GitHub](https://github.com/telegramdesktop/tdesktop)

**Telegram** is a freeware, cross-platform, cloud-based instant messaging (IM) system. It is written in C++.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
-   [[2] [Removal]](#Removal)
    -   [[2.1] [Unmerge]](#Unmerge)
-   [[3] [See Also]](#See_Also)

## [Installation]

### [USE flags]

### [USE flags for] [net-im/telegram-desktop](https://packages.gentoo.org/packages/net-im/telegram-desktop) [[]] [Official desktop client for Telegram]

  --------------------------------------------------------------------- ------------------------------------------------------------------------------
  [`+X`](https://packages.gentoo.org/useflags/+X)                       Add support for X11
  [`+fonts`](https://packages.gentoo.org/useflags/+fonts)               Use builtin patched copy of open-sans fonts (overrides fontconfig)
  [`+libdispatch`](https://packages.gentoo.org/useflags/+libdispatch)   Use dev-libs/libdispatch to speed up concurrent code execution
  [`dbus`](https://packages.gentoo.org/useflags/dbus)                   Enable dbus support for anything that needs it (gpsd, gnomemeeting, etc)
  [`enchant`](https://packages.gentoo.org/useflags/enchant)             Use the app-text/enchant spell-checking backend instead of app-text/hunspell
  [`screencast`](https://packages.gentoo.org/useflags/screencast)       Enable support for remote desktop and screen cast using PipeWire
  [`wayland`](https://packages.gentoo.org/useflags/wayland)             Enable dev-libs/wayland backend
  [`webkit`](https://packages.gentoo.org/useflags/webkit)               Add support for the WebKit HTML rendering/layout engine
  --------------------------------------------------------------------- ------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-05-26 14:57] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

Emerge Telegram:

`root `[`#`]`emerge --ask net-im/telegram-desktop`

Alternatively, install the pre-built binary version:

`root `[`#`]`emerge --ask net-im/telegram-desktop-bin`

## [Removal]

### [Unmerge]

Delete telegram-desktop with emerge:

`root `[`#`]`emerge --ask --depclean --verbose net-im/telegram-desktop`

Delete telegram-desktop-bin with emerge:

`root `[`#`]`emerge --ask --depclean --verbose net-im/telegram-desktop-bin`

## [See Also]

-   [Discord](https://wiki.gentoo.org/wiki/Discord "Discord") --- a proprietary VoIP instant messaging and digital distribution platform for voice, video, and text communication.
-   [Recommended applications](https://wiki.gentoo.org/wiki/Recommended_applications "Recommended applications") --- applications recommended for use in a graphical environment ([X11](https://wiki.gentoo.org/wiki/Xorg "Xorg"), [Wayland](https://wiki.gentoo.org/wiki/Wayland "Wayland"))