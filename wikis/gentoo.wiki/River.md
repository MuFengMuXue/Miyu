This page contains [[changes](https://wiki.gentoo.org/index.php?title=River&diff=1437464)] which are not marked for translation.

[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=River&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

**Resources**

[[]][Home](https://isaacfreund.com/software/river/)

[![Codeberg Logo](/images/thumb/c/cc/Codeberg-logo.png/30px-Codeberg-logo.png)][Codeberg](https://codeberg.org/river/river)

[[]][Official documentation](https://codeberg.org/river/wiki)

[[]][[#river](ircs://irc.libera.chat/#river)] ([[webchat](https://web.libera.chat/#river)])

**River** is a non-monolithic [wlroots](https://wiki.gentoo.org/wiki/Wlroots "Wlroots")-based [Wayland compositor](https://wiki.gentoo.org/wiki/Wayland_compositor "Wayland compositor") written in [Zig](https://wiki.gentoo.org/wiki/Zig "Zig"). River allows for the use of a seperate compatible window manager to define window arrangement, window decorations, keybindings and other behavior.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
-   [[2] [Configuration]](#Configuration)
    -   [[2.1] [Files]](#Files)
    -   [[2.2] [Terminal emulator]](#Terminal_emulator)
    -   [[2.3] [Status bar]](#Status_bar)
    -   [[2.4] [Brightness]](#Brightness)
    -   [[2.5] [Sound volume]](#Sound_volume)
    -   [[2.6] [Taking screenshots]](#Taking_screenshots)
    -   [[2.7] [Setting a wallpaper]](#Setting_a_wallpaper)
-   [[3] [Executing river]](#Executing_river)
-   [[4] [Usage]](#Usage)
    -   [[4.1] [Configurations and key bindings]](#Configurations_and_key_bindings)
    -   [[4.2] [Tags]](#Tags)
    -   [[4.3] [Recommended software]](#Recommended_software)
-   [[5] [Troubleshooting]](#Troubleshooting)
    -   [[5.1] [Additional comments from editor(s)]](#Additional_comments_from_editor.28s.29)
-   [[6] [See also]](#See_also)
-   [[7] [External resources]](#External_resources)

## [Installation]

River is currently not provided by the main Gentoo repository, but it is available from the [GURU](https://wiki.gentoo.org/wiki/Project:GURU "Project:GURU") repository.

### [USE flags]

The available USE flags may be retrieved with the **equery** utility from [[[app-portage/gentoolkit]](https://packages.gentoo.org/packages/app-portage/gentoolkit)[]] with the following command:

`user `[`$`]`equery uses gui-wm/river`

### [Emerge]

First, the GURU repository must be enabled, which can be done with [[[app-eselect/eselect-repository]](https://packages.gentoo.org/packages/app-eselect/eselect-repository)[]]:

`root `[`#`]`eselect repository enable guru`

Once enabled, sync it using **emaint** with the `--repo` option:

`root `[`#`]`emaint sync --repo guru`

After the repository has been synced, [[[gui-wm/river]](https://packages.gentoo.org/packages/gui-wm/river)[]] can finally be installed:

`root `[`#`]`emerge --ask gui-wm/river`

## [Configuration]

** Important**\
The following man pages will only be accessible if the `+man` *USE* flag is set for river.

River is mainly configured through the [riverctl] function. To see documentation for river and configuration options:

`user `[`$`]`man river`

`user `[`$`]`man riverctl`

Layouts are managed by an external program. The simple [rivertile] is installed along with river. To see configuration options:

`user `[`$`]`man rivertile`

A list of alternative layout managers, implementing interesting other layouts, is available at [\[1\]](https://codeberg.org/river/wiki/src/branch/master/pages/Community-Layouts.md).

### [Files]

River starts by executing the **init** file. By default, river will look for the init file at [\$XDG_CONFIG_HOME/river/init]. If `$XDG_CONFIG_HOME` is not set, river will search for the init file at [\~/.config/river/init]. **Make sure to create an init file before running river.** A default is provided by the authors at [\[2\]](https://codeberg.org/river/river/src/branch/master/example/init).

Per the authors, the init file can be any executable script, not just shell scripts. See an example written in lua5.4 [\[3\]](https://gist.github.com/FollieHiyuki/f598db7c548f3397e2a68e4340ac9fdc).

### [Terminal emulator]

River does not have a recommended [terminal emulator](https://wiki.gentoo.org/wiki/Terminal_emulator "Terminal emulator"). The default configuration uses [foot](https://wiki.gentoo.org/wiki/Foot "Foot"):

[[[gui-apps/foot]](https://packages.gentoo.org/packages/gui-apps/foot)[]]

Other Wayland-native terminal emulators include [Alacritty](https://wiki.gentoo.org/wiki/Alacritty "Alacritty") [[[x11-terms/alacritty]](https://packages.gentoo.org/packages/x11-terms/alacritty)[]], and [Kitty](https://wiki.gentoo.org/wiki/Kitty "Kitty") [[[x11-terms/kitty]](https://packages.gentoo.org/packages/x11-terms/kitty)[]] which work natively with Wayland if the `KITTY_ENABLE_WAYLAND` environment variable is set to 1.

### [Status bar]

River does not have a built-in status bar. [Waybar](https://wiki.gentoo.org/wiki/Waybar "Waybar") has modules for showing river mode, tags, windows, and layout [\[4\]](https://github.com/Alexays/Waybar/wiki/Module:-River):

`root `[`#`]`emerge --ask gui-apps/waybar`

The authors also recommended the following status bars:

-   yambar: [\[5\]](https://github.com/neonkore/yambar)

<!-- -->

-   levee: [\[6\]](https://sr.ht/~andreafeletto/levee)

<!-- -->

-   i3bar-river: [\[7\]](https://github.com/MaxVerevkin/i3bar-river)

### [Brightness]

[[[dev-libs/light]](https://packages.gentoo.org/packages/dev-libs/light)[]] can be used to adjust backlight and brightness. Here is an example config:

[FILE] **`~/.config/river/init`Set the keyboard shortcuts for screen brightness support**

    riverctl map $mode None XF86MonBrightnessUp   spawn 'light -A 5'
    riverctl map $mode None XF86MonBrightnessDown spawn 'light -U 5'

** Warning**\
The light project was orphaned as of March 8th 2023 [\[8\]](https://web.archive.org/web/20231031165455/https://github.com/haikarainen/light) and the repository no longer exists. As an alternative, [[[app-misc/brightnessctl::guru]](https://github.com/gentoo-mirror/guru/tree/master/app-misc/brightnessctl)[]] could be used to adjust the brightness.

### [Sound volume]

The following configuration can be used for changing sound volume with [amixer](https://wiki.gentoo.org/index.php?title=Amixer&action=edit&redlink=1 "Amixer (page does not exist)"):

[FILE] **`~/.config/river/init`Set the keyboard shortcuts to change sound volume**

    riverctl map $mode None XF86AudioRaiseVolume  spawn 'amixer set "Master" 10%+'
    riverctl map $mode None XF86AudioLowerVolume  spawn 'amixer set "Master" 10%-'
    riverctl map $mode None XF86AudioMute         spawn 'amixer set "Master" toggle'

Alternatively, if [pulseaudio](https://wiki.gentoo.org/wiki/Pulseaudio "Pulseaudio") is being used, the following configuration should also work:

[FILE] **`~/.config/river/init`Set the keyboard shortcuts to change sound volume**

    riverctl map $mode None XF86AudioRaiseVolume  spawn 'pactl set-sink-volume @DEFAULT_SINK@ +5%'
    riverctl map $mode None XF86AudioLowerVolume  spawn 'pactl set-sink-volume @DEFAULT_SINK@ -5%'

### [Taking screenshots]

To add simple screenshot support you can use the [[[gui-apps/grim]](https://packages.gentoo.org/packages/gui-apps/grim)[]] package.

`root `[`#`]`emerge --ask gui-apps/grim`

Area selection support is added with [[[gui-apps/slurp]](https://packages.gentoo.org/packages/gui-apps/slurp)[]].

`root `[`#`]`emerge --ask gui-apps/slurp`

For clipboard support a handler like [[[gui-apps/wl-clipboard]](https://packages.gentoo.org/packages/gui-apps/wl-clipboard)[]] is necessary.

`root `[`#`]`emerge --ask gui-apps/wl-clipboard`

Next, add the keyboard shortcuts to your config file at [\~/.config/river/init].

[FILE] **`~/.config/river/init`Set the keyboard shortcuts to take screenshots**

    # Screenshot display to clipboard
    riverctl map normal None Print spawn "grim - | wl-copy"

    # Screenshot area to clipboard
    riverctl map normal Control Print spawn 'grim -g "$(slurp)" - | wl-copy'

    # Screenshot display and save to $HOME/Pictures
    riverctl map normal Alt Print spawn "grim $HOME/Pictures/$(date +'%s.png')"

    # Screenshot area and save to $HOME/Pictures
    riverctl map normal Alt+Control Print spawn 'grim -g "$(slurp)" $HOME/Pictures/$(date +'%s.png')'

### [Setting a wallpaper]

The wallpaper can be set with [[[gui-apps/swaybg]](https://packages.gentoo.org/packages/gui-apps/swaybg)[]] with a command like this:

[FILE] **`~/.config/river/init`Setting the wallpaper**

    swaybg -m fill -i /home/larry/wallpapers/Awesome_Gentoo_Wallpaper.png &

## [Executing river]

River can be started from a tty or a terminal with:

`user `[`$`]`dbus-run-session river`

## [Usage]

### [Configurations and key bindings]

All key combinations will be defined in the [\~/.config/river/init] configuration file.

Note that river does not currently support reloading the configuration. Instead, configurations can be changed on-the-fly by typing the corresponding [riverctl] command in a terminal, while permanent configurations can be changed via the init file.

### [Tags]

River uses a dwm-inspired tags system for ordering and grouping windows to outputs. This system is superficially similar to the workspace system in most other WMs/Wayland compositors but are quite different.

Rather than assigning each window to a workspace, each window is assigned one or more tags as one of its properties. Every window and every output has 32 tags, which can either be **on** or **off**.

The following is heavily copy-pasted from [\[9\]](https://codeberg.org/river/wiki/src/branch/master/pages/How-tags-work.md):

To determine which windows should be currently displayed on an output, river loops through all windows and checks if any of its active tags match an active tag of the output. If there is a match, the window will be displayed. This system allows both windows and outputs to have **multiple active tags simultaneously**, which is what makes tags vastly more powerful than the workspaces of other compositors.

River allows both setting and toggling the tags of windows and outputs. Setting tags provides \"on or off\" information for each tag as a 32-bit unsigned integer to overwrite the previous value; toggling also provides river with the same 32-big unsigned integer, but instead of overwriting, river will toggle the matching tag of the window or output.

*For example:* Imagine you have a text editor on **tag 1**, a terminal where you are compiling the code on **tag 2** and documentation on **tag 3**. While you are writing the codebase, you are on **tag 1**. If you want to reference the documentation, you can **toggle tag 3** to have both the editor and the docs side-by-side. Now you want to compile, so you **switch to tag 2**; now only the terminal is on your screen. You compile but notice you have an error. You **toggle tag 1** and now have your editor and your terminal with your compiler error side-by-side, allowing you to quickly find the bug. Compiling succeeds, so you **toggle tag 2** and only your editor remains on the screen.

### [Recommended software]

Besides the recommended terminal emulators and status bars as mentioned above, the authors also summarized various other useful softwares here [\[10\]](https://codeberg.org/river/wiki/src/branch/main/pages/useful-software.md).

## [Troubleshooting]

Please review the river wiki for FAQs and other issues [\[11\]](https://codeberg.org/river/wiki).

### [][Additional comments from editor(s)]

-   Make sure any autostart programs/scripts are defined at the beginning of the init file. Commands defined at the very end of the init file may not be run upon startup.

## [See also]

-   [bspwm](https://wiki.gentoo.org/wiki/Bspwm "Bspwm") --- a lightweight, tiling, minimalist [window manager](https://wiki.gentoo.org/wiki/Window_manager "Window manager") written in C, which organizes its windows as nodes of a binary tree.
-   [dwm](https://wiki.gentoo.org/wiki/Dwm "Dwm") --- a dynamic [window manager](https://wiki.gentoo.org/wiki/Window_manager "Window manager") for [X11](https://wiki.gentoo.org/wiki/X11 "X11") from [suckless.org](https://suckless.org/).
-   [Sway](https://wiki.gentoo.org/wiki/Sway "Sway") --- an open-source [wlroots](https://wiki.gentoo.org/wiki/Wlroots "Wlroots")-based [Wayland compositor](https://wiki.gentoo.org/wiki/Wayland_compositor "Wayland compositor") that is designed to be compatible with the [i3](https://wiki.gentoo.org/wiki/I3 "I3") window manager.
-   [Wayland](https://wiki.gentoo.org/wiki/Wayland "Wayland") --- a [communication protocol](https://en.wikipedia.org/wiki/communication_protocol "wikipedia:communication protocol") between a [display server](https://en.wikipedia.org/wiki/display_server "wikipedia:display server") and its clients

## [External resources]

-   [Separating the Wayland Compositor and Window Manager](https://isaacfreund.com/blog/river-window-management/) - \"The new 0.4.0 release of river \... splits the window manager into a separate program. There are already many window managers compatible with river.\"