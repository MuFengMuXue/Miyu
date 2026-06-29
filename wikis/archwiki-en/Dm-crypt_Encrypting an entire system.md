# Dm-crypt/Encrypting an entire system

The following are examples of common scenarios of full system encryption with dm-crypt. They explain all the adaptations that need to be done to the normal installation procedure. All the necessary tools are on the installation image.

If you want to encrypt an existing unencrypted file system, see dm-crypt/Device encryption#Encrypt an existing unencrypted file system.

## Overview
Securing a root file system is where dm-crypt excels, feature and performance-wise. Unlike selectively encrypting non-root file systems, an encrypted root file system can conceal information such as which programs are installed, the usernames of all user accounts, and common data-leakage vectors such as locate and . Furthermore, an encrypted root file system makes tampering with the system far more difficult, as everything except the boot loader and (usually) the kernel is encrypted.

All scenarios illustrated in the following share these advantages, other pros and cons differentiating them are summarized below:

{| class="wikitable"
! Scenarios
! Advantages
! Disadvantages
|----------------------------------------------------------
| #LUKS on a partition
shows a basic and straightforward set-up for a fully LUKS encrypted root.
|
* Simple partitioning and setup
* On a GPT partitioned disk, systemd can auto-mount the root partition.
|
* Inflexible; disk-space to be encrypted has to be pre-allocated
|----------------------------------------------------------
| #LUKS on a partition with TPM2 and Secure Boot
Similar to the example above, with Secure Boot and TPM2 providing additional layers of security.
|
Same advantages as above, and
* Secure Boot allows protection against Evil maid attacks
* TPM2 prevents the system from being unlocked if Secure Boot is disabled or modified
|
* Same disadvantages as above.
|----------------------------------------------------------
| #LVM on LUKS
achieves partitioning flexibility by using LVM inside a single LUKS encrypted partition.
|
* Simple partitioning with knowledge of LVM
* Only one key required to unlock all volumes (e.g. easy resume-from-disk setup)
* Volume layout not visible when locked
* Easiest method to allow suspension to disk
|
* LVM adds an additional mapping layer and hook
* Less useful, if a singular volume should receive a separate key
* If you have several LVM physical volumes (PVs) in a volume group that you want to use inside LUKS, then each physical volume must be encrypted separately using LUKS. In order to use them, all containers must be unlocked individually before the volume group is activated during system boot.
|----------------------------------------------------------
| #LUKS on LVM
uses dm-crypt only after the LVM is setup.
|
* LVM can be used to have encrypted volumes span multiple disks
* Easy mix of un-/encrypted volume groups
|
* Complex; changing volumes requires changing encryption mappers too
* Volumes require individual keys
* LVM layout is visible when locked
* Slower boot time; each encrypted LV must be unlocked seperately
|----------------------------------------------------------
| #LUKS on software RAID
uses dm-crypt only after RAID is setup.
|
* Analogous to LUKS on LVM
|
* Analogous to LUKS on LVM and Encrypted boot partition (GRUB)
|----------------------------------------------------------
| #Plain dm-crypt
uses dm-crypt plain mode, i.e. without a LUKS header and its options for multiple keys.

This scenario also employs USB devices for  and key storage, which may be applied to the other scenarios.
|
* Data resilience for cases where a LUKS header may be damaged
* Allows deniable encryption
* Helps addressing problems with SSDs
|
* High care to all encryption parameters is required
* Single encryption key and no option to change it
* Very complicated setup for a regular used system
|----------------------------------------------------------
| #Encrypted boot partition (GRUB)
shows how to encrypt the boot partition using the GRUB boot loader.

This scenario also employs an EFI system partition, which may be applied to the other scenarios.
|
* Same advantages as the scenario the installation is based on (LVM on LUKS for this particular example)
* Less data is left unencrypted, i.e. the boot loader and the EFI system partition, if present
|
* Same disadvantages as the scenario the installation is based on (LVM on LUKS for this particular example)
* More complicated configuration
* Not supported by other boot loaders
* GRUB takes a long time to unlock LUKS, thus slowing down boot
|----------------------------------------------------------
| #Root on ZFS
|
* In the case of a encrypted  all datasets are contained inside the same cryptographic environment making it easy to dual-boot and share data across installs.
* Backups can be made to a destination with an unencrypted zfs setup. Snapshots will be encrypted natively on the destination.
|
* ZFS will not encrypt metadata related to the pool structure, including dataset and snapshot names, dataset hierarchy, properties, file size, file holes, and deduplication tables (though the deduplicated data itself is encrypted).
* Pool creation requires the user to have a more in-depth knowledge of disks geometry setting even block size () for best performance.
* ZFS has some caveats with its own implementation of  and some encryption algorithms may not perform well.
* Swap on a  or file inside a dataset is a old and well-known issue with no workaround other than having your swap in another partition or lv and suspend to disk disabled (see below).
|}

