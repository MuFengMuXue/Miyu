# Oblogout

Oblogout is an optional, configurable logout script that presents a graphical interface (i.e. buttons) to , , , , , , and  the screen.

## Installation
Install the  package.

Although Oblogout may be used with a range of window managers, this article will focus on its use with the Openbox window manager. It may be executed as keybind and/or as a desktop menu entry.

## Keybind
To execute the script by pressing + (i.e. create a keybind for it), edit  to add the following to the appropriate part of the  section:

    true

   oblogout

## Screen locking
It will be necessary to edit  to change the   command under the  section, in order to execute the desired package installed for this purpose.

For example, where having installed XScreenSaver - which must itself also be autostarted as a Daemon process in the  file - then  would be edited accordingly:

 lock = xscreensaver-command --lock

Otherwise, where a package such as  has been installed - which does not need to be autostarted -  then an example of the necessary command (to lock with a blank screen) would be:

 lock = xlock -mode blank

## Button theme
The default button theme is . A few other themes are also available, including the pre-installed (and more elegant) . To change the button theme, edit  and change the  command under the  section. An example has been provided below for :

 buttontheme = foom

## Button display
Default buttons are available to , , , , , , and  the screen. Each button also has a configurable shortcut key assigned (e.g. once oblogout has been executed, the system may then be shutdown by pressing the  key, for example).

Both the buttons presented and their order may be configured to suit personal preference. To do so, edit and change the  command under the  section. In the example below, the  and  buttons have been removed:

 buttons = cancel, logout, lock, restart, shutdown
 #buttons = cancel, logout, restart, shutdown, suspend, hibernate, lock

Where removing or adding buttons, it will also be necessary to amend the appropriate shortcut key commands under the  section. Not doing so will mean, for example, that it will still be possible to execute certain functions via the keyboard even where the buttons for them have been removed. For the example provided above, it will be necessary to comment out the  and  shortcuts:

 shortcuts
 cancel = Escape
 shutdown = S
 restart = R
 #suspend = U
 logout = L
 lock = K
 #hibernate = H

## Dual Head
When using multiple monitors, oblogout may cover all monitors. If you only want oblogout to appear on one monitor, you can create an application rule in the Openbox  file to set oblogout's position and size.

For example, if you have two monitors, and you only want oblogout to appear on the first monitor, add to the applications section:
