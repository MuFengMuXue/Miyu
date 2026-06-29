**Resources**

[[]][Home](https://www.lesbonscomptes.com/upmpdcli/)

[[]][Official documentation](https://www.lesbonscomptes.com/upmpdcli/upmpdcli-manual.html)

**upmpdcli** is a free and open source UPnP media renderer front-end for Music Player Daemon (MPD). It allows MPD to be controlled with a UPnP control point (e.g. [BubbleUPnP](https://forum.xda-developers.com/showthread.php?t=1118891)). upmpdcli also allows a single UPnP library to be shared between UPnP control points/renderers and MPD, meaning MPD can be run without a database.

## Contents

-   [[1] [Prerequisites]](#Prerequisites)
-   [[2] [Installation]](#Installation)
    -   [[2.1] [USE Flags]](#USE_Flags)
    -   [[2.2] [Emerge]](#Emerge)
-   [[3] [Configuration]](#Configuration)
    -   [[3.1] [Service]](#Service)
        -   [[3.1.1] [OpenRC]](#OpenRC)
        -   [[3.1.2] [systemd]](#systemd)
-   [[4] [See also]](#See_also)
-   [[5] [External resources]](#External_resources)

## [Prerequisites]

This article assumes that [MPD](https://wiki.gentoo.org/wiki/MPD "MPD") and a UPnP media server such as [Gerbera](https://wiki.gentoo.org/wiki/Gerbera "Gerbera") have been previously configured.

## [Installation]

### [USE Flags]

### [USE flags for] [media-sound/upmpdcli](https://packages.gentoo.org/packages/media-sound/upmpdcli) [[]] [UPnP Media Renderer front-end for MPD, the Music Player Daemon]

  ----------------------------------------------------------------- ---------------------------------------------------------
  [`thirdparty`](https://packages.gentoo.org/useflags/thirdparty)   Enable streaming from Qobuz and Tidal external services
  ----------------------------------------------------------------- ---------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-04-16 13:02] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

`root `[`#`]`emerge --ask media-sound/upmpdcli`

## [Configuration]

Below is a snippet of the default upmpdcli configuration file. Options prefixed with `#` are commented out because they are set to default values. The options that need to be set are `upnpiface` or `upnpip` and `mpdhost`. If the UPnP or MPD ports have been changed from their defaults, then `upnpport` and `mpdport` should be set accordingly.

[FILE] **`/etc/upmpdcli.conf`**

    # upmpdcli general parameters
    #logfilename = /var/log/upmpdcli.log
    #loglevel = 2
    #pkgdatadir=/usr/share/upmpdcli
    #pidfile = /var/run/upmpdcli.pid

    # upnp network parameters
    #upnpiface =
    upnpip = 192.168.0.1
    #upnpport =

    # media renderer parameters
    #friendlyname = UpMpd
    #upnpav = 1
    #openhome = 1
    #lumincompat = 0
    #saveohcredentials = 1
    #checkcontentformat = 1
    #iconpath = /usr/share/upmpdcli/icon.png
    #cachedir = /var/cache/upmpdcli
    #presentationhtml = /usr/share/upmpdcli/presentation.html

    # mpd parameters
    mpdhost = 192.168.0.1
    #mpdport = 6600
    #mpdpassword =
    #ownqueue = 1

upmpdcli relies on MPD\'s curl input plugin which should be enabled by default. It can be explicitly enabled by adding the following to the MPD configuration file:

[FILE] **`/etc/mpd.conf`**

    input

Restart MPD for the changes to take effect:

`root `[`#`]`rc-service mpd restart`

### [Service]

#### [OpenRC]

Start upmpdcli:

`root `[`#`]`rc-service upmpdcli start`

Start upmpdcli at boot:

`root `[`#`]`rc-update add upmpdcli default`

#### [systemd]

Start upmpdcli:

`root `[`#`]`systemctl start upmpdcli`

Start upmpdcli at boot:

`root `[`#`]`systemctl enable upmpdcli`

## [See also]

-   [MPD](https://wiki.gentoo.org/wiki/MPD "MPD") --- a flexible, server-side application for playing music.

## [External resources]

-   [upmpdcli](https://www.lesbonscomptes.com/upmpdcli/upmpdcli-or-mpdupnp.html) - MPD and UPnP