While all above scenarios provide much greater protection from outside threats than encrypted secondary file systems, they also share a common disadvantage: any user in possession of the encryption key is able to decrypt the entire drive, and therefore can access other users' data. If that is of concern, it is possible to use a combination of block device and stacked file system encryption and reap the advantages of both. See Data-at-rest encryption to plan ahead.

See dm-crypt/Drive preparation#Partitioning for a general overview of the partitioning strategies used in the scenarios.

Another area to consider is whether to set up an encrypted swap partition and what kind. See dm-crypt/Swap encryption for alternatives.

If you anticipate to protect the system's data not only against physical theft, but also have a requirement of precautions against logical tampering, see dm-crypt/Specialties#Securing the unencrypted boot partition for further possibilities after following one of the scenarios.

For solid state drives you might want to consider enabling TRIM support, but be warned, there are potential security implications. See dm-crypt/Specialties#Discard/TRIM support for solid state drives (SSD) for more information.

## LUKS on a partition
This example covers a full system encryption with dm-crypt + LUKS in a simple partition layout:

The first steps can be performed directly after booting the Arch Linux install image.

## Preparing the disk
Prior to creating any partitions, you should inform yourself about the importance and methods to securely erase the disk, described in dm-crypt/Drive preparation.

Then create the needed partitions, at least one for  (e.g. ) and  (). See Partitioning.

## Preparing non-boot partitions
This and the next section replace the instructions of Installation guide#Format the partitions.

The following commands create and mount the encrypted root partition. They correspond to the procedure described in detail in dm-crypt/Device encryption#Encrypting devices with LUKS mode. If you want to use particular non-default encryption options (e.g. cipher, key length, sector size), see the encryption options before executing the first command.

 # cryptsetup -v luksFormat /dev/sda2
 # cryptsetup open /dev/sda2 root

Create a file system on unlocked LUKS device. For example, to create an Ext4 file system, run:

 # mkfs.ext4 /dev/mapper/root

Mount the root volume to :

 # mount /dev/mapper/root /mnt

Check the mapping works as intended:

 # umount /mnt
 # cryptsetup close root
 # cryptsetup open /dev/sda2 root
 # mount /dev/mapper/root /mnt

If you created separate partitions (e.g. ), these steps have to be adapted and repeated for all of them, except for . See dm-crypt/Encrypting a non-root file system#Automated unlocking and mounting on how to handle additional partitions at boot.

Note that each block device requires its own passphrase. This may be inconvenient, because it results in a separate passphrase to be input during boot. An alternative is to use a keyfile stored in the root partition to unlock the separate partition via . See dm-crypt/Device encryption#Using LUKS to format partitions with a keyfile for instructions.

## Preparing the boot partition
What you do have to setup is a non-encrypted  partition, which is needed for an encrypted root. For an EFI system partition on UEFI systems, execute the following command to format the newly created partition:

 # mkfs.fat -F32 /dev/sda1

or for an ordinary boot partition on BIOS systems:

 # mkfs.ext4 /dev/sda1

Afterwards create the directory for the mountpoint and mount the partition:

 # mount --mkdir /dev/sda1 /mnt/boot

## Mounting the devices
At the step Installation guide#Mount the file systems, you should mount the  devices (the contents of LUKS), not the actual partitions. Of course, the partition for , which is not encrypted, should still be mounted directly. During installation, it should be mounted to  (assuming the device for the root file system is mounted to  during installation).

## Configuring mkinitcpio
Before following Installation guide#Initramfs you must do the following to your new system:

If using the default systemd-based initramfs, add the  and  hooks to mkinitcpio.conf. If you use a non-US console keymap or a non-default console font, additionally add the  hook.

 HOOKS=(base systemd autodetect microcode modconf kms keyboard sd-vconsole block sd-encrypt filesystems fsck)

If using a busybox-based initramfs, add the  and  hooks. If you use a non-US console keymap or a non-default console font, additionally add the  and  hooks, respectively.

 HOOKS=(base udev autodetect microcode modconf kms keyboard keymap consolefont block encrypt filesystems fsck)

