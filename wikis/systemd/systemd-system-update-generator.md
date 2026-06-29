## Name

systemd-system-update-generator — Generator for redirecting boot to offline update mode

## Synopsis

`/usr/lib/systemd/system-generators/systemd-system-update-generator`

## Description

`systemd-system-update-generator` is a generator that automatically redirects the boot process to `system-update.target`, if `/system-update` or `/etc/system-update` exists. This is required to implement the logic explained in the systemd.offline-updates(7).

`systemd-system-update-generator` implements systemd.generator(7).

## See Also

systemd(1), systemd.special(7)
