# Cinnamon

Cinnamon is a desktop environment which combines a traditional desktop layout with modern graphical effects. The underlying technology was forked from the GNOME desktop. As of version 2.0, Cinnamon is a complete desktop environment and not merely a frontend for GNOME like GNOME Shell and Unity.

## Installation
Cinnamon can be installed with the package .

## Cinnamon applications
Cinnamon introduces X-Apps which are based on GNOME Core Applications but are changed to work across Cinnamon, MATE and XFCE; they have the traditional user interface (UI).

{| class="wikitable"
! Application
! GNOME
! Cinnamon
|-
| Text editor
| Gedit/Pluma
|
|-
| Image viewer
| Eye of GNOME
|
|-
| Document viewer
| Evince/Atril
|
|-
| Media player
| Totem
|
|-
| Image organizer
| gThumb
|
|}

## Fallback mode
On the event when Cinnamon crashes, its Fallback mode activates. To control opened windows in this mode, you need to install  package and  to have a taskbar.

## Starting
## Graphical log-in
Choose Cinnamon or Cinnamon (Software Rendering) from the menu in a display manager of choice. Cinnamon is the 3D accelerated version, which should normally be used. If you experience problems with your video driver (e.g. artifacts or crashing), try the Cinnamon (Software Rendering) session, which disables 3D acceleration.

## Starting Cinnamon manually
If you prefer to start Cinnamon manually from the console, add the following line to Xinitrc:

If the Cinnamon (Software Rendering) session is required, use  instead of .

## Restarting Cinnamon
The following needs to be executed as the user the Cinnamon instance is running under:

 $ cinnamon-dbus-command RestartCinnamon 1

To restart Cinnamon from outside a dbus session, you can use something like this:

 $ DBUS_SESSION_BUS_ADDRESS="unix:path=/run/user/${TARGET_USER_UID}/bus"
 $ sudo -u "#${TARGET_USER_UID}" -H dbus-send --bus=$DBUS_SESSION_BUS_ADDRESS --type=method_call --dest=org.Cinnamon /org/Cinnamon org.Cinnamon.RestartCinnamon boolean:true 2> /dev/null

## Configuration
Cinnamon is quite easy to configure — most common settings can be configured graphically. Its usability can be expanded with applets and extensions, and also it supports theming.

## Cinnamon settings
cinnamon-settings launches a settings module specified on the command line. Without (correct) arguments, it launches System Settings. For example, to start the panel settings:

 $ cinnamon-settings panel

To list all available modules:

 $ pacman -Ql cinnamon | grep -Po '(? Hardware > Keyboard > Layouts''.

## Use a different window manager
Cinnamon does not support using a different window manager.

## Tips and tricks
## Creating custom applets
The official tutorial on creating a Cinnamon applet can be found here.

## Default desktop background wallpaper path
When you add a wallpaper from a custom path in Cinnamon Settings, Cinnamon copies it to . Thus, with every change of your wallpaper, you would have to add your updated wallpaper again from the settings menu or copy / symlink it manually to .

Additionally, the official mint wallpapers are available for every release. Checkout the AUR.

## Show home, filesystem desktop icons
By default, Cinnamon starts with desktop icons enabled but with no desktop icons on screen. To show desktop icons for the home folder, the filesystem, the trash, mounted volumes and network servers, open Cinnamon settings and click on desktop. Enable the checkboxes of the icons you want to see on screen.

## Menu editor
The Menu applet supports launching custom commands. Right click on the applet, click on Configure... and then Open the menu editor. Select a sub-menu (or create a new one) and select New Item. Set Name, Command and Comment. Check the launch in terminal checkbox if needed. Leave unchecked for graphical applications. Click OK and close the menu editor afterwards. The launcher is added to the menu.

## Workspaces
A workspace pager can be added to the panel. Right click the panel and choose the option Add applets to the panel. Add the Workspace switch applet to the panel. To change its position, right click on the panel and change the Panel edit mode on/off switch to on. Click and drag the switcher to the desired position and turn the panel edit mode off when finished.

By default, there are 2 workspaces. To add more, hit  to show all workspaces. Then click on the plus sign button on the right of the screen to add more workspaces.

Alternatively, you can choose the number by command-line:

 $ gsettings set org.cinnamon.desktop.wm.preferences num-workspaces 4

Replacing 4 with the number of workspaces you want.

