# Installation guide

This document is a guide for installing Arch Linux using the live system booted from an installation medium made from an official installation image. The installation medium provides accessibility features which are described on the page Install Arch Linux with accessibility options. For alternative means of installation, see Installation process.

Before installing, it would be advised to view the FAQ. For conventions used in this document, see Help:Reading. In particular, code examples may contain placeholders (formatted in ) that must be replaced manually.

This guide is kept concise and you are advised to follow the instructions in the presented order per section. For more detailed instructions, see the respective ArchWiki articles or the various programs' man pages, both linked from this guide. For interactive help, the IRC channel and the forums are also available.

Arch Linux should run on any x86_64-compatible machine with a minimum of 512 MiB RAM, though more memory is needed to boot the live system for installation.A basic installation should take less than 2 GiB of disk space. As the installation process needs to retrieve packages from a remote repository, this guide assumes a working internet connection is available.

## Pre-installation
## Acquire an installation image
Visit the [https://archlinux.org/download/ Download page and, depending on how you want to boot, acquire the ISO file or a netboot image, and the respective PGP signature.

## Verify signature
It is recommended to verify the image signature before use, especially when downloading from an HTTP mirror, where downloads are generally prone to be intercepted to serve malicious images.

Download the ISO PGP signature from https://archlinux.org/download/#checksums to the ISO directory and follow the instructions there to verify it.

Alternatively, from an existing Arch Linux installation run:

 $ pacman-key -v archlinux-version-x86_64.iso.sig

## Prepare an installation medium
The ISO can be supplied to the target machine via a USB flash drive, an optical disc or a network with PXE: follow the appropriate article to prepare yourself an installation medium from the ISO file.

For the netboot image, follow Netboot#Boot from a USB flash drive to prepare a USB flash drive for UEFI booting.

## Boot the live environment
# Point the current boot device to the one which has the Arch Linux installation medium. Typically it is achieved by pressing a key during the POST phase, as indicated on the splash screen. Refer to your motherboard's manual for details.
# When the installation medium's boot loader menu appears,
#* if you used the ISO, select Arch Linux install medium and press  to enter the installation environment.
#* if you used the Netboot image, choose a geographically close mirror from Mirror menu, then select Boot Arch Linux and press .
# You will be logged in on the first virtual console as the root user, and presented with a Zsh shell prompt.

To switch to a different console—for example, to view this guide with Lynx alongside the installation—use the  keyboard shortcut. To edit configuration files, , nano and vim are available. See pkglist.x86_64.txt for a list of the packages included in the installation medium.

## Set the console keyboard layout and font
The default console keymap is US. Available layouts can be listed with:

 # localectl list-keymaps

To set the keyboard layout, pass its name to . For example, to set a German keyboard layout:

 # loadkeys de-latin1

Console fonts are located in  and can likewise be set with  omitting the path and file extension. For example, to use one of the largest fonts suitable for HiDPI screens, run:

 # setfont ter-132b

## Verify the boot mode
To verify the boot mode, check the UEFI bitness:

 # cat /sys/firmware/efi/fw_platform_size

* If the command returns , the system is booted in UEFI mode and has a 64-bit x64 UEFI.
* If the command returns , the system is booted in UEFI mode and has a 32-bit IA32 UEFI. While this is supported, it will limit the boot loader choice to those that support mixed mode booting.

* If it returns , the system may be booted in BIOS (or CSM) mode.
If the system did not boot in the mode you desired (UEFI vs BIOS), refer to your motherboard's manual.

## Connect to the internet
To set up a network connection in the live environment, go through the following steps:

# Ensure your network interface is listed and enabled, for example with :
# For wireless and WWAN, make sure the card is not blocked with rfkill.
# Connect to the network:
#* Ethernet—plug in the cable.
#* Wi-Fi—authenticate to the wireless network using iwctl.
#* Mobile broadband modem—connect to the mobile network with the mmcli utility.
# Configure your network connection:
#* DHCP: dynamic IP address and DNS server assignment (provided by systemd-networkd and systemd-resolved) should work out of the box for Ethernet, WLAN, and WWAN network interfaces.
#* Static IP address: follow Network configuration#Static IP address.
# The connection may be verified with ping:

## Update the system clock
The live system needs accurate time to prevent package signature verification failures and TLS certificate errors. The systemd-timesyncd service is enabled by default in the live environment and time will be synchronized automatically once a connection to the internet is established.

Use  to ensure the system clock is synchronized:

 # timedatectl

## Partition the disks
When recognized by the live system, disks are assigned to a block device such as ,  or . To identify these devices, use lsblk or fdisk.

 # fdisk -l

Results ending in ,  or  may be ignored.  devices ending in ,  and  can be ignored.

The following partitions are required for a chosen device:

* One partition for the root directory .
* For booting in UEFI mode: an EFI system partition.

Use a partitioning tool like fdisk to modify partition tables. For example:

 # fdisk /dev/the_disk_to_be_partitioned

## Example layouts
{| class="wikitable"
|+ UEFI with GPT
|-
! Mount point on the installed system
! Partition
! Partition type
! Suggested size
|-
| 1
|
| EFI system partition
| 1 GiB
|-
|
|
| Linux swap
| At least 4 GiB
|-
|
|
| Linux x86-64 root (/)
| Remainder of the device. At least 23–32 GiB.
|}

# Other mount points, such as , are possible, provided that the used boot loader is capable of loading the kernel and initramfs images from the root volume. See the warning in Arch boot process#Boot loader.

{| class="wikitable"
|+ BIOS with MBR
|-
! Mount point on the installed system
! Partition
! Partition type
! Suggested size
|-
|
|
| Linux swap
| At least 4 GiB
|-
|
|
| Linux
| Remainder of the device. At least 23–32 GiB.
|}

See also Partitioning#Example layouts.

## Format the partitions
Once the partitions have been created, each newly created partition must be formatted with an appropriate file system. See File systems#Create a file system for details.

For example, to create an Ext4 file system on , run:

 # mkfs.ext4 /dev/root_partition

If you created a partition for swap, initialize it with :

 # mkswap /dev/swap_partition

If you created an EFI system partition, format it to FAT32 using .

 # mkfs.fat -F 32 /dev/efi_system_partition

## Mount the file systems
Mount the root volume to . For example, if the root volume is :

 # mount /dev/root_partition /mnt

Create any remaining mount points under  (such as  for ) and mount the volumes in their corresponding hierarchical order.

For UEFI systems, mount the EFI system partition. For example:

 # mount --mkdir /dev/efi_system_partition /mnt/boot

If you created a swap volume, enable it with :

 # swapon /dev/swap_partition

 will later detect mounted file systems and swap space.

## Installation
## Select the mirrors
Packages to be installed must be downloaded from mirror servers, which are defined in . The higher a mirror is placed in the list, the more priority it is given when downloading a package.

On the live system, all HTTPS mirrors are enabled (i.e. uncommented). The topmost worldwide mirror should be fast enough for most people, but you may still want to inspect the file to see if it is satisfactory. If it is not, edit the file accordingly, and move the geographically closest mirrors to the top of the list, although other criteria should be taken into account. Alternatively, you can use reflector to create a mirrorlist file based on various criteria.

This file will later be copied to the new system by pacstrap, so it is worth getting right.

## Install essential packages
No configuration (except for ) gets carried over from the live environment to the installed system. The only mandatory package to install is , which does not include all tools from the live installation, so installing more packages is frequently necessary.

In particular, review the following software and install everything that you need:

* CPU microcode updates— or —for hardware bug and security fixes,
* userspace utilities for file systems that will be used on the system—for the purposes of e.g. file system creation and fsck,
* utilities for accessing and managing RAID or LVM if they will be used on the system,
* specific firmware for other devices not included in  (e.g.  for onboard audio,  for Marvell wireless and any of the multiple firmware packages for Broadcom wireless),
* software necessary for networking (e.g. a network manager or a standalone DHCP client, authentication software for Wi-Fi, ModemManager for mobile broadband connections),
* a console text editor (e.g nano) to allow editing configuration files from the console,
* packages for accessing documentation in man and info pages: ,  and .

For comparison, packages available in the live system can be found in pkglist.x86_64.txt.

To install more packages or package groups, append the names to the  command below (space separated) or use pacman to install them while chrooted into the new system.

For example, a basic installation with the Linux kernel and firmware for common hardware:

 # pacstrap -K /mnt base linux linux-firmware

## Configure the system
## Fstab
To get needed file systems (like the one used for the boot directory ) mounted on startup, generate an fstab file with persistent block device naming using . For example, reference file systems by their UUIDs with :

 # genfstab -U /mnt >> /mnt/etc/fstab

Check the resulting  file, and edit it in case of errors.

## Chroot
To directly interact with the new system's environment, tools, and configurations for the next steps as if you were booted into it, change root into the new system:

 # arch-chroot /mnt

## Time
For human convenience (e.g. showing the correct local time or handling Daylight Saving Time), set the time zone:

 # ln -sf /usr/share/zoneinfo/Area/Location /etc/localtime

Run  to generate :

 # hwclock --systohc

This command assumes the hardware clock is set to UTC. See System time#Time standard for details.

To prevent clock drift and ensure accurate time, set up time synchronization using a Network Time Protocol (NTP) client such as systemd-timesyncd.

## Localization
To use the correct region and language specific formatting (like dates, currency, decimal separators), edit  and uncomment the UTF-8 locales you will be using. Generate the locales by running:

 # locale-gen

Create the  file, and set the LANG variable accordingly:

If you set the console keyboard layout, make the changes persistent in :

## Network configuration
To assign a consistent, identifiable name to your system (particularly useful in a networked environment), create the hostname file:

Complete the network configuration for the newly installed environment. That may include installing suitable network management software, configuring it if necessary and enabling its systemd unit so that it starts at boot.

## Initramfs
Creating a new initramfs is usually not required, because mkinitcpio was run on installation of the kernel package with pacstrap.

For LVM, system encryption or RAID, modify  and recreate the initramfs image. If you have changed the default console keymap, only recreating the initramfs is required:

 # mkinitcpio -P

## Root password
Set a secure password for the root user to allow performing administrative actions:

 # passwd

## Boot loader
Choose a boot loader applicable to your partitioning scheme and install it. See the explanations and the comparison table in Arch boot process#Boot loader to make your choice, then follow the installation instructions on its dedicated page.

## Reboot
Exit the chroot environment by typing  or pressing .

Optionally manually unmount all the partitions with : this allows noticing any "busy" partitions, and finding the cause with .

Finally, restart the machine by typing : any partitions still mounted will be automatically unmounted by systemd. Remember to remove the installation medium and then login into the new system with the root account.

## Post-installation
See General recommendations for system management directions and post-installation tutorials (like creating unprivileged user accounts, setting up a graphical user interface, sound or a touchpad).

For a list of applications that may be of interest, see List of applications.
