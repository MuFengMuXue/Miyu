# Bcache

Bcache (block cache) allows one to use an SSD as a read/write cache (in writeback mode) or read cache (writethrough or writearound) for another blockdevice (generally a rotating HDD or array). This article will show how to install Arch using Bcache as the root partition. For an intro to bcache itself, see the bcache homepage. Be sure to read and reference the bcache manual.

Bcache needs the backing device to be formatted as a bcache block device.  In most cases, blocks to-bcache can do an in-place conversion.

## Setting up bcached btrfs file systems on an existing system
## Preparation
Install .

Use fdisk to create the appropriate partitions on the SSD's and hard drives to hold the cache and the backing data.

## Situation: 1 hard drive and 1 read cache SSD
 +--------------+
 | btrfs /mnt   |
 +--------------+
 | /dev/Bcache0 |
 +--------------+
 | Cache        |
 | /dev/sdk1    |
 +--------------+
 | Data         |
 | /dev/sdv1    |
 +--------------+

1. Format the backing device (This will typically be your mechanical drive). The backing device can be a whole device, a partition or any other standard block device. This will create /dev/bcache0

 # make-bcache -B /dev/sdv1

2. Format the cache device (This will typically be your SSD). The cache device can be a whole device, a partition or any other standard block device

 # make-bcache -C /dev/sdk1

In this example the default block and bucket sizes of 512B and 128kB are used. The block size should match the backing devices sector size which will usually be either 512 or 4k. The bucket size should match the erase block size of the caching device with the intent of reducing write amplification. For example, using a HDD with 4k sectors and an SSD with an erase block size of 2MB this command would look like

 # make-bcache --block 4k --bucket 2M -C /dev/sdk1

3. Get the uuid of the cache device

 # bcache-super-show /dev/sdk1 | grep cset
 cset.uuid		f0e01318-f4fd-4fab-abbb-d76d870503ec

4. Register the cache device against your backing device. Replace the example uuid with the uuid of your cache. Udev rules will take care of this on reboot and will only need to be done once.

 # echo f0e01318-f4fd-4fab-abbb-d76d870503ec > /sys/block/bcache0/bcache/attach

5. Create the btrfs filesystem.

 # mkfs.btrfs /dev/bcache0

6. mount the filesystem

 # mount /dev/bcache0 /mnt

7. If you want to have this partition available during the initcpio (i.e. you require it at some point in the boot process) you need to add 'bcache' to your modules array in /etc/mkinitcpio.conf as well as adding the 'bcache' hook in your list between block and filesystems. You must then regenerate the initramfs.

## Situation: 4 hard drives and 1 read cache SSD
 +-----------------------------------------------------------+
 |                         btrfs /mnt                        |
 +--------------+--------------+--------------+--------------+
 | /dev/Bcache0 | /dev/Bcache1 | /dev/Bcache2 | /dev/Bcache3 |
 +--------------+--------------+--------------+--------------+
 |                           Cache                           |
 |                         /dev/sdk1                         |
 +--------------+--------------+--------------+--------------+
 | Data         | Data         | Data         | Data         |
 | /dev/sdv1    | /dev/sdw1    | /dev/sdx1    | /dev/sdy1    |
 +--------------+--------------+--------------+--------------+

1. Format the backing devices (These will typically be your mechanical drives). The backing devices can be whole devices, partitions or any other standard block devices. This will create /dev/bcache0, /dev/bcache1, /dev/bcache2 and /dev/bcache3

 # make-bcache -B /dev/sdv1
 # make-bcache -B /dev/sdw1
 # make-bcache -B /dev/sdx1
 # make-bcache -B /dev/sdy1

2. Format the cache device (This will typically be your SSD). The cache device can be a whole device, a partition or any other standard block device. Only one cache device can be added to a group of backing devices.

 # make-bcache -C /dev/sdk1

3. Get the uuid of the cache device

 # bcache-super-show /dev/sdk1 | grep cset
 cset.uuid		f0e01318-f4fd-4fab-abbb-d76d870503ec

