**Polybar** is a fast and easy-to-use status bar. It allows building customizable status bars for various [desktop environments](https://wiki.gentoo.org/wiki/Desktop_environment "Desktop environment"). Currently, [bspwm](https://wiki.gentoo.org/wiki/Bspwm "Bspwm") and [i3wm](https://wiki.gentoo.org/wiki/I3 "I3") are supported off the shelf.

**Resources**

[[]][Home](https://polybar.github.io/)

[[]][Package information](https://packages.gentoo.org/packages/x11-misc/polybar)

[[]][GitHub](https://github.com/polybar/polybar)

[![Ohloh Logo](/images/thumb/c/c1/Ohloh-logo.png/30px-Ohloh-logo.png)][Open Hub](https://www.openhub.net/p/polybar)

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
-   [[2] [Configuration]](#Configuration)
    -   [[2.1] [Date]](#Date)
    -   [[2.2] [Filesystem]](#Filesystem)
    -   [[2.3] [LAN]](#LAN)
    -   [[2.4] [WLAN]](#WLAN)
    -   [[2.5] [CPU]](#CPU)
-   [[3] [Integration with i3 window manager]](#Integration_with_i3_window_manager)
    -   [[3.1] [Configure Polybar\'s i3 module]](#Configure_Polybar.27s_i3_module)
    -   [[3.2] [Create a Polybar launch script]](#Create_a_Polybar_launch_script)
    -   [[3.3] [Update the i3 configuration to use Polybar]](#Update_the_i3_configuration_to_use_Polybar)
-   [[4] [Removal]](#Removal)
-   [[5] [See also]](#See_also)

## [Installation]

### [USE flags]

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

### [Emerge]

`root `[`#`]`emerge --ask x11-misc/polybar`

## [Configuration]

The Polybar package brings a sample configuration file which is installed at [/usr/share/doc/polybar-\*/config.bz2]. This file demonstrates different configuration options, but is not a out of the box working configuration. Users need to assemble a working configuration themselves.

A working sample would look as follows:

[FILE] **`~/.config/polybar/config`**

    [bar/mybar]
    modules-left = i3
    modules-right = lan wlan filesystem cpu date
    tray-position = right
    font-0 = Noto Sans Mono:style=Regular

    [colors]
    black = #000
    white = #fff
    grey = #aaa
    darkgrey = #555
    red = #f00
    green = #0f0

This declares a new bar called `"mybar"`, and identifies which modules are being used and instructs Polybar to create a systray for hosting applets. The different modules (i3, lan, wlan, filesystem, cpu, and date), need to be defined further on in the configuration file, see below.

The optional section `[colors]` makes it easier to use colors in the different modules.

### [Date]

The following section adds date and time to the bar.

[FILE] **`~/.config/polybar/config`**

    [module/date]
    type = internal/date
    ;interval = 1
    date = " | %d-%h-%y %H:%M:%

Increase the interval to reduce power consumption.

### [Filesystem]

For monitoring the disk space utilization of various mount points:

[FILE] **`~/.config/polybar/config`**

    [module/filesystem]
    type = internal/fs
    interval = 60
    mount-0 = /
    mount-1 = /tmp
    mount-2 = /data
    label-mounted = %%mountpoint%%: %percentage_used%%

### [LAN]

The following section shows the network status for a wired LAN:

[FILE] **`~/.config/polybar/config`**

    [module/lan]
    type = internal/network
    interface = eth0
    label-connected = "%ifname%: %local_ip% %local_ip6% | "
    ;label-disconnected = "%ifname%: not connected | "

Update the interface line as required.

### [WLAN]

The [Wifi](https://wiki.gentoo.org/wiki/Wifi "Wifi") wireless LAN section is almost identical as the wired LAN section, but has a few more things to show.

[FILE] **`~/.config/polybar/config`**

    [module/wlan]
    type = internal/network
    interface = wlan0
    label-connected = "%ifname%: %essid% %signal%%  %%local_ip% %%local_ip6% % | "
    ;label-disconnected = "%ifname%: not connected | "

### [CPU]

To show processor utilization the following section can be used:

[FILE] **`~/.config/polybar/config`**

    [module/cpu]
    type = internal/cpu
    format = <label> <ramp-coreload>
    label = " | CPU %percentage%%"
    ramp-coreload-spacing = 1
    ramp-coreload-0 = %▁%
    ramp-coreload-1 = %▂%
    ramp-coreload-2 = %▃%
    ramp-coreload-3 = %▄%
    ramp-coreload-4 = %▅%
    ramp-coreload-5 = %▆%
    ramp-coreload-6 = %▇%
    ramp-coreload-7 = %█%

This section uses the ramp option to graphically show the utilization per core, showing low utilization as green, mid utilization as orange and high utilization as red. Note that the colors section cannot be reused here.

## [Integration with i3 window manager]

Polybar can replace [i3bar]. This requires configuring Polybar for use with i3, creating a Polybar launch script, and updating the i3 configuration to use Polybar.

### [][Configure Polybar\'s i3 module]

In case Polybar is used with the [i3 window manager](https://wiki.gentoo.org/wiki/I3 "I3") the following can be used to configure the Polybar\'s i3 module:

[FILE] **`~/.config/polybar/config`**

    [module/i3]
    type = internal/i3

    label-focused = %index%
    label-focused-background = $
    label-focused-foreground = $
    label-focused-underline= $
    label-focused-padding = 1

    label-unfocused = %index%
    label-unfocused-foreground = $
    label-unfocused-padding = 1

    label-urgent = %index%
    label-urgent-foreground = $
    label-urgent-background = $
    label-urgent-padding = 1

### [Create a Polybar launch script]

[FILE] **`~/.config/polybar/launch`**

    #!/bin/bash

    # Terminate already running bar instances
    killall -q polybar
    # If all your bars have ipc enabled, you can also use
    # polybar-msg cmd quit

    # Launch Polybar, using default config location ~/.config/polybar/config
    polybar mybar 2>&1 | tee -a /tmp/polybar.log & disown

    echo "Polybar launched..."

### [Update the i3 configuration to use Polybar]

Comment out the following section that starts [i3bar], and add a statement to launch Polybar:

[FILE] **`~/.config/i3/config`**

    # Start i3bar to display a workspace bar (plus the system information i3status
    # finds out, if available)
    #bar
    # use Polybar instead of i3bar
    exec_always --no-startup-id ~/.config/polybar/launch

## [Removal]

To remove Polybar issue the following:

`root `[`#`]`emerge --ask --depclean --verbose x11-misc/polybar`

Do not forget to remove the added files under [\~/.config/polybar/] and to restore the i3bar section in [\~/.config/i3/config].

## [See also]

-   [bspwm](https://wiki.gentoo.org/wiki/Bspwm "Bspwm") --- a lightweight, tiling, minimalist [window manager](https://wiki.gentoo.org/wiki/Window_manager "Window manager") written in C, which organizes its windows as nodes of a binary tree.
-   [i3](https://wiki.gentoo.org/wiki/I3 "I3") --- a minimalist [tiling](https://en.wikipedia.org/wiki/Tiling_window_manager "wikipedia:Tiling window manager") [window manager](https://wiki.gentoo.org/wiki/Window_manager "Window manager"), completely written from scratch.