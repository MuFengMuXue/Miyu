[] This article has been flagged for not conforming to the [wiki guidelines](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Guidelines "Gentoo Wiki:Guidelines"). Please [help Gentoo out](https://wiki.gentoo.org/wiki/Help_improve_Gentoo_by_getting_involved_with_documentation!#Make_articles_conform_to_the_guidelines "Help improve Gentoo by getting involved with documentation!") by starting fixing things.

**Resources**

[[]][Official Support Page](https://pcsupport.lenovo.com/us/en/products/laptops-and-netbooks/yoga-series/yoga-7-14arp8)

[[]][Specifications](https://psref.lenovo.com/syspool/Sys/PDF/Yoga/Yoga_7_14ARP8/Yoga_7_14ARP8_Spec.pdf)

[[]][Specifications (by region)](https://psref.lenovo.com/Product/Yoga/Yoga_7_14ARP8?tab=model)

[[]][Hardware Maintenance Manual](https://download.lenovo.com/consumer/mobiles_pub/yoga_7%EF%BC%867i_hmm.pdf)

[[]][User Guide](https://download.lenovo.com/consumer/mobiles_pub/yoga_7_7i_ug_en.pdf)

This article will be talking about the Lenovo Yoga 7 14ARP8 (8th Gen), with the AMD Ryzen 7 7735U Processor, IPS 2,2K screen, SD-card reader, but without the fingerprint sensor. This article is still being written. Some hardware is still being tested and/or being set up.

## [Hardware]

### [Standard]

  ------------- --------------------------------------------------- -------- ------------------------ ------------------ ---------------- ---------------------------------------------------------------------------------------------------------------------
  Device        Make/model                                          Status   Vendor ID / Product ID   Kernel driver(s)   Kernel version   Notes
  CPU           AMD Ryzen 7 7735U                                   Works    N/A                      N/A                6.1.53-r1        Still figuring out performance modes and acpi_call
  Graphics      AMD Radeon 680M (integrated)                        Works    1002:1681                amdgpu             6.1.53-r1        Firmware for the GPU is amdgpu/yellow_carp\_\*.bin
  Speakers      AMD Family 17h/19h HD Audio Controller              Works    1022:15e3                snd_hda_intel      6.1.53-r1        Good volume and clear and good quality
  Wifi          Mediatek MT7922                                     Works    17aa:e0c6                mt7921e            6.1.53-r1        Wasn\'t able to use device in Gentoo LiveCD. Used Arch LiveCD instead
  Bluetooth     \-                                                  Work     \-                       \-                 6.1.53-r1        Refer to [Bluetooth](https://wiki.gentoo.org/wiki/Bluetooth "Bluetooth") Wikipage for setup
  Keyboard      \-                                                  Works    \-                       \-                 6.1.53-r1        Fn+Space works for changing Keyboard backlight. Other function keys need to be mapped or are pre-mapped in some DEs
  Trackpad      Elan                                                Works    \-                       \-                 6.1.53-r1        Works well, multitouch also works
  Touchscreen   Elan                                                Works    \-                       \-                 6.1.53-r1        Works well, including multitouch and pen suport
  Webcam        Luxvisions Innotech Limited Integrated RGB Camera   Works    30c9:00a8                \-                 6.1.53-r1        For setup refer to the wiki entry on [Webcams](https://wiki.gentoo.org/wiki/Webcam "Webcam")
  ------------- --------------------------------------------------- -------- ------------------------ ------------------ ---------------- ---------------------------------------------------------------------------------------------------------------------

`root `[`#`]`lspci -nnk`

    00:00.0 Host bridge [0600]: Advanced Micro Devices, Inc. [AMD] Family 17h-19h PCIe Root Complex [1022:14b5] (rev 01)
        Subsystem: Lenovo Family 17h-19h PCIe Root Complex [17aa:3818]
    00:00.2 IOMMU [0806]: Advanced Micro Devices, Inc. [AMD] Family 17h-19h IOMMU [1022:14b6]
        Subsystem: Lenovo Family 17h-19h IOMMU [17aa:3815]
    00:01.0 Host bridge [0600]: Advanced Micro Devices, Inc. [AMD] Family 17h-19h PCIe Dummy Host Bridge [1022:14b7] (rev 01)
    00:02.0 Host bridge [0600]: Advanced Micro Devices, Inc. [AMD] Family 17h-19h PCIe Dummy Host Bridge [1022:14b7] (rev 01)
    00:02.2 PCI bridge [0604]: Advanced Micro Devices, Inc. [AMD] Family 17h-19h PCIe GPP Bridge [1022:14ba]
        Subsystem: Advanced Micro Devices, Inc. [AMD] Family 17h-19h PCIe GPP Bridge [1022:1453]
        Kernel driver in use: pcieport
    00:02.3 PCI bridge [0604]: Advanced Micro Devices, Inc. [AMD] Family 17h-19h PCIe GPP Bridge [1022:14ba]
        Subsystem: Advanced Micro Devices, Inc. [AMD] Family 17h-19h PCIe GPP Bridge [1022:1453]
        Kernel driver in use: pcieport
    00:02.4 PCI bridge [0604]: Advanced Micro Devices, Inc. [AMD] Family 17h-19h PCIe GPP Bridge [1022:14ba]
        Subsystem: Advanced Micro Devices, Inc. [AMD] Family 17h-19h PCIe GPP Bridge [1022:1453]
        Kernel driver in use: pcieport
    00:03.0 Host bridge [0600]: Advanced Micro Devices, Inc. [AMD] Family 17h-19h PCIe Dummy Host Bridge [1022:14b7] (rev 01)
    00:03.1 PCI bridge [0604]: Advanced Micro Devices, Inc. [AMD] Family 19h USB4/Thunderbolt PCIe tunnel [1022:14cd]
        Subsystem: Advanced Micro Devices, Inc. [AMD] Family 19h USB4/Thunderbolt PCIe tunnel [1022:1453]
        Kernel driver in use: pcieport
    00:04.0 Host bridge [0600]: Advanced Micro Devices, Inc. [AMD] Family 17h-19h PCIe Dummy Host Bridge [1022:14b7] (rev 01)
    00:08.0 Host bridge [0600]: Advanced Micro Devices, Inc. [AMD] Family 17h-19h PCIe Dummy Host Bridge [1022:14b7] (rev 01)
    00:08.1 PCI bridge [0604]: Advanced Micro Devices, Inc. [AMD] Family 17h-19h Internal PCIe GPP Bridge [1022:14b9] (rev 10)
        Subsystem: Advanced Micro Devices, Inc. [AMD] Family 17h-19h Internal PCIe GPP Bridge [1022:14b9]
        Kernel driver in use: pcieport
    00:08.3 PCI bridge [0604]: Advanced Micro Devices, Inc. [AMD] Family 17h-19h Internal PCIe GPP Bridge [1022:14b9] (rev 10)
        Subsystem: Advanced Micro Devices, Inc. [AMD] Family 17h-19h Internal PCIe GPP Bridge [1022:14b9]
        Kernel driver in use: pcieport
    00:14.0 SMBus [0c05]: Advanced Micro Devices, Inc. [AMD] FCH SMBus Controller [1022:790b] (rev 71)
        Subsystem: Lenovo FCH SMBus Controller [17aa:3880]
        Kernel driver in use: piix4_smbus
    00:14.3 ISA bridge [0601]: Advanced Micro Devices, Inc. [AMD] FCH LPC Bridge [1022:790e] (rev 51)
        Subsystem: Advanced Micro Devices, Inc. [AMD] FCH LPC Bridge [1022:790e]
    00:18.0 Host bridge [0600]: Advanced Micro Devices, Inc. [AMD] Rembrandt Data Fabric: Device 18h; Function 0 [1022:1679]
    00:18.1 Host bridge [0600]: Advanced Micro Devices, Inc. [AMD] Rembrandt Data Fabric: Device 18h; Function 1 [1022:167a]
    00:18.2 Host bridge [0600]: Advanced Micro Devices, Inc. [AMD] Rembrandt Data Fabric: Device 18h; Function 2 [1022:167b]
    00:18.3 Host bridge [0600]: Advanced Micro Devices, Inc. [AMD] Rembrandt Data Fabric: Device 18h; Function 3 [1022:167c]
        Kernel driver in use: k10temp
    00:18.4 Host bridge [0600]: Advanced Micro Devices, Inc. [AMD] Rembrandt Data Fabric: Device 18h; Function 4 [1022:167d]
    00:18.5 Host bridge [0600]: Advanced Micro Devices, Inc. [AMD] Rembrandt Data Fabric: Device 18h; Function 5 [1022:167e]
    00:18.6 Host bridge [0600]: Advanced Micro Devices, Inc. [AMD] Rembrandt Data Fabric: Device 18h; Function 6 [1022:167f]
    00:18.7 Host bridge [0600]: Advanced Micro Devices, Inc. [AMD] Rembrandt Data Fabric: Device 18h; Function 7 [1022:1680]
    01:00.0 Network controller [0280]: MEDIATEK Corp. MT7922 802.11ax PCI Express Wireless Network Adapter [14c3:0616]
        Subsystem: Lenovo MT7922 802.11ax PCI Express Wireless Network Adapter [17aa:e0c6]
        Kernel driver in use: mt7921e
    02:00.0 Unassigned class [ff00]: Realtek Semiconductor Co., Ltd. RTS522A PCI Express Card Reader [10ec:522a] (rev 01)
        Subsystem: Realtek Semiconductor Co., Ltd. RTS522A PCI Express Card Reader [10ec:522a]
        Kernel driver in use: rtsx_pci
    03:00.0 Non-Volatile memory controller [0108]: Sandisk Corp WD PC SN740 NVMe SSD 512GB (DRAM-less) [15b7:5016] (rev 01)
        DeviceName: Realtek
        Subsystem: Sandisk Corp WD PC SN740 NVMe SSD 512GB (DRAM-less) [15b7:5016]
        Kernel driver in use: nvme
    73:00.0 VGA compatible controller [0300]: Advanced Micro Devices, Inc. [AMD/ATI] Rembrandt [Radeon 680M] [1002:1681] (rev 08)
        Subsystem: Lenovo Rembrandt [Radeon 680M] [17aa:381d]
        Kernel driver in use: amdgpu
    73:00.1 Audio device [0403]: Advanced Micro Devices, Inc. [AMD/ATI] Rembrandt Radeon High Definition Audio Controller [1002:1640]
        Subsystem: Lenovo Rembrandt Radeon High Definition Audio Controller [17aa:3819]
        Kernel driver in use: snd_hda_intel
    73:00.2 Encryption controller [1080]: Advanced Micro Devices, Inc. [AMD] VanGogh PSP/CCP [1022:1649]
        Subsystem: Lenovo VanGogh PSP/CCP [17aa:3831]
        Kernel driver in use: ccp
    73:00.3 USB controller [0c03]: Advanced Micro Devices, Inc. [AMD] Rembrandt USB4 XHCI controller #3 [1022:161d]
        Subsystem: Advanced Micro Devices, Inc. [AMD] Rembrandt USB4 XHCI controller [1022:161d]
        Kernel driver in use: xhci_hcd
    73:00.4 USB controller [0c03]: Advanced Micro Devices, Inc. [AMD] Rembrandt USB4 XHCI controller #4 [1022:161e]
        Subsystem: Advanced Micro Devices, Inc. [AMD] Rembrandt USB4 XHCI controller [1022:161e]
        Kernel driver in use: xhci_hcd
    73:00.5 Multimedia controller [0480]: Advanced Micro Devices, Inc. [AMD] ACP/ACP3X/ACP6x Audio Coprocessor [1022:15e2] (rev 60)
        Subsystem: Lenovo ACP/ACP3X/ACP6x Audio Coprocessor [17aa:386a]
        Kernel driver in use: snd_pci_acp6x
    73:00.6 Audio device [0403]: Advanced Micro Devices, Inc. [AMD] Family 17h/19h HD Audio Controller [1022:15e3]
        Subsystem: Lenovo Family 17h/19h HD Audio Controller [17aa:3866]
        Kernel driver in use: snd_hda_intel
    73:00.7 Signal processing controller [1180]: Advanced Micro Devices, Inc. [AMD] Sensor Fusion Hub [1022:15e4]
        Subsystem: Advanced Micro Devices, Inc. [AMD] Sensor Fusion Hub [1022:15e4]
        Kernel driver in use: pcie_mp2_amd
    74:00.0 USB controller [0c03]: Advanced Micro Devices, Inc. [AMD] Rembrandt USB4 XHCI controller #8 [1022:161f]
        Subsystem: Advanced Micro Devices, Inc. [AMD] Rembrandt USB4 XHCI controller [1022:161f]
        Kernel driver in use: xhci_hcd
    74:00.3 USB controller [0c03]: Advanced Micro Devices, Inc. [AMD] Rembrandt USB4 XHCI controller #5 [1022:15d6]
        Subsystem: Advanced Micro Devices, Inc. [AMD] Rembrandt USB4 XHCI controller [1022:15d6]
        Kernel driver in use: xhci_hcd
    74:00.4 USB controller [0c03]: Advanced Micro Devices, Inc. [AMD] Rembrandt USB4 XHCI controller #6 [1022:15d7]
        Subsystem: Advanced Micro Devices, Inc. [AMD] Rembrandt USB4 XHCI controller [1022:15d7]
        Kernel driver in use: xhci_hcd
    74:00.5 USB controller [0c03]: Advanced Micro Devices, Inc. [AMD] Rembrandt USB4/Thunderbolt NHI controller #1 [1022:162e]
        Subsystem: Advanced Micro Devices, Inc. [AMD] Rembrandt USB4/Thunderbolt NHI controller [1022:162e]
        Kernel driver in use: thunderbolt

### [Accessories]

  ------------ -------------------- -------- -------- ------------------ ---------------- ------------------------------------------------------
  Device       Make/model           Status   Bus ID   Kernel driver(s)   Kernel version   Notes
  Stylus Pen   Lenovo Digital Pen   Works    N/A      N/A                6.1.53-r1        Buttons on pen working. Pressure sensor in pen works
  ------------ -------------------- -------- -------- ------------------ ---------------- ------------------------------------------------------