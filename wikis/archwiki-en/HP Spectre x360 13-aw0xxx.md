# HP Spectre x360 13-aw0xxx

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
| Touchpad ||  ||
|-
| Touchscreen ||  ||
|-
| Pen input ||  ||
|-
| Webcam ||  ||
|-
| Card Reader ||  ||
|-
| Fingerprint sensor ||  ||
|}

This is the late 2019 edition of the Spectre x360 from HP (13-aw0xxx).

* Intel i7-1065G7 Ice Lake
* 4K OLED Touchscreen with Elantech pen
* Intel Iris Plus Graphics
* 2 Speaker Sound
* 2 USB-C, Thunderbolt 3 Ports
* 1 USB-A
* TPM 2
* Synaptics Fingerprint Sensor

This article covers specific configuration of this laptop. Currently based on experience with BIOS F.13.

## Installation
Disable Secure Boot in the UEFI ( to bring up menu, then  for UEFI and/or  for Boot options) and follow the installation guide as usual.

## Display
See HiDPI.

## Backlight
OLED panels do not have backlight, they get dimmed via PWM. With kernel 5.7+ you can add  to the list of kernel parameters to make backlight controls work natively. This option may not be needed on future kernels.

On older kernels you will have to use  (see Backlight#Color correction) and let it manage color profiles.

## Color profile
A calibrated ICC color profile is available from NotebookCheck.net in the Display section of the article (direct link).

## Auto Rotation
Installing  works out of the box on Gnome. See Tablet PC#Automatic rotation for more details.

## Audio
This laptop requires Sound Open Firmware in order for the soundcard to work.

This laptop has a Realtek ALC285 codec with a 2 speaker system and digital microphone array built in.

## Fingerprint reader
Experimentally supported via vojtapl's fprintd fork which integrates their reverse engineering work on this family of fingerprint readers.

Install  instead of  and then follow the rest of the Fprint instructions to configure like normal.

## IR camera login
Works with Howdy configured to use .

## HP Tilt Pen
As of June 2020 the HP Tilt Pen is supported by the development version of . You can still apply the changes manually.

Pressure sensitivity and tilt to erase are working, but the buttons on the pen are not correctly mapped. When put into presentation mode it is recognized as a Bluetooth mouse but it does not move the cursor or emit events.

## Function keys
{| class="wikitable"
|-
! Key
! Visible?1
! Marked?2
! Effect
|-
|  ||  ||  || Toggles HP Sure View privacy screen
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  || Cycles keyboard backlights between high, low, and off
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
|  ||  ||  ||
|}

# The key is visible to  and similar tools.
# The physical key has a symbol on it, which describes its function.

## Other mappings
The following keys are physically marked, but must be remapped by the desktop environment.

{| class="wikitable"
|-
! Key
! Visible?1
! Marked?2
! Effect
|-
|  ||  ||  || Cycles display mode
|-
|}

# The key is visible to  and similar tools.
# The physical key has a symbol on it, which describes its function.
