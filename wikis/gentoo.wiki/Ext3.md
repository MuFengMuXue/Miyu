This page contains [[changes](https://wiki.gentoo.org/index.php?title=Ext4&oldid=1415635&diff=1415665)] which are not marked for translation.

Other languages:

-   [Deutsch](https://wiki.gentoo.org/wiki/Ext4/de "Ext4 (25% translated)")
-   [English]
-   [français](https://wiki.gentoo.org/wiki/Ext4/fr "Ext4 (2% translated)")
-   [italiano](https://wiki.gentoo.org/wiki/Ext4/it "Ext4 (16% translated)")
-   [magyar](https://wiki.gentoo.org/wiki/Ext4/hu "ext4 (66% translated)")
-   [svenska](https://wiki.gentoo.org/wiki/Ext4/sv "Ext4 (5% translated)")
-   [русский](https://wiki.gentoo.org/wiki/Ext4/ru "ext4 (82% translated)")
-   [中文（中国大陆）‎](https://wiki.gentoo.org/wiki/Ext4/zh-cn "Ext4 (16% translated)")
-   [日本語](https://wiki.gentoo.org/wiki/Ext4/ja "ext4 (100% translated)")

**Resources**

[[]][Home](https://ext4.wiki.kernel.org/index.php/Main_Page)

[[]][Wikipedia](https://en.wikipedia.org/wiki/Ext4 "wikipedia:Ext4")

[[]][Man page](http://man7.org/linux/man-pages/man5/ext4.5.html)

**ext4** (fourth extended file system) is an open source disk [filesystem](https://wiki.gentoo.org/wiki/Filesystem "Filesystem") and the most recent version of the extended series of filesystems. It is the primary file system in use by many Linux systems making it arguably the most stable and well tested file system supported in Linux.

Initially created as a fork of ext3, ext4 brings new features, performance improvements, and removal of size limits with moderate changes to the on-disk format. It can span volumes up to 1 Exabyte and with maximum file size of 16TB. Instead of the classic ext2/3 bitmap block allocation, ext4 uses extents, which improve large file performance and reduce fragmentation. Ext4 also provides more sophisticated block allocation algorithms (delayed allocation and multiblock allocation) giving the filesystem driver more ways to optimize the layout of data on the disk.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [Kernel]](#Kernel)
        -   [[1.1.1] [Ext3]](#Ext3)
        -   [[1.1.2] [Ext2]](#Ext2)
        -   [[1.1.3] [Large drive support]](#Large_drive_support)
    -   [[1.2] [USE flags]](#USE_flags)
    -   [[1.3] [Emerge]](#Emerge)
-   [[2] [Usage]](#Usage)
    -   [[2.1] [Creation]](#Creation)
    -   [[2.2] [Mounting]](#Mounting)
    -   [[2.3] [Ext4 without a journal]](#Ext4_without_a_journal)
        -   [[2.3.1] [Removing the journal from an existing ext4 volume]](#Removing_the_journal_from_an_existing_ext4_volume)
        -   [[2.3.2] [Create a new journal-less ext4 volume]](#Create_a_new_journal-less_ext4_volume)
-   [[3] [Utilities]](#Utilities)
-   [[4] [See also]](#See_also)
-   [[5] [External resources]](#External_resources)
-   [[6] [References]](#References)

## [Installation]

### [Kernel]

Activate the following kernel options for the ext4 driver:

[KERNEL] **Enabling ext4 support**

    File systems  --->
      <*> The Extended 4 (ext4) filesystem Search for <code>CONFIG_CONFIG_EXT4_FS</code> to find this item.

Support for optional ext4 features:

[KERNEL] **Enabling optional features for ext4**

    File systems  --->
      [*]   Ext4 POSIX Access Control Lists Search for <code>CONFIG_CONFIG_EXT4_FS_POSIX_ACL</code> to find this item.
      [*]   Ext4 Security Labels Search for <code>CONFIG_CONFIG_EXT4_FS_SECURITY</code> to find this item.
      [ ]   EXT4 debugging support

** Note**\
The ext4 driver can handle ext2, ext3 and ext4 filesystems. It will maintain compatibility if the filesystem is mounted as ext2 or ext3, and will provide upgradability when mounted as ext4. Additionally [tune2fs] can be used to add ext3- and ext4-specific features to an existing ext2 or ext3 filesystem, though certain hard limits will remain.

** Warning**\
Both ext2 and ext3 file timestamps are affected by the [year 2038 problem](https://en.wikipedia.org/wiki/Year_2038_problem "wikipedia:Year 2038 problem"), while ext4 is Y2k38-safe since 2016, Linux kernel 4.3.6 and e2fsprogs 1.43. When an Extended filesystem specifically *without a journal* is desired, instead of ext2 a journal-less ext4 filesystem should be used; see [ext4 without a journal](https://wiki.gentoo.org/wiki/Ext4#Ext4_without_a_journal "Ext4").

** Important**\
A normal ext4 system will not need to enable ext3 or ext2 options. The following filesystem options are here solely for historical purposes ([ext3](https://wiki.gentoo.org/wiki/Ext4#Ext3 "Ext4")) and very special use-cases ([ext2](https://wiki.gentoo.org/wiki/Ext4#Ext2 "Ext4")).

#### [Ext3]

The original ext3 driver was removed from the Linux kernel with version 4.3. There should remain only rare cases which make it necessary to use an ext3 filesystem, in which case the ext4 driver may be used.

** Note**\
It is advised to use the ext4 driver to mount ext3 filesystems. The old ext3 driver should **not** be enabled.

Activate the following kernel options for ext3 driver:

[KERNEL] **Enabling ext3 support**

    File systems  --->
       <*> Ext3 journalling file system support

Support for optional ext3 features:

[KERNEL] **Enabling optional features for ext3**

    File systems  --->
       [*]   Default to 'data=ordered' in ext3
       [*]   Ext3 extended attributes
       [*]     Ext3 POSIX Access Control Lists
       [*]     Ext3 Security Labels

#### [Ext2]

** Note**\
The ext2 filesystem does not have [journaling support](https://en.wikipedia.org/wiki/Journaling_file_system "wikipedia:Journaling file system").

** Warning**\
When the original ext2 filesystem driver is enabled, it will be used to mount ext2 filesystems. Under *normal* circumstances it is highly recommended to use the ext4 driver, and **not** to enable the older ext2 driver: there is absolutely no necessity for a separate driver when the ext4 driver is already available to mount ext2 filesystems.

** Note**\
The original ext2 driver remains available for special cases. For example: compared to the ext4 driver, the original ext2 code has a lower memory footprint. (In such cases, the ext4 driver will be entirely omitted, so ext3 and ext4 filesystems will not be available.)

Activate the following kernel options for ext2 support using the original ext2 driver:

[KERNEL] **Enabling ext2 support**

    File systems  --->
       <*> Second extended fs support

Support for optional ext2 features:

[KERNEL] **Enabling optional features for ext2**

    File systems  --->
       [*]   Ext2 extended attributes
       [*]     Ext2 POSIX Access Control Lists
       [*]     Ext2 Security Labels

#### [Large drive support]

[KERNEL] **Enabling large drives for **[x86]** kernels**

    -*- Enable the block layer  --->
        [*]   Support for large (2TB+) block devices and files

### [USE flags]

### [USE flags for] [sys-fs/e2fsprogs](https://packages.gentoo.org/packages/sys-fs/e2fsprogs) [[]] [Standard EXT2/EXT3/EXT4 filesystem utilities]

  ------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------
  [`+tools`](https://packages.gentoo.org/useflags/+tools)             Build extfs tools (mke2fs, e2fsck, tune2fs, etc.)
  [`archive`](https://packages.gentoo.org/useflags/archive)           Add support for mke2fs to read a tarball as input. This allows not needing privileges. Needs app-arch/libarchive.
  [`cron`](https://packages.gentoo.org/useflags/cron)                 Install e2scrub_all cron script
  [`fuse`](https://packages.gentoo.org/useflags/fuse)                 Build fuse2fs, a FUSE file system client for ext2/ext3/ext4 file systems
  [`nls`](https://packages.gentoo.org/useflags/nls)                   Add Native Language Support (using gettext - GNU locale utilities)
  [`static-libs`](https://packages.gentoo.org/useflags/static-libs)   Build static versions of dynamic libraries as well
  [`test`](https://packages.gentoo.org/useflags/test)                 Enable dependencies and/or preparations necessary to run tests (usually controlled by FEATURES=test but can be toggled independently)
  [`verify-sig`](https://packages.gentoo.org/useflags/verify-sig)     Verify upstream signatures on distfiles
  ------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-04-13 11:36] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

The [[[sys-fs/e2fsprogs]](https://packages.gentoo.org/packages/sys-fs/e2fsprogs)[]] package and should be available as part of the default [system set](https://wiki.gentoo.org/wiki/System_set_(Portage) "System set (Portage)"). Despite the historical name, the package includes utilities for ext3 and ext4.

`root `[`#`]`emerge --ask sys-fs/e2fsprogs`

## [Usage]

### [Creation]

** Warning**\
Any [mkfs.\*] and [mke2fs] command will irreversibly destroy any content of the device (i.e. partition, volume, disk drive) or file it is told to format. Be sure to select the correct device and partition! (In the following examples `/dev/sdx5` is used.)

To create an ext4 filesystem on the [/dev/sdx5] partition:

`root `[`#`]`mkfs.ext4 /dev/sdx5`

### [Mounting]

See [filesystem](https://wiki.gentoo.org/wiki/Filesystem#Mounting "Filesystem").

### [Ext4 without a journal]

In specific use-cases it may be desirable to create a journal-less filesystem. Even though ext2 does provide exactly that, it is also affected by the year 2038 problem regarding file timestamps. Only the ext4 filesystem has been made Y2K38-safe.

In order to get the current Extended filesystem without a journal, an ext4 filesystem can be created without the `has_journal` feature, or modified accordingly. (Note that this is not possible on ext3 filesystems.)

#### [Removing the journal from an existing ext4 volume]

To display filesystem features currently enabled on a specific ext2/3/4 volume:

`root `[`#`]`dumpe2fs -h /dev/sdx5 | grep "^Filesystem features:"`

To disable the journal, the filesystem must be unmounted first:

`root `[`#`]`umount /dev/sdx5 `

`root `[`#`]`tune2fs -O ^has_journal /dev/sdx5`

The leading `^` disables the specified feature. Otherwise the feature would be enabled; i.e. to enable a journal on an existing ext2 or journal-less ext4 filesystem:

`root `[`#`]`tune2fs -O has_journal /dev/sdx5`

Running [dumpe2fs] again, the `has_journal` feature should no longer be listed. The filesystem can now be mounted again:

`root `[`#`]`mount /dev/sdx5 `

[EXT4-fs (/dev/sdx5): mounted filesystem abcdef01-2345-6789-9876-543210fedcba r/w without journal. Quota mode: disabled.]

#### [Create a new journal-less ext4 volume]

To create (i.e. format) a new ext4 volume without a journal, the default options of the `ext4` filesystem type have to be overridden:

`root `[`#`]`mke2fs -t ext4 -O ^has_journal /dev/sdx5`

## [Utilities]

Utilities included in [[[sys-fs/e2fsprogs]](https://packages.gentoo.org/packages/sys-fs/e2fsprogs)[]] consist of:

  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Utility                                                                                                                                                                  Description                                                                                                                                                                      Man page
  [[badblocks](https://wiki.gentoo.org/wiki/Ext4/badblocks "Ext4/badblocks")]   Scans a disk for bad blocks.                                                                                                                                                     [[[badblocks(8)]](https://man.archlinux.org/man/badblocks.8.en)[[]](https://wiki.gentoo.org/wiki/Special:MyLanguage/man_page "Special:MyLanguage/man page")]
  [debugfs]                                                                     An ext2/ext3/ext4 file system debugger.                                                                                                                                          [[[debugfs(8)]](https://man.archlinux.org/man/debugfs.8.en)[[]](https://wiki.gentoo.org/wiki/Special:MyLanguage/man_page "Special:MyLanguage/man page")]
  [dumpe2fs]                                                                    A tool to dump ext2/ext3/ext4 filesystem information.                                                                                                                            [[[dumpe2fs(8)]](https://man.archlinux.org/man/dumpe2fs.8.en)[[]](https://wiki.gentoo.org/wiki/Special:MyLanguage/man_page "Special:MyLanguage/man page")]
  [e2fsck]                                                                      A tool for checking ext2/ext3/ext4 filesystems.                                                                                                                                  [[[e2fsck(8)]](https://man.archlinux.org/man/e2fsck.8.en)[[]](https://wiki.gentoo.org/wiki/Special:MyLanguage/man_page "Special:MyLanguage/man page")]
  [e2image]                                                                     A tool for saving critical ext2/ext3/ext4 filesystem metadata to a file.                                                                                                         [[[e2image(8)]](https://man.archlinux.org/man/e2image.8.en)[[]](https://wiki.gentoo.org/wiki/Special:MyLanguage/man_page "Special:MyLanguage/man page")]
  [e2label]                                                                     A tool to change the label on an ext2/ext3/ext4 filesystem (symlinks to [tune2fs]).
  [e2undo]                                                                      A tool to replay an undo log for an ext2/ext3/ext4 filesystem.                                                                                                                   [[[e2undo(8)]](https://man.archlinux.org/man/e2undo.8.en)[[]](https://wiki.gentoo.org/wiki/Special:MyLanguage/man_page "Special:MyLanguage/man page")]
  [fsck.ext2]                                                                   Checks, specifically, an ext2 filesystem (symlinks to [e2fsck]).
  [fsck.ext3]                                                                   Checks, specifically, an ext3 filesystem (symlinks to [e2fsck]).
  [fsck.ext4]                                                                   Checks, specifically, an ext4 filesystem (symlinks to [e2fsck]).
  [fsck.ext4dev]                                                                Checks, specifically, an ext4dev filesystem (symlinks to [e2fsck]).
  [logsave]                                                                     A tool to save the output of a command in a logfile.                                                                                                                             [[[logsave(8)]](https://man.archlinux.org/man/logsave.8.en)[[]](https://wiki.gentoo.org/wiki/Special:MyLanguage/man_page "Special:MyLanguage/man page")]
  [mke2fs]                                                                      The base program for creating ext2/ext3/ext4 filesystems. Creation commands symlink here.                                                                                        [[[mke2fs(8)]](https://man.archlinux.org/man/mke2fs.8.en)[[]](https://wiki.gentoo.org/wiki/Special:MyLanguage/man_page "Special:MyLanguage/man page")]
  [mkfs.ext2]                                                                   Creates, specifically, an ext2 filesystem (symlinks to [mke2fs]).
  [mkfs.ext3]                                                                   Creates, specifically, an ext3 filesystem (symlinks to [mke2fs]).
  [mkfs.ext4]                                                                   Creates, specifically, an ext4 filesystem (symlinks to [mke2fs]).
  [mkfs.ext4dev]                                                                Creates, specifically, an ext24dev filesystem (symlinks to [mke2fs]).
  [resize2fs]                                                                   An ext2/ext3/ext4 filesystem resizer.                                                                                                                                            [[[resize2fs(8)]](https://man.archlinux.org/man/resize2fs.8.en)[[]](https://wiki.gentoo.org/wiki/Special:MyLanguage/man_page "Special:MyLanguage/man page")]
  [tune2fs]                                                                     Adjust tunable filesystem parameters on ext2/ext3/ext4 filesystems.                                                                                                              [[[tune2fs(8)]](https://man.archlinux.org/man/tune2fs.8.en)[[]](https://wiki.gentoo.org/wiki/Special:MyLanguage/man_page "Special:MyLanguage/man page")]
  [chattr]                                                                      Change file attributes on a Linux filesystem.                                                                                                                                    [[[chattr(1)]](https://man.archlinux.org/man/chattr.1.en)[[]](https://wiki.gentoo.org/wiki/Special:MyLanguage/man_page "Special:MyLanguage/man page")]
  [lsattr]                                                                      List ext2/ext3/ext4 file attributes.                                                                                                                                             [[[lsattr(1)]](https://man.archlinux.org/man/lsattr.1.en)[[]](https://wiki.gentoo.org/wiki/Special:MyLanguage/man_page "Special:MyLanguage/man page")]
  [e2freefrag]                                                                  Report free space fragmentation information.                                                                                                                                     [[[e2freefrag(8)]](https://man.archlinux.org/man/e2freefrag.8.en)[[]](https://wiki.gentoo.org/wiki/Special:MyLanguage/man_page "Special:MyLanguage/man page")]
  [e4defrag]                                                                    An online defragmenter for ext4 filesystem.                                                                                                                                      [[[e4defrag(8)]](https://man.archlinux.org/man/e4defrag.8.en)[[]](https://wiki.gentoo.org/wiki/Special:MyLanguage/man_page "Special:MyLanguage/man page")]
  [filefrag]                                                                    Report on file fragmentation.                                                                                                                                                    [[[filefrag(8)]](https://man.archlinux.org/man/filefrag.8.en)[[]](https://wiki.gentoo.org/wiki/Special:MyLanguage/man_page "Special:MyLanguage/man page")]
  [mklost+found]                                                                Create a lost+found directory on a mounted ext2/ext3/ext4 file system.                                                                                                           [[[mklost+found(8)]](https://man.archlinux.org/man/mklost+found.8.en)[[]](https://wiki.gentoo.org/wiki/Special:MyLanguage/man_page "Special:MyLanguage/man page")]
  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## [See also]

-   [XFS](https://wiki.gentoo.org/wiki/XFS "XFS") --- a high-performance journaling [filesystem](https://wiki.gentoo.org/wiki/Filesystem "Filesystem")
-   [Btrfs](https://wiki.gentoo.org/wiki/Btrfs "Btrfs") --- a copy-on-write (CoW) [filesystem](https://wiki.gentoo.org/wiki/Filesystem "Filesystem") for Linux aimed at implementing advanced features while focusing on fault tolerance, self-healing properties, and easy administration.
-   [FAT](https://wiki.gentoo.org/wiki/FAT "FAT") --- [filesystem](https://wiki.gentoo.org/wiki/Filesystem "Filesystem") originally created for use with MS-DOS (and later pre-NT Microsoft Windows).

## [External resources]

-   [https://ext4.wiki.kernel.org/](https://ext4.wiki.kernel.org/) - The second, third, and fourth extended file system wiki.

## [References]