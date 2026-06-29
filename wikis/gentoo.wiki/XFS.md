Other languages:

-   [Deutsch](https://wiki.gentoo.org/wiki/XFS/de "XFS (26% translated)")
-   [English]
-   [français](https://wiki.gentoo.org/wiki/XFS/fr "XFS (14% translated)")
-   [italiano](https://wiki.gentoo.org/wiki/XFS/it "XFS (14% translated)")
-   [magyar](https://wiki.gentoo.org/wiki/XFS/hu "XFS (90% translated)")
-   [русский](https://wiki.gentoo.org/wiki/XFS/ru "XFS (51% translated)")
-   [中文（中国大陆）‎](https://wiki.gentoo.org/wiki/XFS/zh-cn "XFS (100% translated)")
-   [日本語](https://wiki.gentoo.org/wiki/XFS/ja "XFS (65% translated)")

**Resources**

[[]][Home](https://xfs.wiki.kernel.org/)

[[]][Wikipedia](https://en.wikipedia.org/wiki/XFS "wikipedia:XFS")

[[]][Userspace](https://git.kernel.org/pub/scm/fs/xfs/xfsprogs-dev.git)

[[]][Kernel](https://git.kernel.org/pub/scm/fs/xfs/xfs-linux.git)

[[]][Tests](https://git.kernel.org/pub/scm/fs/xfs/xfstests-dev.git)

[[]][[xfs](irc://irc.oftc.net/xfs) (on [irc://irc.oftc.net](irc://irc.oftc.net)])

The **XFS** filesystem is a high-performance journaling [filesystem](https://wiki.gentoo.org/wiki/Filesystem "Filesystem"). It is [ACL](https://wiki.gentoo.org/wiki/Filesystem/Access_Control_List_Guide "Filesystem/Access Control List Guide") (POSIX) compliant for use with Linux.

XFS has a reputation for reliability and led to the creation of the venerable [xfstests] Linux kernel test suite which now tests regressions in various filesystems.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [Kernel]](#Kernel)
    -   [[1.2] [Emerge]](#Emerge)
-   [[2] [Usage]](#Usage)
    -   [[2.1] [Mount]](#Mount)
    -   [[2.2] [Creation]](#Creation)
    -   [[2.3] [Filesystem information]](#Filesystem_information)
    -   [[2.4] [Changing parameters]](#Changing_parameters)
    -   [[2.5] [Expanding a filesystem]](#Expanding_a_filesystem)
    -   [[2.6] [Freezing]](#Freezing)
-   [[3] [Utilities]](#Utilities)
-   [[4] [Maintenance]](#Maintenance)
    -   [[4.1] [Year 2038 timestamp support (bigtime)]](#Year_2038_timestamp_support_.28bigtime.29)
        -   [[4.1.1] [Using Dracut initramfs to perform the upgrade]](#Using_Dracut_initramfs_to_perform_the_upgrade)
-   [[5] [Removal]](#Removal)
-   [[6] [See also]](#See_also)
-   [[7] [References]](#References)

## [Installation]

### [Kernel]

[KERNEL] **Enable XFS support**

     File systems  --->
      <*> XFS filesystem support Search for <code>CONFIG_XFS_FS</code> to find this item.

Optional:

[KERNEL] **Enable optional XFS features**

     File systems  --->
      <*> XFS filesystem support Search for <code>CONFIG_XFS_FS</code> to find this item.
        [*]   XFS Quota support Search for <code>CONFIG_XFS_QUOTA</code> to find this item.
        [*]   XFS POSIX ACL support Search for <code>CONFIG_XFS_POSIX_ACL</code> to find this item.
        [*]   XFS Realtime subvolume support Search for <code>CONFIG_XFS_RT</code> to find this item.
      [ ]   XFS Verbose Warnings
      [ ]   XFS Debugging support
      [ ]   XFS online metadata check support
         [ ]   XFS online metadata check usage data collection
         [ ]   XFS online metadata repair support

### [Emerge]

The [[[sys-fs/xfsprogs]](https://packages.gentoo.org/packages/sys-fs/xfsprogs)[]] package is needed for XFS userspace utilities:

`root `[`#`]`emerge --ask sys-fs/xfsprogs`

## [Usage]

### [Mount]

Mount XFS filesystems with the [[mount](https://wiki.gentoo.org/wiki/Mount "Mount")] command.

** Note**\
XFS supports SSD discards in [/etc/fstab](https://wiki.gentoo.org/wiki//etc/fstab "/etc/fstab").

### [Creation]

To make an XFS filesystem with [mkfs.xfs] from [[[sys-fs/xfsprogs]](https://packages.gentoo.org/packages/sys-fs/xfsprogs)[]]:

`root `[`#`]`mkfs.xfs -L 'label' /dev/sda1`

The label is optional. Further tuning on creation might be interesting for use as a RAID, multi-terabyte drives, and placing the journal for a [HDD](https://wiki.gentoo.org/wiki/HDD "HDD") on a separate [SSD](https://wiki.gentoo.org/wiki/SSD "SSD").

Additionally to target stable kernels, it is recommended to add an option so the format does not enable unsupported or experimental features in that LTS kernel. [[[bug #969909]](https://bugs.gentoo.org/show_bug.cgi?id=969909)[]]

`root `[`#`]`mkfs.xfs -c options=/usr/share/xfsprogs/mkfs/lts_6.12.conf /dev/sda1`

The [GRUB](https://wiki.gentoo.org/wiki/GRUB "GRUB") bootloader will not tolerate unknown features enabled where [/boot] resides and will fail to install when [grub-install] is invoked. For example, the sys-boot/grub-2.12 release needs to use no later than lts_6.6.conf in the above command for the partition where [/boot] will reside. Be it a separate partition with the Handbook\'s Legacy BIOS layout or the rootfs in the UEFI layout.

### [Filesystem information]

[xfs_spaceman] can be used to display information about the space available and to run a report on the health of a filesystem.

`root `[`#`]`xfs_spaceman -c info /path/to/mountpoint`

### [Changing parameters]

** Important**\
It is not possible to change the parameters of a mounted filesystem

The parameters of an XFS filesystem can be changed using [xfs_admin]. For the full list of options, view the manpage: [[[xfs_admin(8)]](https://man.archlinux.org/man/xfs_admin.8.en)[[]](https://wiki.gentoo.org/wiki/Special:MyLanguage/man_page "Special:MyLanguage/man page")]

`root `[`#`]`xfs_admin -L 'label' /dev/sda1`

### [Expanding a filesystem]

** Important**\
The filesystem must be mounted to be grown

To grow an XFS filesystem to N amount, use [xfs_growfs].

`root `[`#`]`xfs_growfs -D N /path/to/mountpoint`

** Note**\
Using the `-d` argument results in it being expanded to the max size

### [Freezing]

To suspend access to a filesystem, use the [xfs_freeze] command.

`root `[`#`]`xfs_freeze -f /path/to/mountpoint`

## [Utilities]

  ------------------------------------------------------------------------------------------------------------ ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Utility                                                                                                      Description^[\[1\]](#cite_note-1)^                                                                                                                                                    Man page
  [fsck.xfs]        Checks a filesystem for corruption                                                                                                                                                    [[[fsck.xfs(8)]](https://man.archlinux.org/man/fsck.xfs.8.en)[[]](https://wiki.gentoo.org/wiki/Special:MyLanguage/man_page "Special:MyLanguage/man page")]
  [mkfs.xfs]        Creates a new filesystem                                                                                                                                                              [[[mkfs.xfs(8)]](https://man.archlinux.org/man/mkfs.xfs.8.en)[[]](https://wiki.gentoo.org/wiki/Special:MyLanguage/man_page "Special:MyLanguage/man page")]
  [xfs_admin]       Changes the parameters of a filesystem                                                                                                                                                [[[xfs_admin(8)]](https://man.archlinux.org/man/xfs_admin.8.en)[[]](https://wiki.gentoo.org/wiki/Special:MyLanguage/man_page "Special:MyLanguage/man page")]
  [xfs_bmap]        Prints block mapping for an XFS file                                                                                                                                                  [[[xfs_bmap(8)]](https://man.archlinux.org/man/xfs_bmap.8.en)[[]](https://wiki.gentoo.org/wiki/Special:MyLanguage/man_page "Special:MyLanguage/man page")]
  [xfs_copy]        Copies contents of a filesystem to one or more targets in parallel                                                                                                                    [[[xfs_copy(8)]](https://man.archlinux.org/man/xfs_copy.8.en)[[]](https://wiki.gentoo.org/wiki/Special:MyLanguage/man_page "Special:MyLanguage/man page")]
  [xfs_estimate]    Estimate the amount of space a directory would consume if it were copied to an XFS filesystem                                                                                         [[[xfs_estimate(8)]](https://man.archlinux.org/man/xfs_estimate.8.en)[[]](https://wiki.gentoo.org/wiki/Special:MyLanguage/man_page "Special:MyLanguage/man page")]
  [xfs_db]          Used to debug an XFS filesystem                                                                                                                                                       [[[xfs_db(8)]](https://man.archlinux.org/man/xfs_db.8.en)[[]](https://wiki.gentoo.org/wiki/Special:MyLanguage/man_page "Special:MyLanguage/man page")]
  [xfs_freeze]      Suspends access to a filesystem                                                                                                                                                       [[[xfs_freeze(8)]](https://man.archlinux.org/man/xfs_freeze.8.en)[[]](https://wiki.gentoo.org/wiki/Special:MyLanguage/man_page "Special:MyLanguage/man page")]
  [xfs_fsr]         Improves organization of mounted filesystems, compacting or improving the layout of extents                                                                                           [[[xfs_fsr(8)]](https://man.archlinux.org/man/xfs_fsr.8.en)[[]](https://wiki.gentoo.org/wiki/Special:MyLanguage/man_page "Special:MyLanguage/man page")]
  [xfs_growfs]      Increases a filesystem\'s size                                                                                                                                                        [[[xfs_growfs(8)]](https://man.archlinux.org/man/xfs_growfs.8.en)[[]](https://wiki.gentoo.org/wiki/Special:MyLanguage/man_page "Special:MyLanguage/man page")]
  [xfs_info]        Equivalent to invoking [xfs_growfs] but does not change any aspects about the filesystem   [[[xfs_info(8)]](https://man.archlinux.org/man/xfs_info.8.en)[[]](https://wiki.gentoo.org/wiki/Special:MyLanguage/man_page "Special:MyLanguage/man page")]
  [xfs_io]          Used for debugging, like [xfs_db] but for regular file paths than raw volumes              [[[xfs_io(8)]](https://man.archlinux.org/man/xfs_io.8.en)[[]](https://wiki.gentoo.org/wiki/Special:MyLanguage/man_page "Special:MyLanguage/man page")]
  [xfs_logprint]    Prints the log of an XFS filesystem                                                                                                                                                   [[[xfs_logprint(8)]](https://man.archlinux.org/man/xfs_logprint.8.en)[[]](https://wiki.gentoo.org/wiki/Special:MyLanguage/man_page "Special:MyLanguage/man page")]
  [xfs_mdrestore]   Restores an XFS metadump image to a filesystem image                                                                                                                                  [[[xfs_mdrestore(8)]](https://man.archlinux.org/man/xfs_mdrestore.8.en)[[]](https://wiki.gentoo.org/wiki/Special:MyLanguage/man_page "Special:MyLanguage/man page")]
  [xfs_metadump]    Copies filesystem metadata to a file                                                                                                                                                  [[[xfs_metadump(8)]](https://man.archlinux.org/man/xfs_metadump.8.en)[[]](https://wiki.gentoo.org/wiki/Special:MyLanguage/man_page "Special:MyLanguage/man page")]
  [xfs_mkfile]      Creates an XFS file (padded by zeroes by default)                                                                                                                                     [[[xfs_mkfile(8)]](https://man.archlinux.org/man/xfs_mkfile.8.en)[[]](https://wiki.gentoo.org/wiki/Special:MyLanguage/man_page "Special:MyLanguage/man page")]
  [xfs_ncheck]      Generates pathnames from inode numbers                                                                                                                                                [[[xfs_ncheck(8)]](https://man.archlinux.org/man/xfs_ncheck.8.en)[[]](https://wiki.gentoo.org/wiki/Special:MyLanguage/man_page "Special:MyLanguage/man page")]
  [xfs_quota]       Used for reporting and editing different aspects of filesystem quotas                                                                                                                 [[[xfs_quota(8)]](https://man.archlinux.org/man/xfs_quota.8.en)[[]](https://wiki.gentoo.org/wiki/Special:MyLanguage/man_page "Special:MyLanguage/man page")]
  [xfs_repair]      Repairs corrupted or damaged XFS filesystems                                                                                                                                          [[[xfs_repair(8)]](https://man.archlinux.org/man/xfs_repair.8.en)[[]](https://wiki.gentoo.org/wiki/Special:MyLanguage/man_page "Special:MyLanguage/man page")]
  [xfs_rtcp]        Copies a file to a real-time partition                                                                                                                                                [[[xfs_rtcp(8)]](https://man.archlinux.org/man/xfs_rtcp.8.en)[[]](https://wiki.gentoo.org/wiki/Special:MyLanguage/man_page "Special:MyLanguage/man page")]
  [xfs_scrub]       Checks and repairs contents of a mounted filesystem                                                                                                                                   [[[xfs_scrub(8)]](https://man.archlinux.org/man/xfs_scrub.8.en)[[]](https://wiki.gentoo.org/wiki/Special:MyLanguage/man_page "Special:MyLanguage/man page")]
  [xfs_scrub_all]   Scrubs all mounted XFS filesystems                                                                                                                                                    [[[xfs_scrub_all(8)]](https://man.archlinux.org/man/xfs_scrub_all.8.en)[[]](https://wiki.gentoo.org/wiki/Special:MyLanguage/man_page "Special:MyLanguage/man page")]
  [xfs_spaceman]    Reports and controls free space usage                                                                                                                                                 [[[xfs_spaceman(8)]](https://man.archlinux.org/man/xfs_spaceman.8.en)[[]](https://wiki.gentoo.org/wiki/Special:MyLanguage/man_page "Special:MyLanguage/man page")]
  ------------------------------------------------------------------------------------------------------------ ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## [Maintenance]

### [][Year 2038 timestamp support (bigtime)]

Older partitions (created with \<xfsprogs-5.15) will not have `bigtime` enabled by default. Mounting such partitions results in a warning like:

`root `[`#`]`dmesg`

    ...
    [    4.036258] xfs filesystem being mounted at /home supports timestamps until 2038 (0x7fffffff)
    ...

To check the current version of xfsprogs, run [mkfs.xfs -V]. There\'s no need for this on up-to-date Gentoo systems, but it might be necessary if using install media from another distribution with older userland.

`bigtime` support was enabled by default in xfsprogs 5.15, so manual setting is not required in newer versions.

Beginning with [kernel](https://wiki.gentoo.org/wiki/Kernel "Kernel") 5.10, XFS gained `bigtime` support to extend the maximum recorded date stamps from 2038 to 2486 for the V5 on-disk format. ^[\[2\]](#cite_note-2)^

To upgrade an older filesystem to `bigtime`, first cleanly unmount the file system. The upgrade will refuse to run if the unmount was not completely clean.

Then run:

`root `[`#`]`xfs_admin -O bigtime=1 /dev/sda1`

Replacing [/dev/sda1] with the device path.

** Note**\
XFS on the root mount will require an [initramfs](https://wiki.gentoo.org/wiki/Initramfs "Initramfs") or other live environment with the necessary tools to perform an upgrade to the metadata.

#### [Using Dracut initramfs to perform the upgrade]

First, [Dracut](https://wiki.gentoo.org/wiki/Dracut "Dracut") needs additional files included in the initramfs in order to perform the upgrade. This can be accomplished with either the `--install` option or inside a configuration file using the `install_items` option.

`root `[`#`]`dracut --install "/usr/sbin/xfs_admin /usr/bin/expr" ...`

Then, the kernel command line option can be modified to include `rd.break=pre-mount` to stop the initramfs just before it would mount the root filesystem. Ensure this is done temporarily and removed on subsequent reboots after upgrade.

## [Removal]

To schedule removal at the next run:

`root `[`#`]`emerge --ask --depclean --verbose sys-fs/xfsprogs`

## [See also]

-   [Deduplication](https://wiki.gentoo.org/wiki/Deduplication "Deduplication") --- a mechanism for reducing the space taken by multiple identical copies of a file are stored on a [filesystem](https://wiki.gentoo.org/wiki/Filesystem "Filesystem")
-   [FAT](https://wiki.gentoo.org/wiki/FAT "FAT") --- [filesystem](https://wiki.gentoo.org/wiki/Filesystem "Filesystem") originally created for use with MS-DOS (and later pre-NT Microsoft Windows).
-   [Ext4](https://wiki.gentoo.org/wiki/Ext4 "Ext4") --- an open source disk [filesystem](https://wiki.gentoo.org/wiki/Filesystem "Filesystem") and the most recent version of the extended series of filesystems.
-   [Btrfs](https://wiki.gentoo.org/wiki/Btrfs "Btrfs") --- a copy-on-write (CoW) [filesystem](https://wiki.gentoo.org/wiki/Filesystem "Filesystem") for Linux aimed at implementing advanced features while focusing on fault tolerance, self-healing properties, and easy administration.

## [References]

1.  [[[↑](#cite_ref-1)] [[https://www.linuxfromscratch.org/blfs/view/svn/postlfs/xfsprogs.html](https://www.linuxfromscratch.org/blfs/view/svn/postlfs/xfsprogs.html)]]
2.  [[[↑](#cite_ref-2)] [[https://www.phoronix.com/scan.php?page=news_item&px=XFS-Linux-5.10](https://www.phoronix.com/scan.php?page=news_item&px=XFS-Linux-5.10)]]