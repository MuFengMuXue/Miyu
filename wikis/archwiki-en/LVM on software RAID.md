# LVM on software RAID

This article will provide an example of how to install and configure Arch Linux with Logical Volume Manager (LVM) on top of a software RAID.

## Introduction
Although RAID and LVM may seem like analogous technologies they each present unique features. This article uses an example with three similar 1TB SATA hard drives. The article assumes that the drives are accessible as , , and .

{| class="wikitable" style="text-align:center;"
|-
|
| colspan="3" |
| colspan="3" |
| colspan="3" |
| colspan="3" |
|-
|
| colspan="12" |
|-
|
| colspan="6" |
| colspan="6" |
|-
|
| colspan="2" |
| colspan="2" |
| colspan="2" |
| colspan="2" |
| colspan="2" |
| colspan="2" |
|-
|
| colspan="4" |
| colspan="4" |
| colspan="4" |
|}

## Swap space
Many tutorials treat the swap space differently, either by creating a separate RAID1 array or a LVM logical volume. Creating the swap space on a separate array is not intended to provide additional redundancy, but instead, to prevent a corrupt swap space from rendering the system inoperable, which is more likely to happen when the swap space is located on the same partition as the root directory.

## Boot loader
This tutorial will use Syslinux instead of GRUB. GRUB when used in conjunction with GPT requires an additional BIOS boot partition.

GRUB supports the default style of metadata currently created by mdadm (i.e. 1.2) when combined with an initramfs, which has replaced in Arch Linux with mkinitcpio. Syslinux only supports version 1.0, and therefore requires the  option.

Some boot loaders (e.g. GRUB Legacy, LILO) will not support any 1.x metadata versions, and instead require the older version, 0.90. If you would like to use one of those boot loaders make sure to add the option  to the  array during RAID installation.

## Installation
Obtain the latest installation media and boot the Arch Linux installer as outlined in the installation guide.

## Load kernel modules
Load the appropriate RAID (e.g. , , , , ) and LVM (i.e. ) modules. The following example makes use of RAID1 and RAID5.

 # modprobe raid1
 # modprobe raid5
 # modprobe dm-mod

## Prepare the hard drives
Partition each hard drive with a 1 GiB  partition, a 4 GiB  partition, and a  partition that takes up the remainder of the disk.

The boot partition must be RAID1; i.e it cannot be striped (RAID0) or RAID5, RAID6, etc.. This is because GRUB does not have RAID drivers. Any other level will prevent your system from booting. Additionally, if there is a problem with one boot partition, the boot loader can boot normally from the other two partitions in the  array.

## RAID installation
After creating the physical partitions, you are ready to setup the /boot, /swap, and / arrays with . It is an advanced tool for RAID management that will be used to create a  within the installation environment.

Create the / array at :

 # mdadm --create /dev/md0 --level=5 --raid-devices=3 /dev/sdCreate the /swap array at :

 # mdadm --create /dev/md1 --level=1 --raid-devices=3 /dev/sd[abc2

Create the /boot array at :

 # mdadm --create /dev/md2 --level=1 --raid-devices=3 --metadata=1.0 /dev/sd==== Synchronization ====

After you create a RAID volume, it will synchronize the contents of the physical partitions within the array. You can monitor the progress by refreshing the output of  ten times per second with:

 # watch -n .1 cat /proc/mdstat

Further information about the arrays is accessible with:

 # mdadm --misc --detail /dev/md[012

Once synchronization is complete the  line should read . Each device in the table at the bottom of the output should read  or   in the  column.  means each device is actively in the array.

## Scrubbing
It is good practice to regularly run data scrubbing to check for and fix errors.

To initiate a data scrub:

 # echo check > /sys/block/md0/md/sync_action

As with many tasks/items relating to mdadm, the status of the scrub can be queried:

 # cat /proc/mdstat

Example:

To stop a currently running data scrub safely:

 # echo idle > /sys/block/md0/md/sync_action

When the scrub is complete, admins may check how many blocks (if any) have been flagged as bad:

 # cat /sys/block/md0/md/mismatch_cnt

