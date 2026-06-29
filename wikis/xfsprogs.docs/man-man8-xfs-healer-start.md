# NAME

xfs_healer_start - starts xfs_healer instances

# SYNOPSIS

**xfs_healer_start** \[ **OPTIONS** \]
**xfs_healer_start -V**

# DESCRIPTION

**xfs_healer_start** starts the xfs_healer service whenever the kernel mounts an XFS filesystem in the current mount namespace.

**WARNING!** This program is **EXPERIMENTAL**, which means that its behavior and interface could change at any time!

Normally this program runs as a systemd service.

# OPTIONS

**--supported**
Check if the kernel supports listening for mount events. Exits with 0 if it does, and non-zero if not.

**--mountns ***path*
Monitor the given mount namespace. Defaults to the mount namespace associated with the process itself.

**-V**
Prints the version number and exit.

# SEE ALSO

**xfs_healer**(8).
