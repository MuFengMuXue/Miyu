[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=Modprobed-db&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

**Resources**

[[]][Package information](https://packages.gentoo.org/packages/sys-kernel/modprobed-db)

[[]][GitHub](https://github.com/graysky2/modprobed-db)

[modprobed-db] is a useful utility for users wishing to build a minimal kernel via a make localmodconfig. In a nutshell, this make target creates a config based on the current config and a list of modules. It then disables any module option that is not needed thus not building hundreds/potentially thousands of extraneous modules. This results in a system-specific, streamlined kernel package and footprint as well as reduced compilation times.

## Contents

-   [[1] [Preparation]](#Preparation)
-   [[2] [Installation]](#Installation)
-   [[3] [Building kernels]](#Building_kernels)
-   [[4] [Auto update database]](#Auto_update_database)
    -   [[4.1] [Systemd]](#Systemd)
    -   [[4.2] [OpenRC]](#OpenRC)

## [Preparation]

[modprobed-db] works best by using the distribution kernel for about a month and have the utility run in the background so it can have time to learn what modules the system needs. An alternative (but not recommended) method would be to run the utility in the installcd\'s chroot environment and plug in every device and mount every drive with a different file system that user owns. This will not be perfect as the installcd disables some modules to make sure it works on all systems correctly so some manually editing will be required.

## [Installation]

`root `[`#`]`emerge --ask sys-kernel/modprobed-db`

## [Building kernels]

To build a kernel with [modprobed-db] then first emerge [[[sys-kernel/gentoo-sources]](https://packages.gentoo.org/packages/sys-kernel/gentoo-sources)[]] or any Linux kernel source package.

`root `[`#`]`emerge --ask sys-kernel/gentoo-sources`

If using modprobed-db for the first time make sure to connect any devices which may use modules e.g. removable storage with different file systems, webcams, embedded devices etc. and start any services that might be needed e.g. kvm machines, docker/podman containers. This will trigger any optional modules to be loaded so they can be stored in the modprobed-db database.

To use [modprobed-db] with the sources then first run the tool with:

`root `[`#`]`modprobed-db store`

This will store a database of all currently used modules in [/home/larry/.config/modprobed.db]

Load all modules in modprobed.db using:

`root `[`#`]`modprobed-db recall`

Compare currently loaded modules with modprobed.db using:

`root `[`#`]`modprobed-db debug`

For more information see:

`user `[`$`]`man 8 modprobed-db`

Next, change directories to the kernel sources and configure [make localmodconfig] to use the database just created:

`root `[`#`]`cd /usr/src/linux`

`root `[`#`]`make LSMOD=/home/larry/.config/modprobed.db localmodconfig`

To make manual changes to the config run:

`root `[`#`]`make menuconfig`

See [Kernel/Gentoo Kernel Configuration Guide](https://wiki.gentoo.org/wiki/Kernel/Gentoo_Kernel_Configuration_Guide "Kernel/Gentoo Kernel Configuration Guide") for more details on manual configuration.

Normal steps to build a kernel now apply:

`root `[`#`]`make -j $(nproc)`

`root `[`#`]`make modules_install`

`root `[`#`]`make install`

## [Auto update database]

What makes [modprobed-db] a useful tool is it\'s ability to scan the system periodically and add new modules to the database when new hardware is added.

** Note**\
A kernel rebuild is still required for the modules to be added

### [Systemd]

Systemd users can take advantage of the included user services which will update the database every 6 hours.

`user `[`$`]`systemctl --user enable modprobed-db`

`user `[`$`]`systemctl --user start modprobed-db`

### [OpenRC]

OpenRC users will currently have to use cron to gain this feature.

[FILE] **`/etc/crontab`Run modprobed-db once every 6 hours**

    0 */6 * * *     /usr/bin/modprobed-db store &> /dev/null