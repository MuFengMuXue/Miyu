# TUXEDO InfinityBook 14 Gen10

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
| Ethernet ||  ||
|-
| Bluetooth || ||
|-
| SD card reader || ||
|-
| Audio ||  ||
|-
| Wi-Fi ||  ||
|}

Tuxedo lists a few troubleshooting issues on their device-specific FAQ

See also the official advice from Tuxedo regarding recommended packages for Arch Linux

## Keyboard
The internal keyboard may not function on resume from suspend, as noted in the FAQ linked above. Below you can find the kernel parameters required:

 i8042.reset i8042.nomux i8042.nopnp i8042.noloop

## Keyboard backlight
TUXEDO provides a driver for this. It can be installed with .

## Ethernet
The laptop has a built in Motorcomm YT6801 LAN chipset. The package  provides a kernel module for ethernet functionality. It is built from the official Tuxedo GitLab Repo.

## Function keys
The function keys should be recognised automatically once  is installed, with an exception for F3. This key could be programmed to run the Tuxedo Control Centre binary or for other purposes

{| class="wikitable"
|-
! Key
! Visible?1
! Marked?2
! Effect
|-
|Fn+Esc ||  ||   || Toggles Fn lock
|-
|Fn+F1 ||  ||  ||
|-
|Fn+F2 ||  ||  ||
|-
|Fn+F3 ||  ||  || Open Tuxedo Control Centre
|-
|Fn+F4 ||  ||  ||
|-
|Fn+F5 ||  ||  ||
|-
|Fn+F6 ||  ||  ||
|-
|Fn+F7 ||  ||  ||
|-
|Fn+F8 ||  ||  ||
|-
|Fn+F9 ||  ||  || Toggles display on/off
|-
|Fn+F10 ||  ||  ||
|-
|Fn+F11 ||  ||  ||
|-
|Fn+F12 ||  ||  ||
|}

# The key is visible to  and similar tools
# The physical key has a symbol on it, which describes its function

## Power management
As advised above by Tuxedo you can install the official  to let it control the fan speed and CPU frequency. The package will create and enable the systemd service , which is all that is needed for the laptop to activate the power management options chosen.

To change the power management options, and select different profiles according to the battery status (running on battery power or plugged in), a GUI binary  is provided.
