This article describes some configuration options available for system administrators to help manage [Portage](https://wiki.gentoo.org/wiki/Portage "Portage")\'s resource usage.

** Note**\
Starting with sys-apps/portage-3.0.35, the preferred way to de-prioritize Portage build jobs is by using [scheduling policy](#Scheduling_policy) configuration.

## Contents

-   [[1] [Scheduling policy]](#Scheduling_policy)
    -   [[1.1] [Configuration]](#Configuration)
-   [[2] [Portage \"niceness\"]](#Portage_.22niceness.22)
    -   [[2.1] [Priority and nice values]](#Priority_and_nice_values)
    -   [[2.2] [Controlling priority]](#Controlling_priority)
    -   [[2.3] [Configuration]](#Configuration_2)
-   [[3] [See also]](#See_also)

## [Scheduling policy]

** Tip**\
The scheduling policy control is supported starting with sys-apps/portage-3.0.35

** Note**\
musl doesn\'t support scheduling policies. See [[[bug #904502]](https://bugs.gentoo.org/show_bug.cgi?id=904502)[]].

Using Portage\'s scheduling policy, it is possible to define what scheduling policy the Linux [kernel](https://wiki.gentoo.org/wiki/Kernel "Kernel") will apply to [[emerge](https://wiki.gentoo.org/wiki/Emerge "Emerge")] itself and all the build jobs. System administrators who wish to minimize Portage\'s impact on system responsiveness should set scheduling policy to `idle`. This will *significantly reduce* the disruption to the rest of the system by scheduling Portage processes as extremely low priority. The `idle` policy is order of magnitude lower than anything running with `PORTAGE_NICENESS` set to level of `19`.

### [Configuration]

To set the `idle` scheduling policy:

[FILE] **`/etc/portage/make.conf`Set `PORTAGE_SCHEDULING_POLICY` to idle**

    # Extremely low priority
    PORTAGE_SCHEDULING_POLICY="idle"

** Important**\
The `idle` scheduling policy does *not* support nice levels, meaning `PORTAGE_SCHEDULING_POLICY` can be set to `idle` to then omit setting the `PORTAGE_NICENESS` variable all together.

The supported options are:

-   `other`
-   `batch`
-   `idle`
-   `fifo`
-   `round-robin`

See the [**sched(7)**](https://man7.org/linux/man-pages/man7/sched.7.html) man page for more information on scheduler options.

For more information about Portage\'s scheduling ability, search for `PORTAGE_SCHEDULING_POLICY` in [man 5 make.conf].

## [][Portage \"niceness\"]

** Note**\
If `PORTAGE_SCHEDULING_POLICY` is set to `idle`, as preferred and described in the previous section, this section is not needed.

### [Priority and nice values]

The priority value (PR) of a process ranges from 0 to 139, giving high to low priority respectively. Real time process occupy 0 to 99 and user processes range of 100 to 139.

User process priority is defined in terms of the nice level (NI) plus 20 (*NI + 20*). The nice level therefore ranges from -20 to 19, which corresponds to a user process priority of 0 to 39 and a PR value of 100 to 139. For example, giving a process a nice value of 0 translates into a PR of 120.

### [Controlling priority]

Linux has a few options to control system responsiveness by limiting a process\' use of resources, including [nice] (which is POSIX, not Linux-exclusive), [ionice], and [chrt]. The interaction between these is complicated and it\'s usually hard to reason about.

In short:

-   [nice] controls priority with regard to the CPU scheduler
-   [ionice] controls priority with regard to the disk I/O scheduler
-   [chrt] is like an extended [nice] - it can change attributes of the process(es) which the CPU scheduler utilizes, rather than just the simplistic \'niceness\' level, like priority/task *class*.

Resources online also cover the [distinction](https://serverfault.com/questions/161008/what-is-the-difference-between-renice-and-chrt-commands-in-linux) between [nice] and [chrt].

In any case, all three are valuable tools in making Portage run smoothly in the background without interfering with general system usage from other processes. Anecdotally, [chrt] seems to make the most difference.

### [Configuration]

** Note**\
The [/etc/portage/make.conf] variables mentioned here don\'t allow running multiple commands by themselves, so if desired, PORTAGE_IONICE_COMMAND can point to a wrapper script. This issue is tracked as [[[bug #565418]](https://bugs.gentoo.org/show_bug.cgi?id=565418)[]].

Enable `PORTAGE_SCHEDULING_POLICY`, `PORTAGE_NICENESS`, and `PORTAGE_IONICE_COMMAND` in [/etc/portage/make.conf]:

[FILE] **`/etc/portage/make.conf`**

    # Extremely low priority (per above)
    PORTAGE_SCHEDULING_POLICY="idle"
    # Lowest priority
    PORTAGE_NICENESS="19"
    PORTAGE_IONICE_COMMAND="ionice -c 3 -p \$"

## [See also]

-   [EMERGE_DEFAULT_OPTS](https://wiki.gentoo.org/wiki/EMERGE_DEFAULT_OPTS "EMERGE DEFAULT OPTS") --- a variable for [Portage](https://wiki.gentoo.org/wiki/Portage "Portage") that defines entries to be appended to the [emerge] command line.
-   [MAKEOPTS](https://wiki.gentoo.org/wiki/MAKEOPTS "MAKEOPTS") --- a variable that defines and limits how many parallel make jobs can be launched from Portage.
-   [Knowledge Base:Emerge out of memory](https://wiki.gentoo.org/wiki/Knowledge_Base:Emerge_out_of_memory "Knowledge Base:Emerge out of memory")
-   [Portage](https://wiki.gentoo.org/wiki/Portage "Portage") --- the official [package manager](https://en.wikipedia.org/wiki/Package_manager "wikipedia:Package manager") and [distribution system](https://www.gentoo.org/get-started/about/) for Gentoo.
-   [steve](https://wiki.gentoo.org/wiki/Steve "Steve") --- a jobserver implementation for Gentoo