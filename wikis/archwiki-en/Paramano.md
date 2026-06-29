# Paramano

Paramano is a GPL-licensed GTK 3 application that lets you select your cores' governor or frequency from a tray icon and displays information about your battery graphically. Paramano is designed to be desktop-environment-independent so it depends only on GTK 3, a system tray and sudo.

## Short history
The original version was abandoned at 0.2.x.dev1-3 (sometime during 2009) and eventually failed as  became deprecated. The original project was forked and named trayfreq-archlinux with the aim of bringing trayfreq back into functionality.

It was later renamed to Paramano, initially a nonsense word which turned out to mean 'cuff' in Italian.

## Features
* Displays an icon that shows you the current CPU frequency as a proportion of the maximum
* When the CPU icon is right-clicked, it provides a menu of available frequencies and governors to choose.
* (Optional) Displays an icon that shows you the status of your battery (charging, discharging, charged) and its current charge
* Hovering over the battery icon gives the estimated time until fully charged/discharged
* Automatic switching of CPU governor based on AC adapter presence
* Configuration can be reloaded on-the-fly by sending the  signal
* Lightweight and desktop-environment-independent

## Installation
Install  from the AUR.
Then optionally edit the configuration file.
If you want to have per-user configuration, then create a configuration file in your home directory:

 $ cp /etc/paramano.conf ~/.paramano.conf

Without this, what you change in the next step will be system-wide — it is your choice.

Open the appropriate configuration file ( or ) with your favourite editor.
Everything will be commented out; un-comment what you want to use.
Note that, if a default frequency is set, it will override the governor.

## Troubleshooting and tips
A desktop file is installed into . It will automatically start once installed. If you do not want it to start automatically, open the start up manager that comes with your desktop environment and uncheck paramano.

If paramano does not seem to want to change the governor, it will be because it is detected that it is not running as root and has tried to use sudo to elevate its privileges. However, it requires that it has passwordless access to run . If you have sudo configured such that you type your password to authenticate, you will need to create the following drop-in file using the  command as root:
