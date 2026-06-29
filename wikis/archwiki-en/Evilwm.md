# Evilwm

evilwm is a minimalist window manager for the X Window system. It is minimalist in that it omits unnecessary stuff like window decorations and icons. But it is very usable in that it provides good keyboard control with repositioning and maximize toggles, solid window drags, snap-to-border support, and virtual desktops. Its installed binary size is only 0.07 MB.

## Installation
Install the  package.

## Starting
Run  with xinit.

evilwm does not control the desktop background or mouse cursor, so you may want to use .

## Startup options
evilwm can read options via command line switches. Some examples:

*        (Frame color of currently active window)
*       (Width of window borders in pixels)
*       (Specifies a program to run when spawning a new terminal; default is xterm)
*     (enables snap-to-border support and specifies the proximity in pixels to snap to)
*  (override the default  keyboard modifiers)
*       (draw a window outline while moving or resizing, rather than drawing the entire window)

A full list of the evilwm options can be found in .

By default, evilwm draws a one pixel gold border around the currenly active window. An example of the use of switches to change this would be a  file such as:

 exec evilwm -snap 10 -bw 2 -fg red

This would enable

* snapping to a border within 10 pixels,
* a border width of 2 pixels,
* red for the currently active window border.

From :

:evilwm will also read options, one per line, from a file called  in the user's home directory. Options listed in a configuration file should omit the leading dash. Options specified on the command line override those found in the configuration file.

## Using evilwm
After starting evilwm you will see nothing but a mouse cursor and a black background (or other background if you specified it as above). To open a terminal, use the key combination . Programs can then be run from the terminal using .

## Keyboard controls
Using the keyboard combination of  plus a third key gives you these functions:
* &ndash; spawns new terminal
* &ndash; Deletes current window
* &ndash; Lowers current window
*,,, &ndash; Move window left, down, up, right 16 pixels
*,,, &ndash; Move window to top-left, top-right, bottom-left, bottom-right corner
* &ndash; Show information about current window
* &ndash; Maximize current window vertically (toggle)
* &ndash; Maximize current window full-screen (toggle)

## Mouse controls
By holding down the  key, you can perform these functions with the mouse:
* &ndash; Move window
* &ndash; Resize window
* &ndash; Lower window

## Virtual desktops
Using the keyboard combination of  plus a third key gives you these virtual desktop functions:

* &ndash; &ndash; Switch virtual desktop
*  &ndash; Previous virtual desktop
*  &ndash; Next virtual desktop
*  &ndash; Fix or unfix current window

To move a window from one virtual desktop to another, fix it, switch desktop, then unfix it.  can also be used to cycle through windows on the current desktop.

## Tips and tricks
## Horizontal window maximize
The key combination of  will maximize a window vertically. To maximize a window horizontally, use  to maximize it vertically, then  to maximize it horizontally (as opposed to just using  to maximize it full-screen).

## Exit evilwm by ending a program
By default, evilwm has no quit option. To exit, simply kill X with Ctrl+Alt+Backspace. If you wish, you can exit evilwm by closing a specific program. Instead of using  in your  file, you can transfer exec to another program. Killing this program will then exit evilwm. For example:

## Resize windows using the keyboard
Although not mentioned in the man-page, you can resize windows with the keyboard as well as the mouse. Using the same key-combinations for moving a window, just add the  key to the mix to resize a window.

: ,,, - Resize window smaller horizontally, larger vertically, smaller vertically, larger horizontally

## Keybindings
You can make life easier by using  to run commands in evilwm. See Xbindkeys for more details.

## Troubleshooting
## evilwm does not start
When you run evilwm, Xorg presents error messages in the log file and/or on the screen and exits. The messages may vary from system to system. Commonly,  or  is missing. Install either font to solve the problem.

See the following forum thread.

## Missing fonts.dir
If the default  successfully starts Twm but your  fails to start evilwm and  contains a warning about a missing or invalid file  in , follow the advice below the warning and run

 $ mkfontdir /usr/share/fonts/misc/

to create that file.

See also Fonts#Older applications
