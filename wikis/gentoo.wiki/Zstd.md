**Resources**

[[]][Home](https://facebook.github.io/zstd/)

[[]][Package information](https://packages.gentoo.org/packages/app-arch/zstd)

[[]][Wikipedia](https://en.wikipedia.org/wiki/Zstd "wikipedia:Zstd")

[[]][GitHub](https://github.com/facebook/zstd)

[[]][Official documentation](https://github.com/facebook/zstd/wiki)

[zstd] is a fast, lossless [compression](https://wiki.gentoo.org/wiki/Data_compression "Data compression") algorithm and tool suite.

zstd can be used to compress files or data streams.

zstd is available as a compression method in the Linux [kernel](https://wiki.gentoo.org/wiki/Kernel "Kernel"), for [initramfs](https://wiki.gentoo.org/wiki/Initramfs "Initramfs") compression, compressed [kernel modules](https://wiki.gentoo.org/wiki/Kernel_Modules "Kernel Modules"), and compressed [swap](https://wiki.gentoo.org/wiki/Swap "Swap") space.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [Kernel]](#Kernel)
    -   [[1.2] [USE flags]](#USE_flags)
    -   [[1.3] [Emerge]](#Emerge)
-   [[2] [Usage]](#Usage)
    -   [[2.1] [Invocation]](#Invocation)
    -   [[2.2] [Parallelization]](#Parallelization)
-   [[3] [Configuration]](#Configuration)
    -   [[3.1] [Portage]](#Portage)
    -   [[3.2] [Dracut]](#Dracut)
    -   [[3.3] [Debug symbols]](#Debug_symbols)
-   [[4] [Removal]](#Removal)
    -   [[4.1] [Unmerge]](#Unmerge)
-   [[5] [See also]](#See_also)
-   [[6] [External resources]](#External_resources)

## [Installation]

### [Kernel]

[KERNEL] **Enable support for zstd (`CONFIG_KERNEL_ZSTD`, `CONFIG_RD_ZSTD`, `CONFIG_MODULE_COMPRESS_ZSTD`, `ZSWAP_COMPRESSOR_DEFAULT_ZSTD`, `CONFIG_CRYPTO_ZSTD`, `CONFIG_F2FS_FS_ZSTD`)**

    General setup  --->
       Kernel compression mode (ZSTD)  --->
          (X) ZSTD
       [*] Initial RAM filesystem and RAM disk (initramfs/initrd) support
          [*]   Support initial ramdisk/ramfs compressed using ZSTD
    [*] Enable loadable module support  --->
       Module compression mode (ZSTD)  --->
          (X) ZSTD
    Memory Management options  --->
       [*] Compressed cache for swap pages (EXPERIMENTAL)
          Compressed cache for swap pages default compressor (zstd)  --->
             (X) zstd
    Cryptographic API  --->
          Zstd compression algorithm
    File systems  --->
       <M> F2FS filesystem support
          [*]     ZSTD compression support

### [USE flags]

### [USE flags for] [app-arch/zstd](https://packages.gentoo.org/packages/app-arch/zstd) [[]] [zstd fast compression library]

  ------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------
  [`+lzma`](https://packages.gentoo.org/useflags/+lzma)               Support for LZMA compression algorithm
  [`lz4`](https://packages.gentoo.org/useflags/lz4)                   Enable support for lz4 compression (as implemented in app-arch/lz4)
  [`static-libs`](https://packages.gentoo.org/useflags/static-libs)   Build static versions of dynamic libraries as well
  [`test`](https://packages.gentoo.org/useflags/test)                 Enable dependencies and/or preparations necessary to run tests (usually controlled by FEATURES=test but can be toggled independently)
  [`verify-sig`](https://packages.gentoo.org/useflags/verify-sig)     Verify upstream signatures on distfiles
  [`zlib`](https://packages.gentoo.org/useflags/zlib)                 Add support for zlib compression
  ------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-01-21 02:07] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

`root `[`#`]`emerge --ask app-arch/zstd`

## [Usage]

### [Invocation]

`user `[`$`]`zstd --help`

    *** zstd command line interface 64-bits v1.5.2, by Yann Collet ***
    Usage :
          zstd [args] [FILE(s)] [-o file]

    FILE    : a filename
              with no FILE, or when FILE is - , read standard input
    Arguments :
     -#     : # compression level (1-19, default: 3)
     -d     : decompression
     -D DICT: use DICT as Dictionary for compression or decompression
     -o file: result stored into `file` (only 1 output file)
     -f     : disable input and output checks. Allows overwriting existing files,
              input from console, output to stdout, operating on links,
              block devices, etc.
    --rm    : remove source file(s) after successful de/compression
     -k     : preserve source file(s) (default)
     -h/-H  : display help/long help and exit

    Advanced arguments :
     -V     : display Version number and exit
     -c     : write to standard output (even if it is the console)
     -v     : verbose mode; specify multiple times to increase verbosity
     -q     : suppress warnings; specify twice to suppress errors too
    --[no-]progress : forcibly display, or never display the progress counter.
                      note: any (de)compressed output to terminal will mix with progress counter text.
     -r     : operate recursively on directories
    --filelist FILE : read list of files to operate upon from FILE
    --output-dir-flat DIR : processed files are stored into DIR
    --output-dir-mirror DIR : processed files are stored into DIR respecting original directory structure
    --[no-]check : during compression, add XXH64 integrity checksum to frame (default: enabled). If specified with -d, decompressor will ignore/validate checksums in compressed frame (default: validate).
    --trace FILE : log tracing information to FILE.
    --      : All arguments after "--" are treated as files

    Advanced compression arguments :
    --ultra : enable levels beyond 19, up to 22 (requires more memory)
    --long[=#]: enable long distance matching with given window log (default: 27)
    --fast[=#]: switch to very fast compression levels (default: 1)
    --adapt : dynamically adapt compression level to I/O conditions
    --[no-]row-match-finder : force enable/disable usage of fast row-based matchfinder for greedy, lazy, and lazy2 strategies
    --patch-from=FILE : specify the file to be used as a reference point for zstd's diff engine.
     -T#    : spawns # compression threads (default: 1, 0==# cores)
     -B#    : select size of each job (default: 0==automatic)
    --single-thread : use a single thread for both I/O and compression (result slightly different than -T1)
    --auto-threads= (default: physical} : use either physical cores or logical cores as default when specifying -T0
    --rsyncable : compress using a rsync-friendly method (-B sets block size)
    --exclude-compressed: only compress files that are not already compressed
    --stream-size=# : specify size of streaming input from `stdin`
    --size-hint=# optimize compression parameters for streaming input of approximately this size
    --target-compressed-block-size=# : generate compressed block of approximately targeted size
    --no-dictID : don't write dictID into header (dictionary compression only)
    --[no-]compress-literals : force (un)compressed literals
    --format=zstd : compress files to the .zst format (default)
    --format=gzip : compress files to the .gz format
    --format=xz : compress files to the .xz format
    --format=lzma : compress files to the .lzma format
    --format=lz4 : compress files to the .lz4 format

    Advanced decompression arguments :
     -l     : print information about zstd compressed files
    --test  : test compressed file integrity
     -M#    : Set a memory usage limit for decompression
    --[no-]sparse : sparse mode (default: enabled on file, disabled on stdout)

    Dictionary builder :
    --train ## : create a dictionary from a training set of files
    --train-cover[=k=#,d=#,steps=#,split=#,shrink[=#]] : use the cover algorithm with optional args
    --train-fastcover[=k=#,d=#,f=#,steps=#,split=#,accel=#,shrink[=#]] : use the fast cover algorithm with optional args
    --train-legacy[=s=#] : use the legacy algorithm with selectivity (default: 9)
     -o DICT : DICT is dictionary name (default: dictionary)
    --maxdict=# : limit dictionary to specified size (default: 112640)
    --dictID=# : force dictionary ID to specified value (default: random)

    Benchmark arguments :
     -b#    : benchmark file(s), using # compression level (default: 3)
     -e#    : test all compression levels successively from -b# to -e# (default: 1)
     -i#    : minimum evaluation time in seconds (default: 3s)
     -B#    : cut file into independent blocks of size # (default: no block)
     -S     : output one benchmark result per input file (default: consolidated result)
    --priority=rt : set process priority to real-time

### [Parallelization]

zstd supports parallel compression in the main [zstd] utility which can be configured by environment variables or the `-T` parameter. It does not support parallel decompression in the main tool.

However, a *contrib* tool [pzstd] (which is installed alongside [zstd]) can both compress and decompress in parallel. It takes a different argument for the number of threads (`-p`). pzstd is not as widely used as zstd.

## [Configuration]

[zstd] can be configured via environment variables: `ZSTD_NBTHREADS` sets the number of threads to use for compression (0 means \"autodetect number available\") and `ZSTD_CLEVEL` sets the default compression level.

Create the following file:

[FILE] **`/etc/env.d/99zstd`**

    # Use number of threads available for parallel compression
    ZSTD_NBTHREADS="0"

Then run:

`root `[`#`]`env-update && . /etc/profile`

### [Portage]

To use zstd for Portage compression of both installed files and binary packages:

[FILE] **`/etc/portage/make.conf`**

    PORTAGE_COMPRESS="zstd"
    BINPKG_COMPRESS="zstd"

It\'s possible for zstd to work harder at the cost of more resource usage and compression time - to achieve a smaller file:

[FILE] **`/etc/portage/make.conf`**

    PORTAGE_COMPRESS="zstd"
    BINPKG_COMPRESS="zstd"

    # BINPKG_COMPRESS_FLAGS_ZSTD flags:
    # * -T0 (already the default but adding here so it's not lost)
    # * -22: maximum compression level
    # * --ultra: work harder
    BINPKG_COMPRESS_FLAGS_ZSTD="-T0 -22 --ultra"

Note that Portage 3.0.38 or newer will attempt to compress binpkgs in parallel based on `MAKEOPTS`.

### [Dracut]

** Warning**\
The kernel must be compiled with support for zstd compression!

To use zstd for [Dracut\'s](https://wiki.gentoo.org/wiki/Dracut "Dracut") compression of initramfs:

[FILE] **`/etc/dracut.conf.d/compression.conf`**

    compress="zstd"

Currently busybox\'s kmod doesn\'t support zstd-compressed modules, and if `busybox` module is installed in initramfs it ovewrites original kmod. See [here](https://github.com/dracutdevs/dracut/issues/945#issuecomment-954325681)

Thus the `busybox` module should be blacklisted in Dracut:

[FILE] **`/etc/dracut.conf`**

    omit_dracutmodules+=" busybox "

### [Debug symbols]

** Note**\
Valgrind [gained support](https://bugs.kde.org/show_bug.cgi?id=469782) with 3.25.0.

Fangrui Song has championed and successfully implemented zstd debug info support in much of the toolchain, with it now being part of the ELF specification. zstd has some [significant advantages](https://maskray.me/blog/2022-09-09-zstd-compressed-debug-sections) over the default zlib, including compression ratio.

Portage support to make this truly configurable without a user patch is tracked as [[[bug #906367]](https://bugs.gentoo.org/show_bug.cgi?id=906367)[]].

Debug symbols can be compressed using zstd and parsed with the following newer versions of the toolchain:

-   \>=sys-devel/binutils-2.40\[zstd\]
-   \>=dev-libs/elfutils-0.189\[zstd\]
-   \>=dev-debug/gdb-13.1\[zstd\]
-   \>=llvm-core/llvm-16\[zstd\] if using lld or lldb, etc

Note that GCC doesn\'t need USE=zstd as it has a different meaning there (used for compressing LTO IR).

Portage can be patched to pass `--compress-debug-sections=zstd` to enable this:

[FILE] **`/etc/portage/patches/sys-apps/portage/compressdebug-zstd.patch`**

    Make Portage use zstd for debug info compression.
    Make sure binutils[zstd], elfutils[zstd], and gdb[zstd] are emerged first!
    Portage bug to make this properly configurable: https://bugs.gentoo.org/906367
    --- a/bin/estrip
    +++ b/bin/estrip
    @@ -141,7 +141,7 @@ save_elf_debug() " "$" "$" "$" \
                 && "$" --add-gnu-debuglink="$" "$"

    # end of patch

## [Removal]

### [Unmerge]

`root `[`#`]`emerge --ask --depclean --verbose app-arch/zstd`

## [See also]

-   [Gzip](https://wiki.gentoo.org/wiki/Gzip "Gzip") --- a data [compression](https://wiki.gentoo.org/wiki/Data_compression "Data compression") utility maintained by the GNU project that uses Lempel-Ziv (LZ77) encoding
-   [Bzip2](https://wiki.gentoo.org/wiki/Bzip2 "Bzip2") --- high-quality, patent free file [compressor](https://wiki.gentoo.org/wiki/Data_compression "Data compression") using the [Burrows-Wheeler](https://en.wikipedia.org/wiki/Burrows%E2%80%93Wheeler_transform "wikipedia:Burrows–Wheeler transform") algorithm.
-   [Xz-utils](https://wiki.gentoo.org/wiki/Xz-utils "Xz-utils") --- LZMA2-based data [compression](https://wiki.gentoo.org/wiki/Data_compression "Data compression") utility.

## [External resources]

-   [JNI bindings for Zstd native library](https://github.com/luben/zstd-jni) [[[dev-java/zstd-jni]](https://packages.gentoo.org/packages/dev-java/zstd-jni)[]]