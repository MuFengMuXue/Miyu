# System76 Darter Pro 6

## Drivers
Driver support for the System76 Darter Pro 6 should be included the kernel as of Linux 5.5.

The  package provide firmware updating functionality such as system76-firmware-cli.

## Screen Brightness
Works out of the box with the  package.

## Keyboard Backlight
The keyboard backlight can be controlled programmatically via  entries. Specifically,

 # sh -c "echo 255 > /sys/class/leds/system76_acpi::kbd_backlight/brightness"

will increase the brightness to its maximum, and

 # sh -c "echo FFA500 > /sys/class/leds/system76_acpi::kbd_backlight/color"

will set the color of the backlight via a 6-digit RGB hex code.

## Palm Detection
If the touchpad is not sensitive enough to detect your palm, then it is possible to reduce the palm pressure detection threshold using libinput's quirks. The first step is to follow the instructions for debugging touchpad pressure (you will need the  and  packages installed). Once you run the program, you’ll be able to experiment with different ways to touch the touchpad and see which things are registered as clicks and which are registered as a palm.

Once you have found the ideal palm pressure threshold, you can make it persistent by creating a libinput quirks file at . For example, the following decreases the threshold to :

 pressure override
 MatchUdevType=touchpad
 MatchName=*SynPS/2 Synaptics TouchPad
 MatchDMIModalias=dmi:*svnSystem76*pvrdarp6*
 AttrPalmPressureThreshold=70

To confirm it is working correctly, run

 $ libinput quirks list /dev/input/eventXX

where  is the number of the event device. (It should be shown in the output of the  command that you ran above.) The output should look something like this, with no errors:

 ModelSynapticsSerialTouchpad=1
 AttrPalmPressureThreshold=70

At this point, you can reboot and the setting should be applied persistently.

## X11
Install intel-media-driver for hardware accelerated graphics. Do NOT install xf86-video-intel, and libva-mesa-driver packages.

## Suspend/Resume
Occasionally, on Linux 5.4, it was found that the laptop would become unresponsive when resuming from sleep. After about 90 seconds, the laptop would unfreeze itself and resume normal operation. After profiling the kernel with suspendresume, it was found that the culprit was the thunderbolt port. Namely, this error message was found in the output of dmesg:

 [  803.725685] thunderbolt 0000:03:00.0: failed to send driver ready to ICM

One approach to fix this is to disable thunderbolt support on suspend and then re-enable it on resume. This can be done via a systemd hook script.

Drop the following into  and make it executable:

 #!/bin/sh

 # This is a systemd hook script that is run whenever
 # suspend/resume takes place. It should be symlinked into
 # /usr/lib/systemd/system-sleep.

 # $1 is 'pre' (going to sleep) or 'post' (waking up)
 # $2 is 'suspend', 'hibernate' or 'hybrid-sleep'
 case "$1/$2" in
   pre/*)
     if lsmod | grep -q thunderbolt; then
       rmmod thunderbolt
     fi
     ;;
   post/*)
     modprobe thunderbolt
     ;;
 esac

Alternatively, System76 support suggested disabling the corresponding PCI device on suspend and then reloading it on resume. Adapting their  fix for Arch Linux, the above file might look like this instead:

 #!/bin/sh

 # This is a systemd hook script that is run whenever
 # suspend/resume takes place. It should be symlinked into
 # /usr/lib/systemd/system-sleep.

 # $1 is 'pre' (going to sleep) or 'post' (waking up)
 # $2 is 'suspend', 'hibernate' or 'hybrid-sleep'
 case "$1/$2" in
   pre/*)
     echo 1 > '/sys/devices/pci0000:00/0000:00:1c.0/remove'
     ;;
   post/*)
     echo 1 > '/sys/devices/pci0000:00/pci_bus/0000:00/bus_rescan'
     ;;
 esac

You may find that  does not exist but  does.

## DisplayPort and HDMI over USB-C
For proper operation of DisplayPort / HDMI over USB-C, you need to install the  package, start/enable  and add the  kernel parameter.

Only HDMI was tested with Plugable UD-CA1A dock.
