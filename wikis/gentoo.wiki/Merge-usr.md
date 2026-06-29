Other languages:

-   [English]
-   [magyar](https://wiki.gentoo.org/wiki/Merge-usr/hu "Merge-usr (3% translated)")
-   [русский](https://wiki.gentoo.org/wiki/Merge-usr/ru "merge-usr (98% translated)")
-   [日本語](https://wiki.gentoo.org/wiki/Merge-usr/ja "merge-usr (98% translated)")

**Resources**

[[]][Package information](https://packages.gentoo.org/packages/sys-apps/merge-usr)

[[]][GitHub](https://github.com/floppym/merge-usr)

**[merge-usr]** is a script which may be used to migrate a system from the legacy \"[split-usr](https://wiki.gentoo.org/wiki/Split_/usr "Split /usr")\" layout to the newer \"merged-usr\" layout as well as the \"sbin merge\". This is often referred to as the \"[/usr] merge\" where the [/bin], [/sbin], [/lib], and [/lib64] are permanently migrated to the [/usr/bin], [/usr/sbin], [/usr/lib] and [/usr/lib64] directories respectively. As part of the migration, the former non-[/usr] directories will then be replaced with symlinks pointing to the new locations for backwards compatibility.

In addition, the script applies the \"sbin merge\" at the same time where [/sbin] and [/usr/sbin] are both actually merged to [/usr/bin].

The underlying motivation for this change is compatibility: in theory this change should allow increased interoperability between Linux distributions. Scripts, especially, should \"just work\" under the new system and not fail due to binaries being in unexpected locations when run from a Linux distribution other than the one they were written on.

It also broadly feels cleaner. The separation between [/bin], [/sbin], [/usr/bin], and [/usr/sbin] was often inconsistent between distros and the placement of binaries across them was at the discretion of the package maintainer.

It is required for [[systemd](https://wiki.gentoo.org/wiki/Systemd "Systemd")] ≥255 due to changes upstream, but it remains optional for other init systems.

## Contents

-   [[1] [Migration]](#Migration)
    -   [[1.1] [Manual Migration]](#Manual_Migration)
-   [[2] [Frequently Asked Questions]](#Frequently_Asked_Questions)
    -   [[2.1] [How does the script work?]](#How_does_the_script_work.3F)
    -   [[2.2] [What do I do if the migration fails or is interrupted?]](#What_do_I_do_if_the_migration_fails_or_is_interrupted.3F)
    -   [[2.3] [Do I need to reboot after the migration?]](#Do_I_need_to_reboot_after_the_migration.3F)
    -   [[2.4] [How much disk space do I need?]](#How_much_disk_space_do_I_need.3F)
    -   [[2.5] [I\'m using some exotic filesystem. Will this work on my system?]](#I.27m_using_some_exotic_filesystem._Will_this_work_on_my_system.3F)
    -   [[2.6] [AppArmor]](#AppArmor)
-   [[3] [External resources]](#External_resources)

## [Migration]

** Important**\
If [merge-usr] is being used to perform an upgrade to a 23.0 profile, OpenRC users must run this **post**-migration, while systemd users must run this **pre**-migration.

Here is an overview of the filesystem before the migration:

`user `[`$`]`tree -L 1 /`

    /
    ├── bin
    ├── boot
    ├── dev
    ├── etc
    ├── home
    ├── lib
    ├── lib64
    ├── lost+found
    ├── media
    ├── mnt
    ├── opt
    ├── proc
    ├── root
    ├── run
    ├── sbin
    ├── srv
    ├── sys
    ├── tmp
    ├── usr
    └── var

In the merged-usr layout, [/bin] and [/lib] are symlinks targeted at corresponding directories under the [/usr] directory.

To perform a migration, install the [[[sys-apps/merge-usr]](https://packages.gentoo.org/packages/sys-apps/merge-usr)[]] package.

`root `[`#`]`emerge --ask --oneshot sys-apps/merge-usr`

It is recommended to attempt a dry run first to find any conflicts and correct them first which may involve deleting some conflicting files.

**If in doubt, please seek support in a Gentoo [support](https://wiki.gentoo.org/wiki/Support "Support") channel first.**

`user `[`$`]`merge-usr --dryrun`

After all conflicts are resolved, the script may then be run without options as root to perform the actual migration:

`root `[`#`]`merge-usr`

Here is an overview of the filesystem after the migration:

`user `[`$`]`tree -L 1 /`

    /
    ├── bin -> usr/bin
    ├── boot
    ├── dev
    ├── etc
    ├── home
    ├── lib -> usr/lib
    ├── lib64 -> usr/lib64
    ├── lost+found
    ├── media
    ├── mnt
    ├── opt
    ├── proc
    ├── root
    ├── run
    ├── sbin -> usr/bin
    ├── srv
    ├── sys
    ├── tmp
    ├── usr
    └── var

Then switch to a merged-usr profile, for example for a 23.0 profile using OpenRC:

`root `[`#`]`eselect profile set default/linux/amd64/23.0`

or, for a 17.1 profile using SystemD:

`root `[`#`]`eselect profile set default/linux/amd64/17.1/systemd/merged-usr`

Next, complete a world upgrade with \--newuse or \--changed-use:

`root `[`#`]`emerge --ask -uDN @world`

Finally, you can remove the [[[sys-apps/merge-usr]](https://packages.gentoo.org/packages/sys-apps/merge-usr)[]] package since it is no longer needed:

`root `[`#`]`emerge --ask -C sys-apps/merge-usr`

### [Manual Migration]

It\'s highly unlikely a user will need these steps however, in cases of testing merge-usr on new profiles it is possible to break [portage] so these steps will get the system working again quickly.

Begin by downloading the script from the [GitHub page](https://github.com/floppym/merge-usr):

`user `[`$`]`wget `[`https://raw.githubusercontent.com/floppym/merge-usr/master/merge-usr`](https://raw.githubusercontent.com/floppym/merge-usr/master/merge-usr)

`user `[`$`]`chmod +x merge-usr`

Next, complete the migration as normal:

`user `[`$`]`./merge-usr --dryrun`

After all conflicts are resolved, the script may then be run without options as root to perform the actual migration:

`root `[`#`]`./merge-usr`

## [Frequently Asked Questions]

### [][How does the script work?]

It completes the following steps:

1.  For each directory [D] in ([bin], [sbin], [lib\*]), the script compares the contents of [/D] to [/usr/D] (except /sbin goes to /usr/bin).
2.  For each file or symlink it finds in [/D], it checks to see if the same object exists in [/usr/D]. If there are no conflicts, the file is moved from [/D] to [/usr/D]. If conflicts exist, an error message is output.
3.  If [/D] and [/usr/D] reside on the same filesystem, hard links are used to avoid copying any data. Otherwise, the file is copied along with any permissions, timestamps, and extended attributes.
4.  The original file in [/D] is replaced with a symlink to the new path under [/usr/D].
5.  Once all files have been moved, [/D] is replaced with a symlink to [/usr/D].

In the end, for each directory [D] in [bin], [sbin], [lib\*], these are all symlinked directories into [/usr/D]. Individual files have been moved and are not symlinked.

### [][What do I do if the migration fails or is interrupted?]

Generally, it is safe to just re-run the script after correcting the error. In case of an unsolvable error, the [[#gentoo](ircs://irc.libera.chat/#gentoo)] ([[webchat](https://web.libera.chat/#gentoo)]) channel is a good place to seek help - see the [support](https://wiki.gentoo.org/wiki/Support "Support") article.

### [][Do I need to reboot after the migration?]

This isn\'t strictly necessary, but it\'s probably a good idea in case any system services are holding open files under the directories that have been replaced with symlinks.

### [][How much disk space do I need?]

If the contents of the [/bin] and [/lib] directories live on the same filesystem as [/usr/bin] and [/usr/lib], the disk space requirement is very small. Only a minuscule amout of space is needed for some hard links and symlinks.

If [/bin] and [/lib] live on a different filesystem from [/usr/bin] and [/usr/lib], it will be necessary to ensure that [/usr] is large enough to hold the copied files. The [du] command can be used to calculate space consumption.

The following will output a human readable summary of disk space for the [/usr] directory:

`root `[`#`]`du -sh /usr`

Repeat the same for [/bin] and [/lib] to determine if they will fit under [/usr].

### [][I\'m using some exotic filesystem. Will this work on my system?]

The script has been well-tested with typical filesystems --- [ext2](https://wiki.gentoo.org/wiki/Ext2 "Ext2"), [ext3](https://wiki.gentoo.org/wiki/Ext3 "Ext3"), [ext4](https://wiki.gentoo.org/wiki/Ext4 "Ext4"), [XFS](https://wiki.gentoo.org/wiki/XFS "XFS"), [btrfs](https://wiki.gentoo.org/wiki/Btrfs "Btrfs"), [ZFS](https://wiki.gentoo.org/wiki/ZFS "ZFS") and [bcachefs](https://wiki.gentoo.org/wiki/Bcachefs "Bcachefs") --- on local storage. The script can work on remote storage too, but some manual intervention is required.

The script does work on [NFS](https://wiki.gentoo.org/wiki/NFS "NFS"), for example, but some paths must be manually cleaned up after rebooting, due to the weird way NFS deals with deletion of open files. The script will warn about the paths that could not be deleted automatically.

The script has also been tested on [overlayfs](https://wiki.gentoo.org/wiki/Overlayfs "Overlayfs"). The replacement of directories with symlinks is slightly less atomic than with other filesystems because overlayfs does not allow directories to be renamed in a single operation.

If an issue is encountered with some other exotic filesystem, please report a [bug](https://wiki.gentoo.org/wiki/Bugzilla/Bug_report_guide "Bugzilla/Bug report guide").

Feel free to [add a note](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide") to this article, in case of a positive experience with some other filesystem.

### [AppArmor]

If custom profiles are used for [AppArmor](https://wiki.gentoo.org/wiki/AppArmor "AppArmor"), these must be checked (with [ps auxZ] or [aa-status]) and changed. Because [/usr/sbin] is only a path to [/usr/bin], profiles that still use a call via [/usr/sbin] are no longer loaded.

## [External resources]

-   Gentoo news item - [/usr merge for systemd users](https://www.gentoo.org/support/news-items/2022-12-01-systemd-usrmerge.html)
-   Bugtracker for usrmerge related bugs [[[bug #690294]](https://bugs.gentoo.org/show_bug.cgi?id=690294)[]]
-   [The Case for the [/usr] Merge](https://www.freedesktop.org/wiki/Software/systemd/TheCaseForTheUsrMerge/)