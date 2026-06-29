\
Apple\'s early 2011 13\" MacBook Pro (model code 8,1) is capable of installing and running Gentoo Linux. Installation and configuration is decently easy using [Sakaki\'s EFI Install Guide](https://wiki.gentoo.org/wiki/User:Sakaki/Sakaki%27s_EFI_Install_Guide "User:Sakaki/Sakaki's EFI Install Guide")!

## Contents

-   [[1] [WIFI during Gentoo install]](#WIFI_during_Gentoo_install)
-   [[2] [Kernel Config]](#Kernel_Config)
-   [[3] [Disk Partitionin/Formatting/Layout for Triple Boot (OSX/WIN10/GENTOO)]](#Disk_Partitionin.2FFormatting.2FLayout_for_Triple_Boot_.28OSX.2FWIN10.2FGENTOO.29)
-   [[4] [Restore Win10 Boot option]](#Restore_Win10_Boot_option)
-   [[5] [External resources]](#External_resources)

### [WIFI during Gentoo install]

Booting from the Gentoo-LiveDVD (image on USB stick) the wifi connection can easily established using graphical tools. Installing Gentoo via SSH is untested.

In [Chapter 10](https://wiki.gentoo.org/wiki/User:Sakaki/Sakaki%27s_EFI_Install_Guide/Configuring_systemd_and_Installing_Necessary_Tools "User:Sakaki/Sakaki's EFI Install Guide/Configuring systemd and Installing Necessary Tools") re-establishing a wifi connection was unsuccessful, but using a wired connection should not be any problem. After the installation of Gnome the wifi connection can easily be established using graphical tools. Hence, using a wired connection during this step is recommended.

### [Kernel Config]

Appropriate kernel configuration [can be found here](https://wiki.gentoo.org/wiki/Apple_Macbook_Pro_Retina "Apple Macbook Pro Retina").

If you plan to use the proprietary Broadcom-Sta driver the kernel configuration has to look like below. Ensure the following options are NOT set (required for proper Broadcom wireless): **Warning: Broadcom-Sta driver no longer maintained**

[KERNEL]

    Networking support  --->
      Wireless  --->
        < >   Generic IEEE 802.11 Networking Stack (mac80211)
    Device Drivers  --->
      Network device support  --->
        Wireless LAN  --->
          < >   Broadcom 43xx wireless support (mac80211 stack)
          < >   Broadcom IEEE802.11n embedded FullMAC WLAN driver
      Sonics Silicon Backplane  --->
        < > Sonics Silicon Backplane support
      Broadcom specific AMBA  --->
        < > BCMA support

### [][Disk Partitionin/Formatting/Layout for Triple Boot (OSX/WIN10/GENTOO)]

**This guide is for a complete reinstall of all operating systems on the machine. Do NOT use this if you want to keep your current OSX or Windows installation. ALL PREVIOUS DATA WILL BE LOST!**\
\
The easiest way to install Windows 10 on a Macbook Pro is Apple\'s Boot Camp Assistant. But it requires a disk, **without any other partition**, except for the one OS X is installed on. At the same time it uses **all** disk space from the beginning of the OS X partition to the end of the disk. Hence, the preliminary OSX partition, which will be split into the final OSX partition and the Win10 partition, has to be located at the very end of the disk.

Therefore, I recommend the following installation order:

-   OSX first
-   then Win10
-   Gentoo last

\
To create the preliminary OSX partition in the disk sectors, boot from a Linux USB stick (e.g. using the Gentoo-LiveDVD image), open a console and enter:

`livecd`[`~ $`]` sudo su `

`livecd `[`~ #`]`parted /dev/sdY `

    GNU Parted 3.2
    ... additional output suppressed ...
    (parted) mklabel gpt
    Warning: The existing disk label on /dev/sdY will be destroyed and all data on
    this disk will be lost. Do you want to continue?
    Yes/No? yes
    (parted) unit mib
    (parted) mkpart primary 1 1025
    (parted) name 1 'EFI System Partition'
    (parted) set 1 boot on
    (parted) set 1 esp on

** Note**\
Replace [/dev/sdY] in the above command with the path of hard disk, such as [/dev/sda]\
The size of 1 Gb for a EFI partition is huge (Apple\'s EFI partitions are about 200 Mb), so feel free to adjust the value as you like. More on this topic and a recommmodation for EFI partitions with at least 512MiB (537MB) [can be found here](http://www.rodsbooks.com/efi-bootloaders/principles.html).

In the following example, *b* is the very end of the disk (the \'last\' Mb), whereas *a* is *b* minus the desired size of the final OSX partition + Win10 partition (in Mb).

Example: If you have a total disk capacity of 500 Gb and want to use 200 Gb for OSX, 150 Gb for Win10 and the remaining space for Gentoo, then:

*b = 500000*\
*a = b - 350000*

since we set the units to Mb.

`livecd `[`~ #`]`(parted) mkpart primary a b `

`livecd `[`~ #`]`(parted) q `

`livecd `[`~ #`]`mkfs.vfat -F32 /dev/sdY1 `

Now reboot and

-   install OS X on the partition we just created (350 Gb in this example, OSX will install the EFI on the EFI partition automatically),
-   use Apple\'s Boot Camp Assistant to split this temporary OSX partition into the final OSX partition and the Windows partition and
-   install Windows10 on the partition created for Windows by the Boot Camp Assistant.

** Note**\
I used a Win10-DVD for the installation. I tried to make it work using an USB stick, but eventually I gave up and put my SuperDrive back in (which I had replaced by a second hard disk).

Now that OSX and Win10 boot successfully, use the Linux USB stick again to boot. once again open a console and enter:

`livecd`[`~ $`]` sudo su `

`livecd `[`~ #`]`parted /dev/sdY `

    GNU Parted 3.2
    ... additional output suppressed ...
    (parted) unit mib
    (parted) mkpart primary 1025 a
    (parted) q

** Note**\
*a* still is the same number as before. This would use all disk space that remains between the end of the EFI partition (1025) and the beginning of the OSX partition (*a*) for the Gentoo partition.

### [Restore Win10 Boot option]

In theory you could continue with the Gentoo installation as described by [Sakaki\'s EFI Install Guide](https://wiki.gentoo.org/wiki/User:Sakaki/Sakaki%27s_EFI_Install_Guide "User:Sakaki/Sakaki's EFI Install Guide"), but you will soon recognize that the Win10 partition does not show up as a selectable boot option anymore.

To be able to use Win10 again, we need to use *gdisk*:

`livecd `[`~ #`]`gdisk `

    GPT fdisk (gdisk) version 1.0.1

    Type device filename, or press <Enter> to exit: /dev/sdY

** Note**\
Replace [/dev/sdY] in the above command with the path of hard disk, such as [/dev/sda]

     Partition table scan:
     ... additional output suppressed ...

    Found valid GPT with hybrid MBR; using GPT.

    Command (? for help): r

    Recovery/transformation command (? for help): h

    WARNING! Hybrid MBRs are flaky and dangerous! If you decide not to use one,
    just hit the Enter key at the below prompt and your MBR partition table will
    be untouched.

    Type from one to three GPT partition numbers, separated by spaces, to be
    added to the hybrid MBR, in sequence: 5

    Place EFI GPT (0xEE) partition first in MBR (good for GRUB)? (Y/N): y

    Creating entry for GPT partition #5 (MBR partition #2)
    Enter an MBR hex code (default 07): <enter>
    Set the bootable flag? (Y/N): y

    Unused partition space(s) found. Use one to protect more partitions? (Y/N): n

    Recovery/transformation command (? for help): o

You should have two entries. One type EE, one 07, with the 07 entry marked with \* under Boot. If you don\'t, report back. If you do, write out the update partition information, and hope a power failure doesn\'t occur for the next few seconds\...

    Recovery/transformation command (? for help): w

reboot. hold down option key and you should be able to boot into either Mac HD, Recovery HD, or Windows.

## [External resources]

-   [https://support.apple.com/kb/SP619](https://support.apple.com/kb/SP619) - Apple\'s technical specifications page for this laptop.
-   [https://www.gentoo.org/downloads/](https://www.gentoo.org/downloads/) - Obtain a Minimal Installation CD from a Gentoo mirror.
-   [https://www.system-rescue.org/](https://www.system-rescue.org/) - A rescue CD that includes many helpful troubleshooting tools not included on Gentoo\'s Minimal Installation CDs.