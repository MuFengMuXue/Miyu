# NAME

sane-lexmark_x2600 - SANE backend for Lexmark X2600 Series scanners

# DESCRIPTION

The **sane-lexmark** library implements a SANE (Scanner Access Now Easy) backend that provides access to the scanner part of Lexmark X2600 AIOs.

The scanners that should work with this backend are:

>    Vendor Model           status
>     ----------------------  -----------
>       Lexmark X2670           good

The options the backend supports can either be selected through command line options to programs like **scanimage**(1) or through GUI elements in **xscanimage**(1) , **xsane**(1). or **simple-scan**(1).
If you notice any strange behavior, please report to the backend maintainer or to the SANE mailing list.

# FILES

*@LIBDIR@/libsane-lexmark_x2600.a*
The static library implementing this backend.

*@LIBDIR@/libsane-lexmark_x2600.so*
The shared library implementing this backend (present on systems that support dynamic loading).

# ENVIRONMENT

**SANE_DEBUG_LEXMARK_X2600**
If the library was compiled with debug support enabled, this environment variable controls the debug level for this backend. E.g., a value of 255 requests all debug output to be printed. Smaller levels reduce verbosity.

# AUTHOR

The backend was originally written by Benoit Juin.
\<*benoit.juin@gmail.com*\>

# CREDITS

Many thanks go to:
@skelband aka Ralph Little who help me to dive in the sane-backencode and reviewed the sources.
