# Podman

Podman is an alternative to Docker, providing a similar interface. It supports rootless containers and a shim service for docker-compose.

## Installation
Install the  package.

Podman depends on the  package as the default network backend for rootful containers (see ). Netavark depends on  for name resolution among containers in the same network. Support for the alternative network backend (CNI, ) is deprecated.

If you want to replace Docker, one can install  to mimic the docker binary along with man pages.

Unlike Docker, Podman does not require a daemon, but there is one providing an API for services like cockpit via .

For advanced usage related to building containers see  which is based on Buildah.

## Configuration
Configuration files for configuring how containers behave are located at . You must copy necessary files to  before editing. To configure the network bridge interface used by Podman, see .

## Registries
By default, no container image registries are configured in Arch Linux This means unqualified searches like  will not work. To make Podman behave like Docker, configure :

## User namespace mode
By default, processes in Podman containers run within the same user namespace as the caller, i.e. containers are not isolated by the  feature. This is the behavior of , see .

The  flag automatically creates a unique user namespace for the container using an empty range of UIDs and GIDs:

* For containers started by root, the  flag requires the user name  to be specified in the  and  files with an unused range of IDs. For example: .
* For containers started by other users, the user's range from the  and  files will be used. See #Rootless Podman for the necessary configuration.

There are other valid values for the  flag, see  for details. The user namespace mode can also be configured in the  file on a per-system or per-user basis.

