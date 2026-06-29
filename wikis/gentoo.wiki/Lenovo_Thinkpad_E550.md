[] This article has been flagged for not conforming to the [wiki guidelines](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Guidelines "Gentoo Wiki:Guidelines"). Please [help Gentoo out](https://wiki.gentoo.org/wiki/Help_improve_Gentoo_by_getting_involved_with_documentation!#Make_articles_conform_to_the_guidelines "Help improve Gentoo by getting involved with documentation!") by starting fixing things.

**Resources**

[[]][Home](https://pcsupport.lenovo.com/us/en/products/laptops-and-netbooks/thinkpad-edge-laptops/thinkpad-e550)

[[]][Specifications](https://psref.lenovo.com/syspool/Sys/PDF/ThinkPad/ThinkPad_E550/ThinkPad_E550_Spec.PDF)

[[]][Specifications (by region)](https://psref.lenovo.com/Product/ThinkPad/ThinkPad_E550)

[[]][Hardware Maintenance Manual](https://download.lenovo.com/pccbbs/mobiles_pdf/e550_hmm_en_sp40a27128_02.pdf)

[[]][User Guide](https://download.lenovo.com/ibmdl/pub/pc/pccbbs/mobiles_pdf/e550_e555_e550c_ug_en.pdf)

[[]][BIOS Setup](https://download.lenovo.com/pccbbs/mobiles_pdf/lenovo_bios_setup_linux_wmi_sysfs_1.2.pdf)

[[]][ThinkPad E series](https://en.wikipedia.org/wiki/ThinkPad_E_series "wikipedia:ThinkPad E series")

## Contents

-   [[1] [Hardware]](#Hardware)
    -   [[1.1] [Status]](#Status)
    -   [[1.2] [ACPI / Power Management]](#ACPI_.2F_Power_Management)
-   [[2] [Installation]](#Installation)
    -   [[2.1] [Firmware]](#Firmware)
    -   [[2.2] [Kernel]](#Kernel)
    -   [[2.3] [Emerge]](#Emerge)
-   [[3] [See also]](#See_also)

## [Hardware]

`root `[`#`]`lspci`

    00:00.0 Host bridge: Intel Corporation Broadwell-U Host Bridge -OPI (rev 09)
    00:02.0 VGA compatible controller: Intel Corporation Broadwell-U Integrated Graphics (rev 09)
    00:03.0 Audio device: Intel Corporation Broadwell-U Audio Controller (rev 09)
    00:14.0 USB controller: Intel Corporation Wildcat Point-LP USB xHCI Controller (rev 03)
    00:16.0 Communication controller: Intel Corporation Wildcat Point-LP MEI Controller #1 (rev 03)
    00:19.0 Ethernet controller: Intel Corporation Ethernet Connection (3) I218-V (rev 03)
    00:1b.0 Audio device: Intel Corporation Wildcat Point-LP High Definition Audio Controller (rev 03)
    00:1c.0 PCI bridge: Intel Corporation Wildcat Point-LP PCI Express Root Port #1 (rev e3)
    00:1c.2 PCI bridge: Intel Corporation Wildcat Point-LP PCI Express Root Port #3 (rev e3)
    00:1c.4 PCI bridge: Intel Corporation Wildcat Point-LP PCI Express Root Port #5 (rev e3)
    00:1c.5 PCI bridge: Intel Corporation Wildcat Point-LP PCI Express Root Port #6 (rev e3)
    00:1d.0 USB controller: Intel Corporation Wildcat Point-LP USB EHCI Controller (rev 03)
    00:1f.0 ISA bridge: Intel Corporation Wildcat Point-LP LPC Controller (rev 03)
    00:1f.2 SATA controller: Intel Corporation Wildcat Point-LP SATA Controller [AHCI Mode] (rev 03)
    00:1f.3 SMBus: Intel Corporation Wildcat Point-LP SMBus Controller (rev 03)
    00:1f.6 Signal processing controller: Intel Corporation Wildcat Point-LP Thermal Management Controller (rev 03)
    04:00.0 Network controller: Intel Corporation Wireless 7265 (rev 61)
    05:00.0 Display controller: Advanced Micro Devices, Inc. [AMD/ATI] Opal XT [Radeon R7 M265]
    06:00.0 Unassigned class [ff00]: Realtek Semiconductor Co., Ltd. RTS5227 PCI Express Card Reader (rev 01)

`root `[`#`]`lsusb`

    Bus 003 Device 002: ID 8087:8001 Intel Corp.
    Bus 003 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub
    Bus 002 Device 001: ID 1d6b:0003 Linux Foundation 3.0 root hub
    Bus 001 Device 004: ID 5986:055a Acer, Inc
    Bus 001 Device 002: ID 04f2:b444 Chicony Electronics Co., Ltd
    Bus 001 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub

### [Status]

  ------------------------------------------------------------- ------------- --------------------------------------------------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                             Device                                 Works                                                             Notes
              CPU: Intel Core i5-5200U or i7-5500U                   Yes
                  Video: Intel HD Graphics 5500                      Yes
                    Video: AMD Radeon R7 M265                    Not tested
    SATA: Intel Corporation Wildcat Point-LP SATA Controller         Yes
                      Audio: Intel HD Audio                          Yes
       Ethernet: Intel I218-V PCI Express Gigabit Ethernet           Yes
           Wireless LAN: Intel Wireless 7265 802.11ac                Yes
           Wireless LAN: Intel Wireless 3160 802.11ac                Yes
             Bluetooth: Intel Wireless 7265 802.11ac                 Yes
             Bluetooth: Intel Wireless 3160 802.11ac                 Yes
         Camera: Chicony Electronics Co., Ltd USB webcam             Yes
                        Camera: Acer, Inc                            Yes
   Fingerprint reader: Validity VFS5017 USB fingerprint reader       Yes                                             Works with sys-auth/libfprint-0.5.1-r1
        SD card reader: Realtek RTS5227 PCI-E card reader            Yes
                   SynPS/2 Synaptics TouchPad                        Yes
                       Hardware monitoring                           Yes
                             Hotkeys                                 Yes                                               Some have to be manually configured                                          See also [http://www.thinkwiki.org/wiki/Thinkpad-acpi#Supported_ThinkPads](http://www.thinkwiki.org/wiki/Thinkpad-acpi#Supported_ThinkPads)
                     Discrete TPM (TPM 1.2)                      Not tested                               Must be activated through BIOS, disables access to Intel PTT
                       Intel PTT (TPM 2.0)                         Partial     A bug (allegedly from the BIOS) prevents use when IOMMU is enabled, pass intel_iommu=off at boot time to disable it
  ------------------------------------------------------------- ------------- --------------------------------------------------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### [][ACPI / Power Management]

  ----------------------------- ------- ------------------------ --
            Function             Works           Notes
      CPU frequency scaling       Yes    With laptop-mode-tools
         Suspend to RAM           Yes
   Suspend to disk (hibernate)    Yes
    Display backlight control     Yes
  ----------------------------- ------- ------------------------ --

## [Installation]

### [Firmware]

The wireless card requires external firmware:

`root `[`#`]`emerge --ask sys-kernel/linux-firmware`

### [Kernel]

** Note**\
For UEFI booting, EFI framebuffer is not needed. It conflicts with Intel framebuffer and is recommended not to be built.

[KERNEL]

    Processor type and features  --->
      Processor family (Core 2/Newer Xeon) --->
      <*> CPU microcode loading support
      [*]   Intel microcode loading support

    Power management and ACPI options  --->
      [*] ACPI (Advanced Configuration and Power Interface) Support  --->
        <*> Battery
        <*> Video
      CPU Frequency scaling  --->
        Default CPUFreq governor (userspace)
        <*> 'userspace' governor
        [*] Intel P state control

    [*] Networking support  --->
      <*> Bluetooth subsystem support  --->
        Bluetooth device drivers  --->
          <*> HCI USB driver
      <*> Wireless  --->
        <*> cfg80211 - wireless configuration API
        <*> Generic IEEE 802.11 Networking Stack (mac80211)

    Device Drivers  --->
      Misc devices  --->
        <*> Realtek PCI-E card reader
      SCSI device support  --->
        <*> SCSI disk support
      <*> Serial ATA and Parallel ATA drivers  --->
        <*> AHCI SATA support
      [*] Network device support  --->
        [*] Ethernet driver support  --->
          [*] Intel devices
            <*> Intel(R) PRO/1000 PCI-Express Gigabit Ethernet support
        [*] Wireless LAN  --->
          <M> Intel Wireless WiFi Next Gen AGN - Wireless-N/Advanced-N/Ultimate-N (iwlwifi)
          <M> Intel Wireless WiFi MVM Firmware support
      <*> I2C support  --->
        I2C Hardware Bus support  --->
          <*> Intel 82801 (ICH/PCH)
      <*> Hardware Monitoring support  --->
        <*> Intel Core/Core2/Atom temperature sensor
      Multifunction device drivers  --->
        <*> Intel ICH LPC
      <*> Multimedia support  --->
        [*] Media USB Adapters  --->
          <*> USB Video Class (UVC)
      Graphics support  --->
        <*> Direct Rendering Manager --->
          <*> Direct Rendering Manager (XFree86 4.1.0 and higher DRI support) --->
            <*> Intel 8xx/9xx/G3x/G4x/HD Graphics
              [*] Enable modesetting on intel by default
              [*] Enable legacy fbdev support for the modesettting intel driver
        # For models with discrete AMD graphics, add the following
        [*] Laptop Hybrid Graphics - GPU switching support
        <*> Direct Rendering Manager --->
          <*> Direct Rendering Manager (XFree86 4.1.0 and higher DRI support) --->
            <*> ATI Radeon
        Console display driver support  --->
          Frame buffer Devices --->
            -*- Support for frame buffer devices --->
      <*> Sound card support  --->
        <*> Advanced Linux Sound Architecture  --->
          [*] PCI sound devices  --->
            <*> Intel HD Audio  --->
              <*> Build HDMI/DisplayPort HD-audio codec support
              <*> Build Conexant HD-audio codec support
      [*] USB support  --->
        <*> xHCI HCD (USB 3.0) support
        <*> EHCI HCD (USB 2.0) support
      <*> MMC/SD/SDIO card support
        <*> Realtek PCI-E SD/MMC Card Interface Driver
      [*] X86 Platform Specific Device Drivers  --->
        <*> ThinkPad ACPI Laptop Extras
        <*> Thinkpad Hard Drive Active Protection System (hdaps)
        <*> Intel Intelligent Power Sharing
        <*> Intel Rapid Start Technology Driver
      [*] IOMMU Hardware Support  --->
        [*] Support for Intel IOMMU using DMA Remapping Devices
        [*]  Enable Intel DMA Remapping Devices by default
        [*] Support for Interrupt Remapping

    [*] Cryptographic API  --->
      <*> AES cipher algorithms (AES-NI)

### [Emerge]

[FILE] **`/etc/portage/package.use/00input`**

    */* INPUT_DEVICES: evdev synaptics

[FILE] **`/etc/portage/package.use/00video`**

    */* VIDEO_CARDS: -* intel i965 radeon

[FILE] **`/etc/portage/package.use/00cpu-flags`**

    */*  CPU_FLAGS_X86: aes avx avx2 fma3 mmx mmxext popcnt sse sse2 sse3 sse4_1 sse4_2 ssse3

For the card reader ([[[sys-apps/pcsc-tools]](https://packages.gentoo.org/packages/sys-apps/pcsc-tools)[]]):

`root `[`#`]`emerge --ask sys-apps/pcsc-tools`

For the fingerprint reader ([[[sys-auth/libfprint]](https://packages.gentoo.org/packages/sys-auth/libfprint)[]]):

`root `[`#`]`emerge --ask sys-auth/libfprint`

## [See also]

-   [Lenovo ThinkPad T440s](https://wiki.gentoo.org/wiki/Lenovo_ThinkPad_T440s "Lenovo ThinkPad T440s")
-   [Lenovo Yoga 3 Pro](https://wiki.gentoo.org/wiki/Lenovo_Yoga_3_Pro "Lenovo Yoga 3 Pro")