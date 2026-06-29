# XFS

XFS is a high-performance journaling file system created by Silicon Graphics, Inc. XFS is particularly proficient at parallel IO due to its allocation group based design. This enables extreme scalability of IO threads, filesystem bandwidth, file and filesystem size when spanning multiple storage devices.

## Preparation
For XFS userspace utilities install the  package. It contains the tools necessary to manage an XFS file system.

## Creation
To create a new filesystem on device use:

 # mkfs.xfs device

In general, the default options are optimal for common use.Sample output:

## Checksumming
 3.2.0 introduced a new on-disk format (v5) that includes a metadata checksum scheme called [https://docs.kernel.org/filesystems/xfs/xfs-self-describing-metadata.html Self-Describing Metadata.
Based on CRC32, it provides additional protection against metadata corruption (e.g. on unexpected power losses). Checksums are enabled by default when using  3.2.3 or later, but can be disabled (necessary for read-write mounts on older kernels) using the  switch when calling :

 # mkfs.xfs -m crc=0 /dev/target_partition

The XFS v5 on-disk format is considered stable for production workloads starting in Linux Kernel 3.15.

## Free inode btree
Starting in Linux 3.16, XFS has added a btree that tracks free inodes. It is equivalent to the existing inode allocation btree with the exception that the free inode btree tracks inode chunks with at least one free inode. The purpose is to improve lookups for free inode clusters for inode allocation. It improves performance on aged filesystems i.e. months or years down the track when you have added and removed millions of files to/from the filesystem. Using this feature does not impact overall filesystem reliability level or recovery capabilities.

This feature relies on the new v5 on-disk format that has been considered stable for production workloads starting Linux Kernel 3.15. It does not change existing on-disk structures, but adds a new one that must remain consistent with the inode allocation btree; for this reason older kernels will only be able to mount read-only filesystems with the free inode btree feature.

The feature is enabled by default when using xfsprogs 3.2.3 or later. If you need a writable filesystem for older kernels, it can be disabled with the  switch when formatting an XFS partition. You will need  together:

 # mkfs.xfs -m crc=0,finobt=0 /dev/target_partition

or shortly (because  depends on ):

 # mkfs.xfs -m crc=0 /dev/target_partition

## Reverse mapping btree
The reverse mapping btree is at its core:

:a secondary index of storage space usage that effectively provides a redundant copy of primary space usage metadata. This adds some overhead to filesystem operations, but its inclusion in a filesystem makes cross-referencing very fast. It is an essential feature for repairing filesystems online because we can rebuild damaged primary metadata from the secondary copy.
:The feature graduated from EXPERIMENTAL status in Linux 4.16 and is production ready. However, online filesystem checking and repair is (so far) the only use case for this feature, so it will remain opt-in at least until online checking graduates to production readiness.

From :

:The reverse mapping btree maps filesystem blocks to the owner of the filesystem block. Most of the mappings will be to an inode number and an offset, though there will also be mappings to filesystem metadata. This secondary metadata can be used to validate the primary metadata or to pinpoint exactly which data has been lost when a disk error occurs.

See also and [https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/commit/?id=35a891be96f1f8e1227e6ad3ca827b8a08ce47ea for more information.

This feature is enabled by default for new filesystems as of xfsprogs 6.5.0.

## Big timestamps
Starting in Linux 5.10, XFS supports using refactored "timestamp and inode encoding functions to handle timestamps as a 64-bit nanosecond counter and bit shifting to increase the effective size. This now allows XFS to run well past the Year 2038 problem to now the Year 2486. Making a new XFS file-system with bigtime enabled allows a timestamp range from December 1901 to July 2486 rather than December 1901 to January 2038." The feature will also allow quota timer expirations from January 1970 to July 2486 rather than January 1970 to February 2106.

Big timestamps are enabled by default for new filesystems as of xfsprogs 5.15.

## Upgrading
Verify whether an existing filesystem has bigtime enabled with :

 # xfs_info / | grep bigtime
 ... bigtime=0 ...

With  5.11 and newer you can upgrade an existing (unmounted) filesystem with :

 # xfs_admin -O bigtime=1 device

Or with :

 # xfs_repair -c bigtime=1 device

While there, you may want to enable  as well (another new default).

## Performance
From XFS FAQ:

: The default values already used are optimised for best performance in the first place. mkfs.xfs will detect the difference between single disk and MD/DM RAID setups and change the default values it uses to configure the filesystem appropriately.
: In most cases, the only thing you need to consider for  is specifying the stripe unit and width for hardware RAID devices.

(see #Stripe size and width)

: For mount options, the only thing that will change metadata performance considerably is the  mount option. Increasing  reduces the number of journal IOs for a given workload. The trade off for this increase in metadata performance is that more operations may be "missing" after recovery if the system crashes while actively making modifications.

: As of kernel 3.2.12, the default i/o scheduler, CFQ, will defeat much of the parallelization in XFS.

Therefore for optimal performance, in most cases you can just follow #Creation.

## Stripe size and width
If this filesystem will be on a striped RAID you can gain significant speed improvements by specifying the stripe size to the  command.

XFS can sometimes detect the geometry under software RAID, but in case you reshape it or you are using hardware RAID see how to calculate the correct sunit,swidth values for optimal performance.

## Access time
On some filesystems you can increase performance by adding the  mount option to the  file. For XFS filesystems "the default atime behaviour is , which has almost no overhead compared to noatime but still maintains sane atime values. All Linux filesystems use this as the default now (since around 2.6.30), but XFS has used relatime-like behaviour since 2006, so no-one should really need to ever use noatime on XFS for performance reasons."See Fstab#atime options for more on this topic.

## Discard
Despite XFS supporting async discard[https://lwn.net/Articles/787272/ since kernel 4.7still recommends "that you use the fstrim application to discard unused blocks rather than the discard mount option because the performance impact of this option is quite severe."

See Solid state drive#Periodic TRIM.

## Defragmentation
Although the extent-based nature of XFS and the delayed allocation strategy it uses significantly improves the file system's resistance to fragmentation problems, XFS provides a filesystem defragmentation utility (xfs_fsr, short for XFS filesystem reorganizer) that can defragment the files on a mounted and active XFS filesystem. It can be useful to view XFS fragmentation periodically.

 improves the organization of mounted filesystems. The reorganization algorithm operates on one file at a time, compacting or otherwise improving the layout of the file extents (contiguous blocks of file data).

## Inspect fragmentation levels
To see how much fragmentation your file system currently has:

 # xfs_db -c frag -r /dev/partition

## Perform defragmentation
To begin defragmentation, use the  command:

 # xfs_fsr /dev/partition

## Deduplication
The reflink feature, available since kernel version 4.9 and enabled by default since  version 5.1.0, allows creating fast reflink'ed copies of files as well as deduplication after the fact, in the same way as btrfs:

## Reflink copies
Reflink copies initially use no additional space:

 $ cp --reflink bigfile1 bigfile2

Until either file is edited, and a copy-on-write takes place. This can be very useful to create snapshots of (large) files.

## Deduplication
Existing filesystems can be deduped using tools like  or  from .

## External XFS Journal
Using an external log (metadata journal) on for instance an SSD may be useful to improve performance [https://docs.oracle.com/en/operating-systems/oracle-linux/10/xfs/xfs-CreatinganXFSFileSystem.html#notable_xfs_feature_options. See  for details about the  parameter.

To reserve an external journal with a specified size when you create an XFS file system, specify the  option to the  command. If you omit the  parameter, a journal size based on the size of the file system is used. To mount the XFS file system so that it uses the external journal, specify the  option to the mount command.

## Sync interval
XFS has a dedicated sysctl variable for setting the writeback interval with a default value of 3000.

## Administration
## Resize
XFS can be resized online using :

 # xfs_growfs -D size /path/to/mnt/point

If  is omitted, the filesystem is automatically grown to the largest size possible, i.e. the size of the partition.

## Online metadata checking (scrub)
 asks the kernel to scrub all metadata objects in the XFS filesystem. Metadata records are scanned for obviously bad values and then cross-referenced against other metadata. The goal is to establish a reasonable confidence about the consistency of the overall filesystem by examining the consistency of individual metadata records against the other metadata in the filesystem. Damaged metadata can be rebuilt from other metadata if there exists redundant data structures which are intact.

Enable/start  to periodic check online metadata for all XFS filesystems.

## Repair
See Checking and Repairing an XFS File System, Which factors influence the memory usage of xfs_repair? and XFS Repair.

## Data rescue
Even when being mounted read-only with  an XFS file system's log will be replayed if it has not been unmounted cleanly.

There may be situations where a compromised XFS file system on a damaged storage device should be mounted read-only, so that files may be copied off it hopefully without causing further damage, yet it cannot be mounted because it has not been unmounted cleanly and is damaged to such an extent that the log cannot be replayed.
Also, consider that replaying the log means writing to the compromised file system, which might be a bad idea in itself.

To mount an XFS file system without writing to it in any way and without replaying the log, use .

## Undelete
 can recover (under certain conditions) deleted files on an unmounted or read-only mounted XFS filesystem.  See https://github.com/ianka/xfs_undelete for more information.

## Troubleshooting
## Root file system quota
XFS quota mount options (, , , etc.) fail during re-mount of the file system. To enable quota for root file system, the mount option must be passed to initramfs as a kernel parameter . Subsequently, it should not be listed among mount options in  for the root () filesystem.

## xfs_scrub_all fails if user "nobody" can not access the mountpoint
When running , it will launch  for each mounted XFS file system. The service is run as user , so if  can not navigate to the directory, it will fail with the error:

 xfs_scrub@mountpoint.service: Changing to the requested working directory failed: Permission denied
 xfs_scrub@mountpoint.service: Failed at step CHDIR spawning /usr/bin/xfs_scrub: Permission denied
 xfs_scrub@mountpoint.service: Main process exited, code=exited, status=200/CHDIR

To allow the service to run, change the permissions of the mountpoint so that user  has execute permissions.

## fsck.xfs fails in systemd-based initramfs
When using a mkinitcpio-generated systemd based initramfs without the  hook, you will see the following messages in the journal:

 systemd-fsckfsck: /usr/bin/fsck.xfs: execute failed: No such file or directory
 systemd-fsck[286: fsck failed with exit status 8.
 systemd-fsckIgnoring error.

This is because  is a shell script and requires  to execute.  is provided by the  hook, so the solution is to prepend it to the HOOKS array in . E.g.:

 HOOKS=(base systemd ... )
