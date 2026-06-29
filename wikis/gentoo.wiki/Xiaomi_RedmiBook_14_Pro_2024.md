**Resources**

[[]][Official Product Page](https://www.mi.com/shop/buy/detail?product_id=1230801682)

** Note**\
This article is focused on the specific model I own and my specific Gentoo setup, feel free to add more sections

## Contents

-   [[1] [Laptop specifications]](#Laptop_specifications)
-   [[2] [Installation]](#Installation)
    -   [[2.1] [Kernel]](#Kernel)
        -   [[2.1.1] [Input devices]](#Input_devices)
        -   [[2.1.2] [USB 3.0 support]](#USB_3.0_support)
        -   [[2.1.3] [Drives and storage]](#Drives_and_storage)
        -   [[2.1.4] [Graphics]](#Graphics)
            -   [[2.1.4.1] [Force use of Xe probe]](#Force_use_of_Xe_probe)
        -   [[2.1.5] [Wi-Fi]](#Wi-Fi)
        -   [[2.1.6] [Sound]](#Sound)
        -   [[2.1.7] [CPU frequency scaling]](#CPU_frequency_scaling)
        -   [[2.1.8] [NPU]](#NPU)
        -   [[2.1.9] [Webcam]](#Webcam)
        -   [[2.1.10] [Bluetooth]](#Bluetooth)
    -   [[2.2] [Misc]](#Misc)
        -   [[2.2.1] [Fingerprint reader]](#Fingerprint_reader)

## [Laptop specifications]

-   Intel Core Ultra 5-125H or Intel Core Ultra 7-155H
-   Intel AI Boost NPU 1.4 GHz
-   16-32GB LPDDR5x 7467MT/s single-channel
-   Intel Arc (on-CPU)
-   14in Super Retina display 2880x1800
-   512-GB or 1TB SSD PCle 4.0 2242
-   80Wh battery with Thunderbolt 4 Type-C 100W
-   x2 USB-A 3.2 Gen1, x1 USB-C, x1 Thunderbolt 4, x1 HDMI 2.1 TMDS, x1 3.5mm Jack

Printout of lspci:

`root `[`#`]`lspci`

    00:00.0 Host bridge: Intel Corporation Device 7d01 (rev 04)
    00:02.0 VGA compatible controller: Intel Corporation Meteor Lake-P [Intel Arc Graphics] (rev 08)
    00:04.0 Signal processing controller: Intel Corporation Meteor Lake-P Dynamic Tuning Technology (rev 04)
    00:06.0 PCI bridge: Intel Corporation Device 7e4d (rev 20)
    00:07.0 PCI bridge: Intel Corporation Meteor Lake-P Thunderbolt 4 PCI Express Root Port #1 (rev 10)
    00:08.0 System peripheral: Intel Corporation Meteor Lake-P Gaussian & Neural-Network Accelerator (rev 20)
    00:0a.0 Signal processing controller: Intel Corporation Meteor Lake-P Platform Monitoring Technology (rev 01)
    00:0b.0 Processing accelerators: Intel Corporation Meteor Lake NPU (rev 04)
    00:0d.0 USB controller: Intel Corporation Meteor Lake-P Thunderbolt 4 USB Controller (rev 10)
    00:0d.2 USB controller: Intel Corporation Meteor Lake-P Thunderbolt 4 NHI #0 (rev 10)
    00:12.0 Serial controller: Intel Corporation Meteor Lake-P Integrated Sensor Hub (rev 20)
    00:14.0 USB controller: Intel Corporation Meteor Lake-P USB 3.2 Gen 2x1 xHCI Host Controller (rev 20)
    00:14.2 RAM memory: Intel Corporation Device 7e7f (rev 20)
    00:14.3 Network controller: Intel Corporation Meteor Lake PCH CNVi WiFi (rev 20)
    00:15.0 Serial bus controller: Intel Corporation Meteor Lake-P Serial IO I2C Controller #0 (rev 20)
    00:16.0 Communication controller: Intel Corporation Meteor Lake-P CSME HECI #1 (rev 20)
    00:1f.0 ISA bridge: Intel Corporation Device 7e02 (rev 20)
    00:1f.3 Multimedia audio controller: Intel Corporation Meteor Lake-P HD Audio Controller (rev 20)
    00:1f.4 SMBus: Intel Corporation Meteor Lake-P SMBus Controller (rev 20)
    00:1f.5 Serial bus controller: Intel Corporation Meteor Lake-P SPI Controller (rev 20)
    01:00.0 Non-Volatile memory controller: Yangtze Memory Technologies Co.,Ltd PC300 NVMe SSD (DRAM-less) (rev 03)

Information from [/proc/cpuinfo]:

`root `[`#`]`cat /proc/cpuinfo`

    processor   : 0
    vendor_id   : GenuineIntel
    cpu family  : 6
    model       : 170
    model name  : Intel(R) Core(TM) Ultra 7 155H
    stepping    : 4
    microcode   : 0x17
    cpu MHz     : 2800.000
    cache size  : 24576 KB
    physical id : 0
    siblings    : 22
    core id     : 16
    cpu cores   : 16
    apicid      : 32
    initial apicid  : 32
    fpu     : yes
    fpu_exception   : yes
    cpuid level : 35
    wp      : yes
    flags       : fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush dts acpi mmx fxsr sse sse2 ss ht tm pbe syscall nx pdpe1gb rdtscp lm constant_tsc art arch_perfmon pebs bts rep_good nopl xtopology nonstop_tsc cpuid aperfmperf tsc_known_freq pni pclmulqdq dtes64 monitor ds_cpl vmx smx est tm2 ssse3 sdbg fma cx16 xtpr pdcm pcid sse4_1 sse4_2 x2apic movbe popcnt tsc_deadline_timer aes xsave avx f16c rdrand lahf_lm abm 3dnowprefetch cpuid_fault epb ssbd ibrs ibpb stibp ibrs_enhanced tpr_shadow flexpriority ept vpid ept_ad fsgsbase tsc_adjust bmi1 avx2 smep bmi2 erms invpcid rdseed adx smap clflushopt clwb intel_pt sha_ni xsaveopt xsavec xgetbv1 xsaves split_lock_detect user_shstk avx_vnni dtherm ida arat pln pts hwp hwp_notify hwp_act_window hwp_epp hwp_pkg_req hfi vnmi umip pku ospke waitpkg gfni vaes vpclmulqdq rdpid bus_lock_detect movdiri movdir64b fsrm md_clear serialize arch_lbr ibt flush_l1d arch_capabilities
    vmx flags   : vnmi preemption_timer posted_intr invvpid ept_x_only ept_ad ept_1gb flexpriority apicv tsc_offset vtpr mtf vapic ept vpid unrestricted_guest vapic_reg vid ple shadow_vmcs pml ept_violation_ve ept_mode_based_exec tsc_scaling usr_wait_pause notify_vm_exiting
    bugs        : spectre_v1 spectre_v2 spec_store_bypass swapgs bhi
    bogomips    : 5990.40
    clflush size    : 64
    cache_alignment : 64
    address sizes   : 46 bits physical, 48 bits virtual
    power management:

    processor   : 1
    vendor_id   : GenuineIntel
    cpu family  : 6
    model       : 170
    model name  : Intel(R) Core(TM) Ultra 7 155H
    stepping    : 4
    microcode   : 0x17
    cpu MHz     : 3000.030
    cache size  : 24576 KB
    physical id : 0
    siblings    : 22
    core id     : 8
    cpu cores   : 16
    apicid      : 16
    initial apicid  : 16
    fpu     : yes
    fpu_exception   : yes
    cpuid level : 35
    wp      : yes
    flags       : fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush dts acpi mmx fxsr sse sse2 ss ht tm pbe syscall nx pdpe1gb rdtscp lm constant_tsc art arch_perfmon pebs bts rep_good nopl xtopology nonstop_tsc cpuid aperfmperf tsc_known_freq pni pclmulqdq dtes64 monitor ds_cpl vmx smx est tm2 ssse3 sdbg fma cx16 xtpr pdcm pcid sse4_1 sse4_2 x2apic movbe popcnt tsc_deadline_timer aes xsave avx f16c rdrand lahf_lm abm 3dnowprefetch cpuid_fault epb intel_ppin ssbd ibrs ibpb stibp ibrs_enhanced tpr_shadow flexpriority ept vpid ept_ad fsgsbase tsc_adjust bmi1 avx2 smep bmi2 erms invpcid rdseed adx smap clflushopt clwb intel_pt sha_ni xsaveopt xsavec xgetbv1 xsaves split_lock_detect user_shstk avx_vnni dtherm ida arat pln pts hwp hwp_notify hwp_act_window hwp_epp hwp_pkg_req hfi vnmi umip pku ospke waitpkg gfni vaes vpclmulqdq rdpid bus_lock_detect movdiri movdir64b fsrm md_clear serialize arch_lbr ibt flush_l1d arch_capabilities
    vmx flags   : vnmi preemption_timer posted_intr invvpid ept_x_only ept_ad ept_1gb flexpriority apicv tsc_offset vtpr mtf vapic ept vpid unrestricted_guest vapic_reg vid ple shadow_vmcs pml ept_violation_ve ept_mode_based_exec tsc_scaling usr_wait_pause notify_vm_exiting
    bugs        : spectre_v1 spectre_v2 spec_store_bypass swapgs bhi
    bogomips    : 5990.40
    clflush size    : 64
    cache_alignment : 64
    address sizes   : 46 bits physical, 48 bits virtual
    power management:

    processor   : 2
    vendor_id   : GenuineIntel
    cpu family  : 6
    model       : 170
    model name  : Intel(R) Core(TM) Ultra 7 155H
    stepping    : 4
    microcode   : 0x17
    cpu MHz     : 3002.112
    cache size  : 24576 KB
    physical id : 0
    siblings    : 22
    core id     : 8
    cpu cores   : 16
    apicid      : 17
    initial apicid  : 17
    fpu     : yes
    fpu_exception   : yes
    cpuid level : 35
    wp      : yes
    flags       : fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush dts acpi mmx fxsr sse sse2 ss ht tm pbe syscall nx pdpe1gb rdtscp lm constant_tsc art arch_perfmon pebs bts rep_good nopl xtopology nonstop_tsc cpuid aperfmperf tsc_known_freq pni pclmulqdq dtes64 monitor ds_cpl vmx smx est tm2 ssse3 sdbg fma cx16 xtpr pdcm pcid sse4_1 sse4_2 x2apic movbe popcnt tsc_deadline_timer aes xsave avx f16c rdrand lahf_lm abm 3dnowprefetch cpuid_fault epb intel_ppin ssbd ibrs ibpb stibp ibrs_enhanced tpr_shadow flexpriority ept vpid ept_ad fsgsbase tsc_adjust bmi1 avx2 smep bmi2 erms invpcid rdseed adx smap clflushopt clwb intel_pt sha_ni xsaveopt xsavec xgetbv1 xsaves split_lock_detect user_shstk avx_vnni dtherm ida arat pln pts hwp hwp_notify hwp_act_window hwp_epp hwp_pkg_req hfi vnmi umip pku ospke waitpkg gfni vaes vpclmulqdq rdpid bus_lock_detect movdiri movdir64b fsrm md_clear serialize arch_lbr ibt flush_l1d arch_capabilities
    vmx flags   : vnmi preemption_timer posted_intr invvpid ept_x_only ept_ad ept_1gb flexpriority apicv tsc_offset vtpr mtf vapic ept vpid unrestricted_guest vapic_reg vid ple shadow_vmcs pml ept_violation_ve ept_mode_based_exec tsc_scaling usr_wait_pause notify_vm_exiting
    bugs        : spectre_v1 spectre_v2 spec_store_bypass swapgs bhi
    bogomips    : 5990.40
    clflush size    : 64
    cache_alignment : 64
    address sizes   : 46 bits physical, 48 bits virtual
    power management:

    processor   : 3
    vendor_id   : GenuineIntel
    cpu family  : 6
    model       : 170
    model name  : Intel(R) Core(TM) Ultra 7 155H
    stepping    : 4
    microcode   : 0x17
    cpu MHz     : 400.000
    cache size  : 24576 KB
    physical id : 0
    siblings    : 22
    core id     : 12
    cpu cores   : 16
    apicid      : 24
    initial apicid  : 24
    fpu     : yes
    fpu_exception   : yes
    cpuid level : 35
    wp      : yes
    flags       : fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush dts acpi mmx fxsr sse sse2 ss ht tm pbe syscall nx pdpe1gb rdtscp lm constant_tsc art arch_perfmon pebs bts rep_good nopl xtopology nonstop_tsc cpuid aperfmperf tsc_known_freq pni pclmulqdq dtes64 monitor ds_cpl vmx smx est tm2 ssse3 sdbg fma cx16 xtpr pdcm pcid sse4_1 sse4_2 x2apic movbe popcnt tsc_deadline_timer aes xsave avx f16c rdrand lahf_lm abm 3dnowprefetch cpuid_fault epb intel_ppin ssbd ibrs ibpb stibp ibrs_enhanced tpr_shadow flexpriority ept vpid ept_ad fsgsbase tsc_adjust bmi1 avx2 smep bmi2 erms invpcid rdseed adx smap clflushopt clwb intel_pt sha_ni xsaveopt xsavec xgetbv1 xsaves split_lock_detect user_shstk avx_vnni dtherm ida arat pln pts hwp hwp_notify hwp_act_window hwp_epp hwp_pkg_req hfi vnmi umip pku ospke waitpkg gfni vaes vpclmulqdq rdpid bus_lock_detect movdiri movdir64b fsrm md_clear serialize arch_lbr ibt flush_l1d arch_capabilities
    vmx flags   : vnmi preemption_timer posted_intr invvpid ept_x_only ept_ad ept_1gb flexpriority apicv tsc_offset vtpr mtf vapic ept vpid unrestricted_guest vapic_reg vid ple shadow_vmcs pml ept_violation_ve ept_mode_based_exec tsc_scaling usr_wait_pause notify_vm_exiting
    bugs        : spectre_v1 spectre_v2 spec_store_bypass swapgs bhi
    bogomips    : 5990.40
    clflush size    : 64
    cache_alignment : 64
    address sizes   : 46 bits physical, 48 bits virtual
    power management:

    processor   : 4
    vendor_id   : GenuineIntel
    cpu family  : 6
    model       : 170
    model name  : Intel(R) Core(TM) Ultra 7 155H
    stepping    : 4
    microcode   : 0x17
    cpu MHz     : 3000.000
    cache size  : 24576 KB
    physical id : 0
    siblings    : 22
    core id     : 12
    cpu cores   : 16
    apicid      : 25
    initial apicid  : 25
    fpu     : yes
    fpu_exception   : yes
    cpuid level : 35
    wp      : yes
    flags       : fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush dts acpi mmx fxsr sse sse2 ss ht tm pbe syscall nx pdpe1gb rdtscp lm constant_tsc art arch_perfmon pebs bts rep_good nopl xtopology nonstop_tsc cpuid aperfmperf tsc_known_freq pni pclmulqdq dtes64 monitor ds_cpl vmx smx est tm2 ssse3 sdbg fma cx16 xtpr pdcm pcid sse4_1 sse4_2 x2apic movbe popcnt tsc_deadline_timer aes xsave avx f16c rdrand lahf_lm abm 3dnowprefetch cpuid_fault epb intel_ppin ssbd ibrs ibpb stibp ibrs_enhanced tpr_shadow flexpriority ept vpid ept_ad fsgsbase tsc_adjust bmi1 avx2 smep bmi2 erms invpcid rdseed adx smap clflushopt clwb intel_pt sha_ni xsaveopt xsavec xgetbv1 xsaves split_lock_detect user_shstk avx_vnni dtherm ida arat pln pts hwp hwp_notify hwp_act_window hwp_epp hwp_pkg_req hfi vnmi umip pku ospke waitpkg gfni vaes vpclmulqdq rdpid bus_lock_detect movdiri movdir64b fsrm md_clear serialize arch_lbr ibt flush_l1d arch_capabilities
    vmx flags   : vnmi preemption_timer posted_intr invvpid ept_x_only ept_ad ept_1gb flexpriority apicv tsc_offset vtpr mtf vapic ept vpid unrestricted_guest vapic_reg vid ple shadow_vmcs pml ept_violation_ve ept_mode_based_exec tsc_scaling usr_wait_pause notify_vm_exiting
    bugs        : spectre_v1 spectre_v2 spec_store_bypass swapgs bhi
    bogomips    : 5990.40
    clflush size    : 64
    cache_alignment : 64
    address sizes   : 46 bits physical, 48 bits virtual
    power management:

    processor   : 5
    vendor_id   : GenuineIntel
    cpu family  : 6
    model       : 170
    model name  : Intel(R) Core(TM) Ultra 7 155H
    stepping    : 4
    microcode   : 0x17
    cpu MHz     : 2793.442
    cache size  : 24576 KB
    physical id : 0
    siblings    : 22
    core id     : 16
    cpu cores   : 16
    apicid      : 33
    initial apicid  : 33
    fpu     : yes
    fpu_exception   : yes
    cpuid level : 35
    wp      : yes
    flags       : fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush dts acpi mmx fxsr sse sse2 ss ht tm pbe syscall nx pdpe1gb rdtscp lm constant_tsc art arch_perfmon pebs bts rep_good nopl xtopology nonstop_tsc cpuid aperfmperf tsc_known_freq pni pclmulqdq dtes64 monitor ds_cpl vmx smx est tm2 ssse3 sdbg fma cx16 xtpr pdcm pcid sse4_1 sse4_2 x2apic movbe popcnt tsc_deadline_timer aes xsave avx f16c rdrand lahf_lm abm 3dnowprefetch cpuid_fault epb intel_ppin ssbd ibrs ibpb stibp ibrs_enhanced tpr_shadow flexpriority ept vpid ept_ad fsgsbase tsc_adjust bmi1 avx2 smep bmi2 erms invpcid rdseed adx smap clflushopt clwb intel_pt sha_ni xsaveopt xsavec xgetbv1 xsaves split_lock_detect user_shstk avx_vnni dtherm ida arat pln pts hwp hwp_notify hwp_act_window hwp_epp hwp_pkg_req hfi vnmi umip pku ospke waitpkg gfni vaes vpclmulqdq rdpid bus_lock_detect movdiri movdir64b fsrm md_clear serialize arch_lbr ibt flush_l1d arch_capabilities
    vmx flags   : vnmi preemption_timer posted_intr invvpid ept_x_only ept_ad ept_1gb flexpriority apicv tsc_offset vtpr mtf vapic ept vpid unrestricted_guest vapic_reg vid ple shadow_vmcs pml ept_violation_ve ept_mode_based_exec tsc_scaling usr_wait_pause notify_vm_exiting
    bugs        : spectre_v1 spectre_v2 spec_store_bypass swapgs bhi
    bogomips    : 5990.40
    clflush size    : 64
    cache_alignment : 64
    address sizes   : 46 bits physical, 48 bits virtual
    power management:

    processor   : 6
    vendor_id   : GenuineIntel
    cpu family  : 6
    model       : 170
    model name  : Intel(R) Core(TM) Ultra 7 155H
    stepping    : 4
    microcode   : 0x17
    cpu MHz     : 2900.000
    cache size  : 24576 KB
    physical id : 0
    siblings    : 22
    core id     : 20
    cpu cores   : 16
    apicid      : 40
    initial apicid  : 40
    fpu     : yes
    fpu_exception   : yes
    cpuid level : 35
    wp      : yes
    flags       : fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush dts acpi mmx fxsr sse sse2 ss ht tm pbe syscall nx pdpe1gb rdtscp lm constant_tsc art arch_perfmon pebs bts rep_good nopl xtopology nonstop_tsc cpuid aperfmperf tsc_known_freq pni pclmulqdq dtes64 monitor ds_cpl vmx smx est tm2 ssse3 sdbg fma cx16 xtpr pdcm pcid sse4_1 sse4_2 x2apic movbe popcnt tsc_deadline_timer aes xsave avx f16c rdrand lahf_lm abm 3dnowprefetch cpuid_fault epb intel_ppin ssbd ibrs ibpb stibp ibrs_enhanced tpr_shadow flexpriority ept vpid ept_ad fsgsbase tsc_adjust bmi1 avx2 smep bmi2 erms invpcid rdseed adx smap clflushopt clwb intel_pt sha_ni xsaveopt xsavec xgetbv1 xsaves split_lock_detect user_shstk avx_vnni dtherm ida arat pln pts hwp hwp_notify hwp_act_window hwp_epp hwp_pkg_req hfi vnmi umip pku ospke waitpkg gfni vaes vpclmulqdq rdpid bus_lock_detect movdiri movdir64b fsrm md_clear serialize arch_lbr ibt flush_l1d arch_capabilities
    vmx flags   : vnmi preemption_timer posted_intr invvpid ept_x_only ept_ad ept_1gb flexpriority apicv tsc_offset vtpr mtf vapic ept vpid unrestricted_guest vapic_reg vid ple shadow_vmcs pml ept_violation_ve ept_mode_based_exec tsc_scaling usr_wait_pause notify_vm_exiting
    bugs        : spectre_v1 spectre_v2 spec_store_bypass swapgs bhi
    bogomips    : 5990.40
    clflush size    : 64
    cache_alignment : 64
    address sizes   : 46 bits physical, 48 bits virtual
    power management:

    processor   : 7
    vendor_id   : GenuineIntel
    cpu family  : 6
    model       : 170
    model name  : Intel(R) Core(TM) Ultra 7 155H
    stepping    : 4
    microcode   : 0x17
    cpu MHz     : 400.000
    cache size  : 24576 KB
    physical id : 0
    siblings    : 22
    core id     : 20
    cpu cores   : 16
    apicid      : 41
    initial apicid  : 41
    fpu     : yes
    fpu_exception   : yes
    cpuid level : 35
    wp      : yes
    flags       : fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush dts acpi mmx fxsr sse sse2 ss ht tm pbe syscall nx pdpe1gb rdtscp lm constant_tsc art arch_perfmon pebs bts rep_good nopl xtopology nonstop_tsc cpuid aperfmperf tsc_known_freq pni pclmulqdq dtes64 monitor ds_cpl vmx smx est tm2 ssse3 sdbg fma cx16 xtpr pdcm pcid sse4_1 sse4_2 x2apic movbe popcnt tsc_deadline_timer aes xsave avx f16c rdrand lahf_lm abm 3dnowprefetch cpuid_fault epb intel_ppin ssbd ibrs ibpb stibp ibrs_enhanced tpr_shadow flexpriority ept vpid ept_ad fsgsbase tsc_adjust bmi1 avx2 smep bmi2 erms invpcid rdseed adx smap clflushopt clwb intel_pt sha_ni xsaveopt xsavec xgetbv1 xsaves split_lock_detect user_shstk avx_vnni dtherm ida arat pln pts hwp hwp_notify hwp_act_window hwp_epp hwp_pkg_req hfi vnmi umip pku ospke waitpkg gfni vaes vpclmulqdq rdpid bus_lock_detect movdiri movdir64b fsrm md_clear serialize arch_lbr ibt flush_l1d arch_capabilities
    vmx flags   : vnmi preemption_timer posted_intr invvpid ept_x_only ept_ad ept_1gb flexpriority apicv tsc_offset vtpr mtf vapic ept vpid unrestricted_guest vapic_reg vid ple shadow_vmcs pml ept_violation_ve ept_mode_based_exec tsc_scaling usr_wait_pause notify_vm_exiting
    bugs        : spectre_v1 spectre_v2 spec_store_bypass swapgs bhi
    bogomips    : 5990.40
    clflush size    : 64
    cache_alignment : 64
    address sizes   : 46 bits physical, 48 bits virtual
    power management:

    processor   : 8
    vendor_id   : GenuineIntel
    cpu family  : 6
    model       : 170
    model name  : Intel(R) Core(TM) Ultra 7 155H
    stepping    : 4
    microcode   : 0x17
    cpu MHz     : 1995.012
    cache size  : 24576 KB
    physical id : 0
    siblings    : 22
    core id     : 24
    cpu cores   : 16
    apicid      : 48
    initial apicid  : 48
    fpu     : yes
    fpu_exception   : yes
    cpuid level : 35
    wp      : yes
    flags       : fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush dts acpi mmx fxsr sse sse2 ss ht tm pbe syscall nx pdpe1gb rdtscp lm constant_tsc art arch_perfmon pebs bts rep_good nopl xtopology nonstop_tsc cpuid aperfmperf tsc_known_freq pni pclmulqdq dtes64 monitor ds_cpl vmx smx est tm2 ssse3 sdbg fma cx16 xtpr pdcm pcid sse4_1 sse4_2 x2apic movbe popcnt tsc_deadline_timer aes xsave avx f16c rdrand lahf_lm abm 3dnowprefetch cpuid_fault epb intel_ppin ssbd ibrs ibpb stibp ibrs_enhanced tpr_shadow flexpriority ept vpid ept_ad fsgsbase tsc_adjust bmi1 avx2 smep bmi2 erms invpcid rdseed adx smap clflushopt clwb intel_pt sha_ni xsaveopt xsavec xgetbv1 xsaves split_lock_detect user_shstk avx_vnni dtherm ida arat pln pts hwp hwp_notify hwp_act_window hwp_epp hwp_pkg_req hfi vnmi umip pku ospke waitpkg gfni vaes vpclmulqdq rdpid bus_lock_detect movdiri movdir64b fsrm md_clear serialize arch_lbr ibt flush_l1d arch_capabilities
    vmx flags   : vnmi preemption_timer posted_intr invvpid ept_x_only ept_ad ept_1gb flexpriority apicv tsc_offset vtpr mtf vapic ept vpid unrestricted_guest vapic_reg vid ple shadow_vmcs pml ept_violation_ve ept_mode_based_exec tsc_scaling usr_wait_pause notify_vm_exiting
    bugs        : spectre_v1 spectre_v2 spec_store_bypass swapgs bhi
    bogomips    : 5990.40
    clflush size    : 64
    cache_alignment : 64
    address sizes   : 46 bits physical, 48 bits virtual
    power management:

    processor   : 9
    vendor_id   : GenuineIntel
    cpu family  : 6
    model       : 170
    model name  : Intel(R) Core(TM) Ultra 7 155H
    stepping    : 4
    microcode   : 0x17
    cpu MHz     : 400.000
    cache size  : 24576 KB
    physical id : 0
    siblings    : 22
    core id     : 24
    cpu cores   : 16
    apicid      : 49
    initial apicid  : 49
    fpu     : yes
    fpu_exception   : yes
    cpuid level : 35
    wp      : yes
    flags       : fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush dts acpi mmx fxsr sse sse2 ss ht tm pbe syscall nx pdpe1gb rdtscp lm constant_tsc art arch_perfmon pebs bts rep_good nopl xtopology nonstop_tsc cpuid aperfmperf tsc_known_freq pni pclmulqdq dtes64 monitor ds_cpl vmx smx est tm2 ssse3 sdbg fma cx16 xtpr pdcm pcid sse4_1 sse4_2 x2apic movbe popcnt tsc_deadline_timer aes xsave avx f16c rdrand lahf_lm abm 3dnowprefetch cpuid_fault epb intel_ppin ssbd ibrs ibpb stibp ibrs_enhanced tpr_shadow flexpriority ept vpid ept_ad fsgsbase tsc_adjust bmi1 avx2 smep bmi2 erms invpcid rdseed adx smap clflushopt clwb intel_pt sha_ni xsaveopt xsavec xgetbv1 xsaves split_lock_detect user_shstk avx_vnni dtherm ida arat pln pts hwp hwp_notify hwp_act_window hwp_epp hwp_pkg_req hfi vnmi umip pku ospke waitpkg gfni vaes vpclmulqdq rdpid bus_lock_detect movdiri movdir64b fsrm md_clear serialize arch_lbr ibt flush_l1d arch_capabilities
    vmx flags   : vnmi preemption_timer posted_intr invvpid ept_x_only ept_ad ept_1gb flexpriority apicv tsc_offset vtpr mtf vapic ept vpid unrestricted_guest vapic_reg vid ple shadow_vmcs pml ept_violation_ve ept_mode_based_exec tsc_scaling usr_wait_pause notify_vm_exiting
    bugs        : spectre_v1 spectre_v2 spec_store_bypass swapgs bhi
    bogomips    : 5990.40
    clflush size    : 64
    cache_alignment : 64
    address sizes   : 46 bits physical, 48 bits virtual
    power management:

    processor   : 10
    vendor_id   : GenuineIntel
    cpu family  : 6
    model       : 170
    model name  : Intel(R) Core(TM) Ultra 7 155H
    stepping    : 4
    microcode   : 0x17
    cpu MHz     : 400.000
    cache size  : 24576 KB
    physical id : 0
    siblings    : 22
    core id     : 28
    cpu cores   : 16
    apicid      : 56
    initial apicid  : 56
    fpu     : yes
    fpu_exception   : yes
    cpuid level : 35
    wp      : yes
    flags       : fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush dts acpi mmx fxsr sse sse2 ss ht tm pbe syscall nx pdpe1gb rdtscp lm constant_tsc art arch_perfmon pebs bts rep_good nopl xtopology nonstop_tsc cpuid aperfmperf tsc_known_freq pni pclmulqdq dtes64 monitor ds_cpl vmx smx est tm2 ssse3 sdbg fma cx16 xtpr pdcm pcid sse4_1 sse4_2 x2apic movbe popcnt tsc_deadline_timer aes xsave avx f16c rdrand lahf_lm abm 3dnowprefetch cpuid_fault epb intel_ppin ssbd ibrs ibpb stibp ibrs_enhanced tpr_shadow flexpriority ept vpid ept_ad fsgsbase tsc_adjust bmi1 avx2 smep bmi2 erms invpcid rdseed adx smap clflushopt clwb intel_pt sha_ni xsaveopt xsavec xgetbv1 xsaves split_lock_detect user_shstk avx_vnni dtherm ida arat pln pts hwp hwp_notify hwp_act_window hwp_epp hwp_pkg_req hfi vnmi umip pku ospke waitpkg gfni vaes vpclmulqdq rdpid bus_lock_detect movdiri movdir64b fsrm md_clear serialize arch_lbr ibt flush_l1d arch_capabilities
    vmx flags   : vnmi preemption_timer posted_intr invvpid ept_x_only ept_ad ept_1gb flexpriority apicv tsc_offset vtpr mtf vapic ept vpid unrestricted_guest vapic_reg vid ple shadow_vmcs pml ept_violation_ve ept_mode_based_exec tsc_scaling usr_wait_pause notify_vm_exiting
    bugs        : spectre_v1 spectre_v2 spec_store_bypass swapgs bhi
    bogomips    : 5990.40
    clflush size    : 64
    cache_alignment : 64
    address sizes   : 46 bits physical, 48 bits virtual
    power management:

    processor   : 11
    vendor_id   : GenuineIntel
    cpu family  : 6
    model       : 170
    model name  : Intel(R) Core(TM) Ultra 7 155H
    stepping    : 4
    microcode   : 0x17
    cpu MHz     : 2800.000
    cache size  : 24576 KB
    physical id : 0
    siblings    : 22
    core id     : 28
    cpu cores   : 16
    apicid      : 57
    initial apicid  : 57
    fpu     : yes
    fpu_exception   : yes
    cpuid level : 35
    wp      : yes
    flags       : fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush dts acpi mmx fxsr sse sse2 ss ht tm pbe syscall nx pdpe1gb rdtscp lm constant_tsc art arch_perfmon pebs bts rep_good nopl xtopology nonstop_tsc cpuid aperfmperf tsc_known_freq pni pclmulqdq dtes64 monitor ds_cpl vmx smx est tm2 ssse3 sdbg fma cx16 xtpr pdcm pcid sse4_1 sse4_2 x2apic movbe popcnt tsc_deadline_timer aes xsave avx f16c rdrand lahf_lm abm 3dnowprefetch cpuid_fault epb intel_ppin ssbd ibrs ibpb stibp ibrs_enhanced tpr_shadow flexpriority ept vpid ept_ad fsgsbase tsc_adjust bmi1 avx2 smep bmi2 erms invpcid rdseed adx smap clflushopt clwb intel_pt sha_ni xsaveopt xsavec xgetbv1 xsaves split_lock_detect user_shstk avx_vnni dtherm ida arat pln pts hwp hwp_notify hwp_act_window hwp_epp hwp_pkg_req hfi vnmi umip pku ospke waitpkg gfni vaes vpclmulqdq rdpid bus_lock_detect movdiri movdir64b fsrm md_clear serialize arch_lbr ibt flush_l1d arch_capabilities
    vmx flags   : vnmi preemption_timer posted_intr invvpid ept_x_only ept_ad ept_1gb flexpriority apicv tsc_offset vtpr mtf vapic ept vpid unrestricted_guest vapic_reg vid ple shadow_vmcs pml ept_violation_ve ept_mode_based_exec tsc_scaling usr_wait_pause notify_vm_exiting
    bugs        : spectre_v1 spectre_v2 spec_store_bypass swapgs bhi
    bogomips    : 5990.40
    clflush size    : 64
    cache_alignment : 64
    address sizes   : 46 bits physical, 48 bits virtual
    power management:

    processor   : 12
    vendor_id   : GenuineIntel
    cpu family  : 6
    model       : 170
    model name  : Intel(R) Core(TM) Ultra 7 155H
    stepping    : 4
    microcode   : 0x17
    cpu MHz     : 2251.642
    cache size  : 24576 KB
    physical id : 0
    siblings    : 22
    core id     : 0
    cpu cores   : 16
    apicid      : 0
    initial apicid  : 0
    fpu     : yes
    fpu_exception   : yes
    cpuid level : 35
    wp      : yes
    flags       : fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush dts acpi mmx fxsr sse sse2 ss ht tm pbe syscall nx pdpe1gb rdtscp lm constant_tsc art arch_perfmon pebs bts rep_good nopl xtopology nonstop_tsc cpuid aperfmperf tsc_known_freq pni pclmulqdq dtes64 monitor ds_cpl vmx smx est tm2 ssse3 sdbg fma cx16 xtpr pdcm pcid sse4_1 sse4_2 x2apic movbe popcnt tsc_deadline_timer aes xsave avx f16c rdrand lahf_lm abm 3dnowprefetch cpuid_fault epb intel_ppin ssbd ibrs ibpb stibp ibrs_enhanced tpr_shadow flexpriority ept vpid ept_ad fsgsbase tsc_adjust bmi1 avx2 smep bmi2 erms invpcid rdseed adx smap clflushopt clwb intel_pt sha_ni xsaveopt xsavec xgetbv1 xsaves split_lock_detect user_shstk avx_vnni dtherm ida arat pln pts hwp hwp_notify hwp_act_window hwp_epp hwp_pkg_req hfi vnmi umip pku ospke waitpkg gfni vaes vpclmulqdq rdpid bus_lock_detect movdiri movdir64b fsrm md_clear serialize arch_lbr ibt flush_l1d arch_capabilities
    vmx flags   : vnmi preemption_timer posted_intr invvpid ept_x_only ept_ad ept_1gb flexpriority apicv tsc_offset vtpr mtf vapic ept vpid unrestricted_guest vapic_reg vid ple shadow_vmcs pml ept_violation_ve ept_mode_based_exec tsc_scaling usr_wait_pause notify_vm_exiting
    bugs        : spectre_v1 spectre_v2 spec_store_bypass swapgs bhi
    bogomips    : 5990.40
    clflush size    : 64
    cache_alignment : 64
    address sizes   : 46 bits physical, 48 bits virtual
    power management:

    processor   : 13
    vendor_id   : GenuineIntel
    cpu family  : 6
    model       : 170
    model name  : Intel(R) Core(TM) Ultra 7 155H
    stepping    : 4
    microcode   : 0x17
    cpu MHz     : 1639.430
    cache size  : 24576 KB
    physical id : 0
    siblings    : 22
    core id     : 1
    cpu cores   : 16
    apicid      : 2
    initial apicid  : 2
    fpu     : yes
    fpu_exception   : yes
    cpuid level : 35
    wp      : yes
    flags       : fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush dts acpi mmx fxsr sse sse2 ss ht tm pbe syscall nx pdpe1gb rdtscp lm constant_tsc art arch_perfmon pebs bts rep_good nopl xtopology nonstop_tsc cpuid aperfmperf tsc_known_freq pni pclmulqdq dtes64 monitor ds_cpl vmx smx est tm2 ssse3 sdbg fma cx16 xtpr pdcm pcid sse4_1 sse4_2 x2apic movbe popcnt tsc_deadline_timer aes xsave avx f16c rdrand lahf_lm abm 3dnowprefetch cpuid_fault epb intel_ppin ssbd ibrs ibpb stibp ibrs_enhanced tpr_shadow flexpriority ept vpid ept_ad fsgsbase tsc_adjust bmi1 avx2 smep bmi2 erms invpcid rdseed adx smap clflushopt clwb intel_pt sha_ni xsaveopt xsavec xgetbv1 xsaves split_lock_detect user_shstk avx_vnni dtherm ida arat pln pts hwp hwp_notify hwp_act_window hwp_epp hwp_pkg_req hfi vnmi umip pku ospke waitpkg gfni vaes vpclmulqdq rdpid bus_lock_detect movdiri movdir64b fsrm md_clear serialize arch_lbr ibt flush_l1d arch_capabilities
    vmx flags   : vnmi preemption_timer posted_intr invvpid ept_x_only ept_ad ept_1gb flexpriority apicv tsc_offset vtpr mtf vapic ept vpid unrestricted_guest vapic_reg vid ple shadow_vmcs pml ept_violation_ve ept_mode_based_exec tsc_scaling usr_wait_pause notify_vm_exiting
    bugs        : spectre_v1 spectre_v2 spec_store_bypass swapgs bhi
    bogomips    : 5990.40
    clflush size    : 64
    cache_alignment : 64
    address sizes   : 46 bits physical, 48 bits virtual
    power management:

    processor   : 14
    vendor_id   : GenuineIntel
    cpu family  : 6
    model       : 170
    model name  : Intel(R) Core(TM) Ultra 7 155H
    stepping    : 4
    microcode   : 0x17
    cpu MHz     : 1647.747
    cache size  : 24576 KB
    physical id : 0
    siblings    : 22
    core id     : 2
    cpu cores   : 16
    apicid      : 4
    initial apicid  : 4
    fpu     : yes
    fpu_exception   : yes
    cpuid level : 35
    wp      : yes
    flags       : fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush dts acpi mmx fxsr sse sse2 ss ht tm pbe syscall nx pdpe1gb rdtscp lm constant_tsc art arch_perfmon pebs bts rep_good nopl xtopology nonstop_tsc cpuid aperfmperf tsc_known_freq pni pclmulqdq dtes64 monitor ds_cpl vmx smx est tm2 ssse3 sdbg fma cx16 xtpr pdcm pcid sse4_1 sse4_2 x2apic movbe popcnt tsc_deadline_timer aes xsave avx f16c rdrand lahf_lm abm 3dnowprefetch cpuid_fault epb intel_ppin ssbd ibrs ibpb stibp ibrs_enhanced tpr_shadow flexpriority ept vpid ept_ad fsgsbase tsc_adjust bmi1 avx2 smep bmi2 erms invpcid rdseed adx smap clflushopt clwb intel_pt sha_ni xsaveopt xsavec xgetbv1 xsaves split_lock_detect user_shstk avx_vnni dtherm ida arat pln pts hwp hwp_notify hwp_act_window hwp_epp hwp_pkg_req hfi vnmi umip pku ospke waitpkg gfni vaes vpclmulqdq rdpid bus_lock_detect movdiri movdir64b fsrm md_clear serialize arch_lbr ibt flush_l1d arch_capabilities
    vmx flags   : vnmi preemption_timer posted_intr invvpid ept_x_only ept_ad ept_1gb flexpriority apicv tsc_offset vtpr mtf vapic ept vpid unrestricted_guest vapic_reg vid ple shadow_vmcs pml ept_violation_ve ept_mode_based_exec tsc_scaling usr_wait_pause notify_vm_exiting
    bugs        : spectre_v1 spectre_v2 spec_store_bypass swapgs bhi
    bogomips    : 5990.40
    clflush size    : 64
    cache_alignment : 64
    address sizes   : 46 bits physical, 48 bits virtual
    power management:

    processor   : 15
    vendor_id   : GenuineIntel
    cpu family  : 6
    model       : 170
    model name  : Intel(R) Core(TM) Ultra 7 155H
    stepping    : 4
    microcode   : 0x17
    cpu MHz     : 2272.653
    cache size  : 24576 KB
    physical id : 0
    siblings    : 22
    core id     : 3
    cpu cores   : 16
    apicid      : 6
    initial apicid  : 6
    fpu     : yes
    fpu_exception   : yes
    cpuid level : 35
    wp      : yes
    flags       : fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush dts acpi mmx fxsr sse sse2 ss ht tm pbe syscall nx pdpe1gb rdtscp lm constant_tsc art arch_perfmon pebs bts rep_good nopl xtopology nonstop_tsc cpuid aperfmperf tsc_known_freq pni pclmulqdq dtes64 monitor ds_cpl vmx smx est tm2 ssse3 sdbg fma cx16 xtpr pdcm pcid sse4_1 sse4_2 x2apic movbe popcnt tsc_deadline_timer aes xsave avx f16c rdrand lahf_lm abm 3dnowprefetch cpuid_fault epb intel_ppin ssbd ibrs ibpb stibp ibrs_enhanced tpr_shadow flexpriority ept vpid ept_ad fsgsbase tsc_adjust bmi1 avx2 smep bmi2 erms invpcid rdseed adx smap clflushopt clwb intel_pt sha_ni xsaveopt xsavec xgetbv1 xsaves split_lock_detect user_shstk avx_vnni dtherm ida arat pln pts hwp hwp_notify hwp_act_window hwp_epp hwp_pkg_req hfi vnmi umip pku ospke waitpkg gfni vaes vpclmulqdq rdpid bus_lock_detect movdiri movdir64b fsrm md_clear serialize arch_lbr ibt flush_l1d arch_capabilities
    vmx flags   : vnmi preemption_timer posted_intr invvpid ept_x_only ept_ad ept_1gb flexpriority apicv tsc_offset vtpr mtf vapic ept vpid unrestricted_guest vapic_reg vid ple shadow_vmcs pml ept_violation_ve ept_mode_based_exec tsc_scaling usr_wait_pause notify_vm_exiting
    bugs        : spectre_v1 spectre_v2 spec_store_bypass swapgs bhi
    bogomips    : 5990.40
    clflush size    : 64
    cache_alignment : 64
    address sizes   : 46 bits physical, 48 bits virtual
    power management:

    processor   : 16
    vendor_id   : GenuineIntel
    cpu family  : 6
    model       : 170
    model name  : Intel(R) Core(TM) Ultra 7 155H
    stepping    : 4
    microcode   : 0x17
    cpu MHz     : 2197.520
    cache size  : 24576 KB
    physical id : 0
    siblings    : 22
    core id     : 4
    cpu cores   : 16
    apicid      : 8
    initial apicid  : 8
    fpu     : yes
    fpu_exception   : yes
    cpuid level : 35
    wp      : yes
    flags       : fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush dts acpi mmx fxsr sse sse2 ss ht tm pbe syscall nx pdpe1gb rdtscp lm constant_tsc art arch_perfmon pebs bts rep_good nopl xtopology nonstop_tsc cpuid aperfmperf tsc_known_freq pni pclmulqdq dtes64 monitor ds_cpl vmx smx est tm2 ssse3 sdbg fma cx16 xtpr pdcm pcid sse4_1 sse4_2 x2apic movbe popcnt tsc_deadline_timer aes xsave avx f16c rdrand lahf_lm abm 3dnowprefetch cpuid_fault epb intel_ppin ssbd ibrs ibpb stibp ibrs_enhanced tpr_shadow flexpriority ept vpid ept_ad fsgsbase tsc_adjust bmi1 avx2 smep bmi2 erms invpcid rdseed adx smap clflushopt clwb intel_pt sha_ni xsaveopt xsavec xgetbv1 xsaves split_lock_detect user_shstk avx_vnni dtherm ida arat pln pts hwp hwp_notify hwp_act_window hwp_epp hwp_pkg_req hfi vnmi umip pku ospke waitpkg gfni vaes vpclmulqdq rdpid bus_lock_detect movdiri movdir64b fsrm md_clear serialize arch_lbr ibt flush_l1d arch_capabilities
    vmx flags   : vnmi preemption_timer posted_intr invvpid ept_x_only ept_ad ept_1gb flexpriority apicv tsc_offset vtpr mtf vapic ept vpid unrestricted_guest vapic_reg vid ple shadow_vmcs pml ept_violation_ve ept_mode_based_exec tsc_scaling usr_wait_pause notify_vm_exiting
    bugs        : spectre_v1 spectre_v2 spec_store_bypass swapgs bhi
    bogomips    : 5990.40
    clflush size    : 64
    cache_alignment : 64
    address sizes   : 46 bits physical, 48 bits virtual
    power management:

    processor   : 17
    vendor_id   : GenuineIntel
    cpu family  : 6
    model       : 170
    model name  : Intel(R) Core(TM) Ultra 7 155H
    stepping    : 4
    microcode   : 0x17
    cpu MHz     : 2190.533
    cache size  : 24576 KB
    physical id : 0
    siblings    : 22
    core id     : 5
    cpu cores   : 16
    apicid      : 10
    initial apicid  : 10
    fpu     : yes
    fpu_exception   : yes
    cpuid level : 35
    wp      : yes
    flags       : fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush dts acpi mmx fxsr sse sse2 ss ht tm pbe syscall nx pdpe1gb rdtscp lm constant_tsc art arch_perfmon pebs bts rep_good nopl xtopology nonstop_tsc cpuid aperfmperf tsc_known_freq pni pclmulqdq dtes64 monitor ds_cpl vmx smx est tm2 ssse3 sdbg fma cx16 xtpr pdcm pcid sse4_1 sse4_2 x2apic movbe popcnt tsc_deadline_timer aes xsave avx f16c rdrand lahf_lm abm 3dnowprefetch cpuid_fault epb intel_ppin ssbd ibrs ibpb stibp ibrs_enhanced tpr_shadow flexpriority ept vpid ept_ad fsgsbase tsc_adjust bmi1 avx2 smep bmi2 erms invpcid rdseed adx smap clflushopt clwb intel_pt sha_ni xsaveopt xsavec xgetbv1 xsaves split_lock_detect user_shstk avx_vnni dtherm ida arat pln pts hwp hwp_notify hwp_act_window hwp_epp hwp_pkg_req hfi vnmi umip pku ospke waitpkg gfni vaes vpclmulqdq rdpid bus_lock_detect movdiri movdir64b fsrm md_clear serialize arch_lbr ibt flush_l1d arch_capabilities
    vmx flags   : vnmi preemption_timer posted_intr invvpid ept_x_only ept_ad ept_1gb flexpriority apicv tsc_offset vtpr mtf vapic ept vpid unrestricted_guest vapic_reg vid ple shadow_vmcs pml ept_violation_ve ept_mode_based_exec tsc_scaling usr_wait_pause notify_vm_exiting
    bugs        : spectre_v1 spectre_v2 spec_store_bypass swapgs bhi
    bogomips    : 5990.40
    clflush size    : 64
    cache_alignment : 64
    address sizes   : 46 bits physical, 48 bits virtual
    power management:

    processor   : 18
    vendor_id   : GenuineIntel
    cpu family  : 6
    model       : 170
    model name  : Intel(R) Core(TM) Ultra 7 155H
    stepping    : 4
    microcode   : 0x17
    cpu MHz     : 2200.736
    cache size  : 24576 KB
    physical id : 0
    siblings    : 22
    core id     : 6
    cpu cores   : 16
    apicid      : 12
    initial apicid  : 12
    fpu     : yes
    fpu_exception   : yes
    cpuid level : 35
    wp      : yes
    flags       : fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush dts acpi mmx fxsr sse sse2 ss ht tm pbe syscall nx pdpe1gb rdtscp lm constant_tsc art arch_perfmon pebs bts rep_good nopl xtopology nonstop_tsc cpuid aperfmperf tsc_known_freq pni pclmulqdq dtes64 monitor ds_cpl vmx smx est tm2 ssse3 sdbg fma cx16 xtpr pdcm pcid sse4_1 sse4_2 x2apic movbe popcnt tsc_deadline_timer aes xsave avx f16c rdrand lahf_lm abm 3dnowprefetch cpuid_fault epb intel_ppin ssbd ibrs ibpb stibp ibrs_enhanced tpr_shadow flexpriority ept vpid ept_ad fsgsbase tsc_adjust bmi1 avx2 smep bmi2 erms invpcid rdseed adx smap clflushopt clwb intel_pt sha_ni xsaveopt xsavec xgetbv1 xsaves split_lock_detect user_shstk avx_vnni dtherm ida arat pln pts hwp hwp_notify hwp_act_window hwp_epp hwp_pkg_req hfi vnmi umip pku ospke waitpkg gfni vaes vpclmulqdq rdpid bus_lock_detect movdiri movdir64b fsrm md_clear serialize arch_lbr ibt flush_l1d arch_capabilities
    vmx flags   : vnmi preemption_timer posted_intr invvpid ept_x_only ept_ad ept_1gb flexpriority apicv tsc_offset vtpr mtf vapic ept vpid unrestricted_guest vapic_reg vid ple shadow_vmcs pml ept_violation_ve ept_mode_based_exec tsc_scaling usr_wait_pause notify_vm_exiting
    bugs        : spectre_v1 spectre_v2 spec_store_bypass swapgs bhi
    bogomips    : 5990.40
    clflush size    : 64
    cache_alignment : 64
    address sizes   : 46 bits physical, 48 bits virtual
    power management:

    processor   : 19
    vendor_id   : GenuineIntel
    cpu family  : 6
    model       : 170
    model name  : Intel(R) Core(TM) Ultra 7 155H
    stepping    : 4
    microcode   : 0x17
    cpu MHz     : 2200.508
    cache size  : 24576 KB
    physical id : 0
    siblings    : 22
    core id     : 7
    cpu cores   : 16
    apicid      : 14
    initial apicid  : 14
    fpu     : yes
    fpu_exception   : yes
    cpuid level : 35
    wp      : yes
    flags       : fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush dts acpi mmx fxsr sse sse2 ss ht tm pbe syscall nx pdpe1gb rdtscp lm constant_tsc art arch_perfmon pebs bts rep_good nopl xtopology nonstop_tsc cpuid aperfmperf tsc_known_freq pni pclmulqdq dtes64 monitor ds_cpl vmx smx est tm2 ssse3 sdbg fma cx16 xtpr pdcm pcid sse4_1 sse4_2 x2apic movbe popcnt tsc_deadline_timer aes xsave avx f16c rdrand lahf_lm abm 3dnowprefetch cpuid_fault epb intel_ppin ssbd ibrs ibpb stibp ibrs_enhanced tpr_shadow flexpriority ept vpid ept_ad fsgsbase tsc_adjust bmi1 avx2 smep bmi2 erms invpcid rdseed adx smap clflushopt clwb intel_pt sha_ni xsaveopt xsavec xgetbv1 xsaves split_lock_detect user_shstk avx_vnni dtherm ida arat pln pts hwp hwp_notify hwp_act_window hwp_epp hwp_pkg_req hfi vnmi umip pku ospke waitpkg gfni vaes vpclmulqdq rdpid bus_lock_detect movdiri movdir64b fsrm md_clear serialize arch_lbr ibt flush_l1d arch_capabilities
    vmx flags   : vnmi preemption_timer posted_intr invvpid ept_x_only ept_ad ept_1gb flexpriority apicv tsc_offset vtpr mtf vapic ept vpid unrestricted_guest vapic_reg vid ple shadow_vmcs pml ept_violation_ve ept_mode_based_exec tsc_scaling usr_wait_pause notify_vm_exiting
    bugs        : spectre_v1 spectre_v2 spec_store_bypass swapgs bhi
    bogomips    : 5990.40
    clflush size    : 64
    cache_alignment : 64
    address sizes   : 46 bits physical, 48 bits virtual
    power management:

    processor   : 20
    vendor_id   : GenuineIntel
    cpu family  : 6
    model       : 170
    model name  : Intel(R) Core(TM) Ultra 7 155H
    stepping    : 4
    microcode   : 0x17
    cpu MHz     : 400.000
    cache size  : 2048 KB
    physical id : 0
    siblings    : 22
    core id     : 32
    cpu cores   : 16
    apicid      : 64
    initial apicid  : 64
    fpu     : yes
    fpu_exception   : yes
    cpuid level : 35
    wp      : yes
    flags       : fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush dts acpi mmx fxsr sse sse2 ss ht tm pbe syscall nx pdpe1gb rdtscp lm constant_tsc art arch_perfmon pebs bts rep_good nopl xtopology nonstop_tsc cpuid aperfmperf tsc_known_freq pni pclmulqdq dtes64 monitor ds_cpl vmx smx est tm2 ssse3 sdbg fma cx16 xtpr pdcm pcid sse4_1 sse4_2 x2apic movbe popcnt tsc_deadline_timer aes xsave avx f16c rdrand lahf_lm abm 3dnowprefetch cpuid_fault epb intel_ppin ssbd ibrs ibpb stibp ibrs_enhanced tpr_shadow flexpriority ept vpid ept_ad fsgsbase tsc_adjust bmi1 avx2 smep bmi2 erms invpcid rdseed adx smap clflushopt clwb intel_pt sha_ni xsaveopt xsavec xgetbv1 xsaves split_lock_detect user_shstk avx_vnni dtherm ida arat pln pts hwp hwp_notify hwp_act_window hwp_epp hwp_pkg_req hfi vnmi umip pku ospke waitpkg gfni vaes vpclmulqdq rdpid bus_lock_detect movdiri movdir64b fsrm md_clear serialize arch_lbr ibt flush_l1d arch_capabilities
    vmx flags   : vnmi preemption_timer posted_intr invvpid ept_x_only ept_ad ept_1gb flexpriority apicv tsc_offset vtpr mtf vapic ept vpid unrestricted_guest vapic_reg vid ple shadow_vmcs pml ept_violation_ve ept_mode_based_exec tsc_scaling usr_wait_pause notify_vm_exiting
    bugs        : spectre_v1 spectre_v2 spec_store_bypass swapgs bhi
    bogomips    : 5990.40
    clflush size    : 64
    cache_alignment : 64
    address sizes   : 46 bits physical, 48 bits virtual
    power management:

    processor   : 21
    vendor_id   : GenuineIntel
    cpu family  : 6
    model       : 170
    model name  : Intel(R) Core(TM) Ultra 7 155H
    stepping    : 4
    microcode   : 0x17
    cpu MHz     : 400.000
    cache size  : 2048 KB
    physical id : 0
    siblings    : 22
    core id     : 33
    cpu cores   : 16
    apicid      : 66
    initial apicid  : 66
    fpu     : yes
    fpu_exception   : yes
    cpuid level : 35
    wp      : yes
    flags       : fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush dts acpi mmx fxsr sse sse2 ss ht tm pbe syscall nx pdpe1gb rdtscp lm constant_tsc art arch_perfmon pebs bts rep_good nopl xtopology nonstop_tsc cpuid aperfmperf tsc_known_freq pni pclmulqdq dtes64 monitor ds_cpl vmx smx est tm2 ssse3 sdbg fma cx16 xtpr pdcm pcid sse4_1 sse4_2 x2apic movbe popcnt tsc_deadline_timer aes xsave avx f16c rdrand lahf_lm abm 3dnowprefetch cpuid_fault epb intel_ppin ssbd ibrs ibpb stibp ibrs_enhanced tpr_shadow flexpriority ept vpid ept_ad fsgsbase tsc_adjust bmi1 avx2 smep bmi2 erms invpcid rdseed adx smap clflushopt clwb intel_pt sha_ni xsaveopt xsavec xgetbv1 xsaves split_lock_detect user_shstk avx_vnni dtherm ida arat pln pts hwp hwp_notify hwp_act_window hwp_epp hwp_pkg_req hfi vnmi umip pku ospke waitpkg gfni vaes vpclmulqdq rdpid bus_lock_detect movdiri movdir64b fsrm md_clear serialize arch_lbr ibt flush_l1d arch_capabilities
    vmx flags   : vnmi preemption_timer posted_intr invvpid ept_x_only ept_ad ept_1gb flexpriority apicv tsc_offset vtpr mtf vapic ept vpid unrestricted_guest vapic_reg vid ple shadow_vmcs pml ept_violation_ve ept_mode_based_exec tsc_scaling usr_wait_pause notify_vm_exiting
    bugs        : spectre_v1 spectre_v2 spec_store_bypass swapgs bhi
    bogomips    : 5990.40
    clflush size    : 64
    cache_alignment : 64
    address sizes   : 46 bits physical, 48 bits virtual
    power management:

## [Installation]

### [Kernel]

#### [Input devices]

#### [USB 3.0 support]

[KERNEL] **USB controller: *USB controller: Intel Corporation Meteor Lake-P USB 3.2 Gen 2x1 xHCI Host Controller (rev 20)*, 6.10.7-gentoo**

    Device Drivers  --->
        [*] USB support  --->
            <*>   xHCI HCD (USB 3.0) support

Kernel version 3.3 at least is required for the USB 3 support.

#### [Drives and storage]

[KERNEL] **Non-Volatile memory controller: Yangtze Memory Technologies Co.,Ltd PC300 NVMe SSD (DRAM-less) (rev 03), 6.10.7-gentoo**

    Device Drivers  --->
        NVME Support  --->
            <*>   NVM Express block device

If you want to install the user space tools run this:

`root `[`#`]`emerge --ask sys-apps/nvme-cli`

You can also read the full [NVMe](https://wiki.gentoo.org/wiki/NVMe "NVMe") article for more advanced NVMe support.

#### [Graphics]

** Warning**\
Xe is the new intel GPU driver, it\'s still experimental and WIP. Xe offers the best performance for Battlemage GPU, this guide will focus on this driver. However the old driver can be installed following the [Intel](https://wiki.gentoo.org/wiki/Intel "Intel") wiki page

Compile the Xe driver for Intel Arc as a module

[KERNEL] **VGA compatible controller: Intel Corporation Meteor Lake-P \[Intel Arc Graphics\] (rev 08), 6.10.7-gentoo**

    Device Drivers  --->
        Graphics support  --->
            <*> /dev/agpgart (AGP Support)  --->
                <*>   Intel 440LX/BX/GX, I8xx and E7x05 chipset support
            <*> Direct Rendering Manager (XFree86 4.1.0 and higher DRI support)  --->
                [*]   Enable DisplayPort CEC-Tunneling-over-AUX HDMI support
                [*]   DRM DP AUX Interface
                <M>   Intel Xe Graphics
                [*]     Enable display suppport

You also need the EFI frame buffer driver

[KERNEL] **VGA compatible controller: Intel Corporation Meteor Lake-P \[Intel Arc Graphics\] (rev 08), 6.10.7-gentoo**

    Device Drivers  --->
        Graphics support  --->
                Frame buffer Devices  --->
                <*>   Support for frame buffer device drivers  --->
                    [*]   EFI-based Framebuffer Support

##### [Force use of Xe probe]

You can add `xe.force_probe='7d55'` as module parameters in GRUB for example, or you can directly build that into the kernel, like in the example below.

[KERNEL] **VGA compatible controller: Intel Corporation Meteor Lake-P \[Intel Arc Graphics\] (rev 08), 6.10.7-gentoo**

    Device Drivers  --->
        Graphics support  --->
            <*> Direct Rendering Manager (XFree86 4.1.0 and higher DRI support)  --->
                <M>   Intel Xe Graphics
                (7d55)     Force probe xe for selected Intel hardware IDs

#### [Wi-Fi]

[KERNEL] **Network controller: Intel Corporation Meteor Lake PCH CNVi WiFi (rev 20), 6.10.7-gentoo**

    [*] Networking support  --->
        [*]   Wireless  --->
            <*>   Generic IEEE 802.11 Networking Stack (mac80211)

    Device Drivers  --->
        [*] Network device support  --->
        [*]    Wireless LAN  --->
                [*]   Intel devices
                <M>      Intel Wireless WiFi Next Gen AGN - Wireless-N/Advanced-N/Ultimate-N (iwlwifi)

This driver needs some firmware to run

`root `[`#`]`emerge --ask sys-kernel/linux-firmware`

#### [Sound]

** Note**\
Sound support for Meteor Lake was added in kernel 6.11

[KERNEL] **Sound device**

    Device Drivers  --->
        --- Sound card support  --->
            <M>   Advanced Linux Sound Architecture  --->
                <*>   ALSA for SoC audio support  --->
                   [*]   Intel ASoC SST drivers
                   <M>     CometLake-H Platforms
                   <M>     CometLake-LP Platforms
                   [*]     HDAudio codec support
                   [*]   Sound Open Firmware Support  --->
                       <M>   SOF PCI enumeration support
                       <M>   SOF ACPI enumeration support
                       [*]   SOF support for Intel audio DSPs
                       <M>     SOF support for Meteorlake
                       [*]     SOF support for HDA Links(HDA/HDMI)
                       [*]       SOF support for HDAudio codecs

You need to get the firmware from the SOF project

`root `[`#`]`emerge --ask sys-firmware/sof-firmware`

#### [CPU frequency scaling]

[KERNEL] **CPU frequency scaling, 6.10.7-gentoo**

    Power management and ACPI options  --->
        CPU Frequency scaling  --->
        [*] CPU Frequency scaling
        <*>   Intel P-States control
        <*>   ACPI Processor P-States driver

#### [NPU]

[KERNEL] **CPU frequency scaling, 6.10.7-gentoo**

    Device Drivers  --->
         [*] Compute Acceleration Framework  --->
            <M>   Intel NPU (Neural Processing Unit)

#### [Webcam]

[KERNEL] **Bus 003 Device 004: ID 2b7e:c817 SunplusIT Inc XiaoMi WebCam**

    Device Drivers  --->
        <M> Multimedia support  --->
             Media device types  --->
               [*] Cameras and video grabbers
             Media drivers  --->
               [*] Media USB Adapters  --->
                  <M>   USB Video Class (UVC)
                        [*]     UVC input events device support
               [*] Media PCI Adapters  --->
                  <*>   Intel IPU6 driver

#### [Bluetooth]

[KERNEL]

    [*] Networking support  --->
        <*> Bluetooth subsystem support  --->

            Select options for Bluetooth applications, see table below:
            <*>   ...

                Bluetooth device drivers  --->

                   Select a Bluetooth HCI driver, e.g.:
                   <*> HCI USB driver (btusb)

### [Misc]

#### [Fingerprint reader]

The laptop is equipied with a fingerprint reader, it is supported officially by fprint, but not before v1.94.9. This version is marked as testing on Gentoo. You also can patch an older version if you want to use the stable package. Thanks to portage we can automatically apply patches to packages, you need to create a directory for patches.

`root `[`#`]`mkdir -p /etc/portage/patches/sys-auth/libfprint`

Then create a file with .patch or .diff extension under the directory you just created and fill it with this patch :

[FILE] **`/etc/portage/patches/sys-auth/libfprint/fixfprintreader.patch`**

    diff --git a/libfprint/drivers/goodixmoc/goodix.c b/libfprint/drivers/goodixmoc/goodix.c
    index 5a3ffac..5b9af95 100644
    --- a/libfprint/drivers/goodixmoc/goodix.c
    +++ b/libfprint/drivers/goodixmoc/goodix.c
    @@ -1632,6 +1632,7 @@ static const FpIdEntry id_table[] = ,
       ,
       ,
    +  ,
       ,   /* terminating entry */
     };

You can now install fprint and it will support the laptop\'s fingerprint reader

`root `[`#`]`emerge --ask sys-auth/fprintd`