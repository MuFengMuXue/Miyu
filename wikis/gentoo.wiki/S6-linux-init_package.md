**Resources**

[[]][Home](https://www.skarnet.org/software/s6-linux-init)

[[]][Git repository browser](https://git.skarnet.org/cgi-bin/cgit.cgi/s6-linux-init)

[[]][GitHub mirror](https://github.com/skarnet/s6-linux-init)

[[]][Package information](https://packages.gentoo.org/packages/sys-apps/s6-linux-init)

s6-linux-init is a package that provides a set of tools to help create an [s6-based init system](https://wiki.gentoo.org/wiki/S6_and_s6-rc-based_init_system "S6 and s6-rc-based init system"), with optional [s6-rc](https://wiki.gentoo.org/wiki/S6-rc "S6-rc") support, on top of the Linux kernel. The package\'s documentation is provided in HTML format, and can be read on a text user interface using for example [[[www-client/links]](https://packages.gentoo.org/packages/www-client/links)[]].

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
-   [[2] [Configuration]](#Configuration)
    -   [[2.1] [Files]](#Files)
-   [[3] [Usage]](#Usage)
    -   [[3.1] [s6-linux-init-maker]](#s6-linux-init-maker)
        -   [[3.1.1] [The stage1 init]](#The_stage1_init)
        -   [[3.1.2] [The stage2 init]](#The_stage2_init)
        -   [[3.1.3] [The scan directory image]](#The_scan_directory_image)
        -   [[3.1.4] [The catch-all logger]](#The_catch-all_logger)
        -   [[3.1.5] [The runlevel changer service]](#The_runlevel_changer_service)
        -   [[3.1.6] [The shutdown service and daemon]](#The_shutdown_service_and_daemon)
        -   [[3.1.7] [The diverted signal handlers]](#The_diverted_signal_handlers)
    -   [[3.2] [Runlevels]](#Runlevels)
    -   [[3.3] [s6-rc support]](#s6-rc_support)
    -   [[3.4] [Shutdown and reboot]](#Shutdown_and_reboot)
        -   [[3.4.1] [s6-linux-init-shutdown]](#s6-linux-init-shutdown)
        -   [[3.4.2] [s6-linux-init-hpr]](#s6-linux-init-hpr)
    -   [[3.5] [sysvinit compatibility scripts]](#sysvinit_compatibility_scripts)
    -   [[3.6] [Support programs]](#Support_programs)
    -   [[3.7] [Historical notes]](#Historical_notes)
-   [[4] [Removal]](#Removal)
    -   [[4.1] [Unmerge]](#Unmerge)
-   [[5] [See also]](#See_also)
-   [[6] [External resources]](#External_resources)
-   [[7] [References]](#References)

## [Installation]

### [USE flags]

### [USE flags for] [sys-apps/s6-linux-init](https://packages.gentoo.org/packages/sys-apps/s6-linux-init) [[]] [Generates an init binary for s6-based init systems]

  ------------------------------------------------------------------- -------------------------------------------------------------------------------------------
  [`+sysv-utils`](https://packages.gentoo.org/useflags/+sysv-utils)   Install sysvinit compatibility symlinks for telinit, halt, poweroff, reboot, and shutdown
  ------------------------------------------------------------------- -------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-04-13 11:26] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

** Important**\
The `sysv-utils` USE flag is set by default for this package, causing a blocker with [sysvinit](https://wiki.gentoo.org/wiki/Sysvinit "Sysvinit"). Because s6-based init systems are not officially supported by Gentoo yet, it is recommended to unset this flag in [/etc/portage/package.use](https://wiki.gentoo.org/wiki//etc/portage/package.use "/etc/portage/package.use").

### [Emerge]

`root `[`#`]`emerge --ask sys-apps/s6-linux-init`

** Important**\
s6-linux-init is currently on the testing branch. Users with systems on the stable branch will need to add the package to [/etc/portage/package.accept_keywords] to be able to install it, and also add [[[dev-libs/skalibs]](https://packages.gentoo.org/packages/dev-libs/skalibs)[]], as well as its runtime dependencies: [[[dev-lang/execline]](https://packages.gentoo.org/packages/dev-lang/execline)[]] and [[[sys-apps/s6]](https://packages.gentoo.org/packages/sys-apps/s6)[]]. While it is generally not advised to mix packages of stable and testing branches, the skarnet.org software stack only depends on the libc, so in this case it should be safe.

## [Configuration]

### [Files]

-   [/etc/s6-linux-init/current] --- Default base directory of [s6-linux-init] and [s6-linux-init-shutdownd].
-   [/etc/shutdown.allow] --- List of account names used by [s6-linux-init-shutdown] when invoked with an `-a` option, to decide whether the machine shutdown request should be allowed to proceed or not.

## [Usage]

The package provides the [s6-linux-init-maker] program, which helps create several components of an s6-based init system, programs for booting and shutting down the machine when such components are used, and other support programs. It also provides tools for implementing runlevel-like functionality similar to that of [sysvinit](https://wiki.gentoo.org/wiki/Sysvinit#runlevels "Sysvinit").

### [s6-linux-init-maker]

The [s6-linux-init-maker] program must be run as root, so that it can create files and directories with appropriate owner, group and permissions, and must be invoked with a pathname as its argument. It creates a directory at the specified pathname, which must not exist beforehand, containing several init system components:

-   A subdirectory named [run-image], which contains:
    -   An [s6](https://wiki.gentoo.org/wiki/S6 "S6") scan directory image.
    -   An empty directory named [uncaught-logs].
-   A subdirectory named [env], that might be empty.
-   A subdirectory named [scripts], containing shell scripts named [rc.init], [rc.shutdown] and [runlevel]. For s6-linux-init version 1.0.3.0 and later, this subdirectory also a shell script named [rc.shutdown.final].
-   A subdirectory named [bin], containing [sysvinit](https://wiki.gentoo.org/wiki/Sysvinit "Sysvinit") compatibility execline scripts.

To use these components to make an init system, they must be copied to appropriate filesystem locations. The [init] script contained in the [bin] subdirectory can be e.g. renamed and copied to a directory that matches an `init=` kernel parameter. For example, if the [bootloader](https://wiki.gentoo.org/wiki/Bootloader "Bootloader") is configured to pass an `init=/sbin/s6-imkr-init` parameter to the kernel, then the [init] file generated by [s6-linux-init-maker] must be copied to [/sbin] and renamed as [s6-imkr-init]. The [run-image], [env] and [scripts] subdirectories must be copied to [the [s6-linux-init] program\'s base directory](#stage1). For the sysvinit compatibility scripts, see [here](#sysvinit). Care must be taken to ensure that owner, group and permissions of files and subdirectories are preserved when cpoying them to their destination place, e.g. by using GNU or BusyBox [cp] with the `-a` option, or the [s6-hiercopy] program from s6-portable-utils ([[[sys-apps/s6-portable-utils]](https://packages.gentoo.org/packages/sys-apps/s6-portable-utils)[]]).

The generated init system needs at least three files that must be supplied by the user to complete it: a *stage2 init*, a *shutdown file* and a *runlevel changer file*, all of which must be executable. The stage2 init is used by the [s6-linux-init] program, the shutdown file is used by [the shutdown daemon](#shutdownd), and the runlevel changer file is used by [the runlevel changer service](#runlevels). For s6-linux-init version 1.0.3.0 and later, a fourth executable file can be supplied by the user if needed, the *final shutdown file*. It is also used by the shutdown daemon if present.

** Note**\
[s6-linux-init-maker] from s6-linux-init version 1.0.3.0 failed if the final shutdown file was not provided. The one from s6-linux-init version 1.0.4.0 and later doesn\'t have this problem.

[s6-linux-init-maker] accepts a set of options that customize all init system components. For the full description of [s6-linux-init-maker], please consult the HTML documentation in the package\'s [/usr/share/doc] subdirectory. A summary of each init system component and some of [s6-linux-init-maker]\'s options that customize it follows. []

#### [The stage1 init]

The [init] script contained in the [bin] subdirectory of the directory created by [s6-linux-init-maker] is [a stage1 init](https://wiki.gentoo.org/wiki/S6_and_s6-rc-based_init_system#stage1 "S6 and s6-rc-based init system"). [s6-linux-init-maker]\'s stage1 init runs as process 1 during the machine\'s boot sequence, and is an execline script that wraps an invocation of a program supplied by the package, also named [s6-linux-init].

[s6-linux-init] expects to access the contents of a certain *base directory*, and performs these actions:

-   It sets the `PATH` environment variable to a specified or default value.
-   It sets the working directory to [/].
-   It sets the file mode creation mask to a specified or default value using a POSIX `umask()` call.
-   It makes itself the leader of a new process group using a POSIX `setpgid(0, 0)` call.
-   It unmounts any filesystem that might be mounted at [/run], and mounts a read-write tmpfs with options `mode=0755`, `nodev` and `nosuid`.
    -   If an `-n` option was passed to [s6-linux-init], it assumes that a tmpfs is already mounted at [/run], and remounts it with the previously mentioned options. This is useful when an [initramfs](https://wiki.gentoo.org/wiki/Initramfs "Initramfs") is used to mount the tmpfs, and writes data to it that must be preserved.
    -   If an `-N` option was passed to [s6-linux-init], it assumes that a tmpfs is already mounted at [/run] and does nothing. This is useful when an initramfs is used to mount the tmpfs, and it should remain as the (read-write) rootfs of the machine.
-   If a `-d` option followed by a pathname was passed to [s6-linux-init], it mounts a devtmpfs at the supplied pathname.
-   If an `-s` option followed by a pathname was passed to [s6-linux-init], it dumps the enviroment set up by the kernel to a specified *enviroment store*. The environment store is [an environment directory](https://wiki.gentoo.org/wiki/Daemontools-encore#changingstate "Daemontools-encore") suitable for [s6-envdir].
-   It copies the [run-image] subdirectory of the base directory to the tmpfs, preserving owner, group and permissions of files and subdirectories.
-   It unsets all enviroment variables except `PATH`.
-   It adjusts the enviroment according to the [env] subdirectory of the base directory, as if by an [s6-envdir] invocation.
-   It redirects its standard input to [/dev/null].
-   It redirects its standard output and error to the catch-all logger\'s FIFO.
    -   (version 1.0.4.0 and later) If a `-B` option was passed to [s6-linux-init], it will instead create a pipe, close its reading end, and pass the file descriptor number of its writing end to [s6-svscan] after a `-d` (*notify readiness*) option. The child process that will execute the stage2 init is spawned before closing the reading end of the pipe; the process will therefore inherit the corresponding file descriptor, so that it can use it to [wait for [s6-svscan]\'s readiness notification](https://wiki.gentoo.org/wiki/S6#s6readiness "S6"). This allows setting up the resulting init system without a catch-all logger.
-   It spawns the [stage2 init](#stage2) as a session leader using a POSIX `setsid()` call.
-   (version 1.0.3.0 and later) It uses a Linux `reboot()` system call with an `RB_DISABLE_CAD` command, to ask the kernel to [send a `SIGINT` signal to process 1](#signals) when the [Ctrl]+[Alt]+[Del] key combination is pressed.
-   (version 1.0.4.0 and later) It uses a Linux `ioctl()` system call with a `KDSIGACCEPT` request, to ask the kernel to send a `SIGWINCH` signal to process 1 when the key combination that corresponds to *keyboard signal* is pressed (usually configured to be [Alt]+[Up Arrow]).
-   It replaces itself with [s6-svscan] using a POSIX `execve()` call, passing it the `-s` (*divert signals*) and `-t 0` (*do not periodically scan the scan directory*) options, and passing [/run/service] as the pathname of the scan directory.

If [s6-linux-init] finds that its process ID is not 1, it replaces itself [with [s6-linux-init-telinit]](#runlevels).

Aspects of the stage1 init that can be customized via [s6-linux-init-maker] options are:

-   The pathname of [s6-linux-init]\'s base directory: `-c`. Default: [/etc/s6-linux-init/current].
-   The value the `PATH` environment variable is initially set to: `-p`. This value affects all programs invoked by the stage2 init, and [s6-svscan], and will be the initial value of `PATH` for all the init system\'s supervision tree processes. Default: `/usr/bin:/bin`.
-   The initial value of the file mode creation mask for all the starting processes: `-m`. Default: **0022**.
-   Whether a devtmpfs filesystem will be mounted: `-d`. If this option is not specified, no devtmpfs is mounted by [s6-linux-init]. Otherwise, it must be followed by the pathname of the filesystem\'s mountpoint.
-   What to do about the read-write tmpfs: `-N` or `-n`.
-   (version 1.0.4.0 and later) Whether a catch-all logger will be used: `-B`.
-   The pathname of a read-write directory for storing the kernel\'s environment variables (i.e. the environment store): `-s`. If this option is not specified, the environment set up by the kernel is discarded before [s6-linux-init] replaces itself with [s6-svscan].

All these options, if specified, are passed as-is to [s6-linux-init] (via the generated [init] script). [s6-linux-init-maker] checks that the pathname specified after options `-c`, `-d` and `-s` is absolute. []

#### [The stage2 init]

The [stage2 init](https://wiki.gentoo.org/wiki/S6_and_s6-rc-based_init_system#stage2 "S6 and s6-rc-based init system") must be provided by the user, must be an executable file named [rc.init], and located in the [scripts] subdirectory of [[s6-linux-init]\'s base directory](#stage1). Unless [s6-linux-init] has been invoked with the `-B` option, [rc.init] runs with its standard output and error redirected to [the catch-all logger](#logger)\'s FIFO, i.e. all messages will be logged to the logging directory. Otherwise, its standard output and error are redirected to the machine\'s console.

[rc.init] is invoked with at least one argument: an *initial runlevel name*. All arguments of the stage1 init are also passed verbatim to [rc.init], after the initial runlevel name. [s6-linux-init] scans its argument list, and if one of the arguments is the word `default`, `2`, `3`, `4` or `5`, then it is interpreted as the initial runlevel name and passed to [rc.init] as the first argument ---which means that it will be repeated later in the argument list---. Otherwise, if a `-D` option followed by a runlevel name was passed to [s6-linux-init], then it is interpreted as the initial runlevel name and passed to [rc.init] as the first argument. Otherwise, the word `default` is passed as the first argument.

** Note**\
Every word in the space-separated kernel command line after a \"\--\" (double hyphen) marker is passed as an argument to process 1, as is every word before the marker, if present, that does not contain an equals sign (\'=\') or dot (\'.\'), and that is not recognized as a kernel parameter. Therefore, arguments can be passed to the stage1 init by specifying them in the kernel\'s command line (e.g. using the [bootloader](https://wiki.gentoo.org/wiki/Bootloader "Bootloader")\'s available mechanisms).

[s6-linux-init-maker] copies the file named [rc.init] from a directory that can be specified with the `-f` option, to the [scripts] subdirectory of its generated directory as the stage2 init. If no `-f` option is specified, directory [/etc/s6-linux-init/skel] is used on Gentoo. The package installs an example stage2 init in [/etc/s6-linux-init/skel], that is a shell script containing only comments.

Aspects of the stage2 init that can be customized via [s6-linux-init-maker] options are:

-   The name of the initial rulnevel, if it was not specified in the kernel command line: `-D`. Default: the word `default`.

This option, if specified, is passed as-is to [s6-linux-init] (via the generated [init] script).

#### [The scan directory image]

The init system\'s scan directory image is the [run-image/service] subdirectory of of [[s6-linux-init]\'s base directory](#stage1), which is copied by [s6-linux-init] to the read-write tmpfs mounted at [/run]. This copy then becomes [s6-svscan]\'s scan directory when it starts running as process 1. Therefore, the init system\'s scan directory\'s absolute pathname will be [/run/service].

The scan directory image must contain at least these service directories:

-   One for [the shutdown daemon](#shutdownd), which must be named [s6-linux-init-shutdownd].
-   One for [the catch-all logger](#logger), if one is used. For s6-linux-init version 1.0.4.0, if present, it must be named [s6-svscan-log].
-   One for [the runlevel changer service](#runlevels), if the [s6-linux-init-telinit] program is going to be used. If present, it must be named [s6-linux-init-runleveld].

The scan directory image generated by [s6-linux-init-maker] satisfies this requirements, and can optionally contain a service directory for an *early getty service*, named [s6-linux-init-early-getty]. This service, if present, allows logging in to the machine from its console as early as possible. The scan directory image also contains [s6-svscan] [diverted signal handlers](#signals), as well as the [.s6-svscan/crash] and [.s6-svscan/finish] files used for [[s6-svscan]\'s finish procedure](https://wiki.gentoo.org/wiki/S6#s6svscanfinish "S6"). These two files simply print an *\"s6-svscan crashed. Rebooting.\"* or *\"s6-svscan exited. Rebooting.\"* message, respectively, and perform a forced reboot of the machine with an [s6-linux-init-hpr -r -f] command.

** Warning**\
This means that [rc.shutdown], [s6-linux-init-umountall] and [rc.shutdown.final] won\'t be executed, which might result in s6-rc oneshots not stopping properly and filesystems not being cleanly unmounted. Therefore, the [s6-svscanctl] program should not be run with [/run/service] and an option that makes [s6-svscan] initiate its finish procedure.

Aspects of the scan directory image that can be customized via [s6-linux-init-maker] options are:

-   Whether an early getty service will be present: `-G`. If this option is not specified, there will be no early getty service, and any [getty] setup must be done by the user-provided [stage2 init](#stage2). Otherwise, it must be followed by a suitable invocation (program name and arguments) of some [getty] implementation, such as, for example, `-G '/sbin/agetty 38400 tty1 linux'` for Gentoo. The generated service directory will contain a [run] execline script with the specified invocation.

#### [The catch-all logger]

The [catch-all logger](https://wiki.gentoo.org/wiki/S6_and_s6-rc-based_init_system#logger "S6 and s6-rc-based init system") generated by [s6-linux-init-maker] is an [s6-log] process that, on Gentoo, logs to (automatically rotated) logging directory [/run/uncaught-logs]. This means that the logdir is placed in the read-write tmpfs [mounted by [s6-linux-init]](#stage1). The standard output of the [s6-log] process is redirected to [/dev/null], and [s6-svscan] redirects [s6-log]\'s standard error to the machine\'s console, using an `-X` option (*console holder*) passed by [s6-linux-init].

The [run] file of the logger\'s s6 service directory opens [the corresponding FIFO](https://wiki.gentoo.org/wiki/S6_and_s6-rc-based_init_system#fifo "S6 and s6-rc-based init system") for reading, and then invokes [s6-log] with the `-p` option, so that it cannot be killed by the `SIGTERM` signal, with a `-d 3` option, which makes it [signal readiness](https://wiki.gentoo.org/wiki/S6#s6readiness "S6") to its [s6-supervise] parent process using file descriptor 3 for the notification channel, and with the `-b` (*blocking*) option, which makes [s6-log] stop reading from the FIFO while it has unflushed buffers. This avoids unbound memory use if there is a lot of output to write.

For s6-linux-init version 1.0.4.0 and later, the catch-all logger is optional. If one is not used, all messages that would be logged are printed to the machine\'s console instead.

Aspects of the catch-all logger that can be customized via [s6-linux-init-maker] options are:

-   (version 1.0.4.0 and later) Whether a catch-all logger will be used: `-B`. If this option is specifed, no s6 service directory is generated for the catch-all logger in the scan directory image.
-   The [s6-log] process\' effective user and group: `-u`. Default: [s6-log] runs as root. If this option is specified, it must be followed by an account database username. The [s6-setuidgid] program from the s6 package is used in the generated service directory\'s [run] script to change to a non-privileged user.
-   How logged lines of text are timestamped: `-t`. Default: timestamps in [external TAI64N format](https://cr.yp.to/libtai/tai64.html) are used, as generated by [s6-log]\'s **t** directive.
-   Whether the catch-all logger also prints logged lines to the machine\'s console: `-1` (the number one). This is generally useful to debug a system at a glance, but if a failing program keeps sending error messages, it may interfere with comfortable usage of kernel virtual terminals. This can be avoided by not using [/dev/tty1] for any [getty] process. If this option is used, the standard output of the [s6-log] process is redirected to the console instead of [/dev/null], and a \"1\" directive is used for printing logged lines.

[s6-linux-init-maker] creates an [uncaught-logs] subdirectory in the [run-image] subdirectory of its generated directory, with an owner and group that are suitable for [s6-log]\'s effective user and group, and appropriate permissions. []

#### [The runlevel changer service]

The runlevel changer service generated by [s6-linux-init-maker] is named [s6-linux-init-runleveld], and is [an [s6-sudod] process](https://wiki.gentoo.org/wiki/S6#s6sudo "S6") that executes a [user-provided file](#runlevels). The [s6-sudoc] - [s6-sudod] mechanism allows executing the file in a controlled, reproducible environment, i.e. the one set up for the init system\'s supervision tree processes. This is similar to the [s6rc-oneshot-runner] service that [s6-rc uses for oneshots](https://wiki.gentoo.org/wiki/S6-rc#oneshots "S6-rc"). The file runs with its standard input and output redirected to [/dev/null], and its standard error logged by [the catch-all logger](#logger), if one is used.

This service is used by the [s6-linux-init-telinit] program.

Aspects of the runlevel changer service that can be customized via [s6-linux-init-maker] options are:

-   The pathname of the base directory, where the user-provided script is expected: `-c`. Default: [/etc/s6-linux-init/current]. It is used to construct the argument list for [s6-sudod].

#### [The shutdown service and daemon]

The shutdown service generated by [s6-linux-init-maker] is a supervised [s6-linux-init-shutdownd] process. It is used by [the [s6-linux-init-shutdown] and [s6-linux-init-hpr] programs](#shutdown). The [s6-linux-init-sutdownd] program is a *shutdown daemon* that takes care of [performing the shutdown sequence](https://wiki.gentoo.org/wiki/S6_and_s6-rc-based_init_system#shutdownd "S6 and s6-rc-based init system"). It runs as a long-lived process, expects to access the contents of a certain *base directory*, and performs these actions:

-   It reads from a control FIFO, waiting for either *machine shutdown requests*, or *shutdown cancellation requests*. A shutdown request consists of an *action* that can be *halt*, *poweroff*, *reboot* or the special action *S*, a time value that specifies a delay until actual shutdown, and another optional time value that specifies a *grace period*.
-   If a shutdown request is received, it waits until the specified shutdown delay expires, while it keeps reading from the control FIFO.
-   If a shutdown cancellation request is received, it cancels any pending machine shutdown that has been previously requested.
-   If the shutdown delay expires and the shutdown request has not been canceled, it starts the shutdown sequence by executing a *shutdown file* as a child process, and waits until it terminates. The shutdown file is an executable file that must be provided by the user, must be named [rc.shutdown], and must be located in the [scripts] subdirectory of the base directory. Because [s6-linux-init-sutdownd] is part of the init system\'s supervision tree, [rc.shutdown] runs with the same environment that was set up for [s6-linux-init-sutdownd], with its standard input redirected to [/dev/null], and its standard output and error logged by [the catch-all logger](#logger), if one is used.
-   If the action specified in the shutdown request was **S**, it does nothing and starts reading again from the control FIFO. This allows the implementation of a behaviour that is similar to [sysvinit\'s single user mode](https://wiki.gentoo.org/wiki/Sysvinit#singleuser "Sysvinit"). Otherwise:
-   It redirects its standard output and error to [/dev/console], i.e. the machine\'s console.
-   It creates an execline script named [stage 4] in its s6 service directory.
-   It stops all processes from the supervision tree except the catch-all logger, if one is used, and itself, by renaming the corresponding service directories with a name that starts with a dot (\'.\'), and performing the equivalent of an [s6-svc -dx] command. The renaming of the servicedirs prevents [s6-svscan] from restarting their corresponding [s6-supervise] process after they exit.
-   It syncs all disks, flushing all the dirty system buffers, using a POSIX `sync()` call.
-   It kills all remaining processes by sending them a `SIGTERM` signal followed by a `SIGCONT` signal, using POSIX `kill(-1, SIGTERM)` and `kill(-1, SIGCONT)` calls, and waits for the expiry of the grace period specified in the shutdown request.
    -   If the shutdown request specified a duration for the grace period, that value is used.
    -   Otherwise, if a `-g` option followed by time value in milliseconds was passed to [s6-linux-init-shutdownd], the specified value is used as the duration of the grace period.
    -   Otherwise, the duration of the grace period is 3 seconds.
-   It kills all remaining processes by sending them a `SIGKILL` signal using a `kill(-1, SIGKILL)` call. Then, if [s6-linux-init-sutdownd] did not get killed by the signal, it exits.
-   The shutdown service\'s corresponding [s6-supervise] process restarts [s6-linux-init-sutdownd].
-   [s6-linux-init-sutdownd] notes that there is a file named [stage 4] in its service directory, redirects its standard output and error to [/dev/console], and replaces itself with it using a POSIX `execve()` call.
-   The execline script unmounts all mounted filesystem according to [/proc/mounts], and remounts the rootfs read-only, using auxiliary program [s6-linux-init-umountall].
-   (version 1.0.3.0 and later) The execline script executes a *final shutdown file* as a child process, and waits until it terminates. The final shutdown file is an executable file that must be provided by the user, must named [rc.shutdown.final], and must be located in the [scripts] subdirectory of the base directory. Because [s6-linux-init-sutdownd] is part of the init system\'s supervision tree, [rc.shutdown.final] runs with the same environment that was set up for [s6-linux-init-sutdownd], with its standard input redirected to [/dev/null], and its standard output and error redirected to the machine\'s console.
-   The execline script invokes the [s6-linux-init-hpr] program with an `-f` option (*force*), and an `-h`, `-p` or `-r` option, according to the action specified in the shutdown request (i.e. halt, poweroff or reboot).

[s6-linux-init-sutdownd]\'s control FIFO must be located in the s6 service directory, and must be named [fifo], owned by root, and have permissions **0600** (i.e. the output of [ls -l] should display `prw-------`) to restrict unprivileged users from shutting down the machine. The service directory generated by [s6-linux-init-maker] satisfies all these conditions.

For further information about [s6-linux-init-shutdownd], please consult the HTML documentation in the package\'s [/usr/share/doc] subdirectory. [s6-linux-init-maker] copies the files named [rc.shutdown] and [rc.shutdown.final] from a directory that can be specified with the `-f` option, to the [scripts] subdirectory of its generated directory as the shutdown and final shutdown files. If no `-f` option is specified, directory [/etc/s6-linux-init/skel] is used on Gentoo. The package installs example shutdown and final shutdown files in [/etc/s6-linux-init/skel], that are shell scripts containing only comments.

Aspects of the shutdown service that can be customized via [s6-linux-init-maker] options are:

-   The pathname of [s6-linux-shutdownd]\'s base directory: `-c`. Default: [/etc/s6-linux-init/current].
-   (version 1.0.4.0 and later) Whether a catch-all logger is being used: `-B`. If this option is specified, [s6-linux-shutdownd] does not give special treatment to the service directory named [s6-svscan-log] during the shutdown sequence. Otherwise, this directory is assumed to be that of the catch-all logger, and [s6-linux-init-shutdownd] does not attempt to rename it and stop the service during the shutdown sequence.
-   The default grace period: `-q`. Default: 3 seconds. If this option is specified, it must be followed by a time value in milliseconds. Any value greater than 5 minutes is treated as `5000`.

The `-c` and `-B` options, if specified, are passed as-is to [s6-linux-shutdownd] (via the generated [run] script in the s6 service directory). The `-q` option is converted to a `-g` option with the same value and also passed to [s6-linux-shutdownd]. [s6-linux-init-maker] checks that the pathname specified after option `-c` is absolute. []

#### [The diverted signal handlers]

The [s6-svscan] [diverted signal handlers](https://wiki.gentoo.org/wiki/S6#s6signaldivert "S6") generated by [s6-linux-init-maker] are execline scripts that make the init system [react to signals sent to process 1](https://wiki.gentoo.org/wiki/S6_and_s6-rc-based_init_system#signals "S6 and s6-rc-based init system"). The effect of diverted signals is:

-   `SIGHUP`: does nothing.
-   `SIGQUIT`: does nothing.
-   `SIGINT`: reboots the machine using an [s6-linux-init-shutdown -a -r \-- now] command.
-   `SIGTERM`: does nothing.
-   `SIGUSR1`: powers off the machine using an [s6-linux-init-shutdown -a -p \-- now] command.
-   `SIGUSR2`: halts the machine using an [s6-linux-init-shutdown -a -h \-- now] command.
-   (version 1.0.4.0 and later) `SIGPWR`: powers off the machine using an [s6-linux-init-shutdown -a -p \-- now] command.
-   (version 1.0.4.0 and later) `SIGWINCH`: does nothing.

** Note**\
This means that shutting down by sending signals to process 1 will take [/etc/shutdown.allow] into account, if present.

### [Runlevels]

s6-linux-init allows the implementation of runlevel-like functionality similar to that of [sysvinit](https://wiki.gentoo.org/wiki/Sysvinit#runlevels "Sysvinit"). An s6-linux-init runlevel normally represents a service set, and *entering a runlevel* normally means to start all services in the corresponding set, and stopping all services not in it. Each runlevel has an alphanumerical identifier. The package uses two components to implement runlevels: the [s6-linux-init-telinit] program, and [the runlevel changer service](#runleveld).

What happens exactly when a runlevel is entered is defined by a *runlevel changer file* that must be provided by the user. The runlevel changer service generated by [s6-linux-init-maker] expects this file to be an executable file named [runlevel], and located in the [scripts] subdirectory of the service\'s base directory. It is normally an execline or shell script that relies on some service manager to actually perform the necessary service transitions.

The [s6-linux-init-telinit] program accepts a runlevel identifier as its argument, and uses an [s6-sudo -e -T 3600000] command to connect to the runlevel changer service\'s [s6-sudod] socket (absolute pathname [/run/service/s6-linux-init-runleveld/s] on Gentoo), and pass the identifier to it. The `-e` option avoids passing variables from [s6-linux-init-telinit]\'s enviromnent to the the [runlevel] script, and the `-T` option prevents it from running for more than an hour. The service then executes the runlevel changer file with the received identifier as its argument.

For compatibility with sysvinit, if [s6-linux-init-telinit] is invoked with **0** or **6** as the runlevel identifier, after passing it to the runlevel changer and waiting for the changer file to terminate, it uses an [s6-linux-init-hpr -h] or [s6-linux-init-hpr -p] command, respectively, to initiate machine shutdown.

Integration of [s6-linux-init-telinit] with [OpenRC](https://wiki.gentoo.org/wiki/OpenRC "OpenRC") can be achieved by having the script execute the [openrc] program when invoked. In this case, s6-linux-init runlevels are OpenRC runlevels.

For further information about [s6-linux-init-telinit], please consult the HTML documentation in the package\'s [/usr/share/doc] subdirectory.

[s6-linux-init-maker] copies the file named [runlevel] from a directory that can be specified with the `-f` option, to the [scripts] subdirectory of its generated directory as the runlevel changer file. If no `-f` option is specified, directory [/etc/s6-linux-init/skel] is used on Gentoo. The package installs an example runlevel changer file in [/etc/s6-linux-init/skel], that is a shell script containing only comments that illustrate integration with both OpenRC and [s6-rc](https://wiki.gentoo.org/wiki/S6-rc "S6-rc").

### [s6-rc support]

See [here](https://wiki.gentoo.org/wiki/S6_and_s6-rc-based_init_system#servicemgmt "S6 and s6-rc-based init system"). []

### [Shutdown and reboot]

s6-linux-init provides the [s6-linux-init-shutdown] and [s6-linux-init-hpr] programs, that can be used in combination with the init system components generated by [s6-linux-init-maker] to shut down the machine. The former conforms to the LSB shutdown interface^[\[1\]](#cite_note-1)^, modeled after sysvinit\'s [shutdown], and the latter provide equivalent functionality to that of sysvinit\'s [halt], [poweroff] and [reboot].

#### [s6-linux-init-shutdown]

[s6-linux-init-shutdown] accepts a time specification, an optional message to be shown to logged in users, and the `-h` (*halt after shutdown*), `-r` (*reboot after shutdown*), `-c` (*cancel shutdown*), `-k` (*do not really shutdown; only warn*), `-t` (*grace period between* `SIGTERM` *and* `SIGKILL`) and `-a` (*access control*) options, with the same meaning [as for sysvinit\'s [shutdown]](https://wiki.gentoo.org/wiki/Sysvinit#shutdown "Sysvinit"). For compatibility with the LSB, it accepts `-f` (*ask the [rc subsystem](https://wiki.gentoo.org/wiki/Rc "Rc") to skip checking filesystems with* [fsck] *after next boot*) and `-F` (*ask the rc subsystem to make* [fsck] *check filesystems after next boot, even if they are marked clean*) options, that it ignores. It also accepts `-H` (*halt*), `-p` and `-P` (*poweroff*) options, that combine with `-h` according to the following table:

  ---------------------------------------------------------------------------------------------------------------------------- -------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------
   [s6-linux-init-shutdown] option    Results in                                                                             Comments
                                                              `-h`                                                                Halting      Note that Gentoo\'s patched [shutdown] powers off in this case.
                                                              `-H`                                                                Halting                   Same as Gentoo\'s patched [shutdown]
                                                              `-P`                                                              Powering off                Same as Gentoo\'s patched [shutdown]
                                                            `-h -H`                                                               Halting                                                                  Compatible with upstream sysvinit
                                                            `-h -P`                                                             Powering off                                                               Compatible with upstream sysvinit
  ---------------------------------------------------------------------------------------------------------------------------- -------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------

\
Unless it was invoked with the `-k` option, [s6-linux-init-shutdown] connects to [the shutdown service](#shutdownd)\'s FIFO and sends a shutdown request, or shutdown cancellation request if the `-c` option has been specified, to [s6-linux-init-shutdownd]. If no `-h`, `-p`, `-H` or `-H` option was specified, it sends a special \'S\' shutdown request, that only makes [s6-linux-init-shutdownd] execute the shutdown script, but not actually shut down the machine. This allows the implementation of a behaviour that is similar to [sysvinit\'s single user mode](https://wiki.gentoo.org/wiki/Sysvinit#singleuser "Sysvinit").

If it was invoked with the `-a` option, [s6-linux-init-shutdown] performs access control using file [/etc/shutdown.allow] just like sysvinit\'s [shutdown]. POSIX `setutxent()`, `getutxent()` and `endutxent()` calls are used to read user process records (i.e. `struct utmpx` objects with `ut_type == USER_PROCESS`) from the user accounting database ([/var/run/utmp] for GNU libc), and their `ut_user` user field is matched against account usernames in [/etc/shutdown.allow]. If the duration of the grace time specified with the `-t` option is greater that 5 seconds, it is capped to that value.

For further information about [s6-linux-init-shutdown], please consult the HTML documentation in the package\'s [/usr/share/doc] subdirectory.

#### [s6-linux-init-hpr]

[s6-linux-init-hpr] must be invoked either with an `-h` option, a `-p` option, or an `-r` option, to halt, poweroff, or reboot the machine, respectively. Without other options, it first writes a *shutdown record* to the user accounting log file ([/var/log/wtmp] for GNU libc), using the libc\'s `updwtmpx()` function. Then, it prints a warning about the system going down to logged in users. And finally, it sends a shutdown request to [s6-linux-init-shutdownd], specifying that machine shutdown should be initiated immediately. That is, [s6-linux-init-hpr -h] is equivalent to [s6-linux-init-shutdown -h now], [s6-linux-init-hpr -p], to [s6-linux-init-shutdown -p now], and [s6-linux-init-hpr -r], to [s6-linux-init-shutdown -r now].

The shutdown record is a runlevel record (i.e. a `struct utmpx` object with `ut_type == RUN_LVL`) that has `ut_user` set to \"shutdown\" (or \"reboot\" if [s6-linux-init-hpr] was invoked with the `-r` option), `ut_id` set to the empty string, `ut_line` set to \"\~\", `ut_pid` set to [s6-linux-init-hpr]\'s process ID, `ut_session` set to [s6-linux-init-hpr]\'s session ID (as returned by a POSIX `getsid(0)` call), `ut_tv` set to the current time, and `ut_host` set to the name returned by the POSIX `gethostname()` call (or the empty string if the call fails).

If [s6-linux-init-hpr] is invoked with a `-W` (capital \'w\') option, it does not print the warning to logged in users. And, just like sysvinit\'s [halt], [poweroff] and [reboot], if it is invoked with a `-w` (small \'w\') option, it only writes the shutdown record to the user accounting log file, without actually shutting down the machine, and if it is invoked with a `-d` option, no shutdown record is written to the user accounting log file.

If [s6-linux-init-hpr] is invoked with an `-f` (*force*) option, it syncs all disks, flushing all the dirty system buffers, using the POSIX `sync()` call, and directly performs the shutdown action requested by the `-h`, `-p` or `-r` option, using the Linux `reboot()` system call. No shutdown record is written to the user accounting log file, no warning is printed a to logged in users, and options `-W`, `-w` and `-d` are ignored. If [s6-linux-init-hpr] is also invoked with an `-n` option, the syncing of disks is skipped.

For further information about [s6-linux-init-hpr], please consult the HTML documentation in the package\'s [/usr/share/doc] subdirectory. []

### [sysvinit compatibility scripts]

[s6-linux-init-maker] creates the following execline scripts in the [bin] subdirectory of its generated directory:

-   [init], which calls the [s6-linux-init] program with at least the `-c` (*base directory*) and `-m` (*file mode creation mask*) options.
-   [halt], which calls the [s6-linux-init-hpr] program with the `-h` option (*halt*) and all the supplied arguments.
-   [poweroff], which calls the [s6-linux-init-hpr] program with the `-p` option (*poweroff*) and all the supplied arguments.
-   [reboot], which calls the [s6-linux-init-hpr] program with the `-r` option (*reboot*) and all the supplied arguments.
-   [telinit], which calls the [s6-linux-init-telinit] program with all the supplied arguments.
-   [shutdown], which calls the [s6-linux-init-shutdown] program with all the supplied arguments.

These compatibility scripts are provided as replacements of the sysvinit programs of the same name in pure s6-based setups, and are installed by the Gentoo ebuild in [/sbin] if the `sysv-utils` [USE flag](https://wiki.gentoo.org/wiki/USE_flag "USE flag") is set. On Gentoo, however, this does not allow having both [[[sys-apps/sysvinit]](https://packages.gentoo.org/packages/sys-apps/sysvinit)[]] and sys-apps/s6-linux-init installed, and therefore, switching between init systems with a reboot. In fact, installing sys-apps/s6-linux-init with this USE flag set on a machine with sys-apps/openrc installed, or with [[[sys-apps/systemd]](https://packages.gentoo.org/packages/sys-apps/systemd)[]] with `sysv-utils` also set, results in a blocker. So generally sys-apps/s6-linux-init should be installed with this USE flag unset. The [bin] subdirectory of [s6-linux-init-maker]\'s generated directory could be copied to [/etc/s6-linux-init/current] using, for example, [cp -a], and then scripts could be run using absolute pathname [/etc/s6-linux-init/current/bin/]*\$* (replacing *\$* with the actual the script name).

### [Support programs]

s6-linux-init provides two support programs for init system components created by [s6-linux-init-maker].

The [s6-linux-init-echo] program is used by [s6-svscan]\'s [finish] and [crash] files for printing messages, and is an exact duplicate of [s6-echo] from [[[sys-apps/s6-portable-utils]](https://packages.gentoo.org/packages/sys-apps/s6-portable-utils)[]]. Its inclusion in s6-linux-init avoids creating a runtime dependency on that package.

The [s6-linux-init-umountall] program is used by the [stage 4] execline script created by the [shutdown daemon](#shutdownd), and it unmounts all filesystems, processing [/proc/mounts] in reverse order, starting with the most recently mounted partition and ending with the rootfs. It behaves in a similar way to that of the [s6-umount] program from [[[sys-apps/s6-linux-utils]](https://packages.gentoo.org/packages/sys-apps/s6-linux-utils)[]] when the `-a` option is specified. Its inclusion in s6-linux-init again avoids creating a runtime dependency on that package. For s6-linux-init version 1.0.3.0 and later, [s6-linux-init-umountall] skips the unmounting of the first instance of a devtmpfs, sysfs and proc filesystem it finds in [/proc/mounts], which would usually correspond to [/dev], [/sys] and [/proc], respectively, so that they are available for the final shutdown file, [rc.shutdown.final].

** Note**\
Before s6-linux-init version 1.0.4.0, [s6-linux-init-umountall] would attempt the unmounting of the tmpfs [mounted by [s6-linux-init]](#stage1), which would fail with a warning, but would not otherwise affect the shutdown sequence.

### [Historical notes]

Before version 1.0.0.0, the s6-linux-init package could be used to create an s6 and s6-rc-based init system with a different design, see [here](https://wiki.gentoo.org/wiki/S6_and_s6-rc-based_init_system#historical "S6 and s6-rc-based init system") for a summary. [s6-linux-init-maker] accepted a different set of options that the one described in this article, and its generated directory had a different structure. That design has been deprecated by the release of version 1.0.0.0, and became unsupported with upstream\'s release of version 2.10.0.0 of the s6 package.

## [Removal]

### [Unmerge]

`root `[`#`]`emerge --ask --depclean --verbose sys-apps/s6-linux-init`

If s6-linux-init\'s programs and components generated by [s6-linux-init-maker] are being used as the init system, an alternative one must be installed in parallel, and the machine rebooted to use it (possibly by reconfiguring the bootloader), before the package is removed, or otherwise the machine will become unbootable.

## [See also]

-   [S6 and s6-rc-based init system](https://wiki.gentoo.org/wiki/S6_and_s6-rc-based_init_system "S6 and s6-rc-based init system") --- an init system built using components from the [s6](https://wiki.gentoo.org/wiki/S6 "S6"), [s6-rc](https://wiki.gentoo.org/wiki/S6-rc "S6-rc") and [s6-linux-init](https://wiki.gentoo.org/wiki/S6-linux-init "S6-linux-init") packages

## [External resources]

-   [Adélie Linux](https://www.adelielinux.org), a distribution of Linux and musl that supports using s6-linux-init + [OpenRC](https://wiki.gentoo.org/wiki/OpenRC "OpenRC") as its init system, as an alternative to [sysvinit](https://wiki.gentoo.org/wiki/Sysvinit "Sysvinit") + OpenRC (currently in beta stage).

## [References]

1.  [[[↑](#cite_ref-1)] [Linux Standard Base Core Specification 5.0.0, Generic Part, Chapter 17, \"Commands and Utilities\", [17.2, \"Command Behavior\", shutdown](https://refspecs.linuxfoundation.org/LSB_5.0.0/LSB-Core-generic/LSB-Core-generic/shutdown.html). Retrieved on September 9th, 2019.]]