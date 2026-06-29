[] The information in this article is probably **outdated**. You can help the Gentoo community by verifying and [updating this article](https://wiki.gentoo.org/index.php?title=Lenovo_IdeaPad_Y500&action=edit).

**Resources**

[[]][Official Support Page](https://pcsupport.lenovo.com/us/en/products/laptops-and-netbooks/ideapad-y-series-laptops/ideapad-y500-notebook)

[[]][Hardware Maintenance Manual](https://download.lenovo.com/consumer/mobiles_pub/lenovo_y400_y500_hmm.pdf)

[[]][User Guide](https://download.lenovo.com/consumer/mobiles_pub/ideapad_y400y500_ug_v1.0_july_2012_english.pdf)

[[]][IdeaPad Y series](https://en.wikipedia.org/wiki/IdeaPad_Y_series#Y500 "wikipedia:IdeaPad Y series")

The **Lenovo IdeaPad Y500** is a modular laptop with the ability to replace the CD-ROM drive with an SSD/HDD/GPU. The hardware is supported by Linux very well.

## Contents

-   [[1] [Hardware]](#Hardware)
    -   [[1.1] [Standard]](#Standard)
-   [[2] [Installation]](#Installation)
    -   [[2.1] [Kernel]](#Kernel)
    -   [[2.2] [Emerge]](#Emerge)
-   [[3] [Configuration]](#Configuration)
    -   [[3.1] [Xorg]](#Xorg)
        -   [[3.1.1] [Touchpad]](#Touchpad)

## [Hardware]

### [Standard]

** Tip**\
The CD-ROM drive can be easily replaced with an additional SSD/HDD/GPU.

  ---------------- ---------------------------------------------------------------------------------------- -------- ------------------------ ------------------ ---------------- -------
  Device           Make/model                                                                               Status   Vendor ID / Product ID   Kernel driver(s)   Kernel version   Notes
  CPU              Intel® Core™ i7-3630QM                                                                   Works    N/A                      N/A                3.11
  GPU              NVIDIA Corporation GK107M \[GeForce GT 650M / GTX 660M LE\]                              Works    10de:0fd1                N/A                3.11
  SSD              SanDisk® U100 SSD                                                                        Works    N/A                      N/A                3.11
  HDD              Seagate ST1000LM024                                                                      Works    N/A                      N/A                3.11
  Sound            Intel Corporation 7 Series/C210 Series Chipset Family High Definition Audio Controller   Works    8086:1e20                N/A                3.11
  Ethernet         Qualcomm Atheros AR8161 Gigabit Ethernet                                                 Works    1969:1091                N/A                3.11
  Wi-Fi            Intel® Centrino® Wireless-N 2230                                                         Works    N/A                      N/A                3.11
  SD Card Reader   JMicron Technology Corp. Standard SD Host Controller                                     Works    197b:2391                N/A                3.11
  Touchpad         N/A                                                                                      Works    N/A                      N/A                3.11
  CD-ROM drive     N/A                                                                                      Works    N/A                      N/A                3.11
  Webcam           N/A                                                                                      Works    N/A                      N/A                3.11
  ---------------- ---------------------------------------------------------------------------------------- -------- ------------------------ ------------------ ---------------- -------

`root `[`#`]`lspci -nn`

    00:00.0 Host bridge [0600]: Intel Corporation 3rd Gen Core processor DRAM Controller [8086:0154] (rev 09)
    00:01.0 PCI bridge [0604]: Intel Corporation Xeon E3-1200 v2/3rd Gen Core processor PCI Express Root Port [8086:0151] (rev 09)
    00:14.0 USB controller [0c03]: Intel Corporation 7 Series/C210 Series Chipset Family USB xHCI Host Controller [8086:1e31] (rev 04)
    00:16.0 Communication controller [0780]: Intel Corporation 7 Series/C210 Series Chipset Family MEI Controller #1 [8086:1e3a] (rev 04)
    00:1a.0 USB controller [0c03]: Intel Corporation 7 Series/C210 Series Chipset Family USB Enhanced Host Controller #2 [8086:1e2d] (rev 04)
    00:1b.0 Audio device [0403]: Intel Corporation 7 Series/C210 Series Chipset Family High Definition Audio Controller [8086:1e20] (rev 04)
    00:1c.0 PCI bridge [0604]: Intel Corporation 7 Series/C210 Series Chipset Family PCI Express Root Port 1 [8086:1e10] (rev c4)
    00:1c.1 PCI bridge [0604]: Intel Corporation 7 Series/C210 Series Chipset Family PCI Express Root Port 2 [8086:1e12] (rev c4)
    00:1c.3 PCI bridge [0604]: Intel Corporation 7 Series/C210 Series Chipset Family PCI Express Root Port 4 [8086:1e16] (rev c4)
    00:1d.0 USB controller [0c03]: Intel Corporation 7 Series/C210 Series Chipset Family USB Enhanced Host Controller #1 [8086:1e26] (rev 04)
    00:1f.0 ISA bridge [0601]: Intel Corporation HM76 Express Chipset LPC Controller [8086:1e59] (rev 04)
    00:1f.2 SATA controller [0106]: Intel Corporation 7 Series Chipset Family 6-port SATA Controller [AHCI mode] [8086:1e03] (rev 04)
    00:1f.3 SMBus [0c05]: Intel Corporation 7 Series/C210 Series Chipset Family SMBus Controller [8086:1e22] (rev 04)
    01:00.0 VGA compatible controller [0300]: NVIDIA Corporation GK107M [GeForce GT 650M / GTX 660M LE] [10de:0fd1] (rev a1)
    01:00.1 Audio device [0403]: NVIDIA Corporation GK107 HDMI Audio Controller [10de:0e1b] (rev a1)
    02:00.0 Ethernet controller [0200]: Qualcomm Atheros AR8161 Gigabit Ethernet [1969:1091] (rev 10)
    03:00.0 Network controller [0280]: Intel Corporation Centrino Ultimate-N 6300 [8086:4238] (rev 3e)
    04:00.0 System peripheral [0880]: JMicron Technology Corp. SD/MMC Host Controller [197b:2392] (rev 30)
    04:00.2 SD Host controller [0805]: JMicron Technology Corp. Standard SD Host Controller [197b:2391] (rev 30)
    04:00.3 System peripheral [0880]: JMicron Technology Corp. MS Host Controller [197b:2393] (rev 30)
    04:00.4 System peripheral [0880]: JMicron Technology Corp. xD Host Controller [197b:2394] (rev 30)

`root `[`#`]`lsusb`

    Bus 001 Device 002: ID 8087:0024 Intel Corp. Integrated Rate Matching Hub
    Bus 002 Device 002: ID 8087:0024 Intel Corp. Integrated Rate Matching Hub
    Bus 004 Device 002: ID 5986:0525 Acer, Inc
    Bus 001 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub
    Bus 002 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub
    Bus 003 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub
    Bus 004 Device 001: ID 1d6b:0003 Linux Foundation 3.0 root hub
    Bus 001 Device 003: ID 046d:c044 Logitech, Inc. LX3 Optical Mouse

## [Installation]

### [Kernel]

[KERNEL] **Ethernet (kernel version 3.11)**

    --- Ethernet driver support
           [*]   Atheros devices
           < >     Atheros L2 Fast Ethernet support
           < >     Atheros/Attansic L1 Gigabit Ethernet support
           < >     Atheros L1E Gigabit Ethernet support
           < >     Atheros L1C Gigabit Ethernet support
           <M>     Qualcomm Atheros AR816x/AR817x support
           [ ]   Broadcom devices

[KERNEL] **Webcam (kernel version 3.11)**

    -> Device Drivers
             -> Multimedia support
               -> Media USB Adapters
          *** Webcam devices ***
    <M>   USB Video Class (UVC)
    [*]     UVC input events device support

### [Emerge]

[FILE] **`/etc/portage/package.use/00input`**

    */* INPUT_DEVICES: synaptics evdev

[FILE] **`/etc/portage/package.use/00video`**

    */* VIDEO_CARDS: -* nvidia

## [Configuration]

### [Xorg]

#### [Touchpad]

** Tip**\
If the touchpad is too slow/fast, change the speed parameters.

[FILE] **`/etc/X11/xorg.conf.d/50-touchpad.conf`**

    Section "InputClass"
            Identifier "touchpad"
            MatchProduct "SynPS/2 Synaptics TouchPad"
            Driver "synaptics"
            # tweak the X-server pointer acceleration
            Option "AccelerationProfile" "2"
            Option "AdaptiveDeceleration" "16"
            Option "ConstantDeceleration" "16"
            Option "VelocityScale" "32"
    EndSection