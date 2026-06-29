# File systems

From Wikipedia:

:In computing, a file system or filesystem controls how data is stored and retrieved. Without a file system, information placed in a storage medium would be one large body of data with no way to tell where one piece of information stops and the next begins. By separating the data into pieces and giving each piece a name, the information is easily isolated and identified. Taking its name from the way paper-based information systems are named, each group of data is called a "file". The structure and logic rules used to manage the groups of information and their names is called a "file system".

Individual drive partitions can be set up using one of the many different available file systems. Each has its own advantages, disadvantages, and unique idiosyncrasies. A brief overview of supported file systems follows; the links are to Wikipedia pages that provide much more information.

## Types of file systems
See  for a general overview and Wikipedia:Comparison of file systems for a detailed feature comparison. File systems already loaded by the kernel or built-in are listed in , while all the installed modules can be seen with .

{| class="wikitable sortable"
|+ In-tree and FUSE file systems
! File system
! Creation command
! Userspace utilities
! Archiso ! Kernel documentation [https://docs.kernel.org/filesystems/index.html
! Notes
|-
| Btrfs
|
|
|
| btrfs.html
| Stability status
|-
| VFAT
|
|
|
| vfat.html
| Windows 9x file system. Commonly used for the EFI system partition, USB flash drives and SD cards.
|-
| rowspan="2" | exFAT
|
|
|
|
| Commonly used for USB flash drives and SD cards.
|-
|
|
|
| N/A (FUSE-based)
|
|-
| F2FS
|
|
|
| f2fs.html

| Flash-based devices. Cannot be shrunk.
|-
| ext3
|
|
|
| ext3.html
|
|-
| ext4
|
|
|
| ext4.html
|
|-
| HFS
|
|
|
| hfs.html
| Classic Mac OS file system
|-
| HFS+
|
|
|
| hfsplus.html
| macOS (8–10.12) file system
|-
| JFS
|
|
|
| jfs.html
|
|-
| JFFS2
|
|
|
|
|
|-
| NILFS2
|
|
|
| nilfs2.html
| Mostly intended for flash based devices. Does not support xattrs and ACLs.
|-
| rowspan="2" | NTFS
|
|
|
| ntfs3.html
| Windows NT file system. |-
|
|
|
| N/A (FUSE-based)
| FUSE driver with extended capabilities.
|-
| UDF
|
|
|
| [https://docs.kernel.org/filesystems/udf.html udf.html
| ISO/IEC 13346 file system for disc images and DVDs/Blu-rays. Write support is limited to UDF 2.01 and older. UDF 2.50 and 2.60 are supported as read-only.
|-
| XFS
|
|
|
|
xfs.html
xfs-delayed-logging-design.html
xfs-self-describing-metadata.html
| Cannot be shrunk
|}

{| class="wikitable sortable"
|+ Out-of-tree file systems
! File system
! Creation command
! Kernel patchset
! Userspace utilities
! Notes
|-
| Bcachefs
| bcachefs format
|
|
| Removed from the kernel on 6.18
|-
| APFS
|
|
|
| macOS (10.13 and newer) file system. Read-only, experimental write support. See also  FUSE version.
|-
| ReiserFS
|
|
|
| Removed from the kernel on 6.13.
|-
| Reiser4
|
|
|
|
|-
| ZFS
|
| ,
|
| OpenZFS port
|}

## Journaling
The ext3/4, HFS+, JFS, NTFS, ReiserFS, and XFS file systems use journaling. Journaling provides fault-resilience by logging changes before they are committed to the file system. In the event of a system crash or power failure, such file systems are faster to bring back online and less likely to become corrupted. The logging takes place in a dedicated area of the file system.

ext3/4 offer data-mode journaling, which can optionally log data in addition to the metadata. Data-mode journaling comes with a speed penalty, because it does two write operations: first to the journal and then to the disk. Therefore, data-mode journaling is not enabled by default. The trade-off between system speed and data safety should be considered when choosing the file system type and features.

In the same vein, Reiser4 offers configurable "transaction models": a special model called wandering logs, which eliminates the need to write to the disk twice; write-anywhere, a pure copy-on-write approach; and a combined approach called hybrid which heuristically alternates between the two.

File systems based on copy-on-write (also known as write-anywhere), such as Reiser4, Btrfs, Bcachefs and ZFS, by design operate on full atomicity and also provide checksums for both metadata and inline data (operations entirely occur, or they entirely do not, and in properly functioning hardware data does not corrupt due to operations half-occurring). Therefore, these file systems are by design much less prone to data loss than other file systems and have no need to use traditional journal to protect metadata, because they are never updated in-place. Although Btrfs still has a journal-like log tree, it is only used to speed-up fdatasync/fsync.

FAT, exFAT, ext2, and HFS provide neither journaling nor atomicity, They are for temporary or legacy use and not recommended for use when reliable storage is needed.

## FUSE-based file systems
See FUSE.

## Stackable file systems
*
*
*
*
*

## Read-only file systems
*
*
*

## Clustered file systems
*
*
*
*
*
*
*
*

## Shared-disk file system
*
*
*

## Identify existing file systems
To identify existing file systems, you can use lsblk:

An existing file system, if present, will be shown in the  column. If mounted, it will appear in the  column.

## Create a file system
File systems are usually created on a partition, inside logical containers such as LVM, RAID and dm-crypt, or on a regular file (see Wikipedia:Loop device). This section describes the partition case.

Before continuing, identify the device where the file system will be created and whether or not it is mounted. For example:

Mounted file systems must be unmounted before proceeding. In the above example an existing file system is on  and is mounted at . It would be unmounted with:

 # umount /dev/sda2

To find just mounted file systems, see #List mounted file systems.

To create a new file system, use . See #Types of file systems for the exact type, as well as userspace utilities you may wish to install for a particular file system.

For example, to create a new file system of type ext4 (common for Linux data partitions) on , run:

 # mkfs.ext4 /dev/sda1

The new file system can now be mounted to a directory of choice.

## Mount a file system
To manually mount a file system located on a device (e.g., a partition) to a directory, use . This example mounts  to .

 # mount /dev/sda1 /mnt

This attaches the file system on  at the directory , making the contents of the file system visible. Any data that existed at  before this action is made invisible until the device is unmounted.

fstab contains information on how devices should be automatically mounted if present. See the fstab article for more information on how to modify this behavior.

If a device is specified in  and only the device or mount point is given on the command line, that information will be used in mounting. For example, if  contains a line indicating that  should be mounted to , then the following will automatically mount the device to that location:

 # mount /dev/sda1

Or

 # mount /mnt

mount contains several options, many of which depend on the file system specified.
The options can be changed, either by:

* using flags on the command line with mount
* editing fstab
* creating udev rules
* compiling the kernel yourself
* or using file system–specific mount scripts (located at ).

See these related articles and the article of the file system of interest for more information.

## List mounted file systems
To list all mounted file systems, use :

 $ findmnt

findmnt takes a variety of arguments which can filter the output and show additional information. For example, it can take a device or mount point as an argument to show only information on what is specified:

 $ findmnt /dev/sda1

findmnt gathers information from , , and .

## Unmount a file system
To unmount a file system use . Either the device containing the file system (e.g., ) or the mount point (e.g., ) can be specified:

 # umount /dev/sda1

or

 # umount /mnt

## Troubleshooting
## "linux Structure needs cleaning"
Unmount the file system and run fsck on the problematic volume.
