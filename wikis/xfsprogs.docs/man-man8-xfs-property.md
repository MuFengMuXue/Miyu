# NAME

xfs_property - examine and edit properties about an XFS filesystem

# SYNOPSIS

**xfs_property** *target* **get** *name*...
**xfs_property** *target* **list \[ -v \]**
**xfs_property** *target* **set** *name=value*...
**xfs_property** *target* **remove** *name*...
**xfs_property -V**

# DESCRIPTION

**xfs_property** retrieves, lists, sets, or removes properties of an XFS filesystem. Filesystem properties are root-controlled attributes set on the root directory of the filesystem to enable the system administrator to coordinate with userspace programs.

*target* is one of: the root directory of a mounted filesystem; a block device containing an XFS filesystem; or a regular file containing an XFS filesystem.

# OPTIONS

**-V**
Print the version number and exits.

# COMMANDS

**get**
*name*... Prints the values of the given filesystem properties.

**list**
Lists the names of all filesystem properties. If the **-v** flag is specified, prints the values as well.

**set**
*name*=*value*... Sets the given filesystem properties to the specified values and prints what was set.

**remove**
*name*... Unsets the given filesystem properties.

# FILESYSTEM PROPERTIES

Known filesystem properties for XFS are:

*autofsck* See **xfs_scrub**(8) for more information.
