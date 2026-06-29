**Resources**

[[]][Home](https://savannah.nongnu.org/projects/sysvinit)

[[]][Git repository browser](https://git.savannah.nongnu.org/cgit/sysvinit.git)

[[]][Package information](https://packages.gentoo.org/packages/sys-apps/sysvinit)

[[]][Wikipedia](https://en.wikipedia.org/wiki/Init#SysV-style "wikipedia:Init")

sysvinit is a collection of System V-style init programs originally written by Miquel van Smoorenburg. They include [init], which is run by the kernel as process 1, and is the parent of all other processes. On Gentoo, it is a component of one of its two supported init systems, with the [OpenRC](https://wiki.gentoo.org/wiki/OpenRC "OpenRC") service manager on top of it to implement the [rc subsystem](https://wiki.gentoo.org/wiki/Rc "Rc").

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
-   [[2] [Configuration]](#Configuration)
    -   [[2.1] [Environment variables]](#Environment_variables)
    -   [[2.2] [Files]](#Files)
-   [[3] [Usage]](#Usage)
    -   [[3.1] [init and telinit]](#init_and_telinit)
        -   [[3.1.1] [The inittab file]](#The_inittab_file)
        -   [[3.1.2] [The boot sequence]](#The_boot_sequence)
        -   [[3.1.3] [Runlevels]](#Runlevels)
        -   [[3.1.4] [Ondemand procedures]](#Ondemand_procedures)
        -   [[3.1.5] [Single user mode]](#Single_user_mode)
        -   [[3.1.6] [Signal processing]](#Signal_processing)
        -   [[3.1.7] [init re-execution]](#init_re-execution)
    -   [[3.2] [Shutdown and reboot]](#Shutdown_and_reboot)
        -   [[3.2.1] [halt, poweroff, and reboot]](#halt.2C_poweroff.2C_and_reboot)
        -   [[3.2.2] [shutdown]](#shutdown)
    -   [[3.3] [bootlogd]](#bootlogd)
    -   [[3.4] [Other utilities]](#Other_utilities)
    -   [[3.5] [Gentoo\'s sysvinit setup]](#Gentoo.27s_sysvinit_setup)
-   [[4] [Removal]](#Removal)
    -   [[4.1] [Unmerge]](#Unmerge)
-   [[5] [See also]](#See_also)

## [Installation]

### [USE flags]

### [USE flags for] [sys-apps/sysvinit](https://packages.gentoo.org/packages/sys-apps/sysvinit) [[]] [/sbin/init - parent of all processes]

  ----------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------
  [`ibm`](https://packages.gentoo.org/useflags/ibm)                 Add support for IBM ppc64 specific systems
  [`nls`](https://packages.gentoo.org/useflags/nls)                 Add Native Language Support (using gettext - GNU locale utilities)
  [`selinux`](https://packages.gentoo.org/useflags/selinux)         !!internal use only!! Security Enhanced Linux support, this must be set by the selinux profile or breakage will occur
  [`static`](https://packages.gentoo.org/useflags/static)           !!do not set this during bootstrap!! Causes binaries to be statically linked instead of dynamically
  [`verify-sig`](https://packages.gentoo.org/useflags/verify-sig)   Verify upstream signatures on distfiles
  ----------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-05-02 00:03] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

** Note**\
If an OpenRC stage3 tarball was used during Gentoo installation, sysvinit will be already present. It is not needed in any normal cases to install sysvinit directly with an [emerge] command. It might be *reinstalled* with an [emerge \--oneshot] command, though, if this is needed for some special reason.

`root `[`#`]`emerge --ask sys-apps/sysvinit`

## [Configuration]

### [Environment variables]

-   `CONSOLE` - Pathname [init] will use as that of machine console\'s device node.

### [Files]

-   [/etc/inittab] - [init]\'s configuration file.
-   [/etc/initscript] - If present, used by [init] to spawn processes specified in its configuration file.
-   [/etc/shutdown.allow] - List of account names used by [shutdown] when invoked with an `-a` option, to decide whether the machine shutdown request should be allowed to proceed or not.
-   [/var/run/powerstatus] (formerly [/etc/powerstatus]) - Used by [init] for its power failure and restoration routines.

## [Usage]

The sysvinit package provides:

-   [init] and its control program, [telinit].
-   The [shutdown], [halt], [poweroff], and [reboot] programs, that shut the machine down if [init] is running as process 1.
-   The [bootlogd] daemon.
-   The [killall5], [runlevel], and [fstab-decode] utilities.

The upstream package provides additional programs, but Gentoo does not install them, in favor of their counterparts from other packages.

### [init and telinit]

[init] is executed by the kernel as process 1. No special administrator intervention is required for this; during the machine\'s boot sequence, the kernel automatically looks for a program named \'init\' in directories [/sbin], [/etc] and [/bin], in that order, unless the `init=` parameter has been specified in its command line (e.g. using the [bootloader](https://wiki.gentoo.org/wiki/Bootloader "Bootloader")\'s available mechanisms).

[init] runs for the entire machine\'s uptime and performs these tasks:

-   Spawns a set of child processes, as specified in its configuration file, [/etc/inittab]. A subset of these processes carry out the machine\'s initialization tasks, needed to bring it to its stable, normal \'up and running\' state, usually by relying on the [rc subsystem](https://wiki.gentoo.org/wiki/Rc "Rc")\'s mechanisms.
-   Reaps zombie child processes using the POSIX `waitpid()` call. Zombie processes are those that have exited or have been killed by a signal, which causes the kernel to send a `SIGCHLD` signal to their parent. The children of [init] include orphaned processes that were reparented to it by the kernel.
-   *Supervises* child processes that have a corresponding [inittab] entry with a `respawn` or `ondemand` action (see [here](#inittab)).
-   Reacts to [received signals](#signals).
-   Reacts to commands received via its control FIFO, [/run/initctl]. [init] creates this FIFO if it doesn\'t already exist, with permissions **0600** (i.e. the [ls -l] command would show `prw-------`). For sysvinit version 2.88, the control FIFO is [/dev/initctl].

[init] prints its messages on the machine\'s console, and also sends messages to a syslog server using the [libc](https://wiki.gentoo.org/wiki/Libc "Libc")\'s implementation (i.e. that of the POSIX `openlog()`, `syslog()` and `closelog()` calls). Each time [init] needs to use the console, it opens the corresponding device node, and closes it after use. If the `CONSOLE` environment variable is set, [init] uses its value as the pathname of the console\'s device node, instead of [/dev/console]. [init]\'s syslog messages specify facility `LOG_DAEMON` and severity `LOG_INFO`.

[inittab] specifies processes to be started by [init] both during the boot sequence, and during normal operation. Processes started during normal operation are assigned to groups named *runlevels*. sysvinit runlevels are identified by a number in the range from 0 to 9. Runlevels **0**, **1** and **6** have [assigned meaning](#halt) and are given special treatment by [init]. Runlevels 7 to 9, although existent, have inconsistent treatment in [init]\'s code compared to the others, and are usually avoided. Additionally, sysvinit supports *ondemand procedures*, and special modes of operation called *emergency mode* and *single user mode*.

[OpenRC](https://wiki.gentoo.org/wiki/OpenRC "OpenRC") also uses the term \'runlevel\' to refer to service sets, but these are identified by names instead, like *sysinit*, *default*, *shutdown*, etc. OpenRC\'s named runlevels are independent of sysvinit numeric runlevels, but [correlated on Gentoo](#gentoo).

[telinit] is [init]\'s control program. It can be invoked in two ways: with a single-character argument, and optionally a `-t` option (e.g. [telinit 2], [telinit -t 7 a], [telinit q], etc.), or with a sequence of `-e` options followed by environment variable settings (e.g. [telinit -e VAR1 -e VAR2=value]).

For the full description of [init] and [telinit], please consult their respective man page. A summary of their functionality follows. []

#### [The inittab file]

[inittab] is a text file that must contain a sequence of single-line entries. Each entry is composed by four fields separated by colons (\':\'), optionally preceded by a sequence of whitespace characters (space and TAB):

-   The first one is the *identifier field*, a sequence of characters that uniquely identifies the entry. This identifier gets written to user accounting database login records (see [man utmp]), so its maximum length is the size of the `ut_id` field of the [libc](https://wiki.gentoo.org/wiki/Libc "Libc")\'s `struct utmp` type (4 characters in the case of GNU libc). Identifier \'\~\~\' is reserved.
-   The second one is the *runlevels field*, a sequence of characters that generally represents a set of [runlevels](#runlevels).
-   The third one is the *action field*, it specifies when the program named in the next field must be executed, and how it must be executed.
-   The fourth and last one is the *process field*, it specifies a program name or its pathname, and the program\'s arguments.

If the first non-whitespace character in a line is \'#\', the line is treated as a comment and ignored. The possible values of the action field are:

-   `respawn`, `wait` and `once`. Entries with these action fields associate programs with runlevels, and specify how the program specified in the process field must be executed. An empty runlevels field in these kinds of entries is the same as one containing `0123456789`.
-   `sysinit`, `boot`, `bootwait` and `initdefault`. Entries with these action fields are used during [the machine\'s boot sequence](#boot). The process field of `initdefault` entries is ignored, and so is the runlevels field of `sysinit`, `boot` and `bootwait`entries.
-   `ondemand`. Entries with these action types can be used for [ondemand procedures](#ondemand).
-   `powerfail`, `powerfailnow`, `powerwait`, `powerokwait`, `ctrlaltdel` and `kbrequest`. Entries with these action fields specify [the handling of signals](#signals) received by [init]. An empty runlevels field in a `kbrequest` entry is the same as one containing `0123456789`, and an empty runlevels field in any of the other kinds of entries is the same as one containing `S0123456789`.
-   `off`. Entries with this action type are ignored.

[inittab] is read and processed by [init] during the boot sequence, immediately before a runlevel change, starting on-demand procedures or [entering single user mode](#singleuser), if explicitly requested with a [telinit q] or [telinit Q] command, and if [init] receives a `SIGHUP` signal. When [inittab] is read, if analysis of identifier fields reveals that an entry has been removed or has changed its action field, [init] kills the corresponding process if it is still running, with the same algorithm used for runlevel changes.

If an `init.autocon=1` argument is specified in the kernel command line, each time [inittab] is processed, for each `console=` kernel parameter it finds, [init] behaves as if [inittab] additionally contained the line:

[FILE] **`/etc/inittab`**

    $:2345:respawn:/sbin/agetty -L -s 115200,38400,9600 $ vt102

With *\$* replaced by the value of the `console=` parameter, and *\$* replaced by a string generated from that value. If [/proc/cmdline] can\'t be read to parse the kernel command line, or the value generated for *\$* matches that of a previous entry (either generated in this way or actually specified in [inittab]), this entry is discarded.

The contents of the process field are used by [init] to construct arguments for a POSIX `execvp()` call in a child process, just as if they were typed in an interactive shell, unless:

-   There is an [/etc/initscript] file and [init] is not in single user mode. In this case, [init] spawns a shell child process using the equivalent of a [/bin/sh /etc/initscript \$ \$ \$ \'\$\'] command, with *\$*, *\$* and *\$* replaced by the contents of the [inittab] entry\'s identifier, runlevels and action field, respectively, and *\$* replaced by the contents of the entry\'s process field, which is passed as a single argument to the shell. This script can be used to augment [init]\'s process handling, e.g. controlling the resources available to them with the [ulimit] utiliy, etc.
-   The process field contains characters that are have special meaning to the shell, like \'\$\', \'\*\', \'&\', etc., or the initial `execvp()` call failed because the program\'s executable file has an unrecognized format. In this case, [init] spawns a shell child process using the equivalent of a [/bin/sh -c \'exec \$\'] command, with *\$* replaced by the contents of the [inittab] entry\'s process field, which is passed to the shell as part of a single argument after the `-c` option.

** Note**\
Gentoo\'s sys-apps/sysvinit package does not install an [/etc/initscript] file.

[init] starts processes specified in [inittab] in line order, creating a new session for each of them with a POSIX `setsid()` call, and redirects their standard input, output and error to the machine\' console. Processes specified by `sysinit` and `bootwait` entries, as well as processes specified by `wait`, `powerwait`, `powerokwait`, `powerfailnow` and `ctrlaltdel` entries while [init] is in single user mode, run in the foreground process group with the console as their session\'s controlling terminal. Processes specified by other entries run as the session leader with no controlling terminal. The environment set up by [init] for its child processes is described [here](#runlevels).

For further information please consult [inittab]\'s man page. []

#### [The boot sequence]

These are [init]\'s actions at program startup:

1.  It sets the the write permission for group and others bits in the file mode creation mask using a POSIX `umask()` call, leaving all other file mode bits unmodified.
2.  It uses a Linux `reboot()` system call with an `RB_DISABLE_CAD` command, to ask the kernel to send a `SIGINT` signal to process 1 when the [Ctrl]+[Alt]+[Del] key combination is pressed (see [here](#signals)).
3.  It uses a Linux `ioctl()` system call with a `KDSIGACCEPT` request, to ask the kernel to send a `SIGWINCH` signal to process 1 whenever an appropriate key combination is pressed. This key combination, the *keyboard signal*, is usually configured to be [Alt]+[Up Arrow].
4.  It closes its standard input, output and error.
5.  It makes itself a session leader using the POSIX `setsid()` call.
6.  It sets the `PATH` environment variable to `/sbin:/usr/sbin:/bin:/usr/bin`.
7.  If the file that corresponds to the [libc](https://wiki.gentoo.org/wiki/Libc "Libc")\'s user accounting database exists (`UTMP_FILE`, [/var/run/utmp] for GNU libc), it truncates the file to length 0, otherwise it creates the file with permissions **0644** (i.e. the [ls -l] command would show `-rw-r--r--`).
8.  If emergency mode was requested, it spawns an emergency shell by invoking the [sulogin] program. Emergency mode is requested by passing a `-b` option, or an `emergency` argument, to [init] (see later). The shell process runs in the foreground process group of a new session with the console as the controlling terminal, and if it exits, the boot sequence resumes.
9.  It reads and processes [inittab].
10. It starts all processes that have an [inittab] entry with a `sysinit` action field. [init] handles them as if the action field was `wait` (see [here](#runlevels)). This means that [init] starts processes in the order their corresponding entries appear in [inittab], and waits for each of them to finish before starting the next one, so execution of programs specified in `sysinit` entries must result in a short-lived processes.
11. A *boot record* (i.e. a `struct utmp` object with `ut_type == BOOT_TIME`) is written to the user accounting database, and to the user accounting log file ([/var/log/wtmp] for GNU libc, which is not truncated on each reboot). The boot record has `ut_user` set to \"reboot\", `ut_id` set to \"\~\~\", `ut_pid` set to 0 and `ut_line` set to \"\~\". The record written to the log file also has `ut_host` set to the operating system\'s release, as contained in the `release` field of a `struct utsname` object filled by a POSIX `uname()` call.
12. If an `-s` option or an `S`, `s` or `single` argument was passed to [init], it enters [single user mode](#singleuser). If the mode is later left, the boot sequence resumes.
13. It determines a *default runlevel*. If [inittab] contains entries with `initdefault` action fields, then the runlevels field of the first one in the file specifies the default runlevel. The field must contain a number from 0 to 9 representing a runlevel, or the letters **S** or **s**, representing single user mode. If the entry\'s runlevels field is invalid or if there is no `initdefault` entry in the file, [init] asks the user to enter a runlevel on the machine\'s console. If this fails for any reason, then the default runlevel is single user mode.
14. If the default runlevel is single user mode, [init] enters it. If single user mode is later left, the boot sequence resumes.
15. It starts all processes that have an [inittab] entry with a `boot` or `bootwait` action field. [init] handles processes specified by `bootwait` entries as if the action field was `wait`, and processes specified by `boot` entries as if the action field was `once`. This means that [init] starts processes in the order their corresponding entries appear in [inittab], and, in the case of those specified by `bootwait` entries, waits for each of them to finish before starting the next one, so execution of programs specified in those entries must result in short-lived processes.
16. If a single character argument representing a number from **0** to **9** was passed as an argument to [init], it [enters the requested runlevel](#runlevels). Otherwise, [init] enters the default runlevel.

Arguments can be passed to [init] by specifying them in the kernel command line (e.g. using the [bootloader](https://wiki.gentoo.org/wiki/Bootloader "Bootloader")\'s available mechanisms): every argument in the command line after a \"\--\" (double hyphen) marker is passed to process 1, as is every argument before the marker, if present, that does not contain an equals sign (\'=\') or dot (\'.\'), and that is not recognized as a kernel parameter.

If [inittab] does not exist, is empty or cannot be read, [init] behaves as if there was an [inittab] file containing the single line:

[FILE] **`/etc/inittab`**

    ~~:S:wait:/sbin/sulogin

#### [Runlevels]

Process assignment to runlevels is specified in the runlevels field of [inittab] entries with a `respawn`, `wait` or `once` action field. Runlevel membership does not need to be one-to-one, a process can be a member of more than one runlevel. Processes specified by entries with a `sysinit`, `boot`, or `bootwait` action field are not members of any runlevel.

Processes in a runlevel are started when [init] *enters the runlevel*. This happens at the end of [the boot sequence](#boot) for a requested or default runlevel, and when the [telinit] program is invoked with a single character argument specifying a runlevel. For example, runlevel **4** is entered after following command:

`root `[`#`]`telinit 4`

Or at the end of the boot sequence if [inittab] contains the following line:

[FILE] **`/etc/inittab`**

    id:4:initdefault:

When a runlevel is entered, [init] writes a *runlevel record* (i.e. a `struct utmp` object with `ut_type == RUN_LVL`) to the user accounting database ([/var/run/utmp] for GNU libc) and log file ([/var/log/wtmp] for GNU libc). The runlevel record has `ut_user` set to \"runlevel\", `ut_id` set to \"\~\~\", and `ut_line` set to \"\~\". The `ut_pid` field encodes the values [init] sets environment variables `RUNLEVEL` and `PREVLEVEL` to for processes that belong to the entered runlevel (see later). As of sysvinit-2.91, [init] also saves the value of `RUNLEVEL` to file [/var/run/runlevel].

Handling of runlevel processes is done according to the action field of their respective [inittab] entry:

-   If the action field is set to `respawn`, the process is respawned it each time it terminates (just like [daemontools](https://wiki.gentoo.org/wiki/Daemontools "Daemontools")-style process supervision suites do). The behaviour of [init] for such processes is therefore similar to the way daemontools behaves for supervised processes started by an [svc -u] command, or the way [systemd](https://wiki.gentoo.org/wiki/Systemd "Systemd") behaves for service units that have `Type=simple` and `Restart=always` directives in their corresponding unit file.
-   If the action field is set to `once`, the process is spawned only once, upon entering the runlevel. The behavior of [init] for such processes is therefore similar to the way daemontools behaves for supervised processes started by an [svc -o] command, or the way systemd behaves for service units that have `Type=simple` and `RemainAfterExit=yes` directives in their corresponding unit file.
-   If the action field is set to `wait`, the process is spawned only once, upon entering the runlevel, and [init] waits for it to finish execution, before starting the next process. The behaviour of [init] for such processes is therefore similar to the way systemd behaves for service units that have `Type=oneshot` and `RemainAfterExit=yes` directives in their corresponding unit file.

If execution of a process specified by a `respawn` entry is restarted 10 times in less than 2 minutes, it is considered to be failing, and is not respawned again until 5 minutes have elapsed. Because [init] waits for processes specified by `wait` entries to finish their execution, only programs that result in short-lived processes when executed are suitable for such entries.

The environment set up by [init] for each child process contains:

-   Environment variables set by the kernel for process 1.
-   Variables `PATH` set to `/sbin:/usr/sbin:/bin:/usr/bin` and `SHELL` set to [/bin/sh].
-   Variables `INIT_VERSION` set to `sysvinit-$`, with *\$* replaced by the package\'s version, `CONSOLE` set to the pathname of console device node used by [init], `RUNLEVEL` set to the current runlevel, or to **S** if in [single user mode](#singleuser), and `PREVLEVEL` set to the previous runlevel (left when entering the current one), or to \"S\" if the current runlevel was entered after leaving single user mode, or to \"N\" if the current runlevel was entered after the boot sequence.
-   Environment variables that have been added by use of the [telinit] program with `-e` options. A [telinit -e VAR=newvalue] command adds a variable named `VAR` to the environment and sets its value to *newvalue*, removing the variable first if it already existed. A [telinit -e VAR] command removes a variable named `VAR` from the environment, that was added with a previous [telinit -e] command. Requests to add variables with names that do not begin with `INIT_` are ignored. A maximum of 16 environment variables can be added this way.

Changing the runlevel makes [init] reread [inittab], determine all previously spawned processes that are still running and do not belong to the new runlevel, according to the runlevels field of their corresponding (possibly updated) entry, and then kill all processes in their process group with a signal. [init] first sends a `SIGTERM` signal, then waits for a grace period, and finally sends a `SIGKILL` signal if any of the process group leaders is still alive. [init] sets the duration of the grace period to 5 seconds at program startup (3 seconds as of version 2.92), but it can be changed to a different value each time [telinit] is invoked, by passing it a `-t` option followed by a new time value in seconds. This value is used until the next command received by [init] on its control FIFO updates it. For example, to change to runlevel 2, and also set a grace period of 10 seconds between `SIGTERM` and `SIGKILL`, the following command can be used:

`root `[`#`]`telinit -t 10 2`

Processes that belong to both the previous and current runlevels are left alone. When performing a runlevel change, [init] does not kill processes specified by `boot` entries that are still running. Each time [init] spawns a child process, it writes an *init process record* (i.e. a `struct utmp` object with `ut_type == INIT_PROCESS`) to the user accounting database and log file, and each time a child process that [init] spawned terminates, [init] writes an *terminated process record* (i.e. a `struct utmp` object with `ut_type == DEAD_PROCESS`) to the user accounting database and log file. These records have empty `ut_user` and `ut_line` fields, `ut_id` set to the contents of the corresponding [inittab] entry\'s identifier field, and `ut_pid` set to the process\' process ID (PID). No init process and terminated process records are written to the user accounting database and log file if the process field of the entry starts with a plus sign (\'+\').

Runlevel, init process and terminated process records written to the log file also have the `ut_host` field set to the operating system\'s release, as contained in the `release` field of a `struct utsname` object filled by a POSIX `uname()` call. The contents of the user accounting database and log file can be seen with the [utmpdump] program, see [man utmpdump]. []

#### [Ondemand procedures]

[init] supports the definition of sets of processes that can be launched by explicit use of the [telinit] program. These sets of processes are called *ondemand procedures*. Up to three sets of processes can be defined, identified by letters **A**, **B** and **C**. Their member processes are specified in [inittab] entries that contain an **A**, **B** or **C** character, or its lowercase form, in the runlevels field. A [telinit a], [telinit b] or [telinit c] command, respectively, or a [telinit A], [telinit B] or [telinit C] command, respectively, starts (or restarts) all processes in the set that are not currently running. [init] rereads [inittab] whenever [telinit] is invoked in this way, so that it can pick up updated entries.

Processes configured to be in the A, B or C set can have [inittab] entries with a `respawn`, `wait` or `once` action field. They can also have an `ondemand` action field, which [init] treats it as if it was a `respawn` action. After a [telinit] invocation that specifies their ondemand procedures set, these processes are not killed by [init] when performing a runlevel change, but are if [single user mode](#singleuser) is entered, unless their [inittab] entry also marks them as valid for that mode.

Ondemand procedures can not be started in single user mode or during the boot sequence. []

#### [Single user mode]

Single user mode is an execution mode supported by [init], that is similar to a runlevel: upon entering this mode [init] starts a set of processes that are configured in [inittab] to be *valid* for it and not currently running, and kills all other configured processes that are still running, except those specified by `boot` entries, with the same algorithm used for [runlevel changes](#runlevels).

Processes valid for single user mode are those with an [inittab] entry that contains an **S** or **s** character in its runlevels field. If [inittab] does not contain entries marked as valid for single user mode, [init] behaves as if the file contained the following additional entry:

[FILE] **`/etc/inittab`**

    ~~:S:wait:/sbin/sulogin

This entry makes init spawn an emergency shell by invoking the [sulogin] program when entering single user mode.

[init] enters single user mode:

-   During [the machine\'s boot sequence](#boot), if requested to do so in the kernel command line, after starting all processes specified by `sysinit` entries,
-   If the default runlevel determined during the boot sequence is single user mode, after starting all processes specified by `sysinit` entries but before starting all processes specified by `boot` and `bootwait` entries, or
-   If a [telinit s] or [telinit S] command is used.

Single user mode is left when either a runlevel change is requested using [telinit], or when all processes marked as valid for single user mode exit and are not configured to be restarted (e.g. all their entries have `wait` and `once` action fields). In the latter case, either the boot sequence continues with the processing of [inittab]\'s `boot` and `bootwait` entries, or the default runlevel is determined again with the same algorithm that is used during the boot sequence, and [init] enters it. []

#### [Signal processing]

[init] responds to received signals in the following ways:

-   `SIGHUP`: forces [init] to reexamine its configuration file, [/etc/inittab].
-   `SIGINT`: makes [init] start the process specified by the first active [inittab] entry with a `ctrlaltdel` action field. This signal is sent by the kernel when the [Ctrl]+[Alt]+[Del] key combination is pressed. [init] handles the specified process as if the entry\'s action field was `wait`.
-   `SIGWINCH`: makes [init] start the process specified by the first active [inittab] entry with a `kbrequest` action field. This signal is sent by the kernel when the key combination that corresponds to *keyboard signal* is pressed (usually configured to be [Alt]+[Up Arrow]). [init] handles the specified process as if the entry\'s action field was `once`.
-   `SIGUSR1`: makes [init] close and reopen its control FIFO, [/run/initctl] ([/dev/initctl] for sysvinit version 2.88).
-   `SIGUSR2`: makes [init] close its control FIFO. This may be used to make sure [init] is not holding open any files, but also prevents it from receiving commands from [telinit]. The FIFO can be reopened by sending [init] the `SIGUSR1` signal.
-   `SIGPWR`: used by [init] for its power failure and restoration routines.

[init] supports communication with programs that are able to monitor the machine\'s power supply status (e.g. an uninterruptible power supply management program). If such a program can be configured to write to file [/var/run/powerstatus] (formerly [/etc/powerstatus]) and send process 1 a `SIGPWR` signal, [init] can take actions depending on the reported status. When [init] receives a `SIGPWR` signal, it reads the first character of file [/var/run/powerstatus]:

-   If it is a character other that **O** or **L** (conventionally **F** for \"fail\"), it considers the power to be failing and that there might be a need to shut down soon, and starts all processes specified by active [inittab] entries with `powerfail` and `powerwait` action fields.
-   If it is an **L** character (for \"low\"), it considers the power supply to be in low battery state and that inminent shutdown is needed, and starts all processes specified by active [inittab] entries with a `powerfailnow` action field.
-   If it is an **O** character (for \"OK\"), it considers the power supply to be restored to normal status and that there is no longer an need to shut down, and starts all processes specified by active [inittab] entries with a `powerokwait` action field.

[init] handles processes specified by `powerwait`, `powerfailnow` and `powerokwait` entries as if the action field was `wait`, and processes specified by `powerfail` entries as if the action field was `once`. [init] removes [/var/run/powerstatus] after reading it. Usage of this file and the `SIGPWR` signal is discouraged in favor of sending `INIT_CMD_POWERFAIL`, `INIT_CMD_POWERFAILNOW` and `INIT_CMD_POWEROK` commands on [init]\'s control FIFO (as defined in [/usr/include/initreq.h], see [man initctl]).

A `ctrlaltdel`, `kbrequest`, `powerfail`, `powerfailnow`, `powerwait` or `powerokwait` entry is considered active if its runlevels field includes the current runlevel, or contains either **S** or **s** and [init] is in [single user mode](#singleuser). []

#### [init re-execution]

[init] is capable of re-executing itself. This is similar to [systemd](https://wiki.gentoo.org/wiki/Systemd "Systemd")\'s [systemctl daemon-reexec] command, and mostly useful after a package upgrade, to have a new version of [init] execute as process 1 without a complete machine reboot, provided the new version is sufficiently compatible with the mechanism used by the running version for re-execution.

Re-execution is triggered with a [telinit u] or [telinit U] command. When asked to do this, [init] spawns a child process with a pipe connected to it, the *state pipe*, that the child uses to transmit back an encoding of [init]\'s execution state, as well as of the configuration and state of all processes configured in [inittab]. Process 1 [init] then uses a POSIX `execle()` call to perform the re-execution, including in the environment passed to the call all variables set by [telinit -e] commands. At program startup, the new process image detects whether it has an open file description that corresponds to the reading end of the state pipe or not, and if it does, it reads the encoded state of the previous process image from the pipe, adjusts its own state, and arranges to appear, from the perspective of its externally observable behaviour, as if it resumed execution from the point the previous process image was at before the `execle()` call (e.g. the boot sequence is not performed again, no runlevel change happens, single user mode is not left, etc.).

### [Shutdown and reboot]

#### [][halt, poweroff, and reboot]

The [halt], [poweroff] and [reboot] programs halt the machine, power it off and reboot it, respectively. The [halt] program also behaves as [poweroff] if invoked with a `-p` option.

Unless they are invoked with an `-f` option, these programs check the current runlevel. If the `INIT_VERSION` and `RUNLEVEL` variables are set in the environment (which would happen if they are executed because they are configured in [inittab]), the current runlevel is taken to be the value of `RUNLEVEL`. Otherwise, they search the user accounting database ([/var/run/utmp] for GNU libc) for the most recent runlevel record (i.e. a `struct utmp` object with `ut_type == RUN_LVL`) and decode the current runlevel from its `ut_pid` field. If searching the user accounting database fails or returns nothing, the runlevel is read from [/var/run/runlevel]. If the runlevel is neither **0** nor **6**, they replace themselves with the [shutdown] program (see later), using a POSIX `execv()` call. [halt] and [poweroff] perform the equivalent of a [shutdown -h now] action, and [reboot], the equivalent of a [shutdown -r now] action. If they are invoked with a `-t` option followed by a time value in seconds, they pass them unmodified to the [shutdown] program.

If [halt], [poweroff], and [reboot] are invoked with an `-f` (\"force\") option, or they are invoked in runlevels 0 or 6, they write a *shutdown record* to the user accounting log file ([/var/log/wtmp] for GNU libc). The shutdown record is a runlevel record (`ut_type == RUN_LVL`) that has `ut_user` set to \"shutdown\", `ut_id` and `ut_line` set to \"\~\~\", `ut_pid` set to 0, and `ut_host` set to the operating system\'s release, as contained in the `release` field of a `struct utsname` object filled by a POSIX `uname()` call. Then, unless they have been invoked with an `-n` (\"no sync\") option, they sync all disks, flushing all the dirty system buffers, using the POSIX `sync()` call. And finally, they flush the cache of all hard disks using a Linux `ioctl()` system call with a `HDIO_DRIVE_CMD` request (specifying `WIN_FLUSH_CACHE` or `WIN_FLUSH_CACHE_EXT`), and perform their respective shutdown action using the Linux `reboot()` system call.

Gentoo\'s patched [reboot] program also accepts a `-k` (\"kexec\") option, which makes it reboot the machine using a kernel kexec boot instead of a standard system boot. This works if the kernel is configured with kexec support:

[KERNEL] **kexec support**

    Processor type and features  --->
       [*] kexec system call

If the kexec boot fails, [reboot] falls back to a standard system boot. A [reboot -k] command can only be used if invoked in runlevel 6, or if `-f` is also specified.

If [halt], [poweroff], and [reboot] are invoked with an `-i` (\"ifdown\") option, they also shut network interfaces down using a Linux `ioctl()` system call with a `SIOCSIFFLAGS` request to clear each interface\'s `IFF_UP` flag (see [man netdevice]). If they are invoked with an `-h` (\"hddown\") option, they put all hard disks in standby mode after flushing their cache, using using a Linux `ioctl()` system call with a `HDIO_DRIVE_CMD` request (specifying `WIN_STANDBYNOW1` and `WIN_STANDBYNOW2`). If they are invoked with a `-w` option, they only write the shutdown record to the user accounting log file, without actually shutting the machine down. This option can be combined with `-i` and `-h`. If they are invoked with a `-d` option, no shutdown record is written to the user accounting log file (`-n` implies `-d`).

For more information on [halt], [poweroff] and [reboot], please consult their respective man pages. []

#### [shutdown]

The [shutdown] program is a generic program for shutting the machine down. It accepts options, a time specification, and an optional message to be shown to logged in users. The time specification is used to delay actual shutdown, it can be a nonzero time value in minutes, optionally preceded by a plus sign (\'+\'), it can have the form `h:mm` or `hh:mm` to specify clock time (in 24-hour form and local time, e.g. [shutdown -r 4:30] or [shutdown -r 22:13]), or it can be the word **now**. In the first case, machine shutdown is initiated after the specified time has elapsed, in the second case, it is initiated at the specified clock time, and in the latter case, it is initiated immediately. [shutdown 0] is valid and equivalent to [shutdown now].

[shutdown] does not exit, it writes a PID file with its process ID and waits the requested amount of time, displaying the specified message, if any, to logged in users in the same way that the [wall] program (from package util-linux, [[[sys-apps/util-linux]](https://packages.gentoo.org/packages/sys-apps/util-linux)[]]) does, with an increasing frequency as the scheduled shutdown approaches. The PID file is [/var/run/shutdown.pid]. Within the last 5 minutes until the scheduled shutdown, the program also writes a message in file [/etc/nologin], warning that the system is going down. This file instructs the [login] program to prevent non-root users from logging in. If [shutdown] is invoked and it finds [/var/run/shutdown.pid] exists and contains a valid process ID (probed using a POSIX `kill()` call with a null signal, 0), it exits with a *\"shutdown: already running\"* error. If [shutdown] is invoked with a `-c` option (\"cancel\"), no time specification, and an optional message, it cancels a pending shutdown request by sending a `SIGINT` signal to the process with the PID read from [/var/run/shutdown.pid], and displays the specified message, if any, to logged in users.

[shutdown] changes the working directory to [/], waits the requested amount of time and, unless it was invoked with the `-k` option, sends a message to a syslog server, if available, announcing that the system is shutting down, using the libc\'s implementation (i.e. that of the POSIX `openlog()`, `syslog()` and `closelog()` calls), and initiates shutdown. [shutdown]\'s message specify facility `LOG_USER` and severity `LOG_NOTICE`. If [shutdown] was invoked without the `-n` option, it removes the [/var/run/shutdown.pid] and [/etc/nologin] files, syncs all disks, flushing all the dirty system buffers, using the POSIX `sync()` call, and finally replaces itself with the [telinit] program to [change the runlevel](#runlevels), using a POSIX `execv()` call. The [shutdown] program from upstream\'s package performs the equivalent of a [telinit 0] action if it is invoked with an `-h` option, the equivalent of a [telinit 6] action if it is invoked with an `-r` option, and the equivalent of a [telinit 1] action if it is invoked with neither of these options, which means that [shutdown] will do whatever [/etc/inittab] specifies for those runlevels. Therefore, entering runlevel 0 is customarily expected to either halt or power the machine off, entering runlevel 6 is customarily expected to reboot the machine, and runlevel 1 is customarily expected to be some kind of \'maintenance mode\'. If an `-H` option is passed together with `-h`, [shutdown] additionally performs the equivalent of a [telinit -e INIT_HALT=HALT] action before the `execv()` call, and if a `-P` option is passed together with `-h`, [shutdown] additionally performs the equivalent of a [telinit -e INIT_HALT=POWERDOWN] action before the `execv()` call (corrected to [POWEROFF] in version 2.92 to match the man page). This allows runlevel 0 processes to use the value of the `INIT_HALT` environment variable to determine whether a halt or poweroff operation was requested. [shutdown] can also be invoked with a `-i` option, followed by a single character that is passed as [telinit]\'s argument, and with a `-t` option followed by a time value in seconds, that are passed unmodified to [telinit]. Only 0, 1, 5, 6, A, B, C, S, a, b, c, and s are valid after `-i`.

Gentoo\'s patched [shutdown] program simplifies usage according to the following table:

  ---------------------------------------------------------------------------------------------------------------------------------- ------------------ --------------------------------------------------------------------
                                                                Gentoo                                                                    Upstream                                   Results in
                                                            `shutdown -H`                                                             `shutdown -h -H`     Entering runlevel 0 with `INIT_HALT` set to `HALT`
                                                            `shutdown -P`                                                             `shutdown -h -P`   Entering runlevel 0 with `INIT_HALT` set to `POWERDOWN`
                                                            `shutdown -h`                                                             `shutdown -h -P`   Entering runlevel 0 with `INIT_HALT` set to `POWERDOWN`
   [shutdown] with no `-h`, `-H` or `-P`   `shutdown -i s`                        Entering single user mode
  ---------------------------------------------------------------------------------------------------------------------------------- ------------------ --------------------------------------------------------------------

If [shutdown] is invoked with a `-k` option, it only displays the specified message, if any, to logged in users while waiting the requested amount of time, but doesn´t actually shut the machine down. If it is invoked with a `-f` option, it creates file [/fastboot], a convention for asking the [rc subsystem](https://wiki.gentoo.org/wiki/Rc "Rc") to skip checking filesystems with [fsck] after next boot, and if it is invoked with a `-F` option, it creates file [/forcefsck], a convention for asking the rc subsystem to make [fsck] check filesystems after next boot, even if they are marked clean, by passing it a special \'force\' option. [OpenRC](https://wiki.gentoo.org/wiki/OpenRC "OpenRC")\'s [fsck] service, for instance, follows this convention. Cancelling a pending shutdown with the `-c` option removes files [/var/run/shutdown.pid], [/fastboot], [/forcefsck] and [/etc/nologin].

If [shutdown] is invoked with an `-a` option, it looks up all logged in users in a list contained in file [/etc/shutdown.allow]. If there is a match, or if root is logged in, shutdown is allowed to proceed. Otherwise, a *\"shutdown: no authorized users logged in\"* error is displayed. The list of logged in users is obtained by reading login records from the user accounting database. [/etc/shutdown.allow] is a text file that contains one account name per line. Lines that start with a \'#\' character are treated as comments and ignored. The [/etc/shutdown.allow] mechanism can be used as a way of limiting the ability of logged in users to trigger a machine reboot by pressing the [Ctrl]+[Alt]+[Del] key combination, if [shutdown] is executed as a result because it is specified in an [/etc/inittab] `ctrlaltdel` entry (see [here](#signals)).

Finally, if [shutdown] is invoked with a `-n` option, it performs the machine shutdown itself instead of delegating it to runlevel processes. This option can only be used in combination with options `-h`, `-H`, `-P` and `-r`, or option `-i` if it names runlevels 0 or 6, and its use is discouraged. In this case:

1.  It kills all processes, first by sending a `SIGTERM` signal using a `kill(-1, SIGTERM)` call, then waiting for a grace period, and finally sending a `SIGKILL` signal. The duration of the grace period is the time value passed with the `-t` option, if any (which in this case is interpreted by [shutdown] instead of being passed to [telinit]), or 3 seconds if there is no `-t` option.
2.  It writes a shutdown record to the user accounting log file, just like [halt], [poweroff] or [reboot].
3.  It disables process accounting by invoking the [accton] program (ignoring failures if it is not present).
4.  It turns filesystem quotas off using a [quotaoff -a] command (ignoring failures if the [quotaoff] program is not present).
5.  It syncs all disks, flushing all the dirty system buffers, using the POSIX `sync()` call,
6.  It disables devices and files for paging and swapping using a [swapoff -a] command,
7.  It unmounts all filesystems named in [/proc/self/mountinfo] using a [umount -a] command,
8.  It reboots the machine if it was invoked with `-r` or `-i 6`, or halts the machine otherwise, using the Linux `reboot()` system call.

For more information please consult the [shutdown] man page.

### [bootlogd]

[bootlogd] is a daemon that logs output sent by processes to [/dev/console], to a log file in the filesystem, and can be used as a boot sequence logger. It does so by opening a pseudo-terminal master and slave device pair using the [libc](https://wiki.gentoo.org/wiki/Libc "Libc")\'s `openpty()` function (and falling back to trying to open legacy BSD-like device pairs [/dev/ptyp0] and [/dev/ttyp0], [/dev/ptyp1] and [/dev/ttyp1], etc. if `openpty()` fails), using a Linux `ioctl()` system call with a `TIOCCONS` request to perform console redirection to the pseudo-terminal slave, and then reading from the pseudo-terminal master and logging read messages to the log file, prepended with a timestamp. The pathname of the log file can be specified after an `-i` option, otherwise it defaults to [/var/log/boot]. If the logfile is not accessible, the messages will be buffered in memory until it is (possibly after mounting some filesystem, which prevents [bootlogd] from creating the file under a mount point). If a `-c` option (\"create\") is passed to [bootlogd], the logfile is created if it does not exist. [bootlogd] opens the log file for appending; if it is passed a `-r` option (\"rotate\"), it will rename the current logfile, adding a tilde (\'\~\') after the name (e.g. [/var/log/boot\~]), and create a new one instead.

[bootlogd] also tries to display read messages on the actual machine console, using the POSIX `write()` call with a file descriptor obtained by opening a suitable device node. It parses the kernel command line, and if a `console=` kernel parameter was specified, [bootlogd] tries to use its value as the device node\'s pathname. If that fails or there is no `console=` parameter, it tries a sequence of default device node pathnames ([/dev/tty1], [/dev/ttyS0], and others).

[bootlogd] forks a child process and exits, optionally writing a PID file with the child\'s process ID if a `-p` option is passed followed by the file\'s pathname. The child process is the long-lived one that does the actual logging, for compatibility with [rc subsystems](https://wiki.gentoo.org/wiki/Rc "Rc") that expect that behavior from daemons (like [OpenRC](https://wiki.gentoo.org/wiki/OpenRC "OpenRC")\'s [start-stop-daemon] program). The forking can be prevented by passing a `-d` option (e.g. for use with [daemontools](https://wiki.gentoo.org/wiki/Daemontools "Daemontools")-style process supervision suites, OpenRC\'s [supervise-daemon] program, or configuring it in [/etc/inittab] so that it is launched directly by [init]).

[bootlogd] uses the POSIX `fflush()` call after writing every newline-terminated line to the log file; if it is passed an `-s` option, it also follows this with a POSIX `fdatasync()` call, to ensure that the data is written to the file.

For more information please consult the [bootlogd] man page.

### [Other utilities]

The [killall5] program sends a signal to all processes except itself, process 1, and all processes in its session, so that if it is called from a shell script, it won\'t kill the shell process that is running the script. It does so by reading all process subdirectories of [/proc] (i.e. subdirectories that have names that correspond to process IDs) to get a list of processes, mounting the `proc` filesystem if necessary with a [mount -t proc proc /proc] command, and then sends each of them the specified signal one by one. [killall5] takes a signal number as an argument, optionally preceded by a hyphen (\'-\'); if invoked with no argument, it sends a `SIGKILL` signal.

[killall5] determines each process\' session ID, and whether it is a zombie or kernel thread (so that it can be skipped), by reading the corresponding [/proc/\*/stat] file. It prints error messages on its standard error if its standard input is a terminal, and to a syslog server otherwise, using facility `LOG_DAEMON` (and falling back to the machine\'s console by using a POSIX `openlog()` call with the `LOG_CONS` flag). If it is invoked with a sequence of one or more `-o` (\"omit\") options followed by a comma-separated list of process IDs, corresponding processes are not sent the specified signal.

[killall5] used to be called by OpenRC\'s [killprocs] service until version 0.27, when it was replaced by internal program [/lib/rc/bin/kill_all].

The [runlevel] program prints [the previous and current runlevels](#runlevels) on its standard output. It does so by decoding them from the `ut_pid` field of the most recent runlevel record (i.e. a `struct utmp` object with `ut_type == RUN_LVL`) in the user accounting database. The pathname of the file that corresponds to the database can optionally be specified as an argument, otherwise, [runlevel] uses the libc\'s default one ([/var/run/utmp] for GNU libc). If searching the user accounting database fails or returns nothing, the current runlevel is read from [/var/run/runlevel], and the previous runlevel is displayed as \"N\". If that fails as well, [runlevel] prints \"unknown\".

The [fstab-decode] program can be used to invoke another program with arguments that might have character escape sequences that use the [/etc/fstab] file\'s encoding convention, i.e. \'\\011\' representing a TAB character, \'\\040\' representing a space character, \'\\\\\' or \'\\134\' representing a backslash (\'\\\'), etc. (see [man fstab]). It accepts a program name or its pathname, followed by the program\'s arguments. [fstab-decode] replaces replaces itself with the specified program using a POSIX `execvp()` call, passing the supplied arguments to it with any escape sequence replaced by its corresponding character. Generally, this is only useful if [fstab-decode]\'s arguments are generated from the contents of [/etc/fstab] (e.g. by using the [awk] utility).

For more information on [killall5], [runlevel] or [fstab-decode], please consult their respective man page. []

### [][Gentoo\'s sysvinit setup]

Gentoo\'s sysvinit setup, as specified in its standard [/etc/inittab] file, is as follows:

-   The default runlevel is **3**. This is specified in an `initdefault` entry.
-   [init] executes an [openrc sysinit] command during the [boot sequence](#boot) and waits for it to finish. This is specified in a `sysinit` entry, and makes [OpenRC](https://wiki.gentoo.org/wiki/OpenRC "OpenRC") start services in its `sysinit` runlevel.
-   [init] then executes an [openrc boot] command and waits for it to finish. This is specified in a `bootwait` entry, and makes OpenRC start services in its `boot` runlevel.
-   Entering runlevel 1 makes [init] execute an [openrc single] command and wait for it to finish, then spawn an [agetty] process for terminal [/dev/tty1]. The [openrc] invocation makes OpenRC stop all its managed services except those in its `sysinit` runlevel.
-   Entering runlevel 2 makes [init] execute an [openrc nonetwork] command and wait for it to finish, then spawn [agetty] processes for terminals [/dev/tty1] to [/dev/tty6]. The [openrc] invocation makes OpenRC start services in its `nonetwork` runlevel.
-   Entering runlevel 3 makes [init] execute an [openrc default] command and wait for it to finish, then spawn [agetty] processes for terminals [/dev/tty1] to [/dev/tty6]. The [openrc] invocation makes OpenRC start services in its `default` runlevel.
-   Runlevels 4 and 5 are identical to runlevel 3.
-   Entering runlevel 0 makes [init] [re-execute itself](#reexec), then execute an [openrc shutdown] command and wait for it to finish, then [power the machine off](#halt) with a [halt -dhnp] command. The [openrc] invocation makes OpenRC start services in its `shutdown` runlevel.
-   Entering runlevel 6 makes [init] re-execute itself, then execute an [openrc reboot] command and wait for it to finish, then reboot the machine with a [reboot -dkn] command. The [openrc] invocation makes OpenRC start services in its `shutdown` runlevel, and set variable `RC_REBOOT` to \"YES\" in the environment of executed service scripts. This allows services to use `RC_REBOOT` to determine whether a reboot operation was requested or not.
-   Entering single user mode makes [init] execute an [openrc single] command and wait for it to finish, then spawn an emergency shell by invoking the [sulogin] program.
-   Using a [telinit a] command makes [init] execute the [/etc/X11/startDM.sh] script. This is specified in a `once` entry, and used by OpenRC service script [/etc/init.d/xdm] from package [[[x11-base/xorg-server]](https://packages.gentoo.org/packages/x11-base/xorg-server)[]] to launch a [display manager](https://wiki.gentoo.org/wiki/Display_manager "Display manager"). Script [/etc/X11/startDM.sh] is provided by package [[[x11-apps/xinit]](https://packages.gentoo.org/packages/x11-apps/xinit)[]].
-   Pressing the [Ctrl]+[Alt]+[Del] key combination makes [init] reboot the machine with a [shutdown -r now] command. This is specified in a `ctrlaltdel` entry.

[agetty] process are specified in `respawn` entries, so that when a user\'s interactive shell exits, it is possible to log in again on the terminal the shell used. The Gentoo ebuild might also add architecture-specific entries to [/etc/inittab], to make [init] spawn additional [agetty] processes for special character device nodes.

## [Removal]

** Warning**\
sysvinit can only be removed safely if the operating system has been configured with an init system which doesn\'t require sysvinit, and the machine has been rebooted to use an alternative init (PID 1). Currently, this is *officially* supported by Gentoo only if that init system is [systemd](https://wiki.gentoo.org/wiki/Systemd "Systemd").

Users of OpenRC can have sys-apps/openrc compiled with **USE=sysv-utils** and system (most importantly bootloader) configured to use [openrc-init](https://wiki.gentoo.org/wiki/OpenRC/openrc-init "OpenRC/openrc-init"). This way OpenRC doesn\'t depend on sysvinit.

### [Unmerge]

`root `[`#`]`emerge --ask --depclean --verbose sys-apps/sysvinit`

## [See also]

-   [Runit](https://wiki.gentoo.org/wiki/Runit "Runit") --- lightweight process supervision suite, originally inspired by [daemontools](https://wiki.gentoo.org/wiki/Daemontools "Daemontools") that offers fast and reliable service management.
-   [S6 and s6-rc-based init system](https://wiki.gentoo.org/wiki/S6_and_s6-rc-based_init_system "S6 and s6-rc-based init system") --- an init system built using components from the [s6](https://wiki.gentoo.org/wiki/S6 "S6"), [s6-rc](https://wiki.gentoo.org/wiki/S6-rc "S6-rc") and [s6-linux-init](https://wiki.gentoo.org/wiki/S6-linux-init "S6-linux-init") packages
-   [Systemd](https://wiki.gentoo.org/wiki/Systemd "Systemd") --- a modern SysV-style init and [[rc](https://wiki.gentoo.org/wiki/Rc "Rc")] replacement for Linux systems.
-   [Comparison of init systems](https://wiki.gentoo.org/wiki/Comparison_of_init_systems "Comparison of init systems") --- compares and contrasts **[init systems](https://wiki.gentoo.org/wiki/Init_system "Init system")** for Unix(like) [OSs](https://en.wikipedia.org/wiki/Operating_system "wikipedia:Operating system")