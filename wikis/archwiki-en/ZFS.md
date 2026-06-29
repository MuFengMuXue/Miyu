# ZFS

ZFS—previously Zettabyte File System—features:

* logical volume management (pooled storage) with checkpoints,
* copy-on-write,
* snapshots, clones (writable snapshots) and bookmarks (lightweight change markers),
* scrubbing (data integrity verification and automatic repair),
* RAID-Z,
* a maximum 16 exabyte file size,
* a maximum 256 quadrillion zettabyte storage with no limit on number of filesystems (datasets) or files.

For an overview of ZFS concepts see .

For an overview of ZFS storage pools see , see also .

ZFS is licensed under the Common Development and Distribution License (CDDL). Because the CDDL is incompatible with the GNU General Public License (GPL), it is not possible for ZFS to be included in the Linux kernel. This requirement, however, does not prevent a native Linux kernel module from being developed and distributed by a third party, as is the case with OpenZFS (previously named ZFS on Linux).

As a result of ZFS not being included in the Linux kernel (with other words, ZFS kernel modules are out-of-tree), and Arch Linux is a rolling release distribution:

* OpenZFS project must keep up with Linux kernel versions.
* After making stable OpenZFS release—ArchZFS maintainers release them.
* There will often be brief periods when the kernel-specific packages in the ArchZFS repository are not in sync with those in the Arch Linux repositories. This situation locks down the normal rolling update process by unsatisfied dependencies because the new kernel version, proposed by update, is unsupported by ArchZFS.
* So you might prefer to use the Dynamic Kernel Module Support (DKMS) package, but ZFS modules may fail to compile with the latest kernel if it is unsupported by OpenZFS.

## Installation
The kernel modules for ZFS can be installed in two ways—either installing a package that provides the modules for a specific kernel version or using a Dynamic Kernel Module Support (DKMS) package that builds the modules for installed kernels.

ZFS userspace utilities—such as  and —are provided by the  package which is a dependency of all ZFS kernel module packages.

For using ZFS on the root partition see Install Arch Linux on ZFS.

## Kernel-specific packages
Install from the ArchZFS repository or alternatively the Arch User Repository:

*  — for the  kernel package,
*  — for the  kernel package,
*  — for the  kernel package,
* zfs-linux-zen — for the  kernel package.

Test the installation by running . If an "insmod" error is produced, try .

## DKMS
Users can make use of Dynamic Kernel Module Support (DKMS) to rebuild the ZFS modules automatically.

Install the  package from the ArchZFS repository or alternatively the Arch User Repository.

To compile the ZFS modules provided by the aforementioned DKMS packages, it is also necessary to install the appropriate headers packages for your installed kernels—e.g.  for ,  for , etc. When either the DKMS packages or the kernel is updated, the kernel modules will be automatically recompiled thanks to the DKMS pacman hook.

## systemd configuration
For ZFS to live by its "zero administration" namesake, you probably want the pools to be automatically imported at boot time. To do so, enable:

*  as the overarching reference point for other units to depend on,
*  as it provides the proper ordering*  to import the pools.

 imports the zfs pools by reading the file . For each imported pool you want automatically imported by , execute:

 # zpool set cachefile=/etc/zfs/zpool.cache pool

To actually mount the ZFS file systems (without listing the ZFS file systems in ), you have choices described in the following sections.

## zfs-mount.service
In order to mount ZFS file systems automatically on boot you need to enable .

## zfs-mount-generator
You can also use the zfs-mount-generator to create systemd mount units for your ZFS file systems at boot. systemd will automatically mount the filesystems based on the mount units without having to use the . To do that, you need to:

# Create the  directory.
# Enable the ZFS Event Daemon(ZED) script (called a ZEDLET) required to create a list of mountable ZFS file systems. (This link is created automatically if you are using OpenZFS >= 2.0.0.)
# Enable  and enable/start the ZFS Event Daemon (). This service is responsible for running the script in the previous step.
# You need to create an empty file named after your pool in . The ZEDLET will only update the list of filesystems if the file for the pool already exists.
# Check the contents of . If it is empty, make sure that the  is running and just change the canmount property of any of your ZFS filesystem by running:  This change causes ZFS to raise an event which is captured by ZED, which in turn runs the ZEDLET to update the file in . If the file in  is updated, you can set the  property of the filesystem back by running:
You need to add a file in  for each ZFS pool in your system. Make sure the required units and targets are enabled.

## Usage examples
ZFS is considered a "zero administration" file system by its creators; therefore, configuring ZFS is very straight forward. Configuration is done primarily with two commands:  and .

