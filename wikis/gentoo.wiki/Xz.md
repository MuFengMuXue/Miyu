**Resources**

[[]][Home](https://tukaani.org/xz/)

[[]][Package information](https://packages.gentoo.org/packages/app-arch/xz-utils)

[[]][Wikipedia](https://en.wikipedia.org/wiki/XZ_Utils "wikipedia:XZ Utils")

[[]][GitHub](https://github.com/tukaani-project/xz)

[![Ohloh Logo](/images/thumb/c/c1/Ohloh-logo.png/30px-Ohloh-logo.png)][Open Hub](https://www.openhub.net/p/xz-utils)

[[]][GitWeb](https://git.tukaani.org/?p=xz.git)

[xz] is an LZMA2-based data [compression](https://wiki.gentoo.org/wiki/Data_compression "Data compression") utility. Typically, files compressed with LZMA2 compression are 30% smaller than equivalent [gzip] files and 15% smaller than equivalent [bzip2] files.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [Emerge]](#Emerge)
-   [[2] [Usage]](#Usage)
    -   [[2.1] [Parallelization]](#Parallelization)
-   [[3] [Configuration]](#Configuration)
    -   [[3.1] [Portage]](#Portage)
    -   [[3.2] [Dracut]](#Dracut)
    -   [[3.3] [systemd]](#systemd)
-   [[4] [Removal]](#Removal)
    -   [[4.1] [Unmerge]](#Unmerge)
-   [[5] [See also]](#See_also)
-   [[6] [References]](#References)

## [Installation]

### [Emerge]

The [[[app-arch/xz-utils]](https://packages.gentoo.org/packages/app-arch/xz-utils)[]] package provides utilities for mangling xz-compressed files:

`root `[`#`]`emerge --ask app-arch/xz-utils`

## [Usage]

[xz] has multiple compression levels available. The default is `-6`. The normal highest level is `-9`.

If the user is willing to accept more memory usage and time to compress, `--extreme` (-e) can be used with a numerical level to increase the intensity, e.g. [xz -9e].

xz 5.4.0 or newer can also decompress lzip files, as they share the same format (LZMA) ^[\[1\]](#cite_note-1)^ ^[\[2\]](#cite_note-2)^.

### [Parallelization]

1.  All modern versions of xz can compress in parallel, but only `>=app-arch/xz-utils-5.4.0` can *decompress* in parallel. Archives must be compressed using the parallel compressor (default as of upcoming 5.6.0) for parallel decompression.
2.  If not using the new xz-utils 5.6.0 release or with \<5.6.0 using -Tn, alternatively, [[[app-arch/pixz]](https://packages.gentoo.org/packages/app-arch/pixz)[]] can be used for parallel decompression **but only with archives made using pixz**. As a result of some tools using [pixz] opportunistically, simply installing pixz can be useful even without configuration.

## [Configuration]

[xz] can be configured via environment variables: `XZ_DEFAULTS` is intended for system administration, while `XZ_OPT` is intended for scripts to set defaults.

Create the following file:

[FILE] **`/etc/env.d/99xz`**

    # -T0: compress and decompress with the number of cores available
    # -9: use maximum compression level (but not extreme)
    XZ_DEFAULTS="-9 -T0"

Then run:

`root `[`#`]`env-update && . /etc/profile`

### [Portage]

To use *xz* for Portage compression of both installed files and binary packages:

[FILE] **`/etc/portage/make.conf`**

    PORTAGE_COMPRESS="xz"
    BINPKG_COMPRESS="xz"

It\'s possible for xz to work harder at the cost of more resource usage and compression time - to achieve a smaller file:

[FILE] **`/etc/portage/make.conf`**

    PORTAGE_COMPRESS="xz"
    BINPKG_COMPRESS="xz"

    # BINPKG_COMPRESS_FLAGS_XZ flags:
    # * --x86: enable the X86 BCJ filter which improves compression of binaries
    # * --lzma2=preset=9e: use compression level 9 with --extreme. This has to be specified last with --lzma2=preset if using a BCJ filter like --x86 because of how xz's filter chains work.
    BINPKG_COMPRESS_FLAGS_XZ="--x86 --lzma2=preset=9e"

Note that Portage 3.0.38 or newer will attempt to decompress xz-compressed distfiles in parallel based on `MAKEOPTS`. It will also attempt to compress and decompress binpkgs in parallel.

### [Dracut]

** Warning**\
The kernel must be compiled with support for xz compression!

To use *xz* for Dracut\'s compression of initramfs:

[FILE] **`/etc/dracut.conf.d/compression.conf`**

    compress="xz"

### [systemd]

** Note**\
The [[[lzma]](https://packages.gentoo.org/useflags/lzma)[[]](https://wiki.gentoo.org/wiki/USE_flag "USE flag")] [USE flag](https://wiki.gentoo.org/wiki/USE_flag "USE flag") must be enabled for [[[sys-apps/systemd]](https://packages.gentoo.org/packages/sys-apps/systemd)[]] first!

systemd has a Meson configuration option `default-compression` to [allow choosing](https://github.com/systemd/systemd/commit/cd3c6322dbc6370448bafc216ee4e19e32a79d9e) the preferred default compression algorithm.

To use *xz*:

[FILE] **`/etc/portage/env/sys-apps/systemd`**

    MYMESONARGS="-Dxz=enabled -Ddefault-compression=xz"

Ensure that [[[lzma]](https://packages.gentoo.org/useflags/lzma)[[]](https://wiki.gentoo.org/wiki/USE_flag "USE flag")] is enabled on [[[sys-apps/systemd]](https://packages.gentoo.org/packages/sys-apps/systemd)[]].

## [Removal]

### [Unmerge]

This package is part of the [system set](https://wiki.gentoo.org/wiki/@system "@system") and should not be removed from systems. *Older* versions of the package can be safely removed by passing the `--depclean` option to [emerge]:

`root `[`#`]`emerge --ask --depclean --verbose app-arch/xz-utils`

## [See also]

-   [Data compression](https://wiki.gentoo.org/wiki/Data_compression "Data compression") --- a list of some of the **compression and file-archiver utilities** available in Gentoo Linux
-   [p7zip](https://wiki.gentoo.org/wiki/P7zip "P7zip") --- a command-line port of [7-Zip](https://www.7-zip.org/) for POSIX compliant systems such as Unix, macOS, BeOS, and Amiga.
-   [zip](https://wiki.gentoo.org/wiki/Zip "Zip") --- provides classic ZIP [compression](https://wiki.gentoo.org/wiki/Data_compression "Data compression")

## [References]

1.  [[[↑](#cite_ref-1)] [Michał Górny. [Lzip decompression support for xz-utils](https://blogs.gentoo.org/mgorny/2021/02/10/lzip-decompression-support-for-xz-utils/), [Michał Górny blog](https://blogs.gentoo.org/mgorny/), February 10th, 2021. Retrieved on September 29th, 2022.]]
2.  [[[↑](#cite_ref-2)] [Jia Tan. [\[xz-devel\] XZ Utils 5.3.3alpha](https://www.mail-archive.com/xz-devel@tukaani.org/msg00593.html), [xz-devel mailing list](https://tukaani.org/xz/lists.html), 27th September, 2022. Retrieved on September 29th, 2022.]]