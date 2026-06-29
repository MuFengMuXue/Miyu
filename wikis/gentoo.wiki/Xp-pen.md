**Resources**

[[]][Home](https://www.xp-pen.com/)

[[]][Wikipedia](https://en.wikipedia.org/wiki/XP-PEN "wikipedia:XP-PEN")

This article describes how to install [XP-PEN](https://en.wikipedia.org/wiki/XP-PEN "wikipedia:XP-PEN") drivers on Gentoo.

## Contents

-   [[1] [Prerequisites]](#Prerequisites)
    -   [[1.1] [Kernel]](#Kernel)
    -   [[1.2] [Dependencies]](#Dependencies)
-   [[2] [Installation]](#Installation)
-   [[3] [Ebuild]](#Ebuild)
-   [[4] [Manual Install]](#Manual_Install)
-   [[5] [Running]](#Running)
-   [[6] [Removal]](#Removal)

## [Prerequisites]

### [Kernel]

The driver requires user level driver (`CONFIG_INPUT_UINPUT`) support, or else it won\'t be able to move the cursor.

[KERNEL] **Enabling user level driver support**

    Device Drivers --->
       Input device support --->
          [*] Generic input layer (needed for keyboard, mouse,...)
          [*]   Miscellaneous devices --->
             <*>   User level driver support

### [Dependencies]

It also requires dependencies like [[[dev-qt/qtx11extras]](https://packages.gentoo.org/packages/dev-qt/qtx11extras)[]], [[[dev-qt/qtnetwork]](https://packages.gentoo.org/packages/dev-qt/qtnetwork)[]] and probably [[[x11-libs/libXrandr]](https://packages.gentoo.org/packages/x11-libs/libXrandr)[]].

## [Installation]

## [Ebuild]

An ebuild (x11-drivers/xf86-input-xppen) is provided in [GURU](https://wiki.gentoo.org/wiki/GURU "GURU"). [Enable the GURU repository](https://wiki.gentoo.org/wiki/Project:GURU/Information_for_End_Users "Project:GURU/Information for End Users") on the system if it is not enabled already, then install with:

`root `[`#`]`emerge --ask x11-drivers/xf86-input-xppen`

## [Manual Install]

** Warning**\
This download runs an installer which can damage a working system. Please perform backups before running any commands. Even if the latest ebuild dosen\'t work with your tablet (recent release tablet) is recommend to update it instead.

** Important**\
This driver is **NOT** open source.

Fetch and extract the XP-PEN driver installer:

`user `[`$`]`wget "https://download01.xp-pen.com/file/2024/07/XPPenLinux3.4.9-240131.tar.gz" -O xp-pen-driver.tar.gz `

`user `[`$`]`tar -xvzpf xp-pen-driver.tar.gz `

Run the installer:

`user `[`$`]`cd XPPenLinux3.4.9-240131/`

`root `[`#`]`./install.sh`

## [Running]

To launch the driver, run a script:

`user `[`$`]`/usr/lib/pentablet/pentablet.sh`

** Note**\
This driver may work improperly, if it\'s run as root.

## [Removal]

Go to the directory where you extracted the driver, and run:

`root `[`#`]`./uninstall.sh`