## Name

systemd-sysupdated.service, systemd-sysupdated — System Update Service

## Synopsis

`systemd-sysupdated.service`

`/usr/lib/systemd/systemd-sysupdated`

## Description

**systemd-sysupdated** is a system service that allows unprivileged clients to update the system. It works by scanning the system for updateable "targets" (i.e. portable services, sysexts, sysupdate components, etc.) and exposing them on the bus. Each target then has methods that translate directly into invocations of systemd-sysupdate(8).

See org.freedesktop.sysupdate1(5) and org.freedesktop.LogControl1(5) for a description of the D-Bus API.

## See Also

systemd(1), systemd-sysupdate(8), updatectl(1), org.freedesktop.sysupdate1(5)
