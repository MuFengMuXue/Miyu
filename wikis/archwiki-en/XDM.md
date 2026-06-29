# XDM

From :

:Xdm manages a collection of X displays, which may be on the local host or remote servers. The design of xdm was guided by the needs of X terminals as well as The Open Group standard XDMCP, the X Display Manager Control Protocol. Xdm provides services similar to those provided by init, getty and login on character terminals: prompting for login name and password, authenticating the user, and running a "session."

XDM provides a simple and straightforward graphical login prompt.

## Installation
Install the  package. Optionally, install the  package for Arch Linux themes.

Follow Display manager#Loading the display manager to start XDM at boot.

## Configuration
## Defining the session
Unlike many more modern display managers such as GDM or LightDM, XDM does not source available sessions from .desktop files located in the  directory. As such, XDM does not have a 'session menu.' Instead, XDM will execute the  file in the home directory.

For example, to start Xfce upon login, the  file should look like this:

 startxfce4

Ensure that the  file in your home directory is executable.

## Theming
For the exact meanings of the options discussed below, see . The configuration file is located in , notice that if you installed  the configuration file will instead be located in .

## Background wallpaper
Install .

Create a directory to put wallpapers in, e.g  and then place them inside it.

Edit . Change the  command to

## Font
* Edit . Add/replace the following defines:
 xlogin*greetFont:  -adobe-helvetica-bold-o-normal--20------iso8859-1
 xlogin*font:       -adobe-helvetica-medium-r-normal--14------iso8859-1
 xlogin*promptFont: -adobe-helvetica-bold-r-normal--14------iso8859-1
 xlogin*failFont:   -adobe-helvetica-bold-r-normal--14------iso8859-1

## Login dialog positioning
This configuration will move the login dialog to the bottom right of the screen.

 xlogin*frameWidth: 1
 xlogin*innerFramesWidth: 1
 xlogin*logoPadding: 0
 xlogin*geometry:    300x175-0-0

## Removing the logo
Comment out the logo defines:
 #xlogin*logoFileName: /usr/share/xdm/pixmaps/xorg.xpm
 #xlogin*logoFileName: /usr/share/xdm/pixmaps/xorg-bw.xpm

## Multiple X sessions & Login in the window
With the XDMCP enabled, you can easily connect to local or remote XDM instance and run multiple X sessions simultaneously on the same machine:

 # X -query xdmcp-server-ip :2

This command will launch the second session in window using Xephyr:

 $ Xephyr -query xdmcp-server-ip :2

## Passwordless login
In order to enable passwordless login for XDM, add the line below to :

 xlogin*allowNullPasswd: true
