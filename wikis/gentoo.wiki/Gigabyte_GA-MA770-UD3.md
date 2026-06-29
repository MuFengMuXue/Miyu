**Resources**

[[]][Home](https://www.gigabyte.com/Motherboard/GA-MA770-UD3-rev-10)

## Contents

-   [[1] [General Information]](#General_Information)
-   [[2] [Hardware Specs]](#Hardware_Specs)
-   [[3] [Kernel Configuration]](#Kernel_Configuration)
    -   [[3.1] [CPU]](#CPU)
    -   [[3.2] [Disks]](#Disks)
    -   [[3.3] [Sound]](#Sound)
    -   [[3.4] [Ethernet]](#Ethernet)
    -   [[3.5] [Peripherals]](#Peripherals)
    -   [[3.6] [Sensors]](#Sensors)
-   [[4] [Other details]](#Other_details)
    -   [[4.1] [lspci output]](#lspci_output)
    -   [[4.2] [Known hardware issues]](#Known_hardware_issues)

## [General Information]

The GA-MA770-UD3 is an AMD motherboard with an AM2+ socket and SB700 chipset. This page details the rev 1.0 hardware; there are also 2.0 and 2.1 variants with minor updates.

## [Hardware Specs]

+-----------------------------------+--------------------------------------------------------------------------------------------------------------------------+
| CPU Support                       | AM2/AM2+/AM3 (amdfam10h; up to Phenom II X6 1090T)                                                                       |
+-----------------------------------+--------------------------------------------------------------------------------------------------------------------------+
| Memory                            | 4× DDR 2 slots, maximum 16GB DDR2-1200+                                                                                  |
+-----------------------------------+--------------------------------------------------------------------------------------------------------------------------+
| Expansion Slots                   | -   1× PCIe 2.0 x16                                                                                                      |
|                                   | -   4× PCIe 2.0 x1                                                                                                       |
|                                   | -   2× PCI slots                                                                                                         |
+-----------------------------------+--------------------------------------------------------------------------------------------------------------------------+
| Internal Storage                  | -   6× SATA 3Gbit/s                                                                                                      |
|                                   | -   1× PATA ATA-133                                                                                                      |
|                                   | -   1× floppy disk controller                                                                                            |
|                                   | -   BIOS fake-RAID support                                                                                               |
+-----------------------------------+--------------------------------------------------------------------------------------------------------------------------+
| Connectivity                      | -   8× USB 2.0 on rear panel, 4× internal headers                                                                        |
|                                   | -   2× IEEE1394 (FireWire) on rear panel (4 and 6 pin), 1 internal header                                                |
|                                   | -   PS/2 mouse and keyboard ports                                                                                        |
|                                   | -   RTL8168 Gigabit ethernet                                                                                             |
|                                   | -   Realtek HDA audio: 6-channel PCM + coaxial SPDIF + optical SPDIF on rear panel, front mic/headphone internal headers |
+-----------------------------------+--------------------------------------------------------------------------------------------------------------------------+

## [Kernel Configuration]

### [CPU]

[KERNEL]

    [*] 64-bit kernel
    Processor type and features  --->
        [*] Symmetric multi-processing support
        [*] Avoid speculative indirect branches in kernel
        Processor family (AMD 61xx/7x50/PhenomX3/X4/II/K10)
        [*] Machine Check / overheating reporting
            [*]   AMD MCE features
        [*] MTRR (Memory Type Range Register) support
            [*]   x86 PAT support
    Power management and ACPI options  --->
        CPU Frequency scaling  --->
            Default CPUFreq governor (schedutil)
            <*>   ACPI Processor P-States driver

### [Disks]

[KERNEL] **: Advanced Micro Devices, Inc. \[AMD/ATI\] SB7x0/SB8x0/SB9x0 **

    Device Drivers  --->
        <*> Serial ATA and Parallel ATA drivers (libata)  --->
            <*>   AHCI SATA support
            [*]   ATA SFF support
            [*]     ATA BMDMA support
            <*>     Intel ESB, ICH, PIIX3, PIIX4 PATA/SATA support

Floppy disk support is there, if needed:

[KERNEL] **00:14.3 ISA bridge: Advanced Micro Devices, Inc. \[AMD/ATI\] SB7x0/SB8x0/SB9x0 LPC host controller**

    Device Drivers  --->
        [*] Block devices  --->
            <*>   Normal floppy disk support

### [Sound]

[KERNEL]

    Device Drivers  --->
        <*> Sound Card Support  --->
            <*> Advanced Linux Sound Architecture  --->
                HD-Audio  --->
                    <*> HD Audio PCI
                    <*> Build Realtek HD-audio codec support

### [Ethernet]

[KERNEL] **02:00.0 Ethernet controller: Realtek Semiconductor Co., Ltd. RTL8111/8168/8411 PCI Express Gigabit Ethernet Controller (rev 02)**

    Device Drivers  --->
        Networking support  --->
            [*] Network device support  --->
                [*] Ethernet driver support  --->
                    [*]   Realtek devices
                    <*>     Realtek 8169 gigabit ethernet support

### [Peripherals]

[KERNEL]

    Device Drivers  --->
        [*] USB support  --->
            <*>   Support for Host-side USB
            [*]   PCI based USB host interface
            <*>     EHCI HCD (USB 2.0) support
                [*]     Root Hub Transaction Translators
                [*]     Improved Transaction Translator scheduling
            <*>     OHCI HCD (USB 1.1) support
                <*>     OHCI support for PCI-bus USB controllers
        IEEE 1394 (FireWire) support  --->
            <*> FireWire driver stack
            <*>   OHCI-1394 controllers

### [Sensors]

[KERNEL]

    Device Drivers --->
        I2C support  --->
            <*>   I2C device interface
            [*]   Autoselect pertinent helper modules
            I2C Hardware Bus support  --->
                <*> Intel PIIX4 and compatible (ATI/AMD/Serverworks/Broadcom/SMSC)
        -*- Hardware Monitoring support  --->
            <?>   AMD Family 10h+ temperature sensor
            <*>   ITE IT87xx and compatibles

Many AMD Family 10h (i.e. Athlon/Phenom II) chips have a faulty temperature sensor. It\'s safe to enable the driver here, but the kernel will detect affected CPUs and disable it automatically for them. In that case there\'s no reason to leave it enabled at all.

lm-sensors doesn\'t have an upstream config file for this chipset; the following is a best-effort attempt to write one:

[FILE] **`/etc/sensors.d/it8720-GA-MA770-UD3.conf`lm-sensors config file**

    # Partial Gigabyte GA-MA770-UD3 config file for lm-sensors 3, 2019-12-20
    chip "it8720-*"
        ## Fans
        # These are the labels as printed on the motherboard
        label   fan1    "CPU Fan"
        label   fan2    "Sys Fan"
        label   fan3    "Sys Fan 2"
        label   fan5    "PSU Fan"

        ## Temperatures
        label   temp1   "Sys Temp" # idle temp is 38°C, may need offset
        label   temp2   "CPU Temp" # idle temp is 45°C, ditto
        ignore  temp3   # stuck at 80°C, probably disconnected

        ## Local settings - adjust these yourself!
        set     fan1_min    0   # BIOS sets non-zero
        ignore  fan3        # not present
        ignore  fan5        # not present
        set     temp1_min   25
        set     temp1_max   45
        set     temp2_min   35
        set     temp2_max   65

        ## Voltages
        # These settings were hacked together from bits and pieces of user-submitted
        # config files from similar 770/870 boards (mostly MA770-DS3) here:
        # https://github.com/lm-sensors/lm-sensors/blob/master/configs/Gigabyte/
        # While none of them are a perfect match, it does help significantly.

        ignore  in0     # 1.30V, never changes
        label   in1     "DDR2 1.8V"
        label   in2     "+3.3V"     # suspect, never changes from exactly 3.34V
        label   in3     "+5V"
        label   in4     "+12V"      # DS3's 12V in6 lines seem to work here
        label   in5     "Vcore?"
        ignore  in6     # duplicate of in2?
        label   in7     "5VSB"      # the kernel's it87 driver sets this for us
        label   in8     "Vbat"

        set     in1_min 1.8 * 0.95
        set     in1_max 1.8 * 1.05

        set     in2_min 3.3 * 0.95
        set     in2_max 3.3 * 1.05

        compute in3     @ * ((6.8/10)+1),   @ / ((6.8/10)+1)
        set     in3_min 5 * 0.95
        set     in3_max 5 * 1.05

        compute in4     @ * ((30/10)+1),    @ / ((30/10)+1)
        set     in4_min 12 * 0.95
        set     in4_max 12 * 1.05

        # Unknown, but probably Vcore - seems directly proportional to CPU load.
        # 4 idle cores have this reading around 1.5, fully loaded as high as 2.2
        set     in5_min 1.5 * 0.95
        set     in5_max 2.1 * 1.05

        compute in7     @ * ((6.8/10)+1),   @ / ((6.8/10)+1)
        set     in7_min 5 * 0.95
        set     in7_max 5 * 1.05

        ## Other
        ignore  cpu0_vid    # probably correct (1.250V), but static so not useful
        ignore  intrusion0  # nobody uses these things…

Sensor output with the above configuration:

`user `[`$`]`sensors | sed -n '/it87/,/^ }$/ p'`

    it8720-isa-0228
    Adapter: ISA adapter
    DDR2 1.8V:     1.82 V  (min =  +1.71 V, max =  +1.89 V)
    +3.3V:         3.34 V  (min =  +3.14 V, max =  +3.47 V)
    +5V:           5.03 V  (min =  +4.76 V, max =  +5.24 V)
    +12V:         12.35 V  (min = +11.39 V, max = +12.61 V)
    Vcore?:        1.65 V  (min =  +1.42 V, max =  +2.21 V)
    5VSB:          4.97 V  (min =  +4.76 V, max =  +5.24 V)
    Vbat:          3.14 V
    CPU Fan:     1527 RPM  (min =    0 RPM)
    Sys Fan:     1584 RPM  (min =    0 RPM)
    Sys Temp:     +37.0°C  (low  = +28.0°C, high = +48.0°C)  sensor = thermistor
    CPU Temp:     +45.0°C  (low  = +25.0°C, high = +65.0°C)  sensor = thermal diode

The raw unfiltered sensor values for reference:

`user `[`$`]`sensors -jc /dev/null | sed -n '/it87/,/^ }$/ p'`

       "it8720-isa-0228":,
          "in1":,
          "in2":,
          "+5V":,
          "in4":,
          "in5":,
          "in6":,
          "5VSB":,
          "Vbat":,
          "fan1":,
          "fan2":,
          "fan3":,
          "fan5":,
          "temp1":,
          "temp2":,
          "temp3":,
          "cpu0_vid":,
          "intrusion0":
       }

## [Other details]

### [lspci output]

[CODE] **lspci -k**

    00:00.0 Host bridge: Advanced Micro Devices, Inc. [AMD/ATI] RX780/RX790 Host Bridge
            Subsystem: Advanced Micro Devices, Inc. [AMD/ATI] RX780/RX790 Host Bridge
    00:02.0 PCI bridge: Advanced Micro Devices, Inc. [AMD/ATI] RX780/RD790 PCI to PCI bridge (external gfx0 port A)
            Kernel driver in use: pcieport
    00:0a.0 PCI bridge: Advanced Micro Devices, Inc. [AMD/ATI] RD790 PCI to PCI bridge (PCI express gpp port F)
            Kernel driver in use: pcieport
    00:11.0 SATA controller: Advanced Micro Devices, Inc. [AMD/ATI] SB7x0/SB8x0/SB9x0 SATA Controller [AHCI mode]
            Subsystem: Gigabyte Technology Co., Ltd Device b002
            Kernel driver in use: ahci
    00:12.0 USB controller: Advanced Micro Devices, Inc. [AMD/ATI] SB7x0/SB8x0/SB9x0 USB OHCI0 Controller
            Subsystem: Gigabyte Technology Co., Ltd Device 5004
            Kernel driver in use: ohci-pci
    00:12.1 USB controller: Advanced Micro Devices, Inc. [AMD/ATI] SB7x0 USB OHCI1 Controller
            Subsystem: Gigabyte Technology Co., Ltd Device 5004
            Kernel driver in use: ohci-pci
    00:12.2 USB controller: Advanced Micro Devices, Inc. [AMD/ATI] SB7x0/SB8x0/SB9x0 USB EHCI Controller
            Subsystem: Gigabyte Technology Co., Ltd Device 5004
            Kernel driver in use: ehci-pci
    00:13.0 USB controller: Advanced Micro Devices, Inc. [AMD/ATI] SB7x0/SB8x0/SB9x0 USB OHCI0 Controller
            Subsystem: Gigabyte Technology Co., Ltd Device 5004
            Kernel driver in use: ohci-pci
    00:13.1 USB controller: Advanced Micro Devices, Inc. [AMD/ATI] SB7x0 USB OHCI1 Controller
            Subsystem: Gigabyte Technology Co., Ltd Device 5004
            Kernel driver in use: ohci-pci
    00:13.2 USB controller: Advanced Micro Devices, Inc. [AMD/ATI] SB7x0/SB8x0/SB9x0 USB EHCI Controller
            Subsystem: Gigabyte Technology Co., Ltd Device 5004
            Kernel driver in use: ehci-pci
    00:14.0 SMBus: Advanced Micro Devices, Inc. [AMD/ATI] SBx00 SMBus Controller (rev 3c)
            Subsystem: Gigabyte Technology Co., Ltd GA-MA770-DS3rev2.0 Motherboard
            Kernel modules: i2c_piix4
    00:14.1 IDE interface: Advanced Micro Devices, Inc. [AMD/ATI] SB7x0/SB8x0/SB9x0 IDE Controller
            Subsystem: Gigabyte Technology Co., Ltd Device 5002
            Kernel driver in use: pata_atiixp
    00:14.2 Audio device [0403]: Advanced Micro Devices, Inc. [AMD/ATI] SBx00 Azalia (Intel HDA) [1002:4383]
            Subsystem: Gigabyte Technology Co., Ltd GA-MA770-DS3rev2.0 Motherboard [1458:a022]
            Kernel driver in use: snd_hda_intel
            Kernel modules: snd_hda_intel
    00:14.3 ISA bridge: Advanced Micro Devices, Inc. [AMD/ATI] SB7x0/SB8x0/SB9x0 LPC host controller
            Subsystem: Advanced Micro Devices, Inc. [AMD/ATI] SB7x0/SB8x0/SB9x0 LPC host controller
    00:14.4 PCI bridge: Advanced Micro Devices, Inc. [AMD/ATI] SBx00 PCI to PCI Bridge
    00:14.5 USB controller: Advanced Micro Devices, Inc. [AMD/ATI] SB7x0/SB8x0/SB9x0 USB OHCI2 Controller
            Subsystem: Gigabyte Technology Co., Ltd Device 5004
            Kernel driver in use: ohci-pci
    00:18.0 Host bridge: Advanced Micro Devices, Inc. [AMD] Family 10h Processor HyperTransport Configuration
    00:18.1 Host bridge: Advanced Micro Devices, Inc. [AMD] Family 10h Processor Address Map
    00:18.2 Host bridge: Advanced Micro Devices, Inc. [AMD] Family 10h Processor DRAM Controller
    00:18.3 Host bridge: Advanced Micro Devices, Inc. [AMD] Family 10h Processor Miscellaneous Control
    00:18.4 Host bridge: Advanced Micro Devices, Inc. [AMD] Family 10h Processor Link Control
    02:00.0 Ethernet controller: Realtek Semiconductor Co., Ltd. RTL8111/8168/8411 PCI Express Gigabit Ethernet Controller (rev 02)
            Subsystem: Gigabyte Technology Co., Ltd Onboard Ethernet
            Kernel driver in use: r8169
    03:0e.0 FireWire (IEEE 1394) [0c00]: Texas Instruments TSB43AB23 IEEE-1394a-2000 Controller (PHY/Link) [104c:8024]
            Subsystem: Gigabyte Technology Co., Ltd Motherboard [1458:1000]
            Kernel driver in use: firewire-ohci
            Kernel modules: firewire-ohci

Some of these can be disabled in the BIOS, in which case they won\'t appear here at all.

### [Known hardware issues]

-   The ethernet chip may forget its speed over a suspend and default to 100Mbit after resume. To work around this, put [ethtool -s eth0 speed 1000] in the appropriate place in your suspend scripts.
-   Most AMD family 10h CPUs have a processor erratum related to the temperature sensor\'s unreliability, which is why the driver is disabled above.
-   The SB700 chipset is affected by a kernel quirk that prevents it using message-signalled interrupts due to the possibility of data corruption when a floppy drive is used. There\'s a [patch on the Gentoo forums](https://forums.gentoo.org/viewtopic-t-905708.html) (updated version [here](https://forums.gentoo.org/viewtopic-p-7874714.html#7874714)) to disable the kernel\'s workarounds, which may or may not improve performance slightly.