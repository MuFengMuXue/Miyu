## Contents

-   [[1] [Setup some environment variables]](#Setup_some_environment_variables)
-   [[2] [Partition SD card and format partitions]](#Partition_SD_card_and_format_partitions)
    -   [[2.1] [Partition SD card]](#Partition_SD_card)
    -   [[2.2] [Format partitions]](#Format_partitions)
-   [[3] [Install base system and Gentoo repository snapshot]](#Install_base_system_and_Gentoo_repository_snapshot)
    -   [[3.1] [Mount root partition]](#Mount_root_partition)
    -   [[3.2] [Install stage3]](#Install_stage3)
    -   [[3.3] [Install Gentoo repository snapshot]](#Install_Gentoo_repository_snapshot)
-   [[4] [Install kernel, modules and firmware]](#Install_kernel.2C_modules_and_firmware)
    -   [[4.1] [Install kernel]](#Install_kernel)
    -   [[4.2] [Install modules]](#Install_modules)
    -   [[4.3] [Firmware]](#Firmware)
        -   [[4.3.1] [WIFI]](#WIFI)
        -   [[4.3.2] [Bluetooth]](#Bluetooth)
-   [[5] [Setting up wifi]](#Setting_up_wifi)
    -   [[5.1] [Command to install NetworkManager]](#Command_to_install_NetworkManager)
    -   [[5.2] [Command to download cache files for NetworkManager]](#Command_to_download_cache_files_for_NetworkManager)
-   [[6] [Ready to use]](#Ready_to_use)
    -   [[6.1] [xorg.conf]](#xorg.conf)
    -   [[6.2] [fstab]](#fstab)
    -   [[6.3] [shadow file]](#shadow_file)
    -   [[6.4] [inittab]](#inittab)
    -   [[6.5] [Unmount all partitions]](#Unmount_all_partitions)
    -   [[6.6] [Enjoy Gentoo]](#Enjoy_Gentoo)

## [Setup some environment variables]

These will come in handy when copying commands

`root `[`#`]`WORK=/root `

`root `[`#`]`DISK=/dev/sda `

`root `[`#`]`DEST=/mnt/gentoo `

\

## [Partition SD card and format partitions]

### [Partition SD card]

Normally 3 partitions are needed here: boot, swap and root. If you decide to use swap as a file, then 2 partitions are needed. In this example, we use swap as a partition.

1\. Start partitioning SD card

`root `[`#`]`fdisk $DISK`

    Welcome to fdisk (util-linux 2.38.1).
    Changes will remain in memory only, until you decide to write them.
    Be careful before using the write command.

2\. Create a DOS label

    Command (m for help): o
    Created a new DOS disklabel with disk identifier 0x4fe0c75b.

3\. Create boot partition

    Command (m for help): n
    Partition type
       p   primary (0 primary, 0 extended, 4 free)
       e   extended (container for logical partitions)
    Select (default p): p
    Partition number (1-4, default 1): 1
    First sector (2048-124735487, default 2048):
    Last sector, +/-sectors or +/-size (2048-124735487, default 124735487): +256M

    Created a new partition 1 of type 'Linux' and of size 256 MiB.

4\. Create swap partition

    Command (m for help): n
    Partition type
       p   primary (1 primary, 0 extended, 3 free)
       e   extended (container for logical partitions)
    Select (default p): p
    Partition number (2-4, default 2):
    First sector (526336-124735487, default 526336):
    Last sector, +/-sectors or +/-size (526336-124735487, default 124735487): +8G

    Created a new partition 2 of type 'Linux' and of size 8 GiB.

5\. Create root partition

    Command (m for help): n
    Partition type
       p   primary (2 primary, 0 extended, 2 free)
       e   extended (container for logical partitions)
    Select (default p):

    Using default response p.
    Partition number (3,4, default 3):
    First sector (17303552-124735487, default 17303552):
    Last sector, +/-sectors or +/-size (17303552-124735487, default 124735487):

    Created a new partition 3 of type 'Linux' and of size 51.2 GiB.

6\. Set the file system for boot partition. To boot raspberry pi, boot partition has to be FAT.

    Command (m for help): t
    Partition number (1-3, default 3): 1
    Hex code or alias (type L to list all): 0b

    Changed type of partition 'Linux' to 'W95 FAT32'.

7\. Set the file system for swap partition.

    Command (m for help): t
    Partition number (1-3, default 3): 2
    Hex code or alias (type L to list all): 82

    Changed type of partition 'Linux' to 'Linux swap / Solaris'.

8\. Set the file system for root partition.

    Command (m for help): t
    Partition number (1-3, default 3):
    Hex code or alias (type L to list all): 83

    Changed type of partition 'Linux' to 'Linux'.

9\. Final check of the partitions

    Command (m for help): p
    Disk /dev/sda: 59.48 GiB, 63864569856 bytes, 124735488 sectors
    Disk model: Storage Device
    Units: sectors of 1 * 512 = 512 bytes
    Sector size (logical/physical): 512 bytes / 512 bytes
    I/O size (minimum/optimal): 512 bytes / 512 bytes
    Disklabel type: dos
    Disk identifier: 0x4fe0c75b

    Device     Boot    Start       End   Sectors  Size Id Type
    /dev/sda1           2048    526335    524288  256M  b W95 FAT32
    /dev/sda2         526336  17303551  16777216    8G 82 Linux swap / Solaris
    /dev/sda3       17303552 124735487 107431936 51.2G 83 Linux

10\. Write changes to SD card.

    Command (m for help): w
    The partition table has been altered.
    Calling ioctl() to re-read partition table.
    Syncing disks.

### [Format partitions]

1\. boot partition

`root `[`#`]`mkfs -t vfat $1`

    mkfs.fat 4.2 (2021-01-31)

2\. swap partition

`root `[`#`]`mkswap --pagesize 16384 $2`

    mkswap: Using user-specified page size 16384, instead of the system value 4096
    Setting up swapspace version 1, size = 8 GiB (8589918208 bytes)
    no label, UUID=1c5c3570-8437-431f-b737-7d1e24d8d1b7

3\. root partition

`root `[`#`]`mkfs -t ext4 $3`

    mke2fs 1.47.0 (5-Feb-2023)
    Creating filesystem with 13428992 4k blocks and 3358720 inodes
    Filesystem UUID: b9aefb9c-0c70-49df-b236-95783f17d190
    Superblock backups stored on blocks:
        32768, 98304, 163840, 229376, 294912, 819200, 884736, 1605632, 2654208,
        4096000, 7962624, 11239424

    Allocating group tables: done
    Writing inode tables: done
    Creating journal (65536 blocks): done
    Writing superblocks and filesystem accounting information: done

## [Install base system and Gentoo repository snapshot]

### [Mount root partition]

`root `[`#`]`mount $3 $DEST`

### [Install stage3]

1\. Download latest stage 3 tar file

2\. Untar stage file

`root `[`#`]`tar xpf $/stage3-arm64-openrc-20240107T211819Z.tar.xz --xattrs-include='*.*' --numeric-owner -C $/`

### [Install Gentoo repository snapshot]

1\. Download latest Gentoo repository snapshot

2\. Untar stage file

`root `[`#`]`mkdir -p $/var/db/repos/gentoo`

`root `[`#`]`tar xpf $/gentoo-latest.tar.bz2 --strip-components=1 -C $/var/db/repos/gentoo`

## [][Install kernel, modules and firmware]

** Warning**\
Upstream kernel and firmware versions tagged **20240306** are the minimum required to boot the **Raspberry Pi 5**. At the time of this writing this version is not available in Portage; [[[bug #930269]](https://bugs.gentoo.org/show_bug.cgi?id=930269)[]] has been filed to get this addressed. This is why it is necessary to git clone kernel sources and firmware directly from the upstream project.

** Note**\
If you get an error to the effect of ***bcm2712-rpi-5b.dtb*** *not found* at boot time with a **Raspberry Pi 5**. You have failed to heed the above warning.

### [Install kernel]

There are 2 ways to install the kernel for Raspberry Pi 5, use the pre-built kernel and compile from source code. In this example, we will use the pre-built kernel.

1\. Clone raspberry-firmware repository.

`root `[`#`]`git clone --depth=1 `[`https://github.com/raspberrypi/firmware.git`](https://github.com/raspberrypi/firmware.git)

2\. To boot raspberry pi, a few files from boot folder are needed. Make sure you have copied the following files from firmware/boot to /mnt/gentoo/boot

`root `[`#`]`mount $1 $/boot `

`root `[`#`]`cp $/firmware/boot/bcm2712-rpi-5-b.dtb $/boot/ `

`root `[`#`]`cp $/firmware/boot/kernel_2712.img $/boot/ `

`root `[`#`]`cp -r $/firmware/boot/overlays $/boot/`

3\. Config boot loader

Unlike grub or other boot loader, raspberry pi looks for cmdline.txt from /boot to boot the operating system. Put below content into /mnt/gentoo/boot/cmdline.txt

    dwc_otg.lpm_enable=0 console=tty1 root=/dev/mmcblk0p3 rootfstype=ext4 rootwait

4\. Config.txt

config.txt is needed configure raspberry pi to use correct drivers. Put below content into /mnt/gentoo/boot/config.txt

    # have a properly sized image
    disable_overscan=1

    # Enable audio (loads snd_bcm2835)
    dtparam=audio=on

    # Enable DRM VC4 V3D driver
    dtoverlay=vc4-kms-v3d-pi5

### [Install modules]

[https://github.com/raspberrypi/firmware](https://github.com/raspberrypi/firmware) comes with all the modules we need, just copy modules into /mnt/gentoo/lib/

`root `[`#`]`cp -r $/firmware/modules $/lib/`

### [Firmware]

To use WIFI and bluetooth, we need to copy the firmware to /mnt/gentoo/lib/firmware folder.

#### [WIFI]

1\. Clone wifi firmware repository

`root `[`#`]`git clone --depth=1 `[`https://github.com/RPi-Distro/firmware-nonfree.git`](https://github.com/RPi-Distro/firmware-nonfree.git)

2\. Create /mnt/gentoo/lib/firmware/brcm if it doesn\'t exist

`root `[`#`]`mkdir -p $/lib/firmware/brcm`

3\. The wifi mode for raspberry pi 5 is brcmfmc43455, so we only need to copy files for brcmfmc43455.

`root `[`#`]`cp $/firmware-nonfree/debian/config/brcm80211/cypress/cyfmac43455-sdio-standard.bin $/lib/firmware/brcm/ `

`root `[`#`]`cp $/firmware-nonfree/debian/config/brcm80211/cypress/cyfmac43455-sdio.clm_blob $/lib/firmware/brcm/ `

`root `[`#`]`cp $/firmware-nonfree/debian/config/brcm80211/brcm/brcmfmac43455-sdio.txt $/lib/firmware/brcm/`

4\. When raspberry pi 5 boots, it looks for firmware names with model name (like raspberrypi,5-model-b), so we need to create symlinks for the firmware files:

`root `[`#`]`cd $/lib/firmware/brcm/ `

`root `[`#`]`ln -s cyfmac43455-sdio-standard.bin brcmfmac43455-sdio.raspberrypi,5-model-b.bin `

`root `[`#`]`ln -s cyfmac43455-sdio.clm_blob brcmfmac43455-sdio.raspberrypi,5-model-b.clm_blob `

`root `[`#`]`ln -s brcmfmac43455-sdio.txt brcmfmac43455-sdio.raspberrypi,5-model-b.txt `

`root `[`#`]`cd $WORK`

These should now read as:

`root `[`#`]`ls -l $/lib/firmware/brcm/`

    lrwxrwxrwx 1 root root     22 Jan 21 12:23 brcmfmac43455-sdio.raspberrypi,5-model-b.bin -> cyfmac43455-sdio-standard.bin
    lrwxrwxrwx 1 root root     27 Jan 21 12:23 brcmfmac43455-sdio.raspberrypi,5-model-b.clm_blob -> cyfmac43455-sdio.clm_blob
    lrwxrwxrwx 1 root root     22 Jan 21 12:24 brcmfmac43455-sdio.raspberrypi,5-model-b.txt -> brcmfmac43455-sdio.txt
    -rw-r--r-- 1 root root   2074 Jan 21 12:19 brcmfmac43455-sdio.txt
    -rw-r--r-- 1 root root 643651 Jan 21 12:20 cyfmac43455-sdio-standard.bin
    -rw-r--r-- 1 root root   2676 Jan 21 12:18 cyfmac43455-sdio.clm_blob

\

#### [Bluetooth]

1\. Clone bluetooth firmware repository

`root `[`#`]`git clone --depth=1 `[`https://github.com/RPi-Distro/bluez-firmware.git`](https://github.com/RPi-Distro/bluez-firmware.git)

2\. Create /mnt/gentoo/lib/firmware/brcm if it doesn\'t exist

`root `[`#`]`mkdir -p $/lib/firmware/brcm`

3\. For bluetooth, only BCM4345C0.hcd is needed.

`root `[`#`]`cp $/bluez-firmware/debian/firmware/broadcom/BCM4345C0.hcd $/lib/firmware/brcm/`

4\. Similarly, we need to create a symbolink for raspberry pi 5.

`root `[`#`]`cd $/lib/firmware/brcm/ `

`root `[`#`]`ln -s BCM4345C0.hcd BCM4345C0.raspberrypi,5-model-b.hcd `

`root `[`#`]`cd $WORK`

## [Setting up wifi]

To use wifi, a network tool such as [NetworkManager](https://wiki.gentoo.org/wiki/NetworkManager "NetworkManager") or [wpa_supplicant](https://wiki.gentoo.org/wiki/Wpa_supplicant "Wpa supplicant") is needed.

-   If you have an ethernet cable, you can finish this tutorial and use `emerge` on the Raspberry Pi.
-   If you don\'t have ethernet, you can download all the necessary files to `/mnt/gentoo/var/cache/distfiles` and emerge them on the Raspberry Pi.

### [Command to install NetworkManager]

`root `[`#`]`USE="-modemmanager -ppp -gtk-doc -introspection -concheck" emerge networkmanager`

### [Command to download cache files for NetworkManager]

`root `[`#`]`USE="-modemmanager -ppp -gtk-doc -introspection -concheck" emerge -pf networkmanager`

## [Ready to use]

Before we boot Gentoo on raspberry pi, there are a few things we need to set up.

### [xorg.conf]

If intending to use X11 for video, edit (or create) the file /mnt/gentoo/usr/share/X11/xorg.conf.d/99-rpi5.conf to contain the following

    Section "OutputClass"
        Identifier "vc4"
        MatchDriver "vc4"
        Driver "modesetting"
        Option "PrimaryGPU" "true"
    EndSection

    Section "Device"
        Identifier "kms"
        Driver "modesetting"
        Option "AccelMethod" "msdri3"
        Option "UseGammaLUT" "off"
    EndSection

### [fstab]

Make sure you have below content on [/mnt/gentoo/etc/fstab]

    /dev/mmcblk0p1          /boot           vfat            noatime,noauto,nodev,nosuid,noexec    1 2
    /dev/mmcblk0p2          swap            swap            defaults                                0 0
    /dev/mmcblk0p3          /               ext4            noatime                                 0 0

### [shadow file]

Before we can log into raspberry pi, we need to change the password of root user. Below is the password raspberry, replace this with the first line of [/mnt/gentoo/etc/shadow] file, make sure you only have one line for root user.

    root:$6$xxPVR/Td5iP$/7Asdgq0ux2sgNkklnndcG4g3493kUYfrrdenBXjxBxEsoLneJpDAwOyX/kkpFB4pU5dlhHEyN0SK4eh/WpmO0::0:99999:7:::

### [inittab]

[/mnt/gentoo/etc/inittab] needs to updated, the following line should be commented.

    f0:12345:respawn:/sbin/agetty 9600 ttyAMA0 vt100

### [Unmount all partitions]

`root `[`#`]`cd && umount $/ `

### [Enjoy Gentoo]

Plug the SD card into raspberry pi and enjoy!