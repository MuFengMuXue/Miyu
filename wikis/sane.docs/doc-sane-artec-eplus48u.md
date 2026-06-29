# NAME

sane-artec_eplus48u - SANE backend for the scanner Artec E+ 48U and re-badged models

# DESCRIPTION

The **sane-artec_eplus48u** library implements a SANE (Scanner Access Now Easy) backend that provides access to several USB flatbed scanners using the GT6816 chipset like the Artec E+ 48U. These scanners have a contact image sensor (CIS).

A complete list of supported devices can be found on *http://www.sane-project.org/sane-supported-devices.html*.

This is ALPHA software. Especially if you test new or untested scanners, keep your hand at the scanner's plug and unplug it, if the head bumps at the end of the scan area.

If you own a scanner other than the ones mentioned on the list that works with this backend, please let us know this by sending the scanner's exact model name and the USB vendor and product ids (e.g. from */proc/bus/usb/devices*, **sane-find-scanner**(1) or syslog) to me. Even if the scanner's name is only slightly different from the models mentioned above, please let me know.

# KERNEL ISSUES

If libusb-0.1.6 or later is installed, this section can be skipped. The scanner should be found by **sane-find-scanner**(1) without further actions. For setting permissions and general USB information look at **sane-usb**(5).

When you are using the scanner module, a Linux kernel 2.4.12 or newer is required.

# FIRMWARE FILE

You need a firmware file for your scanner. That's a small file containing software that will be uploaded to the scanner's memory. For the scanners mentioned above, it's usually named *Artec48.usb* or *1200.usb*. You can find it on the installation CD that was provided by the manufacturer, normally in the directory Win98, WinMe or similar. If the Windows-driver is installed on your computer, then you can also find the firmware file under *c:\windows\system32\drivers*.

# CONFIGURATION

The contents of the *artec_eplus48u.conf* file is a list of *usb* lines containing vendor and product ids that correspond to USB scanners. The file can also contain option lines. Empty lines and lines starting with a hash mark (#) are ignored. The scanners are autodetected by *usb vendor_id product_id* statements which are already included into *artec_eplus48u.conf .* "vendor_id" and "product_id" are hexadecimal numbers that identify the scanner.

Every *usb* section can have additional options.

**artecFirmwareFile @DATADIR@/sane/artec_eplus48u/Artec48.usb**
The path to the firmware file. This option is required.

**redGamma 1.0**
**greenGamma 1.0**
**blueGamma 1.0**
**masterGamma 1.9**
These are the default gamma values. If you set the "Defaults" option with a frontend, then the gamma options are reset to the values specified here.

**redOffset 0x28**
**greenOffset 0x2f**
**blueOffset 0x2f**
**redExposure 0xa7**
**greenExposure 0x116**
**blueExposure 0xdc**
These are the default values for offset and exposure time. You can change them (e.g. to speed up calibration) if you don't want to save the calibration data permanently.

**vendorString Artec**
**modelString E+ 48U**
By default, the scanner is reported as "Artec E+ 48U". If you don't like this, e.g. because you have an Tevion MD 9693, then change the options accordingly.

# FILES

*/usr/local/etc/sane.d/artec_eplus48u.conf*
The backend configuration file (see also description of **SANE_CONFIG_DIR** below).

*/usr/local/lib/sane/libsane-artec_eplus48u.a*
The static library implementing this backend.

*/usr/local/lib/sane/libsane-artec_eplus48u.so*
The shared library implementing this backend (present on systems that support dynamic loading).

# ENVIRONMENT

**SANE_CONFIG_DIR**
This environment variable specifies the list of directories that may contain the configuration file. On \*NIX systems, the directories are separated by a colon (\`:'), under OS/2, they are separated by a semi-colon (\`;'). If this variable is not set, the configuration file is searched in two default directories: first, the current working directory (".") and then in *@CONFIGDIR@*. If the value of the environment variable ends with the directory separator character, then the default directories are searched after the explicitly specified directories. For example, setting **SANE_CONFIG_DIR** to "/tmp/config:" would result in directories *tmp/config*, *.*, and *@CONFIGDIR@* being searched (in this order).

**SANE_DEBUG_ARTEC_EPLUS48U**
If the library was compiled with debug support enabled, this environment variable controls the debug level for this backend. Higher debug levels increase the verbosity of the output.

Example: export SANE_DEBUG_ARTEC_EPLUS48U=3

# SEE ALSO

**sane**(7), **sane-usb**(5)

# AUTHOR

Michael Herder.
This backend is based on the gt68xx test-program written by Sergey Vlasov, Andreas Nowack, and David Stevenson. Thanks to everyone who tested the backend or reported bugs.
This man page is based on man **sane-gt68xx**(5), written by Henning Meier-Geinitz.

# BUGS

This backend has been tested on Linux only. If you are using it on a different platform, please contact us.

Interpolation with 1200 dpi is weak.

Support for buttons is missing due to missing support in SANE.

Please contact us if you find a bug: *http://www.sane-project.org/bugs.html*.
