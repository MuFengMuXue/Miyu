\

**Resources**

[[]][Wikipedia](https://en.wikipedia.org/wiki/HFS_Plus "wikipedia:HFS Plus")

The [filesystem](https://wiki.gentoo.org/wiki/Filesystem "Filesystem") **HFS+**, also *HFS Plus* or *Extended [Hierarchical File System](https://wiki.gentoo.org/wiki/HFS "HFS")*, is the native filesystem of Mac OS 8.1+ and Mac OS X up to 10.12 Sierra from Apple for Mac computers. It is per design case-insensitive, but there is an optional case-sensitive variant as well.

Mac OS X is a Unix-based operating system with a BSD core. Up to Version 10.5 Leopard it can run on PowerPC and starting from Version 10.4 Tiger it runs on x86. It was renamed to OS X with version 10.8 Mountain Lion and to macOS with version 10.12 Sierra, which is the last to use HFS+ as the primary filesystem of the base installation. Its successor is APFS.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [Kernel]](#Kernel)
    -   [[1.2] [Emerge]](#Emerge)
        -   [[1.2.1] [diskdev_cmds]](#diskdev_cmds)
        -   [[1.2.2] [hfsplusutils]](#hfsplusutils)
-   [[2] [See also]](#See_also)
-   [[3] [References]](#References)

## [Installation]

### [Kernel]

[KERNEL] **Enable HFS+ support (`CONFIG_HFSPLUS_FS`)**

    File systems  --->
       Miscellaneous Filesystems  --->
          < > Apple Macintosh file system support
          <M> Apple Extended HFS file system support
       -*- Native language support  --->
          (utf8) Default NLS Option
          <M>   Codepage macroman
             NLS UTF-8

** Note**\
The filesystem driver does not support journaled HFS+. Since the journal is actually just a special file on the HFS+ volume, it will be mounted read-only if a journal is present. Use `-o force` to mount a journaled HFS+ volume read/write at your own risk!

On PowerPC-based Macs it is recommended to also select support for the Apple Partition Map (APM), on Intel-based Macs the GUID Partition Table (GPT) is used.

[KERNEL] **Enable APM and GPT support (`CONFIG_MAC_PARTITION`, `CONFIG_MSDOS_PARTITION` and `CONFIG_EFI_PARTITION`)**

    Enable the block layer  --->
       Partition Types  --->
          [*] Macintosh partition map support
          [*] PC BIOS (MSDOS partition tables) support
          [*] EFI GUID Partition support

** Note**\
External devices such as USB or FireWire enclosed Hard Disk Drives can use any partition table with the HFS+ filesystem. Common is APM (Apple Partition Map, \"Macintosh\"), MBR (Master Boot Record, \"PC BIOS\") and GPT (GUID Partition Table).

### [Emerge]

#### [diskdev_cmds]

The [[[sys-fs/diskdev_cmds]](https://packages.gentoo.org/packages/sys-fs/diskdev_cmds)[]] package is a port of HFS/HFS+ utilities from OpenDarwin, the BSD core operating system of macOS (formally Mac OS X). It includes the [mkfs] and [fsck] userspace utilities.

`root `[`#`]`emerge --ask sys-fs/diskdev_cmds`

The commands have names common to OpenDarwin: [newfs_hfs] and [fsck_hfs]. The package creates symlinks to [mkfs.hfsplus] and [fsck.hfsplus]. To create a new filesystem on a partition, e.g. on [/dev/sda2], use:

`root `[`#`]`newfs_hfs /dev/sda2`

** Warning**\
Creating a new filesystem will delete all data on the specified partition! Be **very sure** about the specified device file! (E.g. [/dev/sda2])

** Note**\
[newfs_hfs] is able to create a [HFS](https://wiki.gentoo.org/wiki/HFS "HFS") and a HFS+ filesystem. With the option -w it can also add a HFS wrapper to a HFS+ partition. Other options include -v \"Volume Label\". See the [[[newfs_hfs(8)]](https://man.archlinux.org/man/newfs_hfs.8.en)[[]](https://wiki.gentoo.org/wiki/Special:MyLanguage/man_page "Special:MyLanguage/man page")] manpage for more information.

#### [hfsplusutils]

The [[[sys-fs/hfsplusutils]](https://packages.gentoo.org/packages/sys-fs/hfsplusutils)[]] package was traditionally used on PowerPC based Macs. It provides utilities similar to those for [HFS](https://wiki.gentoo.org/wiki/HFS "HFS") from the [[[sys-fs/hfsutils]](https://packages.gentoo.org/packages/sys-fs/hfsutils)[]] package.

`root `[`#`]`emerge --ask sys-fs/hfsplusutils`

With [[[sys-fs/hfsplusutils]](https://packages.gentoo.org/packages/sys-fs/hfsplusutils)[]] a filesystem isn\'t mounted as part of [/], instead the provided utilities allow limited access to the filesystem.

`root `[`#`]`mac-fdisk -l /dev/sda `

    /dev/sda
            #                    type name                  length   base      ( size )  system
    /dev/sda1     Apple_partition_map Apple                     63 @ 1         ( 31.5k)  Partition map
    /dev/sda2              Apple_Boot NewWorld Bootblock   1286080 @ 64        (628.0M)  Unknown
    /dev/sda3              Apple_Free Extra                1073152 @ 1286144   (524.0M)  Free space
    /dev/sda4               Apple_HFS Tiger              209715200 @ 2359296   (100.0G)  HFS
    ...

** Note**\
On PowerPC Macs with Apple Partition Map, both HFS and HFS+ filesystems are type Apple_HFS. Special partitions, such as case-sensitive HFS+ or Software-RAID partitions, will be Apple_HFSX.

** Note**\
Some HFS+ partitions have a [HFS](https://wiki.gentoo.org/wiki/HFS "HFS") wrapper partition for compatibility reasons which cannot be used.

Select the partition with [hpmount]:

`root `[`#`]`hpmount /dev/sda4`

On the selected partition, the commands [hp\[ls\|pwd\|mkdir\|cd\|copy\|rm\]] can be used for file operations, instead of Unix \"/\" for directories the colon \":\" has to be used. E.g. [/dir/to/file] will be [:dir:to:file] for the specified commands.

`root `[`#`]`hpls`

    Apple Extras     Desktop Folder   Develop

The partition is released with the [hpumount] utility.

`root `[`#`]`hpumount /dev/sda4`

** Note**\
For further help refer to the manpage ([man 1 hfsp]).

## [See also]

-   [HFS](https://wiki.gentoo.org/wiki/HFS "HFS") --- the native filesystem of the Apple Macintosh and its operating system up to Mac OS 8.
-   [Filesystem](https://wiki.gentoo.org/wiki/Filesystem "Filesystem") --- a means to organize data to be retained after a program terminates.
-   [Mount](https://wiki.gentoo.org/wiki/Mount "Mount") --- the attaching of an additional [filesystem](https://wiki.gentoo.org/wiki/Filesystem "Filesystem") to the currently accessible filesystem of a computer.
-   [Removable media](https://wiki.gentoo.org/wiki/Removable_media "Removable media") --- any media that is easily removed from a system.
-   [/etc/fstab](https://wiki.gentoo.org/wiki//etc/fstab "/etc/fstab") --- a configuration file that defines how and where the main [filesystems](https://wiki.gentoo.org/wiki/Filesystem "Filesystem") are to be mounted, especially at boot time.

\

## [References]