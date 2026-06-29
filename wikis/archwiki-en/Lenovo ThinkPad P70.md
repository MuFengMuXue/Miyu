# Lenovo ThinkPad P70

{| class="wikitable archwiki-table-laptop"
|-
! Hardware !! PCI/USB ID !! Working?
|-
| GPU (Intel) || ||
|-
| GPU (Quadro M3000M) || ||
|-
| GPU (Quadro M4000M) || ||
|-
| Ethernet || ||
|-
| Wireless || ||
|-
| Audio || ||
|-
| Trackpad || ||
|-
| Trackpoint || ||
|-
| Webcam || ||
|-
| Card reader || ||
|-
| Bluetooth || ||
|}

## Preliminaries
# Create a recovery device in Windows 10. It required a USB-only (no SD card, no optical media?) flash drive greater than 8 GB. Formatting FAT32 works.
# Update the BIOS. Lenovo provides a bootable, standalone "BIOS Update CD" to perform this update outside of Windows.
# Getting into the BIOS is difficult, so here are some instructions that seemed to work. The easiest way was through Windows 10.
# In the BIOS, you will want to disable UEFI Secure Boot, change the boot order to look at USB devices first, allow  to bypass the BIOS, and possibly enable the verbose mode because it is easier to press the appropriate buttons on time.

## Keyboard
To control the keyboard backlight, you change the value using:

 # echo 1 > /sys/class/leds/tpacpi::kbd_backlight/brightness

for values 0–2.

## Video
There is a BIOS option for turning off the Intel Integrated Graphics and only running the NVIDIA discrete card. While it is possible to get the console working with this configuration, there are no confirmed reports of X.org working in this setup.

## External displays
DisplayPort over USB-C, HDMI, and Mini DisplayPort outputs all work using the above configuration with the proprietary Nvidia driver. HDMI has also been confirmed to work using Bumblebee and .

Limited testing suggests that a maximum of 3 total displays from 2 output types may be used at one time. For example, two external DP/USB-C displays and the one internal display will achieve the maximum of three.
