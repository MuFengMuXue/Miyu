# NAME

xfs_scrub_all - scrub all mounted XFS filesystems

# SYNOPSIS

**xfs_scrub_all** \[ **-hxV** \]

# DESCRIPTION

**xfs_scrub_all** attempts to read and check all the metadata on all mounted XFS filesystems. The online scrub is performed via the **xfs_scrub** tool, either by running it directly or by using systemd to start it in a restricted fashion. Mounted filesystems are mapped to physical storage devices so that scrub operations can be run in parallel so long as no two scrubbers access the same device simultaneously.

# OPTIONS

**--auto-media-scan-interval**
Automatically enable the file data scan (i.e. the **-x** flag) if it has not been run in the specified interval. The interval must be a floating point number with an optional unit suffix. Supported unit suffixes are *y*, *q*, *mo*, *w*, *d*, *h*, *m*, and *s* for years, 90-day quarters, 30-day months, weeks, days, hours, minutes, and seconds, respectively. If no units are specified, the default is seconds.

**--auto-media-scan-stamp**
Path to a file that will record the last time the media scan was run. Defaults to @stampfile@.

**-h**
Display help.

**-x**
Read all file data extents to look for disk errors.

**-V**
Prints the version number and exits.

# EXIT CODE

The exit code returned by **xfs_scrub_all** is the sum of the following conditions:
0 - No errors
4 - File system errors left uncorrected
8 - Operational error
16 - Usage or syntax error

These are the same error codes returned by xfs_scrub.


# SEE ALSO

**xfs_scrub**(8).
