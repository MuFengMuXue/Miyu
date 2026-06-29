# NAME

sane-teco1 - SANE backend for TECO / RELISYS scanners

# DESCRIPTION

The **sane-teco1** library implements a SANE (Scanner Access Now Easy) backend that provides access to some TECO SCSI flatbed scanners. This backend should be considered **beta-quality** software! TECO scanners are sold under various brands like RELISYS, PIOTECH, TRUST. This backend may or may not support yours.

The scanners that should work with this backend are:

>    Vendor Model           TECO model      status
>     ----------------------  --------------  -----------
>       Relisys AVEC 2400        VM3520        tested
>       Relisys AVEC 2412        VM3520+       tested
>       Relisys AVEC 4800        VM4530        untested
>       Relisys AVEC 4816        VM4530+       untested
>       Relisys RELI 2400        VM3530        untested
>       Relisys RELI 2412        VM3530+       tested
>       Relisys RELI 2412        VM3530+       untested
>       Relisys RELI 4816        VM4540        tested
>       Relisys RELI 4830        VM4542        tested
>       Relisys RELI 9600        VM6530        untested
>       Relisys RELI 9612        VM6530*       untested
>       Relisys RELI 9624        VM6530+       untested
>       Relisys RELI 9630        VM6540        untested
>       Relisys RELI DS15        VM3440        untested
>       Relisys RELI DS6         VM3420        untested
>       Dextra  DF-600P          VM3510        tested
>       Dextra  DF-4830T         VM4542        untested
>       Dextra  DF-1200T+        VM3530+       untested
>       Dextra  DF-9624          VM6530+       untested

Note that the untested scanner will not be directly supported. You should contact the author for that.

The TECO VM number can usually be found at the back of the scanner. It is also part of the FCC ID. *sane-find-scanner -v* will also show the SCSI inquiry, and if it is a TECO scanner, the name will be there too.

The options the backend supports can either be selected through command line options to programs like **scanimage**(1) or through GUI elements in **xscanimage**(1) or **xsane**(1).


If you have any success with a scanner not listed here, or if you notice any strange behavior, please report to the backend maintainer or to the SANE mailing list.

Valid command line options and their syntax can be listed by using:

> scanimage --help -d teco1

**Scan Mode**
**--mode Black & White\|Grayscale\|Color**
Selects the basic mode of operation of the scanner. Valid choices are *Black & White*, *Grayscale* and *Color*.

The *Black & White* mode is for black and white only (1 bit). *Grayscale* will produce 256 levels of gray (8 bits). *Color* will produce a 24 bit color image.


**--resolution 1..600**
Selects the resolution for a scan. The scanner can do all resolutions between 1 and 600, in increments of 1.


**Geometry options**
**-l -t -x -y**
Controls the scan area: **-l** sets the top left x coordinate, **-t** the top left y coordinate, **-x** selects the width and **-y** the height of the scan area. All parameters are specified in millimeters by default.


**Enhancement options**
**--custom-gamma**
(color mode only) allows the user to specify a gamma table (see the next 3 parameters).


**--red-gamma-table**
Can be used to download a user defined gamma table for the red channel. The table must be 256 bytes long. Color mode only.


**--green-gamma-table**
Can be used to download a user defined gamma table for the green channel. The table must be 256 bytes long. Color mode only.


**--blue-gamma-table**
Can be used to download a user defined gamma table for the blue channel. The table must be 256 bytes long. Color mode only.


**--dither Line art\|2x2\|3x3\|4x4 bayer\|4x4 smooth\|8x8 bayer\|8x8 smooth\|8x8 horizontal\|8x8 vertical**
Select the dither mask to use. Black & White only.


**--preview**
Requests a preview scan. The resolution used is 22 dpi and the scan area is the maximum allowed. The scan mode is user selected. The default is "no".

# CONFIGURATION FILE

The configuration file *@CONFIGDIR@/teco1.conf* supports only one item: the device name to use (eg */dev/scanner*).

# FILES

*@LIBDIR@/libsane-teco1.a*
The static library implementing this backend.

*@LIBDIR@/libsane-teco1.so*
The shared library implementing this backend (present on systems that support dynamic loading).

# ENVIRONMENT

**SANE_DEBUG_TECO1**
If the library was compiled with debug support enabled, this environment variable controls the debug level for this backend. E.g., a value of 128 requests all debug output to be printed. Smaller levels reduce verbosity.

# LIMITATIONS

The windows TWAIN driver has many more options than this SANE backend. However they are only software adjustments. This backend only implements what the scanner can support.

# BUGS

None known.

# SEE ALSO

**sane-scsi**(5), **scanimage**(1), **xscanimage**(1), **xsane**(1), **sane**(7)

# AUTHOR

The package is actively maintained by Frank Zago.
*http://www.zago.net/sane/#teco*

# CREDITS

Thanks to Gerard Delafond for the VM4542 support. Thanks to Jean-Yves Simon for the VM3510 support.
