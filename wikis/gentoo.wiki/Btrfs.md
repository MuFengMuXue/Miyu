This page contains [[changes](https://wiki.gentoo.org/index.php?title=Btrfs&oldid=1427366&diff=1431964)] which are not marked for translation.

Other languages:

-   [Deutsch](https://wiki.gentoo.org/wiki/Btrfs/de "Btrfs (93% translated)")
-   [English]
-   [español](https://wiki.gentoo.org/wiki/Btrfs/es "Btrfs (22% translated)")
-   [français](https://wiki.gentoo.org/wiki/Btrfs/fr "Btrfs (24% translated)")
-   [italiano](https://wiki.gentoo.org/wiki/Btrfs/it "Btrfs (36% translated)")
-   [magyar](https://wiki.gentoo.org/wiki/Btrfs/hu "Btrfs (95% translated)")
-   [polski](https://wiki.gentoo.org/wiki/Btrfs/pl "Btrfs (6% translated)")
-   [português do Brasil](https://wiki.gentoo.org/wiki/Btrfs/pt-br "BTRFS (30% translated)")
-   [svenska](https://wiki.gentoo.org/wiki/Btrfs/sv "Btrfs (7% translated)")
-   [русский](https://wiki.gentoo.org/wiki/Btrfs/ru "Btrfs (57% translated)")
-   [中文（中国大陆）‎](https://wiki.gentoo.org/wiki/Btrfs/zh-cn "Btrfs (24% translated)")
-   [日本語](https://wiki.gentoo.org/wiki/Btrfs/ja "Btrfs (91% translated)")
-   [한국어](https://wiki.gentoo.org/wiki/Btrfs/ko "Btrfs (12% translated)")

**Resources**

[[]][Home](https://btrfs.readthedocs.io)

[[]][Userspace](https://git.kernel.org/cgit/linux/kernel/git/kdave/btrfs-progs.git)

[[]][Kernel](https://git.kernel.org/cgit/linux/kernel/git/mason/linux-btrfs.git/tree/fs/btrfs?id=HEAD)

[[]][Wikipedia](https://en.wikipedia.org/wiki/Btrfs "wikipedia:Btrfs")

[![Ohloh Logo](/images/thumb/c/c1/Ohloh-logo.png/30px-Ohloh-logo.png)][Open Hub](https://www.openhub.net/p/btrfs)

**Btrfs** is a copy-on-write (CoW) [filesystem](https://wiki.gentoo.org/wiki/Filesystem "Filesystem") for Linux aimed at implementing advanced features while focusing on fault tolerance, self-healing properties, and easy administration. Jointly developed at Oracle, Red Hat, Fujitsu, Intel, SUSE, STRATO, and many others, Btrfs is licensed under the [GPL](https://en.wikipedia.org/wiki/GNU_General_Public_License "wikipedia:GNU General Public License") and open for contribution from anyone.

## Contents

-   [[1] [Features]](#Features)
-   [[2] [Caveats]](#Caveats)
-   [[3] [Installation]](#Installation)
    -   [[3.1] [Kernel]](#Kernel)
        -   [[3.1.1] [Versions \<6.14.0]](#Versions_.3C6.14.0)
        -   [[3.1.2] [Versions \>=6.14.0]](#Versions_.3E.3D6.14.0)
        -   [[3.1.3] [Snippet]](#Snippet)
    -   [[3.2] [Emerge]](#Emerge)
-   [[4] [Usage]](#Usage)
    -   [[4.1] [Creation]](#Creation)
    -   [[4.2] [Labels]](#Labels)
    -   [[4.3] [Mount]](#Mount)
    -   [[4.4] [Converting ext\* based file systems]](#Converting_ext.2A_based_file_systems)
    -   [[4.5] [Defragmentation]](#Defragmentation)
    -   [[4.6] [Compression]](#Compression)
        -   [[4.6.1] [Compression level]](#Compression_level)
        -   [[4.6.2] [Adjust fstab for compression]](#Adjust_fstab_for_compression)
        -   [[4.6.3] [Compression ratio and disk usage]](#Compression_ratio_and_disk_usage)
    -   [[4.7] [Multiple devices (RAID)]](#Multiple_devices_.28RAID.29)
        -   [[4.7.1] [Creation]](#Creation_2)
        -   [[4.7.2] [Conversion]](#Conversion)
        -   [[4.7.3] [Addition]](#Addition)
        -   [[4.7.4] [Removal]](#Removal)
            -   [[4.7.4.1] [By device path]](#By_device_path)
            -   [[4.7.4.2] [By device ID]](#By_device_ID)
    -   [[4.8] [Resizing]](#Resizing)
    -   [[4.9] [Subvolumes]](#Subvolumes)
        -   [[4.9.1] [Create]](#Create)
        -   [[4.9.2] [List]](#List)
        -   [[4.9.3] [Remove]](#Remove)
        -   [[4.9.4] [Snapshots]](#Snapshots)
        -   [[4.9.5] [Mounting]](#Mounting)
    -   [[4.10] [Scrub]](#Scrub)
-   [[5] [Troubleshooting]](#Troubleshooting)
    -   [[5.1] [Filesystem check]](#Filesystem_check)
    -   [[5.2] [Multi device filesystem mount fails]](#Multi_device_filesystem_mount_fails)
    -   [[5.3] [Using with VM disk images]](#Using_with_VM_disk_images)
    -   [[5.4] [Clear the free space cache]](#Clear_the_free_space_cache)
    -   [[5.5] [Btrfs hogging memory (disk cache)]](#Btrfs_hogging_memory_.28disk_cache.29)
    -   [[5.6] [Mounting Btrfs fails, returning mount: unknown filesystem type \'btrfs\']](#Mounting_Btrfs_fails.2C_returning_mount:_unknown_filesystem_type_.27btrfs.27)
    -   [[5.7] [Btrfs root doesn\'t boot]](#Btrfs_root_doesn.27t_boot)
    -   [[5.8] [lsblk doesn\'t show mountpoint for all devices in btrfs RAID]](#lsblk_doesn.27t_show_mountpoint_for_all_devices_in_btrfs_RAID)
-   [[6] [See also]](#See_also)
-   [[7] [External resources]](#External_resources)
-   [[8] [References]](#References)

## [[] Features]

Ext4 is safe and stable and can handle large filesystems with extents, but why switch? While it is true that Btrfs is still considered experimental and is growing in stability, the time when Btrfs will become the default filesystem for Linux systems is getting closer. Some Linux distributions have already begun to switch to it with their current releases. Btrfs has a number of advanced features in common with ZFS, which is what made the ZFS filesystem popular with BSD distributions and NAS devices.

-   **Copy on Write (CoW) and snapshotting** - Make incremental backups painless even from a \"hot\" filesystem or virtual machine (VM).
-   **File level checksums** - Metadata for each file includes a checksum that is used to detect and repair errors.
-   **Compression** - Files may be compressed and decompressed on the fly, which speeds up read performance.
-   **Auto defragmentation** - The filesystems are tuned by a background thread *while* they are in use.
-   **Subvolumes** - Filesystems can share a single pool of space instead of being put into their own partitions.
-   **RAID** - Btrfs does its own RAID implementations so [LVM](https://wiki.gentoo.org/wiki/LVM "LVM") or [mdadm] are not required in to have RAID. Currently RAID 0, 1 and 10 are supported; RAID 5 and 6 are considered unstable.
-   **Partitions are optional** - While Btrfs can work with partitions, it has the potential to use raw devices ([/dev/\<device\>]) directly.
-   **Data deduplication** - There is limited data [deduplication](https://wiki.gentoo.org/wiki/Deduplication "Deduplication") support; however, deduplication will eventually become a standard feature in Btrfs. This enables Btrfs to save space by comparing files via binary diffs.
-   **Quotas** - Btrfs offers quota support, which allows for grouping of subvolumes in quotas.

** Tip**\
For an up-to-date and somewhat exhaustive listing of features see the [upstream wiki\'s status page](https://btrfs.readthedocs.io/en/latest/Status.html). Not all features are sufficiently mature for wide use though.

Down the road, new clustered filesystems will readily take advantage of Btrfs with its copy on write and other advanced features for their object stores. [Ceph](https://wiki.gentoo.org/wiki/Ceph "Ceph") is one example of a clustered filesystem that looks very promising, and can take advantage of Btrfs.

** Warning**\
Btrfs is said to be a stable and well-tested single-disk filesystem and ext4 replacement, but caution is advised when using advanced features such as Btrfs-RAID.^[\[1\]](#cite_note-arstechnica_examining-btrfs_2021-1)^

## [[] Caveats]

Btrfs can counter-intuitively fail filesystem operations with ENOSPC when [df] reports free space due to internal fragmentation (free space pinned by DATA + SYSTEM chunks, but needed in METADATA chunks).

Additionally, a single 4K reference to a 128M extent inside Btrfs can cause free space to be present, but unavailable for allocations. This can also cause Btrfs to return ENOSPC when free space is reported by [df].

One workaround when the system is out of space is to add a spare, non-memory, block device and finish rebalancing while powered on. Another way is to remove or delete more than 1GB of files and snapshots where BTRFS may attempt to start rebalancing. Defragmenting BTRFS when disks are out of space may increase data to be larger than before and is therefore discouraged. Once free space is available, consider periodically running `btrfs balance start -dusage=20 /` with values of 20 or more (lower is quicker) often.

Installing [[[sys-fs/btrfsmaintenance]](https://packages.gentoo.org/packages/sys-fs/btrfsmaintenance)[]] and configuring the scripts to run periodically can help to reduce the possibility of ENOSPC issues by rebalancing Btrfs, but it will not eliminate the risk of ENOSPC when free space is present. Some workloads will never hit ENOSPC while others will. If the risk of ENOSPC in production is unacceptable, the user should use something else. If using Btrfs, be certain to avoid configurations known to have issues.

With the exception of ENOSPC, information on the issues present in Btrfs in the latest kernel branches is available at the [btrfs status page](https://btrfs.readthedocs.io/en/latest/Status.html).

## [[] Installation]

### [[] Kernel]

In order for the Linux kernel to support Btrfs, the filesystem has to be enabled:

#### [][[] Versions \<6.14.0]

[KERNEL] **Enable Btrfs and CRC32c hardware acceleration**

    File systems  --->
       <*> Btrfs filesystem support Search for <code>CONFIG_BTRFS_FS</code> to find this item.
    -*- Cryptographic API --->
       Accelerated Cryptographic Algorithms for CPU (x86) --->
           <*> CRC32c (SSE4.2/PCLMULQDQ) Search for <code>CONFIG_CRYPTO_CRC32C_INTEL</code> to find this item.

#### [][[] Versions \>=6.14.0]

[KERNEL] **Enable Btrfs and CRC32c hardware acceleration**

    File systems  --->
       <*> Btrfs filesystem support Search for <code>CONFIG_BTRFS_FS</code> to find this item.
    Library routines --->
       [*] Enable optimized CRC implementations Search for <code>CONFIG_CRC_OPTIMIZATIONS</code> to find this item.

** Note**\
Btrfs uses checksum algorithms; if there is no hardware acceleration, then it will use the generic software implementation resulting in increased system resource utilization.

[man 5 btrfs] states that we can check if Btrfs is using an accelerated version via:

`user `[`$`]`cat /sys/fs/btrfs/<UUID of partition formatted with btrfs>/checksum`

    crc32c (crc32c-generic)

If the result is `(*-generic)`, Btrfs is using the generic software implementation; this could be because the [btrfs] kernel module gets loaded **before** the related checksum kernel module. To fix this, ensure that the checksum module is loaded before [btrfs]; this can be done via:

-   Making the checksum module built-in (`<*>` instead of `<M>`).

<!-- -->

-   Adding the module to an [initramfs](https://wiki.gentoo.org/wiki/Initramfs "Initramfs") (this can be done automatically with [Dracut](https://wiki.gentoo.org/wiki/Dracut "Dracut")).

Once we\'ve made our changes, we can check again:

`user `[`$`]`cat /sys/fs/btrfs/<UUID of partition formatted with btrfs>/checksum`

    crc32c (crc32c-x86)

The result might vary, but the important part is that it does **\*NOT\*** say `(*-generic)`!

#### [[] Snippet]

[FILE] **`/etc/kernel/config.d/btrfs-linux6-1-111.config`**

    CONFIG_BTRFS_FS=y
    CONFIG_XOR_BLOCKS=y
    CONFIG_RAID6_PQ=y
    CONFIG_RAID6_PQ_BENCHMARK=y
    CONFIG_ZSTD_COMPRESS=y

### [[] Emerge]

To work with the [[[sys-fs/btrfs-progs]](https://packages.gentoo.org/packages/sys-fs/btrfs-progs)[]] utilities package issue:

`root `[`#`]`emerge --ask sys-fs/btrfs-progs`

## [[] Usage]

** Tip**\
Consider setting up [[[sys-fs/btrfsmaintenance]](https://packages.gentoo.org/packages/sys-fs/btrfsmaintenance)[]] to handle regular balancing, defrag, trimming, and scrubbing.

Typing long Btrfs commands can quickly become a hassle. Each command (besides the initial [btrfs] command) can be reduced to a very short set of instructions. This method is helpful when working from the command line to reduce the amount of characters typed.

For example, to defragment a filesystem located at [/], the following shows the long command:

`root `[`#`]`btrfs filesystem defragment -v / `

Shorten each of the longer commands after the [btrfs] command by reducing them to their unique, shortest prefix. In this context, unique means that no *other* [btrfs] commands will match the command at the command\'s shortest length. The shortened version of the above command is:

`root `[`#`]`btrfs fi de -v / `

No other [btrfs] commands start with `fi`; `filesystem` is the only one. The same goes for the `de` sub-command under the `filesystem` command.

### [[] Creation]

** Warning**\
The [mkfs.btrfs] command irreversibly destroys any content of the partition it is told to format. Please be sure the correct drive and partition have been selected *before* running any [mkfs] command!

To create a Btrfs filesystem on the [/dev/sdXN] partition:

`root `[`#`]`mkfs.btrfs /dev/sdXN`

In the example above, replace `N` with the partition number and `X` with the disk letter that is to be formatted. For example, to format the third partition of the first drive in the system with Btrfs, run:

`root `[`#`]`mkfs.btrfs /dev/sda3`

** Important**\
The last number column in [/etc/fstab] should be `0` for all Btrfs partitions. [fsck.btrfs] and [btrfsck] should not be run during each system boot.

### [[] Labels]

Labels can be added to Btrfs filesystems, making mounting and organization easier.

** Note**\
Labels are generally less unique than UUIDs, but setting labels like *rootfs* for [/], and *homedir* for [/home] can help with organization.

** Warning**\
If multiple filesystems with the same label exist on a system, the first labeled system in the fstab, or the first returned by [blkid] will be mounted. It is generally best to avoid depending on this behavior, so unique labels should be used.

Labels can be added to a Btrfs filesystem after it has been created by using:

`root `[`#`]`btrfs filesystem label /dev/sda1 rootfs`

Labels can be added when the Btrfs filesystem is created with:

`root `[`#`]`mkfs.btrfs -L rootfs /dev/sda1`

### [[] Mount]

After creation, filesystems can be mounted in several ways:

-   [[mount](https://wiki.gentoo.org/wiki/Mount "Mount")] - Manual mount.
-   [[/etc/fstab](https://wiki.gentoo.org/wiki//etc/fstab "/etc/fstab")] - Defining mount points in [/etc/fstab] enables automatic mounts on system boot.
-   [Removable media](https://wiki.gentoo.org/wiki/Removable_media "Removable media") - Automatic mounts on demand (useful for USB drives).
-   [AutoFS](https://wiki.gentoo.org/wiki/AutoFS "AutoFS") - Automatic mount on filesystem access.

### [][[] Converting ext\* based file systems]

** Warning**\
Use of this tool is discouraged. It\'s not well-tested and it creates an \'unnatural\' state which doesn\'t occur with a fresh btrfs partition which may expose bugs.

It is possible to convert ext2, ext3, and ext4 filesystems to Btrfs using the [btrfs-convert] utility.

The following instructions only support the conversion of filesystems that are unmounted. To convert the root partition, boot to a system rescue disk (SystemRescueCD works nicely) and run the conversion commands on the root partition.

First, be sure the mount point is unmounted:

`root `[`#`]`umount `*`<mounted_device>`*

Check the integrity of the filesystem using the appropriate [fsck] tool. In the next example, the filesystem is ext4:

`root `[`#`]`fsck.ext4 -f `*`<unmounted_device>`*

Use [btrfs-convert] to convert the ext\* formatted device into a Btrfs-formatted device:

`root `[`#`]`btrfs-convert `*`<unmounted_device>`*

Be sure to edit [/etc/fstab] after the device has been formatted to change the filesystem column from ext4 to Btrfs:

[FILE] **`/etc/fstab`Changing ext4 to btrfs**

    <device>   <mountpoint>  btrfs  defaults  0 0

### [[] Defragmentation]

** Warning**\
Defragmenting breaks up ref-links between files and their COW copies^[\[2\]](#cite_note-2)^ and thus may increase space usage considerably. Make sure to have enough free space available and not too many snapshots on the drive as full Btrfs partitions can get really slow.

Another feature of Btrfs is online defragmentation. To defragment a root Btrfs filesystem, run:

`root `[`#`]`btrfs filesystem defragment -r -v /`

The `autodefrag` mount option sets the default behavior to online defragmentation.

### [[] Compression]

Btrfs supports transparent compression using the zlib, lzo, and zstd (v5.1.0)^[\[3\]](#cite_note-3)^ compression algorithms.

It is possible to compress specific files using the file attributes:

`user `[`$`]`chattr +c <`*`filename`*`> [<`*`filename`*`> ...]`

or

`user `[`$`]`btrfs prop set <`*`filename`*`> compression <`*`type`*`>`

where `type` is one of zlib, lzo, and zstd. When applied to a directory, all files and subdirectories created *afterwards* will be compressed.

The `compress` mount option sets the default behavior to compress all the newly created files. To re-compress the whole filesystem using lzo compression run the following command:

`root `[`#`]`btrfs filesystem defragment -r -v -clzo /`

Depending on the CPU and disk performance, using lzo compression could improve the overall throughput.

As alternatives to lzo it is possible to use the zlib or zstd compression algorithms. Zlib is slower but has a higher compression ratio, whereas zstd has a good ratio between the two^[\[4\]](#cite_note-4)^.

To force zlib compression across the whole filesystem:

`root `[`#`]`btrfs filesystem defragment -r -v -czlib /`

Substitute zstd for zlib in the example above to activate zstd compression.

** Note**\
Compression can *not* be applied to subvolumes; the mount option affects the *entire* filesystem. [\[1\]](https://fedoraproject.org/wiki/Changes/BtrfsTransparentCompression#Q:_I_want_compression_only_on_.27.2F.27_and_not_on_.27.2Fhome.27.2C_can_I_just_modify_fstab.3F) For that purpose one has to compress directories.

#### [[] Compression level]

zlib compression can be set by levels 1-9 and zstd can be set to levels 1-15. For example, to set zlib to maximum compression at mount time:

`root `[`#`]`mount -o compress=zlib:9 /dev/sdXY /path/to/btrfs/mountpoint`

Or to set minimal compression:

`root `[`#`]`mount -o compress=zlib:1 /dev/sdXY /path/to/btrfs/mountpoint`

Or adjust compression by remounting:

`root `[`#`]`mount -o remount,compress=zlib:3 /path/to/btrfs/mountpoint`

The compression level should be visible in [/proc/mounts], or by checking the most recent [dmesg] output using the following command:

`root `[`#`]`dmesg | grep -i btrfs `

    [    0.495284] Btrfs loaded, crc32c=crc32c-intel
    [ 3010.727383] BTRFS: device label My Passport devid 1 transid 31 /dev/sdd1
    [ 3111.930960] BTRFS info (device sdd1): disk space caching is enabled
    [ 3111.930973] BTRFS info (device sdd1): has skinny extents
    [ 9428.918325] BTRFS info (device sdd1): use zlib compression, level 3

#### [[] Adjust fstab for compression]

Once a drive has been remounted or adjusted to compress data, be sure to add the appropriate modifications to the [/etc/fstab] file. In this example, the device is set to noatime and forced zstd level 1 for higher data throughput^[\[5\]](#cite_note-5)^ at mount time:

[FILE] **`/etc/fstab`Add Btrfs compression for zstd**

    /dev/sdb                /srv            btrfs           defaults,noatime,compress-force=zstd:1,rw     0 0

#### [[] Compression ratio and disk usage]

The usual userspace tools for determining used and free space like [du] and [df] may provide inaccurate results on a *Btrfs* partition due to inherent design differences in the way files are written compared to, for example, *ext2/3/4*^[\[6\]](#cite_note-6)^.

It is therefore advised to use the du/df alternatives provided by the Btrfs userspace tool `btrfs filesystem`. In addition, the [compsize] tool found in the [sys-fs/compsize](https://packages.gentoo.org/packages/sys-fs/compsize) package can be helpful in providing additional information regarding compression ratios and the disk usage of compressed files. The following are example uses of these tools for a Btrfs partition mounted under [/media/drive].

`user `[`$`]`btrfs filesystem du -s /media/drive `

         Total   Exclusive  Set shared  Filename
     848.12GiB   848.12GiB       0.00B  /media/drive/

`user `[`$`]`btrfs filesystem df /media/drive `

    Data, single: total=846.00GiB, used=845.61GiB
    System, DUP: total=8.00MiB, used=112.00KiB
    Metadata, DUP: total=2.00GiB, used=904.30MiB
    GlobalReserve, single: total=512.00MiB, used=0.00B

`user `[`$`]`compsize /media/drive `

    Processed 2262 files, 112115 regular extents (112115 refs), 174 inline.
    Type       Perc     Disk Usage   Uncompressed Referenced
    TOTAL       99%      845G         848G         848G
    none       100%      844G         844G         844G
    zlib        16%      532M         3.2G         3.2G

### [][[] Multiple devices (RAID)]

Btrfs can be used with multiple block devices in order to create RAIDs. Using Btrfs to create filesystems that span multiple devices is much easier than creating using [mdadm], since there is no initialization time needed for creation.

Btrfs handles data and metadata separately. This is important to keep in mind when using a multi-device filesystem. It is possible to use separate profiles for data and metadata block groups. For example, metadata could be configured across multiple devices in RAID1, while data could be configured to RAID5. This profile is possible when using three or more block devices, since RAID5 requires a minimum of 3 block devices.

This type of profile offers the benefit of redundancy for metadata on each device and striping for data across devices, which increases read speeds. The drawback of this profile is more space than necessary is used for metadata, and write speeds are reduced for data blocks, since RAID5 uses a parity bit.

#### [[] Creation]

The simplest method is to use the entirety of unpartitioned block devices to create a filesystem spanning multiple devices. For example, to create a filesystem in RAID1 mode across two devices:

`root `[`#`]`mkfs.btrfs -m raid1 -d raid1 `*`<device1>`*` `*`<device2>`*

#### [[] Conversion]

Converting between RAID profiles is possible with the [balance] sub-command. For example, say three block devices are presently configured for RAID1 and mounted at [/srv]. It is possible to convert the data in this profile from RAID1 to RAID5 with the following command:

`root `[`#`]`btrfs balance start -dconvert=raid5 --force /srv`

Conversion can be performed while the filesystem is online and in use. Possible RAID modes in Btrfs include RAID0, RAID1, RAID5, RAID6, and RAID10. See the [upstream Btrfs wiki](https://btrfs.wiki.kernel.org/index.php/Using_Btrfs_with_Multiple_Devices) for more information.

** Warning**\
It is currently not safe to use the RAID 5 or 6 modes^[\[7\]](#cite_note-7)^. RAID 5 and 6 modes have seen some fixes^[\[8\]](#cite_note-8)^ in Linux 4.12, but overall status is still marked as **unstable**.^[\[9\]](#cite_note-9)[\[10\]](#cite_note-10)^. Users who want to use RAID5 or RAID6 functionality of Btrfs are encouraged to check the [Btrfs status page](https://btrfs.readthedocs.io/en/latest/Status.html) for stability status of said modes before utilizing the modes.

#### [[] Addition]

Additional devices can be added to existing multi device file systems. Follow the removal section below.

A riskier, but faster, alternative to safely removing a device is to shut the system down (or if the system supports hot swappable drives, at least unmount the filesystem), physically disconnect and remove the device that is to be replaced, substituted and connect the new device in it\'s place, power up the system (if necessary).

Note: Systems that will be power cycled will have the multi device filesystem fail to mount, since a device has been physically removed from the pool.

Once the system is booted, mount the multi-device filesystem with [mount -odegraded], then perform the following steps on adding a new device.

`root `[`#`]`mount -odegraded /srv `

`root `[`#`]`btrfs device add --force /dev/sdd /srv `

After the device has been re-added it is then necessary to re-balance the filesystem to be sure data is spanned across the newly added device:

`root `[`#`]`btrfs balance start /srv`

#### [[] Removal]

##### [[] By device path]

Block devices (disks) can be removed from multi-device filesystems using the [btrfs device remove] subcommand:

`root `[`#`]`btrfs device remove /dev/sde /srv`

##### [[] By device ID]

Use the usage subcommand to determine the device IDs:

`root `[`#`]`btrfs device usage /srv`

    /dev/sdb, ID: 3
       Device size:             1.82TiB
       Device slack:              0.00B
       Data,RAID1:             25.00GiB
       Data,RAID5:            497.00GiB
       Data,RAID5:              5.00GiB
       Metadata,RAID5:         17.00GiB
       Metadata,RAID5:        352.00MiB
       System,RAID5:           32.00MiB
       Unallocated:             1.29TiB

    /dev/sdc, ID: 1
       Device size:             1.82TiB
       Device slack:              0.00B
       Data,RAID1:             25.00GiB
       Data,RAID5:            497.00GiB
       Data,RAID5:              5.00GiB
       Metadata,RAID5:         17.00GiB
       Metadata,RAID5:        352.00MiB
       System,RAID5:           32.00MiB
       Unallocated:             1.29TiB

    /dev/sdd, ID: 4
       Device size:             1.82TiB
       Device slack:              0.00B
       Data,RAID1:             25.00GiB
       Data,RAID5:            497.00GiB
       Data,RAID5:              5.00GiB
       Metadata,RAID5:         17.00GiB
       Metadata,RAID5:        352.00MiB
       System,RAID5:           32.00MiB
       Unallocated:             1.29TiB

    /dev/sde, ID: 5
       Device size:               0.00B
       Device slack:              0.00B
       Data,RAID1:             75.00GiB
       Data,RAID5:              5.00GiB
       Metadata,RAID5:        352.00MiB
       Unallocated:             1.74TiB

Next use the device ID to remove the device. In this case [/dev/sde] will be removed:

`root `[`#`]`btrfs device remove 5 /srv`

### [[] Resizing]

Btrfs partitions can be resized while online using the built-in resize subcommand.

** Note**\
This does not affect the size of the partition itself, just the filesystem.

Set the size of the root filesystem to 128gb:

`root `[`#`]`btrfs filesystem resize 128g /`

Add 50 gigabytes of space to the rootfs:

`root `[`#`]`btrfs filesystem resize +50g /`

The command can also fill all available space:

`root `[`#`]`btrfs filesystem resize max /`

### [[] Subvolumes]

A **subvolume** of Btrfs is a directory with special properties. Most notably a subvolume can be mounted, in particular without mounting the entire Btrfs volume.

The top directory of a Btrfs itself is always a subvolume. Thus a subvolume can contain other subvolumes. A subvolume has to be created by the `btrfs subvolume` command, as explained below. Another feature is that one can set the quota for a subvolume.

However, a subvolume is not a totally independent volume. Assume X and Y are two subvolumes in a single Btrfs volume. Then it is *not* possible to mount X and Y while

-   X is read-write and Y read-only. (More precisely one can create a permanently read-only subvolume. Such subvolumes are always mounted as read-only independent of other subvolumes.)
-   X and Y\'s compression options are different.
-   X and Y\'s CoW options are different.

If the quota is not enabled, it is also impossible to know a subvolume\'s disk usage (beyond the `du` command), unlike a normal volume.

Thus a Brtfs subvolume is completely different from an [LVM](https://wiki.gentoo.org/wiki/LVM "LVM") volume. A subvolume cannot be created *across* different Btrfs filesystems. The snapshot can be *moved* from one filesystem to another, but it cannot span across the two.

#### [[] Create]

To create a subvolume, issue the following command inside a Btrfs filesystem\'s name space:

`root `[`#`]`btrfs subvolume create `*`<dest-name>`*

Replace *`<dest-name>`* with the desired destination and subvolume name. For example, if a Btrfs filesystem exists at [/mnt/btrfs], a subvolume could be created inside it using the following command:

`root `[`#`]`btrfs subvolume create /mnt/btrfs/subvolume1`

#### [[] List]

To see the subvolume(s) that have been created, use the `subvolume list` command followed by a Btrfs filesystem location. If the current directory is somewhere inside a Btrfs filesystem, the following command will display the subvolume(s) that exist on the filesystem:

`root `[`#`]`btrfs subvolume list .`

If a Btrfs filesystem with subvolumes exists at the mount point created in the example command above, the output from the list command will look similar to the following:

`root `[`#`]`btrfs subvolume list /mnt/btrfs`

    ID 309 gen 102913 top level 5 path mnt/btrfs/subvolume1

#### [[] Remove]

All available subvolume paths in a Btrfs filesystem can be seen using the list command above.

Subvolumes can be properly removed by using the `subvolume delete` command, followed by the path to the subvolume:

`root `[`#`]`btrfs subvolume delete `*`<subvolume-path>`*

As above, replace *`<subvolume-path>`* with the actual path to the subvolume to be removed. To delete the subvolume used in the examples above, the following command would be issued:

`root `[`#`]`btrfs subvolume delete /mnt/btrfs/subvolume1`

    Delete subvolume (no-commit): '/mnt/btrfs/subvolume1'

#### [[] Snapshots]

Snapshots are subvolumes that share data and metadata with other subvolumes. This is made possible by Btrfs\' Copy on Write (CoW) ability.^[\[11\]](#cite_note-11)^ Snapshots can be used for several purposes, one of which is to create backups of file system structures at specific points in time.

If the root filesystem is Btrfs, it is possible to create a snapshot using the `subvolume snapshot` commands:

`root `[`#`]`mkdir -p /mnt/backup/rootfs `

`root `[`#`]`btrfs subvolume snapshot / /mnt/backup/rootfs/ `

The following small shell script can be added to a timed cron job to create a timestamped snapshot backup of a Btrfs formatted root filesystem. The timestamps can be adjusted to whatever is preferred by the user.

[FILE] **`btrfs_snapshot.sh`Btrfs rootfs snapshot cron job example**

    #!/bin/bash
    NOW=$(date +"%Y-%m-%d_%H:%M:%S")

    if [ ! -e /mnt/backup ]; then
    mkdir -p /mnt/backup
    fi

    cd /
    /sbin/btrfs subvolume snapshot / "/mnt/backup/backup_$"

Alternatively, it is possible to use a [portage hook](https://wiki.gentoo.org/wiki/Handbook:AMD64/Portage/Advanced#Hooking_into_the_emerge_process "Handbook:AMD64/Portage/Advanced") to create a new snapshot every time a package is installed. This could be useful for users that run testing keywords or experimental packages. See [Snapper](https://wiki.gentoo.org/wiki/Snapper "Snapper") for one example on enabling this setup.

#### [[] Mounting]

A subvolume can be mounted in a location different from where it was created, or users can choose to not mount them at all. For example, a user could create a Btrfs filesystem in [/mnt/btrfs] and create [/mnt/btrfs/home] and [/mnt/btrfs/gentoo-repo] subvolumes. The subvolumes could then be mounted at [/home] and [/var/db/repos/gentoo], with the original top level subvolume left unmounted. This results in a configuration where the subvolumes\' relative path from the top level subvolume is different from their actual path.

To mount a subvolume, perform the following command, where *`<rel-path>`* is the relative path of the subvolume from the top level subvolume, obtainable through the `subvolume list` command:

`root `[`#`]`mount -o subvol=`*`<rel-path>`*` `*`<device>`*` `*`<mountpoint>`*

Similarly, the filesystem tab can be updated to mount a Btrfs subvolume:

[FILE] **`/etc/fstab`Mounting Subvolumes**

    <device>  <mountpoint>  btrfs  subvol=<rel-path>  0 2

### [[] Scrub]

Scrub detects damage to the filesystem against stored checksums.^[\[12\]](#cite_note-12)^ To start scrubbing a directory:

`root `[`#`]`btrfs scrub start /`

To see the scrub progress:

`root `[`#`]`watch -cn 10 btrfs scrub status /`

## [[] Troubleshooting]

### [[] Filesystem check]

With a failing disk or corrupted data, it may be necessary to run the a filesystem check. Typically filesystem check commands are handled through the [fsck.] prefix, but for Btrfs filesystems, checks are handled via the [btrfs check] subcommand:

`root `[`#`]`btrfs check --progress /dev/<device>`

** Note**\
Checking multi-device filesystems are handled by passing any one of the devices in the filesystem to [btrfs check]. As long as all of the devices are available the check should run.

### [[] Multi device filesystem mount fails]

After ungracefully removing one or more devices from a multi device filesystem, attempting to mount the filesystem will fail:

`root `[`#`]`mnt /srv`

    mount: /srv: wrong fs type, bad option, bad superblock on /dev/sdb, missing codepage or helper program, or other error.

This type of mount failure could be caused by missing one or more devices from the multi device filesystem. Missing devices can be detected by using the [filesystem show] subcommand. In the following example [/dev/sdb] is one of the devices still connected to the multi device filesystem:

`root `[`#`]`btrfs filesystem show /dev/sdb`

    Label: none  uuid: 9e7e9824-d66b-4a9c-a05c-c4245accabe99
            Total devices 5 FS bytes used 2.50TiB
            devid    1 size 1.82TiB used 817.03GiB path /dev/sdc
            devid    3 size 1.82TiB used 817.00GiB path /dev/sdb
            devid    5 size 10.91TiB used 2.53TiB path /dev/sde
            devid    6 size 10.91TiB used 2.53TiB path /dev/sdd
            *** Some devices missing

Missing device can be ungracefully dropped from the filesystem by using the following command:

`root `[`#`]`btrfs device delete missing /srv`

** Warning**\
If the multi device filesystem is in RAID 0 mode, then data loss will occur!

### [[] Using with VM disk images]

When using Btrfs with virtual machine disk images, it is best to disable copy-on-write on the disk images in order to speed up IO performance. This can only be performed on files that are newly created. It also possible to disable CoW on all files created within a certain directory. For example, using the [chattr] command:

`root `[`#`]`chattr +C /var/lib/libvirt/images`

### [[] Clear the free space cache]

It is possible to clear Btrfs\' free space cache by mounting the filesystem with the `clear_cache` mount option. For example:

`root `[`#`]`mount -o clear_cache /path/to/device /path/to/mountpoint`

### [][[] Btrfs hogging memory (disk cache)]

When utilizing some of Btrfs\' special abilities (like making many `--reflink` copies or creating high amounts of snapshots), a lot of memory can be consumed and not freed fast enough by the kernel\'s inode cache. This issue can go undiscovered since memory dedicated to the disk cache might not be clearly visible in traditional system monitoring utilities. The [slabtop] utility (available as part of the [[[sys-process/procps]](https://packages.gentoo.org/packages/sys-process/procps)[]] package) was specifically created to determine how much memory kernel objects are consuming:

`root `[`#`]`slabtop`

    Active / Total Objects (% used)    : 5011373 / 5052626 (99.2%)
    Active / Total Slabs (% used)      : 1158843 / 1158843 (100.0%)
    Active / Total Caches (% used)     : 103 / 220 (46.8%)
    Active / Total Size (% used)       : 3874182.66K / 3881148.34K (99.8%)
    Minimum / Average / Maximum Object : 0.02K / 0.77K / 4096.00K

    OBJS ACTIVE  USE OBJ SIZE  SLABS OBJ/SLAB CACHE SIZE NAME
    2974761 2974485  99%    1.10K 991587        3   3966348K btrfs_inode
    1501479 1496052  99%    0.19K  71499       21    285996K dentry

If the inode cache is consuming too much memory, the kernel can be manually instructed to drop the cache by echoing an integer value to the [/proc/sys/vm/drop_caches] file^[\[13\]](#cite_note-13)^.

To be safe, and to help the kernel determine the maximum amount of freeable memory, be sure to run a [sync] *before* running the [echo] commands below:

`user `[`$`]`sync`

Most of the time Btrfs users will probably want to [echo 2] to reclaim just the slab objects (dentries and btrfs_inodes):

`root `[`#`]`echo 2 > /proc/sys/vm/drop_caches`

To clear the entire disk cache (slab objects *and* the page cache) use [echo 3] instead:

`root `[`#`]`echo 3 > /proc/sys/vm/drop_caches`

** Warning**\
While the above commands are non-destructive (as long as a [sync] was completed before running them), they could seriously but temporarily slow down the system while the kernel loads only the necessary items back into memory. Think twice before running the above commands for systems under heavy load!

More information on kernel slabs can be found in this [dedoimedo blog entry](https://www.dedoimedo.com/computers/slabinfo.html).

### [][[] Mounting Btrfs fails, returning mount: unknown filesystem type \'btrfs\']

The [original solution by Tim on Stack Exchange](http://unix.stackexchange.com/questions/121611/gentoo-does-not-seem-to-be-booting-new-kernel) inspired the following solution: build the kernel manually instead of using [genkernel](https://wiki.gentoo.org/wiki/Genkernel "Genkernel"):

`#``cd /usr/src/linux `

`#``make menuconfig `

`#``make && make modules_install `

`#``cp arch/x86_64/boot/bzImage /boot `

`#``mv /boot/bzImage /boot/whatever_kernel_filename `

`#``genkernel --install initramfs `

### [][[] Btrfs root doesn\'t boot]

Genkernel\'s initramfs as created with the command below doesn\'t load Btrfs:

`root `[`#`]`genkernel --btrfs initramfs `

Compile support for Btrfs in the kernel rather than as a module, or use [Dracut](https://wiki.gentoo.org/wiki/Dracut "Dracut") to generate the initramfs.

### [][[] lsblk doesn\'t show mountpoint for all devices in btrfs RAID]

This is unfortunately a known bug at least since 2014.

What you may expect:

`root `[`#`]`lsblk`

    NAME                           MAJ:MIN RM   SIZE RO TYPE  MOUNTPOINTS
    sda                              8:0    0   3,6T  0 disk
    └─sda1                           8:1    0   3,6T  0 part
      ├─raid0vg0-raid0lv0_rmeta_0  253:0    0     4M  0 lvm
      │ └─raid0vg0-raid0lv0        253:4    0   3,6T  0 lvm
      │   └─home                   253:5    0   3,6T  0 crypt /home
      └─raid0vg0-raid0lv0_rimage_0 253:1    0   3,6T  0 lvm
        └─raid0vg0-raid0lv0        253:4    0   3,6T  0 lvm
          └─home                   253:5    0   3,6T  0 crypt /home
    sdb                              8:16   0   3,6T  0 disk
    └─sdb1                           8:17   0   3,6T  0 part
      ├─raid0vg0-raid0lv0_rmeta_1  253:2    0     4M  0 lvm
      │ └─raid0vg0-raid0lv0        253:4    0   3,6T  0 lvm
      │   └─home                   253:5    0   3,6T  0 crypt /home
      └─raid0vg0-raid0lv0_rimage_1 253:3    0   3,6T  0 lvm
        └─raid0vg0-raid0lv0        253:4    0   3,6T  0 lvm
          └─home                   253:5    0   3,6T  0 crypt /home

What you get:

`root `[`#`]`lsblk`

    NAME        MAJ:MIN RM   SIZE RO TYPE MOUNTPOINTS
    sda           8:0    0   3,6T  0 disk /home
    sdb           8:16   0   3,6T  0 disk

It\'s because */proc/#/mountinfo* contains reference to the one device only.^[\[14\]](#cite_note-GitHub_docs:_update_TODO_.C2.B7_util-linux.2Futil-linux.402b1322f-14)[\[15\]](#cite_note-Redhat_Bugzilla-15)^

## [[] See also]

-   [Btrfs/snapshots](https://wiki.gentoo.org/wiki/Btrfs/snapshots "Btrfs/snapshots") --- script to **make automatic snapshots with [Btrfs]** filesystem, using [btrfs subvolume list-new] function to create snapshots only when files have changed, so as to create fewer snapshots.
-   [Btrfs/System Root Guide](https://wiki.gentoo.org/wiki/Btrfs/System_Root_Guide "Btrfs/System Root Guide") --- one example for re-basing a Gentoo installation\'s root filesystem to use btrfs
-   [Btrfs/Native System Root Guide](https://wiki.gentoo.org/wiki/Btrfs/Native_System_Root_Guide "Btrfs/Native System Root Guide")
-   [Ext4](https://wiki.gentoo.org/wiki/Ext4 "Ext4") --- an open source disk [filesystem](https://wiki.gentoo.org/wiki/Filesystem "Filesystem") and the most recent version of the extended series of filesystems.
-   [Btrbk](https://wiki.gentoo.org/wiki/Btrbk "Btrbk") --- a tool for creating incremental snapshots and remote backups of [Btrfs] subvolumes.
-   [Samba shadow copies](https://wiki.gentoo.org/wiki/Samba_shadow_copies "Samba shadow copies") --- expose Shadow Copies as \'Previous Versions\' to Windows clients.
-   [Snapper](https://wiki.gentoo.org/wiki/Snapper "Snapper") --- a command-line program to create and manage filesystem snapshots, allowing viewing or reversion of changes.
-   [ZFS](https://wiki.gentoo.org/wiki/ZFS "ZFS") --- a next generation [filesystem](https://wiki.gentoo.org/wiki/Filesystem "Filesystem") created by Matthew Ahrens and Jeff Bonwick.

## [[] External resources]

-   [https://wiki.debian.org/Btrfs](https://wiki.debian.org/Btrfs) - As described by the Debian wiki.
-   [https://wiki.archlinux.org/index.php/Btrfs](https://wiki.archlinux.org/index.php/Btrfs) Btrfs article - As described by the Arch Linux wiki.
-   [http://www.funtoo.org/BTRFS_Fun](http://www.funtoo.org/BTRFS_Fun) - BTRFS Fun on the Funtoo wiki.
-   [http://marc.merlins.org/perso/btrfs/post_2014-05-04_Fixing-Btrfs-Filesystem-Full-Problems.html](http://marc.merlins.org/perso/btrfs/post_2014-05-04_Fixing-Btrfs-Filesystem-Full-Problems.html) - Tips and tricks on fixing niche Btrfs filesystem problems in some situations.

## [[] References]

1.  [[[↑](#cite_ref-arstechnica_examining-btrfs_2021_1-0)] [[Examining btrfs, Linux's perpetually half-finished filesystem](https://arstechnica.com/gadgets/2021/09/examining-btrfs-linuxs-perpetually-half-finished-filesystem/)]]
2.  [[[↑](#cite_ref-2)] [[man page for btrfs-filesystem(8)](https://btrfs.readthedocs.io/en/latest/btrfs-filesystem.html), [Btrfs wiki](https://btrfs.readthedocs.io). Retrieved on 6th February, 2017.]]
3.  [[[↑](#cite_ref-3)] [[https://btrfs.readthedocs.io/en/latest/Compression.html#compression-levels](https://btrfs.readthedocs.io/en/latest/Compression.html#compression-levels)]]
4.  [[[↑](#cite_ref-4)] [[https://git.kernel.org/pub/scm/linux/kernel/git/mason/linux-btrfs.git/commit/?h=next&id=5c1aab1dd5445ed8bdcdbb575abc1b0d7ee5b2e7](https://git.kernel.org/pub/scm/linux/kernel/git/mason/linux-btrfs.git/commit/?h=next&id=5c1aab1dd5445ed8bdcdbb575abc1b0d7ee5b2e7)]]
5.  [[[↑](#cite_ref-5)] [braindevices. [btrfs benchmark for daily used desktop os](https://gist.github.com/braindevices/fde49c6a8f6b9aaf563fb977562aafec), Retrieved on September 27, 2024.]]
6.  [[[↑](#cite_ref-6)] [[https://btrfs.wiki.kernel.org/index.php/Compression#How_can_I_determine_compressed_size_of_a_file.3F](https://btrfs.wiki.kernel.org/index.php/Compression#How_can_I_determine_compressed_size_of_a_file.3F)]]
7.  [[[↑](#cite_ref-7)] [[Article mentioning that parity RAID code has multiple serious data-loss bugs](https://btrfs.readthedocs.io/en/latest/btrfs-man5.html#raid56-status-and-recommended-practices), [Btrfs wiki](https://btrfs.readthedocs.io). Retrieved on January 1st, 2017.]]
8.  [[[↑](#cite_ref-8)] [Michael Larabel, [Btrfs RAID56 \"Mostly OK\"](http://www.phoronix.com/scan.php?page=news_item&px=Linux-4.12-Btrfs-RAID-Mostly-OK), Phoronix. July 8, 2017.]]
9.  [[[↑](#cite_ref-9)] [[btrfs: scrub: Fix RAID56 recovery race condition](https://git.kernel.org/pub/scm/linux/kernel/git/mason/linux-btrfs.git/commit/?h=for-linus-4.12&id=28d70e237dac905cd8d1896af10216b7d2bced24), source commit, April 18th 2017.]]
10. [[[↑](#cite_ref-10)] [[GIT PULL Btrfs from Chris Mason](http://lkml.iu.edu/hypermail/linux/kernel/1705.1/01197.html), [Linux kernel mailing list](http://lkml.iu.edu/hypermail/linux/kernel/index.html), May 9th 2017.]]
11. [[[↑](#cite_ref-11)] [[Page explaining the differences between subvolumes and logical volumes in LVM](https://btrfs.readthedocs.io/en/latest/Subvolumes.html), [Btrfs wiki](https://btrfs.readthedocs.io). Retrieved on April 2nd, 2023.]]
12. [[[↑](#cite_ref-12)] [[https://btrfs.readthedocs.io/en/latest/Scrub.html](https://btrfs.readthedocs.io/en/latest/Scrub.html). Retrieved on October 5, 2025.]]
13. [[[↑](#cite_ref-13)] [[Documentation for /proc/sys/vm/\*](https://www.kernel.org/doc/Documentation/sysctl/vm.txt), [Kernel.org](https://www.kernel.org). Retrieved on January 1st, 2017.]]
14. [[[↑](#cite_ref-GitHub_docs:_update_TODO_.C2.B7_util-linux.2Futil-linux.402b1322f_14-0)] [[GitHub docs: update TODO · util-linux/util-linux@2b1322f](https://github.com/util-linux/util-linux/commit/2b1322f478d0149d3d570025dbec7cdf897b99a1)]]
15. [[[↑](#cite_ref-Redhat_Bugzilla_15-0)] [[1084453 -- lsblk does not show mountpoints for raid-1 btrfs](https://bugzilla.redhat.com/show_bug.cgi?id=1084453)]]