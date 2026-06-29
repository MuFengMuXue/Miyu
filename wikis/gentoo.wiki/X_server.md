**Resources**

[[]][Home](http://www.x.org)

[[]][Wikipedia](https://en.wikipedia.org/wiki/X_Window_System "wikipedia:X Window System")

The **X.Org server**, part of the X.Org releases, is the main component of the X Window system which abstracts the hardware and provides the foundation for most graphical user interfaces, like [desktop environments](https://wiki.gentoo.org/wiki/Desktop_environment "Desktop environment") or [window managers](https://wiki.gentoo.org/wiki/Window_manager "Window manager"), and their applications.

Functionality of the X.Org server is handled by [Xwayland](https://wiki.gentoo.org/wiki/Wayland#X-native_app_support_.28XWayland.29 "Wayland") on systems running the [Wayland](https://wiki.gentoo.org/wiki/Wayland "Wayland") protocol.

** See also**\
This page provides useful information but the [Xorg guide](https://wiki.gentoo.org/wiki/Xorg/Guide "Xorg/Guide") details the installation of Xorg in a more convenient manner. See also [Xorg](https://wiki.gentoo.org/wiki/Xorg "Xorg").

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [mesa]](#mesa)
    -   [[1.3] [xorg-drivers]](#xorg-drivers)
    -   [[1.4] [xorg-server]](#xorg-server)
-   [[2] [Configuration]](#Configuration)
    -   [[2.1] [Permissions]](#Permissions)
    -   [[2.2] [xorg.conf]](#xorg.conf)
    -   [[2.3] [Boot service]](#Boot_service)
-   [[3] [See also]](#See_also)

## [Installation]

Installing xorg-server is much lighter than emerging the entire xorg package, and has all the necessary components to have a fully functional GUI such as plasma for example.

** Note**\
When just updating, check the [upgrade sub-article](https://wiki.gentoo.org/wiki/X_server/upgrade "X server/upgrade").

### [USE flags]

### [mesa]

[Correctly setting](https://wiki.gentoo.org/wiki//etc/portage/make.conf#VIDEO_CARDS "/etc/portage/make.conf") [make.conf] `VIDEO_CARDS` with an entry from [Category:Video cards](https://wiki.gentoo.org/wiki/Category:Video_cards "Category:Video cards") affects the USE expand for [[[media-libs/mesa]](https://packages.gentoo.org/packages/media-libs/mesa)[]] (see [Wikipedia](https://en.wikipedia.org/wiki/Mesa_3D_(OpenGL) "wikipedia:Mesa 3D (OpenGL)")). Mesa is a graphic library that provides a generic OpenGL implementation and may already be automatically pulled in by graphics card/driver settings in [make.conf] and if a graphical profile is set. Issue the command [emerge \--search mesa] to see if mesa is already installed prior to emerging.

### [xorg-drivers]

Portage knows the `X` USE flag for enabling support for X in other packages (default in all *desktop* [profiles](https://wiki.gentoo.org/wiki/Profile_(Portage) "Profile (Portage)")). Make sure this USE flag is added to the USE flag list to ensure X compatibility system wide:

[FILE] **`/etc/portage/make.conf`**

    USE="X"

[[[x11-base/xorg-drivers]](https://packages.gentoo.org/packages/x11-base/xorg-drivers)[]] is a meta package to pull in the wanted drivers (note that these driver can be automatically pulled in if the graphics card/drivers info is set in [make.conf] and using a graphical profile) Issue the command [emerge \--search xorg-drivers] to see if xorg-drivers is already installed prior to emerging.

Make sure to follow [Input devices](https://wiki.gentoo.org/wiki/Category:Input_devices "Category:Input devices") and [INPUT_DEVICES](https://wiki.gentoo.org/wiki//etc/portage/make.conf#INPUT_DEVICES "/etc/portage/make.conf").

It is recommended to issue the `--verbose` option when emerging xorg-server because xorg-drivers or mesa may be pulled in as dependencies if they are not already installed. Using `--verbose` will show more information on USE flags and dependencies before package installation. If xorg-drivers and/or the mesa packages are emerged directly (IE without the `--one-shot` option) they will be recorded in the world file and could cause future package upgrade conflicts when Portage is upgrading dependencies. It is a best practice to allow them to be merged into the system as dependencies by setting USE flags or using a graphical [profile](https://wiki.gentoo.org/wiki/Profile_(Portage) "Profile (Portage)").

### [xorg-server]

Now install [[[x11-base/xorg-server]](https://packages.gentoo.org/packages/x11-base/xorg-server)[]].

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

`root `[`#`]`emerge --ask x11-base/xorg-server`

## [Configuration]

### [Permissions]

If the [`acl`](https://packages.gentoo.org/useflags/acl) USE flag is enabled globally and [`elogind`](https://packages.gentoo.org/useflags/elogind) is being used (default for desktop profiles) permissions to video cards will be handled automatically. It is possible to check the permissions using [getfacl]:

`user `[`$`]`getfacl /dev/dri/card0 | grep larry`

`user:`**`larry`**`:rw-`

A broader solution is to add the user(s) needing access the video card to the [video] group:

`root `[`#`]`gpasswd -a larry video`

Note that users will be able to run X without permission to the DRI subsystem, but hardware acceleration will be disabled.

### [xorg.conf]

The X server is designed to work out-of-the-box, with no need to manually edit Xorg\'s configuration files. It should detect and configure devices such as displays, keyboards, and mice.

However, the main configuration file of the X server is the [[xorg.conf](https://wiki.gentoo.org/wiki/Xorg.conf "Xorg.conf")].

### [Boot service]

Usually the X server is started by starting a [display manager](https://wiki.gentoo.org/wiki/Display_manager "Display manager") automatically on boot.

## [See also]

-   [Non root Xorg](https://wiki.gentoo.org/wiki/Non_root_Xorg "Non root Xorg") --- describes how an unprivileged user can run [Xorg](https://wiki.gentoo.org/wiki/Xorg "Xorg") without using suid.
-   [Xorg](https://wiki.gentoo.org/wiki/Xorg "Xorg") --- an open source implementation of the [X server].
-   [Xorg/Guide](https://wiki.gentoo.org/wiki/Xorg/Guide "Xorg/Guide") --- explains what Xorg is, how to install it, and the various configuration options.
-   [Xrandr](https://wiki.gentoo.org/wiki/Xrandr "Xrandr") --- [X](https://wiki.gentoo.org/wiki/X "X") protocol extension and its CLI tool [xrandr] are used to manage screen resolutions, rotation and screens with multiply displays in X