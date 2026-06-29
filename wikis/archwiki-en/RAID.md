# RAID

Redundant Array of Independent Disks (RAID) is a storage technology that combines multiple disk drive components—typically disk drives or partitions thereof—into a logical unit. Depending on the RAID implementation, this logical unit can be a file system or an additional transparent layer that can hold several partitions.

Data is distributed across the drives in one of several ways called #RAID levels, depending on the level of redundancy and performance required. The RAID level chosen can thus prevent data loss in the event of a hard disk failure, increase performance or be a combination of both.

This article explains how to create and manage a software RAID array using .

## RAID levels
Despite redundancy implied by most RAID levels, RAID does not guarantee that data is safe. A RAID will not protect data if there is a fire, the computer is stolen or multiple hard drives fail at once. Furthermore, installing a system with RAID is a complex process that may destroy data.

## Standard RAID levels
There are many different levels of RAID; listed below are the most common.

; RAID 0
: Uses striping to combine disks. Even though it does not provide redundancy (actually decreasing reliability), it is still considered RAID. It does, however, provide a big speed benefit. If the speed increase is worth the possibility of data loss (for swap partition for example), choose this RAID level. On a server, RAID 1 and RAID 5 arrays are more appropriate. The size of a RAID 0 array block device is the size of the smallest component partition times the number of component partitions.

; RAID 1
: The most straightforward RAID level: straight mirroring. As with other RAID levels, it only makes sense if the partitions are on different physical disk drives. If one of those drives fails, the block device provided by the RAID array will continue to function as normal. The example will be using RAID 1 for everything except swap and temporary data. Please note that with a software implementation, the RAID 1 level is the only option for the boot partition, because bootloaders reading the boot partition do not understand RAID, but a RAID 1 component partition can be read as a normal partition. The size of a RAID 1 array block device is the size of the smallest component partition.

; RAID 5
: Requires 3 or more physical drives, and provides the redundancy of RAID 1 combined with the speed and size benefits of RAID 0. RAID 5 uses striping, like RAID 0, but also stores parity blocks distributed across each member disk. In the event of a failed disk, these parity blocks are used to reconstruct the data on a replacement disk. RAID 5 can withstand the loss of one member disk.
:

; RAID 6
: Requires 4 or more physical drives, and provides the benefits of RAID 5 but with security against two drive failures. RAID 6 also uses striping, like RAID 5, but stores two distinct parity blocks distributed across each member disk. In the event of a failed disk, these parity blocks are used to reconstruct the data on a replacement disk. RAID 6 can withstand the loss of two member disks. The robustness against unrecoverable read errors is somewhat better, because the array still has parity blocks when rebuilding from a single failed drive. However, given the overhead, RAID 6 is costly and in most settings RAID 10 in far2 layout (see below) provides better speed benefits and robustness, and is therefore preferred.

## Nested RAID levels
; RAID 1+0
: RAID1+0 is a nested RAID that combines two of the standard levels of RAID to gain performance and additional redundancy. It is commonly referred to as RAID10, however, Linux MD RAID10 is slightly different from simple RAID layering, see below.

; RAID 10
: RAID10 under Linux is built on the concepts of RAID1+0, however, it implements this as a single layer, with multiple possible layouts.
: The near X layout on Y disks repeats each chunk X times on Y/2 stripes, but does not need X to divide Y evenly. The chunks are placed on almost the same location on each disk they are mirrored on, hence the name. It can work with any number of disks, starting at 2. Near 2 on 2 disks is equivalent to RAID1, near 2 on 4 disks to RAID1+0.
: The far X layout on Y disks is designed to offer striped read performance on a mirrored array. It accomplishes this by dividing each disk in two sections, say front and back, and what is written to disk 1 front is mirrored in disk 2 back, and vice versa. This has the effect of being able to stripe sequential reads, which is where RAID0 and RAID5 get their performance from. The drawback is that sequential writing has a very slight performance penalty because of the distance the disk needs to seek to the other section of the disk to store the mirror. RAID10 in far 2 layout is, however, preferable to layered RAID1+0 and RAID5 whenever read speeds are of concern and availability / redundancy is crucial.

:

## RAID level comparison
{| class="wikitable"
! RAID level!!Data redundancy!!Physical drive utilization!!Read performance!!Write performance!!Min drives
|-
| 0||||100%||nX

Best
||nX

Best
||2
|-
| 1||||50%||Up to nX if multiple processes are reading, otherwise 1X
||1X||2
|-
| 5||||67% - 94%||(n−1)X

Superior
||(n−1)X

Superior
||3
|-
| 6||||50% - 88%||(n−2)X||(n−2)X||4
|-
| 10,far2||||50%||nX
Best; on par with RAID0 but redundant
||(n/2)X||2
|-
| 10,near2||||50%||Up to nX if multiple processes are reading, otherwise 1X||(n/2)X||2
|}

