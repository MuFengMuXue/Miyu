# PekWM

pekwm is a X window manager written by Claes Nästen. The code is based on the aewm++ window manager, but it has evolved enough that it no longer resembles aewm++ at all. It also has an expanded feature-set, including window grouping (not unlike to pwm, or even fluxbox), auto properties, xinerama and keygrabber that supports keychains, and much more.

## Installation
Install the  package.

## Starting
Run  with xinit.

## Configuring PekWM
The main configuration file is stored in the file . It controls the workspace and viewports settings, the menu and harbour behaviour, window edge resistance, and more. There is an example file with complete documentation in the pekwm documentation.

## Menus
PekWM comes with pre-created menus by default stored in . These do not reflect an existing system and as such are likely to be inaccurate. These should be seen as an example only.

## MenuMaker
One way to automatically set up menus for your installed applications is . To set up menus of all your installed applications run it with the following command:

 mmaker --no-desktop pekwm

To see a full list of options, run

Now you can modify the menu file by hand, or simply regenerate the list whenever you install new software.

## Manually
The menu file is . The syntax is fairly straightforward; a simple entry has the following structure:

 Entry = "NAME" { Actions = "Exec COMMAND" }

A submenu has the following syntax:

 Submenu = "NAME" {
      Entry = "NAME" { Actions = "Exec COMMAND" }
      Entry = "NAME" { Actions = "Exec COMMAND" }
 }

To add a separator line to the menu, use the following:

 Separator {}

PekWM also supports dynamic menus. These are menu entries or submenus that display the output of a run script every time the entry or submenu is accessed. Check the exact syntax each menu requires, as they may vary.

You can find dynamic menus for Gmail and network connections, and one to display the time and date.

There used to be a project called pekwm_menu_tools which aimed to be a set of useful applications for generating dynamic menus for pekwm.

## Hotkeys
The hotkey settings are stored in . This file controls all the keyboard bindings and keychains used in PekWM. You can add keyboard bindings to launch programs or to perform actions in PekWM, such as show a menu, move a window, switch desktops, etc. For a full list of pekwm's actions, see the documentation.

You can have more than one action assigned to one key combination. To do so, just separate the actions by a semicolon. Here is an example:

 KeyPress = "Ctrl Mod1 R" { Actions = "Exec osdctl -s 'Reconfiguring'; Reload" }

When you press Ctrl+Alt+R Pekwm will display on the screen the text 'Reconfiguring' (osdctl -s 'Reconfiguring') and reconfigure (Reload). (Note that this requires osdsh to be installed)

The next example will bind a media key to lower the volume:

 KeyPress = "XF86AudioLowerVolume" { Actions = "exec amixer set Master 5%- unmute" }

You can also do "chains" of keys, so for example the code

 Chain = "Ctrl Mod1 C" {
      KeyPress = "Q" { Actions = "MoveToEdge TopLeft" }
      KeyPress = "W" { Actions = "MoveToEdge TopCenterEdge" }
 }

Would make it so that if you first press  and then  you move the active window to the top left corner of the screen, and if you press  and then  you move the window to the top center edge.

## Mouse
The Mouse settings are stored in . This file is also rather self-explanatory in its layout. For example:

 FrameTitle {
      ButtonRelease = "1" { Actions = "Raise; Focus" }
 }

means that if you release button 1 (usually left mouse button) over the frame title of a window the window will be "Raised" above the other windows and it will become the focused window.

One of the things PekWM is set up to do by default is to focus windows when the mouse moves over them (as opposed to the "click to focus" style). This is one thing that quite a few users would like to change to the more "traditional" way. To change this, look for the following lines in the file and do what they say (there are quite a few of the first, but only one occurrence of the second):

 # Remove the following line if you want to use click to focus.
 # Uncomment the following line if windows should raise when clicked.

## Autostart
The autostart file is . If you would like to display a wallpaper or launch a panel whenever Pekwm is started, you can add entries for these things in that file. Note, though, that these applications are run every time Pekwm is started -- including when you run Restart in the root menu. The commands are executed only after Pekwm is started.

To add an application, use the following structure:

 nameofapplication &

The & at the end is crucial, or anything after it will not be run. Here is an example:

 xfce4-panel &
 conky &
 hsetroot -fill ~/images/darkwood.jpg &

Before you can use this file, you will have to make it executable.

## Variables
The Variables file contains the general variables used in PekWM, the default entry should explain it quite clearly:

 $TERM="xterm -fn fixed +sb -bg white -fg black"

Whenever the variable $TERM is used in any of PekWM's configuration files, the command xterm -fn fixed +sb -bg white -fg black will be run. For example changing it to:

 $TERM="urxvt"

would mean that urxvt would be loaded for terminal commands.

## Autoproperties
If you would like certain applications to open on certain workspaces, have a certain title, skip the (window) menus, or be automatically tabbed together, you can specify all that here. It is probably the most confusing configuration file in PekWM, but it is also the most powerful file. The amount of things that can be set in this file are far too great to fit here, but it is explained in detail in the autoproperties page of the documentation. The default  file also contains a crash course to autopropping.

## Themes
A collection of themes for pekwm is available on the official homepage a more comprehensive list of themes is available at [https://www.box-look.org/browse/cat/141/ord/latest/ Box-Look.org but they are not always verified against the current version of pekwm.

To install a theme, extract the theme archive to one of the theme paths:

* global:
* user only:

## Setting a wallpaper
With the release pekwm 0.2.0 a background setting application is included named .

Setting a scaled background image:

 $ pekwm_bg Image image.png#scaled

Setting 3 horizontal lines:

 $ pekwm_bg LinezHors 33% #afadbf #9f9daf #afadbf

pekwm 0.1.X releases did not come with a background setting application and required you to use a separate program to set a desktop wallpaper. See List of applications/Other#Wallpaper setters.

## Troubleshooting
## When using Nvidia TwinView, windows maximize across both screens
Edit  and look for the line:

 HonourRandr = "True"

and change it to

 HonourRandr = "False"

## Scrolling does not work in GTK 3 applications
Try setting the environment variable . See pekwm issue #4.
