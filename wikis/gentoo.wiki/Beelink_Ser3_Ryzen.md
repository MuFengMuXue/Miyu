[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=Beelink_Ser3_Ryzen&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

## Contents

-   [[1] [Hardware]](#Hardware)
    -   [[1.1] [BIOS]](#BIOS)
    -   [[1.2] [CPU]](#CPU)
    -   [[1.3] [Graphics]](#Graphics)
    -   [[1.4] [Ethernet]](#Ethernet)
    -   [[1.5] [ACPI]](#ACPI)
    -   [[1.6] [Wireless]](#Wireless)
    -   [[1.7] [Sound]](#Sound)
    -   [[1.8] [USB]](#USB)
    -   [[1.9] [SATA, PCI]](#SATA.2C_PCI)
    -   [[1.10] [NVME SSD]](#NVME_SSD)
    -   [[1.11] [Webcam]](#Webcam)
    -   [[1.12] [Bluetooth]](#Bluetooth)

## [Hardware]

`root `[`#`]`lspci`

    00:00.0 Host bridge: Advanced Micro Devices, Inc. [AMD] Raven/Raven2 Root Complex
    00:00.2 IOMMU: Advanced Micro Devices, Inc. [AMD] Raven/Raven2 IOMMU
    00:01.0 Host bridge: Advanced Micro Devices, Inc. [AMD] Family 17h (Models 00h-1fh) PCIe Dummy Host Bridge
    00:01.2 PCI bridge: Advanced Micro Devices, Inc. [AMD] Raven/Raven2 PCIe GPP Bridge [6:0]
    00:01.3 PCI bridge: Advanced Micro Devices, Inc. [AMD] Raven/Raven2 PCIe GPP Bridge [6:0]
    00:01.4 PCI bridge: Advanced Micro Devices, Inc. [AMD] Raven/Raven2 PCIe GPP Bridge [6:0]
    00:08.0 Host bridge: Advanced Micro Devices, Inc. [AMD] Family 17h (Models 00h-1fh) PCIe Dummy Host Bridge
    00:08.1 PCI bridge: Advanced Micro Devices, Inc. [AMD] Raven/Raven2 Internal PCIe GPP Bridge 0 to Bus A
    00:08.2 PCI bridge: Advanced Micro Devices, Inc. [AMD] Raven/Raven2 Internal PCIe GPP Bridge 0 to Bus B
    00:14.0 SMBus: Advanced Micro Devices, Inc. [AMD] FCH SMBus Controller (rev 61)
    00:14.3 ISA bridge: Advanced Micro Devices, Inc. [AMD] FCH LPC Bridge (rev 51)
    00:18.0 Host bridge: Advanced Micro Devices, Inc. [AMD] Raven/Raven2 Device 24: Function 0
    00:18.1 Host bridge: Advanced Micro Devices, Inc. [AMD] Raven/Raven2 Device 24: Function 1
    00:18.2 Host bridge: Advanced Micro Devices, Inc. [AMD] Raven/Raven2 Device 24: Function 2
    00:18.3 Host bridge: Advanced Micro Devices, Inc. [AMD] Raven/Raven2 Device 24: Function 3
    00:18.4 Host bridge: Advanced Micro Devices, Inc. [AMD] Raven/Raven2 Device 24: Function 4
    00:18.5 Host bridge: Advanced Micro Devices, Inc. [AMD] Raven/Raven2 Device 24: Function 5
    00:18.6 Host bridge: Advanced Micro Devices, Inc. [AMD] Raven/Raven2 Device 24: Function 6
    00:18.7 Host bridge: Advanced Micro Devices, Inc. [AMD] Raven/Raven2 Device 24: Function 7
    01:00.0 Network controller: Intel Corporation Wireless 3165 (rev 81)
    02:00.0 Ethernet controller: Realtek Semiconductor Co., Ltd. RTL8111/8168/8411 PCI Express Gigabit Ethernet Controller (rev 15)
    03:00.0 Non-Volatile memory controller: Intel Corporation SSD 660P Series (rev 03)
    04:00.0 VGA compatible controller: Advanced Micro Devices, Inc. [AMD/ATI] Picasso/Raven 2 [Radeon Vega Series / Radeon Vega Mobile Series] (rev c2)
    04:00.1 Audio device: Advanced Micro Devices, Inc. [AMD/ATI] Raven/Raven2/Fenghuang HDMI/DP Audio Controller
    04:00.2 Encryption controller: Advanced Micro Devices, Inc. [AMD] Family 17h (Models 10h-1fh) Platform Security Processor
    04:00.3 USB controller: Advanced Micro Devices, Inc. [AMD] Raven USB 3.1
    04:00.4 USB controller: Advanced Micro Devices, Inc. [AMD] Raven USB 3.1
    04:00.5 Multimedia controller: Advanced Micro Devices, Inc. [AMD] ACP/ACP3X/ACP6x Audio Coprocessor
    04:00.6 Audio device: Advanced Micro Devices, Inc. [AMD] Family 17h/19h HD Audio Controller
    04:00.7 Non-VGA unclassified device: Advanced Micro Devices, Inc. [AMD] Raven/Raven2/Renoir Non-Sensor Fusion Hub KMDF driver
    05:00.0 SATA controller: Advanced Micro Devices, Inc. [AMD] FCH SATA Controller [AHCI mode] (rev 61)

### [BIOS]

### [CPU]

The CPU is an AMD Ryzen 5 3550H with eight cores.

`user `[`$`]`cat /proc/cpuinfo`

    processor   : 0
    vendor_id   : AuthenticAMD
    cpu family  : 23
    model       : 24
    model name  : AMD Ryzen 5 3550H with Radeon Vega Mobile Gfx
    stepping    : 1
    microcode   : 0x8108102
    cpu MHz     : 2844.579
    cache size  : 512 KB
    physical id : 0
    siblings    : 8
    core id     : 0
    cpu cores   : 4
    apicid      : 0
    initial apicid  : 0
    fpu     : yes
    fpu_exception   : yes
    cpuid level : 13
    wp      : yes
    flags       : fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush mmx fxsr sse sse2 ht syscall nx mmxext fxsr_opt pdpe1gb rdtscp lm constant_tsc rep_good nopl nonstop_tsc cpuid extd_apicid aperfmperf rapl pni pclmulqdq monitor ssse3 fma cx16 sse4_1 sse4_2 movbe popcnt aes xsave avx f16c rdrand lahf_lm cmp_legacy svm extapic cr8_legacy abm sse4a misalignsse 3dnowprefetch osvw skinit wdt tce topoext perfctr_core perfctr_nb bpext perfctr_llc mwaitx cpb hw_pstate ssbd ibpb vmmcall fsgsbase bmi1 avx2 smep bmi2 rdseed adx smap clflushopt sha_ni xsaveopt xsavec xgetbv1 xsaves clzero irperf xsaveerptr arat npt lbrv svm_lock nrip_save tsc_scale vmcb_clean flushbyasid decodeassists pausefilter pfthreshold avic v_vmsave_vmload vgif overflow_recov succor smca sme sev sev_es
    bugs        : sysret_ss_attrs null_seg spectre_v1 spectre_v2 spec_store_bypass retbleed
    bogomips    : 4193.61
    TLB size    : 2560 4K pages
    clflush size    : 64
    cache_alignment : 64
    address sizes   : 43 bits physical, 48 bits virtual
    power management: ts ttp tm hwpstate eff_freq_ro [13] [14]

### [Graphics]

The CPU provides Radeon Vega Mobile graphics, which claims 2Gb of main memory for video. Follow the instructions in the [AMDGPU](https://wiki.gentoo.org/wiki/AMDGPU "AMDGPU") article.

`root `[`#`]`lspci -k -s 04:00.0`

    04:00.0 VGA compatible controller: Advanced Micro Devices, Inc. [AMD/ATI] Picasso/Raven 2 [Radeon Vega Series / Radeon Vega Mobile Series] (rev c2)
            Subsystem: Advanced Micro Devices, Inc. [AMD/ATI] Picasso/Raven 2 [Radeon Vega Series / Radeon Vega Mobile Series]
            Kernel driver in use: amdgpu
            Kernel modules: amdgpu

### [Ethernet]

`root `[`#`]`lspci -k -s 02:00.0`

    02:00.0 Ethernet controller: Realtek Semiconductor Co., Ltd. RTL8111/8168/8411 PCI Express Gigabit Ethernet Controller (rev 15)
            DeviceName: Onboard LAN Brodcom
            Subsystem: Realtek Semiconductor Co., Ltd. RTL8111/8168/8411 PCI Express Gigabit Ethernet Controller
            Kernel driver in use: r8169
            Kernel modules: r8169

### [ACPI]

### [Wireless]

`root `[`#`]`lspci -k -s 01:00.0`

    01:00.0 Network controller: Intel Corporation Wireless 3165 (rev 81)
            Subsystem: Intel Corporation Dual Band Wireless AC 3165
            Kernel driver in use: iwlwifi
            Kernel modules: iwlwifi

### [Sound]

The device features AMD/Realtek HD audio.

`root `[`#`]`lspci -k -s 04:00.1`

    04:00.1 Audio device: Advanced Micro Devices, Inc. [AMD/ATI] Raven/Raven2/Fenghuang HDMI/DP Audio Controller
            Subsystem: Advanced Micro Devices, Inc. [AMD/ATI] Raven/Raven2/Fenghuang HDMI/DP Audio Controller
            Kernel driver in use: snd_hda_intel
            Kernel modules: snd_hda_intel

Configure [ALSA](https://wiki.gentoo.org/wiki/ALSA "ALSA") with the following driver settings:

[KERNEL]

    Device Drivers --->
        <*> Sound card support
            <*> Advanced Linux Sound Architecture --->
                HD-Audio  --->
                    -*- Allow dynamic codec reconfiguration
                    [*] Support initialization patch loading for HD-audio
                    <*> Build Realtek HD-audio codec support
                    <*> Build HDMI/DisplayPort HD-audio codec support
                    -*- Enable generic HD-audio codec parser
              (2048) Pre-allocated buffer size for HD-audio driver

### [USB]

### [][SATA, PCI]

### [NVME SSD]

### [Webcam]

### [Bluetooth]