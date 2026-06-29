This page contains [[changes](https://wiki.gentoo.org/index.php?title=MTPfs&diff=1415684)] which are not marked for translation.

**Resources**

[[]][Home](https://www.adebenham.com/mtpfs/)

[[]][Wikipedia](https://en.wikipedia.org/wiki/Media_Transfer_Protocol "wikipedia:Media Transfer Protocol")

\
MTPfs is a FUSE-based filesystem providing access to MTP devices. Typically these devices are Android phones or similar mobile devices.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [Kernel]](#Kernel)
    -   [[1.2] [USE flags]](#USE_flags)
    -   [[1.3] [Emerge]](#Emerge)
-   [[2] [Configuration]](#Configuration)
    -   [[2.1] [Android devices]](#Android_devices)
    -   [[2.2] [Files]](#Files)
    -   [[2.3] [User privileges]](#User_privileges)
-   [[3] [Usage]](#Usage)
-   [[4] [See also]](#See_also)
-   [[5] [References]](#References)

## [Installation]

### [Kernel]

See the [MTP](https://wiki.gentoo.org/wiki/MTP "MTP") meta article or the [FUSE](https://wiki.gentoo.org/wiki/FUSE "FUSE") article for instructions on enabling FUSE support in the Linux kernel.

### [USE flags]

### [USE flags for] [sys-fs/mtpfs](https://packages.gentoo.org/packages/sys-fs/mtpfs) [[]] [A FUSE filesystem providing access to MTP devices]

  ------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [`debug`](https://packages.gentoo.org/useflags/debug)   Enable extra debug codepaths, like asserts and extra output. If you want to get meaningful backtraces see https://wiki.gentoo.org/wiki/Project:Quality_Assurance/Backtraces
  [`mad`](https://packages.gentoo.org/useflags/mad)       Enable handling of MP3\'s metadata
  ------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2024-12-15 16:16] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

[[[sys-fs/mtpfs]](https://packages.gentoo.org/packages/sys-fs/mtpfs)[]] depends on [[[media-libs/libmtp]](https://packages.gentoo.org/packages/media-libs/libmtp)[]]. It turned out^[\[1\]](#cite_note-1)^ that at least version 1.1.8^[\[2\]](#cite_note-2)^ is needed to make it work.^[\[3\]](#cite_note-3)^.

### [Emerge]

Install [[[sys-fs/mtpfs]](https://packages.gentoo.org/packages/sys-fs/mtpfs)[]]:

`root `[`#`]`emerge --ask sys-fs/mtpfs`

## [Configuration]

### [Android devices]

Android devices will need to be put into MTP mode. The way this is done changes slightly based on the version of Android running. On more modern versions, slide down the top of the screen once to show notifications. There should be a notification from the Android System indicating something to the effect of \"USB debugging connected.\" Below this notification is a second notification. Tap the second notification, then change the setting from \"Charge only\" to \"USB for file transfer.\"

### [Files]

Modify [/etc/fuse.conf]:

[FILE] **`/etc/fuse.conf`**

    user_allow_other

### [User privileges]

Appropriate user(s) need to be in the `plugdev` group:

`root `[`#`]`gpasswd -a <USER_NAME> plugdev`

## [Usage]

[Mount](https://wiki.gentoo.org/wiki/Mount "Mount"):

`user `[`$`]`mkdir ~/AndroidDevice`

`user `[`$`]`mtpfs ~/AndroidDevice`

    Unable to open ~/.mtpz-data for reading, MTPZ disabled.
    Device 0 (VID=0bb4 and PID=0c93) is a HTC EVO 4G LTE/One V (ID1).
    Android device detected, assigning default bug flags

** Note**\
Be patient, as this can take several minutes. Upon successful mount, mtpfs will background itself.

Unmount:

`user `[`$`]`fusermount -u ~/AndroidDevice`

## [See also]

-   [MTP](https://wiki.gentoo.org/wiki/MTP "MTP") --- a protocol to allow the transfer of files to external devices.

## [References]

1.  [[[↑](#cite_ref-1)] [[http://forums.gentoo.org/viewtopic-p-7633366.html#7633366](http://forums.gentoo.org/viewtopic-p-7633366.html#7633366)]]

2.  [[[↑](#cite_ref-2)] [[[[bug #527086]](https://bugs.gentoo.org/show_bug.cgi?id=527086)[]]]]

3.  [[[↑](#cite_ref-3)] [libmtp will scan the usb bus and send messages to the log for all attached usb devices]]

        Dec 29 11:58:42 localhost kernel: usb 1-1.2: new full-speed USB device number 8 using ehci-pci
        Dec 29 11:58:42 localhost mtp-probe: checking bus 1, device 8: "/sys/devices/pci0000:00/0000:00:1d.7/usb1/1-1/1-1.2"
        Dec 29 11:58:42 localhost mtp-probe: bus: 1, device: 8 was not an MTP device
        Dec 29 11:59:51 localhost kernel: usb 1-5.1: new low-speed USB device number 10 using ehci-pci
        Dec 29 11:59:51 localhost kernel: input: Logitech Trackball as /devices/pci0000:00/0000:00:1d.7/usb1/1-5/1-5.1/1-5.1:1.0/0003:046D:C404.0007/input/input25
        Dec 29 11:59:51 localhost kernel: hid-generic 0003:046D:C404.0007: input: USB HID v1.10 Mouse [Logitech Trackball] on usb-0000:00:1d.7-5.1/input0
        Dec 29 11:59:51 localhost mtp-probe: checking bus 1, device 10: "/sys/devices/pci0000:00/0000:00:1d.7/usb1/1-5/1-5.1"
        Dec 29 11:59:51 localhost mtp-probe: bus: 1, device: 10 was not an MTP device
        Dec 29 11:59:51 localhost kernel: input: Logitech Logitech Illuminated Keyboard as /devices/pci0000:00/0000:00:1d.7/usb1/1-5/1-5.4/1-5.4:1.0/0003:046D:C318.0008/input/input26
        Dec 29 11:59:51 localhost kernel: hid-generic 0003:046D:C318.0008: input: USB HID v1.11 Keyboard [Logitech Logitech Illuminated Keyboard] on usb-0000:00:1d.7-5.4/input0
        Dec 29 11:59:51 localhost kernel: input: Logitech Logitech Illuminated Keyboard as /devices/pci0000:00/0000:00:1d.7/usb1/1-5/1-5.4/1-5.4:1.1/0003:046D:C318.0009/input/input27
        Dec 29 11:59:51 localhost kernel: hid-generic 0003:046D:C318.0009: input: USB HID v1.11 Device [Logitech Logitech Illuminated Keyboard] on usb-0000:00:1d.7-5.4/input1
        Dec 29 11:59:51 localhost mtp-probe: checking bus 1, device 11: "/sys/devices/pci0000:00/0000:00:1d.7/usb1/1-5/1-5.4"
        Dec 29 11:59:51 localhost mtp-probe: bus: 1, device: 11 was not an MTP device