**Resources**

[[]][Home](https://untroubled.org/daemontools-encore)

[[]][GitHub](https://github.com/bruceg/daemontools-encore)

[[]][Package information](https://packages.gentoo.org/packages/sys-process/daemontools-encore)

[![Ohloh Logo](/images/thumb/c/c1/Ohloh-logo.png/30px-Ohloh-logo.png)][Open Hub](https://www.openhub.net/p/daemontools-encore)

**Daemontools-encore** is a backwards compatible, enhanced version of [Daniel J. Bernstein\'s daemontools package](https://wiki.gentoo.org/wiki/Daemontools "Daemontools"), written by Bruce Guenter. A summary of the features that have been added to daemontools-encore is available [here](https://untroubled.org/daemontools-encore/CHANGES). The last release of daemontools-encore was in 2014 (as of 2021-11).

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
    -   [[3.1] [Service directories]](#Service_directories)
    -   [[3.2] [The scan directory and supervision tree]](#The_scan_directory_and_supervision_tree)
    -   [[3.3] [The start, stop and notify files, and the daemontools-encore extended service state]](#The_start.2C_stop_and_notify_files.2C_and_the_daemontools-encore_extended_service_state)
    -   [[3.4] [Logging]](#Logging)
        -   [[3.4.1] [The multilog program]](#The_multilog_program)
        -   [[3.4.2] [The readproctitle program]](#The_readproctitle_program)
        -   [[3.4.3] [The logging chain]](#The_logging_chain)
        -   [[3.4.4] [Specifying a logger for svscan]](#Specifying_a_logger_for_svscan)
    -   [[3.5] [Supervised process execution state changes]](#Supervised_process_execution_state_changes)
    -   [[3.6] [Controlling supervised processes]](#Controlling_supervised_processes)
    -   [[3.7] [Starting the supervision tree]](#Starting_the_supervision_tree)
        -   [[3.7.1] [From OpenRC]](#From_OpenRC)
        -   [[3.7.2] [The svscanboot script]](#The_svscanboot_script)
        -   [[3.7.3] [The supervise-scripts package]](#The_supervise-scripts_package)
-   [[4] [Removal]](#Removal)
    -   [[4.1] [Unmerge]](#Unmerge)
-   [[5] [See also]](#See_also)
-   [[6] [External Resources]](#External_Resources)
-   [[7] [References]](#References)

## [Installation]

### [USE flags]

### [USE flags for] [sys-process/daemontools-encore](https://packages.gentoo.org/packages/sys-process/daemontools-encore) [[]] [Collection of tools for managing UNIX services]

  ----------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------
  [`selinux`](https://packages.gentoo.org/useflags/selinux)   !!internal use only!! Security Enhanced Linux support, this must be set by the selinux profile or breakage will occur
  [`static`](https://packages.gentoo.org/useflags/static)     !!do not set this during bootstrap!! Causes binaries to be statically linked instead of dynamically
  ----------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2025-10-12 04:19] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

`root `[`#`]`emerge --ask sys-process/daemontools-encore`

** Important**\
Daemontools-encore is currently on the testing branch. Users with systems on the stable branch will need to add the package to [/etc/portage/package.accept_keywords] (if using Portage) to be able to install it. While it is generally not advised to mix packages of stable and testing branches, this package only depends on the [libc](https://wiki.gentoo.org/wiki/Libc "Libc"), so in this case it should be safe

## [Configuration]

### [Environment variables]

-   `SUPERVISEDIR` - Name of the directory used by [supervise] for its control files. If it is an absolute pathname, it will be suffixed by all programs that use it with the path to the corresponding service directory, with all slashes (\'/\') replaced with colons (\':\'). Otherwise, it is taken relative to the corresponding service directory. For example, if `SUPERVISEDIR` is set to [/run/supervise], a [supervise] process running for service directory [/service/foo] will place its control files in directory [/run/supervise/service:foo].
-   `SOFTLIMIT_ALLBYTES` - Alternative to [softlimit]\'s `-a` option for specifying the corresponding soft limit.
-   `SOFTLIMIT_COREBYTES` - Alternative to [softlimit]\'s `-c` option for specifying the corresponding soft limit.
-   `SOFTLIMIT_DATABYTES` - Alternative to [softlimit]\'s `-d` option for specifying the corresponding soft limit.
-   `SOFTLIMIT_FILEBYTES` - Alternative to [softlimit]\'s `-f` option for specifying the corresponding soft limit.
-   `SOFTLIMIT_LOCKEDBYTES` - Alternative to [softlimit]\'s `-l` option for specifying the corresponding soft limit.
-   `SOFTLIMIT_MEMBYTES` - Alternative to [softlimit]\'s `-m` option for specifying the corresponding soft limits.
-   `SOFTLIMIT_OPENFILES` - Alternative to [softlimit]\'s `-o` option for specifying the corresponding soft limit.
-   `SOFTLIMIT_PROCS` - Alternative to [softlimit]\'s `-p` option for specifying the corresponding soft limit.
-   `SOFTLIMIT_RSSBYTES` - Alternative to [softlimit]\'s `-r` option for specifying the corresponding soft limit.
-   `SOFTLIMIT_STACKBYTES` - Alternative to [softlimit]\'s `-s` option for specifying the corresponding soft limit.
-   `SOFTLIMIT_CPUSECS` - Alternative to [softlimit]\'s `-t` option for specifying the corresponding soft limit.

### [Files]

-   [/service] - Location of the scan directory when using [OpenRC](https://wiki.gentoo.org/wiki/OpenRC "OpenRC"), [[svscanboot]](#svscanboot) or [[svscan-add-to-inittab]](#supervise-scripts).

### [Service]

#### [OpenRC]

See [here](#openrclaunch)

## [Usage]

[Bernstein daemontools](https://wiki.gentoo.org/wiki/Daemontools "Daemontools") and daemontools-encore implement *process supervision*: programs that run as long-lived processes, such as a server program, can be supervised by being run as a child process of a *supervisor*. The supervisor can detect if the process, also called *the service* or *the daemon* in this context, has unexpectedly terminated, e.g. because it exited with an error status or was killed by a signal, and automatically restart it. The supervisor also provides a reliable interface for controlling both the supervised process and itself, to send signals to the process, and to query status information about it.

All this is based on standard POSIX features: a process reliably knows its child\'s process ID (PID), because it is the return value of the `fork()` call that creates it, knows when its child terminates, because it is notified with a `SIGCHLD` signal, and can obtain exit status information when it happens using the `wait()` or `waitpid()` calls.

For more information information about process supervision see ^[\[1\]](#cite_note-1)^ ^[\[2\]](#cite_note-2)^ ^[\[3\]](#cite_note-3)^.

### [Service directories]

The program that implements the supervisor features in Bernstein daemontools and daemontools-encore is [supervise]. Supervision for a single process is configured using a *service directory* (or *servicedir*). A servicedir is an ordinary directory containing at least one executable file named [run]. It can also contain an optional, regular file named [down]. The (absolute or relative to the working directory) pathname of this directory is then passed as an argument to [supervise]. This however is not supposed to be done directly by the user, but to happen indirectly as a consequence of running [svscan].

When [supervise] is invoked, it changes its working directory to the specifed servicedir, and executes the contained [run] file as a child process, unless there is also a [down] file, or, for daemontools-encore only, a [start] file (see [the start, stop and notify files, and the daemontools-encore extended service state](#startstopnotify)). Daemontools-encore\'s [supervise] also makes the child process the leader of a new session using the POSIX `setsid()` call, unless the servicedir contains a regular file named [no-setsid]. In that case, the child process will run in [supervise]\'s session instead. Making the child process a session leader with Bernstein daemontools requires using the [pgrphack] program inside [run] (see [supervised process execution state changes](#changingstate)). If [supervise] is invoked with a servicedir that contains a [down] file, the [run] file won\'t be executed, but the service can be started later with the [svc] program (see [controlling supervised processes](#controlling)). The contents of the [down] and [no-setsid] files are ignored, so they are usually empty.

[run] can have any file format that the kernel knows how to execute, but is usually a shell script that performs some sort of initialization, and then calls the real program intended to be supervised, using the shell\'s [exec] builtin utility. This allows the program to run without creating a new process, so it will have the same PID as the [run] script, and from there on become the supervised process. [supervise] waits for 1 second between two child process spawns, so that it does not loop too quickly if the process exits immediately. The daemontools-encore version of [supervise] also has special behaviour when it receives a signal: if it receives a `SIGTERM` signal, it behaves as if an [svc -dx] command naming the corresponding servicedir had been used (see [controlling supervised processes](#controlling)), if it receives a `SIGTSTP` signal, it sends a `SIGSTOP` signal to the supervised process, as if an [svc -p] command naming the corresponding servicedir had been used, and if it receives a `SIGCONT` signal, it sends a `SIGCONT` signal to the supervised process, as if an [svc -c] command naming the corresponding servicedir had been used.

Programs that fail to adhere to certain design criteria, including those that use `fork()` in order to \"put the daemon into the background\" ^[\[4\]](#cite_note-4)^, might not be able to be supervised. Sometimes programs can meet those criteria if passed certain options (e.g. a \'run in the foreground\' option) on invocation.

An example of a minimal (and simplistic) service directory for a hypothetical [test-daemon] program:

`user `[`$`]`ls -l`

    total 4
    -rwxr-xr-x 1 user user 27 May  5 12:00 run

[FILE] **`run`**

    #!/bin/sh
    exec test-daemon

The [supervise] program keeps control files in a subdirectory of the servicedir, also named [supervise]. If this subdirectory doesn\'t exist when supervise is invoked, it will be created, as well as any of its missing files. If the servicedir contains a [supervise] symbolic link to directory instead of a subdirectory, [supervise] will follow it and use the linked-to directory for its control files. Daemontools-encore also allows setting the name of this control directory via the `SUPERVISEDIR` environment variable, see [environment variables](#Environment_variables).

** Important**\
The service directory can be in a read-only filesystem, but files contained in the [supervise] directory must writable by the effective user of the corresponding [supervise] process. For Bernstein daemontools, and for daemontools-encore when some of the control files are missing, the directory itself must also be writable. So in this case a symbolic link to an existing directory in a read-write filesystem must be used.

Service directories can also optionally contain a subdirectory or symbolic link to directory named [log], which can be used for setting up a dedicated logger (see [logging](#logging)).

For further details about the [supervise] program and service directories, please consult the [supervise] man page.

Service directory with a [supervise] subdirectory:

`user `[`$`]`ls -l`

    total 8
    -rwxr-xr-x 1 user user   27 May  5 12:00 run
    drwx------ 2 user user 4096 May  5 12:00 supervise

[supervise] subdirectory contents:

`user `[`$`]`ls -l supervise`

    total 4
    prw------- 1 user user  0 May  5 12:00 control
    -rw------- 1 user user  0 May  5 12:00 lock
    prw------- 1 user user  0 May  5 12:00 ok
    -rw-r--r-- 1 user user 18 May  5 12:00 status

### [The scan directory and supervision tree]

Bernstein daemontools and daemontools-encore allow supervising a set of processes running in parallel using the [svscan] program and a *scan directory* (or *scandir*). A scan directory is a directory that contains service directories and/or symbolic links to services directories. Invoking [svscan] with the (absolute or relative to the working directory) path of the scandir as its first argument (and only argument for Bernstein daemontools\' [svscan]) launches one child [supervise] process for each contained service directory with a name that does not start with a dot (\'.\'). If [svscan] is called with no arguments, it assumes the working directory is the scandir, otherwise it changes its working directory to the specified scandir.

Every 5 seconds, [svscan] rereads the scan directory (i. e. performs a *scan*), launching [supervise] processes for each new servicedir it finds, or old servicedir for which it finds its [supervise] process has exited. [svscan] acts as a supervisor for every [supervise] child, just like [supervise] does for its child process. This arrangement of processes is called the *supervision tree*. The root of the supervision tree is [svscan], so it is designed to be robust and to cope with [supervise] processes exiting unexpectedly, being killed, or being unable to start. The leaves of the supervision tree are the processes that correspond to the service directories in the scandir.

Example scan directory containing three service directories:

`user `[`$`]`ls -l`

    total 12
    drwxr-xr-x 3 user user 4096 May  5 12:00 test-service1
    drwxr-xr-x 3 user user 4096 May  5 12:00 test-service2
    drwxr-xr-x 3 user user 4096 May  5 12:00 test-service3

[FILE] **`test-service1/run`**

    #!/bin/sh
    exec test-daemon1

[FILE] **`test-service2/run`**

    #!/bin/sh
    exec test-daemon2

[FILE] **`test-service3/run`**

    #!/bin/sh
    exec test-daemon3

Resulting supervision tree when [svscan] is run on this scandir as a background process in an interactive shell, assuming it is the working directory (i.e. launched with [svscan &]):

`user `[`$`]`ps xf -o pid,ppid,pgrp,euser,args`

      PID  PPID  PGRP EUSER    COMMAND
    ...
     1777  1764  1777 user -bash
     2047  1777  2047 user  \_ svscan
     2048  2047  2047 user      \_ supervise test-service3
     2053  2048  2047 user      |   \_ test-daemon3
     2049  2047  2047 user      \_ supervise test-service1
     2052  2049  2047 user      |   \_ test-daemon1
     2050  2047  2047 user      \_ supervise test-service2
     2051  2050  2047 user          \_ test-daemon2
    ...

** Important**\
Since processes in a supervision tree are created using the POSIX `fork()` call, all of them will inherit [svscan]\'s enviroment, which, in the context of this example, is the user\'s login shell environment. If [svscan] is launched in some other way (see later), the environment will likely be completely different. This must be taken into account when trying to debug a supervision tree with an interactive shell.

### [][The start, stop and notify files, and the daemontools-encore extended service state]

Daemontools-encore service directories can contain executable files named [start], [stop] and [notify]. The [run] file is optional for daemontools-encore, but either [start] or [run] must exist in the servicedir. If there is a [start] file and it is executable, it will be executed as a child process instead of [run] when [supervise] is invoked, and also when an [svc -u] or [svc -o] command is used to manually start the service (see [controlling supervised processes](#controlling)). If the [start] process exits with a an exit code of 0, [supervise] will then execute the [run] file just like Bernstein daemontools\' [supervise]. [start] can be used to perform some kind of first time-only initialization for the program intended to be supervised.

If the supervised process exits with an exit code of **100**, or if the [start] process is killed by a signal or exits with a nonzero exit code, [supervise] enters the *failed* extended state (see later) and does not restart the service. If the service is manually stopped with an [svc -d] command or, after an [svc -o] command is used, the supervised or [start] process terminated and the conditions for entering the failed state are not met, [supervise] enters the *stopped* extended state. In stopped state, if there is a [stop] file in the servicedir and it is executable, [supervise] will execute it as a child process. [stop] can be used to perform some kind of last time-only cleanup for the program intended to be supervised, or for the [start] process. If the [stop] process exits with an exit code of **100**, [supervise] will also enter the failed state, otherwise it will remain in stopped state.

If there is a [notify] file, [supervise] will execute it as a child process each time a [start], [run] or [stop] process is spawned or terminates for whatever reason, so it can be used to perfom some action after one or more of those events. [supervise] invokes [notify] with four arguments: the first one is either **start**, **run** or **stop**, indicating which process caused [notify] to be invoked (or **log** [in certain cases](#logging)), the second one is either **start**, **exit** or **killed**, indicating that the corresponding process was spawned, exited or was killed by a signal, respectively, the third one is the process ID of the corresponding process, and the fourth one is the exit code or signal number, as determined by POSIX `waitpid()`, or **0** if the second argument is **start**. So, for example, [notify] could be used to perfom cleanup actions each time the supervised process terminates, possibly depending on its exit status information, by checking that its first argument is **run** and its second argument is other than **start**, behaving like a [runit](https://wiki.gentoo.org/wiki/Runit "Runit") or [s6](https://wiki.gentoo.org/wiki/S6 "S6") [finish] file.

The effect of the [no-setsid] file applies to all [start], [stop], [run] and [notify] processes.

Because Bernstein daemontools\' [supervise] only executes a [run] file, the corresponding service can only be in two states: **up** if [supervise] has a child process, or **down** if it doesn\'t. Daemontools-encore\'s [supervise], on the other hand, can have at any given time either a [start], [run], [stop] or [notify] child process, so for compatibility with Bernstein daemontools, when the service state is queried with the [svstat] program (see [controlling supervised processes](#controlling)), an up or down state will still be displayed, but also an additional *extended* state: **starting**, **started**, **running**, **stopping**, **stopped** or **failed**.

-   Extended state *starting* will be displayed after [supervise] launches a [start] process.
-   Extended state *started* will be displayed after the [start] process exits successfully, if there is no [run] file. In started state, [supervise] does nothing but wait for commands sent with the [svc] program.
-   Extended state *running* will be displayed after [supervise] launches a [run] process.
-   Extended state *stopping* will be displayed after [supervise] sends its child process a `SIGTERM` signal followed by a `SIGCONT` signal to make it stop, until the process dies.
-   Otherwise, either extended state *stopped* or extended state *failed* will be displayed. In failed state, or in stopped state after the [stop] process has exited, [supervise] does nothing but wait for commands sent with the [svc] program.

Whether a [notify] process is currently running or not does not modify the service state, it will be whatever it was immediatly before [notify] was executed.

Service directories using [down], [start], [stop] and [notify] files:

`user `[`$`]`ls -l`

    total 8
    drwxr-xr-x 3 user user 4096 May  6 12:00 test-service1
    drwxr-xr-x 3 user user 4096 May  6 12:00 test-service2

`user `[`$`]`ls -l *`

    test-service1:
    total 4
    -rw-r--r-- 1 user user  0 May  6 12:00 down
    -rwxr-xr-x 1 user user 28 May  6 12:00 run

    test-service2:
    total 16
    -rwxr-xr-x 1 user user 163 May  6 12:00 notify
    -rwxr-xr-x 1 user user  24 May  6 12:00 run
    -rwxr-xr-x 1 user user  24 May  6 12:00 start
    -rwxr-xr-x 1 user user  24 May  6 12:00 stop

[FILE] **`test-service1/run`**

    #!/bin/sh
    exec test-daemon1

[FILE] **`test-service2/run`**

    #!/bin/sh
    exec sleep 20

[FILE] **`test-service2/start`**

    #!/bin/sh
    exec sleep 10

[FILE] **`test-service2/stop`**

    #!/bin/sh
    exec sleep 10

[FILE] **`test-service2/notify`**

    #!/bin/sh
    case $2 in
    start) echo "'$1' started (PID $3)";;
    exit) echo "'$1' (PID $3) exited with $4";;
    killed) echo "'$1' (PID $3) was killed by signal $4";;
    esac

Resulting supervision tree:

`user `[`$`]`ps xf -o pid,ppid,pgrp,euser,args`

      PID  PPID  PGRP EUSER    COMMAND
    ...
     1777  1764  1777 user -bash
     2114  1777  2114 user  \_ svscan
     2115  2114  2114 user      \_ supervise test-service1
     2116  2114  2114 user      \_ supervise test-service2
     2146  2116  2146 user          \_ sleep 20
    ...

Note that since [test-service1] has a [down] file, the corresponding [supervise] process has no children.

Messages printed to [svscan]\'s standard output (stdout) by the [notify] script:

`user `[`$`]`svscan scan &`

    'start' started (PID 2253)
    'start' (PID 2253) exited with 0
    'run' started (PID 2258)
    'run' (PID 2258) exited with 0
    'run' started (PID 2287)

Sending a `SIGTERM` signal to the [run] process (PID 2287):

`user `[`$`]`kill 2287`

    'run' (PID 2287) was killed by signal 15
    'run' started (PID 2295)

Manually stopping service *test-service2*:

`user `[`$`]`svc -d scan/test-service2`

    'run' (PID 2295) was killed by signal 15
    'stop' started (PID 2300)
    'stop' (PID 2300) exited with 0

### [Logging]

#### [The multilog program]

If a servicedir **S** in the scan directory contains a subdirectory or symbolic link to directory named [log], [svscan] will launch two [supervise] processes in parallel, one executing **S**[/run] as a child process, and the other executing **S**[/log/run] with its standard input (stdin) connected to **S**[/run]\'s standard output (stdout) by a pipe. If any of the two processes or their [supervise] parents terminates and is restarted, the same pipe is reused so that no data is lost. This allows per-service logging by having **S**[/log/run] execute a *logger program*. Bernstein daemontools and daemontools-encore provide such a logger: the [multilog] program. This type of logging works for programs that send messages to their standard error (stderr).

Daemontools-encore\'s [supervise] allows [log] to be an *executable file* instead of subdirectory or symlink to directory. In this case, the same [supervise] process will supervise both the \'main\' service and the logger, and maintain the pipe between then. This is similar to having a subdirectory with a [run] file equivalent to the [log] file, and no [start] or [stop] files. The [notify] file of the \'main\' service will be invoked with **log** as its first argument when the [log] process starts, exits or gets killed by a signal. The [down] and [no-setsid] files of the \'main\' service also apply to the [log] process in this case.

[multilog] is invoked as [multilog arg1 arg2 arg3 \...], and expects to read a sequence of newline-terminated lines of text from its standard input. The arguments *arg1*, *arg2*, *arg3*, \... make up a *logging script* that tells [multilog] what to do. Each argument specifies an *action*, actions are carried out sequentially in argument order.

The simplest form of [multilog] invocation is [multilog dir], where *dir* starts with a dot (\'.\') or a slash (\'/\'): it is interpreted as a pathname specifying an automatically rotated *logging directory* (or *logdir*). The logdir contains control files used by [multilog], a *current log file* named [current], and may also contain a set of old log files. The current log file contains a selection of the lines read by [multilog], possibly modified by other actions specified in the logging script, and old log files are produced by *rotations*: when [current] approaches a certain maximum size, its contents are copied to a another file, after some optional processing, and [current] is emptied. Old log file have names beginning with \'@\', continuing with a timestamp in [external TAI64N format](https://cr.yp.to/libtai/tai64.html) showing when the file was finished, and ending with either **.s** or **.u**. The .s files are files that have been completely processed and safely written, i.e. files produced by a complete rotation. The .u files, if any, are files created by an incomplete rotation, they are not completely processed and may be truncated. Rotations respect line boundaries, i.e. old log files will always contain whole lines. Also, to avoid indefinite accumulation of old log files, if, after completing a rotation, their number exceeds a certain value, [multilog] deletes the oldest log file (the file with the smallest TAI64N timestamp). The default maximum size of a [current] file is 99999 bytes, and the default maximum number of old log files is 10. A rotation can be forced by sending [multilog] a `SIGALRM` signal. If it is running as a supervised process, the [svc] program can be used to do that (see [controlling supervised processes](#controlling)).

Some other actions recognized by [multilog] in a logging script are:

-   **+** (plus sign) and **-** (minus sign) followed by a *pattern*: By default, [multilog] logs all the lines read from its standard input without modifications; these actions allow selection and deselection of lines, respectively, based on the specified pattern. Because all lines are initially selected, **+** actions are only effective after a **-** action that deselects some lines first. The pattern uses the shell\'s notation for matching strings, and must match whole lines (i.e. partial matching doesn\'t count), with the following restrictions:
    -   Berstein daemontools\' [multilog] only treats asterisks (\'\*\') as special characters in the pattern: they match any string, including the null string, that does not include the next character in pattern instead of the POSIX behaviour of matching the greatest possible number of characters that still allows the remainder of the pattern to match the line, and cannot be escaped with a backslash (\'\\\').
    -   Daemontools-encore\'s [multilog] can switch between Bernstein daemontools behaviour and using the full range of patterns allowed by POSIX `fnmatch()`, including backslash escaping. The latter is more flexible at the expense of being less efficient. At the start of logging script action processing, Bernstein daemontools match mode is selected.
        -   An **F** action selects `fnmatch()` match mode for all subsequent **+** and **-** actions until the next mode-changing action in the logging script.
        -   An **S** action selects Bernstein daemontools match mode for all subsequent **+** and **-** actions until the next mode-changing action in the logging script.
-   **t**: prepends each logged line with \'@\', followed by a timestamp in [external TAI64N format](https://cr.yp.to/libtai/tai64.html) (printed as 24 lowercase hexadecimal characters), and a space. It must be specified as the first action, and any subsequent **+** and **-** actions match against lines **with** the prepended timesptamp. Daemontools-encore also supports a **T** action, which must also be the first one, that prepends an accustamp-style timestamp and a space instead ([accustamp] was a program shipped with Bernstein daemontools that was eventually dropped).
-   **s** followed by an integer: sets the maximum size of the [current] file to the specified value (in bytes), for all subsequent actions in the logging script that specify a logdir, until the next **s** action.
-   **n** followed by an integer: sets the maximum number of old log files to the specified value, for all subsequent actions in the logging script that specify a logdir, until the next **n** action.
-   **!** (exclamation mark) followed by a string *args*: sets a *processor* for all subsequent actions in the logging script that specify a logdir, until the next **!** action. A processor allows performing some processing of the contents of [current] log files during a rotation; [multilog] performs the equivalent of an [sh -c \'args\'] command for every logdir, and feeds the resulting processes the contents of their corresponding [current] file on its standard input, so *args* should specify a program and its arguments, if any. The .s or .u file produced as a result will contain that program\'s output. For example, a [multilog \'!processor-script arg1 arg2\' ./dirname] command makes [multilog] launch a processor with the equivalent of a [sh -c \'processor-script arg1 arg2\'] command during a rotation on logdir [dirname] in [multilog]\'s working directory. If an executable file named [processor-script] is found via `PATH` search, this will invoke it with arguments `arg1 arg2` and feed it the contents of [dirname/current] on its standard input.

For details about all actions supported [multilog], and about the protocol used for communication between [multilog] and the processor specified in an **!** action, please consult the [multilog] man page.

[FILE] **`input`Sample input for the [multilog] program**

    info: Message 1
    warning: Message 2
    error: Message 3
    error: Message 4
    warning: Message 5
    info: Message 6

`user `[`$`]`cat input | multilog '-*' '+warning: *' ./log1 '+error: *' ./log2`

`user `[`$`]`ls -l`

    drwx------ 2 user user 4096 May  6 12:00 log1
    drwx------ 2 user user 4096 May  6 12:00 log2

`user `[`$`]`ls -l log*`

    log1:
    total 4
    -rwxr--r-- 1 user user 38 May  6 12:00 current
    -rw------- 1 user user  0 May  6 12:00 lock
    -rw-r--r-- 1 user user  0 May  6 12:00 state

    log2:
    total 4
    -rwxr--r-- 1 user user 72 May  6 12:00 current
    -rw------- 1 user user  0 May  6 12:00 lock
    -rw-r--r-- 1 user user  0 May  6 12:00 state

When there\'s no [multilog] process running on a logdir, the [current] file has the executable by user flag set.

[FILE] **`log1/current`**

    warning: Message 2
    warning: Message 5

[FILE] **`log2/current`**

    warning: Message 2
    error: Message 3
    error: Message 4
    warning: Message 5

Note that the [log2/current] file also contains the warning messages. This shows that actions that aren\'t **+** or **-** do not affect the currently selected lines, so warning messages selected by action \'+warning: \*\' stay selected after processing action \'./log1\'. To only have the error messages in [log2/current], a \'-\*\' action should have immediatly preceded the \'+error: \*\' action.

Service directory [test-service] containing a logger:

`user `[`$`]`ls -l`

    total 8
    drwxr-xr-x 2 user user 4096 May  6 12:00 log
    -rwxr-xr-x 1 user user  110 May  6 12:00 run

`user `[`$`]`ls -l log`

    total 4
    -rwxr-xr-x 1 user user 40 May  6 12:00 run

[FILE] **`/home/user/test-daemon`Python script generating messages on its stderr**

    #!/usr/bin/python3
    from time import sleep
    from sys import stderr
    for i in range(1,30):
       print("Message", i, file=stderr, flush=True)
       sleep(2)

[FILE] **`test-service/run`**

    #!/bin/sh
    exec /home/user/test-daemon 2>&1

[FILE] **`test-service/log/run`**

    #!/bin/sh
    exec multilog t ../../../logs

Note that since [supervise] makes the service directory its working directory, the relative pathname in [multilog]\'s invocation results in the logging directory being placed wherever the scan directory is.

Resulting supervision tree:

`user `[`$`]`ps xf -o pid,ppid,pgrp,euser,args`

      PID  PPID  PGRP EUSER    COMMAND
    ...
     1777  1764  1777 user -bash
     2702  1777  2702 user  \_ svscan
     2703  2702  2702 user      \_ supervise test-service
     2706  2703  2702 user      |   \_ /usr/lib/python-exec/python3.6/python3 /home/user/test-daemon
     2704  2702  2702 user      \_ supervise log
     2705  2704  2702 user          \_ multilog t ../../../logs
    ...

Contents of the [logs] logging directory:

`user `[`$`]`ls -l ../logs`

    total 20
    -rwxr--r-- 1 user user  361 May  6 17:20 @40000000590e2ffe0bf16944.s
    -rwxr--r-- 1 user user 2202 May  6 17:22 @40000000590e30941e642c9c.s
    -rw-r--r-- 1 user user 1101 May  6 17:23 current
    -rw------- 1 user user    0 May  6 17:19 lock
    -rw-r--r-- 1 user user    0 May  6 17:19 state

This logdir contains two old log files and, since [multilog] is running, the [current] file has its executable by user flag cleared.

`user `[`$`]`cat ../logs/current`

    @40000000590e30983973bda4 Message 1
    @40000000590e309a39b02a64 Message 2
    @40000000590e309c3a353ccc Message 3
    @40000000590e309e3a93b84c Message 4
    @40000000590e30a03aec8a94 Message 5
    @40000000590e30a23b3bbc04 Message 6
    @40000000590e30a5003a28ac Message 7
    @40000000590e30a70097255c Message 8
    @40000000590e30a900bc221c Message 9
    @40000000590e30ab0100ff04 Message 10

The TAI64N timestamps can be shown in human-readable form with [tai64nlocal], for further details please consult the respective man page.

`user `[`$`]`cat ../logs/current | tai64nlocal`

    2017-05-06 17:22:38.963886500 Message 1
    2017-05-06 17:22:40.967846500 Message 2
    2017-05-06 17:22:42.976567500 Message 3
    2017-05-06 17:22:44.982759500 Message 4
    2017-05-06 17:22:46.988580500 Message 5
    2017-05-06 17:22:48.993770500 Message 6
    2017-05-06 17:22:51.003811500 Message 7
    2017-05-06 17:22:53.009905500 Message 8
    2017-05-06 17:22:55.012329500 Message 9
    2017-05-06 17:22:57.016842500 Message 10

#### [The readproctitle program]

The [readproctitle] program expects to read a sequence of newline-terminated lines of text from its standard input, and saves them to an automatically rotated log it keeps in *memory*. The log can be seen in the output of the [ps] utility. The number of characters displayed is specified by [readproctitle]\'s arguments.

[readproctitle] is invoked as [readproctitle arg1 arg2 \... argn dots]. The arguments *arg1*, *arg2*, \..., *argn* can be anything, they are shown as-is in the output of [ps], and can used for displaying some kind of heading that introduces the log. The last argument, *dots*, must be at least five dots (\'.\'), and its length specifies the number of characters the log kept in memory will have. In the output of [ps], [readproctitle]\'s last shown argument will be the contents of the log up to that time instead of *dots*. Characters shift to the left as [readproctitle] reads new lines of text, and older characters are discarded to keep the log of constant size. Therefore, the [ps] utility will show each time the most recent data. For further details, please consult the [readproctitle] man page.

[FILE] **`doit`Shell script generating output**

    #!/bin/sh
    echo Print this message!
    sleep 10
    echo Second message
    sleep 10

`user `[`$`]`./doit | readproctitle Log header: ........................ &`

`user `[`$`]` ps x -o pid,args`

      PID COMMAND
    ...
     2860 readproctitle Log header: ....Print this message!
    ...

After enough seconds have elapsed:

`user `[`$`]`ps x -o pid,args`

      PID COMMAND
    ...
     2860 readproctitle Log header: ...sage! Second message
    ...

The best known use of [readproctitle] is in the [svscanboot] script included in Bernstein daemontools and daemontools-encore.

#### [The logging chain]

A supervision tree where all leaf processes have a logger can be arranged into what the author of [s6](https://wiki.gentoo.org/wiki/S6 "S6") calls *the logging chain* ^[\[5\]](#cite_note-5)^, which he considers to be technically superior to the traditional syslog-based centralized approach ^[\[6\]](#cite_note-6)^.

Since processes in a supervision tree are created using the POSIX `fork()` call, each of them will inherit [svscan]\'s standard input, output and error. A logging chain arrangement using Bernstein daemontools and daemontools-encore is as follows:

-   Leaf processes should normally have a logger, so their standard output and error connect to their logger\'s standard input. Therefore, all their messages are collected and stored in dedicated, per-service logs by their logger. Some programs might need to be invoked with special options to make them send messages to their standard error, and redirection of standard error to standard output (i.e. **2\>&1** in a shell script) must be performed in the servicedir\'s [run] file.
-   Leaf processes with a controlling terminal are an exception: their standard input, output and error connect to the terminal.
-   [supervise], the loggers, and leaf processes that exceptionally don\'t have logger for some reason, inherit their standard input, output and error from [svscan], so their messages are sent wherever the ones from [svscan] are.
-   Leaf processes that still unavoidably report their messages using `syslog()` have them collected and logged by a (possibly supervised) syslog server.

#### [Specifying a logger for [svscan]]

Daemontools-encore\'s [svscan] allows the pathname of a service directory to be passed as a second argument after the scan directory\'s pathname. If this argument is present, [svscan] will launch one [supervise] process for the specified directory, and connect its standard output and error to the corresponding supervised process\' standard input by a pipe. This makes it possible to set up a logger for [svscan] in the same way a logger can be set up for the leaf processes of the supervision tree.

** Note**\
If the service directory of [svscan]\'s logger is specified as a relative pathname, it is interpreted as relative to the scan directory

### [Supervised process execution state changes]

Bernstein\'s daemontools and daemontools-encore provide a set of tools for modifying a supervised process\' execution state. These tools employ a technique called *chain loading* by some people, and *Bernstein chaining* by others. A program *prog1* designed to use chain loading is invoked as [prog1 arg11 \... arg1n prog2 arg21 \... arg2n], where *prog2* is the name of another program. When *prog1* is invoked, it performs some action based on arguments *arg11*, \..., *arg1n*, and then executes *prog2* without creating a new process, using one of the POSIX `exec...()` calls. Arguments *arg21*, \..., *arg2n* are not interpreted by *prog1* and are passed along to *prog2*.

If *prog2* is also designed to use chain loading, some of those arguments might in turn be the name of a third program *prog3* and its corresponding arguments, which will be executed after *prog2* completes its task. As a consequence, it is possible to build a chain of programs that will run one after the other as a single process, therefore preserving the process ID (PID), which makes the technique suitable for the [run] script of a service directory. The final one in such a chain of programs would be the real program intended to be supervised.

The tools provided by Bernstein\'s daemontools and daemontools-encore to change a process\' execution state are:

-   [envdir]: runs another program with environment modified according to files in a specified directory.
-   [envuidgid]: runs another program with environment variables indicating a specified account\'s user ID and group ID
-   [pgrphack]: runs a program in a new session (using POSIX `setsid()`).
-   [setlock]: runs another program with a file locked (using Linux `flock()` on Gentoo).
-   [setuidgid]: runs another program under a specified account\'s user ID and group ID. Requires root privileges.
-   [softlimit]: runs another program with new soft resource limits (using POSIX `setrlimit()`). These limits are set via options specified as [softlimit]\'s arguments. Daemontools-encore also allows setting those limits via `SOFTLIMIT_*` environment variables, applied at [softlimit] invocation; see [environment variables](#Environment_variables).

For further details on these tools please consult their respective man page.

The directory supplied to the [envdir] program is called an *environment directory* (or *envdir*). Each file in the envdir controls a single environment variable. If the file is empty, and a variable with the same name as the file exists in the process\' environment, it is removed from it. If the file is nonempty, the contents of its first line become the value of a new environment variable with the same name as the file. If the variable existed before [envdir]\'s invocation, it is first removed from the environment, and then readded with the new value. Enviroment variables not referred to by a file in the envdir remain unchanged.

[FILE] **`run`Example *run* script with process state change**

    #!/bin/sh
    exec \
    softlimit -o 5 \
    setuidgid daemon \
    test-daemon 2>&1

This script executes program [test-daemon] with effective user *daemon* and the maximum number of open file descriptors set to 5. This is the same as if [test-daemon] performed a `setrlimit(RLIMIT_NOFILE, &rl)` call itself with `rl.rlim_cur` set to 5, provided that value does not exceed the corresponding hard limit. As in previous examples, the redirection of stderr to stdout allows setting up a dedicated logger for [test-daemon].

Example service directory with an enviroment directory [env]:

`user `[`$`]`ls -l`

    total 8
    drwxr-xr-x 2 root root 4096 May  7 12:00 env
    -rwxr-xr-x 1 root root  125 May  7 12:00 run

`user `[`$`]`ls -l env`

    total 4
    -rw-r--r-- 1 root root 2 May  7 12:00 SOFTLIMIT_OPENFILES

[FILE] **`run`**

    #!/bin/sh
    exec \
    envdir env \
    envuidgid daemon \
    softlimit \
    test-daemon 2>&1

[FILE] **`env/SOFTLIMIT_OPENFILES`**

    5

This script adds variables `UID`, `GID` and `SOFTLIMIT_OPENFILES` to [test-daemon]\'s environment, the first two set to the user ID and group ID of account *daemon* via [envuidgid], and the last one via the enviroment directory [env], which is used by the [softlimit] invocation to set the maximum number of open file descriptors to 5, provided it is the daemontools-encore version of that program. Environment variables `UID` and `GID` could be used by [test-daemon] to drop privileges.

### [Controlling supervised processes]

Bernstein daemontools and daemontools-encore provide two programs for controlling a supervised process and to query status information about it: [svc] and [svstat], respectively.

The [svc] program accepts a set of service directory pathnames and options that specify what to do. Some of these options are:

-   `-d` (*down*): If the supervised process is running, send it a `SIGTERM` signal followed by a `SIGCONT` signal. The [run] file won\'t be reexecuted after that, and, for daemontools-encore, the [stop] file will be executed, if present. This is the standard way to manually stop a supervised process. If the process is not running (e.g. because it has a [down] file or after a previous [svc -d] command) this is a no operation.
-   `-u` (*up*): If the supervised process is not running, start it by executing its [run] file, or, for daemontools-encore, its [start] file, if present. If the process is running, this is mostly a no operation, except that it cancels the effect of a previous [svc -o] command. This is the standard way to manually start a supervised process that has a [down] file, or that has been previously stopped with an [svc -d] command.
-   `-o` (*once*): If the supervised process is not running, start it by executing its [run] file, or, for daemontools-encore, its [start] file, if present, but don\'t restart it if terminates. This still allows the process to be monitored and to be reliably sent signals, but it won\'t actually be supervised. If the process is running, just ask [supervise] to not restart it if it terminates. The effect of this option can be cancelled by a subsequent [svc -u] command, and restored by another [svc -o] command.
-   `-x` (*exit*): Asks [supervise] to exit if the supervised process terminates. This is mostly useful for tearing down a supervision tree: after sending [svscan] a `SIGTERM`, an [svc -dx \$/\*] command can terminate all supervised processes, because of the `-d` option, and make their [supervise] parents exit afterwards, because of the `-x` option. If an [svc -dx] command is used when [svscan] is still running, after the servicedir\'s [supervise] process exits, it will just be restarted on [svscan]\'s next periodic scan.

Other [svc] options allow reliably sending signals to a supervised process. For further details, please consult the [svc] man page. In particular, [svc -a] be used to send a `SIGALRM` signal to a supervised [multilog] process to force it to perform a rotation.

The [svstat] program accepts a set of service directory pathnames. Its output is intended to be displayed on a user interface or logged, not to be fed as input to a program for parsing. It displays whether the supervised process is running (\'up\') or not (\'down\'), its process ID (PID) if it is up, how long it has been in the current state, whether its current up or down status matches the presence or absence of a [down] file in the servicedir (\'normally up\' or \'normally down\'), and whether it is transitioning to the desired state or already there (\'want up\' or \'want down\'). The daemontools-encore version also displays the service\'s extended state (see [the start, stop and notify files, and the daemontools-encore extended service state](#startstopnotify)), and if there is a [log] executable file, it will print a second line of output with information about the logger process. If an `-l` option is passed [svstat], the information about the logger process will be suppressed from the output, and if an `-L` option is passed to [svstat], *only* information about the logger process will be displayed, or the message \'no log service\' if the servicedir has no [log] executable file. For further details, please consult the [svstat] man page.

Bernstein daemontools and daemontools-encore also provide the [svok] program, that accepts a service directory pathname, and exits with an exit code of 0 if there is a [supervise] process successfully running for that directory, and an exit code of **100** if there isn\'t. It produces no output if no error was encountered, otherwise it displays an error message and exits with an exit code of **111**. Finally, daemontools-encore provides the [svup] program, that accepts a service directory pathname, and exits with an exit code of 0 if there is a [supervise] process successfully running for that directory and the service\'s extended state is either **started** or **running**, and an exit code of **100** if the service is in any other state, or if there is no [supervise] process. It produces no output if no error was encountered, otherwise it displays an error message and exits with an exit code of **111**. If there is a [log] executable file, [svup] exits with an exit code of 0 only if *both* the \'main\' service and the logger are in started or running state. If an `-l` option is passed to [svup], only the \'main\' service will be checked, and if an `-L` option is passed to [svup], only the logger will be checked (and the exit code will be **100** if the servicedir has no [log] executable file). For further details about [svok] and [svup], please consult their respective man page.

** Important**\
For the operation performed by [svc] to be allowed, its effective user must have write access to the [supervise/control] FIFO in the service directory, otherwise, it will fail with an \"access denied\" error. For the operation performed by [svstat] and [svup] to be allowed, its effective user must have write access to the [supervise/ok] FIFO and read access to the [supervise/status] file in the service directory, otherwise, it will fail with an \"access denied\" error. Using [svc] or [svstat] on a service directory for which no [supervise] process is running will result in a \"supervise not running\" error.

Service directories with a [log] subdirectory and a [log] executable file:

`user `[`$`]`ls -l`

    total 8
    drwxr-xr-x 3 user user 4096 Jan 28 12:00 test-service1
    drwxr-xr-x 2 user user 4096 Jan 28 12:00 test-service2

`user `[`$`]`ls -l * test-service1/log`

    test-service1:
    total 8
    drwxr-xr-x 2 user user 4096 Jan 28 12:00 log
    -rwxr-xr-x 1 user user   32 Jan 28 12:00 run

    test-service1/log:
    total 4
    -rwxr-xr-x 1 user user 41 Jan 28 12:00 run

    test-service2:
    total 8
    -rwxr-xr-x 1 user user 38 Jan 28 12:00 log
    -rwxr-xr-x 1 user user 32 Jan 28 12:00 run

[FILE] **`test-service1/run`**

    #!/bin/sh
    exec test-daemon 2>&1

[FILE] **`test-service1/log/run`**

    #!/bin/sh
    exec multilog ../../../logdir1

[FILE] **`test-service2/run`**

    #!/bin/sh
    exec test-daemon 2>&1

[FILE] **`test-service2/log`**

    #!/bin/sh
    exec multilog ../../logdir2

Resulting supervision tree:

`user `[`$`]`ps xf -o pid,ppid,pgrp,euser,args`

     PID  PPID  PGRP EUSER    COMMAND
    ...
    2284  2122  2284 user     -bash
    2353  2284  2353 user      \_ svscan
    2354  2353  2353 user          \_ supervise test-service1
    2357  2354  2357 user          |   \_ test-daemon
    2355  2353  2353 user          \_ supervise log
    2359  2355  2359 user          |   \_ multilog ../../../logdir1
    2356  2353  2353 user          \_ supervise test-service2
    2358  2356  2358 user              \_ multilog ../../logdir2
    2360  2356  2360 user              \_ test-daemon
    ...

Note that there are separate [supervise] processes (with PIDs 2354 and 2355) for *test-service1* and its logger, but a single [supervise] process (with PID 2356) supervising both *test-service2* and its logger.

`user `[`$`]`svstat *`

    test-service1: up (pid 2357) 157 seconds, running
    test-service2: up (pid 2360) 156 seconds, running
    test-service2 log: up (pid 2358) 157 seconds, running

`user `[`$`]`svstat -l *`

    test-service1: up (pid 2357) 170 seconds, running
    test-service2: up (pid 2360) 169 seconds, running

`user `[`$`]`svstat -L *`

    test-service1: no log service
    test-service2 log: up (pid 2358) 182 seconds, running

To get the status of the [test-service1]\'s logger, the pathname of the corresponding [log] subdirectory must be specified to [svstat]:

`user `[`$`]`svstat test-service1/log`

    test-service1/log: up (pid 2359) 241 seconds, running

### [Starting the supervision tree]

In a supervision tree arrangement each process supervises its children, therefore the robustness of the supervision tree ultimately relies on the [svscan] process. So the problem of how to supervise [svscan] itself arises, as well as what to do with [svscan]\'s messages in a [logging chain](#loggingchain).

#### [From OpenRC]

Gentoo\'s packaging of Bernstein daemontools and daemontools-encore provides an [OpenRC](https://wiki.gentoo.org/wiki/OpenRC "OpenRC") service script for running [svscan], also named [svscan]. If this service script is used, the scan directory will be [/service]. Thus, [svscan] can be started when the machine boots by adding it to an OpenRC runlevel using [rc-update]:

`root `[`#`]`rc-update add svscan default`

Or it can also be started manually:

`root `[`#`]`rc-service svscan start`

** Warning**\
The service script launches [svscan] using OpenRC\'s [start-stop-daemon] program, so it will run unsupervised, and with its standard output and error redirected to [/dev/null] by default, so supervision tree messages other than those from leaf processes that have a dedicated logger will be lost.

#### [The svscanboot script]

Bernstein daemontools and daemontools-encore provide a script called [scvscanboot], that can be spawned and supervised by [sysvinit](https://wiki.gentoo.org/wiki/Sysvinit "Sysvinit") ([[[sys-apps/sysvinit]](https://packages.gentoo.org/packages/sys-apps/sysvinit)[]]) by adding a `respawn` line for it in [/etc/inittab]. [scvscanboot] is a shell script that launches an [svscan] process and a [readproctitle] process, with the former\'s standard output connected to the latter\'s standard input by a pipe, and every other standard descriptor redirected to [/dev/null]. The enviroment will be empty, except for the `PATH` variable, set to a known value in the script. The scan directory will be [/service].

Used in this way, the supervision tree becomes rooted in process 1, which cannot die without crashing the machine. Also, [svscan]\'s messages will go to [readproctitle], so they can be seen using the [ps] utility.

Gentoo users wanting to use [svscanboot] will need to manually edit [/etc/inittab], and then call [telinit]

[FILE] **`/etc/inittab`**

    SV:12345:respawn:/usr/bin/svscanboot

`root `[`#`]`telinit q`

This will run [svscanboot] when entering [runlevels](https://wiki.gentoo.org/wiki/Sysvinit#runlevels "Sysvinit") 1 to 5. Because [svscanboot] calls [svc] using absolute path [/command/svc], a symlink to the correct path for Gentoo must be created:

`root `[`#`]`mkdir -p /command`

`root `[`#`]`ln -s /usr/bin/svc /command/svc`

#### [The supervise-scripts package]

Bruce Guenter\'s supervise-scripts package ([[[sys-process/supervise-scripts]](https://packages.gentoo.org/packages/sys-process/supervise-scripts)[]]) provides an [svscan-add-to-inittab] script that also allows sysvinit to launch and supervise [svscan]. The script will make a backup of [/etc/inittab] (with a name of the form [/etc/inittab-YYYY-MM-DD]) and then modify it so that another script, [svscan-start] is run when entering runlevels 1 to 5.

`root `[`#`]`svscan-add-to-inittab`

`root `[`#`]`telinit q`

The [svscan-start] script is a wrapper around [svscan]. After some initialization it will replace itself with [svscan] using the shell\'s [exec] builtin utility, with its standard input, output and error redirected to [/dev/console]. Therefore, [svscan]\'s messages will be shown on the console. The enviroment will be empty, except for the `PATH` variable, set to a known value in the script. The scan directory will be [/service].

The package also includes an [svscan-stopall] script, that will be called when entering sysvinit\'s [single user mode](https://wiki.gentoo.org/wiki/Sysvinit#singleuser "Sysvinit") or runlevels 0, 1 and 6, to perform cleanup. It will stop all lingering [supervise] processes and their children using an [svc -dx] command.

## [Removal]

### [Unmerge]

`root `[`#`]`emerge --ask --depclean --verbose sys-process/daemontools-encore`

All scan directories, service directories, the [/command/svc] symlink, etc. must be manually deleted if no longer wanted after removing the package. Also, all modifications to [/etc/inittab] must be manually reverted, even when using the supervise-scripts package, because [svscan-add-to-inittab] does not have an \'undo\' option. Lines for [svscanboot], [svscan-start] and [svscan-stopall] must be deleted, and a [telinit q] command must be used afterwards. If no further changes to [/etc/inittab] have been made after invoking [svscan-add-to-inittab], the backup copy created by that script before the changes are applied can be used to revert them by just replacing [/etc/inittab] with that file.

## [See also]

-   [Daemontools](https://wiki.gentoo.org/wiki/Daemontools "Daemontools") --- a collection of tools for managing UNIX services
-   [Runit](https://wiki.gentoo.org/wiki/Runit "Runit") --- lightweight process supervision suite, originally inspired by [daemontools](https://wiki.gentoo.org/wiki/Daemontools "Daemontools") that offers fast and reliable service management.
-   [S6](https://wiki.gentoo.org/wiki/S6 "S6") --- a package that provides a [daemontools-inspired](https://wiki.gentoo.org/wiki/Daemontools "Daemontools") process supervision suite, a notification framework, a UNIX domain super-server, and tools for file descriptor holding and suidless privilege gain.
-   [Process supervision](https://wiki.gentoo.org/wiki/Process_supervision "Process supervision") --- the ability to manage (long lived) processes or rather *daemons* and be able to get (automated) process restart if needed

## [External Resources]

-   [Tokiclover\'s supervision framework (OpenRC friendly)](https://github.com/tokiclover/supervision)
-   [Avery Payne\'s supervision-scripts project](https://bitbucket.org/avery_payne/supervision-scripts/)

## [References]

1.  [[[↑](#cite_ref-1)] [D. J. Bernstein, [daemontools FAQ](https://cr.yp.to/daemontools/faq/create.html#why), which includes one about the benefits of process supervision. Retrieved on April 23rd, 2017.]]
2.  [[[↑](#cite_ref-2)] [Gerrit Pape, [runit benefits](http://smarden.org/runit/benefits.html), which includes a short description of process supervision in general. Retrieved on April 23rd, 2017.]]
3.  [[[↑](#cite_ref-3)] [Laurent Bercot, [s6 overview](https://www.skarnet.org/software/s6/overview.html), which contains an introduction to process supervision. Retrieved on April 23rd, 2017.]]
4.  [[[↑](#cite_ref-4)] [Jonathan de Boyne Pollard, [Mistakes to avoid when designing Unix dæmon programs](https://jdebp.eu/FGA/unix-daemon-design-mistakes-to-avoid.html). Retrieved on May 5th, 2017.]]
5.  [[[↑](#cite_ref-5)] [Laurent Bercot, [the logging chain](https://www.skarnet.org/software/s6/s6-log.html#loggingchain), Retrieved on May 1st, 2017.]]
6.  [[[↑](#cite_ref-6)] [Laurent Bercot, [on the syslog design](https://www.skarnet.org/software/s6/s6-log.html#diesyslogdiedie), Retrieved on May 1st, 2017.]]