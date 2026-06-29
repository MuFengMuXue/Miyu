# Multiboot USB drive

A multiboot USB flash drive allows booting multiple ISO files from a single device. The ISO files can be copied to the device and booted directly without unpacking them first. There are multiple methods available, but they may not work for all ISO images.

## Using GRUB and loopback devices
Advantages:

* only a single partition required
* all ISO files are found in one directory
* adding and removing ISO files is simple

Disadvantages:

* not all ISO images are compatible
* the original boot menu for the ISO file is not shown
* it can be difficult to find a working boot entry

## Preparation
Create at least one partition and a filesystem supported by GRUB on the USB drive. See Partitioning and File systems#Create a file system. Choose the size based on the total size of the ISO files that you want to store on the drive, and plan for extra space for the boot loader.

## Installing GRUB
## Simple installation
Mount the filesystem located on the USB drive:

 # mount /dev/sdXY /mnt

Create the directory /boot:

 # mkdir /mnt/boot

Install GRUB on the USB drive:

 # grub-install --target=i386-pc --recheck --boot-directory=/mnt/boot /dev/sdX

In case you want to boot ISOs in UEFI mode, you have to install grub for the UEFI target:

 # grub-install --target=x86_64-efi --removable --boot-directory=/mnt/boot --efi-directory=/mnt

For UEFI, the partition has to be the first one in an MBR partition table and formatted with FAT32.

## Hybrid UEFI GPT + BIOS GPT/MBR boot
This configuration is useful for creating a universal USB key, bootable everywhere.
First of all you must create a GPT partition table on your device. You need at least 3 partitions:

# A BIOS boot partition (gdisk type code ). This partition must be 1 MiB in size
# An EFI system partition (gdisk type code  with a FAT32 filesystem). This partition can be as small as 50 MiB.
# Your data partition (use a filesystem supported by GRUB). This partition can take up the rest of the space of your drive.

Next you must create a hybrid MBR partition table. Without it, a BIOS MBR based system will not boot. It will not find the partitions it expects to find.

Hybrid MBR partition table creation example using gdisk:

Do not forget to format the partitions:

 # mkfs.fat -F32 /dev/sdX2
 # mkfs.ext4 /dev/sdX3

You can now install GRUB to support both EFI + GPT and BIOS + GPT/MBR. The GRUB configuration (--boot-directory) can be kept in the same place.

First, you need to mount the EFI system partition and the data partition of your USB drive.

An example of this would be as follows:

 # mount /dev/sdX3 /mnt
 # mkdir /mnt/boot /mnt/efi
 # mount /dev/sdX2 /mnt/efi

Then, you can install GRUB for UEFI with:

In most cases  will correspond to the  directory on your mounted USB disk.
 is where your data partition is mounted. In this example it would be the mount point of sdX3, .

 # grub-install --target=x86_64-efi --recheck --removable --efi-directory=/EFI_MOUNTPOINT --boot-directory=/DATA_MOUNTPOINT/boot

And for BIOS with:

 # grub-install --target=i386-pc --recheck --boot-directory=/DATA_MOUNTPOINT/boot /dev/sdX

As an additional fallback, you can also install GRUB on your MBR-bootable data partition:

 # grub-install --target=i386-pc --recheck --boot-directory=/DATA_MOUNTPOINT/boot /dev/sdX3

## Configuring GRUB
## Using a template
There are some git projects which provide some pre-existing GRUB configuration files, and a nice generic  which can be used to load the other boot entries on demand, showing them only if the specified ISO files - or folders containing them - are present on the drive.

Multiboot USB: https://github.com/hackerncoder/multibootusb

GLIM (GRUB2 Live ISO Multiboot): https://github.com/thias/glim

## Manual configuration
For the purpose of multiboot USB drive it is easier to edit  by hand instead of generating it. Alternatively, make the following changes in  or  and generate  using grub-mkconfig.

As it is recommend to use a persistent name instead of  to identify the partition on the USB drive where the image files are located, define a variable for convenience to hold the value. If the ISO images are on the same partition as GRUB, use the following to read the UUID at boot time:

Or specify the UUID explicitly:

Alternatively, use the device label instead of UUID:

The necessary UUID or label can be found using . Do not use the same label as the Arch ISO for the USB device, otherwise the boot process will fail.

To complete the configuration, a boot entry for each ISO image has to be added below this header, see the next section for examples.

## Boot entries
It is assumed that the ISO images are stored in the  directory on the same filesystem where GRUB is installed. Otherwise it would be necessary to prefix the path to ISO file with device identification when using the  command, for example . As this identification of devices is not persistent, it is not used in the examples in this section.

One can use persistent block device naming like so. Replace the UUID according to your ISO filesystem UUID.

## Arch Linux monthly release
The ISO provides a loopback.cfg which you can leverage with an entry like this.

{{bc|1=
menuentry '{
	set iso_path='/boot-isos/archlinux-2023.10.14-x86_64.iso'
	export iso_path
	search --set=root --file "$iso_path"
	loopback loop "$iso_path"
	root=(loop)
	configfile /boot/grub/loopback.cfg
	loopback --delete loop
}
}}

Also see archiso.

## MemTest86+
MemTest86+ is included in the monthly ISO.

{{bc|1=
menuentry '[loopbackarchlinux-2023.03.01-x86_64.iso MemTest86+' {
	set iso_path='/boot-isos/archlinux-2023.03.01-x86_64.iso'
	loopback loop $iso_path
	linux (loop)/boot/memtest86+/memtest.efi
}
}}

## Archboot
See Archboot Homepage.

{{bc|1=
menuentry '{
	set iso_path='/boot-isos/archlinux-2014.11-1-archboot.iso'
	loopback loop $iso_path
	linux (loop)/boot/vmlinuz_x86_64 iso_loop_dev=$imgdevpath iso_loop_path=$iso_path
	initrd (loop)/boot/initramfs_x86_64.img
}
}}

## Using Syslinux and memdisk
Using the [https://wiki.syslinux.org/wiki/index.php/MEMDISK memdisk module, the ISO image is loaded into memory, and its boot loader is loaded. Make sure that the system that will boot this USB drive has sufficient amount of memory for the image file and running operating system.

## Preparation
Make sure that the USB drive is properly partitioned and that there is a partition with file system supported by Syslinux, for example fat32 or ext4. Then install Syslinux to this partition, see Syslinux#BIOS systems.

## Install the memdisk module
The memdisk module was not installed during Syslinux installation, it has to be installed manually. Mount the partition where Syslinux is installed to  and copy the memdisk module to the same directory where Syslinux is installed:

 # cp /usr/lib/syslinux/bios/memdisk /mnt/boot/syslinux/

## Configuration
After copying the ISO files on the USB drive, edit the Syslinux configuration file and create menu entries for the ISO images. The basic entry looks like this:

See memdisk on Syslinux wiki for more configuration options.

## Automated tools
*
*
*
*
