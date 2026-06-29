This page contains [[changes](https://wiki.gentoo.org/index.php?title=Dunst&diff=1317675)] which are not marked for translation.

**Resources**

[[]][Home](https://dunst-project.org/)

[[]][GitHub](https://github.com/dunst-project/dunst)

[[]][Package information](https://packages.gentoo.org/packages/x11-misc/dunst)

[[]][[#dunst](ircs://irc.libera.chat/#dunst)] ([[webchat](https://web.libera.chat/#dunst)])

\
**dunst** is a lightweight replacement for the notification daemons provided by most desktop environments. It is very customizable and does not depend on any toolkits.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [Review the USE flags]](#Review_the_USE_flags)
    -   [[1.2] [Emerge dunst]](#Emerge_dunst)
    -   [[1.3] [Unmerge other notification daemons]](#Unmerge_other_notification_daemons)
    -   [[1.4] [Start dunst]](#Start_dunst)
        -   [[1.4.1] [Start with Sway]](#Start_with_Sway)
        -   [[1.4.2] [Start with Hyprland]](#Start_with_Hyprland)
-   [[2] [Configuration]](#Configuration)
-   [[3] [Usage]](#Usage)
-   [[4] [References]](#References)

## [Installation]

### [Review the USE flags]

### [USE flags for] [x11-misc/dunst](https://packages.gentoo.org/packages/x11-misc/dunst) [[]] [Lightweight replacement for common notification daemons]

  --------------------------------------------------------------------- ----------------------------------------------------
  [`+X`](https://packages.gentoo.org/useflags/+X)                       Add support for X11
  [`+completions`](https://packages.gentoo.org/useflags/+completions)   Install shell completions (for bash, fish and zsh)
  [`+dunstify`](https://packages.gentoo.org/useflags/+dunstify)         Build dunstify (notify-send alternative)
  [`+xdg`](https://packages.gentoo.org/useflags/+xdg)                   Install xdg-utils for opening links with xdg-open
  [`wayland`](https://packages.gentoo.org/useflags/wayland)             Enable dev-libs/wayland backend
  --------------------------------------------------------------------- ----------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-04-02 19:36] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge dunst]

`root `[`#`]`emerge --ask --verbose x11-misc/dunst`

### [Unmerge other notification daemons]

In order to avoid confusion other notification daemons could be removed, e.g. [[[x11-misc/notification-daemon]](https://packages.gentoo.org/packages/x11-misc/notification-daemon)[]]:

`root `[`#`]`emerge --ask --verbose --depclean x11-misc/notification-daemon`

### [Start dunst]

[D-Bus](https://wiki.gentoo.org/wiki/D-Bus "D-Bus") should start a notification daemon automatically, but if multiple are installed then it may just pick one. Starting [dunst] before any other notification daemons are fired up will make sure that [dunst] will handle your notifications. Review the used desktop setup on how to auto-start programs.

** Note**\
Dunst requires that `DISPLAY` or `WAYLAND_DISPLAY` is set to start.

#### [Start with Sway]

[FILE] **`~/.config/sway/config`Start Dunst with Sway**

    exec dunst &

#### [Start with Hyprland]

[FILE] **`~/.config/hypr/hyprland.conf`Start Dunst with Hyprland**

    exec-once = dunst &

## [Configuration]

After the installation there is a working configuration file [/etc/xdg/dunst/dunstrc]. Edit this file to customize the settings for all users, or copy it to [\$XDG_CONFIG_HOME/dunst/dunstrc] for setting for a single user.

`user `[`$`]`cp -r /etc/xdg/dunst ~/.config/dunst`

## [Usage]

Test dunst by creating a notification with the [dunstify] command:

`user `[`$`]`dunstify "Title" "Content"`

Dunst provides a client called [dunstctl]^[\[1\]](#cite_note-1)^. The [dunstctl] client supports passing commands to the running daemon.

`user `[`$`]`dunstctl --help`

    Commands:
      action                            Perform the default action, or open the
                                        context menu of the notification at the
                                        given position
      close                             Close the last notification
      close-all                         Close the all notifications
      context                           Open context menu
      count [displayed|history|waiting] Show the number of notifications
      history                           Display notification history (in JSON)
      history-pop [ID]                  Pop the latest notification from
                                        history or optionally the
                                        notification with given ID.
      is-paused                         Check if dunst is running or paused
      set-paused [true|false|toggle]    Set the pause status
      rule name [enable|disable|toggle] Enable or disable a rule by its name
      debug                             Print debugging information
      help                              Show this help

All currently displayed notification can be cleared as:

`user `[`$`]`dunstctl close-all`

After modifying the configuration file use the [killall dunst] command, to apply new configuration:

`user `[`$`]`killall dunst`

## [References]

1.  [[[↑](#cite_ref-1)] [[Release v1.5.0 · dunst-project/dunst](https://github.com/dunst-project/dunst/releases/tag/v1.5.0), GitHub. Retrieved on March 10, 2022]]