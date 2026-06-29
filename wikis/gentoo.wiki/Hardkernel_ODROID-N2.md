[] This article has been flagged for not conforming to the [wiki guidelines](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Guidelines "Gentoo Wiki:Guidelines"). Please [help Gentoo out](https://wiki.gentoo.org/wiki/Help_improve_Gentoo_by_getting_involved_with_documentation!#Make_articles_conform_to_the_guidelines "Help improve Gentoo by getting involved with documentation!") by starting fixing things.

[] The information in this article is probably **outdated**. You can help the Gentoo community by verifying and [updating this article](https://wiki.gentoo.org/index.php?title=Hardkernel_ODROID-N2&action=edit).

** Warning**\
This article is incomplete an unfinished

** Note**\
Since 5.2.0-next-20190718 mainline is bootable.

**Resources**

[[]][Specifications](https://www.hardkernel.com/blog-2/odroid-n2)

[[]][Official ORDOID-N2 wiki](https://wiki.odroid.com/odroid-n2/odroid-n2)

[[]][ODROID](https://en.wikipedia.org/wiki/ODROID "wikipedia:ODROID")

This Page describes the necessary steps to take to install gentoo with a recent mainline kernel on an [ODROID-N2](https://www.hardkernel.com/blog-2/odroid-n2/) by [Hardkernel Co., LTD.](https://www.hardkernel.com). It\'s a small ARM based single board computer with 6 cores and 2 or 4 GB of RAM. As it has a 64-bit CPU the experimental aarch64 gentoo is used.

## Contents

-   [[1] [Prerequisites]](#Prerequisites)
-   [[2] [Micro SD-Card preparation Option 1]](#Micro_SD-Card_preparation_Option_1)
    -   [[2.1] [Partition Table]](#Partition_Table)
    -   [[2.2] [Option 1 - Extract from Image]](#Option_1_-_Extract_from_Image)
    -   [[2.3] [Option 2 - Building u-boot]](#Option_2_-_Building_u-boot)
-   [[3] [USB drive Option 2]](#USB_drive_Option_2)
-   [[4] [Building the Kernel]](#Building_the_Kernel)
-   [[5] [Preparing the boot partition]](#Preparing_the_boot_partition)
-   [[6] [Stage 3 copy]](#Stage_3_copy)
-   [[7] [Finish install]](#Finish_install)

## [Prerequisites]

-   Computer running linux (gentoo)
-   Option to access the SD-Card from this computer
-   Option use USB drive.

## [Micro SD-Card preparation Option 1]

The boot process of the N2 is described in the [ODROID-N2 wiki](https://wiki.odroid.com/odroid-n2/software/boot_sequence) and requires a certain partition structure of the micro SD-Card. First the boot software loads U-Boot, which as to be a specific location, which then loads the actual kernel from the boot partition.

\

### [Partition Table]

The desired partition tables looks like this:

  -------------------- -------- ----------------- ------------------ -----------------------
  Area Name            Size     From (sector #)   To (sector #)      device
  Bootloader1 / MBR    512B     0                 0                  \-
  U-Boot               959.5K   1                 1919               /dev/block/bootloader
  U-Boot Environment   64KB     1920              2047               /dev/block/env
  FAT32 for boot       128MB    2048              264191             /dev/mmcblk0p1
  swap                 4GB      todo              todo               /dev/mmcblk0p2
  BTRFS root           \-       todo              remaining blocks   /dev/mmcblk0p3
  -------------------- -------- ----------------- ------------------ -----------------------

The swap partition is optional an depends on the use case.

### [Option 1 - Extract from Image]

In this section, the desired partition table is acquired by using an available ubuntu boot image. This has the advantage of not needing to build U-Boot.

Download an ubuntu image to extract the bootloader from.

`user `[`$`]`wget `[`http://de.eu.odroid.in/ubuntu_18.04lts/N2/ubuntu-18.04.2-4.9-minimal-odroid-n2-20190329.img.xz`](http://de.eu.odroid.in/ubuntu_18.04lts/N2/ubuntu-18.04.2-4.9-minimal-odroid-n2-20190329.img.xz)

Extract the image.

`user `[`$`]`xz -d ubuntu-18.04.2-4.9-minimal-odroid-n2-20190329.img.xz`

Copy the first MBs which contain the partition table and the bootloader to the sd-card.

`user `[`$`]`dd if=ubuntu-18.04.2-4.9-minimal-odroid-n2-20190329.img of=/dev/mmcblk0 bs=1M count=150 status=progress`

    150+0 records in
    150+0 records out
    157286400 bytes (157 MB, 150 MiB) copied, 0,241063 s, 652 MB/s

Change the copied partition table as needed.

`user `[`$`]`fdisk /dev/mmcblk0`

    Welcome to fdisk (util-linux 2.33).
    Changes will remain in memory only, until you decide to write them.
    Be careful before using the write command.

    Command (m for help): p
    Disk /dev/mmcblk0: 29,2 GiB, 31306285056 bytes, 61145088 sectors
    Units: sectors of 1 * 512 = 512 bytes
    Sector size (logical/physical): 512 bytes / 512 bytes
    I/O size (minimum/optimal): 512 bytes / 512 bytes
    Disklabel type: dos
    Disk identifier: 0x03823826

    Device         Boot  Start     End Sectors  Size Id Type
    /dev/mmcblk0p1        2048  264191  262144  128M  c W95 FAT32 (LBA)
    /dev/mmcblk0p2      264192 7045119 6780928  3,2G 83 Linux

    Command (m for help): d
    Partition number (1,2, default 2): 2

    Partition 2 has been deleted.

    Command (m for help): n
    Partition type
       p   primary (1 primary, 0 extended, 3 free)
       e   extended (container for logical partitions)
    Select (default p): p
    Partition number (2-4, default 2): 2
    First sector (264192-61145087, default 264192):
    Last sector, +/-sectors or +/-size (264192-61145087, default 61145087): +4G

    Created a new partition 2 of type 'Linux' and of size 4 GiB.
    Partition #2 contains a ext4 signature.

    Do you want to remove the signature? [Y]es/[N]o: y

    The signature will be removed by a write command.

    Command (m for help): n
    Partition type
       p   primary (2 primary, 0 extended, 2 free)
       e   extended (container for logical partitions)
    Select (default p): p
    Partition number (3,4, default 3): 3
    First sector (8652800-61145087, default 8652800):
    Last sector, +/-sectors or +/-size (8652800-61145087, default 61145087):

    Created a new partition 3 of type 'Linux' and of size 25 GiB.

    Command (m for help): t
    Partition number (1-3, default 3): 2
    Hex code (type L to list all codes): 82

    Changed type of partition 'Linux' to 'Linux swap / Solaris'.

    Command (m for help): p
    Disk /dev/mmcblk0: 29,2 GiB, 31306285056 bytes, 61145088 sectors
    Units: sectors of 1 * 512 = 512 bytes
    Sector size (logical/physical): 512 bytes / 512 bytes
    I/O size (minimum/optimal): 512 bytes / 512 bytes
    Disklabel type: dos
    Disk identifier: 0x03823826

    Device         Boot   Start      End  Sectors  Size Id Type
    /dev/mmcblk0p1         2048   264191   262144  128M  c W95 FAT32 (LBA)
    /dev/mmcblk0p2       264192  8652799  8388608    4G 82 Linux swap / Solaris
    /dev/mmcblk0p3      8652800 61145087 52492288   25G 83 Linux

    Filesystem/RAID signature on partition 2 will be wiped.

    Command (m for help): w
    The partition table has been altered.
    Syncing disks.

Create swap partition.

`user `[`$`]`mkswap /dev/mmcblk0p2`

    mkswap: /dev/mmcblk0p2: warning: wiping old btrfs signature.
    Setting up swapspace version 1, size = 4 GiB (4294963200 bytes)
    no label, UUID=536be908-9479-42fc-a45f-bdc109a90984

Create btrfs partition.

`user `[`$`]`mkfs.btrfs -L sd_pool /dev/mmcblk0p3`

    btrfs-progs v4.19
    See http://btrfs.wiki.kernel.org for more information.

    Detected a SSD, turning off metadata duplication.  Mkfs with -m dup if you want to force metadata duplication.
    Label:              sd_pool
    UUID:               ef4e6022-44bf-4581-a219-ca82beb198b9
    Node size:          16384
    Sector size:        4096
    Filesystem size:    25.03GiB
    Block group profiles:
      Data:             single            8.00MiB
      Metadata:         single            8.00MiB
      System:           single            4.00MiB
    SSD detected:       yes
    Incompat features:  extref, skinny-metadata
    Number of devices:  1
    Devices:
       ID        SIZE  PATH
        1    25.03GiB  /dev/mmcblk0p3

Prepare directory structure for mounting the partitions.

`user `[`$`]`mkdir -p /mnt/odroid/boot `

`user `[`$`]`mkdir /mnt/odroid/sd_pool `

`user `[`$`]`mkdir /mnt/odroid/root`

Mount the partitions.

`user `[`$`]`mount /dev/mmcblk0p1 /mnt/odroid/boot `

`user `[`$`]`mount /dev/mmcblk0p3 /mnt/odroid/sd_pool`

Create a subvolume for the root filesystem.

`user `[`$`]`btrfs subvolume create /mnt/odroid/sd_pool/root`

    Create subvolume '/mnt/odroid/sd_pool/root'

Mount the root filesystem.

`user `[`$`]`mount /dev/mmcblk0p3 -o subvol=/root /mnt/odroid/root`

Change the default subvolume to be mounted if no subvolume is mentioned while mounting to root.

`user `[`$`]`btrfs subvolume set-default /mnt/odroid/root/`

### [Option 2 - Building u-boot]

todo

## [USB drive Option 2]

If the systems petitboot(20191127) has a recent version on it you can boot to a USB drive. I am not sure about the type of drive but SSD and HDD style USB drives work. I had problem with a USB stick type drive. In this case you can use the Ubuntu or other imagine to boot the system. And install like explained below. But in this case you will not need to install the tool chain etc as you are already on an ARM system. But you will have to install some Packages to be able to build if it does not come with the right tools installed.

** Note**\
I also had problems with the 5.4 kernel and how it behaves differnetly than the 4.9 kernel. On boot it appears to power cycle the USB devices. The drive I had would go into an error state because of this. Switching to a different drive resolved the problem.

## [Building the Kernel]

`user `[`$`]`mkdir -p /mnt/odroid/root/usr/src `

`user `[`$`]`cd /mnt/odroid/root/usr/src `

`user `[`$`]`git clone --depth 1 --branch master `[`https://git.kernel.org/pub/scm/linux/kernel/git/next/linux-next.git`](https://git.kernel.org/pub/scm/linux/kernel/git/next/linux-next.git)` linux`

`user `[`$`]`mkdir -p /tmp/toolchain `

`user `[`$`]`cd /tmp/toolchain `

`user `[`$`]`wget `[`https://releases.linaro.org/components/toolchain/binaries/6.3-2017.02/aarch64-linux-gnu/gcc-linaro-6.3.1-2017.02-x86_64_aarch64-linux-gnu.tar.xz`](https://releases.linaro.org/components/toolchain/binaries/6.3-2017.02/aarch64-linux-gnu/gcc-linaro-6.3.1-2017.02-x86_64_aarch64-linux-gnu.tar.xz)` `

`user `[`$`]`tar -xf gcc-linaro-6.3.1-2017.02-x86_64_aarch64-linux-gnu.tar.xz `

`user `[`$`]`export ARCH=arm64 `

`user `[`$`]`export CROSS_COMPILE=aarch64-linux-gnu- `

`user `[`$`]`export PATH=/tmp/toolchain/gcc-linaro-6.3.1-2017.02-x86_64_aarch64-linux-gnu/bin/:$PATH `

`user `[`$`]`aarch64-linux-gnu-gcc -v `

    Using built-in specs.
    COLLECT_GCC=aarch64-linux-gnu-gcc
    COLLECT_LTO_WRAPPER=/tmp/toolchain/gcc-linaro-6.3.1-2017.02-x86_64_aarch64-linux-gnu/bin/../libexec/gcc/aarch64-linux-gnu/6.3.1/lto-wrapper
    Target: aarch64-linux-gnu
    Configured with: /home/tcwg-buildslave/workspace/tcwg-make-release/label/docker-trusty-amd64-tcwg-build/target/aarch64-linux-gnu/snapshots/gcc-linaro-6.3-2017.02/configure SHELL=/bin/bash --with-mpc=/home/tcwg-buildslave/workspace/tcwg-make-release/label/docker-trusty-amd64-tcwg-build/target/aarch64-linux-gnu/_build/builds/destdir/x86_64-unknown-linux-gnu --with-mpfr=/home/tcwg-buildslave/workspace/tcwg-make-release/label/docker-trusty-amd64-tcwg-build/target/aarch64-linux-gnu/_build/builds/destdir/x86_64-unknown-linux-gnu --with-gmp=/home/tcwg-buildslave/workspace/tcwg-make-release/label/docker-trusty-amd64-tcwg-build/target/aarch64-linux-gnu/_build/builds/destdir/x86_64-unknown-linux-gnu --with-gnu-as --with-gnu-ld --disable-libmudflap --enable-lto --enable-objc-gc --enable-shared --without-included-gettext --enable-nls --disable-sjlj-exceptions --enable-gnu-unique-object --enable-linker-build-id --disable-libstdcxx-pch --enable-c99 --enable-clocale=gnu --enable-libstdcxx-debug --enable-long-long --with-cloog=no --with-ppl=no --with-isl=no --disable-multilib --enable-fix-cortex-a53-835769 --enable-fix-cortex-a53-843419 --with-arch=armv8-a --enable-threads=posix --enable-multiarch --enable-libstdcxx-time=yes --enable-gnu-indirect-function --with-build-sysroot=/home/tcwg-buildslave/workspace/tcwg-make-release/label/docker-trusty-amd64-tcwg-build/target/aarch64-linux-gnu/_build/sysroots/aarch64-linux-gnu --with-sysroot=/home/tcwg-buildslave/workspace/tcwg-make-release/label/docker-trusty-amd64-tcwg-build/target/aarch64-linux-gnu/_build/builds/destdir/x86_64-unknown-linux-gnu/aarch64-linux-gnu/libc --enable-checking=release --disable-bootstrap --enable-languages=c,c++,fortran,lto --build=x86_64-unknown-linux-gnu --host=x86_64-unknown-linux-gnu --target=aarch64-linux-gnu --prefix=/home/tcwg-buildslave/workspace/tcwg-make-release/label/docker-trusty-amd64-tcwg-build/target/aarch64-linux-gnu/_build/builds/destdir/x86_64-unknown-linux-gnu
    Thread model: posix
    gcc version 6.3.1 20170109 (Linaro GCC 6.3-2017.02)

`user `[`$`]`cd /mnt/odroid/root/usr/src/linux/ `

`user `[`$`]`make defconfig `

    #
    # configuration written to .config
    #

Disable all unneeded architectures and DEBUG/NOUVEAU drivers as they are not needed.

`user `[`$`]`perl -pi -e 's/CONFIG_ARCH_[^_]*=y|.*(DEBUG|NOUVEAU).*//g' .config `

`user `[`$`]`make olddefconfig`

Enable Amlogic architecture and multiplexer. Mark btrfs to be compiled into the kernel as the root filesystem is btrfs.

`user `[`$`]`make menuconfig`

[KERNEL]

    Platform selection --->
      [*] Amlogic Platforms
    File systems --->
      <*> Btrfs filesystem support
    Device Drivers --->
      [*] Network device support --->
        [*] Ethernet driver support  --->
          [*] STMicroelectronics devices
            <*> STMicroelectronics Multi-Gigabit Ethernet driver
              <*> STMMAC Platform bus support
                <*> Amlogic Meson dwmac support
        -*- MDIO bus device drivers --->
          <*> Amlogic G12a based MDIO bus multiplexer
      Character devices --->
        Serial drivers --->
          <*> Meson serial port support
          [*]   Support for console on meson
      <*> MMC/SD/SDIO card support  --->
          <*>   Amlogic S905/GX*/AXG SD/MMC Host Controller support

Compile the kernel.

`user `[`$`]`make -j4`

Write a uboot readable uImage with the mkimage tool from dev-embedded/u-boot-tools.

`user `[`$`]` mkimage -A arm64 -O linux -T kernel -C none -a "0x1080000" -e "0x1080000" -n "$(make kernelrelease)" -d arch/arm64/boot/Image /mnt/odroid/boot/uImage `

    Image Name:   5.2.0-rc7-gdacac3759
    Created:      Sat Jul 13 22:37:43 2019
    Image Type:   AArch64 Linux Kernel Image (uncompressed)
    Data Size:    22278656 Bytes = 21756.50 KiB = 21.25 MiB
    Load Address: 01080000
    Entry Point:  01080000

Copy the device tree blob to the boot partition.

`user `[`$`]`cp arch/arm64/boot/dts/amlogic/meson-g12b-odroid-n2.dtb /mnt/odroid/boot/ `

Install the modules to the root partition

`user `[`$`]`make modules_install ARCH=arm64 INSTALL_MOD_PATH=/mnt/odroid/root `

## [Preparing the boot partition]

`user `[`$`]`lsblk -f`

    NAME        FSTYPE      LABEL   UUID                                 FSAVAIL FSUSE% MOUNTPOINT
    mmcblk0
    ├─mmcblk0p1 vfat        BOOT    F702-39CB                             110,4M    14% /mnt/odroid/boot
    ├─mmcblk0p2 swap                536be908-9479-42fc-a45f-bdc109a90984
    └─mmcblk0p3 btrfs       sd_pool ef4e6022-44bf-4581-a219-ca82beb198b9   24,8G     0% /mnt/odroid/sd_pool

[FILE] **`/mnt/odroid/boot/boot.ini`**

    ODROIDN2-UBOOT-CONFIG

    setenv bootargs "root=/dev/mmcblk1p3 rootwait rw console=ttyAML0,115200 clk_ignore_unused"
    setenv dtb_loadaddr "0x1000000"
    fatload mmc $:1 $ meson-g12b-odroid-n2.dtb
    fatload mmc $:1 0x01080000 uImage
    bootm 0x1080000 - $

** Note**\
clk_ignore_unused is required (right now) otherwise boot hangs

Some addtional break down of the above. The mkImage command is part of the u-boot-tools package in gentoo. My udnerstanding this just puts a wrapper around the kernel file. The 0x1080000 addresses is the entry point for the linux kernel. If you want to make an Initrd you can use genkernel once the system is online and then use mkImage to generate the wrapped file. Something like this:

`user `[`$`]` mkimage -A arm64 -O linux -T ramdisk -C lzma -a 0 -e 0 -n uinitrd -d initrd.img /boot/uInitrd`

-C = compression -a and -e are basicaly not used for initrd -n is a Name -d is the source file and the last part is the output.

The above file is the boot.ini for uboot. it appears that petitboot can read different filesystems for this information. While most things referencce using vfat, It does appear to work on ext4 even looking for the /boot dir if your root filesystem is the flat. I also noticed that petitboot, picked up my EFI bootable kernel directly so might be something that works as well.

The .ini file really is more of a shell script. setevn is setting variables. fatload reads something off of a device and puts it in memory where you tell it. and booti/bootm/bootz try to boot what was boot into memory. booti is for a kernel that was not wrapped with mkImage bootm is for one that is wrapped. and bootz allows you to use a compressed kernel image. Options are the .dtb file which I assume some Architecture information. second file is the initrd or - for none last is the kernel. And of course this is the memory location that you put them. the 1080000 should not be confused with the one that was put on the mkImage command. These are just locations. It would seem you just need to have an idea if there is enough space between the things you are copying to RAM. Disclaimer I don\'t fully understand it all and probably have mistakes.

[FILE] **`/mnt/odroid/boot/boot.ini`**

    # Boot Args
    setenv bootargs "root=/dev/mmcblk1p3 rootwait rw $ $ no_console_suspend fsck.repair=yes elevator=noop hdmimode=$ cvbsmode=576cvbs max_freq_a53=$ max_freq_a73=$ maxcpus=$ voutmode=$ $ disablehpd=$ cvbscable=$ overscan=$"

    ...

    # Load kernel, dtb and initrd
    fatload mmc $:1 $ Image
    fatload mmc $:1 $ meson64_odroidn2.dtb
    # fatload mmc $:1 $ uInitrd
    fdt addr $
    # unzip the kernel
    # unzip $ $

    # boot
    # booti $ $ $
    booti $ - $

## [Stage 3 copy]

`user `[`$`]`cd /mnt/odroid/root `

`user `[`$`]`wget `[`http://distfiles.gentoo.org/experimental/arm64/stage3-arm64-systemd-20190428.tar.bz2`](http://distfiles.gentoo.org/experimental/arm64/stage3-arm64-systemd-20190428.tar.bz2)` `

`user `[`$`]`tar -xjf stage3-arm64-systemd-20190428.tar.bz2`

[FILE] **`/mnt/odroid/root/etc/fstab`**

    ...

    /dev/mmcblk1p3      /         btrfs      defaults,auto,noatime,nodiratime      0 0
    /dev/mmcblk1p1      /boot     vfat       noauto,noatime                        1 2
    /dev/mmcblk1p2      none      swap       sw                                    0 0

    ...

Remove \* from root user to reset root password to empty.

** Warning**\
First thing on first login should be to set a root password with passwd

[FILE] **`/mnt/odroid/root/etc/shadow`**

    root::17941:0:::::
    ...

\

## [Finish install]

From here you should be able to finish the install of a systemd install. This is what the stage 3 is based on.

** Note**\
Make sure to setup your password sshd and systemd-networkd. In case the video does not come up on the console you should be able to access from the network