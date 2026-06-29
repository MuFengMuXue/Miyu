# GRUB

GRUB (GRand Unified Bootloader) is a boot loader. The current GRUB is also referred to as GRUB 2. The original GRUB, or GRUB Legacy, corresponds to versions 0.9x. This page exclusively describes GRUB 2.

## Supported file systems
GRUB bundles its own support for multiple file systems, notably FAT32, ext4, Btrfs or XFS. See #Unsupported file systems for some caveats.

## UEFI systems
## Installation
First, install the packages  and : GRUB is the boot loader while efibootmgr is used by the GRUB installation script to write boot entries to NVRAM.

Then follow the below steps to install GRUB to your disk:

# Mount the EFI system partition and in the remainder of this section, substitute  with its mount point.
# Choose a boot loader identifier, here named . A directory of that name will be created in  to store the EFI binary and this is the name that will appear in the UEFI boot menu to identify the GRUB boot entry.
# Execute the following command to install the GRUB EFI application  to  and install its modules to .
::
::

After the above installation completed, the main GRUB directory is located at . Read /Tips and tricks#Alternative install method for how to specify an alternative location. Note that  also tries to create an entry in the firmware boot manager, named  in the above example – this will, however, fail if your boot entries are full or the systems prevents the boot order from being manipulated (e.g. Thinkpad firmware has a setting called "Boot Order Lock" which needs to be disabled for efibootmgr to be able to add/remove entries); use efibootmgr to remove unnecessary entries.

See UEFI troubleshooting in case of problems. Additionally see /Tips and tricks#UEFI further reading.

## Secure Boot support
GRUB fully supports secure boot utilising either CA keys or shim; the installation command, however, is different depending on which you intend to use.

## CA Keys
To make use of CA Keys the command is:

 # grub-install --target=x86_64-efi --efi-directory=esp --bootloader-id=GRUB --modules="tpm" --disable-shim-lock

## Shim-lock
When using Shim-lock, GRUB can only be successfully booted in Secure Boot mode if its EFI binary includes all of the modules necessary to read the filesystem containing the vmlinuz and initramfs images.

Since GRUB version , loading modules in Secure Boot Mode via  is no longer allowed, as this would violate the expectation to not sideload arbitrary code. If the GRUB modules are not embedded in the EFI binary, and GRUB tries to sideload/ them, GRUB will fail to boot with the message:

 error: prohibited by secure boot policy

Ubuntu, according to its official build script, embeds the following GRUB modules in its signed GRUB EFI binary :

* the "basic" modules, necessary for booting from a CD or from a simple-partitioned disk: , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , ,
* the "platform-specific" modules for x86_64-efi architecture, for example:
** : to play sounds during boot
** : to the CPU at boot
** : to support Measured Boot / Trusted Platform Modules
* the "advanced" modules, consisting of modules:
** : to boot from plain-mode encrypted disks
** : to support particular hashing and encryption algorithms
** : to boot from LUKS-encrypted disks:
** : to boot from LVM logical volume disks
** , , , : to boot from RAID virtual disks

You must construct your list of GRUB modules in the form of a shell variable that we denote as . You can use the latest Ubuntu script as a starting point, and trim away modules that are not necessary on your system. Omitting modules will make the boot process relatively faster, and save some space on the ESP partition.

