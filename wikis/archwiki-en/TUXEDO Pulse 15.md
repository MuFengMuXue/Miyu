# TUXEDO Pulse 15

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
| Fn Keys || ||
|}

## Function keys
Most of the function keys should be recognised automatically once  is installed.

{| class="wikitable"                    |
|--------------------------------------|
!Key!! Visible? !! Marked? !! Effect
|-
|Fn+Esc ||  ||   || Toggles Fn lock
|-
|Fn+F1 ||  ||  ||
|-
|Fn+F2 ||  ||  ||
|-
|Fn+F3 ||  ||  ||
|-
|Fn+F4 ||  ||  ||
|-
|Fn+F5 ||  ||  ||
|-
|Fn+F6 ||  ||  || Marked to launch  but is recognized by   as
|-
|Fn+F7 ||  ||  ||
|-
|Fn+F8 ||  ||  ||
|-
|Fn+F9 ||  ||  || Toggles the touchpad on/off
|-
|Fn+F10 ||  ||  ||
|-
|Fn+F11 ||  ||  || Recognized as
|-
|Fn+F12 ||  ||  ||
|}

## Video
The Pulse 15 comes with a Ryzen 7 4800H CPU, which includes a Renoir GPU. The laptop works with the open source  driver.

## Keyboard backlight
TUXEDO furnishes a driver for this. It can be installed from source or with .

## Power management
It is advisable to install the official  to let it control the fan speed and CPU frequency. The package will install and enable , which is all that is needed for the laptop to activate the power management options chosen.

To actually change them, select different profiles according to the battery status (running on battery power or plugged in), a GUI binary is also furnished, .
