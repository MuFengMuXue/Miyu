# ThinkFinger

ThinkFinger is a driver for the SGS Thomson Microelectronics fingerprint reader found in older IBM/Lenovo ThinkPads.

ThinkWiki has a list of various fingerprint readers found in ThinkPads. Newer models using different readers might not work with ThinkFinger.

## Installation
Install the  package.

## Configuration
The  module needs to be loaded.

## TF-Tool
Use  to test ThinkFinger. You will have to run this as root because a direct access to the USB devices is needed.
Run  to generate a file at  and  to see if it identifies you correctly.
 acquires and stores your fingerprint in , which is needed for an authentication with PAM.

## PAM
See PAM.

## /etc/pam.d/login
Change the file  to look like this if you want to use your fingerprint to authenticate yourself on logon:

## /etc/pam.d/su
Change this file to confirm the  command with a finger-swipe:

## /etc/pam.d/sudo
Change this file to confirm the  command with a finger-swipe:

## /etc/pam.d/xscreensaver
XScreensaver is a bit tricky. First, configure PAM with a file  containing:

This still will not work because Xscreensaver cannot read/write from  and . A udev rule must be written to authorize a new group read/write access.

First, create a new group, let us say fingerprint:

 # groupadd fingerprint

Add the user you want to be able to unlock Xscreensaver with the fingerprint reader to the group:

 # gpasswd -a  fingerprint

Logout and login again for the changes to take effect.

Next, search for uinput and bus/usb in your udev rules directory:

{{bc|1=
$ grep -in "bus/usb" /etc/udev/rules.d/*

/etc/udev/rules.d/udev.rules:318:SUBSYSTEM=="usb_device", ACTION=="add", PROGRAM="/bin/sh -c 'K=%k; K=$${K#usbdev};printf bus/usb/%%03i/%%03i $${K%%%%.*} $${K#*.}'", NAME="%c", MODE="0664"
/etc/udev/rules.d/udev.rules:320:SUBSYSTEM=="usb", ACTION=="add", ENV{DEVTYPE}=="usb_device", NAME="bus/usb/$env{BUSNUM}/$env{DEVNUM}", MODE="0664"
}}

Copy the lines you found with grep in the previous step to a new udev rules file:

{{hc|head=/etc/udev/rules.d/99fingerprint.rules|output=
KERNEL=="uinput",  NAME="misc/%k", SYMLINK+="%k", MODE="0660", GROUP="fingerprint"
SUBSYSTEM=="usb_device", ACTION=="add", PROGRAM="/bin/sh -c 'K=%k; K=$${K#usbdev};printf bus/usb/%%03i/%%03i $${K%%%%.*} $${K#*.}'", NAME="%c", MODE="0664", GROUP="fingerprint"
SUBSYSTEM=="usb", ACTION=="add", ENV{DEVTYPE}=="usb_device", NAME="bus/usb/$env{BUSNUM}/$env{DEVNUM}", MODE="0664", GROUP="fingerprint"}}

The difference between the rules in  and those in  should only be the addition of  or  at the end of the lines.

After adding the custom udev rules, you should give your user permissions to access their own fingerprint file:

As a last step, you need to remove the root setuid from , otherwise Xscreensaver will not be able to unlock with the fingerprint reader:

 # chmod -s /usr/bin/xscreensaver

## /etc/pam.d/gdm
Edit  and add the following line to the top:

Then modify  to look like this:

## /etc/pam.d/xdm
Edit  to look like this:

## /etc/pam.d/slim
Append the following to :

Now restart SLiM and you may use the fingerprinter to login.

## Alternative fingerprint reader software
Fprint is an alternative fingerprint reader software that works with some of the newer ThinkPad fingerprint readers.
