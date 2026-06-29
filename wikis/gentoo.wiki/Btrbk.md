**Resources**

[[]][Home](https://digint.ch/btrbk/)

[[]][Package information](https://packages.gentoo.org/packages/app-backup/btrbk)

[[]][Official documentation](https://digint.ch/btrbk/doc/readme.html)

[[]][btrbk(1)](https://digint.ch/btrbk/doc/btrbk.1.html)

[[]][btrbk.conf(5)](https://digint.ch/btrbk/doc/btrbk.conf.5.html)

**btrbk** is a tool for creating incremental snapshots and remote backups of [Btrfs](https://wiki.gentoo.org/wiki/Btrfs "Btrfs") subvolumes. It is used for simple backups to an external [hard drive](https://wiki.gentoo.org/wiki/HDD "HDD") as well as more complex scenarios, like a server pulling the backups from all computers in the network or just to make local snapshots to protect against accidental deletions.

## Contents

-   [[1] [Terminology]](#Terminology)
-   [[2] [Installation]](#Installation)
-   [[3] [Configuration]](#Configuration)
    -   [[3.1] [Snapshotting subvolumes]](#Snapshotting_subvolumes)
    -   [[3.2] [Backing up subvolumes]](#Backing_up_subvolumes)
        -   [[3.2.1] [Backing up the root subvolume]](#Backing_up_the_root_subvolume)
        -   [[3.2.2] [Backing up standard subvolumes]](#Backing_up_standard_subvolumes)
    -   [[3.3] [Remote Backups]](#Remote_Backups)
        -   [[3.3.1] [SSH configuration]](#SSH_configuration)
            -   [[3.3.1.1] [Enable and Restrict Root Login]](#Enable_and_Restrict_Root_Login)
            -   [[3.3.1.2] [Generate keys]](#Generate_keys)
        -   [[3.3.2] [Backing up to another host using SSH]](#Backing_up_to_another_host_using_SSH)
        -   [[3.3.3] [Pull backups from another host using SSH]](#Pull_backups_from_another_host_using_SSH)
-   [[4] [Usage]](#Usage)
    -   [[4.1] [Dry run]](#Dry_run)
    -   [[4.2] [Run a full backup]](#Run_a_full_backup)
    -   [[4.3] [Create snapshots]](#Create_snapshots)
    -   [[4.4] [Automation with cron]](#Automation_with_cron)

## [Terminology]

btrbk has terms for the snapshots and backups it creates based on where they\'re stored and their intended purpose:

-   *Snapshots* are locally (on the same filesystem) stored [Btrfs snapshots](https://wiki.gentoo.org/wiki/Btrfs#Snapshots "Btrfs")
-   *Backups* are snapshots copied to a folder or over [SSH](https://wiki.gentoo.org/wiki/SSH "SSH")
-   *Archives* are extra copies of backups.

## [Installation]

`root `[`#`]`emerge --ask app-backup/btrbk`

## [Configuration]

** Tip**\
A commented example configuration file is found in [/etc/btrbk/btrbk.conf.example]. Refer to the [man page](https://digint.ch/btrbk/doc/btrbk.conf.5.html) for more details.

** Important**\
[btrbk] will not create the target directories, it must be created manually.

To backup subvolumes [etc], [var/log], and [var/lib] to [/media/backup/btrbk], with snapshots to [.btrbk_snapshots]:

[FILE] **`/etc/btrbk/btrbk.conf`Basic configuration**

    # Enable transaction logging
    transaction_log            /var/log/btrbk.log
    # Use a lockfile so only one btrbk instance can run at a time
    lockfile                   /run/lock/btrbk.lock
    # Use sudo if btrbk or lsbtr is run by regular user
    backend_local_user         btrfs-progs-sudo
    # Enable stream buffering
    stream_buffer              256m

    # Store snapshots under .btrbk_snapshots under the root of the volume
    snapshot_dir               .btrbk_snapshots
    # Only create new snapshots when changes have been made
    snapshot_create            onchange
    # Preserve hourly snapshots for up to 24 hours, and daily snapshots for up to 7 days
    snapshot_preserve          24h 7d 0w 0m 0y
    # The latest snapshot is always kept, regardless of the preservation policy
    snapshot_preserve_min      latest

    # Preserve daily backups for up to 14 days, weekly backups for up to 5 weeks, monthly backups for up to a month, and yearly backups for up to a year
    target_preserve            0h 14d 5w 1m 1y
    # Preserve the latest snapshot, regardless of the preservation policy
    target_preserve_min        latest
    # Preserve one archive of each type except hourly backups
    archive_preserve           0h 1d 1w 1m 1y
    archive_preserve_min       latest

    # Backup subvolumes at '/etc', '/var/lib' and '/var/log'
    volume /
      target /media/backup/btrbk
      subvolume etc
      subvolume var/lib
      subvolume var/log

### [Snapshotting subvolumes]

** Important**\
This method is *not* a proper backup as snapshots are stored on the same storage. Backups should be made to another system, or at least another storage device.

[FILE] **`/etc/btrbk/btrbk.conf`Make snapshots of Larry\'s homedir.**

    # Create simple snapshots of /home's subvolume 'larry' (replace as appropriate)
    # These are not sent to another device or machine (no 'target').
    #
    # Make sure snapshot_preserve_min / snapshot_preserve are set in the main config section!
    volume /home
      snapshot_dir .btrbk_snapshots
      subvolume    larry

### [Backing up subvolumes]

#### [Backing up the root subvolume]

To backup the root subvolume (the subvolume mounted at [/]) with the relative path to the top-level subvolume, the subvolume with `subvolid=5`, it must be mounted:

[FILE] **`/etc/fstab`fstab example with the top-level subvolume mounted at [/mnt/btr_pool] and *root* subvolume (named `@root` here) mounted at [/].**

    /dev/sda1  /              btrfs  subvol=@root  0 0
    /dev/sda1  /mnt/btr_pool  btrfs  subvolid=5    0 0

[FILE] **`/etc/btrbk/btrbk.conf`Backup the *root* subvolume to [/media/backup/btrbk].**

    volume /mnt/btr_pool
      target /media/backup/btrbk
      subvolume @root

#### [Backing up standard subvolumes]

[FILE] **`/etc/btrbk/btrbk.conf`Backup the *home* subvolume to [/media/backup/home_backups]**

    volume /
      target /media/backup/home_backups
      subvolume home

### [Remote Backups]

#### [SSH configuration]

##### [Enable and Restrict Root Login]

** Important**\
Root login must be enabled on the remote computer for this to work.

[FILE] **`/etc/ssh/sshd_config`**

    PermitRootLogin prohibit-password

To restrict the IPs/IP ranges from where root can log in, use the `Match` keyword. Consult the man page for *sshd_config* for details.

[FILE] **`/etc/ssh/sshd_config`**

    Match Address fd69::6:9
    PermitRootLogin prohibit-password
    Match All

##### [Generate keys]

Root login should only be performed using keys, not passwords. To generate a new root SSH key, and install it on a target system:

`root `[`#`]`ssh-keygen -t ed25519 -f /etc/btrbk/id_ed25519 `

`root `[`#`]`ssh-copy-id -i /etc/btrbk/id_ed25519.pub root@backup.example.org `

#### [Backing up to another host using SSH]

Backups can be made over SSH:

[FILE] **`/etc/btrbk/btrbk.conf`Backup homedirs to backup.example.org using SSH**

    ssh_identity               /etc/btrbk/ssh/id_ed25519
    ssh_user                   root

    volume /
      target ssh://backup.example.org:22/media/backup/home_backups
      subvolume @home

#### [Pull backups from another host using SSH]

This is an example configuration for multiple clients to backup onto a server:

[FILE] **`/etc/btrbk/btrbk.conf`**

    ssh_identity               /etc/btrbk/ssh/id_ed25519
    ssh_user                   root

    volume ssh://larry-desktop.example.org:22/mnt/btr_pool
      target /media/backup/larry-desktop
        subvolume @root
        subvolume @home

    volume ssh://larry-laptop.example.org:22/mnt/btr_pool
      target /media/backup/larry-laptop
        subvolume @root

For more examples, take a look at the official documentation hyperlinked at the top right of this page.

## [Usage]

### [Dry run]

To do a verbose dry run:

`root `[`#`]`btrbk --dry-run --verbose run`

### [Run a full backup]

To create snapshots and backup (if a target was configured), run:

`root `[`#`]`btrbk run`

### [Create snapshots]

To only create snapshots even if a target is configured, run:

`root `[`#`]`btrbk snapshot`

### [Automation with cron]

** Tip**\
Don\'t forget to mark the cron scripts executable:

`user `[`$`]`chmod +x /etc/cron.hourly/btrbk-snapshot /etc/cron.daily/btrbk-run`

[FILE] **`/etc/cron.hourly/btrbk-snapshot`Local snapshots once an hour**

    #!/bin/sh
    exec /usr/bin/btrbk -q snapshot

\

[FILE] **`/etc/cron.daily/btrbk-run`Backup once a day**

    #!/bin/sh
    exec /usr/bin/btrbk -q run