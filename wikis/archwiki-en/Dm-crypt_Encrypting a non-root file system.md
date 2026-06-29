# Dm-crypt/Encrypting a non-root file system

The following are examples of encrypting a secondary, i.e. non-root, filesystem with dm-crypt.

## Overview
Encrypting a secondary filesystem usually protects only sensitive data while leaving the operating system and program files unencrypted. This is useful for encrypting an external medium, such as a USB drive, so that it can be moved to different computers securely. One might also choose to encrypt sets of data separately according to who has access to it.

Because dm-crypt is a block-level encryption layer, it only encrypts whole block devices, e.g. partitions and loop devices. Encrypting individual files requires a filesystem-level encryption layer, such as eCryptfs or EncFS. See Data-at-rest encryption for general information about securing private data.

## Partition
This example covers the encryption of the  partition, but it can be applied to any other comparable non-root partition containing user data.

It is assumed that the partition already exists. If it contained data before, you may consider securely erasing the partition (dm-crypt specific methods). Erasing a single partition instead of the entire disk may still leak some data.

Then setup the LUKS header with:
 # cryptsetup options luksFormat device

Replace  with the previously created partition. See dm-crypt/Device encryption#Encryption options for LUKS mode for details like the available .

To gain access to the encrypted partition, unlock it with the device mapper, using:

 # cryptsetup open device name

After unlocking the partition, it will be available at . Now create a file system of your choice with:

 # mkfs.fstype /dev/mapper/name

Mount the file system to , or if it should be accessible to only one user to , see #Manual mounting and unmounting.

## Manual mounting and unmounting
To mount the partition:

 # cryptsetup open device name
 # mount /dev/mapper/name /mnt/home

To unmount it:

 # umount /mnt/home
 # cryptsetup close name

## Automated unlocking and mounting
There are three different solutions for automating the process of unlocking the partition and mounting its filesystem.

## At boot time
Using the  configuration file, unlocking happens at boot time by systemd's automatic parsing. This is the recommended solution if you want to use one common partition for all users' home partitions or automatically mount another encrypted block device.

See dm-crypt/System configuration#crypttab for references and dm-crypt/System configuration#Mounting at boot time for an example setup.

## On user login
* Using pam_exec: recommended if you want to have a single user's home directory on a partition.
* Using pam_mount.

## File container
Cryptsetup operates with devices, therefore a loop device is required when using a file container. But cryptsetup can take care of the loop device management in the background (see Gentoo:Custom Initramfs#Encrypted keyfile), the user is not required to invoke losetup manually.

First, start by creating an encrypted file container with dd, using an appropriate random number generator:

 $ dd if=/dev/urandom of=bigsecret.img bs=100M count=1 iflag=fullblock

This will create the file  with a size of 100 mebibytes.

Make sure to not omit the  option, otherwise dd might return a partial read. See dd#Partial read: copied data is smaller than requested for details.

To avoid having to resize the container later on, make sure to make it larger than the total size of the files to be encrypted, plus internal file-system/metadata overhead, plus LUKS header. If you are going to use LUKS mode, its metadata header alone requires up to 16 mebibytes. Creating a file smaller than the LUKS2 header (16 MiB) will give a  error when trying to open the device.

The subsequent steps are the same as described in #Partition, but instead of using a  use .

In the background, cryptsetup will take care of finding a free loop device and attaching the file to it. After unmouting, the file container should be closed accordingly; cryptsetup will also detach the used loop device afterwards.

## Manual mounting and unmounting using losetup
To manually mount a file container with a LUKS and an ext4 filesystem inside, first find an unused loop device:

 # losetup --find

Then attach the file container to a loop device, e.g. :

 # losetup /dev/loop0 bigsecret.img

Now proceed with the normal cryptsetup operation:

 # cryptsetup open /dev/loop0 secret
 # mount -t ext4 /dev/mapper/secret /mnt/secret

Proceed in reverse order to unmount the container properly:

 # umount /mnt/secret
 # cryptsetup close secret

To detach the used loop device:

 # losetup --detach /dev/loop0
