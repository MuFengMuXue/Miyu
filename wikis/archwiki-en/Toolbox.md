# Toolbox

Toolbox is a tool that allows you to create and run containers that seamlessly integrate with the rest of the operating system by providing access to the user's home directory, the Wayland and X11 sockets, networking (including Avahi), removable devices (like USB sticks), systemd journal, SSH agent, D-Bus, ulimits, /dev and the udev database, etc.

## Installation
Install the  package.

Note that  is installed as a dependency of Toolbox. By default it is only possible to run Podman containers as root. See Podman#Rootless Podman to set up running containers as a non-root user. In general, if you are having issues with Toolbox, make sure your issues are not with Podman first.

If you want to build your own toolbox-compatible images, install  as well.

## Fedora Containers
You can create a Fedora 35 toolbox with the following:

 $ toolbox create -d fedora -r 35

Once that's done, you can enter the toolbox with:

 $ toolbox enter fedora-toolbox-35

## Arch Containers
You can create an Arch Linux toolbox with the following:

 $ toolbox create

This will create a container named arch-linux-latest.

Once that's done, you should be able to enter the toolbox with:

 $ toolbox enter

## Troubleshooting
## Error: failed to start container (rootless containers)
You may not be able to enter rootless containers if  is installed due to strict permissions in /dev/vboxusb and toolbox trying to stat vboxusb.

To fix this, change /dev/vboxusb permissions from 750 to 755:
 # chmod -R 755 /dev/vboxusb

## X11 applications not starting
When attempting to run an X11 application from within the toolbox, you may get the following error:

 Authorization required, but no authorization protocol specified
 Error: Can't open display: :0

To fix this, you can use  (on your host machine) to give your container permission to communicate with X11. Run the following, or add it to Xinit#xinitrc:

 $ xauth add "toolbox/unix$DISPLAY" . "$(xauth list | grep "^$(hostnamectl hostname)/unix$DISPLAY\s*MIT-MAGIC-COOKIE-1\s*" | awk '{print $3}')"

Alternatively, run:

 $ xauth nlist | sed -e 's/^..../ffff/' | xauth nmerge -
