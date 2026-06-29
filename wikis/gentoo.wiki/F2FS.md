Other languages:

-   [English]
-   [français](https://wiki.gentoo.org/wiki/F2FS/fr "F2FS (92% translated)")
-   [italiano](https://wiki.gentoo.org/wiki/F2FS/it "F2FS (72% translated)")
-   [magyar](https://wiki.gentoo.org/wiki/F2FS/hu "F2FS (96% translated)")
-   [中文（中国大陆）‎](https://wiki.gentoo.org/wiki/F2FS/zh-cn "F2FS (60% translated)")
-   [日本語](https://wiki.gentoo.org/wiki/F2FS/ja "F2FS (100% translated)")

**Resources**

[[]][Wikipedia](https://en.wikipedia.org/wiki/F2FS "wikipedia:F2FS")

[[]][GitWeb](https://git.kernel.org/cgit/linux/kernel/git/stable/linux-stable.git/tree/fs/f2fs)

[[]][Official documentation](https://git.kernel.org/pub/scm/linux/kernel/git/stable/linux.git/tree/Documentation/filesystems/f2fs.rst)

**F2FS** (**F**lash-**F**riendly **F**ile **S**ystem) is a [filesystem](https://wiki.gentoo.org/wiki/Filesystem "Filesystem") designed for NAND flash-based devices. It is available in Linux [kernels](https://wiki.gentoo.org/wiki/Kernel "Kernel") 3.8.x and higher. This filesystem is a good choice when installing Gentoo on an eMMC, [SSD](https://wiki.gentoo.org/wiki/SSD "SSD"), [SDCard](https://wiki.gentoo.org/wiki/SDCard "SDCard"), or a flash-based USB device.

** Note**\
F2FS is potentially useful for \"dumb\" flash storage (like USB thumb drives) if interoperability with other operating systems is not required. Modern SSDs might be better off with [ext4](https://wiki.gentoo.org/wiki/Ext4 "Ext4") or [xfs](https://wiki.gentoo.org/wiki/Xfs "Xfs"). [See the debate here](https://forums.gentoo.org/viewtopic-t-1130286.html).

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [Kernel]](#Kernel)
    -   [[1.2] [Emerge]](#Emerge)
-   [[2] [Usage]](#Usage)
    -   [[2.1] [Creation]](#Creation)
    -   [[2.2] [Filesystem check]](#Filesystem_check)
    -   [[2.3] [Defragmentation]](#Defragmentation)
-   [[3] [See also]](#See_also)
-   [[4] [External resources]](#External_resources)

## [Installation]

### [Kernel]

[KERNEL] **Enabling basic F2FS filesystem options**

    File systems  --->
       <*> F2FS filesystem support
       [ ]   F2FS Status Information
       [*]   F2FS extended attributes
       [*]     F2FS Access Control Lists
       [*]     F2FS Security Labels
       [ ]   F2FS consistency checking feature
       [ ]   F2FS fault injection facility
       [*]   F2FS compression feature
       [*]     LZO compression support
       [*]       LZO-RLE compression support
       [*]     LZ4 compression support
       [*]       LZ4HC compression support
       [*]     ZSTD compression support
       [*]   F2FS IO statistics information
       [ ]   F2FS unfair rw_semaphore

When enabling support to the filesystem in the Linux kernel, it is wise to enable at least \"F2FS extended attributes\" (`F2FS_FS_XATTR`) with \"F2FS Access Control Lists\" (`CONFIG_F2FS_FS_POSIX_ACL`) and \"F2FS Security Labels\" (`CONFIG_F2FS_FS_SECURITY`) suboptions.

\"F2FS consistency checking feature\" (`CONFIG_F2FS_CHECK_FS`) option in the list will enable F2FS\'s filesystem consistency checking. The checking will occur during run time and will decrease the filesystem\'s performance. This option provides an advantage when consistency is more important than speed.

### [Emerge]

Install the userspace tools for the F2FS filesystem:

`root `[`#`]`emerge --ask sys-fs/f2fs-tools`

## [Usage]

### [Creation]

After emerging the userspace tools, create a filesystem by running the [mkfs.f2fs] command followed by the appropriate device and partition number:

** Warning**\
In this example, the device /dev/sdd is used, and it\'s final target (the partition to format with F2FS) is 1 (so, /dev/sdd1). **This is unlikely to be the same device once it\'s connected on the computer** (/dev/sdd1), being aware that **formatting the wrong device will destroy all the data within** is very important ! Users has to be sure to target the proper partition on the proper device.

`root `[`#`]`mkfs.f2fs /dev/sdd1`

### [Filesystem check]

`root `[`#`]`fsck.f2fs /dev/sdd1`

### [Defragmentation]

`root `[`#`]`defrag.f2fs`

## [See also]

-   [Ext4](https://wiki.gentoo.org/wiki/Ext4 "Ext4") --- an open source disk [filesystem](https://wiki.gentoo.org/wiki/Filesystem "Filesystem") and the most recent version of the extended series of filesystems.
-   [Btrfs](https://wiki.gentoo.org/wiki/Btrfs "Btrfs") --- a copy-on-write (CoW) [filesystem](https://wiki.gentoo.org/wiki/Filesystem "Filesystem") for Linux aimed at implementing advanced features while focusing on fault tolerance, self-healing properties, and easy administration.
-   [SquashFS](https://wiki.gentoo.org/wiki/SquashFS "SquashFS") --- an open source, read only, extremely compressible filesystem.

## [External resources]

-   [F2FS (elinux.org)](https://elinux.org/F2FS)
-   [F2FS on wiki.kernel.org](https://f2fs.wiki.kernel.org/)