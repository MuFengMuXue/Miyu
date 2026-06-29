[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=Waybar&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

**Resources**

[[]][Home](https://github.com/Alexays/Waybar)

[[]][Package information](https://packages.gentoo.org/packages/gui-apps/waybar)

[[]][GitHub](https://github.com/Alexays/Waybar)

[[]][Official documentation](https://github.com/Alexays/Waybar/wiki/)

**Waybar** is a status bar for [Wayland compositors](https://wiki.gentoo.org/wiki/Wayland_compositor "Wayland compositor").

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
-   [[2] [Configuration]](#Configuration)
    -   [[2.1] [Files]](#Files)
    -   [[2.2] [Colors]](#Colors)
    -   [[2.3] [Styling]](#Styling)
    -   [[2.4] [Icons]](#Icons)
    -   [[2.5] [Applying configuration changes]](#Applying_configuration_changes)
-   [[3] [See also]](#See_also)

## [Installation]

### [USE flags]

### [USE flags for] [gui-apps/waybar](https://packages.gentoo.org/packages/gui-apps/waybar) [[]] [Highly customizable Wayland bar for Sway and Wlroots based compositors]

  --------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------
  [`+libinput`](https://packages.gentoo.org/useflags/+libinput)         Enable libinput support for libinput related features
  [`+logind`](https://packages.gentoo.org/useflags/+logind)             Enable support for logind (bluetooth and idle inhibit)
  [`+udev`](https://packages.gentoo.org/useflags/+udev)                 Enable virtual/udev integration (device discovery, power and storage device support, etc)
  [`backlight`](https://packages.gentoo.org/useflags/backlight)         Enable module that controls the current backlight level
  [`evdev`](https://packages.gentoo.org/useflags/evdev)                 Enable libevdev support for evdev related features
  [`experimental`](https://packages.gentoo.org/useflags/experimental)   Enable experimental features, such as Bluetooth battery reporting
  [`gps`](https://packages.gentoo.org/useflags/gps)                     Add support for Global Positioning System
  [`jack`](https://packages.gentoo.org/useflags/jack)                   Add support for the JACK Audio Connection Kit
  [`mpd`](https://packages.gentoo.org/useflags/mpd)                     Enable support for the Music Player Daemon
  [`mpris`](https://packages.gentoo.org/useflags/mpris)                 Enable support for mpris
  [`network`](https://packages.gentoo.org/useflags/network)             Enable libnl support for network related features
  [`niri`](https://packages.gentoo.org/useflags/niri)                   Enable support for Niri Wayland compositor
  [`pipewire`](https://packages.gentoo.org/useflags/pipewire)           Enable support for pipewire
  [`pulseaudio`](https://packages.gentoo.org/useflags/pulseaudio)       Enable support for volume control via PulseAudio
  [`sndio`](https://packages.gentoo.org/useflags/sndio)                 Enable support for volume control via sndio
  [`systemd`](https://packages.gentoo.org/useflags/systemd)             Enable use of systemd-specific libraries and features like socket activation or session tracking
  [`test`](https://packages.gentoo.org/useflags/test)                   Enable dependencies and/or preparations necessary to run tests (usually controlled by FEATURES=test but can be toggled independently)
  [`tray`](https://packages.gentoo.org/useflags/tray)                   Enable support for tray
  [`upower`](https://packages.gentoo.org/useflags/upower)               Enable power management support
  [`wifi`](https://packages.gentoo.org/useflags/wifi)                   Enable support for wifi/rfkill
  --------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-02-26 01:21] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

`root `[`#`]`emerge --ask gui-apps/waybar`

## [Configuration]

To view all available configuration options:

`user `[`$`]`man 5 waybar`

### [Files]

Example [config] and [style.css] files are provided in the [/etc/xdg/waybar/] directory:

`user `[`$`]`mkdir -p ~/.config/waybar/ `

`user `[`$`]`cp /etc/xdg/waybar/config.jsonc ~/.config/waybar/ `

`user `[`$`]`cp /etc/xdg/waybar/style.css ~/.config/waybar/ `

### [Colors]

Waybar supports three main ways to set color for particular element: rgb e.g: `rgb(100, 114, 125)`, rgba e.g: `rgba(100, 114, 125, 0.5)` and css styled colors e.g: `#red` or `#cec2eb`.

### [Styling]

The main waybar window can be styled with the following:

       window#waybar
       window#waybar.hidden
       window#waybar.<name>
           <name> is set to the value of the optional name configuration property. If not set, this class is not available.
       window#waybar.
            is set to the value of the position configuration property.

A style with the .module selector would affect all the modules. In practice, you may prefer to use more specific label.module and box.module selectors.

[FILE] **`~/.config/waybar/style.css`Example on styling**

    label.module
    box.module button:hover

### [Icons]

To utilise icons used in the default config, install the [[[media-fonts/fontawesome]](https://packages.gentoo.org/packages/media-fonts/fontawesome)[]] and [[[media-fonts/meslo-nerd::supertux88]](https://gpo.zugaina.org/Overlays/supertux88/media-fonts/meslo-nerd)[]] packages.

The simplest way to use the icons is to set the `font-family` property in [style.css], specifying \"Font Awesome 6 Free\" after the preferred font for text, e.g.:

[FILE] **`~/.config/waybar/style.css`Add support for Font Awesome icons**

    *

However, this will not always result in the desired behaviour for all Waybar modules. In particular, it will result in icons not displaying properly in some modules: the icons can be made to display by reversing the order of values of the `font-family` property for a module, but that will result in Font Awesome being used for non-icon text as well.

An approach to address these issues via [fontconfig](https://wiki.gentoo.org/wiki/Fontconfig "Fontconfig") was described in [this comment on the relevant Waybar issue](https://github.com/Alexays/Waybar/issues/215#issuecomment-1114280705). Firstly, if [\~/.config/fontconfig/fonts.conf] does not already exist, create it with the following contents:

[FILE] **`~/.config/fontconfig/fonts.conf`Add support for Font Awesome icons**

    <?xml version="1.0"?>
    <!DOCTYPE fontconfig SYSTEM "fonts.dtd">
    <fontconfig>
      <alias>
        <family>icon</family>

          <family>Font Awesome 6 Free</family>
        </prefer>
      </alias>
    </fontconfig>

Otherwise, add the above `alias` element subtree within the `fontconfig` element in the existing file.

Then, each icon in the [config] file should be wrapped in `span font='icon'` tags, e.g.:

    "format": " %"

or

    "format": " %"

Finally, the `font-family` property in [style.css] should be set to only the font(s) for non-icon text, e.g.:

    *

After restarting Waybar, both icons and non-icon text should now be displayed appropriately.

### [Applying configuration changes]

Modifications to the [style.css] file, once saved, can be applied by sending the Waybar process a `SIGUSR2` signal, e.g. [pkill -SIGUSR2 waybar]. However, modifications to the [config] file can only be applied by restarting the Waybar process. A script like below could be used to restart Waybar:

[FILE] **`launch-waybar.sh`Restart waybar when config changed.**

    #!/bin/bash
    CONFIG_FILES="$HOME/.config/waybar/config $HOME/.config/waybar/style.css"
    trap "killall waybar" EXIT
    while true; do
        waybar &
        inotifywait -e create,modify $CONFIG_FILES
        killall waybar
    done

## [See also]

-   [Hyprland](https://wiki.gentoo.org/wiki/Hyprland "Hyprland") --- an open-source [Wayland compositor](https://wiki.gentoo.org/wiki/Wayland_compositor "Wayland compositor") written in C++.
-   [Sway](https://wiki.gentoo.org/wiki/Sway "Sway") --- an open-source [wlroots](https://wiki.gentoo.org/wiki/Wlroots "Wlroots")-based [Wayland compositor](https://wiki.gentoo.org/wiki/Wayland_compositor "Wayland compositor") that is designed to be compatible with the [i3](https://wiki.gentoo.org/wiki/I3 "I3") window manager.
-   [Wayland](https://wiki.gentoo.org/wiki/Wayland "Wayland") --- a [communication protocol](https://en.wikipedia.org/wiki/communication_protocol "wikipedia:communication protocol") between a [display server](https://en.wikipedia.org/wiki/display_server "wikipedia:display server") and its clients
-   [Weston](https://wiki.gentoo.org/wiki/Weston "Weston") --- a reference implementation of a [Wayland compositor](https://wiki.gentoo.org/wiki/Wayland_compositor "Wayland compositor").