# AYA NEO 2021

{| class="wikitable archwiki-table-laptop"
|-
! Hardware !! PCI/USB ID !! Working?
|-
| Display || ||
|-
| Touchscreen || ||
|-
| GPU ||  ||
|-
| GPU (Pro)||  ||
|-
| Wi-Fi ||  ||
|-
| Wi-Fi (Pro) ||  ||
|-
| Bluetooth ||  ||
|-
| Bluetooth (Pro)||  ||
|-
| Audio ||  ||
|-
| Gamepad ||  ||
|-
| Gyro/IMU ||  ||
|}

## Display
The integrated 800x1280 display is a portrait tablet display that is displayed in a landscape orientation without software correction.

## Controller
The built-in controller registers as an Xbox360 controller. A linear vibration motor exists and is functional using the xpad_noone driver.

## Bluetooth
Bluetooth on the non-Pro is working as of 5.15.12 (possibly earlier) for the AMD RZ608, which is a re-badged Mediatek MT7921E. The Pro model uses the Mediatek MT7921K and requires the workaround posted in the Wireless section below to work.

## Wireless
The Wi-Fi module is the AMD RZ608, which is a re-badged Mediatek MT7921E for the regular model, and a Mediatek MT7921K for the pro model. The Wireless module does not handle power state changes well and will fail to return to operation after system resume. the  package resolves this issue by unloading the kernel driver at sleep and reloading it at resume.

## Function keys
The front of the device has 4 special keys on the bottom right that are mapped through an additional USB keyboard device:

{| class="wikitable"
|-
! Key
! Visible?1
! Marked?2
! Effect
|-
|  ||  ||  || Inputs
|-
|  ||  ||  || Inputs
|-
|  ||  ||  || Inputs  (Opens the virtual keyboard on Windows)3
|-
|  ||  ||  || Inputs  (Opens the Task Manager on Windows)4
|}

# The key is visible to  and similar tools
# The physical key has a symbol on it, which describes its function
# KB key cannot be mapped to toggling the OSK on Gnome Shell. A feature request has been opened for it.
# Prompts to shutdown the machine on Gnome Shell

It is possible to remap the keys to button codes using .
