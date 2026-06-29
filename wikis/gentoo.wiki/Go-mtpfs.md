**Resources**

[[]][Home](https://github.com/hanwen/go-mtpfs)

[[]][Wikipedia](https://en.wikipedia.org/wiki/Media_Transfer_Protocol "wikipedia:Media Transfer Protocol")

Go-mtpfs is a simple FUSE-based filesystem written in Go language for mounting Android devices as a MTP device.

** Note**\
Newer Galaxy Devices (S3, S4, Note2, etc.) use their own MTP-stack and do not work reliably, although this should be fixed in newer versions. See [Bug#29](https://github.com/hanwen/go-mtpfs/issues/29) for more details.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [Prerequisites]](#Prerequisites)
    -   [[1.2] [Kernel]](#Kernel)
    -   [[1.3] [Emerge]](#Emerge)
-   [[2] [Configuration]](#Configuration)
-   [[3] [Usage]](#Usage)
    -   [[3.1] [Bugs]](#Bugs)

## [Installation]

### [Prerequisites]

Allow live builds for two packages in [/etc/portage/package.accept_keywords]:

[FILE] **`/etc/portage/package.accept_keywords`**

    dev-libs/go-fuse **
    sys-fs/go-mtpfs **

### [Kernel]

See the [MTP](https://wiki.gentoo.org/wiki/MTP "MTP") meta article or the [FUSE](https://wiki.gentoo.org/wiki/FUSE "FUSE") article for instructions on enabling FUSE support in the Linux kernel.

### [Emerge]

Install [[[sys-fs/go-mtpfs]](https://packages.gentoo.org/packages/sys-fs/go-mtpfs)[]]:

`root `[`#`]`emerge --ask sys-fs/go-mtpfs`

## [Configuration]

Appropriate users need to be in the `plugdev` group:

`root `[`#`]`gpasswd -a <USER_NAME> plugdev`

## [Usage]

[Mount](https://wiki.gentoo.org/wiki/Mount "Mount"):

`user `[`$`]`mkdir ~/AndroidDevice `

`user `[`$`]`go-mtpfs ~/AndroidDevice & `

Note: If go-mtpfs is not ran in the background (with `&` at the end), another console will be needed to browse the device and unmount the device (when finished).

Unmount:

`user `[`$`]`fusermount -u ~/AndroidDevice`

When the device is unmount, go-mtpfs will quit.

### [Bugs]

1.  [[[dev-libs/go-fuse-9999]](https://packages.gentoo.org/packages/dev-libs/go-fuse-9999)[]] right now has a bug [638912](https://bugs.gentoo.org/638912) that prevents it from building.
2.  MTP is very unreliable on some devices, old files & directories keep showing up, new ones don\'t get updated. One way to update media storage database is through [SD Scanner](https://f-droid.org/en/packages/com.gmail.jerickson314.sdscanner/).