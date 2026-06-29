**Resources**

[[]][GitHub](https://github.com/niri-wm/niri)

[[]][Official documentation](https://niri-wm.github.io/niri/)

Niri is a scrollable-tiling [Wayland](https://wiki.gentoo.org/wiki/Wayland "Wayland") compositor.

## Contents

-   [[1] [Installation]](#Installation)
-   [[2] [Usage]](#Usage)
    -   [[2.1] [Invocation]](#Invocation)
        -   [[2.1.1] [Display Manager]](#Display_Manager)
    -   [[2.2] [Sound]](#Sound)
    -   [[2.3] [Portals]](#Portals)
    -   [[2.4] [Polkit]](#Polkit)
    -   [[2.5] [MATE polkit]](#MATE_polkit)
    -   [[2.6] [Xwayland satellite]](#Xwayland_satellite)
    -   [[2.7] [Dark Mode]](#Dark_Mode)
    -   [[2.8] [Application Launcher]](#Application_Launcher)
    -   [[2.9] [File Manager]](#File_Manager)
    -   [[2.10] [Wallpaper]](#Wallpaper)
        -   [[2.10.1] [swaybg]](#swaybg)
        -   [[2.10.2] [awww]](#awww)
    -   [[2.11] [OBS]](#OBS)
    -   [[2.12] [Nvidia]](#Nvidia)
-   [[3] [Troubleshooting]](#Troubleshooting)
    -   [[3.1] [Niri doesn\'t start properly]](#Niri_doesn.27t_start_properly)
-   [[4] [See also]](#See_also)

## [Installation]

** Note**\
The Niri ebuild resides in the [GURU respository](https://wiki.gentoo.org/wiki/Project:GURU "Project:GURU"). The following instructions assume that this repository is set up on your machine. If this is not the case, follow the [GURU setup instructions.](https://wiki.gentoo.org/wiki/Project:GURU/Information_for_End_Users "Project:GURU/Information for End Users")

First, unmask niri:

[FILE] **`/etc/portage/package.accept_keywords/niri`**

    gui-wm/niri ~amd64

Emerge niri:

`root `[`#`]`emerge --ask gui-wm/niri`

## [Usage]

### [Invocation]

To start niri on systemd:

`user `[`$`]`niri-session`

To start niri under [OpenRC](https://wiki.gentoo.org/wiki/OpenRC "OpenRC"):

`user `[`$`]`dbus-run-session niri --session`

#### [Display Manager]

Niri should support most [Display Managers](https://wiki.gentoo.org/wiki/Display_manager "Display manager"), but if on OpenRC, some additional tweaking might be needed.

[SDDM](https://wiki.gentoo.org/wiki/SDDM "SDDM") should work out of the box with niri, however, on OpenRC, you must change the .desktop file to not use the \"niri-session\" binary:

[FILE] **`/usr/share/wayland-sessions/niri.desktop`**

    [Desktop Entry]
    Name=Niri
    Comment=A scrollable-tiling Wayland compositor
    # Replaced "niri-session" with "niri --session". You might also wanna add "dbus-run-session" next to it.
    Exec=niri --session
    Type=Application
    DesktopNames=niri

[GDM](https://wiki.gentoo.org/wiki/GDM "GDM") can be used, however it will fallback to X11 if a user is on the Nvidia Proprietary driver and on OpenRC, and will thus be unable to launch a Wayland session. On OpenRC, just like SDDM, you will also need to change the .desktop file to not use \"niri-session\".

Greetd should work with niri as well, as long as your greeter is properly setup. Below is an example configuration using Tuigreet as the greeter:

[FILE] **`/etc/greetd/config.toml`**

    [terminal]
    vt = 1

    [default_session]
    command = "tuigreet --cmd /etc/greetd/niri.sh"
    user = "greeter"

The \"niri.sh\" script should contain the following:

[FILE] **`/etc/greetd/niri.sh`**

    #!/bin/sh

    # Uncomment the appropriate line based on your init system.

    # For systemd:
    niri-session

    # For OpenRC, use niri --session:
    # dbus-run-session niri --session

You may also need to set additional environment variables, depending on your setup.

### [Sound]

[PulseAudio](https://wiki.gentoo.org/wiki/PulseAudio "PulseAudio"), [ALSA](https://wiki.gentoo.org/wiki/ALSA "ALSA"), etc. should work as sound servers, however [PipeWire](https://wiki.gentoo.org/wiki/PipeWire "PipeWire") integrates with Wayland very well. It is also required for screen recording.

View the respective wiki pages for instructions on how to set them up.

### [Portals]

Portals are required for Flatpaks to integrate with the desktop. Refer to the [XDG/xdg-desktop-portal](https://wiki.gentoo.org/wiki/XDG/xdg-desktop-portal "XDG/xdg-desktop-portal") page for information about portals.

Emerge [[[sys-apps/xdg-desktop-portal]](https://packages.gentoo.org/packages/sys-apps/xdg-desktop-portal)[]] and [[[sys-apps/xdg-desktop-portal-gnome]](https://packages.gentoo.org/packages/sys-apps/xdg-desktop-portal-gnome)[]], which is required for screen sharing:

`root `[`#`]`emerge --ask xdg-desktop-portal xdg-desktop-portal-gnome`

Niri must be run with the [niri-session] script to run portals, either through a display manager or manually.

On OpenRC, this would be

`user `[`$`]`dbus-run-session niri --session`

### [Polkit]

Polkit is necessary for a user to mount drives in a file manager, such as Nautilus. There are a few choices in polkit authentication agents, but there are some caveats in most.

GNOME polkit is deprecated as it was added to Gnome Shell, and has not received an update in some time.

Plasma polkit works, but will not respect the user\'s [Qt](https://wiki.gentoo.org/wiki/Qt "Qt") theme.

### [MATE polkit]

MATE polkit respects the user\'s [GTK](https://wiki.gentoo.org/wiki/GTK "GTK") theme and has been updated.

First, emerge [[[mate-extra/mate-polkit]](https://packages.gentoo.org/packages/mate-extra/mate-polkit)[]]:

`root `[`#`]`emerge --ask mate-polkit`

Add the following line to niri configuration for OpenRC:

[FILE] **`~/.config/niri/config.kdl`**

    spawn-at-startup "/usr/libexec/polkit-mate-authentication-agent-1"

### [Xwayland satellite]

Xwayland-satellite is required to run programs like Steam in Wayland environments, if the compositor does not support xwayland natively.

** Note**\
Niri is able to automatically launch xwayland-satellite and set DISPLAY without modifying the configuration since release 25.08, it is sufficient to only install xwayland-satellite now.

Unmask xwayland-satellite:

[FILE] **`/etc/portage/package.accept_keywords/xwayland-satellite`**

    gui-apps/xwayland-satellite ~amd64

Emerge [[[gui-apps/xwayland-satellite]](https://packages.gentoo.org/packages/gui-apps/xwayland-satellite)[]] from GURU:

`root `[`#`]`emerge --ask gui-apps/xwayland-satellite`

add the following to niri configuration file:

[FILE] **`~/.config/niri/config.kdl`**

    spawn-at-startup "xwayland-satellite"
    environment

Launch steam with the following command, to launch Steam as a Flatpak:

`user `[`$`]`env DISPLAY=:0 flatpak run com.valvesoftware.Steam`

### [Dark Mode]

Niri reads dark or light theme from Gnome Settings. To change from light to dark mode, write the following command in the terminal:

`user `[`$`]`dconf write /org/gnome/desktop/interface/color-scheme '"prefer-dark"'`

### [Application Launcher]

The default configuration of niri supports fuzzel.

Emerge fuzzel from GURU:

`root `[`#`]`emerge --ask gui-apps/fuzzel`

Fuzzel can be invoked with super+D.

### [File Manager]

By default, niri uses Nautilus as the file manager.

Emerge Nautilus:

`root `[`#`]`emerge --ask gnome-base/nautilus`

### [Wallpaper]

There are 2 options for wallpapers on Niri: [[[gui-apps/swaybg]](https://packages.gentoo.org/packages/gui-apps/swaybg)[]] and [awww](https://wiki.gentoo.org/wiki/Awww "Awww").

#### [swaybg]

Emerge swaybg:

`root `[`#`]`emerge --ask gui-apps/swaybg`

start swaybg in the Niri configuration:

[FILE] **`~/.config/niri/config.kdl`**

    spawn-sh-at-startup "swaybg -m fill -i /home/larry/wallpapers/Super_Cool_Wallpaper.png"

select a wallpaper with swaybg:

`user `[`$`]`swaybg -i /path/to/image.png`

#### [awww]

Unmask awww

[FILE] **`/etc/portage/package.accept_keywords/awww`**

    gui-apps/awww ~amd64

Emerge awww:

`root `[`#`]`emerge --ask gui-apps/awww`

start the awww daemon in the Niri configuration:

[FILE] **`~/.config/niri/config.kdl`**

    spawn-at-startup "awww-daemon"

select a wallpaper with awww:

`user `[`$`]`awww img /path/to/image.png`

### [OBS]

OBS allows a user to record their desktop. Some use flags may need to be enabled before OBS can screen share.

[FILE] **`/etc/portage/make.conf`make.conf file**

    USE="screencast gstreamer gles2"

### [Nvidia]

If you have flickering or artifacting with Nvidia you can try:

-   Check out [upstream suggestions](https://yalter.github.io/niri/Getting-Started#nvidia).
-   Set nvidia_drm.modeset=1 kernel param.
-   Enable(/Disable) [variable-refresh-rate](https://yalter.github.io/niri/Configuration%3A-Outputs#variable-refresh-rate) in both niri and your monitor(s) config.

## [Troubleshooting]

### [][Niri doesn\'t start properly]

If Niri doesn\'t seem to start properly, with no output from Niri after a `loaded config` message, check that the [VIDEO_CARDS](https://wiki.gentoo.org/wiki//etc/portage/make.conf#VIDEO_CARDS "/etc/portage/make.conf") `USE_EXPAND` variable is configured correctly in [[make.conf](https://wiki.gentoo.org/wiki//etc/portage/make.conf "/etc/portage/make.conf")].

## [See also]

-   [Wayland](https://wiki.gentoo.org/wiki/Wayland "Wayland") --- a [communication protocol](https://en.wikipedia.org/wiki/communication_protocol "wikipedia:communication protocol") between a [display server](https://en.wikipedia.org/wiki/display_server "wikipedia:display server") and its clients
-   [List of software for Wayland](https://wiki.gentoo.org/wiki/List_of_software_for_Wayland "List of software for Wayland") --- various desktop related packages for Wayland