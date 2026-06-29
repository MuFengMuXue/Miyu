[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=Spotify&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

**Resources**

[[]][Home](https://spotify.com/download/linux/)

[[]][Package information](https://packages.gentoo.org/packages/media-sound/spotify)

[[]][Wikipedia](https://en.wikipedia.org/wiki/Spotify "wikipedia:Spotify")

Spotify is a digital music streaming service that provides a proprietary Linux client.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
-   [[2] [Control via MPRIS]](#Control_via_MPRIS)
    -   [[2.1] [Prequisites if using a window manager]](#Prequisites_if_using_a_window_manager)
    -   [[2.2] [With dbus-send]](#With_dbus-send)
    -   [[2.3] [With playerctl]](#With_playerctl)
-   [[3] [Starting with Wayland]](#Starting_with_Wayland)
-   [[4] [External Resources]](#External_Resources)

## [Installation]

### [USE flags]

### [USE flags for] [media-sound/spotify](https://packages.gentoo.org/packages/media-sound/spotify) [[]] [Spotify is a social music platform]

  ------------------------------------------------------------------------- ----------------------------------------------------
  [`libnotify`](https://packages.gentoo.org/useflags/libnotify)             Enable desktop notification support
  [`local-playback`](https://packages.gentoo.org/useflags/local-playback)   Allows playing local files with the Spotify client
  [`pax-kernel`](https://packages.gentoo.org/useflags/pax-kernel)           Triggers a paxmarking of the main Spotify binary
  [`pulseaudio`](https://packages.gentoo.org/useflags/pulseaudio)           Controls the dependency on pulseaudio or apulse
  ------------------------------------------------------------------------- ----------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-04-27 03:22] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

Install Spotify:

`root `[`#`]`emerge --ask media-sound/spotify`

** Note**\
Please ensure that [[[net-misc/curl]](https://packages.gentoo.org/packages/net-misc/curl)[]] is built with the bfd linker (default) instead of the [gold](https://wiki.gentoo.org/wiki/Gold "Gold") linker. See [[[bug #651770]](https://bugs.gentoo.org/show_bug.cgi?id=651770)[]] for more information.

## [Control via MPRIS]

[MPRIS](https://specifications.freedesktop.org/mpris-spec/latest/)is a [D-Bus](https://wiki.gentoo.org/wiki/D-Bus "D-Bus") interface which provides a common API to control media players.

Spotify supports MPRIS.

### [Prequisites if using a window manager]

In [\$HOME/.xinitrc], make the window manager start with [dbus-run-session].

Otherwise, Spotify won\'t provide an MPRIS interface.

[FILE] **`$HOME/.xinitrc`Starting bspwm with D-Bus**

    exec dbus-run-session bspwm

### [With dbus-send]

The most simple approach to controlling Spotify is using [dbus-send].

**Play/pause**:

`user `[`$`]`dbus-send --print-reply --dest=org.mpris.MediaPlayer2.spotify /org/mpris/MediaPlayer2 org.mpris.MediaPlayer2.Player.PlayPause`

**Next**:

`user `[`$`]`dbus-send --print-reply --dest=org.mpris.MediaPlayer2.spotify /org/mpris/MediaPlayer2 org.mpris.MediaPlayer2.Player.Next`

**Previous**:

`user `[`$`]`dbus-send --print-reply --dest=org.mpris.MediaPlayer2.spotify /org/mpris/MediaPlayer2 org.mpris.MediaPlayer2.Player.Previous`

### [With playerctl]

Install [[[media-sound/playerctl]](https://packages.gentoo.org/packages/media-sound/playerctl)[]].

**Play/pause**:

`user `[`$`]`playerctl play-pause`

**Next**:

`user `[`$`]`playerctl next`

**Previous**:

`user `[`$`]`playerctl previous`

More info about [playerctl] can be found on its [GitHub page](https://github.com/altdesktop/playerctl).

## [Starting with Wayland]

Spotify uses Xorg by default. In order to make Spotify start with Wayland, you can add

    --enable-features=UseOzonePlatform --ozone-platform=wayland

to Spotify\'s .desktop file in [/usr/share/applications/spotify.desktop] on the

    Exec=spotify

line. It should look like this:

[FILE] **`/usr/share/applications/spotify.desktop`Starting Spotify with Wayland**

    Exec=spotify --enable-features=UseOzonePlatform --ozone-platform=wayland %U

You can also add these options to anything that launches Spotify through the command line.

## [External Resources]

-   [Arch Linux Wiki - Spotify](https://wiki.archlinux.org/title/spotify)