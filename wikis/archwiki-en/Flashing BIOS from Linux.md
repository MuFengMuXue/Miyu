# Flashing BIOS from Linux

This article provides information on using Linux to update the BIOS of a system. Usually, the update program provided by a manufacturer must be executed under Windows. However, various utilities and methods have been published for upgrading a system BIOS under Linux.

In addition to the tools described below, many laptop pages include individualized instructions for a particular model. The instructions sometimes involve bespoke utilities that may even be particular to the upgrade process on a single model. If there is no page for a particular model, it may be useful to look at pages for similar models, as it might be possible to adapt a process for the target model. The HP ENVY m4-1015dx page, for example, includes instructions that may work on a variety of HP models.

## fwupd
fwupd is a simple daemon to allow session software to update device firmware on your local machine.

Large vendors including Dell and Logitech use this way to distribute firmware updates to Linux.

fwupd only supports flashing BIOS updates in UEFI mode.

See fwupd for further information about installation and usage.

## BiosDisk
BiosDisk simplifies the process of flashing your system BIOS under Linux.

## Installation
Install the  package.

## Usage
To use the biosdisk utility to create a BIOS flash image, first download the latest raw BIOS image for your system from your manufacturer's website. Make sure, however, that you always get the BIOS executable and NOT the Windows executable. You then have one of two options: create a ISO or install the image for your boot loader.

* The mkimage action will create a ISO image on the user's hard drive. Usage is the following:

 # biosdisk mkimage option destination /path/to/.exe

* The install action will create the biosdisk image, copy the image file to /boot, and then update the boot loader with an entry for the image. Then all the user has to do is boot the system and select the image to flash the BIOS; this will load the biosdisk image directly from the hard drive and flash the BIOS.

 # biosdisk install option /path/to/.exe

