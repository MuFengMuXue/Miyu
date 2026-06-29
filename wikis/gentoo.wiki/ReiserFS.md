This page contains [[changes](https://wiki.gentoo.org/index.php?title=ReiserFS&oldid=1333768&diff=1401633)] which are not marked for translation.

Other languages:

-   [English]
-   [français](https://wiki.gentoo.org/wiki/ReiserFS/fr "ReiserFS (94% translated)")
-   [magyar](https://wiki.gentoo.org/wiki/ReiserFS/hu "ReiserFS (100% translated)")
-   [日本語](https://wiki.gentoo.org/wiki/ReiserFS/ja "ReiserFS (100% translated)")

**Resources**

[[]][Wikipedia](https://en.wikipedia.org/wiki/ReiserFS "wikipedia:ReiserFS")

** Warning**\
ReiserFS is considered deprecated in the Linux kernel^[\[1\]](#cite_note-1)^ and was removed in Linux kernel 6.13^[\[2\]](#cite_note-2)^. Users of ReiserFS are encouraged to migrate their data to supported filesystems such as [ext4](https://wiki.gentoo.org/wiki/Ext4 "Ext4"), [XFS](https://wiki.gentoo.org/wiki/XFS "XFS"), or [btrfs](https://wiki.gentoo.org/wiki/Btrfs "Btrfs").

**ReiserFS** is a journaling [filesystem](https://wiki.gentoo.org/wiki/Filesystem "Filesystem") for Linux licensed under the GPL-2 license and is the predecessor of [Reiser4](https://archive.kernel.org/oldwiki/reiser4.wiki.kernel.org). ReiserFS was originally developed by [Namesys](https://en.wikipedia.org/wiki/Namesys "wikipedia:Namesys") and [Hans Reiser](https://en.wikipedia.org/wiki/Hans_Reiser "wikipedia:Hans Reiser"), but is under maintenance by volunteers nowadays.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [Kernel]](#Kernel)
    -   [[1.2] [Emerge]](#Emerge)
-   [[2] [Troubleshooting]](#Troubleshooting)
    -   [[2.1] [ReiserFS filesystem corruption issues]](#ReiserFS_filesystem_corruption_issues)
-   [[3] [See also]](#See_also)
-   [[4] [References]](#References)

## [Installation]

### [Kernel]

Support for ReiserFS has to be enabled in the Kernel first.

[KERNEL] **Enabling ReiserFS support**

    File systems  --->
       <*> Reiserfs support

### [Emerge]

Utilities for ReiserFS are available in [[[sys-fs/reiserfsprogs]](https://packages.gentoo.org/packages/sys-fs/reiserfsprogs)[]] package:

`root `[`#`]`emerge --ask sys-fs/reiserfsprogs`

## [Troubleshooting]

### [ReiserFS filesystem corruption issues]

If the ReiserFS partition is corrupt, try booting the Gentoo Install CD and run [reiserfsck \--rebuild-tree] on the corrupted filesystem. This should make the filesystem consistent again, although there may be some lost files or directories due to the corruption.

## [See also]

-   [Ext4](https://wiki.gentoo.org/wiki/Ext4 "Ext4") --- an open source disk [filesystem](https://wiki.gentoo.org/wiki/Filesystem "Filesystem") and the most recent version of the extended series of filesystems.
-   [XFS](https://wiki.gentoo.org/wiki/XFS "XFS") --- a high-performance journaling [filesystem](https://wiki.gentoo.org/wiki/Filesystem "Filesystem")
-   [ZFS](https://wiki.gentoo.org/wiki/ZFS "ZFS") --- a next generation [filesystem](https://wiki.gentoo.org/wiki/Filesystem "Filesystem") created by Matthew Ahrens and Jeff Bonwick.

## [References]

1.  [[[↑](#cite_ref-1)] [[git.kernel.org](https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/commit/?id=1500e7e0726e963f64b9785a0cb0a820b2587bad)]]
2.  [[[↑](#cite_ref-2)] [[git.kernel.org](https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/commit/?id=c01f664e4ca210823b7594b50669bbd9b0a3c3b0)]]