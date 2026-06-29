## Name

systemd-fsck@.service, systemd-fsck-root.service, systemd-fsck-usr.service, systemd-fsck — File system checker logic

## Synopsis

|                                 |
|---------------------------------|
| `systemd-fsck@.service`         |
| `systemd-fsck-root.service`     |
| `systemd-fsck-usr.service`      |
| `/usr/lib/systemd/systemd-fsck` |

## Description

`systemd-fsck@.service`, `systemd-fsck-root.service`, and `systemd-fsck-usr.service` are services responsible for file system checks. They are instantiated for each device that is configured for file system checking. `systemd-fsck-root.service` and `systemd-fsck-usr.service` are responsible for file system checks on the root and /usr file system, respectively, but only if the root filesystem was not checked in the initrd. `systemd-fsck@.service` is used for all other file systems and for the root file system in the initrd.

These services are started at boot if `passno` in `/etc/fstab` for the file system is set to a value greater than zero, but only if it is also configured to be mounted at boot (i.e. without "`noauto`" option). The file system check for root is performed before the other file systems. Other file systems may be checked in parallel, except when they are on the same rotating disk.

`systemd-fsck` does not know any details about specific filesystems, and simply executes file system checkers specific to each filesystem type (`fsck.`*`type`*). These checkers will decide if the filesystem should actually be checked based on the time since last check, number of mounts, unclean unmount, etc.

`systemd-fsck-root.service` and `systemd-fsck-usr.service` will activate `reboot.target` if fsck(8) returns the "System should reboot" condition, or `emergency.target` if **fsck** returns the "Filesystem errors left uncorrected" condition.

`systemd-fsck@.service` will fail if fsck(8) returns either the "System should reboot" or the "Filesystem errors left uncorrected" condition. For filesystems listed in `/etc/fstab` without "`nofail`" or "`noauto`" options, `local-fs.target` will then activate `emergency.target`.

## Kernel Command Line

**systemd-fsck** understands these kernel command line parameters:

`fsck.mode=`  
One of "`auto`", "`force`", "`skip`". Controls the mode of operation. The default is "`auto`", and ensures that file system checks are done when the file system checker deems them necessary. "`force`" unconditionally results in full file system checks. "`skip`" skips any file system checks.

Added in version 186.

`fsck.repair=`  
One of "`preen`", "`yes`", "`no`". Controls the mode of operation. The default is "`preen`", and will automatically repair problems that can be safely fixed. "`yes`" will answer yes to all questions by fsck and "`no`" will answer no to all questions.

Added in version 213.

## Credentials

**systemd-fsck** supports the service credentials logic as implemented by `ImportCredential=`/`LoadCredential=`/`SetCredential=` (see systemd.exec(5) for details). The following credentials are used when passed in:

`fsck.mode`, `fsck.repair`  
The contents of the credentials are parsed as same as the kernel command line options with the same name. See above for more details.

Added in version 258.

Note that by default the `systemd-fsck@.service`, `systemd-fsck-root.service`, and `systemd-fsck-usr.service` unit files are set up to inherit both `fsck.mode` and `fsck.repair` credentials from the service manager.

## See Also

systemd(1), fsck(8), systemd-quotacheck@.service(8), fsck.btrfs(8), fsck.cramfs(8), fsck.ext4(8), fsck.fat(8), fsck.hfsplus(8), fsck.minix(8), fsck.ntfs(8), fsck.xfs(8)
