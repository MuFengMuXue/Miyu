This page contains [[changes](https://wiki.gentoo.org/index.php?title=ExFAT&oldid=1221869&diff=1420589)] which are not marked for translation.

Other languages:

-   [Deutsch](https://wiki.gentoo.org/wiki/ExFAT/de "ExFAT (57% translated)")
-   [English]
-   [magyar](https://wiki.gentoo.org/wiki/ExFAT/hu "exFAT (100% translated)")
-   [polski](https://wiki.gentoo.org/wiki/ExFAT/pl "ExFAT (51% translated)")
-   [русский](https://wiki.gentoo.org/wiki/ExFAT/ru "ExFAT (100% translated)")
-   [中文（中国大陆）‎](https://wiki.gentoo.org/wiki/ExFAT/zh-cn "ExFAT (100% translated)")
-   [日本語](https://wiki.gentoo.org/wiki/ExFAT/ja "exFAT (100% translated)")

**Resources**

[[]][Wikipedia](https://en.wikipedia.org/wiki/exFAT "wikipedia:exFAT")

[[]][GitHub](https://github.com/relan/exfat)

exFAT (**Ex**tended **F**ile **A**llocation **T**able), a Microsoft file system optimized for flash memory storage such as USB sticks, is available to Gentoo Linux systems through a [FUSE](https://wiki.gentoo.org/wiki/Filesystem_in_Userspace "Filesystem in Userspace") module.

The availability of the exFAT filesystem had long been poor, because of its proprietary, unpublished specification. The situation, however, was improved after release of Linux kernel 5.7 with native exFAT driver implementation.^[\[1\]](#cite_note-1)^

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [Kernel]](#Kernel)
        -   [[1.1.1] [Kernel 5.7 and above]](#Kernel_5.7_and_above)
        -   [[1.1.2] [FUSE system for earlier kernels]](#FUSE_system_for_earlier_kernels)
    -   [[1.2] [Emerge]](#Emerge)
        -   [[1.2.1] [Kernel 5.7 and above]](#Kernel_5.7_and_above_2)
        -   [[1.2.2] [FUSE system for earlier kernels]](#FUSE_system_for_earlier_kernels_2)
-   [[2] [Usage]](#Usage)
    -   [[2.1] [Formatting]](#Formatting)
        -   [[2.1.1] [Kernel 5.7 and above]](#Kernel_5.7_and_above_3)
        -   [[2.1.2] [FUSE system for earlier kernels]](#FUSE_system_for_earlier_kernels_3)
    -   [[2.2] [Mounting]](#Mounting)
        -   [[2.2.1] [Kernel 5.7 and above]](#Kernel_5.7_and_above_4)
        -   [[2.2.2] [FUSE system for earlier kernels]](#FUSE_system_for_earlier_kernels_4)
    -   [[2.3] [Integrity checking]](#Integrity_checking)
-   [[3] [See also]](#See_also)
-   [[4] [References]](#References)

## [Installation]

### [Kernel]

#### [Kernel 5.7 and above]

Enable exFAT support in the kernel:

[KERNEL] **Enable support for CONFIG_EXFAT_FS**

    File systems  --->
       DOS/FAT/EXFAT/NT Filesystems  --->
          <*> exFAT filesystem support

#### [FUSE system for earlier kernels]

Make sure support for Filesystem in Userspace (FUSE) is enabled in the kernel:

[KERNEL] **Enable support for CONFIG_FUSE_FS**

    File systems  --->
       <*> FUSE (Filesystem in Userspace) support

### [Emerge]

#### [Kernel 5.7 and above]

Install the [[[sys-fs/exfatprogs]](https://packages.gentoo.org/packages/sys-fs/exfatprogs)[]] package:

`root `[`#`]`emerge --ask sys-fs/exfatprogs`

#### [FUSE system for earlier kernels]

Install the FUSE exfat package:

`root `[`#`]`emerge --ask sys-fs/fuse-exfat`

For filesystem creation and manipulation beyond that of the [mount] command it is necessary to install the [[[sys-fs/exfat-utils]](https://packages.gentoo.org/packages/sys-fs/exfat-utils)[]] package:

`root `[`#`]`emerge --ask sys-fs/exfat-utils`

## [Usage]

### [Formatting]

#### [Kernel 5.7 and above]

To create an exFAT file system, use [mkfs.exfat]:

`user `[`$`]`mkfs.exfat`

    exfatprogs 1.0.4
    Usage: mkfs.exfat
            -L | --volume-label=label                              Set volume label
            -c | --cluster-size=size(or suffixed by 'K' or 'M')    Specify cluster size
            -b | --boundary-align=size(or suffixed by 'K' or 'M')  Specify boundary alignment
            -f | --full-format                                     Full format
            -V | --version                                         Show version
            -v | --verbose                                         Print debug
            -h | --help                                            Show help

For instance, to create it on a removable device present at [/dev/sde1] while assigning \"Flash\" as the file system label:

`root `[`#`]`mkfs.exfat -L Flash /dev/sde1`

#### [FUSE system for earlier kernels]

To create an exFAT file system, use [mkfs.exfat] (or the [mkexfatfs] command, which is synonymous):

`user `[`$`]`mkfs.exfat`

    mkexfatfs 1.2.1
    Usage: mkfs.exfat [-i volume-id] [-n label] [-p partition-first-sector] [-s sectors-per-cluster] [-V] <device>

For instance, to create it on a removable device present at [/dev/sde1] while assigning \"Flash\" as the file system label:

`root `[`#`]`mkfs.exfat -n Flash /dev/sde1`

### [Mounting]

#### [Kernel 5.7 and above]

With native support, standard mount commands work perfectly:

`root `[`#`]`mount /dev/sde1 /mnt/flash`

#### [FUSE system for earlier kernels]

The file system can then be mounted using the [mount.exfat-fuse] command:

`root `[`#`]`mount.exfat-fuse`

    FUSE exfat 1.0.1
    Usage: mount.exfat-fuse [-d] [-o options] [-v] <device> <dir>

For instance, to mount the file system created in the above example:

`root `[`#`]`mount.exfat-fuse /dev/sde1 /mnt/flash`

To unmount, simply use the [umount] command:

`root `[`#`]`umount /mnt/flash`

### [Integrity checking]

To check the integrity of an exFAT filesystem, use [fsck.exfat]:

`root `[`#`]`fsck.exfat /dev/sde1`

## [See also]

-   [FAT](https://wiki.gentoo.org/wiki/FAT "FAT") --- [filesystem](https://wiki.gentoo.org/wiki/Filesystem "Filesystem") originally created for use with MS-DOS (and later pre-NT Microsoft Windows).
-   [NTFS](https://wiki.gentoo.org/wiki/NTFS "NTFS") --- a proprietary disk [filesystem](https://wiki.gentoo.org/wiki/Filesystem "Filesystem") by Microsoft for Windows (NT-based) and WindowsNT-based operating systems.
-   [Ext4](https://wiki.gentoo.org/wiki/Ext4 "Ext4") --- an open source disk [filesystem](https://wiki.gentoo.org/wiki/Filesystem "Filesystem") and the most recent version of the extended series of filesystems.

## [References]

1.  [[[↑](#cite_ref-1)] [[New features of Linux 5.7](https://kernelnewbies.org/Linux_5.7#New_exFAT_file_system)]]