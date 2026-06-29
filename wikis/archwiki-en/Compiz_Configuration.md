# Compiz/Configuration

This article details more advanced Compiz configuration. It is assumed that you have successfully installed Compiz and have a basic, working configuration. For information on installation, basic configuration and troubleshooting, please consult the Compiz article.

## Settings storage options
## Configuration backends
By default, Compiz stores its configuration settings in a plain text file . In CCSM this is known as Flat-file Configuration Backend.

Compiz can also store its settings in the GSettings or GConf databases. To change how Compiz saves its settings open CCSM and click on the Preferences tab in the left hand column. Then choose your desired backend from the list under Backend.

You can also change the backend manually by editing the  file.

Edit the line below:
 backend = ini

* ini = Flat File Configuration Backend
* gsettings = GSettings Configuration Backend
* gconf = GConf Configuration Backend

Once you have edited and saved the file the change will take place immediately. There is no need to log out.

## Profiles
Profiles allow you to switch between different sets of Compiz settings easily. To create a new profile open CCSM and click on the Preferences tab. Under Profile click the plus sign to add a new profile or the minus sign to delete one. All changes made in CCSM will be written to your current profile.

Profiles are specific to the backend you are using. For instance, if you are using the GSettings backend then any new profile you create will be a GSettings profile. If you switch to a different backend then your current profile will not work and you will automatically switch to a profile available for that backend.

## Window decoration themes
## Emerald
Many Emerald themes are available for download on compiz-themes.org. Emerald themes can be installed, selected, removed and edited using the emerald-theme-manager program. For downloaded themes, unzip the tarball and then install it using the Import option in the theme manager.

Emerald themes are store in two locations:

* -- system
* -- user

The currently selected Emerald theme is copied into the  directory.

Emerald settings such as window button pulse can be configured in  and are written to the  file.

## GTK Window Decorator
The GTK Window Decorator can be compiled with support for the Metacity or Marco window managers (depending on the Compiz version). If it is compiled with this support, the theme used by Metacity or Marco will also be used by GTK Window Decorator. If GTK Window Decorator is not compiled with Metacity or Marco support, a builtin fallback theme will be used.

Many Metacity themes are available for download on gnome-look.org. Once downloaded, they should be unpacked into a directory such as  (for Metacity) or  (for Marco).

;Compiz 0.9

The GTK Window Decorator provided by Compiz 0.9 can be compiled with Metacity (version 3) support. Assuming this support is compiled in, change the Metacity theme using the commands below:

* In a GNOME Flashback session
Firstly, ensure that the theme type is set to metacity:
 $ gsettings set org.gnome.metacity.theme type metacity
Then the theme can be set with the following command:
 $ gsettings set org.gnome.metacity.theme name theme-name
* In a MATE session
Use the following command:
 $ gsettings set org.mate.Marco.general theme theme-name
* In any other session
Use the following command:
 $ gsettings set org.gnome.desktop.wm.preferences theme theme-name

;Compiz 0.8

The GTK Window Decorator included in the Compiz provided by the Compiz-Reloaded upstream (versions 0.8.10 and higher) can be compiled with Marco support. Assuming this support is compiled in, use the command below to change the Marco theme:
 $ gsettings set org.mate.Marco.general theme theme-name

The GTK Window Decorator included in the Compiz provided by the original Compiz upstream (versions 0.8.9 and below) can be compiled with Metacity (version 2) support. This GTK Window Decorator version expects the theme to be defined as a GConf setting. Assuming this support is compiled in, use the command below to change the Metacity theme:
 $ gconftool-2 -s /apps/metacity/general/theme -t string theme-name

## KDE Window Decorator
Kwin themes can be downloaded, installed and managed using the KDE systemsettings panel.

## Workspaces and Viewports
Unlike many other window managers, Compiz does not use multiple workspaces. Instead, it uses one workspace but splits it into multiple sections known as viewports. See for more information.

The number and layout of viewports can be configured in CCSM -> General Options -> Desktop Size. Changing the Horizontal Virtual Size will change the number of viewports in a row. Changing the Vertical Virtual Size will add or remove rows of viewports.

If you are using the Desktop Cube plugin, you will not be to use the rows of viewports added by increasing the Vertical Virtual Size. To take advantage of multiple rows of viewports, use the Desktop Wall plugin instead.

## Keyboard shortcuts
Below is a list of the default keyboard shortcuts for Compiz.

