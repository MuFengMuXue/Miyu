**Resources**

[[]][Home](https://pcsupport.lenovo.com/us/en/products/laptops-and-netbooks/lenovo-s-series-laptops/lenovo-s20-30-notebook)

[[]][Hardware Maintenance Manual](https://download.lenovo.com/consumer/mobiles_pub/lenovo_s20_30_s20_30touch_hmm.pdf)

[[]][User Guide](https://download.lenovo.com/consumer/mobiles_pub/lenovo_s20_30_s20_30touch_ug_english.pdf)

This laptop has two versions, touch and non-touch. This article is based on the non-touch version.

## Contents

-   [[1] [Hardware]](#Hardware)
    -   [[1.1] [Wi-Fi]](#Wi-Fi)
    -   [[1.2] [Bluetooth]](#Bluetooth)
    -   [[1.3] [Ethernet]](#Ethernet)
    -   [[1.4] [Graphics]](#Graphics)
    -   [[1.5] [Smart card reader]](#Smart_card_reader)
    -   [[1.6] [UEFI support]](#UEFI_support)
-   [[2] [External resources]](#External_resources)

## [Hardware]

  ----------- -----------------------------------
  Class       Product
  Processor   Intel® Pentium® Processor N3530
  Wi-Fi       Qualcomm Atheros QCA9565 / AR9565
  Ethernet    Realtek
  Bluetooth   Atheros AR3012
  Audio       Intel HD Audio
  Graphics    Intel HD Graphics
  ----------- -----------------------------------

`root `[`#`]`lspci -nn`

    00:00.0 Host bridge [0600]: Intel Corporation Atom Processor Z36xxx/Z37xxx Series SoC Transaction Register [8086:0f00] (rev 0e)
    00:02.0 VGA compatible controller [0300]: Intel Corporation Atom Processor Z36xxx/Z37xxx Series Graphics & Display [8086:0f31] (rev 0e)
    00:13.0 SATA controller [0106]: Intel Corporation Device [8086:0f23] (rev 0e)
    00:14.0 USB controller [0c03]: Intel Corporation Atom Processor Z36xxx/Z37xxx Series USB xHCI [8086:0f35] (rev 0e)
    00:1a.0 Encryption controller [1080]: Intel Corporation Atom Processor Z36xxx/Z37xxx Series Trusted Execution Engine [8086:0f18] (rev 0e)
    00:1b.0 Audio device [0403]: Intel Corporation Atom Processor Z36xxx/Z37xxx Series High Definition Audio Controller [8086:0f04] (rev 0e)
    00:1c.0 PCI bridge [0604]: Intel Corporation Device [8086:0f48] (rev 0e)
    00:1c.1 PCI bridge [0604]: Intel Corporation Device [8086:0f4a] (rev 0e)
    00:1f.0 ISA bridge [0601]: Intel Corporation Atom Processor Z36xxx/Z37xxx Series Power Control Unit [8086:0f1c] (rev 0e)
    00:1f.3 SMBus [0c05]: Intel Corporation Device [8086:0f12] (rev 0e)
    01:00.0 Ethernet controller [0200]: Realtek Semiconductor Co., Ltd. RTL8101E/RTL8102E PCI Express Fast Ethernet controller [10ec:8136] (rev 08)
    02:00.0 Network controller [0280]: Qualcomm Atheros QCA9565 / AR9565 Wireless Network Adapter [168c:0036] (rev 01)

`root `[`#`]`lsusb`

    Bus 001 Device 007: ID 0bda:0129 Realtek Semiconductor Corp. RTS5129 Card Reader Controller
    Bus 001 Device 005: ID 0cf3:3004 Atheros Communications, Inc. AR3012 Bluetooth 4.0
    Bus 002 Device 001: ID 1d6b:0003 Linux Foundation 3.0 root hub
    Bus 001 Device 004: ID 05e3:0610 Genesys Logic, Inc. 4-port hub
    Bus 001 Device 003: ID 5986:054a Acer, Inc
    Bus 001 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub

### [Wi-Fi]

For Wi-Fi to work, enable the ath9k driver (ATH9K & ATH9K_PCI) and enable the bluetooth coexistence for the bluetooth to work (ATH9K_BTCOEX_SUPPORT)

[KERNEL] **Qualcomm Atheros QCA9565 / AR9565**

    Device Drivers  --->
    [*] Network Device support --->
    [*]  Wireless Lan --->
    <*>   Atheros Wireless Cards --->
    [*]    Atheros bluetooth coexistence support
    <*>    Atheros 802.11n wireless cards support
    [*]       Atheros ath9k PCI/PCIe bus support

### [Bluetooth]

Enable ath3k, in kernel BT_ATH3K

[KERNEL] **Qualcomm Atheros QCA9565 / AR9565**

    [*] Networking support  --->
    <*>   Bluetooth subsystem support --->
    [*]     Bluetooth Classic (BR/EDR) features
    [*]     Bluetooth Low Energy (LE) features
             Bluetooth device drivers --->
    <*>       Atheros firmware download driver

### [Ethernet]

Enable r8169

[KERNEL] **RTL8101E/RTL8102E**

    Device Drivers  --->
    [*] Network Device support --->
    [*]  Ethernet driver support--->
    <*>   Realtek devices
    [*]    Realtek 8169 gigabit ethernet support

If built as module, it will be named r8169

### [Graphics]

Use intel HD graphics: [intel](https://wiki.gentoo.org/wiki/Intel "Intel")

### [Smart card reader]

### [UEFI support]

If you want to directly load the kernel from the UEFI:

-   Enable UEFI-only loading (no legacy support)
-   Set an administrator password
-   Disable secure boot

Then follow the instructions from the wiki: [EFI stub](https://wiki.gentoo.org/wiki/EFI_stub "EFI stub")

## [External resources]

-   [https://wiki.archlinux.org/title/Lenovo_S20-30](https://wiki.archlinux.org/title/Lenovo_S20-30)