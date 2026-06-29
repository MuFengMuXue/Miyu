[] This article has been flagged for not conforming to the [wiki guidelines](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Guidelines "Gentoo Wiki:Guidelines"). Please [help Gentoo out](https://wiki.gentoo.org/wiki/Help_improve_Gentoo_by_getting_involved_with_documentation!#Make_articles_conform_to_the_guidelines "Help improve Gentoo by getting involved with documentation!") by starting fixing things.

**Resources**

[[]][Product Information](https://www.friendlyelec.com/index.php?route=product/product&product_id=279)

[[]][NanoPi](https://en.wikipedia.org/wiki/Nano_Pi "wikipedia:Nano Pi")

## Contents

-   [[1] [Gentoo for NanoPI Neo3]](#Gentoo_for_NanoPI_Neo3)
    -   [[1.1] [License]](#License)
    -   [[1.2] [Features List]](#Features_List)
    -   [[1.3] [Steps to install]](#Steps_to_install)
        -   [[1.3.1] [SDCard layout]](#SDCard_layout)
        -   [[1.3.2] [BOOT Partition]](#BOOT_Partition)
        -   [[1.3.3] [Setting up base system]](#Setting_up_base_system)
        -   [[1.3.4] [Creating a kernel]](#Creating_a_kernel)

## [Gentoo for NanoPI Neo3]

The NanoPI Neo3 is a tiny IoT offered by NanoPI having many more features than initially shown This document tries to guide you how to install Gentoo on a SD card, and boot a bare system on it. Probably you\'ll want to keep the crossdev live, as the cortex A53 chips are not really suited for recompiling the whole device. NanoPI R2S and Neo 3 are very very similar: they only differ by a few hw features, so this guide should be a good start for R2S too. This guide focuses on a minimal setup with all performance we could get, A53 chips are made for power-saving, not performance, and as such we need to use every feature that may be useful

### [License]

U-boot: GPL-2+ [https://github.com/01org/edison-u-boot](https://github.com/01org/edison-u-boot)

### [Features List]

-   working u-boot
-   booting
-   working kernel
-   able to build using crossdev
-   able to unlock special features not in standard dts
-   TODO: ddr controller

### [Steps to install]

1\. prepare the crossdev setup:

`root `[`#`]`emerge --ask crossdev`

`root `[`#`]`crossdev aarch64-unknown-linux-gnu`

Please note that it may be useful to add multilib support for ARMv8, as it \_may\_ allow armv7 code to compile. Also, I prefer to use custom cflags here, as the Rockchip RK3328 chip has SIMD + crypto extensions not defined in standard ARMv8-A.

In order to tune options for gcc, glibc, \...:

`root `[`#`]`echo "cross-aarch64-unknown-linux-gnu/glibc multilib custom-cfags" >> /etc/portage/package.use/crossdev`

`root `[`#`]`echo "cross-aarch64-unknown-linux-gnu/gcc multilib graphite lto" >> /etc/portage/package.use/crossdev`

other details could be found in [Embedded Handbook](https://wiki.gentoo.org/wiki/Embedded_Handbook "Embedded Handbook"), Run it until at compiling the kernel.

**Starting from below, all packages which are not in portage are fetched into /usr/aarch64-unknown-linux-gnu/tmp**

2\. Prepare U-BOOT

U-boot only contains an image for NanoPi R2S, which requires a few modifications to run properly. Also, fancy stuff like boot from pxe, etc .. makes no sense because the device needs an SDcard anyway. In order to compile everything, it could be useful to download the latest ARM firmware first:

[git clone https://github.com/ARM-software/arm-trusted-firmware](https://github.com/ARM-software/arm-trusted-firmware)

and then u-boot (may be useful to add -d 5 to limit the history): see [here](https://github.com/u-boot/u-boot) on github

[Embedded Handbook/Bootloaders/Das U-Boot](https://wiki.gentoo.org/wiki/Embedded_Handbook/Bootloaders/Das_U-Boot "Embedded Handbook/Bootloaders/Das U-Boot")

This is where it becomes tricky, in order to understand, The following boot steps are important:

1.  initial CPU start (onboard SRAM), search for MMC card block 0x40
2.  initial boot loader (U-BOOT) (also referenced as idbloader)
3.  Second program loader (U-BOOT) (setup initial devices, buses, and loads a primary device tree)
4.  Tertiary program loader (U-BOOT) (runs DDR setup)
5.  U-BOOT executable (U-BOOT) (somewhat comparable to EFI boot loader)
6.  Kernel loading

Previously, steps 2-5 all required separate files on separate partitions. This is no longer the case: u-boot generates an image \"u-boot-rockchip.bin\" which could be written to sector 0x40 of your SD card:

`root `[`#`]`dd if=u-boot-rockchip.bin of=/dev/sdd bs=512 seek=64`

Knowing this, the SDCard partition layout (using msdos here, but gpt should work as well) can be created. It is important to keep the order, size and start sector of the FAT32 boot partition. Other things like root fs, swap partition etc are not, and enjoy the flexibility of Gentoo OS.

##### [SDCard layout]

Sector size (logical/physical): 512 bytes / 512 bytes\
I/O size (minimum/optimal): 512 bytes / 512 bytes\
Disklabel type: dos\
Disk identifier: 0x31a5b84a\

Device Boot Start End Sectors Size Id Type\
/dev/sdd1 \* 32768 262143 229376 112M b W95 FAT32\
/dev/sdd2 262144 113246174 112984031 53.9G 83 Linux\
/dev/sdd3 113246175 121634815 8388641 4G 82 Linux swap / Solaris\

#### [BOOT Partition]

There are 2 ways U-BOOT can boot from the SDCard: 1. Using an exlinux config file 2. Using default UEFI image

It is possible to make U-BOOT load grub and configure it before booting the kernel, but the advantage of it is pretty minimal: if boot customization is required, use extlinux.\
`neo3 ~ # ls /boot`\
`efi extlinux rockchip`\
`neo3 ~ # ls /boot/efi/boot/`\
`bootaa64.efi`\
`neo3 ~ # ls /boot/extlinux`\
`extlinux.conf`\
`neo3 ~ # ls /boot/rockchip`\
`rk3328-nanopi-r2s.dtb`\

And for the extlinux.conf file:

\
`neo3 ~ # cat /boot/extlinux/extlinux.conf`\
`default gentoo`\
\
`label gentoo`\
`linux /efi/boot/bootaa64.efi`\
`fdt /rockchip/rk3328-nanopi-r2s.dtb`\
`append earlycon rootwait root=/dev/mmcblk1p2 rootfstype=ext4 init=/sbin/init netconsole=6666@192.168.178.35/eth0,6666@(ip of log server)/(mac of log server)`\

A little explanation about the layout here:

1.  the boot partition contains a default EFI folder (for the kernel image), an extlinux folder (for extlinux config), and a rockchip folder for the device tree, which is necessary to present the devices to the OS.
2.  the EFI partition has the kernel stored as bootaarch4.efi, which makes it the default boot image in case extlinux wouldn\'t work.
3.  rockchip folder contains the dtb file (a compiled dts file) which was generated while compiling u-boot / the linux kernel. It is located at (u-boot)/arch/arm/dts/, or use the default linux dts file in (linux source)/arch/arm64/boot/dts/
4.  In the extlinux folder, write something like explained above
    1.  Default image is gento
    2.  the kernel image is at \....
    3.  the fdt file is at \...
    4.  the kernel arguments are \.... it could be, depending on your DTS settings, that mmcblk1 or mmcblk0 is required: if the eMMC controller of the rockchip is enabled in DTS and thus in DTB, it will take first place, even though not specified. rootwait is required, as it is not guaranteed that the MMC controller is online when Linux tries to mount the root filesystem.
    5.  In this example, the netconsole is enabled. This is for debugging: when something goes wrong inside the kernel, it possible to perform some diagnosis using the logs here.

if no configuration is required, simply append the kernel arguments while compiling the kernel, but the dts magic may be a little more complicated.

#### [Setting up base system]

There are a number of \_essential\_ things that need to be verified before gentoo can boot:

1.  It must be able to mount root fs (see extlinux.conf layout above)
2.  It must be able to run init. This is a caveat: ARM setups tend to default to busybox, but it also replaces the /sbin/init with its own variant. This variant does not load /etc/inittab the way openrc init does. As such, due to these confusions, it is recommended to use init=/bin/openrc-init at kernel boot, or go for busybox all the way and remove openrc entirely

Using crossdev, a normal baselayout has already been fixed, but it\'s always useful to emerge it, even though already marked as \"installed\". Make sure every service that might be needed to bring up the devices is listed in /etc/runlevels. If not, a debug setup is required to run.

an example listing of /usr/aarch64/etc/init.d/sysinit

` /usr/aarch64-unknown-linux-gnu/etc/runlevels/sysinit:`\
`total 8`\
`drwxr-xr-x 2 root root 4096 Apr 7 07:24 .`\
`drwxr-xr-x 7 root root 4096 Mar 18 10:32 ..`\
`lrwxrwxrwx 1 root root 19 Apr 5 13:08 cgroups -> /etc/init.d/cgroups`\
`lrwxrwxrwx 1 root root 17 Apr 5 13:08 devfs -> /etc/init.d/devfs`\
`lrwxrwxrwx 1 root root 17 Apr 5 13:08 dmesg -> /etc/init.d/dmesg`\
`lrwxrwxrwx 1 root root 29 Mar 16 15:01 kmod-static-nodes -> /etc/init.d/kmod-static-nodes`\
`lrwxrwxrwx 1 root root 25 Mar 14 08:43 stmpfiles-dev -> /etc/init.d/stmpfiles-dev`\
`lrwxrwxrwx 1 root root 17 Apr 5 13:08 sysfs -> /etc/init.d/sysfs`\
`lrwxrwxrwx 1 root root 16 Mar 16 15:02 udev -> /etc/init.d/udev`\
`lrwxrwxrwx 1 root root 24 Mar 16 15:02 udev-trigger -> /etc/init.d/udev-trigger`\

and boot:

` /usr/aarch64-unknown-linux-gnu/etc/runlevels/boot:`\
`total 8`\
`drwxr-xr-x 2 root root 4096 Apr 7 07:24 .`\
`drwxr-xr-x 7 root root 4096 Mar 18 10:32 ..`\
`lrwxrwxrwx 1 root root 18 Apr 5 13:08 binfmt -> /etc/init.d/binfmt`\
`lrwxrwxrwx 1 root root 20 Apr 5 13:08 bootmisc -> /etc/init.d/bootmisc`\
`lrwxrwxrwx 1 root root 16 Apr 5 13:08 fsck -> /etc/init.d/fsck`\
`lrwxrwxrwx 1 root root 20 Apr 5 13:08 hostname -> /etc/init.d/hostname`\
`lrwxrwxrwx 1 root root 19 Apr 5 13:08 hwclock -> /etc/init.d/hwclock #not really useful, no "real" rtc is present`\
`lrwxrwxrwx 1 root root 19 Apr 5 13:08 keymaps -> /etc/init.d/keymaps # not really useful, there's no keyboard`\
`lrwxrwxrwx 1 root root 22 Apr 5 13:08 localmount -> /etc/init.d/localmount`\
`lrwxrwxrwx 1 root root 20 Apr 5 13:08 loopback -> /etc/init.d/loopback`\
`lrwxrwxrwx 1 root root 19 Apr 5 13:08 modules -> /etc/init.d/modules`\
`lrwxrwxrwx 1 root root 16 Apr 5 13:08 mtab -> /etc/init.d/mtab`\
`lrwxrwxrwx 1 root root 18 Apr 5 13:08 procfs -> /etc/init.d/procfs`\
`lrwxrwxrwx 1 root root 16 Apr 5 13:08 root -> /etc/init.d/root`\
`lrwxrwxrwx 1 root root 24 Apr 5 13:08 save-keymaps -> /etc/init.d/save-keymaps`\
`lrwxrwxrwx 1 root root 29 Apr 5 13:08 save-termencoding -> /etc/init.d/save-termencoding`\
`lrwxrwxrwx 1 root root 27 Mar 14 08:43 stmpfiles-setup -> /etc/init.d/stmpfiles-setup`\
`lrwxrwxrwx 1 root root 16 Apr 5 13:08 swap -> /etc/init.d/swap`\
`lrwxrwxrwx 1 root root 18 Apr 5 13:08 sysctl -> /etc/init.d/sysctl`\
`lrwxrwxrwx 1 root root 24 Apr 5 13:08 termencoding -> /etc/init.d/termencoding`\
`lrwxrwxrwx 1 root root 19 Apr 5 13:08 urandom -> /etc/init.d/urandom`\

And at last some defaults:

` /usr/aarch64-unknown-linux-gnu/etc/runlevels/default: total 8 drwxr-xr-x 2 root root 4096 Apr 20 10:27 .`\
`drwxr-xr-x 7 root root 4096 Mar 18 10:32 ..`\
`lrwxrwxrwx 1 root root 25 Apr 20 10:26 busybox-ntpd -> ../../init.d/busybox-ntpd`\
`lrwxrwxrwx 1 root root 28 Apr 20 10:26 busybox-syslogd -> ../../init.d/busybox-syslogd`\
`lrwxrwxrwx 1 root root 18 Apr 7 13:14 cronie -> /etc/init.d/cronie`\
`lrwxrwxrwx 1 root root 17 Apr 5 13:08 local -> /etc/init.d/local`\
`lrwxrwxrwx 1 root root 20 Apr 7 11:41 net.eth0 -> /etc/init.d/net.eth0`\
`lrwxrwxrwx 1 root root 16 Mar 16 14:58 sshd -> /etc/init.d/sshd`\
`lrwxrwxrwx 1 root root 18 Mar 16 14:58 xinetd -> /etc/init.d/xinetd`\

It is always a good idea to include both a telnet and ssh server: even though you don\'t need telnet or ssh, if the first one fails you could continue with the other one.\
The people constrained about the ram usage of ssh server or telnetd could use xinetd, but there should \_always\_ be a failover scenario in case xinetd fails.

#### [Creating a kernel]

Every kernel has a number of default config files.