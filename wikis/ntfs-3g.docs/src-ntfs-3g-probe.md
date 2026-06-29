# NAME

ntfs-3g.probe - Probe an NTFS volume mountability

# SYNOPSIS

**ntfs-3g.probe** *\<--readonly\|--readwrite\>* *volume*

# DESCRIPTION

The **ntfs-3g.probe** utility tests a volume if it's NTFS mountable read-only or read-write, and exits with a status value accordingly. The *volume* can be a block device or image file.

# OPTIONS

Below is a summary of the options that **ntfs-3g.probe** accepts.

**-r, --readonly**
Test if the volume can be mounted read-only.

**-w, --readwrite**
Test if the volume can be mounted read-write.

**-h, --help**
Display help and exit.

# EXAMPLE

Test if /dev/sda1 can be mounted read-write:

> **ntfs-3g.probe --readwrite /dev/sda1**

# EXIT CODES

The exit codes are as follows:

0.  Volume is mountable.

1.  Syntax error, command line parsing failed.

2.  The volume doesn't have a valid NTFS.

3.  Inconsistent NTFS, hardware or device driver fault, or unsetup SoftRAID/FakeRAID hardware.

4.  The NTFS partition is hibernated.

5.  The volume was not cleanly unmounted.

6.  The volume is already exclusively opened and in use by a kernel driver or software.

7.  Unsetup SoftRAID/FakeRAID hardware.

8.  Unknown reason.

9.  Not enough privilege to mount.

10. Out of memory.

11. Unclassified FUSE error.

# KNOWN ISSUES

Please see

> https://github.com/tuxera/ntfs-3g/wiki/NTFS-3G-FAQ

for common questions and known issues. If you think you have found an undocumented problem in the latest release of the software then please post an ntfs-3g issue describing it in detail so that the development team can be aware of the issue and take care of it:

> https://github.com/tuxera/ntfs-3g/issues

# AUTHORS

**ntfs-3g.probe** was written by Szabolcs Szakacsits.

# THANKS

Alon Bar-Lev has integrated the utility into the NTFS-3G build process and tested it with Erik Larsson before the public release.

# SEE ALSO

**ntfs-3g**(8)
