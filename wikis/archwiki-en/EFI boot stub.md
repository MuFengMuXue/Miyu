# EFI boot stub

An EFI boot stub (aka EFI stub) is a kernel that is an EFI executable, i.e. that can directly be booted from the UEFI.

Historically, this article and the Debian Wiki used the terms as one word (EFISTUB or EFIStub).

By default Arch Linux kernels are EFI boot stubs. If compiling the kernel, activate it by setting . See The EFI Boot Stub for more information.

Before continuing, you need an EFI system partition and choose how it is mounted.

## Alternative: Unified kernel image
A unified kernel image (UKI) itself is an EFI stub kernel, which also contains the initramfs and boot options in a single file.  The following table lists features of EFI stub that is not UKI compared to UKI, in the situation where they are booted from UEFI.

{| class="wikitable"
!  !! EFI stub that is non-UKI !! Unified kernel image
|-
! initramfs
| A separate file, stored in ESP || Included
|-
! boot option
| Stored in a UEFI variable || Included
|}

When there is no problem, UKI is simpler, by requring only one file that contains everything necessary to boot. However with a non-UKI kernel, one can for example switch between different initramfs files or try various boot options for a single kernel image. For UKI, each change leads to a separate UKI.

## Booting an EFI boot stub
## Using UEFI directly
UEFI is designed to remove the need for an intermediate boot loader such as GRUB. If your motherboard has a good UEFI implementation, it is possible to embed the kernel parameters within a UEFI boot entry and for the motherboard to boot Arch directly. You can use efibootmgr or UEFI Shell v2 to modify your motherboard's boot entries.

## efibootmgr
To create a boot entry with efibootmgr that will load the kernel:

 # efibootmgr --create --disk /dev/sdX --part Y --label "Arch Linux" --loader /vmlinuz-linux --unicode 'root=block_device_identifier rw initrd=\initramfs-linux.img'

Where  and  are the drive and partition number where the ESP is located and  parameters with your Linux root partitions.

If omitted, then the first partition on  is used as the ESP.

Note that the / argument in quotes is just the list of kernel parameters, so you may need to add additional parameters (e.g. for suspend to disk).

An example with LTS Linux kernel, NVME storage, BTRFS filesystem with specific subvolume and hibernation on swap partition:

 # efibootmgr --create \
  --disk /dev/nvme0n1 --part 1 \
  --label "EFISTUB Arch" \
  --loader /vmlinuz-linux-lts \
  --unicode 'root=UUID=01a40dd8-28f0-4636-be1e-aeed60c98095 resume=UUID=2d877d5d-4ca1-4d46-a3d6-b6ee94cbbd78 rw rootflags=subvol=@ loglevel=3 quiet initrd=\initramfs-linux-lts.img'

For getting a list with the boot entries, setting the boot order or removing them, see efibootmgr.

## bcfg
Some UEFI implementations make it difficult to modify the NVRAM successfully using efibootmgr. If efibootmgr cannot successfully create an entry, you can use the bcfg command in UEFI Shell v2 (i.e., from the Arch Linux live iso).

First, find out the device number where your ESP resides with:

 Shell> map

In this example,  is used as the device number. To list the contents of the ESP:

 Shell> ls FS1:

To view the current boot entries:

 Shell> bcfg boot dump

To add an entry for your kernel, use:

 Shell> bcfg boot add N FS1:\vmlinuz-linux "Arch Linux"

Where  is the location where the entry will be added in the boot menu. 0 is the first menu item. Menu items already existing will be shifted in the menu without being discarded.

You can add kernel options directly:

 Shell> bcfg boot -opt N "root=/dev/sda2 initrd=\initramfs-linux.img"

Or by creating a file on your ESP:

 Shell> edit FS1:\options.txt

In the file, add the boot line. For example:

 root=/dev/sda2 rw initrd=\initramfs-linux.img

Press  to save and then  to exit.

Add these options to your previous entry:

 Shell> bcfg boot -opt N FS1:\options.txt

Repeat this process for any additional entries.

To remove a previously added item do:

 Shell> bcfg boot rm N

## Using UEFI Shell
If you do not want to create a permanent boot entry it is possible to launch the kernel from UEFI Shell since it is a normal UEFI application:

 > FS0:
 > \vmlinuz-linux root=PARTUUID=3518bb68-d01e-45c9-b973-0b5d918aae96 rw initrd=\initramfs-linux.img

In this case, the kernel parameters are passed as normal parameters to the EFI boot stub kernel.

To avoid needing to remember all of your kernel parameters every time, you can save the executable command to a shell script such as  on your EFI system partition, then run it with:

 > FS0:
 > archlinux

## Using a startup.nsh script
Some UEFI implementations do not retain EFI variables between cold boots (e.g. VirtualBox before version 6.1) and anything set through the UEFI is lost on poweroff.

The UEFI Shell Specification 2.0 establishes that a script called  at the root of the ESP partition will always be interpreted and can contain arbitrary instructions; among those you can set a bootloading line. Make sure you mount the ESP partition on  and create a  script that contains a kernel bootloading line. For example:

 vmlinuz-linux rw root=/dev/sdX [rootflags=myrootflags \
  [mymodule.flag=bar \
  initrd=\initramfs-linux.img

This method will work with almost all UEFI versions you may encounter in real hardware, you can use it as last resort. The script must be a single long line. Sections in brackets are optional and given only as a guide. Shell style linebreaks are for visual clarification only. FAT filesystems use the backslash as path separator and in this case, the backslash declares the initramfs is located in the root of the ESP partition.

## Tips and tricks
## Boot entry with fallback ramdisk
Without a boot manager, the kernel command line is not changeable at boot time. To have at least some sort of fallback possibility, e.g. to use the  and/or start without Intel microcode, simply create a further boot entry with efibootmgr, e.g. labeled "Arch Linux fallback" and the desired fallback options.

## Archiso on ESP
It is possible to put the Arch Linux ISO on the ESP to have a recovery system. As of 2025.08.01 release the size required is 1.2G.

First download archlinux-YYYY.MM.DD-x86_64.iso.

Next, create a directory for archiso in your ESP:

 # mkdir -p esp/EFI/archiso

Extract the contents of the  directory in there:

 # bsdtar -v -x --no-same-permissions --strip-components 1 -f archlinux-YYYY.MM.DD-x86_64.iso -C esp/EFI/archiso arch

In the last step, create a boot entry using . Replace the following:

 is the device path (eg. /dev/sda)

 is the partition number

 # efibootmgr --create --disk diskpath \
 --part diskpart \
 --label "Arch (rescue system)" \
 --loader '\EFI\archiso\boot\x86_64\vmlinuz-linux' \
 --unicode 'archisobasedir=/EFI/archiso archisosearchfilename=/EFI/archiso/boot/x86_64/vmlinuz-linux initrd=\EFI\archiso\boot\x86_64\initramfs-linux.img'

You can now choose the rescue system from the UEFI boot loader.

## Troubleshooting
## Changes to boot entries are not applied
Some motherboards, such as Haswell-era ASUS boards (as encountered on the french forum), will not notice changes to boot entries unless the system is booted with another pre-existing one.
