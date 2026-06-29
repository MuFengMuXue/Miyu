\

[![](/images/thumb/0/0f/Acer_eM250.jpg/300px-Acer_eM250.jpg)](https://wiki.gentoo.org/wiki/File:Acer_eM250.jpg)

[](https://wiki.gentoo.org/wiki/File:Acer_eM250.jpg "Enlarge")

Acer eMachines eM250 series

## Contents

-   [[1] [Software]](#Software)
    -   [[1.1] [GCC]](#GCC)
    -   [[1.2] [Portage]](#Portage)
    -   [[1.3] [Kernel]](#Kernel)
        -   [[1.3.1] [CPU]](#CPU)
        -   [[1.3.2] [Disk]](#Disk)
        -   [[1.3.3] [Video]](#Video)
        -   [[1.3.4] [Sound]](#Sound)
        -   [[1.3.5] [Network]](#Network)
        -   [[1.3.6] [Webcam]](#Webcam)
        -   [[1.3.7] [Other]](#Other)
-   [[2] [Hardware]](#Hardware)
    -   [[2.1] [BIOS]](#BIOS)
    -   [[2.2] [CPU]](#CPU_2)
    -   [[2.3] [Memory]](#Memory)
    -   [[2.4] [Graphics]](#Graphics)
        -   [[2.4.1] [Frame Buffer]](#Frame_Buffer)
    -   [[2.5] [Ethernet]](#Ethernet)
    -   [[2.6] [ACPI]](#ACPI)
    -   [[2.7] [Wireless]](#Wireless)
    -   [[2.8] [Sound]](#Sound_2)
    -   [[2.9] [USB]](#USB)
        -   [[2.9.1] [2.0]](#2.0)
    -   [[2.10] [SATA]](#SATA)
    -   [[2.11] [Webcam]](#Webcam_2)
    -   [[2.12] [Bluetooth]](#Bluetooth)
    -   [[2.13] [Touchpad]](#Touchpad)
    -   [[2.14] [Keyboard]](#Keyboard)
-   [[3] [External resources]](#External_resources)

## [Software]

### [GCC]

`root `[`#`]`gcc-config -l`

    i686-pc-linux-gnu-4.7.2 *

### [Portage]

[FILE] **`/etc/portage/make.conf`**

    CHOST="i686-pc-linux-gnu"
    CFLAGS="-O2 -march=native -fomit-frame-pointer -pipe"
    CXXFLAGS="$"

[FILE] **`/etc/portage/package.use/00input`**

    */* INPUT_DEVICES: vdev synaptic

[FILE] **`/etc/portage/package.use/00video`**

    */* VIDEO_CARDS: -* intel fbdev vesa

### [Kernel]

[FILE] **`/etc/modules-load.d/drivers.conf`**

    b43
    atl1c
    uvcvideo
    tun
    dummy

#### [CPU]

[KERNEL] **Intel Atom N270**

    Processor type and features  --->
        Processor family ()  --->
            (X) Intel Atom

#### [Disk]

[KERNEL] **SATA**

    Device Drivers --->
        <*> Serial ATA and Parallel ATA drivers  --->
            [*]   ATA ACPI Support
            [*]   SATA Port Multiplier support
            <*>   AHCI SATA support
            [*]   ATA SFF support
            [*]     ATA BMDMA support
            <*>     Intel ESB, ICH, PIIX3, PIIX4 PATA/SATA support

#### [Video]

[KERNEL] **Graphics**

    Device Drivers --->
        Graphics support  --->
            <M> /dev/agpgart (AGP Support)  --->
                <M>   Intel 440LX/BX/GX, I8xx and E7x05 chipset support
            <M> Direct Rendering Manager (XFree86 4.1.0 and higher DRI support)  --->
            <M> Intel 8xx/9xx/G3x/G4x/HD Graphics
             Support for frame buffer devices  --->
                <M>   VGA 16-color graphics support
                <M>   Userspace VESA VGA graphics support
                [*]   VESA VGA graphics support

#### [Sound]

[KERNEL] **Sound**

    Device Drivers --->
        <*> Sound card support  --->
            <M>   Advanced Linux Sound Architecture  --->
                [*]   PCI sound devices  --->
                    <M>   Intel HD Audio  --->
                        (64)  Pre-allocated buffer size for HD-audio driver
                        [*]   Build hwdep interface for HD-audio driver
                        [*]   Build Realtek HD-audio codec support
                        [*]   Build Analog Device HD-audio codec support
                        -*-   Enable generic HD-audio codec parser
                        (0)   Default time-out for HD-audio power-save mode

#### [Network]

[KERNEL] **Ethernet**

    Device Drivers --->
        [*] Network device support  --->
            [*]   Ethernet driver support  --->
                [*]   Atheros devices
                <M>     Atheros L1C Gigabit Ethernet support

[KERNEL] **WIFI**

    Device Drivers --->
        [*] Network device support  --->
            [*]   Wireless LAN  --->
                <M>   Broadcom 43xx wireless support (mac80211 stack)
                [*]   Support for low-power (LP-PHY) devices

#### [Webcam]

[KERNEL] **Webcam**

    Device Drivers --->
        <*> Multimedia support  --->
            [*]   Cameras/video grabbers support
            [*]   Media USB Adapters  --->
                <M>   USB Video Class (UVC)
                [*]     UVC input events device support

#### [Other]

## [Hardware]

`root `[`#`]`lspci`

    00:00.0 Host bridge: Intel Corporation Mobile 945GSE Express Memory Controller Hub (rev 03)
    00:02.0 VGA compatible controller: Intel Corporation Mobile 945GSE Express Integrated Graphics Controller (rev 03)
    00:02.1 Display controller: Intel Corporation Mobile 945GM/GMS/GME, 943/940GML Express Integrated Graphics Controller (rev 03)
    00:1b.0 Audio device: Intel Corporation NM10/ICH7 Family High Definition Audio Controller (rev 02)
    00:1c.0 PCI bridge: Intel Corporation NM10/ICH7 Family PCI Express Port 1 (rev 02)
    00:1c.1 PCI bridge: Intel Corporation NM10/ICH7 Family PCI Express Port 2 (rev 02)
    00:1c.2 PCI bridge: Intel Corporation NM10/ICH7 Family PCI Express Port 3 (rev 02)
    00:1c.3 PCI bridge: Intel Corporation NM10/ICH7 Family PCI Express Port 4 (rev 02)
    00:1d.0 USB controller: Intel Corporation NM10/ICH7 Family USB UHCI Controller #1 (rev 02)
    00:1d.1 USB controller: Intel Corporation NM10/ICH7 Family USB UHCI Controller #2 (rev 02)
    00:1d.2 USB controller: Intel Corporation NM10/ICH7 Family USB UHCI Controller #3 (rev 02)
    00:1d.3 USB controller: Intel Corporation NM10/ICH7 Family USB UHCI Controller #4 (rev 02)
    00:1d.7 USB controller: Intel Corporation NM10/ICH7 Family USB2 EHCI Controller (rev 02)
    00:1e.0 PCI bridge: Intel Corporation 82801 Mobile PCI Bridge (rev e2)
    00:1f.0 ISA bridge: Intel Corporation 82801GBM (ICH7-M) LPC Interface Bridge (rev 02)
    00:1f.2 SATA controller: Intel Corporation 82801GBM/GHM (ICH7-M Family) SATA Controller [AHCI mode] (rev 02)
    00:1f.3 SMBus: Intel Corporation NM10/ICH7 Family SMBus Controller (rev 02)
    01:00.0 Network controller: Broadcom Corporation BCM4312 802.11b/g LP-PHY (rev 01)
    03:00.0 Ethernet controller: Qualcomm Atheros AR8132 Fast Ethernet (rev c0)

### [BIOS]

### [CPU]

The CPU is an Intel® Atom™ processor N270 (512 KB L2 cache, 1.60 GHz) with 2 cores.

`user `[`$`]`cat /proc/cpuinfo`

    processor   : 0
    vendor_id   : GenuineIntel
    cpu family  : 6
    model       : 28
    model name  : Intel(R) Atom(TM) CPU N270   @ 1.60GHz
    stepping    : 2
    microcode   : 0x212
    cpu MHz     : 1600.000
    cache size  : 512 KB
    physical id : 0
    siblings    : 1
    core id     : 0
    cpu cores   : 1
    apicid      : 0
    initial apicid  : 0
    fdiv_bug    : no
    hlt_bug     : no
    f00f_bug    : no
    coma_bug    : no
    fpu     : yes
    fpu_exception   : yes
    cpuid level : 10
    wp      : yes
    flags       : fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat clflush dts acpi mmx fxsr sse sse2 ss ht tm pbe constant_tsc arch_perfmon pebs bts aperfmperf pni dtes64 monitor ds_cpl est tm2 ssse3 xtpr pdcm movbe lahf_lm dtherm
    bogomips    : 3191.98
    clflush size    : 64
    cache_alignment : 64
    address sizes   : 32 bits physical, 32 bits virtual
    power management:

    processor   : 1
    vendor_id   : GenuineIntel
    cpu family  : 6
    model       : 28
    model name  : Intel(R) Atom(TM) CPU N270   @ 1.60GHz
    stepping    : 2
    microcode   : 0x212
    cpu MHz     : 1600.000
    cache size  : 512 KB
    physical id : 0
    siblings    : 1
    core id     : 0
    cpu cores   : 0
    apicid      : 1
    initial apicid  : 1
    fdiv_bug    : no
    hlt_bug     : no
    f00f_bug    : no
    coma_bug    : no
    fpu     : yes
    fpu_exception   : yes
    cpuid level : 10
    wp      : yes
    flags       : fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat clflush dts acpi mmx fxsr sse sse2 ss ht tm pbe constant_tsc arch_perfmon pebs bts aperfmperf pni dtes64 monitor ds_cpl est tm2 ssse3 xtpr pdcm movbe lahf_lm dtherm
    bogomips    : 3191.98
    clflush size    : 64
    cache_alignment : 64
    address sizes   : 32 bits physical, 32 bits virtual
    power management:

`user `[`$`]`lscpu`

    Architecture :        i686
    Mode(s) opératoire(s) des processeurs : 32-bit
    Boutisme :            Little Endian
    Processeur(s) :       2
    Liste de processeur(s) en ligne : 0,1
    Thread(s) par cœur : 2
    Cœur(s) par socket : 0
    Socket(s) :           2
    Identifiant constructeur : GenuineIntel
    Famille de processeur : 6
    Modèle :             28
    Nom de modèle :      Intel(R) Atom(TM) CPU N270   @ 1.60GHz
    Révision :           2
    Vitesse du processeur en MHz : 1600.000
    BogoMIPS :            3191.98
    Cache L1d :           24K
    Cache L1i :           32K
    Cache L2 :            512K

### [Memory]

-   1 GB of DDR2 533MHz memory

### [Graphics]

This Netbook has a 10 inch screen

`root `[`#`]`lspci -k -s 00:02.0`

    00:02.0 VGA compatible controller: Intel Corporation Mobile 945GSE Express Integrated Graphics Controller (rev 03)
        Subsystem: Acer Incorporated [ALI] Device 022f
        Kernel driver in use: i915
        Kernel modules: i915

#### [Frame Buffer]

[CODE]

    video=vesafb:1024x768-32@60

### [Ethernet]

`root `[`#`]`lspci -k -s 03:00.0`

    03:00.0 Ethernet controller: Qualcomm Atheros AR8132 Fast Ethernet (rev c0)
        Subsystem: Acer Incorporated [ALI] Device 022f
        Kernel driver in use: atl1c
        Kernel modules: atl1c

### [ACPI]

### [Wireless]

-   802.11b/g Wi-Fi CERTIFIED® wireless LAN card

`root `[`#`]`lspci -k -s 01:00.0`

    01:00.0 Network controller: Broadcom Corporation BCM4312 802.11b/g LP-PHY (rev 01)
        Subsystem: Foxconn International, Inc. T77H106.00 Wireless Half-size Mini PCIe Card
        Kernel driver in use: b43-pci-bridge
        Kernel modules: ssb

`root `[`#`]`grep b43 /proc/modules`

    b43 136216 0 - Live 0xf8283000
    mac80211 326274 1 b43, Live 0xf81ea000
    cfg80211 297999 2 b43,mac80211, Live 0xf810b000
    ssb 28693 1 b43, Live 0xf860f000

### [Sound]

`root `[`#`]`lspci -k -s 00:1b.0`

    00:1b.0 Audio device: Intel Corporation NM10/ICH7 Family High Definition Audio Controller (rev 02)
        Subsystem: Acer Incorporated [ALI] Device 022f
        Kernel driver in use: snd_hda_intel
        Kernel modules: snd_hda_intel

### [USB]

#### [2.0]

`root `[`#`]`lspci -k -s 00:1d.7`

    00:1d.7 USB controller: Intel Corporation NM10/ICH7 Family USB2 EHCI Controller (rev 02)
        Subsystem: Acer Incorporated [ALI] Device 022f
        Kernel driver in use: ehci-pci
        Kernel modules: ehci_pci

### [SATA]

`root `[`#`]`lspci -k -s 00:1f.2`

    00:1f.2 SATA controller: Intel Corporation 82801GBM/GHM (ICH7-M Family) SATA Controller [AHCI mode] (rev 02)
        Subsystem: Acer Incorporated [ALI] Device 022f
        Kernel driver in use: ahci

### [Webcam]

`root `[`#`]`lsusb -s 001:003`

    Bus 001 Device 003: ID 0c45:62c0 Microdia Sonix USB 2.0 Camera

### [Bluetooth]

** Note**\
Seems some models have Bluetooth

### [Touchpad]

### [Keyboard]

## [External resources]

-   [http://support.gateway.com/emachines/notebook/2009/emachines/em/em250/eM250sp2.shtml](http://support.gateway.com/emachines/notebook/2009/emachines/em/em250/eM250sp2.shtml) (Technical Specifications)
-   [http://support.gateway.com/emachines/Manuals/emachines/QS_eMachines_1_0_EN_EM250\_.pdf](http://support.gateway.com/emachines/Manuals/emachines/QS_eMachines_1_0_EN_EM250_.pdf) (User Manual)
-   [http://support.gateway.com/us/en/emac/product/default.aspx?modelId=1862](http://support.gateway.com/us/en/emac/product/default.aspx?modelId=1862) (Support)