The check operation scans the drives for bad sectors and mismatches. Bad sectors are automatically repaired. If it finds mismatches, i.e., good sectors that contain bad data (the data in a sector does not agree with what the data from another disk indicates that it should be, for example the parity block + the other data blocks would cause us to think that this data block is incorrect), then no action is taken, but the event is logged (see below).  This "do nothing" allows admins to inspect the data in the sector and the data that would be produced by rebuilding the sectors from redundant information and pick the correct data to keep.

## General Notes on Scrubbing
It is a good idea to set up a cron job as root to schedule a periodic scrub. See  which can assist with this.

## RAID1 and RAID10 Notes on Scrubbing
Due to the fact that RAID1 and RAID10 writes in the kernel are unbuffered, an array can have non-0 mismatch counts even when the array is healthy.  These non-0 counts will only exist in transient data areas where they do not pose a problem.  However, since we cannot tell the difference between a non-0 count that is just in transient data or a non-0 count that signifies a real problem.  This fact is a source of false positives for RAID1 and RAID10 arrays.  It is however recommended to still scrub to catch and correct any bad sectors there might be in the devices.

## LVM installation
This section will convert the two RAIDs into physical volumes (PVs). Then combine those PVs into a volume group (VG). The VG will then be divided into logical volumes (LVs) that will act like physical partitions (e.g. , , ). If you did not understand that make sure you read the LVM Introduction section.

## Create physical volumes
Make the RAIDs accessible to LVM by converting them into physical volumes (PVs) using the following command. Repeat this action for each of the RAID arrays created above.

 # pvcreate /dev/md0

Confirm that LVM has added the PVs with:

 # pvdisplay

## Create the volume group
Next step is to create a volume group (VG) on the PVs.

Create a volume group (VG) with the first PV:

 # vgcreate VolGroupArray /dev/md0

Confirm that LVM has added the VG with:

 # vgdisplay

## Create logical volumes
In this example we will create separate , , ,  LVs. The LVs will be accessible as .

Create a / LV:

 # lvcreate -L 20G VolGroupArray -n lvroot

Create a /var LV:

 # lvcreate -L 15G VolGroupArray -n lvvar

Create a /home LV that takes up the remainder of space in the VG:

 # lvcreate -l 100%FREE VolGroupArray -n lvhome

Confirm that LVM has created the LVs with:

 # lvdisplay

## Update RAID configuration
Since the installer builds the initramfs using  in the target system, you should update that file with your RAID configuration. The original file can simply be deleted because it  contains comments on how to fill it correctly, and that is something mdadm can do automatically for you. So let us delete the original and have mdadm create you a new one with the current setup:

 # mdadm --examine --scan >> /etc/mdadm.conf

## Prepare hard drive
Follow the directions outlined the in #Installation section until you reach the Prepare Hard Drive section. Skip the first two steps and navigate to the Manually Configure block devices, filesystems and mountpoints page. Remember to only configure the PVs (e.g. ) and not the actual disks (e.g. ).

## Configure system
## mkinitcpio.conf
mkinitcpio can use a hook to assemble the arrays on boot. For more information see mkinitcpio Using RAID. Add the  and  hooks to the  array in  after .

## Conclusion
Once it is complete you can safely reboot your machine:

 # reboot

## Install the boot loader on the Alternate Boot Drives
Once you have successfully booted your new system for the first time, you will want to install the boot loader onto the other two disks (or on the other disk if you have only 2 HDDs) so that, in the event of disk failure, the system can be booted from any of the remaining drives (e.g. by switching the boot order in the BIOS).  The method depends on the boot loader system you are using:

## Syslinux
Log in to your new system as root and do:

 # /usr/sbin/syslinux-install_update -iam

Syslinux will deal with installing the boot loader to the MBR on each of the members of the RAID array:

 Detected RAID on /boot - installing Syslinux with --raid
 Syslinux install successful

 Attribute Legacy Bios Bootable Set - /dev/sda1
 Attribute Legacy Bios Bootable Set - /dev/sdb1
 Installed MBR (/usr/lib/syslinux/gptmbr.bin) to /dev/sda
 Installed MBR (/usr/lib/syslinux/gptmbr.bin) to /dev/sdb

## Archive your filesystem partition scheme
Now that you are done, it is worth taking a second to archive off the partition state of each of your drives. This guarantees that it will be trivially easy to replace/rebuild a disk in the event that one fails. See fdisk#Backup and restore partition table.

## Management
For further information on how to maintain your software RAID or LVM review the RAID and LVM articles.
