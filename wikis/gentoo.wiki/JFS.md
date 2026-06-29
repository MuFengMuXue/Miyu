Other languages:

-   [English]
-   [italiano](https://wiki.gentoo.org/wiki/JFS/it "JFS (21% translated)")
-   [magyar](https://wiki.gentoo.org/wiki/JFS/hu "JFS (100% translated)")
-   [русский](https://wiki.gentoo.org/wiki/JFS/ru "JFS (100% translated)")
-   [中文（中国大陆）‎](https://wiki.gentoo.org/wiki/JFS/zh-cn "JFS (21% translated)")
-   [日本語](https://wiki.gentoo.org/wiki/JFS/ja "JFS (84% translated)")

**Resources**

[[]][Home](https://jfs.sourceforge.net/)

[[]][Package information](https://packages.gentoo.org/packages/sys-fs/jfsutils)

[[]][Wikipedia](https://en.wikipedia.org/wiki/JFS_(file_system) "wikipedia:JFS (file system)")

**JFS** (**J**ournaled **F**ile **S**ystem) is a 64-bit journaling [filesystem](https://wiki.gentoo.org/wiki/Filesystem "Filesystem") created by IBM. An implementation for the Linux kernel is available as free software under the terms of the GNU General Public License. It is low on resource usage and comparatively fast doing all kinds of filesystem operations (as opposed to being specialized in some, e.g. [XFS](https://wiki.gentoo.org/wiki/XFS "XFS") is fast with big files, but slower with small ones). As such JFS is especially good for usage with battery-powered devices such as laptops.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [Kernel]](#Kernel)
    -   [[1.2] [Emerge]](#Emerge)
-   [[2] [Usage]](#Usage)
    -   [[2.1] [Creation]](#Creation)
    -   [[2.2] [Mount]](#Mount)
    -   [[2.3] [Extracting a Fsck Log]](#Extracting_a_Fsck_Log)
    -   [[2.4] [Tuning]](#Tuning)
-   [[3] [Utilities]](#Utilities)
-   [[4] [Troubleshooting]](#Troubleshooting)
    -   [[4.1] [Fsck]](#Fsck)
    -   [[4.2] [Debugfs]](#Debugfs)
-   [[5] [See also]](#See_also)
-   [[6] [References]](#References)

## [Installation]

### [Kernel]

JFS is supported in the standard Linux kernel:

[KERNEL] **Enabling JFS support**

    File systems  --->
       <*> JFS filesystem support

Optional JFS features:

[KERNEL] **Adding optional JFS features**

    File systems  --->
       <*> JFS filesystem support
       [*]   JFS POSIX Access Control Lists
       [*]   JFS Security Labels
       [ ]   JFS debugging
       [*]   JFS statistics

### [Emerge]

Filesystem utilities are available in the [[[sys-fs/jfsutils]](https://packages.gentoo.org/packages/sys-fs/jfsutils)[]] package:

`root `[`#`]`emerge --ask sys-fs/jfsutils`

## [Usage]

### [Creation]

`root `[`#`]`mkfs.jfs /dev/sda1`

### [Mount]

`root `[`#`]`mount -t jfs /dev/sda1 /path/to/mountpoint`

### [Extracting a Fsck Log]

[jfs_fscklog] can extract the fsck log from a JFS device.

`root `[`#`]`jfs_fscklog -d /dev/sda1 -f fsck.log`

### [Tuning]

[jfs_tune] can change different parameters, to change the UUID:

`root `[`#`]`jfs_tune -l -U random /dev/sda1`

## [Utilities]

  ---------------------------------------------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Utility                                                                                                    Description^[\[1\]](#cite_note-1)^                                                                                                          Man page
  [fsck.jfs]      A hard link to [jfs_fsck].
  [jfs_fsck]      Checks a JFS filesystem for corruption.                                                                                                     [[[jfs_fsck(8)]](https://man.archlinux.org/man/jfs_fsck.8.en)[[]](https://wiki.gentoo.org/wiki/Special:MyLanguage/man_page "Special:MyLanguage/man page")]
  [mkfs.jfs]      A hard link to [jfs_mkfs].
  [jfs_mkfs]      Creates a new JFS filesystem.                                                                                                               [[[jfs_fsck(8)]](https://man.archlinux.org/man/jfs_fsck.8.en)[[]](https://wiki.gentoo.org/wiki/Special:MyLanguage/man_page "Special:MyLanguage/man page")]
  [jfs_debugfs]   A utility to perform low-level actions on a JFS filesystem.                                                                                 [[[jfs_debugfs(8)]](https://man.archlinux.org/man/jfs_debugfs.8.en)[[]](https://wiki.gentoo.org/wiki/Special:MyLanguage/man_page "Special:MyLanguage/man page")]
  [jfs_fscklog]   Extracts the fsck log from a JFS filesystem.                                                                                                [[[jfs_fscklog(8)]](https://man.archlinux.org/man/jfs_fscklog.8.en)[[]](https://wiki.gentoo.org/wiki/Special:MyLanguage/man_page "Special:MyLanguage/man page")]
  [jfs_logdump]   Dumps the journal of a filesystem into [./jfslog.dmp].   [[[jfs_logdump(8)]](https://man.archlinux.org/man/jfs_logdump.8.en)[[]](https://wiki.gentoo.org/wiki/Special:MyLanguage/man_page "Special:MyLanguage/man page")]
  [jfs_tune]      Adjusts tunable parameters of a filesystem.                                                                                                 [[[jfs_tune(8)]](https://man.archlinux.org/man/jfs_tune.8.en)[[]](https://wiki.gentoo.org/wiki/Special:MyLanguage/man_page "Special:MyLanguage/man page")]
  ---------------------------------------------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## [Troubleshooting]

### [Fsck]

** Important**\
Unmount the filesystem to prevent file damage.

To check a JFS filesystem for corruption, run [fsck.jfs]:

`root `[`#`]`fsck.jfs /dev/sda1`

### [Debugfs]

[jfs_debugfs] can be used to perform low-level actions on a JFS filesystem.

In this example, a JFS filesystem with the layout:

Tree

`test/`\
`├── a`\
`├── b`\
`├── c`\

` `

First, the inode needs to be known for the root of the directory.

** Important**\
The **2** is the inode number

`user `[`$`]`ls -id`

    2 .

Next, enter the debugfs interface with [jfs_debugfs]:

`root `[`#`]`jfs_debugfs /dev/sda1`

Now list the directory using the inode number:

`>``dir 2`

    idotdot = 2

    4096    test

**4096** is the inode of the test directory, now list the contents of that directory:

`>``dir 4096`

    idotdot = 2

    4097    a
    4098    b
    4099    c

To see everything that the debugfs interface do, read the man-page [[[jfs_debugfs(8)]](https://man.archlinux.org/man/jfs_debugfs.8.en)[[]](https://wiki.gentoo.org/wiki/Special:MyLanguage/man_page "Special:MyLanguage/man page")].

## [See also]

-   [XFS](https://wiki.gentoo.org/wiki/XFS "XFS") --- a high-performance journaling [filesystem](https://wiki.gentoo.org/wiki/Filesystem "Filesystem")
-   [Ext4](https://wiki.gentoo.org/wiki/Ext4 "Ext4") --- an open source disk [filesystem](https://wiki.gentoo.org/wiki/Filesystem "Filesystem") and the most recent version of the extended series of filesystems.

## [References]

1.  [[[↑](#cite_ref-1)] [[https://www.linuxfromscratch.org/blfs/view/stable/postlfs/jfsutils.html](https://www.linuxfromscratch.org/blfs/view/stable/postlfs/jfsutils.html)]]