[[]][Home](https://nilfs.sourceforge.io/en/index.html)

[[]][Package information](https://packages.gentoo.org/packages/sys-fs/nilfs-tools)

[[]][Wikipedia](https://en.wikipedia.org/wiki/NILFS "wikipedia:NILFS")

[[]][GitHub](https://github.com/nilfs-dev/nilfs-utils)

[[]][Bugs (upstream)](https://bug/tracker/url/)

**NILFS** is a New Implementation of Log-structured File System (LFS) that supports continuous snapshot taking. In addition to full file system versioning, this feature of NILFS allows users to restore accidentally deleted or overwritten files to their previous state. Like traditional LFS, NILFS can guarantee file system consistency after a system crash or unclean shutdown, and like journaling file systems, can quickly recover.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [Kernel]](#Kernel)
    -   [[1.2] [USE flags]](#USE_flags)
    -   [[1.3] [Emerge]](#Emerge)
-   [[2] [Usage]](#Usage)
    -   [[2.1] [Formatting a device]](#Formatting_a_device)
    -   [[2.2] [Checkpoints and snapshots]](#Checkpoints_and_snapshots)
        -   [[2.2.1] [Listing checkpoints]](#Listing_checkpoints)
        -   [[2.2.2] [Creating a checkpoint]](#Creating_a_checkpoint)
        -   [[2.2.3] [Creating a snapshot]](#Creating_a_snapshot)
        -   [[2.2.4] [Converting a checkpoint to a snapshot (and vice versa)]](#Converting_a_checkpoint_to_a_snapshot_.28and_vice_versa.29)
        -   [[2.2.5] [Mounting a snapshot]](#Mounting_a_snapshot)
-   [[3] [See also]](#See_also)

## [Installation]

### [Kernel]

[KERNEL]

    File Systems --->
      <M/*> NILFS2 file system support Search for <code>CONFIG_NILFS2_FS</code> to find this item.

### [USE flags]

### [USE flags for] [sys-fs/nilfs-utils](https://packages.gentoo.org/packages/sys-fs/nilfs-utils) [[]] [A New Implementation of a Log-structured File System for Linux]

  ------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------
  [`split-usr`](https://packages.gentoo.org/useflags/split-usr)       Enable behavior to support maintaining /bin, /lib\*, /sbin and /usr/sbin separately from /usr/bin and /usr/lib\*
  [`static-libs`](https://packages.gentoo.org/useflags/static-libs)   Build static versions of dynamic libraries as well
  ------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2025-09-07 16:52] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

`root `[`#`]`emerge --ask sys-fs/nilfs-utils`

## [Usage]

### [Formatting a device]

To format a device, use [mkfs.nilfs2]:

`root `[`#`]`mkfs.nilfs2 -f /dev/sda1`

    mkfs.nilfs2 (nilfs-utils 2.2.9)
    Start writing file system initial data to the device
           Blocksize:4096  Device:/dev/sda1  Device Size:268435456000
    File system initialization succeeded !!

### [Checkpoints and snapshots]

NILFS makes checkpoints at regular intervals. Checkpoints will be cleaned up by the garbage collector.

#### [Listing checkpoints]

To list checkpoints available, use [lscp]:

`root `[`#`]`lscp`

                     CNO        DATE     TIME  MODE  FLG      BLKCNT       ICNT
                       1  2026-01-12 21:25:44   cp    -            4          2
                       2  2026-01-12 21:28:22   cp    -            4          3

#### [Creating a checkpoint]

To create a checkpoint, use [mkcp]:

`root `[`#`]`mkcp /dev/sda1`

`root `[`#`]`lscp`

                     CNO        DATE     TIME  MODE  FLG      BLKCNT       ICNT
                       1  2026-01-12 21:25:44   cp    -            4          2
                       2  2026-01-12 21:28:22   cp    -            4          3
                       3  2026-01-12 21:28:46   cp    -            5          3

#### [Creating a snapshot]

To create a snapshot, use the `-s` flag in [mkcp]:

`root `[`#`]`mkcp -s`

`root `[`#`]`lscp`

                     CNO        DATE     TIME  MODE  FLG      BLKCNT       ICNT
                       1  2026-01-12 21:25:44   cp    -            4          2
                       2  2026-01-12 21:28:22   cp    -            4          3
                       3  2026-01-12 21:28:46   cp    -            5          3
                       4  2026-01-12 21:29:19   ss    -            5          3

Note how the Mode changed from `cp` to `ss`.

#### [][Converting a checkpoint to a snapshot (and vice versa)]

To convert a checkpoint to a snapshot (or vice versa), use [chcp]:

`root `[`#`]`chcp ss 2`

`root `[`#`]`lscp`

                     CNO        DATE     TIME  MODE  FLG      BLKCNT       ICNT
                       1  2026-01-12 21:25:44   cp    -            4          2
                       2  2026-01-12 21:28:22   ss    -            4          3
                       3  2026-01-12 21:28:46   cp    -            5          3
                       4  2026-01-12 21:29:19   ss    -            5          3

To turn a snapshot into a checkpoint:

\

`root `[`#`]`chcp cp 4`

`root `[`#`]`lscp`

                     CNO        DATE     TIME  MODE  FLG      BLKCNT       ICNT
                       1  2026-01-12 21:25:44   cp    -            4          2
                       2  2026-01-12 21:28:22   ss    -            4          3
                       3  2026-01-12 21:28:46   cp    -            5          3
                       4  2026-01-12 21:29:19   cp    -            5          3

#### [Mounting a snapshot]

Mounting a snapshot has two options, a read-only option, `-r` or `-o ro` and a `cp` option to specify the number of the checkpoint to be mounted.

`root `[`#`]`mkdir /mnt/nilfs-snapshot`

`root `[`#`]`mount -t nilfs2 -r -o cp=2 /dev/sda1 /mnt/nilfs-snapshot`

## [See also]

-   [bcachefs](https://wiki.gentoo.org/wiki/Bcachefs "Bcachefs") --- a fully-featured [B-tree](https://en.wikipedia.org/wiki/B-tree "wikipedia:B-tree") [filesystem](https://wiki.gentoo.org/wiki/Filesystem "Filesystem") based on [bcache](https://wiki.gentoo.org/wiki/Bcache "Bcache").
-   [btrfs](https://wiki.gentoo.org/wiki/Btrfs "Btrfs") --- a copy-on-write (CoW) [filesystem](https://wiki.gentoo.org/wiki/Filesystem "Filesystem") for Linux aimed at implementing advanced features while focusing on fault tolerance, self-healing properties, and easy administration.
-   [F2FS](https://wiki.gentoo.org/wiki/F2FS "F2FS") --- a [filesystem](https://wiki.gentoo.org/wiki/Filesystem "Filesystem") designed for NAND flash-based devices.
-   [ZFS](https://wiki.gentoo.org/wiki/ZFS "ZFS") --- a next generation [filesystem](https://wiki.gentoo.org/wiki/Filesystem "Filesystem") created by Matthew Ahrens and Jeff Bonwick.