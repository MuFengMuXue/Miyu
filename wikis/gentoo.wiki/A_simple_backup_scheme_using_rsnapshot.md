**Resources**

[[]][Home](https://rsnapshot.org/)

[[]][GitHub](https://github.com/rsnapshot/rsnapshot)

[rsnapshot] is an automated [backup](https://wiki.gentoo.org/wiki/Backup "Backup") tool based on the [rsync](https://en.wikipedia.org/wiki/Rsync "wikipedia:Rsync") protocol and written in Perl. rsnapshot makes a specified number of incremental backups of specified file trees using [hard links](https://en.wikipedia.org/wiki/Hard_link "wikipedia:Hard link") to save space on the backup medium.

The following backup scheme will rotate the backups on a daily, weekly, and monthly basis. That means, it will keep a daily snapshot for 7 days, a weekly snapshot for 4 weeks and a monthly snapshot for 12 month. Furthermore, it uses an extra partition for the backup which will be mounted only for the time of the backup process.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [Emerge]](#Emerge)
-   [[2] [Configuration]](#Configuration)
    -   [[2.1] [fstab]](#fstab)
    -   [[2.2] [Cron scripts]](#Cron_scripts)
    -   [[2.3] [rsnapshot configuration files]](#rsnapshot_configuration_files)
    -   [[2.4] [Using rsyncd on a trusted LAN]](#Using_rsyncd_on_a_trusted_LAN)
-   [[3] [Usage]](#Usage)
    -   [[3.1] [Restoration]](#Restoration)
-   [[4] [Possible improvements]](#Possible_improvements)
    -   [[4.1] [BTRFS snapshots]](#BTRFS_snapshots)
-   [[5] [Complete system backup on a local drive]](#Complete_system_backup_on_a_local_drive)
    -   [[5.1] [Configuration]](#Configuration_2)
    -   [[5.2] [Restoration]](#Restoration_2)
-   [[6] [See also]](#See_also)

## [Installation]

### [Emerge]

Install [[[app-backup/rsnapshot]](https://packages.gentoo.org/packages/app-backup/rsnapshot)[]]:

`root `[`#`]`emerge --ask app-backup/rsnapshot`

## [Configuration]

### [fstab]

Assumed the backup partition is labeled *backup*, formatted with [ext4](https://wiki.gentoo.org/wiki/Ext4 "Ext4") and it should be mounted on [/mnt/backup] during backup: Add an entry like the following in [fstab](https://wiki.gentoo.org/wiki//etc/fstab "/etc/fstab"):

[FILE] **`/etc/fstab`**

    LABEL=backup    /mnt/backup    ext4    noatime,noauto    0 0

The `noauto` option means that this backup filesystem will not be mounted by default. The backup filesystem would normally be on an external device to be safe in the case of a device failure.

### [Cron scripts]

Create [cron](https://wiki.gentoo.org/wiki/Cron "Cron") scripts for the different backup intervals:

[FILE] **`/etc/cron.daily/rsnapshot.daily`**

    #!/bin/sh
    echo "### RSNAPSHOT DAILY ###"
    mount /mnt/backup && rsnapshot daily || echo "Backup failure"
    umount /mnt/backup
    echo ""

[FILE] **`/etc/cron.weekly/rsnapshot.weekly`**

    #!/bin/sh
    echo "### RSNAPSHOT WEEKLY ###"
    mount /mnt/backup && rsnapshot weekly || echo "Backup failure"
    umount /mnt/backup
    echo ""

[FILE] **`/etc/cron.monthly/rsnapshot.monthly`**

    #!/bin/sh
    echo "### RSNAPSHOT MONTHLY ###"
    mount /mnt/backup && rsnapshot monthly || echo "Backup failure"
    umount /mnt/backup
    echo ""

** Note**\
These scripts must be executable before they will run.

** Note**\
rsnapshot knows nothing about timing. The daily, weekly and monthly parameters are identifiers for rsnapshot without any semantic meaning. Therefore, it is important to call the daily snapshot only once a day, to call the weekly snapshot only once a week, etc.

### [rsnapshot configuration files]

Set up the rsnapshot configuration file.

** Note**\
rsnapshot configuration files are **tab delimited**. Be careful to always use tabs instead of spaces for the options.

** Note**\
Filetree specifications are in *rsync* format. See the *rsync* [man page](https://wiki.gentoo.org/wiki/Man_page "Man page") for details.

Default rsnapshot config file:

[FILE] **`/etc/rsnapshot.conf`**

    # Default config version
    config_version  1.2

    # So the hard disk is not polluted in case the backup filesystem is not available
    no_create_root  1

    # Standard settings
    cmd_cp          /bin/cp
    cmd_rm          /bin/rm
    cmd_rsync       /usr/bin/rsync
    link_dest       1

    # For convenience, so that mount points can be taken as backup starting points
    one_fs          1

    # Store all backups in one directory per machine
    # A useful alternative may be to create a separate directory for each interval
    snapshot_root   /mnt/backup/

    # increments, which are kept
    retain  daily    7
    retain  weekly   4
    retain  monthly  12

    # Backup folder(s)/files
    backup  /path/to/something/  localhost/
    backup  /var/            localhost/

    # Exclude pattern (refer to --exclude-from from rsync man page)
    exclude     /path/to/something/tmp/

In these files, the second argument of *backup* specifies a container directory for the backups, usually referring to the machine (in this case, *localhost*). This can be changed to any name of your choosing. The final snapshots will be saved under [/mnt/backup/.\[0-9\]\*/localhost/path/to/something/]

** Note**\
rsnapshot will always take the last daily snapshot to create the first weekly snapshot and the last weekly snapshot to create the first monthly one. It will not take the 7th daily snapshot to create the first weekly snapshot. Therefore, it is possible to keep less or more than 7 daily snapshots, but is this case the first weekly snapshot is not one week old.

### [Using rsyncd on a trusted LAN]

Following the [Home router Rsync server](https://wiki.gentoo.org/wiki/Home_router#Rsync_server "Home router") you can setup a rsync daemon on your source computer with a share like:

[FILE] **`/etc/rsyncd.conf`**

    [larry]
      path = /home/larry
      comment = Larry's home directory
      exclude = /foo

On the destination server, which runs rsnapshot, define a backup line in /etc/rsnapshot.conf like:

[FILE] **`/etc/rsnapshot.conf`**

    backup    larry@my_computer::larry larry/

Pay attention to highly insecure mechanism without password checking or encrypted transfer.

## [Usage]

### [Restoration]

To restore the *localhost* backups specified above, we would use:

`root `[`#`]`mount /mnt/backup `

`root `[`#`]`rsync -a /mnt/backup/localhost/monthly.0/localhost/. /mnt/myroot/ `

`root `[`#`]`rsync -a /mnt/backup/localhost/weekly.0/localhost/. /mnt/myroot/ `

`root `[`#`]`rsync -a /mnt/backup/localhost/daily.0/localhost/. /mnt/myroot/ `

where [/mnt/myroot] is the mount point of the fresh root filesystem. In the paths above *\*.0* refers to the latest increment.

## [Possible improvements]

It is also possible to make remote backups via **rsync** or **[SSH](https://en.wikipedia.org/wiki/Secure_Shell "wikipedia:Secure Shell")** \-- see the *rsnapshot* man page for details or [Advanced backup using rsnaphot](https://wiki.gentoo.org/wiki/Advanced_backup_using_rsnaphot "Advanced backup using rsnaphot").

### [BTRFS snapshots]

Those using btrfs can leverage its snapshotting abilities with rsnapshot. Walter Werther has a [guide](http://it.werther-web.de/2011/10/23/migrate-rsnapshot-based-backup-to-btrfs-snapshots/) on this.

## [Complete system backup on a local drive]

In that example, we will make a complete system backup and restoration using an USB drive.

### [Configuration]

In addition to what have been said, we must make a few other configuration changes.

** Note**\
The exact content of the include, exclude, include_file and exclude_file lists will depend on the installed software. Use *equery f PKG* to get the list of files installed by PKG. See the *equery* [man page](https://wiki.gentoo.org/wiki/Man_page "Man page") for details. The main issue here is than files created at run time in */var* can have permissions which can make the *rsync* restoration to stop in the middle.

Set up the rsnapshot configuration file:

[FILE] **`/etc/rsnapshot.conf`**

    # All snapshots will be stored under this root directory.
    # Path to the backup media root directory:
    snapshot_root   /media/MaxiTux/snapshots/

    # Default rsync args. All rsync commands have at least these options set.
    #
    rsync_short_args    -aAHSX
    rsync_long_args --delete --numeric-ids --relative --delete-excluded

    # The include and exclude parameters, if enabled, simply get passed directly
    # to rsync. If you have multiple include/exclude patterns, put each one on a
    # separate line. Please look up the --include and --exclude options in the
    # rsync man page for more details on how to specify file name patterns.
    exclude /dev/*
    exclude /home/*/.thumbnails/*
    #exclude   /home/*/.cache/google-chrome/*
    exclude /home/*/.local/share/Trash/*
    exclude /lost+found/*
    exclude /media/*
    exclude /mnt/*
    exclude /proc/*
    exclude /sys/*
    exclude /run/*
    exclude /tmp/*
    exclude /var/lib/dhcpcd/*
    exclude /var/lib/nfs/*
    exclude /resume_swap

    # The include_file and exclude_file parameters, if enabled, simply get
    # passed directly to rsync. Please look up the --include-from and
    # --exclude-from options in the rsync man page for more details.
    include_file    /var/lib/nfs/.keep_net-fs_nfs-utils-0

    ###############################
    ### BACKUP POINTS / SCRIPTS ###
    ###############################
    backup  /        localhost/

### [Restoration]

To restore the *localhost* backups specified above, we would use:

`root `[`#`]`mount /media/MaxiTux `

`root `[`#`]`rsync -a /media/MaxiTux/snapshots/daily.0/localhost/. / `

** Note**\
This command assume you are making the restoration on a running system. This can cause random issues with some running software, which can or not be fixed after a software restart or a system reboot. An alternative is to to stop these software when making the restoration. Another alternative is to reboot the computer with a Gentoo minimal installation CD, a Gentoo admin CD or any live linux media. How to mount drives into a live Gentoo system is explained into [dd#Hard_disk_backup](https://wiki.gentoo.org/wiki/Dd#Hard_disk_backup "Dd"). The same remark is true during the backup process: you may have to stop some software in order to get a consistent backup.

## [See also]

-   [Advanced backup using rsnaphot](https://wiki.gentoo.org/wiki/Advanced_backup_using_rsnaphot "Advanced backup using rsnaphot") --- describes a advanced automated remote backup scheme using the tool [rsnapshot] as non-root user