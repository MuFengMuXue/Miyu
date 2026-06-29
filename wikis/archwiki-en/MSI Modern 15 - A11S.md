# MSI Modern 15 - A11S

{| class="wikitable archwiki-table-laptop"
|-
! Hardware !! PCI/USB ID !! Working?
|-
| Touchpad || ||
|-
| Keyboard || ||
|-
| GPU ||  ||
|-
| Webcam ||  ||
|-
| Bluetooth ||  ||
|-
| SD-card reader ||  ||
|-
| Audio ||  ||
|-
| Wi-Fi ||  ||
|-
| TPM || ||
|}

The information below is valid for models:

* Modern 15 A11SB
* Modern 15 A11M
* Modern 15 A11SBL
* Modern 15 A11ML
* Modern 15 A11SBU
* Modern 15 A11MU

## Installation
Secure Boot needs to be disabled at first startup and after UEFI updates. Append  and  to pacstrap.

This laptop is supported by the community developed Embedded Controller for MSI laptops driver.

## Firmware
Some devices can be listed with fwupd, but MSI does not provide updates via the LVFS.

Secure Boot functions well with custom keys, make sure to disable automatic reverting to factory keys in the UEFI settings.

To update Intel Management Engine firmware, See Laptop/MSI#Intel Management Engine.

## Sound
This laptop requires Sound Open Firmware in order for the sound card to work.

## Accessibility
The BIOS interface is keyboard driven and does not require the use of a mouse.

## Thermals
Fan control can be tuned by installing .

Configuration entry for Modern 15 A11M is missing, and needs to be added manually (PR: https://github.com/YoyPa/isw/issues/152):

To activate a personalized profile, you need to set the value  to . You can set your profile adding to autostart the following two lines (PR: https://github.com/YoyPa/isw/issues/152):

 # isw -w 1552EMS1
 # isw -s 0xd4 64

To autostart you can also use the provided , but you will need use a drop-in snippet:

Then start/enable .

## Function keys
The keyboard backlight works properly.

Keyboard LEDs :
*  (Audio mute) and  (Microphone status) : not working
* ,  and  : working

{| class="wikitable"
|-
! Key
! Marked1
! XKB
! Libinput
! Notes
|-
|  ||  ||  ||  || Quick FN Launch Keys
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  ||  &&
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  ||  || no effect (MSI Center Pro)
|-
|  ||  ||  ||  || Toggle keyboard backlight levels
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  ||  &&  || Switch display
|-
|  ||  ||  ||  || no effect (Rotate screen)
|-
|  ||  ||  ||  &&  &&  || no effect (Capture screen zone)
|}

# The physical key has a symbol on it, which describes its function
# The key is visible to  and similar tools
# systemd-logind handles this by default
