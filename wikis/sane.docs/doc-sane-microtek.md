# NAME

sane-microtek - SANE backend for Microtek scanners

# DESCRIPTION

The **sane-microtek** library implements a SANE (Scanner Access Now Easy) backend that provides access to the "second generation" Microtek scanners. At present, the following hardware is known to work with this backend:

> Microtek ScanMaker E2, E3, E6
> Microtek ScanMaker II, IIG, IIHR, IISP, III
> Microtek ScanMaker 35t, 35t+, 45t
> Microtek ScanMaker 600GS, 600ZS (see bug notes)
> Agfa StudioScan
> Agfa StudioScan II, StudioScan IIsi
> Agfa Arcus II (but not the "Arcus")
> Agfa DuoScan (preliminary)
> Vobis "Highscreen Realscan"
> Microtek Color PageWiz (preliminary)
>
> Transparent Media Adapter
> Document AutoFeeder

The driver supports line art, halftone, 8bpp gray, and 24bpp color scans at normal and "expanded" resolutions (i.e. 1200x1200 on an E6), fast scans for color previews, and downloadable gamma tables.

The supported scanners are all SCSI scanners. However, some parallel port models may work (under Linux), if they use a parport-\>scsi chip, and if you can find a scsi-\>parport driver. This is known to be the case for the Color PageWiz.

The driver does **not** support the newest Microtek scanners, such as the V330 and V660, which use a new and very different SCSI-II command set. For those, try the alternate **microtek2**(5) backend. Most non-SCSI scanners would use the new command set. Most scanners newer than the Scanmaker E6 would use the new command set.

If you own a Microtek scanner other than the ones listed above, tell us what happens --- see the **BUGS** section at the end of this document.

Although this manual page is generally updated with each release, up-to-date information on new releases and extraneous helpful hints are available from the backend homepage:

> *http://www.mir.com/mtek/*

# DEVICE NAMES

This backend expects device names of the form:

> *special*

Where *special* is the UNIX path-name for the special device that corresponds to the scanner. The special device name must be a generic SCSI device or a symlink to such a device. Under Linux, such a device name could be */dev/sga* or */dev/sge*, for example.

# CONFIGURATION

The contents of the *microtek.conf* file is a list of device names that correspond to Microtek scanners. Empty lines and lines starting with a hash mark (#) are ignored. A sample configuration file is shown below:

> /dev/scanner
> \# this is a comment
> /dev/sge

The configuration file may also contain the special tokens *norealcal* or *noprecal*. *norealcal* will disable the use of magic, undocumented scanner calibration commands which are known to work on the E6, but may not work with other models. *noprecal* will disable logic which tries to avoid scanner precalibration. This logic would only have been activated if the magic calibration code was turned off.

# FILES

*@CONFIGDIR@/microtek.conf*
The backend configuration file (see also description of **SANE_CONFIG_DIR** below).

*@LIBDIR@/libsane-microtek.a*
The static library implementing this backend.

*@LIBDIR@/libsane-microtek.so*
The shared library implementing this backend (present on systems that support dynamic loading).

# ENVIRONMENT

**SANE_CONFIG_DIR**
This environment variable specifies the list of directories that may contain the configuration file. On \*NIX systems, the directories are separated by a colon (\`:'), under OS/2, they are separated by a semi-colon (\`;'). If this variable is not set, the configuration file is searched in two default directories: first, the current working directory (".") and then in *@CONFIGDIR@*. If the value of the environment variable ends with the directory separator character, then the default directories are searched after the explicitly specified directories. For example, setting **SANE_CONFIG_DIR** to "/tmp/config:" would result in directories *tmp/config*, *.*, and *@CONFIGDIR@* being searched (in this order).

**SANE_DEBUG_MICROTEK**
If the library was compiled with debugging support enabled, this environment variable controls the debug level for this backend. A value of 128 requests maximally copious debug output; smaller levels reduce verbosity.

# SEE ALSO

**sane**(7), **sane-scsi**(5), **sane-microtek2**(5)

# AUTHOR

Matt Marjanovic

# BUGS

Known bugs/limitations are:

> Brightness and contrast broken.
> The 600GS is grayscale only, and will lock up if you select color. (Unfortunately, the 600GS and 600ZS are indistinguishable by software.)

i.e. don't complain about these --- but if brightness and/or contrast **do** work for you, please tell me.

If your scanner locks up, try setting the *norealcal* or *noprecal* option in the configuration file (first one, then both), and see if it helps. (If it does, report it.)

Send lengthy bug reports and new scanner information to *mtek-bugs@mir.com*. All bug reports and new scanner inquiries should include an error log file. You can generate copious stderr output by setting the **SANE_DEBUG_MICROTEK** environment variable described above. For example:

> setenv SANE_DEBUG_MICROTEK 128

More general comments, suggestions, and inquiries about frontends or SANE should go to *sane-devel@alioth-lists.debian.net*, the SANE Developers mailing list. Have a look at *http://www.sane-project.org/mailing-lists.html* concerning subscription to sane-devel.
