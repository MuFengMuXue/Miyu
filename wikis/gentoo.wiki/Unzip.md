**Resources**

[[]][Home](http://www.info-zip.org/UnZip.html)

[[]][Wikipedia](https://en.wikipedia.org/wiki/Info-ZIP "wikipedia:Info-ZIP")

**UnZip** provides [decompression](https://wiki.gentoo.org/wiki/Data_compression "Data compression") for classic zip formats. Includes supports for Unicode and encryption if appropriate [USE flags](https://wiki.gentoo.org/wiki/USE_flag "USE flag") have been selected.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
-   [[2] [Removal]](#Removal)
-   [[3] [Configuration]](#Configuration)
    -   [[3.1] [Environment variables]](#Environment_variables)
-   [[4] [Invocation]](#Invocation)
-   [[5] [Usage]](#Usage)
-   [[6] [See also]](#See_also)

## [Installation]

### [USE flags]

### [USE flags for] [app-arch/unzip](https://packages.gentoo.org/packages/app-arch/unzip) [[]] [unzipper for pkzip-compressed files]

  ----------------------------------------------------------- ---------------------------------------------------------------------------------------
  [`bzip2`](https://packages.gentoo.org/useflags/bzip2)       Enable bzip2 compression support
  [`natspec`](https://packages.gentoo.org/useflags/natspec)   Use dev-libs/libnatspec to correctly decode non-ascii file names archived in Windows.
  [`unicode`](https://packages.gentoo.org/useflags/unicode)   Add support for Unicode
  ----------------------------------------------------------- ---------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-05-02 00:03] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

`root `[`#`]`emerge --ask app-arch/unzip`

## [Removal]

`root `[`#`]`emerge --ask --unmerge app-arch/unzip`

## [Configuration]

### [Environment variables]

The following environment variables are available:

-   `UNZIP` - Sets UnZip to run with any option.
-   `UNZIP_OPTS` - For use in VMS systems. Does the same as `UNZIP` (see above).

See the UnZip man page for more environment variable information.

## [Invocation]

`user `[`$`]`unzip -h`

    UnZip 6.00 of 20 April 2009, by Info-ZIP.  Maintained by C. Spieler.  Send
    bug reports using http://www.info-zip.org/zip-bug.html; see README for details.

    Usage: unzip [-Z] [-opts[modifiers]] file[.zip] [list] [-x xlist] [-d exdir]
      Default action is to extract files in list, except those in xlist, to exdir;
      file[.zip] may be a wildcard.  -Z => ZipInfo mode ("unzip -Z" for usage).

      -p  extract files to pipe, no messages     -l  list files (short format)
      -f  freshen existing files, create none    -t  test compressed archive data
      -u  update files, create if necessary      -z  display archive comment only
      -v  list verbosely/show version info       -T  timestamp archive to latest
      -x  exclude files that follow (in xlist)   -d  extract files into exdir
    modifiers:
      -n  never overwrite existing files         -q  quiet mode (-qq => quieter)
      -o  overwrite files WITHOUT prompting      -a  auto-convert any text files
      -j  junk paths (do not make directories)   -aa treat ALL files as text
      -U  use escapes for all non-ASCII Unicode  -UU ignore any Unicode fields
      -C  match filenames case-insensitively     -L  make (some) names lowercase
      -X  restore UID/GID info                   -V  retain VMS version numbers
      -K  keep setuid/setgid/tacky permissions   -M  pipe through "more" pager
    See "unzip -hh" or unzip.txt for more help.  Examples:
      unzip data1 -x joe   => extract all files except joe from zipfile data1.zip
      unzip -p foo | more  => send contents of foo.zip via pipe into program more
      unzip -fo foo ReadMe => quietly replace existing ReadMe if archive file newer

## [Usage]

Extracting all the compressed file in the current directory

`user `[`$`]`unzip temp.zip`

Decompressing an archive without creating directories

`user `[`$`]`unzip -j temp.zip`

Forcefully overwrite existing files when decompressing

`user `[`$`]`unzip -o temp.zip`

Decompressing archive to another directory

`user `[`$`]`unzip temp.zip -d /tmp`

See the content of a zip file without decompressing

`user `[`$`]`unzip -l temp.zip`

Exclude certain file during the decompression

`user `[`$`]`unzip temp.zip -x bashscript.sh -d /tmp`

List detailed information about the archive

`user `[`$`]`unzip -Z temp.zip`

Converting text files when decompressing

`user `[`$`]`unzip -a temp.zip`

To test our test.zip, printing only a summary message indicating whether the archive is OK or not

`user `[`$`]`unzip -tq temp.zip`

To test all zipfiles in the current directory, printing only the summaries

`user `[`$`]`unzip -tq '*.zip'`

To extract all text source files only \'.txt\'

`user `[`$`]`unzip temp.zip '*.txt'`

To extract only newer versions of the files already in the current directory

`user `[`$`]`unzip -fo temp.zip `

To extract newer versions of the files already in the current directory and to create any files not already there

`user `[`$`]`unzip -uo temp.zip`

Extract a password protected zip file

`user `[`$`]`unzip -P  passwordprotected.zip `

Listing files only from zip archive

`user `[`$`]`unzip -l /path/to/file.zip`

## [See also]

-   [Data compression](https://wiki.gentoo.org/wiki/Data_compression "Data compression") --- a list of some of the **compression and file-archiver utilities** available in Gentoo Linux
-   [Zip](https://wiki.gentoo.org/wiki/Zip "Zip") --- provides classic ZIP [compression](https://wiki.gentoo.org/wiki/Data_compression "Data compression")