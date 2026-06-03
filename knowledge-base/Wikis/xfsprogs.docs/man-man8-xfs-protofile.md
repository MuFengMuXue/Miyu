# NAME

xfs_protofile - create a protofile for use with mkfs.xfs

# SYNOPSIS

**xfs_protofile** *path* \[ *paths...* \]
**xfs_protofile -V**

# DESCRIPTION

**xfs_protofile** walks a directory tree to generate a protofile. The protofile format is specified in the **mkfs.xfs**(8) manual page and is derived from 3rd edition Unix.

# OPTIONS

*path*
Create protofile directives to copy this path into the root directory. If the path is a directory, protofile directives will be emitted to replicate the entire subtree as a subtree of the root directory. If the path is a not a directory, protofile directives will be emitted to create the file as an entry in the root directory. The first path must resolve to a directory.

# BUGS

Filenames cannot contain spaces. Extended attributes are not copied into the filesystem.
