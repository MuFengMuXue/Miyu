# Touchegg

Touchegg is a multitouch gesture program that runs as a user in the background,
recognizes gestures, translates them to more conventional types of events and/or performs custom actions in response to them.

Touchegg is not compatible with Wayland.

## Installation
Install the  package. Install  if you want a desktop application to configure touchegg.

For X11 GNOME, one can also install the extension X11 Gestures in addition to touchegg.

## Configuration
The default configuration can be found in .

To customize it, copy the default configuration to  and make your changes.

It is a basic XML file that defines various gestures. Please note that at this time,
, , and  do not appear to work.

See the list of triggers and the list of actions.

The two-fingers scrolling emulation has been dropped, due to bad user experience, in the recent 2.0 rewrite of touchegg.
To restore it, install  and add the following to the configuration file:

Note that on KDE, text gets selected while scrolling (see upstream issue 401).

## Start on login
Enable , the client can then be autostarted.
