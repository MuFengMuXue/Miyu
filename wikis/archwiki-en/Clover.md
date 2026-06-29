# Clover

Clover EFI is a boot loader developed to boot macOS (Hackintoshes), Windows and Linux in legacy or UEFI mode.

The main advantages of Clover are:

* Emulate UEFI on legacy BIOS systems
* Boot Linux kernels with EFI boot stub support
* Supports native resolution GUI on wide screens people commonly use today
* Easy to use
* Easily customizable

## Supported file systems
Clover inherits the support for the file systems from the firmware (i.e. at least FAT12, FAT16 and FAT32). Additionally it loads any UEFI drivers placed in the  subdirectory of its own installation directory on the ESP (i.e. )Clover also ships with multiple [https://github.com/CloverHackyColor/CloverBootloader/tree/master/FileSystems EFI file system drivers.

## Installation
As Clover emulates a UEFI environment on BIOS systems, the steps for each type of system are similar.

## UEFI Systems
Mount EFI system partition to . This is the preferred method when directly booting an EFI boot stub kernel from UEFI.

Generate initial ramdisk environment with mkinitcpio

Download Clover Bootable ISO from here.

Extract the archive  and find the  file, mount it to a directory like . It should be noted all file/folder names will be displayed in lower case in Linux, which is different from Windows and Mac OS.

Copy the whole  folder to your EFI system partition. The tree for  should look likes the following

 /boot/EFI
 /boot/EFI/BOOT
 /boot/EFI/CLOVER
 /boot/initramfs-linux-fallback.img
 /boot/initramfs-linux.img
 /boot/vmlinuz-linux

## BIOS Systems
Download the Clover Bootable ISO.

Extract the archive  and find the  file, mount it to directory like .

The Clover code must be merged now with current Master and Partition Boot Records.
Example with block device  and ESP on 1st partition , change if necessary:

Mount the EFI system partition to .

Copy the whole  folder to your EFI system partition.

Copy the legacy boot loader to the EFI system partition:

## Configuration
Configuration is done through an XML file  under path  from the EFI system partition.

For the meaning of each key, please reference their wiki for custom entries. The key  should be the PARTUUID of the EFI system partition and must be in uppercase. The minimal initramfs  in and the Linux kernel executable  in  are relative to the EFI system partition. Backslashes should be used in accordance with EFI standards. For other arguments in , please reference EFI boot stub and Kernel parameters#Parameter list.

In this example, the initramfs and kernel files are placed at the root of the EFI system partition, at the same level as the  directory. The EFI system partition is mounted at

## chainload systemd-boot
If you need a boot loader for BIOS systems that follows The Boot Loader Specification, then systemd-boot can be pressed into service on BIOS systems. This is the configuration file needed make Clover chainload systemd-boot.
