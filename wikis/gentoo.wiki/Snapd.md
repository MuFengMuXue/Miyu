**Resources**

[[]][Home](https://snapcraft.io/)

[[]][Package information](https://packages.gentoo.org/packages/app-containers/snapd)

[[]][Wikipedia](https://en.wikipedia.org/wiki/Snap_(software) "wikipedia:Snap (software)")

[[]][Official documentation](https://snapcraft.io/docs)

[[]][GitWeb](https://github.com/snapcore/snapd)

**[Snap](https://snapcraft.io/)** is a software management and deployment system that enables distribution-independent software deployment. The packages are called \'snaps\' and one tool for using them is \'[snapd](https://packages.gentoo.org/packages/app-containers/snapd)\'. Canonical, the developer of Snap, manages the [Snap Store](https://snapcraft.io/store) service through which snaps are deployed. snapd is a REST API daemon for managing snap packages. Users can interact with it using the snap client, which is part of the same package.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
-   [[2] [Basic usage]](#Basic_usage)
-   [[3] [Systemd Users]](#Systemd_Users)
-   [[4] [Graphical management]](#Graphical_management)
-   [[5] [Troubleshooting]](#Troubleshooting)
-   [[6] [Support]](#Support)
-   [[7] [See also]](#See_also)
-   [[8] [References]](#References)

## [Installation]

### [USE flags]

### [USE flags for] [app-containers/snapd](https://packages.gentoo.org/packages/app-containers/snapd) [[]] [Service and tools for management of snap packages]

  --------------------------------------------------------------------------- --------------------------------------------------------------------------------------------------
  [`+forced-devmode`](https://packages.gentoo.org/useflags/+forced-devmode)   Automatically disable application confinement if feature detection fails.
  [`apparmor`](https://packages.gentoo.org/useflags/apparmor)                 Enable support for the AppArmor application security system
  [`gtk`](https://packages.gentoo.org/useflags/gtk)                           Add support for x11-libs/gtk+ (The GIMP Toolkit)
  [`kde`](https://packages.gentoo.org/useflags/kde)                           Add support for software made by KDE, a free software community
  [`systemd`](https://packages.gentoo.org/useflags/systemd)                   Enable use of systemd-specific libraries and features like socket activation or session tracking
  --------------------------------------------------------------------------- --------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2025-01-11 08:11] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

** Note**\
It is highly recommended that you install and enable apparmor on your system to use snaps

** Note**\
Snaps can be confined using [Apparmor](https://wiki.gentoo.org/wiki/Security_Handbook/Linux_Security_Modules/AppArmor "Security Handbook/Linux Security Modules/AppArmor"), which is now enabled in the standard kernel. Consult the relevant wiki pages to find steps to enable on your system. [Security Handbook/Linux Security Modules/AppArmor](https://wiki.gentoo.org/wiki/Security_Handbook/Linux_Security_Modules/AppArmor "Security Handbook/Linux Security Modules/AppArmor")

** Note**\
As of this writing, systemd is mandatory ^[\[1\]](#cite_note-1)^

`root `[`#`]`emerge --ask app-containers/snapd`

## [Basic usage]

To install an application, e.g. Thunderbird, run:

`root `[`#`]`snap install thunderbird`

To remove an application, e.g. Thunderbird, run:

`root `[`#`]`snap remove thunderbird`

To run the application use created .desktop file or run:

`user `[`$`]`snap run thunderbird`

To update installed applications and runtimes:

`root `[`#`]`snap refresh`

To create the snap directory manually, run:

`root `[`#`]`mkdir -p /var/lib/snapd/snaps`

## [Systemd Users]

To enable and start the Snap daemon after emerging, run:

`root `[`#`]`systemctl enable --now snapd.socket`

## [Graphical management]

The Snap Store can be installed via snap

`root `[`#`]`snap install snap-store`

## [Troubleshooting]

** Note**\
Enable flags on [SquashFS](https://wiki.gentoo.org/wiki/SquashFS "SquashFS") in case you encounter lzo compression error

Filesystem uses lzo compression Erro. Enable [use flags](https://wiki.gentoo.org/wiki/Package.use "Package.use") \"lzo\" on [sys-fs/squashfs-tools](https://packages.gentoo.org/packages/sys-fs/squashfs-tools)

## [Support]

If you have any further questions, the [Snapcraft forum](https://forum.snapcraft.io/) is a great place to go.

## [See also]

-   [Docker](https://wiki.gentoo.org/wiki/Docker "Docker") --- a [container](https://en.wikipedia.org/wiki/Container_(virtualization) "wikipedia:Container (virtualization)")-based [virtualization](https://wiki.gentoo.org/wiki/Virtualization "Virtualization") system
-   [LXD](https://wiki.gentoo.org/wiki/LXD "LXD") --- a system container manager
-   [systemd/systemd-nspawn](https://wiki.gentoo.org/wiki/Systemd/systemd-nspawn "Systemd/systemd-nspawn") --- a lightweight, loosely [chroot](https://wiki.gentoo.org/wiki/Chroot "Chroot")-like, OS-level [OCI container](https://opencontainers.org/) environment native to [systemd](https://wiki.gentoo.org/wiki/Systemd "Systemd").
-   [Flatpak](https://wiki.gentoo.org/wiki/Flatpak "Flatpak") --- a package management framework aiming to provide support for sandboxed, distro-agnostic binary packages for Linux desktop applications.
-   [Security Handbook/Linux Security Modules/AppArmor](https://wiki.gentoo.org/wiki/Security_Handbook/Linux_Security_Modules/AppArmor "Security Handbook/Linux Security Modules/AppArmor")

## [References]

1.  [https://snapcraft.io/docs/quickstart-guide](https://snapcraft.io/docs/quickstart-guide)

1.  [[[↑](#cite_ref-1)] [[https://forums.gentoo.org/viewtopic-t-1147633-highlight-snap.html](https://forums.gentoo.org/viewtopic-t-1147633-highlight-snap.html)]]