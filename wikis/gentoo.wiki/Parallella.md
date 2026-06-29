**Resources**

[[]][Home](https://www.parallella.org/)

[[]][Wikipedia](https://en.wikipedia.org/wiki/Adapteva#Parallella_project "wikipedia:Adapteva")

The Adapteva Parallella is a family of credit card sized single board computers. Based on the dual-core Zynq-7000 series of ARMv7-A processors, they also contain a built-in FPGA and Epiphany-III 16-core co-processor. The board is intended to democratise access to parallel programming^[\[1\]](#cite_note-1)^, due to the price, number of cores and low power draw (5W).

The Parallella was crowdfunded via Kickstarter^[\[2\]](#cite_note-2)^, and the schematics and design files were released as open source.

## Contents

-   [[1] [Hardware]](#Hardware)
    -   [[1.1] [Parallella-16 Micro Server]](#Parallella-16_Micro_Server)
    -   [[1.2] [Parallella-16 Desktop Computer]](#Parallella-16_Desktop_Computer)
    -   [[1.3] [Parallella-16 Embedded Platform]](#Parallella-16_Embedded_Platform)
-   [[2] [Installation]](#Installation)
    -   [[2.1] [SD Card]](#SD_Card)
    -   [[2.2] [Firmware]](#Firmware)
        -   [[2.2.1] [Versions]](#Versions)
        -   [[2.2.2] [Post-boot customisation]](#Post-boot_customisation)
    -   [[2.3] [Kernel]](#Kernel)
        -   [[2.3.1] [Device Tree]](#Device_Tree)
    -   [[2.4] [Root Filesystem]](#Root_Filesystem)
-   [[3] [Epiphany SDK (esdk)]](#Epiphany_SDK_.28esdk.29)
-   [[4] [Cross-compiling]](#Cross-compiling)
-   [[5] [External Resources]](#External_Resources)
-   [[6] [References]](#References)

## [Hardware]

Generally available Parallella hardware comes in three forms:

-   Parallella-16 Micro Server
-   Parallella-16 Desktop Computer
-   Parallella-16 Embedded Platform

Kickstarter backers would have been able to receive a limited number of Parallella-64s with a 64-core co-processor, but these were not mass-produced and are not covered here.

Parallella-16s can be powered by 2A 5V DC barrel jack (5.5mm OD/2.1mm ID centre-positive^[\[3\]](#cite_note-3)^), microUSB (with jumper) or by the metal pads in the corners via the J15 header^[\[4\]](#cite_note-4)^.

### [Parallella-16 Micro Server]

  -------------- ----------------------------- -------- ------------------ ------------------ ---------------
  Device         Make/model                    Status   Kernel driver(s)   Kernel version     Notes
  CPU            Dual-core Zynq-7010           Works    ARCH_ZYNQ
  Memory         1GB DDR3L                     Works
  Co-processor   16-core Epiphany-III          Works    EPIPHANY           parallella-linux
  Ethernet       10/100/1000                   Works    ARM_AMBA                              Max. 1500 MTU
  Storage        microSDXC                     Works    ARM_AMBA
  Serial         UART^[\[5\]](#cite_note-5)^   Works
  -------------- ----------------------------- -------- ------------------ ------------------ ---------------

### [Parallella-16 Desktop Computer]

Includes all hardware of the Parallella-16 Micro Server, additionally with:

  -------- -------------- -------- ------------------ ---------------- ---------------------
  Device   Make/model     Status   Kernel driver(s)   Kernel version   Notes
  USB      microUSB OTG   Works
  Video    microHDMI      Works
  GPIO                    24                                           via Porcupine board
  -------- -------------- -------- ------------------ ---------------- ---------------------

### [Parallella-16 Embedded Platform]

Includes the hardware of the Parallella-16 Desktop Computers, except the CPU is upgraded to the Zynq-7020. EP devices must use FPGA firmware built for Zynq-7020 devices.

  -------- --------------------- ---------------- ------------------ ---------------- ---------------------------
  Device   Make/model            Status           Kernel driver(s)   Kernel version   Notes
  CPU      Dual-core Zynq-7020   48 (Untested)    ARCH_ZYNQ                           includes Bank 13 I/O pins
  -------- --------------------- ---------------- ------------------ ---------------- ---------------------------

## [Installation]

### [SD Card]

The Parallella finds its firmware, bootloader, kernel and device tree necessary to boot on the SD card. In order for the board to find these files, the SD Card must be MBR/DOS partitioned, with the first partition FAT32 formatted.

`root `[`#`]`lsblk`

    NAME             FSTYPE   LABEL MOUNTPOINT
    /dev/mmcblk0
    ├─/dev/mmcblk0p1 vfat     BOOT  /boot
    └─/dev/mmcblk0p2 ext4     ROOT  /

`root `[`#`]`tree /boot`

    /boot
    ├── devicetree.dtb
    ├── parallella.bit.bin
    └── uImage

### [Firmware]

Parallella boards load the FPGA firmware (including u-boot bootloader), kernel (uImage) and device tree (dtb) from the microSD card slot whenever power is applied to the board.

The firmware file must be named [parallella.bit.bin] on the FAT32 filesystem on the SD card.

This firmware is open sourced on [Github parallella/oh](https://github.com/parallella/oh) but requires the free (as in beer) Xilinx Vivado tools to produce.

#### [Versions]

Parallella has provided 4 versions of the firmware ([parallella.bit.bin]) that boots Linux:

  --------- --------- -------- ------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Date      Elink     Status   Notes               Source
  2019.1    elink2    latest   HDMI and headless   [Github parallella/parabuntu fpga_bitfiles](https://github.com/parallella/parabuntu/tree/master/fpga_bitfiles)
  2016.11   elink2             HDMI and headless   [Github parallella/parabuntu commit 0cb190a](https://github.com/parallella/parabuntu/commit/0cb190af63a3f5f0006bcbd5d33205791f27e197)
  2016.3    elink2             Headless only       [Github parallella/parabuntu commit d36f6be](https://github.com/parallella/parabuntu/commit/d36f6be62e9c9c0f5a45a1e73abaaf1f95b8d71c)
  2014.11   elink1             HDMI and headless   [Github parallella/parallella-hw old bitstreams](https://github.com/parallella/parallella-hw/tree/master/archive/fpga/old/bitstreams)
  --------- --------- -------- ------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------

#### [Post-boot customisation]

Once the operating system is running, the FPGA can be reconfigured with a compatible bitstream by use of the [/dev/xdevcfg] driver^[\[6\]](#cite_note-6)^, or, in more recent kernels, the FPGA Manager^[\[7\]](#cite_note-7)^.

### [Kernel]

The firmware [parallella.bit.bin], in addition to the FPGA routines that concern board bring-in, contains u-boot to boot the system into Linux. The load address for a kernel uImage is **0x8000**.

Parallella provide kernel sources with working Epiphany drivers in the [parallella-linux](https://github.com/parallella/parallella-linux) repository. [parallella-linux] provides the [parallella_defconfig] target to generate a kernel config suitable for all Parallella boards.

`user `[`$`]`make parallella_defconfig `

`user `[`$`]`make uImage LOADADDR=0x8000 `

  ------------------------------------------------------------------------------------------------------------------------------------------ -------- ------------------
  Branch                                                                                                                                     Status   Based on
  [parallella-linux-2019.1](https://github.com/parallella/parallella-linux/tree/parallella-linux-2019.1)     Works    adi-linux-4.14.0
  [parallella-linux-2016.11](https://github.com/parallella/parallella-linux/tree/parallella-linux-2016.11)   Works    adi-linux-4.6.0
  [parallella-linux-2016.3](https://github.com/parallella/parallella-linux/tree/parallella-linux-2016.3)     Works    adi-linux-4.4.0
  ------------------------------------------------------------------------------------------------------------------------------------------ -------- ------------------

Upstream kernels can also work, however the Epiphany driver has not been upstreamed. Upstream kernels have the [multi_v7_defconfig] which is suitable for the Parallella.

`user `[`$`]`make multi_v7_defconfig`

Building a kernel requires the [sys-devel/bc] package, and building a uImage requires the [dev-embedded/u-boot-tools] package:

`root `[`#`]`emerge --ask sys-devel/bc`

`root `[`#`]`emerge --ask dev-embedded/u-boot-tools`

The resulting uImage can be found at [arch/arm/boot/uImage]. The kernel [uImage] must be named [uImage] on the FAT32 filesystem on the SD card.

#### [Device Tree]

The device tree is available in the [parallella-linux] sources at [arch/arm/boot/dts/zynq-parallella\*.dts]. It can be compiled into a dtb file with [make dtbs]:

`root `[`#`]`emerge --ask sys-apps/dtc`

`user `[`$`]`make dtbs`

The device tree must be named [devicetree.dtb] on the FAT32 filesystem on the SD card.

  ---------------------------------------------------------------------------------------------------------------------- ---------------------------------------------------------
  Name                                                                                                                   Board
  [zynq-parallella-microserver.dtb]   Parallella MicroServer
  [zynq-parallella-headless.dtb]      Parallella (Desktop or Embedded) without HDMI bitstream
  [zynq-parallella.dtb]               Parallella with HDMI bitstream
  ---------------------------------------------------------------------------------------------------------------------- ---------------------------------------------------------

### [Root Filesystem]

The upstream device tree ([[zynq-parallella1.dtsi]](https://github.com/parallella/parallella-linux/blob/parallella-linux-2016.3/arch/arm/boot/dts/zynq-parallella1.dtsi#L48)) configures the root partition as the second partition with an ext4 filesystem.

An armv7a stage3 can be unpacked and customised. Gentoo autobuilds can be found on [distfiles.gentoo.org](http://distfiles.gentoo.org/releases/arm/autobuilds/current-stage3-armv7a_hardfp/).

## [][Epiphany SDK (esdk)]

Adapteva provides the SDK to interact with the Epiphany device on [Github adapteva/epiphany-sdk](https://github.com/adapteva/epiphany-sdk).

Version 2016.3 of the esdk utilises the elink2 interface with the Epiphany chip and requires an elink2 firmware.

The esdk sources build for the armv7l architecture which is not the same as the Gentoo architecture (armv7a).

## [Cross-compiling]

A compatible cross-compiler can be generated with [crossdev](https://wiki.gentoo.org/wiki/Embedded_Handbook/General/Creating_a_cross-compiler "Embedded Handbook/General/Creating a cross-compiler"):

`root `[`#`]`crossdev -S -t armv7a-unknown-linux-gnueabihf`

When cross-compiling the kernel, call [make] with the `ARCH` and `CROSS_COMPILE` environment variables:

`user `[`$`]`make ARCH=arm CROSS_COMPILE=armv7a-unknown-linux-gnueabihf-`

When cross-compiling the Epiphany SDK, use the [-c armv7a-unknown-linux-gnueabihf] flag:

`user `[`$`]`git clone `[`https://github.com/adapteva/epiphany-sdk`](https://github.com/adapteva/epiphany-sdk)` sdk `

`user `[`$`]`./sdk/build-epiphany-sdk.sh -d -R -c armv7a-unknown-linux-gnueabihf `

## [External Resources]

-   Parallella hardware design files are available on [Github parallella/parallella-hw](https://github.com/parallella/parallella-hw).
-   [Xilinx Vivado Design Suite](https://www.xilinx.com/products/design-tools/vivado.html) to create the FPGA firmware files

## [References]

1.  [[[↑](#cite_ref-1)] [[Parallella Project History](https://www.parallella.org/about/)]]
2.  [[[↑](#cite_ref-2)] [[Parallella: A Supercomputer For Everyone by Adapteva](https://www.kickstarter.com/projects/adapteva/parallella-a-supercomputer-for-everyone) on Kickstarter]]
3.  [[[↑](#cite_ref-3)] [[Parallella Quick Start](https://www.parallella.org/quick-start/)]]
4.  [[[↑](#cite_ref-4)] [[Parallella Cluster Case](https://github.com/abopen/parallella-cluster-case/blob/master/README.md#powering-boards)]]
5.  [[[↑](#cite_ref-5)] [[elinux Parallella UART Connection](http://elinux.org/Parallella_UART_Connection)]]
6.  [[[↑](#cite_ref-6)] [[Xilinx AR#46913 \"Zynq-7000 Example Design - Program the PL using the Linux driver for DEVCFG\"](https://www.xilinx.com/support/answers/46913.html)]]
7.  [[[↑](#cite_ref-7)] [[Zynq PL Programming With FPGA Manager](https://xilinx-wiki.atlassian.net/wiki/spaces/A/pages/18841645/Solution+Zynq+PL+Programming+With+FPGA+Manager#SolutionZynqPLProgrammingWithFPGAManager-Usingsysfsinterface)]]