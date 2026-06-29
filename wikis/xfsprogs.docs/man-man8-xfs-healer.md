# NAME

xfs_healer - automatically heal damage to XFS filesystem metadata

# SYNOPSIS

**xfs_healer** \[ **OPTIONS** \] *mount-point*
**xfs_healer -V**

# DESCRIPTION

**xfs_healer** is a daemon that tries to automatically repair damaged XFS filesystem metadata.

**WARNING!** This program is **EXPERIMENTAL**, which means that its behavior and interface could change at any time!

**xfs_healer** asks the kernel to report all observations of corrupt metadata, media errors, filesystem shutdowns, and file I/O errors. The program can respond to runtime metadata corruption errors by initiating targeted repairs of the suspect metadata or a full online fsck of the filesystem.

Normally this program runs as a systemd service. The service is activated via the *xfs_healer_start* service if systemd is supported.

The kernel may not support repairing or optimizing the filesystem. If this is the case, the filesystem must be unmounted and **xfs_repair**(8) run on the filesystem to fix the problems.

# OPTIONS

**--everything**
Ask the kernel to send us good metadata health events, not only events related to metadata corruption, media errors, shutdowns, and I/O errors.

**--foreground**
Start enough event handling threads to allow consumption of all online CPUs. If not specified, start exactly one event handling thread.

**--no-autofsck**
Do not use the *autofsck* filesystem property to decide whether or not to repair corrupt metadata. If the **--repair** option is given, then all corruptions will be repaired. If the **--repair** option is not given, then the program will never try to repair the filesystem.

**--quiet**
Do not print every event to standard output.

**--repair**
Always try to repair each piece of corrupt metadata when the kernel tells us about it. If an individual repair fails or the kernel tells us that health events were lost, the *xfs_scrub* service for this mount point will be launched. The default is not to try to repair anything. If this option is specified but the kernel does not support repairs, the program will exit.

**--supported**
Check if the filesystem supports sending health events. Exits with 0 if it does, and non-zero if not.

**-V**
Prints the version number and exit.

# AUTOFSCK

By default, this program will read the *autofsck* filesystem property to decide if it should try to repair corruptions. If the property is set to these values:

> *repair*
> Corruptions will be repaired.
>
> *check* or *optimize*
> Corruptions will be logged.
>
> *none*
> The program will exit.

If the property is not set but the filesystem supports any back-reference metadata (reverse mappings and parent pointers), then corruptions will be logged. If no back-reference metadata are present, the program will exit.

See the **xfs_scrub**(8) manual page for more details on this filesystem property.

# CAVEATS

**xfs_healer** is an immature utility! Do not run this program unless you have backups of your data! This program takes advantage of in-kernel scrubbing to verify a given data structure with locks held and can keep the filesystem busy for a long time. The kernel must be new enough to support the SCRUB_METADATA ioctl.

If errors are found and cannot be repaired, the filesystem must be unmounted and repaired.

# SEE ALSO

**xfs_repair**(8) and **xfs_scrub**(8).
