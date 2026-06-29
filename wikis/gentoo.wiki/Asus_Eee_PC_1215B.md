[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=ASUS_Eee_PC_1215B&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

[![1215B red asus eeepc-550x382.jpg](/images/0/0f/1215B_red_asus_eeepc-550x382.jpg)](https://wiki.gentoo.org/wiki/File:1215B_red_asus_eeepc-550x382.jpg)

## Contents

-   [[1] [Hardware]](#Hardware)
    -   [[1.1] [BIOS]](#BIOS)
    -   [[1.2] [CPU]](#CPU)
    -   [[1.3] [Graphics]](#Graphics)
        -   [[1.3.1] [Frame Buffer]](#Frame_Buffer)
    -   [[1.4] [Ethernet]](#Ethernet)
    -   [[1.5] [ACPI]](#ACPI)
    -   [[1.6] [Wireless]](#Wireless)
    -   [[1.7] [Sound]](#Sound)
    -   [[1.8] [USB]](#USB)
        -   [[1.8.1] [1.1]](#1.1)
        -   [[1.8.2] [2.0]](#2.0)
        -   [[1.8.3] [3.0]](#3.0)
    -   [[1.9] [SATA, PCI]](#SATA.2C_PCI)
    -   [[1.10] [Webcam]](#Webcam)
    -   [[1.11] [Bluetooth]](#Bluetooth)
    -   [[1.12] [Touchpad]](#Touchpad)
    -   [[1.13] [Keyboard]](#Keyboard)
        -   [[1.13.1] [Special keys]](#Special_keys)

## [Hardware]

`root `[`#`]`lspci`

    00:00.0 Host bridge: Advanced Micro Devices [AMD] Device 1510
    00:01.0 VGA compatible controller: ATI Technologies Inc Device 9806
    00:01.1 Audio device: ATI Technologies Inc Device 1314
    00:04.0 PCI bridge: Advanced Micro Devices [AMD] Device 1512
    00:05.0 PCI bridge: Advanced Micro Devices [AMD] Device 1513
    00:11.0 SATA controller: ATI Technologies Inc SB700/SB800 SATA Controller [AHCI mode]
    00:12.0 USB Controller: ATI Technologies Inc SB700/SB800 USB OHCI0 Controller
    00:12.2 USB Controller: ATI Technologies Inc SB700/SB800 USB EHCI Controller
    00:13.0 USB Controller: ATI Technologies Inc SB700/SB800 USB OHCI0 Controller
    00:13.2 USB Controller: ATI Technologies Inc SB700/SB800 USB EHCI Controller
    00:14.0 SMBus: ATI Technologies Inc SBx00 SMBus Controller (rev 42)
    00:14.2 Audio device: ATI Technologies Inc SBx00 Azalia (Intel HDA) (rev 40)
    00:14.3 ISA bridge: ATI Technologies Inc SB700/SB800 LPC host controller (rev 40)
    00:14.4 PCI bridge: ATI Technologies Inc SBx00 PCI to PCI Bridge (rev 40)
    00:15.0 PCI bridge: ATI Technologies Inc Device 43a0
    00:15.2 PCI bridge: ATI Technologies Inc Device 43a2
    00:18.0 Host bridge: Advanced Micro Devices [AMD] Device 1700 (rev 43)
    00:18.1 Host bridge: Advanced Micro Devices [AMD] Device 1701
    00:18.2 Host bridge: Advanced Micro Devices [AMD] Device 1702
    00:18.3 Host bridge: Advanced Micro Devices [AMD] Device 1703
    00:18.4 Host bridge: Advanced Micro Devices [AMD] Device 1704
    00:18.5 Host bridge: Advanced Micro Devices [AMD] Device 1718
    00:18.6 Host bridge: Advanced Micro Devices [AMD] Device 1716
    00:18.7 Host bridge: Advanced Micro Devices [AMD] Device 1719
    01:00.0 Network controller: Broadcom Corporation Device 4727 (rev 01)
    02:00.0 Ethernet controller: Attansic Technology Corp. Device 2062 (rev c1)
    07:00.0 USB Controller: Device 1b21:1042

### [BIOS]

### [CPU]

The CPU is an AMD E-450 with 2 cores.

`user `[`$`]`cat /proc/cpuinfo`

    processor : 0
    vendor_id   : AuthenticAMD
    cpu family  : 20
    model       : 2
    model name  : AMD E-450 APU with Radeon(tm) HD Graphics
    stepping    : 0
    cpu MHz     : 1646.232
    cache size  : 512 KB
    physical id : 0
    siblings    : 2
    core id     : 0
    cpu cores   : 2
    apicid      : 0
    initial apicid  : 0
    fpu     : yes
    fpu_exception   : yes
    cpuid level : 6
    wp      : yes
    flags       : fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush mmx fxsr sse
                      sse2 ht syscall nx mmxext fxsr_opt pdpe1gb rdtscp lm constant_tsc rep_good nopl nonstop_tsc
                      extd_apicid aperfmperf pni monitor ssse3 cx16 popcnt lahf_lm cmp_legacy svm extapic cr8_legacy
                      abm sse4a misalignsse 3dnowprefetch ibs skinit wdt arat npt lbrv svm_lock nrip_save pausefilter
    bogomips    : 3292.46
    TLB size    : 1024 4K pages
    clflush size    : 64
    cache_alignment : 64
    address sizes   : 36 bits physical, 48 bits virtual
    power management: ts ttp tm stc 100mhzsteps hwpstate

Some CPU feature flags:

-   [sse](https://en.wikipedia.org/wiki/Streaming_SIMD_Extensions "wikipedia:Streaming SIMD Extensions"),
-   [sse2](https://en.wikipedia.org/wiki/SSE2 "wikipedia:SSE2"),
-   [ht](https://en.wikipedia.org/wiki/HyperTransport "wikipedia:HyperTransport"),
-   [nx](https://en.wikipedia.org/wiki/NX_bit "wikipedia:NX bit"),
-   [ssse3](https://en.wikipedia.org/wiki/SSSE3 "wikipedia:SSSE3"),
-   [svm](https://en.wikipedia.org/wiki/AMD-V#AMD_virtualization_.28AMD-V.29 "wikipedia:AMD-V"),
-   [sse4a](https://en.wikipedia.org/wiki/SSE4a#SSE4a "wikipedia:SSE4a"),
-   [CPU - Register Acronyms](http://boincfaq.mundayweb.com/index.php?language=1&view=176),
-   [CPU feature flags and their meanings](http://blog.incase.de/index.php/cpu-feature-flags-and-their-meanings/).

`user `[`$`]`lscpu`

    Architecture:          x86_64
    CPU op-mode(s):        32-bit, 64-bit
    Byte Order:            Little Endian
    CPU(s):                2
    On-line CPU(s) list:   0,1
    Thread(s) per core:    1
    Core(s) per socket:    2
    CPU socket(s):         1
    NUMA node(s):          1
    Vendor ID:             AuthenticAMD
    CPU family:            20
    Model:                 2
    Stepping:              0
    CPU MHz:               1646.572
    BogoMIPS:              3292.69
    Virtualization:        AMD-V
    L1d cache:             32K
    L1i cache:             32K
    L2 cache:              512K
    NUMA node0 CPU(s):     0,1

### [Graphics]

The GPU is Radeon HD 6320 ([Evergreen series](https://en.wikipedia.org/wiki/Comparison_of_AMD_graphics_processing_units#IGP_.28HD_6xxx.29 "wikipedia:Comparison of AMD graphics processing units")). Follow the instructions in the [radeon](https://wiki.gentoo.org/wiki/Radeon "Radeon") article.

`root `[`#`]`lspci -k -s 00:01.0`

    00:01.0 VGA compatible controller: ATI Technologies Inc Device 9806
        Subsystem: ASUSTeK Computer Inc. Device 84e3
        Kernel driver in use: radeon
        Kernel modules: radeon

#### [Frame Buffer]

### [Ethernet]

`root `[`#`]`lspci -k -s 02:0.0`

    02:00.0 Ethernet controller: Attansic Technology Corp. Device 2062 (rev c1)
        Subsystem: ASUSTeK Computer Inc. Device 8468
        Kernel driver in use: atl1c

### [ACPI]

`root `[`#`]`lspci -k -s 00:18.3`

    00:18.3 Host bridge: Advanced Micro Devices [AMD] Device 1703
        Kernel driver in use: k10temp
        Kernel modules: k10temp

### [Wireless]

`root `[`#`]`lspci -k -s 01:00.0`

    01:00.0 Network controller: Broadcom Corporation Device 4727 (rev 01)
        Subsystem: Device 1a3b:2047
        Kernel modules: brcmsmac

### [Sound]

`root `[`#`]`lspci -k -s 00:01.1`

    00:01.1 Audio device: ATI Technologies Inc Device 1314
        Subsystem: ASUSTeK Computer Inc. Device 84e3
        Kernel driver in use: snd_hda_intel
        Kernel modules: snd-hda-intel

`root `[`#`]`lspci -k -s 00:14.2`

    00:14.2 Audio device: ATI Technologies Inc SBx00 Azalia (Intel HDA) (rev 40)
        Subsystem: ASUSTeK Computer Inc. Device 841c
        Kernel driver in use: snd_hda_intel
        Kernel modules: snd-hda-intel

### [USB]

#### [1.1]

`root `[`#`]`lspci -k -s 00:12.0`

    00:12.0 USB Controller: ATI Technologies Inc SB700/SB800 USB OHCI0 Controller
        Subsystem: ATI Technologies Inc SB700/SB800 USB OHCI0 Controller
        Kernel driver in use: ohci_hcd

`root `[`#`]`lspci -k -s 00:13.0`

    00:13.0 USB Controller: ATI Technologies Inc SB700/SB800 USB OHCI0 Controller
        Subsystem: ATI Technologies Inc SB700/SB800 USB OHCI0 Controller
        Kernel driver in use: ohci_hcd

#### [2.0]

`root `[`#`]`lspci -k -s 00:12.2`

    00:12.2 USB Controller: ATI Technologies Inc SB700/SB800 USB EHCI Controller
        Subsystem: ATI Technologies Inc SB700/SB800 USB EHCI Controller
        Kernel driver in use: ehci_hcd

`root `[`#`]`lspci -k -s 00:13.2`

    00:13.2 USB Controller: ATI Technologies Inc SB700/SB800 USB EHCI Controller
        Subsystem: ATI Technologies Inc SB700/SB800 USB EHCI Controller
        Kernel driver in use: ehci_hcd

#### [3.0]

`root `[`#`]`lspci -k -s 07:00.0`

    07:00.0 USB Controller: Device 1b21:1042
        Subsystem: ASUSTeK Computer Inc. Device 8488
        Kernel driver in use: xhci_hcd

### [][SATA, PCI]

`root `[`#`]`lspci -k -s 00:04.0`

    00:04.0 PCI bridge: Advanced Micro Devices [AMD] Device 1512
        Kernel driver in use: pcieport

`root `[`#`]`lspci -k -s 00:05.0`

    00:05.0 PCI bridge: Advanced Micro Devices [AMD] Device 1513
        Kernel driver in use: pcieport

`root `[`#`]`lspci -k -s 00:15.0`

    00:15.0 PCI bridge: ATI Technologies Inc Device 43a0
        Kernel driver in use: pcieport

`root `[`#`]`lspci -k -s 00:15.2`

    00:15.2 PCI bridge: ATI Technologies Inc Device 43a2
        Kernel driver in use: pcieport

`root `[`#`]`lspci -k -s 00:11.0`

    00:11.0 SATA controller: ATI Technologies Inc SB700/SB800 SATA Controller [AHCI mode]
        Subsystem: ATI Technologies Inc Device 4390
        Kernel driver in use: ahci

`root `[`#`]`lspci -k -s 00:14.0`

    00:14.0 SMBus: ATI Technologies Inc SBx00 SMBus Controller (rev 42)
        Subsystem: ATI Technologies Inc SBx00 SMBus Controller
        Kernel driver in use: piix4_smbus
        Kernel modules: sp5100_tco, i2c-piix4

### [Webcam]

### [Bluetooth]

### [Touchpad]

### [Keyboard]

#### [Special keys]