# Netboot

Netboot images are small (< 1 MiB) images that can be used to download the latest Arch Linux release on the fly upon system boot. It is unnecessary to update the netboot image, the newest release will be available automatically. Netboot images can be downloaded from the Arch Linux Netboot page.

## BIOS
To use netboot on a BIOS-based computer, you need either the  or  image.

## Using ipxe.lkrn
The  image can be booted like a Linux kernel. Any Linux boot loader (like GRUB or Syslinux) can be used to load it from your hard drive, a CD or a USB drive. For example, the Syslinux wiki gives instructions to installand configure[https://wiki.syslinux.org/wiki/index.php?title=Config Syslinux on a bootable medium.

You can make flash drive that boots  with the following steps:

* Find out your device path using lsblk. Let us assume it is .
* Create MBR partition table on the device.
* Create a primary partition with FAT32 file system and flag it as active.
* Mount partition, create  directory there and copy  to the  directory.

 # mount /dev/sdc /mnt
 # mkdir -p /mnt/boot/syslinux
 # cp ipxe.lkrn /mnt/boot

* Create syslinux configuration

* Unmount partition

 # umount /mnt

* Install Syslinux MBR and Syslinux itself

 # dd bs=440 count=1 conv=notrunc if=/usr/lib/syslinux/bios/mbr.bin of=/dev/sdc
 # syslinux --directory /boot/syslinux/ --install /dev/sdc1

* Now you should be able to boot your usb stick with ipxe.lkrn.

Alternatively, you can also try the image with QEMU by running the following command:

 $ qemu-system-x86_64 -enable-kvm -m 2G -kernel ipxe.lkrn

## Using ipxe.pxe
The  image is a PXE image. It can be chainloaded from an existing PXE environment. This allows configuring a DHCP server such that booting from the network will always boot into Arch Linux netboot.

Alternatively, you can also chainload it from existing pxe loader such as pxelinux. This is a menu entry example:

 LABEL arch_netboot_chain
   COM32 pxechn.c32
   APPEND ipxe.a56af4e6a9a9.pxe

For this example to work you must have pxechn.c32 copied to the directory where your pxelinux.0 resides.

## UEFI
The ipxe-arch.efi image can be used to launch Arch Linux netboot in UEFI mode. Only 64-bit UEFI is supported. The image can be added as a boot option via efibootmgr, launched from a boot manager, like systemd-boot or rEFInd, or directly from the UEFI shell. You can also boot it from a standalone USB stick on UEFI systems.

## Installation with efibootmgr
First install the  package. Assuming your EFI system partition (ESP) is  and mounted under , you should move it as follows—let us also give it a more friendly name:

 # mkdir esp/EFI/arch_netboot
 # mv ipxe.*.efi esp/EFI/arch_netboot/arch_netboot.efi

Then you can create a boot entry as follows:

 # efibootmgr --create --disk /dev/sdd --part 1 --loader /EFI/arch_netboot/arch_netboot.efi --label "Arch Linux Netboot" --unicode

## Boot from a USB flash drive
If you want to boot the Netboot EFI binary from a USB flash drive, copy it to the default/fallback boot path () on a FAT formatted partition. It does not require creating a EFI system partition on the drive as all UEFI will happily boot any FAT volume from USB flash drives. The most compatible setup would be using the MBR partition table with a single active (bootable) primary partition of type  "W95 FAT32 (LBA)".https://lists.gnu.org/archive/html/grub-devel/2019-05/msg00063.html

The image should be then loaded automatically by UEFI systems.

## In GNU/Linux
For example, assuming  as the flash drive, prepare the USB flash drive as follows:

# If not done yet, create a partition table on  and a partition () on the device.
# If not done yet, format the partition to FAT32:
# Mount the file system:
# Create a  directory on the mounted file system:
# Copy  to the default boot path for x64 UEFI:
# Unmount the file system.

## In Windows
Prepare the USB flash drive as follows:

# If not done yet, partition the USB flash drive and format it to FAT32.
# Navigate to the root of the USB flash drive and create an  folder in it and a  folder inside the  folder.
# Copy  to the  folder.
# Rename the  file to .
# Eject the USB flash drive when done.

## Troubleshooting
## Booting EFI binary gives "device error"
If booting the EFI binary results in , make sure the network stack is enabled in your UEFI settings. It may require initializing the network interface controller's (NIC) option ROM, so additionally look for settings like "OnBoard LAN Boot ROM", "Launch PXE OpROM Policy" or similar.
