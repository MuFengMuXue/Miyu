# Btrfs

From the Btrfs Documentation:

:Btrfs is a modern copy on write (COW) file system for Linux aimed at implementing advanced features while also focusing on fault tolerance, repair and easy administration.

## Preparation
For user space utilities, install the  package that is required for basic operations.

If you need to boot from a Btrfs file system (i.e., your kernel and initramfs reside on a Btrfs partition), check if your boot loader supports Btrfs.

## File system creation
The following shows how to create a new Btrfs file system. To convert an Ext3/4 partition to Btrfs, see #Ext3/4 to Btrfs conversion. To use a partitionless setup, see #Partitionless Btrfs disk.

See  for more information.

## File system on a single device
To create a Btrfs file system on partition :

 # mkfs.btrfs -L mylabel /dev/partition

The Btrfs default nodesize for metadata is 16 KiB, while the default sectorsize for data is equal to page size and autodetected. To use a larger nodesize for metadata (must be a multiple of sectorsize, up to 64 KiB is allowed), specify a value for the  via the  switch as shown in this example using 32 KiB blocks:

 # mkfs.btrfs -L mylabel -n 32k /dev/partition

## Multi-device file system
Multiple devices can be used to create a RAID. Supported RAID levels include RAID 0, RAID 1, RAID 10, RAID 5 and RAID 6. Starting from kernel 5.5 RAID1c3 and RAID1c4 for 3- and 4- copies of RAID 1 level. The RAID levels can be configured separately for data and metadata using the  and  options respectively. By default, the data has one copy () and the metadata is mirrored (). This is similar to creating a JBOD configuration, where disks are seen as one file system, but files are not duplicated. See Using Btrfs with Multiple Devices for more information about how to create a Btrfs RAID volume.

 # mkfs.btrfs -d single -m raid1 /dev/part1 /dev/part2 ...

You must include either the  hook,  hook or the  hook in  in order to use multiple Btrfs devices in a pool. See the Mkinitcpio#Common hooks article for more information.

Once the file system is created, it is advised to run the following command to scan for multi-device Btrfs file systems and register them, allowing to mount the multi-device file system by specifying only one member:

 # btrfs device scan

See #RAID for advice on maintenance specific to multi-device Btrfs file systems.

## Profiles
Btrfs uses the concept of profiles to configure mirroring, parity, and striping. In standard RAID terminology, this is called RAID level. Profiles for metadata (the  option of ) and data (the  option of ) may be different for the same Btrfs file system.

Some notable profiles:

; single
: No mirroring, no striping, no parity, enables mapping several devices to a single file system, called  in mdadm terminology.
; raid0
: No mirroring, striping, no parity, enables parallel access between devices, but not limited to same-size devices like traditional mdadm RAID.
; raid1
: Mirroring, no striping, no parity, enables recovering from one drive failure.

## Configuring the file system
## Copy-on-Write (CoW)
By default, Btrfs uses copy-on-write for all files all the time. Writes do not overwrite data in place; instead, a modified copy of the block is written to a new location, and metadata is updated to point at the new location. See the Btrfs Sysadmin Guide section for implementation details, as well as advantages and disadvantages.

## Disabling CoW
To disable copy-on-write for newly created files in a mounted subvolume, use the  mount option. This will only affect newly created files. Copy-on-write will still happen for existing files. The  option also disables compression. See  for details.

To disable copy-on-write for single files/directories, do:

 $ chattr +C /dir/file

## Cases where CoW is still triggered
Copy-on-Write will still be triggered if a file with the NOCOW attribute (+C) has more than one reference (for example, a copy created via  using reflink or a snapshot made by Btrfs).

## Effect on copying
When using  to copy files, the NOCOW attribute is not determined by the source file, but by the destination path—either inherited from the directory or determined by whether the subvolume is mounted with the  option. Reflink copying is possible only if both the source and destination files either have or do not have the NOCOW attribute. The actual behavior depends on the  option, with three possible outcomes:

* With  (default): If the NOCOW attributes match, reflink is used; otherwise, a deep copy is made.
* With  (or ): If the NOCOW attributes match, reflink is used; if they differ, the operation fails.
* With : A deep copy is always performed.

For more information on the  option, refer to .

## Effect on snapshots
If a file has copy-on-write disabled (NOCOW) and a snapshot is taken, the first write to a file block after the snapshot will be a COW operation because the snapshot locks the old file blocks in place. However, the file will retain the NOCOW attribute and any subsequent writes to the same file block will be in-place until the next snapshot.

Frequent snapshots can reduce the effectiveness of NOCOW, as COW is still required on the first write. To avoid copy-on-write for such files altogether, put them in a separate subvolume and do not take snapshots of that subvolume.

