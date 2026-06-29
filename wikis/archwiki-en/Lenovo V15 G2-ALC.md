# Lenovo V15 G2-ALC

{| class="wikitable archwiki-table-laptop"
|-
! Hardware !! PCI/USB ID !! Working?
|-
| Touchpad ||  ||
|-
| Keyboard || ||
|-
| GPU (amdgpu) ||  ||
|-
| Webcam ||  ||
|-
| Ethernet ||  ||
|-
| Bluetooth ||  ||
|-
| Audio ||  ||
|-
| Wi-Fi ||  ||
|-
| Microphone || ||
|-
| TPM || ||
|}

## Installation
Wi-Fi and possibly Bluetooth are blocked by , you can enable them by running .

As mentioned in the Installation guide too, Secure Boot should be disabled from BIOS while installing Arch Linux.

## Firmware
## fwupd
fwupd is supported on this device.

## Journalctl warnings
## PS/2 appears to have AUX port disabled
Following warning message gets logged to  despite all the ports are working:

 PS/2 appears to have AUX port disabled, if this is incorrect please boot with i8042.nopnp

If you do not want to see this message, add  to your kernel parameters.

## Failed to load regulatory.db
Regulatory domain related warning message can be fixed by installing  from official repositories:

 kernel: platform regulatory.0: Direct firmware load for regulatory.db failed with error -2
 kernel: cfg80211: failed to load regulatory.db

## Function Keys
{| class="wikitable"
|-
! Key
! Visible?1
! Marked?2
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
|  ||  ||  || Inputs 3
|-
|  ||  ||  ||
|-
|  ||  ||  || Unknown
|-
|  ||  ||  || Unknown
|-
|  ||  ||  || Unknown
|-
|  ||  ||  ||
|-
|  ||  ||  || Unknown
|-
|  ||  ||  || Inputs 4
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  || 5
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  || Inputs
|}

# The key is visible to  and similar tools.
# The physical key has a symbol on it, which describes its function
# Default shortcut for opening "project" (as in projector) menu on Windows
# Default shortcut for capturing screenshots on Windows
# Default shortcut for changing power mode on Windows

## Known Issues
## Touchpad acceleration speed drops randomly
This issue happens while charging the machine. It is currently unsolved but you can try to;

# Not use your device on charging,
# Use an external mouse,

until a proper solution is found. Follow this forum thread and this GitLab issue for updates.
