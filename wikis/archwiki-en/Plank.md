# Plank

Plank is a lightweight and minimal dock. Plank will not work if you are using Wayland.

## Installation
Install  or  for the development version.

## Running Plank
 $ plank

On Wayland, it may fail with the following error:

 [AbstractMain:255 Only X11 environments are supported.

In this case, it needs the following environment variable to be setXDG_SESSION_TYPE=x11

## Adding new dock icons
* Application icon: drag and drop a shortcut to the dock, or right click a running application's icon and select "Keep in dock".

* Folder or file icon: drag and drop it to the dock.

* Docklets: use their tab in the Preferences dialog.

## Configuration
Preferences can be opened by holding  and right-clicking on the dock. Select Preferences in the context menu that opens.

Although the preferences of each dock is stored in the  database and not in plain text, sometimes it makes sense to get and store that information anyway and then feed it back at some point.  Eg. backing up the settings or migrating the settings, etc.

Therefore one may want to save all the docks:

 $ dconf dump /net/launchpad/plank/docks/ > /path/where/to/save/plank/docks.ini

And then one may want to reload the saved settings:

 $ cat /path/where/saved/plank/docks.ini | dconf load /net/launchpad/plank/docks/

## Setting themes
The theme can be changed by selecting a choice in the drop-down menu of Preferences > Appearance > Theme. Themes are stored globally under  or locally under .

These custom themes can be installed to give your plank dock an eyecandy touch. Search for [https://aur.archlinux.org/packages?K=plank-theme "plank-theme" on AUR, for example  is an Arc theme for Plank.

## Multiple Docks
It is possible to run multiple plank docks at once.

Directories for each dock are stored under . Under these directories, there is a directory named 'launchers'. Going further, under this directory, docklets are stored. When the plank command is run, it either defaults to the dock1 directory or creates it if it is non-existent. If you were to run:

 $ plank -n newdock

A new directory named 'newdock' would be created under  and docklets stored under  is displayed on the dock, unless a directory under that name has already been created. This makes it possible to have multiple docks each with their own settings and preferences by specifying the name under the  flag.

For example:
 $ plank -n primdock
 $ plank -n secondock

## Applications Docklet
Plank's Applications Docklet looks for the file 'applications.menu' by default, and if that doesn't exist it will just say "No applications available". Some desktop managers, like cinnamon-desktop do not create this file, but it is very easy to fix.

 $ ln -s ~/.config/menus/cinnamon-applications.menu ~/.config/menus/applications.menu

Luckily the xml format is identical, the only difference is the name. Once you have created the symlink your Applications Docklet should work as expected!
