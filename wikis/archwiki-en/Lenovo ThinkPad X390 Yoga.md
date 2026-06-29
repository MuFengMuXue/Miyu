# Lenovo ThinkPad X390 Yoga

{| class="wikitable archwiki-table-laptop"
|-
! Hardware !! PCI/USB ID !! Working?
|-
| Touchpad || ||
|-
| TouchScreen || ||
|-
| TrackPoint || ||
|-
| Keyboard || ||
|-
| Video || ||
|-
| Webcam || ||
|-
| Ethernet || ||
|-
| Bluetooth || ||
|-
| microSD-Card slot || ||
|-
| Audio || ||
|-
| Wireless || ||
|-
| Mobile broadband || ||
|-
| Fingerprint Reader  || ||
|}

## Firmware
In August of 2018 Lenovo has joined the Linux Vendor Firmware Service (LVFS) project, which enables firmware updates from within the OS.
BIOS updates (and possibly other firmware such as the Thunderbolt controller) can be queried for and installed through fwupd.

## Touchscreen
One option for fixing the touchscreen after resume is reloading the wacom kernel module:

This reloads the wacom kernel module during standby and fixes the issue for me. Other possible options can be found in the related ThinkPad articles, like disabling Thunderbolt or using rtcwake for 1 second. Both options did not work reliably for me.

The touchscreen appears to perform much better using libinput. Created the following file:

This uses libinput and fixes scrolling with the finger in the desktop environment.

## Fingerprint reader
See fprint.

## Function keys
{| class="wikitable"
|-
! Key
! Visible?1
! Marked?2
! Effect
|-
|  || || || XF86WakeUp
|-
|  || || || XF86AudioMute
|-
|  || || || XF86AudioLowerVolume
|-
|  || || || XF86AudioRaiseVolume
|-
|  || || || XF86AudioMicMute
|-
|  || || || XF86MonBrightnessDown
|-
|  || || || XF86MonBrightnessUp
|-
|  || || || XF86Display
|-
|  || || || XF86WLAN
|-
|  || || || XF86Tools
|-
|  || || || XF86Bluetooth
|-
|  || || || ??
|-
|  || || || XF86Favorites
|}

# The key is visible to  and similar tools.
# The physical key has a symbol on it, which describes its function.
