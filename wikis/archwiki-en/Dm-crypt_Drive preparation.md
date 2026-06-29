# Dm-crypt/Drive preparation

Before encrypting a drive, it is recommended to perform a secure erase by overwriting the entire device with random data. To prevent cryptographic attacks or unwanted file recovery, this data is ideally indistinguishable from data later written by dm-crypt. For a more comprehensive discussion see Data-at-rest encryption#Preparing the disk.

## Secure erasure of the drive
In deciding which method to use for secure erasure of a drive, remember that this needs only to be performed once for as long as the drive is continuously used as an encrypted device.

## Generic methods
For detailed instructions on how to erase and prepare a drive consult Securely wipe disk.

## dm-crypt specific methods
The following two methods are specific for dm-crypt and are mentioned because they are very fast and can be performed after a partition setup too.

The cryptsetup FAQ (item 2.19 "How can I wipe a device with crypto-grade randomness?") mentions a very simple procedure to use an existing dm-crypt-volume to wipe all free space accessible on the underlying block device with random data by acting as a simple pseudorandom number generator. It is also claimed to protect against disclosure of usage patterns. That is because encrypted data is practically indistinguishable from random.

## dm-crypt wipe on an empty device or partition
First, create a temporary encrypted container on the partition (using the form ) or complete device (using the form ) to be encrypted:

 # cryptsetup open --type plain --key-file /dev/urandom --sector-size 4096 /dev/block-device to_be_wiped

You can verify that it exists:

Wipe the container with zeros. A use of  is not required as the encryption cipher is used for randomness.

Finally, close the temporary container:

 # cryptsetup close to_be_wiped

When encrypting an entire system, the next step is #Partitioning. If just encrypting a partition, continue dm-crypt/Encrypting a non-root file system#Partition.

## dm-crypt wipe free space after installation
Users who did not have time for the wipe procedure before installation, can achieve a similar effect once the encrypted system is booted and the filesystems are mounted. However, consider if the concerned filesystem may have set up reserved space, e.g. for the root user, or another disk quota mechanism, that that may limit the wipe even when performed by the root user: some parts of the underlying block device might not get written to at all.

To execute the wipe, temporarily fill the remaining free space of the partition by writing to a file inside the encrypted container:

Sync the cache to disk and then delete the file to reclaim the free space.

 # sync
 # rm /file/in/container

The above process has to be repeated for every partition blockdevice created and filesystem in it. For example, setting-up LVM on LUKS, the process has to be performed for every logical volume.

## dm-crypt wipe free space after installation (via re-encryption)
Alternatively, for users who want to completely wipe free space without re-installation, this can be achieved by re-encrypting LUKS devices. It needs to be performed once per LUKS device. But please note that this process can be slower (e.g ~50MB/s on a desktop HDD).

## Wipe LUKS header
A partition using LUKS consists of two parts: the header and the encrypted data. The header contains keys and cryptographic parameters without which it is practically impossible to recover the data. If creating a new partition or decommissioning the drive it may be sufficient to remove that part instead of wiping the whole device. For caveats see the paragraph at the end of this subsection.

To erase all keys use the following command:

 # cryptsetup erase device

Make sure there is no active slots left by invoking:

 # cryptsetup luksDump device

Additionally the LUKS header itself may be removed to prevent  from detecting it in the future, by invoking wipefs after the keys are erased:

 # wipefs -a device

The encrypted data remains in place. As of 2020 there is no known practical way of decrypting the data, but that may change in the future. It is up to the user to weigh security and privacy against the time needed to perform a proper wiping of the entire drive.

On some storage media, in particular flash-based, it may be impossible to reliably overwrite data. The LUKS header with keys may remain stored in a location inaccessible to the operating system (e.g. a drive-cache). If that is a concern, ATA Secure Erase must be used. The operation is supposed to erase all blocks on the device, including those not visible to software. See cryptsetup FAQ 5.19 for details.

## Partitioning
This section only applies when encrypting an entire system. After the drive(s) has/have been securely overwritten, a proper partitioning scheme will have to be accurately chosen, taking into account the requirements of dm-crypt, and the effects that the various choices will have on the management of the resulting system.

Another important factor to take into account is how the swap area and system suspension will be handled, see dm-crypt/Swap encryption.

## Boot partition and EFI system partition
In almost every case there has to be a separate unencrypted partition that will contain the kernel and initramfs so that the boot loader can access them (see Arch boot process for a detailed explanation on each part of the boot process).

Since, by default, mkinitcpio places the kernel and initramfs images in , this separate unencrypted partition is typically mounted to . The requirements and limitations of the  partition are explained in Partitioning#/boot.

On UEFI systems it is possible to mount the EFI system partition to /boot. This avoids the need to create another separate unencrypted partition since the EFI system partition must be an unencrypted physical partition in the main partition table by definition. The EFI system partition has its own separate requirements and limitations that are listed in the EFI system partition article. When mounting the EFI system partition to , the requirements of a boot partition also apply to it.

If having an unencrypted partition raises security concerns, see dm-crypt/Specialties#Securing the unencrypted boot partition.

## Physical partitions
In the simplest case, the encrypted layers can be based directly on the physical partitions; see Partitioning for the methods to create them. Just like in an unencrypted system, a root partition is sufficient, besides another for  as noted above. This method allows deciding which partitions to encrypt and which to leave unencrypted, and works the same regardless of the number of disks involved. It will also be possible to add or remove partitions in the future, but resizing a partition will be limited by the size of the disk that is hosting it. Finally note that separate passphrases or keys are required to open each encrypted partition, even though this can be automated during boot using the  file, see Dm-crypt/System configuration#crypttab.

## Stacked block devices
If more flexibility is needed, though, dm-crypt can coexist with other stacked block devices like LVM and RAID. The encrypted containers can either reside below or on top of other stacked block devices:

* If the LVM/RAID devices are created on top of the encrypted layer, it will be possible to add, remove and resize the file systems of the same encrypted partition liberally, and only one key or passphrase will be required for all of them. Since the encrypted layer resides on a physical partition, though, it will not be possible to exploit the ability of LVM and RAID to span multiple disks.
* If the encrypted layer is created on top of LVM/RAID devices, it will still be possible to reorganize the file systems in the future, but with added complexity, since the encryption layers will have to be adjusted accordingly. Moreover, separate passphrases or keys will be required to open each encrypted device. This, however, is the only choice for systems that need encrypted file systems to span multiple disks.

## Btrfs subvolumes
Btrfs's built-in subvolumes feature can be used with dm-crypt, fully replacing the need for LVM if no other file systems are required.

## Encrypted boot partition (GRUB)
An exception for needing a unencrypted partition is when using GRUB on BIOS/MBR. In this case, GRUB is stored (unencrypted) in the MBR bootstrap code area and the post-MBR gap and all other partitions can be encrypted.

See dm-crypt/Encrypting an entire system#Encrypted boot partition (GRUB).
