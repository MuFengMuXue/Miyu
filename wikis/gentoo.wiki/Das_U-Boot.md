---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                                                                                      General topics
                               [Introduction](https://wiki.gentoo.org/wiki/Embedded_Handbook/General/Introduction "Embedded Handbook/General/Introduction")
   [Compiling with QEMU user chroot](https://wiki.gentoo.org/wiki/Embedded_Handbook/General/Compiling_with_QEMU_user_chroot "Embedded Handbook/General/Compiling with QEMU user chroot")
            [Creating a cross-compiler](https://wiki.gentoo.org/wiki/Embedded_Handbook/General/Creating_a_cross-compiler "Embedded Handbook/General/Creating a cross-compiler")
       [Cross-compiling with Portage](https://wiki.gentoo.org/wiki/Embedded_Handbook/General/Cross-compiling_with_Portage "Embedded Handbook/General/Cross-compiling with Portage")
          [Cross-compiling the kernel](https://wiki.gentoo.org/wiki/Embedded_Handbook/General/Cross-compiling_the_kernel "Embedded Handbook/General/Cross-compiling the kernel")
          [Frequently asked questions](https://wiki.gentoo.org/wiki/Embedded_Handbook/General/Frequently_asked_questions "Embedded Handbook/General/Frequently asked questions")
                                                                                         Emulators
                                         [Qemu](https://wiki.gentoo.org/wiki/Embedded_Handbook/Emulators/Qemu "Embedded Handbook/Emulators/Qemu")
                                  [Armulator](https://wiki.gentoo.org/wiki/Embedded_Handbook/Emulators/Armulator "Embedded Handbook/Emulators/Armulator")
                                   [Hercules](https://wiki.gentoo.org/wiki/Embedded_Handbook/Emulators/Hercules "Embedded Handbook/Emulators/Hercules")
                                                                                        Bootloaders
                                                                           [Das U-Boot]
                                   [NeTTrom](https://wiki.gentoo.org/wiki/Embedded_Handbook/Bootloaders/NeTTrom "Embedded Handbook/Bootloaders/NeTTrom")
                                   [RedBoot](https://wiki.gentoo.org/wiki/Embedded_Handbook/Bootloaders/RedBoot "Embedded Handbook/Bootloaders/RedBoot")
                                   [SH-LILO](https://wiki.gentoo.org/wiki/Embedded_Handbook/Bootloaders/SH-LILO "Embedded Handbook/Bootloaders/SH-LILO")
  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

\

** Tip**\
Rather than duplicate existing information, please select your version in the [upstream documentation](https://u-boot.readthedocs.io/en/latest/) and check the main [wiki](http://www.denx.de/wiki/view/DULG/UBoot).

**Das U-Boot** (subtitled *the Universal Boot Loader* and often shortened to **U-Boot**)^[\[1\]](#cite_note-uboot_wp-1)^ is an open-source boot loader used in embedded devices to initialize the hardware and load the device\'s [kernel](https://wiki.gentoo.org/wiki/Kernel "Kernel"). It is available for a number of computer architectures, including [PowerPC](https://wiki.gentoo.org/wiki/PowerPC "PowerPC"), [ARM](https://wiki.gentoo.org/wiki/ARM "ARM"), [MIPS](https://wiki.gentoo.org/wiki/MIPS "MIPS"), AVR32, x86, 68k, Nios II, and MicroBlaze.^[\[1\]](#cite_note-uboot_wp-1)^

U-Boot is more than a simple boot loader, providing an interactive command-line interface or shell. This allows users and developers to load and boot a kernel from a variety of sources, including flash memory, SD (TF) cards, SATA drives, or over a network using TFTP. Its scripting capabilities and memory manipulation commands make it a valuable tool for debugging and system development.

## Contents

-   [[1] [U-Boot Mind-set]](#U-Boot_Mind-set)
-   [[2] [Gentoo Specific Instructions]](#Gentoo_Specific_Instructions)
-   [[3] [Building U-boot for an ARMv7 Target]](#Building_U-boot_for_an_ARMv7_Target)
-   [[4] [Building U-boot for an ARM64 Target]](#Building_U-boot_for_an_ARM64_Target)
-   [[5] [Gentoo U-boot Examples]](#Gentoo_U-boot_Examples)
-   [[6] [External References]](#External_References)
-   [[7] [Booting a new distro kernel with U-Boot]](#Booting_a_new_distro_kernel_with_U-Boot)
    -   [[7.1] [Prerequisites]](#Prerequisites)
    -   [[7.2] [Fallback extlinux.conf method]](#Fallback_extlinux.conf_method)

## [U-Boot Mind-set]

Aside from a few odd/legacy boards, most of the current device support in u-boot should follow the Linux kernel devicetree and u-boot driver models, albeit with each vendor on their own upgrade cycle. That said, well-maintained SoC families should have a device tree file and corresponding defconfig, but more importantly, most current board configs should have at least CONFIG_DISTRO_DEFAULTS and basic EFI support enabled. As of v2022.10 there were 355 defconfig files with CONFIG_DISTRO_DEFAULTS enabled.

To effectively use u-boot on a given device (board), the following information is generally required:

-   any additional source repositories (eg, TFA)
-   which build artifacts are needed (eg, flash-image.bin)
-   how and where are these artifacts installed (eg, dd to MMC device, SPI flash via u-boot command, or external flash tool)
-   debug UART connector and device names (eg, debug header or micro-USB/FTDI)

Board examples:

Each board is different and may or may not have an accessible debug header or on-board USB-UART. Check vendor docs and wikis, u-boot docs and search engines. Most boards with RPI-compatible header can use the UART pins near one end of the 40-pin header. For serial console to work, inittab needs the correct device name, baud rate, and term type.

-   esspressobin (**ttyMV0**) - micro-USB connector on the \"front\" side of the board is debug UART
-   beaglebone (old: **ttyO0** \| new: **ttyS0**) - 6-pin debug UART header behind the USB-A host connector
-   orange-pi variants (**ttyS0**) - 3-pin debug UART header, often near ethernet or USB host connector
-   rockchip variants (**ttyS2 @ 1500000**) - 3 pins for UART2 on RPI header (the end near the USB connector)

Note for the latter two examples above, the device name may end in a different number depending on how many UART ports are actually there and enabled.

## [Gentoo Specific Instructions]

There is no package for the **Das U-boot** source code. Follow the instructions in the [documentation](http://www.denx.de/wiki/U-Boot/Documentation) for obtaining the source from git or an archived release.

There is a package for the Das U-boot utility tools (such as **mkimage**), see [u-boot-tools](https://wiki.gentoo.org/wiki/U-boot-tools "U-boot-tools").

It is most likely the build will be cross-compiled. See [Crossdev](https://wiki.gentoo.org/wiki/Crossdev "Crossdev").

## [Building U-boot for an ARMv7 Target]

Building the bootloader for a supported armv7 FOSS device such as beaglebone is fairly simple and straightforward, and generally only requires the u-boot sources.

Build target cross-compiler:

`root `[`#`]`crossdev -t armv7a-unknown-linux-gnueabihf`

Download u-boot:

`user `[`$`]`git clone -b v2023.04 `[`https://github.com/u-boot/u-boot`](https://github.com/u-boot/u-boot)

`user `[`$`]`cd u-boot/`

Find the configuration for your device; if there is no exact match in the existing defconfigs, there may be a close enough match (eg, in the case of Allwinner fruity-pi or Rockchip 3328 boards).

Configure and build u-boot:

`user `[`$`]`make ARCH=arm CROSS_COMPILE=armv7a-unknown-linux-gnueabihf- distclean`

`user `[`$`]`make ARCH=arm CROSS_COMPILE=armv7a-unknown-linux-gnueabihf- <your_device>_defconfig`

`user `[`$`]`make ARCH=arm CROSS_COMPILE=armv7a-unknown-linux-gnueabihf-`

For most FOSS developmment boards, the resulting u-boot images are intended for booting SDCard/EMMC, or possibly installing in SPI flash.

For example, the udoo IMX6quad u-boot binfiles are:

1.  SPL
2.  u-boot.img

Use the **dd** command to install them in the space before the first partition. Note this will destroy all data on the card!

Erase partition table/labels on microSD card:

`root `[`#`]`dd if=/dev/zero of=$ bs=1M count=10`

Install bootloader bins:

`root `[`#`]`dd if=./SPL of=$ seek=1 bs=1k`

`root `[`#`]`dd if=./u-boot.img of=$ seek=69 bs=1k`

where usually DISK=/dev/sdX

## [Building U-boot for an ARM64 Target]

Building the bootloader for at least a few supported arm64 FOSS devices such as rock-pi-4 is still simple-ish, and only requires 2 cross-compilers and 2 source trees (and possibly some blobs). The example rk3399 is a fully supported platform in both TFA and u-boot.

-   check board vendor docs and repos for bootloader forks and additional bootloader repos
-   check u-boot docs and source for board support
-   check TFA docs and source for platform support and possible build recipes

Build target cross-compilers:

`root `[`#`]`crossdev -t arm-none-eabi`

`root `[`#`]`crossdev -t aarch64-unknown-linux-gnu`

`user `[`$`]`export M0_CROSS_COMPILE=arm-none-eabi-`

Download TFA:

`user `[`$`]`git clone `[`https://github.com/ARM-software/arm-trusted-firmware`](https://github.com/ARM-software/arm-trusted-firmware)

`user `[`$`]`cd arm-trusted-firmware/`

Configure and Build:

`user `[`$`]`make CROSS_COMPILE=aarch64-unknown-linux-gnu- realclean`

`user `[`$`]`make CROSS_COMPILE=aarch64-unknown-linux-gnu- PLAT=rk3399`

Export BL31.elf:

`user `[`$`]`` export BL31=`pwd`/build/rk3399/release/bl31/bl31.elf ``

Download u-boot:

`user `[`$`]`git clone -b v2023.04 `[`https://github.com/u-boot/u-boot`](https://github.com/u-boot/u-boot)

`user `[`$`]`cd u-boot/`

Configure and Build:

`user `[`$`]`make ARCH=arm CROSS_COMPILE=aarch64-unknown-linux-gnueabihf- distclean`

`user `[`$`]`make ARCH=arm CROSS_COMPILE=aarch64-unknown-linux-gnueabihf- rock-pi-4-rk3399_defconfig`

`user `[`$`]`make ARCH=arm CROSS_COMPILE=aarch64-unknown-linux-gnueabihf-`

Here the output is one or more u-boot blobs for installing on SDCard/EMMC but for other boards using SPI flash images (eg, espressobin), the output might come from TFA, as u-boot is just one of the input source trees for Marvell Armada. For modern rockchip devices and relatively recent u-boot/TFA, the build output is the combined SPL/TPL and dtb flash file `u-boot-rockchip.bin`, where most of the Internet still refers to the following dtb and loader files shown below. Using the single flash file with `seek=64` should be equivalent to the steps shown below.

The (older) rock-pi-4 u-boot binfiles are:

1.  idbloader.img
2.  u-boot.itb

Use the **dd** command to install them in the space before the first partition. Note this should not destroy all data on the card IFF the first partition starts at 16MB (32768 sectors for 512 byte sectors).

Erase partition table/labels on microSD card:

`root `[`#`]`dd if=/dev/zero of=$ bs=1M count=20`

Install bootloader bins:

`root `[`#`]`dd if=./idbloader.img of=$ seek=64 `

`root `[`#`]`dd if=./u-boot.itb of=$ seek=16384`

where usually DISK=/dev/sdX

## [Gentoo U-boot Examples]

-   [ESPRESSOBin](https://wiki.gentoo.org/wiki/ESPRESSOBin "ESPRESSOBin") arm64 SPI flash
-   [Udoo](https://wiki.gentoo.org/wiki/Udoo "Udoo") armv7 SDCard (old)
-   [PINE64_ROCKPro64/Installing_U-Boot](https://wiki.gentoo.org/wiki/PINE64_ROCKPro64/Installing_U-Boot "PINE64 ROCKPro64/Installing U-Boot") arm64 SDCard

## [External References]

-   [https://trustedfirmware-a.readthedocs.io/en/lts-v2.10.2/plat/index.html](https://trustedfirmware-a.readthedocs.io/en/lts-v2.10.2/plat/index.html)
-   [https://u-boot.readthedocs.io/en/v2024.01/](https://u-boot.readthedocs.io/en/v2024.01/)
-   [https://github.com/sarnold/u-boot-ATF-manifest/tree/marvell-armada](https://github.com/sarnold/u-boot-ATF-manifest/tree/marvell-armada)
-   [https://github.com/sarnold/u-boot-ATF-manifest/tree/rockchip-libre](https://github.com/sarnold/u-boot-ATF-manifest/tree/rockchip-libre)
-   [https://github.com/sarnold/u-boot-ATF-manifest/tree/allwinner-a64](https://github.com/sarnold/u-boot-ATF-manifest/tree/allwinner-a64)
-   [https://forum.digikey.com/c/embedded/linux-guides/71/l/top](https://forum.digikey.com/c/embedded/linux-guides/71/l/top)

## [Booting a new distro kernel with U-Boot]

In addition to new boards, U-boot development has also been focused on moving existing SoC families to newer APIs and driver models, including syncing U-boot with kernel devicetree files periodically and pushing towards more agnostic boot flows and standardized distribution support. A recent U-boot version should support booting several different kernel image formats from a variety of media.

Depending on which u-boot bits are configured/used, several types of files can be booted:

-   raw binaries
-   FIT images
-   various kernel images
-   legacy U-Boot images
-   UEFI binaries

which can then be used with multiple boot methods:

-   legacy boot.scr
-   extlinux configuration (ala syslinux)
-   EFI boot

*However*, the extlinux boot method **does not** use the bootefi command, and *only* the bootefi command can boot a (grub) EFI binary. The upshot is extlinux will fail to boot the new signed distribution kernels ([[[sys-kernel/gentoo-kernel-bin]](https://packages.gentoo.org/packages/sys-kernel/gentoo-kernel-bin)[]] version 6.5.x and up) but u-boot can still be used to boot the EFI grub binary (using the minimum GPT partition layout, eg, a 512 MB ESP and the rest in ext4 rootfs).

#### [Prerequisites]

The following boot flow was tested on espressobin v5 and both nanopi-r5c (rk3568) and rk3328 libre board using the appropriate u-boot builds for each board.

1.  stage3/4 arm64 on USB stick, SSD, or SDCard
2.  make a small dracut configuration to match your boot requirements
3.  check u-boot environment/defconfig for distro_bootcmd or bootflow, upgrade/rebuild u-boot if needed
4.  emerge [[[sys-kernel/gentoo-kernel-bin]](https://packages.gentoo.org/packages/sys-kernel/gentoo-kernel-bin)[]]
5.  emerge [[[sys-boot/grub]](https://packages.gentoo.org/packages/sys-boot/grub)[]] with efi support and [devicetree patches](https://github.com/VCTLabs/embedded-overlay)
6.  install grub with the removable flag, eg: `grub-install --target=arm64-efi --efi-directory=/boot/efi --removable`
7.  edit `/etc/default/grub` and set GRUB_DEFAULT_DTB to the appropriate dtb, eg `marvell/armada-3720-espressobin.dtb`
8.  add `efi=noruntime` to GRUB_CMDLINE_LINUX
9.  run `grub-mkconfig -o /boot/grub/grub.cfg`

According to both the TFA and U-boot docs, the trusted firmware approach should also work on at least some armv7 devices, eg, rk3288.

The following display shows the tested version(s) of the espressobin bootloader components, where almost everything is the latest/stable vendor and TFA versions, and u-boot was left at 2022.10:

[CODE] **U-Boot Env**

    TIM-1.0
    mv_ddr-devel-g2b37d92 DDR3 16b 1GB 2CS
    WTMI-devel-18.12.1-a3e1c67
    WTMI: system early-init
    CPU VDD voltage default value: 1.155V
    Setting clocks: CPU 1000 MHz, DDR 800 MHz
    CZ.NIC's Armada 3720 Secure Firmware v2022.06.11 (Oct 24 2023 20:33:51)
    Running on ESPRESSObin
    NOTICE:  Booting Trusted Firmware
    NOTICE:  BL1: lts-v2.8.9(release):lts-v2.8.9
    NOTICE:  BL1: Built : 20:35:08, Oct 24 2023
    NOTICE:  BL1: Booting BL2
    NOTICE:  BL2: lts-v2.8.9(release):lts-v2.8.9
    NOTICE:  BL2: Built : 20:35:08, Oct 24 2023
    NOTICE:  BL1: Booting BL31
    NOTICE:  BL31: lts-v2.8.9(release):lts-v2.8.9
    NOTICE:  BL31: Built : 20:35:08, Oct 24 2023

    U-Boot 2022.10 (Oct 24 2023 - 20:32:43 -0700)

    DRAM:  1 GiB
    Core:  47 devices, 24 uclasses, devicetree: separate
    WDT:   Not starting watchdog@8300
    Comphy chip #0:
    Comphy-0: USB3_HOST0    5 Gbps
    Comphy-1: PEX0          5 Gbps
    Comphy-2: SATA0         6 Gbps
    Target spinup took 0 ms.
    AHCI 0001.0300 32 slots 1 ports 6 Gbps 0x1 impl SATA mode
    flags: ncq led only pmp fbss pio slum part sxs
    PCIe: Link down
    MMC:   sdhci@d0000: 0, sdhci@d8000: 1
    Loading Environment from SPIFlash... SF: Detected w25q32dw with page size 256 Bytes, erase size 4 KiB, total 4 MiB
    OK
    Model: Globalscale Marvell ESPRESSOBin Board
    Net:   eth0: ethernet@30000
    Hit any key to stop autoboot:  0
    =>

With kernel, initramfs, and updated grub.cfg in place, try booting your device; note this should work on whatever the current u-boot support is configured for, eg, MMC, USB, SATA, NVME, PXE, etc.

If it doesn\'t boot to the grub menu, check the following:

1.  grub install used the removable flag
2.  u-boot env shows appropriate bootcmd value
3.  verify EFI options in u-boot `.config` file
4.  append `efi=noruntime` to the kernel commandline

### [Fallback extlinux.conf method]

*Note that this method only works with unsigned/locally built kernel images.*

The basic requirement for the *distro_bootcmd* to run is the extlinux.conf file; this assumes the kernel and dtbs were installed using the default kernel install paths. A basic example would look something like the following:

[FILE] **`extlinux.conf`**

    LABEL Gentoo arm64
            KERNEL ../vmlinuz-5.10.14-aarch64-x0
            APPEND console=ttyS0,115200 root=/dev/mmcblk0p1 rw rootfstype=ext4 rootwait net.ifnames=0
            FDTDIR ../dtbs/5.10.14-aarch64-x0/

Create a file similar to the above under `/boot/extlinux`. Be sure to use tabs for indenting, and make sure to **use your console and root devices, along with your kernel version** in the config file you create:

`user `[`$`]`cd /mnt/gentoo/boot `

`user `[`$`]`sudo mkdir extlinux `

`user `[`$`]`sudo nano extlinux/extlinux.conf `

`user `[`$`]`cd -`

\

Authorship information[]

This page is based on a document formerly found on [gentoo.org](https://www.gentoo.org/).\
The following people contributed to the original document: **Mike Frysinger, Ned Ludd, Robin H. Johnson, Alex Tarkovsky, Alexey Shvetsov, Raúl Porcel, Joshua Saddler on April 28, 2013.**\
\
*[Editors: please do **not** add yourself here. Contributions are recorded on each article\'s associated history page, this list is only present to preserve authorship information, as wiki history does not allow for any external attribution.]*

1.  [[↑ ^[1.0](#cite_ref-uboot_wp_1-0)^ ^[1.1](#cite_ref-uboot_wp_1-1)^] [[Wikipedia U-Boot article](https://en.wikipedia.org/wiki/Das_U-Boot). denx.de. Retrieved 2025-08-23.]]