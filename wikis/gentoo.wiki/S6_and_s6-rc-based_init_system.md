**This page has been [nominated for deletion](https://wiki.gentoo.org/wiki/Help:Deleting_a_page "Help:Deleting a page")**

The given reason is: ***Page contents have been consolidated into \"S6\" article in main namespace.***

If there is any reason not to delete this page, *do not remove this notice*, but please open a discussion on the associated [talk page](https://wiki.gentoo.org/wiki/Talk:S6_and_s6-rc-based_init_system) (this should delay deletion until the discussion is resolved).

\

[   Note to admins] []

Please remember to check [if anything links here](https://wiki.gentoo.org/wiki/Special:WhatLinksHere/S6_and_s6-rc-based_init_system "Special:WhatLinksHere/S6 and s6-rc-based init system") and [the page history](https://wiki.gentoo.org/index.php?title=S6_and_s6-rc-based_init_system&action=history) before deleting.

This notice should remain for a *minimum of 1 month* after it was placed on the page. If discussion is still ongoing it should remain until a consensus is reached (check the talk page), at which time the page may be deleted or this notice may be removed.

If the page has only been edited by the user who nominated it for deletion and/or is in the nominator\'s user space, then more flexibility in the decision may be allowed.

**Check the [help page on deleting](https://wiki.gentoo.org/wiki/Help:Deleting_a_page#For_admins "Help:Deleting a page") for more information.**

** Note**\
A draft consolidation and restructure of this page and the [S6](https://wiki.gentoo.org/wiki/S6 "S6") page is available [here](https://wiki.gentoo.org/wiki/User:Flexibeast/drafts/S6 "User:Flexibeast/drafts/S6"); it is currently awaiting review by a Gentoo dev.

An s6 and s6-rc-based init system is an init system built using components from the [s6](https://wiki.gentoo.org/wiki/S6 "S6"), [s6-rc](https://wiki.gentoo.org/wiki/S6-rc "S6-rc") and [s6-linux-init](https://wiki.gentoo.org/wiki/S6-linux-init "S6-linux-init") packages. It can be used as alternative to [sysvinit](https://wiki.gentoo.org/wiki/Sysvinit "Sysvinit") + [OpenRC](https://wiki.gentoo.org/wiki/OpenRC "OpenRC"), or [systemd](https://wiki.gentoo.org/wiki/Systemd "Systemd").

## Contents

-   [[1] [General setup]](#General_setup)
-   [[2] [The boot sequence]](#The_boot_sequence)
    -   [[2.1] [The stage1 init]](#The_stage1_init)
    -   [[2.2] [The stage2 init]](#The_stage2_init)
    -   [[2.3] [s6-rc initialization]](#s6-rc_initialization)
-   [[3] [The catch-all logger]](#The_catch-all_logger)
    -   [[3.1] [The catch-all logger\'s FIFO]](#The_catch-all_logger.27s_FIFO)
-   [[4] [Shutdown and reboot]](#Shutdown_and_reboot)
    -   [[4.1] [The shutdown daemon]](#The_shutdown_daemon)
    -   [[4.2] [The s6-svscan diverted signal handlers]](#The_s6-svscan_diverted_signal_handlers)
    -   [[4.3] [Compatibility scripts]](#Compatibility_scripts)
-   [[5] [Service management]](#Service_management)
-   [[6] [Runlevels]](#Runlevels)
-   [[7] [Historical notes]](#Historical_notes)
-   [[8] [See also]](#See_also)
-   [[9] [External resources]](#External_resources)

## [General setup]

** Warning**\
While Gentoo does offer s6, s6-rc and s6-linux-init packages in its official repository, it does not completely support using them to make an init system. Gentoo users who want to do that might need to use [alternative ebuild repositories](https://wiki.gentoo.org/wiki/Ebuild_repository "Ebuild repository") and/or do some local tweaking.

The general setup of an s6 and s6-rc-based init system is as follows:

1.  When the machine boots, all initialization tasks needed to bring it to its stable, normal \'up and running\' state, are split into a [stage1 init](#stage1) and a [stage2 init](#stage2). The stage1 init is the [s6-linux-init] program from the package of the same name, which is invoked by the kernel, runs as process 1, and replaces itself with the [s6-svscan] program from [s6](https://wiki.gentoo.org/wiki/S6 "S6") when its work is done. The stage2 init is invoked by the stage1 init, runs as a child of process 1, blocks until [s6-svscan] starts to execute, and exits when its work is done.
2.  During most of the machine\'s uptime, [s6-svscan] [runs as process 1](https://wiki.gentoo.org/wiki/S6#s6process1 "S6") with [signal diversion turned on](https://wiki.gentoo.org/wiki/S6#s6signaldivert "S6"), and there is an s6 supervision tree rooted in process 1, that is launched as soon as [s6-svscan] starts to execute.
3.  A supervised [catch-all logger](#logger) is started as part of the supervision tree. The catch-all logger logs messages sent by supervision tree processes to [s6-svscan]\'s standard output and error, supporting a [logging chain arrangement](https://wiki.gentoo.org/wiki/S6#loggingchain "S6"). The catch-all logger is optional since s6-linux-init version 1.0.4.0; if one is not set up, messages that would be logged by it are printed to the machine\'s console instead.
4.  The stage2 init [initializes the s6-rc service manager](#s6rcsetup) and starts a subset of the services defined in the boot-time compiled service database. Some of these s6-rc-managed services might carry out part of the machine\'s initialization tasks.
5.  While [s6-svscan] is running as process 1, services are normally [managed using s6-rc tools](https://wiki.gentoo.org/wiki/S6-rc#manage "S6-rc"). The [s6-linux-init-telinit] program in combination with the runlevel changer service created by the [s6-linux-init-maker] program (both from package s6-linux-init) allows the implementation of [sysvinit-like runlevels](#runlevels).
6.  The administrator initiates the machine\'s shutdown sequence using the [s6-linux-init-shutdown] program or the [s6-linux-init-hpr] program, both from package s6-linux-init. These programs communicate with a special supervision tree process, the [shutdown daemon](#shutdownd), which then takes care of the shutdown sequence, including the stopping of all s6-rc-managed services, and finally halts, powers off or reboots the machine.

## [The boot sequence]

### [The stage1 init]

When the machine starts booting (if an [initramfs](https://wiki.gentoo.org/wiki/Initramfs "Initramfs") is being used, after it passes control to the \'main\' init), a *stage1 init* executes as process 1. This is usually a simple execline script wrapper (e.g. as created by [s6-linux-init-maker]) around the [s6-linux-init] program [from the package of the same name](https://wiki.gentoo.org/wiki/S6-linux-init#stage1 "S6-linux-init"). Using a script allows passing options to [s6-linux-init], which would otherwise have to be present in the kernel command line.

Therefore, if the wrapper script is named, for example, [s6-gentoo-init], and placed in [/sbin], to use an s6 and s6-rc-based init system, an `init=/sbin/s6-gentoo-init` argument can be added to the kernel\'s command line using the [bootloader](https://wiki.gentoo.org/wiki/Bootloader "Bootloader")\'s available mechanisms (e.g. a [linux] command in some \'Gentoo with s6 + s6-rc + s6-linux-init\' menu entry for [GRUB](https://wiki.gentoo.org/wiki/GRUB "GRUB")). It is possible to go back to sysvinit + OpenRC at any time, or to any other init system, by reverting the change. Alternatively, the wrapper script can be the [/sbin/init] file, in which case the `init=` parameter is not needed, but this would conflict on Gentoo with [sysvinit](https://wiki.gentoo.org/wiki/Sysvinit "Sysvinit") or with [systemd](https://wiki.gentoo.org/wiki/Systemd "Systemd") if it was installed with the `sysv-utils` [USE flag](https://wiki.gentoo.org/wiki/USE_flag "USE flag").

[s6-linux-init] runs with its standard input, output and error initially redirected to the machine\'s console. It does all necessary setup for [s6-svscan], including setting up its scan directory. Because at that point in the boot sequence the root filesystem might be the only mounted filesystem, and possibly read-only, [s6-linux-init] also mounts a tmpfs (at [/run] on Gentoo) as a read-write filesystem to hold control files that [s6-svscan] and [s6-supervise] need to write to. [s6-linux-init] uses a directory called the *run image*, that contains the initial scan directory, and copies it to the read-write tmpfs as a directory named [service]. When [s6-svscan] starts running as process 1, it uses the directory in the tmpfs as its scan directory (so its absolute pathname would be [/run/service] on Gentoo). The run image can be in a read-only filesystem, and must be subdirectory [run-image] of [s6-linux-init]\'s base directory (normally [/etc/s6-linux-init/current]).

Because [s6-linux-init] runs as process 1, if it terminates in any way, there will be a kernel panic. Therefore, machine initialization is split between [s6-linux-init], which does a minimal amount of work and then replaces itself with [s6-svscan] using a POSIX `execve()` call, and a [stage2 init](#stage2), which is spawned as a child process by [s6-linux-init]. []

### [The stage2 init]

The stage2 init is spawned by the [s6-linux-init] as a child process, and is blocked from running until the latter replaces itself with [s6-svscan]. To achieve this, the child process of [s6-linux-init] opens [the catch-all logger\'s FIFO](#fifo) for writing using the POSIX `open()` call. The call will block until some other process opens the FIFO for reading. The catch-all logger is a supervised process, so it starts executing when [s6-svscan] does, and opens the FIFO for reading, thereby unblocking the process, which then replaces itself with the stage2 init. If no catch-all logger is set up, the child process of [s6-linux-init] just [waits until [s6-svscan] notifies its readiness](https://wiki.gentoo.org/wiki/S6#s6readiness "S6"), using a pipe as the notification channel.

The stage2 init executes with [s6-svscan] as process 1, and performs all remaining initialization tasks needed to bring the machine to its stable, normal \'up and running\' state. It executes with a few vital supervised long-lived processes already running, started as part of process 1\'s supervision tree, including the catch-all logger, if one is used. When the stage2 init finishes its work, it just exits and gets reaped by [s6-svscan].

The stage2 init must be an executable file named [rc.init], and located in the [scripts] subdirectory of [s6-linux-init]\'s base directory (normally [/etc/s6-linux-init/current]). It is usually an execline or shell script. Gentoo\'s official repository does not supply any package with a stage2 init for s6 and s6-rc-based init systems. The s6-linux-init package installs an example [rc.init] shell script in [/etc/s6-linux-init/skel], containing only comments that illustrate how to set up the init system for a variety of [rc subsystems](https://wiki.gentoo.org/wiki/Rc "Rc"). []

### [s6-rc initialization]

The s6-rc service manager [needs to be initialized](https://wiki.gentoo.org/wiki/S6-rc#initialization "S6-rc"), which must be done when [s6-svscan] is already running. Therefore, initialization is performed by having the [stage2 init](#stage2) invoke the [s6-rc-init] program. This program takes the pathname of [a compiled service database](https://wiki.gentoo.org/wiki/S6-rc#database "S6-rc") as an argument (or defaults it to [/etc/s6-rc/compiled]), as well as the pathname of process 1\'s scan directory (i.e. [/run/service] on Gentoo). So a suitable service database must exist and be available at least in a read-only filesystem. This is the *boot-time service database*. s6-rc\'s live state directory must be in a read-write filesystem. On Gentoo, letting [s6-rc-init] default the live state directory pathname to [/run/s6-rc] will place it in the read-write tmpfs mounted by [s6-linux-init].

The initial state of all s6-rc services, as set by [s6-rc-init], is **down**. So the the stage2 init must also start all atomic services (oneshots and longruns) that are needed to complete the machine\'s initialization, if any, as well as all longruns that are wanted up at the end of the boot sequence. This is performed by defining [a service bundle](https://wiki.gentoo.org/wiki/S6-rc#bundles "S6-rc") in the boot-time service database that groups these atomic services, and having the stage2 init start them with an [s6-rc -u change] command naming the bundle. This bundle would be the s6-rc counterpart to [OpenRC](https://wiki.gentoo.org/wiki/OpenRC "OpenRC")\'s [sysinit] + [boot] + [default] runlevels, [systemd](https://wiki.gentoo.org/wiki/Systemd "Systemd")\'s [default.target] unit, or [nosh](https://jdebp.uk/Softwares/nosh/)\'s [normal] target bundle directory. []

## [The catch-all logger]

In the context of an s6 and s6-rc-based init system, the *catch-all logger* is a supervised long-lived process that logs messages sent by supervision tree processes to [s6-svscan]\'s standard output and error, normally in an [automatically rotated logging directory](https://wiki.gentoo.org/wiki/Daemontools-encore#logging "Daemontools-encore"). In a logging chain arrangement, the leaf processes of a supervision tree normally have dedicated loggers that collect and store messages sent to the process\' standard output and error in per-service logs. Messages from [s6-svscan], [s6-supervise] processes, logger processes themselves, and leaf processes that exceptionally don\'t have logger, are printed on process 1\'s standard output or error. At the beginning of the boot sequence, they are redirected by the kernel to the machine\'s console, and can be redirected later so that the messages are delivered to the catch-all logger, using a setup that involves a FIFO. Only the catch-all logger\'s standard error remains redirected to the machine\'s console, as a last resort.

The run image that is copied to the read-write tmpfs mounted by the [stage1 init](#stage1) contains [s6-svscan]\'s initial scan directory with a service directory for the catch-all logger already present, so that it is started as soon as [s6-svscan] begins execution as process 1. For s6-linux-init 1.0.4.0 and later, the catch-all logger\'s service directory must be named [s6-svscan-log], since the [s6-linux-init] program passes [s6-svscan] an `-X` option (*console holder*) to redirect the catch-all logger\'s standard error.

The logging directory is owned by the catch-all logger\'s effective user after dropping privileges, and normally has permissions **2750** (i.e. the output of [ls -l] displays `drwx--s---`). Because it must be set up by the stage1 init before the init system\'s supervision tree is started, a subdirectory with the name, owner, group and permissions of the logging directory must exist in [s6-linux-init]\'s run image. This subdirectory will then be copied to the read-write tmpfs, the only read-write filesystem that can be guaranteed to exist when starting the supervision tree, setting this copy up as the catch-all logger\'s logging directory.

The [s6-linux-init-maker] program from s6-linux-init [can create a catch-all logger](https://wiki.gentoo.org/wiki/S6-linux-init#logger "S6-linux-init") that uses the [s6-log] program. The logging directory of [s6-linux-init-maker]\'s logger is named [uncaught-logs] (so its absolute pathname will be [/run/uncaught-logs] on Gentoo). []

### [][The catch-all logger\'s FIFO]

An s6 and s6-rc-based init system has a FIFO some place in the filesystem, reserved for the catch-all logger. The FIFO is owned by root and has permissions **0600** (i.e. the output of [ls -l] displays `prw-------`). The code of the catch-all logger\'s [run] file opens the FIFO for reading, redirects its standard input to it, optionally drops privileges (e.g. by invoking [s6-setuidgid] or [s6-applyuidgid] if it is a script) and calls the logger program.

The [stage1 init](#stage1) redirects its standard output and error to the catch-all logger\'s FIFO before replacing itself with [s6-svscan], so [s6-svscan] and all supervision tree processes will have their standard output and error redirected this way as well, except the catch-all logger itself. Using a FIFO allows delaying the execution of [the stage2 init](#stage2) until [s6-svscan] is running as process 1.

## [Shutdown and reboot]

### [The shutdown daemon]

The init system\'s supervision tree includes a shutdown daemon, that receives requests to initiate the shutdown sequence, either immediately or after a certain specified time elapses. The shutdown daemon is program [s6-linux-init-shutdownd] [from the s6-linux-init package](https://wiki.gentoo.org/wiki/S6-linux-init#shutdownd "S6-linux-init").

[s6-linux-init-shutdownd] executes a *shutdown file*, and waits for it to terminate. Generally speaking, the shutdown file undoes what the [stage2 init](#stage2) has done at boot time, and is normally an execline or shell script. Its code can use s6 tools and s6-rc services to do its work. In particular, if [s6-rc](https://wiki.gentoo.org/wiki/S6-rc "S6-rc") is in use, it can be used to stop all s6-rc-managed services (normally with a [s6-rc -da change] command).

Then, [s6-linux-init-shutdownd] stops all processes from the supervision tree except the catch-all logger, if one is used, kills all remaining processes, unmounts all mounted filesystem, and finally performs the halt, poweroff or reboot operation, as requested.

Optionally, after unmounting filesystems, [s6-linux-init-shutdownd] can also execute a *final shutdown file*, waiting for it to terminate before shutting down the machine. This file can be used to perform actions after all filesystems are unmounted. For example, to deactivate [LVM](https://wiki.gentoo.org/wiki/LVM "LVM") logical volumes using a [vgchange \--activate] command, or to wipe [LUKS](https://wiki.gentoo.org/wiki/Dm-crypt "Dm-crypt") encrypted volumes\' keys from kernel memory and remove their existing mappings using a [cryptsetup close] command. While the final shutdown file is running the only filesystems remain mounted are the rootfs (read-only), the tmpfs mounted at [/run] by [s6-linux-init] (read-write), and the devtmpfs, sysfs and proc filesystems.

The shutdown and final shutdown files must be executable files named [rc.shutdown] and [rc.shutdown.final], respectively, and located in the [scripts] subdirectory of [s6-linux-init-shutdownd]\'s base directory (normally [/etc/s6-linux-init/current]). They are usually execline or shell scripts. Gentoo\'s official repository does not supply any package with a shutdown file or final shutdown file for s6 and s6-rc-based init systems. Users must create them from scratch or take them from somewhere else (e.g. alternative ebuild repositories). The s6-linux-init package installs example [rc.shutdown] and [rc.shutdown.final] shell scripts in [/etc/s6-linux-init/skel] containing only comments, that illustrate how to set up the init system for a variety of [rc subsystems](https://wiki.gentoo.org/wiki/Rc "Rc"). []

### [The s6-svscan diverted signal handlers]

Since the program running as process 1 is [s6-svscan] [with signal diversion turned on](https://wiki.gentoo.org/wiki/S6#s6signaldivert "S6"), use of diverted signal handlers defines what happens when it receives a signal. The [s6-linux-init-maker] program from s6-linux-init can [create signal handler execline scripts](https://wiki.gentoo.org/wiki/S6-linux-init#signals "S6-linux-init") for all [s6-svscan] diverted signals, that either invoke the [s6-linux-init-shutdown] program from the same package to request that the machine be halted, powered off or rebooted, or do nothing. This allows shutting down the machine by sending signals to process 1, in addition to using the [s6-linux-init-shutdown] or [s6-linux-init-hpr] programs.

### [Compatibility scripts]

[s6-svscan] is not directly compatible with [sysvinit](https://wiki.gentoo.org/wiki/Sysvinit "Sysvinit")\'s [telinit], [halt], [poweroff], [reboot], and [shutdown] commands. However, the [s6-linux-init-maker] program from s6-linux-init can [create execline compatibility scripts](https://wiki.gentoo.org/wiki/S6-linux-init#sysvinit "S6-linux-init") for these programs, that invoke the [s6-linux-init], [s6-linux-init-telinit], [s6-linux-init-shutdown] and [s6-linux-init-hpr] programs from the same package, as appropriate. []

## [Service management]

On an s6 and s6-rc-based init system, the [s6-rc](https://wiki.gentoo.org/wiki/S6-rc "S6-rc") package is used for service management. In particular, the administrator can [replace the init system\'s compiled service database](https://wiki.gentoo.org/wiki/S6-rc#s6rcupdate "S6-rc") with a new one using [s6-rc-update], and can create a new boot-time service database, to be used next time the machine boots, with [s6-rc-compile] and a set of service definitions in this program\'s supported source format. It is best to have the [s6-rc-init] invocation in the [stage2 init](#stage2) use a symbolic link as the compiled service database pathname, so that the boot-time database can be changed by modifying the symlink instead of the stage2 init code, e.g. by having an [/etc/s6-rc/db] directory for storing one or more compiled databases, making [/etc/s6-rc/boot] a symbolic link to one of those databases, and using the symlink in the [s6-rc-init] invocation.

It is possible to have long-lived processes not managed by s6-rc but supervised by process 1, by managing [s6](https://wiki.gentoo.org/wiki/S6 "S6") service directories directly, placing them (or symbolic links to them) in the init system\'s scan directory, and using [s6-svscanctl -a], [s6-svscanctl -n] or [s6-svscanctl -N] commands as needed. It is also possible to use [s6-svscan] as process 1 and just s6 tools, without s6-rc, but then the init system becomes more [like runit](https://wiki.gentoo.org/wiki/Runit#servicemgmt "Runit").

s6 service directories and s6-rc service definitions for anything not supplied in packages from Gentoo\'s official repository must be created by the administrator, either from scratch or taken from somewhere else (e.g. alternative ebuild repositories). []

## [Runlevels]

An s6-based init system can implement the equivalent of [sysvinit-like runlevels](https://wiki.gentoo.org/wiki/Sysvinit#runlevels "Sysvinit"). The [s6-linux-init-maker] program from s6-linux-init can [create a runlevel changer service](https://wiki.gentoo.org/wiki/S6-linux-init#runleveld "S6-linux-init"), that performs a runlevel change\' by invoking a *runlevel changer file*. The meaning of \"runlevel change\" is defined by whatever this file does when executed.

If [s6-linux-init-maker]\'s runlevel changer service is used, the administrator requests a runlevel change using the [s6-linux-init-telinit] program from s6-linux-init. If s6-rc is in use, runlevels can be mapped to [services bundles](https://wiki.gentoo.org/wiki/S6-rc#bundles "S6-rc") and the runlevel changer file can perform a runlevel change using an [s6-rc change] command with the `-p` (*prune*) option. The runlevel changer file must be an executable file named [runlevel], and located in the [scripts] subdirectory of the runlevel changer service\'s base directory (normally [/etc/s6-linux-init/current]). It is usually an execline or shell script. Gentoo\'s official repository does not supply any package with a runlevel changer file for s6-based init systems. The s6-linux-init package installs an example [runlevel] shell script in [/etc/s6-linux-init/skel], containing only comments that illustrate how to implement runlevel-like functionality for a variety of [rc subsystems](https://wiki.gentoo.org/wiki/Rc "Rc"). []

## [Historical notes]

Before version 1.0.0.0, the s6-linux-init package could be used to create an s6 and s6-rc-based init system with a different design:

-   The [stage1 init](#stage1) was a larger script that invoked several execline programs instead of just a wrapper around the [s6-linux-init] program.
-   The shutdown sequence was different:
    -   Shutdown was initiated only by sending signals to process 1. s6-linux init provided programs named [s6-halt], [s6-poweroff] and [s6-reboot] to send the appropriate signal for the desired action.
    -   There was no [shutdown daemon](#shutdownd), [s6-svscan]\'s [diverted signal handlers](#signals) took care of initiating the shutdown sequence, and executing the shutdown file.
    -   [s6-svscan] did not run until the end of the shutdown sequence. The diverted signal handlers used the [s6-svscanctl] program to make [s6-svscan] perform [its finish procedure](https://wiki.gentoo.org/wiki/S6#s6svscanfinish "S6"), replacing itself with its associated [finish] file, which was an execline script that took care of the rest of the shutdown sequence. Because this [finish] file would run as process 1 as a consequence, it was called the *stage3 init*.
    -   The stage3 init was informed about the desired shutdown action (halt, poweroff or reboot) by receiving an argument from [s6-svscan], which in turned depended on the particular option passed to [s6-svcanctl] by the relevant diverted signal handler. The shutdown action was performed at the end by invoking the [s6-halt], [s6-poweroff] or [s6-reboot] program, depending on the requested action, with the `-f` (*force*) option.
-   The [catch-all logger](#logger) did not run until the end of the shutdown sequence, it was stopped by the stage3 init using an [s6-svc] command with a special option (`-X`). This was needed because [s6-log] can be configured to ignore the `SIGTERM` signal sent by its [s6-supervise] parent during supervision tree tear down, so the option made [s6-supervise] arrange to have [s6-log] get an end-of-file condition on its standard input, and exit.

The described design has been deprecated by the relase of s6-linux-init version 1.0.0.0, and became unsupported with upstream\'s release of version 2.10.0.0 of the s6 package.

## [See also]

-   [Comparison of init systems](https://wiki.gentoo.org/wiki/Comparison_of_init_systems "Comparison of init systems") --- compares and contrasts **[init systems](https://wiki.gentoo.org/wiki/Init_system "Init system")** for Unix(like) [OSs](https://en.wikipedia.org/wiki/Operating_system "wikipedia:Operating system")

## [External resources]

-   [lh-bootstrap](https://www.skarnet.org/software/lh-bootstrap), a set of scripts that build a disk image for a virtual machine such as [QEMU](https://wiki.gentoo.org/wiki/QEMU "QEMU"). The image contains a Linux kernel and a collection of small user-space tools such as BusyBox and dropbear ([[[sys-apps/busybox]](https://packages.gentoo.org/packages/sys-apps/busybox)[]], [[[net-misc/dropbear]](https://packages.gentoo.org/packages/net-misc/dropbear)[]]), all statically linked to musl ([[[sys-libs/musl]](https://packages.gentoo.org/packages/sys-libs/musl)[]]), and an s6 and s6-rc-based init system.
-   [Obarun](https://web.obarun.org), an [Arch derivative](https://www.archlinux.org) with an s6 and s6-rc-based init system. It uses a frontend named [66](https://web.obarun.org/software/66).
-   [Slew](https://gitea.com/CasperVector/slew), a project that provides scripts for creating an s6 and s6-rc-based init system, as well as s6-rc service definitions for several services and other supporting scripts, to make an s6 and s6-rc-based init system. Most scripts require Byron Rakitzis\'s implementation of the Plan 9 shell, [rc], for Unix ([[[app-shells/rc]](https://packages.gentoo.org/packages/app-shells/rc)[]]).