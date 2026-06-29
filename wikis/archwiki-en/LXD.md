# LXD

LXD is a manager/hypervisor by Canonical for containers (via LXC) and virtual-machines (via QEMU).

## Installation
Install the  package, then enable the .

Alternatively, you can enable/start the  directly, in case you want instances to autostart for example.

## Configuration
## Unprivileged containers
It is recommended to use unprivileged containers (see Linux Containers#Privileged or unprivileged for an explanation of the difference).

For this, modify both  and  (if these files are not present, create them) to contain the mapping to the containerized uid/gid pairs for each user who shall be able to run the containers. The example below is simply for the root user (and systemd system unit):

 # usermod -v 1000000-1000999999 -w 1000000-1000999999 root

Now, every container will be started  by default.

For the alternative, see #Privileged containers.

## Configure LXD
On the first start, LXD needs to be configured.

Run as root:

 # lxd init

This will start an interactive configuration guide in the terminal, that covers different topics like storages, networks etc.

You can find an overview in the official Getting Started Guide.

## Accessing LXD as an unprivileged user
By default, the LXD daemon allows users in the  group access, so add your user to this group.

## Usage
LXD consists of two parts:

* the daemon (the lxd binary)
* the client (the lxc binary)

The client is used to control one or multiple daemon(s).

The client can also be used to control remote LXD servers.

## Overview of commands
You can get an overview of all available commands by typing:

 $ lxc

## Create a container
You can create a container with , for example:

 $ lxc launch ubuntu:20.04

Container are based on images, that are downloaded from image servers or remote LXD servers.

You can see the list of already added servers with:

 $ lxc remote list

You can list all images on a server with , for example:

 $ lxc image list images:

This will show you all images on one of the default servers: cloud-images.ubuntu.com

You can also search for images by adding terms like the distribution name:

 $ lxc image list images:debian

Launch a container with an image from a specific server with:

 $ lxc launch servername:imagename

For example:

 $ lxc launch images:centos/8/amd64 centos

To create an amd64 Arch container:

 $ lxc launch images:archlinux/amd64 arch

## Create a virtual machine
Just add the flag  to :

 $ lxc launch ubuntu:20.04 --vm

## Use and manage a container or VM
See "Manage instances" in the official Getting Started Guide of LXD.

## Container/VM configuration
You can add various options to instances (containers and VMs).

See Configuration of instances in the official Advanced Guide of LXD for details.

## Tips and tricks
## Access the containers by name on the host
This assumes that you are using the default bridge that it is named  and that you are using systemd-resolved.

## Temporary solution
As a temporary solution, you can set the local dns address to resolve an arbitrary domain, e.g. .

 # resolvectl dns lxdbr0 $(lxc network get lxdbr0 ipv4.address | cut -d / -f 1)
 # resolvectl domain lxdbr0 '~lxd'

You can now access the containers by name:

 $ ping containername.lxd

This behavior will be reset if the  bridge is managed by lxd (default behavior) and the bridge is reset, for example after a reboot of the host machine.

## Permanent solution
Refering to the official documentation, it is possible to set a systemd service that will set the local dns for the lxd bridge at startup. Replace  with the local  IP address:

Then enable/start the service.

## Use Wayland and Xorg applications
There are multiple methods to use GUI applications inside containers, you can find an overview in the official LXD forum.

The following method grants containers access to the host's sockets of Wayland (+Xwayland) or Xorg.

## Add the following devices to a containers profile
See also LXD documentation regarding devices.

General device for the GPU:

 mygpu:
    type: gpu

Device for the Wayland socket:

 Waylandsocket:
     bind: container
     connect: unix:/run/user/1000/wayland-0
     listen: unix:/mnt/wayland1/wayland-0
     uid: "1000"
     gid: "1000"
     security.gid: "1000"
     security.uid: "1000"
     mode: "0777"
     type: proxy

Device for the Xorg (or Xwayland) Socket:

 Xsocket:
     bind: container
     connect: unix:/tmp/.X11-unix/X0
     listen: unix:/mnt/xorg1/X0
     uid: "1000"
     gid: "1000"
     security.gid: "1000"
     security.uid: "1000"
     mode: "0777"
     type: proxy

## Link the sockets to the right location inside the container
Shell script to link the Wayland socket:

 #!/bin/sh
 mkdir /run/user/1000
 ln -s /mnt/wayland1/wayland-0 /run/user/1000/wayland-0

Link the Xorg (or Xwayland) socket:

 #!/bin/sh
 ln -s /mnt/xorg1/X0 /tmp/.X11-unix/X0

## Add environment variables to the users config inside the container
For Wayland:

 $ echo "export XDG_RUNTIME_DIR=/run/user/1000" >> ~/.profile
 $ echo "export WAYLAND_DISPLAY=wayland-0" >> ~/.profile
 $ echo "export QT_QPA_PLATFORM=wayland" >> ~/.profile

For Xorg (or Xwayland):

 $ echo "export DISPLAY=:0" >> ~/.profile

Reload the :

 $ source ~/.profile

## Install necessary software in the container
Necessary software needs to be added. For now, you can install an example GUI application; this will probably install all necessary packages as well.

## Start GUI applications
Now, you should be able to start GUI applications inside the container (via terminal for example) and make them appear as a window on your hosts display.

You can try out glxgears for example.

## Privileged containers
If you want to set up a privileged container, you must provide the config key .

Either during container creation:

 $ lxc launch ubuntu:20.04 ubuntu -c security.privileged=true

Or for an already existing container, you may edit the configuration:

## Add a disk device
## Read-Only
If you want to share a disk device from the host to a container, all you need to do is add a  device to your container. The virtual  device needs a name (only used internally in the LXC configuration file), a path on the host's filesystem pointing to the disk you want to mount, as well as a desired mountpoint on the container's filesystem.

 $ lxc config device add containername virtualdiskname disk source=/path/to/host/disk/ path=/path/to/mountpoint/on/container

## Read-Write (unprivileged container)
The preferred method for read/write access is to use the "shift" method included in LXD.

shift is based on Linux kernel functionality and available in two different versions:

* the most recent version is called "idmapped mounts" and is included in all upstream kernels >5.12 by default. So it is also included in the regular Arch Linux kernel ().
* the old version is called "shiftfs" and needs to be added manually to most kernels as a kernel module. It is available as a legacy version to support older kernels. You can take a look at this GitHub repo that uses the shiftfs kernel module from Ubuntu kernels: https://github.com/toby63/shiftfs-dkms

Shift should be available and activated by default on Arch with the regular Arch Linux kernel () and the  package.

1. To check whether shift is available on your system, run

The first part of the output shows you:

If either idmapped_mounts or shiftfs is true, then your kernel includes it already and you can use shift.
If it is not true, you should check your kernel version and might try the "shiftfs" legacy version mentioned above.

The second part of the output shows you either:

or:

If either idmapped_mounts or shiftfs is true, then LXD has already enabled it.
If it is not enabled, you must enable it first.

2. Usage

Then you can simply set the "shift" config key to "true" in the disk device options.
See: LXD Documentation on disk devices

See also: tutorial in the LXD forums

## Bash completion does not work
This workaround may fix the issue:

 # ln -s /usr/share/bash-completion/completions/lxd /usr/share/bash-completion/completions/lxc

## Troubleshooting
## lxd-agent inside a virtual machine
Inside some virtual machine images, the  is not enabled by default.

In this case, you have to enable it manually, for example by mounting a  network share. This requires console access with a valid user.

1. Login with  and replace  accordingly.

 $ lxc console virtualmachine-name

Login as root:

 $ su root

Mount the network share:

 $ mount -t 9p config /mnt/

Go into the folder and run the install script (this will enable the lxd-agent inside the VM):

 $ cd /mnt/
 $ ./install.sh

After a successful install, reboot with:

 $ reboot

Afterwards, the  is available and  should work.

## Check kernel config
By default, the Arch Linux kernel is compiled correctly for Linux Containers and its frontend LXD. However, if you are using a custom kernel or changed the kernel options, the kernel might be configured incorrectly. Verify that your kernel is properly configured:

 $ lxc-checkconfig

## Resource limits are not applied when viewed from inside a container
Install  and start .

lxd will need to be restarted. Enable  for the service to be started at boot time.

## Starting a virtual machine fails
If you see the error:

 Error: Couldn't find one of the required UEFI firmware files: vars:OVMF_VARS.4MB.ms.fd} {code:OVMF_CODE.2MB.fd vars:OVMF_VARS.2MB.ms.fd} {code:OVMF_CODE.fd vars:OVMF_VARS.ms.fd} {code:OVMF_CODE.fd vars:qemu.nvram}

It is because Arch Linux does not distribute secure boot signed ovmf firmware. To boot virtual machines you need to disable secure boot for the time being:

 $ lxc launch ubuntu:18.04 test-vm --vm -c security.secureboot=false

This can also be added to the default profile by doing:

 $ lxc profile set default security.secureboot=false

## No IPv4 with systemd-networkd
Starting with version version 244.1, systemd detects if  is writable by containers. If it is, udev is automatically started and breaks IPv4 in unprivileged containers. See commit bf331d8 and discussion on linuxcontainers.

On containers created past 2020, there should already be a  override to work around this issue, create it if it is not:

You could also work around this issue by setting  in the profile of the container to ensure  is read-only for the entire container, although this may be problematic, as per the linked discussion above.

## No networking with ufw
When running LXD on a system with ufw, the output of  will contain an empty IPv4 field, outbound requests will not be forwarded out of the container, and inbound requests will not be forwarded into the container. As seen in a thread on LXC's Discourse instance, ufw will block traffic from LXD bridges by default. The solution is to configure two new ufw rules for each bridge:

 # ufw route allow in on lxdbr0
 # ufw allow in on lxdbr0

For more information on these two commands, check out this thread which describes these commands and their limitations in more detail.

## No networking with Docker installed
You have Docker installed on the host, and you are not able to access LAN or internet from within a lxc container.

 # iptables -I DOCKER-USER -i lxdbr0 -o interface -j ACCEPT
 # iptables -I DOCKER-USER -o lxdbr0 -m conntrack --ctstate RELATED,ESTABLISHED -j ACCEPT

On the first line, replace  with the external network interface (what connects the host to LAN/internet, e.g. , , ...). Also replace  if needed.

For more details, see this note in the LXD documentation.

## Building a snap with snapcraft: craft-providers error: LXD requires additional permissions.
If you get the following error:

 craft-providers error: LXD requires additional permissions.
 Ensure that the user is in the 'lxd' group.
 Visit https://documentation.ubuntu.com/lxd/en/latest/getting_started/ for instructions on installing and configuring LXD for your operating system.
 Full execution log: '/home/your_user/.local/state/snapcraft/log/snapcraft-20231129-221308.209638.log'

This might occur if you try to build a snap with the  command. If the error is still there even after you added yourself to the lxd group and rebooted, try installing lxd via snap instead of as an Arch package (do not install both), that might solve this problem.

## Uninstall
Stop and disable  and . Then uninstall the  package.

If you uninstalled the package without disabling the service, you might have a lingering broken symlink at .

If you want to remove all data:

 # rm -r /var/lib/lxd

If you used any of the example networking configuration, you should remove those as well.
