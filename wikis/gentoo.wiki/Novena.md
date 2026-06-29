[] This article has been flagged for not conforming to the [wiki guidelines](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Guidelines "Gentoo Wiki:Guidelines"). Please [help Gentoo out](https://wiki.gentoo.org/wiki/Help_improve_Gentoo_by_getting_involved_with_documentation!#Make_articles_conform_to_the_guidelines "Help improve Gentoo by getting involved with documentation!") by starting fixing things.

**Resources**

[[]][Home](http://www.kosagi.com/w/index.php?title=Novena_Main_Page)

[[]][Novena (computing platform)](https://en.wikipedia.org/wiki/Novena_(computing_platform) "wikipedia:Novena (computing platform)")

This document describes the Gentoo installation on Novena, an open hardware and FOSS-friendly computing platform (see Novena main page [www.kosagi.com](http://www.kosagi.com/w/index.php?title=Novena_Main_Page)).

## Contents

-   [[1] [Prerequisites]](#Prerequisites)
-   [[2] [Installation]](#Installation)
    -   [[2.1] [Base system]](#Base_system)
        -   [[2.1.1] [Partitioning]](#Partitioning)
        -   [[2.1.2] [Installing a stage tarball]](#Installing_a_stage_tarball)
        -   [[2.1.3] [Configuring compile options]](#Configuring_compile_options)
        -   [[2.1.4] [Choosing the right profile]](#Choosing_the_right_profile)
        -   [[2.1.5] [Configuring the USE variable]](#Configuring_the_USE_variable)
        -   [[2.1.6] [systemd]](#systemd)
        -   [[2.1.7] [Installing the sources]](#Installing_the_sources)
        -   [[2.1.8] [Additional notes]](#Additional_notes)
-   [[3] [Bootloader update]](#Bootloader_update)
-   [[4] [Kernel update]](#Kernel_update)
-   [[5] [The novena Overlay]](#The_novena_Overlay)
-   [[6] [MyriadRF]](#MyriadRF)
-   [[7] [Further Documentation]](#Further_Documentation)

## [Prerequisites]

The easiest way for installing Gentoo without initial bootstrapping is using the already shipped and working Debian installation, following a stage3 standard-installation on a second drive e.g. connected via USB. This guide focuses on the more complicated/Novena-unique parts and references to the original documentation whenever possible.

** Note**\
Alternatively, for an even faster start, you might consider trying one of the (unofficial) bootable Gentoo images for Novena from [this project](https://github.com/sakaki-/gentoo-on-novena). The provided images both use OpenRC, boot to a (reasonably populated) Xfce desktop, and come with the [novena] overlay (see [below](#novena-overlay)) pre-installed.

A Second hard disk has to be connected to USB (using the USB directly connected to the mainboard). This disk is further on referred to be found at [/dev/sdb] in the booted Novena/Debian system. After successfully booting the new Gentoo system later on, [/dev/sdb] will become [/dev/sda].

** Warning**\
Make sure the CPU is sufficient cooled e.g. using a fan. Long compilations can lead to an overheating.

## [Installation]

### [Base system]

Follow the standard installation for the **[x86]** architecture found in the [x86 Handbook](https://wiki.gentoo.org/wiki/Handbook:X86/Full/Installation "Handbook:X86/Full/Installation") with the following differences:

#### [Partitioning]

The bootloader and Linux kernel is stored on the internal SD-card of the Novena platform. After loading the kernel, the standard procedure is to mount the root partition by searching for an unique disk-ID 0x4e6f7653 (see [http://www.kosagi.com/w/index.php?title=Novena_Main_Page#Bootloader](http://www.kosagi.com/w/index.php?title=Novena_Main_Page#Bootloader)). The boot process is as follows: SD-card (u-boot → Linux kernel) → hard drive (root filesystem). Because of this, the disk-ID of the new hard drive has to be changed accordingly, e.g. using [fdisk]:

`root `[`#`]`fdisk /dev/sdb`

    Command (m for help): x

    Expert command (m for help): i

    Enter the new disk identifier: 0x4e6f7653

    Disk identifier changed from 0x00000000 to 0x4e6f7653.

    Expert command (m for help): r

    Command (m for help): w

The partition layout on the hard disk for the new installation is as follows:

  ----------- ----------------- -------------------------------------------------------------------------------------------
  Device      Filesystem type   Description
  /dev/sdb1   fat32             Boot (Not needed as boot files and kernel are placed on the SD-card but it doesn\'t hurt)
  /dev/sdb2   swap
  /dev/sdb3   ext4              Root filesystem
  ----------- ----------------- -------------------------------------------------------------------------------------------

The present partition on the SD-card is:

  ---------------- ----------------- -----------------------------------------
  Device           Filesystem type   Description
  /dev/mmcblk0p1   fat32             Boot (contains u-boot and kernel files)
  /dev/mmcblk0p2   swap
  /dev/mmcblk0p3   ext4              Root filesystem
  ---------------- ----------------- -----------------------------------------

\
The device naming has become confusing in the Gentoo handbook. The translation from partition used in this guide to the on in the handbook is:

  ------------------------------------------------------------------------------------------------ ------------------------------------------------------------------------------------------------
  Novena guide                                                                                     Handbook
  \[not present\]                                                                                  [/dev/sda1]
  [/dev/sdb1]   [/dev/sda2]
  [/dev/sdb2]   [/dev/sda3]
  [/dev/sdb3]   [/dev/sda4]
  ------------------------------------------------------------------------------------------------ ------------------------------------------------------------------------------------------------

#### [Installing a stage tarball]

The following information can be used to find the correct stage3 archive:

-   Architecture = arm
-   Subarchitecture = armv7a_hardf
-   Common subdirectory on mirror: \[host\]\[prefix\]/releases/arm/autobuilds/current-stage3-armv7a_hardfp/

#### [Configuring compile options]

Save CFLAGS for Novena can be found at: [Safe_CFLAGS#ARMv7-A.2FCortex-A9_MPCore](https://wiki.gentoo.org/wiki/Safe_CFLAGS#ARMv7-A.2FCortex-A9_MPCore "Safe CFLAGS"). The following changes in [/etc/portage/make.conf] work for Novena:

[FILE] **`/etc/portage/make.conf`**

    CHOST="armv7a-hardfloat-linux-gnueabi"
    CFLAGS="-O2 -march=armv7-a -mtune=cortex-a9 -mfpu=neon -mfloat-abi=hard -pipe -fomit-frame-pointer"
    CXXFLAGS="$"
    FEATURES="parallel-fetch ccache"
    CCACHE_SIZE="2G"

The iMX6 CPU contains a FPU with NEON instruction set so we can set \"-mfpu=neon\".

#### [Choosing the right profile]

Choose: default/linux/arm/10.0 (or newer)

#### [Configuring the USE variable]

Depends on individual needs, when in doubt leave it unchanged.

#### [systemd]

Nope, nobody needs it.

#### [Installing the sources]

The kernel is installed independent from the portage version, so no need to emerge it. See: [https://github.com/xobs/novena-linux](https://github.com/xobs/novena-linux)

At the time of writing the official [novena-linux] patches have been rebased only to version 4.4 of the kernel. An unofficial updated patchset (rebased to 4.7.2) is however available [here](https://github.com/sakaki-/novena-kernel-patches).

** Note**\
[Additionally, if] you choose to install the (unofficial) [novena] overlay (see [below](#novena-overlay)), you can also emerge one of the following two packages:

-   [sys-kernel/novena-sources]. Equivalent to [[[sys-kernel/gentoo-sources]](https://packages.gentoo.org/packages/sys-kernel/gentoo-sources)[]], but with the Novena-specific patchset applied in addition to the Gentoo one.
-   [sys-kernel/novena_hardened-sources]. Equivalent to [[[sys-kernel/hardened-sources]](https://packages.gentoo.org/packages/sys-kernel/hardened-sources)[]], but with the Novena-specific patchset applied. Has the [deblob] USE flag set by default; the resulting libre kernel is surprisingly usable on Novena (only Bluetooth, which requires a run-time firmware blob, is unavailable).

#### [Additional notes]

Installing ccache is a good idea as compiling on Novena can take some time.

After finishing the installation, shut down the system and connect the drive containing the newly installed gentoo installation to the SATA port. Gentoo should boot up successfully. If not, you still have Debian to check for errors (;

## [Bootloader update]

** Warning**\
Make a backup of the original SD-card! You have been warned.

A configuration and installation guide can be found at: [http://www.kosagi.com/w/index.php?title=U-boot-novena](http://www.kosagi.com/w/index.php?title=U-boot-novena)

Alternatively, if you choose to install the (unofficial) [novena] overlay (see [below](#novena-overlay)), you can also emerge [sys-boot/u-boot-novena], which will build U-Boot *and* install it (writing the second-stage bootloader to [/boot] and the first stage bootloader to the microSD card\'s MBR). A utility ([novena-install-spl]) is also created to allow you to write the SPL (first stage bootloader) to the MBR of other devices.

## [Kernel update]

** Warning**\
Make a backup of the original SD-card! You have been warned.

Novena uses the original Linux kernel extended by custom patches. Sources:

-   Kernel sources: [https://github.com/xobs/novena-linux](https://github.com/xobs/novena-linux)
-   Kernel modules: [https://github.com/xobs/gpu-viv](https://github.com/xobs/gpu-viv)

A configuration and installation guide can be found at: [http://www.kosagi.com/w/index.php?title=Novena_linux-kernel](http://www.kosagi.com/w/index.php?title=Novena_linux-kernel). The new kernel is installed by mounting the SD-card copying the resulting kernel:

`root `[`#`]`cd [kernel source directory] `

`root `[`#`]`mount /dev/mmcblk0p1 /boot `

`root `[`#`]`cp arch/arm/boot/zImage /boot/zimage # beware: target name is zimage (lower case "i")`

See also the notes [above](#novena-sources).

## [[The [novena] Overlay]]

An (unofficial) overlay for Gentoo users of the Novena SBC is available [here](https://github.com/sakaki-/novena-overlay). The overlay provides ebuilds shadowing all [xobs\' standard Novena packages from Debian](https://kosagi.com//w/index.php?title=Novena_Main_Page#Distro) ([novena-eeprom-gui] etc.), allowing you to enjoy these same facilities under Gentoo.

More details (including installation instructions) are in the project\'s GitHub page, but here is a brief summary of the provided ebuilds:

-   [sys-kernel/novena-sources] Full kernel sources for 4.7.2, with Gentoo and Novena patchsets.
-   [sys-kernel/novena_hardened-sources] As above, but with the hardened patchset; also, deblobbed by default.
-   [dev-embedded/novena-eeprom] Tool to view and edit the contents of the Novena\'s personality EEPROM.
-   [dev-embedded/novena-eeprom-gui] Qt GUI version of the above.
-   [dev-embedded/novena-heirloom] Support files for the heirloom laptop variant of Novena.
-   [dev-embedded/novena-usb-hub] Hub management tool (power control, etc.) for Novena.
-   [dev-embedded/u-boot-novena] Novena-packaged version of U-Boot.
-   [dev-embedded/update-senoko] Firmware loader for the Senoko battery/passthrough board.
-   [sys-firmware/senoko-chibios] Compile-from-source ChibiOS firmware for Senoko.
-   [media-sound/pulseaudio-novena] Support files for pulseaudio on Novena.
-   [net-wireless/novena-disable-ssp] Small daemon which disables SSP on all Bluetooth adaptors.
-   [sys-apps/irqbalance-novena] Distributes hardware interrupts across processors on Novena.
-   [dev-embedded/etna_viv] FOSS user-space driver for the Vivante GCxx GPUs (armada dependency).
-   [x11-libs/libdrm-armada] Userspace interface to kernel DRM services (armada dependency).
-   [x11-drivers/xf86-video-armada-novena] Accelerated X.org video driver for the Novena\'s i.MX6.
-   [x11-misc/xorg-novena] X.org configuration files for the armada video driver on Novena.
-   [sys-devel/portage-distccmon-gui] Easily view Portage jobs with distccmon-gui.
-   [dev-embedded/novena-meta] Merge this to pull in all baseline Novena packages (USE-flag controlled).

## [MyriadRF]

This is a Software Defined Radio (SDR) module which is plugable to the high speed interface of the Novena board. The following guide describes the installation of the drivers and simple usage demonstrations.

Further installation information:

-   Myriadrf driver for Novena: [https://github.com/myriadrf/Novena-RF/tree/master/driver](https://github.com/myriadrf/Novena-RF/tree/master/driver)
-   Myriadrf info: [https://myriadrf.org/blog/installing-the-novena-rf-driver-and-gnu-radio/](https://myriadrf.org/blog/installing-the-novena-rf-driver-and-gnu-radio/)
-   Soapy: [https://github.com/pothosware/SoapySDR/wiki/](https://github.com/pothosware/SoapySDR/wiki/)
-   Importand: Install UHD and SoapySDR, SoapySDR allone is not enough!

\[TODO: detailed description\]

## [Further Documentation]

-   HOWTOS (for Debian) [https://novena-guide.readthedocs.org/en/pvt2/](https://novena-guide.readthedocs.org/en/pvt2/)