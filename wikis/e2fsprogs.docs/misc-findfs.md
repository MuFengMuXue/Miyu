# NAME

findfs - Find a file system by label or UUID

# SYNOPSIS

**findfs** **LABEL=***label*

**findfs** **UUID=***uuid*

# DESCRIPTION

**findfs** will search the disks in the system looking for a file system which has a label matching *label* or a UUID equal to *uuid*. If the file system is found, the device name for the file system will be printed on stdout.

# AUTHOR

**findfs** was written by Theodore Ts'o (tytso@mit.edu).

# AVAILABILITY

**findfs** is part of the e2fsprogs package and is available from http://e2fsprogs.sourceforge.net.

# SEE ALSO

**fsck**(8)
