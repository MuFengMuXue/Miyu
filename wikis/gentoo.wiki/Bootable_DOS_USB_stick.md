This page describes how to prepare a **bootable USB stick which loads DOS** using tools available in Gentoo.

Many firmware loading programs on PCs require a [DOS](https://en.wikipedia.org/wiki/DOS "wikipedia:DOS") environment to function. Moreover, most computers no longer have floppy drives, and many do not even have CD drives, so a USB bootable DOS environment may come in useful.

## Contents

-   [[1] [Preparing the disk]](#Preparing_the_disk)
    -   [[1.1] [Wiping]](#Wiping)
    -   [[1.2] [Partitioning]](#Partitioning)
    -   [[1.3] [Boot sector]](#Boot_sector)
    -   [[1.4] [Formatting]](#Formatting)
-   [[2] [Loading a DOS environment]](#Loading_a_DOS_environment)
    -   [[2.1] [Configuring DOSEMU]](#Configuring_DOSEMU)
    -   [[2.2] [Setting up DOS with DOSEMU]](#Setting_up_DOS_with_DOSEMU)
-   [[3] [Finishing up]](#Finishing_up)
    -   [[3.1] [Checking with QEMU]](#Checking_with_QEMU)
    -   [[3.2] [Loading firmware]](#Loading_firmware)
-   [[4] [Possible improvements]](#Possible_improvements)
-   [[5] [See also]](#See_also)

## [Preparing the disk]

### [Wiping]

It is advisable to wipe the USB stick before loading it with a new environment. If the USB stick is at [/dev/sdb], this can be done with:

`root `[`#`]`dd if=/dev/zero of=/dev/sdb bs=1M count=<COUNT>`

`<COUNT>` should be replaced with the size of the USB stick in [MiB](https://en.wikipedia.org/wiki/Mebibyte "wikipedia:Mebibyte") (can be found in [dmesg] when plugging in the stick).

** Warning**\
Double-check the device filename for the USB stick, and that the USB stick has no vital data! This operation has no safeguards to prevent destroying all data \-- on any block device.

### [Partitioning]

The stick must now be [partitioned](https://wiki.gentoo.org/wiki/Partition "Partition"). Most any partitioning tool can be used, such as [cfdisk]. In this article, it is assumed that the first partition is to be used for this application. This partition should be marked `bootable` and its type set to `FAT16`.

### [Boot sector]

Using [ms-sys] from the package [[[sys-block/ms-sys]](https://packages.gentoo.org/packages/sys-block/ms-sys)[]], prepare the boot sector on the USB stick with:

`root `[`#`]`ms-sys -s /dev/sdb`

This writes a public domain boot sector compatible with [DOSEMU](https://en.wikipedia.org/wiki/DOSEMU "wikipedia:DOSEMU") which is used below.

### [Formatting]

Finally, using [mkfs.fat] from the package [[[sys-fs/dosfstools]](https://packages.gentoo.org/packages/sys-fs/dosfstools)[]], format this partition as [FAT16](https://en.wikipedia.org/wiki/FAT16#FAT16 "wikipedia:FAT16") with:

`root `[`#`]`mkfs.fat -F16 /dev/sdb1`

** Note**\
The maximum file system size under FAT16 is 4 GiB. It should also possible to load a DOSEMU environment from FAT32, though this author has not tried it.

## [Loading a DOS environment]

Now, use DOSEMU to create a DOS environment in the USB stick. If DOSEMU is not already on the system, install [[[app-emulation/dosemu]](https://packages.gentoo.org/packages/app-emulation/dosemu)[]].

### [Configuring DOSEMU]

Add the previously prepared USB partition to the list of \"hdimages\" in the DOSEMU configuration file [\~/.dosemurc]:

[FILE] **`~/.dosemurc`**

    $_hdimage = "drives/* /tmp /dev/sdb1"

Make sure the USB stick is not already mounted, e.g. through any desktop environment file manager, as DOSEMU requires block-level access. This means that DOSEMU must be invoked as root, unless the permissions of the device file have been modified.

### [Setting up DOS with DOSEMU]

After starting DOSEMU, the disk should appear as `F:`. Start DOSEMU:

`root `[`#`]`dosemu`

Change to drive `Z:`, as some files are being copied from there:

`C:\>``Z:`

Make the USB partition a DOS boot disk:

`Z:\>``sys F:`

This should provide a working command-line environment for running the firmware software.

To have a more user-friendly and powerful DOS environment, it is helpful to copy over tools from DOSEMU into the disk:

`Z:\>``xcopy /S /N Z: F:`

In order to prevent problems with booting and conflicts between drivers and firmware software, it is recommended editing [config.sys] and [autoexec.bat] to be minimal. For example:

[FILE] **`F:\config.sys`**

    SWITCHES=/F
    DOS=UMB,HIGH
    dosdata=umb
    lastdrive=Z
    files=40
    stacks=0
    buffers=10

[FILE] **`F:\autoexec.bat`**

    @echo off
    path c:\bin;c:\gnu;c:\dosemu
    set HELPPATH=c:\help
    set TEMP=c:\tmp
    prompt $P$G

To edit these files within DOSEMU, use the tool [edit]. `File -> Open...` and go to drive `F:`:

`Z:\>``edit`

If editing from Linux, take care to make sure that the files retain their DOS-style `CR+LF` newlines.

** Note**\
The `path` statement in the [autoexec.bat] example above assumes that the BIOS sees the USB stick as a hard disk, such that the stick will be `C:` under DOS. If it is seen as a floppy, it will become `A:`.

Exit DOSEMU:

`Z:\>``exitemu`

## [Finishing up]

### [Checking with QEMU]

Check that the USB stick is bootable without actually rebooting the computer by using [QEMU](https://wiki.gentoo.org/wiki/QEMU "QEMU"):

`root `[`#`]`qemu -hda /dev/sdb1`

Keep in mind that this is no guarantee that the BIOS will boot the computer off the USB stick successfully, only a check that the preparations are correct.

### [Loading firmware]

If the kernel supports the FAT filesystem, just mount the USB stick normally, and copy over the necessary software. Otherwise, this can be done within DOSEMU, where `D:` is the user home directory. Place the firmware software in the home directory:

`C:\>``xcopy /S /N D:\FIRMWARE F:`

Here, *FIRMWARE* is the directory of the firmware software.

## [Possible improvements]

To have a bootable DOS partition as well as a bootable Linux partition (e.g. [SystemRescueCD](https://en.wikipedia.org/wiki/SystemRescueCD "wikipedia:SystemRescueCD")) on the same disk, a bootloader setup more sophisticated than [mbr-sys] is required. This can be done with [GRUB](https://wiki.gentoo.org/wiki/GRUB "GRUB"), as described in [another HOWTO](https://web.archive.org/web/20160318011319/http://linux.koolsolutions.com/2009/02/11/installing-linux-on-usb-part-6-create-a-dos-and-linux-bootable-usb-flash-drive/) (archived).

## [See also]

-   [Alternative method using FreeDOS image in SystemRescueCD](https://wiki.gentoo.org/wiki/BIOS_Update#Using_SystemRescueCD_to_boot_FreeDOS "BIOS Update")