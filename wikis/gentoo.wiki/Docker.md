**Resources**

[[]][Home](https://www.docker.com/)

[[]][Official documentation](https://docs.docker.com/)

[[]][Package information](https://packages.gentoo.org/packages/app-containers/docker)

[[]][Wikipedia](https://en.wikipedia.org/wiki/Docker_(software) "wikipedia:Docker (software)")

[[]][GitHub](https://github.com/docker/docker)

[[]][[#docker](ircs://irc.libera.chat/#docker)] ([[webchat](https://web.libera.chat/#docker)])

**Docker** is a [container](https://en.wikipedia.org/wiki/Container_(virtualization) "wikipedia:Container (virtualization)")-based [virtualization](https://wiki.gentoo.org/wiki/Virtualization "Virtualization") system which can be used to establish development or runtime environments without modifying the base operating system.

Docker is built on a thin layer of virtualization, using the host [kernel](https://wiki.gentoo.org/wiki/Kernel "Kernel"), and as such is \"lighter\" than full hardware virtualization, incurring a lesser performance tradeoff. It allows easy deployment of instances of containers to different hosts.

** Warning**\
Containers that produce kernel panics will induce kernel panics into the host operating system.

** See also**\
The [Gentoo Docker project](https://wiki.gentoo.org/wiki/Project:Docker "Project:Docker") provides pre-built Docker images containing a choice of ready-to-go Gentoo installations for different architectures - [https://cloud.docker.com/u/gentoo](https://cloud.docker.com/u/gentoo) .

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Kernel]](#Kernel)
        -   [[1.2.1] [Snippet]](#Snippet)
        -   [[1.2.2] [Compatibility check]](#Compatibility_check)
    -   [[1.3] [Emerge]](#Emerge)
        -   [[1.3.1] [PaX kernel]](#PaX_kernel)
-   [[2] [Configuration]](#Configuration)
    -   [[2.1] [Service]](#Service)
        -   [[2.1.1] [OpenRC]](#OpenRC)
        -   [[2.1.2] [systemd]](#systemd)
    -   [[2.2] [Permissions]](#Permissions)
    -   [[2.3] [Storage driver]](#Storage_driver)
        -   [[2.3.1] [btrfs]](#btrfs)
    -   [[2.4] [Networking]](#Networking)
-   [[3] [Usage]](#Usage)
    -   [[3.1] [Testing]](#Testing)
    -   [[3.2] [Listing images]](#Listing_images)
    -   [[3.3] [Starting a container from an image]](#Starting_a_container_from_an_image)
    -   [[3.4] [Listing containers]](#Listing_containers)
    -   [[3.5] [Viewing container config]](#Viewing_container_config)
    -   [[3.6] [Running a command in a running container]](#Running_a_command_in_a_running_container)
    -   [[3.7] [Stopping a container]](#Stopping_a_container)
    -   [[3.8] [Starting a container]](#Starting_a_container)
    -   [[3.9] [Building from a Dockerfile]](#Building_from_a_Dockerfile)
-   [[4] [Custom Images]](#Custom_Images)
    -   [[4.1] [Building the image environment]](#Building_the_image_environment)
        -   [[4.1.1] [Using emerge to build the environment]](#Using_emerge_to_build_the_environment)
        -   [[4.1.2] [Alternative minimal approach: Dynamically linked binaries using Kubler]](#Alternative_minimal_approach:_Dynamically_linked_binaries_using_Kubler)
    -   [[4.2] [Packing the environment into a tarball]](#Packing_the_environment_into_a_tarball)
    -   [[4.3] [Importing into Docker]](#Importing_into_Docker)
        -   [[4.3.1] [Tagging the Image]](#Tagging_the_Image)
-   [[5] [Setting up rootless Docker]](#Setting_up_rootless_Docker)
    -   [[5.1] [Disable the existing docker daemon]](#Disable_the_existing_docker_daemon)
        -   [[5.1.1] [OpenRC]](#OpenRC_2)
        -   [[5.1.2] [Systemd]](#Systemd_2)
    -   [[5.2] [Installation]](#Installation_2)
    -   [[5.3] [Confirming rootless installation]](#Confirming_rootless_installation)
-   [[6] [Troubleshooting]](#Troubleshooting)
    -   [[6.1] [Docker service crashes/fails to start (OpenRC)]](#Docker_service_crashes.2Ffails_to_start_.28OpenRC.29)
    -   [[6.2] [Docker service fails because cgroup device not mounted (OpenRC)]](#Docker_service_fails_because_cgroup_device_not_mounted_.28OpenRC.29)
    -   [[6.3] [Docker service fails to start (systemd)]](#Docker_service_fails_to_start_.28systemd.29)
    -   [[6.4] [Docker service runs but fails to start container (systemd)]](#Docker_service_runs_but_fails_to_start_container_.28systemd.29)
    -   [[6.5] [Docker service runs but fails to start container (systemd)]](#Docker_service_runs_but_fails_to_start_container_.28systemd.29_2)
    -   [[6.6] [Docker service fails because cgroup device not mounted (systemd)]](#Docker_service_fails_because_cgroup_device_not_mounted_.28systemd.29)
    -   [[6.7] [systemd-networkd]](#systemd-networkd)
-   [[7] [See also]](#See_also)
-   [[8] [External resources]](#External_resources)

## [Installation]

### [USE flags]

### [USE flags for] [app-containers/docker](https://packages.gentoo.org/packages/app-containers/docker) [[]] [The core functions you need to create Docker images and run Docker containers]

  --------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------
  [`+container-init`](https://packages.gentoo.org/useflags/+container-init)   Makes the a staticly-linked init system tini available inside a container.
  [`+overlay2`](https://packages.gentoo.org/useflags/+overlay2)               Enables dependencies for the \"overlay2\" graph driver, including necessary kernel flags.
  [`apparmor`](https://packages.gentoo.org/useflags/apparmor)                 Enable support for the AppArmor application security system
  [`btrfs`](https://packages.gentoo.org/useflags/btrfs)                       Enables dependencies for the \"btrfs\" graph driver, including necessary kernel flags.
  [`cuda`](https://packages.gentoo.org/useflags/cuda)                         Enable NVIDIA CUDA support (computation on GPU)
  [`seccomp`](https://packages.gentoo.org/useflags/seccomp)                   Enable seccomp (secure computing mode) to perform system call filtering at runtime to increase security of programs
  [`selinux`](https://packages.gentoo.org/useflags/selinux)                   !!internal use only!! Security Enhanced Linux support, this must be set by the selinux profile or breakage will occur
  [`systemd`](https://packages.gentoo.org/useflags/systemd)                   Enable use of systemd-specific libraries and features like socket activation or session tracking
  --------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-01-24 19:59] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Kernel]

If the kernel has not been configured properly before merging the [[[app-containers/docker]](https://packages.gentoo.org/packages/app-containers/docker)[]] package, a list of missing kernel options will be printed by emerge. These kernel features must be enabled [manually](https://wiki.gentoo.org/wiki/Kernel/Configuration "Kernel/Configuration").

** Note**\
Press the [/] key while in the ncurses-based [menuconfig] to search the name of the configuration option.

For the most up-to-date values, check the contents of the `CONFIG_CHECK` in [/var/db/repos/gentoo/app-containers/docker/docker-9999.ebuild] file.

A graphical representation would look something like this:

** Note**\
Kernel configuration may vary depending on different kernel versions, Docker versions, and different USE flags. It is recommended to read messages for package [[[app-containers/docker]](https://packages.gentoo.org/packages/app-containers/docker)[]] when emerging Docker, and recompile kernel based on what is not set when it should be.

[KERNEL] **Configuring the kernel for Docker**

    General setup  --->
      [*] POSIX Message Queues Search for <code>CONFIG_POSIX_MQUEU</code> to find this item.
      BPF subsystem  --->
         [*] Enable bpf() system call (Optional) Search for <code>CONFIG_BPF_SYSCALL</code> to find this item.
      [*] Control Group support  ---> Search for <code>CONFIG_CGROUPS</code> to find this item.
         [*] Memory controller Search for <code>CONFIG_MEMCG</code> to find this item.
         [*] Swap controller (Optional)
         [*]   Swap controller enabled by default (Optional)
         [*] IO controller (Optional)
         [*] CPU controller  ---> Search for <code>CONFIG_CGROUP_SCHED</code> to find this item.
            [*] Group scheduling for SCHED_OTHER (Optional) Search for <code>CONFIG_FAIR_GROUP_SCHED</code> to find this item.
            [*]   CPU bandwidth provisioning for FAIR_GROUP_SCHED (Optional) Search for <code>CONFIG_CFS_BANDWIDTH</code> to find this item.
            [*] Group scheduling for SCHED_RR/FIFO (Optional) Search for <code>CONFIG_RT_GROUP_SCHED</code> to find this item.
         [*] PIDs controller (Optional) Search for <code>CONFIG_CGROUP_PIDS</code> to find this item.
         [*] Freezer controller Search for <code>CONFIG_CGROUP_FREEZER</code> to find this item.
         [*] HugeTLB controller (Optional) Search for <code>CONFIG_CGROUP_HUGETLB</code> to find this item.
         [*] Cpuset controller Search for <code>CONFIG_CPUSETS</code> to find this item.
            [*]  Include legacy /proc//cpuset file (Optional) Search for <code>CONFIG_PROC_PID_CPUSET</code> to find this item.
         [*] Device controller Search for <code>CONFIG_CGROUP_DEVICE</code> to find this item.
         [*] Simple CPU accounting controller Search for <code>CONFIG_CGROUP_CPUACCT</code> to find this item.
         [*] Perf controller (Optional) Search for <code>CONFIG_CGROUP_PERF</code> to find this item.
         [*] Support for eBPF programs attached to cgroups (Optional) Search for <code>CONFIG_CGROUP_BPF</code> to find this item.
      [*] Namespaces support Search for <code>CONFIG_NAMESPACES</code> to find this item.
         [*] UTS namespace Search for <code>CONFIG_UTS_NS</code> to find this item.
         [*] IPC namespace Search for <code>CONFIG_IPC_NS</code> to find this item.
         [*] User namespace (Optional) Search for <code>CONFIG_USER_NS</code> to find this item.
         [*] PID Namespaces Search for <code>CONFIG_PID_NS</code> to find this item.
         [*] Network namespace Search for <code>CONFIG_NET_NS</code> to find this item.
    General architecture-dependent options  --->
      [*] Enable seccomp to safely execute untrusted bytecode (Optional) Search for <code>CONFIG_SECCOMP</code> to find this item.
    [*] Enable the block layer  ---> Search for <code>CONFIG_BLOCK</code> to find this item.
      [*] Block layer bio throttling support (Optional) Search for <code>CONFIG_BLK_DEV_THROTTLING</code> to find this item.
    [*] Networking support  ---> Search for <code>CONFIG_NET</code> to find this item.
       Networking options  --->
          [*] Network packet filtering framework (Netfilter)  ---> Search for <code>CONFIG_NETFILTER</code> to find this item.
               [*] Advanced netfilter configuration Search for <code>CONFIG_NETFILTER_ADVANCED</code> to find this item.
               [*]   Bridged IP/ARP packets filtering Search for <code>CONFIG_BRIDGE_NETFILTER</code> to find this item.
                  Core Netfilter Configuration  --->
                     [*] Netfilter connection tracking support Search for <code>CONFIG_NF_CONNTRACK</code> to find this item.
                     [*] Network Address Translation support Search for <code>CONFIG_NF_NAT</code> to find this item.
                     [*] MASQUERADE target support Search for <code>CONFIG_NETFILTER_XT_TARGET_NFQUEUE</code> to find this item.
                     [*] Netfilter Xtables support Search for <code>CONFIG_NETFILTER_XTABLES</code> to find this item.
                     [*]    "addrtype" address type match support Search for <code>CONFIG_NETFILTER_XT_MATCH_ADDRTYPE</code> to find this item.
                     [*]    "conntrack" connection tracking match support Search for <code>CONFIG_NETFILTER_XT_MATCH_CONNTRACK</code> to find this item.
                     [*]    "ipvs" match support (Optional) Search for <code>CONFIG_NETFILTER_XT_MATCH_IPVS</code> to find this item.
                     [*]    "mark" match support Search for <code>CONFIG_NETFILTER_XT_MATCH_MARK</code> to find this item.
               [*] IP virtual server support  ---> (Optional) Search for <code>CONFIG_IP_VS</code> to find this item.
                  [*] TCP load balancing support (Optional) Search for <code>CONFIG_IP_VS_PROTO_TCP</code> to find this item.
                  [*] UDP load balancing support (Optional) Search for <code>CONFIG_IP_VS_PROTO_UDP</code> to find this item.
                  [*] round-robin scheduling (Optional) Search for <code>CONFIG_IP_VS_RR</code> to find this item.
                  [*] Netfilter connection tracking (Optional) Search for <code>CONFIG_IP_VS_NFCT</code> to find this item.
               IP: Netfilter Configuration  --->
                  [*] IP tables support Search for <code>CONFIG_IP_NF_IPTABLES</code> to find this item.
                  [*]    raw table support (required for NOTRACK/TRACE) Search for <code>CONFIG_IP_NF_RAW</code> to find this item.
                  [*]    Packet filtering Search for <code>CONFIG_IP_NF_FILTER</code> to find this item.
                  [*]    iptables NAT support Search for <code>CONFIG_IP_NF_NAT</code> to find this item.
                  [*]      MASQUERADE target support Search for <code>CONFIG_IP_NF_TARGET_MASQUERADE</code> to find this item.
                  [*]      REDIRECT target support (Optional) Search for <code>CONFIG_NF_TARGET_REDIRECT</code> to find this item.
           [*] 802.1d Ethernet Bridging Search for <code>CONFIG_BRIDGE</code> to find this item.
           [*]   VLAN filtering Search for <code>CONFIG_BRIDGE_VLAN_FILTERING</code> to find this item.
           [*] 802.1Q/802.1ad VLAN Support Search for <code>CONFIG_VLAN_8021Q</code> to find this item.
           [*] QoS and/or fair queueing  --->  (Optional) Search for <code>CONFIG_NET_SCHED</code> to find this item.
              [*] Control Group Classifier (Optional) Search for <code>CONFIG_NET_CLS_CGROUP</code> to find this item.
           [*] L3 Master device support Search for <code>CONFIG_NET_L3_MASTER_DEV</code> to find this item.
           [*] Network priority cgroup (Optional) Search for <code>CONFIG_CGROUP_NET_PRIO</code> to find this item.
    Device Drivers  --->
      [*] Multiple devices driver support (RAID and LVM)  ---> Search for <code>CONFIG_MD</code> to find this item.
         [*] Device mapper support (Optional) Search for <code>CONFIG_BLK_DEV_DM</code> to find this item.
         [*]  Thin provisioning target (Optional) Search for <code>CONFIG_DM_THIN_PROVISIONING</code> to find this item.
       [*] Network device support  ---> Search for <code>CONFIG_NETDEVICES</code> to find this item.
          [*] Network core drive support Search for <code>CONFIG_NET_CORE</code> to find this item.
          [*]   Dummy net driver support Search for <code>CONFIG_DUMMY</code> to find this item.
          [*]   MAC-VLAN net driver support Search for <code>CONFIG_MACVLAN</code> to find this item.
          [*]   IP-VLAN support Search for <code>CONFIG_IPVLAN</code> to find this item.
          [*]   Virtual eXtensible Local Area Network (VXLAN) Search for <code>CONFIG_VXLAN</code> to find this item.
          [*]   Virtual ethernet pair device Search for <code>CONFIG_VETH</code> to find this item.
       Character devices  --->
           -*- Enable TTY Search for <code>CONFIG_TTY</code> to find this item.
           -*-    Unix98 PTY support Search for <code>CONFIG_UNIX98_PTYS</code> to find this item.
           [*]       Support multiple instances of devpts (option appears if you are using systemd)
    File systems  --->
      [*] Btrfs filesystem support (Optional) Search for <code>CONFIG_BTRFS_FS</code> to find this item.
      [*]   Btrfs POSIX Access Control Lists (Optional) Search for <code>CONFIG_BTRFS_FS_POSIX_ACL</code> to find this item.
      [*] Overlay filesystem support Search for <code>CONFIG_OVERLAY_FS</code> to find this item.
      Pseudo filesystems  --->
         [*] HugeTLB file system support (Optional) Search for <code>CONFIG_HUGETLBFS</code> to find this item.
    Security options  --->
      [*] Enable access key retention support Search for <code>CONFIG_KEYS</code> to find this item.

\
After exiting the kernel configuration, [rebuild the kernel](https://wiki.gentoo.org/wiki/Kernel/Rebuild "Kernel/Rebuild"). If the kernel rebuild also performs a kernel upgrade, be sure to rebuild the [bootloader](https://wiki.gentoo.org/wiki/Bootloader "Bootloader")\'s menu configuration, then reboot the system to the newly recompiled kernel binary.

#### [Snippet]

[FILE] **`/etc/kernel/config.d/docker-linux6-11-10.config`**

    CONFIG_XFRM_ESP=m
    CONFIG_NET_IP_TUNNEL=m
    CONFIG_NET_UDP_TUNNEL=m
    CONFIG_INET_ESP=m
    # CONFIG_INET_ESP_OFFLOAD is not set
    # CONFIG_INET_ESPINTCP is not set
    CONFIG_BRIDGE_NETFILTER=m
    CONFIG_NETFILTER_FAMILY_BRIDGE=y
    CONFIG_NF_CONNTRACK_FTP=m
    CONFIG_NF_CONNTRACK_TFTP=m
    CONFIG_NF_NAT_FTP=m
    CONFIG_NF_NAT_TFTP=m
    CONFIG_NF_NAT_REDIRECT=y
    CONFIG_NETFILTER_XT_MARK=m
    CONFIG_NETFILTER_XT_TARGET_REDIRECT=m
    CONFIG_NETFILTER_XT_MATCH_IPVS=m
    # CONFIG_NETFILTER_XT_MATCH_PHYSDEV is not set
    CONFIG_IP_VS=m
    # CONFIG_IP_VS_IPV6 is not set
    # CONFIG_IP_VS_DEBUG is not set
    CONFIG_IP_VS_TAB_BITS=12

    #
    # IPVS transport protocol load balancing support
    #
    CONFIG_IP_VS_PROTO_TCP=y
    CONFIG_IP_VS_PROTO_UDP=y
    # CONFIG_IP_VS_PROTO_ESP is not set
    # CONFIG_IP_VS_PROTO_AH is not set
    # CONFIG_IP_VS_PROTO_SCTP is not set

    #
    # IPVS scheduler
    #
    CONFIG_IP_VS_RR=m
    # CONFIG_IP_VS_WRR is not set
    # CONFIG_IP_VS_LC is not set
    # CONFIG_IP_VS_WLC is not set
    # CONFIG_IP_VS_FO is not set
    # CONFIG_IP_VS_OVF is not set
    # CONFIG_IP_VS_LBLC is not set
    # CONFIG_IP_VS_LBLCR is not set
    # CONFIG_IP_VS_DH is not set
    # CONFIG_IP_VS_SH is not set
    # CONFIG_IP_VS_MH is not set
    # CONFIG_IP_VS_SED is not set
    # CONFIG_IP_VS_NQ is not set
    # CONFIG_IP_VS_TWOS is not set

    #
    # IPVS SH scheduler
    #
    CONFIG_IP_VS_SH_TAB_BITS=8

    #
    # IPVS MH scheduler
    #
    CONFIG_IP_VS_MH_TAB_INDEX=12

    #
    # IPVS application helper
    #
    # CONFIG_IP_VS_FTP is not set
    CONFIG_IP_VS_NFCT=y
    CONFIG_IP_NF_RAW=y
    CONFIG_IP_NF_TARGET_MASQUERADE=m
    CONFIG_IP_NF_TARGET_REDIRECT=m
    CONFIG_BRIDGE_VLAN_FILTERING=y
    CONFIG_VLAN_8021Q=m
    # CONFIG_VLAN_8021Q_GVRP is not set
    # CONFIG_VLAN_8021Q_MVRP is not set
    CONFIG_DUMMY=m
    CONFIG_MACVLAN=m
    # CONFIG_MACVTAP is not set
    CONFIG_IPVLAN_L3S=y
    CONFIG_IPVLAN=m
    # CONFIG_IPVTAP is not set
    CONFIG_VXLAN=m
    # CONFIG_PRESTERA is not set
    CONFIG_CRYPTO_ECHAINIV=m

#### [Compatibility check]

To re-run the kernel configuration compatibility check, issue:

`user `[`$`]`/usr/share/docker/contrib/check-config.sh`

### [Emerge]

** Note**\
In versions prior to 20.10.1, the docker command line tool had been included with [[[app-containers/docker]](https://packages.gentoo.org/packages/app-containers/docker)[]], however for newer versions it has been moved to [[[app-containers/docker-cli]](https://packages.gentoo.org/packages/app-containers/docker-cli)[]].

Install [[[app-containers/docker]](https://packages.gentoo.org/packages/app-containers/docker)[]] and [[[app-containers/docker-cli]](https://packages.gentoo.org/packages/app-containers/docker-cli)[]]:

`root `[`#`]`emerge --ask --verbose app-containers/docker app-containers/docker-cli`

#### [PaX kernel]

** Note**\
When running a PaX kernel (like the deprecated hardened-sources package), memory protection on **containerd** needs to be disabled.

Tools in the [[[sys-apps/paxctl]](https://packages.gentoo.org/packages/sys-apps/paxctl)[]] package are necessary for this operation. See [Hardened/PaX Quickstart](https://wiki.gentoo.org/wiki/Hardened/PaX_Quickstart "Hardened/PaX Quickstart") for an introduction.

`root `[`#`]`/sbin/paxctl -m /usr/bin/containerd`

For the **hello-world** example, set this flag for **containerd-shim** and **runc**:

`root `[`#`]`/sbin/paxctl -m /usr/bin/containerd-shim `

`root `[`#`]`/sbin/paxctl -m /usr/bin/runc `

If an [issue with denied chmods in chroots](https://github.com/docker/docker/issues/20303) occurs, a more recent version of Docker (\>=1.12) is needed. Use the **[\~amd64]** [Keyword](https://wiki.gentoo.org/wiki//etc/portage/package.accept_keywords "/etc/portage/package.accept keywords") for Docker and its dependencies listed subsequently when running [emerge app-containers/docker] again.

## [Configuration]

The docker daemon configuration is located at [/etc/docker/daemon.json], more information on configuring this file is available at: [https://docs.docker.com/config/daemon/](https://docs.docker.com/config/daemon/)

The current [docker] configuration can be viewed with:

`root `[`#`]`docker info`

### [Service]

#### [OpenRC]

OpenRC users can adjust the `DOCKER_OPTS` variable in the service configuration file located in [/etc/conf.d]. The example below displays a change to the storage driver to [btrfs](https://wiki.gentoo.org/wiki/Btrfs "Btrfs") and the docker engine root to [/srv/var/lib/docker]:

[FILE] **`/etc/conf.d/docker`**

    DOCKER_OPTS="--storage-driver btrfs --data-root /srv/var/lib/docker"

** Tip**\
See [upstream documentation](https://docs.docker.com/engine/reference/commandline/dockerd/#/options) for the various options that can be passed to the `DOCKER_OPTS` variable.

** Note**\
Configuration changes will not be active until the [docker] service is reloaded or restarted.

After Docker has been successfully installed and configured, it can be added to the system\'s default runlevel, starting it at boot:

`root `[`#`]`rc-update add docker default `

`root `[`#`]`rc-service docker start`

If the registry service is required:

`root `[`#`]`rc-update add registry default `

`root `[`#`]`rc-service registry start `

#### [systemd]

To have Docker start on boot, enable it:

`root `[`#`]`systemctl enable docker.service`

To start it now:

`root `[`#`]`systemctl start docker.service`

** Note**\
Systemd will use configuration present in [/etc/docker/daemon.json], information about configuring this file is present [above](https://wiki.gentoo.org/wiki/Docker#Configuration "Docker").

### [Permissions]

Add relevant users to the docker group:

`root `[`#`]`usermod -aG docker <username>`

** Warning**\
Allowing a user to talk to the Docker daemon is equivalent to giving the user full root access to the host. [More](https://docs.docker.com/engine/security/security/#docker-daemon-attack-surface)

### [Storage driver]

Overlay2 storage driver is the preferred storage driver for all currently supported Linux distributions, and requires no extra configuration.

View Docker\'s settings in detail with the [info] subcommand:

`user `[`$`]`docker info`

#### [btrfs]

To change the storage driver, first verify the host machines kernel has support for the desired filesystem. The [btrfs](https://wiki.gentoo.org/wiki/Btrfs "Btrfs") filesystem will be used in this example:

** Note**\
Btrfs driver will require additional configuration if the storage engine data-root directory does not use the btrfs filesystem, see [upstream\'s documentation](https://docs.docker.com/storage/storagedriver/btrfs-driver).

[FILE] **`/etc/docker/daemon.json`Set the docker storage driver to use btrfs**



`user `[`$`]`grep btrfs /proc/filesystems`

When using the btrfs driver, be aware the *data-root* directory of the docker engine ([/var/lib/docker/] by default) may need be adjusted to a non-default location if directories backing filesystem is not btrfs. For situations where the btrfs storage pool is located under a different device and/or mountpoint (such as [/mnt] or [/srv]), adjust the data-root location accordingly:

[FILE] **`/etc/docker/daemon.json`Moving the root directory of the docker storage engine**



Insure the running service is stopped before moving data from the previous data-root location, then copy the data to the new location:

`root `[`#`]`systemctl stop docker `

`root `[`#`]`mkdir --parents /srv/var/lib/docker `

`root `[`#`]`rsync -a /var/lib/docker/* /srv/var/lib/docker `

`root `[`#`]`systemctl start docker `

### [Networking]

Port forwarding must be enabled for docker container networking to work.

This can be temporarily enabled using [procfs](https://wiki.gentoo.org/wiki/Procfs "Procfs"):

`user `[`$`]`sudo sysctl net.ipv4.ip_forward=1`

A more permanent change can be made with:

[FILE] **`/etc/sysctl.d/local.conf`Enable ip forwarding persistently**

    net.ipv4.ip_forward=1

## [Usage]

### [Testing]

In order to test the installation, run the following command:

`user `[`$`]`docker run --rm hello-world`

    Hello from Docker.
    This message shows that your installation appears to be working correctly.

    To generate this message, Docker took the following steps:
     1. The Docker client contacted the Docker daemon.
     2. The Docker daemon pulled the "hello-world" image from the Docker Hub.
     3. The Docker daemon created a new container from that image which runs the
        executable that produces the output you are currently reading.
     4. The Docker daemon streamed that output to the Docker client, which sent it
        to your terminal.

    To try something more ambitious, you can run an Ubuntu container with:
     $ docker run -it ubuntu bash

    Share images, automate workflows, and more with a free Docker Hub account:
     https://hub.docker.com

    For more examples and ideas, visit:
     https://docs.docker.com/userguide/

That will first download from the [Docker Hub](https://hub.docker.com/) the image named *hello-world* (if it has not been downloaded locally yet), then it will run it inside new [namespaces](https://wiki.gentoo.org/wiki/Namespaces "Namespaces"). It purpose is just to display some text through a container.

** Tip**\
For most commands, the container ID can be used in place of the container name, not all containers will have a name.

### [Listing images]

Current images can be listed with:

`user `[`$`]`docker images`

### [Starting a container from an image]

A new container can be started using an image with **run**. The following command starts a docker container which is an Alpine Linux shell:

`user `[`$`]`docker run -it --rm alpine:3.18 ash`

** Note**\
Adding **-it** starts the container interactively, and **\--rm** deletes it once execution is complete.

### [Listing containers]

Current containers can be listed with:

`user `[`$`]`docker container list`

### [Viewing container config]

To view the configuration for a container:

`user `[`$`]`docker container inspect  `

### [Running a command in a running container]

To execute a command in an already running container:

`user `[`$`]`docker exec   `

### [Stopping a container]

A running container can be stopped with:

`user `[`$`]`docker stop  `

### [Starting a container]

If a container has been stopped, it can be started again with:

`user `[`$`]`docker start  `

### [Building from a Dockerfile]

Create a new Dockerfile in an empty directory with the following content:

[FILE] **`Dockerfile`**

    FROM php:5.6-apache

Run:

`user `[`$`]`docker build -t my-php-app . `

`user `[`$`]`docker run -it --rm --name my-running-app my-php-app `

## [Custom Images]

Containers are generally structured with either of the following approaches:

-   The minimal approach: According to the [container philosophy](https://docs.docker.com/engine/userguide/eng-image/dockerfile_best-practices/#run-only-one-process-per-container) a container should **only** contain what is needed to serve one process. In this case ideally the container consists of one static binary.
-   The VM approach: A container can be treated like a full system virtualization environment. In this case the container includes a whole operating system.

### [Building the image environment]

The image can be constructed using many methods. The simplest would involve adding a single binary which can be executed. Using [emerge] to generate the environment is a simple and effective method, but more advanced methods such as using [crossdev](https://wiki.gentoo.org/wiki/Crossdev "Crossdev") or [catalyst](https://wiki.gentoo.org/wiki/Catalyst "Catalyst") are possible.

#### [Using emerge to build the environment]

Portage can be used to simply construct an application environment.

A Gentoo-based Docker image can be constructed by using [emerge] with the **\--root** flag. Simply **\--oneshot** the desired packages to that destination.

The following command creates a container for [[[net-p2p/transmission]](https://packages.gentoo.org/packages/net-p2p/transmission)[]] at [/var/lib/chroot/builddir/transmission]:

`root `[`#`]`emerge --ask --verbose --root /var/lib/chroot/builddir/transmission --oneshot transmission`

** Note**\
This approach includes many packages such as compilers which are not required for operation.

** Important**\
This approach does not include a shell, or even init system.

#### [Alternative minimal approach: Dynamically linked binaries using Kubler]

[Kubler](https://github.com/edannenberg/kubler) is a generic, extendable build orchestrator, written in Bash. It can be used to take advantage of Portage\'s features to build lightweight Docker or Podman images without needing to mess with [crossdev], or as a tool to assist with ebuild development.

Detailed instructions for using Kubler are available [Here](https://wiki.gentoo.org/wiki/Kubler "Kubler").

### [Packing the environment into a tarball]

Once the build environment has been created, the contents can be archived with [tar] to be imported into Docker.

The following command creates [gentoo-transmission.tar.gz] based on the contents of [/var/lib/chroot/builddir/transmission/]:

`root `[`#`]`tar -czf gentoo-transmission.tar.gz -C /var/lib/chroot/builddir/transmission/ .`

** Tip**\
When backing up image sources, signing the tarball with [gpg](https://wiki.gentoo.org/wiki/GnuPG "GnuPG") can be useful to verify that the file has not been modified after creation.

### [Importing into Docker]

If using a *Dockerfile*, the tarball can be imported with *ADD*. To import [gentoo-transmission.tar.gz]:

[FILE] **`Dockerfile`**

    FROM scratch
    ADD gentoo-transmission.tar.gz /
    EXPOSE 9091/tcp
    EXPOSE 51413/tcp
    EXPOSE 51413/udp
    USER transmission
    CMD ["/usr/bin/transmission-daemon", "-f", "-g", "/config"]

The image can be manually imported with:

`root `[`#`]`docker import gentoo-transmission.tar.gz`

#### [Tagging the Image]

The imported image should be visible using [docker images]:

`root `[`#`]`docker images`

    REPOSITORY           TAG       IMAGE ID       CREATED          SIZE
    <none>               <none>    a5c15b539917   13 minutes ago   622MB

Using the image ID *a5c15b539917*, the tag *gentoo-transmission* can be applied to this image:

`root `[`#`]`docker tag a5c15b539917 gentoo-transmission`

## [Setting up rootless Docker]

Docker runs a client/server model. The daemon *dockerd* runs as root by default, the result is that anyone that can execute docker commands can effectively run commands as the root user.

Docker provides the option to run as the the daemon on a per user basis instead with a little additional set up documented below.

There are some caveats when running in rootless mode please see [the upstream known limitations](https://docs.docker.com/engine/security/rootless/troubleshoot/#known-limitations) for the up to date list.

**Note: by default rootless docker stores images etc. in \~/.local/share/docker instead of /var/lib/docker images aren\'t shared between users and you may wish to exclude this folder from any backups.**

### [Disable the existing docker daemon]

First disable the existing docker service.

#### [OpenRC]

`root `[`#`]`rc-update del docker default `

`root `[`#`]`rc-service docker stop`

#### [Systemd]

`root `[`#`]`systemctl disable --now docker.service docker.socket`

### [Installation]

Remove the docker socket if it exists

`root `[`#`]` rm /var/run/docker.sock`

Configure the kernel modules to load at boot. The docker root service loads the required modules using modprobe the user services don\'t have permission to do this.

[FILE] **`/etc/modules-load.d/docker.conf`Load ip_tables and overlay modules at boot**

    ip_tables
    overlay

Install [[[app-containers/slirp4netns]](https://packages.gentoo.org/packages/app-containers/slirp4netns)[]] and [[[sys-apps/rootlesskit]](https://packages.gentoo.org/packages/sys-apps/rootlesskit)[]]:

`root `[`#`]`emerge --ask --verbose app-containers/slirp4netns sys-apps/rootlesskit`

To install in rootless mode run:

`user `[`$`]`dockerd-rootless-setuptool.sh install`

This will output various information, it\'s recommend you read these for more information they maybe useful when troubleshooting.

To allow running docker at boot run under systemd run

`root `[`#`]`loginctl enable-linger <username>`

`user `[`$`]`systemctl --user enable docker.service`

### [Confirming rootless installation]

Check the current configuration with

`user `[`$`]`docker info`

At the top of the output you should see output similar to:

    Client:
    Version:    28.4.0
    Context:    rootless
    Debug Mode: false

*Context: rootless* incidates rootless is working.

## [Troubleshooting]

### [][Docker service crashes/fails to start (OpenRC)]

After adding `--storage-driver btrfs` to `DOCKER_OPTS` and restarting the Docker service, Docker may crash. Check this with [rc-status].

If this is the case, try adding the `btrfs` USE flag for the Docker package, and updating Docker package.

`root `[`#`]`touch /etc/portage/package.use/docker `

`root `[`#`]`nano /etc/portage/package.use/docker `

[FILE] **`/etc/portage/package.use/docker`**

    app-containers/docker btrfs device-mapper

Install Docker with the new USE flags

`root `[`#`]`emerge --update --deep --newuse app-containers/docker`

Docker service restart

`root `[`#`]`rc-service docker restart`

### [][Docker service fails because cgroup device not mounted (OpenRC)]

On an error like:

    unable to start container process: error during container init: error mounting "cgroup" to rootfs at "/sys/fs/cgroup": mount cgroup:/sys/fs/cgroup/openrc (via /proc/self/fd/6), flags: 0xf, data: openrc: invalid argument

The solution is to set following: [https://github.com/abiosoft/colima/issues/764#issuecomment-1701672142](https://github.com/abiosoft/colima/issues/764#issuecomment-1701672142)

[FILE] **`/etc/rc.conf`**

    rc_cgroup_mode="unified"

and restart

`root `[`#`]`rc-service cgroups restart`

### [][Docker service fails to start (systemd)]

Some users have issues on starting `docker.service` because of device-mapper error. It can be solved by loading a different storage-driver. E.g. Loading "overlay" graph driver instead of "device-mapper" graph driver.

"overlay" graph driver requires \"Overlay filesystem support\" in kernel configuration:

[KERNEL] **Configuring the kernel for Docker**

File systems \-\--\>

       <*> Overlay filesystem support Search for <code>CONFIG_OVERLAY_FS</code> to find this item.

Add following to `/etc/portage/package.use/docker`, then re-emerge Docker will solve this issue:

[FILE] **`/etc/portage/package.use/docker`**

    app-containers/docker overlay -device-mapper

In case of an error saying, `Error starting daemon: Error initializing network controller: list bridge addresses failed: no available network`, the docker0 network bridge may be missing. Please see the following Docker issue which provides a bash script solution to create the docker0 network bridge: [https://github.com/docker/docker/issues/31546](https://github.com/docker/docker/issues/31546)

### [][Docker service runs but fails to start container (systemd)]

If using systemd-232 or higher and receive an error related to [cgroups](https://wiki.gentoo.org/wiki/Cgroups "Cgroups"):

`user `[`$`]`docker run hello-world`

    container_linux.go:247: starting container process caused
    "process_linux.go:359:lib/docker/overlay2/523ed887f681de6ea3838aa5b26c57e88547d65bdd883a6d3538729f19a3
    docker: Error response from daemon: invalid header field value "oci runtime errotainer
    init caused \\\"rootfs_linux.go:54: mounting \\\\\\\"cgroup\\\\\\\" to
    ro38729f19a34501/merged\\\\\\\" at \\\\\\\"/sys/fs/cgroup\\\\\\\" caused \\\\\\\"n

Add the following line to the kernel boot parameters:

[CODE] **Kernel Boot Parameter**

    systemd.legacy_systemd_cgroup_controller=yes

### [][Docker service runs but fails to start container (systemd)]

If using systemd-232 or higher, and it throws this error:

`user `[`$`]`docker run hello-world`

    applying cgroup configuration for process caused \"open /sys/fs/cgroup/docker/cpuset.cpus.effective: no such file or directory

Add the following line to the kernel boot parameters:

[CODE] **Kernel Boot Parameter**

    systemd.unified_cgroup_hierarchy=0

Since systemd v256-rc3, another kernel boot parameter is required to force systemd to enable cgroup v1 support:

[CODE] **Kernel Boot Parameter**

    SYSTEMD_CGROUP_ENABLE_LEGACY_FORCE=1

If using systemd and received this error:

`user `[`$`]`docker run hello-world`

    cgroup mountpoint does not exist

Run the following commands as root:

`root `[`#`]`mkdir /sys/fs/cgroup/systemd`

`root `[`#`]`mount -t cgroup -o none,name=systemd cgroup /sys/fs/cgroup/systemd`

This is not ideal as these commands must be run after each reboot, but it works.

### [][Docker service fails because cgroup device not mounted (systemd)]

By default systemd uses hybrid cgroup hierarchy combining cgroup and cgroup2 devices. Docker still needs cgroup(v1) devices. Activate USE flag `cgroup-hybrid` for systemd.

Activate USE flag for systemd

[FILE] **`/etc/portage/package.use/systemd`**

    sys-apps/systemd cgroup-hybrid

Install systemd with the new USE flags

`root `[`#`]`emerge --ask --oneshot sys-apps/systemd`

### [systemd-networkd]

If `systemd-networkd` is used for network management, additional options are needed for IP forwarding and/or IP masquerade.

[FILE] **`/etc/systemd/network/50-static.network`**

    [Match]
    Name=enp6s0

    [Network]
    DHCP=yes
    IPForward=true
    IPMasquarade=true

These options are used instead of the sysctl settings for ip forwarding and/or masquerade.

In case the Docker containers are shutting down, with errors from `systemd-udevd` that complain of not being able to assign persistent MAC address to virtual interface(s): See [https://github.com/systemd/systemd/issues/3374#issuecomment-339258483](https://github.com/systemd/systemd/issues/3374#issuecomment-339258483)

[FILE] **`/etc/systemd/network/99-default.link`**

    [Link]
    NamePolicy=kernel database onboard slot path
    MACAddressPolicy=none

## [See also]

-   [Docker/Compose](https://wiki.gentoo.org/wiki/Docker/Compose "Docker/Compose") --- a tool for running multi-container applications on [Docker] defined using the Compose file format
-   [Kubernetes](https://wiki.gentoo.org/wiki/Kubernetes "Kubernetes") --- open-source system for automating deployment, scaling, and management of containerized applications
-   [LXC](https://wiki.gentoo.org/wiki/LXC "LXC") --- a [virtualization](https://wiki.gentoo.org/wiki/Virtualization "Virtualization") system that leverages Linux\'s [namespaces](https://wiki.gentoo.org/wiki/Namespaces "Namespaces") and [cgroups](https://wiki.gentoo.org/wiki/Cgroups "Cgroups") to create containers isolated from the host system
-   [Podman](https://wiki.gentoo.org/wiki/Podman "Podman") --- a daemonless container engine for developing, managing, and running [OCI Containers](https://opencontainers.org/), aiming to be a drop-in replacement for much of [Docker]
-   [Project:Docker](https://wiki.gentoo.org/wiki/Project:Docker "Project:Docker") --- provides minimal docker images so that the Gentoo community can have a consistent experience when building application-specific [Docker] containers.
-   [Virtualization](https://wiki.gentoo.org/wiki/Virtualization "Virtualization") --- the concept and technique that permits running software in an environment separate from a computer operating system.

## [External resources]

-   [Official Docker installation documentation](https://docs.docker.com/engine/installation/linux/gentoolinux/)
-   [Docker introduction for beginners](https://docker-curriculum.com/)
-   [nftables firewall for docker](https://stephank.nl/p/2017-06-05-ipv6-on-production-docker.html)
-   [Installing docker on debian with nftables](https://www.naturalborncoder.com/2024/10/installing-docker-on-debian-with-nftables/)
-   [Docker rootless mode](https://docs.docker.com/engine/security/rootless/)