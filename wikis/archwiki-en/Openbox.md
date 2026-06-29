# Openbox

Openbox is a lightweight, powerful, and highly configurable stacking window manager with extensive standards support. It may be built upon and run independently as the basis of a unique desktop environment, or within other integrated desktop environments such as KDE and Xfce, as an alternative to the window managers they provide. The LXDE desktop environment is itself built around Openbox.

## Installation
Install the  package. Also install TTF fonts such as  and .

## Starting
## Standalone
Run  or  with xinit. Note that only  provides autostart.

## Other desktop environments
See Desktop environment#Custom window manager.

## Configuration
Four key files form the basis of the openbox configuration, each serving a unique role. They are: , , , and . Although these files are discussed in more detail below, to start configuring Openbox, it will first be necessary to create a local Openbox profile (i.e for your specific user account) based on them. This can be done by copying them from the global  profile (applicable to any and all users) as a template:

 $ mkdir -p ~/.config/openbox
 $ cp -a /etc/xdg/openbox ~/.config/

## rc.xml
 is the main configuration file, responsible for determining the behaviour and settings of the overall session, including:

* Keyboard shortcuts (e.g. starting applications; controlling the volume)
* Theming
* Desktop and Virtual desktop settings, and
* Application Window settings

This file is also pre-configured, meaning that it will only be necessary to amend existing content in order to customise behaviour to suit personal preference.

## menu.xml
 defines the type and behaviour of the desktop menu, accessible by right-clicking the background. Although the default provided is a static menu (meaning that it will not automatically update when new applications are installed), it is possible to employ the use of dynamic menus that will automatically update as well.

The available options are discussed extensively below in the #Menus section.

## Autostart
 provides two autostart mechanisms: XDG Autostart (which only works if  is installed) and Openbox's own autostart mechanism.

Openbox's own autostart mechanism:

* sources
* sources
* runs
* runs

Issues regarding commands in  being executed out of order (or skipped altogether) are often resolved by the addition of small delays. For instance:

 xset -b
 (sleep 3s && nm-applet) &
 (sleep 3s && conky) &

In a standalone Openbox session, a Polkit authentication agent like the one provided by  can be launched from Openbox autostart. For example:

 (sleep 3s && /usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1) &

## environment
 can be used to export and set relevant environmental variables such as to:

* Define new pathways (e.g. execute commands that would otherwise require the entire pathway to be listed with them)
* Change language settings, and
* Define other variables to be used (e.g. the fix for GTK theming could be listed here)

## Themes
Install  and/or  for a GUI to configure visual settings and theming.

A good selection of themes are available in the  package or the AUR. Some GTK themes come with an Openbox theme as well. Both Openbox-specific and Openbox-compatible themes will be installed to the  directory and will also be immediately available for selection.

box-look.org is an excellent and well-established source of themes. deviantART.com is another excellent resource. Many more can be found online.

## Edit or create
The process of creating new or modifying existing themes is covered extensively at the official openbox.org website.  is a user-friendly GUI for doing so.

## GUI configuration
Several GUI applications are available to quickly and easily configure your Openbox desktop.

*
*
*
*
*

Programs and applications relating to the configuration of Openbox's desktop menu are discussed in #Menus.

## Openbox reconfiguration
Openbox will not always automatically reflect any changes made to its configuration files within a session. As a consequence, it will be necessary to manually reload those files after they have been edited. To do so, enter the following command:

 $ openbox --reconfigure

Where intending to add this command as a keybind to , it will only be necessary to list the command as . An example has been provided below, using the  keybind:

## Keyboard shortcuts
All keybinds must be added to the  file, and below the  heading. Although a brief overview has been provided here, a more in-depth explanation of keybindings can be found at openbox.org.

Keybinds can be added to the configuration file using the following syntax:

     ...

The action name for running an external command is Execute. Use the following syntax to define an external command to execute:

   my-command

See the Openbox wiki for a list of all available actions.

While the use of standard alpha-numeric keys for keybindings is self-explanatory, special names are assigned to other types of keys, such as ,  and .

## Modifiers
 keys play an important role in keybindings (e.g. holding down the  or  key in combination with another key to undertake an action). Using modifiers helps to prevent conflicting keybinds, whereby two or more actions are linked to the same key or combination of keys. The syntax to use a modifier with another key is:

 "-"

The modifier codes are as follows:

* : Shift
* : Control
* : Alt
* : Super
* : Meta
* : Hyper (If it is bound to something)