## Flashrom or Flashprog
[https://wiki.flashrom.org/Supported_hardware Flashrom / Flashprog is a utility for identifying, reading, writing, verifying and erasing flash chips. It is designed to flash BIOS/EFI/coreboot/firmware/optionROM images on mainboards, network/graphics/storage controller cards, and various programmer devices. Flashprog is a fork of Flashromcommands should mostly work on both.

## Installation
Install the  /  package.

## Usage
Find out if your motherboard and chipset (internal) is listed in [https://wiki.flashrom.org/Supported_hardware flashrom Supported Hardware or flashprog Supported hardware)
You can also find out if your hardware is supported by issuing the following command

 # flashrom --programmer internal

The above command will tell you your motherboard and chipset. You can then find out if yours is supported by issuing this command:

 # flashrom --programmer internal -L | grep CHIPNAMEfrompreviouscommand

On modern mainboards you probably get more than one rom chip listed. You have to select the chipname you get from the upper command. Then you use the  option to select which rom is affected by the command

 # flashrom --programmer internal -c "CHIPNAME" -r backup_CHIPNAME.bin

Write and verify the new BIOS image (proprietary or Coreboot) on the ROM chip:

 # flashrom --programmer internal -c "CHIPNAME" -w newbios.bin

If you want to flash other flash chips on your mainboard, you will find all options with

 # flashrom

## FreeDOS
Some laptop manufacturers provide a DOS compatible executable to flash the system firmware.
FreeDOS, a free DOS-compatible operating system, is up to the challenge, no need for proprietary DOS versions. So, all you need is a bootable floppy disk image with FreeDOS kernel on it.

## Unetbootin
By far the easiest way to make a bootable FreeDOS USB Stick is using .

You should format a pendrive with FAT16 and flag it as "boot" (you may do this through a GUI with  or ). Then, after mounting the flash drive, select under distribution FreeDOS and your mounted stick. The app will automatically download the image for you and copy it to the drive. Finally, you may copy everything you want to flash there (BIOS, firmwares, etc).

## dosemu
The problem with the official FreeDOS images is the lack of extra space for holding firmware and BIOS update files and programs. The easiest way to create a DOS, bootable FAT drive of arbitrary size under Linux is to mount a FAT drive under dosemu and then make it bootable with the FreeDOS sys command.

For an alternative method, see Gentoo:BIOS Update#FreeDOS environment.

## Pre-built images
Yet another simple solution: FreeDOS pre-built bootable USB flash drive image by Christian Taube. Instructions can be found here.

## Using a FreeDOS-provided Disk Image + USB stick on Linux
As of writing (2017-07-11),  does not support versions of FreeDOS more recent than 1.0 (current version is 1.2). The following procedure worked to upgrade an Inspiron 17-3737 to the A09 BIOS. (Dell offers this as a possibility on their site)

Some notes before starting:

* You can check your current BIOS version with . You might already be at the latest version.
* Ensure that your hardware vendor has verified this method works (use of FreeDOS to run BIOS update .exe)
* Laptop users should not attempt this without AC power
* This is dangerous, and you assume all risk for following this procedure.

Procedure:

# Grab the latest USB installer from the FreeDOS Download Page
#* author note: used the "Full" version on suspicion that it might include more drivers, etc (pure speculation)
# Extract the archive, you get a .img file
# Determine which of  is your USB stick (use )
# Write the image directly to the block device:
#*  (where  is the letter representing your USB stick as a block device, do not write the image to a partition)
# Double-check that the image copying worked:
#*  (you should see a single partition on a DOS disk with the bootable ("boot") flag set)
# Mount the partition, and copy over the .exe used to update your firmware
#* Stay on the safe side and limit the filename to 8 characters (without extension), uppercase
#* Ensure that you verified any checksums provided by your hardware vendor
# Unmount and reboot. Do whatever is needed to boot from the USB drive

Now you will find yourself in the FreeDOS live installation environment.

# Select your language
# You will be prompted to install FreeDOS
#* Select "No - Return to DOS"
# You should see a prompt ()
# Run  and verify that your firmware upgrade tool is present
# Run the executable
#* author note: in the case of the Dell tool, the machine displayed a splash screen and then rebooted. Upon reboot, it started the firmware upgrade automatically, and ran for about 2 minutes with the fan at full speed)
# Once the process specific to your vendor completes, optionally verify through the BIOS setup screen, as well as by running  when you are back in Linux

## Using a FreeDOS-provided Disk Image + USB stick with Windows
The author for this procedure encountered several issues related to mounting the FAT partition type of the USB using the previous method on Linux with dd. This procedure seeks to outline a method to flash the BIOS with FreeDOS, a USB stick and Ruckus on Windows.

Prerequisites:
* Download and install Rufus for Windows. This can be either the full installation or the portable version.
* Download the latest Full USB installer for FreeDOS (v1.2 as of the time of writing).
* Download the latest BIOS update from the vendors' website
* It is assumed that dmidecode is installed on the system

Procedure:
# Extract the contents of the FD12FULL.zip archive, noting the .img file
# Insert a flash drive and flash the FD12FULL.img file using Rufus, leaving all default options
#* Detailed use of Rufus is not covered in this guide. Refer to Rufus' manual or documentation for detailed usage
# Once flashed with Rufus, rename the BIOS file with 8 uppercase characters (not including the extension) and copy it over to the flash drive
# Eject the flash drive and plug it into the laptop.
# Perform whatever steps are necessary to boot from the USB with LEGACY BOOT
#* Author note: For my Dell Laptop, I press F12 for boot options and select 'USB Storage Device' under 'Legacy Options'. I have explicitly enabled legacy boot from within my BIOS, but this option may not be present if the system is only configured to boot with UEFI
# You will be presented with the FreeDOS Installation environment
#* Select preferred language
#* Select 'No - Return to DOS' on the next screen
#* Type dir to view the contents of the USB flash drive
#* To execute the BIOS upgrade file, simply type the filename and press enter
#* Note: My upgrade took   sed -r 's/.*startsector (63'''
}}

Or:

Now you can mount the image:

 # mount -oloop,offset=$((63 * 512)) '''' /mnt

Then you can copy your flash utility onto the filesystem as normal.
Once you are done:

 # umount /mnt

The image can now be copied to a USB stick for booting, or booted as a memdisk as per normal instructions.

