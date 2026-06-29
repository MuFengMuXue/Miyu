# NAME

sane-ricoh2 - SANE backend for Ricoh flatbed scanners

# DESCRIPTION

The **sane-ricoh2** library implements a SANE (Scanner Access Now Easy) backend that provides access to the following Ricoh flatbed scanners:

> SG-3110SFNw
> SG-3100SNw
> SP-100SU
> SP-111SU (SP-112SU)

# FILES

*@LIBDIR@/libsane-ricoh2.a*
The static library implementing this backend.

*@LIBDIR@/libsane-ricoh2.so*
The shared library implementing this backend (present on systems that support dynamic loading).

# OPTIONS

The options the backend supports can either be selected through command line options to programs like **scanimage**(1) or through GUI elements in programs like **xscanimage**(1) or **xsane**(1).

The following options are supported by ricoh2:

**--mode color\|gray**

> Color or grayscale mode.

**--resolution 300\|600**

> DPI resolution.

# ENVIRONMENT

**SANE_DEBUG_RICOH2**
If the library was compiled with debug support enabled, this environment variable controls the debug level for this backend. Higher debug levels increase the verbosity of the output.

# SEE ALSO

**sane**(7), **sane-usb**(5), **scanimage**(1), **xscanimage**(1), **xsane**(1)

# AUTHOR

Stanislav Yuzvinsky
