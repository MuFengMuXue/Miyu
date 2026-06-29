[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=MiniDLNA&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

**Resources**

[[]][Home](https://sourceforge.net/projects/minidlna/)

**MiniDLNA** (also known as ReadyMedia) is a media server aiming to be DLNA/UPnP-AV compliant.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
-   [[2] [Configuration]](#Configuration)
    -   [[2.1] [Automatic file discovery]](#Automatic_file_discovery)
    -   [[2.2] [Manual database rebuild]](#Manual_database_rebuild)
    -   [[2.3] [Port forwarding]](#Port_forwarding)
    -   [[2.4] [Permissions]](#Permissions)
    -   [[2.5] [Discovery Problems]](#Discovery_Problems)
    -   [[2.6] [Service]](#Service)
        -   [[2.6.1] [OpenRC]](#OpenRC)
        -   [[2.6.2] [systemd]](#systemd)
-   [[3] [See also]](#See_also)

## [Installation]

### [USE flags]

### [USE flags for] [net-misc/minidlna](https://packages.gentoo.org/packages/net-misc/minidlna) [[]] [DLNA/UPnP-AV compliant media server]

  ------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------
  [`branding`](https://packages.gentoo.org/useflags/branding)   Enable Gentoo specific branding
  [`netgear`](https://packages.gentoo.org/useflags/netgear)     Enable netgear branding
  [`readynas`](https://packages.gentoo.org/useflags/readynas)   Enable readynas branding
  [`selinux`](https://packages.gentoo.org/useflags/selinux)     !!internal use only!! Security Enhanced Linux support, this must be set by the selinux profile or breakage will occur
  [`zeroconf`](https://packages.gentoo.org/useflags/zeroconf)   Support for DNS Service Discovery (DNS-SD)
  ------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-05-24 23:34] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

Install [[[net-misc/minidlna]](https://packages.gentoo.org/packages/net-misc/minidlna)[]]:

`root `[`#`]`emerge --ask net-misc/minidlna`

## [Configuration]

Configuration is controlled by [/etc/minidlna.conf] these settings should be changed.

[FILE] **`/etc/minidlna.conf`**

    #friendly_name=My DLNA Server
    media_dir=/opt

### [Automatic file discovery]

MiniDLNA supports [inotify](https://en.wikipedia.org/wiki/Inotify "wikipedia:Inotify") monitoring to automatically discover new files. To enable inotify support the kernel needs to have inotify support enabled.

[KERNEL] **Enabling inotify support**

        File systems --->
          [*] Inotify support for userspace

And `inotify=yes` set in the MiniDLNA configuration file.

[FILE] **`/etc/minidlna.conf`**

    inotify=yes

### [Manual database rebuild]

`root `[`#`]`rc-service minidlna stop && minidlnad -R`

### [Port forwarding]

MiniDLNA uses UDP port 1900 & TCP port 8200.

### [Permissions]

The service runs as user minidlna. Thus directories and files like the database in *db_dir* or the log file in *log_dir* need correct ownership. Owner must be minidlna.

### [Discovery Problems]

-   do not use spaces for *friendly_name*

### [Service]

#### [OpenRC]

Start MiniDLNA:

`root `[`#`]`rc-service minidlna start`

Start MiniDLNA at boot:

`root `[`#`]`rc-update add minidlna default`

#### [systemd]

Start MiniDLNA:

`root `[`#`]`systemctl start minidlna`

Start MiniDLNA at boot:

`root `[`#`]`systemctl enable minidlna`

## [See also]

-   [Gerbera](https://wiki.gentoo.org/wiki/Gerbera "Gerbera") --- an open source [UPnP](https://en.wikipedia.org/wiki/Universal_Plug_and_Play "wikipedia:Universal Plug and Play") media server that streams digital media through a home network to UPnP compatible devices.