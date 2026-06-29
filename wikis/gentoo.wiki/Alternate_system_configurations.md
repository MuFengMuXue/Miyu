[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=Alternate_system_configurations&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

## Contents

-   [[1] [Introduction]](#Introduction)
-   [[2] [System init]](#System_init)
-   [[3] [Device managers]](#Device_managers)
-   [[4] [Consolekit and polkit free systems]](#Consolekit_and_polkit_free_systems)
-   [[5] [Other stuff]](#Other_stuff)

## [Introduction]

Gentoo can be installed and configured to suit the users needs. While the [handbook](https://wiki.gentoo.org/wiki/Handbook:Main_Page "Handbook:Main Page") provides an officially supported installation and configuration method a number of users find alternate installation and configuration methods useful. For alternate methods of installation see [here](https://wiki.gentoo.org/wiki/Installation_alternatives "Installation alternatives"), Olde Fashoned Gentooee is an interesting approach- see link below.

Discussions regarding the following information can be found on the [user forums](https://forums.gentoo.org/), with this page aimed at providing a brief overview with links to relevant details. The pros and cons of a particular approach can be found in the links, discussions on the user forums, and through web searches. What works best will vary from person to person, and use case to use case.

Following the handbook, using default selections will result in a system installed with three partitions [/boot], swap, and / a root partition. It can be useful to have separate partitions for one or more of [/var] [/tmp] [/usr] [/home] [/opt].\
Although all init systems should support a separate [/home] partition, care is required to ensure other partitions will be correctly mounted and available during system boot.\

The use of encryption, [lvm](https://wiki.gentoo.org/wiki/LVM "LVM"), raid and which parts of the filesystem you choose to put on separate partitions can influence the approach required to ensure the system will boot using a particular init system.\
In some instances an [initramfs](https://wiki.gentoo.org/wiki/Initramfs "Initramfs") will be needed to boot the system, in other cases it may be recommended but may not be essential. A separate /usr partition is an example where some prefer not to use an initramfs \... example forums thread [HOWTO: udev/eudev, sep [/usr], no initramfs.](https://forums.gentoo.org/viewtopic-t-901206-highlight-seperate+separate.html)\
\
[Note: Suggested & recommended methods are just that, and you are free to use an approach which suits your particular use case \... but you get to keep all the pieces if it breaks - in all cases you own the pieces ;-)]\

\

## [System init]

There are a number of systems which can be used to initialize a system a comparison of these is available [comparison of init systems](https://wiki.gentoo.org/wiki/Comparison_of_init_systems "Comparison of init systems")

## [Device managers]

There are a number of alternatives available for device managers, these include udev, eudev, mdev \... Information on each of these can be found on wiki pages for example

[udev](https://wiki.gentoo.org/wiki/Udev "Udev")

[eudev](https://wiki.gentoo.org/index.php?title=Project:Eudev&action=edit&redlink=1 "Project:Eudev (page does not exist)")

[mdev](https://wiki.gentoo.org/wiki/Mdev "Mdev")

Or you could use [[[sys-fs/static-dev]](https://packages.gentoo.org/packages/sys-fs/static-dev)[]], in which case you need to unmerge udev and disable kernel maintain devtmpfs option.

## [Consolekit and polkit free systems]

It is possible setup a secure system without the use of consolekit, [polkit](https://wiki.gentoo.org/wiki/Polkit "Polkit") or [PAM](https://wiki.gentoo.org/wiki/PAM "PAM") - and some users prefer this approach. USE flags -pam -consolekit -polkit will help with this. [Example thread](https://forums.gentoo.org/viewtopic-t-981842.html).

## [Other stuff]

To prevent systemd from being installed add sys-apps/systemd to [/etc/portage/package.mask].

[Olde Fashioned Gentooee](https://dev.gentoo.org/~neddyseagoon/Old_Fashioned_Gentoo_3.xml) is an interesting approach to installing a system, but requires a Gentoo install to borrow from ;) see also [this thread](https://forums.gentoo.org/viewtopic-t-985752-highlight-.html).

To do \... still most of this wiki page \...