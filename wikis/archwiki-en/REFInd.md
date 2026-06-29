# REFInd

rEFInd is a UEFI boot manager capable of launching kernels as EFI boot stubs. It is a fork of the no-longer-maintained rEFIt and fixes many issues with respect to non-Mac UEFI booting. It is designed to be platform-neutral and to simplify booting multiple operating systems.

## Supported file systems
rEFInd inherits the support for the file systems from the firmware (i.e. at least FAT12, FAT16 and FAT32). Additionally it loads any UEFI drivers placed in the  and  subdirectories of its own installation directory on the ESP. E.g. .

rEFInd also ships with a small collection of read-only EFI file system drivers, notably ext4 and Btrfs.

## Installation
Install the  package.

## Installing the rEFInd Boot Manager
rEFInd ships with UEFI drivers that implement read-only support for ReiserFS (deprecated), Ext2, Ext4, Btrfs, ISO-9660 and HFS+. Additionally rEFInd can access any file system that UEFI itself can, that includes FAT (as mandated by the UEFI specification), HFS+ on Macs and ISO-9660 on some systems.

To find additional drivers see The rEFInd Boot Manager: Using EFI Drivers: Finding Additional EFI Drivers.

To use the rEFInd, you must install it to the EFI system partition either using the refind-install script or by copying the files and setting up the boot entry manually.

## Installation with refind-install script
The rEFInd package includes the refind-install script to simplify the process of setting rEFInd as your default EFI boot entry. The script has several options for handling differing setups and UEFI implementations. See  or read the comments in the install script for explanations of the various installation options.

For many systems it should be sufficient to simply run:

 # refind-install

This will attempt to find and mount your ESP, copy rEFInd files to , and use efibootmgr to make rEFInd the default EFI boot application.

Alternatively you can install rEFInd to the default/fallback boot path . This is helpful for bootable USB flash drives or on systems that have issues with the NVRAM changes made by efibootmgr:

 # refind-install --usedefault /dev/sdXY

Where  is your EFI system partition (the block device, not its mountpoint).

After installing rEFInd's files to the ESP, verify that rEFInd has created  containing kernel parameters in the same directory as your kernel. This configuration file will not be created if you used the  option, run  as root to create it.

By default, rEFInd will scan all of your drives (that it has drivers for) and add a boot entry for each EFI boot loader it finds, which should include your kernel (since Arch enables EFI boot stubs by default). So you may have a bootable system at this point.

## Secure Boot
See Managing Secure Boot for Secure Boot support in rEFInd.

## Using PreLoader
See Secure Boot#Set up PreLoader to acquire signed  and  binaries.

Execute  with the option

 # refind-install --preloader /usr/share/preloader-signed/PreLoader.efi

Next time you boot with Secure Boot enabled, HashTool will launch and you will need to enroll the hash of rEFInd (), rEFInd's drivers (e.g. ) and kernel (e.g. ).

See  for more information.

## Using shim
Install . Read Secure Boot#shim, but skip all file copying.

## Using hashes
To use only hashes with shim, execute  with the option

 # refind-install --shim /usr/share/shim-signed/shimx64.efi

Next time you boot with Secure Boot enabled, MokManager will launch and you will need to enroll the hash of rEFInd (), rEFInd's drivers (e.g. ) and kernel (e.g. ).

## Using Machine Owner Key
To sign rEFInd with a Machine Owner Key (MOK), install .

Execute  with the options  and :

 # refind-install --shim /usr/share/shim-signed/shimx64.efi --localkeys

refind-install will create the keys for you and sign itself and its drivers. You will need to sign the kernel with the same key, e.g.:

 # sbsign --key /etc/refind.d/keys/refind_local.key --cert /etc/refind.d/keys/refind_local.crt --output /boot/vmlinuz-linux /boot/vmlinuz-linux

Once in MokManager add  to MoKList.  can be found inside a directory called  in the rEFInd's installation directory, e.g. .

See  for more information.

## Using your own keys
Follow Secure Boot#Using your own keys to create keys.

Create directory  and place Signature Database (db) key and certificates in it. Name the files:  (PEM format private key),  (PEM format certificate) and  (DER format certificate).

When running install script add option , e.g.:

 # refind-install --localkeys

rEFInd EFI binaries will be signed with the supplied key and certificate.

