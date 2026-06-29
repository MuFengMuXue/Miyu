# Incus

Incus is a manager/hypervisor for containers (via LXC) and virtual-machines (via QEMU).

It is a fork of LXD by the original maintainers. Documentation from the LXD wiki page is still largely relevant and encouraged reading.

## Installation
Install the  package, then enable the .

Alternatively, you can enable/start the  directly, in case you want instances to autostart for example.

To delegate container creation to users, enable/start the  unit. See #Accessing Incus as an unprivileged user for group delegation.

The split package  provides a
few related utilities.

## Migrating from LXD
If you wish to migrate from an existing LXD installation, you should do so at this point, as the migration tool will only run against an empty target Incus server.

After verifying that both the  and  commands are running correctly, read the upstream documentation about the process, and afterwards run the migration tool:

 # lxd-to-incus

## Configuration
## Unprivileged containers
Incus launches unprivileged containers by default (see Linux Containers#Privileged or unprivileged for an explanation of the difference).

For this to work, you need to setup an appropriate range of sub{u,g}ids for the root userunlike e.g. podman, Incus uses a daemon that needs to run as root.[https://discuss.linuxcontainers.org/t/incus-no-uid-gid-allocation-configured/19002/13

Verify the content of both  and , and if needed add a contiguous range of at least 10M UID/GID for the root user:

 # usermod -v 1000000-1000999999 -w 1000000-1000999999 root

Then restart .

For the alternative, see LXD#Privileged containers.

## Accessing Incus as an unprivileged user
From the official documentation:

"Access to Incus is controlled through two groups:
*  allows basic user access, no configuration and all actions restricted to a per-user project.
*  allows full control over Incus."

To have a normal user capable of launching and operating instances, add the user to the  group.

To give a normal user full control over Incus without having to use sudo, add the user to .

## Initialize Incus config
Before it can be used, Incus' config needs to be initialized:

 # incus admin init

This will start an interactive configuration guide in the terminal, that covers different topics like storages, networks etc. You can find an overview in the official Getting Started Guide.

## Adding a web UI
The lxd-ui browser frontend has been patched to fit Incus. These patches are found in the debian package source. To make use of this UI install the  package.

Then set the address and port for the webserver:

 $ incus config set core.https_address=127.0.0.1:8443

And restart Incus.

Another available option is to run the web server with the following command:

 $ incus webui

For this option, see [https://linuxcontainers.org/incus/docs/main/reference/manpages/incus/webui/ incus webui

## Usage
## Overview of commands
You can get an overview of all available commands by typing:

 $ incus

## Create a container
Container are based on images, that are downloaded from image servers or remote LXD servers.

You can see the list of already added servers with:

 $ incus remote list

You can list all images on a server with , for example:

 $ incus image list images:

This will show you all images on one of the default servers: images.linuxcontainers.org

You can also search for images by adding terms like the distribution name:

 $ incus image list images:debian

Launch a container with an image from a specific server with:

 $ incus launch servername:imagename

For example to create a randomly named container instance from the Ubuntu Noble image from the default server:

 $ incus launch images:ubuntu/noble

To specify a name for the instance simply add it afterwards, e.g.:

 $ incus launch images:archlinux/current/amd64 arch

will create an amd64 Arch container named .

## Arch Linux container configuration
## Disabling udev in unprivileged containers
When running unprivileged Arch Linux containers, systemd's udev services will generate numerous "Permission denied" errors during boot and package updates (particularly when  runs). This occurs because udev attempts to write to  files owned by the host.

These errors result from an inappropriate default configuration of Arch container images for unpriviledged operation — the container functions correctly.

As per the systemd Container Interface,  is not intended to run in unprivileged containers. Mask the udev services inside the container:

 # systemctl mask \
   systemd-udevd.service \
   systemd-udevd-control.socket \
   systemd-udevd-kernel.socket \
   systemd-udevd-varlink.socket \
   systemd-udev-trigger.service \
   systemd-udev-load-credentials.service

After masking, restart the container:

 $ incus restart container_name

## Tips and tricks
## Access the containers by name on the host
This assumes that you are using the default bridge that it is named  and that you are using systemd-resolved.

 # systemd-resolve --interface incusbr0 --set-domain '~incus' --set-dns $(incus network get incusbr0 ipv4.address | cut -d / -f 1)

You can now access the containers by name:

 $ ping containername.incus

To make this change permanent, edit the  systemd unit to include an  directive, which runs the command after launch:

## Troubleshooting
## Starting a virtual machine fails
If you see the error:

 Error: Couldn't find one of the required UEFI firmware files: vars:OVMF_VARS.4MB.ms.fd} {code:OVMF_CODE.2MB.fd vars:OVMF_VARS.2MB.ms.fd} {code:OVMF_CODE.fd vars:OVMF_VARS.ms.fd} {code:OVMF_CODE.fd vars:qemu.nvram}

It's because Arch Linux does not distribute secure boot signed ovmf firmware. To boot virtual machines, you need to disable secure boot for the time being:

 $ incus launch ubuntu:18.04 test-vm --vm -c security.secureboot=false

This can also be added to the default profile by doing:

 $ incus profile set default security.secureboot=false

## Network connectivity issues
# The official documentation provides instructions on how to configure your firewall.
# Incus creates and manages its own network interfaces, and NetworkManager may interfere in some cases. It may be a good idea to add any entry to ignore  devices using the instructions in NetworkManager#Ignore specific devices.
# Docker's default configuration breaks networking in Incus. Consult the official documentation if Docker and Incus need to run on the same machine.

## Incus does not respect Shell's environment proxy variables
Examples are  or  commands not using value of / variables when downloading images.

Incus implements a server-client paradigm. It simply means that operations are done by  acting as the Incus server — usually running in the background, unless invoked from an interactive shell. And  commandline interface is used to communicate with Incus server acting as the Incus client.

That makes , typically started as a service, not inheriting shell's environment variables of the client. But respecting variables of the environment that it's invoked from, instead.In Arch Linux, Incus server is started by systemd.

There can be many workarounds to this difficulty, following exist some examples. See Incus's [https://github.com/lxc/incus/issues/574 issue#574 for more information.

## Temporary
## Import Shell variables to systemd's environment
First, export  variables:

 $ export ALL_PROXY="socks://proxy_server_address:port/"

Import them to systemd's environment:

 # systemctl import-environment ALL_PROXY

Re/start  unit.

## Persistent
## Edit incus service unit
If you want Incus daemon to always start with some static environment variables, like , you can use  directive of systemd.  command cannot manipulate  directive. Edit  and add  key with appropriate  pair. For example:

## Use Incus core.proxy options
One can make Incus server use a desired proxy with configuring Incus's server with core.proxy options. For instance:

 # incus config set core.proxy_http "proxy_address:proxy_port"

## Uninstall
Stop and disable the services. Then uninstall the  package.

If you want to remove all data:

 # rm -r /var/lib/incus

If you used any of the example networking configuration, you should remove those as well.
