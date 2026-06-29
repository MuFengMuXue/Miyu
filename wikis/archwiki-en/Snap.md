# Snap

Snap is a software deployment and package management system. The packages are called 'snaps' and the tool for using them is 'snapd', which works across a range of Linux distributions and allows, therefore, distribution-agnostic upstream software deployment. Canonical, the developer of Snap, manages the Snap Store service through which snaps are deployed.

snapd is a REST API daemon for managing snap packages. Users can interact with it by using the snap client, which is part of the same package.

Snaps can be confined using AppArmor which is now enabled in the default kernel. Consult relevant wiki pages to find steps for enabling AppArmor in your system.

## Installation
Install the  package.

snapd supports the AppArmor security model if it is enabled on your system, to install it follow AppArmor#Installation.

If you are using AppArmor, enable and start both  and .

## Configuration
To launch the  daemon when snap tries to use it, enable/start .

## Usage
The snap tool is used to manage the snaps.

## Finding
To find snaps to install, you can query the Ubuntu Store with:

 $ snap find searchterm

## Installing
Once you found the snap you are looking for you can install it with:
 # snap install snapname
This requires root privileges. Per user installation of snaps is not possible, yet. This will download the snap into  and mount it to  to make it available to the system.

It will also create mount units for each snap and add them to  as symlinks to make all snaps available when the system is booted.
Once that is done you should find it in the list of installed snaps together with its version number, revision and developer using:
 $ snap list

You can also sideload snaps from your local hard drive with:
 # snap install --dangerous /path/to/snap

## Updating
To update your snaps manually use:
 # snap refresh

Snaps are refreshed automatically according to snap  setting.

To view the next/last refresh times use:
 # snap refresh --time

To set a different refresh time, eg. twice a day:
 # snap set core refresh.timer=0:00~24:00/2

See system options documentation page for details on customizing the refresh time.

## Removing
Snaps can be removed by executing:
 # snap remove snapname

## Tips and tricks
## Classic snaps
Some snaps (e.g. Julia and Pycharm) use classic confinement. However, classic confinement requires the  directory, which is not FHS-compliant. The snapd package does not ship this directory, however the user can manually create a symbolic link between  and  to allow the installation of classic snaps:

 # ln -s /var/lib/snapd/snap /snap

## Confinement
When using AppArmor, snapd will generate the same profiles for snaps as on Ubuntu. The AppArmor parser is smart enough to drop the rules that are not yet supported by the mainline kernel.

To verify that basic confinement is working, install hello-world snap. Then run the following:

The denial was caused by AppArmor and should have been logged:

If you do not see the denial, verify that the profiles were loaded:

Also, you can check what sandbox features are available in the system according to snapd:

## Hide the snap folder
See XDG Base Directory#Hiding unwanted directories to hide the  folder.

## Sudo
With  being enabled in sudo by default, the  directory is no longer present in the default  environment variable of the process started by sudo. Commands such as  will fail, as the  symbolic link can no longer be found by the shell process.

This can be addressed on per user basis by adding the following snippet to :

 # Add snap binaries installation dir to PATH
 Defaults: secure_path="/usr/local/sbin:/usr/local/bin:/usr/bin:/var/lib/snapd/snap/bin"

Where  must be replaced with the desired .

## Troubleshooting
## Text unreadable
If you are seeing squares instead of readable characters, you need to clear the font cache:

 # rm -f /var/cache/fontconfig/*
 $ rm -f ~/.cache/fontconfig/*
 # fc-cache -r -v

Snapctl also stores internal caches for each individual snap, which need to be cleared seperately.
First, find them by running:

Then either remove them individually or use this simple loop.

Finally, Restart your session.

## Error: cannot mount squashfs
Snap packages use the SquashFS file system. In the event of an error similar to the following:
 error: system does not fully support snapd: cannot mount squashfs image using "squashfs"
you may verify that the SquashFS kernel module is loaded with

## Error: /user.slice/user-1000.slice/session-1.scope is not a snap cgroup
You need to set your DBUS_SESSION_BUS_ADDRESS environment variable like so:

 export DBUS_SESSION_BUS_ADDRESS="unix:path=$XDG_RUNTIME_DIR/bus"

To make this change permanent and also available in your GUI session, consider adding this line to your ~/.xprofile file.

For more information and full discussion about this issue, please read here

## Graphical management
Both Gnome Software Center and KDE Discover can provide native snap support. For KDE Discover install  package.

The Snap Store can be installed via snap

 # snap install snap-store

## Support
Arch Linux related mailing lists and other official Arch Linux support channels are not an appropriate place to request help with snaps on Arch Linux. An appropriate place to ask for support is the Snapcraft forum.
