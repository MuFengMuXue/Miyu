[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=ASUSTek_ROG_Zephyrus_G14_GA401&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

This is an article about running Gentoo on an Asus ROG Zephyrus G14 GA401 series laptop.

## Contents

-   [[1] [Laptop Specifications]](#Laptop_Specifications)
-   [[2] [Hardware Support]](#Hardware_Support)
    -   [[2.1] [Input Devices]](#Input_Devices)
    -   [[2.2] [Drives and Storage]](#Drives_and_Storage)
    -   [[2.3] [Graphics Chip]](#Graphics_Chip)
    -   [[2.4] [WLAN Card]](#WLAN_Card)
    -   [[2.5] [CPU Frequency Scaling]](#CPU_Frequency_Scaling)
    -   [[2.6] [Sensors]](#Sensors)
    -   [[2.7] [Touchpad]](#Touchpad)
    -   [[2.8] [Sound Chip]](#Sound_Chip)
    -   [[2.9] [Fingerprint reader]](#Fingerprint_reader)
    -   [[2.10] [Sleep Mode]](#Sleep_Mode)
-   [[3] [Software]](#Software)
    -   [[3.1] [Linux asusctl]](#Linux_asusctl)

## [Laptop Specifications]

Hardware specs may vary. These are the specs for the model ASUSTek ROG Zephyrus G14 GA401QC:

-   AMD Ryzen 7 5800HS with Radeon Graphics L3 Cache: 16 MB, Clock: 2.2GB (base) 4.4 (turbo), 8 core / 16 Thread.
-   16GB DDR4 RAM (2 slots)
-   AMD Renoir Graphics (on-CPU) + NVIDIA GA107M \[GeForce RTX 3050 Mobile\] (Dedicated)
-   Integrated Renoir Radeon High Definition Audio
-   Audio Connections: 3.5mm
-   1 Fingerprint Reader
-   14in TFT LCD Screen FHD 1920x1080 120 Hz
-   512GB SSD Intel NVME 660P Series Hard Disk
-   2x USB A 3.2
-   2x USB Type C 3.2, USB-C Power Delivery (PD),
-   HDMI output
-   MEDIATEK WIFI Device 7961
-   Bluetooth 5.1
-   Keyboard LED with adjustable brightness
-   ELAN1201 Touchpad

Printout of lspci:

`root `[`#`]`lspci`

    00:00.0 Host bridge: Advanced Micro Devices, Inc. [AMD] Renoir/Cezanne Root Complex
    00:00.2 IOMMU: Advanced Micro Devices, Inc. [AMD] Renoir/Cezanne IOMMU
    00:01.0 Host bridge: Advanced Micro Devices, Inc. [AMD] Renoir PCIe Dummy Host Bridge
    00:01.1 PCI bridge: Advanced Micro Devices, Inc. [AMD] Renoir PCIe GPP Bridge
    00:02.0 Host bridge: Advanced Micro Devices, Inc. [AMD] Renoir PCIe Dummy Host Bridge
    00:02.2 PCI bridge: Advanced Micro Devices, Inc. [AMD] Renoir/Cezanne PCIe GPP Bridge
    00:02.4 PCI bridge: Advanced Micro Devices, Inc. [AMD] Renoir/Cezanne PCIe GPP Bridge
    00:08.0 Host bridge: Advanced Micro Devices, Inc. [AMD] Renoir PCIe Dummy Host Bridge
    00:08.1 PCI bridge: Advanced Micro Devices, Inc. [AMD] Renoir Internal PCIe GPP Bridge to Bus
    00:14.0 SMBus: Advanced Micro Devices, Inc. [AMD] FCH SMBus Controller (rev 51)
    00:14.3 ISA bridge: Advanced Micro Devices, Inc. [AMD] FCH LPC Bridge (rev 51)
    00:18.0 Host bridge: Advanced Micro Devices, Inc. [AMD] Cezanne Data Fabric; Function 0
    00:18.1 Host bridge: Advanced Micro Devices, Inc. [AMD] Cezanne Data Fabric; Function 1
    00:18.2 Host bridge: Advanced Micro Devices, Inc. [AMD] Cezanne Data Fabric; Function 2
    00:18.3 Host bridge: Advanced Micro Devices, Inc. [AMD] Cezanne Data Fabric; Function 3
    00:18.4 Host bridge: Advanced Micro Devices, Inc. [AMD] Cezanne Data Fabric; Function 4
    00:18.5 Host bridge: Advanced Micro Devices, Inc. [AMD] Cezanne Data Fabric; Function 5
    00:18.6 Host bridge: Advanced Micro Devices, Inc. [AMD] Cezanne Data Fabric; Function 6
    00:18.7 Host bridge: Advanced Micro Devices, Inc. [AMD] Cezanne Data Fabric; Function 7
    01:00.0 VGA compatible controller [0300]: NVIDIA Corporation [10de]. GA107M [GeForce RTX 3050 Mobile]
    02:00.0 Network controller: MEDIATEK Corp. Device 7961
    03:00.0 Non-Volatile memory controller: Samsung Electronics Co Ltd NVMe SSD Controller SM981/PM981/PM983
    04:00.0 VGA compatible controller: Advanced Micro Devices, Inc. [AMD/ATI] Cezanne (rev c5)
    04:00.1 Audio device: Advanced Micro Devices, Inc. [AMD/ATI] Renoir Radeon High Definition Audio Controller
    04:00.2 Encryption controller: Advanced Micro Devices, Inc. [AMD] Family 17h (Models 10h-1fh) Platform Security Processor
    04:00.3 USB controller: Advanced Micro Devices, Inc. [AMD] Renoir/Cezanne USB 3.1
    04:00.4 USB controller: Advanced Micro Devices, Inc. [AMD] Renoir/Cezanne USB 3.1
    04:00.5 Multimedia controller: Advanced Micro Devices, Inc. [AMD] Raven/Raven2/FireFlight/Renoir Audio Processor (rev 01)
    04:00.6 Audio device: Advanced Micro Devices, Inc. [AMD] Family 17h (Models 10h-1fh) HD Audio Controller

Printout of lsusb (builtin devices, no external devices connected):

`root `[`#`]`lsusb`

    Bus 004 Device 001: ID 1d6b:0003 Linux Foundation 3.0 root hub
    Bus 003 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub
    Bus 002 Device 001: ID 1d6b:0003 Linux Foundation 3.0 root hub
    Bus 001 Device 002: ID 0b05:19b6 ASUSTek Computer, Inc. N-KEY Device
    Bus 001 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub

Printout of lsmod (builtin devices, no external devices connected and excluding nvidia drivers):

`root `[`#`]`lsmod`

    leho@travelmate ~ $ lsmod | sort
    amdgpu               6520832  509
    asus_nb_wmi            28672  0
    asus_wireless          16384  0
    asus_wmi               49152  2 asus_nb_wmi,hid_asus
    configfs               40960  1
    dax                    28672  1 dm_mod
    deflate                16384  1
    dm_crypt               45056  1
    dm_mod                126976  3 dm_crypt
    drm_dp_helper         110592  1 amdgpu
    drm_kms_helper        143360  4 drm_dp_helper,amdgpu
    drm_ttm_helper         16384  1 amdgpu
    efi_pstore             16384  0
    efivarfs               16384  1
    fb_sys_fops            16384  1 drm_kms_helper
    fuse                  139264  3
    gpu_sched              45056  1 amdgpu
    hid_asus               24576  0
    hid_multitouch         28672  0
    i2c_designware_core    28672  1 i2c_designware_platform
    i2c_designware_platform    20480  0
    i2c_piix4              24576  0
    joydev                 24576  0
    mfd_core               16384  1 amdgpu
    Module                  Size  Used by
    mt76                   73728  3 mt7921e,mt7921_common,mt76_connac_lib
    mt76_connac_lib        40960  2 mt7921e,mt7921_common
    mt7921_common          81920  1 mt7921e
    mt7921e                32768  0
    pinctrl_amd            28672  6
    platform_profile       16384  1 asus_wmi
    pstore                 28672  1 efi_pstore
    roles                  16384  1 typec_ucsi
    snd_acp_config         16384  1 snd_rn_pci_acp3x
    snd_hda_codec_hdmi     65536  0
    snd_rn_pci_acp3x       16384  0
    snd_soc_acpi           16384  1 snd_acp_config
    syscopyarea            16384  1 drm_kms_helper
    sysfillrect            16384  1 drm_kms_helper
    sysimgblt              16384  1 drm_kms_helper
    ttm                    65536  2 amdgpu,drm_ttm_helper
    typec                  45056  1 typec_ucsi
    typec_ucsi             32768  1 ucsi_acpi
    uas                    28672  0
    ucsi_acpi              16384  0
    wmi                    24576  2 asus_wmi,wmi_bmof
    wmi_bmof               16384  0
    xhci_pci               20480  0
    xhci_pci_renesas       16384  1 xhci_pci
    zlib_deflate           28672  1 deflate

Information from [/proc/cpuinfo] :

`user `[`$`]`cat /proc/cpuinfo`

    processor   : 0
    vendor_id   : AuthenticAMD
    cpu family  : 25
    model       : 80
    model name  : AMD Ryzen 7 5800HS with Radeon Graphics
    stepping    : 0
    microcode   : 0xa50000c
    cpu MHz     : 1300.000
    cache size  : 512 KB
    physical id : 0
    siblings    : 16
    core id     : 0
    cpu cores   : 8
    apicid      : 0
    initial apicid  : 0
    fpu     : yes
    fpu_exception   : yes
    cpuid level : 16
    wp      : yes
    flags       : fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush mmx fxsr sse sse2 ht syscall nx mmxext fxsr_opt pdpe1gb rdtscp lm constant_tsc rep_good nopl nonstop_tsc cpuid extd_apicid aperfmperf rapl pni pclmulqdq monitor ssse3 fma cx16 sse4_1 sse4_2 movbe popcnt aes xsave avx f16c rdrand lahf_lm cmp_legacy svm extapic cr8_legacy abm sse4a misalignsse 3dnowprefetch osvw ibs skinit wdt tce topoext perfctr_core perfctr_nb bpext perfctr_llc mwaitx cpb cat_l3 cdp_l3 hw_pstate ssbd mba ibrs ibpb stibp vmmcall fsgsbase bmi1 avx2 smep bmi2 erms invpcid cqm rdt_a rdseed adx smap clflushopt clwb sha_ni xsaveopt xsavec xgetbv1 xsaves cqm_llc cqm_occup_llc cqm_mbm_total cqm_mbm_local clzero irperf xsaveerptr rdpru wbnoinvd cppc arat npt lbrv svm_lock nrip_save tsc_scale vmcb_clean flushbyasid decodeassists pausefilter pfthreshold avic v_vmsave_vmload vgif v_spec_ctrl umip pku ospke vaes vpclmulqdq rdpid overflow_recov succor smca fsrm
    bugs        : sysret_ss_attrs spectre_v1 spectre_v2 spec_store_bypass
    bogomips    : 6388.19
    TLB size    : 2560 4K pages
    clflush size    : 64
    cache_alignment : 64
    address sizes   : 48 bits physical, 48 bits virtual
    power management: ts ttp tm hwpstate cpb eff_freq_ro [13] [14]

    processor   : 1
    vendor_id   : AuthenticAMD
    cpu family  : 25
    model       : 80
    model name  : AMD Ryzen 7 5800HS with Radeon Graphics
    stepping    : 0
    microcode   : 0xa50000c
    cpu MHz     : 1200.000
    cache size  : 512 KB
    physical id : 0
    siblings    : 16
    core id     : 0
    cpu cores   : 8
    apicid      : 1
    initial apicid  : 1
    fpu     : yes
    fpu_exception   : yes
    cpuid level : 16
    wp      : yes
    flags       : fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush mmx fxsr sse sse2 ht syscall nx mmxext fxsr_opt pdpe1gb rdtscp lm constant_tsc rep_good nopl nonstop_tsc cpuid extd_apicid aperfmperf rapl pni pclmulqdq monitor ssse3 fma cx16 sse4_1 sse4_2 movbe popcnt aes xsave avx f16c rdrand lahf_lm cmp_legacy svm extapic cr8_legacy abm sse4a misalignsse 3dnowprefetch osvw ibs skinit wdt tce topoext perfctr_core perfctr_nb bpext perfctr_llc mwaitx cpb cat_l3 cdp_l3 hw_pstate ssbd mba ibrs ibpb stibp vmmcall fsgsbase bmi1 avx2 smep bmi2 erms invpcid cqm rdt_a rdseed adx smap clflushopt clwb sha_ni xsaveopt xsavec xgetbv1 xsaves cqm_llc cqm_occup_llc cqm_mbm_total cqm_mbm_local clzero irperf xsaveerptr rdpru wbnoinvd cppc arat npt lbrv svm_lock nrip_save tsc_scale vmcb_clean flushbyasid decodeassists pausefilter pfthreshold avic v_vmsave_vmload vgif v_spec_ctrl umip pku ospke vaes vpclmulqdq rdpid overflow_recov succor smca fsrm
    bugs        : sysret_ss_attrs spectre_v1 spectre_v2 spec_store_bypass
    bogomips    : 6388.19
    TLB size    : 2560 4K pages
    clflush size    : 64
    cache_alignment : 64
    address sizes   : 48 bits physical, 48 bits virtual
    power management: ts ttp tm hwpstate cpb eff_freq_ro [13] [14]

    processor   : 2
    vendor_id   : AuthenticAMD
    cpu family  : 25
    model       : 80
    model name  : AMD Ryzen 7 5800HS with Radeon Graphics
    stepping    : 0
    microcode   : 0xa50000c
    cpu MHz     : 1200.000
    cache size  : 512 KB
    physical id : 0
    siblings    : 16
    core id     : 1
    cpu cores   : 8
    apicid      : 2
    initial apicid  : 2
    fpu     : yes
    fpu_exception   : yes
    cpuid level : 16
    wp      : yes
    flags       : fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush mmx fxsr sse sse2 ht syscall nx mmxext fxsr_opt pdpe1gb rdtscp lm constant_tsc rep_good nopl nonstop_tsc cpuid extd_apicid aperfmperf rapl pni pclmulqdq monitor ssse3 fma cx16 sse4_1 sse4_2 movbe popcnt aes xsave avx f16c rdrand lahf_lm cmp_legacy svm extapic cr8_legacy abm sse4a misalignsse 3dnowprefetch osvw ibs skinit wdt tce topoext perfctr_core perfctr_nb bpext perfctr_llc mwaitx cpb cat_l3 cdp_l3 hw_pstate ssbd mba ibrs ibpb stibp vmmcall fsgsbase bmi1 avx2 smep bmi2 erms invpcid cqm rdt_a rdseed adx smap clflushopt clwb sha_ni xsaveopt xsavec xgetbv1 xsaves cqm_llc cqm_occup_llc cqm_mbm_total cqm_mbm_local clzero irperf xsaveerptr rdpru wbnoinvd cppc arat npt lbrv svm_lock nrip_save tsc_scale vmcb_clean flushbyasid decodeassists pausefilter pfthreshold avic v_vmsave_vmload vgif v_spec_ctrl umip pku ospke vaes vpclmulqdq rdpid overflow_recov succor smca fsrm
    bugs        : sysret_ss_attrs spectre_v1 spectre_v2 spec_store_bypass
    bogomips    : 6388.19
    TLB size    : 2560 4K pages
    clflush size    : 64
    cache_alignment : 64
    address sizes   : 48 bits physical, 48 bits virtual
    power management: ts ttp tm hwpstate cpb eff_freq_ro [13] [14]

    processor   : 3
    vendor_id   : AuthenticAMD
    cpu family  : 25
    model       : 80
    model name  : AMD Ryzen 7 5800HS with Radeon Graphics
    stepping    : 0
    microcode   : 0xa50000c
    cpu MHz     : 1200.000
    cache size  : 512 KB
    physical id : 0
    siblings    : 16
    core id     : 1
    cpu cores   : 8
    apicid      : 3
    initial apicid  : 3
    fpu     : yes
    fpu_exception   : yes
    cpuid level : 16
    wp      : yes
    flags       : fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush mmx fxsr sse sse2 ht syscall nx mmxext fxsr_opt pdpe1gb rdtscp lm constant_tsc rep_good nopl nonstop_tsc cpuid extd_apicid aperfmperf rapl pni pclmulqdq monitor ssse3 fma cx16 sse4_1 sse4_2 movbe popcnt aes xsave avx f16c rdrand lahf_lm cmp_legacy svm extapic cr8_legacy abm sse4a misalignsse 3dnowprefetch osvw ibs skinit wdt tce topoext perfctr_core perfctr_nb bpext perfctr_llc mwaitx cpb cat_l3 cdp_l3 hw_pstate ssbd mba ibrs ibpb stibp vmmcall fsgsbase bmi1 avx2 smep bmi2 erms invpcid cqm rdt_a rdseed adx smap clflushopt clwb sha_ni xsaveopt xsavec xgetbv1 xsaves cqm_llc cqm_occup_llc cqm_mbm_total cqm_mbm_local clzero irperf xsaveerptr rdpru wbnoinvd cppc arat npt lbrv svm_lock nrip_save tsc_scale vmcb_clean flushbyasid decodeassists pausefilter pfthreshold avic v_vmsave_vmload vgif v_spec_ctrl umip pku ospke vaes vpclmulqdq rdpid overflow_recov succor smca fsrm
    bugs        : sysret_ss_attrs spectre_v1 spectre_v2 spec_store_bypass
    bogomips    : 6388.19
    TLB size    : 2560 4K pages
    clflush size    : 64
    cache_alignment : 64
    address sizes   : 48 bits physical, 48 bits virtual
    power management: ts ttp tm hwpstate cpb eff_freq_ro [13] [14]

    processor   : 4
    vendor_id   : AuthenticAMD
    cpu family  : 25
    model       : 80
    model name  : AMD Ryzen 7 5800HS with Radeon Graphics
    stepping    : 0
    microcode   : 0xa50000c
    cpu MHz     : 1300.000
    cache size  : 512 KB
    physical id : 0
    siblings    : 16
    core id     : 2
    cpu cores   : 8
    apicid      : 4
    initial apicid  : 4
    fpu     : yes
    fpu_exception   : yes
    cpuid level : 16
    wp      : yes
    flags       : fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush mmx fxsr sse sse2 ht syscall nx mmxext fxsr_opt pdpe1gb rdtscp lm constant_tsc rep_good nopl nonstop_tsc cpuid extd_apicid aperfmperf rapl pni pclmulqdq monitor ssse3 fma cx16 sse4_1 sse4_2 movbe popcnt aes xsave avx f16c rdrand lahf_lm cmp_legacy svm extapic cr8_legacy abm sse4a misalignsse 3dnowprefetch osvw ibs skinit wdt tce topoext perfctr_core perfctr_nb bpext perfctr_llc mwaitx cpb cat_l3 cdp_l3 hw_pstate ssbd mba ibrs ibpb stibp vmmcall fsgsbase bmi1 avx2 smep bmi2 erms invpcid cqm rdt_a rdseed adx smap clflushopt clwb sha_ni xsaveopt xsavec xgetbv1 xsaves cqm_llc cqm_occup_llc cqm_mbm_total cqm_mbm_local clzero irperf xsaveerptr rdpru wbnoinvd cppc arat npt lbrv svm_lock nrip_save tsc_scale vmcb_clean flushbyasid decodeassists pausefilter pfthreshold avic v_vmsave_vmload vgif v_spec_ctrl umip pku ospke vaes vpclmulqdq rdpid overflow_recov succor smca fsrm
    bugs        : sysret_ss_attrs spectre_v1 spectre_v2 spec_store_bypass
    bogomips    : 6388.19
    TLB size    : 2560 4K pages
    clflush size    : 64
    cache_alignment : 64
    address sizes   : 48 bits physical, 48 bits virtual
    power management: ts ttp tm hwpstate cpb eff_freq_ro [13] [14]

    processor   : 5
    vendor_id   : AuthenticAMD
    cpu family  : 25
    model       : 80
    model name  : AMD Ryzen 7 5800HS with Radeon Graphics
    stepping    : 0
    microcode   : 0xa50000c
    cpu MHz     : 1200.000
    cache size  : 512 KB
    physical id : 0
    siblings    : 16
    core id     : 2
    cpu cores   : 8
    apicid      : 5
    initial apicid  : 5
    fpu     : yes
    fpu_exception   : yes
    cpuid level : 16
    wp      : yes
    flags       : fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush mmx fxsr sse sse2 ht syscall nx mmxext fxsr_opt pdpe1gb rdtscp lm constant_tsc rep_good nopl nonstop_tsc cpuid extd_apicid aperfmperf rapl pni pclmulqdq monitor ssse3 fma cx16 sse4_1 sse4_2 movbe popcnt aes xsave avx f16c rdrand lahf_lm cmp_legacy svm extapic cr8_legacy abm sse4a misalignsse 3dnowprefetch osvw ibs skinit wdt tce topoext perfctr_core perfctr_nb bpext perfctr_llc mwaitx cpb cat_l3 cdp_l3 hw_pstate ssbd mba ibrs ibpb stibp vmmcall fsgsbase bmi1 avx2 smep bmi2 erms invpcid cqm rdt_a rdseed adx smap clflushopt clwb sha_ni xsaveopt xsavec xgetbv1 xsaves cqm_llc cqm_occup_llc cqm_mbm_total cqm_mbm_local clzero irperf xsaveerptr rdpru wbnoinvd cppc arat npt lbrv svm_lock nrip_save tsc_scale vmcb_clean flushbyasid decodeassists pausefilter pfthreshold avic v_vmsave_vmload vgif v_spec_ctrl umip pku ospke vaes vpclmulqdq rdpid overflow_recov succor smca fsrm
    bugs        : sysret_ss_attrs spectre_v1 spectre_v2 spec_store_bypass
    bogomips    : 6388.19
    TLB size    : 2560 4K pages
    clflush size    : 64
    cache_alignment : 64
    address sizes   : 48 bits physical, 48 bits virtual
    power management: ts ttp tm hwpstate cpb eff_freq_ro [13] [14]

    processor   : 6
    vendor_id   : AuthenticAMD
    cpu family  : 25
    model       : 80
    model name  : AMD Ryzen 7 5800HS with Radeon Graphics
    stepping    : 0
    microcode   : 0xa50000c
    cpu MHz     : 1200.000
    cache size  : 512 KB
    physical id : 0
    siblings    : 16
    core id     : 3
    cpu cores   : 8
    apicid      : 6
    initial apicid  : 6
    fpu     : yes
    fpu_exception   : yes
    cpuid level : 16
    wp      : yes
    flags       : fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush mmx fxsr sse sse2 ht syscall nx mmxext fxsr_opt pdpe1gb rdtscp lm constant_tsc rep_good nopl nonstop_tsc cpuid extd_apicid aperfmperf rapl pni pclmulqdq monitor ssse3 fma cx16 sse4_1 sse4_2 movbe popcnt aes xsave avx f16c rdrand lahf_lm cmp_legacy svm extapic cr8_legacy abm sse4a misalignsse 3dnowprefetch osvw ibs skinit wdt tce topoext perfctr_core perfctr_nb bpext perfctr_llc mwaitx cpb cat_l3 cdp_l3 hw_pstate ssbd mba ibrs ibpb stibp vmmcall fsgsbase bmi1 avx2 smep bmi2 erms invpcid cqm rdt_a rdseed adx smap clflushopt clwb sha_ni xsaveopt xsavec xgetbv1 xsaves cqm_llc cqm_occup_llc cqm_mbm_total cqm_mbm_local clzero irperf xsaveerptr rdpru wbnoinvd cppc arat npt lbrv svm_lock nrip_save tsc_scale vmcb_clean flushbyasid decodeassists pausefilter pfthreshold avic v_vmsave_vmload vgif v_spec_ctrl umip pku ospke vaes vpclmulqdq rdpid overflow_recov succor smca fsrm
    bugs        : sysret_ss_attrs spectre_v1 spectre_v2 spec_store_bypass
    bogomips    : 6388.19
    TLB size    : 2560 4K pages
    clflush size    : 64
    cache_alignment : 64
    address sizes   : 48 bits physical, 48 bits virtual
    power management: ts ttp tm hwpstate cpb eff_freq_ro [13] [14]

    processor   : 7
    vendor_id   : AuthenticAMD
    cpu family  : 25
    model       : 80
    model name  : AMD Ryzen 7 5800HS with Radeon Graphics
    stepping    : 0
    microcode   : 0xa50000c
    cpu MHz     : 1200.000
    cache size  : 512 KB
    physical id : 0
    siblings    : 16
    core id     : 3
    cpu cores   : 8
    apicid      : 7
    initial apicid  : 7
    fpu     : yes
    fpu_exception   : yes
    cpuid level : 16
    wp      : yes
    flags       : fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush mmx fxsr sse sse2 ht syscall nx mmxext fxsr_opt pdpe1gb rdtscp lm constant_tsc rep_good nopl nonstop_tsc cpuid extd_apicid aperfmperf rapl pni pclmulqdq monitor ssse3 fma cx16 sse4_1 sse4_2 movbe popcnt aes xsave avx f16c rdrand lahf_lm cmp_legacy svm extapic cr8_legacy abm sse4a misalignsse 3dnowprefetch osvw ibs skinit wdt tce topoext perfctr_core perfctr_nb bpext perfctr_llc mwaitx cpb cat_l3 cdp_l3 hw_pstate ssbd mba ibrs ibpb stibp vmmcall fsgsbase bmi1 avx2 smep bmi2 erms invpcid cqm rdt_a rdseed adx smap clflushopt clwb sha_ni xsaveopt xsavec xgetbv1 xsaves cqm_llc cqm_occup_llc cqm_mbm_total cqm_mbm_local clzero irperf xsaveerptr rdpru wbnoinvd cppc arat npt lbrv svm_lock nrip_save tsc_scale vmcb_clean flushbyasid decodeassists pausefilter pfthreshold avic v_vmsave_vmload vgif v_spec_ctrl umip pku ospke vaes vpclmulqdq rdpid overflow_recov succor smca fsrm
    bugs        : sysret_ss_attrs spectre_v1 spectre_v2 spec_store_bypass
    bogomips    : 6388.19
    TLB size    : 2560 4K pages
    clflush size    : 64
    cache_alignment : 64
    address sizes   : 48 bits physical, 48 bits virtual
    power management: ts ttp tm hwpstate cpb eff_freq_ro [13] [14]

    processor   : 8
    vendor_id   : AuthenticAMD
    cpu family  : 25
    model       : 80
    model name  : AMD Ryzen 7 5800HS with Radeon Graphics
    stepping    : 0
    microcode   : 0xa50000c
    cpu MHz     : 1200.000
    cache size  : 512 KB
    physical id : 0
    siblings    : 16
    core id     : 4
    cpu cores   : 8
    apicid      : 8
    initial apicid  : 8
    fpu     : yes
    fpu_exception   : yes
    cpuid level : 16
    wp      : yes
    flags       : fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush mmx fxsr sse sse2 ht syscall nx mmxext fxsr_opt pdpe1gb rdtscp lm constant_tsc rep_good nopl nonstop_tsc cpuid extd_apicid aperfmperf rapl pni pclmulqdq monitor ssse3 fma cx16 sse4_1 sse4_2 movbe popcnt aes xsave avx f16c rdrand lahf_lm cmp_legacy svm extapic cr8_legacy abm sse4a misalignsse 3dnowprefetch osvw ibs skinit wdt tce topoext perfctr_core perfctr_nb bpext perfctr_llc mwaitx cpb cat_l3 cdp_l3 hw_pstate ssbd mba ibrs ibpb stibp vmmcall fsgsbase bmi1 avx2 smep bmi2 erms invpcid cqm rdt_a rdseed adx smap clflushopt clwb sha_ni xsaveopt xsavec xgetbv1 xsaves cqm_llc cqm_occup_llc cqm_mbm_total cqm_mbm_local clzero irperf xsaveerptr rdpru wbnoinvd cppc arat npt lbrv svm_lock nrip_save tsc_scale vmcb_clean flushbyasid decodeassists pausefilter pfthreshold avic v_vmsave_vmload vgif v_spec_ctrl umip pku ospke vaes vpclmulqdq rdpid overflow_recov succor smca fsrm
    bugs        : sysret_ss_attrs spectre_v1 spectre_v2 spec_store_bypass
    bogomips    : 6388.19
    TLB size    : 2560 4K pages
    clflush size    : 64
    cache_alignment : 64
    address sizes   : 48 bits physical, 48 bits virtual
    power management: ts ttp tm hwpstate cpb eff_freq_ro [13] [14]

    processor   : 9
    vendor_id   : AuthenticAMD
    cpu family  : 25
    model       : 80
    model name  : AMD Ryzen 7 5800HS with Radeon Graphics
    stepping    : 0
    microcode   : 0xa50000c
    cpu MHz     : 1200.000
    cache size  : 512 KB
    physical id : 0
    siblings    : 16
    core id     : 4
    cpu cores   : 8
    apicid      : 9
    initial apicid  : 9
    fpu     : yes
    fpu_exception   : yes
    cpuid level : 16
    wp      : yes
    flags       : fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush mmx fxsr sse sse2 ht syscall nx mmxext fxsr_opt pdpe1gb rdtscp lm constant_tsc rep_good nopl nonstop_tsc cpuid extd_apicid aperfmperf rapl pni pclmulqdq monitor ssse3 fma cx16 sse4_1 sse4_2 movbe popcnt aes xsave avx f16c rdrand lahf_lm cmp_legacy svm extapic cr8_legacy abm sse4a misalignsse 3dnowprefetch osvw ibs skinit wdt tce topoext perfctr_core perfctr_nb bpext perfctr_llc mwaitx cpb cat_l3 cdp_l3 hw_pstate ssbd mba ibrs ibpb stibp vmmcall fsgsbase bmi1 avx2 smep bmi2 erms invpcid cqm rdt_a rdseed adx smap clflushopt clwb sha_ni xsaveopt xsavec xgetbv1 xsaves cqm_llc cqm_occup_llc cqm_mbm_total cqm_mbm_local clzero irperf xsaveerptr rdpru wbnoinvd cppc arat npt lbrv svm_lock nrip_save tsc_scale vmcb_clean flushbyasid decodeassists pausefilter pfthreshold avic v_vmsave_vmload vgif v_spec_ctrl umip pku ospke vaes vpclmulqdq rdpid overflow_recov succor smca fsrm
    bugs        : sysret_ss_attrs spectre_v1 spectre_v2 spec_store_bypass
    bogomips    : 6388.19
    TLB size    : 2560 4K pages
    clflush size    : 64
    cache_alignment : 64
    address sizes   : 48 bits physical, 48 bits virtual
    power management: ts ttp tm hwpstate cpb eff_freq_ro [13] [14]

    processor   : 10
    vendor_id   : AuthenticAMD
    cpu family  : 25
    model       : 80
    model name  : AMD Ryzen 7 5800HS with Radeon Graphics
    stepping    : 0
    microcode   : 0xa50000c
    cpu MHz     : 1300.000
    cache size  : 512 KB
    physical id : 0
    siblings    : 16
    core id     : 5
    cpu cores   : 8
    apicid      : 10
    initial apicid  : 10
    fpu     : yes
    fpu_exception   : yes
    cpuid level : 16
    wp      : yes
    flags       : fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush mmx fxsr sse sse2 ht syscall nx mmxext fxsr_opt pdpe1gb rdtscp lm constant_tsc rep_good nopl nonstop_tsc cpuid extd_apicid aperfmperf rapl pni pclmulqdq monitor ssse3 fma cx16 sse4_1 sse4_2 movbe popcnt aes xsave avx f16c rdrand lahf_lm cmp_legacy svm extapic cr8_legacy abm sse4a misalignsse 3dnowprefetch osvw ibs skinit wdt tce topoext perfctr_core perfctr_nb bpext perfctr_llc mwaitx cpb cat_l3 cdp_l3 hw_pstate ssbd mba ibrs ibpb stibp vmmcall fsgsbase bmi1 avx2 smep bmi2 erms invpcid cqm rdt_a rdseed adx smap clflushopt clwb sha_ni xsaveopt xsavec xgetbv1 xsaves cqm_llc cqm_occup_llc cqm_mbm_total cqm_mbm_local clzero irperf xsaveerptr rdpru wbnoinvd cppc arat npt lbrv svm_lock nrip_save tsc_scale vmcb_clean flushbyasid decodeassists pausefilter pfthreshold avic v_vmsave_vmload vgif v_spec_ctrl umip pku ospke vaes vpclmulqdq rdpid overflow_recov succor smca fsrm
    bugs        : sysret_ss_attrs spectre_v1 spectre_v2 spec_store_bypass
    bogomips    : 6388.19
    TLB size    : 2560 4K pages
    clflush size    : 64
    cache_alignment : 64
    address sizes   : 48 bits physical, 48 bits virtual
    power management: ts ttp tm hwpstate cpb eff_freq_ro [13] [14]

    processor   : 11
    vendor_id   : AuthenticAMD
    cpu family  : 25
    model       : 80
    model name  : AMD Ryzen 7 5800HS with Radeon Graphics
    stepping    : 0
    microcode   : 0xa50000c
    cpu MHz     : 1200.000
    cache size  : 512 KB
    physical id : 0
    siblings    : 16
    core id     : 5
    cpu cores   : 8
    apicid      : 11
    initial apicid  : 11
    fpu     : yes
    fpu_exception   : yes
    cpuid level : 16
    wp      : yes
    flags       : fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush mmx fxsr sse sse2 ht syscall nx mmxext fxsr_opt pdpe1gb rdtscp lm constant_tsc rep_good nopl nonstop_tsc cpuid extd_apicid aperfmperf rapl pni pclmulqdq monitor ssse3 fma cx16 sse4_1 sse4_2 movbe popcnt aes xsave avx f16c rdrand lahf_lm cmp_legacy svm extapic cr8_legacy abm sse4a misalignsse 3dnowprefetch osvw ibs skinit wdt tce topoext perfctr_core perfctr_nb bpext perfctr_llc mwaitx cpb cat_l3 cdp_l3 hw_pstate ssbd mba ibrs ibpb stibp vmmcall fsgsbase bmi1 avx2 smep bmi2 erms invpcid cqm rdt_a rdseed adx smap clflushopt clwb sha_ni xsaveopt xsavec xgetbv1 xsaves cqm_llc cqm_occup_llc cqm_mbm_total cqm_mbm_local clzero irperf xsaveerptr rdpru wbnoinvd cppc arat npt lbrv svm_lock nrip_save tsc_scale vmcb_clean flushbyasid decodeassists pausefilter pfthreshold avic v_vmsave_vmload vgif v_spec_ctrl umip pku ospke vaes vpclmulqdq rdpid overflow_recov succor smca fsrm
    bugs        : sysret_ss_attrs spectre_v1 spectre_v2 spec_store_bypass
    bogomips    : 6388.19
    TLB size    : 2560 4K pages
    clflush size    : 64
    cache_alignment : 64
    address sizes   : 48 bits physical, 48 bits virtual
    power management: ts ttp tm hwpstate cpb eff_freq_ro [13] [14]

    processor   : 12
    vendor_id   : AuthenticAMD
    cpu family  : 25
    model       : 80
    model name  : AMD Ryzen 7 5800HS with Radeon Graphics
    stepping    : 0
    microcode   : 0xa50000c
    cpu MHz     : 1916.532
    cache size  : 512 KB
    physical id : 0
    siblings    : 16
    core id     : 6
    cpu cores   : 8
    apicid      : 12
    initial apicid  : 12
    fpu     : yes
    fpu_exception   : yes
    cpuid level : 16
    wp      : yes
    flags       : fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush mmx fxsr sse sse2 ht syscall nx mmxext fxsr_opt pdpe1gb rdtscp lm constant_tsc rep_good nopl nonstop_tsc cpuid extd_apicid aperfmperf rapl pni pclmulqdq monitor ssse3 fma cx16 sse4_1 sse4_2 movbe popcnt aes xsave avx f16c rdrand lahf_lm cmp_legacy svm extapic cr8_legacy abm sse4a misalignsse 3dnowprefetch osvw ibs skinit wdt tce topoext perfctr_core perfctr_nb bpext perfctr_llc mwaitx cpb cat_l3 cdp_l3 hw_pstate ssbd mba ibrs ibpb stibp vmmcall fsgsbase bmi1 avx2 smep bmi2 erms invpcid cqm rdt_a rdseed adx smap clflushopt clwb sha_ni xsaveopt xsavec xgetbv1 xsaves cqm_llc cqm_occup_llc cqm_mbm_total cqm_mbm_local clzero irperf xsaveerptr rdpru wbnoinvd cppc arat npt lbrv svm_lock nrip_save tsc_scale vmcb_clean flushbyasid decodeassists pausefilter pfthreshold avic v_vmsave_vmload vgif v_spec_ctrl umip pku ospke vaes vpclmulqdq rdpid overflow_recov succor smca fsrm
    bugs        : sysret_ss_attrs spectre_v1 spectre_v2 spec_store_bypass
    bogomips    : 6388.19
    TLB size    : 2560 4K pages
    clflush size    : 64
    cache_alignment : 64
    address sizes   : 48 bits physical, 48 bits virtual
    power management: ts ttp tm hwpstate cpb eff_freq_ro [13] [14]

    processor   : 13
    vendor_id   : AuthenticAMD
    cpu family  : 25
    model       : 80
    model name  : AMD Ryzen 7 5800HS with Radeon Graphics
    stepping    : 0
    microcode   : 0xa50000c
    cpu MHz     : 1200.000
    cache size  : 512 KB
    physical id : 0
    siblings    : 16
    core id     : 6
    cpu cores   : 8
    apicid      : 13
    initial apicid  : 13
    fpu     : yes
    fpu_exception   : yes
    cpuid level : 16
    wp      : yes
    flags       : fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush mmx fxsr sse sse2 ht syscall nx mmxext fxsr_opt pdpe1gb rdtscp lm constant_tsc rep_good nopl nonstop_tsc cpuid extd_apicid aperfmperf rapl pni pclmulqdq monitor ssse3 fma cx16 sse4_1 sse4_2 movbe popcnt aes xsave avx f16c rdrand lahf_lm cmp_legacy svm extapic cr8_legacy abm sse4a misalignsse 3dnowprefetch osvw ibs skinit wdt tce topoext perfctr_core perfctr_nb bpext perfctr_llc mwaitx cpb cat_l3 cdp_l3 hw_pstate ssbd mba ibrs ibpb stibp vmmcall fsgsbase bmi1 avx2 smep bmi2 erms invpcid cqm rdt_a rdseed adx smap clflushopt clwb sha_ni xsaveopt xsavec xgetbv1 xsaves cqm_llc cqm_occup_llc cqm_mbm_total cqm_mbm_local clzero irperf xsaveerptr rdpru wbnoinvd cppc arat npt lbrv svm_lock nrip_save tsc_scale vmcb_clean flushbyasid decodeassists pausefilter pfthreshold avic v_vmsave_vmload vgif v_spec_ctrl umip pku ospke vaes vpclmulqdq rdpid overflow_recov succor smca fsrm
    bugs        : sysret_ss_attrs spectre_v1 spectre_v2 spec_store_bypass
    bogomips    : 6388.19
    TLB size    : 2560 4K pages
    clflush size    : 64
    cache_alignment : 64
    address sizes   : 48 bits physical, 48 bits virtual
    power management: ts ttp tm hwpstate cpb eff_freq_ro [13] [14]

    processor   : 14
    vendor_id   : AuthenticAMD
    cpu family  : 25
    model       : 80
    model name  : AMD Ryzen 7 5800HS with Radeon Graphics
    stepping    : 0
    microcode   : 0xa50000c
    cpu MHz     : 3200.000
    cache size  : 512 KB
    physical id : 0
    siblings    : 16
    core id     : 7
    cpu cores   : 8
    apicid      : 14
    initial apicid  : 14
    fpu     : yes
    fpu_exception   : yes
    cpuid level : 16
    wp      : yes
    flags       : fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush mmx fxsr sse sse2 ht syscall nx mmxext fxsr_opt pdpe1gb rdtscp lm constant_tsc rep_good nopl nonstop_tsc cpuid extd_apicid aperfmperf rapl pni pclmulqdq monitor ssse3 fma cx16 sse4_1 sse4_2 movbe popcnt aes xsave avx f16c rdrand lahf_lm cmp_legacy svm extapic cr8_legacy abm sse4a misalignsse 3dnowprefetch osvw ibs skinit wdt tce topoext perfctr_core perfctr_nb bpext perfctr_llc mwaitx cpb cat_l3 cdp_l3 hw_pstate ssbd mba ibrs ibpb stibp vmmcall fsgsbase bmi1 avx2 smep bmi2 erms invpcid cqm rdt_a rdseed adx smap clflushopt clwb sha_ni xsaveopt xsavec xgetbv1 xsaves cqm_llc cqm_occup_llc cqm_mbm_total cqm_mbm_local clzero irperf xsaveerptr rdpru wbnoinvd cppc arat npt lbrv svm_lock nrip_save tsc_scale vmcb_clean flushbyasid decodeassists pausefilter pfthreshold avic v_vmsave_vmload vgif v_spec_ctrl umip pku ospke vaes vpclmulqdq rdpid overflow_recov succor smca fsrm
    bugs        : sysret_ss_attrs spectre_v1 spectre_v2 spec_store_bypass
    bogomips    : 6388.19
    TLB size    : 2560 4K pages
    clflush size    : 64
    cache_alignment : 64
    address sizes   : 48 bits physical, 48 bits virtual
    power management: ts ttp tm hwpstate cpb eff_freq_ro [13] [14]

    processor   : 15
    vendor_id   : AuthenticAMD
    cpu family  : 25
    model       : 80
    model name  : AMD Ryzen 7 5800HS with Radeon Graphics
    stepping    : 0
    microcode   : 0xa50000c
    cpu MHz     : 1200.000
    cache size  : 512 KB
    physical id : 0
    siblings    : 16
    core id     : 7
    cpu cores   : 8
    apicid      : 15
    initial apicid  : 15
    fpu     : yes
    fpu_exception   : yes
    cpuid level : 16
    wp      : yes
    flags       : fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush mmx fxsr sse sse2 ht syscall nx mmxext fxsr_opt pdpe1gb rdtscp lm constant_tsc rep_good nopl nonstop_tsc cpuid extd_apicid aperfmperf rapl pni pclmulqdq monitor ssse3 fma cx16 sse4_1 sse4_2 movbe popcnt aes xsave avx f16c rdrand lahf_lm cmp_legacy svm extapic cr8_legacy abm sse4a misalignsse 3dnowprefetch osvw ibs skinit wdt tce topoext perfctr_core perfctr_nb bpext perfctr_llc mwaitx cpb cat_l3 cdp_l3 hw_pstate ssbd mba ibrs ibpb stibp vmmcall fsgsbase bmi1 avx2 smep bmi2 erms invpcid cqm rdt_a rdseed adx smap clflushopt clwb sha_ni xsaveopt xsavec xgetbv1 xsaves cqm_llc cqm_occup_llc cqm_mbm_total cqm_mbm_local clzero irperf xsaveerptr rdpru wbnoinvd cppc arat npt lbrv svm_lock nrip_save tsc_scale vmcb_clean flushbyasid decodeassists pausefilter pfthreshold avic v_vmsave_vmload vgif v_spec_ctrl umip pku ospke vaes vpclmulqdq rdpid overflow_recov succor smca fsrm
    bugs        : sysret_ss_attrs spectre_v1 spectre_v2 spec_store_bypass
    bogomips    : 6388.19
    TLB size    : 2560 4K pages
    clflush size    : 64
    cache_alignment : 64
    address sizes   : 48 bits physical, 48 bits virtual
    power management: ts ttp tm hwpstate cpb eff_freq_ro [13] [14]

## [Hardware Support]

### [Input Devices]

TODO

### [Drives and Storage]

-   Hard Drive controller works using ahci driver in the kernel.

### [Graphics Chip]

TODO

### [WLAN Card]

[KERNEL] **MediaTek 7961, 5.15.0**

    [*] Networking support  --->
        [*]   Wireless  --->
            <*>   Generic IEEE 802.11 Networking Stack (mac80211)

    Device Drivers  --->
        [*] Network device support
        [*] Wireless LAN --->
            [*] MediaTek devices
            <M> MediaTek MT7921E (PCIe) support

You\'ll also need the firmware:

`root `[`#`]`emerge --ask linux-firmware`

### [CPU Frequency Scaling]

[KERNEL] **CPU Frequency Scaling**

    Power management and ACPI options  --->
        CPU Frequency scaling  --->
        [*] CPU Frequency scaling
        <*>   ACPI Processor P-States driver

### [Sensors]

`root `[`#`]`emerge --ask asus-wmi-sensors`

### [Touchpad]

[KERNEL] **Touchpad**

    Cryptographic API --->
      Hardware crypto devices --->
        Support for AMD Secure Processor --->
          Secure Processor device driver --->
             [*] Platform Security Processor (PSP) device

    Device Drivers  --->
      I2C support  --->
        [*] I2C support  --->
          I2C Hardware Bus support  --->
                <M> Intel PIIX4 and compatible (ATI/AMD/Serverworks/Broadcom/SMSC)
                <M> Synopsys DesignWare Platform
                [*] AMD PSP I2C semaphore support
                <M> Synopsys DesignWare PCI

    Device Drivers  --->
      Input device support  --->
        [*] Generic input layer (needed for keyboard, mouse, ...)  --->
          [*] Mice (INPUT_MOUSE)  --->
            [M] PS/2 mouse  --->
                [*] Synaptics PS/2 mouse protocol extension

### [Sound Chip]

-   Works

### [Fingerprint reader]

-   Untested

### [Sleep Mode]

**Note:** If you have up to date BIOS and Gentoo system, you probably no longer need this. Also beware that updating BIOS after doing these steps would break your Gentoo installation, You\'ll either need to disable this or redo same steps for the new BIOS.

This family of laptops don\'t support Suspend-to-RAM mode and instead linux fallback to Suspend-to-Idle mode. In Suspend-to-Idle system can wake up from sleep significantly faster but also consume significantly more power while in sleep mode compared to Suspend-to-RAM.

[This repo](https://gitlab.com/marcaux/g14-2021-s3-dsdt) detail how to bring back S3 mode (Suspend-to-RAM) for Asus G14 and G15 variants. Note that while the repo\'s readme recommend updating your bootloader to load the patched \`dsdt\` file, it is also possible to [include it into the kernel](https://wiki.archlinux.org/title/DSDT#Compiling_into_the_kernel) instead.

## [Software]

### [Linux asusctl]

asusctl is a commandline utility that allow configuring different parts of the system without root access.

`user `[`$`]`asusctl`

    Optional arguments:
      -h, --help             print help message
      -v, --version          show program version number
      -s, --show-supported   show supported functions of this laptop
      -k, --kbd-bright       <off, low, med, high>
      -n, --next-kbd-bright  Toggle to next keyboard brightness
      -p, --prev-kbd-bright  Toggle to previous keyboard brightness
      -c, --chg-limit        Set your battery charge limit <20-100>

      led-mode   Set the keyboard lighting from built-in modes
      profile    Set or select platform_profile
      fan-curve  Set, select, or modify fan curves if supported
      graphics   Set the graphics mode (obsoleted by supergfxctl)
      anime      Manage AniMe Matrix
      bios       Change bios settings

asusctl can be compiled and installed from [this repo](https://gitlab.com/asus-linux/asusctl)