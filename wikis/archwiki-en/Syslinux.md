# Syslinux

Syslinux is a collection of boot loaders capable of booting from drives, CDs, and over the network via PXE.

## Supported file systems
Some of the supported file systems are FAT, NTFS, ext2, ext3, ext4, XFS, UFS/FFS, and uncompressed single-device Btrfs.

## Installation
Install the  package.

BIOS booting will also require the  package for BIOS/GPT setups and  if your  partition is FAT-formatted.

UEFI booting requires installing the  package.

## Installing the Syslinux boot loader
Installing the package is not the same as installing the boot loader. After installing the relevant package(s), the boot loader code itself needs to be installed (to the adequate area, usually the VBR or ESP) so to be able to boot the system; the following sections provide alternative instructions depending on the characteristics of your particular system.

## BIOS systems
Syslinux boot process on BIOS happens in stages:

;Stage 1 - Part 1 - Load MBR : At boot, the BIOS loads the 440 byte MBR boot code at the start of the disk ( or ).
;Stage 1 - Part 2 - Search active partition : The Stage 1 MBR boot code looks for the partition that is marked as active (boot flag in MBR disks). Let us assume this is the  partition, for example.
;Stage 2 - Part 1 - Execute volume boot record : The Stage 1 MBR boot code executes the Volume Boot Record (VBR) of the  partition. In the case of Syslinux, the VBR boot code is the starting sector of  which is created by the  command. Note that  is not the same as .
;Stage 2 - Part 2 - Execute  : The VBR will load the rest of . The sector location of  should not change, otherwise syslinux will not boot.
;Stage 3 - Load  : The  will load the  (core module) that contains the rest of the core part of syslinux that could not be fit into  (due to file-size constraints). The  file should be present in every Syslinux installation and should match the version of  installed in the partition. Otherwise Syslinux will fail to boot. See https://bugzilla.syslinux.org/show_bug.cgi?id=7 for more info.
;Stage 4 - Search and Load configuration file : Once Syslinux is fully loaded, it looks for  (or  in some cases) and loads it if it is found. If no configuration file is found, you will be dropped to a Syslinux  prompt. This step and the rest of non-core parts of Syslinux ( modules, excluding  and ) require  (library) modules to be present (https://wiki.syslinux.org/wiki/index.php/Common_Problems#ELF). The  library modules and non-core  modules should match the version of  installed in the partition.

## Automatically
After executing the  script, do not forget to edit  by following #Configuration and #Kernel parameters.

The  script will install the boot loader code (usually to the VBR), copy  modules to , set the boot flag, install the boot code in the MBR and copy  to . It can handle MBR and GPT disks along with software RAID:

If you use a separate boot partition, make sure that it is mounted. Check with ; if you do not see a  mountpoint, mount it before you go any further.

Run  with flags:  (install the files),  (mark the partition active with the boot flag),  (install the MBR boot code):  If this command fails with Syslinux BIOS install failed, the problem is likely that the  binary could not find the partition containing :

This can happen, for example, when upgrading from LILO which, while booting a current custom kernel, turned a kernel command line parameter of say  into its numeric equivalent , as evidenced by  and the output of the  command. Remedy the situation by either continuing with the manual install described below while specifying  to , or simply by first rebooting into a stock Arch Linux kernel; its use of an initramfs avoids the problem.

Now is the time to edit  by following #Configuration and #Kernel parameters.

## Manually
Your boot partition, on which you plan to install Syslinux, must contain a FAT, ext2, ext3, ext4, or Btrfs file system. You do not have to install it on the root directory of a file system, e.g., with device  mounted on . For example, you can install Syslinux in the  subdirectory:

 # mkdir /boot/syslinux

Copy all  files from  to  if you desire to use any menus or configurations other than a basic boot prompt. Do not symlink them.

 # cp /usr/lib/syslinux/bios/*.c32 /boot/syslinux/

Now install the boot loader. For FAT, ext2/3/4, or btrfs boot partition use extlinux, where the device has been mounted:

 # extlinux --install /boot/syslinux

Alternatively, for a FAT boot partition use syslinux, where the device is unmounted:

 # syslinux --directory syslinux --install /dev/sda1

After this, proceed to install the Syslinux bootstrap code appropriate for the partition table:

*  will be installed for an #MBR partition table, or
*  will be installed for a #GUID partition table

as described in the next sections.

See Master Boot Record for further general information.

## MBR partition table
For an MBR partition table, ensure your boot partition is marked as "active" in your partition table (the "boot" flag is set). Applications capable of doing this include fdisk and parted. It should look like this:

Install the MBR:

 # dd bs=440 count=1 conv=notrunc if=/usr/lib/syslinux/bios/mbr.bin of=/dev/sda

An alternative MBR which Syslinux provides is: . This MBR does not scan for bootable partitions; instead, the last byte of the MBR is set to a value indicating which partition to boot from. Here is an example of how  can be copied into position:

 # printf '\x5' | cat /usr/lib/syslinux/bios/altmbr.bin - | dd bs=440 count=1 conv=notrunc iflag=fullblock of=/dev/sda

In this case, a single byte of value 5 (hexadecimal) is appended to the contents of  and the resulting 440 bytes are written to the MBR on device . Syslinux was installed on the first logical partition () of the disk.

## GUID partition table
For a GPT, ensure that attribute bit 2 "Legacy BIOS bootable" is set for the  partition. For Parted it can be set using the "legacy_boot" flag. Using sgdisk the command to set the attribute is:

 # sgdisk /dev/sda --attributes=1:set:2

This will set the attribute "legacy BIOS bootable" on partition 1 of . To check:

Install the MBR:

 # dd bs=440 count=1 conv=notrunc if=/usr/lib/syslinux/bios/gptmbr.bin of=/dev/sda

## UEFI systems
## Limitations of UEFI Syslinux
* Using  to edit kernel parameters in UEFI Syslinux menu might lead to garbled display (text on top of one another). Bug report: * UEFI Syslinux does not support chainloading other EFI applications like  or . Enhancement request: [https://bugzilla.syslinux.org/show_bug.cgi?id=17
* In some cases, UEFI Syslinux might not boot in some Virtual Machines like QEMU/OVMF or VirtualBox or some VMware products/versions and in some UEFI emulation environments like DUET. A Syslinux contributor has confirmed no such issues present on VMware Workstation 10.0.2 and Syslinux-6.02 or later. Bug reports: [https://bugzilla.syslinux.org/show_bug.cgi?id=23 and * Memdisk is not available for UEFI. Enhancement request: [https://bugzilla.syslinux.org/show_bug.cgi?id=30
* Syslinux uses the deprecated EFI handover protocol for UEFI booting. Officially supported kernels are not affected since they are built with . Booting kernels built without it will fail, see .
* Mixed mode booting (booting a x86_64 kernel from IA32 syslinux) may not work.* No proper Secure Boot support.[https://www.rodsbooks.com/efi-bootloaders/syslinux.html

## Deployment
Setup Syslinux in the EFI system partition as follows.

Copy Syslinux files to the ESP:

 # mkdir -p esp/EFI/syslinux
 # cp -r /usr/lib/syslinux/efi64/* esp/EFI/syslinux

Create a UEFI boot entry for Syslinux using efibootmgr:

 # efibootmgr --create --disk /dev/sdX --part Y --loader /EFI/syslinux/syslinux.efi --label "Syslinux" --unicode

where  is the EFI system partition containing the boot loader.

Create or edit  by following #Configuration.

## Configuration
The Syslinux configuration file, , should be created in the same directory where you installed Syslinux. In our case,  for BIOS systems and  for UEFI systems.

The boot loader will look for either  (preferred) or

## Examples
## Boot prompt
This is a simple configuration file that will show a  prompt and will automatically boot after 5 seconds. If you want to boot directly without seeing a prompt, set  to .

Configuration:

## Text boot menu
Syslinux also allows you to use a boot menu. To use it, copy the  and  modules to your Syslinux directory:

 # cp /usr/lib/syslinux/bios/{menu,libutil}.c32 /boot/syslinux/

Since version 5.00, additional  library modules are frequently needed too. See the Syslinux wiki for the module dependency tree.

Configuration:

For more details about the menu system, see the Syslinux wiki.

## Graphical boot menu
Syslinux also allows you to use a graphical boot menu. To use it, copy the  COM32 module to your Syslinux folder:

 # cp /usr/lib/syslinux/bios/vesamenu.c32 /boot/syslinux/

Since version 5.00, additional  library modules are frequently needed too. See the Syslinux wiki for the module dependency tree.

This configuration uses the same menu design as the Arch Install CD, its configuration can be found at gitlab.archlinux.org. The Arch Linux background image can be downloaded from there, too. Copy the image to .

Configuration:

Since Syslinux 3.84,  supports the  directive.
To use it, insert  into your configuration for a 1440x900 resolution.
However, the background picture has to have exactly the right resolution, as Syslinux will otherwise refuse to load the menu.

To center the menu and adjust resolution, use ,  and  where  is a positive number. The default values are both  which is the upper-left hand corner of your monitor. Conversely, a negative number starts from the opposite end of the screen (e.g.  would be 4 rows from the bottom of the screen).

To move the menu to the center, add or edit these values:

VESA standards are commonly a maximum of 25 rows and 80 columns, so going higher than those values might move the menu off the screen, potentially requiring editing from a rescue CD.

## Kernel parameters
The kernel parameters are set by using the  directive in :
for each  entry, a maximum of one APPEND line is accepted (i.e. spanning multiple lines is not valid).

It is recommended to make the following changes for the "fallback" entry as well.

In the simplest case, the value of the  parameter needs to be replaced; see Persistent block device naming for supported methods.

 APPEND root=UUID=xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx rw

Change  to point to the correct root volume.

If you use dm-crypt encryption change the  line to use your encrypted volume:

 APPEND root=/dev/mapper/name cryptdevice=UUID=YYYYYYYY-YYYY-YYYY-YYYY-YYYYYYYYYYYY:name rw

If booting a btrfs subvolume, amend the  line with . For example, where  has been mounted as a btrfs subvolume called 'ROOT' (e.g. ), then the  line would need to be modified as follows:

 APPEND root=UUID=xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx rw rootflags=subvol=ROOT

A failure to do so will otherwise result in the following error message:

## Auto boot
If you do not want to see the Syslinux menu at all, use the #Boot prompt, and set  to  and comment out any  menu entries. Setting the  variable to  might also be a good idea. Make sure there is a  set in your . Holding either  or , or setting either  or , during boot will allow for options other than default to be used.
See the upstream wiki for additional alternatives.

## Security
Syslinux has two levels of boot loader security: a menu master password, and a per-menu-item password. In , use

 MENU MASTER PASSWD passwd

to set a master boot loader password, and

 MENU PASSWD passwd

within a  block to password-protect individual boot items.

The passwd can be either a cleartext password or hashed: see official documentation.

## Chainloading
Syslinux BIOS cannot directly chainload files located on other partitions; however,  can boot a partition boot sector (VBR) or another disk's MBR.

## Chainloading a partition's VBR
If you want to chainload other operating systems (such as Windows) or boot loaders, copy the  module to the Syslinux directory (additional  library modules might be needed too; for details, see the instructions in the previous section). Then create a section in the configuration file:

 is the third partition on the first BIOS drive - drives are counted from zero, but partitions are counted from one.

## Chainloading a disk's MBR
If you are unsure about which drive your BIOS thinks is "first", you can instead use the MBR identifier, or if you are using GPT, the filesystem labels. To use the MBR identifier, run the command

replacing  with the drive you wish to chainload. Using the returned hexadecimal number,  in this case, the syntax in  is:

For more details about chainloading, see the Syslinux wiki.

## Chainloading other boot loaders
If you have GRUB installed on the same partition, you can chainload it by using:

Alternatively, it is also possible to load GRUB as a linux kernel by prepending  to . The file  is part of  and can be found in .

This may be required for booting from ISO images.

## Chainloading other Linux systems
Chainloading another boot loader such as Windows' is pretty obvious, as there is a definite boot loader to chain to. But with Syslinux, it is only able to load files residing on the same partition as the configuration file. Thus, if you have another version of Linux on a separate partition, without a shared , it becomes necessary to employ EXTLINUX rather than the other OS's default boot loader (eg. GRUB2). Essentially, EXTLINUX can be installed on the partition superblock/VBR and be called as a separate boot loader right from the MBR installed by Syslinux. EXTLINUX is part of The Syslinux Project and is included with the  package.

The following instructions assume you have Syslinux installed already. These instructions will also assume that the typical Arch Linux configuration path of  is being used and the chainloaded system's  is on .

From a booted Linux (likely the partition that Syslinux is set up to boot), mount the other system's root partition to your desired mount point. In this example this will be . Also, if a separate  partition is used on the second operating system, that will also need to be mounted. The example assumes this is .

 # mount /dev/sda3 /mnt
 # mount /dev/sda2 /mnt/boot (only necessary for separate /boot)

Install EXTLINUX to the partition VBR, and copy necessary  files

 # extlinux -i /mnt/boot/syslinux/ (first create the directory if necessary)
 # cp /usr/lib/syslinux/bios/*.c32 /mnt/boot/syslinux

Create . You can use the other Linux boot loader menu file for reference. Below is an example:

And then add an entry to your main syslinux.cfg

Note that the other Linux entry in  will need to be edited each time you update this OS's kernel unless it has symlinks to its latest kernel and initramfs in . Since we are booting the kernel directly and not chainloading the other OS default boot loader.

## Using memtest
Install .

Use this  section to launch memtest:

## HDT
HDT (Hardware Detection Tool) displays hardware information. Like before, the  file has to be copied from . Additional  library modules might be needed too.
For PCI info, copy  to  and add the following to your configuration file:

## Reboot and power off
Use the following sections to reboot or power off your machine:

## Clear menu
To clear the screen when exiting the menu, add the following line:

## Keyboard layout
If you often have to edit your boot command with diverse parameters in the Syslinux boot prompt, then you might want to remap your keyboard layout. This allows you to enter "=", "/" and other characters easily on a non-US keyboard.

To create a compatible keymap (e.g. a german one) run:

 # keytab-lilo /usr/share/kbd/keymaps/i386/qwerty/us.map.gz /usr/share/kbd/keymaps/i386/qwertz/de.map.gz > /boot/syslinux/de.ktl

Now edit  and add:

See the Syslinux wiki for more details.

## Hiding the menu
Use the option:

to hide the menu while displaying only the timeout. Press any key to bring up the menu.

## PXELINUX
PXELINUX is provided by the  package.

For BIOS clients, copy the  and  to the boot directory of the client.

 # cp /usr/lib/syslinux/bios/lpxelinux.0 "TFTP_root/boot/"
 # cp /usr/lib/syslinux/bios/ldlinux.c32 "TFTP_root/boot/"
 # mkdir "TFTP_root/boot/pxelinux.cfg"

We also created the  directory, which is where PXELINUX searches for configuration files by default. Because we do not want to discriminate between different host MACs, we then create the  configuration.

Or if you are using NBD, use the following append line:

 APPEND ro initrd=initramfs-linux.img ip=:::::eth0:dhcp nbd_host=10.0.0.1 nbd_port=10809 nbd_name=arch root=/dev/nbd0

PXELINUX uses the same configuration syntax as SYSLINUX; refer to the upstream documentation for more information.

The kernel and initramfs will be transferred via TFTP, so the paths to those are going to be relative to the TFTP root. Otherwise, the root filesystem is going to be the NFS mount itself, so those are relative to the root of the NFS server.

To actually load PXELINUX, replace  in  with .

## Booting ISO9660 image files with memdisk
Syslinux supports booting from ISO images directly using the memdisk module, see Multiboot USB drive#Using Syslinux and memdisk for examples.

## Serial console
See Working with the serial console#Syslinux.

## Boot another OS once
It is possible to temporarily change the default Syslinux action and boot another label only during the next boot. The following command shows how to boot the  label once:

 # extlinux -o archfallback /boot/syslinux

During the next boot, the specified label will be booted without any Syslinux prompt showing up. The default Syslinux boot behaviour will be restored on the next reboot.

## Troubleshooting
## Failed to load ldlinux
An error message such as "Failed to load ldlinux.c32" during the initial boot can be triggered by many diverse reasons.
One potential reason could be a change in file system tools or in a file system structure, depending on its own version.

See also (the whole page might be relevant for troubleshooting too).

## Using the Syslinux prompt
You can type in the  name of the entry that you want to boot (as per your ). If you used the example configurations, just type:

 boot: arch

If you get an error that the configuration file could not be loaded, you can pass your needed boot parameters, e.g.:

 boot: ../vmlinuz-linux root=UUID=xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx rw initrd=../initramfs-linux.img

If you do not have access to  in ramfs, and therefore temporarily unable to boot the kernel again,

# Create a temporary directory, in order to mount your root partition (if it does not exist already):
# Mount  under  (in case  is on the same partition, otherwise you will need to mount them both):
# Edit  again to suit your needs and save file.
# Reboot.

## fsck fails on root partition
In the case of a badly corrupted root partition (in which the journal is damaged), in the ramfs emergency shell, mount the root file system:

 # mount /dev/root partition /new_root

And grab the tune2fs binary from the root partition (it is not included in Syslinux):

 # cp /new_root/sbin/tune2fs /sbin/

Follow the instructions at ext2fs: no external journal to create a new journal for the root partition.

## No Default or UI found on some computers
Certain motherboard manufacturers have less compatibility for booting from USB devices than others. While an ext4 formatted USB drive may boot on a more recent computer, some computers may hang if the boot partition containing the kernel and initramfs are not on a FAT16 partition. To prevent an older machine from loading  and failing to read , create a partition (≤ 2 GB) and format to FAT16 using :

 # mkfs.fat -F 16 /dev/sda1

then install and configure Syslinux.

## Missing operating system
* Check that you have installed  for GPT and  for MBR partition table. A "Missing operating system" message comes from  while  would show a "Missing OS" message.
* Check whether the partition that contains  has the "boot" flag enabled.
* Check whether the first partition at the boot device starts at sector 1 rather than sector 63 or 2048. Check this with . If it starts at sector 1, you can move the partition(s) with  from a rescue disk. Or, if you have a separate boot partition, you can back up  with

 # cp -a /boot /boot.bak

and then boot up with the Arch install disk. Next, use  to delete the  partition, and recreate it. This time it should begin at the proper sector, 63. Now mount your partitions and  into your mounted system, as described in the installation guide. Restore  with the command

 # cp -a /boot.bak/ /boot/

Check if  is correct, run:

 # syslinux-install_update -iam

and reboot.

You will also get this error if you are trying to boot from an md RAID 1 array and created the array with a too new version of the metadata that Syslinux does not understand. As of August 2013 by default mdadm will create an array with version 1.2 metadata, but Syslinux does not understand metadata newer than 1.0. If this is the case you will need to recreate your RAID array using the  flag to mdadm.

## Windows boots up, ignoring Syslinux
Solution: Make sure the partition that contains  has the boot flag enabled. Also, make sure the boot flag is not enabled on the Windows partition. See the installation section above.

The MBR that comes with Syslinux looks for the first active partition that has the boot flag set. The Windows partition was likely found first and had the boot flag set. If you wanted, you could use the MBR that Windows or MS-DOS  provides.

## Menu entries do nothing
You select a menu entry and it does nothing, it just "refreshes" the menu. This usually means that you have an error in your  file. Hit  to edit your boot parameters. Alternatively, press  and type in the  of your boot entry (e.g. arch). Another cause could be that you do not have a kernel installed. Find a way to access your file system (through live CD, etc) and make sure that  exists and does not have a size of 0. If this is the case, reinstall your kernel.

## Cannot remove ldlinux.sys
The  file has the immutable attribute set, which prevents it from being deleted or overwritten. This is because the sector location of the file must not change or else Syslinux has to be reinstalled. To remove it, run:

 # chattr -i /boot/syslinux/ldlinux.sys
 # rm /boot/syslinux/ldlinux.sys

## White block in upper left corner when using vesamenu
Problem:
As of linux-3.0, the modesetting driver tries to keep the current contents of the screen after changing the resolution (at least it does so with my Intel, when having Syslinux in text mode). It seems that this goes wrong when combined with the vesamenu module in Syslinux (the white block is actually an attempt to keep the Syslinux menu, but the driver fails to capture the picture from vesa graphics mode).

If you have a custom resolution and a  with early modesetting, try to append the following in  to remove the white block and continue in graphics mode:

 APPEND root=xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx rw 5 vga=current quiet splash

## Chainloading Windows does not work, when it is installed on another drive
If Windows is installed on a different drive than Arch and you have trouble chainloading it, try the following configuration:

Replace the mbr code with the one your Windows drive has (details above), and append  to the options.

## Read boot loader log
In some cases (e.g. boot loader unable to boot kernel) it is highly desirable to get more information from the boot process. Syslinux prints error messages to screen but the boot menu quickly overwrites the text. To avoid losing the log information, disable  in  and use the default "command-line" prompt. It means:

* avoid the  directive
* avoid
* avoid
* avoid
* use a higher
* use
* use

To get more detailed debug log, recompile the  package with additional CFLAGS:

 -DDEBUG_STDIO=1 -DCORE_DEBUG=1

## Btrfs compression
Booting from btrfs with compression is not supported.[https://wiki.syslinux.org/wiki/index.php/Syslinux_4_Changelog#Changes_in_4.02
This error will show:

 btrfs: found compressed data, cannot continue!
 invalid or corrupt kernel image.

## Btrfs multi-device
Booting from multiple-device btrfs is not supported.(As of 21-Jul-2016 line 1246 in validate_device_btrfs() in main.c)
This head-scratching error will show (assuming you are installing on sda1):

 /boot/syslinux is device /dev/sda1
 extlinux: path /boot/syslinux doesn't match device /dev/sda1
