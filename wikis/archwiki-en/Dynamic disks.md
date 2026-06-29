# Dynamic disks

Dynamic disks, enabled by the Logical Disk Manager (LDM), is a technology for Microsoft Windows that is similar to LVM and mdadm.

## General consideration for Linux usage
In general it is not recommended to convert the disk drive to host your Linux into a dynamic disk. This is because:
* In a dynamic disk, an entire disk is put in a one, big partition. (More precisely, a GPT dynamic disk will have one big partition for data and the other, one small metadata partition. An MBR dynamic disk has a sole partition. See How Dynamic Disks and Volumes Work in microsoft.com.)
* To turn a disk to a dynamic disk, all existing partitions have to be recognized by Windows - Linux partitions (ext4, btrfs, lvm, you name it)  are out!

Probably the sole case you want to use dynamic disks is when you use RAID in Windows.

Dynamic disks cannot be used on removable disks, either.

## Usual course
LVM and mdadm are the preferred tools under Arch Linux.  However, if the system is being dual-booted with Windows, Windows will not be able to read these setups.  The usual course then is to attempt to use fakeraid using  or to use network storage.  However, network storage retrieval will be capped to 1Gb/s (119MiB/s) and getting RAID drivers loaded on an existing Windows installation can be daunting (if not impossible) if the Windows OS partition is installed on a drive that is on the very controller that you want to switch from AHCI to RAID.  Even if you have a spare AHCI controller card, your system may not have enough space to hold two Option ROMs.

## Terminology
Read "spanned volume" of a dynamic disk as a "logical volume" in Linux LVM, and "striped volume" as RAID0.

## Installing support for dynamic disks
Install the   package.  Once installed,  can be used to query and mount dynamic disks.

## Mandatory preparation
To create device mappers, simply do:

 # ldmtool create all

This populates  with volumes under LDM. Once this is done, they become accessible in a usual manner, say by:
 # mount -t ntfs /dev/mapper/LDM volume /mnt/mountpoint

## Other commands
To find all disk groups:

 # ldmtool scan

To find what volumes a disk group contains:

 # ldmtool show diskgroup diskgroup UUID

To create individual device mappers:

 # ldmtool create volume volume name

To create device mappers for all volumes in a disk group:

 # ldmtool create volume diskgroup UUID

## systemd
To get dynamic disks to behave like filesystems natively supported by the Linux kernel, enable .

Once this setup is complete, you can add entries to  that reference dynamic disk volumes and have those mounted like any other volume.
