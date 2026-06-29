# NAME

sane-pnm - SANE PNM image reader pseudo-backend

# DESCRIPTION

The **sane-pnm** library implements a SANE (Scanner Access Now Easy) backend that provides access to PNM (Portable aNyMap files, which covers PBM bitmap files, PGM grayscale files, and PPM pixmap files). The purpose of this backend is primarily to aid in debugging of SANE frontends. It also serves as an illustrative example of a minimal SANE backend.

# DEVICE NAMES

This backend provides two devices called **0** and **1.**

# CONFIGURATION

No configuration required.

# FILES

*@LIBDIR@/libsane-pnm.a*
The static library implementing this backend.

*@LIBDIR@/libsane-pnm.so*
The shared library implementing this backend (present on systems that support dynamic loading).

# ENVIRONMENT

**SANE_DEBUG_PNM**
If the library was compiled with debug support enabled, this environment variable controls the debug level for this backend. E.g., a value of 128 requests all debug output to be printed. Smaller levels reduce verbosity.

# BUGS

If the **sane-pnm** backend is installed and **saned**(8) is used to allow users on remote computers to scan on the local machine, PNM files can be read by the remote user. This is limited to the files **saned**(8) can access (usually it's running as user "sane"). All PNM files can be read if **saned**(8) runs as root which isn't recommended anyway. The **sane-pnm** backend is disabled by default. If you want to use it, enable it with configure (see *configure --help* for details). Be sure that only trusted users can access the **sane-pnm** backend over **saned**(8).

# AUTHOR

Andreas Beck, Gordon Matzigkeit, and David Mosberger

# SEE ALSO

**sane**(7), **saned**(8)
