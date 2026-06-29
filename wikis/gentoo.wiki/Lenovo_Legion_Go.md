**Resources**

[[]][Product Information](https://url/to/hardware/manufacturer's/product/homepage)

[[]][Specifications](https://url/to/hardware/specifications)

[[]][Article Title](https://en.wikipedia.org/wiki/HardwareArticleOnWikipedia "wikipedia:HardwareArticleOnWikipedia")

(Introductory paragraph goes here. Describe the hardware. It is okay to mention the hardware platforms friendliness to open source drivers. Optionally, it is nice provide a nice summary of why or why not a user would want to buy this hardware for use with Linux.)

## Contents

-   [[1] [Hardware]](#Hardware)
    -   [[1.1] [Standard]](#Standard)
    -   [[1.2] [Accessories]](#Accessories)
    -   [[1.3] [Detailed information]](#Detailed_information)
-   [[2] [Installation]](#Installation)
    -   [[2.1] [Firmware]](#Firmware)
    -   [[2.2] [Kernel]](#Kernel)
    -   [[2.3] [Emerge]](#Emerge)
-   [[3] [Configuration]](#Configuration)
    -   [[3.1] [Example 1]](#Example_1)
-   [[4] [Troubleshooting]](#Troubleshooting)
    -   [[4.1] [Issue 1]](#Issue_1)
-   [[5] [See also]](#See_also)
-   [[6] [External resources]](#External_resources)
-   [[7] [References]](#References)

## [Hardware]

### [Standard]

  -------------------------- ---------------------------------------------- ------------- ------------------------ ------------------ ---------------- -----------------
  Device                     Make/model                                     Status        Vendor ID / Product ID   Kernel driver(s)   Kernel version   Notes
  CPU                        AMD Phenom(tm) II X4 955                       Works         N/A                      N/A                3.18.9           This CPU rocks!
  Front side bus             RD790 Host Bridge                              Not tested    1002:5956                pcieport           3.18.9
  Video card                 NVIDIA Corporation NV18 \[GeForce4 MX 4000\]   Borked        10de:0185                nouveau            3.18.9           Note example.
  Wireless Network Adapter   MEDIATEK Corp. MT7922 802.11ax                 Works         14c3:0616                mt7921e            6.16.2-gentoo
  -------------------------- ---------------------------------------------- ------------- ------------------------ ------------------ ---------------- -----------------

### [Accessories]

(Optional section. Describe any accessories that may be possible in this section. Anything from external plug-and-play LCD screens to computer docks.)

  -------- ------------------- ------------- ------------------------ ------------------ ---------------- ---------------
  Device   Make/model          Status        Vendor ID / Product ID   Kernel driver(s)   Kernel version   Notes
  Dock     ThinkPad Pro Dock   Not tested    N/A                      N/A                3.18.9           Note example.
  -------- ------------------- ------------- ------------------------ ------------------ ---------------- ---------------

### [Detailed information]

`root `[`#`]`uname -r`

    The command output goes here.

`root `[`#`]`lscpu`

    Architecture:             x86_64
      CPU op-mode(s):         32-bit, 64-bit
      Address sizes:          48 bits physical, 48 bits virtual
      Byte Order:             Little Endian
    CPU(s):                   16
      On-line CPU(s) list:    0-15
    Vendor ID:                AuthenticAMD
      Model name:             AMD Ryzen Z1 Extreme
        CPU family:           25
        Model:                116
        Thread(s) per core:   2
        Core(s) per socket:   8
        Socket(s):            1
        Stepping:             1
        Frequency boost:      enabled
        CPU(s) scaling MHz:   35%
        CPU max MHz:          5132.0000
        CPU min MHz:          400.0000
        BogoMIPS:             6587.74
        Flags:                fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush mmx fxsr sse sse2 ht syscall nx mmx
                              ext fxsr_opt pdpe1gb rdtscp lm constant_tsc rep_good amd_lbr_v2 nopl xtopology nonstop_tsc cpuid extd_apicid aperfm
                              perf rapl pni pclmulqdq monitor ssse3 fma cx16 sse4_1 sse4_2 x2apic movbe popcnt aes xsave avx f16c rdrand lahf_lm
                              cmp_legacy svm extapic cr8_legacy abm sse4a misalignsse 3dnowprefetch osvw ibs skinit wdt tce topoext perfctr_core
                              perfctr_nb bpext perfctr_llc mwaitx cpb cat_l3 cdp_l3 hw_pstate ssbd mba perfmon_v2 ibrs ibpb stibp ibrs_enhanced v
                              mmcall fsgsbase bmi1 avx2 smep bmi2 erms invpcid cqm rdt_a avx512f avx512dq rdseed adx smap avx512ifma clflushopt c
                              lwb avx512cd sha_ni avx512bw avx512vl xsaveopt xsavec xgetbv1 xsaves cqm_llc cqm_occup_llc cqm_mbm_total cqm_mbm_lo
                              cal avx512_bf16 clzero irperf xsaveerptr rdpru wbnoinvd cppc arat npt lbrv svm_lock nrip_save tsc_scale vmcb_clean
                              flushbyasid decodeassists pausefilter pfthreshold vgif x2avic v_spec_ctrl vnmi avx512vbmi umip pku ospke avx512_vbm
                              i2 gfni vaes vpclmulqdq avx512_vnni avx512_bitalg avx512_vpopcntdq rdpid overflow_recov succor smca fsrm flush_l1d
                              amd_lbr_pmc_freeze
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
      Spec rstack overflow:   Mitigation; Safe RET
      Spec store bypass:      Mitigation; Speculative Store Bypass disabled via prctl
      Spectre v1:             Mitigation; usercopy/swapgs barriers and __user pointer sanitization
      Spectre v2:             Mitigation; Enhanced / Automatic IBRS; IBPB conditional; STIBP always-on; RSB filling; PBRSB-eIBRS Not affected; BH
                              I Not affected
      Srbds:                  Not affected
      Tsx async abort:        Not affected

`root `[`#`]`lspci -nnk`

    00:00.0 Host bridge [0600]: Advanced Micro Devices, Inc. [AMD] Phoenix Root Complex [1022:14e8]
        Subsystem: Lenovo Device [17aa:3812]
    00:00.2 IOMMU [0806]: Advanced Micro Devices, Inc. [AMD] Phoenix IOMMU [1022:14e9]
        Subsystem: Lenovo Device [17aa:3812]
    00:01.0 Host bridge [0600]: Advanced Micro Devices, Inc. [AMD] Phoenix Dummy Host Bridge [1022:14ea]
    00:02.0 Host bridge [0600]: Advanced Micro Devices, Inc. [AMD] Phoenix Dummy Host Bridge [1022:14ea]
    00:02.2 PCI bridge [0604]: Advanced Micro Devices, Inc. [AMD] Phoenix GPP Bridge [1022:14ee]
        Subsystem: Advanced Micro Devices, Inc. [AMD] Device [1022:1453]
        Kernel driver in use: pcieport
    00:02.3 PCI bridge [0604]: Advanced Micro Devices, Inc. [AMD] Phoenix GPP Bridge [1022:14ee]
        Subsystem: Advanced Micro Devices, Inc. [AMD] Device [1022:1453]
        Kernel driver in use: pcieport
    00:02.4 PCI bridge [0604]: Advanced Micro Devices, Inc. [AMD] Phoenix GPP Bridge [1022:14ee]
        Subsystem: Advanced Micro Devices, Inc. [AMD] Device [1022:1453]
        Kernel driver in use: pcieport
    00:03.0 Host bridge [0600]: Advanced Micro Devices, Inc. [AMD] Phoenix Dummy Host Bridge [1022:14ea]
    00:03.1 PCI bridge [0604]: Advanced Micro Devices, Inc. [AMD] Family 19h USB4/Thunderbolt PCIe tunnel [1022:14ef]
        Subsystem: Advanced Micro Devices, Inc. [AMD] Device [1022:1453]
        Kernel driver in use: pcieport
    00:04.0 Host bridge [0600]: Advanced Micro Devices, Inc. [AMD] Phoenix Dummy Host Bridge [1022:14ea]
    00:04.1 PCI bridge [0604]: Advanced Micro Devices, Inc. [AMD] Family 19h USB4/Thunderbolt PCIe tunnel [1022:14ef]
        Subsystem: Advanced Micro Devices, Inc. [AMD] Device [1022:1453]
        Kernel driver in use: pcieport
    00:08.0 Host bridge [0600]: Advanced Micro Devices, Inc. [AMD] Phoenix Dummy Host Bridge [1022:14ea]
    00:08.1 PCI bridge [0604]: Advanced Micro Devices, Inc. [AMD] Phoenix Internal GPP Bridge to Bus [C:A] [1022:14eb]
        Subsystem: Advanced Micro Devices, Inc. [AMD] Phoenix Internal GPP Bridge to Bus [C:A] [1022:14eb]
        Kernel driver in use: pcieport
    00:08.2 PCI bridge [0604]: Advanced Micro Devices, Inc. [AMD] Phoenix Internal GPP Bridge to Bus [C:A] [1022:14eb]
        Subsystem: Advanced Micro Devices, Inc. [AMD] Phoenix Internal GPP Bridge to Bus [C:A] [1022:14eb]
        Kernel driver in use: pcieport
    00:08.3 PCI bridge [0604]: Advanced Micro Devices, Inc. [AMD] Phoenix Internal GPP Bridge to Bus [C:A] [1022:14eb]
    pcilib: Error reading /sys/bus/pci/devices/0000:00:08.3/label: Operation not permitted
        Subsystem: Advanced Micro Devices, Inc. [AMD] Phoenix Internal GPP Bridge to Bus [C:A] [1022:14eb]
        Kernel driver in use: pcieport
    00:14.0 SMBus [0c05]: Advanced Micro Devices, Inc. [AMD] FCH SMBus Controller [1022:790b] (rev 71)
        Subsystem: Lenovo Device [17aa:3812]
        Kernel driver in use: piix4_smbus
    00:14.3 ISA bridge [0601]: Advanced Micro Devices, Inc. [AMD] FCH LPC Bridge [1022:790e] (rev 51)
        Subsystem: Lenovo Device [17aa:3812]
    00:18.0 Host bridge [0600]: Advanced Micro Devices, Inc. [AMD] Phoenix Data Fabric; Function 0 [1022:14f0]
    00:18.1 Host bridge [0600]: Advanced Micro Devices, Inc. [AMD] Phoenix Data Fabric; Function 1 [1022:14f1]
    00:18.2 Host bridge [0600]: Advanced Micro Devices, Inc. [AMD] Phoenix Data Fabric; Function 2 [1022:14f2]
    00:18.3 Host bridge [0600]: Advanced Micro Devices, Inc. [AMD] Phoenix Data Fabric; Function 3 [1022:14f3]
    00:18.4 Host bridge [0600]: Advanced Micro Devices, Inc. [AMD] Phoenix Data Fabric; Function 4 [1022:14f4]
    00:18.5 Host bridge [0600]: Advanced Micro Devices, Inc. [AMD] Phoenix Data Fabric; Function 5 [1022:14f5]
    00:18.6 Host bridge [0600]: Advanced Micro Devices, Inc. [AMD] Phoenix Data Fabric; Function 6 [1022:14f6]
    00:18.7 Host bridge [0600]: Advanced Micro Devices, Inc. [AMD] Phoenix Data Fabric; Function 7 [1022:14f7]
    01:00.0 Network controller [0280]: MEDIATEK Corp. MT7922 802.11ax PCI Express Wireless Network Adapter [14c3:0616]
        Subsystem: Lenovo Device [17aa:e0c7]
        Kernel driver in use: mt7921e
        Kernel modules: mt7921e
    02:00.0 SD Host controller [0805]: Genesys Logic, Inc GL9755 SD Host Controller [17a0:9755] (rev 01)
        Subsystem: Genesys Logic, Inc GL9755 SD Host Controller [17a0:9755]
    03:00.0 Non-Volatile memory controller [0108]: SK hynix BC901 NVMe Solid State Drive (DRAM-less) [1c5c:1d59] (rev 03)
        DeviceName: Realtek
        Subsystem: SK hynix BC901 NVMe Solid State Drive (DRAM-less) [1c5c:1d59]
        Kernel driver in use: nvme
    c2:00.0 VGA compatible controller [0300]: Advanced Micro Devices, Inc. [AMD/ATI] Phoenix1 [1002:15bf] (rev 04)
        Subsystem: Lenovo Device [17aa:3812]
        Kernel driver in use: amdgpu
        Kernel modules: amdgpu
    c2:00.1 Audio device [0403]: Advanced Micro Devices, Inc. [AMD/ATI] Rembrandt Radeon High Definition Audio Controller [1002:1640]
        Subsystem: Lenovo Device [17aa:3812]
        Kernel driver in use: snd_hda_intel
    c2:00.2 Encryption controller [1080]: Advanced Micro Devices, Inc. [AMD] Phoenix CCP/PSP 3.0 Device [1022:15c7]
        Subsystem: Lenovo Device [17aa:3812]
    c2:00.3 USB controller [0c03]: Advanced Micro Devices, Inc. [AMD] Device [1022:15b9]
        Subsystem: Lenovo Device [17aa:3812]
        Kernel driver in use: xhci_hcd
    c2:00.4 USB controller [0c03]: Advanced Micro Devices, Inc. [AMD] Device [1022:15ba]
        Subsystem: Lenovo Device [17aa:3812]
        Kernel driver in use: xhci_hcd
    c2:00.5 Multimedia controller [0480]: Advanced Micro Devices, Inc. [AMD] ACP/ACP3X/ACP6x Audio Coprocessor [1022:15e2] (rev 63)
        Subsystem: Lenovo Device [17aa:3812]
    c2:00.6 Audio device [0403]: Advanced Micro Devices, Inc. [AMD] Family 17h/19h/1ah HD Audio Controller [1022:15e3]
        Subsystem: Lenovo Device [17aa:3c26]
        Kernel driver in use: snd_hda_intel
    c2:00.7 Signal processing controller [1180]: Advanced Micro Devices, Inc. [AMD] Sensor Fusion Hub [1022:164a]
        Subsystem: Lenovo Device [17aa:3812]
        Kernel driver in use: pcie_mp2_amd
    c3:00.0 Non-Essential Instrumentation [1300]: Advanced Micro Devices, Inc. [AMD] Phoenix Dummy Function [1022:14ec]
        Subsystem: Lenovo Device [17aa:3812]
    c4:00.0 Non-Essential Instrumentation [1300]: Advanced Micro Devices, Inc. [AMD] Phoenix Dummy Function [1022:14ec]
        Subsystem: Lenovo Device [17aa:3812]
    c4:00.3 USB controller [0c03]: Advanced Micro Devices, Inc. [AMD] Device [1022:15c0]
        Subsystem: Lenovo Device [17aa:3812]
        Kernel driver in use: xhci_hcd
    c4:00.4 USB controller [0c03]: Advanced Micro Devices, Inc. [AMD] Device [1022:15c1]
        Subsystem: Lenovo Device [17aa:3812]
        Kernel driver in use: xhci_hcd
    c4:00.5 USB controller [0c03]: Advanced Micro Devices, Inc. [AMD] Pink Sardine USB4/Thunderbolt NHI controller #1 [1022:1668]
        Subsystem: Lenovo Device [17aa:3812]
    c4:00.6 USB controller [0c03]: Advanced Micro Devices, Inc. [AMD] Pink Sardine USB4/Thunderbolt NHI controller #2 [1022:1669]
        Subsystem: Lenovo Device [17aa:3812]

`root `[`#`]`lsusb`

    Bus 001 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub
    Bus 001 Device 003: ID 0489:e0d9 Foxconn / Hon Hai Wireless_Device
    Bus 001 Device 012: ID 17ef:61eb Lenovo Legion Controller for Windows
    Bus 002 Device 001: ID 1d6b:0003 Linux Foundation 3.0 root hub
    Bus 003 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub
    Bus 004 Device 001: ID 1d6b:0003 Linux Foundation 3.0 root hub
    Bus 005 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub
    Bus 006 Device 001: ID 1d6b:0003 Linux Foundation 3.0 root hub
    Bus 007 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub
    Bus 008 Device 001: ID 1d6b:0003 Linux Foundation 3.0 root hub

`root `[`#`]`lsusb -vt`

    Bus 008 Device 001: ID 1d6b:0003 Linux Foundation 3.0 root hub
    /:  Bus 001.Port 001: Dev 001, Class=root_hub, Driver=xhci_hcd/5p, 480M
        ID 1d6b:0002 Linux Foundation 2.0 root hub
        |__ Port 003: Dev 012, If 0, Class=Vendor Specific Class, Driver=xpad, 12M
            ID 17ef:61eb Lenovo
        |__ Port 003: Dev 012, If 1, Class=Human Interface Device, Driver=usbhid, 12M
            ID 17ef:61eb Lenovo
        |__ Port 003: Dev 012, If 2, Class=Human Interface Device, Driver=usbhid, 12M
            ID 17ef:61eb Lenovo
        |__ Port 003: Dev 012, If 3, Class=Human Interface Device, Driver=usbhid, 12M
            ID 17ef:61eb Lenovo
        |__ Port 005: Dev 003, If 0, Class=Wireless, Driver=btusb, 480M
            ID 0489:e0d9 Foxconn / Hon Hai
        |__ Port 005: Dev 003, If 1, Class=Wireless, Driver=btusb, 480M
            ID 0489:e0d9 Foxconn / Hon Hai
        |__ Port 005: Dev 003, If 2, Class=Wireless, Driver=btusb, 480M
            ID 0489:e0d9 Foxconn / Hon Hai
    /:  Bus 002.Port 001: Dev 001, Class=root_hub, Driver=xhci_hcd/2p, 10000M
        ID 1d6b:0003 Linux Foundation 3.0 root hub
    /:  Bus 003.Port 001: Dev 001, Class=root_hub, Driver=xhci_hcd/1p, 480M
        ID 1d6b:0002 Linux Foundation 2.0 root hub
    /:  Bus 004.Port 001: Dev 001, Class=root_hub, Driver=xhci_hcd/1p, 10000M
        ID 1d6b:0003 Linux Foundation 3.0 root hub
    /:  Bus 005.Port 001: Dev 001, Class=root_hub, Driver=xhci_hcd/1p, 480M
        ID 1d6b:0002 Linux Foundation 2.0 root hub
    /:  Bus 006.Port 001: Dev 001, Class=root_hub, Driver=xhci_hcd/1p, 10000M
        ID 1d6b:0003 Linux Foundation 3.0 root hub
    /:  Bus 007.Port 001: Dev 001, Class=root_hub, Driver=xhci_hcd/1p, 480M
        ID 1d6b:0002 Linux Foundation 2.0 root hub
    /:  Bus 008.Port 001: Dev 001, Class=root_hub, Driver=xhci_hcd/1p, 10000M
        ID 1d6b:0003 Linux Foundation 3.0 root hub

## [Installation]

(Write the necessary steps to get Gentoo onto this system. Try to document any special step that each user will need to reproduce on their system. Includes getting special drivers or firmware from a manufacturer website, etc.)

### [Firmware]

(Optional section.)

### [Kernel]

(Show what options are necessary in the kernel in order to get all device components functional for this hardware platform.)

[KERNEL] **Enable support for these hardware drivers**

    Write menuconfig instructions here.

[KERNEL] **Touchscreen**

    Device Drivers  --->
        I2C support  --->
    <*>   AMD MP2 PCIe
    <*>   AMD ASF I2C Controller Support
    <*>   Intel PIIX4 and compatible (ATI/AMD/Serverworks/Broadcom/SMSC)
    <*>   Synopsys DesignWare I2C adapter
    <*>     Synopsys DesignWare Platform driver
        ...
    [*] HID bus support  --->
         Special HID drivers  --->
    <*>   HID Multitouch panels
        ...
    -*- Pin controllers  --->
    [*]   AMD GPIO pin control

[KERNEL] **Wireless network adapter**

    Device Drivers  --->
      [*] Network device support  --->
      [*]  Wireless LAN  --->
      [*]   MediaTek devices
      <M>     MediaTek MT7921E (PCIe) support

[KERNEL] **Bluetooth adapter**

    -*- Networking support  --->
    [*]  Bluetooth subsystem support  --->
    [*]   Bluetooth device drivers  --->
    <M>    HCI USB driver
    [*]     MediaTek protocol support

[KERNEL] **Sensors**

    Device drivers  --->
    [*] HID bus support  --->
         Special HID drivers  --->
    <*>   HID Sensors framework support
         ...
         AMD SFH HID support --->
    <*>   AMD Sensor Fusion Hub
    <*> Industrial I/O support  --->
         Accelerometers  --->
    <*>   HID Accelerometers 3D

### [Emerge]

(Optional section. If the platform requires any user space packages or kernel patches, mention them here).

`root `[`#`]`emerge --ask category/package`

## [Configuration]

(Explain any additional configuration or special customization for this hardware platform. Could be anything from BIOS settings to assigning proper media key functionality.)

### [Example 1]

(Example: Do this in order to get these keys working.)

## [Troubleshooting]

(Optional section.)

(Troubleshoot issues in this section. Separate issues by best describing the error with a new section name. Remove this section and subsections if no issues are known.)

### [Issue 1]

When X happens, Y is how you fix it.

## [See also]

## [External resources]

(Optional section.)

-   (Link to external resources (outside the Wiki) using bullet points in this section. It is common for the information in this section to full sentences that are links.)

## [References]

(Optional section. Remove this section if references are not used. This section is used to cite factual information. This information is found outside the Gentoo Wiki and used to back up truth claims. The actual references themselves still be littered throughout the main article.)