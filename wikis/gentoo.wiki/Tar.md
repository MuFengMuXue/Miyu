**Resources**

[[]][Wikipedia](https://en.wikipedia.org/wiki/Tar_(computing) "wikipedia:Tar (computing)")

[[]][GNU tar/\'gtar\' documentation](https://www.gnu.org/software/tar/manual/)

[[]][libarchive tar/\'bsdtar\' documentation](https://libarchive.org/)

[tar] is an [archiver](https://wiki.gentoo.org/wiki/Data_compression "Data compression") tool that provides the ability to create tar archives, as well as various other kinds of manipulation. The [tar] utility is often used for file storage, backup, and transportation.

By default, Gentoo provides [GNU tar](https://www.gnu.org/software/tar/), [[[app-arch/tar]](https://packages.gentoo.org/packages/app-arch/tar)[]] (\'gtar\'), which is installed via the \@system set. However, Gentoo also provides [[[bsdtar(1)]](https://man.archlinux.org/man/bsdtar.1.en)[[]](https://wiki.gentoo.org/wiki/Special:MyLanguage/man_page "Special:MyLanguage/man page")], via the [[[app-arch/libarchive]](https://packages.gentoo.org/packages/app-arch/libarchive)[]] package; once that package is installed, [bsdtar] can be used as the default [tar] provider by setting the `libarchive` USE flag on [[[app-alternatives/tar]](https://packages.gentoo.org/packages/app-alternatives/tar)[]].

For a list of formats supported by GNU tar, refer to the [[[tar(5)]](https://man.archlinux.org/man/tar.5.en)[[]](https://wiki.gentoo.org/wiki/Special:MyLanguage/man_page "Special:MyLanguage/man page")] man page; for a list of formats supported by bsdtar, refer to the [[[libarchive-formats(5)]](https://man.archlinux.org/man/libarchive-formats.5.en)[[]](https://wiki.gentoo.org/wiki/Special:MyLanguage/man_page "Special:MyLanguage/man page")] man page. Both implementations support various compression formats; refer to the [[[gtar(1)]](https://man.archlinux.org/man/gtar.1.en)[[]](https://wiki.gentoo.org/wiki/Special:MyLanguage/man_page "Special:MyLanguage/man page")] and [[[bsdtar(1)]](https://man.archlinux.org/man/bsdtar.1.en)[[]](https://wiki.gentoo.org/wiki/Special:MyLanguage/man_page "Special:MyLanguage/man page")] man pages for details.

The information provided in the rest of this page assumes the use of GNU tar.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
-   [[2] [Configuration]](#Configuration)
    -   [[2.1] [Environment variables]](#Environment_variables)
-   [[3] [Usage]](#Usage)
    -   [[3.1] [Invocation]](#Invocation)
        -   [[3.1.1] [help]](#help)
        -   [[3.1.2] [Three most frequently used options]](#Three_most_frequently_used_options)
            -   [[3.1.2.1] [Creation]](#Creation)
            -   [[3.1.2.2] [Listing]](#Listing)
            -   [[3.1.2.3] [Extraction]](#Extraction)
            -   [[3.1.2.4] [Additional options]](#Additional_options)
        -   [[3.1.3] [Compression]](#Compression)
-   [[4] [Additional information]](#Additional_information)
-   [[5] [Removal]](#Removal)
-   [[6] [See also]](#See_also)
-   [[7] [External resources]](#External_resources)

## [Installation]

### [USE flags]

### [USE flags for] [app-arch/tar](https://packages.gentoo.org/packages/app-arch/tar) [[]] [Use this to make tarballs :)]

  ----------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------
  [`acl`](https://packages.gentoo.org/useflags/acl)                 Add support for Access Control Lists
  [`minimal`](https://packages.gentoo.org/useflags/minimal)         just install \`tar\`
  [`nls`](https://packages.gentoo.org/useflags/nls)                 Add Native Language Support (using gettext - GNU locale utilities)
  [`selinux`](https://packages.gentoo.org/useflags/selinux)         !!internal use only!! Security Enhanced Linux support, this must be set by the selinux profile or breakage will occur
  [`verify-sig`](https://packages.gentoo.org/useflags/verify-sig)   Verify upstream signatures on distfiles
  [`xattr`](https://packages.gentoo.org/useflags/xattr)             Add support for extended attributes (filesystem-stored metadata)
  ----------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-05-13 17:52] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

After adjusting USE flags:

`root `[`#`]`emerge --ask app-arch/tar`

## [Configuration]

It\'s possible to configure tar to use parallel versions of tools for compression, like [[[app-arch/pigz]](https://packages.gentoo.org/packages/app-arch/pigz)[]].

[FILE] **`/etc/portage/env/app-arch/tar`**

    # Use app-arch/lbzip2 for bzip2 and app-arch/pigz for gzip
    EXTRA_ECONF="--with-bzip2=lbzip2 --with-gzip=pigz"

And install the relevant tools:

`root `[`#`]`emerge --ask app-arch/lbzip2 app-arch/pigz`

Then re-emerge tar:

`root `[`#`]`emerge --oneshot app-arch/tar`

### [Environment variables]

`user `[`$`]`tar --help`

displays by default the short tar option summary, which is divided into sections. The exact visual representation of the help output is configurable via the `ARGP_HELP_FMT` environment variable. For more information please refer to [GNU\'s tar manual](https://www.gnu.org/software/tar/manual/html_section/Configuring-Help-Summary.html#Configuring-Help-Summary)

## [Usage]

### [Invocation]

#### [help]

`user `[`$`]`tar --help`

    Usage: tar [OPTION...] [FILE]...
    GNU 'tar' saves many files together into a single tape or disk archive, and can
    restore individual files from the archive.

    Examples:
      tar -cf archive.tar foo bar  # Create archive.tar from files foo and bar.
      tar -tvf archive.tar         # List all files in archive.tar verbosely.
      tar -xf archive.tar          # Extract all files from archive.tar.

     Main operation mode:
      -A, --catenate, --concatenate   append tar files to an archive
      -c, --create               create a new archive
          --delete               delete from the archive (not on mag tapes!)
      -d, --diff, --compare      find differences between archive and file system
      -r, --append               append files to the end of an archive
          --test-label           test the archive volume label and exit
      -t, --list                 list the contents of an archive
      -u, --update               only append files newer than copy in archive
      -x, --extract, --get       extract files from an archive

     Operation modifiers:

          --check-device         check device numbers when creating incremental
                                 archives (default)
      -g, --listed-incremental=FILE   handle new GNU-format incremental backup
      -G, --incremental          handle old GNU-format incremental backup
          --hole-detection=TYPE  technique to detect holes
          --ignore-failed-read   do not exit with nonzero on unreadable files
          --level=NUMBER         dump level for created listed-incremental archive
          --no-check-device      do not check device numbers when creating
                                 incremental archives
          --no-seek              archive is not seekable
      -n, --seek                 archive is seekable
          --occurrence[=NUMBER]  process only the NUMBERth occurrence of each file
                                 in the archive; this option is valid only in
                                 conjunction with one of the subcommands --delete,
                                 --diff, --extract or --list and when a list of
                                 files is given either on the command line or via
                                 the -T option; NUMBER defaults to 1
          --sparse-version=MAJOR[.MINOR]
                                 set version of the sparse format to use (implies
                                 --sparse)
      -S, --sparse               handle sparse files efficiently

     Local file name selection:
          --add-file=FILE        add given FILE to the archive (useful if its name
                                 starts with a dash)
      -C, --directory=DIR        change to directory DIR
          --exclude=PATTERN      exclude files, given as a PATTERN
          --exclude-backups      exclude backup and lock files
          --exclude-caches       exclude contents of directories containing
                                 CACHEDIR.TAG, except for the tag file itself
          --exclude-caches-all   exclude directories containing CACHEDIR.TAG
          --exclude-caches-under exclude everything under directories containing
                                 CACHEDIR.TAG
          --exclude-ignore=FILE  read exclude patterns for each directory from
                                 FILE, if it exists
          --exclude-ignore-recursive=FILE
                                 read exclude patterns for each directory and its
                                 subdirectories from FILE, if it exists
          --exclude-tag=FILE     exclude contents of directories containing FILE,
                                 except for FILE itself
          --exclude-tag-all=FILE exclude directories containing FILE
          --exclude-tag-under=FILE   exclude everything under directories
                                 containing FILE
          --exclude-vcs          exclude version control system directories
          --exclude-vcs-ignores  read exclude patterns from the VCS ignore files
          --no-null              disable the effect of the previous --null option
          --no-recursion         avoid descending automatically in directories
          --no-unquote           do not unquote input file or member names
          --no-verbatim-files-from   -T treats file names starting with dash as
                                 options (default)
          --null                 -T reads null-terminated names; implies
                                 --verbatim-files-from
          --recursion            recurse into directories (default)
      -T, --files-from=FILE      get names to extract or create from FILE
          --unquote              unquote input file or member names (default)
          --verbatim-files-from  -T reads file names verbatim (no escape or option
                                 handling)
      -X, --exclude-from=FILE    exclude patterns listed in FILE

     File name matching options (affect both exclude and include patterns):

          --anchored             patterns match file name start
          --ignore-case          ignore case
          --no-anchored          patterns match after any '/' (default for
                                 exclusion)
          --no-ignore-case       case sensitive matching (default)
          --no-wildcards         verbatim string matching
          --no-wildcards-match-slash   wildcards do not match '/'
          --wildcards            use wildcards (default for exclusion)
          --wildcards-match-slash   wildcards match '/' (default for exclusion)

     Overwrite control:

          --keep-directory-symlink   preserve existing symlinks to directories when
                                 extracting
          --keep-newer-files     don't replace existing files that are newer than
                                 their archive copies
      -k, --keep-old-files       don't replace existing files when extracting,
                                 treat them as errors
          --no-overwrite-dir     preserve metadata of existing directories
          --one-top-level[=DIR]  create a subdirectory to avoid having loose files
                                 extracted
          --overwrite            overwrite existing files when extracting
          --overwrite-dir        overwrite metadata of existing directories when
                                 extracting (default)
          --recursive-unlink     empty hierarchies prior to extracting directory
          --remove-files         remove files after adding them to the archive
          --skip-old-files       don't replace existing files when extracting,
                                 silently skip over them
      -U, --unlink-first         remove each file prior to extracting over it
      -W, --verify               attempt to verify the archive after writing it

     Select output stream:

          --ignore-command-error ignore exit codes of children
          --no-ignore-command-error   treat non-zero exit codes of children as
                                 error
      -O, --to-stdout            extract files to standard output
          --to-command=COMMAND   pipe extracted files to another program

     Handling of file attributes:

          --atime-preserve[=METHOD]   preserve access times on dumped files, either
                                 by restoring the times after reading
                                 (METHOD='replace'; default) or by not setting the
                                 times in the first place (METHOD='system')
          --clamp-mtime          only set time when the file is more recent than
                                 what was given with --mtime
          --delay-directory-restore   delay setting modification times and
                                 permissions of extracted directories until the end
                                 of extraction
          --group=NAME           force NAME as group for added files
          --group-map=FILE       use FILE to map file owner GIDs and names
          --mode=CHANGES         force (symbolic) mode CHANGES for added files
          --mtime=DATE-OR-FILE   set mtime for added files from DATE-OR-FILE
      -m, --touch                don't extract file modified time
          --no-delay-directory-restore
                                 cancel the effect of --delay-directory-restore
                                 option
          --no-same-owner        extract files as yourself (default for ordinary
                                 users)
          --no-same-permissions  apply the user's umask when extracting permissions
                                 from the archive (default for ordinary users)
          --numeric-owner        always use numbers for user/group names
          --owner=NAME           force NAME as owner for added files
          --owner-map=FILE       use FILE to map file owner UIDs and names
      -p, --preserve-permissions, --same-permissions
                                 extract information about file permissions
                                 (default for superuser)
          --same-owner           try extracting files with the same ownership as
                                 exists in the archive (default for superuser)
          --sort=ORDER           directory sorting order: none (default), name or
                                 inode
      -s, --preserve-order, --same-order
                                 member arguments are listed in the same order as
                                 the files in the archive

     Handling of extended file attributes:

          --acls                 Enable the POSIX ACLs support
          --no-acls              Disable the POSIX ACLs support
          --no-selinux           Disable the SELinux context support
          --no-xattrs            Disable extended attributes support
          --selinux              Enable the SELinux context support
          --xattrs               Enable extended attributes support
          --xattrs-exclude=MASK  specify the exclude pattern for xattr keys
          --xattrs-include=MASK  specify the include pattern for xattr keys

     Device selection and switching:

          --force-local          archive file is local even if it has a colon
      -f, --file=ARCHIVE         use archive file or device ARCHIVE
      -F, --info-script=NAME, --new-volume-script=NAME
                                 run script at end of each tape (implies -M)
      -L, --tape-length=NUMBER   change tape after writing NUMBER x 1024 bytes
      -M, --multi-volume         create/list/extract multi-volume archive
          --rmt-command=COMMAND  use given rmt COMMAND instead of rmt
          --rsh-command=COMMAND  use remote COMMAND instead of rsh
          --volno-file=FILE      use/update the volume number in FILE

     Device blocking:

      -b, --blocking-factor=BLOCKS   BLOCKS x 512 bytes per record
      -B, --read-full-records    reblock as we read (for 4.2BSD pipes)
      -i, --ignore-zeros         ignore zeroed blocks in archive (means EOF)
          --record-size=NUMBER   NUMBER of bytes per record, multiple of 512

     Archive format selection:

      -H, --format=FORMAT        create archive of the given format

     FORMAT is one of the following:
        gnu                      GNU tar 1.13.x format
        oldgnu                   GNU format as per tar <= 1.12
        pax                      POSIX 1003.1-2001 (pax) format
        posix                    same as pax
        ustar                    POSIX 1003.1-1988 (ustar) format
        v7                       old V7 tar format

          --old-archive, --portability
                                 same as --format=v7
          --pax-option=keyword[[:]=value][,keyword[[:]=value]]...
                                 control pax keywords
          --posix                same as --format=posix
      -V, --label=TEXT           create archive with volume name TEXT; at
                                 list/extract time, use TEXT as a globbing pattern
                                 for volume name

     Compression options:

      -a, --auto-compress        use archive suffix to determine the compression
                                 program
      -I, --use-compress-program=PROG
                                 filter through PROG (must accept -d)
      -j, --bzip2                filter the archive through bzip2
      -J, --xz                   filter the archive through xz
          --lzip                 filter the archive through lzip
          --lzma                 filter the archive through lzma
          --lzop                 filter the archive through lzop
          --no-auto-compress     do not use archive suffix to determine the
                                 compression program
          --zstd                 filter the archive through zstd
      -z, --gzip, --gunzip, --ungzip   filter the archive through gzip
      -Z, --compress, --uncompress   filter the archive through compress

     Local file selection:

          --backup[=CONTROL]     backup before removal, choose version CONTROL
          --hard-dereference     follow hard links; archive and dump the files they
                                 refer to
      -h, --dereference          follow symlinks; archive and dump the files they
                                 point to
      -K, --starting-file=MEMBER-NAME
                                 begin at member MEMBER-NAME when reading the
                                 archive
          --newer-mtime=DATE     compare date and time when data changed only
      -N, --newer=DATE-OR-FILE, --after-date=DATE-OR-FILE
                                 only store files newer than DATE-OR-FILE
          --one-file-system      stay in local file system when creating archive
      -P, --absolute-names       don't strip leading '/'s from file names
          --suffix=STRING        backup before removal, override usual suffix ('~'
                                 unless overridden by environment variable
                                 SIMPLE_BACKUP_SUFFIX)

     File name transformations:

          --strip-components=NUMBER   strip NUMBER leading components from file
                                 names on extraction
          --transform=EXPRESSION, --xform=EXPRESSION
                                 use sed replace EXPRESSION to transform file
                                 names

     Informative output:

          --checkpoint[=NUMBER]  display progress messages every NUMBERth record
                                 (default 10)
          --checkpoint-action=ACTION   execute ACTION on each checkpoint
          --full-time            print file time to its full resolution
          --index-file=FILE      send verbose output to FILE
      -l, --check-links          print a message if not all links are dumped
          --no-quote-chars=STRING   disable quoting for characters from STRING
          --quote-chars=STRING   additionally quote characters from STRING
          --quoting-style=STYLE  set name quoting style; see below for valid STYLE
                                 values
      -R, --block-number         show block number within archive with each message

          --show-defaults        show tar defaults
          --show-omitted-dirs    when listing or extracting, list each directory
                                 that does not match search criteria
          --show-snapshot-field-ranges
                                 show valid ranges for snapshot-file fields
          --show-transformed-names, --show-stored-names
                                 show file or archive names after transformation
          --totals[=SIGNAL]      print total bytes after processing the archive;
                                 with an argument - print total bytes when this
                                 SIGNAL is delivered; Allowed signals are: SIGHUP,
                                 SIGQUIT, SIGINT, SIGUSR1 and SIGUSR2; the names
                                 without SIG prefix are also accepted
          --utc                  print file modification times in UTC
      -v, --verbose              verbosely list files processed
          --warning=KEYWORD      warning control
      -w, --interactive, --confirmation
                                 ask for confirmation for every action

     Compatibility options:

      -o                         when creating, same as --old-archive; when
                                 extracting, same as --no-same-owner

     Other options:

      -?, --help                 give this help list
          --restrict             disable use of some potentially harmful options
          --usage                give a short usage message
          --version              print program version

    Mandatory or optional arguments to long options are also mandatory or optional
    for any corresponding short options.

    The backup suffix is '~', unless set with --suffix or SIMPLE_BACKUP_SUFFIX.
    The version control may be set with --backup or VERSION_CONTROL, values are:

      none, off       never make backups
      t, numbered     make numbered backups
      nil, existing   numbered if numbered backups exist, simple otherwise
      never, simple   always make simple backups

    Valid arguments for the --quoting-style option are:

      literal
      shell
      shell-always
      shell-escape
      shell-escape-always
      c
      c-maybe
      escape
      locale
      clocale

    *This* tar defaults to:
    --format=gnu -f- -b20 --quoting-style=escape --rmt-command=/usr/sbin/rmt

Most of the tar operations and options can be written in any of three forms: long, short, and old style.

** Note**\
The \"old style\" option forms exist in GNU tar for compatibility with Unix tar.

#### [Three most frequently used options]

##### [Creation]

`user `[`$`]`tar --create`

or

`user `[`$`]`tar -c`

##### [Listing]

`user `[`$`]`tar --list`

or

`user `[`$`]`tar -t`

##### [Extraction]

`user `[`$`]`tar --extract`

or

`user `[`$`]`tar -x`

Some useful options are:

-   `-xz`: for [tar.gz] or [.tgz].
-   `-xy`: for [tar.bz2] or [.tbz2].
-   `-xJ`: for [tar.xz] or [.txz].

\

** Note**\
The fastest way to extract a tarball is ` tar -xf tarball` because it can recognize any additional extensions.

##### [Additional options]

-   To specify the name of an archive:

`user `[`$`]`tar --file=archive-name`

or

`user `[`$`]`tar -f `*`archive-name`*

-   For showing the files being worked on as tar is running:

`user `[`$`]`tar --verbose`

or

`user `[`$`]`tar -v`

#### [Compression]

There are many ways to create a compressed tar file, also known as a \'tarball\'. The best one may be:

`user `[`$`]`tar --auto-compress`

or

`user `[`$`]`tar -a`

This option will select the compression program based on the suffix of the archive file name. For example:

`user `[`$`]`tar caf archive.tar.bz2`

This command will produce a bz2 tarball, while:

`user `[`$`]` tar -caf archive.tar.lzma`

will produce an lzma tarball.

** Note**\
As mentioned previously, the \"old\" style is maintained for compatibility reasons; therefore `caf` and `-caf` still work the same way.

## [Additional information]

Due to tar\'s wide variety of options, it isn\'t possible to cover all the advanced features of this program within a single wiki entry. Some of the more advanced features include:

-   Adding files to existing archives;
-   Updating an archive;
-   Specifying options with `--extract`;
-   Backing up and restoring files;
-   Excluding some files; and
-   Crossing file system boundaries.

This information and more is available in the [GNU tar manual](https://www.gnu.org/software/tar/manual/html_section/tar.html#SEC_Top)

## [Removal]

`root `[`#`]`emerge --ask --depclean app-arch/tar`

## [See also]

-   [Backup](https://wiki.gentoo.org/wiki/Backup "Backup") --- prevent loss of data by ensuring it can be recovered.
-   [Data compression](https://wiki.gentoo.org/wiki/Data_compression "Data compression") --- a list of some of the **compression and file-archiver utilities** available in Gentoo Linux

## [External resources]

-   [Official GNU tar website](https://www.gnu.org/software/tar/).