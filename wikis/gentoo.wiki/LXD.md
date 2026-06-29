*Not to be confused with [the LXDE desktop environment](https://wiki.gentoo.org/wiki/LXDE "LXDE").*

**Resources**

[[]][Home](https://linuxcontainers.org/lxd/introduction/)

[[]][Official documentation](https://linuxcontainers.org/lxd/docs/master/)

[[]][Package information](https://packages.gentoo.org/packages/app-containers/lxd)

[[]][GitHub](https://github.com/lxc/lxd)

[[]][Bugs (upstream)](https://github.com/lxc/lxd/issues)

[[]][[#lxc](ircs://irc.libera.chat/#lxc)] ([[webchat](https://web.libera.chat/#lxc)])

**LXD** is a system container manager. The core of LXD is a privileged daemon which exposes a [REST API](https://en.wikipedia.org/wiki/REST_API "wikipedia:REST API") over a local Unix socket as well as over the network (if enabled)^[\[1\]](#cite_note-1)^.

LXD isn\'t a rewrite of [LXC](https://wiki.gentoo.org/wiki/LXC "LXC"); in fact it is built on top of LXC to provide a new, better user experience. Under the hood, LXD uses LXC through *liblxc* and its Go binding to create and manage the containers. It\'s basically an alternative to LXC\'s tools and distribution template system with the added features that come from being controllable over the network.

For those new to container technology, it can be useful to first read the [LXC Virtualization Concepts](https://wiki.gentoo.org/wiki/LXC#Virtualization_concepts "LXC") article.

Key features of LXD include:

-   It prefers to launch unprivileged containers (secure by default).
-   A command-line client ([lxc]) interacts with a daemon ([lxd]).
-   Configuration is made intuitive and scriptable through cascading profiles.
-   Configuration changes are performed with the [lxc] command (not config files).
-   Multiple hosts can be federated together (with a certificate-based trust system).
-   A federated setup means that containers can be launched on remote machines and live-migrated between hosts (using [CRIU](https://wiki.gentoo.org/index.php?title=CRIU&action=edit&redlink=1 "CRIU (page does not exist)") technology).
-   It is usable as a standalone [hypervisor](https://en.wikipedia.org/wiki/Hypervisor "wikipedia:Hypervisor") or integrated with [Openstack](https://wiki.gentoo.org/wiki/Openstack "Openstack") Nova

** Note**\
Some users might wish to consider [incus](https://wiki.gentoo.org/wiki/Incus "Incus"), a fork of LXD now maintained by [Linux Containers](https://linuxcontainers.org/), created after [LXD was relicensed as AGPLv3](https://stgraber.org/2023/12/12/lxd-now-re-licensed-and-under-a-cla/). Incus remains under the Apache 2.0 license; information about the initial release, including changes from LXD, is available [here](https://discuss.linuxcontainers.org/t/incus-0-1-has-been-released/18036).

## Contents

-   [[1] [Quick start (single host)]](#Quick_start_.28single_host.29)
    -   [[1.1] [Prepare the system]](#Prepare_the_system)
        -   [[1.1.1] [Kernel configuration]](#Kernel_configuration)
        -   [[1.1.2] [Emerge]](#Emerge)
        -   [[1.1.3] [Authorize a non-privileged user]](#Authorize_a_non-privileged_user)
        -   [[1.1.4] [Configure subuid/subgid]](#Configure_subuid.2Fsubgid)
        -   [[1.1.5] [Start the daemon]](#Start_the_daemon)
            -   [[1.1.5.1] [OpenRC]](#OpenRC)
            -   [[1.1.5.2] [systemd]](#systemd)
            -   [[1.1.5.3] [Configuration]](#Configuration)
        -   [[1.1.6] [Setup storage and networking]](#Setup_storage_and_networking)
        -   [[1.1.7] [Configure the bridge]](#Configure_the_bridge)
    -   [[1.2] [Launch a container]](#Launch_a_container)
        -   [[1.2.1] [Make your own container images]](#Make_your_own_container_images)
-   [[2] [Configuration]](#Configuration_2)
    -   [[2.1] [Example]](#Example)
-   [[3] [Multi-host setup]](#Multi-host_setup)
    -   [[3.1] [Setup]](#Setup)
    -   [[3.2] [Result]](#Result)
-   [[4] [Virtual machines]](#Virtual_machines)
    -   [[4.1] [Allocating resources in a virtual machine]](#Allocating_resources_in_a_virtual_machine)
        -   [[4.1.1] [CPU]](#CPU)
        -   [[4.1.2] [Disk size]](#Disk_size)
        -   [[4.1.3] [Memory]](#Memory)
        -   [[4.1.4] [Network]](#Network)
-   [[5] [Advanced features]](#Advanced_features)
    -   [[5.1] [Live migration]](#Live_migration)
    -   [[5.2] [Automatic BTRFS integration]](#Automatic_BTRFS_integration)
    -   [[5.3] [/dev/lxd/sock]](#.2Fdev.2Flxd.2Fsock)
    -   [[5.4] [Graphical (X) applications in a container]](#Graphical_.28X.29_applications_in_a_container)
-   [[6] [Troubleshooting]](#Troubleshooting)
    -   [[6.1] [Containers freeze on \'lxc stop\' with OpenRC (+ SysVinit)]](#Containers_freeze_on_.27lxc_stop.27_with_OpenRC_.28.2B_SysVinit.29)
    -   [[6.2] [Running systemd based containers on OpenRC hosts]](#Running_systemd_based_containers_on_OpenRC_hosts)
        -   [[6.2.1] [Alternative way (lxd-4.0.9)]](#Alternative_way_.28lxd-4.0.9.29)
    -   [[6.3] [Using LXD with self-spun ZFS pools]](#Using_LXD_with_self-spun_ZFS_pools)
    -   [[6.4] [Too many open files on OpenRC hosts]](#Too_many_open_files_on_OpenRC_hosts)
-   [[7] [See also]](#See_also)
-   [[8] [External Resources]](#External_Resources)

## [][Quick start (single host)]

### [Prepare the system]

#### [Kernel configuration]

It is a good idea to have most kernel flags required by [[[app-containers/lxc]](https://packages.gentoo.org/packages/app-containers/lxc)[]] and [[[sys-process/criu]](https://packages.gentoo.org/packages/sys-process/criu)[]].

`root `[`#`]`ebuild /var/db/repos/gentoo/app-containers/lxc/lxc-4.0.6.ebuild setup`

    ...
     * Checking for suitable kernel configuration options...
     *   CONFIG_NETLINK_DIAG:  needed for lxc-checkpoint
     *   CONFIG_PACKET_DIAG:  needed for lxc-checkpoint
     *   CONFIG_INET_UDP_DIAG:  needed for lxc-checkpoint
     *   CONFIG_INET_TCP_DIAG:  needed for lxc-checkpoint
     *   CONFIG_UNIX_DIAG:  needed for lxc-checkpoint
     *   CONFIG_CHECKPOINT_RESTORE:  needed for lxc-checkpoint
     * Please check to make sure these options are set correctly.
     * Failure to do so may cause unexpected problems.
    |ebuild /var/db/repos/gentoo/sys-process/criu/criu-1.6.1.ebuild setup
    ...

Do you have plans for running systemd-based unprivileged containers? You will probably need to enable the \"Gentoo Linux -\> Support for init systems, system and service managers -\> systemd\" (CONFIG_GENTOO_LINUX_INIT_SYSTEMD)

#### [Emerge]

`root `[`#`]`emerge --ask app-containers/lxd`

#### [Authorize a non-privileged user]

All members of the [lxd] group can use *any* of the available containers, irrespective of who created the container.

`root `[`#`]`usermod --append --groups lxd larry`

This will allow a non-root user to interact with the control socket which is owned by the [lxd] UNIX group.\
For the group change to take effect, users need to log out and log back in again.

#### [][Configure subuid/subgid]

LXD requires that subuids and subgids for the `lxd` user are propely configured. An overview for the recommended configuration of subuid/subgids is given in the wiki - [Subuid subgid](https://wiki.gentoo.org/wiki/Subuid_subgid "Subuid subgid").

#### [Start the daemon]

##### [OpenRC]

The [lxd] service is available and can be added to the [default] runlevel:

`root `[`#`]`rc-update add lxd default `

`root `[`#`]`rc-service lxd start `

##### [systemd]

The systemd unit file has also been installed.

##### [Configuration]

[/etc/conf.d/lxd] has a few available options related to debug output, but the defaults are adequate for this quick start.\'

#### [Setup storage and networking]

`root `[`#`]`lxd init`

    Would you like to use LXD clustering? (yes/no) [default=no]:
    Do you want to configure a new storage pool (yes/no) [default=yes]?
    Name of the new storage pool [default=default]:
    Name of the storage backend to use (dir, lvm) [default=dir]:
    Would you like to connect to a MAAS server? (yes/no) [default=no]:
    Would you like to create a new network bridge (yes/no) [default=yes]? no
    Would you like to configure LXD to use an existing bridge or host interface? (yes/no) [default=no]:
    Would you like LXD to be available over the network? (yes/no) [default=no]:
    Would you like stale cached images to be updated automatically? (yes/no) [default=yes]:
    Would you like a YAML "lxd init" preseed to be printed? (yes/no) [default=no]:

#### [Configure the bridge]

If a new bridge was created by `lxd init`, start it now.

`root `[`#`]`rc-service net.lxcbr0 start`

If desired, the bridge can be configured to come up automatically in the runlevel.

`root `[`#`]`rc-update add net.lxcbr0 default`

### [Launch a container]

Add an image repository at a remote called \"images\":

`user `[`$`]`lxc remote add images https://images.linuxcontainers.org`

This is an untrusted remote, which can be a source of images that have been published with the \--public flag. Trusted remotes are also possible, and are used as container hosts and also to serve private images. This specific remote is not special to LXD; organizations may host their own images.

`user `[`$`]`lxc image list images:`

    +--------------------------------+--------------+--------+-------------------------+---------+-------------------------------+
    |             ALIAS              | FINGERPRINT  | PUBLIC |       DESCRIPTION       |  ARCH   |          UPLOAD DATE          |
    +--------------------------------+--------------+--------+-------------------------+---------+-------------------------------+
    |                                | 3ae185265c53 | yes    | Centos 6 (amd64)        | x86_64  | Aug 29, 2015 at 10:17pm (CDT) |
    |                                | 369ac13f390e | yes    | Centos 6 (amd64)        | x86_64  | Sep 3, 2015 at 12:17pm (CDT)  |
    | centos/6/amd64 (1 more)        | 8e54c679f1c2 | yes    | Centos 6 (amd64)        | x86_64  | Sep 3, 2015 at 10:17pm (CDT)  |
    |                                | 755542362bbb | yes    | Centos 6 (i386)         | i686    | Aug 29, 2015 at 10:19pm (CDT) |
    |                                | b4d26dbc6567 | yes    | Centos 6 (i386)         | i686    | Sep 3, 2015 at 12:20pm (CDT)  |
    | centos/6/i386 (1 more)         | 21eeba48a2d4 | yes    | Centos 6 (i386)         | i686    | Sep 3, 2015 at 10:19pm (CDT)  |
    |                                | 9fe7ffdbc0ae | yes    | Centos 7 (amd64)        | x86_64  | Aug 29, 2015 at 10:22pm (CDT) |
    |                                | d750b910e62d | yes    | Centos 7 (amd64)        | x86_64  | Sep 3, 2015 at 12:23pm (CDT)  |
    | centos/7/amd64 (1 more)        | 06c4e5c21707 | yes    | Centos 7 (amd64)        | x86_64  | Sep 3, 2015 at 10:22pm (CDT)  |
    |                                | ee229d68be51 | yes    | Debian jessie (amd64)   | x86_64  | Aug 29, 2015 at 6:29pm (CDT)  |
    |                                | 69e457e1f4ab | yes    | Debian jessie (amd64)   | x86_64  | Sep 2, 2015 at 6:34pm (CDT)   |
    | debian/jessie/amd64 (1 more)   | 2ddd14ff9422 | yes    | Debian jessie (amd64)   | x86_64  | Sep 3, 2015 at 6:30pm (CDT)   |
    |                                | 9fac01d1e773 | yes    | Debian jessie (armel)   | armv7l  | Aug 31, 2015 at 7:24pm (CDT)  |
    |                                | 67f4fedafd2f | yes    | Debian jessie (armel)   | armv7l  | Sep 1, 2015 at 7:24pm (CDT)   |
    ...

There are Gentoo images in the list, although they are not maintained by the Gentoo project. LXC users may recognize these images as the same ones available using the \"download\" template.

`user `[`$`]`lxc launch images:centos/6/amd64 mycentos6`

    Creating mycentos6 done.
    Starting mycentos6 done.

`user `[`$`]`lxc list`

    +-----------+---------+----------------+------+-----------+-----------+
    |   NAME    |  STATE  |      IPV4      | IPV6 | EPHEMERAL | SNAPSHOTS |
    +-----------+---------+----------------+------+-----------+-----------+
    | mycentos6 | RUNNING | 192.168.43.240 |      | NO        | 0         |
    +-----------+---------+----------------+------+-----------+-----------+

A shell can be run in the container\'s context.

`user `[`$`]`lxc exec mycentos6 /bin/bash`

    [root@mycentos6 ~]# ps faux
    USER       PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
    root       428  0.0  0.0  11500  2648 ?        Ss   16:13   0:00 /bin/bash
    root       440  0.0  0.0  13380  1888 ?        R+   16:13   0:00  \_ ps faux
    root         1  0.0  0.0  19292  2432 ?        Ss   16:03   0:00 /sbin/init
    root       188  0.0  0.0   4124  1316 console  Ss+  16:03   0:00 /sbin/mingetty --nohangup console
    root       228  0.0  0.0   9180  1392 ?        Ss   16:03   0:00 /sbin/dhclient -H mycentos6 -1 -q -lf /var/lib/dhclient/dhclient-eth0.leases -pf /var/run/dhc
    root       278  0.0  0.0 171372  2544 ?        Sl   16:03   0:00 /sbin/rsyslogd -i /var/run/syslogd.pid -c 5
    root       439  0.0  0.0   4120  1472 ?        Ss   16:13   0:00 /sbin/mingetty --nohangup /dev/tty[1-6]

While the container sees its processes as running as the root user, running `ps` on the host shows the processes running as UID 1000000. This is the advantage of unprivileged containers: root is only root in the container, and is nobody special in the host. It is possible to manipulate the subuid/subgid maps to allow containers access to host resources (for example, write to the host\'s X socket) but this must be explicitly allowed.

#### [Make your own container images]

Use a tool called [Distrobuilder#Create_your_own_container_images](https://wiki.gentoo.org/wiki/Distrobuilder#Create_your_own_container_images "Distrobuilder").

## [Configuration]

Configuration of containers is managed with the `lxc config` and `lxc profile` commands. The two commands provide largely the same capabilities, but `lxc config` acts on single containers while `lxc profile` configures a profile which can be used across multiple containers.

Importantly, containers can be launched with multiple profiles. The profiles have a cascading effect so that a profile specified later in the list can add, remove, and override configuration values that were specified in a earlier profile. This can allow for complex setups where groups of containers can be specified which share some properties but not others.

`user `[`$`]`lxc profile list`

    default
    migratable

`user `[`$`]`lxc profile show default`

    name: default
    config:
    devices:
      eth0:
        nictype: bridged
        parent: lxcbr0
        type: nic

The default profile is applied if no profile is specified on the command line. In the quick start, the `lxc launch` omitted the profile, and so was equivalent to:

`user `[`$`]`lxc launch images:centos/6/amd64 mycentos6 --profile default`

Notice that that the default profile only specifies that a container should have a single NIC which is bridged onto an existing bridge lxcbr0. So, having a bridge with that name is not a hard requirement, it just happens to be named in the default profile.

Available configuration includes limits on memory and CPU cores, and also devices including NICs, bind mounts, and block/character device nodes.

Configuration is documented in [/usr/share/doc/lxd-0.16/specs/configuration.md] (substitute the correct version of course).

** Important**\
All documented configuration options are not yet implemented, and only by inspecting source code can a user know which devices might be expected to work. For example, at the time of this writing:

-   The only legal nictype for an interface is \"bridged\"
-   The \"disk\" device type can only perform bind mounts, and only on a directory.
-   Setting limits.memory seems not to work, although limits.cpus does

### [Example]

Here a container is launched with the default profile and also a \"cpusandbox\" profile which imposes a limit of one CPU core. A directory on the host is also bind-mounted into the container using the container-specific `lxc config` command.

First, prepare a reusable profile.

`user `[`$`]`lxc profile create cpusandbox`

    Profile cpusandbox created

`user `[`$`]`lxc profile set cpusandbox limits.cpu 1`

`lxc config` requires a container name, so a container is initialized.

`user `[`$`]`lxc init 8e54c679f1c2 confexample --profile default --profile cpusandbox`

    Creating confexample done.

** Note**\
The 8e54c679f1c2 argument represents an image fingerprint obtained with `lxc image list`. It\'s possible to give friendly aliases to images.

** Note**\
In the quick start above the `lxc launch` was invoked, which is a shorthand to `lxc init` followed by `lxc start`. The latter is used in this example so that `lxc config` can be invoked before the container is first started.

In this example a host directory [/tmp/shared] is bind-mounted into the container at [/tmp]. While this could be configured in a profile, instead it will be considered an exclusive feature for that container.

`user `[`$`]`mkdir /tmp/shared`

`user `[`$`]`touch /tmp/shared/hello.txt`

Set the directory to be owned by the container\'s root user (really UID 1000000 in the host).

`user `[`$`]`sudo chown -R 1000000:1000000 /tmp/shared`

`user `[`$`]`lxc config device add confexample sharedtmp disk path=/tmp source=/tmp/shared`

    Device sharedtmp added to confexample

`user `[`$`]`lxc start confexample`

`user `[`$`]`lxc exec confexample ls /tmp`

    hello.txt

## [Multi-host setup]

Two hosts on a network, alpha and beta, are running the lxd daemon. The goal is to run commands on alpha which can manipulate containers and images on either alpha or beta.

** Note**\
Resolvable names are prepared for readability but it also works to use IP addresses.

### [Setup]

Configure the daemon on the remote to listen over HTTPS instead of the default local Unix socket.

`beta $``lxc config set core.https_address beta:8443`

Restart the daemon after this step, and be sure that the firewall will accept incoming connections as specified.

On beta configure a trust password, which is only used until certificates are exchanged.

`beta $``lxc config set core.trust_password Sieth9gei7ahm2ra`

Add the beta remote to alpha.

`alpha $``lxc remote add beta https://beta:8443`

    Certificate fingerprint: 7a 76 5b c6 c6 eb 4e db 20 7f 31 bb 1d 11 ca 2d c5 d8 7d cf 41 c0 a0 1f aa 8b c3 f0 18 79 d3 a3
    ok (y/n)? y
    Admin password for beta:
    Client certificate stored at server:  beta

### [Result]

It is now possible to perform actions on beta from alpha using the remote: syntax

`alpha $``lxc list beta:`

`alpha $``lxc remote list beta:`

`alpha $``lxc launch beta:centos6 beta:container0`

`alpha $``lxc info beta:container0`

To copy containers or images, the source (\"from\") host must have its daemon listening via HTTPS not Unix socket.

`alpha $``lxc image copy beta:gentlean local:`

`alpha $``lxc image copy centos6 beta:`

    error: The source remote isn't available over the network

** Note**\
As long as commands were run from alpha, it was never necessary to add alpha as a remote to either host. It was also not necessary to change alpha\'s core.https_address config setting to use HTTPS instead of Unix socket unless it is the source of a container or image copy.

** Note**\
Configuration settings and profiles are only set on the local host. They can be copied to remotes but this is manual and error-prone unless configuration managment tools are used to propagate these values. Consider requiring all commands to be run from a single host with its local config database for ease of administration.

\

## [Virtual machines]

LXD can use [QEMU](https://wiki.gentoo.org/wiki/QEMU "QEMU") to run virtual machines. The [default image server](https://images.linuxcontainers.org/) already hosts many virtual machine alternatives, even pre-configured desktop vm images. You\'ll find virtual machine images by checking the \"TYPE\"-field. Many pre-configured desktop images can be found with a \"desktop\" in their description.

`user `[`$`]`lxc image list images: | grep -i desktop`

Running and operating virtual machines requires [QEMU](https://wiki.gentoo.org/wiki/QEMU "QEMU") to be installed, with the following USE-flags enabled: spice, usbredir, virtfs.

[FILE] **`/etc/portage/package.use/qemu`**

    app-emulation/qemu spice usbredir virtfs

`root `[`#`]`emerge --ask app-emulation/qemu`

For graphical sessions to work in your virtual machine, i.e. logging to a desktop, either [[[app-emulation/virt-viewer]](https://packages.gentoo.org/packages/app-emulation/virt-viewer)[]] or [[[net-misc/spice-gtk]](https://packages.gentoo.org/packages/net-misc/spice-gtk)[]] needs to be installed.

`root `[`#`]`emerge --ask app-emulation/virt-viewer`

The following kernel options are needed: `CONFIG_MACVTAP`, `CONFIG_VHOST_VSOCK`, `CONFIG_KVM` and either `CONFIG_KVM_AMD` or `CONFIG_KVM_INTEL` depending on your CPU. Please see [QEMU#Kernel](https://wiki.gentoo.org/wiki/QEMU#Kernel "QEMU") for more accurate config options. You\'ll also need to enable virtualization in your BIOS, otherwise you\'ll get an error message of \"KVM: disabled by BIOS\". Basically, make sure [/dev/kvm] exists before trying to launch a virtual machine. And setup QEMU properly so it works.

Get a virtual machine image, and launch it:

`user `[`$`]`lxc launch images:opensuse/15.3/desktop-kde opensuse-kde --vm`

** Note**\
The [\--vm] flag is mandatory.

** Note**\
Currently Gentoo doesn\'t ship required files for secureboot, and **some** distros require them by default. You can override this with [-c security.secureboot=false], in other words, [lxc launch images:opensuse/15.3/desktop-kde opensuse-kde \--vm -c security.secureboot=false]

Alternatively do it manually: [lxc config edit opensuse-kde] and add `security.secureboot: "false"` under `config:` section.

Monitor the status in [[[bug #830006]](https://bugs.gentoo.org/show_bug.cgi?id=830006)[]]

Access the shell of your virtual machine:

`user `[`$`]`lxc exec opensuse-kde -- su --login`

Access the desktop/GUI of your virtual machine:

`user `[`$`]`lxc console opensuse-kde --type=vga`

\

### [Allocating resources in a virtual machine]

By default the virtual machine images are very starved. You may need to use [lxc] or external tools to give them more resources. You can configure many resources similarly to containers, and there are tons of these configuration options. Please refer to upstream documentation about adjusting resources for lxd containers.

#### [CPU]

Give the VM 8 cores:

`user `[`$`]`lxc config set my-vm limits.cpu 8`

Or to allow it to use 50 % of CPU capability:

`user `[`$`]`lxc config set my-vm limits.cpu.allowance 50% `

Give it the lowest CPU priority:

`user `[`$`]`lxc config set my-vm limits.cpu.priority 0`

#### [Disk size]

Simply the following should work when the VM is **off**:

`user `[`$`]`lxc config device set my-vm root size=20GB`

These **profile** settings can be used to create VMs with bigger disk sizes. Make sure the profile is inherited by the VM in question.

`user `[`$`]`lxc profile show bigger-vm-disk`

    config:
    description: VM Profile for a bigger root disk
    devices:
      root:
        path: /
        pool: default
        size: 50GB
        type: disk

`user `[`$`]`lxc config show my-vm`

    ...
    profiles:
    - default
    - bigger-vm-disk
    ...

If it does not, the manual method below is a more sureway to get it done:

On the **host** resize image with [qemu-img].

`user `[`$`]`cd ~/lxd/virtual-machines/gentoo-openrc-vm/ `

`user `[`$`]`qemu-img resize root.img 20G`

** Note**\
Depending on image, [qemu-img resize -f raw root.img 20G] might be required instead.

Now move on to the virtual machine.

`user `[`$`]`lxc start gentoo-vm `

`user `[`$`]`lxc exec gentoo-vm bash`

`gentoo-openrc-vm #``emerge -av sys-fs/growpart `

`gentoo-openrc-vm #``df -h `

`gentoo-openrc-vm #``growpart /dev/sda 2 `

`gentoo-openrc-vm #``resize2fs /dev/sda2 `

`gentoo-openrc-vm #``df -h`

#### [Memory]

Give your VM 8 GB of memory:

`user `[`$`]`lxc config set my-container limits.memory 8GB`

Also accepts `MB`.

#### [Network]

** Note**\
systemd generally \"just works\".

Whether you want to receive an IP address via dhcp or statically, the Handbook has written steps that work in a virtual machine. Get your interface:

`root `[`#`]`ip addr `

    1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN mode DEFAULT group default qlen 1000
        link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    2: enp5s0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast state UP mode DEFAULT group default qlen 1000
        link/ether 74:56:3c:64:cf:26 brd ff:ff:ff:ff:ff:ff

`gentoo-openrc-vm #``cd /etc/init.d `

`gentoo-openrc-vm #``rm net.eth0 `

`gentoo-openrc-vm #``ln -s net.lo net.enp5s0 `

`gentoo-openrc-vm #``/etc/init.d/net.enp5s0 start `

`gentoo-openrc-vm #``rc-update add enp5s0 default`

## [Advanced features]

### [Live migration]

TODO

### [Automatic BTRFS integration]

When LXD detects that [/var/lib/lxd] is on a [Btrfs](https://wiki.gentoo.org/wiki/Btrfs "Btrfs") filesystem, it uses Btrfs\' snapshot capabilities to ensure that images, containers and snapshots share blocks as much as possible. No user action is required to enable this behavior.

When the container was launched in the Quick Start section above LXD created subvolumes for the image and container. The container filesystem is a copy-on-write snapshot of the image.

`root `[`#`]`btrfs subvolume list /`

    ID 330 gen 4518 top level 5 path var/lib/lxd/images/8e54c679f1c293f909c66097d97de23c66a399d2dc396ade92b3b6aae1c7
    ID 331 gen 4595 top level 5 path var/lib/lxd/containers/mycentos6

`root `[`#`]`btrfs subvolume show /var/lib/lxd/images`

    /8e54c679f1c293f909c66097d97de23c66a399d2dc396ade92b3b6a
    /var/lib/lxd/images/8e54c679f1c293f909c66097d97de23c66a399d2dc396ade92b3b6aae1c732fe.btrfs
            Name:                   8e54c679f1c293f909c66097d97de23c66a399d2dc396ade92b3b6aae1c732fe.btrfs
            UUID:                   5530510e-2007-f146-9e0b-8c05480d63de
            Parent UUID:            -
            Received UUID:          -
            Creation time:          2015-09-04 15:03:32 -0500
            Subvolume ID:           330
            Generation:             4518
            Gen at creation:        4517
            Parent ID:              5
            Top level ID:           5
            Flags:                  -
            Snapshot(s):
                                    var/lib/lxd/containers/mycentos6

Making a snapshot of the running container filesystem creates another copy-on-write snapshot.

`user `[`$`]`lxc snapshot mycentos6 firstsnap`

`root `[`#`]`btrfs subvolume list /`

    ID 330 gen 4518 top level 5 path var/lib/lxd/images/8e54c679f1c293f909c66097d97de23c66a399d2dc396ade92b3b6aae1c7
    ID 331 gen 4595 top level 5 path var/lib/lxd/containers/mycentos6
    ID 332 gen 4584 top level 5 path var/lib/lxd/snapshots/mycentos6/firstsnap

`root `[`#`]`btrfs subvolume show /var/lib/lxd/containers/mycentos6`

    /var/lib/lxd/containers/mycentos6
            Name:                   mycentos6
            UUID:                   fe6bfd65-d911-e449-a1df-be42d2997f4a
            Parent UUID:            5530510e-2007-f146-9e0b-8c05480d63de
            Received UUID:          -
            Creation time:          2015-09-04 15:03:39 -0500
            Subvolume ID:           331
            Generation:             4595
            Gen at creation:        4518
            Parent ID:              5
            Top level ID:           5
            Flags:                  -
            Snapshot(s):
                                    var/lib/lxd/snapshots/mycentos6/firstsnap

### [][/dev/lxd/sock]

A socket is bind-mounted into the container at [/dev/lxd/sock]. It serves no critical purpose, but is available to users as a means to query configuration information about the container.

### [][Graphical (X) applications in a container]

It is possible to run GUI applications in a container. Edit container\'s config,

`user `[`$`]`lxc config edit your-container-name`

Add the following:

    config:
      environment.DISPLAY: :0.0
    ...
    ...
    devices:
      X0:
        path: /tmp/.X11-unix
        source: /tmp/.X11-unix
        type: disk
      mygpu:
        type: gpu
    ...
    ...

DISPLAY environment variable can be seen from a host, with **echo \$DISPLAY**. It is also better to share the directory [/tmp/.X11-unix] instead of individual files under [/tmp/.X11-unix/\*].

For container to be allowed to attach into host\'s Xsession, issue **xhost +local:** command in the host.

**Important:** systemd containers will automount [/tmp] as tmpfs in the container, overwriting your setting here! Either manually unmount [/tmp] to find your socket, or do the following: **Inside the container**:

`user `[`$`]`cp /usr/lib/tmpfiles.d/x11.conf /etc/tmpfiles.d/`

`user `[`$`]`$EDITOR /etc/tmpfiles.d/x11.conf`

Modified version:

[FILE] **`/etc/tmpfiles.d/x11.conf`**

    # D! /tmp/.X11-unix 1777 root root 10d
    D! /tmp/.ICE-unix 1777 root root 10d
    D! /tmp/.XIM-unix 1777 root root 10d
    D! /tmp/.font-unix 1777 root root 10d

    # Unlink the X11 lock files
    # r! /tmp/.X[0-9]*-lock

So **comment** the following lines:

    D! /tmp/.X11-unix 1777 root root 10d
    ...
    r! /tmp/.X[0-9]*-lock

Stop and start your container, relogin into it. You can of course edit [/usr/lib/tmpfiles.d/x11.conf] but it\'s going to be overwritten whenever systemd updates inside the container. See the [bug report](https://github.com/lxc/lxd/issues/4540) about this issue.

## [Troubleshooting]

First things to do when facing problems is to check the containers log, lxd\'s log and system log.

`user `[`$`]`lxc start <instance_name> --debug`

`user `[`$`]`lxc info <instance_name> --show-log`

Attach immediately to systart:

`user `[`$`]`lxc start <instance_name> ; lxc console <instance_name>`

By default lxd\'s logs can be found from [/var/log/lxd/] - this can also be modified from [conf.d] and service files.

### [][Containers freeze on \'lxc stop\' with OpenRC (+ SysVinit)]

If the container freezes during the stop command with

`user `[`$`]`lxc stop mycontainer`

while using OpenRC, try to turn it off directly with [poweroff]:

`user `[`$`]`lxc exec mycontainer -- poweroff`

If that works, edit the [/etc/inittab] file **in the container** adding following part:

[FILE] **`/etc/inittab`**

    pf:12345:powerwait:/sbin/halt

Shutdown the container with [poweroff], and next time it is booted, the container should work like normal and [lxc stop] should work as expected. Be careful when doing world updates to not blindly merge changes to [/etc/inittab].

### [Running systemd based containers on OpenRC hosts]

To support systemd guests, e.g. ubuntu/debian/arch linux containers, on an OpenRC system, the host must be modified to support the systemd [cgroup](https://wiki.gentoo.org/wiki/Cgroups "Cgroups"). It is recommended to use cgroupsv2 as most containers support it and OCI runtimes [crun] and [runc] also expect cgroupsv2 to be present.

To enable the cgroupsv2 modify [/etc/rc.conf] to set `rc_cgroup_mode="unified"` and uncomment and add `rc_cgroup_controllers="systemd"`:

[FILE] **`/etc/rc.conf`**

    ...
    ...
    ...
    ##############################################################################
    # LINUX CGROUPS RESOURCE MANAGEMENT

    # This sets the mode used to mount cgroups.
    # "hybrid" mounts cgroups version 2 on /sys/fs/cgroup/unified and
    # cgroups version 1 on /sys/fs/cgroup.
    # "legacy" mounts cgroups version 1 on /sys/fs/cgroup
    # "unified" mounts cgroups version 2 on /sys/fs/cgroup
    rc_cgroup_mode="unified"

    # This is a list of controllers which should be enabled for cgroups version 2.
    # If hybrid mode is being used, controllers listed here will not be
    # available for cgroups version 1.
    # This is a global setting.
    rc_cgroup_controllers="systemd"
    ...
    ...
    ...

Older versions up to lxd-3.9 might need a raw.lxc config entry in addition to mount the host\'s cgroups automagically into the container:

`user `[`$`]`lxc config set <container> raw.lxc 'lxc.mount.auto = cgroup'`

For more details take a look a the upstream issue on [github.com](https://github.com/lxc/lxd/issues/4052)

#### [][Alternative way (lxd-4.0.9)]

Modify these parts, as instructed above:

[FILE] **`/etc/rc.conf`**

    rc_cgroup_mode="hybrid"

    rc_cgroup_controllers="yes"
    rc_controller_cgroups="yes"

After that create [/etc/init.d/cgroups-systemd] [init-file](https://wiki.gentoo.org/wiki/Handbook:AMD64/Working/Initscripts#Writing_initscripts "Handbook:AMD64/Working/Initscripts") with following content:

[FILE] **`/etc/init.d/cgroups-systemd`**

    #!/sbin/openrc-run
    # Copyright 2022 Gentoo Authors
    # Distributed under the terms of the GNU General Public License v2

    description="Mount the control groups (systemd)."

    cgroup_opts=nodev,noexec,nosuid

    depend()

    start() ,name=systemd systemd /sys/fs/cgroup/systemd
    }

Add created init-file into [sysvinit] runlevel:

`root `[`#`]`rc-update add cgroups-systemd sysvinit `

`root `[`#`]`rc-service start cgroups-systemd `

`user `[`$`]`lxc launch images:fedora/36 fedora-systemd-img `

`user `[`$`]`lxc stop fedora-systemd-img `

`user `[`$`]`lxc config set fedora-systemd-img limits.cpu 6 `

`user `[`$`]`lxc config set fedora-systemd-img limits.memory 8GB `

`user `[`$`]`lxc start fedora-systemd-img `

`user `[`$`]`lxc exec fedora-systemd-img bash`

### [Using LXD with self-spun ZFS pools]

If you use ZFS with LXD and provide it the full pool path, then LXD will export the pool on shutdown for safety.

On startup, LXD will look for pools in a standard path, [/var/lib/lxd/disks/] and in the block devices (which can be displayed using [/bin/lsblk].

If you create your own pools outside of LXD and those are not in the standard path or in block devices, you must import them explicitly *before* starting LXD if you want LXD to find them. If you do not, LXD will fail to start.

(See [https://discuss.linuxcontainers.org/t/lxd-exports-zfs-pools-at-shutdown-but-does-not-import-them-properly-at-startup/13031/2](https://discuss.linuxcontainers.org/t/lxd-exports-zfs-pools-at-shutdown-but-does-not-import-them-properly-at-startup/13031/2) for more information.)

### [Too many open files on OpenRC hosts]

If an error due to `Too many open files` is encountered when the daemon is started via OpenRC, increase the limit by setting the `rc_ulimit` variable in [/etc/conf.d/lxd]:

[FILE] **`/etc/conf.d/lxd`Recommended production values**

    ...
    rc_ulimit="-n 1048576 -l unlimited"
    ...

** Note**\
Since OpenRC doesn\'t use PAM, [/etc/etc/security/limits.conf] will be ignored.

## [See also]

-   [Docker](https://wiki.gentoo.org/wiki/Docker "Docker") --- a [container](https://en.wikipedia.org/wiki/Container_(virtualization) "wikipedia:Container (virtualization)")-based [virtualization](https://wiki.gentoo.org/wiki/Virtualization "Virtualization") system
-   [Incus/Gentoo_Github_pullrequest_testing](https://wiki.gentoo.org/wiki/Incus/Gentoo_Github_pullrequest_testing "Incus/Gentoo Github pullrequest testing") --- easy and automated way for testing ebuild contributions via [Gentoo\'s Github mirror](https://github.com/gentoo/gentoo) that\'s based on [Incus](https://wiki.gentoo.org/wiki/Incus "Incus")
-   [LXC](https://wiki.gentoo.org/wiki/LXC "LXC") --- a [virtualization](https://wiki.gentoo.org/wiki/Virtualization "Virtualization") system that leverages Linux\'s [namespaces](https://wiki.gentoo.org/wiki/Namespaces "Namespaces") and [cgroups](https://wiki.gentoo.org/wiki/Cgroups "Cgroups") to create containers isolated from the host system
-   [Podman](https://wiki.gentoo.org/wiki/Podman "Podman") --- a daemonless container engine for developing, managing, and running [OCI Containers](https://opencontainers.org/), aiming to be a drop-in replacement for much of [Docker](https://wiki.gentoo.org/wiki/Docker "Docker")

## [External Resources]

-   [LXC and LXD: a different container story](https://lwn.net/Articles/907613/)
-   [LXD upstream\'s discussion site, support forums etc.](https://discuss.linuxcontainers.org/)
-   [LXD upstream\'s official Youtube channel.](https://www.youtube.com/c/LXDvideos)
-   [Just me and Opensource Youtube channel](https://www.youtube.com/c/wenkatn-justmeandopensource/videos), multiple LXD related guide videos. [Better filtering.](https://www.youtube.com/results?search_query=%23justmelxd)

1.  [[[↑](#cite_ref-1)] [[LXD Introduction](https://linuxcontainers.org/lxd/introduction/), [Linux Containers](https://linuxcontainers.org/). Retreived on March 12th, 2021.]]