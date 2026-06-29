# Dell Latitude 7280

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
| Ethernet ||  ||
|-
| Bluetooth ||  ||
|-
| SD-card reader ||  ||
|-
| Audio ||  ||
|-
| Wi-Fi ||  ||
|-
| Fingerprint reader || ||
|-
| Smart Card reader ||  ||
|-
| TPM || ||
|}
## Installation
Before installing, disable Secure Boot in the UEFI or configure it.

Pressing  on startup enters straight into UEFI/firmware setup.

## Accessibility
The UEFI uses Dell's classic/legacy style, which is mostly dark text on bright background. Should be readable by OCR.

Can be fully navigated with keyboard (arrow keys +  to navigate,  to expand left hand sections and change options on the right), or with mouse/touchpad if preferred.

The Latitude 7280 has a 12.5" screen, which might discourage use for those who need large screen elements and fonts.

Hardware errors are indicated with diagnostic light patterns on the power button LED, these are documented in the owner's manual.

## GPU
## Screen flickering
As of writing this, there seems to be some issues with Intel GPUs relating to how kernels >= 5.10 handle C-states.
Wayland doesn't seem to be affected by this but if you care about TTY mode working properly and if you experience flickering,
add this kernel parameter:

 intel_idle.max_cstate=4

See discussion on the forums.

## Firmware
fwupd currently has updates for the Thunderbolt NVM but not for UEFI system firmware.
