[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=Seatd&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

**Resources**

[[]][Home](https://sr.ht/~kennylevinsen/seatd/)

[[]][Package information](https://packages.gentoo.org/packages/sys-auth/seatd)

**Seatd** is a minimal seat management daemon, and a universal seat management library. Seat management takes care of mediating access to shared devices (graphics, input), without requiring applications like [Wayland compositors](https://wiki.gentoo.org/wiki/Wayland_compositor "Wayland compositor") being granted root privileges.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
    -   [[1.3] [Service]](#Service)
        -   [[1.3.1] [OpenRC]](#OpenRC)
-   [[2] [External resources]](#External_resources)

## [Installation]

### [USE flags]

### [USE flags for] [sys-auth/seatd](https://packages.gentoo.org/packages/sys-auth/seatd) [[]] [Minimal seat management daemon and universal library]

  ----------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------
  [`builtin`](https://packages.gentoo.org/useflags/builtin)   Enable embedded server in libseat
  [`elogind`](https://packages.gentoo.org/useflags/elogind)   Enable session tracking via sys-auth/elogind
  [`selinux`](https://packages.gentoo.org/useflags/selinux)   !!internal use only!! Security Enhanced Linux support, this must be set by the selinux profile or breakage will occur
  [`server`](https://packages.gentoo.org/useflags/server)     Enable standalone seatd server, replacement to (e)logind
  [`systemd`](https://packages.gentoo.org/useflags/systemd)   Enable use of systemd-specific libraries and features like socket activation or session tracking
  ----------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-05-24 23:16] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

`root `[`#`]`emerge --ask sys-auth/seatd`

### [Service]

#### [OpenRC]

To use the [seatd] service, the `builtin` and `server` USE flags must be enabled. In addition, users of [seatd] must be part of the `video` and `seat` groups:

`root `[`#`]`gpasswd -a larry video`

`root `[`#`]`gpasswd -a larry seat`

Add the [seatd] daemon to the default runlevel so that seat management is provided on system startup:

`root `[`#`]`rc-update add seatd default`

Start the [seatd] daemon now:

`root `[`#`]`rc-service seatd start`

## [External resources]

-   [[[seatd(1)]](https://man.archlinux.org/man/seatd.1.en)[[]](https://wiki.gentoo.org/wiki/Special:MyLanguage/man_page "Special:MyLanguage/man page")] - Man page for seatd
-   [[[seatd-launch(1)]](https://man.archlinux.org/man/seatd-launch.1.en)[[]](https://wiki.gentoo.org/wiki/Special:MyLanguage/man_page "Special:MyLanguage/man page")] - Man page for [seatd-launch], to start a process with its own seatd instance