## Rootless Podman
By default, only  is allowed to run containers (or namespaces in kernelspeak). Running rootless Podman improves security as an attacker will not have root privileges over your system, and also allows multiple unprivileged users to run containers on the same machine. See also  and the official [https://github.com/containers/podman/blob/main/docs/tutorials/rootless_tutorial.md rootless tutorial (may be outdated).

## Enable kernel.unprivileged_userns_clone
First, check the value of  by running:

 $ sysctl kernel.unprivileged_userns_clone

If it is currently set to , enable it by setting  via sysctl or a kernel parameter.

## Set subuid and subgid
In order for users to run rootless Podman, a  and  configuration entry must exist for each user that wants to use it. New users created using  have these entries by default.

## Migration for users created prior to shadow 4.11.1-3
Users created prior to  4.11.1-3 do not have entries in  and  by default. An entry can be created for them using the  command or by manually modifying the files.

The following command enables the  user and group to run Podman containers (or other types of containers in that case). It allocates a given range of UIDs and GIDs to the given user and group.

 # usermod --add-subuids 100000-165535 --add-subgids 100000-165535 username

The above range for the user  may already be taken by another user as it defines the default range for the first user on the system. If in doubt, first consult the  and  files to find the already reserved ranges.

## Workaround for users managed by homed
Homed does not seem to allocate gid and uid entries to its users. To do this manually, run:

 # usermod --add-subuids 524288-589823 --add-subgids 524288-589823 username

Or simply edit the following configuration files as root and add these lines

This allocates uid and gid range  to the  user. If these ranges are already taken by other users, you need to shift/adjust the ranges accordingly.

You might need to reboot to reflect the changes.

## Propagate changes to subuid and subgid
Rootless Podman uses a pause process to keep the unprivileged namespaces alive. This prevents any change to the  and  files from being propagated to the rootless containers while the pause process is running. For these changes to be propagated it is necessary to run:

 $ podman system migrate

After this, the user/group specified in the above files is able to start and run Podman containers.

## Enable native rootless overlays
Previously, it was necessary to use the  package for FUSE overlay mounts in a rootless environment. However, modern versions of Podman and Linux kernel support native rootless overlays, which yields better performance.

To migrate from , run the following command (it will unfortunately delete all pulled images):

 $ podman system reset

Also make sure that Podman uses the  driver and that the  parameter is not defined in . Follow the instructions in Docker#Enable native overlay diff engine.

To verify that native rootless overlays are enabled, run

 $ podman info | grep -i overlay

It should show  and .

## Networking
Podman depends on , which provides pasta as the default rootless network backend.

An alternative rootless network backend is , which was the default up to Podman 5.

A major difference between the two is outlined in Podman 5.0 breaking changes in detail:

:Pasta by default performs no Network Address Translation (NAT) and copies the ip addresses from your main interface into the container namespace.

The consequences of this change are explained in upstream's Shortcomings of Rootless Podman:

:Since pasta copies the IP address of the main interface, connections to that IP from containers do not work. This means that unless you have more than one interface, inter-container connections cannot be made without explicitly passing a pasta network configuration, either in  or at runtime.

An example to mimic slirp4netns behavior is given in the "Podman 5.0 breaking changes" blog post:

Also, the default rootless networking tool can be selected in  under the  section with , which can be set to  or . So, if you run into bugs, you can always revert to slirp4netns like so (provided it is installed):

## Dual-stack IPv4/IPv6
The default network created by Podman only supports IPv4 networking You can create a new network with support for dual-stack IPv4/IPv6 support using:

 $ podman network create --ipv6 podman_dual_stack

To change the default rootless network to this, set :

## Storage
The configuration for how and where container images and instances are stored takes place in .

The default  driver is well tested and supports reflink copies [https://github.com/containers/podman/issues/6563#issuecomment-659085291 on filesystems that support it (Btrfs, XFS, ZFS...) For more information on the available alternatives and other configuration options, see .

## Foreign architectures
Podman is able to run images built for different CPU architecture than the host using the Wikipedia:binfmt_misc system.

To enable it, install  and .

systemd comes with the  service which should enable new rules.

Verify that binfmt rules have been added:

Podman should now be able to run foreign architecture images. Most commands use the foreign architecture when  option is passed.

Example:

## Docker Compose
Podman has a compose subcommand which is a thin wrapper around a compose provider, either  or . If both are installed, docker-compose takes precedence. You can override this using the  environment variable.

If you want to use docker-compose, you will need to enable the  user unit and set docker socket environment variable for that user:

 $ export DOCKER_HOST=unix://$XDG_RUNTIME_DIR/podman/podman.sock

This is not required when using podman-compose as it will use podman directly.

## NVIDIA GPUs
[https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/install-guide.html#podman NVIDIA Container Toolkit provides container runtime for NVIDIA GPUs. Install the  package. It contains a pacman hook that generates the CDI specification for your GPU and saves it in .

Test the setup:

 $ podman run --rm --gpus all archlinux nvidia-smi -L

## Containers with restart policy
To automatically start containers with a restart policy, enable .

## Runtimes
Podman allows you to use different container runtimes that should each more or less provide the same features and guarantees.

* : The former default runtime.
* : The new default runtime. Generally preferable since it is faster than .
* : Part of . A special runtime that uses KVM-backed krunvm-based micro VMs to execute the container. Compared to a full VM, these micro VMs start in milliseconds and use a different kernel. This should provide better security compared to regular containers that run with the host kernel.
* : Memory-safe runtime written in Rust.

To start a single command in an alternative runtime, you can use  like so:

 $ podman run --rm --runtime=krun archlinux uname -a

To make this change permanent, you can put it into :

## Quadlet
Quadlet allows to manage Podman containers with systemd.

For rootless Podman, place Quadlet files under one of following directories:

*  or
*  for the user matching
*  for all users

For Podman with root permissions, the directory is .

Podman will read Quadlet files with extensions .container, .volume, .network, .kube, .image, .build and .pod. A corresponding .service file will be generated using . The Quadlet files are read during boot or manually by running a daemon-reload.

Quadlet files can also be generated from Podman commands using .

For example, here is a command that will run Syncthing container from LinuxServer.io:

 $ podman run \
     --rm \
     --replace \
     --label io.containers.autoupdate=registry \
     --name syncthing \
     --hostname=syncthing \
     --uidmap 1000:0:1 \
     --uidmap 0:1:1000 \
     --uidmap 1001:1001:64536 \
     --env PUID=1000 \
     --env PGID=1000 \
     --env TZ=Etc/UTC \
     --publish 127.0.0.1:8384:8384/tcp \
     --publish 22000:22000/tcp \
     --volume /path/to/syncthing/config:/config \
     --volume /path/to/data1:/data1 \
     lscr.io/linuxserver/syncthing:latest

To manage it as a systemd service, create the following Quadlet file:

We can validate the Quadlet file via

Then, daemon-reload and start . See systemd/User#Automatic start-up of systemd user instances to start rootless containers without any open sessions.

If you want to start containers at boot, make sure that your network manager supports and is configured for running services after the network is up.

Valid options for the  section are listed under .  can be used to add other Podman arguments that do not have corresponding file options.

See  for more examples including , ,  and  units.

## Images
## Arch Linux
The following command pulls the Arch Linux x86_64 image from Docker Hub.

 # podman pull docker.io/archlinux

See the Docker Hub page for a full list of available tags, including versions with and without build tools.

See also README.md.

## Alpine Linux
Alpine Linux is a popular choice for small container images, especially for software compiled as static binaries. The following command pulls the latest Alpine Linux image from Docker Hub:

 # podman pull docker.io/alpine

Alpine Linux uses the musl libc implementation instead of the glibc libc implementation used by most Linux distributions. Because Arch Linux uses glibc, there are a number of functional differences between an Arch Linux host and an Alpine Linux container that can impact the performance and correctness of software. A list of these differences is documented in https://wiki.musl-libc.org/functional-differences-from-glibc.html.

Note that dynamically linked software built on Arch Linux (or any other system using glibc) may have bugs and performance problems when run on Alpine Linux (or any other system using a different libc). See [https://superuser.com/questions/1219609/why-is-the-alpine-docker-image-over-50-slower-than-the-ubuntu-image and for examples.

## CentOS Stream
The following command pulls the latest [https://quay.io/repository/centos/centos CentOS Stream image from Quay:

 # podman pull quay.io/centos/centos

See the Quay page for a full list of available tags for each CentOS release.

## Debian
The following command pulls the latest Debian image from Docker Hub:

 # podman pull docker.io/debian

See the Docker Hub page for a full list of available tags, including both standard and slim versions for each Debian release.

## Troubleshooting
## Add pause to process
 WARNFailed to add pause process to systemd sandbox cgroup: Process org.freedesktop.systemd1 exited with status 1

Can be solved using: https://github.com/containers/crun/issues/704

 # echo +cpu +cpuset +io +memory +pids > /sys/fs/cgroup/cgroup.subtree_control

## Containers terminate on shell logout
After logging out from machine, Podman containers are stopped for some users. To prevent that, enable lingering for users running containers.

You can also create user systemd unit as described in .

## Error on commit in rootless mode
 Error committing the finished image: error adding layer with blob "sha256:02823fca9b5444c196f1f406aa235213254af9909fca270f462e32793e2260d8": Error processing tar file(exit status 1) permitted operation

Check that the storage driver is overlay in the storage configuration.

## Error when creating a container with bridge network in rootless mode
If you are using AppArmor you might end up with problems when creating container using a bridge network with the  plugin enabled:

This can be solved by adding the following lines to :

 owner /run/user/[0-9*/containers/cni/dnsname/*/dnsmasq.conf r,
 owner /run/user/r,
 owner /run/user/[0-9*/containers/cni/dnsname/*/pidfile rw,

And then reloading the AppArmor profile:

 # apparmor_parser -R /etc/apparmor.d/usr.sbin.dnsmasq
 # apparmor_parser /etc/apparmor.d/usr.sbin.dnsmasq

## No image found
By default, the registry list is not populated as the files in the package come from upstream. This means that by default, trying to pull any image without specifying the registry will result in an error similar to the following:

 Error: short-name "archlinux" did not resolve to an alias and no unqualified-search registries are defined in "/etc/containers/registries.conf"

A starting configuration could be the following:

This is equivalent to the default docker configuration.

A less convenient alternative, but having a higher compatibility with systems without configured shortnames, use the full registry path in the  or .

## Permission denied: OCI permission denied
Can be solved: BBS#253966

 $ env DBUS_SESSION_BUS_ADDRESS= podman ...
 $ env DBUS_SESSION_BUS_ADDRESS= podman-compose ...

## Pushing images to Docker Hub: access denied/authentication required
When using  to push container images to Docker Hub, the following errors could occur:  or . The following hints can help to fix potential issues:

* Tag the local image:
* Push the tagged image:
* Login to docker.io, the Docker Hub repository and Docker Hub Registry server:
:
* Logout from all registries before the login, e.g.,
* Add  as collaborator in the Docker Hub Collaborators tab of the repository

## WARN"/" is not a shared mount, this could cause issues or missing mounts with rootless containers
Buildah/Podman running as rootless expects the bind mount to be shared, check if it is set to private:

In this case see  and set temporarily the mount as shared with:

 # mount --make-shared /

To set it permanently edit /etc/fstab and add the shared option to the desired mount and reboot. It will result in a entry like:

## Networking issues inside containers
## IP networking
Podman containers are by default bridged with the host through their own virtual network interfaces.

For example, inside a container, virtual interface  has IP 10.89.0.3 (IPs might be different on your system!):

On the host, packets from the container exit on the host side from another virtual interface, here named  as if routed via IP 10.89.0.1:

Despite being virtual IP addresses, packets are still routed through the kernel's packet filtering system and can therefore be blocked by iptables/nftables rules. In particular, default  policy in  or  iptables filter chains and/or running firewalls (ufw, firewalld) can affect containers in some cases. Check your configuration (for example with  or ) if you think this may be the case.

After a change in , note that created networks (from the  section) may not be destroyed when using  to destroy an environment. Make sure (using  and  if necessary) that they are if that is your intention.

## DNS and name resolution
Name resolution is handled by subsystems of Podman (for example ), which provide both external DNS (usually through the host's DNS resolver) and container name resolution (e.g.  talking to ).

In the example above, containers are configured automatically by Podman via  to ask a DNS resolver running on port 53 on the host-side of the pipe:

Check that you don't have another DNS resolver running on the host on port 53 (for example systemd-resolved or Unbound), as it may interfere with Podman name resolution. If that is the case, you can change the port used by Podman on the host to any other available port, and Podman should automatically forward container requests from containers to the correct port on the host:

## kernel does not support overlay fs: 'overlay' is not supported over
Reboot your system, as explained in General troubleshooting#Cannot use some peripherals after kernel upgrade.
