# Mad Catz Mouse

Mad Catz produces a series of gaming mice, for example the Saitek Cyborg R.A.T.3 Mouse (7 buttons USB wired) or the R.A.T9 (7 buttons USB wireless).  The mice do not work properly in X without some reconfiguration.  This article explains how to make it work with any desktop manager.

## Installation
No driver installation is required.
The mouse should be detected at boot or whenever it is hot-plugged.

## Issues
After being plugged, the mouse seems to work, but you may experience different issues :

* You cannot move windows around when grabbing the window's title bar. (happens with Openbox and other Window manager)
* You cannot click on buttons.
* You cannot get the focus on windows.
* You cannot open menus, even with keyboard shortcuts.
* Display does not refresh (using Xcompmgr)
* Closing certain windows restores functionality until the mouse locks into a new window.

## The Disable Button Solution
## On Xorg
The issues are caused by an interaction between R.A.T Mode button and the X Server. To restore proper functionality, the 'Mode' button must be disabled, as follows:

With root privileges, create the file  (see xorg) with the following content :

 Section "InputDevice"
     Identifier     "Mouse0"
     Driver         "evdev"
     Option         "Name" "Saitek Cyborg R.A.T.3 Mouse"
     Option         "Vendor" "06a3"
     Option         "Product" "0ccc"
     Option         "Protocol" "auto"
     Option         "Device" "/dev/input/event4"
     Option         "Emulate3Buttons" "no"
     Option         "Buttons" "7"
     Option         "ZAxisMapping" "4 5"
     Option         "ButtonMapping" "1 2 3 4 5 6 7 0 0 0 0 0 0 0"
     Option         "Resolution" "3200"
 EndSection

After restarting your X server, the mouse should be fully functional, including the two lateral buttons. You may restart the X server by restarting the display manager service, for example ,  etc... If not, or if you need more information about configuring gaming mice, see All Mouse Buttons Working.

## On Wayland
Creating a Xorg config file has no effect on wayland, and wayland doesn't have a direct way to disable the mode button. Udev can be used instead to disable the button.

Get the name of your mice with  and the keys triggered when clicking the mode button with .
Then with root privileges, create the file  with the following content (replacing the name and the codes):

 evdev:name:Mad Catz Mad Catz R.A.T.TE:*
  KEYBOARD_KEY_90009=reserved    # Bouton 280
  KEYBOARD_KEY_9000a=reserved    # Bouton 281
  KEYBOARD_KEY_9000b=reserved    # Bouton 282

Then unplug the mice, reload the configuration file with  and plug the mice again.

## RAT7 or RAT9 Partial Fix
This is the configuration file that will get your R.A.T. 7 or R.A.T. 9 mouse working properly under Linux.
*Does not fix the change-profile button for RAT9, this profile needs more adjustment or just do not push it.

:

 Section "InputClass"
   Identifier "Mouse Remap"
   MatchProduct "Mad Catz Mad Catz M.M.O.7 Mouse|M.M.O.7"
   MatchIsPointer "true"
   MatchUSBID "0738:1713"
   Driver "evdev"
   Option "Buttons" "24"
   Option "ButtonMapping" "1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 0 21 22 23 24"
   Option "AutoReleaseButtons" "20"
   Option "ZAxisMapping" "4 5 6 7"
 # Option "Resolution" "3200"
 # Option "ConstantDeceleration" "2"
 EndSection

