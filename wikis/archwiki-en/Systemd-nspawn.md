# Systemd-nspawn

systemd-nspawn is like the chroot command, but it is a chroot on steroids.

systemd-nspawn may be used to run a command or operating system in a light-weight namespace container. It is more powerful than chroot since it fully virtualizes the file system hierarchy, as well as the process tree, the various IPC subsystems and the host and domain name.

systemd-nspawn limits access to various kernel interfaces in the container to read-only, such as ,  or . Network interfaces and the system clock may not be changed from within the container. Device nodes may not be created. The host system cannot be rebooted and kernel modules may not be loaded from within the container.

systemd-nspawn is a simpler tool to configure than LXC or Libvirt.

## Installation
systemd-nspawn is part of and packaged with .

## Examples
## Create and boot a minimal Arch Linux container
Create a directory to hold the container, in this example we will use .

Use pacstrap from  package to install a basic Arch system into the container. At minimum we need to install the  package.

 # pacstrap -K -c ~/MyContainer base packages/groups

Once your installation is finished, enter the container, and set a root password:

 # systemd-nspawn -D ~/MyContainer
 # passwd
 # logout

Finally, boot into the container:

 # systemd-nspawn -b -D ~/MyContainer

The  option will boot the container (i.e. run  as PID=1), instead of just running a shell, and  specifies the directory that becomes the container's root directory.

After the container starts, log in as "root" with your password.

The container can be powered off by running  from within the container. From the host, containers can be controlled by the machinectl tool.

## Create a Debian or Ubuntu environment
Install , and one or both of  or  depending on which distribution you want.

Then invoke deboostrap with the following structure:

 # debootstrap SUITE TARGET [MIRROR

