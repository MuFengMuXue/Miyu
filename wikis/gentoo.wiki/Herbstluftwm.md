[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=Herbstluftwm&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

**Resources**

[[]][Home](https://herbstluftwm.org/)

[[]][Official documentation](https://herbstluftwm.org/news.html)

[[]][Package information](https://packages.gentoo.org/packages/x11-wm/herbstluftwm)

[[]][GitHub](https://github.com/herbstluftwm/herbstluftwm)

[[]][[#herbstluftwm](ircs://irc.libera.chat/#herbstluftwm)] ([[webchat](https://web.libera.chat/#herbstluftwm)])

[![Ohloh Logo](/images/thumb/c/c1/Ohloh-logo.png/30px-Ohloh-logo.png)][Open Hub](https://www.openhub.net/p/herbstluftwm)

[herbstluftwm] is a manual tiling [window manager](https://wiki.gentoo.org/wiki/Window_manager "Window manager") for [X11](https://wiki.gentoo.org/wiki/X11 "X11"). It supports both tiling and floating windows as well as virtual desktops (tags) and immediate reloading of configuration files without the need to restart the window manager. Herbstluftwm also allows the user to split their screen space into multiple monitors, allowing for a setup where one monitor can have multiple virtual desktops visible at a time. Configuration is done exclusively using [herbstclient] which will send commands to a running [herbstluftwm] via Xlib.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
    -   [[1.3] [Additional software]](#Additional_software)
        -   [[1.3.1] [Rofi]](#Rofi)
        -   [[1.3.2] [Polybar]](#Polybar)
-   [[2] [Starting herbstluftwm]](#Starting_herbstluftwm)
-   [[3] [Configuration]](#Configuration)
    -   [[3.1] [Autostart programs]](#Autostart_programs)
-   [[4] [See also]](#See_also)
-   [[5] [External resources]](#External_resources)

## [Installation]

### [USE flags]

### [USE flags for] [x11-wm/herbstluftwm](https://packages.gentoo.org/packages/x11-wm/herbstluftwm) [[]] [A manual tiling window manager for X]

  --------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------
  [`+doc`](https://packages.gentoo.org/useflags/+doc)       Add extra documentation (API, Javadoc, etc). It is recommended to enable per package instead of globally
  [`python`](https://packages.gentoo.org/useflags/python)   Add optional support/bindings for the Python language
  [`test`](https://packages.gentoo.org/useflags/test)       Enable dependencies and/or preparations necessary to run tests (usually controlled by FEATURES=test but can be toggled independently)
  --------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2025-12-15 08:12] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

To install [herbstluftwm] using Portage simply run this command:

`root `[`#`]`emerge --ask x11-wm/herbstluftwm`

### [Additional software]

The default configuration ships with a script ([panel.sh]) which depends on [[[x11-misc/dzen]](https://packages.gentoo.org/packages/x11-misc/dzen)[]].

### [USE flags for] [x11-misc/dzen](https://packages.gentoo.org/packages/x11-misc/dzen) [[]] [General purpose messaging, notification, and menu utility]

  ------------------------------------------------------------- ---------------------------------------------------------------------------------
  [`xinerama`](https://packages.gentoo.org/useflags/xinerama)   Add support for querying multi-monitor screen geometry through the Xinerama API
  [`xpm`](https://packages.gentoo.org/useflags/xpm)             Add support for XPM graphics format
  ------------------------------------------------------------- ---------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2024-03-20 07:01] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

Install dzen if you want to use the default configuration provided by Herbstluftwm:

`root `[`#`]`emerge --ask x11-misc/dzen`

#### [Rofi]

Rofi is a window switcher, application launcher and dmenu replacement.

### [USE flags for] [x11-misc/rofi](https://packages.gentoo.org/packages/x11-misc/rofi) [[]] [A window switcher, run dialog and dmenu replacement]

  ------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------
  [`+drun`](https://packages.gentoo.org/useflags/+drun)               Enable desktop file run dialog
  [`+windowmode`](https://packages.gentoo.org/useflags/+windowmode)   Enable normal window mode
  [`X`](https://packages.gentoo.org/useflags/X)                       Add support for X11
  [`test`](https://packages.gentoo.org/useflags/test)                 Enable dependencies and/or preparations necessary to run tests (usually controlled by FEATURES=test but can be toggled independently)
  [`wayland`](https://packages.gentoo.org/useflags/wayland)           Enable dev-libs/wayland backend
  ------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-01-22 01:17] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

To add a keybind ([Alt]+[d]) for Rofi modify the [autostart] file:

[FILE] **`~/.config/herbstluftwm/autostart`Adding a keybind for Rofi**

    hc keybind $Mod-d spawn rofi -show drun

#### [Polybar]

[Polybar](https://wiki.gentoo.org/wiki/Polybar "Polybar") is a fast, easy-to-use and highly configurable status bar.

### [USE flags for] [x11-misc/polybar](https://packages.gentoo.org/packages/x11-misc/polybar) [[]] [A fast and easy-to-use tool for creating status bars]

  ----------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------
  [`alsa`](https://packages.gentoo.org/useflags/alsa)               Add support for media-libs/alsa-lib (Advanced Linux Sound Architecture)
  [`curl`](https://packages.gentoo.org/useflags/curl)               Add support for client-side URL transfer library
  [`doc`](https://packages.gentoo.org/useflags/doc)                 Add extra documentation (API, Javadoc, etc). It is recommended to enable per package instead of globally
  [`i3wm`](https://packages.gentoo.org/useflags/i3wm)               Add support for i3 window manager
  [`ipc`](https://packages.gentoo.org/useflags/ipc)                 Add support for Inter-Process Messaging
  [`mpd`](https://packages.gentoo.org/useflags/mpd)                 Add support for Music Player Daemon
  [`network`](https://packages.gentoo.org/useflags/network)         Enable network support
  [`pulseaudio`](https://packages.gentoo.org/useflags/pulseaudio)   Add sound server support via media-libs/libpulse (may be PulseAudio or PipeWire)
  ----------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2025-07-04 19:14] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

To automatically launch Polybar from your [autostart] file add a spawn command:

[FILE] **`~/.config/herbstluftwm/autostart`Launching Polybar automatically**

    hc spawn polybar --config=~/.config/polybar/config.ini

## [Starting herbstluftwm]

To start [herbstluftwm], either use a [display manager](https://wiki.gentoo.org/wiki/Display_manager "Display manager") or the command [startx]. To use [startx] with [elogind](https://wiki.gentoo.org/wiki/Elogind "Elogind") support, setup elogind and create the following file:

[FILE] **`~/.xinitrc`**

    exec dbus-launch --exit-with-session herbstlufwm

## [Configuration]

The default configuration file is a good starting point for users who want to write their own configuration. First create the necessary directory for the configuration file:

`user `[`$`]`mkdir -p ~/.config/herbstluftwm`

Now copy the default configuration file from [/etc/xdg/herbstluftwm/autostart] into the directory created above:

`user `[`$`]`cp /etc/xdg/herbstluftwm/autostart ~/.config/herbstluftwm/`

The [\~/.config/herbstluftwm/autostart] file is a regular shell script (similar to [Bspwm](https://wiki.gentoo.org/wiki/Bspwm "Bspwm")) that by default will be executed by Bash. For all list of all commands that [herbstclient] can send see the section \"COMMANDS\" in the [man page](https://herbstluftwm.org/herbstluftwm.html#COMMANDS).

### [Autostart programs]

[FILE] **`~/.config/herbstluftwm/autostart`**

    # Automatically start these programs
    spawn syncthing
    spawn dunst
    spawn feh --bg-scale ~/Pictures/wallpaper.png

Herbstluftwm also provides tab-completion for [herbstclient] commands for both [Bash](https://wiki.gentoo.org/wiki/Bash "Bash") and [Zsh](https://wiki.gentoo.org/wiki/Zsh "Zsh").

Bash users need to source the [/etc/bash_completion.d/herbstclient_completion] file from inside their [\~/.bashrc].

[FILE] **`~/.bashrc`Enabling herbstclient tab-completion for Bash**

    # Add this to the end of your ~/.bashrc
    source /etc/bash_completion.d/herbstclient_completion

For Zsh tab-completion should be enabled by default, if it is not, activate it with [these instructions](https://wiki.gentoo.org/wiki/Zsh#app-shells.2Fzsh-completions "Zsh").

## [See also]

-   [Bspwm](https://wiki.gentoo.org/wiki/Bspwm "Bspwm") - a lightweight, tiling, minimalist window manager
-   [Polybar](https://wiki.gentoo.org/wiki/Polybar "Polybar") - a fast and easy-to-use status bar

## [External resources]

-   [Herbstluftwm documentation](https://herbstluftwm.org)