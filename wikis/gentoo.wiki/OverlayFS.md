Other languages:

-   [English]
-   [français](https://wiki.gentoo.org/wiki/OverlayFS/fr "OverlayFS (46% translated)")
-   [magyar](https://wiki.gentoo.org/wiki/OverlayFS/hu "OverlayFS (100% translated)")
-   [日本語](https://wiki.gentoo.org/wiki/OverlayFS/ja "OverlayFS (100% translated)")

**Resources**

[[]][Home](https://kernel.org/)

[[]][Wikipedia](https://en.wikipedia.org/wiki/OverlayFS "wikipedia:OverlayFS")

[[]][Official documentation](https://www.kernel.org/doc/Documentation/filesystems/overlayfs.txt)

[[]][GitWeb](https://git.kernel.org/cgit/linux/kernel/git/apw/overlayfs.git/)

**Overlayfs** (**Overlay** **F**ile**s**ystem) is an in-kernel attempt at providing union file system capabilities on Linux. OverlayFS differs from other union filesystem implementations in that after a file is opened all operations go directly to the underlying, lower or upper, filesystems. This simplifies the implementation and allows native performance in these cases.^[\[1\]](#cite_note-1)^

The option to enable OverlayFS exists in Linux kernels 3.18 and higher.^[\[2\]](#cite_note-2)^

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [Kernel]](#Kernel)
-   [[2] [Usage]](#Usage)
-   [[3] [Example]](#Example)
-   [[4] [See also]](#See_also)
-   [[5] [External resources]](#External_resources)
-   [[6] [References]](#References)

## [Installation]

### [Kernel]

[KERNEL] **Enable OverlayFS (OVERLAY_FS) support**

    File systems  --->
       [*] Overlay filesystem support

## [Usage]

Once enabled in the kernel OverlayFS can be controlled using the [mount] command.

`root `[`#`]`mount -t overlay overlay -o lowerdir=``lowerdir``,upperdir=``upperdir``,workdir=``workdir`` ``mountpoint`

## [Example]

To mount an overlay filesystem using the following example of a structure on an ext4 base filesystem.

Create the following folder structure:

`user `[`$`]`tree test_folder`

    test_folder
    ├── low
    ├── my_overlay
    └── up

On the folder *low*, create a file with a clear and recognizable name. Repeat the step on the folder *up* to get a structure similar to the following:

`user `[`$`]`tree test_folder`

    test_folder
    ├── low
    │   └── low_file
    ├── my_overlay
    └── up
        └── up_file

Having that tree, the following command will create an overlay structure with the *up* folder above the *low* folder and that structure will be on the *my_overlay* folder.

`root `[`#`]`mount -t overlay overlay -o lowerdir=/test_folder/low,upperdir=/test_folder/up,workdir=/test_folder/my_overlay /test_folder/my_overlay/`

After inspecting the tree structure of the test_folder, this will be printed:

`user `[`$`]`tree test_folder`

    test_folder
    ├── low
    │   └── low_file
    ├── my_overlay
    │   ├── low_file
    │   └── up_file
    └── up
        └── up_file

A file can be created using the normal filesystem structure, like the following

`root `[`#`]`touch my_overlay/my_overlay_file`

and will generate the following tree

`user `[`$`]`tree test_folder`

    test_folder
    ├── low
    │   └── low_file
    ├── my_overlay
    │   ├── low_file
    │   ├── my_overlay_file
    │   └── up_file
    └── up
        ├── my_overlay_file
        └── up_file

The overlay working dir can be unmounted with the umount command

`root `[`#`]`umount /test_folder/my_overlay/`

After unmounting the overlay folder, a new subfolder will appear on the directory where the operation was conducted

`user `[`$`]`tree test_folder`

    |
    test_folder
    ├── low
    │   └── low_file
    ├── my_overlay
    │   └── work
    └── up
        ├── my_overlay_file
        └── up_file

That folder will have the following properties

[CODE]

    d--------- 2 root root 4,0K sep  6 09:54 work

** Note**\
Multiple `lowerdir` entries, colon (*:*) separated, can be used. When doing so, `upperdir` and `workdir` can be omitted to make a read-only mount.

** Important**\
When included, both `upperdir` and `workdir` have to reside within the *same* filesystem.

## [See also]

-   [Aufs](https://wiki.gentoo.org/wiki/Aufs "Aufs") --- an advanced multi-layered unification filesystem.
-   [SquashFS](https://wiki.gentoo.org/wiki/SquashFS "SquashFS") --- an open source, read only, extremely compressible filesystem.
-   [Wikipedia:UnionFS](https://en.wikipedia.org/wiki/UnionFS "wikipedia:UnionFS") --- The *original* union filesystem.

## [External resources]

-   [A LWN article written by Jonathan Corbet in June 2011 covering vises and virtues of OverlayFS](http://lwn.net/Articles/447650/)
-   [An informative AskUbuntu.com thread](http://askubuntu.com/a/109441)
-   [Overlay fs in the Linux git repository](https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/Documentation/filesystems/overlayfs.rst)

## [References]

1.  [[[↑](#cite_ref-1)] [[https://github.com/torvalds/linux/commit/e9be9d5e76e34872f0c37d72e25bc27fe9e2c54c](https://github.com/torvalds/linux/commit/e9be9d5e76e34872f0c37d72e25bc27fe9e2c54c)]]
2.  [[[↑](#cite_ref-2)] [[http://www.phoronix.com/scan.php?page=news_item&px=MTc5OTc](http://www.phoronix.com/scan.php?page=news_item&px=MTc5OTc)]]