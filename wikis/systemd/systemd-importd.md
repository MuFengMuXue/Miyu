## Name

systemd-importd.service, systemd-importd — VM and container image import and export service

## Synopsis

`systemd-importd.service`

`/usr/lib/systemd/systemd-importd`

## Description

**systemd-importd** is a system service that allows importing, exporting and downloading of disk images. It provides the implementation for importctl(1)'s **pull-raw**, **pull-tar**, **import-raw**, **import-tar**, **import-fs**, **export-raw**, and **export-tar** commands.

See org.freedesktop.import1(5) and org.freedesktop.LogControl1(5) for a description of the D-Bus API.

## See Also

systemd(1), importctl(1), systemd-machined.service(8), systemd-nspawn(1), org.freedesktop.import1(5)
