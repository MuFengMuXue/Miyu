[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=Hybrid_partition_table&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

Most x86 and x86_64 systems only use either the [MBR](https://en.wikipedia.org/wiki/Master_boot_record "wikipedia:Master boot record") (MS-DOS based) partition table layout, or the [GPT](https://en.wikipedia.org/wiki/GUID_Partition_Table "wikipedia:GUID Partition Table") (GUID Partition Table) layout. However, in certain situations it might be necessary for a GPT partition layout to have an \"MBR view\" overlayed. This is called **Hybrid MBR/GPT**.

## Contents

-   [[1] [Using hybrid partition table]](#Using_hybrid_partition_table)
    -   [[1.1] [Creating with gdisk]](#Creating_with_gdisk)
-   [[2] [Supporting boot loaders]](#Supporting_boot_loaders)
    -   [[2.1] [GRUB]](#GRUB)
-   [[3] [See also]](#See_also)

## [Using hybrid partition table]

Using a hybrid partition table might be necessary when dual-booting operating systems that are blind to a GPT-partitioned disk. In these situations, the partition definition requires a tricky workaround.

### [Creating with gdisk]

Creating a hybrid MBR is easy using [gdisk]: at the main menu press the [r] key (for recovery and transformation), then press [h] key (CHS recompute), then enter the series of partitions (less or equal to 3) in the order they should be be listed in the MBR. Finally enter the hexadecimal partition type without the `0x` prefix or accept the defaults by repeatedly pressing the [y] key.

Enable only a single boot flag as found the following example:

`root `[`#`]`gdisk /dev/sdg`

    GPT fdisk (gdisk) version 0.8.1

    Partition table scan:
      MBR: MBR only
      BSD: not present
      APM: not present
      GPT: present

    Found valid MBR and GPT. Which do you want to use?
     1 - MBR
     2 - GPT
     3 - Create blank GPT

    Your answer: 2

`root `[`#`]`gdisk /dev/sdg`

    ...
    Using GPT and creating fresh protective MBR.

    Command (? for help): r
    Recovery/transformation command (? for help): p
    Disk /dev/sdg: 625142448 sectors, 298.1 GiB
    Logical sector size: 512 bytes
    Disk identifier (GUID): 744E8BF3-39A4-4908-8646-AC2E5661C8CF
    Partition table holds up to 128 entries
    First usable sector is 34, last usable sector is 625142414
    Partitions will be aligned on 2048-sector boundaries
    Total free space is 2014 sectors (1007.0 KiB)

    Number  Start (sector)    End (sector)  Size       Code  Name
       1            2048       566233087   270.0 GiB   8300  Linux filesystem
       2       566233088       625142414   28.1 GiB    0700  Microsoft basic data
    Recovery/transformation command (? for help): h

    WARNING! Hybrid MBRs are flaky and dangerous! If you decide not to use one,
    just hit the Enter key at the below prompt and your MBR partition table will
    be untouched.

    Type from one to three GPT partition numbers, separated by spaces, to be
    added to the hybrid MBR, in sequence: 2 1
    Place EFI GPT (0xEE) partition first in MBR (good for GRUB)? (Y/N): N

    Creating entry for GPT partition #2 (MBR partition #1)
    Enter an MBR hex code (default 07):
    Set the bootable flag? (Y/N): Y

    Creating entry for GPT partition #1 (MBR partition #2)
    Enter an MBR hex code (default 83):
    ...
    Unused partition space(s) found. Use one to protect more partitions? (Y/N): N

    Recovery/transformation command (? for help): o

    Disk size is 625142448 sectors (298.1 GiB)
    MBR disk identifier: 0x00000000
    MBR partitions:

    Number  Boot  Start Sector   End Sector   Status      Code
       1      *      566233088    625142414   primary     0x07
       2                  2048    566233087   primary     0x83
       4                     1         2047   primary     0xEE

    Recovery/transformation command (? for help): w

** Note**\
In the example above, [N] was used to answer the safe questions. Without [N], [fdisk -l /dev/sdg] will list the MBR partition list just fine but [ls /dev] wouldn\'t list the partitions - and even more annoying: the partitions wouldn\'t be listed in DOS/BIOS.

## [Supporting boot loaders]

### [GRUB]

GRUB supports booting from GPT and MBR partition tables via the `part_gpt` and `part_msdos` modules. However, a successful setup and GRUB\'s ability to boot correctly depends both on loaded partition modules and on correctly installing GRUB. A determining factor in how GRUB is installed (BIOS-MBR vs BIOS-GPT) is the presence of a EE00 (GPT protective) partition as the first partition in the MBR.

With a hybrid MBR, GRUB will install *if* the first partition in the MBR table is an `EE00` partition. An `EF02` partition should be present anywhere in the disk and not necessarily in the MBR list. Leave enough open sectors before the first partition!

** Note**\
In this case one does *not* have to add/list an `EE00` partition in the hybrid MBR list manually, [gdisk] will provide a prompt to list one if booting with GRUB before displaying the provided list (up to 3 partitions) by the user.

GRUB requires an `EE00` partition type at the first listing in the MBR partition list entry, however it may pose a problem when booting other operating systems on the same disk (especially Windows). A workaround is available in order to recognize a GPT partitioned disk with (or without) hybrid MBR. Removing any protective `EE00` partition with the [fdisk] command.

** Warning**\
Do **not use** [gdisk] to remove the `EE00` partition! The [gdisk] command does not work because a \"fake\" partition exists to protect the main GPT table while booted in BIOS - MBR mode.

Use other disk tools such as [parted] ([[[sys-block/parted]](https://packages.gentoo.org/packages/sys-block/parted)[]]) or [gparted] ([[[sys-block/gparted]](https://packages.gentoo.org/packages/sys-block/gparted)[]]) to resize after that. Otherwise use [gdisk] to add protective `EE00` partitions to protect at least GPT main and backup the partition before using any non-GPT aware tools if necessary.

Another issue should be addressed when attempting to use a GPT Hybrid MBR configuration: Windows MSDOS based bootloaders may not find suitable partitions to boot from if there is a `EE00` partition protecting the GPT main partition table (sectors 1-2047). If this happens remove the protective `EE00` partition before getting a valid MBR partition list in \[MS\]DOS tools (to format a partition for example, the tools recognized a GPT partitioned disk at least). And *then* use [gdisk] to recompute the CHS value for hybrid MBR (in the *recovery and transformation* menu, or in the *expert* section of [gdisk]\'s main menu).

## [See also]

-   [GRUB](https://wiki.gentoo.org/wiki/GRUB "GRUB") --- a multiboot secondary [bootloader](https://wiki.gentoo.org/wiki/Bootloader "Bootloader") capable of loading kernels from a variety of [filesystems](https://wiki.gentoo.org/wiki/Filesystem "Filesystem") on most system architectures.