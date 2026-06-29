# Dd

dd is a core utility whose primary purpose is to copy a file and optionally convert it during the copy process.

Similarly to cp, by default dd makes a bit-to-bit copy of the file, but with lower-level I/O flow control features.

For more information, see  or the full documentation.

## Installation
dd is part of the GNU . For other utilities in the package, please refer to Core utilities.

## Disk cloning and restore
The dd command is a simple, yet versatile and powerful tool. It can be used to copy from source to destination, block-by-block, regardless of their filesystem types or operating systems. A convenient method is to use dd from a live environment, as in a Live CD.

## Cloning a partition
From physical disk , partition 1, to physical disk , partition 1:

 # dd if=/dev/sda1 of=/dev/sdb1 bs=64M status=progress

## Cloning an entire hard disk
From physical disk  to physical disk :

 # dd if=/dev/sda of=/dev/sdb bs=64M status=progress

This will clone the entire drive, including the partition table, boot loader, all partitions, UUIDs, and data.

*  sets the block size in bytes, which is the amount of data dd operates on at once. Bigger values will usually yeld better performance, but will use more memory. Defaults to 512 bytes, which is the "classic" block size for hard drives since the early 1980s, but is quite slow. Use a bigger value, at least 32M or 64M. See and [http://blog.tdg5.com/tuning-dd-block-size/ for details and to figure out the best bs value for your use case.
*  shows periodic transfer statistics which can be used to estimate when the operation may be complete.

## Backing up the partition table
See fdisk#Backup and restore partition table or gdisk#Backup and restore partition table.

## Create disk image
Boot from a live medium and make sure no partitions are mounted from the source hard drive.

Then mount the external hard drive and backup the drive:

 # dd if=/dev/sda bs=64M status=progress  lz4 -z  > /path/to/backup.img.lz4

If necessary (e.g. when the resulting files will be stored on a FAT32 file system), split the disk image into multiple parts (see also ):

 # dd if=/dev/sda bs=64M status=progress  lz4 -z  split -a3 -b2G - /path/to/backup.img.lz4

If there is not enough disk space locally, you may send the image through ssh:

 # dd if=/dev/sda bs=64M status=progress  lz4 -z  ssh user@local dd of=backup.img.lz4

Finally, save extra information about the drive geometry necessary in order to interpret the partition table stored within the image. The most important of which is the sector size.

 # fdisk -l /dev/sda > /path/to/list_fdisk.info

## Restore system
To restore your system:

 # lz4 -dc /path/to/backup.img.lz4 | dd of=/dev/sda bs=64M status=progress

When the image has been split, use the following instead:

 # cat /path/to/backup.img.lz4* | lz4 -dc | dd of=/dev/sda bs=64M status=progress

## Backup and restore MBR
Before making changes to a disk, you may want to backup the partition table and partition scheme of the drive. You can also use a backup to copy the same partition layout to numerous drives.

The MBR is stored in the first 512 bytes of the disk. It consists of 4 parts:

# The first 440 bytes contain the bootstrap code (boot loader).
# The next 6 bytes contain the disk signature.
# The next 64 bytes contain the partition table (4 entries of 16 bytes each, one entry for each primary partition).
# The last 2 bytes contain a boot signature.

To save the MBR as :

 # dd if=/dev/sdX of=/path/to/mbr_file.img bs=512 count=1

You can also extract the MBR from a full dd disk image:

 # dd if=/path/to/disk.img of=/path/to/mbr_file.img bs=512 count=1

To restore (be careful, this destroys the existing partition table and with it access to all data on the disk):

 # dd if=/path/to/mbr_file.img of=/dev/sdX bs=512 count=1

If you only want to restore the boot loader, but not the primary partition table entries, just restore the first 440 bytes of the MBR:

 # dd if=/path/to/mbr_file.img of=/dev/sdX bs=440 count=1

To restore only the partition table, one must use:

 # dd if=/path/to/mbr_file.img of=/dev/sdX bs=1 skip=446 count=64

## Remove boot loader
To erase the MBR bootstrap code (may be useful if you have to do a full reinstall of another operating system), only the first 440 bytes need to be zeroed:

 # dd if=/dev/zero of=/dev/sdX bs=440 count=1

## Extra scenario in addition to disk-related scenes
As some readers might have already realised, the  core utility has a different command-line syntax compared to other utilities. Moreover, while supporting some unique features not found in other commodity utilities, several default behaviours it has are either less-ideal or potentially error-prone if applied to specific scenarios.  For that reason, users may want to use some alternatives that are better in some aspects in lieu of the dd core utility.

That said, it is still worth to note that since dd is a core utility, which is installed by default on Arch and many other systems, it is preferable to some alternatives or more specialised utilities if it is inconvenient to install a new package on your system.

To cover the two aspects that are addressed above, this section is dedicated to summarising the features of the  core utility that are rarely found in other commodity utilities — in a form that resembles the pacman/Rosetta article but with the quantity of examples being cut down to examine the features of dd (as denoted by i.e. or To-clause in "Tip:" box under subsection), either in practice or pseudocode.

## Patching a binary file, block-by-block in-place
It is not an uncommon practice to use dd as a feature-limited binary file patcher in an automated shell script as it supports:

* ing the output file by a given offset before writing.
* writing to an output file (without truncating the size of the output file by adding the  option).

Here is an example to modify the timestamp part of the first member in a  archive, which starts at the 49th byte of the file (or with an offset of  if you prefer hex notation):

 $ touch a-randomly-chosen-file
 $ bsdtar -cf example-modify-ts.cpio --format odc -- a-randomly-chosen-file

 $ printf '%011o' "$(date -d "2019-12-21 00:00:00" +%s)" | dd conv=notrunc of=example-modify-ts.cpio seek=48 oflag=seek_bytes

{{tip|In this feature grid (i.e.  with offset, with no truncation), instead of using dd, one may consider using a shell that supports to call  on shell-opened file descriptor if in case of:

* the input file of dd is a pipe connected with a program that utilize  system call, and the user want to avoid unnecessary userspace I/O of dd for a better performance
* or, to avoid frequently  in a shell script loop to reduce the performance penalty

Then it would be necessary to let that shell open the file descriptor at first, and perform some seeking operation on the file descriptor to assign this file descriptor as output end of corresponding utility that use  system call (or a shell builtin command does not forking, as in following example of ):{{hc|$ zsh|$ local +xr openToWriteFD
$ zmodload zsh/system
$ sysopen -wu openToWriteFD example-modify-ts.cpio
$ sysseek -u $openToWriteFD 48
$ printf '%011o' "$(date -d "2019-12-21 00:00:00" +%s)" >&${openToWriteFD}
...
$ : finally close the fd {openToWriteFD}>&-}}
}}

## Printing volume label of a VFAT filesystem image
To read the filesystem volume label of an VFAT image file, which should be in total length of 11 bytes that padded by ASCII spaces, with an offset of :

 $ truncate -s 36M empty-hole.img
 $ mkfs.fat -F 32 -n LabelMe empty-hole.img

 $ dd iflag=skip_bytes,count_bytes count=11 skip=$((0x047)) if=empty-hole.img | sed -e 's% *$%%'

{{tip|To transfer data from input (with an offset) to output within given length, in shell scripting, one may also consider  as a commodity alternative that use range notation instead.{{note|curl does not support seeking/skipping when input file is a device/pipe, another alternative  does support these operation on input file (incl. block device, excl. pipe and character device) but is less commodifying than curl:{{bc|$ socat -u -,seek=$((0x047)),readbytes=11 - &- | dd count=1 skip=1 status=none | inspect-tar-header-block

{{Tip|In addition to above feature grid, if input file shall be 'd by specific offset before streaming, and the output end of dd is a pipe connected with a program utilize , then, as an alternative, one may consider use:
* a shell with builtin seeking capability (as already mentioned as alternative in a previous subsection.)
* or, a Bourne-like shell (e.g. bash), with help of  for one-off  on shell-opened file descriptor,
and  (mentioned above) as in following bash example (assuming that file descriptor has not allocated in shell by  in bash at first):{{hc|$ bash|$ exec 9/dev/null
 125+1 records in
 125+1 records out
 512400 bytes (512 kB, 500 KiB) copied, 10.7137 s, 47.8 kB/s

When resuming an interrupted transfer like the above PoC, it is recommended to only rely on the readout of number of whole output blocks already copied, as denoted by the number before "+" sign.
