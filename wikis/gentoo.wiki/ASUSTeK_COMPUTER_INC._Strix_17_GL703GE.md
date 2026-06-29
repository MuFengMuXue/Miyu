\
17\" screen with Intel(R) Core(TM) i7-8750H CPU @ 2.20GHz. Full keyboard, keypad and touchpad.

## Contents

-   [[1] [Hardware]](#Hardware)
    -   [[1.1] [Standard]](#Standard)
    -   [[1.2] [lspci]](#lspci)
    -   [[1.3] [lsusb]](#lsusb)
    -   [[1.4] [Accessories]](#Accessories)
-   [[2] [Installation]](#Installation)
    -   [[2.1] [Firmware]](#Firmware)
    -   [[2.2] [Kernel]](#Kernel)
    -   [[2.3] [Emerge]](#Emerge)
-   [[3] [Configuration]](#Configuration)
    -   [[3.1] [Example 1]](#Example_1)
-   [[4] [Troubleshooting]](#Troubleshooting)
    -   [[4.1] [Issue 1]](#Issue_1)
-   [[5] [See also]](#See_also)
-   [[6] [External resources]](#External_resources)
-   [[7] [References]](#References)

## [Hardware]

### [Standard]

### [lspci]

`user `[`$`]`lpci`

    00:00.0 Host bridge: Intel Corporation 8th Gen Core Processor Host Bridge/DRAM Registers (rev 07)
    00:01.0 PCI bridge: Intel Corporation 6th-10th Gen Core Processor PCIe Controller (x16) (rev 07)
    00:02.0 VGA compatible controller: Intel Corporation CoffeeLake-H GT2 [UHD Graphics 630]
    00:04.0 Signal processing controller: Intel Corporation Xeon E3-1200 v5/E3-1500 v5/6th Gen Core Processor Thermal Subsystem (rev 07)
    00:08.0 System peripheral: Intel Corporation Xeon E3-1200 v5/v6 / E3-1500 v5 / 6th/7th/8th Gen Core Processor Gaussian Mixture Model
    00:12.0 Signal processing controller: Intel Corporation Cannon Lake PCH Thermal Controller (rev 10)
    00:14.0 USB controller: Intel Corporation Cannon Lake PCH USB 3.1 xHCI Host Controller (rev 10)
    00:14.2 RAM memory: Intel Corporation Cannon Lake PCH Shared SRAM (rev 10)
    00:15.0 Serial bus controller: Intel Corporation Cannon Lake PCH Serial IO I2C Controller #0 (rev 10)
    00:16.0 Communication controller: Intel Corporation Cannon Lake PCH HECI Controller (rev 10)
    00:17.0 SATA controller: Intel Corporation Cannon Lake Mobile PCH SATA AHCI Controller (rev 10)
    00:1d.0 PCI bridge: Intel Corporation Cannon Lake PCH PCI Express Root Port #9 (rev f0)
    00:1d.5 PCI bridge: Intel Corporation Cannon Lake PCH PCI Express Root Port #14 (rev f0)
    00:1d.6 PCI bridge: Intel Corporation Cannon Lake PCH PCI Express Root Port #15 (rev f0)
    00:1d.7 PCI bridge: Intel Corporation Cannon Lake PCH PCI Express Root Port #16 (rev f0)
    00:1f.0 ISA bridge: Intel Corporation HM470 Chipset LPC/eSPI Controller (rev 10)
    00:1f.3 Audio device: Intel Corporation Cannon Lake PCH cAVS (rev 10)
    00:1f.4 SMBus: Intel Corporation Cannon Lake PCH SMBus Controller (rev 10)
    00:1f.5 Serial bus controller: Intel Corporation Cannon Lake PCH SPI Controller (rev 10)
    01:00.0 3D controller: NVIDIA Corporation GP107M [GeForce GTX 1050 Ti Mobile] (rev a1)
    02:00.0 Non-Volatile memory controller: Phison Electronics Corporation Device 5008 (rev 01)
    03:00.0 Network controller: Intel Corporation Wi-Fi 6 AX200 (rev 1a)
    04:00.0 Ethernet controller: Realtek Semiconductor Co., Ltd. RTL8111/8168/8411 PCI Express Gigabit Ethernet Controller (rev 15)
    05:00.0 Unassigned class [ff00]: Realtek Semiconductor Co., Ltd. RTS5229 PCI Express Card Reader (rev 01)

### [lsusb]

`user `[`$`]`lsusb`

    Bus 002 Device 003: ID 05e3:0612 Genesys Logic, Inc. Hub
    Bus 002 Device 001: ID 1d6b:0003 Linux Foundation 3.0 root hub
    Bus 001 Device 008: ID 0b05:1869 ASUSTek Computer, Inc. ITE Device(8910)
    Bus 001 Device 005: ID 2fee:1014 Holitech USB2.0 HD UVC WebCam
    Bus 001 Device 012: ID 8087:0029 Intel Corp. AX200 Bluetooth
    Bus 001 Device 011: ID 05e3:0610 Genesys Logic, Inc. Hub
    Bus 001 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub

### [Accessories]

  -------- ------------ -------- ------------------------ ------------------ ---------------- -------
  Device   Make/model   Status   Vendor ID / Product ID   Kernel driver(s)   Kernel version   Notes
  -------- ------------ -------- ------------------------ ------------------ ---------------- -------

## [Installation]

TODO

### [Firmware]

TODO

### [Kernel]

TODO

[KERNEL] **Enable support for these hardware drivers**

    Write menuconfig instructions here.

### [Emerge]

TODO

`root `[`#`]`emerge --ask }}`

## [Configuration]

TODO

### [Example 1]

TODO

## [Troubleshooting]

TODO

### [Issue 1]

TODO

## [See also]

## [External resources]

-   [https://www.asus.com/us/supportonly/ROG%20Strix%20GL703/HelpDesk_Knowledge/](https://www.asus.com/us/supportonly/ROG%20Strix%20GL703/HelpDesk_Knowledge/)
-   [https://gitlab.com/asus-linux/asusctl](https://gitlab.com/asus-linux/asusctl) \-- Requires systemd

## [References]

TODO