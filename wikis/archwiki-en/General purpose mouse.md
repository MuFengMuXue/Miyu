# General purpose mouse

GPM, short for General Purpose Mouse, is a daemon that provides mouse support for Linux virtual consoles.

## Installation
Install the  package. For touchpad support on a laptop, please see Laptop#Touchpad.

## Configuration
The  parameter precedes the declaration of the mouse to be used. The  parameter precedes the type of mouse. To get a list of available types for the  option, run  with .
 # gpm -m /dev/input/mice -t help

The  package needs to be started with a few parameters. These parameters can be recorded by creating the file , or used when running gpm directly. The  includes the parameters for USB mice ().

Obviously, it should be edited, preferably in a systemd friendly manner, if there is another mouse type, and the service is used.
* For PS/2 mice, the parameters are:
* And IBM Trackpoints need:

Once a suitable configuration has been found, start and enable the .

For more information see .

## QEMU or VirtualBox
The default mouse emulated by QEMU and VirtualBox has severe problems in both gpm and x with positioning and clicking.  The position becomes unsynchronized with the host, so there are areas that cannot be hovered over without repeatedly exiting and re-entering the window.  Clicks register in a different location than the cursor was showing at.

Both QEMU and VirtualBox solve this problem by providing emulation for a USB tablet, which gives absolute positioning.  ( uses this automatically.)

However, the gpm only knows how to use the emulated mouse in relative positioning mode, so these problems remain.  Attempting to use other types via  fail to get it working properly.

 includes a several year old pull request to add USB tablet support for VirtualBox (which also works under QEMU) and modifies the  file to use it by default.

You may need to change which event is used.  (Giving gpm the original  will not work.)  By default:

You can determine the event to use by installing  and running:

If you need to give gpm additional options, you can set  in .

Once a suitable configuration has been found, start and enable the .
