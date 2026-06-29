[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=BorgBackup&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

**Resources**

[[]][Home](https://www.borgbackup.org)

[[]][Official documentation](https://borgbackup.readthedocs.io/en/stable/index.html)

[[]][GitHub](https://github.com/borgbackup/borg)

[[]][Package information](https://packages.gentoo.org/packages/app-backup/borgbackup)

BorgBackup (short: Borg) is a deduplicating backup program. Optionally, it supports compression and authenticated encryption.

The main goal of Borg is to provide an efficient and secure way to back up data. The data deduplication technique used makes Borg suitable for daily backups since only changes are stored. The authenticated encryption technique makes it suitable for backups to targets not fully trusted.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
-   [[2] [Compatibility]](#Compatibility)
-   [[3] [Usage]](#Usage)
    -   [[3.1] [Initializing a new repository]](#Initializing_a_new_repository)
    -   [[3.2] [Backing up directories]](#Backing_up_directories)
    -   [[3.3] [Listing archives in a repository]](#Listing_archives_in_a_repository)
    -   [[3.4] [Listing contents of an archive]](#Listing_contents_of_an_archive)
    -   [[3.5] [Restoring an archive]](#Restoring_an_archive)
    -   [[3.6] [Deleting an archive]](#Deleting_an_archive)
    -   [[3.7] [Pruning a repository]](#Pruning_a_repository)
    -   [[3.8] [Compacting a repository]](#Compacting_a_repository)
    -   [[3.9] [Mounting a repository]](#Mounting_a_repository)
-   [[4] [See also]](#See_also)

## [[] Installation]

### [[] USE flags]

### [USE flags for] [app-backup/borgbackup](https://packages.gentoo.org/packages/app-backup/borgbackup) [[]] [Deduplicating backup program with compression and authenticated encryption]

  ------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [`debug`](https://packages.gentoo.org/useflags/debug)   Enable extra debug codepaths, like asserts and extra output. If you want to get meaningful backtraces see https://wiki.gentoo.org/wiki/Project:Quality_Assurance/Backtraces
  [`test`](https://packages.gentoo.org/useflags/test)     Enable dependencies and/or preparations necessary to run tests (usually controlled by FEATURES=test but can be toggled independently)
  ------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-04-03 14:40] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [[] Emerge]

`root `[`#`]`emerge --ask app-backup/borgbackup`

## [[] Compatibility]

There is a planned compatibility break in the development, not-yet-released 2.0 version. See the \"Breaking compatibility\" [section](https://www.borgbackup.org/releases/borg-2.0.html) of the preliminary release notes, as well as the [general note](https://borgbackup.readthedocs.io/en/latest/#compatibility-notes) in its documentation.

In the past, there have also been [compatibility issues](https://borgbackup.readthedocs.io/en/stable/faq.html#path-to-repo-is-not-a-valid-repository-check-repo-config) with old clients and new repositories, as well as when [mixing](https://github.com/borgbackup/borg/discussions/7970#discussioncomment-11204436) different client versions because of security fixes.

## [[] Usage]

### [[] Initializing a new repository]

Before backups can be made, a repository must be initialized

`user `[`$`]`borg init --encryption=repokey /path/to/repo`

### [[] Backing up directories]

`user `[`$`]`borg create /path/to/repo::ArchiveName ~/src ~/Documents`

The archive name may include placeholders which will expanded by borg, e.g. \'-\' would become something like \'panther-2024-08-31T19:00:00\'

Statistics can be output with the `--stats` argument.

`user `[`$`]`borg create --stats /path/to/repo::ArchiveName ~/src ~/Documents`

    -----------------------------------------------------------------------------
    Archive name: ArchiveName
    Archive fingerprint: bd31004d58f51ea06ff735d2e5ac49376901b21d58035f8fb05dbf866566e3c2
    Time (start): Tue, 2016-02-16 18:15:11
    Time (end):   Tue, 2016-02-16 18:15:11

    Duration: 0.19 seconds
    Number of files: 127
    ------------------------------------------------------------------------------
                          Original size      Compressed size    Deduplicated size
    This archive:                4.16 MB              4.17 MB             26.78 kB
    All archives:                8.33 MB              8.34 MB              4.19 MB

                          Unique chunks         Total chunks
    Chunk index:                     132                  261
    ------------------------------------------------------------------------------

### [[] Listing archives in a repository]

`user `[`$`]`borg list /path/to/repo`

    First                               Mon, 2016-02-15 19:14:44
    Second                              Tue, 2016-02-16 19:15:11

### [[] Listing contents of an archive]

`user `[`$`]`borg list /path/to/repo::ArchiveName`

    drwxr-xr-x user   group          0 Mon, 2016-02-15 18:22:30 home/user/Documents
    -rw-r--r-- user   group       7961 Mon, 2016-02-15 18:22:30 home/user/Documents/Important.doc
    ...

### [[] Restoring an archive]

`user `[`$`]`borg extract /path/to/repo::ArchiveName`

### [[] Deleting an archive]

`user `[`$`]`borg delete /path/to/repo::ArchiveName`

### [[] Pruning a repository]

Pruning a repository allows borg to delete archives that do not need to be retained. This is useful for managing automated backups.

`user `[`$`]`borg prune --keep-daily=7 --keep-weekly=4 --keep-monthly=6 /path/to/repo`

Afterwards, use **borg compact** to free up repository disk space

### [[] Compacting a repository]

Compacting a repository allows borg to recover disk space by compacting segment files

`user `[`$`]`borg compact /path/to/repo`

### [[] Mounting a repository]

Mounting a repository uses FUSE to make the archives available as directories at the mount point, which is useful for browsing or restoring files and directories.

`user `[`$`]`borg mount /path/to/repo /mount/point`

`user `[`$`]`ls -l /mount/point`

    drwxr-xr-x 1 root root 0 2024-03-31 19:00 hostname-2024-03-31T19:00:00
    drwxr-xr-x 1 root root 0 2024-04-30 19:00 hostname-2024-04-30T19:00:01
    ...

It is also possible to mount a single archive

`user `[`$`]`borg mount /path/to/repo::ArchiveName /mount/point`

To unmount afterwards:

`user `[`$`]`borg umount /mount/point`

## [See also]

-   [restic](https://wiki.gentoo.org/wiki/Restic "Restic") --- a [Go](https://wiki.gentoo.org/wiki/Go "Go")-based backup tool built simplicity, scalability, and verifiability in mind.
-   [dd](https://wiki.gentoo.org/wiki/Dd "Dd") --- a utility used to copy raw data from a source into sink, where source and sink can be a block device, file, or piped input/output.
-   [rsnapshot](https://wiki.gentoo.org/wiki/Rsnapshot "Rsnapshot") --- an automated [backup](https://wiki.gentoo.org/wiki/Backup "Backup") tool based on the [rsync](https://en.wikipedia.org/wiki/Rsync "wikipedia:Rsync") protocol and written in Perl.