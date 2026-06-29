# Intel NUC X15

{| class="wikitable archwiki-table-laptop"
|-
! Hardware !! PCI/USB ID !! Working?
|-
| Bluetooth ||  ||
|-
| Webcam ||  ||
|-
| Ethernet ||  ||
|-
| Wi-Fi ||  ||
|-
| GPU (Intel) ||  ||
|-
| GPU (NVIDIA) ||  ||
|-
| GPU (Intel) ||  ||
|-
| Touchpad || ||
|-
| Keyboard || ||
|-
| TPM || ||
|-
| SD-card reader ||  ||
|-
| Audio ||  ||
|}

## Installation
This device can only boot in UEFI mode.

This device has an IR camera that can be used for face recognition authentication, try Howdy if you want to use that feature.

To control the keyboard RGB backlighting, you can try  and . The latter is not required but provides more functionality.
If the AUR does not recognize the device, try building it yourself from Github.

The most comprehensive driver for this device is , which can read and control fan speed, control the lightbar, enable Fn lock function keys, enable Meta key lock, and control charging limit. It has no user interface, but is quite functional.

To have touchpad toggle and Airplane mode toggle working, you can also try  module in . It has fewer features but has a user interface.

It is worth noting that these two AUR conflict with each other.

Additional steps may be required to get the screen to use a high refresh rate, see Intel graphics#Add support for 165Hz monitor and Kernel mode setting#Forcing modes and EDID.

## Accessibility
The appearance of the UEFI is simple and not very colorful, so it might work well with OCR software. Navigation can be controlled by keyboard or mouse.

* System Setup:
* Update BIOS:
* Windows Recovery Mode:
* Boot Menu:
* Network Boot:

## Firmware
Secure Boot custom keys work well on this device.

fwupd does not support this device yet.

## Function keys
{| class="wikitable"
|-
! Key
! Visible?1
! Marked?2
! Effect
|-
|  ||  ||  || Toggles Fn lock
|-
|  || 3 ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  || , does not work.
|-
|  ||  ||  ||
|-
|  ||  ||  || Toggles keyboard backlight brightness
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  || Inputs
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|}

# The key is visible to  and similar tools
# The physical key has a symbol on it, which describes its function
# systemd-logind handles this by default
