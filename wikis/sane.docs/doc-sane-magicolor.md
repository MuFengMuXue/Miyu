# NAME

sane-magicolor - SANE backend for KONICA MINOLTA magicolor and Toshiba TEC e-STUDIO scanners

# DESCRIPTION

The **sane-magicolor** backend supports KONICA MINOLTA magicolor and Toshiba TEC e-STUDIO scanners connected via USB or LAN.

# SUPPORTED DEVICES

The following scanner should work with this backend:

Device Details
-----------------------------
Vendor: KONICA MINOLTA
Model: magicolor 1690MF
Vendor: Toshiba TEC
Model: e-STUDIO2323AM

# CONFIGURATION

This section describes the backend's configuration file entries. The file is located at:

> *@CONFIGDIR@/magicolor.conf*

For a proper setup, at least one of the following entries are needed:

> *net autodiscovery*
> *net \[IP ADDRESS\] \[DEVICE-ID\]*
> *usb*
> *usb \[VENDOR-ID\] \[DEVICE-ID\]*

# FILES

*@CONFIGDIR@/magicolor.conf*
The backend configuration file

*@LIBDIR@/libsane-magicolor.a*
The static library implementing this backend.

*@LIBDIR@/libsane-magicolor.so*
The shared library implementing this backend (present on systems that support dynamic loading).

# ENVIRONMENT

**SANE_CONFIG_DIR**
This environment variable specifies the list of directories that may contain the configuration file. On \*NIX systems, the directories are separated by a colon (\`:'), under OS/2, they are separated by a semi-colon (\`;'). If this variable is not set, the configuration file is searched in two default directories: first, the current working directory (".") and then in *@CONFIGDIR@*. If the value of the environment variable ends with the directory separator character, then the default directories are searched after the explicitly specified directories. For example, setting **SANE_CONFIG_DIR** to "/tmp/config:" would result in directories */tmp/config*, *.*, and *@CONFIGDIR@* being searched (in this order).

**SANE_DEBUG_MAGICOLOR**
If the library was compiled with debug support enabled, this environment variable controls the debug level for this backend. Higher debug levels increase the verbosity of the output.

Example: export SANE_DEBUG_MAGICOLOR=127

To obtain debug messages from the backend, set this environment variable before calling your favorite frontend (e.g. **xscanimage**(1)).

Example: SANE_DEBUG_MAGICOLOR=65 xscanimage

# KNOWN BUGS AND RESTRICTIONS

Large color scans may sometimes timeout due to unknown reasons (the scanner simply stops returning data).

Cancelling large scans may lock up the scanner.

# SEE ALSO

**sane**(7),
*http://wiki.kainhofer.com/hardware/magicolor_scan*

# AUTHOR

Reinhold Kainhofer \<*reinhold@kainhofer.com*\>
