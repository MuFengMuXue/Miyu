# Lenovo ThinkPad Helix

{| class="wikitable"
|+ Hardware Information
! Form Factor
| Tablet/Ultrabook Convertible (detachable keyboard dock)
|-
! Display
| 11.6" 1920x1080 LCD with Capacitive and Pen Digitizers
|-
! CPU
| 3rd Generation (Ivy Bridge) Core i5-3427U or i7-3667U
|-
! RAM
| 4GiB (i5) or 8GiB (i7) DDR3L RAM (dependent upon CPU)
|-
! Storage
| 128/160/256GB mSATA SSD
|-
! WiFi
| Intel Centrino Advanced-N 6205S mPCI WLAN
|-
! Bluetooth
| Broadcom BCM20702 Bluetooth 4.0 (USB connected)
|-
! Camera
| 5MP Rear and 2MP Front (also USB)
|}

For the second generation of Helix hardware (models 20CG and 20CH), see Levovo ThinkPad Helix 2nd Gen.

## Installation
Due to the fact that there is no optical drive, you need to use a USB flash installation medium.

## Digitizers
The Lenovo Helix comes with the following input devices (the ids may not be the same on your system):

 $ xinput list
 ⎡ Virtual core pointer                    	id=2	pointer  (3)
 ⎜   ↳ Virtual core XTEST pointer              	id=4	pointer  (2)
 ⎜   ↳ Wacom ISDv4 EC Pen stylus               	id=15	pointer  (2)
 ⎜   ↳ Atmel Atmel maXTouch Digitizer          	id=16	pointer  (2)
 ⎜   ↳ SynPS/2 Synaptics TouchPad              	id=18	pointer  (2)
 ⎜   ↳ TPPS/2 IBM TrackPoint                   	id=19	pointer  (2)
 ⎜   ↳ Wacom ISDv4 EC Pen eraser               	id=21	pointer  (2)

A Wacom USB device recognized by the  driver will create multiple X input devices from a single kernel device.  In the Lenovo Helix's case, three such X input devices are created when properly configured:

* Wacom ISDv4 EC Pen stylus
* Wacom ISDv4 EC Pen eraser
* Atmel Atmel maXTouch Digitizer

The Wacom ISDv4 EC Pen stylus xinput device is recognized by the  driver out of the box.  However, additional Udev and Xorg configuration is required to recognize the Atmel Atmel maXTouch Digitizer touchscreen device as well as Wacom ISDv4 EC Pen eraser input if using a pen with an eraser function.

## Xorg configuration
Next, you will need to tell Xorg to use the new inputs.  The  driver package has an up-to-date list of devices that the Helix has.  But, the package does not install the updated list by default.  You will need to link it for Xorg to see them:

 # ln -s /usr/share/X11/xorg.conf.d/50-wacom.conf /etc/X11/xorg.conf.d/50-wacom.conf

Once done with all the above, reboot and you verify  looks the same as the above.

## Touchscreen
If you find yourself frustrated by the capacitive digitizer while trying to use the pen, there are a few options as outlined below that can help.

## thinkpad-helix-utils: Toggle Touch
The  package contains a script located at  that will toggle the capacitive digitizer on and off with a simple command using Xorg's xinput function.  It also installs a  file called Toggle Touch that can be used to toggle xinput on and off with the pen.

Once activated, it disables the touchscreen xinput device until it is ran again to re-activate it.

## xnohands
Another option that also uses Xorg's xinput is xnohands.  This utility disables the touch device in a system when a stylus is detected (either pen or eraser) and re-enables the touchscreen once then stylus is pulled away from the screen.  It does this by listening to the digitizer's "presence" event, which the Helix's Wacom ISDv4 EC input devices support.  You will need to download and extract it.  Follow the README for instructions as it outlines how to set it up.

NOTE: You must have followed the udev and xorg configuration instructions earlier to have both the Pen and Eraser detected, as well as the touchscreen (all three must be detected); or else, this tool will not work.

If you want it always running, install the desktop file in your autostart to have it run on startup:

 $ cp xnohands.desktop ~/.config/autostart/

Please note that you can have both the thinkpad-helix-utils Toggle Touch and xnohands installed; but, do not use both at the same time.  xnohands will "re-activate" the touchscreen as soon as you pull the pen away from the screen, defeating the purpose of Toggle Touch to keep touch disabled at all times.

## Sensors
Install the package  to expose the dbus events. For example,  will automatically utilize the dbus events exposed by the  package to:

* Adjust the display brightness when moving from dark to bright lighting
* Automatically rotate the display based on orientation.

See the upstream source for more information about  and how to configure/test its functionality.

## Screen rotation
If you have both digitizers configured through the  driver and the  package, they will automatically rotate with the display.

Alternatively, you can use a simple command like  to rotate the screen with ease.

If you want to use the bezel buttons (or some other hotkey) to cycle through orientations (or toggle between two specific ones), , also from from , provides an easy-to-bind command that may serve your needs well.

There is also Magick Rotation, which is supposed to automatically rotate the screen based on input events, but it only seems to respond to docking/undocking the tablet.

## Firmware
Helpfully, Lenovo now provides bootable ISO images for the purpose of installing BIOS updates. While it is not stated on their site, these bootable images also include updated firmware for the keyboard dock MPU. It is uncertain as to whether the USB hub firmware is also updated via this utility.

If you do not have access to a USB optical drive and writable media, the information on ThinkWiki is extremely helpful.
