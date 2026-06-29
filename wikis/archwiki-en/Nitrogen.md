# Nitrogen

Nitrogen is a fast and lightweight (GTK2) desktop background browser and setter for X Window.

## Installation
Install the  package.

## Usage
Run  for full details.  The following examples will get you started:

## Setting wallpaper
To view and set the desired wallpaper from a specific directory recursively, run:

 $ nitrogen /path/to/image/directory/

To view and set the desired wallpaper from a specific directory non-recursively, run:

 $ nitrogen --no-recurse /path/to/image/directory/

## Restoring wallpaper
To restore the chosen wallpaper during subsequent sessions, autostart the following command:

 $ nitrogen --restore &

## Troubleshooting
## Freeze with dual monitors
Remove the current nitrogen configuration: https://bbs.archlinux.org/viewtopic.php?id=46245

 $ rm -r ~/.config/nitrogen/