## Compression
Btrfs supports transparent and automatic compression. This reduces the size of files as well as significantly increases the lifespan of flash-based media by reducing write amplification. See Fedora:Changes/BtrfsByDefault#Compression, and [https://pagure.io/fedora-btrfs/project/issue/36#comment-701551. It can also improve performance, in some cases (e.g. single thread with heavy file I/O), while obviously harming performance in other cases (e.g. multi-threaded and/or CPU intensive tasks with large file I/O). Better performance is generally achieved with the fastest compress algorithms, zstd and lzo, and some benchmarks provide detailed comparisons.

## Compression types
Btrfs supports the compression algorithms  (DEFLATE provided by zlib),  (LZO), and  (Zstandard implemented by zstd). LZO has no compression levels, whereas zlib and zstd have adjustable compression levels (zlib: 1-9; zstd: -15 to -1, 1-15, must be integers). Higher levels provide better compression but require more processing time. Changing the levels will affect CPU and I/O throughput differently, so they should be checked / benchmarked before and after changing. For more information about compression types, see .

## Enabling compression
## For filesystems
The  mount option enables automatically considering compression for every write to the filesystem, where  is either , , , or  (for no compression), and the optional  specifies the compression level (defaults to 3 when not specified or set to 0; not applicable for ). Using this option, Btrfs will check if compressing the first data block of a file write shrinks it. If it does, the entire write to that file will be compressed. If it does not, the file is marked as , and both the current write and all subsequent writes to that file will not be compressed This is done to prevent making the disk wait to start writing until all of the data to be written is fully given to Btrfs and compression is attempted.

Alternatively you can set the compression property on a btrfs subvolume and it will persist and apply regardless of how it is mounted, use the  where  can be  or  where  is the level of compression.

