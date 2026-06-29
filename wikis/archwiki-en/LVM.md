# LVM

From Wikipedia:Logical Volume Manager (Linux):

:Logical Volume Manager (LVM) is a device mapper framework that provides logical volume management for the Linux kernel.

## Background
## LVM building blocks
Logical Volume Management utilizes the kernel's device-mapper feature to provide a system of partitions independent of underlying disk layout. With LVM you abstract your storage and have "virtual partitions", making extending/shrinking easier (subject to potential filesystem limitations).

Virtual partitions allow addition and removal without worry of whether you have enough contiguous space on a particular disk, getting caught up fdisking a disk in use (and wondering whether the kernel is using the old or new partition table), or, having to move other partitions out of the way.

Basic building blocks of LVM:

; Physical volume (PV): Unix block device node, usable for storage by LVM. Examples: a hard disk, an MBR or GPT partition, a loopback file, a device mapper device (e.g. dm-crypt). It hosts an LVM header.
; Volume group (VG): Group of PVs that serves as a container for LVs. PEs are allocated from a VG for a LV.
; Logical volume (LV): "Virtual/logical partition" that resides in a VG and is composed of PEs. LVs are Unix block devices analogous to physical partitions, e.g. they can be directly formatted with a file system.
; Physical extent (PE): The smallest contiguous extent (default 4 MiB) in the PV that can be assigned to a LV. Think of PEs as parts of PVs that can be allocated to any LV.

Example:

## Advantages
LVM gives you more flexibility than just using normal hard drive partitions:

