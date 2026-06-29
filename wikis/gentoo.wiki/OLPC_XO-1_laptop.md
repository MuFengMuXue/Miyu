**Resources**

[[]][Home](https://wiki.laptop.org/go/XO-1)

[[]][Wikipedia](https://en.wikipedia.org/wiki/OLPC_XO "wikipedia:OLPC XO")

The **OLPC XO-1 laptop** is a durable low power Linux-based children\'s laptop intended for the developing world. The One Laptop Per Child initiative (optimistically) marketed the XO-1 as a \"\$100 laptop.\" It features a compact clam shell design with a handle that makes it easy for children to carry and a membrane keyboard that is forgiving of spills and rough treatment. The XO-1 has undergone several revisions, from 1.0 to 1.75 incorporating the same basic exterior design.

The laptop design includes a number of innovative features:

-   Extremely low power requirements for an x86 CPU.
-   Automatic 802.11s mesh networking baked into the WiFi firmware, enabling peer-to-peer networking in the absence of infrastructure.
-   An ebook mode allowing the color LCD display to switch to a very low power black-and-white passive mode for text book reading.
-   A highly secure [Open Firmware](https://wiki.gentoo.org/wiki/Open_Firmware "Open Firmware")-based system boot ROM with its own [Forth](https://wiki.gentoo.org/wiki/Forth "Forth") interpreter.

The system spawned a number of accessories, including solar charging panels for use in areas of the world without reliable access to electrical power and a hand-crank intended as a last-ditch charging method. A charging bay for up to 10 laptops was produced. The system\'s battery is external and intended to be user replaceable. Early models provided approximately 3 hours under typical classroom workloads but later models extended this considerably.

In addition to supporting improvised charging methods, the system\'s 802.11s networking is considered especially robust. Any XO laptop can communicate with any other XO laptop within range via peer-to-peer networking. Further, any node may operate as a network gateway for all other nodes in range, albeit slowly.

## Contents

-   [[1] [Hardware]](#Hardware)
    -   [[1.1] [OLPC X0-1 1.0]](#OLPC_X0-1_1.0)
-   [[2] [Installation]](#Installation)
    -   [[2.1] [Firmware]](#Firmware)
    -   [[2.2] [Root and Swap File Systems]](#Root_and_Swap_File_Systems)
-   [[3] [Configuration]](#Configuration)
-   [[4] [See also]](#See_also)
-   [[5] [External resources]](#External_resources)

## [Hardware]

The OLPC was designed from the ground up to run Linux. That said, the OLPC XO-1\'s hardware was considered anemic even for its time. However, this is the result of design trade-offs intended to minimize power consumption and improve durability in locales with minimal infrastructure. The underlying hardware and firmware are very hackable.

### [OLPC X0-1 1.0]

  ---------------- ------------------------------------------------------------------------------------------- -------- ------------------------ ------------------ ---------------- -------------------------------------------
  Device           Make/model                                                                                  Status   Vendor ID / Product ID   Kernel driver(s)   Kernel version   Notes
  CPU              AMD Geode LX 700 \@433 MHz                                                                  Works                                                                 Non-upgradable
  RAM              256MB DDR333 DRAM                                                                           Works                                                                 Non-upgradable
  Firmware         1MB [Open Firmware](https://wiki.gentoo.org/wiki/Open_Firmware "Open Firmware") Flash ROM   Works
  eMMC Storage     1GB SLC NAND                                                                                Works                                                                 System boot device
  Display          7.5\" dual-mode TFT display                                                                 Works
  Touch Pad        ALPS Electric                                                                               Works
  Audio            AC 97                                                                                       Works
  Camera           640×480 \@30 FPS                                                                            Works
  WiFi             2.4GHz Marvell Libertas 88W8388 802.11s (Mesh)                                              Works                                                                 2 Mbit/s max throughput
  USB              3× USB 2.0 type-A connectors                                                                Works                                                                 Max 1W combined output
  SD Card Reader                                                                                               Works                                                                 256 GB manufacturer reported max capacity
  ---------------- ------------------------------------------------------------------------------------------- -------- ------------------------ ------------------ ---------------- -------------------------------------------

## [Installation]

Although XO-1 was designed to run Linux, it makes a poor Gentoo installation target without careful consideration of the platform\'s limitations. The system\'s default boot device is non-upgradable eMMC storage. Also the system\'s keyboard is designed for children, as such the keys are quite small. A \"fat-fingered\" adult will most likely find using the system\'s small membrane keyboard extremely awkward. Consequently, an external USB keyboard is a must for an adult installing Gentoo on to the system. With those caveats out of the way, it is possible to install Gentoo if care is used.

The system uses an 32-bit x86 processor. So, the x86 installation media and handbook are indispensable. The system\'s eMMC storage is ill equipped to handle a full Gentoo system due to the size of the Portage tree and the fact that the act of compiling from that device will likely reduce the life expectancy of the eMMC storage. Thus, most Gentoo users typically do the following to ensure the system has a long life:

-   Place the boot partition in the eMMC storage, as Linux kernel upgrades are relatively infrequent.
-   Place the root and swap partition onto removable media, either a USB flash drive or an SD Card.
-   Enable memory compression to help reduce swapping.
-   Use a [binhost](https://wiki.gentoo.org/wiki/Binary_package_guide "Binary package guide") to provide pre-build binaries to the system.
-   The Open Firmware must be in developer mode, a cryptographic key from [laptop.org](https://laptop.org) is required.

### [Firmware]

Having developer mode access into the Open Firmware ROM is a requirement to replace the existing Linux system image with Gentoo. It is not possible to get to an Open Firmware Forth interpreter prompt from the system itself without requesting a [developer key](https://wiki.laptop.org/go/Activation_and_developer_keys). It *may* be possible to bypass the key requirement with an SPI flash programmer if one has the required skills.

Once developer mode is obtained it is now possible to boot from a device other than the eMMC storage. An XO laptop in developer mode searches the devices in the following order for [/boot/olpc.fth], a Forth script which functions as a bootloader:

1\. USB devices. 2. SD Card. 3. Internal eMMC NAND storage.

While the root file system can be anything Gentoo Linux\'s kernel supports, the boot partition must be one of the following file systems:

-   FAT (8.3 file names only, long file names NOT supported)
-   ext2/ext3
-   JFFS2 (officially for eMMC storage only)
-   UBIFS (officially for eMMC storage only)

It\'s important to understand that the [olpc.fth] file is an arbitrary Forth script, its contents can be anything the system administrator wants. The following is a resonable boot script which boots the Gentoo kernel from eMMC storage and mounts the SD card containing the system\'s root file system. Other configurations are possible, this is just an example:

[FILE] **`/boot/olpc.fth`Example OLPC XO-1 boot script in Forth**

    \ olpc.fth must be present for the boot device for the system to start.
    \ The following boots the OS kernel from NAND storage, the root file system is on an SD Card in this example.
    \ Customize as desired.
    unfreeze
    boot nand:\boot\vmlinuz ro root=mmcblk0p1 rootfstype=btrfs

With the firmware and NAND storage taken care of, it\'s now possible to turn to installation of the OS itself.

### [Root and Swap File Systems]

** Note**\
Do not create a swap partition \>4GB. The XO-1 has a 32-bit CPU and 4GB is the maximum amount of memory (RAM + swap) it can address.

The root device can be any external storage device, be it a USB flash drive or a SD Card. A swap partition is also a functional requirement due to the XO laptop\'s minimal RAM. The Stage 3 tarball can be extracted directly onto the USB flash drive or SD Card partition intended to be used as the new system root. Once present, set up the swap partition and continue with the Gentoo Handbook as normal.

## [Configuration]

The following [make.conf] settings are considered safe for the XO-1\'s AMD Geode processor:

[FILE] **`/etc/portage/make.conf`**

    CHOST="i486-pc-linux-gnu"
    COMMON_FLAGS="-Os -pipe -march=geode -mmmx -m3dnow -fomit-frame-pointer"
    CFLAGS="$"
    CXXFLAGS="$"

## [See also]

-   [Binary package guide](https://wiki.gentoo.org/wiki/Binary_package_guide "Binary package guide") --- in-depth **binary package** creation, distribution, use, and maintenance
-   [Open Firmware](https://wiki.gentoo.org/wiki/Open_Firmware "Open Firmware") --- an [IEEE 1275-1994](https://ieeexplore.ieee.org/document/763383) standard for hardware independent firmware built on top of a [Forth](https://wiki.gentoo.org/wiki/Forth "Forth") machine.
-   [Forth](https://wiki.gentoo.org/wiki/Forth "Forth") --- a heavily stack-oriented self-compiling procedural programming language that is only slightly more abstract than [assembly](https://wiki.gentoo.org/wiki/Assembly_language "Assembly language").

## [External resources]

-   [laptop.org](https://laptop.org) --- the official website for the One Laptop Per Child charity.
-   [The One Laptop Per Child Wiki](https://wiki.laptop.org/go/The_OLPC_Wiki) --- the official OLPC wiki.