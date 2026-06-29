# Ext4

From Ext4 - Linux Kernel Newbies:
:Ext4 is the evolution of the most used Linux filesystem, Ext3. In many ways, Ext4 is a deeper improvement over Ext3 than Ext3 was over Ext2. Ext3 was mostly about adding journaling to Ext2, but Ext4 modifies important data structures of the filesystem such as the ones destined to store the file data. The result is a filesystem with an improved design, better performance, reliability, and features.

## Create a new ext4 filesystem
Install .

To format a partition do:

 # mkfs.ext4 /dev/partition

See  for more options.

## Bytes-per-inode ratio
From :

:mke2fs creates an inode for every bytes-per-inode bytes of space on the disk. The larger the bytes-per-inode ratio, the fewer inodes will be created.

Creating a new file, directory, symlink etc. requires at least one free inode. If the inode count is too low, no file can be created on the filesystem even though there is still space left on it.

Because it is not possible to change either the bytes-per-inode ratio or the inode count after the filesystem is created,  uses by default a rather low ratio of one inode every 16384 bytes (16 KiB) to avoid this situation.

However, for partitions with size in the hundreds or thousands of GB and average file size in the megabyte range, this usually results in a much too large inode number because the number of files created never reaches the number of inodes.

This results in a waste of disk space, because all those unused inodes each take up 256 bytes on the filesystem (this is also set in  but should not be changed). 256 * several millions = quite a few gigabytes wasted in unused inodes.

This situation can be evaluated by comparing the  and  figures provided by  and :

To specify a different bytes-per-inode ratio, use the  option which hints at the expected usage of the filesystem using types defined in . Among those types are the bigger  and  which offer more relevant ratios of one inode every 1 MiB and 4 MiB respectively. It can be used as such:

 # mkfs.ext4 -T largefile /dev/device

The bytes-per-inode ratio can also be set directly via the  option: e.g. use  for a 2 MiB ratio and   for a 6 MiB ratio.

## Reserved blocks
By default, 5% of the filesystem blocks will be reserved for the super-user, to avoid fragmentation and "allow root-owned daemons to continue to function correctly after non-privileged processes are prevented from writing to the filesystem" (from ).

For modern high-capacity disks, this is higher than necessary if the partition is used as a long-term archive or not crucial to system operations (like ). See this email for the opinion of ext4 developer Ted Ts'o on reserved blocks and this superuser answer for general background on this topic.

It is generally safe to reduce the percentage of reserved blocks to free up disk space when the partition is either:

* Very large (for example > 50G)
* Used as long-term archive, i.e., where files will not be deleted and created very often

The  option of ext4-related utilities allows to specify the percentage of reserved blocks.

To totally prevent reserving blocks upon filesystem creation, use:

 # mkfs.ext4 -m 0 /dev/device

To change it to 1% afterwards, use:

 # tune2fs -m 1 /dev/device

To set the number of reserved block space to an absolute size in gigabytes, use :

 # tune2fs -r $((ngigs * 1024**3 / blocksize)) /dev/device

 is the block size of the filesystem in bytes. This is almost always 4096; check to be sure:

The  syntax is for math expansion. This syntax works in  and , but it will not work in . For fish, this is the syntax:

 # tune2fs -r (math 'ngigs * 1024^3 / blocksize') /dev/device

These commands can be applied to currently-mounted filesystems and changes will take effect immediately. Use  to find the device name:

 # tune2fs -m 1 "$(findmnt -no SOURCE /the/mount/point)"

To query the current number of reserved blocks:

This is the number of blocks, so this has to be multiplied by the filesystem's block size to get the number of bytes or gigabytes: .

## Migrating from ext2/ext3 to ext4
## Mounting ext2/ext3 partitions as ext4 without converting
## Rationale
A compromise between fully converting to ext4 and simply remaining with ext2/ext3 is to mount the partitions as ext4.

Pros:

