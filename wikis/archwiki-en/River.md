# River

According to River's homepage:
:River is a non-monolithic Wayland compositor. Unlike other Wayland compositors, river does not combine the compositor and window manager into one program. Instead, users can choose any window manager implementing the river-window-management-v1 protocol.

The stated goals for River is to make getting into Wayland development easier and to allow its "window managers" to be more experimental as they do not need to write a whole compositor. This also allows for things not normally possible with Wayland Compositors such as reloading configurations without closing all windows.

## Installation
River is installed with the  package.

A separate window manager will need to be installed as well. See also River's wiki for a more comprehensive list of window managers.

## Stacking
*

## Tiling
*
## Other
*

## Starting
River can be started by a display manager or with the command below.

 river

River can be started with select window manager with the "c" argument.

 river -c foo

## Configuration
River is configured through a executable shell file, by default it is located in . By default this is .

River can use a different configuration if it is called with the "c" argument.

 river -c customConfPath
## Selecting a default window manager
A window manager can be made the default by appending it to River's configuration file.

## Autostart
Since the configuration is executed by the bourne shell. Commands placed inside the configuration will be executed on start up, certain window managers also allow for autostarting in their configurations.

## Input configuration
Input configuration can be done in multiple ways. Some window managers support input configuration.

There are separate  input managers such as Channel and  that can be used.

If only the keyboard layout needs to be changed. Change the environment variable to the needed layout; example "gb" for UK keyboards.

## Troubleshooting
## Configuration file does nothing
This may be caused by the configuration file lacking execution permissions. See File permissions and attributes.

## Screencast via WebRTC does not work
See River Classic#Troubleshooting.
