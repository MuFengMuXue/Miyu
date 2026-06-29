[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=Waypipe&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

**Resources**

[[]][Home](https://gitlab.freedesktop.org/mstoeckl/waypipe)

[[]][Package information](https://packages.gentoo.org/packages/gui-apps/waypipe)

**Waypipe** is a proxy for Wayland clients. It forwards Wayland messages and serializes changes to shared memory buffers over a single socket. This makes application forwarding similar to `ssh -X` feasible.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
-   [[2] [Usage]](#Usage)

## [Installation]

### [USE flags]

### [USE flags for] [gui-apps/waypipe](https://packages.gentoo.org/packages/gui-apps/waypipe) [[]] [Transparent network proxy for Wayland compositors]

  --------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------
  [`dmabuf`](https://packages.gentoo.org/useflags/dmabuf)         Use DMABUFs for data exchange and hardware decoding
  [`ffmpeg`](https://packages.gentoo.org/useflags/ffmpeg)         Link with ffmpeg to allow buffer displays using video streams
  [`lz4`](https://packages.gentoo.org/useflags/lz4)               Enable support for lz4 compression (as implemented in app-arch/lz4)
  [`systemtap`](https://packages.gentoo.org/useflags/systemtap)   Enable SystemTap/DTrace tracing
  [`test`](https://packages.gentoo.org/useflags/test)             Enable dependencies and/or preparations necessary to run tests (usually controlled by FEATURES=test but can be toggled independently)
  [`vaapi`](https://packages.gentoo.org/useflags/vaapi)           Enable Video Acceleration API for hardware decoding
  [`zstd`](https://packages.gentoo.org/useflags/zstd)             Enable support for ZSTD compression
  --------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2025-08-26 21:27] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

`root `[`#`]`emerge --ask gui-apps/waypipe`

## [Usage]

Any GUI program can be started remotely through Waypipe, by prefixing an ssh command with `waypipe` and connecting to a server that has Waypipe installed:

`user `[`$`]`waypipe ssh user@::`\
`Last login from ::1`\
\

`user `[`$`]`kwrite`

For example to run [Sway](https://wiki.gentoo.org/wiki/Sway "Sway"), use:

`user `[`$`]`waypipe ssh user@127.0.0.1 sway`

Refer to the [[[waypipe(1)]](https://man.archlinux.org/man/waypipe.1.en)[[]](https://wiki.gentoo.org/wiki/Special:MyLanguage/man_page "Special:MyLanguage/man page")] man page for detailed usage information.