You also need a Secure Boot Advanced Targeting (SBAT) file/section included in the EFI binary, to improve the security; if GRUB is launched from the UEFI shim loader.  This SBAT file/section contains metadata about the GRUB binary (version, maintainer, developer, upstream URL) and makes it easier for shim to block certain GRUB versions from being loaded if they have security vulnerabilitiesas explained in the [https://github.com/rhboot/shim/blob/main/SBAT.md UEFI shim boot loader secure boot life-cycle improvements document from shim.

The first-stage UEFI boot loader shim will fail to launch  if the SBAT section from  is missing!

If GRUB is installed, a sample SBAT .csv file is provided under .

Reinstall GRUB using the provided  file and all the needed  and sign it:

 # grub-install --target=x86_64-efi --efi-directory=esp --modules="${GRUB_MODULES}" --sbat /usr/share/grub/sbat.csv
 # sbsign --key MOK.key --cert MOK.crt --output esp/EFI/GRUB/grubx64.efi esp/EFI/GRUB/grubx64.efi
 # cp esp/EFI/GRUB/grubx64.efi esp/EFI/BOOT/grubx64.efi

Reboot, select the key in MokManager, and Secure Boot should be working.

## Using Secure Boot
After installation see Secure Boot#Implementing Secure Boot for instructions on enabling it.

If you are using the CA Keys method then key management, enrollment, and file signing can be automated by using , see Secure Boot#Assisted process with sbctl for details.

## BIOS systems
## GUID Partition Table (GPT) specific instructions
On a BIOS/GPT configuration, a BIOS boot partition is required.  GRUB embeds its  into this partition.

Create a mebibyte partition ( with fdisk or gdisk) on the disk with no file system and with partition type GUID .

* fdisk: Create a partition and use the  command to change its partition type to .
* gdisk: Create a partition with partition type .
* GNU Parted: Create a partition and set the  flag on it.

This partition can be in any position order but has to be on the first 2 TiB of the disk.  This partition needs to be created before GRUB installation.  When the partition is ready, install the boot loader as per the instructions below.

The space before the first partition can also be used as the BIOS boot partition though it will be out of GPT alignment specification.  Since the partition will not be regularly accessed performance issues can be disregarded, though some disk utilities will display a warning about it.  In fdisk or gdisk create a new partition starting at sector 34 and spanning to 2047 and set the type.  To have the viewable partitions begin at the base consider adding this partition last.

## Master Boot Record (MBR) specific instructions
Usually the post-MBR gap (after the 512 byte MBR region and before the start of the first partition) in many MBR partitioned systems is 31 KiB when DOS compatibility cylinder alignment issues are satisfied in the partition table. However a post-MBR gap of about 1 to 2 MiB is recommended to provide sufficient room for embedding GRUB's  (). It is advisable to use a partitioning tool that supports 1 MiB partition alignment to obtain this space as well as to satisfy other non-512-byte-sector issues (which are unrelated to embedding of ).

## Installation
Install the  package. (It will replace  if that is already installed.) Then do:

 # grub-install --target=i386-pc /dev/sdX

where  is deliberately used regardless of your actual architecture, and  is the disk (not a partition) where GRUB is to be installed. For example  or , or . See Device file#Block device names for a description of the block device naming scheme.

Now you must generate the main configuration file.

If you use LVM for your , you can install GRUB on multiple physical disks.

See  and GRUB Manual for more details on the  command.

## Configuration
On an installed system, GRUB loads the  configuration file each boot. You can follow #Generated grub.cfg for using a tool, or #Custom grub.cfg for a manual creation.

## Generated grub.cfg
This section only covers editing the  configuration file. See /Tips and tricks for more information.

## Generate the main configuration file
After the installation, the main configuration file  needs to be generated. The generation process can be influenced by a variety of options in  and scripts in . For the list of options in  and a concise description of each refer to GNU's documentation.

If you have not done additional configuration, the automatic generation will determine the root filesystem of the system to boot for the configuration file. For that to succeed it is important that the system is either booted or chrooted into.

Use the grub-mkconfig tool to generate :

 # grub-mkconfig -o /boot/grub/grub.cfg

By default the generation scripts automatically add menu entries for all installed Arch Linux kernels to the generated configuration.

To automatically add entries for other installed operating systems, see #Detecting other operating systems.

You can add additional custom menu entries by editing  and re-generating . Or you can create  and add them there. Changes to  do not require re-running grub-mkconfig, since  adds the necessary  statement to the generated configuration file.

See #Boot menu entry examples for custom menu entry examples.

## Detecting other operating systems
To have grub-mkconfig search for other installed systems and automatically add them to the menu, install the  package and mount the partitions from which the other systems boot. Then re-run grub-mkconfig. If you get the following output:  then edit  and add/uncomment:

 GRUB_DISABLE_OS_PROBER=false

Then try again.

## Windows
For Windows installed in UEFI mode, make sure the EFI system partition containing the Windows Boot Manager () is mounted. Run  as root to detect and generate an entry for it.

For Windows installed in BIOS mode, mount the Windows system partition (its file system label should be  or ). Run  as root to detect and generate an entry for it.

## Additional arguments
To pass custom additional arguments to the Linux image, you can set the  +  variables in . The two are appended to each other and passed to kernel when generating regular boot entries. For the recovery boot entry, only  is used in the generation.

It is not necessary to use both, but can be useful. For example, you could use  where  is the UUID of your swap partition to enable resume after hibernation. This would generate a recovery boot entry without the resume and without  suppressing kernel messages during a boot from that menu entry. Though, the other (regular) menu entries would have them as options.

By default grub-mkconfig determines the UUID of the root filesystem for the configuration. To disable this, uncomment .

For generating the GRUB recovery entry you have to ensure that  is not set to  in .

See Kernel parameters for more info.

## Setting the top-level menu entry
By default, grub-mkconfig sorts the included kernels using  and uses the first kernel in that list as the top-level entry. This means that, for example, since  is sorted before , if you have both  and  installed, the LTS kernel will be the top-level menu entry, which may not be desirable. This can be overridden by specifying  in . For example, to make the regular kernel be the top-level menu entry, you can use .

## LVM
If you use LVM for your  or  root partition, make sure that the  module is preloaded:

## RAID
GRUB provides convenient handling of RAID volumes. You need to load GRUB modules  or  to allow you to address the volume natively:

For example,  becomes:

 set root=(md/0)

whereas a partitioned RAID volume (e.g. ) becomes:

 set root=(md/0,1)

To install grub when using RAID1 as the  partition (or using  housed on a RAID1 root partition), on BIOS systems, simply run grub-install on both of the drives, such as:

 # grub-install --target=i386-pc --debug /dev/sda
 # grub-install --target=i386-pc --debug /dev/sdb

Where the RAID 1 array housing  is housed on  and .

## Encrypted /boot
GRUB also has special support for booting with an encrypted . This is done by unlocking a LUKS blockdevice in order to read its configuration and load any initramfs and kernel from it. This option tries to solve the issue of having an unencrypted boot partition.

To enable this feature encrypt the partition with  residing on it using LUKS as normal. Then add the following option to :

This option is used by grub-install to generate the grub .

Make sure to install grub after modifying this option or encrypting the partition.

Without further changes you will be prompted twice for a passphrase: the first for GRUB to unlock the  mount point in early boot, the second to unlock the root filesystem itself as implemented by the initramfs. You can use a keyfile to avoid this.

## LUKS2
Use  as described in the #Installation section to create a bootable GRUB image with LUKS support. Note the following caveats:

* Initial LUKS2 support was added to GRUB 2.06, but with several limitations that are only partially addressed in GRUB 2.12rc1. See GRUB bug #55093.
* Since GRUB 2.12rc1,  can create a core image to unlock LUKS2. However, it only supports PBKDF2, not Argon2.
* Argon2id (cryptsetup default) and Argon2i PBKDFs are not supported (GRUB bug #59409), only PBKDF2 is.

:

If you enter an invalid passphrase during boot and end up at the GRUB rescue shell, try  to mount all (hopefully only one) encrypted partitions or use  to mount a specific one. Then proceed with  and  as usual.

If you enter a correct passphrase, but an  error is immediately returned, make sure that the right cryptographic modules are specified. Use  and check whether the hash function (SHA-256, SHA-512) matches the modules (, ) installed and the PBKDF algorithm is pbkdf2. The hash and PBDKDF algorithms can be changed for existing keys by using .  Under normal circumstances it should take a few seconds before the passphrase is processed.

## Custom grub.cfg
This section describes the manual creation of GRUB boot entries in  instead of relying on grub-mkconfig.

A basic GRUB config file uses the following options:

*  is the partition Y on disk X, partition numbers starting at 1, disk numbers starting at 0
*  is the default boot entry that is chosen after timeout for user action
*  is the time M to wait in seconds for a user selection before default is booted
* {{ic|menuentry "title" {entry options}}} is a boot entry titled
*  sets the boot partition, where the kernel and GRUB modules are stored (boot need not be a separate partition, and may simply be a directory under the "root" partition ())

## LoaderDevicePartUUID
For GRUB to set the  UEFI variable required by  for GPT partition automounting, load the  module in :

## Boot menu entry examples
For tips on managing multiple GRUB entries, for example when using both  and  kernels, see /Tips and tricks#Multiple entries.

For Archiso and Archboot boot menu entries see Multiboot USB drive#Boot entries.

## GRUB commands
## "Shutdown" menu entry
{{bc|
menuentry "System shutdown" {
	echo "System shutting down..."
	halt
}
}}

## "Restart" menu entry
{{bc|
menuentry "System restart" {
	echo "System rebooting..."
	reboot
}
}}

## "UEFI Firmware Settings" menu entry
{{bc|1=
if [ ${grub_platform} == "efi" ]; then
	menuentry 'UEFI Firmware Settings' --id 'uefi-firmware' {
		fwsetup
	}
fi
}}

## EFI binaries
When launched in UEFI mode, GRUB can chainload other EFI binaries.

{{Tip|1=To show these menu entries only when GRUB is launched in UEFI mode, enclose them in the following  statement:

{{bc|1=
if [ ${grub_platform} == "efi" ]; then
	place UEFI-only menu entries here
fi
}}

}}

## UEFI Shell
You can launch UEFI Shell by placing it in the root of the EFI system partition and adding this menu entry:

{{bc|1=
menuentry "UEFI Shell" {
	insmod fat
	insmod chain
	search --no-floppy --set=root --file /shellx64.efi
	chainloader /shellx64.efi
}
}}

## gdisk
Download the gdisk EFI application and copy  to .

{{bc|1=
menuentry "gdisk" {
	insmod fat
	insmod chain
	search --no-floppy --set=root --file /EFI/tools/gdisk_x64.efi
	chainloader /EFI/tools/gdisk_x64.efi
}
}}

## Chainloading a unified kernel image
If you have a unified kernel image generated from following Secure Boot or other means, you can add it to the boot menu. For example:

{{bc|1=
menuentry "Arch Linux" {
	insmod fat
	insmod chain
	search --no-floppy --set=root --fs-uuid FILESYSTEM_UUID
	chainloader /EFI/Linux/arch-linux.efi
}
}}

## Dual-booting
## GNU/Linux
Assuming that the other distribution is on partition :

{{bc|1=
menuentry "Other Linux" {
	set root=(hd0,2)
	linux /boot/vmlinuz (add other options here as required)
	initrd /boot/initramfs.img (if the other kernel uses/needs one)
}
}}

Alternatively let GRUB search for the right partition by UUID or file system label:

{{bc|1=
menuentry "Other Linux" {
        # assuming that UUID is 763A-9CB6
	search --no-floppy --set=root --fs-uuid 763A-9CB6

        # search by label OTHER_LINUX (make sure that partition label is unambiguous)
        #search --no-floppy --set=root --label OTHER_LINUX

	linux /boot/vmlinuz (add other options here as required, for example: root=UUID=763A-9CB6)
	initrd /boot/initramfs.img (if the other kernel uses/needs one)
}
}}

If the other distribution has already a valid  folder with installed GRUB, , kernel and initramfs, GRUB can be instructed to load these other  files on-the-fly during boot. For example, for  and the fourth GPT partition:

{{bc|1=
menuentry "configfile hd0,gpt4"  {
        insmod part_gpt
        insmod btrfs
        insmod ext2
        set root='hd0,gpt4'
        configfile /boot/grub/grub.cfg
}
}}

When choosing this entry, GRUB loads the  file from the other volume and displays that menu. Any environment variable changes made by the commands in file will not be preserved after  returns. Press  to return to the first GRUB menu.

## Windows installed in UEFI/GPT mode
This mode determines where the Windows boot loader resides and chain-loads it after GRUB when the menu entry is selected. The main task here is finding the EFI system partition and running the boot loader from it.

{{bc|1=
if [ "${grub_platform}" == "efi" ]; then
	menuentry "Microsoft Windows Vista/7/8/8.1 UEFI/GPT" {
		insmod part_gpt
		insmod fat
		insmod chain
		search --no-floppy --fs-uuid --set=root $hints_string $fs_uuid
		chainloader /EFI/Microsoft/Boot/bootmgfw.efi
	}
fi
}}

where  and  are obtained with the following two commands.

The  command determines the UUID of the EFI system partition:

Alternatively one can run  and read the UUID of the EFI system partition from there.

The  command will determine the location of the EFI system partition, in this case harddrive 0:

These two commands assume the ESP Windows uses is mounted at . There might be case differences in the path to Windows's EFI file, what with being Windows, and all.

## Windows installed in BIOS/MBR mode
Throughout this section, it is assumed your Windows partition is . A different partition will change every instance of .

In both examples  is the filesystem UUID which can be found with command .

For Windows Vista/7/8/8.1/10:

{{bc|1=
if [ "${grub_platform}" == "pc" ]; then
	menuentry "Microsoft Windows Vista/7/8/8.1/10 BIOS/MBR" {
		insmod part_msdos
		insmod ntfs
		insmod ntldr
		search --no-floppy --fs-uuid --set=root --hint-bios=hd0,msdos1 --hint-efi=hd0,msdos1 --hint-baremetal=ahci0,msdos1 XXXX-XXXX
		ntldr /bootmgr
	}
fi
}}

For Windows XP:

{{bc|1=
if [ "${grub_platform}" == "pc" ]; then
	menuentry "Microsoft Windows XP" {
		insmod part_msdos
		insmod ntfs
		insmod ntldr
		search --no-floppy --fs-uuid --set=root --hint-bios=hd0,msdos1 --hint-efi=hd0,msdos1 --hint-baremetal=ahci0,msdos1 XXXX-XXXX
		ntldr /ntldr
	}
fi
}}

## Using labels
It is possible to use file system labels, human-readable strings attached to file systems, by using the  option to . First of all, make sure your file system has a label.

Then, add an entry using labels. An example of this:

 menuentry "Arch Linux, session texte" {
   search --label --set=root archroot
   linux /boot/vmlinuz-linux root=/dev/disk/by-label/archroot ro
   initrd /boot/initramfs-linux.img
 }

## Using the command shell
Since the MBR is too small to store all GRUB modules, only the menu and a few basic commands reside there. The majority of GRUB functionality remains in modules in , which are inserted as needed. In error conditions (e.g. if the partition layout changes) GRUB may fail to boot. When this happens, a command shell may appear.

GRUB offers multiple shells/prompts. If there is a problem reading the menu but the boot loader is able to find the disk, you will likely be dropped to the "normal" shell:

 grub>

If there is a more serious problem (e.g. GRUB cannot find required files), you may instead be dropped to the "rescue" shell:

 grub rescue>

The rescue shell is a restricted subset of the normal shell, offering much less functionality. If dumped to the rescue shell, first try inserting the "normal" module, then starting the "normal" shell:

 grub rescue> set prefix=(hdX,Y)/boot/grub
 grub rescue> insmod (hdX,Y)/boot/grub/i386-pc/normal.mod
 rescue:grub> normal

## Pager support
GRUB supports pager for reading commands that provide long output (like the  command). This works only in normal shell mode and not in rescue mode. To enable pager, in GRUB command shell type:

 sh:grub> set pager=1

## Using the command shell environment to boot operating systems
 grub>

The GRUB's command shell environment can be used to boot operating systems.
A common scenario may be to boot Windows / Linux stored on a drive/partition via chainloading.

Chainloading means to load another boot-loader from the current one, ie, chain-loading.

The other boot loader may be embedded at the start of a partitioned disk (MBR), at the start of a partition or a partitionless disk (VBR), or as an EFI binary in the case of UEFI.

## Chainloading a partition's VBR
 set root=(hdX,Y)
 chainloader +1
 boot

X=0,1,2...
Y=1,2,3...

For example to chainload Windows stored in the first partition of the first hard disk,

 set root=(hd0,1)
 chainloader +1
 boot

Similarly GRUB installed to a partition can be chainloaded.

## Chainloading a disk's MBR or a partitionless disk's VBR
 set root=hdX
 chainloader +1
 boot

## Chainloading Windows/Linux installed in UEFI mode
 insmod fat
 set root=(hd0,gpt4)
 chainloader /EFI/Microsoft/Boot/bootmgfw.efi
 boot

 is used for loading the FAT file system module for accessing the Windows boot loader on the UEFI system partition.
 or  is the UEFI system partition in this example.
The entry in the  line specifies the path of the .efi file to be chain-loaded.

## Normal loading
See the examples in #Using the rescue console

## Using the rescue console
See #Using the command shell first. If unable to activate the standard shell, one possible solution is to boot using a live CD or some other rescue disk to correct configuration errors and reinstall GRUB. However, such a boot disk is not always available (nor necessary); the rescue console is surprisingly robust.

The available commands in GRUB rescue include , , , and . This example uses  and .  modifies variables and  inserts new modules to add functionality.

Before starting, the user must know the location of their  partition (be it a separate partition, or a subdirectory under their root):

 grub rescue> set prefix=(hdX,Y)/boot/grub

where  is the physical drive number and  is the partition number.

To expand console capabilities, insert the  module:

 grub rescue> insmod i386-pc/linux.mod

or simply

 grub rescue> insmod linux

This introduces the  and  commands, which should be familiar.

An example, booting Arch Linux:

 set root=(hd0,5)
 linux /boot/vmlinuz-linux root=/dev/sda5
 initrd /boot/initramfs-linux.img
 boot

With a separate boot partition (e.g. when using UEFI), again change the lines accordingly:

 set root=(hd0,5)
 linux (hdX,Y)/vmlinuz-linux root=/dev/sda6
 initrd (hdX,Y)/initramfs-linux.img
 boot

After successfully booting the Arch Linux installation, users can correct  as needed and then reinstall GRUB.

To reinstall GRUB and fix the problem completely, changing  if needed. See #Installation for details.

## GRUB removal
## UEFI systems
Before removing grub, make sure that some other boot loader is installed and configured to take over.

If  has grub as the first entry, install another boot loader to put it in front, such as systemd-boot above. grub can then be removed using its bootnum.

 # efibootmgr --delete-bootnum -b 1

Also delete the  and  directories.

## BIOS systems
To replace grub with any other BIOS boot loader, simply install them, which will overwrite the MBR boot code.

 creates the  directory that needs to be removed manually. Though some users will want to keep it, should they want to install grub again.

After migrating to UEFI/GPT one may want to remove the MBR boot code using dd.

## Troubleshooting
## Unsupported file systems
In case that GRUB does not support the root file system, an alternative  partition with a supported file system must be created. In some cases, the development version of GRUB  may have native support for the file system.

If GRUB is used with an unsupported file system it is not able to extract the UUID of your drive so it uses classic non-persistent  names instead. In this case you might have to manually edit  and replace  with . You can use the  command to get the UUID of your device, see Persistent block device naming.

While GRUB supports F2FS since version 2.0.4, it cannot correctly read its boot files from an F2FS partition that was created with the  flag enabled.

## Enable debug messages
Add:

 set pager=1
 set debug=all

to .

## msdos-style error message
 grub-setup: warn: This msdos-style partition label has no post-MBR gap; embedding will not be possible!
 grub-setup: warn: Embedding is not possible. GRUB can only be installed in this setup by using blocklists.
             However, blocklists are UNRELIABLE and its use is discouraged.
 grub-setup: error: If you really want blocklists, use --force.

This error may occur when you try installing GRUB in a VMware container. Read more about it here. It happens when the first partition starts just after the MBR (block 63), without the usual space of 1 MiB (2048 blocks) before the first partition. Read #Master Boot Record (MBR) specific instructions

## UEFI
## Common installation errors
* An error that may occur on some UEFI devices is . You have to remount  with read-write enabled.  See the Gentoo Wiki on installing the boot loader.
* If you have a problem running grub-install with sysfs or procfs and it says you must run  try mounting the efivarfs with the command above.
* Without  or  option, grub-install cannot determine for which firmware to install. In such cases  will print .
* If after running grub-install you get , then the partition is most likely not FAT32 formatted.

## Create a GRUB entry in the firmware boot manager
 automatically tries to create a menu entry in the boot manager. If it does not, then see UEFI#efibootmgr for instructions to use  to create a menu entry. However, the problem is likely to be that you have not booted your CD/USB in UEFI mode, as in Installation guide#Verify the boot mode.

As another example of creating a GRUB entry in the firmware boot manager, consider . This assumes that  is the EFI System Partition, and is mounted at . Which are the default behavior of .  It creates a new boot option, called "Linux", and puts it at the top of the boot order list. Options may be passed to modify the default behavior. The default OS Loader is .

## Drop to rescue shell
If GRUB loads but drops into the rescue shell with no errors, it can be due to one of these two reasons:

* It may be because of a missing or misplaced . This will happen if GRUB UEFI was installed with  and  is missing,
* It also happens if the boot partition, which is hardcoded into the  file, has changed.

## GRUB UEFI not loaded
An example of a working UEFI:

If the screen only goes black for a second and the next boot option is tried afterwards, according to this post, moving GRUB to the partition root can help. The boot option has to be deleted and recreated afterwards. The entry for GRUB should look like this then:

 Boot0000* GRUB HD(1,800,32000,23532fbb-1bfa-4e46-851a-b494bfe9478c)File(\grubx64.efi)

## Default/fallback boot path
Some UEFI firmwares (e.g. MSI motherboards) require a bootable file at a known location before they will show UEFI NVRAM boot entries. If this is the case,  will claim  has added an entry to boot GRUB, however the entry will not show up in the VisualBIOS boot order selector. The solution is to install GRUB at the default/fallback boot path:

 # grub-install --target=x86_64-efi --efi-directory=esp --removable

Alternatively you can move an already installed GRUB EFI executable to the default/fallback path:

 # mv esp/EFI/grub esp/EFI/BOOT
 # mv esp/EFI/BOOT/grubx64.efi esp/EFI/BOOT/BOOTX64.EFI

## Invalid signature
If trying to boot Windows results in an "invalid signature" error, e.g. after reconfiguring partitions or adding additional hard drives, (re)move GRUB's device configuration and let it reconfigure:

 # mv /boot/grub/device.map /boot/grub/device.map-old
 # grub-mkconfig -o /boot/grub/grub.cfg

 should now mention all found boot options, including Windows. If it works, remove .

## Boot freezes
If booting gets stuck without any error message after GRUB loading the kernel and the initial ramdisk, try removing the  kernel parameter.

## Arch not found from other OS
Some have reported that other distributions may have trouble finding Arch Linux automatically with . If this problem arises, it has been reported that detection can be improved with the presence of . This file and updating tool is available with the package .

## Warning when installing in chroot
When installing GRUB on a LVM system in a chroot environment (e.g. during system installation), you may receive warnings like

 /run/lvm/lvmetad.socket: connect failed: No such file or directory

or

 WARNING: failed to connect to lvmetad: No such file or directory. Falling back to internal scanning.

This is because  is not available inside the chroot. These warnings will not prevent the system from booting, provided that everything has been done correctly, so you may continue with the installation.

## GRUB loads slowly
GRUB can take a long time to load when disk space is low. Check if you have sufficient free disk space on your  or  partition when you are having problems.

## error: unknown filesystem
GRUB may output  and refuse to boot for a few reasons. If you are certain that all UUIDs are correct and all filesystems are valid and supported, it may be because your BIOS Boot Partition is located outside the first 2 TiB of the drive Use a partitioning tool of your choice to ensure this partition is located fully within the first 2 TiB, then reinstall and reconfigure GRUB.

This error might also be caused by an ext4 filesystem having unsupported features set:
*  - unsupported.
*  - will be supported in GRUB 2.11 ([https://git.savannah.gnu.org/cgit/grub.git/commit/?id=7fd5feff97c4b1f446f8fcf6d37aca0c64e7c763 commit).

## grub-reboot not resetting
GRUB seems to be unable to write to root Btrfs partitions If you use grub-reboot to boot into another entry it will therefore be unable to update its on-disk environment. Either run grub-reboot from the other entry (for example when switching between various distributions) or consider a different file system. You can reset a "sticky" entry by executing  and setting  in your  (do not forget ).

## Old Btrfs prevents installation
If a drive is formatted with Btrfs without creating a partition table (eg. /dev/sdx), then later has partition table written to, there are parts of the BTRFS format that persist. Most utilities and OS's do not see this, but GRUB will refuse to install, even with --force

 # grub-install: warning: Attempting to install GRUB to a disk with multiple partition labels. This is not supported yet..
 # grub-install: error: filesystem `btrfs' does not support blocklists.

You can zero the drive, but the easy solution that leaves your data alone is to erase the Btrfs superblock with

## Windows 8/10 not found
A setting in Windows 8/10 called "Hiberboot", "Hybrid Boot" or "Fast Boot" can prevent the Windows partition from being mounted, so  will not find a Windows install. Disabling Hiberboot in Windows will allow it to be added to the GRUB menu.

## GRUB rescue and encrypted /boot
When using an encrypted /boot, and you fail to input a correct password, you will be dropped in grub-rescue prompt.

This grub-rescue prompt has limited capabilities. Use the following commands to complete the boot:

See [https://blog.stigok.com/2017/12/30/decrypt-and-mount-luks-disk-from-grub-rescue-mode.html this blog post for a better description.

## GRUB is installed but the menu is not shown at boot
Check  if  is set to , in which case set it to a positive number: it sets the number of seconds before the default GRUB entry is loaded. Also check if  is set to  and set it to , so that the menu will be shown by default. Then regenerate the main configuration file and reboot to check if it worked.

If it does not work, there may be incompatibility problems with the graphical terminal. Set  to  in  to disable the GRUB graphical terminal.

## GRUB is installed, but receive "ERROR CODE 1962 - No operating system found" message on older Lenovo machines
See Fixing Lenovo’s ERROR CODE 1962 by spoofing the EFI boot entries.
