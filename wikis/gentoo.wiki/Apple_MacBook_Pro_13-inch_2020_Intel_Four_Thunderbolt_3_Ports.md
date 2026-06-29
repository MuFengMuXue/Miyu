**Resources**

[[]][Official Support Page](https://support.apple.com/en-us/111339)

[[]][GitHub](https://github.com/t2linux/linux-t2-patches)

[][t2linux documentation for T2 Intel Macs](https://wiki.t2linux.org/guides/postinstall/)

The Apple MacBook Pro 13-inch (2020, Four Thunderbolt 3 ports) is an Intel-based laptop with the Model Identifier MacBookPro16,2. It is the final MacBook Pro which was released before the switch to Apple silicon.

There are very similar models with the identifiers MacBookPro16,1...16,4 and most information here applies to the others as well.

## Contents

-   [[1] [Hardware]](#Hardware)
    -   [[1.1] [Components]](#Components)
    -   [[1.2] [ACPI / Power management]](#ACPI_.2F_Power_management)
    -   [[1.3] [Extra hardware information]](#Extra_hardware_information)
-   [[2] [Configuration]](#Configuration)
    -   [[2.1] [CPU flags]](#CPU_flags)
-   [[3] [Installation]](#Installation)
    -   [[3.1] [Preparation]](#Preparation)
    -   [[3.2] [Kernel]](#Kernel)
    -   [[3.3] [Wifi]](#Wifi)
    -   [[3.4] [Touchbar]](#Touchbar)
-   [[4] [Troubleshooting]](#Troubleshooting)
    -   [[4.1] [Framebuffer]](#Framebuffer)
    -   [[4.2] [Touchbar]](#Touchbar_2)

## [Hardware]

A number of components are not supported by the mainline kernel (as of 6.9). Out-of-tree patches need to be applied to use these components.

### [Components]

  ---------------------- ---------------------------------------------------- -------------- ------------------------------ ------------------------------------------------------ -------------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Device                 Make/model                                           Status         Vendor ID / Product ID         Kernel driver(s)                                       Kernel version       Notes
  CPU                    Intel Core i5-1038G7                                 Works          N/A                            N/A                                                    6.9.4
  iGPU                   Intel Iris Plus Graphics G7                          Works          PCI 8086:8a53                  [i915](https://wiki.gentoo.org/wiki/Intel "Intel")     6.9.4
  GPIO                   Intel GPIO Pin Controller                            Works          N/A                            pinctrl_intel                                          6.9.4
  I2C/SMBus Controller   Intel SMBus Controller                               Works          PCI 8086:38c8                  i2c_i801                                               6.9.4
  SPI Controller         Intel Ice Lake SPI Controller                        Works          PCI 8086:38a4                  spi_intel_pci                                          6.9.4
  LPSS Controller        Intel Low Power Subsystem Controller                 Works          PCI 8086:38a8                  intel_lpss_acpi, intel_lpss_pci                        6.9.4                required for Bluetooth
  Serial Controller      Designware Serial Controller                         Works          ?                              8250_dw                                                6.9.4                required for Bluetooth
  VHCI bridge            Apple T2 Bridge Controller                           Partial        PCI 106b:1801                  apple-bce                                              out of tree driver   requires that the IOMMU is enabled; required for keyboard, trackpad, and the Apple Audio device
  Secure element         Apple T2 Secure Enclave Processor                    Unsupported    PCI 106b:1802
  NVMe                   Apple ANS2 NVMe Controller                           Works          PCI 106b:2005                  nvme                                                   6.9.4
  Audio                  Intel Corporation HD Audio device                    Works          PCI 8086:7270                  snd_hda_intel, snd_soc_avs, snd_sof_pci_intel_icl      6.9.4                for HDMI/DisplayPort audio
  Audio                  Apple Audio Device                                   Partial        PCI 106b:1803                  apple-bce                                              out of tree driver   only playback, no recording
  Wireless LAN           Broadcom BCM4364 802.11ac Wireless Network Adapter   Works          PCI 14e4:4464                  brcmfmac                                               6.9.4                needs firmware that is not in linux-firmware.git, see [#Wifi](#Wifi)
  Bluetooth              Broadcom BCM4364 Bluetooth                           Works          PCI 14e4:4464                  hci_uart, hci_uart_bcm                                 6.9.4
  Thunderbolt 3          Intel Ice Lake Thunderbolt NHI                       Works          PCI 8086:8a17, PCI 8086:8a0d   thunderbolt                                            6.9.4                also requires that CONFIG_HOTPLUG_PCI_PCIE is enabled
  USB 3                  Intel Ice Lake USB Controller                        Works          PCI 8086:38ed                  xhci_hcd                                               6.9.4
  Keyboard               Apple Magic Keyboard                                 Works          USB 05ac:027e                  usbhid                                                 6.9.4
  Touchpad               Apple Magic Touchpad                                 Works          USB 05ac:027e                  bcm5974                                                6.9.4
  Touchbar               Apple Touchbar                                       Works          USB 05ac:8302, USB 05ac:8102   appletbdrm, hid_appletb_bl, hid_appletb_kbd            6.15.0               Controlled by [[[app-laptop/tiny-dfr]](https://packages.gentoo.org/packages/app-laptop/tiny-dfr)[]], see [#Touchbar](#Touchbar)
  Fingerprint sensor     Apple Touch ID sensor                                Unsupported    ?
  Webcam                 Apple FaceTime HD Camera                             Works          USB 05ac:8514                  uvcvideo                                               6.9.4
  Hardware Monitoring    various                                              Works                                         acpi_battery, applesmc, coretemp, int340x, nvme, sbs   6.9.4                applesmc needs out of tree patches
  Ambient light sensor   Apple Ambient Light Sensor                           Unknown        USB 05ac:8262                  hid_sensor_hub
  ---------------------- ---------------------------------------------------- -------------- ------------------------------ ------------------------------------------------------ -------------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### [][ACPI / Power management]

  ------------------------------ ------------- --------------------------- -------------------- ----------------- -------
  Function                       Status        Kernel driver(s)            Kernel version       BIOS version      Notes
  CPU frequency scaling          Works         intel_pstate, intel_rapl    6.9.4                2022.100.22.0.0
  GPU Powersaving                Not tested    i915
  PCIe Power Management (ASPM)   Not tested
  USB Type C Power Delivery      Works                                     6.9.4                2022.100.22.0.0
  Battery                        Works         sbs                         6.9.4                2022.100.22.0.0
  Suspend to RAM                 Not tested
  Suspend to disk (hibernate)    Not tested
  Display backlight control      Works         backlight_apple             6.9.4                2022.100.22.0.0
  Keyboard backlight control     Works         hid_apple_magic_backlight   out of tree driver   2022.100.22.0.0
  ------------------------------ ------------- --------------------------- -------------------- ----------------- -------

### [Extra hardware information]

`root `[`#`]`lspci -nnk`

    00:00.0 Host bridge [0600]: Intel Corporation Ice Lake Processor Host Bridge/DRAM Registers [8086:8a14] (rev 03)
            DeviceName: SATA
            Subsystem: Intel Corporation Device [8086:7270]
    00:02.0 VGA compatible controller [0300]: Intel Corporation Iris Plus Graphics G7 [8086:8a53] (rev 07)
            Subsystem: Apple Inc. Device [106b:0211]
            Kernel driver in use: i915
            Kernel modules: i915
    00:04.0 Signal processing controller [1180]: Intel Corporation Processor Power and Thermal Controller [8086:8a03] (rev 03)
            Subsystem: Intel Corporation Device [8086:7270]
            Kernel modules: processor_thermal_device_pci_legacy
    00:07.0 PCI bridge [0604]: Intel Corporation Ice Lake Thunderbolt 3 PCI Express Root Port #0 [8086:8a1d] (rev 03)
            Kernel driver in use: pcieport
    00:07.1 PCI bridge [0604]: Intel Corporation Ice Lake Thunderbolt 3 PCI Express Root Port #1 [8086:8a1f] (rev 03)
            Kernel driver in use: pcieport
    00:07.2 PCI bridge [0604]: Intel Corporation Ice Lake Thunderbolt 3 PCI Express Root Port #2 [8086:8a21] (rev 03)
            Kernel driver in use: pcieport
    00:07.3 PCI bridge [0604]: Intel Corporation Ice Lake Thunderbolt 3 PCI Express Root Port #3 [8086:8a23] (rev 03)
            Kernel driver in use: pcieport
    00:0d.0 USB controller [0c03]: Intel Corporation Ice Lake Thunderbolt 3 USB Controller [8086:8a13] (rev 03)
            Kernel driver in use: xhci_hcd
    00:0d.2 System peripheral [0880]: Intel Corporation Ice Lake Thunderbolt 3 NHI #0 [8086:8a17] (rev 03)
            Kernel driver in use: thunderbolt
    00:0d.3 System peripheral [0880]: Intel Corporation Ice Lake Thunderbolt 3 NHI #1 [8086:8a0d] (rev 03)
            Kernel driver in use: thunderbolt
    00:14.0 USB controller [0c03]: Intel Corporation Device [8086:38ed] (rev 10)
            Subsystem: Intel Corporation Device [8086:7270]
            Kernel driver in use: xhci_hcd
    00:14.2 RAM memory [0500]: Intel Corporation Device [8086:38ef] (rev 10)
    00:16.0 Communication controller [0780]: Intel Corporation Ice Lake Management Engine Interface [8086:38e0] (rev 10)
            Subsystem: Intel Corporation Device [8086:7270]
            Kernel driver in use: mei_me
            Kernel modules: mei_me
    00:1c.0 PCI bridge [0604]: Intel Corporation Device [8086:38b8] (rev 10)
            Subsystem: Intel Corporation Device [8086:7270]
            Kernel driver in use: pcieport
    00:1c.4 PCI bridge [0604]: Intel Corporation Device [8086:38bc] (rev 10)
            Subsystem: Intel Corporation Device [8086:7270]
            Kernel driver in use: pcieport
    00:1e.0 Communication controller [0780]: Intel Corporation Device [8086:38a8] (rev 10)
            Subsystem: Intel Corporation Device [8086:7270]
            Kernel driver in use: intel-lpss
    00:1f.0 ISA bridge [0601]: Intel Corporation Ice Lake LPC Controller [8086:3882] (rev 10)
            Subsystem: Intel Corporation Device [8086:7270]
    00:1f.3 Audio device [0403]: Intel Corporation Device [8086:38c8] (rev 10)
            Subsystem: Intel Corporation Device [8086:7270]
            Kernel driver in use: snd_hda_intel
            Kernel modules: snd_hda_intel, snd_soc_avs, snd_sof_pci_intel_icl
    00:1f.4 SMBus [0c05]: Intel Corporation Device [8086:38a3] (rev 10)
            Subsystem: Intel Corporation Device [8086:7270]
            Kernel driver in use: i801_smbus
    00:1f.5 Serial bus controller [0c80]: Intel Corporation Ice Lake SPI Controller [8086:38a4] (rev 10)
            Subsystem: Intel Corporation Device [8086:7270]
            Kernel driver in use: intel-spi
            Kernel modules: spi_intel_pci
    e5:00.0 Network controller [0280]: Broadcom Inc. and subsidiaries BCM4364 802.11ac Wireless Network Adapter [14e4:4464] (rev 04)
            Subsystem: Apple Inc. Device [106b:07bf]
            Kernel modules: brcmfmac
    e6:00.0 Mass storage controller [0180]: Apple Inc. ANS2 NVMe Controller [106b:2005] (rev 01)
            Subsystem: Apple Inc. Device [106b:1800]
            Kernel driver in use: nvme
    e6:00.1 Non-VGA unclassified device [0000]: Apple Inc. T2 Bridge Controller [106b:1801] (rev 01)
            Subsystem: Apple Inc. T2 Bridge Controller [106b:1801]
    e6:00.2 Non-VGA unclassified device [0000]: Apple Inc. T2 Secure Enclave Processor [106b:1802] (rev 01)
            Subsystem: Apple Inc. T2 Secure Enclave Processor [106b:1802]
    e6:00.3 Multimedia audio controller [0401]: Apple Inc. Apple Audio Device [106b:1803] (rev 01)
            Subsystem: Apple Inc. Device [106b:1889]

`root `[`#`]`lscpu`

    Architecture:             x86_64
      CPU op-mode(s):         32-bit, 64-bit
      Address sizes:          39 bits physical, 48 bits virtual
      Byte Order:             Little Endian
    CPU(s):                   8
      On-line CPU(s) list:    0-7
    Vendor ID:                GenuineIntel
      Model name:             Intel(R) Core(TM) i5-1038NG7 CPU @ 2.00GHz
        CPU family:           6
        Model:                126
        Thread(s) per core:   2
        Core(s) per socket:   4
        Socket(s):            1
        Stepping:             5
        CPU(s) scaling MHz:   24%
        CPU max MHz:          3800.0000
        CPU min MHz:          400.0000
        BogoMIPS:             3993.60
        Flags:                fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush dts
                              acpi mmx fxsr sse sse2 ss ht tm pbe syscall nx pdpe1gb rdtscp lm constant_tsc art ar
                              ch_perfmon pebs bts rep_good nopl xtopology nonstop_tsc cpuid aperfmperf tsc_known_f
                              req pni pclmulqdq dtes64 monitor ds_cpl vmx est tm2 ssse3 sdbg fma cx16 xtpr pdcm pc
                              id sse4_1 sse4_2 x2apic movbe popcnt tsc_deadline_timer aes xsave avx f16c rdrand la
                              hf_lm abm 3dnowprefetch cpuid_fault epb ssbd ibrs ibpb stibp ibrs_enhanced tpr_shado
                              w flexpriority ept vpid ept_ad fsgsbase tsc_adjust bmi1 avx2 smep bmi2 erms invpcid
                              avx512f avx512dq rdseed adx smap avx512ifma clflushopt intel_pt avx512cd sha_ni avx5
                              12bw avx512vl xsaveopt xsavec xgetbv1 xsaves split_lock_detect dtherm ida arat pln p
                              ts hwp hwp_act_window hwp_epp hwp_pkg_req vnmi avx512vbmi umip pku ospke avx512_vbmi
                              2 gfni vaes vpclmulqdq avx512_vnni avx512_bitalg avx512_vpopcntdq rdpid fsrm md_clea
                              r flush_l1d arch_capabilities
    Virtualization features:
      Virtualization:         VT-x
    Caches (sum of all):
      L1d:                    192 KiB (4 instances)
      L1i:                    128 KiB (4 instances)
      L2:                     2 MiB (4 instances)
      L3:                     6 MiB (1 instance)
    NUMA:
      NUMA node(s):           1
      NUMA node0 CPU(s):      0-7
    Vulnerabilities:
      Gather data sampling:   Mitigation; Microcode
      Itlb multihit:          Processor vulnerable
      L1tf:                   Not affected
      Mds:                    Not affected
      Meltdown:               Not affected
      Mmio stale data:        Mitigation; Clear CPU buffers; SMT vulnerable
      Reg file data sampling: Not affected
      Retbleed:               Mitigation; Enhanced IBRS
      Spec rstack overflow:   Not affected
      Spec store bypass:      Mitigation; Speculative Store Bypass disabled via prctl
      Spectre v1:             Mitigation; usercopy/swapgs barriers and __user pointer sanitization
      Spectre v2:             Mitigation; Enhanced / Automatic IBRS; IBPB conditional; RSB filling; PBRSB-eIBRS SW
                               sequence; BHI SW loop, KVM SW loop
      Srbds:                  Mitigation; Microcode
      Tsx async abort:        Not affected

`root `[`#`]`lsusb`

    Bus 001 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub
    Bus 002 Device 001: ID 1d6b:0003 Linux Foundation 3.0 root hub
    Bus 003 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub
    Bus 004 Device 001: ID 1d6b:0003 Linux Foundation 3.0 root hub
    Bus 005 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub
    Bus 005 Device 002: ID 05ac:8233 Apple, Inc. iBridge
    Bus 005 Device 003: ID 05ac:8514 Apple, Inc. FaceTime HD Camera (Built-in)
    Bus 005 Device 004: ID 05ac:8262 Apple, Inc. Ambient Light Sensor
    Bus 005 Device 005: ID 05ac:8103 Apple, Inc. Headset
    Bus 005 Device 006: ID 05ac:027e Apple, Inc. Apple Internal Keyboard / Trackpad
    Bus 005 Device 007: ID 05ac:8302 Apple, Inc. Touch Bar Display
    Bus 005 Device 008: ID 05ac:8102 Apple, Inc. Touch Bar Backlight

## [Configuration]

### [CPU flags]

[FILE] **`/etc/portage/make.conf`**

    COMMON_FLAGS="-O2 -pipe -march=icelake-client"

[FILE] **`/etc/portage/package.use/00cpu-flags`**

    */*  CPU_FLAGS_X86: aes avx avx2 avx512_bitalg avx512_vbmi2 avx512_vnni avx512_vpopcntdq avx512bw avx512cd avx512dq avx512f avx512ifma avx512vbmi avx512vl f16c fma3 mmx mmxext pclmul popcnt rdrand sha sse sse2 sse3 sse4_1 sse4_2 ssse3 vpclmulqdq

## [Installation]

### [Preparation]

Mainline kernels do not support the internal keyboard, trackpad, Wifi and Bluetooth. Either connect USB keyboard/mouse/network or use a Linux image from t2linux during installation.

### [Kernel]

Out of tree patches can be found on [t2linux github](https://github.com/t2linux/linux-t2-patches).

### [Wifi]

Several methods to obtain Wifi firmware are described in the [t2linux documentation](https://wiki.t2linux.org/guides/wifi-bluetooth/)

### [Touchbar]

Install [[[app-laptop/tiny-dfr]](https://packages.gentoo.org/packages/app-laptop/tiny-dfr)[]].

On OpenRC installations, add it to the boot [runlevel](https://wiki.gentoo.org/wiki/OpenRC#Runlevels "OpenRC").

`root `[`#`]`rc-update add tiny-dfr boot`

On systemd installations, enable the tiny-dfr service:

`root `[`#`]`systemctl enable tiny-dfr.service`

## [Troubleshooting]

### [Framebuffer]

Problem: The framebuffer may be too large for the panel, causing text to go off screen or become garbled.

Solution: Apply i915 patch [7001-drm-i915-fbdev-Discard-BIOS-framebuffers-exceeding-h.patch] from t2linux

### [Touchbar]

Problem: Touchbar not recognized after forced poweroff by holding the power button.

Solution: Reboot once more.

Problem: tiny-dfr fails to bind to the touchbar because the DRM device is already in use.

Solution: Ensure that tiny-dfr loads before [Xorg](https://wiki.gentoo.org/wiki/Xorg "Xorg") or [Wayland](https://wiki.gentoo.org/wiki/Wayland "Wayland") graphical sessions, as otherwise these may claim the touchbar drm device.