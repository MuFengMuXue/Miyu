# NAME

sane-epjitsu - SANE backend for Epson-based Fujitsu USB scanners

# DESCRIPTION

The **sane-epjitsu** library implements a SANE (Scanner Access Now Easy) backend which provides basic access the Fujitsu fi-60F/fi-65F and ScanSnap S300/S1300(i)/S1100(i) scanners.

# HARDWARE SUPPORT

These scanners are fairly limited, only supporting a couple of modes and resolutions, and always scanning full width. The backend supports missing modes (binary, grayscale) and intermediate resolutions in software, but provides only minimal scan area controls. See **KNOWN ISSUES.**

This backend may support other scanners. If physical inspection reveals an Epson chipset, please contact the author for instructions on collecting a USB trace under Windows to verify.

# OPTIONS

A limited effort has been made to expose the standard options to the API. This allows a frontend to set resolution, color mode, and choose the ADF setting. The **sane-epjitsu** backend supports the following basic options for most scanners:

**source s**

> Selects the source for the scan. Options may include "Flatbed", "ADF Front", "ADF Back", "ADF Duplex".

**mode m**

> Selects the mode for the scan. Options may include "Lineart", "Gray", "Color".

**resolution**,** y-resolution**

> Controls scan resolution. Setting **--resolution** also sets **--y-resolution**, though this behavior is overridden by some frontends.

Other options will be available based on the capabilities of the scanner. Use *'scanimage --help'* to get a list. Be aware that some options may appear only when another option has been set, and that advanced options may be hidden by the frontend.

# CONFIGURATION FILE

The configuration file *@CONFIGDIR@/epjitsu.conf* is used to tell the backend how to look for scanners, and provide options controlling the operation of the backend. This file is read each time the frontend asks the backend for a list of scanners, generally only when the frontend starts. If the configuration file is missing, the backend will not work.

Scanners can be specified in the configuration file in two ways:

"usb 0x04c5 0x10c7" (or other vendor/product ids)

> Requests backend to search all usb buses in the system for a device which uses that vendor and product id. The device will then be queried to determine if it is a supported scanner.

"usb /dev/usb/scanner0" (or other device file)

> Some systems use a kernel driver to access usb scanners. This method is untested.

The only configuration option supported is "firmware /PATH/TO/FILE", allowing you to set the location of the firmware file you have extracted from the Windows driver.

**Note:** This firmware is a copyrighted work of Fujitsu, so cannot be provided by the backend or the author. Please do not ask.

**Note:** These scanners REQUIRE a firmware file to function. See the supplied configuration file for more detail.

**Note:** This option may appear multiple times in the configuration file. It only applies to scanners discovered by 'usb' lines that follow this option.

# ENVIRONMENT

The backend uses a single environment variable, **SANE_DEBUG_EPJITSU,** which enables debugging output to stderr. Valid values are:

> 5 Errors
> 10 Function trace
> 15 Function detail
> 20 Option commands
> 25 USB trace
> 30 USB detail
> 35 Useless noise

# KNOWN ISSUES

> Only limited scan area options are exposed.
>
> fi-60F and fi-65F hardware grayscale mode is not used, because the calibration code is not finished.

# CREDITS

S300 support funded by Microdea, Inc. and Archivista, GmbH.
fi-60F support funded by TrueCheck, Inc.
Improved calibration code provided by Richard Goedeken.

# SEE ALSO

**sane**(7), **sane-usb**(5) **scanimage**(1)

# AUTHOR

m\. allan noah: \<*kitno455 a t gmail d o t com*\>
