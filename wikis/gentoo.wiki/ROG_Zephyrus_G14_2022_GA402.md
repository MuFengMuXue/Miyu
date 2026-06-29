**Resources**

[[]][Asus Hardware Specifications](https://rog.asus.com/laptops/rog-zephyrus/rog-zephyrus-g14-2022-series/spec/)

[[]][Asus FAQ/Support](https://rog.asus.com/laptops/rog-zephyrus/rog-zephyrus-g14-2022-series/helpdesk/)

[[]][Asus User Manual (English)](https://dlcdnets.asus.com/pub/ASUS/GamingNB/GA402RK/0409_E18586_GA402R_A.pdf?model%3DROG%20Zephyrus%20G14%202022%20GA402)

[[]][Asus Zephyrus G14 Photo Gallery](https://rog.asus.com/laptops/rog-zephyrus/rog-zephyrus-g14-2022-series/gallery/)

[[]][Republic of Gamers (ROG)](https://en.wikipedia.org/wiki/Asus#Republic_of_Gamers_.28ROG.29 "wikipedia:Asus")

[[]][r/ZephyrusG14](https://reddit.com/r/ZephyrusG14)

The [Asus](https://wiki.gentoo.org/wiki/Category:ASUS "Category:ASUS") Republic of Gamers (ROG) Zephyrus G14 (2022) GA402 is an [AMD](https://wiki.gentoo.org/wiki/AMD "AMD") Advantage gaming laptop.^[\[1\]](#cite_note-1)^ It features Asus\' AniMe Matrix and vapor chamber cooling plus AMD\'s Smartshift^[\[2\]](#cite_note-2)^ and Smart Access Memory^[\[3\]](#cite_note-3)^ technologies. Depending on the model (GA402RJ or GA402RK), it has either the 6700S^[\[4\]](#cite_note-4)^ or 6800S^[\[5\]](#cite_note-5)^ Navi 23^[\[6\]](#cite_note-gpuwiki-6)^ dGPU. It has a 1440p 16:10 120 Hz display and has been shown to operate with 40 GB of DDR5 memory.

## Contents

-   [[1] [Hardware]](#Hardware)
    -   [[1.1] [Standard]](#Standard)
        -   [[1.1.1] [Table]](#Table)
        -   [[1.1.2] [lscpu]](#lscpu)
            -   [[1.1.2.1] [AMD virtualisation flags]](#AMD_virtualisation_flags)
        -   [[1.1.3] [lspci]](#lspci)
        -   [[1.1.4] [lsusb]](#lsusb)
        -   [[1.1.5] [Ports]](#Ports)
    -   [[1.2] [Accessories]](#Accessories)
-   [[2] [Installation]](#Installation)
    -   [[2.1] [00cpu-flags]](#00cpu-flags)
    -   [[2.2] [make.conf]](#make.conf)
    -   [[2.3] [package.license]](#package.license)
    -   [[2.4] [package.use]](#package.use)
    -   [[2.5] [Kernel]](#Kernel)
    -   [[2.6] [Firmware]](#Firmware)
    -   [[2.7] [Emerge]](#Emerge)
        -   [[2.7.1] [Firmware]](#Firmware_2)
        -   [[2.7.2] [Graphics/Mesa/Vulkan]](#Graphics.2FMesa.2FVulkan)
        -   [[2.7.3] [Power]](#Power)
    -   [[2.8] [initramfs]](#initramfs)
-   [[3] [Configuration]](#Configuration)
    -   [[3.1] [AMD P-State]](#AMD_P-State)
        -   [[3.1.1] [Kernels 6.1.\* and earlier]](#Kernels_6.1..2A_and_earlier)
        -   [[3.1.2] [Kernels 6.5.5 and later]](#Kernels_6.5.5_and_later)
    -   [[3.2] [asusctl]](#asusctl)
        -   [[3.2.1] [OpenRC]](#OpenRC)
    -   [[3.3] [BIOS]](#BIOS)
    -   [[3.4] [Firmware updates]](#Firmware_updates)
    -   [[3.5] [Hyprland]](#Hyprland)
        -   [[3.5.1] [Function keys and hot keys]](#Function_keys_and_hot_keys)
        -   [[3.5.2] [Keyboard brightness]](#Keyboard_brightness)
        -   [[3.5.3] [Screenshots]](#Screenshots)
    -   [[3.6] [KDE Wayland]](#KDE_Wayland)
    -   [[3.7] [TLP]](#TLP)
-   [[4] [Troubleshooting]](#Troubleshooting)
    -   [[4.1] [680M freezes]](#680M_freezes)
    -   [[4.2] [ccp_crypto: cannot load]](#ccp_crypto:_cannot_load)
    -   [[4.3] [fTPM RNG stutters]](#fTPM_RNG_stutters)
    -   [[4.4] [Machine learning]](#Machine_learning)
    -   [[4.5] [Mesa 23.1 crashes]](#Mesa_23.1_crashes)
    -   [[4.6] [rocminfo]](#rocminfo)
    -   [[4.7] [Suspend]](#Suspend)
-   [[5] [Notes]](#Notes)
    -   [[5.1] [Benchmarks]](#Benchmarks)
        -   [[5.1.1] [6900HS]](#6900HS)
            -   [[5.1.1.1] [Compiling]](#Compiling)
            -   [[5.1.1.2] [Cryptography]](#Cryptography)
    -   [[5.2] [dmidecode]](#dmidecode)
    -   [[5.3] [GPU features]](#GPU_features)
        -   [[5.3.1] [OpenCL]](#OpenCL)
        -   [[5.3.2] [OpenGL]](#OpenGL)
            -   [[5.3.2.1] [680M]](#680M)
            -   [[5.3.2.2] [6700S]](#6700S)
        -   [[5.3.3] [ROCm]](#ROCm)
        -   [[5.3.4] [VAAPI]](#VAAPI)
        -   [[5.3.5] [VDPAU]](#VDPAU)
            -   [[5.3.5.1] [680M]](#680M_2)
            -   [[5.3.5.2] [6700S]](#6700S_2)
        -   [[5.3.6] [Vulkan]](#Vulkan)
    -   [[5.4] [GPU monitoring]](#GPU_monitoring)
-   [[6] [See also]](#See_also)
-   [[7] [External resources]](#External_resources)
-   [[8] [References]](#References)

## [Hardware]

** Note**\
On vendor IDs --- 1002 is ATI, 1022 is AMD.^[\[7\]](#cite_note-7)[\[8\]](#cite_note-8)^

\

### [Standard]

#### [Table]

  -------------------------------- --------------------------------------------------------------------------------------------------------------------------------- -------------------------------------------------------- --------- --------------------------------- ---------------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Device                           Make/model                                                                                                                        Vendor ID / Product ID                                   Status    Kernel driver(s)                  Kernel version   Notes
  APU                              AMD Ryzen 9 6900HS with Radeon Graphics^[\[9\]](#cite_note-amdcpu-9)[\[10\]](#cite_note-10)[\[11\]](#cite_note-11)^               Model: 25.68.1. Part No: 100-000000544, 100-000000560.   Works     amdgpu                            6.14.2           Zen 3+ CPU, codename Rembrandt-H, AMD Radeon 680M iGPU. The 680M requires Yellow Carp^[\[12\]](#cite_note-12)[\[13\]](#cite_note-13)[\[14\]](#cite_note-14)^ firmware, see below. The 6.12.1+ kernel is affected by a known bug which causes screen flickering,^[\[15\]](#cite_note-15)[\[16\]](#cite_note-16)[\[17\]](#cite_note-17)^ especially when scrolling, but it can be tolerated. This issue is fixed since 6.12.11.
  dGPU                             AMD Navi 23 \[Radeon RX 6650 XT / 6700S / 6800S\] (rev c2)                                                                        1002:73ef^[\[18\]](#cite_note-18)^                       Works     amdgpu^[\[19\]](#cite_note-19)^   6.14.2           RDNA 2.0, requires Dimgrey Cavefish^[\[20\]](#cite_note-20)^ firmware (see below) and Mesa 20.3 or later.^[\[21\]](#cite_note-21)^
  Host bridge                      Advanced Micro Devices, Inc. \[AMD\] Family 17h-19h PCIe Root Complex (rev 01)                                                    1022:14b5                                                Works     N/A                               6.14.2
  IOMMU                            Advanced Micro Devices, Inc. \[AMD\] Family 17h-19h IOMMU                                                                         1022:14b6                                                Works     N/A                               6.14.2
  Host bridge                      Advanced Micro Devices, Inc. \[AMD\] Family 17h-19h PCIe Dummy Host Bridge (rev 01)                                               1022:14b7                                                Works     N/A                               6.14.2
  PCI bridge                       Advanced Micro Devices, Inc. \[AMD\] Device 14b8 (prog-if 00 \[Normal decode\])                                                   1022:14b8                                                Works     pcieport                          6.14.2           Subsystem: ASUSTeK Computer Inc. Device 1d42
  Host bridge                      Advanced Micro Devices, Inc. \[AMD\] Family 17h-19h PCIe Dummy Host Bridge (rev 01)                                               1022:14b7                                                Works     N/A                               6.14.2
  PCI bridge                       Advanced Micro Devices, Inc. \[AMD\] Family 17h-19h PCIe GPP Bridge (prog-if 00 \[Normal decode\])                                1022:14ba                                                Works     pcieport                          6.14.2           IOMMU groups 3-5
  Host bridge                      Advanced Micro Devices, Inc. \[AMD\] Family 17h-19h PCIe Dummy Host Bridge (rev 01)                                               1022:14b7                                                Works     N/A                               6.14.2           IOMMU group 6-8
  PCI bridge                       Advanced Micro Devices, Inc. \[AMD\] Family 17h-19h Internal PCIe GPP Bridge (rev 10) (prog-if 00 \[Normal decode\])              1022:14b9                                                Works     pcieport                          6.14.2           IOMMU groups 9-10
  SMBus                            Advanced Micro Devices, Inc. \[AMD\] FCH SMBus Controller (rev 71)                                                                1022:790b                                                Works     piix4_smbus                       6.14.2           66 MHz
  ISA Bridge                       Advanced Micro Devices, Inc. \[AMD\] FCH LPC Bridge (rev 51)                                                                      1022:790e                                                Works     N/A                               6.14.2           66 MHz
  Host bridge                      Advanced Micro Devices, Inc. \[AMD\] Rembrandt Data Fabric: Device 18h; Functions 0-7                                             1022:1679 - 1022:1680                                    Works     k10temp                           6.14.2           IOMMU group 12. Kernel driver used by Function 3.
  PCI bridge                       Advanced Micro Devices, Inc. \[AMD/ATI\] Navi 10 XL Upstream Port of PCI Express Switch (rev c2) (prog-if 00 \[Normal decode\])   1002:1478^[\[22\]](#cite_note-22)^                       Works     pcieport                          6.14.2
  PCI bridge                       Advanced Micro Devices, Inc. \[AMD/ATI\] Navi 10 XL Downstream Port of PCI Express Switch (prog-if 00 \[Normal decode\])          1002:1479^[\[23\]](#cite_note-23)^                       Works     pcieport                          6.14.2
  Audio device                     Advanced Micro Devices, Inc. \[AMD/ATI\] Navi 21/23 HDMI/DP Audio Controller                                                      1002:ab28                                                Works     snd_hda_intel                     6.14.2
  SD Host controller               O2 Micro, Inc. SD/MMC Card Reader Controller (rev 01) (prog-if 01)                                                                1217:8520                                                Works     sdhci-pci                         6.14.2
  Network controller               MEDIATEK Corp. MT7922 802.11ax PCI Express Wireless Network Adapter                                                               14c3:7922                                                Works     mt7921e                           6.14.2           In the past, it occasionally failed to work and a reboot or power off/on was required. This doesn\'t seem to occur any more since perhaps around the time of the 6.8 kernels.
  Non-Volatile memory controller   Samsung Electronics Co Ltd NVMe SSD Controller PM9A1/PM9A3/980PRO (prog-if 02 \[NVM Express\])                                    144d:a80a                                                Works     nvme                              6.14.2           2 TB drives work fine.
  VGA compatible controller        Advanced Micro Devices, Inc. \[AMD/ATI\] Rembrandt \[Radeon 680M\] (rev c7) (prog-if 00 \[VGA controller\])                       1002:1681                                                Works     amdgpu                            6.14.2           See APU section above.
  Audio device                     Advanced Micro Devices, Inc. \[AMD/ATI\] Rembrandt Radeon High Definition Audio Controller                                        1002:1640                                                Works     snd_hda_intel                     6.14.2
  Encryption controller            Advanced Micro Devices, Inc. Advanced Micro Devices, Inc. \[AMD\] VanGogh PSP/CCP                                                 1022:1649                                                Tested    ccp                               6.14.2           AMD\'s fTPM RNG has the infamous sporadic stutter issue.^[\[24\]](#cite_note-24)[\[25\]](#cite_note-25)[\[26\]](#cite_note-26)^
  USB controller                   Advanced Micro Devices, Inc. \[AMD\] Rembrandt USB4 XHCI controller #3, #4, #5, #6, #8 (prog-if 30 \[XHCI\])                      1022:161d - 1022:161f, 1022:15d6 - 1022:15d7             Tested    xhci_hcd                          6.14.2           USB 4 does not work despite the hardware support because Asus has not updated the BIOS for it yet. A beta BIOS is available for those interested.^[\[27\]](#cite_note-27)^ USB 3 is fine.
  Multimedia controller            Advanced Micro Devices, Inc. \[AMD\] ACP/ACP3X/ACP6x Audio Coprocessor (rev 60)                                                   1022:15e2                                                Works     snd_pci_acp6x                     6.14.2
  Audio device                     Advanced Micro Devices, Inc. \[AMD\] Family 17h/19h HD Audio Controller                                                           1022:15e3                                                Works     snd_hda_intel                     6.14.2
  Webcam                           IMC Networks                                                                                                                      13d3:56eb^[\[28\]](#cite_note-28)^                       Works     xhci_hcd/3p, uvcvideo             6.14.2           720p
  Touchpad                         ASUE120A:00^[\[29\]](#cite_note-29)^                                                                                              04F3:319B                                                Works     i2c_hid, usbhid                   6.14.2           Add `libinput` and `synaptics` to [INPUT_DEVICES](https://wiki.gentoo.org/wiki//etc/portage/make.conf#INPUT_DEVICES "/etc/portage/make.conf"), see package.use below.
  -------------------------------- --------------------------------------------------------------------------------------------------------------------------------- -------------------------------------------------------- --------- --------------------------------- ---------------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#### [lscpu]

`root `[`#`]`lscpu`

    Architecture:                    x86_64
    CPU op-mode(s):                  32-bit, 64-bit
    Address sizes:                   48 bits physical, 48 bits virtual
    Byte Order:                      Little Endian
    CPU(s):                          16
    On-line CPU(s) list:             0-15
    Vendor ID:                       AuthenticAMD
    BIOS Vendor ID:                  Advanced Micro Devices, Inc.
    Model name:                      AMD Ryzen 9 6900HS with Radeon Graphics
    BIOS Model name:                 AMD Ryzen 9 6900HS with Radeon Graphics         Unknown CPU @ 3.3GHz
    BIOS CPU family:                 107
    CPU family:                      25
    Model:                           68
    Thread(s) per core:              2
    Core(s) per socket:              8
    Socket(s):                       1
    Stepping:                        1
    Frequency boost:                 enabled
    CPU(s) scaling MHz:              48%
    CPU max MHz:                     4935.0000
    CPU min MHz:                     400.0000
    BogoMIPS:                        6590.41
    Flags:                           fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush mmx fxsr sse sse2 ht syscall nx mmxext fxsr_opt pdpe1gb rdtscp lm constant_tsc rep_good nopl nonstop_tsc cpuid extd_apicid aperfmperf rapl pni pclmulqdq monitor ssse3 fma cx16 sse4_1 sse4_2 x2apic movbe popcnt aes xsave avx f16c rdrand lahf_lm cmp_legacy svm extapic cr8_legacy abm sse4a misalignsse 3dnowprefetch osvw ibs skinit wdt tce topoext perfctr_core perfctr_nb bpext perfctr_llc mwaitx cpb cat_l3 cdp_l3 hw_pstate ssbd mba ibrs ibpb stibp vmmcall fsgsbase bmi1 avx2 smep bmi2 erms invpcid cqm rdt_a rdseed adx smap clflushopt clwb sha_ni xsaveopt xsavec xgetbv1 xsaves cqm_llc cqm_occup_llc cqm_mbm_total cqm_mbm_local clzero irperf xsaveerptr rdpru wbnoinvd cppc arat npt lbrv svm_lock nrip_save tsc_scale vmcb_clean flushbyasid decodeassists pausefilter pfthreshold avic v_vmsave_vmload vgif v_spec_ctrl umip pku ospke vaes vpclmulqdq rdpid overflow_recov succor smca fsrm
    Virtualization:                  AMD-V
    L1d cache:                       256 KiB (8 instances)
    L1i cache:                       256 KiB (8 instances)
    L2 cache:                        4 MiB (8 instances)
    L3 cache:                        16 MiB (1 instance)
    NUMA node(s):                    1
    NUMA node0 CPU(s):               0-15
    Vulnerability Itlb multihit:     Not affected
    Vulnerability L1tf:              Not affected
    Vulnerability Mds:               Not affected
    Vulnerability Meltdown:          Not affected
    Vulnerability Mmio stale data:   Not affected
    Vulnerability Retbleed:          Not affected
    Vulnerability Spec store bypass: Mitigation; Speculative Store Bypass disabled via prctl
    Vulnerability Spectre v1:        Mitigation; usercopy/swapgs barriers and __user pointer sanitization
    Vulnerability Spectre v2:        Mitigation; Retpolines, IBPB conditional, IBRS_FW, STIBP always-on, RSB filling, PBRSB-eIBRS Not affected
    Vulnerability Srbds:             Not affected
    Vulnerability Tsx async abort:   Not affected

\

##### [AMD virtualisation flags]

  ----------------- -------------------------------------------------------------------- ------------- -------
  Abbreviation      Name                                                                 Description   Notes

  `decodeassists`   Decode assists
  `flushbyasid`     Flush-by-ASID (Address-space identifiers^[\[30\]](#cite_note-30)^)
  `lbrv`            LBR (Last branch record) virtualization
  `npt`             Nested page tables
  `nrip_save`       SVM (Secure virtualization machine) next_rip save
  `pausefilter`     Filtered pause intercept
  `pfthreshold`     Pause filter threshold
  `svm_lock`        SVM locking MSR
  `tsc_scale`       TSC (Timestamp-counter) scaling
  `vmcb_clean`      VMCB clean bits
  ----------------- -------------------------------------------------------------------- ------------- -------

#### [lspci]

`root `[`#`]`lspci -k -n -vvv`

    00:00.0 0600: 1022:14b5 (rev 01)
        Subsystem: 1022:14b5
        Control: I/O- Mem- BusMaster- SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx-
        Status: Cap- 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-

    00:00.2 0806: 1022:14b6
        Subsystem: 1022:14b6
        Control: I/O- Mem- BusMaster+ SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx+
        Status: Cap+ 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
        Latency: 0
        Interrupt: pin A routed to IRQ 24
        Capabilities: [40] Secure device <?>
        Capabilities: [64] MSI: Enable+ Count=1/4 Maskable- 64bit+
            Address: 00000000fee03000  Data: 0021
        Capabilities: [74] HyperTransport: MSI Mapping Enable+ Fixed+

    00:01.0 0600: 1022:14b7 (rev 01)
        Control: I/O- Mem- BusMaster- SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx-
        Status: Cap- 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
        IOMMU group: 0

    00:01.1 0604: 1022:14b8 (prog-if 00 [Normal decode])
        Subsystem: 1043:1d42
        Control: I/O+ Mem+ BusMaster+ SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx+
        Status: Cap+ 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
        Latency: 0, Cache Line Size: 64 bytes
        Interrupt: pin ? routed to IRQ 30
        IOMMU group: 1
        Bus: primary=00, secondary=01, subordinate=03, sec-latency=0
        I/O behind bridge: f000-ffff [size=4K] [16-bit]
        Memory behind bridge: fca00000-fccfffff [size=3M] [32-bit]
        Prefetchable memory behind bridge: 7c00000000-7e0fffffff [size=8448M] [32-bit]
        Secondary status: 66MHz- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort+ <SERR- <PERR-
        BridgeCtl: Parity- SERR+ NoISA- VGA- VGA16+ MAbort- >Reset- FastB2B-
            PriDiscTmr- SecDiscTmr- DiscTmrStat- DiscTmrSERREn-
        Capabilities: [50] Power Management version 3
            Flags: PMEClk- DSI- D1- D2- AuxCurrent=0mA PME(D0+,D1-,D2-,D3hot+,D3cold+)
            Status: D0 NoSoftRst- PME-Enable- DSel=0 DScale=0 PME-
        Capabilities: [58] Express (v2) Root Port (Slot+), MSI 00
            DevCap: MaxPayload 256 bytes, PhantFunc 0
                ExtTag+ RBE+
            DevCtl: CorrErr+ NonFatalErr+ FatalErr+ UnsupReq+
                RlxdOrd+ ExtTag+ PhantFunc- AuxPwr- NoSnoop+
                MaxPayload 256 bytes, MaxReadReq 512 bytes
            DevSta: CorrErr- NonFatalErr- FatalErr- UnsupReq- AuxPwr- TransPend-
            LnkCap: Port #0, Speed 16GT/s, Width x8, ASPM not supported
                ClockPM- Surprise- LLActRep+ BwNot+ ASPMOptComp+
            LnkCtl: ASPM Disabled; RCB 64 bytes, Disabled- CommClk+
                ExtSynch- ClockPM- AutWidDis- BWInt- AutBWInt-
            LnkSta: Speed 16GT/s, Width x8
                TrErr- Train- SlotClk+ DLActive+ BWMgmt+ ABWMgmt+
            SltCap: AttnBtn- PwrCtrl- MRL- AttnInd- PwrInd- HotPlug+ Surprise-
                Slot #0, PowerLimit 75W; Interlock- NoCompl+
            SltCtl: Enable: AttnBtn- PwrFlt- MRL- PresDet+ CmdCplt- HPIrq+ LinkChg+
                Control: AttnInd Unknown, PwrInd Unknown, Power- Interlock-
            SltSta: Status: AttnBtn- PowerFlt- MRL- CmdCplt- PresDet+ Interlock-
                Changed: MRL- PresDet- LinkState-
            RootCap: CRSVisible+
            RootCtl: ErrCorrectable- ErrNon-Fatal- ErrFatal- PMEIntEna+ CRSVisible+
            RootSta: PME ReqID 0000, PMEStatus- PMEPending-
            DevCap2: Completion Timeout: Range ABCD, TimeoutDis+ NROPrPrP- LTR+
                 10BitTagComp+ 10BitTagReq+ OBFF Not Supported, ExtFmt+ EETLPPrefix+, MaxEETLPPrefixes 1
                 EmergencyPowerReduction Not Supported, EmergencyPowerReductionInit-
                 FRS- LN System CLS Not Supported, TPHComp+ ExtTPHComp- ARIFwd+
                 AtomicOpsCap: Routing+ 32bit+ 64bit+ 128bitCAS-
            DevCtl2: Completion Timeout: 65ms to 210ms, TimeoutDis- LTR+ 10BitTagReq+ OBFF Disabled, ARIFwd-
                 AtomicOpsCtl: ReqEn- EgressBlck-
            LnkCap2: Supported Link Speeds: 2.5-16GT/s, Crosslink- Retimer+ 2Retimers+ DRS-
            LnkCtl2: Target Link Speed: 16GT/s, EnterCompliance- SpeedDis-
                 Transmit Margin: Normal Operating Range, EnterModifiedCompliance- ComplianceSOS-
                 Compliance Preset/De-emphasis: -6dB de-emphasis, 0dB preshoot
            LnkSta2: Current De-emphasis Level: -3.5dB, EqualizationComplete+ EqualizationPhase1+
                 EqualizationPhase2+ EqualizationPhase3+ LinkEqualizationRequest-
                 Retimer- 2Retimers- CrosslinkRes: unsupported
        Capabilities: [a0] MSI: Enable+ Count=1/1 Maskable- 64bit+
            Address: 00000000fee00000  Data: 0000
        Capabilities: [c0] Subsystem: 1043:1d42
        Capabilities: [c8] HyperTransport: MSI Mapping Enable+ Fixed+
        Capabilities: [100 v1] Vendor Specific Information: ID=0001 Rev=1 Len=010 <?>
        Capabilities: [150 v2] Advanced Error Reporting
            UESta:  DLP- SDES- TLP- FCP- CmpltTO- CmpltAbrt- UnxCmplt- RxOF- MalfTLP- ECRC- UnsupReq- ACSViol-
            UEMsk:  DLP- SDES- TLP- FCP- CmpltTO- CmpltAbrt- UnxCmplt- RxOF- MalfTLP- ECRC- UnsupReq- ACSViol-
            UESvrt: DLP- SDES+ TLP- FCP+ CmpltTO- CmpltAbrt- UnxCmplt- RxOF+ MalfTLP- ECRC- UnsupReq- ACSViol-
            CESta:  RxErr- BadTLP- BadDLLP- Rollover- Timeout- AdvNonFatalErr-
            CEMsk:  RxErr- BadTLP- BadDLLP- Rollover- Timeout- AdvNonFatalErr+
            AERCap: First Error Pointer: 00, ECRCGenCap+ ECRCGenEn- ECRCChkCap+ ECRCChkEn-
                MultHdrRecCap- MultHdrRecEn- TLPPfxPres- HdrLogCap-
            HeaderLog: 00000000 00000000 00000000 00000000
            RootCmd: CERptEn+ NFERptEn+ FERptEn+
            RootSta: CERcvd- MultCERcvd- UERcvd- MultUERcvd-
                 FirstFatal- NonFatalMsg- FatalMsg- IntMsg 0
            ErrorSrc: ERR_COR: 0000 ERR_FATAL/NONFATAL: 0000
        Capabilities: [270 v1] Secondary PCI Express
            LnkCtl3: LnkEquIntrruptEn- PerformEqu-
            LaneErrStat: 0
        Capabilities: [2a0 v1] Access Control Services
            ACSCap: SrcValid+ TransBlk+ ReqRedir+ CmpltRedir+ UpstreamFwd+ EgressCtrl- DirectTrans+
            ACSCtl: SrcValid+ TransBlk- ReqRedir+ CmpltRedir+ UpstreamFwd+ EgressCtrl- DirectTrans-
        Capabilities: [400 v1] Data Link Feature <?>
        Capabilities: [410 v1] Physical Layer 16.0 GT/s <?>
        Capabilities: [440 v1] Lane Margining at the Receiver <?>
        Kernel driver in use: pcieport

    00:02.0 0600: 1022:14b7 (rev 01)
        Control: I/O- Mem- BusMaster- SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx-
        Status: Cap- 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
        IOMMU group: 2

    00:02.1 0604: 1022:14ba (prog-if 00 [Normal decode])
        Subsystem: 1043:1d42
        Control: I/O+ Mem+ BusMaster+ SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx+
        Status: Cap+ 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
        Latency: 0, Cache Line Size: 64 bytes
        Interrupt: pin ? routed to IRQ 31
        IOMMU group: 3
        Bus: primary=00, secondary=04, subordinate=04, sec-latency=0
        I/O behind bridge: 0000f000-00000fff [disabled] [32-bit]
        Memory behind bridge: fcf00000-fcffffff [size=1M] [32-bit]
        Prefetchable memory behind bridge: 00000000fff00000-00000000000fffff [disabled] [64-bit]
        Secondary status: 66MHz- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- <SERR- <PERR-
        BridgeCtl: Parity- SERR+ NoISA- VGA- VGA16+ MAbort- >Reset- FastB2B-
            PriDiscTmr- SecDiscTmr- DiscTmrStat- DiscTmrSERREn-
        Capabilities: [50] Power Management version 3
            Flags: PMEClk- DSI- D1- D2- AuxCurrent=0mA PME(D0+,D1-,D2-,D3hot+,D3cold+)
            Status: D0 NoSoftRst- PME-Enable- DSel=0 DScale=0 PME-
        Capabilities: [58] Express (v2) Root Port (Slot+), MSI 00
            DevCap: MaxPayload 256 bytes, PhantFunc 0
                ExtTag+ RBE+
            DevCtl: CorrErr+ NonFatalErr+ FatalErr+ UnsupReq+
                RlxdOrd+ ExtTag+ PhantFunc- AuxPwr- NoSnoop+
                MaxPayload 128 bytes, MaxReadReq 512 bytes
            DevSta: CorrErr- NonFatalErr- FatalErr- UnsupReq- AuxPwr- TransPend-
            LnkCap: Port #3, Speed 16GT/s, Width x1, ASPM L1, Exit Latency L1 <64us
                ClockPM- Surprise- LLActRep+ BwNot+ ASPMOptComp+
            LnkCtl: ASPM L1 Enabled; RCB 64 bytes, Disabled- CommClk-
                ExtSynch- ClockPM- AutWidDis- BWInt- AutBWInt-
            LnkSta: Speed 2.5GT/s, Width x1
                TrErr- Train- SlotClk+ DLActive+ BWMgmt+ ABWMgmt-
            SltCap: AttnBtn- PwrCtrl- MRL- AttnInd- PwrInd- HotPlug- Surprise-
                Slot #0, PowerLimit 75W; Interlock- NoCompl+
            SltCtl: Enable: AttnBtn- PwrFlt- MRL- PresDet- CmdCplt- HPIrq- LinkChg-
                Control: AttnInd Unknown, PwrInd Unknown, Power- Interlock-
            SltSta: Status: AttnBtn- PowerFlt- MRL- CmdCplt- PresDet+ Interlock-
                Changed: MRL- PresDet- LinkState+
            RootCap: CRSVisible+
            RootCtl: ErrCorrectable- ErrNon-Fatal- ErrFatal- PMEIntEna+ CRSVisible+
            RootSta: PME ReqID 0000, PMEStatus- PMEPending-
            DevCap2: Completion Timeout: Range ABCD, TimeoutDis+ NROPrPrP- LTR+
                 10BitTagComp+ 10BitTagReq+ OBFF Not Supported, ExtFmt+ EETLPPrefix+, MaxEETLPPrefixes 1
                 EmergencyPowerReduction Not Supported, EmergencyPowerReductionInit-
                 FRS- LN System CLS Not Supported, TPHComp+ ExtTPHComp- ARIFwd+
                 AtomicOpsCap: Routing+ 32bit+ 64bit+ 128bitCAS-
            DevCtl2: Completion Timeout: 65ms to 210ms, TimeoutDis- LTR+ 10BitTagReq- OBFF Disabled, ARIFwd-
                 AtomicOpsCtl: ReqEn- EgressBlck-
            LnkCap2: Supported Link Speeds: 2.5-16GT/s, Crosslink- Retimer+ 2Retimers+ DRS-
            LnkCtl2: Target Link Speed: 2.5GT/s, EnterCompliance- SpeedDis+
                 Transmit Margin: Normal Operating Range, EnterModifiedCompliance- ComplianceSOS-
                 Compliance Preset/De-emphasis: -6dB de-emphasis, 0dB preshoot
            LnkSta2: Current De-emphasis Level: -3.5dB, EqualizationComplete- EqualizationPhase1-
                 EqualizationPhase2- EqualizationPhase3- LinkEqualizationRequest-
                 Retimer- 2Retimers- CrosslinkRes: unsupported
        Capabilities: [a0] MSI: Enable+ Count=1/1 Maskable- 64bit+
            Address: 00000000fee00000  Data: 0000
        Capabilities: [c0] Subsystem: 1043:1d42
        Capabilities: [c8] HyperTransport: MSI Mapping Enable+ Fixed+
        Capabilities: [100 v1] Vendor Specific Information: ID=0001 Rev=1 Len=010 <?>
        Capabilities: [150 v2] Advanced Error Reporting
            UESta:  DLP- SDES- TLP- FCP- CmpltTO- CmpltAbrt- UnxCmplt- RxOF- MalfTLP- ECRC- UnsupReq- ACSViol-
            UEMsk:  DLP- SDES- TLP- FCP- CmpltTO- CmpltAbrt- UnxCmplt- RxOF- MalfTLP- ECRC- UnsupReq- ACSViol-
            UESvrt: DLP- SDES+ TLP- FCP+ CmpltTO- CmpltAbrt- UnxCmplt- RxOF+ MalfTLP- ECRC- UnsupReq- ACSViol-
            CESta:  RxErr- BadTLP- BadDLLP- Rollover- Timeout- AdvNonFatalErr-
            CEMsk:  RxErr- BadTLP- BadDLLP- Rollover- Timeout- AdvNonFatalErr+
            AERCap: First Error Pointer: 00, ECRCGenCap+ ECRCGenEn- ECRCChkCap+ ECRCChkEn-
                MultHdrRecCap- MultHdrRecEn- TLPPfxPres- HdrLogCap-
            HeaderLog: 00000000 00000000 00000000 00000000
            RootCmd: CERptEn+ NFERptEn+ FERptEn+
            RootSta: CERcvd- MultCERcvd- UERcvd- MultUERcvd-
                 FirstFatal- NonFatalMsg- FatalMsg- IntMsg 0
            ErrorSrc: ERR_COR: 0000 ERR_FATAL/NONFATAL: 0000
        Capabilities: [270 v1] Secondary PCI Express
            LnkCtl3: LnkEquIntrruptEn- PerformEqu-
            LaneErrStat: 0
        Capabilities: [2a0 v1] Access Control Services
            ACSCap: SrcValid+ TransBlk+ ReqRedir+ CmpltRedir+ UpstreamFwd+ EgressCtrl- DirectTrans+
            ACSCtl: SrcValid+ TransBlk- ReqRedir+ CmpltRedir+ UpstreamFwd+ EgressCtrl- DirectTrans-
        Capabilities: [370 v1] L1 PM Substates
            L1SubCap: PCI-PM_L1.2+ PCI-PM_L1.1+ ASPM_L1.2+ ASPM_L1.1+ L1_PM_Substates+
                  PortCommonModeRestoreTime=120us PortTPowerOnTime=150us
            L1SubCtl1: PCI-PM_L1.2+ PCI-PM_L1.1+ ASPM_L1.2+ ASPM_L1.1+
                   T_CommonMode=120us LTR1.2_Threshold=32768ns
            L1SubCtl2: T_PwrOn=150us
        Capabilities: [400 v1] Data Link Feature <?>
        Capabilities: [410 v1] Physical Layer 16.0 GT/s <?>
        Capabilities: [440 v1] Lane Margining at the Receiver <?>
        Kernel driver in use: pcieport

    00:02.2 0604: 1022:14ba (prog-if 00 [Normal decode])
        Subsystem: 1043:1d42
        Control: I/O+ Mem+ BusMaster+ SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx+
        Status: Cap+ 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
        Latency: 0, Cache Line Size: 64 bytes
        Interrupt: pin ? routed to IRQ 32
        IOMMU group: 4
        Bus: primary=00, secondary=05, subordinate=05, sec-latency=0
        I/O behind bridge: 0000f000-00000fff [disabled] [32-bit]
        Memory behind bridge: fce00000-fcefffff [size=1M] [32-bit]
        Prefetchable memory behind bridge: 7e30300000-7e303fffff [size=1M] [32-bit]
        Secondary status: 66MHz- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort+ <SERR- <PERR-
        BridgeCtl: Parity- SERR+ NoISA- VGA- VGA16+ MAbort- >Reset- FastB2B-
            PriDiscTmr- SecDiscTmr- DiscTmrStat- DiscTmrSERREn-
        Capabilities: [50] Power Management version 3
            Flags: PMEClk- DSI- D1- D2- AuxCurrent=0mA PME(D0+,D1-,D2-,D3hot+,D3cold+)
            Status: D0 NoSoftRst- PME-Enable- DSel=0 DScale=0 PME-
        Capabilities: [58] Express (v2) Root Port (Slot+), MSI 00
            DevCap: MaxPayload 256 bytes, PhantFunc 0
                ExtTag+ RBE+
            DevCtl: CorrErr+ NonFatalErr+ FatalErr+ UnsupReq+
                RlxdOrd+ ExtTag+ PhantFunc- AuxPwr- NoSnoop+
                MaxPayload 128 bytes, MaxReadReq 512 bytes
            DevSta: CorrErr- NonFatalErr- FatalErr- UnsupReq- AuxPwr- TransPend-
            LnkCap: Port #4, Speed 16GT/s, Width x1, ASPM L1, Exit Latency L1 <64us
                ClockPM- Surprise- LLActRep+ BwNot+ ASPMOptComp+
            LnkCtl: ASPM L1 Enabled; RCB 64 bytes, Disabled- CommClk+
                ExtSynch- ClockPM- AutWidDis- BWInt- AutBWInt-
            LnkSta: Speed 5GT/s, Width x1
                TrErr- Train- SlotClk+ DLActive+ BWMgmt+ ABWMgmt-
            SltCap: AttnBtn- PwrCtrl- MRL- AttnInd- PwrInd- HotPlug- Surprise-
                Slot #0, PowerLimit 75W; Interlock- NoCompl+
            SltCtl: Enable: AttnBtn- PwrFlt- MRL- PresDet- CmdCplt- HPIrq- LinkChg-
                Control: AttnInd Unknown, PwrInd Unknown, Power- Interlock-
            SltSta: Status: AttnBtn- PowerFlt- MRL- CmdCplt- PresDet+ Interlock-
                Changed: MRL- PresDet- LinkState+
            RootCap: CRSVisible+
            RootCtl: ErrCorrectable- ErrNon-Fatal- ErrFatal- PMEIntEna+ CRSVisible+
            RootSta: PME ReqID 0000, PMEStatus- PMEPending-
            DevCap2: Completion Timeout: Range ABCD, TimeoutDis+ NROPrPrP- LTR+
                 10BitTagComp+ 10BitTagReq+ OBFF Not Supported, ExtFmt+ EETLPPrefix+, MaxEETLPPrefixes 1
                 EmergencyPowerReduction Not Supported, EmergencyPowerReductionInit-
                 FRS- LN System CLS Not Supported, TPHComp+ ExtTPHComp- ARIFwd+
                 AtomicOpsCap: Routing+ 32bit+ 64bit+ 128bitCAS-
            DevCtl2: Completion Timeout: 65ms to 210ms, TimeoutDis- LTR+ 10BitTagReq- OBFF Disabled, ARIFwd-
                 AtomicOpsCtl: ReqEn- EgressBlck-
            LnkCap2: Supported Link Speeds: 2.5-16GT/s, Crosslink- Retimer+ 2Retimers+ DRS-
            LnkCtl2: Target Link Speed: 5GT/s, EnterCompliance- SpeedDis-
                 Transmit Margin: Normal Operating Range, EnterModifiedCompliance- ComplianceSOS-
                 Compliance Preset/De-emphasis: -6dB de-emphasis, 0dB preshoot
            LnkSta2: Current De-emphasis Level: -3.5dB, EqualizationComplete- EqualizationPhase1-
                 EqualizationPhase2- EqualizationPhase3- LinkEqualizationRequest-
                 Retimer- 2Retimers- CrosslinkRes: unsupported
        Capabilities: [a0] MSI: Enable+ Count=1/1 Maskable- 64bit+
            Address: 00000000fee00000  Data: 0000
        Capabilities: [c0] Subsystem: 1043:1d42
        Capabilities: [c8] HyperTransport: MSI Mapping Enable+ Fixed+
        Capabilities: [100 v1] Vendor Specific Information: ID=0001 Rev=1 Len=010 <?>
        Capabilities: [150 v2] Advanced Error Reporting
            UESta:  DLP- SDES- TLP- FCP- CmpltTO- CmpltAbrt- UnxCmplt- RxOF- MalfTLP- ECRC- UnsupReq- ACSViol-
            UEMsk:  DLP- SDES- TLP- FCP- CmpltTO- CmpltAbrt- UnxCmplt- RxOF- MalfTLP- ECRC- UnsupReq- ACSViol-
            UESvrt: DLP- SDES+ TLP- FCP+ CmpltTO- CmpltAbrt- UnxCmplt- RxOF+ MalfTLP- ECRC- UnsupReq- ACSViol-
            CESta:  RxErr- BadTLP- BadDLLP- Rollover- Timeout- AdvNonFatalErr-
            CEMsk:  RxErr- BadTLP- BadDLLP- Rollover- Timeout- AdvNonFatalErr+
            AERCap: First Error Pointer: 00, ECRCGenCap+ ECRCGenEn- ECRCChkCap+ ECRCChkEn-
                MultHdrRecCap- MultHdrRecEn- TLPPfxPres- HdrLogCap-
            HeaderLog: 00000000 00000000 00000000 00000000
            RootCmd: CERptEn+ NFERptEn+ FERptEn+
            RootSta: CERcvd- MultCERcvd- UERcvd- MultUERcvd-
                 FirstFatal- NonFatalMsg- FatalMsg- IntMsg 0
            ErrorSrc: ERR_COR: 0000 ERR_FATAL/NONFATAL: 0000
        Capabilities: [270 v1] Secondary PCI Express
            LnkCtl3: LnkEquIntrruptEn- PerformEqu-
            LaneErrStat: 0
        Capabilities: [2a0 v1] Access Control Services
            ACSCap: SrcValid+ TransBlk+ ReqRedir+ CmpltRedir+ UpstreamFwd+ EgressCtrl- DirectTrans+
            ACSCtl: SrcValid+ TransBlk- ReqRedir+ CmpltRedir+ UpstreamFwd+ EgressCtrl- DirectTrans-
        Capabilities: [370 v1] L1 PM Substates
            L1SubCap: PCI-PM_L1.2+ PCI-PM_L1.1+ ASPM_L1.2+ ASPM_L1.1+ L1_PM_Substates+
                  PortCommonModeRestoreTime=10us PortTPowerOnTime=150us
            L1SubCtl1: PCI-PM_L1.2+ PCI-PM_L1.1+ ASPM_L1.2+ ASPM_L1.1+
                   T_CommonMode=10us LTR1.2_Threshold=166912ns
            L1SubCtl2: T_PwrOn=150us
        Capabilities: [400 v1] Data Link Feature <?>
        Capabilities: [410 v1] Physical Layer 16.0 GT/s <?>
        Capabilities: [440 v1] Lane Margining at the Receiver <?>
        Kernel driver in use: pcieport

    00:02.4 0604: 1022:14ba (prog-if 00 [Normal decode])
        Subsystem: 1043:1d42
        Control: I/O+ Mem+ BusMaster+ SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx+
        Status: Cap+ 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
        Latency: 0, Cache Line Size: 64 bytes
        Interrupt: pin ? routed to IRQ 33
        IOMMU group: 5
        Bus: primary=00, secondary=06, subordinate=06, sec-latency=0
        I/O behind bridge: 0000f000-00000fff [disabled] [32-bit]
        Memory behind bridge: fcd00000-fcdfffff [size=1M] [32-bit]
        Prefetchable memory behind bridge: 00000000fff00000-00000000000fffff [disabled] [64-bit]
        Secondary status: 66MHz- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort+ <SERR- <PERR-
        BridgeCtl: Parity- SERR+ NoISA- VGA- VGA16+ MAbort- >Reset- FastB2B-
            PriDiscTmr- SecDiscTmr- DiscTmrStat- DiscTmrSERREn-
        Capabilities: [50] Power Management version 3
            Flags: PMEClk- DSI- D1- D2- AuxCurrent=0mA PME(D0+,D1-,D2-,D3hot+,D3cold+)
            Status: D0 NoSoftRst- PME-Enable- DSel=0 DScale=0 PME-
        Capabilities: [58] Express (v2) Root Port (Slot+), MSI 00
            DevCap: MaxPayload 256 bytes, PhantFunc 0
                ExtTag+ RBE+
            DevCtl: CorrErr+ NonFatalErr+ FatalErr+ UnsupReq+
                RlxdOrd+ ExtTag+ PhantFunc- AuxPwr- NoSnoop+
                MaxPayload 256 bytes, MaxReadReq 512 bytes
            DevSta: CorrErr- NonFatalErr- FatalErr- UnsupReq- AuxPwr- TransPend-
            LnkCap: Port #0, Speed 16GT/s, Width x4, ASPM L1, Exit Latency L1 <64us
                ClockPM- Surprise- LLActRep+ BwNot+ ASPMOptComp+
            LnkCtl: ASPM L1 Enabled; RCB 64 bytes, Disabled- CommClk+
                ExtSynch- ClockPM- AutWidDis- BWInt- AutBWInt-
            LnkSta: Speed 16GT/s, Width x4
                TrErr- Train- SlotClk+ DLActive+ BWMgmt+ ABWMgmt-
            SltCap: AttnBtn- PwrCtrl- MRL- AttnInd- PwrInd- HotPlug- Surprise-
                Slot #0, PowerLimit 75W; Interlock- NoCompl+
            SltCtl: Enable: AttnBtn- PwrFlt- MRL- PresDet- CmdCplt- HPIrq- LinkChg-
                Control: AttnInd Unknown, PwrInd Unknown, Power- Interlock-
            SltSta: Status: AttnBtn- PowerFlt- MRL- CmdCplt- PresDet+ Interlock-
                Changed: MRL- PresDet- LinkState+
            RootCap: CRSVisible+
            RootCtl: ErrCorrectable- ErrNon-Fatal- ErrFatal- PMEIntEna+ CRSVisible+
            RootSta: PME ReqID 0000, PMEStatus- PMEPending-
            DevCap2: Completion Timeout: Range ABCD, TimeoutDis+ NROPrPrP- LTR+
                 10BitTagComp+ 10BitTagReq+ OBFF Not Supported, ExtFmt+ EETLPPrefix+, MaxEETLPPrefixes 1
                 EmergencyPowerReduction Not Supported, EmergencyPowerReductionInit-
                 FRS- LN System CLS Not Supported, TPHComp+ ExtTPHComp- ARIFwd+
                 AtomicOpsCap: Routing+ 32bit+ 64bit+ 128bitCAS-
            DevCtl2: Completion Timeout: 65ms to 210ms, TimeoutDis- LTR+ 10BitTagReq+ OBFF Disabled, ARIFwd+
                 AtomicOpsCtl: ReqEn- EgressBlck-
            LnkCap2: Supported Link Speeds: 2.5-16GT/s, Crosslink- Retimer+ 2Retimers+ DRS-
            LnkCtl2: Target Link Speed: 16GT/s, EnterCompliance- SpeedDis-
                 Transmit Margin: Normal Operating Range, EnterModifiedCompliance- ComplianceSOS-
                 Compliance Preset/De-emphasis: -6dB de-emphasis, 0dB preshoot
            LnkSta2: Current De-emphasis Level: -3.5dB, EqualizationComplete+ EqualizationPhase1+
                 EqualizationPhase2+ EqualizationPhase3+ LinkEqualizationRequest-
                 Retimer- 2Retimers- CrosslinkRes: unsupported
        Capabilities: [a0] MSI: Enable+ Count=1/1 Maskable- 64bit+
            Address: 00000000fee00000  Data: 0000
        Capabilities: [c0] Subsystem: 1043:1d42
        Capabilities: [c8] HyperTransport: MSI Mapping Enable+ Fixed+
        Capabilities: [100 v1] Vendor Specific Information: ID=0001 Rev=1 Len=010 <?>
        Capabilities: [150 v2] Advanced Error Reporting
            UESta:  DLP- SDES- TLP- FCP- CmpltTO- CmpltAbrt- UnxCmplt- RxOF- MalfTLP- ECRC- UnsupReq- ACSViol-
            UEMsk:  DLP- SDES- TLP- FCP- CmpltTO- CmpltAbrt- UnxCmplt- RxOF- MalfTLP- ECRC- UnsupReq- ACSViol-
            UESvrt: DLP- SDES+ TLP- FCP+ CmpltTO- CmpltAbrt- UnxCmplt- RxOF+ MalfTLP- ECRC- UnsupReq- ACSViol-
            CESta:  RxErr- BadTLP- BadDLLP- Rollover- Timeout- AdvNonFatalErr-
            CEMsk:  RxErr- BadTLP- BadDLLP- Rollover- Timeout- AdvNonFatalErr+
            AERCap: First Error Pointer: 00, ECRCGenCap+ ECRCGenEn- ECRCChkCap+ ECRCChkEn-
                MultHdrRecCap- MultHdrRecEn- TLPPfxPres- HdrLogCap-
            HeaderLog: 00000000 00000000 00000000 00000000
            RootCmd: CERptEn+ NFERptEn+ FERptEn+
            RootSta: CERcvd- MultCERcvd- UERcvd- MultUERcvd-
                 FirstFatal- NonFatalMsg- FatalMsg- IntMsg 0
            ErrorSrc: ERR_COR: 0000 ERR_FATAL/NONFATAL: 0000
        Capabilities: [270 v1] Secondary PCI Express
            LnkCtl3: LnkEquIntrruptEn- PerformEqu-
            LaneErrStat: 0
        Capabilities: [2a0 v1] Access Control Services
            ACSCap: SrcValid+ TransBlk+ ReqRedir+ CmpltRedir+ UpstreamFwd+ EgressCtrl- DirectTrans+
            ACSCtl: SrcValid+ TransBlk- ReqRedir+ CmpltRedir+ UpstreamFwd+ EgressCtrl- DirectTrans-
        Capabilities: [370 v1] L1 PM Substates
            L1SubCap: PCI-PM_L1.2+ PCI-PM_L1.1+ ASPM_L1.2+ ASPM_L1.1+ L1_PM_Substates+
                  PortCommonModeRestoreTime=10us PortTPowerOnTime=150us
            L1SubCtl1: PCI-PM_L1.2+ PCI-PM_L1.1+ ASPM_L1.2+ ASPM_L1.1+
                   T_CommonMode=10us LTR1.2_Threshold=166912ns
            L1SubCtl2: T_PwrOn=150us
        Capabilities: [400 v1] Data Link Feature <?>
        Capabilities: [410 v1] Physical Layer 16.0 GT/s <?>
        Capabilities: [440 v1] Lane Margining at the Receiver <?>
        Kernel driver in use: pcieport

    00:03.0 0600: 1022:14b7 (rev 01)
        Control: I/O- Mem- BusMaster- SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx-
        Status: Cap- 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
        IOMMU group: 6

    00:04.0 0600: 1022:14b7 (rev 01)
        Control: I/O- Mem- BusMaster- SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx-
        Status: Cap- 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
        IOMMU group: 7

    00:08.0 0600: 1022:14b7 (rev 01)
        Control: I/O- Mem- BusMaster- SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx-
        Status: Cap- 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
        IOMMU group: 8

    00:08.1 0604: 1022:14b9 (rev 10) (prog-if 00 [Normal decode])
        Subsystem: 1022:14b9
        Control: I/O+ Mem+ BusMaster+ SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx+
        Status: Cap+ 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
        Latency: 0, Cache Line Size: 64 bytes
        Interrupt: pin A routed to IRQ 34
        IOMMU group: 9
        Bus: primary=00, secondary=07, subordinate=07, sec-latency=0
        I/O behind bridge: e000-efff [size=4K] [16-bit]
        Memory behind bridge: fc300000-fc6fffff [size=4M] [32-bit]
        Prefetchable memory behind bridge: 7e20000000-7e301fffff [size=258M] [32-bit]
        Secondary status: 66MHz- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- <SERR- <PERR-
        BridgeCtl: Parity- SERR+ NoISA- VGA- VGA16+ MAbort- >Reset- FastB2B-
            PriDiscTmr- SecDiscTmr- DiscTmrStat- DiscTmrSERREn-
        Capabilities: [50] Power Management version 3
            Flags: PMEClk- DSI- D1- D2- AuxCurrent=0mA PME(D0+,D1-,D2-,D3hot+,D3cold+)
            Status: D0 NoSoftRst- PME-Enable- DSel=0 DScale=0 PME-
        Capabilities: [58] Express (v2) Root Port (Slot-), MSI 00
            DevCap: MaxPayload 512 bytes, PhantFunc 0
                ExtTag+ RBE+
            DevCtl: CorrErr- NonFatalErr- FatalErr- UnsupReq-
                RlxdOrd+ ExtTag+ PhantFunc- AuxPwr- NoSnoop+
                MaxPayload 256 bytes, MaxReadReq 512 bytes
            DevSta: CorrErr- NonFatalErr- FatalErr- UnsupReq- AuxPwr- TransPend-
            LnkCap: Port #0, Speed 16GT/s, Width x16, ASPM L0s L1, Exit Latency L0s <64ns, L1 <1us
                ClockPM- Surprise- LLActRep+ BwNot+ ASPMOptComp+
            LnkCtl: ASPM Disabled; RCB 64 bytes, Disabled- CommClk+
                ExtSynch- ClockPM- AutWidDis- BWInt- AutBWInt-
            LnkSta: Speed 16GT/s, Width x16
                TrErr- Train- SlotClk+ DLActive+ BWMgmt+ ABWMgmt-
            RootCap: CRSVisible+
            RootCtl: ErrCorrectable- ErrNon-Fatal- ErrFatal- PMEIntEna+ CRSVisible+
            RootSta: PME ReqID 0000, PMEStatus- PMEPending-
            DevCap2: Completion Timeout: Not Supported, TimeoutDis- NROPrPrP- LTR-
                 10BitTagComp+ 10BitTagReq- OBFF Not Supported, ExtFmt+ EETLPPrefix+, MaxEETLPPrefixes 4
                 EmergencyPowerReduction Not Supported, EmergencyPowerReductionInit-
                 FRS- LN System CLS Not Supported, TPHComp- ExtTPHComp- ARIFwd-
                 AtomicOpsCap: Routing+ 32bit- 64bit- 128bitCAS-
            DevCtl2: Completion Timeout: 50us to 50ms, TimeoutDis- LTR- 10BitTagReq- OBFF Disabled, ARIFwd-
                 AtomicOpsCtl: ReqEn- EgressBlck-
            LnkCap2: Supported Link Speeds: 2.5-16GT/s, Crosslink- Retimer+ 2Retimers+ DRS-
            LnkCtl2: Target Link Speed: 16GT/s, EnterCompliance- SpeedDis-
                 Transmit Margin: Normal Operating Range, EnterModifiedCompliance- ComplianceSOS-
                 Compliance Preset/De-emphasis: -6dB de-emphasis, 0dB preshoot
            LnkSta2: Current De-emphasis Level: -3.5dB, EqualizationComplete+ EqualizationPhase1+
                 EqualizationPhase2+ EqualizationPhase3+ LinkEqualizationRequest-
                 Retimer- 2Retimers- CrosslinkRes: unsupported
        Capabilities: [a0] MSI: Enable+ Count=1/1 Maskable- 64bit+
            Address: 00000000fee00000  Data: 0000
        Capabilities: [c0] Subsystem: 1022:14b9
        Capabilities: [100 v1] Vendor Specific Information: ID=0001 Rev=1 Len=010 <?>
        Capabilities: [270 v1] Secondary PCI Express
            LnkCtl3: LnkEquIntrruptEn- PerformEqu-
            LaneErrStat: 0
        Capabilities: [2a0 v1] Access Control Services
            ACSCap: SrcValid+ TransBlk+ ReqRedir+ CmpltRedir+ UpstreamFwd+ EgressCtrl- DirectTrans+
            ACSCtl: SrcValid+ TransBlk- ReqRedir+ CmpltRedir+ UpstreamFwd+ EgressCtrl- DirectTrans-
        Capabilities: [400 v1] Data Link Feature <?>
        Capabilities: [410 v1] Physical Layer 16.0 GT/s <?>
        Capabilities: [450 v1] Lane Margining at the Receiver <?>
        Kernel driver in use: pcieport

    00:08.3 0604: 1022:14b9 (rev 10) (prog-if 00 [Normal decode])
        Subsystem: 1022:14b9
        Control: I/O+ Mem+ BusMaster+ SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx+
        Status: Cap+ 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
        Latency: 0, Cache Line Size: 64 bytes
        Interrupt: pin A routed to IRQ 35
        IOMMU group: 10
        Bus: primary=00, secondary=08, subordinate=08, sec-latency=0
        I/O behind bridge: 0000f000-00000fff [disabled] [32-bit]
        Memory behind bridge: fc700000-fc9fffff [size=3M] [32-bit]
        Prefetchable memory behind bridge: 00000000fff00000-00000000000fffff [disabled] [64-bit]
        Secondary status: 66MHz- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- <SERR- <PERR-
        BridgeCtl: Parity- SERR+ NoISA- VGA- VGA16+ MAbort- >Reset- FastB2B-
            PriDiscTmr- SecDiscTmr- DiscTmrStat- DiscTmrSERREn-
        Capabilities: [50] Power Management version 3
            Flags: PMEClk- DSI- D1- D2- AuxCurrent=0mA PME(D0+,D1-,D2-,D3hot+,D3cold+)
            Status: D0 NoSoftRst- PME-Enable- DSel=0 DScale=0 PME-
        Capabilities: [58] Express (v2) Root Port (Slot-), MSI 00
            DevCap: MaxPayload 512 bytes, PhantFunc 0
                ExtTag+ RBE+
            DevCtl: CorrErr+ NonFatalErr+ FatalErr+ UnsupReq+
                RlxdOrd+ ExtTag+ PhantFunc- AuxPwr- NoSnoop+
                MaxPayload 256 bytes, MaxReadReq 512 bytes
            DevSta: CorrErr- NonFatalErr- FatalErr- UnsupReq- AuxPwr- TransPend-
            LnkCap: Port #0, Speed 16GT/s, Width x16, ASPM L0s L1, Exit Latency L0s <64ns, L1 <1us
                ClockPM- Surprise- LLActRep+ BwNot+ ASPMOptComp+
            LnkCtl: ASPM Disabled; RCB 64 bytes, Disabled- CommClk+
                ExtSynch- ClockPM- AutWidDis- BWInt- AutBWInt-
            LnkSta: Speed 16GT/s, Width x16
                TrErr- Train- SlotClk+ DLActive+ BWMgmt+ ABWMgmt-
            RootCap: CRSVisible+
            RootCtl: ErrCorrectable- ErrNon-Fatal- ErrFatal- PMEIntEna+ CRSVisible+
            RootSta: PME ReqID 0000, PMEStatus- PMEPending-
            DevCap2: Completion Timeout: Not Supported, TimeoutDis- NROPrPrP- LTR-
                 10BitTagComp+ 10BitTagReq- OBFF Not Supported, ExtFmt- EETLPPrefix-
                 EmergencyPowerReduction Not Supported, EmergencyPowerReductionInit-
                 FRS- LN System CLS Not Supported, TPHComp- ExtTPHComp- ARIFwd-
                 AtomicOpsCap: Routing- 32bit- 64bit- 128bitCAS-
            DevCtl2: Completion Timeout: 50us to 50ms, TimeoutDis- LTR- 10BitTagReq- OBFF Disabled, ARIFwd-
                 AtomicOpsCtl: ReqEn- EgressBlck-
            LnkCap2: Supported Link Speeds: 2.5-16GT/s, Crosslink- Retimer+ 2Retimers+ DRS-
            LnkCtl2: Target Link Speed: 16GT/s, EnterCompliance- SpeedDis-
                 Transmit Margin: Normal Operating Range, EnterModifiedCompliance- ComplianceSOS-
                 Compliance Preset/De-emphasis: -6dB de-emphasis, 0dB preshoot
            LnkSta2: Current De-emphasis Level: -3.5dB, EqualizationComplete+ EqualizationPhase1+
                 EqualizationPhase2+ EqualizationPhase3+ LinkEqualizationRequest-
                 Retimer- 2Retimers- CrosslinkRes: unsupported
        Capabilities: [a0] MSI: Enable+ Count=1/1 Maskable- 64bit+
            Address: 00000000fee00000  Data: 0000
        Capabilities: [c0] Subsystem: 1022:14b9
        Capabilities: [100 v1] Vendor Specific Information: ID=0001 Rev=1 Len=010 <?>
        Capabilities: [150 v2] Advanced Error Reporting
            UESta:  DLP- SDES- TLP- FCP- CmpltTO- CmpltAbrt- UnxCmplt- RxOF- MalfTLP- ECRC- UnsupReq- ACSViol-
            UEMsk:  DLP- SDES- TLP- FCP- CmpltTO- CmpltAbrt- UnxCmplt- RxOF- MalfTLP- ECRC- UnsupReq- ACSViol-
            UESvrt: DLP+ SDES+ TLP- FCP+ CmpltTO- CmpltAbrt- UnxCmplt- RxOF+ MalfTLP+ ECRC- UnsupReq- ACSViol-
            CESta:  RxErr- BadTLP- BadDLLP- Rollover- Timeout- AdvNonFatalErr-
            CEMsk:  RxErr- BadTLP- BadDLLP- Rollover- Timeout- AdvNonFatalErr+
            AERCap: First Error Pointer: 00, ECRCGenCap- ECRCGenEn- ECRCChkCap- ECRCChkEn-
                MultHdrRecCap- MultHdrRecEn- TLPPfxPres- HdrLogCap-
            HeaderLog: 00000000 00000000 00000000 00000000
            RootCmd: CERptEn+ NFERptEn+ FERptEn+
            RootSta: CERcvd- MultCERcvd- UERcvd- MultUERcvd-
                 FirstFatal- NonFatalMsg- FatalMsg- IntMsg 0
            ErrorSrc: ERR_COR: 0000 ERR_FATAL/NONFATAL: 0000
        Capabilities: [270 v1] Secondary PCI Express
            LnkCtl3: LnkEquIntrruptEn- PerformEqu-
            LaneErrStat: 0
        Capabilities: [2a0 v1] Access Control Services
            ACSCap: SrcValid+ TransBlk+ ReqRedir+ CmpltRedir+ UpstreamFwd+ EgressCtrl- DirectTrans+
            ACSCtl: SrcValid+ TransBlk- ReqRedir+ CmpltRedir+ UpstreamFwd+ EgressCtrl- DirectTrans-
        Capabilities: [400 v1] Data Link Feature <?>
        Capabilities: [410 v1] Physical Layer 16.0 GT/s <?>
        Capabilities: [450 v1] Lane Margining at the Receiver <?>
        Kernel driver in use: pcieport

    00:14.0 0c05: 1022:790b (rev 71)
        Subsystem: 1043:1d42
        Control: I/O+ Mem+ BusMaster- SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx+
        Status: Cap- 66MHz+ UDF- FastB2B- ParErr- DEVSEL=medium >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
        IOMMU group: 11
        Kernel driver in use: piix4_smbus

    00:14.3 0601: 1022:790e (rev 51)
        Subsystem: 1043:1d42
        Control: I/O+ Mem+ BusMaster+ SpecCycle+ MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx-
        Status: Cap- 66MHz+ UDF- FastB2B- ParErr- DEVSEL=medium >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
        Latency: 0
        IOMMU group: 11

    00:18.0 0600: 1022:1679
        Control: I/O- Mem- BusMaster- SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx-
        Status: Cap- 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
        IOMMU group: 12

    00:18.1 0600: 1022:167a
        Control: I/O- Mem- BusMaster- SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx-
        Status: Cap- 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
        IOMMU group: 12

    00:18.2 0600: 1022:167b
        Control: I/O- Mem- BusMaster- SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx-
        Status: Cap- 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
        IOMMU group: 12

    00:18.3 0600: 1022:167c
        Control: I/O- Mem- BusMaster- SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx-
        Status: Cap- 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
        IOMMU group: 12
        Kernel driver in use: k10temp

    00:18.4 0600: 1022:167d
        Control: I/O- Mem- BusMaster- SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx-
        Status: Cap- 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
        IOMMU group: 12

    00:18.5 0600: 1022:167e
        Control: I/O- Mem- BusMaster- SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx-
        Status: Cap- 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
        IOMMU group: 12

    00:18.6 0600: 1022:167f
        Control: I/O- Mem- BusMaster- SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx-
        Status: Cap- 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
        IOMMU group: 12

    00:18.7 0600: 1022:1680
        Control: I/O- Mem- BusMaster- SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx-
        Status: Cap- 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
        IOMMU group: 12

    01:00.0 0604: 1002:1478 (rev c2) (prog-if 00 [Normal decode])
        Physical Slot: 0
        Control: I/O+ Mem+ BusMaster+ SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx+
        Status: Cap+ 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
        Latency: 0, Cache Line Size: 64 bytes
        Interrupt: pin A routed to IRQ 37
        IOMMU group: 13
        Region 0: Memory at fcc00000 (32-bit, non-prefetchable) [size=16K]
        Bus: primary=01, secondary=02, subordinate=03, sec-latency=0
        I/O behind bridge: f000-ffff [size=4K] [16-bit]
        Memory behind bridge: fca00000-fcbfffff [size=2M] [32-bit]
        Prefetchable memory behind bridge: 7c00000000-7e0fffffff [size=8448M] [32-bit]
        Secondary status: 66MHz- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- <SERR- <PERR-
        BridgeCtl: Parity- SERR+ NoISA- VGA- VGA16+ MAbort- >Reset- FastB2B-
            PriDiscTmr- SecDiscTmr- DiscTmrStat- DiscTmrSERREn-
        Capabilities: [48] Vendor Specific Information: Len=08 <?>
        Capabilities: [50] Power Management version 3
            Flags: PMEClk- DSI- D1- D2- AuxCurrent=0mA PME(D0+,D1-,D2-,D3hot+,D3cold+)
            Status: D0 NoSoftRst+ PME-Enable- DSel=0 DScale=0 PME-
        Capabilities: [58] Express (v2) Upstream Port, MSI 00
            DevCap: MaxPayload 512 bytes, PhantFunc 0
                ExtTag+ AttnBtn- AttnInd- PwrInd- RBE+ SlotPowerLimit 75W
            DevCtl: CorrErr+ NonFatalErr+ FatalErr+ UnsupReq+
                RlxdOrd+ ExtTag+ PhantFunc- AuxPwr- NoSnoop+
                MaxPayload 256 bytes, MaxReadReq 512 bytes
            DevSta: CorrErr+ NonFatalErr- FatalErr- UnsupReq+ AuxPwr- TransPend-
            LnkCap: Port #0, Speed 16GT/s, Width x8, ASPM L1, Exit Latency L1 <64us
                ClockPM- Surprise- LLActRep- BwNot- ASPMOptComp+
            LnkCtl: ASPM Disabled; Disabled- CommClk+
                ExtSynch- ClockPM- AutWidDis- BWInt- AutBWInt-
            LnkSta: Speed 16GT/s, Width x8
                TrErr- Train- SlotClk+ DLActive- BWMgmt- ABWMgmt-
            DevCap2: Completion Timeout: Not Supported, TimeoutDis- NROPrPrP- LTR+
                 10BitTagComp+ 10BitTagReq+ OBFF Not Supported, ExtFmt+ EETLPPrefix+, MaxEETLPPrefixes 4
                 EmergencyPowerReduction Not Supported, EmergencyPowerReductionInit-
                 FRS-
                 AtomicOpsCap: Routing+ 32bit- 64bit- 128bitCAS-
            DevCtl2: Completion Timeout: 50us to 50ms, TimeoutDis- LTR+ 10BitTagReq+ OBFF Disabled,
                 AtomicOpsCtl: EgressBlck-
            LnkCap2: Supported Link Speeds: 2.5-16GT/s, Crosslink- Retimer+ 2Retimers+ DRS-
            LnkCtl2: Target Link Speed: 16GT/s, EnterCompliance- SpeedDis-
                 Transmit Margin: Normal Operating Range, EnterModifiedCompliance- ComplianceSOS-
                 Compliance Preset/De-emphasis: -6dB de-emphasis, 0dB preshoot
            LnkSta2: Current De-emphasis Level: -3.5dB, EqualizationComplete+ EqualizationPhase1+
                 EqualizationPhase2+ EqualizationPhase3+ LinkEqualizationRequest-
                 Retimer- 2Retimers- CrosslinkRes: unsupported
        Capabilities: [a0] MSI: Enable+ Count=1/1 Maskable- 64bit+
            Address: 00000000fee00000  Data: 0000
        Capabilities: [100 v1] Vendor Specific Information: ID=0001 Rev=1 Len=010 <?>
        Capabilities: [150 v2] Advanced Error Reporting
            UESta:  DLP- SDES- TLP- FCP- CmpltTO- CmpltAbrt- UnxCmplt- RxOF- MalfTLP- ECRC- UnsupReq- ACSViol-
            UEMsk:  DLP- SDES- TLP- FCP- CmpltTO- CmpltAbrt- UnxCmplt- RxOF- MalfTLP- ECRC- UnsupReq- ACSViol-
            UESvrt: DLP+ SDES+ TLP- FCP+ CmpltTO- CmpltAbrt- UnxCmplt- RxOF+ MalfTLP+ ECRC- UnsupReq- ACSViol-
            CESta:  RxErr- BadTLP- BadDLLP- Rollover- Timeout- AdvNonFatalErr-
            CEMsk:  RxErr- BadTLP- BadDLLP- Rollover- Timeout- AdvNonFatalErr+
            AERCap: First Error Pointer: 00, ECRCGenCap+ ECRCGenEn- ECRCChkCap+ ECRCChkEn-
                MultHdrRecCap- MultHdrRecEn- TLPPfxPres- HdrLogCap-
            HeaderLog: 00000000 00000000 00000000 00000000
        Capabilities: [270 v1] Secondary PCI Express
            LnkCtl3: LnkEquIntrruptEn- PerformEqu-
            LaneErrStat: 0
        Capabilities: [320 v1] Latency Tolerance Reporting
            Max snoop latency: 0ns
            Max no snoop latency: 0ns
        Capabilities: [370 v1] L1 PM Substates
            L1SubCap: PCI-PM_L1.2+ PCI-PM_L1.1+ ASPM_L1.2+ ASPM_L1.1+ L1_PM_Substates+
                  PortCommonModeRestoreTime=250us PortTPowerOnTime=170us
            L1SubCtl1: PCI-PM_L1.2- PCI-PM_L1.1- ASPM_L1.2- ASPM_L1.1-
                   T_CommonMode=0us LTR1.2_Threshold=0ns
            L1SubCtl2: T_PwrOn=10us
        Capabilities: [400 v1] Data Link Feature <?>
        Capabilities: [410 v1] Physical Layer 16.0 GT/s <?>
        Capabilities: [440 v1] Lane Margining at the Receiver <?>
        Kernel driver in use: pcieport

    02:00.0 0604: 1002:1479 (prog-if 00 [Normal decode])
        Subsystem: 1002:1479
        Control: I/O+ Mem+ BusMaster+ SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx+
        Status: Cap+ 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
        Latency: 0, Cache Line Size: 64 bytes
        Interrupt: pin A routed to IRQ 38
        IOMMU group: 14
        Bus: primary=02, secondary=03, subordinate=03, sec-latency=0
        I/O behind bridge: f000-ffff [size=4K] [16-bit]
        Memory behind bridge: fca00000-fcbfffff [size=2M] [32-bit]
        Prefetchable memory behind bridge: 7c00000000-7e0fffffff [size=8448M] [32-bit]
        Secondary status: 66MHz- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- <SERR- <PERR-
        BridgeCtl: Parity- SERR+ NoISA- VGA- VGA16+ MAbort- >Reset- FastB2B-
            PriDiscTmr- SecDiscTmr- DiscTmrStat- DiscTmrSERREn-
        Capabilities: [50] Power Management version 3
            Flags: PMEClk- DSI- D1- D2- AuxCurrent=0mA PME(D0+,D1-,D2-,D3hot+,D3cold+)
            Status: D0 NoSoftRst+ PME-Enable- DSel=0 DScale=0 PME-
        Capabilities: [58] Express (v2) Downstream Port (Slot-), MSI 00
            DevCap: MaxPayload 512 bytes, PhantFunc 0
                ExtTag+ RBE+
            DevCtl: CorrErr+ NonFatalErr+ FatalErr+ UnsupReq+
                RlxdOrd+ ExtTag+ PhantFunc- AuxPwr- NoSnoop+
                MaxPayload 256 bytes, MaxReadReq 512 bytes
            DevSta: CorrErr- NonFatalErr- FatalErr- UnsupReq- AuxPwr- TransPend-
            LnkCap: Port #0, Speed 16GT/s, Width x16, ASPM L0s L1, Exit Latency L0s <64ns, L1 <1us
                ClockPM- Surprise- LLActRep+ BwNot+ ASPMOptComp+
            LnkCtl: ASPM Disabled; Disabled- CommClk+
                ExtSynch- ClockPM- AutWidDis- BWInt- AutBWInt-
            LnkSta: Speed 16GT/s, Width x16
                TrErr- Train- SlotClk+ DLActive+ BWMgmt- ABWMgmt-
            DevCap2: Completion Timeout: Not Supported, TimeoutDis- NROPrPrP- LTR+
                 10BitTagComp+ 10BitTagReq+ OBFF Not Supported, ExtFmt+ EETLPPrefix+, MaxEETLPPrefixes 4
                 EmergencyPowerReduction Not Supported, EmergencyPowerReductionInit-
                 FRS- ARIFwd-
                 AtomicOpsCap: Routing+
            DevCtl2: Completion Timeout: 50us to 50ms, TimeoutDis- LTR+ 10BitTagReq+ OBFF Disabled, ARIFwd-
                 AtomicOpsCtl: EgressBlck-
            LnkCap2: Supported Link Speeds: 2.5-16GT/s, Crosslink- Retimer+ 2Retimers+ DRS-
            LnkCtl2: Target Link Speed: 16GT/s, EnterCompliance- SpeedDis-, Selectable De-emphasis: -3.5dB
                 Transmit Margin: Normal Operating Range, EnterModifiedCompliance- ComplianceSOS-
                 Compliance Preset/De-emphasis: -6dB de-emphasis, 0dB preshoot
            LnkSta2: Current De-emphasis Level: -3.5dB, EqualizationComplete+ EqualizationPhase1+
                 EqualizationPhase2+ EqualizationPhase3+ LinkEqualizationRequest-
                 Retimer- 2Retimers- CrosslinkRes: unsupported
        Capabilities: [a0] MSI: Enable+ Count=1/1 Maskable- 64bit+
            Address: 00000000fee00000  Data: 0000
        Capabilities: [c0] Subsystem: 1002:1479
        Capabilities: [100 v1] Vendor Specific Information: ID=0001 Rev=1 Len=010 <?>
        Capabilities: [150 v2] Advanced Error Reporting
            UESta:  DLP- SDES- TLP- FCP- CmpltTO- CmpltAbrt- UnxCmplt- RxOF- MalfTLP- ECRC- UnsupReq- ACSViol-
            UEMsk:  DLP- SDES- TLP- FCP- CmpltTO- CmpltAbrt- UnxCmplt- RxOF- MalfTLP- ECRC- UnsupReq- ACSViol-
            UESvrt: DLP+ SDES+ TLP- FCP+ CmpltTO- CmpltAbrt- UnxCmplt- RxOF+ MalfTLP+ ECRC- UnsupReq- ACSViol-
            CESta:  RxErr- BadTLP- BadDLLP- Rollover- Timeout- AdvNonFatalErr-
            CEMsk:  RxErr- BadTLP- BadDLLP- Rollover- Timeout- AdvNonFatalErr+
            AERCap: First Error Pointer: 00, ECRCGenCap+ ECRCGenEn- ECRCChkCap+ ECRCChkEn-
                MultHdrRecCap- MultHdrRecEn- TLPPfxPres- HdrLogCap-
            HeaderLog: 00000000 00000000 00000000 00000000
        Capabilities: [270 v1] Secondary PCI Express
            LnkCtl3: LnkEquIntrruptEn- PerformEqu-
            LaneErrStat: 0
        Capabilities: [2a0 v1] Access Control Services
            ACSCap: SrcValid+ TransBlk+ ReqRedir+ CmpltRedir+ UpstreamFwd+ EgressCtrl- DirectTrans+
            ACSCtl: SrcValid+ TransBlk- ReqRedir+ CmpltRedir+ UpstreamFwd+ EgressCtrl- DirectTrans-
        Capabilities: [400 v1] Data Link Feature <?>
        Capabilities: [410 v1] Physical Layer 16.0 GT/s <?>
        Capabilities: [440 v1] Lane Margining at the Receiver <?>
        Kernel driver in use: pcieport

    03:00.0 0300: 1002:73ef (rev c2) (prog-if 00 [VGA controller])
        Subsystem: 1043:1dec
        Physical Slot: 1
        Control: I/O+ Mem+ BusMaster+ SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx+
        Status: Cap+ 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
        Latency: 0, Cache Line Size: 64 bytes
        Interrupt: pin A routed to IRQ 39
        IOMMU group: 15
        Region 0: Memory at 7c00000000 (64-bit, prefetchable) [size=8G]
        Region 2: Memory at 7e00000000 (64-bit, prefetchable) [size=256M]
        Region 4: I/O ports at f000 [size=256]
        Region 5: Memory at fca00000 (32-bit, non-prefetchable) [size=1M]
        Expansion ROM at fcb00000 [disabled] [size=128K]
        Capabilities: [48] Vendor Specific Information: Len=08 <?>
        Capabilities: [50] Power Management version 3
            Flags: PMEClk- DSI- D1- D2- AuxCurrent=0mA PME(D0-,D1+,D2+,D3hot+,D3cold+)
            Status: D0 NoSoftRst+ PME-Enable- DSel=0 DScale=0 PME-
        Capabilities: [64] Express (v2) Legacy Endpoint, MSI 00
            DevCap: MaxPayload 256 bytes, PhantFunc 0, Latency L0s <4us, L1 unlimited
                ExtTag+ AttnBtn- AttnInd- PwrInd- RBE+ FLReset-
            DevCtl: CorrErr+ NonFatalErr+ FatalErr+ UnsupReq+
                RlxdOrd+ ExtTag+ PhantFunc- AuxPwr- NoSnoop+
                MaxPayload 256 bytes, MaxReadReq 512 bytes
            DevSta: CorrErr+ NonFatalErr- FatalErr- UnsupReq+ AuxPwr- TransPend-
            LnkCap: Port #0, Speed 16GT/s, Width x16, ASPM L0s L1, Exit Latency L0s <64ns, L1 <1us
                ClockPM+ Surprise- LLActRep- BwNot- ASPMOptComp+
            LnkCtl: ASPM Disabled; RCB 64 bytes, Disabled- CommClk+
                ExtSynch- ClockPM+ AutWidDis- BWInt- AutBWInt-
            LnkSta: Speed 16GT/s, Width x16
                TrErr- Train- SlotClk+ DLActive- BWMgmt- ABWMgmt-
            DevCap2: Completion Timeout: Range ABCD, TimeoutDis+ NROPrPrP- LTR+
                 10BitTagComp+ 10BitTagReq+ OBFF Not Supported, ExtFmt+ EETLPPrefix+, MaxEETLPPrefixes 1
                 EmergencyPowerReduction Not Supported, EmergencyPowerReductionInit-
                 FRS-
                 AtomicOpsCap: 32bit+ 64bit+ 128bitCAS-
            DevCtl2: Completion Timeout: 50us to 50ms, TimeoutDis- LTR+ 10BitTagReq+ OBFF Disabled,
                 AtomicOpsCtl: ReqEn+
            LnkCap2: Supported Link Speeds: 2.5-16GT/s, Crosslink- Retimer+ 2Retimers+ DRS-
            LnkCtl2: Target Link Speed: 16GT/s, EnterCompliance- SpeedDis-
                 Transmit Margin: Normal Operating Range, EnterModifiedCompliance- ComplianceSOS-
                 Compliance Preset/De-emphasis: -6dB de-emphasis, 0dB preshoot
            LnkSta2: Current De-emphasis Level: -3.5dB, EqualizationComplete+ EqualizationPhase1+
                 EqualizationPhase2+ EqualizationPhase3+ LinkEqualizationRequest-
                 Retimer- 2Retimers- CrosslinkRes: unsupported
        Capabilities: [a0] MSI: Enable+ Count=1/1 Maskable- 64bit+
            Address: 00000000fee00000  Data: 0000
        Capabilities: [100 v1] Vendor Specific Information: ID=0001 Rev=1 Len=010 <?>
        Capabilities: [150 v2] Advanced Error Reporting
            UESta:  DLP- SDES- TLP- FCP- CmpltTO- CmpltAbrt- UnxCmplt- RxOF- MalfTLP- ECRC- UnsupReq- ACSViol-
            UEMsk:  DLP- SDES- TLP- FCP- CmpltTO- CmpltAbrt- UnxCmplt- RxOF- MalfTLP- ECRC- UnsupReq- ACSViol-
            UESvrt: DLP+ SDES+ TLP- FCP+ CmpltTO- CmpltAbrt- UnxCmplt- RxOF+ MalfTLP+ ECRC- UnsupReq- ACSViol-
            CESta:  RxErr- BadTLP- BadDLLP- Rollover- Timeout- AdvNonFatalErr-
            CEMsk:  RxErr- BadTLP- BadDLLP- Rollover- Timeout- AdvNonFatalErr+
            AERCap: First Error Pointer: 00, ECRCGenCap+ ECRCGenEn- ECRCChkCap+ ECRCChkEn-
                MultHdrRecCap- MultHdrRecEn- TLPPfxPres- HdrLogCap-
            HeaderLog: 00000000 00000000 00000000 00000000
        Capabilities: [200 v1] Physical Resizable BAR
            BAR 0: current size: 8GB, supported: 256MB 512MB 1GB 2GB 4GB 8GB
            BAR 2: current size: 256MB, supported: 2MB 4MB 8MB 16MB 32MB 64MB 128MB 256MB
        Capabilities: [240 v1] Power Budgeting <?>
        Capabilities: [270 v1] Secondary PCI Express
            LnkCtl3: LnkEquIntrruptEn- PerformEqu-
            LaneErrStat: 0
        Capabilities: [2a0 v1] Access Control Services
            ACSCap: SrcValid- TransBlk- ReqRedir- CmpltRedir- UpstreamFwd- EgressCtrl- DirectTrans-
            ACSCtl: SrcValid- TransBlk- ReqRedir- CmpltRedir- UpstreamFwd- EgressCtrl- DirectTrans-
        Capabilities: [2d0 v1] Process Address Space ID (PASID)
            PASIDCap: Exec+ Priv+, Max PASID Width: 10
            PASIDCtl: Enable- Exec- Priv-
        Capabilities: [320 v1] Latency Tolerance Reporting
            Max snoop latency: 1048576ns
            Max no snoop latency: 1048576ns
        Capabilities: [410 v1] Physical Layer 16.0 GT/s <?>
        Capabilities: [440 v1] Lane Margining at the Receiver <?>
        Kernel driver in use: amdgpu

    03:00.1 0403: 1002:ab28
        Subsystem: 1043:1dec
        Physical Slot: 1
        Control: I/O- Mem+ BusMaster+ SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx+
        Status: Cap+ 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
        Latency: 0, Cache Line Size: 64 bytes
        Interrupt: pin B routed to IRQ 77
        IOMMU group: 16
        Region 0: Memory at fcb20000 (32-bit, non-prefetchable) [size=16K]
        Capabilities: [48] Vendor Specific Information: Len=08 <?>
        Capabilities: [50] Power Management version 3
            Flags: PMEClk- DSI- D1- D2- AuxCurrent=0mA PME(D0-,D1+,D2+,D3hot+,D3cold+)
            Status: D0 NoSoftRst+ PME-Enable- DSel=0 DScale=0 PME-
        Capabilities: [64] Express (v2) Legacy Endpoint, MSI 00
            DevCap: MaxPayload 256 bytes, PhantFunc 0, Latency L0s <4us, L1 unlimited
                ExtTag+ AttnBtn- AttnInd- PwrInd- RBE+ FLReset-
            DevCtl: CorrErr+ NonFatalErr+ FatalErr+ UnsupReq+
                RlxdOrd+ ExtTag+ PhantFunc- AuxPwr- NoSnoop+
                MaxPayload 256 bytes, MaxReadReq 512 bytes
            DevSta: CorrErr+ NonFatalErr- FatalErr- UnsupReq+ AuxPwr- TransPend-
            LnkCap: Port #0, Speed 16GT/s, Width x16, ASPM L0s L1, Exit Latency L0s <64ns, L1 <1us
                ClockPM+ Surprise- LLActRep- BwNot- ASPMOptComp+
            LnkCtl: ASPM Disabled; RCB 64 bytes, Disabled- CommClk+
                ExtSynch- ClockPM+ AutWidDis- BWInt- AutBWInt-
            LnkSta: Speed 16GT/s, Width x16
                TrErr- Train- SlotClk+ DLActive- BWMgmt- ABWMgmt-
            DevCap2: Completion Timeout: Range ABCD, TimeoutDis+ NROPrPrP- LTR+
                 10BitTagComp+ 10BitTagReq+ OBFF Not Supported, ExtFmt+ EETLPPrefix+, MaxEETLPPrefixes 1
                 EmergencyPowerReduction Not Supported, EmergencyPowerReductionInit-
                 FRS-
                 AtomicOpsCap: 32bit- 64bit- 128bitCAS-
            DevCtl2: Completion Timeout: 50us to 50ms, TimeoutDis- LTR- 10BitTagReq+ OBFF Disabled,
                 AtomicOpsCtl: ReqEn-
            LnkSta2: Current De-emphasis Level: -3.5dB, EqualizationComplete- EqualizationPhase1-
                 EqualizationPhase2- EqualizationPhase3- LinkEqualizationRequest-
                 Retimer- 2Retimers- CrosslinkRes: unsupported
        Capabilities: [a0] MSI: Enable+ Count=1/1 Maskable- 64bit+
            Address: 00000000fee00000  Data: 0000
        Capabilities: [100 v1] Vendor Specific Information: ID=0001 Rev=1 Len=010 <?>
        Capabilities: [150 v2] Advanced Error Reporting
            UESta:  DLP- SDES- TLP- FCP- CmpltTO- CmpltAbrt- UnxCmplt- RxOF- MalfTLP- ECRC- UnsupReq- ACSViol-
            UEMsk:  DLP- SDES- TLP- FCP- CmpltTO- CmpltAbrt- UnxCmplt- RxOF- MalfTLP- ECRC- UnsupReq- ACSViol-
            UESvrt: DLP+ SDES+ TLP- FCP+ CmpltTO- CmpltAbrt- UnxCmplt- RxOF+ MalfTLP+ ECRC- UnsupReq- ACSViol-
            CESta:  RxErr- BadTLP- BadDLLP- Rollover- Timeout- AdvNonFatalErr-
            CEMsk:  RxErr- BadTLP- BadDLLP- Rollover- Timeout- AdvNonFatalErr+
            AERCap: First Error Pointer: 00, ECRCGenCap+ ECRCGenEn- ECRCChkCap+ ECRCChkEn-
                MultHdrRecCap- MultHdrRecEn- TLPPfxPres- HdrLogCap-
            HeaderLog: 00000000 00000000 00000000 00000000
        Capabilities: [2a0 v1] Access Control Services
            ACSCap: SrcValid- TransBlk- ReqRedir- CmpltRedir- UpstreamFwd- EgressCtrl- DirectTrans-
            ACSCtl: SrcValid- TransBlk- ReqRedir- CmpltRedir- UpstreamFwd- EgressCtrl- DirectTrans-
        Kernel driver in use: snd_hda_intel

    04:00.0 0805: 1217:8520 (rev 01) (prog-if 01)
        Subsystem: 1043:202f
        Control: I/O- Mem+ BusMaster+ SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx+
        Status: Cap+ 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
        Latency: 0, Cache Line Size: 64 bytes
        Interrupt: pin A routed to IRQ 71
        IOMMU group: 17
        Region 0: Memory at fcf01000 (32-bit, non-prefetchable) [size=4K]
        Region 1: Memory at fcf00000 (32-bit, non-prefetchable) [size=2K]
        Capabilities: [6c] Power Management version 3
            Flags: PMEClk- DSI- D1- D2- AuxCurrent=55mA PME(D0-,D1-,D2-,D3hot+,D3cold+)
            Status: D0 NoSoftRst+ PME-Enable- DSel=0 DScale=0 PME-
        Capabilities: [48] MSI: Enable+ Count=1/1 Maskable+ 64bit+
            Address: 00000000fee00000  Data: 0000
            Masking: 00000000  Pending: 00000000
        Capabilities: [80] Express (v2) Endpoint, MSI 00
            DevCap: MaxPayload 128 bytes, PhantFunc 0, Latency L0s <4us, L1 unlimited
                ExtTag- AttnBtn- AttnInd- PwrInd- RBE+ FLReset- SlotPowerLimit 75W
            DevCtl: CorrErr- NonFatalErr- FatalErr- UnsupReq-
                RlxdOrd+ ExtTag- PhantFunc- AuxPwr+ NoSnoop+
                MaxPayload 128 bytes, MaxReadReq 128 bytes
            DevSta: CorrErr- NonFatalErr- FatalErr- UnsupReq- AuxPwr- TransPend-
            LnkCap: Port #0, Speed 2.5GT/s, Width x1, ASPM L0s L1, Exit Latency L0s <512ns, L1 unlimited
                ClockPM+ Surprise- LLActRep- BwNot- ASPMOptComp-
            LnkCtl: ASPM L1 Enabled; RCB 64 bytes, Disabled- CommClk-
                ExtSynch- ClockPM+ AutWidDis- BWInt- AutBWInt-
            LnkSta: Speed 2.5GT/s, Width x1
                TrErr- Train- SlotClk- DLActive- BWMgmt- ABWMgmt-
            DevCap2: Completion Timeout: Not Supported, TimeoutDis- NROPrPrP- LTR+
                 10BitTagComp- 10BitTagReq- OBFF Not Supported, ExtFmt- EETLPPrefix-
                 EmergencyPowerReduction Not Supported, EmergencyPowerReductionInit-
                 FRS- TPHComp- ExtTPHComp-
                 AtomicOpsCap: 32bit- 64bit- 128bitCAS-
            DevCtl2: Completion Timeout: 50us to 50ms, TimeoutDis- LTR+ 10BitTagReq- OBFF Disabled,
                 AtomicOpsCtl: ReqEn-
            LnkCtl2: Target Link Speed: 2.5GT/s, EnterCompliance- SpeedDis-
                 Transmit Margin: Normal Operating Range, EnterModifiedCompliance- ComplianceSOS-
                 Compliance Preset/De-emphasis: -6dB de-emphasis, 0dB preshoot
            LnkSta2: Current De-emphasis Level: -6dB, EqualizationComplete- EqualizationPhase1-
                 EqualizationPhase2- EqualizationPhase3- LinkEqualizationRequest-
                 Retimer- 2Retimers- CrosslinkRes: unsupported
        Capabilities: [100 v1] Virtual Channel
            Caps:   LPEVC=0 RefClk=100ns PATEntryBits=1
            Arb:    Fixed- WRR32- WRR64- WRR128-
            Ctrl:   ArbSelect=Fixed
            Status: InProgress-
            VC0:    Caps:   PATOffset=00 MaxTimeSlots=1 RejSnoopTrans-
                Arb:    Fixed- WRR32- WRR64- WRR128- TWRR128- WRR256-
                Ctrl:   Enable+ ID=0 ArbSelect=Fixed TC/VC=01
                Status: NegoPending- InProgress-
        Capabilities: [230 v1] Latency Tolerance Reporting
            Max snoop latency: 1048576ns
            Max no snoop latency: 1048576ns
        Capabilities: [240 v1] L1 PM Substates
            L1SubCap: PCI-PM_L1.2- PCI-PM_L1.1+ ASPM_L1.2- ASPM_L1.1+ L1_PM_Substates+
            L1SubCtl1: PCI-PM_L1.2- PCI-PM_L1.1+ ASPM_L1.2- ASPM_L1.1+
            L1SubCtl2:
        Kernel driver in use: sdhci-pci

    05:00.0 0280: 14c3:7922
        Subsystem: 1a3b:5300
        Control: I/O- Mem+ BusMaster+ SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx+
        Status: Cap+ 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
        Latency: 0, Cache Line Size: 64 bytes
        Interrupt: pin A routed to IRQ 44
        IOMMU group: 18
        Region 0: Memory at 7e30300000 (64-bit, prefetchable) [size=1M]
        Region 2: Memory at fce00000 (64-bit, non-prefetchable) [size=32K]
        Capabilities: [80] Express (v2) Endpoint, MSI 00
            DevCap: MaxPayload 128 bytes, PhantFunc 0, Latency L0s unlimited, L1 unlimited
                ExtTag+ AttnBtn- AttnInd- PwrInd- RBE+ FLReset+ SlotPowerLimit 75W
            DevCtl: CorrErr+ NonFatalErr+ FatalErr+ UnsupReq+
                RlxdOrd- ExtTag+ PhantFunc- AuxPwr- NoSnoop+ FLReset-
                MaxPayload 128 bytes, MaxReadReq 512 bytes
            DevSta: CorrErr- NonFatalErr- FatalErr- UnsupReq- AuxPwr- TransPend-
            LnkCap: Port #1, Speed 5GT/s, Width x1, ASPM L0s L1, Exit Latency L0s <2us, L1 <8us
                ClockPM- Surprise- LLActRep- BwNot- ASPMOptComp+
            LnkCtl: ASPM L1 Enabled; RCB 64 bytes, Disabled- CommClk+
                ExtSynch- ClockPM- AutWidDis- BWInt- AutBWInt-
            LnkSta: Speed 5GT/s, Width x1
                TrErr- Train- SlotClk+ DLActive- BWMgmt- ABWMgmt-
            DevCap2: Completion Timeout: Range ABCD, TimeoutDis+ NROPrPrP- LTR+
                 10BitTagComp- 10BitTagReq- OBFF Not Supported, ExtFmt+ EETLPPrefix-
                 EmergencyPowerReduction Not Supported, EmergencyPowerReductionInit-
                 FRS- TPHComp- ExtTPHComp-
                 AtomicOpsCap: 32bit- 64bit- 128bitCAS-
            DevCtl2: Completion Timeout: 50us to 50ms, TimeoutDis- LTR+ 10BitTagReq- OBFF Disabled,
                 AtomicOpsCtl: ReqEn-
            LnkCap2: Supported Link Speeds: 2.5-5GT/s, Crosslink- Retimer- 2Retimers- DRS-
            LnkCtl2: Target Link Speed: 5GT/s, EnterCompliance- SpeedDis-
                 Transmit Margin: Normal Operating Range, EnterModifiedCompliance- ComplianceSOS-
                 Compliance Preset/De-emphasis: -6dB de-emphasis, 0dB preshoot
            LnkSta2: Current De-emphasis Level: -3.5dB, EqualizationComplete- EqualizationPhase1-
                 EqualizationPhase2- EqualizationPhase3- LinkEqualizationRequest-
                 Retimer- 2Retimers- CrosslinkRes: unsupported
        Capabilities: [e0] MSI: Enable+ Count=1/32 Maskable+ 64bit+
            Address: 00000000fee00000  Data: 0000
            Masking: fffffffe  Pending: 00000000
        Capabilities: [f8] Power Management version 3
            Flags: PMEClk- DSI- D1- D2- AuxCurrent=0mA PME(D0+,D1-,D2-,D3hot+,D3cold+)
            Status: D0 NoSoftRst+ PME-Enable- DSel=0 DScale=0 PME-
        Capabilities: [100 v1] Vendor Specific Information: ID=1556 Rev=1 Len=008 <?>
        Capabilities: [108 v1] Latency Tolerance Reporting
            Max snoop latency: 1048576ns
            Max no snoop latency: 1048576ns
        Capabilities: [110 v1] L1 PM Substates
            L1SubCap: PCI-PM_L1.2+ PCI-PM_L1.1+ ASPM_L1.2+ ASPM_L1.1+ L1_PM_Substates+
                  PortCommonModeRestoreTime=3us PortTPowerOnTime=52us
            L1SubCtl1: PCI-PM_L1.2+ PCI-PM_L1.1+ ASPM_L1.2+ ASPM_L1.1+
                   T_CommonMode=0us LTR1.2_Threshold=166912ns
            L1SubCtl2: T_PwrOn=150us
        Capabilities: [200 v2] Advanced Error Reporting
            UESta:  DLP- SDES- TLP- FCP- CmpltTO- CmpltAbrt- UnxCmplt- RxOF- MalfTLP- ECRC- UnsupReq- ACSViol-
            UEMsk:  DLP- SDES- TLP- FCP- CmpltTO- CmpltAbrt- UnxCmplt- RxOF- MalfTLP- ECRC- UnsupReq- ACSViol-
            UESvrt: DLP+ SDES+ TLP- FCP+ CmpltTO- CmpltAbrt- UnxCmplt- RxOF+ MalfTLP+ ECRC- UnsupReq- ACSViol-
            CESta:  RxErr- BadTLP- BadDLLP- Rollover- Timeout- AdvNonFatalErr-
            CEMsk:  RxErr- BadTLP- BadDLLP- Rollover- Timeout- AdvNonFatalErr+
            AERCap: First Error Pointer: 00, ECRCGenCap- ECRCGenEn- ECRCChkCap- ECRCChkEn-
                MultHdrRecCap- MultHdrRecEn- TLPPfxPres- HdrLogCap-
            HeaderLog: 00000000 00000000 00000000 00000000
        Kernel driver in use: mt7921e

    06:00.0 0108: 144d:a80a (prog-if 02 [NVM Express])
        Subsystem: 144d:a801
        Control: I/O- Mem+ BusMaster+ SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx+
        Status: Cap+ 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
        Latency: 0, Cache Line Size: 64 bytes
        Interrupt: pin A routed to IRQ 43
        NUMA node: 0
        IOMMU group: 19
        Region 0: Memory at fcd00000 (64-bit, non-prefetchable) [size=16K]
        Capabilities: [40] Power Management version 3
            Flags: PMEClk- DSI- D1- D2- AuxCurrent=0mA PME(D0-,D1-,D2-,D3hot-,D3cold-)
            Status: D0 NoSoftRst+ PME-Enable- DSel=0 DScale=0 PME-
        Capabilities: [50] MSI: Enable- Count=1/32 Maskable- 64bit+
            Address: 0000000000000000  Data: 0000
        Capabilities: [70] Express (v2) Endpoint, MSI 00
            DevCap: MaxPayload 256 bytes, PhantFunc 0, Latency L0s unlimited, L1 unlimited
                ExtTag+ AttnBtn- AttnInd- PwrInd- RBE+ FLReset+ SlotPowerLimit 75W
            DevCtl: CorrErr+ NonFatalErr+ FatalErr+ UnsupReq+
                RlxdOrd+ ExtTag+ PhantFunc- AuxPwr- NoSnoop+ FLReset-
                MaxPayload 256 bytes, MaxReadReq 512 bytes
            DevSta: CorrErr+ NonFatalErr- FatalErr- UnsupReq+ AuxPwr- TransPend-
            LnkCap: Port #0, Speed 16GT/s, Width x4, ASPM L1, Exit Latency L1 <64us
                ClockPM+ Surprise- LLActRep- BwNot- ASPMOptComp+
            LnkCtl: ASPM L1 Enabled; RCB 64 bytes, Disabled- CommClk+
                ExtSynch- ClockPM- AutWidDis- BWInt- AutBWInt-
            LnkSta: Speed 16GT/s, Width x4
                TrErr- Train- SlotClk+ DLActive- BWMgmt- ABWMgmt-
            DevCap2: Completion Timeout: Range ABCD, TimeoutDis+ NROPrPrP- LTR+
                 10BitTagComp+ 10BitTagReq- OBFF Not Supported, ExtFmt- EETLPPrefix-
                 EmergencyPowerReduction Not Supported, EmergencyPowerReductionInit-
                 FRS- TPHComp- ExtTPHComp-
                 AtomicOpsCap: 32bit- 64bit- 128bitCAS-
            DevCtl2: Completion Timeout: 50us to 50ms, TimeoutDis- LTR+ 10BitTagReq- OBFF Disabled,
                 AtomicOpsCtl: ReqEn-
            LnkCap2: Supported Link Speeds: 2.5-16GT/s, Crosslink- Retimer+ 2Retimers+ DRS-
            LnkCtl2: Target Link Speed: 16GT/s, EnterCompliance- SpeedDis-
                 Transmit Margin: Normal Operating Range, EnterModifiedCompliance- ComplianceSOS-
                 Compliance Preset/De-emphasis: -6dB de-emphasis, 0dB preshoot
            LnkSta2: Current De-emphasis Level: -3.5dB, EqualizationComplete+ EqualizationPhase1+
                 EqualizationPhase2+ EqualizationPhase3+ LinkEqualizationRequest-
                 Retimer- 2Retimers- CrosslinkRes: Upstream Port
        Capabilities: [b0] MSI-X: Enable+ Count=130 Masked-
            Vector table: BAR=0 offset=00003000
            PBA: BAR=0 offset=00002000
        Capabilities: [100 v2] Advanced Error Reporting
            UESta:  DLP- SDES- TLP- FCP- CmpltTO- CmpltAbrt- UnxCmplt- RxOF- MalfTLP- ECRC- UnsupReq- ACSViol-
            UEMsk:  DLP- SDES- TLP- FCP- CmpltTO- CmpltAbrt- UnxCmplt- RxOF- MalfTLP- ECRC- UnsupReq- ACSViol-
            UESvrt: DLP+ SDES+ TLP- FCP+ CmpltTO- CmpltAbrt- UnxCmplt- RxOF+ MalfTLP+ ECRC- UnsupReq- ACSViol-
            CESta:  RxErr- BadTLP- BadDLLP- Rollover- Timeout- AdvNonFatalErr-
            CEMsk:  RxErr- BadTLP- BadDLLP- Rollover- Timeout- AdvNonFatalErr+
            AERCap: First Error Pointer: 00, ECRCGenCap+ ECRCGenEn- ECRCChkCap+ ECRCChkEn-
                MultHdrRecCap+ MultHdrRecEn- TLPPfxPres- HdrLogCap-
            HeaderLog: 00000000 00000000 00000000 00000000
        Capabilities: [168 v1] Alternative Routing-ID Interpretation (ARI)
            ARICap: MFVC- ACS-, Next Function: 0
            ARICtl: MFVC- ACS-, Function Group: 0
        Capabilities: [178 v1] Secondary PCI Express
            LnkCtl3: LnkEquIntrruptEn- PerformEqu-
            LaneErrStat: 0
        Capabilities: [198 v1] Physical Layer 16.0 GT/s <?>
        Capabilities: [1bc v1] Lane Margining at the Receiver <?>
        Capabilities: [214 v1] Latency Tolerance Reporting
            Max snoop latency: 1048576ns
            Max no snoop latency: 1048576ns
        Capabilities: [21c v1] L1 PM Substates
            L1SubCap: PCI-PM_L1.2+ PCI-PM_L1.1+ ASPM_L1.2+ ASPM_L1.1+ L1_PM_Substates+
                  PortCommonModeRestoreTime=10us PortTPowerOnTime=10us
            L1SubCtl1: PCI-PM_L1.2+ PCI-PM_L1.1+ ASPM_L1.2+ ASPM_L1.1+
                   T_CommonMode=0us LTR1.2_Threshold=166912ns
            L1SubCtl2: T_PwrOn=150us
        Capabilities: [3a0 v1] Data Link Feature <?>
        Kernel driver in use: nvme

    07:00.0 0300: 1002:1681 (rev c7) (prog-if 00 [VGA controller])
        Subsystem: 1043:1dec
        Control: I/O+ Mem+ BusMaster+ SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx+
        Status: Cap+ 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
        Latency: 0, Cache Line Size: 64 bytes
        Interrupt: pin A routed to IRQ 40
        IOMMU group: 20
        Region 0: Memory at 7e20000000 (64-bit, prefetchable) [size=256M]
        Region 2: Memory at 7e30000000 (64-bit, prefetchable) [size=2M]
        Region 4: I/O ports at e000 [size=256]
        Region 5: Memory at fc600000 (32-bit, non-prefetchable) [size=512K]
        Capabilities: [48] Vendor Specific Information: Len=08 <?>
        Capabilities: [50] Power Management version 3
            Flags: PMEClk- DSI- D1- D2- AuxCurrent=0mA PME(D0-,D1+,D2+,D3hot+,D3cold+)
            Status: D0 NoSoftRst- PME-Enable- DSel=0 DScale=0 PME-
        Capabilities: [64] Express (v2) Legacy Endpoint, MSI 00
            DevCap: MaxPayload 256 bytes, PhantFunc 0, Latency L0s <4us, L1 unlimited
                ExtTag+ AttnBtn- AttnInd- PwrInd- RBE+ FLReset-
            DevCtl: CorrErr- NonFatalErr- FatalErr- UnsupReq-
                RlxdOrd+ ExtTag+ PhantFunc- AuxPwr- NoSnoop+
                MaxPayload 256 bytes, MaxReadReq 512 bytes
            DevSta: CorrErr- NonFatalErr- FatalErr- UnsupReq- AuxPwr- TransPend-
            LnkCap: Port #0, Speed 16GT/s, Width x16, ASPM L0s L1, Exit Latency L0s <64ns, L1 <1us
                ClockPM- Surprise- LLActRep- BwNot- ASPMOptComp+
            LnkCtl: ASPM Disabled; RCB 64 bytes, Disabled- CommClk+
                ExtSynch- ClockPM- AutWidDis- BWInt- AutBWInt-
            LnkSta: Speed 16GT/s, Width x16
                TrErr- Train- SlotClk+ DLActive- BWMgmt- ABWMgmt-
            DevCap2: Completion Timeout: Range ABCD, TimeoutDis+ NROPrPrP- LTR-
                 10BitTagComp+ 10BitTagReq- OBFF Not Supported, ExtFmt+ EETLPPrefix+, MaxEETLPPrefixes 1
                 EmergencyPowerReduction Not Supported, EmergencyPowerReductionInit-
                 FRS-
                 AtomicOpsCap: 32bit+ 64bit+ 128bitCAS-
            DevCtl2: Completion Timeout: 50us to 50ms, TimeoutDis- LTR- 10BitTagReq- OBFF Disabled,
                 AtomicOpsCtl: ReqEn+
            LnkCap2: Supported Link Speeds: 2.5-16GT/s, Crosslink- Retimer+ 2Retimers+ DRS-
            LnkCtl2: Target Link Speed: 16GT/s, EnterCompliance- SpeedDis-
                 Transmit Margin: Normal Operating Range, EnterModifiedCompliance- ComplianceSOS-
                 Compliance Preset/De-emphasis: -6dB de-emphasis, 0dB preshoot
            LnkSta2: Current De-emphasis Level: -3.5dB, EqualizationComplete+ EqualizationPhase1+
                 EqualizationPhase2+ EqualizationPhase3+ LinkEqualizationRequest-
                 Retimer- 2Retimers- CrosslinkRes: unsupported
        Capabilities: [a0] MSI: Enable- Count=1/4 Maskable- 64bit+
            Address: 0000000000000000  Data: 0000
        Capabilities: [c0] MSI-X: Enable+ Count=4 Masked-
            Vector table: BAR=5 offset=00042000
            PBA: BAR=5 offset=00043000
        Capabilities: [100 v1] Vendor Specific Information: ID=0001 Rev=1 Len=010 <?>
        Capabilities: [270 v1] Secondary PCI Express
            LnkCtl3: LnkEquIntrruptEn- PerformEqu-
            LaneErrStat: 0
        Capabilities: [2a0 v1] Access Control Services
            ACSCap: SrcValid- TransBlk- ReqRedir- CmpltRedir- UpstreamFwd- EgressCtrl- DirectTrans-
            ACSCtl: SrcValid- TransBlk- ReqRedir- CmpltRedir- UpstreamFwd- EgressCtrl- DirectTrans-
        Capabilities: [2b0 v1] Address Translation Service (ATS)
            ATSCap: Invalidate Queue Depth: 00
            ATSCtl: Enable+, Smallest Translation Unit: 00
        Capabilities: [2c0 v1] Page Request Interface (PRI)
            PRICtl: Enable- Reset-
            PRISta: RF- UPRGI- Stopped+
            Page Request Capacity: 00000100, Page Request Allocation: 00000000
        Capabilities: [2d0 v1] Process Address Space ID (PASID)
            PASIDCap: Exec+ Priv+, Max PASID Width: 10
            PASIDCtl: Enable- Exec- Priv-
        Capabilities: [410 v1] Physical Layer 16.0 GT/s <?>
        Capabilities: [450 v1] Lane Margining at the Receiver <?>
        Kernel driver in use: amdgpu

    07:00.1 0403: 1002:1640
        Subsystem: 1002:1640
        Control: I/O- Mem+ BusMaster+ SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx+
        Status: Cap+ 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
        Latency: 0, Cache Line Size: 64 bytes
        Interrupt: pin B routed to IRQ 78
        IOMMU group: 21
        Region 0: Memory at fc6c8000 (32-bit, non-prefetchable) [size=16K]
        Capabilities: [48] Vendor Specific Information: Len=08 <?>
        Capabilities: [50] Power Management version 3
            Flags: PMEClk- DSI- D1- D2- AuxCurrent=0mA PME(D0-,D1+,D2+,D3hot+,D3cold+)
            Status: D0 NoSoftRst- PME-Enable- DSel=0 DScale=0 PME-
        Capabilities: [64] Express (v2) Legacy Endpoint, MSI 00
            DevCap: MaxPayload 256 bytes, PhantFunc 0, Latency L0s <4us, L1 unlimited
                ExtTag+ AttnBtn- AttnInd- PwrInd- RBE+ FLReset-
            DevCtl: CorrErr- NonFatalErr- FatalErr- UnsupReq-
                RlxdOrd+ ExtTag+ PhantFunc- AuxPwr- NoSnoop+
                MaxPayload 256 bytes, MaxReadReq 512 bytes
            DevSta: CorrErr- NonFatalErr- FatalErr- UnsupReq- AuxPwr- TransPend-
            LnkCap: Port #0, Speed 16GT/s, Width x16, ASPM L0s L1, Exit Latency L0s <64ns, L1 <1us
                ClockPM- Surprise- LLActRep- BwNot- ASPMOptComp+
            LnkCtl: ASPM Disabled; RCB 64 bytes, Disabled- CommClk+
                ExtSynch- ClockPM- AutWidDis- BWInt- AutBWInt-
            LnkSta: Speed 16GT/s, Width x16
                TrErr- Train- SlotClk+ DLActive- BWMgmt- ABWMgmt-
            DevCap2: Completion Timeout: Range ABCD, TimeoutDis+ NROPrPrP- LTR-
                 10BitTagComp+ 10BitTagReq- OBFF Not Supported, ExtFmt+ EETLPPrefix+, MaxEETLPPrefixes 1
                 EmergencyPowerReduction Not Supported, EmergencyPowerReductionInit-
                 FRS-
                 AtomicOpsCap: 32bit- 64bit- 128bitCAS-
            DevCtl2: Completion Timeout: 50us to 50ms, TimeoutDis- LTR- 10BitTagReq- OBFF Disabled,
                 AtomicOpsCtl: ReqEn+
            LnkSta2: Current De-emphasis Level: -3.5dB, EqualizationComplete- EqualizationPhase1-
                 EqualizationPhase2- EqualizationPhase3- LinkEqualizationRequest-
                 Retimer- 2Retimers- CrosslinkRes: unsupported
        Capabilities: [a0] MSI: Enable+ Count=1/1 Maskable- 64bit+
            Address: 00000000fee00000  Data: 0000
        Capabilities: [100 v1] Vendor Specific Information: ID=0001 Rev=1 Len=010 <?>
        Capabilities: [2a0 v1] Access Control Services
            ACSCap: SrcValid- TransBlk- ReqRedir- CmpltRedir- UpstreamFwd- EgressCtrl- DirectTrans-
            ACSCtl: SrcValid- TransBlk- ReqRedir- CmpltRedir- UpstreamFwd- EgressCtrl- DirectTrans-
        Kernel driver in use: snd_hda_intel

    07:00.2 1080: 1022:1649
        Subsystem: 1022:1649
        Control: I/O- Mem+ BusMaster+ SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx+
        Status: Cap+ 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
        Latency: 0, Cache Line Size: 64 bytes
        Interrupt: pin C routed to IRQ 72
        IOMMU group: 22
        Region 2: Memory at fc500000 (32-bit, non-prefetchable) [size=1M]
        Region 5: Memory at fc6cc000 (32-bit, non-prefetchable) [size=8K]
        Capabilities: [48] Vendor Specific Information: Len=08 <?>
        Capabilities: [50] Power Management version 3
            Flags: PMEClk- DSI- D1- D2- AuxCurrent=0mA PME(D0-,D1-,D2-,D3hot-,D3cold-)
            Status: D0 NoSoftRst+ PME-Enable- DSel=0 DScale=0 PME-
        Capabilities: [64] Express (v2) Endpoint, MSI 00
            DevCap: MaxPayload 256 bytes, PhantFunc 0, Latency L0s <4us, L1 unlimited
                ExtTag+ AttnBtn- AttnInd- PwrInd- RBE+ FLReset- SlotPowerLimit 0W
            DevCtl: CorrErr- NonFatalErr- FatalErr- UnsupReq-
                RlxdOrd+ ExtTag+ PhantFunc- AuxPwr- NoSnoop+
                MaxPayload 256 bytes, MaxReadReq 512 bytes
            DevSta: CorrErr- NonFatalErr- FatalErr- UnsupReq- AuxPwr- TransPend-
            LnkCap: Port #0, Speed 16GT/s, Width x16, ASPM L0s L1, Exit Latency L0s <64ns, L1 <1us
                ClockPM- Surprise- LLActRep- BwNot- ASPMOptComp+
            LnkCtl: ASPM Disabled; RCB 64 bytes, Disabled- CommClk+
                ExtSynch- ClockPM- AutWidDis- BWInt- AutBWInt-
            LnkSta: Speed 16GT/s, Width x16
                TrErr- Train- SlotClk+ DLActive- BWMgmt- ABWMgmt-
            DevCap2: Completion Timeout: Range ABCD, TimeoutDis+ NROPrPrP- LTR-
                 10BitTagComp+ 10BitTagReq- OBFF Not Supported, ExtFmt+ EETLPPrefix+, MaxEETLPPrefixes 1
                 EmergencyPowerReduction Not Supported, EmergencyPowerReductionInit-
                 FRS- TPHComp- ExtTPHComp-
                 AtomicOpsCap: 32bit- 64bit- 128bitCAS-
            DevCtl2: Completion Timeout: 50us to 50ms, TimeoutDis- LTR- 10BitTagReq- OBFF Disabled,
                 AtomicOpsCtl: ReqEn-
            LnkSta2: Current De-emphasis Level: -3.5dB, EqualizationComplete- EqualizationPhase1-
                 EqualizationPhase2- EqualizationPhase3- LinkEqualizationRequest-
                 Retimer- 2Retimers- CrosslinkRes: unsupported
        Capabilities: [a0] MSI: Enable- Count=1/2 Maskable- 64bit+
            Address: 0000000000000000  Data: 0000
        Capabilities: [c0] MSI-X: Enable+ Count=2 Masked-
            Vector table: BAR=5 offset=00000000
            PBA: BAR=5 offset=00001000
        Capabilities: [100 v1] Vendor Specific Information: ID=0001 Rev=1 Len=010 <?>
        Capabilities: [2a0 v1] Access Control Services
            ACSCap: SrcValid- TransBlk- ReqRedir- CmpltRedir- UpstreamFwd- EgressCtrl- DirectTrans-
            ACSCtl: SrcValid- TransBlk- ReqRedir- CmpltRedir- UpstreamFwd- EgressCtrl- DirectTrans-
        Kernel driver in use: ccp

    07:00.3 0c03: 1022:161d (prog-if 30 [XHCI])
        Subsystem: 1043:201f
        Control: I/O+ Mem+ BusMaster+ SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx+
        Status: Cap+ 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
        Latency: 0, Cache Line Size: 64 bytes
        Interrupt: pin D routed to IRQ 63
        IOMMU group: 23
        Region 0: Memory at fc400000 (64-bit, non-prefetchable) [size=1M]
        Capabilities: [48] Vendor Specific Information: Len=08 <?>
        Capabilities: [50] Power Management version 3
            Flags: PMEClk- DSI- D1- D2- AuxCurrent=0mA PME(D0+,D1-,D2-,D3hot+,D3cold+)
            Status: D0 NoSoftRst- PME-Enable- DSel=0 DScale=0 PME-
        Capabilities: [64] Express (v2) Endpoint, MSI 00
            DevCap: MaxPayload 256 bytes, PhantFunc 0, Latency L0s <4us, L1 unlimited
                ExtTag+ AttnBtn- AttnInd- PwrInd- RBE+ FLReset- SlotPowerLimit 0W
            DevCtl: CorrErr- NonFatalErr- FatalErr- UnsupReq-
                RlxdOrd+ ExtTag+ PhantFunc- AuxPwr- NoSnoop+
                MaxPayload 256 bytes, MaxReadReq 512 bytes
            DevSta: CorrErr- NonFatalErr- FatalErr- UnsupReq- AuxPwr- TransPend-
            LnkCap: Port #0, Speed 16GT/s, Width x16, ASPM L0s L1, Exit Latency L0s <64ns, L1 <1us
                ClockPM- Surprise- LLActRep- BwNot- ASPMOptComp+
            LnkCtl: ASPM Disabled; RCB 64 bytes, Disabled- CommClk+
                ExtSynch- ClockPM- AutWidDis- BWInt- AutBWInt-
            LnkSta: Speed 16GT/s, Width x16
                TrErr- Train- SlotClk+ DLActive- BWMgmt- ABWMgmt-
            DevCap2: Completion Timeout: Range ABCD, TimeoutDis+ NROPrPrP- LTR-
                 10BitTagComp+ 10BitTagReq- OBFF Not Supported, ExtFmt+ EETLPPrefix+, MaxEETLPPrefixes 1
                 EmergencyPowerReduction Not Supported, EmergencyPowerReductionInit-
                 FRS- TPHComp- ExtTPHComp-
                 AtomicOpsCap: 32bit- 64bit- 128bitCAS-
            DevCtl2: Completion Timeout: 50us to 50ms, TimeoutDis- LTR- 10BitTagReq- OBFF Disabled,
                 AtomicOpsCtl: ReqEn-
            LnkSta2: Current De-emphasis Level: -3.5dB, EqualizationComplete- EqualizationPhase1-
                 EqualizationPhase2- EqualizationPhase3- LinkEqualizationRequest-
                 Retimer- 2Retimers- CrosslinkRes: unsupported
        Capabilities: [a0] MSI: Enable+ Count=1/1 Maskable- 64bit+
            Address: 00000000fee00000  Data: 0000
        Capabilities: [c0] MSI-X: Enable- Count=1 Masked-
            Vector table: BAR=0 offset=000fe000
            PBA: BAR=0 offset=000ff000
        Capabilities: [100 v1] Vendor Specific Information: ID=0001 Rev=1 Len=010 <?>
        Capabilities: [2a0 v1] Access Control Services
            ACSCap: SrcValid- TransBlk- ReqRedir- CmpltRedir- UpstreamFwd- EgressCtrl- DirectTrans-
            ACSCtl: SrcValid- TransBlk- ReqRedir- CmpltRedir- UpstreamFwd- EgressCtrl- DirectTrans-
        Kernel driver in use: xhci_hcd

    07:00.4 0c03: 1022:161e (prog-if 30 [XHCI])
        Subsystem: 1043:201f
        Control: I/O+ Mem+ BusMaster+ SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx+
        Status: Cap+ 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
        Latency: 0, Cache Line Size: 64 bytes
        Interrupt: pin A routed to IRQ 64
        IOMMU group: 24
        Region 0: Memory at fc300000 (64-bit, non-prefetchable) [size=1M]
        Capabilities: [48] Vendor Specific Information: Len=08 <?>
        Capabilities: [50] Power Management version 3
            Flags: PMEClk- DSI- D1- D2- AuxCurrent=0mA PME(D0+,D1-,D2-,D3hot+,D3cold+)
            Status: D0 NoSoftRst- PME-Enable- DSel=0 DScale=0 PME-
        Capabilities: [64] Express (v2) Endpoint, MSI 00
            DevCap: MaxPayload 256 bytes, PhantFunc 0, Latency L0s <4us, L1 unlimited
                ExtTag+ AttnBtn- AttnInd- PwrInd- RBE+ FLReset- SlotPowerLimit 0W
            DevCtl: CorrErr- NonFatalErr- FatalErr- UnsupReq-
                RlxdOrd+ ExtTag+ PhantFunc- AuxPwr- NoSnoop+
                MaxPayload 256 bytes, MaxReadReq 512 bytes
            DevSta: CorrErr- NonFatalErr- FatalErr- UnsupReq- AuxPwr- TransPend-
            LnkCap: Port #0, Speed 16GT/s, Width x16, ASPM L0s L1, Exit Latency L0s <64ns, L1 <1us
                ClockPM- Surprise- LLActRep- BwNot- ASPMOptComp+
            LnkCtl: ASPM Disabled; RCB 64 bytes, Disabled- CommClk+
                ExtSynch- ClockPM- AutWidDis- BWInt- AutBWInt-
            LnkSta: Speed 16GT/s, Width x16
                TrErr- Train- SlotClk+ DLActive- BWMgmt- ABWMgmt-
            DevCap2: Completion Timeout: Range ABCD, TimeoutDis+ NROPrPrP- LTR-
                 10BitTagComp+ 10BitTagReq- OBFF Not Supported, ExtFmt+ EETLPPrefix+, MaxEETLPPrefixes 1
                 EmergencyPowerReduction Not Supported, EmergencyPowerReductionInit-
                 FRS- TPHComp- ExtTPHComp-
                 AtomicOpsCap: 32bit- 64bit- 128bitCAS-
            DevCtl2: Completion Timeout: 50us to 50ms, TimeoutDis- LTR- 10BitTagReq- OBFF Disabled,
                 AtomicOpsCtl: ReqEn-
            LnkSta2: Current De-emphasis Level: -3.5dB, EqualizationComplete- EqualizationPhase1-
                 EqualizationPhase2- EqualizationPhase3- LinkEqualizationRequest-
                 Retimer- 2Retimers- CrosslinkRes: unsupported
        Capabilities: [a0] MSI: Enable+ Count=1/1 Maskable- 64bit+
            Address: 00000000fee00000  Data: 0000
        Capabilities: [c0] MSI-X: Enable- Count=1 Masked-
            Vector table: BAR=0 offset=000fe000
            PBA: BAR=0 offset=000ff000
        Capabilities: [100 v1] Vendor Specific Information: ID=0001 Rev=1 Len=010 <?>
        Capabilities: [2a0 v1] Access Control Services
            ACSCap: SrcValid- TransBlk- ReqRedir- CmpltRedir- UpstreamFwd- EgressCtrl- DirectTrans-
            ACSCtl: SrcValid- TransBlk- ReqRedir- CmpltRedir- UpstreamFwd- EgressCtrl- DirectTrans-
        Kernel driver in use: xhci_hcd

    07:00.5 0480: 1022:15e2 (rev 60)
        Subsystem: 1043:1d42
        Control: I/O- Mem+ BusMaster+ SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx-
        Status: Cap+ 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
        Latency: 0, Cache Line Size: 64 bytes
        Interrupt: pin B routed to IRQ 76
        IOMMU group: 25
        Region 0: Memory at fc680000 (32-bit, non-prefetchable) [size=256K]
        Capabilities: [48] Vendor Specific Information: Len=08 <?>
        Capabilities: [50] Power Management version 3
            Flags: PMEClk- DSI- D1- D2- AuxCurrent=0mA PME(D0+,D1-,D2-,D3hot+,D3cold+)
            Status: D0 NoSoftRst+ PME-Enable- DSel=0 DScale=0 PME-
        Capabilities: [64] Express (v2) Endpoint, MSI 00
            DevCap: MaxPayload 256 bytes, PhantFunc 0, Latency L0s <4us, L1 unlimited
                ExtTag+ AttnBtn- AttnInd- PwrInd- RBE+ FLReset- SlotPowerLimit 0W
            DevCtl: CorrErr- NonFatalErr- FatalErr- UnsupReq-
                RlxdOrd+ ExtTag+ PhantFunc- AuxPwr- NoSnoop+
                MaxPayload 256 bytes, MaxReadReq 512 bytes
            DevSta: CorrErr- NonFatalErr- FatalErr- UnsupReq- AuxPwr- TransPend-
            LnkCap: Port #0, Speed 16GT/s, Width x16, ASPM L0s L1, Exit Latency L0s <64ns, L1 <1us
                ClockPM- Surprise- LLActRep- BwNot- ASPMOptComp+
            LnkCtl: ASPM Disabled; RCB 64 bytes, Disabled- CommClk+
                ExtSynch- ClockPM- AutWidDis- BWInt- AutBWInt-
            LnkSta: Speed 16GT/s, Width x16
                TrErr- Train- SlotClk+ DLActive- BWMgmt- ABWMgmt-
            DevCap2: Completion Timeout: Range ABCD, TimeoutDis+ NROPrPrP- LTR-
                 10BitTagComp+ 10BitTagReq- OBFF Not Supported, ExtFmt+ EETLPPrefix+, MaxEETLPPrefixes 1
                 EmergencyPowerReduction Not Supported, EmergencyPowerReductionInit-
                 FRS- TPHComp- ExtTPHComp-
                 AtomicOpsCap: 32bit- 64bit- 128bitCAS-
            DevCtl2: Completion Timeout: 50us to 50ms, TimeoutDis- LTR- 10BitTagReq- OBFF Disabled,
                 AtomicOpsCtl: ReqEn-
            LnkSta2: Current De-emphasis Level: -3.5dB, EqualizationComplete- EqualizationPhase1-
                 EqualizationPhase2- EqualizationPhase3- LinkEqualizationRequest-
                 Retimer- 2Retimers- CrosslinkRes: unsupported
        Capabilities: [a0] MSI: Enable- Count=1/1 Maskable- 64bit+
            Address: 0000000000000000  Data: 0000
        Capabilities: [100 v1] Vendor Specific Information: ID=0001 Rev=1 Len=010 <?>
        Capabilities: [2a0 v1] Access Control Services
            ACSCap: SrcValid- TransBlk- ReqRedir- CmpltRedir- UpstreamFwd- EgressCtrl- DirectTrans-
            ACSCtl: SrcValid- TransBlk- ReqRedir- CmpltRedir- UpstreamFwd- EgressCtrl- DirectTrans-
        Kernel driver in use: snd_pci_acp6x

    07:00.6 0403: 1022:15e3
        Subsystem: 1043:1d42
        Control: I/O+ Mem+ BusMaster+ SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx+
        Status: Cap+ 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
        Latency: 0, Cache Line Size: 64 bytes
        Interrupt: pin C routed to IRQ 79
        IOMMU group: 26
        Region 0: Memory at fc6c0000 (32-bit, non-prefetchable) [size=32K]
        Capabilities: [48] Vendor Specific Information: Len=08 <?>
        Capabilities: [50] Power Management version 3
            Flags: PMEClk- DSI- D1- D2- AuxCurrent=0mA PME(D0+,D1-,D2-,D3hot+,D3cold+)
            Status: D0 NoSoftRst+ PME-Enable- DSel=0 DScale=0 PME-
        Capabilities: [64] Express (v2) Endpoint, MSI 00
            DevCap: MaxPayload 256 bytes, PhantFunc 0, Latency L0s <4us, L1 unlimited
                ExtTag+ AttnBtn- AttnInd- PwrInd- RBE+ FLReset- SlotPowerLimit 0W
            DevCtl: CorrErr- NonFatalErr- FatalErr- UnsupReq-
                RlxdOrd+ ExtTag+ PhantFunc- AuxPwr- NoSnoop+
                MaxPayload 256 bytes, MaxReadReq 512 bytes
            DevSta: CorrErr- NonFatalErr- FatalErr- UnsupReq- AuxPwr- TransPend-
            LnkCap: Port #0, Speed 16GT/s, Width x16, ASPM L0s L1, Exit Latency L0s <64ns, L1 <1us
                ClockPM- Surprise- LLActRep- BwNot- ASPMOptComp+
            LnkCtl: ASPM Disabled; RCB 64 bytes, Disabled- CommClk+
                ExtSynch- ClockPM- AutWidDis- BWInt- AutBWInt-
            LnkSta: Speed 16GT/s, Width x16
                TrErr- Train- SlotClk+ DLActive- BWMgmt- ABWMgmt-
            DevCap2: Completion Timeout: Range ABCD, TimeoutDis+ NROPrPrP- LTR-
                 10BitTagComp+ 10BitTagReq- OBFF Not Supported, ExtFmt+ EETLPPrefix+, MaxEETLPPrefixes 1
                 EmergencyPowerReduction Not Supported, EmergencyPowerReductionInit-
                 FRS- TPHComp- ExtTPHComp-
                 AtomicOpsCap: 32bit- 64bit- 128bitCAS-
            DevCtl2: Completion Timeout: 50us to 50ms, TimeoutDis- LTR- 10BitTagReq- OBFF Disabled,
                 AtomicOpsCtl: ReqEn-
            LnkSta2: Current De-emphasis Level: -3.5dB, EqualizationComplete- EqualizationPhase1-
                 EqualizationPhase2- EqualizationPhase3- LinkEqualizationRequest-
                 Retimer- 2Retimers- CrosslinkRes: unsupported
        Capabilities: [a0] MSI: Enable+ Count=1/1 Maskable- 64bit+
            Address: 00000000fee00000  Data: 0000
        Capabilities: [100 v1] Vendor Specific Information: ID=0001 Rev=1 Len=010 <?>
        Capabilities: [2a0 v1] Access Control Services
            ACSCap: SrcValid- TransBlk- ReqRedir- CmpltRedir- UpstreamFwd- EgressCtrl- DirectTrans-
            ACSCtl: SrcValid- TransBlk- ReqRedir- CmpltRedir- UpstreamFwd- EgressCtrl- DirectTrans-
        Kernel driver in use: snd_hda_intel

    08:00.0 0c03: 1022:161f (prog-if 30 [XHCI])
        Subsystem: 1043:201f
        Control: I/O+ Mem+ BusMaster+ SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx+
        Status: Cap+ 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
        Latency: 0, Cache Line Size: 64 bytes
        Interrupt: pin A routed to IRQ 66
        IOMMU group: 27
        Region 0: Memory at fc900000 (64-bit, non-prefetchable) [size=1M]
        Capabilities: [48] Vendor Specific Information: Len=08 <?>
        Capabilities: [50] Power Management version 3
            Flags: PMEClk- DSI- D1- D2- AuxCurrent=0mA PME(D0+,D1-,D2-,D3hot+,D3cold+)
            Status: D0 NoSoftRst- PME-Enable- DSel=0 DScale=0 PME-
        Capabilities: [64] Express (v2) Endpoint, MSI 00
            DevCap: MaxPayload 256 bytes, PhantFunc 0, Latency L0s <4us, L1 unlimited
                ExtTag+ AttnBtn- AttnInd- PwrInd- RBE+ FLReset- SlotPowerLimit 0W
            DevCtl: CorrErr- NonFatalErr- FatalErr- UnsupReq-
                RlxdOrd+ ExtTag+ PhantFunc- AuxPwr- NoSnoop+
                MaxPayload 256 bytes, MaxReadReq 512 bytes
            DevSta: CorrErr- NonFatalErr- FatalErr- UnsupReq- AuxPwr- TransPend-
            LnkCap: Port #0, Speed 16GT/s, Width x16, ASPM L0s L1, Exit Latency L0s <64ns, L1 <1us
                ClockPM- Surprise- LLActRep- BwNot- ASPMOptComp+
            LnkCtl: ASPM Disabled; RCB 64 bytes, Disabled- CommClk+
                ExtSynch- ClockPM- AutWidDis- BWInt- AutBWInt-
            LnkSta: Speed 16GT/s, Width x16
                TrErr- Train- SlotClk+ DLActive- BWMgmt- ABWMgmt-
            DevCap2: Completion Timeout: Range ABCD, TimeoutDis+ NROPrPrP- LTR-
                 10BitTagComp+ 10BitTagReq- OBFF Not Supported, ExtFmt- EETLPPrefix-
                 EmergencyPowerReduction Not Supported, EmergencyPowerReductionInit-
                 FRS- TPHComp- ExtTPHComp-
                 AtomicOpsCap: 32bit- 64bit- 128bitCAS-
            DevCtl2: Completion Timeout: 50us to 50ms, TimeoutDis- LTR- 10BitTagReq- OBFF Disabled,
                 AtomicOpsCtl: ReqEn-
            LnkCap2: Supported Link Speeds: 2.5-16GT/s, Crosslink- Retimer+ 2Retimers+ DRS-
            LnkCtl2: Target Link Speed: 16GT/s, EnterCompliance- SpeedDis-
                 Transmit Margin: Normal Operating Range, EnterModifiedCompliance- ComplianceSOS-
                 Compliance Preset/De-emphasis: -6dB de-emphasis, 0dB preshoot
            LnkSta2: Current De-emphasis Level: -3.5dB, EqualizationComplete+ EqualizationPhase1+
                 EqualizationPhase2+ EqualizationPhase3+ LinkEqualizationRequest-
                 Retimer- 2Retimers- CrosslinkRes: unsupported
        Capabilities: [a0] MSI: Enable+ Count=1/1 Maskable- 64bit+
            Address: 00000000fee00000  Data: 0000
        Capabilities: [c0] MSI-X: Enable- Count=1 Masked-
            Vector table: BAR=0 offset=000fe000
            PBA: BAR=0 offset=000ff000
        Capabilities: [100 v1] Vendor Specific Information: ID=0001 Rev=1 Len=010 <?>
        Capabilities: [270 v1] Secondary PCI Express
            LnkCtl3: LnkEquIntrruptEn- PerformEqu-
            LaneErrStat: 0
        Capabilities: [2a0 v1] Access Control Services
            ACSCap: SrcValid- TransBlk- ReqRedir- CmpltRedir- UpstreamFwd- EgressCtrl- DirectTrans-
            ACSCtl: SrcValid- TransBlk- ReqRedir- CmpltRedir- UpstreamFwd- EgressCtrl- DirectTrans-
        Capabilities: [410 v1] Physical Layer 16.0 GT/s <?>
        Capabilities: [450 v1] Lane Margining at the Receiver <?>
        Kernel driver in use: xhci_hcd

    08:00.3 0c03: 1022:15d6 (prog-if 30 [XHCI])
        Subsystem: 1022:15d6
        Control: I/O+ Mem+ BusMaster+ SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx+
        Status: Cap+ 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
        Latency: 0, Cache Line Size: 64 bytes
        Interrupt: pin C routed to IRQ 67
        IOMMU group: 28
        Region 0: Memory at fc800000 (64-bit, non-prefetchable) [size=1M]
        Capabilities: [48] Vendor Specific Information: Len=08 <?>
        Capabilities: [50] Power Management version 3
            Flags: PMEClk- DSI- D1- D2- AuxCurrent=0mA PME(D0+,D1-,D2-,D3hot+,D3cold+)
            Status: D0 NoSoftRst- PME-Enable- DSel=0 DScale=0 PME-
        Capabilities: [64] Express (v2) Endpoint, MSI 00
            DevCap: MaxPayload 256 bytes, PhantFunc 0, Latency L0s <4us, L1 unlimited
                ExtTag+ AttnBtn- AttnInd- PwrInd- RBE+ FLReset- SlotPowerLimit 0W
            DevCtl: CorrErr- NonFatalErr- FatalErr- UnsupReq-
                RlxdOrd+ ExtTag+ PhantFunc- AuxPwr- NoSnoop+
                MaxPayload 256 bytes, MaxReadReq 512 bytes
            DevSta: CorrErr- NonFatalErr- FatalErr- UnsupReq- AuxPwr- TransPend-
            LnkCap: Port #0, Speed 16GT/s, Width x16, ASPM L0s L1, Exit Latency L0s <64ns, L1 <1us
                ClockPM- Surprise- LLActRep- BwNot- ASPMOptComp+
            LnkCtl: ASPM Disabled; RCB 64 bytes, Disabled- CommClk+
                ExtSynch- ClockPM- AutWidDis- BWInt- AutBWInt-
            LnkSta: Speed 16GT/s, Width x16
                TrErr- Train- SlotClk+ DLActive- BWMgmt- ABWMgmt-
            DevCap2: Completion Timeout: Range ABCD, TimeoutDis+ NROPrPrP- LTR-
                 10BitTagComp+ 10BitTagReq- OBFF Not Supported, ExtFmt- EETLPPrefix-
                 EmergencyPowerReduction Not Supported, EmergencyPowerReductionInit-
                 FRS- TPHComp- ExtTPHComp-
                 AtomicOpsCap: 32bit- 64bit- 128bitCAS-
            DevCtl2: Completion Timeout: 50us to 50ms, TimeoutDis- LTR- 10BitTagReq- OBFF Disabled,
                 AtomicOpsCtl: ReqEn-
            LnkSta2: Current De-emphasis Level: -3.5dB, EqualizationComplete- EqualizationPhase1-
                 EqualizationPhase2- EqualizationPhase3- LinkEqualizationRequest-
                 Retimer- 2Retimers- CrosslinkRes: unsupported
        Capabilities: [a0] MSI: Enable+ Count=1/1 Maskable- 64bit+
            Address: 00000000fee00000  Data: 0000
        Capabilities: [c0] MSI-X: Enable- Count=1 Masked-
            Vector table: BAR=0 offset=000fe000
            PBA: BAR=0 offset=000ff000
        Capabilities: [100 v1] Vendor Specific Information: ID=0001 Rev=1 Len=010 <?>
        Capabilities: [2a0 v1] Access Control Services
            ACSCap: SrcValid- TransBlk- ReqRedir- CmpltRedir- UpstreamFwd- EgressCtrl- DirectTrans-
            ACSCtl: SrcValid- TransBlk- ReqRedir- CmpltRedir- UpstreamFwd- EgressCtrl- DirectTrans-
        Kernel driver in use: xhci_hcd

    08:00.4 0c03: 1022:15d7 (prog-if 30 [XHCI])
        Subsystem: 1022:15d7
        Control: I/O+ Mem+ BusMaster+ SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx+
        Status: Cap+ 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
        Latency: 0, Cache Line Size: 64 bytes
        Interrupt: pin D routed to IRQ 69
        IOMMU group: 29
        Region 0: Memory at fc700000 (64-bit, non-prefetchable) [size=1M]
        Capabilities: [48] Vendor Specific Information: Len=08 <?>
        Capabilities: [50] Power Management version 3
            Flags: PMEClk- DSI- D1- D2- AuxCurrent=0mA PME(D0+,D1-,D2-,D3hot+,D3cold+)
            Status: D0 NoSoftRst- PME-Enable- DSel=0 DScale=0 PME-
        Capabilities: [64] Express (v2) Endpoint, MSI 00
            DevCap: MaxPayload 256 bytes, PhantFunc 0, Latency L0s <4us, L1 unlimited
                ExtTag+ AttnBtn- AttnInd- PwrInd- RBE+ FLReset- SlotPowerLimit 0W
            DevCtl: CorrErr- NonFatalErr- FatalErr- UnsupReq-
                RlxdOrd+ ExtTag+ PhantFunc- AuxPwr- NoSnoop+
                MaxPayload 256 bytes, MaxReadReq 512 bytes
            DevSta: CorrErr- NonFatalErr- FatalErr- UnsupReq- AuxPwr- TransPend-
            LnkCap: Port #0, Speed 16GT/s, Width x16, ASPM L0s L1, Exit Latency L0s <64ns, L1 <1us
                ClockPM- Surprise- LLActRep- BwNot- ASPMOptComp+
            LnkCtl: ASPM Disabled; RCB 64 bytes, Disabled- CommClk+
                ExtSynch- ClockPM- AutWidDis- BWInt- AutBWInt-
            LnkSta: Speed 16GT/s, Width x16
                TrErr- Train- SlotClk+ DLActive- BWMgmt- ABWMgmt-
            DevCap2: Completion Timeout: Range ABCD, TimeoutDis+ NROPrPrP- LTR-
                 10BitTagComp+ 10BitTagReq- OBFF Not Supported, ExtFmt- EETLPPrefix-
                 EmergencyPowerReduction Not Supported, EmergencyPowerReductionInit-
                 FRS- TPHComp- ExtTPHComp-
                 AtomicOpsCap: 32bit- 64bit- 128bitCAS-
            DevCtl2: Completion Timeout: 50us to 50ms, TimeoutDis- LTR- 10BitTagReq- OBFF Disabled,
                 AtomicOpsCtl: ReqEn-
            LnkSta2: Current De-emphasis Level: -3.5dB, EqualizationComplete- EqualizationPhase1-
                 EqualizationPhase2- EqualizationPhase3- LinkEqualizationRequest-
                 Retimer- 2Retimers- CrosslinkRes: unsupported
        Capabilities: [a0] MSI: Enable+ Count=1/1 Maskable- 64bit+
            Address: 00000000fee00000  Data: 0000
        Capabilities: [c0] MSI-X: Enable- Count=1 Masked-
            Vector table: BAR=0 offset=000fe000
            PBA: BAR=0 offset=000ff000
        Capabilities: [100 v1] Vendor Specific Information: ID=0001 Rev=1 Len=010 <?>
        Capabilities: [2a0 v1] Access Control Services
            ACSCap: SrcValid- TransBlk- ReqRedir- CmpltRedir- UpstreamFwd- EgressCtrl- DirectTrans-
            ACSCtl: SrcValid- TransBlk- ReqRedir- CmpltRedir- UpstreamFwd- EgressCtrl- DirectTrans-
        Kernel driver in use: xhci_hcd

#### [lsusb]

`root `[`#`]`lsusb -v -t`

    /:  Bus 10.Port 1: Dev 1, Class=root_hub, Driver=xhci_hcd/1p, 10000M
        ID 1d6b:0003 Linux Foundation 3.0 root hub
    /:  Bus 09.Port 1: Dev 1, Class=root_hub, Driver=xhci_hcd/1p, 480M
        ID 1d6b:0002 Linux Foundation 2.0 root hub
    /:  Bus 08.Port 1: Dev 1, Class=root_hub, Driver=xhci_hcd/1p, 10000M
        ID 1d6b:0003 Linux Foundation 3.0 root hub
    /:  Bus 07.Port 1: Dev 1, Class=root_hub, Driver=xhci_hcd/1p, 480M
        ID 1d6b:0002 Linux Foundation 2.0 root hub
    /:  Bus 06.Port 1: Dev 1, Class=root_hub, Driver=xhci_hcd/0p, 5000M
        ID 1d6b:0003 Linux Foundation 3.0 root hub
    /:  Bus 05.Port 1: Dev 1, Class=root_hub, Driver=xhci_hcd/1p, 480M
        ID 1d6b:0002 Linux Foundation 2.0 root hub
        |__ Port 1: Dev 2, If 0, Class=Wireless, Driver=btusb, 480M
            ID 13d3:3568 IMC Networks
        |__ Port 1: Dev 2, If 1, Class=Wireless, Driver=btusb, 480M
            ID 13d3:3568 IMC Networks
        |__ Port 1: Dev 2, If 2, Class=Wireless, Driver=, 480M
            ID 13d3:3568 IMC Networks
    /:  Bus 04.Port 1: Dev 1, Class=root_hub, Driver=xhci_hcd/2p, 10000M
        ID 1d6b:0003 Linux Foundation 3.0 root hub
    /:  Bus 03.Port 1: Dev 1, Class=root_hub, Driver=xhci_hcd/3p, 480M
        ID 1d6b:0002 Linux Foundation 2.0 root hub
        |__ Port 3: Dev 2, If 0, Class=Video, Driver=uvcvideo, 480M
            ID 13d3:56eb IMC Networks
        |__ Port 3: Dev 2, If 1, Class=Video, Driver=uvcvideo, 480M
            ID 13d3:56eb IMC Networks
        |__ Port 3: Dev 2, If 2, Class=Video, Driver=uvcvideo, 480M
            ID 13d3:56eb IMC Networks
        |__ Port 3: Dev 2, If 3, Class=Video, Driver=uvcvideo, 480M
            ID 13d3:56eb IMC Networks
        |__ Port 3: Dev 2, If 4, Class=Application Specific Interface, Driver=, 480M
            ID 13d3:56eb IMC Networks
    /:  Bus 02.Port 1: Dev 1, Class=root_hub, Driver=xhci_hcd/2p, 10000M
        ID 1d6b:0003 Linux Foundation 3.0 root hub
    /:  Bus 01.Port 1: Dev 1, Class=root_hub, Driver=xhci_hcd/4p, 480M
        ID 1d6b:0002 Linux Foundation 2.0 root hub
        |__ Port 3: Dev 2, If 0, Class=Human Interface Device, Driver=usbhid, 12M
            ID 0b05:19b6 ASUSTek Computer, Inc.
        |__ Port 3: Dev 2, If 1, Class=Human Interface Device, Driver=usbhid, 12M
            ID 0b05:19b6 ASUSTek Computer, Inc.
        |__ Port 3: Dev 2, If 2, Class=Human Interface Device, Driver=usbhid, 12M
            ID 0b05:19b6 ASUSTek Computer, Inc.
        |__ Port 3: Dev 2, If 3, Class=Human Interface Device, Driver=usbhid, 12M
            ID 0b05:19b6 ASUSTek Computer, Inc.

#### [Ports]

The laptop has 2 USB-C ports. The one on the left outputs from the iGPU and the one on the right outputs from the dGPU. The one on the left can also be used to power the laptop. The HDMI port on the left outputs from the dGPU.^[\[31\]](#cite_note-31)^ There are 2 USB-A 3.2 ports and a MicroSD card slot on the right^[\[32\]](#cite_note-32)^ plus a 3.5 mm audio jack on the left.

### [Accessories]

  ------------------- ---------------------------------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ --------- ------------------ ---------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Device              Make/model                                                                                     Vendor ID / Product ID                                                                                                                                                               Status    Kernel driver(s)   Kernel version   Notes
  RAM                 Vengeance DDR5 SODIMM 32GB (1x32GB) DDR5 4800 (PC5-38400) C40 1.1 V^[\[33\]](#cite_note-33)^   CMSX32GX5M1A4800C40                                                                                                                                                                  Works     N/A                6.14.2
  USB-C Cable         Anker 765 (140W Nylon)^[\[34\]](#cite_note-34)^                                                N/A                                                                                                                                                                                  Works     N/A                6.14.2
  USB-C Hub           Anker 565^[\[35\]](#cite_note-35)^                                                             0b95:1790^[\[36\]](#cite_note-36)^, 2537:1081^[\[37\]](#cite_note-37)^, 2109:0822^[\[38\]](#cite_note-38)^, 14cd:8601^[\[39\]](#cite_note-39)^, 2109:2822^[\[40\]](#cite_note-40)^   Tested    sdhci              6.14.2           Trying to output to 2 monitors simultaneously may not work. 1 monitor should work fine, including when the laptop\'s HDMI port is connected to an external monitor.
  USB Power Adaptor   Anker 737 Charger (GaNPrime 120W)^[\[41\]](#cite_note-41)^                                     N/A                                                                                                                                                                                  Works     N/A                6.14.2           Works well with the cable listed above for USB-C power delivery.
  ------------------- ---------------------------------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ --------- ------------------ ---------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------

## [Installation]

### [00cpu-flags]

[FILE] **`/etc/portage/package.use/00cpu-flags`**

    */* CPU_FLAGS_X86: aes avx avx2 f16c fma3 mmx mmxext pclmul popcnt rdrand sha sse sse2 sse3 sse4_1 sse4_2 sse4a ssse3

### [make.conf]

[FILE] **`/etc/portage/make.conf`**

    # Go
    GOAMD64="v3"
    # Grub
    GRUB_PLATFORMS="efi-64"

### [package.license]

[FILE] **`/etc/portage/package.license`**

    sys-kernel/linux-firmware @BINARY-REDISTRIBUTABLE

### [package.use]

`radeon` does not need to be globally added to `VIDEO_CARDS`, only to [[[x11-libs/libdrm]](https://packages.gentoo.org/packages/x11-libs/libdrm)[]] if that is installed.

[FILE] **`/etc/portage/package.use/package.use`**

    */* INPUT_DEVICES:        -* libinput synaptics
    */* VIDEO_CARDS:          -* amdgpu radeonsi

    media-libs/mesa           gles2 vaapi vdpau vulkan wayland
    media-video/libva-utils   vainfo
    sys-apps/fwupd            -dell nvme spi synaptics tpm uefi
    x11-libs/libdrm           video_cards_radeon

### [Kernel]

** Important**\
Kernel 6.7.5 does not boot, hanging between the ALSA device list and Freeing unused kernel image (initmem) memory steps.

** Important**\
With kernels 6.10.4-6.10.8, connecting an external display freezes the system. 6.10.10+ is okay.

** Important**\
With kernels 6.10.11-6.12.8, about 1/4 of the time, the system freezes upon boot. 6.12.11 seems to have corrected the issue.

** Note**\
For *AMD_MEM_ENCRYPT* to become visible, set *EFI_STUB*=y.

** Note**\
Setting *KVM*=y can cause issues with VirtualBox in 6.12+.^[\[42\]](#cite_note-42)[\[43\]](#cite_note-43)^

[KERNEL] **make menuconfig**

    [*] 64-bit kernel
        Processor type and features  --->
            [*] AMD ACPI2Platform devices support
                Processor family (AMD-Native optimizations autodetected by the compiler)
            [*] Supported processor vendors  --->
                    [ ] Support Intel processors
                    [*] Support AMD processors
            [*] Old AMD GART IOMMU support
            [*] Machine Check / overheating reporting
            [ ]   Intel MCE features
            [*]   AMD MCE features
                Performance monitoring  --->
                    <*> Intel/AMD rapl performance events
                    <*> AMD Processor Power Reporting Mechanism
                    <*> AMD Uncore performance events
                    [*] AMD Zen3 Branch Sampling support
            [*] AMD Secure Memory Encryption (SME) support
            [ ]   Activate AMD Secure Memory Encryption (SME) by default
    [*] Mitigations for CPU vulnerabilities  --->
            [*] Remove the kernel mapping in user mode
            [*] Avoid speculative indirect branches in kernel
            [*]   Enable return-thunks
            [*]     Enable UNRET on kernel entry
            [*] Enable IBPB on kernel entry
            [*] Mitigate speculative RAS overflow on AMD
            [*] Mitigate Straight-Line-Speculation
            [*] Mitigate RETBleed hardware bug
            [*] Mitigate SPECTRE V1 hardware bug
            [*] Mitigate SPECTRE V2 hardware bug
            [*] Mitigate Speculative Store Bypass (SSB) hardware bug
        Power management and ACPI options --->
                CPU Frequency scaling  --->
                    [*] CPU Frequency scaling --->
                        Default CPUFreq governor (performance)  --->
                    -*- 'performance' governor
                    <*> 'powersave' governor
                    [*] AMD Processor P-State driver
                    (3)   AMD Processor P-State default mode
                    <M> selftest for AMD Processor P-State driver
                    < >   ACPI Processor P-States driver
    [*] Virtualization
            <M> KVM for AMD processors support
            [*]   AMD Secure Encrypted Virtualization (SEV) support
    -*- Networking support  --->
            <*> Bluetooth subsystem support  --->
                    [*] Bluetooth Classic (BR/EDR) features
                    <*>   RFCOMM protocol support
                    [*]   Bluetooth Low Energy (LE) features
                        Bluetooth device drivers  --->
                            <*> HCI USB driver
                            [*]   MediaTek protocol support
                            <*> MediaTek HCI SDIO driver
                            <*> MediaTek HCI UART driver
            -*- Wireless  --->
                    <*> cfg80211 - wireless configuration API
                    <*> Generic IEEE 802.11 Networking Stack (mac80211)
        Device Drivers  --->
            [*] PCI support  --->
                    [*] PCI Express Port Bus support
                    [*] PCI Express ASPM control
                NVME Support  --->
                    <*> NVM Express block device
                SCSI device support  --->
                    <*> SCSI disk support
            [*] Network device support  --->
                    [*] Ethernet driver support  --->
                            [*] AMD devices
                    [*] Wireless LAN  --->
                            [*] MediaTek devices
                            <M>   MediaTek MT7615E and MT7663E (PCIe) support
                            <*>   MediaTek MT7921E (PCIe) support
                            <*>   MediaTek MT7921S (SDIO) support
                            <*>   MediaTek MT7921U (USB) support
                    [*] Realtek devices
                    <M>   Realtek 8180/8185/8187SE PCI support
                Character devices  --->
                    -*- Hardware Random Number Generator Core support  --->
                            <*> AMD HW Random Number Generator support
                    -*- TPM Hardware Support  --->
                            [ ] TPM HW Random Number Generator support
            [*] SPI support  --->
                    <*> AMD SPI controller
            -*- Pin controllers  --->
                    [*] AMD GPIO pin control
            -*- Hardware Monitoring support  --->
                    <*> AMD Family 10h+ temperature sensor
                    <*> ASUS ATK0110
                    <*> ASUS WMI X370/X470/B450/X399
                    <*> ASUS EC Sensors
            [*] Watchdog Timer Support  --->
                    <*> AMD/ATI SP5100 TCO Timer/Watchdog
                Graphics support  --->
                    [*] Laptop Hybrid Graphics - GPU switching support
                    <*> Direct Rendering Manager (XFree86 4.1.0 and higher DRI support)  --->
                    < > ATI Radeon
                    <*> AMD GPU
                    [*]   Enable amdgpu support for SI parts
                    [*]   Enable amdgpu support for CIK parts
                    -*-   Always enable userptr write support
                    [ ]   Force the compiler to throw an error instead of a warning when compiling
                          ACP (Audio CoProcessor) Configuration  --->
                              [*] Enable AMD Audio CoProcessor IP support
                          Display Engine Configuration  --->
                              [*] AMD DC - Enable new display engine
                              [*] AMD DC support for Southern Islands ASICs
                              [ ] Enable kgdb break in DC
                              [*] Enable secure display support
                    [*] HSA kernel driver for AMD GPU devices
                    [*]   Enable HMM-based shared virtual memory manager
                    < > Nouveau (NVIDIA) cards
                    < > Intel 8xx/9xx/G3x/G4x/HD Graphics
                    <*> Simple framebuffer driver
                        Frame buffer Devices  --->
                            <*> Support for frame buffer devices  --->
                                    <*> VGA 16-color graphics support
                                    < > Userspace VESA VGA graphics support
                                    [ ] VESA VGA graphics support
                                    [*] EFI-based Framebuffer Support
                        Console display driver support  --->
                            [*] Framebuffer Console support
                            [ ]   Enable legacy fbcon hardware acceleration code
            <*> Sound card support  --->
                    <*> Advanced Linux Sound Architecture  --->
                            <*> ALSA for SoC audio support  --->
                                    <*> AMD Audio Coprocessor support
                                    <*> AMD Audio Coprocessor-v6.x Yellow Carp support
                                    <*>   AMD YC support for DMIC
                                    -*- AMD ACP configuration selection
                                    <*> AMD Audio ACP Common support
                                    <*> AMD Audio Coprocessor-v6.2 RPL support
                                    <*> support for AMD platforms with ACP version >= 6.3
            [*] HID bus support  --->
                    -*- HID bus core support
                    <*>   Generic HID driver
                          Special HID drivers  --->
                              <*> Asus
                        AMD SFH HID Support  --->
                            <*> AMD Sensor Fusion Hub
            [*] USB support  --->
                    <*> xHCI HCD (USB 3.0) support
                    <*> EHCI HCD (USB 2.0) support
                    <*> USB Mass Storage support
                    <*> USB Type-C Support  --->
                            <*> USB Type-C Port Controller Manager
                            <*> Type-C Port Controller Interface driver
                            <*> USB Type-C Connector System Software Interface driver
            <*> MMC/SD/SDIO card support  --->
                    <*> Secure Digital Host Controller Interface support
                    <*> MediaTek SD/MMC Card Interface support
            -*- X86 Platform Specific Device Drivers  --->
                    <M> WMI support for MXM Laptop Graphics
                    <*> AMD Platform Management Framework
                    <*> AMD SoC PMC driver
                    <*> Asus Laptop Extras
                    <*> Asus Wireless Radio Control Driver
                    <*> ASUS WMI Driver
                    <*>   Asus Notebook WMI Driver
            [*] IOMMU Hardware Support  --->
                    [*] AMD IOMMU support
            <*> Unified support for USB4 and Thunderbolt  --->
            <*> Trusted Execution Environment support  --->
                    <*> AMD-TEE
        Security options  --->
            <*> TRUSTED KEYS
            [*]   TPM-based trusted keys
            [*]   TEE-based trusted keys
    -*- Cryptographic API  --->
                Crypto core or helper  --->
                    <*> Parallel crypto engine
                Accelerated Cryptographic Algorithms for CPU (x86)  --->
                    <*> Ciphers: AES, modes: ECB, CBC, CTS, CTR, XTR, XTS, GCM (AES-NI)
                     CRC32c (SSE4.2/PCLMULQDQ)
            [*] Hardware crypto devices  --->
                    [*] Support for AMD Secure Processor
                    <*>   Secure Processor device driver
                    [*]     Cryptographic Coprocessor device
                    <*>       Encryption and hashing offload support
                    [*]     Platform Security Processor (PSP) device

### [Firmware]

For wifi, bluetooth, the two GPUs, microcode updates, and to eliminate the boot error messages about not finding `regulatory.db`, add the following firmware files:

[FILE] **`/usr/src/linux/.config`**

    CONFIG_EXTRA_FIRMWARE="regulatory.db regulatory.db.p7s mediatek/BT_RAM_CODE_MT7922_1_1_hdr.bin mediatek/WIFI_MT7922_patch_mcu_1_1_hdr.bin mediatek/WIFI_RAM_CODE_MT7922_1.bin amd/amd_sev_fam17h_model0xh.sbin amd/amd_sev_fam17h_model3xh.sbin amd/amd_sev_fam19h_model0xh.sbin amd-ucode/microcode_amd_fam17h.bin amd-ucode/microcode_amd_fam19h.bin amdgpu/yellow_carp_asd.bin amdgpu/yellow_carp_ce.bin amdgpu/yellow_carp_dmcub.bin amdgpu/yellow_carp_me.bin amdgpu/yellow_carp_mec2.bin amdgpu/yellow_carp_mec.bin amdgpu/yellow_carp_pfp.bin amdgpu/yellow_carp_rlc.bin amdgpu/yellow_carp_sdma.bin amdgpu/yellow_carp_ta.bin amdgpu/yellow_carp_toc.bin amdgpu/yellow_carp_vcn.bin amdgpu/dimgrey_cavefish_ce.bin amdgpu/dimgrey_cavefish_dmcub.bin amdgpu/dimgrey_cavefish_me.bin amdgpu/dimgrey_cavefish_mec2.bin amdgpu/dimgrey_cavefish_mec.bin amdgpu/dimgrey_cavefish_pfp.bin amdgpu/dimgrey_cavefish_rlc.bin amdgpu/dimgrey_cavefish_sdma.bin amdgpu/dimgrey_cavefish_smc.bin amdgpu/dimgrey_cavefish_sos.bin amdgpu/dimgrey_cavefish_ta.bin amdgpu/dimgrey_cavefish_vcn.bin"
    CONFIG_EXTRA_FIRMWARE_DIR="/lib/firmware"

In order for `regulatory.db` to be present, run:

`root `[`#`]`emerge --ask net-wireless/wireless-regdb`

### [Emerge]

#### [Firmware]

`root `[`#`]`emerge --ask sys-apps/fwupd sys-kernel/linux-firmware`

#### [][Graphics/Mesa/Vulkan]

`root `[`#`]`emerge --ask dev-util/vulkan-tools media-video/libva-utils media-libs/mesa media-libs/vulkan-loader media-libs/vulkan-layers x11-apps/mesa-progs x11-drivers/xf86-video-amdgpu`

#### [Power]

`root `[`#`]`emerge --ask sys-power/tlp`

### [initramfs]

If using [genkernel](https://wiki.gentoo.org/wiki/Genkernel "Genkernel") to make an [initramfs](https://wiki.gentoo.org/wiki/Initramfs "Initramfs"), pass the option `--no-ramdisk-modules`. They are not needed for the system to boot successfully, and with the AMD binary blobs for the GPUs, the initramfs file will be over 200 MB otherwise. Pass other parameters as desired.

`root `[`#`]`genkernel --install --kernel-config=/usr/src/linux/.config --no-ramdisk-modules initramfs`

## [Configuration]

### [AMD P-State]

The AMD P-State driver should be used with this laptop.

#### [][Kernels 6.1.\* and earlier]

These kernels do not have the EPP modes built-in:

[FILE] **`/etc/default/grub`GRUB config**

    GRUB_CMDLINE_LINUX_DEFAULT="amd-pstate=passive acpi_osi=Linux"

The parameter `acpi_osi=Linux` has no functional impact, but will change this boot message:

`kernel: ACPI: [Firmware Bug]: BIOS _OSI(Linux) query ignored`

to this:

`kernel: ACPI: [Firmware Bug]: BIOS _OSI(Linux) query honored via cmdline`.

Refer to the power management guide\'s [section](https://wiki.gentoo.org/wiki/Power_management/Processor#AMD_P-State "Power management/Processor") on AMD P-State for more details.

#### [Kernels 6.5.5 and later]

The variable `amd-pstate=passive` can be removed from the GRUB config, as the value can now be set via *CONFIG_X86_AMD_PSTATE_DEFAULT_MODE* (shown in the kernel config above).^[\[44\]](#cite_note-44)^

### [asusctl]

#### [OpenRC]

Currently only [systemd](https://wiki.gentoo.org/wiki/Systemd "Systemd") is supported upstream.^[\[45\]](#cite_note-45)[\[46\]](#cite_note-46)^ For those interested in using asusctl with [OpenRC](https://wiki.gentoo.org/wiki/OpenRC "OpenRC"), [this](https://gitlab.com/asus-linux/asusctl/-/issues/59) documents some previous efforts.

### [BIOS]

The latest BIOS^[\[47\]](#cite_note-47)^ version as of June 2024 is 319 and can be safely upgraded to.

** Important**\
It is generally recommended to watch forums for user reports prior to updating as previous updates have caused issues (notably, 313^[\[48\]](#cite_note-48)^).

### [Firmware updates]

Use [[[sys-apps/fwupd]](https://packages.gentoo.org/packages/sys-apps/fwupd)[]] and refer to [its page](https://wiki.gentoo.org/wiki/Fwupd "Fwupd") for more details. So far, only UEFI revocation database^[\[49\]](#cite_note-49)^ updates have been available.

### [Hyprland]

The configuration for the built-in laptop display is:

[FILE] **`~/.config/hypr/hyprland.conf`Monitor**

    monitor=eDP-2,2560x1600@120,auto,1

`/dev/dri/card0` is the 6700S/6800S and `/dev/dri/card1` is the 680M. Because the iGPU is tied to the display controller, to make Hyprland run on the dGPU, one must write

** Note**\
The previous `WLR_DRM_DEVICES` environmental variable has been replaced by `AQ_DRM_DEVICES`^[\[50\]](#cite_note-50)^.

[FILE] **`~/.config/hypr/hyprland.conf`To use dGPU**

    env = AQ_DRM_DEVICES,/dev/dri/card0:/dev/dri/card1

to set the dGPU as primary and the iGPU as secondary. If the `:/dev/dri/card1` part is omitted, Hyprland will not start because there is no display. For the same reason, trying to use `env = DRI_PRIME,1` will also not work.

To use the 680M and extend battery life, one would reverse the above:

[FILE] **`~/.config/hypr/hyprland.conf`To use iGPU**

    env = AQ_DRM_DEVICES,/dev/dri/card1:/dev/dri/card0

#### [Function keys and hot keys]

Asus has programmed several of the Fn key combinations to perform unique tasks, as shown by the pictograms on the keys. For example, Fn + F6 is meant to open a screenshot utility. The Windows-only applications which would usually instantiate this functionality like MyASUS or Armoury Crate are entirely unnecessary for replication of similar behaviour on Linux, though the means of implementation will vary with one\'s [desktop environment](https://wiki.gentoo.org/wiki/Desktop_environment "Desktop environment") or [window manager](https://wiki.gentoo.org/wiki/Window_manager "Window manager").

Depending on whether the current environment is X11 or Wayland, either xev^[\[51\]](#cite_note-51)^ (available at [[[x11-apps/xev]](https://packages.gentoo.org/packages/x11-apps/xev)[]]) or wev^[\[52\]](#cite_note-52)^ (available in [GURU](https://gpo.zugaina.org/gui-apps/wev)) can be used to reveal the keysym^[\[53\]](#cite_note-53)[\[54\]](#cite_note-54)^ input which occurs after pressing a physical key. Usually there is a clear 1-1 correspondence, but for this laptop, there are some non-obvious ones:

  -------------------- ----------------------------- --------------- --------------------------------------------------------------------------------------------------------------------------------------------------------------
  Physical key input   Keysym input                  Keycode input   Notes
  `Fn` + `Meta`        none                          none            Meta is the Windows key, or `SUPER` in a Hyprland config. This key combo disables or enables the meta key. No keysym input occurs in either case.
  `Fn` + `F4`          `XF86Launch3`                 202             Intended to toggle the \"Aura lighting effect\"
  `Fn` + `F5`          `XF86Launch4`                 203             Meant for switching between fan modes
  `Fn` + `F6`          `Super_L` + `Shift_L` + `S`   125 + 42 + 31   Super_L is the left CTRL key.
  `Fn` + `F9`          `Super_L` + `p`               125 + 25        Meant for switching between \"display modes\" when external displays are connected.
  `Fn` + `F10`         `XF86TouchpadToggle`          191             Enable or disable the touchpad
  `Fn` + `Super_L`     `Return` + `Menu`             127             This key combo is equivalent to right-clicking.
  `M4`                 `XF86Launch1`                 148             Meant to open the Armoury Crate application.
  -------------------- ----------------------------- --------------- --------------------------------------------------------------------------------------------------------------------------------------------------------------

The command [showkey]^[\[55\]](#cite_note-55)^ can be used to get the keycodes. The user manual lists what Asus intended for these keys on page 43.

#### [Keyboard brightness]

Install [app-misc/brightnessctl](https://gpo.zugaina.org/app-misc/brightnessctl) from [GURU](https://wiki.gentoo.org/wiki/GURU "GURU"). Then add the following lines:

[FILE] **`~/.config/hypr/hyprland.conf`Keyboard brightness keybinds**

    bind=, XF86KbdBrightnessUp, exec, brightnessctl --device='asus::kbd_backlight' set +1
    bind=, XF86KbdBrightnessDown, exec, brightnessctl --device='asus::kbd_backlight' set 1-

#### [Screenshots]

Install [[[gui-apps/grim]](https://packages.gentoo.org/packages/gui-apps/grim)[]]. Then add the following line to use the `Fn` + `F6` combination mentioned above:

[FILE] **`~/.config/hypr/hyprland.conf`Screenshots with Asus F6 key**

    bind= Super_L Shift_L, S, exec, grim -g "$(slurp && sleep 0.5)"

### [KDE Wayland]

** Note**\
The variable `WLR_DRM_DEVICES` doesn\'t work to set the dGPU as primary under KDE.

`KWIN_COMPOSE=O2ES`^[\[56\]](#cite_note-56)^ may be necessary to eliminate graphical glitches. Firefox doesn\'t work well with `DRI_PRIME=1` in this case.

### [TLP]

Here are [TLP](https://wiki.gentoo.org/index.php?title=TLP&action=edit&redlink=1 "TLP (page does not exist)")^[\[57\]](#cite_note-57)^ settings that work well for performance on AC, maximizing battery life on battery, and limiting battery charge to 90% to extend battery life. 90% works fine despite the boot warning message about Asus laptops potentially not respecting it. These settings are based on a kernel with the P-State EPP driver (not the 6.1.\* kernels) and TLP ≥ 1.6.0.

[FILE] **`/etc/tlp.conf`**

    TLP_ENABLE=1

    CPU_DRIVER_OPMODE_ON_AC=active
    CPU_DRIVER_OPMODE_ON_BAT=active

    CPU_SCALING_GOVERNOR_ON_AC=powersave
    CPU_SCALING_GOVERNOR_ON_BAT=powersave

    CPU_ENERGY_PERF_POLICY_ON_AC=balance_performance
    CPU_ENERGY_PERF_POLICY_ON_BAT=balance_power

    CPU_BOOST_ON_AC=1
    CPU_BOOST_ON_BAT=0

    PLATFORM_PROFILE_ON_AC=balanced
    PLATFORM_PROFILE_ON_BAT=quiet

    RADEON_DPM_STATE_ON_AC=performance
    RADEON_DPM_STATE_ON_BAT=battery

    RADEON_POWER_PROFILE_ON_AC=default
    RADEON_POWER_PROFILE_ON_BAT=default

    PCIE_ASPM_ON_BAT=powersupersave

    USB_EXCLUDE_PHONE=1

    STOP_CHARGE_THRESH_BAT0=90

## [Troubleshooting]

### [680M freezes]

There is a known issue, perhaps related to DPMS, which may cause the system to freeze in a way that requires forcibly powering it off.^[\[58\]](#cite_note-58)^ Investigation into a final solution is still ongoing. The link contains a long discussion of attempts to fix or reduce the occurrence of the issue for those interested.

** Warning**\
A recent instance of this issue which seemed to occur simultaneously with attempting to put the laptop to sleep caused a root [btrfs](https://wiki.gentoo.org/wiki/Btrfs "Btrfs") file system to become unrecoverable (bad tree block start, open_ctree failed, checksum verify failed, etc.^[\[59\]](#cite_note-59)[\[60\]](#cite_note-60)[\[61\]](#cite_note-61)^) Consider using [ext4](https://wiki.gentoo.org/wiki/Ext4 "Ext4").

### [ccp_crypto: cannot load]

If the message `ccp_crypto: Cannot load: there are no available CCPs` appears in the boot log, it is because *Encryption and hashing offload support* (CRYPTO_DEV_CCP_CRYPTO) was built into the kernel (\[\*\]) rather than set as a module (\[m\]). Set it to module (shown in the kernel config section above), and the message should not appear after rebooting.

### [fTPM RNG stutters]

See the \"Encryption controller\" row in the hardware table for references, and ensure that *TPM HW Random Number Generator support* is disabled as shown in the kernel configuration above.

### [Machine learning]

Despite not being officially supported by [ROCm](https://wiki.gentoo.org/wiki/ROCm "ROCm")^[\[62\]](#cite_note-62)^, the 6700S/6800S can be used with [PyTorch](https://wiki.gentoo.org/index.php?title=PyTorch&action=edit&redlink=1 "PyTorch (page does not exist)") or [Tensorflow](https://wiki.gentoo.org/index.php?title=Tensorflow&action=edit&redlink=1 "Tensorflow (page does not exist)"). Set the environmental variable `HSA_OVERRIDE_GFX_VERSION=10.3.0` to spoof the [gfx1030](//packages.gentoo.org/useflags/amdgpu_targets_gfx1030) group of cards.^[\[63\]](#cite_note-63)^ It can be prepended to terminal commands (e.g. `HSA_OVERRIDE_GFX_VERSION=10.3.0 jupyter-notebook`) or placed in a file like [[/etc/environment](https://wiki.gentoo.org/index.php?title=/etc/environment&action=edit&redlink=1 "/etc/environment (page does not exist)")] or a Hyprland config file:

[FILE] **`/etc/environment`**

    HSA_OVERRIDE_GFX_VERSION=10.3.0

[FILE] **`~/.config/hypr/hyprland.conf`**

    env = HSA_OVERRIDE_GFX_VERSION,10.3.0

A list of currently available `AMDGPU_TARGETS` can be seen on the pages for packages like [[[sci-libs/rocRAND]](https://packages.gentoo.org/packages/sci-libs/rocRAND)[]]. This variable can be set in [[package.use](https://wiki.gentoo.org/wiki//etc/portage/package.use "/etc/portage/package.use")] as follows:

[FILE] **`/etc/portage/package.use/package.use`**

    */* AMDGPU_TARGETS: -* gfx1030 gfx1031 gfx1032 gfx1033 gfx1034 gfx1035

Only gfx1030 and gfx1031 are currently in place. gfx1032 is the 6700S^[\[64\]](#cite_note-64)^ and gfx1035 is the 680M.^[\[65\]](#cite_note-65)^

### [Mesa 23.1 crashes]

Mesa ([[[media-libs/mesa]](https://packages.gentoo.org/packages/media-libs/mesa)[]]) 23.1.3 causes VA-API-related crashes when using the radeonsi driver on this laptop (e.g., when playing YouTube videos on Firefox).^[\[66\]](#cite_note-66)^ 23.0.3-r1 and ≥ 23.1.5 do not have this issue.

### [rocminfo]

Version 5.4.3 of [[[dev-util/rocminfo]](https://packages.gentoo.org/packages/dev-util/rocminfo)[]] works as expected. Newer 5.\* versions gave this error:

`user `[`$`]`rocminfo`

```
ROCk module is NOT loaded, possibly no GPU devices
```

6.\* versions work fine.

### [Suspend]

It used to be that this laptop could be put to sleep and woken back up, but the fans would not spin after waking and a reboot was needed to get them back. This has happily been recently fixed^[\[67\]](#cite_note-67)[\[68\]](#cite_note-68)[\[69\]](#cite_note-69)^ and is no longer an issue as of the 6.1.41 kernel. The following command can be used to suspend from the terminal:

`root `[`#`]`systemctl suspend`

Running it as a normal user will result in a reboot.

## [Notes]

The \"Header and Data\" data under \"Handle 0x0009, DMI type 44\" was removed, along with serial numbers and OEM Strings.

### [Benchmarks]

Some benchmarks of the 6700S dGPU are available [here](//www.notebookcheck.net/AMD-Radeon-RX-6700S-GPU-Benchmarks-and-Specs.590203.0.html).

#### [6900HS]

Some generic [6900HS](https://cpu.userbenchmark.com/SpeedTest/1796538/AMD-Ryzen-9-6900HS-with-Radeon-Graphics) [benchmarks](https://www.notebookcheck.net/AMD-Ryzen-9-6900HS-Processor-Benchmarks-and-Specs.591451.0.html) are available.

##### [Compiling]

** Note**\
This is with \--jobs=14 and \--load-average=9 in [make.conf](https://wiki.gentoo.org/wiki//etc/portage/make.conf#EMERGE_DEFAULT_OPTS "/etc/portage/make.conf").

Firefox with `jumbo-build`, `lto`, and `pgo`.

`root `[`#`]`qlop -a firefox`

www-client/firefox: 1:07:46 average for 26 merges.

##### [Cryptography]

`root `[`#`]`cryptsetup benchmark`

    # Tests are approximate using memory only (no storage IO).
    PBKDF2-sha1      2713003 iterations per second for 256-bit key
    PBKDF2-sha256    5356710 iterations per second for 256-bit key
    PBKDF2-sha512    2330168 iterations per second for 256-bit key
    PBKDF2-ripemd160  907072 iterations per second for 256-bit key
    PBKDF2-whirlpool  834853 iterations per second for 256-bit key
    argon2i      10 iterations, 1048576 memory, 4 parallel threads (CPUs) for 256-bit key (requested 2000 ms time)
    argon2id     10 iterations, 1048576 memory, 4 parallel threads (CPUs) for 256-bit key (requested 2000 ms time)
    #     Algorithm |       Key |      Encryption |      Decryption
            aes-cbc        128b      1460.5 MiB/s      5726.7 MiB/s
        serpent-cbc        128b       139.0 MiB/s      1008.5 MiB/s
        twofish-cbc        128b       233.9 MiB/s       255.0 MiB/s
            aes-cbc        256b      1104.3 MiB/s      4781.2 MiB/s
        serpent-cbc        256b       139.2 MiB/s      1004.6 MiB/s
        twofish-cbc        256b       233.8 MiB/s       255.2 MiB/s
            aes-xts        256b      4688.8 MiB/s      4723.3 MiB/s
        serpent-xts        256b       901.3 MiB/s       894.6 MiB/s
        twofish-xts        256b       481.9 MiB/s       494.3 MiB/s
            aes-xts        512b      4022.1 MiB/s      3989.7 MiB/s
        serpent-xts        512b       909.4 MiB/s       894.3 MiB/s
        twofish-xts        512b       491.7 MiB/s       493.8 MiB/s

### [dmidecode]

`root `[`#`]`dmidecode`

    # dmidecode 3.5
    Getting SMBIOS data from sysfs.
    SMBIOS 3.4.0 present.
    Table at 0xB9189000.

    Handle 0x0000, DMI type 0, 26 bytes
    BIOS Information
        Vendor: American Megatrends International, LLC.
        Version: GA402RJ.319
        Release Date: 06/06/2023
        Address: 0xF0000
        Runtime Size: 64 kB
        ROM Size: 32 MB
        Characteristics:
            PCI is supported
            BIOS is upgradeable
            BIOS shadowing is allowed
            Boot from CD is supported
            Selectable boot is supported
            BIOS ROM is socketed
            EDD is supported
            ACPI is supported
            Smart battery is supported
            BIOS boot specification is supported
            Targeted content distribution is supported
            UEFI is supported
        BIOS Revision: 5.24
        Firmware Revision: 3.18

    Handle 0x0001, DMI type 1, 27 bytes
    System Information
        Manufacturer: ASUSTeK COMPUTER INC.
        Product Name: ROG Zephyrus G14 GA402RJ_GA402RJ
        Version: 1.0
        Serial Number:
        UUID:
        Wake-up Type: Power Switch
        SKU Number:
        Family: ROG Zephyrus G14

    Handle 0x0002, DMI type 2, 15 bytes
    Base Board Information
        Manufacturer: ASUSTeK COMPUTER INC.
        Product Name: GA402RJ
        Version: 1.0
        Serial Number:
        Asset Tag:
        Features:
            Board is a hosting board
            Board is replaceable
        Location In Chassis: MIDDLE
        Chassis Handle: 0x0003
        Type: Motherboard
        Contained Object Handles: 0

    Handle 0x0003, DMI type 3, 22 bytes
    Chassis Information
        Manufacturer: ASUSTeK COMPUTER INC.
        Type: Notebook
        Lock: Not Present
        Version: 1.0
        Serial Number:
        Asset Tag: No Asset Tag
        Boot-up State: Safe
        Power Supply State: Safe
        Thermal State: Safe
        Security Status: None
        OEM Information: 0x00000000
        Height: Unspecified
        Number Of Power Cords: 1
        Contained Elements: 0
        SKU Number: NA

    Handle 0x0007, DMI type 13, 22 bytes
    BIOS Language Information
        Language Description Format: Long
        Installable Languages: 1
            en|US|iso8859-1
        Currently Installed Language: en|US|iso8859-1

    Handle 0x0008, DMI type 32, 11 bytes
    System Boot Information
        Status: No errors detected

    Handle 0x0009, DMI type 44, 9 bytes
    Unknown Type
        Header and Data:

    Handle 0x000A, DMI type 43, 31 bytes
    TPM Device
        Vendor ID: AMD
        Specification Version: 2.0
        Firmware Revision: 3.87
        Description: AMD
        Characteristics:
            Family configurable via platform software support
        OEM-specific Information: 0x00000000

    Handle 0x000B, DMI type 7, 27 bytes
    Cache Information
        Socket Designation: L1 - Cache
        Configuration: Enabled, Not Socketed, Level 1
        Operational Mode: Write Back
        Location: Internal
        Installed Size: 512 kB
        Maximum Size: 512 kB
        Supported SRAM Types:
            Pipeline Burst
        Installed SRAM Type: Pipeline Burst
        Speed: 1 ns
        Error Correction Type: Multi-bit ECC
        System Type: Unified
        Associativity: 8-way Set-associative

    Handle 0x000C, DMI type 7, 27 bytes
    Cache Information
        Socket Designation: L2 - Cache
        Configuration: Enabled, Not Socketed, Level 2
        Operational Mode: Write Back
        Location: Internal
        Installed Size: 4 MB
        Maximum Size: 4 MB
        Supported SRAM Types:
            Pipeline Burst
        Installed SRAM Type: Pipeline Burst
        Speed: 1 ns
        Error Correction Type: Multi-bit ECC
        System Type: Unified
        Associativity: 8-way Set-associative

    Handle 0x000D, DMI type 7, 27 bytes
    Cache Information
        Socket Designation: L3 - Cache
        Configuration: Enabled, Not Socketed, Level 3
        Operational Mode: Write Back
        Location: Internal
        Installed Size: 16 MB
        Maximum Size: 16 MB
        Supported SRAM Types:
            Pipeline Burst
        Installed SRAM Type: Pipeline Burst
        Speed: 1 ns
        Error Correction Type: Multi-bit ECC
        System Type: Unified
        Associativity: 16-way Set-associative

    Handle 0x000E, DMI type 4, 48 bytes
    Processor Information
        Socket Designation: FP7
        Type: Central Processor
        Family: Zen
        Manufacturer: Advanced Micro Devices, Inc.
        ID: 41 0F A4 00 FF FB 8B 17
        Signature: Family 25, Model 68, Stepping 1
        Flags:
            FPU (Floating-point unit on-chip)
            VME (Virtual mode extension)
            DE (Debugging extension)
            PSE (Page size extension)
            TSC (Time stamp counter)
            MSR (Model specific registers)
            PAE (Physical address extension)
            MCE (Machine check exception)
            CX8 (CMPXCHG8 instruction supported)
            APIC (On-chip APIC hardware supported)
            SEP (Fast system call)
            MTRR (Memory type range registers)
            PGE (Page global enable)
            MCA (Machine check architecture)
            CMOV (Conditional move instruction supported)
            PAT (Page attribute table)
            PSE-36 (36-bit page size extension)
            CLFSH (CLFLUSH instruction supported)
            MMX (MMX technology supported)
            FXSR (FXSAVE and FXSTOR instructions supported)
            SSE (Streaming SIMD extensions)
            SSE2 (Streaming SIMD extensions 2)
            HTT (Multi-threading)
        Version: AMD Ryzen 9 6900HS with Radeon Graphics
        Voltage: 1.2 V
        External Clock: 100 MHz
        Max Speed: 4925 MHz
        Current Speed: 3300 MHz
        Status: Populated, Enabled
        Upgrade: None
        L1 Cache Handle: 0x000B
        L2 Cache Handle: 0x000C
        L3 Cache Handle: 0x000D
        Serial Number: Unknown
        Asset Tag: Unknown
        Part Number: Unknown
        Core Count: 8
        Core Enabled: 8
        Thread Count: 16
        Characteristics:
            64-bit capable
            Multi-Core
            Hardware Thread
            Execute Protection
            Enhanced Virtualization
            Power/Performance Control

    Handle 0x000F, DMI type 18, 23 bytes
    32-bit Memory Error Information
        Type: OK
        Granularity: Unknown
        Operation: Unknown
        Vendor Syndrome: Unknown
        Memory Array Address: Unknown
        Device Address: Unknown
        Resolution: Unknown

    Handle 0x0010, DMI type 16, 23 bytes
    Physical Memory Array
        Location: System Board Or Motherboard
        Use: System Memory
        Error Correction Type: None
        Maximum Capacity: 64 GB
        Error Information Handle: 0x000F
        Number Of Devices: 2

    Handle 0x0011, DMI type 19, 31 bytes
    Memory Array Mapped Address
        Starting Address: 0x00000000000
        Ending Address: 0x009FFFFFFFF
        Range Size: 40 GB
        Physical Array Handle: 0x0010
        Partition Width: 2

    Handle 0x0012, DMI type 18, 23 bytes
    32-bit Memory Error Information
        Type: OK
        Granularity: Unknown
        Operation: Unknown
        Vendor Syndrome: Unknown
        Memory Array Address: Unknown
        Device Address: Unknown
        Resolution: Unknown

    Handle 0x0013, DMI type 17, 92 bytes
    Memory Device
        Array Handle: 0x0010
        Error Information Handle: 0x0012
        Total Width: 64 bits
        Data Width: 64 bits
        Size: 8 GB
        Form Factor: SODIMM
        Set: None
        Locator: DIMM 0
        Bank Locator: P0 CHANNEL A
        Type: DDR5
        Type Detail: Synchronous Unbuffered (Unregistered)
        Speed: 4800 MT/s
        Manufacturer: Samsung
        Serial Number: 00000000
        Asset Tag: Not Specified
        Part Number: M425R1GB4BB0-CQKOD
        Rank: 1
        Configured Memory Speed: 4800 MT/s
        Minimum Voltage: 1.1 V
        Maximum Voltage: 1.1 V
        Configured Voltage: 1.1 V
        Memory Technology: DRAM
        Memory Operating Mode Capability: Volatile memory
        Firmware Version: Unknown
        Module Manufacturer ID: Bank 1, Hex 0xCE
        Module Product ID: Unknown
        Memory Subsystem Controller Manufacturer ID: Unknown
        Memory Subsystem Controller Product ID: Unknown
        Non-Volatile Size: None
        Volatile Size: 8 GB
        Cache Size: None
        Logical Size: None

    Handle 0x0014, DMI type 20, 35 bytes
    Memory Device Mapped Address
        Starting Address: 0x00000000000
        Ending Address: 0x001FFFFFFFF
        Range Size: 8 GB
        Physical Device Handle: 0x0013
        Memory Array Mapped Address Handle: 0x0011
        Partition Row Position: Unknown
        Interleave Position: Unknown
        Interleaved Data Depth: Unknown

    Handle 0x0015, DMI type 18, 23 bytes
    32-bit Memory Error Information
        Type: OK
        Granularity: Unknown
        Operation: Unknown
        Vendor Syndrome: Unknown
        Memory Array Address: Unknown
        Device Address: Unknown
        Resolution: Unknown

    Handle 0x0016, DMI type 17, 92 bytes
    Memory Device
        Array Handle: 0x0010
        Error Information Handle: 0x0015
        Total Width: 64 bits
        Data Width: 64 bits
        Size: 32 GB
        Form Factor: SODIMM
        Set: None
        Locator: DIMM 0
        Bank Locator: P0 CHANNEL B
        Type: DDR5
        Type Detail: Synchronous Unbuffered (Unregistered)
        Speed: 4800 MT/s
        Manufacturer: Unknown
        Serial Number: 00000000
        Asset Tag: Not Specified
        Part Number: CMSX32GX5M1A4800C40
        Rank: 2
        Configured Memory Speed: 4800 MT/s
        Minimum Voltage: 1.1 V
        Maximum Voltage: 1.1 V
        Configured Voltage: 1.1 V
        Memory Technology: DRAM
        Memory Operating Mode Capability: Volatile memory
        Firmware Version: Unknown
        Module Manufacturer ID: Bank 3, Hex 0x9E
        Module Product ID: Unknown
        Memory Subsystem Controller Manufacturer ID: Unknown
        Memory Subsystem Controller Product ID: Unknown
        Non-Volatile Size: None
        Volatile Size: 32 GB
        Cache Size: None
        Logical Size: None

    Handle 0x0017, DMI type 20, 35 bytes
    Memory Device Mapped Address
        Starting Address: 0x00200000000
        Ending Address: 0x009FFFFFFFF
        Range Size: 32 GB
        Physical Device Handle: 0x0016
        Memory Array Mapped Address Handle: 0x0011
        Partition Row Position: Unknown
        Interleave Position: Unknown
        Interleaved Data Depth: Unknown

    Handle 0x002A, DMI type 10, 26 bytes
    On Board Device 1 Information
        Type: Video
        Status: Enabled
        Description: VGA
    On Board Device 2 Information
        Type: Ethernet
        Status: Enabled
        Description: GLAN
    On Board Device 3 Information
        Type: Ethernet
        Status: Enabled
        Description: WLAN
    On Board Device 4 Information
        Type: Sound
        Status: Enabled
        Description: Audio CODEC
    On Board Device 5 Information
        Type: SATA Controller
        Status: Enabled
        Description: SATA Controller
    On Board Device 6 Information
        Type: Other
        Status: Enabled
        Description: USB 2.0 Controller
    On Board Device 7 Information
        Type: Other
        Status: Enabled
        Description: USB 3.0 Controller
    On Board Device 8 Information
        Type: Other
        Status: Enabled
        Description: SMBus Controller
    On Board Device 9 Information
        Type: Other
        Status: Enabled
        Description: Card Reader
    On Board Device 10 Information
        Type: Other
        Status: Enabled
        Description: Cmos Camera
    On Board Device 11 Information
        Type: Other
        Status: Enabled
        Description: Bluetooth

    Handle 0x002B, DMI type 11, 5 bytes
    OEM Strings
        String 1:
        String 2:
        String 3:
        String 4:
        String 5:

    Handle 0x002C, DMI type 12, 5 bytes
    System Configuration Options
        Option 1: SMI:00B26C
        Option 2: DSN:
        Option 3: DSN:
        Option 4: DSN:

    Handle 0x002D, DMI type 127, 4 bytes
    End Of Table

### [GPU features]

** Note**\
All of the below data was collected under the environmental condition of `WLR_DRM_DEVICES = /dev/dri/card0:/dev/dri/card1`.

#### [OpenCL]

With `HSA_OVERRIDE_GFX_VERSION=10.3.0` as an environmental variable, running `clinfo` will hang indefinitely if run as a normal user, but not when run as root. If it is set to 10.3.2 or 10.3.5, this is not an issue. The first `clinfo` output below was run with `HSA_OVERRIDE_GFX_VERSION=10.3.0` as an environmental variable. The OpenCL hardware database has other reports on these devices as well.^[\[70\]](#cite_note-70)[\[71\]](#cite_note-71)^

`root `[`#`]`clinfo`

    Number of platforms                               1
      Platform Name                                   AMD Accelerated Parallel Processing
      Platform Vendor                                 Advanced Micro Devices, Inc.
      Platform Version                                OpenCL 2.1 AMD-APP.dbg (3513.0)
      Platform Profile                                FULL_PROFILE
      Platform Extensions                             cl_khr_icd cl_amd_event_callback
      Platform Extensions function suffix             AMD
      Platform Host timer resolution                  1ns

      Platform Name                                   AMD Accelerated Parallel Processing
    Number of devices                                 2
      Device Name                                     gfx1030
      Device Vendor                                   Advanced Micro Devices, Inc.
      Device Vendor ID                                0x1002
      Device Version                                  OpenCL 2.0
      Driver Version                                  3513.0 (HSA1.1,LC)
      Device OpenCL C Version                         OpenCL C 2.0
      Device Type                                     GPU
      Device Board Name (AMD)                         AMD Radeon RX 6700S
      Device PCI-e ID (AMD)                           0x73ef
      Device Topology (AMD)                           PCI-E, 0000:03:00.0
      Device Profile                                  FULL_PROFILE
      Device Available                                Yes
      Compiler Available                              Yes
      Linker Available                                Yes
      Max compute units                               14
      SIMD per compute unit (AMD)                     4
      SIMD width (AMD)                                32
      SIMD instruction width (AMD)                    1
      Max clock frequency                             2435MHz
      Graphics IP (AMD)                               10.3
      Device Partition                                (core)
        Max number of sub-devices                     14
        Supported partition types                     None
        Supported affinity domains                    (n/a)
      Max work item dimensions                        3
      Max work item sizes                             1024x1024x1024
      Max work group size                             256
      Preferred work group size (AMD)                 256
      Max work group size (AMD)                       1024
      Preferred work group size multiple (kernel)     32
      Wavefront width (AMD)                           32
      Preferred / native vector sizes
        char                                                 4 / 4
        short                                                2 / 2
        int                                                  1 / 1
        long                                                 1 / 1
        half                                                 1 / 1        (cl_khr_fp16)
        float                                                1 / 1
        double                                               1 / 1        (cl_khr_fp64)
      Half-precision Floating-point support           (cl_khr_fp16)
        Denormals                                     No
        Infinity and NANs                             No
        Round to nearest                              No
        Round to zero                                 No
        Round to infinity                             No
        IEEE754-2008 fused multiply-add               No
        Support is emulated in software               No
      Single-precision Floating-point support         (core)
        Denormals                                     Yes
        Infinity and NANs                             Yes
        Round to nearest                              Yes
        Round to zero                                 Yes
        Round to infinity                             Yes
        IEEE754-2008 fused multiply-add               Yes
        Support is emulated in software               No
        Correctly-rounded divide and sqrt operations  Yes
      Double-precision Floating-point support         (cl_khr_fp64)
        Denormals                                     Yes
        Infinity and NANs                             Yes
        Round to nearest                              Yes
        Round to zero                                 Yes
        Round to infinity                             Yes
        IEEE754-2008 fused multiply-add               Yes
        Support is emulated in software               No
      Address bits                                    64, Little-Endian
      Global memory size                              8573157376 (7.984GiB)
      Global free memory (AMD)                        8372224 (7.984GiB) 8372224 (7.984GiB)
      Global memory channels (AMD)                    4
      Global memory banks per channel (AMD)           4
      Global memory bank width (AMD)                  256 bytes
      Error Correction support                        No
      Max memory allocation                           7287183768 (6.787GiB)
      Unified memory for Host and Device              No
      Shared Virtual Memory (SVM) capabilities        (core)
        Coarse-grained buffer sharing                 Yes
        Fine-grained buffer sharing                   Yes
        Fine-grained system sharing                   No
        Atomics                                       No
      Minimum alignment for any data type             128 bytes
      Alignment of base address                       1024 bits (128 bytes)
      Preferred alignment for atomics
        SVM                                           0 bytes
        Global                                        0 bytes
        Local                                         0 bytes
      Max size for global variable                    7287183768 (6.787GiB)
      Preferred total size of global vars             8573157376 (7.984GiB)
      Global Memory cache type                        Read/Write
      Global Memory cache size                        16384 (16KiB)
      Global Memory cache line size                   64 bytes
      Image support                                   Yes
        Max number of samplers per kernel             29679
        Max size for 1D images from buffer            134217728 pixels
        Max 1D or 2D image array size                 8192 images
        Base address alignment for 2D image buffers   256 bytes
        Pitch alignment for 2D image buffers          256 pixels
        Max 2D image size                             16384x16384 pixels
        Max 3D image size                             16384x16384x8192 pixels
        Max number of read image args                 128
        Max number of write image args                8
        Max number of read/write image args           64
      Max number of pipe args                         16
      Max active pipe reservations                    16
      Max pipe packet size                            2992216472 (2.787GiB)
      Local memory type                               Local
      Local memory size                               65536 (64KiB)
      Local memory size per CU (AMD)                  65536 (64KiB)
      Local memory banks (AMD)                        32
      Max number of constant args                     8
      Max constant buffer size                        7287183768 (6.787GiB)
      Preferred constant buffer size (AMD)            16384 (16KiB)
      Max size of kernel argument                     1024
      Queue properties (on host)
        Out-of-order execution                        No
        Profiling                                     Yes
      Queue properties (on device)
        Out-of-order execution                        Yes
        Profiling                                     Yes
        Preferred size                                262144 (256KiB)
        Max size                                      8388608 (8MiB)
      Max queues on device                            1
      Max events on device                            1024
      Prefer user sync for interop                    Yes
      Number of P2P devices (AMD)                     0
      Profiling timer resolution                      1ns
      Profiling timer offset since Epoch (AMD)        0ns (Wed Dec 31 19:00:00 1969)
      Execution capabilities
        Run OpenCL kernels                            Yes
        Run native kernels                            No
        Thread trace supported (AMD)                  No
        Number of async queues (AMD)                  8
        Max real-time compute queues (AMD)            8
        Max real-time compute units (AMD)             14
      printf() buffer size                            4194304 (4MiB)
      Built-in kernels                                (n/a)
      Device Extensions                               cl_khr_fp64 cl_khr_global_int32_base_atomics cl_khr_global_int32_extended_atomics cl_khr_local_int32_base_atomics cl_khr_local_int32_extended_atomics cl_khr_int64_base_atomics cl_khr_int64_extended_atomics cl_khr_3d_image_writes cl_khr_byte_addressable_store cl_khr_fp16 cl_khr_gl_sharing cl_amd_device_attribute_query cl_amd_media_ops cl_amd_media_ops2 cl_khr_image2d_from_buffer cl_khr_subgroups cl_khr_depth_images cl_amd_copy_buffer_p2p cl_amd_assembly_program

      Device Name                                     gfx1030
      Device Vendor                                   Advanced Micro Devices, Inc.
      Device Vendor ID                                0x1002
      Device Version                                  OpenCL 2.0
      Driver Version                                  3513.0 (HSA1.1,LC)
      Device OpenCL C Version                         OpenCL C 2.0
      Device Type                                     GPU
      Device Board Name (AMD)                         AMD Radeon Graphics
      Device PCI-e ID (AMD)                           0x1681
      Device Topology (AMD)                           PCI-E, 0000:07:00.0
      Device Profile                                  FULL_PROFILE
      Device Available                                Yes
      Compiler Available                              Yes
      Linker Available                                Yes
      Max compute units                               6
      SIMD per compute unit (AMD)                     4
      SIMD width (AMD)                                32
      SIMD instruction width (AMD)                    1
      Max clock frequency                             2400MHz
      Graphics IP (AMD)                               10.3
      Device Partition                                (core)
        Max number of sub-devices                     6
        Supported partition types                     None
        Supported affinity domains                    (n/a)
      Max work item dimensions                        3
      Max work item sizes                             1024x1024x1024
      Max work group size                             256
      Preferred work group size (AMD)                 256
      Max work group size (AMD)                       1024
      Preferred work group size multiple (kernel)     <getWGsizes:1980: create kernel : error -6>
      Wavefront width (AMD)                           32
      Preferred / native vector sizes
        char                                                 4 / 4
        short                                                2 / 2
        int                                                  1 / 1
        long                                                 1 / 1
        half                                                 1 / 1        (cl_khr_fp16)
        float                                                1 / 1
        double                                               1 / 1        (cl_khr_fp64)
      Half-precision Floating-point support           (cl_khr_fp16)
        Denormals                                     No
        Infinity and NANs                             No
        Round to nearest                              No
        Round to zero                                 No
        Round to infinity                             No
        IEEE754-2008 fused multiply-add               No
        Support is emulated in software               No
      Single-precision Floating-point support         (core)
        Denormals                                     Yes
        Infinity and NANs                             Yes
        Round to nearest                              Yes
        Round to zero                                 Yes
        Round to infinity                             Yes
        IEEE754-2008 fused multiply-add               Yes
        Support is emulated in software               No
        Correctly-rounded divide and sqrt operations  Yes
      Double-precision Floating-point support         (cl_khr_fp64)
        Denormals                                     Yes
        Infinity and NANs                             Yes
        Round to nearest                              Yes
        Round to zero                                 Yes
        Round to infinity                             Yes
        IEEE754-2008 fused multiply-add               Yes
        Support is emulated in software               No
      Address bits                                    64, Little-Endian
      Global memory size                              536870912 (512MiB)
      Global free memory (AMD)                        524288 (512MiB) 524288 (512MiB)
      Global memory channels (AMD)                    4
      Global memory banks per channel (AMD)           4
      Global memory bank width (AMD)                  256 bytes
      Error Correction support                        No
      Max memory allocation                           456340272 (435.2MiB)
      Unified memory for Host and Device              No
      Shared Virtual Memory (SVM) capabilities        (core)
        Coarse-grained buffer sharing                 Yes
        Fine-grained buffer sharing                   Yes
        Fine-grained system sharing                   No
        Atomics                                       No
      Minimum alignment for any data type             128 bytes
      Alignment of base address                       1024 bits (128 bytes)
      Preferred alignment for atomics
        SVM                                           0 bytes
        Global                                        0 bytes
        Local                                         0 bytes
      Max size for global variable                    456340272 (435.2MiB)
      Preferred total size of global vars             536870912 (512MiB)
      Global Memory cache type                        Read/Write
      Global Memory cache size                        16384 (16KiB)
      Global Memory cache line size                   64 bytes
      Image support                                   Yes
        Max number of samplers per kernel             5761
        Max size for 1D images from buffer            134217728 pixels
        Max 1D or 2D image array size                 8192 images
        Base address alignment for 2D image buffers   256 bytes
        Pitch alignment for 2D image buffers          256 pixels
        Max 2D image size                             16384x16384 pixels
        Max 3D image size                             16384x16384x8192 pixels
        Max number of read image args                 128
        Max number of write image args                8
        Max number of read/write image args           64
      Max number of pipe args                         16
      Max active pipe reservations                    16
      Max pipe packet size                            456340272 (435.2MiB)
      Local memory type                               Local
      Local memory size                               65536 (64KiB)
      Local memory size per CU (AMD)                  65536 (64KiB)
      Local memory banks (AMD)                        32
      Max number of constant args                     8
      Max constant buffer size                        456340272 (435.2MiB)
      Preferred constant buffer size (AMD)            16384 (16KiB)
      Max size of kernel argument                     1024
      Queue properties (on host)
        Out-of-order execution                        No
        Profiling                                     Yes
      Queue properties (on device)
        Out-of-order execution                        Yes
        Profiling                                     Yes
        Preferred size                                262144 (256KiB)
        Max size                                      8388608 (8MiB)
      Max queues on device                            1
      Max events on device                            1024
      Prefer user sync for interop                    Yes
      Number of P2P devices (AMD)                     0
      Profiling timer resolution                      1ns
      Profiling timer offset since Epoch (AMD)        0ns (Wed Dec 31 19:00:00 1969)
      Execution capabilities
        Run OpenCL kernels                            Yes
        Run native kernels                            No
        Thread trace supported (AMD)                  No
        Number of async queues (AMD)                  8
        Max real-time compute queues (AMD)            8
        Max real-time compute units (AMD)             6
      printf() buffer size                            4194304 (4MiB)
      Built-in kernels                                (n/a)
      Device Extensions                               cl_khr_fp64 cl_khr_global_int32_base_atomics cl_khr_global_int32_extended_atomics cl_khr_local_int32_base_atomics cl_khr_local_int32_extended_atomics cl_khr_int64_base_atomics cl_khr_int64_extended_atomics cl_khr_3d_image_writes cl_khr_byte_addressable_store cl_khr_fp16 cl_khr_gl_sharing cl_amd_device_attribute_query cl_amd_media_ops cl_amd_media_ops2 cl_khr_image2d_from_buffer cl_khr_subgroups cl_khr_depth_images cl_amd_copy_buffer_p2p cl_amd_assembly_program

    NULL platform behavior
      clGetPlatformInfo(NULL, CL_PLATFORM_NAME, ...)  No platform
      clGetDeviceIDs(NULL, CL_DEVICE_TYPE_ALL, ...)   No platform
      clCreateContext(NULL, ...) [default]            No platform
      clCreateContext(NULL, ...) [other]              Success [AMD]
      clCreateContextFromType(NULL, CL_DEVICE_TYPE_DEFAULT)  Success (1)
        Platform Name                                 AMD Accelerated Parallel Processing
        Device Name                                   gfx1030
      clCreateContextFromType(NULL, CL_DEVICE_TYPE_CPU)  No devices found in platform
      clCreateContextFromType(NULL, CL_DEVICE_TYPE_GPU)  Success (2)
        Platform Name                                 AMD Accelerated Parallel Processing
        Device Name                                   gfx1030
        Device Name                                   gfx1030
      clCreateContextFromType(NULL, CL_DEVICE_TYPE_ACCELERATOR)  No devices found in platform
      clCreateContextFromType(NULL, CL_DEVICE_TYPE_CUSTOM)  No devices found in platform
      clCreateContextFromType(NULL, CL_DEVICE_TYPE_ALL)  Success (2)
        Platform Name                                 AMD Accelerated Parallel Processing
        Device Name                                   gfx1030
        Device Name                                   gfx1030

    ICD loader properties
      ICD loader Name                                 Khronos OpenCL ICD Loader
      ICD loader Vendor                               Khronos Group
      ICD loader Version                              3.0.6
      ICD loader Profile                              OpenCL 3.0

`user `[`$`]`HSA_OVERRIDE_GFX_VERSION=10.3.2 clinfo`

    Number of platforms                               1
      Platform Name                                   AMD Accelerated Parallel Processing
      Platform Vendor                                 Advanced Micro Devices, Inc.
      Platform Version                                OpenCL 2.1 AMD-APP.dbg (3513.0)
      Platform Profile                                FULL_PROFILE
      Platform Extensions                             cl_khr_icd cl_amd_event_callback
      Platform Extensions function suffix             AMD
      Platform Host timer resolution                  1ns

      Platform Name                                   AMD Accelerated Parallel Processing
    Number of devices                                 2
      Device Name                                     gfx1032
      Device Vendor                                   Advanced Micro Devices, Inc.
      Device Vendor ID                                0x1002
      Device Version                                  OpenCL 2.0
      Driver Version                                  3513.0 (HSA1.1,LC)
      Device OpenCL C Version                         OpenCL C 2.0
      Device Type                                     GPU
      Device Board Name (AMD)                         AMD Radeon RX 6700S
      Device PCI-e ID (AMD)                           0x73ef
      Device Topology (AMD)                           PCI-E, 0000:03:00.0
      Device Profile                                  FULL_PROFILE
      Device Available                                Yes
      Compiler Available                              Yes
      Linker Available                                Yes
      Max compute units                               14
      SIMD per compute unit (AMD)                     4
      SIMD width (AMD)                                32
      SIMD instruction width (AMD)                    1
      Max clock frequency                             2435MHz
      Graphics IP (AMD)                               10.3
      Device Partition                                (core)
        Max number of sub-devices                     14
        Supported partition types                     None
        Supported affinity domains                    (n/a)
      Max work item dimensions                        3
      Max work item sizes                             1024x1024x1024
      Max work group size                             256
      Preferred work group size (AMD)                 256
      Max work group size (AMD)                       1024
      Preferred work group size multiple (kernel)     32
      Wavefront width (AMD)                           32
      Preferred / native vector sizes
        char                                                 4 / 4
        short                                                2 / 2
        int                                                  1 / 1
        long                                                 1 / 1
        half                                                 1 / 1        (cl_khr_fp16)
        float                                                1 / 1
        double                                               1 / 1        (cl_khr_fp64)
      Half-precision Floating-point support           (cl_khr_fp16)
        Denormals                                     No
        Infinity and NANs                             No
        Round to nearest                              No
        Round to zero                                 No
        Round to infinity                             No
        IEEE754-2008 fused multiply-add               No
        Support is emulated in software               No
      Single-precision Floating-point support         (core)
        Denormals                                     Yes
        Infinity and NANs                             Yes
        Round to nearest                              Yes
        Round to zero                                 Yes
        Round to infinity                             Yes
        IEEE754-2008 fused multiply-add               Yes
        Support is emulated in software               No
        Correctly-rounded divide and sqrt operations  Yes
      Double-precision Floating-point support         (cl_khr_fp64)
        Denormals                                     Yes
        Infinity and NANs                             Yes
        Round to nearest                              Yes
        Round to zero                                 Yes
        Round to infinity                             Yes
        IEEE754-2008 fused multiply-add               Yes
        Support is emulated in software               No
      Address bits                                    64, Little-Endian
      Global memory size                              8573157376 (7.984GiB)
      Global free memory (AMD)                        8372224 (7.984GiB) 8372224 (7.984GiB)
      Global memory channels (AMD)                    4
      Global memory banks per channel (AMD)           4
      Global memory bank width (AMD)                  256 bytes
      Error Correction support                        No
      Max memory allocation                           7287183768 (6.787GiB)
      Unified memory for Host and Device              No
      Shared Virtual Memory (SVM) capabilities        (core)
        Coarse-grained buffer sharing                 Yes
        Fine-grained buffer sharing                   Yes
        Fine-grained system sharing                   No
        Atomics                                       No
      Minimum alignment for any data type             128 bytes
      Alignment of base address                       1024 bits (128 bytes)
      Preferred alignment for atomics
        SVM                                           0 bytes
        Global                                        0 bytes
        Local                                         0 bytes
      Max size for global variable                    7287183768 (6.787GiB)
      Preferred total size of global vars             8573157376 (7.984GiB)
      Global Memory cache type                        Read/Write
      Global Memory cache size                        16384 (16KiB)
      Global Memory cache line size                   64 bytes
      Image support                                   Yes
        Max number of samplers per kernel             29679
        Max size for 1D images from buffer            134217728 pixels
        Max 1D or 2D image array size                 8192 images
        Base address alignment for 2D image buffers   256 bytes
        Pitch alignment for 2D image buffers          256 pixels
        Max 2D image size                             16384x16384 pixels
        Max 3D image size                             16384x16384x8192 pixels
        Max number of read image args                 128
        Max number of write image args                8
        Max number of read/write image args           64
      Max number of pipe args                         16
      Max active pipe reservations                    16
      Max pipe packet size                            2992216472 (2.787GiB)
      Local memory type                               Local
      Local memory size                               65536 (64KiB)
      Local memory size per CU (AMD)                  65536 (64KiB)
      Local memory banks (AMD)                        32
      Max number of constant args                     8
      Max constant buffer size                        7287183768 (6.787GiB)
      Preferred constant buffer size (AMD)            16384 (16KiB)
      Max size of kernel argument                     1024
      Queue properties (on host)
        Out-of-order execution                        No
        Profiling                                     Yes
      Queue properties (on device)
        Out-of-order execution                        Yes
        Profiling                                     Yes
        Preferred size                                262144 (256KiB)
        Max size                                      8388608 (8MiB)
      Max queues on device                            1
      Max events on device                            1024
      Prefer user sync for interop                    Yes
      Number of P2P devices (AMD)                     0
      Profiling timer resolution                      1ns
      Profiling timer offset since Epoch (AMD)        0ns (Wed Dec 31 19:00:00 1969)
      Execution capabilities
        Run OpenCL kernels                            Yes
        Run native kernels                            No
        Thread trace supported (AMD)                  No
        Number of async queues (AMD)                  8
        Max real-time compute queues (AMD)            8
        Max real-time compute units (AMD)             14
      printf() buffer size                            4194304 (4MiB)
      Built-in kernels                                (n/a)
      Device Extensions                               cl_khr_fp64 cl_khr_global_int32_base_atomics cl_khr_global_int32_extended_atomics cl_khr_local_int32_base_atomics cl_khr_local_int32_extended_atomics cl_khr_int64_base_atomics cl_khr_int64_extended_atomics cl_khr_3d_image_writes cl_khr_byte_addressable_store cl_khr_fp16 cl_khr_gl_sharing cl_amd_device_attribute_query cl_amd_media_ops cl_amd_media_ops2 cl_khr_image2d_from_buffer cl_khr_subgroups cl_khr_depth_images cl_amd_copy_buffer_p2p cl_amd_assembly_program

      Device Name                                     gfx1032
      Device Vendor                                   Advanced Micro Devices, Inc.
      Device Vendor ID                                0x1002
      Device Version                                  OpenCL 2.0
      Driver Version                                  3513.0 (HSA1.1,LC)
      Device OpenCL C Version                         OpenCL C 2.0
      Device Type                                     GPU
      Device Board Name (AMD)                         AMD Radeon Graphics
      Device PCI-e ID (AMD)                           0x1681
      Device Topology (AMD)                           PCI-E, 0000:07:00.0
      Device Profile                                  FULL_PROFILE
      Device Available                                Yes
      Compiler Available                              Yes
      Linker Available                                Yes
      Max compute units                               6
      SIMD per compute unit (AMD)                     4
      SIMD width (AMD)                                32
      SIMD instruction width (AMD)                    1
      Max clock frequency                             2400MHz
      Graphics IP (AMD)                               10.3
      Device Partition                                (core)
        Max number of sub-devices                     6
        Supported partition types                     None
        Supported affinity domains                    (n/a)
      Max work item dimensions                        3
      Max work item sizes                             1024x1024x1024
      Max work group size                             256
      Preferred work group size (AMD)                 256
      Max work group size (AMD)                       1024
      Preferred work group size multiple (kernel)     <getWGsizes:1980: create kernel : error -6>
      Wavefront width (AMD)                           32
      Preferred / native vector sizes
        char                                                 4 / 4
        short                                                2 / 2
        int                                                  1 / 1
        long                                                 1 / 1
        half                                                 1 / 1        (cl_khr_fp16)
        float                                                1 / 1
        double                                               1 / 1        (cl_khr_fp64)
      Half-precision Floating-point support           (cl_khr_fp16)
        Denormals                                     No
        Infinity and NANs                             No
        Round to nearest                              No
        Round to zero                                 No
        Round to infinity                             No
        IEEE754-2008 fused multiply-add               No
        Support is emulated in software               No
      Single-precision Floating-point support         (core)
        Denormals                                     Yes
        Infinity and NANs                             Yes
        Round to nearest                              Yes
        Round to zero                                 Yes
        Round to infinity                             Yes
        IEEE754-2008 fused multiply-add               Yes
        Support is emulated in software               No
        Correctly-rounded divide and sqrt operations  Yes
      Double-precision Floating-point support         (cl_khr_fp64)
        Denormals                                     Yes
        Infinity and NANs                             Yes
        Round to nearest                              Yes
        Round to zero                                 Yes
        Round to infinity                             Yes
        IEEE754-2008 fused multiply-add               Yes
        Support is emulated in software               No
      Address bits                                    64, Little-Endian
      Global memory size                              536870912 (512MiB)
      Global free memory (AMD)                        524288 (512MiB) 524288 (512MiB)
      Global memory channels (AMD)                    4
      Global memory banks per channel (AMD)           4
      Global memory bank width (AMD)                  256 bytes
      Error Correction support                        No
      Max memory allocation                           456340272 (435.2MiB)
      Unified memory for Host and Device              No
      Shared Virtual Memory (SVM) capabilities        (core)
        Coarse-grained buffer sharing                 Yes
        Fine-grained buffer sharing                   Yes
        Fine-grained system sharing                   No
        Atomics                                       No
      Minimum alignment for any data type             128 bytes
      Alignment of base address                       1024 bits (128 bytes)
      Preferred alignment for atomics
        SVM                                           0 bytes
        Global                                        0 bytes
        Local                                         0 bytes
      Max size for global variable                    456340272 (435.2MiB)
      Preferred total size of global vars             536870912 (512MiB)
      Global Memory cache type                        Read/Write
      Global Memory cache size                        16384 (16KiB)
      Global Memory cache line size                   64 bytes
      Image support                                   Yes
        Max number of samplers per kernel             5761
        Max size for 1D images from buffer            134217728 pixels
        Max 1D or 2D image array size                 8192 images
        Base address alignment for 2D image buffers   256 bytes
        Pitch alignment for 2D image buffers          256 pixels
        Max 2D image size                             16384x16384 pixels
        Max 3D image size                             16384x16384x8192 pixels
        Max number of read image args                 128
        Max number of write image args                8
        Max number of read/write image args           64
      Max number of pipe args                         16
      Max active pipe reservations                    16
      Max pipe packet size                            456340272 (435.2MiB)
      Local memory type                               Local
      Local memory size                               65536 (64KiB)
      Local memory size per CU (AMD)                  65536 (64KiB)
      Local memory banks (AMD)                        32
      Max number of constant args                     8
      Max constant buffer size                        456340272 (435.2MiB)
      Preferred constant buffer size (AMD)            16384 (16KiB)
      Max size of kernel argument                     1024
      Queue properties (on host)
        Out-of-order execution                        No
        Profiling                                     Yes
      Queue properties (on device)
        Out-of-order execution                        Yes
        Profiling                                     Yes
        Preferred size                                262144 (256KiB)
        Max size                                      8388608 (8MiB)
      Max queues on device                            1
      Max events on device                            1024
      Prefer user sync for interop                    Yes
      Number of P2P devices (AMD)                     0
      Profiling timer resolution                      1ns
      Profiling timer offset since Epoch (AMD)        0ns (Wed Dec 31 19:00:00 1969)
      Execution capabilities
        Run OpenCL kernels                            Yes
        Run native kernels                            No
        Thread trace supported (AMD)                  No
        Number of async queues (AMD)                  8
        Max real-time compute queues (AMD)            8
        Max real-time compute units (AMD)             6
      printf() buffer size                            4194304 (4MiB)
      Built-in kernels                                (n/a)
      Device Extensions                               cl_khr_fp64 cl_khr_global_int32_base_atomics cl_khr_global_int32_extended_atomics cl_khr_local_int32_base_atomics cl_khr_local_int32_extended_atomics cl_khr_int64_base_atomics cl_khr_int64_extended_atomics cl_khr_3d_image_writes cl_khr_byte_addressable_store cl_khr_fp16 cl_khr_gl_sharing cl_amd_device_attribute_query cl_amd_media_ops cl_amd_media_ops2 cl_khr_image2d_from_buffer cl_khr_subgroups cl_khr_depth_images cl_amd_copy_buffer_p2p cl_amd_assembly_program

    NULL platform behavior
      clGetPlatformInfo(NULL, CL_PLATFORM_NAME, ...)  No platform
      clGetDeviceIDs(NULL, CL_DEVICE_TYPE_ALL, ...)   No platform
      clCreateContext(NULL, ...) [default]            No platform
      clCreateContext(NULL, ...) [other]              Success [AMD]
      clCreateContextFromType(NULL, CL_DEVICE_TYPE_DEFAULT)  Success (1)
        Platform Name                                 AMD Accelerated Parallel Processing
        Device Name                                   gfx1032
      clCreateContextFromType(NULL, CL_DEVICE_TYPE_CPU)  No devices found in platform
      clCreateContextFromType(NULL, CL_DEVICE_TYPE_GPU)  Success (2)
        Platform Name                                 AMD Accelerated Parallel Processing
        Device Name                                   gfx1032
        Device Name                                   gfx1032
      clCreateContextFromType(NULL, CL_DEVICE_TYPE_ACCELERATOR)  No devices found in platform
      clCreateContextFromType(NULL, CL_DEVICE_TYPE_CUSTOM)  No devices found in platform
      clCreateContextFromType(NULL, CL_DEVICE_TYPE_ALL)  Success (2)
        Platform Name                                 AMD Accelerated Parallel Processing
        Device Name                                   gfx1032
        Device Name                                   gfx1032

    ICD loader properties
      ICD loader Name                                 Khronos OpenCL ICD Loader
      ICD loader Vendor                               Khronos Group
      ICD loader Version                              3.0.6
      ICD loader Profile                              OpenCL 3.0

`user `[`$`]`HSA_OVERRIDE_GFX_VERSION=10.3.5 clinfo`

    Number of platforms                               1
      Platform Name                                   AMD Accelerated Parallel Processing
      Platform Vendor                                 Advanced Micro Devices, Inc.
      Platform Version                                OpenCL 2.1 AMD-APP.dbg (3513.0)
      Platform Profile                                FULL_PROFILE
      Platform Extensions                             cl_khr_icd cl_amd_event_callback
      Platform Extensions function suffix             AMD
      Platform Host timer resolution                  1ns

      Platform Name                                   AMD Accelerated Parallel Processing
    Number of devices                                 2
      Device Name                                     gfx1035
      Device Vendor                                   Advanced Micro Devices, Inc.
      Device Vendor ID                                0x1002
      Device Version                                  OpenCL 2.0
      Driver Version                                  3513.0 (HSA1.1,LC)
      Device OpenCL C Version                         OpenCL C 2.0
      Device Type                                     GPU
      Device Board Name (AMD)                         AMD Radeon RX 6700S
      Device PCI-e ID (AMD)                           0x73ef
      Device Topology (AMD)                           PCI-E, 0000:03:00.0
      Device Profile                                  FULL_PROFILE
      Device Available                                Yes
      Compiler Available                              Yes
      Linker Available                                Yes
      Max compute units                               14
      SIMD per compute unit (AMD)                     4
      SIMD width (AMD)                                32
      SIMD instruction width (AMD)                    1
      Max clock frequency                             2435MHz
      Graphics IP (AMD)                               10.3
      Device Partition                                (core)
        Max number of sub-devices                     14
        Supported partition types                     None
        Supported affinity domains                    (n/a)
      Max work item dimensions                        3
      Max work item sizes                             1024x1024x1024
      Max work group size                             256
      Preferred work group size (AMD)                 256
      Max work group size (AMD)                       1024
      Preferred work group size multiple (kernel)     32
      Wavefront width (AMD)                           32
      Preferred / native vector sizes
        char                                                 4 / 4
        short                                                2 / 2
        int                                                  1 / 1
        long                                                 1 / 1
        half                                                 1 / 1        (cl_khr_fp16)
        float                                                1 / 1
        double                                               1 / 1        (cl_khr_fp64)
      Half-precision Floating-point support           (cl_khr_fp16)
        Denormals                                     No
        Infinity and NANs                             No
        Round to nearest                              No
        Round to zero                                 No
        Round to infinity                             No
        IEEE754-2008 fused multiply-add               No
        Support is emulated in software               No
      Single-precision Floating-point support         (core)
        Denormals                                     Yes
        Infinity and NANs                             Yes
        Round to nearest                              Yes
        Round to zero                                 Yes
        Round to infinity                             Yes
        IEEE754-2008 fused multiply-add               Yes
        Support is emulated in software               No
        Correctly-rounded divide and sqrt operations  Yes
      Double-precision Floating-point support         (cl_khr_fp64)
        Denormals                                     Yes
        Infinity and NANs                             Yes
        Round to nearest                              Yes
        Round to zero                                 Yes
        Round to infinity                             Yes
        IEEE754-2008 fused multiply-add               Yes
        Support is emulated in software               No
      Address bits                                    64, Little-Endian
      Global memory size                              8573157376 (7.984GiB)
      Global free memory (AMD)                        8372224 (7.984GiB) 8372224 (7.984GiB)
      Global memory channels (AMD)                    4
      Global memory banks per channel (AMD)           4
      Global memory bank width (AMD)                  256 bytes
      Error Correction support                        No
      Max memory allocation                           7287183768 (6.787GiB)
      Unified memory for Host and Device              No
      Shared Virtual Memory (SVM) capabilities        (core)
        Coarse-grained buffer sharing                 Yes
        Fine-grained buffer sharing                   Yes
        Fine-grained system sharing                   No
        Atomics                                       No
      Minimum alignment for any data type             128 bytes
      Alignment of base address                       1024 bits (128 bytes)
      Preferred alignment for atomics
        SVM                                           0 bytes
        Global                                        0 bytes
        Local                                         0 bytes
      Max size for global variable                    7287183768 (6.787GiB)
      Preferred total size of global vars             8573157376 (7.984GiB)
      Global Memory cache type                        Read/Write
      Global Memory cache size                        16384 (16KiB)
      Global Memory cache line size                   64 bytes
      Image support                                   Yes
        Max number of samplers per kernel             29679
        Max size for 1D images from buffer            134217728 pixels
        Max 1D or 2D image array size                 8192 images
        Base address alignment for 2D image buffers   256 bytes
        Pitch alignment for 2D image buffers          256 pixels
        Max 2D image size                             16384x16384 pixels
        Max 3D image size                             16384x16384x8192 pixels
        Max number of read image args                 128
        Max number of write image args                8
        Max number of read/write image args           64
      Max number of pipe args                         16
      Max active pipe reservations                    16
      Max pipe packet size                            2992216472 (2.787GiB)
      Local memory type                               Local
      Local memory size                               65536 (64KiB)
      Local memory size per CU (AMD)                  65536 (64KiB)
      Local memory banks (AMD)                        32
      Max number of constant args                     8
      Max constant buffer size                        7287183768 (6.787GiB)
      Preferred constant buffer size (AMD)            16384 (16KiB)
      Max size of kernel argument                     1024
      Queue properties (on host)
        Out-of-order execution                        No
        Profiling                                     Yes
      Queue properties (on device)
        Out-of-order execution                        Yes
        Profiling                                     Yes
        Preferred size                                262144 (256KiB)
        Max size                                      8388608 (8MiB)
      Max queues on device                            1
      Max events on device                            1024
      Prefer user sync for interop                    Yes
      Number of P2P devices (AMD)                     0
      Profiling timer resolution                      1ns
      Profiling timer offset since Epoch (AMD)        0ns (Wed Dec 31 19:00:00 1969)
      Execution capabilities
        Run OpenCL kernels                            Yes
        Run native kernels                            No
        Thread trace supported (AMD)                  No
        Number of async queues (AMD)                  8
        Max real-time compute queues (AMD)            8
        Max real-time compute units (AMD)             14
      printf() buffer size                            4194304 (4MiB)
      Built-in kernels                                (n/a)
      Device Extensions                               cl_khr_fp64 cl_khr_global_int32_base_atomics cl_khr_global_int32_extended_atomics cl_khr_local_int32_base_atomics cl_khr_local_int32_extended_atomics cl_khr_int64_base_atomics cl_khr_int64_extended_atomics cl_khr_3d_image_writes cl_khr_byte_addressable_store cl_khr_fp16 cl_khr_gl_sharing cl_amd_device_attribute_query cl_amd_media_ops cl_amd_media_ops2 cl_khr_image2d_from_buffer cl_khr_subgroups cl_khr_depth_images cl_amd_copy_buffer_p2p cl_amd_assembly_program

      Device Name                                     gfx1035
      Device Vendor                                   Advanced Micro Devices, Inc.
      Device Vendor ID                                0x1002
      Device Version                                  OpenCL 2.0
      Driver Version                                  3513.0 (HSA1.1,LC)
      Device OpenCL C Version                         OpenCL C 2.0
      Device Type                                     GPU
      Device Board Name (AMD)                         AMD Radeon Graphics
      Device PCI-e ID (AMD)                           0x1681
      Device Topology (AMD)                           PCI-E, 0000:07:00.0
      Device Profile                                  FULL_PROFILE
      Device Available                                Yes
      Compiler Available                              Yes
      Linker Available                                Yes
      Max compute units                               6
      SIMD per compute unit (AMD)                     4
      SIMD width (AMD)                                32
      SIMD instruction width (AMD)                    1
      Max clock frequency                             2400MHz
      Graphics IP (AMD)                               10.3
      Device Partition                                (core)
        Max number of sub-devices                     6
        Supported partition types                     None
        Supported affinity domains                    (n/a)
      Max work item dimensions                        3
      Max work item sizes                             1024x1024x1024
      Max work group size                             256
      Preferred work group size (AMD)                 256
      Max work group size (AMD)                       1024
      Preferred work group size multiple (kernel)     <getWGsizes:1980: create kernel : error -6>
      Wavefront width (AMD)                           32
      Preferred / native vector sizes
        char                                                 4 / 4
        short                                                2 / 2
        int                                                  1 / 1
        long                                                 1 / 1
        half                                                 1 / 1        (cl_khr_fp16)
        float                                                1 / 1
        double                                               1 / 1        (cl_khr_fp64)
      Half-precision Floating-point support           (cl_khr_fp16)
        Denormals                                     No
        Infinity and NANs                             No
        Round to nearest                              No
        Round to zero                                 No
        Round to infinity                             No
        IEEE754-2008 fused multiply-add               No
        Support is emulated in software               No
      Single-precision Floating-point support         (core)
        Denormals                                     Yes
        Infinity and NANs                             Yes
        Round to nearest                              Yes
        Round to zero                                 Yes
        Round to infinity                             Yes
        IEEE754-2008 fused multiply-add               Yes
        Support is emulated in software               No
        Correctly-rounded divide and sqrt operations  Yes
      Double-precision Floating-point support         (cl_khr_fp64)
        Denormals                                     Yes
        Infinity and NANs                             Yes
        Round to nearest                              Yes
        Round to zero                                 Yes
        Round to infinity                             Yes
        IEEE754-2008 fused multiply-add               Yes
        Support is emulated in software               No
      Address bits                                    64, Little-Endian
      Global memory size                              536870912 (512MiB)
      Global free memory (AMD)                        524288 (512MiB) 524288 (512MiB)
      Global memory channels (AMD)                    4
      Global memory banks per channel (AMD)           4
      Global memory bank width (AMD)                  256 bytes
      Error Correction support                        No
      Max memory allocation                           456340272 (435.2MiB)
      Unified memory for Host and Device              No
      Shared Virtual Memory (SVM) capabilities        (core)
        Coarse-grained buffer sharing                 Yes
        Fine-grained buffer sharing                   Yes
        Fine-grained system sharing                   No
        Atomics                                       No
      Minimum alignment for any data type             128 bytes
      Alignment of base address                       1024 bits (128 bytes)
      Preferred alignment for atomics
        SVM                                           0 bytes
        Global                                        0 bytes
        Local                                         0 bytes
      Max size for global variable                    456340272 (435.2MiB)
      Preferred total size of global vars             536870912 (512MiB)
      Global Memory cache type                        Read/Write
      Global Memory cache size                        16384 (16KiB)
      Global Memory cache line size                   64 bytes
      Image support                                   Yes
        Max number of samplers per kernel             5761
        Max size for 1D images from buffer            134217728 pixels
        Max 1D or 2D image array size                 8192 images
        Base address alignment for 2D image buffers   256 bytes
        Pitch alignment for 2D image buffers          256 pixels
        Max 2D image size                             16384x16384 pixels
        Max 3D image size                             16384x16384x8192 pixels
        Max number of read image args                 128
        Max number of write image args                8
        Max number of read/write image args           64
      Max number of pipe args                         16
      Max active pipe reservations                    16
      Max pipe packet size                            456340272 (435.2MiB)
      Local memory type                               Local
      Local memory size                               65536 (64KiB)
      Local memory size per CU (AMD)                  65536 (64KiB)
      Local memory banks (AMD)                        32
      Max number of constant args                     8
      Max constant buffer size                        456340272 (435.2MiB)
      Preferred constant buffer size (AMD)            16384 (16KiB)
      Max size of kernel argument                     1024
      Queue properties (on host)
        Out-of-order execution                        No
        Profiling                                     Yes
      Queue properties (on device)
        Out-of-order execution                        Yes
        Profiling                                     Yes
        Preferred size                                262144 (256KiB)
        Max size                                      8388608 (8MiB)
      Max queues on device                            1
      Max events on device                            1024
      Prefer user sync for interop                    Yes
      Number of P2P devices (AMD)                     0
      Profiling timer resolution                      1ns
      Profiling timer offset since Epoch (AMD)        0ns (Wed Dec 31 19:00:00 1969)
      Execution capabilities
        Run OpenCL kernels                            Yes
        Run native kernels                            No
        Thread trace supported (AMD)                  No
        Number of async queues (AMD)                  8
        Max real-time compute queues (AMD)            8
        Max real-time compute units (AMD)             6
      printf() buffer size                            4194304 (4MiB)
      Built-in kernels                                (n/a)
      Device Extensions                               cl_khr_fp64 cl_khr_global_int32_base_atomics cl_khr_global_int32_extended_atomics cl_khr_local_int32_base_atomics cl_khr_local_int32_extended_atomics cl_khr_int64_base_atomics cl_khr_int64_extended_atomics cl_khr_3d_image_writes cl_khr_byte_addressable_store cl_khr_fp16 cl_khr_gl_sharing cl_amd_device_attribute_query cl_amd_media_ops cl_amd_media_ops2 cl_khr_image2d_from_buffer cl_khr_subgroups cl_khr_depth_images cl_amd_copy_buffer_p2p cl_amd_assembly_program

    NULL platform behavior
      clGetPlatformInfo(NULL, CL_PLATFORM_NAME, ...)  No platform
      clGetDeviceIDs(NULL, CL_DEVICE_TYPE_ALL, ...)   No platform
      clCreateContext(NULL, ...) [default]            No platform
      clCreateContext(NULL, ...) [other]              Success [AMD]
      clCreateContextFromType(NULL, CL_DEVICE_TYPE_DEFAULT)  Success (1)
        Platform Name                                 AMD Accelerated Parallel Processing
        Device Name                                   gfx1035
      clCreateContextFromType(NULL, CL_DEVICE_TYPE_CPU)  No devices found in platform
      clCreateContextFromType(NULL, CL_DEVICE_TYPE_GPU)  Success (2)
        Platform Name                                 AMD Accelerated Parallel Processing
        Device Name                                   gfx1035
        Device Name                                   gfx1035
      clCreateContextFromType(NULL, CL_DEVICE_TYPE_ACCELERATOR)  No devices found in platform
      clCreateContextFromType(NULL, CL_DEVICE_TYPE_CUSTOM)  No devices found in platform
      clCreateContextFromType(NULL, CL_DEVICE_TYPE_ALL)  Success (2)
        Platform Name                                 AMD Accelerated Parallel Processing
        Device Name                                   gfx1035
        Device Name                                   gfx1035

    ICD loader properties
      ICD loader Name                                 Khronos OpenCL ICD Loader
      ICD loader Vendor                               Khronos Group
      ICD loader Version                              3.0.6
      ICD loader Profile                              OpenCL 3.0

#### [OpenGL]

##### [680M]

`user `[`$`]`DRI_PRIME=1 glxinfo -B`

    name of display: :0
    display: :0  screen: 0
    direct rendering: Yes
    Extended renderer info (GLX_MESA_query_renderer):
        Vendor: AMD (0x1002)
        Device: AMD Radeon Graphics (rembrandt, LLVM 16.0.6, DRM 3.49, 6.1.41-gentoo-x86_64) (0x1681)
        Version: 23.1.5
        Accelerated: yes
        Video memory: 512MB
        Unified memory: no
        Preferred profile: core (0x1)
        Max core profile version: 4.6
        Max compat profile version: 4.6
        Max GLES1 profile version: 1.1
        Max GLES[23] profile version: 3.2
    Memory info (GL_ATI_meminfo):
        VBO free memory - total: 434 MB, largest block: 434 MB
        VBO free aux. memory - total: 19601 MB, largest block: 19601 MB
        Texture free memory - total: 434 MB, largest block: 434 MB
        Texture free aux. memory - total: 19601 MB, largest block: 19601 MB
        Renderbuffer free memory - total: 434 MB, largest block: 434 MB
        Renderbuffer free aux. memory - total: 19601 MB, largest block: 19601 MB
    Memory info (GL_NVX_gpu_memory_info):
        Dedicated video memory: 512 MB
        Total available memory: 20154 MB
        Currently available dedicated video memory: 434 MB
    OpenGL vendor string: AMD
    OpenGL renderer string: AMD Radeon Graphics (rembrandt, LLVM 16.0.6, DRM 3.49, 6.1.41-gentoo-x86_64)
    OpenGL core profile version string: 4.6 (Core Profile) Mesa 23.1.5
    OpenGL core profile shading language version string: 4.60
    OpenGL core profile context flags: (none)
    OpenGL core profile profile mask: core profile

    OpenGL version string: 4.6 (Compatibility Profile) Mesa 23.1.5
    OpenGL shading language version string: 4.60
    OpenGL context flags: (none)
    OpenGL profile mask: compatibility profile

    OpenGL ES profile version string: OpenGL ES 3.2 Mesa 23.1.5
    OpenGL ES profile shading language version string: OpenGL ES GLSL ES 3.20

##### [6700S]

`user `[`$`]`glxinfo -B`

    name of display: :0
    display: :0  screen: 0
    direct rendering: Yes
    Extended renderer info (GLX_MESA_query_renderer):
        Vendor: AMD (0x1002)
        Device: AMD Radeon RX 6700S (navi23, LLVM 16.0.6, DRM 3.49, 6.1.41-gentoo-x86_64) (0x73ef)
        Version: 23.0.3
        Accelerated: yes
        Video memory: 8192MB
        Unified memory: no
        Preferred profile: core (0x1)
        Max core profile version: 4.6
        Max compat profile version: 4.6
        Max GLES1 profile version: 1.1
        Max GLES[23] profile version: 3.2
    Memory info (GL_ATI_meminfo):
        VBO free memory - total: 7167 MB, largest block: 7167 MB
        VBO free aux. memory - total: 19560 MB, largest block: 19560 MB
        Texture free memory - total: 7167 MB, largest block: 7167 MB
        Texture free aux. memory - total: 19560 MB, largest block: 19560 MB
        Renderbuffer free memory - total: 7167 MB, largest block: 7167 MB
        Renderbuffer free aux. memory - total: 19560 MB, largest block: 19560 MB
    Memory info (GL_NVX_gpu_memory_info):
        Dedicated video memory: 8192 MB
        Total available memory: 27834 MB
        Currently available dedicated video memory: 7167 MB
    OpenGL vendor string: AMD
    OpenGL renderer string: AMD Radeon RX 6700S (navi23, LLVM 16.0.6, DRM 3.49, 6.1.41-gentoo-x86_64)
    OpenGL core profile version string: 4.6 (Core Profile) Mesa 23.0.3
    OpenGL core profile shading language version string: 4.60
    OpenGL core profile context flags: (none)
    OpenGL core profile profile mask: core profile

    OpenGL version string: 4.6 (Compatibility Profile) Mesa 23.0.3
    OpenGL shading language version string: 4.60
    OpenGL context flags: (none)
    OpenGL profile mask: compatibility profile

    OpenGL ES profile version string: OpenGL ES 3.2 Mesa 23.0.3
    OpenGL ES profile shading language version string: OpenGL ES GLSL ES 3.20

#### [ROCm]

`user `[`$`]`rocminfo`

    ROCk module is loaded
    =====================
    HSA System Attributes
    =====================
    Runtime Version:         1.1
    System Timestamp Freq.:  1000.000000MHz
    Sig. Max Wait Duration:  18446744073709551615 (0xFFFFFFFFFFFFFFFF) (timestamp count)
    Machine Model:           LARGE
    System Endianness:       LITTLE

    ==========
    HSA Agents
    ==========
    *******
    Agent 1
    *******
      Name:                    AMD Ryzen 9 6900HS with Radeon Graphics
      Uuid:                    CPU-XX
      Marketing Name:          AMD Ryzen 9 6900HS with Radeon Graphics
      Vendor Name:             CPU
      Feature:                 None specified
      Profile:                 FULL_PROFILE
      Float Round Mode:        NEAR
      Max Queue Number:        0(0x0)
      Queue Min Size:          0(0x0)
      Queue Max Size:          0(0x0)
      Queue Type:              MULTI
      Node:                    0
      Device Type:             CPU
      Cache Info:
        L1:                      32768(0x8000) KB
      Chip ID:                 0(0x0)
      ASIC Revision:           0(0x0)
      Cacheline Size:          64(0x40)
      Max Clock Freq. (MHz):   4935
      BDFID:                   0
      Internal Node ID:        0
      Compute Unit:            16
      SIMDs per CU:            0
      Shader Engines:          0
      Shader Arrs. per Eng.:   0
      WatchPts on Addr. Ranges:1
      Features:                None
      Pool Info:
        Pool 1
          Segment:                 GLOBAL; FLAGS: FINE GRAINED
          Size:                    40227420(0x265d25c) KB
          Allocatable:             TRUE
          Alloc Granule:           4KB
          Alloc Alignment:         4KB
          Accessible by all:       TRUE
        Pool 2
          Segment:                 GLOBAL; FLAGS: KERNARG, FINE GRAINED
          Size:                    40227420(0x265d25c) KB
          Allocatable:             TRUE
          Alloc Granule:           4KB
          Alloc Alignment:         4KB
          Accessible by all:       TRUE
        Pool 3
          Segment:                 GLOBAL; FLAGS: COARSE GRAINED
          Size:                    40227420(0x265d25c) KB
          Allocatable:             TRUE
          Alloc Granule:           4KB
          Alloc Alignment:         4KB
          Accessible by all:       TRUE
      ISA Info:
    *******
    Agent 2
    *******
      Name:                    gfx1030
      Uuid:                    GPU-XX
      Marketing Name:          AMD Radeon RX 6700S
      Vendor Name:             AMD
      Feature:                 KERNEL_DISPATCH
      Profile:                 BASE_PROFILE
      Float Round Mode:        NEAR
      Max Queue Number:        128(0x80)
      Queue Min Size:          64(0x40)
      Queue Max Size:          131072(0x20000)
      Queue Type:              MULTI
      Node:                    1
      Device Type:             GPU
      Cache Info:
        L1:                      16(0x10) KB
        L2:                      2048(0x800) KB
        L3:                      32768(0x8000) KB
      Chip ID:                 29679(0x73ef)
      ASIC Revision:           0(0x0)
      Cacheline Size:          64(0x40)
      Max Clock Freq. (MHz):   2435
      BDFID:                   768
      Internal Node ID:        1
      Compute Unit:            28
      SIMDs per CU:            2
      Shader Engines:          4
      Shader Arrs. per Eng.:   2
      WatchPts on Addr. Ranges:4
      Features:                KERNEL_DISPATCH
      Fast F16 Operation:      TRUE
      Wavefront Size:          32(0x20)
      Workgroup Max Size:      1024(0x400)
      Workgroup Max Size per Dimension:
        x                        1024(0x400)
        y                        1024(0x400)
        z                        1024(0x400)
      Max Waves Per CU:        32(0x20)
      Max Work-item Per CU:    1024(0x400)
      Grid Max Size:           4294967295(0xffffffff)
      Grid Max Size per Dimension:
        x                        4294967295(0xffffffff)
        y                        4294967295(0xffffffff)
        z                        4294967295(0xffffffff)
      Max fbarriers/Workgrp:   32
      Pool Info:
        Pool 1
          Segment:                 GLOBAL; FLAGS: COARSE GRAINED
          Size:                    8372224(0x7fc000) KB
          Allocatable:             TRUE
          Alloc Granule:           4KB
          Alloc Alignment:         4KB
          Accessible by all:       FALSE
        Pool 2
          Segment:                 GROUP
          Size:                    64(0x40) KB
          Allocatable:             FALSE
          Alloc Granule:           0KB
          Alloc Alignment:         0KB
          Accessible by all:       FALSE
      ISA Info:
        ISA 1
          Name:                    amdgcn-amd-amdhsa--gfx1030
          Machine Models:          HSA_MACHINE_MODEL_LARGE
          Profiles:                HSA_PROFILE_BASE
          Default Rounding Mode:   NEAR
          Default Rounding Mode:   NEAR
          Fast f16:                TRUE
          Workgroup Max Size:      1024(0x400)
          Workgroup Max Size per Dimension:
            x                        1024(0x400)
            y                        1024(0x400)
            z                        1024(0x400)
          Grid Max Size:           4294967295(0xffffffff)
          Grid Max Size per Dimension:
            x                        4294967295(0xffffffff)
            y                        4294967295(0xffffffff)
            z                        4294967295(0xffffffff)
          FBarrier Max Size:       32
    *******
    Agent 3
    *******
      Name:                    gfx1030
      Uuid:                    GPU-XX
      Marketing Name:          AMD Radeon Graphics
      Vendor Name:             AMD
      Feature:                 KERNEL_DISPATCH
      Profile:                 BASE_PROFILE
      Float Round Mode:        NEAR
      Max Queue Number:        128(0x80)
      Queue Min Size:          64(0x40)
      Queue Max Size:          131072(0x20000)
      Queue Type:              MULTI
      Node:                    2
      Device Type:             GPU
      Cache Info:
        L1:                      16(0x10) KB
        L2:                      2048(0x800) KB
      Chip ID:                 5761(0x1681)
      ASIC Revision:           2(0x2)
      Cacheline Size:          64(0x40)
      Max Clock Freq. (MHz):   2400
      BDFID:                   1792
      Internal Node ID:        2
      Compute Unit:            12
      SIMDs per CU:            2
      Shader Engines:          2
      Shader Arrs. per Eng.:   2
      WatchPts on Addr. Ranges:4
      Features:                KERNEL_DISPATCH
      Fast F16 Operation:      TRUE
      Wavefront Size:          32(0x20)
      Workgroup Max Size:      1024(0x400)
      Workgroup Max Size per Dimension:
        x                        1024(0x400)
        y                        1024(0x400)
        z                        1024(0x400)
      Max Waves Per CU:        32(0x20)
      Max Work-item Per CU:    1024(0x400)
      Grid Max Size:           4294967295(0xffffffff)
      Grid Max Size per Dimension:
        x                        4294967295(0xffffffff)
        y                        4294967295(0xffffffff)
        z                        4294967295(0xffffffff)
      Max fbarriers/Workgrp:   32
      Pool Info:
        Pool 1
          Segment:                 GLOBAL; FLAGS: COARSE GRAINED
          Size:                    524288(0x80000) KB
          Allocatable:             TRUE
          Alloc Granule:           4KB
          Alloc Alignment:         4KB
          Accessible by all:       FALSE
        Pool 2
          Segment:                 GROUP
          Size:                    64(0x40) KB
          Allocatable:             FALSE
          Alloc Granule:           0KB
          Alloc Alignment:         0KB
          Accessible by all:       FALSE
      ISA Info:
        ISA 1
          Name:                    amdgcn-amd-amdhsa--gfx1030
          Machine Models:          HSA_MACHINE_MODEL_LARGE
          Profiles:                HSA_PROFILE_BASE
          Default Rounding Mode:   NEAR
          Default Rounding Mode:   NEAR
          Fast f16:                TRUE
          Workgroup Max Size:      1024(0x400)
          Workgroup Max Size per Dimension:
            x                        1024(0x400)
            y                        1024(0x400)
            z                        1024(0x400)
          Grid Max Size:           4294967295(0xffffffff)
          Grid Max Size per Dimension:
            x                        4294967295(0xffffffff)
            y                        4294967295(0xffffffff)
            z                        4294967295(0xffffffff)
          FBarrier Max Size:       32
    *** Done ***

#### [VAAPI]

`user `[`$`]`vainfo`

    Trying display: wayland
    vainfo: VA-API version: 1.19 (libva 2.19.0)
    vainfo: Driver version: Mesa Gallium driver 23.0.3 for AMD Radeon RX 6700S (navi23, LLVM 16.0.6, DRM 3.49, 6.1.41-gentoo-x86_64)
    vainfo: Supported profile and entrypoints
          VAProfileMPEG2Simple            : VAEntrypointVLD
          VAProfileMPEG2Main              : VAEntrypointVLD
          VAProfileVC1Simple              : VAEntrypointVLD
          VAProfileVC1Main                : VAEntrypointVLD
          VAProfileVC1Advanced            : VAEntrypointVLD
          VAProfileH264ConstrainedBaseline: VAEntrypointVLD
          VAProfileH264ConstrainedBaseline: VAEntrypointEncSlice
          VAProfileH264Main               : VAEntrypointVLD
          VAProfileH264Main               : VAEntrypointEncSlice
          VAProfileH264High               : VAEntrypointVLD
          VAProfileH264High               : VAEntrypointEncSlice
          VAProfileHEVCMain               : VAEntrypointVLD
          VAProfileHEVCMain               : VAEntrypointEncSlice
          VAProfileHEVCMain10             : VAEntrypointVLD
          VAProfileHEVCMain10             : VAEntrypointEncSlice
          VAProfileJPEGBaseline           : VAEntrypointVLD
          VAProfileVP9Profile0            : VAEntrypointVLD
          VAProfileVP9Profile2            : VAEntrypointVLD
          VAProfileAV1Profile0            : VAEntrypointVLD
          VAProfileNone                   : VAEntrypointVideoProc

#### [VDPAU]

##### [680M]

`user `[`$`]`VDPAU_DRIVER=radeonsi DRI_PRIME=1 vdpauinfo`

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
    MPEG1                          --- not supported ---
    MPEG2_SIMPLE                   --- not supported ---
    MPEG2_MAIN                     --- not supported ---
    H264_BASELINE                  52 65536  4096  4096
    H264_MAIN                      52 65536  4096  4096
    H264_HIGH                      52 65536  4096  4096
    VC1_SIMPLE                     --- not supported ---
    VC1_MAIN                       --- not supported ---
    VC1_ADVANCED                   --- not supported ---
    MPEG4_PART2_SP                 --- not supported ---
    MPEG4_PART2_ASP                --- not supported ---
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
    B8G8R8A8         16384 16384    y  NV12 YV12 UYVY YUYV Y8U8V8A8 V8U8Y8A8 P010 P016 A8I8 I8A8
    R8G8B8A8         16384 16384    y  NV12 YV12 UYVY YUYV Y8U8V8A8 V8U8Y8A8 P010 P016 A8I8 I8A8
    R10G10B10A2      16384 16384    y  NV12 YV12 UYVY YUYV Y8U8V8A8 V8U8Y8A8 P010 P016 A8I8 I8A8
    B10G10R10A2      16384 16384    y  NV12 YV12 UYVY YUYV Y8U8V8A8 V8U8Y8A8 P010 P016 A8I8 I8A8

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

##### [6700S]

`user `[`$`]`VDPAU_DRIVER=radeonsi vdpauinfo`

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
    MPEG1                          --- not supported ---
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
    B8G8R8A8         16384 16384    y  NV12 YV12 UYVY YUYV Y8U8V8A8 V8U8Y8A8 P010 P016 A8I8 I8A8
    R8G8B8A8         16384 16384    y  NV12 YV12 UYVY YUYV Y8U8V8A8 V8U8Y8A8 P010 P016 A8I8 I8A8
    R10G10B10A2      16384 16384    y  NV12 YV12 UYVY YUYV Y8U8V8A8 V8U8Y8A8 P010 P016 A8I8 I8A8
    B10G10R10A2      16384 16384    y  NV12 YV12 UYVY YUYV Y8U8V8A8 V8U8Y8A8 P010 P016 A8I8 I8A8

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

#### [Vulkan]

`user `[`$`]`vulkaninfo --summary`

    ==========
    VULKANINFO
    ==========

    Vulkan Instance Version: 1.3.250

    Instance Extensions: count = 22
    -------------------------------
    VK_EXT_acquire_drm_display             : extension revision 1
    VK_EXT_acquire_xlib_display            : extension revision 1
    VK_EXT_debug_report                    : extension revision 10
    VK_EXT_debug_utils                     : extension revision 2
    VK_EXT_direct_mode_display             : extension revision 1
    VK_EXT_display_surface_counter         : extension revision 1
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
    VK_LAYER_KHRONOS_validation Khronos Validation Layer     1.3.250  version 1
    VK_LAYER_MESA_device_select Linux device selection layer 1.3.211  version 1
    VK_LAYER_MESA_overlay       Mesa Overlay layer           1.3.211  version 1

    Devices:
    ========
    GPU0:
        apiVersion         = 1.3.238
        driverVersion      = 23.0.3
        vendorID           = 0x1002
        deviceID           = 0x73ef
        deviceType         = PHYSICAL_DEVICE_TYPE_DISCRETE_GPU
        deviceName         = AMD Radeon RX 6700S (RADV NAVI23)
        driverID           = DRIVER_ID_MESA_RADV
        driverName         = radv
        driverInfo         = Mesa 23.0.3
        conformanceVersion = 1.3.0.0
        deviceUUID         = 00000000-0300-0000-0000-000000000000
        driverUUID         = 414d442d-4d45-5341-2d44-525600000000
    GPU1:
        apiVersion         = 1.3.238
        driverVersion      = 23.0.3
        vendorID           = 0x1002
        deviceID           = 0x1681
        deviceType         = PHYSICAL_DEVICE_TYPE_INTEGRATED_GPU
        deviceName         = AMD Radeon Graphics (RADV REMBRANDT)
        driverID           = DRIVER_ID_MESA_RADV
        driverName         = radv
        driverInfo         = Mesa 23.0.3
        conformanceVersion = 1.3.0.0
        deviceUUID         = 00000000-0700-0000-0000-000000000000
        driverUUID         = 414d442d-4d45-5341-2d44-525600000000

### [GPU monitoring]

Install the [9999](https://wiki.gentoo.org/wiki/Knowledge_Base:Accepting_a_keyword_for_a_single_package "Knowledge Base:Accepting a keyword for a single package") version of [[[app-misc/radeontop]](https://packages.gentoo.org/packages/app-misc/radeontop)[]]. Version 1.4 is from 2021 and will display UNKNOWN_CHIP for the dGPU otherwise.^[\[72\]](#cite_note-72)^

[FILE] **`/etc/portage/package.accept_keywords/package.accept_keywords`**

    app-misc/radeontop   **

It will default to showing the stats for the iGPU. To see dGPU stats, use this command:

`user `[`$`]`radeontop -b 3`

## [See also]

-   [AMD](https://wiki.gentoo.org/wiki/AMD "AMD") --- a semiconductor company. AMD is best known for producing CPUs based on [x86 intruction set](https://en.wikipedia.org/wiki/x86 "wikipedia:x86"), motherboard chipsets and their own line of GPUs.
-   [AMDGPU](https://wiki.gentoo.org/wiki/AMDGPU "AMDGPU") --- the open source graphics drivers for AMD Radeon and other GPUs.
-   [AMDGPU-PRO](https://wiki.gentoo.org/wiki/AMDGPU-PRO "AMDGPU-PRO") --- the next generation *closed source* graphics component that operates on top of the open source [AMDGPU](https://wiki.gentoo.org/wiki/AMDGPU "AMDGPU") drivers for newer AMD/ATI Radeon graphics cards.
-   [AMD microcode](https://wiki.gentoo.org/wiki/AMD_microcode "AMD microcode") --- describes updating the [microcode](https://wiki.gentoo.org/wiki/Microcode "Microcode") for [AMD](https://wiki.gentoo.org/wiki/AMD "AMD") processors.
-   [Dmidecode](https://wiki.gentoo.org/wiki/Dmidecode "Dmidecode") --- a software tool that enables extraction of detailed hardware information from a system by decoding the DMI (Desktop Management Interface) table
-   [GPU passthrough with virt-manager, QEMU, and KVM](https://wiki.gentoo.org/wiki/GPU_passthrough_with_virt-manager,_QEMU,_and_KVM "GPU passthrough with virt-manager, QEMU, and KVM") --- directly present an internal PCI GPU as-is for direct use by a virtual machine
-   [libinput](https://wiki.gentoo.org/wiki/Libinput "Libinput") --- an input device driver for [Wayland compositors](https://wiki.gentoo.org/wiki/Wayland_Desktop_Landscape#Compositors "Wayland Desktop Landscape") and [X.org](https://wiki.gentoo.org/wiki/Xorg "Xorg") window system.
-   [List of software for Wayland](https://wiki.gentoo.org/wiki/List_of_software_for_Wayland "List of software for Wayland") --- various desktop related packages for Wayland
-   [PowerTOP](https://wiki.gentoo.org/wiki/PowerTOP "PowerTOP") --- a Linux utility that can monitor and display a system\'s electrical power usage.
-   [radeon](https://wiki.gentoo.org/wiki/Radeon "Radeon") --- a family of *open source* graphics drivers for *older* AMD/ATI Radeon graphics cards.
-   [ROCm](https://wiki.gentoo.org/wiki/ROCm "ROCm") --- brand name for ROCm open software platform (for software) or the ROCm™ open platform ecosystem
-   [Ryzen](https://wiki.gentoo.org/wiki/Ryzen "Ryzen") --- a multithreaded, high performance processor manufactured by AMD.
-   [synaptics](https://wiki.gentoo.org/wiki/Synaptics "Synaptics") --- the open source input driver for Synaptics and [ALPS](https://wiki.gentoo.org/wiki/Alps_PS/2 "Alps PS/2") touchpads.
-   [VAAPI](https://wiki.gentoo.org/wiki/VAAPI "VAAPI") --- provides access to graphics hardware (GPU) acceleration for video processing.
-   [VDPAU](https://wiki.gentoo.org/wiki/VDPAU "VDPAU") --- how to setup the **V**ideo **D**ecode and **P**resentation **A**PI for **U**nix (VDPAU).
-   [Vulkan](https://wiki.gentoo.org/wiki/Vulkan "Vulkan") --- a next-generation graphics API created by The Khronos Group.
-   [Wayland](https://wiki.gentoo.org/wiki/Wayland "Wayland") --- a [communication protocol](https://en.wikipedia.org/wiki/communication_protocol "wikipedia:communication protocol") between a [display server](https://en.wikipedia.org/wiki/display_server "wikipedia:display server") and its clients
-   [Xorg/Hardware 3D acceleration guide](https://wiki.gentoo.org/wiki/Xorg/Hardware_3D_acceleration_guide "Xorg/Hardware 3D acceleration guide") --- a guide to getting 3D acceleration working using the DRM with Xorg in Gentoo.

## [External resources]

-   [[asusctl](https://gitlab.com/asus-linux/asusctl)] --- A control daemon, CLI tools, and a collection of crates for interacting with ASUS ROG laptops
-   [[https://asus-linux.org/](https://asus-linux.org/)] --- an independent community effort that works to improve Linux support for Asus notebooks
-   [[zGentoo](https://lab.retarded.farm/zappel/zGentoo/-/tree/main/sys-power)] --- ZappeL\'s Gentoo portage overlay: contains ebuilds for asusctl^[\[73\]](#cite_note-73)^ and supergfxctl.
-   [[2022 Zephyrus G14 Fedora Silverblue Setup](https://gist.github.com/jacobranson/adc32b6247f5c19494da0d3a24026d8f)]
-   [[amd-pstate CPU Performance Scaling Driver](https://docs.kernel.org/admin-guide/pm/amd-pstate.html)] --- Huang Rui, 2021.

## [References]

1.  [[[↑](#cite_ref-1)] [ Advanced Micro Devices, Inc., [AMD Advantage Gaming Laptops](https://www.amd.com/en/gaming/advantage-laptops), [amd.com](https://www.amd.com/en.html) 2022, Retrieved on October 8th, 2023.]]
2.  [[[↑](#cite_ref-2)] [Advanced Micro Devices, Inc., [AMD SmartShift Technology](https://www.amd.com/en/technologies/smartshift), [amd.com](https://www.amd.com/en.html) 2020, Retrieved on October 28th, 2023.]]
3.  [[[↑](#cite_ref-3)] [Advanced Micro Devices, Inc., [AMD Smart Technologies](https://www.amd.com/en/gaming/technologies/smart-technologies.html), [amd.com](https://www.amd.com/en.html) 2023, Retrieved on December 19th, 2023.]]
4.  [[[↑](#cite_ref-4)] [Advanced Micro Devices, Inc., [AMD Radeon™ RX 6700S Mobile Graphics](https://www.amd.com/en/products/graphics/amd-radeon-rx-6700s), [amd.com](https://www.amd.com/en.html) 2022, Retrieved on December 19th, 2023.]]
5.  [[[↑](#cite_ref-5)] [Advanced Micro Devices, Inc., [AMD Radeon™ RX 6800S Mobile Graphics](https://www.amd.com/en/products/graphics/amd-radeon-rx-6800s), [amd.com](https://www.amd.com/en.html) 2022, Retrieved on December 19th, 2023.]]
6.  [[[↑](#cite_ref-gpuwiki_6-0)] [Wikipedia, [Radeon RX 6000 series#Mobile](https://en.wikipedia.org/wiki/Radeon_RX_6000_series#Mobile), [wikipedia.org](https://en.wikipedia.org/wiki/Main_Page) 2021, Retrieved on December 19th, 2023.]]
7.  [[[↑](#cite_ref-7)] [The PCI ID Repository, [Advanced Micro Devices, Inc. (ATI)](https://admin.pci-ids.ucw.cz/read/PC/1002), [https://pci-ids.ucw.cz/](https://admin.pci-ids.ucw.cz/) 2024, Retrieved on August 12th, 2024.]]
8.  [[[↑](#cite_ref-8)] [The PCI ID Repository, [Advanced Micro Devices, Inc. (AMD)](https://admin.pci-ids.ucw.cz/read/PC/1022), [https://pci-ids.ucw.cz/](https://admin.pci-ids.ucw.cz/) 2024, Retrieved on August 12th, 2024.]]
9.  [[[↑](#cite_ref-amdcpu_9-0)] [[https://www.amd.com/en/product/11561](https://www.amd.com/en/product/11561)]]
10. [[[↑](#cite_ref-10)] [[https://bsd-hardware.info/?id=cpu:amd-25-68-1-ryzen-9-6900hs-with-radeon-graphics](https://bsd-hardware.info/?id=cpu:amd-25-68-1-ryzen-9-6900hs-with-radeon-graphics)]]
11. [[[↑](#cite_ref-11)] [[https://www.techpowerup.com/cpu-specs/ryzen-9-6900hs.c2528](https://www.techpowerup.com/cpu-specs/ryzen-9-6900hs.c2528)]]
12. [[[↑](#cite_ref-12)] [[https://www.phoronix.com/news/AMDGPU-Yellow-Carp-FW](https://www.phoronix.com/news/AMDGPU-Yellow-Carp-FW)]]
13. [[[↑](#cite_ref-13)] [[https://www.phoronix.com/review/amd-radeon-680m](https://www.phoronix.com/review/amd-radeon-680m)]]
14. [[[↑](#cite_ref-14)] [[https://git.kernel.org/pub/scm/linux/kernel/git/firmware/linux-firmware.git/commit/?id=198ac651f46b7d4efd660a1f5ab4f93ca422947d](https://git.kernel.org/pub/scm/linux/kernel/git/firmware/linux-firmware.git/commit/?id=198ac651f46b7d4efd660a1f5ab4f93ca422947d)]]
15. [[[↑](#cite_ref-15)] [[https://lore.kernel.org/all/bug-219468-2300@https.bugzilla.kernel.org%2F/T/](https://lore.kernel.org/all/bug-219468-2300@https.bugzilla.kernel.org%2F/T/)]]
16. [[[↑](#cite_ref-16)] [[https://gitlab.freedesktop.org/drm/amd/-/issues/3743](https://gitlab.freedesktop.org/drm/amd/-/issues/3743)]]
17. [[[↑](#cite_ref-17)] [[https://gitlab.freedesktop.org/drm/amd/-/issues/3651](https://gitlab.freedesktop.org/drm/amd/-/issues/3651)]]
18. [[[↑](#cite_ref-18)] [[https://admin.pci-ids.ucw.cz//read/PC/1002/73ef](https://admin.pci-ids.ucw.cz//read/PC/1002/73ef)]]
19. [[[↑](#cite_ref-19)] [[https://cateee.net/lkddb/web-lkddb/DRM_AMDGPU.html](https://cateee.net/lkddb/web-lkddb/DRM_AMDGPU.html)]]
20. [[[↑](#cite_ref-20)] [[https://www.phoronix.com/news/AMDGPU-Dimgrey-Cavefish](https://www.phoronix.com/news/AMDGPU-Dimgrey-Cavefish)]]
21. [[[↑](#cite_ref-21)] [[https://www.phoronix.com/news/Mesa-20.3-Released](https://www.phoronix.com/news/Mesa-20.3-Released)]]
22. [[[↑](#cite_ref-22)] [[https://admin.pci-ids.ucw.cz/read/PC/1002/1478](https://admin.pci-ids.ucw.cz/read/PC/1002/1478)]]
23. [[[↑](#cite_ref-23)] [[https://admin.pci-ids.ucw.cz/read/PC/1002/1479](https://admin.pci-ids.ucw.cz/read/PC/1002/1479)]]
24. [[[↑](#cite_ref-24)] [[https://www.phoronix.com/news/Linux-Disables-RNG-AMD-fTPMs](https://www.phoronix.com/news/Linux-Disables-RNG-AMD-fTPMs)]]
25. [[[↑](#cite_ref-25)] [[https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/commit/?id=554b841d470338a3b1d6335b14ee1cd0c8f5d754](https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/commit/?id=554b841d470338a3b1d6335b14ee1cd0c8f5d754)]]
26. [[[↑](#cite_ref-26)] [[https://bugzilla.kernel.org/show_bug.cgi?id=217719](https://bugzilla.kernel.org/show_bug.cgi?id=217719)]]
27. [[[↑](#cite_ref-27)] [[https://rog.asus.com/uk/support/FAQ/1049059](https://rog.asus.com/uk/support/FAQ/1049059)]]
28. [[[↑](#cite_ref-28)] [[https://linux-hardware.org/?id=usb:13d3-56eb](https://linux-hardware.org/?id=usb:13d3-56eb)]]
29. [[[↑](#cite_ref-29)] [[https://linux-hardware.org/?id=ps/2:04f3-319b-asue120a-00-04f3-319b-mouse](https://linux-hardware.org/?id=ps/2:04f3-319b-asue120a-00-04f3-319b-mouse)]]
30. [[[↑](#cite_ref-30)] [[https://stackoverflow.com/questions/52713940/purpose-of-address-spaced-identifiersasids](https://stackoverflow.com/questions/52713940/purpose-of-address-spaced-identifiersasids)]]
31. [[[↑](#cite_ref-31)] [[https://www.rtings.com/laptop/reviews/asus/rog-zephyrus-g14-2022](https://www.rtings.com/laptop/reviews/asus/rog-zephyrus-g14-2022)]]
32. [[[↑](#cite_ref-32)] [[https://www.tomsguide.com/reviews/asus-rog-zephyrus-g14-2022](https://www.tomsguide.com/reviews/asus-rog-zephyrus-g14-2022)]]
33. [[[↑](#cite_ref-33)] [[https://www.corsair.com/us/en/p/memory/cmsx32gx5m1a4800c40/vengeance-ddr5-sodimm-32gb-1x32gb-ddr5-4800-pc5-38400-c40-1-1v-cmsx32gx5m1a4800c40](https://www.corsair.com/us/en/p/memory/cmsx32gx5m1a4800c40/vengeance-ddr5-sodimm-32gb-1x32gb-ddr5-4800-pc5-38400-c40-1-1v-cmsx32gx5m1a4800c40)]]
34. [[[↑](#cite_ref-34)] [[https://www.anker.com/products/a8866](https://www.anker.com/products/a8866)]]
35. [[[↑](#cite_ref-35)] [[https://www.anker.com/products/a8388](https://www.anker.com/products/a8388)]]
36. [[[↑](#cite_ref-36)] [ASIX Electronics Corp. AX88179 Gigabit Ethernet]]
37. [[[↑](#cite_ref-37)] [Norelsys NS1081]]
38. [[[↑](#cite_ref-38)] [VIA Labs, Inc. USB 3.1 Hub]]
39. [[[↑](#cite_ref-39)] [Super Top 4-Port hub]]
40. [[[↑](#cite_ref-40)] [VIA Labs, Inc. USB 2.0 Hub]]
41. [[[↑](#cite_ref-41)] [[https://www.anker.com/products/a2148](https://www.anker.com/products/a2148)]]
42. [[[↑](#cite_ref-42)] [[https://forums.virtualbox.org/viewtopic.php?t=112580](https://forums.virtualbox.org/viewtopic.php?t=112580)]]
43. [[[↑](#cite_ref-43)] [[https://bbs.archlinux.org/viewtopic.php?id=301155](https://bbs.archlinux.org/viewtopic.php?id=301155)]]
44. [[[↑](#cite_ref-44)] [[https://www.phoronix.com/news/AMD-P-State-Active-Default](https://www.phoronix.com/news/AMD-P-State-Active-Default)]]
45. [[[↑](#cite_ref-45)] [[https://gitlab.com/asus-linux/asusctl/-/issues/93](https://gitlab.com/asus-linux/asusctl/-/issues/93)]]
46. [[[↑](#cite_ref-46)] [[https://forums.gentoo.org/viewtopic-p-8688242.html](https://forums.gentoo.org/viewtopic-p-8688242.html)]]
47. [[[↑](#cite_ref-47)] [[https://rog.asus.com/laptops/rog-zephyrus/rog-zephyrus-g14-2022-series/helpdesk_bios/](https://rog.asus.com/laptops/rog-zephyrus/rog-zephyrus-g14-2022-series/helpdesk_bios/)]]
48. [[[↑](#cite_ref-48)] [[https://photon-reddit.com/r/ZephyrusG14/comments/x0jmc8/bios_313_a_survivors_guide/](https://photon-reddit.com/r/ZephyrusG14/comments/x0jmc8/bios_313_a_survivors_guide/)]]
49. [[[↑](#cite_ref-49)] [[https://uefi.org/revocationlistfile](https://uefi.org/revocationlistfile)]]
50. [[[↑](#cite_ref-50)] [[https://github.com/hyprwm/hyprland-wiki/pull/721/files/6913c30e17d421ad0a33805004b542da92fa775a](https://github.com/hyprwm/hyprland-wiki/pull/721/files/6913c30e17d421ad0a33805004b542da92fa775a)]]
51. [[[↑](#cite_ref-51)] [[https://docstore.mik.ua/orelly/unix3/upt/ch06_02.htm](https://docstore.mik.ua/orelly/unix3/upt/ch06_02.htm)]]
52. [[[↑](#cite_ref-52)] [[https://github.com/jwrdegoede/wev](https://github.com/jwrdegoede/wev)]]
53. [[[↑](#cite_ref-53)] [[https://www.oreilly.com/library/view/xlib-reference-manual/9780937175262/16_appendix-h.html](https://www.oreilly.com/library/view/xlib-reference-manual/9780937175262/16_appendix-h.html)]]
54. [[[↑](#cite_ref-54)] [[https://www.cl.cam.ac.uk/\~mgk25/ucs/keysymdef.h](https://www.cl.cam.ac.uk/~mgk25/ucs/keysymdef.h)]]
55. [[[↑](#cite_ref-55)] [[https://www.geeksforgeeks.org/showkey-command-in-linux-with-examples/](https://www.geeksforgeeks.org/showkey-command-in-linux-with-examples/)]]
56. [[[↑](#cite_ref-56)] [[https://community.kde.org/KWin/Environment_Variables](https://community.kde.org/KWin/Environment_Variables)]]
57. [[[↑](#cite_ref-57)] [[https://linrunner.de/tlp/index.html](https://linrunner.de/tlp/index.html)]]
58. [[[↑](#cite_ref-58)] [[https://gitlab.freedesktop.org/drm/amd/-/issues/2068](https://gitlab.freedesktop.org/drm/amd/-/issues/2068)]]
59. [[[↑](#cite_ref-59)] [[https://unix.stackexchange.com/questions/517689/btrfs-bad-tree-block-start-prevents-mount-and-repair](https://unix.stackexchange.com/questions/517689/btrfs-bad-tree-block-start-prevents-mount-and-repair)]]
60. [[[↑](#cite_ref-60)] [[https://forum.rockstor.com/t/btrfs-wont-mount-says-open-ctree-failed/3122/2](https://forum.rockstor.com/t/btrfs-wont-mount-says-open-ctree-failed/3122/2)]]
61. [[[↑](#cite_ref-61)] [[https://forums.opensuse.org/t/btrfs-error-cant-read-tree-root-bad-tree-blcok-start/147355/7](https://forums.opensuse.org/t/btrfs-error-cant-read-tree-root-bad-tree-blcok-start/147355/7)]]
62. [[[↑](#cite_ref-62)] [[https://docs.amd.com/en/latest/release/gpu_os_support.html](https://docs.amd.com/en/latest/release/gpu_os_support.html)]]
63. [[[↑](#cite_ref-63)] [[https://github.com/RadeonOpenCompute/ROCm/issues/1756](https://github.com/RadeonOpenCompute/ROCm/issues/1756)]]
64. [[[↑](#cite_ref-64)] [[https://www.techpowerup.com/gpu-specs/radeon-rx-6700s.c3868](https://www.techpowerup.com/gpu-specs/radeon-rx-6700s.c3868)]]
65. [[[↑](#cite_ref-65)] [[https://www.techpowerup.com/gpu-specs/radeon-680m.c3871](https://www.techpowerup.com/gpu-specs/radeon-680m.c3871)]]
66. [[[↑](#cite_ref-66)] [[https://bugs.gentoo.org/906222](https://bugs.gentoo.org/906222)]]
67. [[[↑](#cite_ref-67)] [[https://lore.kernel.org/lkml/CAF9VpL4ZavjF9pwbRC_mj7+YAajgCJXTBdnnwNK3gHSS2VUxYw@mail.gmail.com/T/](https://lore.kernel.org/lkml/CAF9VpL4ZavjF9pwbRC_mj7+YAajgCJXTBdnnwNK3gHSS2VUxYw@mail.gmail.com/T/)]]
68. [[[↑](#cite_ref-68)] [[https://lore.kernel.org/lkml/20220909180509.638-1-mario.limonciello@amd.com/](https://lore.kernel.org/lkml/20220909180509.638-1-mario.limonciello@amd.com/)]]
69. [[[↑](#cite_ref-69)] [[https://gitlab.com/marcaux/g14-2021-s3-dsdt](https://gitlab.com/marcaux/g14-2021-s3-dsdt)]]
70. [[[↑](#cite_ref-70)] [[https://opencl.gpuinfo.org/listreports.php?devicename=gfx1032&platform=](https://opencl.gpuinfo.org/listreports.php?devicename=gfx1032&platform=)]]
71. [[[↑](#cite_ref-71)] [[https://opencl.gpuinfo.org/listreports.php?devicename=gfx1035&platform=](https://opencl.gpuinfo.org/listreports.php?devicename=gfx1035&platform=)]]
72. [[[↑](#cite_ref-72)] [[https://github.com/clbr/radeontop/issues/133](https://github.com/clbr/radeontop/issues/133)]]
73. [[[↑](#cite_ref-73)] [[https://bugs.gentoo.org/827002](https://bugs.gentoo.org/827002)]]