Other languages:

-   [Deutsch](https://wiki.gentoo.org/wiki/BIOS_Update/de "Aktualisierung des BIOS (49% translated)")
-   [English]
-   [español](https://wiki.gentoo.org/wiki/BIOS_Update/es "Actualización de BIOS (72% translated)")
-   [français](https://wiki.gentoo.org/wiki/BIOS_Update/fr "Mise à jour du BIOS (78% translated)")
-   [italiano](https://wiki.gentoo.org/wiki/BIOS_Update/it "Aggiornamento del BIOS (74% translated)")
-   [magyar](https://wiki.gentoo.org/wiki/BIOS_Update/hu "BIOS frissítés (100% translated)")
-   [polski](https://wiki.gentoo.org/wiki/BIOS_Update/pl "BIOS Update/pl (1% translated)")
-   [svenska](https://wiki.gentoo.org/wiki/BIOS_Update/sv "BIOS Update/sv (40% translated)")
-   [русский](https://wiki.gentoo.org/wiki/BIOS_Update/ru "Обновление BIOS (100% translated)")
-   [中文（中国大陆）‎](https://wiki.gentoo.org/wiki/BIOS_Update/zh-cn "BIOS 升级 (68% translated)")
-   [日本語](https://wiki.gentoo.org/wiki/BIOS_Update/ja "BIOS アップデート (100% translated)")
-   [한국어](https://wiki.gentoo.org/wiki/BIOS_Update/ko "BIOS Update (68% translated)")

This article describes how to apply a BIOS update on a Gentoo system.

Hardware manufactures often provide updates for [BIOS](https://wiki.gentoo.org/wiki/BIOS "BIOS") and other types of firmware. To apply (often referred to as \"flash\") the updates is sometimes not straight forward on GNU/Linux systems. This occasionally requires some extra work.

** Warning**\
If the hardware is operational there is often no need to upgrade the BIOS. If something goes wrong permanent damage may be caused to the BIOS or system firmware that may expire the hardware warranty. Proceed with caution!

** Note**\
The most prominent and widely used system has historically been the x86-based IBM PC compatible computer and its BIOS, which is why system firmware is sometimes called a BIOS even when it is not an IBM PC compatible BIOS, such as the AlphaBIOS of the DEC [Alpha](https://wiki.gentoo.org/wiki/Alpha "Alpha") architecture or the OpenBIOS, an implementation of [Open Firmware](https://wiki.gentoo.org/wiki/Open_Firmware "Open Firmware") (IEEE-1275). EFI/[UEFI](https://wiki.gentoo.org/wiki/UEFI "UEFI"), the successor of the PC BIOS, is also often called \"(U)EFI-BIOS\". Hence, the term \"BIOS update\" often refers to a system firmware update that is not really a PC BIOS.

This article focuses on the PC BIOS and early versions of its successor EFI/UEFI. On x86 (U)EFI *System Class 1* and *Class 2* have a BIOS compatible mode called \"Legacy BIOS\" or \"CSM\" (short for *Compatiblity Support Module*), which makes the UEFI behave like a PC BIOS. UEFI *System Class 3*, the standard since around 2020, no longer has a CSM.

On other firmwares the process of updating the system firmware may have similarities, but can also be completely different.

## Contents

-   [[1] [Gather firmware information]](#Gather_firmware_information)
-   [[2] [BIOS option]](#BIOS_option)
-   [[3] [Boot-CD]](#Boot-CD)
-   [[4] [FreeDOS environment]](#FreeDOS_environment)
    -   [[4.1] [Create a custom FreeDOS image]](#Create_a_custom_FreeDOS_image)
    -   [[4.2] [Using SystemRescue to boot FreeDOS]](#Using_SystemRescue_to_boot_FreeDOS)
        -   [[4.2.1] [Download SystemRescue and prepare LiveUSB]](#Download_SystemRescue_and_prepare_LiveUSB)
        -   [[4.2.2] [Create a bootable memory stick]](#Create_a_bootable_memory_stick)
        -   [[4.2.3] [Replace the FreeDOS image]](#Replace_the_FreeDOS_image)
    -   [[4.3] [Booting the FreeDOS image from GRUB directly]](#Booting_the_FreeDOS_image_from_GRUB_directly)
    -   [[4.4] [BIOS update]](#BIOS_update)
-   [[5] [Flashrom]](#Flashrom)
-   [[6] [UEFI Firmware Capsule]](#UEFI_Firmware_Capsule)
-   [[7] [See also]](#See_also)
-   [[8] [References]](#References)

## [Gather firmware information]

First find the motherboard\'s manufacturer and the model. Check the user manual that came with the system. Most of the needed information can be found in the user manual.

The [dmidecode](https://wiki.gentoo.org/wiki/Dmidecode "Dmidecode") package can be used to retrieve additional information on system hardware. [dmidecode] looks at the motherboard\'s DMI table in order to provide richer details about the firmware and hardware components.

`root `[`#`]`dmidecode -t bios -t baseboard`

Lastly, if physical access to the motherboard is possible, the required information may be found directly on the motherboard itself.

** Warning**\
Accessing the motherboard of a computer may cause loss of warranty!

After searching for the manufacturer\'s firmware update, proceed to download the package necessary to update the hardware. It is normal for a manufacturer to store firmware update packages in .zip, .exe, or .iso format.

`user `[`$`]`unzip 7235v1A.zip `

    Archive:  7235v1A.zip
       creating: 7235v1A/
    inflating: 7235v1A/7235v1x.txt
    inflating: 7235v1A/AWFL865.EXE
    inflating: 7235v1A/How to flash the BIOS.DOC
    inflating: 7235v1A/W7235IMS.1A0

## [BIOS option]

Many BIOSes have an option to read the new binary image from an external storage medium or from an internal disk. Enter the BIOS setup and look for the option. If the BIOS does not support this, continue with the next section.

## [Boot-CD]

Often the manufacturer offers a CD-ROM image to download as a boot medium. The file should have an [.iso] file extension which should be properly burned to an empty CD-R(W). One of the tools that supports this is [cdrecord] from [[[app-cdr/cdrtools]](https://packages.gentoo.org/packages/app-cdr/cdrtools)[]] package:

`root `[`#`]`cdrecord BOOT-CD.iso`

Choose from the BIOS boot menu to boot from CD and follow the instructions on the manufacturers website or in the user manual.

## [FreeDOS environment]

** Note**\
There is a convenient FreeDOS boot on the [SystemRescue](https://www.system-rescue.org/) that works well for this and will save much effort, allowing readers to skip this section. See the note at the end of the [Using SystemRescue to boot FreeDOS](https://wiki.gentoo.org/wiki/BIOS_Update#Using_SystemRescue_to_boot_FreeDOS "BIOS Update") section for details.

FreeDOS can be used to run DOS-based BIOS update utilities. A \"custom\" FreeDOS image which includes the necessary BIOS tools must be created. After the custom image has been generated, boot the image via one of the methods shown below.

Download FreeDOS and tools:

-   [FreeDOS](https://www.ibiblio.org/pub/micro/pc-stuff/freedos/files/distributions/1.0/) - Download the [fdboot.img] file.
-   [FreeDOS bootsector](https://www.ibiblio.org/pub/micro/pc-stuff/freedos/files/dos/sys/sys-freedos-linux/) - Download the [sys-freedos-linux.zip] file.
-   The DOS-Flash program and new BIOS from the manufacturers website.

### [Create a custom FreeDOS image]

First download the required software and enable the loopback device in the kernel:

[KERNEL] **enable loopback device**

    Device Drivers  --->
        [*] Block devices  --->
            <M>   Loopback device support

If the module has not been loaded use [modprobe] to load it:

`root `[`#`]`modprobe loop`

Install the required software:

`root `[`#`]`emerge --ask dev-lang/nasm app-arch/unzip sys-fs/dosfstools`

Create an image file of \~20MB using the [dd] command. The name needs to be [freedos.img] when replacing the one on the SystemRescue:

`root `[`#`]`dd if=/dev/null of=freedos.img bs=1024 seek=20480`

Write a file system to the image:

`root `[`#`]`mkfs.fat freedos.img`

Write the boot sector to the image file:

`root `[`#`]`unzip sys-freedos-linux.zip && ./sys-freedos.pl --disk=freedos.img`

Now copy the FreeDOS files to the new image.

Create the mount points:

`root `[`#`]`mkdir -p /mnt/freedos /mnt/freedos_new`

Mount the original image:

`root `[`#`]`mount -o loop fdboot.img /mnt/freedos`

Mount the new image:

`root `[`#`]`mount -o loop freedos.img /mnt/freedos_new`

Copy the FreeDOS system files to the new image:

`root `[`#`]`cp -ar /mnt/freedos/* /mnt/freedos_new/`

Now copy the flash program and the new BIOS to the image file:

`root `[`#`]`cp -ar FLASH-PROGRAM BIOS-UPDATE /mnt/freedos_new`

Unmount both images:

`root `[`#`]`umount /mnt/freedos_new /mnt/freedos`

** Note**\
DOS can only display names up to a length of 8 characters. It is a good idea to rename some of the files if their filenames are longer than this limit.

### [Using SystemRescue to boot FreeDOS]

The SystemRescue comes with a version of FreeDOS. This version can replace the original image and create a bootable memory stick which contains the needed programs to flash the firmware.

#### [Download SystemRescue and prepare LiveUSB]

-   [SystemRescue](https://www.system-rescue.org/Download/) - Download the normal ISO image.

#### [Create a bootable memory stick]

Use the default method to create the SystemRescue boot medium, the script [usb_inst.sh] will provide guidance through the installation.

** Warning**\
This will delete any data on the memory stick! Be sure all data has been properly backed up before using the memory stick for this task!

Create the folder in [/mnt]:

`root `[`#`]`mkdir /mnt/SysRescue`

Mount the CD image:

`root `[`#`]`mount -o loop systemrescue-x86-VERSION.iso /mnt/SysRescue`

Start the installation script:

`root `[`#`]`/mnt/SysRescue/usb_inst.sh`

Unmount the CD image:

`root `[`#`]`umount /mnt/SysRescue`

** Note**\
If you simply wish to update your BIOS, there is no need to tinker with the FreeDOS image on SystemRescue. After creating the bootable SystemRescue stick as described above mount the USB stick to a directory. Copy the BIOS update there. You are done! Boot on the USB stick and choose DOS tools \-\--\> FREEDOS from the SystemRescue startup menu. You will find the DOS truncated name of your BIOS update file in the A: directory. If you don\'t see it try C:. I don\'t believe this harms the SystemRescue instance on the USB stick, but if it does it is easy enough to recreate when you are done.

#### [Replace the FreeDOS image]

It is time to replace the original FreeDOS image on the SystemRescue memory stick.

Mount the SystemRescue memory stick ([/dev/sdX1] needs to be replaced by the device name of the memory stick):

`root `[`#`]`mount /dev/sdX1 /mnt/SysRescue`

Replace the [freedos.img] file:

`root `[`#`]`cp freedos.img /mnt/SysRescue/bootdisk/`

Unmount the SystemRescue memory stick:

`root `[`#`]`umount /mnt/SysRescue`

### [Booting the FreeDOS image from GRUB directly]

To boot FreeDOS without any external media use the [memdisk] tool from syslinux to allow grub (or another bootloader) to boot the FreeDOS image directly.

`root `[`#`]`emerge --ask sys-boot/syslinux`

Mount the [/boot] partition (if needed):

`root `[`#`]`mount /boot`

Copy the [memdisk] binary and the newly built FreeDOS image to [/boot]:

`root `[`#`]`cp /usr/share/syslinux/memdisk /boot`

`root `[`#`]`cp freedos.img /boot`

Edit [/boot/grub/grub.conf] and add an entry for FreeDOS:

[FILE] **`/boot/grub/grub.conf`Example grub.conf entry**

    title FreeDOS (BIOS update)
    kernel /boot/memdisk floppy
    initrd /boot/freedos.img

### [BIOS update]

Restart and choose to boot from the USB memory stick *or* the new grub entry. When using SystemRescue, in the GRUB command line type:

`freedos`

This should boot into the new FreeDOS image. The DOS prompt should appear:

`C:\>``_`

Now start the BIOS update by following the manufacturers instructions. Some useful commands in DOS:

[cd \<dir\>]

<!-- -->

[dir]

<!-- -->

[type \[drive\]\[path\]filename]

## [Flashrom]

Some motherboards can support flashing (via the [[[sys-apps/flashrom]](https://packages.gentoo.org/packages/sys-apps/flashrom)[]] package) directly from the system. In this case the only needed component is the BIOS image. Before continuing this path, first check the list of [supported hardware](https://flashrom.org/Supported_hardware).

If the hardware is supported, verify the new BIOS image:

`root `[`#`]`flashrom -v W7235IMS.1A0`

If everything checks out, then flash it:

`root `[`#`]`flashrom -vw W7235IMS.1A0`

## [UEFI Firmware Capsule]

** Note**\
Since EFI/UEFI is the successor of the PC BIOS on x86, the same tools as for BIOS updates were often used on early (U)EFI systems.

For modern UEFI, updates for the system firmware can be provided using UEFI *Capsules* (introduced with UEFI 2.0^[\[1\]](#cite_note-1)^). This method is available on Linux and Windows.^[\[2\]](#cite_note-2)^ Vendors have to provide firmware updates for the use with Linux, which, if they do, they do via the *Linux Vendor Firmware Service* (LVFS).^[\[3\]](#cite_note-3)^

Refer to [fwupd](https://wiki.gentoo.org/wiki/Fwupd "Fwupd") for further details.

## [See also]

-   [BIOS](https://wiki.gentoo.org/wiki/BIOS "BIOS") --- the standard firmware of IBM-PC-compatible computers until it was phased out in 2020.
-   [Bootable DOS USB stick](https://wiki.gentoo.org/wiki/Bootable_DOS_USB_stick "Bootable DOS USB stick") --- describes how to prepare a **bootable USB stick which loads DOS** using tools available in Gentoo.

## [References]

1.  [[[↑](#cite_ref-1)] [[https://uefi.org/sites/default/files/resources/10_Zach_AMI_capsule%20configurations.pdf](https://uefi.org/sites/default/files/resources/10_Zach_AMI_capsule%20configurations.pdf)]]
2.  [[[↑](#cite_ref-2)] [[https://uefi.org/sites/default/files/resources/UEFI%20Fall%202018%20Intel%20UEFI%20Capsules.pdf](https://uefi.org/sites/default/files/resources/UEFI%20Fall%202018%20Intel%20UEFI%20Capsules.pdf)]]
3.  [[[↑](#cite_ref-3)] [[https://fwupd.org/lvfs/devices/](https://fwupd.org/lvfs/devices/)]]