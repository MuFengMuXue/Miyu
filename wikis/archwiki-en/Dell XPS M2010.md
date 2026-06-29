# Dell XPS M2010

From Wikipedia:
: The XPS M2010 is a large 'mobile desktop' with an adjustable display, built-in speakers, and detachable Bluetooth keyboard. For transportation, it may be folded and carried as a briefcase.

It also made an appearance in the 2008 Iron Man film.

## Hardware (Needs configuration)
## Sound
Internal speakers will not work out of the box. (See discussions on the Linux Laptop Wiki, among other places.)

A workaround is described at For the record, the workaround involves running the following commands:

 hda-verb /dev/snd/hwC0D0 0x1 set_gpio_data 5
 hda-verb /dev/snd/hwC0D0 0x1 set_gpio_dir 5
 hda-verb /dev/snd/hwC0D0 0x1 set_gpio_mask 5

Speaker output works as expected after this.

## Running the workaround automatically with systemd
Using systemd, it is possible to set up a script to run these commands automatically at boot.

First, create the relevant script and save it somewhere (e.g., in ):

Make it executable.

Create a new systemd unit (e.g., in ) that calls your script:

Enable the new service.

To test the workaround, either reboot or start the service. However, note that running the commands a second time during the same session might cause the speakers to stop working; they should work again after a reboot.

## Temperature monitoring and fan control (i8k)
The  module appears to work for temperature monitoring
and fan control, but it needs to be loaded explicitly.

First, create a new .conf file in  specifying  as a module to load:

Next, specify the module load options in a .conf file in .
The fan RPM values shown by default appear to be erroneous, so we change the
option here (see [https://bugs.launchpad.net/ubuntu/+source/sensors-applet/+bug/200449):

The  module should now be loaded automatically at boot.

To make system-wide changes to the configuration for ,
you can simply edit  -- You do not need to create a configuration file anywhere else.

Note: Within , the left value appears to control the right fan (GPU) while the right value appears to control the left fan (CPU) for the M2010.

## Hardware (Working)
## Keyboard
The M2010 Bluetooth keyboard/touchpad works out of the box.

## Graphics
The ATI Mobility Radeon X1800 works with 3D acceleration using the  module.

Install .

## Network
Ethernet (Broadcom Corporation NetXtreme BCM5753 Gigabit Ethernet PCI Express) works out of the box with module .

Wireless (Intel Corporation PRO/Wireless 4965 AG or AGN) works out of the box with module .

## Hardware (Not working)
## Webcam
The webcam does not work out of the box (picture is garbled). https://www.dell.com/community/Linux-General/HOWTO-Linux-driver-for-DELL-XPS-M2010-built-in-webcam/m-p/2787282
suggests that it is possible to get it to work; further testing is needed to get it up and running on more modern configurations.

## Hardware (Untested)
The following devices/functions were not tested:

* Other Bluetooth devices
* Card reader
* Fan control (i8k)
* Internal modem
