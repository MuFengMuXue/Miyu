# IceWM

According to Wikipedia:
:IceWM is a window manager for the X Window System graphical infrastructure, written by Marko Maček. It was coded from scratch in C++ and is released under the terms of the GNU Lesser General Public License. It is relatively lightweight in terms of memory and CPU usage, and comes with themes that allow it to imitate the UI of Windows 95, OS/2, Motif, and other graphical user interfaces.

## Installation
Install the  package.

## Starting
With xinit run , or  to also run icewmbg and icewmtray.

## Configuration
Configuration changes from the defaults can be made either system wide (in ) or on a user-specific basis (in ).

To change your icewm configuration from the default, copy the default configuration files from  to , for example:

 $ cp -r /usr/share/icewm/ ~/.config/icewm/

* is the core configuration file for IceWM.
* controls the contents of the IceWM application menu.
* allows the user to customize keyboard shortcuts.
* row of launcher icons on the taskbar.
* behavior of individual applications.
* theme path/name.
* script or command (must be executable) executed on startup.
* the same for shutdown.

## Autostart
The  script is not provided by the  package so you will need to create it yourself, add the commands for the programs that you wish to start with the IceWM session and make it executable.

Below is an example of an IceWM startup script which starts  and XScreenSaver within the IceWM session:

## Generating menu entries
 from the official repositories is a Python script that automatically populates your applications menu based on what is installed in your system. Although this may result in a menu filled with many unwanted applications, it may still be preferable to manually editing the menu configuration file. When running MenuMaker, use the -f flag to overwrite an existing menu file:

 $ mmaker -f icewm

You can avoid populating your menu with terminal based applications such as  by running the following switches with the mmaker command:  and . For example:

 $ mmaker -f --no-legacy --no-debian icewm

Alternatively, you can generate a menu using xdg-menu. See the xdg-menu#IceWM section.

## Themes
A small number of themes are included in the  package. These can supplemented by the themes available from the  package. Many more themes can be downloaded from box-look.org.

## Desktop icons
A file manager such as PCManFM or  can manage the wallpaper and add desktop icons. Alternatively, you could install Idesk, a small program that can also add icons to the desktop.

## Tips and tricks
## Compositing
IceWM is not a compositing window manager. If you need compositing with IceWM, you have the option of using a standalone composite manager such as Xcompmgr or Picom.

## Troubleshooting
## No start menu icon (Intel graphics)
If you are using IceWM with Intel graphics you may find that the start menu in your taskbar has no icon. This is due to a recent change in the  driver which means that the new, but rather unstable, SNA acceleration backend is used by default. To fix the start menu issue (and other possible graphical glitches) you need to switch back to the older UXA backend. See the following article: Intel graphics#AccelMethod.

## Unable to logout when PCManFM is managing the desktop
If you use PCManFM to manage the desktop you may find that the IceWM logout button no longer works. As a workaround, you can define a logout command. This should allow you to logout whilst PCManFM is managing the desktop. To do this, uncomment :

## No shutdown or reboot options in logout menu
* Logout command has been defined:
Shutdown and reboot commands will be ignored if a logout command has been defined. If you want shutdown and reboot options in the logout menu then you must not define a logout command.

* Logout command has not been defined:
If you have defined shutdown and reboot commands (such as  and ) and you have not defined a logout command but you still find that there are no shutdown or reboot options in the logout menu then update to . See  for more information.
