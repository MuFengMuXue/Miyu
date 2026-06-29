**Resources**

[[]][Product Information](https://www3.lenovo.com/us/en/laptops/thinkpad/thinkpad-x/Thinkpad-X1-Yoga-2nd-Generation/p/22TP2TXX12Y)

[[]][Official Support Page](https://pcsupport.lenovo.com/us/en/products/laptops-and-netbooks/thinkpad-x-series-laptops/thinkpad-x1-yoga-type-20jd-20je-20jf-20jg)

[[]][Specifications](https://psref.lenovo.com/syspool/Sys/PDF/ThinkPad/ThinkPad_X1_Yoga_2nd_Gen/ThinkPad_X1_Yoga_2nd_Gen_Spec.PDF)

[[]][Hardware Maintenance Manual](https://download.lenovo.com/pccbbs/mobiles_pdf/tp_x1yoga_2ndgen_hmm_v2.pdf)

[[]][User Guide](https://download.lenovo.com/pccbbs/mobiles_pdf/x1_yoga_ug_en.pdf)

[[]][BIOS Setup](https://download.lenovo.com/pccbbs/mobiles_pdf/lenovo_bios_setup_linux_wmi_sysfs_1.2.pdf)

[[]][ThinkPad X1 series](https://en.wikipedia.org/wiki/ThinkPad_X1_series "wikipedia:ThinkPad X1 series")

## Contents

-   [[1] [Hardware]](#Hardware)
    -   [[1.1] [Stock Device]](#Stock_Device)
        -   [[1.1.1] [With Dock]](#With_Dock)
    -   [[1.2] [Device Table]](#Device_Table)
-   [[2] [Installation]](#Installation)
    -   [[2.1] [Firmware]](#Firmware)
    -   [[2.2] [Kernel]](#Kernel)
    -   [[2.3] [Emerge]](#Emerge)
-   [[3] [Configuration]](#Configuration)
    -   [[3.1] [Finger/Pen Input]](#Finger.2FPen_Input)
    -   [[3.2] [Trackpoint scrolling]](#Trackpoint_scrolling)
    -   [[3.3] [Hotkeys]](#Hotkeys)
-   [[4] [Updates]](#Updates)
    -   [[4.1] [fwupd]](#fwupd)
    -   [[4.2] [BIOS/UEFI]](#BIOS.2FUEFI)
    -   [[4.3] [Thunderbolt Firmware]](#Thunderbolt_Firmware)
    -   [[4.4] [Thunderbolt Dock Firmware]](#Thunderbolt_Dock_Firmware)

## [Hardware]

### [Stock Device]

`root `[`#`]`lspci -nnk`

    00:00.0 Host bridge [0600]: Intel Corporation Xeon E3-1200 v6/7th Gen Core Processor Host Bridge/DRAM Registers [8086:5904] (rev 02)
            Subsystem: Lenovo Xeon E3-1200 v6/7th Gen Core Processor Host Bridge/DRAM Registers [17aa:224e]
            Kernel driver in use: skl_uncore
    00:02.0 VGA compatible controller [0300]: Intel Corporation HD Graphics 620 [8086:5916] (rev 02)
            Subsystem: Lenovo HD Graphics 620 [17aa:224e]
            Kernel driver in use: i915
            Kernel modules: i915
    00:08.0 System peripheral [0880]: Intel Corporation Xeon E3-1200 v5/v6 / E3-1500 v5 / 6th/7th Gen Core Processor Gaussian Mixture Model [8086:1911]
            Subsystem: Lenovo Xeon E3-1200 v5/v6 / E3-1500 v5 / 6th/7th Gen Core Processor Gaussian Mixture Model [17aa:224e]
    00:13.0 Non-VGA unclassified device [0000]: Intel Corporation Sunrise Point-LP Integrated Sensor Hub [8086:9d35] (rev 21)
            Subsystem: Lenovo Sunrise Point-LP Integrated Sensor Hub [17aa:224e]
            Kernel driver in use: intel_ish_ipc
    00:14.0 USB controller [0c03]: Intel Corporation Sunrise Point-LP USB 3.0 xHCI Controller [8086:9d2f] (rev 21)
            Subsystem: Lenovo Sunrise Point-LP USB 3.0 xHCI Controller [17aa:224e]
            Kernel driver in use: xhci_hcd
    00:14.2 Signal processing controller [1180]: Intel Corporation Sunrise Point-LP Thermal subsystem [8086:9d31] (rev 21)
            Subsystem: Lenovo Sunrise Point-LP Thermal subsystem [17aa:224e]
    00:15.0 Signal processing controller [1180]: Intel Corporation Sunrise Point-LP Serial IO I2C Controller #0 [8086:9d60] (rev 21)
            Subsystem: Lenovo Sunrise Point-LP Serial IO I2C Controller [17aa:224e]
    00:16.0 Communication controller [0780]: Intel Corporation Sunrise Point-LP CSME HECI #1 [8086:9d3a] (rev 21)
            Subsystem: Lenovo Sunrise Point-LP CSME HECI [17aa:224e]
            Kernel driver in use: mei_me
    00:1c.0 PCI bridge [0604]: Intel Corporation Sunrise Point-LP PCI Express Root Port #1 [8086:9d10] (rev f1)
            Kernel driver in use: pcieport
    00:1c.2 PCI bridge [0604]: Intel Corporation Sunrise Point-LP PCI Express Root Port #3 [8086:9d12] (rev f1)
            Kernel driver in use: pcieport
    00:1c.4 PCI bridge [0604]: Intel Corporation Sunrise Point-LP PCI Express Root Port #5 [8086:9d14] (rev f1)
            Kernel driver in use: pcieport
    00:1d.0 PCI bridge [0604]: Intel Corporation Sunrise Point-LP PCI Express Root Port #9 [8086:9d18] (rev f1)
            Kernel driver in use: pcieport
    00:1f.0 ISA bridge [0601]: Intel Corporation Sunrise Point LPC Controller/eSPI Controller [8086:9d4e] (rev 21)
            Subsystem: Lenovo Sunrise Point LPC Controller/eSPI Controller [17aa:224e]
    00:1f.2 Memory controller [0580]: Intel Corporation Sunrise Point-LP PMC [8086:9d21] (rev 21)
            Subsystem: Lenovo Sunrise Point-LP PMC [17aa:224e]
    00:1f.3 Audio device [0403]: Intel Corporation Sunrise Point-LP HD Audio [8086:9d71] (rev 21)
            Subsystem: Lenovo Sunrise Point-LP HD Audio [17aa:224e]
            Kernel driver in use: snd_hda_intel
            Kernel modules: snd_hda_intel
    00:1f.4 SMBus [0c05]: Intel Corporation Sunrise Point-LP SMBus [8086:9d23] (rev 21)
            Subsystem: Lenovo Sunrise Point-LP SMBus [17aa:224e]
            Kernel driver in use: i801_smbus
            Kernel modules: i2c_i801
    00:1f.6 Ethernet controller [0200]: Intel Corporation Ethernet Connection (4) I219-LM [8086:15d7] (rev 21)
            Subsystem: Lenovo Ethernet Connection (4) I219-LM [17aa:224e]
            Kernel driver in use: e1000e
    02:00.0 Unassigned class [ff00]: Realtek Semiconductor Co., Ltd. RTS525A PCI Express Card Reader [10ec:525a] (rev 01)
            Subsystem: Lenovo RTS525A PCI Express Card Reader [17aa:224e]
            Kernel driver in use: rtsx_pci
    04:00.0 Network controller [0280]: Intel Corporation Wireless 8265 / 8275 [8086:24fd] (rev 88)
            Subsystem: Intel Corporation Wireless 8265 / 8275 [8086:0130]
            Kernel driver in use: iwlwifi
            Kernel modules: iwlwifi
    05:00.0 Non-Volatile memory controller [0108]: Lenovo Device [17aa:0004]
            Subsystem: Lenovo Device [17aa:1004]
            Kernel driver in use: nvme

`root `[`#`]`lsusb`

    Bus 002 Device 001: ID 1d6b:0003 Linux Foundation 3.0 root hub
    Bus 001 Device 005: ID 138a:0097 Validity Sensors, Inc.
    Bus 001 Device 004: ID 04f2:b5ce Chicony Electronics Co., Ltd Integrated Camera
    Bus 001 Device 003: ID 8087:0a2b Intel Corp.
    Bus 001 Device 007: ID 1199:9079 Sierra Wireless, Inc.
    Bus 001 Device 006: ID 056a:50b8 Wacom Co., Ltd
    Bus 001 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub

`root `[`#`]`lsusb`

    /:  Bus 02.Port 1: Dev 1, Class=root_hub, Driver=xhci_hcd/6p, 5000M
    /:  Bus 01.Port 1: Dev 1, Class=root_hub, Driver=xhci_hcd/12p, 480M
        |__ Port 6: Dev 7, If 12, Class=Communications, Driver=cdc_mbim, 480M
        |__ Port 6: Dev 7, If 13, Class=CDC Data, Driver=cdc_mbim, 480M
        |__ Port 7: Dev 3, If 0, Class=Wireless, Driver=btusb, 12M
        |__ Port 7: Dev 3, If 1, Class=Wireless, Driver=btusb, 12M
        |__ Port 8: Dev 4, If 1, Class=Video, Driver=uvcvideo, 480M
        |__ Port 8: Dev 4, If 0, Class=Video, Driver=uvcvideo, 480M
        |__ Port 9: Dev 5, If 0, Class=Vendor Specific Class, Driver=, 12M
        |__ Port 10: Dev 6, If 0, Class=Human Interface Device, Driver=usbhid, 12M
        |__ Port 10: Dev 6, If 1, Class=Human Interface Device, Driver=usbhid, 12M

\

#### [With Dock]

`root `[`#`]`lspci -nnk`

    00:00.0 Host bridge [0600]: Intel Corporation Xeon E3-1200 v6/7th Gen Core Processor Host Bridge/DRAM Registers [8086:5904] (rev 02)
            Subsystem: Lenovo Xeon E3-1200 v6/7th Gen Core Processor Host Bridge/DRAM Registers [17aa:224e]
            Kernel driver in use: skl_uncore
    00:02.0 VGA compatible controller [0300]: Intel Corporation HD Graphics 620 [8086:5916] (rev 02)
            Subsystem: Lenovo HD Graphics 620 [17aa:224e]
            Kernel driver in use: i915
            Kernel modules: i915
    00:08.0 System peripheral [0880]: Intel Corporation Xeon E3-1200 v5/v6 / E3-1500 v5 / 6th/7th Gen Core Processor Gaussian Mixture Model [8086:1911]
            Subsystem: Lenovo Xeon E3-1200 v5/v6 / E3-1500 v5 / 6th/7th Gen Core Processor Gaussian Mixture Model [17aa:224e]
    00:13.0 Non-VGA unclassified device [0000]: Intel Corporation Sunrise Point-LP Integrated Sensor Hub [8086:9d35] (rev 21)
            Subsystem: Lenovo Sunrise Point-LP Integrated Sensor Hub [17aa:224e]
            Kernel driver in use: intel_ish_ipc
    00:14.0 USB controller [0c03]: Intel Corporation Sunrise Point-LP USB 3.0 xHCI Controller [8086:9d2f] (rev 21)
            Subsystem: Lenovo Sunrise Point-LP USB 3.0 xHCI Controller [17aa:224e]
            Kernel driver in use: xhci_hcd
    00:14.2 Signal processing controller [1180]: Intel Corporation Sunrise Point-LP Thermal subsystem [8086:9d31] (rev 21)
            Subsystem: Lenovo Sunrise Point-LP Thermal subsystem [17aa:224e]
    00:15.0 Signal processing controller [1180]: Intel Corporation Sunrise Point-LP Serial IO I2C Controller #0 [8086:9d60] (rev 21)
            Subsystem: Lenovo Sunrise Point-LP Serial IO I2C Controller [17aa:224e]
    00:16.0 Communication controller [0780]: Intel Corporation Sunrise Point-LP CSME HECI #1 [8086:9d3a] (rev 21)
            Subsystem: Lenovo Sunrise Point-LP CSME HECI [17aa:224e]
            Kernel driver in use: mei_me
    00:1c.0 PCI bridge [0604]: Intel Corporation Sunrise Point-LP PCI Express Root Port #1 [8086:9d10] (rev f1)
            Kernel driver in use: pcieport
    00:1c.2 PCI bridge [0604]: Intel Corporation Sunrise Point-LP PCI Express Root Port #3 [8086:9d12] (rev f1)
            Kernel driver in use: pcieport
    00:1c.4 PCI bridge [0604]: Intel Corporation Sunrise Point-LP PCI Express Root Port #5 [8086:9d14] (rev f1)
            Kernel driver in use: pcieport
    00:1d.0 PCI bridge [0604]: Intel Corporation Sunrise Point-LP PCI Express Root Port #9 [8086:9d18] (rev f1)
            Kernel driver in use: pcieport
    00:1f.0 ISA bridge [0601]: Intel Corporation Sunrise Point LPC Controller/eSPI Controller [8086:9d4e] (rev 21)
            Subsystem: Lenovo Sunrise Point LPC Controller/eSPI Controller [17aa:224e]
    00:1f.2 Memory controller [0580]: Intel Corporation Sunrise Point-LP PMC [8086:9d21] (rev 21)
            Subsystem: Lenovo Sunrise Point-LP PMC [17aa:224e]
    00:1f.3 Audio device [0403]: Intel Corporation Sunrise Point-LP HD Audio [8086:9d71] (rev 21)
            Subsystem: Lenovo Sunrise Point-LP HD Audio [17aa:224e]
            Kernel driver in use: snd_hda_intel
            Kernel modules: snd_hda_intel
    00:1f.4 SMBus [0c05]: Intel Corporation Sunrise Point-LP SMBus [8086:9d23] (rev 21)
            Subsystem: Lenovo Sunrise Point-LP SMBus [17aa:224e]
            Kernel driver in use: i801_smbus
            Kernel modules: i2c_i801
    00:1f.6 Ethernet controller [0200]: Intel Corporation Ethernet Connection (4) I219-LM [8086:15d7] (rev 21)
            Subsystem: Lenovo Ethernet Connection (4) I219-LM [17aa:224e]
            Kernel driver in use: e1000e
    02:00.0 Unassigned class [ff00]: Realtek Semiconductor Co., Ltd. RTS525A PCI Express Card Reader [10ec:525a] (rev 01)
            Subsystem: Lenovo RTS525A PCI Express Card Reader [17aa:224e]
            Kernel driver in use: rtsx_pci
    04:00.0 Network controller [0280]: Intel Corporation Wireless 8265 / 8275 [8086:24fd] (rev 88)
            Subsystem: Intel Corporation Wireless 8265 / 8275 [8086:0130]
            Kernel driver in use: iwlwifi
            Kernel modules: iwlwifi
    05:00.0 Non-Volatile memory controller [0108]: Lenovo Device [17aa:0004]
            Subsystem: Lenovo Device [17aa:1004]
            Kernel driver in use: nvme
    06:00.0 PCI bridge [0604]: Intel Corporation JHL6540 Thunderbolt 3 Bridge (C step) [Alpine Ridge 4C 2016] [8086:15d3] (rev 02)
            Kernel driver in use: pcieport
    07:00.0 PCI bridge [0604]: Intel Corporation JHL6540 Thunderbolt 3 Bridge (C step) [Alpine Ridge 4C 2016] [8086:15d3] (rev 02)
            Kernel driver in use: pcieport
    07:01.0 PCI bridge [0604]: Intel Corporation JHL6540 Thunderbolt 3 Bridge (C step) [Alpine Ridge 4C 2016] [8086:15d3] (rev 02)
            Kernel driver in use: pcieport
    07:02.0 PCI bridge [0604]: Intel Corporation JHL6540 Thunderbolt 3 Bridge (C step) [Alpine Ridge 4C 2016] [8086:15d3] (rev 02)
            Kernel driver in use: pcieport
    07:04.0 PCI bridge [0604]: Intel Corporation JHL6540 Thunderbolt 3 Bridge (C step) [Alpine Ridge 4C 2016] [8086:15d3] (rev 02)
            Kernel driver in use: pcieport
    08:00.0 System peripheral [0880]: Intel Corporation JHL6540 Thunderbolt 3 NHI (C step) [Alpine Ridge 4C 2016] [8086:15d2] (rev 02)
            Subsystem: Device [2222:1111]
            Kernel driver in use: thunderbolt
    09:00.0 PCI bridge [0604]: Intel Corporation JHL6540 Thunderbolt 3 Bridge (C step) [Alpine Ridge 4C 2016] [8086:15d3] (rev 02)
            Kernel driver in use: pcieport
    0a:00.0 PCI bridge [0604]: Intel Corporation JHL6540 Thunderbolt 3 Bridge (C step) [Alpine Ridge 4C 2016] [8086:15d3] (rev 02)
            Kernel driver in use: pcieport
    0a:01.0 PCI bridge [0604]: Intel Corporation JHL6540 Thunderbolt 3 Bridge (C step) [Alpine Ridge 4C 2016] [8086:15d3] (rev 02)
            Kernel driver in use: pcieport
    0a:02.0 PCI bridge [0604]: Intel Corporation JHL6540 Thunderbolt 3 Bridge (C step) [Alpine Ridge 4C 2016] [8086:15d3] (rev 02)
            Kernel driver in use: pcieport
    0a:03.0 PCI bridge [0604]: Intel Corporation JHL6540 Thunderbolt 3 Bridge (C step) [Alpine Ridge 4C 2016] [8086:15d3] (rev 02)
            Kernel driver in use: pcieport
    0a:04.0 PCI bridge [0604]: Intel Corporation JHL6540 Thunderbolt 3 Bridge (C step) [Alpine Ridge 4C 2016] [8086:15d3] (rev 02)
            Kernel driver in use: pcieport
    0b:00.0 USB controller [0c03]: Fresco Logic FL1100 USB 3.0 Host Controller [1b73:1100] (rev 10)
            Subsystem: Device [17ef:3067]
            Kernel driver in use: xhci_hcd
    0d:00.0 USB controller [0c03]: Fresco Logic FL1100 USB 3.0 Host Controller [1b73:1100] (rev 10)
            Subsystem: Device [17ef:3068]
            Kernel driver in use: xhci_hcd

`root `[`#`]`lsusb`

    Bus 006 Device 002: ID 17ef:3069 Lenovo
    Bus 006 Device 001: ID 1d6b:0003 Linux Foundation 3.0 root hub
    Bus 005 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub
    Bus 004 Device 001: ID 1d6b:0003 Linux Foundation 3.0 root hub
    Bus 003 Device 003: ID 17ef:3066 Lenovo
    Bus 003 Device 002: ID 17ef:306a Lenovo
    Bus 003 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub
    Bus 002 Device 001: ID 1d6b:0003 Linux Foundation 3.0 root hub
    Bus 001 Device 005: ID 138a:0097 Validity Sensors, Inc.
    Bus 001 Device 004: ID 04f2:b5ce Chicony Electronics Co., Ltd Integrated Camera
    Bus 001 Device 003: ID 8087:0a2b Intel Corp.
    Bus 001 Device 007: ID 1199:9079 Sierra Wireless, Inc.
    Bus 001 Device 006: ID 056a:50b8 Wacom Co., Ltd
    Bus 001 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub

`root `[`#`]`lsusb -t`

    /:  Bus 06.Port 1: Dev 1, Class=root_hub, Driver=xhci_hcd/4p, 5000M
        |__ Port 1: Dev 2, If 0, Class=Vendor Specific Class, Driver=r8152, 5000M
    /:  Bus 05.Port 1: Dev 1, Class=root_hub, Driver=xhci_hcd/4p, 480M
    /:  Bus 04.Port 1: Dev 1, Class=root_hub, Driver=xhci_hcd/4p, 5000M
    /:  Bus 03.Port 1: Dev 1, Class=root_hub, Driver=xhci_hcd/4p, 480M
        |__ Port 1: Dev 2, If 2, Class=Audio, Driver=snd-usb-audio, 12M
        |__ Port 1: Dev 2, If 0, Class=Audio, Driver=snd-usb-audio, 12M
        |__ Port 1: Dev 2, If 3, Class=Human Interface Device, Driver=usbhid, 12M
        |__ Port 1: Dev 2, If 1, Class=Audio, Driver=snd-usb-audio, 12M
        |__ Port 4: Dev 3, If 0, Class=Human Interface Device, Driver=usbhid, 12M
    /:  Bus 02.Port 1: Dev 1, Class=root_hub, Driver=xhci_hcd/6p, 5000M
    /:  Bus 01.Port 1: Dev 1, Class=root_hub, Driver=xhci_hcd/12p, 480M
        |__ Port 6: Dev 7, If 12, Class=Communications, Driver=cdc_mbim, 480M
        |__ Port 6: Dev 7, If 13, Class=CDC Data, Driver=cdc_mbim, 480M
        |__ Port 7: Dev 3, If 0, Class=Wireless, Driver=btusb, 12M
        |__ Port 7: Dev 3, If 1, Class=Wireless, Driver=btusb, 12M
        |__ Port 8: Dev 4, If 1, Class=Video, Driver=uvcvideo, 480M
        |__ Port 8: Dev 4, If 0, Class=Video, Driver=uvcvideo, 480M
        |__ Port 9: Dev 5, If 0, Class=Vendor Specific Class, Driver=, 12M
        |__ Port 10: Dev 6, If 0, Class=Human Interface Device, Driver=usbhid, 12M
        |__ Port 10: Dev 6, If 1, Class=Human Interface Device, Driver=usbhid, 12M

### [Device Table]

  ----------------------------- ------------------------------------------------------------ ------------- ------------------------ ----------------------------------------------------------- -------------------------------------------------------------
  Device                        Make/model                                                   Status        Vendor ID / Product ID   Kernel driver(s)                                            Notes
  VGA compatible controller     Intel Corporation HD Graphics 620                            Works         ---                      i915                                                        ---
  Ethernet network controller   Intel Corporation Ethernet Connection (4) I219-LM (rev 21)   Works         8086:15d7                e1000e                                                      ---
  Wireless network controller   Intel Corporation Wireless 8265 / 8275 (rev 88)              Works         8086:24fd                [iwlwifi](https://wiki.gentoo.org/wiki/Iwlwifi "Iwlwifi")   ---
  Bluetooth                     Intel Corporation Wireless                                   Works         8087:0a2b                btusb                                                       ---
  Touchscreen                   Wacom Serial Pen and Multitouch Sensor                       Works         056a:50b8                usbhid                                                      ---
  Card Reader                   Realtek RTS525A PCI Express Card Reader                      Works         10ec:525a                rtsx_pci                                                    ---
  Audio device                  Intel Corporation Sunrise Point-LP HD Audio                  Works         ---                      snd_hda_intel                                               ---
  Integrated Webcam             Chicony Electronics Co.,Ltd. Webcam                          Works         04f2:b5ce                uvcvideo                                                    ---
  Thunderbolt                   Intel Corporation JHL6540 Thunderbolt 3 NHI                  Works         2222:1111                thunderbolt                                                 ---
  NVME Disk                     Lenovo Device                                                Works         ---                      [nvme](https://wiki.gentoo.org/wiki/NVMe "NVMe")            ---
  Fingerprint reader            Validity Sensors, Inc. Fingerprint Sensor                    Not tested    138a:0097                ---                                                         ---
  WWAN & GPS                    Sierra Wireless EM7455 Qualcomm Snapdragon X7 LTE-A          Works         1199:9079                cdc_mbim                                                    ---
  NFC                           Foxconn T77H747 NXP NPC300 (PN548)                           Not tested    ---                      nxp_nci_i2c                                                 connected through i2c (listed in ACPI DSDT as NFC1 NXP1001)
  Thunderbolt 3 Dock Ethernet   Realtek RTL8152 USB Ethernet Adapter                         Works         17ef:3069                r8152                                                       ---
  Thunderbolt 3 Dock Audio      ThinkPad Thunderbolt 3 Dock USB Audio                        Works         17ef:306a                snd_usb_audio                                               ---
  ----------------------------- ------------------------------------------------------------ ------------- ------------------------ ----------------------------------------------------------- -------------------------------------------------------------

## [Installation]

Apply the additional lines below to the }file of Portage.

** Note**\
To get up-to-date CPU_FLAGS_X86, discover the flags for your CPU with `cpuid2cpuflags`!

[FILE] **`/etc/portage/package.use/00video`**

    */* VIDEO_CARDS: -* intel i965

[FILE] **`/etc/portage/package.use/00input`**

    */* INPUT_DEVICES: libinput wacom

[FILE] **`/etc/portage/package.use/00cpu-flags`**

    # for i7-7600U
    */* CPU_FLAGS_X86: aes avx avx2 fma3 mmx mmxext pclmul popcnt sse sse2 sse3 sse4_1 sse4_2 ssse3

    # for i5-7300U
    */* CPU_FLAGS_X86: aes avx avx2 f16c fma3 mmx mmxext pclmul popcnt sse sse2 sse3 sse4_1 sse4_2 ssse3

[FILE] **`/etc/portage/package.use/00grub`**

    */* GRUB_PLATFORMS: efi-64

Then you should update the world to recompile all installed packages with the new flags.

`root `[`#`]`emerge --ask --changed-use --deep @world`

### [Firmware]

Install the package [[[sys-kernel/linux-firmware]](https://packages.gentoo.org/packages/sys-kernel/linux-firmware)[]] which contains the wifi device driver.

`root `[`#`]`emerge --ask sys-kernel/linux-firmware`

### [Kernel]

[KERNEL] **NVME SSD**

    Device Drivers  --->
       <*>  NVM Express block device

[KERNEL] **ACPI**

    Generic Driver Options  --->
       [*] X86 Platform Specific Device Drivers  --->
          <*>   ThinkPad ACPI Laptop Extras
          [*]     Console audio control ALSA interface
          [ ]     Maintainer debug facilities
          [ ]     Verbose debug mode
          [ ]     Allow control of important LEDs (unsafe)
          [*]     Video output control support
          [*]     Support NVRAM polling for hot keys

    Device Drivers  --->
       Pin controllers (PINCTRL [=y])  --->
          Intel pinctrl drivers  --->
             <*> Intel Sunrisepoint pinctrl and GPIO driver

[KERNEL] **Ethernet controller**

    Generic Driver Options  --->
       [*] Network device support  ---
          [*]   Ethernet driver support  --->
             [*]   Intel devices
             <*>     Intel(R) PRO/1000 PCI-Express Gigabit Ethernet support

\
Building the following device driver as module may be appropriate as it requires firmware during initialization.

[KERNEL] **Wireless network controller**

    Generic Driver Options  --->
       [*] Network device support  ---
          [*]   Wireless LAN  --->
             [*]   Intel devices
             <M>     Intel Wireless WiFi Next Gen AGN - Wireless-N/Advanced-N/Ultimate-N (iwlwifi)
             <M>       Intel Wireless WiFi MVM Firmware support

[KERNEL] **Audio device**

    Generic Driver Options  --->
       <*> Sound card support  --->
          <*>   Advanced Linux Sound Architecture  --->
             [*]   PCI sound devices  --->
                   HD-Audio  --->
                      <*> HD Audio PCI
                      <*> Build Conexant HD-audio codec support

[KERNEL] **Bluetooth**

    -*- Networking support  --->
       <*>   Bluetooth subsystem support  --->
                Bluetooth device drivers  --->
                   <*> HCI USB driver
                   [*]   Broadcom protocol support

[KERNEL] **Touchscreen**

    No special options needed.

[KERNEL] **USB 3.0 & USB-C**

    USB_PCI=y
    USB_OTG=y
    USB_XHCI_HCD=y
    USB_STORAGE=y
    TYPEC=y
    TYPEC_UCSI=y

[KERNEL] **PCIe Card reader**

    MISC_RTSX_PCI=y
    MMC_REALTEK_PCI=y
    MMC_SDHCI=y

[KERNEL] **Integrated Sensor Hub**

    INTEL_ISH_HID=y

[KERNEL] **Thunderbolt Dock**

    THUNDERBOLT=y
    THUNDERBOLT_NET=y
    HOTPLUG_PCI_PCIE=y
    HOTPLUG_PCI=y
    HOTPLUG_PCI_ACPI=y
    USB_USBNET=y         # dock's network card
    USB_NET_CDCETHER=y   # "
    USB_RTL8152=y        # "
    SND_USB_AUDIO=y      # dock's usb-audio

### [Emerge]

Fingerprint reader is recognized by the following library.

`root `[`#`]`emerge --ask sys-auth/libfprint`

## [Configuration]

(Explain any additional configuration or special customization for this hardware platform. Could be anything from BIOS settings to assigning proper media key functionality.)

### [][Finger/Pen Input]

For [X11](https://wiki.gentoo.org/wiki/X11 "X11") to work with finger/pen input, pull in [[[x11-drivers/xf86-input-wacom]](https://packages.gentoo.org/packages/x11-drivers/xf86-input-wacom)[]] by inserting `wacom` argument into the indicated variable in the file shown below and run the following command for the configuration to emerge.

[FILE] **`/etc/portage/make.conf`**

    INPUT_DEVICES="... wacom"

`root `[`#`]`emerge --ask --deep --newuse @world`

### [Trackpoint scrolling]

Add the following Xorg configuration file so that the driver is selected for the devices we want.

[FILE] **`/etc/X11/xorg.conf.d/90-libinput.conf`**

    Section "InputClass"
            Identifier "libinput pointer catchall"
            MatchIsPointer "on"
            MatchDevicePath "/dev/input/event*"
            Driver "libinput"
    EndSection

    Section "InputClass"
            Identifier "libinput touchpad catchall"
            MatchIsTouchpad "on"
            MatchDevicePath "/dev/input/event*"
            Driver "libinput"
    EndSection

After a reboot/xorg-server restart, trackpoint scrolling should work.

### [Hotkeys]

Most of the hotkeys are available and can be configured by an X hotkey daemon like [[[x11-misc/sxhkd]](https://packages.gentoo.org/packages/x11-misc/sxhkd)[]].

** Note**\
The Audio example functions only work if using [PulseAudio](https://wiki.gentoo.org/wiki/PulseAudio "PulseAudio").

  -------------- -------------------------- -------------------------------------------- ---------------------------------------------- --------------------------------------
  Function key   Function name              Macro                                        Example function                               Notes
  F1             Mute audio                 XF86AudioMute                                pactl set-sink-mute 0 toggle                   The LED works as well.
  F2, F3         Volume -/+                 XF86AudioLowerVolume, XF86AudioRaiseVolume   pactl set-sink-volume 0 -/+5%                  ---
  F4             Mute microphone            XF86AudioMicMute                             pactl set-source-mute 1 toggle                 The LED works as well.
  F5, F6         Brightness -/+             XF86MonBrightnessDown, XF86MonBrightnessUp   xbacklight -dec 5 / xbacklight -inc 5          ---
  F7             Recognize Monitors         XF86Display                                  xrandr \--output HDMI1 \--auto \--below eDP1   ---
  F8             Enable/Disable Wifi        XF86WLAN                                     ---                                            Works without any additional config.
  F9             Settings / Tools           XF86Tools                                    ---                                            ---
  F10            Enable/Disable Bluetooth   XF86Bluetooth                                ---                                            Works without any additional config.
  F11            Switch Keyboard layout     Not working                                  ---                                            ---
  F12            Set Bookmark               Not Working                                  ---                                            ---
  -------------- -------------------------- -------------------------------------------- ---------------------------------------------- --------------------------------------

## [Updates]

### [fwupd]

Firmware of the X1 Yoga 2nd can be updated with [fwupd](https://wiki.gentoo.org/wiki/Fwupd "Fwupd"): [https://fwupd.org/lvfs/device/9ca89fa5-ce05-47ac-bdf3-5b0b6f21d07a](https://fwupd.org/lvfs/device/9ca89fa5-ce05-47ac-bdf3-5b0b6f21d07a)

You need to build [fwupd](https://wiki.gentoo.org/wiki/Fwupd "Fwupd") with the `uefi` useflag (and boot with UEFI).

### [][BIOS/UEFI]

You can use [fwupd](#fwupd) to update the BIOS and other firmware. As an alternative, you can update the X1 Yoga BIOS/UEFI from Linux with an **USB drive**.

-   [Download the .iso](https://pcsupport.lenovo.com/de/en/products/LAPTOPS-AND-NETBOOKS/THINKPAD-X-SERIES-LAPTOPS/THINKPAD-X1-YOGA-TYPE-20JD-20JE-20JF-20JG/downloads/DS121064)
-   Extract the bootable image with [[[app-cdr/geteltorito]](https://packages.gentoo.org/packages/app-cdr/geteltorito)[]]

`user `[`$`]`geteltorito -o image.bin downloaded.iso`

-   Flash the raw image to USB drive, make sure it\'s the right device\...

`root `[`#`]`dd if=image.bin of=/dev/sdx`

-   Boot from the USB drive and install the update

### [Thunderbolt Firmware]

You can update the Lenovo Thunderbolt Firmware right from Linux very easily!

-   [Download the installation .exe](https://pcsupport.lenovo.com/de/en/products/laptops-and-netbooks/thinkpad-x-series-laptops/thinkpad-x1-yoga-type-20jd-20je-20jf-20jg/downloads/ds121630)
-   Run this program with [Wine](https://wiki.gentoo.org/wiki/Wine "Wine") to extract its components, relevant is `TBT.bin`

View the current firmware version:

`root `[`#`]`cat /sys/bus/thunderbolt/devices/0-0/nvm_version`

    15.0

Upload the update:

`root `[`#`]`dd if=/tmp/Thunderbolt/TBT.bin of=/sys/bus/thunderbolt/devices/0-0/nvm_non_active0/nvmem`

    496+0 records in
    496+0 records out
    253952 bytes (254 kB, 248 KiB) copied, 0.00235085 s, 108 MB/s

Trigger the update:

`root `[`#`]`echo 1 > /sys/bus/thunderbolt/devices/0-0/nvm_authenticate`

The screen may flicker and hang, just wait a bit (\<20s). Now you should have a newer version!

`root `[`#`]`cat /sys/bus/thunderbolt/devices/0-0/nvm_version`

    27.0

\

### [Thunderbolt Dock Firmware]

From Linux, you can update the firmware of the USB-C Dock itself with [Wine](https://wiki.gentoo.org/wiki/Wine "Wine")!

-   [Download the windows .exe](https://pcsupport.lenovo.com/de/en/products/LAPTOPS-AND-NETBOOKS/THINKPAD-X-SERIES-LAPTOPS/THINKPAD-X1-YOGA-TYPE-20JD-20JE-20JF-20JG/downloads/DS501903)
-   Run it with [Wine](https://wiki.gentoo.org/wiki/Wine "Wine") and click the **Check current FW** and **Update FW** buttons.

`user `[`$`]`wine thinkpad_usb_c_dock_firmware.exe`

                  ThinkPad USB-C Dock FW Utility v3.7
       Package including(BB:0.1.0.23 HX3:1.14.7.183 DK:1.3.40 DP:3.12.005)
    ========================================================================
    Update date:Sat 04/22/2017
    Update time:02:36 PM

    Checking current Dock FW version
    BillBoard Version: 0.1.0.23
    Hx3 Version: 1.14.7.183
    CCG4 Version: 1.3.40
    DP Hub FW: 3.12.005

    Current Dock FW is newer, no need to update.