Users wishing to experiment with ZFS on [https://openzfs.github.io/openzfs-docs/man/master/7/zpoolconcepts.7.html#file file virtual devices ("vdevs") with no possibility of real data loss are encouraged to see the /Virtual disks article. Common tasks like building a RAIDZ array, purposefully corrupting data and recovering it, snapshotting datasets, etc. are covered.

## Storage pools
It is not necessary to partition the drives before creating the ZFS filesystem. It is recommended to point ZFS at an entire disk (ie.  rather than ), which will automatically create a GPT (GUID Partition Table) and add an 8 MB reserved partition at the end of the disk for legacy bootloaders. However, you can specify a partition or a file within an existing filesystem, if you wish to create multiple volumes with different redundancy properties.

## Identify disks
OpenZFS recommends using device IDs when creating ZFS storage pools of less than 10 devicesUse Persistent block device naming#by-id and by-path to identify the list of drives to be used for ZFS pool.

The disk IDs should look similar to the following:

## Using GPT labels
Disk labels and UUID can also be used for ZFS mounts by using GPT partitions. ZFS drives have labels but Linux is unable to read them at boot. Unlike MBR partitions, GPT partitions directly support both UUID and labels independent of the format inside the partition. Partitioning rather than using the whole disk for ZFS offers two additional advantages. The OS does not generate bogus partition numbers from whatever unpredictable data ZFS has written to the partition sector, and if desired, you can easily over provision SSD drives, and slightly over provision spindle drives to ensure that different models with slightly different sector counts can zpool replace into your mirrors. This is a lot of organization and control over ZFS using readily available tools and techniques at almost zero cost.

Use gdisk to partition the all or part of the drive as a single partition. gdisk does not automatically name partitions so if partition labels are desired use gdisk command "c" to label the partitions. Some reasons you might prefer labels over UUID are: labels are easy to control, labels can be titled to make the purpose of each disk in your arrangement readily apparent, and labels are shorter and easier to type. These are all advantages when the server is down and the heat is on. GPT partition labels have plenty of space and can store most international characters wikipedia:GUID_Partition_Table#Partition_entries allowing large data pools to be labeled in an organized fashion.

Drives partitioned with GPT have labels and UUID that look like this.

## Creating ZFS pools
To create a ZFS pool:

 # zpool create -f -m   [raidz(2|3)|mirror

* create: subcommand to create the pool.

* -f: Force creating the pool. This is to overcome the "EFI label error". See #Does not contain an EFI label.
* -m: The mount point of the pool. If this is not specified, then the pool will be mounted to .
* pool: This is the name of the pool.
* raidz(2|3)|mirror: This is the type of virtual device that will be created from the list of devices. Raidz is a single disk of parity (similar to raid5), raidz2 for 2 disks of parity (similar to raid6) and raidz3 for 3 disks of parity. Also available is mirror, which is similar to raid1 or raid10, but is not constrained to just 2 device. If not specified, each device will be added as a vdev which is similar to raid0. After creation, a device can be added to each single drive vdev to turn it into a mirror, which can be useful for migrating data.
* ids: The ID's of the drives or partitions that to include into the pool.

Create pool with single raidz vdev:

 # zpool create -f -m /mnt/data bigdata \
                raidz \
                   ata-ST3000DM001-9YN166_S1F0KDGY \
                   ata-ST3000DM001-9YN166_S1F0JKRR \
                   ata-ST3000DM001-9YN166_S1F0KBP8 \
                   ata-ST3000DM001-9YN166_S1F0JTM1

Create pool with two mirror vdevs:

 # zpool create -f -m /mnt/data bigdata \
                mirror \
                   ata-ST3000DM001-9YN166_S1F0KDGY \
                   ata-ST3000DM001-9YN166_S1F0JKRR \
                mirror \
                   ata-ST3000DM001-9YN166_S1F0KBP8 \
                   ata-ST3000DM001-9YN166_S1F0JTM1

## Advanced Format disks
At pool creation, ashift=12 should always be used, except with SSDs that have 8k sectors where ashift=13 is correct. A vdev of 512 byte disks using 4k sectors will not experience performance issues, but a 4k disk using 512 byte sectors will. Since ashift cannot be changed after pool creation, even a pool with only 512 byte disks should use 4k because those disks may need to be replaced with 4k disks or the pool may be expanded by adding a vdev composed of 4k disks. Because correct detection of 4k disks is not reliable,  should always be specified during pool creation. See the OpenZFS FAQ for more details.

Create pool with ashift=12 and single raidz vdev:

 # zpool create -f -o ashift=12 -m /mnt/data bigdata \
                raidz \
                   ata-ST3000DM001-9YN166_S1F0KDGY \
                   ata-ST3000DM001-9YN166_S1F0JKRR \
                   ata-ST3000DM001-9YN166_S1F0KBP8 \
                   ata-ST3000DM001-9YN166_S1F0JTM1

## GRUB-compatible pool creation
By default, zpool create enables all features on a pool. If  resides on ZFS when using GRUB you must only enable features supported by GRUB otherwise GRUB will not be able to read the pool. ZFS includes compatibility files (see ) to assist in creating pools at specific feature sets, of which grub2 is an option.

You can create a pool with only the compatible features enabled:

 # zpool create -o compatibility=grub2 $POOL_NAME $VDEVS

## Verifying pool status
If the command is successful, there will be no output. Using the mount command will show that the pool is mounted. Using  will show that the pool has been created:

At this point it would be good to reboot the machine to ensure that the ZFS pool is mounted at boot. It is best to deal with all errors before transferring data.

## Importing a pool created by id
Eventually a pool may fail to auto mount and you need to import to bring your pool back. Take care to avoid the most obvious solution.

Adapt one of the following commands to import your pool so that pool imports retain the persistence they were created with:

 # zpool import -d /dev/disk/by-id bigdata
 # zpool import -d /dev/disk/by-partlabel bigdata
 # zpool import -d /dev/disk/by-partuuid bigdata

Finally check the state of the pool:

 # zpool status -v bigdata

## Destroy a storage pool
ZFS makes it easy to destroy a mounted storage pool, removing all metadata about the ZFS device.

To destroy the pool:
 # zpool destroy

To destroy a dataset:
 # zfs destroy /

And now when checking the status:

## Exporting a storage pool
If a storage pool is to be used on another system, it will first need to be exported. It is also necessary to export a pool if it has been imported from the archiso as the hostid is different in the archiso as it is in the booted system. The zpool command will refuse to import any storage pools that have not been exported. It is possible to force the import with the  argument, but this is considered bad form.

Any attempts made to import an un-exported storage pool will result in an error stating the storage pool is in use by another system. This error can be produced at boot time abruptly abandoning the system in the busybox console and requiring an archiso to do an emergency repair by either exporting the pool, or adding the  to the kernel boot parameters (which is not ideal). See #On boot the zfs pool does not mount stating: "pool may be in use from other system".

To export a pool:

 # zpool export

## Extending an existing zpool
A device (a partition or a disk) can be added to an existing zpool:

 # zpool add

To import a pool which consists of multiple devices:

 # zpool import -d  -d

or simply:

 # zpool import -d /dev/disk-by-id/

## Attaching a device to (create) a mirror
A device (a partition or a disk) can be attached aside an existing device to be its mirror (similar to RAID 1):

 # zpool attach

You can attach the new device to an already existing mirror vdev (e.g. to upgrade from a 2-device to a 3-device mirror) or attach it to single device to create a new mirror vdev.

## Renaming a zpool
Renaming a zpool that is already created is accomplished in 2 steps:

 # zpool export oldname
 # zpool import oldname newname

## Setting a different mount point
The mount point for a given zpool can be moved at will with one command:
 # zfs set mountpoint=/foo/bar poolname

## Upgrade zpools
When using a newer  module, zpools may display an upgrade indication:

To upgrade the version of zpool bigdata:

 # zpool upgrade bigdata

To upgrade the version of all zpools:

 # zpool upgrade -a

## Datasets
Users can optionally create a dataset under the zpool as opposed to manually creating directories under the zpool. Datasets allow for an increased level of control (quotas for example) in addition to snapshots. To be able to create and mount a dataset, a directory of the same name must not pre-exist in the zpool. To create a dataset, use:

 # zfs create /

It is then possible to apply ZFS specific attributes to the dataset. For example, one could assign a quota limit to a specific directory within a dataset:

 # zfs set quota=20G //

To see all the commands available in ZFS, see  and .

## Native encryption
ZFS offers the following supported encryption options: , , , ,  and . When encryption is set to ,  will be used. See  for a description of the native encryption, including limitations.

The following keyformats are supported: , , .

One can also specify/increase the default iterations of PBKDF2 when using  with , although it may increase the decryption time.

To create a dataset including native encryption with a passphrase, use:

 # zfs create -o encryption=on -o keyformat=passphrase /

To use a key instead of using a passphrase:

 # dd if=/dev/random of=/path/to/key bs=32 count=1 iflag=fullblock
 # zfs create -o encryption=on -o keyformat=raw -o keylocation=file:///path/to/key /

The easy way to make a key in human-readable form ():

 # od -Anone -x -N 32 -w64 /dev/random | tr -d > /path/to/hex.key

To verify the key location:

 # zfs get keylocation /

To change the key location:

 # zfs set keylocation=file:///path/to/key /

You can also manually load the keys by using one of the following commands:

 # zfs load-key / # load key for a specific dataset
 # zfs load-key -a # load all keys
 # zfs load-key -r zpool/dataset # load all keys in a dataset

To mount the created encrypted dataset:

 # zfs mount /

## Unlock/Mount at boot time: systemd
It is possible to automatically unlock a pool dataset on boot time by using a systemd unit. For example create the following service to unlock any specific dataset:

Enable/start the service for each encrypted dataset, (e.g. ). Note the use of , which is an escaped  in systemd unit definitions. See  for more info.

An alternative is to load all possible keys:

Enable/start .

## Unlock at login time: PAM
If you are not encrypting the root volume, but only the home volume or a user-specific volume, another idea is to [https://blog.trifork.com/2020/05/22/linux-homedir-encryption/ wait until login to decrypt it.  The advantages of this method are that the system boots uninterrupted, and that when the user logs in, the same password can be used both to authenticate and to decrypt the home volume, so that the password is only entered once.

There are two methods for unlocking the home dataset: #PAM module or #Custom script. Both methods assume your datasets are structured similar to:

Replace , , and  with the values from your setup.

## PAM module
OpenZFS includes a PAM module since 2.0.0. It supports child datasets since 2.3.1.

First, stop systemd from automatically mounting  (this property will be inherited by all child datasets):

 # zfs set org.openzfs.systemd:ignore=on rpool/home

Then create the following file:

 may be omitted if there are no child datasets in any of the users' datasets.

Finally, add the following to the beginning of  and :

 auth       include      zfs-key
 session    include      zfs-key
 password   include      zfs-key

## Custom script
First set the mountpoint to legacy to avoid having it mounted by :

Ensure that it is in /etc/fstab so that  will work:

Alternatively, you can keep using ZFS mounts if you use both:

The first will stop ZFS automatically mounting it, and the second systemd, but you will still be able to manually (or through the following scripts) mount it. If you have child datasets,  will be inherited, but you will need to set  on each as it is not inheritable, otherwise they will try to mount without a mountpoint.

On a single-user system, with only one  volume having the same encryption password as the user's password, it can be decrypted at login as follows: first create

{{hc|/usr/local/bin/mount-zfs-homedir|2=
#!/bin/bash
set -eu

# $PAM_USER will be the username of the user, you can use it for per-user home volumes.
HOME_VOLUME="rpool/home"

if [ "$(zfs get keystatus "${HOME_VOLUME}" -Ho value)" != "available" ]; then
  PASSWORD=$(cat -)
  zfs load-key "${HOME_VOLUME}" /swap

Prepare it as swap partition:

 # mkswap -f /dev/zvol//swap
 # swapon /dev/zvol//swap

To make it permanent, edit . ZVOLs support discard, which can potentially help ZFS's block allocator and reduce fragmentation for all other datasets when/if swap is not full.

Add a line to :

 /dev/zvol//swap none swap discard 0 0

## Access Control Lists
To use ACL on a dataset:

 # zfs set acltype=posixacl /
 # zfs set xattr=sa /

Setting  is recommended for performance reasons It may be preferable to enable ACL on the zpool as datasets will inherit the ACL parameters. Setting  may be wanted as the default mode is  [https://docs.oracle.com/cd/E19120-01/open.solaris/817-2271/gbaaz/index.html; however, it is worth noting that  does not affect POSIX ACLs # zfs set aclinherit=passthrough
 # zfs set acltype=posixacl
 # zfs set xattr=sa

## Databases
ZFS, unlike most other file systems, has a variable record size, or what is commonly referred to as a block size. By default, the recordsize on ZFS is 128KiB, which means it will dynamically allocate blocks of any size from 512B to 128KiB depending on the size of file being written. This can often help fragmentation and file access, at the cost that ZFS would have to allocate new 128KiB blocks each time only a few bytes are written to.

Most RDBMSes work in 8KiB-sized blocks by default. Although the block size is tunable for MySQL/MariaDB, PostgreSQL, and Oracle database, all three of them use an 8KiB block size by default. For both performance concerns and keeping snapshot differences to a minimum (for backup purposes, this is helpful), it is usually desirable to tune ZFS instead to accommodate the databases, using a command such as:

 # zfs set recordsize=8K /postgres

These RDBMSes also tend to implement their own caching algorithm, often similar to ZFS's own ARC. In the interest of saving memory, it is best to simply disable ZFS's caching of the database's file data and let the database do its own job:

 # zfs set primarycache=metadata /postgres

ZFS uses the ZIL for crash recovery, but databases are often syncing their data files to the file system on their own transaction commits anyway. The end result of this is that ZFS will be committing data twice to the data disks, and it can severely impact performance. You can tell ZFS to prefer to not use the ZIL, and in which case, data is only committed to the file system once. However, doing so on non-solid state storage (e.g. HDDs) can result in decreased read performance due to fragmentation ([https://openzfs.org/wiki/ZFS_on_high_latency_devices OpenZFS Wiki) -- with mechanical hard drives, please consider using a dedicated SSD as ZIL rather than setting the option below. In addition, setting this for non-database file systems, or for pools with configured log devices, can also negatively impact the performance, so beware:

 # zfs set logbias=throughput /postgres

These can also be done at file system creation time, for example:

 # zfs create -o recordsize=8K \
              -o primarycache=metadata \
              -o mountpoint=/var/lib/postgres \
              -o logbias=throughput \
               /postgres

Please note: these kinds of tuning parameters are ideal for specialized applications like RDBMSes. You can easily hurt ZFS's performance by setting these on a general-purpose file system such as your /home directory.

## /tmp
If you would like to use ZFS to store your /tmp directory, which may be useful for storing arbitrarily-large sets of files or simply keeping your RAM free of idle data, you can generally improve performance of certain applications writing to /tmp by disabling file system sync. This causes ZFS to ignore an application's sync requests (eg, with  or ) and return immediately. While this has severe application-side data consistency consequences (never disable sync for a database!), files in /tmp are less likely to be important and affected. Please note this does not affect the integrity of ZFS itself, only the possibility that data an application expects on-disk may not have actually been written out following a crash.

 # zfs set sync=disabled /tmp

Additionally, for security purposes, you may want to disable setuid and devices on the /tmp file system, which prevents some kinds of privilege-escalation attacks or the use of device nodes:

 # zfs set setuid=off /tmp
 # zfs set devices=off /tmp

Combining all of these for a create command would be as follows:

 # zfs create -o setuid=off -o devices=off -o sync=disabled -o mountpoint=/tmp /tmp

Please note, also, that if you want /tmp on ZFS, you will need to mask (disable) systemd's automatic tmpfs-backed /tmp (, else ZFS will be unable to mount your dataset at boot-time or import-time.

## Transmitting snapshots with ZFS Send and ZFS Recv
It is possible to pipe ZFS snapshots to an arbitrary target by pairing  and . This is done through standard output, which allows the data to be sent to any file, device, across the network, or manipulated mid-stream by incorporating additional programs in the pipe.

Below are examples of common scenarios:

## Basic ZFS Send
First, create a snapshot of some ZFS filesystem:

 # zfs snapshot zpool0/archive/books@snap

Now send the snapshot to a new location on a different zpool:

 # zfs send -v zpool0/archive/books@snap | zfs recv zpool4/library

The contents of  are now live at

## To and from files
First, create a snapshot of some ZFS filesystem:

 # zfs snapshot zpool0/archive/books@snap

Write the snapshot to a gzip file:

 # zfs send zpool0/archive/books@snap > /tmp/mybooks.gz

Now restore the snapshot from the file:

 # gzcat /tmp/mybooks.gz | zfs recv -F zpool0/archive/books

## Send over ssh
First, create a snapshot of some ZFS filesystem:

 # zfs snapshot zpool1/filestore@snap

Next we pipe our "send" traffic over an ssh session running "recv":

 # zfs send -v zpool1/filestore@snap | ssh $HOST zfs recv coldstore/backups

The  flag prints information about the datastream being generated. If you are using a passphrase or passkey, you will be prompted to enter it.

## Incremental Backups
You may wish update a previously sent ZFS filesystem without retransmitting all of the data over again.
Alternatively, it may be necessary to keep a filesystem online during a lengthy transfer and it is now time to send writes that were made since the initial snapshot.

First, create a snapshot of some ZFS filesystem:

 # zfs snapshot zpool1/filestore@initial

Next we pipe our "send" traffic over an ssh session running "recv":

 # zfs send -v -R zpool1/filestore@initial | ssh $HOST zfs recv coldstore/backups

Once changes are written, make another snapshot:

 # zfs snapshot zpool1/filestore@snap2

The following will send the differences that exist locally between zpool1/filestore@initial and zpool1/filestore@snap2 and create an additional snapshot for the remote filesystem coldstore/backups:

 # zfs send -v -i -R zpool1/filestore@initial | ssh $HOST zfs recv coldstore/backups

Now both zpool1/filestore and coldstore/backups have the @initial and @snap2 snapshots.

On the remote host, you may now promote the latest snapshot to become the active filesystem:
 # zfs rollback coldstore/backups@snap2

## Tuning
## General
ZFS pools and datasets can be further adjusted using parameters.

To retrieve the current pool parameter status:

 # zfs get all

To retrieve the current dataset parameter status:

 # zfs get all /

To disable access time (atime), which is enabled by default:

 # zfs set atime=off

To disable access time (atime) on a particular dataset:

 # zfs set atime=off /

An alternative to turning off atime completely,  is available. This brings the default ext4/XFS atime semantics to ZFS, where access time is only updated if the modified time or changed time changes, or if the existing access time has not been updated within the past 24 hours. It is a compromise between  and . This property only takes effect if  is :

 # zfs set atime=on
 # zfs set relatime=on

Compression is just that, transparent compression of data. ZFS supports a few different algorithms, presently lz4 is the default, gzip is also available for seldom-written yet highly-compressible data; consult the OpenZFS Wiki for more details.

To enable compression:

 # zfs set compression=on

To reset a property of a pool and/or dataset to its default state, use :

 # zfs inherit -rS atime
 # zfs inherit -rS atime /

## Scrubbing
Whenever data is read and ZFS encounters an error, it is silently repaired when possible, rewritten back to disk and logged so you can obtain an overview of errors on your pools. There is no fsck or equivalent tool for ZFS. Instead, ZFS supports a feature known as scrubbing. This traverses through all the data in a pool and verifies that all blocks can be read.

To scrub a pool:

 # zpool scrub

To cancel a running scrub:

 # zpool scrub -s

## How often should I do this?
From the Oracle blog post Disk Scrub - Why and When?:

:This question is challenging for Support to answer, because as always the true answer is "It Depends". So before I offer a general guideline, here are a few tips to help you create an answer more tailored to your use pattern.

:* What is the expiration of your oldest backup? You should probably scrub your data at least as often as your oldest tapes expire so that you have a known-good restore point.
:* How often are you experiencing disk failures? While the recruitment of a hot-spare disk invokes a "resilver" -- a targeted scrub of just the VDEV which lost a disk -- you should probably scrub at least as often as you experience disk failures on average in your specific environment.
:* How often is the oldest piece of data on your disk read? You should scrub occasionally to prevent very old, very stale data from experiencing bit-rot and dying without you knowing it.

:If any of your answers to the above are "I do not know", the general guideline is: you should probably be scrubbing your zpool at least once per month. It is a schedule that works well for most use cases, provides enough time for scrubs to complete before starting up again on all but the busiest & most heavily-loaded systems, and even on very large zpools (192+ disks) should complete fairly often between disk failures.

In the ZFS Administration Guide by Aaron Toponce, he advises to scrub consumer disks once a week.

## Start with a service or timer
Using a systemd timer/service it is possible to automatically scrub pools.

To perform scrubbing monthly on a particular pool:

Enable/start  unit for monthly scrubbing the specified zpool.

## Enabling TRIM
To quickly query your vdevs TRIM support, you can include trimming information in  with .

ZFS is capable of trimming supported vdevs either on-demand or periodically via the  property.

Manually performing a TRIM operation on a zpool:

  # zpool trim

Enabling periodic trimming on all supported vdevs in a pool:

  # zpool set autotrim=on

To perform a full  monthly on a particular pool using a systemd timer/service:

Enable/start  unit for monthly trimming of the specified zpool.

## SSD Caching
If your pool has no configured log devices, ZFS reserves space on the pool's data disks for its intent log (the ZIL, also called SLOG). If your data disks are slow (e.g. HDD) it is highly recommended to configure the ZIL on solid state drives for better write performance and also to consider a layer 2 adaptive replacement cache (L2ARC). The process to add them is very similar to adding a new VDEV.

All of the below references to device-id are the IDs from .

## ZIL
To add a mirrored ZIL:

  # zpool add  log mirror

Or to add a single device ZIL (unsafe):

  # zpool add  log

Because the ZIL device stores data that has not been written to the pool, it is important to use devices that can finish writes when power is lost. It is also important to use redundancy, since a device failure can cause data loss. In addition, the ZIL is only used for sync writes, so may not provide any performance improvement when your data drives are as fast as your ZIL drive(s).

## L2ARC
To add L2ARC:
 # zpool add  cache
L2ARC is only a read cache, so redundancy is unnecessary. Since ZFS version 2.0.0, L2ARC is persisted across reboots.L2ARC is generally only useful in workloads where the amount of hot data is bigger than system memory, but small enough to fit into L2ARC. The L2ARC is indexed by the ARC in system memory, consuming 70 bytes per record (default 128KiB). Thus, the equation for RAM usage is:
 (L2ARC size) / (recordsize) * 70 bytes
Because of this, L2ARC can, in certain workloads, harm performance as it takes memory away from ARC.

## ZVOLs
ZFS volumes (ZVOLs) can suffer from the same block size-related issues as RDBMSes, but it is worth noting that the default recordsize for ZVOLs is 8 KiB already. If possible, it is best to align any partitions contained in a ZVOL to your recordsize (current versions of fdisk and gdisk by default automatically align at 1MiB segments, which works), and file system block sizes to the same size. Other than this, you might tweak the recordsize to accommodate the data inside the ZVOL as necessary (though 8 KiB tends to be a good value for most file systems, even when using 4 KiB blocks on that level).

## RAIDZ and Advanced Format physical disks
Each block of a ZVOL gets its own parity disks, and if you have physical media with logical block sizes of 4096B, 8192B, or so on, the parity needs to be stored in whole physical blocks, and this can drastically increase the space requirements of a ZVOL, requiring 2× or more physical storage capacity than the ZVOL's logical capacity. Setting the recordsize to 16k or 32k can help reduce this footprint drastically.

See [https://github.com/openzfs/zfs/issues/1807 OpenZFS issue #1807 for details.

## I/O Scheduler
While ZFS is expected to work well with modern schedulers including, , and , experimenting with manually setting the I/O scheduler on ZFS disks may yield performance gains. The ZFS recommendation is "users leave the default scheduler [https://github.com/openzfs/zfs/issues/9778#issuecomment-569347505 "unless you're encountering a specific problem, or have clearly measured a performance improvement for your workload""== Tips and tricks ==

## Create an Archiso image with ZFS support
Follow the Archiso steps for creating a fully functional Arch Linux live CD/DVD/USB image. To include ZFS support in the image, you can either build your choice of PKGBUILDs from the AUR or include prebuilt packages from one of the unofficial user repositories.

## Using self-built ZFS packages from the AUR
Build the ZFS packages you want by following the normal procedures. If you are unsure,  and  are likely to be compatible with the widest range of other modifications to the Archiso image you may wish to perform. Proceed to set up a custom local repository. Include the resulting repository in the Pacman configuration of your new profile.

Include the built packages in the list of packages to be installed. The example below presumes you want to include the ,, and  packages.

If you include any DKMS packages, make sure you also include headers for any kernels you are including in the ISO (for example, for the default  kernel this would be . Other kernels have their own respective headers packages).

## Using the archzfs unofficial user repository
Add the ArchZFS unofficial user repository to  in your new Archiso profile.

Add the  group to the list of packages to be installed (the  repository provides packages for the x86_64 architecture only) as well as required dependencies.

## Finishing up
Regardless of where you source your ZFS packages from, you should finish by building the ISO.

## Automatic snapshots
## zrepl
The  package provides a ZFS automatic replication service, which could also be used as a snapshotting service much like snapper.

For details on how to configure the zrepl daemon, see the zrepl [https://zrepl.github.io/ documentation. The configuration file should be located at . Then, run  to make sure that the syntax of the config file is correct. Finally, enable .

## sanoid
 is a policy-driven tool for taking snapshots. Sanoid also includes , which is for replicating snapshots. It comes with systemd services and a timer.

Sanoid only prunes snapshots on the local system. To prune snapshots on the remote system, run sanoid there as well with prune options. Either use the  command line option or use the  command line option together with the  and  configuration options.

## ZFS Automatic Snapshot Service for Linux
The  package provides a shell script to automate the management of snapshots, with each named by date and label (hourly, daily, etc), giving quick and convenient snapshotting of all ZFS datasets. The package also installs cron tasks for quarter-hourly, hourly, daily, weekly, and monthly snapshots. Optionally adjust the  from the defaults depending on how far back the snapshots are to go (the monthly script by default keeps data for up to a year).

To prevent a dataset from being snapshotted at all, set  on it. Likewise, set more fine-grained control as well by label, if, for example, no monthlies are to be kept on a snapshot, for example, set .

Once the package has been installed, enable and start the selected timers ({{ic|zfs-auto-snapshot-{frequent,daily,weekly,monthly}.timer}}).

## Creating a share
ZFS has support for sharing a file system over the Network File System (NFS) or Server Message Block (SMB) protocols.

One potential benefit of using the ZFS primitives to manage NFS and Samba is the ability to automatically restore shares from a source system on a target system after replication.

## NFS
Make sure NFS has been installed and configured. The  and  services should be started.

To make a pool available on the network:

 # zfs set sharenfs=on nameofzpool

To make a dataset available on the network:

 # zfs set sharenfs=on nameofzpool/nameofdataset

To enable read/write access for a specific ip-range(s):

 # zfs set sharenfs="rw=@192.168.1.100/24,rw=@10.0.0.0/24" nameofzpool/nameofdataset

To check if the dataset is exported successfully:

To view the current loaded exports state in more detail, use:

To view the current NFS share list by ZFS:

 # zfs get sharenfs

## SMB
When sharing through SMB, using  in  will allow ZFS to setup and create the shares. See Samba#Enable Usershares for details.

Create and set permissions on the user directory as root:

 # mkdir /var/lib/samba/usershares
 # chmod +t /var/lib/samba/usershares

To make a pool available on the network:

 # zfs set sharesmb=on nameofzpool

To make a dataset available on the network:

 # zfs set sharesmb=on nameofzpool/nameofdataset

To check if the dataset is exported successfully:

To view the current SMB share list by ZFS:

 # zfs get sharesmb

## Encryption in ZFS using dm-crypt
Before OpenZFS version 0.8.0, ZFS did not support encryption directly (See #Native encryption). Instead, zpools can be created on dm-crypt block devices. Since the zpool is created on the plain-text abstraction, it is possible to have the data encrypted while having all the advantages of ZFS like deduplication, compression, and data robustness. Furthermore, utilizing dm-crypt will encrypt the zpools metadata, which the native encryption can inherently not provide. See also .

dm-crypt, possibly via LUKS, creates devices in  and their name is fixed. So you just need to change  commands to point to that names. The idea is configuring the system to create the  block devices and import the zpools from there. Since zpools can be created in multiple devices (raid, mirroring, striping, ...), it is important all the devices are encrypted otherwise the protection might be partially lost.

For example, an encrypted zpool can be created using plain dm-crypt (without LUKS) with:

 # cryptsetup open --type=plain --hash=sha256 --cipher=aes-xts-plain64 --offset=0 \
              --key-file=/dev/sdZ --key-size=512 /dev/sdX enc
 # zpool create zroot /dev/mapper/enc

In the case of a root filesystem pool, the  HOOKS line will enable the keyboard for the password, create the devices, and load the pools. It will contain something like:

 HOOKS=(... keyboard encrypt zfs ...)

Since the  name is fixed no import errors will occur.

Creating encrypted zpools works fine. But if you need encrypted directories, for example to protect your users' homes, ZFS loses some functionality.

ZFS will see the encrypted data, not the plain-text abstraction, so compression and deduplication will not work. The reason is that encrypted data has always high entropy making compression ineffective and even from the same input you get different output (thanks to salting) making deduplication impossible. To reduce the unnecessary overhead it is possible to create a sub-filesystem for each encrypted directory and use eCryptfs on it.

For example to have an encrypted home: (the two passwords, encryption and login, must be the same)

 # zfs create -o compression=off -o dedup=off -o mountpoint=/home/ /
 # useradd -m
 # passwd
 # ecryptfs-migrate-home -u

## Emergency chroot repair with ArchZFS
To get into the ZFS filesystem from live system for maintenance, there are two options:

# Build custom archiso with ZFS as described in #Create an Archiso image with ZFS support.
# Boot the latest official archiso and bring up the network. Then enable ArchZFS repository inside the live system as usual, sync the pacman package database and install the archzfs-archiso-linux package.

To start the recovery, load the ZFS kernel modules:

 # modprobe zfs

Import the pool:

 # zpool import -a -R /mnt

Mount the boot partition and EFI system partition (if any):

 # mount /dev/sda2 /mnt/boot
 # mount /dev/sda1 /mnt/efi

Chroot into the ZFS filesystem:

 # arch-chroot /mnt /bin/bash

Check the kernel version:

 # pacman -Qi linux
 # uname -r

uname will show the kernel version of the archiso. If they are different, run depmod (in the chroot) with the correct kernel version of the chroot installation:

 # depmod -a 3.6.9-1-ARCH (version gathered from pacman -Qi linux but using the matching kernel modules directory name under the chroot's /lib/modules)

This will load the correct kernel modules for the kernel version installed in the chroot installation.

Regenerate the initramfs. There should be no errors.

## Bind mount
Here a bind mount from /mnt/zfspool to /srv/nfs4/music is created. The configuration ensures that the zfs pool is ready before the bind mount is created.

## fstab
See  for more information on how systemd converts fstab into mount unit files with .

## Monitoring / Mailing on Events
See ZED: The ZFS Event Daemon for more information.

An email forwarder, such as S-nail, is required to accomplish this. Test it to be sure it is working correctly.

Uncomment the following in the configuration file:

Update 'root' in  to the email address you want to receive notifications at.

If you are keeping your mailrc in your home directory, you can tell mail to get it from there by setting :

This works because ZED sources this file, so  sees this environment variable.

If you want to receive an email no matter the state of your pool, you will want to set . You will need to do this temporary to test.

Start and enable .

With , you can test by running a scrub as root: .

## Wrap shell commands in pre & post snapshots
Since it is so cheap to make a snapshot, we can use this as a measure of security for sensitive commands such as system and package upgrades. If we make a snapshot before, and one after, we can later diff these snapshots to find out what changed on the filesystem after the command executed. Furthermore we can also rollback in case the outcome was not desired.

## znp
E.g.:

 # zfs snapshot -r zroot@pre
 # pacman -Syu
 # zfs snapshot -r zroot@post
 # zfs diff zroot@pre zroot@post
 # zfs rollback zroot@pre

A utility that automates the creation of pre and post snapshots around a shell command is znp.

E.g.:

 # znp pacman -Syu
 # znp find / -name "something*" -delete

and you would get snapshots created before and after the supplied command, and also output of the commands logged to file for future reference so we know what command created the diff seen in a pair of pre/post snapshots.

## Remote unlocking of ZFS encrypted root
The  hook for unlocking natively-encrypted ZFS datasets via SSH is provided by both  (see PR #261) and the  package. This section describes how to use this hook, and is largely based on dm-crypt/Specialties#Busybox based initramfs (built with mkinitcpio).

For busybox based initramfs the  package provides the ,  and  hooks needed for network connectivity and SSH access during the boot process. After installing the package, check its optional dependencies and manually install those required by the hooks you plan to use. E.g. to use the  and  hooks, you have to install  and .

# If you don't have an SSH key pair yet, generate one on the client system (the one which will be used to unlock the remote machine).
# Add your SSH public key(s) or copy an existing  file to the remote machine's  or  file.
# Add the  hooks to the HOOKS array in , before the  hook:  Then regenerate the initramfs.
# Add the  kernel parameter to your boot loader configuration. E.g. if you use DHCP for network configuration:  The hook will wait up to 120 seconds for a response from the DHCP server. This can be adjusted with the  kernel parameter. Alternatively, configure a static IP:  You can also specify the subnet mask and gateway if necessary:  The  parameter supports many more options, e.g configuring multiple interfaces, etc. For more info see the hook's documentation:  The examples above assume an Ethernet connection. If using Wi-Fi instead, install the  package and create a wpa_supplicant configuration:  Then add the  hook before  in , make sure your Wi-Fi related modules are in the MODULES array, and use  as the kernel parameter.
# Restart the remote system and ssh to it on port 222 as the  user. The SSH server in the initramfs generates its own set of host keys and listens on a non-standard port by default to allow your SSH client to verify a separate set of host keys for the initramfs and the main SSH server. Reusing host keys from the main SSH server isn't recommended as the initramfs image may be world-readable which would expose them and make the system vulnerable to MITM attacks. Both the listening port and the host key types can be configured, see the hook documentation for details ( or ). You will be prompted for the passphrase to unlock the encrypted pool. After unlocking, the system will complete its boot process and you can ssh to it as you normally would.

## Enabling bclone support
To use  and other commands needing bclone support, it is necessary to upgrade the feature flags if coming from a version prior to 2.2.2. This will allow the pool to have support for bclone. This is done with , if the status of the pool show this is possible.

It is also required to enable a module parameter, otherwise userspace apps will not be able to use this feature. You can do this by putting this into :

Check that is working, and how much space is being saved with the command:

## Troubleshooting
## Creating a zpool fails
If the following error occurs then it can be fixed.

  the kernel failed to rescan the partition table: 16
  cannot label 'sdc': try using parted(8) and then provide a specific slice: -1

One reason this can occur is because ZFS expects pool creation to take less than 1 secondThis is a reasonable assumption under ordinary conditions, but in many situations it may take longer. Each drive will need to be cleared again before another attempt can be made.

 # zpool labelclear /dev/sdX
 # wipefs --all /dev/sdX

A brute force creation can be attempted over and over again, and with some luck the ZPool creation will take less than 1 second. One cause for creation slowdown can be slow burst read writes on a drive. By reading from the disk in parallel to ZPool creation, it may be possible to increase burst speeds.

 # dd if=/dev/sda of=/dev/null

This can be done with multiple drives by saving the above command for each drive to a file on separate lines and running

 # cat $FILE | parallel

Then run ZPool creation at the same time.

## ZFS is using too much RAM
By default, ZFS caches file operations (ARC) using up to half of available system memory on the host. To adjust the ARC size, add the following to the Kernel parameters list:

 zfs.zfs_arc_max=536870912 # (for 512MiB)

In case that the default value of  (1/32 of system memory) is higher than the specified  it is needed to add also the following to the Kernel parameters list:

 zfs.zfs_arc_min=268435456 # (for 256MiB, needs to be lower than zfs.zfs_arc_max)

You may also want to increase  instead (in this example to 8GiB):

 # echo $((8*1024**3)) > /sys/module/zfs/parameters/zfs_arc_sys_free

For a more detailed description, as well as other configuration options, see Gentoo:ZFS#ARC.

ZFS should release ARC as applications reserve more RAM, but some applications still [https://github.com/openzfs/zfs/issues/10255 get confused, and reported free RAM is always wrong. But in case all your applications work as intended and you have no problems, there is no need to change ARC settings.

## Does not contain an EFI label
The following error will occur when attempting to create a zfs filesystem,

 /dev/disk/by-id/ does not contain an EFI label but it may contain partition

The way to overcome this is to use  with the zfs create command.

## No hostid found
An error that occurs at boot with the following lines appearing before initscript output:

 ZFS: No hostid found on kernel command line or /etc/hostid.

This warning occurs because the ZFS module does not have access to the spl hosted. There are two solutions, for this. Either place the spl hostid in the kernel parameters in the boot loader. For example, adding .

The other solution is to make sure that there is a hostid in , and then regenerate the initramfs image. Which will copy the hostid into the initramfs image.

## Pool cannot be found while booting from SAS/SCSI devices
In case you are booting a SAS/SCSI based, you might occassionally get boot problems where the pool you are trying to boot from cannot be found. A likely reason for this is that your devices are initialized too late into the process. That means that zfs cannot find any devices at the time when it tries to assemble your pool.

In this case you should force the scsi driver to wait for devices to come online before continuing. You can do this by putting this into :

Afterwards, regenerate the initramfs.

This works because the zfs hook will copy the file at  into the initcpio which will then be used at build time.

## On boot the zfs pool does not mount stating: "pool may be in use from other system"
## Unexported pool
If the new installation does not boot because the zpool cannot be imported, chroot into the installation and properly export the zpool. See #Emergency chroot repair with ArchZFS.

Once inside the chroot environment, load the ZFS module and force import the zpool,

 # zpool import -a -f

now export the pool:

 # zpool export

To see the available pools, use,

 # zpool status

It is necessary to export a pool because of the way ZFS uses the hostid to track the system the zpool was created on. The hostid is generated partly based on the network setup. During the installation in the archiso the network configuration could be different generating a different hostid than the one contained in the new installation. Once the zfs filesystem is exported and then re-imported in the new installation, the hostid is reset. See Re: Howto zpool import/export automatically? - msg#00227.

If ZFS complains about "pool may be in use" after every reboot, properly export pool as described above, and then regenerate the initramfs in normally booted system.

## Incorrect hostid
Double check that the pool is properly exported. Exporting the zpool clears the hostid marking the ownership. So during the first boot the zpool should mount correctly. If it does not there is some other problem.

Reboot again, if the zfs pool refuses to mount it means the hostid is not yet correctly set in the early boot phase and it confuses zfs. Manually tell zfs the correct number, once the hostid is coherent across the reboots the zpool will mount correctly.

Boot using zfs_force and write down the hostid. This one is just an example.

This number have to be added to the kernel parameters as . Another solution is writing the hostid inside the initram image, see the installation guide explanation about this.

Users can always ignore the check adding  in the kernel parameters, but it is not advisable as a permanent solution.

## Devices have different sector alignment
Once a drive has become faulted it should be replaced A.S.A.P. with an identical drive.

 # zpool replace bigdata ata-ST3000DM001-9YN166_S1F0KDGY ata-ST3000DM001-1CH166_W1F478BD -f

but in this instance, the following error is produced:

 cannot replace ata-ST3000DM001-9YN166_S1F0KDGY with ata-ST3000DM001-1CH166_W1F478BD: devices have different sector alignment

ZFS uses the ashift option to adjust for physical block size. When replacing the faulted disk, ZFS is attempting to use , but the faulted disk is using a different ashift (probably ) and this causes the resulting error.

For Advanced Format disks with 4 KiB block size, an  of  is recommended for best performance. See OpenZFS FAQ: Performance Considerations and ZFS and Advanced Format disks.

Use zdb to find the ashift of the zpool: , then use the  argument to set the ashift of the replacement drive:

 # zpool replace bigdata ata-ST3000DM001-9YN166_S1F0KDGY ata-ST3000DM001-1CH166_W1F478BD -o ashift=9 -f

Check the zpool status for confirmation:

## Pool resilvering stuck/restarting/slow?
According to ZFS issue #840, this is a known issue since 2012 with ZFS-ZED which causes the resilvering process to constantly restart, sometimes get stuck and be generally slow for some hardware. The simplest mitigation is to stop zfs-zed.service until the resilver completes.

## Fix slow boot caused by failed import of unavailable pools in the initramfs zpool.cache
Your boot time can be significantly impacted if you update your intitramfs (eg when doing a kernel update) when you have additional but non-permanently attached pools imported because these pools will get added to your initramfs zpool.cache and ZFS will attempt to import these extra pools on every boot, regardless of whether you have exported it and removed it from your regular zpool.cache.

If you notice ZFS trying to import unavailable pools at boot, first run:

 # zdb -C

To check your zpool.cache for pools you do not want imported at boot. If this command is showing (a) additional, currently unavailable pool(s), run:

 # zpool set cachefile=/etc/zfs/zpool.cache zroot

To clear the zpool.cache of any pools other than the pool named zroot. Sometimes there is no need to refresh your zpool.cache, but instead all you need to do is regenerate the initramfs.

## ZFS Command History
ZFS logs changes to a pool's structure natively as a log of executed commands in a ring buffer (which cannot be turned off).
The log may be helpful when restoring a degraded or failed pool.
