# Bcachefs

Bcachefs is a copy on write (CoW) file system with support for multiple devices, RAID, compression, checksumming and encryption. It aims to provide modern features similar to those of Btrfs and ZFS.

It is built upon Bcache and is mainly developed by Kent Overstreet.

## Installation
Install  and , the latter makes use of Dynamic Kernel Module Support (DKMS) to provide the module for installed Linux kernels.

To initramfs with the Bcachefs module provided by the aforementioned dkms package, it is also necessary to install the appropriate headers package(s) for your installed kernel(s) (e.g.  for ,  for , etc.).

## Setup
## Single drive
 # bcachefs format /dev/sdX
 # mount -t bcachefs /dev/sdX /mnt

## Multiple drives
Bcachefs stripes data by default, similar to RAID0. Redundancy is handled via the replicas option. 2 drives with  is equivalent to RAID1, 4 drives with  is equivalent to RAID10, etc.

 # bcachefs format /dev/sdX /dev/sdY --replicas=n
 # mount -t bcachefs /dev/sdX:/dev/sdY /mnt

Heterogeneous drives are supported. If they are different sizes, larger stripes will be used on some, so that they all fill up at the same rate. If they are different speeds, reads for replicated data will be sent to the ones with the lowest IO latency. If some are more reliable than others (a hardware raid device, for example) you can set  to count each copy of data on that device as 2 replicas.