Regenerate the initramfs after saving the changes. See dm-crypt/System configuration#mkinitcpio for details and other hooks that you may need.

## Configuring the boot loader
In order to unlock the encrypted root partition at boot, the following kernel parameters need to be set by the boot loader:

 rd.luks.name=device-UUID=root root=/dev/mapper/root

If using the  hook, the following need to be set instead:

 cryptdevice=UUID=device-UUID:root root=/dev/mapper/root

The  refers to the UUID of the LUKS superblock. See Persistent block device naming for details.

Also see dm-crypt/System configuration#Kernel parameters for more details.

## LUKS on a partition with TPM2 and Secure Boot
This example is similar to #LUKS on a partition, but integrates the use of Secure Boot and a Trusted Platform Module (TPM), enhancing the overall security of the boot process.

In this configuration, only the EFI system partition remains unencrypted, housing a unified kernel image and systemd-boot—both signed for use with Secure Boot. If Secure Boot is disabled or its key databases are tampered with, the TPM will not release the key to unlock the encrypted partition. This approach is akin to BitLocker on Windows or FileVault on macOS. A recovery-key will also be created to make sure the data remains accessible in case of a problem with the TPM unlocking mechanism (unsigned boot loader or kernel update, firmware update, etc.). Optionally, a TPM pin can be set to be required during boot time to prevent fully automatic unlocking.

Make sure to thoroughly read the discussion and warnings in Trusted Platform Module#LUKS encryption.

In this example, partitions are created respecting systemd#GPT partition automounting, there is no need for an fstab or crypttab file.

Follow the Installation guide up to step Installation guide#Partition the disks.

## Preparing the disk
Prior to creating any partitions, you should inform yourself about the importance and methods to securely erase the disk, described in dm-crypt/Drive preparation.

Partition the drive with the GUID Partition Table (GPT).

Create an EFI system partition (e.g., ) with an appropriate size. This will be mounted at .

In the remaining space, create a root partition (e.g., ) that will be encrypted and mounted at . Set the partition type GUID for the root partition using type "Linux root (x86-64)" in fdisk or type code  in gdisk.

Check the output of  to make sure partition types are properly set.

## Preparing the root partition
The following commands create and mount the encrypted root partition. They correspond to the procedure described in detail in dm-crypt/Device encryption#Encrypting devices with LUKS mode.

If you want to use particular non-default encryption options (e.g. cipher, key length), or if you don't want to use TPM based decryption, see the encryption options before executing the first command.

Create the LUKS volume and mount it:

 # cryptsetup luksFormat /dev/sda2
 # cryptsetup open /dev/sda2 root

Create a file system on unlocked LUKS device. For example, to create an Ext4 file system, run:

 # mkfs.ext4 /dev/mapper/root

Mount the root volume to :

 # mount /dev/mapper/root /mnt

## Preparing the EFI system partition
Format the newly created EFI system partition as instructed in EFI system partition#Format the partition and mount it afterwards.

 # mount --mkdir /dev/sda1 /mnt/boot

Continue the installation process until Installation guide#Initramfs. You can skip Installation guide#Fstab.

## Configuring mkinitcpio
To build a working systemd based initramfs, modify the  line in mkinitcpio.conf as follows:

 HOOKS=(base systemd autodetect microcode modconf kms keyboard sd-vconsole block sd-encrypt filesystems fsck)

Next, see Unified kernel image#mkinitcpio to configure mkinitcpio for Unified kernel images.

Do not regenerate the initramfs yet, as the  directory needs to be created by the boot loader installer first.

## Installing the boot loader
You can configure your system to directly boot the UEFI image without any boot loader, see Unified kernel image#Directly from UEFI.

If a boot loader is desired, continue installing systemd-boot with

 # bootctl install

The Unified kernel image generated by mkinitcpio will be automatically recognized and does not need an entry in .

See systemd-boot#Updating the UEFI boot manager and systemd-boot#Loader configuration for further configuration.

## Finalizing the installation
First, Regenerate the initramfs, and make sure the image generation is successful.

Make sure you did not forget to set a root password, reboot to finish the installation.

## Secure Boot
You can now sign the boot loader executables and the EFI binary, in order to enable Secure Boot. For a quick and easy way, see Unified Extensible Firmware Interface/Secure Boot#Assisted process with sbctl.

