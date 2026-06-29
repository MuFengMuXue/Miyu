# 2bwm

From upstream:
:A fast floating WM, with the particularity of having 2 borders, written over the XCB library and derived from mcwm written by Michael Cardell. In 2bwm everything is accessible from the keyboard but a pointing device can be used for move, resize and raise/lower.

## Installation
Install the  package. Although the installation process can be automatic, if directly building from the AUR, it is highly recommended to read and edit the config.h file in the source directory.

## Starting
Run  with xinit.

## Using 2bwm
After the launch of 2bwm, a mouse cursor, a background, and a terminal will be the only thing on the screen (as specified in the .xinitrc). To open a terminal, using the default configuration, hit . Use the terminal as desired, for example to start a program with , however it is easier and more convenient to use a menu to launch programs, for instance dmenu or .

## General commands
*  &ndash; exit 2bwm
*  &ndash; restart 2bwm
*  &ndash; start the menu
*  &ndash; start a terminal
*  () &ndash; move the cursor (with  fast).

## Window controls
Using the  key combined with one of the key below on a specific focused window:

*  &ndash; close window.
*  or  &ndash; go to the next window in the current workspace window ring.
*  &ndash; fix a window, making it visible on all workspaces (toggles).
*  &ndash; make a window unkillable by  (toggles).
*  &ndash; raise or lower (toggles).
*  &ndash; iconify (or hide) a window from the display.

## Move, resize and teleport a window
Using the  key combined with one of the key below on a specific focused window:

*  &ndash; maximize (toggles).
*  &ndash; maximize vertically (toggles).
*  &ndash; maximize horizontally (toggles).
*  () &ndash; resize left (with  slow).
*  () &ndash; resize down (with  slow).
*  () &ndash; resize up (with  slow).
*  () &ndash; resize right (with  slow).
*  &ndash; grow keeping aspect.
*  &ndash; shrink keeping aspect.
*  () &ndash; move left (with  slow)
*  () &ndash; move down (with  slow)
*  () &ndash; move up (with  slow)
*  () &ndash; move right (with  slow)
*  &ndash; move to the upper left corner of monitor.
*  &ndash; move to the upper right corner of monitor.
*  &ndash; move to the lower left corner of monitor.
*  &ndash; move to the lower right corner of monitor.
*  &ndash; move to the center of monitor.
* /// &ndash; move to the left/right/bottom/top while maxvert/maxhor and half max horizontal/vertical.

## Workspaces
* &ndash; &ndash; go to workspace , 0&ndash;9.
*  &ndash; send to workspace .
*  or  &ndash; go to next/previous workspace.
*  or  &ndash; move window to previous/next monitor.

## Mouse controls
By holding the  Key, the mouse buttons act as follows:

* Button 1 on a window &ndash; move window
* Button 3 on a window &ndash; resize window
* Button 3 +  on the desktop &ndash; start the menu specified in .

Note that all functions activated from the keyboard work on the currently focused window regardless of the position of the mouse cursor. Of course, changing workspaces has nothing to do with the focused window.

You may change the keyboard mappings from .

## Tips and tricks
## Get the current workspace number using a script
The following command yields the current workspace:

 $ xprop -root _NET_CURRENT_DESKTOP | sed -e 's/_NET_CURRENT_DESKTOP(CARDINAL) = //'

## Easy to remember outer border colours
A simple trick to remember the meaning of the outer border colours would be by setting, for example, "fixed" to blue, "unkillable" to red, and "fixed + unkillable" to purple. The mix of blue and red create purple!

## Top left squares
Setting  to a negative number will make the outer border turn into a square located in the top-left corner of the full-border. The colours set for the outer borders now stick to the square.
