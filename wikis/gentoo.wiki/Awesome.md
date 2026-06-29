Other languages:

-   [Deutsch](https://wiki.gentoo.org/wiki/Awesome/de "Awesome (100% translated)")
-   [English]
-   [Nederlands](https://wiki.gentoo.org/wiki/Awesome/nl "awesome/nl (5% translated)")
-   [español](https://wiki.gentoo.org/wiki/Awesome/es "Awesome (41% translated)")
-   [français](https://wiki.gentoo.org/wiki/Awesome/fr "Awesome (99% translated)")
-   [italiano](https://wiki.gentoo.org/wiki/Awesome/it "Awesome (53% translated)")
-   [magyar](https://wiki.gentoo.org/wiki/Awesome/hu "awesome (100% translated)")
-   [polski](https://wiki.gentoo.org/wiki/Awesome/pl "Awesome/pl (1% translated)")
-   [português do Brasil](https://wiki.gentoo.org/wiki/Awesome/pt-br "Awesome (41% translated)")
-   [русский](https://wiki.gentoo.org/wiki/Awesome/ru "Awesome (95% translated)")
-   [中文（中国大陆）‎](https://wiki.gentoo.org/wiki/Awesome/zh-cn "Awesome (53% translated)")
-   [日本語](https://wiki.gentoo.org/wiki/Awesome/ja "awesome (100% translated)")
-   [한국어](https://wiki.gentoo.org/wiki/Awesome/ko "awesome/ko (41% translated)")

**Resources**

[[]][Home](https://awesomewm.org/)

[[]][Package information](https://packages.gentoo.org/packages/x11-wm/awesome)

[[]][Wikipedia](https://en.wikipedia.org/wiki/awesome_(window_manager) "wikipedia:awesome (window manager)")

[[]][GitHub](https://github.com/awesomeWM/awesome)

[[]][[#awesome](ircs://irc.libera.chat/#awesome)] ([[webchat](https://web.libera.chat/#awesome)])

[![Ohloh Logo](/images/thumb/c/c1/Ohloh-logo.png/30px-Ohloh-logo.png)][Open Hub](https://www.openhub.net/p/awesome)

**awesome** is a highly configurable, next generation, dynamic [window manager](https://wiki.gentoo.org/wiki/Window_manager "Window manager") for [X](https://wiki.gentoo.org/wiki/X "X"). It is primarily targeted at power users, developers and any people dealing with every day computing tasks and who want to have fine-grained control on their graphical environment. It is extended using the [Lua](https://wiki.gentoo.org/wiki/Lua "Lua") programming language.

## Contents

-   [[1] [Prerequisites]](#Prerequisites)
    -   [[1.1] [Services]](#Services)
    -   [[1.2] [Miscellaneous]](#Miscellaneous)
    -   [[1.3] [X server]](#X_server)
        -   [[1.3.1] [Starting the X server]](#Starting_the_X_server)
-   [[2] [Installation]](#Installation)
    -   [[2.1] [USE flags]](#USE_flags)
    -   [[2.2] [Emerge]](#Emerge)
-   [[3] [Configuration]](#Configuration)
    -   [[3.1] [Starting]](#Starting)
    -   [[3.2] [Configuration file]](#Configuration_file)
    -   [[3.3] [Tags]](#Tags)
    -   [[3.4] [Menu]](#Menu)
    -   [[3.5] [Date]](#Date)
    -   [[3.6] [Volume control]](#Volume_control)
    -   [[3.7] [MPD multimedia keys]](#MPD_multimedia_keys)
    -   [[3.8] [Removing window gaps]](#Removing_window_gaps)
    -   [[3.9] [Debugging the configuration with Xephyr]](#Debugging_the_configuration_with_Xephyr)
-   [[4] [Keyboard shortcuts]](#Keyboard_shortcuts)
-   [[5] [External resources]](#External_resources)

## [[] Prerequisites]

### [[] Services]

Choose exactly one of:

-   [elogind](https://wiki.gentoo.org/wiki/Elogind "Elogind"): Standalone logind package, extracted from the systemd project for use with [OpenRC](https://wiki.gentoo.org/wiki/OpenRC "OpenRC") or other init systems.
-   [systemd](https://wiki.gentoo.org/wiki/Systemd "Systemd"): Uses the session tracker part of systemd. Users of systemd do not need to take any other initiative here.

### [[] Miscellaneous]

-   [D-Bus](https://wiki.gentoo.org/wiki/D-Bus "D-Bus"): Enables use of the D-Bus message bus system.
-   [polkit](https://wiki.gentoo.org/wiki/Polkit "Polkit"): Enables the polkit framework for controlling privileges for system-wide services.
-   [udisks](https://wiki.gentoo.org/wiki/Udisks "Udisks"): Enables support for some storage related services.

### [[] X server]

Follow the instructions on [Xorg/Guide](https://wiki.gentoo.org/wiki/Xorg/Guide "Xorg/Guide") to set up the [X](https://wiki.gentoo.org/wiki/X "X") environment.

#### [[] Starting the X server]

One of the following methods can be used to start [X](https://wiki.gentoo.org/wiki/X "X"):

-   [Display manager](https://wiki.gentoo.org/wiki/Display_manager "Display manager"): Presents the user with a graphical login screen.
-   [X without Display Manager](https://wiki.gentoo.org/wiki/X_without_Display_Manager "X without Display Manager"): When running a single-user system, one may find display managers an unnecessary waste of resources.

## [[] Installation]

### [[] USE flags]

### [USE flags for] [x11-wm/awesome](https://packages.gentoo.org/packages/x11-wm/awesome) [[]] [Dynamic floating and tiling window manager]

  ------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------
  [`dbus`](https://packages.gentoo.org/useflags/dbus)     Enable dbus support for anything that needs it (gpsd, gnomemeeting, etc)
  [`doc`](https://packages.gentoo.org/useflags/doc)       Add extra documentation (API, Javadoc, etc). It is recommended to enable per package instead of globally
  [`gnome`](https://packages.gentoo.org/useflags/gnome)   Add GNOME support
  [`test`](https://packages.gentoo.org/useflags/test)     Enable dependencies and/or preparations necessary to run tests (usually controlled by FEATURES=test but can be toggled independently)
  ------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-02-06 14:51] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [[] Emerge]

Install [[[x11-wm/awesome]](https://packages.gentoo.org/packages/x11-wm/awesome)[]]:

`root `[`#`]`emerge --ask x11-wm/awesome`

## [[] Configuration]

### [[] Starting]

To start **awesome**, refer to [Starting the X server](https://wiki.gentoo.org/wiki/Awesome#Starting_the_X_server "Awesome") or use the command [startx].

To use [startx] with [elogind](https://wiki.gentoo.org/wiki/Elogind "Elogind") support, setup [elogind](https://wiki.gentoo.org/wiki/Elogind "Elogind") and create the following file:

[FILE] **`~/.xinitrc`**

    exec dbus-launch --sh-syntax --exit-with-session awesome

### [[] Configuration file]

The default configuration file of awesome is located in [\~/.config/awesome/rc.lua]. If such a directory or file does not exist then it needs to be created. A default, out of the box, configuration is distributed with [awesome] and can be found at [/etc/xdg/awesome/rc.lua]. Copy that configuration file to the user\'s home directory.

First create the [awesome/] directory:

`user `[`$`]`mkdir -p ~/.config/awesome/`

Next copy the [rc.lua] configuration file:

`user `[`$`]`cp /etc/xdg/awesome/rc.lua ~/.config/awesome/rc.lua`

If [[[x11-terms/xterm]](https://packages.gentoo.org/packages/x11-terms/xterm)[]] is not installed, either install it or change the default terminal emulator to the terminal emulator available on the system. Below, the default terminal emulator is set to [konsole], part of [[[kde-apps/konsole]](https://packages.gentoo.org/packages/kde-apps/konsole)[]].

[FILE] **`~/.config/awesome/rc.lua`**

    -- This is used later as the default terminal and editor to run.
    terminal = "konsole"

After making changes it is useful to check the configuration file for errors:

`user `[`$`]`awesome -k`

    ✔ Configuration file syntax OK

Add wallpaper support through the [[[media-gfx/feh]](https://packages.gentoo.org/packages/media-gfx/feh)[]] package:

`root `[`#`]`emerge --ask media-gfx/feh`

For instance, to set the wallpaper, edit [\~/.config/awesome/theme/theme.lua]:

[FILE] **`~/.config/awesome/theme/theme.lua`Setting a specific background using the wallpaper property**

    theme.wallpaper = ".config/awesome/themes/awesome-wallpaper.png"

### [[] Tags]

In [awesome], tags are the name given to virtual desktops under which one or more applications are running. It is possible to assign custom symbols to these tags:

[FILE] **`~/.config/awesome/rc.lua`**

    --
    for s = 1, screen.count() do
        tags[s] = awful.tag(, s, layouts[1])
    end
    -- }}}

### [[] Menu]

Below is an example of a custom [awesome] menu:

[FILE] **`~/.config/awesome/rc.lua`**

    -- ,
       ,
       ,
       ,
       ,

    }

    appsmenu = ,
       ,
       ,
       ,
       ,
       ,
       ,
       ,
       ,
       ,
       ,
       ,

    }

    gamesmenu = ,
       ,
       ,
       ,
       ,
       ,
       ,
       ,
       ,
       ,
       ,
       ,

    }

    mymainmenu = awful.menu(,
                                        ,
                        ,
                                        ,
                        ,

                                      }
                            })

    mylauncher = awful.widget.launcher()
    -- }}}

### [[] Date]

Below is an example use of a custom date format. The format syntax used is `%Y-%m-%d %H:%M`. The second option, `60`, is the update interval in seconds.

[FILE] **`~/.config/awesome/rc.lua`Creating a text-clock widget**

    -- }}

** Note**\
For more information about the format options run [date \--help]

### [[] Volume control]

[[[media-sound/volumeicon]](https://packages.gentoo.org/packages/media-sound/volumeicon)[]] can be used to handle volume keys automatically, and to show the volume level through a tray icon.

`root `[`#`]`emerge --ask media-sound/volumeicon`

Autostart [volumeicon] from within [\~/.xinitrc]:

[FILE] **`~/.xinitrc`Launching volumeicon in the background when starting X**

    volumeicon &
    exec [...]

Alternatively, a lightweight method is to add volume keys straight into the [awesome] configuration:

[FILE] **`~/.config/awesome/rc.lua`Volume keys**

    awful.key(, "XF86AudioLowerVolume", function () awful.util.spawn("amixer -q sset Master 5%-") end)
    awful.key(, "XF86AudioRaiseVolume", function () awful.util.spawn("amixer -q sset Master 5%+") end)

### [[] MPD multimedia keys]

Install [[[media-sound/mpc]](https://packages.gentoo.org/packages/media-sound/mpc)[]] to add multimedia key bindings for [MPD](https://wiki.gentoo.org/wiki/MPD "MPD"):

`root `[`#`]`emerge --ask media-sound/mpc`

Next update the [awesome] configuration to assign the multimedia keys to the proper command:

[FILE] **`~/.config/awesome/rc.lua`Volume key bindings**

    awful.key(, "XF86AudioNext",function () awful.util.spawn( "mpc next" ) end),
    awful.key(, "XF86AudioPrev",function () awful.util.spawn( "mpc prev" ) end),
    awful.key(, "XF86AudioPlay",function () awful.util.spawn( "mpc play" ) end),
    awful.key(, "XF86AudioStop",function () awful.util.spawn( "mpc pause" ) end),

### [[] Removing window gaps]

Gaps between windows can be visible, most noticeably between terminal windows. These can be removed by inserting the `size_hints_honor = false` property in the `awful.rules.rules` table like this:

[FILE] **`~/.config/awesome/rc.lua`Setting size_hints_honor property**

    awful.rules.rules = ,
          properties = [`$`]`Xephyr -ac -nolisten tcp -br -noreset -screen 800x600 :1`

This will open an 800x600 window. To run awesome within it open a new terminal and run the following:

`user `[`$`]`DISPLAY=:1.0 awesome`

This will run awesome within a window.

## [[] Keyboard shortcuts]

These are the most useful default shortcuts:

-   [Super]+[Mouse1] = move client with mouse
-   [Super]+[Mouse2] = resize client with mouse

<!-- -->

-   [Super]+[Enter] = open terminal
-   [Super]+[r] = run command
-   [Super]+[Shift]+[c] = kill
-   [Super]+[m] = maximize
-   [Super]+[n] = minimize
-   [Super]+[Ctrl]+[n] = restore minimized clients
-   [Super]+[f] = full screen
-   [Super]+[Tab] = switch to previous client
-   [Super]+[Ctrl]+[Space] = float

<!-- -->

-   [Super]+[j] = highlight left client
-   [Super]+[k] = highlight right client
-   [Super]+[Shift]+[j] = move client right
-   [Super]+[Shift]+[k] = move client left

<!-- -->

-   [Super]+[l] = resize tiled client
-   [Super]+[h] = resize tiled client

<!-- -->

-   [Super]+[left / right] = change tag
-   [Super]+[1-9] = change tag
-   [Super]+[Shift]+[1-9] = send client to tag

Custom key bindings, like [Alt]+[Tab], can be mapped to make the [awesome] experience even better. For instance, to use [Alt]+[Tab] to switch to the previous window:

[FILE] **`~/.config/awesome/rc.lua`Alt-TAB key binding**

    -- , "Tab",
            function ()
                awful.client.focus.history.previous()
                if client.focus then
                    client.focus:raise()
                end
            end),
    -- }}}

## [[] External resources]

-   [User Configuration Files](https://web.archive.org/web/20160701200046/https://awesome.naquadah.org/wiki/Main_Page#User_configuration_files) at awesome wiki (web.archive.org)
-   [Desktop profile switching USE default to elogind](https://gentoo.org/support/news-items/2020-04-14-elogind-default.html)