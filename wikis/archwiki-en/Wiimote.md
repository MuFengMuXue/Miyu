# Wiimote

This article will go through the basic steps required to have a working Wiimote in Linux for general use. It will not go into much detail for some steps as there are many guides already written for some parts already.

## Prerequisites
* Bluetooth
* A Wii Remote

Wiimotes connect via Bluetooth. This must already be configured and running without the help of this guide. You will need a Wiimote, this can include (although are not required) the Nunchuk and Classic Control attachments.

Once a Wiimote is connected via Bluetooth, the device should start working, as the kernel driver for the Wiimote is in Linux since version 3.1 and the  package in Arch Linux includes the required wiimote plugin.

## Connect the Wiimote
See XWiimote#Connect the Wii Remote.

## Infrared sources
Possible infrared sources are

* Nintendo Wii Sensor Bar
* Wireless sensor bar - check eBay!
* Normal light bulbs
* Small candles (should have about 30cm distance)
* Home made sensor bar (== Input device ==

## X11
XWiimote provides an X11 input driver for using a Wiimote as a desktop input device. See XWiimote#X.Org Input Driver for details.

## cwiid
The Wiimote can act as a regular input device like a mouse using  from the  package. This package contains a userspace driver, libraries, and programs required for basic use of the Wiimote.

First you need to make sure to load the  module:

 # modprobe uinput

You should have a device in  now. For permanent use, add uinput to MODULES in mkinitcpio.conf.

cwiid should allow you to scan for your Wiimote now. Run the following command and press the  and  buttons on your Wiimote:

Once your Wiimote has been detected you can test if it is working by running  and testing out various buttons and sensors through that interface.

If you have no infrared source, simply run:

 $ wminput -w

You can control your pointer now by tilting your Wiimote forward, backward or to the sides.

If you have an infrared source, run:

 $ wminput -c ir_ptr -w

## Configuration
The default configuration files are in . They are a good starting point for your customized settings in  or . The general syntax is:

 Wiimote_button = keyboard_key

All possible values for  can be found in [https://github.com/abstrakraft/cwiid/blob/master/doc/wminput.list cwiid/wminput.list. The possible values for  are keycodes in /usr/include/linux/input-event-codes.h.

## Unable to open uinput
If wminput gives this error, leaving you unable to use the Wiimote, create a udev rule with the following contents https://bbs.archlinux.org/viewtopic.php?pid=821783#p821783:

 KERNEL=="uinput", GROUP="wheel", MODE="0660"

Reboot the system afterwards. See also  regarding udev rules for .

Alternatively, add  to the MODULES array in mkinitcpio.conf:

 MODULES=(uinput ...)

Regenerate the initramfs and reboot the system afterwards.
