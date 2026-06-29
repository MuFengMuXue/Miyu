# Lenovo Yoga 7 2-in-1 14AHP9

{| class="wikitable archwiki-table-laptop"
! Hardware !! PCI/USB ID !! Working?
|-
| Touchscreen || ||
|-
| Touchpad || ||
|-
| GPU ||  ||
|-
| Webcam ||  ||
|-
| Bluetooth ||   ||
|-
| SD-card reader ||  ||
|-
| Audio ||  ||
|-
| Wi-Fi ||  ||
|-
| Fingerprint reader ||  ||
|-
| Tablet mode switch || ||
|-
| TPM (Pluton) || ||
|}

This laptop tablet is not to be confused with Lenovo Yoga Pro 7 14AHP9.

## Accessibility
Before an operating system loads, the device provides several options for navigation.

* In the firmware interface, use  arrows to switch between side menu and main view,  arrows to navigate within main menu,  to change values,  to select an option, and  to display exit menu.
* Alternatively, use the touchscreen−it is always on while in the firmware interface. An on-screen keyboard is available when entering administrator password.
* Press  to enter the firmware interface, and  to enter the boot menu.
* The Flip To Start option may be enabled in the firmware interface in order to initiate boot by opening the lid.
* While shutdown, connecting AC or pressing any button on the keyboard will display current battery charge.

## Firmware
fwupd does not support this device yet, but is able to update platform's UEFI CA certificates. With great caution, a firmware update can be performed for this device, as described in Flashing BIOS from Linux#Lenovo.

Secure Boot works with custom keys if Microsoft Corporation UEFI CA is also enrolled (e.g., using ).

The device supports "BIOS self-healing", and stores a firmware backup image on EFI system partition; its size is about 6 MB. This image should not be signed when setting up Secure Boot.

## Function keys
{| class="wikitable"
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
|  ||  ||  ||  3
|-
|  ||  ||  || See note 4
|-
|  ||  ||  ||  (Next)
|-
|  ||  ||  ||  (Prior)
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|}

# The key is visible to  and similar tools.
# The physical key has a symbol on it, which describes its function.
# This firmware-managed key cycles between keyboard backlight modes.
# To remap this key, follow the steps described in Keyboard input#Identifying scancodes and Map scancodes to keycodes#Using setkeycodes.

## Power management
Enabling battery conservation mode as described in Lenovo#Battery conservation mode will limit the maximum charge to 80%. TLP also supports this method using options described on the vendors page.

## Disabling redundant WMI drivers
Some kernel modules targeted at Lenovo devices are not used by this ultrabook, such as  and . If these modules fail to load during boot, you can safely blacklist them.

## Fingerprint reader
The supplied fingerprint reader enforces the Secure Device Connection Protocol, and refuses to store fingerprints if the protocol is not followed. Currently, SDCP is not supported by Fprint, but  enrolling and storing fingerprints is possible using the custom script.

You will need to install , , , and . Installing Fprint is not required for this operation.

Save the script as  and comment out lines 500-502 (inclusive):
{{hc|./egismoc-sdcp-1c7a-0583.py|
reconnect_response_raw  egismoc_sdcp_reconnect()
print(f"egismoc SDCP ReconnectResponse: {reconnect_response_raw.tobytes().hex(' ')}")
verify_sdcp_reconnect_response(keys, reconnect_response_raw)
}}

Make the following additional changes to lines 48 and 58, respectively:

After making these changes, it should be possible to enroll fingerprints.
