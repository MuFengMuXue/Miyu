# System backup

A system backup is the process of backing up the operating system, files and system-specific useful/essential data. primarily ensures that not only the user data in a system is saved, but also the system's state or operational condition. This helps in restoring the system to the last-saved state along with all the selected backup data.[https://www.techopedia.com/definition/29387/system-backup

One common and generally effective method is to follow the 3-2-1 strategy:

* Maintain three copies of your data,
* Use two different types of storage media,
* Store one copy offsite.

## Methods
The Synchronization and backup programs page includes many options that are suitable for full system backups. Other common approaches are listed in the following subsections.

## Using Btrfs snapshots
See Btrfs#Snapshots, #Snapshots and /boot partition, and Snapper.

## Using LVM snapshots
See LVM#Snapshots, Create root filesystem snapshots with LVM, and #Snapshots and /boot partition.

## Using rsync
See rsync#As a backup utility.

## Using tar
See Full system backup with tar.

## Using SquashFS
See Full system backup with SquashFS.

## Bootable backup
Having a bootable backup can be useful in case the filesystem becomes corrupt or if an update breaks the system. The backup can also be used as a test bed for updates, with the testing repo enabled, etc. If you transferred the system to a different partition or drive and you want to boot it, the process is as simple as updating the backup's  and your boot loader's configuration file.

This section assumes that you backed up the system to another drive or partition, that your current boot loader is working fine, and that you want to boot from the backup as well.

## Update the fstab
Without rebooting, edit the backup's fstab by commenting out or removing any existing entries. Add one entry for the partition containing the backup, for example:

 UUID=XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX  /  ext4  defaults  0 1

Remember to use a persistent block device name and the proper filesystem type.

## Update the boot loader's configuration file
For Syslinux, all you need to do is duplicate the current entry, except pointing to a different drive or partition.

For GRUB, it is recommended that you automatically re-generate the main configuration file.  If you want to freshly install all GRUB files to somewhere other than , such as , use the  flag.

Also verify the new menu entry in . Make sure the UUID is matching the new partition, otherwise it could still boot the old system. Find the UUID of a partition with lsblk:

 $ lsblk -no NAME,UUID /dev/sdXY

where  is the desired partition (e.g. ). To list the UUIDs of partitions GRUB thinks it can boot, use grep:

 # grep UUID= /boot/grub/grub.cfg

## First boot
Reboot the computer and select the right entry in the boot loader. This will load the system for the first time. All peripherals should be detected and the empty folders in  will be populated.

Now you can re-edit  to add the previously removed partitions and mount points.

## Snapshots and /boot partition
If your file system supports snapshots (e.g., LVM or Btrfs), these will most likely exclude the  partition or ESP.

You can copy the boot partition automatically on a kernel update to your  partition with a pacman hook (make sure the hook file is owned by root):

## Automation
Backups that are only manually created are rarely up to date when they are needed. Therefore it is recommended to setup an automated process to ensure backup processes are executed regularly. The most common solutions are provided by systemd/Timers and Cron.

For a local system wide backup that requires read access to all files the following systemd timer and service may be useful as a template for automated backup processes.

To use a timer unit enable and start it like any other unit.

The following example is configured to run with minimal required permissions while preventing modifications from normal users for increased security.

Note that this example will block the shutdown process when it is initiated while the backup is running. This ensures that the backup is not interrupted, but can lead to a delay during shutdown/reboot if many new files need to be saved.

 sets the capability that allows bypassing file read permission checks in the file system; thus all files in the file system will be accessible without requiring root permissions.

For remote backups allow the use of network protocols:

 RestrictAddressFamilies=AF_UNIX AF_INET AF_INET6