## Manual installation
If the  script does not work for you, rEFInd can be set up manually.

First, copy the executable to the ESP:

 # mkdir -p esp/EFI/refind
 # cp /usr/share/refind/refind_x64.efi esp/EFI/refind/

If you want to install rEFInd to the default/fallback boot path replace  with  in the following instructions and copy rEFInd EFI executable to :

 # mkdir -p esp/EFI/BOOT
 # cp /usr/share/refind/refind_x64.efi esp/EFI/BOOT/bootx64.efi

Then use efibootmgr to create a boot entry in the UEFI NVRAM, where  and  are the device and partition number of your EFI system partition. If you are installing rEFInd to the default/fallback boot path , you can skip this step.

 # efibootmgr --create --disk /dev/sdX --part Y --loader /EFI/refind/refind_x64.efi --label "rEFInd Boot Manager" --unicode

At this point, you should be able to reboot into rEFInd, but it may not be able to boot your kernel. If your kernel does not reside on your ESP, rEFInd may need to mount your partitions to find it. If the relevant file systems are not of the types supported by UEFI, additional driver files may be necessary. rEFInd automatically loads all drivers from the subdirectories  and  (e.g. ) in its install directory.

 # mkdir esp/EFI/refind/drivers_x64
 # cp /usr/share/refind/drivers_x64/drivername_x64.efi esp/EFI/refind/drivers_x64/

Now rEFInd should have a boot entry for your kernel, but it will not pass the correct kernel parameters. Set up #Passing kernel parameters. You should now be able to boot your kernel using rEFInd. If you are still unable to boot or if you want to tweak rEFInd's settings, many options can be changed with a configuration file:

 # cp /usr/share/refind/refind.conf-sample esp/EFI/refind/refind.conf

The sample configuration file is well commented and self-explanatory.

Unless you have set  in the configuration file, you should copy rEFInd's icons to get rid of the ugly placeholders:

 # cp -r /usr/share/refind/icons esp/EFI/refind/

You can try out different fonts by copying them and changing the  setting in :

 # cp -r /usr/share/refind/fonts esp/EFI/refind/

## Upgrading
Pacman updates the rEFInd files in  and will not copy new files to the ESP for you. If  worked for your original installation of rEFInd, you can rerun it to copy the updated files. The new configuration file will be copied as  so that you can integrate changes into your existing configuration file using a diff tool. If your rEFInd required #Manual installation, you will need to figure out which files to copy yourself.

## Pacman hook
You can automate the update process using a pacman hook:

Where the  may need to be changed to the correct update command for your setup. If you did #Manual installation, you could create your own update script to call with the hook.

## Configuration
The rEFInd configuration  is located in the same directory as the rEFInd EFI application (usually  or ). The default configuration file contains extensive comments explaining all its options, see Configuring the Boot Manager for more detailed explanations.

rEFInd detects bootable EFI binaries (Linux kernels, other operating system boot loaders, UEFI boot entries and etc.) at runtime. This means that in most simple situations, rEFInd works without any configuration. In particular, it is likely possible to boot Windows by default.

This does not mean there is no need to configure; for Linux, probably a user wants to set kernel parameters and initramfs. This can be done in another configuration file, . See below for details.

## Passing kernel parameters
There are two methods for setting the kernel parameters that rEFInd will pass to the kernel.

## For kernels automatically detected by rEFInd
rEFInd has two (or more) configuration files. , which lies in the ESP, configures rEFInd itself. On the other hand  lies in , i.e. the directory that kernel images lie, and it configures how the kernels are booted.

For automatically detected kernels you can either specify the kernel parameters explicitly in  or rely on rEFInd's ability to identify the root partition and kernel parameters. See Methods of Booting Linux: For Those With Foresight or Luck: The Easiest Method for more information.

For rEFInd to support the naming scheme of Arch Linux kernels and thus allow matching them with their respective initramfs images, you must uncomment and edit  option in . E.g.:

## refind_linux.conf
If rEFInd automatically detects your kernel, you can place a  file containing the kernel parameters in the same directory as your kernel. You can use  as a starting point. The first uncommented line of  will be the default parameters for the kernel. Subsequent lines will create entries in a submenu accessible using , , , or .

Alternatively, try running  as root. It will attempt to find your kernel in  and automatically generate . The script will only set up the most basic kernel parameters, so be sure to check the file it created for correctness.

