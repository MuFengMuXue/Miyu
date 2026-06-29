\

[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=Ratbagd&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

[[]][Package information](https://packages.gentoo.org/packages/dev-libs/libratbag)

[[]][GitHub](https://github.com/libratbag/libratbag)

libratbag provides ratbagd, a DBus daemon to configure input devices, mainly gaming mice. The daemon provides a generic way to access the various features exposed by these mice and abstracts away hardware-specific and kernel-specific quirks.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
    -   [[1.3] [Service]](#Service)
        -   [[1.3.1] [systemd]](#systemd)
-   [[2] [Testing]](#Testing)

## [Installation]

### [USE flags]

### [USE flags for] [dev-libs/libratbag](https://packages.gentoo.org/packages/dev-libs/libratbag) [[]] [Library to configure gaming mice]

  ----------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------
  [`doc`](https://packages.gentoo.org/useflags/doc)           Add extra documentation (API, Javadoc, etc). It is recommended to enable per package instead of globally
  [`elogind`](https://packages.gentoo.org/useflags/elogind)   Enable session tracking via sys-auth/elogind
  [`systemd`](https://packages.gentoo.org/useflags/systemd)   Enable use of systemd-specific libraries and features like socket activation or session tracking
  [`test`](https://packages.gentoo.org/useflags/test)         Enable dependencies and/or preparations necessary to run tests (usually controlled by FEATURES=test but can be toggled independently)
  ----------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-04-14 11:34] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

`root `[`#`]`emerge --ask dev-libs/libratbag`

### [Service]

#### [systemd]

To start ratbagd on boot:

`root `[`#`]`systemctl enable --now ratbagd`

For non root access to [ratbagd] user should be in group `plugdev`

`root `[`#`]`usermod -aG plugdev larry`

## [Testing]

You can test that ratbagd is running and can see your devices by using the \`ratbagctl\` command:

`root `[`#`]`ratbagctl list`

Running this command as your user will ensure that your user is in the correct groups.