## Multimedia keys
Where available, it is possible to set the appropriate  keys to perform their intended functions, such as to control the volume and/or the screen brightness. These will usually be integrated into the  keys, and are identified by their appropriate symbols. See Keyboard input for details.

The volume and brightness multimedia codes are as follows (note that commands will still have to be assigned to them to actually function):

* : Increase volume
* : Decrease volume
* : Mute / unmute volume
* : Increase screen brightness
* : Decrease screen brightness

For a full list of XF86 multimedia keys, see LQWiki:XF86 keyboard symbols.

## Volume control
What commands should be used for controlling the volume will depend on whether ALSA, PulseAudio, or OSS is used for sound.

*ALSA: see Advanced Linux Sound Architecture#Keyboard volume control.
*PulseAudio: see PulseAudio#Keyboard volume control
*OSS: see OSS#Keyboard volume control.

## Navigation keys
These are the directional / arrow keys, usually used to move the cursor up, down, left, or right. The (self-explanatory) navigation codes are as follows:

* : Up
* : Down
* : Left
* : Right

## Menus
It is possible to employ three types of menu in Openbox: ,  (dynamic), and  (static or dynamic). They may also be used alone or in any combination.

## Static
As the name would suggest, this default type of menu does not change in any way, and may be manually edited and/or (re)generated automatically through the use on an appropriate software package.

Fast and efficient, while this type of menu can be used to select applications, it can also be useful to access specific functions and/or perform specific tasks (e.g. desktop configuration), leaving the access of applications to another process (e.g. the  or  applications).

The  file will be the sole source of static desktop menu content.

## menumaker
 automatically generates  menus for several window managers, including Openbox, Fluxbox, IceWM and Xfce. It will search for all installed executable programs and consequently create a menu file for them. It is also possible to configure MenuMaker to exclude certain application types (e.g. relating to GNOME or KDE), if desired.

Once installed and executed, it will automatically generate a new  file. To avoid overwriting an existing file, enter:

 $ mmaker -v OpenBox3

Otherwise, to overwrite an existing file, add the  argument ():

 $ mmaker -vf OpenBox3

Once a new  file has been generated it may then be manually edited, or configured using a GUI menu editor, such as .

## obmenu
 is a "user-friendly" GUI application to edit , without the need to code in .

## xdg-menu
 will automatically generate a menu based on  files contained within the  directory for numerous Window Managers, including Openbox. Review the Xdg-menu#Openbox article for further information.

## logout menu options
The  file can be edited in order to provide a sub-menu with the same options as provided by oblogout. The sample script below will provide all of these options, with the exception of the ability to lock the screen:

 			openbox --exit

 			systemctl poweroff

 		        systemctl reboot

 		        systemctl suspend

 		        systemctl hibernate

Once the entries have been composed, add the following line to present the sub-menu where desired within the main desktop menu (usually as the last entry):

## Pipes
This type of menu is in essence a script that provides dynamic, refreshed lists on-the-fly as and when run. These lists may be used for multiple purposes, including to list applications, to provide information, and to provide control functions. Pre-configured pipe menus can be installed, although not from the official repositories. More experienced users can also modify and/or create their own custom scripts. Again,  may and commonly will contain several pipe menus.

## Examples
* : Application and file browser
* wifi pipe menu: Wireless networking using Netctl

Openbox.org also provides a further list of pipe menus.

## Generators
This type of menu is akin to those provided by the taskbars of desktop environments such as Xfce or LXDE. Automatically updating on-the-fly, this type of menu can be powerful and very convenient. It may also be possible to add custom categories and menu entries; read the documentation for your intended dynamic menu to determine if and how this can be done.

A menu generator will have to be executed from the  file.

## obmenu-generator
 is highly recommended despite being an unofficial package. With the ability to be used as a static or dynamic menu, it is highly configurable, powerful, and versatile. Menu categories and individual entries may also be easily hidden, customised, and/or added with ease. The official homepage provides further information and screenshots.

Below is an example of how obmenu-generator would be dynamically executed without icons in :

To automatically iconify entries, the  option would be added:

## openbox-menu
 uses the LXDE menu-cache to create dynamic menus. The official homepage provides further information and screenshots.

## Menu icons
To show icons next to menu entries, it will be necessary to ensure they are enabled in the  section of the  file:

 yes

