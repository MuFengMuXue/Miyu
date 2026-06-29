# Limine

Limine is an advanced, portable, multiprotocol boot loader originally developed as the reference implementation for the Limine boot protocol, but also supporting the ability to boot Linux as well as to chainload other boot loaders.

## Supported file systems
Limine supports FAT12, FAT16, FAT32 and ISO9660. The list of supported file systems is intentionally limited per Limine's design philosophy.

## Installation
Install the  package.

Follow the instructions in #Deploying the boot loader and #Configuration.

## Deploying the boot loader
## UEFI systems
Deploying Limine on UEFI systems involves copying the  file to the EFI system partition, and to make the UEFI BIOS aware of it.

 # mkdir -p esp/EFI/arch-limine
 # cp /usr/share/limine/BOOTX64.EFI esp/EFI/arch-limine/

Limine does not add an entry for the boot loader in the NVRAM automatically. Use efibootmgr to setup an entry for Limine.

To do so, one can do the following:

 # efibootmgr \
       --create \
       --disk /dev/sdX \
       --part Y \
       --label "Arch Linux Limine Boot Loader" \
       --loader '\EFI\arch-limine\BOOTX64.EFI' \
       --unicode

*  is the disk (not a partition) where the ESP is located on. For example  or . See Device file#Block device names for a description of the block device naming scheme.
*  is the partition index of the ESP, so if the ESP is , then  should be .

## BIOS systems with MBR
Deploying Limine on BIOS systems involves copying the  file, which contains stage 3 code that Limine needs to boot, to either the root, a , a , or a  directory of any partition on the disk onto which Limine will be deployed, as long as the filesystem is supported. This usually means having to use a FAT partition for , and copying the  file to .

For example:

 # mkdir -p /boot/limine
 # cp /usr/share/limine/limine-bios.sys /boot/limine/

Then, early stage boot loader code needs to be deployed to the disk:

 # limine bios-install /dev/sdX

 is the disk (not a partition) where Limine is to be installed. For example  or . This has to be the disk hosting the  partition. See Device file#Block device names for a description of the block device naming scheme.

## BIOS systems with GPT
To deploy Limine for BIOS booting from a GPT partitioned disk, one needs to specify a GPT partition onto which to store the early stage boot loader code (this is in addition to the FAT boot partition, usually mounted at , as explained in previous section). This partition must be at least 32 KiB in size, and should not be formatted with a file system or mounted.

Create a partition on the disk with no file system and with partition type GUID :

* fdisk: create a partition and use the  command to change its partition type to .
* gdisk: create a partition with partition type .
* GNU Parted: create a partition and set the  flag on it.

Then deploy the early stage boot loader code to the disk and partition:

 # limine bios-install /dev/sdX partition_number

 is the disk (not a partition) where Limine is to be installed. For example  or . This has to be the disk hosting the  partition. See Device file#Block device names for a description of the block device naming scheme.

If the partition number is left out,  will try to detect it automatically.

Like for the BIOS/MBR case, one must copy the  file to either the root, a , a , or a  directory in any of the partitions, using a supported file system, on the same disk where the early stage boot loader code was deployed.

## UEFI + BIOS bootable drives
As long as a drive is MBR formatted, and it contains an EFI system partition (which can be the same as the  partition used for BIOS systems), it is possible to follow both the BIOS and UEFI deployment procedures in order to create a drive capable of booting on both legacy BIOS as well as UEFI systems. This is useful, for example, for installing an operating system on a USB flash drive which is to be used on multiple systems which may or may not support UEFI, or to ease moving hard drives across systems.

## Configuration
 does not ship a default configuration file, it is therefore necessary to create one. This file is necessary to teach Limine which operating systems are available for boot. The configuration file has a lot of options as Limine allows for a fair degree of customisation. A detailed documentation of the configuration file, its format, and its options can be found here.

For UEFI systems, the configuration file may reside in the same directory as the Limine EFI executable, where it is first searched (recommended, as it allows installing multiple instances of Limine with different configurations, without conflicts).

For BIOS systems (or for UEFI systems where the configuration file was not placed alongside the Limine executable), the configuration file needs to reside on either the root, a , a , or a  directory of a partition on the drive on which Limine is deployed, as long as the file system of said partition is supported.

The configuration file has to be named .

Here follows a simple configuration file example that contains 1 boot menu entry that describes a typical Arch Linux kernel and initramfs:

 is the root file system's UUID.

In case the  partition, where the kernel and initramfs are, and the partition of the  file do not match (such as, for example, on UEFI systems with an extra  partition which is not the same as the ESP, and  is placed on the ESP), it may be necessary to replace  in the configuration file with , where  represents the PARTUUID of the  FAT partition.

## Memtest86+
Add one of the following entries to the configuration file.

For UEFI, install  and add:

For BIOS, install  and add:

## Windows entry (UEFI)
Add the following to the configuration:

Alternatively replace  with , where  is the PARTUUID of the ESP, if  is not on the ESP.

## pacman hook
While not mandatory, it may be useful to set up a pacman hook to deploy Limine whenever it is upgraded.

## UEFI
## BIOS
*  is the disk (not a partition) where Limine was installed to in the previous steps.

