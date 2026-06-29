**[] Deprecated article**\
\

This article is **deprecated (obsolete)**. Contents are [no longer relevant], and are intended for historical reference only!

\
TLDR: **Do not use this article!**

This HOWTO explains how to setup persistence on the liveDVD media.

## Contents

-   [[1] [Introduction]](#Introduction)
    -   [[1.1] [Persistence Mode]](#Persistence_Mode)
    -   [[1.2] [Requirements]](#Requirements)
-   [[2] [Setup Instructions]](#Setup_Instructions)
    -   [[2.1] [Writable partition]](#Writable_partition)
    -   [[2.2] [Boot liveDVD]](#Boot_liveDVD)

## [Introduction]

### [Persistence Mode]

The latest Gentoo LiveDVD offers the option of using persistence to store changes on the USB. It uses aufs to layer a read-write file system on top of a read-only squashfs compressed file system. This is great, because it allows you to make changes to the livedvd and have those changes appear on future reboots.

### [Requirements]

In order to have persistent data on the latest livedvd you will need to meet the following requirements

1.  At least 256M of free writable space available
2.  Writable device i.e (usb stick, hard drive or ssd)

## [Setup Instructions]

### [Writable partition]

You need to setup a writable file system on the existing usb stick that you use to boot your livedvd, by creating an extra primary partition. This assumes you already ran

`root `[`#`]`dd if=/path/to/image.iso of=/dev/sdc bs=8192k`

on your usb stick but these instructions can work on any writable media. This HOWTO assumes your writable device is /dev/sdc.

1.  Create the primary partition on /dev/sdc

    :::: cmd-box


    `root `[`#`]`fdisk /dev/sdc`


    ::::

2.  Create file system. We will assume that partition is /dev/sdc4

3.  :::: cmd-box


    `root `[`#`]`mke2fs -t ext2 -L aufs-rw /dev/sdc4`


    ::::

### [Boot liveDVD]

You may now boot your media and when prompted for the kernel to use, edit the kernel line and add (aufs=/dev/sdc4) everytime you boot the system, this will allow persistence and write all changes into /dev/sdc4.