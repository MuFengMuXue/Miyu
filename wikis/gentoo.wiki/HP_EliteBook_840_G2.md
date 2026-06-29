**Resources**

[[]][Official Support Page](https://support.hp.com/us-en/product/details/hp-elitebook-840-g2-notebook-pc/7343202)

[[]][Specifications](https://support.hp.com/us-en/document/c04552057)

[[]][Hardware Maintenance Manual](https://h10032.www1.hp.com/ctg/Manual/c04560057.pdf)

[[]][User Guide](https://h10032.www1.hp.com/ctg/Manual/c04830722.pdf)

[[]][HP EliteBook](https://en.wikipedia.org/wiki/HP_EliteBook "wikipedia:HP EliteBook")

Gentoo is able to run smoothly on this hardware, however it is recommended to SPEND some time in the BIOS to know its hardware and get familiar with is names.

\

## Contents

-   [[1] [Hardware]](#Hardware)
-   [[2] [BIOS]](#BIOS)
-   [[3] [Partition Layout]](#Partition_Layout)
-   [[4] [Hardware as reported by Linux]](#Hardware_as_reported_by_Linux)

## [Hardware]

The following is the hardware as listed by BIOS. **It is strongly recommended that you update the BIOS before installing Gentoo** , there is an option to update it without the need to install an operative system, you just need to adjust network settings inside BIOS.

-   System Board ID: 2216
-   BIOS Version: M71 Ver. 01.27
-   Bios Release Date: July 12th 2018
-   BIOS Revision: INTEL(R) VBIOS (5.5.1040)
-   Processor Type: Intel Core i7-5600U
-   Processor Speed: 2.60 GHz
-   Memory Size: 8192 MB RAM
-   Memory Slot Information: 2x Samsung 4096 MB RAM @ 1600 MHz
-   HDD Model: SanDisk SD7SB2Q-512G-1006
-   HDD Size: 512GB
-   WLAN
-   Bluetooth
-   Ethernet

\

## [BIOS]

Inside BIOS there are three \"Boot Modes\" available:

1.  Legacy
2.  UEFI Hybrid (With CSM)
3.  UEFI Native (Without CSM)

For some unknown reason I wasn\'t able to boot Linux in \"Legacy mode\", internet pointed out that may be related to HDD Model listed in section above, so I selected \"UEFI Hybrid\" and it could be booted correctly. You just need to take note that \"UEFI Hybrid\" allows you to have MBR/DOS partition layout.

## [Partition Layout]

As stated in the previous version, installation was done using MBR/DOS partition layout. If using such layout, it is recommended that first partition starts at sector 2048

## [Hardware as reported by Linux]

`root `[`#`]`lspci -nn`

    00:00.0 Host bridge [0600]: Intel Corporation Broadwell-U Host Bridge -OPI [8086:1604] (rev 09)
    00:02.0 VGA compatible controller [0300]: Intel Corporation HD Graphics 5500 [8086:1616] (rev 09)
    00:03.0 Audio device [0403]: Intel Corporation Broadwell-U Audio Controller [8086:160c] (rev 09)
    00:14.0 USB controller [0c03]: Intel Corporation Wildcat Point-LP USB xHCI Controller [8086:9cb1] (rev 03)
    00:16.0 Communication controller [0780]: Intel Corporation Wildcat Point-LP MEI Controller #1 [8086:9cba] (rev 03)
    00:19.0 Ethernet controller [0200]: Intel Corporation Ethernet Connection (3) I218-LM [8086:15a2] (rev 03)
    00:1b.0 Audio device [0403]: Intel Corporation Wildcat Point-LP High Definition Audio Controller [8086:9ca0] (rev 03)
    00:1c.0 PCI bridge [0604]: Intel Corporation Wildcat Point-LP PCI Express Root Port #1 [8086:9c90] (rev e3)
    00:1c.1 PCI bridge [0604]: Intel Corporation Wildcat Point-LP PCI Express Root Port #2 [8086:9c92] (rev e3)
    00:1c.3 PCI bridge [0604]: Intel Corporation Wildcat Point-LP PCI Express Root Port #4 [8086:9c96] (rev e3)
    00:1d.0 USB controller [0c03]: Intel Corporation Wildcat Point-LP USB EHCI Controller [8086:9ca6] (rev 03)
    00:1f.0 ISA bridge [0601]: Intel Corporation Wildcat Point-LP LPC Controller [8086:9cc3] (rev 03)
    00:1f.2 SATA controller [0106]: Intel Corporation Wildcat Point-LP SATA Controller [AHCI Mode] [8086:9c83] (rev 03)
    00:1f.3 SMBus [0c05]: Intel Corporation Wildcat Point-LP SMBus Controller [8086:9ca2] (rev 03)
    02:00.0 Unassigned class [ff00]: Realtek Semiconductor Co., Ltd. RTS5227 PCI Express Card Reader [10ec:5227] (rev 01)
    03:00.0 Network controller [0280]: Intel Corporation Wireless 7265 [8086:095a] (rev 48)

\

`root `[`#`]`lsusb`

    Bus 002 Device 001: ID 1d6b:0003 Linux Foundation 3.0 root hub
    Bus 001 Device 006: ID 04ca:7053 Lite-On Technology Corp.
    Bus 001 Device 005: ID 138a:003f Validity Sensors, Inc. VFS495 Fingerprint Reader
    Bus 001 Device 004: ID 8087:0a2b Intel Corp.
    Bus 001 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub