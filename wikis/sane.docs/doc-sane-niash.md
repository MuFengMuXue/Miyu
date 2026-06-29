# NAME

sane-niash - SANE backend for scanners based on the NIASH chipset

# DESCRIPTION

The **sane-niash** implements a SANE (Scanner Access Now Easy) backend that provides access to NIASH chipset based scanners. This backend will try to support the following models:

    MANUFACTURER:    MODEL:          USB ID:
    ---------------  ----------------  ---------
    Agfa             Snapscan Touch    06BD-0100 (1)(a)
    Trust            Office Scan 19200 047B-1000 (1)(a)
    Hewlett-Packard  Scanjet 3300c     03F0-0205 (1)(a)(b)
    Hewlett-Packard  Scanjet 3400c     03F0-0405 (2)(b)
    Hewlett-Packard  Scanjet 4300c     03F0-0305 (2)(a)
    Silitek          ScanJet 4300c     047B-1002 (2)(b)


ASIC: (1) - NIASH00012/00013/00014 / (2) - NIASH00019
ANALOG FRONT-END: (a) - ESIC ES8100QA / (b) - WM8143-12

# CONFIGURATION

The *niash.conf* file is meant for future configuration options. Empty lines and lines starting with a hash mark (#) are ignored. Currently no configuration options exist.

# FILES

*@LIBDIR@/libsane-niash.a*
The static library implementing this backend.


*@LIBDIR@/libsane-niash.so*
The shared library implementing this backend (present on systems that support dynamic loading).

# CAVEATS

If you use a
Hewlett-Packard Scanjet 3400c or
Hewlett-Packard Scanjet 4300c
together with Linux kernel **2.6**, kernel version **2.6.8** or newer is necessary.

# ENVIRONMENT

**SANE_DEBUG_NIASH**
If the library was compiled with debug support enabled, this environment variable controls the debug level for this backend. Higher debug levels increase the verbosity of the output.

Example: export SANE_DEBUG_NIASH=255

# SEE ALSO

**sane**(7), **sane-usb**(5)
*http://www.sourceforge.net/projects/hp3300backend*

# AUTHOR

Bertrik Sikken \<*bertrik@zonnet.nl*\>
