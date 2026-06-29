# NAME

sane-canon - SANE backend for Canon SCSI scanners

# DESCRIPTION

The **sane-canon** library implements a SANE (Scanner Access Now Easy) backend that provides access to the following Canon flatbed and film scanners:

> CanoScan 300
> CanoScan 600
> CanoScan FB620S
> CanoScan FB1200S
> CanoScan FS2700F
> CanoScan FS2710S

Parallel port and USB scanners are not supported by this backend; see the manual pages for **sane-canon_pp**(5) and **sane-canon630u**(5) for further information.

IMPORTANT: This is beta code. We tested the code on the scanners listed above, using the computers and operating systems available to us, but we cannot guarantee that the backend will work smoothly with future operating systems, SCSI adapters, SANE frontend programs, or Canon scanners not contained in the list above. In some cases your computer might even hang. It cannot be excluded (although we consider it extremely unlikely) that your scanner will be damaged.

That said, TESTERS ARE WELCOME. Send your bug reports and comments to Manuel Panea *\<mpd@rzg.mpg.de\>*; for questions concerning the FB620 and FB1200S contact Mitsuru Okaniwa *\<m-okaniwa@bea.hi-ho.ne.jp\>*, for the FS2710S Ulrich Deiters *\<ukd@xenon.pc.uni-koeln.de\>*.

# TIPS (FS2700F)

Scanning either slides or negatives has been found to require rather large gamma corrections of about 2.2 to 2.4 (same value for red, green, and blue). It is recommended to use the automatic exposure controls of the frontend **xsane**(1) for best results.

The "Auto Focus" function triggers a special pass to determine the focus value. After that, the real scanning pass takes place.

Even with "Auto Focus" turned on, the scanned image is often a bit too blurred. Using the **gimp**(1) to do a "Filter-\>Enhance-\>Sharpen" at about 40 to 60 improves the image considerably.

# TIPS (FS2710S)

Gamma corrections are done not by the scanner, but by the backend. The scanner is always run in 12-bit mode. In "color" mode the image data are corrected for gamma, shadow point, etc., and then truncated to 8-bit intensities; the default gamma value is 2.0. In "raw" mode the image data are exported without corrections as 16-bit intensities; this mode can be recommended if extensive adjustments have to be made to a picture (and if the frontend can handle 16-bit intensities).

Negatives are handled by simple color inversion and will require manual removal of blue discoloration.

# FILES

*@LIBDIR@/libsane-canon.a*
The static library implementing this backend.

*@LIBDIR@/libsane-canon.so*
The shared library implementing this backend (present on systems that support dynamic loading).

# ENVIRONMENT

**SANE_DEBUG_CANON**
If the library was compiled with debug support enabled, this environment variable controls the debug level for this backend. Higher debug levels increase the verbosity of the output.

Example: export SANE_DEBUG_CANON=4

# SEE ALSO

**sane-scsi**(5)
*http://www.rzg.mpg.de/~mpd/sane/doc/canon.install2700F.txt* (installation of a CanoScan 2700F)

# AUTHOR

Helmut Koeberle, Manuel Panea, and Markus Mertinat;
FB620S and FB1200S support by Mitsuru Okaniwa;
FS2710S support by Ulrich Deiters
Man page by Henning Meier-Geinitz (mostly based on canon.README)
