# Removing system encryption

Removing system encryption with dm-crypt and LUKS.

## Removing LUKS Encryption in-place
## Overview
Although not as safe as backing up your data and restoring it on to a reformatted device,
cryptsetup does allow the user to permanently remove the LUKS encryption from a device in-place. For example, if you have an ext4 filesystem living inside a LUKS-encrypted partition,
performing in-place decryption will remove the LUKS signature, and place the ext4 filesystem
directly on the partition, so that you can mount it directly. Unless something goes wrong,
the files in the filesystem will remain intact. The terms used by cryptsetup's documentation for this is "decryption."

See the  manual for the  option.

Support for non-destructive offline decryption of LUKS1 devices has been available starting with  version 1.5.0, which was released in 2012. LUKS1 decryption is only supported for offline mode decryption.

For LUKS2 devices, both offline and online (i.e. unmount not required) decryption are supported.

## Decrypting LUKS1 devices in-place
The decryption of a LUKS1 device is done in offline mode, i.e. it must not opened and mounted. If you want to decrypt the system drive, reboot into a USB live environment. Otherwise, use  followed by .

To start, identify the device_path using  or .

Next, the following command performs the decryption:

It will automatically identify the LUKS1 header version and not proceed for an opened device. The process might take a while, but give a progress meter. If no problems occur, the filesystem on the device can immediately be mounted directly.

## Decrypting LUKS2 devices in-place
Decryption can be done in either offline or online mode, using the  command. Since  version 2.5.0 (2022) LUKS2 supports decryption by migrating LUKS2 header in a separate file.

The  to which the LUKS2 header will be migrated must not exist in the initialization phase of the decryption.

To resume interrupted LUKS2 in-place decryption just issue following command:

 # cryptsetup reencrypt --decrypt --resume-only --header migrated_header_file device_path

If the decryption was successfully finished on active device (online decryption), the mapped device will be lazy deactivated so that linear mapping is automatically removed when no longer used. Later the original  can be used without device mapper mapping.

## Cleaning up system files
Device names and UUIDs may change due to decryption, and you will likely need to update relevant configuration files. The files most likely to need updating are  ,  and—if your recently decrypted device appeared on the kernel command line—your boot loader configuration, e.g. . If you edit the latter, remember to regenerate the grub configuration as described in GRUB.

## Removing LUKS via Backup-Format-Restore
## Prerequisites
*An encrypted root filesystem you wish to decrypt.
*Enough drive space to store a backup.
*An Arch Linux (or other) live CD/USB.
*A few hours.

## Boot into a live environment
Download and burn the latest Arch ISO to a CD or USB, reboot the system, and boot to cd.

## Activate partitions
## Note about different setups
An example setup is shown here:

{| class="wikitable"
|+ Disk
|
| colspan="2"
|
|-
| rowspan="3"
|
|
| rowspan="3"
|-
|
|
|-
|
|
|}

The grey partition is a frame of reference and can be ignored.
The yellow partition will be used as storage space and may be changed at will.
The green partitions will be modified. Bold text must match your system's setup.

In the example system:
myvg contains lvs called cryptroot and cryptswap. They are located at  and . Upon boot, LUKS is used along with a few crypttab entries to create  and .

Swap will not be unencrypted as part of this guide, as undoing the swap encryption does not require any complex backup or restoration.

The example system is not indicative of all systems. Different filesystems require different tools to effectively backup and restore their data. LVM can be ignored if not used.

## Once partitions are located
Load necessary modules. For device mapper/LVM:

 # modprobe dm-mod

For LUKS:

 # modprobe dm-crypt

Scan for physical, volume and logical volumes:

 # pvscan; vgscan; lvscan

Activate the LVM volume group:

 # lvchange -ay myvg/cryptroot

Open the encrypted filesystem with LUKS so that it can be read:

 # cryptsetup luksOpen /dev/myvg/cryptroot root

Enter password.

## Mounting backup space
Only if using NTFS to store the backup, install .

The next step is important for backup storage.

 # mount -t ntfs-3g -o rw /dev/sdXY /mount/point/

or use netcat to store the backup on a remote system.

## Backup data
Using xfs_copy:

 # xfs_copy -db /dev/mapper/root /mount/point/backup_root.img

Using dd:

 # dd if=/dev/mapper/root of=/mount/point/backup_root.img

## Undo encryption
This is the point of no return. Make sure that you are ready for this step. If you plan to undo this later, you will have to start almost from scratch.

 # cryptsetup luksClose root
 # lvm lvremove myvg/cryptroot

## Restore data
We have to create a new logical volume to house our root filesystem, then we restore our filesystem.

 # lvm lvcreate -l 100%FREE -n root myvg
 # xfs_copy -db /mount/point/backup_root.img /dev/myvg/root

The second drive name is changed now.

## Adjust configurations
You need to boot into your system and edit , , , and possibly .
