This page contains [[changes](https://wiki.gentoo.org/index.php?title=Sway&oldid=1428414&diff=1437419)] which are not marked for translation.

Other languages:

-   [Deutsch](https://wiki.gentoo.org/wiki/Sway/de "Sway/de (43% translated)")
-   [English]
-   [español](https://wiki.gentoo.org/wiki/Sway/es "Sway (15% translated)")
-   [français](https://wiki.gentoo.org/wiki/Sway/fr "Sway (7% translated)")
-   [italiano](https://wiki.gentoo.org/wiki/Sway/it "Sway (24% translated)")
-   [magyar](https://wiki.gentoo.org/wiki/Sway/hu "Sway (88% translated)")
-   [中文（中国大陆）‎](https://wiki.gentoo.org/wiki/Sway/zh-cn "Sway (79% translated)")
-   [日本語](https://wiki.gentoo.org/wiki/Sway/ja "Sway (91% translated)")

**Resources**

[[]][Home](https://swaywm.org/)

[[]][Package information](https://packages.gentoo.org/packages/gui-wm/sway)

[[]][GitHub](https://github.com/swaywm/sway)

[[]][Official documentation](https://github.com/swaywm/sway/wiki)

[[]][[#sway](ircs://irc.libera.chat/#sway)] ([[webchat](https://web.libera.chat/#sway)])

[[]][Wikipedia](https://en.wikipedia.org/wiki/Sway_(window_manager) "wikipedia:Sway (window manager)")

**Sway** (contracted from **S**irCmpwn\'s **Way**land compositor) is an open-source [wlroots](https://wiki.gentoo.org/wiki/Wlroots "Wlroots")-based [Wayland compositor](https://wiki.gentoo.org/wiki/Wayland_compositor "Wayland compositor") that is designed to be compatible with the [i3](https://wiki.gentoo.org/wiki/I3 "I3") window manager.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
-   [[2] [Configuration]](#Configuration)
    -   [[2.1] [Files]](#Files)
    -   [[2.2] [Terminal emulator]](#Terminal_emulator)
    -   [[2.3] [Display configuration]](#Display_configuration)
    -   [[2.4] [Input Devices]](#Input_Devices)
    -   [[2.5] [Application launcher]](#Application_launcher)
        -   [[2.5.1] [bemenu]](#bemenu)
        -   [[2.5.2] [wmenu]](#wmenu)
    -   [[2.6] [Status bar]](#Status_bar)
    -   [[2.7] [Brightness]](#Brightness)
        -   [[2.7.1] [acpilight]](#acpilight)
        -   [[2.7.2] [brightnessctl]](#brightnessctl)
        -   [[2.7.3] [light]](#light)
        -   [[2.7.4] [ddcutil]](#ddcutil)
    -   [[2.8] [Notification]](#Notification)
    -   [[2.9] [Sound volume]](#Sound_volume)
        -   [[2.9.1] [Pipewire]](#Pipewire)
        -   [[2.9.2] [Pulseaudio]](#Pulseaudio)
        -   [[2.9.3] [ALSA]](#ALSA)
        -   [[2.9.4] [sndio]](#sndio)
    -   [[2.10] [Taking screenshots]](#Taking_screenshots)
        -   [[2.10.1] [Simple approach: use slurpshot]](#Simple_approach:_use_slurpshot)
        -   [[2.10.2] [Manual approach]](#Manual_approach)
        -   [[2.10.3] [Snipping tool like behavior]](#Snipping_tool_like_behavior)
    -   [[2.11] [Set a random wallpaper]](#Set_a_random_wallpaper)
    -   [[2.12] [Swaylock]](#Swaylock)
    -   [[2.13] [Swayidle]](#Swayidle)
    -   [[2.14] [HiDPI]](#HiDPI)
    -   [[2.15] [Xresources]](#Xresources)
    -   [[2.16] [GTK configuration]](#GTK_configuration)
        -   [[2.16.1] [Dark Mode]](#Dark_Mode)
            -   [[2.16.1.1] [GTK4]](#GTK4)
            -   [[2.16.1.2] [GTK3]](#GTK3)
            -   [[2.16.1.3] [GTK2]](#GTK2)
        -   [[2.16.2] [GTK3 Themes and Fonts]](#GTK3_Themes_and_Fonts)
    -   [[2.17] [Automatic floating windows]](#Automatic_floating_windows)
        -   [[2.17.1] [Firefox Tweaks]](#Firefox_Tweaks)
        -   [[2.17.2] [Steam Tweaks]](#Steam_Tweaks)
    -   [[2.18] [Service]](#Service)
        -   [[2.18.1] [OpenRC]](#OpenRC)
    -   [[2.19] [Switching Keyboard Layouts]](#Switching_Keyboard_Layouts)
        -   [[2.19.1] [Temporarily change keyboard layout]](#Temporarily_change_keyboard_layout)
        -   [[2.19.2] [Switching between layouts with a keybinding]](#Switching_between_layouts_with_a_keybinding)
-   [[3] [Usage]](#Usage)
    -   [[3.1] [Starting Sway]](#Starting_Sway)
        -   [[3.1.1] [Launching Sway automatically with TTY login]](#Launching_Sway_automatically_with_TTY_login)
            -   [[3.1.1.1] [Automatic login on tty1]](#Automatic_login_on_tty1)
        -   [[3.1.2] [Starting Sway manually]](#Starting_Sway_manually)
        -   [[3.1.3] [Launching Sway from a script]](#Launching_Sway_from_a_script)
        -   [[3.1.4] [Starting Sway without elogind or systemd]](#Starting_Sway_without_elogind_or_systemd)
    -   [[3.2] [Movement]](#Movement)
        -   [[3.2.1] [Useful binds]](#Useful_binds)
    -   [[3.3] [Layouts]](#Layouts)
    -   [[3.4] [Terminal]](#Terminal)
        -   [[3.4.1] [Foot Server]](#Foot_Server)
    -   [[3.5] [Adding features]](#Adding_features)
        -   [[3.5.1] [Moving left and right with non-existing workspaces]](#Moving_left_and_right_with_non-existing_workspaces)
    -   [[3.6] [Font size adjustment]](#Font_size_adjustment)
-   [[4] [Troubleshooting]](#Troubleshooting)
    -   [[4.1] [Screen sharing does not work]](#Screen_sharing_does_not_work)
    -   [[4.2] [Failed to connect to user bus]](#Failed_to_connect_to_user_bus)
    -   [[4.3] [Warning: no icon themes loaded]](#Warning:_no_icon_themes_loaded)
    -   [[4.4] [No backend was able to open a seat]](#No_backend_was_able_to_open_a_seat)
    -   [[4.5] [Applications forget logins]](#Applications_forget_logins)
-   [[5] [See also]](#See_also)
-   [[6] [References]](#References)

## [Installation]

### [USE flags]

### [USE flags for] [gui-wm/sway](https://packages.gentoo.org/packages/gui-wm/sway) [[]] [i3-compatible Wayland window manager]

  ----------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------
  [`+filecaps`](https://packages.gentoo.org/useflags/+filecaps)     Use Linux file capabilities to control privilege rather than set\*id (this is orthogonal to USE=caps which uses capabilities at runtime e.g. libcap)
  [`+man`](https://packages.gentoo.org/useflags/+man)               Build and install man pages
  [`+swaybar`](https://packages.gentoo.org/useflags/+swaybar)       Install \'swaybar\': sway\'s status bar component
  [`+swaynag`](https://packages.gentoo.org/useflags/+swaynag)       Install \'swaynag\': shows a message with buttons
  [`X`](https://packages.gentoo.org/useflags/X)                     Enable support for X11 applications (XWayland)
  [`tray`](https://packages.gentoo.org/useflags/tray)               Enable support for StatusNotifierItem tray specification
  [`verify-sig`](https://packages.gentoo.org/useflags/verify-sig)   Verify upstream signatures on distfiles
  [`wallpapers`](https://packages.gentoo.org/useflags/wallpapers)   Install sway\'s default wallpaper image
  ----------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-04-13 11:26] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

`root `[`#`]`emerge --ask gui-wm/sway`

## [Configuration]

To view all available configuration options:

`user `[`$`]`man 5 sway`

### [Files]

Each user running sway can edit the default configuration file in order to run a customized sway session. Gentoo stores this file at its default [/etc/sway/config] location:

`user `[`$`]`mkdir -p ~/.config/sway/ `

`user `[`$`]`cp /etc/sway/config ~/.config/sway/ `

### [Terminal emulator]

By default the Sway configuration file uses the [foot](https://wiki.gentoo.org/wiki/Foot "Foot") [terminal emulator](https://wiki.gentoo.org/wiki/Terminal_emulator "Terminal emulator") (found in the [[[gui-apps/foot]](https://packages.gentoo.org/packages/gui-apps/foot)[]] package). It is a good idea to emerge this terminal emulator so that a terminal will be available once Sway is running:

`root `[`#`]`emerge --ask gui-apps/foot`

Other popular choices include [[[x11-terms/alacritty]](https://packages.gentoo.org/packages/x11-terms/alacritty)[]] or [[[x11-terms/kitty]](https://packages.gentoo.org/packages/x11-terms/kitty)[]], which works natively with Wayland if the `KITTY_ENABLE_WAYLAND` environment variable is set to `1`.

Another very lightweight alternative is [st](https://wiki.gentoo.org/wiki/St "St"), but it isn\'t Wayland native.

### [Display configuration]

Display options can be queried with:

`user `[`$`]`swaymsg -t get_outputs`

    Output DP-1 'HP Inc. HP X34 6CM2261GK2' (focused)
      Current mode: 3440x1440 @ 165.000 Hz
      Position: 0,0
      Scale factor: 1.000000
      Scale filter: nearest
      Subpixel hinting: unknown
      Transform: normal
      Workspace: 1
      Max render time: off
      Adaptive sync: disabled
      Available modes:
        3440x1440 @ 165.000 Hz

    ...

    Output DP-2 'LG Electronics LG HDR QHD 110NTTQ0U193'
      Current mode: 2560x1440 @ 59.951 Hz
      Position: 3440,0
      Scale factor: 1.000000
      Scale filter: nearest
      Subpixel hinting: unknown
      Transform: normal
      Workspace: 2
      Max render time: off
      Adaptive sync: disabled
      Available modes:
        2560x1440 @ 59.951 Hz
        2560x1440 @ 74.971 Hz

    ...

    Output DP-3 'Ancor Communications Inc VE247 E3LMQS103610'
      Current mode: 1920x1080 @ 60.000 Hz
      Position: 6000,0
      Scale factor: 1.000000
      Scale filter: nearest
      Subpixel hinting: unknown
      Transform: normal
      Workspace: 3
      Max render time: off
      Adaptive sync: disabled
      Available modes:
        1920x1080 @ 60.000 Hz

The results have been shortened to only contain the desired resolution. The default positions are not configured properly, and can be adjusted by modifying [\~/.config/sway/config]. Once the file is saved, the configuration can be reloaded with [\$mod]+[Shift]+[C]

[FILE] **`~/.config/sway/config`Configure the left display which is physically slightly larger than the primary display**

    output DP-1 resolution 3440x1440@165hz pos 2560 350

[FILE] **`~/.config/sway/config`Configure primary display which is centered**

    output DP-2 resolution 2560x1440@74.971hz pos 0 250

[FILE] **`~/.config/sway/config`Configure alternate display which is vertical**

    output DP-3 resolution 1920x1080@60hz pos 6000 0 transform 270

### [Input Devices]

Input devices can be queried with:

`user `[`$`]`swaymsg -t get_inputs`

    Input device: Logitech G502 HERO Gaming Mouse Keyboard
      Type: Mouse
      Identifier: 1133:49291:Logitech_G502_HERO_Gaming_Mouse_Keyboard
      Product ID: 49291
      Vendor ID: 1133
      Libinput Send Events: enabled

    Input device: Logitech G502 HERO Gaming Mouse Keyboard
      Type: Keyboard
      Identifier: 1133:49291:Logitech_G502_HERO_Gaming_Mouse_Keyboard
      Product ID: 49291
      Vendor ID: 1133
      Active Keyboard Layout: English (US)
      Libinput Send Events: enabled

    Input device: Logitech G502 HERO Gaming Mouse
      Type: Mouse
      Identifier: 1133:49291:Logitech_G502_HERO_Gaming_Mouse
      Product ID: 49291
      Vendor ID: 1133
      Libinput Send Events: enabled

[FILE] **`~/.config/sway/config`Disable mouse acceleration, decrease pointer speed**

    input "1133:49291:Logitech_G502_HERO_Gaming_Mouse"

[FILE] **`~/.config/sway/config`Enable touchpad tap to click**

    input type:touchpad

** Tip**\
Tapping with 1 finger left clicks, 2 right clicks, and 3 middle clicks. This can be adjusted with `tap_button_map`.

### [Application launcher]

Sway works with a variety of application launchers. By default it attempts to use [[[gui-apps/wmenu]](https://packages.gentoo.org/packages/gui-apps/wmenu)[]], it\'s a wayland native launcher.

#### [bemenu]

[[[dev-libs/bemenu]](https://packages.gentoo.org/packages/dev-libs/bemenu)[]] is a dynamic menu library and client program inspired by dmenu. to configure sway to use bemenu:

`root `[`#`]`emerge --ask dev-libs/bemenu`

[FILE] **`~/.config/sway/config`Configure sway to use bemenu.**

    set $menu bemenu-run --no-exec | xargs -r swaymsg exec --

[FILE] **`~/.config/sway/config`Configure sway to use bemenu, with an empty prompt.**

    set $menu bemenu-run --no-exec -p "" | xargs -r swaymsg exec --

** Tip**\
`--line-height` (`-H`) can be set to **26** to make the bemenu height match waybar.

#### [wmenu]

By default sway tries to use [[[gui-apps/wmenu]](https://packages.gentoo.org/packages/gui-apps/wmenu)[]], which can be installed with:

`root `[`#`]`emerge --ask gui-apps/wmenu`

To configure sway to simply use wmenu:

[FILE] **`~/.config/sway/config`Configure Sway to use wmenu**

    set $menu wmenu-run | xargs swaymsg exec --

[FILE] **`~/.config/sway/config`Configure Sway to use wmenu with no prompt**

    set $menu wmenu-run -p "" | xargs swaymsg exec --

### [Status bar]

In addition to Sway\'s own status bar, [Waybar](https://wiki.gentoo.org/wiki/Waybar "Waybar") can be used as a highly customizable status bar for Sway:

`root `[`#`]`emerge --ask gui-apps/waybar`

There are two simple ways to enable Waybar in Sway: executing Waybar as a bar subcommand, or as a regular command. Both will behave the same when Sway starts up (and when Sway exits and starts up again), but they differ in the reloading of Sway. Executing Waybar, or any other status bar, as a bar subcommand will restart the status bar on Sway reload. Executing Waybar as a regular command will *not* restart the status bar on Sway reload; executing with `exec_always` instead of `exec` does not solve this, it only makes more status bars on each Sway reload.

Users that wish to quickly test their status bar configurations via a Sway reload should use the bar subcommand method.

[FILE] **`~/.config/sway/config`Enable Waybar via a bar subcommand**

    bar

[FILE] **`~/.config/sway/config`Enable Waybar via a regular command**

    # Execute Waybar; Waybar does not restart when Sway reloads.
    exec waybar

### [Brightness]

There are several options for adjusting the backlight brightness, it can even be done by writing to [/sys/class/backlight/\<device\>/brightness].

#### [acpilight]

Alternatively, [[[sys-power/acpilight]](https://packages.gentoo.org/packages/sys-power/acpilight)[]] can also accomplish the same brightness changes via a [xbacklight] compatible command:

[FILE] **`~/.config/sway/config`Set the keyboard shortcuts for screen brightness support**

    bindsym XF86MonBrightnessDown exec xbacklight -dec 2
    bindsym XF86MonBrightnessUp exec xbacklight -inc 4

#### [brightnessctl]

[[[app-misc/brightnessctl]](https://packages.gentoo.org/packages/app-misc/brightnessctl)[]] is in **[::guru]** and can be used to simply adjust the backlight:

[FILE] **`~/.config/sway/config`Add brightnessctl keybinds**

    bindsym XF86MonBrightnessDown exec brightnessctl set 5%-
    bindsym XF86MonBrightnessUp exec brightnessctl set 5%+

#### [light]

** Warning**\
The [github page for](https://github.com/haikarainen/light) [[[dev-libs/light]](https://packages.gentoo.org/packages/dev-libs/light)[]] currently (2023-09) states: *\"This project is considered orphaned since the 8th of March, 2023. Use is heavily discouraged until such a time that it is adopted by another developer.\"*. The package currently remains in the [Gentoo ebuild repository](https://wiki.gentoo.org/wiki/Ebuild_repository#The_Gentoo_ebuild_repository "Ebuild repository"), but users may want to take the message from the dev into consideration.

[[[dev-libs/light]](https://packages.gentoo.org/packages/dev-libs/light)[]] can be used to adjust backlights and brightness. Here is an example config:

[FILE] **`~/.config/sway/config`Set the keyboard shortcuts for screen brightness support**

    bindsym XF86MonBrightnessDown exec light -U 2
    bindsym XF86MonBrightnessUp exec light -A 4

#### [ddcutil]

For external monitors, you can use [[[app-misc/ddcutil]](https://packages.gentoo.org/packages/app-misc/ddcutil)[]] to control the brightness via [I^2^C](https://wiki.gentoo.org/wiki/I2C "I2C"):

[FILE] **`~/.config/sway/config`Add ddcutil keybinds**

    bindsym XF86MonBrightnessDown exec ddcutil setvcp 10 - 5
    bindsym XF86MonBrightnessUp exec ddcutil setvcp 10 + 5

### [Notification]

[[[gui-apps/mako]](https://packages.gentoo.org/packages/gui-apps/mako)[]] can be used as a notification daemon.

[FILE] **`~/.config/sway/config`Launch mako daemon when Sway starts**

    exec mako

### [Sound volume]

The `XF86AudioRaiseVolume` and `XF86AudioLowerVolume` keycode are generally present and used to adjust the system volume. This must be bound and set depending on the audio backend.

#### [Pipewire]

If [PipeWire](https://wiki.gentoo.org/wiki/PipeWire "PipeWire") is being used, the following configuration can be used for changing sound volume (with [Wireplumber](https://wiki.gentoo.org/wiki/Wireplumber "Wireplumber")):

[FILE] **`~/.config/sway/config`Set the keyboard shortcuts to change sound volume for PipeWire**

    bindsym XF86AudioMute exec wpctl set-mute @DEFAULT_SINK@ toggle
    # tip: you might consider adding `--limit 1.0` to avoid going over 100% volume
    bindsym XF86AudioRaiseVolume exec wpctl set-volume @DEFAULT_SINK@ 5%+
    bindsym XF86AudioLowerVolume exec wpctl set-volume @DEFAULT_SINK@ 5%-
    bindsym XF86AudioMicMute exec wpctl set-mute @DEFAULT_SOURCE@ toggle

#### [Pulseaudio]

If [pulseaudio](https://wiki.gentoo.org/wiki/Pulseaudio "Pulseaudio") is being used, the following configuration can be used for changing sound volume:

[FILE] **`~/.config/sway/config`Set the keyboard shortcuts to change sound volume for pulseaudio**

    bindsym XF86AudioMute exec pactl set-sink-mute @DEFAULT_SINK@ toggle
    bindsym XF86AudioRaiseVolume exec pactl set-sink-volume @DEFAULT_SINK@ +5%
    bindsym XF86AudioLowerVolume exec pactl set-sink-volume @DEFAULT_SINK@ -5%
    bindsym XF86AudioMicMute exec pactl set-source-mute @DEFAULT_SOURCE@ toggle

#### [ALSA]

If [ALSA](https://wiki.gentoo.org/wiki/ALSA "ALSA") is being used, the following configuration can be used for changing the sound volume:

[FILE] **`~/.config/sway/config`Set the keyboard shortcuts to change sound volume for ALSA**

    bindsym XF86AudioRaiseVolume exec amixer -Mq set Speaker 5%+
    bindsym XF86AudioLowerVolume exec amixer -Mq set Speaker 5%-

#### [sndio]

If [[[media-sound/sndio]](https://packages.gentoo.org/packages/media-sound/sndio)[]] is being used, the following configuration can be used for changing the sound volume:

[FILE] **`~/.config/sway/config`Set the keyboard shortcuts to change sound volume for sndio**

    bindsym XF86AudioRaiseVolume exec sndioctl -f snd/default output.level=+0.05
    bindsym XF86AudioLowerVolume exec sndioctl -f snd/default output.level=-0.05

### [Taking screenshots]

#### [Simple approach: use slurpshot]

([Slurpshot](https://github.com/de-arl/slurpshot)) is a script to simplify taking screenshots. It uses native wayland apps only and enables selecting specific windows only, as well as previewing and printing screenshots withous saving them. First install dependencies:

`root `[`#`]`emerge --ask gui-apps/grim gui-apps/slurp app-misc/jq dev-libs/bemenu`

Put the slurpshot script somewhere in your PATH, for example to \~/bin, make it executable and just set one keybind:

[FILE] **`~/.config/sway/config`Set the keyboard shortcuts for slurpshot support**

    #
    # Screen capture
    #
    bindsym Print exec slurpshot

#### [Manual approach]

To add screenshot support, use the [grim] utility (found in the [[[gui-apps/grim]](https://packages.gentoo.org/packages/gui-apps/grim)[]] package). The abbreviation `grim` is defined as **Gr**ab **Im**ages. This utility is tailored to the specifics of the Wayland protocol. In order to install grim, use the following command:

`root `[`#`]`emerge --ask gui-apps/grim`

To add support for determining the boundaries of the selected screen area, the [slurp] utility, found in the [[[gui-apps/slurp]](https://packages.gentoo.org/packages/gui-apps/slurp)[]] package, is used in combination with the [grim] utility. To install slurp, use the command:

`root `[`#`]`emerge --ask gui-apps/slurp`

To add clipboard support [wl-clipboard] is used, found in [[[gui-apps/wl-clipboard]](https://packages.gentoo.org/packages/gui-apps/wl-clipboard)[]]. To install wl-clipboard, use the command:

`root `[`#`]`emerge --ask gui-apps/wl-clipboard`

Next, edit the configuration file to add support for keyboard shortcuts to perform a screenshot operation:

[FILE] **`~/.config/sway/config`Set the keyboard shortcuts for screenshot support**

    #
    # Screen capture
    #
    set $ps1 Print
    set $ps2 Control+Print
    set $ps3 Alt+Print
    set $ps4 Alt+Control+Print
    set $psf $(xdg-user-dir PICTURES)/ps_$(date +"%Y%m%d%H%M%S").png

    bindsym $ps1 exec grim - | wl-copy
    bindsym $ps2 exec grim -g "$(slurp)" - | wl-copy
    bindsym $ps3 exec grim $psf
    bindsym $ps4 exec grim -g "$(slurp)" $psf

Please note that the [Print] or [Ctrl] + [Print] keys combination creates a screenshot in the `wl-copy` buffer. This allows pasting the image directly from the clipboard, without having to save to a file on disk.

For the [Alt] + [Print] or [Alt] + [Ctrl] + [Print] keyboard shortcuts, the method of automatically saving the image file in the [Pictures] user directory is used.

#### [Snipping tool like behavior]

The following captures an area of the screen to the clipboard when [mod]+[shift]+[S] is pressed:

[FILE] **`~/.config/sway/config`Similar function to the snipping tool**

    bindsym $mod+shift+s exec grim -g "$(slurp)" - | wl-copy

** Note**\
**-g** tells [grim] to crop to a region, and \$(slurp) obtains the region. The screenshot is output to *stdout* where [wl-copy] copies the file to the clipboard.

### [Set a random wallpaper]

Default configuration uses [[[gui-apps/swaybg]](https://packages.gentoo.org/packages/gui-apps/swaybg)[]] for wallpapers, other packages are available too. A random wallpaper can be pulled from a folder using **swaybg** and be set: ^[\[1\]](#cite_note-1)^

[FILE] **`~/.config/sway/config`Set a random wallpaper from a folder**

    set $wallpapers_path $HOME/Pictures/Wallpapers
    output * bg $(find $wallpapers_path -type f | shuf -n 1) fill

### [Swaylock]

[[[gui-apps/swaylock]](https://packages.gentoo.org/packages/gui-apps/swaylock)[]] can be used to lock the current session.

`root `[`#`]`emerge --ask gui-apps/swaylock`

[FILE] **`~/.config/sway/config`Lock the session when [\$mod]+[l] is pressed**

    bindsym $mod+l exec swaylock --ignore-empty-password --show-failed-attempts --color 1e1e1e

[FILE] **`~/.config/sway/config`With colors [man swaylock] for more info**

    bindsym $mod+l exec swaylock --ignore-empty-password --show-failed-attempts \
        --color 1e1e1e --inside-color cccccc --ring-color ffffff \
        --inside-clear-color 11a8cd --ring-clear-color 29b8db \
        --inside-ver-color 2472c8 --ring-ver-color 3b8eea \
        --inside-wrong-color cd3131 --ring-wrong-color f14c4c

** Warning**\
If the account is locked out, swaylock will not indicate this, and will simply fail. Switching to another TTY and attempting login can help diagnose this

### [Swayidle]

[[[gui-apps/swayidle]](https://packages.gentoo.org/packages/gui-apps/swayidle)[]] runs a command after a certain idle time, typically to lock and/or power off the screen.

`root `[`#`]`emerge --ask gui-apps/swayidle`

[FILE] **`~/.config/sway/config`Power off all displays after 15 minutes of idle**

    exec swayidle -w \
      timeout 900 'swaymsg "output * power off"' \
      resume 'swaymsg "output * power on"'

### [HiDPI]

To adjust sway\'s rendering for HiDPI displays (4K and above), the name of the display to be adjusted must be obtained. After a sway session is running, issue the following:

`user `[`$`]`swaymsg -t get_outputs`

** Note**\
The `swaymsg` USE flag must be enabled for the [swaymsg] command to be available on the system.

The `output` statement in the sway configuration file will accept a `scale` parameter to adjust the scaling of the high resolution display.

### [Xresources]

[FILE] **`~/.config/sway/config`Reload `~/.Xresources` on sway reload**

    exec_always test -f ~/.Xresources && xrdb -merge ~/.Xresources

### [GTK configuration]

#### [Dark Mode]

##### [GTK4]

GTK4 dark mode can be enabled by setting:

[FILE] **`~/.config/gtk-4.0/settings.ini`Enable gtk4 dark mode**

    [Settings]
    gtk-application-prefer-dark-theme = true

##### [GTK3]

GTK3 dark mode can be enabled by setting:

[FILE] **`~/.config/gtk-3.0/settings.ini`Enable gtk3 dark mode**

    [Settings]
    gtk-application-prefer-dark-theme = true

##### [GTK2]

GTK2 does not have a dark mode toggle, a dark theme must be selected:

[FILE] **`~/.gtkrc-2.0`Enable gtk2 dark mode**

    gtk-theme-name = "Adwaita-dark"

#### [GTK3 Themes and Fonts]

Currently setting a GTK font and theme should be done by editing sway\'s configuration file (see [Sway\'s wiki](https://github.com/swaywm/sway/wiki/GTK-3-settings-on-Wayland) as well):

[FILE] **`~/.config/sway/config`Set the font and theme for GTK applications**

    set $gnome-schema org.gnome.desktop.interface
    exec_always

If encountering problems setting the mouse cursor with certain applications (including sway), this may help:

[FILE] **`~/.config/sway/config`Set the cursor theme**

    seat seat0 xcursor_theme custom_cursor_theme custom_cursor_size

Replace *custom_cursor_theme* and *custom_cursor_size*. **Adwaita** and **24** are pretty much default on all Linux distributions.

### [Automatic floating windows]

By default, Sway opens new windows in tiling mode. The following configuration snippet makes many common windows which should float, float:

[FILE] **`~/.config/sway/config`More reasonable floating windows^[\[2\]](#cite_note-2)^**

    for_window [window_role = "pop-up"] floating enable
    for_window [window_role = "bubble"] floating enable
    for_window [window_role = "dialog"] floating enable
    for_window [window_type = "dialog"] floating enable
    for_window [window_role = "task_dialog"] floating enable
    for_window [window_type = "menu"] floating enable
    for_window [app_id = "floating"] floating enable
    for_window [app_id = "floating_update"] floating enable, resize set width 1000px height 600px
    for_window [class = "(?i)pinentry"] floating enable
    for_window [title = "Administrator privileges required"] floating enable

#### [Firefox Tweaks]

[FILE] **`~/.config/sway/config`Make relevant Firefox windows float^[\[3\]](#cite_note-3)^**

    for_window [title = "About Mozilla Firefox"] floating enable
    for_window [window_role = "About"] floating enable
    for_window [app_id="firefox" title="Library"] floating enable, border pixel 1, sticky enable

[FILE] **`~/.config/sway/config`Remove the sharing indicator window for Firefox^[\[4\]](#cite_note-4)^**

    for_window [title = "Firefox - Sharing Indicator"] kill
    for_window [title = "Firefox — Sharing Indicator"] kill

#### [Steam Tweaks]

[FILE] **`~/.config/sway/config`Make Steam dialog windows float^[\[5\]](#cite_note-5)^**

    for_window [class="^(steam$)" title="^(?!Steam$)"] floating enable

### [Service]

#### [OpenRC]

On [OpenRC](https://wiki.gentoo.org/wiki/OpenRC "OpenRC") based systems, [elogind](https://wiki.gentoo.org/wiki/Elogind "Elogind") must be added to the *boot* runlevel:

`root `[`#`]`rc-update add elogind boot`

### [Switching Keyboard Layouts]

Sway uses [[[gui-libs/wlroots]](https://packages.gentoo.org/packages/gui-libs/wlroots)[]] and supports [[[x11-libs/libxkbcommon]](https://packages.gentoo.org/packages/x11-libs/libxkbcommon)[]] keyboard layouts. Configure the keyboard layout in the `~/.config/sway/config` file or change it dynamically using:

`user `[`$`]`swaymsg`

#### [Temporarily change keyboard layout]

To switch the layout of the keyboard for the current session, use the following command:

`user `[`$`]`swaymsg input type:keyboard xkb_layout "fr"`

Replace `"fr"` with the desired layout code (e.g., `"us"`, `"de"`, `"es"`). This change is immediate, but it will reset when Sway is restarted.

To make the layout persistent across sessions, add the following to your Sway configuration file:

[FILE] **`~/.config/sway/config`Change the keyboard layout**

    input type:keyboard

#### [Switching between layouts with a keybinding]

Define multiple layouts and enable a keyboard shortcut to toggle between them. Add this section to the Sway config:

[FILE] **`~/.config/sway/config`Enable a keyboard shortcut to switch between multiple keyboard layouts**

    input type:keyboard

This sets up US and French layouts and allows toggling between them using [Alt]+[Shift]. You can customize the toggle shortcut by changing `xkb_options`.

A full list of options can be found by running:

`root `[`#`]`cat /usr/share/x11/xkb/rules/base.lst | less`

## [Usage]

### [Starting Sway]

** Tip**\
Although not officially supported, some [display managers](https://wiki.gentoo.org/wiki/Display_manager "Display manager") may work with sway.^[\[6\]](#cite_note-6)^

** Important**\
Starting Sway with dbus requires that `XDG_RUNTIME_DIR` is set. **elogind** or *systemd* will set this if used. Omitting the [dbus-run-session] may cause [runtime errors](https://wiki.gentoo.org/wiki/Sway#Failed_to_connect_to_user_bus "Sway").

** See also**\
[Starting Sway without elogind](https://wiki.gentoo.org/wiki/Sway#Starting_Sway_without_elogind_or_systemd "Sway").

#### [Launching Sway automatically with TTY login]

To start Sway on login to the first TTY:

[FILE] **`~/.bashrc`Launch Sway after logging into the first TTY**

    if [ -z "$" ] && [ "$" -eq 1 ]; then
        dbus-run-session sway
    fi

##### [Automatic login on tty1]

To enable automatic login on tty1, `--skip-login` and `--login-options` can be added to tty1\'s [agetty] instance defined in [/etc/inittab]:

[FILE] **`/etc/inittab`Automatically login as Larry on tty1**

    c1:12345:respawn:/sbin/agetty --noclear 38400 tty1 linux --skip-login --login-options larry

#### [Starting Sway manually]

`user `[`$`]`dbus-run-session sway`

#### [Launching Sway from a script]

This method uses a script to forcibly take over a virtual terminal and launch Sway in it. The typical use case is to launch Sway automatically on boot.

** Note**\
Sway is not supposed to be launched this way, the script may need some tuning to work.

[FILE] **`/usr/sbin/sway_launcher`Sway Launcher**

    #!/bin/sh

    # Launch sway with a specific user, from a specific Virtual Terminal (vt)
    # Two arguments are expected: a username (e.g., larry) and the id of a free vt (e.g., 7)

    # prepare the tty for the user. vtX uses /dev/ttyX
    chown "$1" "/dev/tty$"
    chmod 600 "/dev/tty$"

    # setup a clean environment for the user, take over the target vt, then launch sway
    su --login --command "openvt --switch --console $ -- sway >\$/.sway_autolauncher.log 2>&1" "$1"
    # this script returns immediately

This script has a few limitations:

-   `XDG_RUNTIME_DIR` is expected to be defined and valid, see the section above.
-   Without the `--switch` option for openvt, sway will freeze when trying to switch to a different VT ([Ctrl]+[Alt]+[Fn]), whether this is a bug or not is unknown.
-   The VT is not cleared when Sway exits, clear it by calling deallocvt.
-   Similarly the TTY\'s owner and mode are not changed back to their default values when Sway exits.

Launching this script on boot can be done with the [*local*](https://wiki.gentoo.org/wiki//etc/local.d "/etc/local.d") service:

[FILE] **`/etc/local.d/sway.start`Launch Sway on boot**

    #!/bin/sh
    sway_launcher larry 7

#### [Starting Sway without elogind or systemd]

Systems that are configured with neither systemd nor elogind will need to create a shell script (or use some other means) to set the `XDG_RUNTIME_DIR` variable.

The environment variable can be defined in the usual configuration files. For example, if [Larry the cow (Larry) ](https://wiki.gentoo.org/wiki/User:Larry "User:Larry") sets the `XDG_RUNTIME_DIR` variable in his shell\'s configuration file and he has chosen that the directory will be in [/tmp]:

[FILE] **`/home/larry/.bash_profile`Set the `XDG_RUNTIME_DIR` variable**

    #!/bin/sh
    if test -z "$"; then
      export XDG_RUNTIME_DIR=/tmp/"$"-runtime-dir
        if ! test -d "$"; then
            mkdir "$"
            chmod 0700 "$"
        fi
    fi

With the `XDG_RUNTIME_DIR` defined, sway can be launched as usual:

`user `[`$`]`dbus-run-session sway`

If issues are encountered, check [Sway issues on GitHub](https://github.com/swaywm/sway/issues) before contacting the Sway community on IRC ([[#sway](ircs://irc.libera.chat/#sway)] ([[webchat](https://web.libera.chat/#sway)])) or opening a [new Gentoo bug](https://bugs.gentoo.org/).

### [Movement]

All key combinations will be defined in the [\~/.config/sway/config] configuration file.

The [Super] key is defined as the `$mod` value by default. On most keyboards this will be the Windows key.

Sway has a [Vi](https://wiki.gentoo.org/wiki/Vim "Vim")-like interface. [h] (left), [j] (down), [k] (up), and [l] (right) can be used for movement, in addition to the arrow keys.

Focus can be moved with [mod]+[direction key], windows can be moved with [mod]+[shift]+[direction key]:

[FILE] **`~/.config/sway/config`Default movement definitions**

    bindsym $mod+Left focus left
    bindsym $mod+Down focus down
    bindsym $mod+Up focus up
    bindsym $mod+Right focus right

    bindsym $mod+Shift+Left move left
    bindsym $mod+Shift+Down move down
    bindsym $mod+Shift+Up move up
    bindsym $mod+Shift+Right move right

See [man 5 sway-input] for more information.

#### [Useful binds]

[FILE] **`~/.config/sway/config`Cycle between workspaces with [mod]+[control]+[left arrow] and [mod]+[control]+[right arrow]**

    bindsym $mod+control+Right workspace next
    bindsym $mod+control+Left workspace prev

### [Layouts]

By default, Sway uses a tiling layout. Layout modes can be switched with the following default binds:

-   [mod]+[b] - Horizontal split
-   [mod]+[v] - Vertical split
-   [mod]+[s] - Stacking
-   [mod]+[w] - Tabbed
-   [mod]+[e] - Toggle split
-   [mod]+[shift]+[space] - Toggle floating

[FILE] **`~/.config/sway/config`Default layout definitions**

    bindsym $mod+b splith
    bindsym $mod+v splitv

    bindsym $mod+s layout stacking
    bindsym $mod+w layout tabbed
    bindsym $mod+e layout toggle split

    bindsym $mod+Shift+space floating toggle

### [Terminal]

The default key combination to open a terminal emulator is [\$mod]+[Enter].

#### [Foot Server]

[Foot](https://wiki.gentoo.org/wiki/Foot "Foot") is a minimal Wayland terminal emulator that can be configured to run as a server, reducing resource usage.

[FILE] **`~/.config/sway/config`Start the Foot server with Sway**

    exec foot -s

[FILE] **`~/.config/sway/config`Set the default terminal to be a foot client**

    set $term footclient

** Note**\
If starting the foot server with Sway, it may not start fast enough to also auto-start a service, [exec swaymsg \"workspace 2; exec \$term \"] may be slow enough to mitigate this

### [Adding features]

Sway is designed to be extended, adding additional features is easy:

[FILE] **`~/.config/sway/config`Start htop when [control]+[shift]+[esc] is pressed**

    bindsym control+shift+escape exec $term htop

If using foot, the **app_id**, which is set with **-a**, can be set to make it float automatically:

[FILE] **`~/.config/sway/config`Start htop floating when [control]+[shift]+[esc] is pressed**

    bindsym control+shift+escape exec $term -a 'flying-foot' htop
    for_window [app_id="flying-foot"] floating enable

#### [Moving left and right with non-existing workspaces]

Sway can switch to the left (`prev`) or right (`next`) workspace as long as there exists a workspace to switch to in that direction; this includes moving containers to those workspaces:

[FILE] **`~/.config/sway/config`**

    set $super mod4
    bindsym $super+alt+left  workspace prev
    bindsym $super+alt+right workspace next
    bindsym $super+control+alt+left  move container to workspace prev, workspace prev
    bindsym $super+control+alt+right move container to workspace next, workspace next

To be able to switch to non-existing workspaces, we can create a script to tell Sway to switch to a specific workspace:

[FILE] **`~/.config/sway/config`**

    set $super             mod4
    set $num_of_workspaces 10
    bindsym $super+alt+left          exec swaymsg -pt get_workspaces | gawk -f ~/.config/sway/workspace.gawk -v move_type="left"  -v num_of_workspaces=$num_of_workspaces
    bindsym $super+alt+right         exec swaymsg -pt get_workspaces | gawk -f ~/.config/sway/workspace.gawk -v move_type="right" -v num_of_workspaces=$num_of_workspaces
    bindsym $super+control+alt+left  exec swaymsg -pt get_workspaces | gawk -f ~/.config/sway/workspace.gawk -v move_type="container_left"  -v num_of_workspaces=$num_of_workspaces
    bindsym $super+control+alt+right exec swaymsg -pt get_workspaces | gawk -f ~/.config/sway/workspace.gawk -v move_type="container_right" -v num_of_workspaces=$num_of_workspaces

[FILE] **`~/.config/sway/workspace.gawk`**

    #!/bin/gawk -f

    $3 == "(focused)"
    }

### [Font size adjustment]

[FILE] **`~/.config/sway/config`**

    # For status bar
    bar
    # Globally
    font Fira Sans SemiBold 13

To get current Sway font use

`user `[`$`]`swaymsg -t get_config | grep font`

For [foot] terminal:

[FILE] **`~/.config/foot/foot.ini`**

    [main]
    font=Mono:style=Regular:size=14

## [Troubleshooting]

### [Screen sharing does not work]

Ensure your Sway configuration isn\'t setting outputs with render_bit_depth 10, as only render_bit_depth 8 is supported for screen sharing.

Make sure the package [[[gui-libs/xdg-desktop-portal-wlr]](https://packages.gentoo.org/packages/gui-libs/xdg-desktop-portal-wlr)[]] is installed. By default, it is autostarted by D-Bus but it fails to run because it needs environment variables exported by Sway, and the D-Bus session is started before Sway. To fix, update the D-Bus environment by adding the following line to the beginning of Sway\'s config:

[FILE] **`~/.config/sway/config`**

    exec --no-startup-id dbus-update-activation-environment --all

Also see [this link](https://github.com/emersion/xdg-desktop-portal-wlr/wiki/%22It-doesn't-work%22-Troubleshooting-Checklist) to see if [PipeWire](https://wiki.gentoo.org/wiki/PipeWire "PipeWire") is working properly. Ensure XDG_CURRENT_DESKTOP=sway. If using systemd and wireplumber, you may have to enable wireplumber.**service** ; wireplumber.**socket** may not be enough.

### [Failed to connect to user bus]

`[swaybar/tray/tray.c:42] Failed to connect to user bus: No such file or directory`

-   Forum topic [\[swaybar/tray/tray.c:42\] Failed to connect to user bus: No such file or directory](https://forums.gentoo.org/viewtopic-p-8552581.html#8552581) =\> Use [dbus-run-session sway]
-   Forum topic [sway(bar) with tray support](https://forums.gentoo.org/viewtopic-p-8364686.html#8364686)
-   [https://github.com/swaywm/sway/issues/1415](https://github.com/swaywm/sway/issues/1415)

### [Warning: no icon themes loaded]

`[swaybar/tray/icon.c:348] Warning: no icon themes loaded`

It is looking for [[[x11-themes/hicolor-icon-theme]](https://packages.gentoo.org/packages/x11-themes/hicolor-icon-theme)[]]

### [No backend was able to open a seat]

`[ERROR] [wlr] [libseat] [libseat/libseat.c:78] No backend was able to open a seat`

Make sure you have done everything in [Usage](https://wiki.gentoo.org/wiki/Sway#Usage "Sway") correctly.

You will need to install a seat management daemon such as [[[sys-auth/seatd]](https://packages.gentoo.org/packages/sys-auth/seatd)[]] or [[[sys-auth/elogind]](https://packages.gentoo.org/packages/sys-auth/elogind)[]] and enable the corresponding service. Also check whether setting `XDG_RUNTIME_DIR` is required. If using the `elogind` package, it should set the `XDG_RUNTIME_DIR` variable automatically with no further configuration needed. This is not the case with the `seatd` package, and you will have to set the variable yourself, refer to [Starting Sway without elogind or systemd](https://wiki.gentoo.org/wiki/Sway#Starting_Sway_without_elogind_or_systemd "Sway") for instructions. Also check whether the user needs to be in the `seat` group.

** Important**\
If [[[sys-auth/seatd]](https://packages.gentoo.org/packages/sys-auth/seatd)[]] is used, the [[[server]](https://packages.gentoo.org/useflags/server)[[]](https://wiki.gentoo.org/wiki/USE_flag "USE flag")] [USE flag](https://wiki.gentoo.org/wiki/USE_flag "USE flag") is required.

### [Applications forget logins]

Some applications (e. g. [[[net-misc/nextcloud-client]](https://packages.gentoo.org/packages/net-misc/nextcloud-client)[]]) use a Secret-Service-Agent to save credentials for login. If applications ask for account credentials every run, an incorrectly configured Secret-Service-Agent might be the reason.

First, emerge [[[gnome-base/gnome-keyring]](https://packages.gentoo.org/packages/gnome-base/gnome-keyring)[]].

`root `[`#`]`emerge --ask gnome-base/gnome-keyring`

Then, enable the `gnome-keyring` USE flag.

[FILE] **`/etc/portage/package.use`**

    # Sway Secret-Service-Agent
    */* gnome-keyring

Update the system to apply the new USE flag.

`root `[`#`]`emerge -avuDN @world`

To run and unlock the Agent\'s storage when logging into a Sway session, edit these two files.

[FILE] **`~/.config/sway/config`**

    exec dbus-update-activation-environment --all
    exec gnome-keyring-daemon --start --components=secrets
    exec export $(gnome-keyring-daemon)

[FILE] **`/etc/pam.d/login`**

    auth      optional  pam_gnome_keyring.so
    password  optional  pam_gnome_keyring.so
    session   optional  pam_gnome_keyring.so auto_start

## [See also]

-   [i3](https://wiki.gentoo.org/wiki/I3 "I3") --- a minimalist [tiling](https://en.wikipedia.org/wiki/Tiling_window_manager "wikipedia:Tiling window manager") [window manager](https://wiki.gentoo.org/wiki/Window_manager "Window manager"), completely written from scratch.
-   [List of software for Wayland](https://wiki.gentoo.org/wiki/List_of_software_for_Wayland "List of software for Wayland") --- various desktop related packages for Wayland
-   [Wayland](https://wiki.gentoo.org/wiki/Wayland "Wayland") --- a [communication protocol](https://en.wikipedia.org/wiki/communication_protocol "wikipedia:communication protocol") between a [display server](https://en.wikipedia.org/wiki/display_server "wikipedia:display server") and its clients
-   [Weston](https://wiki.gentoo.org/wiki/Weston "Weston") --- a reference implementation of a [Wayland compositor](https://wiki.gentoo.org/wiki/Wayland_compositor "Wayland compositor").

## [References]

1.  [[[↑](#cite_ref-1)] [[https://github.com/swaywm/sway/issues/1269](https://github.com/swaywm/sway/issues/1269)]]
2.  [[[↑](#cite_ref-2)] [[https://github.com/Madic-/Sway-DE/blob/master/config/sway/sway.d/06_floating.conf](https://github.com/Madic-/Sway-DE/blob/master/config/sway/sway.d/06_floating.conf)]]
3.  [[[↑](#cite_ref-3)] [[https://github.com/Madic-/Sway-DE/blob/master/config/sway/sway.d/06_floating.conf](https://github.com/Madic-/Sway-DE/blob/master/config/sway/sway.d/06_floating.conf)]]
4.  [[[↑](#cite_ref-4)] [[https://github.com/Madic-/Sway-DE/blob/master/config/sway/sway.d/06_floating.conf](https://github.com/Madic-/Sway-DE/blob/master/config/sway/sway.d/06_floating.conf)]]
5.  [[[↑](#cite_ref-5)] [[https://github.com/nishiiko/swayfx-dots/blob/main/.config/sway/config.d/windowrules](https://github.com/nishiiko/swayfx-dots/blob/main/.config/sway/config.d/windowrules)]]
6.  [[[↑](#cite_ref-6)] [[https://github.com/swaywm/sway#running](https://github.com/swaywm/sway#running)]]