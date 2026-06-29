**[] Deprecated article**\
\
This article is **deprecated (obsolete)**. Contents are [no longer relevant], and are intended for historical reference only!

**lmctfy** was long ago dissolved into other projects ([Docker](https://wiki.gentoo.org/wiki/Docker "Docker"), runc, libcontainer\...)

\
TLDR: **Do not use this article!**

This article explains how to install and configure lmctfy, Google\'s open-source container support. This page is very much a WIP.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [Kernel]](#Kernel)
    -   [[1.2] [Userspace]](#Userspace)
-   [[2] [Configuration]](#Configuration)

## [Installation]

### [Kernel]

A kernel that supports cgroups is required in order to make lmctfy work. The following setup enables lmctfy on linux-3.10.7-gentoo-r1.

[KERNEL]

    [*] General setup  --->
        [*] Control Group support  --->
             [ ] Example debug cgroup subsystem
             [*] Freezer cgroup subsystem
             [ ] Device controller for cgroups
             [*] Cpuset support
             [*]   Include legacy /proc//cpuset file
             [*] Simple CPU accounting cgroup subsystem
             [*] Resource counters
             [*]   Memory Resource Controller for Control Groups
             [*]     Memory Resource Controller Swap Extension
             [*]       Memory Resource Controller Swap Extension enabled by default
             [*]     Memory Resource Controller Kernel Memory accounting
             [*]   HugeTLB Resource Controller for Control Groups
             [ ] Enable perf_event per-cpu per-container group (cgroup) monitoring
             [*] Group CPU scheduler  --->
                 [*] Group scheduling for SCHED_OTHER
                 [*]   CPU bandwidth provisioning for FAIR_GROUP_SCHED
                 [*] Group scheduling for SCHED_RR/FIFO
             [*] Block IO controller
             [ ]   Enable Block IO controller debugging

### [Userspace]

The following code exists in the \"palmer\" overlay, available from [eselect repository](https://wiki.gentoo.org/wiki/Eselect/Repository "Eselect/Repository"):

`root `[`#`]`emerge --ask lmctfy`

## [Configuration]

The following commands setup a simple lmctfy container limeted to 100MB of memory and then proceeds to start a process that attempts to allocate 200MB of memory, which should be killed.

`root `[`#`]`lmctfy init "" `

`root `[`#`]`lmctfy create memory_only "memory:" `

`root `[`#`]`lmctfy run memory_only "memtester 200M" `