The  mount option can be used instead, which makes Btrfs check each data block of every write and decide whether to compress them individually. Empirical testing on multiple mixed-use systems showed that using  can significantly improve space savings (from 10% to 20%) compared to , but this causes (slightly) higher CPU usage and longer write times without purpose. However, forcing compression is against [https://btrfs.readthedocs.io/en/latest/Compression.html#incompressible-data official Btrfs guidelines.

Only files created or modified after adding either of the above mount options will be automatically compressed.

## For existing files
To apply compression to existing files, use the  command, where  is either ,  or . To specify the compression level, use the  option, otherwise the default level is used (not applicable for ). For example, to re-compress all files with  and compression level 1, run the following command:

 # btrfs -v filesystem defragment -r -czstd -L1 /

Using the above method to compress files is not persistent; other write operations will apply the original compression settings.

The following two methods can persistently enable compression for individual files:

 $ chattr +c file
 $ btrfs property set file compression zstd

The first command uses the legacy interface of file attributes inherited from the ext2 filesystem and is not flexible, defaulting to  compression algorithm. The second command can specify the compression algorithm, but specifying compression levels is not yet implemented, so the default level 3 is used (not applicable for ).

## View compression types and ratios
 takes a list of files or directories (or an entire Btrfs file system) and outputs the compression types used and actual compression ratios (compressed size/uncompressed size). Uncompressed size may not match the number given by other programs such as , because every extent is counted once and only once—even if it has multiple reflinks, or if parts of it are no longer used anywhere but have not been garbage collected.

The  option keeps it on a single file system, which is useful in situations like  to avoid it from attempting to access non-Btrfs subdirectories and failing the entire run.

## Subvolumes
"A Btrfs subvolume is not a block device (and cannot be treated as one) instead, a Btrfs subvolume can be thought of as a POSIX file namespace. This namespace can be accessed via the top-level subvolume of the file system, or it can be mounted in its own right." Each Btrfs file system has a top-level subvolume with ID 5. This subvolume cannot be removed or replaced by another subvolume. The top-level subvolume has path  on the file system and other subvolumes are nested below the top-level subvolume. However, subvolumes can be moved around in the file system and their path may change, whereas their ID cannot.

By default, the top-level subvolume is mounted when mounting the file system. Options allow to mount a specific subvolume instead.

A major use case for subvolumes are snapshots.

See the following links for more details:

* [https://btrfs.readthedocs.io/en/latest/Subvolumes.html Btrfs Documentation
* Btrfs Wiki SysadminGuide#Subvolumes
* Btrfs Wiki Trees

## Creating a subvolume
To create a subvolume, the Btrfs file system must be mounted.

 # btrfs subvolume create /path/to/subvolume

## Listing subvolumes
To see a list of all subvolumes of the filesystem that  belongs to:

 # btrfs subvolume list -t path

 triggers a more readable table view.

## Deleting a subvolume
To delete a subvolume:

 # btrfs subvolume delete /path/to/subvolume

If the subvolume contains other subvolumes that should be deleted, add the / option. Alternatively, a subvolume can be deleted like a regular directory (, ).

## Mounting subvolumes
Subvolumes can be mounted using the  or  mount options. One can mimic traditional file system partitions by creating various subvolumes under the top level of the file system and then mounting them at the appropriate mount points.

For example, the following mounts the top-level subvolume to  and creates two subvolumes named  and . When the top-level subvolume is unmounted, the new subvolumes are mounted to  and :

 # mount device /mnt/ -o subvolid=5
 # btrfs subvolume create /mnt/subvol_root/
 # btrfs subvolume create /mnt/subvol_home/
 # umount /mnt/
 # mount -o subvol=/subvol_root device /mnt/
 # mount -o subvol=/subvol_home --mkdir device /mnt/home/

Referencing a subvolume with the  mount option requires using the path relative to the top-level subvolume. This can be different from the path where the top-level subvolume is mounted.

See Snapper#Suggested filesystem layout, Btrfs SysadminGuide#Managing Snapshots, and SysadminGuide#Layout for example file system layouts using subvolumes.

## Mounting subvolume as root
To use a subvolume as the root mountpoint, either make it the default subvolume, or specify the subvolume via a kernel parameter using . Edit the root mountpoint in  and specify the mount option . Alternatively, the subvolume can be specified with its id,  as kernel parameter and  as mount option in . It is preferable to mount using , rather than the subvolid, as the subvolid may change when restoring #Snapshots, requiring a change of mount configuration, or else the system will not boot.

## Changing the default sub-volume
The default sub-volume is mounted if no  mount option is provided. To change the default subvolume, do:

 # btrfs subvolume set-default subvolume-id /

where subvolume-id can be found by listing.

Changing the default subvolume with  will make the top level of the file system inaccessible, except by use of the  or  mount options === Quota ===

The concept of disk quota has a long tradition in the Unix world. Traditional quotas are based on file ownership, controlling space usage by limiting the total size of all files owned by users. While this approach is straightforward for file management, it has limitations in directory-level restrictions, typically requiring partitioning at installation time and lacking dynamic adjustment capabilities. Btrfs adopts a different quota design philosophy from traditional Unix systems and does not support traditional user- or group-based quota functionality. This is because its modern storage features (such as #Snapshots, #Copy-on-Write (CoW), #Deduplication, and #Compression) make traditional quota space calculations extremely complex and inaccurate [https://btrfs.readthedocs.io/en/latest/Qgroups.html. As an alternative, Btrfs uses a subvolume-based quota mechanism, currently providing two implementation approaches — traditional #Quota groups (qgroups) and the newer #Simple quotas (squotas) (introduced in kernel 6.7 released in late 2023) to achieve similar space management effects. While this increases management complexity, it provides more flexible and precise storage control capabilities, allowing directory size limitations without partitioning and enabling dynamic quota adjustments.

## Quota groups (qgroups)
Btrfs's precise quota support is implemented through qgroups above subvolumes. Qgroups are represented using qgroupids in the format . Subvolumes have level 0, where  can be omitted, and the corresponding  is the subvolume ID. For example,  represents the qgroup of the top-level subvolume. Subvolume paths can also be used instead of the  representation. Qgroups form a tree hierarchy, but a qgroup can have multiple parent qgroups Leaf qgroups have level 0, corresponding directly to subvolumes. The  of all higher-level qgroups can be freely specified. Higher-level qgroups contain lower-level qgroups, and same-level groups cannot be nested, but level does not indicate nesting depth. For example, child qgroup  can be assigned to qgroup .

## Total referenced space and exclusively referenced space
Each qgroup primarily tracks two values: the amount of total referenced space and the amount of exclusively referenced space. Total referenced space refers to the storage space occupied by all data accessible from within the qgroup, while exclusively referenced space refers to the storage space occupied by data that is only referenced by subvolumes belonging to the qgroup (and not referenced by subvolumes outside the qgroup).

## Enabling/disabling qgroups
Use the following command to enable qgroups for the filesystem containing path:

 # btrfs quota enable path

Change  to  to disable qgroups.

## Creating/destroying qgroups
Level 0 qgroups corresponding to subvolumes are always automatically created. Even if subvolumes are created before enabling quotas, the corresponding qgroups will be automatically created when quotas are enabled. Similarly, when deleting subvolumes, the corresponding qgroups will be deleted and automatically disassociate from higher-level qgroups that originally contained these qgroups.

Use the following command to create qgroup qgroupid in the filesystem containing path:

 # btrfs qgroup create qgroupid path

Change  to  to destroy the qgroup. Destroying a qgroup is similar to using  to delete a directory — if the qgroup has child qgroups, relationships must be removed first; if only parent qgroups exist, relationships will be automatically removed.

## Assigning/removing child qgroups
Use the following command to assign src as the child qgroup of dst in the filesystem containing path, note that dst must be at a higher level than src:

 # btrfs qgroup assign src dst path

Change  to  to remove this relationship.

## Limiting/unlimiting qgroups
You can limit the total referenced space or exclusively referenced space of qgroups, or limit both simultaneously. For example, use the following command to limit the total referenced space of qgroupid to no more than 1GiB in the filesystem containing path:

 # btrfs qgroup limit 1G qgroupid path

If qgroupid is omitted, it attempts to interpret path as a subvolume path. Add the  option (after ) to limit exclusively referenced space instead. Change size to  to remove the limit.

## Listing qgroups
Use the following command to list all qgroups in the filesystem containing path:

 # btrfs qgroup show path

The "Path" column in the output may display some special values with the following meanings:

* : Qgroup corresponding to the top-level subvolume.
* : The subvolume corresponding to this qgroup has been deleted (its directory has been removed), but the subvolume metadata has not been completely cleaned up.

* : (Only applicable to #Simple quotas (squotas)) The subvolume corresponding to this qgroup has been completely deleted but related statistics are still retained. This is because simple quotas only attribute extents to the subvolume that first allocated them, and while that subvolume has been completely deleted, the extents are still referenced by other subvolumes.

According to your needs, you can add some display options (after ). Common options include:

* : Show parent qgroups.
* : Show child qgroups.
* : Show total referenced space limits.
* : Show exclusively referenced space limits.
* : Only list qgroups corresponding to the subvolume containing path.
* : Only list qgroups corresponding to the subvolume containing path and higher-level qgroups that contain these qgroups.

For more options, please refer to .

## Quota rescan
[https://btrfs.readthedocs.io/en/latest/btrfs-qgroup.html#quota-rescan Quota rescan reads the metadata of all extents in the filesystem and updates the statistics of each qgroup accordingly.

Btrfs qgroups can handle many complex extent sharing and unsharing scenarios (including deletion of subvolumes and child qgroups) while maintaining accurate counts of total referenced space and exclusively referenced space. However, when qgroup relationships change (manual assignment/removal of child qgroups), due to insufficient recorded data (only recording total referenced space and exclusively referenced space, without explicitly recording which extents belong to shared or exclusive), quota rescan across the entire filesystem is usually required. At this time, qgroups will be marked as "inconsistent", indicating a state that requires quota rescan.

The only exception in the current implementation is when a qgroup's total referenced space equals its exclusively referenced space, meaning all data is exclusive. In this case, when performing assign/remove operations on this subvolume, it only needs to add/subtract this qgroup's referenced space to/from the parent qgroup's total referenced space and exclusively referenced space simultaneously.

Starting from kernel version 4.19, manual assignment/removal of child qgroups automatically triggers quota rescan (when necessary). However, since quota rescan has high overhead, can only be performed once at a time, and this method cannot wait for the rescan to complete before returning, you can add the  option (after /) to avoid automatic triggering and manually trigger it later.

Use the following command to manually trigger quota rescan for the filesystem containing path:

 # btrfs quota rescan path

The command returns immediately. Add the  () option (after ) to wait for the rescan to complete (even if already started) before returning. Use the  () option to only wait for the currently running rescan to complete. Use the  () option to return current progress.

## Simple quotas (squotas)
Qgroups can handle many complex extent sharing and unsharing scenarios (including deletion of subvolumes and child qgroups) while maintaining accurate counts of total referenced space and exclusively referenced space. However, this flexibility comes at a cost: many computational operations are global in nature, meaning that when extent reference relationships change, they affect the statistics of all qgroups that reference the extent. This can lead to slower transaction commit speeds and unacceptable delays, especially when the number of snapshots increases dramatically.

To address this limitation of qgroups, Btrfs supports a second set of quota semantics: simple quotas (squotas). Squotas reuse the qgroup API and hierarchical structure model but do not track shared and exclusive usage. Instead, squotas attribute all extents to the subvolume that first allocated them. By introducing a small amount of new metadata records, this allows all accounting decisions to be completed locally in operations involving the allocation or release of data blocks themselves, completely avoiding complex and time-consuming reverse reference resolution processes.

Squotas need to be enabled at the filesystem level by simply adding the  () option (after ) to the enabling qgroups command. Note that if qgroups are already enabled, you need to first disable qgroups and then enable squotas, otherwise it will not take effect Due to its simple calculation method, squota mode does not need (and cannot) perform #Quota rescan. Apart from these two points, squotas operate exactly the same as qgroups, but the so-called "total referenced space" and "exclusively referenced space" displayed and limited are all values calculated through the method described above (attributing all extents to the subvolume that first allocated them). Since squotas need to record the subvolume that first allocated extents, they only take effect for extents written after enabling. If squotas are enabled on a non-empty filesystem, the statistics will be 0 when first enabled, so only by enabling squota limits on empty subvolumes and then writing data can you ensure accurate statistics.

## Commit interval
The resolution at which data are written to the file system is dictated by Btrfs itself and by system-wide settings. Btrfs defaults to a 30 seconds checkpoint interval in which new data are committed to the file system. This can be changed by appending the  mount option in  for the Btrfs partition.

 LABEL=arch64 / btrfs defaults,compress=zstd,commit=120 0 0

System-wide settings also affect commit intervals. They include the files under  and are out-of-scope of this wiki article. The kernel documentation for them is available at https://docs.kernel.org/admin-guide/sysctl/vm.html.

## SSD TRIM
A Btrfs file system is able to free unused blocks from an SSD drive supporting the TRIM command. Asynchronous discard support is available with mount option , and is enabled by default as of  6.2. Freed extents are not discarded immediately, but grouped together and trimmed later by a separate worker thread, improving commit latency.

Asynchronous discard can safely be used alongside periodic trim [https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/thread/MLZIPQUXMJFRVSFJS6B2ACDKTYNSX3AX/.

More information about enabling and using TRIM can be found in Solid state drive#TRIM.

## Usage
## Swap file
For general information about swap files, see Swap#Swap file.

To properly create a swap file on Btrfs, first create a subvolume to store the swap file, as snapshots cannot be created for that subvolume afterwards. For example, create the  subvolume:

 # btrfs subvolume create /swap

Create a 4 GiB swap file  in :

 # btrfs filesystem mkswapfile --size 4g --uuid clear /swap/swapfile

The  option specifies the swap file size, with a default of 2 GiB and minimum of 40 KiB.

Activate the swap file:

 # swapon /swap/swapfile

Finally, edit the fstab configuration to add an entry for the swap file:

For additional information, see fstab#Usage.

For more information about removing swap files and other details, see Swap#Swap file.

## Displaying used/free space
General linux userspace tools such as  will inaccurately report free space on a Btrfs partition as they do not account for both file and metadata usage. It is recommended to use  to query Btrfs partitions. For example, for a full breakdown of device allocation and usage stats:

 # btrfs filesystem usage /

Alternatively,  allows a quick check on usage of allocated space without the requirement to run as root:

 $ btrfs filesystem df /

See for more information.

The same limitations apply to tools which analyze space usage for some subset of the file system, such as  or , as they do not consider #Copy-on-Write (CoW) or transparent #Compression. Instead, see  and compsize for Btrfs-aware alternatives.

## Defragmentation
Btrfs supports online defragmentation through the mount option ; see . To manually defragment your root (not descending to subvolumes, mount points and directory symlinks), use:

 # btrfs filesystem defragment -r /

## RAID
Btrfs offers native "RAID" for #Multi-device file systems. Notable features which set Btrfs RAID apart from mdadm are self-healing redundant arrays and online balancing. See [https://archive.kernel.org/oldwiki/btrfs.wiki.kernel.org/index.php/Using_Btrfs_with_Multiple_Devices.html the Btrfs wiki page for more information. The Btrfs sysadmin page also has a section with some more technical background.

## Scrub
The Btrfs Wiki Glossary says that Btrfs scrub is "online file system checking tool. Reads all the data and metadata on the file system and uses checksums and the duplicate copies from RAID storage to identify and repair any corrupt data."

## Start manually
To start a (background) scrub on the file system which contains :

 # btrfs scrub start /

To check the status of a running scrub:

 # btrfs scrub status /

## Start with a service or timer
The  package brings the  unit for monthly scrubbing the specified mountpoint. Enable the timer with an escaped path, e.g.  for  and  for . You can use  to escape the path; see  for details.

You can also run the scrub by starting  (with the same encoded path). The advantage of this over  (as the root user) is that the results of the scrub will be logged in the systemd journal.

On large NVMe drives with insufficient cooling (e.g. in a laptop), scrubbing can read the drive fast enough and long enough to get it very hot. If you are running scrubs with systemd, you can easily limit the rate of scrubbing with the  option described in  by using a drop-in file.

## Balance
"A balance passes all data in the file system through the allocator again. It is primarily intended to rebalance the data in the file system across the devices when a device is added or removed. A balance will regenerate missing copies for the redundant RAID levels, if a device has failed." [https://btrfs.readthedocs.io/en/latest/Glossary.html See Upstream FAQ page.

On a single-device filesystem, a balance may be also useful for (temporarily) reducing the amount of allocated but unused (meta)data chunks. Sometimes this is needed for fixing "file system full" issues.

 # btrfs balance start --bg /
 # btrfs balance status /

## Snapshots
"A snapshot is simply a subvolume that shares its data (and metadata) with some other subvolume, using Btrfs's COW capabilities." See Btrfs Wiki SysadminGuide#Snapshots and the Btrfs documentation for details.

To create a snapshot:

 # btrfs subvolume snapshot source To create a readonly snapshot, add the  flag. To create a writable version of a readonly snapshot, simply create a snapshot of it.

## Send/receive
A subvolume can be sent to stdout or a file using the  command. This is usually most useful when piped to a Btrfs  command. For example, to send a snapshot named  (perhaps of a snapshot you made of  earlier) to , you would do the following:

 # btrfs send /root_backup | btrfs receive /backup

The snapshot that is sent must be readonly. The above command is useful for copying a subvolume to an external device (e.g. a USB disk mounted at  above).

The subvolume will be created on the receiving end. It does not need to be created manually.

Another example which creates: :

 # btrfs send --proto 2 --compressed-data '/mnt/arch/snapshots/@var' | btrfs receive '/mnt/arch-v2/subvolumes/'

The parameters  and  used in the example might be useful for more efficient sending (assumes compressed data).

You can also send only the difference between two snapshots. For example, if you have already sent a copy of  above and have made a new readonly snapshot on your system named , then to send only the incremental difference to , do:

 # btrfs send -p /root_backup /root_backup_new | btrfs receive /backup

Now, a new subvolume named  will be present in .

See [https://archive.kernel.org/oldwiki/btrfs.wiki.kernel.org/index.php/Incremental_Backup.html Btrfs Wiki's Incremental Backup page and #Incremental backup to external drive on how to use this for incremental backups and for tools that automate the process.

## Deduplication
Using copy-on-write, Btrfs is able to copy files or whole subvolumes without actually copying the data. However, whenever a file is altered, a new proper copy is created. Deduplication takes this a step further by actively identifying blocks of data which share common sequences and combining them into an extent with the same copy-on-write semantics.

Tools dedicated to deduplicate a Btrfs formatted partition include  and . One may also want to merely deduplicate data on a file based level instead using e.g. , ,  or . For an overview of available features of those programs and additional information, have a look at the upstream Wiki entry.

## Bees
Bees is a root daemon that deduplicates Btrfs filesystem on the block level, ignoring the actual layout of files and subvolumes. As a result, it can deduplicate files between different users without them noticing, also deduplicate between the system files and podman containers, and deduplicate identical parts of files that are partially different.

To run , install it and configure. One instance of bees works with a single filesystem, so to process multiple filesystems you need to run multiple instances of bees with different config files. In  create a copy of  with arbitrary name ending in .conf: . Edit it. You must provide the UUID of the filesystem you want to deduplicate (find it with  as root). You must also decide how much RAM this instance of Bees will take. The value affects the minimum size of duplicate blocks Bees will detect. See comments in the config file for examples. Write the value into DB_SIZE variable.

Start/enable the Bees , where the  qualifier is the UUID. See its logs with journalctl if needed.

## Resizing
You can grow a file system to the maximum space available on the device, or specify an exact size. Ensure that you grow the size of the device or logical volume before you attempt to increase the size of the file system.
When specifying an exact size for the file system on a device, either increasing or decreasing, ensure that the new size satisfies the following conditions:

* The new size must be greater than the size of the existing data; otherwise, data loss occurs.
* The new size must be equal to or less than the current device size because the file system size cannot extend beyond the space available.

To extend the file system size to the maximum available size of the device:

 # btrfs filesystem resize max /

To extend the file system to a specific size:

 # btrfs filesystem resize size /

Replace  with the desired size in bytes. You can also specify units on the value, such as K (kibibytes), M (mebibytes), or G (gibibytes). Alternatively, you can specify an increase or decrease to the current size by prefixing the value with a plus (+) or a minus (-) sign, respectively:

 # btrfs filesystem resize +size /
 # btrfs filesystem resize -size /

## Known issues
A few limitations should be known before trying.

## Encryption
Btrfs has no built-in encryption support, but there is an ongoing effort to incorporate encryption based on Fscrypt.

Users can however encrypt the partition before running , see dm-crypt/Encrypting an entire system. Another approach is stacked filesystem encryption.

## btrfs check issues
The tool  has known issues and should not be run without further reading; see section #btrfs check.

## Tips and tricks
## Partitionless Btrfs disk
Btrfs can occupy an entire data storage device, replacing the MBR or GPT partitioning schemes, using subvolumes to simulate partitions. However, using a partitionless setup is not required to simply create a Btrfs file system on an existing partition that was created using another method. There are some limitations to partitionless single disk setups:

* Cannot place other file systems on another partition on the same disk.
* Due to the previous point, having an ESP on this disk is not possible. Another device is necessary for UEFI boot.

To create a partitionless Btrfs disk, run the following command:

 # mkfs.btrfs /dev/sdX

For example, use  rather than . The latter would format an existing partition instead of replacing the entire partitioning scheme. Because the root partition is Btrfs, make sure  is compiled into the kernel, or put  into mkinitcpio.conf#MODULES and regenerate the initramfs.

Install the boot loader like you would for a data storage device with a Master Boot Record. See Syslinux#Manually or GRUB/Tips and tricks#Install to partition or partitionless disk. If your kernel does not boot due to , please add  in  and generate the grub configuration.

## Conversion
## Ext3/4 to Btrfs conversion
Boot from an install CD, then convert by doing:

 # btrfs-convert /dev/partition

Mount the partition and test the conversion by checking the files.  Be sure to change the  to reflect the change (type to  and fs_passno −the last field− to  as Btrfs does not do a file system check on boot). Also note that the UUID of the partition will have changed, so update fstab accordingly when using UUIDs.  into the system and rebuild your boot loader's menu list (see Install from existing Linux). If converting a root file system, while still chrooted, regenerate the initramfs or the system will not successfully boot.

After confirming that there are no problems, complete the conversion by deleting the backup  sub-volume. Note that you cannot revert back to ext3/4 without it.

 # btrfs subvolume delete /ext2_saved

Remember that some applications which were installed prior have to be adapted to Btrfs.

## NTFS to Btrfs conversion
NTFS can be converted using  or .

Unmount the target filesystem and run the conversion, the exact compression and checksum types can be specified:

 # ntfs2btrfs -c zstd -h crc32c /dev/partition

If everything works well after the conversion, you can delete the  image otherwise used for restoring the original filesystem.

## After conversion
There are some steps you can take after converting an existing filesystem into Btrfs.

Make file data more contiguous

 # btrfs filesystem defrag -v -r -f -t 32M /mnt/filesystem

#Balance to make Btrfs metadata more compact

## Corruption recovery
btrfs-check cannot be used on a mounted file system. To be able to use btrfs-check without booting from a live USB, add it to the initial ramdisk:

Regenerate the initramfs.

Then if there is a problem booting, the utility is available for repair.

See  for more information.

## Booting into snapshots
In order to boot into a snapshot, the same procedure applies as for mounting a subvolume as your root partition, as given in section mounting a subvolume as your root partition, because snapshots can be mounted like subvolumes.

* If using GRUB, you can automatically populate your boot menu with Btrfs snapshots when regenerating the configuration file with the help of  or .
* If using rEFInd, you can automatically populate your boot menu with Btrfs snapshots with the help of , after enabling .
* If using Limine, you can install , which automatically generates snapshot entries in your boot menu whenever your Snapper list changes after enabling . See Limine#Snapper snapshot integration for Btrfs for more information.

## Use Btrfs subvolumes with systemd-nspawn
See the systemd-nspawn#Use Btrfs subvolume as container root and systemd-nspawn#Use temporary Btrfs snapshot of container articles.

## Reducing access time metadata updates
Because of the copy-on-write nature of Btrfs, simply accessing files can trigger the metadata copy and writing. Reducing the frequency of access time updates may eliminate this unexpected disk usage and increase performance. See fstab#atime options for the available options.

## Incremental backup to external drive
The following packages use  and  to send backups incrementally to an external drive. Refer to their documentation to see differences in implementation, features, and requirements.

*
*
*

The following package allows backing up snapper snapshots to non-Btrfs file systems:

*

## Automatic snapshots
For the managing and automatic creation of Btrfs snapshot, one may use a snapshot manager such as Snapper, Timeshift or Yabsnap.

## Automatic notifications
Desktop notifications help you notice serious Btrfs issues immediately, offering better awareness compared to having no notifications at all.

 provides desktop notifications for the following events:

* Booting into any read-only snapshot or system.
* Btrfs warning, error, or fatal messages appearing in the dmesg log.

See https://gitlab.com/Zesko/btrfs-desktop-notification for more information and configuration.

## space cache v1 is being deprecated
If your Btrfs filesystem was created with older defaults, you may see a warning similar to this in your system logs:

To convert the Btrfs space cache from the older v1 format to the newer v2 format and resolve this warning,
you can either modify the mount options for the partition to include  in fstab,
or perform the conversion manually:

 # umount /dev/partition
 # mount /dev/partition -o rw,space_cache=v2 /mnt
 # umount /mnt

The result of the conerversation can be inspected in the systemd journal log, e.g.

## Troubleshooting
See the [https://btrfs.readthedocs.io/en/latest/trouble-index.html Btrfs Troubleshooting pages and Btrfs Problem FAQ for general troubleshooting.

## GRUB
## Partition offset
The offset problem may happen when you try to embed  into a partitioned disk. It means that it is OK to embed GRUB's  into a Btrfs pool on a partitionless disk (e.g. ) directly.

GRUB can boot Btrfs partitions, however the module may be larger than other file systems. And the  file made by  may not fit in the first 63 sectors (31.5KiB) of the drive between the MBR and the first partition. Up-to-date partitioning tools such as  and  avoid this issue by offsetting the first partition by roughly 1MiB or 2MiB.

## Long boot time
Sometimes a large (> 4TB) Btrfs volume can take a long time to mount, slowing down boots.
Changing the group tree to block group tree can help with that

 # btrfstune --convert-to-block-group-tree /dev/sdX

## Mounting timed out
Sometimes, especially with large RAID1 arrays, mounting might time out during boot with a journal message such as:

This can easily be worked around by providing a longer timeout via the systemd-specific mount option  in fstab. For example:

 UUID=xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx  /data  btrfs  rw,relatime,x-systemd.mount-timeout=5min  0 0

## BTRFS: open_ctree failed
As of November 2014, there seems to be a bug in systemd or mkinitcpio causing the following error on systems with multi-device Btrfs file system using the  hook in :

A workaround is to remove  from the  array in  and instead add  to the  array. Then regenerate the initramfs and reboot.

You will get the same error if you try to mount a raid array without one of the devices. In that case, you must add the  mount option to . If your root resides on the array, you must also add  to your kernel parameters.

As of August 2016, a potential workaround for this bug is to mount the array by a single drive only in , and allow Btrfs to discover and append the other drives automatically. Group-based identifiers such as UUID and LABEL appear to contribute to the failure. For example, a two-device RAID1 array consisting of 'disk1' and disk2' will have a UUID allocated to it, but instead of using the UUID, use only  in . For a more detailed explanation, see the following blog post.

Another possible workaround is to remove the  hook in mkinitcpio.conf and replace it with the  hook. In this case,  should not be in the  or  arrays.

See the original forums thread and  for further information and discussion.

## btrfs check
The  command can be used to check or repair an unmounted Btrfs file system. However, this repair tool is still immature and not able to repair certain file system errors even those that do not render the file system unmountable.

## Constant drive activity
Since the kernel version 6.2,   option is set by default. This has been reported to cause constant drive activity on some drives even while idle, as the discard queue is filled faster than it is processed. This can cause increased power usage, especially on NVMe-based drives.

As of kernel version 6.3, the default discard  has been changed from 100 to 1000 to address this issue. You can manually set it to a desired value on an old kernel version, e.g.

 # echo 1000 > /sys/fs/btrfs/uuid/discard/iops_limit

Where  is the UUID of the Btrfs file system. The limit of  will need to be tuned experimentally.

To set the parameter on boot, systemd-tmpfiles may be used, e.g. by creating the following file:

Alternatively, one can disable asynchronous discard altogether by mounting using the  mount option in fstab, and instead use Periodic TRIM.

## Device total_bytes should be at most X but found Y
If a drive has been moved from another computer or the order of devices has changed, and the difference in sizes reported is tiny (at most megabytes), it is possible HPA (Host Protected Area) is in effect.

To verify if HPA is enabled, use :

 # hdparm -N DEVICE

The output provides two numbers: the number of visible sectors and the actual number of sectors. If they differ, HPA is enabled.

If motherboard sets this forcefully and the firmware provides no option to turn that off, the only option is to shrink the affected file system.  This is most easily done on the original computer, or on any machine that does not apply HPA.

## No space left on device
The blog post Fixing Btrfs Filesystem Full Problems suggests and explains the following checks/steps:

# Clear space now (remove historical snapshots)
# Is your filesystem really full? Mis-balanced metadata and/or data chunks (run )
# Is your filesystem really full? Mis-balanced data chunks
# Is your filesystem really full? Mis-balanced metadata
# Balance cannot run because the filesystem is full (temporarily add a device such as USB key or loop device to the btrfs filesystem using  before running )

For more up-to-date instructions regarding ENOSPC ("Out of disk space"), see ENOSPC - No available disk space | Forza's Ramblings.
