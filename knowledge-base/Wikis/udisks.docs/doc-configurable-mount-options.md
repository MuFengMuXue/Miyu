# Configurable mount options

UDisks comes with a set of predefined mount options for common filesystems used for dynamic mountpoints (i.e., excluding `/etc/fstab` records). This selection has been made with focus on the primary project target: end users, consumers and workstations mostly working with removable media.

Typically acting as a storage management backend for desktop environments running on user level, the selection comes with a security and data consistency in mind. In other words, user must not be able to access or alter other user's data by allowing insecure mount options or damage the filesystem by experimental filesystem options. For removable media it usually involves synchronous writes to prevent data loss by accidental physical removal of the device while background filesystem sync is running yet the user interface provided no indication of such process.

Technically UDisks carries a set of allowed mount options for well known filesystems and related set of default options that are subset of the allowed and are always passed to the mount command. Additional mount options can be specified via the `options` parameter of the [org.freedesktop.UDisks2.Filesystem.Mount()](#gdbus-method-org-freedesktop-UDisks2-Filesystem.Mount) method call. These options however need to be subset of allowed mount options for the given filesystem type.

Since the 2.9.0 UDisks release a new way of overriding builtin set of mount options is supported. This is primarily targeted to sysadmins with system-wide write access (e.g. `/etc/udisks2` or udev rules) and essentially transfers responsibility for security and data consistency to their side. Please keep in mind that wrong combination of options or bad understanding of override levels may lead to inability to mount or false sense of security. Also note that block devices having corresponding records in `/etc/fstab` are excluded from the overrides as the mount options are fully taken from such records just like before.

No public API has changed, overrides can be defined either via config files or via specific udev rules. UDisks computes mount options on every [Mount()](#gdbus-method-org-freedesktop-UDisks2-Filesystem.Mount) method call, no need to restart or poke the daemon.

## Filesystem signature vs. filesystem driver

The configurable mount options definition introduced in UDisks 2.9.0 considered the filesystem signature and corresponding filesystem driver an equal definition. Matching filesystem signature identifier was used as a filesystem type for mounting, as is common for most widely used filesystems.

This has been changed in UDisks 2.10.0 and the configurable mount options gained ability to specify filesystem driver (i.e. a kernel or fuse driver) for a particular filesystem signature, along with a definition of filesystem driver priorities if necessary. In the following paragraphs the term *'filesystem signature'* typically means *'filesystem type'* unless stated otherwise.

## Basic definitions

For the reference this is what the builtin set of options looks like:


Typically for each filesystem signature a pair of two sets are defined: `_allow` and `_defaults`. The syntax of each record is `fs_signature[:fs_driver]_key=value1,value2,...` where `fs_signature` denotes the on-disk filesystem signature as detected by `udev/blkid`, an optional `fs_driver` separated by the '`:`' character indicates the filesystem type (*driver*) to use for the mount call and the `key` is one of the `_allow`, `_defaults` or `_drivers` set of values. In case the optional `fs_driver` part is not specified, it is expected that the name of the filesystem drive equals to filesystem signature, as usual.

The `_allow` set define mount options ever allowed and considered, the `_defaults` are the target options to use that are then (after further amendmends) passed to the mount command.

The `_defaults` always need to be a subset of `_allow`. The `_defaults` options are also merged with any extra options passed via the [Mount()](#gdbus-method-org-freedesktop-UDisks2-Filesystem.Mount) method call.

Optionally, the `_drivers` set defines filesystem driver priorities for the particular filesystem signature to use for the actual mount call, from highest to lowest. Only the `fs_driver` part of the `fs_signature[:fs_driver]_key` triplet should be specified here, separated by comma.

The [Mount()](#gdbus-method-org-freedesktop-UDisks2-Filesystem.Mount) method call will then attempt to mount the filesystem using computed options defined for the particular filesystem driver separately. Multiple mount attempts are made where in case the filesystem driver is unknown to the kernel, the next one in the list is tried until the operation succeeds. This might potentially lead to extra error messages in the system log from the unsuccessful tries. Distributors are suggested to tweak the priorities according to the supported filesystem drivers. To take advantage of this functionality the `_drivers` record needs to be present, otherwise the extra filesystem driver definitions are ignored and only the base filesystem signature definition matching the filesystem driver name is taken in account.

Other than the filesystem signature specific options there's also a group of general options that are always merged with fs-specific ones. These include general options like `rw`, `ro`, etc. Let's refer to them as `any` filesystem options for simplicity in the further text. The result of option set stacking, overrides and merging is referred to as *(resulting) computed set of options*.

Apart from the final computed options UDisks always adds the following options due to security concerns: `nodev`, `nosuid`, `uhelper=udisks2` no matter if included in `_allow` or not. These are hardcoded and can't be changed.

Options that are not allowed in the computed `_allow` set will fail the mount operation with an error.

## Unprivileged mounts, UID and GID passing

UDisks daemon typically runs as root and spawns the mount command with root privileges while processing requests from unprivileged clients and it needs a way to set proper permissions for the mounted filesystem. This is usually done by passing the `uid` and `gid` mount options that common filesystems honour. UDisks take the D-Bus method caller effective UID and finds its corresponding primary GID.

Also a `uhelper=udisks2` mount option is added automatically to indicate the umount command to use UDisks again for unmounting when called by an unprivileged user.

To allow flexibility in mount option naming, two special values are defined as placeholders for aforementioned IDs: `$UID` and `$GID`. These are supposed to be defined as values for specific mount options (typically `uid` and `gid`) within the `_allow` set and are then replaced with numerical values in the late phase of mount option computation.

It's worth noting that there are few more options whose arguments are being replaced by computed values: `mode` and `dmode`. These options are hardcoded at the moment and its values depend on the udev `UDISKS_FILESYSTEM_SHARED` attribute presence on the block device.

## Option set specifics

Option sets are composite strings of mount options with or without arguments separated by commas. There's generally no difference from an option string commonly used with the mount command. UDisks brings a couple of specifics for greater flexibility.

As explained above any particular mount option either defined in the `_defaults` set or passed as an extra argument via the [Mount()](#gdbus-method-org-freedesktop-UDisks2-Filesystem.Mount) method call need to be allowed by the `_allow` set of mount options. There's however a difference in how the option is allowed and what arguments are valid.

When a considered option is defined with either of the `$UID` or `$GID` values within the `_allow` set (see previous chapter), special rules apply. In case the value of a considered option is the `$UID`/`$GID` placeholder (as is the case of builtin set of options) or no value is specified at all (e.g. the `uid=` string), the [Mount()](#gdbus-method-org-freedesktop-UDisks2-Filesystem.Mount) method caller UID or GID is automatically added. In case a particular value is present (e.g. `uid=1001`) it is only allowed when the caller UID matches the option value.

In case a considered option is specified explicitly with a value within the `_allow` set no other checks are performed and this `option=value` pair is always allowed. This even bypasses UID and GID checks, except of the `$UID` or `$GID` strings.

This permits various combinations of caller mount options such as `uid=$UID,uid=ignore` for UDF filesystem where the `uid=ignore` mount options is always allowed yet standard checks (`uid=$UID`) for numerical UID values are still preserved. Similarly, certain numeric UID/GID values may be explicitly allowed this way, allowing non-privileged callers to use predefined IDs (e.g. `uid=1000,uid=1500,uid=ignore` within `_allow`). This also allows to specify arbitrary values permitted, where each pair needs to be specified separately, i.e. `iocharset=utf8,iocharset=iso8859-1,iocharset=iso8859-2`.

Allowed option defined with no value is treated as any value is permitted but only if passed all checks described above. There's generally no difference between `option` and `option=` (i.e. an empty value) in such definitions.

## The config file syntax

A sample config file showing rich syntax:

    [defaults]
    # common options, applied to any filesystem, always merged with specific filesystem type options
    defaults=ro
    allow=exec,noexec,nodev,nosuid,atime,noatime,nodiratime,ro,rw,sync,dirsync,noload

    # specific filesystem type options
    vfat_defaults=uid=$UID,gid=$GID,shortname=mixed,utf8=1,showexec,flush
    vfat_allow=uid=$UID,gid=$GID,flush,utf8,shortname,umask,dmask,fmask,codepage,iocharset,usefree,showexec
    ntfs_defaults=uid=$UID,gid=$GID,windows_names
    ntfs_allow=uid=$UID,gid=$GID,umask,dmask,fmask,locale,norecover,ignore_case,windows_names

    [/dev/disk/by-uuid/18afd8f0-0d86-4d96-8de0-5f92d2ee9800]
    vfat_defaults=uid=$UID,gid=$GID,noexec

    [/dev/disk/by-label/EFI]
    vfat_defaults=noexec,umask=111,dmask=000

The format of the configuration file is an INI-style key-value file parseable by [`GKeyFile`](https://developer.gnome.org/glib/stable/glib-Key-value-file-parser.html). The default location of the file unless specified otherwise during build time is `/etc/udisks2/mount_options.conf`. Sample config file is shipped along the source code.

The config file may contain multiple groups with a common `[defaults]` group. One of the new features is an ability to override mount options for particular block device, matched by the block device path. In such case the name of the group is the block device path. It's strongly encouraged to use stable block device identifiers (that is e.g. `/dev/disk/by-*`). No wildcards or glob expansion is performed, for fine-grained matching please use overrides through the custom udev rules. This shouldn't be abused to weaken security requirements though, it's quite easy to fake storage identifiers, more so on removable media.

## udev rules overrides

Another possibility of overriding mount options is from the udev rules. This brings the flexibility of fine-grained matching by various identifiers and even using external helpers for identification. It's also a less error-prone way than matching by block device symlinks at the config file level.

This is a separate level of overrides that is positioned on top of the config file level, i.e. definitions coming from udev rules will override respective keys from both the config file level and the base builtin mount options. The override mechanism and rules are no different from the config file level `[defaults]` group. There's just a slight syntactic difference to align with usual udev `ENV` naming conventions, consisting of the `UDISKS_MOUNT_OPTIONS_` key prefix.

Depending on your distribution specifics there are usually several paths designated for placing custom udev rules, with `/etc/udev/rules.d/` and `/lib/udev/rules.d` being the common ones. It's strongly recommended to make the rules run last, by the `99-` filename prefix.

Sample udev rules may look as follows:

    # This file contains custom mount options for udisks 2.x
    #

    # Skip if not a block device or if requested by other rules
    #
    SUBSYSTEM!="block", GOTO="udisks_mount_options_end"
    ENV{DM_MULTIPATH_DEVICE_PATH}=="1", GOTO="udisks_mount_options_end"
    ENV{DM_UDEV_DISABLE_OTHER_RULES_FLAG}=="?*", GOTO="udisks_mount_options_end"


    # Additional mount options passed to udisksd to allow sysadmins to restrict mount to read-only or "noexec"
    # for example:
    #
    # ENV{UDISKS_MOUNT_OPTIONS_DEFAULTS}="ro,noexec"
    # ENV{UDISKS_MOUNT_OPTIONS_ALLOW}="exec,noexec,nodev,nosuid,atime,noatime,nodiratime,ro,sync,dirsync,noload"

    #
    # Use specific charset for FAT filesystems
    #
    # ENV{ID_FS_TYPE}=="vfat", \
    # ENV{UDISKS_MOUNT_OPTIONS_VFAT_DEFAULTS}="uid=$UID,gid=$GID,shortname=mixed,utf8=0,iocharset=iso8859-15,showexec,flush"

    #
    # Mount all USB devices read-only
    #
    # SUBSYSTEMS=="usb", ENV{ID_FS_USAGE}=="filesystem", ENV{UDISKS_MOUNT_OPTIONS_DEFAULTS}="ro"

    LABEL="udisks_mount_options_end"

## Levels of overrides

Levels from lower to higher:

- builtin options
- global config file (i.e.
  /etc/udisks2/mount_options.conf
  )
- udev rules

Higher level options always fully override lower levels.

While the builtin options are always present, upper levels are optional.

Each level may consist of a common group and block device specific groups.

## Rules computation

This is the most important part to understand as badly formulated options may lead to unforeseen consequences.

As a general rule, set of options from higher levels always fully replace (*cover*, *override*) options from lower levels. This works on per-set basis, i.e. separately for each of the `_allow` and `_defaults` sets. Please pay attention to allowance of the mount options overridden in the `_defaults` set at a given level without overriding the `_allow` set at the same place - lower levels may not allow all the options.

First, overrides are computed within each level. At a given level, block device specific options take higher priority over the common options (the `[defaults]` group) and fully override them.

As a second step, overrides are computed vertically across all levels, from higher down to lower ones, again separately per-set basis. At this point, there are no block device specific options as they have been computed in the previous step.

The filesystem type specific options and common options (`any`) are computed separately across all levels per-set basis.

As a final step, when all sets are layered and computed onto a flat level, filesystem specific options and common options are merged together.

See the examples for further illustration.

## Examples

    [defaults]
    vfat_defaults=uid=$UID,gid=$GID,shortname=mixed,utf8=1,showexec
    ntfs_defaults=uid=$UID,gid=$GID


There's no way to specify subset addition or subtraction, particular sets need to be overridden fully. I.e. take the builtin mount options and remove/add options as you like.


    [defaults]
    defaults=ro
    allow=exec,noexec,nodev,nosuid,atime,noatime,nodiratime,ro,sync,dirsync,noload


Note that this doesn't apply to fstab mounts where mount options are fully respected.


    [defaults]
    defaults=ro
    allow=exec,noexec,nodev,nosuid,atime,noatime,nodiratime,ro,sync,dirsync,noload

    [/dev/disk/by-uuid/18afd8f0-0d86-4d96-8de0-5f92d2ee9800]
    defaults=
    allow=exec,noexec,nodev,nosuid,atime,noatime,nodiratime,ro,rw,sync,dirsync,noload


Note that this possesses a security risk as it's rather easy to fake commonly used identifiers like UUIDs, labels, etc.


    [defaults]
    defaults=ro
    allow=exec,noexec,nodev,nosuid,atime,noatime,nodiratime,ro,sync,dirsync,noload

    SUBSYSTEM!="block", GOTO="udisks_mount_options_end"
    ENV{DM_MULTIPATH_DEVICE_PATH}=="1", GOTO="udisks_mount_options_end"
    ENV{DM_UDEV_DISABLE_OTHER_RULES_FLAG}=="?*", GOTO="udisks_mount_options_end"

    ENV{ID_VENDOR}=="TrustyQualityInc", ENV{ID_MODEL}=="Unbreakable USB Stick", \
        ENV{ID_SERIAL}=="360014055282611e2e7440198ca5d8ceb", \
        ENV{UDISKS_MOUNT_OPTIONS_DEFAULTS}="rw", \
        ENV{UDISKS_MOUNT_OPTIONS_ALLOW}="exec,noexec,nodev,nosuid,atime,noatime,nodiratime,ro,rw,sync,dirsync,noload"

    LABEL="udisks_mount_options_end"

    [defaults]
    vfat_allow=uid=1001,uid=1005,gid=$GID,flush,utf8,shortname,umask,dmask,fmask,codepage,iocharset,usefree,showexec


Notice that the usual

uid=\$UID

option is missing from the

vfat_allow

set and specific allowed UIDs are the only ones defined. As the

vfat_defaults

set is not being overridden here and still carries the

uid=\$UID

mount option that gets automatically replaced by caller effective UID, the computed option value must match any of the

vfat_allow

options, thus the whole mount operation will be denied if the UIDs don't match.


    [defaults]
    # the legacy ntfs kernel driver and the ntfs-3g fuse driver
    # the usual case where the filesystem signature corresponds with the filesystem driver
    ntfs_defaults=uid=$UID,gid=$GID,windows_names
    ntfs_allow=uid=$UID,gid=$GID,umask,dmask,fmask,locale,norecover,ignore_case,windows_names,compression,nocompression,big_writes

    # ntfs3 kernel driver
    # different filesystem driver for a common filesystem signature
    ntfs:ntfs3_defaults=uid=$UID,gid=$GID
    ntfs:ntfs3_allow=uid=$UID,gid=$GID,umask,dmask,fmask,iocharset,discard,nodiscard,sparse,nosparse,hidden,nohidden,sys_immutable,nosys_immutable,showmeta,noshowmeta,prealloc,noprealloc

    # filesystem driver order for the specified filesystem signature
    # required to actually use the extra definitions
    ntfs_drivers=ntfs3,ntfs
