# Lenovo V15 G3 ABA

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
| Audio ||  ||
|-
| Wi-Fi ||  ||
|-
| TPM || ||
|}

## Firmware
## Essential packages
V15 G3 ABA uses only  and  firmwares. Installing these is sufficient for the hardware to function properly.

## Wi-Fi and Bluetooth
By default,  blocks Wi-Fi connectivity and Bluetooth on every startup. To unblock them automatically, enable the  service.

## Failed to load regulatory.db
Regulatory domain related warning message can be fixed by installing  from official repositories:

 kernel: platform regulatory.0: Direct firmware load for regulatory.db failed with error -2
 kernel: cfg80211: failed to load regulatory.db

## PS/2 appears to have AUX port disabled
Following warning message gets logged to  despite all the ports are working:

 PS/2 appears to have AUX port disabled, if this is incorrect please boot with i8042.nopnp

If you do not want to see this message, add  to your kernel parameters.

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
|  ||  ||  ||
|-
|  ||  ||  || Inputs
|}

# The key is visible to  and similar tools.
# The physical key has a symbol on it, which describes its function
# Default shortcut for opening "project" (as in projector) menu on Windows
# Default shortcut for capturing screenshots on Windows
# Default shortcut for changing power mode on Windows
