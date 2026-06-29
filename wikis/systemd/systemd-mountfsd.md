## Name

systemd-mountfsd.service, systemd-mountfsd — Disk Image File System Mount Service

## Synopsis

`systemd-mountfsd.service`

`/usr/lib/systemd/systemd-mountfsd`

## Description

**systemd-mountfsd** is a system service that dissects disk images, and returns mount file descriptors for the file systems contained therein to clients, via a Varlink IPC API.

The disk images provided must contain a raw file system image or must follow the UAPI.2 Discoverable Partitions Specification. Before mounting any file systems authenticity of the disk image is established in one or a combination of the following ways:

1.  If the disk image is located in a regular file in one of the directories `/var/lib/machines/`, `/var/lib/portables/`, `/var/lib/extensions/`, `/var/lib/confexts/` or their counterparts in the `/etc/`, `/run/`, `/usr/lib/` it is assumed to be trusted.

2.  If the disk image contains a Verity enabled disk image, along with a signature partition with a key in the kernel keyring or in `/etc/verity.d/` (and related directories) the disk image is considered trusted.

This service provides one Varlink service: `io.systemd.MountFileSystem` which accepts a file descriptor to a regular file or block device, and returns a number of file descriptors referring to an `fsmount()` file descriptor the client may then attach to a path of their choice.

The returned mounts are automatically allowlisted in the per-user-namespace allowlist maintained by systemd-nsresourced.service(8).

The file systems are automatically fsck(8)'ed before mounting.

## See Also

systemd(1), systemd-nsresourced.service(8)
