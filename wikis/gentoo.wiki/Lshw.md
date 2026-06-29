**Resources**

[[]][Home](http://www.ezix.org/project/wiki/HardwareLiSter)

[[]][GitWeb](https://ezix.org/src/pkg/lshw)

[[]][Official documentation](https://ezix.org/src/pkg/lshw/wiki)

[lshw] (Hardware Lister) is a small tool that provides detailed information on the hardware configuration of the machine. It can report exact memory configuration, firmware version, mainboard configuration, CPU version and speed, cache configuration, bus speed, etc. on DMI-capable x86 or EFI (IA-64) systems and on some PowerPC machines (PowerMac G4 is known to work).

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
-   [[2] [Usage]](#Usage)
    -   [[2.1] [Invocation]](#Invocation)
    -   [[2.2] [Launch the X11 GUI]](#Launch_the_X11_GUI)
    -   [[2.3] [Generate full information report about all detected hardware]](#Generate_full_information_report_about_all_detected_hardware)
    -   [[2.4] [Display brief hardware information]](#Display_brief_hardware_information)
    -   [[2.5] [Display bus information]](#Display_bus_information)
-   [[3] [Enable/disable specific features]](#Enable.2Fdisable_specific_features)
    -   [[3.1] [Disable USB]](#Disable_USB)
    -   [[3.2] [Enable DMI]](#Enable_DMI)
    -   [[3.3] [Use numeric IDs for devices]](#Use_numeric_IDs_for_devices)
    -   [[3.4] [Display less verbose output]](#Display_less_verbose_output)
    -   [[3.5] [Remove sensitive information from the output]](#Remove_sensitive_information_from_the_output)
-   [[4] [Generate reports]](#Generate_reports)
    -   [[4.1] [Generate report in HTML format]](#Generate_report_in_HTML_format)
    -   [[4.2] [Generate report in XML format]](#Generate_report_in_XML_format)
    -   [[4.3] [Generate report in SQLite format]](#Generate_report_in_SQLite_format)
-   [[5] [Display specific hardware classes]](#Display_specific_hardware_classes)
    -   [[5.1] [Processor]](#Processor)
    -   [[5.2] [Memory]](#Memory)
    -   [[5.3] [Disk]](#Disk)
    -   [[5.4] [Storage controllers]](#Storage_controllers)
    -   [[5.5] [Network adapters]](#Network_adapters)
    -   [[5.6] [Display]](#Display)
    -   [[5.7] [Multimedia]](#Multimedia)
    -   [[5.8] [Printer]](#Printer)
    -   [[5.9] [System]](#System)
    -   [[5.10] [Bus]](#Bus)
    -   [[5.11] [Bridge]](#Bridge)
    -   [[5.12] [Communication]](#Communication)
    -   [[5.13] [Generic]](#Generic)
    -   [[5.14] [Power]](#Power)
    -   [[5.15] [Volume]](#Volume)
-   [[6] [See also]](#See_also)

## [Installation]

### [USE flags]

### [USE flags for] [sys-apps/lshw](https://packages.gentoo.org/packages/sys-apps/lshw) [[]] [Hardware Lister]

  --------------------------------------------------------- -----------------------------------------------------------------------------------------------------
  [`gtk`](https://packages.gentoo.org/useflags/gtk)         Add support for x11-libs/gtk+ (The GIMP Toolkit)
  [`sqlite`](https://packages.gentoo.org/useflags/sqlite)   Add support for sqlite - embedded sql database
  [`static`](https://packages.gentoo.org/useflags/static)   !!do not set this during bootstrap!! Causes binaries to be statically linked instead of dynamically
  --------------------------------------------------------- -----------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2025-12-19 09:51] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

`root `[`#`]`emerge --ask sys-apps/lshw`

## [Usage]

### [Invocation]

`root `[`#`]`lshw --help`

    Hardware Lister (lshw) - B.02.17
    usage: lshw [-format] [-options ...]
           lshw -version

            -version        print program version (B.02.17)

    format can be
            -html           output hardware tree as HTML
            -xml            output hardware tree as XML
            -short          output hardware paths
            -businfo        output bus information

    options can be
            -class CLASS    only show a certain class of hardware
            -C CLASS        same as '-class CLASS'
            -c CLASS        same as '-class CLASS'
            -disable TEST   disable a test (like pci, isapnp, cpuid, etc. )
            -enable TEST    enable a test (like pci, isapnp, cpuid, etc. )
            -quiet          don't display status
            -sanitize       sanitize output (remove sensitive information like serial numbers, etc.)
            -numeric        output numeric IDs (for PCI, USB, etc.)

### [Launch the X11 GUI]

Enables interaction with lshw\'s graphical user interface, presenting a comprehensive and interactive view of hardware components.

`root `[`#`]`lshw -X`

** Note**\
This specific X11 GUI feature requires the appropriate useflag [gtk] to be enabled.

### [Generate full information report about all detected hardware]

Produces a comprehensive report detailing every aspect of the detected hardware components within the system.

`user `[`$`]`lshw`

### [Display brief hardware information]

Gives a succinct summary of the hardware configuration, providing a general overview rather than exhaustive details.

`user `[`$`]`lshw -short`

### [Display bus information]

Details bus information for all detected hardware components, helpful for understanding the communication routes between hardware elements.

`user `[`$`]`lshw -businfo`

## [][Enable/disable specific features]

### [Disable USB]

Prevents the listing of USB devices in the report, useful when USB device details are not necessary for the investigation.

`user `[`$`]`lshw -disable usb`

### [Enable DMI]

Turns on the reporting of DMI/SMBIOS information, which provides additional hardware component details stored in the system BIOS.

`user `[`$`]`lshw -enable dmi`

### [Use numeric IDs for devices]

Outputs numeric IDs instead of descriptive names for devices, aiding in identifying specific hardware elements based on their standard device IDs.

`user `[`$`]`lshw -numeric`

### [Display less verbose output]

Limits the verbosity of the output, leading to a more compact and less detailed report.

`user `[`$`]`lshw -quiet`

### [Remove sensitive information from the output]

Ensures the output excludes any sensitive information such as serial numbers, promoting a safer sharing of the report.

`user `[`$`]`lshw -sanitize`

## [Generate reports]

### [Generate report in HTML format]

Creates an HTML report for easy viewing and navigation within a web browser.

`user `[`$`]`lshw -html > hardware.html`

### [Generate report in XML format]

Forms an XML report, ideal for parsing and processing by other software or for storage purposes.

`user `[`$`]`lshw -xml > hardware.xml`

### [Generate report in SQLite format]

Generates an SQLite database report, allowing efficient querying and extraction of hardware information in structured form.

`user `[`$`]`lshw -dump > hardware.db`

** Note**\
This specific SQLite feature requires the [sqlite] useflag to be enabled.

## [Display specific hardware classes]

### [Processor]

Provides details of the CPU including its type, speed, cores, and cache information.

`user `[`$`]`lshw -class processor`

### [Memory]

Displays comprehensive details about the system memory such as RAM, ROM, and any associated caches.

`user `[`$`]`lshw -class memory`

### [Disk]

Reports on disk drives, including their type, size, and partitioning information.

`user `[`$`]`lshw -class disk`

### [Storage controllers]

Presents information on storage controllers, like SATA or NVMe controllers, critical in understanding the storage infrastructure.

`user `[`$`]`lshw -class storage`

### [Network adapters]

Details on network interfaces including ethernet and WiFi, providing insights into networking capabilities.

`user `[`$`]`lshw -class network`

### [Display]

Describes graphics cards and monitors, essential for understanding the system\'s display capabilities.

`user `[`$`]`lshw -class display`

### [Multimedia]

Details multimedia devices like sound cards, providing information on audio-visual capabilities.

`user `[`$`]`lshw -class multimedia`

### [Printer]

Provides information about any attached printers, useful in troubleshooting and setting up printing capabilities.

`user `[`$`]`lshw -class printer`

### [System]

Offers extensive details about the system/motherboard, providing a broad understanding of the system\'s foundation.

`user `[`$`]`lshw -class system`

### [Bus]

Reports on busses, like USB or PCI, integral to understanding how components communicate within the system.

`user `[`$`]`lshw -class bus`

### [Bridge]

Describes bridge devices, crucial for understanding connections between different parts of the computer system.

`user `[`$`]`lshw -class bridge`

### [Communication]

Presents data on communication devices, useful in examining and troubleshooting communication capabilities.

`user `[`$`]`lshw -class communication`

### [Generic]

Furnishes information about generic/unclassified devices that may not fit into other specific hardware classes.

`user `[`$`]`lshw -class generic`

### [Power]

Reveals details about power-related hardware, like UPS, important in understanding the power management infrastructure.

`user `[`$`]`lshw -class power`

### [Volume]

Provides information about volumes/partitions, assisting in disk and storage management tasks.

`user `[`$`]`lshw -class volume`

## [See also]

-   [Pciutils](https://wiki.gentoo.org/wiki/Pciutils "Pciutils") --- contains various utilities dealing with the [PCI bus](https://en.wikipedia.org/wiki/Peripheral_Component_Interconnect "wikipedia:Peripheral Component Interconnect") (primarily [lspci]).
-   [Usbutils](https://wiki.gentoo.org/wiki/Usbutils "Usbutils") --- a collection various utilities for querying the the Universal Serial Bus (USB).