# Cwm

cwm is an X11 window manager with a focus on getting out of your way so you can be productive.
It was originally derived from evilwm, but the codebase has since been re-written from scratch.

cwm is developed as part of the OpenBSD base system. A “portable” version which runs on Linux is also available.

## Installation
Install the  package.

## Configuration
cmw is configured by editing . There is no default  file; all defaults – including the keybinds – are defined in conf.c.  lists the default keybinds;  lists all configuration directives.

You can remove all default keybinds with  and  though.

## Window groups
cwm lacks traditional ‘workspaces’; instead you can assign windows to a group. This is a more flexible approach, as two or more groups can be displayed at the same time, and is similar or identical to the workspace feature of many tiling window managers.

For example one might put a chat/irc application in group 4, and then assign a key to toggle the visibility of that group () to display that group in addition to whatever other windows/groups might be displayed.

You can also use  to show only windows from that group, hiding everything else.

The default for new windows is to not put them in any group, meaning they will always be displayed (what many WMs call ‘sticky’ windows). However by enabling “sticky group mode” with  windows will be assigned the currently selected group by default.
You can also use the  directory to automatically group windows.

## Moving windows
There is no action to move windows to pre-defined locations; but you can get around this with ; put this  script in your :

 #!/bin/sh
 # Move a window to the side of a screen.

 case "$1" in
 	"left") xdotool getactivewindow windowmove 0 y ;;
 	"top")  xdotool getactivewindow windowmove x 0 ;;

 	"right")
 		screen_width=$(xwininfo -root | grep Width | cut -d: -f2 | tr -d ' ')
 		win_width=$(xdotool getactivewindow  getwindowgeometry --shell | grep WIDTH | cut -d= -f2)
 		xdotool getactivewindow windowmove $(( $screen_width - $win_width )) y
 		;;
 	"bottom")
 		screen_height=$(xwininfo -root | grep Height | cut -d: -f2 | tr -d ' ')
 		win_height=$(xdotool getactivewindow  getwindowgeometry --shell | grep HEIGHT | cut -d= -f2)
 		xdotool getactivewindow windowmove x $(( $screen_height - $win_height ))
 		;;
 	*)
 		echo "Unsupported: \"$1\""
 		exit 1
 esac

And then bind it in cwm with something like:

 bind-key 4-h      cwm-w-mv left   # Move window to side of the screen.
 bind-key 4-j      cwm-w-mv bottom
 bind-key 4-k      cwm-w-mv top
 bind-key 4-l      cwm-w-mv right
 bind-key 4-Left   cwm-w-mv left
 bind-key 4-Down   cwm-w-mv bottom
 bind-key 4-Up     cwm-w-mv top
 bind-key 4-Right  cwm-w-mv right

This will make Mod4 (‘Windows key’) plus hjkl or the arrow keys move the window to the side.
