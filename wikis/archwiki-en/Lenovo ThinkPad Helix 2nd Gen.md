# Lenovo ThinkPad Helix 2nd Gen

{| class="wikitable archwiki-table-laptop"
|-
! Hardware !! PCI/USB ID !! Working?
|-
| GPU
|
|
|-
| Sound
|
|
|-
| Wi-Fi
|
|
|-
| Bluetooth
|
|
|-
| Camera
|
|
|-
| Sensors
|
|
|-
| Fingerprint reader
|
|
|}

This hardware is substantially different from the Lenovo ThinkPad Helix 1st Gen  and thus the solutions outlined there are not helpful.
Note: the following was tested with the standard ThinkPad Ultrabook
keyboard, not the Pro one.

## Suspend & Resume
## Suspend
In order for  to work completely, you must update the BIOS to the latest version (1.99 works). Otherwise, you may only be able to suspend-to-idle and resume while docked in the keyboard (detaching to tablet mode while suspended would prevent the device from resuming).

Older versions of the BIOS misreport the suspend capabilities, and thus the system will try to suspend to RAM.

See Power management/Suspend and hibernate#Changing suspend method for manually setting the suspend method.

On the most recent BIOS versions, this is not necessary.

## Disable embedded-controller wake-ups
By default, s2idle will still exhibit a significant battery drain while suspended (the batteries will be dead within a few hours).  It appears that the device suffers from embedded controller wake-ups.  For a more reasonable drain while suspended (i.e. you can leave it suspended for days), you must set the  kernel parameter.

## Workaround for no Wi-Fi connection on resume
The Wi-Fi chip in this computer (Intel Wireless 7265) has a problem where it can stop re-connecting after waking from suspend.  The system can no longer communicate with the card, so restarting NetworkManager (etc) is not sufficient to regain a connection, nor is unloading and reloading the  module after resuming. A casual internet search reveals this to be a hardware problem that affects Windows users as well.

An effective workaround, however, is to unload the kernel modules before suspending and reloading them upon resuming. For example, using systemd:

## ACPI CPU load and Battery Power
Many ACPI Interrupt - Events are triggered on older Kernels making CPU load up to 80% of one Kernel => Battery goes empty within 3 hours.
With me this problem was fixed when upgrading to Kernel 5.1rc1. Powertop estimates over 7 hours with a pro keyboard attached.
Use tlp package for further improvements.

## Sensors
In order to use the sensors (particularly the accelerometer and the
ambient light sensor) in GNOME, you should install the
 package.  There is presumably a quirk with this sensor hardware. The effect is that  loads too early, requiring the service to be restarted before the sensors can be read properly.  To fix this, edit the systemd unit so that it starts after GDM (; see Systemd#Editing provided units).

If you are using GNOME, a program called tp-helix-orientation-lock enables the use of the "rotation lock" button on the Helix 2, as well as optionally automatically locking/unlocking the screen orientation when docking/undocking the tablet.

## Touch Screen
In order to enable multitouch, install  and
.  By default,  handles
multitouch, however it is limited to two-finger input.  In order to
allow true multitouch, you must disable this built-in support.
Multitouch events will then be passed on to XServer.  To test this,
try running

 $ xset "Wacom HID 501D Finger touch" Gesture off

To make it permanent, copy
 to
 and edit it so the input
entries all contain .

## Touch Pad and Pointing Stick
After detaching and attaching a Pro Keyboard the mouse stops working in gnome. Probably there is a sync problem.
Attempt to load psmouse with "proto=imps" option. To do that, add this line to your :

You can test this before making it permanent by:

 $ modprobe -r psmouse
 $ modprobe psmouse proto=imps

## Graphics
Install  for graphics acceleration.

## Software
## Firefox
Touch Screen Scrolling can be activated by the ScrollAnywhere firefox Plugin

## Unresolved Issues
* The fingerprint reader is apparently not supported by any driver.
* The speakers make popping sounds.