If you do not specify an  parameter, rEFInd will automatically add it by searching for common RAM disk filenames in the same directory as the kernel. If you need either multiple or non-default  parameters, you must specify them manually in . For example:

## Without configuration
If you merely install rEFInd onto the ESP and launch it without any further ado (say via UEFI shell or KeyTool, or directly from firmware) you still get a menu to boot from via autodetection, with no configuration required whatsoever.

This works because rEFInd has a fallback mechanism that can:

* Identify the root partition (for  parameter ) via the Discoverable Partitions Specification or .
* Detect kernel options ( or ) from GPT partition attributes (using attribute  "read-only") or .

## For manual boot stanzas
If your kernel is not autodetected, or if you simply want more control over the options for a menu entry, you can manually create boot entries using stanzas in . Ensure that  includes  or these entries will not appear in rEFInd's menu. Kernel parameters are set with the  keyword. rEFInd will append the  parameter using the file specified by the  keyword in the stanza.

Manual boot stanzas are explained in Creating Manual Boot Stanzas.

{{hc|esp/EFI/refind/refind.conf|2=
...

menuentry "Arch Linux" {
	icon     /EFI/refind/icons/os_arch.png
	volume   "Arch Linux"
	loader   /boot/vmlinuz-linux
	initrd   /boot/initramfs-linux.img
	options  "root=PARTUUID=XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX rw add_efi_memmap"
	submenuentry "Boot using fallback initramfs" {
		initrd /boot/initramfs-linux-fallback.img
	}
	submenuentry "Boot to terminal" {
		add_options "systemd.unit=multi-user.target"
	}
}
}}

It is likely that you will need to change  to match either a filesystem's LABEL, a PARTLABEL, or a PARTUUID of the partition where the kernel image resides. See Persistent block device naming#by-label for examples of assigning a volume label. If  is not specified it defaults to volume from which rEFInd was launched (typically EFI system partition).

## Installation alongside an existing UEFI Windows installation
rEFInd is compatible with the EFI system partition created by a UEFI Windows installation, so there is no need to create or format another FAT32 partition when installing Arch alongside Windows. Simply mount the existing ESP and install rEFInd as usual. By default, rEFInd's autodetection feature should recognize any existing Windows or recovery boot loaders.

## Tools
rEFInd supports running various 3rd-party tools. Tools need to be installed separately. Edit  in  to choose which ones to show.

## UEFI shell
See Unified Extensible Firmware Interface#UEFI Shell.

Copy  to the root of the EFI system partition.

## Memtest86+
Install  and copy it to .

 # cp /boot/memtest86+/memtest.efi esp/EFI/tools/memtest86.efi

## Key management tools
rEFInd can detect Secure Boot key management tools if they are placed in rEFInd's directory on ESP,  or .

## HashTool
Follow #Using PreLoader and  will be placed in rEFInd's directory.

## MokManager
Follow #Using shim and MokManager will be placed in rEFInd's directory.

## KeyTool
Install .

Place KeyTool EFI binary in  or  with the name  or .

See Secure Boot#Using KeyTool for instructions on signing .

## GPT fdisk (gdisk)
Download the gdisk EFI application and copy  to .

## fwupd
Install  and setup fwupd.

Copy the  binary and firmware file to :

 # cp /usr/lib/fwupd/efi/fwupdx64.efi esp/EFI/tools/fwupx64.efi

## Poweroff or reboot
rEFInd reportedly have poweroff and reboot menu entries built in. Since this list of tools is the most extensive of its kind in this wiki, users of UEFI shell, or other UEFI boot managers, such as systemd-boot, might be interested in .

## Customization
rEFInd supports extensive customization, allowing you to modify icons, backgrounds, and fonts on the boot screen.

## Manual customization
To customize rEFInd, you need to edit the  configuration file, found in . In the following example, all assets will be stored in .

To set a custom background image (banner), use the  directive in :

 banner assets/banner.png

To set a custom set of icons, use the  directive in  and point it to the folder containing your icons:

 icons_dir assets/icons

The  package provides a set of icons for most distributions, including Arch Linux. These icons can be found in .

## Installing external themes
Installing external themes is straightforward. First, create a  folder in your rEFInd directory:

 # mkdir esp/EFI/refind/themes