* Where n is standing for the number of dedicated disks.

## LINEAR
LINEAR allows to map two or more devices into a single device, without parallel accesses like RAID0 but allowing to fully use disks from different sizes. To create a pseudo RAID using this mode without mdadm, one can either use the low-level  utility, the high-level LVM framework or the Btrfs filesystem.

## Implementation
The RAID devices can be managed in different ways:

; Software RAID
: This is the easiest implementation as it does not rely on obscure proprietary firmware and software to be used. The array is managed by the operating system either by:
:* an abstraction layer (e.g. mdadm);
:* a logical volume manager (e.g. LVM);
:* a component of a file system (e.g. ZFS, Btrfs).

; Hardware RAID
: The array is directly managed by a dedicated hardware card installed in the PC to which the disks are directly connected. The RAID logic runs on an on-board processor independently of the host processor (CPU). Although this solution is independent of any operating system, the latter requires a driver in order to function properly with the hardware RAID controller. The RAID array can either be configured via an option rom interface or, depending on the manufacturer, with a dedicated application when the OS has been installed. The configuration is transparent for the Linux kernel: it does not see the disks separately.

; FakeRAID
: This type of RAID is properly called BIOS or Onboard RAID, but is falsely advertised as hardware RAID. The array is managed by pseudo-RAID controllers where the RAID logic is implemented in an option ROM or in the firmware itself with a EFI SataDriver (in case of UEFI), but are not full hardware RAID controllers with all RAID features implemented. Therefore, this type of RAID is sometimes called FakeRAID.  will be used to deal with these controllers. Here are some examples of FakeRAID controllers: Intel Rapid Storage, JMicron JMB36x RAID ROM, AMD RAID, ASMedia 106x, and NVIDIA MediaShield.

## Which type of RAID do I have?
Since software RAID is implemented by the user, the type of RAID is easily known to the user.

However, discerning between FakeRAID and true hardware RAID can be more difficult. As stated, manufacturers often incorrectly distinguish these two types of RAID and false advertising is always possible. The best solution in this instance is to run the  command and looking through the output to find the RAID controller. Then do a search to see what information can be located about the RAID controller. Hardware RAID controllers appear in this list, but FakeRAID implementations do not. Also, true hardware RAID controllers are often rather expensive, so if someone customized the system, then it is very likely that choosing a hardware RAID setup made a very noticeable change in the computer's price.

## Installation
Install . mdadm is used for administering pure software RAID using plain block devices: the underlying hardware does not provide any RAID logic, just a supply of disks. mdadm will work with any collection of block devices. Even if unusual. For example, one can thus make a RAID array from a collection of thumb drives.

## Prepare the devices
If the device is being reused or re-purposed from an existing array, erase any old RAID configuration information:

 # mdadm --misc --zero-superblock /dev/drive

or if a particular partition on a drive is to be deleted:

 # mdadm --misc --zero-superblock /dev/partition

## Partition the devices
It is highly recommended to partition the disks to be used in the array. Since most RAID users are selecting disk drives larger than 2 TiB, GPT is required and recommended. See Partitioning for more information on partitioning and the available partitioning tools.

## GUID Partition Table
* After creating the partitions, their partition type GUIDs should be  (it can be assigned by selecting partition type  in fdisk or  in gdisk).
* If a larger disk array is employed, consider assigning filesystem labels or partition labels to make it easier to identify an individual disk later.
* Creating partitions that are of the same size on each of the devices is recommended.

## Master Boot Record
For those creating partitions on HDDs with a MBR partition table, the partition types IDs available for use are:

*  for non-FS data ( in fdisk). This is the recommended mdadm partition type for RAID arrays on Arch Linux.
*  for RAID autodetect arrays ( in fdisk). This partition type should only be used if RAID autodetection is desireable (non-initramfs system, old mdadm metadata format).

See Linux Raid Wiki:Partition Types for more information.

## Build the array
Use  to build the array. See  for supported options. Several examples are given below.

The following example shows building a 2-device RAID1 array:

 # mdadm --create --verbose --level=1 --raid-devices=2 /dev/md/MyRAID1Array /dev/sdb1 /dev/sdc1

