Other languages:

-   [Deutsch](https://wiki.gentoo.org/wiki/HighPoint_RocketRAID/de "HighPoint RocketRAID (100% translated)")
-   [English]
-   [magyar](https://wiki.gentoo.org/wiki/HighPoint_RocketRAID/hu "HighPoint RocketRAID (100% translated)")
-   [русский](https://wiki.gentoo.org/wiki/HighPoint_RocketRAID/ru "HighPoint RocketRAID (80% translated)")
-   [日本語](https://wiki.gentoo.org/wiki/HighPoint_RocketRAID/ja "HighPoint RocketRAID (96% translated)")
-   [한국어](https://wiki.gentoo.org/wiki/HighPoint_RocketRAID/ko "HighPoint RocketRAID/ko (78% translated)")

**[] Deprecated article**\
\

This article is **deprecated (obsolete)**. Contents are [no longer relevant], and are intended for historical reference only!

\
TLDR: **Do not use this article!**

**Resources**

[[]][Home](http://www.highpoint-tech.com/)

** Important**\
The overlay referenced in this article has been abandoned by its author. These instructions may or may not work in recent times.

This guide assists with the installation of a RocketRAID card on Gentoo Linux.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [Enabling the HPT-RR overlay]](#Enabling_the_HPT-RR_overlay)
        -   [[1.1.1] [Using eselect repository]](#Using_eselect_repository)
    -   [[1.2] [Building and installing the Linux kernel module]](#Building_and_installing_the_Linux_kernel_module)
    -   [[1.3] [Loading the kernel module]](#Loading_the_kernel_module)
    -   [[1.4] [Installing supporting software]](#Installing_supporting_software)
-   [[2] [Configuration]](#Configuration)
-   [[3] [Administration]](#Administration)
-   [[4] [Supported cards]](#Supported_cards)
-   [[5] [Special thanks]](#Special_thanks)

## [Installation]

### [Enabling the HPT-RR overlay]

The [HPT-RR overlay](https://github.com/dsiggi/RocketRAID.git) contains the necessary packages to easily install and configure a RocketRAID card.

#### [Using eselect repository]

Ensure that [[[app-eselect/eselect-repository]](https://packages.gentoo.org/packages/app-eselect/eselect-repository)[]] and [[[dev-vcs/git]](https://packages.gentoo.org/packages/dev-vcs/git)[]] are installed:

`root `[`#`]`emerge --ask --noreplace app-eselect/eselect-repository dev-vcs/git`

Then configure and sync the overlay:

`root `[`#`]`eselect repository add RocketRAID git https://github.com/dsiggi/RocketRAID.git `

`root `[`#`]`emerge --sync RocketRAID`

### [Building and installing the Linux kernel module]

Depending on the [hardware card](#Supported_cards), enable the right USE flag.

Then, install the [sys-block/rocketraid](https://github.com/dsiggi/RocketRAID/tree/master/sys-block/rocketraid) package in order to automatically build and install the right kernel module:

`root `[`#`]`emerge --ask rocketraid`

### [Loading the kernel module]

Load the newly built kernel module (example for the rr232x module):

`root `[`#`]`modprobe rr232x`

Validate that the hardware has been properly detected by reading through the [dmesg] output close after loading the module:

`root `[`#`]`dmesg`

    ...
    [    2.499913] rr232x: module license 'Proprietary' taints kernel.
    [    2.500453] rr232x:RocketRAID 232x controller driver v1.10 (Dec 24 2014 11:50:36)
    [    2.500684] rr232x:adapter at PCI 3:4:0, IRQ 16
    [    3.073130] rr232x:start channel [0,0]
    [    3.073149] rr232x:start channel [0,1]
    [    3.073167] rr232x:start channel [0,3]
    [    3.424978] rr232x:channel [0,0] started successfully
    [    3.785922] rr232x:channel [0,1] started successfully
    [    4.156860] rr232x:channel [0,3] started successfully
    [    4.498815] scsi host6: rr232x
    ...

If the module correctly found the hardware, then make sure that this module is automatically loaded at boot. This can be accomplished by adding it to the [/etc/modules-load.d/raid.conf] file.

### [Installing supporting software]

There are a couple of software packages that provide additional support for the RocketRAID cards.

The [sys-block/hptraidconf](https://github.com/dsiggi/RocketRAID/tree/master/sys-block/hptraidconf) package provides configuration and monitoring support for the RocketRAID card. It requires a daemon running on the system, provided through the [sys-block/hptsvr](https://github.com/dsiggi/RocketRAID/tree/master/sys-block/hptsvr) package. The client itself does not need to be installed on the system that has the RAID card in it.

Deploy the two packages:

`root `[`#`]`emerge --ask hptsvr`

`root `[`#`]`emerge --ask hptraidconf`

## [Configuration]

To run the server, add the right hardware module to [/etc/hptcfg]:

`root `[`#`]`echo "rr232x" > /etc/hptcfg`

Now start the server:

`root `[`#`]`/etc/init.d/hptsvr start`

To start the server on every system boot, type in:

`root `[`#`]`rc-update add hptsvr default`

## [Administration]

To administer the RAID card settings, connect to the server using the [hptraidconf] command.

The default username is **RAID** and the default password is **hpt**.

`root `[`#`]`hptraidconf [-i server:port]`

            HighPoint RAID Management Command Line Utility v3.3
    Copyright (C) 2009 HighPoint Technologies, Inc. All rights reserved.

    Login:RAID
    Password:

After a successful login, a prompt will appear through which the administrative tasks can be executed.

`HighPoint CLI>``query arrays 1`

    ID:             1                   Name:           Storage
    Type:           RAID5               Status:         NORMAL
    Capacity(GB):   2000.25             BlockSize:      64k
    SectorSize:     512B                CachePolicy:    WB
    Progress:       --
    ID      Capacity    MaxFree     Flag    Statue    ModelNumber
    -------------------------------------------------------------------------------
    1/1     1000.12     0           NORMAL  RAID      ST1000LM024 HN-M101MBB
    1/2     1000.12     0           NORMAL  RAID      ST1000LM024 HN-M101MBB
    1/4     1000.12     0           NORMAL  RAID      ST1000LM024 HN-M101MBB
    -------------------------------------------------------------------------------

All supported commands are documented in the [official documentation (.tgz)](http://www.highpoint-tech.com/BIOS_Driver/GUI/linux/CLL/CLI-Linux-3.5-100701.tgz).

## [Supported cards]

  --------------------------------- --------
  Card                              module
  RocketRAID 1720                   rr172x
  RocketRAID 1740/1742              rr174x
  RocketRAID 2210                   rr2210
  RocketRAID 2220/2224              rr222x
  RocketRAID 2240                   rr2240
  RocketRAID 2314/2310/2302/2300    rr231x
  RocketRAID 2322/2320              rr232x
  RocketRAID 2340                   rr2340
  RocketRAID 2522                   rr2522
  RocketRAID 2644X4                 rr2644
  RocketRAID 2640X4/2640X1/2642     rr264x
  RocketRAID 2680/2684              rr268x
  RocketRAID 620/622                rr62x
  RocketRAID 640/644                rr64x
  RocketRAID 640L/644L/644LS/642L   rr64xl
  --------------------------------- --------

## [Special thanks]

Special thanks go to *camper2* from [ubuntuforums.org](http://www.ubuntuforums.org) who wrote the patches for the kernel modules.

Also special thanks goes to *dlder* from [forums.opensuse.org](https://forums.opensuse.org/showthread.php/519259-Here-is-an-unofficial-driver-patch-for-the-quot-RocketRaid-232x-quot-%5C!-(kernel-4-x)%5C%22) for the new patches for kernels \>=4.7.