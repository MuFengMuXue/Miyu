[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=Woeusb&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

**Resources**

[[]][Home](https://github.com/WoeUSB/WoeUSB)

[[]][Package information](https://packages.gentoo.org/packages/sys-boot/woeusb)

[[]][GitHub](https://github.com/WoeUSB/WoeUSB)

[[]][Bugs (upstream)](https://github.com/WoeUSB/WoeUSB/issues)

**WoeUSB** is a command-line utility for creating Microsoft Windows USB installation media, written in [Bash](https://wiki.gentoo.org/wiki/Bash "Bash").

Microsoft Windows Vista through Windows 11, including Windows PE, are fully supported.

Bootable media can be written using the [FAT32](https://wiki.gentoo.org/wiki/FAT "FAT") and [NTFS](https://wiki.gentoo.org/wiki/NTFS "NTFS") filesystems, which can be booted using legacy [BIOS](https://wiki.gentoo.org/wiki/BIOS "BIOS") and [UEFI](https://wiki.gentoo.org/wiki/UEFI "UEFI") firmware provided the version of Windows being deployed supports it.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [Emerge]](#Emerge)
    -   [[1.2] [Additional software]](#Additional_software)
-   [[2] [Usage]](#Usage)
    -   [[2.1] [Invocation]](#Invocation)
-   [[3] [Removal]](#Removal)
    -   [[3.1] [Unmerge]](#Unmerge)
-   [[4] [See also]](#See_also)
-   [[5] [External resources]](#External_resources)

## [Installation]

### [Emerge]

Install [[[sys-boot/woeusb]](https://packages.gentoo.org/packages/sys-boot/woeusb)[]]:

`root `[`#`]`emerge --ask sys-boot/woeusb`

Note that there are no USE flags for WoeUSB.

### [Additional software]

While the original version of [woeusb] is written in Bash, a [Python](https://wiki.gentoo.org/wiki/Python "Python")-based rewrite is underway called [woeusb-ng]. This package is not yet available in the mainline Gentoo package repository, but a well maintained ebuild exists in [GURU](https://wiki.gentoo.org/wiki/GURU "GURU").

## [Usage]

WoeUSB will not automatically acquire a Windows installation [.iso] file, it requires that such a file already be on-hand. From Windows 10 forward it\'s simple enough to obtain an installation [.iso] directly from Microsoft\'s website. That done, the actual boot USB can be created with the following command:

`root `[`#`]`woeusb --device <windows_installation_disc_image>.iso /dev/<usb_device> --target-filesystem ntfs`

A lot goes into creating a Windows boot disk. This command can take the better part of an hour to complete --- potentially longer when executed on resource constrained systems.

### [Invocation]

`user `[`$`]`woeusb --help`

    WoeUSB 5.2.4 Help Information
    =============================

    WoeUSB can create a bootable Microsoft Windows(R) USB storage device from an existing Windows optical disk or an ISO disk image.

    Supported installation drive preparation modes
    ----------------------------------------------

    Currently two creation methods are supported:

    ### `--device`, `-d` ###

    Completely WIPE the entire USB storage device, then build a bootable Windows USB device from scratch.

    WARNING: All previous data on the device will be gone!

    ```synopsis
    $ woeusb --device <source media path> <device>
    ```

    ```example
    woeusb --device Windows7_x64.iso /dev/sdX
    woeusb --device /dev/sr0 /dev/sdX
    ```

    ### `--partition`, `-p` ###

    Copy Windows files to an existing partition of a USB storage device and make it bootable.  This allows files to coexist as long as no filename conflict exists.

    WARNING: All files that has the same name will be overwritten!

    ```synopsis
    woeusb --partition <source media path>
    ```

    ```example
    woeusb --partition Windows7_x64.iso /dev/sdX1
    woeusb --partition /dev/sr0 /dev/sdX1
    ```

    Command-line Options
    --------------------

    ### `--verbose`, `-v` ###

    Verbose mode

    ### `--help`, `-h` ###

    Show this help message and exit

    ### `--version`, `-V` ###

    Print application version

    ### `--about`, `-ab` ###

    Show info about this application

    ### `--no-color` ###

    Disable message coloring

    ### `--debug` ###

    Enable script debugging

    ### `--label`, `-l <filesystem_label>` ###

    Specify label for the newly created file system in --device creation method

    Note that the label is not verified for validity and may be illegal for the filesystem

    ### `--workaround-bios-boot-flag` ###

    Workaround BIOS bug that won't include the device in boot menu if non of the partition's boot flag is toggled

    ### `--debugging-internal-function-call <function name> (function_argument)...` ###

    Development option for developers to test certain function without running the entire build\n

    ### `--target-filesystem`, `--tgt-fs <filesystem name>` ###

    Specify the filesystem to use as the target partition's filesystem.

    Currently supported: FAT(default)/NTFS

    ### `--for-gui` ###

    No longer supported, reserved for compatibility with the wrapper programs

## [Removal]

### [Unmerge]

Uninstall [[[sys-boot/woeusb]](https://packages.gentoo.org/packages/sys-boot/woeusb)[]]:

`root `[`#`]`emerge --ask --depclean --verbose sys-boot/woeusb`

## [See also]

-   [dd](https://wiki.gentoo.org/wiki/Dd "Dd") --- a utility used to copy raw data from a source into sink, where source and sink can be a block device, file, or piped input/output.

## [External resources]

-   [woeusb-ng GURU ebuild](https://gitweb.gentoo.org/repo/proj/guru.git/tree/sys-boot/woeusb-ng) the Python-based rewrite of the original [woeusb].
-   [Microsoft Windows 10 Installation Media](https://www.microsoft.com/en-us/software-download/windows10ISO)
-   [Microsoft Windows 11 Installation Media](https://www.microsoft.com/software-download/windows11)