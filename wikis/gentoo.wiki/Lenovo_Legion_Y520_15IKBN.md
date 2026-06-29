**Resources**

[[]][Official Support Page](https://pcsupport.lenovo.com/us/en/products/laptops-and-netbooks/legion-series/legion-y520-15ikbn)

[[]][Specifications](https://psref.lenovo.com/syspool/Sys/PDF/Lenovo_Laptops/Lenovo_Legion_Y520_15/Lenovo_Legion_Y520_15_Spec.PDF)

[[]][Specifications (by region)](https://psref.lenovo.com/Product/Legion/Lenovo_Legion_Y520_15)

[[]][Hardware Maintenance Manual](https://download.lenovo.com/consumer/mobiles_pub/legion_y520-15ikbn_hmm_201701.pdf)

[[]][User Guide](https://download.lenovo.com/consumer/mobiles_pub/legion_y520-15ikbn_ug_en_201701.pdf)

[[]][Lenovo Legion](https://en.wikipedia.org/wiki/Lenovo_Legion "wikipedia:Lenovo Legion")

The **Lenovo Legion Y520 15IKBN** is a thin and light 15.6-inch workstation/multimedia laptop from Lenovo\'s 2017 Legion lineup. The laptop has a solid build, a good keyboard and a nice 15-inch 1920x1080 Full HD IPS display with LED backlighting and anti-glare coating. Once properly configured, all parts of the laptop are Linux friendly.

## Contents

-   [[1] [Hardware]](#Hardware)
    -   [[1.1] [Standard]](#Standard)
-   [[2] [Installation]](#Installation)
    -   [[2.1] [Firmware]](#Firmware)
    -   [[2.2] [Kernel]](#Kernel)
    -   [[2.3] [Emerge]](#Emerge)

## [Hardware]

### [Standard]

  ---------------- ------------------------------------------------------------ -------- ------------------------ ------------------ ---------------- -------
  Device           Make/model                                                   Status   Vendor ID / Product ID   Kernel driver(s)   Kernel version   Notes
  CPU              Intel® Core™ i7-7700HQ                                       Works    N/A                      N/A                5.7.10
  GPU              Intel Corporation HD Graphics 630                            Works    8086:591b                i915               5.7.10
  SSD              Samsung Electronics Co Ltd NVMe SSD Controller SM961/PM961   Works    144d:a804                nvme               5.7.10
  Wi-Fi            Intel Corporation Wireless 8265 / 8275                       Works    8086:24fd                iwlwifi            5.7.10
  Audio            Intel Corporation CM238 HD Audio Controller                  Works    8086:a171                snd_hda_intel      5.7.10
  Camera           Chicony Electronics Co., Ltd EasyCamera                      Works    04f2:b57e                uvcvideo           5.7.10
  Touchpad         ETPS/2 Elantech Touchpad                                     Works    0002:000e                psmouse            5.7.10
  SD Card Reader   O2 Micro, Inc. SD/MMC Card Reader Controller                 Works    1217:8621                sdhci-pci          5.7.10
  ---------------- ------------------------------------------------------------ -------- ------------------------ ------------------ ---------------- -------

`root `[`#`]`lscpu`

    Architecture:                    x86_64
    CPU op-mode(s):                  32-bit, 64-bit
    Byte Order:                      Little Endian
    Address sizes:                   39 bits physical, 48 bits virtual
    CPU(s):                          8
    On-line CPU(s) list:             0-7
    Thread(s) per core:              2
    Core(s) per socket:              4
    Socket(s):                       1
    NUMA node(s):                    1
    Vendor ID:                       GenuineIntel
    CPU family:                      6
    Model:                           158
    Model name:                      Intel(R) Core(TM) i7-7700HQ CPU @ 2.80GHz
    Stepping:                        9
    CPU MHz:                         3500.752
    CPU max MHz:                     3800.0000
    CPU min MHz:                     800.0000
    BogoMIPS:                        5599.85
    Virtualization:                  VT-x
    L1d cache:                       128 KiB
    L1i cache:                       128 KiB
    L2 cache:                        1 MiB
    L3 cache:                        6 MiB
    NUMA node0 CPU(s):               0-7
    Vulnerability Itlb multihit:     Processor vulnerable
    Vulnerability L1tf:              Mitigation; PTE Inversion
    Vulnerability Mds:               Vulnerable: Clear CPU buffers attempted, no microcode; SMT vulnerable
    Vulnerability Meltdown:          Mitigation; PTI
    Vulnerability Spec store bypass: Vulnerable
    Vulnerability Spectre v1:        Mitigation; usercopy/swapgs barriers and __user pointer sanitization
    Vulnerability Spectre v2:        Mitigation; Full generic retpoline, STIBP disabled, RSB filling
    Vulnerability Srbds:             Vulnerable: No microcode
    Vulnerability Tsx async abort:   Not affected
    Flags:                           fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush dts acpi mmx fxsr sse sse2
                                     ss ht tm pbe syscall nx pdpe1gb rdtscp lm constant_tsc art arch_perfmon pebs bts rep_good nopl xtopology no
                                     nstop_tsc cpuid aperfmperf pni pclmulqdq dtes64 monitor ds_cpl vmx est tm2 ssse3 sdbg fma cx16 xtpr pdcm pc
                                     id sse4_1 sse4_2 x2apic movbe popcnt tsc_deadline_timer aes xsave avx f16c rdrand lahf_lm abm 3dnowprefetch
                                      cpuid_fault invpcid_single pti tpr_shadow vnmi flexpriority ept vpid ept_ad fsgsbase tsc_adjust bmi1 avx2
                                     smep bmi2 erms invpcid mpx rdseed adx smap clflushopt intel_pt xsaveopt xsavec xgetbv1 xsaves dtherm ida ar
                                     at pln pts hwp hwp_notify hwp_act_window hwp_epp

`root `[`#`]`lspci -nnk`

    00:00.0 Host bridge [0600]: Intel Corporation Xeon E3-1200 v6/7th Gen Core Processor Host Bridge/DRAM Registers [8086:5910] (rev 05)
        Subsystem: Lenovo Xeon E3-1200 v6/7th Gen Core Processor Host Bridge/DRAM Registers [17aa:3804]
        Kernel driver in use: skl_uncore
    00:01.0 PCI bridge [0604]: Intel Corporation Xeon E3-1200 v5/E3-1500 v5/6th Gen Core Processor PCIe Controller (x16) [8086:1901] (rev 05)
        Kernel driver in use: pcieport
    00:02.0 VGA compatible controller [0300]: Intel Corporation HD Graphics 630 [8086:591b] (rev 04)
        Subsystem: Lenovo HD Graphics 630 [17aa:39fc]
        Kernel driver in use: i915
        Kernel modules: i915
    00:14.0 USB controller [0c03]: Intel Corporation 100 Series/C230 Series Chipset Family USB 3.0 xHCI Controller [8086:a12f] (rev 31)
        Subsystem: Lenovo 100 Series/C230 Series Chipset Family USB 3.0 xHCI Controller [17aa:381d]
        Kernel driver in use: xhci_hcd
        Kernel modules: xhci_pci
    00:14.2 Signal processing controller [1180]: Intel Corporation 100 Series/C230 Series Chipset Family Thermal Subsystem [8086:a131] (rev 31)
        Subsystem: Lenovo 100 Series/C230 Series Chipset Family Thermal Subsystem [17aa:3805]
        Kernel driver in use: intel_pch_thermal
        Kernel modules: intel_pch_thermal
    00:16.0 Communication controller [0780]: Intel Corporation 100 Series/C230 Series Chipset Family MEI Controller #1 [8086:a13a] (rev 31)
        Subsystem: Lenovo 100 Series/C230 Series Chipset Family MEI Controller [17aa:381e]
        Kernel driver in use: mei_me
        Kernel modules: mei_me
    00:17.0 SATA controller [0106]: Intel Corporation HM170/QM170 Chipset SATA Controller [AHCI Mode] [8086:a103] (rev 31)
        Subsystem: Lenovo HM170/QM170 Chipset SATA Controller [AHCI Mode] [17aa:3803]
        Kernel driver in use: ahci
        Kernel modules: ahci
    00:1c.0 PCI bridge [0604]: Intel Corporation 100 Series/C230 Series Chipset Family PCI Express Root Port #2 [8086:a111] (rev f1)
        Kernel driver in use: pcieport
    00:1c.2 PCI bridge [0604]: Intel Corporation 100 Series/C230 Series Chipset Family PCI Express Root Port #3 [8086:a112] (rev f1)
        Kernel driver in use: pcieport
    00:1c.3 PCI bridge [0604]: Intel Corporation 100 Series/C230 Series Chipset Family PCI Express Root Port #4 [8086:a113] (rev f1)
        Kernel driver in use: pcieport
    00:1d.0 PCI bridge [0604]: Intel Corporation 100 Series/C230 Series Chipset Family PCI Express Root Port #9 [8086:a118] (rev f1)
        Kernel driver in use: pcieport
    00:1f.0 ISA bridge [0601]: Intel Corporation HM175 Chipset LPC/eSPI Controller [8086:a152] (rev 31)
        Subsystem: Lenovo HM175 Chipset LPC/eSPI Controller [17aa:3803]
    00:1f.2 Memory controller [0580]: Intel Corporation 100 Series/C230 Series Chipset Family Power Management Controller [8086:a121] (rev 31)
        Subsystem: Lenovo 100 Series/C230 Series Chipset Family Power Management Controller [17aa:3819]
    00:1f.3 Audio device [0403]: Intel Corporation CM238 HD Audio Controller [8086:a171] (rev 31)
        Subsystem: Lenovo CM238 HD Audio Controller [17aa:3803]
        Kernel driver in use: snd_hda_intel
        Kernel modules: snd_hda_intel
    00:1f.4 SMBus [0c05]: Intel Corporation 100 Series/C230 Series Chipset Family SMBus [8086:a123] (rev 31)
        Subsystem: Lenovo 100 Series/C230 Series Chipset Family SMBus [17aa:3817]
        Kernel driver in use: i801_smbus
        Kernel modules: i2c_i801
    02:00.0 SD Host controller [0805]: O2 Micro, Inc. SD/MMC Card Reader Controller [1217:8621] (rev 01)
        Subsystem: Lenovo SD/MMC Card Reader Controller [17aa:381f]
        Kernel driver in use: sdhci-pci
        Kernel modules: sdhci_pci
    03:00.0 Network controller [0280]: Intel Corporation Wireless 8265 / 8275 [8086:24fd] (rev 78)
        Subsystem: Intel Corporation Dual Band Wireless-AC 8265 [8086:1010]
        Kernel driver in use: iwlwifi
        Kernel modules: iwlwifi
    04:00.0 Ethernet controller [0200]: Realtek Semiconductor Co., Ltd. RTL8111/8168/8411 PCI Express Gigabit Ethernet Controller [10ec:8168] (rev 10)
        Subsystem: Lenovo RTL8111/8168/8411 PCI Express Gigabit Ethernet Controller [17aa:3884]
        Kernel driver in use: r8169
        Kernel modules: r8169
    05:00.0 Non-Volatile memory controller [0108]: Samsung Electronics Co Ltd NVMe SSD Controller SM961/PM961 [144d:a804]
        Subsystem: Samsung Electronics Co Ltd NVMe SSD Controller SM961/PM961 [144d:a801]
        Kernel driver in use: nvme
        Kernel modules: nvme

`root `[`#`]`lsusb`

    Bus 001 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub
    Bus 001 Device 004: ID 04f2:b57e Chicony Electronics Co., Ltd EasyCamera
    Bus 001 Device 005: ID 8087:0a2b Intel Corp. Bluetooth wireless interface
    Bus 002 Device 001: ID 1d6b:0003 Linux Foundation 3.0 root hub

`root `[`#`]`lsinput`

     0: 0000:0005 HOST   PNP0C0D/button/i Lid Switch               SW
     1: 0000:0001 HOST   PNP0C0C/button/i Power Button             KEY
     2: 0000:0001 HOST   LNXPWRBN/button/ Power Button             KEY
     3: 0001:0001 I8042  isa0060/serio0/i AT Translated Set 2 keyb KEY MSC LED
     8: 0000:0006 HOST   LNXVIDEO/video/i Video Bus                KEY
     9: 04f2:b57e USB    usb-0000:00:14.0 EasyCamera: EasyCamera   KEY
    10: 0002:000e I8042  isa0060/serio1/i ETPS/2 Elantech Touchpad KEY ABS

## [Installation]

### [Firmware]

[Intel microcode](https://wiki.gentoo.org/wiki/Intel_microcode "Intel microcode"):

`root `[`#`]`emerge --ask sys-firmware/intel-microcode`

### [Kernel]

[KERNEL] **CPU (kernel 5.7.10):**

    Processor type and features  --->
       [*] Symmetric multi-processing support
           Processor family ()  --->
               (X) Core 2/newer Xeon
       (8) Maximum number of CPUs
       -*- MTRR (Memory Type Range Register) support

[KERNEL] **SSD:**

    Device Drivers  --->
       NVME Support  --->
           <*> NVM Express block device
           [*] NVMe multipath support
           [*] NVMe hardware monitoring
           < > NVM Express over Fabrics FC host driver
           < > NVM Express over Fabrics TCP host driver

[KERNEL] **Sound:**

    Device Drivers  --->
       <*> Sound card support  --->
         <*> Advanced Linux Sound Architecture  --->
           HD-Audio  --->
             <*> HD Audio PCI
             [*] Build hwdep interface for HD-audio driver
             [ ] Allow dynamic codec reconfiguration
             [ ] Support digital beep via input layer
             [ ] Support initialization patch loading for HD-audio
             <*> Build Realtek HD-audio codec support
             < > Build Analog Device HD-audio codec support
             < > Build IDT/Sigmatel HD-audio codec support
             < > Build VIA HD-audio codec support
             <*> Build HDMI/DisplayPort HD-audio codec support
             < > Build Cirrus Logic codec support
             < > Build Conexant HD-audio codec support
             < > Build Creative CA0110-IBG codec support
             < > Build Creative CA0132 codec support
             < > Build C-Media HD-audio codec support
             < > Build Silicon Labs 3054 HD-modem codec support
             -*- Enable generic HD-audio codec parser
             (0) Default time-out for HD-audio power-save mode

[KERNEL] **USB:**

    Device Drivers --->
        [*] USB support --->
               Support for Host-side USB
            [*]   PCI based USB host interface
            [*]   USB announce new devices
                  *** Miscellaneous USB options ***
            [*]   Enable USB persist by default
            <*>   xHCI HCD (USB 3.0) support
            [ ]     xHCI support for debug capability
            <*>     Generic xHCI driver for a platform device
            <*>   EHCI HCD (USB 2.0) support
            [ ]     Root Hub Transaction Translators
            [*]     Improved Transaction Translator scheduling

### [Emerge]

[FILE] **`/etc/portage/make.conf`**

    # amd64 architecture
    CHOST="x86_64-pc-linux-gnu"

    # Obtained via cpuinfo2cpuflags (Intel® Core™ i7-7700HQ)
    CPU_FLAGS_X86="aes avx avx2 f16c fma3 mmx mmxext pclmul popcnt rdrand sse sse2 sse3 sse4_1 sse4_2 ssse3"

    # -O2 for super-safe output
    COMMON_FLAGS="-march=skylake -O2 -pipe"

    CFLAGS="$"
    CXXFLAGS="$"
    FCFLAGS="$"
    FFLAGS="$"

    ACCEPT_KEYWORDS="~amd64"

    # Quad-core with enabled Hyper-Threading technology - 8 logical processors
    MAKEOPTS="-j8"

    # Input devices
    INPUT_DEVICES="libinput"

    # Intel GMA Gen 9.5 - Kaby Lake
    VIDEO_CARDS="intel i965 iris"

    # Optinal
    GRUB_PLATFORMS="efi-64"

    # Intel Microcode
    MICROCODE_SIGNATURES="-S"