# Distrobox

Distrobox is a container wrapping layer that allows the user to install containerised versions of Linux that are different to the host while providing tight integration with the host allowing the use of binaries designed for one distribution to run on another.

Distrobox itself is not a container manager and relies on Podman or Docker to create containers.

From the Distrobox documentation:

:Use any Linux distribution inside your terminal. Enable both backward and forward compatibility with software and freedom to use whatever distribution you’re more comfortable with. Distrobox uses Podman or Docker to create containers using the Linux distribution of your choice. The created container will be tightly integrated with the host, allowing sharing of the HOME directory of the user, external storage, external USB devices and graphical apps (X11/Wayland), and audio.

## Security implications
The main goal of Distrobox is not focused on sandboxing the containers from the host. Due to the tight integration nature of the project, complete isolation is not possible as containers running inside Distrobox will have full access to your home folder and application directories.

It is recommended to use Podman over Docker since by default Docker will run containers as root and rootful containers will have unrestricted access to your hosts filesystem. Rootless Docker is currently not working though is being worked on.

While full sandboxing is not possible, Distrobox offers some isolation features through its unsharing mode. See #Unsharing mode for details.

## Installation
## With root access
First follow the page for either Podman or Docker and make sure you are able to install and run a Hello World container.

Install the  package.

## Without root access/Immutable filesystem
It is possible to install Distrobox into your home folder if you don't have root access to the system or if you are using an immutable distro. Doing so requires the use of a curl-to-sh pipe which is an unsupported installation method due to it posing a security risk.

For instructions, refer to the Distrobox Alternative methods documentation.

## Uninstalling
Distrobox provides an uninstallation script for rootless installs, this script is only required if you installed rootless, if you installed via Pacman then you should uninstall in the usual way.

## Usage
To create a new container run the following:
 $ distrobox create -n name

To list installed containers run the following:
 $ distrobox list

To interact with an installed container run the following:
 $ distrobox enter name

or you can send a command directly to a container with:
 $ distrobox enter name -- command-to-execute

To stop a running container run the following:
 $ distrobox stop name

To delete a container run the following:
 $ distrobox rm name

To install a specific distro into a container run the following (in this example it is Ubuntu):
 $ distrobox create --image ubuntu:22.04

Installations can be fully customised as follows (in this example it is a container called test running Gentoo with root access):
 $ distrobox create -i docker.io/gentoo/stage3:latest -n test --root

If you need your container to have root access to the host then it is recommended that you use the  flag over .

## Unsharing mode
Distrobox allows users to partially isolate certain system aspects through its  feature.
By default, the following components are shared between host and container:

, , , ,  and .

You can choose to  some of these components by using the commands listed below when creating a new container:

{| class="wikitable"
|+ Shares
|-
! Share !! Command !! Usage
|-
| devsysfs ||  || Do not share host devices and sysfs dirs from host.
|-
| ipc ||  || Do not share the ipc namespace with host.
|-
| netns ||  || Do not share the network namespace with host.
|-
| process ||  || Do not share the process namespace with host.
|-
| All ||  || Activate all  flags.
|-
|}

Note that unsharing  and  is not possible, as these are mandatory for Distrobox's core functionality.

## Configuration
It is possible to configure Distrobox in two ways, either with a configuration file or by using environment variables.

## Configuration file
Distrobox checks the following locations for config files, from least important to most important:

*
*
*
*
*

An example config file is as follows:
 container_always_pull="1"
 container_generate_entry=0
 container_manager="docker"
 container_image_default="registry.opensuse.org/opensuse/toolbox:latest"
 container_name_default="test-name-1"
 container_user_custom_home="$HOME/.local/share/container-home-test"
 container_init_hook="~/.local/distrobox/a_custom_default_init_hook.sh"
 container_pre_init_hook="~/a_custom_default_pre_init_hook.sh"
 non_interactive="1"
 skip_workdir="0"

## Environment variables
The following variables are available and should be set using per user variables:
 DBX_CONTAINER_ALWAYS_PULL
 DBX_CONTAINER_CUSTOM_HOME
 DBX_CONTAINER_IMAGE
 DBX_CONTAINER_MANAGER
 DBX_CONTAINER_NAME
 DBX_CONTAINER_ENTRY
 DBX_NON_INTERACTIVE
 DBX_SKIP_WORKDIR

## Tips and tricks
## Run graphical apps
When running graphical apps, you should first install the mesa-dri-drivers GPU drivers in Fedora,  in Arch, or the equivalent Mesa package for the distro.

If you encounter an authorization error, see Toolbox#X11 applications not starting for the fix.

You can run apps installed inside the Distrobox from the outside using  or integrate them with your desktop by running  inside the container.

## Use systemd inside the container
Run the following commands inside the container to make the host systemd accessible inside the container:

 # ln -s /run/host/run/systemd/system /run/systemd
 # mkdir -p /run/dbus
 # ln -s /run/host/run/dbus/system_bus_socket /run/dbus

## Execute commands on the host
It is possible to run a command on the host, while inside the container using . This command requires flatpak to be installed, otherwise it will not work, without an obvious error message == See also ==

* [https://github.com/89luca89/distrobox/ Project GitHub page
