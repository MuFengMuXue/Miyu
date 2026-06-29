# EFI system partition

The EFI system partition (also called ESP) is an OS independent partition that acts as the storage place for the UEFI boot loaders, applications  and drivers to be launched by the UEFI firmware. It is mandatory for UEFI boot.

## Check for an existing partition
If you are installing Arch Linux on an UEFI-capable computer with an installed operating system, like Windows 10 for example, it is very likely that you already have an EFI system partition.

To find out the disk partition scheme and the system partition, use fdisk as root on the disk you want to boot from:

 # fdisk -l /dev/sdx

The command returns:

* The disk's partition table: it indicates  if the partition table is GPT or  if it is MBR.
* The list of partitions on the disk: Look for the EFI system partition in the list, it is usually at least 100 MiB in size and has the type  or . To confirm this is the ESP, mount it and check whether it contains a directory named , if it does this is definitely the ESP.

If you found an acceptable existing EFI system partition, simply proceed to #Mount the partition. If you did not find one, you will need to create it, proceed to #Create the partition.

## Create the partition
The following two sections show how to create an EFI system partition (ESP).

The partition size should provide adequate space for storing boot loaders and other files required for booting.

It is recommended to make the partition 1 GiB in size to ensure it has adequate space for multiple kernels or unified kernel images, a boot loader, firmware updates files and any other operating system or OEM files. If still in doubt, 4 GiB ought to be enough for anybody.

For tools like Limine boot loader with Snapper integration for Btrfs (which supports creating multiple bootable snapshots) and Archiso on ESP (a bootable ISO image for system recovery without external media) consider an even larger size (e.g. 8 GiB).

## GPT partitioned disks
EFI system partition on a GUID Partition Table is identified by the partition type GUID .

Choose one of the following methods to create an ESP for a GPT partitioned disk:

* fdisk: Create a partition and use the  command to change its partition type to  using the alias .
* gdisk: Create a partition with partition type .
* GNU Parted: Create a partition with  as the file system type and set the  flag on it.

After creating the partition, it should be formatted with a file system. Proceed to the #Format the partition section below.

## MBR partitioned disks
EFI system partition on a Master Boot Record partition table is identified by the partition type ID .

Choose one of the following methods to create an ESP for a MBR partitioned disk:

* fdisk: Create a primary partition and and use the  command to change its partition type to .
* GNU Parted: Create a primary partition with  as the file system type and set the  flag on it.

After creating the partition, it should be formatted with a file system. Proceed to the #Format the partition section below.

## Format the partition
The UEFI specification mandates support for the FAT12, FAT16, and FAT32 file systems (see UEFI specification version 2.11, section 13.3.1.1), but any conformant vendor can optionally add support for additional file systems; for example, the firmware in Apple Macs supports the HFS+ file system.

To prevent potential issues with other operating systems and since the UEFI specification says that UEFI "encompasses the use of FAT32 for a system partition, and FAT12 or FAT16 for removable media"it is recommended to use FAT32. Use the  utility from :

 # mkfs.fat -F 32 /dev/sdxY

If you get the message  and you cannot create a larger ESP, reduce cluster size with  or ; otherwise the partition may be unreadable by UEFI. See  for supported cluster sizes.

For partitions smaller than 32 MiB using FAT32 may not be possible. In which case, format it to FAT16 or even FAT12. For example, a 2 MiB ESP will only be able to support FAT12:

 # mkfs.fat -F 12 /dev/sdxY

## Mount the partition
The kernels, initramfs files, and, in most cases, the processor's microcode, need to be accessible by the boot loader or UEFI itself to successfully boot the system. Thus if you want to keep the setup simple, your boot loader choice limits the available mount points for EFI system partition.

## Typical mount points
The three typical scenarios for mounting the EFI system partition are:

* mount the ESP to :
** This facilitates system maintenance and administration, as  is the default path where microcode packages place the CPU microcode initramfs files and where mkinitcpio places kernels and initramfs images.
** This ensures that the above files are accessible to most boot loaders, as not all of them can access files on other volumes.
** This prevents setting file-specific permissions and/or extended attributes, as FAT sets global permissions at mount time
** This increases the size requirement for the ESP, as files normally installed in  will join the ones used for UEFI booting.
** This exposes the kernel and initramfs images to potentially hazardous manipulation from bootable drives or other operating systems when dual-booting.
** This makes encrypting /boot impossible, as the boot loader and its files have to be accessible by the firmware.
** This makes root volume snapshots (using Btrfs, Bcachefs, ZFS, LVM) less effective as  content would not be included. In case of kernel updates, returning to a snapshot with older kernel version would draw the system unbootable and require manually downgrading the kernel using external media.
* mount the ESP to  and additionally mount an "Extended Boot Loader Partition" (XBOOTLDR) to . This can be useful when a previously created ESP is too small to hold multiple boot loaders and/or kernels but the ESP cannot be easily resized (such as when installing Linux after Windows to dual boot). This method is supported by at least systemd-boot.
* mount the ESP to :
**
** It ensures a separation of concerns between operating system and UEFI files, which may include other operating system files that are better left alone.
** It avoids increasing the size requirement of the ESP by not placing the files installed to  in it: only the EFI binaries (the boot loader (and optionally drivers) and/or the unified kernel image) will be stored on the ESP, which saves storage space.
** It allows to preserve Linux-specific filesystem permissions for files residing in , avoiding FAT limitations.
** It allows to mount separately the ESP according to the need, e.g. only when upgrading the boot loader.
** If using system encryption with the appropriate setup, it allows to leave only a few required files unencrypted while  remains protected: this can be useful for unified kernel images or boot loaders that have file system drivers capable of accessing the kernel(s) and files that are stored elsewhere.

## Alternative mount points
If you do not use one of the #Typical mount points, you will need to copy your boot files to ESP (referred to hereafter as ).

 # mkdir -p esp/EFI/arch
 # cp -a /boot/vmlinuz-linux esp/EFI/arch/
 # cp -a /boot/initramfs-linux.img esp/EFI/arch/
 # cp -a /boot/initramfs-linux-fallback.img esp/EFI/arch/

Furthermore, you will need to keep the files on the ESP up-to-date with later kernel updates. Failure to do so could result in an unbootable system. The following sections discuss several mechanisms for automating it.

## Using bind mount
Instead of mounting the ESP itself to , you can mount a directory of the ESP to  using a bind mount (see ). This allows pacman to update the kernel directly while keeping the ESP organized to your liking.

Just like in #Alternative mount points, copy all boot files to a directory on your ESP, but mount the ESP outside . Then bind mount the directory:

 # mount --bind esp/EFI/arch /boot

After verifying success, edit your Fstab to make the changes persistent:

## Using systemd
systemd features event triggered tasks. In this particular case, the ability to detect a change in path is used to sync the EFISTUB kernel and initramfs files when they are updated in . The file watched for changes is  since this is the last file built by mkinitcpio, to make sure all files have been built before starting the copy. The systemd path and service files to be created are:

Then enable and start .

## Using filesystem events
Filesystem events can be used to run a script syncing the EFISTUB Kernel after kernel updates. An example with incron follows.

In order to use this method, enable the .

## Using mkinitcpio preset
As the presets in  support shell scripting, the kernel and initramfs can be copied by just editing the presets.

## Replacing the mkinitcpio hook
Edit the file :

{{hc|/etc/mkinitcpio.d/linux.preset|2=
# mkinitcpio preset file for the 'linux' package

# Directory to install the kernel, the initramfs...
ESP_DIR="esp/EFI/arch"

#ALL_config="/etc/mkinitcpio.conf"
ALL_kver="${ESP_DIR}/vmlinuz-linux"

PRESETS=('default' 'fallback')

#default_config="/etc/mkinitcpio.conf"
default_image="${ESP_DIR}/initramfs-linux.img"
default_options=""

#fallback_config="/etc/mkinitcpio.conf"
fallback_image="${ESP_DIR}/initramfs-linux-fallback.img"
fallback_options="-S autodetect"
}}
To test that, just run:

 # rm /boot/initramfs-linux-fallback.img /boot/initramfs-linux.img
 # mv /boot/vmlinuz-linux esp/EFI/arch/
 # mkinitcpio -p linux

