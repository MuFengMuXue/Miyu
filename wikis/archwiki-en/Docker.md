# Docker

Docker is a utility to pack, ship and run any application as a lightweight container.

## Installation
To pull Docker images and run Docker containers, you need the Docker Engine. The Docker Engine includes a daemon to manage the containers, as well as the  CLI frontend.

Install the  package.

Next enable/start  or . Note that  starts the service on boot, whereas  starts Docker on first usage which can decrease boot times. Then verify Docker's status:

 # docker info

Note that starting the docker service may fail if you have an active VPN connection due to IP conflicts between the VPN and Docker's bridge and overlay networks. If this is the case, try disconnecting the VPN before starting the docker service. You may reconnect the VPN immediately afterwards. You can also try to deconflict the networks (see solutions or [https://github.com/docker/compose/issues/4336#issuecomment-457326123).

Next, verify that you can run containers. The following command downloads the latest Arch Linux image and uses it to run a Hello World program within a container:

 # docker run -it --rm archlinux bash -c "echo hello world"

To remove the downloaded  Docker image, see #Remove Docker and images.

If you want to be able to run the  CLI command as a non-root user, add your user to the  user group, re-login and restart .

If you plan to build container images using Docker, install  to use the current builder instead of the deprecated legacy builder.

## Docker Compose
Docker Compose is an alternate CLI frontend for the Docker Engine, which specifies properties of containers using a  YAML file rather than, for example, a script with  options. This is useful for setting up reoccuring services that are used often and/or have complex configurations. To use it, install .

## Docker Desktop
Docker Desktop is a proprietary desktop application that runs the Docker Engine inside a Linux virtual machine. Additional features such as a Kubernetes cluster and a vulnerability scanner are included. This application is useful for software development teams who develop Docker containers using macOS and Windows. The Linux port of the application is relatively new, and complements Docker's CLI frontends An experimental package for Arch is provided directly by Docker; see [https://docs.docker.com/desktop/linux/install/archlinux/ the manual for more information. Unfortunately, it contains files which conflict with the  and  packages, so you will first need to remove them if installed. Alternatively, you can install the  package.

Also, to run Docker Desktop you will need to ensure the Linux system requirements, including  virtualization support via KVM. To see a tray icon under Gnome,  will be needed.

Finally, file sharing support requires mapping user and group ids via  and . See the Docker Desktop For Linux File Sharing instructions for more details.

Furthermore, expect degraded performance and higher CPU usage when using Docker Desktop on Linux.

By default, Docker Desktop enables a user-level systemd service that starts the application automatically on boot. Disabling the "Autostart" setting in the Docker Desktop dashboard does not prevent this service from starting. To disable auto-start, disable the  user unit.

## Front-ends
*
*
*
*
*
*
*

## Usage
Docker consists of multiple parts:

* The Docker daemon (sometimes also called the Docker Engine), which is a process which runs as . It serves the Docker API and manages Docker containers.
* The  CLI command, which allows users to interact with the Docker API via the command line and control the Docker daemon.
* Docker containers, which are namespaced processes that are started and managed by the Docker daemon as requested through the Docker API.

Typically, users use Docker by running  CLI commands, which in turn request the Docker daemon to perform actions which in turn result in management of Docker containers. Understanding the relationship between the client (), server () and containers is important to successfully administering Docker.

Note that if the Docker daemon stops or restarts, all currently running Docker containers are also stopped or restarted.

Also note that it is possible to send requests to the Docker API and control the Docker daemon without the use of the  CLI command. See the Docker API developer documentation for more information.

See the Docker Getting Started guide for more usage documentation.

## Configuration
The Docker daemon can be configured either through a configuration file at  or by adding command line flags to the  systemd unit. According to the Docker official documentation, the configuration file approach is preferred. If you wish to use the command line flags instead, use systemd drop-in files to override the  directive in .

For more information about options in  see dockerd documentation.

## Storage driver
The storage driver controls how images and containers are stored and managed on your Docker host. The default  driver has good performance for most use cases.

Users of btrfs or ZFS may use the  or  drivers, each of which take advantage of the unique features of these filesystems. See the btrfs driver and zfs driver documentation for more information and step-by-step instructions.

