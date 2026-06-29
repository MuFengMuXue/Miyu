**Resources**

[[]][Home](https://developer.solid-run.com/products/cubox-i/)

[[]][Wikipedia](https://en.wikipedia.org/wiki/CuBox "wikipedia:CuBox")

[![Image of Nerdboy\'s Cubox-i device.](/images/thumb/4/45/Cubox-i4-pro-1080.jpg/312px-Cubox-i4-pro-1080.jpg)](https://wiki.gentoo.org/wiki/File:Cubox-i4-pro-1080.jpg)

[](https://wiki.gentoo.org/wiki/File:Cubox-i4-pro-1080.jpg "Enlarge")

[Steve Arnold (nerdboy)](https://wiki.gentoo.org/wiki/User:Nerdboy "User:Nerdboy") \'s Cubox-i device.

This document describes how to install Gentoo on the [SolidRun](https://www.solid-run.com/) Cubox-i and HummingBoard.

## Contents

-   [[1] [Prerequisites]](#Prerequisites)
-   [[2] [Installation]](#Installation)
    -   [[2.1] [Cross-compiler]](#Cross-compiler)
    -   [[2.2] [U-Boot]](#U-Boot)
        -   [[2.2.1] [Mainline]](#Mainline)
        -   [[2.2.2] [SolidRun]](#SolidRun)
    -   [[2.3] [Serial console]](#Serial_console)
    -   [[2.4] [Preparing the SD card]](#Preparing_the_SD_card)
        -   [[2.4.1] [Creating the partitions]](#Creating_the_partitions)
        -   [[2.4.2] [Creating filesystems]](#Creating_filesystems)
        -   [[2.4.3] [Mounting the partitions]](#Mounting_the_partitions)
        -   [[2.4.4] [Unpacking the stage tarball]](#Unpacking_the_stage_tarball)
        -   [[2.4.5] [Creating the fstab file]](#Creating_the_fstab_file)
        -   [[2.4.6] [Setting a default root password]](#Setting_a_default_root_password)
        -   [[2.4.7] [Enabling the serial console]](#Enabling_the_serial_console)
    -   [[2.5] [Kernel]](#Kernel)
        -   [[2.5.1] [Headers]](#Headers)
        -   [[2.5.2] [Firmware]](#Firmware)
            -   [[2.5.2.1] [Video Processing Unit]](#Video_Processing_Unit)
            -   [[2.5.2.2] [WiFi]](#WiFi)
    -   [[2.6] [Bootloader]](#Bootloader)
        -   [[2.6.1] [Mainline]](#Mainline_2)
            -   [[2.6.1.1] [extlinux.conf]](#extlinux.conf)
            -   [[2.6.1.2] [uEnv.txt]](#uEnv.txt)
        -   [[2.6.2] [SolidRun]](#SolidRun_2)
            -   [[2.6.2.1] [uEnv.txt]](#uEnv.txt_2)
        -   [[2.6.3] [Interactive]](#Interactive)
        -   [[2.6.4] [Environment]](#Environment)
        -   [[2.6.5] [uEnv]](#uEnv)
    -   [[2.7] [Continue Gentoo install]](#Continue_Gentoo_install)
    -   [[2.8] [Graphics drivers (FOSS)]](#Graphics_drivers_.28FOSS.29)
    -   [[2.9] [Graphics / Video driver (firmware)]](#Graphics_.2F_Video_driver_.28firmware.29)
    -   [[2.10] [eSATA]](#eSATA)
-   [[3] [Applications]](#Applications)
    -   [[3.1] [Kodi]](#Kodi)
-   [[4] [External resources]](#External_resources)
-   [[5] [Open questions]](#Open_questions)

## [Prerequisites]

**Mandatory**

-   Cubox-i
    -   CuBox-i2ex, CuBox-i2Ultra or CuBox-i4Pro if the serial console is used. Otherwise a HDMI display and a USB keyboard.
-   4 GB+ SD card.
-   Network cable during installation. WiFi can be enabled later.
-   Gentoo system with a cross-compiler for ARM installed.
-   [[[dev-vcs/git]](https://packages.gentoo.org/packages/dev-vcs/git)[]]

**Optional**

-   [TFTP](https://en.wikipedia.org/wiki/Trivial_File_Transfer_Protocol "wikipedia:Trivial File Transfer Protocol") server.
-   [[[dev-embedded/u-boot-tools]](https://packages.gentoo.org/packages/dev-embedded/u-boot-tools)[]]
-   SolidRun [Ignition](https://www.solid-run.com/downloads/ignition/) image to test if the Cubox-i device is working with the serial console, or the connected display and keyboard. This will overwrite the U-Boot installation!

## [Installation]

The install consists of installing [[[sys-devel/crossdev]](https://packages.gentoo.org/packages/sys-devel/crossdev)[]], partitioning and formatting, the SD card. Copying over a stage3 tarball, configuring it so that it can boot and it can be accessed. Creating a kernel. Booting the kernel on the machine. Installing the kernel for an automatic boot. Continue a default Gentoo installation.

### [Cross-compiler]

[crossdev](https://wiki.gentoo.org/wiki/Crossdev "Crossdev") is required to build [U-Boot](https://www.denx.de/wiki/U-Boot) and the kernel on an **[amd64]** or **[x86]** system.

Install crossdev:

`root `[`#`]`emerge --ask sys-devel/crossdev`

Build a cross-compilation toolchain:

`root `[`#`]`crossdev --stable --target armv7a-unknown-linux-gnueabihf`

For more information, please refer to the [Creating a cross-compiler (Embedded Handbook)](https://wiki.gentoo.org/wiki/Embedded_Handbook/General/Creating_a_cross-compiler "Embedded Handbook/General/Creating a cross-compiler") and [Crossdev](https://wiki.gentoo.org/wiki/Crossdev "Crossdev") articles.

### [U-Boot]

#### [Mainline]

When the Cubox-i was released it had no mainline U-Boot support. Instead SolidRun maintained its own patched fork. Since v2017.01 mainline U-Boot works without any patches, so there is no longer a reason to use the SolidRun fork.

Setup the cross-compilation environment:

`user `[`$`]`export ARCH=arm `

`user `[`$`]`export CROSS_COMPILE=armv7a-unknown-linux-gnueabihf- `

Clone the U-Boot Git repository:

`user `[`$`]`git clone https://gitlab.denx.de/u-boot/u-boot.git `

`user `[`$`]`cd u-boot `

`user `[`$`]`git checkout v2019.04 `

Mainline U-Boot has *no* [uEnv.txt] support, although it does have [extlinux.conf] support which is just as easy if not easier to use. If [uEnv.txt] support is still desired, apply the patch by [Steve Arnold (nerdboy)](https://wiki.gentoo.org/wiki/User:Nerdboy "User:Nerdboy") .

** Note**\
The patch applies against U-Boot Git branch v2017.11. If that branch is too old, consider using [extlinux.conf] or the legacy [boot.scr] instead.

`user `[`$`]`git checkout v2017.11 `

`user `[`$`]`wget https://dev.gentoo.org/~nerdboy/files/0001-cubox4i-uEnv.txt-bootz-n-fixes-after-rcn-2017.11.patch `

`user `[`$`]`patch -p1 < 0001-cubox4i-uEnv.txt-bootz-n-fixes-after-rcn-2017.11.patch `

Build U-Boot:

`user `[`$`]`make mx6cuboxi_defconfig `

`user `[`$`]`make `

A successful build will create two files in the source tree directory, [SPL] and [u-boot.img]

-   [SPL] is the actual machine detection and initialization and *must* be flashed at offset 1 KByte of the boot SD card.
-   [u-boot.img] is the second stage bootloader; it can be flashed at offset 69 KByte of the boot SD card;

`root `[`#`]`dd if=SPL of=/dev/mmcblk0 bs=1K seek=1 `

`root `[`#`]`dd if=u-boot.img of=/dev/mmcblk0 bs=1K seek=69 `

** Note**\
If a USB SD card reader is used the device name will be [/dev/sdX], where `X` represents the USB SD card reader.

#### [SolidRun]

SolidRun provides a fork of mainline U-Boot with board support package (BSP) vendor branches. For more information, please refer to the [SolidRun Knowledge Base](https://developer.solid-run.com/knowledge-base/i-mx6-u-boot/).

Setup the cross-compilation environment:

`user `[`$`]`export ARCH=arm `

`user `[`$`]`export CROSS_COMPILE=armv7a-unknown-linux-gnueabihf- `

Clone the U-Boot Git repository:

`user `[`$`]`git clone https://github.com/SolidRun/u-boot.git `

`user `[`$`]`cd u-boot `

Build U-Boot:

`user `[`$`]`make mx6cuboxi_defconfig `

`user `[`$`]`make `

A successful build will create two files in the source tree directory, [SPL] and [u-boot.img]

-   [SPL] is the actual machine detection and initialization and *must* be written at offset 1 KByte of the boot SD card.
-   [u-boot.img] is the second stage bootloader; it can be written at offset 69 KByte of the boot SD card; alternatively it can be placed as-is on the first partition of the SD card if the partition has a FAT filesystem.

** Note**\
Older versions of SolidRun\'s U-Boot wrote [u-boot.img] at offset 42 KByte. SolidRun has updated their fork and now uses the same 69 KByte offset as mainline.

`root `[`#`]`dd if=SPL of=/dev/mmcblk0 bs=1K seek=1 `

`root `[`#`]`dd if=u-boot.img of=/dev/mmcblk0 bs=1K seek=69 `

** Note**\
If a USB SD card reader is used the device name will be [/dev/sdX], where `X` represents the USB SD card reader.

### [Serial console]

The Cubox-i2ex, CuBox-i2Ultra and CubBox-i4Pro have serial console support via a FTDI FT230X USB to UART serial interface. This allows connecting the Cubox-i directly to another computer. Alternatively the Cubox-i can be connected to a HDMI display and USB keyboard.

The computer connecting to the Cubox-i will need to have the following kernel configuration options enabled:

[KERNEL] **Enabling serial console support**

        Device Drivers --->
          [*] USB support --->
                <*>   USB Serial Converter support --->
                        <*>   USB FTDI Single Port Serial Driver

Connecting to the serial console requires an application such as [[[app-misc/screen]](https://packages.gentoo.org/packages/app-misc/screen)[]] or [[[net-dialup/minicom]](https://packages.gentoo.org/packages/net-dialup/minicom)[]]. For more information, please refer to the [SolidRun Knowledge Base](https://developer.solid-run.com/knowledge-base/serial-console-usb-uart/).

### [Preparing the SD card]

#### [Creating the partitions]

A single partition scheme can be used with mainline U-Boot when using an ext2/3/4 formatted root partition. However when using a Btrfs formatted root partition (or other unsupported filesystem), an ext2/3/4 or FAT32 formatted boot partition is required.

  ----------------------------------------------------------------------------------------------------- ------------ ----------------- ----------------
  Partition                                                                                             Filesystem   Size              Description
  [/dev/mmcblk0p1]   ext2         100 MB            Boot partition
  [/dev/mmcblk0p2]   ext4         Rest of SD card   Root partition
  ----------------------------------------------------------------------------------------------------- ------------ ----------------- ----------------

** Note**\
If a USB SD card reader is used the device names will be [/dev/sdX1] and [/dev/sdX2] respectively, where `X` represents the USB SD card reader.

#### [Creating filesystems]

Create the filesystems on the boot and root partitions:

`root `[`#`]`mkfs.ext2 /dev/mmcblk0p1 `

`root `[`#`]`mkfs.ext4 /dev/mmcblk0p2 `

** Note**\
When using ext2, ext3, or ext4 on a small partition (less than 8 GB), then the filesystem must be created with `-T small` to reserve enough [inodes](https://en.wikipedia.org/wiki/Inodes "wikipedia:Inodes").

#### [Mounting the partitions]

Mount the boot and root partitions:

`root `[`#`]`mkdir /mnt/cubox `

`root `[`#`]`mount /dev/mmcblk0p2 /mnt/cubox `

`root `[`#`]`mkdir /mnt/cubox/boot `

`root `[`#`]`mount /dev/mmcblk0p1 /mnt/cubox/boot `

#### [Unpacking the stage tarball]

Go to the mount point where the root filesystem is mounted:

`root `[`#`]`cd /mnt/cubox`

Get the latest [stage 3](http://distfiles.gentoo.org/releases/arm/autobuilds/current-stage3-armv7a_hardfp/) and extract it to the root partition:

`root `[`#`]`tar xpvf stage3-*.tar.bz2 --xattrs-include='*.*' --numeric-owner`

#### [Creating the fstab file]

Add the following entries to the fstab file:

[FILE] **`/mnt/cubox/etc/fstab`**

    /dev/mmcblk1p1          /boot           ext2            noauto,noatime  1 2
    /dev/mmcblk1p2          /               ext4            noatime         0 1

** Note**\
With Linux 4.8.x or earlier use [/dev/mmcblk0] instead of [/dev/mmcblk1] (i.e. [/dev/mmcblk0p1] will be the first partition on the SD card). The device names have changed to to accommodate boards such as the HummingBoard which have an eMMC.

#### [Setting a default root password]

To be able to login after booting, set a default [root] password by creating a password hash and adding it to the shadow file:

`root `[`#`]`openssl passwd -1`

    Password:
    Verifying - Password:
    $1$AK6NWKtp$U8EMq/wAGx0PT1vLOf9/u0

In this example the password hash corresponds to the password \"cubox\".

The default shadow entry for the [root] user will look like:

[FILE] **`/mnt/cubox/etc/shadow`**

    root:*:10770:0:::::

Replace the `*` with the password hash from the [openssl] command above:

[FILE] **`/mnt/cubox/etc/shadow`**

    root:$1$AK6NWKtp$U8EMq/wAGx0PT1vLOf9/u0:10770:0:::::

** Note**\
After booting the [root] password should be set again using [passwd] to create a secure SHA512 password hash. For more information, please refer to the [Setting a default root password](https://wiki.gentoo.org/wiki/Setting_a_default_root_password "Setting a default root password") article.

#### [Enabling the serial console]

To have a serial console available after booting, change the `s0` line to the following:

[FILE] **`/mnt/cubox/etc/inittab`**

    s0:12345:respawn:/sbin/agetty -L 115200 ttymxc0 vt100

### [Kernel]

The mainline kernel 3.19+ and [[[sys-kernel/gentoo-sources]](https://packages.gentoo.org/packages/sys-kernel/gentoo-sources)[]] has great support for Cubox-i devices, complete with working graphics and networking.

Create the install directories:

`root `[`#`]`mkdir -p /var/build/cubox-i/root/boot `

** Note**\
The install directories are where the kernel, modules and devices trees will be installed. In this article [/var/build/cubox-i/root] is used as an intermediate root directory. Any directory can be used, even the actual root directory of the device.

Setup the cross-compilation environment:

`root `[`#`]`export ARCH="arm" `

`root `[`#`]`export CROSS_COMPILE="armv7a-hardfloat-linux-gnueabi-" `

`root `[`#`]`export INSTALL_PATH="/var/build/cubox-i/root/boot" `

`root `[`#`]`export INSTALL_MOD_PATH="/var/build/cubox-i/root" `

Configure the kernel:

`root `[`#`]`cd /path/to/kernel/source `

`root `[`#`]`make imx_v6_v7_defconfig `

`root `[`#`]`make menuconfig `

Build and install the kernel (zImage):

`root `[`#`]`make zImage `

`root `[`#`]`make zinstall `

The kernel is located at [arch/arm/boot/zImage]. The kernel will be installed at [/var/build/cubox-i/root/boot/vmlinuz-\<kernel-version\>]

Build and install the kernel modules:

`root `[`#`]`make modules `

`root `[`#`]`make modules_install `

The kernel modules will be installed at [/var/build/cubox-i/root/lib/modules/\<kernel-version\>/]

Build and install the device trees:

`root `[`#`]`make dtbs `

`root `[`#`]`make dtbs_install `

The device trees are located at [arch/arm/boot/dts/]. The device trees will be installed at [/var/build/cubox-i/root/boot/dtbs/\<kernel-version\>/]

** Note**\
The above will build and install device trees for all i.MX devices. It is possible to build a device tree for a specific device only. For example, run [make imx6q-cubox-i.dtb] to build the device tree for a Cubox-i4Pro. The device tree will be located at [arch/arm/boot/dts/imx6q-cubox-i.dtb], and needs to be copied manually to [/var/build/cubox-i/root/boot/dtbs/\<kernel-version\>/]

The kernel, modules and devices trees can now be installed to the actual root directory of the device:

`root `[`#`]`cp -r /var/build/cubox-i/root/ /mnt/cubox `

#### [Headers]

To compile certain applications like Kodi that have modified/additional codecs you need to expose the patched kernel headers. Fortunately there is a script for that:

`root `[`#`]`make headers_install ARCH=arm INSTALL_HDR_PATH=/usr/local/include`

If you install them into [/usr/local/include] then you don\'t overwrite the ones provided by the Gentoo package.

#### [Firmware]

##### [Video Processing Unit]

The i.MX6 SoC contains a Video Processing Unit (VPU) that allows video decoding and encoding to be done in hardware. The VPU is supported by the mainline kernel but requires firmware to operate. The following table lists the VPU firmware required by each Cubox-i device.

  ------------- ----------------- -------------------------------------------------------------------------------------------------------
  Device        SoC               Firmware
  CuBox-i1      i.MX6 Solo        [vpu_fw_imx6d.bin]
  CuBox-i2      i.MX6 Dual Lite   [vpu_fw_imx6d.bin]
  CuBox-i2eX    i.MX6 Dual        [vpu_fw_imx6q.bin]
  CuBox-i4Pro   i.MX6 Quad        [vpu_fw_imx6q.bin]
  ------------- ----------------- -------------------------------------------------------------------------------------------------------

Instructions for obtaining the VPU firmware can be found at the [coda-bits](https://github.com/pH5/coda-bits#firmware-download) GitHub repository. The firmware needs to be placed in the [/lib/firmware] directory.

##### [WiFi]

The following kernel configuration options are required for WiFi support. These options should already be enabled if the kernel was configured with `imx_v6_v7_defconfig`.

[KERNEL] **Enabling WiFi support**

        Device Drivers --->
          [*] Network device support --->
                [*]   Wireless LAN --->
                        [*]   Broadcom devices
                        <*>     Broadcom FullMAC WLAN driver
                        [*]     SDIO bus interface support for FullMAC driver

The WiFi driver requires firmware to operate, which can be obtained directly from the Linux firmware [repository](https://git.kernel.org/pub/scm/linux/kernel/git/firmware/linux-firmware.git/tree/brcm) or the [[[sys-kernel/linux-firmware]](https://packages.gentoo.org/packages/sys-kernel/linux-firmware)[]] package. The required firmware can be determined by examining the [dmesg] output of a running Cubox-i device:

`root `[`#`]`dmesg | grep -i brcm`

    [    2.981734] brcmfmac: brcmf_fw_map_chip_to_name: using brcm/brcmfmac4330-sdio.bin for chip 0x004330(17200) rev 0x000004
    [    2.983623] brcmfmac mmc0:0001:1: Direct firmware load for brcm/brcmfmac4330-sdio.bin failed with error -2

The above output from a Cubox-i4Pro indicates that [brcmfmac4330-sdio.bin] is the firmware required by the driver. This may be differ depending on the Cubox-i model.

The firmware also requires NVRAM calibration data, which can be obtained from the Freescale (now NXP) [repository](https://github.com/Freescale/meta-freescale-3rdparty/tree/master/recipes-bsp/broadcom-nvram-config/files/cubox-i). The NVRAM calibration data needs to have the correct WiFi regulatory domain set. This can be done by setting the value of the `ccode` parameter to the [country code](https://git.kernel.org/pub/scm/linux/kernel/git/sforshee/wireless-regdb.git/tree/db.txt) in which the device will be operating in. For example, to set the WiFi regulatory domain for the United States:

[FILE] **`brcmfmac4329-sdio.txt or brcmfmac4330-sdio.txt`**

    ccode=US

The firmware and NVRAM calibration data need to be placed in the [/lib/firmware/brcm] directory.

### [Bootloader]

U-Boot will normally wait three seconds for user input before attempting to boot. If user input is received, the boot sequence is interrupted and an interactive shell is started. If three seconds pass with no user input, U-Boot will look for an environment configuration on the first partition. If no valid environment configuration is found, U-Boot will display *\*\*\* Warning - bad CRC, using default environment*, and will then continue with the default environment configuration. This is where mainline U-Boot and SolidRun U-Boot differ. Mainline supports [boot.scr] and extlinux.conf on the first partition, while SolidRun also supports [uEnv.txt].

#### [Mainline]

##### [extlinux.conf]

U-Boot supports [Syslinux](https://wiki.gentoo.org/wiki/Syslinux "Syslinux") style boot configuration. U-Boot only borrows a small subset of the Syslinux [configuration](https://wiki.syslinux.org/wiki/index.php?title=Config) options, and does not require Syslinux itself. This is much simpler than using [boot.scr] or applying patches to add [uEnv.txt] support.

Create the [extlinux] directory:

`root `[`#`]`mkdir /mnt/cubox/boot/extlinux`

Create the following configuration and adjust accordingly:

[FILE] **`/mnt/cubox/boot/extlinux/extlinux.conf`**

    PROMPT 1
    TIMEOUT 50
    DEFAULT linux

    LABEL linux
    KERNEL /vmlinuz-4.19.0
    FDTDIR /dtbs/4.19.0
    APPEND root=/dev/mmcblk1p2 rootfstype=ext4 video=mxcfb0:dev=hdmi,1920x1080M@60,if=RGB24,bpp=32 console=ttymxc0,115200n8 console=tty1 consoleblank=0

** Note**\
The `KERNEL` and `FDTDIR` paths are relative to the root of the boot partition. If a boot partition is not used, adjust accordingly.

** Note**\
With Linux 4.8.x or earlier use [/dev/mmcblk0] instead of [/dev/mmcblk1]. In the above example, change the `root` parameter to `root=/dev/mmcblk0p2` to inform the kernel that the root partition is the 2nd partition on the [/dev/mmcblk0] device.

##### [uEnv.txt]

If the [uEnv.txt] patch was applied when building U-Boot, create [uEnv.txt] in the boot partition or directory:

[FILE] **`uEnv.txt`**

    uname_r=4.10.5-armv7-x1

    cmdline=video=HDMI-A-1:1024x768 net.ifnames=0 cma=384M console=tty1

    fdtfile=imx6q-cubox-i.dtb

Adjust the video argument to match the display.

#### [SolidRun]

##### [uEnv.txt]

If you use the SolidRun U-Boot from this wiki you can use the default settings and no direct modification of the U-Boot configuration might be necessary. If the first partition of the SD card is formatted with ext2 or fat it will read the the file [uEnv.txt] with the configuration from it.

[FILE] **`uEnv.txt`**

    bootfile=zImage
    mmcargs=setenv bootargs root=/dev/mmcblk1p2 rootfstype=ext4 rootwait rootflags=compress console=ttymxc0,115200n8 video=1920x1080M@60 init=/sbin/init

These two lines should be enough to boot the kernel. The U-Boot from this wiki can boot a zImage directly (no conversion to uImage necessary). The zImage and the \*.dtb file have to reside in the root folder of this partition next to the [uEnv.txt]. The second line contains the kernel flags (for example the root).

If you have no console output on your screen during boot, try `console=tty1`

** Note**\
With Linux 4.8.x or earlier use [/dev/mmcblk0] instead of [/dev/mmcblk1]. In the above example, change the `root` parameter to `root=/dev/mmcblk0p2` to inform the kernel that the root partition is the 2nd partition on the [/dev/mmcblk0] device.

#### [Interactive]

Connect to your Cubox-i with a serial console (or with a keyboard and a display) and interrupt the U-Boot bootloader with [Enter] and type the following commands.

    setenv ipaddr 192.168.0.<CUBOXI-IP>
    setenv serverip 192.168.0.<TFTP-IP>
    setenv bootargs root=/dev/mmcblk0p2 rootfstype=ext4 ro rootwait console=ttymxc0,115200
    tftpboot 0x10800000 uimage
    bootm 0x10800000

This should boot you in your Cubox-i installation and you should be able to login as root with your password. From here you can continue with a default Gentoo installation. To make this boot configuration permanent follow the next step \"Default\".

#### [Environment]

In the following we will make the settings permanent. The uImage file is copied to the boot partition. The first line contains the settings for loading the kernel into memory. The second holds the arguments for the kernel. The third one is the code to execute the kernel.

The bootcmd is called by default and executes theses three steps in order. The last line makes these variables permanent in the U-Boot settings.

    setenv mybootload ext2load mmc 0:1 0x10800000 /uimage
    setenv mybootset setenv bootargs root=/dev/mmcblk0p2 rootfstype=ext4 ro rootwait console=ttymxc0,115200
    setenv mybootstart bootm 0x10800000
    setenv bootcmd run mybootset mybootload mybootstart
    saveenv

#### [uEnv]

U-Boot can also read configuration values from a file. This way the boot process can be modified without going into the U-Boot console and the settings are permanent as well. The following script is modified from the original mini-image used for the installation.

    setenv gsetmmc 'root="root=/dev/mmcblk$p$rootpart rootfstype=$rootfs ro rootwait"'
    setenv gconsole console=ttymxc0,115200 consoleblank=0
    setenv gbootextra init=/init
    setenv grootflags ""
    setenv gvideo mxcfb0:dev=hdmi,1920x1080M@60,if=RGB24 dmfc=3
    setenv gbootpreset 'bootdev=mmc; bootunit=0; bootpart=1; bootfs=ext2; envfile=uEnv.txt; bootroot=; bootfile=uImage'
    setenv grootpreset 'rootunit=0; rootpart=2; rootfs=ext4'
    setenv gsetenvscript setenv gbootenv "\'run gset\$; setenv bootargs \$root \$gvideo \$gconsole \$gbootextra \$grootflags $end\'"
    setenv gloaduenv 'if $load $bootdev $bootunit:$bootpart $loadaddr $envfile; then env import -t $loadaddr $filesize; fi'
    setenv grootpresetup 'bootrun=bootm; loadfile=$bootfile; rootdev=$bootdev; rootunit=$bootunit; rootpart=$rootpart; rootfs=$rootfs'
    setenv gbootload '$load $bootdev $bootunit:$bootpart $loadaddr $bootroot/$loadfile'
    setenv gbootstart '$bootrun'
    setenv bootcmd run gbootpreset grootpreset gsetenvscript gloaduenv grootpresetup gbootenv gbootload gbootstart

In the minimal [uEnv.txt](https://github.com/Freescale/meta-fsl-arm-extra/blob/master/recipes-bsp/u-boot/u-boot-cubox-i/uEnv.txt) is enough to boot a stock ext4 system on the SD card. To boot from USB you must use `rootwait` or `rootdelay`.

### [Continue Gentoo install]

Steps that should be done right after the installation:

1.  setup network
2.  set date
3.  emerge-webrsync
4.  emerge ntpd
5.  /etc/init.d/sshd

[Gentoo ARM Handbook](https://wiki.gentoo.org/wiki/Handbook:Main_Page "Handbook:Main Page") (currently unavaliable)

### [][Graphics drivers (FOSS)]

Although it\'s not fully integrated yet, there is useful 2D/3D functionality in the latest FOSS drivers, some of which were only recently added to the [Gentoo ARM overlay](https://github.com/gentoo/arm).

-   mesa - the latest releases enable vivante/imx (be sure and enable gallium/glx/dri3 in mesa)
-   libdrm - enables \"experimental\" vivante/etnaviv api
-   xf86-video-armada - builds multiple drivers, depends on various versions of dependencies below
-   libdrm-armada - gpu shim
-   libetnaviv (latest is header-only, older is a library)
-   galcore-headers - public \"etnaviv\" interface

Note: the packages in the main portage tree call the imx VIDEO_CARD \"vivante\" but in the above Xorg drivers vivante refers to the legacy GAL drivers which are disabled (the FOSS pieces should probably all be called etnaviv). To try the FOSS graphics stack, you should set `VIDEO_CARDS="imx vivante"` in your [make.conf] file and add the ARM overlay.

So far the imx/armada drivers seem to work for 2D in X but the log shows an error initializing the etnadrm_gpu driver and claims to fall back to swrast 3D. Still, with dri3 and vivante enabled glxgears gets over 110 fps in Xorg, so there is that\... (if you only have dri2 enabled then it really is swrast @ 22 fps)

\

### [][Graphics / Video driver (firmware)]

The hardware units have support for decoding certain codecs with additional firmware: [https://github.com/pH5/coda-bits](https://github.com/pH5/coda-bits) More about this can be found here: [https://imxdev.gitlab.io/tutorial/Decoding_video_with_a_mainline_kernel_on_i.MX6/](https://imxdev.gitlab.io/tutorial/Decoding_video_with_a_mainline_kernel_on_i.MX6/)

### [eSATA]

In addition to enabling the Freescale PCIe driver and related SD support, if you want to connect an external eSATA device, there are two main \"issues\" to keep in mind:

-   Use a separate USB power source, since there is no power provided over eSATA (and the onboard USB is not enough)
-   You must add `ahci_imx.hotplug=1` to the kernel command line in [uEnvt.txt] (or your [boot.scr])

## [Applications]

### [Kodi]

The live ebuild of Kodi (v18) can by now compiled without additional modifications.

If you want to use the etnaviv driver make sure to have a kernel with the VPU firmware loaded.

If you have docker running you can use the image [https://hub.docker.com/r/slangenmaier/kodi/](https://hub.docker.com/r/slangenmaier/kodi/) to test it.

## [External resources]

-   [SolidRun Knowledge Base - CuBox-i -- Getting Started](https://developer.solid-run.com/knowledge-base/cubox-i-getting-started/)
-   [SolidRun Knowledge Base - Flashing an SD card](https://developer.solid-run.com/knowledge-base/flashing-an-sd-card/)
-   [SolidRun Knowledge Base - i.MX6 Kernel](https://developer.solid-run.com/knowledge-base/i-mx6-kernel/)
-   [SolidRun Knowledge Base - Serial-Console USB-\>UART](https://developer.solid-run.com/knowledge-base/serial-console-usb-uart/)
-   [Linux Wireless Wiki - Broadcom brcmfmac Firmware](https://wireless.wiki.kernel.org/en/users/Drivers/brcm80211#firmware_installation1)
-   [NXP Community - HDMI goes to sleep](https://community.nxp.com/thread/308940)
-   [U-Boot mainline configuration](https://github.com/archlinuxarm/PKGBUILDs/tree/master/alarm/uboot-cubox-i)
-   [Wandboard](https://www.digikey.com/eewiki/display/linuxonarm/Wandboard)

## [Open questions]

-   open-source hardware-accelerated video driver
    -   [reverse engineered drivers](https://github.com/etnaviv/etna_viv)