## Hide desktop icons
The desktop icons rendering feature is enabled in Nemo by default. To disable this feature, change the setting with the following command:

 $ gsettings set org.nemo.desktop show-desktop-icons false

## Themes, icons and backgrounds
Linux Mint styled themes, icons and backgrounds can be installed with the , , , ,  and  packages. Whereby the latter is a collection of all backgrounds included in all Linux Mint Versions. Backgrounds of individual Linux Mint versions are also available over the AUR.

The themes and icons can be edited in Settings > Themes. The backgrounds in Settings > Backgrounds.

Setting the desktop theme via shell can be done like this:

 $ gsettings set org.cinnamon.theme name "Theme-Name"

## Sound events
Cinnamon does not come with sounds used for events like the startup of the desktop that are also used in Linux Mint by default. These sound effects can be installed with the  package. The sound events can be edited in Settings > Sound > Sound Effects.

## Resize windows by mouse
To resize windows with , use :

 gsettings set org.cinnamon.desktop.wm.preferences resize-with-right-button true

## Portable keybindings
To export your keyboard shortcut keys:

 $ dconf dump /org/cinnamon/desktop/keybindings/ > keybindings-backup.dconf

To later import it on another device:

 $ dconf load /org/cinnamon/desktop/keybindings/  Preferences > Keyboard under Shortcuts > System > Screenshots and Recording''. The default save directory is , but can be customized with eg.

 $ gsettings set org.gnome.gnome-screenshot auto-save-directory file:///home/USER/some_path

## Prevent Cinnamon from overriding xrandr/xinput configuration
The cinnamon-settings-daemon provides a number of plugins which can manage the display, keyboard and mouse. These plugins will override user set configuration (such as xrandr commands in the xinitrc file). To stop user set configuration from being overridden, it is necessary to prevent the settings daemon plugins from being started.

This can be done by copying the .desktop entry for the relevant settings daemon plugin (these will be located in ) to . Then append the line  to each copied entry.

To preserve display, keyboard and mouse settings, consider disabling the following:

 cinnamon-settings-daemon-a11y-keyboard.desktop
 cinnamon-settings-daemon-a11y-settings.desktop
 cinnamon-settings-daemon-keyboard.desktop
 cinnamon-settings-daemon-mouse.desktop
 cinnamon-settings-daemon-xrandr.desktop

## Troubleshooting
## Debugging
You can use the  tool (Melange - Cinnamon Debugger) to inspect various things about the Cinnamon environment:

* a list of currently-open windows
* a list of currently-loaded extensions (applets, desklets, etc.)
* logs

The "logs" feature is especially useful if you are encountering crashes (often happening due to extensions no being compatible or buggy).

## cinnamon-settings: No module named Image
If cinnamon-settings does not start with the message that it cannot find a certain module, e.g. the Image module, it is likely that it uses outdated compiled files which refer to no longer existing file locations. In this case, remove all  files in  and its sub-folders. See the upstream bug report.

## Starting Cinnamon from tty after crash
If Cinnamon is completely unresponsive, it can be restarted from the TTY () with:

 $ cinnamon --replace -d :0 &

## Video tearing
Because  is based upon , video tearing fixes for GNOME should also work in Cinnamon. See GNOME/Troubleshooting#Tear-free video with Intel HD Graphics for more information.

## Disable the NetworkManager applet
Even if you do not use NetworkManager and remove the Network Manager applet from the default panel, Cinnamon will still load nm-applet and display it in the system tray.
You cannot uninstall the package because it is required by  and , but you can still easily disable it. To do so, copy the autostart file from  to . Open it with your favorite text editor and add at the end .

Alternatively, you can disable it by creating the following symlink:

 $ ln -s /bin/true /usr/local/bin/nm-applet

The ability to blacklist particular icons from the system tray (such as the nm-applet icon) has been requested upstream.

## Cinnamon overrides settings in xorg.conf
Cinnamon overrides custom settings in xorg.conf like display orientation and layout.

Open  and set Cinnamon Settings Daemon - xrandr to OFF.

## No prompt for root password when launching applications that require root permissions
Cinnamon uses Polkit to allow a non-root user to elevate their permissions in order to launch applications that require root permissions (such as Timeshift or GParted).
Polkit requires this user to be part of the wheel group.
If your user is not part of the wheel group, you may not receive the prompt for the root password when launching an application that requires root permissions (and thus the application will not be launched).
