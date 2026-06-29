[] This article has been flagged for not conforming to the [wiki guidelines](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Guidelines "Gentoo Wiki:Guidelines"). Please [help Gentoo out](https://wiki.gentoo.org/wiki/Help_improve_Gentoo_by_getting_involved_with_documentation!#Make_articles_conform_to_the_guidelines "Help improve Gentoo by getting involved with documentation!") by starting fixing things.

This article focus on getting all default hardware working with this model

**Resources**

[[]][Official Support Page](https://www.dell.com/support/home/en-us/product-support/product/inspiron-15-3501-laptop/overview)

[[]][Specifications](https://dl.dell.com/content/manual8212688-inspiron-3501-setup-and-specifications.pdf)

[[]][Hardware Maintenance Manual](https://dl.dell.com/content/manual39757171-inspiron-3501-service-manual.pdf)

## Contents

-   [[1] [Hardware]](#Hardware)
    -   [[1.1] [Standard]](#Standard)
-   [[2] [Installation]](#Installation)
    -   [[2.1] [Firmware]](#Firmware)
        -   [[2.1.1] [Graphics]](#Graphics)
            -   [[2.1.1.1] [DMC firmware]](#DMC_firmware)
            -   [[2.1.1.2] [GuC/HuC firmware]](#GuC.2FHuC_firmware)
        -   [[2.1.2] [Ethernet]](#Ethernet)
        -   [[2.1.3] [Wi-Fi]](#Wi-Fi)
    -   [[2.2] [Kernel]](#Kernel)
        -   [[2.2.1] [GPU firmware]](#GPU_firmware)
        -   [[2.2.2] [CPU]](#CPU)
        -   [[2.2.3] [Hard disk]](#Hard_disk)
        -   [[2.2.4] [Wi-Fi and Ethernet]](#Wi-Fi_and_Ethernet)
        -   [[2.2.5] [Sound]](#Sound)
        -   [[2.2.6] [Multi-function driver]](#Multi-function_driver)
        -   [[2.2.7] [Power management]](#Power_management)
        -   [[2.2.8] [Touchpad]](#Touchpad)
-   [[3] [External resources]](#External_resources)

## [Hardware]

### [Standard]

+----------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------+------------------------+------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------+----------------+------------------------------------------------------+
| Device                                                         | Make/model                                                                                                                                                                                                            | Status | Vendor ID / Product ID | Kernel driver(s)                                                                         | Firmware                                                                                                                                        | Kernel version | Notes                                                |
+----------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------+------------------------+------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------+----------------+------------------------------------------------------+
| CPU                                                            | [`Intel(R) Core(TM) i3-10005G1 CPU @ 1.20GHz`](https://www.intel.com/content/www/us/en/products/sku/196588/intel-core-i31005g1-processor-4m-cache-up-to-3-40-ghz/specifications.html) | Works  | N/A                    | N/A                                                                                      | N/A                                                                                                                                             | 5.15.69        | Different CPU options are available for this laptop. |
+----------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------+------------------------+------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------+----------------+------------------------------------------------------+
| GPU                                                            | [`Intel® UHD Graphics`](https://git.kernel.org/pub/scm/linux/kernel/git/firmware/linux-firmware.git/tree/i915)                                                                        | Works  | 8086:8a56              | [i915](https://wiki.gentoo.org/wiki/Intel "Intel")                                       | icl_dmc                                                                                                                                         | 5.15.69        | Intel Corporation Iris Plus Graphics G1 (Ice Lake)   |
|                                                                |                                                                                                                                                                                                                       |        |                        |                                                                                          |                                                                                                                                                 |                |                                                      |
|                                                                | \                                                                                                                                                                                                                     |        |                        |                                                                                          | icl_guc                                                                                                                                         |                |                                                      |
|                                                                | Iris Plus Graphics G1 (Ice Lake)                                                                                                                                                                                      |        |                        |                                                                                          |                                                                                                                                                 |                |                                                      |
|                                                                |                                                                                                                                                                                                                       |        |                        |                                                                                          | icl_huc                                                                                                                                         |                |                                                      |
+----------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------+------------------------+------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------+----------------+------------------------------------------------------+
| RAM                                                            | RAM Module(s) 4GB SODIMM                                                                                                                                                                                              | Works  | N/A                    | N/A                                                                                      | N/A                                                                                                                                             | 5.15.69        | Two DIMM slots. Max memory 16GB.                     |
+----------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------+------------------------+------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------+----------------+------------------------------------------------------+
| Hard Disk                                                      | -   [TOSHIBA MQ04ABF100](https://linux-hardware.org/?id=ide:toshiba-mq04abf100) (1TB)                                                                                                 | Works  |                        | ahci                                                                                     | N/A                                                                                                                                             | 5.15.69        |                                                      |
|                                                                | -                                                                                                                                                                                                                     |        |                        |                                                                                          |                                                                                                                                                 |                |                                                      |
|                                                                |                                                                                                                                                                                                                       |        |                        | [NVMe](https://wiki.gentoo.org/wiki/NVMe "NVMe")                                         |                                                                                                                                                 |                |                                                      |
+----------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------+------------------------+------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------+----------------+------------------------------------------------------+
| [Wifi](https://wiki.gentoo.org/wiki/Wifi "Wifi") | Qualcomm Atheros QCA9377 802.11ac Wireless Network Adapter                                                                                                                                                            | Works  |                        | [ath10k](https://cateee.net/lkddb/web-lkddb/ATH10K.html) | [ath10k](https://git.kernel.org/pub/scm/linux/kernel/git/firmware/linux-firmware.git/tree/ath10k/QCA9377/hw1.0) | 5.15.69        |                                                      |
+----------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------+------------------------+------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------+----------------+------------------------------------------------------+
| Sound                                                          | Realtek ALC3204                                                                                                                                                                                                       | Works  | N/A                    | snd_hda_intel snd_hda_codec_realtek                                                      | N/A                                                                                                                                             | 5.15.69        | N/A                                                  |
+----------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------+------------------------+------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------+----------------+------------------------------------------------------+
| HDMI                                                           | Intel Corporation Ice Lake-LP Smart Sound Technology Audio Controller                                                                                                                                                 | Works  |                        | snd_hda_intel snd_hda_codec_hdmi                                                         | N/A                                                                                                                                             | 5.15.69        | N/A                                                  |
|                                                                |                                                                                                                                                                                                                       |        |                        |                                                                                          |                                                                                                                                                 |                |                                                      |
| Sound                                                          |                                                                                                                                                                                                                       |        |                        |                                                                                          |                                                                                                                                                 |                |                                                      |
+----------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------+------------------------+------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------+----------------+------------------------------------------------------+
| [Touchpad](#Touchpad)                                          | DELL [0A2B:00 06CB:CDD6](https://linux-hardware.org/?id=ps/2:06cb-cdd6-dell0a2b-00-06cb-cdd6-mouse) Touchpad                                                                          | Works  |                        | intel-lpss i2c-hid                                                                       |                                                                                                                                                 | 5.15.69        |                                                      |
+----------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------+------------------------+------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------+----------------+------------------------------------------------------+

## [Installation]

### [Firmware]

Due to errata in the processor, it is advised to install and keep the CPU microcode up-to-date. See intel [intel microcode](https://wiki.gentoo.org/wiki/Intel_microcode "Intel microcode").

#### [Graphics]

Systems using Skylake, Broxton, or newer [Intel graphics](https://wiki.gentoo.org/wiki/Intel "Intel") will need additional [firmware](https://wiki.gentoo.org/wiki/Linux_firmware "Linux firmware") from the [[[sys-kernel/linux-firmware]](https://packages.gentoo.org/packages/sys-kernel/linux-firmware)[]] package:

`root `[`#`]`emerge --ask sys-kernel/linux-firmware`

Alternatively, the blobs can be directly downloaded from the [Linux repository](https://git.kernel.org/pub/scm/linux/kernel/git/firmware/linux-firmware.git/tree/i915) and put into /lib/firmware

##### [DMC firmware]

**D**isplay **M**icro**c**ontroller firmware provides support for advanced graphics low-power idle states.

##### [][GuC/HuC firmware]

**G**raphics **µC**ontroller firmware offloads functions from the host driver. **H**EVC/H.265 **µC**ontroller firmware improves hardware acceleration of media decoding.

`root `[`#`]`cp icl_guc_70.1.1.bin /var/lib/i915/`

[KERNEL] **GPU firmware**

    Device Drivers  --->
        Generic Driver Options  --->
            Firmware loader  --->
                -*- Firmware loading facility
                (i915/icl_dmc_ver1_09.bin ) Build named firmware blobs into the kernel binary
                (/lib/firmware) Firmware blobs root directory

** Warning**\
Including the firmware in-kernel may cause suspend-to-ram to fail, if this is a concern don\'t include the blob built into the kernel, instead, add the firmware blob into the initramfs.

[KERNEL] **Graphics (Linux 5.15)**

    Device Drivers  --->
        Graphics support  --->
            <*> /dev/agpgart (AGP Support)  --->
                --- /dev/agpgart (AGP Support)
                -*-   Intel 440LX/BX/GX, I8xx and E7x05 chipset support
            <*> Direct Rendering Manager (XFree86 4.1.0 and higher DRI support)  --->
                --- Direct Rendering Manager (XFree86 4.1.0 and higher DRI support)
                [*]   Enable legacy fbdev support for your modesetting driver
            <*> Intel 8xx/9xx/G3x/G4x/HD Graphics
            [ ]   Enable alpha quality support for new Intel hardware by default
            ()    Force probe driver for selected new Intel hardware
            [*]   Enable capturing GPU state following a hang
            [*]     Compress GPU error state
            [*]   Always enable userptr support
            [ ]   Enable Intel GVT-g graphics virtualization host support
                  Frame buffer Devices  --->
                      <*> Support for frame buffer devices  --->
                        [*]   EFI-based Framebuffer Support
                        <*>   Simple framebuffer support
                  Console display driver support  --->
                   [*] Framebuffer Console support

#### [Ethernet]

Install the [[[sys-kernel/linux-firmware]](https://packages.gentoo.org/packages/sys-kernel/linux-firmware)[]] package:

`root `[`#`]`emerge --ask sys-kernel/linux-firmware`

Alternatively, the blob can be directly downloaded from the [Linux repository](https://git.kernel.org/pub/scm/linux/kernel/git/firmware/linux-firmware.git/tree/rtl_nic/rtl8106e-1.fw) and copied to [/lib/firmware/rtl_nic].

#### [Wi-Fi]

Install the [[[sys-kernel/linux-firmware]](https://packages.gentoo.org/packages/sys-kernel/linux-firmware)[]] package:

`root `[`#`]`emerge --ask sys-kernel/linux-firmware`

Alternatively, the blobs can be directly downloaded from the [Linux repository](https://git.kernel.org/pub/scm/linux/kernel/git/firmware/linux-firmware.git/tree/ath10k/QCA9377/hw1.0).

### [Kernel]

#### [GPU firmware]

[KERNEL] **GPU firmware**

    Device Drivers  --->
        Generic Driver Options  --->
            Firmware loader --->
                -*- Firmware loading facility
                (i915/kbl_dmc_ver1_04.bin) Build named firmware blobs into the kernel binary
                (/lib/firmware) Firmware blobs root directory

#### [CPU]

[KERNEL] **CPU**

    Processor type and features  --->
        [*] Machine Check / overheating reporting
        [*]   Intel MCE Features
        [ ]   AMD MCE Features
        Processor family (Core 2/newer Xeon)  --->
            ( ) Opteron/Athlon64/Hammer/K8
            ( ) Intel P4 / older Netburst based Xeon
            (X) Core 2/newer Xeon
            ( ) Intel Atom
            ( ) Generic-x86-64

#### [Hard disk]

** Important**\
The configuration assumes that SATA mode is set to AHCI in BIOS/UEFI.

[KERNEL]

    Device Drivers --->
       <*> Serial ATA and Parallel ATA drivers  --->
          [*] ATA ACPI Support

       Select the driver for the SATA controller, e.g.:
          <*> AHCI SATA support (ahci)
             [*]   ATA SFF support (for legacy IDE and PATA)
             [*]     ATA BMDMA support
          <*> Intel ESB, ICH, PIIX3, PIIX4 PATA/SATA support (ata_piix)

       SCSI device support  --->
          <*> SCSI device support
          <*> SCSI disk support

        NVME Support  --->
            [*] NVM Express block device
            [Opt] NVMe hardware monitoring

#### [Wi-Fi and Ethernet]

[KERNEL] **Wi-Fi**

    [*] Networking support  --->
          -*-   Wireless  --->
              <*>   cfg80211 - wireless configuration API
              [*]     support CRDA
              <*>   Generic IEEE 802.11 Networking Stack (mac80211)
              [*]   Minstrel
              [*]   Enable LED triggers
            <*>   RF switch subsystem support  --->
    Device Drivers --->
        Generic Driver Options  --->
                Firmware loader  --->
                   -*- Firmware loading facility
                    (ath10k/QCA9377/hw1.0/board-2.bin ath10k/QCA9377/hw1.0/firmware-5.bin   regulatory.db  regulatory.db.p7s)
       [*] Network device support  --->
          [*]   Ethernet driver support  --->

              [*]   Realtek devices
              <*>     Realtek 8169/8168/8101/8125 ethernet support
          Wireless LAN  --->
              [*]   Atheros/Qualcomm devices
              <*>     Atheros 802.11ac wireless cards support
              <*>     Atheros ath10k PCI support

#### [Sound]

snd-hda-intel driver is used . To force sof driver with kernel parameter options snd-intel-dspcfg dsp_driver=3 but didnt see noticeable difference

[KERNEL] **Sound**

    Device Drivers --->
       <*> Sound card support  --->
       <*>   Advanced Linux Sound Architecture  --->
       <*>   HR-timer backend support
       [*]   Sound Proc FS Support
       <*>   Sequencer support
       [*]     Use HR-timer as default sequencer timer
       [*]   Generic sound devices  --->
       [*]   PCI sound devices  --->
       HD-Audio  --->
           <*> HD Audio PCI
           <*> Build Realtek HD-audio codec support
           <opt> Build HDMI/DisplayPort HD-audio codec support
           -*- Enable generic HD-audio codec parser

#### [Multi-function driver]

** Note**\
The driver is needed for i2c-hid driver of touchpad and other power management.

[KERNEL] **Multi-function driver**

    Device Drivers  --->
         Multifunction device drivers  --->
            <*> Intel ICH LPC
            <*> Intel Low Power Subsystem support in ACPI mode
            <*> Intel Low Power Subsystem support in PCI mode

#### [Power management]

[KERNEL]

            Power management and ACPI options  --->
              [ ] Suspend to RAM and standby
              [*] ACPI (Advanced Configuration and Power Interface) Support  --->
              [*] Power Management Timer Support
              [*] Platform Runtime Mechanism Support
                    CPU Frequency scaling  --->
                          < >   'ondemand' cpufreq policy governor
                          < >   'conservative' cpufreq governor
                          [*]   Intel P state control
              [*] Cpuidle Driver for Intel Processors

#### [Touchpad]

kernel says DELL0A2B i2c_designware which used hid-multitouch driver

[KERNEL] **Touchpad**

    Device Drivers  --->
        Input device support  --->
          <*>   Event interface

      -*- Pin controllers  --->
             [*]   Intel Ice Lake PCH pinctrl and GPIO driver
        -*- I2C support
          I2C Hardware Bus support  --->
                [*] Intel 82801 (ICH/PCH)
                [*] Synopsys DesignWare Platform
        HID support  --->
            [*]   /dev/hidraw raw HID device support
            [*]   User-space I/O driver support for HID subsystem
            [*]   Generic HID driver
            Special HID drivers  --->
                  [*] HID Multitouch panels
            I2C HID support  --->
                  [*] HID over I2C transport layer ACPI driver

## [External resources]

-   [https://linux-hardware.org/?view=computers&vendor=Dell&model=Inspiron+3501](https://linux-hardware.org/?view=computers&vendor=Dell&model=Inspiron+3501)
-   [https://ubuntu.com/certified/202006-27975/20.04%20LTS](https://ubuntu.com/certified/202006-27975/20.04%20LTS)