## Enrolling the TPM
After signing the boot loader executables and enabling Secure Boot, you can now enroll the TPM in order to use it to unlock the LUKS volume. The following commands will remove the empty passphrase created during the LUKS format process, create a key bound to the TPM PCR 7 (Secure Boot state and enrolled certificates) and create a recovery key to be used in case of any problems. The TPM will automatically release the key as long as the boot chain is not tampered with. See systemd-cryptenroll#Trusted Platform Module and .

 # systemd-cryptenroll /dev/sda2 --recovery-key
 # systemd-cryptenroll /dev/sda2 --wipe-slot=empty --tpm2-device=auto --tpm2-pcrs=7+15:sha256=0000000000000000000000000000000000000000000000000000000000000000

## LVM on LUKS
The straightforward method is to set up LVM on top of the encrypted partition instead of the other way round. Technically the LVM is setup inside one big encrypted block device. Hence, the LVM is not visible until the block device is unlocked and the underlying volume structure is scanned and mounted during boot.

The disk layout in this example is:

## Preparing the disk
Prior to creating any partitions, you should inform yourself about the importance and methods to securely erase the disk, described in dm-crypt/Drive preparation.

Create a partition to be mounted at  with a size of 1 GiB or more.

Create a partition which will later contain the encrypted container.

Create the LUKS encrypted container at the designated partition. Enter the chosen password twice.

 # cryptsetup luksFormat /dev/sda1

For more information about the available cryptsetup options see the LUKS encryption options prior to above command.

Open the container:

 # cryptsetup open /dev/sda1 cryptlvm

The decrypted container is now available at .

## Preparing the logical volumes
Create a physical volume on top of the opened LUKS container:

 # pvcreate /dev/mapper/cryptlvm

Create a volume group (in this example named , but it can be whatever you want) and add the previously created physical volume to it:

 # vgcreate MyVolGroup /dev/mapper/cryptlvm

Create all your logical volumes on the volume group:

 # lvcreate -L 4G -n swap MyVolGroup
 # lvcreate -L 32G -n root MyVolGroup
 # lvcreate -l 100%FREE -n home MyVolGroup

Format your file systems on each logical volume. For example, using Ext4 for the root and home volumes:

 # mkfs.ext4 /dev/MyVolGroup/root
 # mkfs.ext4 /dev/MyVolGroup/home
 # mkswap /dev/MyVolGroup/swap

Mount your file systems:

 # mount /dev/MyVolGroup/root /mnt
 # mount --mkdir /dev/MyVolGroup/home /mnt/home
 # swapon /dev/MyVolGroup/swap

## Preparing the boot partition
The boot loader loads the kernel, initramfs, and its own configuration files from the  directory. Any file system on a disk that can be read by the boot loader is eligible.

Create a file system on the partition intended for . For an EFI system partition on UEFI systems, execute the following command to format the newly created partition:

 # mkfs.fat -F32 /dev/sdb1

or for an ordinary boot partition on BIOS systems:

 # mkfs.ext4 /dev/sdb1

Mount the partition to :

 # mount --mkdir /dev/sdb1 /mnt/boot

At this point resume the common Installation guide#Installation steps. Return to this page to customize the Initramfs and Boot loader steps.

## Configuring mkinitcpio
Make sure the  package is installed.

If using the default systemd-based initramfs, add the ,  and  hooks to mkinitcpio.conf. If you use a non-US console keymap or a non-default console font, additionally add the  hook.

 HOOKS=(base systemd autodetect microcode modconf kms keyboard sd-vconsole block sd-encrypt lvm2 filesystems fsck)

If using a busybox-based initramfs, instead add the ,  and  hooks. If you use a non-US console keymap or a non-default console font, additionally add the  and  hooks, respectively.

 HOOKS=(base udev autodetect microcode modconf kms keyboard keymap consolefont block encrypt lvm2 filesystems fsck)

Regenerate the initramfs after saving the changes. See dm-crypt/System configuration#mkinitcpio for details and other hooks that you may need.

## Configuring the boot loader
In order to unlock the encrypted root partition at boot, the following kernel parameters need to be set by the boot loader:

 rd.luks.name=device-UUID=cryptlvm root=/dev/MyVolGroup/root

If using the  hook, the following needs to be set instead:

 cryptdevice=UUID=device-UUID:cryptlvm root=/dev/MyVolGroup/root

The  refers to the UUID of the LUKS superblock, in this example it is the UUID of  e.g. . See Persistent block device naming for details.

If using dracut, these parameters are known to work:

 rd.luks.uuid=device-UUID root=/dev/MyVolGroup/root

