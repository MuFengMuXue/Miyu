## Name

systemd-modules-load.service, systemd-modules-load — Load kernel modules at boot

## Synopsis

`systemd-modules-load.service`

`/usr/lib/systemd/systemd-modules-load`

## Description

`systemd-modules-load.service` is an early boot service that loads kernel modules. It reads static configuration from files in `/usr/` and `/etc/`, but also runtime configuration from `/run/` and the kernel command line (see below).

See modules-load.d(5) for information about the configuration format of this service and paths where configuration files can be created.

## Kernel Command Line

`systemd-modules-load.service` understands the following kernel command line parameters:

`modules_load=`, `rd.modules_load=`  
Takes a comma-separated list of kernel modules to statically load during early boot. The option prefixed with "`rd.`" is read in the initrd only.

Added in version 187.

## See Also

systemd(1), modules-load.d(5)
