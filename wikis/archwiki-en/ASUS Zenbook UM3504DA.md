# ASUS Zenbook UM3504DA

{| class="wikitable archwiki-table-laptop"
|-
! Hardware !! PCI/USB ID !! Working?
|-
| Touchpad || ||
|-
| Keyboard || ||
|-
| SSD ||  ||
|-
| GPU ||  ||
|-
| Webcam ||  ||
|-
| Wi-Fi/Bluetooth ||  ||
|-
| Audio ||  ||
|-
|}

## Wi-Fi/Bluetooth adapter
Mediatek MT7922 card has some issues such as high ping or being unable to connect to some 5Ghz networks or having high ping (up to 20ms) on kernel version newer than 6.1. The solution for this particular problem  was implemented in March of 2024 with the new  firmware. No new issues were encountered on that version.

## Battery charge treshold
Asus's smarty battery charging is working. Battery will stop charging once when it reaches values designed in  However, once when the designed value is reached, system will correctly report  status, but the value will be offset by 1 (e.g. 79% will be displayed instead of 80%). Unfortunately, charge treshold is automatically set to 100% on boot, this may be solved with systemd service: refer to Laptop/ASUS#Battery charge threshold

## Function keys
{| class="wikitable"
|-
! Key
! Visible
! Marked
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
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  || Toggles keyboard backlight level (three stages)
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
|}

## Known issues
There are some issues on this laptop (observed on kernels 6.5, 6.7 - 6.8 untested on other version )
* Laptop will suddenly jump to 100% usage on both fans, only solution is forceful shutdown (pressing Power button for 40 second). Also, it is unresponsive to REISUB or any other keyboard shortcut in that state.
* While powered on, CPU fan will sometimes turn on to 5000 - 6000 RPM for a few seconds, even when it is not under load, and temperatures are under 35°C.
