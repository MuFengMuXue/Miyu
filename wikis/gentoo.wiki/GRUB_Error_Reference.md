The objective of this article is to list problems and errors that may occur in certain situations when using the *[GRUB Legacy](https://wiki.gentoo.org/wiki/GRUB_Legacy "GRUB Legacy")* bootloader. All these solutions have been acquired through the cooperation of users on the Gentoo Forums.

## Contents

-   [[1] [Starting notes]](#Starting_notes)
    -   [[1.1] [Acknowledgements]](#Acknowledgements)
    -   [[1.2] [Disclaimer warning]](#Disclaimer_warning)
-   [[2] [GRUB loading, please wait\...]](#GRUB_loading.2C_please_wait...)
    -   [[2.1] [Situation]](#Situation)
    -   [[2.2] [Solution]](#Solution)
-   [[3] [GRUB Error 12]](#GRUB_Error_12)
    -   [[3.1] [Situation]](#Situation_2)
    -   [[3.2] [Solution]](#Solution_2)
-   [[4] [GRUB error 15]](#GRUB_error_15)
    -   [[4.1] [Situation]](#Situation_3)
    -   [[4.2] [Solution - Initial configuration]](#Solution_-_Initial_configuration)
    -   [[4.3] [Solution - Booting an entry]](#Solution_-_Booting_an_entry)
-   [[5] [GRUB error 17]](#GRUB_error_17)
    -   [[5.1] [Situation]](#Situation_4)
    -   [[5.2] [Solution]](#Solution_3)
-   [[6] [GRUB error 18]](#GRUB_error_18)
    -   [[6.1] [Situation]](#Situation_5)
    -   [[6.2] [Solution]](#Solution_4)
-   [[7] [GRUB GRUB GRUB GRUB GRUB \...]](#GRUB_GRUB_GRUB_GRUB_GRUB_...)
    -   [[7.1] [Situation]](#Situation_6)
    -   [[7.2] [Solution]](#Solution_5)
-   [[8] [Probing devices to guess BIOS drives. This may take a long time]](#Probing_devices_to_guess_BIOS_drives._This_may_take_a_long_time)
    -   [[8.1] [Situation]](#Situation_7)
    -   [[8.2] [Solution]](#Solution_6)
-   [[9] [When installing GRUB, it just hangs]](#When_installing_GRUB.2C_it_just_hangs)
    -   [[9.1] [Situation]](#Situation_8)
    -   [[9.2] [Solution]](#Solution_7)
-   [[10] [Uncompressing Linux\... Ok, booting the kernel]](#Uncompressing_Linux..._Ok.2C_booting_the_kernel)
    -   [[10.1] [Situation]](#Situation_9)
    -   [[10.2] [Solution]](#Solution_8)
-   [[11] [GRUB just shows a GRUB prompt]](#GRUB_just_shows_a_GRUB_prompt)
    -   [[11.1] [Situation]](#Situation_10)
    -   [[11.2] [Solution]](#Solution_9)
-   [[12] [Could not find device for /boot/boot: not found or not a block device]](#Could_not_find_device_for_.2Fboot.2Fboot:_not_found_or_not_a_block_device)
    -   [[12.1] [Situation]](#Situation_11)
    -   [[12.2] [Solution]](#Solution_10)
-   [[13] [The system reboots after hitting return at the GRUB menu]](#The_system_reboots_after_hitting_return_at_the_GRUB_menu)
    -   [[13.1] [Situation]](#Situation_12)
    -   [[13.2] [Solution]](#Solution_11)
-   [[14] [After hitting the Enter (Return) key at the GRUB menu, the screen blanks out]](#After_hitting_the_Enter_.28Return.29_key_at_the_GRUB_menu.2C_the_screen_blanks_out)
    -   [[14.1] [Situation]](#Situation_13)
    -   [[14.2] [Solution]](#Solution_12)
-   [[15] [Missing GRUB image]](#Missing_GRUB_image)
    -   [[15.1] [Situation]](#Situation_14)
    -   [[15.2] [Solution]](#Solution_13)
-   [[16] [Failing To boot Windows from a second hard drive]](#Failing_To_boot_Windows_from_a_second_hard_drive)
    -   [[16.1] [Situation]](#Situation_15)
    -   [[16.2] [Solution]](#Solution_14)
-   [[17] [GRUB segfaults when trying to install]](#GRUB_segfaults_when_trying_to_install)
    -   [[17.1] [Situation]](#Situation_16)
    -   [[17.2] [Solution]](#Solution_15)

## [Starting notes]

### [Acknowledgements]

Many thanks to [Earthwings](https://forums.gentoo.org/profile.php?mode=viewprofile&u=18420), [penetrode](https://forums.gentoo.org/profile.php?mode=viewprofile&u=39305), [loyaltonone](https://forums.gentoo.org/profile.php?mode=viewprofile&u=41638), [pilla](https://forums.gentoo.org/profile.php?mode=viewprofile&u=4980), [airhead](https://forums.gentoo.org/profile.php?mode=viewprofile&u=3139), [nephros](https://forums.gentoo.org/profile.php?mode=viewprofile&u=13816), [yamakawa](https://forums.gentoo.org/profile.php?mode=viewprofile&u=25859) and all the others for the suggestions on the original [thread](https://forums.gentoo.org/viewtopic.php?t=122656).

### [Disclaimer warning]

The examples provided are just examples. Be sure to change partition numbers and the like according to the specific systems specs. Follow the solutions provided by this document at the readers own risk.

## [][GRUB loading, please wait\...]

### [Situation]

    GRUB loading stage 1.5
    GRUB loading, please wait...

After this message, the system stops. If attempting to boot the system using a GRUB floppy, the problem disappears.

### [Solution]

According to [The_Bell](https://forums.gentoo.org/profile.php?mode=viewprofile&u=3134), changing the boot order in the [BIOS](https://wiki.gentoo.org/wiki/BIOS "BIOS") can solve the problem.

Tell the BIOS to not boot from the floppy first.

[\[1\]](https://phz.fi/2014/10/30/grub-loading-stage-1-5-grub-loading-please-wait/) took hard disks off the system one-by-one until found out the problem was caused by the SiI3512A SATA RAID-controller.

[penetrode](https://forums.gentoo.org/profile.php?mode=viewprofile&u=39305) wrote that this may also be due to bad CFLAGS settings. Although the current GRUB ebuild filters out`-fstack-protector`, it can\'t hurt to recompile GRUB with clean CFLAGS if nothing else helps.

`root `[`#`]`CFLAGS="-O2 -march=i686 -fomit-frame-pointer -pipe" emerge grub:0 --ask`

This problem appeared on a dell r320 server, caused by having serial and terminal options in [grub.conf], problem disappeared after removing those options.

[FILE] **`grub.conf`options to remove**

    #serial --unit=1 --speed=19200
    #terminal --timeout=10 serial

## [GRUB Error 12]

### [Situation]

    12 : Invalid device requested.

This error is returned if the device strings syntax is correct but other than that, an error occurred that isn\'t defined by any other error.

### [Solution]

When GRUB was installed in the boot record using the interactive commands, were the two lines below executed in the GRUB prompt?

`grub>``root (hd0,0) `

`grub>``setup (hd0) `

`(hd0,0)` must be replaced with the boot partition and `(hd0)` with the HDD that was chosen. Remember that `(hd0)` will install the bootloader in the Master Boot Record of the first hard disk, the primary master.

## [GRUB error 15]

### [Situation]

This error can occur in two different stages of the GRUB configuration, either during the initial configuration (installing GRUB in the master boot record) or after booting the system and attempting to launch Linux (or any other entry).

Initial configuration:

`grub>``root (hd0,0) `

     Filesystem type is xfs, partition type 0x83

`grub>``setup (hd0) `

     Checking if "/boot/grub/stage1" exists... no
     Checking if "/grub/stage1" exists... no

    Error 15: File not found

Booting an entry:

    Booting 'Gentoo Linux'

    root (hd0,0)
    Filesystem type is ext2fs, partition type 0x83
    kernel (hd0,0)/boot/kernel-2.4.20 root=/dev/sda3 vga=792

    Error 15: File not found
    Press any key to continue...

### [Solution - Initial configuration]

This error is returned if the specified file name cannot be found, but everything else (like the disk/partition info) is OK.

Frequently, the error notes a missing kernel image file. Make sure that the file it is referring to exists on the boot partition.

To find out the exact name of the kernel, boot from the installation cd, mount the root and (if applicable) boot partition. Next, chroot into the Gentoo system and do a listing of the available files to see what kernel images there are available:

`root `[`#`]`cd /boot `

`root `[`#`]`ls `

This will list all the kernels that there are on the boot partition. If the kernel is missing make sure to have compiled a kernel (using [genkernel] or manually):

`root `[`#`]`cd /usr/src/linux/ `

`root `[`#`]`make menuconfig `

`root `[`#`]`make `

And that it has been copied to the boot partition:

`root `[`#`]`cp /usr/src/linux/arch/i386/boot/bzImage /boot`

Verify that the name of the kernel is exactly the same as the one mentioned in the [grub.conf] file. Also make sure that the `kernel` line in the [grub.conf] file is referring to that partition (either explicitly or implicitly).

Another reported mistake is to have the BIOS ignore the disk on which the kernel or GRUB stages reside. Also, the partition on which GRUB stores its stages should not use a software RAID-5 (or other striping technology) configuration.

### [Solution - Booting an entry]

First, verify that the `root` and `setup` lines that were used are correct.

If it is certain they are valid, then there is the *possibility* of using a flawed GRUB version (0.93.20031222). Upgrade the Portage tree or mask this version of GRUB:

`root `[`#`]`echo "=sys-boot/grub-0.93.20031222" >> /etc/portage/package.mask`

`root `[`#`]`emerge --ask sys-boot/grub:0`

Another option is using the [grub-install] script as is recommended by the GRUB authors. The `--root-directory` option is needed if there is a separate boot partition, otherwise it should be left out.

`root `[`#`]`grub-install --root-directory=/boot /dev/sda`

When all this fails, the boot partition may be corrupt. Check the partition for errors:

`root `[`#`]`fsck -y /dev/sda1`

## [GRUB error 17]

### [Situation]

    root (hd0,0)
    filesystem type unknown partition type 0x7

    Error 17 : Cannot mount selected partition

### [Solution]

This error is returned if the partition requested exists, but the filesystem type cannot be recognized by GRUB.

Be sure to check the `root(x,y)` settings in [grub.conf].

Also, when trying to boot Windows, make sure that the [grub.conf] file has the `root (hdX,Y)` (or `rootnoverify (hdX,Y)` ) and `chainloader (hdX,Y)+1` in it.

## [GRUB error 18]

### [Situation]

    kernel (hd1,4)/bzImage root=/dev/sdb7

    Error 18: Selected cylinder exceeds max supported by BIOS

### [Solution]

This error is returned when a read is attempted at a linear block address beyond the end of the BIOS translated area. This generally happens if the disk is larger than the BIOS can handle (512 MB for (E)IDE disks on older machines or larger than 8 GB in general).

Try an update for the BIOS and/or move the boot partition to the front (or at least into the appropriate range).

## [GRUB GRUB GRUB GRUB GRUB \...]

### [Situation]

    GRUB GRUB GRUB GRUB GRUB GRUB GRUB GRUB GRUB GRUB GRUB GRUB GRUB GRUB GRUB
      GRUB GRUB GRUB GRUB GRUB GRUB GRUB GRUB GRUB GRUB GRUB GRUB GRUB GRUB GRUB
    ...

### [Solution]

According to [airhead](https://forums.gentoo.org/profile.php?mode=viewprofile&u=3139) this can be caused by having the BIOS detect the disks automatically. Try to set the BIOS entry to User Type HDD.

Another possibility is that Grub was installed on the MBR and then reinstalled (for instance due to hard disk changes) but using the wrong `setup` and `root` commands.

## [Probing devices to guess BIOS drives. This may take a long time]

### [Situation]

While trying to install GRUB, it hangs after displaying the following line:

`root `[`#`]`grub `

    Probing devices to guess BIOS drives. This may take a long time.

### [Solution]

One reported cause was an exotic configuration of disk devices, like ultra/non-ultra DMA disks on one cable.

## [][When installing GRUB, it just hangs]

### [Situation]

When installing GRUB, it hangs:

`root `[`#`]`grub`

At this stage, the installation stops.

### [Solution]

If there is no floppy drive, was the `--no-floppy` switch used?

`root `[`#`]`grub --no-floppy`

## [][Uncompressing Linux\... Ok, booting the kernel]

### [Situation]

The system hangs after displaying the following line:

    Uncompressing Linux... Ok, booting the kernel.

### [Solution]

Strictly speaking, this is no GRUB error. One possible cause is that ACPI is not working correctly but is enabled in the kernel. Try to disable it in the BIOS or in the kernel. Another possible cause is that the kernel has been compressed to a format it does not support for decompression, such as LZO requiring LZO_DECOMPRESS.

## [GRUB just shows a GRUB prompt]

### [Situation]

When booting the system, a GRUB prompt appears instead of a list of entries that were defined in the [grub.conf] file.

### [Solution]

Mount the boot partition and verify if the [grub/grub.conf] file exists.

`root `[`#`]`mount /dev/sda1 /mnt/gentoo/boot `

`root `[`#`]`cat /mnt/gentoo/boot/grub/grub.conf `

Also make sure that the [menu.lst] symbolic link exists:

`root `[`#`]`ls -l /mnt/gentoo/boot/grub/menu.lst `

    lrwxrwxrwx  1 root root 9 Mar  7 14:00 /mnt/gentoo/boot/grub/menu.lst -> grub.conf

If not, recreate the symbolic link:

`root `[`#`]`cd /mnt/gentoo/boot/grub `

`root `[`#`]`ln -snf grub.conf menu.lst `

If this is the case, reinstall GRUB:

`(chroot) #``grub-install --root-directory=/boot /dev/sda `

## [][Could not find device for /boot/boot: not found or not a block device]

### [Situation]

When running [grub-install] during the GRUB installation, the following error appears:

`root `[`#`]`grub-install --root-directory=/boot /dev/sda `

    Could not find device for /boot/boot: not found or not a block device

### [Solution]

Check that the following wasn\'t forgotten:

`root `[`#`]`grep -v rootfs /proc/mounts > /etc/mtab`

## [The system reboots after hitting return at the GRUB menu]

### [Situation]

After hitting the [Enter] ([Return]) key at the GRUB menu during the system boot, the system reboots.

### [Solution]

Try disabling framebuffer support in the kernel. If this does not help, disable APM and ACPI.

## [][After hitting the Enter (Return) key at the GRUB menu, the screen blanks out]

### [Situation]

After hitting [Enter] ([Return]) at the GRUB menu during system boot, the screen blanks out, but the system is responsive (for instance, the numlock LED is switchable).

### [Solution]

Turn off framebuffer (typically remove `vga=XYZ` from [grub.conf]) and check the processor architecture in the kernel config.

## [Missing GRUB image]

### [Situation]

When booting the system, the spiffy Gentoo splash screen is not seen.

### [Solution]

First of all check if the splash screen file that is being are referred to in [grub.conf] really exists. If that is the case, go and check the GRUB ebuild. Maybe the patch for the splash image is commented out in the version that is being used.

## [Failing To boot Windows from a second hard drive]

### [Situation]

After selecting the Windows entry, the system refuses to boot without any clear reason as to why.

### [Solution]

[cyrillic](https://forums.gentoo.org/profile.php?mode=viewprofile&u=14595) provides information that it is possible to \"map\" the disks in a different order by changing [grub.conf]\'s Windows entry like so:

[FILE] **`grub.conf`Mapping disks**

    title Windows XP
      map (hd0) (hd1)
      map (hd1) (hd0)
      chainloader (hd1,0)+1

## [GRUB segfaults when trying to install]

### [Situation]

The situation described below is only relevant for grub-0.95.x at the moment of installing GRUB at the boot sector.

`grub>``root (hd0,0) `

`grub>``setup (hd0) `

    Segmentation fault

### [Solution]

This is a known bug related to this problem and has been fixed in grub-0.96. It is also known that grub-0.94-r1 and grub-0.94-r2 should work correctly. If that fails too, try to emerge grub-static which is currently stable on **[amd64]** and unstable on **[x86]** and (**[\~x86]**). Check out [[[bug #79378]](https://bugs.gentoo.org/show_bug.cgi?id=79378)[]] for additional information.

\

Authorship information[]

This page is based on a document formerly found on [gentoo.org](https://www.gentoo.org/).\
The following people contributed to the original document: **Hartwig Brandl, Ioannis Aslanidis**\
\
*[Editors: please do **not** add yourself here. Contributions are recorded on each article\'s associated history page, this list is only present to preserve authorship information, as wiki history does not allow for any external attribution.]*