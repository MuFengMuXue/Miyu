# GPT fdisk

GPT fdisk—consisting of the gdisk, cgdisk, sgdisk, and fixparts programs—is a set of text-mode partitioning tools made by Rod Smith. They work on Globally Unique Identifier (GUID) Partition Table (GPT) disks, rather than on the older (and once more common) Master Boot Record (MBR) partition tables.

gdisk, cgdisk and sgdisk all have the same functionality but provide different user interfaces. gdisk is text-mode interactive, sgdisk is command-line, and cgdisk has a curses-based interface. This article covers  and  utilities.

## Installation
Install the  package.

## List partitions
To list partition tables and partitions on a block device, you can run the following, where device is a name like , , , etc.:

 # gdisk -l /dev/sda

or alternatively the same action using sgdisk:

 # sgdisk -p /dev/sda

## Backup and restore partition table
Before making changes to a disk, you may want to backup the partition table and partition scheme of the drive. You can also use a backup to copy the same partition layout to numerous drives.

Using sgdisk you can create a binary backup consisting of the protective MBR, the main GPT header, the backup GPT header, and one copy of the partition table. The example below will save the partition table of  to a file :

 # sgdisk -b=sgdisk-sda.bin /dev/sda

You can later restore the backup by running:

 # sgdisk -l=sgdisk-sda.bin /dev/sda

If you want to clone your current device's partition layout ( in this case) to another drive () run:

 # sgdisk -R=/dev/sdc /dev/sda

If both drives will be in the same computer, you need to randomize the disk and partition GUIDs:

 # sgdisk -G /dev/sdc

## Create a partition table and partitions
The first step to partitioning a disk is making a partition table. After that, the actual partitions are created according to the desired partition scheme.

Before beginning, you may wish to backup your current partition table and scheme.

The following shows how to use gdisk to perform both the creation of a partition table and the creation of the actual partitions. Alternatively, you may use the curses-based version called cgdisk; however, the following instructions do not apply to it. See  for its usage.

gdisk performs partition alignment automatically on a 2048 512-byte sector (1 MiB) block size base which should be compatible with all Advanced Format HDDs and the vast majority of SSDs if not all.

To use gdisk, run the program with the name of the block device you want to change/edit. This example uses :

 # gdisk /dev/sda

## Create new table
To create a new GUID Partition Table and clear all current partition data, type  at the prompt. Skip this step if the table you require has already been created.

## Create partitions
Create a new partition with the  command. You must enter the partition number, first sector, last sector and the partition type.

## Partition number
A partition number is the number assigned to a partition, e.g. a partition with number  on a disk  would be ,  on  and  on . See Device file#Partition for details on the naming scheme. Partition numbers may not always match the order of partitions on disk, in which case they can be sorted.

It is advised to choose the default number suggested by gdisk.

## First and last sector
The first and last sectors of the partition can be specified in sector numbers or as positions measured in kibibytes (), mebibytes (), gibibytes (), tebibytes (), or pebibytes ();

The position can be specified in:

* absolute terms from the start of the disk. E.g.  as a first sector specifies a position 40 MiB from the start of the disk.
* relative terms by preceding the size with  or . E.g.  to specify a point 2 GiB after the default start sector, or  to specify a point 200 MiB before the last available sector.

Pressing the  key with no input specifies the default value, which is the start of the largest available block for the first sector and the end of the same block for the last sector.

{{Note|Make sure to specify partition sizes using relative terms with the {{ic|+size{M,G,T,P}}} notation and not use sizes smaller than 1 MiB. Such partitions will always be aligned according to the device properties.}}

## Partition type
Select the partition's type by entering gdisk's internal type code or specifying the partition type GUID manually. The default,  (GUID , gdisk's internal code ), should be fine for most use cases.

{| class="wikitable"
|+ Common partition types
! Partition type
! Mountpoint
! gdisk's code
! Partition type GUID
|-
|Linux filesystem
|Any
|
|
|-
|EFI system partition
|Any1
|
|
|-
|BIOS boot partition
|None
|
|
|-
|XBOOTLDR partition
|Any
|
|
|-
|Linux x86-64 root (/)
|
|
|
|-
|Linux swap
|
|
|
|-
|Linux /home
|
|
|
|-
|Linux /srv
|
|
|
|-
|Linux /var
|1
|
|
|-
|Linux /var/tmp
|1
|
|
|-
|Linux LVM
|Any
|
|
|-
|Linux RAID
|Any
|
|
|-
|Linux LUKS
|Any
|
|
|-
|Linux dm-crypt
|Any
|
|
|}

#  will only automount the partition if specific conditions are met. See systemd#GPT partition automounting for details.

Repeat this procedure until you have the partitions you desire.

## Write changes to disk
Write the table to disk and exit via the  command.

## Tips and tricks
## Convert between MBR and GPT
gdisk, sgdisk and cgdisk have the ability to convert MBR and BSD disklabels to GPT without data loss. Upon conversion, all the MBR primary partitions and the logical partitions become GPT partitions with the correct partition type GUIDs and Unique partition GUIDs created for each partition.

After conversion, the boot loader will need to be reinstalled to configure it to boot from GPT.

To convert an MBR partition table to GPT using sgdisk, use the / option:

 # sgdisk -g /dev/sda

To convert GPT to MBR use the / option. Note that it is not possible to convert more than four partitions from GPT to MBR.

 # sgdisk -m /dev/sda

## Sort partitions
This applies for when a new partition is created in the space between two partitions or a partition is deleted.  is used in this example.

 # sgdisk -s /dev/sda

After sorting the partitions if you are not using Persistent block device naming, it might be required to adjust the  and/or the  configuration files.

## Recover GPT header
In case main GPT header or backup GPT header gets damaged, you can recover one from the other with gdisk.  is used in this example.

 # gdisk /dev/sda

choose  for recovery and transformation options (experts only). From there choose either

* : use backup GPT header (rebuilding main)
* : use main GPT header (rebuilding backup)

When done write the table to disk and exit via the  command.

## Expand a GPT disk
After enlarging a disk (e.g. in hardware RAID or a virtual machine disk) the newly added free space will not be immediately usable since GPT keeps data at the end of the disk. You must relocate the backup GPT header to the new end of the disk.

Run sgdisk with the option /, e.g.:

 # sgdisk -e /dev/sda

Afterwards print the partition table; the total free space should now be increased.

## Prevent GPT partition automounting
 will automount partitions following the Discoverable Partitions Specification. Sometimes that may not be desirable.

The automounting can be disabled by setting the partition attribute  "do not automount" on the partition.

Start gdisk, e.g.:

 # gdisk /dev/sda

Press  to print the partition table and take note of the partition number(s) of the for which you want to disable automounting.

Press  extra functionality (experts only).

Press  set attributes. Input the partition number and set the attribute . Under  it should now show . Press  to end attribute changing. Repeat this for all partitions you want to prevent from automounting.

When done write the table to disk and exit via the  command.

Alternatively using sgdisk, the attribute can be set using the / option; see  for usage. For example, to set partition attribute  "do not automount" on  run:

 # sgdisk -A 2:set:63 /dev/sda

## gdisk EFI application
There is no package for the EFI version of gdisk, but Rod Smith provides a prebuilt gdisk-1.04 EFI binary on SourceForge. Download  and extract the archive. To use it, copy  to the EFI system partition and launch it from your boot loader or UEFI Shell.

gdisk_x64.efi allows you to edit the partition table before the operating system is even booted. It is used the same way as the gdisk binary on Linux.

See README-efi.txt for more information.
