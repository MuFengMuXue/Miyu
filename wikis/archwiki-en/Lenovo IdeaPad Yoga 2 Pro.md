# Lenovo IdeaPad Yoga 2 Pro

{| class="wikitable archwiki-table-laptop"
|-
! Hardware !! PCI/USB ID !! Working?
|-
| GPU || ||
|-
| Wireless || ||
|-
| Audio || ||
|-
| Touchscreen || ||
|-
| Accelerometer || ||
|-
| Touchpad || ||
|-
| Camera || ||
|-
| Card Reader || ||
|-
| Bluetooth || ||
|}

## Installation
Installing Arch on the HiDPI screen may be difficult as the text will be hard to read. To make the font more readable, before you hit install, disable mode settings. Hit Tab in the arch linux boot menu and append the option  along with  kernel parameter. For Intel graphics card you need to add  and for Nvidia graphics card you need to add . For Nvidia Optimus dual-graphics system, you need to add all the three kernel parameters (i.e. ).

Be aware, adding nomodeset prevents the kernel from identifying the monitor. As a result brightness adjustment and xrandr will not work. This line should probably be removed after installation.

## The ideapad_laptop module
Several problems come up if the ideapad_laptop module is in use.  Namely, it blocks the network card and generates a massive stream of warning from the USB subsystem such as:

 Dec  5 08:40:44 localhost kernel: [  290.632613] xhci_hcd 0000:00:14.0: ep 0x81 - asked for 15360 bytes, 15117 bytes untransferred
 Dec  5 08:40:44 localhost kernel: [  290.735110] xhci_hcd 0000:00:14.0: ep 0x81 - asked for 15360 bytes, 15117 bytes untransferred
 Dec  5 08:40:44 localhost kernel: [  290.837534] xhci_hcd 0000:00:14.0: ep 0x81 - asked for 15360 bytes, 15117 bytes untransferred
 Dec  5 08:40:44 localhost kernel: [  290.940070] xhci_hcd 0000:00:14.0: ep 0x81 - asked for 15360 bytes, 15117 bytes untransferred
 Dec  5 08:40:44 localhost kernel: [  291.042570] xhci_hcd 0000:00:14.0: ep 0x81 - asked for 15360 bytes, 15117 bytes untransferred

You can silence these in the short run by running:

 # dmesg -D

And you can unblock the wireless card by running:

 # rfkill unblock wlan

However, in the long term, you will probably want to blacklist the  driver so that neither of these occur in the first place.  I am yet to find a disadvantage to doing so.

## Keyboard and other hardware keys
To access boot menu or BIOS settings, you must use the alternate power button, next to the standard one.

No keypad available at all.

## Keyboard special keys
{| class="wikitable"
! Keys!! Function !! X sees
|-
|  || Audio mute/unmute || XF86AudioMute
|-
|  || Audio volume down || XF86AudioLowerVolume
|-
|  || Audio volume up || XF86AudioRaiseVolume
|-
|  || Close application ||
|-
|  || Refresh page ||
|-
|  || Disable Touchpad || ?
|-
|  || Airplane mode || ?
|-
|  || Unknown ||
|-
|  || Turn off LCD || ?
|-
|  || Toggle display ||
|-
|  || Dim LCD backlight || XF86MonBrightnessDown
|-
|  || Brighten LCD backlight || XF86MonBrightnessUp
|}

## Hardware keys on right side
From hinge to front:
 XF86AudioRaiseVolume
 XF86AudioLowerVolume
 Super_L+o

## Touchscreen
Touchscreen USB device seems to come and go if the  module is not loaded.

## Multitouch gestures
You need to install  in order to enable multitouch gestures. Optionally, you can install  as a graphical front-end. See more details in the dedicated wiki page.

## Touchscreen button
The touchscreen button with a Windows logo is mapped as . However,  and  are generated simultaneously on touch release. The haptic feedback (vibration) when touching this button is currently not controllable via software.

## Touchscreen stops working after suspension
Sometimes touchscreen stops working after resuming from suspension mode. You should be able to fix the problem reloading the  and  kernel modules:

 # modprobe -r usbhid usbtouchscreen

## ACPI
I modified  to allow for some debugging and additional features (see below):
 #!/bin/sh
 set $*
 group=${1%%/*}
 device=$2
 id=$3
 value=$4
 log_unhandled() {
        logger "ACPI event unhandled: $*"
 }
 case "$group" in
        button)
                case "$action" in
                        power)
                                /etc/acpi/actions/powerbtn.sh
                                ;;
                        lid)
                                /etc/acpi/actions/lid.sh
                                ;;
                        *)      log_unhandled $* ;;
                esac
                ;;
        ac_adapter)
                case "$value" in
                        *)      log_unhandled $* ;;
                esac
                ;;
        *)      echo $* > /dev/tty5
                log_unhandled $* ;;
 esac

## Touchpad
The touchpad sends random input from time to time, especially when lid is closed. If you like your computer to keep running when the lid is closed, you may want to disable the touchpad with ACPI events:
;/etc/acpi/actions/lid.sh
 #!/bin/bash
 export DISPLAY=:0
 if grep closed /proc/acpi/button/lid/LID0/state
 then
        synclient TouchpadOff=1 2>/dev/tty5 && echo "lid closed, disabling touchpad" >/dev/tty5
 else
        synclient TouchpadOff=0 2>/dev/tty5 && echo "lid open, eênabling touchpad" >/dev/tty5
 fi
Of course, the echo statement is optional and for debug purposes.

## Backlight
Screen backlight brightness can be manually set with
 # echo $VAL > /sys/class/backlight/intel_backlight/brightness
with $VAL between 0 and 937

It is possible that you will get a permission denied error, in which case you can run
  # chmod a+rw /sys/class/backlight/intel_backlight/brightness
which makes the brightness editable by any user.

Note: Some users have experienced brightness being stuck under Windows (10) (when you change it there is no actual change), it will most likely work under arch.

## Battery
Battery info can be accessed with
 ls /sys/class/power_supply/BAT1/*
Unfortunately, the values obtained there have no units (older Lenovo products had rates in mA, battery voltage, etc.)

## Graphics
Steam has been known to crash trying to run games complaining about missing i965 module. It seems some applications treat it as accelerated, and some do not.

Resolution seems to be not so well supported by some desktop environments/window managers. Gnome-based DEs like Cinnamon and Mate, as well as XFCE and fvwm seem to work fine.

Users may wish to boost font-sizes, as the HiDPI screen can be hard to read in some settings.

If you have trouble detecting a display with the micro hdmi port, consider filing the plastic on the male hdmi plug back a bit (not on the laptop). See here. The rubber case can prevent the plug from inserting fully.

## Rotation/Conversion
You can easily rotate screen with xrandr, however it does not rotate touchscreen/touchpad input which makes it fairly awkward to use. There is a project attempting to address this. Keyboard hardware-disables in tablet mode, but touchpad is still active which needs to be addressed. No ACPI or keycode signals appear to be emitted for the various screen rotation states.
