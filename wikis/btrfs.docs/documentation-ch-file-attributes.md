# Documentation / Ch File Attributes

The btrfs filesystem supports setting file attributes or flags. Note there are old and new interfaces, with confusing names. The following list should clarify that:

- *attributes*: `chattr(1)` or `lsattr(1)` utilities (the ioctls are FSIOC_GETFLAGS and FSIOC_SETFLAGS), due to the ioctl names the attributes are also called flags
- *xflags*: to distinguish from the previous, it's extended flags, with tunable bits similar to the attributes but extensible and new bits will be added in the future (the ioctls are FSIOC_FSGETXATTR and FSIOC_FSSETXATTR but they are not related to extended attributes that are also called xattrs), there's no standard tool to change the bits, there's support in `xfs_io(8)` as command **xfs_io -c chattr**

Attributes have constraints associated and not all combinations can be set, the order of setting them also matters. Most attributes apply to files and directories but the semantics may differ. For directories the attribute may only mean to set this attribute to all new files (*inheritable* in the list below). Some attributes need root privileges to be set.

# Attributes

a
(file, dir, root) *append only*, new writes are always written at the end of the file

A
(file, dir) *no atime updates*

c
(file, dir, inherited) *compress data*, all data written after this attribute is set will be compressed. Please note that compression is also affected by the mount options or the parent directory attributes.

When set on a directory, all newly created files will inherit this attribute. This attribute cannot be set with 'm' at the same time.

C
(file, dir, inherited) *no copy-on-write*, file data modifications are done in-place

When set on a directory, all newly created files will inherit this attribute.

> [!NOTE]
> Due to implementation limitations, this flag can be set/unset only on empty files.

d
(file) *no dump*, makes sense with 3rd party tools like `dump(8)`, on BTRFS the attribute can be set/unset but no other special handling is done

D
(dir) *synchronous directory updates*, for more details search `open(2)` for *O_SYNC* and *O_DSYNC*

i
(file, dir, root) *immutable*, no file data and metadata changes allowed even to the root user as long as this attribute is set (obviously the exception is unsetting the attribute)

m
(file, dir) *no compression*, permanently turn off compression on the given file. Any compression mount options will not affect this file. (`chattr(1)` support added in 1.46.2)

When set on a directory, all newly created files will inherit this attribute. This attribute cannot be set with *c* at the same time.

S
(file) *synchronous updates*, for more details search `open(2)` for *O_SYNC* and *O_DSYNC*

V
(file, read-only) *fs-verity enabled* on the file

No other attributes are supported. For the complete list please refer to the `chattr(1)` manual page.

# XFLAGS

There's an overlap of letters assigned to the bits with the attributes, this list refers to what `xfs_io(8)` provides:

i
*immutable*, same as the attribute

a
*append only*, same as the attribute

s
*synchronous updates*, same as the attribute *S*

A
*no atime updates*, same as the attribute

d
*no dump*, same as the attribute
