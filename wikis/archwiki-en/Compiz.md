# Compiz

According to Wikipedia:

: Compiz is a compositing window manager for the X Window System, using 3D graphics hardware to create fast compositing desktop effects for window management. Effects, such as a minimization animation or a cube workspace, are implemented as loadable plugins.

## Installation
There are two versions of Compiz available, the 0.8 series which is written in C and the 0.9 series which is a complete re-write of Compiz in C++. Both series are actively developed. Compiz 0.9 is developed by the Compiz Maintainers on Launchpad whilst Compiz 0.8 is developed by the Compiz Reloaded project on GitLab. The two series cannot be installed side by side.

## 0.9 series
*

## 0.8 series
Required:

*

Highly recommended:

*
*

Optional:
*

## Extras
*
*
*
*
*

## Starting
## Enabling important plugins
Before starting Compiz, you should activate some plugins to provide basic window manager behaviour or else you will have no ability to drag, scale or close any windows. Important plugins are listed below:

* Window Decoration - provides window borders, see #Window decoration.
* Move Window.
* Resize Window.
* Place Windows - configure window placement options.
* Application Switcher - provides an  switcher - there are numerous alternative application switcher plugins, for example: Shift Switcher, Static Application Switcher and more. Not all of them use the  keybinding.

To be able to switch to different viewports you will need to enable one of the following:

* Desktop Cube & Rotate Cube - provides the spinning cube with each side being a different viewport.
* Desktop Wall - viewports are arranged next to each other - the animation is similar to the workspace switching animation in Cinnamon and GNOME Shell.
* Expo - creates a view of all viewports and windows when the mouse is moved into the top left corner - this plugin can be used on its own or in conjunction with either of the two previous plugins.

## Window decoration
The window decorator is the program which provides windows with borders. Unlike window managers such as Kwin or Xfwm which provide just one decorator, users of Compiz have a choice of three: GTK Window Decorator, KDE Window Decorator and Emerald. The GTK Window Decorator and the KDE Window Decorator are included in the Compiz source and can be optionally compiled whilst building Compiz. Emerald, on the other hand, is a separate, standalone decorator. The Window Decoration plugin in CCSM must be ticked otherwise no window decorator will be started.

;Choosing the decorator
The window decorator that will be started is specified under CCSM -> Effects -> Window Decoration -> Command. The default command is compiz-decorator which is a script which will attempt to locate the emerald and gtk-window-decorator executables (and also the kde4-window-decorator executable if you are using Compiz 0.9). It will then start the first decorator that it finds, according to the search order and conditions (such as session detection) specified in the script. Note that the script provided by Compiz 0.8 differs significantly from the one provided by Compiz 0.9 so the behavior may be different.

The compiz-decorator command can be replaced with one of the executables listed above. If you find that your preferred decorator is not being started, try appending the  switch to the command, for example: .

## Compiz startup
You can start Compiz using the following command:

 $ compiz --replace

See  for more options.

## Fusion Icon
To start Compiz using Fusion Icon, execute the command below:

 $ fusion-icon

To ensure that fusion-icon then starts Compiz, right click on the icon in the panel and go to select window manager. Choose Compiz if it is not selected already.

## Autostarting Compiz in a desktop environment
See Desktop environment#Custom window manager.

## Using Compiz as a standalone window manager
## Starting the session with a display manager
A standalone Compiz session can be started from a display manager. For most display managers - LightDM for example - all that is required is to create a  file in  that executes compiz (with command line options if needed) or fusion-icon. See the article for your display manager. See Desktop entries for information on creating a  file.

## Autostarting programs when using a display manager
One way in which you could start programs with your Compiz session, when it is started from a display manager, is to use an xprofile file. Another option is for the  file in  to not execute compiz directly but to execute a script which starts the programs you wish to start and also starts Compiz.

## Starting the session with startx
A Compiz session can be started with startx. Define either compiz or fusion-icon in your  file. See the xinitrc article for more details.

## Allow users to shutdown/reboot
See Allow users to shutdown#Using systemd-logind: you can assign a keyboard shortcut to systemctl comands using the Commands plugin in CCSM.

