**Resources**

[[]][Home](https://www.gnu.org/software/gzip/)

[[]][Official documentation](https://www.gnu.org/software/gzip/manual/)

[[]][Package information](https://packages.gentoo.org/packages/app-arch/gzip)

[[]][Wikipedia](https://en.wikipedia.org/wiki/gzip "wikipedia:gzip")

[![Ohloh Logo](/images/thumb/c/c1/Ohloh-logo.png/30px-Ohloh-logo.png)][Open Hub](https://www.openhub.net/p/gzip)

**[gzip]** is a data [compression](https://wiki.gentoo.org/wiki/Data_compression "Data compression") utility maintained by the GNU project that uses Lempel-Ziv (LZ77) encoding. It is commonly paired with archivers such as [[tar](https://wiki.gentoo.org/wiki/Tar "Tar")] prior to compression. Therefore, it is common to see files compressed with [gzip] that end in [.gz], [.tar.gz] and [.tgz] extensions among others.

**[gzip]** can be considered the standard and historical GNU compressor. Although still very relevant, it is less frequently used for package distribution due to lower compression ratios compared to more modern algorithms (such as the [xz format](https://wiki.gentoo.org/wiki/Xz-utils "Xz-utils") provided by [[[app-arch/xz-utils]](https://packages.gentoo.org/packages/app-arch/xz-utils)[]]).

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
-   [[2] [Usage]](#Usage)
    -   [[2.1] [Invocation]](#Invocation)
    -   [[2.2] [Parallelization]](#Parallelization)
-   [[3] [Removal]](#Removal)
    -   [[3.1] [Unmerge]](#Unmerge)
-   [[4] [See also]](#See_also)
-   [[5] [External references]](#External_references)

## [Installation]

### [USE flags]

### [USE flags for] [app-arch/gzip](https://packages.gentoo.org/packages/app-arch/gzip) [[]] [Standard GNU compressor]

  ----------------------------------------------------------------- -----------------------------------------------------------------------------------------------------
  [`pic`](https://packages.gentoo.org/useflags/pic)                 disable optimized assembly code that is not PIC friendly
  [`static`](https://packages.gentoo.org/useflags/static)           !!do not set this during bootstrap!! Causes binaries to be statically linked instead of dynamically
  [`verify-sig`](https://packages.gentoo.org/useflags/verify-sig)   Verify upstream signatures on distfiles
  ----------------------------------------------------------------- -----------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-05-02 17:50] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

`root `[`#`]`emerge --ask app-arch/gzip`

## [Usage]

There are several related utilities included in with the gzip package.

  -------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Binary   Description
  gunzip   Decompresses files compressed using the gzip compression algorithm. Restores a gzip-compressed file to its original form
  gzexe    Compresses executable files using the gzip compression algorithm. Reduces the size of executable files, potentially saving disk space
  gzip     A popular compression utility used to compress files using the gzip compression algorithm. Reduces the size of files, making them more efficient for storage or transmission
  zcat     Displays the contents of a compressed file on the terminal without decompressing it. Reads the compressed file and outputs the uncompressed contents
  zcmp     Compares two compressed files byte by byte. Checks if the compressed files are identical by decompressing them and comparing.
  zdiff    Displays the differences between two compressed files. Decompresses the files and shows the differing lines side by side.
  zegrep   Searches for a pattern or regular expression in compressed files. Decompresses the files and performs the search using extended regular expressions.
  zfgrep   Searches for a fixed string pattern in compressed files. Decompresses the files and searches for the fixed string within them.
  zforce   Forces compression or recompression of files using the gzip compression algorithm. Can update or overwrite compressed files even if the resulting file may not be smaller.
  zgrep    Searches for a pattern or regular expression in compressed files. Decompresses the files and performs the search using basic regular expressions.
  zless    Views the contents of compressed files one screen at a time. Decompresses the file and displays the contents in a pager-like interface.
  zmore    Displays the contents of a compressed file page by page. Decompresses the file and shows the uncompressed contents in a controlled manner.
  znew     Recompresses files in the \".Z\" format to the \".gz\" format. Converts files compressed with the older \"compress\" utility to the gzip compression format.
  -------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### [Invocation]

`user `[`$`]`gzip --help`

    Usage: gzip [OPTION]... [FILE]...
    Compress or uncompress FILEs (by default, compress FILES in-place).

    Mandatory arguments to long options are mandatory for short options too.

      -c, --stdout      write on standard output, keep original files unchanged
      -d, --decompress  decompress
      -f, --force       force overwrite of output file and compress links
      -h, --help        give this help
      -k, --keep        keep (don't delete) input files
      -l, --list        list compressed file contents
      -L, --license     display software license
      -n, --no-name     do not save or restore the original name and timestamp
      -N, --name        save or restore the original name and timestamp
      -q, --quiet       suppress all warnings
      -r, --recursive   operate recursively on directories
          --rsyncable   make rsync-friendly archive
      -S, --suffix=SUF  use suffix SUF on compressed files
          --synchronous synchronous output (safer if system crashes, but slower)
      -t, --test        test compressed file integrity
      -v, --verbose     verbose mode
      -V, --version     display version number
      -1, --fast        compress faster
      -9, --best        compress better

    With no FILE, or when FILE is -, read standard input.

    Report bugs to <bug-gzip@gnu.org>.

### [Parallelization]

gzip itself does not support parallel compression or decompression. [[[app-arch/pigz]](https://packages.gentoo.org/packages/app-arch/pigz)[]] however can be used for parallel compression by some tools, either opportunistically (e.g. Dracut), or if configured (like [tar](https://wiki.gentoo.org/wiki/Tar#Configuration "Tar")).

As a result of some tools using [pigz] opportunistically, simply installing pigz can be useful even without configuration. To maximize the usage of pigz, enable the [[[pigz]](https://packages.gentoo.org/useflags/pigz)[[]](https://wiki.gentoo.org/wiki/USE_flag "USE flag")] [USE flag](https://wiki.gentoo.org/wiki/USE_flag "USE flag") on [[[app-alternatives/gzip]](https://packages.gentoo.org/packages/app-alternatives/gzip)[]] which will create a symlink from [gzip] to [pigz].

The gzip format does not lend itself to parallel decompression and the zlib/pigz maintainer has stated it is not possible for pigz to be extended for it ^[\[1\]](#cite_note-1)^.

## [Removal]

### [Unmerge]

`root `[`#`]`emerge --ask --depclean --verbose app-arch/gzip`

## [See also]

-   [Bzip2](https://wiki.gentoo.org/wiki/Bzip2 "Bzip2") --- high-quality, patent free file [compressor](https://wiki.gentoo.org/wiki/Data_compression "Data compression") using the [Burrows-Wheeler](https://en.wikipedia.org/wiki/Burrows%E2%80%93Wheeler_transform "wikipedia:Burrows–Wheeler transform") algorithm.
-   [Data compression](https://wiki.gentoo.org/wiki/Data_compression "Data compression") --- a list of some of the **compression and file-archiver utilities** available in Gentoo Linux
-   [p7zip](https://wiki.gentoo.org/wiki/P7zip "P7zip") --- a command-line port of [7-Zip](https://www.7-zip.org/) for POSIX compliant systems such as Unix, macOS, BeOS, and Amiga.
-   [tar](https://wiki.gentoo.org/wiki/Tar "Tar") --- an [archiver](https://wiki.gentoo.org/wiki/Data_compression "Data compression") tool that provides the ability to create tar archives, as well as various other kinds of manipulation.
-   [xz](https://wiki.gentoo.org/wiki/Xz "Xz") --- LZMA2-based data [compression](https://wiki.gentoo.org/wiki/Data_compression "Data compression") utility.
-   [zip](https://wiki.gentoo.org/wiki/Zip "Zip") --- provides classic ZIP [compression](https://wiki.gentoo.org/wiki/Data_compression "Data compression")

## [External references]

-   [[[app-arch/pigz]](https://packages.gentoo.org/packages/app-arch/pigz)[]] - a parallel implementation of gzip.

1.  [[[↑](#cite_ref-1)] [Mark Adler. [Decompressing with pigz is not parallel](https://github.com/madler/pigz/issues/36#issuecomment-249041503), [pigz bug tracker](https://github.com/madler/pigz/issues), September 22nd, 2016. Retrieved on September 29th, 2022.]]