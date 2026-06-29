# NAME

sane-s9036 - SANE backend for Siemens 9036 flatbed scanners

# DESCRIPTION

The **sane-s9036** library implements a SANE (Scanner Access Now Easy) backend that provides access to Siemens 9036 flatbed scanners.

# DEVICE NAMES

This backend expects device names of the form:

> *special*

Where *special* is the path-name for the special device that corresponds to a SCSI scanner. The special device name must be a generic SCSI device or a symlink to such a device. The program **sane-find-scanner**(1) helps to find out the correct device. Under Linux, such a device name could be */dev/sga* or */dev/sge*, for example. See **sane-scsi**(5) for details.

# FILES

*@CONFIGDIR@/s9036.conf*
The backend configuration file (see also description of **SANE_CONFIG_DIR** below).

*@LIBDIR@/libsane-s9036.a*
The static library implementing this backend.

*@LIBDIR@/libsane-s9036.so*
The shared library implementing this backend (present on systems that support dynamic loading).

# ENVIRONMENT

**SANE_CONFIG_DIR**
This environment variable specifies the list of directories that may contain the configuration file. On \*NIX systems, the directories are separated by a colon (\`:'), under OS/2, they are separated by a semi-colon (\`;'). If this variable is not set, the configuration file is searched in two default directories: first, the current working directory (".") and then in *@CONFIGDIR@*. If the value of the environment variable ends with the directory separator character, then the default directories are searched after the explicitly specified directories. For example, setting **SANE_CONFIG_DIR** to "/tmp/config:" would result in directories *tmp/config*, *.*, and *@CONFIGDIR@* being searched (in this order).

**SANE_DEBUG_S9036**
If the library was compiled with debug support enabled, this environment variable controls the debug level for this backend. Higher debug levels increase the verbosity of the output.

Example: export SANE_DEBUG_S9036=4

# SEE ALSO

**sane**(7), **sane-scsi**(5)

# AUTHOR

Ingo Schneider