## Tips and tricks
## Restoring the native window manager
You can switch back to your desktop environment's default window manager with the following command:

 wm_name --replace

using kwin, metacity or xfwm4 for example instead of wm_name.

## Enabling the Alt+F2 run dialog
;GNOME Panel

Enable the Gnome Compatibility plugin in CCSM.

;MATE Panel

There are two ways to enable MATE Panel's run dialog in Compiz. You can either:

* Enable the MATE Compatibility plugin in CCSM (use the Gnome Compatibility plugin for older Compiz versions which lack the MATE plugin).
* Map the command below to the  key combination using the Commands plugin in CCSM.

 mate-panel --run-dialog

;LXDE Panel

Map the command below to the  key combination using the Commands plugin in CCSM.

 lxpanelctl run

;Xfce Appfinder

When Compiz is used in an Xfce session, the run dialog (provided by ) should work without intervention. If you are using Xfce Appfinder in a standalone Compiz session, map the command below to the  key combination using the Commands plugin in CCSM.

 xfce4-appfinder --collapsed

;Other run dialogs

Map the command for a run dialog of choice to the  key combination using the Commands plugin in CCSM.

## Remove title bar from maximized windows
Start CCSM and navigate to the Window Decoration plugin. Then in the Decoration Windows field, change  to . == Troubleshooting ==

## Missing GLX_EXT_texture_from_pixmaps
## ATI cards
A possible issue with GLX_EXT_texture_from_pixmap on ATI cards is that the card can only render it indirectly. If so, you have to pass the option to your libgl as shown below:

 LIBGL_ALWAYS_INDIRECT=1 compiz --replace &

## Intel chips
Use the following command to start Compiz (this command must be used every time).

 LIBGL_ALWAYS_INDIRECT=true compiz --replace --sm-disable &

## Compiz starts without window borders with NVIDIA binary drivers
Firstly, ensure that your window decorator settings are configured correctly - see #Window decoration. If window borders still do not start try adding Option "AddARGBGLXVisuals" "True" and Option "DisableGLXRootClipping" "True" to your "Screen" section in . If window borders still do not load and you have used other Options elsewhere in  try commenting them out and using only the aformentioned ARGBGLXVisuals and GLXRootClipping Options.

## Blank screen on resume from suspend-to-ram with NVIDIA binary drivers
If you receive a blank screen with a responsive cursor upon resume, try disabling sync to vblank. To do so, open CCSM, navigate to the OpenGL plugin and untick the Sync to VBlank option.

## Poor performance from capable graphics cards
NVIDIA and Intel chips: If everything is configured correctly but you still have poor performance with some effects, try disabling CCSM > General Options > Display Settings > Detect Refresh Rate and instead choose a value manually.

NVIDIA chips only: The inadequate refresh rate with Detect Refresh Rate may be due to an option called DynamicTwinView being enabled by default which plays a factor in accurately reporting the maximum refresh rate that your card and display support. You can disable DynamicTwinView by adding the following line to the "Device" or "Screen" section of your , and then restarting your computer:

 Option "DynamicTwinView" "False"

## Screen flicks with NVIDIA card
To fix this behaviour create the file below:

## Video tearing
If you experience video tearing when using Compiz, try enabling the Workarounds plugin in CCSM. Once enabled, ensure that the following options are enabled in Workarounds: Force complete redraw on initial damage, Force full screen redraws (buffer swap) on repaint.

If you are using Intel graphics and the workaround above does not fix the video tearing, see Intel graphics#Tearing.

Also see, #Poor performance from capable graphics cards.

## Fusion Icon fails to start
If you get an output like this from the command line:

the problem is with the permission on . To fix it, use:

 # chown -R username /home/username/.config/compiz/

## Alt+F4 keybinding not working (Xfce)
If Compiz replaces Xfwm4 at login, this can cause the  keybinding to become non-functional. To avoid this issue, ensure that only Compiz is started at login - see Xfce#Use a different window manager.

## Emerald crashes when selecting a theme
You may find that Emerald crashes when selecting certain themes (especially themes that use the legacy engine). If this occurs, select another theme in Emerald Theme Manager and then run the command .

