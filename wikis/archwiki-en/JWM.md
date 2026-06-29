# JWM

JWM (Joe's Window Manager) is a lightweight window manager for Xorg written in C. It is under active development and maintained by Joe Wingbermuehle.

## Installation
Install the  package.

## Starting
You can start a JWM session with a display manager. Alternatively, you can run  with xinit.

## Configuration
Configuration is done via a single XML file. There is native support for customizable panels and buttons, and a system tray dock. A sample configuration file is located at  which can be copied to the user configuration :

 $ cp -i /etc/system.jwmrc ~/.jwmrc

Edit this file to establish the environment. See JWM Configuration for a complete list of available tags, attributes and values.

## Autostart
Add an  section in your configuration file to execute one or more commands at startup. For example:

## Tips and tricks
## Improve  contrast
Change the default  settings to match the improved contrast style of the default  and active :

## Logout and refresh
 (Logout) is the menu command to cleanly log out of the current X server.

 (Refresh) is the menu command tag which reinitializes the configuration file and updates menus and keybindings accordingly.

 and  can be bound to the  modified keys following the example syntax below:

 exec:jwm -restart
 exec:jwm -exit

## Reboot and shutdown
The  and  menu options can use systemctl commands:

 systemctl reboot
 systemctl poweroff

Alternatively, use  to bind the commands to a chosen key.

See Allow users to shutdown#Using systemd-logind for additional information.

## Conky
Conky can be run within the  to provide the display of various data streams (e.g. battery life and AC adapter status for notebooks).  may conflict with Conky; workarounds include:

# Review the Conky FAQ for workarounds in
#  Conky and specify the following  tags in :

## Minimal font suggestions
* See  and the X Logical Font Description article for additional details and pattern descriptions.

## Manual tiling support
Tiling support can be added to JWM with the Poor Man's Tiling Window Manager. Assuming  is part of the local , various tiling actions can be assigned to keys, for example:

 exec:manage.py swap
 exec:manage.py cycle
 exec:manage.py left
 exec:manage.py right

## Troubleshooting
## Additional troubleshooting
If X is not already running on ,  will allow you to review standard output errors and messages. See  command for details on how to create a typescript of what is printed to the terminal.

## All windows are transparent using picom
Adjust the window transparency in :

   1.0

## Terminal windows do not fully maximize
Add a group with the  option to , for example:

  URxvt
  iignore

## Verify configuration changes
To check the JWM configuration and return syntax errors (including associated line numbers), if any, run:

 $ jwm -p
