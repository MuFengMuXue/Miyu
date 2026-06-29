# NAME

sane-avision - SANE backend for Avision branded and Avision OEM (HP, Minolta, Mitsubishi, UMAX and possibly more) flatbed and film scanners.

# DESCRIPTION

The **sane-avision** library implements a SANE (Scanner Access Now Easy) backend that provides access to various Avision scanners and the Avision OEM scanners labelled by HP, Minolta, Mitsubishi or Fujitsu.

It is fully big-endian aware and in everyday use on PowerPC and SPARC systems.

**I suggest you hold one hand on the power-button of the scanner while** **you try the first scans - especially with film-scanners!**

# CONFIGURATION

The configuration file for this backend resides in *@CONFIGDIR@/avision.conf*.

Its contents is a list of device names that correspond to Avision and Avision compatible scanners and backend-options. Empty lines and lines starting with a hash mark (#) are ignored. A sample configuration file is shown below:

     # this is a comment
     option force-a4
     option force-a3
     option skip-adf
     option disable-gamma-table
     option disable-calibration
     #scsi Vendor Model Type Bus Channel ID LUN
     scsi AVISION
     scsi HP
     scsi /dev/scanner
     usb 0x03f0 0x0701

force-a4:
Forces the backend to overwrite the scanable area returned by the scanner to ISO A4. Scanner that are known to return bogus data are marked in the backend so if you need this option please report this to the backend maintainer. USE WITH CARE!

force-a3:
Forces the backend to overwrite the scanable area returned by the scanner to ISO A3. Scanner that are known to return bogus data are marked in the backend so if you need this option please report this to the backend maintainer. USE WITH CARE!

skip-adf:
Forces the backend to ignore an inconsistent ADF status returned by the scanner (ADF not present, but ADF model number non-zero). Without this option, the backend will make several attempts to reset the ADF and retry the query in this situation, and will fail with a "not supported" error if the ADF still doesn't respond.

disable-gamma-table:
Disables the usage of the scanner's gamma-table. You might try this if your scans hang or only produce random garbage.

disable-calibration:
Disables the scanner's color calibration. You might try this if your scans hang or only produce random garbage.

Note:
Any option above modifies the default code-flow for your scanner. The options should only be used when you encounter problems with the default behavior of the backend. Please report the need of options to the backend-author so the backend can be fixed as soon as possible.

# DEVICE NAMES

This backend expects device names of the form:

> *scsi scsi-spec*
>
> *usb usb-spec*

Where *scsi-spec* is the path-name to a special device or a device ID for the device that corresponds to a SCSI scanner. The special device name must be a generic SCSI device or a symlink to such a device, for example on Linux */dev/sga* or */dev/sg0*. The device ID is the ID returned by the scanner, for example "HP" or "AVISION". See **sane-scsi**(5) for details.

Note:
Since the backend now includes native USB access, it is no longer needed - even considered obsolete - to access USB scanner via the SCSI emulation (named hpusbscsi on Linux) for Avision USB devices such as the HP 53xx, HP 74xx or Minolta film-scanners.

*usb-spec* is the USB device name, the vendor/product ID pair or the name used by libusb corresponding to the USB scanner. For example "0x03f0 0x0701" or "libusb:002:003". See **sane-usb**(5) for details.

The program **sane-find-scanner**(1) helps to find out the correct scsi or usb device name.

A list with supported devices is built into the avision backend so normally specifying an ID should not be necessary.

# FILES

*@CONFIGDIR@/avision.conf*
The backend configuration file (see also description of **SANE_CONFIG_DIR** below).

*@LIBDIR@/libsane-avision.a*
The static library implementing this backend.

*@LIBDIR@/libsane-avision.so*
The shared library implementing this backend (present on systems that support dynamic loading).

# ENVIRONMENT

**SANE_CONFIG_DIR**
This environment variable specifies the list of directories that may contain the configuration file. On \*NIX systems, the directories are separated by a colon (\`:'), under OS/2, they are separated by a semi-colon (\`;'). If this variable is not set, the configuration file is searched in two default directories: first, the current working directory (".") and then in *@CONFIGDIR@*. If the value of the environment variable ends with the directory separator character, then the default directories are searched after the explicitly specified directories. For example, setting **SANE_CONFIG_DIR** to "/tmp/config:" would result in directories *tmp/config*, *.*, and *@CONFIGDIR@* being searched (in this order).

**SANE_DEBUG_AVISION**
If the library was compiled with debug support enabled, this environment variable controls the debug level for this backend. Higher debug levels increase the verbosity of the output. The debug level 7 is the author's preferred value to debug backend problems.

Example: export SANE_DEBUG_AVISION=7

# SEE ALSO

**sane**(7), **sane-scsi**(5), **sane-usb**(5)
*http://exactcode.com/site/open_source/saneavision*

# MAINTAINER

René Rebe

# AUTHOR

René Rebe and Meino Christian Cramer
