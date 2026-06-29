**[] Deprecated article**\
\

This article is **deprecated (obsolete)**. Contents are [no longer relevant], and are intended for historical reference only!

\
TLDR: **Do not use this article!**

**Resources**

[[![Gentoo peach graphic](/images/thumb/a/ad/Gentoo-logo-peach.svg/25px-Gentoo-logo-peach.svg.png)](https://wiki.gentoo.org/wiki/Project:Project_name "Project:Project name")][Project](https://wiki.gentoo.org/index.php?title=Project:Project_name&action=edit&redlink=1 "Project:Project name (page does not exist)")

[[]][Home](https://web.obarun.org/software)

\
**66** is a service management suite (also an \"init system\") which uses [[[sys-apps/s6]](https://packages.gentoo.org/packages/sys-apps/s6)[]] under the hood. It is a wrapper around the [s6 supervision suite](https://wiki.gentoo.org/wiki/S6 "S6"); See the [draft document of s6](https://wiki.gentoo.org/wiki/User:Flexibeast/drafts/S6 "User:Flexibeast/drafts/S6") for more info.

It provides a simple declarative service frontend format, with support for (hard and soft) dependencies and other features like the user to run under, the description, grouping services by trees (similar to openrc runlevels but more), etc\... See the [official documentation page](https://web.obarun.org/software/66/0.8.0.2/index/) for more detailed info.

## Contents

-   [[1] [Installation]](#Installation)
-   [[2] [Configuration]](#Configuration)
    -   [[2.1] [Environment variables]](#Environment_variables)
    -   [[2.2] [Files]](#Files)
-   [[3] [Usage]](#Usage)
    -   [[3.1] [Usage in service files]](#Usage_in_service_files)
-   [[4] [Caveats]](#Caveats)
-   [[5] [Tips]](#Tips)
    -   [[5.1] [Daemons which stubbornly doublefork]](#Daemons_which_stubbornly_doublefork)
    -   [[5.2] [dbus-broker (yes, without systemd)]](#dbus-broker_.28yes.2C_without_systemd.29)
    -   [[5.3] [syslog]](#syslog)
-   [[6] [Troubleshooting]](#Troubleshooting)
    -   [[6.1] [Unmerge]](#Unmerge)
-   [[7] [See also]](#See_also)
-   [[8] [External resources]](#External_resources)
-   [[9] [References]](#References)

## [Installation]

**66** suite is divided into various packages, which are available in the [66-svmgr](https://github.com/pramodvu1502/66-svmgr-gentoo-overlay/) repository. To the add the repository with eselect:

`root `[`#`]`emerge --ask eselect-repository`

`root `[`#`]`eselect repository add 66-svmgr git `[`https://github.com/pramodvu1502/66-svmgr-gentoo-overlay/`](https://github.com/pramodvu1502/66-svmgr-gentoo-overlay/)

`root `[`#`]`emaint sync -r 66-svmgr`

Installing the package [[[sys-apps/66-boot]](https://packages.gentoo.org/packages/sys-apps/66-boot)[]] will pull in all the required dependencies:

`root `[`#`]`emerge --ask sys-apps/66-boot::66-svmgr`

Unlike [systemd](https://wiki.gentoo.org/wiki/Systemd "Systemd") and [openrc](https://wiki.gentoo.org/wiki/Openrc "Openrc"), s66 doesn\'t know the concept of a **firstboot**. which is a concept that populates the machine-id, that ensures that correct directories and symlinks exist,

Everything, even the default settings, need to be pre-configured by an external script. [[[sys-process/66-initial-setup]](https://packages.gentoo.org/packages/sys-process/66-initial-setup)[]] provides the script. (Script and package section TODO) After configuration you may safely uninstall the script.

## [Configuration]

[66-initial-setup] command is the equivalent of a *firstboot* on **66**. However, it needs to be run manually in the bootstrap environment like the chroot, before the init system is run, and there are no hooks to automatically run it.

`root `[`#`]`66-initial-setup`

This provides reasonable a default configure for most users requirements. If there is a need to customize, then help options are viewable with:

`root `[`#`]`66-initial-setup -h`

** Note**\
Only supports single-hyphen-alphabet arguments.

Prepare boot chain:

Run the command

`root `[`#`]`66 configure boot@system`

** Tip**\
\`system\` can be replaced with anything in \`boot@system\`

It will drop into the system editor (i.e. [nano]) where it\'s possible to adjust the environment variables; Those variables affect how the boot process will be configured.

** Note**\
Currently \`66\` has many variables built-in like HOSTNAME KEYMAP which override and overwrite the global confs like [/etc/hostname] [/etc/vconsole.conf]; This is being fixed soon to respect the global configuration;)

Optionally,

`root `[`#`]`ln -s ../env.d /etc/66/environment`

can be run in order to get all the env-vars applied in **66** just as in **openrc**; The supported format is exactly the same across openrc and 66 (\`VAR=\"value\"\` only, no commands or flags, or shell-specific substitutions).

Not linking as mentioned above breaks many **eselect**-set variables, as eselect subcommands modify here.

### [Environment variables]

Explained and listed in the 66 configure command itself

### [Files]

-   [/usr/share/66/service] - Packaged frontends for system services
-   [/usr/share/66/service/user] - Packaged frontends for user services
-   [/etc/66/] - Same as [/usr/share/66/] but for the system admin/user.
-   [/var/lib/66] - The underlying databases of results of the parsing of the frontends are stored here; Frontends are parsed and their results like start/stop scripts, dependency chains etc\... are stored here; Kindly don\'t touch this manually.
-   [\~/.66/] - Same as [/etc/66/] but for per-user.
-   [\~/.66/system] - The per-user equivalent of [/var/lib/66]
-   [/etc/66/init.conf] - Basic variables for 66. (Can be overriden by mentioning on the kernel command line the same **KEY=value** pairs as in the conffile)
-   [/etc/66/sbin-init] - The execline script which executes into \`66\` as PID-1. Symlinked as [/sbin/init] if **USE**=**init**.

## [Usage]

This software is a service manager and an init system.

The [/etc/66/sbin-init] execlineb script is what execs into \`66\` as PID-1 with the correct arguments. [/sbin/init] is symlinked to it if USE=init is enabled on the package.

The only user-facing command is \`66\`

** Important**\
66 command has no explicit switch meant to differentiate between \"system\" and \"user\" instances (AKA \"scandirs\" by 66).

It depends exclusively on the user it is run as, to differentiate (root is \"system\"; everything else is \"user\").

Run the command as root for the system instance, as your own user for the user instance. To control another user\'s instance, run the command as that user.

The system command example (prefix **sudo**, **doas**, **s6-sudo**, **run0** used for running as root in your own terminal/shell):

`root `[`#`]`66 -z tree status`

The \"user\" command example (Run as your own user, like a normal command; DON\'T use sudo, run0, doas, s6-sudo, whatever else):

`user `[`$`]`66 -z tree status`

Failure to do this will mean logging into as root will not be possible, nor get a \"user\" instance (Which may contain important services).

Run

`user `[`$`]`66 -h`

for help;

`user `[`$`]`66 $ -h`

for specific help.

### [Usage in service files]

Many other tools are available, like 66-ns, execl-\* commands, which are meant to be used in service scripts.

A simple non-interactive scripting language execline is used in 66 (created by the developer of s6 himself). The *entire* script in that language is converted into a long command; each *step* i.e. command executes into the next. However, It is possible to set the preferred interpreter by specifying a **Build=custom** key-value pair in the section with the custom-script and specifying the interpreter in the **Execute=()** key as **Execute=(#!/bin/sh/or/some.other/interpreter** with the script next line onwards until the ending **)**.

** Note**\
The frontend parser is capable of differentiating the **)** in **case \$var in state) command ;;** and other uses of **(** and **)** in the script, from the end of **Execute=(**; So don\'t worry about it.

## [Caveats]

Since this is *new* software, not all services and daemons have 66-compatible frontend files. There might be a need to have to install them unpackaged into [/etc/66/service/] or in rare cases even write them manually. Kindly contact the writer of this wiki for help writing and troubleshooting the frontends.

\
Obarun is an arch-based distro which is the primary distro of 66 upstream. It\'s frontend repository contains many frontend files (for reference, not all can be easily used directly on gentoo).

The repo: [https://git.obarun.org/66-service/Arch](https://git.obarun.org/66-service/Arch) (Many frontend files will soon be packaged, soon. In the 66-svmgr overlay mentioned above in the wiki.)

Some more caveats with paths in scripts, and the general working of 66, exist; They are not yet fully found.

## [Tips]

### [Daemons which stubbornly doublefork]

66 uses s6 for supervision, which requires that daemons when started *don\'t* ever doublefork\...

Most daemons which doublefork, have an option to disable that. But some daemons are too stubborn.

\[[s6-fghack](https://www.skarnet.org/software/s6/s6-fghack.html)\] is a program which handles this for almost all such daemons.

It opens lot of pipes, and runs the daemon. It can track the daemon(s) via those pipes, and itself exits with (an approximation of) the same exitcode, to signal s6 to restart the daemon.

To use it, just prepend **s6-fghack** in **Execute=()\`\`\`\... like** Execute=( s6-fghack /usr/bin/your-daemon \$ )

### [][dbus-broker (yes, without systemd)]

If useflag **dbus** is enabled for [[[sys-apps/66-tools::66-svmgr]](https://packages.gentoo.org/packages/sys-apps/66-tools::66-svmgr)[]], it will come with an additional binary **66-dbus-launch**.

This is the \"launcher\" for [[[sys-apps/dbus-broker]](https://packages.gentoo.org/packages/sys-apps/dbus-broker)[]], a more efficient dbus-daemon. Be sure to disable \"launcher\" useflag on that package, as that pulls in **systemd**.

It will use either [[[sys-auth/elogind]](https://packages.gentoo.org/packages/sys-auth/elogind)[]] or [[[sys-libs/basu]](https://packages.gentoo.org/packages/sys-libs/basu)[]], based on your **elogind** useflag.

**66-dbus-launch** will write the dbus activation environment to a file, which can be read by **execl-envfile**. It creates 66 frontends from the D-BUS Service files, in the sysadmin/user configuration directories, which apply the dbus activation environment and then execute the dbus-activatable daemons\...

When it receives instructions to activate a d-bus-activatable daemon, it asks 66 to start that daemon, via the frontends\...

All frontends generated here have **InTree=dbus**, thus they neatly get added into the **dbus** tree.

### [syslog]

syslog is generally *not* needed in a s6/66 system, as **s6-log** instances (1 per each service) handle the logs from stdout/stderr. (Most 66 frontends configure the daemons to log to stderr and disable syslog to the extent possible.)

You can safely skip even acknowledging the existence of such a thing, and have your system work fine with every line of log stored. 99% of systems using s6/66 *don\'t* need it.

However, *some* daemons (or even CLI tools) stubbornly use the syslog protocol. No CLI switch. No conf. Just hardcoded to log via that protocol. For those rare daemons, you can set up a shim **s6-socklog** which uses **s6-log** underneath. But everything goes to a single log file. (This is the case anyways even on systems where syslog is the only logger, so fine)

(Other syslog daemons are supported but no frontend file yet; Kindly use this s6-socklog file for reference) \[[s6-socklog](https://www.skarnet.org/software/s6/s6-socklog.html)\] is a small daemon in the s6 suite which is effectively a syslog daemon when combined with **s6-log**.

It listens on the syslog socket, and reads the logs sent to it. But, it doesn\'t do *any* processing on the logs. It just prints them to stdout. The stdout is to be piped to an instance of **s6-log** which does the actual logging and filtering.

The **s6-socklog** frontend is ready, except for restricted privileges. It will be shipped in a package soon. In the meanwhile, you can manually write it:

[FILE] **`/etc/66/service/s6-socklog`s6-socklog frontend for 66**

    [Main]
    Type = classic
    Description = "A simple syslog daemon relying on s6-log for filtering and on-disk saving"
    Version = 2.13.1
    User = ( root )
    Notify = 3
    Provide = ( syslog )
    Flags = ( earlier )

    [Start]
    Execute=(
        s6-socklog -d 3 -x $ -l $
    )

    [Logger]
    # No. of total clean (not half-written) files other than the currently-used to keep
    Backup = 5
    # Maximum size of the logfile before rotation
    MaxSize = 1000000
    # Where to save the logs; it is a directory with the state and logfiles
    Destination = /var/log/socklog
    # You might like to leave /var/log alone as they are files rather than a directory which s6-log uses.

    [Environment]
    # The syslog datagram socket to listen on
    syslogSockDatagram=!/dev/log
    # Maximum lines in a single "log" message
    linelen=!1024

** Note**\
s6-log is a powerful filtering and splitting tool, but it\'s primarily designed to exclusively log *one* context like just one service, or as a \"miscellaneous\" logger, not as a single logger meant to log multiple services to multiple files like syslog.

Anyways in **66** all services are assigned dedicated **s6-log** loggers and encouraged to output to stdout/stderr, so this is kind of a \"miscellaneous\" shim for the few uncooperative services. If you seriously want to match against huge sets of regexp definitions etc\... and log to multiple files, use a real syslog daemon.

Personally I recommend busybox\'s (after s6-socklog) as it\'s the only one I know to have built-in (thus race-free) log rotation based on size growth rather than timed intervals, similar to s6-log.

A frontend for using busybox-syslog is available on the alpine\'s frontend repository: [https://git.obarun.org/66-service/alpine/busybox-daemons/-/blob/master/frontends/busybox-syslogd](https://git.obarun.org/66-service/alpine/busybox-daemons/-/blob/master/frontends/busybox-syslogd)

Run the below command to configure some daemon-specific and rotation options:

`root `[`#`]`66 configure busybox-syslog`

But [/etc/syslog.conf] is where you configure the filtering via regex and manitain multiple log files\...

## [Troubleshooting]

### [Unmerge]

`root `[`#`]`emerge --ask --depclean --verbose sys-apps/66-boot::66-svmgr`

## [See also]

-   [S6](https://wiki.gentoo.org/wiki/S6 "S6") --- a package that provides a [daemontools-inspired](https://wiki.gentoo.org/wiki/Daemontools "Daemontools") process supervision suite, a notification framework, a UNIX domain super-server, and tools for file descriptor holding and suidless privilege gain.

## [External resources]

-   [The 66 suite of software](https://web.obarun.org/software) -- 66, 66-tools, etc\...

## [References]