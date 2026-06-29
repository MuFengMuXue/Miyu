**Resources**

[[![Gentoo peach graphic](/images/thumb/a/ad/Gentoo-logo-peach.svg/25px-Gentoo-logo-peach.svg.png)](https://wiki.gentoo.org/wiki/Project:RelEng "Project:RelEng")][Project](https://wiki.gentoo.org/wiki/Project:RelEng "Project:RelEng")

[[]][GitWeb](https://gitweb.gentoo.org/proj/releng.git)

Gentoo offers **bootable media** that can be used to [install](https://wiki.gentoo.org/wiki/Installation "Installation"), maintain, or try out Gentoo Linux.

There are currently at least two bootable media images available for download on [www.gentoo.org](https://www.gentoo.org/downloads/): the *Minimal Installation CD* and the *LiveGUI USB Image*.

These image files may be written to media in order to boot a physical machine, or used to boot a virtual machine.

** Important**\
A bootable media live image file isn\'t commonly used \"as is\" to boot physical hardware: images should not usually just be \"placed\" on a disk as a file with a \"copy\" command, but rather \"interpreted as an entire disk\", with the aid of specialized software. See the [LiveUSB](https://wiki.gentoo.org/wiki/LiveUSB "LiveUSB") article for more information.

## Contents

-   [[1] [Minimal Installation CD]](#Minimal_Installation_CD)
-   [[2] [Admin CD]](#Admin_CD)
-   [[3] [LiveGUI USB Image]](#LiveGUI_USB_Image)
-   [[4] [See also]](#See_also)
-   [[5] [External resources]](#External_resources)

## [Minimal Installation CD]

The **minimal Installation CD** provides a very light [CLI](https://wiki.gentoo.org/wiki/Shell "Shell") environment which may be used for Gentoo installation. Note that the emerge command is not available.

The **[amd64]** minimal Installation CD can be downloaded from here: [install-amd64-minimal/](https://distfiles.gentoo.org/releases/amd64/autobuilds/current-install-amd64-minimal/). The downloaded file will have a name along the lines *install-amd64-minimal-20240225T170409Z.iso*.

Minimal Installation CD images for some other architectures are available in the sub-directories [here](https://distfiles.gentoo.org/releases/) (note that live images are not available for all architectures).

## [Admin CD]

There used to be a hardened version of the Minimal Installation CD with some additional packages to support advanced installs, recovery diagnostics of existing installs, perform additional hardware testing, and provide a better value to users wishing to utilize the full 700MB of CD-R capacity.

All of the features of the **admin CD** are now available in the **minimal installation CD**.

## [LiveGUI USB Image]

Writable directly to a USB stick or a dual-layer DVD, this amd64 image boots into KDE Plasma and is supplied with many useful packages such as office applications, Internet suite, graphics tools, system administration packages etc.

The LiveGUI can be useful for system maintenance, and is designed to show off what a full Gentoo installation can look like.

The list of packages included is found in the [catalyst specification file](https://gitweb.gentoo.org/proj/releng.git/tree/releases/specs/amd64/livegui/livegui-stage1.spec). Portage may be used to install more packages, but changes aren\'t persistent.

See the [release announcement](https://www.gentoo.org/news/2022/04/03/livegui-artwork-contest.html) for more information.

In the past, some \"LiveDVDs\" were produced by the loosely affiliated, community run, [\"Gentoo Ten\" project](https://wiki.gentoo.org/wiki/Project:RelEng/LiveDVD "Project:RelEng/LiveDVD"), but the latest effort is a separate endeavor and was created by [Andreas K. Hüttel (dilfridge)](https://wiki.gentoo.org/wiki/User:Dilfridge "User:Dilfridge") .

The **[amd64]** LiveGUI image can be downloaded from here: [livegui-amd64/](https://distfiles.gentoo.org/releases/amd64/autobuilds/current-livegui-amd64/). The downloaded file will have a name along the lines *livegui-amd64-20240225T170409Z.iso*.

## [See also]

-   [Installation](https://wiki.gentoo.org/wiki/Installation "Installation") --- an overview of the principles and practices of installing Gentoo on a running system.
-   [Live image](https://wiki.gentoo.org/wiki/Live_image "Live image") --- an operating system (OS) environment contained within a file that can be used to [boot](https://en.wikipedia.org/wiki/Booting "wikipedia:Booting") a system
-   [LiveUSB](https://wiki.gentoo.org/wiki/LiveUSB "LiveUSB") --- explains how to create a *Gentoo LiveUSB* or, in other words, how to emulate a **[x86]** or **[amd64]** Gentoo LiveCD using a USB drive.
-   [Stage file](https://wiki.gentoo.org/wiki/Stage_file "Stage file") --- an archive that contains all the files to run a minimal Gentoo environment, typically to serve as a seed for a Gentoo installation

## [External resources]

-   [Downloads -- Gentoo Linux](https://www.gentoo.org/downloads/) \-- the download page for bootable media and stage files.