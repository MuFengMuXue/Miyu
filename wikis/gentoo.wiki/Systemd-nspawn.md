[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=Systemd/systemd-nspawn&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

**Resources**

[[![Gentoo peach graphic](/images/thumb/a/ad/Gentoo-logo-peach.svg/25px-Gentoo-logo-peach.svg.png)](https://wiki.gentoo.org/wiki/Project:Systemd "Project:Systemd")][Project](https://wiki.gentoo.org/wiki/Project:Systemd "Project:Systemd")

[[]][Home](https://nspawn.org/)

[[]][Official documentation](https://www.freedesktop.org/software/systemd/man/systemd-nspawn.html)

**[systemd-nspawn]** is a lightweight, loosely [chroot](https://wiki.gentoo.org/wiki/Chroot "Chroot")-like, OS-level [OCI container](https://opencontainers.org/) environment native to [systemd](https://wiki.gentoo.org/wiki/Systemd "Systemd"). Each container exists in its own [namespace](https://wiki.gentoo.org/wiki/Namespaces "Namespaces") but within the host\'s running kernel. Thus, no hardware emulation is taking place and unlike [QEMU](https://wiki.gentoo.org/wiki/QEMU "QEMU") and [Virtualbox](https://wiki.gentoo.org/wiki/Virtualbox "Virtualbox") non-native CPU instruction sets are not directly supported.

Like a lot of technologies, containerization has trade-offs. A core benefit of containerization is that there is much less overhead than with a traditional virtual machine, so it\'s possible to spawn a large number of containers much more quickly than a large number of VMs. Unfortunately, though uncommon, exploits leading to container escapes have happened and are more prevalent than VM escapes. Further, any containerized processes that causes a kernel crash will bring down the host system as they share a kernel. Lastly, containers are not, by default, more secure than any other processes on the host system. Hardening containers can be done through a mix of technologies such as [cgroups](https://wiki.gentoo.org/wiki/Cgroups "Cgroups"), to constrain resource utilization, and [SELinux](https://wiki.gentoo.org/wiki/SELinux "SELinux") to prevent privilege escalation and enforce access controls.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [Files]](#Files)
    -   [[1.2] [Service]](#Service)
-   [[2] [Usage]](#Usage)
    -   [[2.1] [Invocation]](#Invocation)
-   [[3] [Container setup]](#Container_setup)
    -   [[3.1] [OpenRC]](#OpenRC)
-   [[4] [Troubleshooting]](#Troubleshooting)
    -   [[4.1] [Can I combine QEMU and systemd-nspawn to cross-compile binaries?]](#Can_I_combine_QEMU_and_systemd-nspawn_to_cross-compile_binaries.3F)
    -   [[4.2] [Improper terminal colors]](#Improper_terminal_colors)
    -   [[4.3] [Unable to enable loopback interface: Operation not permitted]](#Unable_to_enable_loopback_interface:_Operation_not_permitted)
-   [[5] [See also]](#See_also)
-   [[6] [External resources]](#External_resources)
    -   [[6.1] [Image Repositories]](#Image_Repositories)

## [Installation]

In order to use [systemd-nspawn] a system must be set to a [profile](https://wiki.gentoo.org/wiki/Profile_(Portage) "Profile (Portage)") that uses the [systemd](https://wiki.gentoo.org/wiki/Systemd "Systemd") init system.

### [Files]

-   [/var/lib/machines/\*] --- the canonical location for [systemd-nspawn] container file systems.

To prevent confusion, it is best practice to name the subdirectory holding the container\'s root file system after the container\'s hostname.

### [Service]

Assuming a properly structured and syntactically unit file, containers should be discoverable by [machinectl]. The unit file needs to be located at [/etc/systemd/nswpan/\<machine_name\>.nspawn]. Thereafter it can be managed like any other service.

## [Usage]

Assuming, for example, a Gentoo root file system exists at [/var/lib/machines/larrythecow/] that has been extracted from a stage3 tarball for the host\'s instruction set architecture the following commands should bring the container up:

`root `[`#`]`systemd-nspawn -b -D /var/lib/machines/larrythecow`

The handbook can be followed as normal from this point forward excluding unnecessary bits, such as kernel and bootloader configuration. Once done, the container can be used by itself or as an up-to-date template from which other containers can be spawned. The latter case is made easier if the container\'s root file system is stored on a [BTRFS](https://wiki.gentoo.org/wiki/Btrfs "Btrfs") subvolume.

### [Invocation]

`user `[`$`]`systemd-nspawn --help`

    systemd-nspawn [OPTIONS...] [PATH] [ARGUMENTS...]

    Spawn a command or OS in a light-weight container.

      -h --help                 Show this help
         --version              Print version string
      -q --quiet                Do not show status information
         --no-pager             Do not pipe output into a pager
         --settings=BOOLEAN     Load additional settings from .nspawn file

    Image:
      -D --directory=PATH       Root directory for the container
         --template=PATH        Initialize root directory from template directory,
                                if missing
      -x --ephemeral            Run container with snapshot of root directory, and
                                remove it after exit
      -i --image=PATH           Root file system disk image (or device node) for
                                the container
         --oci-bundle=PATH      OCI bundle directory
         --read-only            Mount the root directory read-only
         --volatile[=MODE]      Run the system in volatile mode
         --root-hash=HASH       Specify verity root hash for root disk image
         --root-hash-sig=SIG    Specify pkcs7 signature of root hash for verity
                                as a DER encoded PKCS7, either as a path to a file
                                or as an ASCII base64 encoded string prefixed by
                                'base64:'
         --verity-data=PATH     Specify hash device for verity
         --pivot-root=PATH[:PATH]
                                Pivot root to given directory in the container

    Execution:
      -a --as-pid2              Maintain a stub init as PID1, invoke binary as PID2
      -b --boot                 Boot up full system (i.e. invoke init)
         --chdir=PATH           Set working directory in the container
      -E --setenv=NAME[=VALUE]  Pass an environment variable to PID 1
      -u --user=USER            Run the command under specified user or UID
         --kill-signal=SIGNAL   Select signal to use for shutting down PID 1
         --notify-ready=BOOLEAN Receive notifications from the child init process
         --suppress-sync=BOOLEAN
                                Suppress any form of disk data synchronization

    System Identity:
      -M --machine=NAME         Set the machine name for the container
         --hostname=NAME        Override the hostname for the container
         --uuid=UUID            Set a specific machine UUID for the container

    Properties:
      -S --slice=SLICE          Place the container in the specified slice
         --property=NAME=VALUE  Set scope unit property
         --register=BOOLEAN     Register container as machine
         --keep-unit            Do not register a scope for the machine, reuse
                                the service unit nspawn is running in

    User Namespacing:
         --private-users=no     Run without user namespacing
         --private-users=yes|pick|identity
                                Run within user namespace, autoselect UID/GID range
         --private-users=UIDBASE[:NUIDS]
                                Similar, but with user configured UID/GID range
         --private-users-ownership=MODE
                                Adjust ('chown') or map ('map') OS tree ownership
                                to private UID/GID range
      -U                        Equivalent to --private-users=pick and
                                --private-users-ownership=auto

    Networking:
         --private-network      Disable network in container
         --network-interface=INTERFACE
                                Assign an existing network interface to the
                                container
         --network-macvlan=INTERFACE
                                Create a macvlan network interface based on an
                                existing network interface to the container
         --network-ipvlan=INTERFACE
                                Create an ipvlan network interface based on an
                                existing network interface to the container
      -n --network-veth         Add a virtual Ethernet connection between host
                                and container
         --network-veth-extra=HOSTIF[:CONTAINERIF]
                                Add an additional virtual Ethernet link between
                                host and container
         --network-bridge=INTERFACE
                                Add a virtual Ethernet connection to the container
                                and attach it to an existing bridge on the host
         --network-zone=NAME    Similar, but attach the new interface to an
                                an automatically managed bridge interface
         --network-namespace-path=PATH
                                Set network namespace to the one represented by
                                the specified kernel namespace file node
      -p --port=[PROTOCOL:]HOSTPORT[:CONTAINERPORT]
                                Expose a container IP port on the host

    Security:
         --capability=CAP       In addition to the default, retain specified
                                capability
         --drop-capability=CAP  Drop the specified capability from the default set
         --ambient-capability=CAP
                                Sets the specified capability for the started
                                process. Not useful if booting a machine.
         --no-new-privileges    Set PR_SET_NO_NEW_PRIVS flag for container payload
         --system-call-filter=LIST|~LIST
                                Permit/prohibit specific system calls
      -Z --selinux-context=SECLABEL
                                Set the SELinux security context to be used by
                                processes in the container
      -L --selinux-apifs-context=SECLABEL
                                Set the SELinux security context to be used by
                                API/tmpfs file systems in the container

    Resources:
         --rlimit=NAME=LIMIT    Set a resource limit for the payload
         --oom-score-adjust=VALUE
                                Adjust the OOM score value for the payload
         --cpu-affinity=CPUS    Adjust the CPU affinity of the container
         --personality=ARCH     Pick personality for this container

    Integration:
         --resolv-conf=MODE     Select mode of /etc/resolv.conf initialization
         --timezone=MODE        Select mode of /etc/localtime initialization
         --link-journal=MODE    Link up guest journal, one of no, auto, guest,
                                host, try-guest, try-host
      -j                        Equivalent to --link-journal=try-guest

    Mounts:
         --bind=PATH[:PATH[:OPTIONS]]
                                Bind mount a file or directory from the host into
                                the container
         --bind-ro=PATH[:PATH[:OPTIONS]
                                Similar, but creates a read-only bind mount
         --inaccessible=PATH    Over-mount file node with inaccessible node to mask
                                it
         --tmpfs=PATH:[OPTIONS] Mount an empty tmpfs to the specified directory
         --overlay=PATH[:PATH...]:PATH
                                Create an overlay mount from the host to
                                the container
         --overlay-ro=PATH[:PATH...]:PATH
                                Similar, but creates a read-only overlay mount
         --bind-user=NAME       Bind user from host to container

    Input/Output:
         --console=MODE         Select how stdin/stdout/stderr and /dev/console are
                                set up for the container.
      -P --pipe                 Equivalent to --console=pipe

    Credentials:
         --set-credential=ID:VALUE
                                Pass a credential with literal value to container.
         --load-credential=ID:PATH
                                Load credential to pass to container from file or
                                AF_UNIX stream socket.

    See the systemd-nspawn(1) man page for details.

## [Container setup]

In order to import a stage3 tarball, you will need the following USE flags enabled:

[FILE] **`/etc/portage/package.use`Enable systemd importd**

    sys-apps/systemd curl lzma importd

Import the releng GPG key so that systemd can find it.

`root `[`#`]`gpg --no-default-keyring --primary-keyring=/etc/systemd/import-pubring.gpg --auto-key-locate=clear,nodefault,wkd --locate-key releng@gentoo.org`

Unpack a stage3 in [/var/lib/machines].

`root `[`#`]`importctl -m pull-tar `[`https://distfiles.gentoo.org/releases/amd64/autobuilds/20240317T170433Z/stage3-amd64-openrc-20240317T170433Z.tar.xz`](https://distfiles.gentoo.org/releases/amd64/autobuilds/20240317T170433Z/stage3-amd64-openrc-20240317T170433Z.tar.xz)` openrc-20240317`

### [OpenRC]

Edit /var/lib/machines/\.../etc/inittab to disable agetty on tty\[1-6\] and enable it on console.

[FILE] **`/etc/inittab`**

    # TERMINALS
    x1:12345:respawn:/sbin/agetty 38400 console linux
    #c1:12345:respawn:/sbin/agetty --noclear 38400 tty1 linux
    #c2:2345:respawn:/sbin/agetty 38400 tty2 linux
    #c3:2345:respawn:/sbin/agetty 38400 tty3 linux
    #c4:2345:respawn:/sbin/agetty 38400 tty4 linux
    #c5:2345:respawn:/sbin/agetty 38400 tty5 linux
    #c6:2345:respawn:/sbin/agetty 38400 tty6 linux

Clear the root password in /var/lib/machines/\.../etc/shadow.

[FILE] **`/etc/shadow`**

    root::10770:0:::::

Invoke systemd-nspawn with the -b option to boot.

`root `[`#`]`systemd-nspawn -M openrc-20240317 -b`

Or, if you only want a shell and not a complete boot environment, omit the -b option.

`root `[`#`]`systemd-nspawn -M openrc-20240317`

## [Troubleshooting]

### [][Can I combine QEMU and [systemd-nspawn] to cross-compile binaries?]

Yes, follow the instructions to [build QEMU with static-user support](https://wiki.gentoo.org/wiki/Embedded_Handbook/General/Compiling_with_qemu_user_chroot "Embedded Handbook/General/Compiling with qemu user chroot"). Make sure the systemd-binfmt service is enabled. Then, start the container as normal:

`root `[`#`]`systemd-nspawn -D /var/lib/machines/<container_with_different_cpu_isa>`

### [Improper terminal colors]

If you have issues with colors not displaying correctly (e.g. [tmux](https://wiki.gentoo.org/wiki/Tmux "Tmux") does not properly display its status bar), try disabling the background tinting that was introduced in systemd-256.

`root `[`#`]`systemd-nspawn --background= ...`

### [Unable to enable loopback interface: Operation not permitted]

Use [\--capability=CAP_NET_ADMIN] and be aware of potential security issues. For more details, see github issue: [Creating a network namespace within a systemd-nspawn container](https://github.com/systemd/systemd/issues/13308).

## [See also]

-   [Docker](https://wiki.gentoo.org/wiki/Docker "Docker") --- a [container](https://en.wikipedia.org/wiki/Container_(virtualization) "wikipedia:Container (virtualization)")-based [virtualization](https://wiki.gentoo.org/wiki/Virtualization "Virtualization") system
-   [Podman](https://wiki.gentoo.org/wiki/Podman "Podman") --- a daemonless container engine for developing, managing, and running [OCI Containers](https://opencontainers.org/), aiming to be a drop-in replacement for much of [Docker](https://wiki.gentoo.org/wiki/Docker "Docker")
-   [LXC](https://wiki.gentoo.org/wiki/LXC "LXC") --- a [virtualization](https://wiki.gentoo.org/wiki/Virtualization "Virtualization") system that leverages Linux\'s [namespaces](https://wiki.gentoo.org/wiki/Namespaces "Namespaces") and [cgroups](https://wiki.gentoo.org/wiki/Cgroups "Cgroups") to create containers isolated from the host system
-   [LXD](https://wiki.gentoo.org/wiki/LXD "LXD") --- a system container manager
-   [User:Ajak/systemd-nspawn_for_Development_and_Update_Automation](https://wiki.gentoo.org/wiki/User:Ajak/systemd-nspawn_for_Development_and_Update_Automation "User:Ajak/systemd-nspawn for Development and Update Automation")

## [External resources]

-   [On Running systemd-nspawn Containers](https://benjamintoll.com/2022/02/04/on-running-systemd-nspawn-containers/)
-   [Rich0\'s Gentoo Blog: Quick systemd-nspawn guide](https://rich0gentoo.wordpress.com/2014/07/14/quick-systemd-nspawn-guide/)
-   [Systemd-nspawn for fun and... well, mostly for fun](https://blog.oddbit.com/post/2016-02-07-systemd-nspawn-for-fun-and-wel/)
-   [The container interface](https://systemd.io/CONTAINER_INTERFACE)

### [Image Repositories]

-   [https://nspawn.org/images/](https://nspawn.org/images/)