## Usage
The OEM Bootdisk version is recommended, as it only includes  and  thus leaving more space for the flash utility and new BIOS image. Download the [https://web.archive.org/web/20190924142014/http://www.fdos.org/bootdisks/autogen/FDOEM.144.gz FreeDOS image and decompress it.

Copy your BIOS flash utility and new BIOS image to the mounted floppy disk image. Load the necessary modules:

 # modprobe -a vfat loop

 shows if the needed file systems are supported. "loop mount" the floppy disk image to a temporary path:

 $ mount --mkdir -t vfat -o loop FDOEM.144 /tmp/floppy

If the mount went without errors, copy the BIOS flash utility and new BIOS image to the mounted floppy disk image. You will probably have to unzip the archive you downloaded from your motherboard vendor site, to get to those two files. For example:

 # cp 75DVSTA2.60 ASRflash.exe /tmp/floppy

Check that the two files were not too big for the floppy:

Unmount the floppy disk image:

 # umount /tmp/floppy

The next step is to burn the floppy image to a CD/DVD-RW media, but in a way that it can be booted afterwards. First create a bootable CD image, and then burn it.

 # genisoimage -o bootcd.iso -b FDOEM.144 FDOEM.144
 # wodim -v bootcd.iso

You may alternatively add your image to the GRUB menu. Install syslinux and copy  and your image to :

 # cp /usr/lib/syslinux/memdisk /boot
 # cp FDOEM.144 /boot/flashbios.img

Now add an entry to :

Or for GRUB2 in :

{{hc|/boot/grub/grub.cfg|
menuentry "Flash BIOS" {
 linux16 /boot/memdisk
 initrd16 /boot/flashbios.img
}
}}

Or for syslinux in :

Finally reboot your machine, making sure the CD drive is first in the boot sequence, and run the BIOS upgrade procedure when the CD boots. If using the GRUB method, choose the new entry on the list, and it should boot into FreeDOS.

## Bootable optical disk emulation
The script Geteltorito.pl will extract the El Torito boot image. It has worked with Lenovo laptops like the X1 Carbon, X200, X220, X230, X260, X395, W540, T450, T450s and P50. It may work for other vendors as well.

## Installation
Install the  package.

## Usage
Get the bios update iso from the vendor support site. Run the geteltorito image extraction:

 $ geteltorito.pl -o .img .iso

Copy the image to an USB flash installation medium:

 # dd if=.img of= bs=512K

Reboot and boot from the USB drive, follow vendor directions.

## Windows PE
If your manufacturer only provides an exe file and you were not successful following the prior advice, you can update your bios creating a Windows PE flash drive and from there flash the bios update as normally.

## Usage
Download a ISO Windows PE to create a bootable drive.

Boot the USB and go to your manufacturer website and download the respective update, and execute normally.

## Vendor specific
## HP
Some HP BIOS, especially the ones available in their business lines (e.g., ProDesk, EliteDesk, and Thin Clients like the T620), provide a firmware upgrade option through both the Startup Menu and the F10 Setup utility.

The correct directory structure for the USB drive is model-specific. To determine the exact requirements for your model:

# Download the BIOS executable from HP's support website using your serial number (selecting Windows as the OS).
# Extract the downloaded executable using, e.g., 7-Zip.
# Among the extracted files, open the `Bios Flash.htm` file in a web browser.
# Look for a section titled "Updating from Computer Setup (F10)" or "Startup Menu / F10 Setup Firmware Update". This section will specify the exact folder structure and file naming convention needed for your specific model.

For newer models like the OmniBook, the required procedure is as follows:
*   The extracted BIOS file (often a `.bin` file) **must be renamed to `firmware.bin`**.
*   This file must be placed on a FAT32 formatted USB drive in one of these two specific folders (try the first one first):
    *   `\HP\DEVFW\`
    *   `\EFI\HP\DEVFW\`
*   The full path on the USB drive will therefore be either `\HP\DEVFW\firmware.bin` or `\EFI\HP\DEVFW\firmware.bin`.

If you cannot find the documentation within the `Bios Flash.htm` file, the following alternative directory structures are also common for other HP models:
1.  Placing the BIOS `*.bin` file (keeping its original name) in the root of the USB drive.
2.  Using a directory structure like `/HP/BIOS/Newest/` with the original `.bin` file.

Procedure:
# Follow the steps above to download and extract the BIOS files. Determine the required directory structure and filename from the `Bios Flash.htm` file. For Business Desktops, rename the file to `firmware.bin` and place it in the `\HP\DEVFW\` folder on your USB drive.
# Create the appropriate directory structure on a FAT32 formatted USB drive and copy the necessary file.
# Unmount the USB drive.
# Attach it to the computer whose BIOS needs to be upgraded.
# Reboot the computer and press  to display the Startup Menu.
# From the Startup Menu, you can either:
    ## Select **"Update System and Supported Device Firmware"** directly for an immediate update, or
    ## Select **"BIOS Setup (F10)"** (or press ), navigate to the "Update System BIOS" menu, and select **"Update System and Supported Device Firmware Using Local Media"**.
# The utility will search the attached media for the firmware file. If found, it will display the current and new version information.
# Follow the on-screen prompts to complete the upgrade. The system will restart afterwards to finalize the update.

For some older models (particularly from 2010-2014), unpacking the executable produces a file ending in .fd that contains both the BIOS and a signature. This file must be extracted into a `.bin` and a `.sig` or `.s12` file. These files then need to be placed on the USB drive in the correct structure. The HP ENVY m4-1015dx page provides specific details for one such model.

If no method seems to work, then either use the FreeDOS method (if HP provides DOS executables) or use a Windows machine to create an HP BIOS Flash Recovery USB.

## ASUS
Modern ASUS motherboards do not require Windows for firmware update. You can update from within the UEFI with the Ez-Flash utility. However, they ask you to update ME before updating bios. The problem is that they do not include Linux update tool in the archiveEven if your bios is at latest version, you need update ME anyway. It is important to avoid hardware problems, such as unable to wake from sleep.

Download the System Tools from [https://winraid.level1techs.com/t/intel-converged-security-management-engine-drivers-firmware-and-tools-2-15/30719 here. For this particular motherboard the latest (v15) version did not work (Unknown PCH platform). As recommended here, using v11 version worked. Extract the Linux executable from the archive ("CSME System Tools v11 r46/FWUpdate/LINUX64/FWUpdLcl") and place it to the folder with the firmware in archive downloaded from Asus site (MEUpdateTool_11.8.80.3746v5_S/FW/). Make the "FWUpdLcl" executable.

Show usage:

Show your current ME version:

Show the ME version of the file in downloaded archive:

Start flashing:

To be able to see new version you need reboot. Now you can see the version applied:

## Lenovo
Some firmware updates are only provided in Windows executable format. This section uses as an example the Lenovo IdeaPad L340-15API firmware. If you try to apply these steps to another system, your mileage may vary. The Lenovo IdeaPad L340-15API only offers a .exe on the Lenovo support site. This renders not just many, but all of the methods in the article futile:

* Wine: while dangerous, the mentioned IdeaPad firmware failed due to a "TDK library" error. More on this below.
* fwupd alone does not work because the firmware is not on the LVFS, even if other entries might be, such as the Secure Boot Forbidden Signatures Database (dbx).
* BiosDisk only works on "BIOS executables" and not our executable. It is also made by Dell, so your mileage could vary with other vendors.
* Flashrom comes with the specific warning not to use it with laptops. Many systems, and the IdeaPad included, are not supported in their hardware list either.
* For FreeDOS to work, the firmware would need to be a DOS executable. If your firmware executable is like that of the IdeaPad discussed, it will not run in FreeDOS at all even with modern Windows executables starting with a DOS header.
*  only works if you have an ISO.
* Windows PE, might also yield incompatibility issues. In particular, the installer might not run because it is checking the operating system for compatibility.

# The installer. The IdeaPad's firmware download comes in an installer format, specifically set up by Inno Setup. Instead of extracting by running the installer with something like Wine, use the  tool:
# We find inside another executable. This inner IdeaPad executable also does not work in FreeDOS or Windows PE. However, note the earlier mentioned TDK library error. TDK refers to the firmware dev kit made by Phoenix Technologies. It was mentioned on the badcaps forum that the executable itself will extract the contents using the  argument. So using Wine, run  Alternatively, using 7-Zip has been reported as working too:
# We find ourselves with more .exe files in this .exe file too. None of them work in FreeDOS or Windows PE. However, note that the firmware itself is in a UEFI capsule update format, suggested in bladecoder's blog.
#*In the extracted files, look for the .cap file. You have located the extracted firmware.
#*Alternatively, some models use an .fd file.
# With the UEFI capsule in hand, the next step is to try to install it manually. Mentioned in that blog, fwupd can help with this. fwupdate is not provided in the  package, but fwupdtool accomplishes the same task. First, identify the device ID of the firmware (Device ID under System Firmware):
# Finding the ID in the devices output, use it with a manual install:
# Reboot when prompted. The screen may go completely black: wait for it to finish installing.
# The UEFI boot entries in NVRAM are cleared after the update. The boot loader files in the EFI system are not touched, so you simply need to recreate your previous UEFI boot entries. First, update your UEFI settings to your previous ones.
# Finally, boot an external boot media and either reinstall your boot loader or use efibootmgr to recreate the UEFI boot entry for your boot loader.

## Acer
Acer firmware updates are very analogous to #Lenovo ones in that the only downloads available are Windows executable files and that the firmware updates are not available on the LVFS either. However, the update image can be extracted from these files and installed using fwupdtool just as well:

# Find the drivers download page by pasting your device model or serial number on this page: https://www.acer.com/us-en/support/drivers-and-manuals
# Expand BIOS/Firmware section and download the ZIP file for the latest version, in our example BIOS_Acer_1.08_A_A.zip
# Unpack it:
# Inside of it, you will find an .exe file such as JH4SH108.exe, we will extract it using :
# In the unpacked folder OutputDir, we should find abobios.bin – this is the UEFI capsule to install
# Then, identify the device ID of the firmware (Device ID under System Firmware):
# Finding the ID in the devices output, use it with a manual install:
# Reboot when prompted. You should see a screen with flashing progress of the Insyde H2OFFT (Flash Firmware Tool) tool. Verify that the BIOS Model Name of old and new BIOS exactly matches up (in this example's case, JH4SH, with new BIOS version V1.08)
# The UEFI boot order in the NVRAM is cleared after the update (aside from Windows Boot Manager, if it was installed). The boot loader files in the EFI system and the boot entries in the NVRAM are not touched, so you simply need to change the boot order list to match what you had before.
# Finally, boot an external boot media and either reinstall your boot loader or use efibootmgr to set the boot order and place your boot loader entry as the first one to boot.
