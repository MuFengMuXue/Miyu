Construction of this page began 27 September 2023 (Work in Progress)

This is an inexpensive arm64 board\...

** Tip**\
\* There are evidently both \"rk3399-rock-4c-plus\" AND \"rk3399-rock-pi-4c-plus\" devices (or at least .dtb files for both) - but the difference is not clear

-   The product investigated below was delivered in packaging labeled ROCK 4C Plus, but trial-and-error revealed that its wifi (brcmfmac) works only using the \"rk3399-rock-pi-4c-plus.dtb\" device tree file
-   This product\'s wifi (brcmfmac) does NOT work when using the rk3399-rock-4c-plus.dtb device tree file

Overall status - this will be a complete from-scratch build. So far, the board has a gentoo rootfs system, a custom gentoo amd64-cross-compiled u-boot, and it has been transitioned from an initial ubuntu-compiled armbian kernel and initrd to a custom gentoo gcc-compiled kernel built from upstream sources (cdn.kernel.org) using \"rockchip-sources\" (a custom ebuild is available in the \"joetoo\" repository \-- [https://github.com/JosephBrendler/joetoo](https://github.com/JosephBrendler/joetoo)). The kernel was built on a gentoo amd64-cross-compiling desktop workstation, using the author\'s custom \"kernelupdate-embedded\" script, also available via ebuild at the link above.

