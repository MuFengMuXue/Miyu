**Resources**

[[]][Home](http://www.openntpd.org/)

[[]][OpenNTPD](https://en.wikipedia.org/wiki/OpenNTPD "wikipedia:OpenNTPD")

[![Ohloh Logo](/images/thumb/c/c1/Ohloh-logo.png/30px-Ohloh-logo.png)][Open Hub](https://www.openhub.net/p/ntpd)

OpenNTPD is a lightweight [NTP](https://wiki.gentoo.org/wiki/Network_Time_Protocol "Network Time Protocol") server ported from OpenBSD.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
    -   [[1.3] [Service]](#Service)
        -   [[1.3.1] [OpenRC]](#OpenRC)
        -   [[1.3.2] [systemd]](#systemd)
-   [[2] [Configuration]](#Configuration)
    -   [[2.1] [Server]](#Server)
    -   [[2.2] [Client]](#Client)
-   [[3] [Checking the daemon operation]](#Checking_the_daemon_operation)
-   [[4] [See also]](#See_also)

## [Installation]

### [USE flags]

### [USE flags for] [net-misc/openntpd](https://packages.gentoo.org/packages/net-misc/openntpd) [[]] [Lightweight NTP server ported from OpenBSD]

  ------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------
  [`constraints`](https://packages.gentoo.org/useflags/constraints)   Enable HTTPS TLS time constraint support
  [`selinux`](https://packages.gentoo.org/useflags/selinux)           !!internal use only!! Security Enhanced Linux support, this must be set by the selinux profile or breakage will occur
  ------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2025-09-02 17:00] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

Install OpenNTPD:

`root `[`#`]`emerge --ask net-misc/openntpd`

### [Service]

To ask OpenNTPD to attempt clock sync on startup, edit [/etc/conf.d/ntpd]:

[FILE] **`/etc/conf.d/ntpd`Gentoo OpenNTPD configuration file**

    # See ntpd(8) man page ... some popular options:
    #  -s   Set the time immediately at startup
    #       (Note: may cause up to a 15 second startup delay
    #        if ntp servers not reachable)
    NTPD_OPTS="-s"

Note that if the clock drift is sufficiently large, you may first need to set the time manually using [date(1)].

#### [OpenRC]

Start the ntp daemon:

`root `[`#`]`/etc/init.d/ntpd start`

Add the ntp daemon to the default runlevel:

`root `[`#`]`rc-update add ntpd default`

#### [systemd]

To enable and start the service now:

`root `[`#`]`systemctl enable --now ntpd`

## [Configuration]

The default configuration file for OpenNTPD:

[FILE] **`/etc/ntpd.conf`Gentoo\'s default configuration**

    # Addresses to listen on (ntpd does not listen by default)
    #listen on *

    # sync to a single server
    #server ntp.example.org

    # use a random selection of NTP Pool Time Servers
    # see http://support.ntp.org/bin/view/Servers/NTPPoolServers
    #servers pool.ntp.org

    # use a specific local timedelta sensor (radio clock, etc)
    #sensor nmea0

    # use all detected timedelta sensors
    #sensor *

    # get the time constraint from a well-known HTTPS site
    #constraints from "https://www.google.com/search?q=openntpd"

    # Choose servers announced from Gentoo NTP Pool
    servers 0.gentoo.pool.ntp.org
    servers 1.gentoo.pool.ntp.org
    servers 2.gentoo.pool.ntp.org
    servers 3.gentoo.pool.ntp.org

For further information see the man page:

`user `[`$`]`man ntpd.conf`

### [Server]

[FILE] **`/etc/ntpd.conf`OpenNTPD listening on 192.0.2.1 address while syncing with multiple servers**

    # Addresses to listen on (ntpd does not listen by default)
    listen on 192.0.2.1

    # Choose servers announced from Gentoo NTP Pool
    servers 0.gentoo.pool.ntp.org
    servers 1.gentoo.pool.ntp.org
    servers 2.gentoo.pool.ntp.org
    servers 3.gentoo.pool.ntp.org

`root `[`#`]`rc-service ntpd restart`

### [Client]

[FILE] **`/etc/ntpd.conf`OpenNTPD syncing with multiple servers**

    # Choose servers announced from Gentoo NTP Pool
    servers 0.gentoo.pool.ntp.org
    servers 1.gentoo.pool.ntp.org
    servers 2.gentoo.pool.ntp.org
    servers 3.gentoo.pool.ntp.org

Alternatively sync the client to a server on the local network:

[FILE] **`/etc/ntpd.conf`OpenNTPD syncing with a single server on the local network**

    # sync to a single server on the local network
    server 192.0.2.1

`root `[`#`]`rc-service ntpd restart`

## [Checking the daemon operation]

[[[net-misc/openntpd]](https://packages.gentoo.org/packages/net-misc/openntpd)[]] provides the [/usr/sbin/ntpctl] program to display information about the running [ntpd] daemon:

`root `[`#`]`ntpctl -s all`

    4/4 peers valid, clock unsynced, clock offset is 1048.342ms

    peer
       wt tl st  next  poll          offset       delay      jitter
    185.19.184.35 0.gentoo.pool.ntp.org
        1 10  2   23s   34s        41.650ms   190.744ms   227.001ms
    31.14.131.188 1.gentoo.pool.ntp.org
        1 10  2    2s   31s        15.834ms   132.072ms    92.419ms
    212.45.144.3 2.gentoo.pool.ntp.org
        1 10  1    8s   33s        42.733ms   216.937ms   212.899ms
    188.213.165.209 3.gentoo.pool.ntp.org
        1 10  2   19s   30s        45.672ms   228.337ms   240.018ms

The output shows how many servers the daemon is syncing with, the status of the system clock (synced/unsynced) and the clock offset. For further information see the man page:

`user `[`$`]`man ntpctl`

## [See also]

-   [Chrony](https://wiki.gentoo.org/wiki/Chrony "Chrony") --- a versatile implementation of the [Network Time Protocol](https://wiki.gentoo.org/wiki/Network_Time_Protocol "Network Time Protocol") (NTP).
-   [Network Time Protocol](https://wiki.gentoo.org/wiki/Network_Time_Protocol "Network Time Protocol") --- used to synchronize the [system time](https://wiki.gentoo.org/wiki/System_time "System time") with other devices over the network.
-   [System time](https://wiki.gentoo.org/wiki/System_time "System time") --- is used in Unix systems to keep track of time.
-   [Home router](https://wiki.gentoo.org/wiki/Home_router "Home router") --- how to turn an old Gentoo machine into a router for connecting a home network to the Internet.