**Resources**

[[]][Home](https://kdeconnect.kde.org/)

[[]][Package information](https://packages.gentoo.org/packages/kde-misc/kdeconnect)

[[]][GitWeb](https://gitweb.gentoo.org/proj/https://invent.kde.org/network/kdeconnect-kde)

**KDEConnect** is an application that lets two devices shares clipboard, files, and other information. It is similar to Apple\'s AirDrop in functionality. It is mainly used between a phone and a computer to easily share files and notifications.

A KDEConnect implementation for Gnome can be found at [[[gnome-extra/gnome-shell-extension-gsconnect]](https://packages.gentoo.org/packages/gnome-extra/gnome-shell-extension-gsconnect)[]].

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
    -   [[1.3] [Additional software]](#Additional_software)
-   [[2] [Troubleshooting]](#Troubleshooting)
    -   [[2.1] [Use KDEConnect with a firewall]](#Use_KDEConnect_with_a_firewall)
-   [[3] [Removal]](#Removal)
    -   [[3.1] [Unmerge]](#Unmerge)
-   [[4] [See also]](#See_also)
-   [[5] [External resources]](#External_resources)

## [Installation]

### [USE flags]

### [USE flags for] [kde-misc/kdeconnect](https://packages.gentoo.org/packages/kde-misc/kdeconnect) [[]] [Adds communication between KDE Plasma and your smartphone]

  ----------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [`X`](https://packages.gentoo.org/useflags/X)                     Enable remote input mousepad plugin using x11-libs/libfakekey
  [`bluetooth`](https://packages.gentoo.org/useflags/bluetooth)     Enable Bluetooth Support
  [`debug`](https://packages.gentoo.org/useflags/debug)             Enable extra debug codepaths, like asserts and extra output. If you want to get meaningful backtraces see https://wiki.gentoo.org/wiki/Project:Quality_Assurance/Backtraces
  [`pulseaudio`](https://packages.gentoo.org/useflags/pulseaudio)   Enable system volume control plugin using media-libs/libpulse
  [`selinux`](https://packages.gentoo.org/useflags/selinux)         !!internal use only!! Security Enhanced Linux support, this must be set by the selinux profile or breakage will occur
  [`telephony`](https://packages.gentoo.org/useflags/telephony)     Enable telephony plugin using kde-frameworks/modemmanager-qt
  [`test`](https://packages.gentoo.org/useflags/test)               Enable dependencies and/or preparations necessary to run tests (usually controlled by FEATURES=test but can be toggled independently)
  [`zeroconf`](https://packages.gentoo.org/useflags/zeroconf)       Support for DNS Service Discovery (DNS-SD)
  ----------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-05-08 20:34] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

`root `[`#`]`emerge --ask kde-misc/kdeconnect`

### [Additional software]

To use this application, KDEConnect needs to be installed on the two devices which will communicate.

## [Troubleshooting]

### [Use KDEConnect with a firewall]

If your computer has a firewall (like [[[net-firewall/nftables]](https://packages.gentoo.org/packages/net-firewall/nftables)[]]), then the ports 1714-1764 needs to be open. For [Nftables](https://wiki.gentoo.org/wiki/Nftables "Nftables"), the following snippet can be used.

[FILE] **`/etc/nftables.rules.d/kdeconnect.rules`Allow TCP and UDP for KDEConnect**

    #! /sbin/nft -f
    table inet filter
    }

## [Removal]

### [Unmerge]

`root `[`#`]`emerge --ask --depclean --verbose kde-misc/kdeconnect`

## [See also]

-   [KDE](https://wiki.gentoo.org/wiki/KDE "KDE") --- a free software community, producing a wide range of applications including the popular Plasma desktop environment.

## [External resources]

-   [KDEConnect\'s userbase](https://userbase.kde.org/KDEConnect)