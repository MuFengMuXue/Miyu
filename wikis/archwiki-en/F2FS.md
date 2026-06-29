# F2FS

F2FS (Flash-Friendly File System) is a file system intended for NAND-based flash memory equipped with Flash Translation Layer. Unlike JFFS or UBIFS it relies on a flash-transition layer (FTL) to handle write distribution. It is supported from kernel 3.8 onwards.

An FTL is found in all flash memory with a SCSI/SATA/PCIe/NVMe interface opposed to bare NAND Flash and SmartMediaCards [http://www.linux-mtd.infradead.org/archive/tech/nand.html.

## Known issues
## fsck failures
F2FS has a weak fsck that can lead to data loss in case of a sudden power loss If power losses are frequent, consider an alternative file system.

## Long running fsck delays boot
If the kernel version has changed between boots, the fsck.f2fs utility will perform a full file system check which will take longer to finish[https://bbs.archlinux.org/viewtopic.php?id=245702.

This may be mitigated in the future thanks to a recent commit === GRUB support ===

While GRUB supports F2FS since version 2.0.4, it cannot correctly read its boot files from an F2FS partition that was created with the  flag enabled (for more details, see GRUB#Unsupported file systems).

## Creating a F2FS file system
This article assumes the device has partitions already setup.  Install .  Use  to format the target partition referred to as :

 # mkfs.f2fs -l mylabel -i -O extra_attr,inode_checksum,sb_checksum /dev/sdxY

## Compression
To use compression, include the  option. Example:

 # mkfs.f2fs -l mylabel -O extra_attr,inode_checksum,sb_checksum,compression /dev/sdxY

When mounting the filesystem, specify . Using  will cause all txt files to be compressed by default.

In order to tell F2FS to compress a file or a directory, use :

 $ chattr -R +c [FOLDER

## File-based encryption support
Since Linux 4.2, F2FS natively supports file encryption.  Encryption is applied at the directory level, and different directories can use different encryption keys.  This is different from both dm-crypt, which is block-device level encryption, and from eCryptfs, which is a stacked cryptographic filesystem.  To use F2FS's native encryption support, see the fscrypt article.  Create the file system with

  # mkfs.f2fs -l mylabel -O extra_attr,inode_checksum,sb_checksum,encrypt /dev/sdxY

or add encryption capability at a later time with .

## Mounting an F2FS file system
The file system can then be mounted manually or via other mechanisms:

 # mount /dev/sdxY /mnt/foo

## Recommended mount options
Since F2FS is designed to be used on flash devices, compression is a good idea. You have to enable it at  time.
A few mount options can be used to improve things slightly.

 # mount -o compress_algorithm=zstd:6,compress_chksum,atgc,gc_merge,lazytime /dev/sdxY /mnt/mountpoint

*  tells F2FS to use zstd for compression at level 6, which should give pretty good compression ratio.
*  tells the filesystem to verify compressed blocks with a checksum (to avoid corruption)
*  Enable better garbage collector, and enable some foreground garbage collections to be asynchronous.
:
*  Do not synchronously update access or modification times. Improves IO performance and flash durability.

## Implementation of discard
By default, F2FS is mounted using a hybrid TRIM mode which behaves as continuous TRIM.  This implementation creates asynchronous discard threads to alleviate long discarding latency among RW IOs.  It keeps candidates in memory, and the thread issues them in idle time As a result of this, users wanting periodic TRIM will need to implicitly set the  mount option in  or pass it to mount if mounting manually.

## Checking and repair
Checking and repairs to F2FS file systems are accomplished with  provided by . To check a file system, execute
 # fsck.f2fs /dev/sdxY

Depending on the result, see  for available switches to repair inconsistencies. For example:
 # fsck.f2fs -f /dev/sdxY

## Grow an F2FS file system
When the filesystem is unmounted, it can be grown if the partition is expanded. [https://lore.kernel.org/linux-f2fs-devel/1461630518-16944-1-git-send-email-jaegeuk@kernel.org/ Shrinking is not currently supported.

First use a partition tool to resize the partition: for example, suppose the output of the  command in the  console is the following:

 Number  Start   End     Size        File system     Name                  Flag
  1      1049kB  106MB   105MB       fat32           EFI system partition  boot, esp
  2      106MB   11,0GB  10,9GB      ext4
  3      11,0GB  12,3GB  1322MB      f2fs
  4      31,0GB  31,3GB  261MB       ext4

To resize the  partition to occupy all the space up to the fourth one, just give  and . Now expand the filesystem to fill the new partition using:

 # resize.f2fs /dev/sdxY

where  is the target F2FS volume to grow. See  for supported options.

## Troubleshooting
## Remounting impossible with some options
As alluded to in Fsck#Boot time checking, the kernel keeps file systems in a read-only state by default, and it is either explicitly needed to pass the  kernel parameter or have systemd remounting the filesystems as read-write with the .

When remounting the file system from a read-only state to a read-write state, the  steps can fail for multiple reasons, which will either leave the root file system read-only or make the system unable to boot with the error message:

 Failed to start Remount Root and Kernel File Systems.

If the  option is specified in the fstab file but has not been passed as a kernel parameter, the F2FS kernel module will not permit re-mounting with an added or cleared  optioneither:

* add the kernel parameter  to your boot loader configuration,
* add the kernel parameter  to your boot loader configuration,
* remove the  mount option from the fstab.

Since  6.2, a [https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/commit/?id=967eaad1fed5f6335ea97a47d45214744dc57925 check is made in the kernel to disable  when the file system is read-only, but it is the state of the file system before remounting that is checked. As explained in , either:

* add the kernel parameter  to your boot loader configuration,
* remove the  mount option from the fstab.

## Cannot set file attributes for '/var/log/journal'
If the error:

 Cannot set file attributes for '/var/log/journal', maybe due to incompatibility in specified attributes, previous=0x10001000, current=0x10001000, expected=0x10801000, ignoring.

is present in your journal, it can be safely ignored: it is due to systemd-tmpfiles trying to use the NOCOW file system feature that is not supported by F2FS.

To avoid the message, create:

Then do a daemon-reload.