You can define different keystrokes applied to each mouse button by defining them in  eg.:

 # pressing mouse button 7 sends keystroke: 2
 "xvkbd  -text 2"
        m:0x0 + b:7
 # pressing mouse button 8 sends keystroke: Space
 "xvkbd  -text "\m:0x0 + b:8
 # pressing mouse button 9 sends keystroke: F8
 "xvkbd  -text "\[F8""
        m:0x0 + b:9
 # pressing mouse button 10 sends keystroke: CursorLeft
 "xvkbd  -text "\m:0x0 + b:10
 # pressing mouse button 11 sends keystroke: Shift+F2
 "xvkbd  -text "\[Shift\m:0x0 + b:11

A very good article on setting up the Mad Catz M.M.O.7 mouse with Linux is written [https://delightlylinux.wordpress.com/2013/07/29/using-the-mad-catz-m-m-o-7-with-linux-mint-and-ubuntu/ here.

## Manual Button Mapping Fix
Please note that there are two different versions of the R.A.T.3 mouse which are Saitek and Madcatz, this must be input correctly into the "MatchProduct" or you will run into the same issues.

First find out the ID and the Name of the mouse :

 xinput list | grep "id"

In you should see your mouse labeled as "Madcatz Mad Catz R.A.T.3 Mouse" or "Saitek Cyborg R.A.T.3 Mouse". Note the device id number and then input the following command :

 xinput query-state ID

(Where ID corresponds to the ID number of your mouse)

Note which 'mode' color is currently active (red/blue/purple) and which button numbers correspond to the current 'mode' by being either "up" or "down". Change the mouse 'mode' and and retype the above command, noting which buttons change state to match the 'mode'.

Example:

 U = up
 D = down
                         U U U U U D D U U D D D  U  U
 Option "ButtonMapping" "1 2 3 4 5 0 0 8 9 0 0 0 13 14"

Where buttons 10, 11, and 12 have been identified as 'mode' buttons, so they can be disabled by with zeros.

When you have identified which button numbers correspond to the mouse 'modes', you should be able to edit your  file and disable them by inserting a zero in the appropriate point in the button sequence.

Open in your chosen editor:

 /etc/X11/xorg.conf   or
 /etc/X11/xorg.conf.d/910-rat-xx.conf

Create a block that overwrites the mode buttons as listed for your mouse model in chapter Mouse Configurations:

MadCatz R.A.T.3:

 # RAT3 mouse
 Section "InputClass"
  Identifier "Mouse Remap"
  MatchProduct "Madcatz Mad Catz R.A.T.3 Mouse"
  MatchDevicePath "/dev/input/event*"
  Option "ButtonMapping" "1 2 3 4 5 6 7 8 9 0 0 0 13 14 15 16 17 18"
 EndSection

## Use extra mouse buttons with Wine/Games
Install  and add your user to  group and relogin to activate changes.

 # gpasswd -a  input

Edit the evrouter configuration file and change the `eventX` number to the event number the mouse uses with

 $ evrouter --dump /dev/input/event*

Then assign any hotkeys to any mouse button. Preferably use not often used keystrokes to not interfere with others already used as in the example .

Start with:

 $ evrouter /dev/input/event*

Stop with:

 $ evrouter -q && rm -f /tmp/.evrouter*

## R.A.T. configuration software
Saitek/Mad Catz does not provide any official configuration software for Linux.

There is however open an source project which allows you to configure DPI settings for each and mode here.

It might however require some tweaking for certain R.A.T. mice, such as adding your mouse ID to the list of supported IDs.

## Mouse Configurations
It is recommended that you put those settings in a single file for each model you use, eg. .

## Mad Catz R.A.T. 5
 Section "InputClass"
    Identifier "Mad Catz R.A.T. 5"
    MatchProduct "Mad Catz Mad Catz R.A.T.5 Mouse"
    MatchDevicePath "/dev/input/event*"
    Option "Buttons" "21"
    Option "ButtonMapping" "1 2 3 4 5 0 0 9 8 7 6 10 0 0 0 0 0 0 0 0 0"
    Option "ZAxisMapping" "4 5 11 10"
    Option "AutoReleaseButtons" "13 14 15"
 EndSection

## Mad Catz M.M.O.7
 Section "InputClass"
  Identifier "Mouse Remap 7"
  MatchProduct "Mad Catz Mad Catz M.M.O.7 Mouse|M.M.O.7"
  MatchIsPointer "true"
  MatchUSBID "0738:1713"
  Driver "evdev"
  Option "Buttons" "24"
  Option "ButtonMapping" "1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 0 21 22 23 24"
  Option "AutoReleaseButtons" "20"
  Option "ZAxisMapping" "4 5 6 7"
 EndSection

## Mad Catz R.A.T. TE
 Section "InputClass"
    Identifier     "Mouse Remap"
    MatchProduct   "Mad Catz Mad Catz R.A.T.TE"
    MatchDevicePath "/dev/input/event*"
    Option         "ButtonMapping" " 1 2 3 4 5 6 7 8 9 10 11 12 0 0 0"
    Option        "ZAxisMapping" "4 5 6 7"
 EndSection

## Mad Catz M.M.O. TE
 Section "InputClass"
  Identifier "Mouse Remap TE"
  MatchProduct "Mad Catz Mad Catz M.M.O.TE"
  MatchIsPointer "true"
  MatchUSBID "0738:1714"
  Driver "evdev"
  Option "Buttons" "24"
  Option "ButtonMapping" "1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24"
  Option "AutoReleaseButtons" "20"
  Option "ZAxisMapping" "4 5"
  Option "ConstantDeceleration" "2"
 EndSection

## Saitek Cyborg R.A.T.3
 # RAT3 mouse
 Section "InputClass"
  Identifier "Mouse Remap"
  MatchProduct "Saitek Cyborg R.A.T.3 Mouse"
  MatchDevicePath "/dev/input/event*"
  Option "ButtonMapping" "1 2 3 4 5 0 0 8 9 0 0 0 13 14"
 EndSection
