# Mac

This page complements the Installation guide with instructions specific to Apple Macs. The Arch installation image supports Apple Macs with Intel processors, but neither PowerPC nor Apple Silicon processors.

## Overview
Summed up, the procedure for installing Arch Linux on a Mac is:

# Pre-installation: Miscellaneous steps before partitioning.
# Partitions: Resizing or deleting the macOS partition to create partitions for Arch Linux.
# Installation: Actual installation.
# Setup boot loader: Making sure that the new partition is bootable.
# Post-installation: Device-specific configuration.

## Pre-installation
Before proceeding with the installation of Arch Linux, follow these steps.

# Install macOS and install its updates. macOS is the only known method for installing firmware updates, even though the OS will not be necessary after installing Arch. See Apple's instructions.
# Open ColorSync Utility, find the current  color profile, and save the file elsewhere. The profile can later be used to set the display colors correctly. See color profile.
# Set the volume on macOS, which will be the volume of the startup chime. If the volume is muted, the startup chime will also be muted. See mute startup chime.

## Partitions
If only Arch Linux is desired, then format the entire disk according to Installation guide#Partition the disks. To set up dual boot, follow these steps. Once done, go to #Installation.

## Arch Linux with macOS or other operating systems
Macs typically have the following partition table. In Macs that use the Apple Fusion Drive, the partition scheme could be different.

* EFI: the ~200 MB EFI system partition.
* macOS: the main partition containing your macOS installation, either HFS+ or APFS.
* Recovery: If not using APFS, a recovery partition is present. If using APFS, this partition is not present.

To install Arch with macOS, keep these partitions, and follow these steps.

# You may need to turn off FileVault before resizing the macOS partition. See Apple's instructions.
# Run Disk Utility, select the drive to be partitioned in the left-hand column, and click Partition. Do not create a container.
# Add a new partition by pressing the + button and choose how much space you want to leave for macOS, and how much for the new partition. The new partition will be formatted in Arch Linux, so you can choose any partition type you want.
# Optionally, make any other partitions you may need for your setup. See Partitioning#Partition scheme for more information.

Here is an example setup with five discrete partitions:

## Installation
These steps install Arch, assuming #Pre-installation and #Partitions are done.

# Boot the live environment by holding down  ( on an Apple keyboard) during boot.
# If the keyboard has long delays or character doubling, reboot with the following kernel parameters: . Note  will disable SPI, which is used for the builtin keyboard in some MacBook models (e.g. MBP 2017).
# If the display extends beyond the bounds of the screen (unreadable lines at the bottom) use the kernel parameters:. Note: doing this on a 2017 (and perhaps others) prevents the i915 driver from initializing properly in X11.
# Proceed through the installation as described in the Installation guide except in the following areas:
## Skip the partition the disks stage, do only the partition formatting and mounting steps, taking care to assign the correct partitions. Partitions have already been created if you followed #Partitions
## When at the install boot loader stage, follow #Setup boot loader
## (for booting with BIOS-compatibility) Add  as a kernel parameter. This will allow your Mac to reboot correctly from Arch.
# When the install process is complete, reboot your computer.
# During boot, if using optical disk, hold down the eject key to eject the disk.
# During boot, if using systemd-boot or GRUB, hold down the  key to bring up the Apple boot menu, and select "EFI Boot." If using rEFInd, boot without holding any keys.

## Setup boot loader
Macs use UEFI for booting, so any UEFI boot loader will work. The built-in boot loader (shown when holding  during boot) will detect any EFI system partition that has a  file, showing it as a "EFI Boot" entry. Most UEFI boot loaders support installing directly to this location, making a dual boot setup easy.

The boot loader also has an alternate partition discovery method described in #Installing a boot loader to a separate HFS+ partition which is the method used for booting macOS, but can also be used for Linux.

## Installing to the EFI system partition
## systemd-boot
Follow the instructions at systemd-boot#Installing the UEFI boot manager. After installing, a copy of systemd-boot will be present at .

## rEFInd
To install rEFInd to the  location, run:

 # refind-install --usedefault /dev/sdXY

Where  is the EFI system partition. After installing, see rEFInd#Configuration to finish setup.

## Installing from macOS
These steps assume macOS is still installed on a partition, and the steps of the Installation guide were completed up to Installation guide#Boot loader. Boot into Safe Mode by holding down , then disable SIP.

 # csrutil disable

Boot macOS, and run the rEFInd install script,

 # ./refind-install --alldrivers

rEFInd installed itself into Apple's boot partition, and replaced Apple's boot menu with its own. Boot into Safe Mode by holding down , and enable SIP.

 # csrutil enable

