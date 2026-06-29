# Parted

GNU Parted is a program for creating and manipulating partition tables. GParted is a GUI frontend.

## Installation
Install one of the following packages:

*  – command-line only.
*  – a graphical front-end for parted.
:

## Usage
Parted has two modes: command line and interactive. Parted should always be started with:

 # parted device

where  is block device name like , , , etc. If you omit the  argument, parted will attempt to guess which device you want.

## Command line mode
In command line mode, this is followed by one or more commands. For example:

 # parted /dev/sda --script mklabel gpt mkpart P1 ext3 1MiB 8MiB

## Interactive mode
Interactive mode simplifies the partitioning process and reduces unnecessary repetition by automatically applying all partitioning commands to the specified device.

In order to start operating on a device, execute:

 # parted /dev/sdx

You will notice that the command-line prompt changes from a hash () to : this also means that the new prompt is not a command to be manually entered when running the commands in the examples.

To see a list of the available commands, enter:

 (parted) help

When finished, or if wishing to implement a partition table or scheme for another device, exit from parted with:

 (parted) quit

After exiting, the command-line prompt will change back to .

If you do not give a parameter to a command, Parted will prompt you for it. For example:

 (parted) mklabel
 New disk label type? gpt

## Rounding
Since many partitioning systems have complicated constraints, Parted will usually do something slightly different to what you asked. (For example, create a partition starting at 10.352Mb, not 10.4Mb) If the calculated values differ too much, Parted will ask you for confirmation.  If you know exactly what you want, or to see exactly what Parted is doing, it helps to specify partition endpoints in sectors (with the "s" suffix) and give the "unit s" command so that the partition endpoints are displayed in sectors.

As of parted-2.4, when you specify start and/or end values using IEC binary units like “MiB”, “GiB”, “TiB”, etc., parted treats those values as exact, and equivalent to the same number specified in bytes (i.e., with the “B” suffix), in that it provides no “helpful” range of sloppiness. Contrast that with a partition start request of “4GB”, which may actually resolve to some sector up to 500MB before or after that point. Thus, when creating a partition, you should prefer to specify units of bytes (“B”), sectors (“s”), or IEC binary units like “MiB”, but not “MB”, “GB”, etc.

## Partitioning
## Create new partition table
You need to (re)create the partition table of a device when it has never been partitioned before, or when you want to change the type of its partition table. Recreating the partition table of a device is also useful when the partition scheme needs to be restructured from scratch.

Open each device whose partition table must be (re)created with:

 # parted /dev/sdx

To then create a new GUID Partition Table, use the following command:

 (parted) mklabel gpt

To create a new Master Boot Record/MS-DOS partition table instead, use:

 (parted) mklabel msdos

## Partition schemes
You can decide the number and size of the partitions the devices should be split into, and which directories will be used to mount the partitions in the installed system (also known as mount points). See Partitioning#Partition scheme for the required partitions.

The following command will be used to create partitions:

 (parted) mkpart part-type-or-part-label fs-type start end

*  is interpreted differently based on the partition table:
** MBR: the parameter is interpreted as , which can be one of ,  or .
** GPT: the parameter is interpreted as , which sets the PARTLABEL attribute of the partition. To avoid setting a partition label, pass an empty quoted string ().
*  is an identifier chosen among those listed by entering  as the closest match to the file system that you will use. The mkpart command does not actually create the file system: the  parameter will simply be used by parted to set  partition type GUID for GPT partitions or partition type ID for MBR partitions.
*  is the beginning of the partition from the start of the device. It consists of a number followed by a unit, for example  means start at 1 MiB.
*  is the end of the partition from the start of the device (not from the  value). It has the same syntax as , for example  means end at the end of the device (use all the remaining space).

The following command will be used to flag the partition that contains the  directory as bootable:

 (parted) set partition boot on

