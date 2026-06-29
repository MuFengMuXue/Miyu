Other languages:

-   [English]
-   [magyar](https://wiki.gentoo.org/wiki/Xorg/hu "Xorg (100% translated)")
-   [русиньскый](https://wiki.gentoo.org/wiki/Xorg/rue "Xorg/rue (20% translated)")
-   [日本語](https://wiki.gentoo.org/wiki/Xorg/ja "Xorg (100% translated)")

**Resources**

[[![Gentoo peach graphic](/images/thumb/a/ad/Gentoo-logo-peach.svg/25px-Gentoo-logo-peach.svg.png)](https://wiki.gentoo.org/wiki/Project:X11 "Project:X11")][Project](https://wiki.gentoo.org/wiki/Project:X11 "Project:X11")

[[]][Home](http://www.x.org)

[[]][Official documentation](http://www.x.org/wiki/Documentation/)

[[]][Guide](https://wiki.gentoo.org/wiki/Xorg/Guide "Xorg/Guide")

[[]][Wikipedia](https://en.wikipedia.org/wiki/X.Org_Server "wikipedia:X.Org Server")

[[]][GitWeb](http://cgit.freedesktop.org/xorg/xserver/)

**Xorg** is an open source implementation of the [X server](https://wiki.gentoo.org/wiki/X_server "X server").

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [The X USE flag]](#The_X_USE_flag)
    -   [[1.3] [Emerge]](#Emerge)
-   [[2] [Troubleshooting]](#Troubleshooting)
    -   [[2.1] [X server starts and dies unexpectedly with no errors]](#X_server_starts_and_dies_unexpectedly_with_no_errors)
    -   [[2.2] [Blockers when updating xorg-server with xorg-drivers]](#Blockers_when_updating_xorg-server_with_xorg-drivers)
-   [[3] [See also]](#See_also)

## [Installation]

[Xorg guide](https://wiki.gentoo.org/wiki/Xorg/Guide "Xorg/Guide") details the installation of Xorg.

### [USE flags]

### [USE flags for] [x11-base/xorg-server](https://packages.gentoo.org/packages/x11-base/xorg-server) [[]] [X.Org X servers]

  ----------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [`+elogind`](https://packages.gentoo.org/useflags/+elogind)       Use elogind to get control over framebuffer when running as regular user
  [`+udev`](https://packages.gentoo.org/useflags/+udev)             Enable virtual/udev integration (device discovery, power and storage device support, etc)
  [`debug`](https://packages.gentoo.org/useflags/debug)             Enable extra debug codepaths, like asserts and extra output. If you want to get meaningful backtraces see https://wiki.gentoo.org/wiki/Project:Quality_Assurance/Backtraces
  [`minimal`](https://packages.gentoo.org/useflags/minimal)         Install a very minimal build (disables, for example, plugins, fonts, most drivers, non-critical features)
  [`selinux`](https://packages.gentoo.org/useflags/selinux)         !!internal use only!! Security Enhanced Linux support, this must be set by the selinux profile or breakage will occur
  [`suid`](https://packages.gentoo.org/useflags/suid)               Enable setuid root program(s)
  [`systemd`](https://packages.gentoo.org/useflags/systemd)         Enable use of systemd-specific libraries and features like socket activation or session tracking
  [`test`](https://packages.gentoo.org/useflags/test)               Enable dependencies and/or preparations necessary to run tests (usually controlled by FEATURES=test but can be toggled independently)
  [`unwind`](https://packages.gentoo.org/useflags/unwind)           Enable libunwind usage for backtraces
  [`xcsecurity`](https://packages.gentoo.org/useflags/xcsecurity)   Build Security extension
  [`xephyr`](https://packages.gentoo.org/useflags/xephyr)           Build the Xephyr server
  [`xnest`](https://packages.gentoo.org/useflags/xnest)             Build the Xnest server
  [`xorg`](https://packages.gentoo.org/useflags/xorg)               Build the Xorg X server (HIGHLY RECOMMENDED)
  [`xvfb`](https://packages.gentoo.org/useflags/xvfb)               Build the Xvfb server
  ----------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-04-30 20:45] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [The X USE flag]

Many packages can be built with optional X11 support by activating the global [`X`](https://packages.gentoo.org/useflags/X) USE flag (if not already activated by [profile](https://wiki.gentoo.org/wiki/Profile_(Portage) "Profile (Portage)") selection).

### [Emerge]

Just the necessary components:

`root `[`#`]`emerge --ask x11-base/xorg-server`

** Note**\
Getting a working graphical environment (including popular desktops like [KDE](https://wiki.gentoo.org/wiki/KDE "KDE") and [GNOME](https://wiki.gentoo.org/wiki/GNOME "GNOME")) requires additional configuration **before** emerging one of these packages. See the more extensive [Xorg Guide](https://wiki.gentoo.org/wiki/Xorg/Guide "Xorg/Guide") for details.

## [Troubleshooting]

### [X server starts and dies unexpectedly with no errors]

**Problem**: Running [startx] will start the X server, however it will immediately die without any errors (searching \"`EE`\" in [/var/log/Xorg.0.log] returns no related results).

**Cause**: an empty [.xinitrc] file exists for the user who is running the [startx] command, so the X server is starting, then stopping because there is nothing left for it to do.

**Resolution**: Either remove the [.xinitrc] file or define a window manager inside it.

**Reproducible** via:

`user `[`$`]`touch ~/.xinitrc`

### [Blockers when updating xorg-server with xorg-drivers]

When an update is available for xorg-server, it is possible that a normal -up world command will produce blocker messages with xorg drivers. When this happens, rebuilding x11 modules can help proceed with the update Ex:

`root `[`#`]`emerge -av1 xorg-server @x11-module-rebuild`

## [See also]

-   [Non root Xorg](https://wiki.gentoo.org/wiki/Non_root_Xorg "Non root Xorg") --- describes how an unprivileged user can run [Xorg] without using suid.
-   [Xorg/Guide](https://wiki.gentoo.org/wiki/Xorg/Guide "Xorg/Guide") --- explains what Xorg is, how to install it, and the various configuration options.
-   [Xorg/Hardware 3D acceleration guide](https://wiki.gentoo.org/wiki/Xorg/Hardware_3D_acceleration_guide "Xorg/Hardware 3D acceleration guide") --- a guide to getting 3D acceleration working using the DRM with Xorg in Gentoo.
-   [Xrandr](https://wiki.gentoo.org/wiki/Xrandr "Xrandr") --- [X](https://wiki.gentoo.org/wiki/X "X") protocol extension and its CLI tool [xrandr] are used to manage screen resolutions, rotation and screens with multiply displays in X
-   [Xorg/Using the numeric keyboard keys as mouse](https://wiki.gentoo.org/wiki/Xorg/Using_the_numeric_keyboard_keys_as_mouse "Xorg/Using the numeric keyboard keys as mouse") --- XOrg comes with built-in mouse emulation using the keyboards numeric keypad.
-   [X server](https://wiki.gentoo.org/wiki/X_server "X server") --- the main component of the X Window system which abstracts the hardware and provides the foundation for most graphical user interfaces, like [desktop environments](https://wiki.gentoo.org/wiki/Desktop_environment "Desktop environment") or [window managers](https://wiki.gentoo.org/wiki/Window_manager "Window manager"), and their applications.