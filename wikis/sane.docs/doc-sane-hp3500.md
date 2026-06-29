# NAME

sane-hp3500 - SANE backend for Hewlett-Packard ScanJet 3500 series scanners

# DESCRIPTION

The **sane-hp3500** library implements a SANE (Scanner Access Now Easy) backend that provides access to the following Hewlett-Packard USB flatbed scanners:

> ScanJet 3500C
> ScanJet 3530C
> ScanJet 3570C

If you own a scanner other than the ones listed above that works with this backend, please let us know this by sending the scanner's exact model name and the USB vendor and device ids (e.g. from */proc/bus/usb/devices*, **sane-find-scanner (1)** or syslog) to us. Even if the scanner's name is only slightly different from the models mentioned above, please let us know.

# CONFIGURATION

None required.

# FILES

*@LIBDIR@/libsane-hp3500.a*
The static library implementing this backend.

*@LIBDIR@/libsane-hp3500.so*
The shared library implementing this backend (present on systems that support dynamic loading).

# ENVIRONMENT

**SANE_DEBUG_HP3500** If the library was compiled with debug support enabled, this environment variable controls the debug level for this backend. Higher debug levels increase the verbosity of the output.

Example: export SANE_DEBUG_HP3500=4

# SEE ALSO

**sane**(7), **sane-usb**(5),
*http://projects.troy.rollo.name/rt-scanners/*

# AUTHOR

Troy Rollo \<*sane@troy.rollo.name*\>
