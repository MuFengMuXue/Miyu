# Linux Containers

Linux Containers (LXC) is a userspace interface for the Linux kernel containment features, providing a method for OS-level virtualization, using namespaces, cgroups and other Linux kernel  on the LXC host.  is considered something in the middle between a chroot and a full-fledged virtual machine.

Incus or LXD can be used as a manager for LXC. This page deals with using LXC directly.

Alternatives for using containers comprise systemd-nspawn, Docker and Podman.

## Privileged or unprivileged
LXC supports two types of containers: privileged and unprivileged.

On privileged containers, the root UID—UID 0—within the container is mapped to the root UID on a host.

On unprivileged containers, the root UID within the container is mapped to an unprivileged UID on the host, which makes it more difficult for a hack inside the container to lead to consequences on the host system.  In other words, if an attacker manages to escape the container, they should find themselves with limited or no rights on the host.

The Arch ,  and  kernel packages currently provide out-of-the-box support for unprivileged containers. With the  package, unprivileged containers are only available for the system  administrator; hence additional kernel configuration changes are required to enable user namespaces for normal users there.

This article contains information for users to run either type of container, but additional steps may be required in order to use unprivileged containers.

To illustrate the power of UID mapping, consider the output below from a running, unprivileged container.  Therein, we see the containerized processes owned by the containerized root user in the output of :

On the host, however, those containerized root processes are actually shown to be running as the mapped user (ID>99999), rather than the host's actual root user:

## Setup
## Required software
Installing  and  will allow the host system to run privileged lxcs.

## Enable support to run unprivileged containers (optional)
Modify the configuration to contain the following lines:

In other words, map a range of 65536 consecutive uids, starting from container-side uid 0, which shall be uid 100000 from the host’s point of view, up to and including container-side uid 65535, which the host will know as uid 165535. Apply that same mapping to gids.

Create or edit both  at  and  at  to contain the mapping to the containerized uid/gid pairs for each user who shall be able to run the containers.  The example below is simply for the root user (and systemd system unit):

In addition, running unprivileged containers as an unprivileged user only works if you delegate a cgroup in advance (the cgroup2 delegation model enforces this restriction, not liblxc). Use the following systemd command to delegate the cgroup (per LXC - Getting started: Creating unprivileged containers as a user):

 $ systemd-run --unit=myshell --user --scope -p "Delegate=yes" lxc-start container_name

This works similarly for other lxc commands.

Alternatively, delegate unprivileged cgroups by creating a systemd unit (per Rootless Containers: Enabling CPU, CPUSET, and I/O delegation):

## Unprivileged containers on linux-hardened and custom kernels
Users wishing to run unprivileged containers on  or their custom kernel need to complete several additional setup steps.

Firstly, a kernel is required that has support for user namespaces (a kernel with ). All Arch Linux kernels have support for . However, due to more general security concerns, the  kernel does ship with user namespaces enabled only for the root user. There are two options to create unprivileged containers there:

* Start the unprivileged containers only as root. Also give the sysctl setting  a positive value to suit your environment if its current value is  (this fixes  errors seen in ).
* Under  &  you may need to set  &  to use a range of . You may also need to start your first container as privileged. This fixes error
* Enable the sysctl setting  to allow normal users to run unprivileged containers. This can be done for the current session by running  as root and can be made permanent with .

## Host network configuration
LXC supports different virtual network types and devices (see ). A bridge device on the host is required for most types of virtual networking, which is illustrated in this section.

There are several main setups to consider:

# A host bridge
# A NAT bridge

The host bridge requires the host's network manager to manage a shared bridge interface.  The host and any lxc will be assigned an IP address in the same network (for example 192.168.1.x).  This might be more simplistic in cases where the goal is to containerize some network-exposed service like a webserver, or VPN server.  The user can think of the lxc as just another PC on the physical LAN, and forward the needed ports in the router accordingly.  The added simplicity can also be thought of as an added threat vector, again, if WAN traffic is being forwarded to the lxc, having it running on a separate range presents a smaller threat surface.

The NAT bridge does not require the host's network manager to manage the bridge.   ships with  which creates a NAT bridge called . The NAT bridge is a standalone bridge with a private network that is not bridged to the host's ethernet device or to a physical network. It exists as a private subnet in the host.

## Using lxc-net "Virtual NAT Router"
## Enable lxc-net.service
Now you can start the  and among other things the default Bridge  should appear in

 $ ip a

## Advanced Setup
One can override some  defaults by creating  file or editing  file using the following template:

Optionally, create a configuration file to manually define the IP address of any containers:

## Firewall considerations
Depending on which firewall the host machine is running, it might be necessary to allow inbound packets from  to the host, and outbound packets from  to traverse through the host to other networks.  To test this, try to bring up a container configured to use DHCP for its IP assignment and see if  is able to assign an IP address to the container (check with .  If no IP is assigned, the host's policies will need to be adjusted.

Users of  can simply run the following two lines to enable this:

 # ufw allow in on lxcbr0
 # ufw route allow in on lxcbr0

Alternatively, users of  can modify  (and reload it with ; check if the config syntax is correct with ) to allow the container to have internet access (replace  with the device on your system that has internet access; list existing devices with ):

{{hc|/etc/nftables.conf|
table inet filter {
  chain input {
    ...
    iifname "lxcbr0" accept comment "Allow lxc containers"

    pkttype host limit rate 5/second counter reject with icmpx type admin-prohibited
    counter
  }
  chain forward {
    ...
    iifname "lxcbr0" oifname "eth0" accept comment "Allow forwarding from lxcbr0 to eth0"
    iifname "eth0" oifname "lxcbr0" accept comment "Allow forwarding from eth0 to lxcbr0"
  }
}
}}

Additionally, since the container is running on the 10.0.3.x subnet, external access to services such as ssh, httpd, etc. will need to be actively forwarded to the lxc.  In principle, the firewall on the host needs to forward incoming traffic on the expected port on the container.

## Example iptables rule
The goal of this rule is to allow ssh traffic to the lxc:

 # iptables -t nat -A PREROUTING -i eth0 -p tcp --dport 2221 -j DNAT --to-destination 10.0.3.100:22

This rule forwards tcp traffic originating on port 2221 to the IP address of the lxc on port 22.

To ssh into the container from another PC on the LAN, one needs to ssh on port 2221 to the host.  The host will then forward that traffic to the container.

 $ ssh -p 2221 host.lan

## Example ufw rule
If using , append the following at the bottom of  to make this persistent:

## Running containers as non-root user
To create and start containers as a non-root user, extra configuration must be applied.

According to , the entry per line is:

Configure the file with the user needing to create containers. The bridge will be the same as defined in .

A copy of the  is needed in the non-root user's home directory, e.g.  (create the directory if needed).

Running containers as a non-root user requires  permissions on . Make that change with chmod before starting a container.

## Container creation
Containers are built using  command.  With the release of lxc-3.0.0-1, upstream has deprecated locally stored templates.

To create an Arch container:

 # lxc-create --name playtime --template download -- --dist archlinux --release current --arch amd64

To create a container by interactively choosing from a list of supported distributions:

 # lxc-create -n playtime -t download

To see a list of download template options:

 # lxc-create -t download --help

## Container configuration
The examples below can be used with privileged and unprivileged containers alike.  Note that for unprivileged containers, additional lines will be present by default, which are not shown in the examples, including the  and the  values optionally defined in the #Enable support to run unprivileged containers (optional) section.

## Basic configuration with networking
Configurations specific to a container, including system resources to be virtualized/isolated when a process is using the container, are defined in . Read  for the syntax and possible options of the configuration file.

A basic configuration file generated when creating containers using templates. Read  for more information.

By default, the creation process will make a minimum setup without networking support.  Below is an example configuration with networking supplied by :

## Mounts within the container
One can create a host volume outside the container's  and then mount that volume inside the container. This can be advantageous, for example if the same architecture is being containerized and one wants to share pacman packages between the host and container. Another example could be shared directories. Read  for more information. The general syntax is:

 lxc.mount.entry = /var/cache/pacman/pkg var/cache/pacman/pkg none bind 0 0

## Xorg program considerations (optional)
In order to run programs on the host's display, some bind mounts need to be defined so that the containerized programs can access the host's resources.

If still experiencing a permission denied error in the LXC guest, call  in the host to allow the guest to connect to the host's display server. Take note of the security concerns of opening up the display server by doing this.
In addition, add the following line before the above bind mount lines.

## VPN considerations
To run a containerized OpenVPN or WireGuard, see Linux Containers/Using VPNs.

## Managing containers
## Basic usage
To list all installed LXC containers:

 # lxc-ls -f

Systemd can be used to start and to stop LXCs via . Enable  to have it start when the host system boots.

Users can also start/stop LXCs without systemd.
Start a container:

 # lxc-start -n CONTAINER_NAME

Stop a container:

 # lxc-stop -n CONTAINER_NAME

To login into a container:

 # lxc-console -n CONTAINER_NAME

Once logged, treat the container like any other linux system, set the root password, create users, install packages, etc.

To attach to a container:

 # lxc-attach -n CONTAINER_NAME --clear-env

That works nearly the same as lxc-console, but it causes starts with a root prompt inside the container, bypassing login. Without the  flag, the host will pass its own environment variables into the container (including , so some commands will not work when the containers are based on another distribution).

## Advanced usage
## LXC clones
Users with a need to run multiple containers can simplify administrative overhead (user management, system updates, etc.) by using snapshots.  The strategy is to setup and keep up-to-date a single base container, then, as needed, clone (snapshot) it.  The power in this strategy is that the disk space and system overhead are truly minimized since the snapshots use an overlayfs mount to only write out to disk, only the differences in data.  The base system is read-only but changes to it in the snapshots are allowed via the overlayfs.

For example, setup a container as outlined above.  We will call it "base" for the purposes of this guide.  Now create 2 snapshots of "base" which we will call "snap1" and "snap2" with these commands:

 # lxc-copy -n base -N snap1 -B overlayfs -s
 # lxc-copy -n base -N snap2 -B overlayfs -s

The snapshots can be started/stopped like any other container.  Users can optionally destroy the snapshots and all new data therein with the following command.  Note that the underlying "base" lxc is untouched:

 # lxc-destroy -n snap1 -f

Systemd units and wrapper scripts to manage snapshots for pi-hole and OpenVPN are available to automate the process in lxc-service-snapshots.

## Converting a privileged container to an unprivileged container
Once the system has been configured to use unprivileged containers (see #Enable support to run unprivileged containers (optional)), it is possible to make an existing privileged container run as unprivileged by editing the configuration file.

As an alternative to the  option, there is also a utility  in  which changes UIDs and GIDs in the container's rootfs.

Invoke the utility to convert over like so:

 # uidmapshift -b /var/lib/lxc/foo 0 100000 65536

Additional options are available simply by calling  without any arguments.

## Running Xorg programs
Either attach to or SSH into the target container and prefix the call to the program with the DISPLAY ID of the host's X session.  For most simple setups, the display is always 0.

An example of running Firefox from the container in the host's display:

 $ DISPLAY=:0 firefox

Alternatively, to avoid directly attaching to or connecting to the container, the following can be used on the host to automate the process:

 # lxc-attach -n playtime --clear-env -- sudo -u YOURUSER env DISPLAY=:0 firefox

## Tips and tricks
## Ping not working in an unprivileged container
In unprivileged containers, ping is likely to not work without an extra config step. Example error:

To fix this in container foo, on the host:

 # lxc-attach -n foo -- chmod u+s /usr/bin/ping

## Troubleshooting
## Root login fails
If presented with following error upon trying to login using lxc-console:

 login: root
 Login incorrect

And the container's journal shows:

 pam_securetty(login:auth): access denied: tty 'pts/0' is not secure !

Delete and  on the container file system. Optionally add them to NoExtract in  to prevent them from getting reinstalled. See  for details.

Alternatively, create a new user in lxc-attach and use it for logging in to the system, then switch to root.

## No network-connection with veth in container config
If you cannot access your LAN or WAN with a networking interface configured as veth and setup through .
If the virtual interface gets the ip assigned and should be connected to the network correctly.

You may disable all the relevant static ip formulas and try setting the ip through the booted container-os like you would normaly do.

Example

 ...
 lxc.net.0.type = veth
 lxc.net.0.name = veth0
 lxc.net.0.flags = up
 lxc.net.0.link =
 ...

And then assign the IP through a preferred method inside the container, see also Network configuration#Network management.

## Error: unknown command
The error may happen when a basic command (ls, cat, etc.) on an attached container is typed hen a different Linux distribution is containerized relative to the host system (e.g. Debian container in Arch Linux host system). Upon attaching, use the argument :

 # lxc-attach -n container_name --clear-env

## Error: Failed at step KEYRING spawning
Services in an unprivileged container may fail with the following message

 Failed to change ownership of session keyring: Permission denied
 Failed to set up kernel keyring: Permission denied
 Failed at step KEYRING spawning ....: Permission denied

Create the following seccomp ruleset:

Then add the following line to the container configuration after :

## Known issues
## lxc-execute fails due to missing lxc.init.static
 fails with the error message . See  for details.

Starting containers using  works fine.
