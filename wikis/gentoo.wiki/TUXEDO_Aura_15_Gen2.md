**Resources**

[[]][Home](https://www.tuxedocomputers.com/en/Linux-Hardware/Linux-Notebooks/15-16-inch/TUXEDO-Aura-15-Gen2.tuxedo)

[![](/images/thumb/9/93/20220423_190142_nometadata.jpg/300px-20220423_190142_nometadata.jpg)](https://wiki.gentoo.org/wiki/File:20220423_190142_nometadata.jpg)

[](https://wiki.gentoo.org/wiki/File:20220423_190142_nometadata.jpg "Enlarge")

A TUXEDO Aura 15 (Gen2) running Gentoo Linux with TUXEDO\'s custom control center and a terminal with neofetch open.

The **TUXEDO Aura 15 (Gen2)** is a configurable Linux notebook from 2022. It can be run using only open source drivers without sacrificing any functionality. When buying a configuration with 32G memory and a R7 5700U, the notebook can easily run Gentoo.

## Contents

-   [[1] [Hardware]](#Hardware)
-   [[2] [Installation]](#Installation)
    -   [[2.1] [make.conf]](#make.conf)
    -   [[2.2] [Kernel]](#Kernel)
        -   [[2.2.1] [TUXEDO\'s & Clevo\'s driver modules]](#TUXEDO.27s_.26_Clevo.27s_driver_modules)
-   [[3] [See also]](#See_also)
-   [[4] [External ressources]](#External_ressources)
-   [[5] [References]](#References)

## [Hardware]

  -------------------------------------------------------- ------------------------------ -------------------------------------------- ---------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Device                                                   Make/model                     Status                                       Kernel version   Note
  APU                                                      AMD Ryzen 7 5700U              Works                                        6.1.31
  APU                                                      AMD Ryzen 5 5500U              Works^[\[1\]](#cite_note-tuxedo_linux-1)^    N/A
  APU                                                      AMD Ryzen 3 5300U              Works^[\[1\]](#cite_note-tuxedo_linux-1)^    N/A
  Video                                                    AMD ATI 05:00.0 Lucienne       Works                                        6.1.31
  Webcam                                                   BisonCam,NB Pro (1MP 720p)     Works                                        6.1.31
  External speaker                                         Stereo High Definition Audio   Works                                        6.1.31
  Microphone                                               N/A                            Works                                        6.1.31
  Keyboard                                                 QWERTZ                         Works                                        6.1.31           should work with every other layout; to control backlighting, go to [TUXEDO\'s/Clevo\'s driver modules](https://wiki.gentoo.org/wiki/TUXEDO_Aura_15_(Gen2)#TUXEDO.27s_.26_Clevo.27s_driver_modules "TUXEDO Aura 15 (Gen2)")
  LTE/HSDPA+ 4G/GPS Standalone, A-GPS, GPS XTRA, Glonass   Huawei ME936                   Works^[\[1\]](#cite_note-tuxedo_linux-1)^    N/A
  -------------------------------------------------------- ------------------------------ -------------------------------------------- ---------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## [Installation]

### [make.conf]

[FILE] **`/etc/portage/make.conf`For every Notebook configuration**

    CHOST="x86_64-pc-linux-gnu"
    COMMON_FLAGS="-march=znver2"

[FILE] **`/etc/portage/package.use/00video`**

    */* VIDEO_CARDS: -* amdgpu radeonsi radeon

[FILE] **`/etc/portage/package.use/00grub`**

    */* GRUB_PLATFORMS: efi-64

[FILE] **`/etc/portage/package.use/00cpu-flags`Only Ryzen 7 5700U**

    */* CPU_FLAGS_X86: aes avx avx2 f16c fma3 mmx mmxext pclmul popcnt rdrand sha sse sse2 sse3 sse4_1 sse4_2 sse4a ssse3

### [Kernel]

-   Read [this](https://wiki.gentoo.org/wiki/Ryzen#Kernel "Ryzen") article for the processor.
-   Read [this](https://wiki.gentoo.org/wiki/Webcam#Kernel "Webcam") article for the webcam.
-   Enable these options for the remaining hardware:

[KERNEL] **Other options with 6.1.31-gentoo**

    [*] Networking Support  --->
      <M> Bluetooth subsystem support  --->
        Bluetooth device drivers  --->
          <M> HCI USB driver
          [*]   Broadcom protocol support
          [*]   Realtek protocol support
      [*] Wireless  --->
        <M> cfg80211 - wireless configuration API
        <M> Generic IEEE 802.11 Networking Stack (mac80211)
    Device Drivers  --->
      [*] Misc devices  --->
        <*> Realtek PCI-E card reader
      [*] Network device support  --->
        [*] Ethernet driver support  --->
          [*] Realtek devices
          <M>   RealTek RTL-8129/8130/8139 PCI Fast Ethernet Adapter support
          <M>   Realtek 8169/8168/8101/8125 ethernet support
        [*] Wireless LAN  --->
          [*] Intel devices
          <M>   Intel Wireless WiFi Next Gen AGN - Wireless-N/Advanced-N/Ultimate-N (iwlwifi)
          <M>     Intel Wireless WiFi MVM Firmware support
      [*] GPIO Support  --->
        [*] Character device (/dev/gpiochipN) support
        [*]   Support GPIO ABI Version 1
      Graphics support  --->
        <M> ATI Radeon
        <M> AMD GPU
          [*] Enable amdgpu support for SI parts
          ACP (Audio CoProcessor) Configuration  --->
            [*] Enable AMD Audio CoProcessor IP support
          Display Engine Configuration  --->
            [*] AMD DC - Enable new display engine
        Frame buffer Devices  --->
          <*> Support for frame buffer devices  --->
            [*] EFI-based Framebuffer Support
            <*> ATI Radeon display support
            [*]   DDC/I2C for ATI Radeon support
            [*]   Support for backlight control
      HID support  --->
        [*] /dev/hidraw raw HID device support
        <*> Generic HID driver
        I2C HID support  --->
          <*> HID over I2C transport layer ACPI driver
      [*] USB support  --->
        <*> Support for Host-side USB
        [*] PCI based USB host interface
        [*] USB announce new devices
        <*> xHCI HCD (USB 3.0) support
        <*> EHCI HCD (USB 2.0) support
        <*> USB Type-C Support  --->
          <*> USB Type-C Port Controller Manager
          USB Type-C Alternate Mode drivers  --->
            <*> DisplayPort Alternate Mode driver
      <*> MMC/SD/SDIO card support  --->
        <*> Realtek PCI-E SD/MMC Card Interface Driver

#### [][TUXEDO\'s & Clevo\'s driver modules]

Read the [TUXEDO Software](https://wiki.gentoo.org/wiki/TUXEDO_Software "TUXEDO Software") article for further instructions.

## [See also]

-   [Ryzen](https://wiki.gentoo.org/wiki/Ryzen "Ryzen") --- a multithreaded, high performance processor manufactured by AMD.
-   [AMDGPU](https://wiki.gentoo.org/wiki/AMDGPU "AMDGPU") --- the open source graphics drivers for AMD Radeon and other GPUs.

## [External ressources]

-   [Wikipedia Ryzen Mobile 5xxx](https://en.wikipedia.org/wiki/Ryzen#Mobile_4)

## [References]

1.  [[↑ ^[1.0](#cite_ref-tuxedo_linux_1-0)^ ^[1.1](#cite_ref-tuxedo_linux_1-1)^ ^[1.2](#cite_ref-tuxedo_linux_1-2)^] [[https://www.tuxedocomputers.com/en/Infos/Help-Support/FAQ/Operating-Systems/Do-other-operating-systems-run-on-my-TUXEDO-device-.tuxedo](https://www.tuxedocomputers.com/en/Infos/Help-Support/FAQ/Operating-Systems/Do-other-operating-systems-run-on-my-TUXEDO-device-.tuxedo)]]