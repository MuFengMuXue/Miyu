**Resources**

[[]][Home](https://pcsupport.lenovo.com/us/en/products/laptops-and-netbooks/thinkpad-l-series-laptops/thinkpad-l14-gen-5-type-21l5-21l6)

[[]][Specifications](https://psref.lenovo.com/syspool/Sys/PDF/ThinkPad/ThinkPad_L14_Gen_5_AMD/ThinkPad_L14_Gen_5_AMD_Spec.pdf)

[[]][Specifications (by region)](https://psref.lenovo.com/product/thinkpad_l14_gen_5_amd?tab=model)

[[]][Hardware Maintenance Manual](https://download.lenovo.com/pccbbs/mobiles_pdf/l14_gen5_l16_gen1_hmm_en.pdf)

[[]][User Guide](https://download.lenovo.com/pccbbs/mobiles_pdf/l14_gen5_l16_gen1_linux_ug.pdf)

[[]][BIOS Setup](https://download.lenovo.com/pccbbs/mobiles_pdf/lenovo_bios_setup_linux_wmi_sysfs_1.2.pdf)

The **Lenovo ThinkPad L14 (Gen 5)** is a 14-inch laptop manufactured by Lenovo for business needs. As such, it is thicker than many modern laptops and has plenty of ports. The laptop is also quite easy to maintain.

## Contents

-   [[1] [Hardware]](#Hardware)
    -   [[1.1] [Standard]](#Standard)
    -   [[1.2] [Accessories]](#Accessories)
    -   [[1.3] [Detailed information]](#Detailed_information)
-   [[2] [Installation]](#Installation)
    -   [[2.1] [Firmware]](#Firmware)
        -   [[2.1.1] [AMDGPU]](#AMDGPU)
        -   [[2.1.2] [ATH11K]](#ATH11K)
        -   [[2.1.3] [BTUSB]](#BTUSB)
    -   [[2.2] [Kernel]](#Kernel)
    -   [[2.3] [Emerge]](#Emerge)
-   [[3] [Configuration]](#Configuration)
    -   [[3.1] [Portage]](#Portage)

## [Hardware]

### [Standard]

  --------------------- --------------------------------------------------------------------------------------------------------- -------- ------------------------ ------------------ ---------------- -------
  Device                Make/model                                                                                                Status   Vendor ID / Product ID   Kernel driver(s)   Kernel version   Notes
  CPU                   AMD Ryzen 5 PRO 7535U with Radeon Graphics                                                                Works    N/A                      N/A                6.17.1
  Video card            Advanced Micro Devices, Inc. \[AMD/ATI\] Rembrandt \[Radeon 680M\] (rev d5)                               Works    1002:1681                amdgpu             6.17.1
  Wi-Fi                 Qualcomm Technologies, Inc QCNFA765 Wireless Network Adapter (rev 01)                                     Works    17cb:1103                ath11k_pci         6.17.1
  Ethernet              Realtek Semiconductor Co., Ltd. RTL8111/8168/8211/8411 PCI Express Gigabit Ethernet Controller (rev 0e)   Works    10ec:8168                r8169              6.17.1
  Bluetooth             USI Co., Ltd                                                                                              Works    10ab:9309                btusb              6.17.1
  NVMe                  SK hynix BC901 NVMe Solid State Drive (DRAM-less) (rev 03)                                                Works    1c5c:1d59                nvme               6.17.1
  Audio                 Advanced Micro Devices, Inc. \[AMD\] Family 17h/19h/1ah HD Audio Controller                               Works    1022:15e3                snd_hda_intel      6.17.1
  Smart card reader     Generic EMV Smartcard Reader                                                                              Works    2ce3:9563                usbfs              6.17.1
  Finger print reader   Shenzhen Goodix Technology Co.,Ltd. Goodix USB2.0 MISC                                                    Works    27c6:6594                usbfs              6.17.1
  Camera                IMC Networks Integrated Camera                                                                            Works    13d3:54aa                uvcvideo           6.17.1
  Keyboard              AT Translated Set 2 keyboard                                                                              Works    0001:0001                atkbd              6.17.1
  Mouse                 ELAN06D8:00 04F3:3195 Mouse                                                                               Works    04f3:3195                i2c_designware     6.17.1
  Touchpad              ELAN06D8:00 04F3:3195 Touchpad                                                                            Works    04f3:3195                i2c_designware     6.17.1
  TrackPoint            TPPS/2 Elan TrackPoint                                                                                    Works    0002:000a                psmouse            6.17.1
  --------------------- --------------------------------------------------------------------------------------------------------- -------- ------------------------ ------------------ ---------------- -------

### [Accessories]

  -------- --------------------------------------------- ------------- -------- ------------------ ---------------- --------------
  Device   Make/model                                    Status        Bus ID   Kernel driver(s)   Kernel version   Notes
  Dock     ThinkPad Universal USB-C Dock                 Not tested    N/A      N/A                N/A              To be tested
  Dock     ThinkPad Universal USB-C Smart Dock           Not tested    N/A      N/A                N/A              To be tested
  Dock     ThinkPad Universal Thunderbolt 4 Smart Dock   Not tested    N/A      N/A                N/A              To be tested
  Dock     ThinkPad Thunderbolt 4 Workstation Dock       Not tested    N/A      N/A                N/A              To be tested
  Dock     ThinkPad Universal Thunderbolt 4 Dock         Not tested    N/A      N/A                N/A              To be tested
  Dock     ThinkPad Hybrid USB-C with USB-A Dock         Not tested    N/A      N/A                N/A              To be tested
  Dock     Lenovo USB-C Slim Travel Dock                 Not tested    N/A      N/A                N/A              To be tested
  Dock     Lenovo USB-C Dual Display Travel Dock         Not tested    N/A      N/A                N/A              To be tested
  Dock     Lenovo USB-C Universal Business Dock          Not tested    N/A      N/A                N/A              To be tested
  Dock     Lenovo USB-C Mini Dock                        Not tested    N/A      N/A                N/A              To be tested
  -------- --------------------------------------------- ------------- -------- ------------------ ---------------- --------------

### [Detailed information]

`root `[`#`]`uname -r`

    6.17.1-gentoo-dist

`root `[`#`]`lscpu`

    Architecture:                            x86_64
    CPU op-mode(s):                          32-bit, 64-bit
    Address sizes:                           48 bits physical, 48 bits virtual
    Byte Order:                              Little Endian
    CPU(s):                                  12
    On-line CPU(s) list:                     0-11
    Vendor ID:                               AuthenticAMD
    Model name:                              AMD Ryzen 5 Pro 7535U with Radeon Graphics
    CPU family:                              25
    Model:                                   68
    Thread(s) per core:                      2
    Core(s) per socket:                      6
    Socket(s):                               1
    Stepping:                                1
    Frequency boost:                         enabled
    CPU(s) scaling MHz:                      30%
    CPU max MHz:                             4630.4429
    CPU min MHz:                             418.4140
    BogoMIPS:                                5790.74
    Flags:                                   fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush mmx fxsr sse sse2 ht syscall nx mmxext fxsr_opt pdpe1gb rdtscp lm constant_tsc rep_good nopl xtopology nonstop_tsc cpuid extd_apicid aperfmperf rapl pni pclmulqdq monitor ssse3 fma cx16 sse4_1 sse4_2 x2apic movbe popcnt aes xsave avx f16c rdrand lahf_lm cmp_legacy svm extapic cr8_legacy abm sse4a misalignsse 3dnowprefetch osvw ibs skinit wdt tce topoext perfctr_core perfctr_nb bpext perfctr_llc mwaitx cpb cat_l3 cdp_l3 hw_pstate ssbd mba ibrs ibpb stibp vmmcall fsgsbase bmi1 avx2 smep bmi2 erms invpcid cqm rdt_a rdseed adx smap clflushopt clwb sha_ni xsaveopt xsavec xgetbv1 xsaves cqm_llc cqm_occup_llc cqm_mbm_total cqm_mbm_local user_shstk clzero irperf xsaveerptr rdpru wbnoinvd cppc arat npt lbrv svm_lock nrip_save tsc_scale vmcb_clean flushbyasid decodeassists pausefilter pfthreshold avic v_vmsave_vmload vgif v_spec_ctrl umip pku ospke vaes vpclmulqdq rdpid overflow_recov succor smca fsrm debug_swap
    Virtualization:                          AMD-V
    L1d cache:                               192 KiB (6 instances)
    L1i cache:                               192 KiB (6 instances)
    L2 cache:                                3 MiB (6 instances)
    L3 cache:                                16 MiB (1 instance)
    NUMA node(s):                            1
    NUMA node0 CPU(s):                       0-11
    Vulnerability Gather data sampling:      Not affected
    Vulnerability Ghostwrite:                Not affected
    Vulnerability Indirect target selection: Not affected
    Vulnerability Itlb multihit:             Not affected
    Vulnerability L1tf:                      Not affected
    Vulnerability Mds:                       Not affected
    Vulnerability Meltdown:                  Not affected
    Vulnerability Mmio stale data:           Not affected
    Vulnerability Old microcode:             Not affected
    Vulnerability Reg file data sampling:    Not affected
    Vulnerability Retbleed:                  Not affected
    Vulnerability Spec rstack overflow:      Mitigation; Safe RET
    Vulnerability Spec store bypass:         Mitigation; Speculative Store Bypass disabled via prctl
    Vulnerability Spectre v1:                Mitigation; usercopy/swapgs barriers and __user pointer sanitization
    Vulnerability Spectre v2:                Mitigation; Retpolines; IBPB conditional; IBRS_FW; STIBP always-on; RSB filling; PBRSB-eIBRS Not affected; BHI Not affected
    Vulnerability Srbds:                     Not affected
    Vulnerability Tsa:                       Mitigation; Clear CPU buffers
    Vulnerability Tsx async abort:           Not affected
    Vulnerability Vmscape:                   Mitigation; IBPB before exit to userspace

`root `[`#`]`lspci -nnk`

    00:00.0 Host bridge [0600]: Advanced Micro Devices, Inc. [AMD] Family 17h-19h PCIe Root Complex [1022:14b5] (rev 01)
        Subsystem: Lenovo Device [17aa:50e7]
    00:00.2 IOMMU [0806]: Advanced Micro Devices, Inc. [AMD] Family 17h-19h IOMMU [1022:14b6]
        Subsystem: Lenovo Device [17aa:50e7]
    00:01.0 Host bridge [0600]: Advanced Micro Devices, Inc. [AMD] Family 17h-19h PCIe Dummy Host Bridge [1022:14b7] (rev 01)
    00:01.2 PCI bridge [0604]: Advanced Micro Devices, Inc. [AMD] Family 17h-19h PCIe GPP Bridge [1022:14ba]
        Subsystem: Lenovo Device [17aa:50e7]
        Kernel driver in use: pcieport
    00:02.0 Host bridge [0600]: Advanced Micro Devices, Inc. [AMD] Family 17h-19h PCIe Dummy Host Bridge [1022:14b7] (rev 01)
    00:02.4 PCI bridge [0604]: Advanced Micro Devices, Inc. [AMD] Family 17h-19h PCIe GPP Bridge [1022:14ba]
        Subsystem: Lenovo Device [17aa:50e7]
        Kernel driver in use: pcieport
    00:02.5 PCI bridge [0604]: Advanced Micro Devices, Inc. [AMD] Family 17h-19h PCIe GPP Bridge [1022:14ba]
        Subsystem: Lenovo Device [17aa:50e7]
        Kernel driver in use: pcieport
    00:03.0 Host bridge [0600]: Advanced Micro Devices, Inc. [AMD] Family 17h-19h PCIe Dummy Host Bridge [1022:14b7] (rev 01)
    00:03.1 PCI bridge [0604]: Advanced Micro Devices, Inc. [AMD] Family 19h USB4/Thunderbolt PCIe tunnel [1022:14cd]
        Subsystem: Lenovo Device [17aa:50e7]
        Kernel driver in use: pcieport
    00:04.0 Host bridge [0600]: Advanced Micro Devices, Inc. [AMD] Family 17h-19h PCIe Dummy Host Bridge [1022:14b7] (rev 01)
    00:08.0 Host bridge [0600]: Advanced Micro Devices, Inc. [AMD] Family 17h-19h PCIe Dummy Host Bridge [1022:14b7] (rev 01)
    00:08.1 PCI bridge [0604]: Advanced Micro Devices, Inc. [AMD] Family 17h-19h Internal PCIe GPP Bridge [1022:14b9] (rev 10)
        Subsystem: Device [50e7:17aa]
        Kernel driver in use: pcieport
    00:08.3 PCI bridge [0604]: Advanced Micro Devices, Inc. [AMD] Family 17h-19h Internal PCIe GPP Bridge [1022:14b9] (rev 10)
        Subsystem: Device [50e7:17aa]
        Kernel driver in use: pcieport
    00:14.0 SMBus [0c05]: Advanced Micro Devices, Inc. [AMD] FCH SMBus Controller [1022:790b] (rev 71)
        Subsystem: Lenovo Device [17aa:50e7]
        Kernel driver in use: piix4_smbus
        Kernel modules: i2c_piix4, sp5100_tco
    00:14.3 ISA bridge [0601]: Advanced Micro Devices, Inc. [AMD] FCH LPC Bridge [1022:790e] (rev 51)
        Subsystem: Lenovo Device [17aa:50e7]
    00:18.0 Host bridge [0600]: Advanced Micro Devices, Inc. [AMD] Rembrandt Data Fabric: Device 18h; Function 0 [1022:1679]
    00:18.1 Host bridge [0600]: Advanced Micro Devices, Inc. [AMD] Rembrandt Data Fabric: Device 18h; Function 1 [1022:167a]
    00:18.2 Host bridge [0600]: Advanced Micro Devices, Inc. [AMD] Rembrandt Data Fabric: Device 18h; Function 2 [1022:167b]
    00:18.3 Host bridge [0600]: Advanced Micro Devices, Inc. [AMD] Rembrandt Data Fabric: Device 18h; Function 3 [1022:167c]
        Kernel driver in use: k10temp
        Kernel modules: k10temp
    00:18.4 Host bridge [0600]: Advanced Micro Devices, Inc. [AMD] Rembrandt Data Fabric: Device 18h; Function 4 [1022:167d]
    00:18.5 Host bridge [0600]: Advanced Micro Devices, Inc. [AMD] Rembrandt Data Fabric: Device 18h; Function 5 [1022:167e]
    00:18.6 Host bridge [0600]: Advanced Micro Devices, Inc. [AMD] Rembrandt Data Fabric: Device 18h; Function 6 [1022:167f]
    00:18.7 Host bridge [0600]: Advanced Micro Devices, Inc. [AMD] Rembrandt Data Fabric: Device 18h; Function 7 [1022:1680]
    01:00.0 Network controller [0280]: Qualcomm Technologies, Inc QCNFA765 Wireless Network Adapter [17cb:1103] (rev 01)
        Subsystem: Lenovo Device [17aa:9309]
        Kernel driver in use: ath11k_pci
        Kernel modules: ath11k_pci
    02:00.0 Non-Volatile memory controller [0108]: SK hynix BC901 NVMe Solid State Drive (DRAM-less) [1c5c:1d59] (rev 03)
        Subsystem: SK hynix BC901 NVMe Solid State Drive (DRAM-less) [1c5c:1d59]
        Kernel driver in use: nvme
        Kernel modules: nvme
    03:00.0 Ethernet controller [0200]: Realtek Semiconductor Co., Ltd. RTL8111/8168/8211/8411 PCI Express Gigabit Ethernet Controller [10ec:8168] (rev 0e)
        Subsystem: Lenovo Device [17aa:50e7]
        Kernel driver in use: r8169
        Kernel modules: r8169
    74:00.0 VGA compatible controller [0300]: Advanced Micro Devices, Inc. [AMD/ATI] Rembrandt [Radeon 680M] [1002:1681] (rev d5)
        Subsystem: Lenovo Device [17aa:50e7]
        Kernel driver in use: amdgpu
        Kernel modules: amdgpu
    74:00.1 Audio device [0403]: Advanced Micro Devices, Inc. [AMD/ATI] Radeon High Definition Audio Controller [Rembrandt/Strix] [1002:1640]
        Subsystem: Lenovo Device [17aa:50e7]
        Kernel driver in use: snd_hda_intel
        Kernel modules: snd_hda_intel
    74:00.2 Encryption controller [1080]: Advanced Micro Devices, Inc. [AMD] Family 19h PSP/CCP [1022:1649]
        Subsystem: Lenovo Device [17aa:50e7]
        Kernel driver in use: ccp
    74:00.3 USB controller [0c03]: Advanced Micro Devices, Inc. [AMD] Rembrandt USB4 XHCI controller #3 [1022:161d]
        Subsystem: Lenovo Device [17aa:50e7]
        Kernel driver in use: xhci_hcd
    74:00.4 USB controller [0c03]: Advanced Micro Devices, Inc. [AMD] Rembrandt USB4 XHCI controller #4 [1022:161e]
        Subsystem: Lenovo Device [17aa:50e7]
        Kernel driver in use: xhci_hcd
    74:00.5 Multimedia controller [0480]: Advanced Micro Devices, Inc. [AMD] Audio Coprocessor [1022:15e2] (rev 60)
        Subsystem: Lenovo Device [17aa:50e7]
        Kernel driver in use: snd_pci_acp6x
        Kernel modules: snd_pci_acp3x, snd_rn_pci_acp3x, snd_pci_acp5x, snd_pci_acp6x, snd_acp_pci, snd_rpl_pci_acp6x, snd_pci_ps, snd_sof_amd_renoir, snd_sof_amd_rembrandt, snd_sof_amd_vangogh, snd_sof_amd_acp63, snd_sof_amd_acp70
    74:00.6 Audio device [0403]: Advanced Micro Devices, Inc. [AMD] Family 17h/19h/1ah HD Audio Controller [1022:15e3]
        Subsystem: Lenovo Device [17aa:50e7]
        Kernel driver in use: snd_hda_intel
        Kernel modules: snd_hda_intel
    75:00.0 USB controller [0c03]: Advanced Micro Devices, Inc. [AMD] Rembrandt USB4 XHCI controller #8 [1022:161f]
        Subsystem: Lenovo Device [17aa:50e7]
        Kernel driver in use: xhci_hcd
    75:00.3 USB controller [0c03]: Advanced Micro Devices, Inc. [AMD] Rembrandt USB4 XHCI controller #5 [1022:15d6]
        Subsystem: Lenovo Device [17aa:50e7]
        Kernel driver in use: xhci_hcd
    75:00.4 USB controller [0c03]: Advanced Micro Devices, Inc. [AMD] Rembrandt USB4 XHCI controller #6 [1022:15d7]
        Subsystem: Lenovo Device [17aa:50e7]
        Kernel driver in use: xhci_hcd
    75:00.5 USB controller [0c03]: Advanced Micro Devices, Inc. [AMD] Rembrandt USB4/Thunderbolt NHI controller #1 [1022:162e]
        Subsystem: Lenovo Device [17aa:50e7]
        Kernel driver in use: thunderbolt
        Kernel modules: thunderbolt

`root `[`#`]`lsusb`

    Bus 001 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub
    Bus 001 Device 002: ID 27c6:6594 Shenzhen Goodix Technology Co.,Ltd. Goodix USB2.0 MISC
    Bus 002 Device 001: ID 1d6b:0003 Linux Foundation 3.0 root hub
    Bus 003 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub
    Bus 003 Device 002: ID 05e3:0610 Genesys Logic, Inc. Hub
    Bus 003 Device 003: ID 2ce3:9563 Generic EMV Smartcard Reader
    Bus 003 Device 004: ID 10ab:9309 USI Co., Ltd
    Bus 004 Device 001: ID 1d6b:0003 Linux Foundation 3.0 root hub
    Bus 005 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub
    Bus 005 Device 002: ID 13d3:54aa IMC Networks Integrated Camera
    Bus 006 Device 001: ID 1d6b:0003 Linux Foundation 3.0 root hub
    Bus 007 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub
    Bus 008 Device 001: ID 1d6b:0003 Linux Foundation 3.0 root hub
    Bus 009 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub
    Bus 010 Device 001: ID 1d6b:0003 Linux Foundation 3.0 root hub

`root `[`#`]`lsusb -vt`

    /:  Bus 001.Port 001: Dev 001, Class=root_hub, Driver=xhci_hcd/4p, 480M
        ID 1d6b:0002 Linux Foundation 2.0 root hub
        |__ Port 003: Dev 002, If 0, Class=Vendor Specific Class, Driver=[none], 12M
            ID 27c6:6594 Shenzhen Goodix Technology Co.,Ltd.
    /:  Bus 002.Port 001: Dev 001, Class=root_hub, Driver=xhci_hcd/2p, 10000M
        ID 1d6b:0003 Linux Foundation 3.0 root hub
    /:  Bus 003.Port 001: Dev 001, Class=root_hub, Driver=xhci_hcd/3p, 480M
        ID 1d6b:0002 Linux Foundation 2.0 root hub
        |__ Port 003: Dev 002, If 0, Class=Hub, Driver=hub/3p, 480M
            ID 05e3:0610 Genesys Logic, Inc. Hub
            |__ Port 001: Dev 003, If 0, Class=Chip/SmartCard, Driver=[none], 12M
                ID 2ce3:9563
            |__ Port 002: Dev 004, If 0, Class=Wireless, Driver=btusb, 12M
                ID 10ab:9309 USI Co., Ltd
            |__ Port 002: Dev 004, If 1, Class=Wireless, Driver=btusb, 12M
                ID 10ab:9309 USI Co., Ltd
    /:  Bus 004.Port 001: Dev 001, Class=root_hub, Driver=xhci_hcd/2p, 10000M
        ID 1d6b:0003 Linux Foundation 3.0 root hub
    /:  Bus 005.Port 001: Dev 001, Class=root_hub, Driver=xhci_hcd/1p, 480M
        ID 1d6b:0002 Linux Foundation 2.0 root hub
        |__ Port 001: Dev 002, If 0, Class=Video, Driver=uvcvideo, 480M
            ID 13d3:54aa IMC Networks
        |__ Port 001: Dev 002, If 1, Class=Video, Driver=uvcvideo, 480M
            ID 13d3:54aa IMC Networks
    /:  Bus 006.Port 001: Dev 001, Class=root_hub, Driver=xhci_hcd/0p, 5000M
        ID 1d6b:0003 Linux Foundation 3.0 root hub
    /:  Bus 007.Port 001: Dev 001, Class=root_hub, Driver=xhci_hcd/1p, 480M
        ID 1d6b:0002 Linux Foundation 2.0 root hub
    /:  Bus 008.Port 001: Dev 001, Class=root_hub, Driver=xhci_hcd/1p, 10000M
        ID 1d6b:0003 Linux Foundation 3.0 root hub
    /:  Bus 009.Port 001: Dev 001, Class=root_hub, Driver=xhci_hcd/1p, 480M
        ID 1d6b:0002 Linux Foundation 2.0 root hub
    /:  Bus 010.Port 001: Dev 001, Class=root_hub, Driver=xhci_hcd/1p, 10000M
        ID 1d6b:0003 Linux Foundation 3.0 root hub

## [Installation]

### [Firmware]

#### [AMDGPU]

Firmware blobs required for GPU are:

`user `[`$`]`echo amdgpu/*`

    amdgpu/yellow_carp_ce.bin amdgpu/yellow_carp_dmcub.bin amdgpu/yellow_carp_me.bin amdgpu/yellow_carp_mec.bin amdgpu/yellow_carp_mec2.bin amdgpu/yellow_carp_pfp.bin amdgpu/yellow_carp_rlc.bin amdgpu/yellow_carp_sdma.bin amdgpu/yellow_carp_ta.bin amdgpu/yellow_carp_toc.bin amdgpu/yellow_carp_vcn.bin

#### [ATH11K]

Firmware blobs required for Wi-Fi connectivity are:

`user `[`$`]`echo ath11k/*`

    ath11k/WCN6855/hw2.1/amss.bin ath11k/WCN6855/hw2.1/board-2.bin ath11k/WCN6855/hw2.1/firmware-2.bin ath11k/WCN6855/hw2.1/m3.bin

#### [BTUSB]

Firmware blobs required for Bluetooth connectivity are:

`user `[`$`]`echo qca/*`

    qca/nvm_usb_00130201_gf.bin qca/rampatch_usb_00130201.bin

### [Kernel]

TODO.

### [Emerge]

TODO.

## [Configuration]

### [Portage]

[FILE] **`/etc/portage/make.conf`**

    CFLAGS="-march=znver3 -O2 -pipe"
    CPU_FLAGS_X86="aes avx avx2 bmi1 bmi2 f16c fma3 mmx mmxext pclmul popcnt rdrand sha sse sse2 sse3 sse4_1 sse4_2 sse4a ssse3 vpclmulqdq"
    MAKEOPTS="--jobs 9 --load-average 12"
    INPUT_DEVICES="libinput"
    VIDEO_CARDS="amdgpu radeonsi"