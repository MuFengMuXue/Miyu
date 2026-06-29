[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=Pciutils&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

**Resources**

[[]][Home](http://mj.ucw.cz/sw/pciutils/)

[[]][Package information](https://packages.gentoo.org/packages/sys-apps/pciutils)

[[]][Wikipedia](https://en.wikipedia.org/wiki/Lspci "wikipedia:Lspci")

[[]][GitWeb](https://git.kernel.org/?p=utils/pciutils/pciutils.git)

**pciutils** contains various utilities dealing with the [PCI bus](https://en.wikipedia.org/wiki/Peripheral_Component_Interconnect "wikipedia:Peripheral Component Interconnect") (primarily [lspci]). [lspci] is a [hardware detection](https://wiki.gentoo.org/wiki/Hardware_detection "Hardware detection") tool for system resources connected to the PCI bus.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
-   [[2] [Configuration]](#Configuration)
    -   [[2.1] [Files]](#Files)
-   [[3] [Usage]](#Usage)
    -   [[3.1] [Invocation]](#Invocation)
-   [[4] [Removal]](#Removal)
    -   [[4.1] [Unmerge]](#Unmerge)
-   [[5] [See also]](#See_also)

## [Installation]

### [USE flags]

### [USE flags for] [sys-apps/pciutils](https://packages.gentoo.org/packages/sys-apps/pciutils) [[]] [Various utilities dealing with the PCI bus]

  ------------------------------------------------------------------- -------------------------------------------------------------------------------------------
  [`+kmod`](https://packages.gentoo.org/useflags/+kmod)               Enable sys-apps/kmod support for the -k switch in lspci command
  [`+udev`](https://packages.gentoo.org/useflags/+udev)               Enable virtual/udev integration (device discovery, power and storage device support, etc)
  [`dns`](https://packages.gentoo.org/useflags/dns)                   Enable support for querying the central database of PCI IDs using DNS
  [`static-libs`](https://packages.gentoo.org/useflags/static-libs)   Build static versions of dynamic libraries as well
  [`verify-sig`](https://packages.gentoo.org/useflags/verify-sig)     Verify upstream signatures on distfiles
  [`zlib`](https://packages.gentoo.org/useflags/zlib)                 Support compressed pci.ids database
  ------------------------------------------------------------------- -------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-05-10 07:03] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

`root `[`#`]`emerge --ask sys-apps/pciutils`

[lspci] detects the devices based on an ID database provided by [[[sys-apps/hwdata]](https://packages.gentoo.org/packages/sys-apps/hwdata)[]]. To get a more recent database install a new(er) version of hwdata.

`root `[`#`]`emerge --ask sys-apps/hwdata`

## [Configuration]

### [Files]

-   [/etc/conf.d/pciparm]

## [Usage]

### [Invocation]

`user `[`$`]`lspci help`

    Usage: lspci [<switches>]

    Basic display modes:
    -mm     Produce machine-readable output (single -m for an obsolete format)
    -t      Show bus tree

    Display options:
    -v      Be verbose (-vv or -vvv for higher verbosity)
    -k      Show kernel drivers handling each device
    -x      Show hex-dump of the standard part of the config space
    -xxx        Show hex-dump of the whole config space (dangerous; root only)
    -xxxx       Show hex-dump of the 4096-byte extended config space (root only)
    -b      Bus-centric view (addresses and IRQ's as seen by the bus)
    -D      Always show domain numbers
    -P      Display bridge path in addition to bus and device number
    -PP     Display bus path in addition to bus and device number

    Resolving of device ID's to names:
    -n      Show numeric ID's
    -nn     Show both textual and numeric ID's (names & numbers)

    Selection of devices:
    -s [[[[<domain>]:]<bus>]:][<slot>][.[<func>]]   Show only devices in selected slots
    -d [<vendor>]:[<device>][:<class>]        Show only devices with specified ID's

    Other options:
    -i <file> Use specified ID database instead of /usr/share/misc/pci.ids.gz
    -p <file> Look up kernel modules in a given file instead of default modules.pcimap
    -M      Enable `bus mapping' mode (dangerous; root only)

    PCI access options:
    -A <method>   Use the specified PCI access method (see `-A help' for a list)
    -O =<val>  Set PCI access parameter (see `-O help' for a list)
    -G      Enable PCI access debugging
    -H <mode> Use direct hardware access (<mode> = 1 or 2)
    -F <file> Read PCI configuration dump from a given file

## [Removal]

### [Unmerge]

`root `[`#`]`emerge --ask --depclean --verbose sys-apps/pciutils`

## [See also]

-   [Hardware detection](https://wiki.gentoo.org/wiki/Hardware_detection "Hardware detection") --- lists and describes utilities used to detect and provide information on hardware.
-   [Lshw](https://wiki.gentoo.org/wiki/Lshw "Lshw") --- a small tool that provides detailed information on the hardware configuration of the machine. It can report exact memory configuration, firmware version, mainboard configuration, CPU version and speed, cache configuration, bus speed, etc. on DMI-capable x86 or EFI (IA-64) systems and on some PowerPC machines (PowerMac G4 is known to work).
-   [Usbutils](https://wiki.gentoo.org/wiki/Usbutils "Usbutils") --- a collection various utilities for querying the the Universal Serial Bus (USB).