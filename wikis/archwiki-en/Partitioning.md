# Partitioning

From Wikipedia:

:Disk partitioning or disk slicing is the creation of one or more regions on secondary storage, so that each region can be managed separately.

An entire disk may be allocated to a single partition, or multiple ones for cases such as dual-booting, maintaining a swap partition, or to logically separate data such as audio and video files. The partitioning scheme is stored in a partition table such as Master Boot Record (MBR) or GUID Partition Table (GPT).

Partition tables are created and modified using one of many partitioning tools. The tools available for Arch Linux are listed in the #Partitioning tools section.

Partitions usually contain a file system directly which is accomplished by creating a file system on (a.k.a. formatting) the partition. Alternatively, partitions can contain LVM, block device encryption or RAID, which ultimately provide device files on which a file system can be placed (or the devices can be stacked further).

Any block device (e.g. disk, partition, LUKS device, LVM logical volume or RAID array) that directly contains a mountable file system is called a volume.

## Partition table
There are two main types of partition table available. These are described below in the #Master Boot Record (MBR) and #GUID Partition Table (GPT) sections along with a discussion on how to choose between the two. A third, less common alternative is using a partitionless disk, which is also discussed.

Use a partitioning tool to view the partition table of a block device.

## Master Boot Record
The Master Boot Record (MBR) is the first 512 bytes of a storage device. It contains an operating system boot loader and the storage device's partition table. It plays an important role in the boot process under BIOS systems. See Wikipedia:Master boot record#Disk partitioning for the MBR structure.

## Master Boot Record (bootstrap code)
The first 440 bytes of MBR are the bootstrap code area. On BIOS systems it usually contains the first stage of the boot loader. The bootstrap code can be backed up, restored from backup or erased using dd.

## Master Boot Record (partition table)
In the MBR partition table (also known as DOS or MS-DOS partition table) there are 3 types of partitions:

* Primary
* Extended
** Logical

Primary partitions can be bootable and are limited to four partitions per disk or RAID volume. If the MBR partition table requires more than four partitions, then one of the primary partitions needs to be replaced by an extended partition containing logical partitions within it.

Extended partitions can be thought of as containers for logical partitions. A hard disk can contain no more than one extended partition. The extended partition is also counted as a primary partition so if the disk has an extended partition, only three additional primary partitions are possible (i.e. three primary partitions and one extended partition). The number of logical partitions residing in an extended partition is unlimited. A system that dual boots with Windows will require for Windows to reside in a primary partition.

The customary numbering scheme is to create primary partitions sda1 through sda3 followed by an extended partition sda4. The logical partitions on sda4 are numbered sda5, sda6, etc.

## GUID Partition Table
GUID Partition Table (GPT) is a partitioning scheme that is part of the Unified Extensible Firmware Interface specification; it uses globally unique identifiers (GUIDs), or UUIDs in the Linux world, to define partitions and partition types. It is designed to succeed the Master Boot Record partitioning scheme method.

At the start of a GUID Partition Table disk there is a protective Master Boot Record (PMBR) to protect against GPT-unaware software. This protective MBR just like an ordinary MBR has a bootstrap code area which can be used for BIOS/GPT booting with boot loaders that support it.

## Choosing between GPT and MBR
GUID Partition Table (GPT) is an alternative, contemporary, partitioning style; it is intended to replace the old Master Boot Record (MBR) system. GPT has several advantages over MBR which has quirks dating back to MS-DOS times. With the recent developments to the formatting tools, it is equally easy to get good dependability and performance for GPT or MBR.

Some points to consider when choosing:

* To dual-boot with Windows (both 32-bit and 64-bit) using Legacy BIOS, the MBR scheme is required.
* To dual-boot Windows 64-bit using UEFI mode instead of BIOS, the GPT scheme is required.
* If you are installing on older hardware, especially on old laptops, consider choosing MBR because its BIOS might not support GPT (but see below how to fix it).
* If you are partitioning a disk that is larger than 2 TiB (≈2.2 TB), you need to use GPT.
* It is recommended to always use GPT for UEFI boot, as some UEFI implementations do not support booting to the MBR while in UEFI mode.
* If none of the above apply, choose freely between GPT and MBR. Since GPT is more modern, it is recommended in this case.

