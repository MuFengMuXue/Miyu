## Name

systemd-storagetm.service, systemd-storagetm — Exposes all local block devices as NVMe-TCP mass storage devices

## Synopsis

`systemd-storagetm.service`

`/usr/lib/systemd/systemd-storagetm` \[OPTIONS...\] \[*`DEVICE`*\]

## Description

`systemd-storagetm.service` is a service that exposes all local block devices as NVMe-TCP mass storage devices. Its primary use-case is to be invoked by the `storage-target-mode.target` unit that can be booted into.

### Warning

The NVMe disks are currently exposed without authentication or encryption, in read/write mode. This means network peers may read from and write to the device without any restrictions. This functionality should hence only be used in a local setup.

Note that to function properly networking must be configured too. The recommended mechanism to boot into a storage target mode is by adding "`rd.systemd.unit=storage-target-mode.target ip=link-local`" on the kernel command line. Note that "`ip=link-local`" only configures link-local IP, i.e. IPv4LL and IPv6LL, which means non-routable addresses. This is done for security reasons, so that only systems on the local link can access the devices. Use "`ip=dhcp`" to assign routable addresses too. For further details see systemd-network-generator.service(8).

Unless the `--all` switch is used expects one or more block devices or regular files to expose via NVMe-TCP as argument.

## Options

The following options are understood:

`--nqn=`  
Takes a string. If specified configures the NVMe Qualified Name to use for the exposed NVMe-TCP mass storage devices. The NQN should follow the syntax described in NVM Express Base Specification 2.0c, section 4.5 "NVMe Qualified Names". Note that the NQN specified here will be suffixed with a dot and the block device name before it is exposed on the NVMe target. If not specified, defaults to "`nqn.2023-10.io.systemd:storagetm.`*`ID`*", where ID is replaced by a 128bit ID derived from machine-id(5).

Added in version 255.

`--all`, `-a`  
If specified exposes all local block devices via NVMe-TCP, current and future (i.e. it watches block devices come and go and updates the NVMe-TCP list as needed). Note that by default any block devices that originate on the same block device as the block device backing the current root file system are excluded. If the switch is specified twice this safety mechanism is disabled.

Added in version 255.

`--list-devices`  
Show a list of candidate block devices this command may operate on. Specifically, this enumerates block devices currently present, and shows their device node paths along with any of their symlinks.

Added in version 257.

`-h`, `--help`  
Print a short help text and exit.

`--version`  
Print a short version string and exit.

## See Also

systemd(1), systemd.special(7)
