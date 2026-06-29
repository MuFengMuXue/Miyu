# NAME

sane-stv680 - SANE backend for STV680 camera's

# DESCRIPTION

The **sane-stv680** library implements a SANE (Scanner Access Now Easy) backend that provides access to some STV680 cameras. This backend should be considered **beta-quality** software! STV680 cameras are sold under various brands like Aiptek. This backend may or may not support yours.

The cameras that should work with this backend are:

    Vendor Model              USB vendor id  USB product id  status
    ------------------------  -------------  --------------  --------
    AIPTEK stv680                0x0553         0x0202       basic
    Konica e-mini                0x04c8         0x0722       untested
    DigitalDream l'espion XS     0x1183         0x0001       untested
    Creative WebCam Go mini      0x041e         0x4007       untested

For all these cameras, see the backend home page (under AUTHOR) for the exact status of each camera.

For startup of this backend check that if present the stv680 kernel module is removed or disabled.
Also before using, enable the backend by editing the *@CONFIGDIR@/dll.conf* file, change \#stv680 to stv680.

For problems with the untested cameras, you should contact the author for that.

The options the backend supports can either be selected through command line options to programs like **scanimage**(1) or through GUI elements in **xcam**(1). For both programs use the **-B** option needed for size buffer.

Some frontends examples:


**xcam**(1)

> xcam -B

**scanimage**(1): for writing in batch mode to a file or to a new file each time:

> scanimage -B -d stv680:libusb:001:002 --batch=out.ppm --batch-count 5 --mode "Color RGB"

> scanimage -B -d stv680:libusb:001:002 --batch=out%d.ppm --batch-count 5 --mode "Color RGB"


If you have any success with a camera not listed here, or if you observe any strange behavior, please report to the backend maintainer or to the SANE mailing list.

Valid command line options and their syntax can be listed by using:

> scanimage --help -d stv680

**Scan Mode**
**--mode**
selects the basic mode of operation of the webcam's valid choices.

The read resolution mode is 8 bits, output resolution is 24 bits. Selects the resolution for a scan. The camera can do only the resolutions listed.

**--Raw**
In this mode raw data is displayed

**--Color**
In this mode the bayer unshuffle is done but no color correction

**--Color_RGB**
Bayer unshuffle, color correction

**--Color_RGB_TXT**
Bayer unshuffle, color correction, textline with date and time is added


**Enhancement options**
**--white-level-r -32..+32**
Selects what red radiance level should be considered "white", when scanning some sheets by changing the calibration value loaded into the scanner. Scale -32 .. 0 .. +32 in steps of 1.


**--white-level-g -32..+32**
Selects what green radiance level should be considered "white", when scanning some sheets by changing the calibration value loaded into the scanner. Scale -32 .. 0 .. +32 in steps of 1.


**--white-level-b -32..+32**
Selects what blue radiance level should be considered "white", when scanning some sheets by changing the calibration value loaded into the scanner. Scale -32 .. 0 .. +32 in steps of 1.

# CONFIGURATION FILE

The configuration file *@CONFIGDIR@/stv680.conf* supports only one item: the device name to use (eg usb 0x.... 0x....).

# FILES

*@LIBDIR@/libsane-stv680.a*
The static library implementing this backend.

*@LIBDIR@/libsane-stv680.so*
The shared library implementing this backend (present on systems that support dynamic loading).

# ENVIRONMENT

**SANE_DEBUG_STV680**
If the library was compiled with debug support enabled, this environment variable controls the debug level for this backend. E.g., a value of 128 requests all debug output to be printed. Smaller levels reduce verbosity.

# LIMITATIONS

The windows TWAIN driver has many more options than this SANE backend. However they are only software adjustments. This backend only implements what the webcam can support.

# BUGS

Plenty. Parts of this backend are still under development.
1\. Some untested cameras.
2. Video streaming slow and stops sometimes (scanimage).
3. Sometimes 1/3 of image is NOK (xcam).

# SEE ALSO

**sane**(7), **sane-usb**(5), **scanimage**(1), **xcam**(1)

# AUTHORS

Gerard Klaver *http://gkall.hobby.nl/stv680-aiptek.html*

# CREDITS

Thanks to developers of the other stv680 programs:
STV680 kernel module
pencam2 program
**libghoto2**(3) program (camlib stv0680)