you may need a more extensive list of parameters, try:

 rd.luks.uuid=luks-deviceUUID rd.lvm.lv=MyVolGroup/root  rd.lvm.lv=MyVolGroup/swap  root=/dev/mapper/MyVolGroup-root rootfstype=ext4 rootflags=rw,relatime

See dm-crypt/System configuration#Kernel parameters for details.

## LUKS on LVM
To use encryption on top of LVM, the LVM volumes are set up first and then used as the base for the encrypted partitions. This way, a mixture of encrypted and non-encrypted volumes/partitions is possible as well.

The following short example creates a LUKS on LVM setup and mixes in the use of a key-file for the /home partition and a temporary encrypted volume for swap. This is considered desirable from a security perspective, because no potentially sensitive temporary data survives the reboot, when the encryption is re-initialised. If you are experienced with LVM, you will be able to ignore/replace LVM and other specifics according to your plan.

If you want to span a logical volume over multiple disks that have already been set up, or expand the logical volume for  (or any other volume), a procedure to do so is described in dm-crypt/Specialties#Expanding LVM on multiple disks. It is important to note that the LUKS encrypted container has to be resized as well.

## Preparing the disk
Partitioning scheme:

Randomise  according to dm-crypt/Drive preparation#dm-crypt wipe on an empty device or partition.

## Preparing the logical volumes
 # pvcreate /dev/sda2
 # vgcreate MyVolGroup /dev/sda2
 # lvcreate -L 4G -n cryptswap MyVolGroup
 # lvcreate -L 32G -n cryptroot MyVolGroup
 # lvcreate -l 100%FREE -n crypthome MyVolGroup

 # cryptsetup luksFormat /dev/MyVolGroup/cryptroot
 # cryptsetup open /dev/MyVolGroup/cryptroot root

Create a file system on unlocked LUKS device and mount it. For example, to create an Ext4 file system, run:

 # mkfs.ext4 /dev/mapper/root
 # mount /dev/mapper/root /mnt

More information about the encryption options can be found in dm-crypt/Device encryption#Encryption options for LUKS mode.
Note that  will be encrypted in #Encrypting logical volume /home.

## Preparing the boot partition
Create a file system on the partition intended for . For an EFI system partition on UEFI systems, execute the following command to format the newly created partition:

 # mkfs.fat -F32 /dev/sda1

or for an ordinary boot partition on BIOS systems:

 # mkfs.ext4 /dev/sda1

Afterwards create the directory for the mountpoint and mount the partition:

 # mount --mkdir /dev/sda1 /mnt/boot

## Configuring mkinitcpio
Make sure the  package is installed.

If using the default systemd-based initramfs, add the ,  and  hooks to mkinitcpio.conf. If you use a non-US console keymap or a non-default console font, additionally add the  hook.

 HOOKS=(base systemd autodetect microcode modconf kms keyboard sd-vconsole block sd-encrypt lvm2 filesystems fsck)

If using a busybox-based initramfs, instead add the ,  and  hooks. If you use a non-US console keymap or a non-default console font, additionally add the  and  hooks, respectively.

 HOOKS=(base udev autodetect microcode modconf kms keyboard keymap consolefont block encrypt lvm2 filesystems fsck)

Regenerate the initramfs after saving the changes. See dm-crypt/System configuration#mkinitcpio for details and other hooks that you may need.

## Configuring the boot loader
In order to unlock the encrypted root partition at boot, the following kernel parameters need to be set by the boot loader:

 rd.luks.name=device-UUID=root root=/dev/mapper/root

If using the  hook, the following need to be set instead:

 cryptdevice=UUID=device-UUID:root root=/dev/mapper/root

The  refers to the UUID of the LUKS superblock, in this example it is the UUID of  e.g. . See Persistent block device naming for details.

See dm-crypt/System configuration#Kernel parameters for details.

## Configuring fstab and crypttab
Both crypttab and fstab entries are required to both unlock the device and mount the file systems, respectively. The following lines will re-encrypt the swap volume on each reboot:

## Encrypting logical volume /home
Since this scenario uses LVM as the primary and dm-crypt as secondary mapper, each encrypted logical volume requires its own encryption. Yet, unlike the temporary file systems configured with volatile encryption above, the logical volume for  should of course be persistent. The following assumes you have rebooted into the installed system, otherwise you have to adjust paths.
To save on entering a second passphrase at boot, a keyfile is created:

 # dd bs=512 count=4 if=/dev/random iflag=fullblock | install -m 0600 /dev/stdin /etc/cryptsetup-keys.d/home.key

