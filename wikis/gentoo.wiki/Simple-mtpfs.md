[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=Simple-mtpfs&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

**Resources**

[[]][Home](https://github.com/phatina/simple-mtpfs)

[[]][Wikipedia](https://en.wikipedia.org/wiki/Media_Transfer_Protocol "wikipedia:Media Transfer Protocol")

Simple MTP FUSE filesystem driver written in C++.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [Kernel]](#Kernel)
    -   [[1.2] [Emerge]](#Emerge)
    -   [[1.3] [Usage]](#Usage)

## [Installation]

### [Kernel]

See the [MTP](https://wiki.gentoo.org/wiki/MTP "MTP") meta article or the [FUSE](https://wiki.gentoo.org/wiki/FUSE "FUSE") article for instructions on enabling FUSE support in the Linux kernel.

### [Emerge]

Install [[[sys-fs/simple-mtpfs]](https://packages.gentoo.org/packages/sys-fs/simple-mtpfs)[]]:

`root `[`#`]`emerge --ask sys-fs/simple-mtpfs`

### [Usage]

[Mount](https://wiki.gentoo.org/wiki/Mount "Mount"):

`user `[`$`]`mkdir ~/AndroidDevice `

`user `[`$`]`simple-mtpfs ~/AndroidDevice `

Unmount:

`user `[`$`]`fusermount -u ~/AndroidDevice`