Clone the theme (if it is hosted on GitHub, for example):

 # git clone url-to-theme esp/EFI/refind/themes/theme-name

Or, copy the theme manually:

 # cp -r path-to-theme esp/EFI/refind/themes/theme-name

In , include the theme's configuration file:

 include themes/theme-name/theme-name.conf

## Tips and tricks
## Using drivers in UEFI shell
To use rEFInd's drivers in UEFI shell load them using command  and refresh mapped drives with .

 Shell> load FS0:\EFI\refind\drivers\ext4_x64.efi
 Shell> map -r

Now you can access your file system from UEFI shell.

## Setting efifb resolution
If the resolution in  is set to an incorrect value, on all systems except Apple Macs rEFInd will display a list of supported resolutions. For Apple Macs it will silently use the default resolution.

To determine framebuffer resolutions supported by efifb, copy  from  to the root of ESP. Enter the UEFI shell and run .

Set one in . Reboot and check if settings has been applied by running  as root.

## Btrfs subvolume support
## Auto detection
To allow kernel auto detection on a Btrfs subvolume uncomment and edit  in .

Next add  to  in  and then prepend  to the initramfs path.

## Manual boot stanza
If booting a btrfs subvolume as root, prepend the path to the subvolume to the loader and initramfs paths, and amend the  line with . In the example below, root has been mounted as a btrfs subvolume called 'ROOT' (e.g. ):

{{hc|esp/EFI/refind/refind.conf|2=
...
menuentry "Arch Linux" {
        icon     /EFI/refind/icons/os_arch.png
        volume   "loader   /ROOT/boot/vmlinuz-linux
        initrd   /ROOT/boot/initramfs-linux.img
        options  "root=PARTUUID=XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX rw rootflags=subvol=ROOT"
...
}
}}

A failure to do so will otherwise result in the following error message:

## LoaderDevicePartUUID
Since version 0.13.1, rEFInd supports setting the UEFI variable [https://systemd.io/BOOT_LOADER_INTERFACE/ LoaderDevicePartUUID. Enabling this allows  to automount the EFI system partition without needing to specify it in . See systemd#GPT partition automounting.

For rEFInd to set , edit  and uncomment :

You can verify if it is set by checking its value with  or by looking at the state of "Boot loader sets ESP information" in  output.

## ISO images
rEFInd does not support booting ISO files since it lacks a loopback driver, but it can boot a ISO image that has been directly written to a partition. This requires the  driver, which can be found at .

## Troubleshooting
## Apple Macs
Use bless from within macOS to set rEFInd as the default boot entry:

 # bless --setBoot --folder esp/EFI/refind --file esp/EFI/refind/refind_x64.efi

## Blank rEFInd menu screen
If your  folder contains multiple file system drivers (see #Installing the rEFInd Boot Manager for clarification), this can lead to an improper functioning of rEFInd through a file system driver bug, whereby only a blank screen and with the rEFInd logo is shown (for custom themes, this would be the set background image). To fix this, simply remove all drivers except the one for the file system on which the kernel resides.

Another potential blank screen cause occurs when dual booting with Windows, where rEFInd is unsuccessful in auto-scanning the EFI system partitions on other disks. To remedy this, use blkid to identify Windows partitions, and add the PARTUUID of each Windows partition as a comma-separated entry to the variable  in . For example:

## Not using the distribution logo
If you see Tux instead of the Arch Logo, then you might be affected by this issue (your root partition is of type Linux x86-64 root (/) instead of Linux filesystem).

You can fix this using fdisk#Change partition type.

Additionally, if your root partition's label is simply "Linux" or if it contains the word "linux," Tux may be displayed. To specify the name of your distribution, consider renaming the partition label to reflect your distribution's name.

You can fix this using a file system label.

Another way to get the Arch Logo instead of Tux, is to copy the Arch Logo image file next to your kernel (e.g. ) and give the image file the same name as your kernel.

 # cp /usr/share/refind/icons/os_arch.png /boot/vmlinuz-linux.png

## Error: Not Found while loading vmlinuz-linux
If you add a menuentry and set the volume token correctly but still received the "Error: Not Found while loading vmlinuz-linux" message, you may need to check if driver for the file system on which kernel resides is correctly installed. Remember unsupported filesystem will not be detected, even if they are in the configuration file.
