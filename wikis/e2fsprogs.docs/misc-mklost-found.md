# NAME

mklost+found - create a lost+found directory on a mounted ext2/ext3/ext4 file system

# SYNOPSIS

**mklost+found**

# DESCRIPTION

**mklost+found** is used to create a *lost+found* directory in the current working directory on an ext2/ext3/ext4 file system. There is normally a *lost+found* directory in the root directory of each file system.

**mklost+found** pre-allocates disk blocks to the *lost+found* directory so that when **e2fsck**(8) is being run to recover a file system, it does not need to allocate blocks in the file system to store a large number of unlinked files. This ensures that **e2fsck** will not have to allocate data blocks in the file system during recovery.

# OPTIONS

There are none.

# AUTHOR

**mklost+found** has been written by Remy Card \<Remy.Card@linux.org\>. It is currently being maintained by Theodore Ts'o \<tytso@alum.mit.edu\>.

# BUGS

There are none :-)

# AVAILABILITY

**mklost+found** is part of the e2fsprogs package and is available from http://e2fsprogs.sourceforge.net.

# SEE ALSO

**e2fsck**(8), **mke2fs**(8)
