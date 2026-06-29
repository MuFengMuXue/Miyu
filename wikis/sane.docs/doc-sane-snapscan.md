# NAME

sane-snapscan - SANE backend for AGFA SnapScan flatbed scanners

# DESCRIPTION

The **sane-snapscan** library implements a SANE (Scanner Access Now Easy) backend that provides access to AGFA SnapScan flatbed scanners. At present, the following scanners are supported from this backend: AGFA SnapScan 300, 310, 600, and 1236s, 1236u, 1212u, e20, e25, e40, e50, e60, Vuego 310s, Acer 300f, 310s, 610s, 610plus, Prisa 620s, Prisa 620u, Prisa 620ut, Prisa 640u, Prisa 640bu, Prisa 1240, Prisa 3300, Prisa 4300, Prisa 5300 and Guillemot Maxi Scan A4 Deluxe (SCSI) (with varying success).

# DEVICE NAMES

This backend expects device names of the form:

> *special*

Where *special* is the path-name for the special device that corresponds to a SCSI scanner. For SCSI scanners, the special device name must be a generic SCSI device or a symlink to such a device. Under Linux, such a device name could be */dev/sga* or */dev/sge*, for example. See **sane-scsi**(5) for details.

For USB scanners the devicename must contain the keyword "usb", as in */dev/usbscanner* or */dev/usb/scanner0*. For scanners that need a firmware upload before scanning add a line starting with "firmware" followed by the fully qualified path to your firmware file, e.g.

> firmware @DATADIR@/sane/snapscan/firmware.bin

For further details read *http://snapscan.sourceforge.net*.

# CONFIGURATION

The contents of the *snapscan.conf* file is a list of device names that correspond to SnapScan scanners. Empty lines and lines starting with a hash mark (#) are ignored. See **sane-scsi**(5) on details of what constitutes a valid device name.

# FILES

*@CONFIGDIR@/snapscan.conf*
The backend configuration file (see also description of **SANE_CONFIG_DIR** below).

*@LIBDIR@/libsane-snapscan.a*
The static library implementing this backend.

*@LIBDIR@/libsane-snapscan.so*
The shared library implementing this backend (present on systems that support dynamic loading).

# ENVIRONMENT

**SANE_CONFIG_DIR**
This environment variable specifies the list of directories that may contain the configuration file. On \*NIX systems, the directories are separated by a colon (\`:'), under OS/2, they are separated by a semi-colon (\`;'). If this variable is not set, the configuration file is searched in two default directories: first, the current working directory (".") and then in *@CONFIGDIR@*. If the value of the environment variable ends with the directory separator character, then the default directories are searched after the explicitly specified directories. For example, setting **SANE_CONFIG_DIR** to "/tmp/config:" would result in directories *tmp/config*, *.*, and *@CONFIGDIR@* being searched (in this order).

**SANE_DEBUG_SNAPSCAN**
If the library was compiled with debug support enabled, this environment variable controls the debug level for this backend. E.g., a value of 255 requests all debug output to be printed. Smaller levels reduce verbosity.

# BUGS

Man page doesn't provide much information yet.

# SEE ALSO

**sane**(7), **sane-scsi**(5),
*http://sourceforge.net/projects/snapscan/* (new development website)

# AUTHOR

Kevin Charter, Franck Schneider, Michel Roelofs, Emmanuel Blot, Mikko Tyolajarvi, David Mosberger-Tang, Wolfgang Goeller, Petter Reinholdtsen, Gary Plewa, Sebastien Sable, Oliver Schwartz and Mikael Magnusson.
Man page by Henning Meier-Geinitz (mostly based on the web pages and source code).