## Encrypted root filesystem
Bcachefs uses a [https://bcachefs.org/Encryption/#Algorithms self-rolled whole filesystem encryption using ChaCha20Poly1305. To format an encrypted filesystem:

 # bcachefs format --encrypted /dev/sdX

In the case of a root filesystem add  to the HOOKS array in the  configuration to prompt for filesystem unlock at boot or resuming from hibernate.

## SSD caching
Bcachefs has four storage targets: metadata, background, foreground, and promote. Writes to the filesystem prioritize the foreground drives, which are then moved to the background over time. Reads are cached on the promote drives. The metadata target is usually leveraged with ultra-low read-latency NVME drives like Intel Optane.

A recommended configuration is to use an ssd group for the foreground and promote, and an hdd group for the background (a writeback cache).

 # bcachefs format \
     --label=ssd.ssd1 /dev/sdA \
     --label=ssd.ssd2 /dev/sdB \
     --label=hdd.hdd1 /dev/sdC \
     --label=hdd.hdd2 /dev/sdD \
     --label=hdd.hdd3 /dev/sdE \
     --label=hdd.hdd4 /dev/sdF \
     --replicas=2 \
     --foreground_target=ssd \
     --promote_target=ssd \
     --background_target=hdd
 # mount -t bcachefs /dev/sdA:/dev/sdB:/dev/sdC:/dev/sdD:/dev/sdE:/dev/sdF /mnt

For a writethrough cache, do the same as above, but set  on each of the ssd devices.
For a writearound cache, foreground target to the hdd group, and promote target to the ssd group.

## Mounting
The default way of mounting is to specify every device in the mount directive.

 # mount -t bcachefs /dev/sdA:/dev/sdB:/dev/sdC:/dev/sdD:/

The  command supports mounting a filesystem by UUID,
which is displayed by  on filesystem creation.

 # mount.bcachefs UUID=f66d108f-83d2-4679-b50b-7d5e710f6a2b /mnt/

To mount a single or multi-device on boot, add  to the  array in  and regenerate the initramfs.

## Configuration
Most options can be set
* during ,
* after format with ,
* at mount time with ,
* or through sysfs, for example, .

Mount options override those set by the other methods, which save them to the filesystem's superblock.

Examples of some available options are:

{| class="wikitable"
|+ Bcachefs options
! Option !! Description
|-
| metadata_checksum  || specifies the checksum algorithm to be used for metadata writes. By default the algorithm is crc32c. You can choose one of , , , .
|-
| data_checksum || specifies the checksum algorithm to be used for data writes, shares the same defaults and options as .
|-
| compression || specifies the algorithm to be used for (foreground) compression. By default this option is none. You can choose one of ,  , , .
|-
| background_compression || specifies the algorithm to be used for (background) compression, shares the same defaults and options as
|-
| str_hash || specifies the hashing function to be used for directory entries and xattrs. You can choose one of ,  and .
|-
| nocow || all writes will be done in place when possible. Snapshots and reflinks will still  cause writes to be COW, this option implicitly disables data checksumming, compression and encryption.
|-
| encrypted || enables encryption on the filesystem (chacha20/poly1305); passphrase will be prompted for.
|-
|}

More options can be found in the bcachefs documentation.

The following can also be set on a per directory or per file basis with . It will propagate options recursively if you set it on a directory.

* data_replicas
* data_checksum
* compression, background_compression
* foreground_target, background_target, promote_target

To check what options are active you can do

## Changing a device's group
The group of a device can be changed through the sysfs.
 # echo group.drive_name > /sys/fs/bcachefs/filesystem_uuid/dev-X/label

## Adding a device
 # bcachefs device add --label=group.drive_name /mnt /dev/device

If this is the first drive in a group, you will need to change the target settings to make use of it. This example is for adding a cache drive.

 # echo new_group > /sys/fs/bcachefs/filesystem_uuid/options/promote_target
 # echo new_group > /sys/fs/bcachefs/filesystem_uuid/options/foreground_target
 # echo old_group > /sys/fs/bcachefs/filesystem_uuid/options/background_target

## Removing a device
First make sure there are at least 2 metadata replicas (Evacuate does not appear to work for metadata). If your data and metadata are already replicated, you may skip this step.

 # echo 2 > /sys/fs/bcachefs/UUID/options/metadata_replicas
 # bcachefs data rereplicate /mnt
 # bcachefs device set-state ro device
 # bcachefs device evacuate device

Setting state ro meaning read-only.

To remove the device:

 # bcachefs device remove device
 # bcachefs data rereplicate /mnt

## Replication
Metadata and data replication levels in Bcachefs can be configured independently to control redundancy and durability.
The following options define both the synchronous (immediate) replication, which is performed atomically at write time to ensure data integrity, and the eventual replication target, which is fulfilled asynchronously in the background to improve redundancy and fault tolerance:

*  sets both the target number of metadata and data replicas.
*  sets the target number of metadata replicas to be maintained in the background during normal operation and rebalancing.
*  sets the target number of data replicas to be maintained eventually.
*  sets the minimum number of metadata replicas that must be written synchronously before the metadata is considered committed.
*  sets the minimum number of data replicas that must be written synchronously before the data is considered committed.

## Compression
Compression is set with the  option. It is also possible to set the compression level. As an example to set zstd compression level 5, you can use .

## Subvolumes
Bcachefs supports subvolumes and snapshots with a similar userspace interface as Btrfs. A new subvolume may be created empty, or it may be created as a snapshot of another subvolume. Snapshots are writeable and may be snapshot-ted again, creating a tree of snapshots.

Snapshots are very cheap to create: they’re not based on cloning of COW btrees as with Btrfs, but instead are based on versioning of individual keys in the btrees. Many thousands or millions of snapshots can be created, with the only limitation being disk space.

## Creating a subvolume
To create a new, empty subvolume:

 # bcachefs subvolume create /path/to/subvolume

## Deleting a subvolume
To delete an existing subvolume or snapshot:

 # bcachefs subvolume delete /path/to/subvolume

## Creating a snapshot of an existing subvolume
To create a snapshot of an existing subvolume:

 # bcachefs subvolume snapshot /path/to/source /path/to/dest

A subvolume can also be deleting with a normal rmdir after deleting all the contents, as with .

Features including recursive snapshot creation and a method for recursively listing subvolume are still to be implemented.

## Tips and tricks
Check the journal for more useful error messages.

## Flag Ordering
Some  flags are set based upon their argument order and only affect drives that come after the flag is toggled. For example, if you want SSDs to have  and enable  while HDDs use defaults, make sure arguments are passed in the following order:

 # bcachefs format \
     --label=hdd.hdd1 /dev/sdC \
     --label=hdd.hdd2 /dev/sdD \
     --label=hdd.hdd3 /dev/sdE \
     --label=hdd.hdd4 /dev/sdF \
     --durability=0 --discard \
     --label=ssd.ssd1 /dev/sdA \
     --label=ssd.ssd2 /dev/sdB \
     --replicas=2 \
     --foreground_target=ssd \
     --promote_target=ssd \
     --background_target=hdd

## Setting replicas after format
It is possible to set replica count after format using .

 # bcachefs set-fs-option --metadata_replicas=2 --data_replicas=2 /dev/sdX

Afterwards you'll need to tell bcachefs to ensure that all files have a replica with:

 # bcachefs data rereplicate /mnt

## Troubleshooting
## 32-bit programs cannot see directory contents
Some 32-bit programs may fail to retrieve contents of directories in Bcachefs, due to incompatibility of data returned by the filesystem when a  syscall is performed. This can be worked around by temporarily using a different filesystem, such as tmpfs, for such a program to read and write from.

## swapfile contains holes or other unsupported extents.
Bcachefs does not currently support [https://github.com/koverstreet/bcachefs/issues/368 swapfiles.

## Multi-device fstab
There is currently a bug in systemd that does not make it possible for it to mount a multi-device bcachefs filesystem at boot using devices separated by colons in fstab. It will work when doing , but will not mount at boot. However since  version 1.7.0 it is possible to mount a multi-device array using one device node; this allows the use of the normal UUID specifier.

 # UUID=10176fc9-c4fa-4a30-9fd0-a756d861c4cd     /mnt   bcachefs defaults,nofail 0 0

The filesystem UUID / External UUID can be found by either using:

 # bcachefs fs usage /mnt
 # bcachefs show-super /dev/sdXY

## Mounting an encrypted device errors
When the mounting of a device created with the  option fails after  with
 ERROR - bcachefs::commands::cmd_mount: Fatal error: Required key not available

It can be worked-around by manually linking the keys to the session# keyctl link @u @s
 # mount /dev/sdXY /mnt
 Enter passphrase:

The renewed entry of the passphrase queried by mount is not necessary (pressing  suffices).
