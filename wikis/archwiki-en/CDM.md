# CDM

CDM is a minimalistic, yet full-featured replacement for display managers like SLiM, SDDM and GDM that provides a fast, dialog-based login system without the overhead of the X Window System. Written in pure bash, CDM has almost no dependencies, yet supports multiple users/sessions and can start virtually any desktop environment or window manager.

## Installation
Install the  package.

Now ensure no other display managers get started by disabling their systemd services.

For example, if you were using GDM, you would disable .

There is no need to enable a systemd service for CDM. Rather, a script called  will be placed into . This script (along with the rest of the scripts in ) is run when you login to a login shell. However, in order to prevent a scenario where a broken configuration prevents a user from accessing both their desktop and a virtual terminal, the script checks to see which virtual terminal it is being run on, and will by default only run on tty1.

Since the script is placed in the global  directory, CDM will be run for all users who login on tty1. If you would rather it only run for you, take away executable permissions from  and copy the contents of that file into your  for bash, or  for zsh.

## Configuration
You can configure CDM by editing . It is fully documented and should be relatively easy to figure out. You can also have user specific configuration files by copying  to .

## Menu items
Menu items are configured using three arrays: binlist, namelist and flaglist. Order of items in these arrays is important, items with the same index describe the same menu item. binlist contains commands which are executed, namelist contains names which are shown in the menu and flaglist contains type of the programs specified in binlist, either 'X' for X sessions or 'C' for console programs. Basically X sessions are started using startx (the item in binlist is argument of startx command) and console programs are started using exec.

There is a sample configuration:
 binlist=(
   "~/.xsession"                                 # Launch your X session,
   "/bin/bash --login"                           # or just execute your shell,
   "/usr/bin/fbterm"                             # or start a frame buffer console,
   "/usr/bin/cdm ~/.submenu.cdmrc"               # or go to a submenu :)
 )
 namelist=("X session" Console FBTerm "Sub menu")
 flaglist=(X C C C)

## Theming
Themes are located in , all you have to do is to pass the full path of the theme file to the  variable:

The theme syntax is fairly self explanatory, the best way to create a new theme would be to duplicate and edit an existing theme.

## Starting X
You can affect the process of starting an X server in several ways - you can specify on which tty the X server will be started (specify either number or 'keep' if you want to run the X server on current tty), and finally you can specify custom X server arguments.

## Custom commands for power operations
If you want to add entries for power operations, like shutdown or reboot, you can include them in the  array. See systemd#Power management for details.