## Tips and tricks
## Boot entry automation
To automate kernel integration (initramfs or UKI) with Limine, install:

*  for Dracut
or
*  for mkinitcpio

Both tools include pacman hooks for automatically handling kernel entries.

## Configurations
(Optional) Copy  to  if not present.

Edit :
* If  does not detect your ESP, manually set  to any mounted FAT32 boot partition you want to use. Then run  to install the Limine EFI binary.
* Configure permanent kernel parameters as described below.

* (Optional) To save ESP space, set  to  to disable automatic fallback generation by Dracut for initramfs or UKI.
* (Optional) If you prefer booting with UKI, set  to .

* (Optional) Set  to  to detect and add systemd-boot, rEFInd, or the default EFI loader to Limine if they are present in the same ESP.
* (Optional) Install  to keep the kernel in case of an upgrade failure, ensuring system functionality after reboot.
* (Optional) Install Limine as the default EFI fallback. Some motherboards will automatically boot this if custom boot entries are removed by BIOS firmware or Windows updates.
 # limine-install --fallback
* (Optional) Test a different custom Limine binary, edit  and add:
 SKIP_LIMINE_VERSION_CHECK=yes
 LIMINE_BINARY_PATH=/path/to/custom_limine.efi
This skips the version validation and uses your specified Limine binary for installation to the boot partition.

For more configuration options, refer to limine-entry-tool README

## Commands
*  installs Limine to your EFI system partition.
*  updates Limine and generates an initramfs or UKI depending on your initramfs generator:
** For mkinitcpio: run  instead of
** For dracut: run  instead of
*  detects active EFI boot entries (dual boot) and allows you to easily add them to Limine.
*  displays boot entries in a hierarchical tree view with a default depth of 3.
* Removes one or more matching boot entries by path, preserving their bootable files. position selects which of the matching entries is targeted. The default is 1. If set to 0, all matches are removed.
 # limine-remove-entry "entry name/sub-entry name/..." position
*  uses  to sign the binary  when Secure Boot is enabled.

## Hooks
Hooks are located in the following directories:

*  executed before kernel management and updating  on the boot partition.
*  executed after kernel management and updating  on the boot partition.

Execution order is lexical based on filename sorting.

A hook can be disabled by appending the suffix  to its filename.

Examples:

1.  enrolls a Limine config checksum into the Limine binary.

2.  sets the boot partition to read-only to prevent accidental recursive writes. It is disabled by default.

See more information about hooks

## Snapper snapshot integration for Btrfs
 tool provides integration between Snapper and the Limine boot loader. It is useful for:

* Booting into selected Snapper snapshot.
* Providing 3 different methods for restoring a system snapshot: ,  or native .
* Adding a "backup" snapshot entry to the Limine bootloader after restoring a snapshot, making it easy to revert if needed.
* Automatically repairing corrupted bootable files on the boot partition by copying them from a newly created snapshot containing the same bootable files.
* Automatically notifying the desktop about potential hardware issues if two independently generated hashes of a bootable file do not match.
* Supporting an A/B-like system via multiple independent root subvolumes, each with its own Limine snapshot entries, requiring a unique machine-ID and a custom subvolume path in the kernel command line for booting.
* Testing read-only snapshots: Use overlayfs to test any installed packages on an immutable-like system without modifying the original data. Note that this does not mean testing the boot partition or a separate home subvolume/partition.

## Configurations
1. Configure  to include either the  or  keyword for auto-generated snapshot entries.

An example:

2. (Optional) Copy any configurations from  to  if they are not already present.

Edit , which will override :

* If  does not detect your ESP, manually set  to your ESP/boot mount point.
* (Optional) Set  to stop creating new snapshot entries when the limit of the boot partition usage is exceeded. The default is 85.
* (Optional) Set  to limit the number of snapshot boot entries. The default is 8, or change it to . In  mode, older snapshot boot entries are automatically removed when the boot partition usage limit  is reached, without warning.

* If using custom Snapper layout, make sure to configure the following:
** Specify  for the path to your root subvolume. The default is  in most cases.
** Specify  for the path to your root snapshots. The default is , which is the standard Snapper layout for the root subvolume .

3. Run the command to check if it succeeds or shows an error message:
 # limine-snapper-sync

4. If everything works, then enable/start  to automatically synchronize boot entries with the Snapper snapshot list.

5. (Optional) Install . It triggers Snapper to create snapshots during system updates, which limine-snapper-sync then synchronizes to generate related snapshot entries in Limine.

For further details and additional configuration options, refer to limine-snapper-sync README.

## Commands
*  synchronizes Limine snapshot entries with the Snapper list.
*  displays the current Limine snapshot entries.
*  provides detailed information about versions, the total number of bootable snapshots, and verifies bootable files.
*  restores your system, including matching kernel versions, from a selected bootable snapshot.
*  removes snapshot boot entries to free up space on the boot partition. It does not  delete the corresponding Snapper snapshots.

## Known issues
* Supports only any Snapper layouts, not arbitrary Btrfs layouts without Snapper.
* Cannot generate bootable snapshot entries for old snapshots created before the tool was installed, as these snapshots typically no longer have their corresponding kernel versions.

## Troubleshooting
Having problems? Check out the troubleshooting guide in the README
