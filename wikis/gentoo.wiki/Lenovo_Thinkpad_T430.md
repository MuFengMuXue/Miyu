**Resources**

[[]][Home](https://download.lenovo.com/supportdata/product.html?id=LAPTOPS-AND-NETBOOKS/THINKPAD-T-SERIES-LAPTOPS/THINKPAD-T430)

[[]][Product Specifications Reference](https://psref.lenovo.com/syspool/Sys/PDF/withdrawnbook/ThinkPad_T430.pdf)

[[]][T430 Hardware Maintenance Manual](https://download.lenovo.com/ibmdl/pub/pc/pccbbs/mobiles_pdf/t430_t430i_hmm_en_0b48304_01.pdf)

[[]][T430 User Guide](https://download.lenovo.com/ibmdl/pub/pc/pccbbs/mobiles_pdf/t430_t430i_ug_en.pdf)

[[]][BIOS/UEFI Official documentation](https://support.lenovo.com/by/en/downloads/ds029252)

[[]][ThinkPad T Series](https://en.wikipedia.org/wiki/ThinkPad_T_Series "wikipedia:ThinkPad T Series")

[![](/images/thumb/2/2d/Screenshot_2020-10-22_Thinkpad-t430-keyboard_-_ThinkPad_T_series_-_Wikipedia.jpg/300px-Screenshot_2020-10-22_Thinkpad-t430-keyboard_-_ThinkPad_T_series_-_Wikipedia.jpg)](https://wiki.gentoo.org/wiki/File:Screenshot_2020-10-22_Thinkpad-t430-keyboard_-_ThinkPad_T_series_-_Wikipedia.jpg)

[](https://wiki.gentoo.org/wiki/File:Screenshot_2020-10-22_Thinkpad-t430-keyboard_-_ThinkPad_T_series_-_Wikipedia.jpg "Enlarge")

ThinkPad T430

[![](/images/thumb/e/e5/Thinkpad-t430--disassembled.jpeg/300px-Thinkpad-t430--disassembled.jpeg)](https://wiki.gentoo.org/wiki/File:Thinkpad-t430--disassembled.jpeg)

[](https://wiki.gentoo.org/wiki/File:Thinkpad-t430--disassembled.jpeg "Enlarge")

Make holes and use a copper tape to make it cooler

## Contents

-   [[1] [Hardware information]](#Hardware_information)
    -   [[1.1] [Firmware setup]](#Firmware_setup)
    -   [[1.2] [lscpu]](#lscpu)
    -   [[1.3] [lspci]](#lspci)
    -   [[1.4] [lsusb]](#lsusb)
    -   [[1.5] [RAM]](#RAM)
    -   [[1.6] [Hard Drive]](#Hard_Drive)
        -   [[1.6.1] [Trim]](#Trim)
    -   [[1.7] [Battery]](#Battery)
-   [[2] [Installation]](#Installation)
    -   [[2.1] [Firmware]](#Firmware)
        -   [[2.1.1] [Wi-Fi]](#Wi-Fi)
        -   [[2.1.2] [Ethernet]](#Ethernet)
        -   [[2.1.3] [Bluetooth]](#Bluetooth)
        -   [[2.1.4] [Sound]](#Sound)
        -   [[2.1.5] [Microcode]](#Microcode)
    -   [[2.2] [Kernel]](#Kernel)
    -   [[2.3] [Configuration]](#Configuration)
        -   [[2.3.1] [Compiler settings]](#Compiler_settings)
        -   [[2.3.2] [Packages settings]](#Packages_settings)
        -   [[2.3.3] [USE flags]](#USE_flags)
            -   [[2.3.3.1] [Firefox video performance]](#Firefox_video_performance)
    -   [[2.4] [Utils]](#Utils)
        -   [[2.4.1] [battery charge thresholds]](#battery_charge_thresholds)
        -   [[2.4.2] [fan control (noise level)]](#fan_control_.28noise_level.29)
        -   [[2.4.3] [Fingerprint reader]](#Fingerprint_reader)
        -   [[2.4.4] [ThinkLight]](#ThinkLight)
    -   [[2.5] [Displays]](#Displays)
        -   [[2.5.1] [Multiple displays]](#Multiple_displays)
        -   [[2.5.2] [Fastboot (reduce flickering on boot)]](#Fastboot_.28reduce_flickering_on_boot.29)
        -   [[2.5.3] [eGPU]](#eGPU)
        -   [[2.5.4] [Fix screen tearing]](#Fix_screen_tearing)
            -   [[2.5.4.1] [Pros of Wayland (Sway):]](#Pros_of_Wayland_.28Sway.29:)
            -   [[2.5.4.2] [Cons of Wayland]](#Cons_of_Wayland)
        -   [[2.5.5] [i3 bindsym for screenshot to file with a good name and to clipboard]](#i3_bindsym_for_screenshot_to_file_with_a_good_name_and_to_clipboard)
        -   [[2.5.6] [Alter brightness]](#Alter_brightness)
-   [[3] [Keyboard layouts]](#Keyboard_layouts)
-   [[4] [Screen recording with ffmpeg and vaapi (hardware acceleration, without Nvidia GPU chip)]](#Screen_recording_with_ffmpeg_and_vaapi_.28hardware_acceleration.2C_without_Nvidia_GPU_chip.29)
-   [[5] [Suspend without fan rotation]](#Suspend_without_fan_rotation)
-   [[6] [See also]](#See_also)
-   [[7] [References]](#References)

## [Hardware information]

[![](/images/thumb/d/da/T430-power-charger-65w.jpg/300px-T430-power-charger-65w.jpg)](https://wiki.gentoo.org/wiki/File:T430-power-charger-65w.jpg)

[](https://wiki.gentoo.org/wiki/File:T430-power-charger-65w.jpg "Enlarge")

Power charger for 65W: computer will loose power on 45W CPU

[![](/images/thumb/1/17/T430-lenovo-charge-connector.png/300px-T430-lenovo-charge-connector.png)](https://wiki.gentoo.org/wiki/File:T430-lenovo-charge-connector.png)

[](https://wiki.gentoo.org/wiki/File:T430-lenovo-charge-connector.png "Enlarge")

Charger connector

Error creating thumbnail: WARNING: The convert command is deprecated in IMv7, use \"magick\" instead of \"convert\" or \"magick convert\" convert: delegate failed \`\'dwebp\' -pam \'%i\' -o \'%o\'\' @ error/delegate.c/InvokeDelegate/1920. convert: unable to open file \'/tmp/magick-aCk-8cA4ZywxADIpJPbdbj-yNOGSRLRm\': No such file or directory @ error/constitute.c/ReadImage/791. convert: no images defined \`/tmp/transform_6ef379aa3101.png\' @ error/deprecate.c/ConvertImageCommand/3368. Error code: 1

[](https://wiki.gentoo.org/wiki/File:T430-charger-input-with-dock-station-4337.webp "Enlarge")

T430: charger input with dock station 4337

[![](/images/thumb/0/01/T430-charger-90w.jpg/300px-T430-charger-90w.jpg)](https://wiki.gentoo.org/wiki/File:T430-charger-90w.jpg)

[](https://wiki.gentoo.org/wiki/File:T430-charger-90w.jpg "Enlarge")

T430 charger for 90W: with 45W CPU (like i7-3840QM): with it the computer will not discharge when on

iGPU: [Intel HD Graphics 4000](https://en.wikipedia.org/wiki/Intel_Graphics_Technology#Ivy_Bridge "wikipedia:Intel Graphics Technology") ([without Vulkan support](https://www.intel.com/content/www/us/en/support/articles/000005524/graphics.html)): seventh generation, Ivy Bridge (released in 2012-2013). You can get GPU information in Firefox in `about:support`.

`root `[`#`]`dmidecode`

    # dmidecode 3.3
    Getting SMBIOS data from sysfs.
    SMBIOS 2.7 present.
    66 structures occupying 2571 bytes.
    Table at 0xFFFFFFFFDAE9C000.

    Handle 0x0000, DMI type 134, 16 bytes
    OEM-specific Type
        Header and Data:
            86 10 00 00 00 53 54 4D 20 01 01 00 00 02 01 02
        Strings:
            TPM INFO
            System Reserved

    Handle 0x0001, DMI type 4, 42 bytes
    Processor Information
        Socket Designation: CPU Socket - U3E1
        Type: Central Processor
        Family: Core i7
        Manufacturer: Intel(R) Corporation
        ID: A9 06 03 00 FF FB EB BF
        Signature: Type 0, Family 6, Model 58, Stepping 9
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
        Version: Intel(R) Core(TM) i7-3840QM CPU @ 2.80GHz
        Voltage: 0.9 V
        External Clock: 100 MHz
        Max Speed: 2800 MHz
        Current Speed: 2800 MHz
        Status: Populated, Enabled
        Upgrade: Socket rPGA988B
        L1 Cache Handle: 0x0003
        L2 Cache Handle: 0x0004
        L3 Cache Handle: 0x0005
        Serial Number: None
        Asset Tag: None
        Part Number: None
        Core Count: 4
        Core Enabled: 4
        Thread Count: 8
        Characteristics:
            64-bit capable

    Handle 0x0002, DMI type 7, 19 bytes
    Cache Information
        Socket Designation: L1-Cache
        Configuration: Enabled, Not Socketed, Level 1
        Operational Mode: Write Through
        Location: Internal
        Installed Size: 32 kB
        Maximum Size: 32 kB
        Supported SRAM Types:
            Unknown
        Installed SRAM Type: Unknown
        Speed: Unknown
        Error Correction Type: Parity
        System Type: Data
        Associativity: 8-way Set-associative

    Handle 0x0003, DMI type 7, 19 bytes
    Cache Information
        Socket Designation: L1-Cache
        Configuration: Enabled, Not Socketed, Level 1
        Operational Mode: Write Through
        Location: Internal
        Installed Size: 32 kB
        Maximum Size: 32 kB
        Supported SRAM Types:
            Unknown
        Installed SRAM Type: Unknown
        Speed: Unknown
        Error Correction Type: Parity
        System Type: Instruction
        Associativity: 8-way Set-associative

    Handle 0x0004, DMI type 7, 19 bytes
    Cache Information
        Socket Designation: L2-Cache
        Configuration: Enabled, Not Socketed, Level 2
        Operational Mode: Write Through
        Location: Internal
        Installed Size: 256 kB
        Maximum Size: 256 kB
        Supported SRAM Types:
            Unknown
        Installed SRAM Type: Unknown
        Speed: Unknown
        Error Correction Type: Multi-bit ECC
        System Type: Unified
        Associativity: 8-way Set-associative

    Handle 0x0005, DMI type 7, 19 bytes
    Cache Information
        Socket Designation: L3-Cache
        Configuration: Enabled, Not Socketed, Level 3
        Operational Mode: Write Back
        Location: Internal
        Installed Size: 8 MB
        Maximum Size: 8 MB
        Supported SRAM Types:
            Unknown
        Installed SRAM Type: Unknown
        Speed: Unknown
        Error Correction Type: Multi-bit ECC
        System Type: Unified
        Associativity: 16-way Set-associative

    Handle 0x0006, DMI type 129, 8 bytes
    OEM-specific Type
        Header and Data:
            81 08 06 00 01 01 02 01
        Strings:
            Intel_ASF
            Intel_ASF_001

    Handle 0x0007, DMI type 16, 23 bytes
    Physical Memory Array
        Location: System Board Or Motherboard
        Use: System Memory
        Error Correction Type: None
        Maximum Capacity: 16 GB
        Error Information Handle: Not Provided
        Number Of Devices: 2

    Handle 0x0008, DMI type 17, 34 bytes
    Memory Device
        Array Handle: 0x0007
        Error Information Handle: Not Provided
        Total Width: 64 bits
        Data Width: 64 bits
        Size: 8 GB
        Form Factor: SODIMM
        Set: None
        Locator: ChannelA-DIMM0
        Bank Locator: BANK 0
        Type: DDR3
        Type Detail: Synchronous
        Speed: 2133 MT/s
        Manufacturer: Kingston
        Serial Number: 5D1E6408
        Asset Tag: None
        Part Number: KHX2133C11S3L/8G
        Rank: Unknown
        Configured Memory Speed: 2133 MT/s

    Handle 0x0009, DMI type 17, 34 bytes
    Memory Device
        Array Handle: 0x0007
        Error Information Handle: Not Provided
        Total Width: 64 bits
        Data Width: 64 bits
        Size: 8 GB
        Form Factor: SODIMM
        Set: None
        Locator: ChannelB-DIMM0
        Bank Locator: BANK 2
        Type: DDR3
        Type Detail: Synchronous
        Speed: 2133 MT/s
        Manufacturer: Kingston
        Serial Number: 5F1E7508
        Asset Tag: None
        Part Number: KHX2133C11S3L/8G
        Rank: Unknown
        Configured Memory Speed: 2133 MT/s

    Handle 0x000A, DMI type 19, 31 bytes
    Memory Array Mapped Address
        Starting Address: 0x00000000000
        Ending Address: 0x003FFFFFFFF
        Range Size: 16 GB
        Physical Array Handle: 0x0007
        Partition Width: 2

    Handle 0x000B, DMI type 0, 24 bytes
    BIOS Information
        Vendor: LENOVO
        Version: G1ETC2WW (2.82 )
        Release Date: 08/07/2019
        Address: 0xE0000
        Runtime Size: 128 kB
        ROM Size: 12 MB
        Characteristics:
            PCI is supported
            PNP is supported
            BIOS is upgradeable
            BIOS shadowing is allowed
            Boot from CD is supported
            Selectable boot is supported
            EDD is supported
            3.5"/720 kB floppy services are supported (int 13h)
            Print screen service is supported (int 5h)
            8042 keyboard services are supported (int 9h)
            Serial services are supported (int 14h)
            Printer services are supported (int 17h)
            CGA/mono video services are supported (int 10h)
            ACPI is supported
            USB legacy is supported
            BIOS boot specification is supported
            Targeted content distribution is supported
            UEFI is supported
        BIOS Revision: 2.82
        Firmware Revision: 1.13

    Handle 0x000C, DMI type 1, 27 bytes
    System Information
        Manufacturer: LENOVO
        Product Name: 2342CTO
        Version: ThinkPad T430
        Serial Number: PBDBYFH
        UUID: 5ce1ba81-52d5-11cb-adef-8ffdf69da5a1
        Wake-up Type: Power Switch
        SKU Number: LENOVO_MT_2342
        Family: ThinkPad T430

    Handle 0x000D, DMI type 2, 15 bytes
    Base Board Information
        Manufacturer: LENOVO
        Product Name: 2342CTO
        Version: Not Defined
        Serial Number: 1ZLMB2C36BN
        Asset Tag: Not Available
        Features:
            Board is a hosting board
            Board is replaceable
        Location In Chassis: Not Available
        Chassis Handle: 0x0000
        Type: Motherboard
        Contained Object Handles: 0

    Handle 0x000E, DMI type 3, 22 bytes
    Chassis Information
        Manufacturer: LENOVO
        Type: Notebook
        Lock: Not Present
        Version: Not Available
        Serial Number: PBDBYFH
        Asset Tag: No Asset Information
        Boot-up State: Unknown
        Power Supply State: Unknown
        Thermal State: Unknown
        Security Status: Unknown
        OEM Information: 0x00000000
        Height: Unspecified
        Number Of Power Cords: Unspecified
        Contained Elements: 0
        SKU Number: LENOVO_MT_2342

    Handle 0x000F, DMI type 8, 9 bytes
    Port Connector Information
        Internal Reference Designator: Not Available
        Internal Connector Type: None
        External Reference Designator: External Monitor
        External Connector Type: DB-15 female
        Port Type: Video Port

    Handle 0x0010, DMI type 8, 9 bytes
    Port Connector Information
        Internal Reference Designator: Not Available
        Internal Connector Type: None
        External Reference Designator: Mini DisplayPort
        External Connector Type: Other
        Port Type: Video Port

    Handle 0x0011, DMI type 8, 9 bytes
    Port Connector Information
        Internal Reference Designator: Not Available
        Internal Connector Type: None
        External Reference Designator: DisplayPort/DVI-D 1
        External Connector Type: Other
        Port Type: Video Port

    Handle 0x0012, DMI type 126, 9 bytes
    Inactive

    Handle 0x0013, DMI type 8, 9 bytes
    Port Connector Information
        Internal Reference Designator: Not Available
        Internal Connector Type: None
        External Reference Designator: Headphone/Microphone Combo Jack
        External Connector Type: Mini Jack (headphones)
        Port Type: Audio Port

    Handle 0x0014, DMI type 8, 9 bytes
    Port Connector Information
        Internal Reference Designator: Not Available
        Internal Connector Type: None
        External Reference Designator: Headphone Jack
        External Connector Type: Mini Jack (headphones)
        Port Type: Audio Port

    Handle 0x0015, DMI type 8, 9 bytes
    Port Connector Information
        Internal Reference Designator: Not Available
        Internal Connector Type: None
        External Reference Designator: Microphone Jack
        External Connector Type: Mini Jack (headphones)
        Port Type: Audio Port

    Handle 0x0016, DMI type 8, 9 bytes
    Port Connector Information
        Internal Reference Designator: Not Available
        Internal Connector Type: None
        External Reference Designator: Ethernet
        External Connector Type: RJ-45
        Port Type: Network Port

    Handle 0x0017, DMI type 126, 9 bytes
    Inactive

    Handle 0x0018, DMI type 8, 9 bytes
    Port Connector Information
        Internal Reference Designator: Not Available
        Internal Connector Type: None
        External Reference Designator: USB 1
        External Connector Type: Access Bus (USB)
        Port Type: USB

    Handle 0x0019, DMI type 8, 9 bytes
    Port Connector Information
        Internal Reference Designator: Not Available
        Internal Connector Type: None
        External Reference Designator: USB 2
        External Connector Type: Access Bus (USB)
        Port Type: USB

    Handle 0x001A, DMI type 8, 9 bytes
    Port Connector Information
        Internal Reference Designator: Not Available
        Internal Connector Type: None
        External Reference Designator: USB 3
        External Connector Type: Access Bus (USB)
        Port Type: USB

    Handle 0x001B, DMI type 8, 9 bytes
    Port Connector Information
        Internal Reference Designator: Not Available
        Internal Connector Type: None
        External Reference Designator: USB 4
        External Connector Type: Access Bus (USB)
        Port Type: USB

    Handle 0x001C, DMI type 8, 9 bytes
    Port Connector Information
        Internal Reference Designator: Not Available
        Internal Connector Type: None
        External Reference Designator: USB 5
        External Connector Type: Access Bus (USB)
        Port Type: USB

    Handle 0x001D, DMI type 8, 9 bytes
    Port Connector Information
        Internal Reference Designator: Not Available
        Internal Connector Type: None
        External Reference Designator: USB 6
        External Connector Type: Access Bus (USB)
        Port Type: USB

    Handle 0x001E, DMI type 8, 9 bytes
    Port Connector Information
        Internal Reference Designator: Not Available
        Internal Connector Type: None
        External Reference Designator: USB 7
        External Connector Type: Access Bus (USB)
        Port Type: USB

    Handle 0x001F, DMI type 8, 9 bytes
    Port Connector Information
        Internal Reference Designator: Not Available
        Internal Connector Type: None
        External Reference Designator: USB 8
        External Connector Type: Access Bus (USB)
        Port Type: USB

    Handle 0x0020, DMI type 8, 9 bytes
    Port Connector Information
        Internal Reference Designator: Not Available
        Internal Connector Type: None
        External Reference Designator: USB 9
        External Connector Type: Access Bus (USB)
        Port Type: USB

    Handle 0x0021, DMI type 8, 9 bytes
    Port Connector Information
        Internal Reference Designator: Not Available
        Internal Connector Type: None
        External Reference Designator: USB 10
        External Connector Type: Access Bus (USB)
        Port Type: USB

    Handle 0x0022, DMI type 126, 9 bytes
    Inactive

    Handle 0x0023, DMI type 126, 9 bytes
    Inactive

    Handle 0x0024, DMI type 126, 9 bytes
    Inactive

    Handle 0x0025, DMI type 9, 17 bytes
    System Slot Information
        Designation: ExpressCard Slot
        Type: x1 PCI Express
        Current Usage: Available
        Length: Other
        ID: 1
        Characteristics:
            Hot-plug devices are supported
        Bus Address: 0000:00:00.0

    Handle 0x0026, DMI type 9, 17 bytes
    System Slot Information
        Designation: Media Card Slot
        Type: Other
        Current Usage: Available
        Length: Other
        Characteristics:
            Hot-plug devices are supported
        Bus Address: 0000:00:00.0

    Handle 0x0027, DMI type 126, 17 bytes
    Inactive

    Handle 0x0028, DMI type 10, 6 bytes
    On Board Device Information
        Type: Other
        Status: Disabled
        Description: IBM Embedded Security hardware

    Handle 0x0029, DMI type 12, 5 bytes
    System Configuration Options

    Handle 0x002A, DMI type 13, 22 bytes
    BIOS Language Information
        Language Description Format: Abbreviated
        Installable Languages: 1
            en-US
        Currently Installed Language: en-US

    Handle 0x002B, DMI type 126, 26 bytes
    Inactive

    Handle 0x002C, DMI type 126, 26 bytes
    Inactive

    Handle 0x002D, DMI type 18, 23 bytes
    32-bit Memory Error Information
        Type: OK
        Granularity: Unknown
        Operation: Unknown
        Vendor Syndrome: Unknown
        Memory Array Address: Unknown
        Device Address: Unknown
        Resolution: Unknown

    Handle 0x002E, DMI type 21, 7 bytes
    Built-in Pointing Device
        Type: Track Point
        Interface: PS/2
        Buttons: 3

    Handle 0x002F, DMI type 131, 22 bytes
    ThinkVantage Technologies
        Version: 1
        Diagnostics: No

    Handle 0x0030, DMI type 136, 6 bytes
    OEM-specific Type
        Header and Data:
            88 06 30 00 5A 5A

    Handle 0x0031, DMI type 130, 20 bytes
    OEM-specific Type
        Header and Data:
            82 14 31 00 24 41 4D 54 00 00 00 00 01 A5 FF 03
            00 00 00 00

    Handle 0x0032, DMI type 131, 64 bytes
    OEM-specific Type
        Header and Data:
            83 40 32 00 14 00 00 00 08 00 00 00 00 00 45 00
            F8 00 55 1E FF FF FF FF 21 20 00 00 01 00 08 00
            18 0E 47 00 00 00 00 00 C8 00 02 15 00 00 00 00
            00 00 00 00 62 00 00 00 76 50 72 6F 00 00 00 00

    Handle 0x0033, DMI type 135, 74 bytes
    OEM-specific Type
        Header and Data:
            87 4A 33 00 54 50 07 02 42 41 59 20 49 2F 4F 20
            03 00 06 FF 00 00 00 00 00 00 00 FF 00 00 00 00
            00 00 00 FF 00 00 00 00 00 00 00 FF 00 00 00 00
            00 00 00 FF 00 00 00 00 00 00 00 FF 00 00 00 00
            00 00 00 06 00 02 04 FF 03 FF

    Handle 0x0034, DMI type 133, 5 bytes
    OEM-specific Type
        Header and Data:
            85 05 34 00 01
        Strings:
            KHOIHGIUCCHHII

    Handle 0x0035, DMI type 15, 31 bytes
    System Event Log
        Area Length: 18 bytes
        Header Start Offset: 0x0000
        Header Length: 16 bytes
        Data Start Offset: 0x0010
        Access Method: General-purpose non-volatile data functions
        Access Address: 0x00F0
        Status: Valid, Not Full
        Change Token: 0x00000000
        Header Format: Type 1
        Supported Log Type Descriptors: 4
        Descriptor 1: POST error
        Data Format 1: POST results bitmap
        Descriptor 2: PCI system error
        Data Format 2: None
        Descriptor 3: System reconfigured
        Data Format 3: None
        Descriptor 4: Log area reset/cleared
        Data Format 4: None

    Handle 0x0036, DMI type 140, 67 bytes
    OEM-specific Type
        Header and Data:
            8C 43 36 00 4C 45 4E 4F 56 4F 0B 00 01 A5 DC 18
            54 D5 25 FD 24 44 1C 05 A2 62 B6 47 33 01 00 00
            00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
            00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
            00 00 00

    Handle 0x0037, DMI type 140, 47 bytes
    OEM-specific Type
        Header and Data:
            8C 2F 37 00 4C 45 4E 4F 56 4F 0B 01 01 29 00 34
            E0 A7 BA 89 36 93 61 07 D8 DC 0C CB D7 B0 4E 00
            00 00 00 10 00 10 00 10 01 D0 00 20 01 00 01

    Handle 0x0038, DMI type 140, 63 bytes
    OEM-specific Type
        Header and Data:
            8C 3F 38 00 4C 45 4E 4F 56 4F 0B 02 01 00 00 00
            00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
            00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
            00 00 00 00 00 00 00 00 00 00 00 00 00 00 00

    Handle 0x0039, DMI type 140, 17 bytes
    OEM-specific Type
        Header and Data:
            8C 11 39 00 4C 45 4E 4F 56 4F 0B 03 01 00 00 00
            00

    Handle 0x003A, DMI type 140, 19 bytes
    OEM-specific Type
        Header and Data:
            8C 13 3A 00 4C 45 4E 4F 56 4F 0B 04 01 B2 00 4D
            53 20 00

    Handle 0x003B, DMI type 140, 19 bytes
    OEM-specific Type
        Header and Data:
            8C 13 3B 00 4C 45 4E 4F 56 4F 0B 05 01 06 00 00
            00 00 00

    Handle 0x003C, DMI type 24, 5 bytes
    Hardware Security
        Power-On Password Status: Disabled
        Keyboard Password Status: Not Implemented
        Administrator Password Status: Disabled
        Front Panel Reset Status: Not Implemented

    Handle 0x003D, DMI type 132, 7 bytes
    OEM-specific Type
        Header and Data:
            84 07 3D 00 01 D8 36

    Handle 0x003E, DMI type 135, 18 bytes
    OEM-specific Type
        Header and Data:
            87 12 3E 00 54 50 07 01 01 D2 FF 01 00 00 F5 01
            00 00

    Handle 0x003F, DMI type 140, 15 bytes
    ThinkPad Embedded Controller Program
        Version ID: G1HT35WW
        Release Date: 03/04/2014

    Handle 0x0040, DMI type 140, 43 bytes
    OEM-specific Type
        Header and Data:
            8C 2B 40 00 4C 45 4E 4F 56 4F 0B 08 01 FF FF FF
            FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
            FF FF FF FF FF FF FF FF FF FF FF

    Handle 0xFEFF, DMI type 127, 4 bytes
    End Of Table

[Openbenchmarking.org](https://openbenchmarking.org/result/2210128-NE-2210119NE25)

[![Laptop-lenovo-t430-without-keyboard.jpg](/images/thumb/6/65/Laptop-lenovo-t430-without-keyboard.jpg/300px-Laptop-lenovo-t430-without-keyboard.jpg)](https://wiki.gentoo.org/wiki/File:Laptop-lenovo-t430-without-keyboard.jpg)

[](https://wiki.gentoo.org/wiki/File:Laptop-lenovo-t430-without-keyboard.jpg "Enlarge")

### [Firmware setup]

Press **Enter** during boot to enter BIOS, RAM testing. **F12** to choose boot media.

-   ::::::
    ::::
    :::
    [![](/images/thumb/f/f9/Thinkpad-t430-bios-main.jpg/120px-Thinkpad-t430-bios-main.jpg)](https://wiki.gentoo.org/wiki/File:Thinkpad-t430-bios-main.jpg)
    :::
    ::::

    ::: gallerytext
    Main
    :::
    ::::::

-   ::::::
    ::::
    :::
    [![](/images/thumb/6/6f/Lenovo_ThinkPad_T430_UEFI_BIOS_1.16_Startup_Interrupt_Menu.jpg/120px-Lenovo_ThinkPad_T430_UEFI_BIOS_1.16_Startup_Interrupt_Menu.jpg)](https://wiki.gentoo.org/wiki/File:Lenovo_ThinkPad_T430_UEFI_BIOS_1.16_Startup_Interrupt_Menu.jpg)
    :::
    ::::

    ::: gallerytext
    After pressing ENTER on boot
    :::
    ::::::

-   ::::::
    ::::
    :::
    [![](/images/thumb/b/bf/Thinkpad-t430-bios-config-mainlist.jpg/120px-Thinkpad-t430-bios-config-mainlist.jpg)](https://wiki.gentoo.org/wiki/File:Thinkpad-t430-bios-config-mainlist.jpg)
    :::
    ::::

    ::: gallerytext
    Config
    :::
    ::::::

-   ::::::
    ::::
    :::
    [![](/images/thumb/9/93/Thinkpad-t430-bios-amt-config.jpg/120px-Thinkpad-t430-bios-amt-config.jpg)](https://wiki.gentoo.org/wiki/File:Thinkpad-t430-bios-amt-config.jpg)
    :::
    ::::

    ::: gallerytext
    Config AMT
    :::
    ::::::

-   ::::::
    ::::
    :::
    [![](/images/thumb/6/60/Thinkpad-t430-bios-keyboard-mouse.jpg/120px-Thinkpad-t430-bios-keyboard-mouse.jpg)](https://wiki.gentoo.org/wiki/File:Thinkpad-t430-bios-keyboard-mouse.jpg)
    :::
    ::::

    ::: gallerytext
    Keyboard/Mouse
    :::
    ::::::

-   ::::::
    ::::
    :::
    [![](/images/thumb/c/c5/Thinkpad-t430-bios-startup.jpg/120px-Thinkpad-t430-bios-startup.jpg)](https://wiki.gentoo.org/wiki/File:Thinkpad-t430-bios-startup.jpg)
    :::
    ::::

    ::: gallerytext
    Startup
    :::
    ::::::

-   ::::::
    ::::
    :::
    [![](/images/thumb/4/4c/Thinkpad-t430-bios-config-main.jpg/120px-Thinkpad-t430-bios-config-main.jpg)](https://wiki.gentoo.org/wiki/File:Thinkpad-t430-bios-config-main.jpg)
    :::
    ::::

    ::: gallerytext
    Power
    :::
    ::::::

-   ::::::
    ::::
    :::
    [![](/images/thumb/6/60/Lenovo-thinkpad-t430--diagnostics.jpg/120px-Lenovo-thinkpad-t430--diagnostics.jpg)](https://wiki.gentoo.org/wiki/File:Lenovo-thinkpad-t430--diagnostics.jpg)
    :::
    ::::

    ::: gallerytext
    Diagnostic main screen
    :::
    ::::::

-   ::::::
    ::::
    :::
    [![](/images/thumb/8/80/Lenovo-thinkpad-t430--diagnostics--cpu-quick-test-checkboxes.jpg/120px-Lenovo-thinkpad-t430--diagnostics--cpu-quick-test-checkboxes.jpg)](https://wiki.gentoo.org/wiki/File:Lenovo-thinkpad-t430--diagnostics--cpu-quick-test-checkboxes.jpg)
    :::
    ::::

    ::: gallerytext
    Diagnostic CPU quick test checkboxes
    :::
    ::::::

-   ::::::
    ::::
    :::
    [![](/images/thumb/8/83/Lenovo-thinkpad-t430--diagnostics--cpu-quick-test.jpg/120px-Lenovo-thinkpad-t430--diagnostics--cpu-quick-test.jpg)](https://wiki.gentoo.org/wiki/File:Lenovo-thinkpad-t430--diagnostics--cpu-quick-test.jpg)
    :::
    ::::

    ::: gallerytext
    Diagnostic CPU quick test
    :::
    ::::::

-   ::::::
    ::::
    :::
    [![](/images/thumb/7/77/Lenovo-thinkpad-t430--diagnostics--generate-config-file.jpg/120px-Lenovo-thinkpad-t430--diagnostics--generate-config-file.jpg)](https://wiki.gentoo.org/wiki/File:Lenovo-thinkpad-t430--diagnostics--generate-config-file.jpg)
    :::
    ::::

    ::: gallerytext
    Diagnostics: generate configuration file
    :::
    ::::::

-   ::::::
    ::::
    :::
    [![](/images/thumb/0/03/Lenovo-thinkpad-t430--diagnostics--machine-info.jpg/120px-Lenovo-thinkpad-t430--diagnostics--machine-info.jpg)](https://wiki.gentoo.org/wiki/File:Lenovo-thinkpad-t430--diagnostics--machine-info.jpg)
    :::
    ::::

    ::: gallerytext
    Diagnostics: machine info tab
    :::
    ::::::

-   ::::::
    ::::
    :::
    [![](/images/thumb/2/26/Lenovo-thinkpad-t430--diagnostics--cpu.jpg/120px-Lenovo-thinkpad-t430--diagnostics--cpu.jpg)](https://wiki.gentoo.org/wiki/File:Lenovo-thinkpad-t430--diagnostics--cpu.jpg)
    :::
    ::::

    ::: gallerytext
    CPU tab
    :::
    ::::::

-   ::::::
    ::::
    :::
    [![](/images/thumb/f/f6/Lenovo-thinkpad-t430--diagnostics--fan.jpg/120px-Lenovo-thinkpad-t430--diagnostics--fan.jpg)](https://wiki.gentoo.org/wiki/File:Lenovo-thinkpad-t430--diagnostics--fan.jpg)
    :::
    ::::

    ::: gallerytext
    FAN tab
    :::
    ::::::

-   ::::::
    ::::
    :::
    [![](/images/thumb/3/3f/Lenovo-thinkpad-t430--diagnostics--lcd.jpg/120px-Lenovo-thinkpad-t430--diagnostics--lcd.jpg)](https://wiki.gentoo.org/wiki/File:Lenovo-thinkpad-t430--diagnostics--lcd.jpg)
    :::
    ::::

    ::: gallerytext
    LCD tab
    :::
    ::::::

-   ::::::
    ::::
    :::
    [![](/images/thumb/d/d8/Lenovo-thinkpad-t430--system-information--ram.jpg/120px-Lenovo-thinkpad-t430--system-information--ram.jpg)](https://wiki.gentoo.org/wiki/File:Lenovo-thinkpad-t430--system-information--ram.jpg)
    :::
    ::::

    ::: gallerytext
    RAM
    :::
    ::::::

-   ::::::
    ::::
    :::
    [![](/images/thumb/8/85/Lenovo-thinkpad-t430--system-information--motherboard.jpg/120px-Lenovo-thinkpad-t430--system-information--motherboard.jpg)](https://wiki.gentoo.org/wiki/File:Lenovo-thinkpad-t430--system-information--motherboard.jpg)
    :::
    ::::

    ::: gallerytext
    MOBO
    :::
    ::::::

-   ::::::
    ::::
    :::
    [![](/images/thumb/f/f4/Lenovo-thinkpad-t430--system-information--pci-express.jpg/120px-Lenovo-thinkpad-t430--system-information--pci-express.jpg)](https://wiki.gentoo.org/wiki/File:Lenovo-thinkpad-t430--system-information--pci-express.jpg)
    :::
    ::::

    ::: gallerytext
    PCI Express
    :::
    ::::::

-   ::::::
    ::::
    :::
    [![](/images/thumb/d/db/Lenovo-thinkpad-t430--diagnostics--cpu-extended.jpg/120px-Lenovo-thinkpad-t430--diagnostics--cpu-extended.jpg)](https://wiki.gentoo.org/wiki/File:Lenovo-thinkpad-t430--diagnostics--cpu-extended.jpg)
    :::
    ::::

    ::: gallerytext
    Diagnostic: CPU test
    :::
    ::::::

-   ::::::
    ::::
    :::
    [![](/images/thumb/6/6e/Lenovo-thinkpad-t430--diagnostics--ram.jpg/120px-Lenovo-thinkpad-t430--diagnostics--ram.jpg)](https://wiki.gentoo.org/wiki/File:Lenovo-thinkpad-t430--diagnostics--ram.jpg)
    :::
    ::::

    ::: gallerytext
    Diagnostic: RAM
    :::
    ::::::

### [lscpu]

`root `[`#`]`lscpu`

    Architecture:        x86_64
    CPU op-mode(s):      32-bit, 64-bit
    Byte Order:          Little Endian
    CPU(s):              4
    On-line CPU(s) list: 0-3
    Thread(s) per core:  2
    Core(s) per socket:  2
    Socket(s):           1
    Vendor ID:           GenuineIntel
    CPU family:          6
    Model:               58
    Model name:          Intel(R) Core(TM) i5-3320M CPU @ 2.60GHz
    Stepping:            9
    CPU MHz:             1306.347
    CPU max MHz:         3300.0000
    CPU min MHz:         1200.0000
    BogoMIPS:            5188.11
    Virtualization:      VT-x
    L1d cache:           32K
    L1i cache:           32K
    L2 cache:            256K
    L3 cache:            3072K
    Flags:               fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush dts acpi mmx fxsr sse sse2 ss ht tm pbe syscall nx rdtscp lm constant_tsc arch_perfmon pebs bts rep_good nopl xtopology nonstop_tsc cpuid aperfmperf pni pclmulqdq dtes64 monitor ds_cpl vmx smx est tm2 ssse3 cx16 xtpr pdcm pcid sse4_1 sse4_2 x2apic popcnt tsc_deadline_timer aes xsave avx f16c rdrand lahf_lm cpuid_fault epb tpr_shadow vnmi flexpriority ept vpid fsgsbase smep erms xsaveopt dtherm ida arat pln pts

[Product page for stock i5 CPU](https://ark.intel.com/content/www/us/en/ark/products/64896/intel-core-i5-3320m-processor-3m-cache-up-to-3-30-ghz.html).

[Ivy Bridge page on Wikipedia](https://en.wikipedia.org/wiki/Ivy_Bridge_(microarchitecture) "wikipedia:Ivy Bridge (microarchitecture)").

[Compare stock CPU with 3840QM](https://ark.intel.com/content/www/us/en/ark/compare.html?productIds=70846,64896), [Compare 3840QM with 3940XM (highest possible for the mobo)](https://www.intel.com/content/www/us/en/products/compare.html?productIds=70846,71096), [userbenchmark.com](https://cpu.userbenchmark.com/Compare/Intel-Core-i7-3840QM-vs-Intel-Core-i5-3320M/m2451vsm402), [notebookcheck.net](https://www.notebookcheck.net/3320M-vs-3840QM_3076_3346.247596.0.html), [technical.city](https://technical.city/en/cpu/Core-i7-3840QM-vs-Core-i5-3320M), [cpubenchmark.net](https://www.cpubenchmark.net/compare/Intel-i7-3840QM-vs-Intel-i5-3320M/900vs817), [cpu-world.com](https://www.cpu-world.com/Compare/567/Intel_Core_i5_Mobile_i5-3320M_(BGA)_vs_Intel_Core_i7_Mobile_i7-3840QM_(PGA).html), [cpuboss.com](http://cpuboss.com/cpus/Intel-Core-i7-3840QM-vs-Intel-Core-i5-3320M).

[![](/images/thumb/0/06/Intel-cpu-3940xm-top.jpg/300px-Intel-cpu-3940xm-top.jpg)](https://wiki.gentoo.org/wiki/File:Intel-cpu-3940xm-top.jpg)

[](https://wiki.gentoo.org/wiki/File:Intel-cpu-3940xm-top.jpg "Enlarge")

CPU 3940XM top

[![](/images/thumb/5/5f/Intel-cpu-3940xm-bottom.jpg/300px-Intel-cpu-3940xm-bottom.jpg)](https://wiki.gentoo.org/wiki/File:Intel-cpu-3940xm-bottom.jpg)

[](https://wiki.gentoo.org/wiki/File:Intel-cpu-3940xm-bottom.jpg "Enlarge")

CPU 3940XM bottom

[![](/images/thumb/6/62/Lenovo-thinkpad-t430-cpu.jpg/600px-Lenovo-thinkpad-t430-cpu.jpg)](https://wiki.gentoo.org/wiki/File:Lenovo-thinkpad-t430-cpu.jpg)

[](https://wiki.gentoo.org/wiki/File:Lenovo-thinkpad-t430-cpu.jpg "Enlarge")

Without heat sink and fan

[![](/images/thumb/f/f4/Lenovo-thinkpad-t430-cpu-and-hsf.jpg.jpg/600px-Lenovo-thinkpad-t430-cpu-and-hsf.jpg.jpg)](https://wiki.gentoo.org/wiki/File:Lenovo-thinkpad-t430-cpu-and-hsf.jpg.jpg)

[](https://wiki.gentoo.org/wiki/File:Lenovo-thinkpad-t430-cpu-and-hsf.jpg.jpg "Enlarge")

HSF with double pipe for lower temperature.

[![](/images/thumb/0/0c/Thinkpad-t430-heatsync-with-copper-tape.jpg/800px-Thinkpad-t430-heatsync-with-copper-tape.jpg)](https://wiki.gentoo.org/wiki/File:Thinkpad-t430-heatsync-with-copper-tape.jpg)

[](https://wiki.gentoo.org/wiki/File:Thinkpad-t430-heatsync-with-copper-tape.jpg "Enlarge")

Popular hardware mod: copper tape for heat disolving

During Gentoo compilation your T430 may became very hot and even turn off, especially on higher CPU - so you will need to replace HSF too, to have 2 pipes:

[![](/images/thumb/1/19/Lenovo-thinkpad-t430-hsfs--front.jpg/600px-Lenovo-thinkpad-t430-hsfs--front.jpg)](https://wiki.gentoo.org/wiki/File:Lenovo-thinkpad-t430-hsfs--front.jpg)

[](https://wiki.gentoo.org/wiki/File:Lenovo-thinkpad-t430-hsfs--front.jpg "Enlarge")

Two tubes better for cooling

[![Lenovo-thinkpad-t430-hsf-back.jpg](/images/thumb/8/8b/Lenovo-thinkpad-t430-hsf-back.jpg/600px-Lenovo-thinkpad-t430-hsf-back.jpg)](https://wiki.gentoo.org/wiki/File:Lenovo-thinkpad-t430-hsf-back.jpg)

[](https://wiki.gentoo.org/wiki/File:Lenovo-thinkpad-t430-hsf-back.jpg "Enlarge")

Ivy Bridge does not have any undervolting features, but you can limit TDP^[\[1\]](#cite_note-1)^. TODO add how.

### [lspci]

`root `[`#`]`lspci -nnk`

    00:00.0 Host bridge [0600]: Intel Corporation 3rd Gen Core processor DRAM Controller [8086:0154] (rev 09)
            Subsystem: Lenovo 3rd Gen Core processor DRAM Controller [17aa:21f3]
            Kernel driver in use: ivb_uncore
    00:02.0 VGA compatible controller [0300]: Intel Corporation 3rd Gen Core processor Graphics Controller [8086:0166] (rev 09)
            Subsystem: Lenovo 3rd Gen Core processor Graphics Controller [17aa:21f3]
            Kernel driver in use: i915
    00:14.0 USB controller [0c03]: Intel Corporation 7 Series/C210 Series Chipset Family USB xHCI Host Controller [8086:1e31] (rev 04)
            Subsystem: Lenovo 7 Series/C210 Series Chipset Family USB xHCI Host Controller [17aa:21f3]
            Kernel driver in use: xhci_hcd
    00:16.0 Communication controller [0780]: Intel Corporation 7 Series/C216 Chipset Family MEI Controller #1 [8086:1e3a] (rev 04)
            Subsystem: Lenovo 7 Series/C216 Chipset Family MEI Controller [17aa:21f3]
            Kernel driver in use: mei_me
    00:19.0 Ethernet controller [0200]: Intel Corporation 82579LM Gigabit Network Connection [8086:1502] (rev 04)
            Subsystem: Lenovo 82579LM Gigabit Network Connection [17aa:21f3]
            Kernel driver in use: e1000e
    00:1a.0 USB controller [0c03]: Intel Corporation 7 Series/C216 Chipset Family USB Enhanced Host Controller #2 [8086:1e2d] (rev 04)
            Subsystem: Lenovo 7 Series/C216 Chipset Family USB Enhanced Host Controller [17aa:21f3]
            Kernel driver in use: ehci-pci
    00:1b.0 Audio device [0403]: Intel Corporation 7 Series/C216 Chipset Family High Definition Audio Controller [8086:1e20] (rev 04)
            Subsystem: Lenovo 7 Series/C216 Chipset Family High Definition Audio Controller [17aa:21f3]
            Kernel driver in use: snd_hda_intel
    00:1c.0 PCI bridge [0604]: Intel Corporation 7 Series/C216 Chipset Family PCI Express Root Port 1 [8086:1e10] (rev c4)
            Kernel driver in use: pcieport
    00:1c.1 PCI bridge [0604]: Intel Corporation 7 Series/C210 Series Chipset Family PCI Express Root Port 2 [8086:1e12] (rev c4)
            Kernel driver in use: pcieport
    00:1c.2 PCI bridge [0604]: Intel Corporation 7 Series/C210 Series Chipset Family PCI Express Root Port 3 [8086:1e14] (rev c4)
            Kernel driver in use: pcieport
    00:1d.0 USB controller [0c03]: Intel Corporation 7 Series/C216 Chipset Family USB Enhanced Host Controller #1 [8086:1e26] (rev 04)
            Subsystem: Lenovo 7 Series/C216 Chipset Family USB Enhanced Host Controller [17aa:21f3]
            Kernel driver in use: ehci-pci
    00:1f.0 ISA bridge [0601]: Intel Corporation QM77 Express Chipset LPC Controller [8086:1e55] (rev 04)
            Subsystem: Lenovo QM77 Express Chipset LPC Controller [17aa:21f3]
            Kernel driver in use: lpc_ich
    00:1f.2 SATA controller [0106]: Intel Corporation 7 Series Chipset Family 6-port SATA Controller [AHCI mode] [8086:1e03] (rev 04)
            Subsystem: Lenovo 7 Series Chipset Family 6-port SATA Controller [AHCI mode] [17aa:21f3]
            Kernel driver in use: ahci
    00:1f.3 SMBus [0c05]: Intel Corporation 7 Series/C216 Chipset Family SMBus Controller [8086:1e22] (rev 04)
            Subsystem: Lenovo 7 Series/C216 Chipset Family SMBus Controller [17aa:21f3]
            Kernel driver in use: i801_smbus
    02:00.0 System peripheral [0880]: Ricoh Co Ltd PCIe SDXC/MMC Host Controller [1180:e823] (rev 04)
            Subsystem: Lenovo PCIe SDXC/MMC Host Controller [17aa:21f3]
            Kernel driver in use: sdhci-pci
    03:00.0 Network controller [0280]: Intel Corporation Centrino Advanced-N 6205 [Taylor Peak] [8086:0085] (rev 34)
            Subsystem: Intel Corporation Centrino Advanced-N 6205 AGN [8086:1311]
            Kernel driver in use: iwlwifi

### [lsusb]

`root `[`#`]`lsusb`

    Bus 002 Device 002: ID 8087:0024 Intel Corp. Integrated Rate Matching Hub
    Bus 002 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub
    Bus 001 Device 005: ID 04f2:b2db Chicony Electronics Co., Ltd
    Bus 001 Device 004: ID 0a5c:21e6 Broadcom Corp. BCM20702 Bluetooth 4.0 [ThinkPad]
    Bus 001 Device 003: ID 147e:2020 Upek TouchChip Fingerprint Coprocessor (WBF advanced mode)
    Bus 001 Device 002: ID 8087:0024 Intel Corp. Integrated Rate Matching Hub
    Bus 001 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub
    Bus 004 Device 001: ID 1d6b:0003 Linux Foundation 3.0 root hub
    Bus 003 Device 002: ID 0bdb:1926 Ericsson Business Mobile Networks BV H5321 gw Mobile Broadband Driver
    Bus 003 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub

### [RAM]

[![](/images/thumb/2/23/Thinkpad-t430-ram.jpg/300px-Thinkpad-t430-ram.jpg)](https://wiki.gentoo.org/wiki/File:Thinkpad-t430-ram.jpg)

[](https://wiki.gentoo.org/wiki/File:Thinkpad-t430-ram.jpg "Enlarge")

Opened back with slot for RAM

ThinkPad T430 supports [up to 16 GB of SO-DIMM DDR3/DDR3L memory](https://www.reddit.com/r/thinkpad/comments/hrb0fd/can_you_upgrade_ram_on_t430/). Max frequency for *some* machines is 2133 MHz, but [personally I got black screen without loading with 2133 MHz memory](https://www.reddit.com/r/thinkpad/comments/oh7rjn/t430_replaced_ram_to_2133_from_hyperx_and_got/h4nlivw/?context=3), so check in shop before buy. [DDR3L](https://en.wikipedia.org/wiki/DDR3_SDRAM#DDR3L_and_DDR3U_extensions "wikipedia:DDR3 SDRAM") is better because it is 1.35V instead of 1.5V so it uses 10 percent less battery [with the same performance as DDR3](https://medium.com/@n4ru/the-definitive-t430-modding-guide-3dff3f6a8e2e). To check how much of memory the laptop has:

`root `[`#`]`dmidecode -t memory | grep -i size`

     Size: 4096 MB
        Size: No Module Installed

This shows one 4GB module is installed and a second is unpopulated but available.

To find out the frequency of installed RAM modulesː

`root `[`#`]`dmidecode -t memory | grep 'Memory Speed'`

      Configured Memory Speed: 1600 MT/s
        Configured Memory Speed: Unknown

When a second RAM module is installed, they will operate on the same frequency (the lowest one from both), but size can differ (for example 4 GB plus 8 GB).

See [video about how to replace RAM](https://www.youtube.com/watch?v=KVVL-qPqK-k).

[![](/images/thumb/f/f0/Lenovo-thinkpad-t430-ram-front.jpg/600px-Lenovo-thinkpad-t430-ram-front.jpg)](https://wiki.gentoo.org/wiki/File:Lenovo-thinkpad-t430-ram-front.jpg)

[](https://wiki.gentoo.org/wiki/File:Lenovo-thinkpad-t430-ram-front.jpg "Enlarge")

The best possible RAM for this laptop: HyperX 2133 DDR3L, two planks by 8 GB each.

### [Hard Drive]

Better replace for SSD for higher speed, [2.5 inch](https://commons.wikimedia.org/wiki/File:Intel_DC_S3700_SSD_series,_bottom_side_of_a_100_GB_SATA_3.0_model.jpg) (SATA III: 6Gb/s) or [mSATA](https://en.wikipedia.org/wiki/Serial_ATA#Mini-SATA_.28mSATA.29 "wikipedia:Serial ATA") (SATA II: 3Gb/s). Good models: [Samsung EVO 870](https://www.samsung.com/semiconductor/minisite/ssd/product/consumer/870evo/), [MX500](https://www.crucial.com/products/ssd/crucial-mx500-ssd), [BX500](https://www.crucial.com/products/ssd/bx500-ssd)^[\[2\]](#cite_note-2)^, according to Windows [benchmark](https://ssd.userbenchmark.com/Compare/Samsung-870-EVO-2TB-vs-Crucial-MX500-2TB/m1463967vsm421719) - Samsung is the best.

Also you can replace DVD ullrabay to SSD caddy^[\[3\]](#cite_note-3)^ - SATA III^[\[4\]](#cite_note-4)^, and have two storages.

Or [ExpressCard to NVMe Adapter](https://thinkmods.store/collections/all-mods-1/products/expresscard-to-nvme-adapter) - so you will be able to install some m.2 storage (speed: Sata III - 6 Gb/s).

So totally you can have 4 drives inside this laptop (plus USB).

#### [Trim]

If you have SSD --- sometimes you need to [trim](https://en.wikipedia.org/wiki/Trim_(computing) "wikipedia:Trim (computing)") it for faster writing. Do not mount with *discard* option - it will be slower and can be harmful. Better trim on poweroff, on Fridays:

[FILE] **`/etc/local.d/10-run_on_shutdown.stop`**

    #!/bin/bash

    # From
    # https://fitzcarraldoblog.wordpress.com/2018/01/13/running-a-shell-script-at-shutdown-only-not-at-reboot-a-comparison-between-openrc-and-systemd/
    if [ `who -r | awk ''` = "0" ] && [ "$(date +%a)" = "Fri" ]; then
        echo /etc/local.d/10-run_on_shutdown.stop: run SSD trim
        fstrim / --verbose
        sleep 5
    fi

make it executable:

`user `[`$`]`chmod +x /etc/local.d/10-run_on_shutdown.stop`

[/etc/local.d](https://wiki.gentoo.org/wiki//etc/local.d "/etc/local.d") --- **[/etc/local.d/]** can contain small programs or light scripts to be run when the local service is started or stopped. .

By default prints are hidden, to show them:

[FILE] **`/etc/conf.d/local`**

    rc_verbose=yes

### [Battery]

Get current battery level (useful when using [i3](https://wiki.gentoo.org/wiki/I3 "I3") or [Sway](https://wiki.gentoo.org/wiki/Sway "Sway") window managers without GUI battery indicator)^[\[5\]](#cite_note-5)^ː

`user `[`$`]`cat /sys/class/power_supply/BAT0/capacity`

89

For all details about the batteryː

`user `[`$`]`find /sys/class/power_supply/BAT0/ -type f | xargs -tn1 cat`

    cat /sys/class/power_supply/BAT0/energy_full
    75390000
    cat /sys/class/power_supply/BAT0/manufacturer
    SANYO
    cat /sys/class/power_supply/BAT0/cycle_count
    0
    cat /sys/class/power_supply/BAT0/power_now
    16751000
    cat /sys/class/power_supply/BAT0/capacity_level
    Normal
    cat /sys/class/power_supply/BAT0/model_name
    45N1173
    cat /sys/class/power_supply/BAT0/voltage_min_design
    10800000
    cat /sys/class/power_supply/BAT0/present
    1
    cat /sys/class/power_supply/BAT0/energy_now
    70150000
    cat /sys/class/power_supply/BAT0/energy_full_design
    93960000
    cat /sys/class/power_supply/BAT0/capacity
    93
    cat /sys/class/power_supply/BAT0/charge_start_threshold
    0
    cat /sys/class/power_supply/BAT0/technology
    Li-ion
    cat /sys/class/power_supply/BAT0/power/runtime_suspended_time
    0
    cat /sys/class/power_supply/BAT0/power/autosuspend_delay_ms
    cat: /sys/class/power_supply/BAT0/power/autosuspend_delay_ms: Input/output error
    cat /sys/class/power_supply/BAT0/power/runtime_active_time
    0
    cat /sys/class/power_supply/BAT0/power/control
    auto
    cat /sys/class/power_supply/BAT0/power/runtime_status
    unsupported
    cat /sys/class/power_supply/BAT0/type
    Battery
    cat /sys/class/power_supply/BAT0/status
    Charging
    cat /sys/class/power_supply/BAT0/charge_stop_threshold
    100
    cat /sys/class/power_supply/BAT0/serial_number
    32255
    cat /sys/class/power_supply/BAT0/voltage_now
    12473000
    cat /sys/class/power_supply/BAT0/alarm
    3769000
    cat /sys/class/power_supply/BAT0/uevent
    POWER_SUPPLY_NAME=BAT0
    POWER_SUPPLY_STATUS=Charging
    POWER_SUPPLY_PRESENT=1
    POWER_SUPPLY_TECHNOLOGY=Li-ion
    POWER_SUPPLY_CYCLE_COUNT=0
    POWER_SUPPLY_VOLTAGE_MIN_DESIGN=10800000
    POWER_SUPPLY_VOLTAGE_NOW=12473000
    POWER_SUPPLY_POWER_NOW=16751000
    POWER_SUPPLY_ENERGY_FULL_DESIGN=93960000
    POWER_SUPPLY_ENERGY_FULL=75390000
    POWER_SUPPLY_ENERGY_NOW=70150000
    POWER_SUPPLY_CAPACITY=93
    POWER_SUPPLY_CAPACITY_LEVEL=Normal
    POWER_SUPPLY_MODEL_NAME=45N1173
    POWER_SUPPLY_MANUFACTURER=SANYO
    POWER_SUPPLY_SERIAL_NUMBER=32255

## [Installation]

### [Firmware]

#### [Wi-Fi]

The Linux firmware package is needed since the [Centrino Advanced-N 6205 AGN](https://ark.intel.com/content/www/us/en/ark/products/59471/intel-centrino-advancedn-6205-dual-band.html) wifi adapter requires a specific firmware file.

Firmware file that is needed is the [iwlwifi-6000g2a-6.ucode]. It can be obtained by installing the Linux firmware package: [[[sys-firmware/linux-firmware]](https://packages.gentoo.org/packages/sys-firmware/linux-firmware)[]] or [[[sys-firmware/iwl6005-ucode]](https://packages.gentoo.org/packages/sys-firmware/iwl6005-ucode)[]].

[FILE] **`/etc/portage/make.conf`**

    # ipw3945 needed for ThinkPad wireless firmware
    ACCEPT_LICENSE="@FREE ipw3945"

Wireless module can be another one, note that **Intel Centrino Advanced-N 6205** does not have bluetooth. If you want bluetooth - you can buy [Intel Dual Band Wireless-AC 7260](https://www.intel.com/content/www/us/en/products/sku/75439/intel-dual-band-wirelessac-7260/specifications.html). Also you can get a wireless module that does not need a proprietary blobs, for example [something that uses the ath9k driver](https://deviwiki.com/wiki/Ath9k) - in the table look for **Mini PCIe (half)**. ^[\[6\]](#cite_note-6)^

You can replace mini-PCI (half) WLAN module to [something that do not need proprietary blobs](https://www.reddit.com/r/Gentoo/comments/repy1s/thinkpad_t430_what_is_the_best_wlan_module/), for example with the chipset AR5BHB116 or [AR9462](https://www.amazon.com/dp/B00PVWE31E).

[![](/images/thumb/a/ac/Laptop-lenovo-t430-wifi-stock.jpg/600px-Laptop-lenovo-t430-wifi-stock.jpg)](https://wiki.gentoo.org/wiki/File:Laptop-lenovo-t430-wifi-stock.jpg)

[](https://wiki.gentoo.org/wiki/File:Laptop-lenovo-t430-wifi-stock.jpg "Enlarge")

Stock Wi-Fi module: Intel Centrino Advanced-N 6205 \[Taylor Peak\] (rev 34)

After every kernel update (after [make]) execute

`root `[`#`]`make modules_install`

For more info see [iwlwifi](https://wiki.gentoo.org/wiki/Iwlwifi "Iwlwifi").

** Note**\
When error messages saying the kernel isn\'t able to find the [iwlwifi-6000g2a-6.ucode], check content of [/lib/firmware/].

To make connection emerge [wpa_supplicant](https://wiki.gentoo.org/wiki/Wpa_supplicant "Wpa supplicant"):

`root `[`#`]`emerge --ask net-wireless/wpa_supplicant`

Edit config file, this is an example (see more at **man 5 wpa_supplicant.conf** and **/usr/share/doc/wpa_supplicant-2.10-r1/wpa_supplicant.conf.bz2**):

[FILE] **`/etc/wpa_supplicant/wpa_supplicant.conf`**

    ctrl_interface=/var/run/wpa_supplicant

    ctrl_interface_group=0

    ap_scan=1

    network=

    network=

    network=

    network=

Connect to Wi-Fi with this command:

`root `[`#`]`/etc/init.d/wpa_supplicant start`

See status/log at

`root `[`#`]`wpa_cli status`

To see status updates in real time (useful to see when trying to connect) - run **wpa_cli** and inside **status**:

`root `[`#`]`wpa_cli`

    wpa_cli v2.10
    Copyright (c) 2004-2022, Jouni Malinen <j@w1.fi> and contributors

    This software may be distributed under the terms of the BSD license.
    See README for more details.

    Selected interface 'wlp3s0'

    Interactive mode

    > status
    bssid=7c:52:59:4d:e9:68
    freq=2447
    ssid=about.me/zdanevich
    id=0
    mode=station
    wifi_generation=4
    pairwise_cipher=CCMP
    group_cipher=CCMP
    key_mgmt=WPA2-PSK
    wpa_state=COMPLETED
    ip_address=192.168.100.4
    address=a4:4e:31:a0:59:b0

#### [Ethernet]

`root `[`#`]`cd /etc/init.d/`

To try to use [Ethernet](https://www.reddit.com/r/Gentoo/comments/ivslca/wifi_works_ethernet_do_not/) on laptop boot (run by init system):

`root `[`#`]`rc-update add net.enp0s25`

#### [Bluetooth]

Not integrated in my model - I bought a small USB adapter [UB500](https://wiki.gentoo.org/wiki/UB500 "UB500").

If in dmesg you see:

`root `[`#`]`dmesg`

    bluetooth hci0: Direct firmware load for brcm/BCM20702A1-0a5c-21e6.hcd failed with error -2

Thus a Linux firmware file [BCM20702A1-0a5c-21e6.hcd] is needed. See [Broadcom Bluetooth](https://wiki.gentoo.org/wiki/Broadcom_Bluetooth "Broadcom Bluetooth") for additional info.

#### [Sound]

If you plan to use Firefox for meetings - you need PulseAudio, because Firefox has the [issue](https://bugs.gentoo.org/769389) that when built with Alsa - your microphone will not work.

#### [Microcode]

Intel released microcode updates that fixes fault on processors. Install the officially published microcode package [[[sys-firmware/intel-microcode]](https://packages.gentoo.org/packages/sys-firmware/intel-microcode)[]]. For more info see [Intel microcode](https://wiki.gentoo.org/wiki/Intel_microcode "Intel microcode").

### [Kernel]

Gentoo specific Menuconfig. More info at [Kernel](https://wiki.gentoo.org/wiki/Kernel "Kernel").

[KERNEL] **Based on 4.12.1:**

    Processor type and features  --->
      [*] Symmetric multi-processing support
      [*] Support x2apic
      Processor family  --->
        (X) Core 2/newer Xeon
      [*] SMT (Hyperthreading) scheduler support
      [*] Multi-core scheduler support
      Preemption Model  --->
        (X) Preemptible Kernel (Low-Latency Desktop)
      [*] Machine Check / overheating reporting
      [*]   Intel MCE features
      [*] CPU microcode loading support
      [*]   Intel microcode loading support
      Timer frequency
        (X) 1000 HZ

    Power management and ACPI options  --->
      [*] ACPI (Advanced Configuration and Power Interface) Support  --->
        <*> AC Adapter
        <*> Battery
        -*- Button
        -*- Video
        <*> Fan
        [*] Dock
        <*> Processor
        <*> Processor Aggregator
        <*> Thermal Zone
      CPU Frequency scaling  --->
        Default CPUFreq governor  --->
          (X) powersave
        <*> 'performance' governor
        -*- 'powersave' governor
        *** CPU frequency scaling drivers ***
        -*- Intel P state control
      [*] Cpuidle Driver for Intel Processors
      Memory power savings  --->
        <*> Intel chipset idle memory power saving driver

    Bus options (PCI etc.)  --->
      [*] PCI support
      [*]   Support mmconfig PCI config space access
      [*]   PCI Express Port Bus support
      [*]   Message Signaled Interrupts (MSI and MSI-X)
      [*]   Interrupts on hypertransport devices
      <*> PCCard (PCMCIA/CardBus) support  --->
        -*-   32-bit CardBus support
        <*>   CardBus yenta-compatible bridge support

    [*] Networking support  --->
      <*> Bluetooth subsystem support  --->
        Bluetooth device drivers  --->
          <M> HCI USB driver
          [*] Broadcom protocol support
          [*] Realteck protocol support
      <*> Wireless  --->
        <M> cfg80211 - wireless configuration API
        <M> Generic IEEE 802.11 Networking Stack (mac80211)
      <*> RF switch subsystem support

    Device Drivers  --->
       Generic Driver Options  --->
         -*- Userspace firmware loading support
         [*]   Include in-kernel firmware blobs in kernel binary
         (intel-ucode/06-3a-09) External firmware blobs to build into the kernel binary
         (/lib/firmware) Firmware blobs root directory
       Misc Devices --->
         -*- Intel Management Engine Interface
         <*> ME Enabled Intel Chipsets
       SCSI device support  --->
         <*> SCSI disk support
         <*> SCSI media changer support
         [*] Asynchronous SCSI scanning
       <*> Serial ATA and Parallel ATA drivers (libata)  --->
          <*> AHCI SATA support
       [*] Network device support  --->
         [*] Ethernet driver support  --->
           [*] Intel devices
             <M> Intel(R) PRO/1000 PCI-Express Gigabit Ethernet support
         <*>   USB Network Adapters  --->
           <*>   Multi-purpose USB Networking Framework
           -*-     CDC NCM support
           <*>     CDC MBIM support
         [*] Wireless LAN  --->
           <M> Intel Wireless WiFi Next Gen AGN - Wireless-N/Advanced-N/Ultimate-N (iwlwifi)
           <M> Intel Wireless WiFi DVM Firmware support
           <M> Intel Wireless WiFi MVM Firmware support
       Input device support  --->
         <*>   Mouse interface
         [*]   Keyboards  --->
           <*>   AT keyboard
         [*]   Mice  --->
           <*>   PS/2 mouse

       I2C support  --->
         I2C Hardware Bus support  --->
            <*> Intel 82801 (ICH/PCH)
       -*- Hardware Monitoring support  --->
         <*> Intel Core/Core2/Atom temperature sensor
       -*- Generic Thermal sysfs driver
         [*] X86 package temperature thermal driver
         [*] Intel PCH Thermal Reporting Driver
       [*] Watchdog Timer Support  --->
         <*> Intel TCO Timer/Watchdog
       Multifunction device drivers  --->
         <*> Intel ICH LP
       <*> Multimedia support  --->
         [*]   Cameras/video grabbers support
         [*]   Media USB Adapters  --->
           <*>   USB Video Class (UVC)
           [*]     UVC input events device support
       Graphics support  --->
         <*> /dev/agpgart (AGP Support)  --->
           <*>   Intel 440LX/BX/GX, I8xx and E7x05 chipset support
         <*> Direct Rendering Manager (XFree86 4.1.0 and higher DRI support)
           [*] Enable legacy fbdev support for your modesetting driver
         <*> Intel 8xx/9xx/G3x/G4x/HD Graphics
           [*]   Enable capturing GPU state following a hang
           [*]     Compress GPU error state
           [*]   Always enable userptr support
         Frame buffer Devices  --->
           [*] EFI-based Framebuffer Support
         Console display driver support  --->
           <*> Framebuffer Console support
       <*> Sound card support  --->
         <*> Advanced Linux Sound Architecture  --->
           [*]   PCI sound devices  --->
                 HD-Audio  --->
                   <*> HD Audio PCI
                   <*> Build Realtek HD-audio codec support
                   <*> Build HDMI/DisplayPort HD-audio codec support
       [*] USB support  --->
         <*>   xHCI HCD (USB 3.0) support
         <*>   EHCI HCD (USB 2.0) support
         <*>   USB Modem (CDC ACM) support
         <*>   USB Mass Storage support
       <*> MMC/SD/SDIO card support  --->
         <*>   Secure Digital Host Controller Interface support
         <*>     SDHCI support on PCI bus
         <*> Realtek PCI-E SD/MMC Card Interface Driver
       [*] X86 Platform Specific Device Drivers  --->
         <M>   ThinkPad ACPI Laptop Extras
         [*]     Console audio control ALSA interface
         [*]     Video output control support
         [*]     Support NVRAM polling for hot keys
       [*] IOMMU Hardware Support  --->
         [*]   Support for Intel IOMMU using DMA Remapping Devices
         [*]     Support for Shared Virtual Memory with Intel IOMMU
         [*]     Enable Intel DMA Remapping Devices by default
         [*]   Support for Interrupt Remapping

[Ready to use .config for Linux 5](https://gitlab.com/vitaly-zdanevich-configs/linux-kernel-thinkpad-t430/-/blob/master/.config).

### [Configuration]

#### [Compiler settings]

More info is available at:

-   [GCC optimization](https://wiki.gentoo.org/wiki/GCC_optimization "GCC optimization")
-   [MAKEOPTS](https://wiki.gentoo.org/wiki/MAKEOPTS "MAKEOPTS")
-   [EMERGE_DEFAULT_OPTS](https://wiki.gentoo.org/wiki/EMERGE_DEFAULT_OPTS "EMERGE DEFAULT OPTS")

[FILE] **`/etc/portage/make.conf`**

    # O2 for super-safe output
    CFLAGS="-march=ivybridge -O2 -pipe"
    CXXFLAGS="$"
    # Dual-core with enabled Hyper-Threading technology - 4 logical processors
    MAKEOPTS="-j4"
    # AMD64 architecture
    CHOST="x86_64-pc-linux-gnu"

#### [Packages settings]

For more info: [CPU_FLAGS_X86](https://wiki.gentoo.org/wiki/CPU_FLAGS_X86 "CPU FLAGS X86")

[FILE] **`/etc/portage/make.conf`**

    # Obtained via cpuid2cpuflags
    CPU_FLAGS_X86="aes avx f16c mmx mmxext pclmul popcnt rdrand sse sse2 sse3 sse4_1 sse4_2 ssse3"

#### [USE flags]

You can get or review my [/etc/portage configs](https://gitlab.com/vitaly-zdanevich-configs/gentoo--etc-portage--thinkpad-t430).

With [Intel Modesetting DDX](https://wiki.gentoo.org/wiki/Intel "Intel") as video driver and [libinput](https://wiki.gentoo.org/wiki/Libinput "Libinput") as input driver add the USE flags `glamor` and `libinput`.

[FILE] **`/etc/portage/make.conf`**

    # Intel GMA Gen 7 - IvyBridge
    VIDEO_CARDS="intel i965"

    INPUT_DEVICES="libinput"

    USE="glamor libinput"

##### [Firefox video performance]

Video performance is better on [[[media-video/mpv]](https://packages.gentoo.org/packages/media-video/mpv)[]] (use \--hwdec=vaapi), but from 2021 you can `USE="vaapi"` and enable WebRender in Firefox (if not enabled by default, see about:support) to use GPU for video and get higher FPS. Also in firefox in `about:support` enable `gfx.webrender.all` (tested on Firefox 86).

To check that it works: emerge [[[x11-apps/igt-gpu-tools]](https://packages.gentoo.org/packages/x11-apps/igt-gpu-tools)[]] and run `intel_gpu_top`: it must show loading **for Video** when Firefox plays YouTube, **not** like this 0%:

`root `[`#`]`intel_gpu_top`

    intel-gpu-top: Intel Ivybridge (Gen7) @ /dev/dri/card0
        437/ 441 MHz;  57% RC6;  0.70/12.20 W;       45 irqs/s

          IMC reads:        2 MiB/s
         IMC writes:      618 MiB/s

             ENGINES     BUSY                           MI_SEMA MI_WAIT
           Render/3D    8.99% |██                     |      0%      0%
             Blitter    0.00% |                       |      0%      0%
               Video    0.00% |                       |      0%      0%

Note that Intel HD 4000 (Ivybridge) supports only h264 hardware decoding, as you can see in vainfo:

`user `[`$`]`vainfo`

libva info: VA-API version 1.13.0

libva info: Trying to open /usr/lib64/va/drivers/iHD_drv_video.so libva info: va_openDriver() returns -1 libva info: Trying to open /usr/lib64/va/drivers/i965_drv_video.so libva info: Found init function \_\_vaDriverInit_1_13 libva info: va_openDriver() returns 0 vainfo: VA-API version: 1.13 (libva 2.13.0) vainfo: Driver version: Intel i965 driver for Intel(R) Ivybridge Mobile - 2.4.1 vainfo: Supported profile and entrypoints

         VAProfileMPEG2Simple            : VAEntrypointVLD
         VAProfileMPEG2Simple            :  VAEntrypointEncSlice
         VAProfileMPEG2Main              :  VAEntrypointVLD
         VAProfileMPEG2Main              :  VAEntrypointEncSlice
         VAProfileH264ConstrainedBaseline:  VAEntrypointVLD
         VAProfileH264ConstrainedBaseline:  VAEntrypointEncSlice
         VAProfileH264Main               :  VAEntrypointVLD
         VAProfileH264Main               :  VAEntrypointEncSlice
         VAProfileH264High               :  VAEntrypointVLD
         VAProfileH264High               :  VAEntrypointEncSlice
         VAProfileH264StereoHigh         :  VAEntrypointVLD
         VAProfileVC1Simple              :  VAEntrypointVLD
         VAProfileVC1Main                :  VAEntrypointVLD
         VAProfileVC1Advanced            :  VAEntrypointVLD
         VAProfileNone                   :  VAEntrypointVideoProc

VAProfileJPEGBaseline : VAEntrypointVLD

So you can install popular browser extension [h264ify](https://addons.mozilla.org/en-US/firefox/addon/h264ify/). On YouTube make right click on video and choose *Stats for nerds*, see *Codecs* line. Also check *media.ffmpeg.vaapi.enabled*.

You can check video performance on [this video](https://www.youtube.com/watch?v=0RvIbVmCOxg), maybe vp9 and av1 will play smoothly for you even without hardware decoding (**0% Video** in *intel_gpu_top*).

See more

[https://en.wikipedia.org/wiki/Video_Acceleration_API](https://en.wikipedia.org/wiki/Video_Acceleration_API)

[https://wiki.archlinux.org/title/Hardware_video_acceleration](https://wiki.archlinux.org/title/Hardware_video_acceleration)

[Gentoo Wiki about Intel](https://wiki.gentoo.org/wiki/Intel#HTML5.2FVAAPI_GPU_hangs "Intel").

### [Utils]

#### [battery charge thresholds]

Use: [[[app-laptop/tpacpi-bat]](https://packages.gentoo.org/packages/app-laptop/tpacpi-bat)[]]. Example config and instructions can be found at: [github.com/teleshoes/tpacpi-bat](https://github.com/teleshoes/tpacpi-bat/tree/master/examples).

#### [][fan control (noise level)]

Use: [[[app-laptop/thinkfan]](https://packages.gentoo.org/packages/app-laptop/thinkfan)[]].

[FILE] **`/etc/modprobe.d/thinkpad.conf`**

    options thinkpad_acpi fan_control=1

Example config:

[FILE] **`/etc/thinkfan.conf`**

    sensors:
      - hwmon: /sys/class/hwmon
        name: thinkpad
        indices: [1]
    fans:
      - tpacpi: /proc/acpi/ibm/fan
    levels:
      - [0, 0, 70]
      - [1, 70, 90]
      - ["level auto", 90, 255]
    # [level (0-7), from deg, to deg]

After config change:

`root `[`#`]`rc-service thinkfan restart`

#### [Fingerprint reader]

Use: [[[sys-auth/fprintd]](https://packages.gentoo.org/packages/sys-auth/fprintd)[]]. Instructons can be found at: [\[1\]](http://www.thinkwiki.org/wiki/How_to_enable_integrated_fingerprint_reader_with_fprint)

#### [ThinkLight]

Fn-Space to enable/disable the ThinkLight, useful to see the keyboard in low light conditions.

### [Displays]

#### [Multiple displays]

[![T430-three-displays-and-dock-4337.jpg](/images/thumb/5/5a/T430-three-displays-and-dock-4337.jpg/500px-T430-three-displays-and-dock-4337.jpg)](https://wiki.gentoo.org/wiki/File:T430-three-displays-and-dock-4337.jpg)

To add more displays^[\[7\]](#cite_note-7)^, there are several methods: one additional external display, or attach two external displays but internal panel will be disabled, or to do a triple monitor setup^[\[8\]](#cite_note-8)^ with a T430 (iGPU model) you\'ll need the 4337 or 4338 dock for its dual DisplayPort, external screens need to have the same setting (resolution & refresh rate) and interface type (DisplayPort, hence needing the dock). If the monitors lack a DisplayPort you can use an Active cable or adapter (passive cables & adapters won\'t work).

DisplayPort specification here is 1.1a, so **daisy chaining** (**MST**) is unavailable here^[\[9\]](#cite_note-9)[\[10\]](#cite_note-10)[\[11\]](#cite_note-11)^.

Also you can use [[[x11-misc/synergy]](https://packages.gentoo.org/packages/x11-misc/synergy)[]] ([Wayland support in development](https://github.com/symless/synergy-core/issues/4090)) or [[[x11-misc/barrier]](https://packages.gentoo.org/packages/x11-misc/barrier)[]] ([Wayland support in development](https://github.com/debauchee/barrier/issues/109)) to unite multiple computers.

#### [][Fastboot (reduce flickering on boot)]

Uncomment and add:

[FILE] **`/etc/default/grub`**

    GRUB_CMDLINE_LINUX="i915.fastboot=1"

and regenerate grub, as usual after kernel update:

`root `[`#`]`grub-mkconfig -o /boot/grub/grub.cfg`

[See more about fastboot](https://wiki.gentoo.org/wiki/Intel#Fastboot "Intel").

#### [eGPU]

With ThinkPad T430 it is possible to use **external GPU**, connected to **ExpressCard adapter**. The performance will be PCI-e x2: not very good, but on the internet you can find many positive posts about it. See more at:

[https://www.reddit.com/r/thinkpad/comments/hwmf91/t430_finally_maxed_out_egpu/](https://www.reddit.com/r/thinkpad/comments/hwmf91/t430_finally_maxed_out_egpu/)

[https://www.reddit.com/r/thinkpad/comments/hbzkdz/t430_egpu_how_about_coreboot_and_linux/](https://www.reddit.com/r/thinkpad/comments/hbzkdz/t430_egpu_how_about_coreboot_and_linux/)

[https://www.reddit.com/r/thinkpad/comments/727mhn/thinkpad_t430_and_expresscard34_egpu_what_ive/](https://www.reddit.com/r/thinkpad/comments/727mhn/thinkpad_t430_and_expresscard34_egpu_what_ive/)

[https://ounapuu.ee/posts/2022/01/09/why-i-went-back-to-using-a-thinkpad-from-2012/](https://ounapuu.ee/posts/2022/01/09/why-i-went-back-to-using-a-thinkpad-from-2012/)

[https://www.youtube.com/watch?v=390FuyadPIw?t=222](https://www.youtube.com/watch?v=390FuyadPIw)

[https://www.youtube.com/watch?v=2TR2qOdrdtE](https://www.youtube.com/watch?v=2TR2qOdrdtE) - GPU is Nvidia GTX 1060 3GB, overview of games performance on Windows.

#### [Fix screen tearing]

When watching some videos, [some frames may be out of sync with the screen rate](https://en.wikipedia.org/wiki/Screen_tearing "wikipedia:Screen tearing"). Screen tearing can be fixed in multiple ways. For Xorg: ThinkPad T430 has Intel GPU, create [this file](https://learnubuntumate.weebly.com/screen-tearing-on-intel-graphics.html):

[FILE] **`/etc/X11/xorg.conf.d/20-intel.conf`**

    Section "Device"
       Identifier  "Intel Graphics"
       Driver      "intel"
       Option      "TearFree"    "true"
    EndSection

And emerge [[[x11-drivers/xf86-video-intel]](https://packages.gentoo.org/packages/x11-drivers/xf86-video-intel)[]] (because still [not implemented in the default **xf86-video-modesetting**](https://gitlab.freedesktop.org/xorg/xserver/-/issues/244)).

Reboot the system for the new configuration to take effect.

Another option against screen tearing: use [Sway window manager](https://wiki.gentoo.org/wiki/Sway "Sway"), because underlying Wayland protocol has no screen tearing by design.

##### [][Pros of Wayland (Sway):]

1.  A little bit better scrolling in Firefox, better video playing (no drop frames, even if Youtube shows 0), more FPS
2.  No need for xf86-video-intel driver

##### [Cons of Wayland]

1.  Difficult screencasting for Google Meet in Firefox, you will need to mess around with unstable [PipeWire](https://wiki.gentoo.org/wiki/PipeWire "PipeWire"), [xdg-desktop-portal-wlr](https://github.com/emersion/xdg-desktop-portal-wlr), personally I got no success in January 2022 after a few hours of trying, [see this defect](https://bugzilla.mozilla.org/show_bug.cgi?id=1672944)
2.  Xorg will be installed if you compile [Firefox](https://gitweb.gentoo.org/repo/gentoo.git/tree/www-client/firefox) with [PGO](https://en.wikipedia.org/wiki/Profile-guided_optimization "wikipedia:Profile-guided optimization"), looks like Firefox uses Xorg virtual screen for testing
3.  Impossible to use ffmpeg for screen grabbing, but other options exists
4.  The most minor - you will need to change your screenshot software from scrot (or maim) to grim

You can check tearing on [this video](https://www.youtube.com/watch?v=0RvIbVmCOxg).

#### [i3 bindsym for screenshot to file with a good name and to clipboard]

File name will be like [2022-jan-15\--12-05-59_maim.png]:

[CODE]

    bindsym $mod+Shift+s exec maim --select --hidecursor |\
        tee /tmp/$(date +%Y-%b-%d--%H-%M-%S_maim | tr A-Z a-z).png |\
        xclip -selection clipboard -t image/png

Full screen, waiting 5 seconds before, with led and \"notification\":

[CODE]

    bindsym $mod+Shift+x exec "\
        echo 1 > /sys/class/leds/platform\:\:micmute/brightness; \
        sleep 5; \
        maim --hidecursor ~/screenshots/$(date +%Y-%b-%d--%H-%M-%S_maim | tr A-Z a-z).png; \
        echo 0 > /sys/class/leds/platform\:\:micmute/brightness; \
        i3-nagbar --message 'Screenshot created' --type warning & \
        sleep 3; pkill i3-nagbar"

To be able to toggle the led as a regular user - chmod to 666 will works only before the reboot, persistent solution: create file **/etc/tmpfiles.d/\<your name\>** with content:

[FILE] **`/etc/tmpfiles.d/brightness.conf`**

    m /sys/class/leds/platform::micmute/brightness 0664 root video - -

**video** is the group of your user.

See more about tmpfiles at **man 5 tmpfiles.d**

#### [Alter brightness]

Brightness value live in a file [/sys/class/backlight/intel_backlight/brightness], to react current valueː

`user `[`$`]`cat /sys/class/backlight/intel_backlight/brightness`

220

To alter brightnessː

`root `[`#`]`echo 400 > /sys/class/backlight/intel_backlight/brightness`

Alternatively, install [[[sys-power/acpilight]](https://packages.gentoo.org/packages/sys-power/acpilight)[]] or [[[dev-libs/light]](https://packages.gentoo.org/packages/dev-libs/light)[]] to control brightness with the [xbacklight] or [light] tools respectively.

## [Keyboard layouts]

This is usual, for example here we add Russian language, change by Caps:

[FILE] **`/etc/X11/xorg.conf.d/10-keyboard.conf`**

    Section "InputClass"
        Identifier "keyboard-all"
        Driver "evdev"
        Option "XkbLayout" "us,ru"
        Option "XkbOptions" "grp:caps_toggle"
        MatchIsKeyboard "on"
    EndSection

For led indicator [https://gitlab.com/vitaly-zdanevich/keyboard-layout-change-monitor](https://gitlab.com/vitaly-zdanevich/keyboard-layout-change-monitor)

## [][Screen recording with ffmpeg and vaapi (hardware acceleration, without Nvidia GPU chip)]

To h264, because GitHub supports this format (mp4), not webm (vp9), and **Ivy Bridge** supports hardware encoding to h264 (no audio):

`user `[`$`]`ffmpeg -vaapi_device /dev/dri/renderD128 -f x11grab -video_size 1366x768 -i :0+1200,1152 -vf 'format=nv12,hwupload' -c:v h264_vaapi o.mp4`

ffmpeg records middle display, where width of the left is 1200 and height is 1920 (1920 - 768 = 1152):

[![](/images/d/da/Arandr-3-displays.png)](https://wiki.gentoo.org/wiki/File:Arandr-3-displays.png)

Recording of main screen, with audio (merging system sound + mic) into mono:

[FILE] **`main-screen-with-audio.sh`**

    ffmpeg -vaapi_device /dev/dri/renderD128 -f x11grab -video_size 1366x768 -i :0.0 \
        -f pulse -i alsa_output.usb-GN_Netcom_A_S_Jabra_EVOLVE_LINK_00113735E82E0A-00.analog-stereo.monitor \
        -f pulse -i alsa_input.usb-GN_Netcom_A_S_Jabra_EVOLVE_LINK_00113735E82E0A-00.mono-fallback \
        -filter_complex "amerge" -ac 1 \
        -c:v h264_vaapi -vf 'format=nv12,hwupload' ~/record/out/$(date +%Y-%b-%d%a--%H-%M-%S | tr A-Z a-z).mp4

    # Press q to finish the recording.
    # https://trac.ffmpeg.org/wiki/Encode/H.264

Another example for meetings recording: system sound + USB mic into mono (using the **right external display**, so you need to adapt this script for you):

[FILE] **`right-with-audio.sh`**

    ffmpeg -vaapi_device /dev/dri/renderD128 -f x11grab -video_size 1920x1200 -i :0.0+2566,720 \
        -f pulse -i alsa_output.pci-0000_00_1b.0.analog-stereo.monitor \
        -f pulse -i alsa_input.usb-Focusrite_Scarlett_Solo_USB_Y7D1J3F0A66336-00.analog-stereo \
        -filter_complex "amerge" -ac 1 \
        -c:v h264_vaapi -vf 'format=nv12,hwupload' ~/record/$(date +%Y-%b-%d%a--%H-%M-%S | tr A-Z a-z).mp4

    # Press q to finish the recording.
    # https://trac.ffmpeg.org/wiki/Encode/H.264

Resulting file name will be like **2023-apr-28fri\--13-34-54.mp4/home/vitaly/record/out/2023-jul-27thu\--13-22-25.mp4**

List your audio devices with

`user `[`$`]`pacmd list-sources | grep -e 'name:' -e 'index:'`

Related link: [https://trac.ffmpeg.org/wiki/Encode/H.264](https://trac.ffmpeg.org/wiki/Encode/H.264)

## [Suspend without fan rotation]

[FILE] **`/lib64/elogind/system-sleep/fan`**

    #!/bin/bash

    case $1/$2 in
        pre/*)
            echo level 0 > /proc/acpi/ibm/fan

            pkill --signal SIGINT openconnect &
            sleep 5
            # Graceful shutdown of Openconnect: without this after suspend will be no internet connection
            # and I will need to stop it manually.
            # Related link: https://unix.stackexchange.com/a/725171/34318

            ;;
        post/*)
            # No need to restart the thinkfan - after a few seconds it will restore the speed according to the config
            ;;
    esac

File name can be anything. Make it executable:

`root `[`#`]`chmod +x fan`

See more at [Elogind](https://wiki.gentoo.org/wiki/Elogind#Suspend.2FHibernate_Resume.2FThaw_hook_scripts "Elogind").

## [See also]

-   [Lenovo Thinkpad T420](https://wiki.gentoo.org/wiki/Lenovo_Thinkpad_T420 "Lenovo Thinkpad T420")
-   [Lenovo ThinkPad T440s](https://wiki.gentoo.org/wiki/Lenovo_ThinkPad_T440s "Lenovo ThinkPad T440s")

## [References]

1.  [[[↑](#cite_ref-1)] [[https://github.com/n4ru/1vyrain/issues/33#issuecomment-596155537](https://github.com/n4ru/1vyrain/issues/33#issuecomment-596155537)]]
2.  [[[↑](#cite_ref-2)] [[https://www.reddit.com/r/thinkpad/comments/rojn2y/what_ssd_can_you_recommend_for_t430/hpys86n/?context=3](https://www.reddit.com/r/thinkpad/comments/rojn2y/what_ssd_can_you_recommend_for_t430/hpys86n/?context=3)]]
3.  [[[↑](#cite_ref-3)] [[https://www.reddit.com/r/thinkpad/comments/8u860n/t430_hdd_ultrabay_caddy/](https://www.reddit.com/r/thinkpad/comments/8u860n/t430_hdd_ultrabay_caddy/)]]
4.  [[[↑](#cite_ref-4)] [[https://www.reddit.com/r/thinkpad/comments/9fk3bf/t430_ultrabay_sata_2_or_sata_3/](https://www.reddit.com/r/thinkpad/comments/9fk3bf/t430_ultrabay_sata_2_or_sata_3/)]]
5.  [[[↑](#cite_ref-5)] [[https://ostechnix.com/how-to-check-laptop-battery-status-in-terminal-in-linux/](https://ostechnix.com/how-to-check-laptop-battery-status-in-terminal-in-linux/)]]
6.  [[[↑](#cite_ref-6)] [[https://www.reddit.com/r/Gentoo/comments/repy1s/thinkpad_t430_what_is_the_best_wlan_module/](https://www.reddit.com/r/Gentoo/comments/repy1s/thinkpad_t430_what_is_the_best_wlan_module/)]]
7.  [[[↑](#cite_ref-7)] [[https://forums.lenovo.com/t5/T400-T500-and-newer-T-series/T430-Multiple-Monitors-gt-2-with-HD4000/td-p/919831](https://forums.lenovo.com/t5/T400-T500-and-newer-T-series/T430-Multiple-Monitors-gt-2-with-HD4000/td-p/919831)]]
8.  [[[↑](#cite_ref-8)] [[https://www.reddit.com/r/thinkpad/comments/p3q2t3/t430_looks_like_broke_the_mainboard_with_wrong/h8twa36?utm_source=share&utm_medium=web2x&context=3](https://www.reddit.com/r/thinkpad/comments/p3q2t3/t430_looks_like_broke_the_mainboard_with_wrong/h8twa36?utm_source=share&utm_medium=web2x&context=3)]]
9.  [[[↑](#cite_ref-9)] [[https://forums.freebsd.org/threads/displayport-daisy-chaining.75490/](https://forums.freebsd.org/threads/displayport-daisy-chaining.75490/)]]
10. [[[↑](#cite_ref-10)] [[https://community.intel.com/t5/Graphics/Is-the-Intel-HD-Graphics-4000-graphics-card-a-DisplayPort-1-2/td-p/646090?profile.language=en](https://community.intel.com/t5/Graphics/Is-the-Intel-HD-Graphics-4000-graphics-card-a-DisplayPort-1-2/td-p/646090?profile.language=en)]]
11. [[[↑](#cite_ref-11)] [[https://en.wikipedia.org/wiki/DisplayPort#Multi-Stream_Transport\_(MST)](https://en.wikipedia.org/wiki/DisplayPort#Multi-Stream_Transport_(MST))]]