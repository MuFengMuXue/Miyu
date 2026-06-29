**Resources**

[[]][Official Support Page](https://support.hp.com/us-en/product/OMEN-by-HP-15-ax200-Laptop-PC/13810162/model/15464233)

[[]][Specifications](https://support.hp.com/us-en/document/c05391085)

[[]][Hardware Maintenance Manual](https://h10032.www1.hp.com/ctg/Manual/c05357609.pdf)

[[]][User Guide](https://h10032.www1.hp.com/ctg/Manual/c05217360.pdf)

[[]][HP Omen](https://en.wikipedia.org/wiki/HP_Omen "wikipedia:HP Omen")

## [Hardware]

### [Standard]

** Note**\
As of December 2, 2017‎, the NVidia GTX 1050 card was not successfully made to work on Gentoo, although it has been tested to work fine on Ubuntu 16.04 with NVidia\'s driver version 384.90, see [https://forums.gentoo.org/viewtopic-p-8148988.html](https://forums.gentoo.org/viewtopic-p-8148988.html)

  ----------- ------------------------------------------------------------------------------------------- ------------- ------------------------ ------------------ ---------------- -------
  Device      Make/model                                                                                  Status        Vendor ID / Product ID   Kernel driver(s)   Kernel version   Notes
  CPU         Intel® Core™ i5-7300HQ                                                                      Works         N/A                      N/A                N/A
  iGPU        Intel Corporation Device                                                                    Works         8086:591b                N/A                N/A
  dGPU        NVIDIA® GeForce® GTX 1050                                                                   Borked        10de:1c8d                N/A                N/A
  SSD         Samsung Electronics Co Ltd NVMe SSD Controller SM961/PM961                                  Works         144d:a804                N/A                N/A
  Ethernet    Realtek Semiconductor Co., Ltd. RTL8111/8168/8411 PCI Express Gigabit Ethernet Controller   Works         10ec:8168                N/A                N/A
  Wi-Fi       Intel Corporation Wireless 7265                                                             Works         8086:095a                N/A                N/A
  Bluetooth   N/A                                                                                         Not tested    N/A                      N/A                N/A
  ----------- ------------------------------------------------------------------------------------------- ------------- ------------------------ ------------------ ---------------- -------

### [Detailed information]

`root `[`#`]`lspci -nn`

    00:00.0 Host bridge [0600]: Intel Corporation Device [8086:5910] (rev 05)
    00:01.0 PCI bridge [0604]: Intel Corporation Skylake PCIe Controller (x16) [8086:1901] (rev 05)
    00:02.0 VGA compatible controller [0300]: Intel Corporation Device [8086:591b] (rev 04)
    00:04.0 Signal processing controller [1180]: Intel Corporation Skylake Processor Thermal Subsystem [8086:1903] (rev 05)
    00:14.0 USB controller [0c03]: Intel Corporation Sunrise Point-H USB 3.0 xHCI Controller [8086:a12f] (rev 31)
    00:14.2 Signal processing controller [1180]: Intel Corporation Sunrise Point-H Thermal subsystem [8086:a131] (rev 31)
    00:16.0 Communication controller [0780]: Intel Corporation Sunrise Point-H CSME HECI #1 [8086:a13a] (rev 31)
    00:17.0 SATA controller [0106]: Intel Corporation Sunrise Point-H SATA Controller [AHCI mode] [8086:a103] (rev 31)
    00:1c.0 PCI bridge [0604]: Intel Corporation Sunrise Point-H PCI Express Root Port #1 [8086:a110] (rev f1)
    00:1c.4 PCI bridge [0604]: Intel Corporation Sunrise Point-H PCI Express Root Port #5 [8086:a114] (rev f1)
    00:1c.5 PCI bridge [0604]: Intel Corporation Sunrise Point-H PCI Express Root Port #6 [8086:a115] (rev f1)
    00:1c.6 PCI bridge [0604]: Intel Corporation Sunrise Point-H PCI Express Root Port #7 [8086:a116] (rev f1)
    00:1d.0 PCI bridge [0604]: Intel Corporation Sunrise Point-H PCI Express Root Port #9 [8086:a118] (rev f1)
    00:1f.0 ISA bridge [0601]: Intel Corporation Sunrise Point-H LPC Controller [8086:a152] (rev 31)
    00:1f.2 Memory controller [0580]: Intel Corporation Sunrise Point-H PMC [8086:a121] (rev 31)
    00:1f.3 Audio device [0403]: Intel Corporation Device [8086:a171] (rev 31)
    00:1f.4 SMBus [0c05]: Intel Corporation Sunrise Point-H SMBus [8086:a123] (rev 31)
    01:00.0 3D controller [0302]: NVIDIA Corporation GP107M [GeForce GTX 1050 Mobile] [10de:1c8d] (rev a1)
    03:00.0 Unassigned class [ff00]: Realtek Semiconductor Co., Ltd. RTS522A PCI Express Card Reader [10ec:522a] (rev 01)
    04:00.0 Network controller [0280]: Intel Corporation Wireless 7265 [8086:095a] (rev 61)
    05:00.0 Ethernet controller [0200]: Realtek Semiconductor Co., Ltd. RTL8111/8168/8411 PCI Express Gigabit Ethernet Controller [10ec:8168] (rev 15)
    06:00.0 Non-Volatile memory controller [0108]: Samsung Electronics Co Ltd NVMe SSD Controller SM961/PM961 [144d:a804]

`user `[`$`]`lsusb`

    Bus 002 Device 001: ID 1d6b:0003 Linux Foundation 3.0 root hub
    Bus 001 Device 003: ID 8087:0a2a Intel Corp.
    Bus 001 Device 002: ID 05c8:038e Cheng Uei Precision Industry Co., Ltd (Foxlink)
    Bus 001 Device 004: ID 046d:c534 Logitech, Inc. Unifying Receiver
    Bus 001 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub