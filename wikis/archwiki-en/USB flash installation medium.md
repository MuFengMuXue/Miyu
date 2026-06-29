# USB flash installation medium

This page discusses various multi-platform methods on how to create an Arch Linux Installer USB drive (also referred to as "flash drive", "USB stick", "USB key", etc) for booting in BIOS and UEFI systems. The result will be a live USB system that can be used for installing Arch Linux, system maintenance or for recovery purposes, and that, because of using Overlayfs for , will discard all changes once the computer shuts down.

If you would like to run a full install of Arch Linux from a USB drive (i.e. with persistent settings), see Install Arch Linux on a removable medium. If you would like to use your bootable Arch Linux USB stick as a rescue USB, see chroot.

Before following any of these steps, download the ISO from https://archlinux.org/download/ and verify its integrity.

## Using the ISO as is (BIOS and UEFI)
## In GNU/Linux
## Basic command line utilities
This method is recommended due to its simplicity and universal availability, since these tools are part of  (pulled in by the  meta package).

Find out the name of your USB drive with  and check with  to make sure that it is not mounted.

Run one of the following commands, replacing  with your drive, e.g. .

* :
* :
* dd:
* :
* :

See and [https://www.vidarholen.net/contents/blog/?p=479 for a comparison and perspective on the use of those tools and why dd may be the least adapted one, and note that cat (with  system call support) is faster than dd.

## GNOME Disk Utility
Linux distributions running GNOME can easily make a live USB through  and .  Simply right-click on the .iso file, and select Open With Disk Image Writer.  When GNOME Disk Utility opens, specify the flash drive from the Destination drop-down menu and click Start Restoring.

## KDE ISO Image Writer
KDE ISO Image Writer can be downloaded via . It can auto-detect the USB-drive and you need to manually select a ISO file. It is recommended to use .sig file to signature but it can be skipped by clicking "create".

## MultiWriter
 is a simple GTK3 based graphical tool to write an ISO file to one or multiple USB devices at once.

## Popsicle
Popsicle is a tool made for flashing ISO files to multiple USB devices in parallel by the PopOS development team. It is written in Rust and uses GTK. It is available as .

## SUSE Studio ImageWriter
SUSE Studio ImageWriter is a Qt based tool made by the openSUSE development team. It is available as .

## USBImager
USBImager is a multiplatform graphical application that writes and verifies compressed disk images to USB drives, and creates backups. It is available as .

## xorriso-dd-target
xorriso-dd-target (from ) is a shell script which attempts to reduce the risk of overwriting the wrong storage device. Its safest mode is named . For example, to use it as a regular user who can elevate to root using sudo:

 $ xorriso-dd-target -with_sudo -plug_test -DO_WRITE -image_file archlinux-version-x86_64.iso

See  for details.

## In Windows
## Cygwin
Make sure your Cygwin installation contains the  package.

Place your image file in your home directory:

 C:\cygwin\home\User\

Run cygwin as administrator (required for cygwin to access hardware). To write to your USB drive use the following command:

 dd if=archlinux-version-x86_64.iso of=\\.\x: bs=4M

where  is the path to the iso image file within the  directory and  is your USB flash drive where  is the windows designated letter, e.g. .

On Cygwin 6.0, find out the correct partition with:

 cat /proc/partitions

and write the ISO image with the information from the output. Example:

 dd if=archlinux-version-x86_64.iso of=/dev/sdb bs=4M

## dd for Windows
A GPL licensed dd version for Windows is available at http://www.chrysocome.net/dd. The advantage of this over Cygwin is a smaller download. Use it as shown in instructions for Cygwin above.

To begin, download the latest version of dd for Windows. Once downloaded, extract the archive's contents into the  directory or elsewhere.

Now, launch your Command Prompt as an administrator. Next, change directory () into the  directory.

If your Arch Linux ISO is elsewhere you may need to state the full path, for convenience you may wish to put the Arch Linux ISO into the same folder as the dd executable. The basic format of the command will look like this.

 # dd if=archlinux-version-x86_64.iso od=\\.\x: bs=4M

## flashnul
flashnul is an utility to verify the functionality and maintenance of Flash-Memory (USB-Flash, IDE-Flash, SecureDigital, MMC, MemoryStick, SmartMedia, XD, CompactFlash etc).

From a command prompt, invoke flashnul with , and determine which device index is your USB drive, e.g.:

When you have determined which device is the correct one, you can write the image to your drive, by invoking flashnul with the device index, , and the path to your image, e.g:

 C:\>flashnul E: -L path\to\archlinux-version-x86_64.iso

As long as you are really sure you want to write the data, type yes, then wait a bit for it to write. If you get an access denied error, close any Explorer windows you have open.

## KDE ISO Image Writer
KDE ISO Image Writer can be downloaded as .exe file at isoimagewriter. It can auto-detect the USB-drive and you need to manually select a ISO file. It is recommended to use .sig file to signature but it can be skipped by clicking "create".

## Rufus
Rufus is a multi-purpose USB ISO writer. It provides a graphical user interface and does not care if the drive is properly formatted or not.

Simply select the Arch Linux ISO, the USB drive you want to create the bootable Arch Linux onto and click START.

## USBImager
USBImager is a multiplatform graphical application that writes and verifies compressed disk images to USB drives, and creates backups.

## USBwriter
This method does not require any workaround and is as straightforward as  under Linux. Just download the Arch Linux ISO, and with local administrator rights use the USBwriter utility to write to your USB flash memory.

## win32diskimager
win32diskimager is another graphical tool for writing images to USB sticks or SD/CF cards from Windows. Select your ISO image and the target USB drive letter (you may have to format it first to assign it a drive letter), and click Write.

## In macOS
## macOS dd
First, you need to identify the USB device. Open  and list all storage devices with the command:

 $ diskutil list

Your USB device will appear as something like . Verify that this is the device you want to erase by checking its name and size and then use its identifier for the commands below instead of .

A USB device is normally auto-mounted in macOS, and you have to unmount (not eject) it before block-writing to it with . In Terminal, do:

 $ diskutil unmountDisk /dev/diskX

Now copy the ISO image file to the device:

 # dd if=path/to/archlinux-version-x86_64.iso of=/dev/rdiskX bs=1m

This command will run silently. To view progress, send SIGINFO by pressing . Note  here should not include the  suffix, or else the USB device will only be bootable in UEFI mode and not legacy. After completion, macOS may complain that The disk you inserted was not readable by this computer. Select Ignore. The USB device will be bootable.

## USBImager
USBImager is a multiplatform graphical application that writes and verifies compressed disk images to USB drives, and creates backups.

## In Android
## EtchDroid
EtchDroid is a OS image flasher for Android. It works without root permissions since Android 5. Check the upstream GitHub if you have issue.

To create an Arch Linux installer, download the ISO image file on your Android device. Plug the USB drive to your device, using a USB-OTG adapter if needed. Open EtchDroid, select Flash raw image, select your Arch ISO, then select your USB drive. Grant the USB API permission and confirm.

Keep your phone on a table while it is writing the image: a lot of USB-OTG adapters are a bit wobbly and you might unplug it by mistake.

## Using manual formatting
These methods keep the flash drive usable for data storage. For one-partition layouts, extra data can be written to the same partition the ISO is installed on. This is the best layout for compatibility with other operating systems. Alternatively, the ISO can be installed in a specific partition within a partitioned device without altering other partitions, and data can be stored on these other partitions.

## UEFI only
For UEFI-only booting, it is enough to extract the ISO contents onto a FAT-formatted USB flash drive.

It does not require creating a EFI system partition on the drive as all UEFI will happily boot any FAT volume from USB flash drives. The most compatible setup would be using the MBR partition table with a single active (bootable) primary partition of type  "W95 FAT32 (LBA)".==== In GNU/Linux ====

This method extracts files from the ISO image to a USB flash drive.

# If not done yet, create a partition table on  and a partition () on the device.
# If not done yet, format the partition to FAT32:
# Mount the file system:
# Extract the ISO image to the mounted file system:
# Unmount the file system.

## In Windows
This method copies files from the ISO image to a USB flash drive.

# Partition the USB flash drive and format it to FAT32.
# Right click on  and select Mount.
# Navigate to the newly created DVD drive and copy all files and folders to the USB flash drive.
# When done copying, right click on the DVD drive and select Eject.
# Eject the USB flash drive.

## In macOS
Neither DiskImageMounter nor Disk Utility can mount isohybrid ISOs, but since macOS ships with libarchive, the ISO can simply be extracted onto the flash drive using bsdtar.

# If not done yet, partition the USB flash drive and format the partition to FAT32 using Disk Utility.
# Mount the volume.
# Open the Terminal application and use bsdtar to extract the ISO image to the mounted file system:
# When done, unmount and eject the USB flash drive.

## BIOS and UEFI
This method is more complicated, but it is the most compatible. It is necessary for booting on very old computers.

## In GNU/Linux
* If not done yet, create a partition table on .
* If not done yet, create a partition on the device. The partition  must be formatted to FAT32 (to enable compatibility with [https://uefi.org/specs/UEFI/2.11/13_Protocols_Media_Access.html#file-system-format-1 all UEFI implementations).
* Mount the FAT32 file system located in the USB flash device and extract the contents of the ISO image to it. For example:

 # mount /dev/disk/by-id/usb-My_flash_drive-partn /mnt
 # bsdtar -x -f archlinux-version-x86_64.iso -C /mnt

Syslinux files for BIOS systems are already copied to . Unmount the FAT file system, install the  and  packages and run the following commands to make the partition bootable:

 # umount /mnt
 # syslinux --directory boot/syslinux --install /dev/disk/by-id/usb-My_flash_drive-partn
 # dd bs=440 count=1 conv=notrunc if=/usr/lib/syslinux/bios/mbr.bin of=/dev/disk/by-id/usb-My_flash_drive

## In Windows
* Partition and format the USB drive using Rufus USB partitioner. Select partition scheme option as MBR for BIOS and UEFI and File system as FAT32. Uncheck "Create a bootable disk using ISO image" and "Create extended label and icon files" options.
* Extract the ISO (similar to extracting ZIP archive) to the USB flash drive using 7-Zip.
* Download official Syslinux 6.xx binaries (zip file) from https://www.kernel.org/pub/linux/utils/boot/syslinux/ and extract it. The version of Syslinux should be the same version used in the ISO image.

* Run the following command (in Windows cmd prompt, as admin):

 > cd bios\
 > for /r %Y in (*.c32) do copy "%Y" "X:\boot\syslinux\" /y
 > copy mbr\*.bin X:\boot\syslinux\ /y

* Install Syslinux to the USB by running (use  for x64 Windows):

 > cd bios\
 > win32\syslinux.exe -d /boot/syslinux -i -a -m X:

## BIOS only
## In GNU/Linux
## Making a USB-ZIP drive
For some old BIOS systems, only booting from USB-ZIP drives is supported. This method allows you to still boot from a USB hard drive.

* Install  and .
* Find your USB drive with .
* Type . This will take a while.

From here continue with the manual formatting method. The partition will be  due to the way ZIP drives work.

## Using a multiboot USB drive
This allows booting multiple ISOs from a single USB device, including the archiso. Updating an existing USB drive to a more recent ISO is simpler than for most other methods.

## In GNU/Linux
See Multiboot USB drive.

## In Windows: using Syslinux and memdisk
This method uses Syslinux and a Ramdisk (MEMDISK) to load the entire Arch Linux ISO image into RAM. Since this will be running entirely from system memory, you will need to make sure the system you will be installing this on has an adequate amount. A minimum amount of RAM between 500 MB and 1 GB should suffice for a MEMDISK based, Arch Linux install.

For more information on Arch Linux system requirements as well as those for MEMDISK see the Installation guide and here. For reference, here is the preceding forum thread.

## Preparing the USB flash drive
Begin by formatting the USB flash drive as FAT32. Then create the following folders on the newly formatted drive.

*
**
**

## Copy the needed files to the USB flash drive
Next copy the ISO that you would like to boot to the  folder. After that, extract from the following files from the latest release of  from here and copy them into the following folders:

*  to the Desktop or Downloads folder on your system.
*  to the  folder on your USB flash drive.

## Create the configuration file
After copying the needed files, navigate to the USB flash drive,  and create a  file.

For more information see the Syslinux article.

## Final steps
Finally, create a  file where  is located and run it ("Run as administrator" if you are on Vista or Windows 7):

## Inadvisable methods
## etcher
etcher contains analytics and first-party advertising. See [https://github.com/balena-io/etcher/blob/37769efbeda0abe7993d95e2b2aea2f461edd307/lib/gui/app/pages/main/MainPage.tsx#L151 and === UNetbootin ===

* UNetbootin does not write the ISO as-is which breaks BIOS booting due to the discrepancy in syslinux versions.
* The Arch Linux installation image's boot loaders expect the ISO contents to reside on volume with a year and month label (). UNetbootin does not update the file system label, nor does it correct the boot loader configuration.

## Universal USB Installer
* The download page contains fake Download buttons that may contain malware.
* Universal USB Installer does not write the ISO as-is which breaks BIOS booting due to the discrepancy in syslinux versions. See [https://bbs.archlinux.org/viewtopic.php?pid=1344629.
* The Arch Linux installation image's boot loaders expect the ISO contents to reside on volume with a year and month label (). Universal USB Installer does not update the file system label, nor does it correct the boot loader configuration.

## Tips and tricks
## Add an additional data partition to the drive
There are two ways to add an additional (third) partition to a drive prepared using #Using the ISO as is (BIOS and UEFI).

# By creating a file system image of a desired size and attaching to the ISO (before writing the ISO to the USB flash drive). See Install Arch Linux via SSH#Using a single USB flash drive for an example.
# By using fdisk to edit the drive's MBR partition table without touching the ISO 9660 or invalid GPT structures. This will destroy the backup GPT header in the invalid GPT, but that should not matter.

To edit the MBR partition table on the drive, run:

 # fdisk -t mbr --wipe never /dev/disk/by-id/usb-My_flash_drive

Use the  command to create a new partition (leave the default values for the first and last sectors if it should span all available free size). If you want to access it in other operating systems, change the MBR partition type ID using the  command (e.g. to  "W95 FAT32 (LBA)" or  "HPFS/NTFS/exFAT"). Write the changes to disk and exit via the  command.

After partitioning, create a file system on the new partition ().

## Troubleshooting
## Device does not show up
If you get the  error due to  not mounting, try renaming your USB medium to  so Arch can find it. (e.g. For , use ).

## Failed to set up loop devices: No such file or directory
If you get , try using a USB 2.0 port. For example, some USB 3.0 ports through USB hubs do not work.

## Other errors
If you get other errors, try using another USB device. There are multiple scenarios in which it solved all issues.
