# Systemd-boot

, previously called gummiboot (German for "rubber dinghy") and sometimes referred to as sd-boot, is an easy-to-configure UEFI boot manager. It provides a textual menu to select the boot entry and an editor for the kernel command line.

Note that systemd-boot can only start EFI executables (e.g., the Linux kernel EFI boot stub, UEFI shell, GRUB, or the Windows Boot Manager) from the EFI system partition it is installed to or from an Extended Boot Loader Partition (XBOOTLDR partition) on the same disk.

## Supported file systems
systemd-boot inherits the support for the file systems from the firmware (i.e. at least FAT12, FAT16 and FAT32). Additionally it loads any UEFI drivers placed in .

## Installation
systemd-boot is shipped with the  package which is a dependency of the  meta package, so no additional packages need to be installed manually.

## Installing the UEFI boot manager
To install systemd-boot, first make sure that the system is booted into UEFI mode and UEFI variables are accessible. This can be verified by running  or, if  is not installed, by running  (if the directory exists, the system is booted into UEFI mode.)

Use  to install systemd-boot to the ESP:

 # bootctl install

This will copy the systemd-boot UEFI boot manager to the ESP, create a UEFI boot entry for it and set it as the first in the UEFI boot order.

* On an x64 UEFI,  will be copied to  and .
* On an IA32 UEFI,  will be copied to  and .

The UEFI boot entry will be called "Linux Boot Manager" and will point to, depending on the UEFI bitness, either  or  on the ESP.

To conclude the installation, configure systemd-boot.

## Installation using XBOOTLDR
A separate /boot partition of type "Linux extended boot" (XBOOTLDR) can be created to keep the kernel and initramfs separate from the ESP. This is particularly helpful to dual boot with Windows with an existing ESP that is too small. Grml or Archiso are also possible use cases.

Prepare an ESP as usual and create another partition for XBOOTLDR on the same physical drive. The XBOOTLDR partition must have a partition type GUID of  ( type for gdisk,  type for fdisk). The size of the XBOOTLDR partition should be large enough to accommodate all of the kernels you are going to install.

During install, mount the ESP to  and the XBOOTLDR partition to .

Once in chroot, use the command:

 # bootctl --esp-path=/efi --boot-path=/boot install

To conclude the installation, configure systemd-boot.

## Updating the UEFI boot manager
Whenever there is a new version of systemd-boot, the UEFI boot manager can be optionally reinstalled by the user. This can be done manually or automatically; the two approaches are described thereafter.

## Manual update
Use bootctl to update systemd-boot:

 # bootctl update

## Automatic update
To update systemd-boot automatically, either use a systemd service or a pacman hook. The two methods are described below.

## systemd service
As of version 250,  ships with . Enabling this service will cause systemd-boot to run the following command on every boot:

 # bootctl --variables=no --graceful update

Like in the manual update, this will attempt to locate the ESP at ,  or . The command will update all installed versions of systemd-boot in the ESP if a newer version is available in . It will look for a systemd-boot file ending in  first to allow users to sign the image for use with Secure Boot.

## pacman hook
The package  adds a pacman hook which is executed every time  is upgraded. This hook differs from the systemd service method in that it only attempts to update the boot manager when  is updated rather than every boot, and it does it immediately rather than waiting until after the next boot.

Rather than installing the AUR package, you may prefer to manually place the following file in :

## Signing for Secure Boot
If you have Secure Boot enabled, you may want to add a pacman hook to automatically sign the boot manager upon every upgrade of the package:

