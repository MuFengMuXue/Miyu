**Resources**

[[]][Official Support Page](https://support.hp.com/us-en/product/details/hp-elitebook-840-g3-notebook-pc/7815294)

[[]][Specifications](https://support.hp.com/my-en/document/c05259054)

[[]][Hardware Maintenance Manual](https://h10032.www1.hp.com/ctg/Manual/c04887250.pdf)

[[]][User Guide](https://h10032.www1.hp.com/ctg/Manual/c04882471.pdf)

[[]][HP EliteBook](https://en.wikipedia.org/wiki/HP_EliteBook "wikipedia:HP EliteBook")

## Contents

-   [[1] [Hardware]](#Hardware)
    -   [[1.1] [Standard]](#Standard)
    -   [[1.2] [Accessories]](#Accessories)
    -   [[1.3] [Detailed information]](#Detailed_information)
-   [[2] [Installation]](#Installation)
    -   [[2.1] [Firmware]](#Firmware)
    -   [[2.2] [Kernel]](#Kernel)

## [Hardware]

### [Standard]

  ----------------------------- ------------------------------------------------------- ------------- ------------------------ ------------------ ---------------- ------------------------------------------------
  Device                        Make/model                                              Status        Vendor ID / Product ID   Kernel driver(s)   Kernel version   Notes
  Fingerprint Reader            Validity Sensors, Inc. VFS495 Fingerprint Reader        Not tested    138a:003f                N/A                N/A
  Bluetooth                     N/A                                                     Not tested    N/A                      N/A                N/A
  Video card                    Intel Corporation HD Graphics 520 (rev 07)              Works         8086:1916                N/A                4.13.0-pf4
  Ethernet controller           Intel Corporation Ethernet Connection I219-V (rev 21)   Works         8086:1570                N/A                4.13.0-pf4
  Wireless network controller   Intel Corporation Wireless 8260 (rev 3a)                Works         8086:24f3                N/A                4.13.0-pf4       Interface modes other than managed not tested.
  ----------------------------- ------------------------------------------------------- ------------- ------------------------ ------------------ ---------------- ------------------------------------------------

### [Accessories]

  -------- ----------------------------------- -------- ------------------------ ------------------ ---------------- -------
  Device   Make/model                          Status   Vendor ID / Product ID   Kernel driver(s)   Kernel version   Notes
  Dock     HP 2013 UltraSlim Docking Station   Works    N/A                      N/A                4.13.0-pf4
  -------- ----------------------------------- -------- ------------------------ ------------------ ---------------- -------

### [Detailed information]

`root `[`#`]`lspci -nn`

    00:00.0 Host bridge [0600]: Intel Corporation Xeon E3-1200 v5/E3-1500 v5/6th Gen Core Processor Host Bridge/DRAM Registers [8086:1904] (rev 08)
    00:02.0 VGA compatible controller [0300]: Intel Corporation HD Graphics 520 [8086:1916] (rev 07)
    00:14.0 USB controller [0c03]: Intel Corporation Sunrise Point-LP USB 3.0 xHCI Controller [8086:9d2f] (rev 21)
    00:14.2 Signal processing controller [1180]: Intel Corporation Sunrise Point-LP Thermal subsystem [8086:9d31] (rev 21)
    00:15.0 Signal processing controller [1180]: Intel Corporation Sunrise Point-LP Serial IO I2C Controller #0 [8086:9d60] (rev 21)
    00:16.0 Communication controller [0780]: Intel Corporation Sunrise Point-LP CSME HECI #1 [8086:9d3a] (rev 21)
    00:17.0 SATA controller [0106]: Intel Corporation Sunrise Point-LP SATA Controller [AHCI mode] [8086:9d03] (rev 21)
    00:1c.0 PCI bridge [0604]: Intel Corporation Device [8086:9d11] (rev f1)
    00:1c.3 PCI bridge [0604]: Intel Corporation Device [8086:9d13] (rev f1)
    00:1f.0 ISA bridge [0601]: Intel Corporation Sunrise Point-LP LPC Controller [8086:9d48] (rev 21)
    00:1f.2 Memory controller [0580]: Intel Corporation Sunrise Point-LP PMC [8086:9d21] (rev 21)
    00:1f.3 Audio device [0403]: Intel Corporation Sunrise Point-LP HD Audio [8086:9d70] (rev 21)
    00:1f.4 SMBus [0c05]: Intel Corporation Sunrise Point-LP SMBus [8086:9d23] (rev 21)
    00:1f.6 Ethernet controller [0200]: Intel Corporation Ethernet Connection I219-V [8086:1570] (rev 21)
    01:00.0 Unassigned class [ff00]: Realtek Semiconductor Co., Ltd. RTS522A PCI Express Card Reader [10ec:522a] (rev 01)
    02:00.0 Network controller [0280]: Intel Corporation Wireless 8260 [8086:24f3] (rev 3a)

`root `[`#`]`lsusb`

    Bus 002 Device 001: ID 1d6b:0003 Linux Foundation 3.0 root hub
    Bus 001 Device 006: ID 04ca:7053 Lite-On Technology Corp.
    Bus 001 Device 005: ID 138a:003f Validity Sensors, Inc. VFS495 Fingerprint Reader
    Bus 001 Device 004: ID 8087:0a2b Intel Corp.
    Bus 001 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub

## [Installation]

[FILE] **`/etc/portage/make.conf`**

    INPUT_DEVICES="libinput synaptics"
    VIDEO_CARDS="i965 intel"

### [Firmware]

`root `[`#`]`emerge --ask sys-kernel/linux-firmware`

### [Kernel]

[KERNEL] **Ethernet controller**

    Generic Driver Options  --->
       [*] Network device support  ---
          [*]   Ethernet driver support  --->
             [*]   Intel devices
             <*>     Intel(R) PRO/1000 PCI-Express Gigabit Ethernet support

[KERNEL] **Wireless network controller**

    Generic Driver Options  --->
       [*] Network device support  ---
          [*]   Wireless LAN  --->
             [*]   Intel devices
             <M>     Intel Wireless WiFi Next Gen AGN - Wireless-N/Advanced-N/Ultimate-N (iwlwifi)
             <M>       Intel Wireless WiFi DVM Firmware support

[KERNEL] **Audio device**

    Generic Driver Options  --->
       <*> Sound card support  --->
          <*>   Advanced Linux Sound Architecture  --->
             [*]   PCI sound devices  --->
                   HD-Audio  --->
                      <*> HD Audio PCI
                      <*> Build Conexant HD-audio codec support