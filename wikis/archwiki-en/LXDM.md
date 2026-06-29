# LXDM

LXDM is a lightweight display manager for the LXDE desktop environment.

LXDM does not support the XDMCP protocol. An alternative that does is LightDM.

## Installation
Install the  package.

Follow Display manager#Loading the display manager to LXDM at boot.

## Configuration
The configuration files for LXDM are all located in . The main configuration file is . Its format is documented in its comments. Another file, , is the systemwide x session configuration file and should generally not be edited. All other files in this directory are shell scripts, which are run when certain events happen in LXDM.

These are:
#  is executed with root privileges when LXDM is ready to show the login window.
#  is run as root before logging a user in.
#  is run as the logged-in user right after they have logged in.
#  is run as the logged-in user right after they have logged out.
#  is run as root before rebooting with LXDM.
#  is run as root before poweroff with LXDM.

## Default session
The default session can be set globally, as well as set at an individual-user level. Individual user preferences take precedence over globally set preferences for the user in question.

## Globally
Edit  and change the session line to whatever session or DE is desired:

Example using Xfce:

Example using Openbox:

Example using GNOME:

This is useful for themes that have no visible session selection box, and if experiencing trouble using autologin.

## Per user
To define an individual user's preferred session, simply edit their respective  to define the selection.

Example: user1 wants Xfce4, user2 wants Cinnamon, and user3 wants GNOME:

For user1:
 Session=xfce

For user2:
 [Desktop
 Session=cinnamon

For user3:
 Session=gnome

The list of installed sessions can be displayed by using command:
 $ ls /usr/share/xsessions/

## Autologin
To log in to one account automatically on startup, without providing a password, find the line in  that looks like this:
 #autologin=dgod
Uncomment it, substituting the target user instead of dgod.

## Last used options
Previously used LXDM options can be found in:

## Tips and tricks
## Adding face icons
A 96x96 px image (jpg or png) can optionally be displayed on a per-user basis, replacing the stock icon. Copy or symlink the target image to . The  package supplies some default icons suitable for the lxdm screen. Look under  after installing that package.

## Simultaneous users and switching users
LXDM allows multiple users to be logged into different TTYs simultaneously. The following command is used to allow another user to log in without logging out the current user:

 $ lxdm -c USER_SWITCH

## Themes
The LXDM themes are located in .

There is only one theme provided with LXDM: Industrial. To display the background file  which is part of this theme, install .

 provides 6 extra themes: Archlinux, ArchlinuxFull, ArchlinuxTop, Arch-Dark, Arch-Stripes, and IndustrialArch.

Choice of theme is configurable in :

 ## the theme of greeter
 theme=theme_name

You can also configure LXDM to use a GTK theme (stored in ) in :

 ## GTK theme
 gtk_theme=gtk_theme_name

## Advanced Session Configuration
After a user logs on, LXDM sources all of the following files, in the below order:

#
#
#
#

These files can be used to set session environment variables and to start services which  must set certain environment variables in order for clients in the session to be able to use the service, like ssh-agent. See Xprofile for details.

Note that LXDM does not source , so those migrating from a DM that does use this file, like SLiM, will have to move their settings elsewhere — probably . Also note LXDM does not source .

If you still want to use your  file, you can add a line to the  event file:

 source ~/.xinitrc

LXDM also makes use of .Xresources, .Xkbmap, and .Xmodmap. See  for details on how LXDM uses system-wide and per-user configuration files to configure the session.[https://gitlab.archlinux.org/archlinux/packaging/packages/lxdm/-/blob/main/Xsession

## Troubleshooting
## White flash
When using the default LXDM  and a dark background image (e.g. ) there may be a short bright flash before LXDM starts. This is caused by the  property of the selected GTK theme. To avoid this change  to  or to another dark theme.

## Logout Issue
If you had trouble logging out when using lxdm (e.g. stuck, display freeze, etc..) try uncomment the  option in  to refresh xserver on every logout.
