[] The information in this article is probably **outdated**. You can help the Gentoo community by verifying and [updating this article](https://wiki.gentoo.org/index.php?title=Lenovo_G400&action=edit).

[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=Lenovo_G400&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

**Resources**

[[]][Home](https://pcsupport.lenovo.com/us/en/products/laptops-and-netbooks/lenovo-g-series-laptops/lenovo-g400-notebook/)

[[]][Specifications](https://download.lenovo.com/consumer/mobiles_pub/lenovo_g400g500g405g505g410g510_hmm.pdf#G4.1006019)

[[]][Specifications (parts)](https://download.lenovo.com/consumer/mobiles_pub/lenovo_g400g500g405g505g410g510_hmm.pdf#G4.1013683)

[[]][Hardware Maintenance Manual](https://download.lenovo.com/consumer/mobiles_pub/lenovo_g400g500g405g505g410g510_hmm.pdf)

[[]][User Guide](https://download.lenovo.com/consumer/mobiles_pub/lenovo_g400g500g405g505g410g510_ug_english.pdf)

## Contents

-   [[1] [Hardware]](#Hardware)
    -   [[1.1] [Standard]](#Standard)
-   [[2] [Installation]](#Installation)
    -   [[2.1] [Kernel]](#Kernel)
        -   [[2.1.1] [GPU]](#GPU)
        -   [[2.1.2] [Sound]](#Sound)
        -   [[2.1.3] [Ethernet]](#Ethernet)
        -   [[2.1.4] [Wi-Fi]](#Wi-Fi)
        -   [[2.1.5] [Bluetooth]](#Bluetooth)
        -   [[2.1.6] [Fn-keys]](#Fn-keys)
        -   [[2.1.7] [Webcam]](#Webcam)
        -   [[2.1.8] [SD card reader]](#SD_card_reader)
        -   [[2.1.9] [Watchdog]](#Watchdog)
        -   [[2.1.10] [Random number generator]](#Random_number_generator)

## [Hardware]

### [Standard]

  ---------------- ------------------- -------- ------------------------ ------------------ ---------------- -------
  Device           Make/model          Status   Vendor ID / Product ID   Kernel driver(s)   Kernel version   Notes
  CPU              N/A                 Works    N/A                      N/A                N/A
  GPU              N/A                 Works    N/A                      N/A                N/A
  Ethernet         N/A                 Works    N/A                      N/A                N/A
  Wi-Fi            Broadcom BCM43142   Works    N/A                      N/A                N/A
  Bluetooth        N/A                 Works    N/A                      N/A                N/A
  Sound            N/A                 Works    N/A                      N/A                N/A
  SD card reader   N/A                 Works    N/A                      N/A                N/A
  Webcam           N/A                 Works    N/A                      N/A                N/A
  ---------------- ------------------- -------- ------------------------ ------------------ ---------------- -------

## [Installation]

### [Kernel]

#### [GPU]

[KERNEL] **KMS**

    Device drivers -->
      Graphics support -->
        Direct Rendering Manager -->
          <*> Intel 8xx/9xx/G3x/G4x/HD Graphics
            [*] Enable modesetting on intel by default

[KERNEL] **evdev**

    Device Drivers --->
      Input device support --->
      <*>  Event interface

[KERNEL] **Framebuffers**

    Device Drivers --->
      Graphics support --->
        Frame Buffer Devices --->
          <*> Support for frame buffer devices --->

      Graphics support --->
        Console display driver support --->
          <*>  Framebuffer Console Support

[KERNEL] **AMD/ATI settings**

    Device Drivers --->
      Graphics support --->
      <*>  Direct Rendering Manager --->
          <*> Direct Rendering Manager (XFree86 4.1.0 and higher DRI support)  --->
            <M>    ATI Radeon

#### [Sound]

[KERNEL] **Intel HDA**

    Device Drivers  --->
       Sound card support --->
       <*> Sound card support
       <*>   Advanced Linux Sound Architecture --->
       [*]     PCI devices --->
       <*>       Inetl HD Audio --->

#### [Ethernet]

[KERNEL]

    Device Drivers  --->
       [*] Network Device Support  --->
       [*]   Ethernet driver support  --->
       <*>     Qualcomm Atheros AR816x/AR817x support
       [*]     Qualcomm devices

#### [Wi-Fi]

[KERNEL] **Broadcom BCM43142**

    Device Drivers  --->
       [*] Network Device Support  --->
       [*]   Wireless LAN  --->
       <M>     Broadcom IEEE802.11n PCIe SoftMAC WLAN driver

      [*] Network Device Support  --->
           Broadcom specific AMBA  --->
       <*>   BCMA support

[KERNEL]

    [*]   Wireless LAN  --->
    <M>   Intel Wireless WiFi Next Gen AGN - Wireless-N/Advanced-N/Ultimate-N (iwlwifi)
    -M-     Intel Wireless WiFi

#### [Bluetooth]

[KERNEL] **Bluetooth**

    [*] Networking support --->
         <*>   Bluetooth subsystem support --->
         <*>     RFCOMM protocol support
         [*]       RFCOMM tty support
         <*>     BNEP protocol support
         [*]       Multicast filter support
         [*]       Protocol filter support
         <*>     HIDP protocol support
                 Bluetooth device drivers --->
         <*>       HCI USB driver

#### [Fn-keys]

[KERNEL]

    Device Drivers  --->
        [*] X86 Platform Specific Device Drivers  --->
            <*>   Lenovo IdeaPad Laptop Extras
            <*> WMI
            <M>   Lenovo IdeaPad Laptop Extras

#### [Webcam]

[KERNEL]

    Device Drivers --->
       <*> Multimedia Support --->
       [*]   Cameras/video grabbers support
       [*]   Media USB Adapters  --->
       <*>   USB Video Class (UVC)
       [*]     UVC input events device support

#### [SD card reader]

[KERNEL]

    Device Drivers --->
       [*] Staging drivers  --->
       <*>   Realtek RTS5139 USB card reader support

    Device drivers -->
      Multifunction device drivers -->
          <*> Realtek PCI-E card reader
          < > Richtek RT5033 Power Management IC (NEW)
      <M> Realtek USB card reader
      MMC/SD/SDIO card support -->

         <*>   Realtek PCI-E SD/MMC Card Interface Driver
         <M>   Realtek USB SD/MMC Card Interface Driver

#### [Watchdog]

[KERNEL]

    Device Drivers  --->
    [*] Watchdog Timer Support  --->
    <M>   Intel TCO Timer/Watchdog
    [*]     Intel TCO Timer/Watchdog Specific Vendor Support

#### [Random number generator]

[KERNEL]

    Device Drivers  --->
    Character devices  --->
    [*]   Intel HW Random Number Generator support