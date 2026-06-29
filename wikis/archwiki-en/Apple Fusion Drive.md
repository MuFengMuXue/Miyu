# Apple Fusion Drive

Apple uses a RAID alternative called CoreStorage to merge the SSD and HDD into a single logical volume (sold as Fusion). To reinstall macOS to the HDD without using the SSD, allowing the later to be used for Arch Linux, this volume needs to be removed.

## Boot into recovery
The iMacs that come with Fusion also come with a rescue partition that runs itself from RAM (a virtual disk2). This will allow working on the HDD and SSD without them mounted. Power on your iMac, holding down  to enter the recovery environment.

When the recovery has started, start a terminal from the Utilities menu.

## Destroy CoreStorage and prepare new volumes
Find the CoreStorage 'Logical volume group' ID, and take note of the SSD and larger disk (disk0 & 1)

 diskutil cs list

Remove the CoreStorage volume

 diskutil cs delete volumeid

Sometimes you need to unmount a volume or try the above command twice for macOS to actually run it successfuly.

Zero the SSD (if you specify the correct disk this takes around 5 minutes)
This will remove everything, including the partition table, so macOS does not see the disk and will not try to use it during installation.

 diskutil zeroDisk disk1

Erase the HDD (this is faster then zeroDisk and creates a new HFS+ volume for macOS)

 diskutil eraseDisk JHFS+ Macintosh disk0

## Install macOS on the HDD
Quit the terminal and start the macOS installer. Do not use the GUI-based Disk Utility at this point, it will show your disks as errored in red and will want to fix them for you. This will recreate the CoreStorage volume even if you choose not to 'fix' anything, undoing everything we have done so far. The macOS installer should show you 1 disk, which is the Journaled HFS+ volume on the HDD.

Proceed by installing macOS on the HDD. Optionally, use the Disk Utility on the newly installed OS to resize the macOS partition and allocate some space for Linux to use besides the SSD. Now boot the Arch Linux USB stick by holding  while booting your iMac. This will show you a boot menu where you can select the USB drive for booting.

## Proceed installing Arch Linux
Follow the Installation guide, remember to mount the EFI system partition (the first partition of the HDD, e.g. ) to .

When rebooting, hold  to show the internal boot loader so you can select your new install. To change the default boot option to Arch Linux, you need to "bless" the newly created UEFI file. It is suggested to rename the  to , then run the following command from macOS, after mounting the EFI system partition:

 # bless --device=/dev/disk1s2 --file=/Volumes/efi/EFI/BOOT/BOOTX64.EFI --setBoot

Make sure you specify a partition on the SSD as ! Otherwise macOS will boot EFI from the partition, but your boot loader will not find the SSD (where the actual install is) and you will end up in rescue mode.

To know the value to put in  you can print a list of the partitions with the  command, and find your EFI partition. This utility is available in the MacOS recovery too.
