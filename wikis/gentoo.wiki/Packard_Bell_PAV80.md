**Resources**

[[]][DOT SE (German)](https://web.archive.org/web/20110904013355/http://www.packardbell.de/pb/de/DE/content/serie/dotse)

[[]][DOT SE (Russian)](https://web.archive.org/web/20130625004820/http://www.packardbell.com:80/pb/ru/RU/content/productgroup/netbooks)

[[]][DOT SE (Turkish)](https://web.archive.org/web/20160628163735/http://www.packardbell.com/pb/tr/TR/content/serie/dotse)

## Contents

-   [[1] [Hardware status]](#Hardware_status)
-   [[2] [Hardware]](#Hardware)
    -   [[2.1] [PCI]](#PCI)
    -   [[2.2] [USB]](#USB)
    -   [[2.3] [CPU]](#CPU)
-   [[3] [Mainboard and processor]](#Mainboard_and_processor)
-   [[4] [Ethernet]](#Ethernet)
-   [[5] [Card reader]](#Card_reader)
-   [[6] [Webcam]](#Webcam)

## [Hardware status]

  --------------------- ------------- ------------------
         Device             Works           Notes
      Atom CPU N550          Yes       Tested in 32-bit
   Integrated Graphics       Yes
        Intel HDA            Yes
        Ethernet             Yes
        Wireless             Yes
        Bluetooth        Not tested
         Camera          Not tested
       Card Reader           Yes
  --------------------- ------------- ------------------

## [Hardware]

### [PCI]

`root `[`#`]`lspci`

    00:00.0 Host bridge: Intel Corporation Atom Processor D4xx/D5xx/N4xx/N5xx DMI Bridge (rev 02)
    00:02.0 VGA compatible controller: Intel Corporation Atom Processor D4xx/D5xx/N4xx/N5xx Integrated Graphics Controller (rev 02)
    00:02.1 Display controller: Intel Corporation Atom Processor D4xx/D5xx/N4xx/N5xx Integrated Graphics Controller (rev 02)
    00:1b.0 Audio device: Intel Corporation NM10/ICH7 Family High Definition Audio Controller (rev 02)
    00:1c.0 PCI bridge: Intel Corporation NM10/ICH7 Family PCI Express Port 1 (rev 02)
    00:1c.1 PCI bridge: Intel Corporation NM10/ICH7 Family PCI Express Port 2 (rev 02)
    00:1d.0 USB controller: Intel Corporation NM10/ICH7 Family USB UHCI Controller #1 (rev 02)
    00:1d.1 USB controller: Intel Corporation NM10/ICH7 Family USB UHCI Controller #2 (rev 02)
    00:1d.2 USB controller: Intel Corporation NM10/ICH7 Family USB UHCI Controller #3 (rev 02)
    00:1d.3 USB controller: Intel Corporation NM10/ICH7 Family USB UHCI Controller #4 (rev 02)
    00:1d.7 USB controller: Intel Corporation NM10/ICH7 Family USB2 EHCI Controller (rev 02)
    00:1e.0 PCI bridge: Intel Corporation 82801 Mobile PCI Bridge (rev e2)
    00:1f.0 ISA bridge: Intel Corporation NM10 Family LPC Controller (rev 02)
    00:1f.2 SATA controller: Intel Corporation NM10/ICH7 Family SATA Controller [AHCI mode] (rev 02)
    00:1f.3 SMBus: Intel Corporation NM10/ICH7 Family SMBus Controller (rev 02)
    01:00.0 Ethernet controller: Qualcomm Atheros AR8152 v1.1 Fast Ethernet (rev c1)
    02:00.0 Network controller: Qualcomm Atheros AR9285 Wireless Network Adapter (PCI-Express) (rev 01)

### [USB]

`root `[`#`]`lsusb`

    Bus 001 Device 006: ID 0cf2:6250 ENE Technology, Inc. SD card reader (UB6250)
    Bus 001 Device 003: ID 0402:9665 ALi Corp. Gateway Webcam
    Bus 001 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub
    Bus 005 Device 001: ID 1d6b:0001 Linux Foundation 1.1 root hub
    Bus 004 Device 001: ID 1d6b:0001 Linux Foundation 1.1 root hub
    Bus 003 Device 001: ID 1d6b:0001 Linux Foundation 1.1 root hub
    Bus 002 Device 001: ID 1d6b:0001 Linux Foundation 1.1 root hub

### [CPU]

`root `[`#`]`lscpu`

    Architectuur:          i686
    CPU-modus(sen):        32-bit, 64-bit
    Bytevolgorde:          Little Endian
    CPU('s):               4
    Online CPU('s)-lijst:  0-3
    Draden per kern:       2
    Kern(en) per voet:     2
    CPU-voet(en):          1
    Producent-ID:          GenuineIntel
    CPU-familie:           6
    Model:                 28
    Modelnaam:             Intel(R) Atom(TM) CPU N550   @ 1.50GHz
    Stepping:              10
    CPU-frequentie (MHz):  1500.000
    max. CPU-frequentie (MHz):1500,0000
    min. CPU-frequentie (MHz):1000,0000
    BogoMIPS:              2992.81
    L1d-cache:             24K
    L1i-cache:             32K
    L2-cache:              512K
    lscpu

## [Mainboard and processor]

[FILE] **`/etc/portage/make.conf`**

    CHOST="i686-pc-linux-gnu"
    CFLAGS="-march=atom -O2 -fomit-frame-pointer -pipe"
    CXXFLAGS="$"
    MAKEOPTS="-j5"

**Kernel**

[KERNEL] **Intel Atom**

    Processor type and futures --->
     Processor family (Intel Atom)
     [*] Machine Check / overheating reporting
     [*]    Intel MCE features

    Bus options --->
     [*] CPI support
     [*]    CPI Express Port Bus support
     [*] ISA support

    Device Drivers -->
      Hardware monitoring support -->
      [*] Intel Core/Core2/Atom temperature sensor

## [Ethernet]

**Kernel**

[KERNEL] **Qualcomm Atheros AR8152 v1.1 Fast Ethernet (rev c1)**

    [*] Networking support --->

    Device Drivers --->
     [*] Network device support --->
      [*] Ethernet driver support --->
       [*] Atheros devices
        <M>  Atheros L1C Gigabit Ethernet support

## [Card reader]

**Kernel**

[KERNEL] **Card reader**

    Device Drivers --->
     <*> MMC/SD/SDIO card support --->
      <*> MMC block device driver
     USB Support --->
      <*> USB ENE card reader support

## [Webcam]

**Kernel**

[KERNEL] **Webcam**

    Device Drivers --->
     <*> Multimedia support --->
      <*> Cameras/video grabbers support
      [*] Media USB Adapters --->
       <M> USB Video Class (UVC)
        [*] UVC input events device support
       <*> GSPCA based webcams --->
        <M> ALI USB m5602 Camera Driver