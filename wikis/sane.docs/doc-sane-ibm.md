# NAME

sane-ibm - SANE backend for IBM and Ricoh SCSI flatbed scanners

# DESCRIPTION

The **sane-ibm** library implements a SANE (Scanner Access Now Easy) backend that provides access to the IBM 2456 and the Ricoh IS-410, IS-420, and IS-430 flatbed scanners. Support for the IS-410 and IS-430 is untested. Please contact the maintainer or the sane-devel mailing list if you own such a scanner.

This backend is alpha-quality. It may have bugs and some scanners haven't been tested at all. Be careful and pull the plug if the scanner causes unusual noise.

# DEVICE NAMES

This backend expects device names of the form:

> *special*

Where *special* is the path-name for the special device that corresponds to a SCSI scanner. The program **sane-find-scanner**(1) helps to find out the correct device. Under Linux, such a device name could be */dev/sg0* or */dev/sga*, for example. See **sane-scsi**(5) for details.

# CONFIGURATION

The contents of the *ibm.conf* file is a list of device names that correspond to SCSI scanners. Empty lines and lines starting with a hash mark (#) are ignored. See **sane-scsi**(5) on details of what constitutes a valid device name.

# FILES

*@CONFIGDIR@/ibm.conf*
The backend configuration file (see also description of **SANE_CONFIG_DIR** below).

*@LIBDIR@/libsane-ibm.a*
The static library implementing this backend.

*@LIBDIR@/libsane-ibm.so*
The shared library implementing this backend (present on systems that support dynamic loading).

# ENVIRONMENT

**SANE_CONFIG_DIR**
This environment variable specifies the list of directories that may contain the configuration file. On \*NIX systems, the directories are separated by a colon (\`:'), under OS/2, they are separated by a semi-colon (\`;'). If this variable is not set, the configuration file is searched in two default directories: first, the current working directory (".") and then in *@CONFIGDIR@*. If the value of the environment variable ends with the directory separator character, then the default directories are searched after the explicitly specified directories. For example, setting **SANE_CONFIG_DIR** to "/tmp/config:" would result in directories *tmp/config*, *.*, and *"@CONFIGDIR@* being searched (in this order).

**SANE_DEBUG_IBM**
If the library was compiled with debug support enabled, this environment variable controls the debug level for this backend. Higher debug levels increase the verbosity of the output.

# SEE ALSO

**sane**(7), **sane-find-scanner**(1), **sane-scsi**(5),

# AUTHOR

mf \<*massifr@tiscalinet.it*\>
Maintained by Henning Meier-Geinitz \<*henning@meier-geinitz.de*\>
