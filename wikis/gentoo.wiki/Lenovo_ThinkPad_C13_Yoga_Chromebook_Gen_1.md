[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=Lenovo_ThinkPad_C13_Yoga_Chromebook_(Gen_1)&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

**Resources**

[[]][Product Information](https://www.lenovo.com/us/en/p/laptops/thinkpad/thinkpadc/thinkpad-c13-yoga-chromebook-enterprise/22tpc13c3y1)

[[]][Official Support Page](https://pcsupport.lenovo.com/us/en/products/chromebook-laptops/thinkpad-yoga-series-chromebook-laptops/thinkpad-c13-yoga-gen-1-chromebook)

[[]][Specifications](https://psref.lenovo.com/syspool/Sys/PDF/ThinkPad/ThinkPad_C13_Yoga_Gen_1_Chromebook/ThinkPad_C13_Yoga_Gen_1_Chromebook_Spec.pdf)

[[]][Specifications (by region)](https://psref.lenovo.com/Product/ThinkPad/ThinkPad_C13_Yoga_Gen_1_Chromebook?tab=model)

[[]][Hardware Maintenance Manual](https://download.lenovo.com/pccbbs/mobiles_pdf/c13_yoga_gen1_chromebook_hmm_en.pdf)

[[]][User Guide](https://download.lenovo.com/pccbbs/mobiles_pdf/c13_yoga_gen1_chromebook_ug_en.pdf)

[[]][ThinkPad Yoga](https://en.wikipedia.org/wiki/ThinkPad_Yoga "wikipedia:ThinkPad Yoga")

Lenovo ThinkPad C13 Yoga Chromebook (Gen 1) also known as zork and Google Morphius-HFAN.

## Contents

-   [[1] [Hardware]](#Hardware)
    -   [[1.1] [Standard]](#Standard)
    -   [[1.2] [Accessories]](#Accessories)
-   [[2] [Installation]](#Installation)
    -   [[2.1] [Firmware]](#Firmware)
-   [[3] [External resources]](#External_resources)

## [Hardware]

### [Standard]

  --------------------------- ---------------------------------------------------------------------------------------------------------------------- -------- ------------------------ ------------------ ---------------- -------------------------------------------------------------------------------------
  Device                      Make/model                                                                                                             Status   Vendor ID / Product ID   Kernel driver(s)   Kernel version   Notes
  VGA compatible controller   Advanced Micro Devices, Inc. \[AMD/ATI\] Picasso/Raven 2 \[Radeon Vega Series / Radeon Vega Mobile Series\] (rev c1)   Works    1002:15d8                amdgpu             5.17.0-pf1       Requires: iommu=pt kernel boot parameter
  Multimedia controller       Advanced Micro Devices, Inc. \[AMD\] Raven/Raven2/FireFlight/Renoir Audio Processor                                    Works    1022:15e2                snd_pci_acp3x      5.17.0-pf1       Maybe require tweaking due to a but at the time of writing (see externals section).
  Network controller          Realtek Semiconductor Co., Ltd. RTL8822CE 802.11ac PCIe Wireless Network Adapter                                       Works    10ec:c822                rtw_8822ce         5.17.0-pf1       ---
  Touchscreen                 N/A                                                                                                                    Works    N/A                      N/A                N/A
  --------------------------- ---------------------------------------------------------------------------------------------------------------------- -------- ------------------------ ------------------ ---------------- -------------------------------------------------------------------------------------

`root `[`#`]`lspci -nn`

    00:00.0 Host bridge [0600]: Advanced Micro Devices, Inc. [AMD] Raven/Raven2 Root Complex [1022:15d0]
    00:00.2 IOMMU [0806]: Advanced Micro Devices, Inc. [AMD] Raven/Raven2 IOMMU [1022:15d1]
    00:01.0 Host bridge [0600]: Advanced Micro Devices, Inc. [AMD] Family 17h (Models 00h-1fh) PCIe Dummy Host Bridge [1022:1452]
    00:01.2 PCI bridge [0604]: Advanced Micro Devices, Inc. [AMD] Raven/Raven2 PCIe GPP Bridge [6:0] [1022:15d3]
    00:01.3 PCI bridge [0604]: Advanced Micro Devices, Inc. [AMD] Raven/Raven2 PCIe GPP Bridge [6:0] [1022:15d3]
    00:01.7 PCI bridge [0604]: Advanced Micro Devices, Inc. [AMD] Raven/Raven2 PCIe GPP Bridge [6:0] [1022:15d3]
    00:08.0 Host bridge [0600]: Advanced Micro Devices, Inc. [AMD] Family 17h (Models 00h-1fh) PCIe Dummy Host Bridge [1022:1452]
    00:08.1 PCI bridge [0604]: Advanced Micro Devices, Inc. [AMD] Raven/Raven2 Internal PCIe GPP Bridge 0 to Bus A [1022:15db]
    00:14.0 SMBus [0c05]: Advanced Micro Devices, Inc. [AMD] FCH SMBus Controller [1022:790b] (rev 61)
    00:14.3 ISA bridge [0601]: Advanced Micro Devices, Inc. [AMD] FCH LPC Bridge [1022:790e] (rev 51)
    00:18.0 Host bridge [0600]: Advanced Micro Devices, Inc. [AMD] Raven/Raven2 Device 24: Function 0 [1022:15e8]
    00:18.1 Host bridge [0600]: Advanced Micro Devices, Inc. [AMD] Raven/Raven2 Device 24: Function 1 [1022:15e9]
    00:18.2 Host bridge [0600]: Advanced Micro Devices, Inc. [AMD] Raven/Raven2 Device 24: Function 2 [1022:15ea]
    00:18.3 Host bridge [0600]: Advanced Micro Devices, Inc. [AMD] Raven/Raven2 Device 24: Function 3 [1022:15eb]
    00:18.4 Host bridge [0600]: Advanced Micro Devices, Inc. [AMD] Raven/Raven2 Device 24: Function 4 [1022:15ec]
    00:18.5 Host bridge [0600]: Advanced Micro Devices, Inc. [AMD] Raven/Raven2 Device 24: Function 5 [1022:15ed]
    00:18.6 Host bridge [0600]: Advanced Micro Devices, Inc. [AMD] Raven/Raven2 Device 24: Function 6 [1022:15ee]
    00:18.7 Host bridge [0600]: Advanced Micro Devices, Inc. [AMD] Raven/Raven2 Device 24: Function 7 [1022:15ef]
    01:00.0 Network controller [0280]: Realtek Semiconductor Co., Ltd. RTL8822CE 802.11ac PCIe Wireless Network Adapter [10ec:c822]
    02:00.0 SD Host controller [0805]: Genesys Logic, Inc GL9750 SD Host Controller [17a0:9750] (rev 01)
    03:00.0 Non-Volatile memory controller [0108]: Sandisk Corp WD Black SN750 / PC SN730 NVMe SSD [15b7:5006]
    04:00.0 VGA compatible controller [0300]: Advanced Micro Devices, Inc. [AMD/ATI] Picasso/Raven 2 [Radeon Vega Series / Radeon Vega Mobile Series] [1002:15d8] (rev c1)
    04:00.1 Audio device [0403]: Advanced Micro Devices, Inc. [AMD/ATI] Raven/Raven2/Fenghuang HDMI/DP Audio Controller [1002:15de]
    04:00.2 Encryption controller [1080]: Advanced Micro Devices, Inc. [AMD] Family 17h (Models 10h-1fh) Platform Security Processor [1022:15df]
    04:00.3 USB controller [0c03]: Advanced Micro Devices, Inc. [AMD] Raven USB 3.1 [1022:15e0]
    04:00.4 USB controller [0c03]: Advanced Micro Devices, Inc. [AMD] Raven USB 3.1 [1022:15e1]
    04:00.5 Multimedia controller [0480]: Advanced Micro Devices, Inc. [AMD] Raven/Raven2/FireFlight/Renoir Audio Processor [1022:15e2]
    04:00.7 Non-VGA unclassified device [0000]: Advanced Micro Devices, Inc. [AMD] Raven/Raven2/Renoir Sensor Fusion Hub [1022:15e4]

`root `[`#`]`lsusb`

    Bus 004 Device 001: ID 1d6b:0003 Linux Foundation 3.0 root hub
    Bus 003 Device 003: ID 0bda:c123 Realtek Semiconductor Corp. Bluetooth Radio
    Bus 003 Device 005: ID 5986:212f Acer, Inc Integrated Camera
    Bus 003 Device 004: ID 04f2:b639 Chicony Electronics Co., Ltd EasyCamera 5M
    Bus 003 Device 002: ID 05e3:0610 Genesys Logic, Inc. Hub
    Bus 003 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub
    Bus 002 Device 001: ID 1d6b:0003 Linux Foundation 3.0 root hub
    Bus 001 Device 002: ID 046d:c539 Logitech, Inc. USB Receiver
    Bus 001 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub

### [Accessories]

  -------- ------------ -------- ------------------------ ------------------ ---------------- -------
  Device   Make/model   Status   Vendor ID / Product ID   Kernel driver(s)   Kernel version   Notes
  Stylus   N/A          Works    N/A                      N/A                N/A
  -------- ------------ -------- ------------------------ ------------------ ---------------- -------

## [Installation]

Installing Gentoo on this system is not as straight-forward. You will be required to enable developer-mode and tweak firmware settings.

### [Firmware]

`root `[`#`]`emerge --ask sys-kernel/linux-firmware`

## [External resources]

-   Sound device affected by a bug (as of 2022/04/11): [https://gitlab.freedesktop.org/pulseaudio/pulseaudio/-/issues/1030](https://gitlab.freedesktop.org/pulseaudio/pulseaudio/-/issues/1030)