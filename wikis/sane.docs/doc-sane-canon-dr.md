# NAME

sane-canon_dr - SANE backend for Canon DR-series scanners

# DESCRIPTION

The **sane-canon_dr** library implements a SANE (Scanner Access Now Easy) backend which provides access to some Canon DR-series scanners.

This document describes backend version 60, which shipped with SANE 1.0.32.

# SUPPORTED HARDWARE

This version has only been tested with a few scanner models. Please see *http://www.sane-project.org/sane-supported-devices.html* for the most recent list.

This backend may support other Canon scanners. The best way to determine level of support is to test the scanner directly, or to collect a trace of the windows driver in action. Please contact the author for help or with test results.

In general, the larger machines (DR-4000 and up) which have been tested use a fairly complete protocol, with hardware support for many modes, resolutions and features. The smaller machines have many limitations, like missing horizontal resolutions, missing binary mode, always scanning full-width, etc. There is code in the backend to address these problems, but there seems to be no way to detect if they are required, so they must be hard-coded.

# OPTIONS

Effort has been made to expose most hardware options, including:

**--source Flatbed\|ADF Front\|ADF Back\|ADF Duplex**
Selects the source for the scan.


**--mode Lineart\|Halftone\|Gray\|Color**
Selects the mode for the scan.


**--resolution**
Controls scan resolution.


**--tl-x, --tl-y, --br-x, --br-y**
Sets scan area upper left and lower right coordinates. These are renamed **-t**, **-l**, **-x**, **-y** by some frontends.


**--page-width, --page-height**
Sets paper size. Used by scanner to determine centering of scan coordinates when using the ADF (Automatic Document Feeder) and to detect double feed errors.

Other options will be available based on the capabilities of the scanner: enhancement, compression, buttons and sensors, etc.

Additionally, several 'software' options are exposed by the backend. These are reimplementations of features provided natively by larger scanners, but running on the host computer. This enables smaller machines to have similar capabilities. Please note that these features are somewhat simplistic, and may not perform as well as the native implementations. Note also that these features all require that the driver cache the entire image in memory. This will almost certainly result in a reduction of scanning speed.

**--swcrop**
Requests the driver to detect the extremities of the paper within the larger image, and crop the empty edges.


**--swdeskew**
Requests the driver to detect the rotation of the paper within the larger image, and counter the rotation.


**--swdespeck X**
Requests the driver to find and remove dots of X diameter or smaller from the image, and fill the space with the average surrounding color.

Use 'scanimage --help' to get a list, but be aware that some options may be settable only when another option has been set, and that advanced options may be hidden by some frontend programs.

# CONFIGURATION FILE

The configuration file *canon_dr.conf* is used to tell the backend how to look for scanners, and provide options controlling the operation of the backend. This file is read each time the frontend asks the backend for a list of scanners, generally only when the frontend starts. If the configuration file is missing, the backend will fail to run.

Scanners can be specified in the configuration file in 4 ways:

"scsi CANON DR"

> Requests backend to search all scsi buses in the system for a device which reports itself to be a scanner made by 'CANON', with a model name starting with 'DR'.

"scsi /dev/sg0" (or other scsi device file)

> Requests backend to open the named scsi device. Only useful if you have multiple compatible scanners connected to your system, and need to specify one. Probably should not be used with the other "scsi" line above.

"usb 0x04a9 0x1603" (or other vendor/product ids)

> Requests backend to search all usb buses in the system for a device which uses that vendor and product id. The device will then be queried to determine if it is a Canon scanner.

"usb /dev/usb/scanner0" (or other device file)

> Some systems use a kernel driver to access usb scanners. This method is untested.

Besides the 'scsi' and 'usb' lines, the configuration file supports the following 'option' lines:

"option buffer-size \[number of bytes\]"

> Set the number of bytes in the data buffer to something other than the compiled-in default of 4MB. Large values may cause timeouts or hangs, small values may cause slow scans.
>
> Note: The backend does not place an upper bound on this value, as some users required it to be quite large. Values above the default are not recommended, and may crash your OS or lockup your scsi card driver. You have been warned.

"option vendor-name \[string of text\]"
"option model-name \[string of text\]"
"option version-name \[string of text\]"

> These options can be used collectively to override the values provided by the scanner, or to provide the values when the scanner cannot.

"option padded-read \[0\|1\]"

> Some scanners prepend all data transmitted to host with 12 bytes. Enable this option if the scanner fails to respond to commands.

"option duplex-offset \[integer\]"

> Some scanners pad the upper edge of one side of a duplex scan. There is some variation in the amount of padding. Modify this option if your unit shows an unwanted band of image data on only one side.

**NOTE**: "option" lines may appear multiple times in the configuration file. They only apply to scanners discovered by the next 'scsi/usb' line.

# ENVIRONMENT

The backend uses a single environment variable, **SANE_DEBUG_CANON_DR**, which enables debugging output to stderr. Valid values are:

> 5 Errors
> 10 Function trace
> 15 Function detail
> 20 Option commands
> 25 SCSI/USB trace
> 30 SCSI/USB detail
> 35 Useless noise

# KNOWN ISSUES

This backend was entirely reverse engineered from usb traces of the proprietary driver. Various advanced features of the machines may not be enabled. Many machines have not been tested. Their protocol is unknown.

# CREDITS

The various authors of the **sane-fujitsu**(5) backend provided useful code.
Yabarana Corp. *www.yabarana.com* provided significant funding.
EvriChart, Inc. *www.evrichart.com* provided funding and loaned equipment.
Canon, USA. *www.usa.canon.com* loaned equipment.
HPrint *hprint.com.br* provided funding and testing for DR-2510 support.
Stone-IT *www.stone-it.com* provided funding for DR-2010 and DR-2050 support.
Gerhard Pfeffer provided access and testing for P-208 and P-215.
Special thanks to: Alejandro Imass, Andre Shimakawa, Martijn van Brummelen, Thanos Diacakis and Junren Shi for testing and feedback.

# SEE ALSO

**sane**(7), **sane-scsi**(5), **sane-usb(5)**

# AUTHOR

m\. allan noah: *\<kitno455 a t gmail d o t com\>*.