The following example shows building a RAID5 array with 4 active devices and 1 spare device:

 # mdadm --create --verbose --level=5 --raid-devices=4 /dev/md/MyRAID5Array /dev/sdb1 /dev/sdc1 /dev/sdd1 /dev/sde1 --spare-devices=1 /dev/sdf1

The following example shows building a RAID10,far2 array with 2 devices:

 # mdadm --create --verbose --level=10 --raid-devices=2 --layout=f2 /dev/md/MyRAID10Array /dev/sdb1 /dev/sdc1

The array is created under the virtual device , assembled and ready to use (in degraded mode). One can directly start using it while mdadm resyncs the array in the background. It can take a long time to restore parity. Check the progress with:

 $ cat /proc/mdstat

## Update configuration file
By default, most of  is commented out, and it contains just the following:

This directive tells mdadm to examine the devices referenced by  and assemble as many arrays as possible. This is fine if you really do want to start all available arrays and are confident that no unexpected superblocks will be found (such as after installing a new storage device). A more precise approach is to explicitly add the arrays to :

 # mdadm --detail --scan >> /etc/mdadm.conf

This results in something like the following:

This also causes mdadm to examine the devices referenced by . However, only devices that have superblocks with a UUID of  are assembled in to active arrays.

See  for more information.

## Assemble the array
Once the configuration file has been updated the array can be assembled using mdadm:

 # mdadm --assemble --scan

## Format the RAID filesystem
The array can now be formatted with a file system like any other partition, just keep in mind that:

