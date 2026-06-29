# Install Arch Linux on a removable medium

This page explains how to perform a regular Arch installation onto removable media (e.g. a USB flash drive). In contrast to having a LiveUSB as covered in USB flash installation medium, the result will be a persistent installation identical to one on an internal drive.

## Installation
There are various ways of installing Arch on removable media, depending on the operating system you have available:

* If you have another Linux computer available (it does not need to be Arch), you can follow the instructions at Install from existing Linux.
* An Arch Linux CD/USB can be used to install Arch onto the removable medium, via booting the CD/USB and following the installation guide. If booting from a Live USB, the installation cannot be made to the same removable medium you are booting from.
* If you run Windows or macOS, download VirtualBox, install VirtualBox Extensions, attach your removable medium to a virtual machine running Linux (either already installed or via a live ISO), and point the installation into the now attached drive while using the instructions at the Installation guide.
* It is possible to install Arch on the same USB drive that you are trying to install it from. However, you cannot shut down your machine or reboot in the middle of the installation process. If you do that, you would need to create the installation media again.

## Installation tweaks
* Before creating the initial RAM disk, in  move the  and  hooks before the  hook. This is necessary to allow booting on multiple systems each requiring different modules in early userspace.
* If you have chosen to install Arch onto a USB mass storage device and want to be able to continue to use it as a cross-platform removable drive, this can be accomplished by creating a partition housing an appropriate file system (most likely NTFS or exFAT). Note that the data partition may need to be the first partition on the device, as Windows assumes that there can only be one partition on a removable device, and will happily automount an EFI system partition otherwise. Remember to install  and . Some tools are available online that may allow you to flip the Removable Medium Bit (RMB) on your USB mass storage device. This would trick operating systems into treating your USB mass storage device as an external hard disk and allow you to use whichever partitioning scheme you choose.
* If your Arch installation is on a removable drive that needs to have microcode for both manufacturer processors, install both  and  packages. See Microcode#Loading microcode.
* If you generate entries for the fstab file, keep only those related to the removable medium, otherwise the system might take a very long time to boot due to attempts to find non-existent devices.

## Boot loader configuration
## GRUB
Follow the instructions on GRUB#BIOS systems and GRUB#UEFI systems to install GRUB for both BIOS and UEFI booting:

 # grub-install --target=i386-pc /dev/sdX --recheck
 # grub-install --target=x86_64-efi --efi-directory=esp --removable --recheck

## Syslinux
Using your UUID:

 LABEL Arch
         MENU LABEL Arch Linux
         LINUX ../vmlinuz-linux
         APPEND root=UUID=3a9f8929-627b-4667-9db4-388c4eaaf9fa rw
         INITRD ../initramfs-linux.img

## rEFInd
 menuentry "Arch Linux" {
    icon     /EFI/BOOT/icons/os_arch.png
    volume   5028fa50-0079-4c40-b240-abfaf28693ea
    loader   /path/to/vmlinux_image
    initrd   /path/to/initramfs
    options  "root=PARTUUID=5028fa50-0079-4c40-b240-abfaf28693ea rw"
 }

See rEFInd#For manual boot stanzas for details on creating manual boot stanzas.

You must also use the  argument when installing rEFInd.

## Tips and tricks
## Using your portable install on multiple machines
## Video drivers
To support most common GPUs, install , , , .

## Audio drivers
To support most common sound cards, install  and . For more information about configuring audio device, see Advanced Linux Sound Architecture.

## Persistent block device naming
It is recommended to use UUID in both fstab and boot loader configuration. See Persistent block device naming for details.

Alternatively, you may create udev rule to create custom symlink for your disk. Then use this symlink in fstab and boot loader configuration. See udev#Setting static device names for details.

## Kernel parameters
You may want to disable KMS for various reasons, such as getting a blank screen or a "no signal" error from the display, when using some Intel video cards, etc. To disable KMS, add  as a kernel parameter. See Kernel parameters for more info.

## Compatibility
The fallback image should be used for maximum compatibility.

## Minimizing disk access
When installing to a device that offers a limited number of writes before it wears out, such as a USB drive, SD card, or similar, reduce the number of writes to increase the device lifetime. This also reduces the performance impact of slow writes.

* It is highly recommended to review the Improving performance#Reduce disk reads/writes article prior to selecting a file system. To sum it up, for flash-based media such as USB flash drives or SD cards, ext4 without a journal should be fine, which can be created with . The obvious drawback of using a file system with journaling disabled is data loss as a result of an ungraceful dismount. Recognize that flash has a limited number of writes, and a journaling file system will take some of these as the journal is updated. For this same reason, it is best to forget the swap partition. Note that this does not affect installing onto a portable hard drive.
* You may want to configure systemd journal to store its journals in RAM, e.g. by creating a custom configuration file:

* To disable  and related system calls in web browsers and other applications that do not write essential data, use the  command from  to avoid such system calls:

 $ eatmydata firefox

## UI responsiveness
You might encounter UI freezes on high I/O load especially on slow drives. Improving performance#Changing I/O scheduler or switching to a kernel which uses a different default scheduler can drastically affect your UI responsiveness. For example BFQ can improve UI responsiveness which is default on .

See Improving performance#The scheduling algorithms for more info.
