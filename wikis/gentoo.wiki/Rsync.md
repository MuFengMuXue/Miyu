Other languages:

-   [English]

**Resources**

[[]][Home](https://rsync.samba.org/)

[[]][Package information](https://packages.gentoo.org/packages/net-misc/rsync)

[[]][Wikipedia](https://en.wikipedia.org/wiki/rsync "wikipedia:rsync")

[rsync] is a powerful file sync program capable of efficient file transfers and directory synchronization.

rsync is included at the [system set](https://wiki.gentoo.org/wiki/System_set_(Portage) "System set (Portage)") on all Gentoo profiles has been used as the primary method for syncing the Gentoo ebuild repository since Gentoo was created.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
-   [[2] [Configuration]](#Configuration)
    -   [[2.1] [Files]](#Files)
    -   [[2.2] [Service]](#Service)
        -   [[2.2.1] [OpenRC]](#OpenRC)
        -   [[2.2.2] [systemd]](#systemd)
    -   [[2.3] [Examples]](#Examples)
        -   [[2.3.1] [Sharing from a list of files]](#Sharing_from_a_list_of_files)
        -   [[2.3.2] [Synchronizing Gentoo\'s repository between local machines]](#Synchronizing_Gentoo.27s_repository_between_local_machines)
-   [[3] [Usage]](#Usage)
    -   [[3.1] [Invocation]](#Invocation)
    -   [[3.2] [Backuping]](#Backuping)
-   [[4] [Troubleshooting]](#Troubleshooting)
    -   [[4.1] [rsync daemon stops working after glibc build]](#rsync_daemon_stops_working_after_glibc_build)
-   [[5] [See also]](#See_also)

## [Installation]

### [USE flags]

### [USE flags for] [net-misc/rsync](https://packages.gentoo.org/packages/net-misc/rsync) [[]] [File transfer program to keep remote files into sync]

  ------------------------------------------------------------------- -----------------------------------------------------------------------------------------
  [`+xxhash`](https://packages.gentoo.org/useflags/+xxhash)           Enable dev-libs/xxhash support for hashing
  [`acl`](https://packages.gentoo.org/useflags/acl)                   Add support for Access Control Lists
  [`examples`](https://packages.gentoo.org/useflags/examples)         Install examples, usually source code
  [`iconv`](https://packages.gentoo.org/useflags/iconv)               Enable support for the iconv character set conversion library
  [`lz4`](https://packages.gentoo.org/useflags/lz4)                   Enable support for lz4 compression (as implemented in app-arch/lz4)
  [`rrsync`](https://packages.gentoo.org/useflags/rrsync)             Install rrsync script to setup restricted rsync users via ssh logins
  [`ssl`](https://packages.gentoo.org/useflags/ssl)                   Add support for SSL/TLS connections (Secure Socket Layer / Transport Layer Security)
  [`stunnel`](https://packages.gentoo.org/useflags/stunnel)           Provide helper scripts for using rsync via \>=net-misc/stunnel-4
  [`system-zlib`](https://packages.gentoo.org/useflags/system-zlib)   Use system zlib instead of bundled one. This is incompatible with older rsync releases!
  [`verify-sig`](https://packages.gentoo.org/useflags/verify-sig)     Verify upstream signatures on distfiles
  [`xattr`](https://packages.gentoo.org/useflags/xattr)               Add support for extended attributes (filesystem-stored metadata)
  [`zstd`](https://packages.gentoo.org/useflags/zstd)                 Enable support for ZSTD compression
  ------------------------------------------------------------------- -----------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-05-21 04:24] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

`root `[`#`]`emerge --ask --oneshot net-misc/rsync`

## [Configuration]

rsync can run both as a client or a server.

### [Files]

-   [/etc/rsyncd.conf] - rsync\'s configuration file for daemon mode (see [[[rsyncd.conf(5)]](https://man.archlinux.org/man/rsyncd.conf.5.en)[[]](https://wiki.gentoo.org/wiki/Special:MyLanguage/man_page "Special:MyLanguage/man page")] for more configuration options).

### [Service]

Daemon help can be seen by running:

`root `[`#`]`rsync --daemon --help`

    rsync  version 3.1.3  protocol version 31
    Copyright (C) 1996-2018 by Andrew Tridgell, Wayne Davison, and others.
    Web site: http://rsync.samba.org/
    Capabilities:
        64-bit files, 64-bit inums, 64-bit timestamps, 64-bit long ints,
        socketpairs, hardlinks, symlinks, IPv6, batchfiles, inplace,
        append, ACLs, xattrs, iconv, symtimes, prealloc

    rsync comes with ABSOLUTELY NO WARRANTY.  This is free software, and you
    are welcome to redistribute it under certain conditions.  See the GNU
    General Public Licence for details.

    Usage: rsync --daemon [OPTION]...
         --address=ADDRESS       bind to the specified address
         --bwlimit=RATE          limit socket I/O bandwidth
         --config=FILE           specify alternate rsyncd.conf file
     -M, --dparam=OVERRIDE       override global daemon config parameter
         --no-detach             do not detach from the parent
         --port=PORT             listen on alternate port number
         --log-file=FILE         override the "log file" setting
         --log-file-format=FMT   override the "log format" setting
         --sockopts=OPTIONS      specify custom TCP options
     -v, --verbose               increase verbosity
     -4, --ipv4                  prefer IPv4
     -6, --ipv6                  prefer IPv6
         --help                  show this help screen

    If you were not trying to invoke rsync as a daemon, avoid using any of the
    daemon-specific rsync options.  See also the rsyncd.conf(5) man page.

#### [OpenRC]

To enable the service to run at system boot:

`root `[`#`]`rc-update add rsyncd default`

To start the rsync daemon now:

`root `[`#`]`rc-service rsyncd start`

#### [systemd]

To enable the service to run at system boot:

`root `[`#`]`systemctl enable rsyncd.service`

To start the rsync daemon now:

`root `[`#`]`systemctl start rsyncd.service`

### [Examples]

#### [Sharing from a list of files]

[FILE] **`/etc/rsyncd.conf`Sharing configuration.**

    ...
    # use chroot  = no # Needed when crossing filesystem boundaries. - #
    ...
    # hosts allow = 192.168.0.0/16 # Allow local network. - #
    # hosts deny  = *              # Deny the rest. - #
    ...
    # uid = root # Needed for files like /etc/ssh/sshd_config. - #
    # gid = root #         >>            /etc/sudoers. - #
    ...
    [sync]
        path         = /
        include from = /backup.list # List of files to copy. - #
        exclude      = *            # Exclude the rest. - #

In the file list, all the intermediary paths are necessary, except when the `***` wildcard is used.

[FILE] **`/backup.list`Example file list.**

    /etc/
    /etc/conf.d/
    /etc/conf.d/hwclock
    /etc/fonts/***

#### [][Synchronizing Gentoo\'s repository between local machines]

If several Gentoo systems are in the same network, it spares bandwidth for everyone to define a local server for the main ebuild repository instead of letting all the machines synchronize in turn with the same external mirror.

The version of [/etc/rsyncd.conf] shipped by Gentoo already provides a valid default configuration. Uncomment the following lines:

[FILE] **`/etc/rsyncd.conf`local rsync server**

    [gentoo-portage]
        path = /var/db/repos/gentoo
        comment = Gentoo ebuild repository
        exclude = /distfiles /packages

Then, start the rsync daemon on the server.

Finally, change the repository configuration on client machines to match the address of the local server. For example, if this address is 192.168.2.24:

[FILE] **`/etc/portage/repos.conf/gentoo`**

    [gentoo]
    #sync-uri = rsync://rsync.gentoo.org/gentoo-portage
    sync-uri = rsync://192.168.2.24/gentoo-portage

The usual commands [emerge \--sync] or [emaint sync -r gentoo] function normally and the process is usually much faster. The change can be reversed at any time.

## [Usage]

### [Invocation]

Client invocation:

`user `[`$`]`rsync --help`

    rsync  version 3.1.3  protocol version 31
    Copyright (C) 1996-2018 by Andrew Tridgell, Wayne Davison, and others.
    Web site: http://rsync.samba.org/
    Capabilities:
        64-bit files, 64-bit inums, 64-bit timestamps, 64-bit long ints,
        socketpairs, hardlinks, symlinks, IPv6, batchfiles, inplace,
        append, ACLs, xattrs, iconv, symtimes, prealloc

    rsync comes with ABSOLUTELY NO WARRANTY.  This is free software, and you
    are welcome to redistribute it under certain conditions.  See the GNU
    General Public Licence for details.

    rsync is a file transfer program capable of efficient remote update
    via a fast differencing algorithm.

    Usage: rsync [OPTION]... SRC [SRC]... DEST
      or   rsync [OPTION]... SRC [SRC]... [USER@]HOST:DEST
      or   rsync [OPTION]... SRC [SRC]... [USER@]HOST::DEST
      or   rsync [OPTION]... SRC [SRC]... rsync://[USER@]HOST[:PORT]/DEST
      or   rsync [OPTION]... [USER@]HOST:SRC [DEST]
      or   rsync [OPTION]... [USER@]HOST::SRC [DEST]
      or   rsync [OPTION]... rsync://[USER@]HOST[:PORT]/SRC [DEST]
    The ':' usages connect via remote shell, while '::' & 'rsync://' usages connect
    to an rsync daemon, and require SRC or DEST to start with a module name.

    Options
     -v, --verbose               increase verbosity
         --info=FLAGS            fine-grained informational verbosity
         --debug=FLAGS           fine-grained debug verbosity
         --msgs2stderr           special output handling for debugging
     -q, --quiet                 suppress non-error messages
         --no-motd               suppress daemon-mode MOTD (see manpage caveat)
     -c, --checksum              skip based on checksum, not mod-time & size
     -a, --archive               archive mode; equals -rlptgoD (no -H,-A,-X)
         --no-OPTION             turn off an implied OPTION (e.g. --no-D)
     -r, --recursive             recurse into directories
     -R, --relative              use relative path names
         --no-implied-dirs       don't send implied dirs with --relative
     -b, --backup                make backups (see --suffix & --backup-dir)
         --backup-dir=DIR        make backups into hierarchy based in DIR
         --suffix=SUFFIX         set backup suffix (default ~ w/o --backup-dir)
     -u, --update                skip files that are newer on the receiver
         --inplace               update destination files in-place (SEE MAN PAGE)
         --append                append data onto shorter files
         --append-verify         like --append, but with old data in file checksum
     -d, --dirs                  transfer directories without recursing
     -l, --links                 copy symlinks as symlinks
     -L, --copy-links            transform symlink into referent file/dir
         --copy-unsafe-links     only "unsafe" symlinks are transformed
         --safe-links            ignore symlinks that point outside the source tree
         --munge-links           munge symlinks to make them safer (but unusable)
     -k, --copy-dirlinks         transform symlink to a dir into referent dir
     -K, --keep-dirlinks         treat symlinked dir on receiver as dir
     -H, --hard-links            preserve hard links
     -p, --perms                 preserve permissions
     -E, --executability         preserve the file's executability
         --chmod=CHMOD           affect file and/or directory permissions
     -A, --acls                  preserve ACLs (implies --perms)
     -X, --xattrs                preserve extended attributes
     -o, --owner                 preserve owner (super-user only)
     -g, --group                 preserve group
         --devices               preserve device files (super-user only)
         --specials              preserve special files
     -D                          same as --devices --specials
     -t, --times                 preserve modification times
     -O, --omit-dir-times        omit directories from --times
     -J, --omit-link-times       omit symlinks from --times
         --super                 receiver attempts super-user activities
         --fake-super            store/recover privileged attrs using xattrs
     -S, --sparse                turn sequences of nulls into sparse blocks
         --preallocate           allocate dest files before writing them
     -n, --dry-run               perform a trial run with no changes made
     -W, --whole-file            copy files whole (without delta-xfer algorithm)
         --checksum-choice=STR   choose the checksum algorithms
     -x, --one-file-system       don't cross filesystem boundaries
     -B, --block-size=SIZE       force a fixed checksum block-size
     -e, --rsh=COMMAND           specify the remote shell to use
         --rsync-path=PROGRAM    specify the rsync to run on the remote machine
         --existing              skip creating new files on receiver
         --ignore-existing       skip updating files that already exist on receiver
         --remove-source-files   sender removes synchronized files (non-dirs)
         --del                   an alias for --delete-during
         --delete                delete extraneous files from destination dirs
         --delete-before         receiver deletes before transfer, not during
         --delete-during         receiver deletes during the transfer
         --delete-delay          find deletions during, delete after
         --delete-after          receiver deletes after transfer, not during
         --delete-excluded       also delete excluded files from destination dirs
         --ignore-missing-args   ignore missing source args without error
         --delete-missing-args   delete missing source args from destination
         --ignore-errors         delete even if there are I/O errors
         --force                 force deletion of directories even if not empty
         --max-delete=NUM        don't delete more than NUM files
         --max-size=SIZE         don't transfer any file larger than SIZE
         --min-size=SIZE         don't transfer any file smaller than SIZE
         --partial               keep partially transferred files
         --partial-dir=DIR       put a partially transferred file into DIR
         --delay-updates         put all updated files into place at transfer's end
     -m, --prune-empty-dirs      prune empty directory chains from the file-list
         --numeric-ids           don't map uid/gid values by user/group name
         --usermap=STRING        custom username mapping
         --groupmap=STRING       custom groupname mapping
         --chown=USER:GROUP      simple username/groupname mapping
         --timeout=SECONDS       set I/O timeout in seconds
         --contimeout=SECONDS    set daemon connection timeout in seconds
     -I, --ignore-times          don't skip files that match in size and mod-time
     -M, --remote-option=OPTION  send OPTION to the remote side only
         --size-only             skip files that match in size
     -@, --modify-window=NUM     set the accuracy for mod-time comparisons
     -T, --temp-dir=DIR          create temporary files in directory DIR
     -y, --fuzzy                 find similar file for basis if no dest file
         --compare-dest=DIR      also compare destination files relative to DIR
         --copy-dest=DIR         ... and include copies of unchanged files
         --link-dest=DIR         hardlink to files in DIR when unchanged
     -z, --compress              compress file data during the transfer
         --compress-level=NUM    explicitly set compression level
         --skip-compress=LIST    skip compressing files with a suffix in LIST
     -C, --cvs-exclude           auto-ignore files the same way CVS does
     -f, --filter=RULE           add a file-filtering RULE
     -F                          same as --filter='dir-merge /.rsync-filter'
                                 repeated: --filter='- .rsync-filter'
         --exclude=PATTERN       exclude files matching PATTERN
         --exclude-from=FILE     read exclude patterns from FILE
         --include=PATTERN       don't exclude files matching PATTERN
         --include-from=FILE     read include patterns from FILE
         --files-from=FILE       read list of source-file names from FILE
     -0, --from0                 all *-from/filter files are delimited by 0s
     -s, --protect-args          no space-splitting; only wildcard special-chars
         --address=ADDRESS       bind address for outgoing socket to daemon
         --port=PORT             specify double-colon alternate port number
         --sockopts=OPTIONS      specify custom TCP options
         --blocking-io           use blocking I/O for the remote shell
         --stats                 give some file-transfer stats
     -8, --8-bit-output          leave high-bit chars unescaped in output
     -h, --human-readable        output numbers in a human-readable format
         --progress              show progress during transfer
     -P                          same as --partial --progress
     -i, --itemize-changes       output a change-summary for all updates
         --out-format=FORMAT     output updates using the specified FORMAT
         --log-file=FILE         log what we're doing to the specified FILE
         --log-file-format=FMT   log updates using the specified FMT
         --password-file=FILE    read daemon-access password from FILE
         --list-only             list the files instead of copying them
         --bwlimit=RATE          limit socket I/O bandwidth
         --outbuf=N|L|B          set output buffering to None, Line, or Block
         --write-batch=FILE      write a batched update to FILE
         --only-write-batch=FILE like --write-batch but w/o updating destination
         --read-batch=FILE       read a batched update from FILE
         --protocol=NUM          force an older protocol version to be used
         --iconv=CONVERT_SPEC    request charset conversion of filenames
         --checksum-seed=NUM     set block/file checksum seed (advanced)
     -4, --ipv4                  prefer IPv4
     -6, --ipv6                  prefer IPv6
         --version               print version number
    (-h) --help                  show this help (-h is --help only if used alone)

    Use "rsync --daemon --help" to see the daemon-mode command-line options.
    Please see the rsync(1) and rsyncd.conf(5) man pages for full documentation.
    See http://rsync.samba.org/ for updates, bug reports, and answers

### [Backuping]

Rsync is a good tool for the full system backup (but please use [git](https://wiki.gentoo.org/wiki/Git "Git") for specific configs and data), because if only a few files were changes - only them will occupy space inside the next backup folder - thanks to hardlinking.

In order to make a backup:

[FILE] **`/root/full-backup/full-backup.sh`**

    BEFORE=$(df -h)

    STARTED=$(date)

    DATE=`date "+%Y-%m-%d"`

    DEST="/mnt/backup/$DATE"

    rsync --archive --acls --xattrs --delete --progress --verbose --exclude-from=exclude.txt --link-dest=/mnt/backup/last --mkpath / $DEST

    ln --symbolic --force --no-dereference $DATE /mnt/backup/last

    echo "Started at:   " $STARTED
    echo "Current time: " $(date)

    echo "Before:

    $BEFORE

    Now:
    "

    df -h

In the same folder you can have exclude list:

[FILE] **`/root/full-backup/exclude.txt`**

    /dev/*
    /proc/*
    /sys/*
    /run/*
    /var/db/repos/gentoo
    /var/db/repos/guru
    /tmp/*
    /var/tmp
    /lost+found
    /mnt/*
    /home/vitaly/.npm
    /home/vitaly/.cache
    /home/vitaly/go/pkg/mod/cache

So your backups will looks like this:

`user `[`$`]`ls -lh`

    total 40K
    drwxr-xr-x 20 root root 4.0K Oct 14 23:52 2022-09-28
    drwxr-xr-x 20 root root 4.0K Oct 14 23:58 2022-10-14
    drwxr-xr-x 20 root root 4.0K Oct 15 00:34 2022-10-15
    drwxr-xr-x 20 root root 4.0K Oct 15 00:34 2022-11-06
    drwxr-xr-x 20 root root 4.0K Oct 15 00:34 2022-11-19
    drwxr-xr-x 20 root root 4.0K Oct 15 00:34 2022-12-03
    drwxr-xr-x 20 root root 4.0K Oct 15 00:34 2022-12-10
    drwxr-xr-x 20 root root 4.0K Oct 15 00:34 2022-12-17
    drwxr-xr-x 20 root root 4.0K Oct 15 00:34 2022-12-24
    drwxr-xr-x 20 root root 4.0K Oct 15 00:34 2023-01-03
    lrwxrwxrwx  1 root root   10 Jan  3 15:27 last -> 2023-01-03

To restore from such a backup:

`root `[`#`]`rsync --archive --acls --xattrs --progress --verbose /mnt/last/ /`

On the new SSD you probably will need to install the [bootloader](https://wiki.gentoo.org/wiki/Grub "Grub"), or alter UUID values in **/etc/fstab**.

## [Troubleshooting]

### [rsync daemon stops working after glibc build]

Occasionally the rsync daemon will stop working after glibc has been rebuilt. The error on the client side (when trying to sync from the server) will be something like the following:

    @ERROR: invalid uid nobody
    rsync error: error starting client-server protocol (code 5) at main.c(1657) [Receiver=3.1.3]

Unfortunately simply restarting the rsync daemon will not fix the issue.

The solution, found in [[[bug #414843]](https://bugs.gentoo.org/show_bug.cgi?id=414843)[]], is to rebuild the [[[net-misc/rsync]](https://packages.gentoo.org/packages/net-misc/rsync)[]] package so that it can re-link against the proper version of glibc\'s [libc.so.6] file.

`root `[`#`]`emerge --ask --oneshot net-misc/rsync`

After the rebuild then restart the daemon.

## [See also]

-   [Portage](https://wiki.gentoo.org/wiki/Portage "Portage") --- the official [package manager](https://en.wikipedia.org/wiki/Package_manager "wikipedia:Package manager") and [distribution system](https://www.gentoo.org/get-started/about/) for Gentoo.
-   [Ssh](https://wiki.gentoo.org/wiki/Ssh "Ssh") --- the ubiquitous tool for logging into and working on remote machines securely.
-   [csync2](https://wiki.gentoo.org/wiki/Csync2 "Csync2") --- a tool for asynchronous file synchronization in clusters.