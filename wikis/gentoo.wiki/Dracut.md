**Resources**

[[]][Home](https://dracut-ng.github.io/dracut-ng/)

[[]][GitHub](https://github.com/dracut-ng/dracut-ng)

[[]][Official project wiki](https://dracut-ng.github.io/dracut-ng/)

[[]][Wikipedia](https://en.wikipedia.org/wiki/Dracut_(software) "wikipedia:Dracut (software)")

[![Ohloh Logo](/images/thumb/c/c1/Ohloh-logo.png/30px-Ohloh-logo.png)][Open Hub](https://www.openhub.net/p/dracut)

**Dracut** is an [initramfs](https://wiki.gentoo.org/wiki/Initramfs "Initramfs") infrastructure and aims to have as little as possible hard-coded into the initramfs.

Dracut originated from the [Fedora Project](https://fedoraproject.org/wiki/Dracut) and was ported to Gentoo in the [2010 Google Summer of Code](https://www.google-melange.com/archive/gsoc/2010/orgs/gentoo/projects/aidecoe.html). The project has since forked as **dracut-ng** (next generation) which continues active development. For more detailed information, refer to the project [documentation](https://dracut-ng.github.io/dracut-ng/).

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Kernel]](#Kernel)
    -   [[1.3] [Emerge]](#Emerge)
-   [[2] [Building an initramfs image]](#Building_an_initramfs_image)
    -   [[2.1] [Automation]](#Automation)
    -   [[2.2] [Default images]](#Default_images)
    -   [[2.3] [Configuration]](#Configuration)
        -   [[2.3.1] [Localization / i18n]](#Localization_.2F_i18n)
    -   [[2.4] [Modules]](#Modules)
    -   [[2.5] [Adding modules]](#Adding_modules)
    -   [[2.6] [List of modules]](#List_of_modules)
    -   [[2.7] [Customizing the image]](#Customizing_the_image)
        -   [[2.7.1] [Adding files to the image]](#Adding_files_to_the_image)
        -   [[2.7.2] [Kernel modules]](#Kernel_modules)
        -   [[2.7.3] [Filesystems and mount points]](#Filesystems_and_mount_points)
        -   [[2.7.4] [Elogind]](#Elogind)
        -   [[2.7.5] [Compressing the image]](#Compressing_the_image)
-   [[3] [Booting the initramfs]](#Booting_the_initramfs)
-   [[4] [Tasks]](#Tasks)
    -   [[4.1] [ext boot]](#ext_boot)
    -   [[4.2] [LVM on LUKS]](#LVM_on_LUKS)
    -   [[4.3] [NFS boot]](#NFS_boot)
    -   [[4.4] [NBD boot]](#NBD_boot)
    -   [[4.5] [Debug]](#Debug)
    -   [[4.6] [Other filesystems]](#Other_filesystems)
-   [[5] [Custom modules]](#Custom_modules)
    -   [[5.1] [Module structure]](#Module_structure)
    -   [[5.2] [Creating a basic module]](#Creating_a_basic_module)
    -   [[5.3] [Hook scripts]](#Hook_scripts)
    -   [[5.4] [Module installation functions]](#Module_installation_functions)
    -   [[5.5] [Testing custom modules]](#Testing_custom_modules)
    -   [[5.6] [Module naming and priorities]](#Module_naming_and_priorities)
    -   [[5.7] [Advanced features]](#Advanced_features)
        -   [[5.7.1] [Dependencies]](#Dependencies)
        -   [[5.7.2] [Conditional installation]](#Conditional_installation)
    -   [[5.8] [Example: Custom filesystem module]](#Example:_Custom_filesystem_module)
-   [[6] [Troubleshooting]](#Troubleshooting)
    -   [[6.1] [Common issues]](#Common_issues)
        -   [[6.1.1] [Boot failure: \"No root device found\"]](#Boot_failure:_.22No_root_device_found.22)
        -   [[6.1.2] [Dracut emergency shell]](#Dracut_emergency_shell)
        -   [[6.1.3] [Module dependency errors]](#Module_dependency_errors)
        -   [[6.1.4] [Kernel module missing]](#Kernel_module_missing)
    -   [[6.2] [Debug mode]](#Debug_mode)
    -   [[6.3] [Network boot issues]](#Network_boot_issues)
        -   [[6.3.1] [DHCP not working]](#DHCP_not_working)
        -   [[6.3.2] [NFS mount failures]](#NFS_mount_failures)
    -   [[6.4] [Recovery procedures]](#Recovery_procedures)
        -   [[6.4.1] [Rescue with working initramfs]](#Rescue_with_working_initramfs)
        -   [[6.4.2] [Rescue with live media]](#Rescue_with_live_media)
        -   [[6.4.3] [Recreate initramfs]](#Recreate_initramfs)
    -   [[6.5] [Logging and diagnosis]](#Logging_and_diagnosis)
        -   [[6.5.1] [Check dracut build log]](#Check_dracut_build_log)
        -   [[6.5.2] [Check boot messages]](#Check_boot_messages)
        -   [[6.5.3] [Examine initramfs contents]](#Examine_initramfs_contents)
    -   [[6.6] [Performance issues]](#Performance_issues)
        -   [[6.6.1] [Large initramfs size]](#Large_initramfs_size)
        -   [[6.6.2] [Slow boot times]](#Slow_boot_times)
    -   [[6.7] [When dracut is executed]](#When_dracut_is_executed)
        -   [[6.7.1] [Bluetooth]](#Bluetooth)
        -   [[6.7.2] [Cryptsetup]](#Cryptsetup)
        -   [[6.7.3] [NFS / rpcbind]](#NFS_.2F_rpcbind)
-   [[7] [See also]](#See_also)
-   [[8] [External resources]](#External_resources)
-   [[9] [References]](#References)

## [Installation]

### [USE flags]

### [USE flags for] [sys-kernel/dracut](https://packages.gentoo.org/packages/sys-kernel/dracut) [[]] [Generic initramfs generation tool]

  ------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [`debug`](https://packages.gentoo.org/useflags/debug)               Enable extra debug codepaths, like asserts and extra output. If you want to get meaningful backtraces see https://wiki.gentoo.org/wiki/Project:Quality_Assurance/Backtraces
  [`dracut-cpio`](https://packages.gentoo.org/useflags/dracut-cpio)   Build the enhanced \'dracut-cpio\' program
  [`selinux`](https://packages.gentoo.org/useflags/selinux)           !!internal use only!! Security Enhanced Linux support, this must be set by the selinux profile or breakage will occur
  [`systemd`](https://packages.gentoo.org/useflags/systemd)           Enable use of systemd-specific libraries and features like socket activation or session tracking
  [`test`](https://packages.gentoo.org/useflags/test)                 Enable dependencies and/or preparations necessary to run tests (usually controlled by FEATURES=test but can be toggled independently)
  ------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-05-17 20:43] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

Note: some packages have the [[[dracut]](https://packages.gentoo.org/useflags/dracut)[[]](https://wiki.gentoo.org/wiki/USE_flag "USE flag")] [USE flag](https://wiki.gentoo.org/wiki/USE_flag "USE flag").

### [Kernel]

Before using the images generated by dracut, the Linux kernel must include initramfs support. The ebuild will provide a warning post-installation if the kernel is missing the required options:

[KERNEL] **Enabling the initramfs (`CONFIG_BLK_DEV_INITRD` and `CONFIG_DEVTMPFS` respectively)**

    General setup  --->
       [*] Initial RAM filesystem and RAM disk (initramfs/initrd) support
    Device Drivers --->
       Generic Driver Options --->
          [*] Maintain a devtmpfs filesystem to mount at /dev

Certain dracut modules also require additional dependencies to function. A list of optional dependencies is listed at the end of the installation. The `DRACUT_MODULES` variable in [make.conf] is no longer used.

### [Emerge]

Install dracut:

`root `[`#`]`emerge --ask sys-kernel/dracut`

## [Building an initramfs image]

### [Automation]

Installing an initramfs image generated with Dracut can be automated by enabling the [[[dracut]](https://packages.gentoo.org/useflags/dracut)[[]](https://wiki.gentoo.org/wiki/USE_flag "USE flag")] USE flag on [[[sys-kernel/installkernel]](https://packages.gentoo.org/packages/sys-kernel/installkernel)[]]. This will generate a new initramfs image via [/sbin/installkernel](https://wiki.gentoo.org/wiki/Installkernel "Installkernel") everytime a kernel is installed via [make install] or [emerge \--config \<distribution kernel package\>].

### [Default images]

Once dracut is installed, it can be used to build an initramfs image. The simplest way to do this is to just run:

`root `[`#`]`mount /boot`

`root `[`#`]`dracut`

Starting from version 106 the default initramfs generation behaviour has changed by default to only include the kernel drivers required by the system it was created for to boot, rather than a generic initramfs which can boot on any system.

Hostonly images produced will contain only those elements used by the local machine for booting. Certain modules behave differently in host-only mode. The kernel-modules module, for example, will only include the tools and modules used by the current rootfs file system, and the i18n module will install the fonts and keymaps for the local machine. Otherwise, every available file system, font, etc. would be included.

In some situations, like using a faster machine to compile [[[sys-kernel/gentoo-kernel]](https://packages.gentoo.org/packages/sys-kernel/gentoo-kernel)[]] this will cause issues with booting once moved to the new machine. Generic generation can be restored using the `--no-hostonly` as detailed below:

`root `[`#`]`dracut --no-hostonly`

\

** Tip**\
No-hostonly mode can be also set as the default in [/etc/dracut.conf]:

[FILE] **`/etc/dracut.conf`**

    hostonly="no"

By default, dracut will produce an image suitable for booting the currently active kernel; it will pull the kernel modules needed for that kernel, etc. The image will be written in a file called [/boot/initramfs-\<kernel version\>.img]. Both options may be overridden by specifying a new file name and kernel version on the command line, in that order. Both parameters are optional. To override the kernel version and keep the default file name, add the \--kver option:

`root `[`#`]`dracut --hostonly --kver 3.2.5-hardened`

### [Configuration]

#### [][Localization / i18n]

** Tip**\
Localization can be set in [/etc/dracut.conf]:

[FILE] **`/etc/dracut.conf`**

    i18n_vars="/usr/share/consolefonts  /usr/share/keymaps"

\

### [Modules]

Dracut installs all available modules, though some may need additional dependencies. The purpose of each module is to arrange for files to be included in the final initramfs image. In addition, dracut exposes hooks that run at certain points, which modules can hook into to perform required boot actions.

### [Adding modules]

Dracut comes with a suitable set of default modules (see below). This module list can be overridden in two ways: on the command line, or in the configuration file. Editing the configuration file will set up dracut to be re-run easily when changing kernels or after modifying other boot-time options. Options specified in [/etc/dracut.conf] can be overridden by files in [/etc/dracut.conf.d], which are installed by various dracut-aware packages. Both options can be overridden by command-line parameters. The following configuration options deal with the default modules list:

[FILE] **`/etc/dracut.conf`**

    # Equivalent to -H
    hostonly="yes"

    # Equivalent to -m "module module module"
    dracutmodules+=" dash kernel-modules rootfs-block usrmount fs-lib shutdown "

    # Equivalent to -a "module"
    add_dracutmodules+=" module " # Note leading and trailing spaces

    # Equivalent to -o "module"
    omit_dracutmodules+=" module " # Note leading and trailing spaces

Specifying `dracutmodules` (or the `-m` option) will override the entire default list, and install *only* the modules specified. This can cut down significantly on image size (for example, if no kernel modules are needed, or i18n support, etc.). If it is not clear which modules are needed, build one fully-featured image and keep it in [/boot] to experiment. If anything goes wrong, [grub.conf] may be edited at boot to switch to that.

The other options can be used to add or remove items from the default list, including [custom modules](#Custom_modules). If a module refuses to install (for example, its prerequisite binaries are missing) there is a `--force-add` command-line switch (but no matching configuration option) to add them anyway. Note that forcing a module to be added this way is dangerous, as the installed scripts will likely to run execute commands that are not present.

### [List of modules]

Full list of supported modules can be obtained using the `--list-modules` parameter. The following list has been updated for **dracut-106** and is accurate as of **2025-07-01**. Note that available modules may vary depending on your system configuration and installed packages. Modules are listed with their additional requirements. ^[\[1\]](#cite_note-1)^

  ----------------------------------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ------------------------------------------------------------------------------------ -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Module                                                                                                Description                                                                                                                                                                                                                                                                                                                                                                                                       Enabled?                                                                                                                                                                        Depends on modules                                                                   Requirements
  Core System
  base                                                                                                  Base module with required utilities                                                                                                                                                                                                                                                                                                                                                                               always                                                                                                                                                                          udev-rules
  [bash](https://wiki.gentoo.org/wiki/Bash "Bash")                                                      Includes [/bin/bash] as [/bin/sh]                                                                                                                                                                                                           when required; bash is preferred interpreter if there more of them available                                                                                                                                                                                         [[[app-shells/bash]](https://packages.gentoo.org/packages/app-shells/bash)[]] (bash)
  [busybox](https://wiki.gentoo.org/wiki/Busybox "Busybox")                                             Includes [/bin/busybox] as replacement of utilities supported by [busybox \--list]                                                                                                                                                          when required                                                                                                                                                                                                                                                        [[[sys-apps/busybox]](https://packages.gentoo.org/packages/sys-apps/busybox)[]] (busybox)
  [dash](https://wiki.gentoo.org/wiki/Dash "Dash")                                                      Includes [/bin/dash] as [/bin/sh]                                                                                                                                                                                                           when required                                                                                                                                                                                                                                                        [[[app-shells/dash]](https://packages.gentoo.org/packages/app-shells/dash)[]] (dash)
  debug                                                                                                 Enable debug features                                                                                                                                                                                                                                                                                                                                                                                             when required
  dracut-systemd                                                                                        Legacy compatibility module for systemd support                                                                                                                                                                                                                                                                                                                                                                   when required                                                                                                                                                                   systemd
  rescue                                                                                                Includes various utilities for rescue mode (such as ping, ssh, vi, fsck.\*)                                                                                                                                                                                                                                                                                                                                       when required
  shell-interpreter                                                                                     Virtual module for shell interpreter selection                                                                                                                                                                                                                                                                                                                                                                    when required                                                                                                                                                                   OR(bash dash mksh busybox)
  shutdown                                                                                              Sets up hooks to run on shutdown                                                                                                                                                                                                                                                                                                                                                                                  always                                                                                                                                                                          base
  [systemd](https://wiki.gentoo.org/wiki/Systemd "Systemd")                                             Adds systemd as early init initialization system                                                                                                                                                                                                                                                                                                                                                                  when required                                                                                                                                                                                                                                                        [[[sys-apps/systemd]](https://packages.gentoo.org/packages/sys-apps/systemd)[]]
  systemd-ac-power                                                                                      Adds systemd AC power detection support                                                                                                                                                                                                                                                                                                                                                                           when required                                                                                                                                                                   systemd                                                                              [[[sys-apps/systemd]](https://packages.gentoo.org/packages/sys-apps/systemd)[]]
  systemd-ask-password                                                                                  Adds systemd password prompting support                                                                                                                                                                                                                                                                                                                                                                           when required                                                                                                                                                                   systemd                                                                              [[[sys-apps/systemd]](https://packages.gentoo.org/packages/sys-apps/systemd)[]]
  systemd-battery-check                                                                                 Adds systemd battery level checking                                                                                                                                                                                                                                                                                                                                                                               when required                                                                                                                                                                   systemd                                                                              [[[sys-apps/systemd]](https://packages.gentoo.org/packages/sys-apps/systemd)[]]
  systemd-bsod                                                                                          Adds systemd blue screen of death support                                                                                                                                                                                                                                                                                                                                                                         when required                                                                                                                                                                   systemd                                                                              [[[sys-apps/systemd]](https://packages.gentoo.org/packages/sys-apps/systemd)[]]
  systemd-coredump                                                                                      Adds systemd coredump handling                                                                                                                                                                                                                                                                                                                                                                                    when required                                                                                                                                                                   systemd                                                                              [[[sys-apps/systemd]](https://packages.gentoo.org/packages/sys-apps/systemd)[]]
  systemd-creds                                                                                         Adds systemd credentials support                                                                                                                                                                                                                                                                                                                                                                                  when required                                                                                                                                                                   systemd                                                                              [[[sys-apps/systemd]](https://packages.gentoo.org/packages/sys-apps/systemd)[]]
  systemd-emergency                                                                                     Adds systemd emergency mode support                                                                                                                                                                                                                                                                                                                                                                               when required                                                                                                                                                                   systemd                                                                              [[[sys-apps/systemd]](https://packages.gentoo.org/packages/sys-apps/systemd)[]]
  systemd-hostnamed                                                                                     Adds systemd hostname daemon                                                                                                                                                                                                                                                                                                                                                                                      when required                                                                                                                                                                   systemd dbus                                                                         [[[sys-apps/systemd]](https://packages.gentoo.org/packages/sys-apps/systemd)[]]
  systemd-initrd                                                                                        Adds systemd initrd support                                                                                                                                                                                                                                                                                                                                                                                       when required                                                                                                                                                                   systemd                                                                              [[[sys-apps/systemd]](https://packages.gentoo.org/packages/sys-apps/systemd)[]]
  systemd-integritysetup                                                                                Adds systemd dm-integrity support                                                                                                                                                                                                                                                                                                                                                                                 when required                                                                                                                                                                   systemd                                                                              [[[sys-apps/systemd]](https://packages.gentoo.org/packages/sys-apps/systemd)[]]
  systemd-journald                                                                                      Adds systemd journal daemon                                                                                                                                                                                                                                                                                                                                                                                       when required                                                                                                                                                                   systemd                                                                              [[[sys-apps/systemd]](https://packages.gentoo.org/packages/sys-apps/systemd)[]]
  systemd-ldconfig                                                                                      Adds systemd ldconfig support                                                                                                                                                                                                                                                                                                                                                                                     when required                                                                                                                                                                   systemd                                                                              [[[sys-apps/systemd]](https://packages.gentoo.org/packages/sys-apps/systemd)[]]
  systemd-modules-load                                                                                  Adds systemd kernel module loading                                                                                                                                                                                                                                                                                                                                                                                when required                                                                                                                                                                   systemd                                                                              [[[sys-apps/systemd]](https://packages.gentoo.org/packages/sys-apps/systemd)[]]
  systemd-network-management                                                                            Adds network management for systemd                                                                                                                                                                                                                                                                                                                                                                               when required
  systemd-networkd                                                                                      Adds systemd network daemon                                                                                                                                                                                                                                                                                                                                                                                       when required                                                                                                                                                                   systemd                                                                              [[[sys-apps/systemd]](https://packages.gentoo.org/packages/sys-apps/systemd)[]]
  systemd-pcrphase                                                                                      Adds systemd PCR phase support                                                                                                                                                                                                                                                                                                                                                                                    when required                                                                                                                                                                   systemd tpm2-tss                                                                     [[[sys-apps/systemd]](https://packages.gentoo.org/packages/sys-apps/systemd)[]]
  systemd-portabled                                                                                     Adds systemd portable service support                                                                                                                                                                                                                                                                                                                                                                             when required                                                                                                                                                                   systemd                                                                              [[[sys-apps/systemd]](https://packages.gentoo.org/packages/sys-apps/systemd)[]]
  systemd-pstore                                                                                        Adds systemd persistent storage support                                                                                                                                                                                                                                                                                                                                                                           when required                                                                                                                                                                   systemd                                                                              [[[sys-apps/systemd]](https://packages.gentoo.org/packages/sys-apps/systemd)[]]
  systemd-repart                                                                                        Adds systemd partition management                                                                                                                                                                                                                                                                                                                                                                                 when required                                                                                                                                                                   systemd                                                                              [[[sys-apps/systemd]](https://packages.gentoo.org/packages/sys-apps/systemd)[]]
  systemd-resolved                                                                                      Adds systemd DNS resolver daemon                                                                                                                                                                                                                                                                                                                                                                                  when required                                                                                                                                                                   systemd                                                                              [[[sys-apps/systemd]](https://packages.gentoo.org/packages/sys-apps/systemd)[]]
  systemd-sysctl                                                                                        Adds systemd sysctl support                                                                                                                                                                                                                                                                                                                                                                                       when required                                                                                                                                                                   systemd                                                                              [[[sys-apps/systemd]](https://packages.gentoo.org/packages/sys-apps/systemd)[]]
  systemd-sysext                                                                                        Adds systemd system extension support                                                                                                                                                                                                                                                                                                                                                                             when required                                                                                                                                                                   systemd                                                                              [[[sys-apps/systemd]](https://packages.gentoo.org/packages/sys-apps/systemd)[]]
  systemd-sysusers                                                                                      Adds systemd system users support                                                                                                                                                                                                                                                                                                                                                                                 when required                                                                                                                                                                   systemd                                                                              [[[sys-apps/systemd]](https://packages.gentoo.org/packages/sys-apps/systemd)[]]
  systemd-timedated                                                                                     Adds systemd time daemon                                                                                                                                                                                                                                                                                                                                                                                          when required                                                                                                                                                                   systemd dbus                                                                         [[[sys-apps/systemd]](https://packages.gentoo.org/packages/sys-apps/systemd)[]]
  systemd-timesyncd                                                                                     Adds systemd time synchronization daemon                                                                                                                                                                                                                                                                                                                                                                          when required                                                                                                                                                                   systemd                                                                              [[[sys-apps/systemd]](https://packages.gentoo.org/packages/sys-apps/systemd)[]]
  systemd-tmpfiles                                                                                      Adds systemd temporary files support                                                                                                                                                                                                                                                                                                                                                                              when required                                                                                                                                                                   systemd                                                                              [[[sys-apps/systemd]](https://packages.gentoo.org/packages/sys-apps/systemd)[]]
  systemd-udevd                                                                                         Adds systemd udev daemon                                                                                                                                                                                                                                                                                                                                                                                          when required                                                                                                                                                                   systemd                                                                              [[[sys-apps/systemd]](https://packages.gentoo.org/packages/sys-apps/systemd)[]]
  systemd-veritysetup                                                                                   Adds systemd dm-verity support                                                                                                                                                                                                                                                                                                                                                                                    when required                                                                                                                                                                   systemd                                                                              [[[sys-apps/systemd]](https://packages.gentoo.org/packages/sys-apps/systemd)[]]
  syslog                                                                                                Includes syslog capabilites to initramfs                                                                                                                                                                                                                                                                                                                                                                          when required
  terminfo                                                                                              Includes a terminfo file                                                                                                                                                                                                                                                                                                                                                                                          always
  udev-rules                                                                                            Includes udev and some basic rules                                                                                                                                                                                                                                                                                                                                                                                always                                                                                                                                                                                                                                                               [[[virtual/udev]](https://packages.gentoo.org/packages/virtual/udev)[]] (udevadm)

  File Systems
  [btrfs](https://wiki.gentoo.org/wiki/Btrfs "Btrfs")                                                   Adds BTRFS support                                                                                                                                                                                                                                                                                                                                                                                                always; hostonly: rootfs                                                                                                                                                        udev-rules                                                                           [[[sys-fs/btrfs-progs]](https://packages.gentoo.org/packages/sys-fs/btrfs-progs)[]]
  cifs                                                                                                  Adds CIFS filesystem support                                                                                                                                                                                                                                                                                                                                                                                      always; hostonly: rootfs                                                                                                                                                        network                                                                              [[[net-fs/cifs-utils]](https://packages.gentoo.org/packages/net-fs/cifs-utils)[]] (mount.cifs)
  convertfs                                                                                             Merges [/] into [/usr] on next boot                                                                                                                                                                                                         when required                                                                                                                                                                   base bash
  [ecryptfs](https://wiki.gentoo.org/wiki/Ecryptfs "Ecryptfs")                            Adds ecryptfs filesystems support                                                                                                                                                                                                                                                                                                                                                                                 when required                                                                                                                                                                   masterkey
  fs-lib                                                                                                Includes filesystem tools (including fsck.\* and mount)                                                                                                                                                                                                                                                                                                                                                           always
  fstab-sys                                                                                             Arranges for arbitrary partitions to be mounted before rootfs.                                                                                                                                                                                                                                                                                                                                                    always if [/etc/fstab.sys] exists, or command line includes `--fstab` or `--add_fstab`       fs-lib
  [nfs](https://wiki.gentoo.org/wiki/NFS "NFS")                                           Adds support for NFS                                                                                                                                                                                                                                                                                                                                                                                              always; hostonly: rootfs                                                                                                                                                        network                                                                              [[[net-fs/nfs-utils]](https://packages.gentoo.org/packages/net-fs/nfs-utils)[]] (rpc.statd mount.nfs mount.nfs4 umount sed chmod chown) [[[net-nds/rpcbind]](https://packages.gentoo.org/packages/net-nds/rpcbind)[]] (rpcbind portmap)
  rootfs-block                                                                                          Arranges for the block device containing the rootfs to be mounted                                                                                                                                                                                                                                                                                                                                                 always                                                                                                                                                                          base fs-lib
  usrmount                                                                                              Arranges for [/usr] to be mounted                                                                                                                                                                                                                                                                                              always
  virtfs                                                                                                Adds virtual filesystems (9p) support                                                                                                                                                                                                                                                                                                                                                                             when required; hostonly: rootfs
  virtiofs                                                                                              Adds virtiofs filesystems support                                                                                                                                                                                                                                                                                                                                                                                 always; hostonly: rootfs
  zfs                                                                                                   Adds ZFS filesystem support                                                                                                                                                                                                                                                                                                                                                                                       when required                                                                                                                                                                                                                                                        [[[sys-fs/zfs]](https://packages.gentoo.org/packages/sys-fs/zfs)[]] (zfs zpool)

  Storage & Block Devices
  cms                                                                                                   Includes support for mounting z/VM CMS disks                                                                                                                                                                                                                                                                                                                                                                      when required                                                                                                                                                                   znet zfcp dasd dasd_mod bash
  crypt                                                                                                 Adds support for encrypted with [LUKS](https://wiki.gentoo.org/wiki/LUKS "LUKS") filesystems                                                                                                                                                                                                                                                                                                        always; hostonly: rootfs                                                                                                                                                        dm rootfs-block                                                                      [[[sys-fs/cryptsetup]](https://packages.gentoo.org/packages/sys-fs/cryptsetup)[]] (cryptsetup)
  crypt-gpg                                                                                             Adds support GPG for crypto operations and SmartCards (may requires GPG keys)                                                                                                                                                                                                                                                                                                                                     when required; always if file /etc/dracut.conf.d/crypt-public-key.gpg exists                                                                                                    crypt                                                                                [[[app-crypt/gnupg]](https://packages.gentoo.org/packages/app-crypt/gnupg)[]] (gpg)
  crypt-loop                                                                                            Adds support for encrypted loopback devices (symmetric key)                                                                                                                                                                                                                                                                                                                                                       when required                                                                                                                                                                   crypt                                                                                [[[sys-apps/util-linux]](https://packages.gentoo.org/packages/sys-apps/util-linux)[]] losetup
  [dm](https://wiki.gentoo.org/wiki/LVM "LVM")                                                          Adds support of device-mapper                                                                                                                                                                                                                                                                                                                                                                                     when required                                                                                                                                                                                                                                                        [[[sys-fs/lvm2]](https://packages.gentoo.org/packages/sys-fs/lvm2)[]] (dmsetup)
  dmraid                                                                                                Adds support for DMRAID arrays                                                                                                                                                                                                                                                                                                                                                                                    always; hostonly: rootfs                                                                                                                                                        dm rootfs-block                                                                      [[[sys-fs/dmraid]](https://packages.gentoo.org/packages/sys-fs/dmraid)[]] (dmraid)
  dmsquash-live                                                                                         Includes support for SquashFS images                                                                                                                                                                                                                                                                                                                                                                              when required; hostonly: never                                                                                                                                                  dm rootfs-block img-lib bash
  dmsquash-live-autooverlay                                                                             Auto-overlay support for live images                                                                                                                                                                                                                                                                                                                                                                              when required                                                                                                                                                                   dmsquash-live
  dmsquash-live-ntfs                                                                                    Includes support for [SquashFS](https://wiki.gentoo.org/wiki/SquashFS "SquashFS") images located in NTFS filesystems                                                                                                                                                                                                                                                                                              when required                                                                                                                                                                   dmsquash-live                                                                        [[[sys-fs/ntfs3g]](https://packages.gentoo.org/packages/sys-fs/ntfs3g)[]] (ntfs-3g)
  fcoe                                                                                                  Adds support for Fibre Channel over Ethernet (FCoE)                                                                                                                                                                                                                                                                                                                                                               always; hostonly: rootfs                                                                                                                                                        network                                                                              [[[sys-apps/fcoe-utils]](https://packages.gentoo.org/packages/sys-apps/fcoe-utils)[]] (fcoemon fcoeadm fipvlan) [[[sys-apps/lldpad]](https://packages.gentoo.org/packages/sys-apps/lldpad)[]] (lldpad dcbtool) [[[sys-apps/iproute2]](https://packages.gentoo.org/packages/sys-apps/iproute2)[]] (ip) [[[sys-apps/coreutils]](https://packages.gentoo.org/packages/sys-apps/coreutils)[]] (readlink tr)
  fcoe-uefi                                                                                             Adds support for Fibre Channel over Ethernet (FCoE) in EFI mode                                                                                                                                                                                                                                                                                                                                                   always; hostonly: rootfs                                                                                                                                                        fcoe uefi-lib bash                                                                   [[[sys-apps/fcoe-utils]](https://packages.gentoo.org/packages/sys-apps/fcoe-utils)[]] (fipvlan) [[[sys-apps/lldpad]](https://packages.gentoo.org/packages/sys-apps/lldpad)[]] (lldpad dcbtool) [[[sys-apps/iproute2]](https://packages.gentoo.org/packages/sys-apps/iproute2)[]] (ip) [[[sys-apps/coreutils]](https://packages.gentoo.org/packages/sys-apps/coreutils)[]] (readlink)
  [iscsi](https://wiki.gentoo.org/wiki/ISCSI "ISCSI")                                                   Adds support for iSCSI devices                                                                                                                                                                                                                                                                                                                                                                                    always; hostonly: rootfs                                                                                                                                                                                                                                             [[[sys-block/open-iscsi]](https://packages.gentoo.org/packages/sys-block/open-iscsi)[]] (iscsi-iname iscsiadm iscsid)
  livenet                                                                                               Fetch live updates for SquashFS images                                                                                                                                                                                                                                                                                                                                                                            when required                                                                                                                                                                   network url-lib dmsquash-live img-lib bash
  lunmask                                                                                               Masks LUN devices to select only ones which required to boot                                                                                                                                                                                                                                                                                                                                                      always; hostonly: rootfs when type in [/sys/module/scsi_mod/parameters/scan] is \"manual\"
  [lvm](https://wiki.gentoo.org/wiki/LVM "LVM")                                                         Supports LVM devices                                                                                                                                                                                                                                                                                                                                                                                              always; hostonly: rootfs                                                                                                                                                        rootfs-block dm                                                                      [[[sys-fs/lvm2]](https://packages.gentoo.org/packages/sys-fs/lvm2)[]] (lvm, needs USE=lvm enabled), [[[sys-apps/grep]](https://packages.gentoo.org/packages/sys-apps/grep)[]] (grep)
  lvmmerge                                                                                              Merges lvm snapshots                                                                                                                                                                                                                                                                                                                                                                                              when required                                                                                                                                                                   lvm dracut-systemd systemd bash                                                      [[[sys-fs/lvm2]](https://packages.gentoo.org/packages/sys-fs/lvm2)[]] (lvm, needs USE=lvm enabled), [[[sys-apps/coreutils]](https://packages.gentoo.org/packages/sys-apps/coreutils)[]] (dd), [[[sys-apps/util-linux]](https://packages.gentoo.org/packages/sys-apps/util-linux)[]] (swapoff)
  lvmthinpool-monitor                                                                                   Monitor LVM thinpool service                                                                                                                                                                                                                                                                                                                                                                                      when required                                                                                                                                                                   lvm                                                                                  [[[sys-fs/lvm2]](https://packages.gentoo.org/packages/sys-fs/lvm2)[]] (lvm), [[[sys-apps/coreutils]](https://packages.gentoo.org/packages/sys-apps/coreutils)[]] (tr, sort), [[[app-alternatives/awk]](https://packages.gentoo.org/packages/app-alternatives/awk)[]] (awk)
  mdraid                                                                                                Adds support for mdadm arrays                                                                                                                                                                                                                                                                                                                                                                                     always; hostonly: rootfs                                                                                                                                                        rootfs-block                                                                         [[[sys-fs/mdadm]](https://packages.gentoo.org/packages/sys-fs/mdadm)[]] (mdadm)
  multipath                                                                                             Adds support for multipath devices                                                                                                                                                                                                                                                                                                                                                                                always; hostonly: rootfs                                                                                                                                                        rootfs-block dm                                                                      [[[sys-fs/multipath-tools]](https://packages.gentoo.org/packages/sys-fs/multipath-tools)[]] (multipath)
  nbd                                                                                                   Adds support for network block device devices                                                                                                                                                                                                                                                                                                                                                                     always; hostonly: rootfs                                                                                                                                                        network rootfs-block                                                                 [[[sys-block/nbd]](https://packages.gentoo.org/packages/sys-block/nbd)[]] (nbd-client)
  nvdimm                                                                                                Adds support for non-volatile DIMM devices                                                                                                                                                                                                                                                                                                                                                                        when required; hostonly: rootfs or there nvdimm devices in system - always
  nvmf                                                                                                  Adds support for [NVMe](https://wiki.gentoo.org/wiki/NVMe "NVMe") over Fabrics devices                                                                                                                                                                                                                                                                                                                            always; hostonly: rootfs                                                                                                                                                        bash rootfs-block network                                                            [[[sys-apps/nvme-cli]](https://packages.gentoo.org/packages/sys-apps/nvme-cli)[]] (nvme) [[[app-misc/jq]](https://packages.gentoo.org/packages/app-misc/jq)[]] (jq)
  pollcdrom                                                                                             Enables [CD-ROM](https://wiki.gentoo.org/wiki/CDROM "CDROM") polling                                                                                                                                                                                                                                                                                                                                              when required
  squash                                                                                                Builds SquashFS initramfs                                                                                                                                                                                                                                                                                                                                                                                         when required                                                                                                                                                                   systemd-initrd                                                                       [[[sys-fs/squashfs-tools]](https://packages.gentoo.org/packages/sys-fs/squashfs-tools)[]] (mksquashfs unsquashfs)
  squash-erofs                                                                                          Builds EROFS SquashFS initramfs                                                                                                                                                                                                                                                                                                                                                                                   when required                                                                                                                                                                                                                                                        [[[sys-fs/erofs-utils]](https://packages.gentoo.org/packages/sys-fs/erofs-utils)[]] (mkfs.erofs)
  squash-lib                                                                                            Library functions for squash modules                                                                                                                                                                                                                                                                                                                                                                              when required
  squash-squashfs                                                                                       SquashFS specific support                                                                                                                                                                                                                                                                                                                                                                                         when required                                                                                                                                                                   squash-lib                                                                           [[[sys-fs/squashfs-tools]](https://packages.gentoo.org/packages/sys-fs/squashfs-tools)[]]
  systemd-cryptsetup                                                                                    Use systemd-cryptsetup to unlock a device for `crypt`                                                                                                                                                                                                                                                                                                                                                             when required                                                                                                                                                                   dm rootfs-block crypt systemd-ask-password                                           [[[sys-apps/systemd]](https://packages.gentoo.org/packages/sys-apps/systemd)[]]
  zfcp                                                                                                  Adds support for z Systems FCP devices                                                                                                                                                                                                                                                                                                                                                                            when required
  zipl                                                                                                  Adds support for z Systems IPL                                                                                                                                                                                                                                                                                                                                                                                    when required

  Network & Communication
  biosdevname                                                                                           Enables [BIOS](https://wiki.gentoo.org/wiki/BIOS "BIOS") network device renaming.                                                                                                                                                                                                                                                                                                                                 always                                                                                                                                                                                                                                                               [[[sys-apps/biosdevname]](https://packages.gentoo.org/packages/sys-apps/biosdevname)[]] (biosdevname)
  [bluetooth](https://wiki.gentoo.org/wiki/Bluetooth "Bluetooth")                                       Includes bluetooth devices support                                                                                                                                                                                                                                                                                                                                                                                when required; hostonly: always if there bluetooth keyboard or pointing device                                                                                                  systemd dbus                                                                         [[[net-wireless/bluez]](https://packages.gentoo.org/packages/net-wireless/bluez)[]]
  [connman](https://wiki.gentoo.org/wiki/Connman "Connman")                                             Includes [[[net-misc/connman]](https://packages.gentoo.org/packages/net-misc/connman)[]] support                           when required                                                                                                                                                                   dbus systemd bash                                                                    [[[sys-apps/sed]](https://packages.gentoo.org/packages/sys-apps/sed)[]] (sed), [[[sys-apps/grep]](https://packages.gentoo.org/packages/sys-apps/grep)[]] (grep), [[[net-misc/connman]](https://packages.gentoo.org/packages/net-misc/connman)[]] (connmand, connmanctl, connmand-wait-online)
  [dbus](https://wiki.gentoo.org/wiki/Dbus "Dbus")                                        Virtual package for dbus-broker or dbus-daemon                                                                                                                                                                                                                                                                                                                                                                    when required                                                                                                                                                                   OR(dbus-broker dbus-daemon)
  dbus-broker                                                                                           Use [[[sys-apps/dbus-broker]](https://packages.gentoo.org/packages/sys-apps/dbus-broker)[]] as dbus service provider   when required                                                                                                                                                                                                                                                        [[[sys-apps/dbus-broker]](https://packages.gentoo.org/packages/sys-apps/dbus-broker)[]] (busctl, dbus-broker, dbus-broker-launch)
  dbus-daemon                                                                                           Use [[[sys-apps/dbus]](https://packages.gentoo.org/packages/sys-apps/dbus)[]] as dbus service provider                        when required; dbus-broker not in use                                                                                                                                                                                                                                [[[sys-apps/dbus]](https://packages.gentoo.org/packages/sys-apps/dbus)[]] (busctl, dbus-broker, dbus-broker-launch)
  kernel-network-modules                                                                                Includes and loads kernel modules for network devices                                                                                                                                                                                                                                                                                                                                                             when required
  network                                                                                               Virtual module for network service providers                                                                                                                                                                                                                                                                                                                                                                      when required                                                                                                                                                                   OR(connman network-manager network-legacy systemd-networkd) kernel-network-modules
  network-legacy                                                                                        Includes legacy networking tools support                                                                                                                                                                                                                                                                                                                                                                          when required                                                                                                                                                                                                                                                        [[[sys-apps/iproute2]](https://packages.gentoo.org/packages/sys-apps/iproute2)[]] (ip), [[[net-misc/dhcp]](https://packages.gentoo.org/packages/net-misc/dhcp)[]] (dhclient), [[[sys-apps/sed]](https://packages.gentoo.org/packages/sys-apps/sed)[]] (sed), [[[app-alternatives/awk]](https://packages.gentoo.org/packages/app-alternatives/awk)[]] (awk), [[[sys-apps/grep]](https://packages.gentoo.org/packages/sys-apps/grep)[]] (grep), [[[sys-apps/coreutils]](https://packages.gentoo.org/packages/sys-apps/coreutils)[]] (tr, expr), [[[net-analyzer/arping]](https://packages.gentoo.org/packages/net-analyzer/arping)[]] (arping)
  [network-manager](https://wiki.gentoo.org/wiki/NetworkManager "NetworkManager")                       Includes [[[net-misc/networkmanager]](https://packages.gentoo.org/packages/net-misc/networkmanager)[]] support      when required                                                                                                                                                                   dbus bash                                                                            [[[sys-apps/sed]](https://packages.gentoo.org/packages/sys-apps/sed)[]] (sed), [[[sys-apps/grep]](https://packages.gentoo.org/packages/sys-apps/grep)[]] (grep)
  net-lib                                                                                               Network library functions                                                                                                                                                                                                                                                                                                                                                                                         when required
  qemu-net                                                                                              Includes network kernel modules for [QEMU](https://wiki.gentoo.org/wiki/QEMU "QEMU") environment                                                                                                                                                                                                                                                                                                                  always; in hostonly when required
  znet                                                                                                  Adds support for z Systems network devices                                                                                                                                                                                                                                                                                                                                                                        when required
  ssh-client                                                                                            Includes [ssh](https://wiki.gentoo.org/wiki/SSH "SSH") and scp clients                                                                                                                                                                                                                                                                                                                                            when required                                                                                                                                                                   network                                                                              [[[net-misc/openssh]](https://packages.gentoo.org/packages/net-misc/openssh)[]] (ssh scp)
  url-lib                                                                                               Includes curl and SSL certs.                                                                                                                                                                                                                                                                                                                                                                                      when required                                                                                                                                                                   network                                                                              [[[net-misc/curl]](https://packages.gentoo.org/packages/net-misc/curl)[]] (curl)

  Hardware & Drivers
  drm                                                                                                   Includes kernel modules that provides DRM support                                                                                                                                                                                                                                                                                                                                                                 when required
  [kernel-modules](https://wiki.gentoo.org/wiki/Kernel_Modules "Kernel Modules")                        Includes and loads kernel modules for root filesystems and other boot-time devices                                                                                                                                                                                                                                                                                                                                always
  kernel-modules-extra                                                                                  Includes and loads extra out-of-tree kernel modules                                                                                                                                                                                                                                                                                                                                                               always
  numlock                                                                                               Enables NumLock on boot                                                                                                                                                                                                                                                                                                                                                                                           when required
  overlayfs                                                                                             Adds OverlayFS support                                                                                                                                                                                                                                                                                                                                                                                            when required
  pcmcia                                                                                                Adds PCMCIA support                                                                                                                                                                                                                                                                                                                                                                                               when required
  ppcmac                                                                                                PowerPC Mac specific support                                                                                                                                                                                                                                                                                                                                                                                      when required
  qemu                                                                                                  QEMU/KVM specific optimizations                                                                                                                                                                                                                                                                                                                                                                                   when required
  watchdog                                                                                              Includes watchdog devices management; works only if systemd not in use                                                                                                                                                                                                                                                                                                                                            when required                                                                                                                                                                   watchdog-modules
  watchdog-modules                                                                                      Includes watchdog kernel modules to be loaded early in booting                                                                                                                                                                                                                                                                                                                                                    when required

  Security & Access Control
  caps                                                                                                  Supports dropping capabilities before init                                                                                                                                                                                                                                                                                                                                                                        when required; not working if systemd in use                                                                                                                                    bash                                                                                 [[[sys-libs/libcap]](https://packages.gentoo.org/packages/sys-libs/libcap)[]] (capsh)
  fido2                                                                                                 Adds FIDO2 authentication support                                                                                                                                                                                                                                                                                                                                                                                 when required                                                                                                                                                                   systemd                                                                              [[[dev-libs/libfido2]](https://packages.gentoo.org/packages/dev-libs/libfido2)[]] (fido2-token)
  fips                                                                                                  Enforces FIPS security standard regulations                                                                                                                                                                                                                                                                                                                                                                       when required
  fips-crypto-policies                                                                                  Enforces FIPS crypto policies                                                                                                                                                                                                                                                                                                                                                                                     when required                                                                                                                                                                   fips
  integrity                                                                                             Adds support for Extended Verification Module                                                                                                                                                                                                                                                                                                                                                                     when required                                                                                                                                                                   masterkey securityfs
  masterkey                                                                                             Includes masterkey that can be used to decrypt other keys                                                                                                                                                                                                                                                                                                                                                         when required                                                                                                                                                                                                                                                        [[[sys-apps/keyutils]](https://packages.gentoo.org/packages/sys-apps/keyutils)[]] (keyctl) [[[sys-apps/coreutils]](https://packages.gentoo.org/packages/sys-apps/coreutils)[]] (uname)
  [modsign](https://wiki.gentoo.org/wiki/Signed_kernel_module_support "Signed kernel module support")   Adds signing kernel modules support                                                                                                                                                                                                                                                                                                                                                                               when required; in hostonly mode requires keys from /lib/modules/keys/                                                                                                                                                                                                [[[sys-apps/keyutils]](https://packages.gentoo.org/packages/sys-apps/keyutils)[]] (keyctl)
  pcsc                                                                                                  Adds support for PCSC Smart cards                                                                                                                                                                                                                                                                                                                                                                                 when required                                                                                                                                                                   systemd-udevd                                                                        [[[sys-apps/pcsc-lite]](https://packages.gentoo.org/packages/sys-apps/pcsc-lite)[]] (pcsc)
  pkcs11                                                                                                Includes PKCS#11 libraries                                                                                                                                                                                                                                                                                                                                                                                        when required                                                                                                                                                                   systemd-udevd
  securityfs                                                                                            Arranges for the securityfs to be mounted early                                                                                                                                                                                                                                                                                                                                                                   when required
  [selinux](https://wiki.gentoo.org/wiki/SELinux "SELinux")                                             Arranges for the selinux policy to be loaded                                                                                                                                                                                                                                                                                                                                                                      when required
  tpm2-tss                                                                                              Adds support for TPM2 devices                                                                                                                                                                                                                                                                                                                                                                                     when required                                                                                                                                                                   systemd-sysusers systemd-udevd                                                       [[[app-crypt/tpm2-tools]](https://packages.gentoo.org/packages/app-crypt/tpm2-tools)[]] (tpm2)

  Boot & System Services
  i18n                                                                                                  Includes keymaps, console fonts, etc.                                                                                                                                                                                                                                                                                                                                                                             always                                                                                                                                                                                                                                                               [[[sys-apps/kbd]](https://packages.gentoo.org/packages/sys-apps/kbd)[]] (setfont, loadkeys, kbd_mode)
  memstrack                                                                                             Includes memstrack for memory usage monitoring                                                                                                                                                                                                                                                                                                                                                                    always                                                                                                                                                                          systemd                                                                              [[[sys-process/procps]](https://packages.gentoo.org/packages/sys-process/procps)[]] (pgrep pkill) [[[sys-apps/memstrack]](https://packages.gentoo.org/packages/sys-apps/memstrack)[]] (memstrack)
  [plymouth](https://wiki.gentoo.org/wiki/Plymouth "Plymouth")                                          Includes boot splash support via plymouth                                                                                                                                                                                                                                                                                                                                                                         when required                                                                                                                                                                   drm                                                                                  [[[sys-boot/plymouth]](https://packages.gentoo.org/packages/sys-boot/plymouth)[]] (plymouthd plymouth plymouth-set-default-theme)
  resume                                                                                                Allows initramfs to resume from low-power state                                                                                                                                                                                                                                                                                                                                                                   always; hostonly: rootfs when local swap partition exists - always
  rngd                                                                                                  Starts random generator serive on early boot                                                                                                                                                                                                                                                                                                                                                                      when required                                                                                                                                                                   systemd                                                                              [[[sys-apps/rng-tools]](https://packages.gentoo.org/packages/sys-apps/rng-tools)[]] (rngd)
  [uefi-lib](https://wiki.gentoo.org/wiki/UEFI "UEFI")                                                  Includes UEFI tools                                                                                                                                                                                                                                                                                                                                                                                               when required                                                                                                                                                                   bash
  warpclock                                                                                             Sets kernel\'s timezone and reset the system time if adjtime is set to LOCAL                                                                                                                                                                                                                                                                                                                                      when required                                                                                                                                                                                                                                                        [[[sys-apps/util-linux]](https://packages.gentoo.org/packages/sys-apps/util-linux)[]] (hwclock)

  Utilities & Tools
  dasd                                                                                                  Adds support for z Systems DASD                                                                                                                                                                                                                                                                                                                                                                                   when required
  dasd_mod                                                                                              DASD module support                                                                                                                                                                                                                                                                                                                                                                                               when required                                                                                                                                                                   dasd
  dcssblk                                                                                               z Systems DCSS block device support                                                                                                                                                                                                                                                                                                                                                                               when required
  hwdb                                                                                                  Includes hardware database files                                                                                                                                                                                                                                                                                                                                                                                  when required
  img-lib                                                                                               Includes various tools for decompressing images                                                                                                                                                                                                                                                                                                                                                                   when required                                                                                                                                                                                                                                                        [[[app-arch/tar]](https://packages.gentoo.org/packages/app-arch/tar)[]] (tar) [[[app-arch/gzip]](https://packages.gentoo.org/packages/app-arch/gzip)[]] (gzip) [[[sys-apps/coreutils]](https://packages.gentoo.org/packages/sys-apps/coreutils)[]] (dd echo tr)
  test                                                                                                  Test module for dracut development                                                                                                                                                                                                                                                                                                                                                                                when required
  test-makeroot                                                                                         Test makeroot for dracut development                                                                                                                                                                                                                                                                                                                                                                              when required
  test-root                                                                                             Test root for dracut development                                                                                                                                                                                                                                                                                                                                                                                  when required
  zfsexpandknowledge                                                                                    ZFS expand knowledge support                                                                                                                                                                                                                                                                                                                                                                                      when required                                                                                                                                                                   zfs
  ----------------------------------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ------------------------------------------------------------------------------------ -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

-   The Enabled field indicates when a particular module will be included *by default* into the initramfs image.
-   Modules with pre-requisite packages cannot be included (even explicitly) if the required software is missing from the host.
-   Modules enabled for \"host-only: rootfs\" are included in host-only images if the active rootfs requires that module.
-   Modules enabled \"when required\" may be installed as dependency or when explicitly added via the command-line or configuration file.

### [Customizing the image]

Besides defining the list of modules to include, the final initramfs may be customized in a few other ways. The `install_items` option in the configuration file can list a number of arbitrary items to add to the image. Other options add specific elements to the image, as described below.

#### [Adding files to the image]

It is possible to add multiple files to the initramfs image. For example, adding two [firmware](https://wiki.gentoo.org/wiki/Linux_firmware "Linux firmware") files can be achieved via:

[FILE] **`/etc/dracut.conf.d/firmware.conf`**

    install_items+=" /lib/firmware/i915/kbl_guc_ver9_33.bin /lib/firmware/i915/kbl_huc_ver01_07_1398.bin "

#### [Kernel modules]

By default, the `kernel-modules` driver scans the list of available kernel modules, and installs the set of modules needed to boot a system and bring up the rootfs. This includes the hardware bus drivers (SCSI, ATA, USB, etc), keyboard drivers, block device drivers, and file system drivers. (In host-only mode, only the file systems used by the build host are included.) Update the list of installed modules via the command-line or configuration file. When specifying a kernel module name, do not include the `.ko` extension.

[FILE] **`/etc/dracut.conf`**

    # Equivalent to --drivers="module module module"
    drivers+=" module module module "

    # Equivalent to --add-drivers
    add_drivers+=" module "

    # Equivalent to --omit-drivers="module"
    omit_drivers+=" module "

    # Equivalent to --filesystems="fs fs fs"
    filesystems+=" fs fs fs "

    # Equivalent to --kmoddir="/lib/modules/fixed"
    drivers_dir="/lib/modules/fixed"

    # Equivalent to  --fwdir=":/lib/fw/alt:/lib/fw/alt2"
    fw_dir+=":/lib/fw/alt:/lib/fw/alt2"

-   In host-only mode, the running hosts filesystems are always installed, regardless of the `filesystems` parameter.

#### [Filesystems and mount points]

The default image will arrange for the rootfs and the [/usr] partition (if different) to be mounted at boot time. The build process will obtain the device and file system information it needs from [/proc/self/mountinfo]. This may not be the desired behavior, or other partitions may need to be mounted as well. To just have additional partitions mounted at boot, add them under:

[FILE] **`/etc/dracut.conf`**

    # Bring up <device> in initramfs, <device> should be the device name
    add_device+=" /dev/mapper/sysvg-home /dev/mapper/sysvg-swap /dev/mapper/hdvg-private "

To further alter the behavior of the initramfs the `fstab-sys` module is required, plus the following options:

-   Create a file called [/etc/fstab.sys], which will be copied to the initramfs and mounted.
-   Specify `use_fstab="yes"` (or `--use-fstab`), which will use the system\'s [/etc/fstab] instead of [/proc/self/mountinfo].
-   Specify `add_fstab+=" `*`filename`*` "` or `--add_fstab `*`filename`*, which will add the contents of *filename* to the initramfs\'s [/etc/fstab].
-   Specify `--mount `*`fstab mount spec`*, which adds individual entries into the initramfs\' [/etc/fstab].

(Note that `add_fstab` does not automatically trigger `fstab-sys` to be included in the image; this may be a bug, as `use_fstab` does include the module but does not actually supply an [/etc/fstab].)

#### [Elogind]

To fully support elogind, an extra command should be added to the initramfs via the dracut configuration:

[FILE] **`/etc/dracut.conf.d/elogind.conf`**

    install_items+=" /usr/lib/elogind/elogind-uaccess-command "

This will allow uaccess rules to be processed correctly.

#### [Compressing the image]

For zstd, refer to [Zstd](https://wiki.gentoo.org/wiki/Zstd#Dracut "Zstd"). Dracut uses [[[app-arch/lbzip2]](https://packages.gentoo.org/packages/app-arch/lbzip2)[]] if available for bzip2 or [[[app-arch/pigz]](https://packages.gentoo.org/packages/app-arch/pigz)[]] if available for gzip. By default, file systems are compressed with gzip.

** Warning**\
For a working system that will boot, compile the userspace compression program AND the kernel with decompression.

[FILE] **`/etc/dracut.conf.d/compression.conf`**

    # Choose compression program for the image
    compress="gzip"

## [Booting the initramfs]

Any parameters that are need to pass to the dracut modules are passed on the kernel command line. If net booting, the DHCP server can also provide command-line parameters. The dracut scripts parse the kernel command line very early in the boot process and use the information found there to adjust their behavior. The list of options, by module, can be found in the man dracut.cmdline man page.

## [Tasks]

### [ext boot]

For booting an ext(2,3,4) filesystem none of the optional dracut modules are required.

`root `[`#`]`dracut initramfs.img`

Once the image is built, the final step is to include the image in the [bootloader](https://wiki.gentoo.org/wiki/Bootloader "Bootloader"). To do this, simply add a line in [grub.conf]:

[FILE] **`/boot/grub/grub.conf`**

    kernel /boot/vmlinuz root=UUID=00000000-0000-0000-0000-000000000000
    initrd /boot/initramfs.img

It is recommended to use the UUID= (or LABEL=) form of the root specification; to guard against device names changing between boots. Find the UUID of the root device by running this command:

`root `[`#`]`ls -alF /dev/disk/by-uuid`

### [LVM on LUKS]

** Tip**\
[[[sys-fs/lvm2]](https://packages.gentoo.org/packages/sys-fs/lvm2)[]] needs the [[[lvm]](https://packages.gentoo.org/useflags/lvm)[[]](https://wiki.gentoo.org/wiki/USE_flag "USE flag")] USE flag for this.

To boot from a root residing on an [LVM](https://wiki.gentoo.org/wiki/LVM "LVM") volume located inside of an encrypted [LUKS](https://wiki.gentoo.org/wiki/Dm-crypt "Dm-crypt") container these kernel command line options can be used: `root=UUID=<root volume UUID> rd.luks.uuid=<LUKS partition UUID> rd.lvm.vg=<volume group name>`. And to enable [discard](https://wiki.gentoo.org/wiki/SSD#Discard_.28trim.29_support "SSD") `rd.luks.allow-discards` is needed. `rd.lvm.vg` might not be need depending on specific configuration but might lead to not all LVM partitions being activated. If for example the system has the following partitions:

`root `[`#`]`blkid`

    /dev/sda1: UUID="2acb7668-fff1-492d-b46e-f05ead26d153" TYPE="crypto_LUKS" PARTUUID="cbe8be3c-3bcf-0d44-9f7b-27c7ad4dd9f6"
    /dev/mapper/luks-2acb7668-fff1-492d-b46e-f05ead26d153: UUID="19Mtok-zEfG-7JXI-GXvM-Neoz-JnST-vwNlO3" TYPE="LVM2_member"
    /dev/mapper/Vg-root: UUID="199bb83d-c783-4254-a6eb-fdbb83c33144" TYPE="ext4"

the kernel command line options will look like `root=UUID=199bb83d-c783-4254-a6eb-fdbb83c33144 rd.luks.uuid=2acb7668-fff1-492d-b46e-f05ead26d153 rd.lvm.vg=Vg`.

** Note**\
In some instances it might not work to add `root` option, as Dracut also adds the default on its own. This could result in a duplication that will cause the kernel to fail.

### [NFS boot]

**Warning**: Currently Dracut does not have a proper network useflag (see [Bug 590566](https://bugs.gentoo.org/show_bug.cgi?id=590566)), so make sure that \"net-analyzer/arping\" is not installed, but instead \"net-misc/iputils\[arping\]\".

For an NFS boot, the nfs dracut module is required:

`root `[`#`]`dracut -a "nfs" initramfs-nfs-only.img`

Booting is done with the following line in the [PXE config](https://wiki.gentoo.org/wiki/Syslinux "Syslinux"). The rd.ip=auto let\'s it auto detect the NFS settings through DHCP. The NFS boot path is provided to the client through the DHCP option \"root-path\" with the following value: \<SERVER\>:\<NFS Export\>

[FILE] **`/var/lib/tftpboot/pxelinux.cfg/default`**

    ...
     APPEND initrd=initramfs-nfs-only.img rd.ip=auto root=dhcp
    ...

For more specific problems, consult official Dracut page at Fedora Wiki:

-   [https://fedoraproject.org/wiki/Dracut/Options#NFS](https://fedoraproject.org/wiki/Dracut/Options#NFS)

### [NBD boot]

For an NBD boot, the nbd dracut module is needed:

`root `[`#`]`dracut -a "nbd" initramfs-nbd-only.img`

Booting is done with the following line in the [PXE config](https://wiki.gentoo.org/wiki/Syslinux "Syslinux"). The rd.ip=auto let\'s it auto detect the NBD settings through DHCP. The NBD boot path is provided to the client through the DHCP option \"root-path\" with the following value: nbd:\<SERVER\>:\<NBD_PORT\>:\<FS\>

** Note**\
Connecting to name based exports is not documented. A code review of the module shows that specifying an export name instead of a port number is allowed and can be used to connect to name based exports.

[FILE] **`/var/lib/tftpboot/pxelinux.cfg/default`**

    ...
     APPEND initrd=initramfs-nbd-only.img rd.ip=auto root=dhcp
    ...

It is also possible to boot from a partitioned nbd device. To do this, the [PXE config](https://wiki.gentoo.org/wiki/Syslinux "Syslinux") needs to include

-   a kernel parameter \"nbd.max_part=X\" with X\>0 to load the nbd module with partition support
-   a root device setting specifying the partition to mount
-   a netroot setting as described above for the root-path.

[FILE] **`/var/lib/tftpboot/pxelinux.cfg/default`**

    ...
     APPEND initrd=initramfs-nbd-only.img rd.ip=auto nbd.max_part=X root=/dev/nbd0pY netroot=nbd:<SERVER>:<NBD_PORT|EXPORTNAME>
    ...

** Note**\
During shutdown, networking (including dhcp) and nbd-client must not be stopped, otherwise the nbd can not be unmounted cleanly. For OpenRC, this can be configured in [/etc/conf.d/net] for DHCP client daemon options and [/etc/conf.d/killprocs] to exclude nbd-client processes from being killed.

### [Debug]

For debugging the Dracut boot process, a special module is required. Including the module in the initramfs also includes several useful tools like [scp] for copying logfiles. Enable the [debug] USE flag:

`root `[`#`]`dracut -a "<other modules>" initramfs-with-debug-only.img`

Using the [rd.debug] flag, all Dracut commands are shown. When dropped to the Dracut shell, the logfile will be available in [/run/initramfs/init.log].

[FILE] **`/var/lib/tftpboot/pxelinux.cfg/default`**

    ...
     APPEND initrd=initramfs-with-debug.img rd.debug
    ...

In order to be dropped to a shell when mounting the root filesystem fails, the [rd.shell] kernel cmdline flag has to be enabled. To force dropping to a shell before mount, set the [rd.break=mount] flag. See the manpage of dracut.cmdline for more options.

** Note**\
It is possible that the typed characters are not being displayed when you are in the rescue shell. An attempt at fixing this with `stty echo` or `reset` results in error message *unable to perform all requested operations*. This is caused by plymouth, and can be fixed by blindly typing `plymouth quit` and running the command.[\[1\]](https://github.com/dracutdevs/dracut/issues/2299)

### [Other filesystems]

Other filesystems than the ones that are available through the Dracut modules can be installed using the [filesystems] parameter. To include kernel modules, the [kernel-modules] Dracut module also has to be included. This module is installed by default.

`root `[`#`]`dracut --filesystems "squashfs" initramfs-with-squashfs.img`

## [Custom modules]

Dracut allows creation of custom modules to extend initramfs functionality. Custom modules are useful for adding specialized hardware support, custom filesystems, or specific boot requirements not covered by standard modules.

### [Module structure]

A dracut module consists of a directory containing several files that define the module\'s behavior:

[FILE] **`}}`Basic module directory structure**

    /usr/lib/dracut/modules.d/99mymodule/
    ├── module-setup.sh     # Main module configuration
    ├── mymodule.sh         # Runtime script (optional)
    └── README              # Documentation (optional)

### [Creating a basic module]

The minimal requirement is a [module-setup.sh] file that defines the module\'s behavior:

[FILE] **`/usr/lib/dracut/modules.d/99mymodule/module-setup.sh`**

    #!/bin/bash

    # Called by dracut to determine if this module should be included
    check()

    # Called by dracut when building the initramfs
    install()

### [Hook scripts]

Runtime scripts are executed at specific points during boot. Common hook points include:

-   **cmdline** - Parse kernel command line parameters
-   **pre-mount** - Before mounting the root filesystem
-   **mount** - Mount the root filesystem
-   **pre-pivot** - Before switching to the real root
-   **cleanup** - Clean up before switching root

[FILE] **`/usr/lib/dracut/modules.d/99mymodule/mymodule.sh`**

    #!/bin/bash

    type getarg >/dev/null 2>&1 || . /lib/dracut-lib.sh

    # Parse kernel command line parameter
    if myoption=$(getarg mymodule.option); then
        info "mymodule: Got option: $myoption"

        # Perform custom actions
        echo "$myoption" > /tmp/mymodule-config
    fi

### [Module installation functions]

Common functions available in the [install()] function:

-   [inst] - Install a single file
-   [inst_multiple] - Install multiple files/binaries
-   [inst_hook] - Install a hook script
-   [inst_dir] - Create directories
-   [inst_binary] - Install binary with dependencies

[FILE] **`}}`Example installation commands**

    # Install configuration file
    inst /etc/myconfig.conf

    # Install multiple binaries
    inst_multiple /bin/myapp /usr/bin/myutil

    # Install hook at priority 50
    inst_hook pre-mount 50 "$moddir/myhook.sh"

    # Create directory
    inst_dir /var/lib/mymodule

### [Testing custom modules]

Test your module by building an initramfs and checking if it\'s included:

`root `[`#`]`dracut -a "mymodule" --list-modules | grep mymodule`

Build a test initramfs with verbose output:

`root `[`#`]`dracut -v -a "mymodule" /boot/test-initramfs.img`

### [Module naming and priorities]

Module directories are processed in alphabetical order. Use number prefixes to control loading order:

-   **00-** - Core system modules
-   **90-** - Standard modules
-   **99-** - Custom/local modules

### [Advanced features]

#### [Dependencies]

Specify module dependencies in the [depends()] function:

[FILE] **`}}`Module dependencies**

    depends()

#### [Conditional installation]

Use the [check()] function to conditionally include modules:

[FILE] **`}}`Conditional module inclusion**

    check()

### [Example: Custom filesystem module]

Here\'s a complete example for adding custom filesystem support:

[FILE] **`/usr/lib/dracut/modules.d/99myfs/module-setup.sh`**

    #!/bin/bash

    check()

    depends()

    install()

[FILE] **`/usr/lib/dracut/modules.d/99myfs/parse-myfs.sh`**

    #!/bin/bash

    # Check if root filesystem is myfs
    if [[ $root == myfs:* ]]; then
        info "myfs: Detected myfs root filesystem"
        # Set up myfs-specific configuration
        echo "myfs" > /tmp/rootfstype
    fi

For more advanced examples and detailed documentation, refer to the existing modules in [/usr/lib/dracut/modules.d/] and the [official dracut-ng documentation](https://dracut-ng.github.io/dracut-ng/).

## [Troubleshooting]

### [Common issues]

#### [][Boot failure: \"No root device found\"]

This usually indicates that required modules are missing from the initramfs:

`root `[`#`]`dmesg | grep -i "root"`

**Solutions:**

-   Ensure required filesystem modules are included: [btrfs], [lvm], [dm], etc.
-   Check if the correct kernel modules are loaded: [dracut -H]
-   For encrypted root: ensure [crypt] module is included
-   Verify root device UUID/LABEL: [blkid]

#### [Dracut emergency shell]

If dracut drops to an emergency shell, check these common causes:

[FILE] **`}}`Emergency shell debugging commands**

    # Check what's mounted
    mount

    # Check available block devices
    lsblk

    # Check dracut log
    journalctl -b

    # Check for kernel modules
    lsmod | grep -E "(dm_|raid|crypt)"

    # Manual root mounting (example)
    mount /dev/mapper/root /sysroot

#### [Module dependency errors]

Error: \"dracut module \'X\' will not be installed, because command \'Y\' could not be found!\"

**Solution:** Install the required package providing the missing binary:

`root `[`#`]`equery belongs Y`

Common missing dependencies:

-   [dcbtool] → [[[sys-apps/lldpad]](https://packages.gentoo.org/packages/sys-apps/lldpad)[]]
-   [fcoemon] → [[[sys-apps/fcoe-utils]](https://packages.gentoo.org/packages/sys-apps/fcoe-utils)[]]
-   [cryptsetup] → [[[sys-fs/cryptsetup]](https://packages.gentoo.org/packages/sys-fs/cryptsetup)[]]

#### [Kernel module missing]

Error: \"modprobe: FATAL: Module X not found\"

**Solutions:**

-   Verify module exists: [find /lib/modules/\$(uname -r) -name \"\*.ko\" ]
-   Rebuild initramfs with correct kernel version: [dracut \--kver \$(uname -r)]
-   Check if module is built into kernel: [zcat /proc/config.gz ]

### [Debug mode]

Enable debug mode for detailed information:

`root `[`#`]`dracut -v -H`

Add kernel parameters for runtime debugging:

-   [rd.debug] - Enable dracut debug output
-   [rd.shell] - Drop to shell on error
-   [}}] - Break before mounting root
-   [rd.info] - Show informational messages

[FILE] **`/boot/grub/grub.conf`GRUB debug entry example**

    title Gentoo Linux (debug)
    kernel /boot/vmlinuz root=UUID=xxx rd.shell rd.debug
    initrd /boot/initramfs.img

### [Network boot issues]

#### [DHCP not working]

[FILE] **`}}`Manual network configuration**

    # Set IP manually in emergency shell
    ip addr add 192.168.1.100/24 dev eth0
    ip route add default via 192.168.1.1

    # Test connectivity
    ping 8.8.8.8

Add network debugging parameters:

-   [}}] - Require network
-   [}}] - Force DHCP
-   [rd.debug] - Network debug output

#### [NFS mount failures]

Check NFS server accessibility and exports:

[FILE] **`}}`NFS debugging**

    # Test NFS server connectivity
    showmount -e nfs-server-ip

    # Manual NFS mount
    mount -t nfs server:/path /mnt

Common NFS kernel command line: [}}]

### [Recovery procedures]

#### [Rescue with working initramfs]

If you have a working backup initramfs:

`root `[`#`]`mount /boot`

`root `[`#`]`cp /boot/initramfs-backup.img /boot/initramfs-$(uname -r).img`

#### [Rescue with live media]

Boot from live media and chroot into your system:

`root `[`#`]`mount /dev/sdaX /mnt/gentoo`

`root `[`#`]`mount /dev/sdaY /mnt/gentoo/boot`

`root `[`#`]`mount -t proc proc /mnt/gentoo/proc`

`root `[`#`]`mount --rbind /dev /mnt/gentoo/dev`

`root `[`#`]`mount --rbind /sys /mnt/gentoo/sys`

`root `[`#`]`chroot /mnt/gentoo /bin/bash`

`root `[`#`]`source /etc/profile`

`root `[`#`]`dracut --force`

#### [Recreate initramfs]

Force rebuild of initramfs:

`root `[`#`]`dracut --force --verbose`

For host-only rebuild:

`root `[`#`]`dracut -H --force`

### [Logging and diagnosis]

#### [Check dracut build log]

`root `[`#`]`dracut --verbose 2>&1 | tee dracut.log`

#### [Check boot messages]

`root `[`#`]`dmesg | grep -i dracut`

`root `[`#`]`journalctl -b | grep dracut`

#### [Examine initramfs contents]

`root `[`#`]`lsinitrd /boot/initramfs-$(uname -r).img`

`root `[`#`]`lsinitrd /boot/initramfs-$(uname -r).img | grep -i module`

Extract initramfs for inspection:

`root `[`#`]`mkdir /tmp/initramfs`

`root `[`#`]`cd /tmp/initramfs`

`root `[`#`]`zcat /boot/initramfs-$(uname -r).img | cpio -idmv`

### [Performance issues]

#### [Large initramfs size]

Use host-only mode to reduce size:

`root `[`#`]`dracut -H`

List included files to identify large components:

`root `[`#`]`lsinitrd | sort -k5 -n`

Exclude unnecessary modules:

[FILE] **`/etc/dracut.conf`**

    omit_dracutmodules+=" plymouth bluetooth "

#### [Slow boot times]

Identify bottlenecks:

-   Check [systemd-analyze blame] (if using systemd)
-   Use [rd.debug] to see where time is spent
-   Consider disabling unnecessary services

### [When dracut is executed]

The following items appear as part of the output of the command *dracut* or *dracut \--force*.

#### [Bluetooth]

This is not reported as an error and the message may be expected by the user, but if it is not expected, it may cause some confusion when the service is not started.

`root `[`#`]`dracut --force`

    dracut[I]: Executing: /usr/bin/dracut
    dracut[I]: 70bluetooth: Could not find any command of '/usr/lib/bluetooth/bluetoothd /usr/libexec/bluetooth/bluetoothd'!
    ...

Check that the bluetooth service is started

`root `[`#`]`rc-status --all | grep -i bluetooth`

     bluetooth                                                           [  started  ]

The previous command should return *\[ started \]*, if it returns *\[ stopped \]*, restart the service and execute dracut again.

If the previous command doesn\'t return any result, and bluetooth is expected to be working, follow the [Bluetooth](https://wiki.gentoo.org/wiki/Bluetooth "Bluetooth") tutorial.

#### [Cryptsetup]

This is not reported as an error and the message may be expected by the user, but if it is not expected, it may cause some confusion, specially if *systemd* is not expected to be running.

`root `[`#`]`dracut --force`

    dracut[I]: Executing: /usr/bin/dracut
    ...
    dracut[I]: 70crypt: Could not find any command of '/usr/lib/systemd/systemd-cryptsetup cryptsetup'!
    ...

This message is triggered by the activation of the *crypt* module. If disk encryption is not required, the previous information message can be avoided with the following configuration.

[FILE] **`/etc/dracut.conf`**

    omit_dracutmodules+=" crypt "

#### [][NFS / rpcbind]

This is not reported as an error and the message may be expected by the user, but if it is not expected, it may cause some confusion.

`root `[`#`]`dracut --force`

    dracut[I]: Executing: /usr/bin/dracut
    ...
    dracut[I]: 74nfs: Could not find any command of 'rpcbind portmap'!
    ...

This message is triggered by the activation of the *nfs* module. If there is no need to connect to a NFS at boot time; the previous information message can be avoided with the following configuration.

[FILE] **`/etc/dracut.conf`**

    omit_dracutmodules+=" nfs "

## [See also]

-   [Initramfs](https://wiki.gentoo.org/wiki/Initramfs "Initramfs") --- is used to prepare Linux systems during boot before the **init** process starts.

## [External resources]

-   [The Official Dracut Page](https://dracut-ng.github.io/dracut-ng/)
-   [The Official Fedora Wiki Dracut Page](https://fedoraproject.org/wiki/Dracut)

## [References]

1.  [[[↑](#cite_ref-1)] [[modules.d](https://github.com/dracut-ng/dracut-ng/tree/master/modules.d), GitHub.com. dracut]]