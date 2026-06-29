**Resources**

[[]][Official Support Page](https://support.hp.com/us-en/product/hp-elitebook-840-g6-notebook-pc/26609796)

[[]][Specifications](https://support.hp.com/us-en/document/c06352019)

[[]][Hardware Maintenance Manual](https://h10032.www1.hp.com/ctg/Manual/c06358101.pdf)

[[]][User Guide](https://h10032.www1.hp.com/ctg/Manual/c06366686.pdf)

[[]][HP EliteBook](https://en.wikipedia.org/wiki/HP_EliteBook "wikipedia:HP EliteBook")

This article written on HP EliteBook 840 G6 (4WG26AV variant).

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

  -------------------- ------------------------------------------------------------ ------------- ------------------------ ------------------ ---------------- ------------------------------------------------
  Device               Make/model                                                   Status        Vendor ID / Product ID   Kernel driver(s)   Kernel version   Notes
  GPU                  Intel Corporation UHD Graphics 620 (Whiskey Lake) (rev 02)   Works         8086:1916                i915               N/A
  Ethernet             Intel Corporation Ethernet Connection (6) I219-V (rev 11)    Works         8086:15be                e1000e             N/A
  Wi-Fi                Intel Corporation Wi-Fi 6 AX200 (rev 1a)                     Works         8086:2723                iwlwifi            N/A              Interface modes other than managed not tested.
  Bluetooth            N/A                                                          Works         N/A                      bt_intel           N/A
  Webcam               Chicony Electronics Co., Ltd HP HD Camera                    Works         04f2:b66a                uvcvideo           N/A
  Fingerprint reader   N/A                                                          Not tested    N/A                      N/A                N/A
  -------------------- ------------------------------------------------------------ ------------- ------------------------ ------------------ ---------------- ------------------------------------------------

### [Accessories]

  -------- ----------------------------------- -------- ------------------------ ------------------ ---------------- -------
  Device   Make/model                          Status   Vendor ID / Product ID   Kernel driver(s)   Kernel version   Notes
  Dock     HP 2013 UltraSlim Docking Station   Works    N/A                      N/A                N/A
  -------- ----------------------------------- -------- ------------------------ ------------------ ---------------- -------

### [Detailed information]

`root `[`#`]`lspci -nn`

    00:00.0 Host bridge [0600]: Intel Corporation Coffee Lake HOST and DRAM Controller [8086:3e34] (rev 0c)
    00:02.0 VGA compatible controller [0300]: Intel Corporation UHD Graphics 620 (Whiskey Lake) [8086:3ea0] (rev 02)
    00:04.0 Signal processing controller [1180]: Intel Corporation Xeon E3-1200 v5/E3-1500 v5/6th Gen Core Processor Thermal Subsystem [8086:1903] (rev 0c)
    00:12.0 Signal processing controller [1180]: Intel Corporation Cannon Point-LP Thermal Controller [8086:9df9] (rev 11)
    00:14.0 USB controller [0c03]: Intel Corporation Cannon Point-LP USB 3.1 xHCI Controller [8086:9ded] (rev 11)
    00:14.2 RAM memory [0500]: Intel Corporation Cannon Point-LP Shared SRAM [8086:9def] (rev 11)
    00:15.0 Serial bus controller [0c80]: Intel Corporation Cannon Point-LP Serial IO I2C Controller #0 [8086:9de8] (rev 11)
    00:15.1 Serial bus controller [0c80]: Intel Corporation Cannon Point-LP Serial IO I2C Controller #1 [8086:9de9] (rev 11)
    00:16.0 Communication controller [0780]: Intel Corporation Cannon Point-LP MEI Controller #1 [8086:9de0] (rev 11)
    00:1c.0 PCI bridge [0604]: Intel Corporation Cannon Point-LP PCI Express Root Port #5 [8086:9dbc] (rev f1)
    00:1c.7 PCI bridge [0604]: Intel Corporation Cannon Point PCI Express Root Port #8 [8086:9dbf] (rev f1)
    00:1d.0 PCI bridge [0604]: Intel Corporation Cannon Point-LP PCI Express Root Port #13 [8086:9db4] (rev f1)
    00:1f.0 ISA bridge [0601]: Intel Corporation Cannon Point-LP LPC Controller [8086:9d84] (rev 11)
    00:1f.3 Multimedia audio controller [0401]: Intel Corporation Cannon Point-LP High Definition Audio Controller [8086:9dc8] (rev 11)
    00:1f.4 SMBus [0c05]: Intel Corporation Cannon Point-LP SMBus Controller [8086:9da3] (rev 11)
    00:1f.5 Serial bus controller [0c80]: Intel Corporation Cannon Point-LP SPI Controller [8086:9da4] (rev 11)
    00:1f.6 Ethernet controller [0200]: Intel Corporation Ethernet Connection (6) I219-V [8086:15be] (rev 11)
    01:00.0 PCI bridge [0604]: Intel Corporation JHL7540 Thunderbolt 3 Bridge [Titan Ridge 2C 2018] [8086:15e7] (rev 06)
    02:00.0 PCI bridge [0604]: Intel Corporation JHL7540 Thunderbolt 3 Bridge [Titan Ridge 2C 2018] [8086:15e7] (rev 06)
    02:01.0 PCI bridge [0604]: Intel Corporation JHL7540 Thunderbolt 3 Bridge [Titan Ridge 2C 2018] [8086:15e7] (rev 06)
    02:02.0 PCI bridge [0604]: Intel Corporation JHL7540 Thunderbolt 3 Bridge [Titan Ridge 2C 2018] [8086:15e7] (rev 06)
    03:00.0 System peripheral [0880]: Intel Corporation JHL7540 Thunderbolt 3 NHI [Titan Ridge 2C 2018] [8086:15e8] (rev 06)
    39:00.0 USB controller [0c03]: Intel Corporation JHL7540 Thunderbolt 3 USB Controller [Titan Ridge 2C 2018] [8086:15e9] (rev 06)
    3a:00.0 Network controller [0280]: Intel Corporation Wi-Fi 6 AX200 [8086:2723] (rev 1a)
    3b:00.0 Non-Volatile memory controller [0108]: Samsung Electronics Co Ltd NVMe SSD Controller SM981/PM981/PM983 [144d:a808]

`root `[`#`]`lsusb`

    Bus 004 Device 001: ID 1d6b:0003 Linux Foundation 3.0 root hub
    Bus 003 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub
    Bus 002 Device 001: ID 1d6b:0003 Linux Foundation 3.0 root hub
    Bus 001 Device 005: ID 04f2:b66a Chicony Electronics Co., Ltd HP HD Camera
    Bus 001 Device 004: ID 06cb:00b7 Synaptics, Inc.
    Bus 001 Device 007: ID 8087:0029 Intel Corp.
    Bus 001 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub

## [Installation]

[FILE] **`/etc/portage/package.use/00input`**

    */* INPUT_DEVICES: libinput synaptics

[FILE] **`/etc/portage/package.use/00video`**

    */* VIDEO_CARDS: -* i965 intel iris

\

### [Firmware]

The wireless card requires [external firmware](https://wiki.gentoo.org/wiki/Iwlwifi "Iwlwifi") ([[[sys-kernel/linux-firmware]](https://packages.gentoo.org/packages/sys-kernel/linux-firmware)[]]):

`root `[`#`]`emerge --ask sys-kernel/linux-firmware`

### [Kernel]

[KERNEL] **NVME block device**

    Device Drivers  --->
           NVME Support  --->
          <*> NVM Express block device

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
             <M>       Intel Wireless WiFi MVM Firmware support

[KERNEL] **Bluetooth device**

    Networking Support  --->
       <*> Bluetooth subsystem support  --->
          <*>   Bluetooth device drivers  --->
             <M>   HCI USB driver  --->

[KERNEL] **Audio device**

    Generic Driver Options  --->
       <*> Sound card support  --->
          <*>   Advanced Linux Sound Architecture  --->
             [*]   PCI sound devices  --->
                   HD-Audio  --->
                      <*> HD Audio PCI
                      <*> Build Realtek HD-audio codec support

[KERNEL] **Webcam**

    Device Drivers  --->
       <*> Multimedia support  --->
                Media Device Types  --->
             [*] Cameras and video grabbers
                Media drivers  -->
             [*] Media USB Adapters  --->
                   <*>   USB Video Class (UVC)