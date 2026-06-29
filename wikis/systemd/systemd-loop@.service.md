## Name

systemd-loop@.service — Attach a loopback block device

## Synopsis

`systemd-loop@`*`path`*`.service`

## Description

`systemd-loop@.service` is a template service that may be used to automatically attach a loopback block device at boot (or later). Its instance string may reference an (escaped) file system path pointing to a disk image to attach as loopback block device. Use systemd-escape(1)'s `--path` to properly escape a file system path.

This unit invokes **systemd-dissect --attach --quiet --loop-ref-auto** on the specified files, see systemd-dissect(1) for details.

## See Also

systemd(1), systemd-dissect(1), systemd-import-generator(8)
