# GTK

From the GTK website:
:GTK, or the GIMP Toolkit, is a multi-platform toolkit for creating graphical user interfaces. Offering a complete set of widgets, GTK is suitable for projects ranging from small one-off tools to complete application suites.

GTK was initially made by the GNU Project for GIMP, but it is now a very popular toolkit with bindings for many languages. This article will explore the tools used to configure the GTK theme, style, icon, font and font size, and also detail manual configuration.

## Installation
Multiple versions of GTK are currently available. They can be installed with the following packages:

* GTK 4.x is available with the  package.
* GTK 3.x is available with the  package.
* GTK 2.x is available with the  package.
* GTK 1.x is available with the  package.

## Themes
## GTK 3 and GTK 4
In GTK 3 and GTK 4, the default theme is Adwaita, but HighContrast and HighContrastInverse themes are also included.

To apply a specific theme, set the  property in the  namespace via a dconf editor:

 $ gsettings set org.gnome.desktop.interface gtk-theme Adwaita

If you are not using a dconf property, you can use  to apply a GTK 3 and GTK 4 themes. For example to launch GNOME Calculator with the dark variant of Adwaita:

 $ GTK_THEME=Adwaita:dark gnome-calculator

## GTK 2
In GTK 2, the default theme is Raleigh, but Arch Linux has a custom configuration file at , which sets the default theme to Adwaita. However, this requires  package to be installed on the system to work correctly, otherwise GTK-2 applications will continue to appear in Raleigh theme.

To change the GTK 2 theme, use . For example to launch GIMP with the theme Raleigh:

 $ GTK2_RC_FILES=/usr/share/themes/Raleigh/gtk-2.0/gtkrc gimp

More themes can be installed from the official repositories or the AUR. Manually extracted themes go in  or  directory.

## Themes supporting GTK 2 and GTK 3
*
*
*
*
*
*
*
*
*
*
*
*

There are a number of additional GTK themes in the AUR, example: search for gtk-theme.

## GTK and Qt
If you have GTK and Qt (KDE) applications on your desktop then you know that their looks do not blend well. If you wish to make your GTK styles match your Qt styles please read Uniform look for Qt and GTK applications.

## Configuration tools
Most major desktop environments provide tools to configure the GTK theme, icons, font and font size, and manage these settings via XSettings:
* If you use Cinnamon, use Themes tool (cinnamon-settings themes): go to System Settings > Themes.
* If you use Enlightenment: go to Settings > All > Look > Application Theme.
* If you use GNOME, use GNOME Tweaks (gnome-tweaks): install .
* If you use KDE, install . After installation, the GTK theme can be seleted in System Settings > Colors & Themes > Application Style > Configure GNOME/GTK Application Style.
* If you use LXQt, use the Appearance Settings tool (lxqt-config-appearance): go to Settings > Appearance > GTK Style.
* If you use MATE, use the Appearance Preferences tool (mate-appearance-properties): go to System > Settings > Appearance.
* If you use Xfce, use the Appearance tool: go to Settings > Appearance.

Other GUI tools generally overwrite the configuration files.

Both GTK 2 and GTK 3 are supported:
*
:After installation,  can be found in Preferences > GTK Settings.
*
*

Only GTK 2 is supported:
*
*
*

## Configuration
GTK settings can be specified manually in configuration files, but desktop environments and applications can override these settings. Depending on GTK version, these files are located at:
* GTK 2 user specific: ,
* GTK 2 system wide:
* GTK 3 user specific: , or  if  is not set
* GTK 3 system wide:

## Basic theme configuration
To manually change the GTK theme, icons, font and font size, add the following to the configuration files, for example:

* GTK 2:

* GTK 3:

If the theme is not applied for GTK 3, use  in addition:

 $ gsettings set org.gnome.desktop.interface gtk-theme theme_name

Similarly, if the icon theme is not applied for GTK 3 , use :

 $ gsettings set org.gnome.desktop.interface icon-theme icon_theme_name

For downloading and installing icons manually, see Icons.

## Dark theme variant
Some GTK 3 themes contain a dark theme variant, but it is only used by default when the application requests it explicitly. To use dark theme variant with all GTK 3 applications, set:

 gtk-application-prefer-dark-theme = true

For GTK 4, use:

 $ gsettings set org.gnome.desktop.interface color-scheme prefer-dark

## Keyboard shortcuts
Keyboard shortcuts (otherwise known as accelerators in GTK) may be changed by hovering the mouse over the respective menu item, and pressing the desired key combination. To enable this feature, set:

 gtk-can-change-accels = 1

