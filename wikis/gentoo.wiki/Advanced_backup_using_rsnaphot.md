**Resources**

[[]][Home](https://rsnapshot.org/)

This article describes a advanced automated remote backup scheme using the tool [rsnapshot] as non-root user, which is based on [rsync](https://en.wikipedia.org/wiki/Rsync "wikipedia:Rsync").

**rsnapshot** makes a specified number of incremental backups of specified file trees from remote servers via ssh with non-user root using sudo, with help of [hard links](https://en.wikipedia.org/wiki/Hard_link "wikipedia:Hard link") to save space on the backup medium.

The following backup scheme will login to remote user `backup@remote.example.com` via ssh, fetch all required files with [rsync](https://en.wikipedia.org/wiki/Rsync "wikipedia:Rsync") to `backup.example.com` host, rotate the backups on a daily, weekly and monthly basis. That means, it will keep a daily snapshot for 7 days, a weekly snapshot for 4 weeks and a monthly snapshot for 12 month. Furthermore, it uses an extra partition for the backup which will be mounted only for the time of the backup process.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [Emerge]](#Emerge)
-   [[2] [Configuration]](#Configuration)
    -   [[2.1] [Remote server]](#Remote_server)
        -   [[2.1.1] [Backup user]](#Backup_user)
        -   [[2.1.2] [rsync wrapper]](#rsync_wrapper)
    -   [[2.2] [Backup server]](#Backup_server)
        -   [[2.2.1] [Backup user]](#Backup_user_2)
        -   [[2.2.2] [Directories]](#Directories)
        -   [[2.2.3] [SSH keys]](#SSH_keys)
        -   [[2.2.4] [rsnapshot]](#rsnapshot)
        -   [[2.2.5] [cron jobs]](#cron_jobs)
-   [[3] [MySQL backup]](#MySQL_backup)
-   [[4] [PostgreSQL backup]](#PostgreSQL_backup)
-   [[5] [Restoration]](#Restoration)
    -   [[5.1] [MySQL]](#MySQL)
-   [[6] [Possible improvements]](#Possible_improvements)
-   [[7] [See also]](#See_also)
-   [[8] [External resources]](#External_resources)

## [Installation]

### [Emerge]

Install [[[app-backup/rsnapshot]](https://packages.gentoo.org/packages/app-backup/rsnapshot)[]]:

`root `[`#`]`emerge --ask app-backup/rsnapshot`

## [Configuration]

### [Remote server]

First, we will setup remote host `remote.example.com` for backup. Remote host is host, which we want backup. For example, it is Gentoo server, that serves web server and MySQL database.

#### [Backup user]

All operations on remote server will be executed from non-root user. Lets create such user:

`root@remote.example.com #``useradd -m backup`

Backup user must have permissions to run [rsync](https://wiki.gentoo.org/wiki/Rsync "Rsync") as root, as most of files on `remote.example.com` belong to root or other users. As we need to backup them, [rsync](https://wiki.gentoo.org/wiki/Rsync "Rsync") requires root permissions. Lets give those permission to it:

`root@remote.example.com #``vim /etc/sudoers`

And add to sudoers to group `backup` ability to run \[rsync\] from root

[FILE] **`/etc/sudoers`**

    ...
    # backup group can do anything
    %backup ALL=(ALL) NOPASSWD: /usr/bin/rsync
    ...

#### [rsync wrapper]

Remote backup server `backup.example.com` will login to this server and execute `backup@remote.example.com:~/rsync-wrappper.sh` command. This wrapper requires for [sudo](https://wiki.gentoo.org/wiki/Sudo "Sudo"). Lets create those dummy wrapper script

[FILE] **`/home/backup/rsync-wrapper.sh`**

    #!/bin/sh

    logger -t backup $@
    /usr/bin/sudo /usr/bin/rsync "$@";

And give executable flag for those script

`backup@remote.example.com $``chmod ug+x /home/backup/rsync-wrapper.sh`

That all. This `remote.example.com` ready for remote backuping

### [Backup server]

Backup server will connect to `backup@remote.example.com` server via ssh public key. All backup files will be save to [/mnt/backup] directory.

#### [Backup user]

SSH keys, configurations for backup will be stored in backup user `backup@backup.example.com` Lets create those user and group

`root@backup.example.com #``useradd -m backup`

#### [Directories]

All backups will be saving to [/mnt/backup] directory. We will create backup directory

`root@backup.example.com #``mkdir -p /mnt/backup `

`root@backup.example.com #``chown backup:backup /mnt/backup `

`root@backup.example.com #``chmod 770 /mnt/backup `

#### [SSH keys]

[rsnapshot](https://wiki.gentoo.org/wiki/Rsnapshot "Rsnapshot") will login to remote servers via ssh public keys. Lets generate private/public ssh keys for all next ssh sessions.

`root@backup.example.com #``sudo -i -u backup`

`backup@backup.example.com $``ssh-keygen`

Save ssh keys to default path without password. After this, copy ssh key to remote server with ssh-copy-id:

`backup@backup.example.com $``ssh-copy-id backup@remote.example.com`

And lets recheck, that everything is file

`backup@backup.example.com $``ssh remote.example.com`

No password should be asked and you simply login to **remote.example.com**

#### [rsnapshot]

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
    cmd_cp                  /bin/cp
    cmd_rm                  /bin/rm
    cmd_rsync               /usr/bin/rsync
    cmd_ssh                 /usr/bin/ssh
    link_dest               1

    rsync_long_args         -evaAX --numeric-ids --rsync-path=/home/backup/rsync-wrapper.sh
    ssh_args                -i /home/backup/.ssh/id_rsa

    # For convenience, so that mount points can be taken as backup starting points
    one_fs                  1

    # Store all backups in one directory per machine
    # A useful alternative may be to create a separate directory for each interval
    snapshot_root   /mnt/backup/

    # increments, which are kept
    retain  daily   7
    retain  weekly  4
    retain  monthly 12

    # Exclude pattern (refer to --exclude-from from rsync man page)
    exclude         /dev/*
    exclude         /proc/*
    exclude         /sys/*
    exclude         /run/*
    exclude         /var/tmp/*
    exclude         /var/run/*
    exclude         /tmp/*
    exclude         /usr/portage/distfiles/*
    exclude         /lost+found

    # backup of remote.example.com server
    backup  backup@remote.example.com:/                remote.example.com/
    #backup backup@remote.example.com:/otherdir/       remote.example.com/otherdir

This files have such params:

`rsync_long_args` Parameters, that will directly passed to *rsync* command:

       -e specify the remote shell to use
       -v increase verbosity
       -a archive mode. Cause rsync to backup file owners and permissions
       -A acl. This option causes rsync to update the destination extended acl attributes to be the same as the source ones
       -X xattrs. This option causes rsync to update the destination extended attributes to be the same as the source ones
       rsync-path Execute on remote server rsync wrapper script /home/backup/rsync-wrapper.sh

`ssh_args` Path to public key, that should be used for remote ssh login

`snapshot_root` Path to directory, where all backup files will be stored

`backup` specifies a container directory for the backups, usually referring to the machine (in this case, *example.com*). This can be changed to any name of your choosing. The final snapshots will be saved under [/mnt/backup/.\[0-9\]\*/example.com/]

`exclude` This directory will be excluded from backup

** Note**\
To check rnsnapshot configuration file for errors, run

`user `[`$`]`rsnapshot configtest`

** Note**\
rsnapshot will always take the last daily snapshot to create the first weekly snapshot and the last weekly snapshot to create the first monthly one. It will not take the 7th daily snapshot to create the first weekly snapshot. Therefore, it is possible to keep less or more than 7 daily snapshots, but is this case the first weekly snapshot is not one week old.

#### [cron jobs]

Add cron job to run backup-ing

`backup@backup.example.com $``crontab -e`

** Note**\
If you want full backup of remote system, with **full** backup of file owners, groups, permission, attributes, you should run rsnaphost cron jobs from **root** user. In other words, command below should be run from root

`root@backup.example.com #``crontab -e`

[FILE]

    #3am each day
    0 3 * * *    ionice -c 3 nice -n +19 /usr/bin/rsnapshot daily
    #4am each week
    0 4 * * 1    ionice -c 3 nice -n +19 /usr/bin/rsnapshot weekly
    #4am each month
    0 4 1 * *    ionice -c 3 nice -n +19 /usr/bin/rsnapshot monthly

rsnaphost jobs will run [rsnapshot] with minimum CPU and I/O priority.

## [MySQL backup]

** Note**\
This backup configuration are workable for small non-production databases, that doesn\'t have too many transactions. For more advanced MySQL backup, see [https://dev.mysql.com/doc/refman/5.7/en/backup-methods.html](https://dev.mysql.com/doc/refman/5.7/en/backup-methods.html) (replication or Binary Log backup)

Login to backup user:

`user@backup.example.com $``sudo -i -u backup`

Create file [.my.cnf] with such content

[FILE] **`/home/backup/.my.cnf`**

    [mysqldump]
    host = localhost
    port = 3306
    user = backup
    password = BACKUP_USER_PASSWORD

This file are used every time, when [mysqldump] tool will be called. Be sure, that only backup user have access to [/home/backup/.my.cnf] file

Create bash script mysql_dump.bash, that will for backup:

[FILE] **`/home/backup/mysql_dump.bash`**

    #/bin/bash
    /usr/bin/mysqldump --all-databases | bzip2 -c > /backup/mysql/`date +%Y.%m.%d_%H.%M.%S.sql.bz2`

Add executable flag for script:

`user@backup.example.com $``chmod +x /home/backup/mysql_dump.bash`

Create directory [/backup/mysql], that contain all MySQL backups and grand permissions:

`root@backup.example.com #``mkdir -p /backup/mysql `

`root@backup.example.com #``chown backup /backup/mysql `

`root@backup.example.com #``chmod 700 /backup/mysql `

Create MySQL user [backup] with access to all databases (like root user, but for backup)

`root@backup.example.com #``mysql`

and type:

`mysql>``GRANT ALL PRIVILEGES ON *.* TO 'backup'@'localhost' IDENTIFIED BY 'BACKUP_USER_PASSWORD' `

Last step - create cron job, that will call mysql_dump.bash script and dump all databases. Execute from backup user

`backup@backup.example.com $``crontab -e`

and add such line (run every day at 01:00)

[FILE]

    0 1 * * * /home/backup/mysql_dump.bash

## [PostgreSQL backup]

To be DONE

## [Restoration]

To restore the *remote.example.com* backups specified above, we would use:

`root `[`#`]`mount /mnt/backup `

`root `[`#`]`rsync -aAX /mnt/backup/remote.example.com/monthly.0/remote.example.com/. /mnt/myroot/ `

`root `[`#`]`rsync -aAX /mnt/backup/remote.example.com/weekly.0/remote.example.com/. /mnt/myroot/ `

`root `[`#`]`rsync -aAX /mnt/backup/remote.example.com/daily.0/remote.example.com/. /mnt/myroot/ `

If backup are on remote server, rsync can be done via ssh

`root `[`#`]`rsync -aAX root@remote.example.com/monthly.0/remote.example.com/. /`

where [/mnt/myroot] is the mount point of the fresh root filesystem. In the paths above *\*.0* refers to the latest increment.

### [MySQL]

Technically, MySQL dump (created from upper section) are just bzipped text file with SQL commands to MySQL database. Those command will unzip archive, and send sql command to mysql

`root `[`#`]`bzcat /backup/mysql/some_ziped_archive.bz2 | mysql --user=root`

## [Possible improvements]

-   Use remote device for storing backups [/mnt/backup] - TO BE DONE
-   Use encryption to crypt backups [/mnt/backup] - TO BE DONE

## [See also]

-   [Rsnapshot](https://wiki.gentoo.org/wiki/Rsnapshot "Rsnapshot") --- an automated [backup](https://wiki.gentoo.org/wiki/Backup "Backup") tool based on the [rsync](https://en.wikipedia.org/wiki/Rsync "wikipedia:Rsync") protocol and written in Perl.

## [External resources]

-   [\[1\]](https://rsnapshot.org/rsnapshot/docs/docbook/rest.html) - Documentation from rsnapshot site with some help about configuring rsnapshot
-   [\[2\]](https://dev.kprod.net/linux-backup-rsnapshot-no-root) - HOWTO configure the same, but more general