**Resources**

[[]][Product Information](https://www.lenovo.com/us/en/p/laptops/thinkpad/thinkpadp/thinkpad-p16v-16-inch-amd-mobile-workstation/len101t0074)

[[]][Official Support Page](https://pcsupport.lenovo.com/us/en/products/laptops-and-netbooks/thinkpad-p-series-laptops/thinkpad-p16v-gen-1-type-21fe-21ff/21ff/21ffs17201/)

[[]][Specifications](https://psref.lenovo.com/syspool/Sys/PDF/ThinkPad/ThinkPad_P16v_Gen_1_AMD/ThinkPad_P16v_Gen_1_AMD_Spec.pdf)

[[]][Specifications (by region)](https://psref.lenovo.com/Product/ThinkPad/ThinkPad_P16v_Gen_1_AMD?tab=model)

[[]][Hardware Maintenance Manual](https://download.lenovo.com/pccbbs/mobiles_pdf/p16v_gen1_hmm_en.pdf)

[[]][User Guide](https://download.lenovo.com/pccbbs/mobiles_pdf/p16v_gen1_ug_en.pdf)

The **Lenovo ThinkPad P16v Gen 1 (AMD)** is a 16-inch laptop released in July 2023. ^[\[1\]](#cite_note-1)^

## Contents

-   [[1] [Hardware]](#Hardware)
    -   [[1.1] [Standard]](#Standard)
    -   [[1.2] [Detailed information]](#Detailed_information)
-   [[2] [References]](#References)

## [Hardware]

### [Standard]

  ------------------------- ------------------------------------------------------------------- -------- ------------------------ ------------------- ---------------- -------
  Device                    Make/model                                                          Status   Vendor ID / Product ID   Kernel driver(s)    Kernel version   Notes
  CPU                       AMD Ryzen™ 9 PRO 7940HS                                             Works    N/A                      N/A                 6.6.41
  Video Card                AMD Radeon™ 780M                                                    Works    pci:1002:15bf            amdgpu              6.6.41
  Video Card                NVIDIA® RTX 2000 Ada Generation Laptop GPU                          Works    pci:10de:28b8            nvidia              6.6.41
  Wireless & Bluetooth      Qualcomm® Wi-Fi® 6E NFA725A, 802.11ax 2x2 Wi-Fi® + Bluetooth® 5.3   Works    pci:17cb:1103            ath11k_pci          6.6.41
  Sound                     AMD Rembrandt Radeon High Definition Audio                          Works    pci:1002:1640            snd_hda_intel       6.6.41
  Touchpad and trackpoint   Synaptics, Inc                                                      Works    usb:06cb:0126            Synaptics related   6.6.41
  Webcam                    Chicony Electronics Co., Ltd Integrated Camera                      Works    usb:04f2:b7bf            uvcvideo            6.6.41
  ------------------------- ------------------------------------------------------------------- -------- ------------------------ ------------------- ---------------- -------

### [Detailed information]

`root `[`#`]`dmidecode -s system-version`

    ThinkPad P16v Gen 1

`root `[`#`]`uname -r`

    6.6.41-gentoo-dist

`root `[`#`]`lscpu`

    Architecture:             x86_64
      CPU op-mode(s):         32-bit, 64-bit
      Address sizes:          48 bits physical, 48 bits virtual
      Byte Order:             Little Endian
    CPU(s):                   16
      On-line CPU(s) list:    0-15
    Vendor ID:                AuthenticAMD
      BIOS Vendor ID:         Advanced Micro Devices, Inc.
      Model name:             AMD Ryzen 9 PRO 7940HS w/ Radeon 780M Graphics
        BIOS Model name:      AMD Ryzen 9 PRO 7940HS w/ Radeon 780M Graphics  None CPU @ 4.0GHz
        BIOS CPU family:      107
        CPU family:           25
        Model:                116
        Thread(s) per core:   2
        Core(s) per socket:   8
        Socket(s):            1
        Stepping:             1
        CPU(s) scaling MHz:   48%
        CPU max MHz:          6228.0000
        CPU min MHz:          400.0000
        BogoMIPS:             7988.64
        Flags:                fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush mmx fxsr sse sse2 ht syscall nx mmxext fxsr_opt pdpe1gb rdtscp lm constant_tsc rep_good amd_lb
                              r_v2 nopl nonstop_tsc cpuid extd_apicid aperfmperf rapl pni pclmulqdq monitor ssse3 fma cx16 sse4_1 sse4_2 x2apic movbe popcnt aes xsave avx f16c rdrand lahf_lm cmp_legacy sv
                              m extapic cr8_legacy abm sse4a misalignsse 3dnowprefetch osvw ibs skinit wdt tce topoext perfctr_core perfctr_nb bpext perfctr_llc mwaitx cpb cat_l3 cdp_l3 hw_pstate ssbd mba
                               perfmon_v2 ibrs ibpb stibp ibrs_enhanced vmmcall fsgsbase bmi1 avx2 smep bmi2 erms invpcid cqm rdt_a avx512f avx512dq rdseed adx smap avx512ifma clflushopt clwb avx512cd sha
                              _ni avx512bw avx512vl xsaveopt xsavec xgetbv1 xsaves cqm_llc cqm_occup_llc cqm_mbm_total cqm_mbm_local user_shstk avx512_bf16 clzero irperf xsaveerptr rdpru wbnoinvd cppc ara
                              t npt lbrv svm_lock nrip_save tsc_scale vmcb_clean flushbyasid decodeassists pausefilter pfthreshold v_vmsave_vmload vgif x2avic v_spec_ctrl vnmi avx512vbmi umip pku ospke av
                              x512_vbmi2 gfni vaes vpclmulqdq avx512_vnni avx512_bitalg avx512_vpopcntdq rdpid overflow_recov succor smca flush_l1d amd_lbr_pmc_freeze
    Virtualization features:
      Virtualization:         AMD-V
    Caches (sum of all):
      L1d:                    256 KiB (8 instances)
      L1i:                    256 KiB (8 instances)
      L2:                     8 MiB (8 instances)
      L3:                     16 MiB (1 instance)
    NUMA:
      NUMA node(s):           1
      NUMA node0 CPU(s):      0-15
    Vulnerabilities:
      Gather data sampling:   Not affected
      Itlb multihit:          Not affected
      L1tf:                   Not affected
      Mds:                    Not affected
      Meltdown:               Not affected
      Mmio stale data:        Not affected
      Reg file data sampling: Not affected
      Retbleed:               Not affected
      Spec rstack overflow:   Vulnerable: Safe RET, no microcode
      Spec store bypass:      Mitigation; Speculative Store Bypass disabled via prctl
      Spectre v1:             Mitigation; usercopy/swapgs barriers and __user pointer sanitization
      Spectre v2:             Mitigation; Enhanced / Automatic IBRS; IBPB conditional; STIBP always-on; RSB filling; PBRSB-eIBRS Not affected; BHI Not affected
      Srbds:                  Not affected
      Tsx async abort:        Not affected

`root `[`#`]`dmidecode -t 2,17`

    # dmidecode 3.6
    Getting SMBIOS data from sysfs.
    SMBIOS 3.3.0 present.

    Handle 0x0008, DMI type 17, 92 bytes
    Memory Device
        Array Handle: 0x0005
        Error Information Handle: 0x0007
        Total Width: 64 bits
        Data Width: 64 bits
        Size: 32 GB
        Form Factor: SODIMM
        Set: None
        Locator: DIMM 0
        Bank Locator: P0 CHANNEL A
        Type: DDR5
        Type Detail: Synchronous Unbuffered (Unregistered)
        Speed: 5600 MT/s
        Manufacturer: Kingston
        Serial Number: XXXXXXXXXXX
        Asset Tag: Not Specified
        Part Number: KF556S40-32
        Rank: 2
        Configured Memory Speed: 5600 MT/s
        Minimum Voltage: 1.1 V
        Maximum Voltage: 1.1 V
        Configured Voltage: 1.1 V
        Memory Technology: DRAM
        Memory Operating Mode Capability: Volatile memory
        Firmware Version: Unknown
        Module Manufacturer ID: Bank 2, Hex 0x98
        Module Product ID: Unknown
        Memory Subsystem Controller Manufacturer ID: Unknown
        Memory Subsystem Controller Product ID: Unknown
        Non-Volatile Size: None
        Volatile Size: 32 GB
        Cache Size: None
        Logical Size: None

    Handle 0x000B, DMI type 17, 92 bytes
    Memory Device
        Array Handle: 0x0005
        Error Information Handle: 0x000A
        Total Width: 64 bits
        Data Width: 64 bits
        Size: 32 GB
        Form Factor: SODIMM
        Set: None
        Locator: DIMM 0
        Bank Locator: P0 CHANNEL B
        Type: DDR5
        Type Detail: Synchronous Unbuffered (Unregistered)
        Speed: 5600 MT/s
        Manufacturer: Kingston
        Serial Number: XXXXXXXXXXX
        Asset Tag: Not Specified
        Part Number: KF556S40-32
        Rank: 2
        Configured Memory Speed: 5600 MT/s
        Minimum Voltage: 1.1 V
        Maximum Voltage: 1.1 V
        Configured Voltage: 1.1 V
        Memory Technology: DRAM
        Memory Operating Mode Capability: Volatile memory
        Firmware Version: Unknown
        Module Manufacturer ID: Bank 2, Hex 0x98
        Module Product ID: Unknown
        Memory Subsystem Controller Manufacturer ID: Unknown
        Memory Subsystem Controller Product ID: Unknown
        Non-Volatile Size: None
        Volatile Size: 32 GB
        Cache Size: None
        Logical Size: None

    Handle 0x0011, DMI type 2, 15 bytes
    Base Board Information
        Manufacturer: LENOVO
        Product Name: 21FFS17201
        Version: Not Defined
        Serial Number: XXXXXXXXXXX
        Asset Tag: Not Available
        Features:
            Board is a hosting board
            Board is replaceable
        Location In Chassis: Not Available
        Chassis Handle: 0x0012
        Type: Motherboard
        Contained Object Handles: 0

** Note**\
The original RAM sticks have been replaced to max out the memory.

`root `[`#`]`lspci -nnk`

    00:00.0 Host bridge [0600]: Advanced Micro Devices, Inc. [AMD] Device [1022:14e8]
        Subsystem: Lenovo Device [17aa:231c]
    00:00.2 IOMMU [0806]: Advanced Micro Devices, Inc. [AMD] Device [1022:14e9]
        Subsystem: Lenovo Device [17aa:231c]
    00:01.0 Host bridge [0600]: Advanced Micro Devices, Inc. [AMD] Device [1022:14ea]
    00:01.1 PCI bridge [0604]: Advanced Micro Devices, Inc. [AMD] Device [1022:14ed]
        Subsystem: Lenovo Device [17aa:231c]
        Kernel driver in use: pcieport
    00:01.2 PCI bridge [0604]: Advanced Micro Devices, Inc. [AMD] Device [1022:14ed]
        Subsystem: Lenovo Device [17aa:231c]
        Kernel driver in use: pcieport
    00:02.0 Host bridge [0600]: Advanced Micro Devices, Inc. [AMD] Device [1022:14ea]
    00:02.2 PCI bridge [0604]: Advanced Micro Devices, Inc. [AMD] Device [1022:14ee]
        Subsystem: Lenovo Device [17aa:231c]
        Kernel driver in use: pcieport
    00:02.3 PCI bridge [0604]: Advanced Micro Devices, Inc. [AMD] Device [1022:14ee]
        Subsystem: Lenovo Device [17aa:231c]
        Kernel driver in use: pcieport
    00:02.4 PCI bridge [0604]: Advanced Micro Devices, Inc. [AMD] Device [1022:14ee]
        Subsystem: Lenovo Device [17aa:231c]
        Kernel driver in use: pcieport
    00:03.0 Host bridge [0600]: Advanced Micro Devices, Inc. [AMD] Device [1022:14ea]
    00:03.1 PCI bridge [0604]: Advanced Micro Devices, Inc. [AMD] Family 19h USB4/Thunderbolt PCIe tunnel [1022:14ef]
        Subsystem: Advanced Micro Devices, Inc. [AMD] Device [1022:1453]
        Kernel driver in use: pcieport
    00:04.0 Host bridge [0600]: Advanced Micro Devices, Inc. [AMD] Device [1022:14ea]
    00:04.1 PCI bridge [0604]: Advanced Micro Devices, Inc. [AMD] Family 19h USB4/Thunderbolt PCIe tunnel [1022:14ef]
        Subsystem: Advanced Micro Devices, Inc. [AMD] Device [1022:1453]
        Kernel driver in use: pcieport
    00:08.0 Host bridge [0600]: Advanced Micro Devices, Inc. [AMD] Device [1022:14ea]
    00:08.1 PCI bridge [0604]: Advanced Micro Devices, Inc. [AMD] Device [1022:14eb]
        Subsystem: Lenovo Device [17aa:231c]
        Kernel driver in use: pcieport
    00:08.2 PCI bridge [0604]: Advanced Micro Devices, Inc. [AMD] Device [1022:14eb]
        Subsystem: Lenovo Device [17aa:231c]
        Kernel driver in use: pcieport
    00:08.3 PCI bridge [0604]: Advanced Micro Devices, Inc. [AMD] Device [1022:14eb]
    pcilib: Error reading /sys/bus/pci/devices/0000:00:08.3/label: Operation not permitted
        Subsystem: Lenovo Device [17aa:231c]
        Kernel driver in use: pcieport
    00:14.0 SMBus [0c05]: Advanced Micro Devices, Inc. [AMD] FCH SMBus Controller [1022:790b] (rev 71)
        Subsystem: Lenovo Device [17aa:231c]
        Kernel driver in use: piix4_smbus
        Kernel modules: i2c_piix4, sp5100_tco
    00:14.3 ISA bridge [0601]: Advanced Micro Devices, Inc. [AMD] FCH LPC Bridge [1022:790e] (rev 51)
        Subsystem: Lenovo Device [17aa:231c]
    00:18.0 Host bridge [0600]: Advanced Micro Devices, Inc. [AMD] Device [1022:14f0]
    00:18.1 Host bridge [0600]: Advanced Micro Devices, Inc. [AMD] Device [1022:14f1]
    00:18.2 Host bridge [0600]: Advanced Micro Devices, Inc. [AMD] Device [1022:14f2]
    00:18.3 Host bridge [0600]: Advanced Micro Devices, Inc. [AMD] Device [1022:14f3]
        Kernel driver in use: k10temp
        Kernel modules: k10temp
    00:18.4 Host bridge [0600]: Advanced Micro Devices, Inc. [AMD] Device [1022:14f4]
    00:18.5 Host bridge [0600]: Advanced Micro Devices, Inc. [AMD] Device [1022:14f5]
    00:18.6 Host bridge [0600]: Advanced Micro Devices, Inc. [AMD] Device [1022:14f6]
    00:18.7 Host bridge [0600]: Advanced Micro Devices, Inc. [AMD] Device [1022:14f7]
    01:00.0 3D controller [0302]: NVIDIA Corporation AD107GLM [RTX 2000 Ada Generation Laptop GPU] [10de:28b8] (rev a1)
        Subsystem: Lenovo Device [17aa:231d]
        Kernel driver in use: nvidia
        Kernel modules: nouveau, nvidia_drm, nvidia
    02:00.0 Non-Volatile memory controller [0108]: Samsung Electronics Co Ltd NVMe SSD Controller S4LV008[Pascal] [144d:a80c]
        Subsystem: Samsung Electronics Co Ltd Device [144d:a801]
        Kernel driver in use: nvme
        Kernel modules: nvme
    03:00.0 Network controller [0280]: Qualcomm Technologies, Inc QCNFA765 Wireless Network Adapter [17cb:1103] (rev 01)
        Subsystem: Lenovo Device [17aa:9309]
        Kernel driver in use: ath11k_pci
        Kernel modules: ath11k_pci
    04:00.0 Unassigned class [ff00]: Realtek Semiconductor Co., Ltd. RTS5261 PCI Express Card Reader [10ec:5261] (rev 01)
        Subsystem: Lenovo Device [17aa:231c]
        Kernel driver in use: rtsx_pci
        Kernel modules: rtsx_pci
    05:00.0 Non-Volatile memory controller [0108]: Samsung Electronics Co Ltd NVMe SSD Controller PM9A1/PM9A3/980PRO [144d:a80a]
        Subsystem: Samsung Electronics Co Ltd SSD 980 PRO [144d:a801]
        Kernel driver in use: nvme
        Kernel modules: nvme
    c6:00.0 VGA compatible controller [0300]: Advanced Micro Devices, Inc. [AMD/ATI] Phoenix1 [1002:15bf] (rev d3)
        Subsystem: Lenovo Device [17aa:231d]
        Kernel driver in use: amdgpu
        Kernel modules: amdgpu
    c6:00.1 Audio device [0403]: Advanced Micro Devices, Inc. [AMD/ATI] Rembrandt Radeon High Definition Audio Controller [1002:1640]
        Subsystem: Lenovo Device [17aa:231c]
        Kernel driver in use: snd_hda_intel
        Kernel modules: snd_hda_intel
    c6:00.2 Encryption controller [1080]: Advanced Micro Devices, Inc. [AMD] Family 19h (Model 74h) CCP/PSP 3.0 Device [1022:15c7]
        Subsystem: Lenovo Device [17aa:231c]
        Kernel driver in use: ccp
        Kernel modules: ccp
    c6:00.3 USB controller [0c03]: Advanced Micro Devices, Inc. [AMD] Device [1022:15b9]
        Subsystem: Lenovo Device [17aa:231c]
        Kernel driver in use: xhci_hcd
    c6:00.4 USB controller [0c03]: Advanced Micro Devices, Inc. [AMD] Device [1022:15ba]
        Subsystem: Lenovo Device [17aa:231c]
        Kernel driver in use: xhci_hcd
    c6:00.5 Multimedia controller [0480]: Advanced Micro Devices, Inc. [AMD] ACP/ACP3X/ACP6x Audio Coprocessor [1022:15e2] (rev 63)
        Subsystem: Lenovo Device [17aa:231c]
        Kernel driver in use: snd_pci_ps
        Kernel modules: snd_pci_acp3x, snd_rn_pci_acp3x, snd_pci_acp5x, snd_pci_acp6x, snd_rpl_pci_acp6x, snd_pci_ps, snd_sof_amd_renoir, snd_sof_amd_rembrandt, snd_sof_amd_vangogh
    c6:00.6 Audio device [0403]: Advanced Micro Devices, Inc. [AMD] Family 17h/19h HD Audio Controller [1022:15e3]
        Subsystem: Lenovo Device [17aa:231c]
        Kernel driver in use: snd_hda_intel
        Kernel modules: snd_hda_intel
    c7:00.0 Non-Essential Instrumentation [1300]: Advanced Micro Devices, Inc. [AMD] Device [1022:14ec]
        Subsystem: Lenovo Device [17aa:231c]
    c7:00.1 Signal processing controller [1180]: Advanced Micro Devices, Inc. [AMD] AMD IPU Device [1022:1502]
        Subsystem: Lenovo Device [17aa:231c]
    c8:00.0 Non-Essential Instrumentation [1300]: Advanced Micro Devices, Inc. [AMD] Device [1022:14ec]
        Subsystem: Lenovo Device [17aa:231c]
    c8:00.3 USB controller [0c03]: Advanced Micro Devices, Inc. [AMD] Device [1022:15c0]
        Subsystem: Lenovo Device [17aa:231c]
        Kernel driver in use: xhci_hcd
    c8:00.4 USB controller [0c03]: Advanced Micro Devices, Inc. [AMD] Device [1022:15c1]
        Subsystem: Lenovo Device [17aa:231c]
        Kernel driver in use: xhci_hcd
    c8:00.5 USB controller [0c03]: Advanced Micro Devices, Inc. [AMD] Pink Sardine USB4/Thunderbolt NHI controller #1 [1022:1668]
        Subsystem: Lenovo Device [17aa:231c]
        Kernel driver in use: thunderbolt
        Kernel modules: thunderbolt
    c8:00.6 USB controller [0c03]: Advanced Micro Devices, Inc. [AMD] Pink Sardine USB4/Thunderbolt NHI controller #2 [1022:1669]
        Subsystem: Lenovo Device [17aa:231c]
        Kernel driver in use: thunderbolt
        Kernel modules: thunderbolt

** Note**\
The second SSD was installed after purchase, the laptop shipped with only one.

`root `[`#`]`lsusb`

    Bus 001 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub
    Bus 001 Device 003: ID 10ab:9309 USI Co., Ltd
    Bus 001 Device 015: ID 06cb:0126 Synaptics, Inc.
    Bus 002 Device 001: ID 1d6b:0003 Linux Foundation 3.0 root hub
    Bus 003 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub
    Bus 003 Device 002: ID 04f2:b7bf Chicony Electronics Co., Ltd Integrated Camera
    Bus 004 Device 001: ID 1d6b:0003 Linux Foundation 3.0 root hub
    Bus 005 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub
    Bus 005 Device 008: ID 17ef:30ba Lenovo V1003
    Bus 005 Device 009: ID 17ef:30b4 Lenovo ThinkPad Thunderbolt 4 Dock MCU Controller2
    Bus 005 Device 010: ID 17ef:30b5 Lenovo 40B0
    Bus 005 Device 012: ID 17ef:30b7 Lenovo USB2.0 Hub
    Bus 005 Device 013: ID 17ef:30b9 Lenovo USB2.0 Hub
    Bus 005 Device 015: ID 17ef:30bb Lenovo ThinkPad Thunderbolt 4 Dock USB Audio
    Bus 006 Device 001: ID 1d6b:0003 Linux Foundation 3.0 root hub
    Bus 006 Device 007: ID 8087:0b40 Intel Corp. USB3.0 Hub
    Bus 006 Device 008: ID 0bda:8156 Realtek Semiconductor Corp. Lenovo 2.5G C to RJ45
    Bus 006 Device 009: ID 17ef:30b6 Lenovo USB3.1 Hub
    Bus 006 Device 010: ID 17ef:30b8 Lenovo USB3.1 Hub
    Bus 006 Device 011: ID 0bda:8153 Realtek Semiconductor Corp. RTL8153 Gigabit Ethernet Adapter
    Bus 007 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub
    Bus 008 Device 001: ID 1d6b:0003 Linux Foundation 3.0 root hub

** Note**\
The dock station and the USB Type-C 2.5 Gbps Ethernet adapter have been purchased additionally.

`root `[`#`]`lsusb -tv`

    /:  Bus 001.Port 001: Dev 001, Class=root_hub, Driver=xhci_hcd/5p, 480M
        ID 1d6b:0002 Linux Foundation 2.0 root hub
        |__ Port 003: Dev 003, If 0, Class=Wireless, Driver=btusb, 12M
            ID 10ab:9309 USI Co., Ltd
        |__ Port 003: Dev 003, If 1, Class=Wireless, Driver=btusb, 12M
            ID 10ab:9309 USI Co., Ltd
        |__ Port 005: Dev 015, If 0, Class=Vendor Specific Class, Driver=[none], 12M
            ID 06cb:0126 Synaptics, Inc.
    /:  Bus 002.Port 001: Dev 001, Class=root_hub, Driver=xhci_hcd/2p, 10000M
        ID 1d6b:0003 Linux Foundation 3.0 root hub
    /:  Bus 003.Port 001: Dev 001, Class=root_hub, Driver=xhci_hcd/1p, 480M
        ID 1d6b:0002 Linux Foundation 2.0 root hub
        |__ Port 001: Dev 002, If 0, Class=Video, Driver=uvcvideo, 480M
            ID 04f2:b7bf Chicony Electronics Co., Ltd
        |__ Port 001: Dev 002, If 1, Class=Video, Driver=uvcvideo, 480M
            ID 04f2:b7bf Chicony Electronics Co., Ltd
        |__ Port 001: Dev 002, If 2, Class=Application Specific Interface, Driver=[none], 480M
            ID 04f2:b7bf Chicony Electronics Co., Ltd
    /:  Bus 004.Port 001: Dev 001, Class=root_hub, Driver=xhci_hcd/1p, 10000M
        ID 1d6b:0003 Linux Foundation 3.0 root hub
    /:  Bus 005.Port 001: Dev 001, Class=root_hub, Driver=xhci_hcd/1p, 480M
        ID 1d6b:0002 Linux Foundation 2.0 root hub
        |__ Port 001: Dev 008, If 0, Class=Hub, Driver=hub/5p, 480M
            ID 17ef:30ba Lenovo
            |__ Port 001: Dev 009, If 0, Class=Human Interface Device, Driver=usbhid, 12M
                ID 17ef:30b4 Lenovo
            |__ Port 002: Dev 010, If 0, Class=Billboard, Driver=[none], 12M
                ID 17ef:30b5 Lenovo
            |__ Port 002: Dev 010, If 1, Class=Vendor Specific Class, Driver=[none], 12M
                ID 17ef:30b5 Lenovo
            |__ Port 004: Dev 012, If 0, Class=Hub, Driver=hub/4p, 480M
                ID 17ef:30b7 Lenovo
                |__ Port 004: Dev 013, If 0, Class=Hub, Driver=hub/4p, 480M
                    ID 17ef:30b9 Lenovo
                    |__ Port 004: Dev 015, If 0, Class=Audio, Driver=snd-usb-audio, 12M
                        ID 17ef:30bb Lenovo
                    |__ Port 004: Dev 015, If 1, Class=Audio, Driver=snd-usb-audio, 12M
                        ID 17ef:30bb Lenovo
                    |__ Port 004: Dev 015, If 2, Class=Audio, Driver=snd-usb-audio, 12M
                        ID 17ef:30bb Lenovo
                    |__ Port 004: Dev 015, If 3, Class=Human Interface Device, Driver=usbhid, 12M
                        ID 17ef:30bb Lenovo
    /:  Bus 006.Port 001: Dev 001, Class=root_hub, Driver=xhci_hcd/1p, 10000M
        ID 1d6b:0003 Linux Foundation 3.0 root hub
        |__ Port 001: Dev 007, If 0, Class=Hub, Driver=hub/4p, 10000M
            ID 8087:0b40 Intel Corp.
            |__ Port 001: Dev 008, If 0, Class=Vendor Specific Class, Driver=r8152, 5000M
                ID 0bda:8156 Realtek Semiconductor Corp.
            |__ Port 004: Dev 009, If 0, Class=Hub, Driver=hub/4p, 10000M
                ID 17ef:30b6 Lenovo
                |__ Port 004: Dev 010, If 0, Class=Hub, Driver=hub/4p, 10000M
                    ID 17ef:30b8 Lenovo
                    |__ Port 003: Dev 011, If 0, Class=Vendor Specific Class, Driver=r8152, 5000M
                        ID 0bda:8153 Realtek Semiconductor Corp. RTL8153 Gigabit Ethernet Adapter
    /:  Bus 007.Port 001: Dev 001, Class=root_hub, Driver=xhci_hcd/1p, 480M
        ID 1d6b:0002 Linux Foundation 2.0 root hub
    /:  Bus 008.Port 001: Dev 001, Class=root_hub, Driver=xhci_hcd/1p, 10000M
        ID 1d6b:0003 Linux Foundation 3.0 root hub

## [References]

1.  [[[↑](#cite_ref-1)] [[https://news.lenovo.com/pressroom/press-releases/thinkpad-mobile-workstations-amd-ryzen-pro-7040/](https://news.lenovo.com/pressroom/press-releases/thinkpad-mobile-workstations-amd-ryzen-pro-7040/)]]