# File recovery

This article lists data recovery and undeletion options for Linux.

It is mostly intended to be used for educational purposes. If you have accidentally deleted or otherwise damaged your valuable and irreplaceable data on a technically healthy/functional drive and have no previous experience with data recovery, turn off your computer immediately (just press and hold the off button or pull the plug; do not use the system shutdown function) and seek professional help.

## Special cases
## Failing drives
In the area of data recovery, it is best to work on images of disks rather than physical disks themselves. Generally, a failing drive's condition worsens over time. The goal ought to be to first rescue as much data as possible as early as possible in the failure of the disk and to then abandon the disk. The  and  utilities, unlike , will repeatedly try to recover from errors and will read the drive front to back, then back to front, attempting to salvage data. They keep log files so that recovery can be paused and resumed without losing progress.

See Disk cloning.

The image files created from a utility like ddrescue can then be mounted like a physical device and can be worked on safely. Always make a copy of the original image so that you can revert if things go sour!

Do not attempt a filesystem check on a failing drive, as this will likely make the problem worse. Mount it read-only.

## Backup flash media/small partitions
As an alternative to working with a 'live' partition (mounted or not), it is often preferable to work with an image, provided that the filesystem in question is not too large and that you have sufficient free HDD space to accommodate the image file. For example, flash memory devices like thumb drives, digital cameras, portable music players, cellular phones, etc. are likely to be small enough to image in many cases.

Be sure to read the man pages for the utilities listed below to verify that they are capable of working with image files.

To make an image, one can use  as follows:

 # dd if=/dev/target_partition of=/home/user/partition.image

## Working with digital cameras
In order for some of the utilities listed in the next section to work with flash media, the device in question needs to be mounted as a block device (i.e., listed under /dev). Digital cameras operating in PTP (Picture Transfer Protocol) mode will not work in this regard. PTP cameras are transparently handled by libgphoto and/or libptp. In this case, "transparently" means that PTP devices do not get block devices. The alternative to PTP mode, USB Mass Storage (UMS) mode, is not supported by all cameras. Some cameras have a menu item that allows switching between the two modes; refer to your camera's user manual. If your camera does not support UMS mode and therefore cannot be accessed as a block device, your only alternative is to use a flash media reader and physically remove the storage media from your camera.

## List of utilities
See also Wikipedia:List of data recovery software#File Recovery

*
*
*
*
*
*
*
*

## TestDisk and PhotoRec
TestDisk and Photorec are both open-source data recovery utilities licensed under the terms of the GNU Public License (GPL).

TestDisk is primarily designed to help recover lost partitions and/or make non-booting disks bootable again when these symptoms are caused by faulty software, certain types of viruses, or human error, such as the accidental deletion of partition tables. TestDisk detects numerous filesystem including NTFS, FAT12, FAT16, FAT32, exFAT, ext2, ext3, ext4, btrfs, BeFS, CramFS, HFS, JFS, Linux Raid, Linux Swap, LVM, LVM2, NSS, ReiserFS, UFS, XFS. It can also undelete files from FAT, NTFS, exFAT and ext2 filesystem.

TestDisk allows to fix partition tables, recover deleted partitions, recover FAT32 boot sector from its backup, rebuild FAT12/FAT16/FAT32 boot sectors, fix FAT tables, rebuild NTFS boot sector and more.

PhotoRec is file recovery software designed to recover lost files including photographs (Hint: PhotographRecovery), videos, documents, archives from hard disks and CD-ROMs. PhotoRec ignores the filesystem and goes after the underlying data, so it will still work even with a re-formatted or severely damaged filesystems and/or partition tables.

## Installation
Install the  package, which provides both TestDisk and PhotoRec.

## Usage
After running e.g.  to create image.img,
 will open a terminal UI where you can select what file types to search for and where to put the recovered files. There is very good documentation on their wiki (step by step guide).

## Files recovered by photorec
The photorec utility stores recovered files with a random names(for most of the files) under a numbered directories, e.g. , .

## e2fsck
e2fsck is the ext2/ext3/ext4 filesystem checker included in the base install of Arch. e2fsck relies on a valid superblock. A superblock is a description of the entire filesystem's parameters. Because this data is so important, several copies of the superblock are distributed throughout the partition. With the  option, e2fsck can take an alternate superblock argument; this is useful if the main, first superblock is damaged.

To determine where the superblocks are, run  as root on the target, unmounted partition. Superblocks are spaced differently depending on the filesystem's blocksize, which is set when the filesystem is created.

An alternate method to determine the locations of superblocks is to use the  option with mke2fs. Be sure to use the  flag, which, according to , "Causes mke2fs to not actually create a filesystem, but display what it would do if it were to create a filesystem. This can be used to determine the location of the backup superblocks for a particular filesystem, so long as the mke2fs parameters that were passed when the filesystem was originally created are used again. (With the  option added, of course!)".

## Installation
Both e2fsck and dumpe2fs are included in the base Arch install as part of .

See also  and .

## Working with raw disk images
If you have backed up a drive using ddrescue or dd and you need to mount this image as a physical drive, see this section.

## Mount the entire disk
To mount a complete disk image to the next free loop device, use the  command:

 # losetup -f -P /path/to/image

See also QEMU#With loop module autodetecting partitions.

## Mounting partitions
In order to be able to mount a partition of a whole disk image, follow the steps above.

Once the whole disk image is mounted, a normal  command can be used on the loop device:

 # mount /dev/loop0p1 /mnt/example

This command mounts the first partition of the image in loop0 to the folder to the mountpoint . Remember that the mountpoint directory must exist!

## Getting disk geometry
Once the entire disk image has been mounted as a loopback device, its drive layout can be inspected.

## Using QEMU to repair NTFS
With a disk image that contains one or more NTFS partitions that need to be ed by Windows since no good NTFS filesystem checker for Linux exists, QEMU can use a raw disk image as a real hard disk inside a virtual machine:

 # qemu -hda /path/to/primary.img -hdb /path/to/DamagedDisk.img

Then, assuming Windows is installed on , it can be used to check partitions on .

## Text file recovery
It is possible to find deleted plain text files on a hard drive by directly searching on the block device. A preferably unique string from the file you are trying to recover is needed.

Use  to search for fixed strings () directly on the partition:

 $ grep -a -C 200 -F 'Unique string in text file' /dev/sdXN > OutputFile

Hopefully, the content of the deleted file is now in OutputFile, which can be extracted from the surrounding context manually.
