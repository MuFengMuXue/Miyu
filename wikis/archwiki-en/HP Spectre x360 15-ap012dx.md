# HP Spectre x360 15-ap012dx

{| class="wikitable archwiki-table-laptop"
! Hardware !! PCI/USB ID !! Working?
|-
| GPU || ||
|-
| Wireless || ||
|-
| Bluetooth || ||
|-
| Audio || ||
|-
| Touchpad || ||
|-
| Touchscreen || ||
|-
| Webcam || ||
|-
| Card Reader || ||
|}
This article is based on my personal experience with this laptop using Arch x86_64 (kernel 4.8.6-1-ARCH). While I found no noticeable issues remained after the initial installation, some issues have been found in a similar model (see HP Spectre x360 4231).

## Hardware info
## Specifications
This model was released in February 2016.

* Intel Core i7-6500U with Intel HD Graphics 520 (2.5 GHz, up to 3.1 GHz, 4 MB cache, 2 cores)
* 15.6" 4K (3840x2160) Ultra HD IPS WLED multitouch display
* 16 GB LPDDR3-1866 SDRAM
* 256 GB M.2 SSD
* 1 USB Type C port, 3 USB 3.0 ports, 1 HDMI port, 1 Mini DisplayPort, 1 headphone/microphone jack
* 1 SD media card reader
* 802.11ac (2x2) and Bluetooth 4.0
* Bang & Olufsen quad speakers
* 3-cell, 64.5 Wh Li-ion battery
* Webcam
* Backlit keyboard

## Installation
Installing Arch was mostly without hiccup; you do need to disable secure boot (F10 for BIOS options; F9 for boot options). Dual boot was not tested. The laptop does not have a CD drive, so you have to use a USB stick.

The following packages got all the hardware working for me:

## Tweaks
## HiDPI
The screen natively runs at 3840x2160. Often a scaling factor of 2 is picked by default, though 1.5 also gives good results.

## Screen Rotation
The laptop can be flipped completely (hence the 360 in the name) and it is sometimes useful to rotate the display. It is unclear whether this can be done automatically by detecting the physical laptop orientation, but it should be easy enough to map a shortcut to the following script to toggle the screen display (Source: Touchscreen Input Doesn't Rotate: Lenovo Yoga 13 / Yoga 2 Pro)
{{bc|
#!/bin/bash
# This script rotates the screen and touchscreen input 180 degrees,
# disables the touchpad, and enables the virtual keyboard And rotates
# screen back if the touchpad was disabled

isEnabled=$(xinput --list-props 'SynPS/2 Synaptics TouchPad' | awk '/Device Enabled/{print $NF}')

if [ $isEnabled == 1 ]
then
    echo "Screen is turned upside down"
    xrandr -o inverted
    xinput set-prop 'ELAN Touchscreen' 'Coordinate Transformation Matrix' -1 0 1 0 -1 1 0 0 1
    xinput disable 'SynPS/2 Synaptics TouchPad'
    # Remove hashtag below if you want pop-up the virtual keyboard
    # onboard &
else
    echo "Screen is turned back to normal"
    xrandr -o normal
    xinput set-prop 'ELAN Touchscreen' 'Coordinate Transformation Matrix' 1 0 0 0 1 0 0 0 1
    xinput enable 'SynPS/2 Synaptics TouchPad'
    # killall onboard
fi
}}

## TTY font
See HiDPI#Linux console (tty).

## Mute Button LED
In order to get the LED Indicator on the mute button to function, you must add the following line to        (create  if it does not exist)    and then reboot. The LED should now be toggled on or off depending on the mute state.
