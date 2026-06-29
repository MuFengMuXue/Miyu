This page contains [[changes](https://wiki.gentoo.org/index.php?title=Install_Gentoo_on_a_bootable_USB_stick&oldid=1338272&diff=1358521)] which are not marked for translation.

Other languages:

-   [Deutsch](https://wiki.gentoo.org/wiki/Install_Gentoo_on_a_bootable_USB_stick/de "Installieren von Gentoo auf einem bootfähigen USB Stick (64% translated)")
-   [English]
-   [español](https://wiki.gentoo.org/wiki/Install_Gentoo_on_a_bootable_USB_stick/es "Install Gentoo on a bootable USB stick (100% translated)")
-   [français](https://wiki.gentoo.org/wiki/Install_Gentoo_on_a_bootable_USB_stick/fr "Installer Gentoo sur un clef USB bootable (59% translated)")
-   [magyar](https://wiki.gentoo.org/wiki/Install_Gentoo_on_a_bootable_USB_stick/hu "Gentoo rendszer telepítése bootolható USB pendrive adathordozóra (100% translated)")
-   [čeština](https://wiki.gentoo.org/wiki/Install_Gentoo_on_a_bootable_USB_stick/cs "Install Gentoo on a bootable USB stick/cs (9% translated)")
-   [русский](https://wiki.gentoo.org/wiki/Install_Gentoo_on_a_bootable_USB_stick/ru "Установка Gentoo на загрузочную USB-флэшку (46% translated)")
-   [中文（中国大陆）‎](https://wiki.gentoo.org/wiki/Install_Gentoo_on_a_bootable_USB_stick/zh-cn "将Gentoo安装在可启动的U盘上 (30% translated)")
-   [日本語](https://wiki.gentoo.org/wiki/Install_Gentoo_on_a_bootable_USB_stick/ja "Gentoo をブータブル USB メモリにインストールする (90% translated)")
-   [한국어](https://wiki.gentoo.org/wiki/Install_Gentoo_on_a_bootable_USB_stick/ko "Install Gentoo on a bootable USB stick/ko (46% translated)")

Booting **Gentoo from a USB stick** is really quite simple. Thanks to [distribution kernels](https://wiki.gentoo.org/wiki/Project:Distribution_Kernel "Project:Distribution Kernel"), the main challenge, of setting up an initial ramdisk and to include the drivers for all the machines it is going to boot, is made much easier. This article describes how to install Gentoo onto a USB stick that can be booted on any computer. This installation will be just like a regular desktop installation and changes will be persistent.

** Note**\
This article covers installation of a complete, functional Gentoo system onto a USB drive. See the [LiveUSB](https://wiki.gentoo.org/wiki/LiveUSB "LiveUSB") article for instructions on creating a simple bootable drive, that can for example be used for Gentoo installation.

** Note**\
This guide previously used [genkernel](https://wiki.gentoo.org/wiki/Genkernel "Genkernel") to prepare the kernel beforehand, this is now discouraged. Using distribution kernels, no preparation on the host is needed.

## Contents

-   [[1] [Preparing the USB stick]](#Preparing_the_USB_stick)
-   [[2] [Enable secure boot and Gentoo binhost]](#Enable_secure_boot_and_Gentoo_binhost)
-   [[3] [Kernel and essentials]](#Kernel_and_essentials)
-   [[4] [Legacy hardware]](#Legacy_hardware)
    -   [[4.1] [MBR style partitioning]](#MBR_style_partitioning)
    -   [[4.2] [Formatting]](#Formatting)
    -   [[4.3] [Bootloader]](#Bootloader)
        -   [[4.3.1] [lilo]](#lilo)
        -   [[4.3.2] [syslinux]](#syslinux)
    -   [[4.4] [fstab]](#fstab)
-   [[5] [Tips and tricks]](#Tips_and_tricks)
-   [[6] [See also]](#See_also)

## [Preparing the USB stick]

The [Handbook:AMD64/Installation/Disks#Partition_tables](https://wiki.gentoo.org/wiki/Handbook:AMD64/Installation/Disks#Partition_tables "Handbook:AMD64/Installation/Disks") section of the AMD64 Gentoo Handbook discusses different partitioning strategies.

Partition the disk as GPT unless you are going to boot the USB stick on pre-2010s hardware. At minimum you will need the EFI System Partition and a root partition. Swap is optional if your USB stick is low on space.

## [Enable secure boot and Gentoo binhost]

Mount the USB stick to /mnt/gentoo and do the following after entering the chroot.

We enable [secure boot](https://wiki.gentoo.org/wiki/Secure_boot "Secure boot") as it is used on most modern systems. The [Gentoo binhost](https://wiki.gentoo.org/wiki/Gentoo_Binary_Host_Quickstart "Gentoo Binary Host Quickstart") is also enabled as well as this greatly reduces the compilation time. Finally we set USE flags to pull in [[[sys-kernel/gentoo-kernel]](https://packages.gentoo.org/packages/sys-kernel/gentoo-kernel)[]] and GRUB as bootloader.

`(chroot) #``openssl req -new -x509 -newkey rsa:2048 -subj "/CN=Larry's Platform Key" -keyout /root/secureboot.key -out /root/secureboot.crt -days 9999 -noenc -sha256`

`(chroot) #``echo 'FEATURES="getbinpkg binpkg-request-signature"' >> /etc/portage/make.conf`

`(chroot) #``echo 'SECUREBOOT_SIGN_KEY="/root/secureboot.key"' >> /etc/portage/make.conf`

`(chroot) #``echo 'SECUREBOOT_SIGN_CERT="/root/secureboot.crt"' >> /etc/portage/make.conf`

`(chroot) #``echo 'MODULES_SIGN_KEY="/root/secureboot.key"' >> /etc/portage/make.conf`

`(chroot) #``echo 'MODULES_SIGN_CERT="/root/secureboot.crt"' >> /etc/portage/make.conf`

`(chroot) #``echo "*/* secureboot" >> /etc/portage/package.use/00-kernel`

`(chroot) #``echo "*/* dist-kernel" >> /etc/portage/package.use/00-kernel`

`(chroot) #``echo "sys-kernel/gentoo-kernel modules-sign" >> /etc/portage/package.use/00-kernel`

`(chroot) #``echo "sys-kernel/installkernel grub" >> /etc/portage/package.use/00-kernel`

Proceed with the rest of the [Gentoo handbook](https://wiki.gentoo.org/wiki/Handbook:Main_Page "Handbook:Main Page") instructions up to the page \"installing base system\".

## [Kernel and essentials]

We will install all the firmware the handbook mentions and also install [shim](https://wiki.gentoo.org/wiki/Shim "Shim"), which is needed to avoid accessing UEFI firmware to add Secure Boot keys for each PC that the USB stick will be used in.

GRUB and gentoo-kernel will also be pulled in by USE flags set in the previous section.

After installing base system:

`(chroot) #``emerge linux-firmware sof-firmware intel-microcode shim mokutil`

Install shim and GRUB to the [EFI System Partition](https://wiki.gentoo.org/wiki/EFI_System_Partition "EFI System Partition") on the USB stick. The below assumes the ESP is mounted at [/efi].

`(chroot) #``mkdir --parents /efi/EFI/BOOT`

`(chroot) #``cp /usr/share/shim/BOOTX64.EFI /efi/EFI/BOOT`

`(chroot) #``cp /usr/share/shim/mmx64.efi /efi/EFI/BOOT`

`(chroot) #``cp /usr/lib/grub/grub-x86_64.efi.signed /efi/EFI/BOOT/grubx64.efi`

`(chroot) #``cp /boot/grub/grub.cfg /efi/EFI/BOOT`

`(chroot) #``openssl x509 -inform pem -in /root/secureboot.crt -outform der -out /efi/secureboot.der`

** Note**\
Remember not to use efibootmgr to pass any parameters to shim, as they will be lost when the USB stick is used on another PC.

After reboot, shim will load and show \"Access violation\" as the secure boot certificate has not been imported into the UEFI\'s machine owner key list. Press any key to show a menu, then press \"Enroll key from disk\" and navigate to the secureboot.der file on the ESP. After enrolling the cert, select \"Reboot\" and the USB stick will load GRUB. These steps need to be done once for each PC that the stick will be used on.

## [Legacy hardware]

This section covers adaptations needed to boot the USB on pre-2010s hardware. Usually BIOS boot and MBR partitioning is required.

### [MBR style partitioning]

Create 2 partitions on the drive (assuming the installation will have a [/boot] and a [/] (root) partition). We assume that the USB stick is at [/dev/sdb] (run [dmesg] immediately after plugging in the USB stick to see which device is being used).

** Warning**\
On very small USB sticks, you may just use one root-cum-boot partition instead.

`root `[`#`]`fdisk /dev/sdb`

    Command (m for help): d
    Selected partition 1

    Command (m for help): n
    Partition type:
       p   primary (0 primary, 0 extended, 4 free)
       e   extended
    Select (default p): p
    Partition number (1-4, default 1): 1
    First sector (2048-4001759, default 2048):
    Using default value 2048
    Last sector, +sectors or +size (2048-4001759, default 4001759): +100M

    Command (m for help): n
    Partition type:
       p   primary (1 primary, 0 extended, 3 free)
       e   extended
    Select (default p): p
    Partition number (1-4, default 2):
    Using default value 2
    First sector (206848-4001759, default 206848):
    Using default value 206848
    Last sector, +sectors or +size (206848-4001759, default 4001759):
    Using default value 4001759

    Command (m for help): a
    Partition number (1-4): 1

    Command (m for help): p

    Disk /dev/sdb: 2048 MB, 2048901120 bytes
    255 heads, 63 sectors/track, 249 cylinders, total 4001760 sectors
    Units = sectors of 1 * 512 = 512 bytes
    Sector size (logical/physical): 512 bytes / 512 bytes
    I/O size (minimum/optimal): 512 bytes / 512 bytes
    Disk identifier: 0x001663df

       Device Boot      Start         End      Blocks   Id  System
    /dev/sdb1   *        2048      206847      102400   83  Linux
    /dev/sdb2          206848     4001759     1897456   83  Linux

    Command (m for help): w
    The partition table has been altered!

    Calling ioctl() to re-read partition table.
    Syncing disks.

Make sure that the first partition is bootable (`a` command toggles the boot flag).

### [Formatting]

Now format the new partitions. In the example we use the ext4 file system but another file system for the [/] partition can be used if it is supported in the kernel. Notice that during the formatting operation, a label is assigned to the partitions. This is important because it will be how the root file system is detected later as the USB stick can be booted on systems where the drive letter allocation is completely different.

`root `[`#`]`mkfs.ext4 -L GENTOO_USB_BOOT /dev/sdb1 `

`root `[`#`]`mkfs.ext4 -L GENTOO_USB_ROOT /dev/sdb2`

### [Bootloader]

In order to boot the new system, install a bootloader on the USB stick.

The below sections give example configurations for either using [GRUB](https://wiki.gentoo.org/wiki/GRUB "GRUB") or using [lilo](https://wiki.gentoo.org/wiki/LILO "LILO") together with [syslinux](https://wiki.gentoo.org/wiki/Syslinux "Syslinux").

#### [lilo]

Emerge [lilo](https://wiki.gentoo.org/wiki/LILO "LILO") (from within the chroot):

`(chroot) #``emerge sys-boot/lilo`

Edit [etc/lilo.conf] so that it has the correct information in it.

** Warning**\
These settings are very important and will be discussed line by line.

[FILE] **`/etc/lilo.conf`Configure lilo.conf**

    boot=/dev/sdb              # The location of the USB Stick (currently)
    lba32                      # use lba32 addressing (ignore)
    compact                    # boot quickly by loading lots of blocks
                               # remove when there are problems with booting
    prompt                     # Prompt for user input
    timeout=20                 # Time to wait before default selection
    default="Gentoo-352"       # Default selection after timeout

    image=/boot/vmlinuz-5.10.76-gentoo-r1-x86_64
        label="Gentoo-352"
        read-only
        root=/dev/ram0
        append="root=LABEL=GENTOO_USB_ROOT scandelay=5"
        initrd=/boot/initramfs-5.10.76-gentoo-r1-x86_64.img

The lines after image are all easy but the append line contains some interesting options.

-   `root=LABEL=GENTOO_USB_ROOT` will use the label of the disk instead of [/dev/sdb2] which is important because these device numbers move around depending on the number of hard disks in the computer or number of USB disk drives.
-   Also important for USB booting is the `scandelay` option, as USB devices need a little time to be detected by the kernel; that is what this option is for. When there are lots of modules booting takes a long time so it probably does not matter, but if there are only a few modules loaded then it is important, because the system could have booted before the kernel detects the USB device. Also, on newer machines with USB3 controllers it is necessary to add the `xhci_hcd` driver (built into the kernel or as a module).

Now install LILO (with the configuration) on the USB stick:

`(chroot) #``lilo`

    Warning: /dev/sdb is not on the first disk
    Warning: The initial RAM disk is too big to fit between the kernel and
       the 15M-16M memory hole.  It will be loaded in the highest memory as
       though the configuration file specified "large-memory" and it will
       be assumed that the BIOS supports memory moves above 16M.
    Added Gentoo-352 ? *
    2 warnings were issued.

The first warning is to be expected as we are not installing the boot loader onto the hard disk in the computer. The second warning will only cause a problem on machines that are old; if it is a problem try cutting down the kernel by removing modules.

#### [syslinux]

** Warning**\
syslinux currently only works with ext, btrfs, ntfs and fat filesystems.

`(chroot) #``emerge syslinux`

Put the boot sector onto the USB stick.

`(chroot) #``dd bs=440 count=1 conv=notrunc if=/usr/share/syslinux/mbr.bin of=/dev/sdb`

Now to configure the bootloader.

`(chroot) #``mkdir /boot/syslinux`

`(chroot) #``nano -w /boot/syslinux/syslinux.cfg`

[FILE] **`/boot/syslinux/syslinux.cfg`**

    PROMPT 1
    TIMEOUT 50
    DEFAULT gentoo

    LABEL gentoo
            LINUX ../vmlinuz-5.10.76-gentoo-r1-x86_64
            APPEND root=LABEL=GENTOO_USB_ROOT scandelay=3 ro
            INITRD ../initramfs-5.10.76-gentoo-r1-x86_64.img

** Note**\
The `ro` in the above `APPEND` line will cause the root partition to be mounted read-only (which is usually preferred on USB sticks). Replace `ro` with `rw` to allow the system to be modified from the boot onwards (instead of having the user mount the file system as read-write later).

Next install syslinux onto the USB stick. The `--device /dev/sdb1` option is not absolutely necessary though.

`(chroot) #``extlinux --device /dev/sdb1 --install /boot/syslinux`

### [fstab]

[FILE] **`/etc/fstab`Configure the fstab file to work with labels**

    LABEL=GENTOO_USB_BOOT   /boot           ext4            noauto,noatime  1 2
    LABEL=GENTOO_USB_ROOT   /               ext4            noatime         0 1

## [Tips and tricks]

Although it is possible to use the system just made as a standard Gentoo system, it might be worthwhile to compile binary packages on a host and then installing them on the USB stick. Or if the system has enough memory just mount [/var/tmp] to a tmpfs, as compilation will be much quicker that way anyway!

## [See also]

-   [Installation](https://wiki.gentoo.org/wiki/Installation "Installation") --- an overview of the principles and practices of installing Gentoo on a running system.
-   [LiveUSB](https://wiki.gentoo.org/wiki/LiveUSB "LiveUSB") --- explains how to create a *Gentoo LiveUSB* or, in other words, how to emulate a **[x86]** or **[amd64]** Gentoo LiveCD using a USB drive.