The logical volume is encrypted with it:

 # cryptsetup luksFormat -v /dev/MyVolGroup/crypthome /etc/cryptsetup-keys.d/home.key
 # cryptsetup -d /etc/cryptsetup-keys.d/home.key open /dev/MyVolGroup/crypthome home

Create a file system on unlocked LUKS device and mount it. For example, to create an Ext4 file system, run:

 # mkfs.ext4 /dev/mapper/home
 # mount /dev/mapper/home /home

The encrypted mount is configured in both crypttab and fstab:

## LUKS on software RAID
This example is based on a real-world setup for a workstation class laptop equipped with two SSDs of equal size, and an additional HDD for bulk storage. The end result is LUKS based full disk encryption (including ) for all drives, with the SSDs in a RAID0 array, and keyfiles used to unlock all encryption after GRUB is given a correct passphrase at boot.

This setup utilizes a very simplistic partitioning scheme, with all the available RAID storage being mounted at  (no separate  partition), and the decrypted HDD being mounted at .

Please note that regular backups are very important in this setup. If either of the SSDs fail, the data contained in the RAID array will be practically impossible to recover. You may wish to select a different RAID level if fault tolerance is important to you.

The encryption is not deniable in this setup.

For the sake of the instructions below, the following block devices are used:

 /dev/sda = first SSD
 /dev/sdb = second SSD
 /dev/sdc = HDD

Be sure to substitute them with the appropriate device designations for your setup, as they may be different.

## Preparing the disks
Prior to creating any partitions, you should inform yourself about the importance and methods to securely erase the disk, described in dm-crypt/Drive preparation.

For BIOS systems with GPT, create a BIOS boot partition with size of 1 MiB for GRUB to store the second stage of BIOS boot loader. Do not mount the partition.

For UEFI systems create an EFI system partition with an appropriate size, it will later be mounted at .

In the remaining space on the drive create a partition ( in this example) for "Linux RAID". Choose partition type ID  for MBR or partition type GUID  for GPT.

Once partitions have been created on , the following commands can be used to clone them to .

 # sfdisk -d /dev/sda > sda.dump
 # sfdisk /dev/sdb > /etc/mdadm.conf

Edit mkinitcpio.conf to include your keyfile and add the proper hooks:

 FILES=(/crypto_keyfile.bin)
 HOOKS=(base udev autodetect microcode modconf kms keyboard keymap consolefont block mdadm_udev encrypt filesystems fsck)

See dm-crypt/System configuration#mkinitcpio for details.

## Plain dm-crypt
Contrary to LUKS, dm-crypt plain mode does not require a header on the encrypted device: this scenario exploits this feature to set up a system on an unpartitioned, encrypted disk that will be indistinguishable from a disk filled with random data, which could allow deniable encryption. See also wikipedia:Disk encryption#Full disk encryption.

Note that if full disk encryption is not required, the methods using LUKS described in the sections above are better options for both system encryption and encrypted partitions. LUKS features like key management with multiple passphrases/key-files, master key backups or re-encrypting a device in-place are unavailable with plain mode.

Plain dm-crypt encryption can be more resilient to damage than LUKS, because it does not rely on an encryption master-key which can be a single-point of failure if damaged or forcefully destroyed. However, using plain mode also requires more manual configuration of encryption options to achieve the same cryptographic strength. See also Data-at-rest encryption#Cryptographic metadata. Using plain mode could also be considered if concerned with the problems explained in dm-crypt/Specialties#Discard/TRIM support for solid state drives (SSD).

The scenario uses two USB sticks:

* one for the boot device, which also allows storing the options required to open/unlock the plain encrypted device in the boot loader configuration, since typing them on each boot would be error prone;
* another for the encryption key file, assuming it stored as raw bits so that to the eyes of an unaware attacker who might get the usbkey the encryption key will appear as random data instead of being visible as a normal file. See also Wikipedia:Security through obscurity, follow dm-crypt/Device encryption#Keyfiles to prepare the keyfile.

The disk layout is:

## Preparing the disk
It is vital that the mapped device is filled with random data. In particular this applies to the scenario use case we apply here.

See dm-crypt/Drive preparation and dm-crypt/Drive preparation#dm-crypt specific methods

## Preparing the non-boot partitions
See dm-crypt/Device encryption#Encryption options for plain mode for details.

Using the device , with the aes-xts cipher with a 512 bit key size and using a keyfile we have the following options for this scenario:

 # cryptsetup open --type plain --cipher=aes-xts-plain64 --offset=0 --key-file=/dev/sdc --key-size=512 --sector-size 4096 /dev/sda cryptlvm

