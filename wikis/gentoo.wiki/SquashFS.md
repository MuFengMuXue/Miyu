Other languages:

-   [English]
-   [magyar](https://wiki.gentoo.org/wiki/SquashFS/hu "SquashFS (84% translated)")
-   [日本語](https://wiki.gentoo.org/wiki/SquashFS/ja "SquashFS (84% translated)")

**Resources**

[[]][Home](http://squashfs.sourceforge.net/)

[[]][Sourceforge](https://sourceforge.net/projects/squashfs/)

[[]][Wikipedia](https://en.wikipedia.org/wiki/SquashFS "wikipedia:SquashFS")

**SquashFS** is an open source, read only, extremely compressible filesystem. Like other filesystems, SquashFS is capable of de-duplicating the data passed to it, which helps it compress data further. Although not fully necessary to operate correctly, SquashFS is typically paired with some kind of union [filesystem](https://wiki.gentoo.org/wiki/Filesystem "Filesystem") when used for Live media (LiveUSBs and LiveCDs).

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [Kernel]](#Kernel)
        -   [[1.1.1] [Optional SquashFS support]](#Optional_SquashFS_support)
    -   [[1.2] [USE flags]](#USE_flags)
    -   [[1.3] [Emerge]](#Emerge)
-   [[2] [Usage]](#Usage)
    -   [[2.1] [Filesystem creation]](#Filesystem_creation)
    -   [[2.2] [Mount]](#Mount)
    -   [[2.3] [Unmount]](#Unmount)
    -   [[2.4] [Extract]](#Extract)
    -   [[2.5] [Booting]](#Booting)
-   [[3] [Troubleshooting]](#Troubleshooting)
    -   [[3.1] [mount: only root can use \"\--options\" option]](#mount:_only_root_can_use_.22--options.22_option)
-   [[4] [See also]](#See_also)
-   [[5] [External resources]](#External_resources)
-   [[6] [References]](#References)

## [Installation]

### [Kernel]

The following kernel options *must* be activated for SquashFS support:

[KERNEL] **Enabling SquashFS 4.0 support**

    Device Drivers --->
      [*] Block devices Search for <code>CONFIG_BLK_DEV</code> to find this item.  --->
         [*]   Loopback device support Search for <code>CONFIG_BLK_DEV_LOOP</code> to find this item.
    File systems  --->
      [*] Miscellaneous filesystems Search for <code>CONFIG_MISC_FILESYSTEMS</code> to find this item.  --->
         [*]   SquashFS 4.0 - Squashed file system support Search for <code>CONFIG_SQUASHFS</code> to find this item.

\

#### [Optional SquashFS support]

[KERNEL] **Enabling optional features of SquashFS**

    File systems  --->
      [*] Miscellaneous filesystems Search for <code>CONFIG_MISC_FILESYSTEMS</code> to find this item.  --->
            File decompression options (Decompress file data into an intermediate buffer)  --->
            Decompressor parallelisation options (Single threaded compression)  --->
         [*]     Squashfs XATTR support Search for <code>CONFIG_SQUASHFS_XATTR</code> to find this item.
         [*]     Include support for ZLIB compressed file systems Search for <code>CONFIG_SQUASHFS_ZLIB</code> to find this item.
         [*]     Include support for LZ4 compressed file systems Search for <code>CONFIG_SQUASHFS_LZ4</code> to find this item.
         [*]     Include support for LZO compressed file systems Search for <code>CONFIG_SQUASHFS_LZO</code> to find this item.
         [*]     Include support for XZ compressed file systems Search for <code>CONFIG_SQUASHFS_XZ</code> to find this item.
         [*]     Include support for ZSTD compressed file systems Search for <code>CONFIG_SQUASHFS_ZSTD</code> to find this item.
         [*]     Use 4K device block size? Search for <code>CONFIG_SQUASHFS_4K_DEVBLK_SIZE</code> to find this item.
         [*]     Additional option for memory-constrained systems Search for <code>CONFIG_SQUASHFS_EMBEDDED</code> to find this item.
         (3)       Number of fragments cached Search for <code>CONFIG_SQUASHFS_FRAGMENT_CACHE_SIZE</code> to find this item.

### [USE flags]

Like most filesystems in Linux, the SquashFS filesystem tools come in a separate package. This package is called [[[sys-fs/squashfs-tools]](https://packages.gentoo.org/packages/sys-fs/squashfs-tools)[]]. Set the desired support for the package by adjusting USE flags accordingly.

### [USE flags for] [sys-fs/squashfs-tools](https://packages.gentoo.org/packages/sys-fs/squashfs-tools) [[]] [Tools to create and extract Squashfs filesystems]

  ------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [`debug`](https://packages.gentoo.org/useflags/debug)   Enable extra debug codepaths, like asserts and extra output. If you want to get meaningful backtraces see https://wiki.gentoo.org/wiki/Project:Quality_Assurance/Backtraces
  [`lz4`](https://packages.gentoo.org/useflags/lz4)       Enable support for lz4 compression (as implemented in app-arch/lz4)
  [`lzma`](https://packages.gentoo.org/useflags/lzma)     Support for LZMA compression algorithm
  [`lzo`](https://packages.gentoo.org/useflags/lzo)       Enable support for lzo compression
  [`xattr`](https://packages.gentoo.org/useflags/xattr)   Add support for extended attributes (filesystem-stored metadata)
  [`zstd`](https://packages.gentoo.org/useflags/zstd)     Enable support for ZSTD compression
  ------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-04-05 06:55] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

After setting flags as desired, update the system so the changes take effect:

`root `[`#`]`emerge --ask --changed-use --deep sys-fs/squashfs-tools`

## [Usage]

### [Filesystem creation]

Creation of SquashFS filesystems is performed with the [mksquashfs] command. To create a SquashFS filesystem of the home directory of a user named larry, the following command could be used:

`larry@example $``mksquashfs /home/larry /home/larry/home.squashfs`

Depending on what kernel features were selected for SquashFS support, the output of the [mksquashfs] command will look something like the following:

` `

    Parallel mksquashfs: Using 4 processors
    Creating 4.0 filesystem on /home/larry/home.squashfs, block size 131072.
    [=========================================================================|] 4/4 100%

    Exportable Squashfs 4.0 filesystem, gzip compressed, data block size 131072
            compressed data, compressed metadata, compressed fragments, compressed xattrs
            duplicates are removed
    Filesystem size 0.82 Kbytes (0.00 Mbytes)
            58.79% of uncompressed filesystem size (1.39 Kbytes)
    Inode table size 104 bytes (0.10 Kbytes)
            46.02% of uncompressed inode table size (226 bytes)
    Directory table size 96 bytes (0.09 Kbytes)
            77.42% of uncompressed directory table size (124 bytes)
    Number of duplicate files found 1
    Number of inodes 7
    Number of files 5
    Number of fragments 1
    Number of symbolic links  0
    Number of device nodes 0
    Number of fifo nodes 0
    Number of socket nodes 0
    Number of directories 2
    Number of ids (unique uids + gids) 1
    Number of uids 1
            larry (1001)
    Number of gids 1
            larry (1001)

Notice the command provides an excellent summary of what went into the newly created [home.squashfs] file. Information such as filesystem size, inode table, directory table, number of duplicate files, UIDs, and GIDs are easily readable. This information can be very helpful when attempting to gather specific information from the filesystem.

### [Mount]

To mount a SquashFS, use the [mount] command\'s `-o loop` option with escalated privileges:

`larry@example $``mkdir ~/tmp `

`larry@example $``mount -o loop ~/home.squashfs ~/tmp `

** Note**\
If the [mount] command fails, see the related entry in the troubleshooting section below.

Now all the files that are included in [home.squashfs] are available under the [\~/tmp] mount point. List the files in the directory using the `-la` options to see all the files:

`larry@example $``ls -la ~/tmp`

    total 3
    drwxr-xr-x 3 larry larry 125 Mar 31 13:51 .
    drwxr-xr-x 1 larry larry 130 Mar 31 13:52 ..
    -rw------- 1 larry larry  10 Mar 31 13:49 .bash_history
    -rw-r--r-- 1 larry larry 127 Mar 24 13:19 .bash_logout
    -rw-r--r-- 1 larry larry 193 Mar 24 13:19 .bash_profile
    -rw-r--r-- 1 larry larry 551 Mar 24 13:19 .bashrc
    -rw-r--r-- 1 larry larry   0 Mar 31 13:51 home.squashfs
    drwx------ 2 larry larry   3 Oct 23 06:52 .ssh

### [Unmount]

To unmount the filesystem, use the [umount] command with escalated privileges:

`larry@example $``sudo umount ~/tmp`

### [Extract]

SquashFS files can be extracted using [unsquashfs]. Supposing the [\~/tmp] directory and the [\~/home.squashfs] file have been previously created in the steps above:

`larry@example $``unsquashfs -d tmp/ -f home.squashfs`

** Important**\
\* If a filesystem *target* is not specified ([\~/tmp] is the target in the example above) [unsquashfs] will create a folder called [squashfs-root] in the *current* directory and extract the files there.^[\[1\]](#cite_note-pavlovCecchetti2008-1)^

-   If a directory exists previous to the [unsquashfs] command being run, then the `-d <directory>` and `-f` options must be used in order to force SquashFS extraction to the *existing* directory ^[\[1\]](#cite_note-pavlovCecchetti2008-1)^
-   When extracting to a *new* directory, the `-f` option is not needed.

[unsquashfs] can be used to extract a specific file in the SquashFS. Again, presuming the [\~/home.squashfs] file has been previously created in the steps above, the [.bashrc] file can be extracted to the [\~/tmp] directory:

`larry@example $``unsquashfs -d ~/tmp -f ~/home.squashfs -e .bashrc`

    Parallel unsquashfs: Using 4 processors
    1 inodes (1 blocks) to write

    [===========================|] 1/1 100%

    created 1 files
    created 1 directories
    created 0 symlinks
    created 0 devices
    created 0 fifos

View the extract file using the [ls] command:

`larry@example $``ls -la ~/tmp`

    total 4
    drwxr-xr-x 1 larry larry  14 Mar 31 13:51 .
    drwxr-xr-x 1 larry larry 156 Mar 31 14:32 ..
    -rw-r--r-- 1 larry larry 551 Mar 24 13:19 .bashrc

### [Booting]

Asuming we\'re using dracut, simply put your squashfs image to your boot device and append this to the boot cmdline (e.g. via GRUB):

    rd.live.image root=live:<YOUR BOOT DEVICE>

The boot device is in the format you\'d usually have your `root=...` in, be it in the format of [/dev/sdXY], [], or []

By default, it will look for it under the path [LiveOS/squashfs.img]. If you want to use a different file location, you\'d instead have:

    rd.live.image root=live:<YOUR BOOT DEVICE> rd.live.dir=<DIR> rd.live.squashimg=<IMG_FILE>

## [Troubleshooting]

### [][mount: only root can use \"\--options\" option]

This error is should be self-explanatory. Log in as the root user or use [[sudo](https://wiki.gentoo.org/wiki/Sudo "Sudo")] to mount the filesystem with escalated privileges.

## [See also]

-   [OverlayFS](https://wiki.gentoo.org/wiki/OverlayFS "OverlayFS") --- an in-kernel attempt at providing union file system capabilities on Linux.
-   [Wikipedia:UnionFS](https://en.wikipedia.org/wiki/UnionFS "wikipedia:UnionFS") - The *original* union filesystem.

## [External resources]

-   [A SquashFS instructional video on YouTube](https://www.youtube.com/watch?v=Rt6U2gG0ggw).
-   Forums thread [TIP: Compressing portage using squashfs: initscript method](https://forums.gentoo.org/viewtopic-t-465367-start-67-postdays-0-postorder-asc-highlight-.html)
-   [Article/Script](https://startux.de/linux/8-gentoo/11-squashed-portage-tree) using SquashFS to store and update portage tree
-   [Portage tree using squashfs and overlayfs](https://www.brunsware.de/blog/gentoo/portage-tree-squashfs-overlayfs.html)
-   [GitHub - nrdvana/squash-portage: Script to generate squashfs files of the Gentoo portage tree](https://github.com/nrdvana/squash-portage)

## [References]

1.  [[↑ ^[1.0](#cite_ref-pavlovCecchetti2008_1-0)^ ^[1.1](#cite_ref-pavlovCecchetti2008_1-1)^] [Artemiy I. Pavlov, Marco Cecchetti. [The SquashFS tools exposed](http://www.tldp.org/HOWTO/SquashFS-HOWTO/mksqoverview.html), [The Linux Documentation Project](http://www.tldp.org/), July 24, 2008. Retrieved on April 8, 2015]]