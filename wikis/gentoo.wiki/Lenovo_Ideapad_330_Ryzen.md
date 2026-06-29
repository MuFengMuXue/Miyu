**Resources**

[[]][Official Support Page](https://pcsupport.lenovo.com/us/en/products/laptops-and-netbooks/300-series/330-15arr)

[[]][Specifications (by region)](https://psref.lenovo.com/Product/IdeaPad/ideapad_33015ARR)

[[]][Hardware Maintenance Manual](https://download.lenovo.com/consumer/mobiles_pub/330-14igm_330-15igm_330-15icn_330-15arr_330touch-15arr_hmm_201805.pdf)

[[]][User Guide](https://download.lenovo.com/consumer/mobiles_pub/330-14igm_330-15igm_330-15icn_330-15arr_330touch-15arr_ug_en_201805.pdf)

[[]][BIOS/UEFI Official documentation](https://pcsupport.lenovo.com/us/en/products/LAPTOPS-AND-NETBOOKS/300-SERIES/330-15ARR/downloads/DS503857)

Following article aims to make the Lenovo Ideapad 330(-15ARR) usable on Gentoo.

## Contents

-   [[1] [Hardware information]](#Hardware_information)
    -   [[1.1] [lscpu]](#lscpu)
    -   [[1.2] [lspci]](#lspci)
    -   [[1.3] [lsusb]](#lsusb)
-   [[2] [Installation]](#Installation)
    -   [[2.1] [UEFI updates]](#UEFI_updates)
    -   [[2.2] [Legacy boot]](#Legacy_boot)
    -   [[2.3] [Firmware]](#Firmware)
    -   [[2.4] [Kernel]](#Kernel)
    -   [[2.5] [Configuration]](#Configuration)
        -   [[2.5.1] [Compiler settings]](#Compiler_settings)
        -   [[2.5.2] [Packages settings]](#Packages_settings)
        -   [[2.5.3] [USE flags]](#USE_flags)
    -   [[2.6] [Utils]](#Utils)
        -   [[2.6.1] [Battery charge thresholds]](#Battery_charge_thresholds)
        -   [[2.6.2] [fan control]](#fan_control)

## [Hardware information]

### [lscpu]

`root `[`#`]`lscpu`

    Architecture:        x86_64
    CPU op-mode(s):      32-bit, 64-bit
    Byte Order:          Little Endian
    CPU(s):              8
    On-line CPU(s) list: 0-7
    Thread(s) per core:  2
    Core(s) per socket:  4
    Socket(s):           1
    NUMA node(s):        1
    Vendor ID:           AuthenticAMD
    CPU family:          23
    Model:               17
    Model name:          AMD Ryzen 5 2500U with Radeon Vega Mobile Gfx
    Stepping:            0
    CPU MHz:             1444.502
    CPU max MHz:         2000.0000
    CPU min MHz:         1600.0000
    BogoMIPS:            3992.72
    Virtualization:      AMD-V
    L1d cache:           32K
    L1i cache:           64K
    L2 cache:            512K
    L3 cache:            4096K
    NUMA node0 CPU(s):   0-7
    Flags:               fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush mmx fxsr sse sse2 ht syscall nx mmxext fxsr_opt pdpe1gb rdtscp lm constant_tsc rep_good nopl nonstop_tsc cpuid extd_apicid aperfmperf pni pclmulqdq monitor ssse3 fma cx16 sse4_1 sse4_2 movbe popcnt aes xsave avx f16c rdrand lahf_lm cmp_legacy svm extapic cr8_legacy abm sse4a misalignsse 3dnowprefetch osvw skinit wdt tce topoext perfctr_core perfctr_nb bpext perfctr_llc mwaitx hw_pstate sme ssbd sev ibpb vmmcall fsgsbase bmi1 avx2 smep bmi2 rdseed adx smap clflushopt sha_ni xsaveopt xsavec xgetbv1 xsaves clzero irperf xsaveerptr arat npt lbrv svm_lock nrip_save tsc_scale vmcb_clean flushbyasid decodeassists pausefilter pfthreshold avic v_vmsave_vmload vgif overflow_recov succor smca

### [lspci]

`root `[`#`]`lspci -nnk`

    0:00.0 Host bridge [0600]: Advanced Micro Devices, Inc. [AMD] Device [1022:15d0]
        Subsystem: Lenovo Device [17aa:3805]
    00:00.2 IOMMU [0806]: Advanced Micro Devices, Inc. [AMD] Device [1022:15d1]
        Subsystem: Lenovo Device [17aa:3804]
    00:01.0 Host bridge [0600]: Advanced Micro Devices, Inc. [AMD] Family 17h (Models 00h-0fh) PCIe Dummy Host Bridge [1022:1452]
    00:01.2 PCI bridge [0604]: Advanced Micro Devices, Inc. [AMD] Device [1022:15d3]
        Kernel driver in use: pcieport
    00:01.3 PCI bridge [0604]: Advanced Micro Devices, Inc. [AMD] Device [1022:15d3]
        Kernel driver in use: pcieport
    00:08.0 Host bridge [0600]: Advanced Micro Devices, Inc. [AMD] Family 17h (Models 00h-0fh) PCIe Dummy Host Bridge [1022:1452]
    00:08.1 PCI bridge [0604]: Advanced Micro Devices, Inc. [AMD] Device [1022:15db]
        Kernel driver in use: pcieport
    00:08.2 PCI bridge [0604]: Advanced Micro Devices, Inc. [AMD] Device [1022:15dc]
        Kernel driver in use: pcieport
    00:14.0 SMBus [0c05]: Advanced Micro Devices, Inc. [AMD] FCH SMBus Controller [1022:790b] (rev 61)
        Subsystem: Lenovo FCH SMBus Controller [17aa:381e]
        Kernel driver in use: piix4_smbus
        Kernel modules: i2c_piix4, sp5100_tco
    00:14.3 ISA bridge [0601]: Advanced Micro Devices, Inc. [AMD] FCH LPC Bridge [1022:790e] (rev 51)
        Subsystem: Lenovo FCH LPC Bridge [17aa:381f]
    00:18.0 Host bridge [0600]: Advanced Micro Devices, Inc. [AMD] Device [1022:15e8]
    00:18.1 Host bridge [0600]: Advanced Micro Devices, Inc. [AMD] Device [1022:15e9]
    00:18.2 Host bridge [0600]: Advanced Micro Devices, Inc. [AMD] Device [1022:15ea]
    00:18.3 Host bridge [0600]: Advanced Micro Devices, Inc. [AMD] Device [1022:15eb]
        Kernel driver in use: k10temp
        Kernel modules: k10temp
    00:18.4 Host bridge [0600]: Advanced Micro Devices, Inc. [AMD] Device [1022:15ec]
    00:18.5 Host bridge [0600]: Advanced Micro Devices, Inc. [AMD] Device [1022:15ed]
    00:18.6 Host bridge [0600]: Advanced Micro Devices, Inc. [AMD] Device [1022:15ee]
    00:18.7 Host bridge [0600]: Advanced Micro Devices, Inc. [AMD] Device [1022:15ef]
    01:00.0 Network controller [0280]: Qualcomm Atheros QCA9377 802.11ac Wireless Network Adapter [168c:0042] (rev 31)
        Subsystem: Lenovo QCA9377 802.11ac Wireless Network Adapter [17aa:0901]
        Kernel driver in use: ath10k_pci
        Kernel modules: ath10k_pci
    02:00.0 Ethernet controller [0200]: Realtek Semiconductor Co., Ltd. RTL8111/8168/8411 PCI Express Gigabit Ethernet Controller [10ec:8168] (rev 10)
        Subsystem: Lenovo RTL8111/8168/8411 PCI Express Gigabit Ethernet Controller [17aa:38a8]
        Kernel driver in use: r8169
        Kernel modules: r8169
    03:00.0 VGA compatible controller [0300]: Advanced Micro Devices, Inc. [AMD/ATI] Raven Ridge [Radeon Vega Series / Radeon Vega Mobile Series] [1002:15dd] (rev c4)
        DeviceName: Broadcom 5762
        Subsystem: Lenovo Raven Ridge [Radeon Vega Series / Radeon Vega Mobile Series] [17aa:38ef]
        Kernel driver in use: amdgpu
        Kernel modules: amdgpu
    03:00.1 Audio device [0403]: Advanced Micro Devices, Inc. [AMD/ATI] Device [1002:15de]
        Subsystem: Lenovo Device [17aa:3808]
        Kernel driver in use: snd_hda_intel
        Kernel modules: snd_hda_intel
    03:00.2 Encryption controller [1080]: Advanced Micro Devices, Inc. [AMD] Device [1022:15df]
        Subsystem: Lenovo Device [17aa:3809]
    03:00.3 USB controller [0c03]: Advanced Micro Devices, Inc. [AMD] Device [1022:15e0]
        Subsystem: Lenovo Device [17aa:380a]
        Kernel driver in use: xhci_hcd
        Kernel modules: xhci_pci
    03:00.4 USB controller [0c03]: Advanced Micro Devices, Inc. [AMD] Device [1022:15e1]
        Subsystem: Lenovo Device [17aa:380b]
        Kernel driver in use: xhci_hcd
        Kernel modules: xhci_pci
    03:00.6 Audio device [0403]: Advanced Micro Devices, Inc. [AMD] Device [1022:15e3]
        Subsystem: Lenovo Device [17aa:380d]
        Kernel driver in use: snd_hda_intel
        Kernel modules: snd_hda_intel
    04:00.0 SATA controller [0106]: Advanced Micro Devices, Inc. [AMD] FCH SATA Controller [AHCI mode] [1022:7901] (rev 61)
        Subsystem: Advanced Micro Devices, Inc. [AMD] FCH SATA Controller [AHCI mode] [1022:7901]
        Kernel driver in use: ahci

### [lsusb]

`root `[`#`]`lsusb`

    Bus 003 Device 002: ID 0bda:58ea Realtek Semiconductor Corp.
    Bus 002 Device 001: ID 1d6b:0003 Linux Foundation 3.0 root hub
    Bus 004 Device 001: ID 1d6b:0003 Linux Foundation 3.0 root hub
    Bus 001 Device 002: ID 1a40:0101 Terminus Technology Inc. Hub
    Bus 003 Device 003: ID 0cf3:e500 Qualcomm Atheros Communications
    Bus 001 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub
    Bus 003 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub

\

## [Installation]

#### [UEFI updates]

Before removing Windows from the laptop, run the latest UEFI updates from Lenovo, as there is no way to do so once Linux is running.

#### [Legacy boot]

Do not use Compatibility Support Module (CSM) legacy boot services to run Linux, there are some firmware bugs preventing CPU frequency scaling from working.

Use rEFInd USB stick to boot into a UEFI installation media, or, to convert an existing system to EFI boot. This is beyond the scope of the article.

### [Firmware]

The [[[sys-kernel/linux-firmware]](https://packages.gentoo.org/packages/sys-kernel/linux-firmware)[]] package is required as it provides the firmware for the AMDGPU driver and Atheros WiFi adapter.

`root `[`#`]`dmesg`

    [   16.770063] ath10k_pci 0000:01:00.0: firmware ver WLAN.TF.1.0-00002-QCATFSWPZ-5 api 5 features ignore-otp crc32 c3e0d04f

### [Kernel]

As of kernel version 4.19.x, everything is functional including the touchpad. To make the touchpad work, use this [Kernel Configuration Files](https://github.com/mbaraa/ideapad330).

If the \`amdgpu\` module and its firmware are not included in the initramfs, the module may fail to load later due to a race condition and neither X nor virtual terminals will be accessible. This is random, and it may or may not fail. However, adding the amdgpu driver to the initramfs does prevent this issue entirely.

[FILE] **`/etc/dracut.conf.d/drivers.conf`**

    force_drivers+="amdgpu"

Rebuild initramfs using dracut.

### [Configuration]

#### [Compiler settings]

More info is available at:

-   [GCC optimization](https://wiki.gentoo.org/wiki/GCC_optimization "GCC optimization")
-   [MAKEOPTS](https://wiki.gentoo.org/wiki/MAKEOPTS "MAKEOPTS")
-   [EMERGE_DEFAULT_OPTS](https://wiki.gentoo.org/wiki/EMERGE_DEFAULT_OPTS "EMERGE DEFAULT OPTS")

[FILE] **`/etc/portage/make.conf`**

    # O2 for super-safe output
    CFLAGS="-march=znver1 -O2 -pipe"
    CXXFLAGS="$"
    MAKEOPTS="-j4"

#### [Packages settings]

For more info: [CPU_FLAGS_X86](https://wiki.gentoo.org/wiki/CPU_FLAGS_X86 "CPU FLAGS X86")

[FILE] **`/etc/portage/make.conf`**

    # Obtained via cpuinfo2cpuflags-x86
    CPU_FLAGS_X86="aes avx avx2 fma3 mmx mmxext pclmul popcnt sse sse2 sse3 sse4_1 sse4_2 sse4a ssse3"

As of August 2018, your mileage may vary with released versions of Mesa, libdrm, and xf86-video-amdgpu. Adding to `ACCEPT_KEYWORDS` using \`\*\*\` will bring in the latest code that has many unreleased fixes at the expense of random compile failures.

#### [USE flags]

With [AMDGPU](https://wiki.gentoo.org/wiki/AMDGPU "AMDGPU") as video driver and [libinput](https://wiki.gentoo.org/wiki/Libinput "Libinput") as input driver add the USE flag `libinput` and remove any NVIDIA-specific USE flags that may cause issues later.

[FILE] **`/etc/portage/make.conf`**

    VIDEO_CARDS="radeonsi amdgpu"
    # Input devices
    INPUT_DEVICES="libinput"
    # Useflags
    USE="libinput -xvmc -vdpau -cuda"

### [Utils]

#### [Battery charge thresholds]

Use: [[[app-laptop/tpacpi-bat]](https://packages.gentoo.org/packages/app-laptop/tpacpi-bat)[]]. Example econfig and instructions can be found at: [github.com/teleshoes/tpacpi-bat](https://github.com/teleshoes/tpacpi-bat/tree/master/examples).

#### [fan control]

I was unable to make fan control work, but the plumbing is all there and it claims to be supported. Here\'s some tips.

Use: [[[app-laptop/thinkfan]](https://packages.gentoo.org/packages/app-laptop/thinkfan)[]].

[FILE] **`/etc/modprobe.d/thinkpad.conf`**

    options thinkpad_acpi fan_control=1

[FILE] **`/etc/thinkfan.conf`**

    tp_fan /proc/acpi/ibm/fan

    hwmon /sys/class/hwmon/hwmon0/temp1_input
    hwmon /sys/class/hwmon/hwmon1/temp1_input
    hwmon /sys/class/hwmon/hwmon1/temp2_input
    hwmon /sys/class/hwmon/hwmon2/temp1_input

    (0, 0,  55)
    (1, 53, 60)
    (2, 58, 65)
    (3, 63, 70)
    (4, 68, 75)
    (5, 73, 80)
    (6, 78, 85)
    (7, 83, 90)
    (127, 88, 32767)