## Daemon socket
By default, the Docker daemon serves the Docker API using a Unix socket at . This is an appropriate option for most use cases.

It is possible to configure the Daemon to additionally listen on a TCP socket, which can allow remote Docker API access from other computers. This can be useful for allowing  commands on a host machine to access the Docker daemon on a Linux virtual machine, such as an Arch virtual machine on a Windows or macOS system.

Note that the default  file sets the  flag by default, and Docker will not start if an option is present in both the flags and  file. Therefore, the simplest way to change the socket settings is with a drop-in file, such as the following which adds a TCP socket on port 2376:

Reload the systemd daemon and restart  to apply changes.

## HTTP Proxies
There are two parts to configuring Docker to use an HTTP proxy: Configuring the Docker daemon and configuring Docker containers.

## Docker daemon proxy configuration
See [https://docs.docker.com/config/daemon/systemd/#httphttps-proxy Docker documentation on configuring Docker daemon to use HTTP proxies.

## Docker container proxy configuration
See Docker documentation on configuring proxies for information on how to automatically configure proxies for all containers created using the  CLI.

## Configuring DNS
See Docker's DNS documentation for the documented behavior of DNS within Docker containers and information on customizing DNS configuration. In most cases, the resolvers configured on the host are also configured in the container.

Most DNS resolvers hosted on  are not supported due to conflicts between the container and host network namespaces. Such resolvers are removed from the container's /etc/resolv.conf. If this would result in an empty , Google DNS is used instead.

Additionally, a special case is handled if  is the only configured nameserver. In this case, Docker assumes the resolver is systemd-resolved and uses the upstream DNS resolvers from .

If you are using a service such as dnsmasq to provide a local resolver, consider adding a virtual interface with a link local IP address in the  block for dnsmasq to bind to instead of  to avoid the network namespace conflict.

## Images location
Since version 29 (2025-11), the default image store has been changed to containerd for new installs.

When using the containerd image store, image contents and container snapshots are stored in  by default. For old installs that were upgraded, Docker images remain located in .

To verify which image store is in use:

 docker info -f ''

For the containerd image store, the output will be:

 driver-type io.containerd.snapshotter.v1

The image storage location can be changed, e.g. if you wish to use a dedicated partition or disk for your images, by configuring the data root location.

The first step before changing anything is to stop , which will also stop all currently running containers and unmount any running images.

Then edit the appropriate configuration file depending on the image store driver:

* if using the containerd image store:

* if using the classic Docker overlay image store:

{{hc|/etc/docker/daemon.json|2=
{
  "data-root": "/path/to/docker-data"
}
}}

Then move the contents from either  or  to the target destination.

Finally, start  to apply the changes.

## Insecure registries
If you decide to use a self signed certificate for your private registries, Docker will refuse to use it until you declare that you trust it. For example, to allow images from a registry hosted at , configure  in the  file:

{{hc|/etc/docker/daemon.json|2=
{
  "insecure-registries": [
    "my.registry.example.com:8443"
  ]
}
}}

Restart  to apply changes.

## IPv6
In order to enable IPv6 support in Docker, you will need to do a few things. See and [https://github.com/moby/moby/issues/36954 for details.

Firstly, enable the  setting in  and set a specific IPv6 subnet. In this case, we will use the private  subnet. Make sure to use a subnet at least 80 bits as this allows a container's IPv6 to end with the container's MAC address which allows you to mitigate NDP neighbor cache invalidation issues.

{{hc|/etc/docker/daemon.json|
{
  "ipv6": true,
  "fixed-cidr-v6": "fd00::/80"
}
}}

Restart  to apply changes.

Finally, to let containers access the host network, you need to resolve routing issues arising from the usage of a private IPv6 subnet. Add the IPv6 NAT in order to actually get some traffic:

 # ip6tables -t nat -A POSTROUTING -s fd00::/80 ! -o docker0 -j MASQUERADE

Now Docker should be properly IPv6 enabled. To test it, you can run:

 # docker run curlimages/curl curl -v -6 archlinux.org

If you use firewalld, you can add the rule like this:

 # firewall-cmd --zone=public --add-rich-rule='rule family="ipv6" destination not address="fd00::1/80" source address="fd00::/80" masquerade'

If you use ufw, you need to first enable ipv6 forwarding following Uncomplicated Firewall#Forward policy. Next you need to edit  and uncomment the following lines

Then you can add the iptables rule:

 # ip6tables -t nat -A POSTROUTING -s fd00::/80 ! -o docker0 -j MASQUERADE

It should be noted that, for docker containers created with docker-compose, you may need to set  in the  part for the corresponding network. Besides, you may need to configure the IPv6 subnet. See for details.

## User namespace isolation
By default, processes in Docker containers run within the same user namespace as the main  daemon, i.e. containers are not isolated by the  feature. This allows the process within the container to access configured resources on the host according to Users and groups#Permissions and ownership. This maximizes compatibility, but poses a security risk if a container privilege escalation or breakout vulnerability is discovered that allows the container to access unintended resources on the host. (One such vulnerability was [https://seclists.org/oss-sec/2019/q1/119 published and patched in February 2019.)

The impact of such a vulnerability can be reduced by enabling user namespace isolation. This runs each container in a separate user namespace and maps the UIDs and GIDs inside that user namespace to a different (typically unprivileged) UID/GID range on the host.

Configure  in .  is a special value that will automatically create a user and group named  for use with remapping.

{{hc|/etc/docker/daemon.json|2=
{
  "userns-remap": "default"
}
}}

Configure  and  with a username/group name, starting UID/GID and UID/GID range size to allocate  to the remap user and group. This example allocates a range of 65536 UIDs and GIDs starting at 165536 to the  user and group.

Restart  to apply changes.

After applying this change, all containers will run in an isolated user namespace by default. The remapping may be partially disabled on specific containers passing the  flag to the  command. See for details.

## Rootless Docker daemon
To run the Docker daemon as a regular user, install .

Configure  and  for the user running the daemon by allocating a subordinate UID/GID range of 65,536, for example:

Enable either  or  as a user unit.

Finally, configure the Docker client.

Create a persistent Docker context:

Alternatively, set the  environment variable to .

## Enable native overlay diff engine
First check if is it already enabled: run  and check that  is .

By default, Docker cannot use the native overlay diff engine on Arch Linux, which makes building Docker images slow. If you frequently build images, configure the native diff engine as described in [https://mikeshade.com/posts/docker-native-overlay-diff/:

Then stop , reload the  module as follows:

 # modprobe -r overlay
 # modprobe overlay

You can then start  again.

## Images
## Arch Linux
The following command pulls the archlinux x86_64 image. This is a stripped down version of Arch core without network, etc.

 # docker pull archlinux

See also README.md.

For a full Arch base, clone the repository from above and build your own image.

 $ git clone https://gitlab.archlinux.org/archlinux/archlinux-docker.git

Make sure that the ,  and  packages are installed.

To build the base image:

 $ make image-base

## Alpine Linux
Alpine Linux is a popular choice for small container images, especially for software compiled as static binaries. The following command pulls the latest Alpine Linux image:

 # docker pull alpine

Alpine Linux uses the musl libc implementation instead of the glibc libc implementation used by most Linux distributions. Because Arch Linux uses glibc, there are a number of functional differences between an Arch Linux host and an Alpine Linux container that can impact the performance and correctness of software. A list of these differences is documented here.

Note that dynamically linked software built on Arch Linux (or any other system using glibc) may have bugs and performance problems when run on Alpine Linux (or any other system using a different libc). See [https://superuser.com/questions/1219609/why-is-the-alpine-docker-image-over-50-slower-than-the-ubuntu-image and for examples.

## Debian
The following command pulls the latest [https://hub.docker.com/_/debian debian image:

 # docker pull debian

See the Docker Hub page for a full list of available tags, including both standard and slim versions for each Debian release.

## Distroless
Google maintains distroless images which are minimal images without OS components such as package managers or shells, resulting in very small images for packaging software.

See the GitHub README for a list of images and instructions on their use with various programming languages.

## Tips and tricks
## Get the IP address of a running container
To grab the IP address of a running container:

For each running container, the name and corresponding IP address can be listed for use in :

{{bc|#!/usr/bin/env sh
for ID in $(docker ps -q | awk '{print $1}'); do
    IP=$(docker inspect --format="" "$ID")
    NAME=$(docker ps | grep "$ID" | awk '{print $NF}')
    printf "%s %s\n" "$IP" "$NAME"
done}}

## Run graphical programs inside a container
This section describes the necessary steps to allow graphical programs (including those that rely on OpenGL or Vulkan) to run on the host's X server.

First, the correct drivers, compatible with the host's graphics hardware, need to be installed inside the container. The installation procedure depends on the type of the container, but for containers based on Arch Linux images, refer to OpenGL#Installation and Vulkan#Installation for packages specific to your hardware.

Next, the container must be granted access to the host's X server. In a single-user environment, this can easily be done by running Xhost on the host system, which adds non-network local connections to the access control list:

 $ xhost +local:

Lastly, the following parameters need to be passed to :

*  sets the environment variable  within the container to the host's display;
*  mounts the host's X server sockets inside the container under the same path;
*  gives the container access to Direct Rendering Infrastructure devices on the host.

To confirm that everything is set up correctly, run  from the package , or  from the package  in the container.

## Start Docker Compose projects on boot
First, create a template unit for Docker Compose which is parameterized by the name of the service (see ):

Then, for each service you would like to run, set up a directory with the Compose file and any other required files (such as  files) at . Then, enable/start .

## Using buildx for cross-compiling
The [https://docs.docker.com/build/architecture/#buildx buildx CLI plugin makes use of the new BuildKit building toolkit. Install the  package. The buildx interface supports building multi-platform images, including architectures other than that of the host.

QEMU is required to cross-compile images. To setup the static build of QEMU within Docker, see the usage information for the multiarch/qemu-user-static image. Otherwise, to setup QEMU on the host system for use with Docker, see QEMU#Chrooting into arm/arm64 environment from x86_64. In either case, your system will be configured for user-mode emulation of the guest architecture.

As described in Docker's documentation for multi-platform builds, it's required to use the containerd image store for building multi-platform images. If, for example,  fails with

 ERROR: failed to build: Multi-platform build is not supported for the docker driver.
 Switch to a different driver, or turn on the containerd image store, and try again.

edit

{{hc|/etc/docker/daemon.json|2=
{
  "features": {
    "containerd-snapshotter": true
  }
}
}}

and then restart Docker.

## Run GPU accelerated Docker containers with NVIDIA GPUs
Starting from Docker version 19.03, NVIDIA GPUs are natively supported as Docker devices. NVIDIA Container Toolkit is the recommended way of running containers that leverage NVIDIA GPUs.

Install the  package and restart docker. You can now run containers that make use of NVIDIA GPUs using the  option or by registering the NVIDIA container runtime.

## With the --gpus option (recommended)
 # docker run --rm --gpus all nvidia/cuda:12.1.1-runtime-ubuntu22.04 nvidia-smi

Specify how many GPUs are enabled inside a container:

 # docker run --rm --gpus 2 nvidia/cuda:12.1.1-runtime-ubuntu22.04 nvidia-smi

Specify which GPUs to use:

 # docker run --rm --gpus '"device=1,2"' nvidia/cuda:12.1.1-runtime-ubuntu22.04 nvidia-smi

or

 # docker run --rm --gpus '"device=UUID-ABCDEF,1"' nvidia/cuda:12.1.1-runtime-ubuntu22.04 nvidia-smi

For more information see the documentation and install guide.

If, when using the above commands, you receive an error such as , you can try being more specific in specifying the GPU:

 # docker run --rm --gpus all --device /dev/nvidiactl:/dev/nvidiactl --device /dev/nvidia-uvm:/dev/nvidia-uvm --device /dev/nvidia0:/dev/nvidia0 nvidia/cuda:12.1.1-runtime-ubuntu22.04 nvidia-smi

Specify a capability (graphics, compute, ...) for the container (though this is rarely if ever used this way):

 # docker run --rm --gpus all,capabilities=utility nvidia/cuda:12.1.1-runtime-ubuntu22.04 nvidia-smi

## With NVIDIA container runtime
Register the NVIDIA runtime by editing

{{hc|/etc/docker/daemon.json|2=
{
  "runtimes": {
    "nvidia": {
      "path": "/usr/bin/nvidia-container-runtime",
      "runtimeArgs": }
  }
}
}}

and then restart docker.

The runtime can also be registered via a command line option to dockerd:

 # /usr/bin/dockerd --add-runtime=nvidia=/usr/bin/nvidia-container-runtime

Afterwards GPU accelerated containers can be started with

 # docker run --rm --runtime=nvidia nvidia/cuda:12.1.1-runtime-ubuntu22.04 nvidia-smi

See also [https://github.com/NVIDIA/nvidia-container-toolkit/tree/main/cmd/nvidia-container-runtime README.md.

## Arch Linux image with CUDA
You can use the following  to build a custom Arch Linux image with CUDA. It uses the Dockerfile frontend syntax 1.2 to cache pacman packages on the host. The  environment variable must be set on the client before building the Docker image.

## Remove Docker and images
In case you want to remove Docker entirely you can do this by following  the steps below:

Check for running containers:

 # docker ps

List all containers running on the host for deletion:

 # docker ps -a

Stop a running container:

 # docker stop

Killing still running containers:

 # docker kill

Delete containers listed by ID:

 # docker rm

List all Docker images:

 # docker images

Delete images by ID:

 # docker rmi

Delete all images, containers, volumes, and networks that are not associated with a container (dangling):

 # docker system prune

To additionally remove any stopped containers and all unused images (not just dangling ones), add the -a flag to the command:

 # docker system prune -a

Delete all Docker data (purge directory):

 # rm -R /var/lib/docker

## Troubleshooting
## docker0 Bridge gets no IP / no internet access in containers when using systemd-networkd
Docker attempts to enable IP forwarding globally, but by default systemd-networkd overrides the global sysctl setting for each defined network profile. Set  in the network profile. See Internet sharing#Enable packet forwarding for details.

When systemd-networkd tries to manage the network interfaces created by Docker, e.g. when you configured  or  in the  section, this can lead to connectivity issues. The problem should be solved by matching interfaces more specifically, i.e. avoid using  or  or other wildcard that matches an interface managed by Docker. Verify that  reports  in the SETUP column for all networks created by Docker.

## Default number of allowed processes/threads too low
If you run into error messages like

 # e.g. Java
 java.lang.OutOfMemoryError: unable to create new native thread
 # e.g. C, bash, ...
 fork failed: Resource temporarily unavailable

then you might need to adjust the number of processes allowed by systemd. Edit the  with the following snippet:

 TasksMax=infinity

For more background, look for  at . And for  at .

## Error initializing graphdriver: devmapper
If systemctl fails to start docker and provides an error:

 Error starting daemon: error initializing graphdriver: devmapper: Device docker-8:2-915035-pool is not a thin pool

Then, try the following steps to resolve the error. Stop the service, back up  (if desired), remove the contents of , and try to start the service. See https://github.com/moby/moby/issues/21304 for details.

## Failed to create some/path/to/file: No space left on device
If you are getting an error message like this:

 ERROR: Failed to create some/path/to/file: No space left on device

when building or running a Docker image, even though you do have enough disk space available, make sure:

* Tmpfs is disabled or has enough memory allocation. Docker might be trying to write files into  but fails due to restrictions in memory usage and not disk space.
* If you are using XFS, you might want to remove the  mount option from the relevant entries in  (usually where  and/or  reside). Refer to Disk quota for more information, especially if you plan on using and resizing  Docker storage driver.
* XFS quota mount options (, , , etc.) fail during re-mount of the file system. To enable quota for root file system, the mount option must be passed to initramfs as a kernel parameter . Subsequently, it should not be listed among mount options in  for the root () filesystem.

## Docker-machine fails to create virtual machines using the virtualbox driver
In case docker-machine fails to create the VM's using the virtualbox driver, with the following:

 VBoxManage: error: VBoxNetAdpCtl: Error while adding new interface: failed to open /dev/vboxnetctl: No such file or directory

Simply reload the virtualbox via CLI with .

## Starting Docker breaks KVM bridged networking
The issue is that Docker's scripts add some iptables rules to block forwarding on other interfaces other than its own. This is a [https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=865975 known issue.

Adjust the solutions below to replace br0 with your own bridge name.

Quickest fix (but turns off all Docker's iptables self-added adjustments, which you may not want):

{{hc|/etc/docker/daemon.json|2=
{
  "iptables": false
}
}}

If there is already a network bridge configured for KVM, this may be fixable by telling docker about it.  See where docker configuration is modified as:

{{hc|/etc/docker/daemon.json|2=
{
  "bridge": "br0"
}
}}

If the above does not work, or you prefer to solve the issue through iptables directly, or through a manager like UFW, add this:

Even more detailed solutions are [https://serverfault.com/questions/963759/docker-breaks-libvirt-bridge-network here.

## Image pulls from Docker Hub are rate limited
Beginning on November 1st 2020, rate limiting is enabled for downloads from Docker Hub from anonymous and free accounts. See the rate limit documentation for more information.

Unauthenticated rate limits are tracked by source IP. Authenticated rate limits are tracked by account.

If you need to exceed the rate limits, you can either sign up for a paid plan or mirror the images you need to a different image registry. You can host your own registry or use a cloud hosted registry such as Amazon ECR, Google Container Registry, Azure Container Registry or Quay Container Registry.

To mirror an image, use the ,  and  subcommands of the Docker CLI. For example, to mirror the  tag of the Nginx image to a registry hosted at :

 $ docker pull nginx:1.19.3
 $ docker tag nginx:1.19.3 cr.example.com/nginx:1.19.3
 $ docker push cr.example.com/nginx:1.19.3

You can then pull or run the image from the mirror:

 $ docker pull cr.example.com/nginx:1.19.3
 $ docker run cr.example.com/nginx:1.19.3

## iptables (legacy): unknown option "--dport"
If you see this error when running a container, install  instead of  and reboot=== "Your password will be stored unencrypted" when running docker login ===

[https://docs.docker.com/engine/reference/commandline/login/#credentials-store By default Docker will try to use the  or  binaries to store your registry passwords. If they are not found, it will store them in plain text (base64-encoded) in  and print the following message after successfully logging in:

 $ WARNING! Your password will be stored unencrypted in /home/username/.docker/config.json.

If you are using a password manager that implements the Secret Service Freedesktop DBUS API, like KDE's  or GNOME's , you can install the  package to store your passwords in them.

## "Could not find an available, non-overlapping IPv4 address pool among the defaults to assign to the network"
Sometimes if you use a lot of Docker projects (ex. using docker-compose) it can happens that you run out of available IPs for Docker containers triggering the error:

 Could not find an available, non-overlapping IPv4 address pool among the defaults to assign to the network

As found on this Docker issue, the defaults are:

{| class="wikitable"
! Type !! Default Size !! Default Pool
|-
| local || /16 || 172.17.0.0/12
|-
| local* || /20 || 192.168.0.0/16
|}

This can be easily fixed increasing the Docker IP space by configuring  in  increasing the size value from 16 to 24 on the first IP range, keeping the second one unaltered to avoid ip collision on the local network:

{{hc|/etc/docker/daemon.json|2=
{
  ...
  "default-address-pools" : [
    {
      "base" : "172.17.0.0/12",
      "size" : 24
    },
    {
      "base" : "192.168.0.0/16",
      "size" : 24
    }
  ]
}
}}

Restart  to apply changes.

More details and technical explanations can be found on the following excellent article: The definitive guide to docker's default-address-pools option.

## Slow golang compilation
Due to a ulimit configuration, building a docker image and its dependances with makepkg is very slow (stuck at "Entering fakeroot environment..." step).

It is related to and [https://github.com/containerd/containerd/pull/7566.

You can add  to your docker build option or create/edit:

{{hc|/etc/docker/daemon.json|
{
  "default-ulimits": {
    "nofile": {
      "Name": "nofile",
      "Soft": 1024,
      "Hard": 524288
    }
  }
}
}}
