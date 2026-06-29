# NAME

sane-pieusb - SANE backend for USB-connected PIE PowerSlide and Reflecta DigitDia/CrystalScan/ProScan slide scanners

# DESCRIPTION

The **sane-pieusb** library implements a SANE (Scanner Access Now Easy) backend that provides access to USB-connected PIE and Reflecta slide scanners.
At present, the following scanners should work with this backend:

    Model:                    Status
    ------------------------- ------
    PIE PowerSlide 3600       Untested
    PIE PowerSlide 3650       Untested
    PIE PowerSlide 4000       Untested
    PIE PowerSlide 5000       Untested
    Reflecta CrystalScan 7200 Untested
    Reflecta ProScan 4000     Untested
    Reflecta ProScan 7200     Untested
    Reflecta DigitDia 3600    Untested
    Reflecta DigitDia 4000    Untested
    Reflecta DigitDia 5000    Untested
    Reflecta DigitDia 6000    Ok

# MULTIPLE SLIDES

Support for multiple slide scanners (like the PowerSlide or DigitDia series) is done by auto-advancing ('Advance slide' setting) the slide after each scan.

However, for best results, it is recommended to do a preview for every slide since this sets gamma, brightness, and contrast to optimal values.

Attention: SANE does not have an automatic landscape/portrait detection and re-orientation when scanning multiple slides. You have to put all slides into one orientation first !

# DIRT REMOVAL

If available, **sane-pieusb** supports infrared scans for dirt detection and removal. This must be enabled via the 'Clean image' setting.

# KNOWN PROBLEMS

The **sane-pieusb** backend supports dirt removal based on infrared scan information. Since SANE does not provide post-processing in the backend, **sane-pieusb** does the scanning and dirt removal during the setup phase. The 'scan' phase is only used to transfer the completed image. Therefore **sane-pieusb** does not multi-thread making a typical frontend appear as 'blocked'. Also cancel requests are only honored between scans.

# ENVIRONMENT

**SANE_DEBUG_PIEUSB**
If the library was compiled with debug support enabled, this environment variable controls the debug level for this backend. E.g., a value of 128 requests all debug output to be printed. Smaller levels reduce verbosity.

> level   debug output
>     ------- ------------------------------
>      0       nothing
>      1       errors
>      2       warnings & minor errors
>      5       additional information
>      7       SANE api calls
>      9       backend functions
>     11       scanner functions
>     13       usb functions
>     15       image buffer functions

# FILES

*@CONFIGDIR@/pieusb.conf*
The backend configuration file

*@LIBDIR@/libsane-pieusb.a*
The static library implementing this backend.

*@LIBDIR@/libsane-pieusb.so*
The shared library implementing this backend (present on systems that support dynamic loading).

# SEE ALSO

**sane**(7)

# CONTACT AND BUG-REPORTS

Please send any information and bug-reports to:
Klaus Kämpf \<*kkaempf@suse.com*\>

# AUTHORS

The pieusb backend is based on work by Jan Vleeshouwers, Michael Rickmann, and Klaus Kämpf
