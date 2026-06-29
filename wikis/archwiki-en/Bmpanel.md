# Bmpanel

BMPanel (BitMap Panel) is a lightweight, NETWM compliant panel for X11 Window System, which contains a desktop switcher, taskbar, system tray and clock. The application is inspired by simplicity of fspanel. BMPanel has a modern look and feel, while keeping itself tiny and small.

## Installation
Install .

## Themes
Further information about available themes can be found here. Here you can find more themes. Extract them to  (respectively  for bmpanel legacy). Altering design of the theme can be done by adapting the  file (respectively ). More information on this can be found here.

## Starting bmpanel
To start BMPanel automatically after login, add the following to your xinitrc:

## Launchbar
BMPanel2 features a simple launchbar that you may configure manually.

In order for this to work, the theme must have the launchbar enabled. Edit the theme file and make sure that it has something to this extent (the xx's represent icon size):

 launchbar
 	icon_size xx xx

Next, you must edit the configuration file for bmpanel2, usually located at . For each entry, you must provide the command to execute along with an icon.

An example configuration is given below:

 theme xsocam_dark

 launchbar
 	exec urxvt
 		icon /usr/share/pixmaps/gnome-term.png
 	exec firefox
 		icon /usr/share/pixmaps/firefox.png
 	exec blender
 		icon /usr/share/pixmaps/blender.png
 	exec urxvt -e htop
 		icon /usr/share/pixmaps/htop.png
 	exec gvim
 		icon /usr/share/pixmaps/gvim.png
