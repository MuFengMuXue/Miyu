**Resources**

[[]][Wikipedia](https://en.wikipedia.org/wiki/Copy-on-write "wikipedia:Copy-on-write")

**Deduplication** is a mechanism for reducing the space taken by multiple identical copies of a file are stored on a [filesystem](https://wiki.gentoo.org/wiki/Filesystem "Filesystem").

While it would be unusual to deliberately store multiple copies of a file, the situation can arise inadvertently in regular use cases, including:

-   A volume accessed by multiple users, who may not be able to feasibly coordinate their usage, if indeed they are even aware of each other.
-   Development workflows which store dependencies within project folders, which might share dependencies with other unrelated projects.

\
Deduplication uses the **clone** mechanism of a *copy-on-write* or *CoW* capable filesystem, a feature that allows the data of copied but identical files to be shared, much like a [hardlink](https://wiki.gentoo.org/wiki/Util-linux#hardlink "Util-linux") until one of the copies actually is written to and thereby changed, i.e. a delayed copy operation and hence the name *copy-on-write*. If implemented on a block level, only modified blocks are actually stored in the file system, saving space by sharing identical blocks of multiple files.

Copy-on-write (CoW) can be implemented *in-band* or *out-of-band*.^[\[1\]](#cite_note-1)^ The latter is called *deduplication* and requires a user application that compares files or blocks and sets the CoW status for identical blocks in the filesystem, thereby freeing a second block containing identical data.

## Contents

-   [[1] [Filesystems]](#Filesystems)
-   [[2] [Applications with deduplication support]](#Applications_with_deduplication_support)
    -   [[2.1] [GNU coreutils]](#GNU_coreutils)
    -   [[2.2] [Portage]](#Portage)
-   [[3] [Benefits]](#Benefits)
-   [[4] [Practical use scenarios]](#Practical_use_scenarios)
    -   [[4.1] [Portage hooks]](#Portage_hooks)
    -   [[4.2] [Genkernel hooks]](#Genkernel_hooks)
-   [[5] [See also]](#See_also)
-   [[6] [External resources]](#External_resources)
-   [[7] [References]](#References)

## [Filesystems]

On Linux, only a handful of [filesystems](https://wiki.gentoo.org/wiki/Filesystem "Filesystem") implement CoW, namely [bcachefs](https://wiki.gentoo.org/wiki/Bcachefs "Bcachefs"), [Btrfs](https://wiki.gentoo.org/wiki/Btrfs "Btrfs"), [OCFS2](https://en.wikipedia.org/wiki/OCFS2 "wikipedia:OCFS2") and [XFS](https://wiki.gentoo.org/wiki/XFS "XFS"). The clone ioctl kernel functions were previously private to Btrfs, where CoW debuted on Linux, and moved to the Virtual File System (VFS) layer starting with Linux kernel 4.5 so that any CoW-supporting file system can make use of them.^[\[2\]](#cite_note-2)^ The first additional filesystem to implement CoW was XFS.^[\[3\]](#cite_note-3)^

Some filesystem tools themselves support deduplication, like the [Btrfs subvolumes](https://wiki.gentoo.org/wiki/Btrfs#Subvolumes "Btrfs") feature. There are also in-band filesystem options, such as XFS\' `always_cow` sysfs switch.^[\[4\]](#cite_note-4)^

## [Applications with deduplication support]

There are user applications that allow to compare existing files and to deduplicate them, which essentially frees disk space. The most common tools are:

-   [[[sys-fs/duperemove]](https://packages.gentoo.org/packages/sys-fs/duperemove)[]]
-   [[[app-misc/fdupes]](https://packages.gentoo.org/packages/app-misc/fdupes)[]]
-   [[[app-misc/jdupes]](https://packages.gentoo.org/packages/app-misc/jdupes)[]]
-   [[[sys-fs/bees]](https://packages.gentoo.org/packages/sys-fs/bees)[]] (which works on block-level, but is limited to Btrfs)

\
Various tools also support CoW themselves when copying files by using the appropriate Linux syscalls if available:

-   C++ code using `filesystem::copy_file` using GCC 14 or newer\'s libstdc++ ([commit](https://gcc.gnu.org/git/?p=gcc.git;a=commit;h=d87caacf8e2df563afda85f3a5b7b852e08b6b2c))
-   [[[kde-frameworks/kio]](https://packages.gentoo.org/packages/kde-frameworks/kio)[]]
-   [[[dev-libs/glib]](https://packages.gentoo.org/packages/dev-libs/glib)[]] [as of 2.78](https://gitlab.gnome.org/GNOME/glib/-/issues/2863), which will benefit e.g. file copies in Nautilus/Files
-   [[[dev-lang/ruby]](https://packages.gentoo.org/packages/dev-lang/ruby)[]] - Ruby\'s `IO.copy_stream` does and e.g. `FileUtils::copy_file` benefits from it as a result
-   [[[dev-lang/go]](https://packages.gentoo.org/packages/dev-lang/go)[]] - See [https://cs.opensource.google/go/go/+/refs/tags/go1.20.5:src/os/readfrom_linux.go](https://cs.opensource.google/go/go/+/refs/tags/go1.20.5:src/os/readfrom_linux.go).
-   [[[dev-lang/php]](https://packages.gentoo.org/packages/dev-lang/php)[]] - PHP 8.2 [supports it for streams](https://github.com/php/php-src/commit/fa6d97db5d941451615e491034918cdbaa5164bd)
-   [[[app-editors/emacs]](https://packages.gentoo.org/packages/app-editors/emacs)[]] - `copy-file` uses copy_file_range

\
Applications missing support:

-   [[[dev-lang/python]](https://packages.gentoo.org/packages/dev-lang/python)[]]
    -   [https://github.com/python/cpython/issues/81338](https://github.com/python/cpython/issues/81338)
    -   [https://github.com/python/cpython/issues/81338](https://github.com/python/cpython/issues/81338)
-   [[[dev-java/openjdk]](https://packages.gentoo.org/packages/dev-java/openjdk)[]]
    -   [https://bugs.openjdk.org/browse/JDK-8282039](https://bugs.openjdk.org/browse/JDK-8282039) (WONTFIX\'d, seemingly based on a misunderstanding of when the benefit appears - needs a CoW filesystem or using e.g. NFS)
-   [[[net-misc/rsync]](https://packages.gentoo.org/packages/net-misc/rsync)[]]
    -   [https://github.com/WayneD/rsync/issues/153](https://github.com/WayneD/rsync/issues/153)
-   [[[dev-lang/perl]](https://packages.gentoo.org/packages/dev-lang/perl)[]]
    -   See [https://www.nntp.perl.org/group/perl.perl5.porters/2023/07/msg266636.html](https://www.nntp.perl.org/group/perl.perl5.porters/2023/07/msg266636.html)

### [GNU coreutils]

** Tip**\
GNU coreutils 9.0 and newer default to [\--reflink=auto] for [cp] and [install].

The most basic way to deduplicate a file is to clone it with [cp \--reflink]. [[cp](https://wiki.gentoo.org/wiki/GNU_Coreutils#cp "GNU Coreutils")] is part of the [[[sys-apps/coreutils]](https://packages.gentoo.org/packages/sys-apps/coreutils)[]] package. At first the result is almost identical to [[hardlink](https://wiki.gentoo.org/wiki/Util-linux#hardlink "Util-linux")], in that both files use the same blocks of data on the storage device, with the major difference that, if one file gets changed on hardlinks, every linked file is changed as well. On clones (deduplicated files) however the other files that use data from the same blocks are preserved and only the changed file, or blocks of that file, are written to the storage, hence the name *copy-on-write*.

`user `[`$`]`cp --reflink=always sourcefile destfile`

Unlike hardlinks, changing either `destfile` or `sourcefile` will preserve the other. Copy-on-write essentially keeps the files separate while (at least initially) benefiting from the same space advantage as hardlinks do. It is however unclear if the whole file is rewritten in case of a change, or only the changed block (chunk) of an initially deduplicated file, and it heavily depends on how an application implements writing files to disk.

If the filesystem doesn\'t support copy-on-write (CoW), [cp] will abort with an error massage. With the `--reflink=auto` parameter [cp] will automatically make a regular copy instead when CoW is not available.

`user `[`$`]`cp --reflink sourcefile destfile `

    cp: failed to clone 'destfile' from 'sourcefile': Operation not supported

`user `[`$`]`cp --reflink=auto --verbose sourcefile destfile `

    'sourcefile' -> 'destfile'

### [Portage]

Portage uses `copy_file_range` or `sendfile` if available when merging packages from `PORTAGE_TMPDIR` to the live filesystem. This support is implemented as a C extension with [[[native-extensions]](https://packages.gentoo.org/useflags/native-extensions)[[]](https://wiki.gentoo.org/wiki/USE_flag "USE flag")], which is enabled by default for Portage. ^[\[5\]](#cite_note-5)^

Portage 3.0.48 and newer will also avoid overwriting files on the live filesystem if they\'re identical, as implemented for [[[bug #722270]](https://bugs.gentoo.org/show_bug.cgi?id=722270)[]].

## [Benefits]

The obvious benefit of deduplication and copy-on-write is to regain valuable storage space. It might be argued that *in-band* copy-on-write may also be beneficial for reducing wear on [SSD](https://wiki.gentoo.org/wiki/SSD "SSD") storage by reducing writes to the device, similar to [Portage TMPDIR on tmpfs](https://wiki.gentoo.org/wiki/Portage_TMPDIR_on_tmpfs "Portage TMPDIR on tmpfs"). However, a wear reducing factor is uncertain when a write operation has already occurred, which is always the case when using *out-of-band* deduplication tools.

## [[] Practical use scenarios]

### [[] Portage hooks]

Deduplication can be hooked into `pkg_postinst` for specified packages using the [standard portage facilities](https://wiki.gentoo.org/wiki/Handbook:X86/Full/Portage "Handbook:X86/Full/Portage"). For example, to deduplicate the Linux kernels from package [[[sys-kernel/gentoo-sources]](https://packages.gentoo.org/packages/sys-kernel/gentoo-sources)[]] after emerging each new version, a portage environment can be added under [[/etc/portage/package.env](https://wiki.gentoo.org/wiki//etc/portage/package.env "/etc/portage/package.env")]. This will save space for unchanged files of each installed kernel source version under [/usr/src/].

The following example uses [duperemove](https://wiki.gentoo.org/wiki/Duperemove "Duperemove"):

[FILE] **`/etc/portage/env/sys-kernel/gentoo-sources`**

    function post_pkg_postinst()

### [[] Genkernel hooks]

Additionally, after running [genkernel] from [[[sys-kernel/genkernel]](https://packages.gentoo.org/packages/sys-kernel/genkernel)[]], deduplication can be configured in [/etc/genkernel.conf]:

[FILE] **`/etc/genkernel.conf`**

    CMD_CALLBACK="duperemove -r -d -h -q /usr/src/"

## [See also]

-   [Duperemove](https://wiki.gentoo.org/wiki/Duperemove "Duperemove") --- a [btrfs](https://wiki.gentoo.org/wiki/Btrfs "Btrfs") and [XFS](https://wiki.gentoo.org/wiki/XFS "XFS") tool for finding duplicated extents and submitting them to the kernel for [deduplication]
-   [fdupes](https://wiki.gentoo.org/wiki/Fdupes "Fdupes") --- a tool for identifying duplicate files across a set of directories.

## [External resources]

-   [Deduplication](https://btrfs.wiki.kernel.org/index.php/Deduplication), Btrfs Wiki
-   [Which file systems support file cloning](https://www.ctrl.blog/entry/file-cloning.html), Ctrl.blog by Daniel Aleksandersen
-   [XFS, Reflinks and Deduplication](https://strugglers.net/~andy/blog/2017/01/10/xfs-reflinks-and-deduplication/)

## [References]

1.  [[[↑](#cite_ref-1)] [[Read the Docs: Deduplication](https://btrfs.readthedocs.io/en/latest/Deduplication.html)]]
2.  [[[↑](#cite_ref-2)] [[IOCTL_FICLONERANGE(2)](https://www.man7.org/linux/man-pages/man2/ioctl_ficlonerange.2.html) from the Linux Programmer\'s Manual]]
3.  [[[↑](#cite_ref-3)] [[xfs: add reflink and dedupe support](https://lwn.net/Articles/702633/) on LWN.net, 29 Sep 2016]]
4.  [[[↑](#cite_ref-4)] [[XFS Copy-On-Write Support Being Improved, Always CoW Option](https://www.phoronix.com/news/XFS-2019-Copy-On-Write-Better), phoronix, 19 Feb 2019]]
5.  [[[↑](#cite_ref-5)] [[portage_util_file_copy_reflink_linux.c](https://gitweb.gentoo.org/proj/portage.git/tree/src/portage_util_file_copy_reflink_linux.c?h=portage-3.0.49), Portage source code (3.0.49), 10 Jul 2023]]