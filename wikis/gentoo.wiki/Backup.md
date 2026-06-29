**Resources**

[[]][Wikipedia](https://en.wikipedia.org/wiki/Backup "wikipedia:Backup")

**Backups** prevent loss of data by ensuring it can be recovered.

Backup and recovery go together: backups are never taken without supporting a recovery, and recovery cannot be completed without having a backup from which to recover. For this reason, many methods focus on the recovery side (as that is the most vital part of any backup scheme).

There are several backup methods available, ranging from bare-metal backup (and recovery) to record-based backups in a database system. Backup solutions offer a number of different features such as backup snapshots based on time, deduplication, the ability to recover single modified files or whole directory trees, etc.

## Contents

-   [[1] [Methods]](#Methods)
    -   [[1.1] [Bare metal recovery]](#Bare_metal_recovery)
    -   [[1.2] [File and directory recovery]](#File_and_directory_recovery)
    -   [[1.3] [Application-level backups]](#Application-level_backups)
-   [[2] [Important principles]](#Important_principles)
-   [[3] [Available software]](#Available_software)
-   [[4] [See also]](#See_also)

## [Methods]

### [Bare metal recovery]

In case of bare-metal recovery, software is used without installing it on the operating system that is under backup/recovery. The result of a bare-metal restore is a fully bootable system again.

Most of these recovery solutions are based on partition imaging (like with [dd](https://wiki.gentoo.org/wiki/Dd "Dd"), [CloneZilla](https://clonezilla.org/), [PartImage](https://www.partimage.org/), or [FSArchiver](https://www.fsarchiver.org/)), although in Gentoo, stage4 snapshots can also be used as some sort of bare-metal recovery solution (captures files, but not disk partition data).

### [File and directory recovery]

For a more selective approach, a file- and directory-based backup/recovery model is used. For such situations, on-system software is responsible for regularly taking copies (or patches/diffs) from a predefined list of files and directories. Many solutions exist, such as [Bacula](https://www.bacula.org/) or [BackupPC](https://backuppc.github.io/backuppc/), but simple schemes can also be obtained by properly using rsync or just plain copies.

### [Application-level backups]

Some applications offer a more specific approach on backup and restores. Databases are a prime example (as their job is to guard over data) but others, like version control systems, often have specific backup/restore routines too.

When hosting one or more services, it is wise to look at the backup/restore routines for each service and implement them on top of the other backup schemes.

## [Important principles]

A few principles need to be closely guarded when implementing backups:

1.  Always verify that the backups *can* be used to restore. Either restore to another location or system, or restore immediately after taking a backup. Too often users forget this and are severely disappointed when they find out that their daily backups didn\'t do much (e.g. captured the wrong directory) or cannot be restored.
2.  Keep backups on a safe location. Try to have them off premises. Move them regularly to a family members home, or send them over the Internet to a cloud storage provider (password-based encryption schemes can be used to protect confidentiality with off site backups).
3.  Mix backup methods. Take a full system (bare-metal) backup once in a while, with file and directory backups more regularly and application-level backups as much as possible (since those are what clients/users will be most likely angry about if lost).
4.  Mirroring is not having a backup. Mirroring keeps two sides in sync, whereas a backup is a snapshot of data at a point in time.

## [Available software]

This is a partial selection of data compression tools available in Gentoo. See [app-backup](https://packages.gentoo.org/categories/app-backup) on packages.gentoo.org, or use [eix](https://wiki.gentoo.org/wiki/Eix "Eix") ([[[app-portage/eix]](https://packages.gentoo.org/packages/app-portage/eix)[]]).

  -------------------------------------------------------------------------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Name                                                                       Package                                                                                                                                                                                                                                                                                                                                                                                       Description
  backintime                                                                 [[[app-backup/backintime]](https://packages.gentoo.org/packages/app-backup/backintime)[]]         Backup system inspired by TimeVault and FlyBack
  bacula                                                                     [[[app-backup/bacula]](https://packages.gentoo.org/packages/app-backup/bacula)[]]                     Featureful client/server network backup suite.
  backuppc                                                                   [[[app-backup/backuppc]](https://packages.gentoo.org/packages/app-backup/backuppc)[]]               High-performance backups to a server\'s disk.
  [BorgBackup](https://wiki.gentoo.org/wiki/BorgBackup "BorgBackup")         [[[app-backup/borgbackup]](https://packages.gentoo.org/packages/app-backup/borgbackup)[]]         Deduplicating backup program with support for compression and authenticated encryption.
  burp                                                                       [[[app-backup/burp]](https://packages.gentoo.org/packages/app-backup/burp)[]]                           Network backup and restore program, uses librsync to save network traffic and to reduce space used by each backup.
  [btrbk](https://wiki.gentoo.org/wiki/Btrbk "Btrbk")                        [[[app-backup/btrbk]](https://packages.gentoo.org/packages/app-backup/btrbk)[]]                        Tool for creating snapshots and remote backups of btrfs subvolumes.
  dar                                                                        [[[app-backup/dar]](https://packages.gentoo.org/packages/app-backup/dar)[]]                              Disk ARchive - full featured backup tool, aimed for disks.
  [dd](https://wiki.gentoo.org/wiki/Dd "Dd")                                 [[[sys-apps/coreutils]](https://packages.gentoo.org/packages/sys-apps/coreutils)[]]                  Utility used to copy raw data from source to sink, where source and sink can be a block device, file, or piped input/output.
  [Duplicity](https://wiki.gentoo.org/wiki/Duplicity "Duplicity")            [[[app-backup/duplicity]](https://packages.gentoo.org/packages/app-backup/duplicity)[]]            Secure backup system using gnupg to encrypt data
  [etckeeper](https://wiki.gentoo.org/wiki/Etckeeper "Etckeeper")            [[[sys-apps/etckeeper]](https://packages.gentoo.org/packages/sys-apps/etckeeper)[]]                  Collection of tools to let [/etc] be stored in a git, mercurial, bazaar, or darcs repository.
  fsarchiver                                                                 [[[app-backup/fsarchiver]](https://packages.gentoo.org/packages/app-backup/fsarchiver)[]]         Flexible filesystem archiver for backup and deployment tool.
  partimage                                                                  [[[sys-block/partimage]](https://packages.gentoo.org/packages/sys-block/partimage)[]]               Console-based application to efficiently save raw partition data to image file.
  [rdiff-backup](https://wiki.gentoo.org/wiki/Rdiff-backup "Rdiff-backup")   [[[app-backup/rdiff-backup]](https://packages.gentoo.org/packages/app-backup/rdiff-backup)[]]   GPL-licensed incremental backup utility based on librsync; it stores changes to files instead of entire duplications.
  [restic](https://wiki.gentoo.org/wiki/Restic "Restic")                     [[[app-backup/restic]](https://packages.gentoo.org/packages/app-backup/restic)[]]                     restic is a backup program that is fast, efficient and secure; it supports backends like AWS S3, Google Storage, Backblaze among others.
  [Rsnapshot](https://wiki.gentoo.org/wiki/Rsnapshot "Rsnapshot")            [[[app-backup/rsnapshot]](https://packages.gentoo.org/packages/app-backup/rsnapshot)[]]            Automated backup tool based on the rsync protocol and written in Perl.
  [rsync](https://wiki.gentoo.org/wiki/Rsync "Rsync")                        [[[net-misc/rsync]](https://packages.gentoo.org/packages/net-misc/rsync)[]]                              A powerful file sync program capable of efficient file transfers and directory synchronization.
  [tarsnap](https://www.tarsnap.com/)        [[[app-backup/tarsnap]](https://packages.gentoo.org/packages/app-backup/tarsnap)[]]                  Secure, open source, efficient online backups. Service is fairly priced; \"online backups for the truly paranoid.\"
  -------------------------------------------------------------------------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## [See also]

-   [Data compression](https://wiki.gentoo.org/wiki/Data_compression "Data compression") --- a list of some of the **compression and file-archiver utilities** available in Gentoo Linux