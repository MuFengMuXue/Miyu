The Beelink SER5 AMD Ryzen 5 5560U Mini PC was produced in 2022, then discontinued after a bad batch of motherboards resulted in many users having hardware issues^[\[1\]](#cite_note-discontinued-1)[\[2\]](#cite_note-issues-2)[\[3\]](#cite_note-threads-3)[\[4\]](#cite_note-redditissue-4)^. If one is lucky enough to have a non-defective board, it makes a fantastic mini PC that Gentoo runs quite well on (this article was written on it). According to this^[\[5\]](#cite_note-bios-5)^ post, the latest BIOS version is FP655U504 09/13/2022, and the drivers are the same as for the 5600 model^[\[6\]](#cite_note-drivers-6)^. The original ads for the product can be found here^[\[7\]](#cite_note-xpc-7)[\[8\]](#cite_note-xpcarchive-8)^. The Ryzen 5 5560U is a Zen 3 chip and part of the Cezanne family^[\[9\]](#cite_note-amd-9)^.

\

## Contents

-   [[1] [Hardware]](#Hardware)
    -   [[1.1] [Standard]](#Standard)
-   [[2] [Installation]](#Installation)
    -   [[2.1] [make.conf]](#make.conf)
    -   [[2.2] [Firmware]](#Firmware)
    -   [[2.3] [Kernel]](#Kernel)
    -   [[2.4] [Emerge]](#Emerge)
    -   [[2.5] [GPU software support notes]](#GPU_software_support_notes)
-   [[3] [See also]](#See_also)
-   [[4] [References]](#References)

## [Hardware]

### [Standard]

  -------------------------------- ------------------------------------------------------------------------------------------------------------------------------------- ------------- ------------------------- ---------------- ---------------------------------------------------------------------------------------- --
  Device                           Make/model                                                                                                                            Status        Kernel driver(s)          Kernel version   Notes
  CPU                              AMD Ryzen 5 5560U                                                                                                                     Works         N/A                       6.1.31           Zen 3
  GPU                              AMD Radeon Graphics, Cezanne \[Radeon Vega Series / Radeon Vega Mobile Series\] (rev c3)                                              Works         amdgpu                    6.1.31           Integrated Ryzen 5000 graphics, \"Green Sardine\" codename^[\[9\]](#cite_note-amd-9)^.
  Host Bridge                      Advanced Micro Devices, Inc. \[AMD\] Renoir/Cezanne Root Complex                                                                      Works         N/A                       6.1.31
  Host Bridge                      Advanced Micro Devices, Inc. \[AMD\] Cezanne Data Fabric                                                                              Works         k10temp                   6.1.31
  PCI Bridge                       Advanced Micro Devices, Inc. \[AMD\] Renoir/Cezanne PCIe GPP Bridge                                                                   Works         pcieport                  6.1.31
  SMBus                            Advanced Micro Devices, Inc. \[AMD\] FCH SMBus Controller (rev 51)                                                                    Works         piix4_smbus, sp5100_tco   6.1.31
  Ethernet controller              Realtek Semiconductor Co., Ltd. RTL8111/8168/8411 PCI Express Gigabit Ethernet Controller (rev 15)                                    Works         r8169                     6.1.31
  Network controller               MEDIATEK Corp. MT7921K (RZ608) Wi-Fi 6E 80MHz                                                                                         Works         mt7921e                   6.1.31           Bluetooth works after adding the firmware files listed below.
  Non-Volatile memory controller   Intel Corporation Device f1aa (rev 03)                                                                                                Works         nvme                      6.1.31
  Audio device                     Advanced Micro Devices, Inc. \[AMD/ATI\] Renoir Radeon High Definition Audio Controller, \[AMD\] Family 17h/19h HD Audio Controller   Works         snd_hda_intel             6.1.31
  Multimedia controller            Advanced Micro Devices, Inc. \[AMD\] ACP/ACP3X/ACP6x Audio Coprocessor (rev 01)                                                       Works         snd_rn_pci_acp3x          6.1.31
  Encryption controller            Advanced Micro Devices, Inc. \[AMD\] Family 17h (Models 10h-1fh) Platform Security Processor                                          Not tested    ccp                       6.1.31
  USB controller                   Advanced Micro Devices, Inc. \[AMD\] Renoir/Cezanne USB 3.1                                                                           Works         xhci_hcd                  6.1.31
  -------------------------------- ------------------------------------------------------------------------------------------------------------------------------------- ------------- ------------------------- ---------------- ---------------------------------------------------------------------------------------- --

`root `[`#`]`lscpu`

    Architecture:            x86_64
      CPU op-mode(s):        32-bit, 64-bit
      Address sizes:         48 bits physical, 48 bits virtual
      Byte Order:            Little Endian
    CPU(s):                  12
      On-line CPU(s) list:   0-11
    Vendor ID:               AuthenticAMD
      BIOS Vendor ID:        Advanced Micro Devices, Inc.
      Model name:            AMD Ryzen 5 5560U with Radeon Graphics
        BIOS Model name:     AMD Ryzen 5 5560U with Radeon Graphics          Unknown CPU @ 2.3GHz
        BIOS CPU family:     107
        CPU family:          25
        Model:               80
        Thread(s) per core:  2
        Core(s) per socket:  6
        Socket(s):           1
        Stepping:            0
        Frequency boost:     enabled
        CPU(s) scaling MHz:  52%
        CPU max MHz:         4060.9370
        CPU min MHz:         1600.0000
        BogoMIPS:            4593.59
        Flags:               stop_tsc cpuid extd_apicid aperfmperf rapl pni pclmulqdq monitor ssse3 fma cx16 sse4_1 sse4_2 movbe popcnt aes xsave avx f16c rdrand lahf_lm cmp_legacy svm extapic cr8_legacy abm sse4a misalignsse 3dnowprefetch osvw ibs skinit wdt tce topoext perfctr_core perfctr_nb bpext perfctr_llc mwaitx cpb cat_l3 cdp_l3 hw_pstate ssbd mba ibrs ibpb stibp vmmcall fsgsbase bmi1 avx2 smep bmi2 erms invpcid cqm rdt_a rdseed adx smap clflushopt clwb sha_ni xsaveopt xsavec xgetbv1 xsaves cqm_llc cqm_occup_llc cqm_mbm_total cqm_mbm_local clzero irperf xsaveerptr rdpru wbnoinvd cppc arat npt lbrv svm_lock nrip_save tsc_scale vmcb_clean flushbyasid decodeassists pausefilter pfthreshold avic v_vmsave_vmload vgif v_spec_ctrl umip pku ospke vaes vpclmulqdq rdpid overflow_recov succor smca fsrm
    Virtualization features:
      Virtualization:        AMD-V
    Caches (sum of all):
      L1d:                   192 KiB (6 instances)
      L1i:                   192 KiB (6 instances)
      L2:                    3 MiB (6 instances)
      L3:                    8 MiB (1 instance)
    NUMA:
      NUMA node(s):          1
      NUMA node0 CPU(s):     0-11
    Vulnerabilities:
      Itlb multihit:         Not affected
      L1tf:                  Not affected
      Mds:                   Not affected
      Meltdown:              Not affected
      Mmio stale data:       Not affected
      Retbleed:              Not affected
      Spec store bypass:     Mitigation; Speculative Store Bypass disabled via prctl
      Spectre v1:            Mitigation; usercopy/swapgs barriers and __user pointer sanitization
      Spectre v2:            Mitigation; Retpolines, IBPB conditional, IBRS_FW, STIBP always-on, RSB filling, PBRSB-eIBRS Not affected
      Srbds:                 Not affected
      Tsx async abort:       Not affected

`root `[`#`]`lspci -k -v`

    00:00.0 Host bridge: Advanced Micro Devices, Inc. [AMD] Renoir/Cezanne Root Complex
        Subsystem: Advanced Micro Devices, Inc. [AMD] Renoir/Cezanne Root Complex
        Flags: fast devsel

    00:00.2 IOMMU: Advanced Micro Devices, Inc. [AMD] Renoir/Cezanne IOMMU
        Subsystem: Advanced Micro Devices, Inc. [AMD] Renoir/Cezanne IOMMU
        Flags: bus master, fast devsel, latency 0, IRQ -2147483648
        Capabilities: [40] Secure device <?>
        Capabilities: [64] MSI: Enable- Count=1/4 Maskable- 64bit+
        Capabilities: [74] HyperTransport: MSI Mapping Enable+ Fixed+

    00:01.0 Host bridge: Advanced Micro Devices, Inc. [AMD] Renoir PCIe Dummy Host Bridge
        Flags: fast devsel, IOMMU group 0

    00:01.2 PCI bridge: Advanced Micro Devices, Inc. [AMD] Renoir/Cezanne PCIe GPP Bridge (prog-if 00 [Normal decode])
        Subsystem: Advanced Micro Devices, Inc. [AMD] Renoir/Cezanne PCIe GPP Bridge
        Flags: bus master, fast devsel, latency 0, IRQ 26, IOMMU group 1
        Bus: primary=00, secondary=01, subordinate=01, sec-latency=0
        I/O behind bridge: f000-ffff [size=4K] [16-bit]
        Memory behind bridge: fcf00000-fcffffff [size=1M] [32-bit]
        Prefetchable memory behind bridge: [disabled] [64-bit]
        Capabilities: [50] Power Management version 3
        Capabilities: [58] Express Root Port (Slot+), MSI 00
        Capabilities: [a0] MSI: Enable+ Count=1/1 Maskable- 64bit+
        Capabilities: [c0] Subsystem: Advanced Micro Devices, Inc. [AMD] Renoir/Cezanne PCIe GPP Bridge
        Capabilities: [c8] HyperTransport: MSI Mapping Enable+ Fixed+
        Capabilities: [100] Vendor Specific Information: ID=0001 Rev=1 Len=010 <?>
        Capabilities: [270] Secondary PCI Express
        Capabilities: [2a0] Access Control Services
        Capabilities: [370] L1 PM Substates
        Kernel driver in use: pcieport

    00:01.3 PCI bridge: Advanced Micro Devices, Inc. [AMD] Renoir/Cezanne PCIe GPP Bridge (prog-if 00 [Normal decode])
        Subsystem: Advanced Micro Devices, Inc. [AMD] Renoir/Cezanne PCIe GPP Bridge
        Flags: bus master, fast devsel, latency 0, IRQ 27, IOMMU group 2
        Bus: primary=00, secondary=02, subordinate=02, sec-latency=0
        I/O behind bridge: [disabled] [32-bit]
        Memory behind bridge: [disabled] [32-bit]
        Prefetchable memory behind bridge: e0300000-e04fffff [size=2M] [32-bit]
        Capabilities: [50] Power Management version 3
        Capabilities: [58] Express Root Port (Slot+), MSI 00
        Capabilities: [a0] MSI: Enable+ Count=1/1 Maskable- 64bit+
        Capabilities: [c0] Subsystem: Advanced Micro Devices, Inc. [AMD] Renoir/Cezanne PCIe GPP Bridge
        Capabilities: [c8] HyperTransport: MSI Mapping Enable+ Fixed+
        Capabilities: [100] Vendor Specific Information: ID=0001 Rev=1 Len=010 <?>
        Capabilities: [270] Secondary PCI Express
        Capabilities: [2a0] Access Control Services
        Kernel driver in use: pcieport

    00:02.0 Host bridge: Advanced Micro Devices, Inc. [AMD] Renoir PCIe Dummy Host Bridge
        Flags: fast devsel, IOMMU group 3

    00:02.1 PCI bridge: Advanced Micro Devices, Inc. [AMD] Renoir/Cezanne PCIe GPP Bridge (prog-if 00 [Normal decode])
        Subsystem: Advanced Micro Devices, Inc. [AMD] Renoir/Cezanne PCIe GPP Bridge
        Flags: bus master, fast devsel, latency 0, IRQ 28, IOMMU group 4
        Bus: primary=00, secondary=03, subordinate=03, sec-latency=0
        I/O behind bridge: [disabled] [32-bit]
        Memory behind bridge: fce00000-fcefffff [size=1M] [32-bit]
        Prefetchable memory behind bridge: [disabled] [64-bit]
        Capabilities: [50] Power Management version 3
        Capabilities: [58] Express Root Port (Slot+), MSI 00
        Capabilities: [a0] MSI: Enable+ Count=1/1 Maskable- 64bit+
        Capabilities: [c0] Subsystem: Advanced Micro Devices, Inc. [AMD] Renoir/Cezanne PCIe GPP Bridge
        Capabilities: [c8] HyperTransport: MSI Mapping Enable+ Fixed+
        Capabilities: [100] Vendor Specific Information: ID=0001 Rev=1 Len=010 <?>
        Capabilities: [270] Secondary PCI Express
        Capabilities: [2a0] Access Control Services
        Kernel driver in use: pcieport

    00:08.0 Host bridge: Advanced Micro Devices, Inc. [AMD] Renoir PCIe Dummy Host Bridge
        Flags: fast devsel, IOMMU group 5

    00:08.1 PCI bridge: Advanced Micro Devices, Inc. [AMD] Renoir Internal PCIe GPP Bridge to Bus (prog-if 00 [Normal decode])
        Subsystem: Advanced Micro Devices, Inc. [AMD] Renoir Internal PCIe GPP Bridge to Bus
        Flags: bus master, fast devsel, latency 0, IRQ 29, IOMMU group 6
        Bus: primary=00, secondary=04, subordinate=04, sec-latency=0
        I/O behind bridge: e000-efff [size=4K] [16-bit]
        Memory behind bridge: fca00000-fcdfffff [size=4M] [32-bit]
        Prefetchable memory behind bridge: d0000000-e01fffff [size=258M] [32-bit]
        Capabilities: [50] Power Management version 3
        Capabilities: [58] Express Root Port (Slot-), MSI 00
        Capabilities: [a0] MSI: Enable+ Count=1/1 Maskable- 64bit+
        Capabilities: [c0] Subsystem: Advanced Micro Devices, Inc. [AMD] Renoir Internal PCIe GPP Bridge to Bus
        Capabilities: [100] Vendor Specific Information: ID=0001 Rev=1 Len=010 <?>
        Capabilities: [270] Secondary PCI Express
        Capabilities: [2a0] Access Control Services
        Capabilities: [400] Data Link Feature <?>
        Capabilities: [410] Physical Layer 16.0 GT/s <?>
        Capabilities: [440] Lane Margining at the Receiver <?>
        Kernel driver in use: pcieport

    00:14.0 SMBus: Advanced Micro Devices, Inc. [AMD] FCH SMBus Controller (rev 51)
        Subsystem: Advanced Micro Devices, Inc. [AMD] FCH SMBus Controller
        Flags: 66MHz, medium devsel, IOMMU group 7
        Kernel driver in use: piix4_smbus
        Kernel modules: sp5100_tco

    00:14.3 ISA bridge: Advanced Micro Devices, Inc. [AMD] FCH LPC Bridge (rev 51)
        Subsystem: Advanced Micro Devices, Inc. [AMD] FCH LPC Bridge
        Flags: bus master, 66MHz, medium devsel, latency 0, IOMMU group 7

    00:18.0 Host bridge: Advanced Micro Devices, Inc. [AMD] Cezanne Data Fabric; Function 0
        Flags: fast devsel, IOMMU group 8

    00:18.1 Host bridge: Advanced Micro Devices, Inc. [AMD] Cezanne Data Fabric; Function 1
        Flags: fast devsel, IOMMU group 8

    00:18.2 Host bridge: Advanced Micro Devices, Inc. [AMD] Cezanne Data Fabric; Function 2
        Flags: fast devsel, IOMMU group 8

    00:18.3 Host bridge: Advanced Micro Devices, Inc. [AMD] Cezanne Data Fabric; Function 3
        Flags: fast devsel, IOMMU group 8
        Kernel driver in use: k10temp

    00:18.4 Host bridge: Advanced Micro Devices, Inc. [AMD] Cezanne Data Fabric; Function 4
        Flags: fast devsel, IOMMU group 8

    00:18.5 Host bridge: Advanced Micro Devices, Inc. [AMD] Cezanne Data Fabric; Function 5
        Flags: fast devsel, IOMMU group 8

    00:18.6 Host bridge: Advanced Micro Devices, Inc. [AMD] Cezanne Data Fabric; Function 6
        Flags: fast devsel, IOMMU group 8

    00:18.7 Host bridge: Advanced Micro Devices, Inc. [AMD] Cezanne Data Fabric; Function 7
        Flags: fast devsel, IOMMU group 8

    01:00.0 Ethernet controller: Realtek Semiconductor Co., Ltd. RTL8111/8168/8411 PCI Express Gigabit Ethernet Controller (rev 15)
        Subsystem: Realtek Semiconductor Co., Ltd. RTL8111/8168/8411 PCI Express Gigabit Ethernet Controller
        Flags: bus master, fast devsel, latency 0, IRQ 34, IOMMU group 9
        I/O ports at f000 [size=256]
        Memory at fcf04000 (64-bit, non-prefetchable) [size=4K]
        Memory at fcf00000 (64-bit, non-prefetchable) [size=16K]
        Capabilities: [40] Power Management version 3
        Capabilities: [50] MSI: Enable- Count=1/1 Maskable- 64bit+
        Capabilities: [70] Express Endpoint, MSI 01
        Capabilities: [b0] MSI-X: Enable+ Count=4 Masked-
        Capabilities: [100] Advanced Error Reporting
        Capabilities: [140] Virtual Channel
        Capabilities: [160] Device Serial Number 01-00-00-00-68-4c-e0-00
        Capabilities: [170] Latency Tolerance Reporting
        Capabilities: [178] L1 PM Substates
        Kernel driver in use: r8169

    02:00.0 Network controller: MEDIATEK Corp. MT7921K (RZ608) Wi-Fi 6E 80MHz
        DeviceName: Onboard LAN Brodcom
        Subsystem: MEDIATEK Corp. MT7921K (RZ608) Wi-Fi 6E 80MHz
        Flags: bus master, fast devsel, latency 0, IRQ 44, IOMMU group 10
        Memory at e0300000 (64-bit, prefetchable) [size=1M]
        Memory at e0400000 (64-bit, prefetchable) [size=16K]
        Memory at e0404000 (64-bit, prefetchable) [size=4K]
        Capabilities: [80] Express Endpoint, MSI 00
        Capabilities: [e0] MSI: Enable+ Count=1/32 Maskable+ 64bit+
        Capabilities: [f8] Power Management version 3
        Capabilities: [100] Vendor Specific Information: ID=1556 Rev=1 Len=008 <?>
        Capabilities: [108] Latency Tolerance Reporting
        Capabilities: [110] L1 PM Substates
        Capabilities: [200] Advanced Error Reporting
        Kernel driver in use: mt7921e

    03:00.0 Non-Volatile memory controller: Intel Corporation Device f1aa (rev 03) (prog-if 02 [NVM Express])
        Subsystem: Intel Corporation Device 390f
        Flags: bus master, fast devsel, latency 0, IRQ 32, NUMA node 0, IOMMU group 11
        Memory at fce00000 (64-bit, non-prefetchable) [size=16K]
        Capabilities: [40] Power Management version 3
        Capabilities: [50] MSI: Enable- Count=1/8 Maskable+ 64bit+
        Capabilities: [70] Express Endpoint, MSI 00
        Capabilities: [b0] MSI-X: Enable+ Count=16 Masked-
        Capabilities: [100] Advanced Error Reporting
        Capabilities: [158] Alternative Routing-ID Interpretation (ARI)
        Capabilities: [168] Secondary PCI Express
        Capabilities: [188] Single Root I/O Virtualization (SR-IOV)
        Capabilities: [1c8] Latency Tolerance Reporting
        Capabilities: [1d0] L1 PM Substates
        Kernel driver in use: nvme

    04:00.0 VGA compatible controller: Advanced Micro Devices, Inc. [AMD/ATI] Cezanne [Radeon Vega Series / Radeon Vega Mobile Series] (rev c3) (prog-if 00 [VGA controller])
        Subsystem: Advanced Micro Devices, Inc. [AMD/ATI] Cezanne [Radeon Vega Series / Radeon Vega Mobile Series]
        Flags: bus master, fast devsel, latency 0, IRQ 30, IOMMU group 12
        Memory at d0000000 (64-bit, prefetchable) [size=256M]
        Memory at e0000000 (64-bit, prefetchable) [size=2M]
        I/O ports at e000 [size=256]
        Memory at fcd00000 (32-bit, non-prefetchable) [size=512K]
        Capabilities: [48] Vendor Specific Information: Len=08 <?>
        Capabilities: [50] Power Management version 3
        Capabilities: [64] Express Legacy Endpoint, MSI 00
        Capabilities: [a0] MSI: Enable- Count=1/4 Maskable- 64bit+
        Capabilities: [c0] MSI-X: Enable+ Count=4 Masked-
        Capabilities: [100] Vendor Specific Information: ID=0001 Rev=1 Len=010 <?>
        Capabilities: [270] Secondary PCI Express
        Capabilities: [2a0] Access Control Services
        Capabilities: [2b0] Address Translation Service (ATS)
        Capabilities: [2c0] Page Request Interface (PRI)
        Capabilities: [2d0] Process Address Space ID (PASID)
        Capabilities: [400] Data Link Feature <?>
        Capabilities: [410] Physical Layer 16.0 GT/s <?>
        Capabilities: [440] Lane Margining at the Receiver <?>
        Kernel driver in use: amdgpu

    04:00.1 Audio device: Advanced Micro Devices, Inc. [AMD/ATI] Renoir Radeon High Definition Audio Controller
        Subsystem: Advanced Micro Devices, Inc. [AMD/ATI] Renoir Radeon High Definition Audio Controller
        Flags: bus master, fast devsel, latency 0, IRQ 65, IOMMU group 13
        Memory at fcdc8000 (32-bit, non-prefetchable) [size=16K]
        Capabilities: [48] Vendor Specific Information: Len=08 <?>
        Capabilities: [50] Power Management version 3
        Capabilities: [64] Express Legacy Endpoint, MSI 00
        Capabilities: [a0] MSI: Enable+ Count=1/1 Maskable- 64bit+
        Capabilities: [100] Vendor Specific Information: ID=0001 Rev=1 Len=010 <?>
        Capabilities: [2a0] Access Control Services
        Kernel driver in use: snd_hda_intel

    04:00.2 Encryption controller: Advanced Micro Devices, Inc. [AMD] Family 17h (Models 10h-1fh) Platform Security Processor
        Subsystem: Advanced Micro Devices, Inc. [AMD] Family 17h (Models 10h-1fh) Platform Security Processor
        Flags: bus master, fast devsel, latency 0, IRQ 32, IOMMU group 14
        Memory at fcc00000 (32-bit, non-prefetchable) [size=1M]
        Memory at fcdcc000 (32-bit, non-prefetchable) [size=8K]
        Capabilities: [48] Vendor Specific Information: Len=08 <?>
        Capabilities: [50] Power Management version 3
        Capabilities: [64] Express Endpoint, MSI 00
        Capabilities: [a0] MSI: Enable- Count=1/2 Maskable- 64bit+
        Capabilities: [c0] MSI-X: Enable+ Count=2 Masked-
        Capabilities: [100] Vendor Specific Information: ID=0001 Rev=1 Len=010 <?>
        Capabilities: [2a0] Access Control Services
        Kernel driver in use: ccp

    04:00.3 USB controller: Advanced Micro Devices, Inc. [AMD] Renoir/Cezanne USB 3.1 (prog-if 30 [XHCI])
        Subsystem: Advanced Micro Devices, Inc. [AMD] Renoir/Cezanne USB 3.1
        Flags: bus master, fast devsel, latency 0, IRQ 45, IOMMU group 15
        Memory at fcb00000 (64-bit, non-prefetchable) [size=1M]
        Capabilities: [48] Vendor Specific Information: Len=08 <?>
        Capabilities: [50] Power Management version 3
        Capabilities: [64] Express Endpoint, MSI 00
        Capabilities: [a0] MSI: Enable- Count=1/8 Maskable- 64bit+
        Capabilities: [c0] MSI-X: Enable+ Count=8 Masked-
        Capabilities: [100] Vendor Specific Information: ID=0001 Rev=1 Len=010 <?>
        Capabilities: [2a0] Access Control Services
        Kernel driver in use: xhci_hcd

    04:00.4 USB controller: Advanced Micro Devices, Inc. [AMD] Renoir/Cezanne USB 3.1 (prog-if 30 [XHCI])
        Subsystem: Advanced Micro Devices, Inc. [AMD] Renoir/Cezanne USB 3.1
        Flags: bus master, fast devsel, latency 0, IRQ 30, IOMMU group 16
        Memory at fca00000 (64-bit, non-prefetchable) [size=1M]
        Capabilities: [48] Vendor Specific Information: Len=08 <?>
        Capabilities: [50] Power Management version 3
        Capabilities: [64] Express Endpoint, MSI 00
        Capabilities: [a0] MSI: Enable- Count=1/8 Maskable- 64bit+
        Capabilities: [c0] MSI-X: Enable+ Count=8 Masked-
        Capabilities: [100] Vendor Specific Information: ID=0001 Rev=1 Len=010 <?>
        Capabilities: [2a0] Access Control Services
        Kernel driver in use: xhci_hcd

    04:00.5 Multimedia controller: Advanced Micro Devices, Inc. [AMD] ACP/ACP3X/ACP6x Audio Coprocessor (rev 01)
        Subsystem: Advanced Micro Devices, Inc. [AMD] ACP/ACP3X/ACP6x Audio Coprocessor
        Flags: bus master, fast devsel, latency 0, IRQ 67, IOMMU group 17
        Memory at fcd80000 (32-bit, non-prefetchable) [size=256K]
        Capabilities: [48] Vendor Specific Information: Len=08 <?>
        Capabilities: [50] Power Management version 3
        Capabilities: [64] Express Endpoint, MSI 00
        Capabilities: [a0] MSI: Enable+ Count=1/1 Maskable- 64bit+
        Capabilities: [100] Vendor Specific Information: ID=0001 Rev=1 Len=010 <?>
        Capabilities: [2a0] Access Control Services
        Kernel driver in use: snd_rn_pci_acp3x

    04:00.6 Audio device: Advanced Micro Devices, Inc. [AMD] Family 17h/19h HD Audio Controller
        DeviceName: HD Audio Controller
        Subsystem: Advanced Micro Devices, Inc. [AMD] Family 17h/19h HD Audio Controller
        Flags: bus master, fast devsel, latency 0, IRQ 66, IOMMU group 18
        Memory at fcdc0000 (32-bit, non-prefetchable) [size=32K]
        Capabilities: [48] Vendor Specific Information: Len=08 <?>
        Capabilities: [50] Power Management version 3
        Capabilities: [64] Express Endpoint, MSI 00
        Capabilities: [a0] MSI: Enable+ Count=1/1 Maskable- 64bit+
        Capabilities: [100] Vendor Specific Information: ID=0001 Rev=1 Len=010 <?>
        Capabilities: [2a0] Access Control Services
        Kernel driver in use: snd_hda_intel

## [Installation]

### [make.conf]

[FILE] **`/etc/portage/make.conf`**

    VIDEO_CARDS="amdgpu radeonsi"
    GRUB_PLATFORMS="efi-64"

[FILE] **`/etc/portage/package.use/00cpu-flags`**

    */* CPU_FLAGS_X86: aes avx avx2 f16c fma3 mmx mmxext pclmul popcnt rdrand sha sse sse2 sse3 sse4_1 sse4_2 sse4a ssse3

### [Firmware]

For wifi, bluetooth, integrated graphics, and microcode updates add the following firmware files:

[FILE] **`/usr/src/linux/.config`**

    CONFIG_EXTRA_FIRMWARE="mediatek/BT_RAM_CODE_MT7961_1_2_hdr.bin mediatek/WIFI_MT7961_patch_mcu_1_2_hdr.bin mediatek/WIFI_RAM_CODE_MT7961_1.bin amd/amd_sev_fam17h_model0xh.sbin amd/amd_sev_fam17h_model3xh.sbin amd/amd_sev_fam19h_model0xh.sbin amd-ucode/microcode_amd_fam17h.bin amd-ucode/microcode_amd_fam19h.bin amdgpu/green_sardine_asd.bin amdgpu/green_sardine_ce.bin amdgpu/green_sardine_dmcub.bin amdgpu/green_sardine_me.bin amdgpu/green_sardine_mec2.bin amdgpu/green_sardine_mec.bin amdgpu/green_sardine_pfp.bin amdgpu/green_sardine_rlc.bin amdgpu/green_sardine_sdma.bin amdgpu/green_sardine_ta.bin amdgpu/green_sardine_vcn.bin"
    CONFIG_EXTRA_FIRMWARE_DIR="/lib/firmware"

### [Kernel]

[KERNEL] **menuconfig**

    [*] 64-bit kernel
        Processor type and features  --->
            [*] AMD ACPI2Platform devices support
            Processor family (AMD-Native optimizations autodetected by the compiler)
    [*] Virtualization
            <*> KVM for AMD processors support
        Device Drivers  --->
            [*] PCI support  --->
                [*] PCI Express Port Bus support
                NVME Support  --->
                    <*> NVM Express block device
            [*] Network device support  --->
                [*] Wireless LAN  --->
                    [*] MediaTek devices
                    <*>     MediaTek MT7921E (PCIe) support
                    <*>     MediaTek MT7921S (SDIO) support
                    <*>     MediaTek MT7921U (USB) support
                [*] Realtek devices
                <*>     Realtek 8180/8185/8187SE PCI support
            Graphics support  --->
                < > ATI Radeon
                <*> AMD GPU
                    ACP (Audio CoProcessor) Configuration  --->
                        [*] Enable AMD Audio CoProcessor IP support
                    Display Engine Configuration  --->
                        [*] AMD DC - Enable new display engine
                        [*] Enable HDCP support in DC
                [*] HSA kernel driver for AMD GPU devices
            [*] USB support  --->
                <*> xHCI HCD (USB 3.0) support
                <*> EHCI HCD (USB 2.0) support
                <*> USB Mass Storage support
                <*> USB Type-C Support  --->
                    <*> USB Type-C Port Controller Manager
                    <*> Type-C Port Controller Interface driver
                    <*> USB Type-C Connector System Software Interface driver
            [*] IOMMU Hardware Support  --->
                [*]   AMD IOMMU support
                <*>     AMD IOMMU Version 2 driver

### [Emerge]

`root `[`#`]`emerge --ask sys-kernel/linux-firmware media-libs/mesa x11-apps/mesa-progs vulkan-tools`

### [GPU software support notes]

`root `[`#`]`vulkaninfo --summary`

    ==========
    VULKANINFO
    ==========

    Vulkan Instance Version: 1.3.246

    Instance Extensions: count = 23
    -------------------------------
    VK_EXT_acquire_drm_display             : extension revision 1
    VK_EXT_acquire_xlib_display            : extension revision 1
    VK_EXT_debug_report                    : extension revision 10
    VK_EXT_debug_utils                     : extension revision 2
    VK_EXT_direct_mode_display             : extension revision 1
    VK_EXT_display_surface_counter         : extension revision 1
    VK_EXT_surface_maintenance1            : extension revision 1
    VK_EXT_swapchain_colorspace            : extension revision 4
    VK_KHR_device_group_creation           : extension revision 1
    VK_KHR_display                         : extension revision 23
    VK_KHR_external_fence_capabilities     : extension revision 1
    VK_KHR_external_memory_capabilities    : extension revision 1
    VK_KHR_external_semaphore_capabilities : extension revision 1
    VK_KHR_get_display_properties2         : extension revision 1
    VK_KHR_get_physical_device_properties2 : extension revision 2
    VK_KHR_get_surface_capabilities2       : extension revision 1
    VK_KHR_portability_enumeration         : extension revision 1
    VK_KHR_surface                         : extension revision 25
    VK_KHR_surface_protected_capabilities  : extension revision 1
    VK_KHR_wayland_surface                 : extension revision 6
    VK_KHR_xcb_surface                     : extension revision 6
    VK_KHR_xlib_surface                    : extension revision 6
    VK_LUNARG_direct_driver_loading        : extension revision 1

    Instance Layers: count = 3
    --------------------------
    VK_LAYER_KHRONOS_validation Khronos Validation Layer     1.3.246  version 1
    VK_LAYER_MESA_device_select Linux device selection layer 1.3.211  version 1
    VK_LAYER_MESA_overlay       Mesa Overlay layer           1.3.211  version 1

    Devices:
    ========
    GPU0:
        apiVersion         = 1.3.212
        driverVersion      = 2.0.225
        vendorID           = 0x1002
        deviceID           = 0x1638
        deviceType         = PHYSICAL_DEVICE_TYPE_INTEGRATED_GPU
        deviceName         = AMD Radeon Graphics
        driverID           = DRIVER_ID_AMD_PROPRIETARY
        driverName         = AMD proprietary driver
        driverInfo         =
        conformanceVersion = 1.3.0.0
        deviceUUID         = 00000000-0400-0000-0000-000000000000
        driverUUID         = 414d442d-4c49-4e55-582d-445256000000
    GPU1:
        apiVersion         = 1.3.246
        driverVersion      = 23.1.1
        vendorID           = 0x1002
        deviceID           = 0x1638
        deviceType         = PHYSICAL_DEVICE_TYPE_INTEGRATED_GPU
        deviceName         = AMD Radeon Graphics (RADV RENOIR)
        driverID           = DRIVER_ID_MESA_RADV
        driverName         = radv
        driverInfo         = Mesa 23.1.1
        conformanceVersion = 1.2.7.1
        deviceUUID         = 00000000-0400-0000-0000-000000000000
        driverUUID         = 414d442d-4d45-5341-2d44-525600000000

`root `[`#`]`glxinfo -B`

    name of display: :0
    display: :0  screen: 0
    direct rendering: Yes
    Extended renderer info (GLX_MESA_query_renderer):
        Vendor: AMD (0x1002)
        Device: AMD Radeon Graphics (renoir, LLVM 16.0.5, DRM 3.49, 6.1.31-gentoo-x86_64) (0x1638)
        Version: 23.1.1
        Accelerated: yes
        Video memory: 3072MB
        Unified memory: no
        Preferred profile: core (0x1)
        Max core profile version: 4.6
        Max compat profile version: 4.6
        Max GLES1 profile version: 1.1
        Max GLES[23] profile version: 3.2
    Memory info (GL_ATI_meminfo):
        VBO free memory - total: 2382 MB, largest block: 2382 MB
        VBO free aux. memory - total: 6238 MB, largest block: 6238 MB
        Texture free memory - total: 2382 MB, largest block: 2382 MB
        Texture free aux. memory - total: 6238 MB, largest block: 6238 MB
        Renderbuffer free memory - total: 2382 MB, largest block: 2382 MB
        Renderbuffer free aux. memory - total: 6238 MB, largest block: 6238 MB
    Memory info (GL_NVX_gpu_memory_info):
        Dedicated video memory: 3072 MB
        Total available memory: 9499 MB
        Currently available dedicated video memory: 2382 MB
    OpenGL vendor string: AMD
    OpenGL renderer string: AMD Radeon Graphics (renoir, LLVM 16.0.5, DRM 3.49, 6.1.31-gentoo-x86_64)
    OpenGL core profile version string: 4.6 (Core Profile) Mesa 23.1.1
    OpenGL core profile shading language version string: 4.60
    OpenGL core profile context flags: (none)
    OpenGL core profile profile mask: core profile

    OpenGL version string: 4.6 (Compatibility Profile) Mesa 23.1.1
    OpenGL shading language version string: 4.60
    OpenGL context flags: (none)
    OpenGL profile mask: compatibility profile

    OpenGL ES profile version string: OpenGL ES 3.2 Mesa 23.1.1
    OpenGL ES profile shading language version string: OpenGL ES GLSL ES 3.20

`root `[`#`]`VDPAU_DRIVER=radeonsi vdpauinfo`

    display: :0   screen: 0
    API version: 1
    Information string: G3DVL VDPAU Driver Shared Library version 1.0

    Video surface:

    name   width height types
    -------------------------------------------
    420    16384 16384  NV12 YV12
    422    16384 16384  UYVY YUYV
    444    16384 16384  Y8U8V8A8 V8U8Y8A8
    420_16 16384 16384
    422_16 16384 16384
    444_16 16384 16384

    Decoder capabilities:

    name                        level macbs width height
    ----------------------------------------------------
    MPEG1                           0 65536  4096  4096
    MPEG2_SIMPLE                    3 65536  4096  4096
    MPEG2_MAIN                      3 65536  4096  4096
    H264_BASELINE                  52 65536  4096  4096
    H264_MAIN                      52 65536  4096  4096
    H264_HIGH                      52 65536  4096  4096
    VC1_SIMPLE                      1 65536  4096  4096
    VC1_MAIN                        2 65536  4096  4096
    VC1_ADVANCED                    4 65536  4096  4096
    MPEG4_PART2_SP                  3 65536  4096  4096
    MPEG4_PART2_ASP                 5 65536  4096  4096
    DIVX4_QMOBILE                  --- not supported ---
    DIVX4_MOBILE                   --- not supported ---
    DIVX4_HOME_THEATER             --- not supported ---
    DIVX4_HD_1080P                 --- not supported ---
    DIVX5_QMOBILE                  --- not supported ---
    DIVX5_MOBILE                   --- not supported ---
    DIVX5_HOME_THEATER             --- not supported ---
    DIVX5_HD_1080P                 --- not supported ---
    H264_CONSTRAINED_BASELINE       0 65536  4096  4096
    H264_EXTENDED                  --- not supported ---
    H264_PROGRESSIVE_HIGH          --- not supported ---
    H264_CONSTRAINED_HIGH          --- not supported ---
    H264_HIGH_444_PREDICTIVE       --- not supported ---
    VP9_PROFILE_0                  --- not supported ---
    VP9_PROFILE_1                  --- not supported ---
    VP9_PROFILE_2                  --- not supported ---
    VP9_PROFILE_3                  --- not supported ---
    HEVC_MAIN                      186 139264  8192  4352
    HEVC_MAIN_10                   186 139264  8192  4352
    HEVC_MAIN_STILL                --- not supported ---
    HEVC_MAIN_12                   --- not supported ---
    HEVC_MAIN_444                  --- not supported ---
    HEVC_MAIN_444_10               --- not supported ---
    HEVC_MAIN_444_12               --- not supported ---
    AV1_MAIN                       --- not supported ---
    AV1_HIGH                       --- not supported ---
    AV1_PROFESSIONAL               --- not supported ---

    Output surface:

    name              width height nat types
    ----------------------------------------------------
    B8G8R8A8         16384 16384    y  NV12 YV12 UYVY YUYV Y8U8V8A8 V8U8Y8A8 P010 P016 I8A8
    R8G8B8A8         16384 16384    y  NV12 YV12 UYVY YUYV Y8U8V8A8 V8U8Y8A8 P010 P016 I8A8
    R10G10B10A2      16384 16384    y  NV12 YV12 UYVY YUYV Y8U8V8A8 V8U8Y8A8 P010 P016 I8A8
    B10G10R10A2      16384 16384    y  NV12 YV12 UYVY YUYV Y8U8V8A8 V8U8Y8A8 P010 P016 I8A8

    Bitmap surface:

    name              width height
    ------------------------------
    B8G8R8A8         16384 16384
    R8G8B8A8         16384 16384
    R10G10B10A2      16384 16384
    B10G10R10A2      16384 16384
    A8               16384 16384

    Video mixer:

    feature name                    sup
    ------------------------------------
    DEINTERLACE_TEMPORAL             y
    DEINTERLACE_TEMPORAL_SPATIAL     -
    INVERSE_TELECINE                 -
    NOISE_REDUCTION                  y
    SHARPNESS                        y
    LUMA_KEY                         y
    HIGH QUALITY SCALING - L1        y
    HIGH QUALITY SCALING - L2        -
    HIGH QUALITY SCALING - L3        -
    HIGH QUALITY SCALING - L4        -
    HIGH QUALITY SCALING - L5        -
    HIGH QUALITY SCALING - L6        -
    HIGH QUALITY SCALING - L7        -
    HIGH QUALITY SCALING - L8        -
    HIGH QUALITY SCALING - L9        -

    parameter name                  sup      min      max
    -----------------------------------------------------
    VIDEO_SURFACE_WIDTH              y        48     4096
    VIDEO_SURFACE_HEIGHT             y        48     4096
    CHROMA_TYPE                      y
    LAYERS                           y         0        4

    attribute name                  sup      min      max
    -----------------------------------------------------
    BACKGROUND_COLOR                 y
    CSC_MATRIX                       y
    NOISE_REDUCTION_LEVEL            y      0.00     1.00
    SHARPNESS_LEVEL                  y     -1.00     1.00
    LUMA_KEY_MIN_LUMA                y
    LUMA_KEY_MAX_LUMA                y

## [See also]

-   [AMD](https://wiki.gentoo.org/wiki/AMD "AMD") --- a semiconductor company. AMD is best known for producing CPUs based on [x86 intruction set](https://en.wikipedia.org/wiki/x86 "wikipedia:x86"), motherboard chipsets and their own line of GPUs.
-   [Ryzen](https://wiki.gentoo.org/wiki/Ryzen "Ryzen") --- a multithreaded, high performance processor manufactured by AMD.
-   [AMDGPU](https://wiki.gentoo.org/wiki/AMDGPU "AMDGPU") --- the open source graphics drivers for AMD Radeon and other GPUs.
-   [VDPAU](https://wiki.gentoo.org/wiki/VDPAU "VDPAU") --- how to setup the **V**ideo **D**ecode and **P**resentation **A**PI for **U**nix (VDPAU).
-   [radeon](https://wiki.gentoo.org/wiki/Radeon "Radeon") --- a family of *open source* graphics drivers for *older* AMD/ATI Radeon graphics cards.
-   [GPU passthrough with virt-manager, QEMU, and KVM](https://wiki.gentoo.org/wiki/GPU_passthrough_with_virt-manager,_QEMU,_and_KVM "GPU passthrough with virt-manager, QEMU, and KVM") --- directly present an internal PCI GPU as-is for direct use by a virtual machine

## [References]

1.  [[[↑](#cite_ref-discontinued_1-0)] [[https://web.archive.org/web/20230609163728/https://forum.bee-link.com/forum.php?mod=viewthread&tid=86020&highlight=5560U](https://web.archive.org/web/20230609163728/https://forum.bee-link.com/forum.php?mod=viewthread&tid=86020&highlight=5560U)]]
2.  [[[↑](#cite_ref-issues_2-0)] [[https://web.archive.org/web/20230609163627/https://forum.bee-link.com/forum.php?mod=viewthread&tid=85959&highlight=5560U](https://web.archive.org/web/20230609163627/https://forum.bee-link.com/forum.php?mod=viewthread&tid=85959&highlight=5560U)]]
3.  [[[↑](#cite_ref-threads_3-0)] [[https://web.archive.org/web/20230609163548/https://forum.bee-link.com/search.php?mod=forum&searchid=57&orderby=lastpost&ascdesc=desc&searchsubmit=yes&kw=5560U](https://web.archive.org/web/20230609163548/https://forum.bee-link.com/search.php?mod=forum&searchid=57&orderby=lastpost&ascdesc=desc&searchsubmit=yes&kw=5560U)]]
4.  [[[↑](#cite_ref-redditissue_4-0)] [[https://web.archive.org/web/20230116210928/https://www.reddit.com/r/MiniPCs/comments/10aifxt/beelink_ser5_5560u_setup_issue/](https://web.archive.org/web/20230116210928/https://www.reddit.com/r/MiniPCs/comments/10aifxt/beelink_ser5_5560u_setup_issue/)]]
5.  [[[↑](#cite_ref-bios_5-0)] [[https://web.archive.org/web/20230609163637/https://forum.bee-link.com/forum.php?mod=viewthread&tid=86668&highlight=5560U](https://web.archive.org/web/20230609163637/https://forum.bee-link.com/forum.php?mod=viewthread&tid=86668&highlight=5560U)]]
6.  [[[↑](#cite_ref-drivers_6-0)] [[https://web.archive.org/web/20230609163641/https://forum.bee-link.com/forum.php?mod=viewthread&tid=86785&highlight=5560U](https://web.archive.org/web/20230609163641/https://forum.bee-link.com/forum.php?mod=viewthread&tid=86785&highlight=5560U)]]
7.  [[[↑](#cite_ref-xpc_7-0)] [[https://minixpc.com/products/beelink-ser-5-mini-pc-amd-ryzen%E2%84%A2-55560u-windows-11-wifi-6e-16g-500g-ssd?variant=43882372628714](https://minixpc.com/products/beelink-ser-5-mini-pc-amd-ryzen%E2%84%A2-55560u-windows-11-wifi-6e-16g-500g-ssd?variant=43882372628714)]]
8.  [[[↑](#cite_ref-xpcarchive_8-0)] [[https://web.archive.org/web/20230609224652/https://minixpc.com/products/beelink-ser-5-mini-pc-amd-ryzen%E2%84%A2-55560u-windows-11-wifi-6e-16g-500g-ssd?variant=43882372628714](https://web.archive.org/web/20230609224652/https://minixpc.com/products/beelink-ser-5-mini-pc-amd-ryzen%E2%84%A2-55560u-windows-11-wifi-6e-16g-500g-ssd?variant=43882372628714)]]
9.  [[↑ ^[9.0](#cite_ref-amd_9-0)^ ^[9.1](#cite_ref-amd_9-1)^] [[https://www.amd.com/en/product/11876](https://www.amd.com/en/product/11876)]]