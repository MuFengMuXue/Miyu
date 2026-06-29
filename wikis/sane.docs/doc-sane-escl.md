# NAME

sane-escl - SANE backend for eSCL scanners

# DESCRIPTION

The **sane-escl** library implements a SANE (Scanner Access Now Easy) backend that provides access to eSCL protocol scanners.

Currently, the following models work with this backend (This list is not exhaustive):

> BROTHER DCP-J772DW, DCP-L2530DW
> BROTHER HL-L2590DW
> BROTHER MFC-J4540DW, MFC-J985DW, MFC-J1300DW
> CANON IR C3520
> CANON PIXMA MG5765
> CANON PIXMA G4511, G7050
> CANON PIXMA TR4520, TR4540, TR4550, TR4551, TR7500, TR8500
> CANON PIXMA TR8520
> CANON PIXMA TS3100, TS3150, TS3151, TS3152, TS3300, TS3350
> CANON PIXMA TS3351, TS3352, TS3450, TS3451, TS3452, TS5350
> CANON PIXMA TS5351, TS5150, TS6150, TS8050, TS8350, TS9100
> EPSON ET-2750, ET-3750, ET-4750
> EPSON EcoTank L3160
> EPSON XP-4200, XP-6100
> HP DESKJET 2710, DESKJET 2723, DESKJET 3760
> HP LASERJET ENTREPRISE FLOW MFP M578,
> HP LASERJET MFP M28W, LASERJET MFP M630
> HP OFFICEJET 4630, OFFICEJET PRO 8610
> RICOH SP3710S
> XEROX VERSALINK C7220

The. **sane-escl** backend for SANE supports AirScan/eSCL devices that announce themselves on mDNS as \_uscan.\_utcp or \_uscans.\_utcp. If the device is available, the **sane-escl** backend recovers these capacities. The user configures and starts scanning. A list of devices that use the eSCL protocol can be found at *https://support.apple.com/en-us/HT201311*. While these devices are expected to work, your mileage may vary.

# FILES

*@CONFIGDIR@/escl.conf*
The backend configuration file.

*@LIBDIR@/libsane-escl.a*
The static library implementing this backend.

*@LIBDIR@/libsane-escl.so*
The shared library implementing this backend (present on systems that support dynamic loading).

# ENVIRONMENT

**SANE_DEBUG_ESCL**
If the library was compiled with debug support enabled, this environment variable controls the debug level for this backend. E.g., a value of 128 requests all debug output to be printed. Smaller levels reduce verbosity.

# SEE ALSO

**sane**(7) **scanimage**(1) **xscanimage**(1) **xsane**(1)

# AUTHORS

Touboul Nathane, Thierry HUCHARD
