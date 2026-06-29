[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=Razer_Blade_Pro_(2019)&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

**Resources**

[[]][Home](https://www.razer.com/eu-en/gaming-laptops/razer-blade-pro/)

This page describes the installation of Gentoo Linux on a mid-2019 Razer Blade Pro 17 FHD laptop.

## Contents

-   [[1] [Hardware]](#Hardware)
    -   [[1.1] [Standard]](#Standard)
    -   [[1.2] [Detailed information]](#Detailed_information)
-   [[2] [Installation]](#Installation)
    -   [[2.1] [Firmware]](#Firmware)
    -   [[2.2] [Kernel]](#Kernel)
-   [[3] [Configuration]](#Configuration)
    -   [[3.1] [Xorg]](#Xorg)
        -   [[3.1.1] [Touchpad]](#Touchpad)
        -   [[3.1.2] [Graphics]](#Graphics)
        -   [[3.1.3] [External graphics]](#External_graphics)
    -   [[3.2] [Fan control, RGB keyboard effects and gaming mode]](#Fan_control.2C_RGB_keyboard_effects_and_gaming_mode)
    -   [[3.3] [Power management]](#Power_management)
        -   [[3.3.1] [PowerTOP]](#PowerTOP)
        -   [[3.3.2] [DPMS]](#DPMS)
        -   [[3.3.3] [NVIDIA]](#NVIDIA)
        -   [[3.3.4] [Bluetooth]](#Bluetooth)
-   [[4] [Troubleshooting]](#Troubleshooting)
    -   [[4.1] [No sound]](#No_sound)
-   [[5] [External resources]](#External_resources)

## [Hardware]

** Note**\
\* Disassembly requires a T5 Torx screwdriver.

-   The laptop has a spare M.2 slot in which an extra NVMe disk can be installed.

### [Standard]

  -------------- -------------------------------------------------------------------------- -------- ------------------------ ------------------- ---------------- -------
  Device         Make/model                                                                 Status   Vendor ID / Product ID   Kernel driver(s)    Kernel version   Notes
  CPU            Intel® Core™ i7-9750H                                                      Works    N/A                      N/A                 6.5.6
  GPU            Intel Corporation UHD Graphics 630 (Mobile)                                Works    N/A                      N/A                 6.5.6
  Discrete GPU   NVIDIA Corporation TU106M \[GeForce RTX 2070 Mobile\] (rev a1)             Works    N/A                      nvidia_drm nvidia   6.5.6
  SSD            Samsung Electronics Co Ltd NVMe SSD Controller SM981/PM981/PM983           Works    N/A                      nvme                5.5
  Sound          Intel Corporation Cannon Lake PCH cAVS (rev 10)                            Works    N/A                      snd_hda_intel       5.5
  Ethernet       Realtek Semiconductor Co., Ltd. Device 8125                                Works    N/A                      r8169               5.5
  Wi-Fi          Intel Corporation Wi-Fi 6 AX200 (rev 1a)                                   Works    8087:0029                iwlwifi             5.5
  Bluetooth      Intel Corporation Wi-Fi 6 AX200 (rev 1a)                                   Works    8087:0029                btusb               5.5
  Card Reader    Realtek Semiconductor Co., Ltd. RTS5260 PCI Express Card Reader (rev 01)   Works    N/A                      N/A                 5.5
  Touchpad       N/A                                                                        Works    N/A                      N/A                 5.5
  Webcam         IMC Networks Integrated Camera                                             Works    13d3:56d5                uvcvideo            5.5
  -------------- -------------------------------------------------------------------------- -------- ------------------------ ------------------- ---------------- -------

### [Detailed information]

`user `[`$`]`lspci -k`

    00:00.0 Host bridge: Intel Corporation 8th Gen Core Processor Host Bridge/DRAM Registers (rev 07)
        DeviceName: Onboard - Other
        Subsystem: Razer USA Ltd. 8th Gen Core Processor Host Bridge/DRAM Registers
        Kernel driver in use: skl_uncore
    00:01.0 PCI bridge: Intel Corporation Xeon E3-1200 v5/E3-1500 v5/6th Gen Core Processor PCIe Controller (x16) (rev 07)
        Kernel driver in use: pcieport
    00:02.0 VGA compatible controller: Intel Corporation UHD Graphics 630 (Mobile)
        DeviceName: Onboard - Video
        Subsystem: Razer USA Ltd. UHD Graphics 630 (Mobile)
        Kernel driver in use: i915
        Kernel modules: i915
    00:04.0 Signal processing controller: Intel Corporation Xeon E3-1200 v5/E3-1500 v5/6th Gen Core Processor Thermal Subsystem (rev 07)
        DeviceName: Onboard - Other
        Subsystem: Razer USA Ltd. Xeon E3-1200 v5/E3-1500 v5/6th Gen Core Processor Thermal Subsystem
    00:12.0 Signal processing controller: Intel Corporation Cannon Lake PCH Thermal Controller (rev 10)
        DeviceName: Onboard - Other
        Subsystem: Razer USA Ltd. Cannon Lake PCH Thermal Controller
        Kernel driver in use: intel_pch_thermal
    00:14.0 USB controller: Intel Corporation Cannon Lake PCH USB 3.1 xHCI Host Controller (rev 10)
        DeviceName: Onboard - Other
        Subsystem: Razer USA Ltd. Cannon Lake PCH USB 3.1 xHCI Host Controller
        Kernel driver in use: xhci_hcd
    00:14.2 RAM memory: Intel Corporation Cannon Lake PCH Shared SRAM (rev 10)
        DeviceName: Onboard - Other
        Subsystem: Razer USA Ltd. Cannon Lake PCH Shared SRAM
    00:15.0 Serial bus controller [0c80]: Intel Corporation Cannon Lake PCH Serial IO I2C Controller #0 (rev 10)
        DeviceName: Onboard - Other
        Subsystem: Razer USA Ltd. Cannon Lake PCH Serial IO I2C Controller
        Kernel driver in use: intel-lpss
    00:16.0 Communication controller: Intel Corporation Cannon Lake PCH HECI Controller (rev 10)
        DeviceName: Onboard - Other
        Subsystem: Razer USA Ltd. Cannon Lake PCH HECI Controller
        Kernel driver in use: mei_me
    00:17.0 SATA controller: Intel Corporation Cannon Lake Mobile PCH SATA AHCI Controller (rev 10)
        DeviceName: Onboard - SATA
        Subsystem: Razer USA Ltd. Cannon Lake Mobile PCH SATA AHCI Controller
        Kernel driver in use: ahci
    00:1b.0 PCI bridge: Intel Corporation Cannon Lake PCH PCI Express Root Port #17 (rev f0)
        Kernel driver in use: pcieport
    00:1b.4 PCI bridge: Intel Corporation Cannon Lake PCH PCI Express Root Port #21 (rev f0)
        Kernel driver in use: pcieport
    00:1d.0 PCI bridge: Intel Corporation Cannon Lake PCH PCI Express Root Port #9 (rev f0)
        Kernel driver in use: pcieport
    00:1d.5 PCI bridge: Intel Corporation Cannon Lake PCH PCI Express Root Port #14 (rev f0)
        Kernel driver in use: pcieport
    00:1d.6 PCI bridge: Intel Corporation Cannon Lake PCH PCI Express Root Port #15 (rev f0)
        Kernel driver in use: pcieport
    00:1d.7 PCI bridge: Intel Corporation Cannon Lake PCH PCI Express Root Port #16 (rev f0)
        Kernel driver in use: pcieport
    00:1e.0 Communication controller: Intel Corporation Device a328 (rev 10)
        DeviceName: Onboard - Other
        Subsystem: Razer USA Ltd. Device 3000
        Kernel driver in use: intel-lpss
    00:1f.0 ISA bridge: Intel Corporation Device a30d (rev 10)
        DeviceName: Onboard - Other
        Subsystem: Razer USA Ltd. Device 3000
    00:1f.3 Audio device: Intel Corporation Cannon Lake PCH cAVS (rev 10)
        DeviceName: Onboard - Sound
        Subsystem: Razer USA Ltd. Cannon Lake PCH cAVS
        Kernel driver in use: snd_hda_intel
        Kernel modules: snd_hda_intel
    00:1f.4 SMBus: Intel Corporation Cannon Lake PCH SMBus Controller (rev 10)
        DeviceName: Onboard - Other
        Subsystem: Razer USA Ltd. Cannon Lake PCH SMBus Controller
        Kernel driver in use: i801_smbus
        Kernel modules: i2c_i801
    00:1f.5 Serial bus controller [0c80]: Intel Corporation Cannon Lake PCH SPI Controller (rev 10)
        DeviceName: Onboard - Other
        Subsystem: Razer USA Ltd. Cannon Lake PCH SPI Controller
    01:00.0 VGA compatible controller: NVIDIA Corporation TU106M [GeForce RTX 2070 Mobile] (rev a1)
        Subsystem: Razer USA Ltd. TU106M [GeForce RTX 2070 Mobile]
        Kernel modules: nvidia_drm, nvidia
    02:00.0 PCI bridge: Intel Corporation JHL7540 Thunderbolt 3 Bridge [Titan Ridge 2C 2018] (rev 06)
        Kernel driver in use: pcieport
    03:00.0 PCI bridge: Intel Corporation JHL7540 Thunderbolt 3 Bridge [Titan Ridge 2C 2018] (rev 06)
        Kernel driver in use: pcieport
    03:01.0 PCI bridge: Intel Corporation JHL7540 Thunderbolt 3 Bridge [Titan Ridge 2C 2018] (rev 06)
        Kernel driver in use: pcieport
    03:02.0 PCI bridge: Intel Corporation JHL7540 Thunderbolt 3 Bridge [Titan Ridge 2C 2018] (rev 06)
        Kernel driver in use: pcieport
    04:00.0 System peripheral: Intel Corporation JHL7540 Thunderbolt 3 NHI [Titan Ridge 2C 2018] (rev 06)
        Subsystem: Razer USA Ltd. JHL7540 Thunderbolt 3 NHI [Titan Ridge 2C 2018]
        Kernel driver in use: thunderbolt
    43:00.0 USB controller: Intel Corporation JHL7540 Thunderbolt 3 USB Controller [Titan Ridge 2C 2018] (rev 06)
        Subsystem: Intel Corporation JHL7540 Thunderbolt 3 USB Controller [Titan Ridge 2C 2018]
        Kernel driver in use: xhci_hcd
    44:00.0 Non-Volatile memory controller: Samsung Electronics Co Ltd NVMe SSD Controller SM981/PM981/PM983
        Subsystem: Samsung Electronics Co Ltd NVMe SSD Controller SM981/PM981/PM983
        Kernel driver in use: nvme
    45:00.0 Non-Volatile memory controller: Samsung Electronics Co Ltd NVMe SSD Controller SM981/PM981/PM983
        Subsystem: Samsung Electronics Co Ltd NVMe SSD Controller SM981/PM981/PM983
        Kernel driver in use: nvme
    46:00.0 Ethernet controller: Realtek Semiconductor Co., Ltd. Device 8125
        Subsystem: Razer USA Ltd. Device 3000
        Kernel driver in use: r8169
    47:00.0 Unassigned class [ff00]: Realtek Semiconductor Co., Ltd. RTS5260 PCI Express Card Reader (rev 01)
        Subsystem: Razer USA Ltd. RTS5260 PCI Express Card Reader
    48:00.0 Network controller: Intel Corporation Wi-Fi 6 AX200 (rev 1a)
        Subsystem: Intel Corporation Wi-Fi 6 AX200
        Kernel driver in use: iwlwifi

`user `[`$`]`lsusb`

    Bus 002 Device 001: ID 1d6b:0003 Linux Foundation 3.0 root hub
    Bus 001 Device 003: ID 1532:0234 Razer USA, Ltd Razer Blade
    Bus 006 Device 001: ID 1d6b:0003 Linux Foundation 3.0 root hub
    Bus 001 Device 002: ID 13d3:56d5 IMC Networks Integrated Camera
    Bus 001 Device 004: ID 8087:0029 Intel Corp.
    Bus 001 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub
    Bus 005 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub

`user `[`$`]`dmidecode`

    # dmidecode 3.2
    Getting SMBIOS data from sysfs.
    SMBIOS 3.2.0 present.
    Table at 0x3C9A9000.

    Handle 0x0000, DMI type 0, 26 bytes
    BIOS Information
        Vendor: Razer
        Version: 1.02
        Release Date: 05/16/2019
        Address: 0xF0000
        Runtime Size: 64 kB
        ROM Size: 16 MB
        Characteristics:
            PCI is supported
            BIOS is upgradeable
            BIOS shadowing is allowed
            Boot from CD is supported
            Selectable boot is supported
            BIOS ROM is socketed
            EDD is supported
            5.25"/1.2 MB floppy services are supported (int 13h)
            3.5"/720 kB floppy services are supported (int 13h)
            3.5"/2.88 MB floppy services are supported (int 13h)
            Print screen service is supported (int 5h)
            Serial services are supported (int 14h)
            Printer services are supported (int 17h)
            ACPI is supported
            USB legacy is supported
            BIOS boot specification is supported
            Targeted content distribution is supported
            UEFI is supported
        BIOS Revision: 1.2
        Firmware Revision: 1.0

    Handle 0x0001, DMI type 1, 27 bytes
    System Information
        Manufacturer: Razer
        Product Name: Blade Pro 17 (2019)
        Version: 2.04
        Serial Number: BYXXXXXXXXXXXXXXXXXX
        UUID: YYYYYYYYYY-3637-6131-6235-XXXXXXXXXXXXXXXXX
        Wake-up Type: Power Switch
        SKU Number: RZ09-02877N92
        Family: 1A583000 Razer Blade Pro 17

    Handle 0x0002, DMI type 2, 15 bytes
    Base Board Information
        Manufacturer: Razer
        Product Name: DA720
        Version:
        Serial Number:
        Asset Tag:
        Features:
            Board is a hosting board
            Board is replaceable
        Location In Chassis:
        Chassis Handle: 0x0003
        Type: Motherboard
        Contained Object Handles: 0

    Handle 0x0003, DMI type 3, 22 bytes
    Chassis Information
        Manufacturer: Razer
        Type: Notebook
        Lock: Not Present
        Version:
        Serial Number:
        Asset Tag:
        Boot-up State: Safe
        Power Supply State: Safe
        Thermal State: Safe
        Security Status: None
        OEM Information: 0x00000000
        Height: Unspecified
        Number Of Power Cords: 1
        Contained Elements: 0
        SKU Number:

    Handle 0x0004, DMI type 8, 9 bytes
    Port Connector Information
        Internal Reference Designator: FFH
        Internal Connector Type: None
        External Reference Designator: USB3
        External Connector Type: Access Bus (USB)
        Port Type: USB

    Handle 0x0005, DMI type 8, 9 bytes
    Port Connector Information
        Internal Reference Designator: FFH
        Internal Connector Type: None
        External Reference Designator: EXT HDMI
        External Connector Type: None
        Port Type: Other

    Handle 0x0006, DMI type 8, 9 bytes
    Port Connector Information
        Internal Reference Designator: FFH
        Internal Connector Type: None
        External Reference Designator: USB-C Thunderbolt
        External Connector Type: None
        Port Type: Other

    Handle 0x0007, DMI type 8, 9 bytes
    Port Connector Information
        Internal Reference Designator: FFH
        Internal Connector Type: None
        External Reference Designator: Audio Jack
        External Connector Type: Mini Jack (headphones)
        Port Type: Audio Port

    Handle 0x0008, DMI type 8, 9 bytes
    Port Connector Information
        Internal Reference Designator: FFH
        Internal Connector Type: None
        External Reference Designator: LAN
        External Connector Type: RJ-45
        Port Type: Network Port

    Handle 0x0009, DMI type 8, 9 bytes
    Port Connector Information
        Internal Reference Designator: FFH
        Internal Connector Type: None
        External Reference Designator: SD-Card
        External Connector Type: None
        Port Type: Other

    Handle 0x000A, DMI type 9, 17 bytes
    System Slot Information
        Designation: J6B2
        Type: x16 PCI Express
        Current Usage: In Use
        Length: Long
        ID: 0
        Characteristics:
            3.3 V is provided
            Opening is shared
            PME signal is supported
        Bus Address: 0000:00:01.0

    Handle 0x000B, DMI type 9, 17 bytes
    System Slot Information
        Designation: J6B1
        Type: x1 PCI Express
        Current Usage: In Use
        Length: Short
        ID: 1
        Characteristics:
            3.3 V is provided
            Opening is shared
            PME signal is supported
        Bus Address: 0000:00:1c.3

    Handle 0x000C, DMI type 9, 17 bytes
    System Slot Information
        Designation: J6D1
        Type: x1 PCI Express
        Current Usage: In Use
        Length: Short
        ID: 2
        Characteristics:
            3.3 V is provided
            Opening is shared
            PME signal is supported
        Bus Address: 0000:00:1c.4

    Handle 0x000D, DMI type 9, 17 bytes
    System Slot Information
        Designation: J7B1
        Type: x1 PCI Express
        Current Usage: In Use
        Length: Short
        ID: 3
        Characteristics:
            3.3 V is provided
            Opening is shared
            PME signal is supported
        Bus Address: 0000:00:1c.5

    Handle 0x000E, DMI type 9, 17 bytes
    System Slot Information
        Designation: J8B4
        Type: x1 PCI Express
        Current Usage: In Use
        Length: Short
        ID: 4
        Characteristics:
            3.3 V is provided
            Opening is shared
            PME signal is supported
        Bus Address: 0000:00:1c.6

    Handle 0x000F, DMI type 10, 6 bytes
    On Board Device Information
        Type: Video
        Status: Enabled
        Description:    To Be Filled By O.E.M.

    Handle 0x0010, DMI type 11, 5 bytes
    OEM Strings
        String 1: 0
        String 2:
        String 3:
        String 4:
        String 5:
        String 6:
        String 7:
        String 8:

    Handle 0x0011, DMI type 12, 5 bytes
    System Configuration Options
        Option 1:

    Handle 0x0012, DMI type 32, 20 bytes
    System Boot Information
        Status: No errors detected

    Handle 0x0013, DMI type 34, 11 bytes
    Management Device
        Description: LM78-1
        Type: LM78
        Address: 0x00000000
        Address Type: I/O Port

    Handle 0x0014, DMI type 26, 22 bytes
    Voltage Probe
        Description: LM78A
        Location: Motherboard
        Status: OK
        Maximum Value: Unknown
        Minimum Value: Unknown
        Resolution: Unknown
        Tolerance: Unknown
        Accuracy: Unknown
        OEM-specific Information: 0x00000000
        Nominal Value: Unknown

    Handle 0x0015, DMI type 36, 16 bytes
    Management Device Threshold Data
        Lower Non-critical Threshold: 1
        Upper Non-critical Threshold: 2
        Lower Critical Threshold: 3
        Upper Critical Threshold: 4
        Lower Non-recoverable Threshold: 5
        Upper Non-recoverable Threshold: 6

    Handle 0x0016, DMI type 35, 11 bytes
    Management Device Component
        Description: Default string
        Management Device Handle: 0x0013
        Component Handle: 0x0014
        Threshold Handle: 0x0015

    Handle 0x0017, DMI type 28, 22 bytes
    Temperature Probe
        Description: LM78A
        Location: Motherboard
        Status: OK
        Maximum Value: Unknown
        Minimum Value: Unknown
        Resolution: Unknown
        Tolerance: Unknown
        Accuracy: Unknown
        OEM-specific Information: 0x00000000
        Nominal Value: Unknown

    Handle 0x0018, DMI type 36, 16 bytes
    Management Device Threshold Data
        Lower Non-critical Threshold: 1
        Upper Non-critical Threshold: 2
        Lower Critical Threshold: 3
        Upper Critical Threshold: 4
        Lower Non-recoverable Threshold: 5
        Upper Non-recoverable Threshold: 6

    Handle 0x0019, DMI type 35, 11 bytes
    Management Device Component
        Description: Default string
        Management Device Handle: 0x0013
        Component Handle: 0x0017
        Threshold Handle: 0x0018

    Handle 0x001A, DMI type 27, 15 bytes
    Cooling Device
        Temperature Probe Handle: 0x0017
        Type: Power Supply Fan
        Status: OK
        Cooling Unit Group: 1
        OEM-specific Information: 0x00000000
        Nominal Speed: Unknown Or Non-rotating
        Description: Cooling Dev 1

    Handle 0x001B, DMI type 36, 16 bytes
    Management Device Threshold Data
        Lower Non-critical Threshold: 1
        Upper Non-critical Threshold: 2
        Lower Critical Threshold: 3
        Upper Critical Threshold: 4
        Lower Non-recoverable Threshold: 5
        Upper Non-recoverable Threshold: 6

    Handle 0x001C, DMI type 35, 11 bytes
    Management Device Component
        Description: Default string
        Management Device Handle: 0x0013
        Component Handle: 0x001A
        Threshold Handle: 0x001B

    Handle 0x001D, DMI type 27, 15 bytes
    Cooling Device
        Temperature Probe Handle: 0x0017
        Type: Power Supply Fan
        Status: OK
        Cooling Unit Group: 1
        OEM-specific Information: 0x00000000
        Nominal Speed: Unknown Or Non-rotating
        Description: Not Specified

    Handle 0x001E, DMI type 36, 16 bytes
    Management Device Threshold Data
        Lower Non-critical Threshold: 1
        Upper Non-critical Threshold: 2
        Lower Critical Threshold: 3
        Upper Critical Threshold: 4
        Lower Non-recoverable Threshold: 5
        Upper Non-recoverable Threshold: 6

    Handle 0x001F, DMI type 35, 11 bytes
    Management Device Component
        Description: Default string
        Management Device Handle: 0x0013
        Component Handle: 0x001D
        Threshold Handle: 0x001E

    Handle 0x0020, DMI type 29, 22 bytes
    Electrical Current Probe
        Description: ABC
        Location: Motherboard
        Status: OK
        Maximum Value: Unknown
        Minimum Value: Unknown
        Resolution: Unknown
        Tolerance: Unknown
        Accuracy: Unknown
        OEM-specific Information: 0x00000000
        Nominal Value: Unknown

    Handle 0x0021, DMI type 36, 16 bytes
    Management Device Threshold Data

    Handle 0x0022, DMI type 35, 11 bytes
    Management Device Component
        Description: Default string
        Management Device Handle: 0x0013
        Component Handle: 0x0020
        Threshold Handle: 0x0021

    Handle 0x0023, DMI type 39, 22 bytes
    System Power Supply
        Power Unit Group: 1
        Location:
        Name:
        Manufacturer:
        Serial Number:
        Asset Tag:
        Model Part Number:
        Revision:
        Max Power Capacity: 0 W
        Status: Not Present
        Type: <OUT OF SPEC>
        Input Voltage Range Switching: <OUT OF SPEC>
        Plugged: Yes
        Hot Replaceable: No

    Handle 0x0024, DMI type 16, 23 bytes
    Physical Memory Array
        Location: System Board Or Motherboard
        Use: System Memory
        Error Correction Type: None
        Maximum Capacity: 32 GB
        Error Information Handle: Not Provided
        Number Of Devices: 2

    Handle 0x0027, DMI type 19, 31 bytes
    Memory Array Mapped Address
        Starting Address: 0x00000000000
        Ending Address: 0x003FFFFFFFF
        Range Size: 16 GB
        Physical Array Handle: 0x0024
        Partition Width: 2

    Handle 0x0028, DMI type 43, 31 bytes
    TPM Device
        Vendor ID: CTNI
        Specification Version: 2.0  Firmware Revision: 403.1
        Description: INTEL  Characteristics:
            Family configurable via platform software support
        OEM-specific Information: 0x00000000

    Handle 0x0029, DMI type 221, 26 bytes
    OEM-specific Type
        Header and Data:
            DD 1A 29 00 03 01 00 07 00 5C 50 00 02 00 00 00
            00 B4 00 03 00 01 05 00 00 00
        Strings:
            Reference Code - CPU
            uCode Version
            TXT ACM version

    Handle 0x002A, DMI type 221, 26 bytes
    OEM-specific Type
        Header and Data:
            DD 1A 2A 00 03 01 00 07 00 5C 50 00 02 00 0C 00
            00 0A 00 03 04 0C 00 26 96 05
        Strings:
            Reference Code - ME
            MEBx version
            ME Firmware Version
            Consumer SKU

    Handle 0x002B, DMI type 221, 82 bytes
    OEM-specific Type
        Header and Data:
            DD 52 2B 00 0B 01 00 07 00 5C 50 00 02 03 FF FF
            FF FF FF 04 00 FF FF FF 10 00 05 00 FF FF FF 10
            00 06 00 FF FF FF FF FF 07 00 02 00 00 00 00 08
            00 09 00 00 00 00 09 00 0A 00 00 00 00 0A 00 07
            00 00 00 00 0B 00 06 00 00 00 00 0C 00 07 00 00
            00 00
        Strings:
            Reference Code - CNL PCH
            PCH-CRID Status
            Disabled
            PCH-CRID Original Value
            PCH-CRID New Value
            OPROM - RST - RAID
            CNL PCH H A0 Hsio Version
            CNL PCH H Ax Hsio Version
            CNL PCH H Bx Hsio Version
            CNL PCH LP B0 Hsio Version
            CNL PCH LP Bx Hsio Version
            CNL PCH LP Dx Hsio Version

    Handle 0x002C, DMI type 221, 54 bytes
    OEM-specific Type
        Header and Data:
            DD 36 2C 00 07 01 00 07 00 5C 50 00 02 00 00 07
            01 67 00 03 00 07 00 5C 50 00 04 05 FF FF FF FF
            FF 06 00 00 00 00 07 00 07 00 00 00 00 07 00 08
            00 FF FF FF FF FF
        Strings:
            Reference Code - SA - System Agent
            Reference Code - MRC
            SA - PCIe Version
            SA-CRID Status
            Disabled
            SA-CRID Original Value
            SA-CRID New Value
            OPROM - VBIOS

    Handle 0x002D, DMI type 221, 12 bytes
    OEM-specific Type
        Header and Data:
            DD 0C 2D 00 01 01 00 04 00 00 00 00
        Strings:
            FSP Binary Version

    Handle 0x002E, DMI type 7, 27 bytes
    Cache Information
        Socket Designation: L1 Cache
        Configuration: Enabled, Not Socketed, Level 1
        Operational Mode: Write Back
        Location: Internal
        Installed Size: 384 kB
        Maximum Size: 384 kB
        Supported SRAM Types:
            Synchronous
        Installed SRAM Type: Synchronous
        Speed: Unknown
        Error Correction Type: Parity
        System Type: Unified
        Associativity: 8-way Set-associative

    Handle 0x002F, DMI type 7, 27 bytes
    Cache Information
        Socket Designation: L2 Cache
        Configuration: Enabled, Not Socketed, Level 2
        Operational Mode: Write Back
        Location: Internal
        Installed Size: 1536 kB
        Maximum Size: 1536 kB
        Supported SRAM Types:
            Synchronous
        Installed SRAM Type: Synchronous
        Speed: Unknown
        Error Correction Type: Single-bit ECC
        System Type: Unified
        Associativity: 4-way Set-associative

    Handle 0x0030, DMI type 7, 27 bytes
    Cache Information
        Socket Designation: L3 Cache
        Configuration: Enabled, Not Socketed, Level 3
        Operational Mode: Write Back
        Location: Internal
        Installed Size: 12288 kB
        Maximum Size: 12288 kB
        Supported SRAM Types:
            Synchronous
        Installed SRAM Type: Synchronous
        Speed: Unknown
        Error Correction Type: Multi-bit ECC
        System Type: Unified
        Associativity: 16-way Set-associative

    Handle 0x0031, DMI type 4, 48 bytes
    Processor Information
        Socket Designation: U3E1
        Type: Central Processor
        Family: Core i7
        Manufacturer: Intel(R) Corporation
        ID: EA 06 09 00 FF FB EB BF
        Signature: Type 0, Family 6, Model 158, Stepping 10
        Flags:
            FPU (Floating-point unit on-chip)
            VME (Virtual mode extension)
            DE (Debugging extension)
            PSE (Page size extension)
            TSC (Time stamp counter)
            MSR (Model specific registers)
            PAE (Physical address extension)
            MCE (Machine check exception)
            CX8 (CMPXCHG8 instruction supported)
            APIC (On-chip APIC hardware supported)
            SEP (Fast system call)
            MTRR (Memory type range registers)
            PGE (Page global enable)
            MCA (Machine check architecture)
            CMOV (Conditional move instruction supported)
            PAT (Page attribute table)
            PSE-36 (36-bit page size extension)
            CLFSH (CLFLUSH instruction supported)
            DS (Debug store)
            ACPI (ACPI supported)
            MMX (MMX technology supported)
            FXSR (FXSAVE and FXSTOR instructions supported)
            SSE (Streaming SIMD extensions)
            SSE2 (Streaming SIMD extensions 2)
            SS (Self-snoop)
            HTT (Multi-threading)
            TM (Thermal monitor supported)
            PBE (Pending break enabled)
        Version: Intel(R) Core(TM) i7-9750H CPU @ 2.60GHz
        Voltage: 0.8 V
        External Clock: 100 MHz
        Max Speed: 8300 MHz
        Current Speed: 2475 MHz
        Status: Populated, Enabled
        Upgrade: Socket BGA1440
        L1 Cache Handle: 0x002E
        L2 Cache Handle: 0x002F
        L3 Cache Handle: 0x0030
        Serial Number:
        Asset Tag:
        Part Number:
        Core Count: 6
        Core Enabled: 6
        Thread Count: 12
        Characteristics:
            64-bit capable
            Multi-Core
            Hardware Thread
            Execute Protection
            Enhanced Virtualization
            Power/Performance Control

    Handle 0x0039, DMI type 248, 17 bytes
    OEM-specific Type
        Header and Data:
            F8 11 39 00 00 02 69 00 01 4F 45 4D 57 49 46 49
            00

    Handle 0x003A, DMI type 17, 84 bytes
    Memory Device
        Array Handle: 0x0024
        Error Information Handle: Not Provided
        Total Width: 64 bits
        Data Width: 64 bits
        Size: 8192 MB
        Form Factor: SODIMM
        Set: None
        Locator: ChannelA-DIMM0
        Bank Locator: BANK 0
        Type: DDR4
        Type Detail: Synchronous
        Speed: 2667 MT/s
        Manufacturer: Samsung
        Serial Number: NNNNNNNN
        Asset Tag: AAAAAAAAAA
        Part Number: M471A1K43CB1-CTD
        Rank: 1
        Configured Memory Speed: 2667 MT/s
        Minimum Voltage: 1.2 V
        Maximum Voltage: 1.2 V
        Configured Voltage: 1.2 V
        Memory Technology: DRAM
        Memory Operating Mode Capability: Volatile memory
        Firmware Version: Not Specified
        Module Manufacturer ID: Bank 1, Hex 0xCE
        Module Product ID: Unknown
        Memory Subsystem Controller Manufacturer ID: Unknown
        Memory Subsystem Controller Product ID: Unknown
        Non-Volatile Size: None
        Volatile Size: 8 GB
        Cache Size: None
        Logical Size: None

    Handle 0x003B, DMI type 17, 84 bytes
    Memory Device
        Array Handle: 0x0024
        Error Information Handle: Not Provided
        Total Width: 64 bits
        Data Width: 64 bits
        Size: 8192 MB
        Form Factor: SODIMM
        Set: None
        Locator: ChannelB-DIMM0
        Bank Locator: BANK 2
        Type: DDR4
        Type Detail: Synchronous
        Speed: 2667 MT/s
        Manufacturer: Samsung
        Serial Number: GGGGGGGGGG
        Asset Tag: BBBBBBBBB
        Part Number: M471A1K43CB1-CTD
        Rank: 1
        Configured Memory Speed: 2667 MT/s
        Minimum Voltage: 1.2 V
        Maximum Voltage: 1.2 V
        Configured Voltage: 1.2 V
        Memory Technology: DRAM
        Memory Operating Mode Capability: Volatile memory
        Firmware Version: Not Specified
        Module Manufacturer ID: Bank 1, Hex 0xCE
        Module Product ID: Unknown
        Memory Subsystem Controller Manufacturer ID: Unknown
        Memory Subsystem Controller Product ID: Unknown
        Non-Volatile Size: None
        Volatile Size: 8 GB
        Cache Size: None
        Logical Size: None

    Handle 0x003C, DMI type 20, 35 bytes
    Memory Device Mapped Address
        Starting Address: 0x00000000000
        Ending Address: 0x001FFFFFFFF
        Range Size: 8 GB
        Physical Device Handle: 0x003A
        Memory Array Mapped Address Handle: 0x0027
        Partition Row Position: Unknown
        Interleave Position: 1
        Interleaved Data Depth: 1

    Handle 0x003D, DMI type 20, 35 bytes
    Memory Device Mapped Address
        Starting Address: 0x00200000000
        Ending Address: 0x003FFFFFFFF
        Range Size: 8 GB
        Physical Device Handle: 0x003B
        Memory Array Mapped Address Handle: 0x0027
        Partition Row Position: Unknown
        Interleave Position: 2
        Interleaved Data Depth: 1

    Handle 0x003E, DMI type 130, 20 bytes
    OEM-specific Type
        Header and Data:
            82 14 3E 00 24 41 4D 54 00 00 00 00 00 A5 AF 02
            C0 00 00 00

    Handle 0x003F, DMI type 131, 64 bytes
    OEM-specific Type
        Header and Data:
            83 40 3F 00 31 00 00 00 0C 00 00 00 00 00 0A 00
            F8 00 0D A3 00 00 00 00 01 00 00 00 00 00 0C 00
            96 05 26 00 00 00 00 00 FE 00 FF FF 00 00 00 00
            00 00 00 00 22 00 00 00 76 50 72 6F 00 00 00 00

    Handle 0x0040, DMI type 13, 22 bytes
    BIOS Language Information
        Language Description Format: Long
        Installable Languages: 1
            en|US|iso8859-1
        Currently Installed Language: en|US|iso8859-1

    Handle 0x0041, DMI type 41, 11 bytes
    Onboard Device
        Reference Designation: Onboard - Other
        Type: Other
        Status: Enabled
        Type Instance: 1
        Bus Address: 0000:00:00.0

    Handle 0x0042, DMI type 41, 11 bytes
    Onboard Device
        Reference Designation: Onboard - Video
        Type: Video
        Status: Enabled
        Type Instance: 1
        Bus Address: 0000:00:02.0

    Handle 0x0043, DMI type 41, 11 bytes
    Onboard Device
        Reference Designation: Onboard - Other
        Type: Other
        Status: Enabled
        Type Instance: 2
        Bus Address: 0000:00:04.0

    Handle 0x0044, DMI type 41, 11 bytes
    Onboard Device
        Reference Designation: Onboard - Other
        Type: Other
        Status: Enabled
        Type Instance: 3
        Bus Address: 0000:00:12.0

    Handle 0x0045, DMI type 41, 11 bytes
    Onboard Device
        Reference Designation: Onboard - Other
        Type: Other
        Status: Enabled
        Type Instance: 4
        Bus Address: 0000:00:14.0

    Handle 0x0046, DMI type 41, 11 bytes
    Onboard Device
        Reference Designation: Onboard - Other
        Type: Other
        Status: Enabled
        Type Instance: 5
        Bus Address: 0000:00:14.2

    Handle 0x0047, DMI type 41, 11 bytes
    Onboard Device
        Reference Designation: Onboard - Other
        Type: Other
        Status: Enabled
        Type Instance: 6
        Bus Address: 0000:00:15.0

    Handle 0x0048, DMI type 41, 11 bytes
    Onboard Device
        Reference Designation: Onboard - Other
        Type: Other
        Status: Enabled
        Type Instance: 7
        Bus Address: 0000:00:16.0

    Handle 0x0049, DMI type 41, 11 bytes
    Onboard Device
        Reference Designation: Onboard - SATA
        Type: SATA Controller
        Status: Enabled
        Type Instance: 1
        Bus Address: 0000:00:17.0

    Handle 0x004A, DMI type 41, 11 bytes
    Onboard Device
        Reference Designation: Onboard - Other
        Type: Other
        Status: Enabled
        Type Instance: 8
        Bus Address: 0000:00:1e.0

    Handle 0x004B, DMI type 41, 11 bytes
    Onboard Device
        Reference Designation: Onboard - Other
        Type: Other
        Status: Enabled
        Type Instance: 9
        Bus Address: 0000:00:1f.0

    Handle 0x004C, DMI type 41, 11 bytes
    Onboard Device
        Reference Designation: Onboard - Sound
        Type: Sound
        Status: Enabled
        Type Instance: 1
        Bus Address: 0000:00:1f.3

    Handle 0x004D, DMI type 41, 11 bytes
    Onboard Device
        Reference Designation: Onboard - Other
        Type: Other
        Status: Enabled
        Type Instance: 10
        Bus Address: 0000:00:1f.4

    Handle 0x004E, DMI type 41, 11 bytes
    Onboard Device
        Reference Designation: Onboard - Other
        Type: Other
        Status: Enabled
        Type Instance: 11
        Bus Address: 0000:00:1f.5

    Handle 0x004F, DMI type 221, 89 bytes
    OEM-specific Type
        Header and Data:
            DD 59 4F 00 0C 01 00 FF FF FF FF FF 02 00 FF FF
            FF FF FF 03 04 FF FF FF FF FF 05 06 FF FF FF FF
            FF 07 08 FF FF FF FF FF 09 00 00 00 00 00 00 0A
            00 FF FF FF FF FF 0B 00 01 00 00 00 00 0C 00 00
            09 00 85 10 0D 0E 01 04 03 00 00 0F 00 00 07 00
            00 00 10 00 00 02 00 0E 00
        Strings:
            Lan Phy Version
            Sensor Firmware Version
            Debug Mode Status
            Disabled
            Performance Mode Status
            Disabled
            Debug Use USB(Disabled:Serial)
            Disabled
            ICC Overclocking Version
            UNDI Version
            EC FW Version
            GOP Version
            Royal Park Version
            BP1.4.3.0_RP03
            Platform Version
            Client Silicon Version

    Handle 0x0050, DMI type 136, 6 bytes
    OEM-specific Type
        Header and Data:
            88 06 50 00 00 00

    Handle 0x0051, DMI type 14, 23 bytes
    Group Associations
        Name: Firmware Version Info
        Items: 6
            0x0029 (OEM-specific)
            0x002A (OEM-specific)
            0x002B (OEM-specific)
            0x002C (OEM-specific)
            0x002D (OEM-specific)
            0x004F (OEM-specific)

    Handle 0x0052, DMI type 14, 8 bytes
    Group Associations
        Name: $MEI
        Items: 1
            0x0000 (OEM-specific)

    Handle 0x0053, DMI type 219, 106 bytes
    OEM-specific Type
        Header and Data:
            DB 6A 53 00 01 04 01 45 02 00 90 06 01 10 86 20
            00 00 00 00 48 00 00 00 00 00 00 06 00 40 40 02
            FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
            FF FF FF FF FF FF FF FF 03 00 00 00 80 00 00 00
            00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
            00 04 00 00 00 00 00 00 00 00 00 00 00 00 00 00
            00 00 00 00 00 00 00 00 00 00
        Strings:
            MEI1
            MEI2
            MEI3
            MEI4

    Handle 0x0054, DMI type 127, 4 bytes
    End Of Table

`user `[`$`]`sensors`

    coretemp-isa-0000
    Adapter: ISA adapter
    Package id 0:  +47.0°C  (high = +100.0°C, crit = +100.0°C)
    Core 0:        +47.0°C  (high = +100.0°C, crit = +100.0°C)
    Core 1:        +47.0°C  (high = +100.0°C, crit = +100.0°C)
    Core 2:        +46.0°C  (high = +100.0°C, crit = +100.0°C)
    Core 3:        +47.0°C  (high = +100.0°C, crit = +100.0°C)
    Core 4:        +45.0°C  (high = +100.0°C, crit = +100.0°C)
    Core 5:        +46.0°C  (high = +100.0°C, crit = +100.0°C)

    nvme-pci-4500
    Adapter: PCI adapter
    Composite:    +44.9°C  (low  = -273.1°C, high = +84.8°C)
                           (crit = +84.8°C)
    Sensor 1:     +44.9°C  (low  = -273.1°C, high = +65261.8°C)
    Sensor 2:     +39.9°C  (low  = -273.1°C, high = +65261.8°C)

    BAT0-acpi-0
    Adapter: ACPI interface
    in0:          17.46 V
    curr1:         0.00 A

    pch_cannonlake-virtual-0
    Adapter: Virtual device
    temp1:        +53.0°C

    iwlwifi_1-virtual-0
    Adapter: Virtual device
    temp1:        +46.0°C

    nvme-pci-4400
    Adapter: PCI adapter
    Composite:    +36.9°C  (low  = -273.1°C, high = +80.8°C)
                           (crit = +81.8°C)
    Sensor 1:     +36.9°C  (low  = -273.1°C, high = +65261.8°C)
    Sensor 2:     +38.9°C  (low  = -273.1°C, high = +65261.8°C)

    acpitz-acpi-0
    Adapter: ACPI interface
    temp1:        +27.8°C

## [Installation]

** Note**\
If BIOS version 1.02 is installed, there may exist a possibility to unlock a fair amount of options in the BIOS which may or may not be permanently hidden and locked, with later BIOS versions. This requires installing a modified BIOS, and installing a modified BIOS may or may not break warranties (and laptops).

** Tip**\
\* Disable Fast Boot in Windows first, if there is a plan to use Windows alongside.

-   Hit [F1] immediately/repeatedly after power on to enter the BIOS.
-   Disable Fast Boot and Secure Boot to be able to boot from a flash drive.

### [Firmware]

The wireless card requires external firmware (**intel/ibt-20-1-3.sfi**):

`root `[`#`]`emerge --ask sys-kernel/linux-firmware`

### [Kernel]

[KERNEL]

    CONFIG_BLK_DEV_NVME=y
    CONFIG_BT_HCIBTUSB_AUTOSUSPEND=y
    CONFIG_BT_HCIBTUSB=m
    CONFIG_BT_INTEL=m
    CONFIG_BT=y
    CONFIG_DRM_I915=m
    CONFIG_HID=y
    CONFIG_HID_BATTERY_STRENGTH=y
    CONFIG_HIDRAW=y
    CONFIG_HID_GENERIC=y
    CONFIG_HID_LOGITECH=y
    CONFIG_HID_LOGITECH_DJ=y
    CONFIG_HID_LOGITECH_HIDPP=y
    CONFIG_HID_MULTITOUCH=m
    CONFIG_HID_RMI=m
    CONFIG_HID_SENSOR_HUB=m
    CONFIG_HID_SENSOR_CUSTOM_SENSOR=m
    CONFIG_HID_ALPS=m
    CONFIG_I2C_DESIGNWARE_CORE=m
    CONFIG_I2C_DESIGNWARE_PCI=m
    CONFIG_I2C_DESIGNWARE_PLATFORM=m
    CONFIG_I2C_DESIGNWARE_SLAVE=y
    CONFIG_I2C_I801=m
    CONFIG_I2C_SMBUS=m
    CONFIG_INTEL_GTT=m
    CONFIG_INTEL_MEI_ME=y
    CONFIG_INTEL_MEI_TXE=y
    CONFIG_INTEL_MEI=y
    CONFIG_INTEL_PCH_THERMAL=y
    CONFIG_IWLDVM=y
    CONFIG_IWLMVM=y
    CONFIG_IWLWIFI_LEDS=y
    CONFIG_IWLWIFI=y
    CONFIG_MFD_INTEL_LPSS_ACPI=y
    CONFIG_MFD_INTEL_LPSS_PCI=y
    CONFIG_MFD_INTEL_LPSS=y
    CONFIG_MISC_RTSX=m
    CONFIG_MISC_RTSX_PCI=m
    CONFIG_MMC=m
    CONFIG_MMC_BLOCK=m
    CONFIG_MMC_BLOCK_MINORS=8
    CONFIG_MMC_SDHCI=m
    CONFIG_MMC_SDHCI_IO_ACCESSORS=y
    CONFIG_MMC_SDHCI_PCI=m
    CONFIG_MMC_RICOH_MMC=y
    CONFIG_MMC_SDHCI_ACPI=m
    CONFIG_MMC_SDHCI_PLTFM=m
    CONFIG_MMC_REALTEK_PCI=m
    CONFIG_MMC_CQHCI=m
    CONFIG_MOUSE_PS2_SMBUS=y
    CONFIG_MOUSE_PS2_SYNAPTICS_SMBUS=y
    CONFIG_NVME_CORE=y
    CONFIG_PCIEPORTBUS=y
    CONFIG_PERF_EVENTS_INTEL_UNCORE=y
    CONFIG_PINCTRL_CANNONLAKE=m
    CONFIG_R8169=y
    CONFIG_SATA_AHCI=y
    CONFIG_SND_HDA_CODEC_REALTEK=m
    CONFIG_SND_HDA_INTEL=m
    CONFIG_THUNDERBOLT=y
    CONFIG_USB_HID=y
    CONFIG_USB_XHCI_HCD=y
    CONFIG_MEDIA_USB_SUPPORT=y
    CONFIG_USB_VIDEO_CLASS=m
    CONFIG_USB_VIDEO_CLASS_INPUT_EVDEV=y

## [Configuration]

### [Xorg]

#### [Touchpad]

[FILE] **`/etc/X11/xorg.conf.d/70-synaptics.conf`**

    Section "InputClass"
     Identifier "User options"
     MatchDriver "synaptics"
     MatchIsTouchpad "yes"
     Option "HorizHysteresis" "15"
     Option "VertHysteresis" "15"
     Option "CoastingSpeed" "10"
     Option "CoastingFriction" "40"
     Option "VertScrollDelta" "50"
     Option "HorizScrollDelta" "50"
    EndSection

#### [Graphics]

This section describes a way to use Intel graphics as the primary graphics and NVIDIA graphics as the secondary graphics (only when needed).

This is a working configuration for use with [[[x11-drivers/nvidia-drivers]](https://packages.gentoo.org/packages/x11-drivers/nvidia-drivers)[]]:

[FILE] **`/etc/X11/xorg.conf`**

    Section "ServerLayout"
      Identifier "layout"
      Option "AllowNVIDIAGPUScreens"
      Screen 0 "iGPU"
      Inactive "dGPU"
    EndSection

    Section "Device"
      Identifier "iGPU"
      Driver "modesetting"
      BusID "PCI:0:2:0"
      Option "DRI" "3"
    EndSection

    Section "DRI"
        Group "video"
        Mode 0666
    EndSection

    Section "Extensions"
        Option "Composite" "Enable"
        Option "RENDER" "Enable"
    EndSection

    Section "Screen"
      Identifier "iGPU"
      Device "iGPU"
    EndSection

    Section "Screen"
      Identifier "dGPU"
      Device "dGPU"
      Option "AllowEmptyInitialConfiguration" "Yes"
    EndSection

    Section "Device"
      Identifier "dGPU"
      Driver "nvidia"
      BusID "PCI:1:0:0"
    EndSection

Hybrid graphics works. Emerging [[[media-libs/mesa]](https://packages.gentoo.org/packages/media-libs/mesa)[]], [[[x11-base/xorg-server]](https://packages.gentoo.org/packages/x11-base/xorg-server)[]] and [[[x11-drivers/nvidia-drivers]](https://packages.gentoo.org/packages/x11-drivers/nvidia-drivers)[]] with these flags yields a working solution.

`root `[`#`]`emerge -pv media-libs/mesa xorg-server nvidia-drivers`

    ebuild   R    ] media-libs/mesa-19.3.0_rc6::gentoo  USE="X classic dri3 egl gallium gbm gles2 libglvnd llvm -d3d9 -debug -gles1 -lm-sensors -opencl -osmesa -pax_kernel (-selinux) -test -unwind -vaapi -valgrind -vdpau -vulkan -vulkan-overlay -wayland -xa -xvmc" ABI_X86="(64) -32 (-x32)" VIDEO_CARDS="i915 i965 intel (-freedreno) -iris (-lima) -nouveau (-panfrost) -r100 -r200 -r300 -r600 -radeon -radeonsi (-vc4) -virgl (-vivante) -vmware" 0 KiB
    [ebuild   R    ] x11-base/xorg-server-1.20.6:0/1.20.6::gentoo  USE="ipv6 libglvnd suid udev xorg -debug -dmx -doc -elogind -kdrive -libressl -minimal (-selinux) -static-libs -systemd -unwind -wayland -xcsecurity -xephyr -xnest -xvfb" 0 KiB
    [ebuild   R    ] x11-drivers/nvidia-drivers-440.44:0/440::gentoo  USE="X acpi driver gtk3 kms libglvnd multilib tools -compat -static-libs -uvm -wayland" ABI_X86="(64) -32 (-x32)" 0 KiB

In the case of [LightDM](https://wiki.gentoo.org/wiki/LightDM "LightDM"), the following file should be modified:

[FILE] **`/etc/lightdm/lightdm.conf`**

    ...

    [Seat:*]
    ...
    display-setup-script=/usr/local/bin/prepare-optimus.sh
    ...

    [...]

Then the script should be created:

[FILE] **`/usr/local/bin/prepare-optimus.sh`**

    #!/bin/bash
    xrandr --setprovideroutputsource modesetting NVIDIA-G0
    xrandr --auto
    # Run the rest of the arguments.
    # -
    $($@)

After this, there is no longer an [OpenGL](https://wiki.gentoo.org/wiki/OpenGL "OpenGL") eselect. By default, OpenGL runs on the iGPU. To offload to the dGPU, the command should be prefixed with:

    __NV_PRIME_RENDER_OFFLOAD=1 __GLX_VENDOR_LIBRARY_NAME=nvidia

#### [External graphics]

This example shows a way to connect an external monitor:

`user `[`$`]`xrandr --setprovideroutputsource 1 0`

`user `[`$`]`xrandr --output HDMI-1-0 --auto --left-of eDP-1`

### [][Fan control, RGB keyboard effects and gaming mode]

To control fans, set the gaming mode and customize RGB keyboard effects, [this application](https://github.com/Razer-Linux/razer-laptop-control-no-dkms) should be installed.

### [Power management]

** Note**\
It is possible to get down to 12.5 watts ([Wayfire](https://wiki.gentoo.org/wiki/Wayfire "Wayfire"), a couple of terminals, Wi-Fi, dual NVMe, 32GB memory, display is set to full brightness) or 6.5 watts when the display is off. (Updated April 2024, using kernel 6.8.3)

To establish the baseline, the following steps should be performed:

-   Install [PowerTOP](https://wiki.gentoo.org/wiki/PowerTOP "PowerTOP") and run it.
-   Disconnect the laptop\'s power supply.
-   Wait a few seconds for PowerTOP to report the power consumed from the battery.

#### [PowerTOP]

** Warning**\
**Do not** enable auto-suspend for the USB device, as it results in an **erratic keyboard**. See the configuration file below.

[PowerTOP](https://wiki.gentoo.org/wiki/PowerTOP "PowerTOP") should be run at bootup. To run PowerTOP at boot with [systemd](https://wiki.gentoo.org/wiki/Systemd "Systemd"), the following file should be created:

[FILE] **`/etc/systemd/system/powertop.service`**

    [Unit]
    Description=PowerTOP tuning

    [Service]
    Type=oneshot
    RemainAfterExit=yes
    # Do not auto-suspend the Razer USB device. Leads to wonky keyboard.
    ExecStart=/bin/bash -c "/usr/sbin/powertop --auto-tune && echo on > /sys/bus/usb/devices/1-8/power/control"

    [Install]
    WantedBy=multi-user.target

The created service should be enabled:

`root `[`#`]`systemctl enable --now powertop`

#### [DPMS]

Enable [DPMS](https://en.wikipedia.org/wiki/VESA_Display_Power_Management_Signaling "wikipedia:VESA Display Power Management Signaling"). In the case of [Wayfire](https://wiki.gentoo.org/wiki/Wayfire "Wayfire"), the following changes should be made to its configuration file:

[FILE] **`~/.config/wayfire.ini`**

    .....

    [idle]
    ......
    disable_on_fullscreen = true
    dpms_timeout = 60
    screensaver_timeout = 3600
    ....

    [....]

#### [NVIDIA]

** Note**\
\* This section provides information for **x11-drivers/nvidia-drivers-535.113.01** and **sys-kernel/gentoo-sources-6.5.5**.

-   After performing these steps, **nvidia-smi** may report that the GPU power consumption is 28 watts, which is incorrect.

By default, NVIDIA GPU is in **D0** state and consumes 5-6 watts continuously, even if it is not being used for anything. To save the energy, the card can be turned off (set to **D3cold** state).

The current state can be found by executing the following command:

`root `[`#`]`cat /sys/class/drm/card2/device/power_state`

    D0

To switch to **D3cold**, the NVIDIA audio should be disabled first:

[FILE] **`/etc/wireplumber/main.lua.d/51-alsa-disable.lua`**

    rule = ,
        },
      },
      apply_properties = ,
    }

    table.insert(alsa_monitor.rules,rule)

Then the NVIDIA driver should be configured:

[FILE] **`/etc/modprobe.d/nvidia.conf`**

    # NVIDIA drivers options
    # See /usr/share/doc/nvidia-drivers-*/README.txt* for more information.

    # nvidia-drivers and nouveau cannot be used at same time.
    # Comment out the following line if you wish to allow nouveau.
    blacklist nouveau

    # unsure if this line is strictly required for D3cold
    options nvidia-drm modeset=0

    # unsure if this line is strictly required for D3cold
    options nvidia NVreg_EnableS0ixPowerManagement=1

    # this line is required for D3cold, and should be 0x03 for RTX 30xx.
    options nvidia NVreg_DynamicPowerManagement=0x02

    # Suspend options. Allocations=0 recommended over =1 unless enable nvidia's
    # systemd sleep services (nvidia-hibernate, nvidia-resume, nvidia-suspend).
    options nvidia \
        NVreg_PreserveVideoMemoryAllocations=0 \
        NVreg_TemporaryFilePath=/var/tmp

    # options nvidia NVreg_DynamicPowerManagement=1 NVreg_EnableS0ixPowerManagement=1
    # !!! Security Warning !!!
    # Do not change the DeviceFile options unless you know what you are doing.
    # Only add trusted users to the 'video' group, these users may be able to
    # crash, compromise, or irreparably damage the machine.
    options nvidia \
        NVreg_DeviceFileGID=27 \
        NVreg_DeviceFileMode=432 \
        NVreg_DeviceFileUID=0 \
        NVreg_ModifyDeviceFiles=1

    # Should be no need to touch anything below.
    alias char-major-195 nvidia
    alias /dev/nvidiactl char-major-195
    remove nvidia modprobe -r --ignore-remove nvidia-drm nvidia-modeset nvidia-uvm nvidia

And the following [udev](https://wiki.gentoo.org/wiki/Udev "Udev") rules should be set:

[FILE] **`/etc/udev/rules.d/80-nvidia-pm.rules`**

    # Remove NVIDIA USB xHCI Host Controller devices, if present
    ACTION=="add", SUBSYSTEM=="pci", ATTR=="0x10de", ATTR=="0x0c0330", ATTR="1"

    # Remove NVIDIA USB Type-C UCSI devices, if present
    ACTION=="add", SUBSYSTEM=="pci", ATTR=="0x10de", ATTR=="0x0c8000", ATTR="1"

    # Remove NVIDIA Audio devices, if present
    ACTION=="add", SUBSYSTEM=="pci", ATTR=="0x10de", ATTR=="0x040300", ATTR="1"

    # Enable runtime PM for NVIDIA VGA/3D controller devices on driver bind
    ACTION=="bind", SUBSYSTEM=="pci", ATTR=="0x10de", ATTR=="0x030000", TEST=="power/control", ATTR="auto"
    ACTION=="bind", SUBSYSTEM=="pci", ATTR=="0x10de", ATTR=="0x030200", TEST=="power/control", ATTR="auto"

    # Disable runtime PM for NVIDIA VGA/3D controller devices on driver unbind
    ACTION=="unbind", SUBSYSTEM=="pci", ATTR=="0x10de", ATTR=="0x030000", TEST=="power/control", ATTR="on"
    ACTION=="unbind", SUBSYSTEM=="pci", ATTR=="0x10de", ATTR=="0x030200", TEST=="power/control", ATTR="on"

After creating or modifying the above files, a reboot must be performed.

After reboot, the state should be **D3cold**:

`root `[`#`]`cat /sys/class/drm/card2/device/power_state`

    D3cold

#### [Bluetooth]

Disabling bluetooth may conserve some energy as well:

`root `[`#`]`systemctl disable --now bluetooth`

`root `[`#`]`rfkill block 1`

## [Troubleshooting]

### [No sound]

Two driver options are required for HDA audio. Otherwise, speakers may be mute, or wireplumber may be sad and confused.

[FILE] **`/etc/modprobe.d/alsa.conf`**

    options snd-hda-intel model=alc298-spk-volume probe_mask=1

## [External resources]

-   [Razer Insider Linux Corner](https://insider.razer.com/index.php?forums/linux/)
-   [Official Razer Discord Server](https://discord.gg/razer)
-   [Linux Blade Discord Server](https://discord.gg/X5efAvM)