* Use any number of disks as one big disk.
* Have logical volumes stretched over several disks (RAID, mirroring, striping which offer advantages such as additional resilience and performance * Create small logical volumes and resize them "dynamically" as they get filled up.
* Resize logical volumes regardless of their order on disk. It does not depend on the position of the LV within VG, there is no need to ensure surrounding available space.
* Resize/create/delete logical and physical volumes online. File systems on them still need to be resized, but some (such as Ext4 and Btrfs) support online resizing.
* Online/live migration of LV (or segments) being used by services to different disks without having to restart services.
* Snapshots allow you to backup a frozen copy of the file system, while keeping service downtime to a minimum and easily merge the snapshot into the original volume later.
* Support for unlocking separate volumes without having to enter a key multiple times on boot (make LVM on top of LUKS).
* Built-in support for caching of frequently used data ().

## Disadvantages
* Additional steps in setting up the system (may require changes to mkinitcpio configuration), more complicated. Requires (multiple) daemons to constantly run.
* If dual-booting, note that Windows does not support LVM; you will be unable to access any LVM partitions from Windows. 3rd Party software may allow to mount certain kinds of LVM setups. [https://www.paragon-software.com/home/linuxfs-windows/
* If your physical volumes are not on a RAID-1, RAID-5 or RAID-6 losing one disk can lose one or more logical volumes if you span (or extend) your logical volumes across multiple non-redundant disks.
* It is not always easy to shrink the space used by the logical volume manager, meaning the physical volumes used for the logical volumes. If the physical extents are scattered across the physical volume until the end you might need to inspect the segments and move them (potentially to another physical device) or the same device with custom allocation settings (e.g. ). If you want to dual-boot with other operating systems (e.g. with Microsoft Windows), the only space left on the device for Microsoft Windows is the space not used by LVM / not used as physical volume.
* Potentially worse performance than using plain partitions. * May not work well with all file systems, especially those that are designed to be (multi-)device aware. For example, Btrfs offers some of the same functionality ([https://btrfs.readthedocs.io/en/latest/btrfs-device.html multi device support, (sub)volumes, snapshots and RAID) which could clash (read further about issues with LVM snapshots with Btrfs).

## Installation
Make sure the  package is installed.

If you have LVM volumes not activated via the initramfs, enable , which is provided by the  package.

## Volume operations
## Physical volumes
## Creating
To create a PV on , run:

 # pvcreate /dev/sda1

You can check the PV is created using the following command:

 # pvs

## Growing
After extending or prior to reducing the size of a device that has a physical volume on it, you need to grow or shrink the PV using .

To expand the PV on  after enlarging the partition, run:

 # pvresize /dev/sda1

This will automatically detect the new size of the device and extend the PV to its maximum.

## Shrinking
To shrink a physical volume prior to reducing its underlying device, add the  parameters to the command, e.g.:

 # pvresize --setphysicalvolumesize 40G /dev/sda1

The above command may leave you with this error:

 /dev/sda1: cannot resize to 25599 extents as later ones are allocated.
 0 physical volume(s) resized / 1 physical volume(s) not resized

Indeed pvresize will refuse to shrink a PV if it has allocated extents after where its new end would be. One needs to run pvmove beforehand to relocate these elsewhere in the volume group if there is sufficient free space.

## Move physical extents
Before freeing up physical extents at the end of the volume, one must run  to see them. An alternative way to view segments in a tabular form is .

In the below example, there is one physical volume on , one volume group  and one logical volume .

One can observe  space are split across the volume. To shrink the physical volume, we must first move all used segments to the beginning.

Here, the first free segment is from 0 to 153600 and leaves us with 153601 free extents. We can now move this segment number from the last physical extent to the first extent. The command will thus be:

## Resize physical volume
Once all your free physical segments are on the last physical extents, run  with root privileges and see your free PE.

Then you can now run again the command:

 # pvresize --setphysicalvolumesize size PhysicalVolume

See the result:

## Resize partition
Last, you need to shrink the partition with your favorite partitioning tool.

## Volume groups
## Creating a volume group
To create a VG  with an associated PV , run:

 # vgcreate MyVolGroup /dev/sdb1

You can check the VG  is created using the following command:

 # vgs

You can bind multiple PVs when creating a VG like this:

 # vgcreate MyVolGroup /dev/sdb1 /dev/sdb2

## Activating a volume group
 # vgchange -a y MyVolGroup

By default, this will reactivate the volume group when applicable. For example, if you had a drive failure in a mirror and you swapped the drive; and ran (1) , (2)  and (3) .

## Repairing a volume group
To start the rebuilding process of the degraded mirror array in this example, you would run:

 # lvconvert --repair /dev/MyVolGroup/mirror

You can monitor the rebuilding process (Cpy%Sync Column output) with:

 # lvs -a -o +devices

## Deactivating a volume group
Just invoke

 # vgchange -a n MyVolGroup

This will deactivate the volume group and allow you to unmount the container it is stored in.

## Renaming a volume group
Use the  command to rename an existing volume group.

Either of the following commands renames the existing volume group  to

 # vgrename /dev/MyVolGroup /dev/my_volume_group

 # vgrename MyVolGroup my_volume_group

Make sure to update all configuration files (e.g.  or ) that reference the renamed volume group.

## Add physical volume to a volume group
You first create a new physical volume on the block device you wish to use, then extend your volume group

 # pvcreate /dev/sdb1
 # vgextend MyVolGroup /dev/sdb1

This of course will increase the total number of physical extents on your volume group, which can be allocated by logical volumes as you see fit.

## Remove partition from a volume group
If you created a logical volume on the partition, remove it first.

All of the data on that partition needs to be moved to another partition. Fortunately, LVM makes this easy:

 # pvmove /dev/sdb1

If you want to have the data on a specific physical volume, specify that as the second argument to :

 # pvmove /dev/sdb1 /dev/sdf1

Then the physical volume needs to be removed from the volume group:

 # vgreduce MyVolGroup /dev/sdb1

Or remove all empty physical volumes:

 # vgreduce --all MyVolGroup

For example: if you have a bad disk in a group that cannot be found because it has been removed or failed:

 # vgreduce --removemissing --force MyVolGroup

And lastly, if you want to use the partition for something else, and want to avoid LVM thinking that the partition is a physical volume:

 # pvremove /dev/sdb1

## Logical volumes
## Creating a logical volume
To create a LV  in a VG  with 300 GiB of capacity, run:

 # lvcreate -L 300G MyVolGroup -n homevol

or, to create a LV  in a VG  with the rest of capacity, run:

 # lvcreate -l 100%FREE MyVolGroup -n homevol

To create the LV while restricting it to specific PVs within the VG, append them to the command:

 # lvcreate -L 300G MyVolGroup -n homevol /dev/sda1

The new LV will appear as . Now you can format the LV with an appropriate file system.

You can check the LV is created using the following command:

 # lvs

## Renaming a logical volume
To rename an existing logical volume, use the  command.

Either of the following commands renames logical volume  in volume group  to .

 # lvrename /dev/MyVolGroup/old_vol /dev/MyVolGroup/new_vol

 # lvrename MyVolGroup old_vol new_vol

Make sure to update all configuration files (e.g.  or ) that reference the renamed logical volume.

## Resizing the logical volume and file system in one go
Extend the logical volume  in  by 10 GiB  and resize its file system all at once:

 # lvresize -L +10G --resizefs MyVolGroup/mediavol

Set the size of logical volume  in  to 15 GiB and resize its file system all at once:

 # lvresize -L 15G --resizefs MyVolGroup/mediavol

If you want to fill all the free space on a volume group, use the following command:

 # lvresize -l +100%FREE --resizefs MyVolGroup/mediavol

See  for more detailed options.

## Resizing the logical volume and file system separately
For file systems not supported by  will need to use the appropriate utility to resize the file system before shrinking the logical volume or after expanding it.

To extend logical volume  within volume group  by 2 GiB without touching its file system:

 # lvresize -L +2G MyVolGroup/mediavol

Now expand the file system (ext4 in this example) to the maximum size of the underlying logical volume:

 # resize2fs /dev/MyVolGroup/mediavol

For Btrfs,  expects the mountpoint instead of the device, the equivalent is:

 # btrfs filesystem resize max /mnt/my-mountpoint

To reduce the size of logical volume  in  by 500 MiB, first calculate the resulting file system size and shrink the file system (Ext4 in this example) to the new size:

 # resize2fs /dev/MyVolGroup/mediavol NewSize

Unlike Ext4, Btrfs supports online shrinking (again, a mountpoint should be specified) e.g.:

 # btrfs filesystem resize -500M /mnt/my-mountpoint

When the file system is shrunk, reduce the size of logical volume:

 # lvresize -L -500M MyVolGroup/mediavol

To calculate the exact logical volume size for ext2, ext3, ext4 file systems, use a simple formula: .

 102400000 blocks × 4096 bytes/block ÷ 4 MiB/extent = 100000 extents

Passing  will confirm that the correctness.

See  for more detailed options.

## Removing a logical volume
First, find out the name of the logical volume you want to remove. You can get a list of all logical volumes with:

 # lvs

Next, look up the mountpoint of the chosen logical volume:

 $ lsblk

Then unmount the filesystem on the logical volume:

 # umount /mountpoint

Finally, remove the logical volume:

 # lvremove volume_group/logical_volume

For example:

 # lvremove MyVolGroup/homevol

Confirm by typing in .

Make sure to update all configuration files (e.g.  or ) that reference the removed logical volume.

You can verify the removal of the logical volume by typing  as root again (see first step of this section).

## Snapshots
LVM supports CoW (Copy-on-Write) snapshots. A CoW snapshot initially points to the original data. When data blocks are overwritten, the original copy is left intact and the new blocks are written elsewhere on-disk. This has several desirable properties:
* Creating snapshots is fast, because it does not copy data (just the much shorter list of pointers to the on-disk locations).
* Snapshots require just enough free space to hold the new data blocks (plus a negligible amount for the pointers to the new blocks). For example, a snapshot of 35 GiB of data, where you write only 2 GiB (on both the original and snapshot), only requires 2 GiB of free space.

LVM snapshots are at the block level. They make a new block device, with no apparent relationship to the original except when dealing with the LVM tools. Therefore, deleting files in the original copy does not free space in the snapshots. If you need filesystem-level snapshots, you rather need btrfs, ZFS or bcachefs.

## Configuration
You create snapshot logical volumes just like normal ones.

 # lvcreate --size 100M --snapshot --name snap01vol /dev/MyVolGroup/lvol

With that volume, you may modify less than 100 MiB of data, before the snapshot volume fills up.

Reverting the modified  logical volume to the state when the  snapshot was taken can be done with

 # lvconvert --merge /dev/MyVolGroup/snap01vol

In case the origin logical volume is active, merging will occur on the next reboot (merging can be done even from a LiveCD).

Also multiple snapshots can be taken and each one can be merged with the origin logical volume at will.

## Backups
A snapshot provides a frozen copy of a file system to make backups. For example, a backup taking two hours provides a more consistent image of the file system than directly backing up the partition.

The snapshot can be mounted and backed up with dd or tar. The size of the backup file done with dd will be the size of the files residing on the snapshot volume.
To restore just create a snapshot, mount it, and write or extract the backup to it. And then merge it with the origin.

See Create root filesystem snapshots with LVM for automating the creation of clean root file system snapshots during system startup for backup and rollback.

## Encryption
See dm-crypt/Encrypting an entire system#LUKS on LVM and dm-crypt/Encrypting an entire system#LVM on LUKS for the possible schemes of combining LUKS with LVM.

## Cache
From :

: The cache logical volume type uses a small and fast LV to improve the performance of a large and slow LV. It does this by storing the frequently used blocks on the faster LV. LVM refers to the small fast LV as a cache pool LV. The large slow LV is called the origin LV. Due to requirements from dm-cache (the kernel driver), LVM further splits the cache pool LV into two devices - the cache data LV and cache metadata LV. The cache data LV is where copies of data blocks are kept from the origin LV to increase speed. The cache metadata LV holds the accounting information that specifies where data blocks are stored (e.g. on the origin LV or on the cache data LV).  Users should be familiar with these LVs if they wish to create the best and most robust cached logical volumes. All of these associated LVs must be in the same VG.

## Create cache
Convert your fast disk () to PV and add to your existing VG ():

 # vgextend MyVolGroup /dev/fastdisk

## Using a cache logical volume
Create a cache logical volume with automatic metadata on  and convert the existing LV  to a cached LV, all in one step:

 # lvcreate --type cache --cachemode writethrough -l 100%FREE -n root_cachevol MyVolGroup/rootvol /dev/fastdisk

## Using a cache pool
With a cache logical volume, LVM automatically manages metadata and data for the cache. But you can also manually create the metatada and cache LVs, and create a cache pool:

 # lvcreate -n cache_meta -l 1%FREE MyVolGroup /dev/fastdisk
 # lvcreate -n cache_data -l 100%FREE MyVolGroup /dev/fastdisk
 # lvconvert --type cache-pool --cachemode writeback --poolmetadata MyVolGroup/cache_meta MyVolGroup/cache_data
 # lvconvert --type cache --cachepool MyVolGroup/cache_data MyVolGroup/rootvol

## Cachemode options
Cachemode has two possible options:

*  ensures that any data written will be stored both in the cache LV and on the origin LV. The loss of a device associated with the cache LV in this case would not mean the loss of any data;
*  ensures better performance, but at the cost of a higher risk of data loss in case the drive used for cache fails.

If a specific  is not indicated, the system will assume  as default.

## Remove cache
If you ever need to undo the one step creation operation above:

 # lvconvert --uncache MyVolGroup/rootvol

This commits any pending writes still in the cache back to the origin LV, then deletes the cache. Other options are available and described in .

## RAID
LVM may be used to create a software RAID. It is a good choice if the user does not have hardware RAID and was planning on using LVM anyway. From :
:  RAID is a way to create a Logical Volume (LV) that uses multiple physical devices to improve performance or tolerate device failures.  In LVM, the physical devices are Physical Volumes (PVs) in a single Volume Group (VG).

LVM RAID supports RAID 0, RAID 1, RAID 4, RAID 5, RAID 6 and RAID 10. See Wikipedia:Standard RAID levels for details on each level.

## Setup RAID
Create physical volumes:

 # pvcreate /dev/sda2 /dev/sdb2

Create volume group on the physical volumes:

 # vgcreate MyVolGroup /dev/sda2 /dev/sdb2

## New volumes
Create logical volumes using , see  and  for more options.

 # lvcreate --type RaidLevel -n Name -L Size VG [PVs

Please mind how the examples below each specify the physical volumes. This can make sense in some situations to have LVM use a specific subset of devices for your new logical volume. But generally speaking, this is not necessary.

## RAID 0
For example:

 # lvcreate -n myraid1vol -i 2 -I 64 -L 70G VolGroup00 /dev/nvme1n1p1 /dev/nvme0n1p1

will create a 70 GiB striped (raid0) logical volume named "myraid1vol" in VolGroup00. Stripes will be spread over  and . Stripesize is set to be 64K.

## RAID 1
For example:

 # lvcreate --type raid1 --mirrors 1 -L 20G -n myraid1vol MyVolGroup /dev/sda2 /dev/sdb2

will create a 20 GiB mirrored logical volume named "myraid1vol" in VolGroup00 on  and .

## RAID 5
RAID5 requires at least three drives (number of  plus one parity device). Data and parity blocks are stored on each device, typically in a rotating pattern.

For example:

 # lvcreate --type raid5 --stripes 2 -L 40G -n myraid5vol MyVolGroup /dev/sda2 /dev/sdb2 /dev/sdc2

will create a 40 GiB striped logical volume named "myraid5vol" in VolGroup00 on ,  and . On each disk, the RAID5 will occupy about 20 GiB.

## RAID 6
RAID6 requires at least five drives (number of  plus two parity devices). As with RAID5, data and parity blocks are stored on each device, typically in a rotating pattern.

For example:

 # lvcreate --type raid6 --stripes 3 -L 60G -n myraid6vol MyVolGroup /dev/sda2 /dev/sdb2 /dev/sdc2 /dev/sdd2

will create a 60 GiB striped logical volume named "myraid6vol" in VolGroup00 on , ,  and . On each disk, the RAID6 will occupy about 20 GiB.

## RAID 10
For example:

 # lvcreate -n myraid1vol -L 100G --type raid10 -m 1 -i 2 MyVolGroup /dev/sdd1 /dev/sdc1 /dev/sdb1 /dev/sda5

will create a 100 GiB RAID10 logical volume named "myraid1vol" in VolGroup00 on , , , and .

## Existing volumes
You can convert easily a non-RAID (e.g. linear) volume to pretty much any other raid configuration provided that you have enough physical devices to meet the RAID requirements. Some of them will require you to go through intermediate steps which  will inform you about and prompt you to agree.  below can be replaced with , ,  etc.

 # lvconvert --type raid10 /dev/vg01/lv01

Use specific PVs:

 # lvconvert --type raid10 /dev/vg01/lv01 /dev/sda1 /dev/sdb2 /dev/nvme0n1p1 ...

You can keep track of the progress of conversion with:

 # watch lvs -o name,vg_name,copy_percent

## Thin provisioning
From :

:Blocks in a standard  Logical Volume (LV) are allocated when the LV is created, but blocks in a thin provisioned LV are allocated as they are written. Because of this, a thin provisioned LV is given a virtual size, and can then be much larger than physically available storage. The amount of physical storage provided for thin provisioned LVs can be increased later as the need arises.

## Example: implementing virtual private servers
Here is the classic use case. Suppose you want to start your own VPS service, initially hosting about 100 VPSes on a single PC with a 930 GiB hard drive. Hardly any of the VPSes will actually use all of the storage they are allotted, so rather than allocate 9 GiB to each VPS, you could allow each VPS a maximum of 30 GiB and use thin provisioning to only allocate as much hard drive space to each VPS as they are actually using. Suppose the 930 GiB hard drive is . Here is the setup.

Prepare the volume group, .

 # vgcreate MyVolGroup /dev/sdb

Create the thin pool LV, . This LV provides the blocks for storage.

 # lvcreate --type thin-pool -n MyThinPool -l 95%FREE MyVolGroup

The thin pool is composed of two sub-volumes, the data LV and the metadata LV. This command creates both automatically. But the thin pool stops working if either fills completely, and LVM currently does not support the shrinking of either of these volumes. This is why the above command allows for 5% of extra space, in case you ever need to expand the data or metadata sub-volumes of the thin pool.

For each VPS, create a thin LV. This is the block device exposed to the user for their root partition.

 # lvcreate -n SomeClientsRoot -V 30G --thinpool MyThinPool MyVolGroup

The block device  may then be used by a VirtualBox instance as the root partition.

## Use thin snapshots to save more space
Thin snapshots are much more powerful than regular snapshots, because they are themselves thin LVs. See Red Hat's guide for a complete list of advantages thin snapshots have.

Instead of installing Linux from scratch every time a VPS is created, it is more space-efficient to start with just one thin LV containing a basic installation of Linux:

 # lvcreate -n GenericRoot -V 30G --thinpool MyThinPool MyVolGroup
 *** install Linux at /dev/MyVolGroup/GenericRoot ***

Then create snapshots of it for each VPS:

 # lvcreate -s MyVolGroup/GenericRoot -n SomeClientsRoot

This way, in the thin pool there is only one copy the data common to all VPSes, at least initially. As an added bonus, the creation of a new VPS is instantaneous.

Since these are thin snapshots, a write operation to  only causes one COW operation in total, instead of one COW operation per snapshot. This allows you to update  more efficiently than if each VPS were a regular snapshot.

## Example: zero-downtime storage upgrade
There are applications of thin provisioning outside of VPS hosting. Here is how you may use it to grow the effective capacity of an already-mounted file system without having to unmount it. Suppose, again, that the server has a single 930 GiB hard drive. The setup is the same as for VPS hosting, only there is only one thin LV and the LV's size is far larger than the thin pool's size.

 # lvcreate -n MyThinLV -V 16T --thinpool MyThinPool MyVolGroup

This extra virtual space can be filled in with actual storage at a later time by extending the thin pool.

Suppose some time later, a storage upgrade is needed, and a new hard drive, , is plugged into the server. To upgrade the thin pool's capacity, add the new hard drive to the VG:

 # vgextend MyVolGroup /dev/sdc

Now, extend the thin pool:

 # lvextend -l +95%FREE MyVolGroup/MyThinPool

Since this thin LV's size is 16 TiB, you could add another 15.09 TiB of hard drive space before finally having to unmount and resize the file system.

## Customizing
Some customisation is available by editing . You may find it useful to customize the output of  and  which by default does not include the % sync (useful to see progress of conversion between e.g. linear and raid type) and type of logical volume:

{{hc|/etc/lvm/lvm.conf|
report {
 	lvs_cols  "lv_name,lv_attr,lv_active,vg_name,lv_size,lv_layout,lv_allocation_policy,copy_percent,chunk_size"
	pvs_cols  "pv_name,vg_name,pv_size,pv_free,pv_used,dev_size"
}
}}

## Troubleshooting
## LVM commands do not work
* Load proper module:

 # modprobe dm_mod

The  module should be automatically loaded. In case it does not, explicitly load the module at boot.

* Try preceding commands with lvm like this:

 # lvm pvdisplay

## Logical volumes do not show up
If you are trying to mount existing logical volumes, but they do not show up in , you can use the following commands to activate them:

 # vgscan
 # vgchange -ay

## LVM on removable media
Symptoms:

Cause: removing an external LVM drive without deactivating the volume group(s) first. Before you disconnect, make sure to:

 # vgchange -an volume_group_name

Fix: assuming you already tried to activate the volume group with , and are receiving the Input/output errors:

 # vgchange -an volume_group_name

Unplug the external drive and wait a few minutes:

 # vgscan
 # vgchange -ay volume_group_name

## Suspend/resume with LVM and removable media
In order for LVM to work properly with removable media – like an external USB drive – the volume group of the external drive needs to be deactivated before suspend. If this is not done, you may get buffer I/O errors on the dm device (after resume). For this reason, it is not recommended to mix external and internal drives in the same volume group.

To automatically deactivate the volume groups with external USB drives, tag each volume group with the  tag in this way:

 # vgchange --addtag sleep_umount vg_external

Once the tag is set, use the following unit file for systemd to properly deactivate the volumes before suspend. On resume, they will be automatically activated by LVM.

and this script:

Finally, enable the unit.

## Resizing a contiguous logical volume fails
If trying to extend a logical volume errors with:

 " Insufficient suitable contiguous allocatable extents for logical volume "

The reason is that the logical volume was created with an explicit contiguous allocation policy (options  or ) and no further adjacent contiguous extents are available.[https://hostatic.ro/lvm-inherit-and-contiguous-policies/

To fix this, prior to extending the logical volume, change its allocation policy with . If you need to keep the contiguous allocation policy, an alternative approach is to move the volume to a disk area with sufficient free extents. See === Command "grub-mkconfig" reports "unknown filesystem" errors ===

Make sure to remove snapshot volumes before generating grub.cfg.

## Thinly-provisioned root volume device times out
With a large number of snapshots,  runs for a long enough time so that waiting for the root device times out. To compensate, add the  kernel boot parameter to your boot loader configuration.  Or, make  skip checking block mappings (see [https://www.redhat.com/archives/linux-lvm/2016-January/msg00010.html) and regenerate the initramfs:

## Delay on shutdown
If you use RAID, snapshots or thin provisioning and experience a delay on shutdown, make sure  is started. See .

## Hibernating into a thinly-provisioned swap volume
See Power management/Suspend and hibernate#Hibernation into a thinly-provisioned LVM volume.
