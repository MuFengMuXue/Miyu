**Resources**

[[]][Home](https://github.com/emersion/mako)

[[]][Package information](https://packages.gentoo.org/packages/gui-apps/mako)

**Mako** is a lightweight replacement for the notification daemons provided by most desktop environments. It implements the [FreeDesktop Notifications Specification](https://specifications.freedesktop.org/notification-spec/latest/).

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
    -   [[1.3] [Configuration]](#Configuration)
    -   [[1.4] [Usage]](#Usage)
-   [[2] [See also]](#See_also)

## [Installation]

### [USE flags]

### [USE flags for] [gui-apps/mako](https://packages.gentoo.org/packages/gui-apps/mako) [[]] [A lightweight notification daemon for Wayland. Works on Sway]

  ----------------------------------------------------------------- --------------------------------------------------------------------------------------------------
  [`+icons`](https://packages.gentoo.org/useflags/+icons)           Enable support for icons
  [`elogind`](https://packages.gentoo.org/useflags/elogind)         Enable session tracking via sys-auth/elogind
  [`systemd`](https://packages.gentoo.org/useflags/systemd)         Enable use of systemd-specific libraries and features like socket activation or session tracking
  [`verify-sig`](https://packages.gentoo.org/useflags/verify-sig)   Verify upstream signatures on distfiles
  ----------------------------------------------------------------- --------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-05-04 18:19] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

`root `[`#`]`emerge --ask gui-apps/mako`

### [Configuration]

Mako is highly configurable; refer to the [[[mako(5)]](https://man.archlinux.org/man/mako.5.en)[[]](https://wiki.gentoo.org/wiki/Special:MyLanguage/man_page "Special:MyLanguage/man page")] man page for details about the configuration file.

For example, to configure Mako to use [[[gui-apps/wofi]](https://packages.gentoo.org/packages/gui-apps/wofi)[]] to present a list of options when the notification requires a user response, and the user right-clicks on the notification:

[FILE] **`~/.config/mako/config`**

    [actionable=true]
    on-button-right=exec makoctl menu -n "$" wofi_run.sh dmenu

where `$` is the shell variable `id`, which will contain the ID of the notification, and [wofi_run.sh] is a simple shell script, e.g.:

[FILE] **`wofi_run.sh`**

    #!/bin/sh

    wofi --width=400 --height=260 --hide-scroll --show="$"

To get notification content, such as the subject or message, use [[[makoctl(1)]](https://man.archlinux.org/man/makoctl.1.en)[[]](https://wiki.gentoo.org/wiki/Special:MyLanguage/man_page "Special:MyLanguage/man page")] and [[[jq(1)]](https://man.archlinux.org/man/jq.1.en)[[]](https://wiki.gentoo.org/wiki/Special:MyLanguage/man_page "Special:MyLanguage/man page")]. For example, to send the message body to a webhook service like ntfy.sh:

[FILE] **`~/.config/mako/config`**

    on-notify=exec curl -d "$(makoctl list | jq -r '.data|..|select(.id?.data=='$id')|.body|.data')" https://ntfy.sh/examplewebhook

To configure Mako to present notification messages with urgency \'critical\' in the center of the screen with a red background:

[FILE] **`~/.config/mako/config`**

    [urgency="critical"]
    anchor=center
    background-color=#ff0000ff

To configure Mako to handle notifications from a specific application in a specific way:

[FILE] **`~/.config/mako/config`**

    [app-name="Firefox"]
    default-timeout=10000

### [Usage]

Mako will run automatically when a notification is emitted via D-Bus activation, so in most cases there is no need to explicitly start it up. A [running session bus](https://wiki.gentoo.org/wiki/D-Bus#The_session_bus "D-Bus") is needed in order to use Mako.

Mako can be started from your GUI\'s startup file, e.g. [\~/.config/sway/config]:

[FILE] **`~/.config/sway/config`**

    exec mako

Mako can be controlled from the command line via [makoctl(1)](https://manpages.debian.org/bookworm/mako-notifier/makoctl.1.en.html). For example, to reload the configuration file:

`user `[`$`]`makoctl reload`

To show again the most recent expired notification:

`user `[`$`]`makoctl restore`

To view the history of expired notificactions:

`user `[`$`]`makoctl history`

** Note**\
Installing Mako puts a D-Bus service file, [fr.emersion.mako.service], in [/usr/share/dbus-1/services]. This can result in Mako being used for notifications, instead of other notification services. If using Plasma, and the KDE notification service is preferred, create a symbolic link to [/usr/share/dbus-1/services/org.kde.plasma.Notifications.service] in [\~/.local/share/dbus-1/services], to ensure use of the KDE notification service.

## [See also]

-   [dunst](https://wiki.gentoo.org/wiki/Dunst "Dunst") - a lightweight replacement for the notification daemons provided by most desktop environments, usable under both X and Wayland.