# Xephyr

Xephyr is a nested X server that runs as an X application.

This may be useful to workaround a badly written application. For example, Supermicro servers may be controlled with a java ipmi kvm viewer application. While the server is rebooting, the application frequently recreates its window and steals focus from your current window. This happens several times per minute, and makes your work impossible. It is not obvious how to make a window rule that prevents such application's window from gaining focus when created, because focus must be given when launched for the first time. Using Xephyr allows you to keep these window recreations inside a separate window, which does not steal focus from your currently opened window(s).

## Installation
Install .

## Usage
If you wish to run a nested X window, you will need to specify a new display:

 $ Xephyr -br -ac -noreset -screen 800x600 :1

This will launch a new Xephyr window with a DISPLAY of ":1". In order to launch an application in that window, you would need to specify that display:

 $ DISPLAY=:1 xterm

## Launching window managers
If you want to launch a specific WM, spectrwm for example, you would type:

 $ DISPLAY=:1 spectrwm

You can also launch Xephyr with your xinitrc using startx:

 $ startx -- /usr/bin/Xephyr :1

## Grabbing and un-grabbing user input
Pressing  should lock/unlock your mouse pointer and your keystrokes inside Xephyr window exclusively if possible.

## Sending Alt+Tab
If using KDE, create a window rule to ignore global shortcuts. Then you can use  inside Xephyr.

## Tips and tricks
Other examples for situations where Xephyr can be useful are:
# A testing environment for an X application, or feature, in which the tester would like to keep working in their usual X environment, yet defending the other applications from failures of the application under test.
# OpenSSH#Remote emphasize 3 settings in the sshd server  configuration file for OpenSSH#X11 forwarding (over ssh). 2 of these, out of 3, are the default settings. When the ssh client can not influence the ssh server administrator to set the 3rd one, , to yes,  Forwarding X11 over ssh uses Xephyr as a work around to be installed in the ssh client machine.
