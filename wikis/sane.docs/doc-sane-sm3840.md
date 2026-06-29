# NAME

sane-sm3840 - SANE backend for Microtek scanners with SCAN08 USB chip

# DESCRIPTION

The **sane-sm3840** library implements a SANE (Scanner Access Now Easy) backend that provides access to some Microtek scanners with the SCAN08 USB chip.

There exist backends for Microtek scanners with SCSI command set. Refer to **sane-microtek**(5) and **sane-microtek2**(5) for details.

There also exists a Microtek 3600 series driver, see **sane-sm3600**(5) for details.

At present, the following scanners are known positively to work with this backend:

> Vendor     Product ID:     Remark:
>     --------   --------------  -----------
>     Microtek   ScanMaker 3840  All modes OK
>     Microtek   ScanMaker 4800  All modes OK

If you own a Microtek scanner with the SCAN08 chip other than the ones listed above, it may or may not work with SANE. Feel free to contact the backend author (*earle@ziplabel.com*) to report results with scanners not on the list.

# FRONTEND OPTIONS

The following options are supported by the **sane-sm3840** driver:

**--mode color\|gray\|lineart\|halftone**
Color or grayscale mode.


**--resolution 150\|300\|600\|1200**
Pixels per inch for scans.


**--depth 8\|16**
Note that the least significant bits of 16bpp mode may be noise.


**--brightness 1..4096**
Higher numbers increase brightness of returned image.


**--contrast 0.1..9.9**
Larger numbers decrease contrast of returned image.


**--lamp-timeout 1..15**
Time in minutes until the lamp is turned off after a scan.

# CONFIGURATION

This backend does not support a configuration file right now.

# FILES

*@LIBDIR@/libsane-sm3840.a*
The static library implementing this backend.

*@LIBDIR@/libsane-sm3840.so*
The shared library implementing this backend (present on systems that support dynamic loading).

# ENVIRONMENT

**SANE_DEBUG_SM3840**
If the library was compiled with debug support enabled, this environment variable controls the debug level for this backend. E.g., a value of 128 requests all debug output to be printed. Smaller levels reduce verbosity. To see error messages on stderr set **SANE_DEBUG_SM3840** to 1.

# SEE ALSO

**sane**(7), **sane-microtek**(5), **sane-microtek2**(5), **sane-sm3600**(5)
*http://www.ziplabel.com/sm3840*

# AUTHOR

Earle F. Philhower III \<*earle@ziplabel.com*\>
