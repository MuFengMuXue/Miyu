## Name

systemd-dissect, mount.ddi — Dissect Discoverable Disk Images (DDIs)

## Synopsis

`systemd-dissect` \[OPTIONS...\] *`IMAGE`*

`systemd-dissect` \[OPTIONS...\] \[--mount\] *`IMAGE`* *`PATH`*

`systemd-dissect` \[OPTIONS...\] \[--umount\] *`PATH`*

`systemd-dissect` \[OPTIONS...\] \[--attach\] *`IMAGE`*

`systemd-dissect` \[OPTIONS...\] \[--detach\] *`PATH`*

`systemd-dissect` \[OPTIONS...\] \[--list\] *`IMAGE`*

`systemd-dissect` \[OPTIONS...\] \[--mtree\] *`IMAGE`*

`systemd-dissect` \[OPTIONS...\] \[--with\] *`IMAGE`* \[*`COMMAND`*...\]

`systemd-dissect` \[OPTIONS...\] \[--copy-from\] *`IMAGE`* *`PATH`* \[*`TARGET`*\]

`systemd-dissect` \[OPTIONS...\] \[--copy-to\] *`IMAGE`* \[*`SOURCE`*\] *`PATH`*

`systemd-dissect` \[OPTIONS...\] \[--make-archive\] *`IMAGE`* \[*`TARGET`*\]

`systemd-dissect` \[OPTIONS...\] \[--discover\]

`systemd-dissect` \[OPTIONS...\] \[--validate\] *`IMAGE`*

`systemd-dissect` \[OPTIONS...\] \[--shift\] *`IMAGE`* *`UIDBASE`*

## Description

**systemd-dissect** is a tool for introspecting and interacting with file system OS disk images, specifically Discoverable Disk Images (DDIs). It supports four different operations:

1.  Show general OS image information, including the image's os-release(5) data, machine ID, partition information and more.

2.  Mount an OS image to a local directory. In this mode it will dissect the OS image and mount the included partitions according to their designation onto a directory and possibly sub-directories.

3.  Unmount an OS image from a local directory. In this mode it will recursively unmount the mounted partitions and remove the underlying loop device, including all the partition sub-devices.

4.  Copy files and directories in and out of an OS image.

The tool may operate on three types of OS images:

1.  OS disk images containing a GPT partition table envelope, with partitions marked according to the UAPI.2 Discoverable Partitions Specification.

2.  OS disk images containing just a plain file-system without an enveloping partition table. (This file system is assumed to be the root file system of the OS.)

3.  OS disk images containing a GPT or MBR partition table, with a single partition only. (This partition is assumed to contain the root file system of the OS.)

OS images may use any kind of Linux-supported file systems. In addition they may make use of LUKS disk encryption, and contain Verity integrity information. Note that qualifying OS images may be booted with systemd-nspawn(1)'s `--image=` switch, and be used as root file system for system service using the `RootImage=` unit file setting, see systemd.exec(5).

Note that the partition table shown when invoked without command switch (as listed below) does not necessarily show all partitions included in the image, but just the partitions that are understood and considered part of an OS disk image. Specifically, partitions of unknown types are ignored, as well as duplicate partitions (i.e. more than one per partition type), as are root and `/usr/` partitions of architectures not compatible with the local system. In other words: this tool will display what it operates with when mounting the image. To display the complete list of partitions use a tool such as fdisk(8).

The **systemd-dissect** command may be invoked as **mount.ddi** in which case it implements the mount(8) "external helper" interface. This ensures disk images compatible with **systemd-dissect** can be mounted directly by **mount** and fstab(5). For details see below.

In place of the image path a "`.v/`" versioned directory may be specified, see systemd.v(7) for details.

## Commands

If neither of the command switches listed below are passed the specified disk image is opened and general information about the image and the contained partitions and their use is shown.

`--mount`, `-m`  
Mount the specified OS image to the specified directory. This will dissect the image, determine the OS root file system — as well as possibly other partitions — and mount them to the specified directory. If the OS image contains multiple partitions marked with the UAPI.2 Discoverable Partitions Specification multiple nested mounts are established. This command expects two arguments: a path to an image file and a path to a directory where to mount the image.

To unmount an OS image mounted like this use the `--umount` operation.

When the OS image contains LUKS encrypted or Verity integrity protected file systems appropriate volumes are automatically set up and marked for automatic disassembly when the image is unmounted.

The OS image may either be specified as path to an OS image stored in a regular file or may refer to block device node (in the latter case, the block device must be the "whole" device, i.e. not a partition device). (The other supported commands described here support this, too.)

