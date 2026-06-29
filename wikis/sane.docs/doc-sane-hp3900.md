# NAME

sane-hp3900 - SANE backend for RTS8822 chipset based scanners

# DESCRIPTION

The **sane-hp3900** library implements a SANE (Scanner Access Now Easy) backend that provides access at least to the following USB flatbed scanners:

> Model:                     Chipset:
>     ------                     --------
>     HP ScanJet 3800            RTS8822BL-03A
>     HP ScanJet 3970            RTS8822L-01H
>     HP ScanJet 4070 Photosmart RTS8822L-01H
>     HP ScanJet 4370            RTS8822L-02A
>     HP ScanJet G2710           RTS8822BL-03A
>     HP ScanJet G3010           RTS8822L-02A
>     HP ScanJet G3110           RTS8822L-02A
>     UMAX Astra 4900/4950       RTS8822L-01H *
>     BenQ 5550                  RTS8823L-01E *

More details can be found on the **sane-hp3900**(5) backend homepage *http://sourceforge.net/projects/hp3900-series/*.

This is ALPHA software. Keep your hand at the scanner's plug and unplug it, if scanner does not start to scan. See also the **BUGS** section.

If you own a scanner other than the ones listed above that works with this backend, please let us know this by sending the scanner's exact model name and the USB vendor and device ids (e.g. from */proc/bus/usb/devices*, **sane-find-scanner**(1) or syslog) to us. Even if the scanner's name is only slightly different from the models mentioned above, please let us know.

# CONFIGURATION

The contents of the *hp3900.conf* file is a list of usb lines containing vendor and product ids that correspond to USB scanners. The file can also contain the names of device files that correspond to an HP 39XX scanner. Empty lines and lines starting with a hash mark (#) are ignored. The scanners are autodetected by **usb vendor_id product_id** statements which are already included into *hp3900.conf*. "vendor_id" and "product_id" are hexadecimal numbers that identify the scanner. If autodetection does not work, add the device name of your scanner to the configuration file,

# FILES

*@CONFIGDIR@/hp3900.conf*
The backend configuration file (see also description of **SANE_CONFIG_DIR** below).

*@LIBDIR@/libsane-hp3900.a*
The static library implementing this backend.

*@LIBDIR@/libsane-hp3900.so*
The shared library implementing this backend (present on systems that support dynamic loading).

# ENVIRONMENT

**SANE_CONFIG_DIR**
This environment variable specifies the list of directories that may contain the configuration file. On \*NIX systems, the directories are separated by a colon (\`:'), under OS/2, they are separated by a semi-colon (\`;'). If this variable is not set, the configuration file is searched in two default directories: first, the current working directory (*.*) and then in *@CONFIGDIR@*. If the value of the environment variable ends with the directory separator character, then the default directories are searched after the explicitly specified directories. For example, setting **SANE_CONFIG_DIR** to "/tmp/config:" would result in directories *tmp/config*, *.*, and *@CONFIGDIR@* being searched (in this order).

**SANE_DEBUG_HP3900**
If the library was compiled with debug support enabled, this environment variable controls the debug level for this backend. Higher debug levels increase the verbosity of the output.

Example: export SANE_DEBUG_HP3900=4

# SEE ALSO

**sane**(7), **sane-usb**(5), **sane-find-scanner**(1),
*http://sourceforge.net/projects/hp3900-series/*
*http://jkdsoftware.dyndns.org/drupal/?q=es/books/151*

# AUTHOR

Jonathan Bravo Lopez \<*jkdsoft@gmail.com*\>

# BUGS

Scanning is only tested with Linux/ix86/gcc. Be careful when testing on other operating systems and especially on big-endian platforms. The scanner may get wrong data.
