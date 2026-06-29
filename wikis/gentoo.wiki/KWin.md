[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=KWin&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

**Resources**

[[]][Home](https://invent.kde.org/plasma/kwin)

[[]][Package information](https://packages.gentoo.org/packages/kde-plasma/kwin)

[[]][Wikipedia](https://en.wikipedia.org/wiki/KWin "wikipedia:KWin")

[[]][GitHub](https://github.com/KDE/kwin)

[KWin] is an [Xorg](https://wiki.gentoo.org/wiki/Xorg "Xorg") [window manager](https://wiki.gentoo.org/wiki/Window_manager "Window manager") and [Wayland](https://wiki.gentoo.org/wiki/Wayland "Wayland") compositor.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [Merge]](#Merge)
-   [[2] [Removal]](#Removal)
    -   [[2.1] [Unmerge]](#Unmerge)

## [Installation]

### [USE flags for] [kde-plasma/kwin](https://packages.gentoo.org/packages/kde-plasma/kwin) [[]] [Flexible, composited Window Manager for windowing systems on Linux]

  ----------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [`+filecaps`](https://packages.gentoo.org/useflags/+filecaps)           Use Linux file capabilities to control privilege rather than set\*id (this is orthogonal to USE=caps which uses capabilities at runtime e.g. libcap)
  [`+handbook`](https://packages.gentoo.org/useflags/+handbook)           Enable handbooks generation for packages by KDE
  [`+shortcuts`](https://packages.gentoo.org/useflags/+shortcuts)         Enable global shortcuts support via kde-plasma/kglobalacceld
  [`X`](https://packages.gentoo.org/useflags/X)                           Enable ability to support native X11 applications via x11-base/xwayland
  [`accessibility`](https://packages.gentoo.org/useflags/accessibility)   Add support for accessibility (eg \'at-spi\' library)
  [`debug`](https://packages.gentoo.org/useflags/debug)                   Enable extra debug codepaths, like asserts and extra output. If you want to get meaningful backtraces see https://wiki.gentoo.org/wiki/Project:Quality_Assurance/Backtraces
  [`gamepad`](https://packages.gentoo.org/useflags/gamepad)               Support using game controllers as input devices
  [`gles2-only`](https://packages.gentoo.org/useflags/gles2-only)         Use GLES 2.0 (OpenGL for Embedded Systems) or later instead of full OpenGL (see also: gles2)
  [`lock`](https://packages.gentoo.org/useflags/lock)                     Enable screen locking via kde-plasma/kscreenlocker
  [`screencast`](https://packages.gentoo.org/useflags/screencast)         Enable screencast portal using media-video/pipewire
  [`selinux`](https://packages.gentoo.org/useflags/selinux)               !!internal use only!! Security Enhanced Linux support, this must be set by the selinux profile or breakage will occur
  [`systemd`](https://packages.gentoo.org/useflags/systemd)               Enable use of systemd-specific libraries and features like socket activation or session tracking
  [`test`](https://packages.gentoo.org/useflags/test)                     Enable dependencies and/or preparations necessary to run tests (usually controlled by FEATURES=test but can be toggled independently)
  ----------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-05-25 06:17] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Merge]

`root `[`#`]`emerge --ask kde-plasma/kwin`

## [Removal]

### [Unmerge]

`root `[`#`]`emerge --ask --depclean --verbose kde-plasma/kwin`