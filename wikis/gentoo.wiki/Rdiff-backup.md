**Resources**

[[]][Home](http://www.nongnu.org/rdiff-backup/)

[[]][Wikipedia](https://en.wikipedia.org/wiki/Rdiff-backup "wikipedia:Rdiff-backup")

[rdiff-backup] is a GPL-licensed incremental backup utility based on librsync; it stores *changes* to files instead of entire duplications. This can greatly reduce storage requirements for backups. The resultant incremental data can be viewed and restored from as if it were whole file backups via [FUSE](https://wiki.gentoo.org/wiki/FUSE "FUSE")-based [rdiff-backup-fs].

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
-   [[2] [Usage]](#Usage)
    -   [[2.1] [Backup]](#Backup)
    -   [[2.2] [Restore]](#Restore)
    -   [[2.3] [cron]](#cron)
-   [[3] [External resources]](#External_resources)

## [Installation]

### [USE flags]

### [USE flags for] [app-backup/rdiff-backup](https://packages.gentoo.org/packages/app-backup/rdiff-backup) [[]] [Local/remote mirroring+incremental backup]

  ------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [`debug`](https://packages.gentoo.org/useflags/debug)   Enable extra debug codepaths, like asserts and extra output. If you want to get meaningful backtraces see https://wiki.gentoo.org/wiki/Project:Quality_Assurance/Backtraces
  ------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-05-13 13:29] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

`root `[`#`]`emerge --ask --verbose --tree rdiff-backup`

## [Usage]

### [Backup]

`user `[`$`]`rdiff-backup path/to/source path/to/backup/destination`

To backup again, simply run the exact same command; each increment will be individually accessible.

### [Restore]

The [cp] command can simply be used to copy a file from a backup created with rdiff-backup.

See [rdiff website](http://rdiff-backup.nongnu.org/examples.html#restore) for more examples.

### [cron]

`user `[`$`]`crontab -e`

[CODE]

    0 3 * * * rdiff-backup /path/to/source /path/to/backup/destination

## [External resources]

-   [rdiff-backup tutorial at howtoforge.com](https://www.howtoforge.com/linux_rdiff_backup)
-   [Unattended rdiff-backup HOWTO](http://arctic.org/~dean/rdiff-backup/unattended.html)
-   [A Debian based tutorial at linode.com](https://www.linode.com/docs/security/backups/using-rdiff-backup-with-sshfs/)