*  is the number of the partition to be flagged (see the output of the  command).
*  is an alias for  on GPT. *  sets the Legacy BIOS Bootable attribute. This attribute is used by syslinux[https://git.savannah.gnu.org/cgit/parted.git/commit/?id=3dd52c822a40f9787765f21f7cbd6f1c37b42f7e and other software that has a traditional PC-AT BIOS firmware implementation.==== UEFI/GPT examples ====

In every instance, a special bootable EFI system partition is required.

If creating a new EFI system partition, use the following commands (the recommended size is at least 1 GiB):

 (parted) mkpart "EFI system partition" fat32 1MiB 1025MiB
 (parted) set 1 esp on

The remaining partition scheme is entirely up to you. For one root partition using 100% of remaining space:

 (parted) mkpart "root partition" ext4 1025MiB 100%
 (parted) type 2 4F68BCE3-E8CD-4DB1-96E7-FBCAF984B709

For separate swap (4 GiB) and  (all remaining space) partitions:

 (parted) mkpart "swap partition" linux-swap 1025MiB 5121MiB
 (parted) mkpart "root partition" ext4 5121MiB 100%
 (parted) type 3 4F68BCE3-E8CD-4DB1-96E7-FBCAF984B709

And for separate swap (4 GiB),  (32 GiB) and  (all remaining space) partitions:

 (parted) mkpart "swap partition" linux-swap 1025MiB 5121MiB
 (parted) mkpart "root partition" ext4 5121MiB 37889MiB
 (parted) type 3 4F68BCE3-E8CD-4DB1-96E7-FBCAF984B709
 (parted) mkpart "home partition" ext4 37889MiB 100%
 (parted) set 4 linux-home on

## BIOS/MBR examples
For a minimum single primary partition using all available disk space, the following command would be used:

 (parted) mkpart primary ext4 1MiB 100%
 (parted) set 1 boot on

In the following instance, a 4 GiB swap partition will be created, followed by a  partition using all the remaining space:

 (parted) mkpart primary linux-swap 1MiB 4097MiB
 (parted) mkpart primary ext4 4097MiB 100%
 (parted) set 2 boot on

In the final example below, separate  (1 GiB), swap (4 GiB),  (32 GiB), and  (all remaining space) partitions will be created:

 (parted) mkpart primary ext4 1MiB 1025MiB
 (parted) set 1 boot on
 (parted) set 1 bls_boot on
 (parted) mkpart primary linux-swap 1025MiB 5121MiB
 (parted) mkpart primary ext4 5121MiB 37889MiB
 (parted) mkpart primary ext4 37889MiB 100%

## Resizing partitions
If you are growing a partition, you have to first resize the partition and then resize the filesystem on it, while for shrinking the filesystem must be resized before the partition to avoid data loss.

## Growing partitions
To grow a partition (in parted interactive mode):

 (parted) resizepart number end

Where  is the number of the partition you are growing, and  is the new end of the partition (which needs to be larger than the old end).

Then, to grow the (ext2/3/4) filesystem on the partition (if  is not specified, it will default to the size of the partition):

 # resize2fs /dev/sdaX size

Or to grow a Btrfs filesystem:

 # btrfs filesystem resize size /path/to/mount/point

Where  stands for the mount point of the partition you are growing, and  in the form  or  is the new size or modification of the partition. Use  to fill the remaining space on the partition.

## Shrinking partitions
To shrink an ext2/3/4 filesystem on the partition:

 # resize2fs /dev/sdaX size

To shrink a Btrfs filesystem:

 # btrfs filesystem resize size /path/to/mount/point

Where  stands for the mount point of the partition you are shrinking, and  is the new size of the partition.

Then shrink the partition (in parted interactive mode):

 (parted) resizepart number end

Where  is the number of the partition you are shrinking, and  is the new end of the partition (which needs to be smaller than the old end).

When done, use the resizepart command from  to tell the kernel about the new size:

 # resizepart device number size

Where  is the device that holds the partition,  is the number of the partition and  is the new size of the partition, in 512-byte sectors.

## Known issues
Parted will always warn you before doing something that is potentially dangerous, unless the command is one of those that is inherently dangerous (e.g. rm, mklabel and mkpart).

## Alignment
When creating a partition, parted might warn about improper partition alignment but does not hint about proper alignment. For example:

 (parted) mkpart primary fat16 0 32M
 Warning: The resulting partition is not properly aligned for best performance.
 Ignore/Cancel?

The warning means the partition start is not aligned. Enter "Ignore" to go ahead anyway, print the partition table in sectors to see where it starts, and remove/recreate the partition with the start sector rounded up to increasing powers of 2 until the warning stops. As one example, on a flash drive with 512B sectors, Parted wanted partitions to start on sectors that were a multiple of 2048, which is 1 MiB alignment.

If you want parted to attempt to calculate the correct alignment for you, specify the start position as 0% instead of some concrete value. To make one large ext4 partition, your command would look like this:

 (parted) mkpart primary ext4 0% 100%

## Tips and tricks
## Check alignment
On an already partitioned disk, you can use parted to verify the alignment of a partition on a device. For instance, to verify alignment of partition 1 on :

 # parted /dev/sda
 (parted) align-check optimal 1
 1 aligned
