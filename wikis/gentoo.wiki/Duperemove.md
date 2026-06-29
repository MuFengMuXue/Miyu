**Resources**

[[]][GitHub](https://github.com/markfasheh/duperemove)

Duperemove is a [btrfs](https://wiki.gentoo.org/wiki/Btrfs "Btrfs") and [XFS](https://wiki.gentoo.org/wiki/XFS "XFS") tool for finding duplicated extents and submitting them to the kernel for [deduplication](https://wiki.gentoo.org/wiki/Deduplication "Deduplication").

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [Emerge]](#Emerge)
-   [[2] [Usage]](#Usage)
    -   [[2.1] [Invocation]](#Invocation)
    -   [[2.2] [Reading a file list created with fdupes]](#Reading_a_file_list_created_with_fdupes)
-   [[3] [See also]](#See_also)

## [Installation]

### [Emerge]

`root `[`#`]`emerge --ask sys-fs/duperemove`

## [Usage]

Detailed information can be seen by running [man duperemove].

### [Invocation]

`root `[`#`]`duperemove --help`

    duperemove v0.11
    Find duplicate extents and optionally dedupe them.

    Basic usage: duperemove [-r] [-d] [-h] [-v] [-A] [--hashfile=hashfile] OBJECTS

    "OBJECTS" is a list of files (or directories) which we
    want to find duplicate extents in. If a directory is
    specified, all regular files inside of it will be scanned.

        <switches>
        -r      Enable recursive dir traversal.
        -d      De-dupe the results (must run on a supported fs).
        --hashfile=FILE Store hashes in this file.
        -A      Open files for dedupe in read-only mode.
        -h      Print numbers in human-readable format.
        -v      Print extra information (verbose).
        --help      Prints this help text.

    Please see the duperemove(8) manpage for a complete list of options.

The following command shows how to deduplicate the [/home] filesystem; the hash file will be stored under the [/root] directory:

`root `[`#`]`duperemove -rdh --hashfile=/root/home.hash /home`

** Note**\
The previous command may be interrupted at any time with [Ctrl]+[c] and resumed later without risk of corrupting any data.

### [Reading a file list created with fdupes]

By passing the `--fdupes` option, [duperemove] can work in conjunction with [[fdupes](https://wiki.gentoo.org/wiki/Fdupes "Fdupes")] in order to deduplicate a pre-calculated list of files. When in this mode, input will be accepted on stdin:

`root `[`#`]`cat fdupes_list.txt | duperemove --fdupes`

This is handy when a list of duplicates has already been created so that disk-intensive deduplication job can be ran at a time when the system is not under heavy load.

It is also possible to deduplicate directly from fdupes (without creating a file list):

`root `[`#`]`fdupes -r /path/to/filesystem/directory | duperemove --fdupes`

## [See also]

-   [Deduplication](https://wiki.gentoo.org/wiki/Deduplication "Deduplication") --- a mechanism for reducing the space taken by multiple identical copies of a file are stored on a [filesystem](https://wiki.gentoo.org/wiki/Filesystem "Filesystem")
-   [fdupes](https://wiki.gentoo.org/wiki/Fdupes "Fdupes") --- a tool for identifying duplicate files across a set of directories.
-   [btrfs](https://wiki.gentoo.org/wiki/Btrfs "Btrfs") --- a copy-on-write (CoW) [filesystem](https://wiki.gentoo.org/wiki/Filesystem "Filesystem") for Linux aimed at implementing advanced features while focusing on fault tolerance, self-healing properties, and easy administration.
-   [XFS](https://wiki.gentoo.org/wiki/XFS "XFS") --- a high-performance journaling [filesystem](https://wiki.gentoo.org/wiki/Filesystem "Filesystem")