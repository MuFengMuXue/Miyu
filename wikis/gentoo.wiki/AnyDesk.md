[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=AnyDesk&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

**Resources**

[[]][Home](https://anydesk.com/)

[[]][Wikipedia](https://en.wikipedia.org/wiki/AnyDesk "wikipedia:AnyDesk")

**AnyDesk** is a proprietary (closed source), software for remote access and support over the Internet similar to [TeamViewer](https://wiki.gentoo.org/wiki/TeamViewer "TeamViewer").

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
    -   [[1.3] [Service]](#Service)
        -   [[1.3.1] [OpenRC]](#OpenRC)
        -   [[1.3.2] [systemd]](#systemd)
-   [[2] [Troubleshooting]](#Troubleshooting)
-   [[3] [See also]](#See_also)

## [Installation]

### [USE flags]

### [USE flags for] [net-misc/anydesk](https://packages.gentoo.org/packages/net-misc/anydesk) [[]] [Feature rich multi-platform remote desktop application]

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-02-15 11:52] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

Accept AnyDesk TOS license.

[FILE] **`/etc/portage/package.license`**

    net-misc/anydesk AnyDesk-TOS

`root `[`#`]`emerge --ask net-misc/anydesk`

### [Service]

AnyDesk service can be run manually with

`user `[`$`]`anydesk --service`

AnyDesk service can also be turned on so that it runs every time the system boots.

#### [OpenRC]

Start AnyDesk during system start:

`root `[`#`]`rc-update add anydesk default`

Start the AnyDesk daemon now:

`root `[`#`]`rc-service anydesk start`

#### [systemd]

Start AnyDesk during system start:

`root `[`#`]`systemctl enable anydesk`

Start the AnyDesk daemon now:

`root `[`#`]`systemctl start anydesk`

## [Troubleshooting]

If [PulseAudio](https://wiki.gentoo.org/wiki/PulseAudio "PulseAudio") is not used, AnyDesk may not be able to receive connection. In case it is undesirable to install [PulseAudio](https://wiki.gentoo.org/wiki/PulseAudio "PulseAudio"), AnyDesk can be run with PULSE_SERVER=0 environment variable:

`user `[`$`]`PULSE_SERVER=0 anydesk --service`

systemd users can add this into the AnyDesk service

`root `[`#`]`systemctl edit anydesk`

[FILE] **`/etc/systemd/system/anydesk.service.d/override.conf`**

    ### Editing /etc/systemd/system/anydesk.service.d/override.conf
    ### Anything between here and the comment below will become the contents of the drop-in file

    [Service]
    Type=simple
    Environment=PULSE_SERVER=0

    ### Edits below this comment will be discarded

    ### /usr/lib/systemd/system/anydesk.service
    # [Unit]
    # Description=AnyDesk
    # Requires=network.target
    # After=systemd-user-sessions.service
    #
    # [Service]
    # Type=simple
    # ExecStart=/opt/bin/anydesk --service
    # PIDFile=/run/anydesk.pid
    # KillMode=mixed
    # TimeoutStopSec=30
    # User=root
    # LimitNOFILE=100000
    #
    # [Install]
    # WantedBy=multi-user.target

openrc users can export this from the conf.d/anydesk file:

[FILE] **`/etc/conf.d/anydesk`**

    export PULSE_SERVER=0

## [See also]

-   [TigerVNC](https://wiki.gentoo.org/wiki/TigerVNC "TigerVNC") --- a client/server software package allowing remote network access to graphical desktops.
-   [TeamViewer](https://wiki.gentoo.org/wiki/TeamViewer "TeamViewer") --- a proprietary (closed source), all-in-one solution for remote access and support over the Internet.