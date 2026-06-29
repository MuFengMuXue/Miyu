**Resources**

[[]][Package information](https://packages.gentoo.org/packages/sys-apps/openrc)

**[/etc/local.d/]** can contain small programs or light scripts to be run when the local service is started or stopped. The local service is part of [OpenRC](https://wiki.gentoo.org/wiki/OpenRC "OpenRC").

Scripts in [/etc/local.d/] with the suffix [.start] will be executed at boot time, scripts with suffix [.stop] at shutdown time. Scripts should have the execute permission. Files are processed in lexical order.

** Warning**\
The local service is intended to execute just a few [*very light*] commands and terminate. Read and understand this rest of this section before use.

This system is intended only for very light scripts that will terminate quickly, and are at no risk of hanging, e.g. to write a value to a file in [/proc/].

The local service is not considered started or stopped until everything is processed, so if there is a [.start] or [.stop] process which takes some time to run, it can delay - possibly even freeze - boot or shutdown.

[*This infrastructure should not be used to start other scripts or programs in the background.*] If the [/etc/init.d/local] service script is restarted several times, then those scripts or programs will be started in the background several times, possibly resulting in race conditions. A [.stop] script for terminating background processes started this way would be needed, but may easily fail, e.g. if the [.start] script had been executed several times.

** Note**\
To start a process in the background, write an OpenRC initscript file, as described in the [OpenRC Initscripts section](https://wiki.gentoo.org/wiki/Handbook:AMD64/Working/Initscripts#Writing_initscripts "Handbook:AMD64/Working/Initscripts") of the Gentoo Handbook.

## Contents

-   [[1] [Configuration]](#Configuration)
-   [[2] [Usage]](#Usage)
    -   [[2.1] [Invocation]](#Invocation)
    -   [[2.2] [Add local service to default runlevel]](#Add_local_service_to_default_runlevel)
-   [[3] [Troubleshooting]](#Troubleshooting)
-   [[4] [See also]](#See_also)

## [Configuration]

Here is a script simply as an example of what can be put in [/etc/local.d/]. This script will set parameters for the cpu governor, it is a good candidate to be used with the local service as it simply writes to some files in proc and terminates:

[FILE] **`/etc/local.d/cpu_governor.start`**

    #!/bin/bash

    #set cpu governors to "performance"
    for c in $(ls -d /sys/devices/system/cpu/cpu[0-9]*); do echo performance >$c/cpufreq/scaling_governor; done

** Note**\
Remember to mark the script as executable:

`root `[`#`]`chmod +x /etc/local.d/<scriptname>.<start|stop>`

## [Usage]

### [Invocation]

The local service will usually be started on boot by adding it to the default runlevel (see the next section), however it can be started explicitly:

`root `[`#`]`rc-service local start`

If the local service is in the default runlevel, but stopped, it can be started by having OpenRC check for stopped services:

`root `[`#`]`openrc`

### [Add local service to default runlevel]

To start the [local.d] scripts at boot time, add it to the default runlevel:

`root `[`#`]`rc-update add local default`

## [Troubleshooting]

By default, the local service will silence all output. Adding [-v] option to rc-service will cause it to show which scripts were run and their output, if any:

`root `[`#`]`rc-service local restart -v`

## [See also]

-   [OpenRC](https://wiki.gentoo.org/wiki/Openrc "Openrc") --- a dependency-based [init system](https://en.wikipedia.org/wiki/Init "wikipedia:Init") for Unix-like systems that maintains compatibility with the system-provided [init system](https://wiki.gentoo.org/wiki/Init_system "Init system")