Reboot without holding down any keys. Arch should be recognized as  by default. If it is not, uncomment the lines  and  in . For configuration, see rEFInd#refind_linux.conf. Since rEFInd by default mounts root as ro, it is recommended to create refind-linux.conf.

## GRUB
To install GRUB to , follow the instructions at GRUB#Installation, adding the  option when running .

## Installing a boot loader to a separate HFS+ partition
Despite using UEFI, the Mac native EFI boot loader does not use the EFI system partition for booting macOS. Instead, it uses the following conditions to find existing macOS installations inside all the partitions in internal and external drives and shows them as possible boot options if they are satisfied:

* The partition is formatted as HFS+
* The partition type ID is  ("Apple HFS/HFS+")
* In the root of the partition, there is a file called
* Inside that partition, there a  file inside

The advantage of this method to boot Arch over using a  file in the EFI system partition is that it can coexist with macOS nicely, showing the partition as a bootable volume in the macOS Startup Disk settings. However, this method requires manual configuration. The following steps will illustrate how to perform this configuration using GRUB.

First, create a new HFS+ partition. This can be done through the macOS Disk Utility, or the  tool in the  package. The size and mount point of the partition depend on how you plan to use it:

* If you plan on using it as the /boot directory, give it at least 300 MB;
* If you are going to keep your kernels in another partition and use a boot loader that can load other file systems, like rEFInd or GRUB, the partition can be smaller and be mounted anywhere you want.

Mount the partition, then create the  file:

 # touch /mountpoint/mach_kernel

Create the directory structure for the boot loader:

 # mkdir -p /mountpoint/System/Library/CoreServices

Now you can install any UEFI boot loader you want. For example, to do a manual install of rEFInd:

Finally, you can create an optional  file that will display some information about the volume in the macOS Startup Disk settings:

After following these instructions, the new volume will appear on the Mac boot loader when holding down  during boot, and it will also appear as a bootable volume in the macOS Startup Disk options.

## Using blessing
It is possible to boot directly from GRUB in EFI mode without using rEFIt through what is known as "blessing" after placing GRUB on a separate partition.  These instructions are known to work on a MacBook7,1. It is advisable to host GRUB on either a FAT32 or HFS+ partition, but ext2 or ext3 may also work.

After the GRUB install is in the desired location, the firmware needs to be instructed to boot from that location.  This can be done from either an existing macOS install or an macOS install disk.  The following command assumes that the GRUB install is in  on an existing macOS partition:

 # bless --folder /efi/grub --file /efi/grub/grub.efi

## Tips and tricks
## Color Profile
Macs use ICC profiles which can easily be loaded in Arch. The current profile can be shown using ColorSync Utility or System Preferences > Displays > Color. These files correspond to particular models,

*  for MacBook Pro with CoreDuo CPU
*  for MacBook with Core2Duo
*  for MacBook (non-Pro) based on CoreDuo or Core2Duo.
*  for MacBookPro9,2 (Mid-2012)

## Apple Remote
Install and configure . See LIRC.

Make LIRC use  or :

Use irrecord to create a configuration file matching your remote control signals:

 # irrecord -d /dev/usb/hiddev0 -H macmini output_conf_file

Start  and use irw to check if it works.

Alternatively, use the following:

## HFS+ Partitions
## HFS partition sharing
Install  and use fdisk to list the partitions:

The "Unknown" partition is our macOS partition, which is located in . We can use this in our fstab:

It can then be mounted, and the content accessed.

## Bad Superblock Error
This section addresses error message when mounting hfsplus partition:

Since Yosemite, HFS+ partitions are now wrapped a CoreStorage volume. Verify that you have an CoreStorage volume.

HFS+ uses two volume headers, one 1024 bytes into the device and one 1024 from the end of the device. With the HFS+ partition wrapped in the CoreStorage volume the end of the partition is not actually 1024 bytes from the end of the  partition. To fix this you need to specify  when mounting.

To determine  do the following:

# Run  and select your drive
# Select
# Select  and then

Sample output:

What you see now is the output of the HFS partition itself without the CoreStorage volume. Take the size in sectors (622738176 in this example) and multiply by the number of bytes in your logical sector size (512 in this example).

622738176 * 512 = 318841946112

Finally, mount your disk with the  option.

  mount /dev/sdX -t hfsplus -o ro,sizelimit=318841946112

## Disable Journaling
HFS+ partitions are not fully supported by Linux and are mounted as read-only by default. In order to write to an HFS+ partition, the safe way is to disable journaling. This can be accomplished using the macOS Disk Utility. Refer to this Apple support page for more information or try to do it from the command line:

Find your partition:

In this example we will use disk0s3 partition named as Macintosh HD. To know if journaling is activate or not you could execute:

As you can read the journaling is active. To turn off the journaling you could execute:

 # diskutil disableJournal disk0s3

To verify it is done execute the info command again.

If you get noting as output, then journaling is disabled.

However, if you fail to disable journaling. You can change "auto,user,rw,exec" in  to "auto,user,force,rw,exec" and mount it.

## UID synchronization for home sharing
If you want to access your macOS user directories from Linux, write down the UID and GID for the users. macOS begins with the first user's UID at 501 while Arch defaults to 1000.

## In macOS
## Change UID and GID(s)
The default UID and GID on Arch Linux for a user is 1000, adjust the following steps according to your setup.

## Pre-Leopard
# Open NetInfo Manager located in the  folder.
# If not done for you already, enable access to user account transactions by clicking on the closed lock at the bottom of the window, and entering your account password, or root password if you have created a root account.
# Navigate to
# Change the UID value to 1000
# Change the GID value to 1000
# Navigate to , automatically saving the changes you have made so far.

## Leopard
In Leopard, the NetInfo Manager application is not present. A different set of steps is required for UID synchronization:

# Open System Preferences.
# Click on Users & Groups.
# Unlock the pane if not already done so.
# Right-click on the desired user and select Advanced Options.
# Write down the value of the User ID field, you will need it later on. Change both the UID and GID to match the UID and GID of the account to be shared with in Arch.

## Change "Home" permissions
# Open up Terminal in the  folder.

# Enter the following command to reclaim the permission settings of your home folder:

 # find /User/your_user_name -user your_old_UID -exec chown your_user_name:your_user_group {} \;

## In Arch
To synchronize your UID in Arch Linux, you are advised to perform this operation while creating a new user account.
It is therefore recommended that you do this as soon as you install Arch Linux.

 # useradd -m -u -g [gid -G -s [login_shell Now you must substitute Arch's home with macOS's home, by modify entries of . In order to be able to access a macOS user's directory, only the uid and gid need to match (usernames can differ).

## Mute startup chime
The startup chime volume is controlled by the EFI variable SystemAudioVolume-7c436110-ab2a-4bbb-a880-fe41995c9f82. So it can be muted with (as root):

 # chattr -i /sys/firmware/efi/efivars/SystemAudioVolume-7c436110-ab2a-4bbb-a880-fe41995c9f82
 # printf "\x07\x00\x00\x00\x80" > /sys/firmware/efi/efivars/SystemAudioVolume-7c436110-ab2a-4bbb-a880-fe41995c9f82
 # chattr +i /sys/firmware/efi/efivars/SystemAudioVolume-7c436110-ab2a-4bbb-a880-fe41995c9f82

This removes the immutable bit (see File permissions and attributes#File attributes), writes the muted volume level and chime disable bit to the EFI, and re-sets the immutable bit.

Note that if you have not changed the system volume from macOS after resetting the NVRAM/PRAM, this efi variable may not exist. Creating the variable as shown above will mute the chime.

On some older Macs (pre-2010), this may not mute the chime, as it was not yet controlled by an explicit disable bit. Try setting the following value instead:

 # printf "\x07\x00\x00\x00\x00" > /sys/firmware/efi/efivars/SystemAudioVolume-7c436110-ab2a-4bbb-a880-fe41995c9f82

If you wish to restore the startup chime, run the following:

 # chattr -i /sys/firmware/efi/efivars/SystemAudioVolume-7c436110-ab2a-4bbb-a880-fe41995c9f82
 # rm /sys/firmware/efi/efivars/SystemAudioVolume-7c436110-ab2a-4bbb-a880-fe41995c9f82

Alternatively, you can use a macOS install disk to mute the chime. Boot from it, select language, then click Utilities > Terminal, and enter

 # /usr/sbin/nvram SystemAudioVolume=%percentage

## Custom icon in the boot loader
The Mac boot loader supports loading custom icons for each volume it detects. The custom icon must be in the  format, and be located at the root of the volume containing the boot loader, with the file name .

The following example downloads an Arch logo SVG with , converts it to PNG with  and then converts it to an  with :

 $ wget -O /tmp/archlinux.svg https://archlinux.org/logos/archlinux-icon-crystal-64.svg
 $ rsvg-convert -w 128 -h 128 -o /tmp/archlogo.png /tmp/archlinux.svg
 # png2icns /boot/.VolumeIcon.icns /tmp/archlogo.png

Obviously, you can replace the Arch logo with any other icon you like.
