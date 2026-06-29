**Resources**

[[]][Official Support Page](https://support.hp.com/us-en/product/details/hp-pavilion-15-au600-notebook-pc/model/14057671)

[[]][Specifications](https://support.hp.com/in-en/document/c05349012)

[[]][Hardware Maintenance Manual](https://h10032.www1.hp.com/ctg/Manual/c05228250.pdf)

[[]][User Guide](https://h10032.www1.hp.com/ctg/Manual/c06195629.pdf)

[[]][HP Pavilion](https://en.wikipedia.org/wiki/HP_Pavilion "wikipedia:HP Pavilion")

Information about how to install/configure Gentoo GNU/Linux in HP Pavillion au624tx Notebook

## Contents

-   [[1] [lscpu]](#lscpu)
-   [[2] [lspci]](#lspci)
-   [[3] [lsusb]](#lsusb)
-   [[4] [Installation]](#Installation)
    -   [[4.1] [Firmware]](#Firmware)
        -   [[4.1.1] [WiFi and BLuetooth]](#WiFi_and_BLuetooth)
        -   [[4.1.2] [Microcode]](#Microcode)
        -   [[4.1.3] [Kernel]](#Kernel)
-   [[5] [Configuration]](#Configuration)
    -   [[5.1] [Compiler settings]](#Compiler_settings)
    -   [[5.2] [Packages settings]](#Packages_settings)
    -   [[5.3] [USE flags]](#USE_flags)
-   [[6] [Utils and Extras]](#Utils_and_Extras)
    -   [[6.1] [Enabling Mute LED light]](#Enabling_Mute_LED_light)
    -   [[6.2] [Optimize system]](#Optimize_system)
    -   [[6.3] [Extra notes on Uefi settings]](#Extra_notes_on_Uefi_settings)

#### [lscpu]

`user `[`$`]`lscpu`

    Architecture:                    x86_64
    CPU op-mode(s):                  32-bit, 64-bit
    Byte Order:                      Little Endian
    Address sizes:                   39 bits physical, 48 bits virtual
    CPU(s):                          4
    On-line CPU(s) list:             0,1
    Off-line CPU(s) list:            2,3
    Thread(s) per core:              1
    Core(s) per socket:              2
    Socket(s):                       1
    NUMA node(s):                    1
    Vendor ID:                       GenuineIntel
    CPU family:                      6
    Model:                           142
    Model name:                      Intel(R) Core(TM) i5-7200U CPU @ 2.50GHz
    Stepping:                        9
    CPU MHz:                         800.033
    CPU max MHz:                     3100.0000
    CPU min MHz:                     400.0000
    BogoMIPS:                        5399.81
    Virtualization:                  VT-x
    L1d cache:                       64 KiB
    L1i cache:                       64 KiB
    L2 cache:                        512 KiB
    L3 cache:                        3 MiB
    NUMA node0 CPU(s):               0,1
    Vulnerability Itlb multihit:     KVM: Mitigation: Split huge pages
    Vulnerability L1tf:              Mitigation; PTE Inversion; VMX conditional cach
                                     e flushes, SMT disabled
    Vulnerability Mds:               Mitigation; Clear CPU buffers; SMT disabled
    Vulnerability Meltdown:          Mitigation; PTI
    Vulnerability Spec store bypass: Mitigation; Speculative Store Bypass disabled v
                                     ia prctl and seccomp
    Vulnerability Spectre v1:        Mitigation; usercopy/swapgs barriers and __user
                                      pointer sanitization
    Vulnerability Spectre v2:        Mitigation; Full generic retpoline, IBPB condit
                                     ional, IBRS_FW, RSB filling
    Vulnerability Srbds:             Mitigation; Microcode
    Vulnerability Tsx async abort:   Not affected
    Flags:                           fpu vme de pse tsc msr pae mce cx8 apic sep mtr
                                     r pge mca cmov pat pse36 clflush dts acpi mmx f
                                     xsr sse sse2 ss ht tm pbe syscall nx pdpe1gb rd
                                     tscp lm constant_tsc art arch_perfmon pebs bts
                                     rep_good nopl xtopology nonstop_tsc cpuid aperf
                                     mperf pni pclmulqdq dtes64 monitor ds_cpl vmx e
                                     st tm2 ssse3 sdbg fma cx16 xtpr pdcm pcid sse4_
                                     1 sse4_2 x2apic movbe popcnt tsc_deadline_timer
                                      aes xsave avx f16c rdrand lahf_lm abm 3dnowpre
                                     fetch cpuid_fault epb invpcid_single pti ssbd i
                                     brs ibpb stibp tpr_shadow vnmi flexpriority ept
                                      vpid ept_ad fsgsbase tsc_adjust bmi1 avx2 smep
                                      bmi2 erms invpcid mpx rdseed adx smap clflusho
                                     pt intel_pt xsaveopt xsavec xgetbv1 xsaves dthe
                                     rm ida arat pln pts hwp hwp_notify hwp_act_wind
                                     ow hwp_epp md_clear flush_l1d

#### [lspci]

`root `[`#`]`lspci`

    00:00.0 Host bridge: Intel Corporation Xeon E3-1200 v6/7th Gen Core Processor Host Bridge/DRAM Registers (rev 02)
    00:02.0 VGA compatible controller: Intel Corporation HD Graphics 620 (rev 02)
    00:04.0 Signal processing controller: Intel Corporation Xeon E3-1200 v5/E3-1500 v5/6th Gen Core Processor Thermal Subsystem (rev 02)
    00:14.0 USB controller: Intel Corporation Sunrise Point-LP USB 3.0 xHCI Controller (rev 21)
    00:14.2 Signal processing controller: Intel Corporation Sunrise Point-LP Thermal subsystem (rev 21)
    00:16.0 Communication controller: Intel Corporation Sunrise Point-LP CSME HECI #1 (rev 21)
    00:17.0 SATA controller: Intel Corporation Sunrise Point-LP SATA Controller [AHCI mode] (rev 21)
    00:1c.0 PCI bridge: Intel Corporation Sunrise Point-LP PCI Express Root Port #1 (rev f1)
    00:1c.4 PCI bridge: Intel Corporation Sunrise Point-LP PCI Express Root Port #5 (rev f1)
    00:1c.5 PCI bridge: Intel Corporation Sunrise Point-LP PCI Express Root Port #6 (rev f1)
    00:1d.0 PCI bridge: Intel Corporation Sunrise Point-LP PCI Express Root Port #9 (rev f1)
    00:1d.3 PCI bridge: Intel Corporation Device 9d1b (rev f1)
    00:1f.0 ISA bridge: Intel Corporation Sunrise Point-LP LPC Controller (rev 21)
    00:1f.2 Memory controller: Intel Corporation Sunrise Point-LP PMC (rev 21)
    00:1f.3 Audio device: Intel Corporation Sunrise Point-LP HD Audio (rev 21)
    00:1f.4 SMBus: Intel Corporation Sunrise Point-LP SMBus (rev 21)
    01:00.0 3D controller: NVIDIA Corporation GM108M [GeForce 940MX] (rev a2)
    02:00.0 Unassigned class [ff00]: Realtek Semiconductor Co., Ltd. RTS522A PCI Express Card Reader (rev 01)
    03:00.0 Ethernet controller: Realtek Semiconductor Co., Ltd. RTL810xE PCI Express Fast Ethernet controller (rev 0a)
    05:00.0 Network controller: Intel Corporation Dual Band Wireless-AC 3168NGW [Stone Peak] (rev 10)

#### [lsusb]

`user `[`$`]`lsusb`

    Bus 002 Device 001: ID 1d6b:0003 Linux Foundation 3.0 root hub
    Bus 001 Device 003: ID 8087:0aa7 Intel Corp.
    Bus 001 Device 002: ID 0408:5090 Quanta Computer, Inc. HP Wide version HD
    Bus 001 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub

## [Installation]

#### [Firmware]

###### [WiFi and BLuetooth]

The Linux firmware package is needed for wifi adapter to work.

It can be obtained by installing the Linux firmware package: [[[sys-firmware/linux-firmware]](https://packages.gentoo.org/packages/sys-firmware/linux-firmware)[]]. For more info see [iwlwifi](https://wiki.gentoo.org/wiki/Iwlwifi "Iwlwifi").

\

##### [Microcode]

Intel released microcode updates that fixes fault on processors. Install the officially published microcode package [[[sys-firmware/intel-microcode]](https://packages.gentoo.org/packages/sys-firmware/intel-microcode)[]]. For more info see [Intel microcode](https://wiki.gentoo.org/wiki/Intel_microcode "Intel microcode").

\

##### [Kernel]

Recommended kernel config for [[[sys-linux/gentoo-sources]](https://packages.gentoo.org/packages/sys-linux/gentoo-sources)[]]. More info at [Kernel](https://wiki.gentoo.org/wiki/Kernel "Kernel").

** Note**\
This config is last tested on Linux Kernel [[[sys-linux/gentoo-sources]](https://packages.gentoo.org/packages/sys-linux/gentoo-sources)[]] 5.4.60

\
Kernel config being maintained at [au624tx_defconfig](https://github.com/kumarayush2104/au624tx_defconfig)

## [Configuration]

##### [Compiler settings]

More info is available at:

-   [GCC optimization](https://wiki.gentoo.org/wiki/GCC_optimization "GCC optimization")
-   [MAKEOPTS](https://wiki.gentoo.org/wiki/MAKEOPTS "MAKEOPTS")
-   [EMERGE_DEFAULT_OPTS](https://wiki.gentoo.org/wiki/EMERGE_DEFAULT_OPTS "EMERGE DEFAULT OPTS")

[FILE] **`/etc/portage/make.conf`**

    # O2 for super-safe output
    CFLAGS="-march=native -O2 -pipe"
    CXXFLAGS="$"
    # Dual-core with enabled Hyper-Threading technology - 4 logical processors
    MAKEOPTS="-j4"
    # AMD64 architecture
    CHOST="x86_64-pc-linux-gnu"

\

##### [Packages settings]

For more info: [CPU_FLAGS_X86](https://wiki.gentoo.org/wiki/CPU_FLAGS_X86 "CPU FLAGS X86")

[FILE] **`/etc/portage/package.use/00cpu-flags`**

    */* CPU_FLAGS_X86: aes avx2 mmx popcnt sse sse2 sse3 sse4_1 sse4_2 ssse3 mmxext avx

##### [USE flags]

With [Intel Modesetting DDX](https://wiki.gentoo.org/wiki/Intel "Intel") as video driver and [libinput](https://wiki.gentoo.org/wiki/Libinput "Libinput") as input driver add the USE flags `glamor` and `libinput`.

[FILE] **`/etc/portage/package.use/00video`**

    */* VIDEO_CARDS: -* intel i965
    ## only if you are going to configure dedicated gpu
    */* VIDEO_CARDS: -* nouveau

[FILE] **`/etc/portage/package.use/00input`**

    */* INPUT_DEVICES: libinput

## [Utils and Extras]

#### [Enabling Mute LED light]

Create the following file:-

[FILE] **`/etc/modprobe.d/snd-hda-intel.conf`**

    ## Enabling Mute LED for Hp Pavillion Notebooks Containing Realtek ALC295 Audio Card
    options snd-hda-intel model=alc295-hp-x360

#### [Optimize system]

Use [[[app-laptop/laptop-mode-tools]](https://packages.gentoo.org/packages/app-laptop/laptop-mode-tools)[]], For more info check [Power_management](https://wiki.gentoo.org/wiki/Power_management "Power management")

#### [Extra notes on Uefi settings]

Do not disable \"Fan Always ON\" from UEFI settings, since Operating Systems (Other than Windows) are not able to disable ACPI fan, causing battery drain even after shutting down.