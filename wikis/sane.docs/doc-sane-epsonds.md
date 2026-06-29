# NAME

sane-epsonds - SANE backend for EPSON ESC/I-2 scanners

# DESCRIPTION

The **sane-epsonds** library implements a SANE (Scanner Access Now Easy) backend that provides access to Epson ESC/I-2 scanners.

Valid command line options and their syntax can be listed by using

> scanimage --help -d epsonds

Not all devices support all options.

*Scan Mode*
The **--mode** switch selects the basic mode of operation of the scanner. Valid choices are Lineart, Gray and Color. The Lineart mode is black and white only, Gray will produce 256 levels of gray or more depending on the scanner and Color means 24 bit color mode or more depending on the scanner. Some scanners will internally use 36 bit color, their external interface however may only support 24 bits.

The **--depth** option selects the bit depth the scanner is using. This option is only available for scanners that support more than one bit depth. Older scanners will always transfer the image in 8bit mode. Newer scanners allow one to select either 8 bits, 12 or 14 bits per color channel. For a color scan this means an effective color depth of 36 or 42 bits over all three channels. The valid choices depend on the scanner model.

The **--resolution** switch selects the resolution for a scan. Some EPSON scanners will scan in any resolution between the lowest and highest possible value. The list reported by the scanner can be displayed using the "--help -d epson" parameters to **scanimage**(1).

The geometry options **-l -t -x -y** control the scan area: **-l** sets the top left x coordinate, **-t** the top left y coordinate, **-x** selects the width and **-y** the height of the scan area. All parameters are specified in millimeters.

The **--source** option selects the scan source. Valid options depend on the installed options. The default is "Flatbed".

The **--eject** option ejects the sheet in the ADF.

The **--adf-mode** option select the ADF mode (simplex/duplex).

# SENSORS

Some scanners (e.g. ES-60W) have a hardware scan button. The button state can be polled via the **--scan** option, which returns 1 when the button is pressed and 0 otherwise. This is useful for scanning applications that want to trigger a scan when the user presses the button on the device.

# CONFIGURATION FILE

The configuration file *@CONFIGDIR@/epsonds.conf* specifies the device(s) that the backend will use. Possible connection types are:

**USB**
For not automatically detected USB scanners, their VENDOR and PRODUCT ID can be specified manually in the config file. More information about valid syntax for USB devices can be found in **sane-usb**(5).

**Network (not yet supported)**
Network scanners can be auto-discovered if **autodiscovery** is specified after **net** keyword. An IP address to connect to can also be used.

# FILES

*@LIBDIR@/libsane-epsonds.a*
The static library implementing this backend.

*@LIBDIR@/libsane-epsonds.so*
The shared library implementing this backend (present on systems that support dynamic loading).

# ENVIRONMENT

**SANE_DEBUG_EPSONDS**
If the library was compiled with debug support enabled, this environment variable controls the debug level for this backend. E.g., a value of 128 requests all debug output to be printed. Smaller levels reduce verbosity. Values around 11-16 will usually be enough for a bug report.

# SEE ALSO

**sane-usb**(5), **scanimage**(1), **xscanimage**(1), **xsane**(1)

# AUTHOR

The backend is written by Alessandro Zummo.
