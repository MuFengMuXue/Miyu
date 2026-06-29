**Resources**

[[]][Home](https://flatpak.github.io/xdg-desktop-portal/)

[[]][Package information](https://packages.gentoo.org/packages/sys-apps/xdg-desktop-portal)

**[xdg-desktop-portal]** is a frontend to implementations of the xdg-desktop-portal interface. Backend implementations available on Gentoo include:

-   [[[sys-apps/xdg-desktop-portal-gnome]](https://packages.gentoo.org/packages/sys-apps/xdg-desktop-portal-gnome)[]]
-   [[[sys-apps/xdg-desktop-portal-gtk]](https://packages.gentoo.org/packages/sys-apps/xdg-desktop-portal-gtk)[]]
-   [[[kde-plasma/xdg-desktop-portal-kde]](https://packages.gentoo.org/packages/kde-plasma/xdg-desktop-portal-kde)[]]
-   [[[gui-libs/xdg-desktop-portal-lxqt]](https://packages.gentoo.org/packages/gui-libs/xdg-desktop-portal-lxqt)[]]
-   [[[gui-libs/xdg-desktop-portal-wlr]](https://packages.gentoo.org/packages/gui-libs/xdg-desktop-portal-wlr)[]]
-   [[[sys-apps/xdg-desktop-portal-xapp]](https://packages.gentoo.org/packages/sys-apps/xdg-desktop-portal-xapp)[]] (for Cinnamon, MATE, and Xfce4)

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
-   [[2] [Configuration]](#Configuration)
-   [[3] [Usage]](#Usage)
    -   [[3.1] [KDE]](#KDE)
-   [[4] [Troubleshooting]](#Troubleshooting)
    -   [[4.1] [Backends not starting]](#Backends_not_starting)
-   [[5] [See also]](#See_also)

## [Installation]

### [USE flags]

### [USE flags for] [sys-apps/xdg-desktop-portal](https://packages.gentoo.org/packages/sys-apps/xdg-desktop-portal) [[]] [Desktop integration portal]

  ------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------
  [`flatpak`](https://packages.gentoo.org/useflags/flatpak)           Enable sys-apps/flatpak integration
  [`geolocation`](https://packages.gentoo.org/useflags/geolocation)   Enable physical position determination
  [`gstreamer`](https://packages.gentoo.org/useflags/gstreamer)       Add support for media-libs/gstreamer (Streaming media)
  [`seccomp`](https://packages.gentoo.org/useflags/seccomp)           Use sys-apps/bubblewrap (which requires seccomp) to sandbox some functionality like icon handling
  [`systemd`](https://packages.gentoo.org/useflags/systemd)           Enable use of systemd-specific libraries and features like socket activation or session tracking
  [`test`](https://packages.gentoo.org/useflags/test)                 Enable dependencies and/or preparations necessary to run tests (usually controlled by FEATURES=test but can be toggled independently)
  [`udev`](https://packages.gentoo.org/useflags/udev)                 Enable virtual/udev integration (device discovery, power and storage device support, etc)
  ------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-04-24 12:37] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

`root `[`#`]`emerge --ask sys-apps/xdg-desktop-portal`

After installing [[[sys-apps/xdg-desktop-portal]](https://packages.gentoo.org/packages/sys-apps/xdg-desktop-portal)[]], ensure that one or more implementations appropriate to the system environment are installed (e.g. [[[gui-libs/xdg-desktop-portal-wlr]](https://packages.gentoo.org/packages/gui-libs/xdg-desktop-portal-wlr)[]]).

The following table describes the Portal interfaces (e.g. `org.freedesktop.portal.FileChooser`) implemented by backends (e.g. [[[gui-libs/xdg-desktop-portal-xapp]](https://packages.gentoo.org/packages/gui-libs/xdg-desktop-portal-xapp)[]]). Note that a given environment might implement a particular interface outside of its backend - for example, in KDE, the `Secret` interface is implemented by [[[kde-frameworks/kwallet]](https://packages.gentoo.org/packages/kde-frameworks/kwallet)[]].

  ----------------------- ----------------------------------------------------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------------------- --------------------------------------------------------------------------------------------------------------- --------------------------------------------------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------
  Interface               [gnome](https://packages.gentoo.org/packages/sys-apps/xdg-desktop-portal-gnome)   [gtk](https://packages.gentoo.org/packages/sys-apps/xdg-desktop-portal-gtk)   [hyprland](https://packages.gentoo.org/packages/sys-apps/xdg-desktop-portal-hyprland)   [kde](https://packages.gentoo.org/packages/kde-plasma/xdg-desktop-portal-kde)   [lxqt](https://packages.gentoo.org/packages/gui-libs/xdg-desktop-portal-lxqt)   [wlr](https://packages.gentoo.org/packages/gui-libs/xdg-desktop-portal-wlr)   [xapp](https://packages.gentoo.org/packages/sys-apps/xdg-desktop-portal-xapp)
  Access
  Account
  AppChooser
  Background
  Camera
  Clipboard
  Documents
  Dynamic Launcher
  Email
  File Chooser
  File Transfer
  Game Mode
  Global Shortcuts
  Inhibit
  Input Capture
  Location
  Lockdown
  Memory Monitor
  Network Monitor
  Notification
  OpenURI
  Power Profile Monitor
  Print
  Proxy Resolver
  Realtime
  Remote Desktop
  Request
  ScreenCast
  Screenshot
  Secret
  Session
  Settings
  Trash
  Wallpaper
  ----------------------- ----------------------------------------------------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------------------- --------------------------------------------------------------------------------------------------------------- --------------------------------------------------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------

## [Configuration]

As described in the [[[portals.conf(5)]](https://man.archlinux.org/man/portals.conf.5.en)[[]](https://wiki.gentoo.org/wiki/Special:MyLanguage/man_page "Special:MyLanguage/man page")] man page, **xdg-desktop-portal** is configured via one or more files:

-   [\$XDG_CONFIG_HOME/xdg-desktop-portal/portals.conf]
-   [\$XDG_CONFIG_DIRS/xdg-desktop-portal/portals.conf]
-   [/etc/xdg-desktop-portal/portals.conf]
-   [\$XDG_DATA_HOME/xdg-desktop-portal/portals.conf]
-   [\$XDG_DATA_DIRS/xdg-desktop-portal/portals.conf]
-   [/usr/share/xdg-desktop-portal/portals.conf]

If none of these files are present, create a simple [portals.conf] file:

[FILE] **`~/.config/xdg-desktop-portal/portals.conf`Example portals.conf file**

    [preferred]
    # Use xdg-desktop-portal-gtk for every portal interface...
    default=gtk
    # ... except for the Screencast, Screenshot and Settings (dark/light mode) interface
    org.freedesktop.impl.portal.Screencast=wlr
    org.freedesktop.impl.portal.Screenshot=wlr
    org.freedesktop.impl.portal.Settings=darkman

Each xdg-desktop-portal implementation has a configuration file itself; refer to the relevant package\'s documentation (e.g. [[[xdg-desktop-portal-wlr(5)]](https://man.archlinux.org/man/xdg-desktop-portal-wlr.5.en)[[]](https://wiki.gentoo.org/wiki/Special:MyLanguage/man_page "Special:MyLanguage/man page")]) for details.

If using a portal in a desktop environment other than the one for which it was designed (e.g. using the GNOME portal with Sway), you may need to modify the relevant portal file in [/usr/share/xdg-desktop-portal/portals/], adding the value of `XDG_CURRENT_DESKTOP` to the value of the `UseIn` key, e.g.:

[FILE] **`/usr/share/xdg-desktop-portal/portals/gnome.portal`**

    [portal]
    DBusName=org.freedesktop.impl.portal.desktop.gnome
    Interfaces=org.freedesktop.impl.portal.Account;org.freedesktop.impl.portal.AppChooser;org.freedesktop.impl.portal.Screenshot;org.freedesktop.impl.portal.ScreenCast;org.freedesktop.impl.portal.RemoteDesktop;org.freedesktop.impl.portal.Lockdown;org.freedesktop.impl.portal.Background;org.freedesktop.impl.portal.Settings;org.freedesktop.impl.portal.Wallpaper;org.freedesktop.impl.portal.FileChooser;org.freedesktop.impl.portal.Print;org.freedesktop.impl.portal.DynamicLauncher;
    UseIn=gnome;sway;

** Note**\
The `UseIn` key is [deprecated](https://github.com/flatpak/xdg-desktop-portal/commit/939f0b0fcec6a42c1acdc397986547e9805359ff), superseded by portals.conf files as described above. However, they are still in active use as of 2023-12-24.

## [Usage]

**xdg-desktop-portal** is usually not called manually; instead, other programs call it as required. However, you can run it manually to debug your configuration, using the `-v` option:

`user `[`$`]`/usr/libexec/xdg-desktop-portal -v`

This can be used to display the configuration found by xdg-desktop-portal:

`user `[`$`]`/usr/libexec/xdg-desktop-portal -v 2>&1 | grep 'Found' | sort | uniq`

    XDP: Found 'gnome' in configuration for default
    XDP: Found 'gtk' in configuration for default
    XDP: Found 'gtk' in configuration for org.freedesktop.impl.portal.FileChooser
    XDP: Found 'wlr;gtk;gnome' in configuration for default
    XDP: Found 'wlr' in configuration for default
    XDP: Found 'wlr' in configuration for org.freedesktop.impl.portal.Screenshot

and which portals will be used for interfaces:

`user `[`$`]`/usr/libexec/xdg-desktop-portal -v 2>&1 | grep 'Using'`

    XDP: Using portal configuration file '<HOME>/.config/xdg-desktop-portal/portals.conf' for non-specific desktop
    XDP: Using gnome.portal for org.freedesktop.impl.portal.Lockdown (config)
    XDP: Using gtk.portal for org.freedesktop.impl.portal.Settings (config)
    XDP: Using gnome.portal for org.freedesktop.impl.portal.Settings (config)
    XDP: Using gtk.portal for org.freedesktop.impl.portal.FileChooser (config)
    XDP: Using gtk.portal for org.freedesktop.impl.portal.AppChooser (config)
    XDP: Using gtk.portal for org.freedesktop.impl.portal.Print (config)
    XDP: Using gtk.portal for org.freedesktop.impl.portal.Notification (config)
    XDP: Using gtk.portal for org.freedesktop.impl.portal.Inhibit (config)
    ...

### [KDE]

In addition to xdg-desktop-portal-kde, the KDE Community Wiki [recommends](https://community.kde.org/Distributions/Packaging_Recommendations) also installing xdg-desktop-portal-gtk, to sync font settings to Flatpak apps when run in Plasma.

## [Troubleshooting]

### [Backends not starting]

This can result in issues like screensharing not working.

If [portals.conf] contains e.g.:

[FILE] **`$/xdg-desktop-portal/portals.conf`**

    [preferred]
    default=wlr;gtk

to use the -wlr and -gtk backends, yet neither are running (in addition to [xdg-desktop-portal] itself) once the [window manager](https://wiki.gentoo.org/wiki/Window_manager "Window manager") (WM) or compositor has started, it might be that the activation environment of the D-Bus session needs to be updated. This should be done after starting the WM/compositor (e.g. in the startup file run by the WM/compositor).

If using systemd, this can be done via:

`user `[`$`]`dbus-update-activation-environment --systemd WAYLAND_DISPLAY XDG_CURRENT_DESKTOP=<value> `

`user `[`$`]`systemctl --user restart xdg-desktop-portal `

where \"\<value\>\" should be replaced by a value appropriate for the compositor, e.g. `wlroots` (for various [wlroots-based compositors](https://wiki.gentoo.org/wiki/List_of_software_for_Wayland#Compositors "List of software for Wayland")) or the specific name of the compositor (e.g. `sway`).

If started with [xdg-desktop-portal], this can be done via:

`user `[`$`]`dbus-update-activation-environment WAYLAND_DISPLAY XDG_CURRENT_DESKTOP=<value> `

`user `[`$`]`/usr/libexec/xdg-desktop-portal -r `

Or, if using OpenRC [user services](https://wiki.gentoo.org/wiki/OpenRC#User_services "OpenRC"):

`user `[`$`]`dbus-update-activation-environment WAYLAND_DISPLAY XDG_CURRENT_DESKTOP=<value> `

`user `[`$`]`rc-service --user xdg-desktop-portal restart `

## [See also]

-   [The xdg-desktop-portal project page](https://flatpak.github.io/xdg-desktop-portal/)
-   The [[[portals.conf(5)]](https://man.archlinux.org/man/portals.conf.5.en)[[]](https://wiki.gentoo.org/wiki/Special:MyLanguage/man_page "Special:MyLanguage/man page")] man page