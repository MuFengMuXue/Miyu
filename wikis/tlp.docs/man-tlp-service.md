# NAME

tlp.service - Initialize power saving at boot and cleanup upon shutdown

# SYNOPSIS

**tlp.service**

# DESCRIPTION

tlp.service executes the following tasks:

 1.
System boot-up: switch or restore radio states, apply power saving settings and charge thresholds.

 2.
System shutdown: save radio states and cleanup.

# FILES

*/lib/systemd/system-sleep/tlp*

> Applies power saving settings upon system suspend and resume.

# SEE ALSO

**tlp**(8).

# NOTES

Do *not* employ tlp.service to refresh power saving settings after a configuration change. Use **tlp start** instead.

# SEE ALSO

**tlp**(8).

# BUGS

Report bugs to: \<https://github.com/linrunner/TLP/issues\>.

# AUTHOR

\(c\) 2026 Thomas Koch \<linrunner at gmx.net\>
