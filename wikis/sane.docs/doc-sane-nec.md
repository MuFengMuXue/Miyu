# NAME

sane-nec - SANE backend for NEC scanners

# DESCRIPTION

The **sane-nec** library implements a SANE (Scanner Access Now Easy) backend that provides access to NEC SCSI scanners. This backend should be considered **alpha-quality** software! In the current state it is known to work with PC-IN500/4C scanners. Other MultiReader scanner series are not supported. PC-IN 500/4C and MultiReader scanner are only sold in Japan (except Multi Reader PetiScan).

For other scanners, it may or may not work.

The backend has the following known problems:

> \- ColorLineart mode is not supported.
> \- Device name is fixed to */dev/scanner*
>
> At present, the following scanners are known to work with this backend.
>
> > Vendor Product id
> >     ------ -----------
> >     NEC    PC-IN500/4C

# FILES

*@CONFIGDIR@/nec.conf*
The backend configuration file.

*@LIBDIR@/libsane-nec.a*
The static library implementing this backend.

*@LIBDIR@/libsane-nec.so*
The shared library implementing this backend (present on systems that support dynamic loading).

# ENVIRONMENT

**SANE_DEBUG_NEC**
If the library was compiled with debug support enabled, this environment variable controls the debug level for this backend. E.g., a value of 128 requests all debug output to be printed. Smaller levels reduce verbosity.

# SEE ALSO

**sane**(7), **sane-scsi**(5)

# AUTHORS

Kazuya Fukuda
