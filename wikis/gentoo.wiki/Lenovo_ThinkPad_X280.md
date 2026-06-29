[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=Lenovo_ThinkPad_X280&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

**Resources**

[[]][Official Support Page](https://pcsupport.lenovo.com/us/en/products/laptops-and-netbooks/thinkpad-x-series-laptops/thinkpad-x280-type-20kf-20ke)

[[]][Specifications](https://psref.lenovo.com/syspool/Sys/PDF/ThinkPad/ThinkPad_X280/ThinkPad_X280_Spec.PDF)

[[]][Specifications (by region)](https://psref.lenovo.com/WDProduct/ThinkPad/ThinkPad_X280?tab=model)

[[]][Hardware Maintenance Manual](https://download.lenovo.com/pccbbs/mobiles_pdf/tp_x280_hmm_en.pdf)

[[]][User Guide](https://download.lenovo.com/pccbbs/mobiles_pdf/tp_x280_ug_v2_en.pdf)

## [Hardware]

  ------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -------- ------------------------ ----------------------------------------------------------- -----------------------------------------------------------------
  Device        Make/model                                                                                                                                                                Status   Vendor ID / Product ID   Kernel driver(s)                                            Notes
  CPU           Intel [i5-7300U](https://ark.intel.com/content/www/us/en/ark/products/97472/intel-core-i5-7300u-processor-3m-cache-up-to-3-50-ghz.html)   Works    N/A                      N/A
  USB           Intel Corporation Sunrise Point-LP USB 3.0 xHCI Controller                                                                                                                Works    8086:9d2f                xhci_hcd
  Thunderbolt   Intel Corporation JHL6240 Thunderbolt 3 USB 3.1 Controller                                                                                                                Works    8086:15c1                xhci_hcd
  Video card    Intel Corporation HD Graphics 620                                                                                                                                         Works    8086:5916                [i915](https://wiki.gentoo.org/wiki/Intel "Intel")          [#Video_card](#Video_card)
  Audio card    Intel Corporation Sunrise Point-LP HD Audio                                                                                                                               Works    8086:9d71                [snd_hda_intel](https://wiki.gentoo.org/wiki/ALSA "ALSA")   [#Audio_card](#Audio_card)
  WLAN          Intel Corporation Wireless 8265 / 8275                                                                                                                                    Works    8086:24fd                [iwlwifi](https://wiki.gentoo.org/wiki/Iwlwifi "Iwlwifi")   [#Wi-Fi](#Wi-Fi)
  Touchpad      SynPS/2 Synaptics TouchPad                                                                                                                                                Works    N/A                                                                                  [synaptics](https://wiki.gentoo.org/wiki/Synaptics "Synaptics")
  ------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -------- ------------------------ ----------------------------------------------------------- -----------------------------------------------------------------

`root `[`#`]`lspci -nnk`

    00:00.0 Host bridge [0600]: Intel Corporation Xeon E3-1200 v6/7th Gen Core Processor Host Bridge/DRAM Registers [8086:5904] (rev 02)
            Subsystem: Lenovo Device [17aa:2256]
            Kernel driver in use: skl_uncore
    00:02.0 VGA compatible controller [0300]: Intel Corporation HD Graphics 620 [8086:5916] (rev 02)
            Subsystem: Lenovo Device [17aa:2256]
            Kernel driver in use: i915
            Kernel modules: i915
    00:04.0 Signal processing controller [1180]: Intel Corporation Xeon E3-1200 v5/E3-1500 v5/6th Gen Core Processor Thermal Subsystem [8086:1903] (rev 02)
            Subsystem: Lenovo Device [17aa:2256]
            Kernel driver in use: proc_thermal
            Kernel modules: processor_thermal_device_pci_legacy
    00:08.0 System peripheral [0880]: Intel Corporation Xeon E3-1200 v5/v6 / E3-1500 v5 / 6th/7th/8th Gen Core Processor Gaussian Mixture Model [8086:1911]
            Subsystem: Lenovo Device [17aa:2256]
    00:14.0 USB controller [0c03]: Intel Corporation Sunrise Point-LP USB 3.0 xHCI Controller [8086:9d2f] (rev 21)
            Subsystem: Lenovo Device [17aa:2256]
            Kernel driver in use: xhci_hcd
            Kernel modules: xhci_pci
    00:14.2 Signal processing controller [1180]: Intel Corporation Sunrise Point-LP Thermal subsystem [8086:9d31] (rev 21)
            Subsystem: Lenovo Device [17aa:2256]
            Kernel driver in use: intel_pch_thermal
            Kernel modules: intel_pch_thermal
    00:16.0 Communication controller [0780]: Intel Corporation Sunrise Point-LP CSME HECI #1 [8086:9d3a] (rev 21)
            Subsystem: Lenovo Device [17aa:2256]
            Kernel driver in use: mei_me
            Kernel modules: mei_me
    00:1c.0 PCI bridge [0604]: Intel Corporation Sunrise Point-LP PCI Express Root Port #1 [8086:9d10] (rev f1)
            Subsystem: Lenovo Device [17aa:2256]
            Kernel driver in use: pcieport
    00:1c.2 PCI bridge [0604]: Intel Corporation Sunrise Point-LP PCI Express Root Port #3 [8086:9d12] (rev f1)
            Subsystem: Lenovo Device [17aa:2256]
            Kernel driver in use: pcieport
    00:1c.4 PCI bridge [0604]: Intel Corporation Sunrise Point-LP PCI Express Root Port #5 [8086:9d14] (rev f1)
            Subsystem: Lenovo Device [17aa:2256]
            Kernel driver in use: pcieport
    00:1f.0 ISA bridge [0601]: Intel Corporation Sunrise Point LPC/eSPI Controller [8086:9d4e] (rev 21)
            Subsystem: Lenovo Device [17aa:2256]
    00:1f.2 Memory controller [0580]: Intel Corporation Sunrise Point-LP PMC [8086:9d21] (rev 21)
            Subsystem: Lenovo Device [17aa:2256]
    00:1f.3 Audio device [0403]: Intel Corporation Sunrise Point-LP HD Audio [8086:9d71] (rev 21)
            Subsystem: Lenovo Device [17aa:2256]
            Kernel driver in use: snd_hda_intel
            Kernel modules: snd_hda_intel, snd_soc_skl, snd_sof_pci_intel_skl
    00:1f.4 SMBus [0c05]: Intel Corporation Sunrise Point-LP SMBus [8086:9d23] (rev 21)
            Subsystem: Lenovo Device [17aa:2256]
            Kernel driver in use: i801_smbus
            Kernel modules: i2c_i801
    00:1f.6 Ethernet controller [0200]: Intel Corporation Ethernet Connection (4) I219-LM [8086:15d7] (rev 21)
            Subsystem: Lenovo Device [17aa:2256]
            Kernel driver in use: e1000e
            Kernel modules: e1000e
    02:00.0 PCI bridge [0604]: Intel Corporation JHL6240 Thunderbolt 3 Bridge (Low Power) [Alpine Ridge LP 2016] [8086:15c0] (rev 01)
            Subsystem: Lenovo Device [17aa:2256]
            Kernel driver in use: pcieport
    03:00.0 PCI bridge [0604]: Intel Corporation JHL6240 Thunderbolt 3 Bridge (Low Power) [Alpine Ridge LP 2016] [8086:15c0] (rev 01)
            Subsystem: Lenovo Device [17aa:2256]
            Kernel driver in use: pcieport
    03:01.0 PCI bridge [0604]: Intel Corporation JHL6240 Thunderbolt 3 Bridge (Low Power) [Alpine Ridge LP 2016] [8086:15c0] (rev 01)
            Subsystem: Lenovo Device [17aa:2256]
            Kernel driver in use: pcieport
    03:02.0 PCI bridge [0604]: Intel Corporation JHL6240 Thunderbolt 3 Bridge (Low Power) [Alpine Ridge LP 2016] [8086:15c0] (rev 01)
            Subsystem: Lenovo Device [17aa:2256]
            Kernel driver in use: pcieport
    04:00.0 System peripheral [0880]: Intel Corporation JHL6240 Thunderbolt 3 NHI (Low Power) [Alpine Ridge LP 2016] [8086:15bf] (rev 01)
            Subsystem: Lenovo Device [17aa:2256]
    3a:00.0 USB controller [0c03]: Intel Corporation JHL6240 Thunderbolt 3 USB 3.1 Controller (Low Power) [Alpine Ridge LP 2016] [8086:15c1] (rev 01)
            Subsystem: Lenovo Device [17aa:2256]
            Kernel driver in use: xhci_hcd
            Kernel modules: xhci_pci
    3b:00.0 Network controller [0280]: Intel Corporation Wireless 8265 / 8275 [8086:24fd] (rev 78)
            Subsystem: Intel Corporation Dual Band Wireless-AC 8265 [Windstorm Peak] [8086:0010]
            Kernel driver in use: iwlwifi
            Kernel modules: iwlwifi
    3c:00.0 Non-Volatile memory controller [0108]: Micron Technology Inc 2550 NVMe SSD (DRAM-less) [1344:5416] (rev 01)
            Subsystem: Micron Technology Inc Device [1344:1100]
            Kernel driver in use: nvme
            Kernel modules: nvme

`root `[`#`]`lsusb`

    Bus 001 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub
    Bus 001 Device 002: ID 8087:0a2b Intel Corp. Bluetooth wireless interface
    Bus 001 Device 003: ID 04f2:b604 Chicony Electronics Co., Ltd Integrated Camera (1280x720@30)
    Bus 001 Device 004: ID 06cb:009a Synaptics, Inc. Metallica MIS Touch Fingerprint Reader
    Bus 002 Device 001: ID 1d6b:0003 Linux Foundation 3.0 root hub
    Bus 002 Device 002: ID 0bda:0316 Realtek Semiconductor Corp. Card Reader
    Bus 003 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub
    Bus 004 Device 001: ID 1d6b:0003 Linux Foundation 3.0 root hub

`root `[`#`]`lsusb -t`

    /:  Bus 001.Port 001: Dev 001, Class=root_hub, Driver=xhci_hcd/12p, 480M
        |__ Port 007: Dev 002, If 0, Class=Wireless, Driver=btusb, 12M
        |__ Port 007: Dev 002, If 1, Class=Wireless, Driver=btusb, 12M
        |__ Port 008: Dev 003, If 0, Class=Video, Driver=uvcvideo, 480M
        |__ Port 008: Dev 003, If 1, Class=Video, Driver=uvcvideo, 480M
        |__ Port 009: Dev 004, If 0, Class=Vendor Specific Class, Driver=[none], 12M
    /:  Bus 002.Port 001: Dev 001, Class=root_hub, Driver=xhci_hcd/6p, 5000M
        |__ Port 003: Dev 002, If 0, Class=Mass Storage, Driver=usb-storage, 5000M
    /:  Bus 003.Port 001: Dev 001, Class=root_hub, Driver=xhci_hcd/2p, 480M
    /:  Bus 004.Port 001: Dev 001, Class=root_hub, Driver=xhci_hcd/2p, 10000M

`root `[`#`]`lscpu`

    Architecture:                        x86_64
      CPU op-mode(s):                      32-bit, 64-bit
      Address sizes:                       39 bits physical, 48 bits virtual
      Byte Order:                          Little Endian
    CPU:                                   4
      On-line CPU(s) list:                 0-3
    Vendor ID:                           GenuineIntel
      Model name:                        Intel(R) Core(TM) i5-7300U CPU @ 2.60GHz
        CPU family:                       6
        Model:                            142
        Thread(s) per core:               2
        Core(s) per socket:               2
        Socket(s):                        1
        Stepping:                         9
        CPU(s) scaling MHz:                14%
        CPU max MHz:                      3500.0000
        CPU min MHz:                      400.0000
        BogoMIPS:                          5401.81
        Flags:                            fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov p
                                           at pse36 clflush dts acpi mmx fxsr sse sse2 ss ht tm pbe syscal
                                           l nx pdpe1gb rdtscp lm constant_tsc art arch_perfmon pebs bts r
                                           ep_good nopl xtopology nonstop_tsc cpuid aperfmperf pni pclmulq
                                           dq dtes64 monitor ds_cpl vmx smx est tm2 ssse3 sdbg fma cx16 xt
                                           pr pdcm pcid sse4_1 sse4_2 x2apic movbe popcnt tsc_deadline_tim
                                           er aes xsave avx f16c rdrand lahf_lm abm 3dnowprefetch cpuid_fa
                                           ult epb pti ssbd ibrs ibpb stibp tpr_shadow flexpriority ept vp
                                           id ept_ad fsgsbase tsc_adjust bmi1 avx2 smep bmi2 erms invpcid
                                           mpx rdseed adx smap clflushopt intel_pt xsaveopt xsavec xgetbv1
                                            xsaves dtherm ida arat pln pts hwp hwp_notify hwp_act_window h
                                           wp_epp vnmi md_clear flush_l1d arch_capabilities
    Virtualization features:
      Virtualization:                      VT-x
    Caches (sum of all):
      L1d:                                 64 KiB (2 instances)
      L1i:                                 64 KiB (2 instances)
      L2:                                  512 KiB (2 instances)
      L3:                                  3 MiB (1 instance)
    NUMA:
      NUMA node(s):                        1
      NUMA node0 CPU(s):                   0-3
    Vulnerabilities:
      Gather data sampling:                Mitigation; Microcode
      Itlb multihit:                       Processor vulnerable
      L1tf:                                Mitigation; PTE Inversion
      Mds:                                 Mitigation; Clear CPU buffers; SMT vulnerable
      Meltdown:                            Mitigation; PTI
      Mmio stale data:                     Mitigation; Clear CPU buffers; SMT vulnerable
      Reg file data sampling:              Not affected
      Retbleed:                            Mitigation; IBRS
      Spec rstack overflow:                Not affected
      Spec store bypass:                   Mitigation; Speculative Store Bypass disabled via prctl
      Spectre v1:                          Mitigation; usercopy/swapgs barriers and __user pointer sanitiz
                                           ation
      Spectre v2:                          Mitigation; IBRS; IBPB conditional; STIBP conditional; RSB fill
                                           ing; PBRSB-eIBRS Not affected; BHI Not affected
      Srbds:                               Mitigation; Microcode
      Tsx async abort:                     Mitigation; TSX disabled

`root `[`#`]`lsinput -v`

```
/dev/input/event0
   id   : 0000:0003, HOST, v0
   phys : "PNP0C0E/button/input0"
   name : "Sleep Button"
   KEY  : SLEEP

/dev/input/event1
   id   : 0000:0005, HOST, v0
   phys : "PNP0C0D/button/input0"
   name : "Lid Switch"
   SW   : LID

/dev/input/event2
   id   : 0000:0001, HOST, v0
   phys : "LNXPWRBN/button/input0"
   name : "Power Button"
   KEY  : POWER

/dev/input/event3
   id   : 0001:0001, I8042, v43907
   phys : "isa0060/serio0/input0"
   name : "AT Translated Set 2 keyboard"
   KEY  : [ 144 codes ]
   MSC  : SCAN
   LED  : NUML CAPSL SCROLLL

/dev/input/event4
   id   : 0002:0007, I8042, v433
   phys : "isa0060/serio1/input0"
   name : "SynPS/2 Synaptics TouchPad"
   KEY  : [ 7 codes ]
   ABS  : [ 9 codes ]

/dev/input/event5
   id   : 0002:000a, I8042, v0
   phys : "synaptics-pt/serio0/input0"
   name : "TPPS/2 Elan TrackPoint"
   KEY  : BTN_LEFT BTN_RIGHT BTN_MIDDLE
   REL  : X Y

/dev/input/event6
   id   : 001f:0001, ISA, v256
   phys : "isa0061/input0"
   name : "PC Speaker"
   SND  : BELL TONE

/dev/input/event7
   id   : 17aa:5054, HOST, v16641
   phys : "thinkpad_acpi/input0"
   name : "ThinkPad Extra Buttons"
   KEY  : [ 39 codes ]
   MSC  : SCAN
   SW   : RADIO

/dev/input/event8
   id   : 0000:0006, HOST, v0
   phys : "LNXVIDEO/video/input0"
   name : "Video Bus"
   KEY  : [ 8 codes ]

/dev/input/event9
   id   : 0000:0000, (null), v0
   phys : "ALSA"
   name : "HDA Intel PCH Mic"
   SW   : MICROPHONE_INSERT

/dev/input/event10
   id   : 0000:0000, (null), v0
   phys : "ALSA"
   name : "HDA Intel PCH Headphone"
   SW   : HEADPHONE_INSERT

/dev/input/event11
   id   : 0000:0000, (null), v0
   phys : "ALSA"
   name : "HDA Intel PCH HDMI/DP,pcm=3"
   SW   : LINEOUT_INSERT VIDEOOUT_INSERT

/dev/input/event12
   id   : 0000:0000, (null), v0
   phys : "ALSA"
   name : "HDA Intel PCH HDMI/DP,pcm=7"
   SW   : LINEOUT_INSERT VIDEOOUT_INSERT

/dev/input/event13
   id   : 0000:0000, (null), v0
   phys : "ALSA"
   name : "HDA Intel PCH HDMI/DP,pcm=8"
   SW   : LINEOUT_INSERT VIDEOOUT_INSERT
```

`root `[`#`]`libinput list-devices`

```
Device:           Power Button
Kernel:           /dev/input/event2
Group:            1
Seat:             seat0, default
Capabilities:     keyboard
Tap-to-click:     n/a
Tap-and-drag:     n/a
Tap drag lock:    n/a
Left-handed:      n/a
Nat.scrolling:    n/a
Middle emulation: n/a
Calibration:      n/a
Scroll methods:   none
Click methods:    none
Disable-w-typing: n/a
Disable-w-trackpointing: n/a
Accel profiles:   n/a
Rotation:         0.0

Device:           Video Bus
Kernel:           /dev/input/event8
Group:            2
Seat:             seat0, default
Capabilities:     keyboard
Tap-to-click:     n/a
Tap-and-drag:     n/a
Tap drag lock:    n/a
Left-handed:      n/a
Nat.scrolling:    n/a
Middle emulation: n/a
Calibration:      n/a
Scroll methods:   none
Click methods:    none
Disable-w-typing: n/a
Disable-w-trackpointing: n/a
Accel profiles:   n/a
Rotation:         0.0

Device:           Lid Switch
Kernel:           /dev/input/event1
Group:            3
Seat:             seat0, default
Capabilities:     switch
Tap-to-click:     n/a
Tap-and-drag:     n/a
Tap drag lock:    n/a
Left-handed:      n/a
Nat.scrolling:    n/a
Middle emulation: n/a
Calibration:      n/a
Scroll methods:   none
Click methods:    none
Disable-w-typing: n/a
Disable-w-trackpointing: n/a
Accel profiles:   n/a
Rotation:         0.0

Device:           Sleep Button
Kernel:           /dev/input/event0
Group:            4
Seat:             seat0, default
Capabilities:     keyboard
Tap-to-click:     n/a
Tap-and-drag:     n/a
Tap drag lock:    n/a
Left-handed:      n/a
Nat.scrolling:    n/a
Middle emulation: n/a
Calibration:      n/a
Scroll methods:   none
Click methods:    none
Disable-w-typing: n/a
Disable-w-trackpointing: n/a
Accel profiles:   n/a
Rotation:         0.0

Device:           AT Translated Set 2 keyboard
Kernel:           /dev/input/event3
Group:            5
Seat:             seat0, default
Capabilities:     keyboard
Tap-to-click:     n/a
Tap-and-drag:     n/a
Tap drag lock:    n/a
Left-handed:      n/a
Nat.scrolling:    n/a
Middle emulation: n/a
Calibration:      n/a
Scroll methods:   none
Click methods:    none
Disable-w-typing: n/a
Disable-w-trackpointing: n/a
Accel profiles:   n/a
Rotation:         0.0

Device:           SynPS/2 Synaptics TouchPad
Kernel:           /dev/input/event4
Group:            6
Seat:             seat0, default
Size:             98x53mm
Capabilities:     pointer gesture
Tap-to-click:     disabled
Tap-and-drag:     enabled
Tap drag lock:    disabled
Left-handed:      disabled
Nat.scrolling:    disabled
Middle emulation: disabled
Calibration:      n/a
Scroll methods:   *two-finger edge
Click methods:    *button-areas clickfinger
Disable-w-typing: enabled
Disable-w-trackpointing: enabled
Accel profiles:   flat *adaptive custom
Rotation:         n/a

Device:           TPPS/2 Elan TrackPoint
Kernel:           /dev/input/event5
Group:            7
Seat:             seat0, default
Capabilities:     pointer
Tap-to-click:     n/a
Tap-and-drag:     n/a
Tap drag lock:    n/a
Left-handed:      disabled
Nat.scrolling:    disabled
Middle emulation: disabled
Calibration:      n/a
Scroll methods:   *button
Click methods:    none
Disable-w-typing: n/a
Disable-w-trackpointing: n/a
Accel profiles:   flat *adaptive custom
Rotation:         n/a

Device:           ThinkPad Extra Buttons
Kernel:           /dev/input/event7
Group:            8
Seat:             seat0, default
Capabilities:     keyboard
Tap-to-click:     n/a
Tap-and-drag:     n/a
Tap drag lock:    n/a
Left-handed:      n/a
Nat.scrolling:    n/a
Middle emulation: n/a
Calibration:      n/a
Scroll methods:   none
Click methods:    none
Disable-w-typing: n/a
Disable-w-trackpointing: n/a
Accel profiles:   n/a
Rotation:         0.0
```

### [Video card]

[KERNEL] **linux-6.6**

    Processor type and features  --->
        -*- MTRR (Memory Type Range Register) support
    Device Drivers  --->
        Graphics support  --->
            <*> Intel 8xx/9xx/G3x/G4x/HD Graphics
            [*]   Enable capturing GPU state following a hang
            [*]     Compress GPU error state
            [*]   Always enable userptr support

### [NVMe]

[NVMe](https://wiki.gentoo.org/wiki/NVMe "NVMe")