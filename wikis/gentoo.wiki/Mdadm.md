[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=Mdadm&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

[[]][Package information](https://packages.gentoo.org/packages/sys-fs/mdadm)

[[]][Wikipedia](https://en.wikipedia.org/wiki/Mdadm "wikipedia:Mdadm")

[[]][GitHub](https://github.com/md-raid-utilities/mdadm)

**mdamd** is a tool for running software RAID in Linux systems.

## Contents

-   [[1] [Introduction to Software RAID]](#Introduction_to_Software_RAID)
    -   [[1.1] [Advantages of RAID]](#Advantages_of_RAID)
    -   [[1.2] [Disadvantages of RAID]](#Disadvantages_of_RAID)
-   [[2] [Setting up Software RAID]](#Setting_up_Software_RAID)
    -   [[2.1] [Installing the Tools]](#Installing_the_Tools)
    -   [[2.2] [Using Software RAID]](#Using_Software_RAID)
    -   [[2.3] [Software RAID for Root File System]](#Software_RAID_for_Root_File_System)
        -   [[2.3.1] [Boot Using GRUB and genkernel\'s initramfs]](#Boot_Using_GRUB_and_genkernel.27s_initramfs)
-   [[3] [Managing Software RAID]](#Managing_Software_RAID)
    -   [[3.1] [Adding Disks]](#Adding_Disks)
    -   [[3.2] [Removing Disks]](#Removing_Disks)
    -   [[3.3] [Changing RAID Layout]](#Changing_RAID_Layout)
-   [[4] [External Resources]](#External_Resources)

## [Introduction to Software RAID]

[Redundant Array of Inexpensive Disks (RAID)](https://en.wikipedia.org/wiki/RAID "wikipedia:RAID") is a technology to combine multiple disks in order to improve their reliability and/or performance. There is *hardware RAID*, implemented by the controller on your motherboard or specific extension cards, and there is *software RAID*, implemented by the kernel.

### [Advantages of RAID]

The main advantages of RAID are reliability and/or performance improvements.

There are vast differences between soft- and hardware RAID. Differences include: cost (monetarily), performance, overhead and flexibility. Of course software RAID comes cheapest. Another advantage of soft- over hardware RAID is that you can easily move you RAID set to another (Linux) computer. With hardware RAID you will depend on the vendor.

### [Disadvantages of RAID]

RAID usually takes more disk space than it delivers. E.g. a RAID-1 set of two 3TB disks delivers a 3TB RAID disk (a reduction of 50%).

The time it takes to synchronize you RAID disk (initially and when they need to rebuild).

The extra effort to manage and monitor your RAID disks. To make full use of software RAID, you need to learn about disk failures so you don\'t end up loosing two disks from your 3 disk RAID-5 just because you don\'t notice failure of the first one.

## [Setting up Software RAID]

** Note**\
Be aware that a reliable RAID does not remove the need for regular backups!

** Warning**\
If you work with existing data, be sure to make a backup before you even start with RAID, preferably on external storage!

### [Installing the Tools]

Start with the kernel configuration. After all, the kernel does most of the work:

[KERNEL]

    [*] Device Drivers  --->
        <*> Multiple devices driver support (RAID and LVM)
            <*> RAID support
                [*] Autodetect RAID arrays during kernel boot

                If you want to combine multiple disks or partitions to one (bigger) device:
                    <*> Linear (append) mode

                If you want to increase I/O performance by striping data across multiple disks (at the expense of reliability):
                    <*> RAID-0 (striping) mode

                If you want to increase reliability by mirroring data across multiple disks (at the expense of storage capacity):
                    <*> RAID-1 (mirroring) mode

                If you want to combine the previous two options (for whatever reason):
                    <*> RAID-10 (mirrored striping) mode

                If you want to combine 3 or more disks for reliability and performance:
                    <*> RAID-4/RAID-5/RAID-6 mode

Get the proper RAID admin tool:

`root `[`#`]`emerge --ask mdadm`

Make sure your RAID disks are started and stopped:

`root `[`#`]`rc-update add mdraid boot`

** Note**\
The kernel or udev (or both) may already have assembled your RAID arrays by the time [mdraid] runs, but it\'s good to add it anyway as a redundant mechanism to ensure the arrays start and to defer [fsck] running until the arrays are up (since [mdraid] declares it must run before [fsck]). If your [[/etc/fstab](https://wiki.gentoo.org/wiki//etc/fstab "/etc/fstab")] were to mention an array that wasn\'t assembled by the time `fsck` ran, you\'d see a possibly very alarming error message and it also may not get mounted automatically.

** Warning**\
Until [[[bug #948846]](https://bugs.gentoo.org/show_bug.cgi?id=948846)[]] is fixed, [udev](https://wiki.gentoo.org/wiki/Udev "Udev") will initialize devices and assemble RAID arrays in parallel with [mdraid]. If [/etc/mdadm.conf] contains `DEVICE` lines that refer to symlinks in [/dev/disk/], and udev has not yet setup those symlinks by the time [mdraid] runs, [mdraid] will fail, and that may result in a similar situation as [fsck] described above. A workaround is to add this line to [mdraid]\'s config to make it wait for the udev event queue to be fully processed before starting:

[FILE] **`/etc/conf.d/mdraid`**

    rc_need="udev-settle"

Note that this workaround may expose another (albeit harmless) [bug](https://github.com/md-raid-utilities/mdadm/issues/144) whereby [mdraid]\'s [mdadm] command will fail because the arrays have already been setup by udev.

### [Using Software RAID]

To create a simple mirrored disk (RAID-1), make sure you have two partitions that have the same size and bring them together in your first RAID-1 disk:

`root `[`#`]`mdadm --create /dev/md0 --level=1 --raid-devices=2 /dev/sdd1 /dev/sde1`

The disks in the mirror will now be synchronized (also when there is no data or file system yet). you can check the status like this:

`user `[`$`]`cat /proc/mdstat`

    Personalities : [raid1]
    md1 : active raid1 sde2[1] sdd2[0]
          1900953472 blocks super 1.2 [2/2] [UU]
          [======>..............]  resync = 31.6% (600768512/1900953472) finish=819.4min speed=26444K/sec

    md0 : active raid1 sde1[1] sdd1[0]
          52395904 blocks super 1.2 [2/2] [UU]

    unused devices: <none>

Create a filesystem of choice:

`root `[`#`]`mkfs.ext4 /dev/md0`

Start using the RAID!

### [Software RAID for Root File System]

#### [][Boot Using GRUB and genkernel\'s initramfs]

When the root file system is located on a software RAID, an initramfs is necessary for automatic assembly. [Genkernel](https://wiki.gentoo.org/wiki/Genkernel "Genkernel")\'s initramfs can be used for that purpose. Generate the initramfs with `--mdadm` option, or have `MDADM="yes"` in [/etc/genkernel.conf] before generation.

[FILE] **`/etc/genkernel.conf`**

    MDADM="yes"

Then, add the `domdadm` parameter to the kernel command line. The script in initramfs interprets this parameter, not the kernel itself. Also, be aware that the auto assembly takes into account the hostname, which will probably be set to `(none)` in the initramfs environment. Using [GRUB](https://wiki.gentoo.org/wiki/GRUB "GRUB"), the parameter can be added to [/etc/default/grub]:

[FILE] **`/etc/default/grub`**

    GRUB_CMDLINE_LINUX_DEFAULT="domdadm"

Remember to regenerate the [/boot/grub/grub.cfg] configuration file with the following command:

`root `[`#`]`grub-mkconfig -o /boot/grub/grub.cfg`

## [Managing Software RAID]

### [Adding Disks]

To add a new disk to the software RAID, issue this command:

`root `[`#`]`mdadm /dev/md0 --add /dev/sdd1`

If the RAID has healthy members, the new disk will be added as spare disk `(S)`.

### [Removing Disks]

First determine the disk to be removed.

`root `[`#`]`cat /proc/mdstat`

    md0 : active raid1 sdd1[1](F) sde1[0]
          32000 blocks [2/1] [U_]
          bitmap: 0/4 pages [0KB], 4KB chunk

As you can see, there sdd1 marked as failed `(F)` and RAID missing one of disks `[U_]`. To remove the failed drive execute following command:

`root `[`#`]`mdadm /dev/md0 --remove /dev/sdd1`

Physically replace the (sdd) disk or add blank space from another attached location.

Sometimes you may need to remove an healthy member. For this you need to mark drive as failed then remove it from the software RAID set. Perform this action all in one command:

`root `[`#`]`mdadm /dev/md0 --fail /dev/sdd1 --remove /dev/sdd1`

### [Changing RAID Layout]

In some cases it is necessary to change the RAID layout. An example case would be when adding disks to a RAID1 or converting a RAID1 to a RAID5.

## [External Resources]

-   The [Linux RAID kernel list](https://raid.wiki.kernel.org/index.php/Linux_Raid)