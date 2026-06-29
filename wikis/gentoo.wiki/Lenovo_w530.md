**Resources**

[[]][Official Support Page](https://pcsupport.lenovo.com/us/en/products/laptops-and-netbooks/thinkpad-w-series-laptops/thinkpad-w530)

[[]][Specifications](https://psref.lenovo.com/syspool/Sys/PDF/withdrawnbook/ltwbook_WE.pdf#p80)

[[]][Hardware Maintenance Manual](https://download.lenovo.com/ibmdl/pub/pc/pccbbs/mobiles_pdf/t530_t530i_w530_hmm_en_0b48474_03.pdf)

[[]][User Guide](https://download.lenovo.com/ibmdl/pub/pc/pccbbs/mobiles_pdf/t530_t530i_w530_ug_en.pdf)

[[]][BIOS Setup](https://download.lenovo.com/pccbbs/mobiles_pdf/lenovo_bios_setup_linux_wmi_sysfs_1.2.pdf)

[[]][ThinkPad W series](https://en.wikipedia.org/wiki/ThinkPad_W_series "wikipedia:ThinkPad W series")

The Lenovo Thinkpad W530 and its associated hardware components can (potentially) be difficult to configure properly in Gentoo. This article has been written as a configuration guide to help users work out some of the gritty details needed to get this notebook working as it should on Gentoo Linux.

** Note**\
Do not expect to have exactly the same hardware listed in this guide in *your* W530. The hardware listed here is to be used as an example. Some of the components may be similar, but there are always variants in computers depending on what hardware was purchased. See the ThinkWiki.org link in the [External resources](https://wiki.gentoo.org/wiki/Lenovo_Thinkpad_W530#External_resources "Lenovo Thinkpad W530") section for a review of possible factory hardware setups.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [Preparation]](#Preparation)
    -   [[1.2] [Hardware]](#Hardware)
        -   [[1.2.1] [lspci]](#lspci)
        -   [[1.2.2] [lsusb]](#lsusb)
-   [[2] [Configuration]](#Configuration)
    -   [[2.1] [Intel graphics]](#Intel_graphics)
    -   [[2.2] [Nouveau and Intel graphics]](#Nouveau_and_Intel_graphics)
    -   [[2.3] [NVidia Optimus graphics]](#NVidia_Optimus_graphics)
    -   [[2.4] [USB]](#USB)
        -   [[2.4.1] [Microphone]](#Microphone)
        -   [[2.4.2] [Power management]](#Power_management)
-   [[3] [Tips]](#Tips)
    -   [[3.1] [Become familiar with helpful tools]](#Become_familiar_with_helpful_tools)
-   [[4] [See also]](#See_also)
-   [[5] [External resources]](#External_resources)

## [Installation]

### [Preparation]

Adequate preparation should be established for the case something should go wrong in the middle of installing Gentoo. The following list does not only apply to the current hardware list in this article; it generally applies to whenever attempting to install Linux on any machine:

Backups

Time

Diligence

### [Hardware]

** Important**\
As stated above, the hardware listed in the following commands might not match the hardware in *your* laptop verbatim. Use the following hardware information as reference guide.

#### [lspci]

`root `[`#`]`lspci -nnk`

    00:00.0 Host bridge [0600]: Intel Corporation 3rd Gen Core processor DRAM Controller [8086:0154] (rev 09)
            Subsystem: Lenovo Device [17aa:21f6]
            Kernel driver in use: ivb_uncore
    00:01.0 PCI bridge [0604]: Intel Corporation Xeon E3-1200 v2/3rd Gen Core processor PCI Express Root Port [8086:0151] (rev 09)
            Kernel driver in use: pcieport
    00:02.0 VGA compatible controller [0300]: Intel Corporation 3rd Gen Core processor Graphics Controller [8086:0166] (rev 09)
            Subsystem: Lenovo Device [17aa:21f5]
            Kernel driver in use: i915
    00:14.0 USB controller [0c03]: Intel Corporation 7 Series/C210 Series Chipset Family USB xHCI Host Controller [8086:1e31] (rev 04)
            Subsystem: Lenovo Device [17aa:21f6]
            Kernel driver in use: xhci_hcd
    00:16.0 Communication controller [0780]: Intel Corporation 7 Series/C210 Series Chipset Family MEI Controller #1 [8086:1e3a] (rev 04)
            Subsystem: Lenovo Device [17aa:21f6]
    00:16.3 Serial controller [0700]: Intel Corporation 7 Series/C210 Series Chipset Family KT Controller [8086:1e3d] (rev 04)
            Subsystem: Lenovo Device [17aa:21f6]
            Kernel driver in use: serial
    00:19.0 Ethernet controller [0200]: Intel Corporation 82579LM Gigabit Network Connection [8086:1502] (rev 04)
            Subsystem: Lenovo Device [17aa:21f3]
            Kernel driver in use: e1000e
    00:1a.0 USB controller [0c03]: Intel Corporation 7 Series/C210 Series Chipset Family USB Enhanced Host Controller #2 [8086:1e2d] (rev 04)
            Subsystem: Lenovo Device [17aa:21f6]
            Kernel driver in use: ehci-pci
    00:1b.0 Audio device [0403]: Intel Corporation 7 Series/C210 Series Chipset Family High Definition Audio Controller [8086:1e20] (rev 04)
            Subsystem: Lenovo Device [17aa:21f6]
            Kernel driver in use: snd_hda_intel
    00:1c.0 PCI bridge [0604]: Intel Corporation 7 Series/C210 Series Chipset Family PCI Express Root Port 1 [8086:1e10] (rev c4)
            Kernel driver in use: pcieport
    00:1c.1 PCI bridge [0604]: Intel Corporation 7 Series/C210 Series Chipset Family PCI Express Root Port 2 [8086:1e12] (rev c4)
            Kernel driver in use: pcieport
    00:1c.2 PCI bridge [0604]: Intel Corporation 7 Series/C210 Series Chipset Family PCI Express Root Port 3 [8086:1e14] (rev c4)
            Kernel driver in use: pcieport
    00:1d.0 USB controller [0c03]: Intel Corporation 7 Series/C210 Series Chipset Family USB Enhanced Host Controller #1 [8086:1e26] (rev 04)
            Subsystem: Lenovo Device [17aa:21f6]
            Kernel driver in use: ehci-pci
    00:1f.0 ISA bridge [0601]: Intel Corporation QM77 Express Chipset LPC Controller [8086:1e55] (rev 04)
            Subsystem: Lenovo Device [17aa:21f6]
    00:1f.2 SATA controller [0106]: Intel Corporation 7 Series Chipset Family 6-port SATA Controller [AHCI mode] [8086:1e03] (rev 04)
            Subsystem: Lenovo Device [17aa:21f6]
            Kernel driver in use: ahci
            Kernel modules: ahci
    00:1f.3 SMBus [0c05]: Intel Corporation 7 Series/C210 Series Chipset Family SMBus Controller [8086:1e22] (rev 04)
            Subsystem: Lenovo Device [17aa:21f6]
            Kernel driver in use: i801_smbus
            Kernel modules: i2c_i801
    01:00.0 VGA compatible controller [0300]: NVIDIA Corporation GK107GLM [Quadro K2000M] [10de:0ffb] (rev a1)
            Subsystem: Lenovo Device [17aa:21f5]
    02:00.0 System peripheral [0880]: Ricoh Co Ltd PCIe SDXC/MMC Host Controller [1180:e823] (rev 05)
            Subsystem: Lenovo Device [17aa:21f6]
        Kernel driver in use: sdhci-pci
    02:00.3 FireWire (IEEE 1394) [0c00]: Ricoh Co Ltd R5C832 PCIe IEEE 1394 Controller [1180:e832] (rev 04)
            Subsystem: Lenovo Device [17aa:21f6]
            Kernel driver in use: firewire_ohci
    03:00.0 Network controller [0280]: Intel Corporation Centrino Ultimate-N 6300 [8086:4238] (rev 2c)
            Subsystem: Intel Corporation Centrino Ultimate-N 6300 3x3 AGN [8086:1111]
            Kernel driver in use: iwlwifi
            Kernel modules: iwlwifi

#### [lsusb]

`root `[`#`]`lsusb`

    Bus 002 Device 002: ID 8087:0024 Intel Corp. Integrated Rate Matching Hub
    Bus 002 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub
    Bus 001 Device 005: ID 04f2:b2ea Chicony Electronics Co., Ltd Integrated Camera [ThinkPad]
    Bus 001 Device 004: ID 0a5c:21e6 Broadcom Corp. BCM20702 Bluetooth 4.0 [ThinkPad]
    Bus 001 Device 003: ID 147e:2020 Upek TouchChip Fingerprint Coprocessor (WBF advanced mode)
    Bus 001 Device 002: ID 8087:0024 Intel Corp. Integrated Rate Matching Hub
    Bus 001 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub
    Bus 004 Device 001: ID 1d6b:0003 Linux Foundation 3.0 root hub
    Bus 003 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub

## [Configuration]

#### [Intel graphics]

Configure the integrated graphics card:

[KERNEL]

    Device drivers -->
       Graphics support -->
          <*> Direct Rendering Manager (XFree86 4.1.0 and higher DRI support) --->
             <*> Enable legacy fbdev support for your modesetting driver
          <*> Intel 8xx/9xx/G3x/G4x/HD Graphics

Set the `VIDEO_CARDS` variable in [/etc/portage/package.use]:

[FILE] **`/etc/portage/package.use/00video`**

    */* VIDEO_CARDS: -* intel

Finally, when rebooting the system, press [F12], then [Tab], then scroll down three lines to enter the motherboard\'s firmware. Scroll over the right one frame, then choose [Display]. Select [Integrated] graphics mode and disable Operating System detection for Optimus.

#### [Nouveau and Intel graphics]

[KERNEL]

    Device drivers -->
       Graphics support -->
          <*> Direct Rendering Manager (XFree86 4.1.0 and higher DRI support) --->
             <*> Enable legacy fbdev support for your modesetting driver
          <*> Nouveau (NVIDIA) cards
          <*> Intel 8xx/9xx/G3x/G4x/HD Graphics

When using both [Intel](https://wiki.gentoo.org/wiki/Intel "Intel") and [nouveau](https://wiki.gentoo.org/wiki/Nouveau "Nouveau") drivers, simply add both values to the `VIDEO_CARDS` variable and update the [\@world set](https://wiki.gentoo.org/wiki/World_set_(Portage) "World set (Portage)"):

[FILE] **`/etc/portage/package.use/00video=bash`**

    */* VIDEO_CARDS:  intel nvidia

`root `[`#`]`emerge --ask --update --deep --newuse @world`

#### [NVidia Optimus graphics]

Use [Hybrid_graphics](https://wiki.gentoo.org/wiki/Hybrid_graphics "Hybrid graphics")

Finally, enter the motherboard\'s firmware and select [Discrete] graphics mode and disable Operating System detection for Optimus.

### [USB]

The Wiki\'s [USB guide](https://wiki.gentoo.org/wiki/USB/Guide "USB/Guide") can be helpful for configuring anything USB related on the system.

#### [Microphone]

The USB Audio kernel driver must be enabled for the USB microphones to work properly. This is the case for most laptops since their microphones are connected on the USB bus.

[KERNEL] **Enable support for `SND_USB_AUDIO`**

    Device Drivers -->
       Sound card support -->
          Advanced Linux Sound Architecture -->
             USB sound devices -->
                <*> USB Audio/MIDI driver

#### [Power management]

If the default USB power saving features are bothersome they can disabled by adding a configuration file to [/etc/modprobe.d/]

[FILE] **`/etc/modprobe.d/usb_auto_suspend_disable.conf`**

    #This example disables USB power saving altogether
    options usbcore autosuspend=-1

For more information visit Kernel.org\'s [USB Power Management page](https://www.kernel.org/doc/Documentation/usb/power-management.txt).

## [Tips]

### [Become familiar with helpful tools]

Many [software tools](https://wiki.gentoo.org/wiki/Software_tools_list "Software tools list") and [hardware detection utilities](https://wiki.gentoo.org/wiki/Hardware_detection "Hardware detection") are available in order to help troubleshoot a new Gentoo installation. Users who are new to Gentoo have many options to choose from. Quite a few of the packages available in the Portage tree are utilities available on other Linux distributions.

## [See also]

-   [Portage TMPDIR on tmpfs](https://wiki.gentoo.org/wiki/Portage_TMPDIR_on_tmpfs "Portage TMPDIR on tmpfs") - Instructions on how to build packages entirely in memory (RAM). This is useful for preserving read/write operations to a disk.
-   [Gentoo Cheat Sheet](https://wiki.gentoo.org/wiki/Gentoo_Cheat_Sheet "Gentoo Cheat Sheet") - A reference article for basic package management, USE flags, log file, and administration management.

## [External resources]

-   [https://www.gentoo.org/downloads/](https://www.gentoo.org/downloads/) - Obtain a Minimal Installation CD from a Gentoo mirror.
-   [http://www.thinkwiki.org/wiki/Category:W530](http://www.thinkwiki.org/wiki/Category:W530) - Lenovo Thinkpad W530\'s entry at ThinkWiki.org