## No system bell when Compiz is running
You may find that the system bell (such as the drip sound played when pressing backspace at the beginning of a line in GNOME or MATE Terminal) will not sound if Compiz is running. See the following [https://bugs.launchpad.net/ubuntu/+source/compiz/+bug/537703 upstream bug report.

PulseAudio users, as a workaround, can force PulseAudio to handle the system bell, see PulseAudio#X11 Bell Events.

## Compiz crashes when enabling the Gnome Compatibility plugin (GSettings backend)
If you are using the GSettings backend, you may find that Compiz crashes if you try to enable the Gnome Compatibility plugin. In order to enable this plugin whilst using the GSettings backend you need to open CCSM and navigate to Preferences. Under the header Integration untick the box labelled Enable integration into the desktop environment. After unticking this option, you should find it possible to enable the Gnome Compatibility plugin.

## Windows lose focus when unminimised
You may find that certain windows (such as a Chromium window) will lose focus when unminimised. See the following upstream bug report. One possible solution is to enable the Keep previews of minimized windows option, located within the Workarounds plugin.

## Popout windows are offset when Compiz is running
You may find that popout windows for panels which are placed at the bottom of the screen are offset by a few pixels so that the window appears to float above the panel. This problem is known to affect Xfce and KDE and may affect other desktops as well. Listed below are a number of workarounds that might fix some cases.

* Place the panel at the top of screen instead of the bottom - this should work in most cases.
* Disable the Place Windows plugin - this works for the Xfce Whisker Menu plugin but may not work elsewhere.
* Use fixed window placement to determine the window's position. This can be set from the Place Windows plugin. For instance, for the Whisker Menu, specify that the window with the title Whisker Menu should appear at (-1, -1).

For more information, see the following upstream bug report.

## Alt-Tab switcher has no background (Emerald)
You may find that the  switcher (provided by the staticswitcher or switcher plugins) has a completely transparent background when using Emerald as well. This can make it hard to differentiate window thumbnails from the desktop background behind them. As of Compiz 0.9.12 (revision 3975) a workaround is available. In CCSM, navigate to Application Switcher or Static Application Switcher depending on which plugin you are using. For the former, the Background settings are located under General and for the latter the settings are located under Appearance. Once you have found the settings, ensure that the Set background color box is ticked. The default is a dark grey which can be optionally changed.

Alternatively, use GTK Window Decorator instead of Emerald or use a different window switcher altogether such as the shift switcher. Note that even if you are using the GTK Window Decorator, you can still change the background color as described above.

## Mouse cursor invisible or X shaped on startup
See Cursor themes#Change X shaped default cursor.

## Known issues
## Plugins in Compiz 0.8 are not present in Compiz 0.9
Some plugins that were popular in Compiz 0.8 were disabled in Compiz versions 0.9.8 and above in order to complete OpenGL ES support. A few of the disabled plugins have since been re-enabled; for instance, the Animations Add-On plugin was re-enabled for the Compiz 0.9.13.0 release. Other currently-disabled plugins that receive patches for this issue may well be re-enabled in future releases. For more information, see the Compiz 0.9.8 release notes.

Likewise, Compiz Plugins Unsupported (a package which includes plugins such as Atlantis) is unavailable in recent versions of Compiz 0.9. It has not been developed for the Compiz 0.9 series since Compiz 0.9.5 and no longer builds successfully.

## Xfce panel issues
## Xfce workspace switcher has wrong aspect ratio
When Compiz is used with Xfce Panel 4.11 and above, the workspace pager will use the width of only one workspace but will divide this space into ever smaller bars, according to how many viewports Compiz specifies. This issue can be fixed by replacing  with  which incorporates a patch for this issue. For more information, see the following upstream bug report.

## Compiz crashes when enabling the D-Bus plugin
The D-Bus plugin will cause Compiz to crash if enabled in conjunction with certain other plugins such as the Cube plugin. See the following upstream bug report.

## Workspace pager and window buttons issues
Only a few taskbars are compatible with Compiz's viewports. Incompatible panels and docks may display issues such as showing all window buttons in all workspaces or the workspace pager may only show one workspace available. The panels listed below are known to be compatible:

*  (partial, see #Xfce panel issues)
*
*
*
