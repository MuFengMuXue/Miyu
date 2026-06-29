# Deepin Desktop Environment

The Deepin Desktop Environment (DDE) is the desktop environment of the Deepin Linux distribution. It is comprised of the desktop environment, a custom window manager, the control center, a launcher and a dock.

## Installation
Install  and  for the basic components for a minimal desktop interface.

Optionally, also install  for some extra applications for a more complete desktop environment.

## Starting
## Via a display manager
LightDM is the default display manager for the DDE. Follow Display manager#Loading the display manager to start it at boot.

## Via xinit
To use Deepin via xinit, you will need to add the following to your .xinitrc file.

## Configuration
## Networking
NetworkManager is integrated in the DDE network administration and is installed together. Enable  to use it.

## Customize touchpad gesture behavior
Deepin does not officially support customizing the gesture behaviors, but it is possible to manually change this by editing the configuration file .

For instance, if you want to disable tapping gesture activity, set its action to :

{{hc|/usr/share/dde-daemon/gesture.json|
[
    ...
    {
        "Name": "tap",
        "Direction": "none",
        "Fingers": 3,
        "Action": {
            "Type": "built-in",
            "Action": "none"
        }
    },
    ...
]
}}

To apply the changes, reboot your system or log off and log in again.

## Changing default deepin sounds
While this is not officially supported, it is possible to change or even remove the default sounds that are used by Deepin (ex. login sound). Simply replace the sounds in the directory:

 /usr/share/sounds/deepin/stereo

Note: If you simply want to disable the sound effects entirely, it can be done from Deepin's system settings (sound section).

## Changing system language
The environment variable  of Deepin can be affected by , and it has the highest precedence at the moment, the  and  will be ignored if this file exists:

## Troubleshooting
## No background after resuming from standby
Because of the way the NVIDIA driver stores its FBOs it happens that after resuming from standby the background suddenly disappears, leaving only a white screen with possibly some color noise on it. The bug appears to be fixed in GNOME upstream, but the Deepin desktop environment still has it.

A possible workaround would be restarting the window manager every time the computer resumes from suspension. A way to do that would be to create the following systemd service

That executes the following script

Once those two files are created in the correct directories, make the script executable and start/enable

## Wireless network does not connect
NetworkManager sets the MAC address generated randomly. This was already enabled by default, to disable it add the following lines to the NetworkManager configuration file.

## Bluetooth Menu does not show up / work
Start/enable . This service is not enabled by default.

## Window shortcuts does not work in dual boot
When home directory is shared in dual boot,
 can lead to strange shortcut behavior and we can try renaming this file to another name.

## Bug reporting
Any bugs related to Arch packaging should be reported in the [https://gitlab.archlinux.org/archlinux/packaging/packages bug tracker.

Any upstream related bugs should be reported here.
All the Deepin developers will see the bug reports and solve them as soon as possible.
