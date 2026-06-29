# NAME

sane-rts8891 - SANE backend for rts8891 based scanners

# DESCRIPTION

The **sane-rts8891** library implements a SANE (Scanner Access Now Easy) backend that provides access to scanners based on the rts8891 ASIC.

The scanners that work with this backend are:

>    Vendor Model           status
>     ----------------------  -----------
>       Umax Astra 4400       untested
>       Umax Astra 4450       untested
>       HP scanjet 4000c      good
>       HP scanjet 4470c      good

The options the backend supports can either be selected through command line options to programs like **scanimage**(1) or through GUI elements in **xscanimage**(1) or **xsane**(1).


If you notice any strange behavior, please report to the backend maintainer or to the SANE mailing list.

Valid command line options and their syntax can be listed by using

> scanimage --help -d rts8891

**Scan Mode Options**
**--mode**
selects the basic mode of operation of the scanner. Valid choices are *Color*, *Gray* and *Lineart*. The default mode is *Color*. The *Lineart* mode is for black and white only (1 bit). *Gray* will produce 256 levels of gray (8 bits). *Color* mode allows for over 16 million different colors produced from 24 bits of color information.


**--resolution**
selects the resolution for a scan. The horizontal and vertical resolutions are set by the value of this option. The scanner is capable of the following resolutions for the specified option value:

>   Value   Hor. Resolution  Vert. Resolution
>       -----   ---------------  -------------------
>       75      75dpi            75dpi
>       150     150dpi           150dpi
>       300     300dpi           300dpi
>       600     600dpi           600dpi
>       1200    1200dpi          1200dpi

**--preview**
requests a preview scan. The resolution used for that scan is 75 dpi and the scan area and the scan mode are as specified through their options, or the default if not specified. The default value for preview mode is "no".


**--threshold**
selects the minimum-brightness to get a white point. The threshold is only used with Lineart mode scans. It is specified as a percentage in the range 0..100% (in steps of 1). The default value of the threshold option is 50.

# CONFIGURATION FILE

The configuration file *@CONFIGDIR@/rts8891.conf* contains the usb device ids of supported scanners (eg usb 0x043d 0x007c) and scanner configuration options. Empty lines and lines starting with a hash mark (#) are ignored.

The options supported are **allowsharing**, **modelnumber**

Option

**allowsharing**
enables or not the sharing of the scanner between multiple frontends at the same time.

**modelnumber**
is used to force the reported model by the backend and is only useful in the case of a scanner which NVRAM has been erased.

> 0 to report a HP4470c.
>     1 to report a HP4400c.
>     2 to report an Astra 4400.

# FILES

*@LIBDIR@/libsane-rts8891.a*
The static library implementing this backend.

*@LIBDIR@/libsane-rts8891.so*
The shared library implementing this backend (present on systems that support dynamic loading).

# ENVIRONMENT

**SANE_DEBUG_RTS8891 SANE_DEBUG_RTS8891_LOW SANE_DEBUG_RTS88XX_LIB**
If the library was compiled with debug support enabled, these environment variables control the debug level for this backend. E.g., a value of 255 requests all debug output to be printed. Smaller levels reduce verbosity.

# LIMITATIONS

Scanners of the same model exist with different sensors, due to lack of data (ie USB logs) some sensors are better supported than others. At least 75 dpi mode is working for any model. Sharing the scanner between several frontends at the same time (allowsharing option) may not work on some USB controllers.

XPA is not (yet) supported.

# BUGS


No bugs currently known.

# SEE ALSO

**sane-scsi**(5), **scanimage**(1), **xscanimage**(1), **xsane**(1), **sane**(7)

# AUTHOR

This backend has been developed by Stéphane Voltz.
*http://stef.dev.free.fr/sane/rts8891*

# CREDITS

Many thanks go to:
Laurent Fournier who donated me a HP4470c. Vladimir Sysoev and "TheUnruly Squash" for the time they spent recording USB activity and testing the experimental version on HP4400 models.
