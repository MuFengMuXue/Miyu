\

## Contents

-   [[1] [Hardware Specs]](#Hardware_Specs)
-   [[2] [Installation]](#Installation)
    -   [[2.1] [make.conf]](#make.conf)
    -   [[2.2] [Compilation speed]](#Compilation_speed)
-   [[3] [Kernel Configuration]](#Kernel_Configuration)
    -   [[3.1] [CPU]](#CPU)
    -   [[3.2] [Hard disk]](#Hard_disk)
    -   [[3.3] [Graphics]](#Graphics)
    -   [[3.4] [Sound]](#Sound)
    -   [[3.5] [Ethernet]](#Ethernet)
    -   [[3.6] [Wireless]](#Wireless)
    -   [[3.7] [Touchpad]](#Touchpad)
    -   [[3.8] [ACPI, LEDs and Hotkeys]](#ACPI.2C_LEDs_and_Hotkeys)
    -   [[3.9] [USB]](#USB)
        -   [[3.9.1] [Bluetooth]](#Bluetooth)
        -   [[3.9.2] [SD card reader]](#SD_card_reader)
        -   [[3.9.3] [Webcam]](#Webcam)

## [Hardware Specs]

-   [Intel Atom N270](https://ark.intel.com/products/36331/Intel-Atom-Processor-N270-512K-Cache-1-60-GHz-533-MHz-FSB-) (with turbo up to 1.8GHz using the [eeepc_laptop] driver)
-   10.1\" LCD screen (1024×600)
-   i945 graphics chipset ("gen3", OpenGL 1.4)
-   1 GB DDR2-533 RAM (upgradable to 2GB)
-   160GB hard disk (2.5\" SATA, replaceable)
-   3× USB2 ports, SD card reader (SDHC compatible), VGA port
-   10/100 Ethernet
-   2.4GHz Wi-Fi B/G/N support
-   Bluetooth 2.1
-   HDA audio
-   1.3 megapixel webcam

Although the N270 CPU was considered weak even at launch, its lack of speculative execution hardware makes it immune to [Spectre and related security issues](https://wiki.gentoo.org/wiki/Project:Security/Vulnerabilities/Meltdown_and_Spectre "Project:Security/Vulnerabilities/Meltdown and Spectre"):

`user `[`$`]` lscpu | grep Vuln`

    Vulnerability Itlb multihit:     Not affected
    Vulnerability L1tf:              Not affected
    Vulnerability Mds:               Not affected
    Vulnerability Meltdown:          Not affected
    Vulnerability Spec store bypass: Not affected
    Vulnerability Spectre v1:        Not affected
    Vulnerability Spectre v2:        Not affected
    Vulnerability Tsx async abort:   Not affected

## [Installation]

As with most netbooks the Eee PC 1000H lacks an optical drive; an external one may be used, but a more common choice is [creating LiveUSB boot media](https://wiki.gentoo.org/wiki/LiveUSB "LiveUSB"). To boot from external media you have to press [Esc] during the BIOS boot splash screen and select the right installation medium. After booting a live system follow the [Gentoo Linux x86 Handbook](https://wiki.gentoo.org/wiki/Handbook:X86 "Handbook:X86").

** Note**\
The BIOS contains a "Boot Booster" feature, designed to speed up the boot process by caching some info on the hard disk. To ensure this works correctly, create one unused disk partition with MBR partition type [EF], at least 32MB in size.

### [make.conf]

[FILE] **`/etc/portage/make.conf`**

    CFLAGS="-O2 -pipe -march=bonnell -msahf -mmovbe -mfxsr"
    CXXFLAGS="$"

[FILE] **`/etc/portage/package.use/00video`**

    */* VIDEO_CARDS: -* intel i915

[FILE] **`/etc/portage/package.use/00input`**

    */* INPUT_DEVICES: libinput

[FILE] **`/etc/portage/package.use/00cpu-flags`**

    */* CPU_FLAGS_X86: mmx mmxext sse sse2 sse3 ssse3

### [Compilation speed]

To reduce compiling time and decrease the likelihood of builds failing due to low memory, consider using one or more of [ccache](https://wiki.gentoo.org/wiki/Ccache "Ccache"), [distcc](https://wiki.gentoo.org/wiki/Distcc "Distcc"), or [zram](https://wiki.gentoo.org/wiki/Zram "Zram"). Upgrading the RAM to 2GB will help too, especially if building modern web browsers.

## [Kernel Configuration]

### [CPU]

[KERNEL] **Intel Atom N270**

    [ ] 64-bit kernel
    Processor type and features  --->
        Processor family ()  --->
            <*> Intel Atom
    Power management and ACPI options  --->
        [*] Cpuidle Driver for Intel Processors

### [Hard disk]

[lspci] and other tools will show the drive controller operating in IDE emulation mode, thus the appropriate driver is the PATA one:

[KERNEL] **00:1f.2 IDE interface: Intel Corporation 82801GBM/GHM (ICH7-M Family) SATA Controller \[IDE mode\]**

    Device Drivers --->
        <*> Serial ATA and Parallel ATA drivers (libata)  --->
            < >   AHCI SATA support
            [*]   ATA SFF support
            [*]     ATA BMDMA support
            <*>     Intel ESB, ICH, PIIX3, PIIX4 PATA/SATA support

** Note**\
Although the ICH7 in this netbook *does* support native AHCI, the BIOS disables it at boot and fixing it would require in-depth kernel or [ACPI DSDT hacking](https://www.kernel.org/doc/Documentation/acpi/initrd_table_override.txt). There are a few existing workarounds on the web (particularly for GRUB) but none of those are known to handle suspend-to-RAM, which makes them dangerous to use here.

### [Graphics]

[KERNEL] **00:02.0 VGA compatible controller: Intel Corporation Mobile 945GSE Express Integrated Graphics Controller**

    Device Drivers  --->
        Graphics support  --->
            < > /dev/agpgart (AGP Support)  --->
            <*> Direct Rendering Manager (XFree86 4.1.0 and higher DRI support) --->
                [*]   Enable legacy fbdev support for your modesetting driver
            <*> Intel 8xx/9xx/G3x/G4x/HD Graphics

### [Sound]

[KERNEL] **00:1b.0 Audio device: Intel Corporation NM10/ICH7 Family High Definition Audio Controller**

    Device Drivers --->
        <*> Sound Card Support --->
            <*> Advanced Linux Sound Architecture --->
                HD-Audio --->
                    <*> HD Audio PCI
                    <*> Build Realtek HD-audio codec support

### [Ethernet]

[KERNEL] **03:00.0 Ethernet controller: Qualcomm Atheros AR8121/AR8113/AR8114 Gigabit or Fast Ethernet**

    Device Drivers  --->
        Networking support  --->
            [*] Network device support --->
                [*] Ethernet driver support --->
                    [*]   Atheros devices
                    <*>     Atheros L1E Gigabit Ethernet support

** Note**\
Although the label says gigabit, this Ethernet hardware only supports 10/100.

### [Wireless]

[KERNEL] **01:00.0 Network controller: Ralink corp. RT2790 Wireless 802.11n 1T/2R PCIe**

    Bus options (PCI etc.)  --->
        [*] PCI Express Port Bus support
        [*]   PCI Express Hotplug driver
        [*] Support for PCI Hotplug  --->
            [*]   ACPI PCI Hotplug driver
    [*] Networking support  --->
        <*> Wireless  --->
            <*> cfg80211 - wireless configuration API
            <*> Generic IEEE 802.11 Networking Stack (mac80211)
    Device Drivers  --->
        Generic Driver Options  --->
            Firmware loader  --->
                (rt2860.bin regulatory.db regulatory.db.p7s) Build named firmware blobs into the kernel binary
                (/lib/firmware) Firmware blobs root directory
        Network device support  --->
            Wireless LAN  --->
                [*] Ralink devices  --->
                    <*> Ralink driver support  --->
                        <*> Ralink rt27xx/rt28xx/rt30xx (PCI/PCIe/PCMCIA) support

The required firmware files are available in [[[sys-kernel/linux-firmware]](https://packages.gentoo.org/packages/sys-kernel/linux-firmware)[]] and [[[net-wireless/wireless-regdb]](https://packages.gentoo.org/packages/net-wireless/wireless-regdb)[]]. PCIe hotplug is required for the [Fn+F2] keyboard toggle to actually switch the card on and off.

### [Touchpad]

[KERNEL] **ETPS/2 Elantech Touchpad**

    Device Drivers --->
        Input device support --->
            <*> Event interface
            [*] Mice --->
                <*> PS/2 mouse
                    [*] Elantech PS/2 protocol extension
                    [ ]   Elantech PS/2 SMbus companion

### [][ACPI, LEDs and Hotkeys]

[KERNEL] **Asus EeePC extra buttons, hotplug toggles, hardware sensors, turbo mode support**

    Device Drivers --->
        [*] X86 Platform Specific Device Drivers --->
            <*>   Eee PC Hotkey Driver

If you have updated the BIOS to a recent version, it assumes Windows 7 is running by default and disables the interfaces needed by the [eeepc_laptop] driver. To fix this, append [acpi_osi=Linux] to the kernel command line.

Newer BIOS revisions have more [Fn] combinations (mostly on the unlabelled F-keys). Stable versions of the kernel have already received updates to recognize most of these, but [Fn]+[space] is missing; see below for a fix.

### [USB]

[KERNEL] **00:1d.7 USB controller: Intel Corporation NM10/ICH7 Family USB2 EHCI Controller**

    Device Drivers --->
        [*] USB support  --->
            <*>   Support for Host-side USB
            <*>     EHCI HCD (USB 2.0) support
                [*]     Root Hub Transaction Translators
                [*]     Improved Transaction Translator scheduling
            < >     OHCI HCD (USB 1.1) support
            <*>     UHCI HCD (most Intel and VIA) support

Several internal devices are on the USB bus:

#### [Bluetooth]

[KERNEL] **0b05:b700 ASUSTek Computer, Inc. Broadcom Bluetooth 2.1**

    [*] Networking support  --->
        <*> Bluetooth subsystem support  --->
            [*]  Bluetooth Classic (BR/EDR) features
            Bluetooth device drivers  --->
                <*>  HCI USB driver
                [*]    Enable USB autosuspend for Bluetooth USB devices by default

#### [SD card reader]

[KERNEL] **058f:6335 Alcor Micro Corp. SD/MMC Card Reader**

    Device Drivers --->
        [*] USB support  --->
            <*>   USB Mass Storage support

#### [Webcam]

[KERNEL] **04f2:b071 Chicony Electronics Co., Ltd 2.0M UVC Webcam / CNF7129**

    Device Drivers  --->
        <*> Multimedia support  --->
            [*]  Cameras/video grabbers support
            [*]  Media USB Adapters  --->
                 <*>  USB Video Class (UVC)
                 [*]        UVC input events device support