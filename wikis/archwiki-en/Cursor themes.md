# Cursor themes

The display server is accompanied by a cursor theme that helps with various aspects of GUI navigation and manipulation. The display server includes a cursor theme, however, other cursor themes can be installed and selected.

## Installation
Installation can be done with a package, or downloaded and extracted to an appropriate directory.

## Packages
Cursors themes are available in the:

* Official repositories — search for packages with the prefix "xcursor-", or the suffix "-cursors". Several icon themes also include cursors.
* AUR — "cursor" search.

## Manually
If a cursor theme is not available in the official repositories or the AUR, it can be added manually.  A number of websites exist where cursor themes can be downloaded.  Once downloaded, they need to be put in the icons directory (as cursors have the ability to be bundled with icon themes).

Some websites that have cursor themes:

* GNOME Look
* Deviant Art
* Open Desktop

For user-specific installation, use the  directory, or  which is used for backwards compatibility.  Extract them with this command that will work for most archives:

 $ tar xvf foobar-cursor-theme.tar.gz -C ~/.local/share/icons

The cursor theme directory structure is , for example: ; make sure the extracted files follow this structure.

Already installed cursor themes can be viewed with the command:

 find /usr/share/icons ~/.local/share/icons ~/.icons -type d -name "cursors"

If the package includes an  file, check if there is an "Inherits" line inside.  If yes, check whether the inherited theme also exists on the system (rename if needed).

## Configuration
There are various ways to set the cursor theme. The cursor appearance may change from one window to another if programs are not configured to use the same cursor theme.

Installed cursors may generally be set per desktop environment and per GUI framework. The cursor theme named "default" is the fallback when a configuration is not set.

## GTK and Qt configuration files
## GTK
## Qt
There is no Qt configuration for cursors. Qt programs may pick up a cursor theme from the desktop environment, X resources, or lastly the "default" cursor theme if none are configured. To make Qt programs find cursors in the  path, it must be in the XCURSOR_PATH environment variable.

## Desktop environments
Desktop environments use the XSETTINGS protocol, typically implemented through a settings daemon like Xsettingsd.

## GNOME
To change the theme in GNOME, use  or set the configuration directly with:

 $ gsettings set org.gnome.desktop.interface cursor-theme cursor_theme_name

Change the cursor size with (depending on the theme, sizes are 24, 32, 48, 64):

 $ gsettings set org.gnome.desktop.interface cursor-size cursor_theme_size

## MATE
In MATE one can use  or . To change the theme:

 $ gsettings set org.mate.peripherals-mouse cursor-theme cursor_theme_name

To change the size:

 $ gsettings set org.mate.peripherals-mouse cursor_theme_size

## Plasma (Wayland)
 must be installed for GTK applications to correctly apply cursor theming on Wayland.

## XFCE
To change the xcursor theme, use:

 $ xfconf-query --channel xsettings --property /Gtk/CursorThemeName --set cursor_theme_name

To change the size:

 $ xfconf-query --channel xsettings --property /Gtk/CursorThemeSize --set cursor_theme_size

## Sway
See Sway#Change cursor theme and size.

## X resources
To locally name a cursor theme, add to the  file:

 Xcursor.theme: cursor-theme

To have the cursor theme properly loaded, it will need to be done so by the window manager; if it does not, it can be forced to load prior the window manager by putting the following command in .xinitrc or .xprofile (depending on ones personal setup):

Optionally, add this line to  if your cursor theme supports multiple sizes:

 Xcursor.size: 16

If in doubt over supported cursor sizes, start X without this setting and let it choose the cursor size automatically. (Refer to your window manager documentation for details).

## The default cursor theme
The cursor theme name default is used by an application if it cannot pick up on a configuration. Thus, a last resort to make the cursor choice consistent across fragmented configurations is to edit the default theme to become a synonym of the theme of choice.

The default cursor theme is in the usual theme locations:

*
*
*  (system-wide)

## Aliasing
The default theme can be aliased to any other cursor theme by symlinking/copying the directory containing the desired cursor to the default theme paths:

 $ ln --symbolic /usr/share/icons/cursor_theme_name ~/.local/share/icons/default

## Inheritance
Alternatively, the theme can simply inherit another desired one:

## LXAppearance
LXAppearance creates an  file: if you edited that file manually, LXAppearance will overwrite it.

