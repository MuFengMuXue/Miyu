**[] Archived article**\
\

This article is **archived (obsolete)**. Contents are surely incorrect for current usage, and are intended for historical reference only.

\
TLDR: **Do not use this article!**

**Resources**

[[]][Home](https://www.freebsd.org/)

[[]][Wikipedia](https://en.wikipedia.org/wiki/FreeBSD "wikipedia:FreeBSD")

** Important**\
Sometimes, Gentoo FreeBSD\'s `@system` is broken. Please get latest information from \"Depends on\" of [[[bug #462580]](https://bugs.gentoo.org/show_bug.cgi?id=462580)[]].

Gentoo FreeBSD was a Gentoo system based on the FreeBSD kernel. Gentoo FreeBSD is no longer maintained by any active Gentoo developers.

Gentoo FreeBSD was FreeBSD with the following changes:

-   Portage replaces ports.
-   The base system is managed by Portage.
-   Software in [./contrib] and [./crypto] is replaced with Gentoo versions.
-   The rc system is replaced with [OpenRC](https://wiki.gentoo.org/wiki/OpenRC "OpenRC").
-   [python], [wget], and [bash] are included in the base system to support Portage.
-   FreeBSD\'s bootloader is removed from the base system (useful for jails).

** Note**\
Gentoo FreeBSD is not 100% binary-compatibility with regular FreeBSD due to `SONAME` differences. It is possible to workaround that by running regular FreeBSD in either a jail or chroot on Gentoo FreeBSD or vice versa. Gentoo FreeBSD is also not 100% script-compatible with regular FreeBSD by default. Script compatibility can be restored by installing [[[sys-freebsd/ubin-wrappers]](https://packages.gentoo.org/packages/sys-freebsd/ubin-wrappers)[]]. This makes it possible to use \*BSD software like pkgsrc.

## Contents

-   [[1] [Introduction to FreeBSD]](#Introduction_to_FreeBSD)
    -   [[1.1] [What is FreeBSD?]](#What_is_FreeBSD.3F)
    -   [[1.2] [What is Gentoo/FreeBSD?]](#What_is_Gentoo.2FFreeBSD.3F)
    -   [[1.3] [FreeBSD and Linux]](#FreeBSD_and_Linux)
-   [[2] [Installation]](#Installation)
    -   [[2.1] [Caution]](#Caution)
    -   [[2.2] [Preparation]](#Preparation)
        -   [[2.2.1] [Optional: Setting keymap]](#Optional:_Setting_keymap)
        -   [[2.2.2] [Network setting]](#Network_setting)
        -   [[2.2.3] [Optional: Installing via ssh]](#Optional:_Installing_via_ssh)
        -   [[2.2.4] [Setting the partition]](#Setting_the_partition)
            -   [[2.2.4.1] [Using the UFS2 file system (GPT)]](#Using_the_UFS2_file_system_.28GPT.29)
                -   [[2.2.4.1.1] [Using FreeBSD\'s default bootloader (recommended)]](#Using_FreeBSD.27s_default_bootloader_.28recommended.29)
                -   [[2.2.4.1.2] [Using grub2. \[Experimental\]]](#Using_grub2._.5BExperimental.5D)
            -   [[2.2.4.2] [Using the UFS2 file system (MBR)]](#Using_the_UFS2_file_system_.28MBR.29)
                -   [[2.2.4.2.1] [Using FreeBSD\'s default bootloader (recommended)]](#Using_FreeBSD.27s_default_bootloader_.28recommended.29_2)
                -   [[2.2.4.2.2] [Using GRUB2 (experimental)]](#Using_GRUB2_.28experimental.29)
            -   [[2.2.4.3] [Using the ZFS file system (experimental) / (GPT)]](#Using_the_ZFS_file_system_.28experimental.29_.2F_.28GPT.29)
                -   [[2.2.4.3.1] [Using FreeBSD\'s default bootloader (recommended)]](#Using_FreeBSD.27s_default_bootloader_.28recommended.29_3)
                -   [[2.2.4.3.2] [Using GRUB2 (experimental)]](#Using_GRUB2_.28experimental.29_2)
        -   [[2.2.5] [Creating and mounting a file system]](#Creating_and_mounting_a_file_system)
            -   [[2.2.5.1] [Using the UFS2 file system]](#Using_the_UFS2_file_system)
            -   [[2.2.5.2] [Using the ZFS file system (experimental)]](#Using_the_ZFS_file_system_.28experimental.29)
        -   [[2.2.6] [Downloading the stage 3 file and Portage snapshot]](#Downloading_the_stage_3_file_and_Portage_snapshot)
        -   [[2.2.7] [Unpacking stage3 and Portage snapshot]](#Unpacking_stage3_and_Portage_snapshot)
        -   [[2.2.8] [Entering the new environment]](#Entering_the_new_environment)
    -   [[2.3] [Settings and install more in chroot environment]](#Settings_and_install_more_in_chroot_environment)
        -   [[2.3.1] [The first settings and time zone settings]](#The_first_settings_and_time_zone_settings)
        -   [[2.3.2] [Bug fixes (for x86-fbsd users, 9.0 stage 3 only)]](#Bug_fixes_.28for_x86-fbsd_users.2C_9.0_stage_3_only.29)
        -   [[2.3.3] [Special settings for ZFS]](#Special_settings_for_ZFS)
        -   [[2.3.4] [Installing a kernel source]](#Installing_a_kernel_source)
        -   [[2.3.5] [Compiling and installing kernel]](#Compiling_and_installing_kernel)
        -   [[2.3.6] [System settings]](#System_settings)
            -   [[2.3.6.1] [Special settings for ZFS]](#Special_settings_for_ZFS_2)
            -   [[2.3.6.2] [Special settings for virtual machine]](#Special_settings_for_virtual_machine)
        -   [[2.3.7] [Installing the required packages]](#Installing_the_required_packages)
        -   [[2.3.8] [Installing the boot loader]](#Installing_the_boot_loader)
        -   [[2.3.9] [Setting boot loader]](#Setting_boot_loader)
        -   [[2.3.10] [Exiting the chroot]](#Exiting_the_chroot)
    -   [[2.4] [Cleaning up and setting the remaining]](#Cleaning_up_and_setting_the_remaining)
        -   [[2.4.1] [Special settings for ZFS]](#Special_settings_for_ZFS_3)
        -   [[2.4.2] [Reboot!]](#Reboot.21)
-   [[3] [Running Gentoo FBSD in vanilla FreeBSD\'s jail]](#Running_Gentoo_FBSD_in_vanilla_FreeBSD.27s_jail)
    -   [[3.1] [Preparing directory]](#Preparing_directory)
    -   [[3.2] [Downloading and unpacking the stage 3 file and Portage snapshot]](#Downloading_and_unpacking_the_stage_3_file_and_Portage_snapshot)
    -   [[3.3] [Setting]](#Setting)
    -   [[3.4] [Run jail]](#Run_jail)
-   [[4] [Developing for Gentoo/FreeBSD]](#Developing_for_Gentoo.2FFreeBSD)
    -   [[4.1] [How to help]](#How_to_help)
-   [[5] [Troubleshooting]](#Troubleshooting)
    -   [[5.1] [Architecture independent issues]](#Architecture_independent_issues)
        -   [[5.1.1] [Emerge fails app-misc/screen]](#Emerge_fails_app-misc.2Fscreen)
        -   [[5.1.2] [lex: not found]](#lex:_not_found)
        -   [[5.1.3] [cc: not found]](#cc:_not_found)
-   [[6] [Contacts]](#Contacts)
-   [[7] [See also]](#See_also)
-   [[8] [External resources]](#External_resources)

## [Introduction to FreeBSD]

### [][What is FreeBSD?]

[FreeBSD](https://www.freebsd.org/) is a free ([license](https://www.freebsd.org/copyright/freebsd-license.html)) Unix-like operating system. Back in 1993 when development of [386BSD](https://www.386bsd.org/) stopped, two projects were born: [NetBSD](https://www.netbsd.org/), commonly known to run on a huge number of architectures, and FreeBSD which supports the x86, amd64, ia64, sparc64, and alpha platforms. FreeBSD is renowned for its stability, performance and security, thus being used from small to huge companies all over the world.

FreeBSD\'s current production release is version 11.0. Gentoo/FreeBSD is based on version 11.0 and older versions of Gentoo/FreeBSD are discontinued and no longer supported.

### [][What is Gentoo/FreeBSD?]

Gentoo FreeBSD project was a sub-project of the [Prefix project](https://wiki.gentoo.org/wiki/Project:Prefix "Project:Prefix"), with the goal of providing a fully-capable FreeBSD operating system featuring design sensibilities taken from Gentoo Linux, such as the init system and the Portage package management system.

### [FreeBSD and Linux]

Users migrating from Linux to FreeBSD commonly consider the two operating systems \"almost the same\". In fact, FreeBSD really shares a lot of similarities with Linux distributions in general. Nevertheless, it has some key differences that are worth noting:

-   Contrary to Linux, which actually only refers to the kernel, FreeBSD is a complete operating system, consisting of a C library, userland tools, and much more. This development approach makes the overall system very consistent.
-   Contrary to the Linux kernel, FreeBSD development is not led by one person, but instead managed by a small group of people called the [Core Team](https://www.freebsd.org/doc/en_US.ISO8859-1/articles/contributors/staff-committers.html).

Besides, FreeBSD also has some technical differences which set it apart from Linux. Some of them are very important to know, even for those who do not plan on joining the Gentoo FreeBSD development effort:

-   To get run-time dynamic linking functions like `dlopen()`, programs do not need to be linked against libdl like on GNU/Linux. Instead they are linked against libc.
-   FreeBSD doesn\'t have an official tool for kernel compilation, thus you\'ll have to resolve feature dependencies by hand.
-   FreeBSD supports [UFS](https://wiki.gentoo.org/wiki/UFS "UFS")/[UFS2](https://wiki.gentoo.org/wiki/UFS2 "UFS2") and [ZFS](https://wiki.gentoo.org/wiki/ZFS "ZFS") as native file systems.
-   FreeBSD also supports Linux filesystems, but you cannot install your system on them. ext2/ext3 supports read/write access. ReiserFS and [XFS](https://wiki.gentoo.org/wiki/XFS "XFS") are read-only support. For details see FreeBSD\'s handbook [21.3. Linux® Filesystems](https://www.freebsd.org/doc/handbook/filesystems-linux.html)

## [Installation]

** Important**\
Part of x86-fbsd is out of date. Please install amd64-fbsd.

### [Caution]

This guide provides minimal information about Gentoo FreeBSD. You need specialized knowledge of Gentoo Linux and FreeBSD. The [Gentoo Linux Handbook](https://wiki.gentoo.org/wiki/Handbook:Main_Page "Handbook:Main Page") and [FreeBSD Handbook](https://www.freebsd.org/handbook/) should be close friends.

### [Preparation]

Gentoo/FreeBSD doesn\'t have the installation media. Instead, you can use vanilla FreeBSD 9.0 or later version one. Please get [i386](http://ftp-archive.freebsd.org/pub/FreeBSD-Archive/old-releases/i386/ISO-IMAGES/9.0/) or [amd64](http://ftp-archive.freebsd.org/pub/FreeBSD-Archive/old-releases/amd64/ISO-IMAGES/9.1/) from ftp-archive.freebsd.org. Some ISO images are available from the ftp server, but please get -bootonly.iso image. Because you can install Gentoo/FreeBSD with the smallest media. If you want to use a memory stick, please get -memstick.img. If necessary, burn it to a CD or write it to a memory stick.

Boot your PC with the installation media. Wait for a Welcome dialog display. Please choose Shell.

** Note**\
If you have 4KB/sector HDD (aka AFT Drive)

Please select \"2. \[Esc\]ape to loader prompt\" at boot time if you have a 4KB/sector HDD.

Set the device name of your HDD with 4KB sectors in the boot loader. ada1 and ada2\... to increase if you have more than one.

    set kern.cam.ada.0.quirks="1"
    boot

#### [Optional: Setting keymap]

If the keyboard is not an English 101 key keyboard, set the keymap as appropriate:

`root `[`#`]`kbdcontrol -l uk.iso`

A list of the keymap is available with the following command:

`root `[`#`]`ls -1 /usr/share/syscons/keymaps | less`

#### [Network setting]

First, create a directory [/tmp/bsdinstall_etc] to rewrite the [resolv.conf] file:

`root `[`#`]`mkdir -p /tmp/bsdinstall_etc`

Identify the system\'s network devices. In this example the network interface is `em0`:

`root `[`#`]`ifconfig`

    em0: flags=8843<UP,BROADCAST,RUNNING,SIMPLEX,MULTICAST> metric 0 mtu 1500
            options=209b<RXCSUM,TXCSUM,VLAN_MTU,VLAN_HWTAGGING,VLAN_HWCSUM,WOL_MAGIC>
            ether 00:00:00:00:00:00
            nd6 options=29<PERFORMNUD,IFDISABLED,AUTO_LINKLOCAL>
            media: Ethernet autoselect (1000baseT <full-duplex>)
            status: active
    lo0: flags=8049<UP,LOOPBACK,RUNNING,MULTICAST> metric 0 mtu 16384
            options=3<RXCSUM,TXCSUM>
            inet6 ::1 prefixlen 128
            inet6 fe80::1%lo0 prefixlen 64 scopeid 0x3
            inet 127.0.0.1 netmask 0xff000000
            nd6 options=21<PERFORMNUD,AUTO_LINKLOCAL>

Set the default gateway and IP address.

When setting a static address:

`root `[`#`]`ifconfig em0 192.168.0.100 `

`root `[`#`]`route add default 192.168.0.1 `

`root `[`#`]`echo "nameserver 8.8.8.8" > /etc/resolv.conf `

When using DHCP:

`root `[`#`]`dhclient em0`

#### [Optional: Installing via ssh]

`root `[`#`]`mkdir -p /tmp/etc `

`root `[`#`]`mount -t tmpfs tmpfs /tmp/etc `

`root `[`#`]`mount -t unionfs /tmp/etc /etc `

`root `[`#`]`passwd `

`root `[`#`]`echo "PermitRootLogin yes" >> /etc/ssh/sshd_config `

`root `[`#`]`/etc/rc.d/sshd onestart `

Please connect with any ssh client. The username is root.

#### [Setting the partition]

** Important**\
[[[sys-boot/grub2]](https://packages.gentoo.org/packages/sys-boot/grub2)[]] doesn\'t have KEYWORDS=\"\~amd64-fbsd \~x86-fbsd\" yet. [[[sys-freebsd/boot0]](https://packages.gentoo.org/packages/sys-freebsd/boot0)[]] is recommended for bootloader on Gentoo FreeBSD.

** Note**\
If you want to use GRUB2, you need 1 MB free space at the beginning of the disk (MBR) or bios-boot partition (GPT). GRUB2 cannot find freebsd-boot partition. Please set the bios-boot (GPT).

You need to find out the device name to install. You can get it with `ls /dev/*da*` or `dmesg | grep 'da[0-9]'`. In this case, it\'s ada0:

** Note**\
If you are using serial ATA & IDE drives, the device name is /dev/ada\*. If you are using SCSI & USB drives, it\'s /dev/da\*.

`root `[`#`]`dmesg | grep 'da[0-9]'`

    ada0 at ata0 bus 0 scbus0 target 0 lun 0
    ada0: <QEMU HARDDISK 0.15.> ATA-7 device
    ada0: 16.700MB/s transfers (WDMA2, PIO 8192bytes)
    ada0: 12288MB (25165824 512 byte sectors: 16H 63S/T 16383C)
    ada0: Previously was known as ad0

##### [][Using the UFS2 file system (GPT)]

** Note**\
GPT partitions are the standard in FreeBSD 9.0. Please read the next MBR section if using a MBR partition.

If you follow this example, you will create two simple partitions. If necessary, you can split [/], [/usr], [/var], [/tmp], and [/home]. Please set these with gpart.

  -------------------------------------------------------------------------------------------------- ------------ -------------------------- -------------------------
  Partition                                                                                          Filesystem   Size                       Description
  [/dev/ada0p1]   none         just a bit                 Reserved for bootloader
  [/dev/ada0p2]   UFS2 + SU    entire disk - swap space   Root partition
  [/dev/ada0p3]   swap         Rest of the disk           Swap partition
  -------------------------------------------------------------------------------------------------- ------------ -------------------------- -------------------------

** Note**\
Please add options `-a 4k` to gpart add commands, if you have an AFT drive (4096 bytes/sector). The start of the partition is properly configured, you can get the best performance.

###### [][Using FreeBSD\'s default bootloader (recommended)]

`root `[`#`]`gpart create -s GPT ada0 `

`root `[`#`]`gpart add -s 64k -t freebsd-boot ada0 `

`root `[`#`]`gpart add -s 10G -t freebsd-ufs -l root ada0 `

`root `[`#`]`gpart add -t freebsd-swap -l swap ada0 `

Please run gpart show in order to confirm results.

`root `[`#`]`gpart show`

    =>      34  25165757  ada0  GPT  (12G)
            34       128     1  freebsd-boot  (64k)
           162  20971520     2  freebsd-ufs  (10G)
      20971682   4194109     3  freebsd-swap  (2G)

Results when you create a partition with option -a 4k.

`root `[`#`]`gpart show`

    =>      34  25165757  ada0  GPT  (12G)
            34         6        - free -  (3.0k)
            40       128     1  freebsd-boot  (64k)
           168  20971520     2  freebsd-ufs  (10G)
      20971688   4194096     3  freebsd-swap  (2G)
      25165784         7        - free -  (3.5k)

###### [][Using grub2. \[Experimental\]]

`root `[`#`]`gpart create -s GPT ada0 `

`root `[`#`]`gpart add -s 1024k -t bios-boot ada0 `

`root `[`#`]`gpart add -s 10G -t freebsd-ufs -l root ada0 `

`root `[`#`]`gpart add -t freebsd-swap -l swap ada0 `

##### [][Using the UFS2 file system (MBR)]

  --------------------------------------------------------------------------------------------------- ------------ -------------------------- ----------------
  Partition                                                                                           Filesystem   Size                       Description
  [/dev/ada0s1a]   UFS2 + SU    entire disk - swap space   Root partition
  [/dev/ada0s1b]   swap         Rest of the disk           Swap partition
  --------------------------------------------------------------------------------------------------- ------------ -------------------------- ----------------

###### [][Using FreeBSD\'s default bootloader (recommended)]

`root `[`#`]`gpart create -s mbr ada0 `

`root `[`#`]`gpart add -t freebsd ada0 `

`root `[`#`]`gpart set -a active -i 1 ada0 `

`root `[`#`]`gpart create -s bsd ada0s1 `

`root `[`#`]`gpart add -s 10G -t freebsd-ufs ada0s1 `

`root `[`#`]`gpart add -t freebsd-swap ada0s1 `

###### [][Using GRUB2 (experimental)]

`root `[`#`]`gpart create -s mbr ada0 `

`root `[`#`]`gpart add -b 1024k -t freebsd ada0 `

`root `[`#`]`gpart set -a active -i 1 ada0 `

`root `[`#`]`gpart create -s bsd ada0s1 `

`root `[`#`]`gpart add -s 10G -t freebsd-ufs ada0s1 `

`root `[`#`]`gpart add -t freebsd-swap ada0s1 `

##### [][Using the ZFS file system (experimental) / (GPT)]

###### [][Using FreeBSD\'s default bootloader (recommended)]

`root `[`#`]`gpart create -s GPT ada0 `

`root `[`#`]`gpart add -s 64k -t freebsd-boot ada0 `

`root `[`#`]`gpart add -t freebsd-zfs -l zfs-system ada0 `

###### [][Using GRUB2 (experimental)]

`root `[`#`]`gpart create -s GPT ada0 `

`root `[`#`]`gpart add -s 1024k -t bios-boot ada0 `

`root `[`#`]`gpart add -t freebsd-zfs -l zfs-system ada0 `

#### [Creating and mounting a file system]

##### [Using the UFS2 file system]

Please don\'t forget newfs `-L` option to label.

** Note**\
Add option `-j` to newfs to enable soft updates journaling. Add option `-t` to enable TRIM.

Your choice GPT:

`root `[`#`]`newfs -L gfbsdroot -U /dev/ada0p2`

Your choice MBR:

`root `[`#`]`newfs -L gfbsdroot -U /dev/ada0s1a`

And mount it:

`root `[`#`]`mount /dev/ufs/gfbsdroot /mnt `

`root `[`#`]`swapon /dev/gpt/swap (GPT) `

`root `[`#`]`swapon /dev/ada0s1b (MBR) `

##### [][Using the ZFS file system (experimental)]

Load the kernel module in order to enable ZFS:

`root `[`#`]`kldload zfs`

Prepare the RAM disk to write [/boot/zfs/zpool.cache]:

`root `[`#`]`mount -t tmpfs tmpfs /boot/zfs`

Please use gnop if you have 4KB/sector HDD. You can get the best performance:

`root `[`#`]`gnop create -S 4096 /dev/gpt/zfs-system`

Creates a new storage pool. When using gnop, please specify [/dev/gpt/zfs-system.nop] instead of [/dev/gpt/zfs-system].

`root `[`#`]`zpool create zsys /dev/gpt/zfs-system `

`root `[`#`]`zfs set mountpoint=none zsys`

Creates a new ZFS file system:

`root `[`#`]`zfs create zsys/root `

`root `[`#`]`zfs set mountpoint=/mnt zsys/root `

`root `[`#`]`zfs mount -a `

`root `[`#`]`zfs create zsys/root/usr `

`root `[`#`]`zfs create zsys/root/var`

`root `[`#`]`zfs create zsys/root/tmp `

`root `[`#`]`zfs create zsys/home `

`root `[`#`]`zfs create -V 8gb zsys/swap `

`root `[`#`]`zfs set org.freebsd:swap=on zsys/swap `

`root `[`#`]`zfs set checksum=off zsys/swap `

`root `[`#`]`mkdir /mnt/home `

`root `[`#`]`mount -t zfs zsys/home /mnt/home `

#### [Downloading the stage 3 file and Portage snapshot]

Now, Gentoo/FreeBSD 9.0 [stage 3](https://wiki.gentoo.org/index.php?title=Stage_3&action=edit&redlink=1 "Stage 3 (page does not exist)") is available for x86-fbsd. And Gentoo FreeBSD 9.1 [stage 3](https://wiki.gentoo.org/index.php?title=Stage_3&action=edit&redlink=1 "Stage 3 (page does not exist)") is available for amd64-fbsd.

** Important**\
If you want to use amd64-fbsd, please upgrade to 10.3 after the installation is complete. FreeBSD 9.1 is EOL on December 31, 2014. If you want to use x86-fbsd, please upgrade to 10.3 after the installation is complete. FreeBSD 9.0 is EOL on March 31, 2013.

`root `[`#`]`cd /mnt `

`root `[`#`]`fetch `[`http://dev.gentoo.org/~aballier/fbsd9.0/x86/stage3-i686-freebsd-9.0.tar.bz2`](http://dev.gentoo.org/~aballier/fbsd9.0/x86/stage3-i686-freebsd-9.0.tar.bz2)` (for x86-fbsd users) `

`root `[`#`]`fetch `[`http://distfiles.gentoo.org/experimental/bsd/freebsd/stages/amd64-fbsd-9.1/stage3-amd64-freebsd-9.1.tar.bz2`](http://distfiles.gentoo.org/experimental/bsd/freebsd/stages/amd64-fbsd-9.1/stage3-amd64-freebsd-9.1.tar.bz2)` (for amd64-fbsd users) `

`root `[`#`]`fetch `[`http://distfiles.gentoo.org/snapshots/portage-latest.tar.bz2`](http://distfiles.gentoo.org/snapshots/portage-latest.tar.bz2)` `

#### [Unpacking stage3 and Portage snapshot]

** Important**\
The following error may be displayed. Don\'t worry, please continue the installation. This problem will be fixed in 9.2. Details, see [[[bug #469454]](https://bugs.gentoo.org/show_bug.cgi?id=469454)[]]

    ./bin/fuser: Can't create 'bin/fuser'
    tar: Error exit delayed from previous errors.

`root `[`#`]`cd /mnt `

`root `[`#`]`setenv LANG "en_US.UTF-8" `

`root `[`#`]`tar xjpf stage3-*.tar.bz2 -C /mnt `

`root `[`#`]`tar xjf portage-latest.tar.bz2 -C /mnt/usr `

#### [Entering the new environment]

`root `[`#`]`mount -t devfs devfs /mnt/dev `

`root `[`#`]`cp /etc/resolv.conf /mnt/etc/ `

`root `[`#`]`chroot /mnt /bin/bash`

### [Settings and install more in chroot environment]

#### [The first settings and time zone settings]

env-update and time zone settings. Of course, you can modify [/etc/portage/make.conf].

`(chroot) root #``env-update && source /etc/profile `

`(chroot) root #``cp /usr/share/zoneinfo/GMT /etc/localtime (please select your time zone) `

`(chroot) root #``emerge -u sys-apps/portage ; emerge sys-devel/libtool app-admin/eselect `

`(chroot) root #``emerge app-editors/nano `

`(chroot) root #``mv /etc/make.conf /etc/portage/ (if /etc/make.conf is exist.) `

`(chroot) root #``nano -w /etc/portage/make.conf (if necessary) `

#### [][Bug fixes (for x86-fbsd users, 9.0 stage 3 only)]

Bugs have been fixed in several packages. Please upgrade them. For details, see [[[bug #324445]](https://bugs.gentoo.org/show_bug.cgi?id=324445)[]], [[[bug #412319]](https://bugs.gentoo.org/show_bug.cgi?id=412319)[]], [[[bug #417031]](https://bugs.gentoo.org/show_bug.cgi?id=417031)[]], and [[[bug #421191]](https://bugs.gentoo.org/show_bug.cgi?id=421191)[]].

`(chroot) root #``emerge sys-devel/gcc-config `

`(chroot) root #``emerge sys-freebsd/freebsd-mk-defs sys-freebsd/freebsd-lib app-arch/libarchive dev-libs/libedit `

#### [Special settings for ZFS]

If you select ZFS file system, the following additional work is required.

`(chroot) root #``emerge flaggie `

`(chroot) root #``flaggie +zfs `

`(chroot) root #``emerge sys-devel/flex `

`(chroot) root #``emerge sys-freebsd/freebsd-cddl `

`(chroot) root #``emerge sys-freebsd/freebsd-lib sys-freebsd/freebsd-ubin sys-freebsd/boot0 `

#### [Installing a kernel source]

Unlike Gentoo/Linux, freebsd-sources package is the only sources.

`(chroot) root #``USE=symlink emerge freebsd-sources `

#### [Compiling and installing kernel]

Now let\'s compile the kernel. For more information see the [FreeBSD Handbook](https://www.freebsd.org/doc/handbook/kernelconfig.html).

`(chroot) root #``emerge -u sys-devel/flex `

`(chroot) root #``cd /usr/src/sys/i386/conf (case of x86-fbsd) `

`(chroot) root #``cd /usr/src/sys/amd64/conf (case of amd64-fbsd) `

`(chroot) root #``cp GENERIC.hints /boot/device.hints `

`(chroot) root #``config GENERIC `

`(chroot) root #``cd ../compile/GENERIC `

`(chroot) root #``make cleandepend && make depend && make -j3 && make install `

#### [System settings]

Familiar settings. Please refer to [Gentoo Handbook](https://wiki.gentoo.org/wiki/Gentoo_Handbook "Gentoo Handbook") for more information.

When selecting UFS2:

`(chroot) root #``nano -w /etc/fstab`

    # Device  Mountpoint  FStype  Options Dump    Pass#
    /dev/ufs/gfbsdroot  /       ufs rw  1   1

    #your choice GPT (don't forget comment out)
    #/dev/gpt/swap  none        swap    sw  0   0

    #your choice MBR (don't forget comment out)
    #/dev/ada0s1b   none        swap    sw  0   0

If you select ZFS. Note that the Pass# column should be zero for ZFS, because it cannot be checked by fsck.

`(chroot) root #``nano -w /etc/fstab`

    # Device  Mountpoint  FStype  Options Dump    Pass#
    #/dev/ad0s1a    /       ufs rw  1   1
    #/dev/ad0s1b    none        swap    sw  0   0
    zsys/root   /       zfs rw  0   0

Setting the host name

`(chroot) root #``nano -w /etc/conf.d/hostname`

    # (Set the hostname variable to your host name.  On BSD this is expected to be the FQDN.)
    hostname="daemon.homenetwork"

Editing network settings

`(chroot) root #``nano -w /etc/conf.d/net`

    # (Set the dns_domain variable to your domain name)
    dns_domain_lo="homenetwork"

    # Manually setting)
    config_em0="192.168.0.100 netmask 255.255.255.0"
    routes_em0="default via 192.168.0.1"

    # Using DHCP)
    config_em0="dhcp"

Adding net.em0 to the default runlevel

`(chroot) root #``cd /etc/init.d `

`(chroot) root #``ln -s net.lo0 net.em0 `

`(chroot) root #``rc-update add net.em0 default `

Setting keymap

Please edit [/etc/conf.d/syscons] if you want to change the keymap.

`(chroot) root #``nano -w /etc/conf.d/syscons `

A list of the keymap is available with the following command.

`(chroot) root #``ls -1 /usr/share/syscons/keymaps | less `

Setting the root password

`(chroot) root #``passwd `

Adding a user for daily use (sample)

`(chroot) root #``adduser `

    Username: yournickname
    Full name:
    Uid (Leave empty for default):
    Login group [yournickname]:
    Login group is yournickname. Invite yournickname into other groups? []: wheel
    Login class [default]:
    Shell (bash csh esh fish ksh sash sh tcsh zsh nologin) [sh]: bash
    Home directory [/home/yournickname]:
    Home directory permissions (Leave empty for default):
    Use password-based authentication? [yes]:
    Use an empty password? (yes/no) [no]:
    Use a random password? (yes/no) [no]:
    Enter password:
    Enter password again:
    Lock out the account after creation? [no]:
    Username   : yournickname
    Password   : *****
    Full Name  :
    Uid        : 1001
    Class      :
    Groups     : yournickname wheel
    Home       : /home/yournickname
    Home Mode  :
    Shell      : /bin/bash
    Locked     : no
    OK? (yes/no): yes
    adduser: INFO: Successfully added (yournickname) to the user database.
    Add another user? (yes/no): no
    Goodbye!

You can run at startup [sshd]:

`(chroot) root #``emerge -u net-misc/openssh `

`(chroot) root #``rc-update add sshd default `

##### [Special settings for ZFS]

When using the ZFS file system, the following additional work is required:

`(chroot) root #``rc-update add zfs boot `

`(chroot) root #``rc-update add zvol default `

`(chroot) root #``echo 'zfs_load="YES"' >> /boot/loader.conf `

`(chroot) root #``echo 'vfs.root.mountfrom="zfs:zsys/root"' >> /boot/loader.conf `

##### [Special settings for virtual machine]

When installing on a virtual machine, the following additional configuration is required:

`(chroot) root #``echo 'kern.hz=100' >> /boot/loader.conf `

#### [Installing the required packages]

To use DHCP, [[[net-misc/dhcpcd]](https://packages.gentoo.org/packages/net-misc/dhcpcd)[]] is required:

`(chroot) root #``emerge net-misc/dhcpcd `

#### [Installing the boot loader]

Install a boot loader to boot the Gentoo FreeBSD:

`(chroot) root #``emerge sys-freebsd/boot0 `

Please see [this section](https://wiki.gentoo.org/wiki/Gentoo_FreeBSD/Experimental#How_to_use_sys-boot.2Fgrub2 "Gentoo FreeBSD/Experimental") if you want to use GRUB2. But it is experimental!

#### [Setting boot loader]

Let\'s prepare for using [[[sys-freebsd/boot0]](https://packages.gentoo.org/packages/sys-freebsd/boot0)[]].

If you select UFS2 (GPT):

`(chroot) root #``gpart bootcode -b /boot/pmbr ada0 `

`(chroot) root #``gpart bootcode -p /boot/gptboot -i 1 ada0 `

If you select UFS2 (MBR):

`(chroot) root #``gpart bootcode -b /boot/boot0 ada0 `

`(chroot) root #``gpart bootcode -b /boot/boot ada0s1 `

If you select ZFS (GPT):

`(chroot) root #``gpart bootcode -b /boot/pmbr ada0 `

`(chroot) root #``gpart bootcode -p /boot/gptzfsboot -i 1 ada0 `

#### [Exiting the chroot]

Exit from the chroot environment:

`(chroot) root #``exit `

### [Cleaning up and setting the remaining]

Do you want to reboot now? Just a minute. ZFS users must make few more setting changes.

#### [Special settings for ZFS]

If you select ZFS file system, the following additional work is required.

`root `[`#`]`umount /mnt/dev `

`root `[`#`]`cd / `

`root `[`#`]`zpool set bootfs=zsys/root zsys `

`root `[`#`]`zpool export zsys `

`root `[`#`]`gnop destroy /dev/gpt/zfs-system.nop (please run if you are using gnop)`

`root `[`#`]`zpool import zsys `

`root `[`#`]`mkdir /mnt/boot/zfs `

`root `[`#`]`cp /boot/zfs/zpool.cache /mnt/boot/zfs/ `

`root `[`#`]`zfs unmount -a`

`root `[`#`]`zfs set mountpoint=none zsys `

`root `[`#`]`zfs set mountpoint=/usr zsys/root/usr `

`root `[`#`]`zfs set mountpoint=/var zsys/root/var `

`root `[`#`]`zfs set mountpoint=/tmp zsys/root/tmp `

`root `[`#`]`zfs set mountpoint=/home zsys/home `

`root `[`#`]`zfs set mountpoint=legacy zsys/root`

#### [][Reboot!]

No problems? You can now reboot. Don\'t forget to remove the installation media.

`root `[`#`]`shutdown -r now`

## [][Running Gentoo FBSD in vanilla FreeBSD\'s jail]

Details of jail, please see the [FreeBSD Handbook](https://www.freebsd.org/handbook/jails.html).

### [Preparing directory]

`root `[`#`]`mkdir -p /usr/jail/gfbsd `

`root `[`#`]`cd /usr/jail/gfbsd`

### [Downloading and unpacking the stage 3 file and Portage snapshot]

`root `[`#`]`fetch `[`http://dev.gentoo.org/~aballier/fbsd9.0/x86/stage3-i686-freebsd-9.0.tar.bz2`](http://dev.gentoo.org/~aballier/fbsd9.0/x86/stage3-i686-freebsd-9.0.tar.bz2)` (for x86-fbsd users) `

`root `[`#`]`fetch `[`http://distfiles.gentoo.org/experimental/bsd/freebsd/stages/amd64-fbsd-9.1/stage3-amd64-freebsd-9.1.tar.bz2`](http://distfiles.gentoo.org/experimental/bsd/freebsd/stages/amd64-fbsd-9.1/stage3-amd64-freebsd-9.1.tar.bz2)` (for amd64-fbsd users) `

`root `[`#`]`fetch `[`http://distfiles.gentoo.org/snapshots/portage-latest.tar.bz2`](http://distfiles.gentoo.org/snapshots/portage-latest.tar.bz2)` `

`root `[`#`]`tar xjpf stage3-*.tar.bz2 `

`root `[`#`]`tar xjf portage-latest.tar.bz2 -C /usr/jail/gfbsd/usr `

### [Setting]

Configure the jail to start with FreeBSD:

[FILE] **`/etc/rc.conf`Example for starting the jail at boot time**

    jail_enable="YES"
    jail_list="gfbsd"

    jail_gfbsd_rootdir="/usr/jail/gfbsd"
    jail_gfbsd_hostname="gfbsd.example.org"
    jail_gfbsd_devfs_enable="YES"

    # You will need to add the following line if you want network access.
    # Please specify your network devices instead of em0.
    jail_gfbsd_interface="em0"
    jail_gfbsd_ip="192.168.0.10"

Setting to operate Gentoo/FreeBSD in the jail:

`root `[`#`]`echo 'rc_sys="jail"' >> /usr/jail/gfbsd/etc/rc.conf `

`root `[`#`]`echo 'hostname="gfbsd"' > /usr/jail/gfbsd/etc/conf.d/hostname `

`root `[`#`]`echo 'syslogd_args="-ss"' >> /usr/jail/gfbsd/etc/conf.d/syslogd`

`root `[`#`]`chroot /usr/jail/gfbsd /bin/bash`

`(chroot) root #``rc-update add vixie-cron default `

`(chroot) root #``exit `

### [Run jail]

Run jail:

`root `[`#`]`/etc/rc.d/jail start`

You can check that it worked:

`root `[`#`]`jls`

       JID  IP Address      Hostname                      Path
         1  192.168.0.10    gfbsd                         /usr/jail/gfbsd

Enter the jail environment with the [jexec] command:

`root `[`#`]`jexec 1 /bin/bash`

## [][Developing for Gentoo/FreeBSD]

### [How to help]

There are many things you could help with, depending on one\'s skill level and spare time:

-   Working on current ebuilds: this means working closely with ebuild maintainers in order to create patches or modify ebuilds in a way that can be accepted into the Gentoo ebuild repository.
-   Security: if you are into security, we need you! Although security advisories from the FreeBSD project are tracked and fixed, we can always use help in this area.
-   Contacts: we need people who can get in touch with FreeBSD developers to maintain contacts between us and the original project to exchange patches and discuss various problems and their solutions. Note that this should never involve any kind of spamming of mailing lists or IRC channels.
-   Testing: the more people are actively using Gentoo FreeBSD, the more bugs will be discovered, which helps us improving the quality of the port. If you are good at describing bugs or problems, we definitely want to hear from you.
-   Other areas where we need help include: system ebuilds, creation of installation CDs, documentation, kernel hacking.

## [Troubleshooting]

### [Architecture independent issues]

#### [][Emerge fails app-misc/screen]

For details see [[[bug #393039]](https://bugs.gentoo.org/show_bug.cgi?id=393039)[]] and [[[bug #409819]](https://bugs.gentoo.org/show_bug.cgi?id=409819)[]].

Please use [[[app-misc/tmux]](https://packages.gentoo.org/packages/app-misc/tmux)[]] instead of [[[app-misc/screen]](https://packages.gentoo.org/packages/app-misc/screen)[]].

#### [lex: not found]

`root `[`#`]`emerge --ask sys-devel/flex`

#### [cc: not found]

For details see [[[bug #412319]](https://bugs.gentoo.org/show_bug.cgi?id=412319)[]]:

`root `[`#`]`emerge '>=sys-devel/gcc-config-1.7.1'`

## [Contacts]

-   gentoo-bsd mailing list ([Gentoo Mailing Lists](https://archives.gentoo.org/gentoo-bsd/))
-   IRC channel [[#gentoo-bsd](ircs://irc.libera.chat/#gentoo-bsd)] ([[webchat](https://web.libera.chat/#gentoo-bsd)]) on ~~Freenode~~ Libera Chat ([Gentoo Linux IRC channels list](https://gentoo.org/get-involved/irc-channels/all-channels.html))

## [See also]

-   [Gentoo FreeBSD/Upgrade Guide](https://wiki.gentoo.org/wiki/Gentoo_FreeBSD/Upgrade_Guide "Gentoo FreeBSD/Upgrade Guide") - A sub-article on upgrading a G/FBSD system.
-   [Gentoo FreeBSD/Experimental](https://wiki.gentoo.org/wiki/Gentoo_FreeBSD/Experimental "Gentoo FreeBSD/Experimental") - A sub-article that contains attempts to implement some uncommon features.
-   [Gentoo FreeBSD/Developers Note](https://wiki.gentoo.org/wiki/Gentoo_FreeBSD/Developers_Note "Gentoo FreeBSD/Developers Note") - A sub-article of developers note.
-   [Gentoo Alt/Contributor\'s Guide](https://wiki.gentoo.org/wiki/Gentoo_Alt/Contributor%27s_Guide "Gentoo Alt/Contributor's Guide") - A Gentoo Alt contributor\'s guide (deprecated).
-   [Project:Gentoo/Staffing_Needs](https://wiki.gentoo.org/wiki/Project:Gentoo/Staffing_Needs "Project:Gentoo/Staffing Needs") - An article that lists the ways users can help.
-   [Gentoo Linux Handbook](https://wiki.gentoo.org/wiki/Handbook:Main_Page "Handbook:Main Page")

## [External resources]

-   [FreeBSD Handbook](https://www.freebsd.org/handbook/)
-   [FreeBSD Man Pages](https://www.freebsd.org/cgi/man.cgi)
-   [ZFSTuningGuide - FreeBSD Wiki](https://wiki.freebsd.org/ZFSTuningGuide)
-   [FreeBSD Wiki](https://wiki.freebsd.org/)

\

Authorship information[]

This page is based on a document formerly found on [gentoo.org](https://www.gentoo.org/).\
The following people contributed to the original document: **Ignacio Arque-Latour, Michael Kohl, Otavio R. Piske, Aaron Walker, Chris White, , , Camille Huot, [Francisco Blas Izquierdo Riera (klondike)](https://wiki.gentoo.org/wiki/User:Klondike "User:Klondike") **\
\
*[Editors: please do **not** add yourself here. Contributions are recorded on each article\'s associated history page, this list is only present to preserve authorship information, as wiki history does not allow for any external attribution.]*