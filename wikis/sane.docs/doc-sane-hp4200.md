# NAME

sane-hp4200 - SANE backend for Hewlett-Packard 4200 scanners

# DESCRIPTION

The **sane-hp4200** library implements a SANE (Scanner Access Now Easy) backend that provides access to the following Hewlett-Packard USB flatbed scanners:

> ScanJet 4200 C
> ScanJet 4200 Cxi
> ScanJet 4200 Cse

More details can be found on the hp4200 backend homepage *http://hp4200-backend.sourceforge.net/*.

This is BETA software. Keep your hand at the scanner's plug and unplug it, if the head bumps at the end of the scan area.

If you own a scanner other than the ones listed above that works with this backend, please let us know this by sending the scanner's exact model name and the USB vendor and device ids (e.g. from */proc/bus/usb/devices*, **sane-find-scanner**(1) or syslog) to us. Even if the scanner's name is only slightly different from the models mentioned above, please let us know.

# CONFIGURATION

The contents of the *hp4200.conf* file is a list of usb lines containing vendor and product ids that correspond to USB scanners. The file can also contain the names of device files that correspond to an HP 4200 scanner. Empty lines and lines starting with a hash mark (#) are ignored. The scanners are autodetected by **usb vendor_id product_id** statements which are already included into *hp4200.conf*. "vendor_id" and "product_id" are hexadecimal numbers that identify the scanner. If autodetection does not work, add the device name of your scanner to the configuration file, e.g. */dev/usb/scanner0*.

# FILES

*@CONFIGDIR@/hp4200.conf*
The backend configuration file (see also description of **SANE_CONFIG_DIR** below).

*@LIBDIR@/libsane-hp4200.a*
The static library implementing this backend.

*@LIBDIR@/libsane-hp4200.so*
The shared library implementing this backend (present on systems that support dynamic loading).

# ENVIRONMENT

**SANE_CONFIG_DIR**
This environment variable specifies the list of directories that may contain the configuration file. On \*NIX systems, the directories are separated by a colon (\`:'), under OS/2, they are separated by a semi-colon (\`;'). If this variable is not set, the configuration file is searched in two default directories: first, the current working directory (*.*) and then in *@CONFIGDIR@*. If the value of the environment variable ends with the directory separator character, then the default directories are searched after the explicitly specified directories. For example, setting **SANE_CONFIG_DIR** to "/tmp/config:" would result in directories *tmp/config*, *.*, and *@CONFIGDIR@* being searched (in this order).

**SANE_DEBUG_HP4200**
If the library was compiled with debug support enabled, this environment variable controls the debug level for this backend. Higher debug levels increase the verbosity of the output.

Example: export SANE_DEBUG_HP4200=4

# SEE ALSO

**sane**(7), **sane-usb**(5), **sane-find-scanner**(1),
*http://hp4200-backend.sourceforge.net/*

# AUTHOR

Adrian Perez Jorge, Andrew John Lewis, Arnar Mar Hrafnkelsson, Frank Zago, Henning Meier-Geinitz. Current maintainer: Henning Meier-Geinitz \<*henning@meier-geinitz.de*\>.

# BUGS

Tested only with Linux.

Only 8 bit color mode works.

Scanning is slow due to backtracking.

Send bug reports to the sane-devel mailing list: *sane-devel@alioth-lists.debian.net*.
