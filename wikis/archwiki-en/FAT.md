# FAT

From Wikipedia:File Allocation Table:

:File Allocation Table (FAT) is a computer file system architecture and a family of industry-standard file systems utilizing it. The FAT file system is a legacy file system which is simple and robust. It offers good performance even in light-weight implementations, but cannot deliver the same performance, reliability and scalability as some modern file systems. It is, however, supported for compatibility reasons by nearly all currently developed operating systems for personal computers and many mobile devices and embedded systems, and thus is a well-suited format for data exchange between computers and devices of almost any type and age from 1981 up to the present.

## File system creation
To create a FAT filesystem, install .

 supports creating FAT12, FAT16 and FAT32; See Wikipedia:File Allocation Table#Variants for an explanation on their differences.  will select the FAT type based on the partition size. To explicitly create a certain type of FAT filesystem, use the  option. See  for more information.

Format a partition to FAT32:

 # mkfs.fat -F 32 /dev/partition

## Kernel configuration
Here is an example of the default mount configuration in the kernel:

A short description of the options:

* Language settings: ,
* All filenames to lower letters on a FAT partitions if enabled:
* Enables support of the FAT file systems: , ,
* Enables support of a FAT partitioned harddisks on x86 PCs:

If the partition type detected by mount is VFAT then it will run the  script.

## Writing to FAT32 as normal user
To write on a FAT32 partition, you must make a few changes to the fstab file.

The  option means that any user (even non-root) can mount and unmount the partition  ().  gives read-write access.

For example, if your FAT32 partition is on , and you wish to mount it to , then you would use:

Now, any user can mount it with:

 $ mount /mnt/fat32

And unmount it with:

 $ umount /mnt/fat32

Note that FAT does not support Linux file permissions. Each file will also appear to be executable. You may want to use the  option to only mark Windows executables (com, exe, bat) as executable. See  for more options.

## Detecting FAT type
If you need to know which type of FAT file system a partition uses, use the file command:

Alternatively you can use minfo from the  package:
