# Stalonetray

Stalonetray is a stand-alone freedesktop.org and KDE system tray for the X Window System. It has full XEMBED support, minimal dependencies and works with virtually any EWMH-compliant window manager. Window managers that are reported to work well with stalonetray are: FVWM, Openbox, Enlightenment, Compiz, Xmonad, dwm, and awesome.

## Installation
Install . Once installed, copy the  file to your XDG configuration directory. It can also be placed directly in the home directory  as .

 $ cp /etc/stalonetrayrc ~/.config/stalonetrayrc

## Configuration
## Openbox
To run Stalonetray in Openbox,  must be set to . This can be accomplished with either the command-line argument  or by modifying .

Openbox now treats the tray as the dock, and you can adjust its position by using the Openbox Configuration Tool. To run Stalonetray on start up, add the following to :
 stalonetray --dockapp-mode simple &

See also Stalonetray WM hints for OpenBox

## Troubleshooting
## Icons do not have the desired size
To force the size of the icons to be equal to icon_size, launch stalonetray with the following arguments:

 stalonetray --icon-size=16 --kludges=force_icons_size

This will force the size of all icons to 16×16 pixels.

Alternatively, one could add the following to the configuration file:

 icon_size 16
 kludges force_icons_size