Some advantages of GPT over MBR are:

* Provides a unique disk GUID and unique partition GUID (PARTUUID) for each partition – a good filesystem-independent way of referencing partitions and disks. GUIDs are a prerequisite for the Discoverable Partitions Specification that can be utilized in a systemd-enabled initramfs.
* Provides a filesystem-independent partition name (PARTLABEL).
* Arbitrary number of partitions - depends on space allocated for the partition table - No need for extended and logical partitions. By default the GPT table contains space for defining 128 partitions. However if you want to define more partitions, you can allocate more space to the partition table (currently only gdisk is known to support this feature).
* Uses 64-bit LBA for storing Sector numbers - maximum addressable disk size is 2 ZiB. MBR is limited to addressing 2 TiB of space per drive.* Stores a backup header and partition table at the end of the disk that aids in recovery in case the primary ones are damaged.
* CRC32 checksums to detect errors and corruption of the header and partition table.

The section on #Partitioning tools contains a table indicating which tools are available for creating and modifying GPT and MBR tables.

## Partitionless disk
Partitionless disk a.k.a. [https://learn.microsoft.com/en-us/windows-hardware/manufacture/desktop/windows-and-gpt-faq#superfloppy superfloppy refers to a storage device without a partition table, having one file system occupying the whole storage device. The boot sector present on a partitionless device is called a volume boot record (VBR).

## Btrfs partitioning
Btrfs can occupy an entire data storage device and replace the MBR or GPT partitioning schemes. See the Btrfs#Partitionless Btrfs disk instructions for details.

## Partition scheme
There are no strict rules for partitioning a hard drive, although one may follow the general guidance given below. A disk partitioning scheme is determined by various issues such as desired flexibility, speed, security, as well as the limitations imposed by available disk space. It is essentially personal preference. If you would like to dual boot Arch Linux and a Windows operating system please see Dual boot with Windows.

## Single root partition
This scheme is the simplest, most flexible and should be enough for most use cases given the increase in storage size of consumer grade devices. A swap file can be created and easily resized as needed. It usually makes sense to start by considering a single  partition and then separate out others based on specific use cases like RAID, encryption, a shared media partition, etc… See #Discrete partitions for a description of some common to uncommon dedicated partitions.

The suggested minimum size is 23–32 GiB for a single root partition. More space may be needed for user files and when using a swap file. A bare minimal installation requires about 2 GiB. As examples, a simple server can fit under 4 GiB while a full KDE Plasma installation uses 10 GiB. Both examples require frequent purges of the package cache.

A GPT partition should have the "Linux root (x86-64)" type GUID  ( type for gdisk). An MBR partition should have the default "Linux" type ID .

## Discrete partitions
Separating out a path as a partition allows for the choice of a different filesystem and mount options. In some cases like a media partition, they can also be shared between operating systems.

Below are some example layouts that can be used when partitioning, and the following subsections detail a few of the directories which can be placed on their own separate partition and then mounted at mount points under . See  for a full description of the contents of these directories.

## /
The root directory is the top of the hierarchy, the point where the primary filesystem is mounted and from which all other filesystems stem. All files and directories appear under the root directory , even if they are stored on different physical devices. The contents of the root filesystem must be adequate to boot, restore, recover, and/or repair the system. Therefore, certain directories under  are not candidates for separate partitions.

The  partition or root partition is necessary and it is the most important. The other partitions can be replaced by it.

 traditionally contains the  directory, which can grow significantly depending upon how much software is installed. 15–20 GiB should be sufficient for most users with modern hard disks. If you plan to store a swap file here and do not plan on using a separate /var, you might need a larger partition size (i.e. adding the size of your RAM to be able to hibernate and an additional 8–12 GiB for ).

A GPT partition should have the "Linux root (x86-64)" type GUID  ( for gdisk). An MBR partition should have the default "Linux" type ID .

## /boot
The  directory contains the vmlinuz and initramfs images as well as the boot loader configuration file and boot loader stages. It also stores data that is used before the kernel begins executing user-space programs.  is not required for normal system operation, but only during boot and kernel upgrades (when regenerating the initial ramdisk).

When using an EFI system partition as , the requirements are as described in the EFI system partition article—the correct partition type must be set.

In other cases, it is recommended to set the partition type to Extended Boot Loader (XBOOTLDR) Partition which is GPT partition type GUID  ( type for gdisk,  type for fdisk) or MBR partition type ID .

In both cases the suggested size for the partition is 1 GiB, which should give enough space to house multiple kernels. If still in doubt, 4 GiB ought to be enough for anybody.

## /home
The  directory contains user-specific configuration files, caches, application data and media files.

Separating out  allows  to be re-partitioned separately, but note that you can still reinstall Arch with  untouched even if it is not separate—the other top-level directories just need to be removed, and then pacstrap can be run.

You should not share home directories between users on different distributions, because they use incompatible software versions and patches. Instead, consider sharing a media partition or at least using different home directories on the same  partition. The size of this partition varies.

A GPT partition should have the "Linux home" type GUID  ( type for gdisk,  type for fdisk). An MBR partition should have the default "Linux" type ID .

## Swap
A swap is a file or partition that provides disk space used as virtual memory. Swap files and swap partitions are equally performant, but swap files are much easier to resize as needed. A swap partition can potentially be shared between operating systems, but not if hibernation is used.

Since computers have gained memory capacities superior to a gibibit, the previous "twice the amount of physical RAM" rule has become outdated. A sane default size is 4 GiB.

To use hibernation (a.k.a. suspend to disk) it is advised to create the swap partition at the size of RAM. Although the kernel will try to compress the suspend-to-disk image to fit the swap space there is no guarantee it will succeed if the used swap space is significantly smaller than RAM. See Power management/Suspend and hibernate#Hibernation for more information.

A GPT partition should have the "Linux swap" type with GUID  ( type for gdisk,  type for fdisk). An MBR partition should have the "Linux swap" type ID .

## /data
One can consider mounting a "data" partition to cover various files to be shared by all users. Using the  partition for this purpose is fine as well. The size of this partition varies.

A GPT partition should have the default "Linux filesystem" type GUID . An MBR partition should have the default "Linux" type ID .

## /var
The  directory stores variable data such as spool directories and files, administrative and logging data, pacman's cache, etc. It is used, for example, for caching and logging, and hence frequently read or written. Keeping it in a separate partition avoids running out of disk space due to flunky logs, etc.

It exists to make it possible to mount  as read-only. Everything that historically went into  that is written to during system operation (as opposed to installation and software maintenance) must reside under .

 will contain, among other data, the pacman cache. Retaining these packages is helpful in case a package upgrade causes instability, requiring a downgrade to an older, archived package. The pacman cache will grow as the system is expanded and updated, but it can be safely cleared if space becomes an issue.

8–12 GiB on a desktop system should be sufficient for , depending on how much software will be installed. For users of NVIDIA, Wayland and GDM, consider adding to this partition size as to have enough free space to fit your whole video memory.

A GPT partition should have the "Linux variable data" a.k.a. "Linux /var" type GUID  ( type for gdisk). An MBR partition should have the default "Linux" type ID .

## Example layouts
The following examples use  as the example disk with  as the first partition. The block device naming scheme will differ if you are partitioning an NVMe disk (e.g.  with partitions starting from ) or an SD card or eMMC disk (e.g.  with partitions starting from ). See Device file#Block device names for more information.

## UEFI/GPT layout example
{| class="wikitable"
! Mount point on the installed system
! Partition
! Partition type GUID
! Suggested size
|-
|  or 1
|
| : EFI system partition
| 1 GiB
|-
|
|
| : Linux swap
| At least 4 GiB or the size of RAM to use hibernation
|-
|
|
| : Linux x86-64 root (/)
| Remainder of the device. At least 23–32 GiB.
|}

## BIOS/MBR layout example
{| class="wikitable"
! Mount point on the installed system
! Partition
! Partition type ID
! Boot flag
! Suggested size
|-
|
|
| : Linux swap
|
| At least 4 GiB or the size of RAM to use hibernation
|-
|
|
| : Linux
|
| Remainder of the device. At least 23–32 GiB.
|-
|
| Unallocated space2
|
|
| At least 16.5 KiB at the end of the disk
|}

## BIOS/GPT layout example
{| class="wikitable"
! Mount point on the installed system
! Partition
! Partition type GUID
! Suggested size
|-
|
|
| : BIOS boot partition3
| 1 MiB
|-
|
|
| : Linux swap
| At least 4 GiB or the size of RAM to use hibernation
|-
|
|
| : Linux x86-64 root (/)
| Remainder of the device. At least 23–32 GiB.
|}

# The ESP can be mounted to  if the used boot loader is capable of accessing the file system (and everything above it) on which the kernel and initramfs images are located. See EFI system partition#Typical mount points and the warning in Arch boot process#Boot loader for details.
# An unpartitioned space of at least 33 512-byte sectors (16.5 KiB) at the end of the disk to allow converting to GPT in the future. The space will be required for the backup GPT header. The recommendation to preserve an unpartitioned space applies to all MBR partitioned disks.
# A BIOS boot partition is only required when using GRUB or Limine for BIOS booting from a GPT disk, it is not needed when using other boot loaders. The partition has nothing to do with , and it must not be formatted with a file system or mounted.

## Tools
## Partitioning tools
The following programs are used to create and/or manipulate device partition tables and partitions. See the linked articles for the exact commands to be used.

This table will help you to choose utility for your needs:

{| class="wikitable sortable"
|-
! Name
! Package
! MBR
! GPT
! CLI
! TUI
! Scripting utility
|-
| fdisk
|
|
|
|
|
|
|-
| GPT fdisk
|
|
|
|
|
|
|-
| Parted
|
|
|
|
|
|
|}

## GUI frontends
*
*
*
*

## Backup
* fdisk can create a backup of the partitions table. See fdisk#Backup and restore partition table.
* GPT fdisk can create a binary backup consisting of the protective MBR, the main GPT header, the backup GPT header, and one copy of the partition table. See GPT fdisk#Backup and restore partition table.

## Recovery
*
*
*

## Partition alignment
The rule of thumb is to align a partition's start and size to mebibytes. See Advanced Format#Partition alignment.

## GPT kernel support
The  option in the kernel config enables GPT support in the kernel (despite the name, EFI PARTITION which looks close to EFI system partition). This option must be built in the kernel and not compiled as a loadable module. This option is required even if GPT disks are used only for data storage and not for booting. This option is enabled by default in all Arch's officially supported kernels. In case of a custom kernel, enable this option by doing .

## Troubleshooting
## Tricking old BIOS into booting from GPT
Some old BIOSes (from before year 2010) attempt to parse the boot sector and refuse to boot it if it does not contain a bootable MBR partition. This is a problem if one wants to use GPT on this disk, because, from the BIOS viewpoint, it contains only one, non-bootable, MBR partition of type  (i.e., the protective MBR partition). One can mark the protective MBR entry as bootable using , and it will work on some BIOSes. However, the UEFI specification prohibits the protective MBR partition entry from being bootable, and UEFI-based boards do care about this, even in the legacy boot mode. So, this matters if one wants to create a GPT-based USB flash drive that is supposed to boot both on modern UEFI-based boards and also on old BIOSes that insist on finding a bootable MBR partition. It is not possible to solve this problem using traditional tools such as fdisk or gdisk, but it is possible to create a fake MBR partition entry suitable for both kinds of BIOSes manually as a sequence of bytes.

The command below will overwrite the second MBR partition slot and add a bootable partition there of type 0 (i.e. unused), covering only the first sector of the device. It will not interfere with the GPT or with the first MBR partition entry which normally contains a protective MBR partition.

 # printf '\200\0\0\0\0\0\0\0\0\0\0\0\001\0\0\0' | dd of=/dev/sda bs=1 seek=462

The end result will look like this:

## Drives are not visible when firmware RAID is enabled
If a SATA or NVMe drive is visible in firmware setup, but not to Linux (e.g.  does not list it), it is possible that the controller is in firmware RAID mode.

For NVMe, the journal should show something like:

 kernel: ahci 0000:00:17.0: Found 1 remapped NVMe devices.
 kernel: ahci 0000:00:17.0: Switch your BIOS from RAID to AHCI mode to use them.

The solution is to enter firmware setup and disable NVMe RAID mode and change the SATA controller operation mode from RAID to AHCI. Mind that the setting may have a different name (e.g. "Intel Rapid Storage Technology", "Intel RST", "Intel VMD controller" or "VMD") and it could also be per-controller or per-port.
