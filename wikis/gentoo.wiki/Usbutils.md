[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=Usbutils&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

**Resources**

[[]][Home](http://linux-usb.sourceforge.net/)

[[]][Package information](https://packages.gentoo.org/packages/sys-apps/usbutils)

[[]][GitWeb](https://git.kernel.org/cgit/linux/kernel/git/gregkh/usbutils.git/)

[[]][GitHub](https://github.com/gregkh/usbutils)

usbutils is a collection various utilities for querying the the Universal Serial Bus (USB). The most prominent utility included is [lsusb], a hardware detection tool for system resources connected to the Universal Serial Bus.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
-   [[2] [Usage]](#Usage)
    -   [[2.1] [Invocation]](#Invocation)
-   [[3] [See also]](#See_also)

## [Installation]

### [USE flags]

### [USE flags for] [sys-apps/usbutils](https://packages.gentoo.org/packages/sys-apps/usbutils) [[]] [USB enumeration utilities]

  ------------------------------------------------------------- ----------------------------------------------------------------
  [`python`](https://packages.gentoo.org/useflags/python)       Add optional support/bindings for the Python language
  [`usbreset`](https://packages.gentoo.org/useflags/usbreset)   additionally compile the potentially problematic usbreset util
  ------------------------------------------------------------- ----------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-04-19 15:52] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

`root `[`#`]`emerge --ask sys-apps/usbutils`

[lsusb] detects the devices based on an ID database provided by [[[sys-apps/hwids]](https://packages.gentoo.org/packages/sys-apps/hwids)[]] which will be installed as a dependency of usbutils.

## [Usage]

### [Invocation]

`user `[`$`]`qlist usbutils | grep bin/`

    /usr/bin/usb-devices
    /usr/bin/lsusb
    /usr/bin/usbhid-dump

`user `[`$`]`lsusb -h`

    Usage: lsusb [options]...
    List USB devices
      -v, --verbose
          Increase verbosity (show descriptors)
      -s [[bus]:][devnum]
          Show only devices with specified device and/or
          bus numbers (in decimal)
      -d vendor:[product]
          Show only devices with the specified vendor and
          product ID numbers (in hexadecimal)
      -D device
          Selects which device lsusb will examine
      -t, --tree
          Dump the physical USB device hierarchy as a tree
      -V, --version
          Show version of program
      -h, --help
          Show usage and help

## [See also]

-   [Hardware detection](https://wiki.gentoo.org/wiki/Hardware_detection "Hardware detection") --- lists and describes utilities used to detect and provide information on hardware.
-   [Lshw](https://wiki.gentoo.org/wiki/Lshw "Lshw") --- a small tool that provides detailed information on the hardware configuration of the machine. It can report exact memory configuration, firmware version, mainboard configuration, CPU version and speed, cache configuration, bus speed, etc. on DMI-capable x86 or EFI (IA-64) systems and on some PowerPC machines (PowerMac G4 is known to work).
-   [Pciutils](https://wiki.gentoo.org/wiki/Pciutils "Pciutils") --- contains various utilities dealing with the [PCI bus](https://en.wikipedia.org/wiki/Peripheral_Component_Interconnect "wikipedia:Peripheral Component Interconnect") (primarily [lspci]).