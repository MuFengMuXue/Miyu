[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=Gigabyte_X570-UD&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

**Resources**

[[]][Home](https://www.gigabyte.com/Motherboard/X570-UD-rev-10)

[[]]This article has some todo items:\

-   What to do about sensors?
-   Is everything in lspci accounted for?
-   Most of the CPU-specific stuff should be folded into [Ryzen](https://wiki.gentoo.org/wiki/Ryzen "Ryzen")

## Contents

-   [[1] [General Information]](#General_Information)
-   [[2] [Hardware Specs]](#Hardware_Specs)
-   [[3] [Kernel Configuration]](#Kernel_Configuration)
    -   [[3.1] [CPU]](#CPU)
    -   [[3.2] [Storage Devices]](#Storage_Devices)
    -   [[3.3] [Sound]](#Sound)
    -   [[3.4] [Ethernet]](#Ethernet)
    -   [[3.5] [Peripherals]](#Peripherals)
    -   [[3.6] [Sensors]](#Sensors)
-   [[4] [Other details]](#Other_details)
    -   [[4.1] [lspci output]](#lspci_output)
    -   [[4.2] [dmesg excerpts]](#dmesg_excerpts)
    -   [[4.3] [Known hardware issues]](#Known_hardware_issues)

## [General Information]

This article details the Gigabyte X570-UD motherboard, providing Linux kernel configuration hints and outlines what to expect (including known hardware and firmware issues). The motherboard has an X570 chipset and AM4 CPU socket compatible with [Ryzen](https://wiki.gentoo.org/wiki/Ryzen "Ryzen") CPUs. This page is for the "rev 1.0" hardware, the only revision at the time of writing.

## [Hardware Specs]

+-----------------------------------+---------------------------------------------------------------------------+
| CPU Support                       | AM4 (znver2; supports Ryzen 7 and 9 models)                               |
+-----------------------------------+---------------------------------------------------------------------------+
| Memory                            | 4× DDR 4 slots, maximum 128GB DDR4-3200, XMP up to DDR4-4000              |
+-----------------------------------+---------------------------------------------------------------------------+
| Expansion Slots                   | -   1× PCIe 4.0 ×16                                                       |
|                                   | -   2× PCIe 4.0 ×4                                                        |
|                                   | -   2× PCIe 4.0 ×1                                                        |
+-----------------------------------+---------------------------------------------------------------------------+
| Internal Storage                  | -   6× SATA 6Gbit/s                                                       |
|                                   | -   1× M.2 PCIe 4.0 ×4                                                    |
|                                   | -   BIOS fake-RAID support                                                |
+-----------------------------------+---------------------------------------------------------------------------+
| Connectivity                      | -   4× USB 2.0 on rear panel, 4× internal headers                         |
|                                   | -   4× USB 3.2 on rear panel, 4× internal headers                         |
|                                   | -   1× TPM module internal header                                         |
|                                   | -   PS/2 mouse/keyboard combo port                                        |
|                                   | -   RTL8168 Gigabit ethernet                                              |
|                                   | -   Realtek HDA audio: 3 back ports, front mic/headphone internal headers |
|                                   | -   HDMI 2.0 on rear panel (only for Ryzen APUs)                          |
+-----------------------------------+---------------------------------------------------------------------------+

## [Kernel Configuration]

### [CPU]

This list is only a guideline, in particular note that current kernels (5.4) need to *disable* SME due to an incompatibility with the [amdgpu](https://wiki.gentoo.org/wiki/AMDGPU#AMD_Secure_Memory_Encryption "AMDGPU") driver.

[KERNEL]

    Processor type and features  --->
        [*] DMA memory allocation support
        [*] Symmetric multi-processing support
        [*] Support x2apic
        [*] Avoid speculative indirect branches in kernel
        [*] x86 CPU resource control support
        Processor family (AMD Zen 2)
        [*] Machine Check / overheating reporting
            [*]   AMD MCE features
        [*] CPU microcode loading support
        [*]   AMD microcode loading support
        [*] AMD Secure Memory Encryption (SME) support
        [ ]   Activate AMD Secure Memory Encryption (SME) by default
        [*] MTRR (Memory Type Range Register) support
            [*]   x86 PAT support
        [*] x86 architectural random number generator
        [*] Supervisor Mode Access Prevention
    Power management and ACPI options  --->
        CPU Frequency scaling  --->
            Default CPUFreq governor (schedutil)
            <*>   ACPI Processor P-States driver
            <*>   AMD frequency sensitivity feedback powersave bias
    [*] Virtualization  --->
        <M>   Kernel-based Virtual Machine (KVM) support
        <M>     KVM for AMD processors support
        [*]       AMD Secure Encrypted Virtualization (SEV) support
    Device Drivers  --->
        Character devices  --->
            <*> TPM Hardware Support  --->
                [*]   TPM HW Random Number Generator support
                <*>   TPM 2.0 CRB Interface
        -*- Hardware Monitoring support  --->
            <*>   AMD Family 10h+ temperature sensor
        [*] IOMMU Hardware Support  --->
            [*]   AMD IOMMU support
            <*>     AMD IOMMU Version 2 driver
            [*]   Support for Interrupt Remapping

The CCP is present but non-functional due to a broken BIOS:

[KERNEL]

    -*- Cryptographic API  --->
        [*]   Hardware crypto devices  --->
            [*]   Support for AMD Secure Processor
            <*>     Secure Processor device driver
            [*]       Cryptographic Coprocessor device
            <*>         Encryption and hashing offload support
            [*]       Platform Security Processor (PSP) device

[CODE] **dmesg**

    [  +0.013766] ccp 0000:0a:00.1: enabling device (0000 -> 0002)
    [  +0.000074] ccp 0000:0a:00.1: ccp: unable to access the device: you might be running a broken BIOS.
    [  +0.000027] ccp_crypto: Cannot load: there are no available CCPs

### [Storage Devices]

The NVMe driver has support for temperature sensors as of Linux 5.5.

[KERNEL] **01:00.0 Non-Volatile memory controller: (your device name here)**

    Device Drivers  --->
        NVME Support  --->
            <*> NVM Express block device
            [*] NVMe hardware monitoring

If you have SATA disks, the usual driver works. There are six physical ports spread across four PCIe devices, presumably to make virtualisation setups simpler.

[KERNEL] **0:00.0 SATA controller \[0106\]: Advanced Micro Devices, Inc. \[AMD\] FCH SATA Controller \[AHCI mode\] \[1022:7901\] (rev 51)**

    Device Drivers  --->
        <*> Serial ATA and Parallel ATA drivers (libata)  --->
            <*>   AHCI SATA support

### [Sound]

[KERNEL]

    Device Drivers  --->
        <*> Sound Card Support  --->
            <*> Advanced Linux Sound Architecture  --->
                HD-Audio  --->
                    <*> HD Audio PCI
                    <*> Build Realtek HD-audio codec support

### [Ethernet]

[KERNEL]

    Device Drivers  --->
        Networking support  --->
            [*] Network device support  --->
                [*] Ethernet driver support  --->
                    [*]   Realtek devices
                    <*>     Realtek 8169/8168/8101/8125 ethernet support

The NIC can have its firmware ([rtl_nic/rtl8168h-2.fw]) built into the kernel to silence a warning, though in practice it doesn\'t affect functionality.

### [Peripherals]

The XHCI driver covers all USB functionality, even the USB 2.0 ports.

[KERNEL]

    Device Drivers  --->
        [*] USB support  --->
            [*]   PCI based USB host interface
            <*>   xHCI HCD (USB 3.0) support

### [Sensors]

The following is correct for Linux 5.6:

-   The CPU supports the [k10temp] driver with ⅛°C resolution. Linux 5.6 also supports Fam17h voltage, current and per-core-complex temperatures.
-   ACPI Thermal Zone readings appear to be invalid and unchanging, at 16.8°C. [dmesg] contains warnings about "Invalid passive threshold" which might be related, but according to web search results this appears to be a BIOS bug.
-   The X570-UD has an IT8688 chip on an [i2c-piix4] bus. sensors-detect can see the IT8688 but [Linux **does not** have a driver for it](https://github.com/lm-sensors/lm-sensors/issues/154). The BIOS provides a configuration GUI for its various fan settings and temperature trip points.

Raw unfiltered sensor values for reference, using kernel 5.5.2 (with the k10temp patches from 5.6):

`user `[`$`]`sensors -jc /dev/null | sed -n '/k10temp\|acpitz/,/^ },$/ p'`

       "k10temp-pci-00c3":,
          "Vsoc":,
          "Tdie":,
          "Tctl":,
          "Tccd1":,
          "Tccd2":,
          "Icore":,
          "Isoc":
       },
       "acpitz-acpi-0":,
          "temp2":
       },

## [Other details]

### [lspci output]

[CODE] **lspci -nnk**

    00:00.0 Host bridge [0600]: Advanced Micro Devices, Inc. [AMD] Starship/Matisse Root Complex [1022:1480]
        Subsystem: Advanced Micro Devices, Inc. [AMD] Device [1022:1450]
    00:00.2 IOMMU [0806]: Advanced Micro Devices, Inc. [AMD] Starship/Matisse IOMMU [1022:1481]
        Subsystem: Advanced Micro Devices, Inc. [AMD] Starship/Matisse IOMMU [1022:1481]
    00:01.0 Host bridge [0600]: Advanced Micro Devices, Inc. [AMD] Starship/Matisse PCIe Dummy Host Bridge [1022:1482]
    00:01.1 PCI bridge [0604]: Advanced Micro Devices, Inc. [AMD] Starship/Matisse GPP Bridge [1022:1483]
        Kernel driver in use: pcieport
    00:01.2 PCI bridge [0604]: Advanced Micro Devices, Inc. [AMD] Starship/Matisse GPP Bridge [1022:1483]
        Kernel driver in use: pcieport
    00:02.0 Host bridge [0600]: Advanced Micro Devices, Inc. [AMD] Starship/Matisse PCIe Dummy Host Bridge [1022:1482]
    00:03.0 Host bridge [0600]: Advanced Micro Devices, Inc. [AMD] Starship/Matisse PCIe Dummy Host Bridge [1022:1482]
    00:03.1 PCI bridge [0604]: Advanced Micro Devices, Inc. [AMD] Starship/Matisse GPP Bridge [1022:1483]
        Kernel driver in use: pcieport
    00:04.0 Host bridge [0600]: Advanced Micro Devices, Inc. [AMD] Starship/Matisse PCIe Dummy Host Bridge [1022:1482]
    00:05.0 Host bridge [0600]: Advanced Micro Devices, Inc. [AMD] Starship/Matisse PCIe Dummy Host Bridge [1022:1482]
    00:07.0 Host bridge [0600]: Advanced Micro Devices, Inc. [AMD] Starship/Matisse PCIe Dummy Host Bridge [1022:1482]
    00:07.1 PCI bridge [0604]: Advanced Micro Devices, Inc. [AMD] Starship/Matisse Internal PCIe GPP Bridge 0 to bus[E:B] [1022:1484]
        Kernel driver in use: pcieport
    00:08.0 Host bridge [0600]: Advanced Micro Devices, Inc. [AMD] Starship/Matisse PCIe Dummy Host Bridge [1022:1482]
    00:08.1 PCI bridge [0604]: Advanced Micro Devices, Inc. [AMD] Starship/Matisse Internal PCIe GPP Bridge 0 to bus[E:B] [1022:1484]
        Kernel driver in use: pcieport
    00:08.2 PCI bridge [0604]: Advanced Micro Devices, Inc. [AMD] Starship/Matisse Internal PCIe GPP Bridge 0 to bus[E:B] [1022:1484]
        Kernel driver in use: pcieport
    00:08.3 PCI bridge [0604]: Advanced Micro Devices, Inc. [AMD] Starship/Matisse Internal PCIe GPP Bridge 0 to bus[E:B] [1022:1484]
        Kernel driver in use: pcieport
    00:14.0 SMBus [0c05]: Advanced Micro Devices, Inc. [AMD] FCH SMBus Controller [1022:790b] (rev 61)
        Subsystem: Gigabyte Technology Co., Ltd Device [1458:5001]
    00:14.3 ISA bridge [0601]: Advanced Micro Devices, Inc. [AMD] FCH LPC Bridge [1022:790e] (rev 51)
        Subsystem: Gigabyte Technology Co., Ltd Device [1458:5001]
    00:18.0 Host bridge [0600]: Advanced Micro Devices, Inc. [AMD] Matisse Device 24: Function 0 [1022:1440]
    00:18.1 Host bridge [0600]: Advanced Micro Devices, Inc. [AMD] Matisse Device 24: Function 1 [1022:1441]
    00:18.2 Host bridge [0600]: Advanced Micro Devices, Inc. [AMD] Matisse Device 24: Function 2 [1022:1442]
    00:18.3 Host bridge [0600]: Advanced Micro Devices, Inc. [AMD] Matisse Device 24: Function 3 [1022:1443]
        Kernel driver in use: k10temp
    00:18.4 Host bridge [0600]: Advanced Micro Devices, Inc. [AMD] Matisse Device 24: Function 4 [1022:1444]
    00:18.5 Host bridge [0600]: Advanced Micro Devices, Inc. [AMD] Matisse Device 24: Function 5 [1022:1445]
    00:18.6 Host bridge [0600]: Advanced Micro Devices, Inc. [AMD] Matisse Device 24: Function 6 [1022:1446]
    00:18.7 Host bridge [0600]: Advanced Micro Devices, Inc. [AMD] Matisse Device 24: Function 7 [1022:1447]
    02:00.0 PCI bridge [0604]: Advanced Micro Devices, Inc. [AMD] Device [1022:57ad]
        Kernel driver in use: pcieport
    03:04.0 PCI bridge [0604]: Advanced Micro Devices, Inc. [AMD] Device [1022:57a3]
        Kernel driver in use: pcieport
    03:08.0 PCI bridge [0604]: Advanced Micro Devices, Inc. [AMD] Device [1022:57a4]
        Kernel driver in use: pcieport
    03:09.0 PCI bridge [0604]: Advanced Micro Devices, Inc. [AMD] Device [1022:57a4]
        Kernel driver in use: pcieport
    03:0a.0 PCI bridge [0604]: Advanced Micro Devices, Inc. [AMD] Device [1022:57a4]
        Kernel driver in use: pcieport
    04:00.0 Ethernet controller [0200]: Realtek Semiconductor Co., Ltd. RTL8111/8168/8411 PCI Express Gigabit Ethernet Controller [10ec:8168] (rev 16)
        Subsystem: Gigabyte Technology Co., Ltd Onboard Ethernet [1458:e000]
        Kernel driver in use: r8169
    05:00.0 Non-Essential Instrumentation [1300]: Advanced Micro Devices, Inc. [AMD] Starship/Matisse Reserved SPP [1022:1485]
        Subsystem: Advanced Micro Devices, Inc. [AMD] Starship/Matisse Reserved SPP [1022:1485]
    05:00.1 USB controller [0c03]: Advanced Micro Devices, Inc. [AMD] Matisse USB 3.0 Host Controller [1022:149c]
        Subsystem: Advanced Micro Devices, Inc. [AMD] Device [1022:1486]
        Kernel driver in use: xhci_hcd
    05:00.3 USB controller [0c03]: Advanced Micro Devices, Inc. [AMD] Matisse USB 3.0 Host Controller [1022:149c]
        Subsystem: Advanced Micro Devices, Inc. [AMD] Device [1022:148c]
        Kernel driver in use: xhci_hcd
    06:00.0 SATA controller [0106]: Advanced Micro Devices, Inc. [AMD] FCH SATA Controller [AHCI mode] [1022:7901] (rev 51)
        Subsystem: Advanced Micro Devices, Inc. [AMD] FCH SATA Controller [AHCI mode] [1022:7901]
        Kernel driver in use: ahci
        Kernel modules: ahci
    07:00.0 SATA controller [0106]: Advanced Micro Devices, Inc. [AMD] FCH SATA Controller [AHCI mode] [1022:7901] (rev 51)
        Subsystem: Advanced Micro Devices, Inc. [AMD] FCH SATA Controller [AHCI mode] [1022:7901]
        Kernel driver in use: ahci
        Kernel modules: ahci
    09:00.0 Non-Essential Instrumentation [1300]: Advanced Micro Devices, Inc. [AMD] Starship/Matisse PCIe Dummy Function [1022:148a]
        Subsystem: Advanced Micro Devices, Inc. [AMD] Starship/Matisse PCIe Dummy Function [1022:148a]
    0a:00.0 Non-Essential Instrumentation [1300]: Advanced Micro Devices, Inc. [AMD] Starship/Matisse Reserved SPP [1022:1485]
        Subsystem: Advanced Micro Devices, Inc. [AMD] Starship/Matisse Reserved SPP [1022:1485]
    0a:00.1 Encryption controller [1080]: Advanced Micro Devices, Inc. [AMD] Starship/Matisse Cryptographic Coprocessor PSPCPP [1022:1486]
        Subsystem: Advanced Micro Devices, Inc. [AMD] Starship/Matisse Cryptographic Coprocessor PSPCPP [1022:1486]
        Kernel driver in use: ccp
        Kernel modules: ccp
    0a:00.3 USB controller [0c03]: Advanced Micro Devices, Inc. [AMD] Matisse USB 3.0 Host Controller [1022:149c]
        Subsystem: Gigabyte Technology Co., Ltd Device [1458:5007]
        Kernel driver in use: xhci_hcd
    0a:00.4 Audio device [0403]: Advanced Micro Devices, Inc. [AMD] Starship/Matisse HD Audio Controller [1022:1487]
        Subsystem: Gigabyte Technology Co., Ltd Device [1458:a184]
        Kernel driver in use: snd_hda_intel
    0b:00.0 SATA controller [0106]: Advanced Micro Devices, Inc. [AMD] FCH SATA Controller [AHCI mode] [1022:7901] (rev 51)
        Subsystem: Gigabyte Technology Co., Ltd Device [1458:b002]
        Kernel driver in use: ahci
        Kernel modules: ahci
    0c:00.0 SATA controller [0106]: Advanced Micro Devices, Inc. [AMD] FCH SATA Controller [AHCI mode] [1022:7901] (rev 51)
        Subsystem: Gigabyte Technology Co., Ltd Device [1458:b002]
        Kernel driver in use: ahci
        Kernel modules: ahci

### [dmesg excerpts]

The usual set of x86 hardware vulnerabilities have to be worked around:

[CODE]

    [  +0.000002] Spectre V1 : Mitigation: usercopy/swapgs barriers and __user pointer sanitization
    [  +0.000002] Spectre V2 : Mitigation: Full AMD retpoline
    [  +0.000002] Spectre V2 : Spectre v2 / SpectreRSB mitigation: Filling RSB on context switch
    [  +0.000002] Spectre V2 : mitigation: Enabling conditional Indirect Branch Prediction Barrier
    [  +0.000002] Spectre V2 : User space: Mitigation: STIBP via seccomp and prctl
    [  +0.000001] Speculative Store Bypass: Mitigation: Speculative Store Bypass disabled via prctl and seccomp

The BIOS wants to know if we\'re running Linux, for some reason:

[CODE]

    [  +0.004069] ACPI: 8 ACPI AML tables successfully acquired and loaded
    [  +0.000559] ACPI: [Firmware Bug]: BIOS _OSI(Linux) query ignored

Some messages about badly-provisoned onboard PCIe devices:

[CODE]

    [  +0.000000] pci 0000:02:00.0: 63.012 Gb/s available PCIe bandwidth, limited by 16 GT/s x4 link at 0000:00:01.2 (capable of 126.024 Gb/s with 16 GT/s x8 link)
    [  +0.000153] pci 0000:05:00.0: 63.012 Gb/s available PCIe bandwidth, limited by 16 GT/s x4 link at 0000:00:01.2 (capable of 252.048 Gb/s with 16 GT/s x16 link)
    [  +0.000081] pci 0000:06:00.0: 63.012 Gb/s available PCIe bandwidth, limited by 16 GT/s x4 link at 0000:00:01.2 (capable of 252.048 Gb/s with 16 GT/s x16 link)
    [  +0.000081] pci 0000:07:00.0: 63.012 Gb/s available PCIe bandwidth, limited by 16 GT/s x4 link at 0000:00:01.2 (capable of 252.048 Gb/s with 16 GT/s x16 link)

Buggy ACPI:

[CODE]

    [  +1.039967] ACPI: Invalid passive threshold
    [  +0.000525] thermal LNXTHERM:00: registered as thermal_zone0
    [  +0.000406] ACPI: Thermal Zone [TZ10] (17 C)
    [  +0.000434] ACPI: Invalid passive threshold
    [  +0.000426] thermal LNXTHERM:01: registered as thermal_zone1
    [  +0.000399] ACPI: Thermal Zone [PCT0] (17 C)

[CODE]

    [  +0.000054] ACPI Warning: SystemIO range 0x0000000000000B00-0x0000000000000B08 conflicts with OpRegion 0x0000000000000B00-0x0000000000000B0F (\GSA1.SMBI) (20191018/utaddress-204)
    [  +0.000036] ACPI: If an ACPI driver is available for this device, you should use it instead of the native driver

Buggy USB 3.1 controllers:

[CODE]

    [  +0.000139] xhci_hcd 0000:05:00.1: xHCI Host Controller
    [  +0.000013] xhci_hcd 0000:05:00.1: new USB bus registered, assigned bus number 2
    [  +0.000016] xhci_hcd 0000:05:00.1: Host supports USB 3.1 Enhanced SuperSpeed
    [  +0.000024] usb usb2: We don't know the algorithms for LPM for this host, disabling LPM.
    […]
    [  +0.000024] usb usb4: We don't know the algorithms for LPM for this host, disabling LPM.
    [  +0.000026] usb: port power management may be unreliable
    [  +0.000021] usb usb6: We don't know the algorithms for LPM for this host, disabling LPM.

There is a watchdog timer chip physically present, but not usable:

[CODE]

    [  +0.000045] sp5100_tco: SP5100/SB800 TCO WatchDog Timer Driver
    [  +0.000033] sp5100-tco sp5100-tco: Using 0xfed80b00 for watchdog MMIO address
    [  +0.000020] sp5100-tco sp5100-tco: Watchdog hardware is disabled

### [Known hardware issues]

-   Many of AMD\'s AM4 CPUs come with an animated RGB LED heatsink fan, which some may find irritating. It can be disabled (persistently) using the included USB cable and [cm-rgb](https://github.com/gfduszynski/cm-rgb).
-   If boot ends in a hard reset more than once in a row (e.g. due to a kernel misconfiguration), the firmware will reset its settings back to factory defaults. To lessen the impact of this, use the "Save Profile" option in the BIOS menu to keep a backup of known-working settings, and use [kexec](https://wiki.gentoo.org/wiki/Kexec "Kexec") to test new kernels and avoid doing a cold reboot.
-   Do *not* change [Default ASPM policy] from \"BIOS default\" in the kernel, as the power saving modes will cause various peripherals (including NVMe) to go missing during boot.