**Resources**

[[]][Home](http://smarden.org/runit/)

[[]][Wikipedia](https://en.wikipedia.org/wiki/Runit "wikipedia:Runit")

[[]][Package information](https://packages.gentoo.org/packages/sys-process/runit)

[![Ohloh Logo](/images/thumb/c/c1/Ohloh-logo.png/30px-Ohloh-logo.png)][Open Hub](https://www.openhub.net/p/runit)

**runit** is lightweight process supervision suite, originally inspired by [daemontools](https://wiki.gentoo.org/wiki/Daemontools "Daemontools") that offers fast and reliable service management. It can be used as alternative to [sysvinit](https://packages.gentoo.org/packages/sys-apps/sysvinit) or [systemd](https://wiki.gentoo.org/wiki/Systemd "Systemd"), either by itself or alongside [OpenRC](https://wiki.gentoo.org/wiki/OpenRC "OpenRC"). Additionally, runit can be employed as a PID 1 init system or as a supervision layer, managing services defined by OpenRC.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
-   [[2] [Configuration]](#Configuration)
    -   [[2.1] [Environment variables]](#Environment_variables)
    -   [[2.2] [Files]](#Files)
    -   [[2.3] [Service]](#Service)
        -   [[2.3.1] [OpenRC]](#OpenRC)
-   [[3] [Usage]](#Usage)
    -   [[3.1] [Process supervision]](#Process_supervision)
        -   [[3.1.1] [The check file]](#The_check_file)
        -   [[3.1.2] [The sv program\'s LSB-like interface]](#The_sv_program.27s_LSB-like_interface)
        -   [[3.1.3] [Custom process control]](#Custom_process_control)
    -   [[3.2] [Starting the supervision tree]](#Starting_the_supervision_tree)
        -   [[3.2.1] [From OpenRC]](#From_OpenRC)
        -   [[3.2.2] [From sysvinit]](#From_sysvinit)
    -   [[3.3] [The logging chain]](#The_logging_chain)
    -   [[3.4] [Runit as the init system]](#Runit_as_the_init_system)
        -   [[3.4.1] [Reboot and shutdown]](#Reboot_and_shutdown)
        -   [[3.4.2] [The runsvchdir program]](#The_runsvchdir_program)
        -   [[3.4.3] [Runit and service management]](#Runit_and_service_management)
    -   [[3.5] [OpenRC\'s runit integration feature]](#OpenRC.27s_runit_integration_feature)
-   [[4] [Removal]](#Removal)
    -   [[4.1] [Unmerge]](#Unmerge)
-   [[5] [See also]](#See_also)
-   [[6] [External resources]](#External_resources)
-   [[7] [References]](#References)

## [Installation]

### [USE flags]

### [USE flags for] [sys-process/runit](https://packages.gentoo.org/packages/sys-process/runit) [[]] [A UNIX init scheme with service supervision]

  ------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------
  [`+scripts`](https://packages.gentoo.org/useflags/+scripts)         Install boot scripts into /etc/runit/.
  [`split-usr`](https://packages.gentoo.org/useflags/split-usr)       Enable behavior to support maintaining /bin, /lib\*, /sbin and /usr/sbin separately from /usr/bin and /usr/lib\*
  [`static`](https://packages.gentoo.org/useflags/static)             !!do not set this during bootstrap!! Causes binaries to be statically linked instead of dynamically
  [`system-init`](https://packages.gentoo.org/useflags/system-init)   Installed as a provider of virtual/service-manager.
  ------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-03-25 05:53] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

`root `[`#`]`emerge --ask sys-process/runit`

## [Configuration]

### [Environment variables]

-   `SVDIR` - Directory [sv] will search for the services specified as arguments.
-   `SVWAIT` - Time [sv] will wait for a service to reach its desired state before timing out or killing it with a `SIGKILL` signal.

### [Files]

-   [/service] - Directory [sv] will search for the services specified as arguments if `SVDIR` is empty of unset.
-   [/etc/runit/1] - File [runit] will execute when the machine boots.
-   [/etc/runit/2] - File [runit] will execute and supervise when [/etc/runit/1] exits.
-   [/etc/runit/3] - File [runit] will execute when the machine shuts down.
-   [/etc/runit/ctrlaltdel] - File [runit] will execute when receiving a `SIGINT` signal.
-   [/etc/runit/stopit] - Used by [runit] to decide whether it should initiate machine shutdown when receiving a `SIGCONT` signal or not.
-   [/etc/runit/reboot] - Used by [runit] to decide whether it should halt or reboot the machine.
-   [/etc/runit/runsvdir/current] - Symbolic link set by [runsvchdir] to [runsvdir]\'s current scan directory.
-   [/etc/runit/runsvdir/previous] - Symbolic link set by [runsvchdir] to [runsvdir]\'s previous scan directory.
-   [/etc/runit/runsvdir/default] - [runsvdir]\'s initial scan directory when using `<sys-process/runit-2.1.2`.
-   [/etc/runit/runsvdir/all] - Service directory repository when using `<sys-process/runit-2.1.2`.
-   [/etc/service] - [runsvdir]\'s scan directory when using `>=sys-process/runit-2.1.2`.
-   [/etc/sv] - Service directory repository when using `>=sys-process/runit-2.1.2`.
-   [/run/openrc/sv] - [runsvdir]\'s scan directory when using OpenRC\'s [runit integration feature](#runitintegration).
-   [/var/service] - Symbolic link to [runsvdir]\'s scan directory when using `<sys-process/runit-2.1.2`.

### [Service]

#### [OpenRC]

See [here](#openrclaunch).

## [Usage]

### [Process supervision]

For more in-depth information about the process supervision aspects of runit, see [daemontools-encore](https://wiki.gentoo.org/wiki/Daemontools-encore#Usage "Daemontools-encore"). A summary follows.

  -------------------------------------------------------------------------------------------------------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  runit program                                                                                            daemontools program with similar functionality
  [runsv]       [supervise]
  [runsvdir]    [svscan] plus [readproctitle] functionality
  [svlogd]      [multilog]
  [sv down]     [svc -d]
  [sv up]       [svc -u]
  [sv once]     [svc -o]
  [sv exit]     [svc -dx]
  [sv status]   [svstat]
  [chpst -e]    [envdir]
  [chpst -U]    [envuidgid]
  [chpst -P]    [pgrphack]
  [chpst -l]    [setlock -N] ([setlock]\'s default behaviour)
  [chpst -L]    [setlock -n]
  [chpst -u]    [setuidgid]
  [chpst -m]    [softlimit -m]
  [chpst -d]    [softlimit -d]
  [chpst -o]    [softlimit -o]
  [chpst -p]    [softlimit -p]
  [chpst -f]    [softlimit -f]
  [chpst -c]    [softlimit -c]
  [chpst -r]    [softlimit -r]
  -------------------------------------------------------------------------------------------------------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The process supervision features in runit are implemented by runsv, which functions similarly to daemontools\' supervise. It takes the absolute or relative path of a service directory (or servicedir) as its argument. A valid runit service directory must contain at least an executable run file, and can optionally include a down file and a log subdirectory (or symlink). These components function like their daemontools equivalents. However, unlike supervise, if a log subdirectory is present, the same runsv process manages both the main run and log/run processes and handles the pipe connecting them internally. For example, if a service directory S contains a log subdirectory for logging, ps would show the runsv S process with two child processes. The logger is still controlled via sv, targeting S/log as the service.

Additionally, the service directory can include an executable finish file for cleanup tasks whenever the supervised process exits. runsv calls finish with two arguments: the exit code of the run process (or -1 if it didn't exit normally) and the least significant byte of the exit status (per POSIX waitpid() behavior). For instance, the second argument will be 0 if run exited normally or the signal number if it was terminated by a signal. runsv enforces a 1-second delay before restarting run or invoking finish to prevent fast exit loops. A supervised process runs within the session of its runsv parent. To make it a session leader, use the chpst -P option inside run. If runsv receives SIGTERM, it acts as if the sv exit command was issued for the corresponding service.

Like supervise, runsv maintains control files in a supervise subdirectory. If a symlink to a supervise directory is found, runsv will follow it for control files. Additionally, runsv includes human-readable files in supervise---stat and pid---that store process ID and status information about the supervised process. Refer to the runsv man page for further details.

The runsvdir program supervises multiple processes in parallel using a scan directory (or scandir), similar to daemontools\' svscan, serving as the root of the supervision tree. It monitors the scandir for changes (checking inode, device, or modification time at least every 5 seconds), launching new runsv processes for any newly detected servicedir, or restarting runsv for any terminated servicedir. It also sends SIGTERM to runsv processes whose corresponding servicedir is no longer present. Unlike svscan, runsvdir accepts a second argument that functions like readproctitle and specifies a rolling log buffer viewable in ps output. The first five characters remain static, while subsequent characters rotate as new log messages are added. A -P option allows runsvdir to make runsv children session leaders via setsid(). When runsvdir receives SIGHUP, it sends SIGTERM to its children before exiting. Refer to the runsvdir man page for more details.

svlogd is the logging program in the runit suite, analogous to daemontools\' multilog, but with a different user interface. It accepts logging directory pathnames as arguments, which don\'t need to begin with . or /. To prepend a timestamp in TAI64N format to logged lines, invoke svlogd with the -t option. The -tt option adds a UTC timestamp (YYYY-MM-DD_HH:MM:SS.xxxxx), and -ttt uses ISO8601 format (YYYY-MM-DDTHH:MM:SS.xxxxx). Actions on log lines are defined in a config file in the log directory. Action lines starting with s, n, !, +, or - mirror those in multilog, with + in patterns meaning \"one or more\" of the next character. Patterns ignore timestamps. svlogd rotates logs on receiving SIGALRM and rereads config after receiving SIGHUP. For full details, consult the svlogd man page.

chpst is a chain-loading utility that alters a supervised process\' execution environment. It includes options similar to daemontools\' envdir, envuidgid, pgrphack, setuidgid, setloc, and softlimit, as well as runit-specific features. For example, chpst -n adjusts the process\' nice value, chpst -/ changes the root directory before executing the next command in the chain (chroot()), and chpst -b newname substitutes argv\[0\] to execute the next program with a new name. If invoked with names such as envdir or setuidgid, chpst behaves identically to those respective tools. For complete details, refer to the chpst man page.

sv is the control tool for runit-supervised processes. It accepts a subcommand and service directory pathnames as arguments. Pathnames are relative to \$SVDIR or /service if \$SVDIR is unset. Subcommands such as up, down, once, and exit map to daemontools\' svc -u, svc -d, svc -o, and svc -dx respectively. The status subcommand provides similar functionality to svstat, displaying whether the supervised process is run or down, if its finish script is running, if the process is transitioning states, and additional metadata like PID, uptime, and paused or termination state. Other subcommands reliably send signals to supervised processes. For example, sv alarm sends SIGALRM to rotate logs, and sv hup sends SIGHUP to reload the log config. Refer to the sv man page for the full command set.

Example runit scan directory with [down] and [finish] files, as well as a [log] subdirectory and a symbolic link to a [supervise] directory elsewhere:

`user `[`$`]`ls -l *`

    test-service1:
    total 8
    drwxr-xr-x 2 user user 4096 Sep 15 12:00 log
    -rwxr-xr-x 1 user user   32 Sep 15 12:00 run
    lrwxrwxrwx 1 user user   24 Sep 15 12:00 supervise -> ../../external-supervise

    test-service2:
    total 8
    -rw-r--r-- 1 user user  0 Sep 15 12:00 down
    -rwxr-xr-x 1 user user 78 Sep 15 12:00 finish
    -rwxr-xr-x 1 user user 56 Sep 15 12:00 run

[FILE] **`test-service1/run`**

    #!/bin/sh
    exec test-daemon 2>&1

`user `[`$`]`ls -l test-service1/log`

    total 4
    -rwxr-xr-x 1 user user 42 Sep 15 12:00 run

[FILE] **`test-service1/log/run`**

    #!/bin/sh
    exec svlogd -tt ../../../logdir

Service directory [test-service1] sets up process supervision for a hypothetical [test-daemon] program. Messages sent by the program to its standard error are collected by an also supervised [svlogd] process; a redirection of standard error to standard output (i.e. `2>&1`) is needed so that the pipe set up by [runsv] between those processes is used. A logging directory named [logdir] and placed in the same directory as the scan directory is used. UTC timestamps are prepended to logged messages.

`user `[`$`]`ls -l ../logdir`

    total 4
    -rw-r--r-- 1 user user 3 Sep 15 12:00 config

[FILE] **`../logdir/config`**

    n1

The `n1` action in the [config] file sets the number of old log files [svlogd] should maintain to 1.

[FILE] **`test-service2/run`**

    #!/bin/sh
    echo Starting test-service2/run
    exec sleep 10

[FILE] **`test-service2/finish`**

    #!/bin/sh
    echo Executing test-service2/finish with arguments $@
    exec sleep 10

Resulting supervision tree when [runsvdir] is run as a background process in an interactive shell using this scan directory, assuming it is the working directory (i.e. launched with [runsvdir . &]):

`user `[`$`]`ps xf -o pid,ppid,pgrp,euser,args`

     PID  PPID  PGRP EUSER    COMMAND
    ...
    1524  1517  1524 user     -bash
    2116  1524  2116 user      \_ runsvdir .
    2117  2116  2116 user          \_ runsv test-service1
    2119  2117  2116 user          |   \_ svlogd -tt ../../../logdir
    2120  2117  2116 user          |   \_ test-daemon
    2118  2116  2116 user          \_ runsv test-service2
    ...

** Important**\
Since processes in a supervision tree are created using the POSIX `fork()` call, all of them will inherit [runsvdir]\'s enviroment, which, in the context of this example, is the user\'s login shell environment. If [runsvdir] is launched in some other way (see later), the environment will likely be completely different. This must be taken into account when trying to debug a supervision tree with an interactive shell.

This shows that both the [test-daemon] and [svlogd] processes are supervised by the same [runsv] process. [supervise] subdirectory contents:

`user `[`$`]`ls -l */supervise`

    lrwxrwxrwx 1 user user 24 Sep 15 12:00 test-service1/supervise -> ../../external-supervise

    test-service2/supervise:
    total 8
    prw------- 1 user user  0 Sep 15 12:05 control
    -rw------- 1 user user  0 Sep 15 12:05 lock
    prw------- 1 user user  0 Sep 15 12:05 ok
    -rw-r--r-- 1 user user  0 Sep 15 12:05 pid
    -rw-r--r-- 1 user user  5 Sep 15 12:05 stat
    -rw-r--r-- 1 user user 20 Sep 15 12:05 status

`user `[`$`]`ls -l ../external-supervise`

    total 12
    prw------- 1 user user  0 Sep 15 12:05 control
    -rw------- 1 user user  0 Sep 15 12:05 lock
    prw------- 1 user user  0 Sep 15 12:05 ok
    -rw-r--r-- 1 user user  5 Sep 15 12:05 pid
    -rw-r--r-- 1 user user  4 Sep 15 12:05 stat
    -rw-r--r-- 1 user user 20 Sep 15 12:05 status

`user `[`$`]`ls -l test-service1/log/supervise`

    total 12
    prw------- 1 user user  0 Sep 15 12:05 control
    -rw------- 1 user user  0 Sep 15 12:05 lock
    prw------- 1 user user  0 Sep 15 12:05 ok
    -rw-r--r-- 1 user user  5 Sep 15 12:05 pid
    -rw-r--r-- 1 user user  4 Sep 15 12:05 stat
    -rw-r--r-- 1 user user 20 Sep 15 12:05 status

Contents of the log directory and current log file:

`user `[`$`]`ls -l ../logdir`

    total 8
    -rw-r--r-- 1 user user   3 Sep 15 12:00 config
    -rw-r--r-- 1 user user 308 Sep 15 12:35 current
    -rw------- 1 user user   0 Sep 15 12:05 lock

`user `[`$`]`cat ../logdir/current`

    2018-09-15_15:34:26.40056 Logged message #1
    2018-09-15_15:34:31.40295 Logged message #2
    2018-09-15_15:34:36.40484 Logged message #3
    2018-09-15_15:35:04.89572 Logged message #4
    2018-09-15_15:35:09.89814 Logged message #5
    2018-09-15_15:35:14.89977 Logged message #6
    2018-09-15_15:35:19.90165 Logged message #7

The timestamp is in UTC, and the computer\'s operating system is assumed to be set to a UTC-3 timezone. Forcing [svlogd] to perform a rotation:

`user `[`$`]`sv alarm ./test-service1/log`

`user `[`$`]`ls -l ../logdir`

    total 8
    -rwxr--r-- 1 user user 308 Sep 15 12:41 @400000005b9d2888221699c4.s
    -rw-r--r-- 1 user user   3 Sep 15 12:00 config
    -rw-r--r-- 1 user user   0 Sep 15 12:42 current
    -rw------- 1 user user   0 Sep 15 12:05 lock

This shows that a log file with a name containing a [TAI64N timestamp](https://cr.yp.to/libtai/tai64.html) and ending in **.s** (meaning \'completely processed log file\') was created, and that [current] was truncated. Messages sent by [test-service2]\'s [run] process to [runsvdir]\'s standard output when manually started:

`user `[`$`]`export SVDIR="$(pwd)"`

`user `[`$`]`sv up test-service2`

    Starting test-service2/run
    Executing test-service2/finish with arguments 0 0
    Starting test-service2/run
    Executing test-service2/finish with arguments 0 0
    Starting test-service2/run
    ...

As shown by the output of [test-service2/finish], the [run] process exits each time with an exit code of 0. Resulting supervision tree:

`user `[`$`]`ps xf -o pid,ppid,pgrp,euser,args`

     PID  PPID  PGRP EUSER    COMMAND
    ...
    1524  1517  1524 user     -bash
    2116  1524  2116 user      \_ runsvdir .
    2117  2116  2116 user          \_ runsv test-service1
    2119  2117  2116 user          |   \_ svlogd -tt ../../../logdir
    2120  2117  2116 user          |   \_ test-daemon
    2118  2116  2116 user          \_ runsv test-service2
    2146  2118  2116 user              \_ sleep 10
    ...

`user `[`$`]`sv status *`

    run: test-service1: (pid 2120) 220s; run: log: (pid 2119) 220s
    run: test-service2: (pid 2146) 7s, normally down

This shows that because [test-service1] has a [log] subdirectory, [sv status] shows the status of the [svlogd] process too, after [test-daemon]\'s status (\"run: log:\"). After enough seconds have elapsed:

`user `[`$`]`sv status *`

    run: test-service1: (pid 2120) 230s; run: log: (pid 2119) 230s
    finish: test-service2: (pid 2150) 17s, normally down

This shows that [runsv] is currently executing [test-service2]\'s [finish] file (\"finish:\"). Reliably sending a `SIGSTOP` signal to [test-service2]\'s [run] process:

`user `[`$`]`sv pause test-service2`

`user `[`$`]`sv status test-service2`

    run: test-service2: (pid 2169) 17s, normally down, paused

This confirms that [run] is stopped (\"paused\"). Reliably sending a `SIGTERM` signal afterwards:

`user `[`$`]`sv term test-service2`

`user `[`$`]`sv status test-service2`

    run: test-service2: (pid 2169) 52s, normally down, paused, got TERM

This confirms that [run] received a `SIGTERM` signal (\"got TERM\"), but it doesn\'t have any efect yet because the process is stopped. To resume it a `SIGCONT` signal is needed:

`user `[`$`]`sv cont test-service2`

    Executing test-service2/finish with arguments -1 15
    Starting test-service2/run
    Executing test-service2/finish with arguments 0 0
    Starting test-service2/run

The output of [test-service2/finish] shows that after resuming execution, [run] was killed by the `SIGTERM` signal that was awaiting delivery (signal 15), and because the process is supervised, [runsv] first executes [test-service2/finish], and then reexecutes [test-service2/run]. Messages sent by [test-service2]\'s [run] process to [runsvdir]\'s standard output when manually stopped:

`user `[`$`]`sv down test-service2`

    Executing test-service2/finish with arguments -1 15

`user `[`$`]`sv status *`

    run: test-service1: (pid 2120) 506s; run: log: (pid 2119) 506s
    finish: test-service2: (pid 2172) 17s, normally down, want down

As shown by [test-service2/finish], [runsv] stopped the [run] process by killing it with a `SIGTERM` signal (signal 15). The output of [sv status] shows that [runsv] is executing the [test-service2/finish] script, and that when it exits, the service will stay down (\"want down\"). []

#### [The check file]

The [sv] program accepts a `-v` option (\'verbose\') that makes it wait for the action requested by the specified subcommand to be completed, and then prints the resulting process\' status, as if an [sv status] command had been used. The wait period\'s duration is the value of the `SVWAIT` environment variable (in seconds), or 7 seconds if `SVWAIT` is empty or unset. It can also be specified with a `-w` option passed to [sv], which overrides the value of `SVWAIT`. If the requested action completes before the expiry of the wait period, the status line is prepended with \'ok:\' followed by a space. Otherwise, the [sv] command exits with a nonzero code and the status line is prepended with \'timeout:\' followed by a space.

For the [sv -v up] command, and, if the supervised process is wanted up after the action (i.e. no [sv once] command was used before), the [sv -v term] and [sv -v kill] commands, the action is considered complete if [runsv] considers the supervised process to be in \'run\' state (i.e. [sv status] would print \'run:\'). However, when the supervised process is executing a server program for example, it might not be *ready* to provide its service immediately after startup. Programs might do initialization work that could take some noticeable time before they are actually ready to serve, but it is impossible for the supervisor to know exactly how much. If there is some program-specific way to infer that it is ready, runit is able to take advantage of it by including an executable file named [check] in the service directory. When using one of the aforementioned subcommands, after [sv] determines that the supervised process is in \'run\' state (via the [supervise/status] file), it executes the [check] file if present, and waits for it to exit. This file is assumed to contain code that *polls for readiness*, and must exit with a 0 code if it considers the supervised process to be ready, and with a nonzero code otherwise. Just like [run] or [finish], the [check] file can have any format the kernel knows how to execute, and is normally a shell script. If [check] determines that the process is ready, [sv] will print an \'ok\' status line and exit, otherwise it reexecutes [check] after waiting 420 milliseconds. In other words, during the wait period [sv] will periodically poll for readiness using [check]; if its exit code is never 0, on expiry of the wait period [sv] will print a \'timeout\' status line and exit.

In addition, the [sv check] command can be used to poll for readiness (periodically during a wait period) by executing the [check] file, without changing the supervised process\' state. The [sv status] command does not use the [check] file. For the full description of the [sv] program please consult the respective man page.

Example service directory with a [check] file:

`user `[`$`]`ls -l test-service`

    total 8
    -rwxr-xr-x 1 user user 71 Sep 16 12:00 check
    -rw-r--r-- 1 user user  0 Sep 16 12:00 down
    -rwxr-xr-x 1 user user 27 Sep 16 12:00 run

[FILE] **`test-service/run`**

    #!/bin/sh
    exec test-daemon

[FILE] **`test-service/check`**

    #!/bin/sh
    echo Polling test-daemon 1>&2
    sleep 1
    exec test-daemon-check

This service directory sets up process supervision for a hypothetical [test-daemon] program. It is assumed that the program can be polled for readiness using another program named [test-daemon-check]. For demonstration purposes, the [sleep] utility is used so that [check] does not exit too quickly. Using the [sv check] command after launching the supervision tree, assuming that the scan directory is the working directory:

`user `[`$`]`export SVDIR="$(pwd)"`

`user `[`$`]`sv check test-service`

    ok: down: test-service: 85s

Because of the [down] file, [runsv] does not launch [test-daemon], so it considers its supervised process to be in \'down\' state, so [sv check] exited immediately with an \'ok\' status and without executing [check]. Starting the supervised process using [sv]\'s `-v` option:

`user `[`$`]`sv -v up test-service`

    Polling test-daemon
    Polling test-daemon
    Polling test-daemon
    Polling test-daemon
    Polling test-daemon
    Polling test-daemon
    timeout: run: test-service: (pid 1908) 8s, normally down

This shows that a [test-daemon] process was spawned (\"run: test-service:\"), but the [test-daemon-check] program determined that it was not ready. The [check] was executed 6 times before the expiery of the default 7 seconds wait period, so [sv] finally gave up with a \'timeout\' status. Polling [test-daemon] again:

`user `[`$`]`sv check test-service`

    Polling test-daemon
    ok: run: test-service: (pid 1908) 29s, normally down

Between both [sv] commands [test-daemon] became ready, so this time the (single) poll was successful, and [sv] exited immediately with an \'ok\' status. Reliably sending [test-daemon] a `SIGTERM` signal using [sv]\'s `-v` option and a longer wait period:

`user `[`$`]`sv -v -w 10 term test-service`

    Polling test-daemon
    Polling test-daemon
    Polling test-daemon
    Polling test-daemon
    Polling test-daemon
    Polling test-daemon
    Polling test-daemon
    Polling test-daemon
    ok: run: test-service: (pid 1930) 10s, normally down

This shows that a [test-daemon] process was killed and then restarted (because it is supervised), but 8 polls were necessary until the [test-daemon-check] program determined that it was ready. Because the process became ready during the wait period, [sv] exited with an \'ok\' status. Stopping the [test-daemon] process using [sv]\'s `-v` option:

`user `[`$`]`sv -v down test-service`

    ok: down: test-service: 0s

Making [runsv] stop and exit using [sv]\'s `-v` option, assuming its supervising [runsvdir] parent process was already killed:

`user `[`$`]`sv -v exit test-service`

    ok: test-service: runsv not running

#### [][The sv program\'s LSB-like interface]

[sv] also accepts a set of subcommands resembling LSB init script actions ^[\[1\]](#cite_note-1)^:

-   The [sv start], [sv stop] and [sv shutdown] commands are equivalent to [sv -v up], [sv -v down] and [sv -v exit], respectively.
-   The [sv force-stop] and [sv force-shutdown] commands, or equivalently, [sv Down] and [sv Exit] (with capital \'D\' and \'E\'), behave like [sv stop] and [sv shutdown], respectively, except that if the action requested by the specified subcommand does not complete during the wait period, the supervised process is sent a `SIGKILL` signal on its expiry, as if an [sv kill] command had been used. The status line printed by [sv] is prepended with \'kill:\' followed by a space in that case.
-   The [sv reload] and [sv try-restart] commands are equivalent to [sv -v hup], [sv -v term] respectively, except that the latter also sends a `SIGCONT` signal to the supervised process after the `SIGTERM` signal, as if an [sv cont] command had been used.
-   The [sv restart] command is equivalent to [sv term] followed by [sv cont] followed by [sv -v up]. Therefore, unlike [sv try-restart], [sv restart] cancels the \'do not restart\' effect of any previous [sv once] command.
-   The [sv force-reload] and [sv force-restart] commands behave like [sv try-restart] and [sv restart], respectively, except that if the action requested by the specified subcommand does not complete during the wait period, the supervised process is sent a `SIGKILL` signal on its expiry, just like what happens with [sv force-stop] and [sv force-shutdown]. The [sv Term] command (with capital \'T\') is equivalent to [sv force-reload].

As noted in section [\"The check file\"](#svcheck), the equivalences stated above imply that the `start`, `try-restart`, `restart`, `force-reload` and `force-restart` subcommands make [sv] execute the [check] file in the named service directories, if present, to poll for readiness.

The [sv] program can be invoked with the name of a service directory (with any `argv[0]` substitution mechanism), in that case, also its exit code tries to comply with the LSB specification: it is **2** for usage errors and **151** (in the \"reserved for application use\" range) for fatal errors, instead of 100 in both cases, it is **0**, **3** or **4**, as appropriate, if the subcommand is `status`, and it is **1** on error (other than fatal errors) for other subcommands. This is useful if a symbolic link to [sv] representing a \'service name\' is placed in directory [/etc/init.d], resembling an LSB initialization script: executing this \'initialization script\' with an action argument results in actually executing [sv] with a runit service directory of that name as an argument (e.g. [/etc/init.d/foo try-restart] will result in [sv try-restart foo]).

For the full description of [sv]\'s functionality please consult the respective man page.

Example service directory for a hypothetical [test-daemon] program with a setup similar to that of section [\"The check file\"](#svcheck):

`user `[`$`]`ls -l test-service`

    total 12
    -rwxr-xr-x 1 user user 71 Sep 16 12:00 check
    -rw-r--r-- 1 user user  0 Sep 16 12:00 down
    -rwxr-xr-x 1 user user 65 Sep 16 12:00 finish
    -rwxr-xr-x 1 user user 41 Sep 16 12:00 run

[FILE] **`test-service/run`**

    #!/bin/sh
    exec test-daemon --ignore-term

[FILE] **`test-service/check`**

    #!/bin/sh
    echo Polling test-daemon 1>&2
    sleep 5
    exec test-daemon-check

[FILE] **`test-service/finish`**

    #!/bin/sh
    [ "$1" != -1 ] || echo test-daemon killed by signal $2

It is assumed that [test-daemon] supports an `--ignore-term` option that makes it ignore the `SIGTERM` signal. Starting the supervised process using [sv]\'s LSB-like interface:

`user `[`$`]`export SVDIR="$(pwd)"`

`user `[`$`]`sv -w 10 start test-service`

    Polling test-daemon
    Polling test-daemon
    ok: run: test-service: (pid 1870) 6s, normally down

This shows that [sv start], being equivalent to [sv -v up], also uses the [check] file. The [test-daemon-check] program was used to poll twice for readiness, and succeeded before the expiry of the 10 seconds wait period. Stopping the [test-daemon] process using [sv]\'s LSB-like interface:

`user `[`$`]`sv stop test-service`

    timeout: run: test-service: (pid 1870) 41s, normally down, want down, got TERM

This shows that [sv stop], being equivalent to [sv -v down], tried to stop the supervised process by sending it a `SIGTERM` signal. Because [test-daemon] ignores the signal, the stop action didn\'t complete before the expiry of the wait period, so [sv] gives up with a \"timeout\" status. The status line confirms that the wanted supervised process\'s state is \'down\' (\"wanted down\"), and that a `SIGTERM` signal was sent (\"got TERM\"). Stopping the [test-daemon] process using [sv]\'s `force-stop` subcommand:

`user `[`$`]`sv force-stop test-service`

    kill: run: test-service: (pid 1870) 76s, normally down, want down, got TERM
    test-daemon killed by signal 9

This shows that, again, the stop action didn\'t complete before the expiry of the wait period, but this time a `SIGKILL` signal was sent to the supervised process on expiry of the wait period. The [finish] file is then executed by [runsv], and its message confirms that [test-daemon] got killed by a `SIGKILL` signal (signal 9).

#### [Custom process control]

The [runsv] program allows the customization of the effect of some [sv] subcommands to some degree. This is done by providing executable files in a subdirectory of the service directory named [control]. The executable files must have single character names that map to an [sv] subcommand, the [runsv] man page details this mapping (it corresponds to the character that is written by [sv] to [runsv]\'s [supervise/control] FIFO). The subcommands that can be customized this way are:

-   The ones that send signals to the supervised process (`term`, `hup`, `quit`, etc.). In particular, if present, the control file that corresponds to customized [sv term], [control/t], is also used by the [sv down] and [sv exit] commands. [runsv] executes the file, waits for it to finish, and then checks its exit code. If it is a nonzero code, [runsv] additionaly sends the corresponding signal to the supervised process. If it is 0, no signal is sent.
-   The `up` and `once` subcommands. A single control file, [control/u], is used for both subcommands. [runsv] executes the file and waits for it to exit, before executing the [run] file. The control file is also executed after [finish] and before reexecution of [run] if the spuervised process unexpectedly stops running and gets restarted by [runsv], and is ignored for the [sv once] command if [run] or [finish] are running. The control file\'s exit code is ignored.
-   The `down` and `exit` subcommands. [runsv] executes the control file, [control/d] and [control/x], respectively, *after* sending the supervised process the `SIGTERM` signal, or executing [control/t] if appropriate, and after sending the subsequent `SIGCONT` signal, *ignoring* [control/c] if present (the control file for [sv cont]), and waits for it to exit. The control file\'s exit code is ignored. For [sv exit], [runsv] exits after [control/x] exits.

Just like [run] or [finish], the files in the [control] subdirectory can have any format the kernel knows how to execute, and are normally shell scripts. In particular, [control/t] should contain code that can stop the supervised process, and is useful if there is an alternative (and preferred) way to do so without sending a `SIGTERM` signal. For further details about customizing the the effect of [sv], please consult [runsv]\'s man page.

** Note**\
Because [runsv] waits for the control file to exit, it its execution takes too long, [runsv] might become unresponsive.

Example service directory with a [control] subdirectory for customized control:

`user `[`$`]`ls -l test-service`

    total 16
    drwxr-xr-x 2 user user 4096 Sep 16 12:00 control
    drwxr-xr-x 2 user user 4096 Sep 16 12:00 env
    drwxr-xr-x 2 user user 4096 Sep 16 12:00 log
    -rwxr-xr-x 1 user user   64 Sep 16 12:00 run

[FILE] **`test-service/run`**

    #!/bin/sh
    echo '(Re)starting test-daemon'
    exec test-daemon 2>&1

`user `[`$`]`ls -l test-service/log`

    total 4
    -rwxr-xr-x 1 user user 38 Sep 16 12:00 run

[FILE] **`test-service/log/run`**

    #!/bin/sh
    exec svlogd ../../../logdir

This service directory sets up process supervision for a hypothetical [test-daemon] program. Messages sent by the program to its standard error are collected by an also supervised [svlogd] process; a redirection of standard error to standard output (i.e. `2>&1`) is needed so that the pipe set up by [runsv] between those processes is used. A logging directory named [logdir] and placed in the same directory as the scan directory is used.

`user `[`$`]`ls -l test-service/control`

    total 16
    -rwxr-xr-x 1 user user 53 Sep 16 12:00 d
    -rwxr-xr-x 1 user user 95 Sep 16 12:00 h
    -rwxr-xr-x 1 user user 96 Sep 16 12:00 t
    -rwxr-xr-x 1 user user 51 Sep 16 12:00 u

[FILE] **`test-service/control/d`**

    #!/bin/sh
    echo 'control/d: Executing custom sv down'

[FILE] **`test-service/control/u`**

    #!/bin/sh
    echo 'control/u: Executing custom sv up'

This control files do nothing but print a message for logging purposes.

[FILE] **`test-service/control/h`**

    #!/bin/sh
    chpst -e env \
    sh -c 'echo control/h: Executing custom sv hup...; exit $EXIT_STATUS'

This control file is executed when an [sv hup] command is used. It is assumed that [test-daemon] prints a message of the form \'Message #N\' each time it receives a `SIGHUP` signal, where **N** is an increasing integer.

[FILE] **`test-service/control/t`**

    #!/bin/sh
    chpst -e env \
    sh -c 'echo control/t: Executing custom sv term...; exit $EXIT_STATUS'

This is a deliberate misuse of the [test-service/control/t] file, for demonstration purposes, because it doesn\'t actually stop [test-daemon]. Both [test-service/control/t] and [test-service/control/h] exit with a code that is the value of environment variable `EXIT_STATUS`. A [chpst -e] command is used each time these control files are executed, to modify the environment according to [environment directory](https://wiki.gentoo.org/wiki/Daemontools-encore#changingstate "Daemontools-encore") [env]:

`user `[`$`]`ls -l test-service/env`

    total 4
    -rw-r--r-- 1 user user 2 Sep 16 12:00 EXIT_STATUS

[FILE] **`test-service/env/EXIT_STATUS`**

    1

When [chpst -e] is executed, the value of `EXIT_STATUS` will be 1.

`user `[`$`]`ls -l ../logdir`

    total 4
    -rw-r--r-- 1 user user 26 Sep 16 12:00 config

[FILE] **`../logdir/config`**

    -control/h:*
    econtrol/h:*

The [config] file in the logging directory deselects messages that start with \'control/h:\' for logging to the [current] file (\'-\' action), and selects them for logging to [runsv]\'s standard error (\'e\' action), which in this example is the interactive shell\'s controlling terminal. These would be the messages printed by the [test-service/control/h] file. Contents of the [current] file in the logging directory when the supervision tree is launched, assuming that the scan directory is the working directory:

`user `[`$`]`cat ../logdir/current`

    control/u: Executing custom sv up
    (Re)starting test-daemon

This shows that [test-service/control/u] was executed before [test-service/run]. Using the [sv hup] command:

`user `[`$`]`export SVDIR="$(pwd)"`

`user `[`$`]`for i in 1 2 3; do sv hup test-service; done`

    control/h: Executing custom sv hup...
    control/h: Executing custom sv hup...
    control/h: Executing custom sv hup...

This shows that [test-service/control/h] was executed.

`user `[`$`]`cat ../logdir/current`

    control/u: Executing custom sv up
    (Re)starting test-daemon
    Message #1
    Message #2
    Message #3

This confirms that, because `EXIT_STATUS` is 1, [test-service/control/h] exits with a nonzero code, so a `SIGHUP` signal was also sent to [test-daemon], causing it to print messages to its standard error. Using the [sv -v term] command:

`user `[`$`]`sv -v term test-service`

    ok: run: test-service: (pid 1897) 0s

`user `[`$`]`cat ../logdir/current`

    control/u: Executing custom sv up
    (Re)starting test-daemon
    Message #1
    Message #2
    Message #3
    control/t: Executing custom sv term...
    control/u: Executing custom sv up
    (Re)starting test-daemon

This shows that [test-service/control/t] was executed, and because its exit code is 1, a `SIGTERM` signal was also sent to [test-daemon]. The signal killed the process, and because it is supervised, [test-service/run] is reexecuted. And because there is also a [test-service/control/u] file, it was executed as well, before [test-service/run]. Using the [sv -v down] command:

`user `[`$`]`sv -v down test-service`

    ok: down: test-service: 0s, normally up

The command shows an \"ok\" status and a \"down\" state, so it successfully stopped [test-daemon].

`user `[`$`]`cat ../logdir/current`

    control/u: Executing custom sv up
    (Re)starting test-daemon
    Message #1
    Message #2
    Message #3
    control/t: Executing custom sv term...
    control/u: Executing custom sv up
    (Re)starting test-daemon
    control/t: Executing custom sv term...
    control/d: Executing custom sv down

This shows that both [test-service/control/t] and [test-service/control/d] were executed, in that order. Starting [test-daemon] again with a modified environment directory, assuming the logging directory has been rotated with an [sv alarm test-service/log] command:

`user `[`$`]`echo 0 >test-service/env/EXIT_STATUS`

`user `[`$`]`sv -v up test-service`

    ok: run: test-service: (pid 1926) 0s

Repeating the [sv hup] commands:

`user `[`$`]`for i in 4 5 6; do sv hup test-service; done`

    control/h: Executing custom sv hup...
    control/h: Executing custom sv hup...
    control/h: Executing custom sv hup...

`user `[`$`]`cat ../logdir/current`

    control/u: Executing custom sv up
    (Re)starting test-daemon

This shows that, again, [test-service/control/h] was executed, but this time, because `EXIT_STATUS` is now 0, the script exits with a 0 code, so no `SIGHUP` signal was sent to [test-daemon]. This is confirmed by the absence of logged messages from the process. Stopping [test-daemon] with the [sv -v down] command:

`user `[`$`]`sv -v down test-service`

    timeout: run: test-service: (pid 1926) 64s, want down

`user `[`$`]`sv status test-service`

    run: test-service: (pid 1926) 70s, want down; run: log: (pid 1890) 70s

This shows that, because [test-service/control/t] contains no code to stop [test-daemon], and because its exit code is now 0, [sv] times out (\"timeout\") and the supervised process\' state is still \"run\". Stopping [test-daemon] with the [sv force-stop] command:

`user `[`$`]`sv force-stop test-service`

    kill: run: test-service: (pid 1926) 93s, want down

This shows that because [test-daemon] doesn\'t get stopped, [sv] sends a `SIGKILL` signal to the supervised process on expiry of the wait period, and exits with a \"kill\" status.

`user `[`$`]`cat ../logdir/current`

    control/u: Executing custom sv up
    (Re)starting test-daemon
    control/t: Executing custom sv term...
    control/d: Executing custom sv down
    control/t: Executing custom sv term...
    control/d: Executing custom sv down

`user `[`$`]`sv status test-service`

    down: test-service: 4s, normally up; run: log: (pid 1890) 106s

This confirms that [test-daemon] is now in \"down\" state, and that, again, both [sv] commands executed [test-service/control/t] and then [test-service/control/d].

### [Starting the supervision tree]

#### [From OpenRC]

As of version 0.22, [OpenRC](https://wiki.gentoo.org/wiki/OpenRC "OpenRC") provides a service script that can launch [runsvdir] with [readproctitle]-style logging, also named [runsvdir]. On Gentoo, the scan directory will be [/run/openrc/sv]. This script exists to support the [OpenRC-runit integration](#runitintegration) feature, but can be used to just launch a runit supervision tree when the machine boots by adding it to an OpenRC runlevel using [rc-update]:

`root `[`#`]`rc-update add runsvdir default`

Or it can also be started manually:

`root `[`#`]`rc-service runsvdir start`

** Note**\
The service script launches [runsvdir] using OpenRC\'s [start-stop-daemon] program, so it will run unsupervised. Also, its standard input and output will be redirected to [/dev/null]. Its standard error will be redirected to the [readproctitle]-style log, though.

Because the service script calls [runsvdir] using absolute path [/usr/bin/runsvdir], a symlink to the correct path must be created if using `>=sys-process/runit-2.1.2`:

`root `[`#`]`ln -s /bin/runsvdir /usr/bin/runsvdir`

And because [/run] is a tmpfs, and therefore volatile, servicedir symlinks must be created in the scan directory each time the machine boots, before [runsvdir] starts. The [tmpfiles.d](https://www.freedesktop.org/software/systemd/man/tmpfiles.d.html) interface, which is supported by OpenRC using [package opentmpfiles](https://packages.gentoo.org/packages/sys-apps/opentmpfiles), can be used for this:

[FILE] **`/etc/tmpfiles.d/runsvdir.conf`**

    #Type Path Mode UID GID Age Argument
    d /run/openrc/sv
    L /run/openrc/sv/service1 - - - - /path/to/servicedir1
    L /run/openrc/sv/service2 - - - - /path/to/servicedir2
    L /run/openrc/sv/service3 - - - - /path/to/servicedir3
    ...

Alternatively, OpenRC\'s [local] service could be used to start the supervision tree when entering OpenRC\'s \'default\' runlevel, by placing \'.start\' and \'.stop\' files in [/etc/local.d] (please read [/etc/local.d/README] for more details) that perform actions similar to those of the [runsvdir] service script:

[FILE] **`/etc/local.d/runsvdir.start`**

    #!/bin/sh
    # Remember to add --user if you don't want to run as root
    # Remember to change /usr/bin/runsvdir to /bin/runsvdir if using >=sys-process/runit-2.1.2
    start-stop-daemon --start --background --make-pidfile \
       --pidfile /run/runsvdir.pid \
       --exec /usr/bin/runsvdir -- -P /path/to/scandir readproctitle-like-log-argument

[FILE] **`/etc/local.d/runsvdir.stop`**

    #!/bin/sh
    start-stop-daemon --stop --retry SIGHUP/5 --pidfile /run/runsvdir.pid

The `SIGHUP` signal makes [runsvdir] send a `SIGTERM` signal to all its [runsv] children before exiting, which, in turn, makes them stop their supervised processes and exit. The `SIGTERM` signal that [start-stop-daemon] sends by default would just make [runsvdir] exit.

#### [From sysvinit]

Following upstream\'s suggestion ^[\[2\]](#cite_note-2)^, Gentoo\'s packaging of runit provides a [/sbin/runsvdir-start] symbolic link to [/etc/runit/2], that allows [runsvdir] to be launched and supervised by [sysvinit](https://packages.gentoo.org/packages/sys-apps/sysvinit) by adding a \'respawn\' line for it in [/etc/inittab]. Used in this way, the supervision tree becomes rooted in process 1, which cannot die without crashing the machine.

Gentoo users wanting to use [runsvdir-start] in this way will need to manually edit [/etc/inittab], and then call [telinit]:

[FILE] **`/etc/inittab`**

    SV:12345:respawn:/sbin/runsvdir-start

`root `[`#`]`telinit q`

This will make sysvinit launch and supervise [runsvdir] when entering runlevels 1 to 5.

### [The logging chain]

A supervision tree where all leaf processes have a logger can be arranged into what the author of [s6](https://wiki.gentoo.org/wiki/S6 "S6") calls *the logging chain* ^[\[3\]](#cite_note-3)^, which he considers to be technically superior to the traditional syslog-based centralized approach ^[\[4\]](#cite_note-4)^.

Since processes in a supervision tree are created using the POSIX `fork()` call, each of them will inherit [runsvidir]\'s standard input, output and error. A logging chain arrangement using runit is as follows:

-   Leaf processes should normally have a logger, so their standard output and error connect to their logger\'s standard input. Therefore, all their messages are collected and stored in dedicated, per-service logs by their logger. Some programs might need to be invoked with special options to make them send messages to their standard error, and redirection of standard error to standard output (i.e. **2\>&1** in a shell script) must be performed in the servicedir\'s [run] file.
-   Leaf processes with a controlling terminal are an exception: their standard input, output and error connect to the terminal.
-   [runsv], the loggers, and leaf processes that exceptionally don\'t have logger for some reason, inherit their standard input, output and error from [runsvdir], so their messages are sent wherever the ones from [runsvdir] are.
-   Leaf processes that still unavoidably report their messages using `syslog()` have them collected and logged by a (possibly supervised) syslog server.

If runit [is used as the init system](#runitinit), and [runsvdir] was invoked with no second argument, its standard input, output and error will be redirected to [/dev/console]. If [runsvdir] was invoked with a second argument, [readproctitle]-like logging is turned on and messages sent to [runsvdir]\'s standard error will go to the log and can be seen using [ps]. []

### [Runit as the init system]

** Warning**\
While Gentoo does offer a runit package in its official repository, it is not completely supported as an init system. Gentoo users wanting to use runit as their machine\'s init system might need to use [alternative ebuild repositories](https://wiki.gentoo.org/wiki/Ebuild_repository "Ebuild repository") and/or do some local tweaking. See [\"External resources\"](#External_resources)

The runit package provides a program capable of running as process 1, also called [runit], and a helper program, [runit-init]. If [runit-init] detects it is running as process 1, it replaces itself with [runit] using the POSIX `execve()` call. Therefore, to use [runit] as the system\'s init, a `init=/sbin/runit-init` parameter can be added to kernel\'s command line using the [bootloader\'s](https://wiki.gentoo.org/wiki/Bootloader "Bootloader") available mechanisms (e.g. a [linux] command in some \'Gentoo with runit\' menu entry for [GRUB](https://wiki.gentoo.org/wiki/GRUB "GRUB")). It is possible to go back to sysvinit + OpenRC at any time by reverting the change.

When the machine starts booting (if an [initramfs](https://wiki.gentoo.org/wiki/Initramfs "Initramfs") is being used, after it passes control to the \'main\' init), [runit] executes the [/etc/runit/1] file as a child process, in a foreground process group with [/dev/console] as the controlling terminal, and waits for it to finish. This file is usually a shell script, and is expected to perform all one time initialization tasks needed to bring the machine to its stable, normal \'up and running\' state. Gentoo\'s [/etc/runit/1] file is quite minimal, it only calls the [openrc] program to enter OpenRC\'s **sysinit** runlevel, and then its **boot** runlevel, emulating Gentoo\'s sysvinit setup.

** Note**\
This setup means that any long-lived processes launched by a service script upon entering OpenRC\'s \'sysinit\' and \'boot\' runlevels won\'t be supervised

When [/etc/runit/1] exits, [runit] then executes the [/etc/runit/2] file as a child process, makes it a session leader with the POSIX `setsid()` call, and *supervises* it: if [/etc/runit/2] is killed by a signal or its exit code is **111**, then [runit] will restart it, after sending a `SIGKILL` signal to every remaining process in its process group. Gentoo\'s [/etc/runit/2] file is upstream\'s suggested one with minimal modifications. It is a shell script that uses the [exec] builtin utility to replace itself with [runsvdir], so this creates a supervision tree rooted in process 1. The scan directory will be [/var/service] for `<sys-process/runit-2.1.2`, and [/etc/service] for `>=sys-process/runit-2.1.2`. The enviroment will be empty, except for the `PATH` variable, set to a known value in the script. [runsvdir] will use [readproctitle]-like logging, and, for `>=sys-process/runit-2.1.2`, is also passed the `-P` option.

Gentoo\'s packaging of runit expects [/etc/runit/runsvdir/all] for `<sys-process/runit-2.1.2`, or [/etc/sv] for `>=sys-process/runit-2.1.2`, to be a repository of service directories. Services that need to be started when the machine boots require a symbolic link in the scan directory to the corresponding servicedir in that repository. Gentoo only provides service directories for 6 parallel supervised [agetty] processes (with their symlinks in the scan directory); this allow users to get to a text console login, like with Gentoo\'s sysvinit setup. Service directories for anything else must be created by the administrator, either from scratch or taken from somewhere else (e.g. alternative ebuild repositories).

If [runit] receives a `SIGCONT` signal, and the file [/etc/runit/stopit] exists and has the execute by owner permission set, it will kill [/etc/runit/2] (first by sending it a `SIGTERM` signal and waiting, then by sending it a `SIGKILL` signal) and then execute the [/etc/runit/3] file. This file is usually a shell script, and is expected to perform all tasks needed to shut the machine down. If [/etc/runit/1] is killed by a signal or its exit code is **100**, [runit] skips execution of [/etc/runit/2] and executes [/etc/runit/3]. [runit] will also execute [/etc/runit/3] if [/etc/runit/2] exits (with an exit code other than 111). If [/etc/runit/3] exits, [runit] will send a `SIGKILL` signal to all remaining processes, and then check the file [/etc/runit/reboot] to decide what to do next. If the file exists and has the execute by owner permission set, it reboots the machine. In any other case, it will power off the machine, or halt it if it can\'t power it off.

Gentoo\'s [/etc/runit/3] file performs an [sv shutdown] for `<sys-process/runit-2.1.2`, or an [sv force-shutdown] for `>=sys-process/runit-2.1.2`, on every servicedir of [runsvdir]\'s scan directory, and then calls the [openrc] program to enter OpenRC\'s **shutdown** or **reboot** runlevels, depending on whether a poweroff or reboot operation was requested to [runit] via [/etc/runit/reboot].

If [runit] receives a `SIGINT` signal (which is usually configured to happen when key combination [Ctrl]+[Alt]+[Del] is pressed), and the file [/etc/runit/ctrlaltdel] exists and has the execute by owner permission set, it will execute it as a child process, and when it exits, behave as if it had received a `SIGCONT` signal. Gentoo\'s [/etc/runit/ctrlaltdel] prints a \"*System is going down in 14 seconds\...*\" message using the [wall] utility, makes sure file [/etc/runit/stopit] exists and has the execute by owner permission set, waits 14 seconds and then exits. The result being that `SIGINT` will either halt or reboot the machine after 14 seconds, depending on [/etc/runit/reboot].

All [runit]\'s children run with their standard input, output and error initially redirected to [/dev/console].

#### [Reboot and shutdown]

The [runit-init] program can be used to shut the machine down. Unless it is running as process 1, it accepts one argument, which can be either **0** or **6**:

-   If it is 0, [runit-init] will create the [/etc/runit/stopit] and [/etc/runit/reboot] files if any of them does not exist, set the execute by owner permission for the former, unset it for the latter, and send a `SIGCONT` signal to process 1.
-   If it is 6, [runit-init] will create the [/etc/runit/stopit] and [/etc/runit/reboot] files if any of them does not exist, set the execute by owner permission for both of them, and send a `SIGCONT` signal to process 1.

Therefore, if process 1 is [runit], then [runit-init 0] will power off the machine, and [runit-init 6] will reboot it.

This means that [runit] is not directly compatible with sysvinit\'s [telinit], [halt], [poweroff], [reboot], and [shutdown] commands. However, many programs (e.g. desktop environments) expect to be able to call programs with those names during operation, so if such thing is needed, it is possible to use compatibility shell scripts:

[FILE] **`$PATH/shutdown`**

    #!/bin/sh
    runit-init 0

[FILE] **`$PATH/reboot`**

    #!/bin/sh
    runit-init 6

#### [The runsvchdir program]

Runit doesn\'t directly support any runlevel-like concept, but if the machine contains a set of directories, each one with a scan directory structure, then it is possible to have a behaviour similar to \'changing runlevels\' if the scan directory argument of runsvdir is actually a symbolic link. The software package\'s author proposes^[\[5\]](#cite_note-5)^ creating a symbolic link to directory pointing to one of the aforementioned directories, which then becomes the current scan directory. Runit provides a [runsvchdir] program that can atomically modify this symlink, thereby switching the current scan directory used by [runsvdir]. As a result, on [runsvdir]\'s next periodic scan, new supervised processes can be started, and some supervised processes can be stopped: new [runsv] processes will be spawned for service directories present in the new scan directory but not in the old one, and running [runsv] processes will be sent `SIGTERM` signals (resulting in the equivalent of an [sv exit] command) if their corresponding service directories are present in the old scan directory but not in the new one. Supervised processes that have service directories with the same name in both the old and new scan directory remain unaffected.

Using [runsvchdir] requires that the scan directory be specified to [runvsdir] as pathname [/etc/runit/runsvdir/current], or a symbolic link that resolves to that pathname. This means that [runsvchdir] can affect only a single [runsvdir] process, which is normally the one started by [/etc/runit/2] and supervised by process 1. [runsvchdir] accepts a pathname specifying the new scan directory as an argument, that must not start with a dot (\'.\'); it creates a symlink named [/etc/runit/runsvdir/current.new] that points to this pathname, renames [/etc/runit/runsvdir/current] to [/etc/runit/runsvdir/previous], and then renames [/etc/runit/runsvdir/current.new] to [/etc/runit/runsvdir/current]. This means that if the supplied pathname does not start with a slash (\'/\'), it will be interpreted as relative to [/etc/runit/runsvdir]. Therefore, if [/etc/runit/runsvdir/runlevelA] and [/etc/runit/runsvdir/runlevelB] are runit scan directories, and [/etc/runit/runsvdir/current] is currently a symbolic link to [/etc/runit/runsvdir/runlevelA], then command [runsvchdir runlevelB] performs a \'runlevel change\' to *runlevelB*. For further details on [runsvchdir], please consult the respective man page.

Gentoo\'s packaging of runit version 2.1.1 supports this model: runsvdir\'s scan directory is [/var/service], a symbolic link to [/etc/runit/runsvdir/current]. After package installation, a directory named [/etc/runit/runsvdir/default] is created, emulating a \'default runlevel\', and initially [/etc/runit/runsvdir/current] points to [/etc/runit/runsvdir/default]. Directory [/etc/runit/runsvdir/default] contains initially symbolic links to the 6 service directories for [agetty] processes installed in the servicedir repository ([/etc/runit/runsvdir/all]).

Gentoo\'s packaging of runit version 2.1.2 does away with this runlevel-like setup.

Examples of [runsvchdir] usage (with a setup more similar to that of [Void Linux](https://voidlinux.org) rather than Gentoo\'s):

`user `[`$`]`ls -l /etc/runit/runsvdir/current`

    lrwxrwxrwx 1 root root 7 Sep 23  2017 /etc/runit/runsvdir/current -> default

`root `[`#`]`runsvchdir default`

    runsvchdir: default: current.

This shows that using [runsvchdir] with a pathname that [/etc/runit/runsvdir/current] already points to has no effect.

`root `[`#`]`runsvchdir /home/user/custom-scandir`

    runsvchdir: /home/user/custom-scandir: now current.

`user `[`$`]`ls -l /etc/runit/runsvdir`

    total 8
    lrwxrwxrwx 1 root root   25 Sep 17 12:00 current -> /home/user/custom-scandir
    drwxr-xr-x 2 root root 4096 Sep 23  2017 default
    lrwxrwxrwx 1 root root    7 Sep 17 12:00 previous -> default
    drwxr-xr-x 2 root root 4096 Sep 23  2017 single

This shows that [runsvchdir] also updated symbolic link [/etc/runit/runsvdir/previous].

`root `[`#`]`runsvchdir single`

    runsvchdir: single: now current.

`user `[`$`]`ls -l /etc/runit/runsvdir`

    total 8
    lrwxrwxrwx 1 root root    6 Sep 17 12:10 current -> single
    drwxr-xr-x 2 root root 4096 Sep 23  2017 default
    lrwxrwxrwx 1 root root   25 Sep 17 12:10 previous -> /home/user/custom-scandir
    drwxr-xr-x 2 root root 4096 Sep 23  2017 single

#### [Runit and service management]

Runit doesn\'t have service manager features, i.e. it does not provide mechanisms for specifiying dependencies, service ordering constraits, etc. like OpenRC does using `depend()` functions in service scripts. If such things are needed, the desired behaviour must be explicitly enforced in the code of [run] files; the software package\'s author provides some tips on how to do that ^[\[6\]](#cite_note-6)^. Sometimes, just doing nothing *might* be enough: if [run] simply exits with an error status when there is an unmet required condition, and, perhaps with help from a [finish] files that analyzes the exit code, the state the machine was in before [run] was executed is restored, the supervisor would just keep restarting the service until, after some convergence period, all its required conditions are met. The author of nosh calls this \"*the thundering herd solution*\" ^[\[7\]](#cite_note-7)^.

Nevertheless, OpenRC and runit do not interfere with each other, so it is possible to use OpenRC-managed services on a machine where the init system is runit. In particular, once the supervision tree rooted in process 1 is launched, it is still possible to manually start individual OpenRC services using [rc-service], or even entering OpenRC\'s \'default\' runlevel manually:

`root `[`#`]`openrc default`

Services from OpenRC\'s \'default\' runlevel could be started automatically on boot using the existing [local] service, moving it to the \'boot\' runlevel:

[FILE] **`/etc/local.d/rc-default.start`Enter OpenRC\'s \'default\' runlevel**

    #!/bin/sh
    openrc default

`root `[`#`]`rc-update del local default`

`root `[`#`]`rc-update add local boot`

Alternatively, [/etc/runit/1] can be modified to add the corresponding [openrc] invocation:

[FILE] **`/etc/runit/1`**

    RUNLEVEL=S /sbin/openrc default

Note however that OpenRC services will not be supervised by runit.

Runit can be used without OpenRC\'s service management, but this requires alternative implementation of the functionality of its service scripts, especially those executed upon entering the \'sysinit\', \'boot\' and \'shutdown\' runlevels, and replacing the Gentoo-provided [/etc/runit/1] and [/etc/runit/3] files with custom ones, since they call the [openrc] program. It can be be useful to study those from runit-based distributions (e.g. see Void Linux\'s ones in [their void-runit package sources](https://github.com/void-linux/void-runit)). []

### [][OpenRC\'s runit integration feature]

Starting with version 0.22, OpenRC can launch supervised long-lived processes using the runit package as a helper ^[\[8\]](#cite_note-8)^. This is an alternative to \'classic\' unsupervised long-lived processes launched using the [start-stop-daemon] program. It should be noted that service scripts that don\'t contain `start()` and `stop()` functions implicitly use [start-stop-daemon].

OpenRC services that want to use runit supervision need both a service script in [/etc/init.d] and a runit service directory. The service script must contain a `supervisor=runit` variable assignment to turn the feature on, and must have a \'need\' dependency on the [runsvdir] service in its `depend()` function, to make sure the [runsvdir] program is launched (see [here](#openrclaunch)). It can contain neither a `start()` function, nor a `stop()` function (but their `_pre()` and `_post()` variants are OK), nor a `status()` function; OpenRC internally invokes [sv] when the service script is called with a \'start\', \'stop\' or \'status\' argument.

The runit service directory can be placed anywhere in the filesystem, and have any name, as long as the service script (or the service-specific configuration file in [/etc/conf.d]) assigns the servicedir\'s absolute path to the `runit_service` variable. If `runit_service` is not assigned to, the runit servicedir must have the same name as the OpenRC service script, and will be searched in the \>=sys-process/runit-2.1.2 service directory repository, [/etc/sv]. The scan directory when using this feature is [/run/openrc/sv], and OpenRC will create a symlink to the service directory when the service is started, and delete it when the service is stopped.

** Warning**\
OpenRC does not integrate as expected when runit is [used as the init system](#runitinit), since there will be two [runsvdir] processes: the one supervised by [runit] with [/etc/service] or [/var/service] as the scan directory, and the unsupervised one launched by OpenRC with [/run/openrc/sv] as the scan directory. So the result will be two independent supervision trees.

Example setup for a hypothetical supervised *test-daemon* service, with and without a dedicated logger.

[FILE] **`/etc/init.d/test-service`OpenRC service script**

    #!/sbin/openrc-run
    description="A supervised test service"
    supervisor=runit
    runit_service=/home/user/test/svc-repo/test-service

    depend()

`user `[`$`]`/sbin/rc-service test-service describe`

    * A supervised test service
    * cgroup_cleanup: Kill all processes in the cgroup

[FILE] **`/etc/init.d/test-service-logged`OpenRC service script**

    #!/sbin/openrc-run
    description="A supervised test service with a logger"
    supervisor=runit
    runit_service=/home/user/test/svc-repo/test-service-logged

    depend()

`user `[`$`]`/sbin/rc-service test-service-logged describe`

    * A supervised test service with a logger
    * cgroup_cleanup: Kill all processes in the cgroup

The service directories:

`user `[`$`]`ls -l /home/user/test/svc-repo/test-service* /home/user/test/svc-repo/test-service*/log`

    test-service:
    total 4
    -rwxr-xr-x 1 user user 96 Jun 17 12:00 run

    test-service-logged:
    total 8
    drwxr-xr-x 2 user user 4096 Jun 17 12:00 log
    -rwxr-xr-x 1 user user  101 Jun 17 12:00 run

    test-service-logged/log:
    total 4
    -rwxr-xr-x 1 user user 62 Jun 17 12:00 run

[FILE] **`test-service/run`**

    #!/bin/sh
    exec \
    chpst -o 5 \
    chpst -u daemon \
    /home/user/test/test-daemon

This launches program [test-daemon] with effective user *daemon* and the maximum number of open file descriptors set to 5. This is the same as if [test-daemon] performed a `setrlimit(RLIMIT_NOFILE, &rl)` call itself with `rl.rlim_cur` set to 5, provided that value does not exceed the corresponding hard limit. The program also periodically sends a message of the form \"*Logged message #N*\" to its standard error.

[FILE] **`test-service-logged/run`**

    #!/bin/sh
    exec \
    chpst -o 5 \
    chpst -u daemon \
    /home/user/test/test-daemon 2>&1

[FILE] **`test-service-logged/log/run`**

    #!/bin/sh
    exec \
    chpst -u user \
    svlogd -tt /home/user/test/logdir

The redirection of [test-daemon]\'s standard error to standard output allows logging its messages using runit\'s [svlogd]. An automatically rotated logging directory named *logdir* will be used, and messages will have a UTC timestamp prepended to them.

Manually starting [test-service-logged]:

`root `[`#`]`rc-service test-service-logged start`

    * /run/openrc/sv: creating directory
    * Starting runsvdir ...                       [ ok ]
    * Starting test-service-logged ...
    * Failed to start test-service-logged         [ !! ]
    * ERROR: test-service-logged failed to start

** Warning**\
There\'s currently a bug in the implementation of service startup; OpenRC calls [sv start] immediately after creating the servicedir symlink in the scan directory, instead of waiting for [runsvdir]\'s next periodic scan. Because no [runsv] process has been launched yet, [sv start] will fail. However, if there is no [down] file in the service directory, after the next scan the service will go up regardless, when the corresponding [runsv] process is launched.

`root `[`#`]`rc-service test-service-logged status`

    run: /run/openrc/sv/test-service-logged: (pid 2155) 24s; run: log: (pid 2154) 24s

Make OpenRC\'s notion of the service\'s state catch up:

`root `[`#`]`rc-service test-service-logged start`

    * Starting test-service-logged ...            [ ok ]

The resulting supervision tree so far:

`user `[`$`]`ps axf -o pid,ppid,pgrp,euser,args`

      PID  PPID  PGRP EUSER    COMMAND
     ...
     1931     1  1931 root     /usr/bin/runsvdir -P /run/openrc/sv log: ...................................................
     2153  1931  2153 root      \_ runsv test-service-logged
     2154  2153  2153 user          \_ svlogd -tt /home/user/test/logdir
     2155  2153  2153 daemon        \_ /home/user/test/test-daemon
     ...

Messages from the [test-daemon] process with PID 2155 go to the logging directory:

`user `[`$`]`ls -l /home/user/test/logdir`

    total 12
    -rwxr--r-- 1 user user 441 Jun 17 12:19 @4000000059454877288a41fc.s
    -rwxr--r-- 1 user user 264 Jun 17 12:19 @400000005945489513993834.s
    -rw-r--r-- 1 user user 706 Jun 17 12:20 current
    -rw------- 1 user user   0 Jun 17 12:04 lock

`user `[`$`]`cat /home/user/test/logdir/current`

    2017-06-17_12:19:42.20404 Logged message #1
    2017-06-17_12:19:47.20759 Logged message #2
    2017-06-17_12:19:52.21598 Logged message #3
    2017-06-17_12:19:57.21806 Logged message #4
    2017-06-17_12:20:02.22180 Logged message #5
    2017-06-17_12:20:07.22399 Logged message #6

Manually starting [test-service]:

`root `[`#`]`rc-service test-service start`

    * Starting test-service ...
    * Failed to start test-service                [ !! ]
    * ERROR: test-service failed to start

Make OpenRC\'s notion of the service\'s state catch up because of the service startup bug:

`root `[`#`]`rc-service test-service start`

    * Starting test-service ...                   [ ok ]

`user `[`$`]`rc-status`

    Runlevel: default
    ...
    Dynamic Runlevel: needed/wanted
    runsvdir                                      [  started  ]
    ...
    Dynamic Runlevel: manual
    test-service-logged                           [  started  ]
    test-service                                  [  started  ]

The scan directory:

`user `[`$`]`ls -l /run/openrc/sv`

    total 0
    lrwxrwxrwx 1 root root 46 Jun 17 12:25 test-service -> /home/user/test/svc-repo/test-service
    lrwxrwxrwx 1 root root 53 Jun 17 12:12 test-service-logged -> /home/user/test/svc-repo/test-service-logged

Final supervision tree:

`user `[`$`]`ps axf -o pid,ppid,pgrp,euser,args`

      PID  PPID  PGRP EUSER    COMMAND
     ...
     1931     1  1931 root     /usr/bin/runsvdir -P /run/openrc/sv log: ged message #8 Logged message #9 Logged message #10
     2153  1931  2153 root      \_ runsv test-service-logged
     2154  2153  2153 user      |   \_ svlogd -tt /home/user/test/logdir
     2155  2153  2153 daemon    |   \_ /home/user/test/test-daemon
     2249  1931  2249 root      \_ runsv test-service
     2250  2249  2249 daemon        \_ /home/user/test/test-daemon
     ...

Since the [test-daemon] process with PID 2250 doesn\'t have a dedicated logger, its messages go to [runsvdir]\'s standard error, are logged [readproctitle]-style, and show up in [ps]\' output (for process 1931 in this case).

## [Removal]

### [Unmerge]

`root `[`#`]`emerge --ask --depclean --verbose sys-process/runit`

Service directories, additional scan directories, the [/usr/bin/runsvdir] symlink to [/bin/runsvdir], etc. must be manually deleted if no longer wanted after removing the package. Also, all modifications to sysvinit\'s [/etc/inittab] must be manually reverted: lines for [runsvdir-start] must be deleted, and a [telinit q] command must be used afterwards. And obviously, if runit is being used as the init system, an alternative one must be installed in parallel, and the machine rebooted to use it (possibly by reconfiguring the bootloader), before the package is removed, or otherwise the machine will become unbootable.

## [See also]

-   [S6](https://wiki.gentoo.org/wiki/S6 "S6") --- a package that provides a [daemontools-inspired](https://wiki.gentoo.org/wiki/Daemontools "Daemontools") process supervision suite, a notification framework, a UNIX domain super-server, and tools for file descriptor holding and suidless privilege gain.
-   [Comparison of init systems](https://wiki.gentoo.org/wiki/Comparison_of_init_systems "Comparison of init systems") --- compares and contrasts **[init systems](https://wiki.gentoo.org/wiki/Init_system "Init system")** for Unix(like) [OSs](https://en.wikipedia.org/wiki/Operating_system "wikipedia:Operating system")

## [External resources]

-   [Section runit in the Void Linux Handbook](https://docs.voidlinux.org/config/services/index.html) (a runit-based GNU/Linux distribution).
-   [Runit article on the Arch Linux Wiki](https://wiki.archlinux.org/index.php/runit).
-   [A thread about runit on the Gentoo Forums](https://forums.gentoo.org/viewtopic-p-7605220.html).
-   [The flussence ebuild repository](https://gitlab.com/flussence/overlay), providing an alternative runit packaging, and accompanying [runit-scripts repository](https://gitlab.com/flussence/runit-scripts).
-   [The powerman ebuild repository](https://github.com/powerman/powerman-overlay), providing an alternative runit packaging, service directory [run] files for many services, and runit boot scripts.
-   [Avery Payne\'s supervision-scripts project](https://bitbucket.org/avery_payne/supervision-scripts), compatible with runit.

## [References]

1.  [[[↑](#cite_ref-1)] [Linux Standard Base Core Specification 5.0.0, Generic Part, Chapter 22, \"System Initialization\", [22.2, \"Init Script Actions\"](https://refspecs.linuxfoundation.org/LSB_5.0.0/LSB-Core-generic/LSB-Core-generic/iniscrptact.html). Retrieved on June 4th, 2017.]]
2.  [[[↑](#cite_ref-2)] [[Using runit with sysvinit and inittab](http://smarden.org/runit/useinit.html#sysv). Retrieved on May 28th, 2017.]]
3.  [[[↑](#cite_ref-3)] [Laurent Bercot, [the logging chain](https://www.skarnet.org/software/s6/s6-log.html#loggingchain), Retrieved on May 1st, 2017.]]
4.  [[[↑](#cite_ref-4)] [Laurent Bercot, [on the syslog design](https://www.skarnet.org/software/s6/s6-log.html#diesyslogdiedie), Retrieved on May 1st, 2017.]]
5.  [[[↑](#cite_ref-5)] [[runit - runlevels](http://smarden.org/runit/runlevels.html). Retrieved on June 10th, 2017.]]
6.  [[[↑](#cite_ref-6)] [[runit - service dependencies](http://smarden.org/runit/dependencies.html). Retrieved on June 10th, 2017.]]
7.  [[[↑](#cite_ref-7)] [Jonathan de Boyne Pollard, the nosh Guide, [Introduction](https://jdebp.uk/Softwares/nosh/guide/introduction.html), section \"Differentiation from other systems\", bullet \"No daemontools-style thundering herds\". Retrieved on June 10th, 2017.]]
8.  [[[↑](#cite_ref-8)] [[Using runit with OpenRC](https://github.com/OpenRC/openrc/blob/master/runit-guide.md). Retrieved on June 15th, 2017.]]