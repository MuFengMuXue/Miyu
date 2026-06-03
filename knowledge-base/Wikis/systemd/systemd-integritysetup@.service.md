## Name

systemd-integritysetup@.service, systemd-integritysetup — Disk integrity protection logic

## Synopsis

`systemd-integritysetup@.service`

`/usr/lib/systemd/systemd-integritysetup`

## Description

`systemd-integritysetup@.service` is a service responsible for setting up integrity protected block devices. It should be instantiated for each device that requires integrity protection.

At early boot and when the system manager configuration is reloaded, entries from integritytab(5) are converted into `systemd-integritysetup@.service` units by systemd-integritysetup-generator(8).

`systemd-integritysetup@.service` calls **systemd-integritysetup**.

## Commands

The following commands are understood by **systemd-integritysetup**:

 `attach` *`volume`* *`device`* \[*`key-file|-`*\] \[*`option(s)|-`*\]  
Create a block device *`volume`* using *`device`*. See integritytab(5) and Kernel dm-integrity documentation for details.

Added in version 250.

 `detach` *`volume`*  
Detach (destroy) the block device *`volume`*.

Added in version 250.

 `help`  
Print short information about command syntax.

Added in version 250.

## See Also

systemd(1), integritytab(5), systemd-integritysetup-generator(8), integritysetup(8)
