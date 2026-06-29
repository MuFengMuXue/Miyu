**Resources**

[[]][Home](https://www.nongnu.org/dmidecode/)

[[]][Package information](https://packages.gentoo.org/packages/sys-apps/dmidecode)

[dmidecode] is a software tool that enables extraction of detailed hardware information from a system by decoding the DMI (Desktop Management Interface) table. It provides valuable insights into the system\'s hardware configuration as described in SMBIOS (System Management BIOS). With dmidecode, you can retrieve information such as the system\'s [BIOS](https://wiki.gentoo.org/wiki/BIOS "BIOS") vendor, version, release date, and revision, as well as details about the system\'s manufacturer, product name, serial number, UUID, SKU number, family, baseboard information, chassis details, processor family, manufacturer, version, and frequency.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
-   [[2] [Description]](#Description)
-   [[3] [Command Usage]](#Command_Usage)
    -   [[3.1] [BIOS Information]](#BIOS_Information)
        -   [[3.1.1] [BIOS Vendor]](#BIOS_Vendor)
        -   [[3.1.2] [BIOS Version]](#BIOS_Version)
        -   [[3.1.3] [BIOS Release Date]](#BIOS_Release_Date)
        -   [[3.1.4] [BIOS Revision]](#BIOS_Revision)
        -   [[3.1.5] [Firmware Revision]](#Firmware_Revision)
    -   [[3.2] [System Information]](#System_Information)
        -   [[3.2.1] [System Manufacturer]](#System_Manufacturer)
        -   [[3.2.2] [System Product Name]](#System_Product_Name)
        -   [[3.2.3] [System Version]](#System_Version)
        -   [[3.2.4] [System Serial Number]](#System_Serial_Number)
        -   [[3.2.5] [System UUID]](#System_UUID)
        -   [[3.2.6] [System SKU Number]](#System_SKU_Number)
        -   [[3.2.7] [System Family]](#System_Family)
    -   [[3.3] [Baseboard Information]](#Baseboard_Information)
        -   [[3.3.1] [Baseboard Manufacturer]](#Baseboard_Manufacturer)
        -   [[3.3.2] [Baseboard Product Name]](#Baseboard_Product_Name)
        -   [[3.3.3] [Baseboard Version]](#Baseboard_Version)
        -   [[3.3.4] [Baseboard Serial Number]](#Baseboard_Serial_Number)
        -   [[3.3.5] [Baseboard Asset Tag]](#Baseboard_Asset_Tag)
    -   [[3.4] [Chassis Information]](#Chassis_Information)
        -   [[3.4.1] [Chassis Manufacturer]](#Chassis_Manufacturer)
        -   [[3.4.2] [Chassis Type]](#Chassis_Type)
        -   [[3.4.3] [Chassis Version]](#Chassis_Version)
        -   [[3.4.4] [Chassis Serial Number]](#Chassis_Serial_Number)
        -   [[3.4.5] [Chassis Asset Tag]](#Chassis_Asset_Tag)
    -   [[3.5] [Processor Information]](#Processor_Information)
        -   [[3.5.1] [Processor Family]](#Processor_Family)
        -   [[3.5.2] [Processor Manufacturer]](#Processor_Manufacturer)
        -   [[3.5.3] [Processor Version]](#Processor_Version)
        -   [[3.5.4] [Processor Frequency]](#Processor_Frequency)
-   [[4] [Ownership]](#Ownership)
-   [[5] [Vpddecode]](#Vpddecode)
-   [[6] [Tips and Tricks]](#Tips_and_Tricks)
    -   [[6.1] [Systemd]](#Systemd)
    -   [[6.2] [Reading DMI Data Without dmidecode and as Non-Root]](#Reading_DMI_Data_Without_dmidecode_and_as_Non-Root)
-   [[7] [See also]](#See_also)

## [Installation]

### [USE flags]

To install dmidecode, you can configure the following USE flag:

### [USE flags for] [sys-apps/dmidecode](https://packages.gentoo.org/packages/sys-apps/dmidecode) [[]] [DMI (Desktop Management Interface) table related utilities]

  ----------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------
  [`selinux`](https://packages.gentoo.org/useflags/selinux)         !!internal use only!! Security Enhanced Linux support, this must be set by the selinux profile or breakage will occur
  [`verify-sig`](https://packages.gentoo.org/useflags/verify-sig)   Verify upstream signatures on distfiles
  ----------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-02-04 04:30] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

To install dmidecode using the Portage package manager, run the following command:

`root `[`#`]`emerge --ask sys-apps/dmidecode`

\

## [Description]

Here is a description of the various keywords and their corresponding information:

  ------------------------- --------------------------------------------------------------------------------------------------------------------------------------------
  Keyword                   Description
  bios-vendor               The vendor responsible for manufacturing the system\'s BIOS firmware.
  bios-version              The specific release or version number assigned to the system\'s BIOS firmware.
  bios-release-date         The date when the system\'s BIOS firmware was initially released or made available.
  bios-revision             The specific version or revision number assigned to the system\'s BIOS firmware.
  firmware-revision         The specific version or revision number assigned to the system\'s firmware, including the BIOS.
  system-manufacturer       The manufacturer responsible for manufacturing the system.
  system-product-name       The specific model or name assigned to the system by the manufacturer.
  system-version            The specific release or version number assigned to the system.
  system-serial-number      The unique serial number assigned to the system by the manufacturer.
  system-uuid               The Universally Unique Identifier (UUID) assigned to the system, providing a globally unique identifier across platforms and environments.
  system-sku-number         The Stock Keeping Unit (SKU) number assigned to the system, used for inventory or product tracking.
  system-family             The family or category of the system, indicating similarities or belonging to the same product line.
  baseboard-manufacturer    The manufacturer responsible for manufacturing the motherboard or baseboard.
  baseboard-product-name    The specific model or name assigned to the motherboard or baseboard by the manufacturer.
  baseboard-version         The specific release or version number assigned to the motherboard or baseboard.
  baseboard-serial-number   The unique serial number assigned to the motherboard or baseboard by the manufacturer.
  baseboard-asset-tag       The asset tag assigned to the motherboard or baseboard for tracking or identification purposes.
  chassis-manufacturer      The manufacturer responsible for manufacturing the chassis or case of the system.
  chassis-type              The type or form factor of the chassis, such as tower, rack-mount, or desktop.
  chassis-version           The specific release or version number assigned to the chassis.
  chassis-serial-number     The unique serial number assigned to the chassis by the manufacturer.
  chassis-asset-tag         The asset tag assigned to the chassis for tracking or identification purposes.
  processor-family          The family or category of the processor, indicating similarities or belonging to the same processor family.
  processor-manufacturer    The manufacturer responsible for manufacturing the processor.
  processor-version         The specific release or version number assigned to the processor.
  processor-frequency       The operating frequency or speed of the processor, typically measured in gigahertz (GHz).
  ------------------------- --------------------------------------------------------------------------------------------------------------------------------------------

## [Command Usage]

Here is the detailed hardware information that can be retrieved using [dmidecode]:

### [BIOS Information]

#### [BIOS Vendor]

To obtain the vendor information of the system\'s BIOS firmware, use the following command:

`root `[`#`]`dmidecode -s bios-vendor`

#### [BIOS Version]

To retrieve the version number of the system\'s BIOS firmware, use the following command:

`root `[`#`]`dmidecode -s bios-version`

#### [BIOS Release Date]

To obtain the release date of the system\'s BIOS firmware, use the following command:

`root `[`#`]`dmidecode -s bios-release-date`

#### [BIOS Revision]

To retrieve the revision number of the system\'s BIOS firmware, use the following command:

`root `[`#`]`dmidecode -s bios-revision`

#### [Firmware Revision]

To obtain the revision number of the system\'s firmware, including the BIOS, use the following command:

`root `[`#`]`dmidecode -s firmware-revision`

### [System Information]

#### [System Manufacturer]

To retrieve the manufacturer information of the system, use the following command:

`root `[`#`]`dmidecode -s system-manufacturer`

#### [System Product Name]

To obtain the product name assigned to the system by the manufacturer, use the following command:

`root `[`#`]`dmidecode -s system-product-name`

#### [System Version]

To retrieve the version number assigned to the system, use the following command:

`root `[`#`]`dmidecode -s system-version`

#### [System Serial Number]

To obtain the unique serial number assigned to the system by the manufacturer, use the following command:

`root `[`#`]`dmidecode -s system-serial-number`

#### [System UUID]

To retrieve the Universally Unique Identifier (UUID) assigned to the system, use the following command:

`root `[`#`]`dmidecode -s system-uuid`

#### [System SKU Number]

To obtain the Stock Keeping Unit (SKU) number assigned to the system, use the following command:

`root `[`#`]`dmidecode -s system-sku-number`

#### [System Family]

To retrieve the family or category information of the system, use the following command:

`root `[`#`]`dmidecode -s system-family`

### [Baseboard Information]

#### [Baseboard Manufacturer]

To obtain the manufacturer information of the motherboard or baseboard, use the following command:

`root `[`#`]`dmidecode -s baseboard-manufacturer`

#### [Baseboard Product Name]

To retrieve the product name assigned to the motherboard or baseboard, use the following command:

`root `[`#`]`dmidecode -s baseboard-product-name`

#### [Baseboard Version]

To obtain the version number assigned to the motherboard or baseboard, use the following command:

`root `[`#`]`dmidecode -s baseboard-version`

#### [Baseboard Serial Number]

To retrieve the unique serial number assigned to the motherboard or baseboard, use the following command:

`root `[`#`]`dmidecode -s baseboard-serial-number`

#### [Baseboard Asset Tag]

To obtain the asset tag assigned to the motherboard or baseboard, use the following command:

`root `[`#`]`dmidecode -s baseboard-asset-tag`

### [Chassis Information]

#### [Chassis Manufacturer]

To retrieve the manufacturer information of the chassis or case of the system, use the following command:

`root `[`#`]`dmidecode -s chassis-manufacturer`

#### [Chassis Type]

To obtain the type or form factor of the chassis, use the following command:

`root `[`#`]`dmidecode -s chassis-type`

#### [Chassis Version]

To retrieve the version number assigned to the chassis, use the following command:

`root `[`#`]`dmidecode -s chassis-version`

#### [Chassis Serial Number]

To obtain the unique serial number assigned to the chassis, use the following command:

`root `[`#`]`dmidecode -s chassis-serial-number`

#### [Chassis Asset Tag]

To retrieve the asset tag assigned to the chassis, use the following command:

`root `[`#`]`dmidecode -s chassis-asset-tag`

### [Processor Information]

#### [Processor Family]

To obtain the family or category information of the processor, use the following command:

`root `[`#`]`dmidecode -s processor-family`

#### [Processor Manufacturer]

To retrieve the manufacturer information of the processor, use the following command:

`root `[`#`]`dmidecode -s processor-manufacturer`

#### [Processor Version]

To obtain the version number assigned to the processor, use the following command:

`root `[`#`]`dmidecode -s processor-version`

#### [Processor Frequency]

To retrieve the operating frequency or speed of the processor, use the following command:

`root `[`#`]`dmidecode -s processor-frequency`

## [Ownership]

The **ownership** command allows you to manipulate ownership options for memory reading. You can specify different options to customize the behavior of the command.

To read memory from a specific device file ([/dev/custom_mem]), you can use the following command:

`root `[`#`]`ownership -d /dev/custom_mem`

## [Vpddecode]

The **vpddecode** command is used for decoding VPD (Vital Product Data) records. You can provide various options to customize the behavior of the command.

To read memory from a specific device file (e.g., [/dev/custom_mem]), you can use the following command:

`root `[`#`]`vpddecode -d /dev/custom_mem`

To only display the value of a specific VPD string (e.g., \"motherboard-serial-number\"), use the following command:

`root `[`#`]`vpddecode -s motherboard-serial-number`

To prevent the decoding of VPD records and dump the raw data, use the following command:

`root `[`#`]`vpddecode -u`

## [Tips and Tricks]

### [Systemd]

If dmidecode is not available or inaccessible, there are alternative methods to retrieve BIOS information. In addition to the previously mentioned tips, you can also utilize systemd commands to access relevant data. Some of the systemd commands for retrieving BIOS info include:

\- To access kernel output related to the BIOS, you can use the following command:

`root `[`#`]`journalctl --quiet --system --boot SYSLOG_IDENTIFIER=kernel`

\- Another command that can provide BIOS-related information is:

`root `[`#`]`systemctl show --property=EFI_VARS`

Please note that the availability and output of these commands may vary depending on the system configuration.

### [Reading DMI Data Without dmidecode and as Non-Root]

If you are unable to launch dmidecode as usual or do not have root privileges, there are alternative methods to read DMI (Desktop Management Interface) information. Please note that some information, such as serial numbers, may require root privileges to access.

One option is to access the DMI information under the directory [/sys/class/dmi/id/] as a regular user. This directory contains various files that provide DMI-related information. However, please be aware that the following options require root access:

-   Chassis serial number: [/sys/class/dmi/id/chassis_serial]
-   Product serial number: [/sys/class/dmi/id/product_serial]
-   Product UUID: [/sys/class/dmi/id/product_uuid]

\
For example, you can retrieve the platform type (system product name) by reading the file:

`user `[`$`]`cat /sys/class/dmi/id/product_name`

Similarly, you can obtain the BIOS version by reading:

`user `[`$`]`cat /sys/class/dmi/id/bios_version`

To retrieve the amount of physical memory, you can make use of the following command:

`user `[`$`]`cat /sys/class/dmi/id/memory/size`

## [See also]

-   [Lshw](https://wiki.gentoo.org/wiki/Lshw "Lshw") --- a small tool that provides detailed information on the hardware configuration of the machine. It can report exact memory configuration, firmware version, mainboard configuration, CPU version and speed, cache configuration, bus speed, etc. on DMI-capable x86 or EFI (IA-64) systems and on some PowerPC machines (PowerMac G4 is known to work).
-   [Lspci](https://wiki.gentoo.org/wiki/Lspci "Lspci") --- contains various utilities dealing with the [PCI bus](https://en.wikipedia.org/wiki/Peripheral_Component_Interconnect "wikipedia:Peripheral Component Interconnect") (primarily [lspci]).
-   [Lsusb](https://wiki.gentoo.org/wiki/Lsusb "Lsusb") --- a collection various utilities for querying the the Universal Serial Bus (USB).
-   [BIOS_Update#Gather_firmware_information](https://wiki.gentoo.org/wiki/BIOS_Update#Gather_firmware_information "BIOS Update")