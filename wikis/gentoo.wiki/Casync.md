[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=Casync&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

**Resources**

[[]][GitHub](https://github.com/systemd/casync)

[[]][Package information](https://packages.gentoo.org/packages/net-misc/casync)

[[]][Wikipedia](https://en.wikipedia.org/wiki/ "wikipedia:")

[casync] is a **c**ontent-**a**ddressable data **sync**hronization tool. It can be thought up as a hybrid between git and rsync; able to store changes between files and quickly send/receive them. It is capable of operating on the block layer using raw devices and the filesystem level.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
-   [[2] [Usage]](#Usage)
    -   [[2.1] [Invocation]](#Invocation)
-   [[3] [Removal]](#Removal)
    -   [[3.1] [Unmerge]](#Unmerge)
-   [[4] [See also]](#See_also)

## [Installation]

### [USE flags]

### [USE flags for] [net-misc/casync](https://packages.gentoo.org/packages/net-misc/casync) [[]] [Content-Addressable Data Synchronization Tool]

  ----------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------
  [`+fuse`](https://packages.gentoo.org/useflags/+fuse)       Enable fuse support
  [`+udev`](https://packages.gentoo.org/useflags/+udev)       Enable virtual/udev integration (device discovery, power and storage device support, etc)
  [`man`](https://packages.gentoo.org/useflags/man)           Build and install man pages
  [`selinux`](https://packages.gentoo.org/useflags/selinux)   !!internal use only!! Security Enhanced Linux support, this must be set by the selinux profile or breakage will occur
  [`test`](https://packages.gentoo.org/useflags/test)         Enable dependencies and/or preparations necessary to run tests (usually controlled by FEATURES=test but can be toggled independently)
  ----------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2025-12-04 08:59] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

`root `[`#`]`emerge --ask net-misc/casync`

## [Usage]

### [Invocation]

`user `[`$`]`casync --help`

    casync [OPTIONS...] make [ARCHIVE|ARCHIVE_INDEX|BLOB_INDEX] [PATH]
    casync [OPTIONS...] extract [ARCHIVE|ARCHIVE_INDEX|BLOB_INDEX] [PATH]
    casync [OPTIONS...] list [ARCHIVE|ARCHIVE_INDEX|DIRECTORY]
    casync [OPTIONS...] mtree [ARCHIVE|ARCHIVE_INDEX|DIRECTORY]
    casync [OPTIONS...] stat [ARCHIVE|ARCHIVE_INDEX|DIRECTORY] [PATH]
    casync [OPTIONS...] digest [ARCHIVE|BLOB|ARCHIVE_INDEX|BLOB_INDEX|DIRECTORY]
    casync [OPTIONS...] mount [ARCHIVE|ARCHIVE_INDEX] PATH
    casync [OPTIONS...] mkdev [BLOB|BLOB_INDEX] [NODE]

    Content-Addressable Data Synchronization Tool

      -h --help                  Show this help
         --version               Show brief version information
      -v --verbose               Show terse status information during runtime
      -n --dry-run               When garbage collecting, only print what would
                                 be done
         --store=PATH            The primary chunk store to use
         --extra-store=PATH      Additional chunk store to look for chunks in
         --chunk-size=[MIN:]AVG[:MAX]
                                 The minimal/average/maximum number of bytes in a
                                 chunk
         --digest=DIGEST         Pick digest algorithm (sha512-256 or sha256)
         --compression=COMPRESSION
                                 Pick compression algorithm (zstd, xz or gzip)
         --seed=PATH             Additional file or directory to use as seed
         --cache=PATH            Directory to use as encoder cache
      -c --cache-auto            Pick encoder cache directory automatically
         --rate-limit-bps=LIMIT  Maximum bandwidth in bytes/s for remote
                                 communication
         --exclude-nodump=no     Don't exclude files with chattr(1)'s +d 'nodump'
                                 flag when creating archive
         --exclude-submounts=yes Exclude submounts when creating archive
         --exclude-file=no       Don't respect .caexclude files in file tree
         --reflink=no            Don't create reflinks from seeds when extracting
         --hardlink=yes          Create hardlinks from seeds when extracting
         --punch-holes=no        Don't create sparse files when extracting
         --delete=no             Don't delete existing files not listed in archive
                                 after extraction
         --undo-immutable=yes    When removing existing files, undo chattr(1)'s +i
                                 'immutable' flag when extracting
         --seed-output=no        Don't implicitly add pre-existing output as seed
                                 when extracting
         --recursive=no          List non-recursively
         --mkdir=no              Don't automatically create mount directory if it
                                 is missing
         --uid-shift=yes|SHIFT   Shift UIDs/GIDs
         --uid-range=RANGE       Restrict UIDs/GIDs to range

    Input/output selector:
         --what=archive          Operate on archive file
         --what=archive-index    Operate on archive index file
         --what=blob             Operate on blob file
         --what=blob-index       Operate on blob index file
         --what=directory        Operate on directory

         --what=help             Print allowed values

    Archive feature sets:
         --with=best             Store most accurate information
         --with=unix             Store UNIX baseline information
         --with=fat              Store FAT information
         --with=chattr           Store chattr(1) file attributes
         --with=fat-attrs        Store FAT file attributes
         --with=privileged       Store file data that requires privileges to
                                 restore
         --with=fuse             Store file data that can exposed again via
                                 'casync mount'
         (and similar: --without=fat-attrs, --without=privileged, ...)
         --without=all           Disable all optional attributes

    Individual archive features:
         --with=16bit-uids       Store reduced 16bit UID/GID information
         --with=32bit-uids       Store full 32bit UID/GID information
         --with=user-names       Store user and group names
         --with=sec-time         Store timestamps with 1s granularity
         --with=usec-time        Store timestamps with 1µs granularity
         --with=nsec-time        Store timestamps with 1ns granularity
         --with=2sec-time        Store timestamps with 2s granularity
         --with=read-only        Store per-file read only flag
         --with=permissions      Store full per-file UNIX permissions
         --with=symlinks         Store symbolic links
         --with=device-nodes     Store block and character device nodes
         --with=fifos            Store named pipe nodes
         --with=sockets          Store AF_UNIX file system socket nodes
         --with=flag-hidden      Store FAT "hidden" file flag
         --with=flag-system      Store FAT "system" file flag
         --with=flag-archive     Store FAT "archive" file flag
         --with=flag-append      Store "append-only" file flag
         --with=flag-noatime     Store "disable access time" file flag
         --with=flag-compr       Store "enable compression" file flag
         --with=flag-nocow       Store "disable copy-on-write" file flag
         --with=flag-nodump      Store "disable dumping" file flag
         --with=flag-dirsync     Store "synchronous" directory flag
         --with=flag-immutable   Store "immutable" file flag
         --with=flag-sync        Store "synchronous" file flag
         --with=flag-nocomp      Store "disable compression" file flag
         --with=flag-projinherit Store "project quota inheritance" flag
         --with=subvolume        Store btrfs subvolume information
         --with=subvolume-ro     Store btrfs subvolume read-only property
         --with=xattrs           Store extended file attributes
         --with=acl              Store file access control lists
         --with=selinux          Store SELinux file labels
         --with=fcaps            Store file capabilities
         --with=quota-projid     Store ext4/XFS quota project ID
         (and similar: --without=16bit-uids, --without=32bit-uids, ...)

## [Removal]

### [Unmerge]

`root `[`#`]`emerge --ask --depclean --verbose net-misc/casync`

## [See also]

-   [Systemd](https://wiki.gentoo.org/wiki/Systemd "Systemd") --- a modern SysV-style init and [[rc](https://wiki.gentoo.org/wiki/Rc "Rc")] replacement for Linux systems.
-   [Rsync](https://wiki.gentoo.org/wiki/Rsync "Rsync") --- a powerful file sync program capable of efficient file transfers and directory synchronization.
-   [Git](https://wiki.gentoo.org/wiki/Git "Git") --- widely used, open source, distributed [version control system](https://wiki.gentoo.org/wiki/Version_control_systems "Version control systems")
-   [Tar](https://wiki.gentoo.org/wiki/Tar "Tar") --- an [archiver](https://wiki.gentoo.org/wiki/Data_compression "Data compression") tool that provides the ability to create tar archives, as well as various other kinds of manipulation.