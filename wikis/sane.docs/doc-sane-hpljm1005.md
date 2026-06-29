# NAME

sane-hpljm1005 - SANE backend for Hewlett-Packard LaserJet M1005 MFP Scanner

# DESCRIPTION

The **sane-hpljm1005** library implements a SANE (Scanner Access Now Easy) backend that provides access to the following Hewlett-Packard scanner:

> LaserJet M1005

If you own a scanner other than the ones listed above that works with this backend, please let us know this by sending the scanner's exact model name and the USB vendor and device ids (e.g. from */proc/bus/usb/devices*, **sane-find-scanner**(1) or syslog) to us. Even if the scanner's name is only slightly different from the models mentioned above, please let us know.

# CONFIGURATION

None required.

# FILES

*@LIBDIR@/libsane-hpljm1005.a*
The static library implementing this backend.

*@LIBDIR@/libsane-hpljm1005.so*
The shared library implementing this backend (present on systems that support dynamic loading).

# ENVIRONMENT

**SANE_DEBUG_HPLJM1005**
If the library was compiled with debug support enabled, this environment variable controls the debug level for this backend. Higher debug levels increase the verbosity of the output.

There is not currently a great deal of diagnostic output, it being mainly confined to error conditions.

# SEE ALSO

**sane**(7), **sane-usb**(5), **sane-find-scanner**(1)

# AUTHOR

Philippe Rétornaz \<*couriousous@mandriva.org*\>
