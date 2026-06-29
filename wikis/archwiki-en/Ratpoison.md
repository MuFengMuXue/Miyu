# Ratpoison

Ratpoison is a manually tiling window manager written in C that allows the user to manage graphical windows without a mouse. The user interface is inspired by GNU Screen.

By default, Ratpoison keybindings work quite similarly to Emacs and GNU Screen. Commands begin by pressing the prefix key (by default ), and are then followed by another key combination such as  to move to the next window.

## Installation
Install the  package from AUR.

## Ratpoison and display managers
Many display managers (e.g., LightDM) source the available sessions from  and most window managers and desktop environments install their desktop entries there. However, Ratpoison instead creates a desktop entry file in . To allow display managers to find Ratpoison one may need to copy the Ratpoison to desktop entry . You can alternatively use a symbolic link. If the  directory does not exist, create it as root.

## Using Ratpoison
To start Ratpoison, you need to first logout and select "Ratpoison" from your Display manager.
Alternatively, you can configure xinit and use .

After X11 starts up you will see a black screen and a little textbox on the upper right of it that says "Welcome to Ratpoison".
Now type  and then  to get a list of keybindings. If you are used to GNU Screen or Tmux, you will feel at home very soon.

You are able to define custom keystrokes and even override existing ones in

Here is an example config file:

## Useful key bindings
{| class="wikitable"
! Key bindings !! Effect
|-
|    || Start any program
|-
|   || Show key bindings, even custom ones!
|-
|   || Start xterm
|-
|   || Switch to next window
|-
|   || Switch to previous window
|-
|  – || Switch to windows 1–9
|-
|   || Close the current window
|-
|   || Kill the current application
|-
|  , || Split the current frame into two vertical,horizontal ones
|-
|  , , , ,  || Switch to the next, left, top, right, bottom frame.
|-
|   || Make the current frame the only one
|-
|   || Execute a ratpoison command
|}

## Tips and tricks
## Screen reader accessibility
By default, Ratpoison is not accessible with Orca screen-reader. There is a project at gitlab.com/stormdragon2976/strychnine that replaces the default Ratpoison widgets with GTK counterparts.

Follow the on screen prompts, and you will get a  that will automatically launch Orca when it starts. See the included  for more options.

## Java applications
Java GUI applications assume stacking window managers, and do not go to fullscreen properly with the default Ratpoison configuration. See Java#Impersonate another window manager and Java#Gray window, applications not resizing with WM, menus immediately closing for solutions.

## Switch to another window manager temporarily
If a program misbehaves under Ratpoison, you can temporarily switch to another window manager.
You need to be sure that your temporary window manager doesn't kill all programs when it exits.
Notably at least IceWM is known to unfortunately not work because of that.

To switch to another window manager temporarily, you can use  Ratpoison command with

## Multiple workspaces
By default, Ratpoison only has one workspace.
But Ratpoison comes with  script that can be used to add more workspaces.

Edit your , and add:

That creates 2 workspaces. By default, you can access to them by using  to access the first,  to access the second, etc.

You can also add binds to them, like this:

 bind C-1 exec rpws 1
 bind C-2 exec rpws 2

That allows to access the first workspace with   (assuming  as your escape/prefix key).

## URxvt and xterm
URxvt and xterm, as they are installed by default, send resize hints to the window manager. This works in most tiling window managers, but not in Ratpoison. The end result is that URxvt/xterm resizes itself in multiples of the font size, rather than resizing to the whole screen, and chances that there are unfilled gaps are high. There are two solutions to this problem, documented below.

## Install a patched URxvt
If you use URxvt, the  package, among other improvements, sends no resize hints to the window manager. If you install this version of URxvt rather than the default, URxvt will resize properly within Ratpoison.

## Adjust the border
We can use the URxvt/xterm option internalBorder and set the border of Ratpoison to 0.

A trial and error process must be done to find the exact number of internalBorder for each combination of resolution and font size. (the border of Ratpoison must be set to 0 before doing the tests)
The term command line option  can be used to test for the correct number and then can be saved on the following files.

If a combination cannot be found, you could try changing the font size and the font family also (that changes the required border number).

## Autostart
Examples for launching programs when Ratpoison starts. File  is executed by Ratpoison on startup.

To launch URxvt with a Tmux session:

 exec urxvt -e bash -c "tmux -q has-session && exec tmux attach-session -d || exec tmux new-session -n$USER -s$USER@$HOSTNAME"

To launch Chromium with the cache in a tmpfs:

 exec bash -c 'pidof chromium &>/dev/null || exec /usr/bin/chromium --disk-cache-dir=~/tmp/cache'

## Wallpaper and transparency
Example for setting transparency using xcompmgr and Nitrogen.
First start nitrogen and set the desired wallpaper. Then use this in your

## Focus-follows-mouse (sloppy.c)
 is a companion program for Ratpoison and can be found in . To enable focus-follows-mouse (also called "sloppy focus"), run the following commands:

 # cd /usr/share/ratpoison/
 # gcc -o sloppy sloppy.c -lX11
 # ./sloppy

To autostart focus-follows-mouse feature, add the following to your :

## ratpoison-sloppymove
Sloppy.c inhibits continued use of the keyboard to make focus changes. An improved version of focus follows mouse which does not interfere with keyboard-driven focus changes is available

To autostart ratpoison-sloppymove, add the following to your :
