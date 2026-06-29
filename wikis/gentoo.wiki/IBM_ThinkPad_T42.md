**Resources**

[[]][Home](http://support.lenovo.com/us/en/products/laptops-and-netbooks/thinkpad-t-series-laptops/thinkpad-t42)

It is an old IBM ThinkPad T42, at the year of writing of this article it is 12 years old. It\'s a good piece of hardware, good quality, great keyboard. Overall a very good laptop. Nowadays it is working as a metronome, sequencer and small synthesizer.

## Contents

-   [[1] [Hardware]](#Hardware)
-   [[2] [CPU]](#CPU)
-   [[3] [Synaptics]](#Synaptics)
    -   [[3.1] [Emerge]](#Emerge)
    -   [[3.2] [Configuration]](#Configuration)
-   [[4] [Wired NIC]](#Wired_NIC)
-   [[5] [Wireless NIC]](#Wireless_NIC)
    -   [[5.1] [Emerge]](#Emerge_2)
-   [[6] [Configuration]](#Configuration_2)
    -   [[6.1] [package.use]](#package.use)
-   [[7] [External resources]](#External_resources)

## [Hardware]

Hardware list with corresponding kernel modules and its names:

`root `[`#`]`lspci -k`

    0:00.0 Host bridge: Intel Corporation 82855PM Processor to I/O Controller (rev 03)
            Subsystem: IBM Thinkpad T40 series
    00:01.0 PCI bridge: Intel Corporation 82855PM Processor to AGP Controller (rev 03)
    00:1d.0 USB controller: Intel Corporation 82801DB/DBL/DBM (ICH4/ICH4-L/ICH4-M) USB UHCI Controller #1 (rev 01)
            Subsystem: IBM ThinkPad
            Kernel driver in use: uhci_hcd
    00:1d.1 USB controller: Intel Corporation 82801DB/DBL/DBM (ICH4/ICH4-L/ICH4-M) USB UHCI Controller #2 (rev 01)
            Subsystem: IBM ThinkPad
            Kernel driver in use: uhci_hcd
    00:1d.2 USB controller: Intel Corporation 82801DB/DBL/DBM (ICH4/ICH4-L/ICH4-M) USB UHCI Controller #3 (rev 01)
            Subsystem: IBM ThinkPad
            Kernel driver in use: uhci_hcd
    00:1d.7 USB controller: Intel Corporation 82801DB/DBM (ICH4/ICH4-M) USB2 EHCI Controller (rev 01)
            Subsystem: IBM ThinkPad
            Kernel driver in use: ehci-pci
    00:1e.0 PCI bridge: Intel Corporation 82801 Mobile PCI Bridge (rev 81)
    00:1f.0 ISA bridge: Intel Corporation 82801DBM (ICH4-M) LPC Interface Bridge (rev 01)
    00:1f.1 IDE interface: Intel Corporation 82801DBM (ICH4-M) IDE Controller (rev 01)
            Subsystem: IBM ThinkPad
            Kernel driver in use: ata_piix
    00:1f.3 SMBus: Intel Corporation 82801DB/DBL/DBM (ICH4/ICH4-L/ICH4-M) SMBus Controller (rev 01)
            Subsystem: IBM ThinkPad
            Kernel driver in use: i801_smbus
    00:1f.5 Multimedia audio controller: Intel Corporation 82801DB/DBL/DBM (ICH4/ICH4-L/ICH4-M) AC'97 Audio Controller (rev 01)
            Subsystem: IBM ThinkPad T4x Series
            Kernel driver in use: snd_intel8x0
    00:1f.6 Modem: Intel Corporation 82801DB/DBL/DBM (ICH4/ICH4-L/ICH4-M) AC'97 Modem Controller (rev 01)
            Subsystem: IBM ThinkPad R50e
            Kernel driver in use: snd_intel8x0m
    01:00.0 VGA compatible controller: Advanced Micro Devices, Inc. [AMD/ATI] RV200/M7 [Mobility Radeon 7500]
            Subsystem: IBM ThinkPad T4x Series
            Kernel driver in use: radeonfb
    02:00.0 CardBus bridge: Texas Instruments PCI4520 PC card Cardbus Controller (rev 01)
            Subsystem: IBM ThinkPad
            Kernel driver in use: yenta_cardbus
    02:00.1 CardBus bridge: Texas Instruments PCI4520 PC card Cardbus Controller (rev 01)
            Subsystem: IBM ThinkPad
            Kernel driver in use: yenta_cardbus
    02:01.0 Ethernet controller: Intel Corporation 82540EP Gigabit Ethernet Controller (Mobile) (rev 03)
            Subsystem: IBM Thinkpad
            Kernel driver in use: e1000
    02:02.0 Network controller: Intel Corporation PRO/Wireless 2915ABG [Calexico2] Network Connection (rev 05)
            Subsystem: Intel Corporation PRO/Wireless 2915ABG [Calexico2] Network Connection
            Kernel driver in use: ipw2200
            Kernel modules: ipw2200

## [CPU]

`user `[`$`]`cat /proc/cpuinfo`

    processor       : 0
    vendor_id       : GenuineIntel
    cpu family      : 6
    model           : 13
    model name      : Intel(R) Pentium(R) M processor 1.70GHz
    stepping        : 6
    microcode       : 0x18
    cpu MHz         : 1700.000
    cache size      : 2048 KB
    physical id     : 0
    siblings        : 1
    core id         : 0
    cpu cores       : 1
    apicid          : 0
    initial apicid  : 0
    fdiv_bug        : no
    f00f_bug        : no
    coma_bug        : no
    fpu             : yes
    fpu_exception   : yes
    cpuid level     : 2
    wp              : yes
    flags           : fpu vme de pse tsc msr mce cx8 sep mtrr pge mca cmov clflush dts acpi mmx fxsr sse sse2 ss tm pbe bts est tm2
    bugs            :
    bogomips        : 3388.71
    clflush size    : 64
    cache_alignment : 64
    address sizes   : 32 bits physical, 32 bits virtual
    power management:

`user `[`$`]`lscpu`

    Architecture:          i686
    CPU op-mode(s):        32-bit
    Byte Order:            Little Endian
    CPU(s):                1
    On-line CPU(s) list:   0
    Thread(s) per core:    1
    Core(s) per socket:    1
    Socket(s):             1
    Vendor ID:             GenuineIntel
    CPU family:            6
    Model:                 13
    Model name:            Intel(R) Pentium(R) M processor 1.70GHz
    Stepping:              6
    CPU MHz:               1700.000
    CPU max MHz:           1700.0000
    CPU min MHz:           600.0000
    BogoMIPS:              3388.71

## [Synaptics]

[KERNEL] **Synaptics PS/2 mouse protocol extension**

    Device Drivers --->
       Input device support  --->
          [*] Mice  --->
             <*> PS/2 mouse

### [Emerge]

`root `[`#`]`emerge --ask x11-drivers/xf86-input-synaptics`

### [Configuration]

[FILE] **`/etc/X11/xorg.conf.d/50-synaptics.conf`Synaptics enhanced configuration**

    Section "InputDevice"
            identifier      "touchpad0"
            driver          "synaptics"
            option          "AutoServerLayout" "on"

            # Some extra options for touchpad.
            Option  "LeftEdge"      "1700"
            Option  "RightEdge"     "5300"
            Option  "TopEdge"       "1700"
            Option  "BottomEdge"    "4200"
            Option  "FingerLow"     "25"
            Option  "FingerHigh"    "30"
            Option  "MaxTapTime"    "180"
            Option  "MaxTapMove"    "220"
            Option  "MinSpeed"      "0.7"
            Option  "MaxSpeed"      "0.8"
            Option  "AccelFactor"   "0.0010"
            Option  "SHMConfig"     "on"
            Option  "TapButton1"    "1"
            Option  "VertTwoFingerScroll"   "1"
            Option  "HorizTwoFingerScroll"  "1"
            Option  "VertScrollDelta"       "100"
    EndSection

## [Wired NIC]

[KERNEL] **Intel(R) PRO/1000 Gigabit Ethernet support**

    [*]  Networking support  --->
        [*]  Ethernet driver support  --->
            [*]   Intel devices
            <*>     Intel(R) PRO/1000 Gigabit Ethernet support

## [Wireless NIC]

Needed to be build as a module (`<M>`).

[KERNEL] **Intel PRO/Wireless 2200BG and 2915ABG Network Connection**

    [*]  Networking support  --->
         -*- Wireless  --->
             <M>   cfg80211 - wireless configuration API
             [*]     enable powersave by default
             <M>   Generic IEEE 802.11 Networking Stack (mac80211)

    Device Drivers  --->
       [*]   Network device support  --->
             [*] Wireless LAN  --->
                 <M>   Intel PRO/Wireless 2200BG and 2915ABG Network Connection

### [Emerge]

Wireless NIC kernel firmware:

`root `[`#`]`emerge --ask sys-firmware/ipw2200-firmware`

## [Configuration]

### [package.use]

[FILE] **`/etc/portage/make.conf`**

    CHOST="i686-pc-linux-gnu"
    CFLAGS="-O2 -march=pentium-m -pipe -fomit-frame-pointer"
    CXXFLAGS="$"

    MAKEOPTS="-j2"

[FILE] **`/etc/portage/package.use/00video`**

    */* VIDEO_CARDS: -* radeon intel i915

[FILE] **`/etc/portage/package.use/00input`**

    */* INPUT_DEVICES: evdev synaptics

[FILE] **`/etc/portage/package.use/00cpu-flags`**

    */* CPU_FLAGS_X86: mmx mmext sse sse2

## [External resources]

-   [\[1\]](http://www.thinkwiki.org/wiki/Category:T42)