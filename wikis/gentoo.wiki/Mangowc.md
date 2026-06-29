**Resources**

[[]][GitHub](https://github.com/mangowm/mango)

[[]][Official documentation](https://mangowm.github.io/docs)

[[]][Official project wiki](https://github.com/mangowm/mango/wiki)

MangoWM is a [Wayland](https://wiki.gentoo.org/wiki/Wayland "Wayland") Compositor based on [wlroots](https://wiki.gentoo.org/wiki/Wlroots "Wlroots") and scenefx.

## Contents

-   [[1] [Installation]](#Installation)
-   [[2] [Usage]](#Usage)
    -   [[2.1] [Invocation]](#Invocation)
    -   [[2.2] [Configuration]](#Configuration)
    -   [[2.3] [Terminal emulator]](#Terminal_emulator)
    -   [[2.4] [Launcher]](#Launcher)
    -   [[2.5] [Essential Keybindings]](#Essential_Keybindings)
-   [[3] [See also]](#See_also)

## [Installation]

** Note**\
MangoWM and its dependency SceneFX are available in the [GURU repository](https://wiki.gentoo.org/wiki/Project:GURU "Project:GURU"). Before proceeding with the installation, ensure this repository has been enabled on the system. Instructions for setting up GURU can be found at [GURU setup page](https://wiki.gentoo.org/wiki/Project:GURU/Information_for_End_Users "Project:GURU/Information for End Users").

First, unmask MangoWM and SceneFX:

[FILE] **`/etc/portage/package.accept_keywords/mango`**

    gui-wm/mangowm ~amd64
    gui-libs/scenefx ~amd64

Emerge MangoWM:

`root `[`#`]`emerge --ask gui-wm/mangowm`

## [Usage]

### [Invocation]

To start Mango on systemd:

`user `[`$`]`mango`

To start Mango under [OpenRC](https://wiki.gentoo.org/wiki/OpenRC "OpenRC"):

`user `[`$`]`dbus-run-session mango`

### [Configuration]

Copy the default configuration file to the user directory:

`user `[`$`]`mkdir -p ~/.config/mango/ `

`user `[`$`]`cp /etc/mango/config.conf ~/.config/mango/config.conf `

### [Terminal emulator]

By default, the MangoWM configuration file uses [[[gui-apps/foot]](https://packages.gentoo.org/packages/gui-apps/foot)[]] as the [terminal emulator](https://wiki.gentoo.org/wiki/Terminal_emulator "Terminal emulator"). It is recommended to install this terminal emulator to ensure a terminal will be available once MangoWM is running:

`root `[`#`]`emerge --ask gui-apps/foot`

** Tip**\
Other popular options include [[[x11-terms/alacritty]](https://packages.gentoo.org/packages/x11-terms/alacritty)[]] or [[[x11-terms/kitty]](https://packages.gentoo.org/packages/x11-terms/kitty)[]], which are GPU-accelerated and work natively with Wayland.

### [Launcher]

By default, the MangoWM configuration file uses [[[x11-misc/rofi]](https://packages.gentoo.org/packages/x11-misc/rofi)[]] as the application launcher. It is recommended to install this launcher to ensure that programs can be opened when MangoWM is running.

`root `[`#`]`emerge --ask x11-misc/rofi`

** Tip**\
[[[gui-apps/wofi]](https://packages.gentoo.org/packages/gui-apps/wofi)[]] is a popular option as a launcher.

### [Essential Keybindings]

-   [Alt]+[Return] = Open Terminal (defaults to [[[gui-apps/foot]](https://packages.gentoo.org/packages/gui-apps/foot)[]]).
-   [Alt]+[Space] = Open Launcher (defaults to [[[x11-misc/rofi]](https://packages.gentoo.org/packages/x11-misc/rofi)[]]).
-   [Alt]+[Q] = Close (Kill) the active window.
-   [Super]+[M] = Quit MangoWC.
-   [Super]+[F] = Toggle Fullscreen.
-   [Ctrl]+[1-9] = Switch to Tag 1-9.
-   [Alt]+[1-9] = Move window to Tag 1-9.

## [See also]

-   [Wayland](https://wiki.gentoo.org/wiki/Wayland "Wayland") --- a [communication protocol](https://en.wikipedia.org/wiki/communication_protocol "wikipedia:communication protocol") between a [display server](https://en.wikipedia.org/wiki/display_server "wikipedia:display server") and its clients
-   [List of software for Wayland](https://wiki.gentoo.org/wiki/List_of_software_for_Wayland "List of software for Wayland") --- various desktop related packages for Wayland