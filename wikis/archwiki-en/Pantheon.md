# Pantheon

Pantheon is the desktop environment of elementary OS. It is written in Vala, using GTK 3 and Granite.

## Development
elementary OS releases are derived from Ubuntu's LTS releases, typically trailing Ubuntu's cycle by a few weeks or months. However, its constituent packages are updated continuously. See the official github repository and consult their community slack.

## Installation
## Package sources
## Official repository
The Pantheon desktop environment and elementary OS's curated applications are provided by the  group.

## Unofficial repository
extra-alucryd contains a few packages not yet available in the  group.

## AUR
PKGBUILDs for many Pantheon-related packages, such as third-party applications developed for elementary OS and unstable development packages, are available in the AUR.

## Desktop environment
For the minimal Pantheon shell, install , which pulls several dependencies and core components:
* : Window and compositing manager
* : Top panel for application launcher, clock, and indicators
* : Application launcher formerly known as "Slingshot"
* : macOS-style Dock

## Services
These optional packages provide (background) services for Pantheon and elementary OS applications:
* : Geoclue2 authentication agent
* : Polkit authentication agent
* : Print settings dialog
* : Supplemental settings daemon

## Theme and configuration
These optional packages contribute to the look and feel of the desktop:
* : LightDM greeter
* : Default appearance, behavior, and configuration.

* : Pluggable settings manager similar to

## Applications
These are some of the original, patched, and selected packages that comprise the optional elementary OS software suite:

* : Easily log into public WiFi networks
* : Web browser
* : Calculator
* : Webcam app formerly known as "Snap"
* : Text editor formerly known as "Scratch"
* : File explorer developed from Marlin
* : Audio player formerly known as "Noise"
* : Photo manager developed from Shotwell
* : Simple screencaster forked from Eidete
* : Screenshot utility
* : OS-wide shortcut overlay
* : Terminal emulator
* : Video player formerly known as "Audience" (GStreamer backend)
* : Simple scan utility

## Launching Pantheon
## Via display manager
 provides a  entry for display managers, such as LightDM.

## Autostart applications with a display manager
* Use XDG Autostarts.
* Use systemd units.

## Via xinit
Use xinitrc to launch the Pantheon shell components by appending them at the end of the file, ie:

## Autostart applications with xinit
* Run something just once, when X starts, by adding it to xinitrc before the  line.
* Use systemd units.
* Use XDG Autostarts via , , or .

## Configuration and workarounds
Configure Pantheon via  and its plugs, which must be installed separately.

Pantheon components, except for plank, store their configuration in the  or  dconf keys.

## General
## Missing D-Bus services
Pantheon components and elementary OS software are increasingly delegating certain functions to the  window manager, in preparation for the transition to Wayland. If you are using another window manager with Pantheon components or elementary OS software, you may see errors like the following:

 ** (io.elementary.screenshot:10150): ERROR **: 15:17:28.099: ScreenshotBackend.vala:37: Couldn't get dbus proxy: GDBus.Error:org.freedesktop.DBus.Error.ServiceUnknown: The name org.gnome.Shell.Screenshot was not provided by any .service files

In this situation, you have a few options:

# Downgrade to a version of the software prior to when this dbus request was implemented.
# Use the  window manager.
# Implement the missing interfaces on your own.
# Find a different software for the functionality you are seeking (e.g. a different screenshot tool)

## "No such key" when installing packages
Several dconf keys  expects are missing, as it is written for an older version of . This is not a problem, but if the messages are an annoyance, comment out or remove the specified keys from .

## Desktop
## Crashes at login
## "Oh no! Something has gone wrong."
One of the  in Pantheon's session file may be failing.

This may be worked around by removing the failed component from .

## Returns to display manager
See gnome-session crashes on session startup.

## Incorrect screen resolutions with multiple monitors
 attempts to setup monitors from , instead of Xorg configuration, which does not seem to work reliably.

An alternative is to use another greeter, such as .

## Touchpad gestures
Install . However, this package comes with some gestures that could conflict with pantheon's gestures. You can copy  to  and delete these gesture settings. For more instructions, refer to Touchegg.

## Change wallpaper and text scaling
Install  and configure in switchboard.

## Files
## Plank
See Plank.

## Not launching at startup
Since cerbere was retired,  expects plank to use this xdg autostart to initiate and request gnome-session's built in management to maintain it.

Either install , or create .

## Terminal
## Opacity
Set the dconf key  to your desired background color and opacity with an RGBA value, ie the default: .

## Wingpanel
## Indicators
Wingpanel does not come with any indicators; they must be installed separately.

At the minimum, you will probably want to install:
* : Applications menu and "Run" dialog
* : Clock and calendar widget
* : User and session menu (Switch user, Logout, Shutdown, etc.)

## Third-party indicators
When launched #Via display manager, if third-party indicators' XDG Autostarts contain , append  to it.

## Session indicator menus unresponsive
* The Lock menu item requires a Lock dbus method provided by an  dbus service.
* The Shutdown... and Log Out.. menu items request dialogs which require the  window manager to appear. If you intend to use any other window manager, an alternative is required—such as .

## Dynamic transparency
The  window manager provides Wingpanel with dynamic transparency.

With , it becomes opaque when a maximized window occupies the screen and otherwise blends with the wallpaper; using other GTK themes may produce a statically opaque panel.

To achieve the behavior within another theme, add the following code to its css or the override file, :

 /*********************
  * wingpanel support *
  ********************/

 .panel {
     background-color: transparent;
     transition: all 1s ease-in-out;
 }

 .panel.maximized {
     background-color: #000;
 }