All mounted file systems are checked with the appropriate fsck(8) implementation in automatic fixing mode, unless explicitly turned off (`--fsck=no`) or read-only operation is requested (`--read-only`).

Note that this functionality is also available in mount(8) via a command such as **mount -t ddi myimage.raw targetdir/**, as well as in fstab(5). For details, see below.

Added in version 247.

`-M`  
This is a shortcut for `--mount --mkdir`.

Added in version 247.

`--umount`, `-u`  
Unmount an OS image from the specified directory. This command expects one argument: a directory where an OS image was mounted.

All mounted partitions will be recursively unmounted, and the underlying loop device will be removed, along with all its partition sub-devices.

Added in version 252.

`-U`  
This is a shortcut for `--umount --rmdir`.

Added in version 252.

`--attach`  
Attach the specified disk image to an automatically allocated loopback block device, and print the path to the loopback block device to standard output. This is similar to an invocation of **losetup --find --show --partscan**, but will validate the image as DDI before attaching, and derive the correct sector size to use automatically. Moreover, it ensures the per-partition block devices are created before returning and attempts to enable direct IO mode, if possible. Takes a path to a disk image file.

If combined with `--quiet` output of the block device name is suppressed.

Added in version 254.

`--detach`  
Detach the specified disk image from a loopback block device. This undoes the effect of `--attach` above. This expects either a path to a loopback block device as an argument, or the path to the backing image file. In the latter case, it will automatically determine the right device to detach.

Added in version 254.

`--list`, `-l`  
Prints the paths of all the files and directories in the specified OS image or directory to standard output.

Added in version 253.

`--mtree`  
Generates a BSD mtree(8) compatible file manifest of the specified disk image or directory. This is useful for comparing image contents in detail, including inode information and other metadata. While the generated manifest will contain detailed inode information, it currently excludes extended attributes, file system capabilities, MAC labels, chattr(1) file flags, btrfs(5) subvolume information, and various other file metadata. File content information is shown via a SHA256 digest. Additional fields might be added in future. Note that inode information such as link counts, inode numbers and timestamps is excluded from the output on purpose, as it typically complicates reproducibility.

Added in version 253.

`--with`  
Runs the specified command with the specified OS image mounted. This will mount the image to a temporary directory, switch the current working directory to it, and invoke the specified command line as child process. Once the process ends it will unmount the image again, and remove the temporary directory. If no command is specified a shell is invoked. The image is mounted writable, use `--read-only` to switch to read-only operation. The invoked process will have the `$SYSTEMD_DISSECT_ROOT` environment variable set, containing the absolute path name of the temporary mount point, i.e. the same directory that is set as the current working directory. It will also have the `$SYSTEMD_DISSECT_DEVICE` environment variable set, containing the absolute path name of the loop device the image was attached to.

Added in version 253.

`--copy-from`, `-x`  
Copies a file or directory from the specified OS image or directory into the specified location on the host file system. Expects three arguments: a path to an image file or directory, a source path (relative to the image's root directory) and a destination path (relative to the current working directory, or an absolute path, both outside of the image). If the destination path is omitted or specified as dash ("`-`"), the specified file is written to standard output. If the source path in the image file system refers to a regular file it is copied to the destination path. In this case, access mode, extended attributes and timestamps are copied as well, but file ownership is not. If the source path in the image refers to a directory, it is copied to the destination path, recursively with all containing files and directories, merging into existing directories and updating already existing files. In this case, the file ownership is copied too.

Added in version 247.

`--copy-to`, `-a`  
Copies a file or directory from the specified location in the host file system into the specified OS image or directory. Expects three arguments: a path to an image file or directory, a source path (relative to the current working directory, or an absolute path, both outside of the image) and a destination path (relative to the image's root directory). If the source path is omitted or specified as dash ("`-`"), the data to write is read from standard input. If the source path in the host file system refers to a regular file, it is copied to the destination path. In this case, access mode, extended attributes and timestamps are copied as well, but file ownership is not. If the source path in the host file system refers to a directory it is copied to the destination path, recursively with all containing files and directories, merging into existing directories and updating already existing files.. In this case, the file ownership is copied too.

As with `--mount` file system checks are implicitly run before the copy operation begins.

Added in version 247.

`--make-archive`  
Generates an archive file from the specified disk image. Expects two arguments: the path to the disk image and optionally the output archive file path. If the latter is omitted the archive is written to standard output. The archive file format is determined automatically from the specified output archive file name, e.g. any path suffixed with "`.tar.xz`" will result in an xz compressed UNIX tarball (if the path is omitted an uncompressed UNIX tarball is created). See libarchive(3) for a list of supported archive formats and compression schemes.

Added in version 256.

`--discover`  
Show a list of DDIs in well-known directories. This will show machine, portable service and system/configuration extension disk images in the usual directories `/usr/lib/machines/`, `/usr/lib/portables/`, `/usr/lib/confexts/`, `/var/lib/machines/`, `/var/lib/portables/`, `/var/lib/extensions/` and so on.

Added in version 253.

`--validate`  
Validates the partition arrangement of a disk image (DDI), and ensures it matches the image policy specified via `--image-policy=`, if one is specified. This parses the partition table and probes the file systems in the image, but does not attempt to mount them (nor to set up disk encryption/authentication via LUKS/Verity). It does this taking the configured image dissection policy into account. Since this operation does not mount file systems, this command – unlike all other commands implemented by this tool – requires no privileges other than the ability to access the specified file. Prints "OK" and returns zero if the image appears to be in order and matches the specified image dissection policy. Otherwise, prints an error message and returns non-zero.

Added in version 254.

`--shift`  
Recursively iterates through all inodes of the specified image and shifts the UIDs and GIDs the inodes are owned by into the specified UID range. Takes an image path and a UID base as parameter. The UID base can be specified numerically (in which case it must be a multiple of 65536, and either 0 or within the container or foreign UID range, as per Users, Groups, UIDs and GIDs on systemd Systems), or as the symbolic identifier "`foreign`" which is shorthand to the foreign UID base. This command is useful for preparing directory container images for unprivileged use. Note that this command is intended for images that use the 16bit UIDs/GIDs range only, and it always ignores the upper 16bit of the current UID/GID ownership, combining the lower 16 bit with the target UID base.

Use **systemd-dissect --shift /some/container/tree foreign** to shift a container image into the foreign UID range, or **systemd-dissect --shift /some/container/tree 0** to shift it to host UID range.

Added in version 258.

`-h`, `--help`  
Print a short help text and exit.

`--version`  
Print a short version string and exit.

## Options

The following options are understood:

`--read-only`, `-r`  
Operate in read-only mode. By default, `--mount` will establish writable mount points. If this option is specified they are established in read-only mode instead.

Added in version 247.

`--fsck=no`  
Turn off automatic file system checking. By default, when an image is accessed for writing (by `--mount` or `--copy-to`) the file systems contained in the OS image are automatically checked using the appropriate fsck(8) command, in automatic fixing mode. This behavior may be switched off using `--fsck=no`.

Added in version 247.

`--growfs=no`  
Turn off automatic growing of accessed file systems to their partition size, if marked for that in the GPT partition table. By default, when an image is accessed for writing (by `--mount` or `--copy-to`) the file systems contained in the OS image are automatically grown to their partition sizes, if bit 59 in the GPT partition flags is set for partition types that are defined by the UAPI.2 Discoverable Partitions Specification. This behavior may be switched off using `--growfs=no`. File systems are grown automatically on access if all of the following conditions are met:

1.  The file system is mounted writable

2.  The file system currently is smaller than the partition it is contained in (and thus can be grown)

3.  The image contains a GPT partition table

4.  The file system is stored on a partition defined by the Discoverable Partitions Specification

5.  Bit 59 of the GPT partition flags for this partition is set, as per specification

6.  The `--growfs=no` option is not passed.

Added in version 249.

`--mkdir`  
If combined with `--mount` the directory to mount the OS image to is created if it is missing. Note that the directory is not automatically removed when the disk image is unmounted again.

Added in version 247.

`--rmdir`  
If combined with `--umount` the specified directory where the OS image is mounted is removed after unmounting the OS image.

Added in version 252.

`--discard=`  
Takes one of "`disabled`", "`loop`", "`all`", "`crypto`". If "`disabled`" the image is accessed with empty block discarding turned off. If "`loop`" discarding is enabled if operating on a regular file. If "`crypt`" discarding is enabled even on encrypted file systems. If "`all`" discarding is unconditionally enabled.

Added in version 247.

`--in-memory`  
If specified an in-memory copy of the specified disk image is used. This may be used to operate with write-access on a (possibly read-only) image, without actually modifying the original file. This may also be used in order to operate on a disk image without keeping the originating file system busy, in order to allow it to be unmounted.

Added in version 253.

`--root-hash=`, `--root-hash-sig=`, `--verity-data=`  
Configure various aspects of Verity data integrity for the OS image. Option `--root-hash=` specifies a hex-encoded top-level Verity hash to use for setting up the Verity integrity protection. Option `--root-hash-sig=` specifies the path to a file containing a PKCS#7 signature for the hash. This signature is passed to the kernel during activation, which will match it against signature keys available in the kernel keyring. Option `--verity-data=` specifies a path to a file with the Verity data to use for the OS image, in case it is stored in a detached file. It is recommended to embed the Verity data directly in the image, using the Verity mechanisms in the UAPI.2 Discoverable Partitions Specification.

Added in version 247.

`--usr-hash=`, `--usr-hash-sig=`  
Similar to `--root-hash=` and `--root-hash-sig=`, but specifies hash and signature for the `/usr/` partition. Note that either the options for the root partition may be used or the ones for the `/usr/`, but not both in combination.

Added in version 258.

`--loop-ref=`  
Configures the "reference" string the kernel shall report as backing file for the loopback block device. While this is supposed to be a path or filename referencing the backing file, this is not enforced and the kernel accepts arbitrary free-form strings, chosen by the user. Accepts arbitrary strings up to a length of 63 characters. This sets the kernel's "`.lo_file_name`" field for the block device. Note this is distinct from the `/sys/class/block/loopX/loop/backing_file` attribute file that always reports a path referring to the actual backing file. The latter is subject to mount namespace translation, the former is not.

This setting is particularly useful in combination with the `--attach` command, as it allows later referencing the allocated loop device via `/dev/disk/by-loop-ref/…` symlinks. Example: first, set up the loopback device via **systemd-dissect attach --loop-ref=quux foo.raw**, and then reference it in a command via the specified filename: **cfdisk /dev/disk/by-loop-ref/quux**.

Added in version 254.

`--loop-ref-auto`  
Similar to `--loop-ref=`, but automatically derive the reference string from the specified backing filename, truncating it if necessary.

Added in version 258.

`--mtree-hash=no`  
If combined with `--mtree`, turns off inclusion of file hashes in the mtree output. This makes the `--mtree` faster when operating on large images.

Added in version 254.

`--copy-ownership=`  
Controls whether file ownership (user and group) is preserved when copying files with `--copy-from` or `--copy-to`. Takes a boolean, or `auto`. If "`yes`", ownership is always preserved. If "`no`", ownership is never preserved and the current user's UID/GID is used instead. If not specified or `auto`, ownership is preserved when copying directory trees, but not when copying individual regular files.

Added in version 260.

`--system`, `--user`  
When used together with `--discover` controls whether to search for images installed system-wide or in the user's directories in `$HOME`. If neither switch is specified, will search within both scopes.

Added in version 258.

`--all`  
If combined with `--discover`, also shows images that start with a dot, i.e. hidden images.

Added in version 258.

`--quiet`, `-q`  
If combined with `--attach`, suppresses output of the used loopback block device path.

Added in version 258.

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

On success, 0 is returned, a non-zero failure code otherwise. If the `--with` command is used the exit status of the invoked command is propagated.

## Invocation as **/sbin/mount.ddi**

