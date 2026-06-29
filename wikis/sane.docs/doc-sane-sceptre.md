# NAME

sane-sceptre - SANE backend for SCEPTRE scanners

# DESCRIPTION

The **sane-sceptre** library implements a SANE (Scanner Access Now Easy) backend that provides access to Sceptre flatbed scanners. This backend should be considered **beta-quality** software! Please report any strange behavior to the maintainer of the backend or to the SANE mailing list.

At present, only one scanner is known to work with this backend:

> Model                        Connection Type
>     ---------------------------  -------------------
>     Sceptre VividScan S1200      SCSI

The make of this scanner is KINPO, so other scanners from that manufacturer may also work (eg. the S600).

# OPTIONS

The options the backend supports can either be selected through command line options to programs like **scanimage**(1) or through GUI elements in **xscanimage**(1) or **xsane**(1).

Valid command line options and their syntax can be listed by using

> scanimage --help -d sceptre

**Scan Mode**
**--mode Lineart\|Halftone\|Gray\|Color**
Selects the basic mode of operation of the scanner. The *Lineart* and *Halftone* mode are black and white only (1 bit). *Gray* will produce 256 levels of gray (8 bits). *Color* will produce a 24 bits color image. The scanner supports 30 bits internally but it only exports 24.


**--resolution 50..1200**
Selects the resolution for a scan. The scanner can do several resolutions between 50 and 1200.


**--halftone-pattern 1\|2\|3\|4**
Selects the pattern mode that is used in *Halftone* mode.


**--gamma-correction Default\|User Defined\|High Density Printing\|Low density printing\|High contrast printing**
controls the scanner internal gamma correction.


**--custom-gamma**
Allows the user to specify a gamma table (see the next 3 parameters). *Color* mode only.


**--red-gamma-table**
Can be used to download a user defined gamma table for the red channel. The table must be 256 bytes long. *Color* mode only.


**--green-gamma-table**
Can be used to download a user defined gamma table for the green channel. The table must be 256 bytes long. *Color* mode only.


**--blue-gamma-table**
Can be used to download a user defined gamma table for the blue channel. The table must be 256 bytes long. *Color* mode only.


**--threshold 0..255**
Sets the threshold for black and white pixels in *Lineart* mode. Possible values are from 0 (darker) to 255 (lighter).


**--preview**
Requests a preview scan. The resolution used for that scan is 30 dpi and the scan area is the maximum allowed. The scan mode is user selected. The default is "no".


**The geometry options**
**-l -t -x -y**
control the scan area: **-l** sets the top left x coordinate, **-t** the top left y coordinate, **-x** selects the width and **-y** the height of the scan area. All parameters are specified in millimeters by default.

# CONFIGURATION FILE

The configuration file *@CONFIGDIR@/sceptre.conf* supports only one item: the device name to use (eg */dev/scanner*).

# FILES

*@LIBDIR@/libsane-sceptre.a*
The static library implementing this backend.

*@LIBDIR@/libsane-sceptre.so*
The shared library implementing this backend (present on systems that support dynamic loading).

# ENVIRONMENT

**SANE_DEBUG_SCEPTRE**
If the library was compiled with debug support enabled, this environment variable controls the debug level for this backend. E.g., a value of 128 requests all debug output to be printed. Smaller levels reduce verbosity.

# LIMITATIONS

**Resolutions**
The windows TWAIN driver can be set to any resolution between 50 to 1200 (excluding software interpolation). This backend cannot. Only a handful of resolution are available, although they should be numerous enough.

# BUGS

None known.

# SEE ALSO

**sane-scsi**(5), **scanimage**(1), **xscanimage**(1), **xsane**(1), **sane**(7)

# AUTHOR

The package is actively maintained by Frank Zago.
*http://www.zago.net/sane/#sceptre*