* Switch windows = .
* Switch to next desktops = .
* Switch to previous desktop = .
* Move window = .
* Resize window = .

A more detailed list can be found under [http://wiki.compiz.org/CommonKeyboardShortcuts CommonKeyboardShortcuts in the Compiz wiki or you can always just look at your plugin's configuration.

Extra shortcuts can be added using the commands plugin in CCSM.

## Edge bindings
Besides mouse and key bindings, Compiz can also assign commands to certain actions involving the screen edges, for example: dragging a window to the screen edge. For instance: the Rotate Cube plugin has an option to switch to the next viewport if a window is dragged to the screen edge. Edge bindings can usually be disabled, through CCSM, by unticking Edge Flip options in the plugin's settings section or by disabling actions which have the screen icon next to them in the Bindings section of the relevant plugin.

## Plugins
Almost all Compiz functionality is implemented using plugins. Some plugins must be enabled for standard window manager functionality - see Compiz#Enabling important plugins. Plugins that provide extra functionality, above and beyond standard window management, are discussed here.

## Grid
If you want to compare two windows side by side by dragging them to the edges of the screen, similar to the "Aero Snap" feature introduced in Windows 7, enable the Grid plugin in CCSM. If you are using the Desktop Wall or Rotate Cube plugin then disable the Edge Flip options in that plugin's section to ensure that windows do not move to the next desktop when dragged to the screen edge.

## Scale
The Scale plugin provides an option to view scaled thumbnails of all windows in the current viewport, similar to the "Present Windows" feature in KDE or the "Overview Mode" in GNOME Shell. Once the plugin is enabled, the view can be accessed by moving the mouse cursor into the top right corner of the screen. The active corner can be configured in the Bindings tab of the plugin's settings section.

## Widget Layer
The Widget Layer plugin allows you to define certain windows as widgets. Widget windows are shown on a separate "layer" of the screen. When the widget layer is hidden, all windows defined as widget windows will be iconified. By default, the widget layer is shown and hidden using  key.

To define a window as a widget, open CCSM and navigate to the Widget Layer plugin. Click on the Behaviour tab and click on the plus sign button next to the Widget Windows field. In the dialog box that appears, choose Window Title from the Type menu. In the Value field enter the title for the window you wish to define as a widget, for example: galculator.

## Screen Magnification
There are two Compiz plugins that can provide magnification functionality. The first is Magnifier which acts much like a magnifying glass (everything within the rectangular box will be zoomed). The magnifier can be used by enabling the plugin in CCSM and pressing .

The other plugin is called Enhanced Desktop Zoom. When this plugin is enabled, pressing the  key and scrolling the middle mouse button will magnify the part of the desktop that is under the mouse cursor.

## Crash handler
It is a good idea to enable the Crash handler plugin in CCSM. This plugin ensures that if, for whatever reason, Compiz fails to start with the session or crashes at some point during the session, crash logs will be dumped and an alternative window manager will be started. To specify a window manager that can replace Compiz in the event of a crash, click on the Crash handler plugin and tick the Start Other Window Manager option. Then, in the Window Manager Command Line field, enter a command to start the window manager of choice, for instance: .

## Compiz configuration without CCSM
Compiz does not have to be configured through CCSM. Settings can be changed by editing the profile directly. For Flat File profiles, this will mean making editing changes to the  file or similar. For GSettings or GConf profiles, this will mean making changes to the DConf or GConf databases using the gsettings or gconftool-2 tools.

## Flat-file sample configuration
Features of this sample configuration:
*  arranges the current window.
* Left and right bottom corner shows taskbar.
* Mouse control for everything (but typing).
* Some effects.

 as_active_plugins = core;session;glib;grid;notification;workarounds;place;put;wall;regex;blur;dbus;fs;inotify;widget;animation;resize;text;mousepoll;obs;expo;fade;move;staticswitcher;mag;scale;scaleaddon;
 s0_hsize = 2
 s0_vsize = 2

 [wall
 as_show_switcher = false
 s0_edgeflip_dnd = true
 as_flip_down_edge =

 as_reflection = false
 as_vp_brightness = 100.000000
 as_expo_edge =
 as_expo_button = Button9
 as_mipmaps = true
 as_zoom_time = 0.150000
 as_vp_distance = 0.000000

 [scale
 as_initiate_edge =
 as_initiate_all_button = Button8
 s0_darken_back = false
 s0_opacity = 100
 s0_overlay_icon = 0
 s0_multioutput_mode = 1
 as_show_desktop = false
 s0_hover_time = 100
 s0_spacing = 4
 s0_timestep = 0.100000
 s0_speed = 2.615500

 s0_window_highlight = true
 s0_highlight_color = #ffffff08
 s0_window_title = 0

 [mag
 as_zoom_in_button = Button4
 as_zoom_out_button = Button5
 s0_mode = 2
 s0_radius = 600

 s0_multioutput_mode = 3
 s0_mode = 2

 [workarounds
 as_notification_daemon_fix = true
 as_firefox_menu_fix = true
 as_legacy_fullscreen = true
 as_qt_fix = true
 as_convert_urgency = true

 as_opacity = 85

 [blur
 s0_filter = 1
 s0_independent_tex = true
 s0_mipmap_lod = 1.700000
 s0_gaussian_radius = 7
 s0_alpha_blur_match = (any) & !(class=Conky)

 as_put_next_output_button = Button10
 s0_speed = 10.441400
 s0_timestep = 0.100000

 [obs
 s0_opacity_matches = type=dock | Tooltip | Menu | PopupMenu | DropdownMenu;(any) & !(class=Whaawmp.py | class=Gimp | class=Inkscape | class=Xfdesktop | class=Ristretto);
 s0_opacity_values = 70;90;

 s0_close_effects = animation:Dream;animation:Fade;animation:Fade;
 s0_open_effects = animation:Magic Lamp;animation:Fade;animation:Fade;
 s0_focus_effects = animation:Dodge;
 s0_open_durations = 150;100;100;
 s0_close_durations = 150;100;100;
 s0_minimize_durations = 150;
 s0_shade_durations = 150;
 s0_focus_durations = 150;

 [widget
 s0_bg_brightness = 100
 s0_fade_time = 0.250000
 s0_match = type=Dock
 as_toggle_edge = BottomLeft|BottomRight
 s0_end_on_click = false

 s0_highlight_mode = 2
 s0_highlight_rect_hidden = 2
 as_next_key = Disabled
 as_next_no_popup_key = Tab
 as_prev_all_key = Disabled

## GSettings configuration
List all of the available Compiz profiles:
 $ gsettings list-recursively org.compiz | grep existing-profiles

Show the active Compiz profile:
 $ gsettings list-recursively org.compiz | grep current-profile

Set the active Compiz profile:
 $ gsettings set org.compiz current-profile profile-name

List all the available Compiz plugins schemas:
 $ gsettings list-relocatable-schemas | grep org.compiz

View all of the available settings for a Compiz plugin and their values (this example will show the settings of Static Application Switcher):
 $ gsettings list-recursively org.compiz.staticswitcher:/org/compiz/profiles/Default/plugins/staticswitcher/

View the value for a specific Compiz setting (this example checks the whether the Icon option in Static Application Switcher is enabled:
 $ gsettings get org.compiz.staticswitcher:/org/compiz/profiles/Default/plugins/staticswitcher/ icon

Change the value for a Compiz plugin setting (this will disable icons in Static Application Switcher):
 $ gsettings set org.compiz.staticswitcher:/org/compiz/profiles/Default/plugins/staticswitcher/ icon false

## Enabling or disabling a Compiz plugin using GSettings
Two steps are required. Firstly, get the list of active Compiz plugins using the command below:
 $ gsettings get org.compiz.core:/org/compiz/profiles/Default/plugins/core/ active-plugins

This should return an output similar to the one below:

 ['core', 'composite', 'opengl', 'compiztoolbox', 'decor', 'vpswitch', 'snap', 'mousepoll', 'resize', 'place', 'move', 'wall', 'grid', 'regex', 'imgpng', 'session', 'gnomecompat', 'animation', 'fade', 'workarounds'

Copy and paste the output and add it to the command to set the active plugins, adding or removing plugins from the array as appropriate. The example below will enable the Static Application Switcher:
 $ gsettings set org.compiz.core:/org/compiz/profiles/Default/plugins/core/ active-plugins "'composite', 'opengl', 'compiztoolbox', 'decor', 'vpswitch', 'snap', 'mousepoll', 'resize', 'place', 'move', 'wall', 'grid', 'regex', 'imgpng', 'session', 'gnomecompat', 'animation', 'fade', 'workarounds', 'staticswitcher'"
