## Contents

-   [[1] [General Information]](#General_Information)
    -   [[1.1] [Technical specifications]](#Technical_specifications)
-   [[2] [Kernel Configuration]](#Kernel_Configuration)
    -   [[2.1] [SATA]](#SATA)
    -   [[2.2] [Sound]](#Sound)
    -   [[2.3] [USB]](#USB)
    -   [[2.4] [Network]](#Network)
-   [[3] [Appendices]](#Appendices)
    -   [[3.1] [Lspci Output]](#Lspci_Output)
    -   [[3.2] [Disclaimer]](#Disclaimer)

## [General Information]

The Asus P5N32-E SLI Plus is a motherboard with an Intel LGA775 socket, compatible with 45nm multi-core CPUS.

[Official Asus Page](http://www.asus.com/Product.aspx?P_ID=kveVJLd8DpPGYsNj)

### [Technical specifications]

  -------------------- --------------------------------------------------------------------------
  CPU-socket           Intel LGA775
  Front Side Bus       1333/1066/800/533/ MHz
  Memory               4 x DIMM, Max. 8 GB, DDR2 800/667/533
  Northbridge          C55 a.k.a. nForce®650i SLI
  Expansion Slots      2 x PCIe x16 slot (SLI) + 2 x PCI 2.2 + 1 x PCI Express x16, at x8 speed
  Southbridge          MCP55P a.k.a. nForce®570 SLI
  Storage              1 xUltraDMA + 6 xSATA 3 Gb/s
  Integrated NIC       Dual Gigabit/ MAC with external Marvell PHY Support
  Integrated Audio     ADI 1988B 8 -Channel
  USB                  10 USB 2.0 ports (6 ports at mid-board, 4 ports at back panel)
  IEE1394 (Firewire)   VIA6308P controller supports 2 x 1394a ports
  -------------------- --------------------------------------------------------------------------

## [Kernel Configuration]

### [SATA]

Select \"NVIDIA SATA support\" module.

[KERNEL] **SATA on P5N32-E SLI Plus**

    Device Drivers --->
      Serial ATA (prod) and Parallel ATA (experimental) drivers  --->
       <*>   ATA SFF support
        <*>   NVIDIA SATA support

### [Sound]

The soundchip works with the snd-hda-intel sound module. The corresponding kernel options are:

[KERNEL] **Soundchip on P5N32-E SLI Plus**

    Device Drivers --->
      Sound --->
       Advanced Linux Sound Architecture --->
        PCI sound devices --->
         <*> Intel HD Audio
          <*> Build Analog Device HD-audio codec support

### [USB]

[KERNEL] **USB on P5N32-E SLI Plus**

    Device Drivers --->
      USB support --->
       <*> EHCI HCD (USB 2.0) support
       <*> OHCI HCD support

### [Network]

The NIC is a NVIDIA Dual Gigabit MAC with external Marvell PHY.

[KERNEL] **NIC on P5N32-E SLI Plus**

    Device Drivers --->
      [*] Network device support --->
       [*] Ethernet (10 or 100Mbit)  --->
        <*> nForce Ethernet support
         [*] Use Rx Polling
       <*> PHY Device support and infrastructure  --->
        <*>   Drivers for Marvell PHYs

## [Appendices]

### [Lspci Output]

[CODE] **lspci**

    00:00.0 Host bridge: nVidia Corporation C55 Host Bridge (rev a2)
    00:03.0 PCI bridge: nVidia Corporation C55 PCI Express bridge (rev a1)
    00:0a.0 ISA bridge: nVidia Corporation MCP55 LPC Bridge (rev a2)
    00:0a.1 SMBus: nVidia Corporation MCP55 SMBus (rev a2)
    00:0b.0 USB Controller: nVidia Corporation MCP55 USB Controller (rev a1)
    00:0b.1 USB Controller: nVidia Corporation MCP55 USB Controller (rev a2)
    00:0d.0 IDE interface: nVidia Corporation MCP55 IDE (rev a1)
    00:0e.0 IDE interface: nVidia Corporation MCP55 SATA Controller (rev a2)
    00:0e.1 IDE interface: nVidia Corporation MCP55 SATA Controller (rev a2)
    00:0e.2 IDE interface: nVidia Corporation MCP55 SATA Controller (rev a2)
    00:0f.0 PCI bridge: nVidia Corporation MCP55 PCI bridge (rev a2)
    00:0f.1 Audio device: nVidia Corporation MCP55 High Definition Audio (rev a2)
    00:11.0 Bridge: nVidia Corporation MCP55 Ethernet (rev a2)
    00:12.0 Bridge: nVidia Corporation MCP55 Ethernet (rev a2)
    02:0b.0 FireWire (IEEE 1394): VIA Technologies, Inc. VT6306 Fire II IEEE 1394 OHCI Link Layer
            Controller (rev c0)

### [Disclaimer]

Everything been tested working on

[CODE] **uname -a**

    2.6.28-gentoo-r3 #2 SMP PREEMPT Wed Mar 18 15:45:13 IST 2009
    x86_64 Intel(R) Core(TM)2 Quad CPU Q6600 @ 2.40GHz GenuineIntel GNU/Linux