The **systemd-dissect** executable may be symlinked to `/sbin/mount.ddi`. If invoked through that it implements mount(8)'s "external helper" interface for the (pseudo) file system type "`ddi`". This means conformant disk images may be mounted directly via

``` programlisting
# mount -t ddi myimage.raw targetdir/
```

in a fashion mostly equivalent to:

``` programlisting
# systemd-dissect --mount myimage.raw targetdir/
```

Note that since a single DDI may contain multiple file systems it should later be unmounted with **umount -R targetdir/**, for recursive operation.

This functionality is particularly useful to mount DDIs automatically at boot via simple `/etc/fstab` entries. For example:

``` programlisting
/path/to/myimage.raw /images/myimage/ ddi defaults 0 0
```

When invoked this way the mount options "`ro`", "`rw`", "`discard`", "`nodiscard`" map to the corresponding options listed above (i.e. `--read-only`, `--discard=all`, `--discard=disabled`). Mount options are *not* generically passed on to the file systems inside the images.

## Examples

**Example 1. Generate a tarball from an OS disk image (`--with`)**

``` programlisting
# systemd-dissect --with foo.raw tar cz . >foo.tar.gz
```

  

or alternatively just:

**Example 2. Generate a tarball from an OS disk image (`--make-archive`)**

``` programlisting
# systemd-dissect --make-archive foo.raw foo.tar.gz
```

  

## See Also

systemd(1), systemd-nspawn(1), systemd.exec(5), systemd.v(7), UAPI.2 Discoverable Partitions Specification, mount(8), umount(8), fdisk(8)
