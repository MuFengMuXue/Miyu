## Name

systemd-mstack, mount.mstack — Mstack Discoverable Disk Images (DDIs)

## Synopsis

`systemd-mstack` \[OPTIONS...\] *`IMAGE`*

`systemd-mstack` \[OPTIONS...\] \[--mount\] *`IMAGE`* *`PATH`*

`systemd-mstack` \[OPTIONS...\] \[--umount\] *`PATH`*

## Description

**systemd-mstack** is a tool for introspecting and interacting with `.mstack/` mount stack directories, as described in systemd.mstack(7). It supports three different operations:

1.  Show general mount stack information, including all described "`overlayfs`" layers and bind mounts.

2.  Mount a mount stack to a local directory.

3.  Unmount a mount stack from a local directory.

The **systemd-mstack** command may be invoked as **mount.mstack** in which case it implements the mount(8) "external helper" interface. This ensures mount stack directories compatible with **systemd-mstack** can be mounted directly by **mount** and fstab(5). For details see below.

In place of the image path a "`.v/`" versioned directory may be specified, see systemd.v(7) for details.

## Commands

If neither of the command switches listed below are passed the specified mount stack is opened and general information about it is shown, including a list of all defined layers.

`--mount`, `-m`  
Mount the specified mount stack to the specified directory.

To unmount a mount stack directory mounted like this use the `--umount` operation.

Note that this functionality is also available in mount(8) via a command such as **mount -t mstack mystack.mstack targetdir/**, as well as in fstab(5). For details, see below.

Added in version 260.

`-M`  
This is a shortcut for `--mount --mkdir`.

Added in version 260.

`--umount`, `-u`  
Unmount a mount stack from the specified directory. This command expects one argument: a directory where mount stack was mounted.

All mounted mounts will be recursively unmounted

Added in version 260.

`-U`  
This is a shortcut for `--umount --rmdir`.

Added in version 260.

`-h`, `--help`  
Print a short help text and exit.

`--version`  
Print a short version string and exit.

## Options

The following options are understood:

`--read-only`, `-r`  
Operate in read-only mode. By default, `--mount` will establish writable mount points. If this option is specified they are established in read-only mode instead.

Added in version 260.

`--mkdir`  
If combined with `--mount` the directory to mount the mount stack to is created if it is missing. Note that the directory is not automatically removed when the mount stack is unmounted again.

Added in version 260.

`--rmdir`  
If combined with `--umount` the specified directory where the mount stack is mounted is removed after unmounting it.

Added in version 260.

`--image-policy=`*`policy`*  
Takes an image policy string as argument, as per systemd.image-policy(7). The policy is enforced when operating on the disk image specified via `--image=`, see above. If not specified, defaults to the "`*`" policy, i.e. all recognized file systems in the image are used.

`--image-filter=`*`filter`*  
Takes an image filter string as argument, as per systemd.image-filter(7). The filter is taken into consideration when operating on the disk image specified via `--image=`, see above. If not specified no filtering is applied.

`--no-pager`  
Do not pipe output into a pager.

`--no-legend`  
Do not print the legend, i.e. column headers and the footer with hints.

`--json=`*`MODE`*  
Shows output formatted as JSON. Expects one of "`short`" (for the shortest possible output without any redundant whitespace or line breaks), "`pretty`" (for a pretty version of the same, with indentation and line breaks) or "`off`" (to turn off JSON output, the default).

## Exit status

On success, 0 is returned, a non-zero failure code otherwise.

## Invocation as **/sbin/mount.mstack**

The **systemd-mstack** executable may be symlinked to `/sbin/mount.mstack`. If invoked through that it implements mount(8)'s "external helper" interface for the (pseudo) file system type "`mstack`". This means conformant mount stack directories may be mounted directly via

``` programlisting
# mount -t mstack mystack.mstack targetdir/
```

in a fashion mostly equivalent to:

``` programlisting
# systemd-mstack --mount mystack.mstack targetdir/
```

Note that since a single mount stack may contain multiple mount points it should later be unmounted with **umount -R targetdir/**, for recursive operation.

This functionality is particularly useful to mount mount stacks automatically at boot via simple `/etc/fstab` entries. For example:

``` programlisting
/path/to/mystack.nspawn /images/mystack/ mstack defaults 0 0
```

When invoked this way the mount options "`ro`", "`rw`" map to the corresponding options listed above (i.e. `--read-only`).

## See Also

systemd(1), systemd.mstack(7), systemd-nspawn(1), systemd.exec(5), mount(8), umount(8)
