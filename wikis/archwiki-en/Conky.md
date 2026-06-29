# Conky

Conky is a system monitor software for the X Window System, Wayland and other things, too. It is available for GNU/Linux and FreeBSD. It is free software released under the terms of the GPL license. Conky is able to monitor many system variables including CPU, memory, swap, disk space, temperature, top, upload, download, system messages, and much more. It is extremely configurable, however, the configuration can be a little hard to understand. Conky is a fork of torsmo.

## Installation
Install the  package. There are also alternative packages you can install with extra compile options enabled:

*  - conky without X11 dependencies
*  - with both Lua and NVIDIA support

Some built in variables in conky require additional packages to be installed in order to be utilized, for example mpd for music. As for hard drive temperature, see  lm_sensors#S.M.A.R.T. drive temperature. From Conky's point of view,  can be used as a replacement for the hddtemp package and variable by using its  variable.

Additional utility:

*

## Configuration
The configuration file can be located in one of the following paths (the first one found will be used):

*
*
*

If none of these files exist, conky will use the default built-in configuration, which you can print out with:

 $ conky --print-config

Furthermore, you can create a default configuration file with the following command:

 $ mkdir -p ~/.config/conky && conky --print-config > ~/.config/conky/conky.conf

If you prefer to have a configuration dotfile in home, you can create a file elsewhere and tell conky to use it using arguments.

For example to tell conky to use a dotfile located in the user's home directory:

 $ conky --config=~/.conky.conf

Additional example configuration files are available in the upstream wiki article.

When editing your configuration file while conky is running, conky will update with the new changes every time you write to the file.

See the SourceForge page for a complete reference for all Conky objects/variables; these are also listed in .

## Dual screen
When using a dual screen configuration, you will need to play with a few options to place your conky window where you want it on the desktop.

By adjusting , let us say you are running a 1680x1050 pixels resolution and you want the window on middle top of your left monitor, you will use:

 alignment = 'top_left',
 gap_x = 840,

The  option is self-explanatory, the  is the distance, in pixels, from the left border of your screen.

 is an alternative useful option, the following will place the conky window at the top right of the second screen:

 alignment = 'top_right',
 xinerama_head = 2,

## Fonts
For displaying Unicode pictures and emoji with conky you will need a font that supports this and then configure conky to use the font with the Unicode you want to display. For example:

  ${font Symbola:size=48}☺${font}

## Symbolic fonts
Symbolic fonts are also very commonly used in more decorated conky configurations, some of the more popular ones include;

*
*  - PizzaDude Bullet's font
*  - Erik flowers weather icon font with 222 glyphs

## Autostart
There are several different ways to start Conky automatically, as outlined in Autostarting.

Conky has a configuration setting which will tell it to fork to the background. This may be desirable for some autostarting setups.

In :

 conky.config = {
     background = true,
 }

If you use a graphical desktop environment and wish to use a  file for autostarting, use the following:

The  parameter delays conkys drawing for 5 seconds at startup to make sure that the desktop had time to load and is up.

## Troubleshooting
These are known issues people have with conky and their solutions.

## Conky starts and does not display anything on the screen
First check for syntax errors in your configuration file's text variable. Then double check that your user has permission to run every command inside your configuration file and that all needed packages are installed.

## Do not minimize on Show Desktop
Using Compiz: If the 'Show Desktop' button or key-binding minimizes Conky along with all other windows, start the Compiz configuration settings manager, go to "General Options" and uncheck the "Hide Skip Taskbar Windows" option.

Using XFCE: If clicking the desktop hides Conky, add  inside .

For the other desktop environments/window managers: Try editing  and adding/changing the following line:

 own_window_type = 'override',

or

 own_window_type = 'desktop',

Refer to  man page for the exact differences. But the latter option enables you to snap windows to conkys border using resize key-binds in e.g. Openbox, which the first one does not.

## Integrate with GNOME Shell
Some have experienced problems with conky showing up under GNOME.

Add these lines to :

 own_window = true,
 own_window_type = 'desktop',

## Prevent flickering
Conky needs Double Buffer Extension (DBE) support from the X server to prevent flickering because it cannot update the window fast enough without it. It can be enabled with Xorg in  with  line in  section. The  file has been replaced (1.8.x patch upwards) by  which contains the particular configuration files. DBE is loaded automatically as long as it is present within . The list of loaded modules can be checked with .

To enable double buffering, add the  option to :

  conky.config = {
      double_buffer = true,
  }
