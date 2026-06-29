[] The information in this article is probably **outdated**. You can help the Gentoo community by verifying and [updating this article](https://wiki.gentoo.org/index.php?title=Udoo&action=edit).

**Resources**

[[]][Home](https://www.udoo.org/udoo-dual-and-quad/)

[[]][Ebuild repository](https://github.com/gentoo/arm)

[[]][Link](https://github.com/RobertCNelson/armv7-multiplatform)

[[]][Link](https://www.eewiki.net/display/linuxonarm/UDOO)

[![caption](/images/thumb/a/ab/Imv6-udoo-quad-1080.jpg/500px-Imv6-udoo-quad-1080.jpg)](https://wiki.gentoo.org/wiki/File:Imv6-udoo-quad-1080.jpg "caption")

This document is both a mainline integration story and a description of how to install Gentoo using mainline u-boot and kernel plus FOSS graphics on the [Udoo](https://www.udoo.org/) Quad and Dual kickstarter boards. See [this gist](https://gist.github.com/sarnold/2e244fa8580ec715321a515c72535d4f) for a quick and dirty howto on Udoo Neo (note that mainline kernel still has barebones DTS files for Neo boards, no HDMI output, etc).

## Contents

-   [[1] [Prerequisite]](#Prerequisite)
    -   [[1.1] [Optional]](#Optional)
-   [[2] [Installation]](#Installation)
    -   [[2.1] [Installing Crossdev]](#Installing_Crossdev)
    -   [[2.2] [Setup U-Boot]](#Setup_U-Boot)
        -   [[2.2.1] [Mainline]](#Mainline)
    -   [[2.3] [Setup serial console]](#Setup_serial_console)
    -   [[2.4] [Preparing the SD card]](#Preparing_the_SD_card)
        -   [[2.4.1] [Extract stage 3]](#Extract_stage_3)
        -   [[2.4.2] [Edit /etc/fstab]](#Edit_.2Fetc.2Ffstab)
        -   [[2.4.3] [Set the root password]](#Set_the_root_password)
        -   [[2.4.4] [Enable the serial console]](#Enable_the_serial_console)
    -   [[2.5] [Kernel]](#Kernel)
        -   [[2.5.1] [Mainline (or Gentoo sources)]](#Mainline_.28or_Gentoo_sources.29)
        -   [[2.5.2] [Latest patched version]](#Latest_patched_version)
        -   [[2.5.3] [WiFi]](#WiFi)
    -   [[2.6] [Bootloader]](#Bootloader)
        -   [[2.6.1] [Mainline]](#Mainline_2)
            -   [[2.6.1.1] [uEnv.txt]](#uEnv.txt)
            -   [[2.6.1.2] [extlinux.conf]](#extlinux.conf)
    -   [[2.7] [Continue Gentoo install]](#Continue_Gentoo_install)
    -   [[2.8] [Graphics drivers (FOSS)]](#Graphics_drivers_.28FOSS.29)
    -   [[2.9] [Sam3 Microcontroller (Arduino Due compatible)]](#Sam3_Microcontroller_.28Arduino_Due_compatible.29)
-   [[3] [Hardware Random Number Generator]](#Hardware_Random_Number_Generator)
    -   [[3.1] [Install rng-tools]](#Install_rng-tools)
    -   [[3.2] [Load modules]](#Load_modules)
    -   [[3.3] [Apply settings in /etc/conf.d/rngd]](#Apply_settings_in_.2Fetc.2Fconf.d.2Frngd)
    -   [[3.4] [Check that /dev/random is slow]](#Check_that_.2Fdev.2Frandom_is_slow)
    -   [[3.5] [Restart rngd]](#Restart_rngd)
    -   [[3.6] [Test if it works]](#Test_if_it_works)
    -   [[3.7] [Add rng-tools to boot]](#Add_rng-tools_to_boot)
    -   [[3.8] [Add loading of caamrng to boot]](#Add_loading_of_caamrng_to_boot)
-   [[4] [Applications]](#Applications)
    -   [[4.1] [Arduino IDE]](#Arduino_IDE)
        -   [[4.1.1] [eselect repository]](#eselect_repository)
    -   [[4.2] [Required Packages]](#Required_Packages)
    -   [[4.3] [Required Devices]](#Required_Devices)
-   [[5] [References]](#References)

## [Prerequisite]

-   Udoo Quad/Dual
    -   if you want to configure over a serial console you need a micro-USB cable.
    -   otherwise you need an HDMI display and a USB keyboard (and hope ;)
-   git
-   SD card (with enough space, rootfs with a kernel and Gentoo, 4GB+)
-   network cable for an internet connection (the WiFi driver should actually work with a newer kernel)
-   another (Linux) computer with a cross compiler for arm installed (the installation for Gentoo is documented here)

### [Optional]

-   tftp server
-   [[[dev-embedded/u-boot-tools]](https://packages.gentoo.org/packages/dev-embedded/u-boot-tools)[]]
-   [Udoobuntu](https://www.udoo.org/udoobuntu-the-official-udoo-linux-operating-system/)

If you want you can install the Udoobuntu image to see if your machine is working with the serial connection (or the connected keyboard and display). This will overwrite your card!

## [Installation]

The install consists of installing [[[sys-devel/crossdev]](https://packages.gentoo.org/packages/sys-devel/crossdev)[]], partitioning and formatting, the SD card. Copying over a stage3 tarball, configuring it so that it can boot and it can be accessed. Building U-Boot and a kernel. Booting the kernel on the machine. Installing the kernel for an automatic boot. Continue a default Gentoo installation.

### [Installing Crossdev]

This is necessary to build U-Boot and the kernel on your desktop system.

`root `[`#`]`emerge sys-devel/crossdev `

`root `[`#`]`crossdev -t armv7a-hardfloat-linux-gnueabi `

For more details, please refer to the [Embedded Handbook](https://wiki.gentoo.org/wiki/Embedded_Handbook/General/Creating_a_cross-compiler "Embedded Handbook/General/Creating a cross-compiler") and [Crossdev](https://wiki.gentoo.org/wiki/Crossdev "Crossdev") articles.

### [Setup U-Boot]

When the Udoo was released there was no mainline support for it. So the vendor maintained its own patched fork of bootloader and kernel. That said, since 2014.04 a mainline U-Boot works without any patches, so there is no longer a real reason to go with the fork. Just use mainline (and possibly some RCN convenience patches).

If you\'re already familiar with the LinuxOnArm wiki approach ^[\[1\]](#cite_note-1)^ and like the convenience of uEnv.txt configuration, then you can download and apply the optional patch below.

#### [Mainline]

`user `[`$`]`export ARCH=arm `

`user `[`$`]`export CROSS_COMPILE=armv7a-hardfloat-linux-gnueabi- `

`user `[`$`]`git clone http://git.denx.de/u-boot.git `

`user `[`$`]`cd u-boot `

`user `[`$`]`git checkout v2017.11 `

`user `[`$`]`wget https://dev.gentoo.org:/~nerdboy/files/0001-udoo-uEnv.txt-bootz-n-fixes-ala-rcn-2017.11.patch `

`user `[`$`]`git am --whitespace=fix 0001-udoo-uEnv.txt-bootz-n-fixes-ala-rcn-2017.11.patch `

`user `[`$`]`make udoo_defconfig `

`user `[`$`]`make `

A successful build will create two files in the source tree directory, [SPL] and [u-boot.img]

-   [SPL] file is the actual machine detection and initialization and must be flashed on offset 1 KByte of the boot SD card.
-   [u-boot.img] is the second stage bootloader; it can be flashed at offset 69 KByte from the starting of the boot SD card;

`root `[`#`]` dd if=SPL of=/dev/sdX bs=1K seek=1 `

`root `[`#`]` dd if=u-boot.img of=/dev/sdX bs=1K seek=69 `

In the mainline version there is no support for a [uEnv.txt] file without a patch. So you can use the legacy [boot.scr] method using u-boot-tools, or you can download a uEnv patch to provide more flexibility and easier configuration. The patch follows the usual [LinuxOnArm wiki](https://eewiki.net/display/linuxonarm/UDOO) setup for deploying dtb files in versioned subdirectories, which is the default kernel make install path:

U-Boot patch and SD card deploy steps: [https://eewiki.net/display/linuxonarm/UDOO#UDOO-Bootloader:U-Boot](https://eewiki.net/display/linuxonarm/UDOO#UDOO-Bootloader:U-Boot)

Get the patch here: [https://dev.gentoo.org:/\~nerdboy/files/0001-udoo-uEnv.txt-bootz-n-fixes-ala-rcn-2017.11.patch](https://dev.gentoo.org:/~nerdboy/files/0001-udoo-uEnv.txt-bootz-n-fixes-ala-rcn-2017.11.patch)

More information: [http://www.denx.de/wiki/U-Boot](http://www.denx.de/wiki/U-Boot)

### [Setup serial console]

The Udoo Quad/Dual boards all have serial console support via a FTDI FT230X USB to UART serial interface. This allows connecting the Udoo directly to another computer. Alternatively the Udoo can be connected to an HDMI display and USB keyboard.

The computer connecting to the Udoo will need to have the following kernel configuration options enabled:

[KERNEL] **Enabling serial console support**

        Device Drivers --->
          [*] USB support --->
                <*>   USB Serial Converter support --->
                        <*>   USB FTDI Single Port Serial Driver

Connecting to the serial console requires an application such as [[[app-misc/screen]](https://packages.gentoo.org/packages/app-misc/screen)[]] or [[[net-dialup/minicom]](https://packages.gentoo.org/packages/net-dialup/minicom)[]]. For more information refer to the [\[1\]](https://www.udoo.org/tutorial/connecting-via-serial-cable/).

Note with U-Boot uEnv.txt patch above, you can make the sdcard a single ext4 partition with /boot directory instead of the two partitions shown below. The patch also allows you to change the rootfs via the \"mmcroot\" variable.

### [Preparing the SD card]

  ----------------------------------------------------------------------------------------------------- ------------ ----------------- ----------------
  Partition                                                                                             Filesystem   Size              Description
  [/dev/mmcblk0p1]   ext2         100 MB            Boot partition
  [/dev/mmcblk0p2]   ext4         Rest of SD card   Root partition
  ----------------------------------------------------------------------------------------------------- ------------ ----------------- ----------------

** Note**\
With kernel 4.9.x or later use [/dev/mmcblk0] instead of [/dev/mmcblk1] (i.e. [/dev/mmcblk0p1] will be the first partition on the SD card). The device names have changed back and forth a couple of times to accommodate another potential SD card.

As noted above, a single partition scheme can be used with mainline U-Boot when using an ext2/3/4 formatted root partition. However when using a Btrfs formatted root partition (or other unsupported filesystem), an ext2/3/4 or fat32 formatted boot partition is required.

#### [Extract stage 3]

Get the latest [stage 3](http://distfiles.gentoo.org/releases/arm/autobuilds/current-stage3-armv7a_hardfp/) and extract it to the root partition:

`root `[`#`]`cd /mnt/sdcard-root `

`root `[`#`]`tar xvjpf /path/to/download/stage3-*.tar.bz2 `

#### [][Edit /etc/fstab]

Edit on the root partition on the SD card [/etc/fstab]:

[FILE] **`/etc/fstab`**

    /dev/mmcblk0p1          /boot           ext2            noauto,noatime  1 2
    /dev/mmcblk0p2          /               ext4            noatime         0 1

    #/dev/SWAP              none            swap            sw              0 0
    #/dev/cdrom             /mnt/cdrom      auto            noauto,ro       0 0
    #/dev/fd0               /mnt/floppy     auto            noauto          0 0

#### [Set the root password]

To be able to login later we need to set a root password, we create password hash and edit it to the [/etc/shadow].

`root `[`#`]`openssl passwd -1 `

`root `[`#`]`nano -w /mnt/sdcard-root/etc/shadow `

Replace the star or current hash of the root user with the output from the command above.

#### [Enable the serial console]

To have a serial console available after booting, change the `s0` line to the following:

[FILE] **`/mnt/sdcard-root/etc/inittab`**

    s0:12345:respawn:/sbin/agetty -L 115200 ttymxc0 vt100

### [Kernel]

#### [][Mainline (or Gentoo sources)]

The mainline kernel 3.19+ and [[[sys-kernel/gentoo-sources]](https://packages.gentoo.org/packages/sys-kernel/gentoo-sources)[]] has great support for Udoo devices, complete with working graphics and networking.

Create the install directories:

`root `[`#`]`mkdir -p /var/build/Udoo/root/boot `

** Note**\
The install directories are where the kernel, modules and devices trees will be installed. In this article [/var/build/Udoo/root] is used as an intermediate root directory. Any directory can be used, even the actual root directory of the device.

Setup the cross-compilation environment:

`root `[`#`]`export ARCH="arm" `

`root `[`#`]`export CROSS_COMPILE="armv7a-hardfloat-linux-gnueabi-" `

`root `[`#`]`export INSTALL_PATH="/var/build/Udoo/root/boot" `

`root `[`#`]`export INSTALL_MOD_PATH="/var/build/Udoo/root" `

Configure the kernel:

`root `[`#`]`cd /path/to/kernel/source `

`root `[`#`]`make imx_v6_v7_defconfig `

`root `[`#`]`make menuconfig `

Build and install the kernel (zImage):

`root `[`#`]`make zImage `

`root `[`#`]`make zinstall `

The kernel is located at [arch/arm/boot/zImage]. The kernel will be installed at [/var/build/Udoo/root/boot/vmlinuz-\<kernel-version\>]

Build and install the kernel modules:

`root `[`#`]`make modules `

`root `[`#`]`make modules_install `

The kernel modules will be installed at [/var/build/Udoo/root/lib/modules/\<kernel-version\>/]

Build and install the device trees:

`root `[`#`]`make dtbs `

`root `[`#`]`make dtbs_install `

The device trees are located at [arch/arm/boot/dts/]. The device trees will be installed at [/var/build/Udoo/root/boot/dtbs/\<kernel-version\>/]

** Note**\
The above will build and install device trees for all i.MX devices. It is possible to build a device tree for a specific device only. For example, run [make imx6q-Udoo.dtb] to build the device tree for a Udoo Quad/Dual. The device tree will be located at [arch/arm/boot/dts/imx6q-udoo.dtb], and needs to be copied manually to [/var/build/Udoo/root/boot/dtbs/\<kernel-version\>/]

The kernel, modules and devices trees can now be installed to the actual root directory of the device:

`root `[`#`]`cp -r /var/build/Udoo/root/ /path/to/actual/root `

#### [Latest patched version]

-   These [patches](https://rcn-ee.net/deb/xenial-armhf/) apply to the latest kernels. As of this writing you can apply them to sys-kernel/git-sources-4.xx or the matching gentoo-sources. Gentoo can do this automatically for you. Unzip the latest patch to [/etc/portage/patches/sys-kernel/git-sources] and create [/etc/portage/bashrc] as is documented here: [/etc/portage/patches](https://wiki.gentoo.org/wiki//etc/portage/patches "/etc/portage/patches").

`root `[`#`]`make imx_v6_v7_defconfig `

`root `[`#`]`make menuconfig `

Create the zImage and the dtb file

`root `[`#`]`make zImage `

`root `[`#`]`make imx6q-udoo.dtb `

`root `[`#`]`make modules `

`root `[`#`]`make modules_install `

You can find the individual patches here: [latest patches for OMAP, iMX, and other devcices](https://github.com/RobertCNelson/armv7-multiplatform)

Kernel Sources Summary:

-   gentoo-sources (or mainline vanilla)
    -   works, but is missing specific fixes and device features
-   armv7-multiplatform (mainline with embedded patches)
    -   cross-arm kernel build scripts (not an ebuild)
    -   includes lots of device fixes/patches plus baseline defconfig
-   armv7multi-sources (arm overlay, latest is 4.17.7-r8)
    -   same as gentoo sources plus patch from armv7-multiplatform, plus extra patches
    -   in particular, the udoo serial/arduino patches for uploading firmware

\

#### [WiFi]

The following kernel configuration options are required for WiFi support. These options should already be enabled if the kernel was configured with `imx_v6_v7_defconfig` or the armv7-multiplatform config.

[KERNEL] **Enabling WiFi support**

        Device Drivers --->
          [*] Network device support --->
                [*]   Wireless LAN --->
                        <M>     Ralink driver support  --->
                                <M>   Ralink rt2500 (USB) support
                                <M>   Ralink rt2501/rt73 (USB) support
                                <M>   Ralink rt27xx/rt28xx/rt30xx (USB) support

Install the sys-kernel/linux-firmware and net-wireless/wpa_supplicant packages and you should be all set.

### [Bootloader]

U-Boot will normally wait three seconds for user input before attempting to boot. If user input is received, the boot sequence is interrupted and an interactive shell is started. If three seconds pass with no user input, U-Boot will look for an environment configuration on the first partition. If no valid environment configuration is found, U-Boot will display *\*\*\* Warning - bad CRC, using default environment*, and will then continue with the default environment configuration. This is where mainline U-Boot and Udoo U-Boot differ. Mainline supports [boot.scr] and extlinux.conf on the first partition, and it also supports [uEnv.txt] with the patch. The Udoo version of u-boot-imx supports both methods natively.

#### [Mainline]

##### [uEnv.txt]

Using the mainline U-Boot uEnv patch cut from 2017.11, create [uEnv.txt] in your boot partition or directory:

[FILE] **`uEnv.txt`**

    uname_r=4.14.5-armv7-x2

    cmdline=console=tty1 consoleblank=0 cma=16M uart_from_osc clk_ignore_unused net.ifnames=0

** Note**\
Make sure the value of uname_r matches the kernel you actually built (the above matches the version string produced by the build scripts from the [LinuxOnArm wiki](https://eewiki.net/display/linuxonarm/UDO). The kernel parameter cma=16M is enough for console video, but if you want accelerated X then replace \"cma=16M\" with \"gpumem=256M\". You can also omit the video parameter with newer kernels and it \*should\* default to 1080p.

** Warning**\
Kernel versions above 4.12 have been known to not boot fully without the extra uart/clk arguments shown above. As shown boots fine.

\

##### [extlinux.conf]

Vanilla U-Boot also supports [Syslinux](https://wiki.gentoo.org/wiki/Syslinux "Syslinux") style boot configuration. U-Boot only borrows a small subset of the Syslinux [configuration](http://www.syslinux.org/wiki/index.php?title=Config) options, and does not require Syslinux itself. This is much simpler than using [boot.scr] or applying patches to add [uEnv.txt] support.

Create the [extlinux] directory:

`root `[`#`]`mkdir /boot/extlinux`

Create the following configuration and adjust accordingly:

[FILE] **`/boot/extlinux/extlinux.conf`**

    PROMPT 1
    TIMEOUT 50
    DEFAULT linux

    LABEL linux
    KERNEL /vmlinuz-4.14.0
    FDTDIR /dtbs/4.14.0
    APPEND console=tty1 consoleblank=0 cma=16M net.ifnames=0 video=HDMI-A-1:1920x1080

Adjust the video argument to match your display.

** Note**\
The `KERNEL` and `FDTDIR` paths are relative to the root of the boot partition. If a boot partition is not used, adjust accordingly.

\

### [Continue Gentoo install]

Steps that should be done right after the installation:

1.  setup network
2.  set date
3.  emerge-webrsync
4.  emerge ntpd
5.  /etc/init.d/sshd

[Gentoo arm install Handbook](http://www.gentoo.org/doc/en/handbook/handbook-arm.xml)

### [][Graphics drivers (FOSS)]

Although it\'s not fully integrated yet, there is useful 2D/3D functionality in the latest FOSS drivers, some of which were only recently added to the [Gentoo ARM overlay](https://github.com/gentoo/arm).

-   mesa - the latest releases enable vivante/imx (be sure and enable gallium/glx/dri3 in mesa)
-   libdrm - enables \"experimental\" vivante/etnaviv api
-   xf86-video-armada - builds multiple drivers, depends on various versions of dependencies below
-   libdrm-armada - gpu shim
-   libetnaviv (latest is header-only, older is a library)
-   galcore-headers - public \"etnaviv\" interface

Note: the packages in the main portage tree call the imx VIDEO_CARD \"vivante\" but in the above Xorg drivers vivante refers to the legacy GAL drivers which are disabled (the FOSS pieces should probably all be called etnaviv). To try the FOSS graphics stack, you should set `VIDEO_CARDS="vivante"` in your [make.conf] file and add the ARM overlay. Also note that `VIDEO_CARDS="imx"` has been removed in Xorg 1.20 and above.

So far the imx/armada drivers seem to work for 2D in X but the log shows an error initializing the etnadrm_gpu driver and claims to fall back to swrast 3D. Still, with dri3 and vivante enabled glxgears gets over 110 fps in Xorg, so there is that\... (if you only have dri2 enabled then it really is swrast @ 22 fps)

### [][Sam3 Microcontroller (Arduino Due compatible)]

The main \"thing\" about Udoo boards is that they have a built-in Arduino-compatible ARM cortex-M microcontroller. The original Udoo Quad/Dual boards have an Atmel Sam3 (equivalent to a Cortex-M3, no FPU) connected directly to the i.MX ARM via serial (ttymxc3 on the ARM side). This can be adjusted via a jumper on the board. As of the 4.14 mainline kernel there is a new imx-rproc driver similar to the BeagleBone PRU drivers (as well as the rpmsg char interface).

You can use the latest crossdev-99999999 to build a multilib arm-none-eabi toolchain for ARM embedded processors; currently gcc 5.4.0_r4 and 6.4.0 in the ada-overlay have some extra patches for armv8-M and somewhat saner support for thumb/hardfloat/softfloat but it should be possible with the current versions in the main Portage tree. Without the extra patches, you should add \"\--with-multilib-list=aprofile\" to EXTRA_ECONF on your crossdev command, and for bare metal toolchains you should also add USE=\"-nptl -sanitize -vtv\".

## [Hardware Random Number Generator]

The FSL/NXP i.MX6 boards have a hardware random number generator.^[\[2\]](#cite_note-2)^

All of the Freescale CAAM kernel options should be enabled as modules (built-in may have trouble with rngd).

Driving /dev/random with the hardware CAAM module is done via the following steps.

### [Install rng-tools]

`root `[`#`]`emerge -av sys-apps/rng-tools`

### [Load modules]

`root `[`#`]`modprobe caamrng `

`root `[`#`]`modprobe caamhash`

### [][Apply settings in /etc/conf.d/rngd]

Add the following to /etc/conf.d/rngd

[FILE] **`/etc/conf.d/rngd`**

    NO_TPM=1
    RNGD_OPTS="-o /dev/random -r /dev/hwrng"

### [][Check that /dev/random is slow]

To verify that we have done everything correctly, open a new terminal and do:

`user `[`$`]`cat /dev/random`

It will start displaying gibberish (random) but will stop at some point or at least slow down. Now issue CTRL+C to stop it.

### [Restart rngd]

`root `[`#`]`/etc/init.d/rngd restart`

### [Test if it works]

Again, issue:

`user `[`$`]`cat /dev/random`

in another terminal. Now the random information should be flowing faster than the first time around. Now issue CTRL+C to stop it.

Using the kernel entropy source (a USB keyboard attached, display connected) /dev/random spews approx. 100 \"chars\" of random information before it blocks. After loading the module and starting rng-tools, it should print out many lines without blocking.

### [Add rng-tools to boot]

If all is good, add rngd to boot.

`root `[`#`]`rc-update add rngd boot`

### [Add loading of caamrng to boot]

Add the following to /etc/conf.d/modules so that the modules get loaded at boot

[FILE] **`/etc/conf.d/modules`**

    modules="caamrng caamhash"

## [Applications]

The main application of \"concern\" for Udoo quad/dual boards is a functioning Arduino core + IDE so sketches can be compiled and uploaded to the sam3 as expected. In this case upstream maintains their own forks of both the Arduino IDE and bossac uploader, and it\'s all tied together with their vendor kernel forks. This needs several patches on both the kernel and application side, so there are corresponding overlays required to get all the right bits:

-   [arduino overlay](https://github.com/sarnold/arduino-overlay) - ebuilds for arduino 1.8.5 and bossa 1.3 (USE=udooqdl)
-   [arm support overlay](https://github.com/gentoo/arm) - kernel ebuilds with patches for arduino manager and dts

Note that crossdev-99999999 is also required for basic cortex-M multilib support, and you will also probably want to set the multilib-list configure option for gcc (see below).

An optional overlay contains ebuilds and patches for Ada language support in the toolchain, as well as gcc-6.4.0 patches for amrv8-M support (not required for Udoo).

-   [ada toolchain overlay](https://github.com/sarnold/ada-overlay) - ebuilds/eclass with Ada language and armv8-M patches. Note that if you want to build your cross toolchain with Ada support you must first (re)build your system gcc with USE=\"ada.\" See the [overlay readme](https://github.com/sarnold/ada-overlay/blob/master/README.md) for details.

### [Arduino IDE]

[![Screenshot of Nerdboy\'s Udoo desktop with latest Arduino IDE.](/images/thumb/3/33/Slim-arduino.png/600px-Slim-arduino.png)](https://wiki.gentoo.org/wiki/File:Slim-arduino.png)

[](https://wiki.gentoo.org/wiki/File:Slim-arduino.png "Enlarge")

[Steve Arnold (nerdboy)](https://wiki.gentoo.org/wiki/User:Nerdboy "User:Nerdboy") \'s Udoo desktop.

Due to the way the hardware is integrated, including shared pins and a dedicated serial interface between the ARM side and the sam3 side, the arduino IDE takes several Udoo-specific patches. All of them are required, including kernel/dts patches, arduino board patches, and a patched version of the bossa upload tool. The following packages and USE flags will pull all the right integration bits.

First build your favorite light-weight desktop (eg, lxqt) and use [eselect repository] to add the arduino-overlay and arm overlay. Make sure you\'re running the latest armv7multi kernel with arduino patches, then get rid of old icedtea-7 and install icedtea-8 and crossdev-99999999. Use crossdev to build the arm-none-eabi toolchain.

The desktop pic shows the arduino IDE after uploading one of the example sketches that reads characters from the IDE serial console (sorry no blinky lights). Note you need to select the [/dev/ttymxc3] port as well as the board.

** Note**\
Feel free to pluck the Udoo patches from the arm overlay and apply them on top the corresponding version of [[[sys-kernel/gentoo-sources]](https://packages.gentoo.org/packages/sys-kernel/gentoo-sources)[]] if you prefer.

#### [eselect repository]

Install [[[app-eselect/eselect-repository]](https://packages.gentoo.org/packages/app-eselect/eselect-repository)[]] and [[[dev-vcs/git]](https://packages.gentoo.org/packages/dev-vcs/git)[]] if they do not yet exist:

`root `[`#`]`emerge --ask --noreplace app-eselect/eselect-repository dev-vcs/git`

Add and sync the extra overlays with these commands:

`root `[`#`]`eselect repository enable arm_support `

`root `[`#`]`eselect repository add arduino git `[`https://github.com/sarnold/arduino-overlay.git`](https://github.com/sarnold/arduino-overlay.git)` `

`root `[`#`]`emerge --sync arm_support arduino`

### [Required Packages]

`root `[`#`]`USE="imx udooqdl" emerge -av armv7multi-sources`

For arduino to work, you need either armv7multi-sources-4.14.5-r2 or armv7multi-sources-4.14.6-r2.

`root `[`#`]`emerge -av icedtea`

Default USE flags for icedtea should be fine.

`root `[`#`]`USE="udooqdl" emerge -av arduino`

For arduino 1.8.5 you need USE=\"udooqdl\" and it should pull in bossa 1.3 which has the Udoo sam3 upload patches.

Finally, for the toolchain you want crossdev-99999999 and something like this crossdev command:

`root `[`#`]`PORTDIR_OVERLAY="/usr/local/cortex-m3" USE="graphite hardened -nptl multitarget lzma multilib -openmp -fortran -go -jit -pch -sanitize -vtv" crossdev -t arm-none-eabi --genv 'EXTRA_ECONF="--with-newlib --disable-decimal-float --enable-plugins --enable-libstdcxx-time=no --with-multilib-list=aprofile" USE="multilib"' --g 5.4.0-r3 --b 2.27-r1 --lenv 'USE="newlib-nano"' -s4 --ex-gdb --show-fail-log`

** Note**\
The PORTDIR_OVERLAY path above is where you want the crossdev output overlay to go.

If all goes well (and it should) you will see a new entry in your list of system compilers:

`root `[`#`]`gcc-config -l`

     [1] arm-none-eabi-5.4.0
     [2] arm-none-eabi-5.4.0-hardenednopie
     [3] arm-none-eabi-5.4.0-vanilla
     [4] arm-none-eabi-6.4.0 *

     [5] armv7a-hardfloat-linux-gnueabi-4.9.4
     [6] armv7a-hardfloat-linux-gnueabi-4.9.4-hardenednopie
     [7] armv7a-hardfloat-linux-gnueabi-4.9.4-hardenednopiessp
     [8] armv7a-hardfloat-linux-gnueabi-4.9.4-hardenednossp
     [9] armv7a-hardfloat-linux-gnueabi-4.9.4-vanilla
     [10] armv7a-hardfloat-linux-gnueabi-5.4.0
     [11] armv7a-hardfloat-linux-gnueabi-5.4.0-hardenednopie
     [12] armv7a-hardfloat-linux-gnueabi-5.4.0-hardenednopiessp
     [13] armv7a-hardfloat-linux-gnueabi-5.4.0-hardenednossp
     [14] armv7a-hardfloat-linux-gnueabi-5.4.0-vanilla
     [15] armv7a-hardfloat-linux-gnueabi-6.4.0 *
     [16] armv7a-hardfloat-linux-gnueabi-7.2.0

     [17] avr-6.4.0 *

Check your available multilib targets:

`root `[`#`]`arm-none-eabi-gcc -print-multi-lib`

    .;
    thumb;@mthumb
    v7-a;@march=armv7-a
    v7ve;@march=armv7ve
    v8-a;@march=armv8-a
    v7-a/fpv3/softfp;@march=armv7-a@mfpu=vfpv3-d16@mfloat-abi=softfp
    v7-a/fpv3/hard;@march=armv7-a@mfpu=vfpv3-d16@mfloat-abi=hard
    v7-a/simdv1/softfp;@march=armv7-a@mfpu=neon@mfloat-abi=softfp
    v7-a/simdv1/hard;@march=armv7-a@mfpu=neon@mfloat-abi=hard
    v7ve/fpv4/softfp;@march=armv7ve@mfpu=vfpv4-d16@mfloat-abi=softfp
    v7ve/fpv4/hard;@march=armv7ve@mfpu=vfpv4-d16@mfloat-abi=hard
    v7ve/simdvfpv4/softfp;@march=armv7ve@mfpu=neon-vfpv4@mfloat-abi=softfp
    v7ve/simdvfpv4/hard;@march=armv7ve@mfpu=neon-vfpv4@mfloat-abi=hard
    v8-a/simdv8/softfp;@march=armv8-a@mfpu=neon-fp-armv8@mfloat-abi=softfp
    v8-a/simdv8/hard;@march=armv8-a@mfpu=neon-fp-armv8@mfloat-abi=hard
    thumb/v7-a;@mthumb@march=armv7-a
    thumb/v7ve;@mthumb@march=armv7ve
    thumb/v8-a;@mthumb@march=armv8-a
    thumb/v7-a/fpv3/softfp;@mthumb@march=armv7-a@mfpu=vfpv3-d16@mfloat-abi=softfp
    thumb/v7-a/fpv3/hard;@mthumb@march=armv7-a@mfpu=vfpv3-d16@mfloat-abi=hard
    thumb/v7-a/simdv1/softfp;@mthumb@march=armv7-a@mfpu=neon@mfloat-abi=softfp
    thumb/v7-a/simdv1/hard;@mthumb@march=armv7-a@mfpu=neon@mfloat-abi=hard
    thumb/v7ve/fpv4/softfp;@mthumb@march=armv7ve@mfpu=vfpv4-d16@mfloat-abi=softfp
    thumb/v7ve/fpv4/hard;@mthumb@march=armv7ve@mfpu=vfpv4-d16@mfloat-abi=hard
    thumb/v7ve/simdvfpv4/softfp;@mthumb@march=armv7ve@mfpu=neon-vfpv4@mfloat-abi=softfp
    thumb/v7ve/simdvfpv4/hard;@mthumb@march=armv7ve@mfpu=neon-vfpv4@mfloat-abi=hard
    thumb/v8-a/simdv8/softfp;@mthumb@march=armv8-a@mfpu=neon-fp-armv8@mfloat-abi=softfp
    thumb/v8-a/simdv8/hard;@mthumb@march=armv8-a@mfpu=neon-fp-armv8@mfloat-abi=hard

### [Required Devices]

Since this is an embedded device, you get bonus tty devices with funky names (yay!). In the case of Freescale/NXP they are mostly of the form ttymxcN where N is 1-9. By default on imx6 there is usually ttymxc0 or ttymxc1 for the serial console, which on Udoo quad/dual boards is one of the micro-USB connectors. The sam3 \"arduino\" part requires a second ttymxc3 serial port (which is enabled by a kernel patch) and a special device (also enabled by a kernel patch) to allow the uploader to control the port on the arduino (see below). The latter two devices require user-level permissions for the IDE, so we\'ll use the usual uucp group udev rules.

If you\'re running the patched kernel, you should see the following devices after boot-up:

`user `[`$`]`ls /dev/ttymxc* /dev/udoo*`

    /dev/ttymxc1  /dev/ttymxc3  /dev/udoo_ard

For the right permissions, udev defaults need to be changed; for now you can edit the default serial rules and add the following:

[FILE] **`/lib/udev/rules.d/50-udev-default.rules`**

    KERNEL=="ttymxc[2-3]", GROUP="uucp"
    KERNEL=="udoo_ard", GROUP="uucp", MODE="0660"

Make sure you are in the uucp group, and after \"udevadm trigger\" or a reboot, the device permissions should be:

`user `[`$`]`ls -l /dev/ttymxc* /dev/udoo*`

    crw--w---- 1 root tty  207, 17 Dec 15 20:56 /dev/ttymxc1
    crw-rw---- 1 root uucp 207, 19 Dec 15 22:09 /dev/ttymxc3
    crw-rw---- 1 root uucp 242,  0 Dec 31  1969 /dev/udoo_ard

Other than possibly a transient error if you open the IDE serial console right before it starts to flash, the arduino IDE should now be able to upload firmware with the default \"upload\" button. If you get an error message in the IDE about \"can\'t erase/reset device\" and the above output looks good, then make sure you emerged the arduino IDE and kernel sources with USE=\"udooqdl\" and your version of bossa is 1.3.

## [References]

1.  [[[↑](#cite_ref-1)] [[LinuxOnArm wiki UDOO page](https://eewiki.net/display/linuxonarm/UDOO)]]
2.  [[[↑](#cite_ref-2)] [[CAAM (Cryptographic Accelerator and Assurance Module)](https://www.digi.com/resources/documentation/digidocs/90001546/reference/bsp/cc6/r_caam.htm)]]