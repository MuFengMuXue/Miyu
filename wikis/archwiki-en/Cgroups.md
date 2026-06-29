# Cgroups

Control groups (or cgroups as they are commonly known) are a feature provided by the Linux kernel to manage, restrict, and audit groups of processes. Compared to other approaches like the  command or , cgroups are more flexible as they can operate on (sub)sets of processes (possibly with different system users).

Control groups can be accessed with various tools:

* using directives in systemd unit files to specify limits for services and slices;
* by accessing the  filesystem directly;
* via tools like ,  and  (part of the  and  packages);
* using the "rules engine daemon" to automatically move certain users/groups/commands to groups ( and ) (part of the  and  packages); and
* through other software such as Linux Containers (LXC) virtualization.

For Arch Linux, systemd is the preferred and easiest method of invoking and configuring cgroups as it is a part of the default installation.

## Installing
Make sure you have one of these packages installed for automated cgroup handling:

*  - for controlling resources of a systemd service.
* ,  - set of standalone tools (, , persistence via ).

## With systemd
## Hierarchy
Current cgroup hierarchy can be seen with  or  command.

## Find cgroup of a process
The cgroup name of a process can be found in .

For example, the cgroup of the shell:

## cgroup resource usage
The  command can be used to see the resource usage:

## Custom cgroups
 systemd unit files can be used to define a custom cgroup configuration.  They must be placed in a systemd directory, such as .  The resource control options that can be assigned are documented in .

This is an example slice unit that only allows 30% of one CPU to be used:

Remember to do a daemon-reload to pick up any new or changed  files.

## As service
## Service unit file
Resources can be directly specified in service definition or as a drop-in file:

 MemoryMax=1G

This example limits the service to 1 gigabyte.

## Grouping unit under a slice
Service can be specified what slice to run in:

## As root
 can be used to run a command in a specific slice.

 # systemd-run --slice=my.slice command

 option can be used to spawn the command as specific user.

 # systemd-run --uid=username --slice=my.slice command

The  option can be used to spawn a command shell inside the slice.

## As unprivileged user
Unprivileged users can divide the resources provided to them into new cgroups, if some conditions are met.

Cgroups v2 must be utilized for a non-root user to be allowed managing cgroup resources.

## Controller types
Not all resources can be controlled by user.

{| class="wikitable"
! Controller !! Can be controlled by user !! Options
|-
| cpu ||  || CPUAccounting, CPUWeight, CPUQuota, AllowedCPUs, AllowedMemoryNodes
|-
| io ||  || IOWeight, IOReadBandwidthMax, IOWriteBandwidthMax, IODeviceLatencyTargetSec
|-
| memory ||  || MemoryLow, MemoryHigh, MemoryMax, MemorySwapMax
|-
| pids ||  || TasksMax
|-
| rdma ||  || ?
|-
| eBPF ||  || IPAddressDeny, DeviceAllow, DevicePolicy
|}

## User delegation
For user to control cpu and io resources, the resources need to be delegated. This can be done with a drop-in file.

For example if your user id is 1000:

Reboot and verify that the slice your user session is under has cpu and io controller:

## User-defined slices
The user slice files can be placed in .

To run the command under certain slice:

 $ systemd-run --user --slice=my.slice command

You can also run your login shell inside the slice:

 $ systemd-run --user --slice=my.slice --shell

## Run-time adjustment
cgroups resources can be adjusted at run-time using  command. Option syntax is the same as in .

For example, cutting off internet access for all user sessions:

 $ systemctl set-property user.slice IPAddressDeny=any

## With libcgroup and the cgroup virtual filesystem
One layer lower than management with systemd is the cgroup virtual file system. "libcgroup" provides a library and utilities for making management easier, so we will use them here as well.

The reason for using the lower level is simple: systemd does not provide an interface for every single interface file in cgroups and nor should it be expected for it to provide them at any point in the future. It is completely harmless to read from them for additional insights on a cgroup's resource use.

## Before using a non-systemd tool...
One cgroup should only have one set of programs writing to it to avoid race conditions, the "single-writer rule". This is not enforced by the kernel, but following this recommendation prevents hard-to-debug issues from happening. To set the boundary at which systemd stops managing child cgroups, see the  property. Otherwise do not be surprised if system to overwrites what you have set.

## Creating ad hoc groups
One of the powers of cgroups is that you can create "ad-hoc" groups on the fly. You can even grant the privileges to create custom groups to regular users.  is the cgroup name:

 # cgcreate -a user -t user -g memory,cpu:groupname

Now all the tunables in the group  are writable by your user:

Cgroups are hierarchical, so you can create as many subgroups as you like. If a normal user wants to make new subgroup called  and distributes memory and cpu controller to the subgrroup:

 $ cgcreate -g memory,cpu:groupname/foo

## Using cgroups
As previously mentioned, only one thing should write to a cgroup at any point. This does not affect non-write operations including spawning new processes inside a group, moving processes to a group, or reading properties from cgroup files.

## Spawning and moving processes
libcgroup contains a simple tool for running new processes inside a cgroup. If a normal user wants to run a  shell under a our previous :

 $ cgexec    -g cpu:groupname/foo bash

Inside of the shell, we can confirm which cgroup it belongs to with:

This makes use of , a file that exists in every process. Manually writing to the file causes the cgroup to change as well.

To move all 'bash' commands to this group:

 $ cgclassify -g cpu:groupname/foo `pidof bash`

Internally (i.e. without  the kernel provides two ways to move processes between cgroups. These two are equivalent:

 $ echo 0::/groupname/foo > /proc/13244/cgroup
 $ echo 13244 > /sys/fs/cgroup/groupname/foo/cgroup.procs

## Manipulating group properties
A new subdirectory is crated for  at its creation, located at . These files can be read and written to change the group's properties. (Again, writing is not recommended unless delegation is done!)

Let us try to see how much memory all the processes in our group is taking up:

To limit the RAM (not swap) usage of all processes, run the following:

 $ echo 10000000 > /sys/fs/cgroup/groupname/foo/memory.max

To change the CPU priority of this group (the default is 100):

 $ echo 10 > /sys/fs/cgroup/groupname/foo/cpu.weight

You can find more tunables or statistics by listing the cgroup directory.

## Persistent group configuration
If you want your cgroups to be created at boot, you can define them in  instead. This causes a service booted at launch to configure your cgroups. See the relevant manual page about the syntax of this file; we will make no instruction on how to use a truly deprecated mechanism.

## Examples
## Restrict memory or CPU use of a command
The following example shows a cgroup that constrains a given command to 2GB of memory.

 $ systemd-run --scope -p MemoryMax=2G --user command

The following example shows a command restricted to 20% of one CPU core.

 $ systemd-run --scope -p CPUQuota="20%" --user command

## Matlab
Doing large calculations in MATLAB can crash your system, because Matlab does not have any protection against taking all your machine's memory or CPU. The following examples show a cgroup that constrains Matlab to first 6 CPU cores and 5 GB of memory.

## With systemd
Launch Matlab like this (be sure to use the right path):

 $ systemd-run --user --slice=matlab.slice /opt/MATLAB/2012b/bin/matlab -desktop

## Documentation
* For information on controllers and what certain switches and tunables mean, refer to kernel's documentation [https://docs.kernel.org/admin-guide/cgroup-v2.html v2 (or install  and see )
* Linux manual page:
* A detailed and complete Resource Management Guide can be found in the Red Hat Enterprise Linux documentation.
For commands and configuration files, see relevant man pages, e.g.  or

## Historical note: cgroup v1
Before our current cgroup v2 there was an earlier version called v1. V1 allowed a lot of additional flexibility including a non-unified hierarchy and thread-granular management. This was, in retrospect, a bad idea (see the rationales for v2):
* Even though many hierarchies can exist and processes can be bound to several hierarchies, a controller can ever be used in one hierarchy. This makes the many hierarchies essentially pointless, with the usual setup being to bind each controller to one hierarchy (e.g. ), then each process to multiple hierarchies. This in turn made tools like  essential for syncing the membership of processes across multiple hierarchies.
* Thread-granular management caused cgroup to be abused as a way for a process to manage itself. The proper way to do this is through system calls, not the convoluted interfaces that have emerged to support this use. Self-managing requires clunky string management and is inherently vulnerable to race conditions.

To avoid further chaos, cgroup v2 has two key design rules on top of the removal of features:
* If a cgroup has child cgroups, it cannot have attached processes (with the exception of the root cgroup). This is enforced on v2 and helps make the single-writer rule (below) viable.
* Each cgroup should only have one process managing it at the same time (single-writer rule). This is not enforced anywhere but should be respected at most times to avoid pain from software fighting each other over what to do to a group.
** On systemd systems, the root cgroup is managed by systemd, making any change not by systemd a violation of this rule (or, as it's not enforced, recommendation), unless when  is set on the surrounding service or scope unit to tell systemd to not meddle with what is inside.

Before systemd v258, the kernel parameters  could be used to force booting with cgroup-v1 (the first parameter was added in v256 to make it harder to use cgroup-v1). However, this feature has now been removed. It is still worth knowing about because some software like to put  in your kernel command-line without telling you, causing your entire system to break.
