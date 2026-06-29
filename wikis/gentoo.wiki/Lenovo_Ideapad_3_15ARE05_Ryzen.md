[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=Lenovo_IdeaPad_3_15ARE05&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

**Resources**

[[]][Official Support Page](https://pcsupport.lenovo.com/ee/en/products/laptops-and-netbooks/3-series/ideapad-3-15are05)

[[]][Specifications](https://psref.lenovo.com/syspool/Sys/PDF/IdeaPad/IdeaPad_3_15ARE05/IdeaPad_3_15ARE05_Spec.pdf)

[[]][Specifications (by region)](https://psref.lenovo.com/Product/IdeaPad/IdeaPad_3_15ARE05?tab=model)

[[]][Hardware Maintenance Manual](https://download.lenovo.com/consumer/mobiles_pub/ideapad3_hmm.pdf)

[[]][User Guide](https://download.lenovo.com/consumer/mobiles_pub/ideapad3_ug_202001_en.pdf)

The Lenovo IdeaPad 3 15ARE05 is a mid-range laptop with an [AMD Ryzen 5 4500U](https://www.amd.com/en/products/apu/amd-ryzen-5-4500u) processor and integrated Radeon graphics. There is also an Intel version of this laptop, but this article is written specifically for the AMD version. The Laptop generally works very well with GNU+Linux although there is no official support from Lenovo. This article will guide users throughout installing Gentoo with a graphical environment on the laptop, and showing hardware-specific tweaks that the user can make.

## Contents

-   [[1] [Hardware]](#Hardware)
    -   [[1.1] [Standard]](#Standard)
-   [[2] [Installation]](#Installation)
    -   [[2.1] [Disabling Secure Boot]](#Disabling_Secure_Boot)
    -   [[2.2] [Choosing a secure boot supported installation media]](#Choosing_a_secure_boot_supported_installation_media)
    -   [[2.3] [package.use]](#package.use)
    -   [[2.4] [Kernel]](#Kernel)
-   [[3] [Troubleshooting]](#Troubleshooting)
    -   [[3.1] [Brighness control bug after waking from suspend]](#Brighness_control_bug_after_waking_from_suspend)

## [Hardware]

### [Standard]

  --------------------- ------------------------------------------------------ ------------- ------------------------ ------------------ ---------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Device                Make/model                                             Status        Vendor ID / Product ID   Kernel driver(s)   Kernel version   Notes
  CPU                   AMD Ryzen 5 4500U                                      Works         N/A                      N/A                4.19+
  GPU                   AMD Renoir APU                                         Works         N/A                      N/A                4.19+            Does work without proprietary firmware, except multi-monitor and brighness control doesn\'t work.
  Webcam                IMC Networks Integrated Camera                         Works         N/A                      N/A                4.19+            Works out of the box.
  Wireless Adapter      Realtek RTL8822CE                                      Works         N/A                      N/A                4.19+            Works, but requires proprietary [[[sys-kernel/linux-firmware]](https://packages.gentoo.org/packages/sys-kernel/linux-firmware)[]]. It is replacable.
  Touchpad              N/A                                                    Works         N/A                      N/A                5.12.6+          Does not work on kernel versions older than 5.12.6. See [bug report](https://bugzilla.kernel.org/show_bug.cgi?id=207759).
  Keyboard              N/A                                                    Works         N/A                      N/A                4.19+            Works out of the box.
  Sound Card            AMD Raven/Renoir Family 17h Audio Processor (rev 01)   Works         N/A                      N/A                4.19+            Works well with minor issues, as described below.
  Display               AMD Raven/Renoir Family 17h Audio Processor (rev 01)   Works         N/A                      N/A                4.19+            Works with minor (harmless) brightness control issues.
  Fingerprint scanner   N/A                                                    Not tested    N/A                      N/A                N/A
  --------------------- ------------------------------------------------------ ------------- ------------------------ ------------------ ---------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

`user `[`$`]`lscpu`

    Architecture:                    x86_64
    CPU op-mode(s):                  32-bit, 64-bit
    Address sizes:                   48 bits physical, 48 bits virtual
    Byte Order:                      Little Endian
    CPU(s):                          6
    On-line CPU(s) list:             0-5
    Vendor ID:                       AuthenticAMD
    BIOS Vendor ID:                  Advanced Micro Devices, Inc.
    Model name:                      AMD Ryzen 5 4500U with Radeon Graphics
    BIOS Model name:                 AMD Ryzen 5 4500U with Radeon Graphics
    CPU family:                      23
    Model:                           96
    Thread(s) per core:              1
    Core(s) per socket:              6
    Socket(s):                       1
    Stepping:                        1
    Frequency boost:                 enabled
    CPU max MHz:                     2375.0000
    CPU min MHz:                     1400.0000
    BogoMIPS:                        4742.49
    Flags:                           fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush mmx fxsr sse sse2 ht syscall nx mmxext fxsr_opt pdpe1gb rdtscp lm constant_tsc rep_good nopl nonstop_tsc cpuid extd_apicid aperfmperf rapl pni pclmulqdq monitor ssse3 fma cx16 sse4_1 sse4_2 movbe popcnt aes xsave avx f16c rdrand lahf_lm cmp_legacy svm extapic cr8_legacy abm sse4a misalignsse 3dnowprefetch osvw ibs skinit wdt tce topoext perfctr_core perfctr_nb bpext perfctr_llc mwaitx cpb cat_l3 cdp_l3 hw_pstate ssbd mba ibrs ibpb stibp vmmcall fsgsbase bmi1 avx2 smep bmi2 cqm rdt_a rdseed adx smap clflushopt clwb sha_ni xsaveopt xsavec xgetbv1 xsaves cqm_llc cqm_occup_llc cqm_mbm_total cqm_mbm_local clzero irperf xsaveerptr rdpru wbnoinvd arat npt lbrv svm_lock nrip_save tsc_scale vmcb_clean flushbyasid decodeassists pausefilter pfthreshold avic v_vmsave_vmload vgif v_spec_ctrl umip rdpid overflow_recov succor smca
    Virtualization:                  AMD-V
    L1d cache:                       192 KiB (6 instances)
    L1i cache:                       192 KiB (6 instances)
    L2 cache:                        3 MiB (6 instances)
    L3 cache:                        8 MiB (2 instances)
    NUMA node(s):                    1
    NUMA node0 CPU(s):               0-5
    Vulnerability Itlb multihit:     Not affected
    Vulnerability L1tf:              Not affected
    Vulnerability Mds:               Not affected
    Vulnerability Meltdown:          Not affected
    Vulnerability Spec store bypass: Mitigation; Speculative Store Bypass disabled via prctl and seccomp
    Vulnerability Spectre v1:        Mitigation; usercopy/swapgs barriers and __user pointer sanitization
    Vulnerability Spectre v2:        Mitigation; Full AMD retpoline, IBPB conditional, IBRS_FW, STIBP disabled, RSB filling
    Vulnerability Srbds:             Not affected
    Vulnerability Tsx async abort:   Not affected

`user `[`$`]`lspci`

    00:00.0 Host bridge: Advanced Micro Devices, Inc. [AMD] Renoir/Cezanne Root Complex
    00:00.2 IOMMU: Advanced Micro Devices, Inc. [AMD] Renoir/Cezanne IOMMU
    00:01.0 Host bridge: Advanced Micro Devices, Inc. [AMD] Renoir PCIe Dummy Host Bridge
    00:02.0 Host bridge: Advanced Micro Devices, Inc. [AMD] Renoir PCIe Dummy Host Bridge
    00:02.2 PCI bridge: Advanced Micro Devices, Inc. [AMD] Renoir/Cezanne PCIe GPP Bridge
    00:02.4 PCI bridge: Advanced Micro Devices, Inc. [AMD] Renoir/Cezanne PCIe GPP Bridge
    00:08.0 Host bridge: Advanced Micro Devices, Inc. [AMD] Renoir PCIe Dummy Host Bridge
    00:08.1 PCI bridge: Advanced Micro Devices, Inc. [AMD] Renoir Internal PCIe GPP Bridge to Bus
    00:08.2 PCI bridge: Advanced Micro Devices, Inc. [AMD] Renoir Internal PCIe GPP Bridge to Bus
    00:14.0 SMBus: Advanced Micro Devices, Inc. [AMD] FCH SMBus Controller (rev 51)
    00:14.3 ISA bridge: Advanced Micro Devices, Inc. [AMD] FCH LPC Bridge (rev 51)
    00:18.0 Host bridge: Advanced Micro Devices, Inc. [AMD] Renoir Device 24: Function 0
    00:18.1 Host bridge: Advanced Micro Devices, Inc. [AMD] Renoir Device 24: Function 1
    00:18.2 Host bridge: Advanced Micro Devices, Inc. [AMD] Renoir Device 24: Function 2
    00:18.3 Host bridge: Advanced Micro Devices, Inc. [AMD] Renoir Device 24: Function 3
    00:18.4 Host bridge: Advanced Micro Devices, Inc. [AMD] Renoir Device 24: Function 4
    00:18.5 Host bridge: Advanced Micro Devices, Inc. [AMD] Renoir Device 24: Function 5
    00:18.6 Host bridge: Advanced Micro Devices, Inc. [AMD] Renoir Device 24: Function 6
    00:18.7 Host bridge: Advanced Micro Devices, Inc. [AMD] Renoir Device 24: Function 7
    01:00.0 Network controller: Realtek Semiconductor Co., Ltd. RTL8822CE 802.11ac PCIe Wireless Network Adapter
    02:00.0 Non-Volatile memory controller: SK hynix BC511
    03:00.0 VGA compatible controller: Advanced Micro Devices, Inc. [AMD/ATI] Renoir (rev c3)
    03:00.1 Audio device: Advanced Micro Devices, Inc. [AMD/ATI] Renoir Radeon High Definition Audio Controller
    03:00.2 Encryption controller: Advanced Micro Devices, Inc. [AMD] Family 17h (Models 10h-1fh) Platform Security Processor
    03:00.3 USB controller: Advanced Micro Devices, Inc. [AMD] Renoir/Cezanne USB 3.1
    03:00.4 USB controller: Advanced Micro Devices, Inc. [AMD] Renoir/Cezanne USB 3.1
    03:00.5 Multimedia controller: Advanced Micro Devices, Inc. [AMD] Raven/Raven2/FireFlight/Renoir Audio Processor (rev 01)
    03:00.6 Audio device: Advanced Micro Devices, Inc. [AMD] Family 17h (Models 10h-1fh) HD Audio Controller
    04:00.0 SATA controller: Advanced Micro Devices, Inc. [AMD] FCH SATA Controller [AHCI mode] (rev 81)
    04:00.1 SATA controller: Advanced Micro Devices, Inc. [AMD] FCH SATA Controller [AHCI mode] (rev 81)

`user `[`$`]`lsusb`

    Bus 004 Device 001: ID 1d6b:0003 Linux Foundation 3.0 root hub
    Bus 003 Device 002: ID 0bda:c123 Realtek Semiconductor Corp. Bluetooth Radio
    Bus 003 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub
    Bus 002 Device 001: ID 1d6b:0003 Linux Foundation 3.0 root hub
    Bus 001 Device 002: ID 13d3:5a08 IMC Networks Integrated Camera
    Bus 001 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub

## [Installation]

### [Disabling Secure Boot]

If the user will use the official [Gentoo Installation Media](https://www.gentoo.org/downloads/) (or other installation media that is not supported by secure boot), they will have to disable [secure boot](https://en.wikipedia.org/wiki/Unified_Extensible_Firmware_Interface#Secure_Boot), which is a protocol that is supposed to secure the boot process of the system by preventing the [UEFI](https://en.wikipedia.org/wiki/Unified_Extensible_Firmware_Interface) to load [bootloaders](https://en.wikipedia.org/wiki/Bootloader) that are not signed by Microsoft.

To disable secure boot the user must go to the UEFI settings by pressing F2 before the computer boots.

In UEFI \| **Security \> AMD Platform Security Processor \> \[Disabled\]**

### [Choosing a secure boot supported installation media]

The user may want to choose to boot with secure boot instead of disabling it. You can install Gentoo from numerous other GNU+Linux distributions\' installation media. Those that are supported by secure boot are:

-   [Ubuntu](https://en.wikipedia.org/wiki/Ubuntu)
-   [Debian GNU/Linux](https://en.wikipedia.org/wiki/Debian)
-   [Fedora](https://en.wikipedia.org/wiki/Fedora_Linux)
-   [OpenSUSE](https://en.wikipedia.org/wiki/OpenSUSE)
-   [Red Hat Enterprise Linux](https://en.wikipedia.org/wiki/Red_Hat_Enterprise_Linux)

### [package.use]

[FILE] **`/etc/portage/package.use`**

    MAKEOPTS="-j6"

[FILE] **`/etc/portage/package.use/00video`**

    */* VIDEO_CARDS: -* amdgpu radeonsi

[FILE] **`/etc/portage/package.use/00input`**

    */* INPUT_DEVICES: libinput synaptics

### [Kernel]

**WiFi adapter**

[KERNEL] **Wireless Networking (With the shipped Realtek WiFi card)**

    Device Drivers  --->
        [*] Network device support  --->
            [*] Wireless Lan --->
                 [*] Realtek devices
                 <*> Realtek rtlwifi family of devices --->

**Touchpad**

[KERNEL] **elants-i2c**

    Device Drivers  --->
        [*] Network device support  --->
             Input device support --->
                [*] Touchscreens --->
                   [*] Elan eKTF2127 I2C touchscreen
                   [*] Elan eKTH I2C touchscreen

[KERNEL] **Enable PS/2 mice**

    Device Drivers  --->
        [*] Network device support  --->
             Input device support --->
              [*] Mice --->
                  <*> PS/2 mouse
                  [*] Elantech PS/2 protocol extension
                  <*> Synaptics I2C Touchpad support

See [synaptics](https://wiki.gentoo.org/wiki/Synaptics "Synaptics") for more info.

**Keyboard**

[KERNEL] **Enable keyboard support**

    Device Drivers  --->
        [*] Network device support  --->
             Input device support --->
               [*] Keyboards --->

**Graphical Processing Unit**

[KERNEL] **Enable AMD GPU support**

    Device Drivers  --->
         [*] Graphics support --->
             (1) Maximum number of GPUs
             [*] AMD GPU

## [Troubleshooting]

### [Brighness control bug after waking from suspend]

*This issue is yet to be solved.*

There is a strange brightness control bug that causes the screen go totally black when pressing the *Brightness down function key* (or the *F11* key) until the user tries to increase the brightness again. This happens only after waking from suspend. It is a harmless bug.