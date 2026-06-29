# NAME

sane-lexmark - SANE backend for Lexmark X1100/X1200 Series scanners

# DESCRIPTION

The **sane-lexmark** library implements a SANE (Scanner Access Now Easy) backend that provides access to the scanner part of Lexmark X1100/X1200 AIOs. This backend should be considered **beta-quality** software!

The scanners that should work with this backend are:

>    Vendor Model           status
>     ----------------------  -----------
>       Lexmark X74             good
>       Lexmark X1110           untested
>       Lexmark X1140           untested
>       Lexmark X1150           good
>       Lexmark X1170           good
>       Lexmark X1180           good
>       Lexmark X1185           complete
>       Lexmark X12xx           good in USB1.1,
>                               not fully tested in USB2.0
>       Dell    A920            good

The options the backend supports can either be selected through command line options to programs like **scanimage**(1) or through GUI elements in **xscanimage**(1) or **xsane**(1).


If you notice any strange behavior, please report to the backend maintainer or to the SANE mailing list.

Valid command line options and their syntax can be listed by using

> scanimage --help -d lexmark:usb:\<usb port\>

**Scan Mode Options**
**--mode**
selects the basic mode of operation of the scanner. Valid choices are *Color*, *Gray* and *Lineart*. The default mode is *Color*. The *Lineart* mode is black and white only (1 bit). *Gray* mode will produce 256 levels of gray (8 bits). *Color* mode allows for over 16 million different colors produced from 24 bits of color information.


**--resolution**
selects the resolution for a scan. The horizontal and vertical resolutions are set by the value of this option. The scanner is capable of the following resolutions for the specified option value:

>   Value   Hor. Resolution  Vert. Resolution
>       -----   ---------------  -------------------
>       75      75dpi            75dpi
>       150     150dpi           150dpi
>       300     300dpi           300dpi
>       600     600dpi           600dpi
>       1200    600dpi           1200dpi  (only for X11xx models with 'B2' sensor)

**--preview**
requests a preview scan. The resolution used for that scan is 75 dpi and the scan area and the scan mode are as specified through their options, or the default if not specified. The default value for preview mode is "no".


**--threshold**
selects the minimum-brightness to get a white point. The threshold is only used with Lineart mode scans. It is specified as a percentage in the range 0..100% (in steps of 1). The default value of the threshold option is 50.

# CONFIGURATION FILE

The configuration file *@CONFIGDIR@/lexmark.conf* contains only the usb device id (eg usb 0x043d 0x007c).

# FILES

*@LIBDIR@/libsane-lexmark.a*
The static library implementing this backend.

*@LIBDIR@/libsane-lexmark.so*
The shared library implementing this backend (present on systems that support dynamic loading).

# ENVIRONMENT

**SANE_DEBUG_LEXMARK**
If the library was compiled with debug support enabled, this environment variable controls the debug level for this backend. E.g., a value of 255 requests all debug output to be printed. Smaller levels reduce verbosity.

**SANE_DEBUG_LEXMARK_LOW**
Provides debug output for low level Lexmark functions.

# LIMITATIONS

The windows TWAIN driver has many more options than this SANE backend. However they are only software adjustments. This backend only implements what the scanner can support. For instance, shading correction (vertical stripes due to sensor variation across its width) is done in software. Head park position is also detected by software. The data compression isn't supported for the X1200 series on USB 1.1, leading to slow scans.

# BUGS


No bugs currently known.

# SEE ALSO

**sane-scsi**(5), **scanimage**(1), **xscanimage**(1), **xsane**(1), **sane**(7)

# AUTHOR

The backend was originally written by Fred Odendaal.
*http://ca.geocities.com/freshshelf@rogers.com/*

The new version is currently developed by Stéphane Voltz.
*http://stef.dev.free.fr/sane/lexmark*

X74 support was written by Torsten Houwaart
\<*ToHo@gmx.de*\>

# CREDITS

Many thanks go to:
Julien Furgerot who lent me a Dell A920. Robert Price, Dani Ele and Dalai Felinto for the time they spent recording USB activity and testing the experimental version.