## Another example
## Using a mkinitcpio post hook
A mkinitcpio post hook can be used to copy kernels and initramfs images to a desired directory after the initramfs is generated.

Create the following file and make it executable:

{{hc|/etc/initcpio/post/copy-kernel-and-initramfs|2=
#!/usr/bin/env bash

kernel="$1"
initramfs="$2"
target_dir="esp/EFI/arch"
files_to_copy=()

for file in "$kernel" "$initramfs"; do
	if  -n "$file"  && ! cmp -s -- "$file" "${target_dir}/${file##*/}"; then
		files_to_copy+=("$file")
	fi
done

(( ! ${#files_to_copy[@} )) && exit 0

cp -af -- "${files_to_copy"${target_dir}/"
}}

## Using pacman hook
A last option relies on the pacman hooks that are run at the end of the transaction.

The first file is a hook that monitors the relevant files, and it is run if they were modified in the former transaction.

The second file is the script itself. Create the file and make it executable:

## Tips and tricks
## Replace the partition with a larger one
On a disk with a preexisting operating system, the EFI system partition may be smaller than recommended in #Create the partition. E.g. Windows Setup creates a measly 100 MiB EFI system partition on non-4Kn drives.

In such cases, it may be a good idea to create a new, larger EFI system partition to prevent running out of space on it.

## Free up space for a new partition in Windows
In Windows, partitions can be either managed graphically with Disk Management () or from the command line with the  utility.

Run  as Administrator.

# Right click on the "(C:)" partition (the only one of the default Windows-created partitions which can be resized online) and select Shrink Volume....
# Enter  as the amount to shrink and click Shrink.

There should now be a 4 GiB unallocated space after the "(C:)" partition.

Boot into Arch Linux or the Arch Linux installation medium to proceed to creating a new partition.

## Delete the old partition and create a new one
First, make sure to backup the contents of the EFI system partition. For example, with esp being its mountpoint:

 # cp -a esp /esp_backup

Unmount the EFI system partition:

 # umount esp

Run blkid and take note of the UUID and PARTUUID values. They will later be reused for the new partition.

Delete the old partition using sgdisk from :

 # sgdisk --delete=Y /dev/sdx

Create a new partition in the largest unallocated space while reusing the old PARTUUID and PARTLABEL:

 # sgdisk --align-end --largest-new=0 --typecode=0:ef00 --change-name=0:'EFI system partition' --partition-guid=0:YYYYYYYY-YYYY-YYYY-YYYY-YYYYYYYYYYYY /dev/sdx

Tell the kernel to reread the partition table using  from :

 # partprobe /dev/sdx

Confirm the new, 4 GiB in size, EFI system partition is created by listing the partitions with fdisk:

Partition numbers are not resorted when deleting and creating partitions, so the EFI system partition number on the disk will likely be the same as before.

Format the partition to FAT32 reusing the old UUID (while removing the dash from it):

 # mkfs.fat -F 32 -i XXXXXXXX /dev/sdxY

Finally, mount the new partition and restore its contents from backup:

 # mount /dev/sdxY esp
 # cp -a /esp_backup/. esp/

If you previously stopped , start it again.

## Sacrifice an adjacent swap partition to enlarge the ESP
If there is a swap partition right after the EFI system partition, you can sacrifice it to give space for enlarging the EFI system partition. E.g. with a layout similar to:

First, deactivate the swap partition and remove it from fstab.

Use fdisk to delete the swap partition and enlarge the EFI system partition.

# Run:
# Use the  command to delete the swap partition (partition number  in the example layout above).
# Use the  command to enlarge the EFI system partition (partition number  in the example layout above). Use the suggested default value for the new size and press .
# Write changes to disk and exit via the  command.

After the partition is resized, you need to resize the file system in it. Since  [https://github.com/ya-mouse/fatresize/issues/18 does not work and libparted cannot resize FAT volumes of certain sizes, the only option is to backup the files from the existing file system and create a new one that takes up all space of the partition.

Take note of the file system UUID to allow reusing it for the new file system:

Backup the contents of the EFI system partition. For example, with esp being its mountpoint:

 # cp -a esp /esp_backup

Unmount the EFI system partition:

 # umount esp

Wipe the file system signature from the partition to avoid any artifacts from the old file system:

 # wipefs -af /dev/sdxY

Format the partition to FAT32 reusing the old UUID (while removing the dash from it):

 # mkfs.fat -F 32 -i XXXXXXXX /dev/sdxY

Finally, mount the new partition and restore its contents from backup:

 # mount /dev/sdxY esp
 # cp -a /esp_backup/. esp/

If you previously stopped , start it again.

Now that the swap partition is gone, set up swap on a swap file.

## Troubleshooting
## ESP on software RAID1
It is possible to make the ESP part of a RAID1 array, but doing so brings the risk of data corruption, and further considerations need to be taken when creating the ESP. See and [https://bbs.archlinux.org/viewtopic.php?pid=1390741#p1390741 for details and UEFI booting and RAID1 for an in-depth guide with a solution.

The key part is to use  in order to keep the RAID metadata at the end of the partition, otherwise the firmware will not be able to access it:

 # mdadm --create --verbose --level=1 --metadata=1.0 --raid-devices=2 /dev/md/ESP /dev/sdaX /dev/sdbY

Alternatively, as the ESP is not often updated, a secondary ESP can be managed by copying the primary ESP to the secondary one on a different disk during relevant updates. A boot entry for the secondary ESP can then be added manually using efibootmgr. See Debian:UEFI#RAID for the EFI System Partition for an implementation example. Note that while this avoids some risks of the RAID approach, it only works when using a single OS.

## Firmware does not see the EFI directory
If you give the FAT file system a volume name (i.e. file system label), be sure to name it something other than . That can trigger a bug in some firmwares (due to the volume name matching the EFI directory name) that will cause the firmware to act like the EFI directory does not exist.

## Hibernation and multi boot systems
If you are running a multi boot system (including but not limited to dual booting with Windows) and want to be able to boot into your other system while your main Arch Linux is hibernated, you must take extra caution not to mount the ESP in both systems, as this will likely cause data corruption and I/O errors on usage.

There are three possible mitigation strategies:

# Use a separate EFI system partition per system. Most UEFIs support this as long as the ESPs reside on physically different disks, but hardware support and usability may vary.
# Use systemd's automount mechanism to only mount the ESP when needed. Make sure to also specify an idle timeout ( option), otherwise systemd would not unmount the ESP after usage. However, note two limitations: First, unless you mount the ESP to , you must not rely on the automount during kernel upgrades (see note above). Second, you must make sure not to hibernate the system before systemd has auto-unmounted the ESP after usage (see automatic unmount).
# Mount the ESP at , and unmount it before and remount it after hibernating the system. See instructions below.

By successfully applying one of the mitigation strategies above you may hibernate this system, but not the other systems unless you apply one of the mitigation strategies to them as well. For example, applying one of the solutions to your main Arch Linux allows you to hibernate Arch Linux and boot into another e.g. Ubuntu Linux, but not to hibernate that Ubuntu Linux and boot into your main Arch Linux. Allowing this with Windows requires separate EFI system partitions.

Strictly speaking, this issue of mounting the same filesystem multiple times at once is neither limited to the EFI system partition, nor to hibernating the system. However, it is particularly relevant for the ESP, because the ESP is expected to be shared across multiple systems. The mitigation strategies can be adapted for other use cases as well.

## Unmount and remount ESP on hibernation
If you choose option 3 above, you can create and enable the following systemd system service that unmounts the ESP before hibernating the system and remounts it after resuming:

However, since  is pulled in as a requirement for  by default, stopping  also permanently brings down . This might have all sorts of negative side-effects, including ordering issues when shutting down the system, which might trigger systemd to auto-mask  as defective. This can be mitigated by telling systemd that  is not required by , but just wanted by it. To ensure this you must add the following mount options to  in :