* Due to the large volume size not all filesystems are suited (see: Wikipedia:Comparison of file systems#Limits).
* The filesystem should support growing and shrinking while online (see: Wikipedia:Comparison of file systems#Features).
* One should calculate the correct stride and stripe-width for optimal performance.

## Calculating the stride and stripe width
Two parameters are required to optimise the filesystem structure to fit optimally within the underlying RAID structure: the stride and stripe width. These are derived from the RAID chunk size, the filesystem block size, and the number of "data disks".

The chunk size is a property of the RAID array, decided at the time of its creation. 's current default is 512 KiB. It can be found with :

 # mdadm --detail /dev/mdX | grep 'Chunk Size'

The block size is a property of the filesystem, decided at its creation. The default for many filesystems, including ext4, is 4 KiB. See  for details on ext4.

The number of "data disks" is the minimum number of devices in the array required to completely rebuild it without data loss. For example, this is N for a raid0 array of N devices and N-1 for raid5.

Once you have these three quantities, the stride and the stripe width can be calculated using the following formulas:

 stride = chunk size / block size
 stripe width = number of data disks * stride

## Example 1. RAID0
Example formatting to ext4 with the correct stripe width and stride:

* Hypothetical RAID0 array is composed of 2 physical disks.
* Chunk size is 512 KiB.
* Block size is 4 KiB.

stride = chunk size / block size. In this example, the math is 512/4 so the stride = 128.

stripe width = # of physical data disks * stride. In this example, the math is 2*128 so the stripe width = 256.

 # mkfs.ext4 -v -L myarray -b 4096 -E stride=128,stripe-width=256 /dev/md0

## Example 2. RAID5
Example formatting to ext4 with the correct stripe width and stride:

* Hypothetical RAID5 array is composed of 4 physical disks; 3 data discs and 1 parity disc.
* Chunk size is 512 KiB.
* Block size is 4 KiB.

stride = chunk size / block size. In this example, the math is 512/4 so the stride = 128.

stripe width = # of physical data disks * stride. In this example, the math is 3*128 so the stripe width = 384.

 # mkfs.ext4 -v -L myarray -b 4096 -E stride=128,stripe-width=384 /dev/md0

For more on stride and stripe width, see: RAID Math.

## Example 3. RAID10,far2
Example formatting to ext4 with the correct stripe width and stride:

* Hypothetical RAID10 array is composed of 2 physical disks. Because of the properties of RAID10 in far2 layout, both count as data disks.
* Chunk size is 512 KiB.
* Block size is 4 KiB.

stride = chunk size / block size.
In this example, the math is 512/4 so the stride = 128.

stripe width = # of physical data disks * stride.
In this example, the math is 2*128 so the stripe width = 256.

 # mkfs.ext4 -v -L myarray -b 4096 -E stride=128,stripe-width=256 /dev/md0

## Mounting from a Live CD
Users wanting to mount the RAID partition from a Live CD, use:

 # mdadm --assemble /dev/mdnumber /dev/disk1 /dev/disk2 /dev/disk3 /dev/disk4

If your RAID 1 that is missing a disk array was wrongly auto-detected as RAID 1 (as per ) and reported as inactive (as per ), stop the array first:

 # mdadm --stop /dev/mdnumber

## Installing Arch Linux on RAID
You should create the RAID array between the Partitioning and formatting steps of the Installation Procedure. Instead of directly formatting a partition to be your root file system, it will be created on a RAID array.
Follow the section #Installation to create the RAID array. Then continue with the installation procedure until the pacstrap step is completed.
When using UEFI boot, also read EFI system partition#ESP on software RAID1.

## Update configuration file
After the base system is installed the default configuration file, , must be updated like so:

 # mdadm --detail --scan >> /mnt/etc/mdadm.conf

Always check the  configuration file using a text editor after running this command to ensure that its contents look reasonable.

Continue with the installation procedure until you reach the step Installation guide#Initramfs, then follow the next section.

## Configure mkinitcpio
Install  and add  to the HOOKS array of the  to add support for mdadm into the initramfs image:

Then regenerate the initramfs.

## Configure the boot loader
## Root device
Point the  parameter to the mapped device. E.g.:

 root=/dev/md/MyRAIDArray

If booting from a software raid partition fails using the kernel device node method above, an alternative way is to use one of the methods from Persistent block device naming, for example:

 root=LABEL=Root_Label

See also GRUB#RAID.

## RAID0 layout
Since version 5.3.4 of the Linux kernel, you need to explicitly tell the kernel which RAID0 layout should be used: RAID0_ORIG_LAYOUT () or RAID0_ALT_MULTIZONE_LAYOUT ().You can do this by providing the kernel parameter as follows:

 raid0.default_layout=2

The correct value depends upon the kernel version that was used to create the raid array: use  if created using kernel 3.14 or earlier, use  if using a more recent version of the kernel. One way to check this is to look at the creation time of the raid array:

Here we can see that this raid array was created on September 24, 2015. The release date of Linux Kernel 3.14 was March 30, 2014, and as such this raid array is most likely created using a multizone layout ().

## RAID Maintenance
## Scrubbing
It is good practice to regularly run data scrubbing to check for and fix errors. Depending on the size/configuration of the array, a scrub may take multiple hours to complete.

To initiate a data scrub:

 # echo check > /sys/block/mdX/md/sync_action

Alternatively, you may enable the included  which performs weekly scans.

The check operation scans the drives for bad sectors and automatically repairs them. If it finds good sectors that contain bad data (i.e. a mismatch, the data in a sector does not agree with what the data from another disk indicates that it should be, for example the parity block + the other data blocks would cause us to think that this data block is incorrect), then no action is taken, but the event is logged (see below). This "do nothing" allows admins to inspect the data in the sector and the data that would be produced by rebuilding the sectors from redundant information and pick the correct data to keep.

As with many tasks/items relating to mdadm, the status of the scrub can be queried by reading .

Example:

To stop a currently running data scrub safely:

 # echo idle > /sys/block/md0/md/sync_action

When the scrub is complete, admins may check how many blocks (if any) have been flagged as bad:

 # cat /sys/block/md0/md/mismatch_cnt

## General notes on scrubbing
It is a good idea to set up a cron job as root to schedule a periodic scrub. See  which can assist with this. To perform a periodic scrub using systemd timers instead of cron, See  which contains the same script along with associated systemd timer unit files.

## RAID1 and RAID10 notes on scrubbing
Due to the fact that RAID1 and RAID10 writes in the kernel are unbuffered, an array can have non-0 mismatch counts even when the array is healthy. These non-0 counts will only exist in transient data areas where they do not pose a problem. However, we cannot tell the difference between a non-0 count that is just in transient data or a non-0 count that signifies a real problem. This fact is a source of false positives for RAID1 and RAID10 arrays. It is however still recommended to scrub regularly in order to catch and correct any bad sectors that might be present in the devices.

## Removing devices from an array
One can remove a block device from the array after marking it as faulty:

 # mdadm --fail /dev/md0 /dev/failing_array_member

Now remove it from the array:

 # mdadm --remove /dev/md0 /dev/failing_array_member

If the device has not failed entirely, but you would like to replace it, e.g. because it looks like it is dying, you can actually handle replacement more gracefully by first adding a new drive and then telling mdadm to replace it.

For example, with  as the new one and  as the failing one:

 # mdadm /dev/md0 --add /dev/sdc1
 # mdadm /dev/md0 --replace /dev/sdb1 --with /dev/sdc1

The  part is optional, but more explicit. See [https://unix.stackexchange.com/questions/74924/how-to-safely-replace-a-not-yet-failed-disk-in-a-linux-raid5-array/104052#104052 for more details.

To remove a device permanently (for example, to use it individually from now on), follow the steps above (fail/remove or add/replace) and then run:

 # mdadm --zero-superblock /dev/failing_array_member

Stop using an array:

# Umount target array
# Stop the array with:
# Repeat the three command described in the beginning of this section on each device.
# Remove the corresponding line from .

## Adding a new device to an array
Adding new devices with mdadm can be done on a running system with the devices mounted.
Partition the new device using the same layout as one of those already in the arrays as discussed above.

Assemble the RAID array if it is not already assembled:

 # mdadm --assemble /dev/md0 /dev/sda1 /dev/sdb1

Add the new device to the array:

 # mdadm --add /dev/md0 /dev/sdc1

This should not take long for mdadm to do.

Depending on the type of RAID (for example, with RAID1), mdadm may add the device as a spare without syncing data to it. You can increase the number of disks the RAID uses by using  with the  option. For example, to increase an array to four disks:

 # mdadm --grow /dev/md0 --raid-devices=4

You can check the progress with:

 # cat /proc/mdstat

Check that the device has been added with the command:

 # mdadm --misc --detail /dev/md0

## Increasing size of a RAID volume
If larger disks are installed in a RAID array or partition size has been increased, it may be desirable to increase the size of the RAID volume to fill the larger available space. This process may be begun by first following the above sections pertaining to replacing disks. Once the RAID volume has been rebuilt onto the larger disks it must be "grown" to fill the space.

 # mdadm --grow /dev/md0 --size=max

Next, partitions present on the RAID volume  may need to be resized. See Partitioning for details. Finally, the filesystem on the above mentioned partition will need to be resized. If partitioning was performed with  this will be done automatically. If other tools were used, unmount and then resize the filesystem manually.

 # umount /storage
 # fsck.ext4 -f /dev/md0p1
 # resize2fs /dev/md0p1

## Change sync speed limits
Syncing can take a while. If the machine is not needed for other tasks the speed limit can be increased.

In the above example, it would seem the max speed is limited to approximately 238 M/sec.

Check the current speed limit (in kibibytes per second, KiB/s):

Set a new maximum speed of raid resyncing operations using sysctl:

 # sysctl -w dev.raid.speed_limit_min=600000
 # sysctl -w dev.raid.speed_limit_max=600000

Then check out the syncing speed and estimated finish time.

## RAID5 performance
To improve RAID5 performance for fast storage (e.g. NVMe), increase  to more threads. For example, to use 8 threads to operate on a RAID5 device:

 # echo 8 > /sys/block/md0/md/group_thread_cnt

See git kernel commit 851c30c9badf.

## Update RAID superblock
To update the RAID superblock, you need to first unmount the array and then stop the array with the following command:

 # mdadm --stop /dev/md0

Then you can update certain parameters by reassembling the array. For example, to update the :

 # mdadm --assemble --update=homehost --homehost=NAS /dev/md0 /dev/sda1 /dev/sdb1

See the arguments of  for details.

## Monitoring
A simple one-liner that prints out the status of the RAID devices:

{{hc|# awk '/^md/ {printf "%s: ", $1}; /blocks/ {print $NF}'  /sys/module/md_mod/parameters/start_ro

## Recovering from a broken or missing drive in the raid
You might get the above mentioned error also when one of the drives breaks for whatever reason. In that case you will have to force the raid to still turn on even with one disk short. Type this (change where needed):

 # mdadm --manage /dev/md0 --run

Now you should be able to mount it again with something like this (if you had it in fstab):

 # mount /dev/md0

Now the raid should be working again and available to use, however with one disk short. So, to add that one disc partition it the way like described above in #Prepare the devices. Once that is done you can add the new disk to the raid by doing:

 # mdadm --manage --add /dev/md0 /dev/sdd1

If you type:

 # cat /proc/mdstat

you probably see that the raid is now active and rebuilding.

You also might want to update your configuration (see: #Update configuration file).

## Benchmarking
There are several tools for benchmarking a RAID. The most notable improvement is the speed increase when multiple threads are reading from the same RAID volume.

 tests database type access to one or more files, and creation, reading, and deleting of small files which can simulate the usage of programs such as Squid, INN, or Maildir format e-mail. The enclosed ZCAV program tests the performance of different zones of a hard drive without writing any data to the disk.

hdparm should not be used to benchmark a RAID, because it provides very inconsistent results.