Where using a static menu, it will then be necessary to edit the  file to provide both the  command, along with the full path and icon name for each entry. An example of the syntax used to provide an icon for a category is:

If you are having problems with icons not showing in the menu then try converting them to .png

## Desktop menu as a panel menu
xdotool is a package that can issue commands to simulate key presses / keybinds, meaning that it is possible to use it to invoke keybind-related actions without having to actually press their assigned keys. As this includes the ability to invoke an assigned keybind for the Openbox desktop menu, it is therefore possible to use XDoTool to turn the Openbox desktop menu into a panel menu. Especially where the desktop menu is heavily customised and feature-rich, this may prove very useful to:

* Replace an existing panel menu
* Implement a panel menu where otherwise not provided or possible (e.g. for Tint2)
* Compensate where losing access to the desktop menu due to the use of an application like  to manage the desktop.

Once XDoTool has been installed - if not already present - it will be necessary to create a keybind to access the root menu in , and again below the  heading. For example, the following code will bring up the menu by pressing :

        root-menu

Openbox must then be reconfigured. In this instance, XDoTool will be used to simulate the  keypress to access the desktop menu with the following command (note the use of  in place of ):

 xdotool key control+m

How this command may be used as a panel launcher / icon is largely dependent on the features of panel used. While some panels will allow the above command to be executed directly in the process of creating a new launcher, others may require the use of an executable script. As an example, a custom executable script called  will be created in the  directory and the appropriate XDoTool command is added to the file (to simulate the  keypress in this example):

After the file has been saved and closed, it may then be made into an executable script.

Executing it will bring up the Openbox desktop menu. Consequently, where using a panel that supports drag-and-drop functionality to add new launchers, simply drag the executable script onto it before changing the icon to suit personal taste.

## XDG compliant menu
A xdg compliant menu is based on the freedesktop.org standard. The menu is defined in menu-files which reside in . New applications will occur automatically in the menu.

## Example
The  package provides an Arch Linux specific XDG-compliant menu.

## Tips and tricks
## Cursor and icon themes
See Cursor themes and Icons for details.

## Desktop icons and wallpapers
Openbox does not natively support the use of desktop icons or wallpapers.

See PCManFM, SpaceFM and Idesk.

See List of applications/Other#Wallpaper setters.

## Compositing effects
Openbox does not provide native support for compositing, and thus requires an external compositor for this purpose.

Although compositing is not a necessary component, it may specifically avoid issues such as screen distortion with oblogout, and visual glitches with terminal window transparency. See Xorg#List of composite managers for common choices.

## oblogout
See the Oblogout article for an overview on how to use this useful, graphical logout script.

## Launch a complex command with hotkey
If you need to execute a complex command, use shell functionality.

When writing your own scripts, make sure to escape xml special characters, such as "" ("&amp;amp;"), "" ("&amp;gt;") and other (see more on Predefined entities in XML).

This example will turn off display immediately and lock screen with . It was taken from this thread.

      sh -c 'slock &amp;amp; (sleep .5 &amp;amp;&amp;amp; xset dpms force off)'

Sometimes one need to specify environment variable for application:

      sh -c "LC_ALL=C.UTF-8 obconf-qt"

Another example will launch application preserving all stdout and stderr output to file:

      sh -c sh -c "exec gimp &amp;gt;/tmp/gimp.out 2&amp;gt;&amp;amp;1"

Enable screenshot:

      gnome-screenshot --clipboard

      gnome-screenshot --clipboard --window

      gnome-screenshot --interactive

## Application launchers
Given the lack of a desktop environment with a plain Openbox install, it can be useful to install one or more application launchers as supplements to the Openbox menu system and the hotkeys.  Lists of such launchers can be found at Application launchers and List of applications/Other#Application launchers; popular examples are Gmrun and dmenu.

## Switch desktops using the mouse
It is possible to switch desktop by moving the mouse cursor to the edges of the screen. First install  and add the following two lines to your :

 xdotool behave_screen_edge --delay 500 left set_desktop --relative -- -1 &
 xdotool behave_screen_edge --delay 500 right set_desktop --relative -- +1 &

## Set default applications / file associations
See the Default applications article.

## Ad-hoc window transparency
The program  can enable window transparency on-the-fly.

For example, using the following code in the  section of the  file will enable control of application window transparency by hovering the mouse-pointer over the title bar and scrolling with the middle button:

     ...

         transset-df --point .2 --inc

         transset-df --point .2 --dec

     ...