* SUITE (required) is the code name or alias for the specific version of the desired distribution as found in the scripts directory:
** for Debian, valid suite names are either the stable aliases ,  and , or release names like  and : see for a list.
**For Ubuntu, only version names such as  and  should be used and not version numbers: see [https://wiki.ubuntu.com/Releases and for a table of code names to version numbers.
** other references exist in the scripts directory for other Debian-based distributions such as Devuan, eLxr, Kali Linux, Pardus, PureOS, Trisquel and Tanglu (discontinued since 2017). Invoking those usually require acquiring their specific keyring and passing it to the  option, or disabling checking OpenPGP signatures of retrieved Release files with .
* TARGET (required) is the directory that will contain the debootstrapped system; it will be created if it does not yet exist.
* MIRROR (optional): the archive URL from which packages should be downloaded. For current Debian releases it can be any [https://www.debian.org/mirror/list valid mirror such as the CDN-backed https://deb.debian.org/debian (default), and for Ubuntu any mirror from such as the reference https://archive.ubuntu.com/ubuntu (also used by default).
:

debootstrap cannot resolve dependencies on virtual package[https://forums.debian.net/viewtopic.php?t=160578, and as a consequence it does not install systemds  and  recommended dependencies by defaultAs a consequence, some systemd/dbus-related functionalities (e.g. localectl) as well as managing the container with #machinectl do not work out of the box.

In order to get full functionality in systemd-based systems, add  to the debootstrap invocation or install those packages once in the container:

 # debootstrap --include=dbus,libpam-systemd,libnss-systemd stable /path/to/machine

Just like Arch, Debian and Ubuntu will not let you log in without a password. To set the root password, run systemd-nspawn without the  option:

 # systemd-nspawn -D /path/to/machine
 # passwd
 # logout

## Create a RHEL-derivative environment using Podman or Docker
These instructions should be applicable to any distribution which uses . You will need Podman or Docker.

 # mkdir -p /var/lib/machines/my-machine
 # podman pull centos:stream9
 # podman run --rm -it -v /var/lib/machines/my-machine:/machine centos:stream9

From within that container, you can build the root environment for your machine:

 bash-5.1# dnf update -y
 bash-5.1# dnf --repo=baseos \
               --releasever=9 \
               --best \
               --installroot=/machine \
               install \
               systemd-udev \
               hostname \
               yum \
               dnf \
               centos-gpg-keys \
               centos-stream-release \
               rootfiles \
               shadow-utils \
               util-linux
 bash-5.1# sed -i 's/^root:[^:*:/root::/' /machine/etc/shadow # remove root password for initial login
 bash-5.1# exit

From there, you should be able to boot the machine:

 # systemd-nspawn --machine=my-machine --boot

## Create a Fedora or AlmaLinux environment
Install , and edit the  file to add the required Fedora repositories.

The fedora.gpg file contain the gpg keys for the latest Fedora releases https://getfedora.org/security/. To set up a minimal Fedora 42 container:

 # mkdir /var/lib/machines/container-name
 # dnf5 --releasever=42 --best --use-host-config --setopt=install_weak_deps=False --repo=fedora --repo=updates --installroot=/var/lib/machines/container-name install dhcp-client dnf fedora-release glibc glibc-langpack-en iputils less ncurses passwd systemd systemd-networkd systemd-resolved util-linux vim-default-editor

An Enterprise Linux derivative like AlmaLinux has three repositories enabled by default, BaseOS wich contains a core set that provides the basis for all installations, AppStream that includes additional applications, language packages, etc and Extras that contains packages not included in RHEL. So for a minimal container we only need to add the BaseOS repository to

To create an AlmaLinux 9 minimal container:

 # dnf --repo=baseos --releasever=9 --best --installroot=/var/lib/machines/container-name --setopt=install_weak_deps=False install almalinux-release dhcp-client dnf glibc-langpack-en iproute iputils less passwd systemd vim-minimal

This will install the latest minor version of AlmaLinux 9, you can choose to install a specific point release, but you will need to change the gpgpkey entry to manually point to RPM-GPG-KEY-AlmaLinux-9

Just like Arch, Fedora or AlmaLinux will not let you log in as root without a password. To set up the root password, run systemd-nspawn without the  option:

 # systemd-nspawn -D /var/lib/machines/container-name passwd

## Build and test packages
See Creating packages for other distributions for example uses.

## Management
Containers located in  can be controlled by the machinectl command, which internally controls instances of the  unit. The subdirectories in  correspond to the container names, i.e. .

## Default systemd-nspawn options
Note that containers started via machinectl or  use different default options than containers started manually by the systemd-nspawn command. The extra options used by the service are:

* / – Managed containers automatically search for an init program and invoke it as PID 1.
*  which implies  – Managed containers get a virtual network interface and are disconnected from the host network. See #Networking for details.
*  – Managed containers use the  feature by default if supported by the kernel. See #Unprivileged containers for implications.
*

This behavior can be overridden in per-container configuration files. See #Configuration for details.

## machinectl
Containers can be managed by the  command. For example, to start a container:

 $ machinectl start container-name

Similarly, there are subcommands such as , ,  and . See  for detailed explanations.

Other common commands are:

*  – show a list of currently running containers
*  – open an interactive login session in a container
*  – open an interactive shell session in a container (this immediately invokes a user process without going through the login process in the container)
*  and  – enable or disable a container to start at boot, see #Enable container to start at boot for details

machinectl also has subcommands for managing container (or virtual machine) images and image transfers. See  and  for details. As of 2023Q1, the first 3 examples at  demonstrate image transfer commands.  discusses where to find suitable images.

## systemd toolchain
Much of the core systemd toolchain has been updated to work with containers. Tools that do usually provide a  option which will take a container name as argument.

Examples:

See journal logs for a particular machine:

 # journalctl -M container-name

Show control group contents:

 $ systemd-cgls -M container-name

See startup time of container:

 $ systemd-analyze -M container-name

For an overview of resource usage:

 $ systemd-cgtop

## Configuration
## Per-container settings
To specify per-container settings and not global overrides, the .nspawn files can be used. See  for details.

## Enable container to start at boot
When using a container frequently, you may want to start it at boot.

First make sure that the  is enabled.

Containers discoverable by machinectl can be enabled or disabled:

 $ machinectl enable container-name

## Resource control
You can take advantage of control groups to implement limits and resource management of your containers with , see . For example, you may want to limit the memory amount or CPU usage. To limit the memory consumption of your container to 2 GiB:

 # systemctl set-property systemd-nspawn@container-name.service MemoryMax=2G

Or to limit the CPU time usage to roughly the equivalent of 2 cores:

 # systemctl set-property systemd-nspawn@container-name.service CPUQuota=200%

This will create permanent files in .

According to the documentation,  is the preferred method to keep in check memory consumption, but it will not be hard-limited as is the case with . You can use both options leaving  as the last line of defense. Also take in consideration that you will not limit the number of CPUs the container can see, but you will achieve similar results by limiting how much time the container will get at maximum, relative to the total CPU time.

## Networking
systemd-nspawn containers can use either host networking or private networking:

* In the host networking mode, the container has full access to the host network. This means that the container will be able to access all network services on the host and packets coming from the container will appear to the outside network as coming from the host (i.e. sharing the same IP address).
* In the private networking mode, the container is disconnected from the host's network. This makes all network interfaces unavailable to the container, with the exception of the loopback device and those explicitly assigned to the container. There is a number of different ways to set up network interfaces for the container:
** An existing interface can be assigned to the container (e.g. if you have multiple Ethernet devices): see #Use an existing interface.
** A virtual network interface associated with an existing interface (i.e. VLAN interface) can be created and assigned to the container: see #Use a "macvlan" or "ipvlan" interface.
** A virtual Ethernet link between the host and the container can be created: see #Use a virtual Ethernet link.
: In the latter case the container's network is fully isolated (from the outside network as well as other containers) and it is up to the administrator to configure networking between the host and the containers. This typically involves using NAT networking between multiple interfaces or using a network bridge to connect multiple (physical or virtual) interfaces.

The host networking mode is suitable for application containers which do not run any networking software that would configure the interface assigned to the container. Host networking is the default mode when you run systemd-nspawn from the shell.

On the other hand, the private networking mode is suitable for system containers that should be isolated from the host system. The creation of virtual Ethernet links is a very flexible tool allowing to create complex virtual networks. This is the default mode for containers started by machinectl or .

The following subsections describe common scenarios. See  for details about the available systemd-nspawn options.

## Host networking
To disable private networking and the creation of a virtual Ethernet link used by containers started with machinectl, add a .nspawn file with the following option:

This will override the / option used in  and the newly started containers will use the host networking mode.

## Private networking
## Use a virtual Ethernet link
If a container is started with the / option, systemd-nspawn will create a virtual Ethernet link between the host and the container. The host side of the link will be available as a network interface named . The container side of the link will be named . Note that this option implies .

When you start the container, an IP address has to be assigned to both interfaces (on the host and in the container). If you use systemd-networkd on the host as well as in the container, this is done out-of-the-box:

* the  file on the host matches the  interface and starts a DHCP server, which assigns IP addresses to the host interface as well as the container,
* the  file in the container matches the  interface and starts a DHCP client, which receives an IP address from the host.

If you do not use systemd-networkd, you can configure static IP addresses or start a DHCP server on the host interface and a DHCP client in the container. See Network configuration for details.

## Use NAT networking
To give the container access to the outside network, you can configure NAT as described in Internet sharing#Enable NAT. If you use systemd-networkd, this is done (partially) automatically via the  option in . However, this issues just one iptables (or nftables) rule such as

 -t nat -A POSTROUTING -s 192.168.163.192/28 -j MASQUERADE

The  table has to be configured manually as shown in Internet sharing#Enable NAT. You can use a wildcard to match all interfaces starting with :

 # iptables -A FORWARD -i ve-+ -o internet0 -j ACCEPT

Additionally, you need to open the UDP port 67 on the  interfaces for incoming connections to the DHCP server (operated by systemd-networkd):

 # iptables -A INPUT -i ve-+ -p udp -m udp --dport 67 -j ACCEPT

## Use a network bridge
If you have configured a network bridge on the host system, you can create a virtual Ethernet link for the container and add its host side to the network bridge. This is done with the  option. Note that  implies , i.e. the virtual Ethernet link is created automatically. However, the host side of the link will use the  prefix instead of , so the systemd-networkd options for starting the DHCP server and IP masquerading will not be applied.

The bridge management is left to the administrator. For example, the bridge can connect virtual interfaces with a physical interface, or it can connect only virtual interfaces of several containers. See systemd-networkd#Network bridge with DHCP and systemd-networkd#Network bridge with static IP addresses for example configurations using systemd-networkd.

There is also a  option which is similar to  but the network bridge is managed automatically by systemd-nspawn and systemd-networkd. The bridge interface named  is automatically created when the first container configured with  is started, and is automatically removed when the last container configured with  exits. Hence, this option makes it easy to place multiple related containers on a common virtual network. Note that  interfaces are managed by systemd-networkd same way as  interfaces using the options from the  file.

## Use a "macvlan" or "ipvlan" interface
Instead of creating a virtual Ethernet link (whose host side may or may not be added to a bridge), you can create a virtual interface on an existing physical interface (i.e. VLAN interface) and add it to the container. The virtual interface will be bridged with the underlying host interface and thus the container will be exposed to the outside network, which allows it to obtain a distinct IP address via DHCP from the same LAN as the host is connected to.

systemd-nspawn offers 2 options:

*  – the virtual interface will have a different MAC address than the underlying physical  and will be named .
*  – the virtual interface will have the same MAC address as the underlying physical  and will be named .

Both options imply .

## Use an existing interface
If the host system has multiple physical network interfaces, you can use the  to assign  to the container (and make it unavailable to the host while the container is started). Note that  implies .

## Port mapping
When private networking is enabled, individual ports on the host can be mapped to ports on the container using the / option or by using the  setting in an .nspawn file. For example, to map a TCP port 8000 on the host to the TCP port 80 in the container:

This works by issuing iptables (or nftables) rules to the  table, but the  chain in the  table needs to be configured manually as shown in #Use a virtual Ethernet link. Additionally, if you followed Simple stateful firewall, run the following command to allow new connections to the host's  on a forwarded port to be established:

 # iptables -A FORWARD -i wan_interface -o ve-+ -p tcp --syn --dport 8000 -m conntrack --ctstate NEW -j ACCEPT

## Domain name resolution
Domain name resolution in the container can be configured the same way as on the host system. Additionally, systemd-nspawn provides options to manage the  file inside the container:

*  can be used on command-line
*  can be used in .nspawn files

These corresponding options have many possible values which are described in . The default value is , which means that:

* If  is enabled, the  is left as it is in the container.
* Otherwise, if systemd-resolved is running on the host, its stub  file is copied or bind-mounted into the container.
* Otherwise, the  file is copied or bind-mounted from the host to the container.

In the last two cases, the file is copied, if the container root is writeable, and bind-mounted if it is read-only.

For the second case where systemd-resolved runs on the host, systemd-nspawn expects it to also run in the container, so that the container can use the stub symlink file  from the host. If not, the default value  no longer works, and you should replace the symlink by using one of the  options.

## Tips and tricks
## Running non-shell/init commands
From :
:option  the shell or specified program as process ID (PID) 2 instead of PID 1 (init). [... It is recommended to use this mode to invoke arbitrary commands in containers, unless they have been modified to run correctly as PID 1. Or in other words: this switch should be used for pretty much all commands, except when the command refers to an init or shell implementation This option may not be combined with .

## Unprivileged containers
systemd-nspawn supports unprivileged containers, though the containers need to be booted as root.

The easiest way to do this is to let systemd-nspawn automatically choose an unused range of UIDs/GIDs by using the  option:

 # systemd-nspawn -bUD ~/MyContainer

If kernel supports user namespaces, the  option is equivalent to . See  for details.

If a container has been started with a private UID/GID range using the  option (or on a filesystem where  requires ), you need to keep using it that way to avoid permission errors. Alternatively, it is possible to undo the effect of  on the container's file system by specifying a range of IDs starting at 0:

 # systemd-nspawn -D ~/MyContainer --private-users=0 --private-users-ownership=chown

## Use an X environment
See Xhost and Change root#Run graphical applications from chroot.

You will need to set the  environment variable inside your container session to connect to the external X server.

X stores some required files in the  directory. In order for your container to display anything, it needs access to those files. To do so, append the  option when starting the container.

## Avoiding xhost
 only provides rather coarse access rights to the X server. More fine-grained access control is possible via the  file. Unfortunately, just making the  file accessible in the container will not do the job:
your  file is specific to your host, but the container is a different host.
The following trick adapted from [https://stackoverflow.com/a/25280523 stackoverflow can be used to make your X server accept the  file from an X application run inside the container:

 $ XAUTH=/tmp/container_xauth
 $ xauth nextract - "$DISPLAY" | sed -e 's/^..../ffff/' | xauth -f "$XAUTH" nmerge -
 # systemd-nspawn -D myContainer --bind=/tmp/.X11-unix --bind="$XAUTH" -E DISPLAY="$DISPLAY" -E XAUTHORITY="$XAUTH" --as-pid2 /usr/bin/xeyes

The second line above sets the connection family to "FamilyWild", value , which causes the entry to match every display. See  for more information.

## Using X nesting/Xephyr
Another simple way to run X applications and avoid the risks of a shared X desktop is using X nesting.
The advantages here are avoiding interaction between in-container applications and non-container applications entirely and being able to run a different desktop environment or window manager. The downsides are less performance, and the lack of hardware acceleration when using Xephyr.

Start Xephyr outside of the container using:

 # Xephyr :1 -resizeable

Then start the container with the following options:

 --setenv=DISPLAY=:1 --bind-ro=/tmp/.X11-unix/X1

No other binds are necessary.

You might still need to manually set  in the container under some circumstances (mostly if used with ).

## Run Firefox
 # systemd-nspawn --setenv=DISPLAY=:0 \
               --setenv=XAUTHORITY=~/.Xauthority \
               --bind-ro=$HOME/.Xauthority:/root/.Xauthority \
               --bind=/tmp/.X11-unix \
               -D ~/containers/firefox \
               --as-pid2 \
               firefox

Alternatively you can boot the container and let e.g. systemd-networkd set up the virtual network interface:

 # systemd-nspawn --bind-ro=$HOME/.Xauthority:/root/.Xauthority \
               --bind=/tmp/.X11-unix \
               -D ~/containers/firefox \
               --network-veth -b

Once your container is booted, run the Xorg binary like so:

 # systemd-run -M firefox --setenv=DISPLAY=:0 firefox

## 3D graphics acceleration
To enable accelerated 3D graphics, it may be necessary to bind mount  to the container by adding the following line to the .nspawn file:

 Bind=/dev/dri

The above trick was adopted from patrickskiba.com. This notably solves the problem of

 libGL error: MESA-LOADER: failed to retrieve device information
 libGL error: Version 4 or later of flush extension not found
 libGL error: failed to load driver: i915

You can confirm that it has been enabled by running  or .

## NVIDIA GPUs
If you cannot install the same NVIDIA driver version on the container as on the host, you may need to also bind the driver library files. You can run  on the host to see all the files it contains. You do not need to copy everything over. The following systemd override file will bind all the necessary files over when the container is run via .

## Access host filesystem
See  and  in .

If both the host and the container are Arch Linux, then one could, for example, share the pacman cache:

 # systemd-nspawn --bind=/var/cache/pacman/pkg

Or you can specify per-container bind using the file:

See #Per-container settings.

To bind the directory to a different path within the container, add the path be separated by a colon. For example:

 # systemd-nspawn --bind=/path/to/host_dir:/path/to/container_dir

In case of #Unprivileged containers, the resulting mount points will be owned by the nobody user. This can be modified with the  mount option:
 # systemd-nspawn --bind=/path/to/host_dir:/path/to/container_dir:idmap

## Run on a non-systemd system
See Init#systemd-nspawn.

## Use Btrfs subvolume as container root
To use a Btrfs subvolume as a template for the container's root, use the  flag. This takes a snapshot of the subvolume and populates the root directory for the container with it.

For example, to use a snapshot located at :

 # systemd-nspawn --template=/.snapshots/403/snapshot -b -D my-container

where  is the name of the directory that will be created for the container. After powering off, the newly created subvolume is retained.

## Use temporary Btrfs snapshot of container
One can use the  or  flag to create a temporary btrfs snapshot of the container and use it as the container root. Any changes made while booted in the container will be lost. For example:

 # systemd-nspawn -D my-container -xb

where my-container is the directory of an existing container or system. For example, if  is a btrfs subvolume one could create an ephemeral container of the currently running host system by doing:

 # systemd-nspawn -D / -xb

After powering off the container, the btrfs subvolume that was created is immediately removed.

## Run docker in systemd-nspawn
Since Docker 20.10, it is possible to run Docker containers inside an unprivileged systemd-nspawn container with cgroups v2 enabled (default in Arch Linux) without undermining security measures by disabling cgroups and user namespaces. To do so, edit  (create if absent) and add the following configurations.

Then, Docker should work as-is inside the container.

With recent versions of systemd, you would also need to need the following workaround:

See for more details.

Since overlayfs does not work with user namespaces and is unavailable inside systemd-nspawn, by default, Docker falls back to using the inefficient vfs as its storage driver, which creates a copy of the image each time a container is started. This can be worked around by using fuse-overlayfs as its storage driver. To do so, we need to first expose fuse to the container:

and then allow the container to read and write the device node:

 # systemctl set-property systemd-nspawn@myContainer DeviceAllow='/dev/fuse rwm'

Finally, install the package  inside the container. You need to restart the container for all the configuration to take effect.

## Map a local user and bind-mount their home directory into a container
Create a container in  as explained in #Create and boot a minimal Arch Linux container.

Create a configuration file with  to map the selected local user name into the container. Note that this requires , see  for details. Files created in the bind-mounted home directory both inside and outside the container will have the same UID and GID.

Having also  in the configuration specifies the default user used for running commands inside the container, such as the interactive shell:

 # systemd-nspawn -M MyContainer bash

This is helpful for testing Arch Linux packages from another Linux distribution.

## Troubleshooting
## execv(...) failed: Permission denied
When trying to boot the container via  (or executing something in the container), and the following error comes up:

 execv(/usr/lib/systemd/systemd, /lib/systemd/systemd, /sbin/init) failed: Permission denied

even though the permissions of the files in question (i.e. ) are correct, this can be the result of having mounted the file system on which the container is stored as non-root user. For example, if you mount your disk manually with an entry in fstab that has the options , systemd-nspawn will not allow executing the files even if they are owned by root.

## Terminal type in TERM is incorrect (broken colors)
When logging into the container via , the colors and keystrokes in the terminal within the container might be broken. This may be due to an incorrect terminal type in  environment variable. The environment variable is not inherited from the shell on the host, but falls back to a default fixed in systemd (), unless explicitly configured. To configure, within the container create a configuration overlay for the  systemd service that launches the login getty for , and set  to the value that matches the host terminal you are logging in from:

Alternatively use . It properly inherits the  environment variable from the terminal.

## Mounting a NFS share inside the container
Not possible at this time (June 2019).
