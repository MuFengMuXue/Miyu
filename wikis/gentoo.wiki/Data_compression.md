**Resources**

[[]][Wikipedia](https://en.wikipedia.org/wiki/Data_compression "wikipedia:Data compression")

This article provides a list of some of the **compression and file-archiver utilities** available in Gentoo Linux.

It\'s important to note distinctions between [file-archiver](https://en.wikipedia.org/wiki/File_archiver "wikipedia:File archiver") utilities able to \"bundle\" multiple files (which may or may not support some forms of compression), and [pure compression](https://en.wikipedia.org/wiki/Lossless_compression "wikipedia:Lossless compression") utilities that can only compress the contents of a file (often without metadata, such as permissions or timestamps). File-archiver utilities are frequently used in conjunction with compression utilities to create a compressed archive containing multiple files and associated metadta.

Target platforms for archive usage are often also an important consideration. Format support may vary, and file metatdata - such as Unix(like) file permissions - may not be available on other platforms, and vice-versa.

Compression has trade-offs including compression ratios, compression times, decompression times, and memory usage. ^[\[1\]](#cite_note-1)^

** See also**\
See [archive managers](https://wiki.gentoo.org/wiki/Recommended_applications#Archive_managers "Recommended applications") on the [recommended applications](https://wiki.gentoo.org/wiki/Recommended_applications "Recommended applications") page for some examples of GUI archiving uilities.

## Contents

-   [[1] [Available software]](#Available_software)
-   [[2] [See also]](#See_also)
-   [[3] [External references]](#External_references)
-   [[4] [References]](#References)

## [Available software]

This is a partial selection of data compression tools available in Gentoo. See [app-arch](https://packages.gentoo.org/categories/app-arch) package category on [packages.g.o](https://packages.gentoo.org), or use a package query tool such as [[eix](https://wiki.gentoo.org/wiki/Eix "Eix")] ([[[app-portage/eix]](https://packages.gentoo.org/packages/app-portage/eix)[]]).

  ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Name                                                                                                                                                                                                  Package                                                                                                                                                                                                                                                                                                                                                                     Description
  [ace]                                                                                                      [[[app-arch/unace]](https://packages.gentoo.org/packages/app-arch/unace)[]]            ACE unarchiver.
  [arj]                                                                                                      [[[app-arch/arj]](https://packages.gentoo.org/packages/app-arch/arj)[]]                  Software tool for creating compressed file archives.
  [[bzip2](https://wiki.gentoo.org/wiki/Bzip2 "Bzip2")]                                                      [[[app-arch/bzip2]](https://packages.gentoo.org/packages/app-arch/bzip2)[]]            High-quality data compressor that used to be the primary compression format used in distributing source code. It is slowly losing ground to the newer, tightly packable xz format.
  [[cpio](https://wiki.gentoo.org/wiki/Cpio "Cpio")]                                                         [[[app-arch/cpio]](https://packages.gentoo.org/packages/app-arch/cpio)[]]               File archival tool which can also read and write tar files.
  [[gzip](https://wiki.gentoo.org/wiki/Gzip "Gzip")]                                                         [[[app-arch/gzip]](https://packages.gentoo.org/packages/app-arch/gzip)[]]               The Standard GNU compressor. One of the oldest of the group, has less compression than bzip2 format.
  lzop                                                                                                                                                                                                  [[[app-arch/lzop]](https://packages.gentoo.org/packages/app-arch/lzop)[]]               Fast (even real-time) compression/decompression.
  [7-Zip](https://wiki.gentoo.org/wiki/7-Zip "7-Zip"), [[7zz](https://wiki.gentoo.org/wiki/7-Zip "7-Zip")]   [[[app-arch/7zip]](https://packages.gentoo.org/packages/app-arch/7zip)[]]               File archiver aiming for high compression ratios.
  [p7zip](https://wiki.gentoo.org/wiki/P7zip "P7zip"), [[7za](https://wiki.gentoo.org/wiki/P7zip "P7zip")]   [[[app-arch/p7zip]](https://packages.gentoo.org/packages/app-arch/p7zip)[]]            [** Warning:** See note in article about possible security issues] Command-line port of 7-Zip for POSIX compliant systems.
  [pax](https://wiki.gentoo.org/wiki/Pax "Pax")                                                                                                                                                         [[[app-arch/pax]](https://packages.gentoo.org/packages/app-arch/pax)[]]                  Archiving utility specified by [POSIX](https://wiki.gentoo.org/wiki/POSIX "POSIX"), intended to replace the [cpio](https://wiki.gentoo.org/wiki/Cpio "Cpio") utility.
  [rar]                                                                                                      [[[app-arch/unrar]](https://packages.gentoo.org/packages/app-arch/unrar)[]]            Uncompress rar files.
  rzip                                                                                                                                                                                                  [[[app-arch/rzip]](https://packages.gentoo.org/packages/app-arch/rzip)[]]               Compression program for large files.
  Snappy                                                                                                                                                                                                [[[app-arch/snappy]](https://packages.gentoo.org/packages/app-arch/snappy)[]]         High-speed compression/decompression library by Google.
  [[tar](https://wiki.gentoo.org/wiki/Tar "Tar")]                                                            [[[app-arch/tar]](https://packages.gentoo.org/packages/app-arch/tar)[]]                  GNU\'s tarball generator software (used extensively by Gentoo Linux). tar has the ability to create [.gz], [.bz2], and [.xz] compression by passing different options. This is one tool all Linux users should have in their tool belt.
  [unar]                                                                                                     [[[app-arch/unar]](https://packages.gentoo.org/packages/app-arch/unar)[]]               The Unarchiver is an open-source utility that can extract RAR files.
  [UnZip](https://wiki.gentoo.org/wiki/UnZip "UnZip")                                                                                                                                                   [[[app-arch/unzip]](https://packages.gentoo.org/packages/app-arch/unzip)[]]            Provides decompression for classic ZIP formats.
  [[xz](https://wiki.gentoo.org/wiki/Xz-utils "Xz-utils")]                                                   [[[app-arch/xz-utils]](https://packages.gentoo.org/packages/app-arch/xz-utils)[]]   Includes utilities for managing LZMA compressed files.
  [[Zip](https://wiki.gentoo.org/wiki/Zip "Zip")]                                                            [[[app-arch/zip]](https://packages.gentoo.org/packages/app-arch/zip)[]]                  Provides classic ZIP compression (this flavor created by Info-ZIP). Nice for cross-platform compatibility with Microsoft operating systems.
  [zoo]                                                                                                      [[[app-arch/zoo]](https://packages.gentoo.org/packages/app-arch/zoo)[]]                  Data compression program and format developed the 1980s and based on LZW.
  [zpaq]                                                                                                     [[[app-arch/zpaq]](https://packages.gentoo.org/packages/app-arch/zpaq)[]]               Journaling incremental deduplicating archiving compressor.
  [[zstd](https://wiki.gentoo.org/wiki/Zstd "Zstd")]                                                         [[[app-arch/zstd]](https://packages.gentoo.org/packages/app-arch/zstd)[]]               zstd fast compression library.
  ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## [See also]

-   [Backup](https://wiki.gentoo.org/wiki/Backup "Backup") --- prevent loss of data by ensuring it can be recovered.

## [External references]

-   [List of archive formats on Wikipedia](https://en.wikipedia.org/wiki/list_of_archive_formats "wikipedia:list of archive formats")
-   [UNPACKER.ECLASS](https://devmanual.gentoo.org/eclass-reference/unpacker.eclass/)

## [[] References]

1.  [[[↑](#cite_ref-1)] [LinuxReviews. [\[1\]](https://linuxreviews.org/Comparison_of_Compression_Algorithms), August 2, 2022. Retrieved on November 20, 2024.]]