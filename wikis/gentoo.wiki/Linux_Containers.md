**Resources**

[[]][Home](https://linuxcontainers.org/)

[[]][Wikipedia](https://en.wikipedia.org/wiki/LXC "wikipedia:LXC")

[[]][GitHub](https://github.com/lxc/lxc)

[[]][Bugs (upstream)](https://github.com/lxc/lxc/issues)

[[]][[#lxc](ircs://irc.libera.chat/#lxc)] ([[webchat](https://web.libera.chat/#lxc)])

**LXC** (Linux Containers) is a [virtualization](https://wiki.gentoo.org/wiki/Virtualization "Virtualization") system that leverages Linux\'s [namespaces](https://wiki.gentoo.org/wiki/Namespaces "Namespaces") and [cgroups](https://wiki.gentoo.org/wiki/Cgroups "Cgroups") to create containers isolated from the host system.

LXC is conceptually similar to [Solaris\'s Zones](https://en.wikipedia.org/wiki/Solaris_Zones "wikipedia:Solaris Zones") and [FreeBSD\'s Jails](https://en.wikipedia.org/wiki/FreeBSD_Jail "wikipedia:FreeBSD Jail"), providing more segregation than a simple [chroot](https://wiki.gentoo.org/wiki/Chroot "Chroot"), without introducing the overhead of hardware virtualization. Unlike [systemd-nspawn](https://wiki.gentoo.org/wiki/Systemd/systemd-nspawn "Systemd/systemd-nspawn") but similarly to other OS-level virtualization technologies on Linux such as [Docker](https://wiki.gentoo.org/wiki/Docker "Docker"), LXC optionally permits containers to be spawned by an unprivileged user.

[LXD](https://wiki.gentoo.org/wiki/LXD "LXD") uses LXC through *liblxc* and its Go binding to help create and manage containers. [Incus](https://wiki.gentoo.org/wiki/Incus "Incus"), a fork of LXD, is also available.

## Contents

-   [[1] [Introduction]](#Introduction)
    -   [[1.1] [Virtualization]](#Virtualization)
        -   [[1.1.1] [Container-based virtualization]](#Container-based_virtualization)
        -   [[1.1.2] [Full virtualization]](#Full_virtualization)
    -   [[1.2] [LXC limitations]](#LXC_limitations)
        -   [[1.2.1] [Isolation]](#Isolation)
        -   [[1.2.2] [Unprivileged Containers]](#Unprivileged_Containers)
        -   [[1.2.3] [Different Operating Systems and Architectures]](#Different_Operating_Systems_and_Architectures)
    -   [[1.3] [LXC components]](#LXC_components)
        -   [[1.3.1] [Control groups]](#Control_groups)
        -   [[1.3.2] [File locations]](#File_locations)
            -   [[1.3.2.1] [Unprivileged locations]](#Unprivileged_locations)
-   [[2] [Installation]](#Installation)
    -   [[2.1] [USE flags]](#USE_flags)
    -   [[2.2] [Kernel]](#Kernel)
    -   [[2.3] [Emerge]](#Emerge)
-   [[3] [Network Configuration]](#Network_Configuration)
    -   [[3.1] [General Parameters]](#General_Parameters)
    -   [[3.2] [Interface Types]](#Interface_Types)
        -   [[3.2.1] [none]](#none)
        -   [[3.2.2] [empty]](#empty)
        -   [[3.2.3] [phys]](#phys)
        -   [[3.2.4] [veth]](#veth)
            -   [[3.2.4.1] [Bridge Mode]](#Bridge_Mode)
            -   [[3.2.4.2] [Router Mode]](#Router_Mode)
        -   [[3.2.5] [vlan]](#vlan)
        -   [[3.2.6] [macvlan]](#macvlan)
            -   [[3.2.6.1] [private mode]](#private_mode)
            -   [[3.2.6.2] [vepa (Virtual Ethernet Port Aggregator)]](#vepa_.28Virtual_Ethernet_Port_Aggregator.29)
            -   [[3.2.6.3] [bridge]](#bridge)
            -   [[3.2.6.4] [passthru]](#passthru)
    -   [[3.3] [DNS Configuration]](#DNS_Configuration)
    -   [[3.4] [Host Configuration]](#Host_Configuration)
        -   [[3.4.1] [OpenRC Netifrc Bridge creation]](#OpenRC_Netifrc_Bridge_creation)
        -   [[3.4.2] [Nftables NAT rules]](#Nftables_NAT_rules)
-   [[4] [Service Configuration]](#Service_Configuration)
    -   [[4.1] [OpenRC]](#OpenRC)
        -   [[4.1.1] [Unified Cgroups for Unprivileged Containers]](#Unified_Cgroups_for_Unprivileged_Containers)
    -   [[4.2] [Systemd]](#Systemd)
        -   [[4.2.1] [Creating User Namespaces for Unprivileged Containers]](#Creating_User_Namespaces_for_Unprivileged_Containers)
-   [[5] [Unprivileged User configuration]](#Unprivileged_User_configuration)
    -   [[5.1] [User Creation]](#User_Creation)
    -   [[5.2] [Network Quota Allocation]](#Network_Quota_Allocation)
    -   [[5.3] [Sub UID and GID mapping]](#Sub_UID_and_GID_mapping)
    -   [[5.4] [Default container configuration creation]](#Default_container_configuration_creation)
-   [[6] [Guest configuration]](#Guest_configuration)
    -   [[6.1] [Guest Filesystem Creation]](#Guest_Filesystem_Creation)
    -   [[6.2] [Template scripts]](#Template_scripts)
        -   [[6.2.1] [Download template]](#Download_template)
        -   [[6.2.2] [Local template]](#Local_template)
            -   [[6.2.2.1] [Create an empty metadata tarball]](#Create_an_empty_metadata_tarball)
            -   [[6.2.2.2] [Import a stage3 tarball]](#Import_a_stage3_tarball)
    -   [[6.3] [Backing Store]](#Backing_Store)
    -   [[6.4] [Mount configuration]](#Mount_configuration)
    -   [[6.5] [TTY configuration]](#TTY_configuration)
    -   [[6.6] [Init configuration]](#Init_configuration)
    -   [[6.7] [Logging configuration]](#Logging_configuration)
        -   [[6.7.1] [File]](#File)
        -   [[6.7.2] [Syslog]](#Syslog)
    -   [[6.8] [Console Logging]](#Console_Logging)
-   [[7] [Usage]](#Usage)
    -   [[7.1] [Starting a container]](#Starting_a_container)
    -   [[7.2] [Stopping a container]](#Stopping_a_container)
    -   [[7.3] [lxc-console]](#lxc-console)
    -   [[7.4] [lxc-attach]](#lxc-attach)
    -   [[7.5] [Accessing the container with sshd]](#Accessing_the_container_with_sshd)
-   [[8] [Troubleshooting]](#Troubleshooting)
    -   [[8.1] [Systemd containers on an OpenRC host]](#Systemd_containers_on_an_OpenRC_host)
    -   [[8.2] [Containters freeze on \'lxc stop\' with OpenRC]](#Containters_freeze_on_.27lxc_stop.27_with_OpenRC)
    -   [[8.3] [newuidmap error]](#newuidmap_error)
    -   [[8.4] [Could not set clone_children to 1 for cpuset hierarchy in parent cgroup]](#Could_not_set_clone_children_to_1_for_cpuset_hierarchy_in_parent_cgroup)
    -   [[8.5] [tee: /sys/fs/cgroup/memory/memory.use_hierarchy: Device or resource busy]](#tee:_.2Fsys.2Ffs.2Fcgroup.2Fmemory.2Fmemory.use_hierarchy:_Device_or_resource_busy)
    -   [[8.6] [lxc-console: no promt / console (may be a temporary as of 2019-10)]](#lxc-console:_no_promt_.2F_console_.28may_be_a_temporary_as_of_2019-10.29)
-   [[9] [See also]](#See_also)
-   [[10] [External resources]](#External_resources)
-   [[11] [References]](#References)

## [Introduction]

### [Virtualization]

Roughly speaking there are two main types of virtualization, container-based virtualization and full virtualization.

#### [Container-based virtualization]

[Container based virtualization](https://en.wikipedia.org/wiki/OS-level_virtualization "wikipedia:OS-level virtualization"), such as LXC or [Docker](https://wiki.gentoo.org/wiki/Docker "Docker"), is very fast and efficient. It\'s based on the premise that an OS kernel provides different views of the system to different running processes. This compartmentalization, sometimes called *thick sandboxing*, can be useful for ensuring access to hardware resources such as CPU and IO bandwidth, whilst maintaining security and efficiency.

Conceptually, containers are very similar to using a *chroot*, but offer far more isolation and control, mostly through the use of *cgroups* and *namespace*s. A *chroot* only provides filesystem isolation, while namespaces can provide network and process isolation. *cgroups* can be used to manage container resource allocation.

** Note**\
Container environments are typically designed to only have what is required for operation, and can be as simple as a single binary.

#### [Full virtualization]

Full virtualization and paravirtualization solutions, such as [KVM](https://wiki.gentoo.org/wiki/KVM "KVM"), [Xen](https://wiki.gentoo.org/wiki/Xen "Xen"), [VirtualBox](https://wiki.gentoo.org/wiki/VirtualBox "VirtualBox"), and [VMware](https://wiki.gentoo.org/wiki/VMware "VMware"), aim to simulate the underlying hardware. This method of virtualization results in an environment which provides more isolation, and is generally more compatible, but requires far more overhead.

### [LXC limitations]

#### [Isolation]

LXC provides better isolation than a chroot, but many resources can be, or are still shared. Root users in privileged containers have the same level of system access as the root user outside of the container, unless ID mapping is in place.

** Important**\
Use *unprivileged* containers whenever possible. All containers run by non-root users are *unprivileged*, containers made by the root user with ID mapping can be *unprivileged*.

If the kernel is built allowing a [Magic SysRQ](https://wiki.gentoo.org/wiki/Magic_SysRQ "Magic SysRQ") with `CONFIG_MAGIC_SYSRQ`, a container could abuse this to perform a Denial of Service.

** Warning**\
Virtualization does very little to mitigate CPU vulnerabilities, or protect access if resources are overshared.

#### [Unprivileged Containers]

By design, unprivileged containers cannot do several things which require privileged system access, such as:

-   Mounting filesystems
-   Creating device nodes
-   Operations against a UID/GID outside of the mapped set
-   Creation of network interfaces

In order to create network interfaces, LXC uses [lxc-user-nic] which uses *setuid-root* to create the network interfaces.

#### [Different Operating Systems and Architectures]

Containers cannot be used to run operating systems or software designed for other architectures or operating systems.

** Note**\
[LXD](https://wiki.gentoo.org/wiki/LXD "LXD") or [Incus](https://wiki.gentoo.org/wiki/Incus "Incus") can use [QEMU](https://wiki.gentoo.org/wiki/QEMU "QEMU") for virtualization, but this doesn\'t use containers.

### [LXC components]

#### [Control groups]

Control Groups are a multi-hierarchy, multi-subsystem resource management / control framework for the Linux kernel. They can be used for advanced resource control and accounting using groups which could apply to one or more processes.

Some of the resources *cgroups* can manage are^[\[1\]](#cite_note-1)^:

-   Memory usage.
-   CPU bandwidth.
-   Filesystem usage.
-   Process limits.
-   Block device IO bandwidth.
-   Miscellaneous Devices.

The user-space access to these new kernel features is a kernel-provided filesystem, known as \'cgroup\'. It is typically mounted at [/sys/fs/cgroup] and provides files similar to [/proc] and [/sys], representing the running environment and various kernel configuration options.

#### [File locations]

LXC information is typically stored under:

-   [/etc/lxc/default.conf] - The default guest configuration file. When new containers are created, these values are added.
-   [/etc/lxc/lxc.conf] - LXC system configuration. See [man lxc.conf].
-   [/etc/lxc/lxc-usernet] - LXC configuration for user namespace network allocations.
-   [/var/lib/lxc//config] - Main guest configuration file.
-   [/var/lib/lxc//rootfs/] - The root of the guest filesystem.
-   [/var/lib/lxc//snaps/] - Guest snapshots.
-   [/var/log/lxc/.log] - Guest startup logs.

\

** Note**\
LXC 1.0 used [/var/lib/lxcsnaps] to store snapshots. This location will be used if it exists, but [/var/lib/lxc//snaps/] is now used.

##### [Unprivileged locations]

When running unprivileged containers, configuration files are loaded from the following locations, based on the user home:

-   [/etc/lxc/default.conf] -\> [\~/.config/lxc/default.conf]
-   [/etc/lxc/lxc.conf] -\> [\~/.config/lxc/lxc.conf]
-   [/var/lib/lxc/] -\> [\~/.local/share/lxc/] - This includes a directory for each guest.

## [Installation]

### [USE flags]

### [USE flags for] [app-containers/lxc](https://packages.gentoo.org/packages/app-containers/lxc) [[]] [A userspace interface for the Linux kernel containment features]

  ----------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------
  [`+caps`](https://packages.gentoo.org/useflags/+caps)             Use Linux capabilities library to control privilege
  [`+tools`](https://packages.gentoo.org/useflags/+tools)           Build and install additional command line tools
  [`apparmor`](https://packages.gentoo.org/useflags/apparmor)       Enable support for the AppArmor application security system
  [`doc`](https://packages.gentoo.org/useflags/doc)                 Add extra documentation (API, Javadoc, etc). It is recommended to enable per package instead of globally
  [`examples`](https://packages.gentoo.org/useflags/examples)       Install examples, usually source code
  [`io-uring`](https://packages.gentoo.org/useflags/io-uring)       Enable the use of io_uring for efficient asynchronous IO and system requests
  [`landlock`](https://packages.gentoo.org/useflags/landlock)       Use Landlock to restrict what the monitor API handlers can do on the system
  [`lto`](https://packages.gentoo.org/useflags/lto)                 Enable Link-Time Optimization (LTO) to optimize the build
  [`man`](https://packages.gentoo.org/useflags/man)                 Build and install man pages
  [`pam`](https://packages.gentoo.org/useflags/pam)                 Add support for PAM (Pluggable Authentication Modules) - DANGEROUS to arbitrarily flip
  [`seccomp`](https://packages.gentoo.org/useflags/seccomp)         Enable seccomp (secure computing mode) to perform system call filtering at runtime to increase security of programs
  [`selinux`](https://packages.gentoo.org/useflags/selinux)         !!internal use only!! Security Enhanced Linux support, this must be set by the selinux profile or breakage will occur
  [`ssl`](https://packages.gentoo.org/useflags/ssl)                 Add support for SSL/TLS connections (Secure Socket Layer / Transport Layer Security)
  [`systemd`](https://packages.gentoo.org/useflags/systemd)         Enable use of systemd-specific libraries and features like socket activation or session tracking
  [`test`](https://packages.gentoo.org/useflags/test)               Enable dependencies and/or preparations necessary to run tests (usually controlled by FEATURES=test but can be toggled independently)
  [`verify-sig`](https://packages.gentoo.org/useflags/verify-sig)   Verify upstream signatures on distfiles
  ----------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-05-03 12:33] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Kernel]

The host\'s kernel must be configured with Control Group, namespace, and virtual networking support:

** Tip**\
Once **LXC** is installed, [lxc-checkconfig] can be used to check if the system has been configured properly.

[KERNEL] **Essential configuration options**

    General setup  --->
       [*] POSIX Message Queues
       [*] Control Group support  --->
          [*] Memory controller
          [*] CPU controller  --->
          [*] Freezer controller
          [*] Cpuset controller
          [*] Device controller
          [*] Simple CPU accounting controller
       [*] Namespaces support  --->
          [*] UTS namespace
          [*] IPC namespace
          [*] User namespace
          [*] PID namespace
          [*] Network namespace
    [*] Networking support  --->
       Networking options  --->
          [*] TCP/IP networking
          [*]  INET: socket monitoring interface
          [*] Network packet filtering framework (Netfilter)  --->
             [*] Advanced netfilter configuration
                 Core Netfilter Configuration  --->
                    [*] Netfilter Xtables support (required for ip_tables)
                    [*]   CHECKSUM target support
                 IP: Netfilter Configuration  --->
                    [*] IP tables support (required for filtering/masq/NAT)
                    [*] iptables NAT support
                    [*]   MASQUERADE target support
          [*] 802.1d Ethernet Bridging
          [*]   VLAN filtering
          [*] 802.1Q/802.1ad VLAN Support
    Device Drivers  --->
       [*] Network device support  --->
          [*] Network core driver support
          [*] MAC-VLAN support
          [*] Virtual ethernet pair device
    File systems  --->
       [*] FUSE (Filesystem in Userspace) support

[CODE] **General support**

    CONFIG_POSIX_MQUEUE=y
    CONFIG_FUSE=y

[CODE] **Control Group support options**

    CONFIG_CGROUPS=y
    CONFIG_MEMCG=y
    CONFIG_CGROUP_SCHED=y
    CONFIG_CGROUP_FREEZER=y
    CONFIG_CGROUP_DEVICE=y
    CONFIG_CGROUP_CPUACCT=y
    CONFIG_CPUSETS=y

[CODE] **Namespace support options**

    CONFIG_NAMESPACES=y
    CONFIG_UTS_NS=y
    CONFIG_IPC_NS=y
    CONFIG_USER_NS=y
    CONFIG_PID_NS=y
    CONFIG_NET_NS=y

[CODE] **Network support options**

    CONFIG_NET=y
    CONFIG_NET_CORE=y
    CONFIG_NETFILTER=y
    CONFIG_NETFILTER_ADVANCED=y
    CONFIG_IP_NF_IPTABLES=y
    CONFIG_IP_NF_NAT=y
    CONFIG_IP_NF_TARGET_MASQUERADE=y
    CONFIG_IP6_NF_TARGET_MASQUERADE=y
    CONFIG_NETFILTER_XTABLES=y
    CONFIG_NETFILTER_XT_TARGET_CHECKSUM=y
    CONFIG_NETFILTER_XT_MATCH_COMMENT=y
    CONFIG_BRIDGE=y
    CONFIG_BRIDGE_VLAN_FILTERING=y
    CONFIG_VLAN_8021Q=y
    CONFIG_MACVLAN=y
    CONFIG_VETH=y
    CONFIG_INET=y
    CONFIG_INET_DIAG=y

### [Emerge]

`root `[`#`]`emerge --ask app-containers/lxc`

** Note**\
By default, **lxc** is not emerged with documentation, this can be included with the *man* **USE** flag.

## [Network Configuration]

LXC provides a variety of network options for containers. Container interfaces are defined with `lxc.net..type`, where *i* is the interface index number.

** Important**\
Creating network configuration for a LXC guest will not create corresponding host interfaces, they must be created manually.

** Note**\
Each **LXC** interface may only have one type, but multiple interfaces can be defined with different indexes.

** Tip**\
If **lxc** was emerged with the *man* **USE** flag, network documentation details can be found in [man lxc.container.conf].

** See also**\
Examples exist at [LXC/Network_examples](https://wiki.gentoo.org/wiki/LXC/Network_examples "LXC/Network examples").

### [General Parameters]

The following configuration options apply to all interface types, and are prefixed with `lxc.net..`:

-   **flags** - Specifies an action to perform on the interface, *up* starts the interface on container creation, otherwise it must manually be started with [ip].
-   **link** - Specifies the host interface the container interface should be associated with.
-   **mtu** - Specifies the container interface MTU.
-   **name** - Defines the name which will be given to the interface within the container.
-   **hwaddrd** - Defines the MAC address which will be allocated to the virtual interface, `X`s in the supplied value will be randomized.
-   **ipv4.address** - Specifies the interface\'s assigned IP address, in ip/cidr format, optionally, a broadcast address can be specified after the cidr to use one [other] than the last value on that network. Ex. `lxc.net.0.ipv4.address = 192.168.123.1 192.168.123.32`.
-   **ipv4.gateway** - Specifies the interface\'s default gateway.

### [Interface Types]

LXC offers a variety of interface types, which can be configured using `lxc.net..type`.

#### [none]

The **none** network type provides *no network isolation or virtualization*, and is comparable to Docker\'s *host* networking mode.

** Important**\
Giving a container access to the host\'s network stack is very powerful, and should be done sparingly.

** Warning**\
If both the container and host use upstart init, [halt] in a container will shut down the host.

** Note**\
This option only works with privileged containers.

#### [empty]

The **empty** interface type starts the container with only a loopback interface, if no other interface is defined, the container should be isolated from the host\'s network.

#### [phys]

The **phys** interface type can be used to give a container access to a single interface on the host system. It must be used along with `lxc.net..link` which specifies the host interface.

[FILE] **`/var/lib/lxc//config`Passing eth0 to the container**

    lxc.net.0.type = phys
    lxc.net.0.flags = up
    lxc.net.0.link = eth0

** Warning**\
Defining the host\'s primary physical Ethernet device as the interface for the container can leave the host without a connection to the Internet.

#### [veth]

The **veth** or *Virtual Ethernet Pair Device* can be used to *bridge* or *route*, specified with `lxc.net..mode`, traffic between the host and container using virtual ethernet devices. The default mode of operation is [Network bridge](https://wiki.gentoo.org/wiki/Network_bridge "Network bridge") mode.

##### [Bridge Mode]

When the `lxc.net..veth.mode` is not specified, *bridge* mode will be used, which generally expects a *link* to be set to a *bridge* interface on the host system with `lxc.net..link`. If this link is not set, *veth* interface will be created in the container but not configured on the host.

[FILE] **`/var/lib/lxc//config`Defining a *veth* device connected to the default *lxcbr0* interface**

    lxc.net.0.type = veth
    lxc.net.0.flags = up
    lxc.net.0.link = lxcbr0

##### [Router Mode]

If `lxt.net..veth.mode = router`, static routes are created between the addresses associated with the specified host link device and the container\'s veth interface. For *privileged* containers, *ARP* and *NDP* entries are proxied between the host interface and the container\'s specified *gateway* interface.

[FILE] **`/var/lib/lxc//config`Defining a *routed veth* device associated with *eth0*.**

    lxc.net.0.type = veth
    lxc.net.0.flags = up
    lxc.net.0.veth.mode = router
    lxc.net.0.link = eth0

#### [vlan]

The **vlan** interface type can be used with a host interface specified with `lxc.net..link` and *VLAN* id specified with `lxc.net..vlan.id`. This type is comparable to the **phys** type, but only the specified *VLAN* is shared.

[FILE] **`/var/lib/lxc//config`Defining a **vlan** device on VLAN 100, interface eth0**

    lxc.net.0.type = vlan
    lxc.net.0.flags = up
    lxc.net.0.link = eth0
    lxc.net.0.vlan.id = 100

#### [macvlan]

The **macvlan** interface type can be used to share a physical interface with the host. A link must be specified with `lxc.net..link`. The mode can be configured with `lxc.net..macvlan.mode` where the default mode is *private* mode.

** Important**\
When using the **macvlan** interface type, network communication between the host and container will not function, because the source and destination interfaces are technically the same, even if the MAC address is different.

##### [private mode]

Setting `lxc.net..macvlan.mode = private` results in a *macvlan* interface which cannot communicate to the devices *upper_dev*, or the interface which the *macvlan* interface is based off of.

[FILE] **`/var/lib/lxc//config`Defining a *private* **macvlan** interface on eth0.100**

    lxc.net.0.type = macvlan
    lxc.net.0.flags = up
    lxc.net.0.link = eth0
    lxc.net.0.macvlan.vlan = 100

** Note**\
`lxc.net..macvlan.mode = private` is optional but can be added for clarity.

##### [][vepa (Virtual Ethernet Port Aggregator)]

Setting `lxc.net..macvlan.mode = vepa` results in a *macvlan* interface which operates similarly to *private* mode, but packets are actually sent to the switch, not virtually bridged. This allows different subinterfaces to communicate with each other using another switch.

** Important**\
The interface must be connected to a switch which supports *hairpin* mode, allowing traffic to be sent back over the interface it came from.

[FILE] **`/var/lib/lxc//config`Defining a *vepa* **macvlan** interface on eth0.100**

    lxc.net.0.type = macvlan
    lxc.net.0.flags = up
    lxc.net.0.macvlan.mode = vepa
    lxc.net.0.link = eth0
    lxc.net.0.macvlan.vlan = 100

##### [bridge]

Setting `lxc.net..macvlan.mode = bridge` results in a *macvlan* interface which only delivers traffic across the bridge, not allowing outbound traffic.

[FILE] **`/var/lib/lxc//config`Defining two *bridge* **macvlan** interfaces on eth0.100**

    lxc.net.0.type = macvlan
    lxc.net.0.flags = up
    lxc.net.0.macvlan.mode = bridge
    lxc.net.0.link = eth0
    lxc.net.0.macvlan.vlan = 100
    lxc.net.0.name = macvlan_bridge0

    lxc.net.1.type = macvlan
    lxc.net.1.flags = up
    lxc.net.1.macvlan.mode = bridge
    lxc.net.1.link = eth0
    lxc.net.1.macvlan.vlan = 100
    lxc.net.1.name = macvlan_bridge1

** Note**\
*bridge* mode can be used with other *macvlan* interfaces in *vepa* mode if used with a *hairpin* capable switch.

##### [passthru]

Only one subinterface can use `lxc.net..macvlan.mode = bridge`, this operates similarly to using *phys* or *vlan* mode, but offers more isolation, since the container doesn\'t actually get access to the physical interface, but the *macvlan* interface which is associated with it.

[FILE] **`/var/lib/lxc//config`Using eth0.100 in *passthru* **macvlan** mode.**

    lxc.net.0.type = macvlan
    lxc.net.0.flags = up
    lxc.net.0.macvlan.mode = passthru
    lxc.net.0.link = eth0
    lxc.net.0.macvlan.vlan = 100

### [DNS Configuration]

DNS settings can be configured by editing [/etc/resolv.conf] within the container like it would be done on a normal system.

### [Host Configuration]

LXC will not automatically create interfaces for containers, even if the container is configured to use something like a bridge on the host.

#### [OpenRC Netifrc Bridge creation]

[Netifrc](https://wiki.gentoo.org/wiki/Netifrc "Netifrc") can be used to create bridges:

[FILE] **`/etc/conf.d/net`**

    bridge_lxcbr0=""
    config_lxcbr0="192.168.78.1/24"

A symbolic link for this interface\'s init unit can be created with:

`root `[`#`]`ln -s net.lo net.lxcbr0`

The bridge can be created with:

`root `[`#`]`rc-service net.lxcbr0 start`

This bridge can be created at boot with:

`root `[`#`]`rc-update add net.lxcbr0`

#### [Nftables NAT rules]

This file will be automatically loaded if using [Nftables#Modular_Ruleset_Management](https://wiki.gentoo.org/wiki/Nftables#Modular_Ruleset_Management "Nftables"), but can be loaded by making the file executable and running it.

[FILE] **`/etc/nftables.rules.d/12-lxc_base.rules`**

    #! /sbin/nft -f

    define lxc_net = 192.168.78.0/24

    table inet nat
      }
    }

** Note**\
The following portion is omitted because it exists as part of the example modular ruleset:

[CODE]

    table inet nat
    }

## [Service Configuration]

### [OpenRC]

To create an init script for a specific container, simply create a symbolic link from [/etc/init.d/lxc] to [/etc/init.d/lxc.guestname]:

`root `[`#`]`ln -s lxc /etc/init.d/lxc.`**`guestname`**

This can be started, then set to start at boot with:

`root `[`#`]`rc-service lxc.`**`guestname`**` `

`root `[`#`]`rc-update add lxc.`**`guestname`**

#### [Unified Cgroups for Unprivileged Containers]

If running unprivileged containers on OpenRC based systems, the `rc_cgroup_mode` must be changed from *hybrid* to *unified* and `rc_cgroup_controllers` must be populated:

[FILE] **`/etc/rc.conf`**

    ...
    rc_cgroup_mode="unified"
    rc_cgroup_controllers="yes"
    ...

** Tip**\
Setting `rc_cgroup_controllers` to \"**yes**\" enables all cgroups.

### [Systemd]

To start a container by name:

`root `[`#`]`systemctl start lxc@`**`guestname`**`.service`

To stop ii, issue:

`root `[`#`]`systemctl stop lxc@`**`guestname`**`.service`

To start it automatically at (host) system boot up, use:

`root `[`#`]`systemctl enable lxc@`**`guestname`**`.service`

#### [Creating User Namespaces for Unprivileged Containers]

Unprivileged containers require cgroups to be delegated in advance. These are not managed by LXC.

`lxc@localhost $``systemd-run --unit=my-unit --user --scope -p "Delegate=yes" -- lxc-start my-container `

** Tip**\
This works similarly for other lxc commands.

It is possible to delegate unprivileged cgroups by creating a systemd unit:

[FILE] **`/etc/systemd/system/user@.service.d/delegate.conf`**

    [Service]
    Delegate=cpu cpuset io memory pids

## [Unprivileged User configuration]

** Important**\
Most of this section describes how to allow particular users to run unprivileged containers. Simply adding ID maps to the root user, and adding these to container configs results in an unprivileged container being made.^[\[2\]](#cite_note-2)^

While it is possible to create a single LXC user to run all unprivileged containers with, it\'s a much better practice to create a LXC user for each container, or groups of related containers.

### [User Creation]

To create a new user, which will be used to run *dnscrypt* containers:

`root `[`#`]`useradd -m -G lxc lxc-dnscrypt`

### [Network Quota Allocation]

** Important**\
By default, unprivileged users cannot use any networking

Allocations for network device access must be made by editing [/etc/lxc/lxc-usernet]:

[FILE] **`/etc/lxc/lxc-usernet`Add allocations for the lxc-dnscrypt user to add 1 veth device on the lxbr0 bridge.**

    lxc-dnscrypt veth lxcbr0 1

### [Sub UID and GID mapping]

Once the user has been created, subUIDs and subGIDs must be mapped.

Current mappings can be checked with:

`user `[`$`]`cat /etc/subuid`

    larry:100000:65536
    lxc-dnscrypt:165536:65536

`user `[`$`]`cat /etc/subgid`

    larry:100000:65536
    lxc-dnscrypt:165536:65536

** Tip**\
A set of 65536 UIDs and GIDs are allocated by default when a new user is created.

### [Default container configuration creation]

LXC does not create user configuration by default, [\~/.config/lxc] may need to be created:

`user `[`$`]`mkdir --parents ~/.config/lxc`

Adding the user ID map information is a good base:

[FILE] **`~/.config/lxc/default.conf`Add user ID maps to the default container configuration file**

    lxc.idmap = u 0 165536 65536
    lxc.idmap = g 0 165536 65536

## [Guest configuration]

### [Guest Filesystem Creation]

To create the base container fileystem, to be imported with the *local* template, emerge can be used:

`root `[`#`]`emerge --verbose --ask --root /path/to/build/dir category/packagename`

** Tip**\
Emerging **\@system** or at the very least, [[[sys-libs/glibc]](https://packages.gentoo.org/packages/sys-libs/glibc)[]] makes sense in most cases.

Once the build has completed, it can be archived with:

`root `[`#`]`tar -cJf rootfs.tar.xz -C /path/to/build/dir .`

** Tip**\
`-J` can be replaced with `-I 'xz -9 -T0'` to set the compression level to **9** and use all available threads.

### [Template scripts]

A number of *template scripts* are distributed with the LXC package. These scripts assist with generating various guest environments.

Template scripts exist at [/usr/share/lxc/templates] as bash scripts, but should be executed via the [lxc-create] tool as follows:

`root `[`#`]`lxc-create -n `*`guestname`*` -t `*`template-name`*` -f `*`configuration-file-path`*

** Tip**\
Template files start with *lxc-* but this is not included when using the **-t** argument.

** Note**\
The root filesystem of Linux container, once created, is stored in [/var/lib/lxc/guestname/rootfs].

#### [Download template]

The **download** template is the easiest and most commonly used template, downloading a container from a repository.

Using **download** as the *template-name* displays a list of available guest environments to download and saves the guest image in [/var/lib/lxc].

Available containers can be viewed with:

`root `[`#`]`sudo lxc-create -t download -n alpha -- --list`

[Downloading the image index ]

\-\-- DIST RELEASE ARCH VARIANT BUILD \-\-- almalinux 8 amd64 default 20230815_23:08 almalinux 8 arm64 default 20230815_23:08 almalinux 9 amd64 default 20230815_23:08 almalinux 9 arm64 default 20230815_23:08 alpine 3.15 amd64 default 20230816_13:00 alpine 3.15 arm64 default 20230816_13:00 alpine 3.16 amd64 default 20230816_13:00 alpine 3.16 arm64 default 20230816_13:00 alpine 3.17 amd64 default 20230816_13:00 alpine 3.17 arm64 default 20230816_13:00 alpine 3.18 amd64 default 20230816_13:00 alpine 3.18 arm64 default 20230816_13:00 alpine edge amd64 default 20230816_13:00 alpine edge arm64 default 20230816_13:00 alt Sisyphus amd64 default 20230816_01:17 alt Sisyphus arm64 default 20230816_01:17 alt p10 amd64 default 20230816_01:17 alt p10 arm64 default 20230816_01:17 alt p9 amd64 default 20230816_01:17 alt p9 arm64 default 20230816_01:17 amazonlinux current amd64 default 20230816_05:09 amazonlinux current arm64 default 20230816_05:09 apertis v2020 amd64 default 20230816_10:53 apertis v2020 arm64 default 20230816_10:53 apertis v2021 amd64 default 20230816_10:53 apertis v2021 arm64 default 20230816_10:53 archlinux current amd64 default 20230816_04:18 archlinux current arm64 default 20230816_04:18 busybox 1.34.1 amd64 default 20230816_06:00 busybox 1.34.1 arm64 default 20230816_06:00 centos 7 amd64 default 20230816_07:08 centos 7 arm64 default 20230816_07:08 centos 8-Stream amd64 default 20230816_07:49 centos 8-Stream arm64 default 20230816_07:08 centos 9-Stream amd64 default 20230815_07:08 centos 9-Stream arm64 default 20230816_07:50 debian bookworm amd64 default 20230816_05:24 debian bookworm arm64 default 20230816_05:24 debian bullseye amd64 default 20230816_05:24 debian bullseye arm64 default 20230816_05:24 debian buster amd64 default 20230816_05:24 debian buster arm64 default 20230816_05:24 debian sid amd64 default 20230816_05:24 debian sid arm64 default 20230816_05:24 devuan beowulf amd64 default 20230816_11:50 devuan beowulf arm64 default 20230816_11:50 devuan chimaera amd64 default 20230816_11:50 devuan chimaera arm64 default 20230816_11:50 fedora 37 amd64 default 20230816_20:33 fedora 37 arm64 default 20230816_20:33 fedora 38 amd64 default 20230816_20:33 fedora 38 arm64 default 20230816_20:33 funtoo 1.4 amd64 default 20230816_16:52 funtoo 1.4 arm64 default 20230816_16:52 funtoo next amd64 default 20230816_16:52 funtoo next arm64 default 20230816_16:52 kali current amd64 default 20230816_17:14 kali current arm64 default 20230816_17:14 mint ulyana amd64 default 20230816_08:52 mint ulyssa amd64 default 20230816_08:52 mint uma amd64 default 20230816_08:51 mint una amd64 default 20230816_08:51 mint vanessa amd64 default 20230816_08:51 mint vera amd64 default 20230816_08:51 mint victoria amd64 default 20230816_08:51 openeuler 20.03 amd64 default 20230816_15:48 openeuler 20.03 arm64 default 20230816_15:48 openeuler 22.03 amd64 default 20230816_15:48 openeuler 22.03 arm64 default 20230816_15:48 openeuler 23.03 amd64 default 20230816_15:48 openeuler 23.03 arm64 default 20230816_15:48 opensuse 15.4 amd64 default 20230816_04:20 opensuse 15.4 arm64 default 20230816_04:20 opensuse 15.5 amd64 default 20230816_04:20 opensuse 15.5 arm64 default 20230816_04:20 opensuse tumbleweed amd64 default 20230816_04:20 opensuse tumbleweed arm64 default 20230816_04:20 openwrt 21.02 amd64 default 20230816_11:57 openwrt 21.02 arm64 default 20230816_11:57 openwrt 22.03 amd64 default 20230816_11:57 openwrt 22.03 arm64 default 20230816_11:57 openwrt snapshot amd64 default 20230816_11:57 openwrt snapshot arm64 default 20230816_11:57 oracle 7 amd64 default 20230816_08:52 oracle 7 arm64 default 20230816_08:53 oracle 8 amd64 default 20230816_07:47 oracle 8 arm64 default 20230815_11:39 oracle 9 amd64 default 20230816_07:46 oracle 9 arm64 default 20230816_07:47 plamo 7.x amd64 default 20230816_01:33 plamo 8.x amd64 default 20230816_01:33 rockylinux 8 amd64 default 20230816_02:06 rockylinux 8 arm64 default 20230816_02:06 rockylinux 9 amd64 default 20230816_02:06 rockylinux 9 arm64 default 20230816_02:06 springdalelinux 7 amd64 default 20230816_06:38 springdalelinux 8 amd64 default 20230816_06:38 springdalelinux 9 amd64 default 20230816_06:38 ubuntu bionic amd64 default 20230816_07:43 ubuntu bionic arm64 default 20230816_07:42 ubuntu focal amd64 default 20230816_07:42 ubuntu focal arm64 default 20230816_07:42 ubuntu jammy amd64 default 20230816_07:42 ubuntu jammy arm64 default 20230816_07:42 ubuntu lunar amd64 default 20230816_07:42 ubuntu lunar arm64 default 20230816_07:42 ubuntu mantic amd64 default 20230816_07:42 ubuntu mantic arm64 default 20230816_07:42 ubuntu xenial amd64 default 20230816_07:42 ubuntu xenial arm64 default 20230816_07:42 voidlinux current amd64 default 20230816_17:10

voidlinux current arm64 default 20230816_17:10

To download an Ubuntu container, selecting the *lunar* release, and *amd64* architecture:

`root `[`#`]`lxc-create -t download -n ubuntu-guest -- -d ubuntu -r lunar -a amd64`

#### [Local template]

The **local** template allows a guest root filesystem to be imported from a xzipped tarball.

** Important**\
In LXC versions prior to 6.0, the *metadata* tarball is required, and must contain a file called *config*. This defines the container config, but may be empty.

##### [Create an empty metadata tarball]

If using a LXC version lower than 6, start by creating a metadata tarball:

`user `[`$`]`touch config `

`user `[`$`]`tar -cJf metadata.tar.xz config`

** Tip**\
The path to this archive can be specified with the `--metadata` argument for the *local* template.

** Note**\
Container config could be specified within this archive\'s *config* file, but is not required.

##### [Import a stage3 tarball]

LXC\'s *local* template can be used to natively import stage 3 tarballs:

`user `[`$`]`lxc-create -t local -n gentoo-guest -- --fstree stage3.tar.xz --no-dev`

** Note**\
In LXC 6.0, the `--no-dev` was added to the local import template, excluding the [/dev] directory in the tarball, which contains *device nodes* and cannot be extracted by unprivileged users.

### [Backing Store]

By default, containers will use the **dir** backing, copying the files into a directory.

Using a backing such as **btrfs** will allow [lxc-copy] to create a new container using another container as a snapshot.

The backing type is specified with **\--bdev** or **-B**:

`user `[`$`]`lxc-create -t local -n gentoo-guest -B btrfs -- --fstree stage3.tar.xz --no-dev`

** Tip**\
If running this as an unprivileged user, the subvolume containing the guest filesystems should be mounted with `user_subvol_rm_allowed`

### [Mount configuration]

By default, LXC will not make any mounts - including ones like [/proc] and [/sys], to create these mounts:

[FILE] **`/var/lib/lxc//config`**

    lxc.mount.auto = proc:mixed  # Mount /proc as rw but /proc/sys and /proc/sysrq-trigger as ro
    lxc.mount.auto = sys:ro  # mount /sys read only
    lxc.mount.auto = cgroup:ro  # Mount /sys/fs/cgroups read only

### [TTY configuration]

The following configuration is taken from [/usr/share/lxc/config/common.conf], it creates 1024 *pty*s and 4 *tty*s:

[FILE] **`/var/lib/lxc//config`**

    # Setup the LXC devices in /dev/lxc/
    lxc.tty.dir = lxc

    # Allow for 1024 pseudo terminals
    lxc.pty.max = 1024

    # Setup 4 tty devices
    lxc.tty.max = 4

** Tip**\
At least one *tty* must be defined for [lxc-console] to work properly. Additional *pyt*s are required to run a SSH server in a container.

### [Init configuration]

The way LXC starts a container can be adjusted with:

[FILE] **`/var/lib/lxc//config`**

    lxc.init.uid = 169  # Set the UID of the init process
    lxc.init.gid = 169  # Set the GID of the init process
    lxc.init.cmd = /usr/bin/tini /usr/bin/transmission-daemon -- -f -g /var/lib/transmission  # Tell lxc to use tini init, start transmission

### [Logging configuration]

** Important**\
This section covers logging for LXC itself, not the guests it manages.

LXC\'s log level can be adjusted with `lxc.log.level`:

[FILE] **`/var/lib/lxc//config`**

    lxc.log.level = 4

** Note**\
The default is **5**, but any value from **0** (*trace*) to **8** (*fatal*) can be used.

#### [File]

To send log information to a file, set the file with `lxc.log.file`:

[FILE] **`/var/lib/lxc//config`**

    lxc.log.file = /var/log/containers/container_name.log

#### [Syslog]

LXC containers can be configured to send logs to syslog using `lxc.log.syslog`:

[FILE] **`/var/lib/lxc//config`**

    lxc.log.syslog = daemon

** Tip**\
The following syslog facilities are valid: `daemon, local0, local1, local2, local3, local4, local5, local5, local6, local7`.

### [Console Logging]

To log the container console, `lxc.console.logfile` can be used:

[FILE] **`/var/lib/lxc//config`**

    lxc.console.logfile = /var/log/lxc/container_console.log

## [Usage]

** Tip**\
Usage for unprivileged containers is generally the same, but requires a bit more setup, described above.

### [Starting a container]

To start a container, simply use [lxc-start] with the container name:

`root `[`#`]`lxc-start gentoo-guest`

** Tip**\
The **-F** flag can be used to start the container in the foreground.

** Note**\
The process executed at startup is defined by `lxc.init.cmd`.

### [Stopping a container]

A container can be stopped with [lxc-stop]:

`root `[`#`]`lxc-stop guest-name`

### [lxc-console]

Using **lxc-console** provides console access to a guest with `lxc.tty = 1` defined:

`root `[`#`]`lxc-console -n `**`guestname`**

** Tip**\
[Ctrl+a] then [q] can be used to exit the console without killing the guest.

** Warning**\
Access to [lxc-console] should be restricted, since it gives full access to a container.

### [lxc-attach]

**lxc-attach** starts a process inside a running container. If no command is specified, it looks for the default shell. Therefore, you can get into the container by:

`root `[`#`]`lxc-attach -n `**`guestname`**

### [Accessing the container with sshd]

A common technique to allow users direct access into a system container is to run a separate sshd inside the container. Users then connect to that sshd directly. In this way, you can treat the container just like you treat a full virtual machine where you grant external access. If you give the container a routable address, then users can reach it without using ssh tunneling.

If you set up the container with a virtual ethernet interface connected to a bridge on the host, then it can have its own Ethernet address on the LAN, and you should be able to connect directly to it without logically involving the host (the host will transparently relay all traffic destined for the container, without the need for any special considerations). You should be able to simply \'ssh \<container_ip\>\'.

** Note**\
The above comments of *Hu* and *BoneKracker* have been taken from the [Gentoo Forums](https://forums.gentoo.org/viewtopic.php?p=6943426).

## [Troubleshooting]

### [Systemd containers on an OpenRC host]

To use systemd in the container, a recent enough (\>=4.6) kernel version with support for cgroup namespaces is needed. Additionally the host needs to have a `name=systemd` cgroup hierarchy mounted. Doing so does not require running systemd on the host:

`root `[`#`]`mkdir -p /sys/fs/cgroup/systemd `

`root `[`#`]`mount -t cgroup -o none,name=systemd systemd /sys/fs/cgroup/systemd `

`root `[`#`]`chmod 777 /sys/fs/cgroup/systemd`

** Note**\
This directory must be writable by the container UID. Created folders will be owned by the container user.

### [][Containters freeze on \'lxc stop\' with OpenRC]

Please see [LXD#Containters_freeze_on\_.27lxc_stop.27_with_OpenRC](https://wiki.gentoo.org/wiki/LXD#Containters_freeze_on_.27lxc_stop.27_with_OpenRC "LXD"). Just replace \'lxc exec\' with \'lxc-console\' or \'lxc-attach\' to get console access.

### [newuidmap error]

Packages `sys-auth/pambase-20150213` and `sys-apps/shadow-4.4-r2` provides newuidmap and newgidmap commands without required permissions for lxc. As result, all lxc-\* commands return error like:

`newuidmap: write to uid_map failed: Operation not permitted`

For example:

`lxc@localhost $``lxc-create -t download -n alpha -f ~/.config/lxc/guest.conf -- -d ubuntu -r trusty -a amd64 `

    newuidmap: write to uid_map failed: Operation not permitted
    error mapping child
    setgid: Invalid argument

To fix this issue, set setuid and setgid flags with command:

`root `[`#`]`chmod 4755 /usr/bin/newuidmap `

`root `[`#`]`chmod 4755 /usr/bin/newgidmap`

For more details regarding bug, see this issue: [\[1\]](https://github.com/lxc/lxc/issues/1454)

### [Could not set clone_children to 1 for cpuset hierarchy in parent cgroup]

As of december 2017, unified cgroups recently introduced in systemd and openrc are messing things up in the realm of unprivileged containers. It\'s tricky to see in other distros how they solve the problem because Arch doesn\'t support unprivileged containers and Ubuntu Xenial is on systemd 229 (unified cgroups became the default with 233), Debian stretch is on 232.

I began looking at non-LTS ubuntu releases but I haven\'t figured out what they\'re doing yet. It involves using the new `cgfsng` driver which, to my knowledge, has never been made to work on Gentoo. Unprivileged containers always worked with `cgmanager` which is now deprecated.

To work around that on systemd, you\'ll have to manually set user namespaces by following \"Create user namespace manually (no systemd)\" instructions above, ignoring the \"no systemd\" part. After that, you should be good to go.

On the OpenRC side, you also have to disable unified cgroups. You do that by editing `/etc/rc.conf` and setting `rc_cgroup_mode="legacy"`

That will bring you pretty far because your unprivileged container will boot, but if you boot a systemd system, it won\'t be happy about not being in its cosy systemd world. You will have to manually create a `systemd` cgroup for it. [this write up about LXC under alpine](https://j2h2.com/entry/alpine-linux-and-systemd-containers-round-2) helps a lot.

### [][tee: /sys/fs/cgroup/memory/memory.use_hierarchy: Device or resource busy]

Current kernel upstream changed behavior for cgroup v1 and it is unable to change memory_hierarchy after lxc fs mount. To use this functionality, set `rc_cggroup_memory_use_hierarchy="yes"` in `/etc/rc.conf`

### [][lxc-console: no promt / console (may be a temporary as of 2019-10)]

Make sure the container spawns the right agetty / ttys, so lxc-console can connect to it. Alternatively, connect to the console.

Gentoo LXC images from jenkins server currently might not work out of the box as expected before - they don\'t spawn ttys because of this [reported bug](https://discuss.linuxcontainers.org/t/gentoo-image-ttys-die/5139) / [fix](https://github.com/lxc/lxc-ci/commit/39b5e11afdd8d94a26fe30692c4f9e405a27bd19). Try connecting with lxc-console using the \"-t 0\" option, which explicitly connects to the container console instead of a tty:

`root `[`#`]`lxc-console -n mycontainer -t 0`

Alternatively, spawn more standard ttys inside the container by editing /etc/inittab:

[FILE] **`/etc/inittab`**

    ...
    # TERMINALS
    x1:12345:respawn:/sbin/agetty 38400 console linux
    c1:12345:respawn:/sbin/agetty 38400 tty1 linux
    c2:2345:respawn:/sbin/agetty 38400 tty2 linux
    #c3:2345:respawn:/sbin/agetty 38400 tty3 linux
    ...

## [See also]

-   [Docker](https://wiki.gentoo.org/wiki/Docker "Docker") --- a [container](https://en.wikipedia.org/wiki/Container_(virtualization) "wikipedia:Container (virtualization)")-based [virtualization](https://wiki.gentoo.org/wiki/Virtualization "Virtualization") system
-   [Incus](https://wiki.gentoo.org/wiki/Incus "Incus") --- next generation system container and virtual machine manager
-   [Magic SysRq](https://wiki.gentoo.org/wiki/Magic_SysRq "Magic SysRq") --- a kernel hack that enables the kernel to listen to specific key presses and respond by calling a specific kernel function.

## [External resources]

-   [CAP_SYS_ADMIN: the new root](https://lwn.net/Articles/486306/)
-   [Stéphane Graber\'s LXC 1.0: Blog post series](https://www.stgraber.org/2013/12/20/lxc-1-0-blog-post-series/)

## [References]

1.  [[[↑](#cite_ref-1)] [[https://www.kernel.org/doc/html/latest/admin-guide/cgroup-v2.html](https://www.kernel.org/doc/html/latest/admin-guide/cgroup-v2.html)]]
2.  [[[↑](#cite_ref-2)] [[https://linuxcontainers.org/lxc/getting-started/#creating-unprivileged-containers-as-root](https://linuxcontainers.org/lxc/getting-started/#creating-unprivileged-containers-as-root)]]