4. Register the cache device against your backing devices. Replace the example uuid with the uuid of your cache.

 # echo f0e01318-f4fd-4fab-abbb-d76d870503ec > /sys/block/bcache0/bcache/attach
 # echo f0e01318-f4fd-4fab-abbb-d76d870503ec > /sys/block/bcache1/bcache/attach
 # echo f0e01318-f4fd-4fab-abbb-d76d870503ec > /sys/block/bcache2/bcache/attach
 # echo f0e01318-f4fd-4fab-abbb-d76d870503ec > /sys/block/bcache3/bcache/attach

5. Create the btrfs filesystem. Both the data and the metadata is stored twice in the array, so there will be no data loss when a single hard drive fails. The -L argument defines the label of the filesystem.

 # mkfs.btrfs -L STORAGE -f -d raid1 -m raid1 /dev/bcache0 /dev/bcache1 /dev/bcache2 /dev/bcache3

6. mount the filesystem

 # mount /dev/bcache0 /mnt

## Situation: 3 hard drives and 3 read/write cache SSD's
 +--------------------------------------------+
 |                  btrfs /mnt                |
 +--------------+--------------+--------------+
 | /dev/Bcache0 | /dev/Bcache1 | /dev/Bcache2 |
 +--------------+--------------+--------------+
 | Cache        | Cache        | Cache        |
 | /dev/sdk1    | /dev/sdl1    | /dev/sdm1    |
 +--------------+--------------+--------------+
 | Data         | Data         | Data         |
 | /dev/sdv1    | /dev/sdw1    | /dev/sdx1    |
 +--------------+--------------+--------------+

1. Format the backing devices (These will typically be your mechanical drives). The backing devices can be whole devices, partitions or any other standard block devices. This will create /dev/bcache0, /dev/bcache1 and /dev/bcache2.

 # make-bcache -B /dev/sdv1
 # make-bcache -B /dev/sdw1
 # make-bcache -B /dev/sdx1

