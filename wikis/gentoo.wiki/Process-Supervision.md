**Process supervision** is the ability to manage (long lived) processes or rather *daemons* and be able to get (automated) process restart if needed, be it a process crash or signal misuse.

There are currently four well known implementations using the same API: [Daemontools](https://wiki.gentoo.org/wiki/Daemontools "Daemontools"), [Daemontools-encore](https://wiki.gentoo.org/wiki/Daemontools-encore "Daemontools-encore"), [Runit](https://wiki.gentoo.org/wiki/Runit "Runit"), and [S6](https://wiki.gentoo.org/wiki/S6 "S6"). The two later suites can also be used as [init](https://wiki.gentoo.org/wiki/Comparison_of_init_systems "Comparison of init systems") PID 1 replacement. Although the latter case, [S6](https://wiki.gentoo.org/wiki/S6 "S6") that is, is left to the distribution or operating system implementation.

## Contents

-   [[1] [Rationale]](#Rationale)
-   [[2] [Implementation]](#Implementation)
    -   [[2.1] [OpenRC\'s supervise-daemon]](#OpenRC.27s_supervise-daemon)
    -   [[2.2] [Damontools]](#Damontools)
    -   [[2.3] [Daemontools-encore]](#Daemontools-encore)
    -   [[2.4] [Runit]](#Runit)
    -   [[2.5] [S6]](#S6)
    -   [[2.6] [Supervisor]](#Supervisor)
-   [[3] [Supervision scripts]](#Supervision_scripts)
-   [[4] [OpenRC supervision backend]](#OpenRC_supervision_backend)
-   [[5] [OpenRC supervision service]](#OpenRC_supervision_service)
    -   [[5.1] [Local service]](#Local_service)
    -   [[5.2] [System service]](#System_service)
-   [[6] [See also]](#See_also)
-   [[7] [External resources]](#External_resources)

## [Rationale]

There is certainly the need of process management and supervision in order to ensure the availability of certain functionalities in the Operating System. Without daemontools\[-encore\], runit and s6 supervision model, this is done with some dirty and less dirty hacks which involve managing PID files of (child) processes to be able to start/stop (child) processes when necessary. Current process management implementation---start-stop-daemon (*ssd* for short)---in OpenRC uses this scheme with some known flaws like positive false PID acquisition with a kind of racy start up.

This is where enter process supervision which normally have a direct feedback link with child process. Well, the daemontools API supervision family start child processes in the foreground,---instead of the background for SSD implementation,---for this end with a foreground (hack) utility is used if necessary,---usualy named *fghack*,---to achieve this feast with (*bad*) daemons.

However, the supervision advocates tend to advocate a complete system supervision, meaning that, every daemon in the system is supervised. Does this really fit well in every use case? Or is it safe to supervise every daemon in every environment? Even in a server oriented one? Supervision advocates would say *yes*. And the process supervisor overhead seems to be a non issue because it has small resources foot print.

See the end of the article for an OpenRC supervision backend\... still being worked on.

## [Implementation]

### [][OpenRC\'s supervise-daemon]

[OpenRC/supervise-daemon](https://wiki.gentoo.org/wiki/OpenRC/supervise-daemon "OpenRC/supervise-daemon")

### [Damontools]

[Daemontools](https://wiki.gentoo.org/wiki/Daemontools "Daemontools")

### [Daemontools-encore]

See [Daemontools-encore](https://wiki.gentoo.org/wiki/Daemontools-encore "Daemontools-encore") main article for more info.

### [Runit]

See [Runit](https://wiki.gentoo.org/wiki/Runit "Runit") main article for more info.

### [S6]

See [S6](https://wiki.gentoo.org/wiki/S6 "S6") main article for more info.

### [Supervisor]

Python folks intake on supervision following daemontools steps.

[Supervisor](https://wiki.gentoo.org/index.php?title=Supervisor&action=edit&redlink=1 "Supervisor (page does not exist)")

------------------------------------------------------------------------

## [Supervision scripts]

A supervision scripts [framework](https://github.com/tokiclover/supervision-scripts) inspired by the original *supervision-scripts*, see [#External Resources](#External_Resources), by Avery Payne is available. This framework aims to get a KISS supervision suite which work out of the box with an almost empty service directory and log directory: a symlink of *sv/SERVICE/run* to *sv/.opt/run* and *sv/SERVICE/log/run* to *sv/.opt/run-log* would be enough for most cases.

Similarly, getty,---be it agetty, mingetty or fgetty (the latter would require either an edit of the default configuration, or adding a *sv/SERVICE/OPTIONS* configuration file)---work out of the box.

All in all, easy and no environment variable (file) x local (*sv/SERVICE/env*) & global (*sv/.env*) environment directory x (number of) services useless disk seeks! A single *OPTIONS* configuration file for each service is preferred here---with a default (*sv/.opt/SVC_OPTIONS*) configuration file.

OpenRC friendly [Runit](https://wiki.gentoo.org/wiki/Runit "Runit") *stage* 1, 2, and 3 along with a [Ctrl]+[Alt]+[Delete] files are available as well, notwithstanding the compatibility mode offered by setting *RC_OPTS=Yes* in *OPTIONS* configuration file. Some [S6](https://wiki.gentoo.org/wiki/S6 "S6") experimental stage 1, 2 and 3 are available as well.

Tired to (re-)write the same ([./run]) thing over and over again?! Check this out! Do not want to wear out the (system boot) disk for no good reason?! Try it out!

Finally, there is an environment variables file *sv/.opt/SVC_BACKEND* which contains supervision backend commands and signal that can be used to write a *generic* supervisor backend for OpenRC---*generic*, here, means daemontools family *generic API* (runit and s6 included.)

See the following sub-section for more info on an OpenRC supervisor backend.

## [OpenRC supervision backend]

There is a [Runit](https://wiki.gentoo.org/wiki/Runit "Runit") backend for [OpenRC](https://wiki.gentoo.org/wiki/OpenRC "OpenRC") experiment on BGO, see external resources. The major blocker issue is starting a service in a race free conditions in a timely manner and be able to report success or failure of said service which does not fit quite well on the *scan* service directory (*/service/*) model without races. This is true at least for Runit. Maybe putting a *stop* file in the service directory */service/SERVICE/stop* can help to *start* a service in *down* state and be able to send a *start* or rather *up* command. Still\... this has to be tested.

## [OpenRC supervision service]

This is rather easy to do than the previous supervisor backend, very easy in fact. Simple *local* start/stop scripts for OpenRC can be written quickly for this end. Or else, a more elaborate init service script could be written and added to possibly *boot* or *default* run level.

See Supervision Scripts Framework on External Resources for such (*stage-2 alike*) script and/or [Runit](https://wiki.gentoo.org/wiki/Runit "Runit") article for a *local* init service script variant.

### [Local service]

See [Runit#Local Service](https://wiki.gentoo.org/wiki/Runit#Local_Service "Runit") for an example.

### [System service]

A *generic* system service can be done in a few seconds, and thus, be used for any supervision backend along the lines of the following.

[FILE] **`/etc/init.d/supervision`Supervision-Service**

    #!/sbin/openrc-run
    #
    # $License: Public Domain                                Exp $
    #

    command="$"
    command_args="$"
    pidfile="/run/$.pid"
    command_background="Yes"
    description="Supervision Daemon Service"

    depend()

    stop_pre()  $ "$"/*
        eend "$?"
        return 0
    }

A short configuration file is necessary to select a supervision backend to use.

[FILE] **`/etc/conf.d/supervision`Service-Configuration-File**

    # '/service/' directory to use
    SV_RUNDIR=/etc/service
    # Supervisor to use
    SV_CMD=svscan
    SV_OPTS="$"
    # Service utility to use
    SVC_CMD=svc
    SVC_OPTS="-x"

** Note**\
Notice that, this service use daemontools\[-encore\] as a supervision backend, so adapt it to another backend, if necessary, before adding the service to *boot* or *default* run level.

See [Runit#System Service](https://wiki.gentoo.org/wiki/Runit#System_Service "Runit") for another implementation.

## [See also]

-   [Daemontools](https://wiki.gentoo.org/wiki/Daemontools "Daemontools") --- a collection of tools for managing UNIX services
-   [Daemontools-encore](https://wiki.gentoo.org/wiki/Daemontools-encore "Daemontools-encore") --- a backwards compatible, enhanced version of [Daniel J. Bernstein\'s daemontools package](https://wiki.gentoo.org/wiki/Daemontools "Daemontools"), written by Bruce Guenter.
-   [Runit](https://wiki.gentoo.org/wiki/Runit "Runit") --- lightweight process supervision suite, originally inspired by [daemontools](https://wiki.gentoo.org/wiki/Daemontools "Daemontools") that offers fast and reliable service management.
-   [S6](https://wiki.gentoo.org/wiki/S6 "S6") --- a package that provides a [daemontools-inspired](https://wiki.gentoo.org/wiki/Daemontools "Daemontools") process supervision suite, a notification framework, a UNIX domain super-server, and tools for file descriptor holding and suidless privilege gain.

## [External resources]

-   [OpenRC friendly Supervision Scripts Framework](https://github.com/tokiclover/supervision)
-   [Init & Supervision Forums Thread](http://forums.gentoo.org/viewtopic-t-994548.html)
-   [Runit Supervisor Backend for OpenRC](https://bugs.gentoo.org/show_bug.cgi?id=501364)
-   [Runit Forums Thread with Supervision discussion](http://forums.gentoo.org/viewtopic-t-1007648.html)
-   [Socket Activation Requirement?](http://www.skarnet.org/software/s6/socket-activation.html)
-   [Why Process Supervision (at all?)](http://www.skarnet.org/software/s6/why.html)