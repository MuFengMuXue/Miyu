# NAME

sane-coolscan3 - SANE backend for Nikon Coolscan film scanners

# DESCRIPTION

The **sane-coolscan3** library implements a SANE (Scanner Access Now Easy) backend that provides access to Nikon Coolscan film scanners. Some functions of this backend should be considered **beta-quality** software. Most functions have been stable for a long time, but of course new development can not and will not function properly from the very first day.

At present, the following scanners are known to work with this backend:

> Model:                       Connection Type
>     ---------------------------  -------------------
>     LS-30 (Coolscan III)         SCSI
>     LS-40 ED (Coolscan IV)       USB
>     LS-50 ED (Coolscan V)        USB
>     LS-2000                      SCSI
>     LS-4000 ED                   IEEE 1394
>     LS-8000 ED                   IEEE 1394

Please send mail to *sane-devel@alioth-lists.debian.net* to report successes or failures.

# OPTIONS

The options the backend supports can either be selected through command line options to programs like **scanimage**(1) or through GUI elements in **xscanimage**(1) or **xsane**(1).

Valid command line options and their syntax can be listed by using:

> scanimage --help -d coolscan3:\<interface\>:\<device\>

where \<interface\> and \<device\> specify the device in question, as in the configuration file (see next section). The **-d** parameter and its argument can be omitted to obtain information on the first scanner identified. Use the command:

> scanimage -L

to list all devices recognized by your SANE installation.

The options should be fully described by the description or tooltips given by frontend. Here is a description of some of the most important options, in the syntax with which they must be supplied to **scanimage**(1):

**--frame \<n\>**
This option specifies which frame to operate on, if a motorized film strip feeder or APS adapter are used. The frame number *\<n\>* ranges from 1 to the number of frames available, which is sensed each time the backend is initialized (usually each time you start the frontend).

**--subframe \<x\>**
This option shifts the scan window by the specified amount (default unit is mm).

**--infrared=yes/no**
If set to "yes", the scanner will read the infrared channel, thus allowing defect removal in software. The infrared image is read during a second scan, with no options altered. The backend must not be restarted between the scans. If you use **scanimage**(1), perform a batch scan with **--batch-count=2** to obtain the IR information.

**--depth \<n\>**
Here \<n\> can either be 8 or the maximum number of bits supported by the scanner (10, 12, or 14). It specifies whether or not the scanner reduces the scanned data to 8 bits before sending it to the backend. If 8 bits are used, some information and thus image quality is lost, but the amount of data is smaller compared to higher depths. Also, many imaging programs and image formats cannot handle depths greater than 8 bits.

**--autofocus**
Perform autofocus operation. Unless otherwise specified by the other options ( **--focus-on-centre** and friends), focusing is performed on the centre of the selected scan area.

**--ae-wb**
**--ae**
Perform a pre-scan to calculate exposure values automatically. **--ae-wb** will maintain the white balance, while **--ae** will adjust each channel separately.

**--exposure**
Multiply all exposure times with this value. This allows exposure correction without modifying white balance.

**--load**
Load the next slide when using the slide loader (SF-200 bulk loader only).

**--eject**
Eject the film strip or mounted slide when using the slide loader.

**--reset**
Reset scanner. The scanner will perform the same action as when power is turned on: it will eject the slide (with the SF-200 bulk loader) and calibrate itself. Use this whenever the scanner refuses to load a slide properly, as a result of which **--eject** does not work.

# CONFIGURATION FILE

The configuration file *@CONFIGDIR@/coolscan3.conf* specifies the device(s) that the backend will use. Owing to the nature of the supported connection types SCSI, USB, and IEEE 1394, the default configuration file supplied with the SANE distribution should work without being edited.

Each line in the configuration file is either of the following, where all entries are case-sensitive:

*blank or starting with a '#' character*
These lines are ignored, thus '#' can be used to include comments.

*containing only the word "auto"*
This instructs the backend to probe for a scanner by scanning the buses for devices with known identifiers. This is the default action when no configuration file is present.

*a line of the form \<interface\>:\<device\>*
Here \<interface\> can be one of "scsi" or "usb", and \<device\> is the device file of the scanner. Note that IEEE 1394 devices are handled by the SBP-2 module in the kernel and appear to SANE as SCSI devices.

# FILES

*@LIBDIR@/libsane-coolscan3.a*
The static library implementing this backend.

*@LIBDIR@/libsane-coolscan3.so*
The shared library implementing this backend (present on systems that support dynamic loading).

*@CONFIGDIR@/coolscan3.conf*
Configuration file for this backend, read each time the backend is initialized.

# ENVIRONMENT

**SANE_DEBUG_COOLSCAN3**
If the library was compiled with debug support enabled, this environment variable controls the debug level for this backend. E.g., a value of 128 requests all debug output to be printed. Smaller levels reduce verbosity.

# SEE ALSO

**sane-scsi**(5), **sane-usb**(5), **scanimage**(1), **xscanimage**(1), **xsane**(1)

# BUGS

Currently, the SANE protocol does not allow automatically updating options whenever the hardware changes. Thus the number of choices for the **--frame** option will be fixed when the backend is initialized (usually when the user runs the frontend). In particular, if there is no film strip in the automatic film strip feeder when the backend is initialized, the **--frame** option will not appear at all. Also, restarting the frontend after swapping film adapters is strongly recommended.

Linux kernels prior to 2.4.19 had a patch that truncated INQUIRY data from IEEE 1394 scanners to 36 bytes, discarding vital information about the scanner. The IEEE 1394 models therefore only work with 2.4.19 or later.

No real bugs currently known, please report any to the SANE developers' list.

# AUTHORS

coolscan3 written by A. Zummo \<*a.zummo@towertech.it*\>, based heavily on coolscan2 written by András Major \<*andras@users.sourceforge.net*\>.