2. Format the cache devices (This will typically be your SSD's). The cache devices can be whole devices, partitions or any other standard block devices. To avoid data loss in case of a failing SSD, each backing device needs its own SSD if it is in writeback mode. Cache SSD's in writethrough and in writearound mode can be shared by multiple backing devices, as they do not cause data loss when they fail.

 # make-bcache -C /dev/sdk1
 # make-bcache -C /dev/sdl1
 # make-bcache -C /dev/sdm1

3. Get the uuid of the cache devices

 # bcache-super-show /dev/sdk1 | grep cset
 cset.uuid		f0e01318-f4fd-4fab-abbb-d76d870503ec
 # bcache-super-show /dev/sdl1 | grep cset
 cset.uuid		4b05ce02-19f4-4cc6-8ca0-1f765671ceda
 # bcache-super-show /dev/sdm1 | grep cset
 cset.uuid		75ff0598-7624-46f6-bcac-c27a3cf1a09f

4. Register the cache devices against your backing devices. Replace the example uuid's with the uuid's of your caches.

 # echo f0e01318-f4fd-4fab-abbb-d76d870503ec > /sys/block/bcache0/bcache/attach
 # echo 4b05ce02-19f4-4cc6-8ca0-1f765671ceda > /sys/block/bcache1/bcache/attach
 # echo 75ff0598-7624-46f6-bcac-c27a3cf1a09f > /sys/block/bcache2/bcache/attach

5. enable writeback mode

 # echo writeback > /sys/block/bcache0/bcache/cache_mode
 # echo writeback > /sys/block/bcache1/bcache/cache_mode
 # echo writeback > /sys/block/bcache2/bcache/cache_mode

6. Create the btrfs filesystem. Both the data and the metadata is stored twice in the array, so there will be no data loss when a single hard drive fails. The -L argument defines the label of the filesystem.

 # mkfs.btrfs -L STORAGE -f -d raid1 -m raid1 /dev/bcache0 /dev/bcache1 /dev/bcache2

7. mount the filesystem

 # mount /dev/bcache0 /mnt

## Situation: 5 hard drives and 3 cache SSD's
 +--------------------------------------------------------------------------+
 |                                btrfs /mnt                                |
 +--------------+--------------+--------------+--------------+--------------+
 | /dev/Bcache0 | /dev/Bcache1 | /dev/Bcache2 | /dev/Bcache3 | /dev/Bcache4 |
 +--------------+--------------+--------------+--------------+--------------+
 | WriteB Cache |     Writethrough or writearound Cache      | WriteB Cache |
 | /dev/sdk1    |                 /dev/sdl1                  | /dev/sdm1    |
 +--------------+--------------+--------------+--------------+--------------+
 | Data         | Data         | Data         | Data         | Data         |
 | /dev/sdv1    | /dev/sdw1    | /dev/sdx1    | /dev/sdy1    | /dev/sdz1    |
 +--------------+--------------+--------------+--------------+--------------+

1. Format the backing devices (These will typically be your mechanical drives). The backing devices can be whole devices, partitions or any other standard block devices. This will create /dev/bcache0, /dev/bcache1, /dev/bcache2, /dev/bcache3 and /dev/bcache4.

 # make-bcache -B /dev/sdv1
 # make-bcache -B /dev/sdw1
 # make-bcache -B /dev/sdx1
 # make-bcache -B /dev/sdy1
 # make-bcache -B /dev/sdz1

2. Format the cache devices (This will typically be your SSD's). The cache devices can be whole devices, partitions or any other standard block devices. To avoid data loss in case of a failing SSD, each backing device needs its own SSD if it is in writeback mode. Cache SSD's in writethrough and in writearound mode can be shared by multiple backing devices, as they do not cause data loss when they fail.

 # make-bcache -C /dev/sdk1
 # make-bcache -C /dev/sdl1
 # make-bcache -C /dev/sdm1

3. Get the uuid of the cache devices

 # bcache-super-show /dev/sdk1 | grep cset
 cset.uuid		f0e01318-f4fd-4fab-abbb-d76d870503ec
 # bcache-super-show /dev/sdl1 | grep cset
 cset.uuid		4b05ce02-19f4-4cc6-8ca0-1f765671ceda
 # bcache-super-show /dev/sdm1 | grep cset
 cset.uuid		75ff0598-7624-46f6-bcac-c27a3cf1a09f

4. Register the cache devices against your backing devices. Replace the example uuid's with the uuid's of your caches.

 # echo f0e01318-f4fd-4fab-abbb-d76d870503ec > /sys/block/bcache0/bcache/attach
 # echo 4b05ce02-19f4-4cc6-8ca0-1f765671ceda > /sys/block/bcache1/bcache/attach
 # echo 4b05ce02-19f4-4cc6-8ca0-1f765671ceda > /sys/block/bcache2/bcache/attach
 # echo 4b05ce02-19f4-4cc6-8ca0-1f765671ceda > /sys/block/bcache3/bcache/attach
 # echo 75ff0598-7624-46f6-bcac-c27a3cf1a09f > /sys/block/bcache4/bcache/attach

5. enable writeback mode on non-shared caches

 # echo writeback > /sys/block/bcache0/bcache/cache_mode
 # echo writeback > /sys/block/bcache4/bcache/cache_mode

6. Create the btrfs filesystem. Both the data and the metadata is stored twice in the array, so there will be no data loss when a single hard drive fails. The -L argument defines the label of the filesystem.

 # mkfs.btrfs -L STORAGE -f -d raid1 -m raid1 /dev/bcache0 /dev/bcache1 /dev/bcache2 /dev/bcache3 /dev/bcache4

7. mount the filesystem

 # mount /dev/bcache0 /mnt

## Bcache management
1. Check that everything has been correctly setup

 # cat /sys/block/bcache0/bcache/state

The output can be:

* : this means you have not attached a caching device to your backing bcache device
* clean: this means everything is ok. The cache is clean.
* dirty: this means everything is setup fine and that you have enabled writeback and that the cache is dirty.
* inconsistent: you are in trouble because the backing device is not in sync with the caching device

You can have a  device associated with a backing device with no caching device attached. This means that all I/O (read/write) are passed directly to the backing device (pass-through mode)

2. See what caching mode is in use

In the above example, the writethrough mode is enabled.

3. Show info about a bcached device:

 # bcache-super-show /dev/sdXY

4. Stop the backing device:

 # echo 1 > /sys/block/sdX/sdX5. Detach a caching device:

 # echo 1 > /sys/block/sdX/sdX[Y/bcache/detach

6. Safely remove the cache device

 # echo cache-set-uuid > /sys/block/bcache0/bcache/detach

7. Release attached devices

 # echo 1 > /sys/fs/bcache/cache-set-uuid/stop

## Installation to a bcache device
1. Boot on the install disk (2013.08.01 minimum).

2. Install the .

3. Partition your HDD

grub cannot handle bcache, so you will need at least 2 partitions (boot and one for the bcache backing device). If you are doing UEFI, you will need an EFI system partition (ESP) as well. E.g.:

    1            2048         2099199   1024.0 MiB  EF00  EFI system partition
    2         2099200         4196351   1024.0 MiB  EA00  arch_boot
    3         4196352       499998719   236.4 GiB   8300  bcache_backing

4. Configure your HDD as a bcache backing device.

 # make-bcache -B /dev/sda3

 # make-bcache -B /dev/sd? /dev/sd? -C /dev/sd?

You now have a  device.

5. Configure your SSD

Format the SSD as a caching device and link it to the backing device

 # make-bcache -C /dev/sdb
 # echo /dev/sdb > /sys/fs/bcache/register
 # echo UUID__from_previous_command > /sys/block/bcache0/bcache/attach

6. Format the bcache device. Use LVM or btrfs subvolumes if you want to divide up the  device how you like (ex for separate , , , etc):

 # mkfs.btrfs /dev/bcache0
 # mount /dev/bcache0 /mnt/
 # btrfs subvolume create /mnt/root
 # btrfs subvolume create /mnt/home
 # umount /mnt

You can even setup LUKS on it if you want using e.g. cryptsetup. Referencing the bcache device in the 'cryptdevice' kernel option will work fine, for instance.

7. Prepare the installation mount point:

 # mkfs.ext4 /dev/sda2
 # mkfs.fat -F 32 /dev/sda1

Now install  package. Then:

 # mount /dev/bcache0 -o subvol=root,compress=lzo /mnt/
 # mount --mkdir /dev/bcache0 -o subvol=home,compress=lzo /mnt/home
 # mount --mkdir /dev/sda2 /mnt/boot
 # mount --mkdir /dev/sda1 /mnt/efi

8. Install the system as per the Installation guide as normal except this:

Before you edit  and run :

* Install .
* Edit :
** add the "bcache" module
** add the "bcache" hook between block and filesystem hooks

## Accessing from the install disk
This is how to access a bcache partition from the install disk that was present before the install disk was booted. Boot the install disk and install  from the AUR, just as in the previous section. Then, add the module to the kernel:

 # modprobe bcache

Your device will not appear immediately at . To force the kernel to find it, tell it to reread the partition table:

 # partprobe

Now,  should be present, and you can carry on mounting, reformatting, etc. from here.

To start the cache without having to configure the internet and install , load the kernel module just as before—it is included in the mainline kernel. Then start the cache by registering all of the slave devices:

 # echo /dev/sdX > /sys/fs/bcache/register
 # echo /dev/sdY > /sys/fs/bcache/register
 # ...

The bcache device will appear right after the last required slave device is registered.

A writethrough backing device can be started without having to register any caches. This can be done if there are a lot of them and you are in a hurry, or if some of the caches are inaccessible for some reason. Register the device, as above, then start it:

 # echo 1 > /sys/block/sdX/bcache/running

Bcache has not actually detached any caches, and will still add any cache devices if they are registered. This command will "work" on writeback backing devices, but there will be massive data corruption. Only do this if the missing cache is totally unrecoverable.

## Configuring
There are many options that can be configured (such as cache mode, cache flush interval, sequential write heuristic, etc.) This is currently done by writing to files in . See the bcache user documentation.

Changing the cache mode is done by echoing one of , ,  or  to .

Note that some changes to  are temporary, and will revert back after a reboot (It seems that at least cache_mode does not need this workaround). To set custom configurations at boot create a .conf file in . To set, in a persistent fashion, the sequential cutoff for  to 1 MB  and write back you could create a file  with the contents:

 w /sys/block/bcache0/bcache/sequential_cutoff - - - - 1M
 w /sys/block/bcache0/bcache/cache_mode        - - - - writeback

## Situation: Prevent all write access to a HDD
In this situation the goal is to keep the HDD idle as long as possible. This is achieved by absorbing all writes with the SSD. The hard drive is only activated when the SSD is full, or when something is read that's not on the SSD.

Enable the writeback cache mode:

 # echo writeback > /sys/block/bcache0/bcache/cache_mode

Let bcache completely sync with the hard drive.

 # echo 0 > /sys/block/bcache0/bcache/writeback_percent

Don't let sequential IO bypass the cache:

 # echo 0 > /sys/block/bcache0/bcache/sequential_cutoff

Let bcache wait a week after the previous sync is done:

 # echo $((7*24*60*60)) > /sys/block/bcache0/bcache/writeback_delay

Don't let bcache go around the cache when there's read / write congestion

 # echo 0 > /sys/fs/bcache//congested_read_threshold_us
 # echo 0 > /sys/fs/bcache//congested_write_threshold_us

Put the HDD to sleep after 20 minutes:
 # hdparm -S 240  /dev/$(cat /sys/block/bcache0/bcache/backing_dev_name)
 /dev/sdh1:
 setting standby to 240 (20 minutes)

 First use lsblk to get the device names of the HDD and SSD. In this example /dev/sdh1 is the HDD, /dev/sdc1 is the SSD:

 # lsblk -M -s
 bcache0   254:0    0 931.5G  0 disk
    ├─sdc1      8:33   0 111.8G  0 part
    │ └─sdc     8:32   0 111.8G  0 disk
    └─sdh1      8:113  0 931.5G  0 part
      └─sdh     8:112  0 931.5G  0 disk

Now Dstat can be used to monitor disk access to the members of the bcache set.

 $ dstat -D sdc1,sdh1

## Advanced operations
## Resize backing device
It is possible to resize the backing device so long as you do not move the partition start. This process is described in the mailing list. Here is an example using btrfs volume directly on bcache0. For LVM containers or for other filesystems, procedure will differ.

## Example of growing
In this example, I grow the filesystem by 4GB.

1. Reboot to a live CD/USB Drive (need not be bcache enabled) and use fdisk, gdisk, parted, or your other favorite tool to delete the backing partition and recreate it with the same start and a total size 4G larger.

2. Reboot to your normal install. Your filesystem will be currently mounted. That is fine. Issue the command to resize the partition to its maximum. For btrfs, that is

 # btrfs filesystem resize max /

For ext3/4, that is:

 # resize2fs /dev/bcache0

## Example of shrinking
In this example, I shrink the filesystem by 4GB.

1. Disable writeback cache (switch to writethrough cache) and wait for the disk to flush.

 # echo writethrough > /sys/block/bcache0/bcache/cache_mode
 $ watch cat /sys/block/bcache0/bcache/state

wait until state reports "clean". This might take a while.

## Force flush of cache to backing device
I suggest to use

  # echo 0 > /sys/block/bcache0/bcache/writeback_percent

This will flush the dirty data of the cache to the backing device in less a minute.

Revert back the value after with

 # echo 10 > /sys/block/bcache0/bcache/writeback_percent

2. Shrink the mounted filesystem by something more than the desired amount, to ensure we do not accidentally clip it later. For btrfs, that is:

 # btrfs filesystem resize -5G /

For ext3/4 you can use resize2fs, but only if the partition is unmounted

 # umount /home
 # resize2fs /dev/bcache0 283G

3. Reboot to a LiveCD/USB drive (does not need to support bcache) and use fdisk, gdisk, parted, or your other favorite tool to delete the backing partition and recreate it with the same start and a total size 4G smaller.

4. Reboot to your normal install. Your filesystem will be currently mounted. That is fine. Issue the command to resize the partition to its maximum (that is, the size we shrunk the actual partition to in step 3). For btrfs, that is:

 # btrfs filesystem resize max /

For ext3/4, that is:

 # resize2fs /dev/bcache0

5. Re-enable writeback cache if you want that enabled:

 # echo writeback > /sys/block/bcache0/bcache/cache_mode

## Troubleshooting
## /dev/bcache device does not exist on bootup
If you are sent to a busy box shell with an error:

This might happen if the backing device is configured for "writeback" mode (default is writearound). When in "writeback" mode, the /dev/bcache0 device is not started until the cache device is both registered and attached. Registering is something that needs to happen every bootup, but attaching should only have to be done once.

To continue booting, try one of the following:

* Register both the backing device and the caching device

 # echo /dev/sda3 > /sys/fs/bcache/register
 # echo /dev/sdb > /sys/fs/bcache/register

If the /dev/bcache0 device now exists, type exit and continue booting. You will need to fix your initcpio to ensure devices are registered before mounting the root device.

* Re-attach the cache to the backing device:

If the cache device was registered, a folder with the UUID of the cache should exist in . Use that UUID when following the example below:

 # echo b6b2d82b-f87e-44d5-bbc5-c51dd7aace15 > /sys/block/sda/sda3/bcache/attach

If the  device now exists, type exit and continue booting. You should not have to do this again. If it persists, ask on the bcache mailing list.

* Invalidate the cache and force the backing device to run without it. You might want to check some stats, such as "dirty_data" so you have some idea of how much data will be lost.

dirty data is data in the cache that has not been written to the backing device. If you force the backing device to run, this data will be lost, even if you later re-attach the cache.

 # echo 1 > /sys/block/sda/sda3/bcache/running

The  device will now exist. Type exit and continue booting. You might want to unregister the cache device and run make-bcache again. An fsck on  would also be wise. See the bcache documentation.

## /sys/fs/bcache/ does not exist
The kernel you booted is not bcache enabled, or you the bcache module is not loaded

## write error: Invalid argument when trying to attach a device due to mismatched block parameter
Given  when trying to attach a device, and the actual error is shown with dmesg:

 bcache: bch_cached_dev_attach() Couldn't attach sdc: block size less than set's block size

This happens because the  parameter was not set on either device and defaults can mismatch.

Creating both the backing and caching device in one command automatically solves the issue, but when using separate commands the block size parameter sometimes needs to be set manually on both devices.

## Device or resource busy
When a device is in use as a bcache backing device, it can not be formatted nor partitioned:
 # make-bcache -C /dev/sdb1
 Can't open dev /dev/sdb1: Device or resource busy

 # fdisk /dev/sdb

 Welcome to fdisk (util-linux 2.37.2).
 Changes will remain in memory only, until you decide to write them.
 Be careful before using the write command.

 This disk is currently in use - repartitioning is probably a bad idea.
 It's recommended to umount all file systems, and swapoff all swap
 partitions on this disk.

 Command (m for help): q

To fix this, first run this command to confirm the disk is actually used as a bcache backing device:
 # bcache-super-show /dev/sdb1
 sb.magic		ok
 sb.first_sector		8 sb.csum			A3D2B8610F6C5E35 [match
 sb.version		1 device

 dev.label		(empty)
 dev.uuid		5a868788-65a2-4564-b4b7-c1817d0b6080
 dev.sectors_per_block	1
 dev.sectors_per_bucket	1024
 dev.data.first_sector	16
 dev.data.cache_mode	1 dev.data.cache_state	2 [dirty

 cset.uuid		42dcb651-6b53-4b65-bc49-9b1ca0acc5b1

Then stop the backing device. This will also remove the corresponding /dev/bcache device.
 # echo 1 > /sys/class/block/sdb1/bcache/stop

 # dmesg
 [ 3171.263577] bcache: bcache_device_free() bcache0 stopped
Now the device can be partitioned:
 # fdisk /dev/sdb

 Welcome to fdisk (util-linux 2.37.2).
 Changes will remain in memory only, until you decide to write them.
 Be careful before using the write command.

 Command (m for help): q
When fdisk exits, the kernel scans the drive again, notices it's a bcache backing device, and uses the drive as a backing device.
 # dmesg
 [ 3190.643270]  sdb: sdb1
 [ 3190.833029] bcache: register_bdev() registered backing device sdb1
This creates the directory bcache under /sys/class/block/sdb1/
 # ls /sys/class/block/sdb1/
 alignment_offset  bcache  dev  discard_alignment  holders  inflight  partition	power  ro  size  start	stat  subsystem  uevent
