# NAME

sane-xerox_mfp - SANE backend for Xerox Phaser 3200MFP device et al.

# DESCRIPTION

The **sane-xerox_mfp** library implements a SANE (Scanner Access Now Easy) backend that provides access to several Samsung-based Samsung, Xerox, and Dell scanners. Please see full list of supported devices at *http://www.sane-project.org/sane-supported-devices.html*.

# CONFIGURATION

*@CONFIGDIR@/xerox_mfp.conf*
USB scanners do not need any configuration.

For SCX-4500W in network mode you need to specify

> **tcp host_address \[port\]**

The **host_address** is passed through resolver, thus can be a dotted quad or a name from */etc/hosts* or resolvable through DNS.

# FILES

*@CONFIGDIR@/xerox_mfp.conf*
The backend configuration file. By default all scanner types/models are enabled, you may want to comment out unwanted entries.

*@LIBDIR@/libsane-xerox_mfp.a*
The static library implementing this backend.

*@LIBDIR@/libsane-xerox_mfp.so*
The shared library implementing this backend (present on systems that support dynamic loading).

# ENVIRONMENT

**SANE_DEBUG_XEROX_MFP**
If the library was compiled with debug support enabled, this environment variable controls the debug level for this backend. Higher debug levels increase the verbosity of the output.

Example: export SANE_DEBUG_XEROX_MFP=4

# LIMITATIONS

Multicast autoconfiguration for LAN scanners is not implemented yet. IPv6 addressing has never been tested.

# BUGS AND SUPPORT

If you have found a bug or need support please follow open-source way of acquiring support via mail-lists *http://www.sane-project.org/mailing-lists.html* or SANE bug tracker *http://www.sane-project.org/bugs.html*.

# AUTHORS

Alex Belkin \<*abc@telekom.ru*\>.
Samsung SCX-4500W scan over network support by Alexander Kuznetsov \<*acca(at)cpan.org*\>.
Color scanning on Samsung M2870 model and Xerox Cognac 3215 & 3225 models by Laxmeesh Onkar Markod \<*m.laxmeesh@samsung.com*\>.

# SEE ALSO

**sane**(7), **sane-usb**(5)
