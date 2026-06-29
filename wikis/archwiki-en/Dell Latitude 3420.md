# Dell Latitude 3420

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
| Microphone || ||
|-
| Ethernet ||  ||
|-
| Wi-Fi ||  ||
|-
| Bluetooth ||  ||
|-
| SD-card reader || ||
|-
| Audio ||  ||
|-
| Fingerprint reader ||  ||
|-
| TPM || ||
|}

## Performance
This device can be throttled and have very bad performance, even if setting on BIOS the Ultra Performance option.

Installing and enabling  seems to fix the issue, allowing the processor to reach higher speeds, while also running on higher CPU temperature.

## Accessibility
The appearance of the BIOS is pretty simple and not very colorful, so it might work well with OCR software. However, it requires the user to use a mouse.

* System Setup :
* Boot Menu:

From the official manual see Navigation keys.

## Firmware
fwupd supports update for those devices:

* Touchpad
* Fingerprint sensor
* NVMe drive
* System firmware
* TPM
* UEFI device firmware
* USB host controller

## Video
For better video support install , . As per Intel graphics#Installation, it is not recommended to install .

## Tearing when using Xorg and modesetting driver
However, if you experience too much tearing you could add back  driver to alleviate tearing when using Xorg.

You can additionally enable  (see Intel graphics#Tearing), but be aware that there is a noticeable impact on performance.

## Audio
Sound and microphone requires the installation of Sound Open Firmware to work, else no card / output device will be detected.

## Fingerprint reader
The built-in fingerprint reader () is supported and works with fprint.

## Function keys
{| class="wikitable"
|-
! Key
! Visible?1
! Marked?2
! Effect
|-
|  ||  ||  || Enables Fn lock
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  || Enables/disables keyboard backlight
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  || Inputs
|-
|  ||  ||  || Unmarked keybinds
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  || Contextual menu
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|}

# The key is visible to  and similar tools
# The physical key has a symbol on it, which describes its function
