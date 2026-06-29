**Resources**

[[![Gentoo peach graphic](/images/thumb/a/ad/Gentoo-logo-peach.svg/25px-Gentoo-logo-peach.svg.png)](https://wiki.gentoo.org/wiki/Project:RelEng "Project:RelEng")][Project](https://wiki.gentoo.org/wiki/Project:RelEng "Project:RelEng")

[[]][GitWeb](https://gitweb.gentoo.org/proj/releng.git)

A **live image** provides an operating system (OS) environment contained within a file that can be used to [boot](https://en.wikipedia.org/wiki/Booting "wikipedia:Booting") a system. Live images are typically written to local media for booting into a *live environment*. Such an environment is often non-persistent, but can sometimes be used to install a *permanent* OS to non-volatile storage.

Live images are used to create a [live environment](https://wiki.gentoo.org/wiki/Live_environment "Live environment") from which to install Gentoo to persistent storage. Live images may also be used to maintain a Gentoo-based operating system, particularly in the case of issues resulting in a non-bootable system.

Gentoo offers the *LiveGUI USB Image*, the *Minimal Installation CD*, and an *Admin CD*.

A live image can also be called a *LiveUSB* image, or *live operating system* image. Historically, a live image has been referred to as a \"LiveCD\", \"LiveDVD\", \"ISO file\", \"LiveUSB GUI\", etc.

** Important**\
A live image file isn\'t commonly used \"as is\" to boot physical hardware: images should not usually just be \"placed\" on a disk as a file with a \"copy\" command, but rather \"interpreted as an entire disk\", with the aid of specialized software. See the [LiveUSB](https://wiki.gentoo.org/wiki/LiveUSB "LiveUSB") article for more information.

## Contents

-   [[1] [Live images offered by Gentoo]](#Live_images_offered_by_Gentoo)
-   [[2] [What live images are used for]](#What_live_images_are_used_for)
-   [[3] [Format]](#Format)
-   [[4] [See also]](#See_also)
-   [[5] [External resources]](#External_resources)

## [[] Live images offered by Gentoo]

The [Gentoo release engineering project](https://wiki.gentoo.org/wiki/Project:RelEng "Project:RelEng") produces live images for installation of or maintenance to Gentoo-based operating systems.

Go to the [bootable media](https://wiki.gentoo.org/wiki/Bootable_media "Bootable media") article to see what live images are offered by Gentoo for download.

## [[] What live images are used for]

Live images are used for a variety of useful purposes such as:

-   Installation of a Linux or other operating system
-   Demonstrating features prior to installation
-   System rescue
    -   Failed disk drive hardware
    -   Failed or corrupted file system
    -   Corrupted or missing kernel binary or modules preventing normal use of the system. In particular when missing a network interface driver or a filesystem required to mount rootfs
-   Digital forensics
-   Development
    -   Kernel driver development
-   Portable installation
-   Accessing/controlling physical hardware resources with an unlocked bootloader *without* needing special credentials for login :)
-   Testing
    -   Hardware testing
    -   Software testing

## [Format]

Live images are usually [.iso](https://en.wikipedia.org/wiki/ISO_9660 "wikipedia:ISO 9660") image files, using either [El Torito](https://en.wikipedia.org/wiki/ISO_9660#El_Torito "wikipedia:ISO 9660") or [Joliet](https://en.wikipedia.org/wiki/ISO_9660#Joliet "wikipedia:ISO 9660") extensions.

Gentoo live images are hybrid, meaning the image can either be burned to optical media or directly written to a USB drive using a data dump tool such as [dd](https://wiki.gentoo.org/wiki/Dd "Dd").

## [[] See also]

-   [Bootable media](https://wiki.gentoo.org/wiki/Bootable_media "Bootable media") --- Gentoo offers **bootable media** that can be used to [install](https://wiki.gentoo.org/wiki/Installation "Installation"), maintain, or try out Gentoo Linux
-   [Installation](https://wiki.gentoo.org/wiki/Installation "Installation") --- an overview of the principles and practices of installing Gentoo on a running system.
-   [Live environment](https://wiki.gentoo.org/wiki/Live_environment "Live environment") --- a term that describes an ephemeral or disposable operating system environment, typically created from a [live image].
-   [LiveUSB](https://wiki.gentoo.org/wiki/LiveUSB "LiveUSB") --- explains how to create a *Gentoo LiveUSB* or, in other words, how to emulate a **[x86]** or **[amd64]** Gentoo LiveCD using a USB drive.
-   [Stage file](https://wiki.gentoo.org/wiki/Stage_file "Stage file") --- an archive that contains all the files to run a minimal Gentoo environment, typically to serve as a seed for a Gentoo installation

## [External resources]

-   [Downloads -- Gentoo Linux](https://www.gentoo.org/downloads/) \-- the download page for bootable media and stage files.