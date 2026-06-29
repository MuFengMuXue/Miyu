[] This article has been flagged for not conforming to the [wiki guidelines](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Guidelines "Gentoo Wiki:Guidelines"). Please [help Gentoo out](https://wiki.gentoo.org/wiki/Help_improve_Gentoo_by_getting_involved_with_documentation!#Make_articles_conform_to_the_guidelines "Help improve Gentoo by getting involved with documentation!") by starting fixing things.

**Resources**

[[]][Official Support Page](https://pcsupport.lenovo.com/us/en/products/laptops-and-netbooks/yoga-series/yoga-900-13isk)

[[]][Specifications](https://psref.lenovo.com/syspool/Sys/PDF/Lenovo_Laptops/Lenovo_YOGA_900_13/Lenovo_YOGA_900_13_Spec.PDF)

[[]][Specifications (by region)](https://psref.lenovo.com/Product/Yoga/Lenovo_YOGA_900_13)

[[]][Hardware Maintenance Manual](https://download.lenovo.com/consumer/mobiles_pub/yoga_900-13isk_hmm_201509.pdf)

[[]][User Guide](https://download.lenovo.com/consumer/mobiles_pub/yoga_900-13isk_ug_en_201602.pdf)

[[]][Yoga 900](https://en.wikipedia.org/wiki/Lenovo_Yoga#Yoga_900 "wikipedia:Lenovo Yoga")

Still working on installation, wiki will come soon.

## Contents

-   [[1] [Hardware Lenovo Yoga 900-13ISK]](#Hardware_Lenovo_Yoga_900-13ISK)
    -   [[1.1] [Laptop Specifications]](#Laptop_Specifications)
        -   [[1.1.1] [Forum]](#Forum)
-   [[2] [Configuration details]](#Configuration_details)
    -   [[2.1] [host bridge]](#host_bridge)
    -   [[2.2] [Graphics]](#Graphics)
    -   [[2.3] [pcie bus]](#pcie_bus)
    -   [[2.4] [USB Bus]](#USB_Bus)
    -   [[2.5] [SMBus]](#SMBus)
    -   [[2.6] [ISA bus]](#ISA_bus)
    -   [[2.7] [Power Management Controler]](#Power_Management_Controler)
    -   [[2.8] [SATA SSD]](#SATA_SSD)
    -   [[2.9] [Display]](#Display)
    -   [[2.10] [Wireless]](#Wireless)
        -   [[2.10.1] [Method 1: Using the kernel driver]](#Method_1:_Using_the_kernel_driver)
            -   [[2.10.1.1] [Configure and compile kernel]](#Configure_and_compile_kernel)
            -   [[2.10.1.2] [Install firmware package]](#Install_firmware_package)
    -   [[2.11] [sound]](#sound)
    -   [[2.12] [bluetooth]](#bluetooth)
    -   [[2.13] [misc]](#misc)
    -   [[2.14] [Touchpad and TouchScreen]](#Touchpad_and_TouchScreen)
    -   [[2.15] [SD card]](#SD_card)
    -   [[2.16] [webcam]](#webcam)
    -   [[2.17] [HEVC]](#HEVC)
    -   [[2.18] [driver summary]](#driver_summary)
-   [[3] [External resources]](#External_resources)

## [Hardware Lenovo Yoga 900-13ISK]

on linux-5.3.9 kernel

### [Laptop Specifications]

+:-------------------------------------------------:+:------------------------------------------------:+:---------------:+:-----------------------------------------------------------------------------------------------------------------------------------------:+
| Device                                            | Model                                            | Works           | Notes                                                                                                                                     |
+---------------------------------------------------+--------------------------------------------------+-----------------+-------------------------------------------------------------------------------------------------------------------------------------------+
| Intel® Core™ i7                                   | Intel Core i7 (6th Gen) 6500U / 2.5 GHz          | Yes             |                                                                                                                                           |
+---------------------------------------------------+--------------------------------------------------+-----------------+-------------------------------------------------------------------------------------------------------------------------------------------+
| Intel® HD Graphics                                | 520                                              | Yes             | by default i915 driver will be used, need USE change to use i965 idriver instead See [Intel](https://wiki.gentoo.org/wiki/Intel "Intel"). |
+---------------------------------------------------+--------------------------------------------------+-----------------+-------------------------------------------------------------------------------------------------------------------------------------------+
| samsung 13.3\"3200×1800 touchscreen               | Wide QXGA+ (WQXGA+) 3200×1800, 16:9 aspect ratio | Yes             | intel_backlight works, PPI of 276.05                                                                                                      |
+---------------------------------------------------+--------------------------------------------------+-----------------+-------------------------------------------------------------------------------------------------------------------------------------------+
| Wireless Intel Corporation Wireless 8260 (rev 3a) |                                                  | Yes             |                                                                                                                                           |
+---------------------------------------------------+--------------------------------------------------+-----------------+-------------------------------------------------------------------------------------------------------------------------------------------+
| Bluetooth                                         |                                                  | Yes             |                                                                                                                                           |
+---------------------------------------------------+--------------------------------------------------+-----------------+-------------------------------------------------------------------------------------------------------------------------------------------+
| Sound                                             |                                                  | Yes             |                                                                                                                                           |
+---------------------------------------------------+--------------------------------------------------+-----------------+-------------------------------------------------------------------------------------------------------------------------------------------+
| Camera                                            |                                                  | Yes             |                                                                                                                                           |
+---------------------------------------------------+--------------------------------------------------+-----------------+-------------------------------------------------------------------------------------------------------------------------------------------+
| Card Reader                                       |                                                  | Partial         | :::                                                            |
|                                                   |                                                  |                 | ** Note**\                                                                                                                                |
|                                                   |                                                  |                 | a patch is needed for micro sd \>= 256G \*see below\*                                                                                     |
|                                                   |                                                  |                 | :::                                                                                                                                       |
|                                                   |                                                  |                 |                                                                                                                                           |
|                                                   |                                                  |                 | :::                                                            |
|                                                   |                                                  |                 | ** Note**\                                                                                                                                |
|                                                   |                                                  |                 | sdcard performance are good                                                                                                               |
|                                                   |                                                  |                 |                                                                                                                                           |
|                                                   |                                                  |                 |     dd if=/dev/urandom of=/media/mmc/test bs=30M count=10                                                                                 |
|                                                   |                                                  |                 |     10+0 records in                                                                                                                       |
|                                                   |                                                  |                 |     10+0 records out                                                                                                                      |
|                                                   |                                                  |                 |     314572800 bytes (315 MB, 300 MiB) copied, 2.02639 s, 155 MB/s                                                                         |
|                                                   |                                                  |                 | :::                                                                                                                                       |
+---------------------------------------------------+--------------------------------------------------+-----------------+-------------------------------------------------------------------------------------------------------------------------------------------+
| Touchscreen                                       |                                                  | Yes             | multitouch ok                                                                                                                             |
+---------------------------------------------------+--------------------------------------------------+-----------------+-------------------------------------------------------------------------------------------------------------------------------------------+
| Touchpad                                          |                                                  | Yes             | some multitouch support (two finger scrolling ok) monotouch ok, left and right click ok, touch click ok                                   |
+---------------------------------------------------+--------------------------------------------------+-----------------+-------------------------------------------------------------------------------------------------------------------------------------------+

#### [Forum]

see [https://forums.gentoo.org/viewtopic-p-8223726.html#8223726](https://forums.gentoo.org/viewtopic-p-8223726.html#8223726) for intallation discussion

## [Configuration details]

### [host bridge]

`root `[`#`]`lspci -nn -k`

    00:00.0 Host bridge [0600]: Intel Corporation Xeon E3-1200 v5/E3-1500 v5/6th Gen Core Processor Host Bridge/DRAM Registers [8086:1904] (rev 08)
        Subsystem: Lenovo Xeon E3-1200 v5/E3-1500 v5/6th Gen Core Processor Host Bridge/DRAM Registers [17aa:3800]
        Kernel driver in use: skl_uncore

[KERNEL]

    .config - Linux/x86 4.9.95-gentoo Kernel Configuration
     →

### [Graphics]

`root `[`#`]`lspci -nn -k`

    00:02.0 VGA compatible controller [0300]: Intel Corporation HD Graphics 520 [8086:1916] (rev 07)
        Subsystem: Lenovo HD Graphics 520 [17aa:3800]
        Kernel driver in use: i915

[KERNEL]

    .config - Linux/x86 4.9.95-gentoo Kernel Configuration
     →

See [Intel](https://wiki.gentoo.org/wiki/Intel "Intel").

See [\[1\]](https://forums.gentoo.org/viewtopic-p-8538508.html#8538508) for video decoding hardware acceleration

### [pcie bus]

`root `[`#`]`lspci -nn -k`

    00:1c.0 PCI bridge [0604]: Intel Corporation Sunrise Point-LP PCI Express Root Port #5 [8086:9d14] (rev f1)
        Kernel driver in use: pcieport
    00:1c.5 PCI bridge [0604]: Intel Corporation Sunrise Point-LP PCI Express Root Port #6 [8086:9d15] (rev f1)
        Kernel driver in use: pcieport

[KERNEL]

    .config - Linux/x86 4.9.95-gentoo Kernel Configuration
     →

### [USB Bus]

`root `[`#`]`lspci -nn -k`

    00:14.0 USB controller [0c03]: Intel Corporation Sunrise Point-LP USB 3.0 xHCI Controller [8086:9d2f] (rev 21)
        Subsystem: Lenovo Sunrise Point-LP USB 3.0 xHCI Controller [17aa:3800]
        Kernel driver in use: xhci_hcd

[KERNEL]

    .config - Linux/x86 4.9.95-gentoo Kernel Configuration
     →

### [SMBus]

`root `[`#`]`lspci -nn -k`

    00:1f.4 SMBus [0c05]: Intel Corporation Sunrise Point-LP SMBus [8086:9d23] (rev 21)
        Subsystem: Lenovo Sunrise Point-LP SMBus [17aa:3800]
        Kernel driver in use: i801_smbus
        Kernel modules: i2c_i801

[KERNEL]

    .config - Linux/x86 4.9.95-gentoo Kernel Configuration
     →

### [ISA bus]

`root `[`#`]`lspci -nn -k`

    00:1f.0 ISA bridge [0601]: Intel Corporation Sunrise Point-LP LPC Controller [8086:9d48] (rev 21)
        Subsystem: Lenovo Sunrise Point-LP LPC Controller [17aa:3800]

[KERNEL]

    .config - Linux/x86 4.9.95-gentoo Kernel Configuration
     →

### [Power Management Controler]

`root `[`#`]`lspci -nn -k`

    00:04.0 Signal processing controller [1180]: Intel Corporation Xeon E3-1200 v5/E3-1500 v5/6th Gen Core Processor Thermal Subsystem [8086:1903] (rev 08)
        Subsystem: Lenovo Xeon E3-1200 v5/E3-1500 v5/6th Gen Core Processor Thermal Subsystem [17aa:3800]
    00:14.2 Signal processing controller [1180]: Intel Corporation Sunrise Point-LP Thermal subsystem [8086:9d31] (rev 21)
        Subsystem: Lenovo Sunrise Point-LP Thermal subsystem [17aa:3800]
    00:1f.2 Memory controller [0580]: Intel Corporation Sunrise Point-LP PMC [8086:9d21] (rev 21)
        Subsystem: Lenovo Sunrise Point-LP PMC [17aa:3800]

[KERNEL]

    .config - Linux/x86 4.9.95-gentoo Kernel Configuration
    → Device Drivers → Generic Thermal sysfs driver → ACPI INT340X thermal drivers
    <M> ACPI INT340X thermal drivers
    <M> ACPI INT3406 display thermal driver
     → Device Drivers → Generic Thermal sysfs driver
    <M>   Intel PCH Thermal Reporting Driver
     → Device Drivers → X86 Platform Specific Device Drivers
    [*]   Intel PMC Core driver

### [SATA SSD]

`root `[`#`]`lspci -nn -k`

    00:17.0 SATA controller [0106]: Intel Corporation Sunrise Point-LP SATA Controller [AHCI mode] [8086:9d03] (rev 21)
        Subsystem: Lenovo Sunrise Point-LP SATA Controller [AHCI mode] [17aa:3800]
        Kernel driver in use: ahci

[KERNEL]

    .config - Linux/x86 4.9.95-gentoo Kernel Configuration
     →

** Note**\
some issue when formating with ext4 with `inline_data`

** Note**\
formating with `has_journal,extent,huge_file,flex_bg,uninit_bg,64bit,dir_nlink,extra_isize` seems to not create issues with mount options `rw,noatime,defaults,errors=remount-ro`

\

### [Display]

Backlight control through brightness buttons works without modification on X screen resolution is a little bit tricky to tune

`root `[`#`]`cat /etc/X11/xorg.conf.d/90-monitor`

    Section "Monitor"
        Identifier             "Monitor-eDP-1"
        DisplaySize            293 165    # In millimeters
    EndSection

`root `[`#`]`cat .xinitrc `

    xrandr  --dpi 192
    xrdb -merge ~/.Xresources
    xinput set-prop "Synaptics TM3066-002" "Synaptics Palm Detection" 1
    xinput set-prop "Synaptics TM3066-002" "Synaptics Palm Dimensions" 5, 5
    #exec ck-launch-session dbus-launch --sh-syntax --exit-with-session xfce4-session
    exec ck-launch-session dbus-launch --sh-syntax --exit-with-session fluxbox

`root `[`#`]`cat .Xresources `

    Xft.dpi: 144
    Xft.autohint: 0
    Xft.lcdfilter:  lcddefault
    Xft.hintstyle:  hintfull
    Xft.hinting: 1
    Xft.antialias: 1
    Xft.rgba: rgb

In xfce-\>settings-\>appearance-\>fonts, set custom DPI to 140 see [https://wiki.archlinux.org/index.php/Xorg#Display_size_and_DPI](https://wiki.archlinux.org/index.php/Xorg#Display_size_and_DPI) for more settings on DPI especially for gtk3 based app

### [Wireless]

#### [Method 1: Using the kernel driver]

##### [Configure and compile kernel]

`root `[`#`]`lspci -nn -k`

    01:00.0 Network controller [0280]: Intel Corporation Wireless 8260 [8086:24f3] (rev 3a)
        Subsystem: Intel Corporation Wireless 8260 [8086:1130]
        Kernel driver in use: iwlwifi
        Kernel modules: iwlwifi

[KERNEL]

    .config - Linux/x86 4.9.95-gentoo Kernel Configuration
     → Device Drivers → Network device support → Wireless LAN

    <M>     Intel Wireless WiFi Next Gen AGN - Wireless-N/Advanced-N/Ultimate-N (iwlwifi)
          <M>       Intel Wireless WiFi DVM Firmware support
          <M>       Intel Wireless WiFi MVM Firmware support
          [ ]       Enable broadcast filtering (NEW)
          [*]       Enable runtime power management mode for PCIe devices
          Debugging Options  --->

** Note**\
rfkill: exports duplicate symbol rfkill_alloc (owned by kernel)

##### [Install firmware package]

`root `[`#`]`emerge --ask sys-kernel/linux-firmware`

### [sound]

`root `[`#`]`lspci -nn -k`

    00:1f.3 Audio device [0403]: Intel Corporation Sunrise Point-LP HD Audio [8086:9d70] (rev 21)
        Subsystem: Lenovo Sunrise Point-LP HD Audio [17aa:3800]
        Kernel driver in use: snd_hda_intel
        Kernel modules: snd_hda_intel, snd_soc_skl

[KERNEL]

    .config - Linux/x86 4.9.95-gentoo Kernel Configuration
     → to complete
    → Device Drivers → Generic Driver Options
    -*- Userspace firmware loading support
    [*]   Include in-kernel firmware blobs in kernel binary
    (i915/skl_dmc_ver1_26.bin) External firmware blobs to build into the kernel binary
    (/lib/firmware) Firmware blobs root directory

** Note**\
soundcore: exports duplicate symbol register_sound_dsp (owned by kernel)

The package [[[sys-kernel/linux-firmware]](https://packages.gentoo.org/packages/sys-kernel/linux-firmware)[]] is required.

`root `[`#`]`emerge --ask sys-kernel/linux-firmware`

### [bluetooth]

`root `[`#`]`lsusb -t`

    /:  Bus 02.Port 1: Dev 1, Class=root_hub, Driver=xhci_hcd/6p, 5000M
    /:  Bus 01.Port 1: Dev 1, Class=root_hub, Driver=xhci_hcd/12p, 480M
        |__ Port 7: Dev 4, If 0, Class=Wireless, Driver=btusb, 12M
        |__ Port 7: Dev 4, If 1, Class=Wireless, Driver=btusb, 12M

[KERNEL]

    .config - Linux/x86 4.9.95-gentoo Kernel Configuration
     → Search (CONFIG_BT_HCIBTUSB)

     Symbol: BT_HCIBTUSB [=m]
     Type  : tristate
     Prompt: HCI USB driver
     Location:
      │     -> Networking support (NET [=y])
      │       -> Bluetooth subsystem support (BT [=m])│
      │ (1)     -> Bluetooth device drivers│
      │   Defined at drivers/bluetooth/Kconfig:21│
      │   Depends on: NET [=y] && BT [=m] && USB [=y]│
      │   Selects: BT_INTEL [=m]

working under command line (net-wireless/bluez-tools) could pair to an android phone

[Bluetooth](https://wiki.gentoo.org/wiki/Bluetooth "Bluetooth") --- describes the configuration and usage of Bluetooth controllers and devices.

[https://wiki.archlinux.org/index.php/bluetooth](https://wiki.archlinux.org/index.php/bluetooth)

### [misc]

`root `[`#`]`lspci -nn -k`

    00:16.0 Communication controller [0780]: Intel Corporation Sunrise Point-LP CSME HECI #1 [8086:9d3a] (rev 21)
        Subsystem: Lenovo Sunrise Point-LP CSME HECI [17aa:3800]
        Kernel driver in use: mei_me

[KERNEL]

    .config -

** Note**\
[https://www.kernel.org/doc/Documentation/misc-devices/mei/mei.txt](https://www.kernel.org/doc/Documentation/misc-devices/mei/mei.txt) Intel Management Engine (Intel ME) is an isolated and protected computing resource (Co-processor) residing inside certain Intel chipsets.

### [Touchpad and TouchScreen]

`root `[`#`]`lspci -nn -k`

    00:15.0 Signal processing controller [1180]: Intel Corporation Sunrise Point-LP Serial IO I2C Controller #0 [8086:9d60] (rev 21)
        Subsystem: Lenovo Sunrise Point-LP Serial IO I2C Controller [17aa:3800]
        Kernel driver in use: intel-lpss
        Kernel modules: intel_lpss_pci
    00:15.1 Signal processing controller [1180]: Intel Corporation Sunrise Point-LP Serial IO I2C Controller #1 [8086:9d61] (rev 21)
        Subsystem: Lenovo Sunrise Point-LP Serial IO I2C Controller [17aa:3800]
        Kernel driver in use: intel-lpss
        Kernel modules: intel_lpss_pci
    00:15.3 Signal processing controller [1180]: Intel Corporation Sunrise Point-LP Serial IO I2C Controller #3 [8086:9d63] (rev 21)
        Subsystem: Lenovo Sunrise Point-LP Serial IO I2C Controller [17aa:3800]
        Kernel driver in use: intel-lpss
        Kernel modules: intel_lpss_pci

`root `[`#`]`xinput list `

    Virtual core pointer                       id=2    [master pointer  (3)]
       ↳ Virtual core XTEST pointer                 id=4    [slave  pointer  (2)]
       ↳ Synaptics TM3066-002                       id=10   [slave  pointer  (2)]
       ↳ ELAN21EF:00 04F3:21EF                      id=11   [slave  pointer  (2)]
    Virtual core keyboard                       id=3    [master keyboard (2)]
        ↳ Virtual core XTEST keyboard               id=5    [slave  keyboard (3)]
        ↳ Power Button                              id=6    [slave  keyboard (3)]
        ↳ Video Bus                                 id=7    [slave  keyboard (3)]
        ↳ Power Button                              id=8    [slave  keyboard (3)]
        ↳ Lenovo EasyCamera: Lenovo EasyC           id=9    [slave  keyboard (3)]
        ↳ AT Translated Set 2 keyboard              id=12   [slave  keyboard (3)]

\

`root `[`#`]`less /proc/bus/input/devices `

    I: Bus=0018 Vendor=06cb Product=77c6 Version=0100
    N: Name="Synaptics TM3066-002"
    P: Phys=i2c-SYNA2B29:00
    S: Sysfs=/devices/pci0000:00/0000:00:15.1/i2c_designware.1/i2c-6/i2c-SYNA2B29:00/0018:06CB:77C6.0002/input/input23
    U: Uniq=
    H: Handlers=mouse0 event15
    B: PROP=5
    B: EV=b
    B: KEY=e520 10000 0 0 0 0
    B: ABS=6f3800001000003

    I: Bus=0018 Vendor=04f3 Product=21ef Version=0100
    N: Name="ELAN21EF:00 04F3:21EF"
    P: Phys=i2c-ELAN21EF:00
    S: Sysfs=/devices/pci0000:00/0000:00:15.3/i2c_designware.2/i2c-7/i2c-ELAN21EF:00/0018:04F3:21EF.0003/input/input24
    U: Uniq=
    H: Handlers=mouse1 event16
    B: PROP=2
    B: EV=1b
    B: KEY=400 0 0 0 0 0
    B: ABS=3273800000000003
    B: MSC=20

** Note**\
this is work in progress, synaptic module : hid_rmi, i2c_designware, i2c_hid, i2c-ITE8396, hid-rmi

** Note**\
this is work in progress, elan module : hid_multitouch, i2c_hid, hid-generic

** Note**\
module difference between a working synaptic and touchscreen and not working configuration : modules added : 8021q ccm ctr hid_multitouch hid_rmi hid_sensor_custom i2c_designware_platform i2c_designware_core elan_i2c i2c_i801 iTCO_vendor_support iTCO_wdt llc rmi_core stp garp i2c_designware_core hid_sensor_hub

[KERNEL]

    .config - Linux/x86 4.9.95-gentoo Kernel Configuration
     → Device Drivers → Multifunction device drivers
    <M> Intel Low Power Subsystem support in PCI mode
    Device Drivers → HID support →  I2C HID support
    <M> HID over I2C transport layer
    Device Drivers → HID support →  Special HID Drivers
    <M> HID multitouch panels
    <M> synaptic RM14 device support
    Device Drivers →  Input device support →  Touchscreens
    <M>   Elan eKTF2127 I2C touchscreen
    <M>   Elan eKTH I2C touchscreen
    Device Drivers → HID support → Special HID drivers
    <M> ELAN USB Touchpad Support

** Note**\
echo elan_i2c \>\> /etc/modules-load.d/synaptic.conf

** Note**\
i2c_hid i2c-ITE8396:00: error in i2c_hid_init_report size:19 / ret_size:18\<

See [Synaptics](https://wiki.gentoo.org/wiki/Synaptics "Synaptics") to configure.

### [SD card]

`root `[`#`]`lspci -nn -k`

    02:00.0 SD Host controller [0805]: O2 Micro, Inc. Device [1217:8620] (rev 01)
        Subsystem: Lenovo Device [17aa:3800]
        Kernel driver in use: sdhci-pci
        Kernel modules: sdhci_pci

[KERNEL]

    .config -

The reader detects the partition but gives timeouts on linux 4.16.11

`root `[`#`]`dd if=/dev/mmcblk0 bs=512 count=1 of=test`

    [385702.654671] mmc0: Tuning timeout, falling back to fixed sampling clock
    [385702.654769] mmc0: new ultra high speed SDR104 SDXC card at address 0001
    [385702.655364] mmcblk0: mmc0:0001 EE8QT 239 GiB
    [385702.657337]  mmcblk0: p1
    [385713.140629] mmc0: Timeout waiting for hardware interrupt.
    [385713.140635] mmc0: sdhci: ============ SDHCI REGISTER DUMP ===========
    [385713.140643] mmc0: sdhci: Sys addr:  0x00000008 | Version:  0x00000603
    [385713.140649] mmc0: sdhci: Blk size:  0x00007200 | Blk cnt:  0x00000008
    [385713.140655] mmc0: sdhci: Argument:  0x1dcffff0 | Trn mode: 0x0000003b
    [385713.140661] mmc0: sdhci: Present:   0x01ff0000 | Host ctl: 0x00000017
    [385713.140667] mmc0: sdhci: Power:     0x0000000f | Blk gap:  0x00000000
    [385713.140673] mmc0: sdhci: Wake-up:   0x00000000 | Clock:    0x00000007
    [385713.140678] mmc0: sdhci: Timeout:   0x0000000a | Int stat: 0x00000000
    [385713.140684] mmc0: sdhci: Int enab:  0x02ff008b | Sig enab: 0x02ff008b
    [385713.140690] mmc0: sdhci: AC12 err:  0x00000004 | Slot int: 0x00000000
    [385713.140696] mmc0: sdhci: Caps:      0x25fcc8bf | Caps_1:   0x00002077
    [385713.140702] mmc0: sdhci: Cmd:       0x0000123a | Max curr: 0x005800c8
    [385713.140708] mmc0: sdhci: Resp[0]:   0x00000900 | Resp[1]:  0x00000000
    [385713.140714] mmc0: sdhci: Resp[2]:   0x00000000 | Resp[3]:  0x00001b00
    [385713.140718] mmc0: sdhci: Host ctl2: 0x0000800b
    [385713.140723] mmc0: sdhci: ADMA Err:  0x00000000 | ADMA Ptr: 0xfffff208
    [385713.140726] mmc0: sdhci: ============================================
    [385713.191687] mmc0: Tuning timeout, falling back to fixed sampling clock

patch to fix this issue (no more required on 5.9.1)

    diff --git a/drivers/mmc/host/sdhci-pci-o2micro.c b/drivers/mmc/host/sdhci-pci-o2micro.c
    index 19944b004..1d8938a68 100644
    --- a/drivers/mmc/host/sdhci-pci-o2micro.c
    +++ b/drivers/mmc/host/sdhci-pci-o2micro.c
    @@ -681,7 +681,6 @@ static const struct sdhci_ops sdhci_pci_o2_ops = [`#`]`lsusb -t`

        |__ Port 6: Dev 3, If 0, Class=Video, Driver=uvcvideo, 480M
        |__ Port 6: Dev 3, If 1, Class=Video, Driver=uvcvideo, 480M

[KERNEL]

    .config - Linux/x86 4.9.95-gentoo Kernel Configuration
     → Device Drivers → Multimedia support →
    [*]   Cameras/video grabbers support
    [*]   Media USB Adapters  --->
           <M>   USB Video Class (UVC)
           [*]     UVC input events device support

### [HEVC]

see [https://forums.gentoo.org/viewtopic-p-8522411.html#8522411](https://forums.gentoo.org/viewtopic-p-8522411.html#8522411)

### [driver summary]

** Important**\
lsmod is a poor representation of what drivers are needed. It will show modules loaded even if they are not necessary. this list must be split and reduced to the useful modules for each hardware parts

`root `[`#`]`lsmod`

    Module                  Size  Used by
    8021q                  32768  0
    garp                   16384  1 8021q
    stp                    16384  1 garp
    llc                    16384  2 stp,garp
    ctr                    16384  2
    ccm                    20480  6
    tcp_diag               16384  0
    udp_diag               16384  0
    inet_diag              24576  2 tcp_diag,udp_diag
    xt_conntrack           16384  18
    nf_conntrack          151552  1 xt_conntrack
    nf_defrag_ipv4         16384  1 nf_conntrack
    ip6table_filter        16384  0
    ip6_tables             28672  1 ip6table_filter
    ipv6                  540672  39 udp_diag
    crc_ccitt              16384  1 ipv6
    nf_defrag_ipv6         24576  2 nf_conntrack,ipv6
    iptable_filter         16384  1
    ip_tables              28672  1 iptable_filter
    rfcomm                 90112  4
    cmac                   16384  15
    ecb                    16384  8
    algif_skcipher         16384  7
    bnep                   28672  2
    snd_hda_codec_hdmi     65536  1
    snd_hda_codec_realtek   126976  1
    snd_hda_codec_generic    94208  1 snd_hda_codec_realtek
    ledtrig_audio          16384  2 snd_hda_codec_generic,snd_hda_codec_realtek
    hid_multitouch         32768  0
    mmc_block              49152  2
    hid_sensor_custom      28672  0
    hid_rmi                24576  0
    rmi_core               61440  1 hid_rmi
    hid_sensor_hub         24576  1 hid_sensor_custom
    vfat                   20480  1
    i2c_designware_platform    16384  0
    iTCO_wdt               16384  0
    i2c_designware_core    28672  1 i2c_designware_platform
    iTCO_vendor_support    16384  1 iTCO_wdt
    wmi_bmof               16384  0
    uvcvideo              114688  0
    i915                 1921024  17
    btusb                  57344  0
    x86_pkg_temp_thermal    20480  0
    btrtl                  24576  1 btusb
    videobuf2_vmalloc      20480  1 uvcvideo
    btbcm                  16384  1 btusb
    btintel                28672  1 btusb
    videobuf2_memops       20480  1 videobuf2_vmalloc
    coretemp               20480  0
    iwlmvm                323584  0
    videobuf2_v4l2         28672  1 uvcvideo
    videobuf2_common       57344  2 videobuf2_v4l2,uvcvideo
    bluetooth             655360  33 btrtl,btintel,btbcm,bnep,btusb,rfcomm
    snd_hda_intel          49152  3
    mac80211              802816  1 iwlmvm
    kvm_intel             229376  0
    drm_kms_helper        200704  1 i915
    libarc4                16384  1 mac80211
    ecdh_generic           16384  2 bluetooth
    videodev              233472  3 videobuf2_v4l2,uvcvideo,videobuf2_common
    snd_hda_codec         147456  4 snd_hda_codec_generic,snd_hda_codec_hdmi,snd_hda_intel,snd_hda_codec_realtek
    ecc                    32768  1 ecdh_generic
    kvm                   753664  1 kvm_intel
    mc                     61440  4 videodev,videobuf2_v4l2,uvcvideo,videobuf2_common
    irqbypass              16384  1 kvm
    snd_hda_core          102400  5 snd_hda_codec_generic,snd_hda_codec_hdmi,snd_hda_intel,snd_hda_codec,snd_hda_codec_realtek
    iwlwifi               282624  1 iwlmvm
    sdhci_pci              49152  0
    drm                   573440  7 drm_kms_helper,i915
    snd_hwdep              16384  1 snd_hda_codec
    cqhci                  32768  1 sdhci_pci
    ghash_clmulni_intel    16384  0
    snd_pcm               118784  4 snd_hda_codec_hdmi,snd_hda_intel,snd_hda_codec,snd_hda_core
    sdhci                  65536  1 sdhci_pci
    syscopyarea            16384  1 drm_kms_helper
    cryptd                 24576  1 ghash_clmulni_intel
    sysfillrect            16384  1 drm_kms_helper
    mmc_core              176128  4 sdhci,cqhci,mmc_block,sdhci_pci
    pcspkr                 16384  0
    sysimgblt              16384  1 drm_kms_helper
    snd_timer              40960  1 snd_pcm
    serio_raw              20480  0
    cfg80211              823296  3 iwlmvm,iwlwifi,mac80211
    fb_sys_fops            16384  1 drm_kms_helper
    iosf_mbi               24576  3 i2c_designware_platform,i915,sdhci_pci
    snd                    94208  14 snd_hda_codec_generic,snd_hda_codec_hdmi,snd_hwdep,snd_hda_intel,snd_hda_codec,snd_hda_codec_realtek,snd_timer,snd_pcm
    soundcore              16384  1 snd
    i2c_i801               32768  0
    i2c_algo_bit           16384  1 i915
    intel_lpss_pci         20480  0
    rfkill                 28672  5 bluetooth,cfg80211
    intel_lpss             16384  1 intel_lpss_pci
    wmi                    32768  1 wmi_bmof
    i2c_hid                32768  0
    video                  49152  1 i915
    backlight              20480  2 video,i915
    vboxpci                28672  0
    vboxnetadp             28672  0
    vboxnetflt             32768  0
    vboxdrv               466944  3 vboxpci,vboxnetadp,vboxnetflt
    elan_i2c               49152  0
    i2c_core               94208  10 i2c_designware_platform,videodev,i2c_hid,i2c_designware_core,drm_kms_helper,i2c_algo_bit,elan_i2c,i2c_i801,i915,drm
    xts                    16384  1
    aes_generic            36864  22
    crc32c_intel           24576  6
    cbc                    16384  0
    sha256_generic         20480  0
    msdos                  20480  0
    fat                    86016  2 msdos,vfat
    efivarfs               16384  1
    configfs               53248  1
    cramfs                 53248  0
    squashfs               65536  0
    fuse                  131072  3
    xfs                  1482752  0
    nfs                   319488  0
    lockd                  98304  1 nfs
    grace                  16384  1 lockd
    sunrpc                405504  2 lockd,nfs
    fscache               385024  1 nfs
    jfs                   200704  0
    reiserfs              270336  0
    btrfs                1454080  0
    zstd_decompress        90112  1 btrfs
    zstd_compress         192512  1 btrfs
    bcache                270336  0
    crc64                  16384  1 bcache
    ext4                  737280  4
    jbd2                  126976  1 ext4
    ext2                   86016  0
    mbcache                16384  2 ext4,ext2
    linear                 20480  0
    raid10                 61440  0
    raid1                  49152  0
    raid0                  24576  0
    dm_zero                16384  0
    dm_verity              32768  0
    reed_solomon           20480  1 dm_verity
    dm_thin_pool           81920  0
    dm_switch              16384  0
    dm_snapshot            53248  0
    dm_raid                45056  0
    raid456               172032  1 dm_raid
    async_raid6_recov      24576  1 raid456
    async_memcpy           20480  2 raid456,async_raid6_recov
    async_pq               20480  2 raid456,async_raid6_recov
    raid6_pq              122880  4 async_pq,btrfs,raid456,async_raid6_recov
    dm_mirror              28672  0
    dm_region_hash         16384  1 dm_mirror
    dm_log_writes          20480  0
    dm_log_userspace       24576  0
    dm_log                 20480  3 dm_region_hash,dm_log_userspace,dm_mirror
    dm_integrity           61440  0
    async_xor              20480  4 dm_integrity,async_pq,raid456,async_raid6_recov
    async_tx               20480  5 async_pq,async_memcpy,async_xor,raid456,async_raid6_recov
    xor                    24576  2 async_xor,btrfs
    dm_flakey              16384  0
    dm_era                 28672  0
    dm_delay               16384  0
    dm_crypt               49152  1
    dm_cache_smq           28672  0
    dm_cache               69632  1 dm_cache_smq
    dm_persistent_data     81920  3 dm_era,dm_thin_pool,dm_cache
    libcrc32c              16384  5 nf_conntrack,dm_persistent_data,btrfs,xfs,raid456
    dm_bufio               32768  4 dm_verity,dm_integrity,dm_persistent_data,dm_snapshot
    dm_bio_prison          20480  2 dm_thin_pool,dm_cache
    dm_mod                147456  19 dm_verity,dm_integrity,dm_raid,dm_crypt,dm_era,dm_thin_pool,dm_zero,dm_log,dm_delay,dm_flakey,dm_log_writes,dm_log_userspace,dm_cache,dm_snapshot,dm_mirror,dm_switch,dm_bufio
    firewire_core          73728  0
    crc_itu_t              16384  1 firewire_core
    hid_sunplus            16384  0
    hid_sony               36864  0
    hid_samsung            16384  0
    hid_pl                 20480  0
    hid_petalynx           16384  0
    hid_monterey           16384  0
    hid_microsoft          16384  0
    hid_logitech_dj        28672  0
    hid_logitech           20480  0
    ff_memless             20480  4 hid_logitech,hid_sony,hid_microsoft,hid_pl
    hid_gyration           16384  0
    hid_ezkey              16384  0
    hid_cypress            16384  0
    hid_chicony            16384  0
    hid_cherry             16384  0
    hid_belkin             16384  0
    hid_apple              16384  0
    hid_a4tech             16384  0
    sl811_hcd              32768  0
    xhci_pci               20480  0
    xhci_hcd              278528  1 xhci_pci
    usb_storage            77824  0
    mpt3sas               290816  0
    raid_class             16384  1 mpt3sas
    aic94xx                94208  0
    libsas                 94208  1 aic94xx
    lpfc                  942080  0
    qla2xxx               860160  0
    megaraid_sas          176128  0
    megaraid_mbox          45056  0
    megaraid_mm            20480  1 megaraid_mbox
    aacraid               131072  0
    sx8                    20480  0
    hpsa                  110592  0
    3w_9xxx                45056  0
    3w_xxxx                32768  0
    3w_sas                 32768  0
    mptsas                 69632  0
    scsi_transport_sas     45056  5 mptsas,aic94xx,hpsa,libsas,mpt3sas
    mptfc                  24576  0
    scsi_transport_fc      65536  3 lpfc,qla2xxx,mptfc
    mptspi                 28672  0
    mptscsih               45056  3 mptsas,mptspi,mptfc
    mptbase                98304  4 mptsas,mptspi,mptfc,mptscsih
    imm                    20480  0
    parport                61440  1 imm
    sym53c8xx              94208  0
    initio                 28672  0
    arcmsr                 53248  0
    aic7xxx               143360  0
    aic79xx               155648  0
    scsi_transport_spi     40960  4 mptspi,aic79xx,aic7xxx,sym53c8xx
    sr_mod                 28672  0
    cdrom                  73728  1 sr_mod
    sg                     40960  0
    sd_mod                 49152  5
    pdc_adma               16384  0
    sata_inic162x          16384  0
    sata_mv                40960  0
    ata_piix               36864  0
    ahci                   40960  4
    libahci                40960  1 ahci
    sata_qstor             16384  0
    sata_vsc               16384  0
    sata_uli               16384  0
    sata_sis               16384  0
    sata_sx4               20480  0
    sata_nv                32768  0
    sata_via               24576  0
    sata_svw               16384  0
    sata_sil24             24576  0
    sata_sil               16384  0
    sata_promise           20480  0
    pata_via               20480  0
    pata_jmicron           16384  0
    pata_marvell           16384  0
    pata_sis               20480  1 sata_sis
    pata_netcell           16384  0
    pata_pdc202xx_old      16384  0
    pata_atiixp            16384  0
    pata_amd               24576  0
    pata_ali               20480  0
    pata_it8213            16384  0
    pata_pcmcia            20480  0
    pata_serverworks       16384  0
    pata_oldpiix           16384  0
    pata_artop             16384  0
    pata_it821x            16384  0
    pata_hpt3x2n           16384  0
    pata_hpt3x3            16384  0
    pata_hpt37x            24576  0
    pata_hpt366            16384  0
    pata_cmd64x            16384  0
    pata_sil680            20480  0
    pata_pdc2027x          16384  0
    nvme                   49152  0
    nvme_core             102400  1 nvme
    virtio_net             57344  0
    net_failover           20480  1 virtio_net
    failover               16384  1 net_failover
    virtio_crypto          28672  0
    crypto_engine          16384  1 virtio_crypto
    virtio_mmio            16384  0
    virtio_pci             28672  0
    virtio_balloon         20480  0
    virtio_rng             16384  0
    virtio_console         36864  0
    virtio_blk             20480  0
    virtio_scsi            24576  0
    virtio_ring            40960  9 virtio_rng,virtio_mmio,virtio_console,virtio_balloon,virtio_scsi,virtio_crypto,virtio_pci,virtio_blk,virtio_net
    virtio                 16384  9 virtio_rng,virtio_mmio,virtio_console,virtio_balloon,virtio_scsi,virtio_crypto,virtio_pci,virtio_blk,virtio_net

`root `[`#`]`lsusb -t`

    /:  Bus 02.Port 1: Dev 1, Class=root_hub, Driver=xhci_hcd/6p, 5000M
    /:  Bus 01.Port 1: Dev 1, Class=root_hub, Driver=xhci_hcd/12p, 480M
        |__ Port 1: Dev 2, If 0, Class=Human Interface Device, Driver=usbhid, 1.5M
        |__ Port 6: Dev 3, If 0, Class=Video, Driver=uvcvideo, 480M
        |__ Port 6: Dev 3, If 1, Class=Video, Driver=uvcvideo, 480M
        |__ Port 7: Dev 4, If 0, Class=Wireless, Driver=btusb, 12M
        |__ Port 7: Dev 4, If 1, Class=Wireless, Driver=btusb, 12M

## [External resources]

-   [https://wiki.archlinux.org/title/Lenovo_IdeaPad_Yoga_900](https://wiki.archlinux.org/title/Lenovo_IdeaPad_Yoga_900)