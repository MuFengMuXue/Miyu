# NAME

sane-umax1220u - SANE backend for the UMAX Astra 1220U and similar scanners

# DESCRIPTION

The **sane-umax1220** library implements a SANE (Scanner Access Now Easy) backend for the the UMAX Astra 1220U and similar scanners.

For more information on this backend, please visit *http://umax1220u-sane.sourceforge.net/*.

# UMAX ASTRA 1600U/2000U/2100U SUPPORT

This backend is also able to drive the UMAX Astra 1600U/2000U/2100U. The 2100U is confirmed to work. For the other scanners no reports have been received yet. Please contact us and tell us if your scanner works (*sane-devel@alioth-lists.debian.net*).

# CONFIGURATION

Usually, no manual configuration is necessary. The configuration file for this backend resides in *@CONFIGDIR@/umax1220u.conf*.

Its content is a list of device names that correspond to UMAX Astra scanners. Empty lines and lines starting with a hash mark (#) are ignored. A sample configuration file is shown below:

     #usb vendor product
     usb 0x1606 0x0010
     # Device list for non-linux systems
     /dev/scanner
     /dev/usb/scanner0

See **sane-usb**(5) for information on how to set the access permissions on the usb device files.

# FILES

The backend configuration file:
*@CONFIGDIR@/umax1220u.conf*

The static library implementing this backend:
*@LIBDIR@/libsane-umax1220u.a*

The shared library implementing this backend:
*@LIBDIR@/libsane-umax1220u.so* (present on systems that support dynamic loading)

# ENVIRONMENT

**SANE_DEBUG_UMAX1220U**
If the library was compiled with debug support enabled, this environment variable controls the debug level for this backend. E.g., a value of 128 requests all debug output to be printed. Smaller levels reduce verbosity:

**SANE_DEBUG_UMAX1220U** values:


    Number  Remark
     1       print failures
     2       print information
     3       print high-level function calls
     4       print high-level function checkpoints
     9       print mid-level function calls
     10      print mid-level function checkpoints
     80      print protocol-level function entry
     90      print protocol-level function exit

Example:
export SANE_DEBUG_UMAX1220U=10

# KNOWN BUGS

600 dpi scanning may fail for large image sizes.

If you keep getting I/O errors, try cycling the power on your scanner to reset it.

There is no way to cancel a scan, since the driver ignores **sane_cancel**().

If you try scanning an image which is too small, you will get I/O errors. Be sure to adjust the scan area before doing a scan, since by default, the scan area is zero.

# SEE ALSO

**sane**(7), **sane-usb**(5)

(Old) homepage:
*http://umax1220u-sane.sourceforge.net/*

# AUTHOR

Marcio Luis Teixeira \<*marciot@users.sourceforge.net*\>

# EMAIL-CONTACT

*sane-devel@alioth-lists.debian.net*

# REPORTING BUGS

This backend isn't actively maintained. Nevertheless, bug reports and comments should be sent to the sane-devel mailing list. When reporting bugs, please run the backend with **SANE_DEBUG_UMAX1220U** set to 10 and attach a copy of the log messages.
