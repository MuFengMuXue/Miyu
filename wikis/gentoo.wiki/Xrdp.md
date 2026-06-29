**Resources**

[[]][Home](https://www.xrdp.org/)

[[]][Man page](https://linux.die.net/man/8/xrdp)

[[]][Wikipedia](https://en.wikipedia.org/wiki/xrdp "wikipedia:xrdp")

**xrdp** is an open source [RDP](https://en.wikipedia.org/wiki/RDP "wikipedia:RDP") server that supports many session runners.

One of the runners, [xorgxrdp], starts a standalone [X11](https://wiki.gentoo.org/wiki/X11 "X11") server. In this guide we\'ll use it.

## Contents

-   [[1] [Features]](#Features)
-   [[2] [Installation]](#Installation)
    -   [[2.1] [Emerge]](#Emerge)
-   [[3] [Configuration]](#Configuration)
    -   [[3.1] [Example Window Manager Xrdp startup configuration]](#Example_Window_Manager_Xrdp_startup_configuration)
    -   [[3.2] [Service]](#Service)
        -   [[3.2.1] [OpenRC]](#OpenRC)
        -   [[3.2.2] [systemd]](#systemd)
-   [[4] [Audio support]](#Audio_support)

## [Features]

-   Two-way clipboard transfer
-   Drive redirection (mount local client drives on remote machine)
-   [TLS](https://en.wikipedia.org/wiki/TLS "wikipedia:TLS") encryption
-   Proxying RDP and [VNC](https://en.wikipedia.org/wiki/VNC "wikipedia:VNC")
-   Reconnect to an existing session

## [Installation]

### [Emerge]

Enable the [dilfridge](https://repos.gentoo.org/#dilfridge) repository:

`root `[`#`]`eselect repository enable dilfridge `

`root `[`#`]`emaint sync -r dilfridge `

Install xorgxrdp:

`root `[`#`]`emerge --ask net-misc/xorgxrdp`

## [Configuration]

The configuration file is installed into [/etc/xrdp/xrdp.ini], the configuration file for session management parameters into [/etc/xrdp/sesman.ini].

The default system-wide [startwm.sh] respects \$XSESSION variable set in [/etc/profile]. Without additional configuration, xrdp will start Xorg with the startup of [/etc/xrdp/xrdp.ini].

The default per-user windows manager startup script is [\~/startwm.sh]

### [Example Window Manager Xrdp startup configuration]

Change file name of per-user windows manager startup script to something more explicit and make it a dot file.

[FILE] **`/etc/xrdp/sesman.ini`**

    [Globals]
    ; Give in relative path to user's home directory
    ; UserWindowManager=startwm.sh
    UserWindowManager=.start_xrdpwm.sh

Example startup script for [Xfce](https://wiki.gentoo.org/wiki/Xfce "Xfce").

[FILE] **`$HOME/.start_xfcewm.sh`Startup script for Xfce4**

    #!/bin/sh

    # Setup XRDP specific config directory / environment variables
    # so that the XRDP desktop can have different parameters from
    # any possible local / physical display Xdisplay

    [ -d $HOME/.config/xfce4-xrdp ] && mkdir -p $HOME/.config/xfce4-xrdp
    [ -d $HOME/.cache/xfce4-xrdp ]  && mkdir -p $HOME/.cache/xfce4-xrdp
    export XDG_CONFIG_HOME=$HOME/.config/xfce4-xrdp
    export XDG_CACHE_HOME=$HOME/.cache/xfce4-xrdp

    exec xfce4-session

### [Service]

To start xrdp at boot, run the following commands:

#### [OpenRC]

`root `[`#`]`rc-service xrdp start `

`root `[`#`]`rc-update add xrdp default `

#### [systemd]

`root `[`#`]`systemctl start xrdp.service `

`root `[`#`]`systemctl enable xrdp.service `

## [Audio support]

Enable the [GURU](https://wiki.gentoo.org/wiki/GURU "GURU") repository:

`root `[`#`]`eselect repository enable guru `

`root `[`#`]`emaint sync -r guru `

Install the xrdp module for [Pipewire](https://wiki.gentoo.org/wiki/Pipewire "Pipewire"):

`root `[`#`]`emerge --ask media-sound/pipewire-module-xrdp`

The module will load automatically via XDG autostart if xrdp session is detected.