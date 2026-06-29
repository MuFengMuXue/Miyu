# MangoWM

Mango is a modern, lightweight, high-performance tiling Wayland compositor built on dwl — crafted for speed, flexibility, and a customizable desktop experience.

## Installation
Install the  package.

Alternatively  depends on  which supports individual window capture but not scenefx.

## Starting
Select Mango from the menu in a display manager or run  from a tty.

## LXQT
See LXQt#Wayland session.

## Configuration
The system-wide mango configuration file is  while user configuration is :

## Creating the configuration file
First, run the following to create the directory needed in the next step:

 $ mkdir -p ~/.config/mango/

Whenever started, mango will attempt to use whatever custom settings are contained in , then fall back to . The user configuration file is not created by default, so copy the template file:

 $ cp /etc/mango/config.conf ~/.config/mango/

## Autostart
Add an  command in  file to execute a command at startup. For example:

 exec-once=waybar

Using an  command instead will ensure that the command is also run whenever mango is restarted.

## Screen sharing
To setup PipeWire screen sharing install the  package (or  for ).

If the portal does not start automatically try autostarting .

## Troubleshooting
## Fixing misbehaving Java applications
See Java#Gray window, applications not resizing with WM, menus immediately closing.
