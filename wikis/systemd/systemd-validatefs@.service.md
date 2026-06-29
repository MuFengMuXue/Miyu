## Name

systemd-validatefs@.service — Validate File System Mount Constraint Data

## Synopsis

`systemd-validatefs@.service`

`/usr/lib/systemd/systemd-validatefs` \[*`DEVICE`*\]

## Description

`systemd-validatefs@.service` is a system service template that can be instantiated for newly established mount points. It reads file system mount constraint data from the file system, and ensures the mount runtime setup matches it. If it doesn't the service fails, which effects an immediate reboot.

This functionality is supposed to ensure that trusted file systems cannot be used in a different context then what they were intended for. More specifically: in an systemd-gpt-auto-generator(8) based environment the file systems to mount are largely auto-discovered based on (unprotected) GPT partition table data. The mount constraint information can be used to validate the GPT partition data, based on the (protected) file system contents.

Specifically, the mount constraints are encoded in the following extended attributes on the root inode of the file systems:

1.  `user.validatefs.mount_point`: this extended attribute shall contain one or more absolute, normalized paths, separated by NUL bytes. If set and the specified file system is mounted to a location not matching any of the listed paths the validation check will fail.

2.  `user.validatefs.gpt_label`: this extended attribute may contain one or more free-form strings, separated by NUL bytes. If set, all backing partitions of the file system are checked against this list, and if any backing partition's label is not listed, the validation will fail. Note that there may be multiple backing partition in case of Verity setups, which combines a data and a hash partition.

3.  `user.validatefs.gpt_type_uuid`: this extended attribute may contain one or more GPT partition type UUIDs, formatted as string, separated by NUL bytes. As above, all backing partitions of the file system are checked against this list, and if none is matching the validation will fail.

The `systemd-validatefs@.service` unit is automatically pulled into the initial transaction by systemd-gpt-auto-generator(8) for all file systems it discovers and generates mounts for. systemd-fstab-generator(8) will do this for all mounts with the `x-systemd.validatefs` mount option in `/etc/fstab`.

The systemd-repart(8) tool generates these extended attributes automatically for the file systems it puts together, which may be controlled with the `AddValidateFS=` configuration option.

## Options

The `/usr/lib/systemd/system-validatefs` executable may also be invoked from the command line, where it expects a path to a mount and the following options:

`--root=`  
Takes an absolute path or the special string "`auto`". The specified path is removed as prefix from the specified mount point argument before the validation. If set to "`auto`" defaults to unspecified on the host and `/sysroot/` when run in initrd context, in order to validate the mount constraint data relative to the future file system root.

Added in version 258.

`-h`, `--help`  
Print a short help text and exit.

`--version`  
Print a short version string and exit.

## See Also

systemd(1), systemd-gpt-auto-generator(8), systemd-fstab-generator(8), systemd-repart(8)
