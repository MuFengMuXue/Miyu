**Resources**

[[]][Home](http://www.gphoto.org/)

[[]][Wikipedia](https://en.wikipedia.org/wiki/Media_Transfer_Protocol "wikipedia:Media Transfer Protocol")

gphotofs is a FUSE file system for interfacing with digital cameras using gphoto2. Most modern mobile phones are cameras at the same time, and gphotofs can be a good alternative to [MTPfs](https://wiki.gentoo.org/wiki/MTPfs "MTPfs") or [go-mtpfs](https://wiki.gentoo.org/wiki/Go-mtpfs "Go-mtpfs").

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [Kernel]](#Kernel)
    -   [[1.2] [Emerge]](#Emerge)
-   [[2] [Usage]](#Usage)

## [Installation]

### [Kernel]

See the [MTP](https://wiki.gentoo.org/wiki/MTP "MTP") meta article or the [FUSE](https://wiki.gentoo.org/wiki/FUSE "FUSE") article for instructions on enabling FUSE support in the Linux kernel.

### [Emerge]

Install [[[media-gfx/gphotofs]](https://packages.gentoo.org/packages/media-gfx/gphotofs)[]]:

`root `[`#`]`emerge --ask media-gfx/gphotofs`

## [Usage]

[Mount](https://wiki.gentoo.org/wiki/Mount "Mount"):

`user `[`$`]`mkdir ~/AndroidDevice `

`user `[`$`]`gphotofs ~/AndroidDevice -o allow_other `

Unmount:

`user `[`$`]`fusermount -u ~/AndroidDevice`