* Compatibility (the filesystem can continue to be mounted as ext3) &ndash; This allows users to still read the filesystem from other operating systems without ext4 support (e.g. Windows with ext2/ext3 drivers)
* Improved performance (though not as much as a fully-converted ext4 partition).[https://events.static.linuxfound.org/slides/2010/linuxcon_japan/linuxcon_jp2010_fujita.pdf

Cons:

* Fewer features of ext4 are used (only those that do not change the disk format such as multiblock allocation and delayed allocation)

## Procedure
# Edit  and change the 'type' from ext2/ext3 to ext4 for any partitions to mount as ext4.
# Re-mount the affected partitions.

## Converting ext2/ext3 partitions to ext4
## Rationale
To experience the benefits of ext4, an irreversible conversion process must be completed.

Pros:

* Improved performance and new features.[https://events.static.linuxfound.org/slides/2010/linuxcon_japan/linuxcon_jp2010_fujita.pdf

Cons:

* Partitions that contain mostly static files, such as a  partition, may not benefit from the new features. Also, adding a journal (which is implied by moving a ext2 partition to ext3/4) always incurs performance overhead.
* Irreversible (ext4 partitions cannot be 'downgraded' to ext2/ext3. It is, however, backwards compatible until extent and other unique options are enabled)

## Procedure
These instructions were adapted from Kernel documentation and a BBS thread.

In the following steps  denotes the path to the partition to be converted, such as .

# Back up all data on any ext3 partitions that are to be converted to ext4. A useful package, especially for root partitions, is .
# Edit  and change the 'type' from ext3 to ext4 for any partitions that are to be converted to ext4.
# Boot the live medium (if necessary). The conversion process with  must be done when the drive is not mounted. If converting a root partition, the simplest way to achieve this is to boot from some other live medium.
# Ensure the partition is not mounted
# If converting an ext2 partition, the first conversion step is to add a journal by running  as root; making it a ext3 partition.
# Run  as root. This command converts the ext3 filesystem to ext4 (irreversibly).
# Run  as root.
#* This step is necessary, otherwise the filesystem will be unreadable. This fsck run is needed to return the filesystem to a consistent state. It will find checksum errors in the group descriptors - this is expected. The  option asks fsck to force checking even if the file system seems clean. The  option may be used on top to "automatically repair" (otherwise, the user will be asked for input for each error).
# Recommended: mount the partition and run  as root.
#* Even though the filesystem is now converted to ext4, all files that have been written before the conversion do not yet take advantage of the extent option of ext4, which will improve large file performance and reduce fragmentation and filesystem check time. In order to fully take advantage of ext4, all files would have to be rewritten on disk. Use e4defrag to take care of this problem.
# Reboot

## Improving performance
## Disabling access time update
The ext4 file system records information about when a file was last accessed and there is a cost associated with recording it. See fstab#atime options for the  and related options.

## Increasing commit interval
The sync interval for data and metadata can be increased by providing a higher time delay to the  option.

The default 5 sec means that if the power is lost, one will lose as much as the latest 5 seconds of work.
It forces a full sync of all data/journal to physical media every 5 seconds. The filesystem will not be damaged though, thanks to the journaling.
The following fstab illustrates the use of :

## Turning barriers off
Ext4 enables write barriers by default. It ensures that file system metadata is correctly written and ordered on disk, even when write caches lose power. This goes with a performance cost especially for applications that use fsync heavily or create and delete many small files. For disks that have a write cache that is battery-backed in one way or another, disabling barriers may safely improve performance.

To turn barriers off, add the option  to the desired filesystem. For example:

## Disabling journaling
Disabling the journal with ext4 can be done with the following command on an unmounted disk:

 # tune2fs -O "^has_journal" /dev/sdXn

## Use the journal to optimize performance
The Fast commits for ext4 article introduction summarizes succinctly why and how the mount options  or  speed up overall ext4 performance, compared to the default  operation mode. In addition, the journaling itself can be sped up by adding the  mount option.

A further option is to to use a newer journal format, see #Enabling fast_commit.

## External journal device
If using the non-default  options, a dedicated device for the journal may also speed up file operations in some cases. For example, when a relatively slow device is used for the data itself and another (faster but smaller) device for the journal. To set up a separate journal device:

 # mke2fs -O journal_dev /dev/journal_device

To assign  as the journal of , use:

 # tune2fs -J device=/dev/journal_device /dev/ext4_device

Replace  with  if wanting to make a new filesystem on .

Add the  as a dependency of the  using the  mount option in :

This prevents issues if  needs any setup (e.g. it is encrypted).

{{Note|Both the  and the devnum of the journal device are saved to the ext4 filesystem. When loading the journal device, only the devnum is used, causing issues as the devnum changes when disks are rearranged. Linux will refuse to mount the filesystem if the devnum points to the wrong device, but the below workarounds may still be helpful:

Ignore the saved devnum and force loading of the journal by path using the  mount option:

 will look up the journal device using the  and fix the saved devnum if it goes out of sync. However, it will consider this as corruption and trigger an unnecessary full filesystem scan This can be disabled in 's [https://man.archlinux.org/man/e2fsck.conf.5.en config file:

{{hc|/etc/e2fsck.conf|2=
# PR_0_EXTERNAL_JOURNAL_HINT: Superblock hint for external superblock should be xxxx
0x000033 = {
    # Tell e2fsck that if this problem is encountered, it can be fixed but should
    # not be considered corruption, the filesystem should still be marked clean.
    not_a_fix = true
}
}}
}}

## Tips and tricks
## Using file-based encryption
Since Linux 4.1, ext4 natively supports file encryption, see the fscrypt article.  Encryption is applied at the directory level, and different directories can use different encryption keys.  This is different from both dm-crypt, which is block-device level encryption, and from eCryptfs, which is a stacked cryptographic filesystem.

## Enabling metadata checksums in existing filesystems
When a filesystem has been created with  1.43 (2016) or later, metadata checksums are enabled by default. Existing filesystems may be converted to enable metadata checksum support.

To read more about metadata checksums, see the [https://ext4.wiki.kernel.org/index.php/Ext4_Metadata_Checksums ext4 wiki.

First the partition needs to be checked and optimized using :

 # e2fsck -Df /dev/path/to/disk

Convert the filesystem to 64-bit:

 # resize2fs -b /dev/path/to/disk

Finally enable checksums support:

 # tune2fs -O metadata_csum /dev/path/to/disk

To verify:

## Maintenance when using LVM
The e2scrub tool checks metadata of the ext4 filesystem, if it is used in LVM logical volumes. The volume group must have 256MiB unallocated space for this check, because the tool creates a snapshot to check. As noted by the  manual the tool does not repair errors, but report them and marks the filesystem to require an e2fsck (see ) run prior to the next mount.

The check can be automated, for example by enabling the packaged  unit.

If the minimum 256MiB unallocated space is missing, see LVM#Resizing the logical volume and file system in one go.

## Enabling fast_commit
The ext4 "fast commits" feature introduces a new, lighter-weight journaling method.
It is expected to significantly increase the performance of the ext4 filesystem,To enable on the feature on a new filesystem, include  in the  file system options argument.

To enable the feature on an existing file system, run:

 # tune2fs -O fast_commit /dev/drivepartition

To query the current configuration:

 # tune2fs -l /dev/drivepartition | grep features

To disable the feature on an existing file system, run:

 # tune2fs -O '^fast_commit' /dev/drivepartition

## Enabling case-insensitive mode
ext4 can be used in case-insensitive mode, which can increase the performance of applications and games running in Wine. This feature does not affect the entire file system, only directories that have the case-insensitive attribute enabled.

First, enable the feature in the file system:

 # tune2fs -O casefold /dev/path/to/disk

Enable the case-insensitive attribute in any directory:

 $ chattr +F /mnt/partition/case-insensitive-directory

Note that the directory must be empty, and moving subdirectories from elsewhere will not cause them to inherit the attribute, so plan ahead accordingly.

## Resize filesystem
The  program can resize ext2, ext3, or ext4 file systems. It can be used to enlarge or shrink an unmounted file system located on device. To resize an ext4 filesystem to a specific size:

 # resize2fs /dev/partition size

If size parameter is not specified, it will default to the size of the partition.

Make sure to prepare the required partition size beforehand (in case of inflating) with your favorite partitioning tool.
