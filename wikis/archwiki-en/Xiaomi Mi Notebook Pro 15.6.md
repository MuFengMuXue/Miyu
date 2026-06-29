# Xiaomi Mi Notebook Pro 15.6

{| class="wikitable archwiki-table-laptop"
|-
! Hardware !! PCI/USB ID !! Working?
|-
| Bluetooth ||  ||
|-
| Webcam ||  ||
|-
| Wi-Fi ||  ||
|-
| GPU (Intel) ||  ||
|-
| GPU (nvidia) ||  ||
|-
| Touchpad ||  ||
|-
| Keyboard ||  ||
|-
| TPM || ||
|-
| Fingerprint reader ||  ||
|-
| SD-card reader ||  ||
|-
| Audio ||  ||
|}

## Installation
Enter the UEFI menu by pressing  during Boot and disable the password and Secure Boot.

* Security -> Set password
* Security -> Disable Secure Boot
* Reset the password by setting the password again but letting the "New Password" fields blank.

## Function keys
{| class="wikitable"
! Key
! Effect
|-
|
|  Enables/disables Fn lock
|-
|
|
|-
|
|
|-
|
|
|-
|
|
|-
|
|
|-
|
|
|-
|
|  Invokes user-defined action if "xiaomi_wmi" module is loaded
|-
|
|
|-
|
|  Enables/disables touchpad
|-
|
|  Enables/disables keyboard backlight
|-
|
|
|-
|
|
|}

## Display
Factory display calibration is poor. Check the panel model:

 $ edid-decode < /sys/class/drm/card0-eDP-1/edid | grep Alphanumeric

If it is NV156FHM-N61, try the ICC profiles at https://www.notebookcheck.net/uploads/tx_nbc2/NV156FHM_N61.icm.

The path to the backlight is non-standard and causes tools like  to not work. To fix this issue, you have to setup Intel driver and add Backlight option to respective X-Org configuration file:

## Touchpad troubles
You may face a problem when the kernel sees 2 touchpad devices
if you have multiple touchpad devices displayed in libinput list-devices
Try to add i8042.noaux kernel param

## TPM issues
BIOS used in this model does not allow enabling SHA256 PCR bank, all measurements are  done to SHA1 PCR bank only.
