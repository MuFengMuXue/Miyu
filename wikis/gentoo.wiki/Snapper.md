[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=Snapper&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

**Resources**

[[]][Home](http://snapper.io/)

[[]][GitHub](https://github.com/openSUSE/snapper)

[[]][Official documentation](http://snapper.io/documentation.html)

**Snapper** is a command-line program to create and manage filesystem snapshots, allowing viewing or reversion of changes.

Snapper has the ability to create, delete, compare, and undo changes between snapshots. Snapper never modifies the content of snapshots, creating read-only snapshots (if supported by the system\'s kernel). It can work with privileged and non-privileged users.

Snapper mainly targets [btrfs](https://wiki.gentoo.org/wiki/Btrfs "Btrfs") , but also supports snapshots of [LVM](https://wiki.gentoo.org/wiki/LVM "LVM") volumes with thin-provisioning (some filesystems might not be supported depending on the installation ^[\[1\]](#cite_note-1)^).

ext4 used to be supported. Upstream ext4 does not support snapshotting, and most likely never will. snapper/ext4 had required kernel patches that never got merged in the upstream kernel^[\[2\]](#cite_note-2)^.

Snapper was initially developed by SUSE Linux but is now uses in many Linux distributions.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
-   [[2] [Configuration]](#Configuration)
-   [[3] [Usage]](#Usage)
    -   [[3.1] [Rollback]](#Rollback)
-   [[4] [Tips and tricks]](#Tips_and_tricks)
    -   [[4.1] [Portage]](#Portage)
-   [[5] [Troubleshooting]](#Troubleshooting)
    -   [[5.1] [Fatal exceptions]](#Fatal_exceptions)
        -   [[5.1.1] [dbus not running]](#dbus_not_running)
-   [[6] [See also]](#See_also)
-   [[7] [References]](#References)

## [Installation]

### [USE flags]

### [USE flags for] [app-backup/snapper](https://packages.gentoo.org/packages/app-backup/snapper) [[]] [Command-line program for btrfs and lvm snapshot management]

  ----------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------
  [`lvm`](https://packages.gentoo.org/useflags/lvm)           Enable LVM thinprovisioned snapshots support sys-fs/lvm2
  [`pam`](https://packages.gentoo.org/useflags/pam)           Add support for PAM (Pluggable Authentication Modules) - DANGEROUS to arbitrarily flip
  [`systemd`](https://packages.gentoo.org/useflags/systemd)   Enable use of systemd-specific libraries and features like socket activation or session tracking
  [`test`](https://packages.gentoo.org/useflags/test)         Enable dependencies and/or preparations necessary to run tests (usually controlled by FEATURES=test but can be toggled independently)
  [`xattr`](https://packages.gentoo.org/useflags/xattr)       Add support for getting and setting POSIX extended attributes, through sys-apps/attr.
  ----------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-05-06 01:46] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

After USE flags have been set, [emerge] snapper:

`root `[`#`]`emerge --ask `[[[`app-backup/snapper`]](https://packages.gentoo.org/packages/app-backup/snapper)[]]

## [Configuration]

Configuration files for [snapper] are found in the [/etc/snapper/] directory. According to the snapper\'s man page, each filesystem or subvolume that should be snapshotted by snapper requires a configuration file.

A [create-config] sub-command exists to aid in configuration file generation:

`root `[`#`]`snapper create-config <subvolume>`

To create a configuration for the root filesystem, run:

`root `[`#`]`snapper create-config /`

This presumes the root filesystem has been formatted with [btrfs](https://wiki.gentoo.org/wiki/Btrfs "Btrfs") or some other snapper compatible filesystem. The [create-config] command will attempt to guess the underlying filesystem type. If the filesystem type is known (in this case btrfs), then it can be specified using the `--fstype <fstype>` option. See the [snapper] man page for more information.

Create new snapper configuration named **home** for the Btrfs volume at [/home].

`root `[`#`]`snapper --config home create-config /home`

Verify the snapper configuration files have been created.

`root `[`#`]`snapper list-configs`

Allow the regular user to list snapshots. Add user name to the snapper\'s **root** and **home** configurations.

`user `[`$`]`sudo snapper -c root set-config ALLOW_USERS=$ SYNC_ACL=yes`

`user `[`$`]`sudo snapper -c home set-config ALLOW_USERS=$ SYNC_ACL=yes`

Change the group permissions of the [/.snapshots] and [/home/.snapshots] directories to the user name.

`user `[`$`]`sudo chown -R :$ /.snapshots `

`user `[`$`]`sudo chown -R :$ /home/.snapshots`

## [Usage]

`user `[`$`]`snapper --help`

    usage: snapper [--global-options] <command> [--command-options] [command-arguments]

        Global options:
        --quiet, -q         Suppress normal output.
        --verbose, -v           Increase verbosity.
        --utc               Display dates and times in UTC.
        --iso               Display dates and times in ISO format.
        --table-style, -t <style> Table style (integer).
        --config, -c <name>       Set name of config to use.
        --no-dbus           Operate without DBus.
        --root, -r      Operate on target root (works only without DBus).
        --version           Print version and exit.

      List configs:
        snapper list-configs

      Create config:
        snapper create-config <subvolume>

        Options for 'create-config' command:
        --fstype, -f <fstype>     Manually set filesystem type.
        --template, -t <name>     Name of config template to use.

      Delete config:
        snapper delete-config

      Get config:
        snapper get-config

      Set config:
        snapper set-config <configdata>

      List snapshots:
        snapper list

        Options for 'list' command:
        --type, -t <type>     Type of snapshots to list.
        --all-configs, -a       List snapshots from all accessible configs.

      Create snapshot:
        snapper create

        Options for 'create' command:
        --type, -t <type>     Type for snapshot.
        --pre-number <number>     Number of corresponding pre snapshot.
        --print-number, -p      Print number of created snapshot.
        --description, -d <description>   Description for snapshot.
        --cleanup-algorithm, -c <algo>    Cleanup algorithm for snapshot.
        --userdata, -u <userdata> Userdata for snapshot.
        --command <command>   Run command and create pre and post snapshots.

      Modify snapshot:
        snapper modify <number>

        Options for 'modify' command:
        --description, -d <description>   Description for snapshot.
        --cleanup-algorithm, -c <algo>    Cleanup algorithm for snapshot.
        --userdata, -u <userdata> Userdata for snapshot.

      Delete snapshot:
        snapper delete <number>

        Options for 'delete' command:
        --sync, -s          Sync after deletion.

      Mount snapshot:
        snapper mount <number>

      Umount snapshot:
        snapper umount <number>

      Comparing snapshots:
        snapper status <number1>..<number2>

        Options for 'status' command:
        --output, -o <file>       Save status to file.

      Comparing snapshots:
        snapper diff <number1>..<number2> [files]

        Options for 'diff' command:
        --input, -i <file>        Read files to diff from file.
        --diff-cmd <command>      Command used for comparing files.
        --extensions, -x <options>    Extra options passed to the diff command.

      Comparing snapshots extended attributes:
        snapper xadiff <number1>..<number2> [files]

      Undo changes:
        snapper undochange <number1>..<number2> [files]

        Options for 'undochange' command:
        --input, -i <file>        Read files for which to undo changes from file.

      Rollback:
        snapper rollback [number]

        Options for 'rollback' command:
        --print-number, -p      Print number of second created snapshot.
        --description, -d <description>   Description for snapshots.
        --cleanup-algorithm, -c <algo>    Cleanup algorithm for snapshots.
        --userdata, -u <userdata> Userdata for snapshots.

      Cleanup snapshots:
        snapper cleanup <cleanup-algorithm>

### [Rollback]

Snapper has a function called \'rollback\' to switch the current mounted btrfs subvolume to an older subvolume. This feature requires a btrfs file system.

During the initialization, snapper creates a subvolume .snapper automatically, all snapshots are available there.

## [Tips and tricks]

### [Portage]

Installations by portage may be all automatically snapshotted with the number cleanup algorithm using the following configuration:^[\[3\]](#cite_note-3)^ (updated for the recent portage)

[FILE] **`/etc/portage/bashrc`**

    pre_pkg_setup() /$"
      NUMBER=`snapper create -t pre -p -d "$" -c number`
    }

    post_pkg_setup() /$"
      snapper create -t post --pre-number $NUMBER -d "$" -c number
    }

## [Troubleshooting]

### [Fatal exceptions]

#### [dbus not running]

If dbus error messages such as the following are seen:

    terminate called after throwing an instance of 'DBus::FatalException'
      what():  dbus fatal exception
    Aborted

or

    Failure (dbus fatal exception).

dbus is probably not running. To start dbus, on OpenRC, issue:

`root `[`#`]`rc-service dbus start `

`root `[`#`]`rc-update add dbus default `

Furthermore, if dbus refuses to start, check that lvm is running:

`root `[`#`]`rc-service lvm start `

## [See also]

-   [Btrfs](https://wiki.gentoo.org/wiki/Btrfs "Btrfs") --- a copy-on-write (CoW) [filesystem](https://wiki.gentoo.org/wiki/Filesystem "Filesystem") for Linux aimed at implementing advanced features while focusing on fault tolerance, self-healing properties, and easy administration.
-   [Ext4](https://wiki.gentoo.org/wiki/Ext4 "Ext4") --- an open source disk [filesystem](https://wiki.gentoo.org/wiki/Filesystem "Filesystem") and the most recent version of the extended series of filesystems.
-   [LVM](https://wiki.gentoo.org/wiki/LVM "LVM") --- allows administrators to create meta devices that provide an abstraction layer between a file system and the physical storage that is used underneath.

## [References]

1.  [[[↑](#cite_ref-1)] [[http://snapper.io/manpages/snapper.html](http://snapper.io/manpages/snapper.html)]]
2.  [[[↑](#cite_ref-2)] [[https://github.com/openSUSE/snapper/issues/331](https://github.com/openSUSE/snapper/issues/331)]]
3.  [[[↑](#cite_ref-3)] [[https://rich0gentoo.wordpress.com/2013/11/26/btrfs-and-snapper-with-portage-on-gentoo/](https://rich0gentoo.wordpress.com/2013/11/26/btrfs-and-snapper-with-portage-on-gentoo/)]]