{{hc|/etc/pacman.d/hooks/80-secureboot.hook|2=
[Trigger
Operation = Install
Operation = Upgrade
Type = Path
Target = usr/lib/systemd/boot/efi/systemd-boot*.efi

Description = Signing systemd-boot EFI binary for Secure Boot
When = PostTransaction
Exec = /bin/sh -c 'while read -r f; do /usr/lib/systemd/systemd-sbsign sign --private-key /path/to/keyfile.key --certificate /path/to/certificate.crt --output "${f}.signed" "$f"; done;'
Depends = sh
NeedsTargets
}}

Replace  and  with your signing key and certificate respectively. For better understanding of this hook, consult .

The created  will automatically be picked up by  or . See .

As an alternative, use sbctl.

## Configuration
## Loader configuration
The loader configuration is stored in the file . See  for details.

A loader configuration example is provided below:

## Remember last entry
The  can be changed to  in order to remember the last picked entry on startup. This is useful for when dual booting Windows and the surprise windows auto update pushes you into Linux.

Consult  for more details.

## Adding loaders
systemd-boot will search for .conf files in  on the EFI system partition it was launched from and additionally the XBOOTLDR partition on the same disk.

An example of loader files launching Arch from a volume using its UUID  is:

See the [https://uapi-group.org/specifications/specs/boot_loader_specification/#type-1-boot-loader-specification-entries Boot Loader Specification for details on all configuration options.

systemd-boot will automatically check at boot time for Windows Boot Manager at the location , Apple macOS Boot Manager in firmware, UEFI shell  and EFI Default Loader , as well as specially prepared kernel files found in . When detected, corresponding entries with titles , ,  and , respectively, will be generated. These entries do not require manual loader configuration. However, it does not auto-detect other EFI applications (unlike rEFInd), so for booting the Linux kernel, manual configuration entries must be created.

## UEFI Shells or other EFI applications
In case you installed a UEFI shell with the package , systemd-boot will auto-detect and create a new entry if the EFI file is placed in .
To perform this an example command after installing the package would be:

 # cp /usr/share/edk2-shell/x64/Shell.efi /boot/shellx64.efi

Otherwise in case you installed other EFI applications into the ESP, you can use the following snippets.

## Memtest86+
You need to install  for this to work. Also sign the EFI binary when using Secure Boot.

## Netboot
systemd-boot can chainload Netboot. Download the  EFI binary and signature, verify it and place it as proposed in .

## GRUB
systemd-boot can chainload GRUB. The location of the  binary matches the used  when GRUB was installed to the ESP.

## Boot from another disk
systemd-boot cannot launch EFI binaries from partitions other than the ESP it is launched from or the XBOOTLDR partition on the same disk, but it can direct the UEFI shell to do so.

First, install  as described above. In the UEFI shell, use the map command to take notes of the FS alias (ex: HD0a66666a2, HD0b, FS1, or BLK7) of the partition with the corresponding PARTUUID.

Then, use the  command to boot back into Linux, where you can create a new loader entry to run the target EFI program through the UEFI shell:

Ensure that the  path matches the location where the  has been copied in the esp partition. Also, note that the  EFI file can be moved elsewhere to avoid the automatic entry creation by systemd-boot.

Replace  with the previously noted FS alias.

* The  option prevents interrupting the target EFI program with .
* The  options hide the default UEFI shell greeting.
* To have the UEFI shell automatically return to the boot manager if the target EFI program exits (e.g. due to an error), add the  option.
* You can also add the  option if there is still unnecessary output in the UEFI shell.

## Booting into UEFI firmware setup
systemd-boot will automatically add an entry to boot into UEFI firmware setup if your device's firmware supports rebooting into setup from the OS.

## Kernel parameters editor with password protection
Alternatively you can install  which supports  basic configuration option. Use  to generate a value for this option.

Install systemd-boot-password with the following command:

 # sbpctl install esp

With enabled editor you will be prompted for your password before you can edit kernel parameters.

## Tips and tricks
## Keys inside the boot menu
You can use  and  while in the menu to adjust the menu timeout and  to edit the kernel parameters for this boot. Press  to see a short list of useful hotkeys. See  for the full list of available key bindings inside the boot menu.

## Choosing next boot
The boot manager is integrated with the systemctl command, allowing you to choose what option you want to boot after a reboot. For example, suppose you have built a custom kernel and created an entry file  to boot into it, you can just launch

 $ systemctl reboot --boot-loader-entry=arch-custom.conf

and your system will reboot into that entry maintaining the default option intact for subsequent boots. To see a list of possible entries pass the  option.

If you want to boot into the firmware of your motherboard directly, then you can use this command:

 $ systemctl reboot --firmware-setup

## Unified kernel images
Unified kernel images (UKIs) in  are automatically sourced by systemd-boot, and do not need an entry in . (Note that unified kernel images must have a  extension to be identified by systemd-boot.)

## Grml on ESP
Grml is a small live system with a collection of software for system administration and rescue.

In order to install Grml on the ESP, we only need to copy the kernel , the initramfs , and the squashed image  from the iso file to the ESP. To do so, first download grml64-small.iso and mount the file (the mountpoint is henceforth denoted mnt); the kernel and initramfs are located in , and the squashed image resides in .

Next, create a directory for Grml in your ESP,

 # mkdir -p esp/grml

and copy the above-mentioned files in there:

 # cp mnt/boot/grml64small/vmlinuz esp/grml
 # cp mnt/boot/grml64small/initrd.img esp/grml
 # cp mnt/live/grml64-small/grml64-small.squashfs esp/grml

In the last step, create an boot entry for systemd-boot: In  create a  file with the following content:

For an overview of the available boot options, consult the cheatcode for Grml.

## Archiso on ESP
As with Grml it is possible to use the Arch Linux ISO. To do this we need to copy the kernel , the initramfs , and the squashfs image  from the ISO file to the EFI system partition.

First download archlinux-YYYY.MM.DD-x86_64.iso.

Next, create a directory for archiso in your ESP:

 # mkdir -p esp/EFI/archiso

Extract the contents of the  directory in there:

 # bsdtar -v -x --no-same-permissions --strip-components 1 -f archlinux-YYYY.MM.DD-x86_64.iso -C esp/EFI/archiso arch

In the last step, create a boot entry for the systemd-boot: In  create a  file with the following content:

For an overview of the available boot options, consult the README.bootparams for mkinitcpio-archiso.

## Recovery Arch image on the ESP with Secure Boot
The official Arch ISO does not currently support Secure Boot. As a result, Secure Boot must be disabled to boot into the ISO for recovery or maintenance. This undermines system security and is not an ideal approach.

An alternative is to create a signed unified kernel image (UKI) using mkosi, assuming Secure Boot is already configured and functioning properly on your system. This allows you to boot into a signed recovery Arch environment without disabling Secure Boot or carrying an Arch ISO USB drive wherever your laptop goes.

https://swsnr.de/archlinux-rescue-image-with-mkosi/ describes how to set up Secure Boot-compatible Arch recovery images. A practical starting point with a sane mkosi configuration you can add your packages to is available at https://codeberg.org/swsnr/rescue-image.

## systemd-boot on BIOS systems
If you need a boot loader for BIOS systems that follows The Boot Loader Specification, then systemd-boot can be pressed into service on BIOS systems. The Clover boot loader supports booting from BIOS systems and provides an emulated UEFI environment.

## Troubleshooting
## systemd-boot does not display my boot entry
This may be caused by a variety of issues with the configuration file, such as the path to the kernel being specified incorrectly. To check, run:

 # bootctl

## Installing after booting in BIOS mode
If booted in BIOS mode, you can still install systemd-boot, however this process requires you to tell firmware to launch systemd-boots EFI file at boot:

* you have a working UEFI Shell somewhere else.
* your firmware interface provides a way of properly setting the EFI file that needs to be loaded at boot time.
* some firmware may use the default  if there is no other entry set in the UEFI.

If you can do it, the installation is easier: go into your UEFI Shell or your firmware configuration interface and change your machine's default EFI file to .

## Manual entry using efibootmgr
If the  command failed, you can create a UEFI boot entry manually using :

 # efibootmgr --create --disk /dev/sdX --part Y --loader '\EFI\systemd\systemd-bootx64.efi' --label "Linux Boot Manager" --unicode

where  is the EFI system partition.

## Manual entry using bcdedit from Windows
If for any reason you need to create a UEFI boot entry from Windows, you can use the following commands from an Administrator prompt:

 > bcdedit /copy "{bootmgr}" /d "Linux Boot Manager"
 > bcdedit /set "{guid}" path \EFI\systemd\systemd-bootx64.efi

Replace  with the id returned by the first command. You can also set it as the default entry using

 > bcdedit /default "{guid}"

## Menu does not appear after Windows upgrade
See UEFI#Windows changes boot order.

## Add support for Windows BitLocker TPM unlocking
To stop BitLocker from requesting the recovery key, add the following to loader.conf:

This will set the BootNext UEFI variable, whereby Windows Boot Manager is loaded without BitLocker requiring the recovery key. This is a one-time change, and systemd-boot remains the default boot loader. There is no need to specify Windows as an entry if it was autodetected.

This is an experimental feature, so make sure to consult .
