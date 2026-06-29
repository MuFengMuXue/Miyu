## Name

sysext.conf, confext.conf, sysext.conf.d, confext.conf.d — Configuration files for systemd-sysext

## Synopsis

`/etc/systemd/sysext.conf`

`/etc/systemd/sysext.conf.d/*.conf`

`/run/systemd/sysext.conf`

`/run/systemd/sysext.conf.d/*.conf`

`/usr/lib/systemd/sysext.conf`

`/usr/lib/systemd/sysext.conf.d/*.conf`

`/etc/systemd/confext.conf`

`/etc/systemd/confext.conf.d/*.conf`

`/run/systemd/confext.conf`

`/run/systemd/confext.conf.d/*.conf`

`/usr/lib/systemd/confext.conf`

`/usr/lib/systemd/confext.conf.d/*.conf`

## Description

These configuration files control the behavior of systemd-sysext(8) and systemd-confext(8). They are especially useful when needing to customize the behavior of the respective extension service units.

## Configuration Directories and Precedence

The default configuration is set during compilation, so configuration is only needed when it is necessary to deviate from those defaults. The main configuration file is loaded from one of the listed directories in order of priority, only the first file found is used: `/etc/systemd/`, `/run/systemd/`, `/usr/local/lib/systemd/` <sup>\[1\]</sup>, `/usr/lib/systemd/`. The vendor version of the file contains commented out entries showing the defaults as a guide to the administrator. Local overrides can also be created by creating drop-ins, as described below. The main configuration file can also be edited for this purpose (or a copy in `/etc/` if it is shipped under `/usr/`), however using drop-ins for local configuration is recommended over modifications to the main configuration file.

In addition to the main configuration file, drop-in configuration snippets are read from `/usr/lib/systemd/*.conf.d/`, `/usr/local/lib/systemd/*.conf.d/`, and `/etc/systemd/*.conf.d/`. Those drop-ins have higher precedence and override the main configuration file. Files in the `*.conf.d/` configuration subdirectories are sorted by their filename in lexicographic order, regardless of in which of the subdirectories they reside. When multiple files specify the same option, for options which accept just a single value, the entry in the file sorted last takes precedence, and for options which accept a list of values, entries are collected as they occur in the sorted files.

When packages need to customize the configuration, they can install drop-ins under `/usr/`. Files in `/etc/` are reserved for the local administrator, who may use this logic to override the configuration files installed by vendor packages. Drop-ins have to be used to override package drop-ins, since the main configuration file has lower precedence. It is recommended to prefix all filenames in those subdirectories with a two-digit number and a dash, to simplify the ordering. This also defines a concept of drop-in priorities to allow OS vendors to ship drop-ins within a specific range lower than the range used by users. This should lower the risk of package drop-ins overriding accidentally drop-ins defined by users. It is recommended to use the range 10-40 for drop-ins in `/usr/` and the range 60-90 for drop-ins in `/etc/` and `/run/`, to make sure that local and transient drop-ins take priority over drop-ins shipped by the OS vendor.

To disable a configuration file supplied by the vendor, the recommended way is to place a symlink to `/dev/null` in the configuration directory in `/etc/`, with the same filename as the vendor configuration file.

## Options

The following options are understood in both the "`[SysExt]`" and "`[ConfExt]`" sections:

### Section Options

`Mutable=`  
Set the mutable mode for system extensions. Takes one of "`no`", "`yes`", "`auto`", "`import`", "`ephemeral`", or "`ephemeral-import`". For details about the modes, see the `--mutable=` option in systemd-sysext(8). Defaults to "`no`".

Added in version 259.

`ImagePolicy=`  
Set the image policy. Takes an image policy string as argument, as per systemd.image-policy(7). For details, see the `--image-policy=` option in systemd-sysext(8).

Added in version 259.

## See Also

systemd(1), systemd-sysext(8), systemd.syntax(7)

  

<sup>\[1\]</sup> 💣💥🧨💥💥💣 Please note that those configuration files must be available at all times. If `/usr/local/` is a separate partition, it may not be available during early boot, and must not be used for configuration.
