Other languages:

-   [English]
-   [español](https://wiki.gentoo.org/wiki/LILO/es "LILO (86% translated)")
-   [magyar](https://wiki.gentoo.org/wiki/LILO/hu "LILO (93% translated)")
-   [русский](https://wiki.gentoo.org/wiki/LILO/ru "LILO (95% translated)")
-   [தமிழ்](https://wiki.gentoo.org/wiki/LILO/ta "LILO (71% translated)")
-   [中文（中国大陆）‎](https://wiki.gentoo.org/wiki/LILO/zh-cn "LILO (50% translated)")
-   [日本語](https://wiki.gentoo.org/wiki/LILO/ja "LILO (75% translated)")
-   [한국어](https://wiki.gentoo.org/wiki/LILO/ko "LILO (86% translated)")

\

**Resources**

[[]][Home](https://www.joonet.de/lilo/)

[[]][Package information](https://packages.gentoo.org/packages/sys-boot/lilo)

[[]][Wikipedia](https://en.wikipedia.org/wiki/LILO_(boot_loader) "wikipedia:LILO (boot loader)")

**LILO (LInux LOader)** is a simple boot loader to load Linux and other operating systems.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
    -   [[1.3] [Installing LILO on the MBR]](#Installing_LILO_on_the_MBR)
-   [[2] [Configuration]](#Configuration)
    -   [[2.1] [General configuration]](#General_configuration)
    -   [[2.2] [Configuring the Gentoo OS block]](#Configuring_the_Gentoo_OS_block)
    -   [[2.3] [Adding kernel parameters]](#Adding_kernel_parameters)
    -   [[2.4] [Multiple block definitions]](#Multiple_block_definitions)
-   [[3] [Usage]](#Usage)
    -   [[3.1] [Updating LILO in the MBR]](#Updating_LILO_in_the_MBR)
        -   [[3.1.1] [Dual boot Gentoo and FreeBSD]](#Dual_boot_Gentoo_and_FreeBSD)
-   [[4] [Removal]](#Removal)
    -   [[4.1] [Unmerge]](#Unmerge)
-   [[5] [See also]](#See_also)

## [Installation]

LILO\'s installation is two-fold. One is the installation of the software itself on the system (but does not activate LILO), the second one is the installation (activation) of the LILO bootloader on the disk\'s MBR.

### [USE flags]

### [USE flags for] [sys-boot/lilo](https://packages.gentoo.org/packages/sys-boot/lilo) [[]] [LInux LOader, the original Linux bootloader]

  ----------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------
  [`device-mapper`](https://packages.gentoo.org/useflags/device-mapper)   Enable support for device-mapper from sys-fs/lvm2
  [`keytab`](https://packages.gentoo.org/useflags/keytab)                 Install keytab, keyboard remapping helper script
  [`minimal`](https://packages.gentoo.org/useflags/minimal)               Do not install optional bits (dolilo helper, docs, etc.)
  [`pxeserial`](https://packages.gentoo.org/useflags/pxeserial)           Avoid character echo on PXE serial console
  [`static`](https://packages.gentoo.org/useflags/static)                 !!do not set this during bootstrap!! Causes binaries to be statically linked instead of dynamically
  ----------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2025-11-30 18:53] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

The software installation will only deploy the software on the file system, but will not install LILO in the MBR.

`root `[`#`]`emerge --ask sys-boot/lilo`

### [Installing LILO on the MBR]

In order to install LILO on the MBR or update LILO, invoke [lilo]. However, before doing that, the [/etc/lilo.conf] file must be set up, which is covered in the [Configuration](https://wiki.gentoo.org/wiki/LILO#Configuration "LILO") section below.

`root `[`#`]`lilo`

## [[] Configuration]

An example [lilo.conf] file is provided at [/etc/lilo.conf.example]. To start configuring LILO, copy over the example file.

`root `[`#`]`cp /etc/lilo.conf.example /etc/lilo.conf`

Update the [/etc/lilo.conf] file accordingly.

### [General configuration]

First configure LILO to be deployed on the system. The `boot` parameter tells LILO where to install the LILO bootloader in. Usually, this is the block device that represents the first disk (the disk that the system will boot), such as [/dev/sda]. Be aware that the [lilo.conf.example] file still uses [/dev/hda] so make sure that references to [/dev/hda] are changed to [/dev/sda].

[FILE] **`/etc/lilo.conf`Defining where to install LILO in**

    boot=/dev/sda
    map=/boot/.map

Next, tell LILO what to boot as default (if the user does not select any other option at the boot menu). The name used here is the `label` value of the operating system blocks defined later in the file.

[FILE] **`/etc/lilo.conf`Booting the block labeled as Gentoo by default**

    default=Gentoo

LILO will show the available options for a short while before continuing to boot the default selected operating system. How long it waits is defined by the `timeout` parameter and is measured in tenths of a second (so the value 10 is one second):

[FILE] **`/etc/lilo.conf`Setting a 5 second timeout before continuing to boot the default OS**

    timeout=50

In case of slow loading time, one could use `compact` which will reduce the read operation of the sector from each individual sector into sector and its adjacent sectors. That will boost the booting time in slow machine. But caveat is that the file should be in contiguous sectors to have the effect. Partially continuous sectors are fine but if they are nowhere close to each other, the number of read operation would still stay the same. Hence, no effect.

[FILE] **`/etc/lilo.conf`Reduce the read operation for contiguous sectors**

    compact

### [Configuring the Gentoo OS block]

An example configuration block for Gentoo is shown below. It is given the \"Gentoo\" label to match the `default` parameter declared earlier.

[FILE] **`/etc/lilo.conf`Example Gentoo Linux configuration in lilo.conf**

    image=/boot/kernel-3.11.2-gentoo
        label=Gentoo
        read-only
        root=/dev/sda4

This will boot the Linux kernel [/boot/kernel-3.11.2-gentoo] with root file system [/dev/sda4].

** Warning**\
Use [UUID] of root instead of path if intended to use with [initramfs](https://wiki.gentoo.org/wiki/Initramfs "Initramfs") (especially with [dracut](https://wiki.gentoo.org/wiki/Dracut "Dracut")) as it might fail to recognize the root directory from translated code by [lilo].

\

### [Adding kernel parameters]

To add additional kernel parameters to the OS block, use the `append` parameter. For instance, to boot the Linux kernel silently (so it does not show any kernel messages unless critical):

[FILE] **`/etc/lilo.conf`Showing the use of the append parameter with the quiet option**

    image=/boot/kernel-3.11.2-gentoo
        label=Gentoo
        read-only
        root=/dev/sda4
        append="quiet"

[systemd](https://wiki.gentoo.org/wiki/Systemd "Systemd") users for instance would want to set `init=/usr/lib/systemd/systemd` so that the systemd init is used:

[FILE] **`/etc/lilo.conf`Using systemd with LILO**

      append="quiet init=/usr/lib/systemd/systemd"

As can be seen, additional kernel parameters are just appended to the same `append` parameter.

### [Multiple block definitions]

It is a good idea to keep old definitions available in case the new kernel doesn\'t boot successfully. This is accomplished by creating another block:

[FILE] **`/etc/lilo.conf`Defining a second OS block**

    image=/boot/kernel-3.9.2-gentoo
            root=/dev/sda4
            label=OldGentoo
            read-only

## [Usage]

### [Updating LILO in the MBR]

As mentioned earlier, [lilo] has to be executed in order to install LILO in the MBR. This step has to be repeated every time [/etc/lilo.conf] is modified or when the Linux kernel(s) that the [/etc/lilo.conf] file points to are updated!

`root `[`#`]`lilo`

Running [lilo] too much doesn\'t hurt.

#### [Dual boot Gentoo and FreeBSD]

To dual boot Gentoo and FreeBSD, edit [/etc/lilo.conf] as follows:

[FILE] **`/etc/lilo.conf`Dual boot: Gentoo and FreeBSD**

    large-memory
    lba32
    boot=/dev/sda
    install=menu
    map=/boot/map
    prompt
    default=Gentoo

    image=/boot/vmlinuz-2.6.26
        label="Gentoo"
        root=/dev/sda1
        append=""
        read-only
        optional

    other=/dev/sda3
        label="FreeBSD"

Make sure to adapt the example configuration file to match the setup used.

## [Removal]

### [Unmerge]

** Warning**\
Be sure there\'s another [bootloader](https://wiki.gentoo.org/wiki/Bootloader "Bootloader") installed and properly configured *before* uninstalling [lilo]! Failing to do so will most likely result in the system failing to bootstrap.

Uninstall lilo, simply:

`root `[`#`]`emerge --ask --depclean --verbose sys-boot/lilo`

## [See also]

-   [GRUB](https://wiki.gentoo.org/wiki/GRUB "GRUB") --- a multiboot secondary [bootloader](https://wiki.gentoo.org/wiki/Bootloader "Bootloader") capable of loading kernels from a variety of [filesystems](https://wiki.gentoo.org/wiki/Filesystem "Filesystem") on most system architectures.
-   [Forum](https://forums.gentoo.org/viewtopic-p-8639638.html?sid=318bb4687e49059e853cf8c08b8218c4) discussion about [initramfs] and [lilo]