[![](/images/thumb/d/d2/20230927_215324.jpg/600px-20230927_215324.jpg)](https://wiki.gentoo.org/wiki/File:20230927_215324.jpg)

[](https://wiki.gentoo.org/wiki/File:20230927_215324.jpg "Enlarge")

\"Rock 4c Plus packaging, annotated board layout\"

## Contents

-   [[1] [Hardware]](#Hardware)
    -   [[1.1] [Specifications]](#Specifications)
-   [[2] [SoC]](#SoC)
    -   [[2.1] [Accessories]](#Accessories)
    -   [[2.2] [Peripherals]](#Peripherals)
-   [[3] [GCC optimization^\[5\]^]](#GCC_optimization.5B5.5D)
-   [[4] [Gentoo Installation Options and Procedures]](#Gentoo_Installation_Options_and_Procedures)
    -   [[4.1] [Getting to Know the Board]](#Getting_to_Know_the_Board)
    -   [[4.2] [Bootloader Build and Installation]](#Bootloader_Build_and_Installation)
    -   [[4.3] [Assemble a Working Gentoo System]](#Assemble_a_Working_Gentoo_System)
    -   [[4.4] [Kernel Build and Installation]](#Kernel_Build_and_Installation)
-   [[5] [Install a Gentoo System \"From Scratch\"]](#Install_a_Gentoo_System_.22From_Scratch.22)
-   [[6] [Bootable gentoo system images]](#Bootable_gentoo_system_images)
-   [[7] [See also]](#See_also)
-   [[8] [External resources]](#External_resources)
-   [[9] [References]](#References)

## [Hardware]

### [Specifications]

  ------------ -------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Make/model                              Notes
  Board        Radxa ROCK Pi 4C+          dtb: rk3399-rock-pi-4c-plus.dtb
  SoC          Rockchip RK3399-T          [datasheet](https://dl.radxa.com/rockpi4/docs/hw/datasheets/Rockchip%20RK3399-T%20Datasheet%20V1.0-20210818.pdf)
  RAM          4GB                        LPDDR4
  Firmware     U-Boot                     rk3399_u-boot-2023.07.02 *(cross-compiled by user on Gentoo AMD64 desktop PC)*
               Trusted Firmware A (ATF)   rk3399-atf-2.9.0 *(cross-compiled by user on Gentoo AMD64 desktop PC)*
  Boot media   SD card                    eMMC not present but supported by u-boot standard. PXE not tested but supported by u-boot standard. USB boot option exists in u-boot documentation, but it was not tested (and there may be issues with that).^[\[1\]](#cite_note-1)[\[2\]](#cite_note-2)^
  ------------ -------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## [SoC]

** Note**\
The hardware is tested on kernel version 6.1.55-current-rockchip64 (ARM64). The 6.5.4 kernel has been built, but has not been tested yet.

+-------------+-------------------------------------------------------------------------------------------------------------------------------------------+-------------+----------------+---------------------------------------------------------------+
| Device      | Make/model                                                                                                                                | Status      | kernel drivers | Notes                                                         |
+-------------+-------------------------------------------------------------------------------------------------------------------------------------------+-------------+----------------+---------------------------------------------------------------+
| **CPU**     | 64bits hexa core processor Rockchip RK3399-T                                                                                              | Works       |                |                                                               |
|             |                                                                                                                                           |             |                |                                                               |
|             | 4 x Cortex-72, freq **1.5GHz**                                                                                                            |             |                |                                                               |
|             |                                                                                                                                           |             |                |                                                               |
|             | 2 x Cortex-A53, freq **1.0GHz**                                                                                                           |             |                |                                                               |
+-------------+-------------------------------------------------------------------------------------------------------------------------------------------+-------------+----------------+---------------------------------------------------------------+
| **GPU**     | 4 x Mali T860MP4 gpu, support OpenGL ES 1.1/2.0/3.0/3.1/3.2, Vulkan 1.0, Open CL 1.1 1.2, DX11.                                           | Works       |                |                                                               |
+-------------+-------------------------------------------------------------------------------------------------------------------------------------------+-------------+----------------+---------------------------------------------------------------+
| Memory      | LPDDR4 4GB 64bit dual channel LPDDR4@3200Mb/s                                                                                             | Works       |                |                                                               |
+-------------+-------------------------------------------------------------------------------------------------------------------------------------------+-------------+----------------+---------------------------------------------------------------+
| Storage     | eMMC connector                                                                                                                            | Works       |                | eMMC not present                                              |
|             |                                                                                                                                           |             |                |                                                               |
|             | μSD card (μSD slot supports up to 256 GB μSD card)                                                                                        |             |                |                                                               |
+-------------+-------------------------------------------------------------------------------------------------------------------------------------------+-------------+----------------+---------------------------------------------------------------+
| Display     | One Micro HDMI 2K up to 1440P@60                                                                                                          | Works       |                | Display video is present at boot on the right of 2 HDMI ports |
|             |                                                                                                                                           |             |                |                                                               |
|             | One Micro HDMI 4K 2.0 up to 4k@60 MIPI DSI 4 lanes via FPC connector Only two of HDMI 2k, HDMI 4K and MIPI DSI can work at the same time. |             |                |                                                               |
+-------------+-------------------------------------------------------------------------------------------------------------------------------------------+-------------+----------------+---------------------------------------------------------------+
| Audio       | 3.5mm jack HD codec that supports up to 24-bit/96KHz audio.                                                                               | Not tested  |                |                                                               |
+-------------+-------------------------------------------------------------------------------------------------------------------------------------------+-------------+----------------+---------------------------------------------------------------+
| Camera      | MIPI CSI 2 lanes via FPC connector, support up to 800 MP camera (0.3mm pitch connector).                                                  | Not tested  |                |                                                               |
+-------------+-------------------------------------------------------------------------------------------------------------------------------------------+-------------+----------------+---------------------------------------------------------------+
| Wireless    | 802.11 ac wifi                                                                                                                            | Works       |                | WiFi works w brcmfmac, wpa_supplicant. BT not tested          |
|             |                                                                                                                                           |             |                |                                                               |
|             | BT 5.0 with external antenna                                                                                                              |             |                |                                                               |
+-------------+-------------------------------------------------------------------------------------------------------------------------------------------+-------------+----------------+---------------------------------------------------------------+
| USB         | USB 3.0 OTG X1, upper one, software configurable to be host or OTG,                                                                       | Works       |                |                                                               |
|             |                                                                                                                                           |             |                |                                                               |
|             | USB 3.0 HOST X1, dedicated USB 3.0 channel, lower one USB 2.0 HOST X2                                                                     |             |                |                                                               |
+-------------+-------------------------------------------------------------------------------------------------------------------------------------------+-------------+----------------+---------------------------------------------------------------+
| Ethernet    | GbE LAN with Power over Ethernet (PoE) support                                                                                            | Works       |                |                                                               |
|             |                                                                                                                                           |             |                |                                                               |
|             | additional HAT is required for powering from PoE                                                                                          |             |                |                                                               |
+-------------+-------------------------------------------------------------------------------------------------------------------------------------------+-------------+----------------+---------------------------------------------------------------+
| IO          | 40-pin expansion header                                                                                                                   | Works       |                |                                                               |
|             |                                                                                                                                           |             |                |                                                               |
|             | 2 x UART 2 x SPI bus 3 x I2C bus 1 x PCM/I2S 1 x SPDIF 2 x PWM 1 x ADC 6 x GPIO 2 x 5V DC power in 2 x 3.3V DC power in                   |             |                |                                                               |
+-------------+-------------------------------------------------------------------------------------------------------------------------------------------+-------------+----------------+---------------------------------------------------------------+
| Others      | RTC                                                                                                                                       | Not tested  |                |                                                               |
+-------------+-------------------------------------------------------------------------------------------------------------------------------------------+-------------+----------------+---------------------------------------------------------------+
| Power       | USB C 5V/3A                                                                                                                               | Works       |                |                                                               |
+-------------+-------------------------------------------------------------------------------------------------------------------------------------------+-------------+----------------+---------------------------------------------------------------+

### [Accessories]

-   Standard (shipped in starter kit): case, heat sinks, fan, and power supply.
-   Keyboard, mouse, micro-HDMI cable, and FTDIboard-with-miniUSB cable provided separately by the user

\

-   Rock 4c plus in operation. Shown here with UART connected via FTDI/USB to a PC for u-boot serial port use.

-   ::::::
    ::::
    :::
    [![](/images/thumb/1/10/20230927_212510.jpg/378px-20230927_212510.jpg)](https://wiki.gentoo.org/wiki/File:20230927_212510.jpg)
    :::
    ::::

    ::: gallerytext
    Cover on
    :::
    ::::::

-   ::::::
    ::::
    :::
    [![](/images/thumb/5/5b/20230927_212105.jpg/465px-20230927_212105.jpg)](https://wiki.gentoo.org/wiki/File:20230927_212105.jpg)
    :::
    ::::

    ::: gallerytext
    Cover open
    :::
    ::::::

### [Peripherals]

  -------------- ------------------ -------- -------------------------- ---------------- -------------------------------------------------------------------------------------------------------------
  Component      Make/model         Status   Kernel driver(s)           Kernel version   Notes
  PMIC           Rockchip RK808     Works    rk808                      5.10             Power Management Integrated Circuit (Regulators, RTC, Clocking)^[\[3\]](#cite_note-3)[\[4\]](#cite_note-4)^
  Ethernet PHY   Realtek RTL8211F   Works    realtek_phy                5.10             via RGMII
  Analog Audio                       ?       es8316, audio_graph_card   5.10
  -------------- ------------------ -------- -------------------------- ---------------- -------------------------------------------------------------------------------------------------------------

## [][GCC optimization^[\[5\]](#cite_note-5)^]

** Note**\
ARM errata 835769 and 843419 affect Cortex-A53 up to r0p4 and Linux kernel recommends working around the latter though states nothing about the former.

[FILE] **`/etc/portage/make.conf`RK3399 example**

    COMMON_FLAGS="-march=armv8-a+crc+crypto -mtune=cortex-a72.cortex-a53 -mfix-cortex-a53-835769 -mfix-cortex-a53-843419"
    CFLAGS="$"
    CXXFLAGS="$"

** Note**\
For a hardened system consider appending `-fstack-protector-all`

## [Gentoo Installation Options and Procedures]

### [Getting to Know the Board]

The purpose of this guide is to document \"from scratch\" procedures for installing a pure gentoo system on this SBC. However the quicker way to get gentoo up and running is to install another distribution, and replace the root file system contents. See [User:Brendlefly62/Radxa ROCK Pi 4C Plus/Getting to Know the Board](https://wiki.gentoo.org/wiki/User:Brendlefly62/Radxa_ROCK_Pi_4C_Plus/Getting_to_Know_the_Board "User:Brendlefly62/Radxa ROCK Pi 4C Plus/Getting to Know the Board")

### [Bootloader Build and Installation]

To build a U-Boot bootloader from sources, see [User:Brendlefly62/Radxa ROCK Pi 4C Plus/Build-Install-U-Boot](https://wiki.gentoo.org/wiki/User:Brendlefly62/Radxa_ROCK_Pi_4C_Plus/Build-Install-U-Boot "User:Brendlefly62/Radxa ROCK Pi 4C Plus/Build-Install-U-Boot")

### [Assemble a Working Gentoo System]

To assemble a working Gentoo system with minimal effort, using resources developed above, consult [User:Brendlefly62/Radxa ROCK Pi 4C Plus/Assemble a Gentoo System](https://wiki.gentoo.org/wiki/User:Brendlefly62/Radxa_ROCK_Pi_4C_Plus/Assemble_a_Gentoo_System "User:Brendlefly62/Radxa ROCK Pi 4C Plus/Assemble a Gentoo System")

### [Kernel Build and Installation]

To build a gentoo linux kernel (including modules, device tree blobs, etc) from sources, see [User:Brendlefly62/Radxa ROCK Pi 4C Plus/Build-Install-Kernel](https://wiki.gentoo.org/wiki/User:Brendlefly62/Radxa_ROCK_Pi_4C_Plus/Build-Install-Kernel "User:Brendlefly62/Radxa ROCK Pi 4C Plus/Build-Install-Kernel")

## [][Install a Gentoo System \"From Scratch\"]

To install Gentoo from scratch on this board, consult [User:Brendlefly62/Radxa ROCK Pi 4C Plus/Gentoo From Scratch](https://wiki.gentoo.org/wiki/User:Brendlefly62/Radxa_ROCK_Pi_4C_Plus/Gentoo_From_Scratch "User:Brendlefly62/Radxa ROCK Pi 4C Plus/Gentoo From Scratch")

## [Bootable gentoo system images]

To use pre-built bootable system images files, see [User:Brendlefly62/Radxa ROCK Pi 4C Plus/Bootable-System-Images](https://wiki.gentoo.org/index.php?title=User:Brendlefly62/Radxa_ROCK_Pi_4C_Plus/Bootable-System-Images&action=edit&redlink=1 "User:Brendlefly62/Radxa ROCK Pi 4C Plus/Bootable-System-Images (page does not exist)")

## [See also]

-   [PINE64 ROCKPro64](https://wiki.gentoo.org/wiki/PINE64_ROCKPro64 "PINE64 ROCKPro64") --- the Radxa ROCK 4C+ SBC employs the same SoC as the PINE64 ROKCPro64, so the associated article on that SBC may also be helpful.

## [External resources]

-   [OKdo.com Rock Pi 4c Plus page (\$55)](https://www.okdo.com/us/p/okdo-rock-4-model-c-4gb-single-board-computer-rockchip-rk3399-t-arm-cortex-a72-cortex-a53/), accessed circa 15 September 2023
-   [Radxa Rock 4C Plus Development Guide](https://wiki.radxa.com/Rock4/dev), first visit circa 20 September 2023
-   [Radxa Development Guide to Armbian Build](https://wiki.radxa.com/Rockpi4/dev/build-Armbian), first visit circa 23 September 2023
-   [PINE64 ROCKPro64](https://wiki.gentoo.org/wiki/PINE64_ROCKPro64 "PINE64 ROCKPro64"), retrieved 22 September 2023
-   [RK3399-T Datasheet](https://dl.radxa.com/rockpi4/docs/hw/datasheets/Rockchip%20RK3399-T%20Datasheet%20V1.0-20210818.pdf), retrieved 27 September 2023
-   [How to Compile Armbian: Step-by-Step Tutorial for Beginners](https://www.youtube.com/watch?v=Fg966ivZlrc) , first visit circa 23 September 2023
-   [Debug output in \"somewhat successful build\"](https://www.mail-archive.com/debian-bugs-dist@lists.debian.org/msg1903318.html) First accessed 28 September 2023 (useful lsmod list and dmesg hardware/driver recognition information)

## [References]

1.  [[[↑](#cite_ref-1)] [[PINE64 ROCKPro64](https://wiki.gentoo.org/wiki/PINE64_ROCKPro64#Issues "PINE64 ROCKPro64")]]
2.  [[[↑](#cite_ref-2)] [[https://gitlab.manjaro.org/manjaro-arm/packages/core/uboot-rockpro64/-/issues/4](https://gitlab.manjaro.org/manjaro-arm/packages/core/uboot-rockpro64/-/issues/4)]]
3.  [[[↑](#cite_ref-3)] [[https://www.mail-archive.com/debian-bugs-dist@lists.debian.org/msg1903318.html](https://www.mail-archive.com/debian-bugs-dist@lists.debian.org/msg1903318.html)]]
4.  [[[↑](#cite_ref-4)] [Fuzhou Rockchip Electronics Co., Ltd., [RK808 Datasheet V0.8 (PDF)](https://files.pine64.org/doc/datasheet/rockpro64/RK808%20datasheet%20V0.8.pdf), [PINE64](http://www.pine64.org). Retrieved on January 25th, 2021]]
5.  [[[↑](#cite_ref-5)] [[PINE64 ROCKPro64#GCC optimization](https://wiki.gentoo.org/wiki/PINE64_ROCKPro64#GCC_optimization "PINE64 ROCKPro64")]]