## Using obxprop for faster configuration
The  package provides a  binary that can parse relevant values for applications settings in . Officially  is recommended for this task. Start the process by running the command shown, then click a window to see its properties in the terminal.

## Xprop values for applications
 can be used to relay property values for selected applications. Where frequently using per-application settings, the following Bash Alias may be useful:

 alias xp='xprop | grep "WM_WINDOW_ROLE\|WM_CLASS" && echo "WM_CLASS(STRING) = \"NAME\", \"CLASS\""'

To use Xorg-XProp, run using the alias given , and click on the active program desired to define with per-application settings. The results displayed will only be the information that Openbox itself requires, namely the  and  (name and class) values:

 WM_WINDOW_ROLE(STRING) = "roster"
 WM_CLASS(STRING) = "gajim.py", "Gajim.py"
 WM_CLASS(STRING) = "NAME", "CLASS"

## Switching between keyboard layouts
See the article section switching between keyboard layouts for instructions.

## Set grid layout for virtual desktops
Install . To set a 2x2 grid for example:

 obsetlayout 0 2 2 0

Run it without arguments to know what the arguments mean.

## Enable Hot Corners
 provides hot corners for openbox and other lightweight window managers. Start the application with a entry in the autostart-file:

 lead &

Commands can be edited in the configuration file  (replace  with the name of your screen output, which you can find out using xrandr):

 bottom=
 bottomLeft=chromium
 bottomRight=thunar
 left=
 right=
 top=
 topLeft=mlde.californium toggle
 topRight=skippy-xd

For more information see [https://github.com/MageJohn/lead.

## Window snapping
Many desktop environments and window managers support window snapping (e.g. Windows 7 Aero snap), whereby they will automatically snap into place when moved to the edge of the screen. This effect can also be simulated in Openbox through the use of keybinds on focused windows.

As illustrated in the example below, percentages must be used to determine window sizes (see openbox.org for further information). In this instance, The  key is used in conjunction with the  keys:

     50%
     0
     0

     50%
     50%
     0

However, it should be noted that once a window has been 'snapped' to an edge, it will remain vertically maximised unless subsequently maximised and then restored. The solution is to implement additional keybinds - in this instance using the  and  keys - to do so. This will also make pulling 'snapped' windows from screen edges faster as well:

This Ubuntu forum thread provides more information. Applications such as  are also available to automatically simulate window snapping behaviour without the use of keybinds.
Another option is to use  which provides  and  commands which will snap active window on left or right edge respectively if it is not snapped and restore it to original size and position otherwise. Just bind these commands to the key combination of your choosing.

The example below will give you quarter window tiling in each corner of the screen using the alt key in combination with the navigation keys

     0
     0
     50%
     50%

     50%
     0
     50%
     50%

     0
     50%
     50%
     50%

     50%
     50%
     50%
     50%

## Smooth display manager transition
Users of display managers might experience a flickering during the transition between the display manager and the Openbox desktop. The flickering comes from Openbox setting the root window's color during startup. Therefore there is a brief moment when the display flashes in a grey color, between the display manager's background and the desktop's wallpaper.

Setting the root window's background color can be disabled by editing the Openbox startup script found in . Simply comment out (or delete) the block starting with .

## Window decorations
To remove window decorations for all or particular applications, use the  option in the  section of  (user:  or system: ).

Using Firefox as an example (including variants like Firefox-Beta and Firefox-Nightly):

    no

One could also disable decorations for all applications (using class ), then enable them (using ) for individual ones. To apply the changes, restart your desktop session, and thus Openbox. Reference: Openbox FAQ

## Troubleshooting
## Firefox
Mozilla based browsers may ignore application rules (e.g. ) unless  is used. See #Xprop values for applications.

## Missing themes
If for any reason the newly extracted theme cannot be selected, open the theme directory to first ensure that it is compatible with Openbox - there should be an  directory and a  file within it. An  (OpenBox Theme) file may also be present in some instances, which can then be manually loaded in .

A theme may also be not accessible due to wrong permissions. See File permissions and attributes for more.

## Stop continuous desktop switching
By default Openbox switches from the last desktop back to the first desktop on mouse wheel scroll. Use  in the  section to disable this behaviour.

          previous
          no

          next
          no

## Windows load behind the active window
Some application windows (such as Firefox windows) may load behind the currently active window, causing you to need to switch to the window you just created to focus it. To fix this behavior add this to your  file, inbetween the  and  tags:
