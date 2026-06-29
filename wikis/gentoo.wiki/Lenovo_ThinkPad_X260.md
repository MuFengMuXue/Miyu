**Resources**

[[]][Official Support Page](https://pcsupport.lenovo.com/us/en/products/laptops-and-netbooks/thinkpad-x-series-laptops/thinkpad-x260)

[[]][Specifications (by region)](https://psref.lenovo.com/Product/ThinkPad/ThinkPad_X260)

[[]][Hardware Maintenance Manual](https://download.lenovo.com/pccbbs/mobiles_pdf/x260_hmm_en_sp40j47622_02.pdf)

[[]][User Guide](https://download.lenovo.com/pccbbs/mobiles_pdf/x260_ug_en.pdf)

[[]][BIOS Setup](https://download.lenovo.com/pccbbs/mobiles_pdf/lenovo_bios_setup_linux_wmi_sysfs_1.2.pdf)

[[]][ThinkPad T series](https://en.wikipedia.org/wiki/ThinkPad_X_series#X260 "wikipedia:ThinkPad X series")

## Contents

-   [[1] [Hardware]](#Hardware)
    -   [[1.1] [Configuration]](#Configuration)
    -   [[1.2] [Ethernet]](#Ethernet)
    -   [[1.3] [Wi-Fi]](#Wi-Fi)
    -   [[1.4] [Bluetooth]](#Bluetooth)
    -   [[1.5] [USB]](#USB)
    -   [[1.6] [Video card]](#Video_card)
    -   [[1.7] [Audio card]](#Audio_card)
    -   [[1.8] [Integrated camera]](#Integrated_camera)
    -   [[1.9] [ACPI]](#ACPI)
        -   [[1.9.1] [ThinkPad ACPI]](#ThinkPad_ACPI)
    -   [[1.10] [Memory card reader]](#Memory_card_reader)
    -   [[1.11] [Synaptics Touchpad]](#Synaptics_Touchpad)
    -   [[1.12] [Fingerprint scanner]](#Fingerprint_scanner)
-   [[2] [BIOS Update]](#BIOS_Update)
-   [[3] [External resources]](#External_resources)

## [Hardware]

  --------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -------- -------------------------------------------------------------------------------------------------------------------------- --------------------------------------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------------
  Device                Make/model                                                                                                                                                                Status   Vendor ID / Product ID                                                                                                     Kernel driver(s)                                                                                                      Notes
  CPU                   Intel [i5-6300U](https://ark.intel.com/content/www/us/en/ark/products/88190/intel-core-i5-6300u-processor-3m-cache-up-to-3-00-ghz.html)   Works    N/A                                                                                                                        N/A
  SATA Controller       Intel Corporation Sunrise Point-LP SATA Controller \[AHCI mode\]                                                                                                          Works    8086:9d03                                                                                                                  AHCI
  USB                   Intel Corporation Sunrise Point-LP USB 3.0 xHCI Controller                                                                                                                Works    8086:9d2f                                                                                                                  xhci_hcd
  Video card            Intel Corporation Skylake GT2 \[HD Graphics 520\]                                                                                                                         Works    8086:1916                                                                                                                  [i915](https://wiki.gentoo.org/wiki/Intel "Intel")                                                                    [#Video_card](#Video_card)
  Audio card            Intel Corporation Sunrise Point-LP HD Audio                                                                                                                               Works    8086:9d70                                                                                                                  [snd_hda_intel](https://wiki.gentoo.org/wiki/ALSA "ALSA")                                                             [#Audio_card](#Audio_card)
  Memory card reader    RTS522A PCI Express Card Reader                                                                                                                                           Works    [10ec:522a](https://www.startpage.com/do/search?query=%2210ec:522a%22+site%3Acateee.net)   rtsx_pci                                                                                                              [#Memory_card_reader](#Memory_card_reader)
  Ethernet              Intel Corporation Ethernet Connection I219-LM                                                                                                                             Works    [8086:156f](https://cateee.net/lkddb/web-lkddb/E1000E.html)                                [e1000e](https://wiki.gentoo.org/index.php?title=E1000e&action=edit&redlink=1 "E1000e (page does not exist)")   [#Ethernet](#Ethernet)
  WLAN                  Intel Corporation Wireless 8260                                                                                                                                           Works    8086:24f3                                                                                                                  [iwlwifi](https://wiki.gentoo.org/wiki/Iwlwifi "Iwlwifi")                                                             [iwlmvm](https://wireless.wiki.kernel.org/en/users/drivers/iwlwifi?s%5b%5d=iwlmvm#firmware)
  Bluetooth             Intel Wireless Bluetooth                                                                                                                                                  Works    [8087:0a2b](https://www.startpage.com/do/search?query=%228087:0a2b%22+site%3Acateee.net)   [btusb, btintel](https://wiki.gentoo.org/wiki/Bluetooth "Bluetooth")                                                  [#Bluetooth](#Bluetooth)
  Touchpad              SynPS/2 Synaptics TouchPad                                                                                                                                                Works    [n/a](https://cateee.net/lkddb/web-lkddb/MOUSE_PS2_SYNAPTICS.html)                         MOUSE_PS2_SYNAPTICS                                                                                                   [Synaptics](https://wiki.gentoo.org/wiki/Synaptics "Synaptics"), [Libinput](https://wiki.gentoo.org/wiki/Libinput#Configuration "Libinput")
  Trackpoint            TPPS/2 IBM TrackPoint                                                                                                                                                     Works    n/a
  Fingerprint scanner   [Validity Sensors, Inc. VFS 5011 fingerprint sensor](https://devicehunt.com/view/type/usb/vendor/138A/device/0017)                        Works    138a:0017                                                                                                                  libfprint
  --------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -------- -------------------------------------------------------------------------------------------------------------------------- --------------------------------------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------------

`root `[`#`]`lspci -nnk`

    00:00.0 Host bridge [0600]: Intel Corporation Xeon E3-1200 v5/E3-1500 v5/6th Gen Core Processor Host Bridge/DRAM Registers [8086:1904] (rev 08)
            Subsystem: Lenovo Xeon E3-1200 v5/E3-1500 v5/6th Gen Core Processor Host Bridge/DRAM Registers [17aa:504a]
            Kernel driver in use: skl_uncore
    00:02.0 VGA compatible controller [0300]: Intel Corporation Skylake GT2 [HD Graphics 520] [8086:1916] (rev 07)
            Subsystem: Lenovo Skylake GT2 [HD Graphics 520] [17aa:504a]
            Kernel driver in use: i915
    00:14.0 USB controller [0c03]: Intel Corporation Sunrise Point-LP USB 3.0 xHCI Controller [8086:9d2f] (rev 21)
            Subsystem: Lenovo Sunrise Point-LP USB 3.0 xHCI Controller [17aa:504a]
            Kernel driver in use: xhci_hcd
    00:14.2 Signal processing controller [1180]: Intel Corporation Sunrise Point-LP Thermal subsystem [8086:9d31] (rev 21)
            Subsystem: Lenovo Sunrise Point-LP Thermal subsystem [17aa:504a]
            Kernel driver in use: intel_pch_thermal
            Kernel modules: intel_pch_thermal
    00:16.0 Communication controller [0780]: Intel Corporation Sunrise Point-LP CSME HECI #1 [8086:9d3a] (rev 21)
            Subsystem: Lenovo Sunrise Point-LP CSME HECI [17aa:504a]
            Kernel driver in use: mei_me
            Kernel modules: mei_me
    00:17.0 SATA controller [0106]: Intel Corporation Sunrise Point-LP SATA Controller [AHCI mode] [8086:9d03] (rev 21)
            Subsystem: Lenovo Sunrise Point-LP SATA Controller [AHCI mode] [17aa:504a]
            Kernel driver in use: ahci
    00:1c.0 PCI bridge [0604]: Intel Corporation Sunrise Point-LP PCI Express Root Port #1 [8086:9d10] (rev f1)
            Kernel driver in use: pcieport
    00:1c.2 PCI bridge [0604]: Intel Corporation Sunrise Point-LP PCI Express Root Port #3 [8086:9d12] (rev f1)
            Kernel driver in use: pcieport
    00:1f.0 ISA bridge [0601]: Intel Corporation Sunrise Point-LP LPC Controller [8086:9d48] (rev 21)
            Subsystem: Lenovo Sunrise Point-LP LPC Controller [17aa:504a]
    00:1f.2 Memory controller [0580]: Intel Corporation Sunrise Point-LP PMC [8086:9d21] (rev 21)
            Subsystem: Lenovo Sunrise Point-LP PMC [17aa:504a]
    00:1f.3 Audio device [0403]: Intel Corporation Sunrise Point-LP HD Audio [8086:9d70] (rev 21)
            Subsystem: Lenovo Sunrise Point-LP HD Audio [17aa:504a]
            Kernel driver in use: snd_hda_intel
    00:1f.4 SMBus [0c05]: Intel Corporation Sunrise Point-LP SMBus [8086:9d23] (rev 21)
            Subsystem: Lenovo Sunrise Point-LP SMBus [17aa:504a]
            Kernel driver in use: i801_smbus
    00:1f.6 Ethernet controller [0200]: Intel Corporation Ethernet Connection I219-LM [8086:156f] (rev 21)
            Subsystem: Lenovo Ethernet Connection I219-LM [17aa:2233]
            Kernel driver in use: e1000e
    02:00.0 Unassigned class [ff00]: Realtek Semiconductor Co., Ltd. RTS522A PCI Express Card Reader [10ec:522a] (rev 01)
            Subsystem: Lenovo RTS522A PCI Express Card Reader [17aa:504a]
            Kernel driver in use: rtsx_pci
            Kernel modules: rtsx_pci
    04:00.0 Network controller [0280]: Intel Corporation Wireless 8260 [8086:24f3] (rev 3a)
            Subsystem: Intel Corporation Wireless 8260 [8086:0130]
            Kernel driver in use: iwlwifi
            Kernel modules: iwlwifi

`root `[`#`]`lsusb`

    Bus 002 Device 001: ID 1d6b:0003 Linux Foundation 3.0 root hub
    Bus 001 Device 004: ID 138a:0017 Validity Sensors, Inc. VFS 5011 fingerprint sensor
    Bus 001 Device 003: ID 04f2:b52c Chicony Electronics Co., Ltd
    Bus 001 Device 002: ID 8087:0a2b Intel Corp.
    Bus 001 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub

`root `[`#`]`lsusb -t`

    /:  Bus 02.Port 1: Dev 1, Class=root_hub, Driver=xhci_hcd/6p, 5000M
    /:  Bus 01.Port 1: Dev 1, Class=root_hub, Driver=xhci_hcd/12p, 480M
        |__ Port 7: Dev 2, If 0, Class=Wireless, Driver=btusb, 12M
        |__ Port 7: Dev 2, If 1, Class=Wireless, Driver=btusb, 12M
        |__ Port 8: Dev 3, If 1, Class=Video, Driver=uvcvideo, 480M
        |__ Port 8: Dev 3, If 0, Class=Video, Driver=uvcvideo, 480M
        |__ Port 9: Dev 4, If 0, Class=Vendor Specific Class, Driver=, 12M

`root `[`#`]`lscpu`

    Architektura:           x86_64
    Tryb(y) pracy CPU:      32-bit, 64-bit
    Kolejność bajtów:       Little Endian
    Rozmiary adresów:       39 bits physical, 48 bits virtual
    CPU:                    4
    Lista aktywnych CPU:    0-3
    Wątków na rdzeń:        2
    Rdzeni na gniazdo:      2
    Gniazd:                 1
    Węzłów NUMA:            1
    ID producenta:          GenuineIntel
    Rodzina CPU:            6
    Model:                  78
    Nazwa modelu:           Intel(R) Core(TM) i5-6300U CPU @ 2.40GHz
    Wersja:                 3
    CPU MHz:                500.002
    CPU max MHz:            3000,0000
    CPU min MHz:            400,0000
    BogoMIPS:               4992.00
    Wirtualizacja:          VT-x
    Cache L1d:              32K
    Cache L1i:              32K
    Cache L2:               256K
    Cache L3:               3072K
    Procesory węzła NUMA 0: 0-3
    Flagi:                  fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush dts acpi mmx fxsr sse sse2 ss ht tm pbe syscall nx pdpe1gb rdtscp lm constant_tsc art arch_perfmon pebs bts rep_good nopl xtopology nonstop_tsc cpuid aperfmperf tsc_known_freq pni pclmulqdq dtes64 monitor ds_cpl vmx smx est tm2 ssse3 sdbg fma cx16 xtpr pdcm pcid sse4_1 sse4_2 x2apic movbe popcnt aes xsave avx f16c rdrand lahf_lm abm 3dnowprefetch cpuid_fault epb invpcid_single pti tpr_shadow vnmi flexpriority ept vpid ept_ad fsgsbase tsc_adjust bmi1 hle avx2 smep bmi2 erms invpcid rtm mpx rdseed adx smap clflushopt intel_pt xsaveopt xsavec xgetbv1 xsaves dtherm ida arat pln pts hwp hwp_notify hwp_act_window hwp_epp

`root `[`#`]`lsinput -v`

```
/dev/input/event0
   id   : 0000:0005, HOST, v0
   phys : "PNP0C0D/button/input0"
   name : "Lid Switch"
        : (null)

/dev/input/event1
   id   : 0000:0003, HOST, v0
   phys : "PNP0C0E/button/input0"
   name : "Sleep Button"
        : (null)

/dev/input/event2
   id   : 0000:0001, HOST, v0
   phys : "LNXPWRBN/button/input0"
   name : "Power Button"
        : (null)

/dev/input/event3
   id   : 0000:0006, HOST, v0
   phys : "LNXVIDEO/video/input0"
   name : "Video Bus"
        : (null) (null) (null) (null) (null) (null) (null) (null)

/dev/input/event4
   id   : 0001:0001, I8042, v43860
   phys : "isa0060/serio0/input0"
   name : "AT Translated Set 2 keyboard"
        : [ 144 codes ]
        : (null)
        : (null) (null) (null)

/dev/input/event5
   id   : 0002:0007, I8042, v433
   phys : "isa0060/serio1/input0"
   name : "SynPS/2 Synaptics TouchPad"
        : (null) (null) (null) (null) (null) (null) (null)
        : (null) (null) (null) (null) (null) (null) (null) (null) (null)

/dev/input/event6
   id   : 0000:0000, (null), v0
   phys : "ALSA"
   name : "HDA Intel PCH Mic"
        : (null)

/dev/input/event7
   id   : 0000:0000, (null), v0
   phys : "ALSA"
   name : "HDA Intel PCH Headphone"
        : (null)

/dev/input/event8
   id   : 0000:0000, (null), v0
   phys : "ALSA"
   name : "HDA Intel PCH HDMI"
        : (null) (null)

/dev/input/event9
   id   : 0002:000a, I8042, v0
   phys : "synaptics-pt/serio0/input0"
   name : "TPPS/2 IBM TrackPoint"
        : (null) (null) (null)
        : (null) (null)

/dev/input/event10
   id   : 04f2:b52c, USB, v41
   phys : "usb-0000:00:14.0-8/button"
   name : "Integrated Camera: Integrated C"
        : (null)
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
Accel profiles:   n/a
Rotation:         n/a

Device:           Video Bus
Kernel:           /dev/input/event3
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
Accel profiles:   n/a
Rotation:         n/a

Device:           Lid Switch
Kernel:           /dev/input/event0
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
Accel profiles:   n/a
Rotation:         n/a

Device:           Sleep Button
Kernel:           /dev/input/event1
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
Accel profiles:   n/a
Rotation:         n/a

Device:           Integrated Camera: Integrated C
Kernel:           /dev/input/event10
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
Accel profiles:   n/a
Rotation:         n/a

Device:           HDA Intel PCH HDMI
Kernel:           /dev/input/event8
Group:            6
Seat:             seat0, default
Capabilities:
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
Accel profiles:   n/a
Rotation:         n/a

Device:           HDA Intel PCH Mic
Kernel:           /dev/input/event6
Group:            6
Seat:             seat0, default
Capabilities:
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
Accel profiles:   n/a
Rotation:         n/a

Device:           HDA Intel PCH Headphone
Kernel:           /dev/input/event7
Group:            6
Seat:             seat0, default
Capabilities:
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
Accel profiles:   n/a
Rotation:         n/a

Device:           AT Translated Set 2 keyboard
Kernel:           /dev/input/event4
Group:            7
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
Accel profiles:   n/a
Rotation:         n/a

Device:           SynPS/2 Synaptics TouchPad
Kernel:           /dev/input/event5
Group:            8
Seat:             seat0, default
Size:             85x51mm
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
Accel profiles:   none
Rotation:         n/a

Device:           TPPS/2 IBM TrackPoint
Kernel:           /dev/input/event9
Group:            9
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
Accel profiles:   flat *adaptive
Rotation:         n/a
```

### [Configuration]

[FILE] **`/etc/portage/make.conf`**

    CHOST="x86_64-pc-linux-gnu"
    COMMON_FLAGS="-march=skylake -O2 -pipe"

    VIDEO_CARDS="intel i965"

    INPUT_DEVICES="synaptics libinput"

[FILE] **`/etc/portage/package.use/00cpi-flags`**

    # generated by cpuid2cpuflags
    */*  CPU_FLAGS_X86: aes avx avx2 f16c fma3 mmx mmxext pclmul popcnt sse sse2 sse3 sse4_1 sse4_2 ssse3

### [Ethernet]

[KERNEL] **linux-4.19**

    Device Drivers  --->
        [*] Network device support  --->
            [*]   Ethernet driver support  --->
                [*]   Intel devices
                <*>     Intel(R) PRO/1000 PCI-Express Gigabit Ethernet support
                [*]       Support HW cross-timestamp on PCH devices

### [Wi-Fi]

[Iwlwifi](https://wiki.gentoo.org/wiki/Iwlwifi "Iwlwifi")

### [Bluetooth]

USB ID 8087:0a2b Intel Corp.

[KERNEL] **linux-4.19**

    [*] Networking support  --->
        <M>   Bluetooth subsystem support  --->
            Bluetooth device drivers  --->
                <*> HCI USB driver
                [*]   Broadcom protocol support (NEW)

### [USB]

[KERNEL] **linux-4.19**

    Device Drivers  --->
        HID support  --->
            -*- HID bus support
            [*]   Battery level reporting for HID devices
            [*]   /dev/hidraw raw HID device support
            < >   User-space I/O driver support for HID subsystem
            <*>   Generic HID driver
            USB HID support  --->
                 <*> USB HID transport layer
                 [*] PID device support
                 [*] /dev/hiddev raw HID device support
        [*] USB support  --->
            <*>   xHCI HCD (USB 3.0) support
            <*>   EHCI HCD (USB 2.0) support
            <*>   OHCI HCD (USB 1.1) support

### [Video card]

[KERNEL] **linux-4.19**

    Processor type and features  --->
        -*- MTRR (Memory Type Range Register) support
    Device Drivers  --->
        Graphics support  --->
            <*> Intel 8xx/9xx/G3x/G4x/HD Graphics
            [*]   Enable capturing GPU state following a hang
            [*]     Compress GPU error state
            [*]   Always enable userptr support

### [Audio card]

[KERNEL] **linux-5.15**

    General setup  --->
        Timers subsystem  --->
            [*] High Resolution Timer Support
    Device Drivers  --->
        <*> Sound card support  --->
            <*>   Advanced Linux Sound Architecture  --->
                 HD-Audio  --->
                     <*> HD Audio PCI
                     [*] Build hwdep interface for HD-audio driver
                     -*- Allow dynamic codec reconfiguration
                     [*] Support initialization patch loading for HD-audio
                     <*> Build HDMI/DisplayPort HD-audio codec support
                     <*> Build Conexant HD-audio codec support
                     -*- Enable generic HD-audio codec parser
                         (0) Default time-out for HD-audio power-save mode

### [Integrated camera]

USB ID 04f2:b52c Chicony Electronics Co., Ltd

[KERNEL] **linux-4.19**

    Device Drivers  --->
        <M> Multimedia support  --->
            [*]   Cameras/video grabbers support
            [*]   Media USB Adapters  --->
                <M>   USB Video Class (UVC)
                [*]     UVC input events device support (NEW)

### [ACPI]

[KERNEL] **linux-4.19**

    Device Drivers  --->
        -*- Hardware Monitoring support  --->
            <M>   Intel Core/Core2/Atom temperature sensor
        -*- Generic Thermal sysfs driver  --->
            <M>   X86 package temperature thermal driver
            <M>   Intel PCH Thermal Reporting Driver
        [*] X86 Platform Specific Device Drivers  --->
            <M>   Intel PMC Core driver
        Misc devices  --->
             Intel Management Engine Interface
            <M> ME Enabled Intel Chipsets

#### [ThinkPad ACPI]

[KERNEL] **linux-4.19**

    Device Drivers  --->
        [*] X86 Platform Specific Device Drivers  --->
            <M>   ThinkPad ACPI Laptop Extras
            [*]     Support NVRAM polling for hot keys (NEW)

`root `[`#`]`emerge --ask --verbose lm-sensors`

`root `[`#`]`sensors-detect`

`user `[`$`]`sensors`

`user `[`$`]`sensors`

```
iwlwifi-virtual-0
Adapter: Virtual device
temp1:        +34.0°C

acpitz-acpi-0
Adapter: ACPI interface
temp1:        +44.0°C  (crit = +128.0°C)

thinkpad-isa-0000
Adapter: ISA adapter
fan1:           0 RPM

coretemp-isa-0000
Adapter: ISA adapter
Package id 0:  +44.0°C  (high = +100.0°C, crit = +100.0°C)
Core 0:        +42.0°C  (high = +100.0°C, crit = +100.0°C)
Core 1:        +42.0°C  (high = +100.0°C, crit = +100.0°C)

pch_skylake-virtual-0
Adapter: Virtual device
temp1:        +42.5°C
```

### [Memory card reader]

[KERNEL] **linux-4.19**

    Device Drivers  --->
        Misc devices  --->
            <M> Realtek PCI-E card reader
        <M> MMC/SD/SDIO card support  --->
            <M>   Secure Digital Host Controller Interface support
            <M>   Realtek PCI-E SD/MMC Card Interface Driver

### [Synaptics Touchpad]

[KERNEL] **linux-4.19**

    Device Drivers  --->
        Input device support  --->
            <*>   Event interface
            [*]   Mice  --->
                <M>   PS/2 mouse

[FILE] **`/etc/X11/x.org.conf.d/50-synaptics.conf`**

    Section "InputClass"
      Identifier      "Synaptics Touchpad"
      Driver          "synaptics"
      MatchIsTouchpad "on"
      Option          "VertEdgeScroll"        "on"
      Option          "CircularScrolling"     "on"
      Option          "VertTwoFingerScroll"   "on"
      Option          "HorizTwoFingerScroll"  "on"
      Option          "TapButton1"            "1"
      Option          "TapButton2"            "3"
      Option          "TapButton3"            "2"
    EndSection

\

### [Fingerprint scanner]

USB: 138a:0017 Validity Sensors, Inc. VFS 5011 fingerprint sensor

`root `[`#`]`emerge --ask fprintd`

IMO it is not good idea to login into computer with it, but yes... it works at least with [Gnome](https://help.gnome.org/users/gnome-help/stable/session-fingerprint.html.en).

## [BIOS Update]

Download bootable CD image from [Lenovo ThinkPad X260 BIOS/UEFI](https://pcsupport.lenovo.com/us/en/products/laptops-and-netbooks/thinkpad-x-series-laptops/thinkpad-x260/downloads/driver-list/component?name=BIOS%2FUEFI).

`root `[`#`]`ACCEPT_KEYWORDS="~amd64" emerge -av1 geteltorito`

`user `[`$`]`geteltorito -o bios.bin r02uj72d.iso`

Write bios.bin file to your USB stick.

`root `[`#`]`dd if=bios.bin of=/dev/sdX bs=4M status=progress`

Now boot, from prepared USB stick, follow instructions. Than boot into new BIOS, reset all options to defaults, and set them as you like again.

## [External resources]

-   [https://www.thinkwiki.org/wiki/Category:X260](https://www.thinkwiki.org/wiki/Category:X260)
-   [https://www.thinkwiki.org/wiki/Thinkpad-acpi](https://www.thinkwiki.org/wiki/Thinkpad-acpi)
-   [https://en.wikipedia.org/wiki/ThinkPad_X_series#X260](https://en.wikipedia.org/wiki/ThinkPad_X_series#X260)