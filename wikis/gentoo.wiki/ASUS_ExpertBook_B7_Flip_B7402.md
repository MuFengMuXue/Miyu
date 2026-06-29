**Resources**

[[]][Home](https://www.asus.com/laptops/for-work/expertbook/expertbook-b7-flip-b7402f-11th-gen-intel/)

## Contents

-   [[1] [Hardware]](#Hardware)
    -   [[1.1] [Standard]](#Standard)
    -   [[1.2] [Kernel config]](#Kernel_config)
-   [[2] [CPU flags]](#CPU_flags)
-   [[3] [package.use]](#package.use)
-   [[4] [Sound configuration]](#Sound_configuration)
-   [[5] [Troubleshooting]](#Troubleshooting)
    -   [[5.1] [Battery drains during suspend to ram]](#Battery_drains_during_suspend_to_ram)
    -   [[5.2] [Some hardware does not work]](#Some_hardware_does_not_work)
    -   [[5.3] [Some AX201 troubles]](#Some_AX201_troubles)
        -   [[5.3.1] [Power consumption]](#Power_consumption)
        -   [[5.3.2] [AX 201 not detected after S3 sleep]](#AX_201_not_detected_after_S3_sleep)
        -   [[5.3.3] [Bluetooth not working after S3 sleep]](#Bluetooth_not_working_after_S3_sleep)

## [Hardware]

### [Standard]

See [Linux Hardware for ASUS EXPERTBOOK B7402FEA](https://linux-hardware.org/?view=computers&type=convertible&vendor=ASUSTek+Computer&model=ASUS+EXPERTBOOK+B7402FEA_B7402FEA)

  --------------------- ------------------------------------------------------------------------- ------------- ------------------------ -------------------------------------- ---------------- -----------------------------------------------------------------------------------------
  Device                Make/model                                                                Status        Vendor ID / Product ID   Kernel driver(s)                       Kernel version   Notes
  CPU                   Intel® Core™ i5-1155G7                                                    Works         N/A                      N/A                                    5.15
  Video card            Intel Corporation Iris Xe Graphics                                        Works         N/A                      i915                                   5.15
  Audio card            Intel Corporation Tiger Lake-LP Smart Sound Technology Audio Controller   Partial       N/A                      snd_hda_intel, snd_sof_pci_intel_tgl   5.15             Requires sys-firmware/sof-firmware. Microphone from wired headset does not work
  Wi-Fi                 Intel Corporation Wi-Fi 6 AX201                                           Works         N/A                      iwlwifi                                5.15
  Ethernet controller   Intel Corporation Ethernet Connection I219-V                              Works         N/A                      e1000e                                 5.15
  Bluetooth             Intel Corporation AX201 Bluetooth                                         Works         N/A                      btusb                                  5.15             Required sys-kernel/linux-firmware
  Web Camera            IMC Networks USB2.0 HD UVC WebCam                                         Works         N/A                      uvcvideo                               5.15
  Fingerprint Reader    Synaptics, Inc.                                                           Not tested    N/A                      N/A                                    N/A
  Touchpad              Elan Microelectronics Corp. ELAN:ARM-M4                                   Works         N/A                      N/A                                    5.15
  LTE Controller        Intel 5G Solution                                                         Partial       N/A                      N/A                                    N/A              0000:55:00.0 Wireless controller \[0d40\]: MEDIATEK Corp. Device \[14c3:4d75\] (rev 01)
  --------------------- ------------------------------------------------------------------------- ------------- ------------------------ -------------------------------------- ---------------- -----------------------------------------------------------------------------------------

`root `[`#`]`lscpu`

    Architecture:            x86_64
      CPU op-mode(s):        32-bit, 64-bit
      Address sizes:         39 bits physical, 48 bits virtual
      Byte Order:            Little Endian
    CPU(s):                  8
      On-line CPU(s) list:   0-7
    Vendor ID:               GenuineIntel
      BIOS Vendor ID:        Intel(R) Corporation
      Model name:            11th Gen Intel(R) Core(TM) i5-1155G7 @ 2.50GHz
        BIOS Model name:     11th Gen Intel(R) Core(TM) i5-1155G7 @ 2.50GHz To Be Filled By O.E.M. CPU @ 4.3GHz
        BIOS CPU family:     205
        CPU family:          6
        Model:               140
        Thread(s) per core:  2
        Core(s) per socket:  4
        Socket(s):           1
        Stepping:            2
        CPU(s) scaling MHz:  23%
        CPU max MHz:         4500.0000
        CPU min MHz:         400.0000
        BogoMIPS:            4992.00
        Flags:               fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush dts acpi mmx fxsr sse sse2 ss ht tm pbe syscall nx pdpe1gb rdtscp lm constant_tsc art arch_perfmon pebs
                             bts rep_good nopl xtopology nonstop_tsc cpuid aperfmperf tsc_known_freq pni pclmulqdq dtes64 monitor ds_cpl vmx est tm2 ssse3 sdbg fma cx16 xtpr pdcm pcid sse4_1 sse4_2 x2apic movbe po
                             pcnt tsc_deadline_timer aes xsave avx f16c rdrand lahf_lm abm 3dnowprefetch cpuid_fault epb cat_l2 cdp_l2 ssbd ibrs ibpb stibp ibrs_enhanced tpr_shadow flexpriority ept vpid ept_ad fsg
                             sbase tsc_adjust bmi1 avx2 smep bmi2 erms invpcid rdt_a avx512f avx512dq rdseed adx smap avx512ifma clflushopt clwb intel_pt avx512cd sha_ni avx512bw avx512vl xsaveopt xsavec xgetbv1 x
                             saves split_lock_detect dtherm ida arat pln pts hwp hwp_notify hwp_act_window hwp_epp hwp_pkg_req vnmi avx512vbmi umip pku ospke avx512_vbmi2 gfni vaes vpclmulqdq avx512_vnni avx512_bi
                             talg avx512_vpopcntdq rdpid movdiri movdir64b fsrm avx512_vp2intersect md_clear ibt flush_l1d arch_capabilities
    Virtualization features:
      Virtualization:        VT-x
    Caches (sum of all):
      L1d:                   192 KiB (4 instances)
      L1i:                   128 KiB (4 instances)
      L2:                    5 MiB (4 instances)
      L3:                    8 MiB (1 instance)
    NUMA:
      NUMA node(s):          1
      NUMA node0 CPU(s):     0-7
    Vulnerabilities:
      Gather data sampling:  Mitigation; Microcode
      Itlb multihit:         Not affected
      L1tf:                  Not affected
      Mds:                   Not affected
      Meltdown:              Not affected
      Mmio stale data:       Not affected
      Retbleed:              Not affected
      Spec rstack overflow:  Not affected
      Spec store bypass:     Mitigation; Speculative Store Bypass disabled via prctl
      Spectre v1:            Mitigation; usercopy/swapgs barriers and __user pointer sanitization
      Spectre v2:            Mitigation; Enhanced / Automatic IBRS, IBPB conditional, RSB filling, PBRSB-eIBRS SW sequence
      Srbds:                 Not affected
      Tsx async abort:       Not affected

`root `[`#`]`lspci -nnk`

    0000:00:00.0 Host bridge [0600]: Intel Corporation 11th Gen Core Processor Host Bridge/DRAM Registers [8086:9a14] (rev 02)
            Subsystem: ASUSTeK Computer Inc. 11th Gen Core Processor Host Bridge/DRAM Registers [1043:1b02]
            Kernel modules: igen6_edac
    0000:00:02.0 VGA compatible controller [0300]: Intel Corporation TigerLake-LP GT2 [Iris Xe Graphics] [8086:9a49] (rev 03)
            DeviceName: VGA
            Subsystem: ASUSTeK Computer Inc. TigerLake-LP GT2 [Iris Xe Graphics] [1043:1b02]
            Kernel driver in use: i915
            Kernel modules: i915
    0000:00:04.0 Signal processing controller [1180]: Intel Corporation TigerLake-LP Dynamic Tuning Processor Participant [8086:9a03] (rev 02)
            Subsystem: ASUSTeK Computer Inc. TigerLake-LP Dynamic Tuning Processor Participant [1043:1b02]
            Kernel driver in use: proc_thermal
            Kernel modules: processor_thermal_device_pci_legacy
    0000:00:07.0 PCI bridge [0604]: Intel Corporation Tiger Lake-LP Thunderbolt 4 PCI Express Root Port #0 [8086:9a23] (rev 02)
            Kernel driver in use: pcieport
    0000:00:07.1 PCI bridge [0604]: Intel Corporation Tiger Lake-LP Thunderbolt 4 PCI Express Root Port #1 [8086:9a25] (rev 02)
            Kernel driver in use: pcieport
    0000:00:08.0 System peripheral [0880]: Intel Corporation GNA Scoring Accelerator module [8086:9a11] (rev 02)
            Subsystem: ASUSTeK Computer Inc. GNA Scoring Accelerator module [1043:1b02]
    0000:00:0a.0 Signal processing controller [1180]: Intel Corporation Tigerlake Telemetry Aggregator Driver [8086:9a0d] (rev 01)
            Kernel driver in use: intel_vsec
            Kernel modules: intel_vsec
    0000:00:0d.0 USB controller [0c03]: Intel Corporation Tiger Lake-LP Thunderbolt 4 USB Controller [8086:9a13] (rev 02)
            Kernel driver in use: xhci_hcd
            Kernel modules: xhci_pci
    0000:00:0d.2 USB controller [0c03]: Intel Corporation Tiger Lake-LP Thunderbolt 4 NHI #0 [8086:9a1b] (rev 02)
            Subsystem: Device [2222:1111]
            Kernel driver in use: thunderbolt
            Kernel modules: thunderbolt
    0000:00:0e.0 RAID bus controller [0104]: Intel Corporation Volume Management Device NVMe RAID Controller [8086:9a0b]
            Subsystem: ASUSTeK Computer Inc. Volume Management Device NVMe RAID Controller [1043:1b02]
            Kernel driver in use: vmd
            Kernel modules: vmd
    0000:00:12.0 Serial controller [0700]: Intel Corporation Tiger Lake-LP Integrated Sensor Hub [8086:a0fc] (rev 30)
            Kernel driver in use: intel_ish_ipc
            Kernel modules: intel_ish_ipc
    0000:00:14.0 USB controller [0c03]: Intel Corporation Tiger Lake-LP USB 3.2 Gen 2x1 xHCI Host Controller [8086:a0ed] (rev 30)
            Subsystem: ASUSTeK Computer Inc. Tiger Lake-LP USB 3.2 Gen 2x1 xHCI Host Controller [1043:201f]
            Kernel driver in use: xhci_hcd
            Kernel modules: xhci_pci
    0000:00:14.2 RAM memory [0500]: Intel Corporation Tiger Lake-LP Shared SRAM [8086:a0ef] (rev 30)
            Subsystem: ASUSTeK Computer Inc. Tiger Lake-LP Shared SRAM [1043:1b02]
    0000:00:14.3 Network controller [0280]: Intel Corporation Wi-Fi 6 AX201 [8086:a0f0] (rev 30)
            DeviceName: WLAN
            Subsystem: Intel Corporation Wi-Fi 6 AX201 [8086:0074]
            Kernel driver in use: iwlwifi
            Kernel modules: iwlwifi
    0000:00:15.0 Serial bus controller [0c80]: Intel Corporation Tiger Lake-LP Serial IO I2C Controller #0 [8086:a0e8] (rev 30)
            Subsystem: ASUSTeK Computer Inc. Tiger Lake-LP Serial IO I2C Controller [1043:1b02]
            Kernel driver in use: intel-lpss
            Kernel modules: intel_lpss_pci
    0000:00:15.1 Serial bus controller [0c80]: Intel Corporation Tiger Lake-LP Serial IO I2C Controller #1 [8086:a0e9] (rev 30)
            Subsystem: ASUSTeK Computer Inc. Tiger Lake-LP Serial IO I2C Controller [1043:1b02]
            Kernel driver in use: intel-lpss
            Kernel modules: intel_lpss_pci
    0000:00:15.2 Serial bus controller [0c80]: Intel Corporation Tiger Lake-LP Serial IO I2C Controller #2 [8086:a0ea] (rev 30)
            Subsystem: ASUSTeK Computer Inc. Tiger Lake-LP Serial IO I2C Controller [1043:1b02]
            Kernel driver in use: intel-lpss
            Kernel modules: intel_lpss_pci
    0000:00:16.0 Communication controller [0780]: Intel Corporation Tiger Lake-LP Management Engine Interface [8086:a0e0] (rev 30)
            Subsystem: ASUSTeK Computer Inc. Tiger Lake-LP Management Engine Interface [1043:1b02]
            Kernel driver in use: mei_me
            Kernel modules: mei_me
    0000:00:1c.0 PCI bridge [0604]: Intel Corporation Device [8086:a0b8] (rev 30)
            Subsystem: ASUSTeK Computer Inc. Device [1043:1b02]
            Kernel driver in use: pcieport
    0000:00:1c.5 PCI bridge [0604]: Intel Corporation Tigerlake PCH-LP PCI Express Root Port #6 [8086:a0bd] (rev 30)
            Subsystem: ASUSTeK Computer Inc. Tigerlake PCH-LP PCI Express Root Port [1043:1b02]
            Kernel driver in use: pcieport
    0000:00:1d.0 System peripheral [0880]: Intel Corporation RST VMD Managed Controller [8086:09ab]
            Subsystem: ASUSTeK Computer Inc. RST VMD Managed Controller [1043:1b02]
    0000:00:1f.0 ISA bridge [0601]: Intel Corporation Tiger Lake-LP LPC Controller [8086:a082] (rev 30)
            Subsystem: ASUSTeK Computer Inc. Tiger Lake-LP LPC Controller [1043:1b02]
    0000:00:1f.3 Multimedia audio controller [0401]: Intel Corporation Tiger Lake-LP Smart Sound Technology Audio Controller [8086:a0c8] (rev 30)
            Subsystem: ASUSTeK Computer Inc. Tiger Lake-LP Smart Sound Technology Audio Controller [1043:1b02]
            Kernel driver in use: sof-audio-pci-intel-tgl
            Kernel modules: snd_hda_intel, snd_sof_pci_intel_tgl
    0000:00:1f.4 SMBus [0c05]: Intel Corporation Tiger Lake-LP SMBus Controller [8086:a0a3] (rev 30)
            Subsystem: ASUSTeK Computer Inc. Tiger Lake-LP SMBus Controller [1043:1b02]
            Kernel driver in use: i801_smbus
            Kernel modules: i2c_i801
    0000:00:1f.5 Serial bus controller [0c80]: Intel Corporation Tiger Lake-LP SPI Controller [8086:a0a4] (rev 30)
            Subsystem: ASUSTeK Computer Inc. Tiger Lake-LP SPI Controller [1043:1b02]
    0000:00:1f.6 Ethernet controller [0200]: Intel Corporation Ethernet Connection (13) I219-V [8086:15fc] (rev 30)
            DeviceName: GLAN
            Subsystem: Intel Corporation Ethernet Connection (13) I219-V [8086:0000]
            Kernel driver in use: e1000e
            Kernel modules: e1000e
    0000:58:00.0 Wireless controller [0d40]: MEDIATEK Corp. Device [14c3:4d75] (rev 01)
            Subsystem: Device [1cf8:3500]
    10000:e0:1d.0 PCI bridge [0604]: Intel Corporation Tiger Lake-LP PCI Express Root Port #9 [8086:a0b0] (rev 30)
            Subsystem: ASUSTeK Computer Inc. Tiger Lake-LP PCI Express Root Port [1043:1b02]
            Kernel driver in use: pcieport
    10000:e1:00.0 Non-Volatile memory controller [0108]: Kingston Technology Company, Inc. KC3000/Renegade NVMe SSD [2646:5013] (rev 01)
            Subsystem: Kingston Technology Company, Inc. KC3000/FURY Renegade NVMe SSD E18 [2646:5013]
            Kernel driver in use: nvme
            Kernel modules: nvme

`root `[`#`]`lsusb`

    Bus 001 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub
    Bus 002 Device 001: ID 1d6b:0003 Linux Foundation 3.0 root hub
    Bus 003 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub
    Bus 003 Device 002: ID 13d3:56eb IMC Networks USB2.0 HD UVC WebCam
    Bus 003 Device 003: ID 04f3:0c77 Elan Microelectronics Corp. ELAN:ARM-M4
    Bus 003 Device 004: ID 058f:9540 Alcor Micro Corp. AU9540 Smartcard Reader
    Bus 003 Device 005: ID 8087:0026 Intel Corp. AX201 Bluetooth
    Bus 004 Device 001: ID 1d6b:0003 Linux Foundation 3.0 root hub

`root `[`#`]`lsusb -vt`

    /:  Bus 001.Port 001: Dev 001, Class=root_hub, Driver=xhci_hcd/1p, 480M
        ID 1d6b:0002 Linux Foundation 2.0 root hub
    /:  Bus 002.Port 001: Dev 001, Class=root_hub, Driver=xhci_hcd/4p, 10000M
        ID 1d6b:0003 Linux Foundation 3.0 root hub
    /:  Bus 003.Port 001: Dev 001, Class=root_hub, Driver=xhci_hcd/12p, 480M
        ID 1d6b:0002 Linux Foundation 2.0 root hub
        |__ Port 005: Dev 002, If 0, Class=Video, Driver=uvcvideo, 480M
            ID 13d3:56eb IMC Networks
        |__ Port 005: Dev 002, If 1, Class=Video, Driver=uvcvideo, 480M
            ID 13d3:56eb IMC Networks
        |__ Port 005: Dev 002, If 2, Class=Video, Driver=uvcvideo, 480M
            ID 13d3:56eb IMC Networks
        |__ Port 005: Dev 002, If 3, Class=Video, Driver=uvcvideo, 480M
            ID 13d3:56eb IMC Networks
        |__ Port 005: Dev 002, If 4, Class=Application Specific Interface, Driver=[none], 480M
            ID 13d3:56eb IMC Networks
        |__ Port 008: Dev 003, If 0, Class=Vendor Specific Class, Driver=[none], 12M
            ID 04f3:0c77 Elan Microelectronics Corp.
        |__ Port 009: Dev 004, If 0, Class=Chip/SmartCard, Driver=[none], 12M
            ID 058f:9540 Alcor Micro Corp. AU9540 Smartcard Reader
        |__ Port 010: Dev 005, If 0, Class=Wireless, Driver=btusb, 12M
            ID 8087:0026 Intel Corp. AX201 Bluetooth
        |__ Port 010: Dev 005, If 1, Class=Wireless, Driver=btusb, 12M
            ID 8087:0026 Intel Corp. AX201 Bluetooth
    /:  Bus 004.Port 001: Dev 001, Class=root_hub, Driver=xhci_hcd/4p, 10000M
        ID 1d6b:0003 Linux Foundation 3.0 root hub

### [Kernel config]

[Kernel config](https://raw.githubusercontent.com/aruslantsev/system-configs/refs/heads/master/Gentoo/ExpertBook/kernel/config-6.12.17)

## [CPU flags]

[FILE] **`/etc/portage/package.use/00-cpuflags`**

    */* CPU_FLAGS_X86: aes avx avx2 avx512f avx512dq avx512cd avx512bw avx512vl avx512vbmi f16c fma3 mmx mmxext pclmul popcnt rdrand sha sse sse2 sse3 sse4_1 sse4_2 ssse3

## [package.use]

[FILE] **`/etc/portage/package.use/00video`**

    */* VIDEO_CARDS: -* intel

[FILE] **`/etc/portage/package.use/00input`**

    */* INPUT_DEVICES: libinput synaptics

## [Sound configuration]

Used default parameters with pipewire.

Fix for wired headphones for ALC 294 codec (microphone still does not work).

[FILE] **`/lib/firmware/alc294-sound-patch.fw`**

    [codec]
    0x10ec0294 0x1043194e 0

    [pincfg]
    0x19 0x03a11050
    0x1a 0x03a11c30
    0x21 0x03211420

    [verb]
    0x20 0x500 0x62
    0x20 0x400 0xa007
    0x20 0x500 0x10
    0x20 0x400 0x8420
    0x20 0x500 0x0f
    0x20 0x400 0x7774

[FILE] **`cat /etc/modprobe.d/alsa-base.conf`**

    options snd_hda_intel model=auto
    options snd-hda-intel patch=alc294-sound-patch.fw

Different combinations of hda verbs work for wired headphones, but still none of them makes wired microphone useful.

## [Troubleshooting]

### [Battery drains during suspend to ram]

Check what sleep state system uses. Add option mem_sleep_default=deep to grub.cfg if needed.

[FILE] **`/sys/power/mem_sleep`**

    s2idle [deep]

### [Some hardware does not work]

E.g. Wi-Fi controller is not detected, keyboard is partially working.

Check kernel version, I had troubles with version 6.1. All works on 5.15 and 6.4+ with some exceptions for 6.8.

Update firmware to the latest versions.

### [Some AX201 troubles]

This part is tested only on one laptop, so **it does not have any statistical significance**

#### [Power consumption]

Adding iwlwifi.power_save=1 kernel parameter helps to reduce power consumption by 1-1.5W. This parameter does not affect the stability of the system.

Power consumption was measured by powertop with moderate network I/O.

#### [AX 201 not detected after S3 sleep]

This problem arises on gentoo-sources \>6.6.8 \<6.7 in 20% cases. Also kernel bug with kernel NULL pointer dereference is thrown. After this system becomes unusable, and only reboot helps to fix this issue.

#### [Bluetooth not working after S3 sleep]

With some kernel versions after S3 sleep system does not see bluetooth in 10% cases max. Reboot always helps. Sending system to S3 sleep and return back helps in 80-90% cases.