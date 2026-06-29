**Resources**

[[]][Home](https://pcsupport.lenovo.com/us/en/products/laptops-and-netbooks/lenovo-b-series-laptops/lenovo-b570e-notebook/)

[[]][Hardware Maintenance Manual](https://download.lenovo.com/consumer/mobiles_pub/lenovo_v570_b570_b570e_hmm_v2.0.pdf)

[[]][User Guide](https://download.lenovo.com/consumer/mobiles_pub/lenovo_b470e_b570e_ug_3rd_edition_jun_2012_english.pdf)

## Contents

-   [[1] [Hardware]](#Hardware)
    -   [[1.1] [Standard]](#Standard)
    -   [[1.2] [Fn keys]](#Fn_keys)
    -   [[1.3] [Detailed information]](#Detailed_information)
-   [[2] [Installation]](#Installation)
    -   [[2.1] [DSDT]](#DSDT)
    -   [[2.2] [Firmware]](#Firmware)
    -   [[2.3] [Kernel]](#Kernel)

## [Hardware]

### [Standard]

  ------------- ---------------------------------------------------------------------------------------- -------- ------------------------ ------------------ ---------------- -------
  Device        Make/model                                                                               Status   Vendor ID / Product ID   Kernel driver(s)   Kernel version   Notes
  CPU           Intel Celeron B800                                                                       Works    N/A                      N/A                N/A
  GPU           Intel Corporation 2nd Generation Core Processor Family DRAM Controller                   Works    8086:0104                N/A                N/A
  Sound         Intel Corporation 6 Series/C200 Series Chipset Family High Definition Audio Controller   Works    8086:1c20                N/A                N/A
  Ethernet      Realtek Semiconductor Co., Ltd. RTL8111/8168 PCI Express Gigabit Ethernet controller     Works    10ec:8168                N/A                N/A
  Wi-Fi         Broadcom Corporation BCM4313 802.11b/g/n Wireless LAN Controller                         Works    14e4:4727                N/A                N/A
  Bluetooth     Broadcom Corporation BCM4313 802.11b/g/n Wireless LAN Controller                         Works    N/A                      N/A                N/A
  Webcam        Chicony Electronics Co., Ltd Lenovo EasyCamera                                           Works    04f2:b272                N/A                N/A
  Card reader   Realtek Semiconductor Corp. RTS5139 Card Reader Controller                               Works    0bda:0139                N/A                N/A
  ------------- ---------------------------------------------------------------------------------------- -------- ------------------------ ------------------ ---------------- -------

### [Fn keys]

  ----------------- ---------- ------------- -------
  Function          Keys       Status        Notes
  Camera            Fn-Esc     Works
  Sleep             Fn-F1      Works
  LCD On/Off        Fn-F2      Works
  VGA/LCD           Fn-F3      Not tested
  N/A               Fn-F4      Not tested
  Wireless          Fn-F5      Not tested
  Touchpad On/Off   Fn-F6      Borked
  Volume +          Fn-Right   Works
  Volume -          Fn-Left    Works
  Brightness +      Fn-Up      Not tested
  Brightness -      Fn-Down    Not tested
  ----------------- ---------- ------------- -------

### [Detailed information]

`root `[`#`]`lspci -nn`

    00:00.0 Host bridge [0600]: Intel Corporation 2nd Generation Core Processor Family DRAM Controller [8086:0104] (rev 09)
    00:02.0 VGA compatible controller [0300]: Intel Corporation 2nd Generation Core Processor Family Integrated Graphics Controller [8086:0106] (rev 09)
    00:16.0 Communication controller [0780]: Intel Corporation 6 Series/C200 Series Chipset Family MEI Controller #1 [8086:1c3a] (rev 04)
    00:1a.0 USB controller [0c03]: Intel Corporation 6 Series/C200 Series Chipset Family USB Enhanced Host Controller #2 [8086:1c2d] (rev 05)
    00:1b.0 Audio device [0403]: Intel Corporation 6 Series/C200 Series Chipset Family High Definition Audio Controller [8086:1c20] (rev 05)
    00:1c.0 PCI bridge [0604]: Intel Corporation 6 Series/C200 Series Chipset Family PCI Express Root Port 1 [8086:1c10] (rev b5)
    00:1c.1 PCI bridge [0604]: Intel Corporation 6 Series/C200 Series Chipset Family PCI Express Root Port 2 [8086:1c12] (rev b5)
    00:1c.3 PCI bridge [0604]: Intel Corporation 6 Series/C200 Series Chipset Family PCI Express Root Port 4 [8086:1c16] (rev b5)
    00:1d.0 USB controller [0c03]: Intel Corporation 6 Series/C200 Series Chipset Family USB Enhanced Host Controller #1 [8086:1c26] (rev 05)
    00:1f.0 ISA bridge [0601]: Intel Corporation HM65 Express Chipset Family LPC Controller [8086:1c49] (rev 05)
    00:1f.2 SATA controller [0106]: Intel Corporation 6 Series/C200 Series Chipset Family 6 port SATA AHCI Controller [8086:1c03] (rev 05)
    00:1f.3 SMBus [0c05]: Intel Corporation 6 Series/C200 Series Chipset Family SMBus Controller [8086:1c22] (rev 05)
    02:00.0 Network controller [0280]: Broadcom Corporation BCM4313 802.11b/g/n Wireless LAN Controller [14e4:4727] (rev 01)
    03:00.0 Ethernet controller [0200]: Realtek Semiconductor Co., Ltd. RTL8111/8168 PCI Express Gigabit Ethernet controller [10ec:8168] (rev 06)

`root `[`#`]`lsusb`

    Bus 001 Device 002: ID 8087:0024 Intel Corp. Integrated Rate Matching Hub
    Bus 002 Device 002: ID 8087:0024 Intel Corp. Integrated Rate Matching Hub
    Bus 001 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub
    Bus 002 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub
    Bus 001 Device 003: ID 04f2:b272 Chicony Electronics Co., Ltd Lenovo EasyCamera
    Bus 002 Device 003: ID 0bda:0139 Realtek Semiconductor Corp. RTS5139 Card Reader Controller

## [Installation]

### [DSDT]

Extract ACPI tables:

    cat /sys/firmware/acpi/tables/DSDT > dsdt.dat

Decompile:

    iasl -d dsdt.dat

Recompile:

    iasl -tc dsdt.dsl

Errors, Remarks and Warnings:

    Intel ACPI Component Architecture
    ASL Optimizing Compiler version 20130117-32 [Oct  3 2013]
    Copyright (c) 2000 - 2013 Intel Corporation
    dsdt.dsl   4461:                             Name (_T_0, Zero)
    Remark   5011 -        Use of compiler reserved name ^  (_T_0)
    ...
    dsdt.dsl   7854:                 Method (_CRS, 0, NotSerialized)
    Warning  1114 -                            ^ Not all control paths return a value (_CRS)
    ...
    dsdt.dsl  10690:                     Name (_PLD, Buffer (0x10)
    Error    4105 -      Invalid object type for reserved name ^  (_PLD: found BUFFER, requires Package)
    ...
    Compilation complete. 7 Errors, 10 Warnings, 7 Remarks, 60 Optimizations

To remove Remarks change:

    Name (_T_0, Zero)

to:

    Name (T_0, Zero)

To remove Errors change:

    Name (_PLD, Buffer (0x10)


to:

    Name (_PLD, Package (0x01)
    }

To remove Warnings, `Return (0)` should be added at the end of the function:

    Method (_CRS, 0, NotSerialized)

Enable custom DSDT in kernel:

[KERNEL] **DSDT**

    Device Drivers  --->
       Generic Driver Options  --->
       [ ] Select only drivers that don't need compile-time external firmware

    Power management and ACPI options  --->
       [*] ACPI (Advanced Configuration and Power Interface) Support  --->
       (/boot/dsdl.hex) Custom DSDT Table file to include

** Note**\
Working with dsdt latest version of iasl should be used

### [Firmware]

The wireless card requires [[[sys-kernel/linux-firmware]](https://packages.gentoo.org/packages/sys-kernel/linux-firmware)[]] to be installed:

`root `[`#`]`emerge --ask sys-kernel/linux-firmware`

### [Kernel]

[KERNEL] **Sound**

    Device Drivers  --->
       Sound --->
       <*> Sound card support
       <*>   Advanced Linux Sound Architecture --->
       [*]     PCI devices --->
       <*>       Intel HD Audio --->

[KERNEL] **Ethernet**

    Device Drivers  --->
       [*] Network Device Support  --->
       [*]   Ethernet driver support  --->
       [*]     Realtek devices
       < >       RealTek RTL-8139 C+ PCI Fast Ethernet Adapter support
       < >       RealTek RTL-8129/8130/8139 PCI Fast Ethernet Adapter support
       <*>       Realtek 8169 gigabit ethernet support

[KERNEL] **Wi-Fi**

    Device Drivers  --->
       [*] Network Device Support  --->
       [*]   Wireless LAN  --->
       <*>     Broadcom IEEE802.11n PCIe SoftMAC WLAN driver
           Broadcom specific AMBA  --->
       <*>   BCMA support

[KERNEL] **Bluetooth**

    [*] Networking support --->
         <*>   Bluetooth subsystem support --->
         <*>     L2CAP protocol support
         <*>     SCO links support
         <*>     RFCOMM protocol support
         [*]       RFCOMM tty support
         <*>     BNEP protocol support
         [*]       Multicast filter support
         [*]       Protocol filter support
         <*>     HIDP protocol support
                 Bluetooth device drivers --->
         <*>       HCI USB driver

[KERNEL] **Fn keys**

    Device Drivers  --->
        [*] X86 Platform Specific Device Drivers  --->
            <*>   Lenovo IdeaPad Laptop Extras
            <*> WMI

[KERNEL] **Webcam**

    Device Drivers --->
       <*> Multimedia Support --->
       [*]   Cameras/video grabbers support
       [*]   Media USB Adapters  --->
       <*>     USB Video Class (UVC)
       [*]       UVC input events device support

** Tip**\
To test the camera, install the [[[media-video/mplayer]](https://packages.gentoo.org/packages/media-video/mplayer)[]] package with the **v4l** USE flag enabled and run the command:

`user `[`$`]`mplayer -tv driver=v4l2:device=/dev/video0 tv://`

[KERNEL] **Card reader**

    Device Drivers --->
       [*] Staging drivers  --->
       <*>   Realtek RTS5139 USB card reader support