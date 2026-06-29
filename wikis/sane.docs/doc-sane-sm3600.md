# NAME

sane-sm3600 - SANE backend for Microtek scanners with M011 USB chip

# DESCRIPTION

The **sane-sm3600** library implements a SANE (Scanner Access Now Easy) backend that provides access to some Microtek scanners with the Toshiba M011 custom USB chip. This backend should be considered alpha.

There are also backends for Microtek scanners with SCSI command set. Refer to **sane-microtek**(5) and **sane-microtek2**(5) for details.

At present, the following scanners are known positively to work with this backend:

> Vendor     Product id:     Remark:
>     --------   --------------  -----------
>     Microtek   ScanMaker 3600  all modes ok
>     Microtek   ScanMaker 3700  reported to work
>     Microtek   ScanMaker 3750  reported to work

If you own a Microtek scanner with the M011 chip other than the ones listed above, it may or may not work with SANE!

# FRONTEND OPTIONS

This backend dynamically enables the options for the frontend, that are supported by the scanner dependent on the scanning-mode and other options. Unsupported options are disabled.

The following options are supported by the **sane-sm3600** backend: Color, grayscale, halftone and lineart scans. Also contrast, brightness, and gamma correction.

# DEVICE NAMES

This backend does not support device names in a standardized form.

# CONFIGURATION

This backend does not support a configuration file right now.

# FILES

*@LIBDIR@/libsane-sm3600.a*
The static library implementing this backend.

*@LIBDIR@/libsane-sm3600.so*
The shared library implementing this backend (present on systems that support dynamic loading).

# ENVIRONMENT

**SANE_DEBUG_SM3600**
If the library was compiled with debug support enabled, this environment variable controls the debug level for this backend. E.g., a value of 128 requests all debug output to be printed. Smaller levels reduce verbosity. To see error messages on stderr set **SANE_DEBUG_SM3600** to 1.


E.g. just say:
export SANE_DEBUG_SM3600=5

# SEE ALSO

**sane**(7)**,** **sane-microtek**(5), **sane-microtek2**(5)
*http://sm3600.sourceforge.net*

# AUTHOR


Marian Eichholz \<*eichholz@computer.org*\>
Glenn Ramsey \<*glenn@componic.com*\>
