Other languages:

-   [Deutsch](https://wiki.gentoo.org/wiki/Systemd/de "Systemd (6% translated)")
-   [English]
-   [español](https://wiki.gentoo.org/wiki/Systemd/es "Systemd (49% translated)")
-   [français](https://wiki.gentoo.org/wiki/Systemd/fr "Systemd (0% translated)")
-   [italiano](https://wiki.gentoo.org/wiki/Systemd/it "Systemd (50% translated)")
-   [magyar](https://wiki.gentoo.org/wiki/Systemd/hu "systemd (99% translated)")
-   [português do Brasil](https://wiki.gentoo.org/wiki/Systemd/pt-br "Systemd (1% translated)")
-   [svenska](https://wiki.gentoo.org/wiki/Systemd/sv "Systemd (0% translated)")
-   [русский](https://wiki.gentoo.org/wiki/Systemd/ru "Systemd (77% translated)")
-   [中文（中国大陆）‎](https://wiki.gentoo.org/wiki/Systemd/zh-cn "Systemd (48% translated)")
-   [日本語](https://wiki.gentoo.org/wiki/Systemd/ja "systemd (98% translated)")
-   [한국어](https://wiki.gentoo.org/wiki/Systemd/ko "Systemd/ko (49% translated)")

[] Some of the information in this article may have drifted out of sync with current practices. Please help out by [checking over the content](https://wiki.gentoo.org/index.php?title=Systemd&action=edit) ([how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide")).

References deprecated packages: *sys-fs/udev*, *sys-fs/eudev*, *microcode-ctl*.

**Resources**

[[![Gentoo peach graphic](/images/thumb/a/ad/Gentoo-logo-peach.svg/25px-Gentoo-logo-peach.svg.png)](https://wiki.gentoo.org/wiki/Project:Systemd "Project:Systemd")][Project](https://wiki.gentoo.org/wiki/Project:Systemd "Project:Systemd")

[[]][Home](https://freedesktop.org/wiki/Software/systemd)

[[]][Package information](https://packages.gentoo.org/packages/sys-apps/systemd)

[[]][Wikipedia](https://en.wikipedia.org/wiki/Systemd "wikipedia:Systemd")

[[]][GitHub](https://github.com/systemd/systemd/)

[[]][[#systemd](ircs://irc.libera.chat/#systemd)] ([[webchat](https://web.libera.chat/#systemd)])

[systemd] is a modern SysV-style init and [[rc](https://wiki.gentoo.org/wiki/Rc "Rc")] replacement for Linux systems. It is supported in Gentoo as an alternative [init system](https://wiki.gentoo.org/wiki/Init_system "Init system").

Switching init systems is a non trivial operation that has implications for how the system is configured, and sometimes for what software can be installed or not. Generally, an init system will be chosen at installation time (i.e. by downloading either a [systemd] or an [[openrc]](https://wiki.gentoo.org/wiki/OpenRC "OpenRC") stage3 tarball), and only changed if necessary. In true Gentoo style, in addition to [systemd] and [OpenRC], [several init systems](https://wiki.gentoo.org/wiki/Comparison_of_init_systems "Comparison of init systems") are supported.

If [systemd] is being unwantedly pulled in as a dependency, see [Gentoo without systemd](https://wiki.gentoo.org/wiki/Gentoo_without_systemd "Gentoo without systemd").

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [Kernel]](#Kernel)
        -   [[1.1.1] [Distribution Kernel]](#Distribution_Kernel)
        -   [[1.1.2] [Kernel sources]](#Kernel_sources)
    -   [[1.2] [USE flags]](#USE_flags)
    -   [[1.3] [Profile]](#Profile)
        -   [[1.3.1] [Dependency problems]](#Dependency_problems)
    -   [[1.4] [Bootloader]](#Bootloader)
        -   [[1.4.1] [GRUB]](#GRUB)
        -   [[1.4.2] [YABOOT]](#YABOOT)
        -   [[1.4.3] [In-kernel config]](#In-kernel_config)
-   [[2] [Upgrades]](#Upgrades)
-   [[3] [Configuration]](#Configuration)
    -   [[3.1] [Machine ID]](#Machine_ID)
    -   [[3.2] [Hostname]](#Hostname)
    -   [[3.3] [Locale]](#Locale)
    -   [[3.4] [Time and date]](#Time_and_date)
    -   [[3.5] [Automatic module loading]](#Automatic_module_loading)
    -   [[3.6] [Automatic mounting of partitions at boot]](#Automatic_mounting_of_partitions_at_boot)
    -   [[3.7] [Network]](#Network)
        -   [[3.7.1] [systemd-networkd]](#systemd-networkd)
        -   [[3.7.2] [systemd-resolved]](#systemd-resolved)
        -   [[3.7.3] [NetworkManager]](#NetworkManager)
    -   [[3.8] [Handling of log files]](#Handling_of_log_files)
    -   [[3.9] [/tmp is now in tmpfs]](#.2Ftmp_is_now_in_tmpfs)
    -   [[3.10] [Configure verbosity of boot process]](#Configure_verbosity_of_boot_process)
-   [[4] [Usage]](#Usage)
    -   [[4.1] [Converting traditional home directories to systemd homed]](#Converting_traditional_home_directories_to_systemd_homed)
-   [[5] [Services]](#Services)
    -   [[5.1] [Preset services]](#Preset_services)
    -   [[5.2] [OpenRC services]](#OpenRC_services)
    -   [[5.3] [Listing available services]](#Listing_available_services)
    -   [[5.4] [Enabling, disabling, starting, and stopping services]](#Enabling.2C_disabling.2C_starting.2C_and_stopping_services)
    -   [[5.5] [Installing custom unit files]](#Installing_custom_unit_files)
    -   [[5.6] [Customizing unit files]](#Customizing_unit_files)
    -   [[5.7] [Enabling a service under a custom name]](#Enabling_a_service_under_a_custom_name)
    -   [[5.8] [Native services]](#Native_services)
    -   [[5.9] [User services]](#User_services)
    -   [[5.10] [Timer services]](#Timer_services)
        -   [[5.10.1] [Emailing failures]](#Emailing_failures)
        -   [[5.10.2] [Replacing cron]](#Replacing_cron)
-   [[6] [Troubleshooting]](#Troubleshooting)
    -   [[6.1] [Slow shutdowns or reboot times due to running services]](#Slow_shutdowns_or_reboot_times_due_to_running_services)
    -   [[6.2] [/dev/kmsg buffer overrun, some messages lost]](#.2Fdev.2Fkmsg_buffer_overrun.2C_some_messages_lost)
    -   [[6.3] [Graphical sessions opened in random places]](#Graphical_sessions_opened_in_random_places)
    -   [[6.4] [LVM]](#LVM)
    -   [[6.5] [systemd-bootchart]](#systemd-bootchart)
    -   [[6.6] [syslog-ng source for systemd]](#syslog-ng_source_for_systemd)
    -   [[6.7] [sys-fs/cryptsetup configuration]](#sys-fs.2Fcryptsetup_configuration)
    -   [[6.8] [Check for units that failed to start]](#Check_for_units_that_failed_to_start)
    -   [[6.9] [Enable debug mode]](#Enable_debug_mode)
    -   [[6.10] [e4rat usage]](#e4rat_usage)
    -   [[6.11] [GRSecurity hardening]](#GRSecurity_hardening)
    -   [[6.12] [shutdown -rF does not force fsck]](#shutdown_-rF_does_not_force_fsck)
    -   [[6.13] [Optional systemd binaries]](#Optional_systemd_binaries)
-   [[7] [See also]](#See_also)
-   [[8] [External resources]](#External_resources)
-   [[9] [References]](#References)

## [Installation]

** Important**\
If updating from **\<=sys-apps/systemd-203** check the [upgrade sub-article](https://wiki.gentoo.org/wiki/Systemd/upgrade "Systemd/upgrade").

The core around which all distributions are built is the Linux kernel. It is the layer between the user programs and the system hardware. Gentoo provides its users several possible kernel sources and packages. A full listing with description is available at the [kernel packages page](https://wiki.gentoo.org/wiki/Kernel/Packages "Kernel/Packages").

For amd64-based systems, both the [[[sys-kernel/gentoo-sources]](https://packages.gentoo.org/packages/sys-kernel/gentoo-sources)[]] and [[[sys-kernel/gentoo-kernel]](https://packages.gentoo.org/packages/sys-kernel/gentoo-kernel)[]] packages are recommended for installing the kernel.

### [Kernel]

#### [Distribution Kernel]

A [Distribution Kernel](https://wiki.gentoo.org/wiki/Project:Distribution_Kernel "Project:Distribution Kernel") is used to configure, automatically build, and install the Linux kernel, its associated modules, and (optionally, but enabled by default) an initramfs file. These kernel images are ready to use for [systemd] systems, no extra configuration required.

Users looking to compile the distribution kernel may emerge the [[[sys-kernel/gentoo-kernel]](https://packages.gentoo.org/packages/sys-kernel/gentoo-kernel)[]] package:

`root `[`#`]`emerge --ask sys-kernel/gentoo-kernel`

For users not wanting to compile the distribution kernel and instead look for a prebuilt kernel image, a [[[sys-kernel/gentoo-kernel-bin]](https://packages.gentoo.org/packages/sys-kernel/gentoo-kernel-bin)[]] package exists as well:

`root `[`#`]`emerge --ask sys-kernel/gentoo-kernel-bin`

** Important**\
[*Distribution Kernels*](https://wiki.gentoo.org/wiki/Project:Distribution_Kernel "Project:Distribution Kernel") are expected to be installed alongside an [initramfs](https://wiki.gentoo.org/wiki/Initramfs "Initramfs"). Users may need to properly configure [[[sys-kernel/installkernel]](https://packages.gentoo.org/packages/sys-kernel/installkernel)[]] before running emerge as described on the [Handbook](https://wiki.gentoo.org/wiki/Handbook:AMD64/Installation/Kernel#sys-kernel.2Finstallkernel "Handbook:AMD64/Installation/Kernel").

#### [Kernel sources]

For users looking to manually configure the kernel, the [[[sys-kernel/gentoo-sources]](https://packages.gentoo.org/packages/sys-kernel/gentoo-sources)[]] package may be installed:

`root `[`#`]`emerge --ask sys-kernel/gentoo-sources`

** Note**\
[[[sys-kernel/gentoo-sources]](https://packages.gentoo.org/packages/sys-kernel/gentoo-sources)[]] is the recommended kernel source for amd64-based Gentoo systems. A vanilla kernel source is provided by [[[sys-kernel/vanilla-sources]](https://packages.gentoo.org/packages/sys-kernel/vanilla-sources)[]], but its configuration goes beyond both the [Handbook](https://wiki.gentoo.org/wiki/Handbook "Handbook") and this article.

[systemd] makes use of many modern Linux kernel features. Right now, the lower bound on kernel version is set in the ebuild to 2.6.39. In recent versions of [[[sys-kernel/gentoo-sources]](https://packages.gentoo.org/packages/sys-kernel/gentoo-sources)[]], there is a convenient way of selecting the mandatory and optional kernel options for systemd (see [Kernel/Configuration](https://wiki.gentoo.org/wiki/Kernel/Configuration "Kernel/Configuration") for further details):

[KERNEL] **Quick setup using gentoo-sources**

    Gentoo Linux --->
       Support for init systems, system and service managers --->
          [*] systemd

To configure the kernel options manually (which is the only option when not using [[[sys-kernel/gentoo-sources]](https://packages.gentoo.org/packages/sys-kernel/gentoo-sources)[]]), the following kernel configuration options are required or recommended:

[KERNEL] **Mandatory options**

    General setup  --->
        [*] Control Group support --->
            [*]   Support for eBPF programs attached to cgroups
        [ ] Enable deprecated sysfs features to support old userspace tools
        [*] Configure standard kernel features (expert users)  --->
            [*] open by fhandle syscalls
            [*] Enable eventpoll support
            [*] Enable signalfd() system call
            [*] Enable timerfd() system call
        [*] Enable bpf() system call
    [*] Networking support --->
        Networking options --->
            [*] Unix domain sockets
    Device Drivers  --->
        Generic Driver Options  --->
            [*] Maintain a devtmpfs filesystem to mount at /dev
    File systems  --->
        [*] Inotify support for userspace
        Pseudo filesystems  --->
            [*] /proc file system support
            [*] sysfs file system support

[KERNEL] **Recommended options**

    General setup  --->
        [*] Namespaces support  --->
            [*] Network namespace
    [*] Enable the block layer  --->
        [*] Block layer SG support v4
    Processor type and features  --->
        [*] Enable seccomp to safely compute untrusted bytecode
    Networking support --->
        Networking options --->
            <*> The IPv6 protocol
    Device Drivers  --->
        Generic Driver Options  --->
            ()  path to uevent helper
            [ ] Fallback user-helper invocation for firmware loading
        Firmware Drivers  --->
            [*] Export DMI identification via sysfs to userspace
    File systems --->
        <*> Kernel automounter support (supports v3, v4 and v5)
        Pseudo filesystems --->
            [*] Tmpfs virtual memory file system support (former shm fs)
            [*]   Tmpfs POSIX Access Control Lists
            [*]   Tmpfs extended attributes

For an UEFI system also enable the following:

[KERNEL] **UEFI support**

    [*] Enable the block layer  --->
        Partition Types  --->
            [*] Advanced partition selection
            [*]   EFI GUID Partition support
    Processor type and features  --->
        [*] EFI runtime service support
    Device Drivers  --->
            Firmware Drivers  --->
                    EFI (Extensible Firmware Interface) Support -->
                        <*> EFI Variable Support via sysfs

If the system is using the BFQ scheduler, it\'s recommended by BFQ upstream to enable hierarchical scheduling support:

[KERNEL] **BFQ scheduler**

    IO Schedulers  --->
        <*> BFQ I/O scheduler
            [*]   BFQ hierarchical scheduling support

For an up-to-date list, see section \"REQUIREMENTS\" in the upstream [README](https://github.com/systemd/systemd/blob/main/README) file.

### [USE flags]

### [USE flags for] [sys-apps/systemd](https://packages.gentoo.org/packages/sys-apps/systemd) [[]] [System and service manager for Linux]

  --------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------
  [`+dns-over-tls`](https://packages.gentoo.org/useflags/+dns-over-tls)       Enable DNS-over-TLS support
  [`+gcrypt`](https://packages.gentoo.org/useflags/+gcrypt)                   Enable use of dev-libs/libgcrypt for various features
  [`+kernel-install`](https://packages.gentoo.org/useflags/+kernel-install)   Enable kernel-install
  [`+kmod`](https://packages.gentoo.org/useflags/+kmod)                       Enable kernel module loading via sys-apps/kmod
  [`+lz4`](https://packages.gentoo.org/useflags/+lz4)                         Enable lz4 compression for the journal
  [`+openssl`](https://packages.gentoo.org/useflags/+openssl)                 Enable use of dev-libs/openssl for various features
  [`+resolvconf`](https://packages.gentoo.org/useflags/+resolvconf)           Install resolvconf symlink for systemd-resolve
  [`+seccomp`](https://packages.gentoo.org/useflags/+seccomp)                 Enable seccomp (secure computing mode) to perform system call filtering at runtime to increase security of programs
  [`+zstd`](https://packages.gentoo.org/useflags/+zstd)                       Enable support for ZSTD compression
  [`acl`](https://packages.gentoo.org/useflags/acl)                           Add support for Access Control Lists
  [`apparmor`](https://packages.gentoo.org/useflags/apparmor)                 Enable support for the AppArmor application security system
  [`audit`](https://packages.gentoo.org/useflags/audit)                       Enable support for sys-process/audit
  [`boot`](https://packages.gentoo.org/useflags/boot)                         Enable EFI boot manager and stub loader
  [`bpf`](https://packages.gentoo.org/useflags/bpf)                           Enable BPF support for sandboxing and firewalling.
  [`cgroup-hybrid`](https://packages.gentoo.org/useflags/cgroup-hybrid)       Default to hybrid (legacy) cgroup hierarchy instead of unified (modern).
  [`cryptsetup`](https://packages.gentoo.org/useflags/cryptsetup)             Enable cryptsetup tools (includes unit generator for crypttab)
  [`curl`](https://packages.gentoo.org/useflags/curl)                         Enable support for uploading journals
  [`elfutils`](https://packages.gentoo.org/useflags/elfutils)                 Enable coredump stacktraces in the journal
  [`fido2`](https://packages.gentoo.org/useflags/fido2)                       Enable FIDO2 support
  [`gnutls`](https://packages.gentoo.org/useflags/gnutls)                     Prefer net-libs/gnutls as SSL/TLS provider (ineffective with USE=-ssl)
  [`homed`](https://packages.gentoo.org/useflags/homed)                       Enable portable home directories
  [`http`](https://packages.gentoo.org/useflags/http)                         Enable embedded HTTP server in journald
  [`idn`](https://packages.gentoo.org/useflags/idn)                           Enable support for Internationalized Domain Names
  [`importd`](https://packages.gentoo.org/useflags/importd)                   Enable import daemon
  [`lzma`](https://packages.gentoo.org/useflags/lzma)                         Support for LZMA compression algorithm
  [`pam`](https://packages.gentoo.org/useflags/pam)                           Add support for PAM (Pluggable Authentication Modules) - DANGEROUS to arbitrarily flip
  [`passwdqc`](https://packages.gentoo.org/useflags/passwdqc)                 Use sys-auth/passwdqc for password checking in homed
  [`pcre`](https://packages.gentoo.org/useflags/pcre)                         Add support for Perl Compatible Regular Expressions
  [`pkcs11`](https://packages.gentoo.org/useflags/pkcs11)                     Enable PKCS#11 support for cryptsetup and homed
  [`policykit`](https://packages.gentoo.org/useflags/policykit)               Enable PolicyKit (polkit) authentication support
  [`pwquality`](https://packages.gentoo.org/useflags/pwquality)               Use dev-libs/libpwquality for password checking in homed
  [`qrcode`](https://packages.gentoo.org/useflags/qrcode)                     Enable qrcode output support in journal
  [`remote`](https://packages.gentoo.org/useflags/remote)                     Enable remote journal access
  [`secureboot`](https://packages.gentoo.org/useflags/secureboot)             Automatically sign efi executables using user specified key
  [`selinux`](https://packages.gentoo.org/useflags/selinux)                   !!internal use only!! Security Enhanced Linux support, this must be set by the selinux profile or breakage will occur
  [`split-usr`](https://packages.gentoo.org/useflags/split-usr)               Enable behavior to support maintaining /bin, /lib\*, /sbin and /usr/sbin separately from /usr/bin and /usr/lib\*
  [`sysv-utils`](https://packages.gentoo.org/useflags/sysv-utils)             Install sysvinit compatibility symlinks and manpages for init, telinit, halt, poweroff, reboot, runlevel, and shutdown
  [`test`](https://packages.gentoo.org/useflags/test)                         Enable dependencies and/or preparations necessary to run tests (usually controlled by FEATURES=test but can be toggled independently)
  [`tpm`](https://packages.gentoo.org/useflags/tpm)                           Enable TPM support
  [`ukify`](https://packages.gentoo.org/useflags/ukify)                       Enable systemd-ukify
  [`vanilla`](https://packages.gentoo.org/useflags/vanilla)                   Disable Gentoo-specific behavior and compatibility quirks
  [`xkb`](https://packages.gentoo.org/useflags/xkb)                           Depend on x11-libs/libxkbcommon to allow logind to control the X11 keymap
  --------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-05-09 21:13] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Profile]

Enable the `systemd` USE flag globally (in [make.conf]). The `elogind` USE flag should also be disabled to prevent conflicts with the [systemd-logind] service. It is also possible to switch to a systemd subprofile to use saner USE flags defaults in which case it is not necessary to change [make.conf]:

`root `[`#`]`eselect profile list`

Finally update the system with the new profile:

`root `[`#`]`emerge -avDN @world`

** Note**\
Once this command is complete, it is important follow the [Configuration](https://wiki.gentoo.org/wiki/Systemd#Configuration "Systemd") steps.

#### [Dependency problems]

When replacing OpenRC with systemd, several dependency problems may occur.

If [[[sys-apps/sysvinit]](https://packages.gentoo.org/packages/sys-apps/sysvinit)[]] blocks [[[sys-apps/systemd]](https://packages.gentoo.org/packages/sys-apps/systemd)[]], try disabling the `netifrc` USE flag for [[[sys-apps/openrc]](https://packages.gentoo.org/packages/sys-apps/openrc)[]]. Then rebuild OpenRC temporarily to break the dependency with [[[net-misc/netifrc]](https://packages.gentoo.org/packages/net-misc/netifrc)[]] followed by a depclean operation:

`root `[`#`]`emerge --oneshot sys-apps/openrc `

`root `[`#`]`emerge --ask --depclean`

If [[[sys-apps/sysvinit]](https://packages.gentoo.org/packages/sys-apps/sysvinit)[]] is still blocking [[[sys-apps/systemd]](https://packages.gentoo.org/packages/sys-apps/systemd)[]], make sure it and [[[sys-apps/openrc]](https://packages.gentoo.org/packages/sys-apps/openrc)[]] are not contained in the world file:

`root `[`#`]`emerge --deselect sys-apps/openrc sys-apps/sysvinit`

If [[[sys-fs/udev]](https://packages.gentoo.org/packages/sys-fs/udev)[]] blocks [[[sys-apps/systemd]](https://packages.gentoo.org/packages/sys-apps/systemd)[]], [[[sys-fs/udev]](https://packages.gentoo.org/packages/sys-fs/udev)[]] might be registered in the world file. Try to resolve this by deselecting it:

`root `[`#`]`emerge --deselect sys-fs/udev`

[[[sys-apps/systemd]](https://packages.gentoo.org/packages/sys-apps/systemd)[]] contains udev. Once installed, [[[sys-fs/udev]](https://packages.gentoo.org/packages/sys-fs/udev)[]] can be removed as systemd will be the provider for the [[[virtual/udev]](https://packages.gentoo.org/packages/virtual/udev)[]] requirement.

If the [\@system set](https://wiki.gentoo.org/wiki/System_set_(Portage) "System set (Portage)") provides [[[sys-fs/eudev]](https://packages.gentoo.org/packages/sys-fs/eudev)[]], [[[virtual/udev]](https://packages.gentoo.org/packages/virtual/udev)[]] and [[[virtual/libudev]](https://packages.gentoo.org/packages/virtual/libudev)[]] may be preventing systemd. To make portage resolve the problem, after setting the USE flag, try to reinstall the virtuals:

`root `[`#`]`emerge --oneshot virtual/udev virtual/libudev`

### [Bootloader]

** Important**\
This is no longer necessary with [[[sys-apps/systemd]](https://packages.gentoo.org/packages/sys-apps/systemd)[]] when the `sysv-utils` USE is enabled. This defaults to on with at least version 239 in Gentoo

In order to run systemd, switch the [init] that the executable kernel (or the initramfs) uses.

** Warning**\
The services that are set up for the previous service manager will not be automatically started. This is because the system is switching to a different service manager. In order to obtain back the functionality like networking or a login manager, these services will need to be enabled again. More information about this follows in the services section later in this article.

** Note**\
In case the migration yields a broken state, it is always possible to boot back into the default service manager (OpenRC) by undoing this init change step. This allows safe return and a way to follow through the troubleshooting section at the end of this article to fix the problem.

The following subsections document how to switch the [init] in one of the boot managers or the kernel.

#### [GRUB]

When [grub-mkconfig] is used, add the init option to `GRUB_CMDLINE_LINUX`:

** Note**\
This is not needed when using an initramfs generated by [dracut] with systemd inside as the initramfs already starts systemd.

[FILE] **`/etc/default/grub`Configure GRUB for systemd**

    # Append parameters to the linux kernel command line
    GRUB_CMDLINE_LINUX="init=/lib/systemd/systemd"

When the GRUB configuration file is written by hand (experts only), append the `init=` parameter to the `linux` or `linux16` command.

[FILE] **`/boot/grub/grub.cfg`Example GRUB2 configuration fragment**

    linux /vmlinuz-3.10.9 root=UUID=508868e4-54c6-4e6b-84b0-b3b28b1656b6 init=/lib/systemd/systemd

#### [YABOOT]

Yaboot is a boot loader for PowerPC-based hardware running Linux, particularly New World ROM Macintosh systems.

The `init=/lib/systemd/systemd` argument should be added directly after the kernel command-line. An example from [yaboot.conf]:

[FILE] **`/etc/yaboot.conf`Example yaboot config for systemd**

    image=/vmlinux
       append="init=/lib/systemd/systemd"
       label=Linux
       read-only
       initrd=/initramfs
       initrd-size=8192

For the changes to take effect, the [ybin] command must be run each time the [yaboot.conf] file is modified.

#### [In-kernel config]

The init configuration can also be hard-coded in the kernel configuration. See [Processor type and features -\> Built-in kernel command line]. Note that this technique works for both GRUB Legacy and GRUB.

## [Upgrades]

[systemd] has the ability to update in-place on a running system (no reboot necessary). After an upgrade to systemd has emerged, run the following command:

`root `[`#`]`systemctl daemon-reexec`

## [Configuration]

systemd supports a few system configuration files to set the most basic system details.

After installing systemd, run the following:

`root `[`#`]`systemd-machine-id-setup `

`root `[`#`]`systemd-firstboot --prompt `

`root `[`#`]`systemctl preset-all `

** Warning**\
If [systemd-firstboot] is not ran, it will automatically run on next boot. However, it interrupts the normal boot process, preventing access to the system from users who don\'t have access to the interactive console - like accessing a server via SSH.

** Note**\
While some system configuration parameters can be updated by modifying the appropriate configuration files, most settings are managed using utilities that require systemd to be running. In this case, it is safe to reboot the computer with systemd now and use the [hostnamectl], [localectl], and [timedatectl] utilities - indeed this may be required to be able to use them.

### [Machine ID]

Create a machine ID for journaling to work. This can be done through the following command:

`root `[`#`]`systemd-machine-id-setup`

** Note**\
The [systemd-machine-id-setup] command also has an impact on the `systemd-networkd` service. If this command is not run the system may exhibit strange behavior like network interfaces not coming up or network addresses not being applied.

### [Hostname]

To set the hostname, create/edit [/etc/hostname] and simply provide the desired hostname.

When booted using systemd, a tool called [hostnamectl] exists for editing [/etc/hostname] and [/etc/machine-info]. To change the hostname, run:

`root `[`#`]`hostnamectl hostname <HOSTNAME>`

Refer to [man hostnamectl] for more options.

### [Locale]

Usually, locales will be properly migrated from OpenRC when installing systemd. When required, the locale can be set in [/etc/locale.conf] as per the Gentoo handbook instructions:

[FILE] **`/etc/locale.conf`System locale configuration**

    LANG="en_US.utf8"

Once booted with systemd, the tool [localectl] is used to set locale and console or X11 keymaps. To change the system locale, run the following command:

`root `[`#`]`localectl set-locale LANG=<LOCALE>`

To change the virtual console keymap:

`root `[`#`]`localectl set-keymap <KEYMAP>`

And finally, to set the X11 layout:

`root `[`#`]`localectl set-x11-keymap <LAYOUT>`

If needed the model, variant and options can be specified as well:

`root `[`#`]`localectl set-x11-keymap <LAYOUT> <MODEL> <VARIANT> <OPTIONS>`

\
After doing any of the above, update the environment so the changes will take effect:

`root `[`#`]`env-update && source /etc/profile`

### [Time and date]

Time, date, and timezone can be set using the [timedatectl] utility. That will also allow users to set up synchronization without needing to rely on [[[net-misc/ntp]](https://packages.gentoo.org/packages/net-misc/ntp)[]] or other providers than systemd\'s own implementation.

To learn how to use [timedatectl] simply run:

`root `[`#`]`timedatectl --help`

### [Automatic module loading]

Automatic module loading is configured in a different file, or rather directory of files. The configuration files are stored in [/etc/modules-load.d]. On boot every file with a list of modules will be loaded. The file format is a list of modules separated by newlines and can have any name as long as it ends with [.conf]. The module loading can be separated by program, service or whatever way that fits personal preference. An example [virtualbox.conf] is listed below:

[FILE] **`/etc/modules-load.d/virtualbox.conf`Example file for the virtualbox modules**

    vboxdrv
    vboxnetflt
    vboxnetadp
    vboxpci

### [Automatic mounting of partitions at boot]

Systemd is capable of automatically mounting various partitions to standardized location via `systemd-gpt-auto-generator`. This makes it possible to boot and automatically mount essential partitions without an [fstab](https://wiki.gentoo.org/wiki/Fstab "Fstab") and without a `root=` paramter on the [kernel command line](https://wiki.gentoo.org/wiki/Kernel/Command-line_parameters "Kernel/Command-line parameters"). To use this capability, first systemd must be included in the [initramfs](https://wiki.gentoo.org/wiki/Initramfs "Initramfs"), this is the case by default for initramfs images generated with [Dracut](https://wiki.gentoo.org/wiki/Dracut "Dracut") on systems with systemd installed. And second, each partition must have the correct `Partition Type GUID`. A list of the most important GUIDs can be found in the `systemd-gpt-auto-generator` manual, the full list can be found on [wikipedia](https://en.wikipedia.org/wiki/GUID_Partition_Table#Partition_type_GUIDs "wikipedia:GUID Partition Table").

To list the current `Partition Type GUID` of your partitions:

`root `[`#`]`lsblk -o NAME,LABEL,PARTLABEL,PARTTYPE,PARTTYPENAME,MOUNTPOINT`

`systemd-gpt-auto-generator` can auto-mount partitions at the following locations, note that the correct GUID depends on the systems CPU architecture:

-   [/] `SD_GPT_ROOT_....`
-   [/boot/] `SD_GPT_ESP` if no [/efi/] and no XBOOTLDR partition, otherwise `SD_GPT_XBOOTLDR`
-   [/efi/] `SD_GPT_ESP` if [/efi/] is present on the root, if not then ESP is at /boot/
-   [/home/] `SD_GPT_HOME`
-   [/srv/] `SD_GPT_SRV`
-   [/usr/] `SD_GPT_USR_....`
-   [/var/] `SD_GPT_VAR`
-   [/var/tmp/] `SD_GPT_TMP`
-   Swap `SD_GPT_SWAP`

Below is an example of the most basic partition layout consisting of one [EFI System Partition](https://wiki.gentoo.org/wiki/EFI_System_Partition "EFI System Partition") and one `x86-64 root` partition.

`root `[`#`]`lsblk -o NAME,LABEL,PARTLABEL,PARTTYPE,PARTTYPENAME,MOUNTPOINT`

    NAME        LABEL    PARTLABEL            PARTTYPE                             PARTTYPENAME                 MOUNTPOINT
    nvme1n1
    ├─nvme1n1p1 ESP      EFI System Partition c12a7328-f81f-11d2-ba4b-00a0c93ec93b EFI System                   /boot
    └─nvme1n1p2 Gentoo   Gentoo               4f68bce3-e8cd-4db1-96e7-fbcaf984b709 Linux root (x86-64)          /

The `PARTTYPE` for an EFI System Partition is `c12a7328-f81f-11d2-ba4b-00a0c93ec93b`, it will be mounted at either [/efi/] or [/boot/] depending on which of these mount points is available and on if there is also an `Extended Boot Loader Partition` (`PARTTYPE=bc13c2ff-59e6-4262-a352-b275fd6f7172`) present on this disk. The `PARTTYPE` for an `x86-64 root` parition is `4f68bce3-e8cd-4db1-96e7-fbcaf984b709`.

If the `Partition Type GUID` is not correct it can be changed without data loss using a partitioning tool such as [fdisk](https://wiki.gentoo.org/wiki/Fdisk "Fdisk"). Note that the system must be offline to change the patition types! A system rescue image, or secondary operating system, must be used to complete the following steps.

Open the disk with the to be changed partition types in fdisk, in this exameple `/dev/nvme1n1` is used:

`root `[`#`]`fdisk /dev/nvme1n1`

    Welcome to fdisk (util-linux 2.39.3).
    Changes will remain in memory only, until you decide to write them.
    Be careful before using the write command.

    Command (m for help):

List the current partition layout with the `p` command:

`Command (m for help):`` p`

    Disk /dev/nvme1n1: 1.82 TiB, 2000398934016 bytes, 3907029168 sectors
    Disk model: Samsung SSD 970 EVO Plus 2TB
    Units: sectors of 1 * 512 = 512 bytes
    Sector size (logical/physical): 512 bytes / 512 bytes
    I/O size (minimum/optimal): 512 bytes / 512 bytes
    Disklabel type: gpt
    Disk identifier: B25D5B33-4A10-F940-826C-3CB24ADC7D86

    Device           Start        End    Sectors  Size Type
    /dev/nvme1n1p1    2048    1052671    1050624  513M EFI System
    /dev/nvme1n1p2 1052672 3907028991 3905976320  1.8T Linux root (x86-64)

Change the `Partition Type GUID` of any partition with the `t` command, followed by the number of the partition to be changed, and finally the alias for the desired partition type:

`Command (m for help):`` t`

    Partition number (1,2, default 2): 2
    Partition type or alias (type L to list all): L
    Partition type or alias (type L to list all): 23

    Changed type of partition 'Linux root (x86-64)' to 'Linux root (x86-64)'.

Repeat the above steps for any additional partitions of which the `Partition Type GUID` should be changed. Once completed, save the changes with the `w` command:

`Command (m for help):`` w`

** Note**\
`systemd-gpt-auto-generator` will only auto-mount partitions that reside on the same disk as the EFI System Partition that the system is being booted from.

** Tip**\
Some tools may become confused if there is no `root=` parameter on the kernel command line at all. To placate such tools add `root=/dev/gpt-auto-root` to the kernel command line. This trick is also usefull if a swapfile on the root partition is used instead of a [swap](https://wiki.gentoo.org/wiki/Swap "Swap") partition for hibernation, i.e. one may specify the resume target on the kernel command line as `resume=/dev/gpt-auto-root resume_offset=xxxxxxxxx`.

### [Network]

systemd is compatible with various [network management](https://wiki.gentoo.org/wiki/Network_management "Network management") tools.

#### [[] systemd-networkd]

See the [systemd/systemd-networkd](https://wiki.gentoo.org/wiki/Systemd/systemd-networkd "Systemd/systemd-networkd") article for details on setting up a wired network on systemd systems.

#### [[] systemd-resolved]

See the [systemd/systemd-resolved](https://wiki.gentoo.org/wiki/Systemd/systemd-resolved "Systemd/systemd-resolved") article for details on setting up address name resolution (DNS) on systemd systems.

#### [NetworkManager]

[NetworkManager](https://wiki.gentoo.org/wiki/NetworkManager "NetworkManager") is often used to configure network settings. For that purpose, simply run the following command when using a graphical desktop:

`root `[`#`]`nm-connection-editor`

If that is not the case and the network needs to be configured from console, give [nmcli] a try, or follow a guided configuration process through [nmtui]:

`root `[`#`]`nmtui`

[nmtui] is a curses frontend that will guide the user in the process while running in console mode.

For more details see the [dedicated article](https://wiki.gentoo.org/wiki/NetworkManager "NetworkManager").

### [Handling of log files]

systemd has its own way of handling log files without needing to rely on an external log system (such as [[[app-admin/syslog-ng]](https://packages.gentoo.org/packages/app-admin/syslog-ng)[]] or [[[app-admin/rsyslog]](https://packages.gentoo.org/packages/app-admin/rsyslog)[]]).

If desired, the logging service be configured to pass log messages to external logging utilities such as sysklog or syslog-ng. See [man journald.conf] to learn how to configure the systemd-journald service to suit situational needs.

systemd\'s integrated logging service writes log messages in a secure, binary format. The logs are *read* by using the [journalctl] command, which is a separate executable from the systemd-journald logging service.

** Important**\
When using systemd\'s systemd-journald.service for logging, which is typically the default for systems running systemd, standard users running the [journalctl] command will be *unable to view system logs*. To view system logs as a non-root account, users must be in one of the following three user groups in order to view system logs: **systemd-journal**, **adm**, or **wheel**. The simplest method to allow a standard user to view logs is to use the systemd-journal group. Add a user by running the following command where `larry` is the desired username:\
\

`root `[`#`]`gpasswd --add larry systemd-journal`

System logs can now be read by running [journalctl \--system] as the user(s) added in the previous command.

Some common [journalctl] options:

  ---------------------------------------------------------------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Command-line options for [journalctl]   Result
  [journalctl] without options            Show all log entries, starting with earliest.
  `-b`, `--boot`                                                                                                                     Show all log entries from the current boot.
  `-r`, `--reverse`                                                                                                                  Show the *newest* log entries first (reverse chronological order).
  `-f`, `--follow`                                                                                                                   Show the last few entries and display new log entries as they\'re being produced. This is similar to running [tail -f] in text logging utilities.
  `-p`, `--priority=`                                                                                                                Specify (minimum) priority to display messages, with a choice from: \"emerg\" (0), \"alert\" (1), \"crit\" (2), \"err\" (3), \"warning\" (4), \"notice\" (5), \"info\" (6), \"debug\" (7).
  `-S`, `--since=`, `-U`, `--until=`                                                                                                 Restrict entries by time. Accepts the format \"YYYY-MM-DD hh:mm:ss\" or the strings \"yesterday\", \"today\" and \"tomorrow\".
  `-n`, `--lines=`                                                                                                                   Restrict to a number of entries.
  `-k`, `--dmesg`                                                                                                                    Restrict to kernel messages.
  `-u`, `--unit=`                                                                                                                    Restrict to a certain systemd unit.
  `--system`                                                                                                                         View system service and kernel logs. By default, this is only possible as the root user. See [man journalctl] for how to grant standard users the ability to read the system journal.
  ---------------------------------------------------------------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

For more information and many more options, look at [man journalctl].

### [][/tmp is now in tmpfs]

Unless some other filesystem is explicitly mounted to [/tmp] in [/etc/fstab], systemd will mount [/tmp] as tmpfs. That means it will be emptied on every boot and its size will be limited to 50% of the system\'s RAM size. To know why this is the desired behavior and how to modify it, take a look at [API File Systems](https://www.freedesktop.org/wiki/Software/systemd/APIFileSystems/).

### [Configure verbosity of boot process]

When migrating to systemd users usually notice differences regarding verbosity of boot process:

-   The kernel command-line option `quiet` not only influences the kernel output, but also that of systemd itself. Then, while setting up systemd for the machine, drop the option to see any errors could arise more easily. After that, add it back to get a quiet (and faster) boot.
-   Even passing the `quiet` kernel command-line option, systemd can still be configured to show its status by also passing `systemd.show_status=1`.
-   When not using the `quiet` kernel command-line option, some messages might be overwriting consoles. This could be caused by the kernel configuration (see [man 5 proc] and look for [/proc/sys/kernel/printk]). To tweak it pass the `loglevel=5` kernel command-line parameter (and update the value according to preference, for instance set a lower value like 1).

## [Usage]

### [Converting traditional home directories to systemd homed]

See the [systemd-homed](https://wiki.gentoo.org/wiki/Systemd/systemd-homed "Systemd/systemd-homed") subarticle.

## [Services]

At some point the system will need to be rebooted in order to get systemd running (in system mode). Be sure to read all of this document to ensure systemd is configured as completely as possible before rebooting. Note that [journalctl] works with systemd not running, but that [systemctl] will not do anything useful without systemd running. Complete the service configuration (enabling and starting of services) after logging in to the system running systemd.

### [Preset services]

Most services are disabled when systemd is first installed. A \"preset\" file is provided, and may be used to enable a reasonable set of default services.

`root `[`#`]`systemctl preset-all`

### [OpenRC services]

Although systemd originally intended to support running old init.d scripts, that support is not suited well for a dependency-based RC like OpenRC and thus is completely disabled on Gentoo. OpenRC provides additional measures to ensure that init.d scripts can\'t be run when OpenRC was not used to boot the system (otherwise the results would be unpredictable).

### [Listing available services]

All available service units can be listed using the `list-units` argument of [systemctl]:

`root `[`#`]`systemctl list-units`

    UNIT                               LOAD   ACTIVE SUB       DESCRIPTION
    boot.automount                     loaded active waiting   EFI System Partition Automount
    proc-sys-fs-binfmt_misc.automount  loaded active waiting   Arbitrary Executable File Formats File System Automount Point
    ...

The following file suffixes are of interest:

  ----------------------------------------------------------------------------------------------- ------------------------------------------------------------------------------
  Suffix                                                                                          Description
  [.service]   Plain service files (e.g. ones just running a daemon directly).
  [.socket]    Socket listeners (much like *inetd*).
  [.path]      Filesystem triggers for services (running services when files change, etc.).
  ----------------------------------------------------------------------------------------------- ------------------------------------------------------------------------------

Alternatively the [systemctl] tool can be used to list all services (including implicit ones):

`root `[`#`]`systemctl --all --full`

And finally check for services that failed to start:

`root `[`#`]`systemctl --failed`

### [][Enabling, disabling, starting, and stopping services]

The usual way of enabling a service is using the following command:

`root `[`#`]`systemctl enable foo.service`

Services can be disabled likewise:

`root `[`#`]`systemctl disable foo.service`

These commands enable services using their default name in default target (both specified in \"Install\" section of the service file). However, sometimes services either don\'t provide that information or users prefer to have another name/target.

Note that these commands only enable or disable the service to be started on a next boot; to start the service right now, use:

`root `[`#`]`systemctl start foo.service`

Services can be stopped likewise:

`root `[`#`]`systemctl stop foo.service`

Services implementing `ExecReload=` can be commanded to reload their configuration without restarting itself:

`root `[`#`]`systemctl reload foo.service`

### [Installing custom unit files]

Custom unit files can be placed in [/etc/systemd/system], where they will be recognized after running [systemctl daemon-reload]:

`root `[`#`]`systemctl daemon-reload`

The [/lib/systemd/system] directory is reserved for service files installed by the package manager.

### [Customizing unit files]

When only minor changes or overrides to a unit are needed, there\'s no need to create a full copy of the original unit file in [/etc/systemd/system/] or [/lib/systemd/system/]. Overriding settings in a package management provided unit can be achieved by drop-in files in a [\*.d] directory named after the original unit (e.g. [apache2.service.d]) in [/etc/systemd/system/].

Both the drop-in directory and config file can be created using the [systemctl edit] utility or manually.

The editing utility can be invoked as:

`root `[`#`]`systemctl edit apache2.service`

[FILE] **`/etc/systemd/system/apache2.service.d/mem-limit.conf`Example of adding/overriding settings in a service file**

    [Service]
    MemoryLimit=1G

A reload of systemd is needed to inform it of the changes:

`root `[`#`]`systemctl daemon-reload`

Then the service needs to be restarted to apply the changes:

`root `[`#`]`systemctl restart apache2`

Verify that the changed property was applied to the service:

`root `[`#`]`systemctl show --property=MemoryLimit apache2`

    MemoryLimit=1074000000

** Note**\
Drop-ins add items obtained from the unit being overridden to list entries (e.g. `ExecStart=`). In order to remove the obtained items, it is necessary to first clear the list entry and then add the desired items. For example:

[FILE] **`/etc/systemd/system/foo.service.d/override.conf`Clearing ExecStart= entry in a drop-in**

    [Service]
    ExecStart=
    ExecStart=/usr/bin/bar

### [Enabling a service under a custom name]

When the name provided by `Alias=` in the unit\'s `[Install]` section does not meet the expectations and providing a permanent new value for this through a [customization](https://wiki.gentoo.org/wiki/Systemd#Customizing_unit_files "Systemd") is not desired, a symlink can be created manually in [/etc/systemd/system/\*.wants/]. The name of the [\*.wants] directory can either specify a target or another service which will depend on the new one.

For example, to install [mysqld.service] as [db.service] in the [multi-user.target]:

`root `[`#`]`ln -s /lib/systemd/system/mysqld.service /etc/systemd/system/multi-user.target.wants/db.service`

To disable the service, just remove the symlink:

`root `[`#`]`unlink /etc/systemd/system/multi-user.target.wants/db.service`

### [Native services]

Some of Gentoo packages already install systemd unit files. For these services, it is enough to enable them. A quick summary of packages installing unit files can be seen on [systemd eclass users list](https://qa-reports.gentoo.org/output/eclass-usage/systemd.txt).

The following table lists systemd services matching OpenRC ones:

  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ----------------- ---------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Gentoo package                                                                                                                                                                                                                                                                                                                                                                                            OpenRC service    systemd unit                       Notes

  [[[sys-apps/openrc]](https://packages.gentoo.org/packages/sys-apps/openrc)[]]                                       bootmisc          systemd-tmpfiles-setup.service     always enabled, uses [tmpfiles.d]

                                                                                                                                                                                                                                                                                                                                                                                                            consolefont       systemd-vconsole-setup.service     always enabled, uses [vconsole.conf]

                                                                                                                                                                                                                                                                                                                                                                                                            devfs

                                                                                                                                                                                                                                                                                                                                                                                                            dmesg

                                                                                                                                                                                                                                                                                                                                                                                                            fsck              fsck\*.service                     pulled in implicitly by mounts

                                                                                                                                                                                                                                                                                                                                                                                                            functions.sh      See note                           [[[bug #373219]](https://bugs.gentoo.org/show_bug.cgi?id=373219)[]]

                                                                                                                                                                                                                                                                                                                                                                                                            hostname          (builtin)                          [/etc/hostname]

                                                                                                                                                                                                                                                                                                                                                                                                            hwclock           See note                           always enabled as part of systemd (i.e. it is baked in and it is not a unit)

                                                                                                                                                                                                                                                                                                                                                                                                            keymaps           systemd-vconsole-setup.service     always enabled, uses [vconsole.conf]

                                                                                                                                                                                                                                                                                                                                                                                                            killprocs

                                                                                                                                                                                                                                                                                                                                                                                                            local

                                                                                                                                                                                                                                                                                                                                                                                                            localmount        local-fs.target                    actual units are created implicitly from [/etc/fstab]

                                                                                                                                                                                                                                                                                                                                                                                                            modules           systemd-modules-load.service       always enabled, uses [/etc/modules-load.d/\*.conf]

                                                                                                                                                                                                                                                                                                                                                                                                            mount-ro

                                                                                                                                                                                                                                                                                                                                                                                                            mtab

                                                                                                                                                                                                                                                                                                                                                                                                            netmount          remote-fs.target

                                                                                                                                                                                                                                                                                                                                                                                                            numlock

                                                                                                                                                                                                                                                                                                                                                                                                            procfs            (builtin)

                                                                                                                                                                                                                                                                                                                                                                                                            root              remount-rootfs.service

                                                                                                                                                                                                                                                                                                                                                                                                            savecache         n/a                                OpenRC internals

                                                                                                                                                                                                                                                                                                                                                                                                            staticroute

                                                                                                                                                                                                                                                                                                                                                                                                            swap              swap.target                        actual units are created implicitly from [/etc/fstab]

                                                                                                                                                                                                                                                                                                                                                                                                            swclock

                                                                                                                                                                                                                                                                                                                                                                                                            sysctl            systemd-sysctl.service             [sysctl.conf] and [sysctl.d/]

                                                                                                                                                                                                                                                                                                                                                                                                            sysfs             (builtin)

                                                                                                                                                                                                                                                                                                                                                                                                            termencoding      systemd-vconsole-setup.service     always enabled, uses [vconsole.conf]

                                                                                                                                                                                                                                                                                                                                                                                                            urandom           systemd-random-seed-load.service

                                                                                                                                                                                                                                                                                                                                                                                                                              systemd-random-seed-save.service

  [[[app-admin/rsyslog]](https://packages.gentoo.org/packages/app-admin/rsyslog)[]]                                 rsyslog           rsyslog.service

  [[[app-admin/syslog-ng]](https://packages.gentoo.org/packages/app-admin/syslog-ng)[]]                           syslog-ng         syslog-ng.service

  [[[media-sound/alsa-utils]](https://packages.gentoo.org/packages/media-sound/alsa-utils)[]]                  alsasound         alsa-store.service                 (enabled by default)

                                                                                                                                                                                                                                                                                                                                                                                                                              alsa-restore.socket                (enabled by default)

  [[[net-misc/dhcpcd]](https://packages.gentoo.org/packages/net-misc/dhcpcd)[]]                                       dhcpcd            dhcpcd.service

  [[[net-misc/netifrc]](https://packages.gentoo.org/packages/net-misc/netifrc)[]]                                    net.\*            net@.service                       systemd wrapper for net.\* scripts (comes with [[[net-misc/netifrc]](https://packages.gentoo.org/packages/net-misc/netifrc)[]])

                                                                                                                                                                                                                                                                                                                                                                                                                              netctl@.service                    [[[net-misc/netctl]](https://packages.gentoo.org/packages/net-misc/netctl)[]] is originally an Arch Linux tool.

                                                                                                                                                                                                                                                                                                                                                                                                                              NetworkManager.service             For \<networkmanager-0.9.8.4 : enable NetworkManager-dispatcher.service for dispatcher.d scripts to work.\
                                                                                                                                                                                                                                                                                                                                                                                                                                                                 Enable NetworkManager-wait-online.service to detect that the system has a working internet connection.\
                                                                                                                                                                                                                                                                                                                                                                                                                                                                 Disable all other managers (e.g., wicd, dhcpcd) and wpa_supplicant.

                                                                                                                                                                                                                                                                                                                                                                                                                              dhcpcd.service                     Provided by [[[net-misc/dhcpcd]](https://packages.gentoo.org/packages/net-misc/dhcpcd)[]]

                                                                                                                                                                                                                                                                                                                                                                                                                              systemd.networkd.service           Part of systemd

  [[[net-misc/openntpd]](https://packages.gentoo.org/packages/net-misc/openntpd)[]]                                 ntpd              ntpd.service

  [[[net-misc/openssh]](https://packages.gentoo.org/packages/net-misc/openssh)[]]                                    sshd              sshd.service                       runs sshd as a daemon

                                                                                                                                                                                                                                                                                                                                                                                                                              sshd.socket                        runs sshd on a inetd-like basis (for each incoming connection)

  [[[net-wireless/wpa_supplicant]](https://packages.gentoo.org/packages/net-wireless/wpa_supplicant)[]]   wpa-supplicant    wpa_supplicant.service             D-Bus controlled daemon (e.g. for [NetworkManager](https://wiki.gentoo.org/wiki/NetworkManager#Systemd "NetworkManager"))

                                                                                                                                                                                                                                                                                                                                                                                                                              wpa_supplicant@.service            interface-specific wpa_supplicant (used like [wpa_supplicant@wlan0.service])

  [[[net-print/cups]](https://packages.gentoo.org/packages/net-print/cups)[]]                                          cupsd             cups.service                       classic on-boot start up service

                                                                                                                                                                                                                                                                                                                                                                                                                              cups.socket                        socket and path activation (cups only started on-demand)

                                                                                                                                                                                                                                                                                                                                                                                                                              cups.path

  [[[net-wireless/bluez]](https://packages.gentoo.org/packages/net-wireless/bluez)[]]                              bluetooth         bluetooth.service

  [[[sys-apps/dbus]](https://packages.gentoo.org/packages/sys-apps/dbus)[]]                                             dbus              dbus.service

                                                                                                                                                                                                                                                                                                                                                                                                                              dbus.socket

  [[[sys-apps/irqbalance]](https://packages.gentoo.org/packages/sys-apps/irqbalance)[]]                           irqbalance        irqbalance.service                 supports daemon mode only

  [[[sys-apps/microcode-ctl]](https://packages.gentoo.org/packages/sys-apps/microcode-ctl)[]]                  microcode_ctl                                        Configure *microcode* as a **module** to let it load the microcode itself. Go to \"Processor type and features\" -\> \"CPU microcode loading support\" and remember to add the right option based on the system having an Intel or AMD processor.

  [[[sys-fs/udev]](https://packages.gentoo.org/packages/sys-fs/udev)[]]                                                   udev              udev.service

                                                                                                                                                                                                                                                                                                                                                                                                            udev-mount        (builtin)                          [/dev] is mounted as tmpfs

                                                                                                                                                                                                                                                                                                                                                                                                            udev-postmount    udev-trigger.service

                                                                                                                                                                                                                                                                                                                                                                                                                              udev-settle.service

  [[[sys-power/acpid]](https://packages.gentoo.org/packages/sys-power/acpid)[]]                                       acpid             acpid.service                      Most of its functionality is done by systemd itself, so consider disabling this

  [[[x11-apps/xdm]](https://packages.gentoo.org/packages/x11-apps/xdm)[]]                                                (xdm)             xdm.service                        OpenRC uses common xdm init.d installed by [[[x11-base/xorg-server]](https://packages.gentoo.org/packages/x11-base/xorg-server)[]]. With systemd the corresponding unit file for each DM (gdm.service, kdm.service\...) needs to be enabled.

  [[[net-firewall/iptables]](https://packages.gentoo.org/packages/net-firewall/iptables)[]]                     iptables          iptables-store.service

                                                                                                                                                                                                                                                                                                                                                                                                                              iptables-restore.service
  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ----------------- ---------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  : Service migration chart

### [User services]

It is possible to manage services as a per-user [systemd] instance. This allows users to setup their own services or timers.

User units can be located at multiple places. Users are allowed to place them to [\$XDG_CONFIG_HOME/systemd/user/]. Installed packages place them to [/usr/lib/systemd/user/].

User services use `--user` [systemctl] option. For example to start a [mpd] user service:

`user `[`$`]`systemctl --user start mpd`

### [Timer services]

Since version 197 systemd supports timers, making [cron](https://wiki.gentoo.org/wiki/Cron "Cron") unnecessary on a systemd system. Since version 212 persistent services are supported, replacing even anacron. Persistent timers are run at the next opportunity if the system was powered down when the timer was scheduled to run.

The following is an example on how to make a simple timer that runs in the context of a user. It will even run if the user is not logged in. Every timed service needs a timer and a service unit file that is activated by the timer as follows:

[FILE] **`~/.config/systemd/user/backup-work.timer`Example of a timer running every working day**

    [Unit]
    Description=daily backup work
    RefuseManualStart=no
    RefuseManualStop=no

    [Timer]
    Persistent=false
    OnCalendar=Mon-Fri *-*-* 11:30:00
    Unit=backup-work.service

    [Install]
    WantedBy=default.target

[FILE] **`~/.config/systemd/user/backup-work.service`Example of a service triggering backup**

    [Unit]
    Description=daily backup work
    RefuseManualStart=no
    RefuseManualStop=yes

    [Service]
    Type=oneshot
    ExecStart=/home/<user>/scripts/backup-work.sh

These unit files can be created either manually or using the [systemctl edit] utility:

`user `[`$`]`systemctl edit --force --full --user backup-work.timer`

When creating the unit files manually, the files are to be placed in the [\~/.config/systemd/user] directory. It may need to be created for the relevant user:

`user `[`$`]`mkdir -p ~/.config/systemd/user`

To have a timer run while the user is not logged in, be sure to enable lingering sessions:

`user `[`$`]`loginctl enable-linger <username>`

First, tell systemd to rescan the service files:

`user `[`$`]`systemctl --user daemon-reload`

As a user, it is possible to trigger the backup manually by running the following command:

`user `[`$`]`systemctl --user start backup-work.service`

Start and stop the timer manually as follows:

`user `[`$`]`systemctl --user start backup-work.timer `

`user `[`$`]`systemctl --user stop backup-work.timer`

Finally, to activate the timer at every system start, run:

`user `[`$`]`systemctl --user enable backup-work.timer`

To check the last results of running the service:

`user `[`$`]`systemctl --user list-timers`

#### [Emailing failures]

If a timed service runs and fails an e-mail can be send out to inform the user or administrator. This is possible with the \"OnFailure\" stanza which specifies what should happen if a service fails. A failure is detected by a non-zero return code of the invoked script.

For that change the script as follows:

[FILE] **`~/.config/systemd/user/backup-work.service`Example of a service triggering backup**

    [Unit]
    Description=daily backup work
    RefuseManualStart=no
    RefuseManualStop=yes
    OnFailure=failure-email@%i.service

    [Service]
    Type=oneshot
    ExecStart=/home/<user>/scripts/backup-work.sh

This requires to have the service [failure-email@.service] installed, which can be found in [kylemanna\'s systemd-utils repository](https://github.com/kylemanna/systemd-utils/tree/master/onfailure).

#### [Replacing cron]

The above timer and service files can also be added to [/lib/systemd/system] to make them available system-wide. The install section should then say `WantedBy=multi-user.target` to enable the service at system start.

However, cron also runs the scripts in [/etc/cron.daily] and other locations. Several packages place scripts there that they expect to be run daily. This behavior can be emulated with systemd by installing [[[sys-process/systemd-cron]](https://packages.gentoo.org/packages/sys-process/systemd-cron)[]]. Then activate the new cron replacement with the following commands:

`root `[`#`]`systemctl enable cron.target `

`root `[`#`]`systemctl start cron.target`

## [Troubleshooting]

-   [[[Gentoo bugtracker: known bugs]](https://bugs.gentoo.org/buglist.cgi?quicksearch=systemd&order=bug_id%20DESC)[]]
-   [[[Freedesktop.org bugtracker: known bugs]](https://bugs.freedesktop.org/buglist.cgi?bug_status=UNCONFIRMED&bug_status=NEW&bug_status=CONFIRMED&bug_status=ASSIGNED&bug_status=REOPENED&bug_status=NEEDINFO&bug_status=PLEASETEST&bug_status=IN_PROGRESS&product=systemd&component=&order=bug_id%20DESC)[]]
-   [Upstream debugging guide](https://freedesktop.org/wiki/Software/systemd/Debugging/)
-   [systemd-analyze verify] to get readable warnings and errors associated with the given systemd unit

### [Slow shutdowns or reboot times due to running services]

Problem

<!-- -->

Solution

[FILE] **`/etc/systemd/system.conf.d/system.conf`Reduce default timeout to 10s for hanging system services**

    [Manager]
    DefaultTimeoutStopSec=10s

[FILE] **`~/.config/systemd/user.conf`Reduce default timeout to 10s for hanging user services**

    [Manager]
    DefaultTimeoutStopSec=10s

### [][/dev/kmsg buffer overrun, some messages lost]

Problem

<!-- -->

Solution

### [Graphical sessions opened in random places]

By default systemd only launches a [getty] process when it\'s going to be used. This causes some display managers (like GDM) to use the remaining TTYs for opening graphical sessions on demand, which can result in having consoles and graphical sessions placed randomly depending on the order they were used.

To stick with a more \"classical\" behavior (i.e, consoles placed from [tty1] to [tty6] and graphical sessions using the remaining TTYs) force it to always launch [getty] on those:

`root `[`#`]`systemctl enable getty@tty.service`

### [LVM]

When switching from OpenRC to systemd and LVM is needed to properly mount the system volumes, activate the LVM service:

`root `[`#`]`systemctl enable lvm2-monitor.service`

While it might not be needed for activation of the root volume (if LVM is integrated into the initramfs) it might not work for other LVM volumes, unless the service is activated.

### [systemd-bootchart]

Make sure that `CONFIG_DEBUG_KERNEL`, `CONFIG_SCHED_DEBUG`, and `CONFIG_SCHEDSTATS` are enabled.

[KERNEL] **Enable systemd-bootchart support**

    File systems  --->
        Pseudo filesystems --->
        [*] /proc file system support
    Kernel hacking  --->
        [*] Kernel debugging
        [*] Collect scheduler debugging info
        [*] Collect scheduler statistics

Next, enable [systemd-bootchart.service]:

`root `[`#`]`systemctl enable systemd-bootchart`

The result of the changes will produce a bootchart report in SVG format located in [/run/log/] after each boot. It can be viewed using a modern web browser.

As an alternative to systemd-bootchart the starting of services can be visualized with:

`root `[`#`]`systemd-analyze plot > plot.svg`

### [syslog-ng source for systemd]

There is *no need* to add `unix-dgram('/dev/log');` to the [/etc/syslog-ng/syslog-ng.conf] config file. It will cause [syslog-ng] to fail (at least on version syslog-ng-3.7.2). Update the `source src ;` line mentioned in the [syslog-ng article](https://wiki.gentoo.org/wiki/Syslog-ng#Sources "Syslog-ng") as follows:

[FILE] **`/etc/syslog-ng/syslog-ng.conf`**

    # default config for openrc
    #source src ;

    # systemd
    source src ;

### [][sys-fs/cryptsetup configuration]

systemd does not seem to respect [/etc/conf.d/dmcrypt] (see [[[bug #429966]](https://bugs.gentoo.org/show_bug.cgi?id=429966)[]]) so it needs to be configured through the [/etc/crypttab] file:

[FILE] **`/etc/crypttab`Configuration file for encrypted block devices**

    crypt-home UUID=c25dd0f3-ecdd-420e-99a8-0ff2eaf3f391 -

Make sure to enable the `cryptsetup` USE flag for [[[sys-apps/systemd]](https://packages.gentoo.org/packages/sys-apps/systemd)[]]. It will install [/lib/systemd/system-generators/systemd-cryptsetup-generator] that will automatically create a service (`cryptsetup@crypt-home.service` for above example) for each entry on boot.

### [Check for units that failed to start]

Check for units that failed to start with:

`root `[`#`]`systemctl --failed`

### [Enable debug mode]

To get more informations set the following in [/etc/systemd/system.conf]:

[FILE] **`/etc/systemd/system.conf`**

    LogLevel=debug

Or enable the debug-shell, that opens a terminal at tty9. This helps to debug services during the boot process.

`root `[`#`]`systemctl enable debug-shell.service`

### [e4rat usage]

Please remember to edit [/etc/e4rat.conf] setting \'init\' to [/lib/systemd/systemd], otherwise it will keep booting OpenRC.

### [GRSecurity hardening]

With grsecurity enabled, systemd-networkd might log the following error:

[CODE] **systemd-networkd error**

    could not find udev device: Permission denied

The error raises due to systemd-networkd working under a non-root user with grsecurity refusing access to the complete [/sys] structure for such users. To disable this option, disable the `CONFIG_GRKERNSEC_SYSFS_RESTRICT` kernel option.

logind may also have subtle permission issues with `CONFIG_GRKERNSEC_PROC` active, see [[[bug #472098]](https://bugs.gentoo.org/show_bug.cgi?id=472098)[]].

### [shutdown -rF does not force fsck]

The [systemd-fsck] service is responsible of running [fsck] when needed. It doesn\'t honor [shutdown]\'s `-rF` option, but instead honors the following kernel boot parameters.

  ----------------------- ----------------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Boot parameter          Supported options       Description

  `fsck.mode`             `auto`\                 Controls the mode of operation. The default is `auto`, and ensures that file system checks are done when the file system checker deems them necessary. `force` unconditionally results in full file system checks. `skip` skips any file system checks.
                          `force`\
                          `skip`

  `fsck.repair`           `preen`\                Controls the mode of operation. The default is `preen`, and will automatically repair problems that can be safely fixed. `yes` will answer yes to all questions by fsck and `no` will answer no to all questions.
                          `yes`\
                          `no`
  ----------------------- ----------------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### [Optional systemd binaries]

Many optional systemd binaries can be built by setting certain use flags. An incomplete mapping of USE flag to binary is below.

  ----------------------------------- -----------------------------------------------------------------------------------------------------------------------------
  USE flag                            Additional binary built

  `curl`                              [/lib/systemd/systemd-journal-upload]

  `http`                              [/lib/systemd/systemd-journal-gatewayd]\
                                      [/lib/systemd/systemd-journal-remote]
  ----------------------------------- -----------------------------------------------------------------------------------------------------------------------------

## [See also]

-   [systemd/systemd-homed](https://wiki.gentoo.org/wiki/Systemd/systemd-homed "Systemd/systemd-homed") --- provides instructions to migrate home directories from their traditional structure into the encrypted by default, portable concept provided by systemd\'s homed.
-   [systemd/systemd-boot](https://wiki.gentoo.org/wiki/Systemd/systemd-boot "Systemd/systemd-boot") --- a minimal [UEFI](https://wiki.gentoo.org/wiki/UEFI "UEFI") boot manager.
-   [systemd/systemd-nspawn](https://wiki.gentoo.org/wiki/Systemd/systemd-nspawn "Systemd/systemd-nspawn") --- a lightweight, loosely [chroot](https://wiki.gentoo.org/wiki/Chroot "Chroot")-like, OS-level [OCI container](https://opencontainers.org/) environment native to [systemd].
-   [Comparison of init systems](https://wiki.gentoo.org/wiki/Comparison_of_init_systems "Comparison of init systems") --- compares and contrasts **[init systems](https://wiki.gentoo.org/wiki/Init_system "Init system")** for Unix(like) [OSs](https://en.wikipedia.org/wiki/Operating_system "wikipedia:Operating system")
-   [Hard dependencies on systemd](https://wiki.gentoo.org/wiki/Hard_dependencies_on_systemd "Hard dependencies on systemd") --- a (possibly partial) list of packages in Gentoo\'s repository that unconditionally require [systemd]
-   [OpenRC to systemd Cheatsheet](https://wiki.gentoo.org/wiki/OpenRC_to_systemd_Cheatsheet "OpenRC to systemd Cheatsheet") --- list of commands commonly used in OpenRC and its equivalent systemd command.

## [External resources]

-   [FAQ](https://www.freedesktop.org/wiki/Software/systemd/FrequentlyAskedQuestions/)
-   [Tips and tricks](https://www.freedesktop.org/wiki/Software/systemd/TipsAndTricks/)
-   [Mastering systemd: Securing and sandboxing applications and services (RedHat)](https://www.redhat.com/sysadmin/mastering-systemd)

## [References]

1.  [[[↑](#cite_ref-1)] [[https://forums.gentoo.org/viewtopic-t-977530-postdays-0-postorder-asc-start-25.html](https://forums.gentoo.org/viewtopic-t-977530-postdays-0-postorder-asc-start-25.html) Retrieved on March 12th, 2016]]