## Emacs key bindings
To have Emacs-like key bindings in GTK applications add the following:

For GTK3 also run:

 $ gsettings set org.gnome.desktop.interface gtk-key-theme "Emacs"

XFCE has a similar setting:

 $ xfconf-query -c xsettings -p /Gtk/KeyThemeName -s Emacs

## Declaring keybinds
The configuration files e.g. in  determine what the Emacs bindings are, and can be changed.

{{hc|/usr/share/themes/Emacs/gtk-2.0-key/gtkrc|
binding "gtk-emacs-text-entry"
{
  bind "b" { "move-cursor" (logical-positions, -1, 0) }
  ...
}
}}

{{hc|/usr/share/themes/Emacs/gtk-3.0/gtk-keys.css|
@binding-set gtk-emacs-text-entry
{
  bind "b" { "move-cursor" (logical-positions, -1, 0) };
  ...
}
}}
Copying sections to the users  and  for GTK 2 and 3 respectively, allows for changes on a per user basis.

## GNOME menu delay
This setting controls the delay between pointing the mouse at a menu and that menu opening. This delay is measured in milliseconds.

 gtk-menu-popup-delay = 0

## Reduce widget sizes
If you have a small screen or you just do not like big icons and widgets, you can resize things easily.

To have icons without text in toolbars (valid values), use

 gtk-toolbar-style = GTK_TOOLBAR_ICONS

To use smaller icons, use a line like this:

 gtk-icon-sizes = "panel-menu=16,16:panel=16,16:gtk-menu=16,16:gtk-large-toolbar=16,16\
 :gtk-small-toolbar=16,16:gtk-button=16,16"

Or to remove icons from buttons completely:

 gtk-button-images = 0

You can also remove icons from menus:

 gtk-menu-images = 0

