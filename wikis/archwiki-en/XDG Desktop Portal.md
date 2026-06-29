# XDG Desktop Portal

From the Flatpak documentation:

:Portals are the framework for securely accessing resources from outside an application sandbox. They provide a range of common features to applications, including: determining network status, opening a file with a file chooser, opening URIs, taking screenshots and screencasts Portals were designed for use with applications sandboxed through Flatpak, but any application can use portals to provide uniform access to features independent of desktops and toolkits. This is commonly used, for example, to allow screen sharing on Wayland via PipeWire, or to use file open and save dialogs on Firefox that use the same toolkit as your current desktop environment.

## Installation
Install  and one or more backends. The package includes a systemd/User service that will be automatically started via D-Bus.

## Backends
When an application sends a request to the portal, it is handled by , which then forwards it to a backend implementation. This allows implementations to provide suitable user interfaces that fit into the user's desktop environments, and access environment-specific APIs for requests like opening a URI or recording the screen. Multiple backends can be installed and used at the same time. For example, a Sway setup may use  for screen sharing support and  as a fallback for all other interfaces that xdg-desktop-portal-wlr does not implement.

Portal backend definitions are located in . Each portal backend file contains a list of interfaces that it can handle, and the desktop environments which it supports.

## List of backends and interfaces
The following table lists all backends available and their support for certain common interfaces.

{| class="wikitable"
|-
! Backend !! Supported environment !! Toolkit !! Access portal !! Account portal !! App chooser portal !! Background portal !! Clipboard portal !! Dynamic launcher portal !! Email portal !! File chooser portal !! Global shortcuts portal !! Inhibit portal !! Input capture portal !! Notification portal !! Print portal !! Remote desktop portal !! Screen cast portal !! Screenshot portal !! Secret portal !! Settings portal !! Wallpaper portal
|-
|  || COSMIC || iced ||  ||  ||  ||  ||  ||  ||  ||  ||  ||  ||  ||  ||  ||  ||  ||  ||  ||  ||
|-
|  || Deepin || Qt 6 ||  ||  ||  ||  ||  ||  ||  ||  ||  ||  ||  ||  ||  ||  ||  ||  ||  ||  ||
|-
|  || GNOME || GTK 4 ||  ||  ||  ||  ||  ||  ||  ||  ||  ||  ||  ||  ||  ||  ||  ||  ||  ||  ||
|-
|  || generic || GTK 3 ||  ||  ||  ||  ||  ||  ||  ||  ||  ||  ||  ||  ||  ||  ||  ||  ||  ||  ||
|-
|  || Hyprland1 || Qt 6 ||  ||  ||  ||  ||  ||  ||  ||  ||  ||  ||  ||  ||  ||  ||  ||  ||  ||  ||
|-
|  || KDE Plasma || Qt 6 ||  ||  ||  ||  ||  ||  ||  ||  ||  ||  ||  ||  ||  ||  ||  ||  ||  ||  ||
|-
|  || wlroots || iced ||  ||  ||  ||  ||  ||  ||  ||  ||  ||  ||  ||  ||  ||  ||  ||  ||  ||  ||
|-
|  || LXQt || Qt 6 ||  ||  ||  ||  ||  ||  ||  ||  ||  ||  ||  ||  ||  ||  ||  ||  ||  ||  ||
|-
|  || Phosh || GTK 4 ||  ||  ||  ||  ||  ||  ||  ||  ||  ||  ||  ||  ||  ||  ||  ||  ||  ||  ||
|-
|  || theDesk || Qt 6 ||  ||  ||  ||  ||  ||  ||  ||  ||  ||  ||  ||  ||  ||  ||  ||  ||  ||  ||
|-
|  || wlroots ||  ||  ||  ||  ||  ||  ||  ||  ||  ||  ||  ||  ||  ||  ||  ||  ||  ||  ||  ||
|-
|  || Cinnamon2 ||  ||  ||  ||  ||  ||  ||  ||  ||  ||  ||  ||  ||  ||  ||  ||  ||  ||  ||  ||
|}

# Works with all wlroots-based compositors, but provides extra functionality when used with Hyprland such as sharing individual windows.
# Provides partial support also for MATE and Xfce.

The following packages provide a specific backend only, and not specific to a desktop environment:

*  implements the Settings portal backend (only for color scheme setting).
*  implements the Secret portal backend.
*  implements the Secret portal backend.
*  implements the File chooser portal backend with its own GUI application.
*  implements the File chooser portal backend. It can spawn interactive terminal sessions with shell shims for selecting files using any command-line tools. Also supports headless mode for controlling dialogs from existing terminals without spawning new windows, and queue mode for pre-selecting files before applications even request the dialog.
*  implements the File chooser portal backend. It redirects requests to GNOME/GTK/KDE/LXQt backends.
*  implements the File chooser portal backend. It allows using a terminal file manager as a file chooser.
*  is a new fork for the now archived xdg-desktop-portal-termfilechooser-git that implements the File chooser portal backend and allows using a terminal file manager as a file chooser.

## Configuration
When a request is made,  will use the  file, where DE is based on the  environment variable. These files are provided by the desktop environments themselves and determine which backends should be used when a specific environment is running.

If you want to override the desktop environment defaults, or your desktop environment does not provide a default configuration, you may create a portal configuration file at  to determine which backends you want to use, either generally or for each individual interface. If you use multiple desktop environments, you may also create multiple  files for each environment.

For example, if your desktop environment does not have a portal backend, and you want to use  as a generic fallback but also use the LXQt file picker through , you can use the following configuration:

See  for more information.

## Force desktop environment
In some cases, such as when you have a standalone window manager, you might want to make  to think you are using a specific desktop environment. This can be achieved by setting the XDG_CURRENT_DESKTOP environment variable for the  user unit using a drop-in snippet. For example, to use the backend associated with KDE:

## Troubleshooting
## Portal does not start
For  and  to work, the  and  environment variables have to be set in the systemd user session.

 has to be set to the name of your compositor, e.g. .  is set automatically by the compositor.

Check whether these variables are set with . If they are not set, import these environment variables into the systemd user session and dbus by running the following commands before launching the compositor (e.g., include them in the compositor's configuration file).

 $ systemctl --user import-environment WAYLAND_DISPLAY XDG_CURRENT_DESKTOP
 $ dbus-update-activation-environment --systemd WAYLAND_DISPLAY XDG_CURRENT_DESKTOP=compositor_name

See [https://github.com/emersion/xdg-desktop-portal-wlr#running and for more details.

## Using multiple monitors with xdg-desktop-portal-wlr
 requires an external chooser to select the shared monitor. By default, it looks for ,  and  in this order. When using slurp, after a request for screen sharing you will be presented with a crosshair cursor and you will need to click the screen you want to share. When using wofi or bemenu, you will be presented with a menu of available displays to share. If no choosers are available,  will fallback to the first monitor found. For more information, see .

## Poor font rendering in GTK applications on KDE Plasma
Some GTK apps require  on Plasma in order to render font correctly. Install it and then run:

 $ /usr/lib/xdg-desktop-portal --replace

## GTK (possibly others) file chooser not working
If the application runs on X via Xwayland (easiest way to check is to run  and see whether they follow the mouse over the application in question), then  will show up on demand, but after you select the file nothing will happen. In that case adding  to the  environment might help. To do this, you can either follow the instructions above about  or just edit the systemd user unit file of . Alternatively, you can force the application under Wayland (e.g. if it is using Electron).
