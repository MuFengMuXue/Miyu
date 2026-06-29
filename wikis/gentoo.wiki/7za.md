*Not to be confused with [7-Zip](https://wiki.gentoo.org/wiki/7-Zip "7-Zip").*

** Warning**\
As of 2024-08-02, the last **update** of p7zip was a **year ago** ^[\[1\]](#cite_note-1)^, and it is probably **vulnerable** ^[\[2\]](#cite_note-2)[\[3\]](#cite_note-3)^, so it is better to use [7-Zip](https://wiki.gentoo.org/wiki/7-Zip "7-Zip") instead.

**Resources**

[[]][GitHub](https://github.com/p7zip-project/p7zip)

[[]][Wikipedia](https://en.wikipedia.org/wiki/7-Zip "wikipedia:7-Zip")

**p7zip** is a command-line port of [7-Zip](https://www.7-zip.org/) for POSIX compliant systems such as Unix, macOS, BeOS, and Amiga. Created by Igor Pavlov, the 7-Zip [compression](https://wiki.gentoo.org/wiki/Data_compression "Data compression") type implements the LZMA compression algorithm, which is one of the highest compression ratios currently available. Since version 4.10 it supports little and big endian machines.^[\[4\]](#cite_note-4)^ p7zip has most of the additional compression methods from the windows only 7zip plugin [modern7z](https://www.tc4shell.com/en/7zip/modern7z/) ported and integrated in core. Additional compression methods available compared to 7zip are BROTLI, ZSTD, LZ5, LZ4, LIZARD and FLZMA2.

** Important**\
The 7-zip archive format does **not** store standard Unix file permissions such as owner/group or extended file attributes. Those who desire to use 7-zip as a long-term backup or archiving solution should wrap files in a tar archive before compressing with [7z]. Examples are provided below.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
-   [[2] [Usage]](#Usage)
    -   [[2.1] [Invocation]](#Invocation)
    -   [[2.2] [Extraction of files to current directory]](#Extraction_of_files_to_current_directory)
    -   [[2.3] [Extraction to a new directory]](#Extraction_to_a_new_directory)
    -   [[2.4] [Preserving file attributes]](#Preserving_file_attributes)
-   [[3] [See also]](#See_also)
-   [[4] [References]](#References)

## [Installation]

### [USE flags]

### [USE flags for] [app-arch/p7zip](https://packages.gentoo.org/packages/app-arch/p7zip) [[]] [Port of 7-Zip archiver for Unix]

  ----------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------
  [`+pch`](https://packages.gentoo.org/useflags/+pch)         Enable precompiled header support for faster compilation at the expense of disk space and memory
  [`natspec`](https://packages.gentoo.org/useflags/natspec)   Use dev-libs/libnatspec to correctly decode non-ascii file names archived in Windows.
  [`rar`](https://packages.gentoo.org/useflags/rar)           Enable support for non-free rar decoder
  [`test`](https://packages.gentoo.org/useflags/test)         Enable dependencies and/or preparations necessary to run tests (usually controlled by FEATURES=test but can be toggled independently)
  ----------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2025-12-19 09:51] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

p7zip can be installed by running:

`root `[`#`]`emerge --ask app-arch/p7zip`

## [Usage]

### [Invocation]

There are three different ways to invoke the compression utility:

-   [7z]
-   [7za]
-   [7zr]

If compiled with the [`wxwidgets`](https://packages.gentoo.org/useflags/wxwidgets) USE flag it also provides a graphical interface via the following invocations:

-   [7zG]
-   [7zFM]

Also a wrapper included is for [7za]:

-   [p7zip]

### [Extraction of files to current directory]

To extract all files from an archive to the current directory without using directory names, use the following command:

`user `[`$`]`7za e <archive name>`

Where `<archive name>` is to be replaced with the archive\'s name.

To extract with full paths, use the following command:

`user `[`$`]`7za x <archive name>`

### [Extraction to a new directory]

To extract into a new directory, use the following command:

`user `[`$`]`7za x -o<folder name> <archive name>`

Where `<folder name>` is the name of the new folder.

### [Preserving file attributes]

When using 7-zip on Gentoo or any other operating system that should preserve Unix file permissions, tar will need to be used in conjunction with 7z to archive or extract files.

Use the following command to archive directories of files, preserving Unix file permissions:

`user `[`$`]`tar cf - <directory> | 7za a -si <directory>.tar.7z`

To extract:

`user `[`$`]`7za x -so <directory>.tar.7z | tar xf -`

## [See also]

-   [Data compression](https://wiki.gentoo.org/wiki/Data_compression "Data compression") --- a list of some of the **compression and file-archiver utilities** available in Gentoo Linux
-   [7-Zip](https://wiki.gentoo.org/wiki/7-Zip "7-Zip") --- a file [archiver](https://wiki.gentoo.org/wiki/Data_compression "Data compression").
-   [Tar](https://wiki.gentoo.org/wiki/Tar "Tar") --- an [archiver](https://wiki.gentoo.org/wiki/Data_compression "Data compression") tool that provides the ability to create tar archives, as well as various other kinds of manipulation.
-   [Zip](https://wiki.gentoo.org/wiki/Zip "Zip") --- provides classic ZIP [compression](https://wiki.gentoo.org/wiki/Data_compression "Data compression")

## [References]

1.  [[[↑](#cite_ref-1)] [[https://github.com/p7zip-project/p7zip/commits/p7zip17/](https://github.com/p7zip-project/p7zip/commits/p7zip17/)]]
2.  [[[↑](#cite_ref-2)] [[[[bug #914736]](https://bugs.gentoo.org/show_bug.cgi?id=914736)[]]]]
3.  [[[↑](#cite_ref-3)] [[https://github.com/p7zip-project/p7zip/issues/224](https://github.com/p7zip-project/p7zip/issues/224)]]
4.  [[[↑](#cite_ref-4)] [[https://sourceforge.net/projects/p7zip/?source=directory](https://sourceforge.net/projects/p7zip/?source=directory)]]