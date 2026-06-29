# Lenovo IdeaPad Yoga 900

{| class="wikitable archwiki-table-laptop"
|-
! Hardware !! PCI/USB ID !! Working?
|-
| GPU || ||
|-
| Wi-Fi || ||
|-
| Audio || ||
|-
| Touchpad || ||
|-
| Touchscreen || ||
|-
| Camera || ||
|-
| Card Reader || ||
|-
| Bluetooth || ||
|}

The Lenovo Yoga 900 is a 2 in 1 laptop with a faux-3200x1800 RG/BW Pentile display.

For a general overview of laptop-related articles and recommendations, see Laptop.

Lenovo has released a BIOS (version 2UCN10T) for Yoga 900 13ISK2, in which Lenovo gives back the right for choosing RAID/AHCI mode to the users. Hence, 13ISK2 is edible for Linux now.

## Installation
## BIOS
Lenovo does not currently offer a BIOS update ISO image. This means you can only upgrade the BIOS from Windows 10.

## Font Size
The console text is hard to read during install with this display, which renders in 3200x1800 resolution but omits part of the detail due to its incomplete (RG/BW) subpixel matrix. You can temporarily use a default larger font like sun12x22.

Consider installing the  package for access to even larger fonts and making it permanent with  (Linux console#Persistent configuration).

## Wi-Fi
During install the wifi-menu may show no networks. This is caused by a soft-block. Using rfkill should fix the issue.

## Configuration
## Keyboard
{| class="wikitable"
|-
! Key
! Visible?
! Working?
! Effect
|-
|  ||  ||   || Audio mute/unmute
|-
|  ||  ||   || Audio volume down
|-
|  ||  ||   || Audio volume up
|-
|  ||  ||   || Close application
|-
|  ||  ||   || Refresh page
|-
|  ||  ||   || Disable Touchpad
|-
|  ||  ||   || Airplane mode
|-
|  ||  ||   || Display active apps
|-
|  ||  ||   || Turn off LCD
|-
|  ||  ||   || Toggle display
|-
|  ||  ||   || Dim LCD backlight
|-
|  ||  ||   || Brighten LCD backlight
|-
|  ||  ||   || Toggle keyboard backlight
|}

## KVM
KVM can be enabled in the BIOS via the Intel Virtual Technology option.

## HiDPI
See HiDPI.

## Sensors
Install the  to get the accelerometer and light sensor working

## Troubleshooting
## Card Reader
Initial testing shows the card read working fine out of the box. There are a few errors on boot that need more research.

Boot message:

Insert of card message:

## External Monitor
Several issues occur when trying to display on an external monitor. This laptop only has a display port over USBC-C, which requires dongles to connect to most monitors. Testing to a monitor with a display port connection has yielded the best result. Testing with HDMI and VGA dongles have revealed several issues. Often xrandr does not show a display connected. Rebooting with the monitor attached does not fix the issue. Sometimes running xrandr several times will show a connection.

If you try to force xrandr to display with the following:

Sometimes you will see the following kernel message:

## Networking
## Toggle Trackpad
The trackpad key (F6) is not mapped correctly to toggle the trackpad. Using UDEV to Map scancodes to keycodes will restore this function. This is a custom hwdb file to restore the feature.

Depending of the exact model, the scancode can vary. If this not work, try  or use  as explained in Map scancodes to keycodes to get the scancode.

## Screen Rotation
When you first boot the screen rotation may not work. A bug currently requires you to suspend and resume the laptop before the screen will rotate using the  package.

## Light Sensor
When you first boot the light sensor for automatic screen brightness may not work. A bug currently requires you to suspend and resume the laptop before the light sensor will work using the  package.
