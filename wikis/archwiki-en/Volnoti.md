# Volnoti

Volnoti is, according to its own GitHub page,
:A lightweight volume notification daemon for GNU/Linux and other POSIX operating systems. It is based on GTK and D-Bus and should work with any sensible window manager. The original aim was to create a volume notification daemon for lightweight window managers like LXDE or XMonad. It is known to work with a wide range of WMs, including GNOME, KDE, Xfce, LXDE, XMonad, i3 and many others.

Volnoti can be useful to check volume changes if you are running a lightweight window manager like Openbox, which does not usually come with a notification daemon, especially in combination with your laptop/keyboard's special keys.

## Installation
Install the  package.

## Usage
To start the daemon, run the command

 $ volnoti

Volnoti will run in background. In order to have Volnoti run automatically, autostart it. Check the program is running by typing in your terminal emulator

 $ volnoti-show 20

A semi-transparent square should appear at the centre of your screen, showing a volume of 25%. Now you should configure Volnoti to display a notification each time your volume is changed.

## Configuration
## Xbindkeys
The configuration below will use Volnoti, ALSA and Xbindkeys to show the volume changes while pressing the hotkeys; this example will assume Xbindkeys has already been install and configured as described in its page.

Open  in a text editor and add these lines before the string :

The first two commands will increase or lower the volume when the corresponding special keys are pressed, reading the new volume level and sending it as an argument to ; the third one will toggle the volume and display Volnoti's corresponding notification (according to whether the volume was muted or unmuted).

Now you can restart Xbindkeys with  and test your configuration.

## i3
Add the following three lines to your i3 configuration file:
