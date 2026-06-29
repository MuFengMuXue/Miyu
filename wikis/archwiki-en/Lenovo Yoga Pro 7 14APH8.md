# Lenovo Yoga Pro 7 14APH8

{| class="wikitable archwiki-table-laptop"
|-
! Hardware !! PCI/USB ID !! Working?
|-
| GPU ||  ||
|-
| Wi-Fi ||  ||
|-
| Bluetooth ||  ||
|-
| Audio ||  ||
|-
| Microphone ||  ||
|-
| TouchPad ||  ||
|-
| Webcam ||  ||
|}

## Installation
See #Accessibility on how to change UEFI settings, disable Secure Boot and boot an Arch installation medium.

System boot and everything works, see #Video for possible visual glitches.

## Accessibility
The UEFI firmware settings can be entered by pressing  repeatedly during boot.

## Navigation
The interface can be fully navigated and controlled with a keyboard and mouse. Up and down arrow keys let the user choose categories, settings items within each category and values for settings. Left and right arrow keys let the user leave and enter a category, settings item or value picker. The enter key can also be used to enter a category or enter and leave an item's value picker. Settings can be saved and the system restarted by pressing .

## Secure Boot
In order to boot an Arch installation medium, Secure Boot must be disabled in the UEFI settings. Once disabled, press  on the next boot to enter the boot device menu and select your Arch installation medium.

## Firmware
This laptop is not supported by fwupd. You need a Windows installation in order to update UEFI.

## Video
If you see sporadic graphic glitches, add  as a kernel parameter.

## Power management
## System performance mode
There are 3 modes available: Intelligent Cooling, Extreme Performance and Battery Saving.

## Audio
This laptop has 4 speakers: 2 tweeter and 2 woofer, by default only the tweeters work.

The volume switch only on-off, to correct that you can edit:

From kernel 6.6.7 this workaround are not necessary due this kernel patch officially merged:

https://lore.kernel.org/all/20231207182035.30248-1-tiwai@suse.de/
## Function keys
{| class="wikitable"
|-
! Key
! Visible? 1
! Marked? 2
! Effect
|-
|  ||  ||  || Toggles Fn lock
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  || ??
|-
|  ||  ||  ||  3
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  || ??
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  || Cycles keyboard backlight brightness
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|}

# The key is visible to  and similar tools.
# The physical key has a symbol on it, which describes its function.
# Pressing  always hardware-toggles the Wifi and Bluetooth hardware and additionally releases an  keypress event.
