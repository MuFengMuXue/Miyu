# NAME

sane-v4l - SANE interface for Video for Linux API

# DESCRIPTION

The **sane-v4l** library implements a SANE (Scanner Access Now Easy) backend that provides generic access to video cameras and similar equipment using the V4L (Video for Linux) API.

This is ALPHA software. Really! Important features are missing and there are lots of bugs. The code is currently only tested on a Linux 2.4 system with a Hauppauge WinTV video card.

# DEVICE NAMES

This backend expects device names of the form:

> *special*

Where *special* is the UNIX path-name for the special device that corresponds to the v4l device. The special device name must be a v4l device or a symlink to such a device. For example, such a device name could be */dev/video0* or */dev/bttv0*.

# CONFIGURATION

The contents of the *v4l.conf* file is a list of device names that correspond to v4l devices. Empty lines and lines starting with a hash mark (#) are ignored. A sample configuration file is shown below:

> /dev/bttv0
> \# this is a comment
> /dev/video3

# FILES

*@CONFIGDIR@/v4l.conf*
The backend configuration file (see also description of **SANE_CONFIG_DIR** below).

*@LIBDIR@/libsane-v4l.a*
The static library implementing this backend.

*@LIBDIR@/libsane-v4l.so*
The shared library implementing this backend (present on systems that support dynamic loading).

# ENVIRONMENT

**SANE_CONFIG_DIR**
This environment variable specifies the list of directories that may contain the configuration file. On \*NIX systems, the directories are separated by a colon (\`:'), under OS/2, they are separated by a semi-colon (\`;'). If this variable is not set, the configuration file is searched in two default directories: first, the current working directory (".") and then in *@CONFIGDIR@*. If the value of the environment variable ends with the directory separator character, then the default directories are searched after the explicitly specified directories. For example, setting **SANE_CONFIG_DIR** to "/tmp/config:" would result in directories *tmp/config*, *.*, and *@CONFIGDIR@* being searched (in this order).

**SANE_DEBUG_V4L**
If the library was compiled with debug support enabled, this environment variable controls the debug level for this backend. E.g., a value of 128 requests all debug output to be printed. Smaller levels reduce verbosity.

# AUTHOR

Juergen G. Schimmer, Henning Meier-Geinitz

# BUGS:

If more than one video card is present, a crash may occur. Frequency and geometry selection is missing.
Send bug reports to the SANE mailing list: *sane-devel@alioth-lists.debian.net*. You must be subscribed to the list to send mail. See *http://www.sane-project.org/mailing-lists.html* for details.

# SEE ALSO

**sane**(7), **xcam**(1)
