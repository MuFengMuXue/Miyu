[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=Boxes&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

**Resources**

[[]][Home](https://help.gnome.org/users/gnome-boxes/stable/)

[[]][Package information](https://packages.gentoo.org/packages/gnome-extra/gnome-boxes)

[[]][GitHub](https://github.com/GNOME/gnome-boxes)

[[]][GitLab](https://gitlab.gnome.org/GNOME/gnome-boxes)

**Boxes** is an application from the [GNOME](https://wiki.gentoo.org/wiki/GNOME "GNOME") project that allows creating and accessing [virtual machines](https://wiki.gentoo.org/wiki/Virtualization "Virtualization"), running locally or remotely. It also allows to connect to the display of a remote computer.

Boxes leverages [QEMU](https://wiki.gentoo.org/wiki/QEMU "QEMU") with [KVM](https://wiki.gentoo.org/wiki/KVM "KVM"), [libvirt](https://wiki.gentoo.org/wiki/Libvirt "Libvirt"), [SPICE](https://wiki.gentoo.org/wiki/Remote_desktop#SPICE "Remote desktop"), and [VNC](https://wiki.gentoo.org/wiki/Remote_desktop#VNC_.28RFB_protocol.29 "Remote desktop").

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
-   [[2] [Configuration]](#Configuration)
    -   [[2.1] [User permissions]](#User_permissions)
-   [[3] [See also]](#See_also)

## [Installation]

### [USE flags]

### [USE flags for] [gnome-extra/gnome-boxes](https://packages.gentoo.org/packages/gnome-extra/gnome-boxes) [[]] [Simple GNOME application to access remote or virtual systems]

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2025-12-20 12:07] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

To use the file sharing feature of Boxes, [[[net-misc/spice-gtk]](https://packages.gentoo.org/packages/net-misc/spice-gtk)[]] must be emerged with the [webdav] USE flag enabled:

[FILE] **`/etc/portage/package.use/gnome-boxes`**

    net-misc/spice-gtk webdav

Install [gnome-boxes]:

`root `[`#`]`emerge --ask gnome-extra/gnome-boxes`

## [Configuration]

### [User permissions]

To create and run virtual machines using Boxes as a normal user, the user permissions and service for [libvirt](https://wiki.gentoo.org/wiki/Libvirt "Libvirt") must be set up [as shown in this article](https://wiki.gentoo.org/wiki/Libvirt#User_permissions "Libvirt").

Additionally, the user must be added to the [kvm] group:

`root `[`#`]`usermod -a -G kvm <user>`

## [See also]

-   [Gnome](https://wiki.gentoo.org/wiki/Gnome "Gnome") --- a feature-rich desktop environment provided by the [GNOME project](https://www.gnome.org).
-   [Virtualization](https://wiki.gentoo.org/wiki/Virtualization "Virtualization") --- the concept and technique that permits running software in an environment separate from a computer operating system.