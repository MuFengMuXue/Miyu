# HP EliteBook 745 G4

{| class="wikitable archwiki-table-laptop"
! Hardware !! PCI/USB ID !! Working?
|-
| Bluetooth || ||
|-
| Webcam || ||
|-
| Ethernet || ||
|-
| Wi-Fi || ||
|-
| GPU (AMD) || ||
|-
| Touchpad || ||
|-
| Pointing stick || ||
|-
| Keyboard || ||
|-
| TPM || ||
|-
| Fingerprint reader || ||
|-
| SD-card reader || ||
|-
| Speakers || ||
|-
| Microphone || ||
|-
| Smartcard Reader || ||
|-
| 4G modem || ||
|-
| Dock || ||
|-
|}

## Function keys
{| class="wikitable"
|-
! Key
! Visible?1
! Marked?2
! Effect
|-
|  ||  ||  ||
|-
|  || 3 ||  ||
|-
|  || ||  || Adjust keyboard backlight (HIGH->LOW->OFF)
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

# The key is visible to  and similar tools
# The physical key has a symbol on it, which describes its function
# systemd-logind handles this by default

## Smartcard Reader
Works perfectly with  . Read Smartcards for more info.

## 4G modem
Works fine, can be controlled via nmcli / nmtui or GNOME settings.

Tested with HP lt4132, but lt4120 and hs3210 should be supported too. (Check manual for more information)
