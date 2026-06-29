This page contains [[changes](https://wiki.gentoo.org/index.php?title=MTP&diff=1415682)] which are not marked for translation.

**Resources**

[[]][Wikipedia](https://en.wikipedia.org/wiki/Media_Transfer_Protocol "wikipedia:Media Transfer Protocol")

\
**MTP** (**M**edia **T**ransfer **P**rotocol) is a protocol to allow the transfer of files to external devices. It is provided by several programs, most of them depending on [FUSE](https://wiki.gentoo.org/wiki/FUSE "FUSE").

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [Kernel]](#Kernel)
    -   [[1.2] [User privileges]](#User_privileges)
-   [[2] [Available software]](#Available_software)
    -   [[2.1] [KDE Plasma 5]](#KDE_Plasma_5)
    -   [[2.2] [gMTP]](#gMTP)
-   [[3] [Troubleshooting]](#Troubleshooting)
-   [[4] [See also]](#See_also)
-   [[5] [References]](#References)

## [Installation]

### [Kernel]

Prepare for MTP implementations by activating `CONFIG_FUSE_FS` in the [Linux kernel](https://wiki.gentoo.org/wiki/Kernel/Configuration "Kernel/Configuration").

[KERNEL] **Enable FUSE for MTP implementations:**

    File systems  --->
       <*> FUSE (Filesystem in Userspace) support

### [User privileges]

Any user that needs to have access via MTP should be added to the [usb] and [plugdev] group:

`root `[`#`]`gpasswd -a <USER_NAME> usb`

`root `[`#`]`gpasswd -a <USER_NAME> plugdev`

\'usb\', obviously, because your phone is connected via USB. The missing plugdev group can result in an \'LIBMTP PANIC\' error while testing with^[\[1\]](#cite_note-1)^:

`user `[`$`]`mtp-detect`

## [Available software]

Below are some MTP packages available in Gentoo. Depending on your use case, some packages may work better than others. If you experience freezes or other issues when mounting, listing or copying files, see [Troubleshooting](#Troubleshooting), or try a different package.^[\[2\]](#cite_note-issues-thread-2)^

  -------------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ ------------------------------------------------------------------------------------------------------------------------------------------------------------------ ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Name                                                                       Package                                                                                                                                                                                                                                                                                                                                                                                                                        Homepage                                                                                                                                                           Description
  [MTPfs](https://wiki.gentoo.org/wiki/MTPfs "MTPfs")                        [[[sys-fs/mtpfs]](https://packages.gentoo.org/packages/sys-fs/mtpfs)[]]                                                                     [https://www.adebenham.com/mtpfs/](https://www.adebenham.com/mtpfs/)                                                               A FUSE-based filesystem providing access to MTP devices. More mature than some of the alternatives.
  [Go-mtpfs](https://wiki.gentoo.org/wiki/Go-mtpfs "Go-mtpfs")               [[[sys-fs/go-mtpfs]](https://packages.gentoo.org/packages/sys-fs/go-mtpfs)[]]                                                            [https://github.com/hanwen/go-mtpfs](https://github.com/hanwen/go-mtpfs)                                                           A simple FUSE-based filesystem written in Go language.
  jmtpfs                                                                     [[[sys-fs/jmtpfs]](https://packages.gentoo.org/packages/sys-fs/jmtpfs)[]]                                                                  [https://github.com/JasonFerrara/jmtpfs](https://github.com/JasonFerrara/jmtpfs)                                                   A FUSE and [[[media-libs/libmtp]](https://packages.gentoo.org/packages/media-libs/libmtp)[]] based filesystem for accessing MTP devices.
  [gphotofs](https://wiki.gentoo.org/wiki/Gphotofs "Gphotofs")               [[[media-gfx/gphotofs]](https://packages.gentoo.org/packages/media-gfx/gphotofs)[]]                                                   [http://www.something.com](http://www.something.com)                                                                               gphotofs is a FUSE-based file system for interfacing with digital cameras using the gphoto2 application.
  [simple-mtpfs](https://wiki.gentoo.org/wiki/Simple-mtpfs "Simple-mtpfs")   [[[sys-fs/simple-mtpfs]](https://packages.gentoo.org/packages/sys-fs/simple-mtpfs)[]]                                                [https://github.com/phatina/simple-mtpfs](https://github.com/phatina/simple-mtpfs)                                                 Like the others: a simple MTP FUSE filesystem driver written in C++.
  [Gnome](https://wiki.gentoo.org/wiki/Gnome "Gnome")          [[[gnome-base/gvfs]](https://packages.gentoo.org/packages/gnome-base/gvfs)[]]                                                            [https://wiki.gnome.org/Projects/gvfs](https://wiki.gnome.org/Projects/gvfs)                                                       Install [[[gnome-base/gvfs]](https://packages.gentoo.org/packages/gnome-base/gvfs)[]] with the `mtp` USE flag enabled. This can be either globally in [make.conf]\'s USE flag or for [[[gnome-base/gvfs]](https://packages.gentoo.org/packages/gnome-base/gvfs)[]] in [package.use].
  [Thunar](https://wiki.gentoo.org/wiki/Thunar "Thunar")                     [[[xfce-base/thunar-volman]](https://packages.gentoo.org/packages/xfce-base/thunar-volman)[]]                                    [https://goodies.xfce.org/projects/thunar-plugins/thunar-volman](https://goodies.xfce.org/projects/thunar-plugins/thunar-volman)   To have Thunar automount MTP devices (and other volumes), install the [[[xfce-base/thunar-volman]](https://packages.gentoo.org/packages/xfce-base/thunar-volman)[]] package and make sure [[[gnome-base/gvfs]](https://packages.gentoo.org/packages/gnome-base/gvfs)[]] is also installed with the `mtp` USE flag enabled as above.
  Android File Transfer for Linux                                            [[[sys-fs/android-file-transfer-linux]](https://packages.gentoo.org/packages/sys-fs/android-file-transfer-linux)[]]   [https://whoozle.github.io/android-file-transfer-linux/](https://whoozle.github.io/android-file-transfer-linux/)                   Robust MTP implementation with unlimited file size support, partial 64-bit edits, album cover, USB zero copy, with Qt, CLI and Fuse interfaces available.
  -------------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ ------------------------------------------------------------------------------------------------------------------------------------------------------------------ ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### [KDE Plasma 5]

**kio-extras** contains MTP support, but it requires the `mtp` USE flag.

Enable the global `mtp` use flag; one way of doing it is by creating a file named [mtp] in [/etc/portage/package.use]:

[FILE] **`/etc/portage/package.use/mtp`**

    */* mtp

Then run a [\@world](https://wiki.gentoo.org/wiki/World_set_(Portage) "World set (Portage)") update:

`root `[`#`]`emerge --ask --deep --newuse --update @world`

Alternatively, enable it in only in [[[kde-apps/kio-extras]](https://packages.gentoo.org/packages/kde-apps/kio-extras)[]]:

[FILE] **`/etc/portage/package.use/mtp`**

    kde-apps/kio-extras mtp

After either approach mentioned above, install [[[kde-apps/kio-extras]](https://packages.gentoo.org/packages/kde-apps/kio-extras)[]]:

`root `[`#`]`emerge --ask kde-apps/kio-extras`

After this, quitting [plasmashell] and restarting is probably sufficient to get it working.

If that does not work, please try restarting the system.

### [gMTP]

**gMTP** is a simple MTP client for Solaris and Linux.

It is sufficient to just install and run [[[media-sound/gmtp]](https://packages.gentoo.org/packages/media-sound/gmtp)[]]:

`root `[`#`]`emerge --ask media-sound/gmtp`

`user `[`$`]`gmtp`

Click on connect. A few second later, the file hierarchy on the device should appear. It is now possible to manipulate the files on the device. It support features like Album Artwork and playlists.

## [Troubleshooting]

-   Make sure the Android device is not going to sleep and the screen is not getting locked. Set screen timeout to very long values, or enable the \"Do not turn off the screen\" flag in the device\'s Settings - Development section.
-   Some ROMs (e.g. PAC ROM) require the unlocking of the screen of the device before files will appear. If the screen is not unlocked the device will appear empty.
-   Sometimes (specifically on HTC One X) USB debugging automatically activates when device is connected to a PC. USB debugging must be *disabled*. Otherwise [[[media-libs/libmtp]](https://packages.gentoo.org/packages/media-libs/libmtp)[]] can\'t recognize the device.
-   If the device is not recognized by [[[media-libs/libmtp]](https://packages.gentoo.org/packages/media-libs/libmtp)[]], try upgrading to latest (or even live) version.
-   Lumia devices might require [[[media-libs/libmtp]](https://packages.gentoo.org/packages/media-libs/libmtp)[]] version 1.1.9 and [[[sys-fs/simple-mtpfs]](https://packages.gentoo.org/packages/sys-fs/simple-mtpfs)[]] to be mounted properly.
    -   Lumia devices must be unlocked to be able to connect (enter the user\'s PIN).

If all else fails, using a different package from the above list may help.^[\[2\]](#cite_note-issues-thread-2)^ It is also possible the cable between the computer and device only allows charging. Using a different cable supporting data transfer fixes this.

## [See also]

-   [MTPfs](https://wiki.gentoo.org/wiki/MTPfs "MTPfs") --- a FUSE-based filesystem providing access to MTP devices.

## [References]

1.  [[[↑](#cite_ref-1)] [Available via [[[media-libs/libmtp]](https://packages.gentoo.org/packages/media-libs/libmtp)[]]]]
2.  [[↑ ^[2.0](#cite_ref-issues-thread_2-0)^ ^[2.1](#cite_ref-issues-thread_2-1)^] [[Gentoo Forums thread discussing issues experienced with the packages listed here](https://forums.gentoo.org/viewtopic-p-8757499.html)]]