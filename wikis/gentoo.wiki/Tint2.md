[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=Tint2&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

**Resources**

[[]][Home](https://gitlab.com/o9000/tint2)

[[]][Package information](https://packages.gentoo.org/packages/x11-misc/tint2)

[[]][Official documentation](https://gitlab.com/o9000/tint2/wikis/home)

**tint2** is a lightweight panel/taskbar specifically made for [Openbox](https://wiki.gentoo.org/wiki/Openbox "Openbox"), but it can also work with other window managers.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE Flags]](#USE_Flags)
    -   [[1.2] [Emerge]](#Emerge)
-   [[2] [Configuration]](#Configuration)
-   [[3] [External resources]](#External_resources)

## [Installation]

### [USE Flags]

### [USE flags for] [x11-misc/tint2](https://packages.gentoo.org/packages/x11-misc/tint2) [[]] [Lightweight panel/taskbar for Linux]

  ------------------------------------------------------------------------------------- -----------------------------------------------------
  [`startup-notification`](https://packages.gentoo.org/useflags/startup-notification)   Enable application startup event feedback mechanism
  [`svg`](https://packages.gentoo.org/useflags/svg)                                     Add support for SVG (Scalable Vector Graphics)
  [`tint2conf`](https://packages.gentoo.org/useflags/tint2conf)                         Build/Install tint2conf as well
  ------------------------------------------------------------------------------------- -----------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-02-14 00:28] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

`root `[`#`]`emerge --ask x11-misc/tint2`

## [Configuration]

[FILE] **`~/.config/tint2/tint2rc`**

    # Tint2 config file

    # Background definitions
    # ID 1
    rounded = 7
    border_width = 2
    background_color = #000000 60
    border_color = #FFFFFF 16

    # ID 2
    rounded = 5
    border_width = 0
    background_color = #FFFFFF 40
    border_color = #FFFFFF 48

    # ID 3
    rounded = 5
    border_width = 0
    background_color = #FFFFFF 16
    border_color = #FFFFFF 68

    # Panel
    panel_monitor = all
    panel_position = bottom center horizontal
    panel_size = 94% 30
    panel_margin = 0 0
    panel_padding = 7 0 7
    panel_dock = 0
    wm_menu = 0
    panel_layer = top
    panel_background_id = 1
    panel_items = LTSBC

    # Panel Autohide
    autohide = 0
    autohide_show_timeout = 0.3
    autohide_hide_timeout = 2
    autohide_height = 2
    strut_policy = follow_size

    # Taskbar
    taskbar_mode = single_desktop
    taskbar_padding = 2 3 2
    taskbar_background_id = 0
    taskbar_active_background_id = 0

    # Tasks
    urgent_nb_of_blink = 8
    task_icon = 1
    task_text = 1
    task_centered = 1
    task_maximum_size = 140 35
    task_padding = 6 2
    task_background_id = 3
    task_active_background_id = 2
    task_urgent_background_id = 2
    task_iconified_background_id = 3

    # Task Icons
    task_icon_asb = 70 0 0
    task_active_icon_asb = 100 0 0
    task_urgent_icon_asb = 100 0 0
    task_iconified_icon_asb = 70 0 0

    # Fonts
    task_font = sans 7
    task_font_color = #FFFFFF 68
    task_active_font_color = #FFFFFF 83
    task_urgent_font_color = #FFFFFF 83
    task_iconified_font_color = #FFFFFF 68
    font_shadow = 0

    # System Tray
    systray = 1
    systray_padding = 0 4 5
    systray_sort = ascending
    systray_background_id = 0
    systray_icon_size = 16
    systray_icon_asb = 70 0 0

    # Clock
    time1_format = %H:%M
    time1_font = sans 8
    time2_format = %A %d %B
    time2_font = sans 6
    clock_font_color = #FFFFFF 74
    clock_padding = 1 0
    clock_background_id = 0
    clock_rclick_command = orage

    # Tooltips
    tooltip = 0
    tooltip_padding = 2 2
    tooltip_show_timeout = 0.7
    tooltip_hide_timeout = 0.3
    tooltip_background_id = 1
    tooltip_font = sans 10
    tooltip_font_color = #000000 80

    # Mouse
    mouse_middle = none
    mouse_right = close
    mouse_scroll_up = toggle
    mouse_scroll_down = iconify

    # Battery
    battery = 1
    battery_low_status = 10
    battery_low_cmd = notify-send "battery low"
    battery_hide = 98
    bat1_font = sans 8
    bat2_font = sans 6
    battery_font_color = #FFFFFF 74
    battery_padding = 1 0
    battery_background_id = 0

    #------------------------------------------
      #LAUNCHER
      #------------------------------------------
      launcher_icon_theme = areao43
      launcher_padding = 2 2
      launcher_background_id = 1
      launcher_icon_size = 20
      launcher_item_app = /usr/share/applications/firefox-bin.desktop
      launcher_item_app = /usr/share/applications/xterm.desktop

    # End of config

## [External resources]

-   [ArchWiki - tint2](https://wiki.archlinux.org/index.php/Tint2)