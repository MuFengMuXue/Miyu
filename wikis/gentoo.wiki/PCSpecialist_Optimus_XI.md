**Resources**

[[]][Home](https://www.pcspecialist.fr/ordinateurs-portables/optimusXI-15/)

## Contents

-   [[1] [Hardware information]](#Hardware_information)
    -   [[1.1] [lscpu]](#lscpu)
    -   [[1.2] [lspci]](#lspci)
    -   [[1.3] [lsusb]](#lsusb)
-   [[2] [Installation]](#Installation)
    -   [[2.1] [Kernel]](#Kernel)
        -   [[2.1.1] [EFI stub]](#EFI_stub)
        -   [[2.1.2] [AHCI]](#AHCI)
        -   [[2.1.3] [SSD drive]](#SSD_drive)
        -   [[2.1.4] [Ethernet]](#Ethernet)
        -   [[2.1.5] [WiFi]](#WiFi)
        -   [[2.1.6] [Sound]](#Sound)
        -   [[2.1.7] [USB]](#USB)
        -   [[2.1.8] [SD card]](#SD_card)
        -   [[2.1.9] [Webcam]](#Webcam)
        -   [[2.1.10] [Keyboard backlight]](#Keyboard_backlight)
    -   [[2.2] [Optimus graphics]](#Optimus_graphics)
        -   [[2.2.1] [Proprietary NVIDIA driver]](#Proprietary_NVIDIA_driver)
        -   [[2.2.2] [Nouveau]](#Nouveau)

## [Hardware information]

### [lscpu]

`root `[`#`]`lscpu`

    Architecture:                    x86_64
    CPU op-mode(s):                  32-bit, 64-bit
    Byte Order:                      Little Endian
    Address sizes:                   39 bits physical, 48 bits virtual
    CPU(s):                          12
    On-line CPU(s) list:             0-11
    Thread(s) per core:              2
    Core(s) per socket:              6
    Socket(s):                       1
    NUMA node(s):                    1
    Vendor ID:                       GenuineIntel
    CPU family:                      6
    Model:                           165
    Model name:                      Intel(R) Core(TM) i7-10750H CPU @ 2.60GHz
    Stepping:                        2
    CPU MHz:                         900.213
    CPU max MHz:                     5000.0000
    CPU min MHz:                     800.0000
    BogoMIPS:                        5199.98
    Virtualization:                  VT-x
    L1d cache:                       192 KiB
    L1i cache:                       192 KiB
    L2 cache:                        1.5 MiB
    L3 cache:                        12 MiB
    NUMA node0 CPU(s):               0-11
    Vulnerability Itlb multihit:     Processor vulnerable
    Vulnerability L1tf:              Not affected
    Vulnerability Mds:               Not affected
    Vulnerability Meltdown:          Not affected
    Vulnerability Spec store bypass: Mitigation; Speculative Store Bypass disabled via prctl and seccomp
    Vulnerability Spectre v1:        Mitigation; usercopy/swapgs barriers and __user pointer sanitization
    Vulnerability Spectre v2:        Mitigation; Enhanced IBRS, IBPB conditional, RSB filling
    Vulnerability Srbds:             Not affected
    Vulnerability Tsx async abort:   Not affected
    Flags:                           fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush dts acpi mmx fxsr sse sse2 ss ht tm pbe syscall nx pdpe1gb rdtscp lm constant_tsc art arch_perfmon pebs bts rep_good nopl xtopology nonstop_tsc cpuid aperfmperf pni pclmulqdq dtes64 monitor ds_cpl vmx est tm2 ssse3 sdbg fma cx16 xtpr pdcm pcid sse4_1 sse4_2 x2apic movbe popcnt tsc_deadline_timer aes xsave avx f16c rdrand lahf_lm abm 3dnowprefetch cpuid_fault epb invpcid_single ssbd ibrs ibpb stibp ibrs_enhanced tpr_shadow vnmi flexpriority ept vpid ept_ad fsgsbase tsc_adjust bmi1 avx2 smep bmi2 erms invpcid mpx rdseed adx smap clflushopt intel_pt xsaveopt xsavec xgetbv1 xsaves dtherm ida arat pln pts hwp hwp_notify hwp_act_window hwp_epp pku ospke md_clear flush_l1d arch_capabilities

### [lspci]

`root `[`#`]`lspci -nnk`

    00:00.0 Host bridge [0600]: Intel Corporation Device [8086:9b54] (rev 02)
        Subsystem: CLEVO/KAPOK Computer Device [1558:8520]
    00:01.0 PCI bridge [0604]: Intel Corporation Xeon E3-1200 v5/E3-1500 v5/6th Gen Core Processor PCIe Controller (x16) [8086:1901] (rev 02)
        Kernel driver in use: pcieport
    00:02.0 VGA compatible controller [0300]: Intel Corporation Device [8086:9bc4] (rev 05)
        Subsystem: CLEVO/KAPOK Computer Device [1558:8520]
        Kernel driver in use: i915
    00:12.0 Signal processing controller [1180]: Intel Corporation Device [8086:06f9]
        Subsystem: CLEVO/KAPOK Computer Device [1558:8520]
    00:14.0 USB controller [0c03]: Intel Corporation Device [8086:06ed]
        Subsystem: CLEVO/KAPOK Computer Device [1558:8520]
        Kernel driver in use: xhci_hcd
    00:14.2 RAM memory [0500]: Intel Corporation Device [8086:06ef]
        Subsystem: CLEVO/KAPOK Computer Device [1558:8520]
    00:15.0 Serial bus controller [0c80]: Intel Corporation Device [8086:06e8]
        Subsystem: CLEVO/KAPOK Computer Device [1558:8520]
    00:15.1 Serial bus controller [0c80]: Intel Corporation Device [8086:06e9]
        Subsystem: CLEVO/KAPOK Computer Device [1558:8520]
    00:16.0 Communication controller [0780]: Intel Corporation Device [8086:06e0]
        Subsystem: CLEVO/KAPOK Computer Device [1558:8520]
    00:17.0 SATA controller [0106]: Intel Corporation Device [8086:06d3]
        Subsystem: CLEVO/KAPOK Computer Device [1558:8520]
        Kernel driver in use: ahci
    00:1d.0 PCI bridge [0604]: Intel Corporation Device [8086:06b0] (rev f0)
        Kernel driver in use: pcieport
    00:1d.5 PCI bridge [0604]: Intel Corporation Device [8086:06b5] (rev f0)
        Kernel driver in use: pcieport
    00:1d.6 PCI bridge [0604]: Intel Corporation Device [8086:06b6] (rev f0)
        Kernel driver in use: pcieport
    00:1f.0 ISA bridge [0601]: Intel Corporation Device [8086:068d]
        Subsystem: CLEVO/KAPOK Computer Device [1558:8520]
    00:1f.3 Audio device [0403]: Intel Corporation Device [8086:06c8]
        Subsystem: CLEVO/KAPOK Computer Device [1558:8520]
        Kernel driver in use: snd_hda_intel
    00:1f.4 SMBus [0c05]: Intel Corporation Device [8086:06a3]
        Subsystem: CLEVO/KAPOK Computer Device [1558:8520]
    00:1f.5 Serial bus controller [0c80]: Intel Corporation Device [8086:06a4]
        Subsystem: CLEVO/KAPOK Computer Device [1558:8520]
    01:00.0 VGA compatible controller [0300]: NVIDIA Corporation TU116M [GeForce GTX 1660 Ti Mobile] [10de:2191] (rev a1)
        Subsystem: CLEVO/KAPOK Computer TU116M [GeForce GTX 1660 Ti Mobile] [1558:8520]
        Kernel driver in use: nvidia
        Kernel modules: nvidia_drm, nvidia
    01:00.1 Audio device [0403]: NVIDIA Corporation TU116 High Definition Audio Controller [10de:1aeb] (rev a1)
        Subsystem: NVIDIA Corporation TU116 High Definition Audio Controller [10de:0000]
        Kernel driver in use: snd_hda_intel
    01:00.2 USB controller [0c03]: NVIDIA Corporation Device [10de:1aec] (rev a1)
        Subsystem: NVIDIA Corporation Device [10de:0000]
        Kernel driver in use: xhci_hcd
    01:00.3 Serial bus controller [0c80]: NVIDIA Corporation TU116 [GeForce GTX 1650 SUPER] [10de:1aed] (rev a1)
        Subsystem: NVIDIA Corporation TU116 [GeForce GTX 1650 SUPER] [10de:0000]
    06:00.0 Non-Volatile memory controller [0108]: Realtek Semiconductor Co., Ltd. Device [10ec:5763] (rev 01)
        Subsystem: Realtek Semiconductor Co., Ltd. Device [10ec:5763]
        Kernel driver in use: nvme
    07:00.0 Network controller [0280]: Intel Corporation Wi-Fi 6 AX200 [8086:2723] (rev 1a)
        Subsystem: Intel Corporation Wi-Fi 6 AX200 [8086:0080]
        Kernel driver in use: iwlwifi
        Kernel modules: iwlwifi
    08:00.0 Unassigned class [ff00]: Realtek Semiconductor Co., Ltd. RTL8411B PCI Express Card Reader [10ec:5287] (rev 01)
        Subsystem: CLEVO/KAPOK Computer RTL8411B PCI Express Card Reader [1558:8520]
        Kernel driver in use: rtsx_pci
    08:00.1 Ethernet controller [0200]: Realtek Semiconductor Co., Ltd. RTL8111/8168/8411 PCI Express Gigabit Ethernet Controller [10ec:8168] (rev 12)
        Subsystem: CLEVO/KAPOK Computer RTL8111/8168/8411 PCI Express Gigabit Ethernet Controller [1558:8520]
        Kernel driver in use: r8169

### [lsusb]

`root `[`#`]`lsusb`

    Bus 002 Device 001: ID 1d6b:0003 Linux Foundation 3.0 root hub
    Bus 001 Device 004: ID 5986:9102 Acer, Inc BisonCam,NB Pro
    Bus 004 Device 001: ID 1d6b:0003 Linux Foundation 3.0 root hub
    Bus 003 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub
    Bus 001 Device 003: ID 8087:0029 Intel Corp.
    Bus 001 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub

## [Installation]

### [Kernel]

#### [EFI stub]

The kernel can be [booted with EFI stub](https://wiki.gentoo.org/wiki/EFI_stub "EFI stub"), however the path has to be [/EFI/Boot/bootx64.efi]. I haven\'t been able to register custom entries with [efibootmgr](https://wiki.gentoo.org/wiki/Efibootmgr "Efibootmgr") (the UEFI firmware seems to reset the entries).

#### [AHCI]

AHCI has to be enabled.

[KERNEL] **Based on 5.4.48:**

    Device Drivers  --->
      <*> Serial ATA and Parallel ATA drivers (libata)  --->
        <*>   AHCI SATA support

#### [SSD drive]

If you have a SSD drive, enable [NVMe](https://wiki.gentoo.org/wiki/NVMe "NVMe") support:

[KERNEL] **Based on 5.4.48:**

    Device Drivers  --->
      NVME Support  --->
        <*> NVM Express block device

#### [Ethernet]

Enable r8169:

[KERNEL] **Based on 5.4.48:**

    Device Drivers  --->
      [*] Network device support  --->
      [*]   Ethernet driver support  --->
        [*]   Realtek devices
        <*>     Realtek 8169/8168/8101/8125 ethernet support

#### [WiFi]

The driver is [iwlwifi](https://wiki.gentoo.org/wiki/Iwlwifi "Iwlwifi"):

[KERNEL] **Based on 5.4.48:**

    Device Drivers  --->
      [*] Network device support  --->
      [*]   Wireless LAN  --->
        <M>   Intel Wireless WiFi Next Gen AGN - Wireless-N/Advanced-N/Ultimate-N (iwlwifi)
        <M>     Intel Wireless WiFi DVM Firmware support
        <M>     Intel Wireless WiFi MVM Firmware support

#### [Sound]

Enable snd_hda_intel:

[KERNEL] **Based on 5.4.48:**

    Device Drivers  --->
      <*> Sound card support  --->
        <*>   Advanced Linux Sound Architecture  --->
          HD-Audio  --->
            <*> HD Audio PCI
            <*> Build HDMI/DisplayPort HD-audio codec support
            <*> Enable generic HD-audio codec parser

#### [USB]

[KERNEL] **Based on 5.4.48:**

    Device Drivers  --->
      [*] USB support  --->
        <*>   xHCI HCD (USB 3.0) support
        <*>   EHCI HCD (USB 2.0) support

#### [SD card]

Enable rtsx_pci:

[KERNEL] **Based on 5.4.48:**

    Device Drivers  --->
      Misc devices  --->
        <*> Realtek PCI-E card reader
      <*> MMC/SD/SDIO card support  --->
        <*> Realtek PCI-E SD/MMC Card Interface Driver

#### [Webcam]

[KERNEL] **Based on 5.4.48:**

    Device Drivers  --->
      <*> Multimedia support  --->
        [*]   Cameras/video grabbers support
        [*]   Media USB Adapters  --->
          <*>   USB Video Class (UVC)
          [*]     UVC input events device support

#### [Keyboard backlight]

First, enable WMI in the kernel:

[KERNEL] **Based on 5.4.48:**

    Device Drivers  --->
      [*] X86 Platform Specific Device Drivers  --->
        <*>   WMI
        <*>     WMI embedded Binary MOF driver

Then, install the kernel module [[[app-laptop/tuxedo-keyboard]](https://packages.gentoo.org/packages/app-laptop/tuxedo-keyboard)[]]. This will make the keyboard backlight Fn keys work, and allow configuration via [/sys/devices/platform/tuxedo_keyboard].

### [Optimus graphics]

#### [Proprietary NVIDIA driver]

With the proprietary NVIDIA driver, one can use either [bumblebee](https://wiki.gentoo.org/wiki/NVIDIA/Bumblebee "NVIDIA/Bumblebee") or [PRIME render offload](https://download.nvidia.com/XFree86/Linux-x86_64/435.17/README/primerenderoffload.html).

For the bumblebee method, bbswitch has to be disabled, as it will freeze the system. To do so, set `PMMethod=none` in your [/etc/bumblebee/bumblebee.conf]. Note that this will disable powering off the card when unused; I haven\'t been able to make linux PM work.

For PRIME render offload, make sure that the `libglvnd` is enabled and `nvidia` is in VIDEO_CARDS, and add `options nvidia_drm modeset=1` to [/etc/modprobe.d/nvidia.conf]. To enable power management in the NVIDIA driver, add `NVreg_DynamicPowerManagement=0x02` in the module options in [/etc/modprobe.d/nvidia.conf]. This is described in the [driver documentation](https://download.nvidia.com/XFree86/Linux-x86_64/435.17/README/dynamicpowermanagement.html).

#### [Nouveau]

Untested.