# NAME

sane-kodak - SANE backend for big Kodak flatbed and ADF scanners

# DESCRIPTION

The **sane-kodak** library implements a SANE (Scanner Access Now Easy) backend which provides access to large Kodak flatbed and ADF scanners.

This document describes backend version 7, which shipped with SANE 1.0.21.

# SUPPORTED HARDWARE

This version should support models which speak the Kodak SCSI and Firewire protocols. The i1860 was used to develop the backend, but other models may work with only minimal modifications. Please see the list at *http://www.sane-project.org/sane-supported-devices.html* for an updated list.

If you have a machine not on that list, or reported as 'untested': the best way to determine level of support is to test the scanner directly, or to collect a trace of the windows driver in action. Please contact the author for help or with test results.

# UNSUPPORTED HARDWARE

Most of the recent Kodak consumer or workgroup level machines are based on other chipsets and are not supported by this backend. Some of these scanners may be supported by another backend.

# OPTIONS

Effort has been made to expose the basic hardware options, including:

**--source s**

> Selects the source for the scan. Options may include "Flatbed", "ADF Front", "ADF Back", "ADF Duplex".

**--mode m**

> Selects the mode for the scan. Options may include "Lineart", "Halftone", "Gray", and "Color".

**--resolution**

> Controls scan resolution. Available choices may be limited by mode.

**--tl-x**, **--tl-y**, **--br-x**, **--br-y**

> Sets scan area upper left and lower right coordinates. These are renamed **-t**, **-l**, **-x**, **-y** by some frontends.

**--page-width**, **--page-height**

> Sets paper size. Used by scanner to determine centering of scan coordinates when using the ADF (Automatic Document Feeder) and to detect double feed errors.

Other options will be available based on the capabilities of the scanner. Use *scanimage --help* to get a list, but be aware that some options may be settable only when another option has been set, and that advanced options may be hidden by some frontend programs.

# CONFIGURATION FILE

The configuration file *kodak.conf* is used to tell the backend how to look for scanners, and provide options controlling the operation of the backend. This file is read each time the frontend asks the backend for a list of scanners, generally only when the frontend starts. If the configuration file is missing, the backend will use a set of compiled defaults, which are identical to the default configuration file shipped with SANE.

Scanners can be specified in the configuration file in 2 ways:

"scsi KODAK"

> Requests backend to search all scsi buses in the system for a device which reports itself to be a scanner made by 'KODAK'.

"scsi /dev/sg0" (or other scsi device file)

> Requests backend to open the named scsi device. Only useful if you have multiple compatible scanners connected to your system, and need to specify one. Probably should not be used with the other "scsi" line above.

The only configuration option supported is "buffer-size=xxx", allowing you to set the number of bytes in the data buffer to something other than the compiled-in default, 32768 (32K). Some users report that their scanner will "hang" mid-page, or fail to transmit the image if the buffer is not large enough.

Note: This option may appear multiple times in the configuration file. It only applies to scanners discovered by 'scsi/usb' lines that follow this option.

Note: The backend does not place an upper bound on this value, as some users required it to be quite large. Values above the default are not recommended, and may crash your OS or lockup your scsi card driver. You have been warned.

# ENVIRONMENT

The backend uses a single environment variable, **SANE_DEBUG_KODAK**, which enables debugging output to stderr. Valid values are:

> 5 Errors
> 10 Function trace
> 15 Function detail
> 20 Option commands
> 25 SCSI trace
> 30 SCSI detail
> 35 Useless noise

# KNOWN ISSUES

Most hardware options are either not supported or not exposed for control by the user, including: multifeed detection, image compression, autocropping, endorser, thresholding, multi-stream, etc.

# CREDITS

The various authors of the **sane-fujitsu**(5) backend provided useful code.
Kodak provided access to hardware, documentation and personnel.

# SEE ALSO

**sane**(7), **sane-scsi**(5), **scanimage**(1)

# AUTHOR

m\. allan noah: \<*kitno455 a t gmail d o t com*\>
