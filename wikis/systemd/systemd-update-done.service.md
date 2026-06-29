## Name

systemd-update-done.service, systemd-update-done — Mark `/etc/` and `/var/` as fully updated

## Synopsis

`systemd-update-done.service`

`/usr/lib/systemd/systemd-update-done`

## Description

`systemd-update-done.service` is a service that is invoked as part of the first boot after the vendor operating system resources in `/usr/` have been updated. This is useful to implement offline updates of `/usr/` which might require updates to `/etc/` or `/var/` on the following boot.

`systemd-update-done.service` updates the file modification time (mtime) stored in and "on" the files `/etc/.updated` and `/var/.updated` to the modification time of the `/usr/` directory, unless the stamp files are already newer. (The timestamp is stored as the mtime field on the file, but also *in* the file to support filesystems that do not store full timestamp precision.)

Services that shall run after offline upgrades of `/usr/` should order themselves before `systemd-update-done.service`, and use the `ConditionNeedsUpdate=` (see systemd.unit(5)) condition to make sure to run when `/etc/` or `/var/` are older than `/usr/` according to the modification times of the files described above. This requires that updates to `/usr/` are always followed by an update of the modification time of `/usr/`, for example by invoking touch(1) on it.

Note that if the `systemd.condition_needs_update=` kernel command line option is used it overrides the `ConditionNeedsUpdate=` unit condition checks. In that case `systemd-update-done.service` will not reset the condition state until a follow-up reboot where the kernel switch is not specified anymore.

## Options

The following options are understood:

`--root=`*`root`*  
Takes a directory path as an argument. The program will operate on paths below the specified root directory.

Added in version 258.

`-h`, `--help`  
Print a short help text and exit.

## See Also

systemd(1), systemd.unit(5), touch(1)
