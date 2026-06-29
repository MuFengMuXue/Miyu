**Resources**

[[]][Home](https://sourceware.org/bzip2/)

[[]][Package information](https://packages.gentoo.org/packages/app-arch/bzip2)

**Bzip2** is a high-quality, patent free file [compressor](https://wiki.gentoo.org/wiki/Data_compression "Data compression") using the [Burrows-Wheeler](https://en.wikipedia.org/wiki/Burrows%E2%80%93Wheeler_transform "wikipedia:Burrows–Wheeler transform") algorithm. Files are typically compressed to anywhere between 10% - 15% of their original size^[\[1\]](#cite_note-1)^ while maintaining a speed of roughly twice the speed of compression and up to six times the speed of decompression of the PPM compression family. Any machine with an ANSI C compiler should be able to support bzip2, making it a great choice for those who run systems with portable demands.

In 2019, an experimental Rust rewrite of bzip2 started ^[\[2\]](#cite_note-2)^ with the blessing of the bzip2 maintainer, but progress was slow. A new maintainer took over the nascent Rust rewrite repository in 2021 ^[\[3\]](#cite_note-3)^ but there does not appear to be movement towards a release.

The original bzip2 is [still maintained](https://sourceware.org/bzip2/downloads.html) on Sourceware despite the initial plans otherwise.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
-   [[2] [Usage]](#Usage)
    -   [[2.1] [Invocation]](#Invocation)
        -   [[2.1.1] [Compression]](#Compression)
        -   [[2.1.2] [Decompression]](#Decompression)
    -   [[2.2] [Memory management]](#Memory_management)
    -   [[2.3] [Parallelization]](#Parallelization)
-   [[3] [Configuration]](#Configuration)
    -   [[3.1] [Environment variables]](#Environment_variables)
-   [[4] [Removal]](#Removal)
    -   [[4.1] [Unmerge]](#Unmerge)
-   [[5] [See also]](#See_also)
-   [[6] [References]](#References)

## [Installation]

### [USE flags]

### [USE flags for] [app-arch/bzip2](https://packages.gentoo.org/packages/app-arch/bzip2) [[]] [A high-quality data compressor used extensively by Gentoo Linux]

  ------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------
  [`static`](https://packages.gentoo.org/useflags/static)             !!do not set this during bootstrap!! Causes binaries to be statically linked instead of dynamically
  [`static-libs`](https://packages.gentoo.org/useflags/static-libs)   Build static versions of dynamic libraries as well
  [`verify-sig`](https://packages.gentoo.org/useflags/verify-sig)     Verify upstream signatures on distfiles
  ------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2025-09-02 17:00] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

After adjusting USE flags:

`root `[`#`]`emerge --ask app-arch/bzip2`

## [Usage]

### [Invocation]

Displays the default bzip2 arguments summary. The command line options are similar to [gzip](https://wiki.gentoo.org/wiki/Gzip "Gzip"), however they aren\'t identical and so a little revision on bzip2\'s arguments go a long way. For more information, see the [bzip2 man page.](https://linux.die.net/man/1/bzip2)

A short summary of usage flags can be found below:

`user `[`$`]`bzip2 --help`

    bzip2, a block-sorting file compressor.  Version 1.0.8, 13-Jul-2019.

       usage: bzip2 [flags and input files in any order]

       -h --help           print this message
       -d --decompress     force decompression
       -z --compress       force compression
       -k --keep           keep (don't delete) input files
       -f --force          overwrite existing output files
       -t --test           test compressed file integrity
       -c --stdout         output to standard out
       -q --quiet          suppress noncritical error messages
       -v --verbose        be verbose (a 2nd -v gives more)
       -L --license        display software version & license
       -V --version        display software version & license
       -s --small          use less memory (at most 2500k)
       -1 .. -9            set block size to 100k .. 900k
       --fast              alias for -1
       --best              alias for -9

       If invoked as `bzip2', default action is to compress.
                  as `bunzip2',  default action is to decompress.
                  as `bzcat', default action is to decompress to stdout.

       If no file names are given, bzip2 compresses or decompresses
       from standard input to standard output.  You can combine
       short flags, so `-v -4' means the same as -v4 or -4v, &c.

#### [Compression]

The default behavior of bzip2 is to compress a file when given as an argument.

`user `[`$`]`bzip2 <file-to-compress>`

If forcing a compression operation is desired, bzip2 can be invoked with the `-z` option:

`user `[`$`]`bzip2 -z <file-to-compress>`

#### [Decompression]

If invoked as bunzip2, the default action is to decompress a given file:

`user `[`$`]`bunzip2 <file-to-decompress>`

A file can also be decompressed to stdout:

`user `[`$`]`bzcat <file-to-decompress>`

If no arguments are given, bzip2 will compress/decompress from standard input to standard output.

### [Memory management]

bzip2 compresses large files in blocks. The block size is proportionate to the compression ratio achieved and the total amount of memory needed for compression and decompression. Block size is read from the header of the file and can be specified manually when compressing.

** Tip**\
You can specify the block sized used by setting `-1` through to `-9`, which specifies block sizes of 100,000 bytes through to 900,000 bytes respectively.

When decompressing bzip2 will read this and allocate just enough space to decompress the file. Because during decompression, the block size is read from the header, the -1 to -9 flags are ignored.^[\[4\]](#cite_note-4)^ For more information, visit the [bzip2 man page.](https://linux.die.net/man/1/bzip2)

### [Parallelization]

bzip2 itself does not support parallel compression or decompression. [[[app-arch/lbzip2]](https://packages.gentoo.org/packages/app-arch/lbzip2)[]] however can be used for parallel compression by some tools, either opportunistically (e.g. Dracut), or if configured (like [tar](https://wiki.gentoo.org/wiki/Tar#Configuration "Tar")). Another option is [[[app-arch/pbzip2]](https://packages.gentoo.org/packages/app-arch/pbzip2)[]].

As a result of some tools using [lbzip2] opportunistically, simply installing lbzip2 can be useful even without configuration. To maximize the usage of lbzip2 (or pbzip2), enable one of the [[[lbzip2]](https://packages.gentoo.org/useflags/lbzip2)[[]](https://wiki.gentoo.org/wiki/USE_flag "USE flag")] or [[[pbzip2]](https://packages.gentoo.org/useflags/pbzip2)[[]](https://wiki.gentoo.org/wiki/USE_flag "USE flag")] [USE flags](https://wiki.gentoo.org/wiki/USE_flag "USE flag") on [[[app-alternatives/bzip2]](https://packages.gentoo.org/packages/app-alternatives/bzip2)[]] which will create a symlink at [bzip2] to [lbzip2] (or [pbzip2], respectively).

## [Configuration]

### [Environment variables]

## [Removal]

### [Unmerge]

`root `[`#`]`emerge --ask --depclean --verbose app-arch/bzip2`

## [See also]

-   [Gzip](https://wiki.gentoo.org/wiki/Gzip "Gzip") --- a data [compression](https://wiki.gentoo.org/wiki/Data_compression "Data compression") utility maintained by the GNU project that uses Lempel-Ziv (LZ77) encoding
-   [Zstd](https://wiki.gentoo.org/wiki/Zstd "Zstd") --- a fast, lossless [compression](https://wiki.gentoo.org/wiki/Data_compression "Data compression") algorithm and tool suite
-   [Xz-utils](https://wiki.gentoo.org/wiki/Xz-utils "Xz-utils") --- LZMA2-based data [compression](https://wiki.gentoo.org/wiki/Data_compression "Data compression") utility.

## [References]

1.  [[[↑](#cite_ref-1)] [[What is bzip2? - https://sourceware.org/bzip2/](https://sourceware.org/bzip2/)]]
2.  [[[↑](#cite_ref-2)] [Federico Mena Quintero. [Maintaining bzip2](https://viruta.org/maintaining-bzip2.html), [Federico\'s Blog](https://viruta.org/), June 4th, 2019. Retrieved on October 18th, 2022.]]
3.  [[[↑](#cite_ref-3)] [Federico Mena Quintero. [Bzip2\'s experimental repository is changing maintainership, https://viruta.org/ Federico\'s Blog](https://viruta.org/bzip2-changing-maintainership.html), June 3rd, 2021. Retrieved on October 18th, 2022.]]
4.  [[[↑](#cite_ref-4)] [[https://linux.die.net/man/1/bzip2](https://linux.die.net/man/1/bzip2)]]