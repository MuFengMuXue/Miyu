## Name

localtime — Local timezone configuration file

## Synopsis

`/etc/localtime` -\> `../usr/share/zoneinfo/…`

## Description

The `/etc/localtime` file configures the system-wide timezone of the local system that is used by applications for presentation to the user. It should be an absolute or relative symbolic link pointing to `/usr/share/zoneinfo/`, followed by a timezone identifier such as "`Europe/Berlin`" or "`Etc/UTC`". The resulting link should lead to the corresponding binary tzfile(5) timezone data for the configured timezone.

Because the timezone identifier is extracted from the symlink target name of `/etc/localtime`, this file may not be a normal file or hardlink.

If `/etc/localtime` is missing, the default "`UTC`" timezone is used.

The timezone may be overridden for individual programs by using the `$TZ` environment variable. See environ(7).

You may use timedatectl(1) to change the settings of this file from the command line during runtime. Use systemd-firstboot(1) to initialize the time zone on mounted (but not booted) system images.

## See Also

systemd(1), tzset(3), localtime(3), timedatectl(1), systemd-timedated.service(8), systemd-firstboot(1)
