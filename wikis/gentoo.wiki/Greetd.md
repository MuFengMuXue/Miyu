This page contains [[changes](https://wiki.gentoo.org/index.php?title=Greetd&diff=1434617)] which are not marked for translation.

**Resources**

[[]][Home](https://git.sr.ht/~kennylevinsen/greetd)

[[]][Package information](https://packages.gentoo.org/packages/gui-apps/gtkgreet)

[[]][Official documentation](https://man.sr.ht/~kennylevinsen/greetd/)

[[]][[#kennylevinsen](ircs://irc.libera.chat/#kennylevinsen)] ([[webchat](https://web.libera.chat/#kennylevinsen)])

**greetd** is a minimal login manager daemon with pluggable greeter frontends.

greetd only provides a backend authentication service and is meant to be used with a frontend greeter, such as [[[gui-apps/gtkgreet]](https://packages.gentoo.org/packages/gui-apps/gtkgreet)[]], [gui-apps/qtgreet](https://github.com/bsd-ac/wayland-desktop/tree/master/gui-apps/qtgreet) or [[[gui-apps/tuigreet]](https://packages.gentoo.org/packages/gui-apps/tuigreet)[]].

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
-   [[2] [Front-ends]](#Front-ends)
    -   [[2.1] [GTKGreet]](#GTKGreet)
    -   [[2.2] [TUIGreet]](#TUIGreet)
    -   [[2.3] [QTGreet]](#QTGreet)
-   [[3] [Usage]](#Usage)
    -   [[3.1] [Preliminaries]](#Preliminaries)
        -   [[3.1.1] [OpenRC]](#OpenRC)
        -   [[3.1.2] [systemd]](#systemd)
    -   [[3.2] [GTKGreet/QTGreet + Wayfire]](#GTKGreet.2FQTGreet_.2B_Wayfire)
    -   [[3.3] [Hyprland + QTGreet]](#Hyprland_.2B_QTGreet)
        -   [[3.3.1] [Hyprland session with D-Bus (OpenRC)]](#Hyprland_session_with_D-Bus_.28OpenRC.29)
    -   [[3.4] [TUIGreet]](#TUIGreet_2)
-   [[4] [See also]](#See_also)

## [Installation]

### [USE flags]

### [USE flags for] [gui-libs/greetd](https://packages.gentoo.org/packages/gui-libs/greetd) [[]] [ipc based login daemon]

  ----------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [`debug`](https://packages.gentoo.org/useflags/debug)       Enable extra debug codepaths, like asserts and extra output. If you want to get meaningful backtraces see https://wiki.gentoo.org/wiki/Project:Quality_Assurance/Backtraces
  [`man`](https://packages.gentoo.org/useflags/man)           Build and install man pages
  [`selinux`](https://packages.gentoo.org/useflags/selinux)   !!internal use only!! Security Enhanced Linux support, this must be set by the selinux profile or breakage will occur
  ----------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2025-01-21 01:29] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

## [Front-ends]

greetd implements an authentication protocol and provides the backend service daemon implementation, integrated with [PAM](https://wiki.gentoo.org/wiki/PAM "PAM"). The frontend provided to a user, called a *greeter*, is implemented separately, with multiple greeters available.

### [GTKGreet]

[![GTKGreet.png](/images/thumb/4/42/GTKGreet.png/300px-GTKGreet.png)](https://wiki.gentoo.org/wiki/File:GTKGreet.png)

[](https://wiki.gentoo.org/wiki/File:GTKGreet.png "Enlarge")

`root `[`#`]`emerge --ask gui-apps/gtkgreet`

### [TUIGreet]

[![Tuigreet.png](/images/thumb/e/ec/Tuigreet.png/300px-Tuigreet.png)](https://wiki.gentoo.org/wiki/File:Tuigreet.png)

[](https://wiki.gentoo.org/wiki/File:Tuigreet.png "Enlarge")

`root `[`#`]`emerge --ask gui-apps/tuigreet`

### [QTGreet]

[![QTGreet.jpg](/images/thumb/9/9c/QTGreet.jpg/300px-QTGreet.jpg)](https://wiki.gentoo.org/wiki/File:QTGreet.jpg)

[](https://wiki.gentoo.org/wiki/File:QTGreet.jpg "Enlarge")

QTGreet is available from the [wayland-desktop](https://github.com/bsd-ac/wayland-desktop) overlay.

`root `[`#`]`eselect repository enable wayland-desktop `

`root `[`#`]`emaint sync --repo wayland-desktop `

`root `[`#`]`emerge --ask --verbose gui-apps/qtgreet`

## [Usage]

The GUI greeters, GTKGreet and QTGreet, need a wayland compositor to display them. The compositor used to display the greeter does not need to be the same as the one used by the user in their session. For example, it is possible to configure [sway](https://wiki.gentoo.org/wiki/Sway "Sway") to start [[[gui-apps/gtkgreet]](https://packages.gentoo.org/packages/gui-apps/gtkgreet)[]] to start a [Wayfire](https://wiki.gentoo.org/wiki/Wayfire "Wayfire") session.

A few example configurations are shown here.

### [Preliminaries]

#### [OpenRC]

Enable the [display-manager] service from [[[gui-libs/display-manager-init]](https://packages.gentoo.org/packages/gui-libs/display-manager-init)[]]

`root `[`#`]`rc-update add display-manager default`

Configure the [display-manager] service to use greetd:

[FILE] **`/etc/conf.d/display-manager`Setting greetd as the display manager**

    CHECKVT=7
    DISPLAYMANAGER="greetd"

As pointed out in the [session bus section of the dbus page](https://wiki.gentoo.org/wiki/D-Bus#The_session_bus "D-Bus"), if `echo $DBUS_SESSION_BUS_ADDRESS` returns nothing, then there is no D-Bus session bus visible to the session. In that case running the window manager using `dbus-run-session` should fix the issue

An example fix when using tuigreet to start sway:

[FILE] **`/etc/greetd/config.toml`Using tuigreet with a custom sessions directory**

    [terminal]
    vt = 7

    [default_session]
    command = "tuigreet --sessions /etc/greetd/sessions"
    user = "greetd"

Because tuigreet fetches it\'s sessions from desktop files in [/usr/share/xsessions] and [/usr/share/wayland-sessions], a custom sessions directory should be provided, because modifying the default `.desktop` file for the window manager is needed

[FILE] **`/etc/greetd/sessions/sway.desktop`Executing sway using dbus-run-session**

    [Desktop Entry]
    Name=Sway
    Comment=An i3-compatible Wayland compositor
    Exec=dbus-run-session sway
    Type=Application

#### [systemd]

Enable the [greetd] service to start on boot

`root `[`#`]`systemctl enable greetd.service`

### [][GTKGreet/QTGreet + Wayfire]

Configure greetd to use wayfire as the startup command, where wayfire will be started with a custom configuration file:

[FILE] **`/etc/greetd/config.toml`Wayfire startup on greetd**

    [terminal]
    vt = 7

    [default_session]
    command = "wayfire -c /etc/wayfire.ini"
    user = "greetd"

[FILE] **`/etc/wayfire.ini`Wayfire config to start GTKGreet/QTGreet**

    [autostart]
    autostart_wf_shell = false
    gtkgreet = /usr/bin/gtkgreet -l
    #qtgreet = /usr/bin/qtgreet

    [core]
    plugins = autostart
    vheight = 1
    vwidth = 1
    xwayland = false

### [][Hyprland + QTGreet]

greetd can be configured to start [Hyprland](https://wiki.gentoo.org/wiki/Hyprland "Hyprland") directly, where Hyprland in turn starts the greeter (such as QTGreet) via its own configuration.

Example configuration for greetd:

[FILE] **`/etc/greetd/config.toml`Hyprland startup with greetd**

    [terminal]
    vt = 7

    [default_session]
    command = "start-hyprland -- --config /etc/greetd/hyprland.conf"
    user = "greetd"

Example Hyprland configuration to launch QTGreet and exit afterward:

[FILE] **`/etc/greetd/hyprland.conf`Hyprland config to start QTGreet**

    exec-once = qtgreet; hyprctl dispatch exit

#### [][Hyprland session with D-Bus (OpenRC)]

Under OpenRC, a [dbus](https://wiki.gentoo.org/wiki/Dbus "Dbus") session is not started automatically. If a desktop environment or compositor requires dbus, it must be launched manually. The recommended method is to use [dbus-run-session], although [dbus-launch] may still work for some environments.

For example, Hyprland can be configured to start with dbus using a modified or new Wayland session file.

[FILE] **`/usr/share/wayland-sessions/hyprland-dbus.desktop`Create a D-Bus-enabled Hyprland session entry**

    [Desktop Entry]
    Name=Hyprland (with D-Bus)
    Comment=Start Hyprland with a D-Bus session
    Exec=dbus-run-session start-hyprland
    Type=Application
    DesktopNames=Hyprland

Alternatively, modify the existing Hyprland session entry:

[FILE] **`/usr/share/wayland-sessions/hyprland.desktop`Modify existing Hyprland session entry**

    [Desktop Entry]
    Name=Hyprland
    Comment=An intelligent dynamic tiling Wayland compositor
    Exec=dbus-run-session start-hyprland
    Type=Application
    DesktopNames=Hyprland
    Keywords=tiling;wayland;compositor;

### [TUIGreet]

TUIGreet does not need a compositor to be used.

[FILE] **`/etc/greetd/config.toml`TUIGreet with GreetD**

    [terminal]
    vt = 7

    [default_session]
    command = "tuigreet --cmd sway"
    user = "greetd"

## [See also]

-   [Display manager](https://wiki.gentoo.org/wiki/Display_manager "Display manager") --- presents the user with a graphical login screen to start a GUI session, either [X](https://wiki.gentoo.org/wiki/Xorg "Xorg") or [Wayland](https://wiki.gentoo.org/wiki/Wayland "Wayland").
-   [Wayland](https://wiki.gentoo.org/wiki/Wayland "Wayland") --- a [communication protocol](https://en.wikipedia.org/wiki/communication_protocol "wikipedia:communication protocol") between a [display server](https://en.wikipedia.org/wiki/display_server "wikipedia:display server") and its clients