## Name

systemd-time-wait-sync.service, systemd-time-wait-sync — Wait until kernel time is synchronized

## Synopsis

`systemd-time-wait-sync.service`

`/usr/lib/systemd/systemd-time-wait-sync`

## Description

`systemd-time-wait-sync` is a system service that delays the start of units that are ordered after `time-sync.target` (see systemd.special(7) for details) until the system time has been synchronized with an accurate remote reference time source by `systemd-timesyncd.service`.

`systemd-timesyncd.service` notifies `systemd-time-wait-sync` about successful synchronization. `systemd-time-wait-sync` also tries to detect when the kernel marks the system clock as synchronized, but this detection is not reliable and is intended only as a fallback for compatibility with alternative NTP services that can be used to synchronize time (e.g., ntpd, chronyd).

## Files

`/run/systemd/timesync/synchronized`  
The presence of this file indicates to this service that the system clock has been synchronized.

Added in version 239.

## See Also

systemd(1), systemd.special(7), systemd-timesyncd.service(8)
