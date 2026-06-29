# Logitech M570

The Logitech M570 is a wireless trackball mouse. It is quite similar to the Logitech Marble Mouse.

## Installation
No additional drivers need to be installed.

## Configuration
## Temporary
If the system is not using libinput, the mouse can be configured on the fly using a script such as:

## Permanent
To make the changes permanent, either a script such as the one above has to be run at startup/login or changes can be made to the Xorg configuration files. When changing the configuration files, the product name as reported by Xorg has to be known and used. Typically, your M570 should be known as , however, it can be valuable to check  for the match product name.

In the two configuration files below, only the essential changes are made to get button scrolling to work. Other worthwhile options are:
*
*

It is important to find out if your system is using only evdev or libinput and evdev. See Xorg#Input devices for how to check the driver in use.

Changes made to Xorg configuration files do not take effect until the X session is restarted. To restart the X session, simply log out from your window manager and log back in.

## Using libinput
Create a configuration file for libinput to recognise it:

## Using evdev
Create a configuration file for evdev to recognise it:
