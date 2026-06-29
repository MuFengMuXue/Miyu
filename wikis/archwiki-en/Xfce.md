# Xfce

Xfce is a lightweight and modular desktop environment based on GTK. To provide a complete user experience, it includes a window manager, a file manager, desktop and panel.

## Installation
Install the  group. You may also wish to install the  group which includes extra plugins and a number of useful utilities such as the  editor. Xfce uses the Xfwm window manager by default.

## Starting
Choose Xfce Session from the menu in a display manager of choice, or add  to Xinitrc.

## Configuration
Xfce stores configuration options in Xfconf. There are several ways to modify these options:

* In the main menu, select Settings and the category you want to customize. Categories are programs usually located in  and .
*  can see and modify all settings. Options modified here will take effect immediately. Use  to change settings from the commandline; see the documentation for details.
* Settings are stored in XML files in  which can be edited by hand. However, changes made here will not take effect immediately.

## Menu
See Xdg-menu for more info on using the Free Desktop menu system.

## Whisker menu
 (also part of ) is an alternative application launcher. It shows a list of favorites, browses through all installed applications through category buttons, and supports fuzzy searching. After package being installed, it can replace Applications Menu as first item in Panel 1 (in Settings > Panel > Items add Whisker Menu).

## Set keyboard shortcut to launch whisker menu
To set a keyboard shortcut to launch the whisker menu, go to Settings > Keyboard and then the Application Shortcuts tab. Click on the Add button, set the command to  and assign the desired keyboard shortcut.

## Edit entries
A number of graphical tools are available for this task:

* .
*
*

Alternatively, create the file  manually. See the example configuration below:

     Xfce
     /etc/xdg/menus/xfce-applications.menu

         xfce4-run.desktop
         exo-terminal-emulator.desktop
         exo-file-manager.desktop
         exo-mail-reader.desktop
         exo-web-browser.desktop
         xfce4-about.desktop
         xfhelp4.desktop

         Settings

         xfce4-session-logout.desktop

The  tag includes the default Xfce menu.

The  tag excludes applications which we do not want to appear in the menu. Here we excluded some Xfce default shortcuts, but you can exclude  or any other application.

The  tag defines the layout of the menu. The applications can be organized in folders or however we wish. For more details see the Xfce wiki.

You can also make changes to the Xfce menu by editing the  files themselves. To hide entries, see Desktop entries#Hide desktop entries. You can edit the application's category by modifying the  line of the desktop entry, see Desktop entries#Example .desktop file.

## Set preferred applications
To change the default applications used for opening certain resources, use the Preferred Applications setting. This will change the behavior of , which is invoked by resource openers such as xdg-open.

## Desktop
## Remove desktop icons
Issue the following command:

 $ xfconf-query -c xfce4-desktop -v --create -p /desktop-icons/style -t int -s 0

To reinstate icons on the desktop, issue the same command with a value of 2.

## Kill window shortcut
Xfce does not have a shortcut to kill a window, for example when a program freezes.

With , use  to interactively kill a window. For the currently active window, use :

 $ xdotool getwindowfocus windowkill

Alternatively:

 $ sh -c "xkill -id $(xprop -root -notype | sed -n '/^_NET_ACTIVE_WINDOW/ s/^.*# *\|\,.*$//g p')"

To add the shortcut, use Settings > Keyboard or an application like .

## Session
## Autostart
To launch custom applications when Xfce starts up, click the Applications Menu > Settings > Settings Manager and then choose the Session and Startup option and click the tab Application Autostart.
You will see a list of programs that get launched on startup. To add an entry, click the Add button and fill out the form, specifying the path to an executable you want to run.

Autostart application location paths are described in the XDG Autostart specification.

Alternatively, add the commands you wish to run (including setting environment variables) to xinitrc (or xprofile when a display manager is being used).

## Lock the screen
xflock4 is the reference Shell script which is used to lock an Xfce session.

It tries to lock the screen with these screen lockers in the specified order:

*  (also part of )
*
*
* Screen lockers providing the  D-Bus method (e.g. )
*  from
*

It exits with return code 1 if it fails to find any of these.

The List of applications/Security#Screen lockers contains a short description of these screen lockers together with other popular applications.

To have xflock4 run a custom session locker, set  in the session's xfconf channel to the command line to be used:

The panel lock button in the Action Buttons panel simply executes . It should work as expected as long as xflock4 is functioning i.e. one of the native lockers is installed or a custom locker is configured to integrate with it as proposed above.

## Suspend
Whether or not the session is systematically locked on suspend can be configured through the xfconf properties or from the GUI.

To prevent locking on suspend using the CLI, turn  to :

 $ xfconf-query -c xfce4-power-manager -p /xfce4-power-manager/lock-screen-suspend-hibernate -s false

Similarly, turn it to  to lock the session on suspend.

The setting can also be controlled from the GUI: open the Session and Startup application and turn the flag General > Lock screen before sleep on or off.

Whenever the suspend keyboard button is pressed, it can be handled by either Xfce's power manager or by systemd-logind. To give precedence to logind, the following xfconf setting must be set to :

 $ xfconf-query --create -c xfce4-power-manager -p /xfce4-power-manager/logind-handle-suspend-key -t bool -s true

## Disable saved sessions
Per user, saved sessions can be disabled by unchecking Applications > Settings > Session and Startup > General > Automatically save session on logout or by executing the following command:

 $ xfconf-query --create -c xfce4-session -p /general/SaveOnExit -t bool -s false

Alternatively, Xfce kiosk mode can be used to disable the saving of sessions systemwide. To disable sessions, create or edit the file  and add the following:

 SaveSession=NONE

You may need to remove previously saved sessions. Navigate to Applications > Settings > Session and Startup > Saved Sessions and press the Clear Saved Sessions button, or simply delete the  directory.

## Use a different window manager
The files specifying the default window manager are found in the following locations:
* - per user
* - systemwide

The default window manager for the user can be set easily using xfconf-query:
 $ xfconf-query -c xfce4-session -p /sessions/Failsafe/Client0_Command -t string -sa xfsettingsd
 $ xfconf-query -c xfce4-session -p /sessions/Failsafe/Client1_Command -t string -sa wm_name

If you want to start the window manager with command line options, see the commands below:
 $ xfconf-query -c xfce4-session -p /sessions/Failsafe/Client0_Command -t string -sa xfsettingsd
 $ xfconf-query -c xfce4-session -p /sessions/Failsafe/Client1_Command -t string -s wm_name -t string -s --wm-option
If you need more command line options, simply add more  and  arguments to the command.

If you want to change the default window manager systemwide, edit the file specified above manually, changing xfwm4 to the preferred window manager and adding more  lines for extra command line options if needed.

You can also change the window manager by autostarting  using the autostart facility or by running  in a terminal and making sure the session is saved on logout. Be aware though that this method does not truly change the default manager, it merely replaces it at login. Note that if you are using the autostart facility, you should disable saved sessions as this could lead to the new window manager being started twice after the default window manager.

## Theming
XFCE themes are available at [https://www.xfce-look.org xfce-look.org. Xfwm themes are stored in , and set in Settings > Window Manager. GTK themes are stored in  and  and are set in Settings > Appearance.

To achieve a uniform look for all applications, see Uniform look for Qt and GTK applications.

See also Cursor themes, Icons, and Font configuration.

## Consistent Look Between SSD and CSD Windows
Xfce currently uses Server-Side Decorations (SSD) (see Wikipedia:Window decoration) themed by Xfwm for most windows and Client-side decoration (CSD) themed by the respective programs for Xfce Settings, Print, Save, and other dialogs.

Xfwm SSD window styles can be themed to match the CSD windows by manually adjusting or creating themes in  or by using a tool such as  which "Creates xfwm4 themes from client side decorations."

## Reverting Client-Side Decorations
With Xfce 4.18, client-side decorations are optional and disabled by default. Non-Xfce applications may still use client-side decorations. To disable them globally, see GTK#Client-side decorations.

## Sound
## Sound themes
XFCE4 supports [https://www.freedesktop.org/wiki/Specifications/sound-theme-spec/ freedesktop system sounds, but it is not configured out of the box.

To enable a sound theme:

# Check Enable event sounds in Settings > Appearance > Settings;
# In the Settings Editor set  to a sound theme located in ;
# Turn on System Sounds in audio mixer (e.g. ).

 provides a compatible sound theme, but it lacks many required events. A better choice is  ( should be ).

## Keyboard volume buttons
 provides a panel applet which has support for keyboard volume control and volume notifications. As an alternative, you can install , which also provides keybinding and notification control, but without an icon sitting in the panel. This is handy, for example, when using  at the same time for a finer control.

Alternatively,  also provides a panel applet and keyboard shortcuts. The Arch package only supports ALSA, but you can rebuild it manually to add PulseAudio support.

After installing the panels, you have to add it to the taskbar or the keyboard shortcuts will not work.

For non desktop environment specific alternatives, see List of applications/Multimedia#Volume control.

## Shortcuts
If you are not using an applet or daemon that controls the volume keys, you can map volume control commands to your volume keys manually using Xfce's keyboard settings. For the sound system you are using, see the sections linked to below for the appropriate commands.

* ALSA: see Advanced Linux Sound Architecture#Keyboard volume control.
* PulseAudio: see PulseAudio#Keyboard volume control.
* OSS: see OSS#Keyboard volume control.

## Keyboard shortcuts
Keyboard shortcuts are defined in two places: Settings > Window Manager > Keyboard, and Settings > Keyboard > Shortcuts.

## Polkit Authentication Agent
The  agent will be installed along with  and autostarted automatically; no user intervention is required. For more information, see Polkit#Authentication agents.

A third party polkit authentication agent for Xfce is also available, see  or .

## Display blanking
Some programs that are commonly used with Xfce will control monitor blanking and DPMS (monitor powersaving) settings. They are discussed below.

;Xfce Power Manager
Xfce Power Manager controls DPMS settings only. They can be configured in the Power Manager GUI within the Display tab.

Note that when Display power management is turned off, DPMS is fully disabled, but this does not mean that Power Manager will simply stop controlling DPMS. However, it does not control screen blanking, which may remain enabled even after display power management is disabled. To disable both blanking and DPMS, right click on the power manager system tray icon or left click on the panel applet and make sure that the option labelled Presentation mode is ticked.

;XScreenSaver
If  is installed and runs alongside Xfce Power Manager, it may not be clear which application is in control of blanking and DPMS as both are competing for control of the same settings. Therefore, in a situation where it is important that the monitor not be blanked (when watching a video for instance), it is advisable to disable blanking and DPMS through both applications. To know more about XScreenSaver options, see XScreenSaver#DPMS and blanking settings.

;xset
If neither of the above applications are running, then blanking and DPMS settings can be controlled using the xset command, see DPMS#Runtime settings.

## Tips and tricks
## Mounting support for Thunar and xfdesktop
If plugged external drives does not appear and installation partitions are shown as mounted devices, on the desktop and in Thunar, install . See Udisks#Hide selected partitions for more advanced configuration options.

## Screenshots
Xfce has its own screenshot tool, . It is part of the  group.

Default keyboard shortcuts:  opens the main dialog window,  takes a screenshot of the active window,  allows you to select a region to be captured.

Alternatively, an independent screenshot program like scrot can be used.

## Terminal color themes or palettes
Terminal color themes or palettes can be changed in the GUI, under the Colors tab in Preferences. These are the colors that are available to most console applications like Emacs, Vi and so on.

The settings are stored in Xfconf. Although you can edit them directly, it might be more convenient to download or create a color preset file. The default presets are stored in , custom presets can be placed in . You can select a preset in Preferences > Colors > Presets.

Check forum thread [https://bbs.archlinux.org/viewtopic.php?id=51818 Terminal Colour Scheme Screenshots for hundreds of available choices and themes.

A commented example of a color preset file:

## env-modules autocompletion in Terminal
The  package provides shell autocompletion for login shells. However, by default, sessions in  are not considered as login. To enable autocompletion for Environment Modules, tick the Run command as login shell checkbox in Preferences > General.

## Colour management
Xfce has no native support for colour management. See ICC profiles for alternatives.

## Multiple monitors
Xfce has support for multiple monitors, which can be configured in the Applications > Settings > Display dialog. In the Advanced tab, one can save profiles for different monitors and have them applied automatically as soon as the connected monitors change. For more information, see the [https://docs.xfce.org/xfce/xfce4-settings/display display article from the Xfce documentation.

Alternatively, one can use  to manage display configurations in the form of xrandr commands which can be assigned to Xfce keyboard shortcuts.

## SSH agents
By default, Xfce will try to load gpg-agent and ssh-agent. Since gpg-agent is handled by systemd, you may want to disable it in the Xfce settings:

 $ xfconf-query --create -c xfce4-session -p /startup/gpg-agent/enabled -t bool -s false

If you plan to use the  user unit as described in SSH keys#Start ssh-agent with systemd user, disable ssh-agent in the Xfce settings as well:

 $ xfconf-query --create -c xfce4-session -p /startup/ssh-agent/enabled -t bool -s false

To use GNOME Keyring, simply tick the checkbox Launch GNOME services on startup in the Advanced tab of Session and Startup in Xfce's settings. This will also disable gpg-agent and ssh-agent.

Source: https://docs.xfce.org/xfce/xfce4-session/advanced#ssh_and_gpg_agents

## Scroll a background window without shifting focus on it
Go to Main Menu > Settings > Window Manager Tweaks > Accessibility tab.
Uncheck Raise windows when any mouse button is pressed.

 $ xfconf-query --channel xfwm4 --property /general/raise_with_any_button --set false

## Mouse button modifier
By default, the mouse button modifier in Xfce is set to . This can be changed with xfconf-query. For instance, the following command will set the  key as the mouse button modifier:

 $ xfconf-query -c xfwm4 -p /general/easy_click -n -t string -s "Super"

Strictly speaking, using multiple modifiers is not supported. However, as a workaround, multiple modifiers can be specified if the key names are separated with {{ic|> Show label''

## Using the Windows (Super) key for shortcuts
The  key is treated as a modifier key, like  and , instead of producing a keypress. Assigning an action to it will keep you from using it for other shortcuts, because it will trigger that action in addition to whatever else you assign to it.

To get around this, and make it more useful for shortcuts, install the application . This lets you configure modifier keys to act as other keys when pressed and released on their own.

Next, go to Settings > Keyboard > Application Shortcuts and assign an unused key combination, say , to the Application menu (or whatever action you want when you press the Super key by itself). Test that it works.
Next, use  to assign  to the  key:

 $ xcape -e 'Super_L=Alt_L|F1'

Check that the Super key now performs the action you assigned to .

If all is well, make this an autostart action; go to Settings > Session and Startup > Application Autostart tab, press the Add button and enter the command there to make it run every time you start Xfce (if xcape was already installed, also check that there is not already a similar entry registered).

Now, you can freely use the  key in shortcuts.
For example: In Window Manager > Keyboard, you can use  and  or  for Raise window or Lower window.

## Using the experimental Wayland support
Note: Xfce is transitioning from using labwc and wayfire as its compositor to creating a replacement compositor/window manager combo called xfwl4 that will replace xfwm4 on Wayland sessions. Once that happens this section will no longer be relevant.

Xfce supports both  and  as its Wayland compositor. However, only labwc works out of the box; Wayfire requires additional tweaking to the session file to make it work. For this purpose this section focuses on getting Xfce working with labwc as it requires the least effort to get Xfce working in Wayland.

After installing , you should be able to switch to the Xfce Session (Wayland) option in your display manager of choice and log in as usual. Note that Wayland support is marked as experimental for a good reason: things will not work like you expect it to and a lot of stuff is generally broken. For example, desktop icons placed by  may appear and disappear as the desktop gain and lose focus.

## Using labwc custom keymaps
The  configuration files for Xfce are located in  instead of the default labwc directory . If you have a custom  file with keymaps in it, you need a lock file , otherwise the layout gets overwritten by  with the system's default layout.

## Wallpaper changing does not work with the usual control panel settings
The Xfce desktop wallpaper control panel is still not yet adapted to work with Wayland, use a alternative wallpaper changer tool like  to change the wallpaper as a workaround.

## Troubleshooting
## Modifying setting does not take effect
If you are running a separate Xsettings daemon, it may make some configuration not taking effect. Disable it by removing or commenting the corresponding line and restart Xorg.

## NVIDIA and xfce4-sensors-plugin
To detect and use the sensors of an NVIDIA GPU, install  and then rebuild  with ABS. Another option is  which replaces .

## Panel applets keep being aligned on the left
Add a separator someplace before the right end and set its "expand" property. === Restore default settings ===

If for any reason you need to revert back to the default settings, remove or rename :

 $ mv ~/.config/xfce4/ ~/.config/xfce4-bak

Relogin for changes to take effect. If you get  upon login, see the #Session failure section.

## Session failure
Symptoms include:

* The mouse is an X and/or does not appear at all;
* Window decorations have disappeared and windows cannot be closed;
* Desktop turns grey and all desktop icons disappear;
* () will not start, reporting ;
* Errors reported by a display manager such as ;
* Unable to load a failsafe session:

 Unable to load a failsafe session.
 Unable to determine failsafe session name.  Possible causes: xfconfd is not running (D-Bus setup problem); environment variable $XDG_CONFIG_DIRS is set incorrectly (must include "/etc"), or xfce4-session is installed incorrectly.

Restarting Xfce or rebooting your system may solve the problem, but a corrupt session could also be the cause. Delete the session folder:

 $ rm -r ~/.cache/sessions/

Also make sure that the relevant folders in  are owned by the user starting . See Chown.

## Mousepad editor menu bar is not visible
Run the following to make it visible:

 $ gsettings set org.xfce.mousepad.preferences.window menubar-visible true

## Trash icon not visible and trash applet does not work
Trash requires the optional dependency gvfs to work.  Install  and reboot the system.

## Wayland support not working
If you are trying to get Xfce working with , additional editing must be done to the session files to make it work.

If not, make sure you have  installed.
