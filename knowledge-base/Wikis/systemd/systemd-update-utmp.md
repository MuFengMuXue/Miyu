## Name

systemd-update-utmp.service, systemd-update-utmp — Write audit and utmp updates at bootup and shutdown

## Synopsis

`systemd-update-utmp.service`

`/usr/lib/systemd/systemd-update-utmp`

## Description

`systemd-update-utmp.service` is a service that writes system reboots and shutdown requests to utmp and wtmp, as well as the audit logs.

## See Also

systemd(1), utmp(5), auditd(8)
