**Resources**

[[]][Home](https://podman.io/)

[[]][Official documentation](https://docs.podman.io/en/latest/)

[[]][Package information](https://packages.gentoo.org/packages/app-containers/podman)

[[]][GitHub](https://github.com/containers/podman)

**Podman** is a daemonless container engine for developing, managing, and running [OCI Containers](https://opencontainers.org/), aiming to be a drop-in replacement for much of [Docker](https://wiki.gentoo.org/wiki/Docker "Docker").

Podman can be used to run containers without the need for a privileged daemon, as required by Docker.

Podman is modular, built around [libpod] and [Open Container Initiative libraries](https://github.com/containers/podman?tab=readme-ov-file#oci-projects-plans). External tools such as [buildah](https://buildah.io/) for building images and and [skopeo](https://github.com/containers/skopeo) for distributing them are used for non-core functionality.^[\[1\]](#cite_note-1)^

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [Kernel]](#Kernel)
        -   [[1.1.1] [Rootless mode]](#Rootless_mode)
            -   [[1.1.1.1] [Configure the kernel]](#Configure_the_kernel)
            -   [[1.1.1.2] [Load required modules]](#Load_required_modules)
            -   [[1.1.1.3] [Configure subuid/subgid]](#Configure_subuid.2Fsubgid)
    -   [[1.2] [USE flags]](#USE_flags)
    -   [[1.3] [Emerge]](#Emerge)
    -   [[1.4] [Additional software]](#Additional_software)
-   [[2] [Configuration]](#Configuration)
    -   [[2.1] [Files]](#Files)
        -   [[2.1.1] [Example: specify the TCP socket for the API service daemon]](#Example:_specify_the_TCP_socket_for_the_API_service_daemon)
-   [[3] [Usage]](#Usage)
    -   [[3.1] [Managing and using images]](#Managing_and_using_images)
        -   [[3.1.1] [Search for available images]](#Search_for_available_images)
        -   [[3.1.2] [Download an image]](#Download_an_image)
        -   [[3.1.3] [List local images]](#List_local_images)
        -   [[3.1.4] [Run command in a temporary container]](#Run_command_in_a_temporary_container)
    -   [[3.2] [Managing and using containers]](#Managing_and_using_containers)
        -   [[3.2.1] [Example: A systemd container for the root user on an OpenRC system]](#Example:_A_systemd_container_for_the_root_user_on_an_OpenRC_system)
    -   [[3.3] [Rootless cgroup operations under OpenRC]](#Rootless_cgroup_operations_under_OpenRC)
    -   [[3.4] [Nvidia in rootless containers]](#Nvidia_in_rootless_containers)
    -   [[3.5] [Exposing containers to local network]](#Exposing_containers_to_local_network)
-   [[4] [Tips]](#Tips)
    -   [[4.1] [Replacing Docker with Podman]](#Replacing_Docker_with_Podman)
-   [[5] [Troubleshooting]](#Troubleshooting)
    -   [[5.1] [Not enough namespaces]](#Not_enough_namespaces)
    -   [[5.2] [Slow storage in the rootless mode]](#Slow_storage_in_the_rootless_mode)
    -   [[5.3] [Rootful netavark nftables error]](#Rootful_netavark_nftables_error)
-   [[6] [See also]](#See_also)
-   [[7] [External resources]](#External_resources)
-   [[8] [References]](#References)

## [Installation]

### [Kernel]

The [runc] upstream provides a method of listing required kernel configuration via [check-config.sh](https://github.com/opencontainers/runc/blob/master/script/check-config.sh) script, but note that some of the config options from the `check-config.sh` script are deprecated and will be safe to ignore.

#### [Rootless mode]

##### [Configure the kernel]

[[[user_namespaces(7)]](https://man.archlinux.org/man/user_namespaces.7.en)[[]](https://wiki.gentoo.org/wiki/Special:MyLanguage/man_page "Special:MyLanguage/man page")] have to be enabled in order to use rootless mode. Many Docker images make use of FUSE and overlayfs, which also need to be enabled. The `tun` kernel module also needs to be available and loaded for rootless mode to access networking.

[KERNEL] **Enable support for Podman**

    General setup  --->
      -*- Namespaces support  ---> Search for <code>CONFIG_NAMESPACES</code> to find this item.
        -*-  User namespace Search for <code>CONFIG_USER_NS</code> to find this item.
    Networking support  --->
      Networking options  --->
      [*] Network packet filtering framework Search for <code>CONFIG_NETFILTER</code> to find this item.
        Core Netfilter Configuration  --->
          <M> Netfilter connection tracking support Search for <code>CONFIG_NF_CONNTRACK</code> to find this item.
          <M> Network Address Translation support Search for <code>CONFIG_NF_NAT</code> to find this item.
           Netfilter Xtables support Search for <code>CONFIG_NETFILTER_XTABLES</code> to find this item.
            <M> nfmark target and match support Search for <code>CONFIG_NETFILTER_XT_MARK</code> to find this item.
            -M- "SNAT and DNAT" targets support Search for <code>CONFIG_NETFILTER_XT_NAT</code> to find this item.
            -M- MASQUERADE target support Search for <code>CONFIG_NETFILTER_XT_TARGET_MASQUERADE</code> to find this item.
            <M> "ipvs" match support Search for <code>CONFIG_NETFILTER_XT_MATCH_IPVS</code> to find this item.
        <M> IP virtual server support Search for <code>CONFIG_IP_VS</code> to find this item.
        IP: Netfilter Configuration  --->
          <M> IP tables support Search for <code>CONFIG_IP_NF_IPTABLES</code> to find this item.
            <M> iptables NAT support Search for <code>CONFIG_IP_NF_NAT</code> to find this item.
              <M> MASQUERADE target support Search for <code>CONFIG_NETFILTER_XT_MATCH_ADDRTYPE</code> to find this item.
              <M> "addrtype" address type match support Search for <code>CONFIG_NETFILTER_XT_MATCH_ADDRTYPE</code> to find this item.
              <M> "comment" match support Search for <code>CONFIG_NETFILTER_XT_MATCH_COMMENT</code> to find this item.
        <M> Ethernet Bridge tables (ebtables) support Search for <code>CONFIG_BRIDGE_NF_EBTABLES</code> to find this item.  -->
          <M> ebt: STP filter support Search for <code>CONFIG_BRIDGE_EBT_STP</code> to find this item.
      <M> 802.1d Ethernet Bridging Search for <code>CONFIG_BRIDGE</code> to find this item.
        [*] IGMP/MLD snooping Search for <code>CONFIG_BRIDGE_IGMP_SNOOPING</code> to find this item.
    Device Drivers  --->
      -*- Network device support  ---> Search for <code>CONFIG_NETDEVICES</code> to find this item.
        -*- Network core driver support  ---> Search for <code>CONFIG_NETDEVICES</code> to find this item.
          <M/*> Universal TUN/TAP device driver support Search for <code>CONFIG_TUN</code> to find this item.
          <M> Virtual ethernet pair device Search for <code>CONFIG_VETH</code> to find this item.
    File systems  --->
      <M/*> FUSE (Filesystem in Userspace) support Search for <code>CONFIG_FUSE_FS</code> to find this item.
      <M/*> Overlay filesystem support Search for <code>CONFIG_OVERLAY_FS</code> to find this item.

##### [Load required modules]

If the `tun` module is not built into the kernel, it needs to be loaded manually:

[FILE] **`/etc/modules-load.d/networking.conf`Load tun module**

    tun

##### [][Configure subuid/subgid]

[podman] requires the user to have a range of UIDs listed in [/etc/subuid] and [/etc/subgid] files. These UIDs are used for mapping the container UIDs to the host UIDs via *user namespaces*.

Refer to the [Subuid subgid](https://wiki.gentoo.org/wiki/Subuid_subgid "Subuid subgid") page for further information.

**Note**: if you use `systemd-homed` to manage the user, the subuid and subgid should be `524288:65536`.

### [USE flags]

### [USE flags for] [app-containers/podman](https://packages.gentoo.org/packages/app-containers/podman) [[]] [A tool for managing OCI containers and pods with Docker-compatible CLI]

  ------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------
  [`+seccomp`](https://packages.gentoo.org/useflags/+seccomp)   Enable seccomp (secure computing mode) to perform system call filtering at runtime to increase security of programs
  [`apparmor`](https://packages.gentoo.org/useflags/apparmor)   Enable support for the AppArmor application security system
  [`btrfs`](https://packages.gentoo.org/useflags/btrfs)         Enable btrfs support (graph driver) in Podman
  [`selinux`](https://packages.gentoo.org/useflags/selinux)     !!internal use only!! Security Enhanced Linux support, this must be set by the selinux profile or breakage will occur
  [`systemd`](https://packages.gentoo.org/useflags/systemd)     Enable use of systemd-specific libraries and features like socket activation or session tracking
  [`wrapper`](https://packages.gentoo.org/useflags/wrapper)     Install a wrapper to allow using \`podman\` as a drop-in replacement for \`docker\`
  ------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-05-06 20:49] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

It is recommended to use [[[app-containers/crun]](https://packages.gentoo.org/packages/app-containers/crun)[]] as the OCI runtime provider, [[[bug #723080]](https://bugs.gentoo.org/show_bug.cgi?id=723080)[]].

`root `[`#`]`emerge --ask --oneshot app-containers/crun`

** Tip**\
From version 4.0.2 (available 2022-03-24), [podman] relies on [crun], so it is unnecessary to install [crun] in advance.

`root `[`#`]`emerge --ask app-containers/podman`

### [Additional software]

-   [[[app-containers/buildah]](https://packages.gentoo.org/packages/app-containers/buildah)[]] is a tool to help build images and containers for use with Podman
-   [[[app-containers/skopeo]](https://packages.gentoo.org/packages/app-containers/skopeo)[]] helps manage image repositories
-   [Podman Desktop](https://podman-desktop.io/) is an open-source [Electron](https://en.wikipedia.org/wiki/Electron_(software_framework) "wikipedia:Electron (software framework)") GUI for managing a Podman installation
-   [[[app-containers/podman-tui]](https://packages.gentoo.org/packages/app-containers/podman-tui)[]] Terminal UI frontend for Podman
-   [[[sec-policy/selinux-podman]](https://packages.gentoo.org/packages/sec-policy/selinux-podman)[]] SELinux policy for Podman
-   [[[app-containers/podman-compose]](https://packages.gentoo.org/packages/app-containers/podman-compose)[]] script to run docker-compose.yml using Podman

## [Configuration]

### [Files]

-   [/etc/containers/registries.conf] - specifies which container registries should be searched for images (see [/etc/containers/registries.conf.example] for example defaults)
-   [/etc/containers/policy.json] - defines policies for image validation (see [/etc/containers/policy.json.example] for example defaults)
-   [/etc/conf.d/podman] - configuration file for the [podman] OpenRC service
-   [/etc/user/conf.d/podman] - configuration file for the [podman] OpenRC user service

#### [Example: specify the TCP socket for the API service daemon]

[FILE] **`/etc/conf.d/podman`**

    #SOCKET="unix:///run/podman/podman.sock"
    SOCKET="tcp://localhost:12979" # this port is an example, choose whatever you want

## [Usage]

The [podman] tool aims to be a drop-in replacement for [docker] client provided by Docker. For example, [docker run] becomes [podman run] and [docker build] becomes [podman build].

All Container Pod-related actions are accessible via [podman pod] command.

### [Managing and using images]

Here are some basic usage examples. Detailed information can be found in the [[[podman-search(1)]](https://man.archlinux.org/man/podman-search.1.en)[[]](https://wiki.gentoo.org/wiki/Special:MyLanguage/man_page "Special:MyLanguage/man page")], [[[podman-pull(1)]](https://man.archlinux.org/man/podman-pull.1.en)[[]](https://wiki.gentoo.org/wiki/Special:MyLanguage/man_page "Special:MyLanguage/man page")], [[[podman-images(1)]](https://man.archlinux.org/man/podman-images.1.en)[[]](https://wiki.gentoo.org/wiki/Special:MyLanguage/man_page "Special:MyLanguage/man page")]. and [[[podman-run(1)]](https://man.archlinux.org/man/podman-run.1.en)[[]](https://wiki.gentoo.org/wiki/Special:MyLanguage/man_page "Special:MyLanguage/man page")] man pages.

** Note**\
Docker uses the [docker.io] registry by default, however Podman recommends [always using fully qualified image names](https://man.archlinux.org/man/containers-registries.conf.5.en#Short-Name_Aliasing) including the registry server, i.e. [\<full dns name\>/\<namespace/\<image name\>:\<tag\>] (e.g. [docker.io/gentoo/stage3:latest]) for security reasons.

#### [Search for available images]

To search for available images, use [podman search]:

`user `[`$`]`podman search docker.io/gentoo`

    NAME                                        DESCRIPTION
    docker.io/osuosl/gentoo
    docker.io/osuosl/gentoo-ppc64le
    docker.io/osuosl/gentoo-i686
    docker.io/centerforopenneuroscience/opfvta  Gentoo based container for a reproducible an...
    docker.io/gentoo/stage3                     Official Gentoo stage3 images.
    docker.io/gentoo/portage                    Official Gentoo Portage snapshot. Designed t...
    ...

#### [Download an image]

To download an image, use [podman pull]:

`user `[`$`]`podman pull docker.io/gentoo/stage3`

    Trying to pull docker.io/gentoo/stage3:latest...
    Getting image source signatures
    Copying blob 93476f02ccbb done   |
    Copying config eb88956325 done   |
    Writing manifest to image destination
    eb8895632523167a51c60f247fbce008ca99bd54924c26f3ec3371c20524d88c

#### [List local images]

To list images available locally, run [podman images]:

`user `[`$`]`podman images`

    $ podman images
    REPOSITORY               TAG         IMAGE ID      CREATED     SIZE
    docker.io/gentoo/stage3  latest      eb8895632523  3 days ago  1.34 GB

#### [Run command in a temporary container]

To use an image to interactively run a command in a new container, removing that container once it\'s exited:

`user `[`$`]`podman run --interactive --tty --rm docker.io/gentoo/stage3:latest /usr/bin/bash`

The `--interactive` and `--tty` options can be abbreviated as `-i` and `-t`, respectively.

### [Managing and using containers]

All existing containers, running or not, can be listed via [podman container]:

`user `[`$`]`podman container list -a`

Without the `-a` option, only running containers will be listed.

Containers can be created, but not started, by using the [create]; subcommand if a name is not supplied, a name will be generated automatically.

`user `[`$`]`podman create --interactive --tty --name gentoo-bash docker.io/gentoo/stage3:latest /usr/bin/bash`

Containers can be started, restarted and stopped via the [start], [restart] and [stop] subcommands, e.g.:

`user `[`$`]`podman start gentoo-bash`

Running containers can be listed via the [ps] subcommand:

`user `[`$`]`podman ps`

Adding the `-a` option will list all containers, running or not.

A container can be deleted via the [rm] subcommand:

`user `[`$`]`podman rm gentoo-bash`

Detailed information can be found in the [[[podman-container(1)]](https://man.archlinux.org/man/podman-container.1.en)[[]](https://wiki.gentoo.org/wiki/Special:MyLanguage/man_page "Special:MyLanguage/man page")], [[[podman-create(1)]](https://man.archlinux.org/man/podman-create.1.en)[[]](https://wiki.gentoo.org/wiki/Special:MyLanguage/man_page "Special:MyLanguage/man page")], [[[podman-start(1)]](https://man.archlinux.org/man/podman-start.1.en)[[]](https://wiki.gentoo.org/wiki/Special:MyLanguage/man_page "Special:MyLanguage/man page")], [[[podman-ps(1)]](https://man.archlinux.org/man/podman-ps.1.en)[[]](https://wiki.gentoo.org/wiki/Special:MyLanguage/man_page "Special:MyLanguage/man page")], and [[[podman-rm(1)]](https://man.archlinux.org/man/podman-rm.1.en)[[]](https://wiki.gentoo.org/wiki/Special:MyLanguage/man_page "Special:MyLanguage/man page")] man pages.

#### [Example: A systemd container for the root user on an OpenRC system]

Create a container named \"gentoo-systemd\", fetching the base image if necessary, that will run that image\'s [init] command:

`root `[`#`]`podman create --interactive --tty --name gentoo-systemd docker.io/gentoo/stage3:systemd /usr/sbin/init`

Set the password for the root user by mounting the container\'s root filesystem and using [[[passwd(1)]](https://man.archlinux.org/man/passwd.1.en)[[]](https://wiki.gentoo.org/wiki/Special:MyLanguage/man_page "Special:MyLanguage/man page")] to change it:

`root `[`#`]`podman mount gentoo-systemd`

`root `[`#`]`passwd -R [mount directory]`

`root `[`#`]`podman unmount gentoo-systemd`

Start the container and immediately attach to it:

`root `[`#`]`podman start --attach gentoo-systemd`

This should result in a boot sequence and a login prompt. Once logged in, confirm that systemd is PID 1 by running [systemctl status].

### [Rootless cgroup operations under OpenRC]

** Warning**\
The following configuration might have security issues, as described in [Talk:Podman](https://wiki.gentoo.org/wiki/Talk:Podman#Potential_security_issues_in_.22Rootless_containers_under_OpenRC.22_setup "Talk:Podman"). It\'s generally not necessary for most uses of podman

On systemd-based systems, Podman uses systemd slices to allow Podman to operate on cgroups without requiring root permissions.

On OpenRC-based systems, some extra configuration is required, and an extra option needs to be added to the `podman start` command line.

Create a new group, `cgroup`:

`root `[`#`]`groupadd cgroup`

Add the non-privileged user to this group:

`root `[`#`]`usermod -aG cgroup larry`

As root, create a file in [/etc/local.d](https://wiki.gentoo.org/wiki//etc/local.d "/etc/local.d") called e.g. [01-podman-rootless.start] - modifying the leading number if that number is already in use - with the following contents^[\[2\]](#cite_note-2)^:

[FILE] **`/etc/local.d/01-podman-rootless.start`**

    #!/bin/sh

    # Allow users in the 'cgroup' group to use Podman containers rootless.

    mount --make-rshared /

    chown root:cgroup /sys/fs/cgroup
    chmod 775 /sys/fs/cgroup

    chown root:cgroup /sys/fs/cgroup/cgroup.procs
    chown root:cgroup /sys/fs/cgroup/cgroup.subtree_control
    chown root:cgroup /sys/fs/cgroup/cgroup.threads
    chmod 664 /sys/fs/cgroup/cgroup.procs
    chmod 664 /sys/fs/cgroup/cgroup.subtree_control
    chmod 664 /sys/fs/cgroup/cgroup.threads

Make that file executable by root:

`root `[`#`]`chmod 744 /etc/local.d/01-podman-rootless.start`

Reboot the system.

After logging in as the non-privileged user, run the [[[groups(1)]](https://man.archlinux.org/man/groups.1.en)[[]](https://wiki.gentoo.org/wiki/Special:MyLanguage/man_page "Special:MyLanguage/man page")] command to confirm that the user is in the `cgroup` group.

The user should then be able to utilize podman cgroup operations by adding `--cgroup-manager=cgroupfs` option to the `podman start` command line:

`user `[`$`]`podman --cgroup-manager=cgroupfs start --attach gentoo-systemd`

### [Nvidia in rootless containers]

The [[[nvidia-container-toolkit::guru]](https://gpo.zugaina.org/Overlays/guru/nvidia-container-toolkit)[]] package is available in the [GURU](https://wiki.gentoo.org/wiki/Project:GURU "Project:GURU") repository. The repository can be enabled with the help of [[[app-eselect/eselect-repository]](https://packages.gentoo.org/packages/app-eselect/eselect-repository)[]] utility; refer to the [eselect/repository](https://wiki.gentoo.org/wiki/Eselect/Repository "Eselect/Repository") page for information about how to enable and sync a repository.

Once the [guru] repository is set up, install the package:

`root `[`#`]`emerge --ask app-containers/nvidia-container-toolkit`

Generate the CDI specification file.

`root `[`#`]`nvidia-ctk cdi generate --output=/etc/cdi/nvidia.yaml`

Enable sharing user groups inside containers in user configuration file.

[FILE] **`~/.config/containers/containers.conf`**

    [containers]
    annotations=["run.oci.keep_original_groups=1",]

### [Exposing containers to local network]

By default, [podman] works in *bridge mode*, with a separate **cni-podman0** bridge; requests are translated to the local network via NAT. However, the root user can give pods/containers real IP addresses on the local network using *macvlan* mode.

First enable and start the **cni-dhcp** daemon:

`root `[`#`]`rc-update add cni-dhcp default`

`root `[`#`]`rc-service cni-dhcp start `

Add a new network configuration for [podman] to support *macvlan* networks:

[FILE] **`/etc/cni/net.d/88-macvlan.conflist`**


        },

        },
        ,

      ]
    }

The above assumes there is an externally configured bridge [br0] already in existence; an example of such a configuration is available on the [Network bridge](https://wiki.gentoo.org/wiki/Network_bridge#Single_NIC_bridge "Network bridge") page. It is also possible to use an existing Ethernet device (e.g. [enp5s0f0]) and attach to it.

Now create a pod with the newly-configured network:

`root `[`#`]`podman pod create --name homeserver --network macvlan`

To validate that the pod has the proper configuration, an Alpine test container can be run inside the pod:

`root `[`#`]`podman run -dt --pod homeserver --name alpine_test docker.io/library/alpine:latest top `

`root `[`#`]`podman exec alpine_test ip addr`

    1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
        link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
        inet 127.0.0.1/8 brd 127.255.255.255 scope host lo
           valid_lft forever preferred_lft forever
        inet6 ::1/128 scope host proto kernel_lo
           valid_lft forever preferred_lft forever
    2: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast state UP group default qlen 1000
        link/ether 3A:09:C6:B8:7F:DB brd ff:ff:ff:ff:ff:ff
        inet 192.168.2.121/24 brd 192.168.2.255 scope global dynamic noprefixroute enp5s0
           valid_lft 85793sec preferred_lft 74993sec
        inet6 fe80::ab3d:b093:a223:776a/64 scope link noprefixroute
           valid_lft forever preferred_lft forever
        inet6 fe80::8c32:bb30:5827:8c34/64 scope link
           valid_lft forever preferred_lft forever

## [Tips]

### [Replacing Docker with Podman]

For most user applications running Docker images, setting `alias docker=podman` should be enough for most pipelines to switch to [podman].

When replacing Docker with Podman, [[[app-containers/buildah]](https://packages.gentoo.org/packages/app-containers/buildah)[]] may be used for building images and [[[app-containers/skopeo]](https://packages.gentoo.org/packages/app-containers/skopeo)[]] for distributing them.

It is possible to configure Podman to use the [docker.io] registry by default, however this comes with security considerations so be sure to read [the appropriate documentation](https://man.archlinux.org/man/containers-registries.conf.5.en#Short-Name_Aliasing) if considering this configuration.

## [Troubleshooting]

### [Not enough namespaces]

If running a container results in the message:

    error creating libpod runtime: there might not be enough IDs available in the namespace

then increase the number of user [namespaces](https://wiki.gentoo.org/wiki/Namespaces "Namespaces") via the relevant kernel parameter, either temporarily via [[[sysctl(8)]](https://man.archlinux.org/man/sysctl.8.en)[[]](https://wiki.gentoo.org/wiki/Special:MyLanguage/man_page "Special:MyLanguage/man page")]:

`root `[`#`]`sysctl user.max_user_namespaces=15076`

or permanently via a line in [/etc/sysctl.d/local.conf]:

[FILE] **`/etc/sysctl.d/local.conf`**

    user.max_user_namespaces=15076

### [Slow storage in the rootless mode]

Check the storage driver being used:

`user `[`$`]`podman info -f }`

If the reported storage driver is `vfs`, consider switching to a faster `overlayfs`.

See [Choosing a storage driver](https://github.com/containers/podman/blob/main/docs/tutorials/performance.md#choosing-a-storage-driver)

### [Rootful netavark nftables error]

When using rootful Podman with netavark and nftables, containers may fail to start with:

    Error: netavark: nftables error: "nft" did not return successfully while applying ruleset
    internal:0:0-0: Error: Could not process rule: No such file or directory

One common cause is missing kernel support for inet fib lookups in nf_tables.

Required kernel option:

    CONFIG_NFT_FIB_INET=y (or module)

Without this option, netavark rules using fib daddr type local in the inet family can fail, even if general nftables NAT support appears to work.

Notes:

-   This affects rootful networking paths that use netavark nftables firewall programming.
-   The netdev fib option (CONFIG_NFT_FIB_NETDEV) is not required for this specific failure.
-   Rootful + nftables is useful when you want production-grade host networking control from containers. This means real host-level firewalling and NAT: netavark can program nft rules directly for port publishing and isolation.

## [See also]

-   [Docker](https://wiki.gentoo.org/wiki/Docker "Docker") --- a [container](https://en.wikipedia.org/wiki/Container_(virtualization) "wikipedia:Container (virtualization)")-based [virtualization](https://wiki.gentoo.org/wiki/Virtualization "Virtualization") system
-   [Kubernetes](https://wiki.gentoo.org/wiki/Kubernetes "Kubernetes") --- open-source system for automating deployment, scaling, and management of containerized applications
-   [Virtualization](https://wiki.gentoo.org/wiki/Virtualization "Virtualization") --- the concept and technique that permits running software in an environment separate from a computer operating system.

## [External resources]

-   [[[podman(1)]](https://man.archlinux.org/man/podman.1.en)[[]](https://wiki.gentoo.org/wiki/Special:MyLanguage/man_page "Special:MyLanguage/man page")]
-   [[[podman-create(1)]](https://man.archlinux.org/man/podman-create.1.en)[[]](https://wiki.gentoo.org/wiki/Special:MyLanguage/man_page "Special:MyLanguage/man page")]
-   [[[podman-container(1)]](https://man.archlinux.org/man/podman-container.1.en)[[]](https://wiki.gentoo.org/wiki/Special:MyLanguage/man_page "Special:MyLanguage/man page")]
-   [[[podman-images(1)]](https://man.archlinux.org/man/podman-images.1.en)[[]](https://wiki.gentoo.org/wiki/Special:MyLanguage/man_page "Special:MyLanguage/man page")]
-   [[[podman-mount(1)]](https://man.archlinux.org/man/podman-mount.1.en)[[]](https://wiki.gentoo.org/wiki/Special:MyLanguage/man_page "Special:MyLanguage/man page")]
-   [[[podman-ps(1)]](https://man.archlinux.org/man/podman-ps.1.en)[[]](https://wiki.gentoo.org/wiki/Special:MyLanguage/man_page "Special:MyLanguage/man page")]
-   [[[podman-pull(1)]](https://man.archlinux.org/man/podman-pull.1.en)[[]](https://wiki.gentoo.org/wiki/Special:MyLanguage/man_page "Special:MyLanguage/man page")]
-   [[[podman-restart(1)]](https://man.archlinux.org/man/podman-restart.1.en)[[]](https://wiki.gentoo.org/wiki/Special:MyLanguage/man_page "Special:MyLanguage/man page")]
-   [[[podman-rm(1)]](https://man.archlinux.org/man/podman-rm.1.en)[[]](https://wiki.gentoo.org/wiki/Special:MyLanguage/man_page "Special:MyLanguage/man page")]
-   [[[podman-run(1)]](https://man.archlinux.org/man/podman-run.1.en)[[]](https://wiki.gentoo.org/wiki/Special:MyLanguage/man_page "Special:MyLanguage/man page")]
-   [[[podman-search(1)]](https://man.archlinux.org/man/podman-search.1.en)[[]](https://wiki.gentoo.org/wiki/Special:MyLanguage/man_page "Special:MyLanguage/man page")]
-   [[[podman-start(1)]](https://man.archlinux.org/man/podman-start.1.en)[[]](https://wiki.gentoo.org/wiki/Special:MyLanguage/man_page "Special:MyLanguage/man page")]
-   [[[podman-stop(1)]](https://man.archlinux.org/man/podman-stop.1.en)[[]](https://wiki.gentoo.org/wiki/Special:MyLanguage/man_page "Special:MyLanguage/man page")]
-   [[[podman-unmount(1)]](https://man.archlinux.org/man/podman-unmount.1.en)[[]](https://wiki.gentoo.org/wiki/Special:MyLanguage/man_page "Special:MyLanguage/man page")]

## [References]

1.  [[[↑](#cite_ref-1)] [[A Comprehensive Container Runtime Comparison](https://www.capitalone.com/tech/cloud/container-runtime/), Retrieved on January 18, 2021]]
2.  [[[↑](#cite_ref-2)] [[Linux kernel user\'s and administrator\'s guide: \"Control Group v2\" / \"Delegation\"](https://www.kernel.org/doc/html/v4.18/admin-guide/cgroup-v2.html#delegation)]]