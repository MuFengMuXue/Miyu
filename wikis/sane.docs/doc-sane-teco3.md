# NAME

sane-teco3 - SANE backend for TECO / RELISYS scanners

# DESCRIPTION

The **sane-teco3** library implements a SANE (Scanner Access Now Easy) backend that provides access to some TECO SCSI flatbed scanners. This backend should be considered **alpha-quality** software! TECO scanners are sold under various brands like RELYSIS, PIOTECH, TRUST. This backend may or may not support yours.

The scanners that should work with this backend are:

>   Vendor Model                 TECO model   status
>       ---------------------------  ----------  ----------
>       Relisys Scorpio                VM3552     tested
>       Plustek OpticPro 2400SP        VM3552     untested
>       PIOTECH Splendeur 3024         VM3552     tested
>       Trust Imagery 2400 SP          VM3552     tested
>       Trust Imagery 4800 SP+         VM3552     tested
>       Trust Imagery 9600 SP          VM3552     untested

The TECO VM number can usually be found at the back of the scanner. It is also part of the FCC ID.

The options the backend supports can either be selected through command line options to programs like **scanimage**(1) or through GUI elements in **xscanimage**(1) or **xsane**(1).


If you have any success with a scanner not listed here, or if you notice any strange behavior, please report to the backend maintainer or to the SANE mailing list.

# OPTIONS

Valid command line options and their syntax can be listed by using:

> scanimage --help -d teco3

**Scan Mode**
**--mode Black & White\|Grayscale\|Color**
Selects the basic mode of operation of the scanner. The *Black & White* mode is black and white only (1 bit). *Grayscale* will produce 256 levels of gray (8 bits). *Color* will produce a 24-bit color image.


**--resolution 1..1200**
Selects the resolution for a scan. The scanner can do all resolutions between 1 and 1200, in increments of 1.


**--preview**
Requests a preview scan. The resolution used for that scan is 22 dpi and the scan area is the maximum allowed. The scan mode is user selected. The default is "no".


**Geometry options**
**-l -t -x -y**
Control the scan area: **-l** sets the top left x coordinate, **-t** the top left y coordinate, **-x** selects the width and **-y** the height of the scan area. All parameters are specified in millimeters by default.

# OPTIONS FOR COLOR MODE ONLY

**--custom-gamma**
Allows the user to specify a gamma table (see the next 3 parameters).


**--red-gamma-table**
Can be used to download a user defined gamma table for the red channel. The table must be 1024 bytes long.


**--green-gamma-table**
Can be used to download a user defined gamma table for the green channel. The table must be 1024 bytes long.


**--blue-gamma-table**
Can be used to download a user defined gamma table for the blue channel. The table must be 1024 bytes long.

# CONFIGURATION FILE

The configuration file *@CONFIGDIR@/teco3.conf* supports only one item: the device name to use (eg */dev/scanner*).

# FILES

*@LIBDIR@/libsane-teco3.a*
The static library implementing this backend.

*@LIBDIR@/libsane-teco3.so*
The shared library implementing this backend (present on systems that support dynamic loading).

# ENVIRONMENT

**SANE_DEBUG_TECO3**
If the library was compiled with debug support enabled, this environment variable controls the debug level for this backend. E.g., a value of 128 requests all debug output to be printed. Smaller levels reduce verbosity.

# LIMITATIONS

The windows TWAIN driver has many more options than this SANE backend. However they are only software adjustments. This backend only implements what the scanner can support.

# BUGS

Not much.

# SEE ALSO

**sane-scsi**(5), **scanimage**(1), **xscanimage**(1), **xsane**(1), **sane**(7)

# AUTHOR

The package is actively maintained by Frank Zago.
*http://www.zago.net/sane/#teco3*
