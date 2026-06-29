# NAME

sane-mustek_usb - SANE backend for Mustek USB flatbed scanners

# DESCRIPTION

The **sane-mustek_usb** library implements a SANE (Scanner Access Now Easy) backend that provides access to Mustek USB flatbed scanners (including a clone from Trust). At present, the following scanners are known to work more or less with this backend:

> Mustek 600 CU
> Mustek 1200 UB
> Mustek 1200 CU
> Mustek 1200 CU Plus
> Trust Compact Scan USB 19200

More details can be found on the Mustek USB backend homepage *http://www.meier-geinitz.de/sane/mustek_usb-backend/*.

The Mustek BearPaw 1200 and 2400 scanners are supported by the plustek backend. See **sane-plustek**(5) for details. The Mustek BearPaw 1200F is supported by the MA-1509 backend. See **sane-ma1509**(5) for details. Other Mustek USB scanners are supported by the gt68xx backend, see **sane-gt68xx**(5).

This backend can only work with scanners that are already detected by the operating system. See **sane-usb**(5) for details.

If you own a Mustek (or Trust) scanner other than the ones listed above that works with this backend, please let me know this by sending the scanner's exact model name and the USB vendor and device ids (e.g. from */proc/bus/usb/devices* or syslog) to me.

# DEVICE NAMES

This backend expects device names of the form:

> *special*

Where *special* is a path-name for the special device that corresponds to a USB scanner. With Linux, such a device name could be */dev/usb/scanner0* or */dev/usbscanner1*, for example.

For FreeBSD use */dev/uscanner0*.

# CONFIGURATION

The contents of the *mustek_usb.conf* file is a list of options and device names that correspond to Mustek USB scanners. Empty lines and lines starting with a hash mark (#) are ignored. If a device name is placed in *mustek_usb.conf*, it must be followed by a line containing the keyword **option** and an option specifying the scanner type. The following options can be used: **600cu**, **1200cu**, **1200cu_plus**, **1200ub**. For the Trust Compact Scan USB 19200 use \`option 1200ub'.

Instead of using the device name, the scanner can be autodetected by **usb vendor_id product_id** statements which are already included into *mustek_usb.conf*. This is only supported with Linux 2.4.8 and higher and all systems that support libusb. "vendor_id" and "product_id" are hexadecimal numbers that identify the scanner. If this doesn't work, a device name and the option specifying the scanner type must be placed in *mustek_usb.conf* as described above.

The global **option max_block_size** can be used to limit the amount of data acquired in one turn from the USB system. It may be worth trying, if USB errors occur.

A sample configuration file is shown below:

> \# Comment
> option max_block_size 1024
> usb 0x055f 0x0001
> /dev/usb/scanner0
> option 600cu

The first line is ignored. The second line sets the buffer size to a maximum of 1024 bytes. The third line tries to autodetect a scanner with vendor id 0x055f and product id 0x0001 (Mustek 1200 CU). The fourth line tells the backend to attach to */dev/usb/scanner0* and the fifth line specifies that */dev/usb/scanner0* is a Mustek 600 CU.

# FILES

*@CONFIGDIR@/mustek_usb.conf*
The backend configuration file (see also description of **SANE_CONFIG_DIR** below).

*@LIBDIR@/libsane-mustek_usb.a*
The static library implementing this backend.

*@LIBDIR@/libsane-mustek_usb.so*
The shared library implementing this backend (present on systems that support dynamic loading).

# ENVIRONMENT

**SANE_CONFIG_DIR**
This environment variable specifies the list of directories that may contain the configuration file. On \*NIX systems, the directories are separated by a colon (\`:'), under OS/2, they are separated by a semi-colon (\`;'). If this variable is not set, the configuration file is searched in two default directories: first, the current working directory (".") and then in *@CONFIGDIR@*. If the value of the environment variable ends with the directory separator character, then the default directories are searched after the explicitly specified directories. For example, setting **SANE_CONFIG_DIR** to "/tmp/config:" would result in directories *tmp/config*, *.*, and *@CONFIGDIR@* being searched (in this order).

**SANE_DEBUG_MUSTEK_USB**
If the library was compiled with debug support enabled, this environment variable controls the debug level for this backend. Higher debug levels increase the verbosity of the output.


    Value  Description
    0      no output
    1      print fatal errors
    2      print important messages
    3      print non-fatal errors and less important messages
    4      print all but debugging messages
    5      print high level debugging messages
    6      print medium level debugging messages
    7      print low level debugging messages

Example: export SANE_DEBUG_MUSTEK_USB=4

# SEE ALSO

**sane**(7), **sane-usb**(5), **sane-mustek**(5), **sane-mustek_pp**(5), **sane-plustek**(5), **sane-gt68xx**(5), **sane-ma1509**(5)
*@DOCDIR@/mustek_usb/mustek_usb.CHANGES*,
*@DOCDIR@/mustek_usb/mustek_usb.TODO*
*http://www.meier-geinitz.de/sane/mustek_usb-backend/*

# AUTHOR

Henning Meier-Geinitz \<*henning@meier-geinitz.de*\>
This backend is based on the Mustek 1200ub backend from Mustek, maintained by Tom Wang.

# BUGS

These devices have a hardware bug: Once data is written to them, they can't be reset (toggle = DATA0). That means, any operation that tries to reset the device will result in running into timeouts.

In earlier versions this backend failed when it was loaded the second time in some configurations. The only choice was to replug the scanner in this case. The backend uses a workaround for that bug now but it's only tested on Linux. Reports for other operating systems are appreciated.

More detailed bug information is available at the Mustek backend homepage *http://www.meier-geinitz.de/sane/mustek_usb-backend/*.