## Environment variable
You can use an environment variable to set a theme for a single application to try it out temporarily, for example:

 $ XCURSOR_THEME=cursor_theme_name xclock

 is optional if your cursor theme supports multiple sizes.

If cursor themes are installed in , in order to avoid possible issues, add that path to . For example:

 XCURSOR_PATH=${XCURSOR_PATH}:~/.local/share/icons

## Display managers
Cursor theme can usually be set within a display manager, but keep in mind the cursor theme may not carry over to the user session.

## GDM
See GDM#Changing the cursor theme.

## Tor Browser
Tor Browser has its own "virtual" home directory and does not read the file in the user's home directory. Therefore, you need to copy configuration and, if necessary, icon themes to the Tor Browser installation directory:

Create a GTK configuration file on the Tor Browser "virtual" home directory:

If your desired cursor theme is not installed system-wide, you'll have to copy it to the Tor Browser "virtual" home directory; for example:
 $ cp -r ~/.local/share/icons/cursor_theme_name ~/.local/share/torbrowser/tbb/x86_64/tor-browser/Browser/.local/share/icons/

You can also just simply copy your whole cursor themes folder:
 $ cp -r ~/.local/share/icons ~/.local/share/torbrowser/tbb/x86_64/tor-browser/Browser/.local/share

## Troubleshooting
## Create links to missing cursors
Applications may keep using the default cursors when a theme lacks some cursors.  This can be corrected by adding links to the missing cursors. For example:

 $ cd ~/.icons/theme/cursors/
 $ ln -s right_ptr arrow
 $ ln -s cross crosshair
 $ ln -s right_ptr draft_large
 $ ln -s right_ptr draft_small
 $ ln -s cross plus
 $ ln -s left_ptr top_left_arrow
 $ ln -s cross tcross
 $ ln -s hand hand1
 $ ln -s hand hand2
 $ ln -s left_side left_tee
 $ ln -s left_ptr ul_angle
 $ ln -s left_ptr ur_angle
 $ ln -s left_ptr_watch 08e8e1c95fe2fc01f976f1e063a24ccd

If the above does not solve the problem, look in  for additional cursors your theme may be missing, and create links for these as well.

## Supplying missing cursors
Some programs set their own custom cursors  which you may want to override.  A common example of this is rdesktop, which connects to a Microsoft Windows computer and uses the cursors obtained from the remote machine, which can often be difficult to see due to protocol limitations yielding poor conversion quality.

This can be resolved by replacing these cursors with ones from the same (or another) cursor theme.  In order to do this, the hash of the image must be obtained.  This is done by setting the  environment variable prior to launching the application that sets these cursors:

 $ XCURSOR_DISCOVER=1 rdesktop ...

The first time (and only the first time) the cursor is set, some details will be displayed, like this:

 Cursor image name: 24020000002800000528000084810000
 ...
 Cursor image name: 7bf1cc07d310bf080118007e08fc30ff
 ...
 Cursor hash 24020000002800000528000084810000 returns 0x0

When Xcursor looks for missing cursors, the search path includes  so this is where an image can be placed for Xcursor to find.  First, create this directory if it does not already exist:

 $ mkdir -p ~/.icons/default/cursors

Then link the hash to the target image.  Here we are using the  image from the  cursor theme:

 $ ln -s /usr/share/icons/Vanilla-DMZ/cursors/left_ptr ~/.icons/default/cursors/24020000002800000528000084810000

The change will be visible as soon as the application is restarted.  No special method of launching the application is required.

## Change X shaped default cursor
The default X shaped Xcursor appears in window managers that do not set the default cursor to left_ptr or in window managers using XCB (like awesome) instead of Xlib.

To fix this, simply add the following to your , xsession or window managers startup configuration if possible (for example bspwm's bspwmrc).
 $ xsetroot -cursor_name left_ptr

The list of cursor styles is in appendix B of the X protocol.

## .Xdefaults
If you have conflicting cursors then it might be because a different cursor has been set in the  file.

## Cursor size does not change on startup
If you are trying to change cursor size via  in your  and it does not work, make sure that xrandr runs before loading .

Make sure your  looks similar to the following:

## Cursor size or theme does not change on Plasma (Wayland)
When changing the cursor size or theme when using Plasma under Wayland, make sure to restart the session after applying the changes [https://bugs.kde.org/show_bug.cgi?id=420859.

This is a bug. See a workaround at KDE#Plasma cursor sometimes shown incorrectly.
