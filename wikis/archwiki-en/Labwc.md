# Labwc

Labwc stands for Lab Wayland CompositorAccording to [https://labwc.github.io/ the official website:

:Labwc is a wlroots-based window-stacking compositor for Wayland, inspired by Openbox.
:It is lightweight and independent with a focus on simply stacking windows well, and rendering some window decorations. It relies on clients for panels, screenshots, wallpapers, and so on to create a full desktop environment.
:Labwc tries to stay in keeping with wlroots and sway in terms of general approach and coding style.
:Labwc only understands wayland-protocols & wlr-protocols, and cannot be controlled with dbus, sway/i3-IPC, or other technology. The reason for this is that we believe that custom IPCs and protocols create a fragmentation that hinders general Wayland adoption.

## Installation
Labwc can be installed with the  package.

## Starting
You can start it by typing  in the Linux console or using a Wayland-compatible display manager.

## Configuration
Following files can be used for configuration:
; : For general configuration.
; : For menu layout.
; : Script executed when launching labwc.
; : Script executed when launching Xwayland.
; : Script executed when exiting labwc.
; : For environment variables in the session.
; : For additional theme settings.

Example files are provided in . Especially,  contains all the default configurations.

To check the xml files for syntax errors, e.g. with  from :

 $ if xmllint --noout ~/.config/labwc/rc.xml; then echo "xml syntax ok"; else echo "xml syntax error"; fi

In case a configuration file has a faulty syntax, a default config will be used.

To apply configuration changes reload the compositor (by sending SIGHUP to `$LABWC_PID`):

 $ labwc --reconfigure

See  and  for further details.

 is a GUI settings application, which manages settings in  and .

## Autostart
Preferred place for starting wayland-only applications is .
Scripts are executed when launching labwc. "&" is not needed for daemons. For example:

Example to start a screenlocker after 300 seconds of idle time:

## Keymap
The keyboard layout can be configured by setting environment variables in . For example:

See  for details.

## Activating numlock on startup
Numlock is not set by default, set it on in  section:

## Outputs
A cli utility to manage outputs of a Wayland compositor is . For example:

A Wayland equivalent for the X11 tool like  is kanshi.

 is a graphical application for configuring Wayland displays.

## Statusbar
Use external tools like  and  can be used to show status bars. For example:

## Wallpaper
Use external tools like ,  and  can be used to show backgrounds. For example:

## Custom keybindings
Keybindings are configured by adding  sections with . For example:

## Workspaces
Workspaces are configured in  section and switched with keybindings. For example:

## Menu
Labwc follows Openbox's syntax for menu configuration in . For example:

Also, you can use menu generators for Openbox like  and .

See  for details.

## Themes
Labwc loosely follows Openbox 3 theme specification. You can install themes to the following directories:
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

These directories contain  which defines the theme colors and geometries, and button icon files like  and .
XBM, SVG and PNG formats are supported for icon files.

Additionally, you can override the theme entries with .

labwc-artwork provides some themes for labwc.

See  for details.

## Xwayland
 starts automatically if Xwayland support is enabled at build time. To force disable it, set:

## wlroots renderer
The default renderer is OpenGL and sufficient for normal desktop usage.

To use another renderer such as Vulkan for modern gaming, heavy 3D workloads or advanced GPU compute, see Wayland#Use another renderer for wlroots based compositor.

To see which renderer is in use see  from .

## Tips and tricks
## Screen capture
See Screen capture#Wayland for selecting a Wayland / Wlroots-based compatible compositor.
