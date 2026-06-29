This page contains [[changes](https://wiki.gentoo.org/index.php?title=OpenRC&oldid=1414759&diff=1423084)] which are not marked for translation.

Other languages:

-   [Deutsch](https://wiki.gentoo.org/wiki/OpenRC/de "OpenRC/de (13% translated)")
-   [English]
-   [español](https://wiki.gentoo.org/wiki/OpenRC/es "OpenRC (94% translated)")
-   [italiano](https://wiki.gentoo.org/wiki/OpenRC/it "OpenRC (83% translated)")
-   [magyar](https://wiki.gentoo.org/wiki/OpenRC/hu "OpenRC (94% translated)")
-   [čeština](https://wiki.gentoo.org/wiki/OpenRC/cs "OpenRC/cs (1% translated)")
-   [русский](https://wiki.gentoo.org/wiki/OpenRC/ru "OpenRC (81% translated)")
-   [中文（中国大陆）‎](https://wiki.gentoo.org/wiki/OpenRC/zh-cn "OpenRC/zh-cn (1% translated)")
-   [日本語](https://wiki.gentoo.org/wiki/OpenRC/ja "OpenRC (98% translated)")

**Resources**

[[![Gentoo peach graphic](/images/thumb/a/ad/Gentoo-logo-peach.svg/25px-Gentoo-logo-peach.svg.png)](https://wiki.gentoo.org/wiki/Project:OpenRC "Project:OpenRC")][Project](https://wiki.gentoo.org/wiki/Project:OpenRC "Project:OpenRC")

[[]][Official documentation](https://github.com/OpenRC/openrc/blob/master/README.md)

[[]][Official documentation](https://github.com/OpenRC/openrc/blob/master/user-guide.md)

[[]][Package information](https://packages.gentoo.org/packages/sys-apps/openrc)

[[]][Wikipedia](https://en.wikipedia.org/wiki/OpenRC "wikipedia:OpenRC")

[[]][GitHub](https://github.com/OpenRC/openrc)

[[]][[#openrc](ircs://irc.libera.chat/#openrc)] ([[webchat](https://web.libera.chat/#openrc)])

**Article status**

[[]]This article has some todo items:\

-   Review for accuracy & test.
-   Complete to cover most basic usage under Gentoo.
-   Rework for precision, readability, concision\...
-   Section [BusyBox Integration](https://wiki.gentoo.org/wiki/OpenRC#BusyBox_integration "OpenRC") needs testing and documenting (or removing).

**OpenRC** is a dependency-based [init system](https://en.wikipedia.org/wiki/Init "wikipedia:Init") for Unix-like systems that maintains compatibility with the system-provided [init system](https://wiki.gentoo.org/wiki/Init_system "Init system"), normally located in [/sbin/init].

OpenRC will start necessary system services in the correct order at boot, manage them while the system is in use, and stop them at shutdown. It can manage daemons installed from the Gentoo repository, can optionally supervise the processes it launches, and has the possibility to start processes in parallel - when possible - to shorten boot time.

Gentoo officially supports both OpenRC and [systemd](https://wiki.gentoo.org/wiki/Systemd "Systemd"), but [other init systems are available](https://wiki.gentoo.org/wiki/Comparison_of_init_systems "Comparison of init systems").

OpenRC was developed for Gentoo, but is designed to be used in [other Linux distributions and BSD systems](https://wiki.gentoo.org/wiki/OpenRC/Users "OpenRC/Users"). By default, OpenRC is invoked by [sysvinit](https://wiki.gentoo.org/wiki/Sysvinit "Sysvinit"), on Gentoo.

Daemons installed from outside the Gentoo repository, e.g. software downloaded as source code and compiled manually, may sometimes need to be adapted to work with OpenRC (which is sometimes trivial).

** Note**\
See the [OpenRC documentation section](https://wiki.gentoo.org/wiki/OpenRC#OpenRC_documentation "OpenRC") for links to the documentation provided by the OpenRC project itself. See the [Handbook](https://wiki.gentoo.org/wiki/Handbook:AMD64/Working/Initscripts "Handbook:AMD64/Working/Initscripts") for information on how OpenRC works with the init system.

## Contents

-   [[1] [Implementation]](#Implementation)
-   [[2] [Installation]](#Installation)
    -   [[2.1] [USE flags]](#USE_flags)
-   [[3] [Configuration]](#Configuration)
    -   [[3.1] [Files]](#Files)
    -   [[3.2] [Logging]](#Logging)
    -   [[3.3] [Network management]](#Network_management)
    -   [[3.4] [Dependency behavior]](#Dependency_behavior)
    -   [[3.5] [Selecting a specific runlevel at boot]](#Selecting_a_specific_runlevel_at_boot)
-   [[4] [Usage]](#Usage)
    -   [[4.1] [Runlevels]](#Runlevels)
        -   [[4.1.1] [Listing]](#Listing)
        -   [[4.1.2] [Named runlevels]](#Named_runlevels)
        -   [[4.1.3] [Stacked runlevels]](#Stacked_runlevels)
    -   [[4.2] [Prefix]](#Prefix)
    -   [[4.3] [Hotplug]](#Hotplug)
    -   [[4.4] [CGroups support]](#CGroups_support)
    -   [[4.5] [Chroot support]](#Chroot_support)
    -   [[4.6] [User services]](#User_services)
        -   [[4.6.1] [Lingering]](#Lingering)
        -   [[4.6.2] [Service start on boot (lingering)]](#Service_start_on_boot_.28lingering.29)
        -   [[4.6.3] [Service start on login (no lingering)]](#Service_start_on_login_.28no_lingering.29)
            -   [[4.6.3.1] [PAM-based auto-start]](#PAM-based_auto-start)
            -   [[4.6.3.2] [KDE Compatibility]](#KDE_Compatibility)
-   [[5] [System integration]](#System_integration)
    -   [[5.1] [systemd compatibility]](#systemd_compatibility)
        -   [[5.1.1] [logind]](#logind)
        -   [[5.1.2] [tmpfiles.d]](#tmpfiles.d)
    -   [[5.2] [udev and mdev]](#udev_and_mdev)
    -   [[5.3] [BusyBox integration]](#BusyBox_integration)
-   [[6] [Troubleshooting]](#Troubleshooting)
    -   [[6.1] [Respawning crashed services]](#Respawning_crashed_services)
    -   [[6.2] [Manually recovering crashed services]](#Manually_recovering_crashed_services)
-   [[7] [See also]](#See_also)
-   [[8] [External resources]](#External_resources)
    -   [[8.1] [OpenRC documentation]](#OpenRC_documentation)
        -   [[8.1.1] [Man pages]](#Man_pages)

## [[] Implementation]

OpenRC does not require large, fundamental, changes to the traditional Unix-like system. OpenRC integrates with other system software as a component of a modular and flexible system. It is designed to be fast, lightweight, easily configurable, and adaptable. OpenRC has only a few basic dependencies, on core system components.

As a modern init system, OpenRC provides a number of useful features:

-   [cgroups](https://wiki.gentoo.org/wiki/OpenRC/CGroups "OpenRC/CGroups") support.
-   Process supervision.
-   Dependency-based launch, with parallel startup of services.
-   Automatic resolving, and ordering, of dependencies.
-   Hardware initiated initscripts.
-   Setting `ulimit` and `nice` values per service through the `rc_ulimit` variable.
-   Permits complex init scripts that start multiple components.
-   Modular architecture, fitting into existing infrastructure.
-   OpenRC has its own optional [init system](https://wiki.gentoo.org/wiki/Init_system "Init system") called [openrc-init], see [OpenRC/openrc-init](https://wiki.gentoo.org/wiki/OpenRC/openrc-init "OpenRC/openrc-init") for details.
-   OpenRC has its own optional process supervisor, see [OpenRC/supervise-daemon](https://wiki.gentoo.org/wiki/OpenRC/supervise-daemon "OpenRC/supervise-daemon") for details.

See the [comparison of init systems](https://wiki.gentoo.org/wiki/Comparison_of_init_systems "Comparison of init systems") article for more information on init systems.

## [[] Installation]

OpenRC generally does not need installing manually, and is provided as part of an OpenRC [profile](https://wiki.gentoo.org/wiki/Profile_(Portage) "Profile (Portage)") on [installation](https://wiki.gentoo.org/wiki/Handbook:AMD64/Installation/Base#Choosing_the_right_profile "Handbook:AMD64/Installation/Base"). It will be present in the [stage 3 tarball](https://wiki.gentoo.org/wiki/Handbook:AMD64/Installation/Stage#OpenRC "Handbook:AMD64/Installation/Stage"), and will be maintained across system updates.

### [[] USE flags]

### [USE flags for] [sys-apps/openrc](https://packages.gentoo.org/packages/sys-apps/openrc) [[]] [OpenRC manages the services, startup and shutdown of a host]

  ----------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [`+netifrc`](https://packages.gentoo.org/useflags/+netifrc)       enable Gentoo\'s network stack (net.\* scripts)
  [`+sysvinit`](https://packages.gentoo.org/useflags/+sysvinit)     control the dependency on sysvinit (experimental)
  [`audit`](https://packages.gentoo.org/useflags/audit)             Enable support for Linux audit subsystem using sys-process/audit
  [`bash`](https://packages.gentoo.org/useflags/bash)               enable the use of bash in service scripts (experimental)
  [`debug`](https://packages.gentoo.org/useflags/debug)             Enable extra debug codepaths, like asserts and extra output. If you want to get meaningful backtraces see https://wiki.gentoo.org/wiki/Project:Quality_Assurance/Backtraces
  [`newnet`](https://packages.gentoo.org/useflags/newnet)           enable the new network stack (experimental)
  [`pam`](https://packages.gentoo.org/useflags/pam)                 Add support for PAM (Pluggable Authentication Modules) - DANGEROUS to arbitrarily flip
  [`s6`](https://packages.gentoo.org/useflags/s6)                   install s6-linux-init
  [`selinux`](https://packages.gentoo.org/useflags/selinux)         !!internal use only!! Security Enhanced Linux support, this must be set by the selinux profile or breakage will occur
  [`sysv-utils`](https://packages.gentoo.org/useflags/sysv-utils)   Install sysvinit compatibility scripts for halt, init, poweroff, reboot and shutdown
  [`unicode`](https://packages.gentoo.org/useflags/unicode)         Add support for Unicode
  ----------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-05-10 22:49] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

If the USE flags are modified, the package may be rebuilt to apply changes. For OpenRC [profiles](https://wiki.gentoo.org/wiki/Profile_(Portage) "Profile (Portage)"), [[[sys-apps/openrc]](https://packages.gentoo.org/packages/sys-apps/openrc)[]] is pulled in as a dependency of [[[virtual/service-manager]](https://packages.gentoo.org/packages/virtual/service-manager)[]], thus it should never be added to the [selected-packages set](https://wiki.gentoo.org/wiki/Selected-packages_set_(Portage) "Selected-packages set (Portage)") ([/var/lib/portage/world] file) - the [`--oneshot` option](https://wiki.gentoo.org/wiki/Emerge#Do_not_add_dependencies_to_the_world_file "Emerge") avoids adding OpenRC to this set.

`root `[`#`]`emerge --ask --oneshot sys-apps/openrc`

## [[] Configuration]

### [[] Files]

[/etc/rc.conf]

[/etc/conf.d]

### [[] Logging]

OpenRC doesn\'t log anything by default. To log OpenRC\'s output during boot, uncomment and set the `rc_logger` option in [/etc/rc.conf]. The log will be saved at [/var/log/rc.log] by default.

[FILE] **`/etc/rc.conf`**

    rc_logger="YES"
    #rc_log_path="/var/log/rc.log"

### [[] Network management]

OpenRC can be used with one of several network managers or even with none. By default, with Gentoo\'s [OpenRC profiles](https://wiki.gentoo.org/wiki/Profile_(Portage) "Profile (Portage)"), [netifrc](https://wiki.gentoo.org/wiki/Netifrc "Netifrc") scripts are utilized to manage network connections.

See the [Network manager](https://wiki.gentoo.org/wiki/Network_manager "Network manager") article for a list of options on network management.

### [[] Dependency behavior]

Changing the default dependencies of init scripts, might be needed to fit more complex setups. See [/etc/rc.conf] for how to change the default behavior; notice the *rc_depend_strict* option. In addition, next networking examples show how flexible OpenRC can be.

*Multiple network interfaces (example)*

The [SSH service](https://wiki.gentoo.org/wiki/SSH "SSH") must come up with the internal network, for instance *eth0* and never *wlan0*.

Overrule the \"net\" dependency from [/etc/init.d/sshd], and refine it to depend on \"net.eth0\":

[FILE] **`/etc/conf.d/sshd`**

    rc_need="!net net.eth0"

*Multiple network interfaces in multiple runlevels (example)*

The SSH service must start with *eth0* (not *wlan0*) in \"default\" runlevel, but in \"office\" runlevel it must start with *wlan0* (not *eth0*).

Keep the default:

[FILE] **`/etc/rc.conf`**

    #rc_depend_strict="YES"

Make additional symlinks to [sshd] with the network interface names:

`root `[`#`]`ln -s sshd /etc/init.d/sshd.eth0 `

`root `[`#`]`ln -s sshd /etc/init.d/sshd.wlan0 `

Settings are read from [/etc/conf.d/sshd.eth0] and [/etc/conf.d/sshd.wlan0] now:

`root `[`#`]`cp /etc/conf.d/sshd /etc/conf.d/sshd.eth0 `

`root `[`#`]`cp /etc/conf.d/sshd /etc/conf.d/sshd.wlan0 `

Add the dependencies:

`root `[`#`]`echo 'rc_need="!net net.eth0"' >> /etc/conf.d/sshd.eth0 `

`root `[`#`]`echo 'rc_need="!net net.wlan0"' >> /etc/conf.d/sshd.wlan0 `

In this example *net.eth0* and *net.wlan0* read their settings from [/etc/conf.d/net], or [/etc/conf.d/net.office] depending on the active runlevel. Add all runscripts to the different runlevels:

`root `[`#`]`rc-update add sshd.eth0 default `

`root `[`#`]`rc-update add sshd.wlan0 office `

`root `[`#`]`rc-update add net.eth0 default office `

`root `[`#`]`rc-update add net.wlan0 default office `

To switch between \"default\" runlevel and \"office\" runlevel without rebooting the computer, change to \"nonetwork\" runlevel in between. The network interfaces will be stopped this way, and re-read their runlevel specific configuration. This works best when \"nonetwork\" is a *stacked runlevel* in both the \"default\" and \"office\" runlevels, and the display manager and other non-network services are added to the \"nonetwork\" runlevel only.

    default runlevel <---> nonetwork runlevel <---> office runlevel

`root `[`#`]`openrc nonetwork && openrc office `

`root `[`#`]`openrc nonetwork && openrc default `

### [[] Selecting a specific runlevel at boot]

OpenRC reads the kernel command-line used at boot time, and will start the runlevel specified by the `softlevel` parameter if provided. If no `softlevel` parameter is provided, the *default* runlevel will be used.

The following example shows a [grub](https://wiki.gentoo.org/wiki/GRUB "GRUB") configuration allowing to choose to boot into either the *default* or *nonetwork* runlevels:

[FILE] **`/boot/grub/grub.conf`Example grub.conf (GRUB Legacy)**

    title=Regular Start-up

    kernel (hd0,0)/boot/kernel-3.7.10-gentoo-r1 root=/dev/sda3

    title=Start without Networking

    kernel (hd0,0)/boot/kernel-3.7.10-gentoo-r1 root=/dev/sda3 softlevel=nonetwork

See below for a description of how to add additional runlevels.

## [[] Usage]

### [[] Runlevels]

OpenRC can be controlled and configured using [openrc], [rc-update] and [rc-status] commands.

Delete a service from default runlevel, where `<service>` is the name of the service to be removed:

`root `[`#`]`rc-update delete <service> default`

#### [[] Listing]

It is not necessary to have root permissions to list runlevels and services (init scripts) assigned to them.

Use [rc-update show -v] to display all available init scripts and their current runlevel (if they have been added to one):

`user `[`$`]`rc-update show -v`

Running [rc-update] or [rc-update show] will display only the init scripts that have been added to a runlevel.

Alternatively, the [rc-status] command can be used with the `--servicelist` (`-s`) option to view the state of all services:

`user `[`$`]`rc-status --servicelist`

#### [[] Named runlevels]

OpenRC runlevels are implemented as directories living in [/etc/runlevels]. Additional runlevels (indicated as `<runlevel>` below) may be created by using:

`root `[`#`]`install -d /etc/runlevels/<runlevel>`

Additional runlevels are helpful to provide alternative system start-up profiles.

#### [[] Stacked runlevels]

Stacked runlevels are used to allow a runlevel to inherit the actions of one or more other runlevels. The command variant used to create stacked runlevels is [rc-update -s]. Adding a runlevel to another runlevel causes a dependency to be created such that any init scripts (services) in any dependent (stacked) runlevels are started or stopped when the target runlevel is started or stopped.

An usage example for using stacked runlevel on laptop to group networking services based on location is at [OpenRC/Stacked runlevel](https://wiki.gentoo.org/wiki/OpenRC/Stacked_runlevel "OpenRC/Stacked runlevel").

### [[] Prefix]

[Gentoo Prefix](https://wiki.gentoo.org/wiki/Project:Prefix "Project:Prefix") installs Gentoo within an offset, known as a prefix, allowing users to install Gentoo in another location in the filesystem hierarchy, hence avoiding conflicts. Next to this offset, Gentoo Prefix runs unprivileged, meaning no root user or rights are required to use it.

By using an offset (the \"prefix\" location), it is possible for many \"alternative\" user groups to benefit from a large part of the packages in the Gentoo Linux Portage tree. Currently users of the following systems successfully run Gentoo Prefix: Mac OS X on PPC and x86, Linux on x86, x86_64 and ia64, Solaris 10 on Sparc, Sparc/64, x86 and x86_64, FreeBSD on x86, AIX on PPC, Interix on x86, Windows on x86 (with the help of Interix), HP-UX on PARISC and ia64.

OpenRC runscript already support prefix-installed daemons, during the Summer of Code 2012 work will be done to implement full secondary/session daemon behavior to complete the overall feature set provided by Prefix.

[OpenRC/Prefix](https://wiki.gentoo.org/wiki/OpenRC/Prefix "OpenRC/Prefix"), a tutorial for trying it out.

### [[] Hotplug]

OpenRC can be triggered by external events, such as new hardware from udev. This is what the configuration file says about hotplugged services:

[FILE] **`/etc/rc.conf`rc_hotplug**

    # rc_hotplug controls which services we allow to be hotplugged.
    # A hotplugged service is one started by a dynamic dev manager when a matching
    # hardware device is found.
    # Hotplugged services appear in the "hotplugged" runlevel.
    # If rc_hotplug is set to any value, we compare the name of this service
    # to every pattern in the value, from left to right, and we allow the
    # service to be hotplugged if it matches a pattern, or if it matches no
    # patterns. Patterns can include shell wildcards.
    # To disable services from being hotplugged, prefix patterns with "!".
    # If rc_hotplug is not set or is empty, all hotplugging is disabled.
    # Example - rc_hotplug="net.wlan !net.*"
    # This allows net.wlan and any service not matching net.* to be hotplugged.
    # Example - rc_hotplug="!net.*"
    # This allows services that do not match "net.*" to be hotplugged.

### [[] CGroups support]

OpenRC starting with version 0.12 has extended cgroups support. See [OpenRC/CGroups](https://wiki.gentoo.org/wiki/OpenRC/CGroups "OpenRC/CGroups") for details. Since OpenRC 0.51, unified cgroups (v2) is enabled by default.

### [[] Chroot support]

`root `[`#`]`mkdir -p /lib64/rc/init.d`

`root `[`#`]`ln -s /lib64/rc/init.d /run/openrc `

`root `[`#`]`touch /run/openrc/softlevel `

`root `[`#`]`emerge --oneshot sys-apps/openrc `

[FILE] **`/etc/rc.conf`OpenRC config file**

    rc_sys="prefix"
    rc_controller_cgroups="NO"
    rc_depend_strict="NO"
    rc_need="!net !dev !udev-mount !sysfs !checkfs !fsck !netmount !logger !clock !modules"

The system may report the following message upon attempting to start a service:

    * WARNING: <service> is already starting

This may be fixed by issuing the following command:

`root `[`#`]`rc-update --update`

### [[] User services]

User services are services that run as the specific user they belong to. Starting with version 0.60, OpenRC has support for user services.

OpenRC user service support requires an `XDG_RUNTIME_DIR` to be set, since user services store state in [\$/openrc/]; thus, a mechanism for setting `XDG_RUNTIME_DIR` is required. That could be [[[sys-auth/elogind]](https://packages.gentoo.org/packages/sys-auth/elogind)[]], the shell\'s rc files as well as any other method of creating the directory and setting the environment variable. While system OpenRC service scripts are loaded from [/etc/init.d/], scripts for user services are loaded from [/etc/user/init.d/]. User configurations are located in [/etc/user/conf.d/] respectively. Configuration options defined in [\$/rc/conf.d/] override options set in [/etc/user/conf.d/], and options set in [\$/rc/rc.conf] override those in [/etc/rc.conf]. If `XDG_CONFIG_HOME` is unset, OpenRC uses [\~/.config] as a default value.

#### [[] Lingering]

In the context of systemd, lingering is a mechanism ensuring the presence of a user session for a specific user. A session is created on system startup and this session is guaranteed to persist until shutdown, even if the user logs in or out. Thus, services run on behalf of this user are preserved throughout the entire runtime of the system. While lingering itself is implemented by the session daemon (`logind` in case of systemd), there are methods to achieve the similar results on an OpenRC-based system.

Although [[[sys-auth/elogind]](https://packages.gentoo.org/packages/sys-auth/elogind)[]] has an `--enable-linger <user>` option that should work with the PAM-based auto-start, it is recommended to enable the [OpenRC user-specific session](#User_service_start_boot) that achieves the same effect.

#### [][[] Service start on boot (lingering)]

** Note**\
Due to a [bug](https://github.com/OpenRC/openrc/issues/929), this currently does not work when the PAM-based auto-start is enabled (which it is by default). PAM-based auto-start can be disabled by adding `rc_autostart_user="NO"` to [/etc/rc.conf].

To enable per-user services for a user (`<user>` is the name of the user), create a symlink [/etc/init.d/user.\<name\>] pointing to [/etc/init.d/user]. This service starts an OpenRC user session that then handles all services enabled for the user.

`root `[`#`]`ln -s /etc/init.d/user /etc/init.d/user.<user> `

`root `[`#`]`rc-update add user.<user> `

Enable a service for a user with:

`user `[`$`]`rc-update --user add <service> `

The service to enable must be present in [/etc/user/init.d]. All OpenRC commands (`rc-update`, `rc-service`, `rc-status` etc.) have a `--user` (`-U`) flag to act on the OpenRC user session instead of the system session.

#### [][[] Service start on login (no lingering)]

The OpenRC session is only active while the user is logged in (see [#lingering](#lingering)). As soon as the user logs out, the session is terminated.

##### [PAM-based auto-start]

** Note**\
This behavior is enabled by default since the [stabilization](https://www.gentoo.org/support/news-items/2025-09-04-openrc-user-services.html) of user services.

The provided `pam_openrc.so` can automatically start openrc on login. It\'s loaded from [/etc/pam.d/system-login], and dynamically starts [/etc/init.d/user] script, multiplexed for the user logging in, which launches the `openrc-user` daemon.

`openrc-user` opens another pam session for the user, which will last as long as any given session using pam_openrc is active. It loads [/etc/pam.d/openrc-user] as the pam stack for the new session, then proceeds to launch the `default` runlevel for the user via calling the user\'s login shell with `-c` as an argument, and creating [\$/rc/runlevels/default] should it not exist.

In order to make use of the PAM-based auto-start, `XDG_RUNTIME_DIR` must be set during the login process, either by a pam module or shell rc file.

##### [KDE Compatibility]

KDE has some issues with the OpenRC 0.62.10. If you want to use user services with it then you\'ll need to make some changes to your system:

-   KDE (Qt) fails to find the DBus socket created by the DBus Session user service.
-   Gentoo bundles an Auto-start desktop file for PipeWire which conflicts with the user services ([[[bug #964059]](https://bugs.gentoo.org/show_bug.cgi?id=964059)[]]). See also [PipeWire#User_Services](https://wiki.gentoo.org/wiki/PipeWire#User_Services "PipeWire").

To correct Qt not being able to find the session socket, the following profile script will be needed (or you can just paste this into [\~/.bash_profile] instead if you prefer not to enable this system wide):

[CODE] **[/etc/profile.d/zz-dbus-hack.sh]**

    #!/bin/sh
    if [ -z "$DBUS_SESSION_BUS_ADDRESS" ]; then
        export DBUS_SESSION_BUS_ADDRESS="unix:path=$/bus"
    fi

To disable the conflicting autostart file, add `Hidden=true` to it. It\'s also possible to copy `pipewire.desktop` to [\$/autostart] \[Default: `XDG_CONFIG_HOME=~/.config`\] to create a local override for only the current user if you prefer.

[CODE] **Disable autostart file: [/etc/xdg/autostart/pipewire.desktop]**

    echo 'Hidden=true' >> /etc/xdg/autostart/pipewire.desktop

Once this is done, you can enable `dbus`, `pipewire`, `pipewire-pulse` and `wireplumber` with `rc-update --user add $service_name default`. After logging out and logging in, all services should now be running and are able to be used by KDE.

## [[] System integration]

### [[] systemd compatibility]

#### [[] logind]

Some setups require systemd-logind. [Elogind](https://wiki.gentoo.org/wiki/Elogind "Elogind") can be a suitable replacement as a standalone logind running with OpenRC.

#### [[] tmpfiles.d]

systemd has a special tmpfiles.d file syntax for managing temporary files. [[[sys-apps/systemd-utils\[tmpfiles\]]](https://packages.gentoo.org/packages/sys-apps/systemd-utils)[]] is a standalone provider for OpenRC systems.

Both can also be used to manage volatile entries in [/sys] or [/proc].

### [[] udev and mdev]

[udev](https://wiki.gentoo.org/wiki/Udev "Udev") and [mdev](https://wiki.gentoo.org/wiki/Mdev "Mdev") are systems available on Gentoo to manage [/dev]. [eudev](https://wiki.gentoo.org/wiki/Eudev "Eudev") used to be available as well, but has been removed. udev is available for OpenRC via the [[[sys-apps/systemd-utils\[udev\]]](https://packages.gentoo.org/packages/sys-apps/systemd-utils)[]] package, however should be able to work with both on Gentoo.

Older Gentoo installs used udev as the main [[[virtual/udev]](https://packages.gentoo.org/packages/virtual/udev)[]] provider. Based on [[[bug #575718]](https://bugs.gentoo.org/show_bug.cgi?id=575718)[]] this was changed to eudev, but it was changed back to udev in [[[bug #807193]](https://bugs.gentoo.org/show_bug.cgi?id=807193)[]]. However, the rc service is still [/etc/init.d/udev].

See [mdev](https://wiki.gentoo.org/wiki/Mdev "Mdev"), for possible use, e.g. for embedded systems.

### [[] BusyBox integration]

N.B. This section lacks information on how to actually use BusyBox with OpenRC.

Please note that there are currently many BusyBox applets that are incompatible with OpenRC, see [[[bug #529086]](https://bugs.gentoo.org/show_bug.cgi?id=529086)[]] for details. **Be warned that using OpenRC with BusyBox may require some work to set up.** BusyBox is more adapted to embedded use, see previous section about mdev.

[BusyBox](https://wiki.gentoo.org/wiki/Busybox "Busybox") can be used to replace most of the userspace utilities needed by OpenRC ([init], shell, [awk], and other POSIX tools), by using a complete BusyBox as the shell for OpenRC [\[1\]](https://github.com/OpenRC/openrc/blob/master/BUSYBOX.md), all the calls that normally would cause a fork/exec would be spared, improving the overall speed.

The SysV-init [/etc/inittab] file provided by Gentoo is not compatible with the BusyBox [init]. Here is an example inittab compatible with BusyBox:

[FILE] **`/etc/inittab`Example inittab compatible with BusyBox init**

    ::sysinit:/sbin/openrc sysinit
    ::wait:/sbin/openrc boot
    ::wait:/sbin/openrc

BusyBox provides a number of applets that could be used to replace third party software like acpid or dhcp/dhcpcd.

See the OpenRC documentation on [using BusyBox with OpenRC](https://github.com/OpenRC/openrc/blob/master/BUSYBOX.md).

## [[] Troubleshooting]

### [[] Respawning crashed services]

OpenRC can return state of services to runlevel setting state, to provide stateful init scripts and automatic respawning.

To respawn crashed services from the default runlevel, run [openrc]: crashed services will be started and any manually-run services will be stopped. To keep manually-started services running, run [openrc \--no-stop] or [openrc -n], for short.

By default [openrc] will attempt to *start* crashed services, not to *restart* them. This can be controlled by the rc_crashed_stop (default NO) and rc_crashed_start (default YES) options in [/etc/rc.conf].

### [[] Manually recovering crashed services]

When a process crashes while starting, an error or warning message will be printed when trying to start, stop, or show the status of a service. For example, when using the \"docker\" service:

`root `[`#`]`rc-service docker status`

     * status: crashed

`root `[`#`]`rc-service docker start`

     * WARNING: docker has already been started

`root `[`#`]`rc-service docker stop`

     * Caching service dependencies ...                                                                                                  [ ok ]
     * Stopping docker ...
     * Failed to stop docker                                                                                                             [ !! ]
     * ERROR: docker failed to stop

To remedy this situation, zap the service:

`root `[`#`]`rc-service docker zap `

## [[] See also]

-   [OpenRC/CGroups](https://wiki.gentoo.org/wiki/OpenRC/CGroups "OpenRC/CGroups") --- OpenRC includes support for [cgroups](https://wiki.gentoo.org/wiki/Cgroups "Cgroups").
-   [OpenRC/openrc-init](https://wiki.gentoo.org/wiki/OpenRC/openrc-init "OpenRC/openrc-init") --- OpenRC\'s own init system
-   [OpenRC/Prefix](https://wiki.gentoo.org/wiki/OpenRC/Prefix "OpenRC/Prefix") --- The following guideline applies to a Gentoo [Prefix](https://wiki.gentoo.org/wiki/Prefix "Prefix") on RHEL-5.6 amd64 and on Debian 6.0 amd64, for other setups it should be similar.
-   [OpenRC/Stacked runlevel](https://wiki.gentoo.org/wiki/OpenRC/Stacked_runlevel "OpenRC/Stacked runlevel") --- a tutorial for setting up complicated networking with the help of stacked runlevel.
-   [OpenRC/supervise-daemon](https://wiki.gentoo.org/wiki/OpenRC/supervise-daemon "OpenRC/supervise-daemon") --- OpenRC\'s daemon supervisor
-   [OpenRC/Users](https://wiki.gentoo.org/wiki/OpenRC/Users "OpenRC/Users") --- an (incomplete) list of distributions and operating systems using OpenRC.
-   [/etc/local.d](https://wiki.gentoo.org/wiki//etc/local.d "/etc/local.d") --- **[/etc/local.d/]** can contain small programs or light scripts to be run when the local service is started or stopped.
-   [Gentoo AMD64 Handbook - Initscript system](https://wiki.gentoo.org/wiki/Handbook:AMD64/Working/Initscripts "Handbook:AMD64/Working/Initscripts")
-   The main OpenRC configuration file, [/etc/rc.conf], contains extensive comments documenting OpenRC configuration.

## [[] External resources]

### [[] OpenRC documentation]

OpenRC has its own useful documentation, maintained by the OpenRC developers themselves. Be aware that Gentoo does not use all of OpenRC\'s functionality by default:

-   [README](https://github.com/OpenRC/openrc/blob/master/README.md)
-   [User Guide](https://github.com/OpenRC/openrc/blob/master/user-guide.md)
-   [OpenRC init process guide](https://github.com/OpenRC/openrc/blob/master/init-guide.md) - How to [use OpenRC\'s own init system](https://wiki.gentoo.org/wiki/OpenRC/openrc-init "OpenRC/openrc-init") (not used by default in Gentoo).
-   [agetty guide](https://github.com/OpenRC/openrc/blob/master/agetty-guide.md) - Setting up the agetty service in OpenRC (By default, ttys are spawned with [sysvinit](https://wiki.gentoo.org/wiki/Sysvinit#Gentoo.27s_sysvinit_setup "Sysvinit") in Gentoo).
-   [Using runit with OpenRC](https://github.com/OpenRC/openrc/blob/master/runit-guide.md)
-   [Using S6 with OpenRC](https://github.com/OpenRC/openrc/blob/master/s6-guide.md)
-   [Using supervise-daemon](https://github.com/OpenRC/openrc/blob/master/supervise-daemon-guide.md) - [Optional process supervision](https://wiki.gentoo.org/wiki/OpenRC/supervise-daemon "OpenRC/supervise-daemon").
-   [Using BusyBox with OpenRC](https://github.com/OpenRC/openrc/blob/master/BUSYBOX.md)
-   [Service script writing guide](https://github.com/OpenRC/openrc/blob/master/service-script-guide.md) - For developers or packagers.
-   [NEWS](https://github.com/OpenRC/openrc/blob/master/NEWS.md) - Important information about each release.
-   [HISTORY](https://github.com/OpenRC/openrc/blob/master/HISTORY.md) - History of how OpenRC came to be.

#### [Man pages]

-   [[[openrc(8)]](https://man.archlinux.org/man/openrc.8.en)[[]](https://wiki.gentoo.org/wiki/Special:MyLanguage/man_page "Special:MyLanguage/man page")] - Stops and starts services for the specified runlevel.
-   [[[openrc-run(8)]](https://man.archlinux.org/man/openrc-run.8.en)[[]](https://wiki.gentoo.org/wiki/Special:MyLanguage/man_page "Special:MyLanguage/man page")] - Interpreter used to process OpenRC service scripts.
-   [[[rc-service(8)]](https://man.archlinux.org/man/rc-service.8.en)[[]](https://wiki.gentoo.org/wiki/Special:MyLanguage/man_page "Special:MyLanguage/man page")] - Locate and run an OpenRC service with the given arguments.
-   [[[rc-status(8)]](https://man.archlinux.org/man/rc-status.8.en)[[]](https://wiki.gentoo.org/wiki/Special:MyLanguage/man_page "Special:MyLanguage/man page")] - Show status info about runlevels.
-   [[[rc-update(8)]](https://man.archlinux.org/man/rc-update.8.en)[[]](https://wiki.gentoo.org/wiki/Special:MyLanguage/man_page "Special:MyLanguage/man page")] - Add and remove services to and from a runlevel.