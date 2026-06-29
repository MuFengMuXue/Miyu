# NAME

sane-mustek_usb2 - SANE backend for SQ113 based USB flatbed scanners

# DESCRIPTION

The **sane-mustek_usb2** library implements a SANE (Scanner Access Now Easy) backend that provides access to USB flatbed scanners based on the Service & Quality SQ113 chipset. At the moment, only the Mustek BearPaw 2448 TA Pro is supported. It's planned to add support for other scanners that are based on the SQ113 and maybe SQ11 chip. For more details, see the **sane-mustek_usb2** backend homepage: *http://www.meier-geinitz.de/sane/mustek_usb2-backend/*.

This is BETA software. Especially if you test new or untested scanners, keep your hand at the scanner's plug and unplug it, if the head bumps at the end of the scan area.

If you own a scanner other than the ones listed on the mustek_usb2 homepage that works with this backend, please let me know this by sending the scanner's exact model name and the USB vendor and device ids (e.g. from **sane-find-scanner**(1) or syslog) to me. Even if the scanner's name is only slightly different from the models already listed as supported, please let me know.

# LIBUSB ISSUES

Please use libusb-0.1.8 or later. Without libusb or with older libusb versions all kinds of trouble can be expected. The scanner should be found by **sane-find-scanner**(1) without further actions. For setting permissions and general USB information, look at **sane-usb**(5).

# FILES

*@LIBDIR@/libsane-mustek_usb2.a*
The static library implementing this backend.

*@LIBDIR@/libsane-mustek_usb2.so*
The shared library implementing this backend (present on systems that support dynamic loading).

# ENVIRONMENT

**SANE_DEBUG_MUSTEK_USB2**
If the library was compiled with debug support enabled, this environment variable controls the debug level for this backend. Higher debug levels increase the verbosity of the output.

Example: export SANE_DEBUG_MUSTEK_USB2=4

# SEE ALSO

**sane**(7), **sane-usb**(5), **sane-plustek**(5), **sane-ma1509**(5), **sane-mustek_usb**(5), **sane-mustek**(5), **sane-mustek_pp**(5), **sane-find-scanner**(1)


*@DOCDIR@/mustek_usb2/mustek_usb2.CHANGES*
*http://www.meier-geinitz.de/sane/mustek_usb2-backend/*

# AUTHOR

The driver has been written Roy Zhou, Jack Xu, and Vinci Cen from Mustek.
Adjustments to SANE by Henning Meier-Geinitz.

# BUGS

Please contact me if you find a bug or missing feature: \<*henning@meier-geinitz.de*\>.
Please send a debug log if your scanner isn't detected correctly (see **SANE_DEBUG_MUSTEK_USB2** above).
