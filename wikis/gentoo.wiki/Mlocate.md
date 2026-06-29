**Resources**

[[]][Home](https://pagure.io/mlocate)

[[]][Wikipedia](https://en.wikipedia.org/wiki/Locate_(Unix) "wikipedia:Locate (Unix)")

mlocate is a **m**erging **locate** and database package. \"Merging\" means [updatedb] reuses the existing database to avoid re-reading most of the file system. This makes the database update faster and does not tax the system caches.^[\[1\]](#cite_note-1)^ [mlocate] can index several file systems including network file systems for network shares. This package is essential when attempting to quickly find documents in a terminal.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
-   [[2] [Configuration]](#Configuration)
    -   [[2.1] [Files]](#Files)
    -   [[2.2] [Services]](#Services)
        -   [[2.2.1] [OpenRC]](#OpenRC)
        -   [[2.2.2] [systemd]](#systemd)
-   [[3] [Usage]](#Usage)
    -   [[3.1] [Initial database indexing]](#Initial_database_indexing)
    -   [[3.2] [Invocation]](#Invocation)
-   [[4] [Troubleshooting]](#Troubleshooting)
    -   [[4.1] [Cannot find a file]](#Cannot_find_a_file)
-   [[5] [External resources]](#External_resources)
-   [[6] [References]](#References)

## [Installation]

### [USE flags]

### [USE flags for] [sys-apps/mlocate](https://packages.gentoo.org/packages/sys-apps/mlocate) [[]] [Merging locate is an utility to index and quickly search for files]

  ----------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------
  [`nls`](https://packages.gentoo.org/useflags/nls)           Add Native Language Support (using gettext - GNU locale utilities)
  [`selinux`](https://packages.gentoo.org/useflags/selinux)   !!internal use only!! Security Enhanced Linux support, this must be set by the selinux profile or breakage will occur
  ----------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2025-09-02 17:00] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

Emerge [[[sys-apps/mlocate]](https://packages.gentoo.org/packages/sys-apps/mlocate)[]] via:

`root `[`#`]`emerge --ask sys-apps/mlocate`

Once installed mlocate can be invoked with the [locate] command.

## [Configuration]

### [Files]

To have network file systems *included* when mlocate\'s index is populated edit the pruning of the file system variable (`PRUNEFS`) in the [/etc/updatedb.conf] file. Remove the `nfs`, `NFS`, and `nfs4`, `nfsd` entries:

[FILE] **`/etc/updatedb.conf`Include network file systems example**

    # This file sets variables that are used by updatedb.
    # For more info, see the updatedb.conf(5) manpage.

    # Filesystems that are pruned from updatedb database
    PRUNEFS="afs anon_inodefs auto autofs bdev binfmt binfmt_misc cgroup cifs coda configfs cramfs cpuset debugfs devfs devpts devtmpfs ecryptfs eventpollfs exofs futexfs ftpfs fuse fusectl gfs gfs2 hostfs hugetlbfs inotifyfs iso9660 jffs2 lustre misc mqueue ncpfs nnpfs ocfs ocfs2 pipefs proc ramfs rpc_pipefs securityfs selinuxfs sfs shfs smbfs sockfs spufs sshfs subfs supermount sysfs tmpfs ubifs udf usbfs vboxsf vperfctrfs"

    # Paths which are pruned from updatedb database
    PRUNEPATHS="/tmp /var/tmp /var/cache /var/lock /var/run /var/spool"

    # Folder names that are pruned from updatedb database
    PRUNENAMES=".git .hg .svn CVS"

    # Skip bind mounts.
    PRUNE_BIND_MOUNTS="yes"

### [Services]

#### [OpenRC]

On OpenRC, systems, if a [cron](https://wiki.gentoo.org/wiki/Cron "Cron") daemon is installed and added to a runlevel, [updatedb] will run routinely via a cron job. See the [/etc/cron.daily/mlocate] and [/etc/mlocate-cron.conf] files for more details.

#### [systemd]

To enable [updatedb] to run routinely (each day), activate its timer file:

`root `[`#`]`systemctl enable --now updatedb.timer`

## [Usage]

### [Initial database indexing]

Upon installation, the [updatedb] command will automatically be added as a scheduled cron job. To index the files immediately run:

`root `[`#`]`updatedb`

Searching can be performed as soon as this step is complete.

### [Invocation]

See more options from the command-line by asking for help:

`user `[`$`]`locate --help`

    Usage: locate [OPTION]... [PATTERN]...
    Search for entries in a mlocate database.

      -A, --all              only print entries that match all patterns
      -b, --basename         match only the base name of path names
      -c, --count            only print number of found entries
      -d, --database DBPATH  use DBPATH instead of default database (which is
                             /var/lib/mlocate/mlocate.db)
      -e, --existing         only print entries for currently existing files
      -L, --follow           follow trailing symbolic links when checking file
                             existence (default)
      -h, --help             print this help
      -i, --ignore-case      ignore case distinctions when matching patterns
      -l, --limit, -n LIMIT  limit output (or counting) to LIMIT entries
      -m, --mmap             ignored, for backward compatibility
      -P, --nofollow, -H     don't follow trailing symbolic links when checking file
                             existence
      -0, --null             separate entries with NUL on output
      -S, --statistics       don't search for entries, print statistics about each
                             used database
      -q, --quiet            report no error messages about reading databases
      -r, --regexp REGEXP    search for basic regexp REGEXP instead of patterns
          --regex            patterns are extended regexps
      -s, --stdio            ignored, for backward compatibility
      -V, --version          print version information
      -w, --wholename        match whole path name (default)

    Report bugs to mitr@redhat.com.

To find all Firefox executables:

`user `[`$`]`locate firefox | grep bin`

## [Troubleshooting]

### [Cannot find a file]

When having trouble finding a newly installed file, be sure the database has been manually rebuilt before the search. The default cron job will index on a daily basis, however the chances of it running directly after new files have been added to the system is slim.

More information concerning the default cron job can be found in the [/etc/cron.daily/mlocate] file.

## [External resources]

-   [mlocate](https://wiki.archlinux.org/index.php/Mlocate) (Arch Wiki)

## [References]

1.  [[[↑](#cite_ref-1)] [[https://pagure.io/mlocate](https://pagure.io/mlocate)]]