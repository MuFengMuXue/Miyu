## Name

systemd-portabled.service, systemd-portabled — Portable service manager

## Synopsis

`systemd-portabled.service`

`/usr/lib/systemd/systemd-portabled`

## Description

**systemd-portabled** is a system service that may be used to attach, detach and inspect portable service images.

Most of **systemd-portabled**'s functionality is accessible through the portablectl(1) command.

See the Portable Services page for details about the concepts this service implements.

See org.freedesktop.portable1(5) and org.freedesktop.LogControl1(5) for a description of the D-Bus API.

## See Also

systemd(1), portablectl(1), org.freedesktop.portable1(5)
