# LXQt

LXQt is a desktop environment built on Qt which derives from Razor-qt and LXDE components which were ported to Qt. While development is mainly focused on LXQt, the GTK 3 version of LXDE will see continued development.

## Installation
First, install and configure Xorg. Then, install the  group and an icon theme (e.g.  or ).

For additional functionality, you may wish to install the following:

*
*
* A screen locker, if needed. For example, slock or XScreenSaver. Both are confirmed to integrate with LXQt, others may too.
** If you are using LightDM as your display manager, you can use light-locker.
** If you want to disable screen locking upon suspend/sleep it is under LXQt > Preferences > LXQt Settings > Session Settings > Lock screen before suspending/hibernating checkbox.
* For audio support, see General recommendations#Sound system.
* Some LXQt panel plugins require extra packages to function, check the optional dependencies for .

## Starting the desktop
## Using xinit
Append the following line to Xinitrc:

## Graphical login
Choose LXQt Desktop from the menu in a display manager of choice.

## Configuration
LXQt in general tries to provide GUI applications to change its settings. Configuration files are in . This directory is initialized automatically. The default configuration for new users is found in .

## Screen Brightness
If you find that LXQt uses screen contrast control instead of screen brightness control for the screen brightness keyboard shortcuts, you can change the command to use xbacklight instead under the LXQt configuration center > shortcut keys

 xbacklight -inc 10
 xbacklight -dec 10

If you are using the Intel kernel modesetting driver xbacklight will not work, but you can use the following command instead

 pkexec lxqt-backlight_backend --inc
 pkexec lxqt-backlight_backend --dec

You may need to create two scripts for screen brightness up and down and point the keyboard shortcut to the path of the scripts for it to work.

Another way to change screen brightness is to use

 brightnessctl -d intel_backlight set +5%
 brightnessctl -d intel_backlight set 5%-

## Panel widgets
If you cannot add the CPU and System Statistics widgets to the panel, make sure  and  are installed.

## Use a different window manager
LXQt presents a dialog to pick the preferred window manager at the first login. After that, you can specify a different window manager to use with LXQt via Session Settings, ; or by editing . Change the following line:

 window_manager=current_window_manager

to a window manager of choice:

 window_manager=your_window_manager

## Wayland session
To enable and use the Wayland session install  and a supported Wayland compositor described below. The settings for the Wayland compositor and the screensaver can now be enabled under LXQt > Preferences > LXQt Settings > Session Settings ().

Supported stacking compositors are labwc,  and , while the tiling ones are hyprland, niri, River Classic and sway. For other compositors manual configuration is needed, as the compositor needs to start lxqt-session.

A conservative, lightweight choice is labwc, which in some way the successor of Openbox (X11) and therefor much similar in configuration and behavior.

Supported screensavers are hyprlock,  and . If kwin_wayland is used, the command in  Session Settings needs to be set to  to use its screen locker.

Choose LXQt (Wayland) from the menu in a display manager which supports Wayland.

From a console the LXQt Wayland Session can be started directly with .

For mouse, keyboard, monitor and shortcuts/keybindings configuration LXQt offers only limited or no support so far; check instead your Wayland compositor and/or external tools designed for Wayland support.

## Autostart
To have applications start on login, click the main menu from the LXQt > Preferences > LXQt Settings > Session Settings. Alternatively, this can be launched with:

 $ lxqt-config-session

From this window, click on AutoStart on the left side. Here you can add a new application to either the global autostart (launched in all sessions implementing the XDG Autostart specification) or your local autostart (labelled LXQt Autostart). For each item you add,  will create a Desktop entry (.desktop file) in the appropriate XDG Autostart directory.

The distinction between "Global Autostart" and "LXQt Autostart" does not depend on the directory in which the corresponding .desktop file is located, but rather on the  setting. If it is , it is considered an "LXQt Autostart". Furthermore, if , the item is not shown in .

## Set-up environment variables
Environment variables for LXQt session can be defined in Session Settings.

## Editing the Application Menu
It is possible to edit menu entries by editing their .desktop files stored in  files. See Desktop entries.

## Tips and tricks
## Screen Compositor (x11)
You can add a compositor like  to autostart applications with a command like the following
 picom --vsync -r 12 --no-fading-openclose -b

## Customizing Leave
The options available under Leave can be customized by copying the respective package provided  file to  and modifying it to contain the  directive.  Reference: #876.

Complete list of files to consider masking include:

 lxqt-hibernate.desktop
 lxqt-leave.desktop
 lxqt-lockscreen.desktop
 lxqt-logout.desktop
 lxqt-reboot.desktop
 lxqt-shutdown.desktop
 lxqt-suspend.desktop

Example: remove hibernate option.

 $ mkdir -p ~/.local/share/applications
 $ sed '/OnlyShowIn/aNoDisplay=true' ~/.local/share/applications/lxqt-hibernate.desktop

## Troubleshooting
## Desktop icons are grouped together
When moving icons on the desktop it is possible to place them a bit too close to each other making them connected. If unable to separate them Stop Desktop from Session Settings, remove  and Start Desktop again.

## Run LXQt with xrdp
Running LXQt with xrdp for remote login has the benefit of being fast and convenient, while minimizing resource consumption on the server. Setting up xrdp is rather painless, and only requires a user to adjust the . Since LXQt appears to rely on some D-Bus service functionality, that file should have the following line at the end exec dbus-run-session -- startlxqt

## Mouse cursor has different sizes on different windows (X11)
Install . LXQt saves cursor info to .Xresources and to read this info you need this package.
