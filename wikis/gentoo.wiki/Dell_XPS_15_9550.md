[] This article has been flagged for not conforming to the [wiki guidelines](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Guidelines "Gentoo Wiki:Guidelines"). Please [help Gentoo out](https://wiki.gentoo.org/wiki/Help_improve_Gentoo_by_getting_involved_with_documentation!#Make_articles_conform_to_the_guidelines "Help improve Gentoo by getting involved with documentation!") by starting fixing things.

[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=Dell_XPS_15_9550&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

## Contents

-   [[1] [General]](#General)
-   [[2] [Laptop Specification]](#Laptop_Specification)
-   [[3] [Hardware List]](#Hardware_List)
-   [[4] [Hardware List with Details]](#Hardware_List_with_Details)
-   [[5] [USB Hardware List with Details]](#USB_Hardware_List_with_Details)
-   [[6] [System Configuration]](#System_Configuration)
    -   [[6.1] [Kernel]](#Kernel)
    -   [[6.2] [Portage and GCC]](#Portage_and_GCC)
-   [[7] [Issues]](#Issues)
    -   [[7.1] [Audio]](#Audio)
    -   [[7.2] [Wireless]](#Wireless)
-   [[8] [Notes]](#Notes)

## [General]

This laptop is Dell\'s flagship on the market with 32GB RAM is really beast and ready for any type of development where one requires to run multiple virtual machines at once. I got working all the non-standard hardware including keyboard special Dell keys, 4k touchscreen. But there remain still few minor issues described in specific chapter.

## [Laptop Specification]

-   Intel® Core™ i7-6700HQ Processor (6M Cache, up to 3.50 GHz) (One of many CPU models offered)
-   Up to 1TB Solid State hard drive (NVMe)
-   Up to 32GB (2x16GB) 2133MHz DDR4
-   15.6\" 4K Ultra HD (3840 x 2160) InfinityEdge touch Corning® Gorilla® Glass or 15.6\" HD (1920 x 1080) without touch
-   Dedicated NVIDIA GTX960M 2GB DDR5
-   Dell 56 WHr 3-Cell Lithium-Ion Battery
-   Integrated WiFi DW1830 3x3 802.11ac 2.4/5GHz
-   Precision touchpad, seamless glass integrated button
-   Integrated Widescreen HD (720p) webcam with dual array digital microphones
-   Dell™ TrueMobile internal 4.1 Bluetooth Module - European
-   Ports: HDMI, USB 3.0 (x2) with PowerShare; Headset Jack (1); SD card reader (SD, SDHC, SDXC); Kensington Lock slot; Thunderbolt™ 3 (1)
-   Thunderbolt™ 3 supports: Power in / charging, PowerShare, Thunderbolt 3 (40Gbps bi-directional), USB 3.1 Gen 2 (10Gbps), VGA, HDMI

## [Hardware List]

`root `[`#`]`lspci`

    00:00.0 Host bridge: Intel Corporation Sky Lake Host Bridge/DRAM Registers (rev 07)
    00:01.0 PCI bridge: Intel Corporation Sky Lake PCIe Controller (x16) (rev 07)
    00:02.0 VGA compatible controller: Intel Corporation Device 191b (rev 06)
    00:04.0 Signal processing controller: Intel Corporation Device 1903 (rev 07)
    00:14.0 USB controller: Intel Corporation Sunrise Point-H USB 3.0 xHCI Controller (rev 31)
    00:14.2 Signal processing controller: Intel Corporation Sunrise Point-H Thermal subsystem (rev 31)
    00:15.0 Signal processing controller: Intel Corporation Sunrise Point-H LPSS I2C Controller #0 (rev 31)
    00:15.1 Signal processing controller: Intel Corporation Sunrise Point-H LPSS I2C Controller #1 (rev 31)
    00:16.0 Communication controller: Intel Corporation Sunrise Point-H CSME HECI #1 (rev 31)
    00:17.0 RAID bus controller: Intel Corporation 82801 Mobile SATA Controller [RAID mode] (rev 31)
    00:1c.0 PCI bridge: Intel Corporation Sunrise Point-H PCI Express Root Port #1 (rev f1)
    00:1c.1 PCI bridge: Intel Corporation Sunrise Point-H PCI Express Root Port #2 (rev f1)
    00:1d.0 PCI bridge: Intel Corporation Sunrise Point-H PCI Express Root Port #9 (rev f1)
    00:1d.4 PCI bridge: Intel Corporation Sunrise Point-H PCI Express Root Port #13 (rev f1)
    00:1d.6 PCI bridge: Intel Corporation Sunrise Point-H PCI Express Root Port #15 (rev f1)
    00:1f.0 ISA bridge: Intel Corporation Sunrise Point-H LPC Controller (rev 31)
    00:1f.2 Memory controller: Intel Corporation Sunrise Point-H PMC (rev 31)
    00:1f.3 Audio device: Intel Corporation Sunrise Point-H HD Audio (rev 31)
    00:1f.4 SMBus: Intel Corporation Sunrise Point-H SMBus (rev 31)
    01:00.0 3D controller: NVIDIA Corporation GM107M [GeForce GTX 960M] (rev a2)
    02:00.0 Network controller: Broadcom Corporation BCM43602 802.11ac Wireless LAN SoC (rev 01)
    03:00.0 Unassigned class [ff00]: Realtek Semiconductor Co., Ltd. Device 525a (rev 01)

NOTE: I am in RAID mode instead of AHCI on SATA controller, but that shouldn\'t make big difference.

## [Hardware List with Details]

`root `[`#`]`lspci -kk`

    00:00.0 Host bridge: Intel Corporation Sky Lake Host Bridge/DRAM Registers (rev 07)
        Subsystem: Dell Sky Lake Host Bridge/DRAM Registers
    00:01.0 PCI bridge: Intel Corporation Sky Lake PCIe Controller (x16) (rev 07)
        Kernel driver in use: pcieport
    00:02.0 VGA compatible controller: Intel Corporation Device 191b (rev 06)
        Subsystem: Dell Device 06e4
        Kernel driver in use: i915
    00:04.0 Signal processing controller: Intel Corporation Device 1903 (rev 07)
        Subsystem: Dell Device 06e4
        Kernel driver in use: proc_thermal
    00:14.0 USB controller: Intel Corporation Sunrise Point-H USB 3.0 xHCI Controller (rev 31)
        Subsystem: Dell Sunrise Point-H USB 3.0 xHCI Controller
        Kernel driver in use: xhci_hcd
    00:14.2 Signal processing controller: Intel Corporation Sunrise Point-H Thermal subsystem (rev 31)
        Subsystem: Dell Sunrise Point-H Thermal subsystem
    00:15.0 Signal processing controller: Intel Corporation Sunrise Point-H LPSS I2C Controller #0 (rev 31)
        Subsystem: Dell Sunrise Point-H LPSS I2C Controller
        Kernel driver in use: intel-lpss
    00:15.1 Signal processing controller: Intel Corporation Sunrise Point-H LPSS I2C Controller #1 (rev 31)
        Subsystem: Dell Sunrise Point-H LPSS I2C Controller
        Kernel driver in use: intel-lpss
    00:16.0 Communication controller: Intel Corporation Sunrise Point-H CSME HECI #1 (rev 31)
        Subsystem: Dell Sunrise Point-H CSME HECI
        Kernel driver in use: mei_me
    00:17.0 RAID bus controller: Intel Corporation 82801 Mobile SATA Controller [RAID mode] (rev 31)
        Subsystem: Dell 82801 Mobile SATA Controller [RAID mode]
        Kernel driver in use: ahci
    00:1c.0 PCI bridge: Intel Corporation Sunrise Point-H PCI Express Root Port #1 (rev f1)
        Kernel driver in use: pcieport
    00:1c.1 PCI bridge: Intel Corporation Sunrise Point-H PCI Express Root Port #2 (rev f1)
        Kernel driver in use: pcieport
    00:1d.0 PCI bridge: Intel Corporation Sunrise Point-H PCI Express Root Port #9 (rev f1)
        Kernel driver in use: pcieport
    00:1d.4 PCI bridge: Intel Corporation Sunrise Point-H PCI Express Root Port #13 (rev f1)
        Kernel driver in use: pcieport
    00:1d.6 PCI bridge: Intel Corporation Sunrise Point-H PCI Express Root Port #15 (rev f1)
        Kernel driver in use: pcieport
    00:1f.0 ISA bridge: Intel Corporation Sunrise Point-H LPC Controller (rev 31)
        Subsystem: Dell Sunrise Point-H LPC Controller
    00:1f.2 Memory controller: Intel Corporation Sunrise Point-H PMC (rev 31)
        Subsystem: Dell Sunrise Point-H PMC
    00:1f.3 Audio device: Intel Corporation Sunrise Point-H HD Audio (rev 31)
        Subsystem: Dell Sunrise Point-H HD Audio
        Kernel driver in use: snd_hda_intel
    00:1f.4 SMBus: Intel Corporation Sunrise Point-H SMBus (rev 31)
        Subsystem: Dell Sunrise Point-H SMBus
        Kernel driver in use: i801_smbus
    01:00.0 3D controller: NVIDIA Corporation GM107M [GeForce GTX 960M] (rev a2)
        Subsystem: Dell GM107M [GeForce GTX 960M]
        Kernel driver in use: nvidia
        Kernel modules: nvidia_drm, nvidia
    02:00.0 Network controller: Broadcom Corporation BCM43602 802.11ac Wireless LAN SoC (rev 01)
        Subsystem: Dell BCM43602 802.11ac Wireless LAN SoC
        Kernel driver in use: brcmfmac
        Kernel modules: brcmfmac
    03:00.0 Unassigned class [ff00]: Realtek Semiconductor Co., Ltd. Device 525a (rev 01)
        Subsystem: Dell Device 06e4
        Kernel driver in use: rtsx_pci

## [USB Hardware List with Details]

`root `[`#`]`lsusb`

    Bus 002 Device 001: ID 1d6b:0003 Linux Foundation 3.0 root hub
    Bus 001 Device 004: ID 04f3:21d5 Elan Microelectronics Corp.
    Bus 001 Device 003: ID 0a5c:6410 Broadcom Corp.
    Bus 001 Device 008: ID 17ef:7205 Lenovo
    Bus 001 Device 007: ID 1532:0032 Razer USA, Ltd
    Bus 001 Device 006: ID 1a40:0101 Terminus Technology Inc. Hub
    Bus 001 Device 005: ID 0c45:6713 Microdia
    Bus 001 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub

## [System Configuration]

`root `[`#`]`uname -a`

    Linux ares 4.8.6-gentoo #3 SMP Fri Nov 11 21:25:38 CET 2016 x86_64 Intel(R) Core(TM) i7-6700HQ CPU @ 2.60GHz GenuineIntel GNU/Linux

### [Kernel]

List of Kernel Configs

1.  [linux-4.10.3-gentoo.config](https://github.com/archenroot/gentoo-overlay/blob/master/dell-xps-15-linux-4.10.3-gentoo-config)
2.  [linux-4.8.6-gentoo.config](https://github.com/archenroot/gentoo-overlay/blob/master/dell-xps-15-linux-4.8.6-gentoo-config)

-   This kernel works is configured with packed firmware and initramfs inside, so able to boot on its own within UEFI. I use [rEFInd](https://sourceforge.net/projects/refind/) as it detects and shows on boot all available operating systems/kernel versions. I don\'t use standard kind of loader like Grub or LiLo. I think that this kernel image is bootable directly from EFI bios itself without anything else needed.
-   I am still working on proper KVM configuration for PCI Passtrough on QEMU.

### [Portage and GCC]

[CODE] **make.conf**

    CFLAGS="-march=skylake -O2 -pipe"
    CPU_FLAGS_X86="aes avx avx2 fma3 mmx mmxext popcnt sse sse2 sse3 sse4_1 sse4_2 ssse3"
    CXXFLAGS="$"

[FILE] **`/etc/portage/package.use/00input`**

    */* INPUT_DEVICES: evdev synaptics

[FILE] **`/etc/portage/package.use/00video`**

    */* VIDEO_CARDS: -* intel nvidia

[FILE] **`/etc/portage/package.use/00cpu-flags`**

    */* CPU_FLAGS_X86: aes avx avx2 fma3 mmx mmxext popcnt sse sse2 sse3 sse4_1 sse4_2 ssse3

## [Issues]

### [Audio]

Audio basically works, but when the headphones are plugged in, it suddenly stops working. Neither reboot or disable-\>re-enable of audio in BIOS helped. I resolved by flashing the BIOS again :-) and the sound is back:

[ALSA Detail Report](https://www.alsa-project.org/db/?f=e17ca2cf79482607eb88d2e546dbdd054d537e08)

Update: It\'s also reported working if you make i915 a built-in kernel driver and not a module, but keep the sound driver as a module. It seems that some power setup that i915 does has to run before the sound stuff gets set up. When you do this, it seems to work. Remember to build-in all the required firmware for i915 (dmesg will tell you what you need).

There are multiple bugs reported in Arch and Ubuntu with this ALC3266 sound chip: [Ubuntu bug](https://bugs.launchpad.net/ubuntu/+source/alsa-driver/+bug/1575078)

Arch wiki refer to some workarounds: [Arch Wiki related resource](https://wiki.archlinux.org/index.php/Dell_XPS_15#Sound)

\

Hardware workaround: I have USB wireless headset and switching between internal and USB based headphones works like charm.

### [Wireless]

There is some serious issue with the driver which works with some networks, but when connecting to others it causes kernel panic even on latest kernel (only seen on certain WPA2 network, maybe you are lucky with your wifi router):

[brcmfmac issue report](https://patchwork.kernel.org/patch/6481071/) [bug report at kernel.org](https://bugzilla.kernel.org/show_bug.cgi?id=195427)

## [Notes]

-   This device is supported by [fwupd](https://fwupd.org/), so you can easily queue a BIOS update from within Linux.
-   You should use a new as possible kernel to get good USB-C support, e.g. HDMI out via USB-C did not start working on resolutions over 720p before around kernel version 4.12
-   The best acpi_osi option seems to be \'acpi_osi=\"!Windows 2012\"\'. This works with Optimus, and makes you able to turn of the discrete nVIDIA card off or on with e.g. bbswitch. \"!Windows 2015\" is supported by the ACPI DSDT, but it makes the touchpad report itself as a device with a bus id \"DLL06e4 PNP0f13\" according to the PS/2 synaptics driver, and no driver (except the aforementioned old Synaptics PS/2 driver) seems to support this. The old PS/2 driver uses more power, and does not support all multitouch features, so it shouldn\'t be used.