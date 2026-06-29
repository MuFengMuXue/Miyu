**Resources**

[[]][Official Support Page](https://www.dell.com/support/home/en-us/product-support/product/alienware-15-laptop/overview)

[[]][Specifications](https://dl.dell.com/content/manual38481186-alienware-15-r3-setup-and-specifications.pdf)

[[]][Hardware Maintenance Manual](https://dl.dell.com/topicspdf/alienware-15-laptop_service-manual_en-us.pdf)

[[]][Alienware](https://en.wikipedia.org/wiki/Alienware#Laptops "wikipedia:Alienware")

The **Dell Alienware 15 R3** is a 15-inch laptop released in 2016. ^[\[1\]](#cite_note-1)^

## Contents

-   [[1] [Hardware]](#Hardware)
    -   [[1.1] [Standard]](#Standard)
    -   [[1.2] [Detailed information]](#Detailed_information)
-   [[2] [References]](#References)

## [Hardware]

### [Standard]

  ----------------------------- ----------------------------------------------------------------------------------- -------- ------------------------ ------------------ ---------------- ------------------------------------------------
  Device                        Make/model                                                                          Status   Vendor ID / Product ID   Kernel driver(s)   Kernel version   Notes
  CPU                           Intel(R) Core(TM) i7-7700HQ CPU @ 2.80GHz                                           Works    N/A                      N/A                4.13.0-pf4
  Video card                    Advanced Micro Devices, Inc. \[AMD/ATI\] Ellesmere \[Radeon RX 470/480\] (rev c5)   Works    1028:0774                amdgpu             4.13.0-pf4
  Ethernet controller           Qualcomm Atheros Device (rev 10)                                                    Works    1969:e0b1                alx                4.13.0-pf4
  Wireless network controller   Qualcomm Atheros QCA6174 802.11ac Wireless Network Adapter (rev 32)                 Works    168c:003e                ath10k_pci         4.13.0-pf4       Interface modes other than managed not tested.
  ----------------------------- ----------------------------------------------------------------------------------- -------- ------------------------ ------------------ ---------------- ------------------------------------------------

### [Detailed information]

`root `[`#`]`lspci -nn`

    00:00.0 Host bridge [0600]: Intel Corporation Device [8086:5910] (rev 05)
    00:01.0 PCI bridge [0604]: Intel Corporation Skylake PCIe Controller (x16) [8086:1901] (rev 05)
    00:01.2 PCI bridge [0604]: Intel Corporation Skylake PCIe Controller (x4) [8086:1909] (rev 05)
    00:02.0 VGA compatible controller [0300]: Intel Corporation Device [8086:591b] (rev 04)
    00:04.0 Signal processing controller [1180]: Intel Corporation Skylake Processor Thermal Subsystem [8086:1903] (rev 05)
    00:14.0 USB controller [0c03]: Intel Corporation Sunrise Point-H USB 3.0 xHCI Controller [8086:a12f] (rev 31)
    00:14.2 Signal processing controller [1180]: Intel Corporation Sunrise Point-H Thermal subsystem [8086:a131] (rev 31)
    00:16.0 Communication controller [0780]: Intel Corporation Sunrise Point-H CSME HECI #1 [8086:a13a] (rev 31)
    00:17.0 RAID bus controller [0104]: Intel Corporation SATA Controller [RAID mode] [8086:2822] (rev 31)
    00:1c.0 PCI bridge [0604]: Intel Corporation Sunrise Point-H PCI Express Root Port #1 [8086:a110] (rev f1)
    00:1c.4 PCI bridge [0604]: Intel Corporation Sunrise Point-H PCI Express Root Port #5 [8086:a114] (rev f1)
    00:1c.5 PCI bridge [0604]: Intel Corporation Sunrise Point-H PCI Express Root Port #6 [8086:a115] (rev f1)
    00:1f.0 ISA bridge [0601]: Intel Corporation Sunrise Point-H LPC Controller [8086:a154] (rev 31)
    00:1f.2 Memory controller [0580]: Intel Corporation Sunrise Point-H PMC [8086:a121] (rev 31)
    00:1f.3 Audio device [0403]: Intel Corporation Device [8086:a171] (rev 31)
    00:1f.4 SMBus [0c05]: Intel Corporation Sunrise Point-H SMBus [8086:a123] (rev 31)
    01:00.0 VGA compatible controller [0300]: Advanced Micro Devices, Inc. [AMD/ATI] Ellesmere [Radeon RX 470/480] [1002:67df] (rev c5)
    01:00.1 Audio device [0403]: Advanced Micro Devices, Inc. [AMD/ATI] Device [1002:aaf0]
    3c:00.0 Ethernet controller [0200]: Qualcomm Atheros Device [1969:e0b1] (rev 10)
    3d:00.0 Network controller [0280]: Qualcomm Atheros QCA6174 802.11ac Wireless Network Adapter [168c:003e] (rev 32)

`root `[`#`]`lsusb`

    Bus 002 Device 001: ID 1d6b:0003 Linux Foundation 3.0 root hub
    Bus 001 Device 004: ID 0bda:58c2 Realtek Semiconductor Corp.
    Bus 001 Device 003: ID 0cf3:e300 Qualcomm Atheros Communications
    Bus 001 Device 002: ID 187c:0530 Alienware Corporation
    Bus 001 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub

## [References]

1.  [[[↑](#cite_ref-1)] [[https://en.wikipedia.org/wiki/Alienware#Laptops](https://en.wikipedia.org/wiki/Alienware#Laptops)]]