# Autostarting

This article links to various methods to launch scripts or applications automatically when some particular event is taking place.

## On bootup / shutdown
Enable the relevant systemd services. If an application does not provide a systemd service, write your own.

## On user login / logout
Enable the relevant user unit.

## On device plug in / unplug
Use udev rules.

## On time events
Periodically at certain times, dates or intervals:

* systemd/Timers
* Cron

Once at a date and time:

* systemd/Timers
*

## On filesystem events
Use an inotify event watcher:

* , see
* incron
*
*
* systemd can activate units on filesystem events using  files

## On shell login / logout
See Command-line shell#Configuration files.

## On Xorg startup
* xinitrc if you are starting Xorg manually with xinit.
* xprofile if you are using a display manager.

## On desktop environment startup
Most desktop environments implement XDG Autostart.

If the desktop environments has an article, see its Autostart section.

* GNOME#Autostart
* KDE#Autostart
* Xfce#Autostart
* LXDE#Autostart
* LXQt#Autostart

## On window manager startup
Many window managers (and Wayland compositors) implement XDG Autostart.

If it has an article, see its Autostart section.

* awesome#Autostart
* dwm#Autostart
* Fluxbox#Autostart
* FVWM#Autostart
* Hyprland#Autostart
* i3#Autostart
* IceWM#Autostart
* JWM#Autostart
* Labwc#Autostart
* Niri#Autostart
* Openbox#Autostart
* PekWM#Autostart
* Qtile#Autostart
* Ratpoison#Autostart
* River#Autostart
* Sway#Autostart