Unlike encrypting with LUKS, the above command must be executed in full whenever the mapping needs to be re-established, so it is important to remember the cipher, and key file details.

We can now check a mapping entry has been made for :

 # fdisk -l

Next, we setup LVM logical volumes on the mapped device. See Install Arch Linux on LVM for further details:

 # pvcreate /dev/mapper/cryptlvm
 # vgcreate MyVolGroup /dev/mapper/cryptlvm
 # lvcreate -L 32G MyVolGroup -n root
 # lvcreate -L 4G MyVolGroup -n swap
 # lvcreate -l 100%FREE MyVolGroup -n home

We format and mount them and activate swap. See File systems#Create a file system for further details:

 # mkfs.ext4 /dev/MyVolGroup/root
 # mkfs.ext4 /dev/MyVolGroup/home
 # mount /dev/MyVolGroup/root /mnt
 # mount --mkdir /dev/MyVolGroup/home /mnt/home
 # mkswap /dev/MyVolGroup/swap
 # swapon /dev/MyVolGroup/swap

## Preparing the boot partition
The  partition can be a typical FAT32 formatted partition on a USB stick, if required. But if manual partitioning is needed, then a small 1 GiB partition is all that is required. Create the partition using a partitioning tool of your choice.

Create a file system on the newly created partition intended for :

 # mkfs.fat -F32 /dev/sdb1
 # mount --mkdir /dev/sdb1 /mnt/boot

## Configuring mkinitcpio
Make sure the  package is installed.

If using a busybox-based initramfs, add the ,  and  hooks. If you use a non-US console keymap or a non-default console font, additionally add the  and  hooks, respectively.

 HOOKS=(base udev autodetect microcode modconf kms keyboard keymap consolefont block encrypt lvm2 filesystems fsck)

Regenerate the initramfs after saving the changes. See dm-crypt/System configuration#mkinitcpio for details and other hooks that you may need.

## Configuring the boot loader
In order to boot the encrypted root partition, the following kernel parameters need to be set by the boot loader (note that 64 is the number of bytes in 512 bits):

 cryptdevice=/dev/disk/by-id/disk-ID-of-sda:cryptlvm:sector-size=4096 cryptkey=/dev/disk/by-id/disk-ID-of-sdc:0:64 crypto=:aes-xts-plain64:512:0:

The  refers to the id of the referenced disk. See Persistent block device naming for details.

See dm-crypt/System configuration#Kernel parameters for details and other parameters that you may need.

## Post-installation
You may wish to remove the USB sticks after booting. Since the  partition is not usually needed, the  option can be added to the relevant line in :

However, when an update to anything used in the initramfs, or a kernel, or the boot loader is required; the  partition must be present and mounted. As the entry in  already exists, it can be mounted simply with:

 # mount /boot

## Encrypted boot partition (GRUB)
This setup utilizes the same partition layout and configuration as the previous #LVM on LUKS section, with the difference that the GRUB boot loader is used since it is capable of booting from an LVM logical volume and a LUKS-encrypted . See also GRUB#Encrypted /boot.

The disk layout in this example is:

## Preparing the disk
Prior to creating any partitions, you should inform yourself about the importance and methods to securely erase the disk, described in dm-crypt/Drive preparation.

For UEFI systems create an EFI system partition with an appropriate size, it will later be mounted at .

For BIOS/GPT setups create a BIOS boot partition with size of 1 MiB for GRUB to store the second stage of BIOS boot loader. Do not mount the partition. For BIOS/MBR setups this is not necessary.

Create a partition of type , which will later contain the encrypted container for the LVM.

Create the LUKS encrypted container:

 # cryptsetup luksFormat --pbkdf pbkdf2 /dev/sda3

For more information about the available cryptsetup options see the LUKS encryption options prior to above command.

Your partition layout should look similar to this:

Open the container:

 # cryptsetup open /dev/sda3 cryptlvm

The decrypted container is now available at .

## Preparing the logical volumes
The LVM logical volumes of this example follow the exact layout as the #LVM on LUKS scenario. Therefore, please follow #Preparing the logical volumes above and adjust as required.

For UEFI systems, create a mountpoint for the EFI system partition at  for compatibility with  and mount it:

 # mount --mkdir /dev/sda2 /mnt/efi

At this point, you should have the following partitions and logical volumes inside of :

Now at this point resume the common Installation guide#Installation steps. Return to this page to customize the Initramfs and Boot loader steps.

