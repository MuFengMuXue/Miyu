This page contains [[changes](https://wiki.gentoo.org/index.php?title=Libvirt&diff=1436300)] which are not marked for translation.

**Resources**

[[]][Home](https://www.libvirt.org/)

[[]][Package information](https://packages.gentoo.org/packages/app-emulation/libvirt)

[[]][GitLab](https://gitlab.com/libvirt/libvirt)

[[]][Wikipedia](https://en.wikipedia.org/wiki/Libvirt "wikipedia:Libvirt")

[[]][Official documentation](https://www.libvirt.org/docs.html)

[[]][Bugs (upstream)](https://libvirt.org/bugs.html)

[![Ohloh Logo](/images/thumb/c/c1/Ohloh-logo.png/30px-Ohloh-logo.png)][Open Hub](https://www.openhub.net/p/libvirt)

[libvirt] is a virtualization management toolkit.

The [libvirt] package is comprised of two components: a toolkit, and a static object library. It primarily provides virtualization support for UNIX.

## Contents

-   [[1] [Overview]](#Overview)
    -   [[1.1] [Features]](#Features)
        -   [[1.1.1] [Supported guest types]](#Supported_guest_types)
-   [[2] [Installation]](#Installation)
    -   [[2.1] [Kernel]](#Kernel)
    -   [[2.2] [USE flags]](#USE_flags)
        -   [[2.2.1] [USE_EXPAND]](#USE_EXPAND)
    -   [[2.3] [Emerge]](#Emerge)
    -   [[2.4] [Additional software]](#Additional_software)
        -   [[2.4.1] [Custom UEFI]](#Custom_UEFI)
-   [[3] [Configuration]](#Configuration)
    -   [[3.1] [Environment variables]](#Environment_variables)
    -   [[3.2] [Files]](#Files)
    -   [[3.3] [User permissions]](#User_permissions)
    -   [[3.4] [Service]](#Service)
        -   [[3.4.1] [OpenRC]](#OpenRC)
        -   [[3.4.2] [systemd]](#systemd)
    -   [[3.5] [Firewall]](#Firewall)
    -   [[3.6] [Networking]](#Networking)
    -   [[3.7] [Autostart]](#Autostart)
        -   [[3.7.1] [System autostart]](#System_autostart)
        -   [[3.7.2] [Session autostart]](#Session_autostart)
-   [[4] [Usage]](#Usage)
    -   [[4.1] [Managing domains]](#Managing_domains)
    -   [[4.2] [Host information]](#Host_information)
    -   [[4.3] [Host verification]](#Host_verification)
    -   [[4.4] [Connect types - Default]](#Connect_types_-_Default)
    -   [[4.5] [Connect types - Required]](#Connect_types_-_Required)
        -   [[4.5.1] [Transport]](#Transport)
        -   [[4.5.2] [**target-or-path**]](#target-or-path)
            -   [[4.5.2.1] [Predefined target name]](#Predefined_target_name)
            -   [[4.5.2.2] [Path]](#Path)
    -   [[4.6] [Connect types - Optional]](#Connect_types_-_Optional)
        -   [[4.6.1] [Hostname]](#Hostname)
            -   [[4.6.1.1] [No Hostname]](#No_Hostname)
            -   [[4.6.1.2] [Hostname given]](#Hostname_given)
        -   [[4.6.2] [Protocol]](#Protocol)
        -   [[4.6.3] [Connect types syntax]](#Connect_types_syntax)
            -   [[4.6.3.1] [Connect Type URI Usage]](#Connect_Type_URI_Usage)
    -   [[4.7] [Invocation]](#Invocation)
-   [[5] [Removal]](#Removal)
-   [[6] [Troubleshooting]](#Troubleshooting)
    -   [[6.1] [Messages mentioning \...or mount/enable cgroup controller in your system]](#Messages_mentioning_...or_mount.2Fenable_cgroup_controller_in_your_system)
    -   [[6.2] [WARN (Unknown if this platform has Secure Guest support)]](#WARN_.28Unknown_if_this_platform_has_Secure_Guest_support.29)
    -   [[6.3] [Docker doesn\'t work]](#Docker_doesn.27t_work)
    -   [[6.4] [Using Libvirt with Android]](#Using_Libvirt_with_Android)
-   [[7] [See also]](#See_also)
-   [[8] [External resources]](#External_resources)
-   [[9] [References]](#References)

## [Overview]

[[[app-emulation/libvirt]](https://packages.gentoo.org/packages/app-emulation/libvirt)[]] package provides a CLI toolkit that can be used to assist in the creation and configuration of new domains. It is also used to adjust a domain's resource allocation/virtual hardware.

\

### [Features]

The overview of Libvirt features are:

-   Guest configuration is stored in the XML format at [/etc/libvirt]. For example, QEMU config goes under [/etc/libvirt/qemu]
-   Snapshots for virtual machines can be crated and rolled back.
-   Network interface creation and management, including bridge and MACVLAN creation.
-   Network configuration automation and management for NAT and DHCP.
-   Storage pool management for easier mounting on guests, filesystems including:
    -   Virtio directory sharing
    -   Direct block device access
    -   gluster
    -   [iSCSI](https://wiki.gentoo.org/wiki/ISCSI "ISCSI")/SCSI
    -   [LVM](https://wiki.gentoo.org/wiki/LVM "LVM")
    -   multi-path devices
    -   netfs
    -   RADOS/[Ceph](https://wiki.gentoo.org/wiki/Ceph "Ceph")
    -   Sheepdog

#### [Supported guest types]

[libvirt] can manage the following types of virtual machines and containers, [among others](https://www.libvirt.org/drivers.html#hypervisor-drivers):

-   BHyve (FreeBSD, NetBSD, OpenBSD)
-   [LXC](https://wiki.gentoo.org/wiki/LXC "LXC")
-   [QEMU](https://wiki.gentoo.org/wiki/QEMU "QEMU") and QEMU/[KVM](https://wiki.gentoo.org/wiki/KVM "KVM")
-   [VirtualBox](https://wiki.gentoo.org/wiki/VirtualBox "VirtualBox")
-   [OpenVZ](https://wiki.gentoo.org/wiki/OpenVZ "OpenVZ") (Virtuozzo)
-   [VMware](https://wiki.gentoo.org/wiki/VMware "VMware") ESX
-   [Xen](https://wiki.gentoo.org/wiki/Xen "Xen")

## [Installation]

Verify host as QEMU-capable:

To verify that the host hardware has the needed virtualization support, issue the following command:

`host$``grep --color -E "vmx|svm" /proc/cpuinfo`

The [vmx] or [svm] CPU flag should be red highlighted and available.

File [/dev/kvm] must exist.

\

### [Kernel]

The following kernel config is recommended by the [libvirtd] daemon.

** Note**\
Check the logs to see if any additional kernel configs are requested by the build.

[KERNEL] **libvirt (`CONFIG_BRIDGE_EBT_MARK`, `CONFIG_NETFILTER_ADVANCED`, `CONFIG_NETFILTER_XT_CONNMARK`, `CONFIG_NETFILTER_XT_TARGET_CHECKSUM`, `CONFIG_IP6_NF_NAT`)**

    [*] Networking support
        Networking Options  --->
            [*] Network packet filtering framework (Netfilter)  --->
                [*] Advanced netfilter configuration
                Core Netfilter Configuration  --->
                    <*> "conntrack" connection tracking match support
                    <*> CHECKSUM target support
                IPv6: Netfilter Configuration  --->
                    <*> IP6 tables support (required for filtering)
                      <*> ip6tables NAT support

                <*> Ethernet Bridge tables (ebtables) support  --->
                    <*> ebt: nat table support
                    <*> ebt: mark filter support
            [*] QoS and/or fair queueing  --->
                <*> Hierarchical Token Bucket (HTB)
                <*> Stochastic Fairness Queueing (SFQ)
                <*> Ingress/classifier-action Qdisc
                <*> Netfilter mark (FW)
                <*> Universal 32bit comparisons w/ hashing (U32)
                [*] Actions
                <*>    Traffic Policing
                <*>    Checksum Updating

The following kernel options are required to pass some checks by the [virt-host-validate] tool. That also means that are requirements for some functionality.

[KERNEL] **Enabling `blkio` (`CONFIG_BLK_CGROUP`)**

    General setup --->
    [*] Control Group support --->
        --- Control Group support
            [*] IO controller

[KERNEL] **Enabling `memory` (`CONFIG_MEMORY`)**

    Device Drivers --->
        [*] Memory Controller drivers ---
            --- Memory Controller drivers

[KERNEL] **Enabling `tun` (`CONFIG_TUN`) (used in the default libvirt/virt-manager networking setup)**

    Device Drivers --->
        [*] Network device support  --->
            [*] Network core driver support
                <*> Universal TUN/TAP device driver support

### [USE flags]

Some packages are aware of the [`libvirt`](https://packages.gentoo.org/useflags/libvirt) USE flag.

Review the possible USE flags for [libvirt]:

### [USE flags for] [app-emulation/libvirt](https://packages.gentoo.org/packages/app-emulation/libvirt) [[]] [C toolkit to manipulate virtual machines]

  ------------------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [`+caps`](https://packages.gentoo.org/useflags/+caps)                           Use Linux capabilities library to control privilege
  [`+libvirtd`](https://packages.gentoo.org/useflags/+libvirtd)                   Builds the libvirtd daemon as well as the client utilities instead of just the client utilities
  [`+qemu`](https://packages.gentoo.org/useflags/+qemu)                           Support management of QEMU virtualisation (app-emulation/qemu)
  [`+udev`](https://packages.gentoo.org/useflags/+udev)                           Enable virtual/udev integration (device discovery, power and storage device support, etc)
  [`+virt-network`](https://packages.gentoo.org/useflags/+virt-network)           Enable virtual networking (NAT) support for guests. Includes all the dependencies for NATed network mode. Effectively any network setup that relies on libvirt to setup and configure network interfaces on your host. This can include bridged and routed networks ONLY if you are allowing libvirt to create and manage the underlying devices for you. In some cases this requires enabling the \'netcf\' USE flag (currently unavailable).
  [`apparmor`](https://packages.gentoo.org/useflags/apparmor)                     Enable support for the AppArmor application security system
  [`audit`](https://packages.gentoo.org/useflags/audit)                           Enable support for Linux audit subsystem using sys-process/audit
  [`bash-completion`](https://packages.gentoo.org/useflags/bash-completion)       Enable bash-completion support
  [`dtrace`](https://packages.gentoo.org/useflags/dtrace)                         Enable dtrace support via dev-debug/systemtap
  [`firewalld`](https://packages.gentoo.org/useflags/firewalld)                   DBus interface to iptables/ebtables allowing for better runtime management of your firewall.
  [`fuse`](https://packages.gentoo.org/useflags/fuse)                             Allow LXC to use sys-fs/fuse for mountpoints
  [`glusterfs`](https://packages.gentoo.org/useflags/glusterfs)                   Enable GlusterFS support via sys-cluster/glusterfs
  [`iscsi`](https://packages.gentoo.org/useflags/iscsi)                           Allow using an iSCSI remote storage server as pool for disk image storage
  [`iscsi-direct`](https://packages.gentoo.org/useflags/iscsi-direct)             Allow using libiscsi for iSCSI storage pool backend
  [`libssh`](https://packages.gentoo.org/useflags/libssh)                         Use net-libs/libssh to communicate with remote libvirtd hosts, for example: qemu+libssh://server/system
  [`libssh2`](https://packages.gentoo.org/useflags/libssh2)                       Use net-libs/libssh2 to communicate with remote libvirtd hosts, for example: qemu+libssh2://server/system
  [`lvm`](https://packages.gentoo.org/useflags/lvm)                               Allow using the Logical Volume Manager (sys-fs/lvm2) as pool for disk image storage
  [`lxc`](https://packages.gentoo.org/useflags/lxc)                               Support management of Linux Containers virtualisation (app-containers/lxc)
  [`nbd`](https://packages.gentoo.org/useflags/nbd)                               Allow using sys-block/nbdkit to access network disks
  [`nfs`](https://packages.gentoo.org/useflags/nfs)                               Allow using Network File System mounts as pool for disk image storage
  [`nls`](https://packages.gentoo.org/useflags/nls)                               Add Native Language Support (using gettext - GNU locale utilities)
  [`numa`](https://packages.gentoo.org/useflags/numa)                             Use NUMA for memory segmenting via sys-process/numactl and sys-process/numad
  [`parted`](https://packages.gentoo.org/useflags/parted)                         Allow using real disk partitions as pool for disk image storage, using sys-block/parted to create, resize and delete them.
  [`pcap`](https://packages.gentoo.org/useflags/pcap)                             Support auto learning IP addreses for routing
  [`policykit`](https://packages.gentoo.org/useflags/policykit)                   Enable PolicyKit (polkit) authentication support
  [`rbd`](https://packages.gentoo.org/useflags/rbd)                               Enable rados block device support via sys-cluster/ceph
  [`sasl`](https://packages.gentoo.org/useflags/sasl)                             Add support for the Simple Authentication and Security Layer
  [`selinux`](https://packages.gentoo.org/useflags/selinux)                       !!internal use only!! Security Enhanced Linux support, this must be set by the selinux profile or breakage will occur
  [`test`](https://packages.gentoo.org/useflags/test)                             Enable dependencies and/or preparations necessary to run tests (usually controlled by FEATURES=test but can be toggled independently)
  [`verify-sig`](https://packages.gentoo.org/useflags/verify-sig)                 Verify upstream signatures on distfiles
  [`virtiofsd`](https://packages.gentoo.org/useflags/virtiofsd)                   Drag in virtiofsd dependency app-emulation/virtiofsd
  [`virtualbox`](https://packages.gentoo.org/useflags/virtualbox)                 Support management of VirtualBox virtualisation (app-emulation/virtualbox)
  [`wireshark-plugins`](https://packages.gentoo.org/useflags/wireshark-plugins)   Build the net-analyzer/wireshark plugin for the Libvirt RPC protocol
  [`xen`](https://packages.gentoo.org/useflags/xen)                               Support management of Xen virtualisation (app-emulation/xen)
  [`zfs`](https://packages.gentoo.org/useflags/zfs)                               Enable ZFS backend storage sys-fs/zfs
  ------------------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-04-10 18:50] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

** Note**\
If [libvirt] is going to be used, you may need the `usbredir` USE flags to redirect USB devices to another machine over TCP.

libvirt comes with a number of USE flags. Please check those flags and set them according to your setup. These are recommended USE flags for libvirt:

[FILE] **`/etc/portage/package.use/libvirt`**

    app-emulation/libvirt pcap virt-network numa fuse macvtap vepa qemu

##### [USE_EXPAND]

See [/etc/portage/make.conf#USE_EXPAND](https://wiki.gentoo.org/wiki//etc/portage/make.conf#USE_EXPAND "/etc/portage/make.conf") for more detail on `USE_EXPAND`.

### [Emerge]

After reviewing and adding any desired USE flags, emerge [[[app-emulation/libvirt]](https://packages.gentoo.org/packages/app-emulation/libvirt)[]] and [[[app-emulation/qemu]](https://packages.gentoo.org/packages/app-emulation/qemu)[]] :

`root `[`#`]`emerge --ask app-emulation/libvirt app-emulation/qemu`

### [Additional software]

#### [Custom UEFI]

Custom UEFI are provided by [[[app-emulation/virt-firmware]](https://packages.gentoo.org/packages/app-emulation/virt-firmware)[]] package.

## [Configuration]

### [Environment variables]

See specific CLI commands related to Libvirt for its available environment variable settings: [virsh](https://wiki.gentoo.org/wiki/Virsh#Environment_variables "Virsh"), [libvirtd](https://wiki.gentoo.org/wiki/Libvirt/libvirtd#Environment_variables "Libvirt/libvirtd"), [virt-manager](https://wiki.gentoo.org/wiki/Virt-manager#Environment_variables "Virt-manager").

### [Files]

When a domain starts, client using [Libvirt] API library (ie., [virt-manager](https://wiki.gentoo.org/wiki/Virt-manager "Virt-manager"), [virsh](https://wiki.gentoo.org/wiki/Virsh "Virsh")) checks for that [domain](https://wiki.gentoo.org/wiki/Libvirt/domain "Libvirt/domain") XML file in the following paths:

-   System : [/etc/libvirt/qemu/] via [qemu:///system].
-   User session: [\$HOME/.config/libvirt/qemu/] via [qemu:///session].

\
Other directory paths used by [Libvirt] library are:

-   [/etc/libvirt/hooks/]
-   [/etc/libvirt/nwfilter/]
-   [/etc/libvirt/secrets/]
-   [/etc/libvirt/storage/]
-   [/proc/]
-   [/proc/sys/ipv4/]
-   [/proc/sys/ipv6/conf/all/]
-   [/proc/sys/ipv6/conf/%s/%s]
-   [/sys/class/fc_host/]
-   [/sys/devices/system/%s/cpu/]
-   [/sys/devices/system/node/node0/]
-   [/sys/fs/resctrl/info/%s/]
-   [/sys/kernel/mm/transparent_hugepage/]
-   [/sys/fs/resctrl/info/%s/]
-   [/sys/fs/resctrl/info/MB/]
-   [/var/lib/libvirt/]

\
For specific file accesses, see Libvirt-related CLI commands [virsh](https://wiki.gentoo.org/wiki/Virsh#Files "Virsh"), [libvirtd](https://wiki.gentoo.org/wiki/Libvirt/libvirtd#Files "Libvirt/libvirtd"), [virt-manager](https://wiki.gentoo.org/wiki/Virt-manager#Files "Virt-manager")..

### [User permissions []]

To have a user join the UNIX **[libvirt]** group, check that the group name is already defined:

`host$``getent group libvirt`

    libvirt:x:1001:

If the output line exist above stating that the **[libvirt]** group exists, then add the user to that group:

`host$``sudo usermod -aG libvirt username`

\
If **[libvirt]** group is missing, then `policykit` may have not been installed.

** Important**\
If `policykit` *USE* flag is not enabled for libvirt package, the [libvirt] group will not be created when [[[app-emulation/libvirt]](https://packages.gentoo.org/packages/app-emulation/libvirt)[]] is emerged. If this is the case, another group, such as **wheel** must be used for *unix_sock_group*.

If not using `policykit` and still wanting to use libvirt session (per-user/user-mode), then add manually the **[wheel]** group, replace **[username]** with its actual username, run:

`host$``sudo usermod -aG wheel username`

** Warning**\
It is difficult to use **[libvirt]** group name without the `policykit`. Use this **[wheel]** group instead.

------------------------------------------------------------------------

Uncomment the following lines from the libvirtd configuration file:

[FILE] **`/etc/libvirt/libvirtd.conf`**

    auth_unix_ro = "none"
    auth_unix_rw = "none"
    unix_sock_group = "libvirt"
    unix_sock_ro_perms = "0777"
    unix_sock_rw_perms = "0770"

** Tip**\
Replace **[libvirt]** in [unix_sock_group] with **[wheel]** if no `policykit` installed.

Be sure to have the user log out then log in again for the new group settings to be applied.

[virt-admin] should then be launchable as a regular user, after the services have been started.

** Note**\
If permission denied issues are experienced when loading ISO images user directories (somewhere beneath [/home/]) then the [/var/lib/libvirt/images/] directory can be used to store the images.

### [Service []]

#### [OpenRC]

To start [libvirtd] daemon using OpenRC and add it to default runlevel:

`host-root#``rc-service libvirtd start && rc-update add libvirtd default`

#### [systemd]

Historically, all libvirt functionality was provided by the monolithic libvirtd daemon. [Upstream](https://libvirt.org/daemons.html#modular-driver-daemons) has developed a new modular architecture for libvirt where each driver is run in its own daemon. Therefore, recent versions of libvirt (at least \>=app-emulation/libvirt-9.3.0) need the service units for the hypervisor drivers enabled. For QEMU this is [virtqemud.service], for Xen it is [virtxend.service] and for LXC [virtlxcd.service] and their corresponding sockets.

Enable the service units and their sockets, depending on the functionality (qemu, xen, lxc) you need:

`host-root#``systemctl enable --now virtnetworkd.service`

    Created symlink '/etc/systemd/system/multi-user.target.wants/virtnetworkd.service' → '/usr/lib/systemd/system/virtnetworkd.service'.
    Created symlink '/etc/systemd/system/sockets.target.wants/virtnetworkd.socket' → '/usr/lib/systemd/system/virtnetworkd.socket'.
    Created symlink '/etc/systemd/system/sockets.target.wants/virtnetworkd-ro.socket' → '/usr/lib/systemd/system/virtnetworkd-ro.socket'.
    Created symlink '/etc/systemd/system/sockets.target.wants/virtnetworkd-admin.socket' → '/usr/lib/systemd/system/virtnetworkd-admin.socket'.

`host-root#``systemctl enable --now virtqemud.service`

    Created symlink /etc/systemd/system/multi-user.target.wants/virtqemud.service → /usr/lib/systemd/system/virtqemud.service.
    Created symlink /etc/systemd/system/sockets.target.wants/virtqemud.socket → /usr/lib/systemd/system/virtqemud.socket.
    Created symlink /etc/systemd/system/sockets.target.wants/virtqemud-ro.socket → /usr/lib/systemd/system/virtqemud-ro.socket.
    Created symlink /etc/systemd/system/sockets.target.wants/virtqemud-admin.socket → /usr/lib/systemd/system/virtqemud-admin.socket.
    Created symlink /etc/systemd/system/sockets.target.wants/virtlogd.socket → /usr/lib/systemd/system/virtlogd.socket.
    Created symlink /etc/systemd/system/sockets.target.wants/virtlockd.socket → /usr/lib/systemd/system/virtlockd.socket.
    Created symlink /etc/systemd/system/sockets.target.wants/virtlogd-admin.socket → /usr/lib/systemd/system/virtlogd-admin.socket.
    Created symlink /etc/systemd/system/sockets.target.wants/virtlockd-admin.socket → /usr/lib/systemd/system/virtlockd-admin.socket.

`host-root#``systemctl enable --now virtstoraged.socket`

    Created symlink /etc/systemd/system/sockets.target.wants/virtstoraged.socket → /usr/lib/systemd/system/virtstoraged.socket.
    Created symlink /etc/systemd/system/sockets.target.wants/virtstoraged-ro.socket → /usr/lib/systemd/system/virtstoraged-ro.socket.
    Created symlink /etc/systemd/system/sockets.target.wants/virtstoraged-admin.socket → /usr/lib/systemd/system/virtstoraged-admin.socket.

`host-root#``systemctl enable --now virtlogd.service`

[ ]

Created symlink \'/etc/systemd/system/sockets.target.wants/virtlogd.socket\' → \'/usr/lib/systemd/system/virtlogd.socket\'. Created symlink \'/etc/systemd/system/sockets.target.wants/virtlogd-admin.socket\' → \'/usr/lib/systemd/system/virtlogd-admin.socket\'.

All the service units use a timeout that causes them to shutdown after 2 minutes if no VM is running. They get automatically reactivated when a socket is accessed, e. g. when [virt-manager] is started or a [virsh] command is run.

### [Firewall]

The following firewall chain names have been reserved by the [libvirt] library and [libvirtd] daemon.

Reserved chain name

Description

[nat]

NAT

[LIBVIRT_INP]

Firewall input

[LIBVIRT_FWI]

Firewall input

[LIBVIRT_FWO]

Firewall output

[LIBVIRT_FWX]

Firewall forward

[LIBVIRT_OUT]

Firewall output

[LIBVIRT_PRT]

Firewall postrouting

Reserved Firewall Chain Names by [libvirt] ([viriptable.c] source)

** Warning**\
To firewall administrators: [nat] chain name is often used by [[[net-firewall/shorewall]](https://packages.gentoo.org/packages/net-firewall/shorewall)[]], [[[net-firewall/firewalld]](https://packages.gentoo.org/packages/net-firewall/firewalld)[]], [[[net-firewall/ufw]](https://packages.gentoo.org/packages/net-firewall/ufw)[]], [[[net-firewall/ipfw]](https://packages.gentoo.org/packages/net-firewall/ipfw)[]] and possibly [[[net-firewall/fwbuilder]](https://packages.gentoo.org/packages/net-firewall/fwbuilder)[]]; it is far much easier to rename it at the firewall side than it is to rename [nat] within [libvirt]/[libvirtd].

### [Networking]

For configuration of networking under [libvirt], continue reading at [QEMU networking in Libvirt](https://wiki.gentoo.org/wiki/Libvirt/QEMU_networking "Libvirt/QEMU networking").

### [Autostart]

[] AutoStart feature enables a domain to power up automatically after the host or X session gets ready.

Autostarting a domain can be done in session (X) or in system (host).

\

#### [System autostart]

AutoStart for system-specific domain is natively supported by [libvirtd].

For **[AutoStart]** option of a domain on power-up/reset:

-   run `virsh --connect qemu:///system autostart <vm-name>`; creates a symbolic link to [/etc/libvirt/qemu/autostart/\<vm-name\>.xml].
-   from the [virt-manager] \"`Virtual Machine Manager`\" window, select the domain in the main panel, go to **[Edit-\>Virtual Machine Details]** menu suboptions,
-   or from the [virt-manager] \"`<domain> on QEMU/KVM`\" window, go to **[View-\>Detail]** menu options then select **[Boot Options]** line item in left navigation panel: under **[Autostart]** in main panel

\
Toggle the checkbox for \"Start virtual machine at boot up\".

#### [Session autostart]

The hypervisor controller ([libvirtd]) does not directly support the autostart of session-specific domains ([\--connect=qemu:///session]).

Because session runs under an unprivileged user, its [libvirt] instance becomes available only after that user logs in. As a result, [libvirtd] does not manage session autostart.

To automatically start a session-specific domain, one of the following methods can be used:

-   XDG Autostart mechanism
-   Login script
-   X session script

** Tip**\
In all examples below, replace **[mydomain]** with the actual domain name.

XDG Autostart mechanism

`host$``vi ~/.config/autostart/libvirt-mydomain.desktop`

[FILE] **`$HOME/.config/autostart/libvirt-mydomain.desktop`\"Typical `.desktop` file\"**

    [Desktop Entry]
    Name=My Domain VM
    Type=Application
    Exec=virsh --connect qemu:///session start mydomain
    X-GNOME-Autostart-enabled=true

** Tip**\
On KDE Plasma, any file placed in [\~/.config/autostart/] will be executed automatically, without additional configuration.

For more fine-grained control under KDE Plasma, one of the following lines may be added to the [\~/.config/autostart/libvirt-mydomain.desktop] file:

[FILE] **`$HOME/.config/autostart/libvirt-mydomain.desktop`\"Optional KDE-specific autostart phase\"**

    X-KDE-autostart-phase=0  # Pre-KDE startup
    X-KDE-autostart-phase=1  # After KDE startup
    X-KDE-autostart-phase=2  # After user apps

Login script

[FILE] **`$HOME/.bash_profile`\"Add to `~/.bash_profile`\"**

    # Start a libvirt session domain at login
    virsh --connect=qemu:///session start mydomain >/dev/null 2>&1

Redirecting output ensures that the command does not interfere with the login prompt.

** Note**\
For [zsh], the corresponding file is [\~/.zprofile]. Adjust accordingly.

X session script

[FILE] **`$HOME/.xinitrc`\"Add to `~/.xinitrc`\"**

    # Start a libvirt session domain with X
    virsh --connect=qemu:///session start mydomain &

    # Continue with the usual session startup
    exec startplasma-x11

For display managers (e.g. GDM, SDDM, LightDM), use [\~/.xsession] instead. The trailing [&] runs the domain start command in the background so it does not block the session launch.

** Note**\
Which method to choose?

-   Use the **XDG Autostart mechanism** if you primarily start graphical desktop sessions (GNOME, KDE Plasma, XFCE, etc.).
-   Use a **Login script** if you need the domain started whenever you log in on a TTY or via SSH.
-   Use an **X session script** if you start X manually with [startx] or need per-display-manager customization.

## [Usage]

### [Managing domains]

List all active domains with:

`host$``virsh list`

     Id   Name     State
    ------------------------
     1    gentoo   running
     2    default  running

** Important**\
If no domains are running, [virsh list] will show an empty list. Use [virsh list \--all] to display all detailed domains, including inactive ones.

### [Host information]

Show host CPU and memory details with:

`host$``virsh nodeinfo`

    CPU model:           x86_64
    CPU(s):              4
    CPU frequency:       1600 MHz
    CPU socket(s):       1
    Core(s) per socket:  4
    Thread(s) per core:  1
    NUMA cell(s):        1
    Memory size:         16360964 KiB

Query host DMI/SMBIOS data with:

`host$``virsh sysinfo`

    <sysinfo type='smbios'>
      <bios>
        <entry name='vendor'>Dell Inc.</entry>
        <entry name='version'>A22</entry>
        <entry name='date'>11/29/2018</entry>
        <entry name='release'>4.6</entry>
      </bios>
      <system>
        <entry name='manufacturer'>Dell Inc.</entry>
        <entry name='product'>OptiPlex 3010</entry>
        <entry name='version'>01</entry>
        <entry name='serial'>JRJ0SW1</entry>
        <entry name='uuid'>4c4c4544-0052-4a10-8030-cac04f535731</entry>
        <entry name='sku'>OptiPlex 3010</entry>
        <entry name='family'>Not Specified</entry>
      </system>
      <baseBoard>
        <entry name='manufacturer'>Dell Inc.</entry>
        <entry name='product'>042P49</entry>
        <entry name='version'>A00</entry>
        <entry name='serial'>/JRJ0SW1/CN701632BD05R5/</entry>
        <entry name='asset'>Not Specified</entry>
        <entry name='location'>Not Specified</entry>
      </baseBoard>
      <chassis>
        <entry name='manufacturer'>Dell Inc.</entry>
        <entry name='version'>Not Specified</entry>
        <entry name='serial'>JRJ0SW1</entry>
        <entry name='asset'>Not Specified</entry>
        <entry name='sku'>To be filled by O.E.M.</entry>
      </chassis>

        <entry name='socket_destination'>CPU 1</entry>
        <entry name='type'>Central Processor</entry>
        <entry name='family'>Core i5</entry>
        <entry name='manufacturer'>Intel(R) Corporation</entry>
        <entry name='signature'>Type 0, Family 6, Model 58, Stepping 9</entry>
        <entry name='version'>Intel(R) Core(TM) i5-3470 CPU @ 3.20GHz</entry>
        <entry name='external_clock'>100 MHz</entry>
        <entry name='max_speed'>3200 MHz</entry>
        <entry name='status'>Populated, Enabled</entry>
        <entry name='serial_number'>Not Specified</entry>
        <entry name='part_number'>Fill By OEM</entry>
      </processor>
      <memory_device>
        <entry name='size'>8 GB</entry>
        <entry name='form_factor'>DIMM</entry>
        <entry name='locator'>DIMM1</entry>
        <entry name='bank_locator'>Not Specified</entry>
        <entry name='type'>DDR3</entry>
        <entry name='type_detail'>Synchronous</entry>
        <entry name='speed'>1600 MT/s</entry>
        <entry name='manufacturer'>8C26</entry>
        <entry name='serial_number'>00000000</entry>
        <entry name='part_number'>TIMETEC-UD3-1600</entry>
      </memory_device>
      <memory_device>
        <entry name='size'>8 GB</entry>
        <entry name='form_factor'>DIMM</entry>
        <entry name='locator'>DIMM2</entry>
        <entry name='bank_locator'>Not Specified</entry>
        <entry name='type'>DDR3</entry>
        <entry name='type_detail'>Synchronous</entry>
        <entry name='speed'>1600 MT/s</entry>
        <entry name='manufacturer'>8C26</entry>
        <entry name='serial_number'>00000000</entry>
        <entry name='part_number'>TIMETEC-UD3-1600</entry>
      </memory_device>
      <oemStrings>
        <entry>Dell System</entry>
        <entry>1[0585]</entry>
        <entry>3[1.0]
    </entry>
        <entry>12[www.dell.com]
    </entry>
        <entry>14[1]</entry>
        <entry>15[11]</entry>
      </oemStrings>
    </sysinfo>

** Note**\
virsh sysinfo is also a good simple test to see if [libvirtd] daemon is up and running.

### [Host verification]

Verify the full host setup of [libvirtd] with:

`host-root#``virt-host-validate`

      QEMU: Checking for hardware virtualization                                 : PASS
      QEMU: Checking if device /dev/kvm exists                                   : PASS
      QEMU: Checking if device /dev/kvm is accessible                            : PASS
      QEMU: Checking if device /dev/vhost-net exists                             : PASS
      QEMU: Checking if device /dev/net/tun exists                               : PASS
      QEMU: Checking for cgroup 'cpu' controller support                         : PASS
      QEMU: Checking for cgroup 'cpuacct' controller support                     : PASS
      QEMU: Checking for cgroup 'cpuset' controller support                      : PASS
      QEMU: Checking for cgroup 'memory' controller support                      : PASS
      QEMU: Checking for cgroup 'devices' controller support                     : PASS
      QEMU: Checking for cgroup 'blkio' controller support                       : PASS
      QEMU: Checking for device assignment IOMMU support                         : PASS
      QEMU: Checking if IOMMU is enabled by kernel                               : PASS
      QEMU: Checking for secure guest support                                    : WARN (Unknown if this platform has Secure Guest support)
       LXC: Checking for Linux >= 2.6.26                                         : PASS
       LXC: Checking for namespace ipc                                           : PASS
       LXC: Checking for namespace mnt                                           : PASS
       LXC: Checking for namespace pid                                           : PASS
       LXC: Checking for namespace uts                                           : PASS
       LXC: Checking for namespace net                                           : PASS
       LXC: Checking for namespace user                                          : PASS
       LXC: Checking for cgroup 'cpu' controller support                         : PASS
       LXC: Checking for cgroup 'cpuacct' controller support                     : PASS
       LXC: Checking for cgroup 'cpuset' controller support                      : PASS
       LXC: Checking for cgroup 'memory' controller support                      : PASS
       LXC: Checking for cgroup 'devices' controller support                     : PASS
       LXC: Checking for cgroup 'freezer' controller support                     : FAIL (Enable 'freezer' in kernel Kconfig file or mount/enable cgroup controller in your system)
       LXC: Checking for cgroup 'blkio' controller support                       : PASS
       LXC: Checking if device /sys/fs/fuse/connections exists                   : PASS

** Warning**\
Run [virt-host-validate] at root, otherwise the **[devices]** cgroups will fail

### [Connect types - Default []]

The connect type **[\--connect \<URI\>]** CLI option tells the Libvirt clients how to connect (transport), and optionally where.

The connect type option lets the Libvirt client ([virt-manager], [virsh]) connect to and manage the hypervisor (eg. [libvirtd], [libqemud]) daemon.

If the connect type option not used, the default URI is supplied by its Libvirt client application and is always a local hypervisor URI:

  -------------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------ ----------------------------------------------------------------------------------------------------------------------------- ----------------
  Libvirt client                                                             Default URI                                                                                            Socket Path                                                                                                                   Requires Root?
  [virsh](https://wiki.gentoo.org/wiki/Virsh "Virsh") as root                [qemu:///system]    [/run/libvirt/libvirt-sock]                ✅
  [virsh](https://wiki.gentoo.org/wiki/Virsh "Virsh") as regular user        [qemu:///session]   [\$XDG_RUNTIME_DIR/libvirt/libvirt-sock]   ❌
  [virt-manager](https://wiki.gentoo.org/wiki/Virt-manager "Virt-manager")   Both system + session
  -------------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------ ----------------------------------------------------------------------------------------------------------------------------- ----------------

### [Connect types - Required []]

URI is used to denote the specific connect type for a libvirt client to connect to a hypervisor aka libvirt daemon (e.g., [libqemud]).

The generalized syntax of the Libvirt connect URI is:

       transport[+protocol]:///target-or-path
       transport[+protocol]://[user@]hostname[:port]/target-or-path[?extra_parameters]

\
Required URI components are **[transport]** and **[target-or-path]**, but **[hostname]** is required only for remote hypervisor daemon.

\

#### [Transport]

**[qemu]** hypervisor type is the most common choice for the mandatory **[transport]** syntax component.

Set **[transport]** to one of the following hypervisor type: (`qemu`, `xen`, `lxc`, `vz`, `uml`, `bhyve`, `exs`, `vbox`, `test`, `hv`).

#### [**[target-or-path]**]

There are two types of pathways for the **[target-or-path]** syntax component of connect type URI:

-   predefined target name
-   absolute path specification

\
Depending on the **[transport]**/**[protocol]** combo, one of above syntax is used and each example given below:

  ----------------------------------------------------------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------- ------------------------------------------------------------------------------------------
  URI Example                                                                                                             Path / Target                                                                                           Meaning
  [qemu:///session]                    [session]            Per-user session daemon
  [qemu:///system]                     [system]             System-wide daemon
  [qemu+ssh://user@host/system]        [system]             Remote system daemon via SSH protocol
  [qemu+unix:///path/to/socket]        [/path/to/socket]    UNIX domain socket path, in absolute path specification.
  [test:///default]                    [default]            Named mock environment, for testing only
  [esx://user@host/?transport=https]   [?transport=https]   ESXi uses HTTP query string for configuration, in absolute path specification.
  [lxc:///]                            (empty)                                                                                                 Default system daemon for Linux [LXC](https://wiki.gentoo.org/wiki/LXC "LXC") container.
  ----------------------------------------------------------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------- ------------------------------------------------------------------------------------------

\

##### [Predefined target name]

The **[target]** name is the component to communicate within that libvirt daemon.

The connect type depends on [\$USER] environment variable for the **[target]** part of **[target-or-path]** keyword used in CLI connect type syntax:

-   [session], if regular UNIX user. Commonly used in X user-logged-in sessions.
-   [system], if root user. Useful for persistence at bootup.

\

##### [Path]

Absolute paths are the standard and expected form when specifying Unix socket locations in Libvirt URIs.

** Warning**\
Using relative path specification like [qemu+unix://./johndoe/.cache/libvirt], behavior would be unusual and typically unsupported or error-prone in Libvirt.

### [Connect types - Optional []]

Optional components to the connect type URI are detailed below.

\

#### [Hostname]

For the **[hostname]** syntax component, the host name is optional.

Hypervisor ([libqemud], formerly [libvirtd]) can be reach using a UNIX domain socket or an **[inet]** network socket.

\

##### [No Hostname]

No hostname means only **[unix]** domain socket is used.

UNIX Domain Socket is the most common usage to connect with a local host hypervisor ([libqemud]).

** Note**\
**[unix]** domain socket is located in [/var/run/libvirt/libvirt.sock].

** Tip**\
This 3-slash is identical to **[file:///]** URI. It represents a missing host name, also non-network socket.

The most common method of connecting to a local host hypervisor is through UNIX domain socket:

       /var/lib/libvirt/libvirt.sock, for non-root user
       /var/lib/libvirt/libvirt-admin.sock, for root

** Note**\
[libvirtd] UNIX domain socket is created at [/var/run/libvirt/libvirt.sock] by [libvirtd] (or other libvirt-variant VM handlers, like [virtqemud], [virtxdomd].

##### [Hostname given]

If hostname is specified, then **[inet]** network socket is used instead of UNIX domain socket.

DNS domain name lookup is used to find the IP address of the host name, which can be local or remote.

#### [Protocol]

-   **[qemu+ssh://]** - a secured connection to QEMU over SSH/TCP protocol
-   **[xen+ssh://]** - a secured connection to Xen Dom0 over SSH/TCP protocol

\
[virt-manager] can connect to multiple **[local hosts]** and **[remote hosts]** using different protocols.

\

#### [Connect types syntax]

The breakdown of Connect Type URI format is:

\

-   `+protocol` - (Optional) connection over transport (`+tcp`, `+ssh`, `+tls`, `+libssh2`, `+unix`). Default is `unix`.
-   `user@` - (Optional) SSH username. Default is `$USER` environment value.

<!-- -->

-   `:port` - (Optional) The port number to use other than the default `16509/tcp`.
-   `/path` - Path to the libvirt UNIX socket on the remote machine (`/session` or `/system` (default)).

##### [Connect Type URI Usage]

For command line, pass the connect type for a local host:

`host$``virsh --connect=qemu:///session`

or

`host-root#``virt-manager -c qemu:///system`

Using an environment variable, pass the connect type for a local host:

`host$``export LIBVIRT_DEFAULT_URI=qemu:///session; virsh`

To connect to the hypervisor, choose one of the valid hypervisor code:

Hypervisor code name

Description

`qemu`

**[local host]** UNIX domain socket to [QEMU](https://wiki.gentoo.org/wiki/QEMU "QEMU").

`xen`

**[local host]** [Xen](https://wiki.gentoo.org/wiki/Xen "Xen") Domain 0 (Dom0).

`lxc`

`vz`

`uml`

`bhyve`

`exs`

`vbox`

`test`

`hv`

When using system connection (**[\--connect=qemu:///system]**), the files accessed are:

-   [/run/libvirt/libvirt-sock]
-   [/run/libvirt/libvirt-admin-sock]
-   [/run/libvirt/libvirt-sock-ro]

When using session connection (**[\--connect=qemu:///session]**), the files accessed are:

-   [/run/user/1000/libvirt/libvirt-sock]
-   [/run/user/1000/libvirt/libvirt-admin-sock]

\
More URI details at \[[libvirt.org URI](https://www.libvirt.org/uri.html)\].

### [Invocation]

For invocation of the command line interface (CLI) of [libvirt], see [virsh invocation](https://wiki.gentoo.org/wiki/Virsh#Invocation "Virsh").

For invocation of the [libvirtd] daemon:

`user `[`$`]`libvirtd --help`

    Usage:
      libvirtd [options]

    Options:
      -h | --help            Display program help
      -v | --verbose         Verbose messages
      -d | --daemon          Run as a daemon & write PID file
      -l | --listen          Listen for TCP/IP connections
      -t | --timeout <secs>  Exit after timeout period
      -f | --config <file>   Configuration file
      -V | --version         Display version information
      -p | --pid-file <file> Change name of PID file

    libvirt management daemon:

      Default paths:

        Configuration file (unless overridden by -f):
          /etc/libvirt/libvirtd.conf

        Sockets:
          /run/libvirt/libvirt-sock
          /run/libvirt/libvirt-sock-ro

        TLS:
          CA certificate: /etc/pki/CA/cacert.pem
          Server certificate: /etc/pki/libvirt/servercert.pem
          Server private key: /etc/pki/libvirt/private/serverkey.pem

        PID file (unless overridden by -p):
          /run/libvirtd.pid

** Note**\
[virsh] cannot assist with the creation of XML files needed by [libvirt]. This is what some [virt-\*] tools and [QEMU front-ends](https://wiki.gentoo.org/wiki/QEMU/Front-ends "QEMU/Front-ends") are for.

## [Removal]

Removal of [[[app-emulation/libvirt]](https://packages.gentoo.org/packages/app-emulation/libvirt)[]] package (toolkit, library, and utilities) can be done by executing:

`root `[`#`]`emerge --ask --depclean --verbose app-emulation/libvirt`

## [Troubleshooting]

### [][Messages mentioning \...or mount/enable cgroup controller in your system]

Some of those messages are addressed on the [previous section about the kernel configuration](#Some_extra_configurations).

If the above doesn\'t fix the problem, follow the section [Control groups](https://wiki.gentoo.org/wiki/LXC#Control_groups "LXC") on the LXC page to activate the correct kernel options.

### [][WARN (Unknown if this platform has Secure Guest support)]

This message appears on non [IBM s390](https://en.wikipedia.org/wiki/IBM_System/390 "wikipedia:IBM System/390") or [AMD systems](https://en.wikipedia.org/wiki/Advanced_Micro_Devices "wikipedia:Advanced Micro Devices") and seems to be of little relevance ^[\[1\]](#cite_note-1)^ ^[\[2\]](#cite_note-2)^ ^[\[3\]](#cite_note-3)^ ^[\[4\]](#cite_note-4)^.

### [][[] Docker doesn\'t work]

Can Libvirt Work with [Docker](https://wiki.gentoo.org/wiki/Docker "Docker")?

While Libvirt itself doesn't manage Docker containers, there are workarounds to make them work

-   Running Docker inside a VM managed by Libvirt:
    -   You can create a VM using Libvirt/KVM and install Docker inside it.
    -   Useful for isolating Docker workloads in a dedicated VM.
-   Using [Libvirt-lxc](https://libvirt.org/drvlxc.html) (Limited Support):
    -   Libvirt has an [LXC](https://wiki.gentoo.org/wiki/LXC "LXC") (Linux Containers) driver, which is somewhat similar to Docker.
    -   However, libvirt-lxc is not as feature-rich as Docker.
-   Using [Podman](https://wiki.gentoo.org/wiki/Podman "Podman") (A Docker Alternative) with Libvirt:
    -   Podman is a rootless container tool compatible with Docker.
    -   Unlike Docker, Podman does not require a daemon, making it easier to run inside Libvirt-managed VMs.

\

### [[] Using Libvirt with Android]

Workarounds to Use Libvirt with Android.

While Libvirt cannot directly manage Google AVF and its **[pKVM]**s, you can:

-   Use Libvirt to manage Android x86/x64 VMs on Linux (via QEMU/KVM).
-   Run Android inside a Libvirt-managed VM (e.g., using android-x86 ISO on QEMU/KVM).
-   Use Libvirt on Android devices running full Linux distributions (e.g., via Termux or a rooted environment).

## [See also]

-   [Virtualization](https://wiki.gentoo.org/wiki/Virtualization "Virtualization") --- the concept and technique that permits running software in an environment separate from a computer operating system.
-   [QEMU](https://wiki.gentoo.org/wiki/QEMU "QEMU") --- a generic, open-source hardware emulator and virtualization suite.
-   [QEMU/Front-ends](https://wiki.gentoo.org/wiki/QEMU/Front-ends "QEMU/Front-ends") --- facilitate VM management and use

<!-- -->

-   [Libvirt/QEMU_networking](https://wiki.gentoo.org/wiki/Libvirt/QEMU_networking "Libvirt/QEMU networking") --- details the setup of Gentoo networking by [Libvirt] for use by guest containers and [QEMU](https://wiki.gentoo.org/wiki/QEMU "QEMU")-based virtual machines.
-   [Libvirt/QEMU_guest](https://wiki.gentoo.org/wiki/Libvirt/QEMU_guest "Libvirt/QEMU guest") --- creation of a guest domain (virtual machine, VM), running inside a QEMU hypervisor, using tools found in [[[libvirt]](https://packages.gentoo.org/packages/libvirt)[]] package.

<!-- -->

-   [Virt-manager](https://wiki.gentoo.org/wiki/Virt-manager "Virt-manager") --- lightweight GUI application designed for managing virtual machines and containers via the [libvirt] API.
-   [Virt-manager/QEMU_guest](https://wiki.gentoo.org/wiki/Virt-manager/QEMU_guest "Virt-manager/QEMU guest") --- creation of a guest virtual machine (VM) running inside a QEMU hypervisor using just the [virt-manager] GUI tool.

<!-- -->

-   [QEMU/Linux guest](https://wiki.gentoo.org/wiki/QEMU/Linux_guest "QEMU/Linux guest") --- describes the setup of a Gentoo Linux guest in [QEMU](https://wiki.gentoo.org/wiki/QEMU "QEMU") using Gentoo bootable media.
-   [Virsh](https://wiki.gentoo.org/wiki/Virsh "Virsh") --- a CLI-based [virtualization](https://wiki.gentoo.org/wiki/Virtualization "Virtualization") management toolkit
-   [Libvirt/libvirtd](https://wiki.gentoo.org/wiki/Libvirt/libvirtd "Libvirt/libvirtd") --- a daemon for [Libvirt] management of virtual machines.
-   [Virt-install](https://wiki.gentoo.org/wiki/Virt-install "Virt-install") --- a CLI-based [virtualization](https://wiki.gentoo.org/wiki/Virtualization "Virtualization") machine creator utility.

## [External resources]

-   [Daniel P. Berrangé libvirt announcements](https://www.berrange.com/topics/libvirt/)
-   [Red Hat Virtualization Network Configuration](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/5/html/virtualization/chap-virtualization-network_configuration)
-   [Create libvirt XML file for a virtual machine (VM) of Gentoo Install CD](http://www.unixversal.com/linux/gentoo/install10-1.html)

## [References]

1.  [[[↑](#cite_ref-1)] [Libvirt [Protected Virtualization on s390](https://libvirt.org/kbase/s390_protected_virt.html)]]
2.  [[[↑](#cite_ref-2)] [libvir-list mailing list [PATCH 3/6 qemu: check if AMD secure guest support is enabled](https://listman.redhat.com/archives/libvir-list/2020-May/202495.html)]]
3.  [[[↑](#cite_ref-3)] [libvir-list mailing list [PATCH 4/6 tools: secure guest check on s390 in virt-host-validate](https://listman.redhat.com/archives/libvir-list/2020-May/202496.html)]]
4.  [[[↑](#cite_ref-4)] [libvir-list mailing list [PATCH 5/6 tools: secure guest check for AMD in virt-host-validate](https://listman.redhat.com/archives/libvir-list/2020-May/202492.html)]]