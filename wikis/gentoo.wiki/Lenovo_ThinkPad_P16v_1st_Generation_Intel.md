**Resources**

[[]][Product Information](https://www.lenovo.com/us/en/p/laptops/thinkpad/thinkpadp/thinkpad-p16v-(16-inch-intel)-mobile-workstation/len101t0071)

[[]][Official Support Page](https://pcsupport.lenovo.com/us/en/products/laptops-and-netbooks/thinkpad-p-series-laptops/thinkpad-p16v-gen-1-type-21fc-21fd/21fc/21fc002fus/)

[[]][Specifications](https://psref.lenovo.com/syspool/Sys/PDF/ThinkPad/ThinkPad_P16v_Gen_1_Intel/ThinkPad_P16v_Gen_1_Intel_Spec.pdf)

[[]][Specifications (by region)](https://psref.lenovo.com/Product/ThinkPad/ThinkPad_P16v_Gen_1_Intel?tab=model)

[[]][Hardware Maintenance Manual](https://download.lenovo.com/pccbbs/mobiles_pdf/p16v_gen1_hmm_en.pdf)

[[]][User Guide](https://download.lenovo.com/pccbbs/mobiles_pdf/p16v_gen1_ug_en.pdf)

The **Lenovo ThinkPad P16v 1st Generation (Intel)** is a 16-inch laptop released in 2023. ^[\[1\]](#cite_note-1)^

## Contents

-   [[1] [Hardware]](#Hardware)
    -   [[1.1] [Standard]](#Standard)
    -   [[1.2] [Detailed information]](#Detailed_information)
-   [[2] [Troubleshooting]](#Troubleshooting)
    -   [[2.1] [Lagging screen]](#Lagging_screen)
-   [[3] [References]](#References)

## [Hardware]

### [Standard]

  ------------------------- ------------------------------------------------------------------ -------- ------------------------ ----------------------- ---------------- ----------------------------------------------------------------------
  Device                    Make/model                                                         Status   Vendor ID / Product ID   Kernel driver(s)        Kernel version   Notes
  CPU                       13th Gen Intel(R) Core(TM) i9-13900H                               Works    N/A                      N/A                     6.6.21
  Video Card                Iris Xe Graphics                                                   Works    pci:8086:a7a0            i915                    6.6.21
  Video Card                NVIDIA Corporation AD107GLM (RTX 2000 Ada Generation Laptop GPU)   Works    pci:10de:28b8            nvidia-drivers          6.6.21
  Wireless & Bluetooth      Intel Corporation Raptor Lake PCH CNVi WiFi                        Works    pci:8086:51f1            iwlmvm                  6.6.21
  Sound                     Intel Corporation Raptor Lake-P/U/H cAVS                           Works    pci:8086:51ca            snd_sof_pci_intel_tgl   6.6.21           driver is uncertain since multiple build and not cleaned up
  Touchpad and trackpoint   Synaptics, Inc                                                     Works    usb:06cb:0126            Synaptics related       6.6.21           touchpad is only tested on 6.1.67. not tried to clean up kernel opts
  Webcam                    Syntek Integrated Camera                                           Works    usb:174f:11a8            uvcvideo                6.1.67           only RGB tested, IR not tested
  ------------------------- ------------------------------------------------------------------ -------- ------------------------ ----------------------- ---------------- ----------------------------------------------------------------------

### [Detailed information]

`root `[`#`]`dmidecode -s system-version`

    ThinkPad P16v Gen 1

`root `[`#`]`uname -r`

    6.6.21-gentoo

`root `[`#`]`lscpu`

    Architecture:            x86_64
      CPU op-mode(s):        32-bit, 64-bit
      Address sizes:         46 bits physical, 48 bits virtual
      Byte Order:            Little Endian
    CPU(s):                  14
      On-line CPU(s) list:   0-13
    Vendor ID:               GenuineIntel
      BIOS Vendor ID:        Intel(R) Corporation
      Model name:            13th Gen Intel(R) Core(TM) i9-13900H
        BIOS Model name:     13th Gen Intel(R) Core(TM) i9-13900H None CPU @ 2.6GHz
        BIOS CPU family:     207
        CPU family:          6
        Model:               186
        Thread(s) per core:  1
        Core(s) per socket:  14
        Socket(s):           1
        Stepping:            2
        CPU(s) scaling MHz:  25%
        CPU max MHz:         5400.0000
        CPU min MHz:         400.0000
        BogoMIPS:            5992.00
        Flags:               fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat
                              pse36 clflush dts acpi mmx fxsr sse sse2 ss ht tm pbe syscall nx
                              pdpe1gb rdtscp lm constant_tsc art arch_perfmon pebs bts rep_goo
                             d nopl xtopology nonstop_tsc cpuid aperfmperf tsc_known_freq pni
                             pclmulqdq dtes64 monitor ds_cpl vmx smx est tm2 ssse3 sdbg fma cx
                             16 xtpr pdcm sse4_1 sse4_2 x2apic movbe popcnt tsc_deadline_timer
                              aes xsave avx f16c rdrand lahf_lm abm 3dnowprefetch cpuid_fault
                             epb ssbd ibrs ibpb stibp ibrs_enhanced tpr_shadow flexpriority ep
                             t vpid ept_ad fsgsbase tsc_adjust bmi1 avx2 smep bmi2 erms invpci
                             d rdseed adx smap clflushopt clwb intel_pt sha_ni xsaveopt xsavec
                              xgetbv1 xsaves split_lock_detect user_shstk avx_vnni dtherm ida
                             arat pln pts hwp hwp_notify hwp_act_window hwp_epp hwp_pkg_req hf
                             i vnmi umip pku waitpkg gfni vaes vpclmulqdq tme rdpid movdiri mo
                             vdir64b fsrm md_clear serialize pconfig arch_lbr ibt flush_l1d ar
                             ch_capabilities
    Virtualization features:
      Virtualization:        VT-x
    Caches (sum of all):
      L1d:                   544 KiB (14 instances)
      L1i:                   704 KiB (14 instances)
      L2:                    11.5 MiB (8 instances)
      L3:                    24 MiB (1 instance)
    Vulnerabilities:
      Gather data sampling:  Not affected
      Itlb multihit:         Not affected
      L1tf:                  Not affected
      Mds:                   Not affected
      Meltdown:              Not affected
      Mmio stale data:       Not affected
      Retbleed:              Not affected
      Spec rstack overflow:  Not affected
      Spec store bypass:     Mitigation; Speculative Store Bypass disabled via prctl
      Spectre v1:            Mitigation; usercopy/swapgs barriers and __user pointer sanitizat
                             ion
      Spectre v2:            Mitigation; Enhanced / Automatic IBRS, IBPB conditional, RSB fill
                             ing, PBRSB-eIBRS SW sequence
      Srbds:                 Not affected
      Tsx async abort:       Not affected

** Note**\
SMT was manually disabled using the kernel command line options.

`root `[`#`]`lspci -nnk`

    00:00.0 Host bridge [0600]: Intel Corporation Device [8086:a706]
        Subsystem: Lenovo Device [17aa:2309]
    00:01.0 PCI bridge [0604]: Intel Corporation Device [8086:a70d]
        Subsystem: Lenovo Device [17aa:2309]
        Kernel driver in use: pcieport
    00:02.0 VGA compatible controller [0300]: Intel Corporation Raptor Lake-P [Iris Xe Graphics] [8086:a7a0] (rev 04)
        Subsystem: Lenovo Raptor Lake-P [Iris Xe Graphics] [17aa:230a]
        Kernel driver in use: i915
        Kernel modules: i915
    00:04.0 Signal processing controller [1180]: Intel Corporation Raptor Lake Dynamic Platform and Thermal Framework Processor Participant [8086:a71d]
        Subsystem: Lenovo Raptor Lake Dynamic Platform and Thermal Framework Processor Participant [17aa:2309]
        Kernel driver in use: proc_thermal_pci
    00:06.0 PCI bridge [0604]: Intel Corporation Raptor Lake PCIe 4.0 Graphics Port [8086:a74d]
        Subsystem: Lenovo Raptor Lake PCIe 4.0 Graphics Port [17aa:2309]
        Kernel driver in use: pcieport
    00:06.2 PCI bridge [0604]: Intel Corporation Device [8086:a73d]
        Subsystem: Lenovo Device [17aa:2309]
        Kernel driver in use: pcieport
    00:07.0 PCI bridge [0604]: Intel Corporation Raptor Lake-P Thunderbolt 4 PCI Express Root Port #0 [8086:a76e]
        Subsystem: Lenovo Raptor Lake-P Thunderbolt 4 PCI Express Root Port [17aa:2309]
        Kernel driver in use: pcieport
    00:07.2 PCI bridge [0604]: Intel Corporation Raptor Lake-P Thunderbolt 4 PCI Express Root Port #2 [8086:a72f]
        Subsystem: Lenovo Raptor Lake-P Thunderbolt 4 PCI Express Root Port [17aa:2309]
        Kernel driver in use: pcieport
    00:08.0 System peripheral [0880]: Intel Corporation GNA Scoring Accelerator module [8086:a74f]
        Subsystem: Lenovo GNA Scoring Accelerator module [17aa:2309]
    00:0d.0 USB controller [0c03]: Intel Corporation Raptor Lake-P Thunderbolt 4 USB Controller [8086:a71e]
        Subsystem: Lenovo Raptor Lake-P Thunderbolt 4 USB Controller [17aa:2309]
        Kernel driver in use: xhci_hcd
    00:0d.2 USB controller [0c03]: Intel Corporation Raptor Lake-P Thunderbolt 4 NHI #0 [8086:a73e]
        Subsystem: Lenovo Raptor Lake-P Thunderbolt 4 NHI [17aa:2309]
        Kernel driver in use: thunderbolt
    00:0d.3 USB controller [0c03]: Intel Corporation Raptor Lake-P Thunderbolt 4 NHI #1 [8086:a76d]
        Subsystem: Lenovo Raptor Lake-P Thunderbolt 4 NHI [17aa:2309]
        Kernel driver in use: thunderbolt
    00:14.0 USB controller [0c03]: Intel Corporation Alder Lake PCH USB 3.2 xHCI Host Controller [8086:51ed] (rev 01)
        Subsystem: Lenovo Alder Lake PCH USB 3.2 xHCI Host Controller [17aa:2309]
        Kernel driver in use: xhci_hcd
    00:14.2 RAM memory [0500]: Intel Corporation Alder Lake PCH Shared SRAM [8086:51ef] (rev 01)
        Subsystem: Lenovo Alder Lake PCH Shared SRAM [17aa:2309]
    00:14.3 Network controller [0280]: Intel Corporation Raptor Lake PCH CNVi WiFi [8086:51f1] (rev 01)
        Subsystem: Intel Corporation Raptor Lake PCH CNVi WiFi [8086:0090]
        Kernel driver in use: iwlwifi
        Kernel modules: iwlwifi
    00:15.0 Serial bus controller [0c80]: Intel Corporation Alder Lake PCH Serial IO I2C Controller #0 [8086:51e8] (rev 01)
        Subsystem: Lenovo Alder Lake PCH Serial IO I2C Controller [17aa:2309]
        Kernel driver in use: intel-lpss
    00:16.0 Communication controller [0780]: Intel Corporation Alder Lake PCH HECI Controller [8086:51e0] (rev 01)
        Subsystem: Lenovo Alder Lake PCH HECI Controller [17aa:2309]
        Kernel driver in use: mei_me
    00:1c.0 PCI bridge [0604]: Intel Corporation Device [8086:51b8] (rev 01)
        Subsystem: Lenovo Device [17aa:2309]
        Kernel driver in use: pcieport
    00:1c.5 PCI bridge [0604]: Intel Corporation Device [8086:51bd] (rev 01)
        Subsystem: Lenovo Device [17aa:2309]
        Kernel driver in use: pcieport
    00:1f.0 ISA bridge [0601]: Intel Corporation Raptor Lake LPC/eSPI Controller [8086:519d] (rev 01)
        Subsystem: Lenovo Raptor Lake LPC/eSPI Controller [17aa:2309]
    00:1f.3 Audio device [0403]: Intel Corporation Raptor Lake-P/U/H cAVS [8086:51ca] (rev 01)
        Subsystem: Lenovo Raptor Lake-P/U/H cAVS [17aa:2309]
        Kernel driver in use: sof-audio-pci-intel-tgl
        Kernel modules: snd_sof_pci_intel_tgl
    00:1f.4 SMBus [0c05]: Intel Corporation Alder Lake PCH-P SMBus Host Controller [8086:51a3] (rev 01)
        Subsystem: Lenovo Alder Lake PCH-P SMBus Host Controller [17aa:2309]
        Kernel driver in use: i801_smbus
    00:1f.5 Serial bus controller [0c80]: Intel Corporation Alder Lake-P PCH SPI Controller [8086:51a4] (rev 01)
        Subsystem: Lenovo Alder Lake-P PCH SPI Controller [17aa:2309]
    01:00.0 3D controller [0302]: NVIDIA Corporation AD107GLM [RTX 2000 Ada Generation Laptop GPU] [10de:28b8] (rev a1)
        Subsystem: Lenovo AD107GLM [RTX 2000 Ada Generation Laptop GPU] [17aa:230a]
        Kernel driver in use: nvidia
        Kernel modules: nvidia_drm, nvidia
    04:00.0 Non-Volatile memory controller [0108]: SK hynix Platinum P41/PC801 NVMe Solid State Drive [1c5c:1959]
        Subsystem: SK hynix Platinum P41/PC801 NVMe Solid State Drive [1c5c:1959]
        Kernel driver in use: nvme
    05:00.0 Non-Volatile memory controller [0108]: SK hynix Platinum P41/PC801 NVMe Solid State Drive [1c5c:1959]
        Subsystem: SK hynix Platinum P41/PC801 NVMe Solid State Drive [1c5c:1959]
        Kernel driver in use: nvme
    0a:00.0 Unassigned class [ff00]: Realtek Semiconductor Co., Ltd. RTS5261 PCI Express Card Reader [10ec:5261] (rev 01)
        Subsystem: Lenovo RTS5261 PCI Express Card Reader [17aa:2309]
        Kernel driver in use: rtsx_pci

** Note**\
The second SSD was installed after purchase, the laptop shipped with only one.

`root `[`#`]`lsusb`

    Bus 001 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub
    Bus 002 Device 001: ID 1d6b:0003 Linux Foundation 3.0 root hub
    Bus 003 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub
    Bus 003 Device 002: ID 06cb:0126 Synaptics, Inc.
    Bus 003 Device 003: ID 174f:11a8 Syntek Integrated Camera
    Bus 003 Device 006: ID 8087:0033 Intel Corp. AX211 Bluetooth
    Bus 004 Device 001: ID 1d6b:0003 Linux Foundation 3.0 root hub

`root `[`#`]`lsusb -tv`

    D 1d6b:0002 Linux Foundation 2.0 root hub
        |__ Port 003: Dev 002, If 0, Class=Vendor Specific Class, Driver=[none], 12M
            ID 06cb:0126 Synaptics, Inc.
        |__ Port 004: Dev 003, If 0, Class=Video, Driver=uvcvideo, 480M
            ID 174f:11a8 Syntek
        |__ Port 004: Dev 003, If 1, Class=Video, Driver=uvcvideo, 480M
            ID 174f:11a8 Syntek
        |__ Port 004: Dev 003, If 2, Class=Video, Driver=uvcvideo, 480M
            ID 174f:11a8 Syntek
        |__ Port 004: Dev 003, If 3, Class=Video, Driver=uvcvideo, 480M
            ID 174f:11a8 Syntek
        |__ Port 004: Dev 003, If 4, Class=Application Specific Interface, Driver=[none], 480M
            ID 174f:11a8 Syntek
        |__ Port 010: Dev 006, If 0, Class=Wireless, Driver=btusb, 12M
            ID 8087:0033 Intel Corp. AX211 Bluetooth
        |__ Port 010: Dev 006, If 1, Class=Wireless, Driver=btusb, 12M
            ID 8087:0033 Intel Corp. AX211 Bluetooth
    /:  Bus 004.Port 001: Dev 001, Class=root_hub, Driver=xhci_hcd/4p, 10000M
        ID 1d6b:0003 Linux Foundation 3.0 root hub

## [Troubleshooting]

### [Lagging screen]

If experiencing laggy screen, a possible solution is to add the following line:

[FILE] **`/etc/modprobe.d/i915.conf`**

    options i915 enable_psr=0

## [References]

1.  [[[↑](#cite_ref-1)] [[https://news.lenovo.com/pressroom/press-releases/lenovos-latest-workstations-push-the-limits-of-creative-productivity/](https://news.lenovo.com/pressroom/press-releases/lenovos-latest-workstations-push-the-limits-of-creative-productivity/)]]