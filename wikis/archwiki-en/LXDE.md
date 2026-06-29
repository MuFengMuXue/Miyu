# LXDE

From project home page:

:The "Lightweight X11 Desktop Environment" is an extremely fast-performing and energy-saving desktop environment. Maintained by an international community of developers, it comes with a beautiful interface, multi-language support, standard keyboard short cuts and additional features like tabbed file browsing. LXDE uses less CPU and less RAM than other environments. It is especially designed for cloud computers with low hardware specifications, such as, netbooks, mobile devices (e.g. MIDs) or older computers.

## Installation
LXDE requires at least ,  and Openbox (or another window manager) to be installed. The  group contains the full desktop.

## Starting the desktop
## Graphical log-in
LXDM is the default display manager for LXDE and is installed as part of the  group. See also Display manager.

## Console
To use startx, add to xinitrc:

See also Start X at login.

## Tips and tricks
## Application menu editing
The application menu works by resolving the .desktop files located in  and . To add or edit a menu item, see desktop entries. Third party menu editors can be found in the AUR (e.g. ). There are also official ones like  (GNOME),  (MATE), etc.

## Autostart
LXDE implements XDG Autostart. Applications can be automatically started in a couple of ways:

* With .desktop files
* Via LXsession

Each line in  represents a command to be executed. If a line starts with , and the command following it crashes, the command is automatically re-executed. For example:

## Keyboard shortcuts
Mouse and key bindings (i.e. keyboard shortcuts) are implemented with Openbox. LXDE users should follow the Openbox wiki to edit .

An optional GUI for editing the key bindings is provided by the  package. While it edits  by default, you can direct it to the LXDE configuration as follows:

 $ obkey ~/.config/openbox/lxde-rc.xml

See for more information.

## Cursors
 is a graphical tool to set GTK look and feel, including the cursor theme. Settings configured with LXAppearance are written to ,  and . See also Cursor themes.

## Digital clock applet time
You can right click on the digital clock applet on the panel and set how it displays the current time using the strftime format. See  for details.

## Font settings
 configures Openbox settings. See also Font configuration.

## Keyboard layout
 includes a keyboard layout applet. See Keyboard configuration in Xorg for generic instructions and #Autostart to automatically start setxkbmap in LXDE.

## Screen locking
LXDE does not come with a screen locker of its own. See List of applications/Security#Screen lockers and #Autostart on how to start them.

The Screen Lock icon executes a script (located at ) which searches for a number of well known screen lockers and uses the first one it finds to lock the screen. See [https://github.com/lxde/lxsession/blob/master/lxlock/lxlock lxlock on GitHub.

 (from the  package) lists XScreenSaver which will be launched automatically.

See DPMS on how to control the screen saver without external programs.

## LXPanel icons
To change default icons for applications, see Desktop entries#Icons.

## LXPanel menus
The panel's menus can be configured in  as per the xdg-menu format to work with applications from other sessions (notably MATE) to add some of the function-ability that LXDE lacks.

## Use a different window manager
LXsession uses the window manager defined in  (Openbox by default). If this file does not exist, it searches in  instead.

Replace  in either file with a window manager of your choice:

For metacity:

 window_manager=metacity

For compiz:

 window_manager=compiz

Alternatively use  as defined in #Autostart, where WM is the name of the window manager executable being started. This means that openbox will be started first on each login and will then immediately be replaced. Note that Openbox and LXDE do not share the same  and keyboard shortcuts may differ. See xbindkeys.

## Using a composite manager
LXDE does not enable compositing by default, which can lead to screen tearing problems. These can be remedied at the cost of a some graphical performance by installing a composite manager, such as picom.

## Replicating the look of Lubuntu 18.04
The wallpaper, GTK theme, and icons from Lubuntu 18.04 can be used with LXDE to replicate the look of Lubuntu 18.04. The package  provides the files necessary for this. Install the package, then open . Select the "Widget" tab and choose "Lubuntu-default", then choose the "Icon Theme" tab and select "Lubuntu". Last, select "Window Border" and select "Lubuntu-default". Click "Apply" to save. Additionally, to theme the taskbar, right click the taskbar and select "Panel Settings". In the "Appearance" tab, select "System theme" and ensure the font custom color box is unchecked, then select the "Geometry" tab and ensure the "Height" is set to 24 pixels. Note that all of these settings may be adjusted as needed, but the above instructions should provide the default look of Lubuntu 18.04.

## Troubleshooting
## LXPanel crashes
With some GTK themes, launching lxpanel will lead to the following error:

 lxpanel: cairo-scaled-font.c:459: _cairo_scaled_glyph_page_destroy: Assertion `!scaled_font->cache_frozen' failed.

In this case install .

If lxpanel crashes when browsing particular unicode web pages, install .

## LXPanel Task Bar icon size
The icons of running applications do not match the set Icon size in Panel Settings > Geometry but are 4px smaller which makes some of them blurry. To have clear looking 32px icons in the Task Bar the set Icon size has to be 36px which would blur the icons of the rest of your active Panel Applets. To get around this create additional panel(s) and have them collectively make a single continuous looking panel by adjusting the Alignment and Margin in Panel Settings > Geometry.

## Fake transparency in LXTerminal
Newer versions of the VTE terminal widget library require a compositing window manager for background transparency. The unmaintained, legacy GTK 2 version of VTE has fake transparency, where the desktop background image will show through the terminal. It you prefer fake transparency, the GTK 2 version of LXTerminal can be installed with the  package.

## LibreOffice theming does not work
LXDE overrides the  environment variable used for theming LibreOffice in . Change the line in that file to set the theme. Upstream bug
