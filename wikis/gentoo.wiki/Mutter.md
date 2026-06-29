[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=Mutter&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

**Resources**

[[]][Home](https://mutter.gnome.org/)

[[]][Package information](https://packages.gentoo.org/packages/x11-wm/mutter)

[[]][Wikipedia](https://en.wikipedia.org/wiki/Mutter_(software) "wikipedia:Mutter (software)")

[[]][GitLab](https://gitlab.com/GNOME/mutter)

[Mutter] is a [Wayland](https://wiki.gentoo.org/wiki/Wayland "Wayland") display server and [X11](https://wiki.gentoo.org/wiki/X11 "X11") [window manager](https://wiki.gentoo.org/wiki/Window_manager "Window manager") and compositor library.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [Merge]](#Merge)
-   [[2] [Removal]](#Removal)
    -   [[2.1] [Unmerge]](#Unmerge)

## [Installation]

### [USE flags for] [x11-wm/mutter](https://packages.gentoo.org/packages/x11-wm/mutter) [[]] [GNOME compositing window manager based on Clutter]

  --------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [`+introspection`](https://packages.gentoo.org/useflags/+introspection)     Add support for GObject based introspection
  [`+wayland`](https://packages.gentoo.org/useflags/+wayland)                 Enable dev-libs/wayland backend
  [`+xwayland`](https://packages.gentoo.org/useflags/+xwayland)               Enable X11 application support in Wayland sessions
  [`X`](https://packages.gentoo.org/useflags/X)                               Add support for X11
  [`bash-completion`](https://packages.gentoo.org/useflags/bash-completion)   Enable bash-completion support
  [`debug`](https://packages.gentoo.org/useflags/debug)                       Enable extra debug codepaths, like asserts and extra output. If you want to get meaningful backtraces see https://wiki.gentoo.org/wiki/Project:Quality_Assurance/Backtraces
  [`devkit`](https://packages.gentoo.org/useflags/devkit)                     Enable support for running a nested wayland session
  [`elogind`](https://packages.gentoo.org/useflags/elogind)                   Rely on sys-auth/elogind as logind provider for Wayland sessions
  [`gnome`](https://packages.gentoo.org/useflags/gnome)                       Add GNOME support
  [`gtk-doc`](https://packages.gentoo.org/useflags/gtk-doc)                   Build and install gtk-doc based developer documentation for dev-util/devhelp, IDE and offline use
  [`screencast`](https://packages.gentoo.org/useflags/screencast)             Enable support for remote desktop and screen cast using PipeWire
  [`selinux`](https://packages.gentoo.org/useflags/selinux)                   !!internal use only!! Security Enhanced Linux support, this must be set by the selinux profile or breakage will occur
  [`sysprof`](https://packages.gentoo.org/useflags/sysprof)                   Enable profiling data capture support using dev-util/sysprof-capture
  [`systemd`](https://packages.gentoo.org/useflags/systemd)                   Enable use of systemd-specific libraries and features like socket activation or session tracking
  [`test`](https://packages.gentoo.org/useflags/test)                         Enable dependencies and/or preparations necessary to run tests (usually controlled by FEATURES=test but can be toggled independently)
  [`udev`](https://packages.gentoo.org/useflags/udev)                         Enable virtual/udev integration (device discovery, power and storage device support, etc)
  --------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-05-24 23:39] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Merge]

`root `[`#`]`emerge --ask x11-wm/mutter`

## [Removal]

### [Unmerge]

`root `[`#`]`emerge --ask --depclean --verbose x11-wm/mutter`