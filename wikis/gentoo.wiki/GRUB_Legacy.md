**[] Archived article**\
\
This article is **archived (obsolete)**. Contents are surely incorrect for current usage, and are intended for historical reference only.

GRUB Legacy was [removed](https://gitweb.gentoo.org/repo/gentoo.git/commit/sys-boot/grub?id=65be92768fab88a84a8cc05eea53fc9b67384c8b) from the [Gentoo ebuild repository](https://wiki.gentoo.org/wiki/Ebuild_repository#The_Gentoo_ebuild_repository "Ebuild repository"). [[[sys-boot/grub]](https://packages.gentoo.org/packages/sys-boot/grub)[]] is now the only available version of grub in ::gentoo. For up to date information, take a look at [GRUB](https://wiki.gentoo.org/wiki/GRUB "GRUB") page. To migrate a system that still uses GRUB legacy, see [GRUB2 Migration](https://wiki.gentoo.org/wiki/GRUB2_Migration "GRUB2 Migration").

\
TLDR: **Do not use this article!**

\

**Resources**

[[]][Home](http://www.gnu.org/software/grub/grub-legacy.html)

[[]][Wikipedia](https://en.wikipedia.org/wiki/GNU_GRUB#GRUB_version_1_.28GRUB_legacy.29 "wikipedia:GNU GRUB")

[[]][Official documentation](http://gnu.org/software/grub/manual/legacy/)

**GRUB** (**GR**and **U**nified **B**ootloader), also known as **GRUB Legacy** or GRUB version 1, was previously recommended by the [Handbook](https://wiki.gentoo.org/wiki/Handbook "Handbook") as Gentoo\'s default [bootloader](https://wiki.gentoo.org/wiki/Bootloader "Bootloader") on **[x86]** and **[amd64]** architectures. Currently the only way to emerge package is to [recover ebuild](https://gitweb.gentoo.org/repo/gentoo.git/tree/sys-boot/grub/grub-0.97-r18.ebuild?id=51c905af544411c486f1fea821742384c22b17ef) (and patch it since grub-0.97-patches-1.15.tar.bz2 do not exist any more). Alternatively may be it is possible find maintained version in some overlay. Also note that it was not possible to emerge GRUB Legacy on [amd64 systems without multilib](https://archives.gentoo.org/gentoo-dev/message/5665a75401fde06b7113066ce8a43a6c), it\'s necessary to have 32 bit glibc to compile it.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
-   [[2] [Configuration]](#Configuration)
    -   [[2.1] [Considerations]](#Considerations)
    -   [[2.2] [USB disks]](#USB_disks)
    -   [[2.3] [Using LABEL or UUID]](#Using_LABEL_or_UUID)
-   [[3] [See also]](#See_also)

## [Installation]

### [USE flags]

Latest version of ebuild as removed on February 08 2018 was [0.97-r18](https://gitweb.gentoo.org/repo/gentoo.git/tree/sys-boot/grub/grub-0.97-r18.ebuild?id=51c905af544411c486f1fea821742384c22b17ef). It respected the following USE flags:

-   [custom-cflags](https://packages.gentoo.org/useflags/custom-cflags) -- Build with user-specified CFLAGS (unsupported)
-   [ncurses](https://packages.gentoo.org/useflags/ncurses) -- Add ncurses support (console display library)
-   [netboot](https://packages.gentoo.org/useflags/netboot) -- Enable network booting
-   [static](https://packages.gentoo.org/useflags/static) -- !!do not set this during bootstrap!! Causes binaries to be statically linked instead of dynamically

### [Emerge]

Grub 2 is in SLOT 0 now, so you\'ll need to work with that like:

`root `[`#`]`emerge --ask =sys-boot/grub-0.97-r18`

## [Configuration]

### [Considerations]

Hard drive numbering starts from 0. Unlike [GRUB](https://wiki.gentoo.org/wiki/GRUB "GRUB"), in GRUB Legacy *partition* numbering also starts at 0.

Instead of installing GRUB in the MBR, it is possible to install to a partition.

GRUB gets boot information from the BIOS, and can chainload other boot loaders, even if Linux can\'t see them. An example is a BIOS supported software RAID. When a physical drive is set up as 2 logical drives, the second logical drive starts in the middle of the physical drives. Without dmraid, Linux does not see that second logical drive. But GRUB can chainload Windows on it.

If installing Windows and Linux on a computer with two drives, it may be desirable to install each OS on one of the disks. Before installing, change the boot order in the BIOS. After installation, make the Windows disk the second disk and use GRUB to chainload it. This way, by reinstalling Windows, the MBR of the first disk will not get affected and if GRUB can\'t boot, it is still possible to boot Windows by changing the boot order in the BIOS.

When chainloading Windows, GRUB needs to know the active Windows partition, which is not always the same as the partition which Windows labels as the *startpartition*.

### [USB disks]

The key to understand GRUB is to remember, in what environment GRUB is running.

Suppose there are 3 internal SATA disks. A Gentoo is running on them and the goal is to install GRUB now on an external USB hard disk to boot a version of Gentoo, which is installed on the second partition of the USB disk.

The Linux system has the following device names:

-   [/dev/sda], [/dev/sdb] and [/dev/sdc]: internal drives
-   [/dev/sdd]: USB disk

The configuration of GRUB, which is read while booting, is stored in [/boot/grub/grub.conf]. [menu.lst] in the same directory is a symlink to [grub.conf].

The kernel and the Linux system of the USB drive is installed in [/dev/sdd2]. Following the example, now edit [/mnt/sdd2/boot/grub/grub.conf], if the mounted USB partition is on [/mnt/sdd2].

When GRUB boots from the USB disk, for GRUB itself it is the first hard disk. It should be written in [grub.conf]:

[FILE] **`grub.conf`**

    default 0
    timeout 10

    title gentoo USB
    root (hd0,1)
    kernel /boot/kernel-3.4.9 rootwait root=/dev/sdd2

In contrast, the kernel sees the USB disk as [/dev/sdd], the `root=` kernel parameter has to contain `/dev/sdd2`.

** Tip**\
The `rootwait` parameter can be passed so that the kernel will wait until the USB disk is ready. The same applies for the installation of GRUB.

Here pass GRUB the names, under which Linux sees it now. First chroot into [/mnt/sdd2]. Fire up GRUB, passing the root of the USB Linux with

`grub>``root (hd3,1) `

Then tell GRUB to install on the MBR of the USB disk with:

`grub>``setup (hd3) `

Consequence: To boot the USB disk, regardless of how many disks are installed, there is a requirement of using an initramfs or something else.

If the `root=` parameter doesn\'t match the actual configuration, all is not lost. It is possible to edit the lines before booting. How this can be done, is explained in [Knowledge Base:Adjusting GRUB settings for a single boot session](https://wiki.gentoo.org/wiki/Knowledge_Base:Adjusting_GRUB_settings_for_a_single_boot_session "Knowledge Base:Adjusting GRUB settings for a single boot session")

To get the USB disk boot without initramfs regardless of the number of installed disks, use a GPT partition table and the `root=PARTUUID=` kernel parameter as explained in this external link: [Mounting root partition by UUID (no initrd needed)](https://archives.gentoo.org/gentoo-user/message/35eb3187ef8be8a23cdec253b66b5a59)

Since kernel 3.8 and newer it is possible to use MBR 32-bit UUID, so it\'s possible to use a MBR partition table as well.

In this case PARTUUID refer to an MBR partition using the format SSSSSSSS-PP, where SSSSSSSS is a zero-filled hex representation of the 32-bit \"NT disk signature\", and PP is a zero-filled hex representation of the 1-based partition number.

To get \"NT disk signature\" one possibility is using fdisk:

`root `[`#`]`fdisk -l /dev/sdd`

The output will be something like `Disk identifier: 0x2d6b036c`, so assuming root partition is [/dev/sdd2], the resulting line will be `root=PARTUUID=2d6b036c-02`\
More info is available here: [Description of PARTUUID feature](http://lxr.linux.no/#linux+v3.8/init/do_mounts.c#L190)

### [Using LABEL or UUID]

Kernel boot parameters are `real_root=LABEL=` or `real_root=UUID=`.

Requires an [initramfs](https://wiki.gentoo.org/wiki/Initramfs "Initramfs").

Refer to [Install Gentoo on a bootable USB stick](https://wiki.gentoo.org/wiki/Install_Gentoo_on_a_bootable_USB_stick "Install Gentoo on a bootable USB stick") for examples using [[lilo](https://wiki.gentoo.org/wiki/Lilo "Lilo")] or [syslinux](https://wiki.gentoo.org/wiki/Syslinux "Syslinux").

## [See also]

-   [GRUB Error Reference](https://wiki.gentoo.org/wiki/GRUB_Error_Reference "GRUB Error Reference") --- list problems and errors that may occur in certain situations when using the *[GRUB Legacy]* bootloader.
-   [Adjusting GRUB settings for a single boot session](https://wiki.gentoo.org/wiki/Knowledge_Base:Adjusting_GRUB_settings_for_a_single_boot_session "Knowledge Base:Adjusting GRUB settings for a single boot session")
-   [Install Gentoo on a bootable USB stick](https://wiki.gentoo.org/wiki/Install_Gentoo_on_a_bootable_USB_stick "Install Gentoo on a bootable USB stick") --- describes how to install Gentoo onto a USB stick that can be booted on any computer.
-   [GRUB](https://wiki.gentoo.org/wiki/GRUB "GRUB") --- a multiboot secondary [bootloader](https://wiki.gentoo.org/wiki/Bootloader "Bootloader") capable of loading kernels from a variety of [filesystems](https://wiki.gentoo.org/wiki/Filesystem "Filesystem") on most system architectures.
-   [LILO](https://wiki.gentoo.org/wiki/LILO "LILO")