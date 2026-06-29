\

[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=Piper&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

[[]][Package information](https://packages.gentoo.org/packages/app-misc/piper)

[[]][GitHub](https://github.com/libratbag/piper)

Piper is a GTK+ application to configure gaming mice. Piper is merely a graphical frontend to the ratbagd DBus daemon.

## [Installation]

### [USE flags]

### [USE flags for] [app-misc/piper](https://packages.gentoo.org/packages/app-misc/piper) [[]] [GTK application to configure gaming devices]

  ----------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------
  [`test`](https://packages.gentoo.org/useflags/test)   Enable dependencies and/or preparations necessary to run tests (usually controlled by FEATURES=test but can be toggled independently)
  ----------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-04-14 11:34] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

`root `[`#`]`emerge --ask app-misc/piper`

For non root access to [ratbagd](https://wiki.gentoo.org/wiki/Ratbagd "Ratbagd") user should be in group `plugdev`

`root `[`#`]`usermod -aG plugdev larry`