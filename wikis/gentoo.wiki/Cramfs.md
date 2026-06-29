**Resources**

[[]][Wikipedia](https://en.wikipedia.org/wiki/Cramfs "wikipedia:Cramfs")

[[]][GitHub](https://github.com/npitre/cramfs-tools)

Cramfs is a memory and space sensitive filesystem that supports random reading. Ideal for use as ROM, it avoids the block device layer entirely and useful in embedded systems with very tight memory constraints. Cramfs is extremely limited in terms of features and performance.

The precursor to [SquashFS](https://wiki.gentoo.org/wiki/SquashFS "SquashFS"), Cramfs was obsolete since late 2013^[\[1\]](#cite_note-1)^ but has recently found new life from a kernel maintainer in Linux kernel 4.15.0.^[\[2\]](#cite_note-2)^

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [Kernel]](#Kernel)
    -   [[1.2] [Emerge]](#Emerge)
-   [[2] [See also]](#See_also)
-   [[3] [References]](#References)

## [Installation]

### [Kernel]

Specifically the `CONFIG_CRAMFS` and `CONFIG_CRAMFS_BLOCKDEV` options.

[KERNEL] **Enable Cramfs support**

    File systems  --->
      [*] Miscellaneous filesystems  --->
        <*>   Compressed ROM file system support (cramfs)
        [*]     Support CramFs image over a regular block device (NEW)

### [Emerge]

## [See also]

-   [SquashFS](https://wiki.gentoo.org/wiki/SquashFS "SquashFS") --- an open source, read only, extremely compressible filesystem.

## [References]

1.  [[[↑](#cite_ref-1)] [[https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/commit/?id=54886a7153353ea2bf21ebfc1b8e030e71d151d7](https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/commit/?id=54886a7153353ea2bf21ebfc1b8e030e71d151d7)]]
2.  [[[↑](#cite_ref-2)] [[https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/commit/?id=8d59598c35dc1071e6c36f86c9a95f26dd08b4e5](https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/commit/?id=8d59598c35dc1071e6c36f86c9a95f26dd08b4e5)]]