See also and [https://www.gnome-look.org/p/1079374.

## Hide CSD buttons
To remove the client-side decorations (CSD)minimize and maximize buttons from gtk3 windows:

 gtk-decoration-layout=menu:close

See [https://docs.gtk.org/gtk3/property.Settings.gtk-decoration-layout.html GTK docs.

## Disable mouse paste
To turn off pasting from the clipboard (PRIMARY selection) when the middle mouse button is clicked:

 gtk-enable-primary-paste=false

## File-chooser start-up location
Open the file-chooser within the current working directory and not the recent location. Normally the current working directory is the Home directory.

GTK 3

Change setting with the following command:

 $ gsettings set org.gtk.Settings.FileChooser startup-mode cwd

GTK 2

Add the following to :

 StartupMode=cwd

## Legacy scrolling behavior
Prior to GTK 3.6, clicking on either side of the slider in the scrollbar would move the scrollbar in the direction of the click by approximately one page. Since GTK 3.6, the slider will move directly to the position of the click. This behaviour can be reverted in some applications by creating the file with the content below:

## Disable overlay scrollbars
Since GTK 3.15, overlay scrollbars are enabled by default, meaning that scrollbars will be shown only on mouseover in GTK 3 applications. This behavior can be reverted by setting the following environment variable: . See Environment variables#Graphical environment.

Alternatively, overlay scrollbars can be disabled in the GTK 3 settings since GTK 3.24.9. To do so, the value of gtk-overlay-scrolling has to be set to false in the section of the settings file:

GTK 4 will no longer support . It has already been [https://github.com/GNOME/gtk/commit/e49615184a9d85bb0bb4e289b3ee8252adee3813#diff-3cf94c6e1eb009e20985034bc2210bfd dropped from master. As of GTK 4, the overlay nature of the scrollbars is part of the toolkit. The blanket toggle has been removed to prevent developers from breaking applications that have not been tested with both combinations. To allow application developers to decide what their applications should look like, the toolkit instead provides a mechanism to opt-out or add a setting for users. The function gtk_scrolled_window_set_overlay_scrolling() can be used to enable/disable overlay scrolling on a per-application basis. Application developers can optionally use GSettings to have a user setting bound to the property.

## Remove overlay scroll indicators
The positions of the overlay scrollbars are indicated by thin dashed lines in the application window. These dashed lines will be present even when overlay scrolling is disabled using the environment variable discussed in the section above. To remove the indicator lines, create the following file:

{{hc|~/.config/gtk-3.0/gtk.css|
/* Remove dotted lines from GTK 3 applications */
undershoot.top, undershoot.right, undershoot.bottom, undershoot.left { background-image: none; }
}}

## Disable sounds
 gtk-enable-event-sounds=0
 gtk-enable-input-feedback-sounds=0

## Examples
GTK example configurations:

## GDK backends
GDK (the underlying abstraction layer of GTK) supports multiple backends to display GTK applications.

## Wayland backend
The GDK Wayland backend is supported only by  or newer and is the default backend when using Wayland display server.

Applications that use versions of GTK prior to  do not have Wayland support, and need to use Xwayland in order to run on a Wayland session using the X11 backend.

When using the Wayland backend, some variables are not sourced from .
Any key that is present in the GSettings schema  are read from there instead of .

An example of such variables are  and , which must have their keys set with GSettings in order to theme GTK Applications under Wayland. Alternatively, if only the theme needs to be customized, the environment variable  can be set.

See the relevant article on the sway wiki for more details on this.

## Xorg backend
If Xorg display server is in use, the backend defaults to x11 automatically.

It is possible to force GTK3 applications running on a wayland session to use the X11 backend through Xwayland by setting the environment variable .

## Broadway backend
The GDK Broadway backend provides support for displaying GTK applications in a web browser, using HTML5 and web sockets.
When using broadwayd, specify the display number to use, prefixed with a colon, similar to X. The default display number is 0 (zero).

 $ display_number=:5
Start it.
 $ broadwayd $display_number

Port used by default
 port = 8080 + $display_number

Point your browser to http://127.0.0.1:port

To Start applications

 $ GDK_BACKEND=broadway BROADWAY_DISPLAY=$display_number >

Alternatively can set address and port

 $ broadwayd --port $port_number --address $address $display_number

## Troubleshooting
## Different themes between GTK 2 and GTK 3 applications
In general, if a selected theme has support for both GTK 2 and GTK 3, the theme will be applied to all GTK 2 and GTK 3 applications. If a selected theme has support for only GTK 2, it will be used for GTK 2 applications and the default GTK theme will be used for GTK 3 applications. If the selected theme has support for only GTK 3, it will be used for GTK 3 applications and the default GTK theme will be used for GTK 2 applications. Thus for application theme consistency, it is best to use a theme which has support for both GTK 2 and GTK 3.

You could find what themes installed on your system  have both an GTK 2 and GTK 3 version by using this command (does not work with names containing spaces):
 find $(find ~/.themes /usr/share/themes/ -wholename "*/gtk-3.0" | sed -e "s/^\(.*\)\/gtk-3.0$/\1/") -wholename "*/gtk-2.0" | sed -e "s/.*\/\(.*\)\/gtk-2.0/\1"/

## Theme not applied to root applications
As user theme files (, ) are not read by other accounts, the selected theme will not apply to X applications running as root. Possible solutions include:

* Create symlinks, e.g
 # ln -s $HOME/.gtkrc-2.0 /etc/gtk-2.0/gtkrc
 # ln -s $HOME/.config/gtk-3.0/settings.ini /etc/gtk-3.0/settings.ini
* Configure system-wide theme files:  (GTK 3) or  (GTK 2)
* Adjust the theme as root
 # lxappearance
* Use a settings daemon (this is what most desktop environments do). A desktop-agnostic variant using [https://specifications.freedesktop.org/xsettings-spec/latest/ XSettings is available with .

## Client-side decorations
GTK 3.12 introduced client-side decorations, which move the title-bar away from the window manager. This may present issues such as double title-bars, no title-bar at all, double shadows with compositing enabled, or being unable to move a frozen application.

To remove the shadow and gap around windows (for example in combination with a tiling window manager), create the following file:

{{hc|~/.config/gtk-3.0/gtk.css|.window-frame, .window-frame:backdrop {
 box-shadow: 0 0 0 black;
 border-style: none;
 margin: 0;
 border-radius: 0;
}

.titlebar {
 border-radius: 0;
}

.window-frame.csd.popup {
  box-shadow: 0 1px 2px rgba(0, 0, 0, 0.2), 0 0 0 1px rgba(0, 0, 0, 0.13);
}

.header-bar {
  background-image: none;
  background-color: #ededed;
  box-shadow: none;
}
/* You may want to use this if you do not like the double title.
GtkLabel.title {
    opacity: 0;
}*/
}}

Note that if visual problems persist, you may want to use the GTK Inspector to find the offending elements as explained here To adjust the buttons in the header bar, use the  setting. [https://developer.gnome.org/gtk3/stable/GtkSettings.html#GtkSettings--gtk-decoration-layout The below examples removes all buttons:

To remove client-side decorations altogether, you can use  which contains a patch that disables them by default. To enable client-side decorations, set the  environment variable with any value.

Alternatively, you can use , see README for GTK3 and GTK4.

## cedilla ç/Ç instead of ć/Ć
See and [https://bugs.launchpad.net/ubuntu/+source/ibus/+bug/518056/comments/37 for a workaround using Xcompose (US international layout).

## Suppress warning about accessibility bus
If you do not use any Gnome Accessibility features, you may receive warnings like:

 WARNING **: Couldn't connect to accessibility bus:

To suppress these warnings, execute programs with  or set that as a global environment variable.

## Titlebar background color mismatch
If you are using a window manager which uses a window decoration theme that mimics the GTK theme background color, you may find that the titlebar color no longer completely matches the application color in some GTK 3 applications. As a workaround, create the following file:
{{hc|~/.config/gtk-3.0/gtk.css|
/* Always use background color */
GtkWindow {
    background-color: @theme_bg_color;
}

/* Fix tooltip background override */
.tooltip {
    background-color: rgba(0, 0, 0, 0.8);
}

.tooltip * {
    background-color: transparent;
}

/* Fix Nautilus desktop window background override */
NautilusWindow {
     background-color: transparent;
}
}}

## Wrong focus events with tiling window managers
Define  to use GTK2 style input, instead of xinput2. === Thumbnail support for GTK file dialog ===

Install  and  to have the option to view files as thumbnails instead of list in the GTK file chooser.

## Button and menu icons
For some applications in GNOME's Wayland session, your  file is misconfigured. This can happen if you try other GTK based desktop environments. These are the offending values:

Simply set them to 0 or remove the whole file to use GNOME defaults.

## GTK 3 without polkit
GTK3 depends on polkit through colord, which is required for printing. However printing works fine without polkit installed; at least with a monochrome printer and package versions gtk3-print-backends=3.22.19-2 and colord=1.4.1-1.

## Some GTK 2 themes only change the UI color palette
Depending on the theme of choice's support for GTK 2, UI controls may still have the default Raleigh appearance, possibly with a different color palette. This is due to these themes requiring the GTK 2 Murrine engine, which is missing (GTK 2 programs should complain about it on their standard error output). Install the  package.

## Patching GTK file chooser to use regular type ahead
GTK file chooser uses the same type-ahead-find feature as GNOME/Files. This can be very jarring and does not fit in very well with other desktop environments.

Some applications support XDG Desktop Portal which allows application to use the native file chooser. If that does not work you can restore type-ahead functionality by using a patched GTK, for example .

## Text in GTK 4 applications is blurry or renders incorrectly
GTK 4 switched to grayscale antialiasing without hinting when rendering fonts. A setting is available that will restore some of the GTK 3 behavior [https://gitlab.gnome.org/GNOME/gtk/-/issues/3787#note_1260756. It is on by default for non-HiDPI screens (as of August, 2023), which should produce good results for most users. Subpixel antialiasing is not available.

## GTK 4 applications are slow
Because GTK switched to a new GPU renderer ngl (and vulkan in later versions), whose performance are worse than the old gl renderer(#6438 and possibly more issues), GTK 4 applications may feel sluggish and consume more resources than before.

This can be reverted by setting the environment variables below:

 GSK_RENDERER=gl

## GTK4 applications using the dGPU on NVIDIA Optimus setups
Recent GTK4 versions have switched to the vulkan renderer; this is problematic for users with an NVIDIA dGPU, as these will be used by default now due to GTK selecting the first usable GPU when enumerating devices and NVIDIA usually presenting the dGPU as the first one. The most reliable solution for the time being is to revert to one of the OpenGL-based renderers; this can be done by setting the  environment variable (or  for the old GL backend, which may perform better).

Alternatively, set the  environment variable; run a GTK application with  set first to find the correct device index. This has the downside of still waking up the dGPU on application start/shutdown and is more likely to break in some way if using a MUX switch to switch to the dGPU-only mode.

Finally, NVIDIA driver can be told to put the dGPU last in Vulkan device enumeration with  environment variables. While it works, it is a very bad idea to set this globally, as it will make all OpenGL applications use the dGPU ( is only respected if  is set, and the latter causes OpenGL applications to use the dGPU).

## Preview and image corruption issues on older AMD graphics cards
Users of pre-RDNA AMD graphics cards may experience some images and previews being generated glitched (#7559).

As a workaround, set the  environment variable == See also ==

* [https://www.gtk.org/ The official GTK website
* Wikipedia article about GTK
