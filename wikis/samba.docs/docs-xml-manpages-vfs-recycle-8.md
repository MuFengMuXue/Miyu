# Docs Xml / Manpages / Vfs recycle.8

vfs_recycle

8

Samba

System Administration tools

vfs_recycle

Samba VFS recycle bin

vfs objects = recycle

# DESCRIPTION

This VFS module is part of the `samba(7)` suite.

The `vfs_recycle` intercepts file deletion requests and moves the affected files to a temporary repository rather than deleting them immediately. This gives the same effect as the Recycle Bin on Windows computers.

The Recycle Bin will not appear in Windows Explorer views of the network file system (share) nor on any mapped drive. Instead, a directory called .recycle will be automatically created when the first file is deleted and recycle:repository is not configured. If recycle:repository is configured, the name of the created directory depends on recycle:repository. Users can recover files from the recycle bin. If the recycle:keeptree option has been specified, deleted files will be found in a path identical with that from which the file was deleted.

This module is stackable.

# OPTIONS

recycle:repository = PATH
Path of the directory where deleted files should be moved.

If this option is not set, the default path .recycle is used.

recycle:directory_mode = MODE
Set MODE to the octal mode the recycle repository should be created with. The recycle repository will be created when first file is deleted. If recycle:subdir_mode is not set, MODE also applies to subdirectories.

If this option is not set, the default mode 0700 is used.

recycle:subdir_mode = MODE
Set MODE to the octal mode with which sub directories of the recycle repository should be created.

If this option is not set, subdirectories will be created with the mode from recycle:directory_mode.

recycle:keeptree = BOOL
Specifies whether the directory structure should be preserved or whether the files in a directory that is being deleted should be kept separately in the repository.

recycle:versions = BOOL
If this option is True, two files with the same name that are deleted will both be kept in the repository. Newer deleted versions of a file will be called "Copy \#x of filename".

recycle:touch = BOOL
Specifies whether a file's access date should be updated when the file is moved to the repository.

recycle:touch_mtime = BOOL
Specifies whether a file's last modified date should be updated when the file is moved to the repository.

recycle:minsize = BYTES
Files that are smaller than the number of bytes specified by this parameter will not be put into the repository.

recycle:maxsize = BYTES
Files that are larger than the number of bytes specified by this parameter will not be put into the repository.

recycle:exclude = LIST
List of files that should not be put into the repository when deleted, but deleted in the normal way. Wildcards such as \* and ? are supported.

recycle:exclude_dir = LIST
List of directories whose files should not be put into the repository when deleted, but deleted in the normal way. Wildcards such as \* and ? are supported.

recycle:noversions = LIST
Specifies a list of paths (wildcards such as \* and ? are supported) for which no versioning should be used. Only useful when recycle:versions is enabled.

# EXAMPLES

Move files "deleted" on `share` to `/data/share/.recycle` instead of deleting them:


        /data/share
        recycle
        .recycle
        yes
        yes

# VERSION

This man page is part of version of the Samba suite.

# AUTHOR

The original Samba software and related utilities were created by Andrew Tridgell. Samba is now developed by the Samba Team as an Open Source project similar to the way the Linux kernel is developed.
