# Fbsplash

Fbsplash (formerly gensplash) is a user-space implementation of a splash screen for Linux systems. It provides a graphical environment at system startup using the Linux framebuffer layer.

## Installation
## Fbsplash
Install the  package.

To have a background image of your virtual terminals you will need to install a kernel patched with fbcondecor, see below.

## Themes
Themes are available as packages and can also be found at GNOME-Look.org or KDE-Look.org.

## Configuration
## Preview
To choose from the themes that you will have installed without restarting or configuring anything, you can use  command.

This command must not be executed under X, but from a TTY.

For example to test the arch-black theme, after having installed it of course, in silent mode without restarting:

 # splash_manager -c demo -t arch-black --steps 100

For more information:

 $ splash_manager --help

## Configuration file
Add the theme (s) you installed in . You can also specify screen resolutions to save some space:

## Kernel command line
To work with Fbsplash, you must pass the following options to your kernel parameters:

 console=tty1 splash=silent,theme:theme name

## Starting
## Normal launch
Once installed and configured, without doing anything more, fbsplash should load automatically the next time you boot, right after a few Arch messages on boot (right after udev).

## Early launch
If you find these few messages unsightly (or just to enjoy your splash longer), it is possible to start fbsplash before the first messages at startup.

Just add  to HOOKS array in mkinitcpio.conf:

Then, regenerate the initramfs.

## Console background images
With a kernel that supports Fbcondecor (e.g., one with a framebuffer console decoration patch applied), you can have a background image of your virtual consoles.

## Configuration
There is also a configuration file, , to define the virtual terminals that will support this display mode.

Add the appropriate entries to your boot loader file, this kernel called  and its images  and .
