# Tint2

tint2 is a simple, unobtrusive and light panel for Xorg. It can be configured to include a system tray, a task list, a battery monitor and more. Its look is configurable and it only has few dependencies, making it ideal for window managers like Openbox, that do not come with a panel.

## Installation
Install the  package.

## Configuration
tint2 has a configuration file in . A skeleton configuration file with the default settings is created the first time you run tint2. You can then change this file to your liking. Full documentation on how to configure tint2 is found here. You can configure the fonts, colors, looks, location and more in this file. The tint2 package also contains a GUI configuration tool which can be launched with tint2conf.

## Application launchers
With version 0.12, it has become possible to add application launchers to tint2. It is necessary to add the following configuration options to your tint2 configuration file:

Under :

 # Panel
 panel_items = LTSBC

And under the new section :

 # Launchers
 launcher_icon_theme = LinuxLex-8
 launcher_padding = 5 0 10
 launcher_background_id = 9
 launcher_icon_size = 85
 launcher_item_app = /some/where/application.desktop
 launcher_item_app = /some/where/anotherapplication.desktop

 is a new configuration option which defines which items tint2 shows and in what order:

; L: shows the Launcher
; T: shows the Taskbar
; S: shows the Systray (also called notification area)
; B: shows the Battery status
; C: shows the Clock
; F: adds an extensible spacer (freespace). You can specify more than one. Has no effect if `T` is also present. (since 0.12)
; E: adds an executor plugin. You can specify more than one. (since 0.12.4)
; P: adds a push button. You can specify more than one. (since 0.14)
; :: adds a separator. You can specify more than one. (since 0.13.0)

## Applications menu in Openbox
Since version 0.12, you have the ability to create launchers. Unfortunately, tint2 does not support nested menus yet, so there is no native function to enable an applications menu. This section describes a way to create a launcher for Openbox.

Besides tint2 and Openbox, install the  package. Next, create a keybinding for opening the Openbox menu:

This will set  to open the root-menu (this is the menu that opens when you right-click the desktop). You can change  to any menu-id that you have defined in . Next we need to make that keybinding into a  file with . First test that your keybind works with:

 $ xdotool key ctrl+alt+space

If the menu you chose pops up under your mouse cursor, you have done it right! Now create a  file inside the  directory. Add the line  where  are your chosen key combinations. Open your new  file from your file manager and, once again, you should see the menu appear under your cursor. Now just add this to tint2 as a launcher, and you have your Openbox Applications Menu as a launcher for tint2. If you need to place the menu at a fixed position, you can use . You can create a script and reference it in  since it involves two commands.

See Openbox Menus for further help on creating your own menu to use here, and  to generate a nice full  for most (possibly all) of your installed programs.

Since version 0.14, you have the ability to create buttons. Just add "xdotool key ctrl+alt+space" string from example above to button key action you want to be start menu action.

## Volume control
tint2 does not come with a volume control applet. See List of applications/Multimedia#Volume control.

## Running tint2
## Openbox
You can run tint2 by simply typing the command:

 $ tint2

If you want to run tint2 when starting Openbox, you will need to edit  and add the following line:

 tint2 &

## GNOME
In GNOME, the Activities view has replaced the bottom panel and taskbar. To use tint2 in its place, run

 $ gnome-session-properties

and add  as an application to run on start-up. The next time GNOME starts, tint2 will run automatically.

## i3
In i3, to use tint2 as a replacement for , append the following line to end of the i3 configuration file:

and comment out or remove any section like {{ic|bar{status_command i3status}}} from the same file.

## Multiple panels
Multiple tint2 panels can be simultaneously running by executing tint2 with different configuration files:

 tint2 -c path/to/first/config/file
 tint2 -c path/to/second/config/file

## Enabling transparency
tint2 supports both fake and real transparency. Which one is used is regulated by the  option in the  configuration file.

If you want to completely disable transparency you need to use  and set the panel background opacity to 100. Eg:

  background_color = #000000 100

## Fake transparency
For fake transparency you need to set .

Fake transparency captures a portion of the desktop background and uses that as the panel background. Because of that it is important to set the background image before tint2 is activated. A startup script example for Openbox could be (using Feh for the background):

 ...
 feh --randomize --no-fehbg --bg-fill ~/Pictures/wallpapers/
 (sleep 1 && tint2) &
 ...

## Real transparency
For real transparency you need to activate a compositor like picom first and set .

The opacity is regulated by the second parameter of the  property in the tint2 configuration file.

If you are making changes on the fly, you may need to restart tint2 for the transparency to take effect.

## Fullscreen/Overlay
To force tint2 to stay on top of the application (overlay), you need to set the panel_layer option appropriately. This can be helpful when you switch from a fullscreen window to a normal application using . There is a discussion on this at Crunchbang Forum

  #Panel
  panel_layer = top
  strut_policy = follow_size

## Third party extensions
It is also possible to extend tint2 with other applications. To add third party extensions, check the Applets section of official Wiki.
