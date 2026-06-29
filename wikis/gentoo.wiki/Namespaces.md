[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=Namespaces&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

Linux **namespaces** wrap system resources, making processes within that namespace appear to have isolated instances of that resource. Changes can be made within the namespace that will not be visible outside, on the system.

## Contents

-   [[1] [Namespace types]](#Namespace_types)
-   [[2] [Interacting with user namespaces]](#Interacting_with_user_namespaces)
    -   [[2.1] [Checking current ID maps]](#Checking_current_ID_maps)
    -   [[2.2] [Creating a new namespace]](#Creating_a_new_namespace)
    -   [[2.3] [Creating a new namespace with outside user privileges]](#Creating_a_new_namespace_with_outside_user_privileges)
    -   [[2.4] [Entering an existing namespace]](#Entering_an_existing_namespace)
-   [[3] [See also]](#See_also)
-   [[4] [External resources]](#External_resources)

## [Namespace types]

The following namespaces are available in Linux:

-   Cgroup - Provides a new Cgroup root directory for the process.
-   IPC - Provides System V IPC and POSIX message queues.
-   Network - Isolated network devices, IP stacks, routing tables, firewall rules, used ports, UNIX sockets, and more.
-   Mount - Isolated [mount] records for the process, providing distinct single-directory hierarchies.
-   PID - Provides a new PID tree, starting at 1 like a typical Linux system.
-   Time - Provides 2 virtual clocks for the process: `CLOCK_MONOTONIC`, and `CLOCK_BOOTTIME`.
-   User - Provides isolated user security identifiers and attributes, such as: UIDs, GIDs, keyrings, capabilities.
-   UTS - Isolates the process\' *hostname* and *NIS domain name* using [sethostname] and [setdomainname].

** Tip**\
For each namespace type, there is a man page, ex: [man mount_namespaces] or [man user_namespaces].

## [Interacting with user namespaces]

*User* namespaces, or namespaces where UID/GIDs are mapped, can be used to act as the root UID without elevated privilages.

### [Checking current ID maps]

The current UID/GID maps can be set or edited using [/proc/\$\$/uid_map] and [/proc/\$\$/gid_map].

`user `[`$`]`cat /proc/$$/uid_map`

             0          0 4294967295

** Tip**\
`$$` should resolve to the shell\'s PID. Any PID can be used to check uid/gid maps for a running process.

### [Creating a new namespace]

To create a new user namespace, mapped to the **root** user and group within the namespace:

`user `[`$`]`unshare --map-auto -S 0 -G 0`

This new shell session has the following mapped UIDs:

`root `[`#`]`cat /proc/$$/uid_map`

             0     100000      65536

** Important**\
This does not map any UIDs within this namespace to ones on the host system, including the user running unshare.

### [Creating a new namespace with outside user privileges]

To create a new shell session where **root** inside is mapped to the user running the command outside:

`user `[`$`]`unshare --map-auto --map-root`

** Tip**\
This can be set to an alias like `alias nsudo="unshare --map-auto --map-root "`.

This new shell session has the following mapped UIDs:

`root `[`#`]`cat /proc/$$/uid_map`

             0       1000          1
             1     100000      65536

### [Entering an existing namespace]

If a process is already running in a namespace, [nsenter] can be used to interact with it.

To get root user context within a namespace running on PID **12345**:

`user `[`$`]`nsenter --target 12345 --setuid 0 --setgid 0 --user`

** Tip**\
A command can be specified with [nsenter], but if one is not specified, it will start a shell specified by **\$**.

## [See also]

-   [Cgroups](https://wiki.gentoo.org/wiki/Cgroups "Cgroups") --- allow securely managing the system resource usage of processes

## [External resources]

-   [[[namespaces(7)]](https://man.archlinux.org/man/namespaces.7.en)[[]](https://wiki.gentoo.org/wiki/Special:MyLanguage/man_page "Special:MyLanguage/man page")] - man page for an overview of Linux namespaces
-   [Wikipedia article on Linux namespaces](https://en.wikipedia.org/wiki/Linux_namespaces "wikipedia:Linux namespaces")