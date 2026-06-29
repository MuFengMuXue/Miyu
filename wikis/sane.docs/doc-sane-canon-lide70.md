# NAME

sane-canon_lide70 - SANE backend for the Canon LiDE 70 and 600(F) USB flatbed scanners

# DESCRIPTION

The **canon_lide70** library implements a SANE (Scanner Access Now Easy) backend that provides access to the Canon Inc. CanoScan LiDE 70 and 600(F) flatbed scanners. The film unit of the LiDE 600F is not supported.

Due to Canon's unwillingness to provide scanner documentation, this software was developed by analyzing the USB traffic of the Windows XP driver. The precise meaning of the individual commands that are sent to the scanner is known only to a very limited extent. Some sophistication present in the Windows XP driver has been left out. There is, for example, no active calibration.

Testers and reviewers are welcome. Send your bug reports and comments to the sane-devel mailing list *\<sane-devel@alioth-lists.debian.net\>*.

# CONFIGURATION

The *@CONFIGDIR@/canon_lide70.conf* file identifies the LiDE 70 by its vendor code 0x04a9 and its product code 0x2225. For the LiDE 600(f) the product code is 0x2224.

# BACKEND SPECIFIC OPTIONS

**Scan Mode:**

**--resolution 75\|150\|300\|600\|1200 \[default 600\]**
Sets the resolution of the scanned image in dots per inch. Scanning at 1200 dpi is not available on the LiDE 600(F) and it is very slow on the LiDE 70.


**--mode Color\|Gray\|Lineart \[default: Color\]**
Selects the scan mode. Lineart means fully black and fully white pixels only.


**--threshold 0..100 (in steps of 1) \[default 75\]**
Select minimum-brightness percentage to get a white point, relevant only for Lineart


**--non-blocking\[=(yes\|no)\] \[inactive\]**
This option has not yet been implemented. Scans are captured in a temporary file with a typical size of 100MB.

**Geometry:**

**-l 0..216.069 \[default 0\]**
Top-left x position of scan area in millimeters.

**-t 0..297 \[default 0\]**
Top-left y position of scan area in millimeters.

**-x 0..216.069 \[default 80\]**
Width of scan-area in millimeters.

**-y 0..297 \[default 100\]**
Height of scan-area in millimeters.

# FILES

*@CONFIGDIR@/canon_lide70.conf*
The backend configuration file

*@LIBDIR@/libsane-canon_lide70.a*
The static library implementing this backend.

*@LIBDIR@/libsane-canon_lide70.so*
The shared library implementing this backend (present on systems that support dynamic loading).

# ENVIRONMENT

**SANE_DEBUG_CANON_LIDE70**
If the library was compiled with debug support enabled, this environment variable controls the debug level for this backend. Higher debug levels increase the verbosity of the output.

Example:
SANE_DEBUG_CANON_LIDE70=128 scanimage \> /dev/null

# KNOWN PROBLEMS

At low resolutions (75 and 150 dpi, implying high slider speeds) the LiDE 70 misses the top one millimeter of the scan area. This can be remedied by shifting the document one millimeter downward, in cases where such precision matters. Note that **xsane**(1) uses the 75 dpi mode for prescans. The problem is worse on the LiDE 600(F), where the offset is five millimeters.

# SEE ALSO

**sane**(7), **sane-usb**(5), **sane-find-scanner**(1), **scanimage**(1), **xsane**(1),
http://www.juergen-ernst.de/info_sane.html

# AUTHOR

pimvantend, building upon pioneering work by Juergen Ernst.
