# Samsung Series 7 Slate XE700T1A

{| class="wikitable archwiki-table-laptop"
|-
! Hardware !! PCI/USB ID !! Working?
|-
| Touchscreen || ||
|-
| Video || ||
|-
| Webcam || ||
|-
| Bluetooth || ||
|-
| Accelerometer || ||
|-
| Audio || ||
|-
| Wireless || ||
|}

## Installation
Get into BIOS by holding down the home button after powering on the device.

From there enable Legacy USB which lets you use a USB keyboard and boot from a flash drive.

## Function keys
The volume rocker buttons and power button seem to be recognised by default. However the rotation lock and home buttons do not.

Press the lock button and the home button, then you should get the following:

See Setkeycodes on how to set up these 2 keys.

In addition to that article, first run setkeycodes, you can easily check whether the key you are about to set it to is already set by running

 # getkeycodes | grep keycode

where  is your desired keycode.

## Touchscreen
In order to get the pen button to emulate a right click, go into the Wacom settings in System Preferences.

The touch screen will be recognized as a finger input by many applications, such as Gnome Files or chromium by default and will result in dragging causing the page to scroll, rather than selecting text or objects.

## Screen rotation
If you like to use the tablet in portrait mode, or some other orientation than, normal. Simply setting the screen rotation is not enough since the touchscreen and wacom inputs will still be calibrated to the standard landscape mode.

The touchscreen is calibrated via axis inversion and axes swap. Swapping the axes basically means that the x axis becomes the y and vice verse. Inverting the axis swaps up and down or left and right.

The wacom tablet however, simply uses a number, 0, 1, 2 or 3, however, these do not correspond to the XRandR numbers.

{| class="wikitable"
! Orientation !! XRandR !! Evdev Axis Inversion !! Evdev Axis Swap !! Wacom Rotation
|-
| 0&deg; || 0 || 0 0 || 0 || 0
|-
| 90&deg; || 1 || 1 0 || 1 || 2
|-
| 180&deg; || 2 || 1 1 || 0 || 3
|-
| 270&deg; || 3 || 0 1 || 1 || 1
|}
