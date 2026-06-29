# NAME

sane-canon630u - SANE backend for the Canon 630u USB flatbed scanner

# DESCRIPTION

The **sane-canon630u** library implements a SANE (Scanner Access Now Easy) backend that provides access to the following Canon flatbed scanners:

> CanoScan 630u
> CanoScan 636u

Color scanning is supported at 75, 150, 300, and 600 dpi, and gamma and analog gain are adjustable.

TESTERS ARE WELCOME. Send your bug reports and comments to Nathan Rutman *\<nthn1@yahoo.com\>*.

# CONFIGURATION

The contents of the *canon630u.conf* file is a list of device names that correspond to Canon USB scanners. Empty lines and lines starting with a hash mark (#) are ignored. Only one device name can be listed in *canon630u.conf*. The program **sane-find-scanner**(1) helps to find out the correct device. Under Linux, such a device name could be */dev/usb/scanner0* for example. See **sane-usb**(5) for details.

This product-specific scanner driver uses the lower-level kernel USB driver "scanner". Check for "Driver=usbscanner" under */proc/bus/usb/devices*. If "Driver=(none)", try forcing it with *insmod scanner vendor=0x04a9 product=0x2204*

# NOTES

Due to Canon's unwillingness to provide scanner documentation, this software was developed by analyzing the USB traffic of the Windows 2000 driver. So things like the calibration procedure I kind of made up; it seems to work for my scanner. If you have complaints, let me know.

This driver requires the ability to send USB Control Messages, available in kernel 2.4.12 or later.

Some users have reported that this driver doesn't work at all. This seems to be a hardware specific issue, although I dsane-uson't know what exactly the problem is. If you are having problems, please send me the info in */proc/bus/usb/devices*, */proc/pci*, the kernel *scanner.c* driver version from */var/log/messages*, and the output from *SANE_DEBUG_CANON630U=12 scanimage \> /dev/null*

# FILES

*@CONFIGDIR@/canon630u.conf*
The backend configuration file (see also description of **SANE_CONFIG_DIR** below).

*@LIBDIR@/libsane-canon630u.a*
The static library implementing this backend.

*@LIBDIR@/libsane-canon630u.so*
The shared library implementing this backend (present on systems that support dynamic loading).

*/tmp/canon.cal*
The calibration file used to normalize pixel brightness. This is calculated every time the scanner is first used after it has lost power. Deleting this file will force recalibration.

# ENVIRONMENT

**SANE_CONFIG_DIR**
This environment variable specifies the list of directories that may contain the configuration file. On \*NIX systems, the directories are separated by a colon (\`:'), under OS/2, they are separated by a semi-colon (\`;'). If this variable is not set, the configuration file is searched in two default directories: first, the current working directory (".") and then in *@CONFIGDIR@*. If the value of the environment variable ends with the directory separator character, then the default directories are searched after the explicitly specified directories. For example, setting **SANE_CONFIG_DIR** to "/tmp/config:" would result in directories *tmp/config*, *.*, and *@CONFIGDIR@* being searched (in this order).

**SANE_DEBUG_CANON630U**
If the library was compiled with debug support enabled, this environment variable controls the debug level for this backend. Higher debug levels increase the verbosity of the output.

Example:
SANE_DEBUG_CANON630U=12 scanimage \> /dev/null

# SEE ALSO

**sane**(7), **sane-usb**(5), **sane-find-scanner**(1)
*http://canon-fb630u.sourceforge.net/*

# AUTHOR

Nathan Rutman
