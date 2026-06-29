** See also**\
For those looking to learn how to use Catalyst to build LiveCDs should check the [Custom media image](https://wiki.gentoo.org/wiki/Custom_media_image "Custom media image") article.

This article explains how to create a *Gentoo LiveUSB* or, in other words, how to emulate a **[x86]** or **[amd64]** Gentoo LiveCD using a USB drive. This is particularly useful for installing Gentoo on a modern laptop with no CD-ROM drive.

Although the instructions found in this document aim at emulating a Gentoo LiveCD using a USB drive, they should work for any arbitrary block device as long as the device names are adjusted accordingly.

Many other methods available on different operating systems should work for creating bootable LiveUSB drives for Gentoo installation.

** Note**\
This article covers creation of a simple bootable drive, from an image file, that can be useful for installing Gentoo to a hard drive, for example. For instructions on installation of a complete, functional, Gentoo system onto a USB drive, see the [Install Gentoo on a bootable USB stick](https://wiki.gentoo.org/wiki/Install_Gentoo_on_a_bootable_USB_stick "Install Gentoo on a bootable USB stick") article.

## Contents

-   [[1] [Prerequisites]](#Prerequisites)
    -   [[1.1] [Choosing an installation media for Gentoo]](#Choosing_an_installation_media_for_Gentoo)
    -   [[1.2] [Convert the ISO image to hybrid mode]](#Convert_the_ISO_image_to_hybrid_mode)
-   [[2] [Using dd to write the ISO image to a USB drive]](#Using_dd_to_write_the_ISO_image_to_a_USB_drive)
-   [[3] [Creating bootable LiveUSB drives from Linux systems]](#Creating_bootable_LiveUSB_drives_from_Linux_systems)
    -   [[3.1] [Manually preparing a LiveUSB drive]](#Manually_preparing_a_LiveUSB_drive)
        -   [[3.1.1] [Preparing the USB drive]](#Preparing_the_USB_drive)
            -   [[3.1.1.1] [Partitioning the drive]](#Partitioning_the_drive)
            -   [[3.1.1.2] [Creating the filesystem]](#Creating_the_filesystem)
        -   [[3.1.2] [Copying the files]](#Copying_the_files)
            -   [[3.1.2.1] [Mounting the Gentoo boot image]](#Mounting_the_Gentoo_boot_image)
            -   [[3.1.2.2] [Mounting the LiveUSB]](#Mounting_the_LiveUSB)
            -   [[3.1.2.3] [Copying the files]](#Copying_the_files_2)
            -   [[3.1.2.4] [Modify the bootloader configuration]](#Modify_the_bootloader_configuration)
        -   [[3.1.3] [Installing a bootloader]](#Installing_a_bootloader)
            -   [[3.1.3.1] [Installing GRUB]](#Installing_GRUB)
            -   [[3.1.3.2] [Unmounting the drive]](#Unmounting_the_drive)
-   [[4] [Creating bootable LiveUSB drives under Windows]](#Creating_bootable_LiveUSB_drives_under_Windows)
    -   [[4.1] [Rufus]](#Rufus)
    -   [[4.2] [Universal USB Installer]](#Universal_USB_Installer)
-   [[5] [Booting]](#Booting)
-   [[6] [See also]](#See_also)
-   [[7] [External resources]](#External_resources)
-   [[8] [References]](#References)

## [Prerequisites]

In order to boot a LiveUSB, the following will be needed:

-   Bootable USB drive with enough space to write the image to. When using the Gentoo Minimal Installation CD, at least 1GB.
-   A computer which supports booting from USB. While common now, some early systems with USB did not.

Access to the following is needed for creating a LiveUSB:

-   A computer able to run the [[dd](https://wiki.gentoo.org/wiki/Dd "Dd")] command, which includes Linux and macOS
-   A computer running Microsoft Windows with the appropriate software (see the [Windows section](https://wiki.gentoo.org/wiki/LiveUSB#Creating_bootable_LiveUSB_drives_under_Windows "LiveUSB") below)

### [Choosing an installation media for Gentoo]

The architecture appropriate [Gentoo Minimal Installation CD](https://www.gentoo.org/downloads/) iso can be downloaded and used to install from a [command line interface](https://wiki.gentoo.org/wiki/Terminal_emulator "Terminal emulator"), as a \"light\" installation option. There is also a [Gentoo LiveGUI USB Image](https://www.gentoo.org/downloads/) which can provide a more ergonomic option (e.g. open the handbook in another window and copy paste commands with a middle mouse click to a terminal emulator, use a GUI [IRC](https://wiki.gentoo.org/wiki/IRC "IRC") client for [support](https://wiki.gentoo.org/wiki/Support "Support"), etc.).

When downloading, adjust the architecture (**[x86]**, **[amd64]**, **[arm]**, **[sparc]**, etc.) portion of the URL to match the system\'s CPU. Gentoo mirrors are [here](https://www.gentoo.org/downloads/mirrors/).

The Gentoo bootable images are by no means the only thing that can be used to install Gentoo - almost any modern LiveCD should work. Use whatever feels the most comfortable.

** Note**\
Gentoo Minimal Installation CD images support *both* UEFI and legacy boot.

### [Convert the ISO image to hybrid mode]

Most modern LiveCD\'s, like Gentoo are already in hybrid mode. If the LiveUSB does not boot, then it may be that the image will have to be converted to hybrid mode. Hybrid mode means image will enable the ISO to boot from both a CD-ROM device *or* a USB drive.

Convert the ISO with the following command:

`root `[`#`]`isohybrid filename.iso`

The [isohybrid] command comes as part of the [[[sys-boot/syslinux]](https://packages.gentoo.org/packages/sys-boot/syslinux)[]] package.

## [Using dd to write the ISO image to a USB drive]

** Warning**\
The [dd] command *will* **wipe all data** from the destination drive. Always **[backup](https://wiki.gentoo.org/wiki/Backup "Backup") all important data**.

When using the Gentoo Installation CD ISOs, it is sufficient to directly copy the ISO contents onto the USB device. The [[dd](https://wiki.gentoo.org/wiki/Dd "Dd")] command can be used to accomplish this. For instance, assuming the USB device is at [/dev/sdc]:

`root `[`#`]`dd if=/path/to/image.iso of=/dev/sdc bs=8192k status=progress; sync`

The command will exit without any errors when it completes the transfer successfully. Depending on the size of the ISO image and the speed of the USB device, this process could take some time. Be patient!

Once complete, the USB drive should be bootable.

On Windows, the [dd] command is also available through various projects, such as [Cygwin](https://www.cygwin.com), [GNUWin32](http://gnuwin32.sourceforge.net/), or [Chrysocome](http://www.chrysocome.net/dd).

The remainder of this document explains how to setup a vfat partition that is writable using the [GRUB](https://wiki.gentoo.org/wiki/GRUB "GRUB") bootloader.

## [Creating bootable LiveUSB drives from Linux systems]

### [Manually preparing a LiveUSB drive]

[] The information in this section is probably **outdated**. You can help the Gentoo community by verifying and [updating this section](https://wiki.gentoo.org/index.php?title=LiveUSB&action=edit).

This method works at least with current Gentoo [GRUB](https://wiki.gentoo.org/wiki/GRUB "GRUB")-based images.

#### [Preparing the USB drive]

##### [Partitioning the drive]

** Warning**\
These instructions *will* **erase all data** from the USB drive. Make sure to [backup](https://wiki.gentoo.org/wiki/Backup "Backup") any pre-existing data first.

** Important**\
This article assumes that the [/dev/sdc] device node corresponds to the USB drive. If other SCSI-like devices exist **be sure to use the correct device node** to prevent data loss!

Create a MBR partition table with a FAT16 partition on the USB drive, and mark it bootable using [fdisk]. In a combined approach, this is fine for booting BIOS and UEFI machines. An example partitioning scheme can be seen below:

** Note**\
If the USB drive is 4GB or larger, use partition type `b` (W95 FAT32).

`root `[`#`]`fdisk -l /dev/sdc`

    Disk /dev/sdc: 2063 MB, 2063597056 bytes
    255 heads, 63 sectors/track, 250 cylinders
    Units = cylinders of 16065 * 512 = 8225280 bytes

       Device Boot      Start         End      Blocks   Id  System
    /dev/sdc1   *           1         250     2008124+   6  FAT16

A Gentoo LiveGUI image doesn\'t need more than 5GB. On a larger drive, a second partition could be created for the remaining space, and formatted when needed later.

`root `[`#`]`fdisk -l /dev/sdc`

    Disk /dev/sdc: 14.92 GiB, 16025387008 bytes, 31299584 sectors
    Disk model: USB Flash Disk
    Units: sectors of 1 * 512 = 512 bytes
    Sector size (logical/physical): 512 bytes / 512 bytes
    I/O size (minimum/optimal): 512 bytes / 512 bytes
    Disklabel type: dos

    Device     Boot   Start      End  Sectors  Size Id Type
    /dev/sdc1  *       2048 10487807 10485760    5G  b W95 FAT32
    /dev/sdc2      10487808 31299583 20811776  9.9G 83 Linux

##### [Creating the filesystem]

Create a FAT16 filesystem on the USB drive using [mkfs.fat]:

** Note**\
If the drive is 4GB or larger, use `-F 32` to create a FAT32 filesystem.

`root `[`#`]`emerge --ask sys-fs/dosfstools`

`root `[`#`]`mkfs.fat -n LiveUSB -F 16 /dev/sdc1`

    mkfs.fat 3.0.22 (2013-07-19)

GRUB will use \"LiveUSB\" as root label.

#### [Copying the files]

##### [Mounting the Gentoo boot image]

Download a Gentoo boot image for the system\'s architecture from a the main site\'s [download page](https://www.gentoo.org/downloads/) and mount the ISO image on [/mnt/cdrom] as shown below:

`root `[`#`]`mkdir -p /mnt/cdrom `

`root `[`#`]`mount -o loop,ro -t iso9660 /path/to/isofile.iso /mnt/cdrom `

Adjust the `/path/to/isofile.iso` as necessary to the location of the downloaded boot image ISO.

** Note**\
If a \"*Could not find any loop device*\" error message is displayed when mounting the ISO, a kernel recompile may be required. Verify the `Loopback device support` option in the kernel configuration has been enabled. For more information on kernel configuration see the [kernel configuration article](https://wiki.gentoo.org/wiki/Kernel/Configuration "Kernel/Configuration").

##### [Mounting the LiveUSB]

Mount the newly formatted USB drive on [/mnt/usb] as shown below:

`root `[`#`]`mkdir -p /mnt/usb `

`root `[`#`]`mount -t vfat /dev/sdc1 /mnt/usb `

##### [Copying the files]

Copy the files from the boot image to the LiveUSB:

`root `[`#`]`cp -r /mnt/cdrom/* /mnt/usb `

Unmount the ISO image:

`root `[`#`]`umount /mnt/cdrom`

##### [Modify the bootloader configuration]

Change all root labels to \"LiveUSB\", so the partition can be found (4x in this example).

[FILE] **`/mnt/usb/boot/grub/grub.cfg`**

    set default=0
    set gfxpayload=keep
    set timeout=10
    insmod all_video

    menuentry 'Boot LiveCD (kernel: gentoo)' --class gnu-linux --class os

    menuentry 'Boot LiveCD (kernel: gentoo) (cached)' --class gnu-linux --class os

    ...

#### [Installing a bootloader]

##### [Installing GRUB]

Finally install the [grub] bootloader on the USB drive. Pick one or more targets supported by the image.

64 bit UEFI:

`root `[`#`]`grub-install --force --removable --no-floppy --target=x86_64-efi --boot-directory=/mnt/usb/boot --efi-directory=/mnt/usb/efi`

32 bit UEFI:

`root `[`#`]`grub-install --force --removable --no-floppy --target=i386-efi --boot-directory=/mnt/usb/boot --efi-directory=/mnt/usb/efi`

BIOS:

`root `[`#`]`grub-install --force --no-floppy --target=i386-pc --boot-directory=/mnt/usb/boot /dev/sdc`

##### [Unmounting the drive]

`root `[`#`]`umount /mnt/usb`

## [Creating bootable LiveUSB drives under Windows]

### [Rufus]

Rufus is a free and open source project created to write images to USB drives, with a variety of operating systems. It tends to be faster than the Universal USB installer (see in the next section).

Rufus can be downloaded from the project\'s [homepage](https://rufus.ie/en/).

Rufus is easy to use and should be mostly self explanatory. For more information, see Rufus\' [FAQ page](https://github.com/pbatard/rufus/wiki/FAQ).

** Warning**\
On UEFI systems, one must select \"dd mode\" when using Rufus, otherwise GRUB fails with \"unknown filesystem\". The option for \"dd mode\" is presented after clicking \"START\" and is NOT the default

### [Universal USB Installer]

Universal USB installer is one of the oldest Linux-capable LiveUSB creators for Windows systems. It supports most Linux distributions, and has a simple, helpful wizard for selecting the Linux distribution. For Gentoo Minimal Installation CDs, however, select the [Try Unlisted Linux ISO] which is at the very bottom of the list. Select the proper USB drive to format and extract Linux to, and click [Create].

Universal USB installer can be downloaded from its [homepage](https://www.pendrivelinux.com/universal-usb-installer-easy-as-1-2-3/).

## [Booting]

Insert the USB drive and turn on the computer, make sure the BIOS (or EFI firmware) has been set to boot from USB. If all goes well, a standard syslinux prompt should appear on the screen.

When attempting to boot from a USB device, be sure to select or enable USB drives as bootable devices in the system\'s firmware interface. If the ISO is UEFI capable, it may be also necessary to enable booting UEFI devices. This is typically performed via toggle options in the [BIOS](https://wiki.gentoo.org/wiki/BIOS "BIOS") or UEFI firmware interface.

The boot order may need to be adjusted in the system\'s firmware for USB devices to boot first, although it is usually easier to hit the appropriate key (commonly either [F2] or [Delete]) and manually select the USB device as a one-time boot option from the list of bootable devices.

If installing Gentoo, follow the installation instructions found in the [Gentoo Handbook](https://wiki.gentoo.org/wiki/Handbook:Main_Page "Handbook:Main Page") appropriate to the system\'s architecture from here on.

## [See also]

-   [Live image](https://wiki.gentoo.org/wiki/Live_image "Live image") --- an operating system (OS) environment contained within a file that can be used to [boot](https://en.wikipedia.org/wiki/Booting "wikipedia:Booting") a system
-   [CD/DVD/BD writing](https://wiki.gentoo.org/wiki/CD/DVD/BD_writing "CD/DVD/BD writing") --- how to **burn optical disks** on Gentoo from the [command line](https://wiki.gentoo.org/wiki/Terminal_emulator "Terminal emulator") with the [[[app-cdr/cdrtools]](https://packages.gentoo.org/packages/app-cdr/cdrtools)[]] or [[[app-cdr/dvd+rw-tools]](https://packages.gentoo.org/packages/app-cdr/dvd+rw-tools)[]] packages
-   [FAQ - How do I burn an ISO file?](https://wiki.gentoo.org/wiki/FAQ#How_do_I_burn_an_ISO_file.3F "FAQ")

## [External resources]

-   [Installing SystemRescueCd on a USB stick](https://www.system-rescue.org/Installing-SystemRescue-on-a-USB-memory-stick/#recommended-usb-installation-method-on-linux) --- The very popular alternative
-   [https://www.ventoy.net/](https://www.ventoy.net/) - Ventoy provides a simple means to create and modify bootable media. One disk may be used to provide multiple boot iso options. Beware that there seem to be a large number of open bugs - [[[bug #736936]](https://bugs.gentoo.org/show_bug.cgi?id=736936)[]].

## [References]

\

Authorship information[]

This page is based on a document formerly found on [gentoo.org](https://www.gentoo.org/).\
The following people contributed to the original document: **brix, neysx**\
\
*[Editors: please do **not** add yourself here. Contributions are recorded on each article\'s associated history page, this list is only present to preserve authorship information, as wiki history does not allow for any external attribution.]*