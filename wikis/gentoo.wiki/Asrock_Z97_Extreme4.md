**Resources**

[[]][Home](https://www.asrock.com/mb/Intel/Z97%20Extreme4)

## Contents

-   [[1] [General Information]](#General_Information)
    -   [[1.1] [Technical specifications]](#Technical_specifications)
-   [[2] [Kernel Configuration]](#Kernel_Configuration)
    -   [[2.1] [Sata]](#Sata)
    -   [[2.2] [Sound]](#Sound)
    -   [[2.3] [USB]](#USB)
    -   [[2.4] [Network]](#Network)
    -   [[2.5] [Intel MEI]](#Intel_MEI)
    -   [[2.6] [Sensor]](#Sensor)
    -   [[2.7] [PCI Express]](#PCI_Express)
    -   [[2.8] [SMBus]](#SMBus)
    -   [[2.9] [Warning]](#Warning)

## [General Information]

Asrock Z97 Extreme4 is a motherboard with an Intel LGA1150 socket and Intel Z97 Express Chipset.

### [Technical specifications]

  ------------------ ------------------------------------------------------------------------------------------------------------------------------------
  CPU-socket         Intel LGA1150
  Chipset            Z97
  Memory             4 x DIMM, Max. 32 GB, DDR3/DDR3L 3200+(OC)/2933(OC)/2800(OC)/2400(OC)/2133(OC)/1866(OC)/1600/1333/1066 non-ECC, un-buffered memory
  Expansion Slots    3 x PCIe 3.0 x16 slot + 3 x PCIe 2.0 x1
  Storage            6 xSATA 6 Gb/s - RAID 0, RAID 1, RAID 5, RAID 10 + 2 x SATA3 6.0 Gb/s Connectors by ASMedia ASM1061
  Integrated NIC     Giga PHY Intel® I218V Gigabit LAN 10/100/1000 Mb/s
  Integrated Audio   Realtek ALC1150
  USB                4 x USB 3.0 Ports (Intel® Z97) 2 x USB 2.0 Ports 2 x USB 2.0 Ports (ASMedia ASM1042AE)
  ------------------ ------------------------------------------------------------------------------------------------------------------------------------

## [Kernel Configuration]

### [Sata]

Select \"AHCI SATA support\" module.

[KERNEL] **SATA on Asrock Z97 Extreme4**

    Device Drivers --->
      Serial ATA and Parallel ATA drivers (libata)  --->
       [*]   ATA ACPI Support
       <*>   AHCI SATA support
       <*>   Platform AHCI SATA support

### [Sound]

[KERNEL] **Sound on Asrock Z97 Extreme4**

    Device Drivers --->
     <*> Sound card support  --->
      <*> Advanced Linux Sound Architecture --->
       <*> PCI sound devices --->
         HD-Audio  --->
         <*> Build Realtek HD-audio codec support

### [USB]

[KERNEL] **USB on Asrock Z97 Extreme4**

    Device Drivers --->
      USB support --->
       <*> xHCI HCD (USB 3.0) support
       <*> EHCI HCD (USB 2.0) support

### [Network]

[KERNEL] **NIC on Asrock Z97 Extreme**

    Device Drivers --->
      [*] Network device support --->
       [*]   Ethernet driver support  --->
        [*]   Intel devices
         <M>     Intel(R) PRO/1000 PCI-Express Gigabit Ethernet support

### [Intel MEI]

[KERNEL] **MEI on Asrock Z97 Extreme**

    Device Drivers --->
      Misc devices  --->
        Intel Management Engine Interface
         <M> ME Enabled Intel Chipsets

### [Sensor]

[KERNEL] **Sensor on Asrock Z97 Extreme**

    Device Drivers --->
      <*> Hardware Monitoring support  --->
       <M>   Nuvoton NCT6775F and compatibles

### [PCI Express]

[KERNEL] **PCI Express on Asrock Z97 Extreme**

    Bus options (PCI etc.)  --->
      [*] PCI support
       [*] Support mmconfig PCI config space access
        [*] PCI Express Port Bus support

### [SMBus]

[KERNEL] **SMBus on Asrock Z97 Extreme**

    Device Drivers --->
      I2C support  --->
       <*> I2C support
        [*] ACPI I2C Operation region support
        [*] Enable compatibility bits for old user-space
        <M> I2C device interface
        [*] Autoselect pertinent helper modules
        [*] I2C slave support
         I2C Hardware Bus support  --->
          <M> Intel 82801 (ICH/PCH)

### [Warning]

All tested and working very well.

`user `[`$`]`uname -mvrpo`

    4.0.5-gentoo #4 SMP PREEMPT Thu Jun 11 11:40:18 GMT 2015 x86_64 Intel(R) Core(TM) i7-4790K CPU @ 4.00GHz GNU/Linux