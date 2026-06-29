# Microcode

Processor manufacturers release stability and security updates to the processor microcode. These updates provide bug fixes that can be critical to the stability of your system. Without them, you may experience spurious crashes or unexpected system halts that can be difficult to track down.

All users with an AMD or Intel CPU should install the microcode updates to ensure system stability. In virtual machines and containers, the microcode updates belongs on the host, not in the guest system.

## Installation
To acquire updated microcode, depending on the processor, install one of the following packages:

*  for AMD processors,
*  for Intel processors.

mkinitcpio and dracut generate combined initramfs files by default. The microcode will be loaded automatically at boot time.

## Loading microcode
Microcode updates are usually shipped with the motherboard's firmware and applied during firmware initialization. Since OEMs might not release firmware updates in a timely fashion and old systems do not get new firmware updates at all, the ability to apply CPU microcode updates during boot was added to the Linux kernel. The Linux microcode loader supports three loading methods:

# Built-in microcode can be compiled into the kernel and then applied by the early loader.
# Early loading updates the microcode very early during boot, before the initramfs stage, and is preferred over late loading. This is mandatory for CPUs with severe hardware bugs, like the Intel Haswell and Broadwell processor families.
# Late loading (which may be dangerous) updates the microcode after booting which could be too late since the CPU might have already tried to use a faulty instruction. Even if already using early loading, late loading can still be used to apply a newer microcode update without needing to reboot.

## Early loading
The kernel's early loader expects microcode update files in  or  inside an uncompressed CPIO archive (initramfs image).

The early initramfs image can be combined with the main initramfs image into one file and passed as a single initramfs to the kernel (via the  kernel command line option by your boot loader or when packed in a unified kernel image) or it can exist as a separate file in which case multiple  kernel command line options need to be used. In both cases, the uncompressed CPIO archive with the microcode must be placed before the main initramfs.

Note that because of the wide variability in users' early-boot configuration, microcode updates may not be triggered automatically by Arch's default configuration.

## Custom built kernels
In order for early loading to work in custom kernels, "CPU microcode loading support" needs to be compiled into the kernel, not compiled as a module. This will enable the "Early load microcode" prompt which should be set to .

 CONFIG_BLK_DEV_INITRD=Y
 CONFIG_MICROCODE=y
 CONFIG_MICROCODE_INTEL=Y
 CONFIG_MICROCODE_AMD=y

## Microcode initramfs packed together with the main initramfs in one file
The uncompressed microcode CPIO can be prepended into the initramfs and used as a single initramfs file. This method is preferred over #Microcode in a separate initramfs file since no additional boot parameter configuration is necessary.

## mkinitcpio
For mkinitcpio to generate an initramfs file that includes microcode, make sure  is in the  array in .

If the  hook precedes , then only the microcode for the current CPU will be included. To include all CPU microcode files that can be found on the system, move the  hook before  or remove the  hook entirely.

When generating the initramfs, mkinitcpio will show:

 -> Early uncompressed CPIO image generation successful

You can verify the initramfs includes the microcode update files with . E.g., for :

For a unified kernel image you can use:

## dracut
For dracut, see .

## Microcode in a separate initramfs file
In the following sections replace  with your CPU manufacturer, i.e.  or .

## GRUB
grub-mkconfig will automatically detect the microcode update and configure GRUB appropriately. After installing the microcode package, regenerate the GRUB configuration to activate loading the microcode update by running:

 # grub-mkconfig -o /boot/grub/grub.cfg

Alternatively, users that manage their GRUB configuration file manually can add  (or  if  is a separate partition) as follows:

Repeat it for each menu entry.

## systemd-boot
Use the  option to load the microcode, before the initial ramdisk, as follows:

The latest microcode  must be available at boot time in your EFI system partition (ESP). The ESP must be mounted as  in order to have the microcode updated every time  or  is updated. Otherwise, copy  to your ESP at every update of the microcode package.

## EFISTUB
Append two  options:

 initrd=\cpu_manufacturer-ucode.img initrd=\initramfs-linux.img

## rEFInd
Edit boot options in
and add an  option for the microcode image as the first  argument passed. Use either  or  depending if the files in  are in the root of a separate partition.

The microcode is required to be the first initramfs declared for the boot options list. For example:

 "Boot using default options"  "root=PARTUUID=XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX rw add_efi_memmap initrd=boot\cpu_manufacturer-ucode.img initrd=boot\initramfs-%v.img"

## Manual boot stanzas
Users employing manual stanzas in  to define  kernels should add the  parameter with the proper path within the boot partition. This parameter is required as part of the options line, and not in the main part of the stanza. E.g.:

 options  "root=PARTUUID=XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX rw add_efi_memmap initrd=boot\cpu_manufacturer-ucode.img"

## Syslinux
Multiple initramfs files can be separated by commas in :

 LABEL arch
     MENU LABEL Arch Linux
     LINUX ../vmlinuz-linux
     INITRD ../cpu_manufacturer-ucode.img,../initramfs-linux.img
 ...

## LILO
LILO and potentially other old boot loaders do not support multiple initramfs images. Follow the #Microcode initramfs packed together with the main initramfs in one file method instead.

## Limine
For Limine you will just need to add the path to the microcode through the  option in your limine.conf file. Here is an example:

## Late loading
Late loading of microcode updates happens after the system has booted. It uses files in  and . The microcode update files are provided by  and , respectively.

Late loading requires the kernel to be built with , which is not the case for Arch officially supported kernels at the moment. ==== Late loading microcode updates ====

To manually reload the microcode, e.g. after updating the microcode files in  or , run:

 # echo 1 > /sys/devices/system/cpu/microcode/reload

This allows to apply newer microcode updates without rebooting the system.

## Verifying that microcode got updated on boot
Check the kernel messages with journalctl to see if the microcode has been updated:

 # journalctl -k --grep='microcode:'

One should see something similar to the following on every boot, indicating that microcode is updated very early on:

 kernel: microcode: Current revision: 0x00000012
 kernel: microcode: Updated early from: 0x0000000e

It is entirely possible, particularly with newer hardware, that there is no microcode update for the CPU.

On AMD systems using late loading the output will show the version of the old microcode before reloading the microcode and the new one once it is reloaded.

## Which CPUs accept microcode updates
Users may consult either Intel's repository or Gentoo's wiki on AMD at the following links to see if a particular model is supported:

* Gentoo:AMD microcode#Microcode firmware files.
* [https://www.intel.com/content/www/us/en/developer/articles/technical/software-security-guidance/secure-coding/loading-microcode-os.html Intel's Github repository.

## Detecting available microcode update
For Intel, it is possible to find out if the  contains microcode for the running CPU with .

# Install  and
# Load the  kernel module:
# Search it for your cpuid:
# If an update is available, it should show up below selected microcodes
# The microcode might already be in your vendor bios and not show up loading in dmesg. Compare to the current microcode running

For AMD, it can be done manually.

# Find out family, model and stepping of the CPU. For example, by running the following command:  Look at the output part like .
# Match the values accordingly with the list from amd-ucode README.
# If matched, compare the current revision of running microcode with the listed  value.

## Disable microcode loader
In case an updated CPU microcode causes issues, you may want to temporarily disable the microcode loader to allow successfully booting and downgrading the package. To disable the kernel's microcode loader, specify the  kernel parameter.