## Configuring mkinitcpio
Make sure the  package is installed.

If using the default systemd-based initramfs, add the ,  and  hooks to mkinitcpio.conf. If you use a non-US console keymap or a non-default console font, additionally add the  hook.

 HOOKS=(base systemd autodetect microcode modconf kms keyboard sd-vconsole block sd-encrypt lvm2 filesystems fsck)

If using a busybox-based initramfs, instead add the ,  and  hooks. If you use a non-US console keymap or a non-default console font, additionally add the  and  hooks, respectively.

 HOOKS=(base udev autodetect microcode modconf kms keyboard keymap consolefont block encrypt lvm2 filesystems fsck)

Regenerate the initramfs after saving the changes. See dm-crypt/System configuration#mkinitcpio for details and other hooks that you may need.

## Configuring GRUB
Configure GRUB to allow booting from  on a LUKS encrypted partition:

Set the kernel parameters, so that the initramfs can unlock the encrypted root partition. Using the  hook:

If using the  hook, the following need to be set instead:

See dm-crypt/System configuration#Kernel parameters and GRUB#Encrypted /boot for details. The  refers to the UUID of the LUKS superblock, in this example it is the UUID of  (the partition which holds the lvm containing the root file system) e.g. . See Persistent block device naming for details.

install GRUB to the mounted ESP for UEFI booting:

 # grub-install --target=x86_64-efi --efi-directory=/efi --bootloader-id=GRUB --recheck

install GRUB to the disk for BIOS booting:

 # grub-install --target=i386-pc --recheck /dev/sda

Generate GRUB's configuration file:

 # grub-mkconfig -o /boot/grub/grub.cfg

If all commands finished without errors, GRUB should prompt for the passphrase to unlock the  partition after the next reboot.

## Avoiding having to enter the passphrase twice
While GRUB asks for a passphrase to unlock the LUKS encrypted partition after above instructions, the partition unlock is not passed on to the initramfs. Hence, you have to enter the passphrase twice at boot: once for GRUB and once for the initramfs.

This section deals with extra configuration to let the system boot by only entering the passphrase once, in GRUB. This is accomplished by with a keyfile embedded in the initramfs.

First create a keyfile and add it as LUKS key:

 # dd bs=512 count=4 if=/dev/random iflag=fullblock | install -m 0600 /dev/stdin /etc/cryptsetup-keys.d/cryptlvm.key
 # cryptsetup -v luksAddKey /dev/sda3 /etc/cryptsetup-keys.d/cryptlvm.key

Add the keyfile to the initramfs image:

Regenerate the initramfs.

When using the default sd-encrypt hook,  will be used by default, so no additional kernel parameters need to be set.

When using the  hook, set the following kernel parameters to unlock the LUKS partition with the keyfile:

 GRUB_CMDLINE_LINUX="... cryptkey=rootfs:/etc/cryptsetup-keys.d/cryptlvm.key"

If for some reason the keyfile fails to unlock the boot partition, systemd will fallback to ask for a passphrase to unlock and, in case that is correct, continue booting.

## Using a USB drive to unlock /boot
To avoid having to memorise a complicated password, or using a simple one which may be guessed, a keyfile stored on an external USB drive can be used to unlock the LUKS volume. For this to be secure, this USB drive must be stored securely away from the computer when not in use.

First, generate a keyfile in the same way as in #Avoiding having to enter the passphrase twice. Do not use the same keyfile as if the USB drive is lost or compromised you will need to replace the keyfile embedded in initramfs.

Copy this keyfile to your USB drive and create a new GRUB configuration file:

Create a GRUB image and install it (not all of these modules will be needed depending on your file system):

 # grub-mkimage -p /boot/grub -O x86_64-efi -c /boot/grub/grub-pre.cfg -o /tmp/grubx64.efi  part_gpt  part_msdos cryptodisk  luks  gcry_rijndael gcry_sha512 lvm ext2 ntfs fat exfat
 # install -v /tmp/grubx64.efi /efi/EFI/GRUB/grubx64.efi

## Root on ZFS
To use dm-crypt with ZFS, see ZFS#Encryption in ZFS using dm-crypt.

Additionally, ZFS features native encryption, which may also be utilized to encrypt the system root, excluding the boot loader and file system metadata. See:

* Arch Linux Root on ZFS guide on the OpenZFS page,
* Install Arch Linux on ZFS.

After the installation, a boot loader can be verified with Secure Boot on UEFI-based systems.
